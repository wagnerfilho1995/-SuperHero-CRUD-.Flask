from marshmallow import Schema, fields


class CardSkills(Schema):
    force = fields.Int(default=0)
    speed = fields.Int(default=0)
    defense = fields.Int(default=0)
    knowledge = fields.Int(default=0)
    technology = fields.Int(default=0)
    magic = fields.Int(default=0)


class HeroIn(Schema):
    name = fields.Str()
    nickname = fields.Str(required=True)
    age = fields.Int()
    universe = fields.Str()
    skills = fields.Nested(CardSkills)


class HeroOut(Schema):
    id_hero = fields.Str()
    age = fields.Int()
    name = fields.Str()
    nickname = fields.Str()
    universe = fields.Str()
    skills = fields.Nested(CardSkills)
    created_at = fields.Str()


class HeroOutAll(Schema):
    id_hero = fields.Str()
    nickname = fields.Str()
    universe = fields.Str()


class Heroes(Schema):
    heroes = fields.List(fields.Nested(HeroOutAll))
