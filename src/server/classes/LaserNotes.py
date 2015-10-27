from classes.Database import Database
from settings import *
from classes.LogBuffer import LogBuffer
import hashlib

class LaserNotes():
	"""Classe che gestisce le operazioni di LaserNotes (es: login, getAllNotes, ...)"""
	def __init__(self):
		pass
	
	def login(self,aData):
		"""
			Cosa fa			:			Effettua il login all'interno di LaserNotes
			aData			:			dizionario, valori necessari per effettuare il login (user, password), così formato
											["sUser"] => "luca.bertoni24@gmail.com"
											["sPassword"] => "b9be11166d72e9e3ae7fd407165e4bd2" (md5(md5("root")))
			Ritorna			:			aRet -> dizionario, risposta da inviare al client, così formato:
											["sRisultato"] => "OK" | "NO"
											["sCookie"] => "ahsdj" | ""
		"""
		sUser = aData['sUser']
		sPassword = aData['sPassword']
		aRet = {'sRisultato':"NO","sCookie":""}

		try:
			oDB = Database(DBHOST,DBUSER,DBPASSWORD,DBNAME)
		except Exception as e:
			LogBuffer.write("Errore durante la connessione al database: {0}".format(e),3)
			return aRet

		# Cosa fa				:				Esegue una semplice select su una tabella
		# aWhat					:				tupla, quali campi estrarre, così formata:
		#										[0] => "sUsername"
		#										[1] => "sPassword"
		#										...
		# sTabella				:				stringa, nome della tabella sulla quale eseguire la query
		# aWhere				:				dizionario, campi per where, es:
		#										['sNome'] => "Luca"
		#										['sCognome'] => "Bertoni"
		# Ritorna				:				aRet -> dizionario, lista di elementi estratti con la select, così formato:
		#										["sUsername"] => "luca.bertoni24@gmail.com"
		#										["sPassword"] => "b9be11166d72e9e3ae7fd407165e4bd2"
		aSelect = oDB.select(("id","sUsername","sPassword"),"utenti",{"sUsername" : sUser, "sPassword" : sPassword})

		# Se aRet non è None significa che l'username e la password sono corretti
		if not(aSelect == None):
			sCookie = self.cookie_encode(aSelect["id"])
			LogBuffer.write("Effettuo login con cookie: {0}".format(sCookie),1)
			aRet["sCookie"] = sCookie
			aRet["sRisultato"] = "OK"

		return aRet

	def addUser(self, aData):
		"""
			Cosa fa				:				Aggiunge un utente in db. Se l'email è già presente non fa nulla
			aData				:				dizionario, dati dell'utente da aggiungere, così formato:
													["sNome"] => "Luca"
													["sCognome"] => "Bertoni"
													["sEmail"] => "luca.bertoni24@gmail.com"
													["sUsername"] => "lucabertoni"
													["sPassword"] => "9be11166d72e9e3ae7fd407165e4bd2" (md5(md5("root")))
													["nLivello"] => 1		1 = Utente Normale | 2 = Tester | 3 = Amministratoreù
			Ritorna				:				aRet -> dizionario, risposta da inviare al client, così formato:
													["sRisultato"] => "OK" | "NO"
		"""
		aRet = {'sRisultato':"NO"}

		if aData == None:
			return aRet

		try:
			oDB = Database(DBHOST,DBUSER,DBPASSWORD,DBNAME)
		except Exception as e:
			LogBuffer.write("Errore durante la connessione al database: {0}".format(e),3)
			return aRet

		"""
			Cosa fa				:				Esegue una semplice insert su una tabella
			aWhat				:				tupla, quali campi usare per l'insert, così formata:
													[0] => "sUsername"
													[1] => "sPassword"
													...
			sTabella			:				stringa, nome della tabella sulla quale eseguire la query
			aData				:				dizionario, campi per insert con chiavi corrispondenti ai campi aWhat, es:
													['sUsername'] => "Luca"
													['sPassword'] => "Bertoni"
			Ritorna				:				bRet -> logico, true = Insert OK | false = Errore
		"""
		bInsert = oDB.insert(("sNome","sCognome","sEmail","sUsername","sPassword","nLivello"),"utenti",aData)

		if bInsert:
			aRet["sRisultato"] = "OK"
			
		oDB.close()
		return aRet

	def cookie_encode(self,nId):
		"""
			Cosa fa				:				Genera un cookie sulla base dell'id
			nId					:				numerico, id sul quale basare la generazione del cookie
			Ritorna				:				sRet -> stringa, cookie
		"""
		sRet = ""

		nId = 1
		sApp = hashlib.md5(hashlib.md5(str(nId).encode()).hexdigest().encode()).hexdigest()

		sRet = sApp[:16] + str(nId*12) + sApp[16:]
		return sRet

	def cookie_decode(self,sCookie):
		"""
			Cosa fa				:				Ritorna l'id estratto dalla decodifica del cookie
			sCookie				:				stringa, cookie da decodificare
			Ritorna				:				nId -> numerico, id estratto dal cookie, -1 = Errore
		"""
		nId = -1

		nId = int(sCookie[16:-16])

		return nId