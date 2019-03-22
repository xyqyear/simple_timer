# -*- coding:utf-8 -*-
import time


class Timer:
    def __init__(self):
        self.is_started = False
        self.start_time = 0
        self.stop_timer = 0

    def start(self):
        self.is_started = True
        self.start_time = time.time()

    def stop(self):
        self.is_started = False
        self.stop_timer += time.time() - self.start_time

    def time(self):
        return self.stop_timer + time.time() - self.start_time if self.is_started \
          else self.stop_timer

    def reset(self):
        self.__init__()
