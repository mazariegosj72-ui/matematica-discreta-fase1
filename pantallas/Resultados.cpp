#include "Resultados.h"
#include "../mainwindow.h"
#include <QVBoxLayout>
#include <QPushButton>

Resultados::Resultados(MainWindow *parent) : QWidget(parent), mainWindow(parent)
{
    QVBoxLayout *layout = new QVBoxLayout(this);
    
    lblTitulo = new QLabel("Resultados", this);
    lblTitulo->setStyleSheet("font-size: 20px; font-weight: bold;");
    
    txtContenido = new QTextEdit(this);
    txtContenido->setReadOnly(true);
    txtContenido->setStyleSheet("font-size: 14px;");
    
    QPushButton *btnVolver = new QPushButton("Volver al Menú Principal", this);
    btnVolver->setMinimumHeight(40);
    
    layout->addWidget(lblTitulo);
    layout->addWidget(txtContenido);
    layout->addWidget(btnVolver);
    
    connect(btnVolver, &QPushButton::clicked, mainWindow, &MainWindow::mostrarMenuPrincipal);
}

void Resultados::setResultados(const QString& titulo, const QString& contenido) {
    lblTitulo->setText(titulo);
    txtContenido->setText(contenido);
}
