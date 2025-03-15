"""Módulo para inicializar la conexión con Redis."""

import os
from redis import Redis


def get_redis_client():
    """Retorna una instancia del cliente Redis."""
    redis_host = os.getenv("REDIS_HOST", "redis-server")
    redis_port = os.getenv("REDIS_PORT", "6379")

    return Redis(
        host=redis_host,
        port=int(redis_port),
        db=0,
        decode_responses=True
    )
