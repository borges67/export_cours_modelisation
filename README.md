# Mission LaPosteImmobilier : séances 1, 2 et 3

Notebooks élèves des séances 1, 2 et 3 du cours de modélisation (IFPEN), avec les données nécessaires.

| Élément | Rôle |
|---|---|
| `seance1_eleve.ipynb` | Séance 1 : demande électrique des bureaux, aujourd'hui et en 2040 |
| `seance2_eleve.ipynb` | Séance 2 : production solaire, prix, facture et niveau de solaire des bureaux en 2040 |
| `seance3_eleve.ipynb` | Séance 3 : dimensionnement du solaire et de la batterie par optimisation linéaire |
| `modele_lineaire.py` | Graphique d'une semaine de résultats, utilisé par la séance 3 |
| `data/lpi/` | Fichiers transmis par LPI |
| `data/interne/` | Données du modélisateur (températures, PV, prix, CO2, PAC) |
| `data/resultats/consommation/` | Consommation d'un site de chaque type, calculée avec la méthode de la séance 1, lue par la séance 2 |
| `data/resultats/prix/` | Tarifs d'achat et puissances solaires possibles de chaque bâtiment, exportés par la séance 2, lus par la séance 3 |

## Sur Google Colab

1. Ouvrir le lien du notebook donné en cours.
2. Faire **Fichier > Enregistrer une copie dans Drive** pour garder son travail.
3. Exécuter la première cellule de code (sous « Imports ») : elle télécharge les données dans la machine Colab
   (et installe `pulp` pour la séance 3).
   Il faut la relancer à chaque nouvelle session.

## En local

```
pip install -r requirements.txt
jupyter notebook
```

Les notebooks se lancent depuis ce dossier (chemins relatifs, `data/...`).
