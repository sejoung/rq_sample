import os
import signal
import time


def kill_worker(pid: int, double_kill: bool, interval: float = 1.5):
    # wait for the worker to be started over on the main process
    time.sleep(interval)
    os.kill(pid, signal.SIGTERM)
    if double_kill:
        # give the worker time to switch signal handler
        time.sleep(interval)
        os.kill(pid, signal.SIGTERM)
