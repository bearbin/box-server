#!/ usr/bin/python3

# Code start

class OperationFailedError(Exception):
    pass

class Server():
    """The base server class for stuff."""

    def __init__(self, location):
        self.location = location
        self.started = 0 # The server is not started quite yet.
        self.rotatelogs = 1 # Always rotate logs for now.