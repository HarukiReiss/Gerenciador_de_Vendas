from model.cliente import Cliente
import model.cliente_dao as fun_cliente
from model.peca import Peca
import model.peca_dao as fun_peca


for i in range(0, 15):
    novo_cliente = Cliente(i, f'Aranha - {i}', 'Cidade Meteoro', 'XXX')
    fun_cliente.add(novo_cliente)

fun_cliente.delete(13)
fun_cliente.delete(15)
fun_cliente.delete(14)

id_cliente = 2
cliente_edit = fun_cliente.getCliente(id_cliente)
cliente_edit.nome = 'Feitan Portor'
cliente_edit.endereco = 'Cidade Meteoro'
cliente_edit.tel = '666'
fun_cliente.edit(cliente_edit)

fun_cliente.listAll()




