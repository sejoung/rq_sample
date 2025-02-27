import redis

from sejoung.producer.produce import produce


def test_produce(redis_container_url: str):
    produce(redis_container_url)
    with redis.from_url(redis_container_url) as client:
        actual = client.llen("rq:queue:default")

    assert actual == 1

def test_produce2(redis_container_url: str):
    produce(redis_container_url)
    with redis.from_url(redis_container_url) as client:
        actual = client.llen("rq:queue:default")

    assert actual == 1
