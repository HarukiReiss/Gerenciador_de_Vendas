class Cliente():
    def __init__(self, id, nome, endereco, tel):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.tel = tel 

    def exibir(self):
        print(f'ID: {self.id} - Nome: {self.nome} - Endereço: {self.endereco} - Telefone: {self.tel}')


