 /$$$$$$$  /$$                                           /$$                     /$$$$$$$$ /$$                                                             
| $$__  $$|__/                                          | $$                    |__  $$__/|__/                                                             
| $$  \ $$ /$$  /$$$$$$$  /$$$$$$$  /$$$$$$   /$$$$$$  /$$$$$$    /$$$$$$          | $$    /$$ /$$$$$$/$$$$   /$$$$$$                                      
| $$  | $$| $$ /$$_____/ /$$_____/ /$$__  $$ /$$__  $$|_  $$_/   /$$__  $$         | $$   | $$| $$_  $$_  $$ /$$__  $$                                     
| $$  | $$| $$|  $$$$$$ | $$      | $$  \__/| $$$$$$$$  | $$    | $$$$$$$$         | $$   | $$| $$ \ $$ \ $$| $$$$$$$$                                     
| $$  | $$| $$ \____  $$| $$      | $$      | $$_____/  | $$ /$$| $$_____/         | $$   | $$| $$ | $$ | $$| $$_____/                                     
| $$$$$$$/| $$ /$$$$$$$/|  $$$$$$$| $$      |  $$$$$$$  |  $$$$/|  $$$$$$$         | $$   | $$| $$ | $$ | $$|  $$$$$$$                                     
|_______/ |__/|_______/  \_______/|__/       \_______/   \___/   \_______/         |__/   |__/|__/ |__/ |__/ \_______/                                     
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
 /$$$$$$$$                            /$$                           /$$$$$$$$                                      /$$$$$$                                 
| $$_____/                           |__/                          |__  $$__/                                     /$$__  $$                                
| $$     /$$$$$$  /$$   /$$  /$$$$$$  /$$  /$$$$$$   /$$$$$$          | $$  /$$$$$$  /$$$$$$  /$$$$$$$   /$$$$$$$| $$  \__//$$$$$$   /$$$$$$  /$$$$$$/$$$$ 
| $$$$$ /$$__  $$| $$  | $$ /$$__  $$| $$ /$$__  $$ /$$__  $$         | $$ /$$__  $$|____  $$| $$__  $$ /$$_____/| $$$$   /$$__  $$ /$$__  $$| $$_  $$_  $$
| $$__/| $$  \ $$| $$  | $$| $$  \__/| $$| $$$$$$$$| $$  \__/         | $$| $$  \__/ /$$$$$$$| $$  \ $$|  $$$$$$ | $$_/  | $$  \ $$| $$  \__/| $$ \ $$ \ $$
| $$   | $$  | $$| $$  | $$| $$      | $$| $$_____/| $$               | $$| $$      /$$__  $$| $$  | $$ \____  $$| $$    | $$  | $$| $$      | $$ | $$ | $$
| $$   |  $$$$$$/|  $$$$$$/| $$      | $$|  $$$$$$$| $$               | $$| $$     |  $$$$$$$| $$  | $$ /$$$$$$$/| $$    |  $$$$$$/| $$      | $$ | $$ | $$
|__/    \______/  \______/ |__/      |__/ \_______/|__/               |__/|__/      \_______/|__/  |__/|_______/ |__/     \______/ |__/      |__/ |__/ |__/
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
Il programma accetta in input:
	1. File .txt contenente il campionamento temporale di uno o più periodi di un segnale.
	2. Minima e massima frequenza di analisi.
	3. Risoluzione spettrale necessaria.
	4. Caratteristica di interesse del segnale.
	5. (opzionale) Eliminazione della media del segnale da ogni campione.
	6. (opzionale) Tipo di finestratura. (Selezionando questa opzione verrà invalidato il valore dell'ampiezza del risultato).
Ritorna in output una serie discreta che rappresenta lo spettro del segnale in input con risoluzione specificata.

   
1. DTFT.py	->	Libreria con le operazioni necessarie
2. form.py	->	Interfaccia grafica
3. signalGenerator.py	->	script per la generazione di un segnale sinusoidale


Lo scopo del software è quello di individuare, con precisione arbitraria, la frequenza dell'armonica principale di un segnale campionato.