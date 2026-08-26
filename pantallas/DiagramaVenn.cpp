#include "DiagramaVenn.h"
#include "../mainwindow.h"
#include "../matematica/LogicaMatematica.h"
#include <QVBoxLayout>
#include <QGridLayout>
#include <QLabel>
#include <QPushButton>

DiagramaVenn::DiagramaVenn(MainWindow *parent) : QWidget(parent), mainWindow(parent)
{
    QVBoxLayout *layout = new QVBoxLayout(this);
    
    QLabel *titulo = new QLabel("Diagrama de Venn (3 Conjuntos)", this);
    titulo->setStyleSheet("font-size: 20px; font-weight: bold;");
    
    QLabel *instrucciones = new QLabel("Selecciona cuál variable es la incógnita. Esa será despejada matemáticamente.", this);
    
    QGridLayout *grid = new QGridLayout();
    grupoIncognita = new QButtonGroup(this);
    
    // Función lambda para crear filas repetitivas
    auto crearFila = [&](int fila, int id, const QString& texto, QSpinBox*& spin) {
        QRadioButton *radio = new QRadioButton(texto, this);
        grupoIncognita->addButton(radio, id);
        
        spin = new QSpinBox(this);
        spin->setRange(0, 1000000);
        
        grid->addWidget(radio, fila, 0);
        grid->addWidget(spin, fila, 1);
    };
    
    crearFila(0, 0, "Universo (U)", spinU);
    crearFila(1, 1, "Conjunto A", spinA);
    crearFila(2, 2, "Conjunto B", spinB);
    crearFila(3, 3, "Conjunto C", spinC);
    crearFila(4, 4, "Intersección A ∩ B", spinAnB);
    crearFila(5, 5, "Intersección A ∩ C", spinAnC);
    crearFila(6, 6, "Intersección B ∩ C", spinBnC);
    crearFila(7, 7, "Intersección A ∩ B ∩ C", spinAnBnC);
    crearFila(8, 8, "Complemento (Fuera de A, B y C)", spinComp);
    
    connect(grupoIncognita, &QButtonGroup::idClicked, this, &DiagramaVenn::onIncognitaCambiada);
    
    QPushButton *btnCalcular = new QPushButton("Despejar Incógnita", this);
    QPushButton *btnVolver = new QPushButton("Volver al Menú", this);
    
    layout->addWidget(titulo);
    layout->addWidget(instrucciones);
    layout->addLayout(grid);
    layout->addWidget(btnCalcular);
    layout->addWidget(btnVolver);
    
    connect(btnCalcular, &QPushButton::clicked, this, &DiagramaVenn::calcular);
    connect(btnVolver, &QPushButton::clicked, mainWindow, &MainWindow::mostrarMenuPrincipal);
    
    // Seleccionar Universo como incógnita por defecto
    grupoIncognita->button(0)->setChecked(true);
    onIncognitaCambiada(0);
}

void DiagramaVenn::onIncognitaCambiada(int id) {
    // Reactivar todos
    spinU->setEnabled(true);
    spinA->setEnabled(true);
    spinB->setEnabled(true);
    spinC->setEnabled(true);
    spinAnB->setEnabled(true);
    spinAnC->setEnabled(true);
    spinBnC->setEnabled(true);
    spinAnBnC->setEnabled(true);
    spinComp->setEnabled(true);
    
    // Desactivar el que es incógnita
    switch(id) {
        case 0: spinU->setEnabled(false); break;
        case 1: spinA->setEnabled(false); break;
        case 2: spinB->setEnabled(false); break;
        case 3: spinC->setEnabled(false); break;
        case 4: spinAnB->setEnabled(false); break;
        case 5: spinAnC->setEnabled(false); break;
        case 6: spinBnC->setEnabled(false); break;
        case 7: spinAnBnC->setEnabled(false); break;
        case 8: spinComp->setEnabled(false); break;
    }
}

void DiagramaVenn::calcular() {
    VennVariables v;
    int id = grupoIncognita->checkedId();
    
    v.U = (id == 0) ? -1 : spinU->value();
    v.A = (id == 1) ? -1 : spinA->value();
    v.B = (id == 2) ? -1 : spinB->value();
    v.C = (id == 3) ? -1 : spinC->value();
    v.AnB = (id == 4) ? -1 : spinAnB->value();
    v.AnC = (id == 5) ? -1 : spinAnC->value();
    v.BnC = (id == 6) ? -1 : spinBnC->value();
    v.AnBnC = (id == 7) ? -1 : spinAnBnC->value();
    v.Complemento = (id == 8) ? -1 : spinComp->value();
    
    QString pasos = LogicaMatematica::resolverVenn(v);
    
    // Actualizar la caja bloqueada con el resultado real
    if (id == 0) spinU->setValue(v.U);
    if (id == 1) spinA->setValue(v.A);
    if (id == 2) spinB->setValue(v.B);
    if (id == 3) spinC->setValue(v.C);
    if (id == 4) spinAnB->setValue(v.AnB);
    if (id == 5) spinAnC->setValue(v.AnC);
    if (id == 6) spinBnC->setValue(v.BnC);
    if (id == 7) spinAnBnC->setValue(v.AnBnC);
    if (id == 8) spinComp->setValue(v.Complemento);
    
    mainWindow->mostrarResultados("Resultados: Diagrama de Venn", pasos);
}
