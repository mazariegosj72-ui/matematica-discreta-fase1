#ifndef DIAGRAMAVENN_H
#define DIAGRAMAVENN_H

#include <QWidget>
#include <QSpinBox>
#include <QRadioButton>
#include <QButtonGroup>

class MainWindow;

class DiagramaVenn : public QWidget
{
    Q_OBJECT
public:
    explicit DiagramaVenn(MainWindow *parent = nullptr);

private slots:
    void onIncognitaCambiada(int id);
    void calcular();

private:
    MainWindow *mainWindow;
    
    QButtonGroup *grupoIncognita;
    
    QSpinBox *spinU;
    QSpinBox *spinA;
    QSpinBox *spinB;
    QSpinBox *spinC;
    QSpinBox *spinAnB;
    QSpinBox *spinAnC;
    QSpinBox *spinBnC;
    QSpinBox *spinAnBnC;
    QSpinBox *spinComp;
};

#endif // DIAGRAMAVENN_H
