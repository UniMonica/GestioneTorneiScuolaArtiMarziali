from datetime import datetime
from crud.crud_operations import inserisci_studente

inserisci_studente(
    nome="Monica",
    cognome="Paccagnella",
    data_nascita = datetime.strptime('1978-09-13', '%Y-%m-%d').date(),
    telefono="333-5551234",
    email="monica@example.com",
    id_grado=1,
)
print("Studente inserito con successo!")
