import multiprocessing
from common import shell
from rce import logger

shell_api = shell.API(logger)


class CommandExecutor(multiprocessing.Process):

    def __init__(self, cmds):
        """a Command Executor."""
        super(CommandExecutor, self).__init__()
        self.cmds = self._format_commands_to_list(cmds)
        self.daemon = True

    @classmethod
    def _format_commands_to_list(cls, cmds):
        """
        Format the commands as a list.
        :param cmds: commands
        :return: a list of commands
        """
        if isinstance(cmds, str):
            logger.debug('Input commands are str type: %s' % cmds)
            _cmds = cmds.split('\n')
        elif isinstance(cmds, list):
            logger.debug('Input commands are list type: %s' % str(cmds))
            _cmds = cmds
        else:
            cmds = str(cmds)
            logger.debug(
                'Input commands are neither str type nor list type, it will be forced to type to list: %s' % cmds)
            _cmds = cmds.split('\n')
        return _cmds

    def _execute(self):
        """
        Execute the command set.
        :return:
        """
        for cmd in self.cmds:
            if cmd != '':
                ret = shell_api.execute_and_return(cmd)
                if ret is not None:
                    logger.info('Command %s has been executed, and returned: \n%s\n' % (cmd, ret))

    def run(self):
        """
        Override the parent class method.
        :return:
        """
        self._execute()
