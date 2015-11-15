package app.lasernotes.org.lasernotes;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;

/**
 * Classe che gestisce le socket
 */
public class lnSocket {
    Socket oSocket;
    Boolean bSockOk = false;

    /*
    * Cosa fa           :           Crea una socket sulla base dei parametri
    * sHost             :           stringa, indirizzo dell'host
    * nPort             :           numerico, numero della porta dell'host
    * */
    lnSocket(String sHost, int nPort) throws java.io.IOException{
        // Ha bisogno del try-catch con eccezione "UnknownHostException"
        try{
            // Converto l'indirizzo dell'host passato come parametro nel formato necessario per la Socket
            InetAddress sIp = InetAddress.getByName(sHost);

            this.oSocket = new Socket(sHost,nPort);
            this.bSockOk = true;
        }catch(UnknownHostException e){
            /*
            *   Cosa fa			:			Scrive il messaggio di log all'interno del file di log (LOGFILE)
            *   sMsg			:			stringa, messaggio da scrivere nei log
            *   nLevel			:			numerico, livello di log:
            *                                       1: Info
            *                                       2: Warning
            *                                       3: Errore
            *                                       4: Debug
            * */
            LogBuffer.write("Impossibile risolvere l'indirizzo: " + sHost,3);
            return;
        }
    }

    /*
    *   Cosa fa         :           Legge dal server ciò che è stato inviato tramite la socket
    *   Ritorna         :           sRet -> stringa, testo inviato dal server (secondo il protocollo  un json)
    * */
    public String read() throws java.io.IOException{
        String sRet, sApp;
        sRet = "";

        // Leggo il buffer dal server al quale è connessa la socket
        InputStreamReader oInput = new InputStreamReader(this.oSocket.getInputStream());
        BufferedReader oBuffer = new BufferedReader(oInput);

        while ((sApp = oBuffer.readLine()) != null) {
            sRet += sApp;
        }

        oBuffer.close();
        return sRet;
    }

    /**
     *  Cosa fa         :           Scrive al server al quale è collegata la socket
     *  sMsg            :           Stringa, messaggio da inviare
     */
    public void write(String sMsg) throws java.io.IOException{
        OutputStreamWriter oOutput = new OutputStreamWriter(this.oSocket.getOutputStream());
        BufferedWriter oBuffer = new BufferedWriter(oOutput);
        PrintWriter oWriter = new PrintWriter(oOutput,true);

        // Scrivo sulla socket
        oWriter.println(sMsg);

        oWriter.close();
    }

    /*
    *   Cosa fa         :           Chiude la comunicazione della socket
    * */
    public void close() throws java.io.IOException{
        this.oSocket.close();
    }

}