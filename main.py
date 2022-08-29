import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStyleFactory
from ui.main_dialog import MainDialogUi


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = MainDialogUi()
        self.ui.setup_ui(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 风格样式
    QApplication.setStyle(QStyleFactory.create("fusion"))

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
