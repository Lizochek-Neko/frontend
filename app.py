from flask import Flask, render_template, request
import requests

app = Flask(__name__)

BACKEND_URL = 'http://127.0.0.1:5000'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    """Проксирует отправку текста на бэкенд."""
    text = request.form.get('text', '')
    try:
        resp = requests.post(f'{BACKEND_URL}/api/save', json={'text': text})
        return resp.json()
    except requests.exceptions.ConnectionError:
        return {'status': 'error', 'message': 'Бэкенд недоступен'}, 500

@app.route('/read', methods=['GET'])
def read():
    """Проксирует запрос чтения данных с бэкенда."""
    try:
        resp = requests.get(f'{BACKEND_URL}/api/read')
        return resp.json()
    except requests.exceptions.ConnectionError:
        return {'status': 'error', 'message': 'Бэкенд недоступен'}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)


#Frontend 1.0
# from flask import Flask, render_template, request
# import requests

# app = Flask(__name__)

# BACKEND_URL = 'http://127.0.0.1:5000'

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/send', methods=['POST'])
# def send():
#     """Проксирует запрос с фронтенда на бэкенд."""
#     text = request.form.get('text', '')
#     try:
#         resp = requests.post(
#             f'{BACKEND_URL}/api/save',
#             json={'text': text}
#         )
#         return resp.json()
#     except requests.exceptions.ConnectionError:
#         return {'status': 'error', 'message': 'Бэкенд недоступен'}, 500

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8080, debug=True)
