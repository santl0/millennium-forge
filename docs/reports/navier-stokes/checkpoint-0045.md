## DÉCISION DU CYCLE

Sélectionner Caccioppoli locale, absorption et remplissage des trous, score
`19/20`, puis appliquer Simon. Réviser le brouillon initial : la borne
faible-`L3` seule ne donne pas d'énergie, mais la borne jointe à l'équation
lisse, à la pression de Riesz et à la force localement uniforme fournit une
dissipation locale. Fermer compacité, produit et admissibilité; pivoter vers
la persistance de trace.

## ÉQUATION ET TYPE DE SOLUTION

Sur `R3 x [-S,0]`, viscosité un, sans bord, les champs classiques
solénoïdaux vérifient
`partial_s Z_j-Delta Z_j+div(Z_j tensor Z_j)+nabla Pi_j+kappa(1+y dot nabla)Z_j=F_j`,
avec pression globale de Riesz, `kappa` fixé, borne uniforme
`L-infinity_sL^(3,infinity)_y` et `F_j->0` dans `C^infinity_y,loc`
uniformément en temps. La limite est faible adaptée pour l'équation
renormalisée non forcée; elle n'est pas encore dérenormalisée ni démontrée
non triviale.

## ÉCHELLE DES QUANTITÉS

Sous l'échelle Navier–Stokes physique, vitesse, pression et force ont les
amplitudes `lambda`, `lambda²`, `lambda³`; `L^(3,infinity)` et le stress
faible-`L^(3/2)` sont critiques. Les énergies locales normalisées
`r^-1 ess sup integral|u|²`, `r^-1 integral|nabla u|²` et les intégrales
cubiques/pression normalisées par `r^-2` sont invariantes. Le drift
renormalisé fixe une horloge et n'est pas déclaré invariant sous une seconde
dilatation à `kappa` fixé.

## AFFIRMATIONS AJOUTÉES OU MODIFIÉES

Ajout de `NS-TYPE-I-WEAK-L3-LOCAL-SUITABLE-COMPACTNESS`, statut
`COMPUTATION_ONLY`, portant le registre à 83 claims. Fermeture interne de
`GAP-TYPE-I-LOCAL-DISTRIBUTIONAL-COMPACTNESS` et
`GAP-TYPE-I-LOCAL-SUITABILITY-ENERGY`. Ajout de `FAIL-NS-0081`; le verrou
actif devient `GAP-TYPE-I-CRITICAL-TRACE-PERSISTENCE`, avant
dérenormalisation et rigidité ancienne faible-`L3`.

## PREUVE / SOURCE / CALCUL

La pression faible-`L^(3/2)` est localement `L^(4/3)`. Le test par cutoff,
Gagliardo–Nirenberg et Young absorbe le cubique et le flux de pression;
le remplissage des trous donne uniformément
`L-infinity_tL2_x,loc inter L2_tH1_x,loc`. Simon fournit forte `L2_loc`,
puis l'interpolation sous `L^(10/3)` donne forte `L3_loc` et produit fort
`L^(3/2)_loc`. La pression proche converge fortement, le reste harmonique
passe faible-étoile, et l'énergie locale passe. Albritton–Barker 2020 et
Barker–Seregin–Šverák 2018 sont ajoutés sous `NS-SRC-0187`–`0188`; le corpus
atteint 188 sources. La dérivation interne ne reçoit pas `PAPER_PROOF`.

## ÉCART AVEC LE PROBLÈME CLAY

La branche suppose un blow-up Type I et une borne faible-`L3` uniforme qui
ne découle pas de l'énergie Clay. La capture critique peut disparaître à la
trace malgré la compacité volumique. Il manque un observable fixe non nul,
l'horloge de dérenormalisation, la mildness ou classe ancienne exacte, puis
un théorème de rigidité faible-`L3`. Type II, le tore périodique et tout
blow-up admissible restent hors du résultat.

## TEST ADVERSE ET RÉSIDU CERTIFIÉ

Le registre exact passe 401 assertions. `C_n=nV(n dot)` conserve `K_3`, tend
vers zéro dans tous les espaces sous-critiques et dans `W^(-1,q)`, mais son
enstrophie croît comme `n` et son résidu PDE principal comme `n³`. Une couche
de cisaillement périodique forcée a volume `L2²=1/(6n²)`, dissipation `1/6`,
trace `1/2` et force `L2_tH^-1` carrée `7/6`; elle ne satisfait pas la
topologie forte de force du claim. Résidu numérique : nul, arithmétique
rationnelle exacte. Le certificat externe dépendant repasse 253 assertions.

## ARTEFACTS MIS À JOUR

Rapport principal, trois revues séparées, script de 401 assertions, claim
JSON, catalogue et audit de 188 sources, état de l'art, carte et graphe de
recherche, journal supercritique, questions ouvertes, registres des échecs,
expériences et formalisation, contexte, décisions et tâches persistantes.
Contrat, 83 claims, six prompts, JSON des sources, empreintes de preuve et
diff Git sont validés.

## ÉTAT : CONTINUER / RÉVISER / ABANDONNER / À REPRENDRE

CONTINUER. Le premier ledger a été révisé à la hausse après attaque
contradictoire; la compacité adaptée locale est conservée. La transmission
automatique d'une norme terminale est abandonnée. Aucun résultat Clay n'est
revendiqué.

## PROCHAINE EXPÉRIENCE DÉCISIVE

Tester si la capture Type I peut imposer un moment signé contre une fonction
test fixe, par propagation calorique rétrograde contrôlée ou par la condition
de persistance d'Albritton–Barker A.5. En parallèle adverse, chercher une
cascade PDE-compatible dont la force reste `C^infinity_x,loc`-petite
uniformément en temps tout en annulant chaque moment fixe; si elle survit,
abandonner la normalisation non signée actuelle.
