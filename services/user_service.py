
import json
from models.user import User
from utils.helpers import generate_uuid

DB_PATH = "db/FakeDB.json"

def load_db():
    with open(DB_PATH, "r") as f:
        return json.load(f)

def save_db(data):
    with open(DB_PATH, "w") as f:
        json.dump(data, f, indent=4)

def create_user(email, password):
    db = load_db()
    user_id = generate_uuid()
    user = User(user_id, email, password)
    db["users"].append(user.to_dict())
    save_db(db)
    return user

def read_user(user_id):
    db = load_db()
    for user in db["users"]:
        if user["id"] == user_id:
            return user
    return None

def update_user(user_id, email=None, password=None):
    db = load_db()
    for user in db["users"]:
        if user["id"] == user_id:
            if email:
                user["email"] = email
            if password:
                user["password"] = password
            save_db(db)
            return user
    return None

def delete_user(user_id):
    db = load_db()
    for user in db["users"]:
        if user["id"] == user_id:
            user["active"] = False  # Logical deletion by setting active flag to False
            save_db(db)
            return True
    return False

def activate_user_by_email(email):
    db = load_db()
    for user in db["users"]:
        if user["email"] == email and not user["active"]:
            user["active"] = True
            save_db(db)
            return True
    return False

def list_users(active_only=True):
    db = load_db()
    if active_only:
        return [user for user in db["users"] if user.get("active", True)]
    return db["users"]
