import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'levisama-dbserver.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'levisama-db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'levisama-admin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'defineTh3jerry'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'levisamastorage'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'rBomh7+OAvdi+NItvjO7k/WKtbIvJ4FUsxYfGWGwRjOxeddSaEaqldmAVjHc7HkqLC0pNHYKbI+26uFQLBCZSw=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
