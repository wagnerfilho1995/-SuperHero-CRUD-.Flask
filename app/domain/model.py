import os
from datetime import datetime
from pony.orm import Database, set_sql_debug, PrimaryKey, Required, Optional

db = Database()


class Hero(db.Entity):
    __table__ = 'tb_hero'
    id_hero = PrimaryKey(str, auto=True)
    name = Optional(str, nullable=True)
    nickname = Required(str)
    age = Optional(int, nullable=True)
    universe = Optional(str, nullable=True)
    created_at = Optional(datetime, nullable=True, volatile=True)


class CardHero(db.Entity):
    __table__ = 'tb_card_hero'
    id_hero = PrimaryKey(str, auto=True)
    force = Required(int)
    speed = Required(int)
    defense = Required(int)
    knowledge = Required(int)
    technology = Required(int)
    magic = Required(int)


db.bind(provider='mysql', host='localhost', user='user', passwd='password', db='db')

db.generate_mapping(create_tables=True)
set_sql_debug(bool(int(os.getenv('SQL_DEBUG', '0'))))
