import os


class Config:
    '''
    General configuration parent class
    '''

    SQLALCHEMY_TRACK_NOTIFICATIONS = False
    SECRET_KEY = 'os.environ.get("SECRET_KEY")'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME='halkanoh10@gmail.com'
    MAIL_PASSWORD='1234'
    SUBJECT_PREFIX='PITCH HUB'
    SENDER_EMAIL='halkanoh10@gmail.com'


class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://halkano:1234@localhost/pitch'
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
