#!/usr/bin/python
from classes.Server import Server
from classes.LogBuffer import LogBuffer
import os

oServer = Server()

nPid = os.getpid()

while 1:

	# Se sono nel processo figlio elaboro la richiesta trasmessa dal padre
	if nPid == 0:
		bOk = oServer.elabora(oClient)

		if not bOk:
			LogBuffer.write("Errore durante l'elaborazione della richiesta",3)
		else:
			LogBuffer.write("Richiesta elaborata correttamente",4)

		# Termino l'esecuzione del processo
		os._exit(0)
	else:
		print("Ascolto...")
		
		try:
			# Cosa fa				:				Attende di ricevere dei dati
			# Ritorna				:				oClient -> tupla che identifica il client, così formata
			# 										[0] => socket, oggetto socket riferito al client. Identifica la connessione con il client
			# 										[1] => address
			#											[0] => "192.168.0.183", stringa -> indirizzo del client
			#											[1] => 50465, numerico -> porta del client
			oClient = oServer.oSocket.accept()	# Resta in attesa di una connessione
		except KeyboardInterrupt:
			print("\nTermino l'esecuzione.")
			oServer.close()
			os._exit(0)

		# Una volta creata la connessione, creo un fork che elabora la richiesta
		nPid = os.fork()

oServer.close()