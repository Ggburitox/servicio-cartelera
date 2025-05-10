from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

MYSQL_HOST = os.getenv("MYSQL_HOST")  # IP privada MV BD
MYSQL_PORT = os.getenv("MYSQL_PORT")  # 8008
MYSQL_USER = os.getenv("MYSQL_USER")  # root
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")  # utec
MYSQL_DB = os.getenv("MYSQL_DB")  # bd_cartelera

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
