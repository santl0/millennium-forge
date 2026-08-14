# DÉCISION DU CYCLE

Réfuter le halo de volume fixé par un témoin `v_j` et retenir la bande au
niveau global commun, score `20/20`. Fermer les queues, corridors et sections
variables comme échappements à la sélection endpoint pure-swirl disjointe;
activer `GAP-ACTIVE-HALO-DIAMETER-OR-OVERLAP`.

# ÉQUATION ET TYPE DE SOLUTION

Référence : Navier–Stokes incompressible non forcé sur `R3`, viscosité
`nu>0`. Objets traités : données initiales lisses compactes divergence-free
`U_j=(R_j/r)F_j e_theta` et leurs curls exacts. Aucune solution en temps,
pression, singularité admissible ou solution ancienne n'est construite.

# ÉCHELLE DES QUANTITÉS

`||U||_(L^(3,infinity))`, `||W||_(L^(3/2,infinity))` et leurs rapports sont
invariants sous le scaling Clay. `lambda V^(2/3)` et `integral_H|W|` ont
l'homogénéité `rho^-1`. La constante `C_I/324` ne dépend ni d'un rayon, ni du
diamètre axial, ni du volume support ou du nombre de cellules.

# AFFIRMATIONS AJOUTÉES OU MODIFIÉES

Ajout de `NS-FIXED-CORE-HALO-LOCALIZATION`, statut `REFUTED`, et de
`NS-PURE-SWIRL-COMMON-LEVEL-CELL-SELECTION`, statut `COMPUTATION_ONLY`, revue
`adversarial_pass`. Pour des cellules annulaires à supports complets disjoints,
une cellule vérifie
`K_(u,j)>=(C_I/324)K_u^2/K_w` et
`K_(u,j)/K_(w,j)>=(C_I/324)(K_u/K_w)^2` sans borne axiale ni plateau.

# PREUVE / SOURCE / CALCUL

Un niveau `lambda` presque optimal définit les superniveaux signés à
`lambda/2` et les bandes `lambda/4<+/-F_j<lambda/2`. Coaire R3 et
isopérimétrie donnent le registre; la bande est incluse dans
`{|U|>lambda/6}` et l'intégration faible-`L^(3/2)` donne la constante 324.
Fleming–Rishel, Federer–Fleming, Hunt/O'Neil et les analogues dynamiques sont
sourcés; aucun n'est présenté comme auteur de la composition interne. Le
corpus atteint 155 sources.

# ÉCART AVEC LE PROBLÈME CLAY

Le résultat est statique, pure-swirl, annulaire, fini et à supports complets
disjoints. Il ne localise pas la bande dans une boule, ne contrôle pas les
chevauchements ou annulations, ne traite ni composantes poloidales, pression,
diffusion, stretching, Type II, ni rayon pré-singulier tendant vers zéro.

# TEST ADVERSE ET RÉSIDU CERTIFIÉ

Le halo fixe est réfuté par une dilatation lisse curl-compatible. La queue
dyadique atteint un rapport support/coeur
`5396990266136737387081` sans faire disparaître le budget de curl au niveau
commun. Le certificat parcourt 1 536 familles, 12 288 superniveaux signés et
10 837 assertions rationnelles : zéro échec, résidu exact maximal zéro.
Empreinte
`b197d3b45af0f034c09c91d4b7bb6d3be55293ab1f458ec769c250c8998490f8`.

# ARTEFACTS MIS À JOUR

Deux claims, rapport principal, trois revues, expérience, catalogue et audit
des sources, veille, état de l'art, carte de recherche, graphe de dépendances,
registre supercritique, questions, deux échecs, backlog formel et journaux de
contexte/décision. Staging Git explicite; aucun historique réécrit ni travail
hors périmètre touché.

# ÉTAT : CONTINUER / RÉVISER / ABANDONNER / À REPRENDRE

CONTINUER vers la localisation métrique d'une composante active. ABANDONNER le
halo fixé par `v_j` et la queue longue comme fuite endpoint. À REPRENDRE pour
les chevauchements, la dynamique Type I/II et le passage au problème Clay.

# PROCHAINE EXPÉRIENCE DÉCISIVE

Construire une cellule pure-swirl avec `m` gouttelettes de diamètre `R`,
séparées par des distances croissantes et reliées sous `lambda/4`. Calculer le
curl de chaque raccord et décider si le budget commun sélectionne une goutte
de bon rapport dans une boule `O(R)`, ou seulement leur union dispersée.
