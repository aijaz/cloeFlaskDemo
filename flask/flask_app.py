from flask import Flask

my_flask_app = Flask(__name__)


@my_flask_app.route("/cloe")
def cloe():
    return "Hello, Cloe"


if __name__ == "__main__":
    my_flask_app.run(host='0.0.0.0', port=8000, debug=True)
