import tkinter as tk

# Ana pencereyi oluştur
root = tk.Tk()
root.geometry("400x300")
root.title("Hüma")

# Metin etiketini oluştur
text = tk.Label(root, text="Bu bir metin etiketi", font=("Arial", 24), fg="black")
text.pack()

# Pencereyi göster
root.mainloop()
