# -*- coding:utf-8 -*-

valor_hora = float(raw_input('\nQuanto custa sua hora de tabalho? '))
qtde_horas = float(raw_input('\nQuantas horas você trabalhou este mês? '))

bruto = valor_hora * qtde_horas
ir = bruto * 0.11
inss = bruto * 0.08
sindicato = bruto * 0.05
liquido = bruto - ( ir + inss + sindicato )

holerith = '\nSalário bruto: R$ %5.2f\n\
IR (11%%): R$ %5.2f\n\
INSS (8%%): R$ %5.2f\n\
Sindicato (5%%): R$ %5.2f\n\
Salário Líquido:R$ %5.2f\n\nObs: Falta fazer aparecer o simbolo do percebtual.'

print holerith % (bruto,ir,inss,sindicato,liquido)