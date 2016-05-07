import mock
from unittest import TestCase
from acmdrunner import CommandDispatcher


class CommandExample(object):

    def execute(self, *args, **kwargs):
        pass


class CommandDispatcherTestCase(TestCase):

    def setUp(self):
        self.command_dispatcher = CommandDispatcher()

    def register_command(self):
        self.command_dispatcher.register_command('test', CommandExample)

    def test_is_exists(self):
        self.register_command()
        self.assertTrue(
            self.command_dispatcher.is_exists('test'),
            'The command test is not registered'
        )

    def test_execute_command(self):
        with mock.patch(
                'tests.test_command_dispatcher.CommandExample',
                autospec=True
        ) as command_mock:
            self.register_command()
            self.command_dispatcher.execute_command('test', '1', '2', ert=1)
            self.assertEquals(
                command_mock.method_calls[0],
                mock.call().execute('1', '2', ert=1)
            )
