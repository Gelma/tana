# tana

Necessitonsi di campi:
* data  (come da esempio in data.php): necessaria
* evetuale ora
* eventuale nome
* tipo attivita': tandem / allievo (selettore)
* per quanti: selettore (come nell'esempio index.php per Age), con preselezionato 1, con bottoni fino a 5
* bottone di invio

Struttura:
* pagina unica, in testa l'inserimento, sotto i dati ordinati per data/ora (dalla data odierna in avanti);
* ad ogni inserimento delete degli eventi piu' vecchi di 3 mesi
* per il momento nessuna autenticazione
* c'è da fare una migliore validazione dell'input

## Per Far partire

Se si vuole far partire da db pulito bisogna 
* cancellare il file db.sqlite3
* eseguire python manage.py migrate
* eseguire python manage.py createsuperuser

Se va bene per il test c'è l'utente bveronesi bveronesi
* andare dentro aeroplanisti 
* far partire bower install
* far partire python manage.py runserver
