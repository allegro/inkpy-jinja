from abc import ABCMeta, abstractmethod
from six import add_metaclass


@add_metaclass(ABCMeta)
class PDFBackend(object):
    def __init__(self, input_path, output_path, **kwargs):
        self.input_path = input_path
        self.output_path = output_path

    @abstractmethod
    def render(self):
        pass
