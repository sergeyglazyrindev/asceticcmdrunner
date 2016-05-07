from acmdrunner import BaseCommand
from acmdrunner.dispatcher import CommandDispatcher

command_dispatcher = CommandDispatcher()


class TestCommand(BaseCommand):

    def execute(self, *args):
        pass

command_dispatcher.register_command('test', TestCommand)
