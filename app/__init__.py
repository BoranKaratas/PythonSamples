from flask import Flask
from dotenv import load_dotenv
import os

def create_app():
    app = Flask(__name__)
    load_dotenv()

    # MongoDB bağlantısı (örnek)
    app.config['MONGO_URI'] = os.getenv('MONGO_URI')

    # Blueprint'leri kaydet
    from app.routes.user_routes import user_bp
    app.register_blueprint(user_bp, url_prefix='/api/users')

    return app