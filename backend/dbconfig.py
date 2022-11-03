from sqlalchemy import create_engine, MetaData
from os import getenv

user = getenv('MYSQL_USER')
password = getenv('MYSQL_PASSWORD')
host = getenv('MYSQL_HOST')
port = getenv('MYSQL_PORT')

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/taylor-survey")

meta = MetaData()

conn = engine.connect()