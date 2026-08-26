#include "MainMenu.h"
#include "../mainwindow.h"
#include <QVBoxLayout>
#include <QPushButton>
#include <QLabel>

MainMenu::MainMenu(MainWindow *parent) : QWidget(parent), mainWindow(parent)
{
    QVBoxLayout *layout = new QVBoxLayout(this);
    
    QLabel *titulo = new QLabel("Fase 1: Matemática Discreta", this);
    titulo->setAlignment(Qt::AlignCenter);
    titulo->setStyleSheet("font-size: 24px; font-weight: bold; margin-bottom: 20px;");
    
    QPushButton *btnPerm = new QPushButton("Permutaciones y Combinaciones", this);
    QPushButton *btnCart = new QPushButton("Producto Cartesiano", this);
    QPushButton *btnVenn = new QPushButton("Diagrama de Venn (3 Conjuntos)", this);
    
    btnPerm->setMinimumHeight(50);
    btnCart->setMinimumHeight(50);
    btnVenn->setMinimumHeight(50);
    
    layout->addStretch();
    layout->addWidget(titulo);
    layout->addWidget(btnPerm);
    layout->addWidget(btnCart);
    layout->addWidget(btnVenn);
    layout->addStretch();
    
    connect(btnPerm, &QPushButton::clicked, mainWindow, &MainWindow::mostrarPermutaciones);
    connect(btnCart, &QPushButton::clicked, mainWindow, &MainWindow::mostrarCartesiano);
    connect(btnVenn, &QPushButton::clicked, mainWindow, &MainWindow::mostrarVenn);
}
