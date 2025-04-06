from app.models import Studente
from .database import SessionLocal

def create_studente(nome, cognome, data_nascita, telefono, email, grado_id):
    db = SessionLocal()
    nuovo_studente = Studente(
        nome=nome,
        cognome=cognome,
        data_nascita=data_nascita,
        telefono=telefono,
        email=email,
        grado_id=grado_id
    )
    db.add(nuovo_studente)
    db.commit()
    db.refresh(nuovo_studente)
    return nuovo_studente

def get_studenti():
    db = SessionLocal()
    studenti = db.query(Studente).all()
    db.close()
    return studenti
 
