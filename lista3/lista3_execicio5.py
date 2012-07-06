# -*- coding:utf-8 -*-
"""
Este módulo contem a função imprime uma piramide com
números até a n-ésima linha.
"""
def piramide(num=0):
    x = ''
    for i in range(1,num+1):
        x = x + str(i) + ' '
        print x

if __name__ == '__main__':
    piramide(15)