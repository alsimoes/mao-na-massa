# -*- coding:utf-8 -*-

valor_hora = float(raw_input('\nQuanto custa sua hora de tabalho? '))
qtde_horas = float(raw_input('\nQuantas horas você trabalhou este mês? '))
salario = valor_hora * qtde_horas
print '\nVocê irá receber R$ %5.2f.\n' % salario