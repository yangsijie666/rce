import os
import signal
from executor import CommandExecutor
from rce import logger


class Manager(object):

    def __init__(self):
        """Command Executor Manager."""
        self.executors = []

    def _generate_executor(self, cmds):
        """
        Generate a command executor.
        :param cmds: commands which need to be executed
        :return:
        """
        return CommandExecutor(cmds)

    def execute_commands(self, cmds):
        """
        Execute commands.
        :param cmds: commands which need to be executed
        :return:
        """
        executor = self._generate_executor(cmds)
        executor.start()
        self.executors.append(executor)

    def clear_executors(self):
        """
        Clear all executors.
        :return:
        """
        for executor in self.executors:
            try:
                executor_pid = executor.pid
                os.kill(executor_pid, signal.SIGTERM)
                logger.info('Pid: {pid} is about to exit.'.format(pid=str(executor_pid)))
                executor.join()
                logger.info('Pid: {pid} has exited.'.format(pid=str(executor_pid)))
            except OSError:
                continue
        # empty the list
        self.executors = []
