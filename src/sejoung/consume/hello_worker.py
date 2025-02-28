from redis import Redis
from rq import Worker


def start_worker(redis_url: str):
    with Redis.from_url(redis_url) as conn:
        print("start_worker")
        worker = Worker("default", connection=conn)
        worker.work()
        return worker
