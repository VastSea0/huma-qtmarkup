from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Ana pencere ayarları
        self.setWindowTitle("PyQt WebEngine Example")
        self.setGeometry(100, 100, 800, 800)  # x, y, width, height

        # WebView oluşturma
        webview = QWebEngineView()
        webview.setGeometry(150, 150, 500, 500)  # x, y, width, height
        webview.setUrl('https://www.example.com')  # Web sayfası yükleme
        layout.addWidget(webview)

        # Ana widget oluşturma ve düzenleme
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(webview)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
