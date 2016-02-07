#-------------------------------------------------
#
# Project created by QtCreator 2016-01-31T16:03:28
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = laserNotes
TEMPLATE = app


SOURCES += main.cpp\
        lasernotes.cpp \
    client.cpp \
    user.cpp \
    login.cpp \
    lnsocket.cpp \
    common.cpp \
    md5.cpp

HEADERS  += \
    client.h \
    user.h \
    lasernotes.h \
    login.h \
    lnsocket.h \
    common.h \
    md5.h

FORMS    += lasernotes.ui \
    login.ui

RESOURCES = resource.qrc
