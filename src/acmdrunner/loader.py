import importlib
import os
from pathlib import Path


class Loader(object):

    def __init__(self, project_path, package_name=None):
        self.project_path = project_path
        self.package_name = package_name

    def load(self):
        _mod_name = 'acr_commands'
        for management_dir in Path(self.project_path).glob('*/management'):
            if not management_dir.is_dir():
                continue
            management_dirs = os.fsdecode(bytes(management_dir)).split(os.sep)
            module_name = '.'.join(management_dirs[-2:])
            if self.package_name:
                module_name = self.package_name + '.' + module_name
            try:
                importlib.import_module(module_name + '.' + _mod_name)
            except ImportError:
                print('Error while importing module: {}'.format(module_name + '.' + _mod_name))
