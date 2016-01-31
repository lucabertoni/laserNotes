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
    socket.cpp

HEADERS  += lasernotes.h \
    client.h \
    user.h \
    socket.h

FORMS    += lasernotes.ui

RESOURCES = resource.qrc
