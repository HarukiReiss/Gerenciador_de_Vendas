from qt_core import *
from controller.cad_produto import CadProdutoWindow
import model.peca_dao as fun_peca

FILE_UI = 'view/produto.ui'

class PecaPage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        self.peca_window = None

        self.carrega_dados()

        self.novo_btn.clicked.connect(self.nova_peca)

        self.tabela.verticalHeader().setVisible(False)
        self.tabela.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tabela.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.tabela.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)


    def nova_peca(self):
        self.peca_window = CadProdutoWindow(self)
        self.peca_window.show()
        
    def carrega_dados(self):
        lista_pecas = fun_peca.lista_pecas
        self.tabela.setRowCount(0)
        for peca in lista_pecas:
            self.add_linha(peca)
    
    def add_linha(self, peca):
        rowCount = self.tabela.rowCount()
        self.tabela.insertRow(rowCount)

        id = QTableWidgetItem(str(peca.id))
        nome = QTableWidgetItem(peca.nome)
        valor = QTableWidgetItem(peca.valor)
        validade = QTableWidgetItem(peca.validade)

        self.tabela.setItem(rowCount, 0, id)
        self.tabela.setItem(rowCount, 1, nome)
        self.tabela.setItem(rowCount, 2, valor)
        self.tabela.setItem(rowCount, 3, validade)


