#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QStackedWidget>

class MainMenu;
class PermutacionCombinacion;
class ProductoCartesiano;
class DiagramaVenn;
class Resultados;

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

public slots:
    void mostrarMenuPrincipal();
    void mostrarPermutaciones();
    void mostrarCartesiano();
    void mostrarVenn();
    void mostrarResultados(const QString& titulo, const QString& contenido);

private:
    QStackedWidget *stackedWidget;
    
    MainMenu *pantallaMenu;
    PermutacionCombinacion *pantallaPerm;
    ProductoCartesiano *pantallaCart;
    DiagramaVenn *pantallaVenn;
    Resultados *pantallaRes;
};

#endif // MAINWINDOW_H
