from classes.Socket import Socket
import os
import json
from settings import *
from classes.LogBuffer import LogBuffer
from classes.LaserNotes import LaserNotes

class Server():
	"""Classe che gestice il server di laserNotes"""
	def __init__(self):
		self.oSocket = Socket(HOST,PORT)
		self.oSocket.listen()
		self.oLN = LaserNotes()
	
	def parse(self,aData,oSock):
		"""
			Cosa fa			:			Esegue il parse del comando e reindirizza il funzionamento a funzioni specifiche
			aData			:			dizionario, comando ed eventuali parametri, così formato:
											{sComando: "LOGIN"} // Comando - nome comando
											{sUser : "luca"}	// nome parametro - valore
											{sPasswd : "root"}	// nome parametro - valore
											...
			oSock			:			oggetto socket, connessione socket con il client
			Ritorna			:			bRet -> logico, true se tutto ok, false in caso di errore
		"""
		bRet = False

		sComando = aData['sComando'].upper()
		del aData['sComando']

		if sComando == 'LOGIN':
			aRisultato = self.oLN.login(aData) # Effettuo il login
			oSock.sendall(json.dumps(aRisultato).encode("utf-8")) # Invio la risposta al client
			bRet = True

		return bRet

	def elabora(self,oClient):
		"""
			oClient			:			tupla che identifica il client, così formata
											[0] => socket, oggetto socket riferito al client. Identifica la connessione con il client
											[1] => address
											[0] => "192.168.0.183", stringa -> indirizzo del client
											[1] => 50465, numerico -> porta del client		
			Ritorna			:			bRet -> logico, true = tutto ok | false = errore
		"""
		bRet = False
		print("Elaboro...")
		
		LogBuffer.write("Elaboro richiesta da: {0}:{1}".format(oClient[1][0],oClient[1][1]),1)
		
		sData = self.oSocket.recv(oClient,MSGLEN)

		LogBuffer.write("{0} dice: {1}".format(oClient[1][0],sData),1)

		if sData == "":
			return bRet

		aData = json.loads(sData)

		bOk = self.parse(aData,oClient[0])

		if not bOk:
			LogBuffer.write("Errore durante il parse del comando. Controllare log precedenti per maggiori informazioni",3)
		else:
			bRet = True			

		return bRet

	def close(self):
		"""
			Chiude la connessione socket
		"""
		self.oSocket.close()