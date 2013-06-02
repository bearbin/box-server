#! /usr/bin/python3

# Imports

import subprocess
import os.path
from os import remove
import serverbasics

OperationFailedError = serverbasics.OperationFailedError

# Server start code.

class Server(serverbasics.Server):
    """Provides the interface for managing a MCServer server."""

    def start(self):
        """Starts the server."""
        if self.started == 1:
            raise OperationFailedError({"operation":"start", "cause":"alreadystarted", "details":None})
        else:
            self.logfile = open(os.path.join(self.location, ".boxservertemplog"), 'w')
            self.serverprocess = subprocess.Popen(["cd "+self.location+"; ./MCServer"], shell=True, stdin=subprocess.PIPE, stdout=self.logfile, stderr=subprocess.STDOUT)
            self.started = 1
            return		

    def stop(self):
        """Stops the server."""
        if self.started == 0:
            raise OperationFailedError({"operation":"stop", "cause":"notstarted", "details":None})
        else:
            self.serverprocess.communicate(input=bytes('stop\n', "UTF-8"))[0]
            self.started = 0
            self.logfile.close()
            os.remove(os.path.join(self.location, ".boxservertemplog"))
            if self.rotatelogs == 1:
                self.rotatelogs()
            if self.serverprocess.poll() != 0:
                raise OperationFailedError({"operation":"stop", "cause":"badexit", "details":None})

    def runcommand(self, args):
        """Runs the command 'args'."""
        if self.started == 0:
            raise OperationFailedError({"operation":"runcommand", "cause":"notstarted", "details":None})
        else:
            self.serverprocess.stdin.write(bytes(args+"\n", "UTF-8"))
            self.serverprocess.stdin.write(bytes("\n", "UTF-8")) # Workaround for strange behaiviour...

    def check():
        """Checks to see if the server is still running."""
        if self.serverprocess.poll() != None:
            return 1
        else:
            return 0

    def rotatelogs():
        """Rotate all those pesky logs the server has been generating."""
        return # doesn't do anything yet
