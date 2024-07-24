from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from models import FavoriteLocation, User

users_bp = Blueprint('users', __name__)

@users_bp.route('/favorites', methods=['GET'])
@jwt_required()
def get_favorite_locations():
    user_identity = get_jwt_identity()
    user = User.query.filter_by(id=user_identity['id']).first()
    favorites = FavoriteLocation.query.filter_by(user_id=user.id).all()
    return jsonify([{'city': fav.city, 'country': fav.country} for fav in favorites]), 200

@users_bp.route('/favorites', methods=['POST'])
@jwt_required()
def add_favorite_location():
    data = request.get_json()
    user_identity = get_jwt_identity()
    user = User.query.filter_by(id=user_identity['id']).first()
    favorite_location = FavoriteLocation(city=data['city'], country=data['country'], user=user)
    db.session.add(favorite_location)
    db.session.commit()
    return jsonify({'message': 'Favorite location added successfully!'}), 201
