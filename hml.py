class HtmlTag:
    """
    Özelliklere ve içeriğe sahip bir HTML tag'ini temsil eder.
    """

    def __init__(self, tag, content, cls="", id=""):
        """
        Bir HtmlTag nesnesini başlatır.

        Args:
            tag (str): HTML tag adı (örneğin, "h1", "p", "div").
            content (str): Tag'in içine yerleştirilecek içerik.
            cls (str, optional): Tag'e uygulanacak bir CSS sınıfı. Varsayılan olarak "".
            id (str, optional): Tag için bir ID özniteliği. Varsayılan olarak "".
        """

        self.tag = tag
        self.content = content
        self.cls = cls
        self.id = id

    def __str__(self):
        """
        HtmlTag nesnesinin tam bir HTML tag olarak metin temsilini döndürür.
        """

        return f"<{self.tag} class='{self.cls}' id='{self.id}'> {self.content} </{self.tag}>"

    def dosyaya_yaz(self, dosya_adi, goster=False):
        """
        HTML tag'ini bir dosyaya yazar.

        Args:
            dosya_adi (str): Yazılacak dosyanın adı.
            goster (bool, optional): Oluşturulan HTML tag'i konsola yazdırmak için. Varsayılan olarak False.

        Raises:
            IOError: Dosyaya yazarken hata oluşursa.
        """

        try:
            with open(dosya_adi, "w") as dosya:
                dosya.write(str(self))
                if goster:
                    print(str(self))
        except IOError as e:
            print(f"'{dosya_adi}' dosyasına yazarken hata: {e}")

# Kullanım
tag = HtmlTag("h1", "helo", cls="baslik", id="hosgeldiniz")
tag.dosyaya_yaz("index.html", goster=True)
