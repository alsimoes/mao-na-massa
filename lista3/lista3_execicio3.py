# -*- coding:utf-8 -*-

def desenhaRetangulo(z=1,y=1):
    """
    Esta função desenha um retângulo com '+', '-' e '|'.
    Aceita apenas valores naturais entre 1 e 20.
    desenhaRetangulo(arg,arg) -> retângulo
    """
    if z > 20:
        z = 20
    if y > 20:
        y = 20
    if z < 1:
        z = 1
    if y < 1:
        y = 1
    
    print '\n Desenhando %d (max. 20) X %d (max. 20):' % (z,y)
        
    print '\n   +' + z * '-' + '+'
    for i in range(y):
        print '   |' + (z * ' ') + '|'
    print '   +' + z * '-' + '+\n'

if __name__ == '__main__':
    #testes
    desenhaRetangulo(10,40)
    desenhaRetangulo(40,10)
    desenhaRetangulo(40,-10)
    desenhaRetangulo(-40,10)