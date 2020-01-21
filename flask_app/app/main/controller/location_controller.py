from flask import request
from flask_restplus import Resource

from app.main.util.decorator import token_required
from ..util.dto import LocationDto
from ..service.location_service import save_location

api = LocationDto.api


@api.route('/')
class Location(Resource):
    @api.doc('location by ip addr')
    @token_required
    def get(self):
        return save_location(request.headers['X-Real-Ip'])
