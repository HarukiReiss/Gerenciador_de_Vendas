from qt_core import *

FILE_UI = 'view/produto.ui'

class PecaPage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUI(FILE_UI, self)