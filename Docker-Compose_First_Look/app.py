import os
from flask import Flask

app = Flask(__name__)

# Читаем переменные окружения
PORT = int(os.environ.get('APP_PORT', 8080))
PONG_MESSAGE = os.environ.get('PONG_MESSAGE', 'pong')

@app.route('/')
def ping():
    return f'{PONG_MESSAGE}\n'

@app.route('/ping')
def ping_endpoint():
    return f'{PONG_MESSAGE}\n'

@app.route('/health')
def health():
    return 'OK\n'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=False)