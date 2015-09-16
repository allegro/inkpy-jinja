from subprocess import call
import sys

from django.conf import settings

from inkpy.backends.base import PDFBackend


class OdtToPdfScriptPathNotConfigured(Exception):
    """OdtToPdf script path not found in settings"""


class ExternalRenderer(PDFBackend):
    def __init__(self, *args, **kwargs):
        super(ExternalRenderer, self).__init__(*args, **kwargs)
        if not settings.INKPY.get('script_path'):
            raise OdtToPdfScriptPathNotConfigured()
        self.script_path = settings.INKPY.get('script_path')

    def render(self):
        call([
            sys.executable,
            self.script_path,
            self.input_path,
            self.output_path,
        ])
