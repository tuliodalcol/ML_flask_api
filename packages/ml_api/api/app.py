from flask import Flask
from api.config import get_logger


_logger = get_logger(logger_name=__name__)


def create_app(*, config_object) -> Flask:
    """Create a flask app instance."""

    app = Flask(__name__)
    app.config.from_object(config_object)

    # import blueprints
    from api.controller import prediction_app
    app.register_blueprint(prediction_app)
    _logger.debug('Application instance created')

    return app

