from flask import Flask
from flask_restful import Api
from controller.controller import Hero, HeroList


app = Flask("teste")
api = Api(app)
api.add_resource(HeroList, "/heroes")
api.add_resource(Hero, '/heroes/<hero_id>')

if __name__ == '__main__':
    app.run() 
