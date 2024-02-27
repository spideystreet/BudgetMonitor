from budgetApp import BudgetApp
from budgetUI import BudgetUI

# Création d'une instance de la classe BudgetApp
budget_app = BudgetApp()
# Création d'une instance de la classe BudgetUI en lui passant l'instance de BudgetApp en paramètre
budget_ui = BudgetUI(budget_app)
# Lancement de l'application en appelant la méthode run de la classe BudgetUI
budget_ui.run() 