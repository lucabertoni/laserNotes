package app.lasernotes.org.lasernotes;

import java.net.InetAddress;
import java.net.UnknownHostException;

/**
 * Classe che gestisce le socket
 */
public class Socket {
    Socket oSocket;

    /*
    * Cosa fa           :           Crea una socket sulla base dei parametri
    * sHost             :           stringa, indirizzo dell'host
    * nPort             :           numerico, numero della porta dell'host
    * */
    Socket(String sHost, int nPort){
        // Ha bisogno del try-catch con eccezione "UnknownHostException"
        try{
            // Converto l'indirizzo dell'host passato come parametro nel formato necessario per la Socket
            InetAddress sIp = InetAddress.getByName(sHost);
        }catch(UnknownHostException e){

        }
        this.oSocket = new Socket(sHost,nPort);
    }


}
