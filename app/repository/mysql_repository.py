from pony.orm import commit, db_session

from domain.model import Hero, CardHero


class MySqlRepository:

    @staticmethod
    def check_connection():
        return Hero.select().first()

    @staticmethod
    @db_session
    def save(hero: Hero, card_hero: CardHero):
        commit()

    @staticmethod
    @db_session
    def save_card(card_hero: CardHero):
        commit()

    @staticmethod
    @db_session
    def update(hero: Hero, card_hero: CardHero):
        commit()

    @staticmethod
    def find_all():
        result = Hero.select()
        return result

    @staticmethod
    def find_by_id(id):
        hero = Hero.select(lambda s: s.id_hero == id).first()
        card_hero = CardHero.select(lambda c: c.id_hero == id).first()
        return hero, card_hero

    @staticmethod
    def delete_hero(id_hero):
        Hero.select(lambda s: s.id_hero == id_hero).delete()
        CardHero.select(lambda c: c.id_hero == id_hero).delete()
