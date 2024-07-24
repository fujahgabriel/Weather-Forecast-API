from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
import requests
from app import db
from config import Config
from models import FavoriteLocation, User

weather_bp = Blueprint('weather', __name__)

@weather_bp.route('/current', methods=['GET'])
@jwt_required()
def get_current_weather():
    user_identity = get_jwt_identity()
    user = User.query.filter_by(id=user_identity['id']).first()
    favorites = FavoriteLocation.query.filter_by(user_id=user.id).all()
    weather_data = []
    for fav in favorites:
        response = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={fav.city},{fav.country}&appid={Config.WEATHER_API_KEY}')
        weather_data.append(response.json())
    return jsonify(weather_data), 200
