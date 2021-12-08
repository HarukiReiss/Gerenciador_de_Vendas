from model.cliente import Cliente
from qt_core import*
import model.cliente_dao as fun_cliente

FILE_UI = 'view/cad_cliente.ui'

class CadClienteWindow(QWidget):
    def __init__(self, janela_cliente):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        self.janela_cliente = janela_cliente

        self.cancelar_btn.clicked.connect(self.fechar_janela)
        self.salvar_btn.clicked.connect(self.salvar)
    
    def fechar_janela(self):
        self.close()
    
    def salvar(self):
        nome = self.nome.text()
        endereco = self.endereco.text()
        tel = self.tel.text()
        novo_cliente = Cliente(None, nome, endereco, tel)
        fun_cliente.add(novo_cliente)

        self.janela_cliente.carrega_dados()

        self.close()

