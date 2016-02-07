#include "ui_login.h"
#include <QMessageBox>
#include <QString>
#include <QRect>
#include <QDesktopWidget>

#include "md5.h"

#include "login.h"
#include "home.h"

Login::Login(QWidget *parent) : QMainWindow(parent), ui(new Ui::Login){
    bool bConnected;
    QMessageBox oMsgBox;

    ui->setupUi(this);

    /*
     * Cosa fa          :           Imposta il client sulla base di diversi parametri
     * server_ip        :           intero, indirizzo ip del server al quale connettersi
     * port             :           intero, numero della porta alla quale connettersi
    */
    // TODO: Prendere server e porta da file
    this->oClient = new Client("192.168.1.9",52000);
    bConnected = this->oClient->connect();
    if(!bConnected){
        oMsgBox.setIcon(QMessageBox::Critical);
        oMsgBox.setText("Impossibile connettersi al server di laserNotes.\nVerificare che sia presente una connesione a internet.\nPrima di continuare è necessario risolvere il problema.");
        oMsgBox.setWindowTitle("Connesione al server non riuscita");
        oMsgBox.setStandardButtons(QMessageBox::Ok);
        oMsgBox.exec();

        this->setEnabled(false);
    }
}

Login::~Login()
{

    /*
     * Cosa fa          :           Si disconnette al server
    */
    this->oClient->disconnect();
    delete oClient;
    delete ui;
}

void Login::on_pushButton_clicked(){
    string sUsername, sPassword, sCookie;
    Home *window;
    QMessageBox oMsgBox;
    float x,y;

    sUsername = this->ui->entryfieldUsername->text().toStdString();
    sPassword = this->ui->entryfieldPassword->text().toStdString();

    sCookie = "";

    if(sUsername == "" || sPassword == ""){
        oMsgBox.setIcon(QMessageBox::Warning);
        oMsgBox.setText("Non sono stati compilati tutti i campi. Per procedere con il login è necessario inserire username e password.");
        oMsgBox.setWindowTitle("Campo vuoto");
        oMsgBox.setStandardButtons(QMessageBox::Ok);
        oMsgBox.setStyleSheet("background-color:white;color:black");
        oMsgBox.exec();
    }else{
        sPassword = md5(md5(this->ui->entryfieldPassword->text().toStdString().c_str()));
        /*
         * Cosa fa          :           Effettua il login al server.
         * username         :           stringa, username da utilizzare per effettuare l'accesso
         * password         :           stringa, password da utilizzare per l'accesso, criptata con doppio md5
         *
         * Ritorna          :           sCookie -> stringa, cookie con il quale eseguire le operazioni. "" = Errore login
        */
        sCookie = this->oClient->login(sUsername, sPassword);

        // Se il cookie non è vuoto significa che il login ha avuto successo
        if(sCookie != ""){

            /*
             * Cosa fa          :           Imposta il cookie da usare per lo scambio di dati
             * sCookie          :           stringa, cookie da usare
            */
            this->oClient->setCookie(sCookie);

            /*
             * Cosa fa              :               Crea la classe sulla base di una connessione con il server prestabilita
             * oClient              :               Client, oggetto client con vari settings(cookie,...) e con socket aperta verso il server
            */
            window = new Home(0, oClient);

            // Centro la finestra sullo schermo
            QRect screenGeometry = QApplication::desktop()->screenGeometry();
            x = (screenGeometry.width()-window->width()) / 2;
            y = (screenGeometry.height()-window->height()) / 2;
            window->move(x, y);
            window->show();

            this->close();
        }else{
            this->oClient->disconnect();
            this->oClient->connect();
        }
    }
}
