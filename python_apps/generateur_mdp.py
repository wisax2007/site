from tkinter import *
import random

tous_les_caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:,.<>?"

def mdp():
    mot = ""
    try:
        longueur = int(entre_longueur.get())
        
        if longueur <= 0:
            mot_de_passe.config(text="Entrez un nombre > 0", fg="red")
        else:
            for i in range(longueur):
                mot += random.choice(tous_les_caracteres)
            mot_de_passe.config(text=mot, fg="blue")
            
    except ValueError:
        mot_de_passe.config(text="Entrez un nombre valide", fg="red")

window = Tk()
window.title("Générateur de MDP")
window.geometry("400x350")
window.config(padx=20, pady=20)

Label(window, text="Sécurisez vos comptes", font=("Arial", 14, "bold")).pack(pady=10)

Label(window, text="Longueur du mot de passe :").pack()
entre_longueur = Entry(window)
entre_longueur.pack(pady=5)

Label(window, text="Mot de passe généré :").pack(pady=10)


mot_de_passe = Label(window, text="", font=("Courier", 10, "bold"), wraplength=350)
mot_de_passe.pack(pady=5)

btn_generer = Button(window, text="Générer le mot de passe", command=mdp, bg="#4CAF50", fg="white")
btn_generer.pack(fill=X, padx=5, pady=20)

window.mainloop()