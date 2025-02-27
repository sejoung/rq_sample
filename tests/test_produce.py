import redis

from sejoung.producer.produce import produce


def test_produce(redis_container_url: str):
    produce(redis_container_url)
    client = redis.from_url(redis_container_url)
    actual = client.llen("rq:queue:default")
    assert actual == 1
