import os
import six
import sys

if six.PY2:
    raise RuntimeError(
        'LibreOfficePDFBackend backends works only with Python 3.x'
    )

sys.path.append('/usr/lib/python3/dist-packages')

LIBRE_OFFICE_CONNECTION_PAIR = (
    os.environ.get('PDF_WORKER_LIBRE_HOST', '0.0.0.0'),
    int(os.environ.get('PDF_WORKER_LIBRE_PORT', '2002')),
)

try:
    from unotools import Socket, connect
    from unotools.component.writer import Writer
    from unotools.unohelper import convert_path_to_url
except:
    raise ImportError(
        'unotools package must be installed.'
        ' Run pip install inkpy_jinja[libre]'
    )
from inkpy_jinja.backends.base import PDFBackend


class LibreOfficeContext(object):
    def __init__(self, host, port, input_path):
        self.host = host
        self.port = port
        self.input_path = input_path

    def __enter__(self):
        context = connect(Socket(self.host, self.port))
        self.writer = Writer(context, convert_path_to_url(self.input_path))
        return self

    def __exit__(self, type, value, traceback):
        self.writer.close(True)

    def write(self, path):
        self.writer.store_to_url(
            convert_path_to_url(path),
            'FilterName',
            'writer_pdf_Export'
        )


class LibreOfficePDFBackend(PDFBackend):
    def render(self):
        host, port = LIBRE_OFFICE_CONNECTION_PAIR
        with LibreOfficeContext(host, port, self.input_path) as ctx:
            ctx.write(self.output_path)
