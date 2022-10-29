import sys
from AppContext import AppContext


class LineOffsetStreamWrapper:
    UP = '\033[F'
    DOWN = '\033[B'

    def __init__(self, lines=0, stream=sys.stderr):
        self.stream = stream
        self.lines = lines

    def write(self, data):
        with AppContext.output_lock:
            self.stream.write(self.UP * self.lines)
            self.stream.write(data)
            self.stream.write(self.DOWN * self.lines)
            self.stream.flush()

    def __getattr__(self, name):
        return getattr(self.stream, name)