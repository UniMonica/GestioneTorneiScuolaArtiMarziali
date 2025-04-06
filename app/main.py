from app.database import Base, engine
from app.models import Studente, Grado
from app.crud import create_studente, get_studenti
from datetime import datetime

# Funzione per inizializzare il database
def inizializza_database():
    Base.metadata.create_all(bind=engine)

# Funzione principale
def main():
    inizializza_database()
    print("Applicativo per la gestione dei tornei.")
    
    while True:
        print("\n1. Aggiungi studente\n2. Elenca studenti\n3. Esci")
        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            # Raccolta dei dati dello studente
            nome = input("Nome: ")
            cognome = input("Cognome: ")

            # Validazione della data di nascita
            while True:
                data_nascita_str = input("Data di nascita (YYYY-MM-DD): ")
                if data_nascita_str.strip():  # Controlla che non sia vuoto
                    try:
                        data_nascita = datetime.strptime(data_nascita_str, '%Y-%m-%d').date()
                        break  # Esci dal ciclo se la data è valida
                    except ValueError:
                        print("Errore: La data deve essere nel formato YYYY-MM-DD.")
                else:
                    print("Errore: La data di nascita non può essere vuota.")
            
            # Altri dati
            telefono = input("Telefono: ")
            email = input("Email: ")
            
            # Validazione del grado
            while True:
                try:
                    grado_id = int(input("ID del grado: "))
                    break  # Esci dal ciclo se il grado è valido
                except ValueError:
                    print("Errore: ID del grado deve essere un numero intero.")
            
            # Creazione dello studente
            studente = create_studente(nome, cognome, data_nascita, telefono, email, grado_id)
            print(f"Studente aggiunto: {studente.nome} {studente.cognome}")
        
        elif scelta == "2":
            # Elencare gli studenti
            studenti = get_studenti()
            for studente in studenti:
                print(f"{studente.nome} {studente.cognome}, Grado ID: {studente.grado_id}")
        
        elif scelta == "3":
            print("Uscita dall'applicativo.")
            break
        
        else:
            print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    main()
