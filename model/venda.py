class Venda():
    def __init__(self, id, cliente, data, itens):
        self.id = id
        self.cliente = cliente
        self.data = data
        self.itens = itens
    
    def valorTotal(self):
        vtotal = 0
        for peca in self.itens:
            vtotal += peca.valor
        return vtotal

