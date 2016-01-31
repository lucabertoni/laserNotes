#include "lasernotes.h"
#include "ui_lasernotes.h"

laserNotes::laserNotes(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::laserNotes)
{
    ui->setupUi(this);
}

laserNotes::~laserNotes()
{
    delete ui;
}
