# -*- coding:utf-8 -*-
class carro:
    def __init__(self,consumo):
        self.__consumo = consumo
        self.__combustivel = 0.0
        self.__quilometragem = 0.0
    
    def andar(self,quilometros):
        necessario = quilometros / self.__consumo
        if necessario <= self.obterGasolina():
            self.__combustivel = self.obterGasolina() - necessario
            self.__quilometragem = self.obterQuilometragem() + quilometros
            return quilometros
        else:
            possivel = self.obterGasolina() * self.__consumo
            return self.andar(possivel)
    
    def obterQuilometragem(self):
        return self.__quilometragem
    
    def obterGasolina(self):
        return self.__combustivel
    
    def adicionarGasolina(self,litros):
        self.__combustivel = self.obterGasolina() + litros
        
if __name__ == '__main__':
    p = 's'
    modelo = raw_input('\n    Qual é o seu carro? ')
    meuCarro = carro(int(raw_input('\n    Quantos litros ele faz por quilômetro? ')))
    #meuCarro.adicionarGasolina(int(raw_input('\nQuantos litros deseja abastecer? ')))
    while p == 's':
        if raw_input('\n    Deseja parar para abastecer o carro (S/N)? ').lower() == 's':
            meuCarro.adicionarGasolina(int(raw_input('\n    Quantos litros deseja abastecer? ')))
        andar = int(raw_input('\n    Quantos quilometros deseja andar? '))
        andei = meuCarro.andar(andar)
        if andei == 0:
            print '\n    Você não tem gasolina para andar!!!\n'
        else:
            if andar == andei:
                print '\n    Andei %d quiômetros.' % andar
            else:
                print '\n    Tentei andar %d quiômetros, mas só consegui %d!!!' % (andar,andei)
        if meuCarro.obterGasolina() == 0:
            print '\n    Meu %s ficou com sem gasolina, mas já rodei %d quilômetros.\n' % (modelo,meuCarro.obterQuilometragem())
        else:
            print '\n    Meu %s ficou com %3.1f litros no tanque e já rodei %d quilômetros.\n' % (modelo,meuCarro.obterGasolina(),meuCarro.obterQuilometragem())
        p = raw_input('    Deseja continuar o passeio (S/N)? ').lower()
    print '\n    Até o próximo passeio. Um abraço!!!\n'