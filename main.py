#atamalar
import random
import json
import ast

#fonksiyonlar
def parse_html(html_file, tag):
    if tag == "h1":
        h1_tags = []

        # HTML dosyasını aç
        with open(html_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Her satırı kontrol et
        for line in lines:
            # Satırda <h1> etiketi var mı kontrol et
            if "<huma:1>" in line:
                # Satır içerisinde <h1> etiketi varsa, içeriğini al ve listeye ekle
                start_index = line.find("<huma:1>") + len("<huma:1>")
                end_index = line.find("</huma:1>")
                h1_content = line[start_index:end_index]
                h1_tags.append(h1_content)

        return h1_tags
    elif tag == "h2":
        h2_tags = []

        # HTML dosyasını aç
        with open(html_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Her satırı kontrol et
        for line in lines:
            # Satırda <h2> etiketi var mı kontrol et
            if "<huma:2>" in line:
                # Satır içerisinde <h2> etiketi varsa, içeriğini al ve listeye ekle
                start_index = line.find("<huma:2>") + len("<huma:2>")
                end_index = line.find("</huma:2>")
                h2_content = line[start_index:end_index]
                h2_tags.append(h2_content)

        return h2_tags

    elif tag == "p":
        p_tags = []

        # HTML dosyasını aç
        with open(html_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Her satırı kontrol et
        for line in lines:
            # Satırda <h2> etiketi var mı kontrol et
            if "<huma:p>" in line:
                # Satır içerisinde <h2> etiketi varsa, içeriğini al ve listeye ekle
                start_index = line.find("<huma:p>") + len("<huma:p>")
                end_index = line.find("</huma:p>")
                p_content = line[start_index:end_index]
                p_tags.append(p_content)

        return p_tags

    elif tag == "title":
        title_tags = []

        # HTML dosyasını aç
        with open(html_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Her satırı kontrol et
        for line in lines:
            # Satırda <h2> etiketi var mı kontrol et
            if "<huma:window:title>" in line:
                # Satır içerisinde <h2> etiketi varsa, içeriğini al ve listeye ekle
                start_index = line.find("<huma:window:title>") + len("<huma:window:title>")
                end_index = line.find("</huma:window:title>")
                title_content = line[start_index:end_index]
                title_tags.append(title_content)

        return title_tags

    elif tag == "size":
        size_tags = []

        # HTML dosyasını aç
        with open(html_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Her satırı kontrol et
        for line in lines:
            # Satırda <h2> etiketi var mı kontrol et
            if "<huma:window:size>" in line:
                # Satır içerisinde <h2> etiketi varsa, içeriğini al ve listeye ekle
                start_index = line.find("<huma:window:size>") + len("<huma:window:size>")
                end_index = line.find("</huma:window:size>")
                size_content = line[start_index:end_index]
                size_tags.append(size_content)

        return size_tags

    elif tag == "text":
        text_tags = []
 
        # HTML dosyasını aç
        with open(html_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Her satırı kontrol et
        for line in lines:
            # Satırda <huma:t: etiketi var mı kontrol et
            if "<huma:t:" in line:
                # Satır içerisinde <huma:t: etiketi varsa, içeriğini al ve font boyutunu belirleyerek listeye ekle
                start_index = line.find("<huma:t:") + len("<huma:t:")
                end_index = line.find(">", start_index)  # Sayıdan sonraki > işaretini bul
                font_size_str = line[start_index:end_index]  # Sayıyı al
                try:
                    font_size = int(font_size_str)  # String olarak alınan sayıyı integer'a çevir
                except ValueError:
                    # Sayı olarak işlenemeyen durumlar için hata ver
                    print("Hata: Sayı bulunamadı veya geçersiz.")
                    continue

                # Sonraki metni al ve listeye ekle
                text_content = line[end_index + 1:line.find("</huma:t:", end_index)]  # Sonraki metni al
                text_tags.append((text_content, font_size))  # Metni ve font boyutunu bir tuple olarak ekle
                
        return text_tags



def parse_tags(count):
    if count == "hepsi":
        h1_tags = parse_html(html_file, "h1")
        h2_tags = parse_html(html_file, "h2")
        p_tags = parse_html(html_file, "p")
        title_tags = parse_html(html_file, "title")
        size_tags = parse_html(html_file, "size")
        return h1_tags, h2_tags, p_tags, title_tags, size_tags
        


    elif count == "head":
        h2_tags = parse_html(html_file, "h2")
        h1_tags = parse_html(html_file, "h1")
        return h1_tags, h2_tags
      
    else:
        print("Geçersiz")
def template(json):
    # JSON formatındaki çıktıyı dosyaya yazma
    asil_sayi = random.randint(0, 5000)
    asil_ad = f"temp.yeniui{asil_sayi}.json"
    with open(f"./output.json", "w") as file:
        file.write(json)
        print(f"Dosya yazdırıldı: {asil_ad}")

 
def pythonayaz(veri):
    veri_dict = json.loads(veri)
    with open("ui.py", "a") as dosya:
        for key, values in veri_dict.items():  
                if key == "title tagleri":
                    for value in values:
                        print(value)
                        titleid = random.randint(0,1000)
                        dosya.write(f'print("pencere: {value}")\n')
                        dosya.write(f'root.title("{value}")\n')
                        dosya.write(f'# Bu pencerenin "title" kimliği: {titleid}... \n')
                elif key == "size tagleri":
                    for value in values:
                        print(value)
                        sizeid = random.randint(0,1000)
                        dosya.write(f'print("pencere boyutu: {value}")\n')
                        dosya.write(f'root.geometry("{value}")\n')
                        dosya.write(f'# Bu pencerenin "size" kimliği: {sizeid}... \n')
                elif key == "h1 tagleri":
                    for value in values:
                        h1id = random.randint(0,1000)
                        dosya.write(f'texth1{h1id} = tk.Label(root, text="{value}", font=("Arial", 24), fg="white")\n')
                        dosya.write(f'texth1{h1id}.pack()\n')
                elif key == "h2 tagleri" :
                    for value in values:
                        h2id = random.randint(0,1000)
                        dosya.write(f'texth2{h2id} = tk.Label(root, text="{value}", font=("Arial", 20), fg="white")\n')
                        dosya.write(f'texth2{h2id}.pack()\n')
                elif key == "p tagleri" :
                    for value in values:
                        pid = random.randint(0,1000)
                        dosya.write(f'textp{pid} = tk.Label(root, text="{value}", font=("Arial", 16), fg="white")\n')
                        dosya.write(f'textp{pid}.pack()\n')
                elif key == "text" and isinstance(values, list):
                    for value, font_size in values:  # Iterate through values (value, font_size tuples)
                        textid = random.randint(0, 1000)
                        dosya.write(f'text{textid} = tk.Label(root, text="{value}", font=("Arial", {font_size}), fg="white")\n')
                        dosya.write(f'text{textid}.pack()\n')
                    
                
def arayuzubitir(dosya):
    with open(dosya, "a") as file:
        file.write("\nroot.mainloop()")

def arayuzubaslat(dosya):
    girismetni = """
import tkinter as tk
# Ana pencereyi oluştur
root = tk.Tk()
#root.geometry("400x300")
#root.configure(bg=”black”)
#root.title("Hüma")
#https://vastseablog.com/
"""
    with open(dosya, "w") as file:
        file.write(girismetni)


def create_ui():
    #Parse işlemleri
    h1_tags = parse_html(html_file, "h1")
    h2_tags = parse_html(html_file, "h2")
    p_tags = parse_html(html_file, "p")
    title_tags = parse_html(html_file, "title")
    size_tags = parse_html(html_file, "size")
    text_tags = parse_html(html_file, "text")
    tag_dict = {
        "title tagleri": title_tags, 
        "size tagleri": size_tags, 
        "h1 tagleri": 
        h1_tags, 
        "h2 tagleri": 
        h2_tags, 
        "p tagleri": 
        p_tags, 
        "text": 
        text_tags 
    }
    # JSONa dönüştür
    tag_json = json.dumps(tag_dict)
    template(tag_json)
    arayuzubaslat("ui.py")
    pythonayaz(tag_json)
    arayuzubitir("ui.py")
    
# Kullanıcıdan dosya adını al
html_file = "index.html" #input("Dosya adını girin: ")
# Fonksiyonu çağır ve  etiketleri  yazdır
#show_tags("hepsi")
create_ui()