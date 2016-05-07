import mock
import os

from src.acmdrunner import Loader
from . import management

from unittest import TestCase


class TestLoader(TestCase):

    @mock.patch('tests.management.acr_commands.TestCommand.execute')
    def test(self, mocked_command):
        Loader.load_from_directory(os.path.dirname(__file__))
        management.acr_commands.command_dispatcher.execute_command(
            'test',
            'dsdas'
        )
        self.assertEqual(
            mocked_command.call_args,
            mock.call('dsdas', )
        )
