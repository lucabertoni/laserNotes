from classes.Database import Database
from settings import *
from classes.LogBuffer import LogBuffer

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
			oDB = Database(HOST,DBUSER,DBPASSWORD,DBNAME)
		except Exception as e:
			LogBuffer.write("Errore durante la connessione al database: {0}".format(e),3)
			return aRet

		aSelect = oDB.select(("sUsername","sPassword"),"utenti",{"sUsername" : sUser, "sPassword" : sPassword})

		# Se aRet non è None significa che l'username e la password sono corretti
		if not(aSelect == None):
			aRet["sCookie"] = "ajsdghf"
			aRet["sRisultato"] = "OK"

		return aRet