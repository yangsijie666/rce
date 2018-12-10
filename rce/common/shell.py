import os
import subprocess


class API(object):

    def __init__(self, logger=None):
        self.logger = logger

    def execute(self, cmd):
        ret = os.system(cmd)
        if ret != 0:
            if self.logger is not None:
                self.logger.debug('Command: \'' + cmd + '\' is illegal.')
            return False
        else:
            if self.logger is not None:
                self.logger.debug('Command: \'' + cmd + '\' has been applied.')
            return True

    def execute_and_return(self, cmd):
        ret = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).communicate()

        if ret[0] == '' and ret[1] != '':
            if self.logger is not None:
                self.logger.debug('Command: \'' + cmd + '\' is illegal.')
            return None
        elif ret[1] == '':
            if self.logger is not None:
                self.logger.debug(
                    'Command: \'' + cmd + '\' has been applied and return the following: \'' + ret[0] + '\'.')
            return ret[0]
        else:
            if self.logger is not None:
                self.logger.debug(
                    'Command: \'' + cmd + '\' may be illegal, but return the following:\'' + ret[0] + '\'')
            return ret[0]
