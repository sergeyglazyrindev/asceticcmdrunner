import mock
from src import run_command

from unittest import TestCase


class TestLoader(TestCase):

    @mock.patch('tests.management.acr_commands.TestCommand.execute')
    def test(self, mocked_command):
        run_command('test', 'dsdas')
        self.assertEqual(
            mocked_command.call_args[0],
            ('dsdas', )
        )
