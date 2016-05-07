class BaseCommand(object):

    def execute(self, *args, **kwargs):
        """The method is being called on command execution
        :returns: no result of the execution should be returned
        :rtype: None
        """
        raise NotImplementedError
