# -*- coding: utf-8 -*-
import unittest

from inkpy_jinja.converter import Converter, FileDoesNotExist


class ConverterTests(unittest.TestCase):

    def test_given_non_exist_template_should_raise_exception(self):
        with self.assertRaises(FileDoesNotExist):

        # OK = 'Maj 31, 2014'
        # source_file = output_path = 'unused_in_test'
        # test_data = {
        #     'id': 'mocked-id',
        #     'today': datetime.date(2014, 5, 31),
        # }
        # converter = MockedConverter(source_file, output_path, test_data)
        # file_content = "{{today}}"

        # rendered = converter._django_renderer(file_content)
        # self.assertNotIn('Maj', rendered)
        # converter.lang_code = 'pl'
        # rendered = converter._django_renderer(file_content)
        # self.assertEqual(rendered, OK)


if __name__ == '__main__':
    unittest.main()
