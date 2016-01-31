#ifndef LASERNOTES_H
#define LASERNOTES_H

#include <QMainWindow>

#include "client.h"

namespace Ui {
class laserNotes;
}

class laserNotes : public QMainWindow
{
    Q_OBJECT

public:
    explicit laserNotes(QWidget *parent = 0);
    ~laserNotes();

private:
    Ui::laserNotes *ui;
    Client *oClient;
};

#endif // LASERNOTES_H
