#ifndef HOME_H
#define HOME_H

#include <QMainWindow>

#include "client.h"

namespace Ui {
class Home;
}

class Home : public QMainWindow
{
    Q_OBJECT

public:
    explicit Home(QWidget *parent = 0);

    /*
     * Cosa fa              :               Crea la classe sulla base di una connessione con il server prestabilita
     * oClient              :               Client, oggetto client con vari settings(cookie,...) e con socket aperta verso il server
    */
    explicit Home(QWidget *parent = 0, Client *oClient = 0);
    ~Home();

private:
    Ui::Home *ui;
    Client *oClient;
};

#endif // LASERNOTES_H
