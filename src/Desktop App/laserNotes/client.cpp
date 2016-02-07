#include "client.h"

/*
 * Cosa fa          :           Imposta il client sulla base di diversi parametri
 * server_ip        :           intero, indirizzo ip del server al quale connettersi
 * port             :           intero, numero della porta alla quale connettersi
*/
Client::Client(string server_ip, int port){
    /*
     * Cosa fa          :           Imposta i valori dell'indirizzo ip al quale deve connettersi la socket e quale porta deve usare
     * ip               :           stringa, indirizzo ip al quale connettersi
     * port             :           intero, porta da utilizzare
    */
    this->oSocket = new Socket(server_ip,port);
}

/*
 * Cosa fa          :           Si connette al server
 * Ritorna          :           bRet -> logico, true = Connessione stabilita | false = Errore durante la connessione
*/
bool Client::connect(){
    bool bRet;

    bRet = false;

    /*
     * Cosa fa          :           Apre la connessione con l'host
     * Ritorna          :           bRet -> logico, true = connessione stabilita | false = connessione non stabilita
    */
    bRet = this->oSocket->open();

    return bRet;
}

/*
 * Cosa fa          :           Si disconnette al server
*/
void Client::diconnect(){
    /*
     * Cosa fa          :           Chiude la comunicazione
    */
    this->oSocket->closeSocket();
    return;
}

/*
 * Cosa fa          :           Effettua il login al server.
 * username         :           stringa, username da utilizzare per effettuare l'accesso
 * password         :           stringa, password da utilizzare per l'accesso, criptata con doppio md5
 *
 * Ritorna          :           sCookie -> stringa, cookie con il quale eseguire le operazioni. "" = Errore login
*/
string Client::login(string username, string password){
    string sCookie;

    sCookie = "";


    return sCookie;
}

/*
 * Cosa fa         :           Rilascia dalla memoria le risorse che ha allocato
*/
Client::~Client(){
    delete this->oSocket;
}
