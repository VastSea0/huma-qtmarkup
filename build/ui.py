import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt, QUrl

from PyQt5.QtWebEngineWidgets import QWebEngineView

class HumaUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.setup_ui()

    def setup_ui(self):
        self.resize(500, 500)
        self.setWindowTitle("Pencere adı")
        label = QLabel("Welcome To World Wide Web")
        label.setFont(QFont("Arial", 12))
        label.setStyleSheet("color: red;")

      # Added Label
        label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(label)

      # Browser
        webview = QWebEngineView()
        webview.setGeometry(150, 150, 500, 500)
        webview.setUrl(QUrl('https://uzaylinin-notlari.netlify.app/'))
        self.layout.addWidget(webview)

def main():
    app = QApplication(sys.argv)
    ui = HumaUI()
    ui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
