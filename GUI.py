import tkinter as tk
from functools import partial, reduce

# Fonction pure pour calculer le nouveau budget
def calculer_budget(budget_actuel, montant, operation):
    return budget_actuel + montant if operation == 'ajouter' else budget_actuel - montant

# Historique des transactions comme une liste immuable
historique_transactions = []

# Fonction pour mettre à jour l'interface et le budget
def mise_a_jour_interface(label_budget, entree_montant, listbox_historique, operation):
    montant = float(entree_montant.get())
    budget_actuel = float(label_budget["text"])
    nouveau_budget = calculer_budget(budget_actuel, montant, operation)
    label_budget.config(text=str(nouveau_budget))
    # Ajout de la transaction à l'historique
    global historique_transactions
    historique_transactions.append((montant, operation))
    mise_a_jour_historique(listbox_historique)

# Mettre à jour l'historique des transactions dans la Listbox
def mise_a_jour_historique(listbox_historique):
    listbox_historique.delete(0, tk.END)  # Effacer les entrées existantes
    for montant, operation in historique_transactions:
        listbox_historique.insert(tk.END, f"{operation}: {montant}")

# Initialisation de l'interface
def init_interface():
    root = tk.Tk()
    root.title("Moniteur de Budget")
    root.geometry("500x500")  # Taille de la fenêtre

    label_budget = tk.Label(root, text="0")
    label_budget.pack()

    entree_montant = tk.Entry(root)
    entree_montant.pack()

    listbox_historique = tk.Listbox(root)
    listbox_historique.pack()

    bouton_ajouter = tk.Button(root, text="Ajouter", command=partial(mise_a_jour_interface, label_budget, entree_montant, listbox_historique, 'ajouter'))
    bouton_ajouter.pack()

    bouton_soustraire = tk.Button(root, text="Soustraire", command=partial(mise_a_jour_interface, label_budget, entree_montant, listbox_historique, 'soustraire'))
    bouton_soustraire.pack()

    root.mainloop()

init_interface()
