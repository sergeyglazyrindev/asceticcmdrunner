import mock
from acmdrunner import Loader
import os
import tests.management.acr_commands

cur_dir = os.path.dirname(__file__)


def test_load_from_directory():
    with mock.patch(
            'acmdrunner.loader.load_commands_from_directory',
            autospec=True
    ) as commands_mock:
        Loader.load_from_directory(cur_dir)
        commands_mock.assert_called_once_with(cur_dir)


def test_load_from_package():
    with mock.patch(
            'acmdrunner.loader.load_commands_from_directory',
            autospec=True
    ) as commands_mock:
        Loader.load_from_package('tests')
        commands_mock.assert_called_once_with(cur_dir, package='tests')


def test_integration():
    Loader.load_from_directory(cur_dir)
    assert (tests.management.acr_commands.command_dispatcher
            .is_registered('test'))
