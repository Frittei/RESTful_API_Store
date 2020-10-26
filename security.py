from models.user import UserModel
from werkzeug.security import safe_str_cmp



def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password): #In case of different types of string encoding (Asci, untext)
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)

