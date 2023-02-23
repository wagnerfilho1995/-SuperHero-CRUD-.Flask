from flask import request
from flask_restful import Resource

from domain.schema import HeroIn
from service.service import get_heroes, get_hero_by_id, save_hero, update_hero, delete_hero


class Hero(Resource):
    @staticmethod
    def get(hero_id: str):
        result = get_hero_by_id(hero_id)
        return result

    @staticmethod
    def put(hero_id: str):
        request_in = HeroIn().load(request.get_json())
        hero = update_hero(hero_id, request_in)
        return hero

    @staticmethod
    def delete(hero_id: str):
        result = delete_hero(hero_id)
        return result


class HeroList(Resource):
    @staticmethod
    def get():
        result = get_heroes()
        return result

    @staticmethod
    def post():
        request_in = HeroIn().load(request.get_json())
        hero = save_hero(request_in)
        return hero
