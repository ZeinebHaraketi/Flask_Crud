import os
import secrets


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or  secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:root@localhost:5432/tutoFlask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False