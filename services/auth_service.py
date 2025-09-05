import jwt
from datetime import datetime, timedelta
import hashlib

SECRET_KEY = "your-secret-key"  # In production, use environment variables
ALGORITHM = "HS256"

def verify_password(plain_password, hashed_password):
    """Verify a password against its hash"""
    return hashlib.sha256(plain_password.encode()).hexdigest() == hashed_password

def create_access_token(user_id: str, expires_delta: timedelta = timedelta(minutes=15)):
    """Create a JWT token"""
    expire = datetime.utcnow() + expires_delta
    to_encode = {
        "user_id": user_id,
        "exp": expire
    }
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    """Verify a JWT token"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.JWTError:
        return None