# -*- coding:utf-8 -*-

import sys
inv = []
status = 1

while status != 0:
    mouseid = int(raw_input('\nInforme a identificação do mouse: '))
    if mouseid == 0:
        status = 0
        break
    print '(1) Necessita da esfera\n(2) Necessita de limpeza\n(3) Necessita de troca do cabo ou conector\n(4) Quebrado ou inutilizado'
    estado = int(raw_input('\nQual estado do mouse %d: ' % mouseid))
    inv.append({'mouseid':mouseid,'estado':estado})
    print

esfera = 0.0
limpeza = 0.0
troca = 0.0
quebrado = 0.0

total = len(inv)

if total == 0:
    print '\nNenhum mouse foi inventariado.\n'
    sys.exit()

for i in inv:
    if i['estado'] == 1:
        esfera = esfera + 1
    elif i['estado'] == 2:
        limpeza = limpeza + 1
    elif i['estado'] == 3:
        troca = troca + 1
    elif i['estado'] == 4:
        quebrado = quebrado + 1

print '\nQuantidade de mouses: %d\n' % total
print 'Situação                                   Quantidade   Perncentual'
print '1 - Necessita da esfera                             %d           %2.0f%%' % (esfera,(esfera/total) * 100)
print '2 - Necessita de limpeza                            %d           %2.0f%%' % (limpeza,(limpeza/total) * 100)
print '3 - Necessita de troca do cabo ou conector          %d           %2.0f%%' % (troca,(troca/total) * 100)
print '4 - Quebrado ou inutilizado                         %d           %2.0f%%\n' % (quebrado,(quebrado/total) * 100)