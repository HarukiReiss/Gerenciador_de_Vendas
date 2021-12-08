from qt_core import *
from controller.cliente import ClientePage
from controller.inicio import InicioPage
from controller.pecas import PecaPage

FILE_UI = 'view/main_window.ui'

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        self.inicio_page = InicioPage()
        self.cliente_page = ClientePage()
        self.peca_page = PecaPage()

        self.painel_principal.insertWidget(0, self.inicio_page)
        self.painel_principal.insertWidget(1, self.cliente_page)
        self.painel_principal.insertWidget(2, self.peca_page)

        self.inicio_btn.clicked.connect(self.show_inicio)
        self.cliente_btn.clicked.connect(self.show_cliente)
        self.produto_btn.clicked.connect(self.show_pecas)

    def show_inicio(self):
        self.painel_principal.setCurrentIndex(0)

    def show_cliente(self):
        self.painel_principal.setCurrentIndex(1)

    def show_pecas(self):
        self.painel_principal.setCurrentIndex(2)




