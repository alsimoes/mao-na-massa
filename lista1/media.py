# -*- coding:utf-8 -*-

notas = []
soma = 0.0

notas.append(float(raw_input('\nDigite a nota do primeiro bimestre: ')))
notas.append(float(raw_input('\nDigite a nota do segundo bimestre: ')))
notas.append(float(raw_input('\nDigite a nota do terceiro bimestre: ')))
notas.append(float(raw_input('\nDigite a nota do quarto bimestre: ')))

for i in notas:
    soma = soma + i

media = soma / len(notas)

print '\nA média final é: %2.1f\n\n' % media
