import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from budgetApp import BudgetApp
import tkinter.simpledialog as simpledialog

class BudgetUI:
    def __init__(self, budget_app):
        self.categories = {} 
        self.budget_app = budget_app
        
        self.root = tk.Tk()
        self.root.title("Gestion de budget")
        self.root.iconbitmap("logo.ico")
        self.root.geometry("600x600")
        #Bloquer la redimensionnement de la fenêtre
        self.root.resizable(False, False)
        self.depense_var = tk.StringVar(self.root)
        self.recette_var = tk.StringVar(self.root)
        self.setup_ui()
        self.depense_var.trace("w", self.check_fields)
        self.recette_var.trace("w", self.check_fields)
    def setup_ui(self):
        # Champs de saisie pour les dépenses
        depense_label = tk.Label(self.root, text="Dépense :")
        depense_label.pack()
        self.depense_entry = tk.Entry(self.root, textvariable=self.depense_var)  # Lier la variable
        self.depense_entry.pack()

        # Menu déroulant pour les catégories de dépenses
        categorie_label = tk.Label(self.root, text="Catégorie :")
        categorie_label.pack()
        self.categorie_var = tk.StringVar(self.root)
        self.categorie_var.set("shopping")  # valeur par défaut
        self.categorie_menu = ttk.Combobox(self.root, textvariable=self.categorie_var, values=list(self.budget_app.categories.keys()))
        self.categorie_menu.pack()
        # Bouton pour ajouter une catégorie
        self.ajouter_categorie_button = tk.Button(self.root, text="Ajouter une catégorie", command=self.ajouter_categorie_callback)
        self.ajouter_categorie_button.pack()
        # Champs de saisie pour les recettes
        recette_label = tk.Label(self.root, text="Recette :")
        recette_label.pack()
        self.recette_entry = tk.Entry(self.root, textvariable=self.recette_var)  # Lier la variable
        self.recette_entry.pack()

        # Boutons
        self.ajouter_depense_button = tk.Button(self.root, text="Ajouter une dépense", command=self.ajouter_depense_callback)
        self.ajouter_depense_button.pack()

        self.ajouter_recette_button = tk.Button(self.root, text="Ajouter une recette", command=self.ajouter_recette_callback)
        self.ajouter_recette_button.pack()

        # Bouton pour exporter les données
        self.exporter_donnees_button = tk.Button(self.root, text="Exporter les données", command=self.exporter_donnees_callback)
        self.exporter_donnees_button.pack()
        

        # Initialiser les boutons avec l'état "disabled"
        self.ajouter_depense_button.config(state="disabled")
        self.ajouter_recette_button.config(state="disabled")

        # Étiquette pour afficher le solde actuel
        self.solde_label = tk.Label(self.root, text="Solde actuel : 0")
        self.solde_label.pack()


    def ajouter_categorie_callback(self):
        nouvelle_categorie = simpledialog.askstring("Nouvelle Catégorie", "Entrez le nom de la nouvelle catégorie:")
        if nouvelle_categorie:
            if nouvelle_categorie not in self.budget_app.categories:
                self.budget_app.categories[nouvelle_categorie] = []
                self.categorie_menu['values'] = list(self.budget_app.categories.keys())



    def check_fields(self, *args):
        print("Checking fields...")
        print("Depense entry:", self.depense_entry.get())
        print("Recette entry:", self.recette_entry.get())

        # Vérifier si les champs de dépense et de recette sont remplis
        if self.depense_entry.get() and self.recette_entry.get():
            print("Both fields are filled.")
            self.ajouter_depense_button.config(state="active")
            self.ajouter_recette_button.config(state="active")
        elif self.depense_entry.get():
            print("Only the depense field is filled.")
            self.ajouter_depense_button.config(state="active")
            self.ajouter_recette_button.config(state="disabled")
        elif self.recette_entry.get():
            print("Only the recette field is filled.")
            self.ajouter_recette_button.config(state="active")
            self.ajouter_depense_button.config(state="disabled")
        else:
            print("At least one field is empty.")
            self.ajouter_depense_button.config(state="disabled")
            self.ajouter_recette_button.config(state="disabled")



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
    def exporter_donnees_callback(self):
        donnees = self.budget_app.exporter_donnees()
        # csv
        with open('donnees.csv', 'w') as f:
            f.write("categorie,depense\n")
            for recette in donnees['recettes']:
                f.write(f"recette,{recette}\n")
            for categorie, depenses in donnees['categories'].items():
                for depense in depenses:
                    f.write(f"{categorie},{depense}\n")

    
            




    def afficher_solde(self):
        solde = self.budget_app.calculer_solde()
        self.solde_label.config(text=f"Solde actuel : {solde}")

    def mettre_a_jour_graphique(self):
        self.fig = Figure(figsize=(6, 6))
        self.ax = self.fig.add_subplot(111)

        # Calculer les totaux par catégorie
        total_par_categorie = self.budget_app.calculer_total_par_categorie()

        # Créer des listes pour les catégories et les montants
        categories_filtrees = []
        montants_filtres = []

        # Parcourir les catégories et les montants et les inclure dans les listes filtrées si le montant est non nul
        for cat, montant in total_par_categorie.items():
            if montant != 0:
                categories_filtrees.append(cat)
                montants_filtres.append(montant)

        # Créer le graphique uniquement si des catégories filtrées sont présentes
        if categories_filtrees:
            self.ax.pie(montants_filtres, labels=categories_filtrees, autopct='%1.1f%%')

            # Créer le canvas s'il n'existe pas encore
            if not hasattr(self, 'canvas'):
                self.canvas = FigureCanvasTkAgg(self.fig, self.root)
                self.canvas_widget = self.canvas.get_tk_widget()
                self.canvas_widget.pack()
            else:
                # Supprimer et recréer le canvas pour mettre à jour le graphique
                self.canvas_widget.pack_forget()
                self.canvas = FigureCanvasTkAgg(self.fig, self.root)
                self.canvas_widget = self.canvas.get_tk_widget()
                self.canvas_widget.pack()
            self.canvas.draw()  # Mettre à jour le graphique
        else:
            # Afficher un message indiquant qu'il n'y a pas de données à afficher
            no_data_label = tk.Label(self.root, text="Pas de données à afficher")
            no_data_label.pack()
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = BudgetApp()
    ui = BudgetUI(app)
    ui.run()
