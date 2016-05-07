from acmdrunner.dispatcher import CommandDispatcher

command_dispatcher = CommandDispatcher()


def execute(*args):
    pass

command_dispatcher.register_command('test', execute)
