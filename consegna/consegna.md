### Tempo (40 minuti)

##### (70 punti) Scrivere un socket server in Python che riceve da un client un messaggio JSON che rappresenta un elenco di più nominativi con la rispettiva età (minimo 5). es:
- Angelo: 25
- Francesca: 22
- Luigi: 23
- Pamela: 21
- Riccardo: 24
- ..... ecc

Il server deve trovare la persona più giovane e quella più anziana e inviare al client un messaggio JSON che contiene
i due nominativi trovati compresa la loro età. Il client deve stampare i dati ricevuti dal server e salvarli in un file
JSON. Il messaggio JSON che il client invierà al server dovrà essere letto da un file JSON;

(30 punti) Il socket server dovrà verificare la validità del messaggio JSON ricevuto tramite un JSON schema e adeguare
la risposta in base alla validità del messaggio.