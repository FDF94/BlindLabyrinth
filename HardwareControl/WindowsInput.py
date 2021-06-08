from msvcrt import getwch, kbhit
from time import time


def handle_input() -> str:
    timeout = 1
    start_time = time()
    while True:
        if kbhit():
            return getwch().upper()
        elif time() - start_time > timeout:
            return ""
