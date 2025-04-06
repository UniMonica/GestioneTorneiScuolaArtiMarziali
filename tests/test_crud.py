from crud.crud_operations import inserisci_studente

inserisci_studente(
    nome="Monica",
    cognome="Paccagnella",
    data_nascita="2000-05-10",
    telefono="333-5551234",
    email="monica@example.com",
    id_grado=1,
)
print("Studente inserito con successo!")
