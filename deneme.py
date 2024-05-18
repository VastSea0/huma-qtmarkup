import ast
import json

# Verilen girdi
girdi = """["h1 tagleri: ['Deneme', 'Deneme2', 'Deneme h2den h1']", "h2 tagleri: ['Deneme', 'Deneme2', 'Deneme h2den h1']"]"""


def temzile(temizlencekgirdi):

    liste_girdi = ast.literal_eval(temizlencekgirdi)

    # Çıktı oluşturma
    cikti = {}
    for item in liste_girdi:
        key, value = item.split(': ')
        key = key.strip('"')
        value = ast.literal_eval(value)
        cikti[key] = value

    
    # Sözlüğü JSON formatına dönüştürme
    cikti_json = json.dumps(cikti, indent=4)

    # JSON formatındaki çıktıyı dosyaya yazma
    with open("output.json", "w") as file:
        file.write(cikti_json)
        