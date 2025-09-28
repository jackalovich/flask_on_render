from flask import Flask

def create_app():
    # Create and configure the app
    app = Flask(__name__)

    # A simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, World from Render!'

    return app
