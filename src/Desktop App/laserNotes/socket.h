#ifndef SOCKET_H
#define SOCKET_H


                /*==================================
                =            INCLUSIONI            =
                ==================================*/

        /*----------  Librerie di sistema  ----------*/
#include <string>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>     // "in" per "sockaddr_in"
#include <netdb.h>          // per "gethostbyname"
#include <unistd.h>         // Utilizzato per funzione close()

        /*----------  Librerie definite dal programmatore  ----------*/
                /*=====  End of INCLUSIONI  ======*/

using namespace std;

class Socket
{

                /*=================================
                =            PROTOTIPI            =
                =================================*/

    /*----------  Definizione tipi/struct/attributi  ----------*/

private:
    /*
     * host             :           host al quale connettersi con la socket
     * stSock           :           struttura che definisce la socket (porta, protocollo)
     * sock             :           intero, descrittore della socket
    */
    struct hostent *host;
    struct sockaddr_in *stSock;
    int sock;

    /*----------  Funzioni/Metodi  ----------*/
public:
    /*
     * Cosa fa          :           Imposta i valori dell'indirizzo ip al quale deve connettersi la socket e quale porta deve usare
     * ip               :           stringa, indirizzo ip al quale connettersi
     * port             :           intero, porta da utilizzare
    */
    Socket(string ip, int port);

private:
    /*
     * Cosa fa          :           Imposta l'host da usare per la socket
     * ip               :           stringa, indirizzo ip
    */
    void setHost(string ip);


    /*
     * Cosa fa          :           Imposta la porta da usare per la socket
     * port             :           intero, numero della porta
    */
    void setPort(int port);

    /*
     * Cosa fa          :           Crea una socket usando come protocollo AF_INET
    */
    void createSocket();

public:
    /*
     * Cosa fa          :           Estrae l'indirizzo ip che utilizza la socket
     * Ritorna          :           stringa, indirizzo ip in formato stringa
    */
    string getIp();

    /*
     * Cosa fa          :           Estrae la porta che utilizza la socket
     * Ritorna          :           intero, numero della porta utilizzata dalla socket
    */
    int getPort();

    /*
     * Cosa fa          :           Apre la connessione con l'host
     * Ritorna          :           bRet -> logico, true = connessione stabilita | false = connessione non stabilita
    */
    bool open();

    /*
     * Cosa fa          :           Chiude la comunicazione
    */
    void closeSocket();

                /*=====  End of PROTOTIPI  ======*/
};

#endif // SOCKET_H
