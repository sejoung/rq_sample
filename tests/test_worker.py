import os
from multiprocessing import Process

import kill_worker
from sejoung.consume.hello_worker import start_worker
from sejoung.producer.produce import produce


def test_worker(redis_container_url: str):
    produce(redis_container_url)
    p = Process(target=kill_worker.kill_worker, args=(os.getpid(), False))
    p.start()
    start_worker(redis_container_url)
    p.join(1)
    assert not p.is_alive()
