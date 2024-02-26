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


Documentation
==================

La documentation est disponible sous

.. code-block:: python

   BudgetMonitor/docs/build/html/index.html

.. important:: HTML static

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
