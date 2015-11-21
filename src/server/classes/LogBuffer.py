from settings import *

class LogBuffer(object):
	"""Scrive i log all'interno del file di log (LOGFILE)"""

	def write(sMsg,nLevel):
		"""
			Cosa fa			:			Scrive il messaggio di log all'interno del file di log (LOGFILE in settings.py)
			sMsg			:			stringa, messaggio da scrivere nei log
			nLevel			:			numerico, livello di log:
											1: Info
											2: Warning
											3: Errore
											4: Debug
		"""
		if LOG == 0:
			return

		sLog = ""
		oFile = open(LOGFILE,"a")
		if nLevel == 1:
			if LOGLEVEL == 1 or LOGLEVEL == 2:		 #LOGLEVEL: 1 = ALL | 2 = INFO | 3 = WARNING | 4 = ERROR | 5 = DEBUG
				sLog += "INFO    | " + sMsg + "\n"
		elif nLevel == 2:
			if LOGLEVEL == 1 or LOGLEVEL == 3:		 #LOGLEVEL: 1 = ALL | 2 = INFO | 3 = WARNING | 4 = ERROR | 5 = DEBUG
				sLog += "WARNING | " + sMsg + "\n"
		elif nLevel == 3:
			if LOGLEVEL == 1 or LOGLEVEL == 4:		 #LOGLEVEL: 1 = ALL | 2 = INFO | 3 = WARNING | 4 = ERROR | 5 = DEBUG
				sLog += "ERROR   | " + sMsg + "\n"
		elif nLevel == 4:
			if LOGLEVEL == 1 or LOGLEVEL == 5:		 #LOGLEVEL: 1 = ALL | 2 = INFO | 3 = WARNING | 4 = ERROR | 5 = DEBUG
				sLog += "DEBUG   | " + sMsg + "\n"

		if not (sLog == ""):
			oFile.write(sLog)
			
		oFile.close()