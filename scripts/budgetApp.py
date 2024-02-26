class BudgetApp:
    def __init__(self):
        # Initialisation des listes de dépenses et de recettes
        self.depenses = []
        self.recettes = []

    def ajouter_depense(self, montant):
        # Ajout d'une dépense à la liste des dépenses
        self.depenses.append(montant)

    def ajouter_recette(self, montant):
        # Ajout d'une recette à la liste des recettes
        self.recettes.append(montant)

    def calculer_solde(self):
        # Calcul du total des dépenses et des recettes
        total_depenses = sum(self.depenses)
        total_recettes = sum(self.recettes)
        # Calcul du solde actuel
        return total_recettes - total_depenses