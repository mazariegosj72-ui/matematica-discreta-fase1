#ifndef RESULTADOS_H
#define RESULTADOS_H

#include <QWidget>
#include <QTextEdit>
#include <QLabel>

class MainWindow;

class Resultados : public QWidget
{
    Q_OBJECT
public:
    explicit Resultados(MainWindow *parent = nullptr);
    void setResultados(const QString& titulo, const QString& contenido);

private:
    MainWindow *mainWindow;
    QLabel *lblTitulo;
    QTextEdit *txtContenido;
};

#endif // RESULTADOS_H
