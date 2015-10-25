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
		"""
		if LOG == 0:
			return

		sLog = ""
		oFile = open(LOGFILE,"a")
		if nLevel == 1:
			sLog += "INFO    | "
		elif nLevel == 2:
			sLog += "WARNING | "
		elif nLevel == 3:
			sLog += "ERROR   | "

		sLog += sMsg
		sLog += "\n"
		oFile.write(sLog)
		oFile.close()