from tkinter import *
from tkinter import messagebox

top = Tk()
top.title("Students")
top.geometry("500x300")


# 1. Frame pour Nom
frame_nom = Frame(top)
frame_nom.pack(pady=10)

label_nom = Label(frame_nom, text="Nom :",fg="red")
label_nom.grid(row=0, column=0, padx=5)
entry_nom = Entry(frame_nom, fg="red", cursor="man")
entry_nom.grid(row=0, column=1, padx=5)

# 2. Frame pour Age
frame_age = Frame(top)
frame_age.pack(pady=5)

label_age = Label(frame_age, text="Age :", fg="green")
label_age.grid(row=0, column=0, padx=5)
entry_age = Entry(frame_age, fg="green", cursor="pirate")
entry_age.grid(row=0, column=1, padx=5)

# 3. Checkbuttons
frame_activite = Frame(top)
frame_activite.place(x=50, y=90)  

var_s = IntVar()
var_m = IntVar()
var_i = IntVar()

label_activites = Label(frame_activite, text="Activités", fg="purple", font=("Arial", 12))
label_activites.grid(row=0, column=0)

bouton_sport = Checkbutton(frame_activite, text="Sport", fg="purple",activeforeground="red",variable=var_s)
bouton_sport.grid(row=1, column=0,pady=5)
bouton_musique = Checkbutton(frame_activite, text="Musique", fg="purple",activeforeground="blue",variable=var_m)
bouton_musique.grid(row=2, column=0, pady=5)
bouton_lecture = Checkbutton(frame_activite, text="Lecture",fg="purple",activeforeground="red", variable=var_i)
bouton_lecture.grid(row=3, column=0, pady=5)

#bouton radio
frame_statut = Frame(top)
frame_statut.place(x=350, y=90) 

label_statuts = Label(frame_statut, text="Statuts",fg="orange", font=("Arial", 12))
label_statuts.grid(row=0, column=0)

statut = IntVar() 

bouton_etudiant = Radiobutton(frame_statut, text="Etudiant",fg="orange", activeforeground="orange", variable=statut, value=1)
bouton_etudiant.grid(row=1, column=0,pady=5)
bouton_professionnel = Radiobutton(frame_statut, text="Professionnel",fg="orange",activeforeground="orange", variable=statut, value=2)
bouton_professionnel.grid(row=2, column=0,pady=5)
bouton_independant = Radiobutton(frame_statut, text="Indépendant", fg="orange",activeforeground="orange",variable=statut, value=3)
bouton_independant.grid(row=3, column=0,pady=5)


#bouton valider
frame_validation = Frame(top)
frame_validation.place(x=235, y=250)

def loisir():
    activites = []

    if var_s.get() == 1:
        activites.append("Sport")
    if var_m.get() == 1:
        activites.append("Musique")
    if var_i.get() == 1:
        activites.append("Lecture")
    
    if len(activites) == 0:
        activites.append("Pas d'activité")
    
    return activites



def donnees():
    nom = entry_nom.get()

    if nom == "":
        messagebox.showerror("Erreur", "Le nom ne peut pas être vide.")
        return
    

    try:
        age = int(entry_age.get())
        messagebox.showinfo("donneUSER", f"Nom : {nom}\nAge : {age}\nCentre interet :{loisir()}")
    except ValueError:
        messagebox.showerror("Erreur de saisie", "L'âge doit être un nombre.")


bouton_valider = Button(frame_validation, text="Valider",bg="light blue", 
                        command= lambda : donnees())
bouton_valider.pack()



top.mainloop()
