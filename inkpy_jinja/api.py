import os
import tempfile
import uuid

from inkpy_jinja.converter import Converter
from inkpy_jinja.backends.libre import LibreOfficePDFBackend


def pdf(template, data):
    name = str(uuid.uuid4())
    tmp_path = os.path.join(
        tempfile.gettempdir(), '{}.tmp'.format(name)
    )
    template_path = tmp_path + '.template'
    tmp_pdf = tmp_path + '.pdf'
    with open(template_path, 'wb') as f:
        f.write(template)
    converter = Converter(
        template_path,
        tmp_pdf,
        data=data,
        backend=LibreOfficePDFBackend,
    )
    converter.convert()
    with open(tmp_pdf, 'rb') as f:
        return f.read()
