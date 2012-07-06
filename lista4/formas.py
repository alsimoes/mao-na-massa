# -*- coding:utf-8 -*-

class bola:
    def __init__(self,cor='branca',circ=1.0,material='capotão'):
        self.cor = cor
        self.circ = float(circ)
        self.material = material
    
    def troca_cor(self,cor=''):
        self.cor = cor
    
    def mostra_cor(self):
        return self.cor

class quadrado:
    def __init__(self,lado):
        self._lado = lado
    
    def mudar_lado(self,lado):
        self._lado = lado
    
    def retorna_lado(self):
        return self._lado
    
    def calcula_area(self):
        return self._lado * self._lado