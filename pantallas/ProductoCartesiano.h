#ifndef PRODUCTOCARTESIANO_H
#define PRODUCTOCARTESIANO_H

#include <QWidget>
#include <QSpinBox>
#include <QVector>
#include <QLineEdit>
#include <QVBoxLayout>

class MainWindow;

class ProductoCartesiano : public QWidget
{
    Q_OBJECT
public:
    explicit ProductoCartesiano(MainWindow *parent = nullptr);

private slots:
    void actualizarConjuntos(int cantidad);
    void agregarElemento(int conjuntoIndex);
    void calcular();

private:
    void limpiarConjuntos();

    MainWindow *mainWindow;
    QSpinBox *spinCantidadConjuntos;
    QVBoxLayout *layoutConjuntos;
    
    // Almacena los inputs de cada conjunto
    QVector<QVector<QLineEdit*>> m_inputs;
    QVector<QVBoxLayout*> m_layoutsConjuntos;
};

#endif // PRODUCTOCARTESIANO_H
