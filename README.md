
# Hüma QtMarkup

Hüma QtMarkup (HQM), özel bir HTML benzeri sözdizimi kullanarak PyQt5 tabanlı kullanıcı arayüzleri oluşturmak için geliştirilmiş deneysel bir projedir.

## Proje Hakkında

HHE, basit bir HTML benzeri sözdizimi kullanarak hızlı ve kolay bir şekilde PyQt5 tabanlı kullanıcı arayüzleri oluşturmanıza olanak tanır. Özel `<huma:>` etiketleri kullanarak pencere özellikleri, metin öğeleri ve hatta web içeriği ekleyebilirsiniz.

## Özellikler

- Özel HTML benzeri sözdizimi
- PyQt5 tabanlı arayüz oluşturma
- Dinamik etiket işleme
- JSON çıktısı oluşturma
- Web içeriği görüntüleme desteği (QWebEngineView)

## Kullanım

1. `public/index.html` dosyasını özel Hüma etiketleriyle düzenleyin.
2. Scripti çalıştırın: `python3 install.sh`
3. Scripti çalıştırın: `python3 run.sh`
4. Script, HTML'i işleyecek ve `build/ui.py` dosyasını oluşturacaktır. ve çalıştıracaktır
 

## Etiket Örnekleri

```XHTML
<!DOCTYPE hml>
<!ENCODİNG utf-8>
<hqm lang="hqm">
<sets>
    <huma:window:size>500x500</huma:window:size>    
    <huma:window:title>Pencere adı</huma:window:title>
    <huma:window:style>style.css</huma:window:style>
</sets>
<window>
    <huma:t:12:red>Welcome To World Wide Web</huma:t>
    <huma:webengine:500x500:https://uzaylinin-notlari.netlify.app/:show>Hüma On PyQtWebEngine</huma:webengine:500x500:https://google.com>
 
</window>
</hqm>
 
```

## Gereksinimler

- Python 3.x
- PyQt5
- PyQtWebEngine

## Kurulum

1. Repo'yu klonlayın:
   ```
   git clone https://github.com/VastSea0/huma-markup-lang
   ```
2. Gerekli paketleri yükleyin:
   ```
   python -m venv hwe
   source hwe/bin/activate
   pip install pyqt5 pyqtwebengine
   ```

## Katkıda Bulunma

Bu deneysel bir projedir ve geliştirmeye açıktır. Öneriler, hata raporları ve pull request'ler her zaman hoş karşılanır.

## Ekran Görüntüleri

![image](https://github.com/user-attachments/assets/6b185706-dcc8-4819-9074-2bd1f2af6f5a)

## Kaynaklar,
[PyQt5](https://www.pythonguis.com/pyqt5-tutorial/)

## Lisans
[MIT Lisansı](LICENSE)

## İletişim

Sorularınız veya önerileriniz için vastseaoffical0@outlook.com adresinden bana ulaşabilirsiniz.


