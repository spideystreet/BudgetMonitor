.. BudgetMonitor DOC documentation master file, created by
   sphinx-quickstart on Mon Feb 26 10:56:57 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=============================================
Welcome to BudgetMonitor DOC's !
=============================================

Introduction
============

BudgetMonitor est une petite application avec interface graphique développée en Python et utilisant un maximum de notions de programmation fonctionnelle.

Fonctionnalités
===============

- **Entrer ses recettes**
- **Connaître ses dépenses**
- **Gérer son budget**

=====================
Développeurs
=====================

Cette section est faite pour pouvoir utiliser et modifier le code.

GIT
==================

.. note:: **REPO** : *https://github.com/spideystreet/BudgetMonitor*


Pour modifier le code :

1. Pull le main **(main)** (= récup les dernieres modifs)

.. code-block:: python

   git checkout origin main
   git pull

2. Créer une nouvelle branche
   
.. code-block:: python

   git checkout -b nom_de_ma_branche

3. Une fois les modifs finie dans la branche, poussez les modifs **dans la branche**

.. code-block:: python

   git commit -m "Détail sur les modifs"
   git push origin <nom_de_ma_branche>


.. important:: Ensuite on verra ensemble si on pousse la modif dans le main

4. Charger les dépendances

.. code-block:: python

   python -m venv venv   #Crée son env virtuel (si pas déjà fait)
   source venv/bin/activate   #Charge l'env virtuel
   pip install -r BudgetMonitor/requirements.txt   #Installe les dépendances dans l'environnement

Utilisation
==================

Cette section donnera les infos nécessaires pour utiliser BudgetMonitor.

- Lancement de l'app

.. code-block:: python

   python scripts/main.py

.. image:: ../build/_static/interface.png


On peut ajouter deux choses : 

- Des recettes
- Des dépenses

Plusieurs catégories sont là pour définir les dépenses : 

- shopping
- voiture
- alimentation
- loisirs


Exemple : 500 de recette initiale et des dépenses aoutées à la main

.. image:: ../build/_static/demo.png



Notions fonctionnelle
=====================

Plusieurs notions de programmation fonctionnelle sont utilisées ici. 
- En voici quelques unes :

1. Fonctions d'ordre supérieur :

- BudgetApp.py :

.. code-block:: python

    def calculer_solde(self):
        # Calcul du total des dépenses et des recettes
        total_depenses = sum(self.depenses)
        total_recettes = sum(self.recettes)
        # Calcul du solde actuel
        return total_recettes - total_depenses

2. Immutabilité :

- BudgetApp.py :

.. code-block:: python

         #  Utilisations de la fonction sum()
         self.depenses.append(montant)
         self.recettes.append(montant)

1. Fonctions comme des citoyens de premiere classe :

- BudgetUI.py :
  
.. code-block:: python

         #  Passage en argument des fonctions aux boutons Tkinter
         ajouter_depense_button = tk.Button(self.root, text="Ajouter une dépense", command=self.ajouter_depense_callback)
         ajouter_recette_button = tk.Button(self.root, text="Ajouter une recette", command=self.ajouter_recette_callback)



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
