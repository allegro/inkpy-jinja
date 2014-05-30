#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import shutil
import sys
import zipfile

from subprocess import call

from django.conf import settings
from django.template import Context, Template

from inkpy.utils import switch_language


class Error(Exception):
    pass


class FileDoesNotExist(Error):
    """File to file does not exist"""


class IdDoesNotExist(Error):
    """Document id does not exist"""


class OdtToPdfScriptPathNotConfigured(Error):
    """OdtToPdf script path not found in settings"""


class Converter(object):
    """
    Fill special prepareted odt file with filled django style template
    tags and convert this file to pdf file.
    Conversion from odt to pdf file it's made with external command
    run in subprocess.call.

    :param source_file: The source odt file path.
    :param output_path: The destination pdf file path.
    :param data: The directory with data to fill template.
    :param lang_code: forces language during docs generation, if None then
        django's *settings.LANGUAGE_CODE* is used.
    """

    def __init__(self, source_file, output_path, data, lang_code=None):
        if not os.path.exists(source_file):
            raise FileDoesNotExist()
        self.source_file = source_file
        self.output_path = output_path
        output_path_without_ext = self.source_file[:-3]
        if not data.get('id'):
            raise IdDoesNotExist()
        if not settings.INKPY.get('script_path'):
            raise OdtToPdfScriptPathNotConfigured()
        self.script_path = settings.INKPY.get('script_path')
        self.output_odt_path = "{}odt".format(output_path_without_ext)
        self.data = data
        self.tmp_dir_master = settings.INKPY.get('tmp_dir', '/tmp/INKPY')
        self.tmp_dir = "{}/{}".format(self.tmp_dir_master, self.data['id'])
        self.set_lang(lang_code)

    def set_lang(self, lang_code):
        if not lang_code:
            lang_code = getattr(settings, 'LANGUAGE_CODE').split('-')[0]
        self.lang_code = lang_code

    def convert(self):
        self._convert()

    def _convert(self):
        """
        Flow:
        unzip odt file -> render content.xml -> zip to odt file ->
        convert odt to pdf -> remove temporary data
        """

        self.unzip_odt()
        self.render()
        self.zip_odt()
        self.to_pdf()
        self.remove_tmp()

    def remove_tmp(self):
        """Remove temporary unpaced odt and translated odt file"""
        shutil.rmtree(self.tmp_dir)
        os.remove(self.tmp_odt)

    def unzip_odt(self):
        if not os.path.exists(self.tmp_dir):
            os.makedirs(self.tmp_dir)
        with zipfile.ZipFile(self.source_file) as zf:
            zf.extractall(self.tmp_dir)

    def zip_odt(self):
        self.tmp_odt = '{}/{}'.format(
            self.tmp_dir_master, self.output_odt_path.split('/')[-1],
        )
        self.zip_dir(self.tmp_dir, self.tmp_odt, False)

    def render(self):
        content_xml = "{}/content.xml".format(self.tmp_dir)
        styles_xml = "{}/styles.xml".format(self.tmp_dir)

        def _render(file_name):
            with open(file_name, 'r') as f:
                content = f.read()
                new_content = self._django_renderer(content)
                f.close()
            with open(file_name, 'w') as f:
                f.write(new_content.encode("UTF-8"))
                f.close()
        _render(content_xml)
        _render(styles_xml)

    def _django_renderer(self, file_content):
        template = Template(file_content)
        context = Context(self.data)
        with switch_language(self.lang_code):
            rendered = template.render(context)
        return rendered

    def zip_dir(self, dirPath=None, zipFilePath=None, includeDirInZip=True):
        """Create a zip archive from a directory.

        Note that this function is designed to put files in the zip archive
        with either no parent directory or just one parent directory, so it
        will trim any leading directories in the filesystem paths and not
        include them inside the zip archive paths. This is generally the case
        when you want to just take a directory and make it into a zip file that
        can be extracted in differentlocations.

        Keyword arguments:

        dirPath -- string path to the directory to archive. This is the only
        required argument. It can be absolute or relative, but only one or zero
        leading directories will be included in the zip archive.

        zipFilePath -- string path to the output zip file. This can be an
        absolute or relative path. If the zip file already exists, it will be
        updated. If not, it will be created. If you want to replace it from
        scratch, delete it prior to calling this function. (default is computed
        as dirPath + ".zip")

        includeDirInZip -- boolean indicating whether the top level directory
        should be included in the archive or omitted. (default True)

        """

        if not zipFilePath:
            zipFilePath = dirPath + ".zip"
        if not os.path.isdir(dirPath):
            raise OSError(
                "dirPath argument must point to a directory. "
                "'%s' does not." % dirPath
            )
        parentDir, dirToZip = os.path.split(dirPath)

        def trimPath(path):
            # Little nested function to prepare the proper archive path
            archivePath = path.replace(parentDir, "", 1)
            if parentDir:
                archivePath = archivePath.replace(os.path.sep, "", 1)
            if not includeDirInZip:
                archivePath = archivePath.replace(
                    dirToZip + os.path.sep, "", 1,
                )
            return os.path.normcase(archivePath)

        outFile = zipfile.ZipFile(
            zipFilePath, "w", compression=zipfile.ZIP_DEFLATED,
        )
        for (archiveDirPath, dirNames, fileNames) in os.walk(dirPath):
            for fileName in fileNames:
                filePath = os.path.join(archiveDirPath, fileName)
                print(filePath)
                outFile.write(filePath, trimPath(filePath))
            # Make sure we get empty directories as well
            if not fileNames and not dirNames:
                zipInfo = zipfile.ZipInfo(trimPath(archiveDirPath) + "/")
                # Some web sites suggest doing zipInfo.external_attr = 16
                # or zipInfo.external_attr = 48. Here to allow for inserting
                # an empty directory. Still TBD/TODO.
                outFile.writestr(zipInfo, "")
        outFile.close()

    def to_pdf(self):
        """ Run external python file to provide convert odt file to pdf"""
        call([
            sys.executable,
            self.script_path,
            self.tmp_odt,
            self.output_path,
        ])
