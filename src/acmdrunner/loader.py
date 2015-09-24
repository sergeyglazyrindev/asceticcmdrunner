import glob
import imp
import os


class Loader(object):

    def __init__(self, project_path):
        self.project_path = project_path

    def load(self):
        cur_dir = os.getcwd()
        os.chdir(self.project_path)
        _mod_name = 'acr_commands'
        for management_dir in glob.glob('management'):
            full_path = os.path.abspath(os.path.join(self.project_path, management_dir))
            if not os.path.isdir(full_path):
                continue
            full_path = os.path.abspath(os.path.join(full_path, _mod_name + '.py'))
            with open(full_path, 'r') as fp:
                try:
                    mod = imp.find_module(_mod_name, [full_path])
                    if not mod:
                        imp.load_module(_mod_name, fp, full_path, ('.py', 'r', 1))
                except ImportError:
                    pass
        os.chdir(cur_dir)
