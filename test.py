import time

from tasks import get_webpage

if __name__ == "__main__":
    while True:
        time.sleep(5)
        get_webpage.delay()
