# -*- coding:utf-8 -*-
"""
Este módulo contem a função que inverte números inteiros.
"""

def inverte(numero=0):
    """
    Esta função recebe um número inteiro e o inverte.
    Exemplo: inverte(123) -> 321
    """
    x = 0
    while numero > 0:
        x = x * 10
        x = x + (numero % 10)
        numero = numero / 10
    return x

if __name__ == '__main__':
    print '\nO inverso de 123 é %d.\n' % (inverte(123))
    print '\nO inverso de 1234 é %d.\n' % (inverte(1234))
    print '\nO inverso de 9346 é %d.\n' % (inverte(9346))