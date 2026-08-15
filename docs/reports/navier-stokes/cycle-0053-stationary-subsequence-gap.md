# Cycle 0053 — défaut de générateur et sous-suite stationnaire

Date : 2026-08-15.

Statut : `AI_INTERNAL_DERIVATION`; aucune conclusion Clay.

## Décision adaptative

Le verrou relu est
`GAP-TYPE-I-ANCIENT-SIGNED-BASE-FLUX-CANCELLATION`. Le cycle 0052 a montré
qu'une estimation absolue du flux perd exactement une demi-puissance au
passé et que le Liouville backward auto-similaire faible-`L3` est déjà
publié. Les actions candidates sont :

| action | nouveauté | tractabilité | falsifiabilité | levier | total |
|---|---:|---:|---:|---:|---:|
| raccorder un petit générateur renormalisé à un profil stationnaire interdit | 4 | 5 | 5 | 5 | **19** |
| calculer le gain visqueux d'une triade isolée intégrée en temps | 4 | 5 | 5 | 3 | 17 |
| prouver directement une cancellation dyadique du flux de base | 5 | 2 | 4 | 5 | 16 |

La première action est sélectionnée. Le lemme actif est unique : transformer
une sous-suite de fenêtres où `partial_s Z` tend vers zéro dans un espace
négatif endpoint en un profil stationnaire global non nul, puis le confronter
au Liouville publié.

## Cadre exact

Soit `kappa>0`. Sur `R3 x (-infinity,0]`, sans frontière, considérons une
solution ancienne renormalisée faible adaptée locale

```text
partial_s Z-Delta Z+div(Z tensor Z)+nabla Pi
  +kappa(1+y dot nabla)Z=0,
div Z=0,                                                 (53.1)
```

avec pression globale

```text
Pi=R_iR_j(Z_i Z_j),
sup_(s<=0)||Z(s)||_(L^(3,infinity))<=M.                 (53.2)
```

La sortie Type I des cycles 0045--0046 possède en outre une capture
persistante : il existe `gamma>0` tel que, pour tout intervalle borné
`J subset (-infinity,0]`,

```text
integral_J integral_(B_1)|Z(y,s)|^3 dy ds
  >=|J| gamma^3.                                         (53.3)
```

Il ne s'agit ni de l'équation standard en temps physique, ni d'Euler, ni
d'une équation forcée. Le drift est autonome et sa constante `kappa` reste
fixée pendant toutes les translations temporelles.

## Espace négatif endpoint

Pour `R>=1`, notons `Y_R` la fermeture des champs tests vectoriels
`C_c^infinity(B_R)` pour la norme de Lorentz--Sobolev

```text
||phi||_(Y_R)
 =||phi||_(L^(3,1)(R3))+||nabla phi||_(L^(3,1)(R3)),      (53.4)
```

après prolongement par zéro, et `X_R=Y_R^*`. Pour éviter de supposer une
mesurabilité forte dans ce dual endpoint, définissons directement la
variation distributionnelle intégrée

```text
D_R(s)=sup |integral_(s-1)^s
              <partial_sigma Z(sigma),psi(sigma)>dsigma|, (53.5)
```

où le supremum porte sur les tests vectoriels lisses, supportés dans
`B_R x (s-1,s)`, tels que
`sup_sigma||psi(sigma)||_(Y_R)<=1`. Lorsque `partial_s Z` admet un
représentant de Bochner dans `L1 X_R`, (53.5) est dominée par sa norme
`L1 X_R`; aucune telle représentation n'est requise ici.

Le raffinement Lorentz de (53.4) est indispensable. Le stress et la pression
sont seulement dans `L^(3/2,infinity)`; leur dual endpoint est
`L^(3,1)`, pas `L3` sans second indice suivi.

La quantité (53.5) est finie sur chaque fenêtre. En effet, l'équation permet
de définir son action sans choisir de représentant ponctuel du générateur :

1. `nabla Z in L2_loc` contrôle `Delta Z` contre `nabla phi`, car sur une
   boule `L^(3,1)` s'injecte dans `L2`;
2. `Z tensor Z` et `Pi` dans `L^(3/2,infinity)` se pairent avec
   `nabla phi` dans `L^(3,1)`;
3. le drift se traite par intégration par parties, les facteurs `y` étant
   bornés sur `B_R`.

Les ensembles de tests sont emboîtés. Ainsi

```text
R_1<=R_2  implique  ||f||_(X_(R_1))<=||f||_(X_(R_2)),
D_(R_1)(s)<=D_(R_2)(s).                                  (53.6)
```

## Lemme de non-stationnarité quantitative

Sous (53.1)--(53.3), il existe un rayon entier `R_*>=1`, puis des constantes
`epsilon_*>0` et `S_*<0`, dépendant de l'orbite, tels que

```text
boxed: D_(R_*)(s)>=epsilon_* pour tout s<=S_*.            (53.7)
```

Autrement dit, une limite Type I capturée ne peut devenir asymptotiquement
stationnaire sur toutes les boules pendant des fenêtres unitaires de temps
similaire. La conclusion n'affirme aucune valeur explicite de `R_*` ou
`epsilon_*`, aucune périodicité et aucune borne de flux spectral.

## Preuve par contradiction et diagonalisation

Supposons (53.7) fausse. Grâce à la monotonie (53.6), cela implique pour
chaque entier `m>=1`

```text
liminf_(s->-infinity)D_m(s)=0.                            (53.8)
```

On choisit alors `s_n<=-n-2` tel que

```text
D_n(s_n)<=1/n.                                           (53.9)
```

Posons, sur toute fenêtre compacte en `tau`,

```text
Z_n(y,tau)=Z(y,s_n+tau),
Pi_n(y,tau)=Pi(y,s_n+tau).                               (53.10)
```

L'équation (53.1), le drift et les constantes sont inchangés. Les estimations
locales du cycle 0045, appliquées aux translations d'une même solution
suitable, donnent sur chaque cylindre compact

```text
Z_n borne dans L-infinity_tau L2_y inter L2_tau H1_y,
Z_n -> U fortement dans L3_loc,
Pi_n -> P dans la decomposition pression proche/harmonique. (53.11)
```

L'extraction est diagonale en rayon et en fenêtre. Aucune compacité globale
ni convergence forte faible-`L3` n'est revendiquée.

Fixons `R` et une fonction temporelle test `eta` supportée dans `(-1,0)`.
Pour `n>=R`, (53.6)--(53.9) donnent

```text
|integral_(-1)^0 <partial_tau Z_n,phi>eta(tau)dtau|
 <=||eta||_infinity ||phi||_(Y_R) D_R(s_n)
 <=||eta||_infinity ||phi||_(Y_R)/n.                    (53.12)
```

Le passage à la limite montre `partial_tau U=0` dans les distributions sur
`R3 x (-1,0)`. Il existe donc un champ spatial, encore noté `U(y)`, tel que

```text
Z_n -> U(y) fortement dans L3_loc(R3 x (-1,0)).          (53.13)
```

## Équation stationnaire et pression

La convergence forte (53.13) identifie `Z_n tensor Z_n`. Contre les tests
solénoïdaux compacts, la pression disparaît et la limite satisfait

```text
-Delta U+div(U tensor U)+kappa(U+y dot nabla U)+nabla P=0,
div U=0                                                   (53.14)
```

au sens faible. La décomposition globale de Riesz fixe ensuite `P` modulo
une constante. Les bornes d'énergie locales de (53.11), combinées à
l'indépendance temporelle, donnent

```text
U in W^(1,2)_loc(R3).                                    (53.15)
```

La borne uniforme (53.2) passe faible-étoile; l'identification par la
convergence locale donne

```text
U in L^(3,infinity)(R3), ||U||_(3,infinity)<=M.          (53.16)
```

L'équation (53.14) est exactement l'équation stationnaire de Leray avec
paramètre positif `kappa`. Pour rejoindre la normalisation publiée à
coefficient `1/2`, posons

```text
lambda=sqrt(2kappa),
U(y)=lambda V(lambda y),
P(y)=lambda^2 Q(lambda y).                              (53.17a)
```

Cette dilatation préserve `L^(3,infinity)`, `W1,2_loc` et la non-nullité.
Le claim publié `NS-BACKWARD-SELFSIMILAR-WEAK-L3-LIOUVILLE`, via
Guevara--Phuc, impose donc

```text
V=0, donc U=0.                                            (53.17)
```

## Capture et contradiction

Appliquons (53.3) à `J=[s_n-1,s_n]`. La forte convergence `L3` sur
`B_1 x (-1,0)` donne

```text
integral_(B_1)|U(y)|^3dy
 =lim_n integral_(-1)^0 integral_(B_1)|Z_n|^3 dy dtau
 >=gamma^3.                                               (53.18)
```

Ainsi `U` n'est pas nul, en contradiction avec (53.17). L'hypothèse (53.8)
est fausse pour au moins un rayon, ce qui donne (53.7).

## Loi d'échelle et constantes

L'équation renormalisée est autonome : une translation `s->s+s_0` conserve
`kappa`, `M`, la durée unitaire et la forme de `D_R`. Dans les variables
physiques, cette translation correspond à une dilatation parabolique; aucun
indice dyadique absolu n'est figé avant le zoom.

Les constantes locales de Caccioppoli et de compacité dépendent de `R`,
`M`, `kappa` et de la marge temporelle du cylindre. Le raisonnement ne les
prétend pas uniformes quand `R->infinity`. La diagonalisation utilise
précisément un rayon croissant avant de conclure l'existence d'un seul
`R_*`. Il n'y a ni coefficient de Gronwall global, ni constante de
troncature envoyée silencieusement à l'infini.

## Passe contradictoire

1. **Endpoint du test.** Remplacer `L^(3,1)` par `L3` perd la dualité avec
   la pression et le stress faible-`L^(3/2)`.
2. **Fenêtre contre tranche.** `partial_s Z(s_n)->0` à des temps isolés ne
   suffit pas; (53.5) porte sur une fenêtre entière.
3. **Un seul compact.** `D_R(s_n)->0` pour un rayon fixé ne produit qu'une
   stationnarité locale et ne permet pas le Liouville global.
4. **Compacité forte.** Une convergence faible ne passe ni le produit
   quadratique ni la masse cubique de capture.
5. **Pression.** La jauge de Riesz et la décomposition proche/harmonique sont
   conservées; aucune pression locale arbitraire n'est supprimée.
6. **Capture.** Sans (53.3), le profil stationnaire nul serait compatible
   avec l'échappement spatial ou la concentration.
7. **Récurrence.** Un retour, même exact, n'implique pas un petit générateur;
   une orbite périodique non stationnaire est l'obstruction élémentaire.
8. **Coefficient du drift.** `kappa` reste strictement positif et fixe. Le
   laisser tendre vers zéro conduirait à une équation stationnaire différente.
9. **Notion de solution.** Le résultat porte sur la limite renormalisée
   suitable locale du pipeline Type I, pas sur toute solution faible.
10. **Clay.** (53.7) ne réfute que l'asymptotique stationnaire de cette
    branche; il ne contrôle pas DSS, orbites apériodiques, Type II ou le flux
    infrarouge du cycle 0052.

## Résultat et pivot

Le résultat positif du cycle est l'exclusion quantitative

```text
capture Type I persistante + faible-L3 + suitability
  -/-> generateur renormalise localement evanescent au passe.       (53.19)
```

Le verrou BSS exact est donc fermé dans la branche capturée : toute
sous-suite globalement asymptotiquement stationnaire conduirait à un profil
interdit. Le résultat négatif associé est

```text
recurrence ou precompacite abstraite
  -/-> petit generateur sur des fenetres.                           (53.20)
```

Le verrou est raffiné en

```text
GAP-TYPE-I-RENORMALIZED-GENERATOR-TO-SIGNED-FLUX.          (53.21)
```

La prochaine expérience décisive doit relier la minoration (53.7) à la
densité signée `Phi_a` du cycle 0052 : déterminer si un générateur qui reste
non nul force une circulation inter-échelle détectable, ou peut rester
entièrement tangent à une orbite récurrente sans gain infrarouge.
