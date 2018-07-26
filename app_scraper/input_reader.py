import sys

class InputReader:
    @staticmethod
    def get():
        del sys.argv[0]
        return sys.argv
