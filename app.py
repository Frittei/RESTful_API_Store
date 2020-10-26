from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
import sqlite3


from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList # This enables SQLAlchemy to know what tables sould be created

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' #DB lives at root of folder
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'frid'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity) #/auth

api.add_resource(Item, '/item/<string:name>') # http://127.0.0.1.5000/sudent/Rolf
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True) #HTML link for debugging