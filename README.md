Gestione Tornei Scuola di Arti Marziali
Un applicativo Python progettato per gestire i tornei, i corsi e le attività di una scuola di arti marziali. Questo progetto si concentra sull'organizzazione efficiente dei dati relativi agli studenti, agli istruttori, ai corsi e ai tornei.

Caratteristiche Principali
Gestione degli Studenti: Inserimento, aggiornamento e visualizzazione delle informazioni sugli studenti.

Gestione dei Corsi: Dettagli sui corsi, istruttori e programmazione degli orari.

Tornei e Categorie: Registrazione dei partecipanti e monitoraggio dei risultati.

Promozioni di Grado: Tracciamento dei gradi (cinture) e degli avanzamenti degli studenti.

Funzionalità CRUD: Operazioni per creare, leggere, aggiornare e cancellare dati.

Struttura del Progetto
GestioneTorneiScuolaArtiMarziali/
├── app/
│   ├── __init__.py          # Definizione del pacchetto
│   ├── main.py              # Punto di ingresso principale
│   ├── database.py          # Configurazione del database SQLAlchemy
│   ├── models.py            # Definizione delle tabelle
│   ├── crud.py              # Operazioni CRUD
├── docs/
│   ├── relazione.pdf        # Documentazione dettagliata
├── tests/
│   ├── test_database.py     # Test per il database
│   ├── test_models.py       # Test per i modelli
├── .gitignore               # Esclusione dei file inutili dal repository
├── README.md                # Descrizione del progetto
├── requirements.txt         # Dipendenze del progetto
├── venv/                    # Ambiente virtuale (non incluso nel repository)
└── tornei.db                # File del database (non incluso nel repository)

