import mock
import os

from src.acmdrunner import Loader, run_command
from src.acmdrunner.helpers import _CMD_RUNNERS

from unittest import TestCase


class TestLoader(TestCase):

    @mock.patch('tests.management.acr_commands.TestCommand.execute')
    def test(self, mocked_command):
        Loader(os.path.dirname(__file__)).load()
        self.assertTrue('test' in _CMD_RUNNERS)
        run_command('test', 'dsdas')
        self.assertEqual(
            mocked_command.call_args[0],
            ('dsdas', )
        )
