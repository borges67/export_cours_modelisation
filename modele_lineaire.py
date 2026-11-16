"""Graphique des résultats du modèle linéaire de la séance 3 : une semaine, heure par heure."""
import matplotlib.pyplot as plt
import pandas as pd

# (colonne, légende, couleur) : ce qui entre dans le site (production), ce qui en sort (consommation)
PRODUCTION = [("production_pv", "production solaire", "gold"), ("decharge_batterie", "décharge de la batterie", "tab:green"),
              ("achat_reseau", "achat au réseau", "tab:grey")]
CONSOMMATION = [("consommation", "consommation du bâtiment", "tab:blue"), ("charge_batterie", "charge de la batterie", "yellowgreen"),
                ("vente_reseau", "vente au réseau", "tab:purple"), ("ecretement", "écrêtement du solaire", "lightgrey")]


def tracer_semaine(resultat, prix_achat, prix_vente, debut, titre):
    """Graphique empilé des 7 jours qui commencent le jour `debut` : en haut la production (ce qui entre dans le site),
    en bas la consommation (ce qui en sort) ; les deux se compensent heure par heure.

    `resultat` : une ligne par heure, une colonne par actif (kW) ; `prix_achat`, `prix_vente` : une valeur par heure de
    l'année (EUR/MWh), tableau numpy ou série pandas.
    """
    fin = pd.Timestamp(debut) + pd.Timedelta(days=7) - pd.Timedelta(hours=1)
    s = resultat.loc[debut:fin]
    # les prix sur les mêmes heures que les résultats, puis la même semaine
    achat = pd.Series(list(prix_achat), index=resultat.index).loc[debut:fin]
    vente = pd.Series(list(prix_vente), index=resultat.index).loc[debut:fin]

    fig, ax = plt.subplots(figsize=(14, 4.5))
    haut = ax.stackplot(s.index, *[s[c] for c, _, _ in PRODUCTION], colors=[k for _, _, k in PRODUCTION])
    bas = ax.stackplot(s.index, *[-s[c] for c, _, _ in CONSOMMATION], colors=[k for _, _, k in CONSOMMATION])
    ax.axhline(0, color="black", lw=0.8)
    limite = 1.05 * max(sum(s[c] for c, _, _ in PRODUCTION).max(), sum(s[c] for c, _, _ in CONSOMMATION).max(), 1)
    ax.set_ylim(-limite, limite)
    ax.set_ylabel("kW : production (+), consommation (-)")

    # deux légendes séparées : production, puis consommation
    legende_production = ax.legend(haut, [l for _, l, _ in PRODUCTION], title="Production", fontsize=8,
                                   loc="upper left", bbox_to_anchor=(1.06, 1))
    ax.add_artist(legende_production)
    ax.legend(bas, [l for _, l, _ in CONSOMMATION], title="Consommation", fontsize=8,
              loc="center left", bbox_to_anchor=(1.06, 0.45))

    ax2 = ax.twinx()
    ax2.plot(achat.index, achat, color="black", lw=1, label="prix d'achat")
    ax2.plot(vente.index, vente, color="black", lw=1, ls="--", label="prix de vente")
    ax2.set_ylabel("EUR/MWh")
    ax2.legend(title="Prix", fontsize=8, loc="lower left", bbox_to_anchor=(1.06, 0))

    ax.set_title(titre)
    fig.tight_layout()
    plt.show()
