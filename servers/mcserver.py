#! /usr/bin/python3

# Imports

import subprocess
import os.path
from serverbasics import OperationFailedError

# Server start code.

class Server():
    """Provides the interface for managing a MCServer server."""

    def __init__(self, location):
        self.location = location
        self.started = 0 # The server is not started quite yet.

    def start(self):
        """Starts the server."""
        if self.started == 1:
            raise OperationFailedError({"operation":"start", "cause":"alreadystarted", "details":None})
        else:
            self.logfile = open(os.path.join(self.location, "supahlog3k"), 'a')
            self.serverprocess = subprocess.Popen([os.path.join(self.location, "MCServer")], stdin=subprocess.PIPE, stdout=self.logfile, stderr=subprocess.STDOUT)
            self.started = 1
            return		

    def stop(self):
        """Stops the server."""
        if self.started == 0:
            raise OperationFailedError({"operation":"stop", "cause":"notstarted", "details":None})
        else:
            self.serverprocess.communicate(input=bytes('stop\n', "UTF-8"))[0]
            self.logfile.close()
            if self.serverprocess.poll() != 0:
                raise OperationFailedError({"operation":"stop", "cause":"badexit", "details":None})
            self.started = 0

    def runcommand(self, args):
        """Runs the command 'args'."""
        if self.started == 0:
            raise OperationFailedError({"operation":"runcommand", "cause":"notstarted", "details":None})
        else:
            self.serverprocess.stdin.write(bytes(args+"\n", "UTF-8"))
            self.serverprocess.stdin.flush()
