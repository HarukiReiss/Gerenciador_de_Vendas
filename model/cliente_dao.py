
lista_clientes = []

def add(novo_cliente):
    lista_clientes.append(novo_cliente)

def edit():
    pass

def delete():
    pass

def listAll():
    for c in lista_clientes:
        c.exibir()
