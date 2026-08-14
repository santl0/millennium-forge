# DÉCISION DU CYCLE

Retenir la troncature signée par composante, score `20/20`, devant le
contre-profil multi-gouttes (`18/20`) et la boule Vitali depuis le volume
(`15/20`). Fermer les gouttelettes reliées strictement sous `lambda/4` et
activer `GAP-ABOVE-THRESHOLD-THIN-BRIDGE`.

# ÉQUATION ET TYPE DE SOLUTION

Référence : Navier–Stokes incompressible non forcé sur `R3`, viscosité
`nu>0`. Objets traités : données lisses compactes divergence-free pure-swirl
`U_j=(R_j/r)F_j e_theta`, leurs curls exacts et des troncatures
`W_c^(1,infinity)` à temps fixé. Aucune solution en temps, pression,
singularité admissible ou solution ancienne n'est construite.

# ÉCHELLE DES QUANTITÉS

`||U||_(L^(3,infinity))`, `||curl U||_(L^(3/2,infinity))` et leurs rapports
sont invariants sous le scaling Clay. `lambda V_alpha^(2/3)` et
`integral|curl U_alpha|` ont l'homogénéité `rho^-1`. Les constantes
`C_I/648` et `c_Lambda` ne dépendent ni du nombre ni de la séparation des
gouttes.

# AFFIRMATIONS AJOUTÉES OU MODIFIÉES

Ajout de `NS-PURE-SWIRL-COMPONENTWISE-DROPLET-SELECTION` et
`NS-PURE-SWIRL-LIPSCHITZ-DIRECTION-GATE`, statuts `COMPUTATION_ONLY`, revues
`adversarial_pass`. Une composante tronquée vérifie
`K_(u,alpha)>=(C_I/648)K_u^2/K_w` et un rapport local quadratique; sous
diamètre `O(R_j)`, son oscillation directionnelle est minorée par une
puissance douze du rapport global. Le registre compte 72 claims.

# PREUVE / SOURCE / CALCUL

La troncature `(sigma F-lambda/4)_+1_C` est lipschitzienne à trace nulle : son
curl ne possède aucune mesure de bord. Coaire R3 par composante,
isopérimétrie et intégration faible-`L^(3/2)` donnent `648=36*18`.
Frank–Lieb borne la masse dans une boule de rayon `V/P`, tandis que
Ambrosio–Caselles–Masnou–Morel, Fusco–Maggi–Pratelli, Seregin et Barker
séparent composantes BV, petit déficit et centres dynamiques. Sept sources
primaires sont ajoutées; corpus à 162.

# ÉCART AVEC LE PROBLÈME CLAY

Le résultat est statique, pure-swirl, annulaire et à supports originaux
disjoints. Il suppose un diamètre composante `O(R_j)` seulement pour le gate
directionnel. Ponts au-dessus du seuil, chevauchements/annulations, composante
poloïdale, pression, diffusion, stretching, Type II et sélection dynamique
de `R_j(t)->0` restent absents.

# TEST ADVERSE ET RÉSIDU CERTIFIÉ

Le certificat principal parcourt 1 920 familles, 10 560 composantes et 5 773
assertions rationnelles : zéro échec, résidu exact minimal nul. Le script
embarqué indépendant ajoute 465 contrôles, facteur 648 et résidu nul. Pour
`m` copies identiques, le cube du rapport global normalisé vaut exactement
`1/m`; le filament `lambda/8` est sous les deux cutoffs. Empreinte principale
`f0550313e21e05a7cda46fd8d1264b982d3ab3b809b5c5b05ec1f77c5c56892a`.

# ARTEFACTS MIS À JOUR

Deux claims, rapport principal, trois revues, expérience, sept sources,
catalogue/audit/veille, état de l'art, carte, graphe de dépendances, questions,
registre supercritique, deux échecs, backlog formel, contexte, décisions et
todo. Les quatre validations contractuelles et les deux certificats exacts
réussissent; aucun historique ou travail externe n'est réécrit.

# ÉTAT : CONTINUER / RÉVISER / ABANDONNER / À REPRENDRE

CONTINUER vers le pont mince au-dessus du seuil. ABANDONNER les copies
identiques, les filaments strictement sous `lambda/4` et le renforcement
volume+périmètre vers un diamètre uniforme. À REPRENDRE pour chevauchements,
dynamique Type I/II et passage au problème Clay.

# PROCHAINE EXPÉRIENCE DÉCISIVE

Relier deux gouttes de rayon `R`, distantes de `LR`, par un tube d'amplitude
juste supérieure à `lambda/4` et de rayon `delta R`. Calculer les distributions
complètes des deux couches de transition et décider si un choix
`delta=delta(L)` garde les endpoints non dégénérés quand `L->infinity`, ou si
le curl force une seconde troncature de diamètre `O(R)`.
