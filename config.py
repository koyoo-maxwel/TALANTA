import os

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_VIDEOS_DEST = 'app/static/videos'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

  
    # simple mde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass

class DevConfig():
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://student:1209@localhost/talanta'
    DEBUG = True

config_options = {
    'development' : DevConfig ,
    'production'  : ProdConfig
}