from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "我爱特朗普"


if __name__ == '__main__':
    app.run()
