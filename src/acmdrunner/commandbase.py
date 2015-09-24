class BaseCommand(object):

    def execute(self, *args, **kwargs):
        raise NotImplementedError
