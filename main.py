from model.cliente import Cliente
import model.cliente_dao as fun_cliente
from model.peca import Peca
import model.peca_dao as fun_peca

for i in range(0, 15):
    novo_cliente = Cliente(i, f'Cliente - {i}', 'Meteoro', '75 9883298493')
    fun_cliente.add(novo_cliente)

fun_cliente.listAll()

print("\n_________\n")

for p in range(0, 15):
    nova_peca = Peca(p, f'Peça - {p}', p+5, '20/02/2022')
    fun_peca.add(nova_peca)

fun_peca.listAll()


