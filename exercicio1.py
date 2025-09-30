class Transporte:
    def __init__(self, capacidade, velocidade):

        self.__capacidade = capacidade
        self.__velocidade_maxima = velocidade

    def 
    
    def getCapacidade(self):
        return self.__capacidade
    
    def getVelocidade(self):
        return self.__velocidade_maxima
    
    def descricao(self):
        print()

class Onibus(Transporte):
    def __init__(self, capacidade, velocidade):
        super().__init__(capacidade, velocidade)

    def mover(self):
        print('O ônibus está seguindo sua rota') 


class Bicicleta(Transporte):
    def __init__(self, capacidade, velocidade):
        super().__init__(capacidade, velocidade)

    def mover(self):
        print('A bicicleta está sendo pedalada')

bicicleta1 = Bicicleta(1, 30)
onibus1 = Onibus(80, 80)

bicicleta1.mover()
onibus1.mover()