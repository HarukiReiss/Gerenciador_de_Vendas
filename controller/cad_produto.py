from model.peca import Peca
from qt_core import*
import model.peca_dao as fun_peca

FILE_UI = 'view/cad_produto.ui'

class CadProdutoWindow(QWidget):
    def __init__(self, janela_peca):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        self.janela_peca = janela_peca

        self.cancelar_btn.clicked.connect(self.fechar_janela)
        self.salvar_btn.clicked.connect(self.salvar)
    
    def fechar_janela(self):
        self.close()
    
    def salvar(self):
        nome = self.nome.text()
        validade = self.validade.text()
        valor = self.valor.text()
        nova_peca = Peca(None, nome, valor, validade)
        fun_peca.add(nova_peca)

        self.janela_peca.carrega_dados()

        self.close()
