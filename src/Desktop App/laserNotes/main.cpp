#include "home.h"
#include "login.h"
#include <QApplication>
#include <QRect>
#include <QDesktopWidget>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Login w;
    float x,y;

    // Centro la finestra sullo schermo
    QRect screenGeometry = QApplication::desktop()->screenGeometry();
    x = (screenGeometry.width()-w.width()) / 2;
    y = (screenGeometry.height()-w.height()) / 2;
    w.move(x, y);

    w.show();

    return a.exec();
}
