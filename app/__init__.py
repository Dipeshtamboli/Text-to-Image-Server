from flask import Flask
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize the TextToImageModel
    from app.model import TextToImageModel
    app.model = TextToImageModel(app.config['MODEL_ID'])
    
    # Register blueprints
    from app.routes import main
    app.register_blueprint(main)
    
    return app
