from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Se crea la instancia engine
engine = create_engine("sqlite:///data.db")

#Se crea la instancia declaritive base 
Base = declarative_base()


#se crea la clase session local para el session maker
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)