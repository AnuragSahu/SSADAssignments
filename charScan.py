import signal,copy,sys,time
from random import randint

class CharScan():
    def __init__(self):
        import tty

    def __call__(self):
        import termios,tty
        fileDes = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fileDes)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)

        finally:
            termios.tcsetattr(fileDes,termios.TCSADRAIN, old_settings)

        return ch
