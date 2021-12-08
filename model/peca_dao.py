lista_pecas = []

def add(nova_peca):
    lista_pecas.append(nova_peca)


def getPeca(id):
    for peca in lista_pecas:
        if peca.id == id:
            return peca
    return None


def edit(peca):
    for index in range(0, len(lista_pecas)):
        peca_atual = lista_pecas[index]
        if peca.id == peca_atual.id:
            lista_pecas[index] = peca


def delete(id_peca):
    for index in range(0, len(lista_pecas)):
        peca_atual = lista_pecas[index]
        if id_peca == peca_atual.id:
            del lista_pecas[index]

            return


def listAll():
    for c in lista_pecas:
        c.exibir()


def view():
    pass




