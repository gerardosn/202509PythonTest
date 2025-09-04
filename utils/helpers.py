
import uuid
import re

def generate_uuid():
    return str(uuid.uuid4())

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

def is_valid_password(password):
    return len(password) >= 3
