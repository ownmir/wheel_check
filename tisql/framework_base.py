import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QTextEdit, QAction, QHBoxLayout, QFrame, QSplitter
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

    
class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.init_ui()
        

    def init_ui(self):
        # textEdit = QTextEdit()
        
        central_widget = QWidget(self)                  # Создаём центральный виджет
        self.setCentralWidget(central_widget)
        hbox = QHBoxLayout(central_widget)
        top = QFrame(central_widget)
        top.setFrameShape(QFrame.StyledPanel)

        bottom_left = QFrame(central_widget)
        bottom_left.setFrameShape(QFrame.StyledPanel)
        bottom_right = QFrame(central_widget)
        bottom_right.setFrameShape(QFrame.StyledPanel)

        splitter_horizontal = QSplitter(Qt.Horizontal)
        splitter_horizontal.addWidget(top)
        
        splitter_vertical = QSplitter(Qt.Vertical)

        splitter_horizontal.addWidget(splitter_vertical)
        splitter_vertical.addWidget(bottom_left)
        splitter_vertical.addWidget(bottom_right)
        

        hbox.addWidget(splitter_vertical)
        central_widget.setLayout(hbox)

        
        # QAction является абстракцией для действий, совершенных из меню, панели инструментов, или комбинаций клавиш. 
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)  # В этих трех строках, мы создаем действие с соответствующей иконкой.
        exitAction.setShortcut('Ctrl+Q')  # Кроме того, для этого действия определяется комбинация клавиш.
        exitAction.setStatusTip('Exit application')  # создает подсказку, которая показывается в строке состояния, когда вы наведёте указатель мыши на пункт меню.
        # Когда мы выбираем именно это действие, срабатывает сигнал.
        exitAction.triggered.connect(self.close)  # Сигнал подключен к методу close(). Это завершает приложение.

        # Чтобы получить строку состояния, мы вызываем метод statusBar() класса QtGui.QMainWindow.
        # Первый вызов метода создает строку состояния.
        # Последующие вызовы возвращают объект статусбара.
        # showMessage() отображает сообщение в строке состояния.
        self.statusBar().showMessage('Ready')

        menubar = self.menuBar()  # Метод menuBar() создает строку меню.
        fileMenu = menubar.addMenu('&File')  # Мы создаем меню файла
        fileMenu.addAction(exitAction)  # и добавляем к нему действие выхода.

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        self.setGeometry(300, 100, 650, 550)
        self.setWindowTitle('Like silq')
##        self.setWindowIcon(QIcon('cfg.ico'))
        self.show()

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
