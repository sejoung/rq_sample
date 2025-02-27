import pytest
from testcontainers.redis import RedisContainer


@pytest.fixture(autouse=True)
def redis_container_url():
    """Start a Redis container."""
    with RedisContainer("redis:7.0") as redis:
        yield f"redis://{redis.get_container_host_ip()}:{redis.get_exposed_port(6379)}"
