import tkinter as tk

def afficher_selection():
    indices = liste.curselection()

    print("Concepts sélectionnés:")
    for i in indices:
        element = liste.get(i)
        print("-", element)

window = tk.Tk()
window.title("Concept de cybersecurité")
window.geometry("300x400")
window.configure(bg="yellow")

liste = tk.Listbox(window, selectmode="multiple")
liste.pack(pady=20)

concepts= ["Phishing", "Malware", "Firewall", "Chiffrement", "VPN"]


for concept in concepts:
    liste.insert(tk.END, concept)

bouton = tk.Button(window, text="Afficher", command=afficher_selection)
bouton.pack()



window.mainloop()