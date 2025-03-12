from redis import Redis

def get_redis_client():
    return Redis(host='redis', port=6379, db=0, decode_responses=True)
