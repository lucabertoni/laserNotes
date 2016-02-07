/********************************************************************************
** Form generated from reading UI file 'home.ui'
**
** Created by: Qt User Interface Compiler version 5.5.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_HOME_H
#define UI_HOME_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QFrame>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Home
{
public:
    QWidget *centralWidget;
    QFrame *headerFrane;
    QPushButton *pushbuttonMenu;
    QLabel *labelUsername;
    QPushButton *pushbuttonAltro;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *Home)
    {
        if (Home->objectName().isEmpty())
            Home->setObjectName(QStringLiteral("Home"));
        Home->setEnabled(true);
        Home->resize(800, 600);
        Home->setMinimumSize(QSize(800, 600));
        Home->setMaximumSize(QSize(800, 600));
        Home->setAutoFillBackground(false);
        Home->setStyleSheet(QStringLiteral("background-color:white;"));
        centralWidget = new QWidget(Home);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        headerFrane = new QFrame(centralWidget);
        headerFrane->setObjectName(QStringLiteral("headerFrane"));
        headerFrane->setGeometry(QRect(0, 0, 800, 50));
        headerFrane->setAutoFillBackground(false);
        headerFrane->setStyleSheet(QStringLiteral("background-color: rgb(0, 150, 136)"));
        headerFrane->setFrameShape(QFrame::StyledPanel);
        headerFrane->setFrameShadow(QFrame::Raised);
        pushbuttonMenu = new QPushButton(headerFrane);
        pushbuttonMenu->setObjectName(QStringLiteral("pushbuttonMenu"));
        pushbuttonMenu->setGeometry(QRect(0, 0, 50, 50));
        pushbuttonMenu->setStyleSheet(QStringLiteral("border:none;"));
        QIcon icon;
        icon.addFile(QStringLiteral(":/menu-icon"), QSize(), QIcon::Normal, QIcon::Off);
        pushbuttonMenu->setIcon(icon);
        pushbuttonMenu->setIconSize(QSize(27, 27));
        labelUsername = new QLabel(headerFrane);
        labelUsername->setObjectName(QStringLiteral("labelUsername"));
        labelUsername->setGeometry(QRect(580, 0, 200, 50));
        QFont font;
        font.setFamily(QStringLiteral("Nimbus Sans L"));
        font.setPointSize(16);
        font.setItalic(false);
        labelUsername->setFont(font);
        labelUsername->setTextFormat(Qt::AutoText);
        labelUsername->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        labelUsername->setMargin(10);
        pushbuttonAltro = new QPushButton(headerFrane);
        pushbuttonAltro->setObjectName(QStringLiteral("pushbuttonAltro"));
        pushbuttonAltro->setGeometry(QRect(780, 15, 20, 20));
        pushbuttonAltro->setStyleSheet(QStringLiteral("border:none;"));
        QIcon icon1;
        icon1.addFile(QStringLiteral(":/drop-down-icon"), QSize(), QIcon::Normal, QIcon::Off);
        pushbuttonAltro->setIcon(icon1);
        pushbuttonAltro->setIconSize(QSize(27, 27));
        Home->setCentralWidget(centralWidget);
        statusBar = new QStatusBar(Home);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        Home->setStatusBar(statusBar);

        retranslateUi(Home);

        QMetaObject::connectSlotsByName(Home);
    } // setupUi

    void retranslateUi(QMainWindow *Home)
    {
        Home->setWindowTitle(QApplication::translate("Home", "laserNotes", 0));
        pushbuttonMenu->setText(QString());
        labelUsername->setText(QApplication::translate("Home", "Nome utente", 0));
        pushbuttonAltro->setText(QString());
    } // retranslateUi

};

namespace Ui {
    class Home: public Ui_Home {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_HOME_H
