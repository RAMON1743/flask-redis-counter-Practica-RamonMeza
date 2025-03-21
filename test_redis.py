import redis

try:
    redis_client = redis.StrictRedis(host="localhost", port=6379, decode_responses=True)
    print("Conexión a Redis exitosa:", redis_client.ping())  # Debe imprimir True
except Exception as e:
    print(f"Error conectando a Redis: {e}")
