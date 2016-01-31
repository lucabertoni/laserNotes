import hashlib
import time

from classes.Database import Database
from settings import *
from classes.LogBuffer import LogBuffer

class LaserNotes():
	"""Classe che gestisce le operazioni di LaserNotes (es: login, getAllNotes, ...)"""
	def __init__(self):
		pass

	######################################################################################################
	#												SESSIONE											 #
	######################################################################################################
	
	def login(self,aData):
		"""
			Cosa fa			:			Effettua il login all'interno di LaserNotes
			aData			:			dizionario, valori necessari per effettuare il login (user, password), così formato
											["sUser"] => "luca.bertoni24@gmail.com"
											["sPassword"] => "b9be11166d72e9e3ae7fd407165e4bd2" (md5(md5("root")))
			Ritorna			:			aRet -> dizionario, risposta da inviare al client, così formato:
											["sRisultato"] => "OK" | "NO"
											["sCookie"] => "28c8edde3d61a041121511d3b1866f0636" | ""
		"""
		sUser = aData['sUser']
		sPassword = aData['sPassword']
		aRet = {'sRisultato':"NO"}

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

		oDB.close()
		return aRet


	######################################################################################################
	#												UTENTE												 #
	######################################################################################################

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
		aSelect = oDB.select(("id",),"utenti",{"sEmail" : aData["sEmail"]})

		# Se l'utente esiste già non lo inserisco
		if not(aSelect == None) > 0:
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
		# Se non è stato definito un livello, imposto quello di default: 1
		if not("nLivello" in aData):
			aData["nLivello"] = "1"

		bInsert = oDB.insert(("sNome","sCognome","sEmail","sUsername","sPassword","nLivello"),"utenti",aData)

		if bInsert:
			aRet["sRisultato"] = "OK"
			LogBuffer.write("Aggiungo utente: Username = {0}".format(aData["sUsername"]),1)

		oDB.close()
		return aRet

	def getUsername(self,aData):
		"""
			Cosa fa			:			Estrapola il nome utente di un utente
			aData			:			dizionario, cookie dell'utente, così formato
											["sCookie"] => "28c8edde3d61a041121511d3b1866f0636"
			Ritorna			:			aRet -> dizionario, risposta da inviare al client, così formato:
											["sRisultato"]	=> "OK" | "NO"
											["sUsername]	=> "lucabertoni"
		"""
		sCookie = aData['sCookie']
		aRet = {'sRisultato':"NO"}

		nId = self.cookie_decode(sCookie)

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
		aSelect = oDB.select(("sUsername",),"utenti",{"id" : str(nId)})

		# Se aRet non è None significa che l'username e la password sono corretti
		if not(aSelect == None):
			aRet["sUsername"] = aSelect["sUsername"]
			aRet["sRisultato"] = "OK"

		oDB.close()
		return aRet
	
	def getAllUserInfo(self,aData):
		"""
			Cosa fa			:			Effettua il login all'interno di LaserNotes
			aData			:			dizionario, valori necessari per effettuare il login (user, password), così formato
											["sUser"] => "luca.bertoni24@gmail.com"
											["sPassword"] => "b9be11166d72e9e3ae7fd407165e4bd2" (md5(md5("root")))
			Ritorna			:			aRet -> dizionario, risposta da inviare al client, così formato:
											["sRisultato"] => "OK" | "NO"
											["sCookie"] => "28c8edde3d61a041121511d3b1866f0636" | ""
		"""
		sCookie = aData['sCookie']
		aRet = {'sRisultato':"NO"}
		nId = self.cookie_decode(sCookie)

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
		aSelect = oDB.select(("*",),"utenti",{"id" : str(nId)})

		# Se aRet non è None significa che l'username e la password sono corretti
		if not(aSelect == None):
			sCookie = self.cookie_encode(aSelect["id"])
			aRet["aUser"] = {}
			for key in aSelect:
				aRet["aUser"][key] = aSelect[key]
			aRet["sRisultato"] = "OK"

		oDB.close()
		return aRet


	######################################################################################################
	#												NOTE												 #
	######################################################################################################

	def addNote(self, aData):
		"""
			Cosa fa				:				Aggiunge una nota in db
			aData				:				dizionario, definizione della nota da inserire in db
													["sCookie"] => "28c8edde3d61a041121511d3b1866f0636"
													["aNote"] 	=>
															["sTitolo"]	=> "Titolo nota"
															["sTesto"]	=> "Testo della nota"
			N.B.				:				La data della nota viene generata automaticamente
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


		# Aggiungo l'id dell'utente sulla base del cookie
		"""
			Cosa fa				:				Ritorna l'id estratto dalla decodifica del cookie
			sCookie				:				stringa, cookie da decodificare
			Ritorna				:				nId -> numerico, id estratto dal cookie, -1 = Errore
		"""
		aData["aNote"]["nIdUtente"] = str(self.cookie_decode(aData["sCookie"]))

		# Aggiungo la data in formato DATETIME
		aData["aNote"]["sDate"] = time.strftime('%Y-%m-%d %H:%M:%S')

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
		bInsert = oDB.insert(("sTitolo","sTesto","nIdUtente","sDate"),"note",aData["aNote"])

		if bInsert:
			aRet["sRisultato"] = "OK"
			LogBuffer.write("Aggiungo una nota: Id Utente = {0}".format(aData["aNote"]["nIdUtente"]),1)

		oDB.close()
		return aRet
	
	def getAllNotes(self,aData):
		"""
			Cosa fa			:			Estrae la lista di tutte le note di un utente
			aData			:			dizionario, così formato
											["sCookie"] => "28c8edde3d61a041121511d3b1866f0636"
			Ritorna			:			aRet -> dizionario, risposta da inviare al client, così formato:
											["sRisultato"] 	=> "OK" | "NO"
											["aNotes"] =>
												[0]	=> 
													["id"] => 1
													["sTitolo"] => "Titolo nota"
													["sTesto"] => "Testo nota"
													["sDate"] => "2015-11-21 20:22:15"
												...
		"""
		sCookie = aData['sCookie']
		aRet = {'sRisultato':"NO"}
		nId = self.cookie_decode(sCookie)

		try:
			oDB = Database(DBHOST,DBUSER,DBPASSWORD,DBNAME)
		except Exception as e:
			LogBuffer.write("Errore durante la connessione al database: {0}".format(e),3)
			return aRet

		# Cosa fa				:				Esegue una select multipla su una tabella
		# aWhat				:				tupla, quali campi estrarre, così formata:
		#										[0] => "sTitolo"
		#										[1] => "sTesto"
		#										...
		# sTabella			:				stringa, nome della tabella sulla quale eseguire la query
		# aWhere				:				dizionario, campi per where, es:
		#										["sCookie"] => "28c8edde3d61a041121511d3b1866f0636"
		# Ritorna				:				aRet -> lista, lista di dizionari (elementi) estratti con la select, così formato:
		#									[0]	=> 
		#										["id"] => 1
		#										["sTitolo"] => "Titolo nota"
		#										["sTesto"] => "Testo nota"
		#										["sDate"] => "2015-11-21 20:22:15"
		#									...
		aSelect = oDB.selectAll(("id","sTitolo","sTesto","sDate"),"note",{"nIdUtente" : str(nId)})

		# Se aRet non è None significa che sono stati estratti dei dati
		if not(aSelect == None):
			nApp = 0
			# Trasformo il datetime in stringa
			for aNote in aSelect:
				aSelect[nApp]["sDate"] = aNote["sDate"].strftime("%Y-%m-%d %H:%M:%S")
				nApp += 1
			aRet["aNotes"] = aSelect
			aRet["sRisultato"] = "OK"

		oDB.close()
		return aRet

	def updateNote(self, aData):
		"""
			Cosa fa				:				Aggiorna una nota in db
			aData				:				dizionario, definizione della nota da aggiornare in db
													["sCookie"] => "28c8edde3d61a041121511d3b1866f0636"
													["aNote"] 	=>
															["id"] => 1
															["sTitolo"]	=> "Titolo nota"
															["sTesto"]	=> "Testo della nota"
			N.B.				:				La data della nota viene generata automaticamente
			Ritorna				:				aRet -> dizionario, risposta da inviare al client, così formato:
													["sRisultato"] => "OK" | "NO"
		"""
		sCookie = aData['sCookie']
		aRet = {'sRisultato':"NO"}
		nId = self.cookie_decode(sCookie)

		if aData == None:
			return aRet

		nIdNota = aData["aNote"]["id"]
		try:
			oDB = Database(DBHOST,DBUSER,DBPASSWORD,DBNAME)
		except Exception as e:
			LogBuffer.write("Errore durante la connessione al database: {0}".format(e),3)
			return aRet

		# Aggiungo la data in formato DATETIME
		aData["aNote"]["sDate"] = time.strftime('%Y-%m-%d %H:%M:%S')

		"""
			Cosa fa				:				Aggiorna un dato in una tabella
			aWhat				:				tupla, quali campi aggiornare, così formata:
													[0] => "sUsername"
													[1] => "sPassword"
													...
			sTabella			:				stringa, nome della tabella sulla quale eseguire la query
			aData				:				dizionario, campi per update con chiavi corrispondenti ai campi aWhat, es:
													['sUsername'] => "Luca"
													['sPassword'] => "Bertoni"
			aWhere				:				dizionario, campi per where, es:
													["id"] => 1
			Ritorna				:				bRet -> logico, true = Insert OK | false = Errore
		"""
		bUpdate = oDB.update(("sTitolo","sTesto","sDate"),"note",aData["aNote"],{'id':str(nIdNota)})

		if bUpdate:
			aRet["sRisultato"] = "OK"
			LogBuffer.write("Aggiorno una nota: Id Utente = {0}. Id nota: {1}".format(nId,nIdNota),1)

		oDB.close()
		return aRet

	def deleteNote(self, aData):
		"""
			Cosa fa				:				Cancella una nota dal db
			aData				:				dizionario, definizione della nota da cancellare dal db
													["sCookie"] => "28c8edde3d61a041121511d3b1866f0636"
													["nIdNota"] => 1
			Ritorna				:				aRet -> dizionario, risposta da inviare al client, così formato:
													["sRisultato"] => "OK" | "NO"
		"""
		sCookie = aData['sCookie']
		aRet = {'sRisultato':"NO"}
		nId = self.cookie_decode(sCookie)

		if aData == None:
			return aRet

		nIdNota = aData["nIdNota"]

		try:
			oDB = Database(DBHOST,DBUSER,DBPASSWORD,DBNAME)
		except Exception as e:
			LogBuffer.write("Errore durante la connessione al database: {0}".format(e),3)
			return aRet

		"""
			Cosa fa				:				Cancella un dato da una tabella
			sTabella			:				stringa, nome della tabella sulla quale eseguire la query
			aWhere				:				dizionario, campi per where, es:
													["id"] => 1
			Ritorna				:				bRet -> logico, true = Insert OK | false = Errore
		"""
		bUpdate = oDB.delete("note",{'id':str(nIdNota),'nIdUtente': str(nId)})

		if bUpdate:
			aRet["sRisultato"] = "OK"
			LogBuffer.write("Cancello una nota: Id Utente = {0}. Id nota: {1}".format(nId,nIdNota),1)

		oDB.close()
		return aRet

	######################################################################################################
	#												COOKIE												 #
	######################################################################################################

	def cookie_encode(self,nId):
		"""
			Cosa fa				:				Genera un cookie sulla base dell'id
			nId					:				numerico, id sul quale basare la generazione del cookie
			Ritorna				:				sRet -> stringa, cookie
		"""
		sRet = ""

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
		if not(sCookie == None) and (not(sCookie == "")):
			nId = int(int(sCookie[16:-16])/12)

		return nId