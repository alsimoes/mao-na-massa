# -*- coding:utf-8 -*-
class conta_corrente:
    _contas_abertas = 0
    def __init__(self,numero,nome,deposito=0.0):
        self.numero = numero
        self.nome = nome
        self._saldo = deposito
        conta_corrente._contas_abertas = conta_corrente._contas_abertas + 1
    
    def saldo(self):
        return self._saldo
    
    def alterar_nome(self,nome):
        self.nome = nome
    
    def deposito(self,valor):
        if valor > 0:
            self._saldo = self.saldo() + valor
            return 'Saldo disponível: R$ %5.2f.' % self._saldo
        else:
            return 'Informe apenas valores positivos.'
    
    def saque(self,valor):
        if valor > 0:
            if valor <= self.saldo():
                self._saldo = self.saldo() - valor
                return 'Saldo disponível: R$ %5.2f.' % self.saldo()
            else:
                return 'Saldo insuficiente.'
        else:
            return 'Informe apenas valores positivos.'

class conta_especial(conta_corrente):
    def __init__(self,numero,nome,limite,deposito=0):
        conta_corrente.__init__(self,numero,nome,deposito)
        self.limite = limite
    
    def saque(self,valor):
        if valor > 0:
            if valor <= self.saldo_disponivel():
                self._saldo = self.saldo() - valor
                return 'Saldo: R$ %5.2f. Saldo disponivel: R$ %5.2f' % (self.saldo(),self.saldo_disponivel())
            else:
                return 'Saldo insuficiente.'
        else:
            return 'Informe apenas valores positivos.'
    
    def saldo_disponivel(self):
        return self.saldo() + self.limite