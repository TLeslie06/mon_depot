import tkinter as tk

class Window(tk.Tk):
   def __init__(self):
    super().__init__()

    self.title("Exercice 3")
    self.configure(bg="purple")
    self.geometry("400x300")

    self.label = tk.Label(self, text="Entrez votre nom", bg="purple", font=("Comic Sans MS", 12), fg="white")
    self.label.pack(pady=30)

    self.entry = tk.Entry(self)
    self.entry.pack(pady=10)

    self.bouton = tk.Button(self, text= "Afficher", command=self.get_text)
    self.bouton.pack(pady=30)

    self.label_resultat = tk.Label(self, text="", bg="purple" )
    self.label_resultat.pack(pady=20)

   def get_text(self):
    text_saisi = self.entry.get()
    self.label_resultat.config(text=f"Bonjour, {text_saisi}.\nBienvenue dans le monde de la cybersécurité. ", 
                               font=("Comic Sans MS",12), fg="white") 
    

my_window=Window()
my_window.mainloop()
