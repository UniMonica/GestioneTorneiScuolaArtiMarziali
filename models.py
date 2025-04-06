from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Tabella Studente
class Studente(Base):
    __tablename__ = "studente"
    id_studente = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    cognome = Column(String, nullable=False)
    data_nascita = Column(Date)
    telefono = Column(String)
    email = Column(String)
    id_grado = Column(Integer, ForeignKey("grado.id_grado"))

# Tabella Grado
class Grado(Base):
    __tablename__ = "grado"
    id_grado = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    descrizione = Column(String)
    livello = Column(Integer)
    print("File models.py eseguito correttamente! Le tabelle sono pronte.")
from db_config import engine  # Importa l'engine dal file db_config.py

# Crea le tabelle nel database
Base.metadata.create_all(engine)
print("Tabelle create nel database.")
