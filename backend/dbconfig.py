from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values


user = dotenv_values().get("MYSQL_USER")
password = dotenv_values().get('MYSQL_PASSWORD')
host = dotenv_values().get('MYSQL_HOST')
port = dotenv_values().get('MYSQL_PORT')

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{user}:{password}@{host}:{port}/taylor_survey"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()