package app.lasernotes.org.lasernotes;

import java.io.BufferedWriter;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.OutputStream;
import java.io.PrintWriter;

/**
 * Classe che gestisce la scrittura dei log
 */
public class LogBuffer{
    static final String LOGFILE = "laserNotes-app.log";
    static final Boolean LOG = true;
    static final int LOGLEVEL = 1;  // 1 = ALL | 2 = INFO | 3 = ERROR | 4 = WARNING | 5 = DEBUG

    /*
    *   Cosa fa			:			Scrive il messaggio di log all'interno del file di log (LOGFILE)
    *   sMsg			:			stringa, messaggio da scrivere nei log
    *   nLevel			:			numerico, livello di log:
    *                                       1: Info
    *                                       2: Warning
    *                                       3: Errore
    *                                       4: Debug
    * */
    static void write(String sMsg, int nLevel){
        if(LOG == false){
            return;
        }

        String sLog = "";

        // In base al livello compongo il messaggio di log
        switch (nLevel){
            case 1:
                if(LOGLEVEL == 1 || LOGLEVEL == 2)  sLog = "INFO    | " + sMsg + "\n";
            case 2:
                if(LOGLEVEL == 1 || LOGLEVEL == 3)  sLog = "WARNING | " + sMsg + "\n";
            case 3:
                if(LOGLEVEL == 1 || LOGLEVEL == 4)  sLog = "ERROR   | " + sMsg + "\n";
            case 4:
                if(LOGLEVEL == 1 || LOGLEVEL == 5)  sLog = "DEBUG   | " + sMsg + "\n";
        }

        // Aggiungo il testo al file di log
        // Per maggiori informazioni vedi: http://stackoverflow.com/questions/1625234/how-to-append-text-to-an-existing-file-in-java
        try{
            PrintWriter oPrint = new PrintWriter(new BufferedWriter(new FileWriter(LOGFILE, true)));
            oPrint.println(sLog);
        }catch (IOException e) {
        }
    }
}
