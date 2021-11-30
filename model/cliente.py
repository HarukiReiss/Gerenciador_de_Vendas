class Cliente():
    def __init__(self, id, nome, endereco, tel):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.tel = tel 

    def print(self):
        print(self.id, self.nome, self.endereco, self.tel)


