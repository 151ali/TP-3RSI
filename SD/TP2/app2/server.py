from flask import Flask

app = Flask(__name__)

@app.route('/')
def greeting():
    return "Hello, world from app 2!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5002')