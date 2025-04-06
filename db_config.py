from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///scuola_arti_marziali.db"  # Usando SQLite come database.
engine = create_engine(DATABASE_URL, echo=True)  # Configurazione dell'engine.

Session = sessionmaker(bind=engine)  # Configurazione della sessione.
session = Session()
