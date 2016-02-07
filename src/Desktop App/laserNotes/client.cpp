#include "client.h"
#include "include/rapidjson/rapidjson.h"
#include "include/rapidjson/document.h"
#include "include/rapidjson/writer.h"
#include "include/rapidjson/stringbuffer.h"

using namespace rapidjson;

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
void Client::disconnect(){
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
    string sCookie,sJson;
    Document oJson;

    sCookie = "";

    StringBuffer oBuffer;
    Writer<StringBuffer> oWriter(oBuffer);

    // Compongo gli elementi del json
    oWriter.StartObject();              // Aggiunge "{"
    oWriter.String("sComando");         // Aggiunge una chiave
    oWriter.String(_LOGIN_COMMAND);     // Aggiunge un valore
    oWriter.String("sUser");
    oWriter.String(username.c_str());
    oWriter.String("sPassword");
    oWriter.String(password.c_str());
    oWriter.EndObject();                // Aggiunge "}"

    // Estraggo il json in formato stringa
    sJson = oBuffer.GetString();

    // Invio il json al server
    /*
     * Cosa fa          :           Scrive sulla socket
     * message          :           stringa, testo da scrivere sulla socket
    */
    this->oSocket->write_buffer(sJson);

    /*
     * Cosa fa          :           Legge dalla socket
     * Ritorna          :           sRet -> stringa, buffer letto dalla socket
    */
    sJson = this->oSocket->read_buffer();

    oJson.Parse(sJson.c_str());
    if(oJson.HasMember("sRisultato")){
        if(strcmp(oJson["sRisultato"].GetString(), _RESULT_OK) == 0){
            sCookie = oJson["sCookie"].GetString();
        }
    }

    return sCookie;
}

/*
 * Cosa fa         :           Rilascia dalla memoria le risorse che ha allocato
*/
Client::~Client(){
    /*
     * Cosa fa          :           Chiude la comunicazione
    */
    this->oSocket->closeSocket();
    delete this->oSocket;
}

/*
 * Cosa fa          :           Imposta il cookie da usare per lo scambio di dati
 * sCookie          :           stringa, cookie da usare
*/
void Client::setCookie(string sCookie){
    this->sCookie = sCookie;
}

/*
 * Cosa fa          :           Estrae il cookie impostato
 * Ritorna          :           stringa, cookie attualmente in uso
*/
string Client::getCookie(){
    return this->sCookie;
}

/*
 * Cosa fa          :           Richiede al server l'username dell'utente
 * Ritorna          :           sUsername -> stringa, username dell'utente
*/
string Client::getUsername(){
    string sUsername,sJson;
    Document oJson;

    sUsername = "";

    StringBuffer oBuffer;
    Writer<StringBuffer> oWriter(oBuffer);

    // Compongo gli elementi del json
    oWriter.StartObject();              // Aggiunge "{"
    oWriter.String("sComando");         // Aggiunge una chiave
    oWriter.String(_GETUSERNAME_COMMAND);     // Aggiunge un valore
    oWriter.String("sCookie");
    oWriter.String(this->getCookie().c_str());
    oWriter.EndObject();                // Aggiunge "}"

    // Estraggo il json in formato stringa
    sJson = oBuffer.GetString();

    // Invio il json al server
    /*
     * Cosa fa          :           Scrive sulla socket
     * message          :           stringa, testo da scrivere sulla socket
    */
    this->oSocket->write_buffer(sJson);

    /*
     * Cosa fa          :           Legge dalla socket
     * Ritorna          :           sRet -> stringa, buffer letto dalla socket
    */
    sJson = this->oSocket->read_buffer();

    oJson.Parse(sJson.c_str());
    if(oJson.HasMember("sRisultato")){
        if(strcmp(oJson["sRisultato"].GetString(), _RESULT_OK) == 0){
            sCookie = oJson["sUsername"].GetString();
        }
    }

    return sUsername;
}
