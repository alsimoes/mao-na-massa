# -*- coding:utf-8 -*-
import sys
print '\nGERADOR DE TABUADA\n'
multi = int(raw_input('Escolha um número inteiro entre 1 e 10: '))

if multi == 0 or multi > 10:
    print '\nEscolha um número entre 1 e 10.\n'
    sys.exit()

print

for i in range(1,11):
    result = multi * i
    print '    %d X %d = %d' % (multi,i,result)
print '\nfdp\n'