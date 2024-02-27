import tkinter as tk

class BudgetUI:
    def __init__(self, budget_app):
        
        self.budget_app = budget_app

        # Fenetre principale
        self.root = tk.Tk()

        # Champs de saisie pour les dépenses et les recettes
        depense_label = tk.Label(self.root, text="Dépense :")
        depense_label.pack()
        self.depense_entry = tk.Entry(self.root)
        self.depense_entry.pack()

        recette_label = tk.Label(self.root, text="Recette :")
        recette_label.pack()
        self.recette_entry = tk.Entry(self.root)
        self.recette_entry.pack()

        # Boutons pour ajouter une dépense ou une recette
        ajouter_depense_button = tk.Button(self.root, text="Ajouter une dépense", command=self.ajouter_depense_callback)
        ajouter_depense_button.pack()

        ajouter_recette_button = tk.Button(self.root, text="Ajouter une recette", command=self.ajouter_recette_callback)
        ajouter_recette_button.pack()

        # Création de l'étiquette pour afficher le solde actuel
        self.solde_label = tk.Label(self.root, text="Solde actuel :")
        self.solde_label.pack()

    def ajouter_depense_callback(self):
        # Recupération du montant de la dépense
        montant = float(self.depense_entry.get())
        # Appel de la méthode ajouter_depense de la classe BudgetApp pour ajouter la dépense à la liste des dépenses
        self.budget_app.ajouter_depense(montant)
        # Mise à jour de l'affichage du solde actuel
        self.afficher_solde()

    def ajouter_recette_callback(self):
        # Récupération du montant de la recette saisie par l'utilisateur
        montant = float(self.recette_entry.get())
        # Appel de la méthode ajouter_recette de la classe BudgetApp pour ajouter la recette à la liste des recettes
        self.budget_app.ajouter_recette(montant)
        # Mise à jour de l'affichage du solde actuel
        self.afficher_solde()

    def afficher_solde(self):
        # Calcul du solde actuel en appelant la méthode calculer_solde de la classe BudgetApp
        solde = self.budget_app.calculer_solde()
        # Mise à jour de l'étiquette correspondante dans l'interface utilisateur
        self.solde_label.config(text="Solde actuel : {}".format(solde))

    def run(self):
        # Lancement de la boucle principale de la fenetre graphique
        self.root.mainloop()