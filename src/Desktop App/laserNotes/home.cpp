#include "home.h"
#include "ui_home.h"
#include "client.h"

Home::Home(QWidget *parent) : QMainWindow(parent), ui(new Ui::Home){
    bool bConnected;

    ui->setupUi(this);

    // Creo l'oggetto Client che gestisce le comunicazioni con il server
    this->oClient = new Client("192.168.1.9",52000);

    /*
     * Cosa fa          :           Si connette al server
     * Ritorna          :           bRet -> logico, true = Connessione stabilita | false = Errore durante la connessione
    */
    bConnected = this->oClient->connect();

    // Se non sono riuscito ad effettuare la connessione, riprovo N volte con uno sleep di 1 secondo
    if(!bConnected){

    }

}

/*
 * Cosa fa              :               Crea la classe sulla base di una connessione con il server prestabilita
 * oClient              :               Client, oggetto client con vari settings(cookie,...) e con socket aperta verso il server
*/
Home::Home(QWidget *parent, Client *oClient) : QMainWindow(parent), ui(new Ui::Home){
    string sUsername;
    ui->setupUi(this);

    // Creo l'oggetto Client che gestisce le comunicazioni con il server
    this->oClient = oClient;

    /*
     * Cosa fa          :           Richiede al server l'username dell'utente
     * Ritorna          :           sUsername -> stringa, username dell'utente
    */
    sUsername = this->oClient->getUsername();
    //this->ui->labelUsername->setText(sUsername.c_str());
}

Home::~Home(){
    delete ui;
}
