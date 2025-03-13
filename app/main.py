"""Módulo principal de la aplicación Flask."""

from flask import Flask, render_template, request, redirect, url_for
from app.redis_client import get_redis_client

app = Flask(__name__)
redis_client = get_redis_client()

@app.route('/', methods=['GET', 'POST'])
def index():
    """Maneja las solicitudes GET y POST para la página principal."""
    if request.method == 'POST':
        redis_client.incr('counter')
        return redirect(url_for('index'))
    
    counter = redis_client.get('counter') or 0
    return render_template('index.html', counter=int(counter))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # No trailing whitespace
