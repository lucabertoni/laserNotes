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
void diconnect(){
    // TODO: Implementare metodo
    return;
}
