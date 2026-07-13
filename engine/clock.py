import time

class Clock:
    def __init__(self, fps):
        self.fps = fps
        self.target_frame_time = 1 / fps
        self.last_frame_time = time.perf_counter()


    def tick(self):
        # before sleep
        execute_time = time.perf_counter() - self.last_frame_time
        time_to_sleep = max(0, self.target_frame_time - execute_time)
        time.sleep(time_to_sleep)
        # after sleep
        current_time = time.perf_counter()
        delta_time = current_time - self.last_frame_time
        self.last_frame_time = current_time
        return delta_time