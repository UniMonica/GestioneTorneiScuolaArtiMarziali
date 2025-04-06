from models import Studente
from db_config import session

def inserisci_studente(nome, cognome, data_nascita, telefono, email, id_grado):
    nuovo_studente = Studente(
        nome=nome,
        cognome=cognome,
        data_nascita=data_nascita,
        telefono=telefono,
        email=email,
        id_grado=id_grado,
    )
    session.add(nuovo_studente)
    session.commit()
