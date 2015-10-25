import socket

class Socket():
	"""Socket server che gestisce la comunicazione con i client"""
	def __init__(self,sHost,nPort):
		"""
			Cosa fa				:				Inizializza la socket
			sHost				:				stringa, host con cui comunicare
			nPort				:				stringa, porta di comunicazione con l'host
		"""
		self.setHost(sHost)
		self.setPort(nPort)
		self.createSocket()
		self.bind()

	def setHost(self,sHost):
		"""
			Cosa fa				:				Imposta la porta su cui avverrà la comunicazione
			sHost				:				stringa, host con cui comunicare
		"""
		self.sHost = sHost

	def setPort(self,nPort):
		"""
			Cosa fa				:				Imposta la porta su cui avverrà la comunicazione
			nPort				:				stringa, porta di comunicazione con l'host
		"""
		self.nPort = nPort
	
	def getHost(self):
		"""
			Cosa fa				:				Estrapola l'host con cui avviene la comunicazione
			Ritorna				:				stringa, host con cui si sta comunicando o con cui iniziare una comunicazione
		"""
		return self.sHost

	def getPort(self):
		"""
			Cosa fa				:				Estrapola la porta di comunicazione con l'host
			Ritorna				:				numerico, porta di comunicazione
		"""
		return self.nPort

	def createSocket(self):
		"""
			Cosa fa				:				Crea una socket di tipo STREAM
		"""
		self.SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def bind(self):
		sHost = self.getHost()
		nPort = self.getPort()
		self.SOCKET.bind((sHost, nPort))
	
	def listen(self):
		"""
			Cosa fa				:				Ascolta e aspetta che ci siano dei dati.
			Ritorna				:				sMsg -> stringa, messaggio
		"""
		self.SOCKET.listen(1)

	def accept(self):
		"""
			Cosa fa				:				Attende di ricevere dei dati
			Ritorna				:				oClient -> tupla che identifica il client, così formata
													[0] => socket, oggetto socket riferito al client. Identifica la connessione con il client
													[1] => address
														[0] => "192.168.0.183", stringa -> indirizzo del client
														[1] => 50465, numerico -> porta del client
		"""
		oClient = self.SOCKET.accept()
		return oClient

	def recv(self,oClient,nMsgLen):
		"""
			oClient				:			tupla, tupla che identifica il client, così formata
													[0] => socket, oggetto socket riferito al client. Identifica la connessione con il client
													[1] => address
														[0] => "192.168.0.183", stringa -> indirizzo del client
														[1] => 50465, numerico -> porta del client
			nMsgLen				:			numerico, lunghezza del messaggio da ricevere
			Ritorna				:			sRet -> stringa, valore ricevuto dal client
		"""
		sRet = ""
		oSock = oClient[0]
		sRet = oSock.recv(nMsgLen)
		sRet = sRet.decode("utf-8")
		return sRet

	def close(self):
		"""
			Cosa fa				:				Chiude la connessione socket
		"""
		self.SOCKET.close()