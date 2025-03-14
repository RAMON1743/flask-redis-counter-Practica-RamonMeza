"""Módulo para inicializar la conexión con Redis."""

import os
from redis import Redis

def get_redis_client():
    """Retorna una instancia del cliente Redis."""
    redis_host = os.getenv("REDIS_HOST", "redis-server")  # Usa "redis-server" para Docker
    redis_port = int(os.getenv("REDIS_PORT", 6379))  # Permite cambiar el puerto mediante variable de entorno
    
    return Redis(host=redis_host, port=redis_port, db=0, decode_responses=True)
