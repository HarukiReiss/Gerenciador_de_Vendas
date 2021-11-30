class Peca():
    def __init__(self, cod, nome, valor, validade):
        self.cod = cod
        self.nome = nome
        self.valor = valor 
        self.validade = validade

    def print(self):
        print(self.cod, self.nome, self.valor, self.validade)



