#include "ProductoCartesiano.h"
#include "../mainwindow.h"
#include "../matematica/LogicaMatematica.h"
#include <QHBoxLayout>
#include <QLabel>
#include <QPushButton>
#include <QScrollArea>
#include <QGroupBox>

ProductoCartesiano::ProductoCartesiano(MainWindow *parent) : QWidget(parent), mainWindow(parent)
{
    QVBoxLayout *mainLayout = new QVBoxLayout(this);
    
    QLabel *titulo = new QLabel("Producto Cartesiano", this);
    titulo->setStyleSheet("font-size: 20px; font-weight: bold;");
    
    QHBoxLayout *hTop = new QHBoxLayout();
    hTop->addWidget(new QLabel("Cantidad de Conjuntos:"));
    spinCantidadConjuntos = new QSpinBox(this);
    spinCantidadConjuntos->setRange(2, 10);
    spinCantidadConjuntos->setValue(3);
    hTop->addWidget(spinCantidadConjuntos);
    
    QScrollArea *scroll = new QScrollArea(this);
    scroll->setWidgetResizable(true);
    QWidget *scrollContent = new QWidget(scroll);
    layoutConjuntos = new QVBoxLayout(scrollContent);
    scroll->setWidget(scrollContent);
    
    QPushButton *btnCalcular = new QPushButton("Calcular Producto Cartesiano", this);
    QPushButton *btnVolver = new QPushButton("Volver al Menú", this);
    
    mainLayout->addWidget(titulo);
    mainLayout->addLayout(hTop);
    mainLayout->addWidget(scroll);
    mainLayout->addWidget(btnCalcular);
    mainLayout->addWidget(btnVolver);
    
    connect(spinCantidadConjuntos, QOverload<int>::of(&QSpinBox::valueChanged), this, &ProductoCartesiano::actualizarConjuntos);
    connect(btnCalcular, &QPushButton::clicked, this, &ProductoCartesiano::calcular);
    connect(btnVolver, &QPushButton::clicked, mainWindow, &MainWindow::mostrarMenuPrincipal);
    
    actualizarConjuntos(3); // Inicializar con 3
}

void ProductoCartesiano::limpiarConjuntos() {
    QLayoutItem *child;
    while ((child = layoutConjuntos->takeAt(0)) != nullptr) {
        if (child->widget()) {
            delete child->widget();
        }
        delete child;
    }
    m_inputs.clear();
    m_layoutsConjuntos.clear();
}

void ProductoCartesiano::actualizarConjuntos(int cantidad) {
    limpiarConjuntos();
    
    m_inputs.resize(cantidad);
    m_layoutsConjuntos.resize(cantidad);
    
    for (int i = 0; i < cantidad; ++i) {
        QGroupBox *grupo = new QGroupBox(QString("Conjunto %1").arg(QChar('A' + i)), this);
        QVBoxLayout *vbox = new QVBoxLayout(grupo);
        
        QPushButton *btnAgregar = new QPushButton("Agregar Elemento", grupo);
        connect(btnAgregar, &QPushButton::clicked, this, [this, i]() {
            agregarElemento(i);
        });
        
        vbox->addWidget(btnAgregar);
        
        m_layoutsConjuntos[i] = vbox;
        layoutConjuntos->addWidget(grupo);
        
        // Agregamos un elemento vacío por defecto
        agregarElemento(i);
    }
    layoutConjuntos->addStretch();
}

void ProductoCartesiano::agregarElemento(int conjuntoIndex) {
    QLineEdit *input = new QLineEdit(this);
    input->setPlaceholderText(QString("Elemento %1").arg(m_inputs[conjuntoIndex].size() + 1));
    
    m_layoutsConjuntos[conjuntoIndex]->insertWidget(m_layoutsConjuntos[conjuntoIndex]->count() - 1, input); // Antes del botón
    m_inputs[conjuntoIndex].append(input);
}

void ProductoCartesiano::calcular() {
    QVector<QVector<QString>> conjuntos;
    
    for (int i = 0; i < m_inputs.size(); ++i) {
        QVector<QString> conjunto;
        for (QLineEdit *input : m_inputs[i]) {
            QString texto = input->text().trimmed();
            if (!texto.isEmpty()) {
                conjunto.append(texto);
            }
        }
        conjuntos.append(conjunto);
    }
    
    QVector<QString> resultado = LogicaMatematica::productoCartesiano(conjuntos);
    
    QString textoFinal = "El Producto Cartesiano es:\n\n{ ";
    textoFinal += resultado.join(", ");
    textoFinal += " }\n\n";
    textoFinal += QString("Total de pares ordenados: %1").arg(resultado.size());
    
    mainWindow->mostrarResultados("Producto Cartesiano", textoFinal);
}
