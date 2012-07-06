# -*- coding:utf-8 -*-

numeros = range(20)
par = []
impar = []

for i in numeros:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print '\nNúmeros -> ' + str(numeros) + '\n\nPar -----> ' + str(par) + '\n\nImpar ---> ' + str(impar) + '\n'