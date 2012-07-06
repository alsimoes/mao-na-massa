# -*- coding:utf-8 -*-
import getpass
auth = 0
while auth != 1:
    user = raw_input('\nLogin: ')
    pwd = raw_input('Senha: ')
    if pwd.lower() == user.lower():
        print '\nSenha inválida, senhas não podem ser iguais.'
    else:
        auth = 1
print '\nUsuário autenticado com sucesso.'