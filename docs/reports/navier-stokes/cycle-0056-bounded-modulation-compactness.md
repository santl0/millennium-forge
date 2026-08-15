# Cycle 0056 — compacité d'une modulation rotationnelle bornée

Date : 2026-08-15.

Statut : `AI_INTERNAL_DERIVATION`; aucune conclusion Clay.

## Décision adaptative

Le verrou relu est
`GAP-TYPE-I-APPROXIMATE-ROTATION-MODULATION-COMPACTNESS`. Les actions sont
notées avant la preuve :

| action | nouveauté | tractabilité | falsifiabilité | levier | total |
|---|---:|---:|---:|---:|---:|
| compacité d'un défaut modulé avec vitesses bornées | 4 | 5 | 5 | 5 | **19** |
| construire une coordonnée locale de phase par un test transverse | 4 | 4 | 5 | 4 | 17 |
| extraire une moyenne axisymétrique lorsque les vitesses divergent | 5 | 2 | 4 | 5 | 16 |

La première action est sélectionnée. Le lemme actif est unique : passer à la
limite dans

```text
partial_s Z_n-beta_n mathcal R Z_n -> 0                 (56.1)
```

lorsque `beta_n` reste borné, reconstruire l'orbite de rotation de la limite,
puis utiliser l'autonomie de Navier--Stokes pour obtenir une RSS exacte ou
un profil stationnaire.

## Cadre exact

Fixons `kappa>0`, un intervalle borné ouvert `I` et l'opérateur renormalisé

```text
F_kappa(Z)=-Delta Z+P div(Z tensor Z)+kappa D Z,
D Z=(1+y dot nabla)Z.                                    (56.2)
```

Les champs `Z_n` sont des solutions faibles adaptées locales de

```text
partial_s Z_n+F_kappa(Z_n)=0,
div Z_n=0                                                (56.3)
```

sur `R3 x I`, sans frontière, viscosité un et force nulle. La pression est
soit suivie dans le paquet compact suitable, soit fixée globalement par
Riesz. Les hypothèses compactes sont :

```text
sup_n ||Z_n||_(L-infinity(I;L^(3,infinity)(R3))) <= M,   (56.4)

Z_n -> Z fortement dans L3(K) pour tout
K compact de R3 x I,                                    (56.5)

pour tout J compactement inclus dans I et R fini,
sup_n ||Z_n||_(L-infinity(J;L2(B_R)))
+sup_n ||nabla Z_n||_(L2(J x B_R))
+sup_n ||Pi_n||_(L^(3/2)(J x B_R)) < infinity,
avec les convergences locales du paquet suitable du cycle 0045. (56.6)
```

On fixe l'action autour de l'axe `e_3` passant par l'origine similaire,

```text
(Q_theta U)(y)=R_theta U(R_(-theta)y),
mathcal R U=J U-(J y dot nabla)U.                        (56.7)
```

Enfin,

```text
beta_n in L-infinity(I),
||beta_n||_infinity<=B,                                  (56.8)

r_n:=partial_s Z_n-beta_n mathcal R Z_n ->0
dans D'(R3 x I).                                         (56.9)
```

Le défaut (56.9) est une hypothèse dynamique forte. Il ne découle pas de la
seule minoration `D_R` du cycle 0053 ni du flux du cycle 0054.

## Extraction de la vitesse

Par Banach--Alaoglu et séparabilité de `L1(I)`, après sous-suite,

```text
beta_n weak-* -> beta dans L-infinity(I),
||beta||_infinity<=B.                                    (56.10)
```

Il n'est pas nécessaire que les `beta_n` convergent ponctuellement ou en
mesure. Les oscillations rapides peuvent subsister au niveau de la suite;
seule leur limite faible-étoile entre dans l'équation limite.

Sur un intervalle similaire non borné, la même conclusion vaut sous une
borne `L-infinity_loc`, par exhaustion et extraction diagonale. Les phases
et vitesses obtenues coïncident sur les recouvrements; dans la branche
`mathcal R U!=0`, la classification ci-dessous impose une même constante
`alpha` sur tout intervalle connexe.

## Le produit faible-étoile × fort

Pour un test vectoriel lisse compact `phi(s,y)`, l'adjoint spatial du
générateur est

```text
mathcal R^* phi=-J phi+(J y dot nabla)phi.               (56.11)
```

En effet `div(Jy)=0` et `J^T=-J`. Posons

```text
h_n(s)=<mathcal R Z_n(s),phi(s)>_y
      =<Z_n(s),mathcal R^*phi(s)>_y.                      (56.12)
```

La convergence forte locale (56.5) donne

```text
h_n -> h:=<mathcal R Z,phi> fortement dans L1(I).         (56.13)
```

Alors

```text
integral beta_n h_n-integral beta h
=integral beta_n(h_n-h)+integral (beta_n-beta)h ->0.      (56.14)
```

Le premier terme tend vers zéro par la borne `B`; le second par (56.10).
Donc

```text
beta_n mathcal R Z_n -> beta mathcal R Z
dans D'(R3 x I).                                         (56.15)
```

Cette étape est linéaire en `Z_n`. La convergence forte `L3_loc` est plus
forte que nécessaire pour (56.15), mais elle est simultanément celle qui
ferme le stress `Z_n tensor Z_n` dans (56.3).

## Équation de transport rotationnel de la limite

En passant à la limite dans (56.9),

```text
partial_s Z=beta(s)mathcal R Z                           (56.16)
```

dans les distributions. Définissons, pour un point `s_0 in I`,

```text
theta(s)=integral_(s_0)^s beta(sigma)dsigma.              (56.17)
```

Ainsi `theta in W^(1,infinity)(I)` et `theta'=beta` presque partout.
Considérons dans les distributions

```text
W(s)=Q_(-theta(s))Z(s).                                  (56.18)
```

La règle de chaîne faible, testée contre les rotations de fonctions lisses,
donne

```text
partial_s W
=Q_(-theta)[partial_s Z-beta mathcal R Z]=0.             (56.19)
```

Il existe donc une distribution spatiale `U`, indépendante de `s`, telle que

```text
Z(s)=Q_(theta(s))U                                       (56.20)
```

presque partout. Le relèvement de phase est construit par (56.17); aucune
appartenance préalable de `Z(s)` à une orbite n'est supposée.

## Passage de Navier--Stokes à la limite

La forte convergence `L3_loc` donne

```text
Z_n tensor Z_n -> Z tensor Z fortement dans L^(3/2)_loc. (56.21)
```

Les termes linéaires passent distributionnellement. Testée contre les champs
solénoïdaux compacts, l'équation limite ne requiert aucune localisation de la
projection de Leray. Le ledger uniforme (56.6) transmet en plus la pression
locale et l'inégalité d'énergie locale; `Z` reste faible adaptée locale. Le
seul fait que chaque `Z_n` soit suitable, sans constantes uniformes en `n`,
ne suffit pas à cette conclusion.

La borne faible-`L3` passe dans la limite au sens faible-étoile et la jauge
globale de Riesz est reconstruite si les hypothèses de queue du paquet sont
conservées. Ainsi

```text
partial_s Z+F_kappa(Z)=0.                                (56.22)
```

## Classification de la limite

Les équations (56.20) et (56.22) satisfont exactement les prémisses du cycle
0055. Deux branches subsistent.

### Branche stationnaire

Si `mathcal R U=0`, alors `Q_theta U=U`, `Z(s)=U` et

```text
F_kappa(U)=0.                                             (56.23)
```

La valeur de `beta` devient une jauge non identifiable. Sous suitability,
`U in W1,2_loc`; sous la borne faible-`L3`, la normalisation de `kappa` et le
théorème publié de Guevara--Phuc donnent `U=0`.

### Branche RSS

Si `mathcal R U!=0`, l'autonomie et l'équivariance imposent

```text
beta(s)=alpha presque partout,
theta(s)=alpha(s-s_0),                                   (56.24)

F_kappa(U)+alpha mathcal R U=0.                          (56.25)
```

La limite est une RSS exacte, même si les vitesses `beta_n` oscillaient et
ne convergeaient que faible-étoile.

## Capture et exclusion de la branche nulle

Supposons que, pour un cylindre compact `J x B_1` avec `J subset I`,

```text
integral_(J x B1)|Z_n|^3 >= |J| gamma^3.                 (56.26)
```

La forte convergence `L3` transmet (56.26) à `Z`. Si la branche stationnaire
était présente, Guevara--Phuc donnerait `Z=0`, en contradiction avec la
capture. Dans la branche RSS, `alpha=0` donnerait aussi une trajectoire
stationnaire et la même contradiction. Par conséquent, sous le paquet
capturé complet,

```text
mathcal R U!=0 et alpha!=0.                              (56.27)
```

Le résultat ne rend pas `U` trivial : la rigidité RSS tournante faible-`L3`
reste manquante.

## Loi d'échelle et constantes

Le temps similaire, `beta_n` et `alpha` sont sans dimension. Les rotations
préservent `L^(3,infinity)`, les boules centrées et les normes locales. La
constante du passage (56.14) est exactement la borne `B`; aucune division par
`||mathcal R U||` n'est utilisée. La classification traite donc sans
instabilité le cas où le générateur limite s'annule : elle bascule vers la
branche stationnaire.

En revanche, si `B` dépend de `n`, aucune compacité faible-étoile n'est
disponible et `beta_n mathcal R Z_n` peut rester d'ordre un alors que
`mathcal R Z_n->0`. La borne uniforme de vitesse est le coefficient critique
de ce cycle.

## Passe contradictoire

1. **Produit de deux limites faibles.** Faible-étoile de `beta_n` et faible
   de `Z_n` ne suffisent pas; des oscillations corrélées ont un produit moyen
   non nul.
2. **Borne de vitesse.** Sans (56.8), Banach--Alaoglu et le premier terme de
   (56.14) échouent.
3. **Stress.** Le passage du défaut est linéaire, mais l'équation NS demande
   la forte `L3_loc` pour `Z_n tensor Z_n`.
4. **Pression.** Les tests solénoïdaux ferment l'équation; la suitability et
   la pression globale exigent encore le paquet compact distinct.
5. **Temps.** `beta_n` est une fonction de `s` seulement. Une modulation
   spatiale `beta_n(s,y)` ne définit pas l'action d'un groupe global.
6. **Axe.** L'axe et le centre sont fixes. Une rotation mobile ajoute des
   générateurs de translation ou d'inclinaison.
7. **Phase.** Les phases `theta_n` ne sont jamais supposées converger. La
   phase limite est reconstruite depuis `beta` après passage au produit.
8. **Stabilisateur.** Lorsque `mathcal R U=0`, `beta` n'est pas déterminé;
   conclure sa constance serait faux, mais le champ est stationnaire.
9. **Capture.** Elle doit être sur un même cylindre compact où la convergence
   est forte; une masse fuyant à l'infini ne passe pas.
10. **Liouville.** Guevara--Phuc ne s'applique qu'à la branche stationnaire,
    jamais directement à (56.25) avec `alpha!=0`.
11. **Prépublication.** Pineau--Vicol v2 demande une borne Type I ponctuelle
    et ne couvre pas toutes les rotations; faible-`L3` ne suffit pas.
12. **Clay.** Rien ne produit l'hypothèse (56.9) depuis une singularité
    arbitraire, et Type II n'est pas traité.

## Résultat et pivot

Le résultat positif est la fermeture conditionnelle

```text
forte L3_loc + beta_n borné + défaut modulé ->0
  => limite stationnaire ou RSS exacte;
capture persistante + Liouville stationnaire
  => limite RSS non stationnaire.                         (56.28)
```

Le résultat négatif est

```text
faible × faible ou vitesse non bornée
  -/-> passage du produit modulé.                         (56.29)
```

Le verrou devient

```text
GAP-TYPE-I-UNBOUNDED-ROTATION-MODULATION-OR-RSS-RIGIDITY. (56.30)
```

La prochaine expérience décisive doit séparer deux sorties : soit démontrer
qu'une modulation sélectionnée par le pipeline possède une borne uniforme de
vitesse, soit analyser `|beta_n|->infinity` par moyenne angulaire et montrer
que toute limite devient axisymétrique. Même après cette fermeture, il
restera à annuler les profils RSS faible-`L3` de vitesse intermédiaire.
