from src.acmdrunner import register_command, BaseCommand


class TestCommand(BaseCommand):

    def execute(self, *args):
        pass

register_command('test', TestCommand)
