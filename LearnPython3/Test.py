from flask import Flask, url_for()
app = Flask(__name__)


@app.route('/')
def index():
    return 'index!'


if __name__ == '__main__':
    app.run()



