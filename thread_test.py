from threading import Thread, local
from time import sleep

class ThreadedObject(Thread):
    def run(self):
        while (True):
            print "I am a ThreadedObject", self.getName()
            sleep(1)


if __name__ == "__main__":
    to1 = ThreadedObject().start()
    to2 = ThreadedObject().start()
