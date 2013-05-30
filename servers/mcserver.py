#! /usr/bin/python3

# Imports

import subprocess
import serverbasics

# Server start code.

class Server():
    """Provides the interface for managing a MCServer server."""

    def __init__(self, filename):
        self.filename = filename
        self.started = 0 # The server is not started quite yet.

    def start(self):
        """Starts the server."""
        if self.started == 1:
            raise OperationFailedError({"operation":"start", "cause":"alreadystarted", "details":None})
        else:
            self.serverprocess = subprocess.Popen([self.filename], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            self.started = 1
            return		

    def stop(self):
        """Stops the server."""
        if self.started == 0:
            return
        else:
            output = self.serverprocess.communicate(input=bytes('stop\n', "UTF-8"))[0]
            if self.serverprocess.poll() != 0:
                raise OperationFailedError({"operation":"stop", "cause":"badexit", "details":None})
            self.started = 0

    def runcommand(self, args):
        """Runs the command 'args'."""
        if self.started == 0:
            raise OperationFailedError({"operation":"runcommand", "cause":"notstarted", "details":None})
        else:

if __name__ == "__main__":
    print("This is the MCServer module for box-server. DERP")
