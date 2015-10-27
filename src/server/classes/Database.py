import pymysql.cursors

class Database():
	"""Classe che gestisce la connesione al database"""
	def __init__(self,sHost,sUser,sPassword,sDbName):
		self.oConnection = pymysql.connect(host=sHost,
		                             user=sUser,
		                             password=sPassword,
		                             db=sDbName,
		                             charset='utf8mb4',
		                             cursorclass=pymysql.cursors.DictCursor)
		self.oCursor = self.oConnection.cursor()

	def select(self,aWhat = ("*"),sTabella = "",aWhere = {}):
		"""
			Cosa fa				:				Esegue una semplice select su una tabella
			aWhat				:				tupla, quali campi estrarre, così formata:
													[0] => "sUsername"
													[1] => "sPassword"
													...
			sTabella			:				stringa, nome della tabella sulla quale eseguire la query
			aWhere				:				dizionario, campi per where, es:
													['sNome'] => "Luca"
													['sCognome'] => "Bertoni"
			Ritorna				:				aRet -> dizionario, lista di elementi estratti con la select, così formato:
													["sUsername"] => "luca.bertoni24@gmail.com"
													["sPassword"] => "b9be11166d72e9e3ae7fd407165e4bd2"
		"""
		aRet = {}
		sSql = "SELECT "

		# Compongo i campi da cercare
		for x in aWhat:
			sSql += x + ","

		# Cancello la virgola finale
		sSql = sSql[:-1]

		# Aggiungo il nome della tabella da cui estrarre i dati
		sSql += " FROM " + sTabella

		# Aggiungo eventuali where
		if len(aWhere) > 0:
			sSql += " WHERE"
			for key in aWhere:
				# Se è un numero non metto gli apici
				if aWhere[key].isnumeric():
					sSql += " " + key + "=" + aWhere[key] + " AND"
				else:
					sSql += " " + key + "='" + aWhere[key] + "' AND"
					
			# Cancello l' "AND" finale
			sSql = sSql[:-3]

		try:
			self.oCursor.execute(sSql)
			aRet = self.oCursor.fetchone()
		except Exception as e:
			pass

		return aRet

	def insert(self, aWhat = (""), sTabella = "", aData = {}):
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
		bRet = False
		sSql = "INSERT INTO " + sTabella + " ("

		# Compongo i campi da cercare
		for x in aWhat:
			sSql += x + ","

		# Cancello la virgola finale
		sSql = sSql[:-1]

		sSql += ") VALUES ("

		for x in aWhat:
			ele = aData[x]

			# Se è un numero non metto gli apici
			if ele.isnumeric():
				sSql += " " + ele + ","
			else:
				sSql += " " + "'" + ele + "',"

		# Cancello la virgola finale
		sSql = sSql[:-1]

		sSql += ")"
		
		try:
			bRet = self.oCursor.execute(sSql) # Eseguo la sql
			self.oConnection.commit() # Eseguo il commit dell'insert
		except Exception as e:
			bRet = False

		return bRet

	def close(self):
		"""
			Cosa fa				:				Chiude la comunicazione con il db
		"""
		self.oConnection.close()

"""
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='user',
                             password='passwd',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
"""		