from flask import Flask
<<<<<<< HEAD
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from DevOps Master Project! SHADAB IS THE BEST HE CAN CONQUER ANYTHIGN YESSSSSSSSS!!! U MUST BELIVE !!!"
=======
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Define a metric (Counter)
REQUEST_COUNT = Counter('app_requests_total', 'Total number of HTTP requests')

@app.route('/')
def hello():
    REQUEST_COUNT.inc()  # Increment metric
    return "Hello, world!"

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}
>>>>>>> master

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
