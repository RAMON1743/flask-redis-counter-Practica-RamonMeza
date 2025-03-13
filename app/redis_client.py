"""Módulo de conexión con Redis."""

import os
from redis import Redis

def get_redis_client():
    """Retorna una instancia del cliente Redis."""
    redis_host = os.getenv("REDIS_HOST", "localhost")
    return Redis(host=redis_host, port=6379, db=0, decode_responses=True)
