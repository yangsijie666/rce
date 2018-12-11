import subprocess
import signal


class API(object):

    def __init__(self, logger=None):
        self.sub_processes = []
        self.logger = logger

    def _signal_handler(self, signum, frame):
        """
        Signal processing function.
        :param signum:
        :param frame:
        :return:
        """
        for sub_process in self.sub_processes:
            sub_process.terminate()
        if self.logger is not None:
            self.logger.debug('All commands process has been finished.')

    def execute_and_return(self, cmd):
        """
        Execute the command and return the execution result.
        :param cmd: commands needs to be executed
        :return:
        """
        signal.signal(signal.SIGTERM, self._signal_handler)

        if self.logger is not None:
            self.logger.debug('Command: \'' + cmd + '\' is about to be executed.')

        child = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        self.sub_processes.append(child)
        ret = child.communicate()

        if ret[0] == '' and ret[1] != '':
            if self.logger is not None:
                self.logger.debug('Command: \'' + cmd + '\' is illegal.')
            return None
        elif ret[1] == '':
            if self.logger is not None:
                self.logger.debug(
                    'Command: \'' + cmd + '\' has been applied and return the following: \n' + ret[0])
            return ret[0]
        else:
            if self.logger is not None:
                self.logger.debug(
                    'Command: \'' + cmd + '\' may be illegal, but return the following: \n' + ret[0])
            return ret[0]
