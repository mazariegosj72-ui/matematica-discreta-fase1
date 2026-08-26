#ifndef LOGICAMATEMATICA_H
#define LOGICAMATEMATICA_H

#include <QString>
#include <QVector>

struct VennVariables {
    long long U;
    long long A;
    long long B;
    long long C;
    long long AnB;
    long long AnC;
    long long BnC;
    long long AnBnC;
    long long Complemento;
};

class LogicaMatematica
{
public:
    static unsigned long long factorial(int n);
    static unsigned long long permutacion(int n, int r);
    static unsigned long long combinacion(int n, int r);

    static QVector<QString> productoCartesiano(const QVector<QVector<QString>>& conjuntos);
    
    // Despeja la variable que esté en -1 y devuelve el procedimiento en texto.
    static QString resolverVenn(VennVariables& v);

private:
    static void productoCartesianoRecursivo(const QVector<QVector<QString>>& conjuntos, int index, QString actual, QVector<QString>& resultado);
};

#endif // LOGICAMATEMATICA_H
