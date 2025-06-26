from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from DevOps Master Project! SHADAB IS THE BEST HE CAN CONQUER ANYTHIGN YESSSSSSSSS!!! U MUST BELIVE !!!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
