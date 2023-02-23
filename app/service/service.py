from datetime import datetime
from uuid import uuid4

from apiflask import abort
from flask import Response
from pony.orm import db_session

from domain.model import Hero, CardHero
from domain.schema import HeroOutAll, HeroOut, CardSkills
from repository.mysql_repository import MySqlRepository

db = MySqlRepository()


def build_hero(id_hero: str, hero: dict):
    del hero['skills']
    return Hero(id_hero=id_hero, created_at=datetime.now(), **hero)


def build_card_hero(id_hero: str, skills: dict):
    return CardHero(id_hero=id_hero, **skills)


@db_session
def save_hero(hero: dict) -> HeroOut | Response:
    # Generate an uuid to the new hero
    id_hero = str(uuid4())

    # Transform into the model that can save in database
    card_hero_model = build_card_hero(id_hero, hero['skills'])

    # Transform into the model that can save in database
    hero_model = build_hero(id_hero, hero)

    db.save(hero_model, card_hero_model)

    # Check if hero was really saved
    new_hero, new_card = db.find_by_id(id_hero)
    if not new_hero:
        return Response(f"Hero {id_hero} not found", status=404)

    skills_schema = CardSkills()
    skills = skills_schema.dump(new_card)

    hero_schema = HeroOut()
    hero = hero_schema.dump(new_hero)

    return HeroOut().dump(dict(hero, skills=skills))


@db_session
def update_hero(hero_id: str, hero: dict):
    hero_from_db, card_from_db = db.find_by_id(hero_id)
    if not hero:
        raise abort(404, f"Hero {hero_id} not found")

    hero_from_db.name = hero['name']
    hero_from_db.nickname = hero['nickname']
    hero_from_db.age = hero['age']
    hero_from_db.universe = hero['universe']

    card_from_db.force = hero['skills']['force']
    card_from_db.speed = hero['skills']['speed']
    card_from_db.defense = hero['skills']['defense']
    card_from_db.knowledge = hero['skills']['knowledge']
    card_from_db.technology = hero['skills']['technology']
    card_from_db.magic = hero['skills']['magic']

    db.update(hero_from_db, card_from_db)

    up_hero, up_card = db.find_by_id(hero_id)
    if not up_hero:
        return Response(f"Hero {hero_id} not found", status=404)

    skills_schema = CardSkills()
    skills = skills_schema.dump(up_card)

    hero_schema = HeroOut()
    hero = hero_schema.dump(up_hero)

    return HeroOut().dump(dict(hero, skills=skills))


@db_session
def get_heroes():
    result = db.find_all()
    schema = HeroOutAll(many=True)
    heroes = schema.dump(result)

    return heroes


@db_session
def get_hero_by_id(id_hero: str):
    hero, card = db.find_by_id(id_hero)
    if not hero:
        return Response(f"Hero {id_hero} not found", status=404)

    skills_schema = CardSkills()
    skills = skills_schema.dump(card)

    hero_schema = HeroOut()
    hero = hero_schema.dump(hero)

    return HeroOut().dump(dict(hero, skills=skills))


@db_session
def delete_hero(hero_id: str):
    hero = db.find_by_id(hero_id)
    if not hero:
        return Response(f"Hero {hero_id} not found", status=404)

    db.delete_hero(hero_id)
