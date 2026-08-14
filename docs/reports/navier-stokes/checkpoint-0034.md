# DÉCISION DU CYCLE

Réfuter le pigeonhole fondé sur les seules quasi-normes faibles et retenir la
sélection sous registre BV, score `19/20`. Fermer les cellules pure-swirl
épaisses, disjointes et uniformément enregistrées; activer
`GAP-DEGENERATE-CELL-REGISTER-OR-OVERLAP`.

# ÉQUATION ET TYPE DE SOLUTION

Référence : Navier–Stokes incompressible non forcé sur `R3`, viscosité
`nu>0`. Objets effectivement traités : familles finies de données initiales
compactes divergence-free, puis cellules pure-swirl
`U_j=(R_j/r)F_j e_theta`, `W_j=curl U_j`. Aucune trajectoire, pression,
solution ancienne ou singularité admissible n'est construite.

# ÉCHELLE DES QUANTITÉS

`||U||_(L^(3,infinity))`, `||W||_(L^(3/2,infinity))`, leurs rapports et les
moyennes d'oscillation sont invariants sous le scaling Clay. Le registre
`A_jv_j^(2/3)` et `integral|W_j|` ont la même loi d'échelle. Le rayon d'une
cellule se divise par le facteur de dilatation; les gates seuls ne prouvent pas
que le rayon sélectionné tend vers zéro.

# AFFIRMATIONS AJOUTÉES OU MODIFIÉES

Ajout de `NS-WEAK-LORENTZ-CELL-SELECTION`, statut `REFUTED`, et de
`NS-BV-REGISTERED-HETEROGENEOUS-CELL-SELECTION`, statut `COMPUTATION_ONLY`,
revue `adversarial_pass`. Sous plateau effectif, boîte comparable et registre
`integral_(Q_j)|W_j|>=cA_jv_j^(2/3)`, une cellule vérifie
`K_(u,j)>=cK_u^2/K_w` et
`K_(u,j)/K_(w,j)>=c(K_u/K_w)^2`. Le cycle 0033 donne ensuite
`MO_(B_j)>=c(K_u/K_w)^12`.

# PREUVE / SOURCE / CALCUL

La preuve choisit un niveau global presque optimal de vitesse, utilise la
densité du plateau pour contrôler chaque `v_j`, somme le registre BV, puis
applique `integral_E|W|<=3K_w|E|^(1/3)` sur l'union des boîtes. Coaire et
isopérimétrie fournissent le registre pour les cellules pure-swirl épaisses.
Lions, Solimini, Gérard, Jaffard, Koch, Bahouri–Cohen–Koch et Barker–Prange
sont ajoutés comme `NS-SRC-0140`–`0147`; aucun ne source la sélection statique
nouvelle. Le corpus atteint 147 sources.

# ÉCART AVEC LE PROBLÈME CLAY

Le résultat est statique, axisymétrique dans son corollaire, à cellules
disjointes, aspect borné, plateau uniforme et boîte comparable. Il ne traite
ni longues queues, chevauchements et annulations de curls, composantes
poloïdales, pression non locale, cutoff de Leray, diffusion, stretching,
Type II ou sélection d'une échelle pré-singulière.

# TEST ADVERSE ET RÉSIDU CERTIFIÉ

Le contre-exemple exact satisfait `K_u=1`, `K_w^3<=64/49` et des rapports
locaux cubiques `8^-n`, mais viole le registre curl-compatible. Le certificat
teste quatre lignes fermées, deux distributions matérialisées et 1 152
familles enregistrées, soit 9 792 cellules et 31 746 assertions rationnelles :
zéro échec. Empreinte
`d918ff7ec5e200d388cde1d3ed5230ebdd4535bc65fc3b94a2c7ac21c0962763`.
Le calcul encode le registre BV; il ne certifie pas coaire au continuum.

# ARTEFACTS MIS À JOUR

Deux claims, rapport principal, trois revues, expérience, catalogue et audit
des sources, veille, état de l'art, carte de recherche, graphe de dépendances,
registre supercritique, questions, échecs, backlog formel et journaux de
contexte/décision. Les commits sont auditables et la branche de travail est
poussée; `main` local reste intact. Aucune pull request n'est possible sans
branche de base distante distincte.

# ÉTAT : CONTINUER / RÉVISER / ABANDONNER / À REPRENDRE

CONTINUER sur les registres dégénérés et chevauchants. ABANDONNER la sélection
par quasi-normes seules. À REPRENDRE pour produire dynamiquement une cellule
de rayon tendant vers zéro et pour le passage Type I vers Type II.

# PROCHAINE EXPÉRIENCE DÉCISIVE

Construire des cellules lisses à coeur–queue avec
`|Q_j|/v_j->infinity`, calculer leurs fonctions de distribution complètes et
le curl de tout raccord, puis déterminer si une queue de faible amplitude peut
reproduire les niveaux dyadiques sans payer un nouveau plateau effectif. En
cas de réfutation, le test des curls chevauchants signés sera le cycle suivant,
avant toute projection de Leray.
