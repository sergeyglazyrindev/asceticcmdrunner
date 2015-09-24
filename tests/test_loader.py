import os

from src import Loader
from src.helpers import _CMD_RUNNERS

from unittest import TestCase


class TestLoader(TestCase):

    def test(self):
        Loader(os.path.dirname(__file__)).load()
        self.assertTrue('test' in _CMD_RUNNERS)
