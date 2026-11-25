# Séance 3 : dimensionnement du solaire et de la batterie

| Élément | Rôle |
|---|---|
| `seance3_envoie.ipynb` | Le notebook de la séance 3 : modèle linéaire corrigé (parties 1 et 2), émissions de CO2 et indicateurs à compléter (parties 3 et 4) |
| `data/resultats/consommation/2040/<bâtiment>/` | Consommation 2040 de chaque type de bâtiment, par usage, pour les années climatiques 2008, 2009 et 2012 (séance 1) |
| `data/resultats/prix/<bâtiment>/` | Tarifs d'achat spot, plat et HP/HC (`tarifs.csv`) et puissances solaires possibles (`kwc.csv`), exportés par la séance 2 |
| `data/interne/` | Données internes : production d'un kWc de solaire (`courbe_pv.csv`) et contenu CO2 horaire de l'électricité (`courbe_co2.csv`), lus par le notebook ; prix spot 2040, températures, courbe de PAC et paramètres de tarifs (`parametres.xlsx`) pour le rapport |
| `data/lpi/` | Fichiers transmis par LPI : description des bâtiments types, nombre de bâtiments du parc et flotte en 2040 |

Le notebook écrit ses résultats dans `data/resultats/modele/<bâtiment>/` : on peut changer de bâtiment, de tarif,
d'injection, de coût de batterie ou de capacités minimales dans les premières cellules, puis relancer.

## Sur Google Colab

1. Ouvrir le lien du notebook donné en cours.
2. Faire **Fichier > Enregistrer une copie dans Drive** pour garder son travail.
3. Exécuter la première cellule de code (sous « Imports ») : elle télécharge ce dossier dans la machine Colab et
   installe `pulp`. Il faut la relancer à chaque nouvelle session.

## En local

```
pip install -r requirements.txt
jupyter notebook seance3_envoie.ipynb
```

Le notebook se lance depuis ce dossier (chemins relatifs `data/...`). Compter environ 30 secondes par résolution du
modèle, soit 2 minutes pour tout le notebook.
