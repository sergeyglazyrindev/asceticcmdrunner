import mock
import os

from src.acmdrunner import Loader, execute_command
from src.acmdrunner.helpers import _CMD_RUNNERS

from unittest import TestCase


class TestLoader(TestCase):

    @mock.patch('tests.management.acr_commands.TestCommand.execute')
    def test(self, mocked_command):
        Loader.load_from_directory(os.path.dirname(__file__))
        self.assertTrue('test' in _CMD_RUNNERS)
        execute_command('test', 'dsdas')
        self.assertEqual(
            mocked_command.call_args,
            mock.call('dsdas', )
        )
