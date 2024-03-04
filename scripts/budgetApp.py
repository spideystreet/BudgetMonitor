class BudgetApp:
    def __init__(self):
        self.categories = {
            'shopping': [],
            'voiture': [],
            'alimentation': [],
            'loisirs': []
        }
        self.recettes = []

    def ajouter_depense(self, montant, categorie):
        if categorie in self.categories:
            self.categories[categorie].append(montant)

    def ajouter_recette(self, montant):
        self.recettes.append(montant)

    def calculer_solde(self):
        total_depenses = sum(sum(depenses) for depenses in self.categories.values())
        total_recettes = sum(self.recettes)
        return total_recettes - total_depenses
    def exporter_donnees(self):
        donnees = {
            'categories': self.categories,
            'recettes': self.recettes,
        }
        return donnees

    def calculer_total_par_categorie(self):
        return {categorie: sum(depenses) for categorie, depenses in self.categories.items()}
