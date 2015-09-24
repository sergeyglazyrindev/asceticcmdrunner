Ascetic Command Runner
=============

Not all of our projects are using either django or another *God* framework.
So, once we start our hobby project, would be great to put into the game some commands.
For example, maybe we need for our hobby project simple command test which loads custom TestRunner, etc
In this case this package maybe handy for you!

Installation
-----------

Simply run:
``bash
python setup.py install
``

Usage
-----------

In your django like manage.py command loader, you need to trigger following:
```python
import os
from acmdrunner import Loader

...
make all your preparations, initialize project settings, etc
...

Loader(os.path.dirname(__file__)).load()
```

Loader will search recursively in passed folder for folders with name management.
And try to load from folders found file acr_commands.py

An example of the file acr_commands.py:
```python
from src import register_command, BaseCommand


class TestCommand(BaseCommand):

    def execute(self, *args):
        pass

register_command('test', TestCommand)
```

register_command registers specific command and handler for this command.
You commands should implement execute method. Better to inherit from BaseCommand.
But as it is ascetic, you can simply pass class with execute method implemented.
That's all!

To run command, please trigger following call:
```python
from acmdrunner import run_command
run_command(command_name, *args, **kwargs)
```
