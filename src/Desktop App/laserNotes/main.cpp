#include "lasernotes.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    laserNotes w;
    w.show();

    return a.exec();
}
