# -*- coding:utf-8 -*-

alunos = []

alunos.append({'nome':'André','idade':13,'altura':1.9})
alunos.append({'nome':'Erica','idade':14,'altura':1.6})
alunos.append({'nome':'Idenir','idade':12,'altura':1.7})
alunos.append({'nome':'Ana Paula','idade':11,'altura':1.8})
alunos.append({'nome':'Alex','idade':15,'altura':1.7})
alunos.append({'nome':'João','idade':13,'altura':1.9})
alunos.append({'nome':'Maria','idade':14,'altura':1.6})
alunos.append({'nome':'Fernanda','idade':12,'altura':1.7})
alunos.append({'nome':'Camila','idade':11,'altura':1.8})
alunos.append({'nome':'Angela','idade':15,'altura':1.7})
alunos.append({'nome':'Claudio','idade':13,'altura':1.9})
alunos.append({'nome':'Marcos','idade':14,'altura':1.6})
alunos.append({'nome':'Paulo','idade':12,'altura':1.7})
alunos.append({'nome':'José','idade':11,'altura':1.8})
alunos.append({'nome':'Francisco','idade':15,'altura':1.7})
alunos.append({'nome':'Careta','idade':13,'altura':1.9})
alunos.append({'nome':'Joana','idade':14,'altura':1.6})
alunos.append({'nome':'Jussara','idade':12,'altura':1.7})
alunos.append({'nome':'Danilo','idade':11,'altura':1.8})
alunos.append({'nome':'Samantha','idade':15,'altura':1.7})
alunos.append({'nome':'Yolanda','idade':13,'altura':1.9})
alunos.append({'nome':'Janete','idade':14,'altura':1.6})
alunos.append({'nome':'Sergio','idade':12,'altura':1.7})
alunos.append({'nome':'Marta','idade':11,'altura':1.8})
alunos.append({'nome':'Neiva','idade':15,'altura':1.7})
alunos.append({'nome':'Marieta','idade':13,'altura':1.9})
alunos.append({'nome':'Carlito','idade':14,'altura':1.6})
alunos.append({'nome':'Geni','idade':12,'altura':1.7})
alunos.append({'nome':'Eliezer','idade':11,'altura':1.8})
alunos.append({'nome':'Reginaldo','idade':15,'altura':1.7})

t_altura = 0

for i in alunos:
    t_altura = t_altura + i['altura']

m_altura = t_altura / 30

t_alunos = 0

for i in alunos:
    if i['altura'] < m_altura:
        t_alunos = t_alunos + 1

print '\nDos 30 alunos, %d medem menos que %1.2fm (média da classe).\n' % (t_alunos,m_altura)