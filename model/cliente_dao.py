lista_clientes = []

def add(novo_cliente):
    lista_clientes.append(novo_cliente)


def getCliente(id):
    for cliente in lista_clientes:
        if cliente.id == id:
            return cliente
    return None


def edit(cliente):
    for index in range(0, len(lista_clientes)):
        cliente_atual = lista_clientes[index]
        if cliente.id == cliente_atual.id:
            lista_clientes[index] = cliente


def delete(id_cliente):
    for index in range(0, len(lista_clientes)):
        cliente_atual = lista_clientes[index]
        if id_cliente == cliente_atual.id:
            del lista_clientes[index]

            return


def listAll():
    for c in lista_clientes:
        c.exibir()


def view():
    pass

