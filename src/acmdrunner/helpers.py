_CMD_RUNNERS = {}


def register_command(name, runner):
    if name in _CMD_RUNNERS:
        raise ValueError('command {} already registered'.format(name))
    _CMD_RUNNERS[name] = runner


def execute_command(name, *params, **param_kwargs):
    if name not in _CMD_RUNNERS:
        raise ValueError('command {} is not loaded yet'.format(name))
    _CMD_RUNNERS[name]().execute(*params, **param_kwargs)


def is_command_exists(name):
    return name in _CMD_RUNNERS


def list_all_commands():
    print("\n".join(_CMD_RUNNERS.keys()))
