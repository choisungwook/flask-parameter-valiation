from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route("/helloworld")
    def helloworld():
        return "hello world"

    return app