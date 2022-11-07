import time

class Timer:
    def __init__(self):
        self.ref_time = int(time.time())
        self.current_time = 0

    def __setCurrentTime(self):
        self.current_time = int(time.time())

    def getTimeDifference(self):
        self.__setCurrentTime()
        return self.current_time - self.ref_time
