
import tkinter as tk
# Ana pencereyi oluştur
root = tk.Tk()
#root.geometry("400x300")
#root.configure(bg=”black”)
#root.title("Hüma")
print("pencere: Pencere adı")
root.title("Pencere adı")
# Bu pencerenin "title" kimliği: 962... 
print("pencere boyutu: 800x600")
root.geometry("800x600")
# Bu pencerenin "size" kimliği: 978... 
texth1192 = tk.Label(root, text="H1", font=("Arial", 24), fg="white")
texth1192.pack()
texth2510 = tk.Label(root, text="H2", font=("Arial", 20), fg="white")
texth2510.pack()
textp387 = tk.Label(root, text="bu bir paragraf", font=("Arial", 16), fg="white")
textp387.pack()
textp346 = tk.Label(root, text="bu bir paragraf", font=("Arial", 16), fg="white")
textp346.pack()
textp1 = tk.Label(root, text="bu bir paragraf", font=("Arial", 16), fg="white")
textp1.pack()
textp923 = tk.Label(root, text="bu bir paragraf", font=("Arial", 16), fg="white")
textp923.pack()
text74 = tk.Label(root, text="BU 30 PİXEL TEXT", font=("Arial", 30), fg="white")
text74.pack()
text966 = tk.Label(root, text="26 PİXEL TEXT", font=("Arial", 26), fg="white")
text966.pack()
text647 = tk.Label(root, text="16 PİXEL TEXT.", font=("Arial", 16), fg="white")
text647.pack()
text204 = tk.Label(root, text="56 PİXEL TEXT.", font=("Arial", 56), fg="white")
text204.pack()
text268 = tk.Label(root, text="108  pixel text", font=("Arial", 108), fg="white")
text268.pack()

root.mainloop()