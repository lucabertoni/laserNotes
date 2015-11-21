package app.lasernotes.org.lasernotes;

import java.net.Socket;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

import android.util.Log;

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
//Log.d("SOCKET","Host: " + oSocket.oSocket.getInetAddress().toString());
        return oSocket;
    }

    /*
    * Cosa fa           :           Effettua il login comunicando con l'host
    * sUser             :           stringa, username per loggarsi
    * sPassword         :           stringa, md5(md5(della password))
    * Ritorna           :           sRet -> cookie generato dal server, oppure vuoto in caso di errore
    * */
    public String login(String sUser,String sPassword){
        String sRet,sJson,sComando;
        sRet = "";
        lnSocket oSocket;
        JSONObject oJson = new JSONObject();

        sComando = "Login";

        // Mi collego con il server...
        try{
            oSocket = this.connect();
        }catch(java.io.IOException e){
            //LogBuffer.write("Login -> Impossibile creare il collegamento con il server",3);
            return sRet;
        }

        // Genero il json sulla base dello user e della password seguendo il protocollo.
        try {
            oJson.put("sComando", sComando);
            oJson.put("sUser", sUser);
            oJson.put("sPassword", sPassword);
        }catch(org.json.JSONException e){

        }

        sJson = oJson.toString();

        try {
            oSocket.write(sJson);
            sJson = oSocket.read();
        }catch(java.io.IOException e){
            return sRet;
        }

        try {
            oJson = new JSONObject(sJson);
            sRet = oJson.getString("sCookie");
        }catch(org.json.JSONException e){}

        return sRet;
    }

    /*
    *   Cosa fa             :               Registra un nuovo utente all'interno del server
    *   aUser               :               assocarray, array con i dati dell'utente, così formato:
    *                                           ["sNome"] => "Luca"
    *                                           ["sCognome"] => "Bertoni"
    *                                           ["sEmail"] => "luca.bertoni24@gmail.com"
    *                                           ["sUsername"] => "lucabertoni"
    *                                           ["sPassword"] => "b9be11166d72e9e3ae7fd407165e4bd2" (md5(md5("root")))
    *   Ritorna             :               bRet -> logico, true = Utente aggiunto | false = utente non aggiunto, errore
    *
    *   CLIENT: {'sComando': “addUser”, 'aUtente':{'sNome':'Luca',sCognome:'Bertoni','sEmail':'luca.bertoni24@gmail.com','sUsername':'lucabertoni','sPassword':'b9be11166d72e9e3ae7fd407165e4bd2','nLivello':1}}
    *   SERVER: {'sRisultato':'OK'} | {'sRisultato':'NO'}
    * */
    public boolean addUser(Map<String, String> aUser){
        boolean bRet = false;
        String sJson,sComando,sRisposta;

        sRisposta = "";
        lnSocket oSocket;
        JSONObject oJson = new JSONObject();

        sComando = "AddUser";

        // Mi collego con il server...
        try{
            oSocket = this.connect();
        }catch(java.io.IOException e){
            //LogBuffer.write("Login -> Impossibile creare il collegamento con il server",3);
            return bRet;
        }

        // Genero il json sulla base dell'array dei dati dell'utente
        try {
            /*
            *                                           ["sNome"] => "Luca"
            *                                           ["sCognome"] => "Bertoni"
            *                                           ["sEmail"] => "luca.bertoni24@gmail.com"
            *                                           ["sUsername"] => "lucabertoni"
            *                                           ["sPassword"] => "b9be11166d72e9e3ae7fd407165e4bd2" (md5(md5("root")))
            */
            oJson.put("sComando", sComando);
            oJson.put("sNome", aUser.get("sNome"));
            oJson.put("sCognome", aUser.get("sCognome"));
            oJson.put("sUsername", aUser.get("sUsername"));
            oJson.put("sEmail", aUser.get("sEmail"));
            oJson.put("sPassword", aUser.get("sPassword"));
        }catch(org.json.JSONException e){

        }

        sJson = oJson.toString();

        // Scrivo e poi attendo una risposta dal server
        try {
            oSocket.write(sJson);
            sJson = oSocket.read();
        }catch(java.io.IOException e){
            return bRet;
        }

        // Estraggo il risultato
        try {
            oJson = new JSONObject(sJson);
            sRisposta = oJson.getString("sRisultato");
        }catch(org.json.JSONException e){}

        // Se è andato tutto a buon fine, ritorno true
        if(sRisposta.equals("OK"))    bRet = true;

        return bRet;
    }

    /*
     *   Cosa fa            :               Estrapola il nome utente dello user
     *   sCookie            :               stringa, cookie associato all'utente
     *   Ritorna            :               sRet -> stringa, username dell'utente
     *
     *   CLIENT: {'sComando': “getUsername”, 'sCookie':”28c8edde3d61a041121511d3b1866f0636”}
     *   SERVER: {'sRisultato':'OK',”sUsername”:”lucabertoni”} | {'sRisultato':'NO'}
     * */
    public String getUsername(String sCookie){
        String sRet,sJson,sComando;
        sRet = "";
        lnSocket oSocket;
        JSONObject oJson = new JSONObject();

        sComando = "getUsername";

        // Mi collego con il server...
        try{
            oSocket = this.connect();
        }catch(java.io.IOException e){
            //LogBuffer.write("Login -> Impossibile creare il collegamento con il server",3);
            return sRet;
        }

        // Genero il json sulla base dell'array dei dati dell'utente
        try {
            oJson.put("sComando", sComando);
            oJson.put("sCookie", sCookie);
        }catch(org.json.JSONException e){

        }

        sJson = oJson.toString();

        // Scrivo e poi attendo una risposta dal server
        try {
            oSocket.write(sJson);
            sJson = oSocket.read();
        }catch(java.io.IOException e){
            return sRet;
        }

        // Estraggo il risultato
        try {
            oJson = new JSONObject(sJson);
            sRet = oJson.getString("sUsername");
        }catch(org.json.JSONException e){}

        return sRet;
    }


    /*
     *   Cosa fa            :               Estrae tutte le informazioni dell'utente
     *   sCookie            :               stringa, cookie associato all'utente
     *   Ritorna            :               aRet -> assocarray, dati dell'utente, così formato:
     *                                           ["sNome"]      => "Luca"
     *                                           ["sCognome"]   => "Bertoni"
     *                                           ["sEmail"]     => "luca.bertoni24@gmail.com"
     *                                           ["sUsername"]  => "lucabertoni"
     *                                           ["sPassword"]  => "b9be11166d72e9e3ae7fd407165e4bd2" (md5(md5("root")))
     *                                           ["nLivello"]   => "1"
     *
     *   CLIENT: {'sComando': “getAllUserInfo”, 'sCookie':”28c8edde3d61a041121511d3b1866f0636”}
     *   SERVER:{'sRisultato':'OK', ”aUser”:{'sNome':'Luca',sCognome:'Bertoni','sEmail':'luca.bertoni24@gmail.com','sUsername':'lucabertoni','sPassword':'b9be11166d72e9e3ae7fd407165e4bd2','nLivello':1}} | {'sRisultato':'NO'}
     * */
    public Map<String,String> getAllUserInfo(String sCookie){
        String sJson,sComando;
        Map<String,String> aRet = new HashMap();
        lnSocket oSocket;
        JSONObject oJson = new JSONObject();

        sComando = "getAllUserInfo";

        // Mi collego con il server...
        try{
            oSocket = this.connect();
        }catch(java.io.IOException e){
            //LogBuffer.write("Login -> Impossibile creare il collegamento con il server",3);
            return aRet;
        }

        // Genero il json sulla base dell'array dei dati dell'utente
        try {
            oJson.put("sComando", sComando);
            oJson.put("sCookie", sCookie);
        }catch(org.json.JSONException e){

        }

        sJson = oJson.toString();

        // Scrivo e poi attendo una risposta dal server
        try {
            oSocket.write(sJson);
            sJson = oSocket.read();
        }catch(java.io.IOException e){
            return aRet;
        }

        Log.d("JSON",sJson);
        // Estraggo il risultato
        try {
            oJson = new JSONObject(sJson);
            oJson = oJson.getJSONObject("aUser");
            /**
            *                                           ["sNome"]      => "Luca"
            *                                           ["sCognome"]   => "Bertoni"
            *                                           ["sEmail"]     => "luca.bertoni24@gmail.com"
            *                                           ["sUsername"]  => "lucabertoni"
            *                                           ["sPassword"]  => "b9be11166d72e9e3ae7fd407165e4bd2" (md5(md5("root")))
            *                                           ["nLivello"]   => "1"
            **/
            aRet.put("sNome", oJson.getString("sNome"));
            aRet.put("sCognome",oJson.getString("sCognome"));
            aRet.put("sEmail",oJson.getString("sEmail"));
            aRet.put("sUsername",oJson.getString("sUsername"));
            aRet.put("sPassword",oJson.getString("sPassword"));
            aRet.put("nLivello",oJson.getString("nLivello"));
        }catch(org.json.JSONException e){
            Log.d("GETALLUSERINFO","ERRORE: " + e);
        }

        return aRet;
    }
}