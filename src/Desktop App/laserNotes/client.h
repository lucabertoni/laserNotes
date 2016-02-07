#ifndef CLIENT_H
#define CLIENT_H

#include <string>

#include "user.h"   // File che definisce la classe per la gestione dell'utente
#include "lnsocket.h"

#define _RESULT_OK              "OK"
#define _GETUSERNAME_COMMAND    "GETUSERNAME"
#define _LOGIN_COMMAND          "LOGIN"

using namespace std;

class Client
{
private:
    Socket *oSocket;
    string sCookie;

public:
    /*
     * Cosa fa          :           Imposta il client sulla base di diversi parametri
     * server_ip        :           intero, indirizzo ip del server al quale connettersi
     * port             :           intero, numero della porta alla quale connettersi
    */
    Client(string server_ip, int port);

    /*
     * Cosa fa          :           Si connette al server
     * Ritorna          :           bRet -> logico, true = Connessione stabilita | false = Errore durante la connessione
    */
    bool connect();

    /*
     * Cosa fa          :           Effettua il login al server.
     * username         :           stringa, username da utilizzare per effettuare l'accesso
     * password         :           stringa, password da utilizzare per l'accesso, criptata con doppio md5
     *
     * Ritorna          :           sCookie -> stringa, cookie con il quale eseguire le operazioni. "" = Errore login
    */
    string login(string username, string password);

    /*
     * Cosa fa          :           Si disconnette al server
    */
    void disconnect();

    /*
     * Cosa fa         :           Rilascia dalla memoria le risorse che ha allocato
    */
    ~Client();

    /*
     * Cosa fa          :           Imposta il cookie da usare per lo scambio di dati
     * sCookie          :           stringa, cookie da usare
    */
    void setCookie(string sCookie);

    /*
     * Cosa fa          :           Estrae il cookie impostato
     * Ritorna          :           stringa, cookie attualmente in uso
    */
    string getCookie();

    /*
     * Cosa fa          :           Richiede al server l'username dell'utente
     * Ritorna          :           sUsername -> stringa, username dell'utente
    */
    string getUsername();
};

#endif // CLIENT_H
