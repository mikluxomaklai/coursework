from flask import Flask, render_template, request
from bp_posts.views import bp_posts


def create_and_config_app(config_pyth):

    app = Flask(__name__)
    app.register_blueprint(bp_posts)
    app.config.from_pyfile(config_pyth)
    return app


app = create_and_config_app("config.py")



app.run()

