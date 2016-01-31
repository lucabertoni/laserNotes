#include "lasernotes.h"
#include "ui_lasernotes.h"
#include "client.h"

laserNotes::laserNotes(QWidget *parent) : QMainWindow(parent), ui(new Ui::laserNotes){    
    bool bConnected;

    ui->setupUi(this);

    // Creo l'oggetto Client che gestisce le comunicazioni con il server
    this->oClient = new Client("192.168.1.9",52000);

    /*
     * Cosa fa          :           Si connette al server
     * Ritorna          :           bRet -> logico, true = Connessione stabilita | false = Errore durante la connessione
    */
    bConnected = this->oClient->connect();
    if(bConnected){
        ui->labelUsername->setText("LOOL");
    }

}

laserNotes::~laserNotes(){
    delete ui;
}
