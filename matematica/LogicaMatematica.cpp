#include "LogicaMatematica.h"
#include <stdexcept>

unsigned long long LogicaMatematica::factorial(int n) {
    if (n < 0) return 0;
    unsigned long long fact = 1;
    for (int i = 2; i <= n; ++i) {
        fact *= i;
    }
    return fact;
}

unsigned long long LogicaMatematica::permutacion(int n, int r) {
    if (n < r || n < 0 || r < 0) return 0;
    unsigned long long perm = 1;
    for (int i = n; i > n - r; --i) {
        perm *= i;
    }
    return perm;
}

unsigned long long LogicaMatematica::combinacion(int n, int r) {
    if (n < r || n < 0 || r < 0) return 0;
    return permutacion(n, r) / factorial(r);
}

void LogicaMatematica::productoCartesianoRecursivo(const QVector<QVector<QString>>& conjuntos, int index, QString actual, QVector<QString>& resultado) {
    if (index == conjuntos.size()) {
        resultado.append("(" + actual + ")");
        return;
    }
    
    for (const QString& elemento : conjuntos[index]) {
        QString siguiente = actual;
        if (!siguiente.isEmpty()) {
            siguiente += ", ";
        }
        siguiente += elemento;
        productoCartesianoRecursivo(conjuntos, index + 1, siguiente, resultado);
    }
}

QVector<QString> LogicaMatematica::productoCartesiano(const QVector<QVector<QString>>& conjuntos) {
    QVector<QString> resultado;
    if (conjuntos.isEmpty()) return resultado;
    productoCartesianoRecursivo(conjuntos, 0, "", resultado);
    return resultado;
}

QString LogicaMatematica::resolverVenn(VennVariables& v) {
    QString pasos = "Fórmula de Inclusión-Exclusión:\n";
    pasos += "|A ∪ B ∪ C| = |A| + |B| + |C| - |A ∩ B| - |A ∩ C| - |B ∩ C| + |A ∩ B ∩ C|\n";
    pasos += "U = |A ∪ B ∪ C| + Complemento\n\n";

    // Reemplazamos |A U B U C| = U - Complemento
    // Entonces: U - Complemento = A + B + C - AnB - AnC - BnC + AnBnC
    
    if (v.U == -1) {
        pasos += "Incógnita: Universo (U)\n";
        v.U = v.A + v.B + v.C - v.AnB - v.AnC - v.BnC + v.AnBnC + v.Complemento;
        pasos += QString("U = %1 + %2 + %3 - %4 - %5 - %6 + %7 + %8\n")
            .arg(v.A).arg(v.B).arg(v.C).arg(v.AnB).arg(v.AnC).arg(v.BnC).arg(v.AnBnC).arg(v.Complemento);
        pasos += QString("U = %1").arg(v.U);
    } else if (v.Complemento == -1) {
        pasos += "Incógnita: Complemento\n";
        long long AUBUC = v.A + v.B + v.C - v.AnB - v.AnC - v.BnC + v.AnBnC;
        v.Complemento = v.U - AUBUC;
        pasos += QString("Complemento = U - (|A| + |B| + |C| - |A ∩ B| - |A ∩ C| - |B ∩ C| + |A ∩ B ∩ C|)\n");
        pasos += QString("Complemento = %1 - %2\n").arg(v.U).arg(AUBUC);
        pasos += QString("Complemento = %1").arg(v.Complemento);
    } else if (v.A == -1) {
        pasos += "Incógnita: Conjunto A\n";
        long long AUBUC = v.U - v.Complemento;
        v.A = AUBUC - v.B - v.C + v.AnB + v.AnC + v.BnC - v.AnBnC;
        pasos += QString("A = (U - Complemento) - |B| - |C| + |A ∩ B| + |A ∩ C| + |B ∩ C| - |A ∩ B ∩ C|\n");
        pasos += QString("A = %1").arg(v.A);
    } else if (v.B == -1) {
        pasos += "Incógnita: Conjunto B\n";
        long long AUBUC = v.U - v.Complemento;
        v.B = AUBUC - v.A - v.C + v.AnB + v.AnC + v.BnC - v.AnBnC;
        pasos += QString("B = %1").arg(v.B);
    } else if (v.C == -1) {
        pasos += "Incógnita: Conjunto C\n";
        long long AUBUC = v.U - v.Complemento;
        v.C = AUBUC - v.A - v.B + v.AnB + v.AnC + v.BnC - v.AnBnC;
        pasos += QString("C = %1").arg(v.C);
    } else if (v.AnB == -1) {
        pasos += "Incógnita: Intersección A ∩ B\n";
        long long AUBUC = v.U - v.Complemento;
        v.AnB = v.A + v.B + v.C - v.AnC - v.BnC + v.AnBnC - AUBUC;
        pasos += QString("A ∩ B = %1").arg(v.AnB);
    } else if (v.AnC == -1) {
        pasos += "Incógnita: Intersección A ∩ C\n";
        long long AUBUC = v.U - v.Complemento;
        v.AnC = v.A + v.B + v.C - v.AnB - v.BnC + v.AnBnC - AUBUC;
        pasos += QString("A ∩ C = %1").arg(v.AnC);
    } else if (v.BnC == -1) {
        pasos += "Incógnita: Intersección B ∩ C\n";
        long long AUBUC = v.U - v.Complemento;
        v.BnC = v.A + v.B + v.C - v.AnB - v.AnC + v.AnBnC - AUBUC;
        pasos += QString("B ∩ C = %1").arg(v.BnC);
    } else if (v.AnBnC == -1) {
        pasos += "Incógnita: Intersección A ∩ B ∩ C\n";
        long long AUBUC = v.U - v.Complemento;
        v.AnBnC = AUBUC - v.A - v.B - v.C + v.AnB + v.AnC + v.BnC;
        pasos += QString("A ∩ B ∩ C = %1").arg(v.AnBnC);
    }

    return pasos;
}
