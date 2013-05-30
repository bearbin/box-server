#! /usr/bin/python3

# Imports

import subprocess
from serverbasics import OperationFailedError
import sys
from threading import Thread
from queue import Queue, Empty

# Setup code

def enqueue_output(out, queue):
    for line in iter(out.readline, b''):
        queue.put(line)
    out.close()

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
            self.q = Queue()
            self.t = Thread(target=enqueue_output, args=(self.serverprocess.stdout, self.q))
            self.t.daemon = True
            self.t.start()
            self.started = 1
            return		

    def stop(self):
        """Stops the server."""
        if self.started == 0:
            raise OperationFailedError({"operation":"stop", "cause":"notstarted", "details":None})
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
            self.serverprocess.stdin.write(bytes(args+"\n", "UTF-8"))
            self.serverprocess.stdin.flush()

if __name__ == "__main__":
    print("This is the MCServer module for box-server. DERP")
