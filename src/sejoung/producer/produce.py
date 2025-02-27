from redis import Redis

from rq import Queue


def produce(_url: str):
    conn = Redis.from_url(_url)
    q = Queue(connection=conn, default_timeout=1)
    q.enqueue('math.factorial', 5)
