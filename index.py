from flask import Flask, render_template, request
import requests
import threading
import webbrowser
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', message="Hello from Flask!")

def open_browser():
      webbrowser.open_new('http://127.0.0.1:5000/')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    name = request.form['name']
    return f"Hello {name}, your form has been submitted successfully!"

@app.route('/api-data')
def api_data():
    response = requests.get('https://some-api.com/data')
    data = response.json()
    return render_template('api_data.html', data=data)

@app.errorhandler(400)
def bad_request(error):
    return render_template('400.html'), 400

@app.errorhandler(401)
def unauthorized(error):
    return render_template('401.html'), 401

@app.errorhandler(403)
def forbidden(error):
    return render_template('403.html'), 403

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return render_template('405.html'), 405

@app.errorhandler(408)
def request_timeout(error):
    return render_template('408.html'), 408

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

@app.errorhandler(502)
def bad_gateway(error):
    return render_template('502.html'), 502

@app.errorhandler(503)
def service_unavailable(error):
    return render_template('503.html'), 503






if __name__ == '__main__':
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        threading.Timer(1.25, open_browser).start()
    app.run(debug=True)