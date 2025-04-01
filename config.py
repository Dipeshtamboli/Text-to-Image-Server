import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Flask app config
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    
    # Model config
    MODEL_ID = os.environ.get('MODEL_ID') or "runwayml/stable-diffusion-v1-5"
    
    # Output directory for generated images
    OUTPUT_DIR = os.environ.get('OUTPUT_DIR') or os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app/static/images/generated')
    
    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
