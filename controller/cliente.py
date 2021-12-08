from qt_core import *
from controller.cad_cliente import CadClienteWindow
import model.cliente_dao as fun_cliente

FILE_UI = 'view/cliente.ui'

class ClientePage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        self.cliente_window = None

        self.carrega_dados()

        self.novo_btn.clicked.connect(self.novo_cliente)

        self.tabela.verticalHeader().setVisible(False)
        self.tabela.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tabela.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.tabela.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)


    def novo_cliente(self):
        self.cliente_window = CadClienteWindow(self)
        self.cliente_window.show()
    
    def carrega_dados(self):
        lista_clientes = fun_cliente.lista_clientes
        self.tabela.setRowCount(0)
        for cliente in lista_clientes:
            self.add_linha(cliente)
    
    def add_linha(self, cliente):
        rowCount = self.tabela.rowCount()
        self.tabela.insertRow(rowCount)

        id = QTableWidgetItem(str(cliente.id))
        nome = QTableWidgetItem(cliente.nome)
        endereco = QTableWidgetItem(cliente.endereco)
        tel = QTableWidgetItem(cliente.tel)

        self.tabela.setItem(rowCount, 0, id)
        self.tabela.setItem(rowCount, 1, nome)
        self.tabela.setItem(rowCount, 2, endereco)
        self.tabela.setItem(rowCount, 3, tel)




