from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.database import Base


class Studente(Base):
    __tablename__ = "studenti"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    cognome = Column(String)
    data_nascita = Column(Date)
    telefono = Column(String)
    email = Column(String)
    grado_id = Column(Integer, ForeignKey("gradi.id"))
    grado = relationship("Grado", back_populates="studenti")

class Grado(Base):
    __tablename__ = "gradi"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    livello = Column(Integer)
    studenti = relationship("Studente", back_populates="grado")
 
