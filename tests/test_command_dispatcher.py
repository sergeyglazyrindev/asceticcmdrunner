import mock
from unittest import TestCase
from acmdrunner import CommandDispatcher


def execute_command(*args, **kwargs):
    pass


class CommandDispatcherTestCase(TestCase):

    def setUp(self):
        self.command_dispatcher = CommandDispatcher()

    def register_command(self):
        self.command_dispatcher.register_command('test', execute_command)

    def test_is_registered(self):
        self.register_command()
        self.assertTrue(
            self.command_dispatcher.is_registered('test'),
            'The command test is not registered'
        )

    def test_execute_command(self):
        with mock.patch(
                'tests.test_command_dispatcher.execute_command',
                autospec=True
        ) as command_mock:
            self.register_command()
            self.command_dispatcher.execute_command('test', '1', '2', ert=1)
            self.assertEquals(
                command_mock.call_args_list[0],
                mock.call('1', '2', ert=1)
            )
