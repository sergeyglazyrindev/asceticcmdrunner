class CommandDispatcher(object):

    __slots__ = ('registered_commands')

    def __init__(self):
        self.registered_commands = {}

    def register_command(self, name, command_class):
        """Enables execution of the command with name `name`

        :param name: The name of the command
        :type name: string
        :param command_class: a class of the command to be executed
        :type command_class: acmdrunner.commandbase.CommandDispatcher
        :returns: None
        :rtype: None
        """
        if name in self.registered_commands:
            raise ValueError('command {} already registered'.format(name))
        self.registered_commands[name] = command_class

    def execute_command(self, name, *params, **param_kwargs):
        """Execute given command

        :param name: Name of the command to be executed
        :type name: string
        :returns: None
        :rtype: None
        """
        if name not in self.registered_commands:
            raise ValueError('command {} is not loaded yet'.format(name))
        self.registered_commands[name]().execute(*params, **param_kwargs)

    def is_exists(self, name):
        """Is exists given command

        :param name: Name of the command
        :type name: string
        :returns: None
        :rtype: None
        """
        return name in self.registered_commands

    def list_all_commands(self):
        """Prints all registered commands to stdout
        :returns: None
        :rtype: None
        """
        print("\n".join(self.registered_commands.keys()))
