#include "mainwindow.h"
#include "pantallas/MainMenu.h"
#include "pantallas/PermutacionCombinacion.h"
#include "pantallas/ProductoCartesiano.h"
#include "pantallas/DiagramaVenn.h"
#include "pantallas/Resultados.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
{
    stackedWidget = new QStackedWidget(this);
    
    pantallaMenu = new MainMenu(this);
    pantallaPerm = new PermutacionCombinacion(this);
    pantallaCart = new ProductoCartesiano(this);
    pantallaVenn = new DiagramaVenn(this);
    pantallaRes = new Resultados(this);
    
    stackedWidget->addWidget(pantallaMenu); // index 0
    stackedWidget->addWidget(pantallaPerm); // index 1
    stackedWidget->addWidget(pantallaCart); // index 2
    stackedWidget->addWidget(pantallaVenn); // index 3
    stackedWidget->addWidget(pantallaRes);  // index 4
    
    setCentralWidget(stackedWidget);
    stackedWidget->setCurrentWidget(pantallaMenu);
}

MainWindow::~MainWindow()
{
}

void MainWindow::mostrarMenuPrincipal() {
    stackedWidget->setCurrentWidget(pantallaMenu);
}

void MainWindow::mostrarPermutaciones() {
    stackedWidget->setCurrentWidget(pantallaPerm);
}

void MainWindow::mostrarCartesiano() {
    stackedWidget->setCurrentWidget(pantallaCart);
}

void MainWindow::mostrarVenn() {
    stackedWidget->setCurrentWidget(pantallaVenn);
}

void MainWindow::mostrarResultados(const QString& titulo, const QString& contenido) {
    pantallaRes->setResultados(titulo, contenido);
    stackedWidget->setCurrentWidget(pantallaRes);
}
