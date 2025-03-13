import os
from redis import Redis

def get_redis_client():
    redis_host = os.getenv("REDIS_HOST", "localhost")  # Usar variable de entorno
    return Redis(host=redis_host, port=6379, db=0, decode_responses=True)
