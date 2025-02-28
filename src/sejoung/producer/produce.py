from redis import Redis

from rq import Queue


def produce(_url: str):
    conn = Redis.from_url(_url)
    q = Queue(name="default", connection=conn, default_timeout=1)
    q.enqueue('sejoung.consume.consume_func', 5)
    print("end produce")
