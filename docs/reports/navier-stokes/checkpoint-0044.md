## DÉCISION DU CYCLE

Sélectionner le lemme de fuite locale de la force projetée, score `19/20`,
et distinguer définitivement convergence locale et contrôle critique global.
Conserver le résultat local; abandonner la conjecture de convergence globale
dans `X=L1+div L^(3/2,infinity)` sous le seul éloignement de la couronne.

## ÉQUATION ET TYPE DE SOLUTION

Navier–Stokes incompressible 3D non forcé sur `R3`, viscosité un, sans bord,
pour une solution classique avant un temps maximal fini, avec jauge globale
de Riesz et borne Type I
`sup_sigma||U(sigma)||_(L^(3,infinity))<=M`. Le champ tronqué satisfait
l'équation renormalisée avec drift `+kappa D` et force `F_L`; aucune solution
faible terminale ou ancienne n'est construite.

## ÉCHELLE DES QUANTITÉS

Sous `u_lambda=lambda u(lambda x,lambda^2t)`, la pression se dilate comme
`lambda^2`, la force comme `lambda^3`, `L^(3,infinity)` et
`L^(3/2,infinity)` pour le stress restent critiques. Le noyau lointain de
`P div` est homogène de degré `-4`; une dérivée spatiale supplémentaire
gagne une puissance de `L`. Le contre-profil de drift se dilate comme
`kappa L^-1h(dot/L)` et sa norme globale `X` comme `L^2`.

## AFFIRMATIONS AJOUTÉES OU MODIFIÉES

Ajout de `NS-TYPE-I-OUTER-CUTOFF-LOCAL-FORCE-ESCAPE`, statut
`COMPUTATION_ONLY`, portant le corpus à 82 claims canoniques. Fermeture de
`GAP-TYPE-I-FORCE-LOCAL-ESCAPE`; réfutation globale enregistrée sous
`FAIL-NS-0080`. Le verrou est remplacé par
`GAP-TYPE-I-LOCAL-COMPACTNESS-TRACE`, puis
`GAP-TYPE-I-ANCIENT-WEAK-L3-RIGIDITY`.

## PREUVE / SOURCE / CALCUL

Pour `L>=2rho`, les commutateurs et `Q_LH` coïncident localement avec leurs
termes non tronqués, d'où
`F_L=P div(Z_L tensor Z_L-U tensor U)` dans `B_rho`. Le stress est nul dans
`B_L` et uniformément borné dans faible-`L^(3/2)`; la sommation dyadique donne
`||partial^alpha F_L||_Linf(B_rho)<=C_alpha(1+C_Q^2)M^2L^(-3-|alpha|)`.
Bradshaw–Tsai (`NS-SRC-0186`) source le gain lointain de pression; Wolf,
Kwon et Hunt sourcent les autres ingrédients. Le catalogue atteint 186
sources; la borne complète reste une dérivation interne auditée.

## ÉCART AVEC LE PROBLÈME CLAY

Le résultat suppose une borne Type I faible-`L3`, non contrôlée par l'énergie
Clay. Il ne donne ni compacité forte locale, ni passage du produit et de
l'inégalité d'énergie locale, ni pression limite, ni trace non triviale. Il
reste ensuite à dérenormaliser exactement le drift et à obtenir un théorème
de rigidité pour les solutions anciennes faible-`L3`. Type II et le cas
périodique exigent des raccords séparés.

## TEST ADVERSE ET RÉSIDU CERTIFIÉ

Le registre exact passe 253 assertions. Il certifie les numérateurs du noyau
`24` et `204`, les bornes rationnelles d'ordre zéro et un, et les taux
`11904/35 M L^-3`, `134912/25 M L^-4`. Un pure-swirl critique donne pour la
force complète
`F_L=L^-3B_0(dot/L)+kappa L^-1h(dot/L)` et
`||F_L||_X>=c|kappa|L^2-C` lorsque `kappa!=0`. Résidu de discrétisation : nul,
car le test est rationnel et symbolique; aucune simulation du PDE n'est
revendiquée. Le registre dépendant du cycle 0042 repasse 499 assertions.

## ARTEFACTS MIS À JOUR

Rapport analytique, trois revues séparées, expérience exacte, claim JSON,
catalogue et audit des sources, état de l'art, carte et graphe de recherche,
journal supercritique, questions ouvertes, registres des échecs, expériences
et formalisation, contexte, décisions et tâches persistantes. Les contrôles
du contrat, des 82 claims, des six prompts, des 253+499 assertions et du diff
Git sont tous passants.

## ÉTAT : CONTINUER / RÉVISER / ABANDONNER / À REPRENDRE

CONTINUER. Le lemme local est conservé; la convergence globale dans `X` est
abandonnée; tout passage à une solution ancienne reste à réviser jusqu'à
fermeture de la compacité et de la non-trivialité.

## PROCHAINE EXPÉRIENCE DÉCISIVE

Écrire un ledger Aubin–Lions local sur `B_rho x [-S,0]` avec espaces exacts
pour `partial_sigma Z_j`, pression, force et produit quadratique. Construire
en parallèle logique un contre-profil de concentration temporelle conservant
toutes les bornes spatiales disponibles; s'il survit, identifier l'estimation
temporelle minimale qui le détruit, puis tester la persistance de la trace du
core avant toute rigidité ancienne.
