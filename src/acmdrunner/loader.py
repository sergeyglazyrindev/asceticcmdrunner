import importlib
import os
from pathlib import Path


def load_commands_from_directory(project_path, prefix=None):
    _mod_name = 'acr_commands'
    for management_dir in Path(project_path).glob('*/management'):
        if not management_dir.is_dir():
            continue
        management_dirs = os.fsdecode(bytes(management_dir)).split(os.sep)
        module_name = '.'.join(management_dirs[-2:])
        if prefix:
            module_name = prefix + '.' + module_name
        try:
            importlib.import_module(module_name + '.' + _mod_name)
        except ImportError:
            print('Error while importing module: {}'.format(module_name + '.' + _mod_name))


class Loader(object):

    @classmethod
    def load_from_directory(cls, project_path):
        load_commands_from_directory(project_path)

    @classmethod
    def load_from_package(cls, package_name):
        package = importlib.import_module(package_name)
        project_path = os.path.dirname(package.__file__)
        load_commands_from_directory(project_path, prefix=package_name)
