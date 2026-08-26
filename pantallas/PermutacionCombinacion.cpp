#include "PermutacionCombinacion.h"
#include "../mainwindow.h"
#include "../matematica/LogicaMatematica.h"
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QLabel>
#include <QPushButton>
#include <QMessageBox>

PermutacionCombinacion::PermutacionCombinacion(MainWindow *parent) : QWidget(parent), mainWindow(parent)
{
    QVBoxLayout *layout = new QVBoxLayout(this);
    
    QLabel *titulo = new QLabel("Permutaciones y Combinaciones", this);
    titulo->setStyleSheet("font-size: 20px; font-weight: bold;");
    
    radioPermutacion = new QRadioButton("Permutación P(n, r)", this);
    radioCombinacion = new QRadioButton("Combinación C(n, r)", this);
    radioPermutacion->setChecked(true);
    
    QHBoxLayout *hN = new QHBoxLayout();
    hN->addWidget(new QLabel("Valor de n (Total de elementos):"));
    spinN = new QSpinBox(this);
    spinN->setRange(0, 100);
    hN->addWidget(spinN);
    
    QHBoxLayout *hR = new QHBoxLayout();
    hR->addWidget(new QLabel("Valor de r (Elementos seleccionados):"));
    spinR = new QSpinBox(this);
    spinR->setRange(0, 100);
    hR->addWidget(spinR);
    
    QPushButton *btnCalcular = new QPushButton("Calcular", this);
    QPushButton *btnVolver = new QPushButton("Volver al Menú", this);
    
    layout->addWidget(titulo);
    layout->addWidget(radioPermutacion);
    layout->addWidget(radioCombinacion);
    layout->addLayout(hN);
    layout->addLayout(hR);
    layout->addWidget(btnCalcular);
    layout->addWidget(btnVolver);
    layout->addStretch();
    
    connect(btnCalcular, &QPushButton::clicked, this, &PermutacionCombinacion::calcular);
    connect(btnVolver, &QPushButton::clicked, mainWindow, &MainWindow::mostrarMenuPrincipal);
}

void PermutacionCombinacion::calcular() {
    int n = spinN->value();
    int r = spinR->value();
    
    if (n < r) {
        QMessageBox::warning(this, "Error", "El valor de 'n' debe ser mayor o igual a 'r'.");
        return;
    }
    
    unsigned long long resultado = 0;
    QString operacion;
    
    if (radioPermutacion->isChecked()) {
        resultado = LogicaMatematica::permutacion(n, r);
        operacion = QString("Permutación P(%1, %2)").arg(n).arg(r);
    } else {
        resultado = LogicaMatematica::combinacion(n, r);
        operacion = QString("Combinación C(%1, %2)").arg(n).arg(r);
    }
    
    QString texto = QString("El resultado de la %1 es:\n\n%2").arg(operacion).arg(resultado);
    mainWindow->mostrarResultados(operacion, texto);
}
