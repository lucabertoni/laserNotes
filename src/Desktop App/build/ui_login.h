/********************************************************************************
** Form generated from reading UI file 'login.ui'
**
** Created by: Qt User Interface Compiler version 5.5.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_LOGIN_H
#define UI_LOGIN_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QFrame>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Login
{
public:
    QWidget *centralwidget;
    QFrame *frameHeader;
    QLabel *label;
    QLabel *label_2;
    QFrame *frameForm;
    QLabel *label_3;
    QLineEdit *entryfieldUsername;
    QLabel *label_4;
    QLineEdit *entryfieldPassword;
    QPushButton *pushButton;

    void setupUi(QMainWindow *Login)
    {
        if (Login->objectName().isEmpty())
            Login->setObjectName(QStringLiteral("Login"));
        Login->resize(350, 350);
        Login->setMinimumSize(QSize(350, 350));
        Login->setMaximumSize(QSize(350, 350));
        Login->setStyleSheet(QStringLiteral(""));
        centralwidget = new QWidget(Login);
        centralwidget->setObjectName(QStringLiteral("centralwidget"));
        frameHeader = new QFrame(centralwidget);
        frameHeader->setObjectName(QStringLiteral("frameHeader"));
        frameHeader->setGeometry(QRect(0, 0, 350, 50));
        frameHeader->setAutoFillBackground(false);
        frameHeader->setStyleSheet(QStringLiteral("background-color: rgb(0, 150, 136)"));
        frameHeader->setFrameShape(QFrame::StyledPanel);
        frameHeader->setFrameShadow(QFrame::Raised);
        label = new QLabel(frameHeader);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(80, 10, 160, 30));
        QFont font;
        font.setFamily(QStringLiteral("Monospace"));
        font.setPointSize(20);
        font.setBold(false);
        font.setWeight(50);
        label->setFont(font);
        label->setTextFormat(Qt::AutoText);
        label->setScaledContents(false);
        label->setAlignment(Qt::AlignCenter);
        label_2 = new QLabel(frameHeader);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setGeometry(QRect(250, 10, 27, 27));
        label_2->setPixmap(QPixmap(QString::fromUtf8(":/pencil-icon")));
        frameForm = new QFrame(centralwidget);
        frameForm->setObjectName(QStringLiteral("frameForm"));
        frameForm->setGeometry(QRect(0, 50, 350, 350));
        frameForm->setStyleSheet(QStringLiteral("background-color:white;"));
        frameForm->setFrameShape(QFrame::StyledPanel);
        frameForm->setFrameShadow(QFrame::Raised);
        label_3 = new QLabel(frameForm);
        label_3->setObjectName(QStringLiteral("label_3"));
        label_3->setGeometry(QRect(50, 50, 135, 19));
        QFont font1;
        font1.setPointSize(12);
        font1.setKerning(true);
        label_3->setFont(font1);
        label_3->setStyleSheet(QStringLiteral("color:black;"));
        label_3->setLineWidth(1);
        entryfieldUsername = new QLineEdit(frameForm);
        entryfieldUsername->setObjectName(QStringLiteral("entryfieldUsername"));
        entryfieldUsername->setGeometry(QRect(50, 75, 260, 30));
        QFont font2;
        font2.setPointSize(10);
        entryfieldUsername->setFont(font2);
        entryfieldUsername->setStyleSheet(QLatin1String("color:black;\n"
"border:1px solid rgb(0, 150, 136);\n"
"border-radius:2px;"));
        label_4 = new QLabel(frameForm);
        label_4->setObjectName(QStringLiteral("label_4"));
        label_4->setGeometry(QRect(50, 125, 77, 19));
        QFont font3;
        font3.setPointSize(12);
        label_4->setFont(font3);
        label_4->setStyleSheet(QStringLiteral("color:black;"));
        label_4->setLineWidth(1);
        entryfieldPassword = new QLineEdit(frameForm);
        entryfieldPassword->setObjectName(QStringLiteral("entryfieldPassword"));
        entryfieldPassword->setGeometry(QRect(50, 150, 260, 30));
        entryfieldPassword->setFont(font2);
        entryfieldPassword->setStyleSheet(QLatin1String("color:black;\n"
"border:1px solid rgb(0, 150, 136);\n"
"border-radius:2px;"));
        entryfieldPassword->setEchoMode(QLineEdit::Password);
        pushButton = new QPushButton(frameForm);
        pushButton->setObjectName(QStringLiteral("pushButton"));
        pushButton->setEnabled(true);
        pushButton->setGeometry(QRect(210, 200, 103, 45));
        pushButton->setFont(font3);
        pushButton->setFocusPolicy(Qt::TabFocus);
        pushButton->setToolTipDuration(-1);
        pushButton->setLayoutDirection(Qt::RightToLeft);
        pushButton->setAutoFillBackground(false);
        pushButton->setStyleSheet(QLatin1String("text-align:left;\n"
"padding:1em;\n"
"background-color: rgb(0, 150, 136);"));
        QIcon icon;
        icon.addFile(QStringLiteral(":/forward-icon"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton->setIcon(icon);
        pushButton->setIconSize(QSize(27, 27));
        pushButton->setAutoRepeat(false);
        pushButton->setFlat(false);
        Login->setCentralWidget(centralwidget);

        retranslateUi(Login);

        pushButton->setDefault(false);


        QMetaObject::connectSlotsByName(Login);
    } // setupUi

    void retranslateUi(QMainWindow *Login)
    {
        Login->setWindowTitle(QApplication::translate("Login", "laserNotes - Login", 0));
        label->setText(QApplication::translate("Login", "laserNotes", 0));
        label_2->setText(QString());
        label_3->setText(QApplication::translate("Login", "Username / Email", 0));
        entryfieldUsername->setInputMask(QString());
        entryfieldUsername->setText(QString());
        entryfieldUsername->setPlaceholderText(QApplication::translate("Login", "Username / example@domain.com", 0));
        label_4->setText(QApplication::translate("Login", "Password", 0));
        entryfieldPassword->setInputMask(QString());
        entryfieldPassword->setText(QString());
        entryfieldPassword->setPlaceholderText(QString());
#ifndef QT_NO_TOOLTIP
        pushButton->setToolTip(QApplication::translate("Login", "Effettua il login", 0));
#endif // QT_NO_TOOLTIP
        pushButton->setText(QApplication::translate("Login", "Entra", 0));
    } // retranslateUi

};

namespace Ui {
    class Login: public Ui_Login {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_LOGIN_H
