class Peca():
    def __init__(self, id, nome, valor, validade):
        self.id = id
        self.nome = nome
        self.valor = valor 
        self.validade = validade

    def exibir(self):
        print(f'ID: {self.id} - Nome: {self.nome} - Valor: R${self.valor} - Validade: {self.validade}')



