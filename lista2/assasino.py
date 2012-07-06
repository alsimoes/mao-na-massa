# -*- coding:utf-8 -*-
print '\nINTERROGATÓRIO ELETRÔNICO\n'
sai = 'n'
while sai == 'n':
    quest = []
    quest.append(raw_input('\nVocê telefonou para a vítima? (s/n) ').lower())
    quest.append(raw_input('Você esteve no local do crime? (s/n) ').lower())
    quest.append(raw_input('Você mora perto da vítima? (s/n) ').lower())
    quest.append(raw_input('Você devia para a vítima? (s/n) ').lower())
    quest.append(raw_input('Você já trabalhou com a vítima? (s/n) ').lower())
    resp = quest.count('s')
    if resp == 2:
        result = 'suspeito!'
    elif resp == 3 or resp == 4:
        result = 'cúmplice!!!'
    elif resp == 5:
        result = 'CULPADO!!!'
    else:
        result = 'inocente.'
    print '\nVocê é %s \n' % result
    sai = raw_input('Encerrar o interrogatório? (s/n) ').lower()
print '\nfdp\n'