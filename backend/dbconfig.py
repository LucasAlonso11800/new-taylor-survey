from sqlalchemy import create_engine, MetaData
from dotenv import dotenv_values


user = dotenv_values().get("MYSQL_USER")
password = dotenv_values().get('MYSQL_PASSWORD')
host = dotenv_values().get('MYSQL_HOST')
port = dotenv_values().get('MYSQL_PORT')

connectionString = f"mysql+pymysql://{user}:{password}@{host}:{port}/taylor_survey"

engine = create_engine(connectionString)

meta = MetaData()

conn = engine.connect()