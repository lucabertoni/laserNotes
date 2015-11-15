package app.lasernotes.org.lasernotes;

import java.net.Socket;

import org.json.JSONObject;

/**
 * Classe che gestisce la comunicazione con il server.
 */
public class Client {
    String sHost;
    int nPort;

    /*
    * Cosa fa           :           Costruisce la classe client sulla base dell'indirizzo dell'host e della porta
    * sHost             :           stringa, indirizzo dell'host
    * nPort             :           numerico, numero della porta dell'host
    * */
    Client(String sHost, int nPort){
        this.sHost = sHost.trim();
        this.nPort = nPort;
    }

    /*
    *   Cosa fa         :           Crea collegamento con il server utilizzando una socket (classe lnSocket) sulla base dei parametri settati nel costruttore
    * */
    private lnSocket connect() throws java.io.IOException{
        /*
        * Cosa fa           :           Crea una socket sulla base dei parametri
        * sHost             :           stringa, indirizzo dell'host
        * nPort             :           numerico, numero della porta dell'host
        * */
        lnSocket oSocket = new lnSocket(this.sHost,this.nPort);
        return oSocket;
    }


    /*
    * Cosa fa           :           Effettua il login comunicando con l'host
    * sUser             :           stringa, username per loggarsi
    * sPassword         :           stringa, md5(md5(della password))
    * Ritorna           :           sRet -> cookie generato dal server, oppure vuoto in caso di errore
    * */
    String login(String sUser,String sPassword){
        String sRet,sJson;
        sRet = "";
        lnSocket oSocket;
        JSONObject oJson = new JSONObject();

        /*
        // Mi collego con il server...
        try{
            oSocket = this.connect();
        }catch(java.io.IOException e){
            LogBuffer.write("Login -> Impossibile creare il collegamento con il server",3);
            return sRet;
        }

        // Genero il json sulla base dello user e della password seguendo il protocollo.
        try {
            oJson.put("sUser", sUser);
            oJson.put("sPassword", sPassword);
        }catch(org.json.JSONException e){

        }

        sJson = oJson.toString();

        try {
            oSocket.write(sJson);
        }catch(java.io.IOException e){
            LogBuffer.write("Login -> Impossibile comunicare con la socket",3);
        }
        */
        return sRet;
    }
}