# -*- coding: utf-8 -*-
import os
import unittest

from jinja2.exceptions import SecurityError

from inkpy_jinja.converter import Converter
from inkpy_jinja.backends.libre import LibreOfficePDFBackend

SAMPLES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'samples'))
SAMPLE_TXT = os.path.join(SAMPLES_DIR, 'sample.txt')
SAMPLE_NOT_SAFE_TXT = os.path.join(SAMPLES_DIR, 'sample_not_safe.txt')


class ConverterTests(unittest.TestCase):
    def _get_converter(self, data, file=SAMPLE_TXT):
        return Converter(
            SAMPLE_TXT, '', data,
            backend=LibreOfficePDFBackend
        )

    def test_jinja_renderer(self):
        c = self._get_converter(data={'id': 123, 'test': '1234'})
        result = c._jinja_renderer(open(SAMPLE_TXT, 'rb').read())
        self.assertEqual(result, 'Lorem ipsum 1234')

    def test_jinja_renderer_not_safe(self):
        c = self._get_converter(data={'id': 123})
        with self.assertRaises(SecurityError):
            c._jinja_renderer(open(SAMPLE_NOT_SAFE_TXT, 'rb').read())


if __name__ == '__main__':
    unittest.main()
