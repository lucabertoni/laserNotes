/*==================================
=            INCLUSIONI            =
==================================*/

/*----------  Librerie di sistema  ----------*/
#include <strings.h>
#include <stdlib.h>

#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <sys/types.h>
#include <netdb.h>
/*----------  Librerie definite dal programmatore  ----------*/
#include "lnsocket.h"

/*=====  End of INCLUSIONI  ======*/

/*================================================
=            IMPLEMENTAZIONI FUNZIONI            =
================================================*/
/*
 * Cosa fa          :           Imposta i valori dell'indirizzo ip al quale deve connettersi la socket e quale porta deve usare
 * ip               :           stringa, indirizzo ip al quale connettersi
 * port             :           intero, porta da utilizzare
*/
Socket::Socket(string ip, int port){
    /*
     * Cosa fa          :           Crea una socket usando come protocollo AF_INET
    */
    this->createSocket();

    // Tipo di indirizzo
    this->stSock.sin_family = AF_INET;

    /*
     * Cosa fa          :           Imposta la porta da usare per la socket
     * port             :           intero, numero della porta
    */
    this->setPort(port);

    /*
     * Cosa fa          :           Imposta l'host da usare per la socket
     * ip               :           stringa, indirizzo ip
    */
    this->setHost(ip);
    return;
}

/*
 * Cosa fa          :           Imposta l'host da usare per la socket
 * ip               :           stringa, indirizzo ip
*/
void Socket::setHost(string ip){
    const char* ip_address = ip.c_str();

    this->stSock.sin_addr.s_addr = inet_addr(ip_address);

    return;
}

/*
 * Cosa fa          :           Imposta la porta da usare per la socket
 * port             :           intero, numero della porta
*/
void Socket::setPort(int port){
    this->stSock.sin_port = htons(port);
    return;
}

/*
 * Cosa fa          :           Estrae l'indirizzo ip che utilizza la socket
 * Ritorna          :           stringa, indirizzo ip in formato stringa
*/
string Socket::getIp(){
    //return this->host->h_name;
    return "";
}

/*
 * Cosa fa          :           Estrae la porta che utilizza la socket
 * Ritorna          :           intero, numero della porta utilizzata dalla socket
*/
int Socket::getPort(){
    return ntohs(this->stSock.sin_port);
}

/*
 * Cosa fa          :           Crea una socket usando come protocollo AF_INET
*/
void Socket::createSocket(){
    this->sock=socket(AF_INET, SOCK_STREAM, 0);
    return;
}

/*
 * Cosa fa          :           Apre la connessione con l'host
 * Ritorna          :           bRet -> logico, true = connessione stabilita | false = connessione non stabilita
*/
bool Socket::open(){
    bool bRet;
    int nConnection;

    // Di default imposto che ci sia un errore
    bRet = false;

    // Se l'indirizzo ip utilizzato non è valido, ritorno
/*
    if(this->host == 0){
        return bRet;
    }
*/
    // Ritorna 0 nel caso la connessione sia stata stabilita correttamente
    nConnection = connect(this->sock, (struct sockaddr*)&this->stSock, sizeof(this->stSock));

    // Imposto il valore di ritorno a true se la connessione è stata stabilita correttamente
    nConnection == 0 ? bRet = true : bRet = false;
    return bRet;
}

/*
 * Cosa fa          :           Chiude la comunicazione
*/
void Socket::closeSocket(){
    close(this->sock);
    return;
}
/*=====  End of IMPLEMENTAZIONI FUNZIONI  ======*/
