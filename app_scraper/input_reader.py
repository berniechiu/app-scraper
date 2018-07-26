import sys

class InputReader:
    @staticmethod
    def parse_argv():
        del sys.argv[0]
        return sys.argv
