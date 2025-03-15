"""Módulo principal de la aplicación Flask para manejar un contador con Redis."""

from flask import Flask, render_template, request
from app.redis_client import get_redis_client

app = Flask(__name__)
redis_client = get_redis_client()

@app.route('/', methods=['GET', 'POST'])
def index():
    """Maneja las solicitudes GET y POST para la página principal."""
    if request.method == 'POST':
        action = request.form.get('action')
        if action == "incrementar":
            redis_client.incr('counter')
        elif action == "decrementar":
            redis_client.decr('counter')

    counter = int(redis_client.get('counter') or 0)

    # Determinar la clase de color según el valor del contador
    counter_class = "counter-positive" if counter >= 0 else "counter-negative"

    return render_template('index.html', counter=counter, counter_class=counter_class)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
