# -*- coding:utf-8 -*-
def testaValor(arg):
    if arg <= 0:
        return 'N'
    else:
        return 'P'
    
if __name__ == '__main__':
    print '\nTeste com número 3: %s' % testaValor(3)
    print 'Teste com número 100: %s' % testaValor(100)
    print 'Teste com número -3: %s' % testaValor(-3)
    print 'Teste com número -100: %s' % testaValor(-100)
    print 'Teste com número 0: %s\n' % testaValor(0)