from testcontainers.redis import RedisContainer

from sejoung.producer.produce import produce


def test_produce():
    with RedisContainer() as redis:
        redis_container_ip_address = redis.get_docker_client().bridge_ip(redis._container.id)
        port = redis.port_to_expose
        produce(redis_container_ip_address, port)

        client = redis.get_client()
        actual = client.llen("rq:queue:default")

        assert actual == 1
