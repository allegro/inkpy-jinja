import os
import sys
from subprocess import call

from inkpy_jinja.backends.base import PDFBackend


class OdtToPdfScriptPathNotConfigured(Exception):
    """OdtToPdf script path not found in settings"""


class ExternalRenderer(PDFBackend):
    def __init__(self, *args, **kwargs):
        super(ExternalRenderer, self).__init__(*args, **kwargs)
        script_path = os.environ.get('INKPY_SCRIPT_PATH', None)
        if not script_path:
            raise OdtToPdfScriptPathNotConfigured()
        self.script_path = script_path

    def render(self):
        call([
            sys.executable,
            self.script_path,
            self.input_path,
            self.output_path,
        ])
