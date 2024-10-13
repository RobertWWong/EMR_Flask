import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    App = Flask(__name__, instance_relative_config=True)
    App.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(App.instance_path, 'flaskr.sqlite'),
    )
    if test_config is None:
        # load the instance config, if it exists, when not testing
        App.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        App.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(App.instance_path)
    except OSError:
        pass
    return App


app = create_app()
