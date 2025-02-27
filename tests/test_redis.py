from testcontainers.redis import RedisContainer


def test_redis():
    with RedisContainer() as redis_container:
        client = redis_container.get_client()
        client.set("my_key", "my_value")
        actual = client.get("my_key")

        assert actual == b"my_value"
