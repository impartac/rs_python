from flask import Flask
from flask import jsonify
from dotenv import dotenv_values
from flask import request
from controllers import operation


def get_port() -> int:
    config = dotenv_values(".env")
    return config.get("PORT", 5000)


app = Flask(__name__)


@app.route("/")
def server_info():
    return "Partac Server"


@app.route("/author")
def author():
    author = {
        "name": "Matvej Aparkin",
        "nick": "Partac",
        "course": 2,
        "age": 19,
    }
    return jsonify(author)


@app.route("/sum")
def runner():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return jsonify({'sum': operation(a, b)})


if __name__ == "__main__":
    app.run(debug=True, port=get_port())
