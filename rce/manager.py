import os
import signal
from executor import CommandExecutor


class Manager(object):

    def __init__(self):
        """Command Executor Manager."""
        self.executor_pids = []

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
        self.executor_pids.append(executor.pid)
        executor.start()

    def clear_executors(self):
        """
        Clear all executors.
        :return:
        """
        for executor_pid in self.executor_pids:
            try:
                os.kill(executor_pid, sig=signal.SIGTERM)
            except OSError:
                continue
        # empty the list
        self.executor_pids = []
