# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.utils.translation import get_language, activate

__all__ = (
    'switch_language',
)


class switch_language(object):
    """
    A contextmanager to switch the translation.

    NOTE: when the object is shared between threads, this is not thread-safe.

    It can be used to render objects in a different language, like::

        with switch_language('nl'):
            # execute code here with changed locale to 'nl'
    """

    def __init__(self, language_code=None):
        self.language = language_code
        self.old_language = get_language()

    def __enter__(self):
        # Be smarter then translation.override(), also avoid unneeded switches.
        if self.language != self.old_language:
            activate(self.language)

    def __exit__(self, exc_type, exc_value, traceback):
        if self.language != self.old_language:
            activate(self.old_language)
