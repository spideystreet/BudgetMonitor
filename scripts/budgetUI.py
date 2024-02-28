import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from budgetApp import BudgetApp  # Assurez-vous que cela correspond à votre structure de fichiers

class BudgetUI:
    def __init__(self, budget_app):
        self.budget_app = budget_app
        self.root = tk.Tk()
        self.setup_ui()

    def setup_ui(self):
        # Champs de saisie pour les dépenses
        depense_label = tk.Label(self.root, text="Dépense :")
        depense_label.pack()
        self.depense_entry = tk.Entry(self.root)
        self.depense_entry.pack()

        # Menu déroulant pour les catégories de dépenses
        categorie_label = tk.Label(self.root, text="Catégorie :")
        categorie_label.pack()
        self.categorie_var = tk.StringVar(self.root)
        self.categorie_var.set("shopping")  # valeur par défaut
        self.categorie_menu = ttk.Combobox(self.root, textvariable=self.categorie_var, values=list(self.budget_app.categories.keys()))
        self.categorie_menu.pack()

        # Champs de saisie pour les recettes
        recette_label = tk.Label(self.root, text="Recette :")
        recette_label.pack()
        self.recette_entry = tk.Entry(self.root)
        self.recette_entry.pack()

        # Boutons
        ajouter_depense_button = tk.Button(self.root, text="Ajouter une dépense", command=self.ajouter_depense_callback)
        ajouter_depense_button.pack()
        ajouter_recette_button = tk.Button(self.root, text="Ajouter une recette", command=self.ajouter_recette_callback)
        ajouter_recette_button.pack()

        # Étiquette pour afficher le solde actuel
        self.solde_label = tk.Label(self.root, text="Solde actuel : 0")
        self.solde_label.pack()

        # Zone de graphique pour le camembert
        self.fig = Figure(figsize=(6, 6))
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, self.root)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack()

    def ajouter_depense_callback(self):
        montant = float(self.depense_entry.get())
        categorie = self.categorie_var.get()
        self.budget_app.ajouter_depense(montant, categorie)
        self.afficher_solde()
        self.mettre_a_jour_graphique()

    def ajouter_recette_callback(self):
        montant = float(self.recette_entry.get())
        self.budget_app.ajouter_recette(montant)
        self.afficher_solde()
        self.mettre_a_jour_graphique()

    def afficher_solde(self):
        solde = self.budget_app.calculer_solde()
        self.solde_label.config(text=f"Solde actuel : {solde}")

    def mettre_a_jour_graphique(self):
        self.ax.clear()  # Efface le tracé précédent
        total_par_categorie = self.budget_app.calculer_total_par_categorie()
        categories = list(total_par_categorie.keys())
        montants = list(total_par_categorie.values())
        self.ax.pie(montants, labels=categories, autopct='%1.1f%%')
        self.canvas.draw()

    def run(self):
        self.root.mainloop()

# Test
if __name__ == "__main__":
    app = BudgetApp()
    ui = BudgetUI(app)
    ui.run()
