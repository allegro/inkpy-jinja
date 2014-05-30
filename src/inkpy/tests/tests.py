# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import datetime
import os
import unittest

import inkpy

os.environ['DJANGO_SETTINGS_MODULE'] = 'inkpy.tests.settings'


class MockedConverter(inkpy.Converter):
    def __init__(self, source_file, output_path, data, lang_code=None):
        self.data = data
        self.set_lang(lang_code)


class BaseTests(unittest.TestCase):

    def test__django_renderer(self):
        OK = 'Maj 31, 2014'
        source_file = output_path = 'unused_in_test'
        test_data = {
            'id': 'mocked-id',
            'today': datetime.date(2014, 5, 31),
        }
        converter = MockedConverter(source_file, output_path, test_data)
        file_content = "{{today}}"

        rendered = converter._django_renderer(file_content)
        self.assertNotIn('Maj', rendered)
        converter.lang_code = 'pl'
        rendered = converter._django_renderer(file_content)
        self.assertEqual(rendered, OK)


if __name__ == '__main__':
    unittest.main()
