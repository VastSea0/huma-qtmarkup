import random
import json
from typing import List, Dict, Any
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt

class HumaHtmlEngine:
    def __init__(self, html_file: str):
        self.html_file = html_file
        self.tag_list: List[Dict[str, Any]] = []

    def parse_html(self) -> None:
        with open(self.html_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for line in lines:
            line = line.strip()
            if line.startswith("<huma:"):
                end_index = line.find(">")
                tag_content = line[6:end_index]
                content = line[end_index + 1 : line.rfind("<")]
                
                tag_parts = tag_content.split(':')
                tag_type = tag_parts[0]
                
                tag_info = {"type": tag_type, "content": content}
                
                if tag_type == "window":
                    tag_info["attribute"] = tag_parts[1]
                    
                elif len(tag_parts) > 1:
                    for i, part in enumerate(tag_parts[1:], 1):
                        if part.isdigit():
                            tag_info[f"param{i}"] = int(part)
                        else:
                            tag_info[f"param{i}"] = part
                
                self.tag_list.append(tag_info)

    def create_json_template(self) -> None:
        json_output = json.dumps(self.tag_list, indent=2)
        file_name = f"build/temp.yeniui{random.randint(0, 5000)}.json"
        with open("build/output.json", "w") as file:
            file.write(json_output)
        print(f"JSON dosyası oluşturuldu: {file_name}")

    def create_ui_file(self) -> None:
        with open("build/ui.py", "w") as file:
            file.write("import sys\n")
            file.write("from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget\n")
            file.write("from PyQt5.QtGui import QFont, QColor\n")
            file.write("from PyQt5.QtCore import Qt, QUrl\n\n")
            file.write("from PyQt5.QtWebEngineWidgets import QWebEngineView\n\n")
            file.write("class HumaUI(QMainWindow):\n")
            file.write("    def __init__(self):\n")
            file.write("        super().__init__()\n")
            file.write("        self.central_widget = QWidget()\n")
            file.write("        self.setCentralWidget(self.central_widget)\n")
            file.write("        self.layout = QVBoxLayout(self.central_widget)\n")
            file.write("        self.setup_ui()\n\n")
            file.write("    def setup_ui(self):\n")
            
            for tag in self.tag_list:
                if tag["type"] == "window":
                    if tag["attribute"] == "size":
                        width, height = map(int, tag["content"].split('x'))
                        file.write(f'        self.resize({width}, {height})\n')
                    elif tag["attribute"] == "title":
                        file.write(f'        self.setWindowTitle("{tag["content"]}")\n')

                elif tag["type"] == "webengine":
                    

                   
                         
                    if "param4" in tag:
                        show = tag["param4"]
                        if show == "show": 
                            protokol = tag["param2"]
                            url = tag["param3"]
                            WebWidth, WebHeight = map(int, tag["param1"].split('x'))
                            file.write(f'\n      # Browser\n')
                            file.write(f'        webview = QWebEngineView()\n')
                            file.write(f'        webview.setGeometry(150, 150, {WebWidth}, {WebHeight})\n')
                            file.write(f"        webview.setUrl(QUrl('{protokol}:{url}'))\n")
                            file.write(f'        self.layout.addWidget(webview)\n')

              
                        
                        elif show == "prefs" or "d":
                            file.write(f'        Weblabel = QLabel("ENGINE NAME:{tag["content"]}")\n')
                            file.write(f'        Weblabel.setAlignment(Qt.AlignCenter)\n')
                            file.write(f'        self.layout.addWidget(Weblabel)\n')
                            if  "param1" in tag:
                                width, height = map(int, tag["param1"].split('x'))
                                file.write(f'\n       # Added Label\n')
                                file.write(f'        label = QLabel("ENGINE SIZE:{width}, {height}")\n')
                                file.write(f'        label.setAlignment(Qt.AlignCenter)\n')
                                file.write(f'        self.layout.addWidget(label)\n')

                    
                            if "param2" in tag:
                                protokol = tag["param2"]
                                file.write(f'\n       # Added Label\n')
                                file.write(f'        label = QLabel("ENGINE PROTOKOL:{protokol}")\n')
                                file.write(f'        label.setAlignment(Qt.AlignCenter)\n')
                                file.write(f'        self.layout.addWidget(label)\n')
                                
                                

                            if "param3" in tag:
                                url = tag["param3"]
                                file.write(f'\n      # Added Label\n')
                                file.write(f'        label = QLabel("ENGINE URL:{url}")\n')
                                file.write(f'        label.setAlignment(Qt.AlignCenter)\n')
                                file.write(f'        self.layout.addWidget(label)\n')
                            
                        elif show != "show":
                            file.write(f'\n      # Passed Browser\n')
                   

                else:
                    file.write(f'        label = QLabel("{tag["content"]}")\n')
                    if "param1" in tag:
                        file.write(f'        label.setFont(QFont("Arial", {tag["param1"]}))\n')
                    if "param2" in tag:
                        file.write(f'        label.setStyleSheet("color: {tag["param2"]};")\n')
                    
                    file.write(f'\n      # Added Label\n')
                    file.write(f'        label.setAlignment(Qt.AlignCenter)\n')
                    file.write(f'        self.layout.addWidget(label)\n')
                   

            file.write("\ndef main():\n")
            file.write("    app = QApplication(sys.argv)\n")
            file.write("    ui = HumaUI()\n")
            file.write("    ui.show()\n")
            file.write("    sys.exit(app.exec_())\n\n")
            file.write("if __name__ == '__main__':\n")
            file.write("    main()\n")

    def run(self) -> None:
        self.parse_html()
        self.create_json_template()
        self.create_ui_file()

def main():
    html_file = "public/index.html"  # input("Dosya adını girin: ")
    engine = HumaHtmlEngine(html_file)
    engine.run()

if __name__ == "__main__":
    main()