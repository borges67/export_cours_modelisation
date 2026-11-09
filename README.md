# Mission LaPosteImmobilier : séances 1 et 2

Notebooks élèves des séances 1 et 2 du cours de modélisation (IFPEN), avec les données nécessaires.

| Élément | Rôle |
|---|---|
| `seance1_eleve.ipynb` | Séance 1 : demande électrique des bureaux, aujourd'hui et en 2040 |
| `seance2_eleve.ipynb` | Séance 2 : production solaire, prix, facture et niveau de solaire des bureaux en 2040 |
| `data/lpi/` | Fichiers transmis par LPI |
| `data/interne/` | Données du modélisateur (températures, PV, prix, CO2, PAC) |
| `data/resultats/consommation/` | Consommation d'un site de chaque type, calculée avec la méthode de la séance 1, lue par la séance 2 |

## Sur Google Colab

1. Ouvrir le lien du notebook donné en cours.
2. Faire **Fichier > Enregistrer une copie dans Drive** pour garder son travail.
3. Exécuter la première cellule de code (sous « Imports ») : elle télécharge les données dans la machine Colab.
   Il faut la relancer à chaque nouvelle session.

## En local

```
pip install -r requirements.txt
jupyter notebook
```

Les notebooks se lancent depuis ce dossier (chemins relatifs, `data/...`).
