package app.lasernotes.org.lasernotes;

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
    * Cosa fa           :           Effettua il login comunicando con l'host
    * sUser             :           stringa, username per loggarsi
    * sPassword         :           stringa, md5(md5(della password))
    * Ritorna           :           sRet -> json, così formato: {'sRisultato':”OK”, sCookie:””} | {'sRisultato':”NO”}
    * */
    String login(String sUser,String sPassword){
        String sRet;
        sRet = "";

        return sRet;
    }
}
