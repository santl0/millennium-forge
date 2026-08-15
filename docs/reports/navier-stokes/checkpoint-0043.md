## DÉCISION DU CYCLE

Sélectionner, avec le score `18/20`, la réalisation supportée et
pseudodifférentielle d'ordre `-1` de Bogovskiĭ, puis fermer la borne de la
force de cutoff mobile dans
`X=L1+div L^(3/2,infinity)`. Abandonner comme réfutation la seule croissance
haute fréquence en norme positive : elle est absorbée par la divergence du
stress dans `X`.

## ÉQUATION ET TYPE DE SOLUTION

Navier–Stokes incompressible 3D non forcé sur `R3`, viscosité un, sans bord,
pour une solution classique avant un temps maximal fini `T_*`, sous
`sup_(t<T_*)||u(t)||_(L^(3,infinity))<=M`. La pression est fixée par la jauge
globale de Riesz. Le résultat porte sur l'équation forcée satisfaite par le
champ localisé solénoïdal dans les variables Type I; il ne construit pas une
solution faible au temps terminal.

## ÉCHELLE DES QUANTITÉS

Sous `u_lambda(x,t)=lambda u(lambda x,lambda^2 t)`, on a
`p_lambda=lambda^2p` et `F_lambda=lambda^3F`. La quasi-norme faible-`L3` de
`u` est invariante. Pour `F=f+div G`, `||f||_L1` et
`||G||_(L^(3/2,infinity))` sont invariantes; la borne obtenue est donc
critique et indépendante du rayon de cutoff `R`. Elle dépend de la
réalisation fixe de Bogovskiĭ et de `kappa(M)`.

## AFFIRMATIONS AJOUTÉES OU MODIFIÉES

Ajout de `NS-TYPE-I-MOVING-CUTOFF-CRITICAL-FORCE-BOUND`, statut
`COMPUTATION_ONLY`, avec revue contradictoire et dépendances explicites. Le
corpus contient désormais 81 claims canoniques. Le trou
`GAP-TYPE-I-MOVING-COMMUTATOR-BOUND` est fermé pour l'opérateur fixé; il est
remplacé par `GAP-TYPE-I-FORCE-COMPACTNESS`, puis
`GAP-TYPE-I-FORCED-RIGIDITY`.

## PREUVE / SOURCE / CALCUL

La décomposition exacte est
`K_kappa(U)=f_kappa(U)+div(-2U tensor nabla chi)`, avec les commutateurs
`[Delta,B M_a]` d'ordre zéro et `[D,B M_a]` d'ordre `-1`. Elle donne
`||F_sol||_X<=C[M^2+(1+|kappa|)M]`. Costabel–McIntosh fournit l'opérateur
supporté d'ordre `-1` et l'échelle Sobolev supportée; les ordres de
commutateurs sont une dérivation symbolique interne. Geißert–Heck–Hieber,
théorème 2.5, fournit directement
`B:W_0^(-1,4/3)=(W^(1,4))' -> L^(4/3)` pour les données de masse nulle. La
source `NS-SRC-0185` porte le corpus primaire à 185 entrées.

## ÉCART AVEC LE PROBLÈME CLAY

La borne n'implique ni petitesse ni disparition de la force localisée. Elle
n'apporte pas la compacité forte des champs ou de la pression, ne permet pas
encore le passage des produits quadratiques et ne produit pas de solution
ancienne non forcée. La borne faible-`L3` Type I est une hypothèse
conditionnelle non déduite de l'énergie Clay; Type II reste séparé.

## TEST ADVERSE ET RÉSIDU CERTIFIÉ

Le témoin pure-swirl divergence-free vérifie exactement
`a dot U_N=a dot Delta U_N=0`. La norme positive satisfait
`||[Delta,chi]U_N||_2>=epsilon(5N/32-8/15)` pour `N>=16`, mais la
représentation négative vérifie uniformément
`||f_0||_1<=99epsilon/140` et
`||G_0||_(L^(3/2,infinity))<=8epsilon/5`. Le registre symbolique passe 222
assertions exactes, résidu algébrique nul; aucune simulation Navier–Stokes ni
erreur de discrétisation n'est revendiquée. La passe bibliographique isole le
résidu fonctionnel : aucune source ne couvre sans qualification le grand
espace intrinsèque `(W_0^(2,p'))'`.

## ARTEFACTS MIS À JOUR

Rapport analytique, trois passes séparées de même famille de modèle, script adverse, claim JSON,
catalogue et audit des sources, carte de recherche, graphe de dépendances,
journal supercritique, questions ouvertes, registres des expériences, de la
formalisation et des échecs, contexte, décisions et tâches persistantes. Les
validations du contrat, des claims, des prompts, de l'expérience et du diff
Git sont consignées dans le checkpoint Git du cycle.

## ÉTAT : CONTINUER / RÉVISER / ABANDONNER / À REPRENDRE

CONTINUER. La borne critique est conservée; la réfutation par norme positive
est abandonnée; toute conclusion de compacité ou de rigidité reste à réviser
jusqu'à preuve.

## PROCHAINE EXPÉRIENCE DÉCISIVE

Introduire une coupure à facteur externe `L`, garder le core dans `B1` et
placer la transition dans `B_L\B_(L/2)`. Suivre toutes les constantes de
Bogovskiĭ, des commutateurs, de la pression et de Leray, puis tester si la
force disparaît sur chaque compact quand `L->infinity` sans perdre la capture
Type I. En cas d'échec, fixer la topologie faible-étoile exacte de `X` et
tester le passage des produits quadratiques.
