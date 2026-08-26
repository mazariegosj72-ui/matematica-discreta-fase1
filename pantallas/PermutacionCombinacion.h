#ifndef PERMUTACIONCOMBINACION_H
#define PERMUTACIONCOMBINACION_H

#include <QWidget>
#include <QSpinBox>
#include <QRadioButton>

class MainWindow;

class PermutacionCombinacion : public QWidget
{
    Q_OBJECT
public:
    explicit PermutacionCombinacion(MainWindow *parent = nullptr);

private slots:
    void calcular();

private:
    MainWindow *mainWindow;
    QRadioButton *radioPermutacion;
    QRadioButton *radioCombinacion;
    QSpinBox *spinN;
    QSpinBox *spinR;
};

#endif // PERMUTACIONCOMBINACION_H
