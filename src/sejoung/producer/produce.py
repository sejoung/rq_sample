from redis import Redis

from rq import Queue


def produce(_host: str, _port: int):
    q = Queue(connection=Redis(host=_host, port=_port), default_timeout=1)
    q.enqueue('math.factorial', 5)
