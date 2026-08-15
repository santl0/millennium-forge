# Cycle 0063 — sortie exacte d'un cône modal sous le flot

Date : 2026-08-15.

Statut : **AI_INTERNAL_DERIVATION + COMPUTATION_ONLY**. Le cycle construit
une donnée initiale de Schwartz pour laquelle une face régulière d'un
orthant de numérateurs modaux est franchie vers l'extérieur par le flot
Navier--Stokes local. Il ne construit ni blow-up, ni solution ancienne.

## Décision adaptative

Le verrou relu est
`GAP-TYPE-I-DYNAMIC-MODAL-CONE-OR-INTRINSIC-HAAR-DEFECT`.

| action candidate | nouveauté | tractabilité | falsifiabilité | levier | total |
|---|---:|---:|---:|---:|---:|
| dériver `C'_m` et tester une face du cône | 5 | 5 | 5 | 5 | **20** |
| construire directement un défaut de Haar critique | 4 | 3 | 4 | 5 | 16 |
| attaquer la rigidité RSS à vitesse intermédiaire | 3 | 2 | 3 | 5 | 13 |

La première action est sélectionnée. Le lemme candidat minimal est :

> **Invariance modale locale.** Pour un ensemble fini de modes actifs, la
> région `K_M^+={Z:C_m(Z)>=0 pour tout m dans M}` est positivement invariante
> sous le semiflot Navier--Stokes fort.

Une face régulière avec dérivée sortante suffit à réfuter ce lemme. Le cycle
construit une telle face pour `M={1,2,3}`.

## Équation, espace et observable

Le test choisit `kappa=0`; il porte donc sur Navier--Stokes standard,
incompressible, 3D, non forcé, viscosité un, sur `R3` sans frontière :

```text
partial_t Z=F(Z)=Delta Z-P div(Z tensor Z),
div Z=0.
```

Pour l'action covariante SO(2) autour de `e3`, ses projecteurs isotypiques
réels `P_m` et son générateur `mathcal R`, on pose

```text
Z_m=P_mZ,
C_m(Z)=<P_mF(Z),mathcal RZ_m>_L2.
```

La donnée construite est divergence-free et de Schwartz. La théorie mild
forte locale sur `R3` fournit donc une solution classique unique sur un
intervalle positif. Les calculs de dérivée sont faits à `t=0`, où toutes les
quantités requises sont régulières et intégrables. La projection de Leray
peut produire des queues non locales; le champ vectoriel n'est pas déclaré
de Schwartz sans vérification.

## Dérivée exacte et critère de tangence

La différentielle du champ vectoriel est

```text
DF(Z)[H]
 =Delta H-P div(H tensor Z+Z tensor H).
```

Le long d'une solution, avec `U=F(Z)`, la règle du produit donne

```text
C'_m
 =<P_mDF(Z)[U],mathcal RZ_m>
  +<P_mU,mathcal RP_mU>.
```

Le second terme est présent avant simplification, puis s'annule par
antisymétrie. Ainsi

```text
C'_m=<P_mDF(Z)[F(Z)],mathcal RZ_m>.
```

La pression linéarisée extérieure disparaît seulement dans cet appariement
global avec la tangente solénoïdale. La pression déjà contenue dans `F(Z)`
reste dans les termes convectifs linéarisés et doit être calculée.

Pour

```text
K_M^+={Z:C_m(Z)>=0 pour tout m dans M},
```

le critère intrinsèque de Nagumo est
`F(Z) in T_(K_M^+)(Z)` sur tout le bord. À une face régulière définie par
`C_j=0`, une condition nécessaire est `C'_j>=0`. Une donnée avec
`C'_j<0` quitte donc immédiatement la région. Cette implication locale ne
requiert pas la suffisance globale du critère de Nagumo.

## Donnée de frontière

Avec `r2=x^2+y^2+z^2`, posons

```text
h_1c=x,                    h_1s=y,
h_2c=x^2-y^2,              h_2s=2xy,
h_3c=x^3-3xy^2,
Z[h]=curl(0,0,h exp(-r2)).
```

La donnée est

```text
Z_1=Z[-h_1c-h_1s],
Z_2=Z[-h_2c-h_2s],
Z_3=Z[-h_3c],
Z=Z_1+Z_2+Z_3.
```

Chaque bloc est un isotype réel non nul et `div Z=0` exactement. Le calcul
des moments gaussiens donne

```text
(C_1,C_2,C_3)
 =(8/9,16/9,0)*(pi/3)^(3/2).
```

La donnée appartient donc à une face de `K_{1,2,3}^+`, avec les deux autres
contraintes strictement intérieures. Ce n'est ni l'apex ni un Gram nul : le
mode `m=3` et sa tangente sont non nuls.

La première famille à seulement deux modes `m=1,2` est conservée comme
échec : 576 orientations exactes vérifient `C_2=2C_1`; sa frontière de signe
est seulement l'apex et ne fournit pas la face régulière recherchée.

## Calcul non local de `C'_3`

Écrivons

```text
N=(Z dot nabla)Z,
A=Delta Z-N,
F=A-nabla p,
-Delta p=S=div N,
w=mathcal RZ_3.
```

La partie locale est calculée directement comme

```text
<Delta A-(A dot nabla)Z-(Z dot nabla)A,w>.
```

Elle se décompose par taux gaussien en

```text
rate 2 : 0,
rate 3 : 0,
rate 4 : -675/32,
```

donc vaut `-(675/256)*pi^(3/2)` après réinsertion du facteur
`(pi/4)^(3/2)`.

La partie de pression interne vaut `<p,Q>`, avec

```text
Q
 =-partial_j[(partial_j Z_i)w_i]
  +partial_i[Z_j(partial_j w_i)].
```

Comme `S` et `Q` sont des polynômes fois `exp(-2r2)`, Parseval donne

```text
<p,Q>=<(-Delta)^(-1)S,Q>
 =(2pi)^(-3) integral hat(S) conjugate(hat(Q))/|xi|^2 dxi.
```

Les transformées sont des polynômes complexes à coefficients rationnels
fois `exp(-|xi|^2/8)`. Pour un monôme pair, le moment utilisé est

```text
integral xi_1^(2a)xi_2^(2b)xi_3^(2c)/|xi|^2
         *exp(-|xi|^2/4) dxi / pi^(3/2)
 =[(2a-1)!!(2b-1)!!(2c-1)!!]
   *2^(a+b+c+2)/(2(a+b+c)+1),
```

et les monômes impairs s'annulent. Le facteur de Parseval et des deux
gaussiennes est exactement `1/64`. Le résultat est

```text
<p,Q>=(575457/320320)*pi^(3/2).
```

La somme exacte est donc

```text
C'_3(0)
 =[-675/256+575457/320320]*pi^(3/2)
 =-(1076547/1281280)*pi^(3/2)
 <0.
```

Par continuité, pour tout temps positif assez petit,
`C_1(t)>0`, `C_2(t)>0` et `C_3(t)<0`. La région
`K_{1,2,3}^+` n'est pas positivement invariante sous le flot fort local.

## Passe adversariale du calcul

Une première séparation locale a écrit la convection linéarisée sous forme
de divergence après avoir remplacé `F` par `A-nabla p`. Cette étape était
illégitime : `A=Delta Z-N` n'est pas divergence-free séparément. Elle
donnait `-1035/32` pour le terme local et une pression compensatrice
différente. Le calcul a été rejeté, puis refait avec
`Delta A-B(A,Z)-B(Z,A)` et la formule de `Q` ci-dessus. Le total final est
resté le même, mais seules les valeurs corrigées `-675/32` et
`575457/320320` sont admises.

La normalisation de l'inverse du Laplacien est attaquée par des solutions
manufacturées `S=-Delta(phi)` : le certificat retrouve exactement
`<S,(-Delta)^(-1)Q>=<phi,Q>`, vérifie la symétrie de la forme et sa
positivité diagonale. Toutes les parties imaginaires de l'intégrale de
Fourier s'annulent exactement.

Une passe pseudo-spectrale indépendante, non utilisée comme preuve, donne
sur `[-8,8]^3`, `80^3` points :

```text
C_3=1.06e-14,
C'_3=-4.678565508144,
exact=-4.678576735768,
erreur absolue=1.12e-5,
||div F||_2=5.52e-12.
```

Ce contrôle flottant confirme le signe, mais le résultat certifié repose
sur l'arithmétique exacte.

## Échelle et portée

Pour `kappa=0` et `Z_lambda(y)=lambda Z(lambda y)`, `C_m` porte `lambda` et
`C'_m` porte `lambda^3`. Le signe de la sortie est donc invariant sous la
remise à l'échelle critique. Une multiplication d'amplitude n'est pas cette
dilatation; elle doit être suivie séparément.

Le résultat réfute l'invariance de l'orthant sur l'espace de phase fort
local. Il ne réfute pas :

- une propriété asymptotique spéciale d'un élément minimal de blow-up;
- une condition imposée seulement aux solutions anciennes Type I capturées;
- un cône différent faisant intervenir vorticité, fréquence ou temps moyen;
- une rigidité RSS à vitesse intermédiaire;
- un mécanisme Type II.

Nagumo est orienté vers le futur et ne construit pas une solution ancienne.
Une propriété sur un nombre fini de modes ne passe pas automatiquement à
tous les modes, ni à une limite faible suitable.

## Veille primaire

La veille indépendante ne trouve aucun théorème publiant l'invariance de
`C_m>=0` pour Navier--Stokes 3D complet. Les théorèmes de Nagumo et leurs
extensions aux semi-groupes exigent une condition tangentielle sur tout le
bord. Les régions spectrales validées de Zgliczyński portent sur NS 2D ou de
petites données 3D et sur des coordonnées de Fourier différentes. Les
sous-espaces hélicoïdaux de Mahalov--Titi--Leibovich et le système homochiral
de Biferale--Titi reposent sur une symétrie imposée ou une non-linéarité
décimée. Aucun ne fournit le cône des `C_m` du système 3D complet.

## Décision et pivot après trois stratégies

`FAIL-NS-0099` ferme l'invariance locale du cône modal. Les trois stratégies
réellement distinctes sur le verrou sont désormais :

1. robustesse de la phase sous changement de métrique, réfutée au cycle
   0061;
2. cohérence de signe du champ vectoriel instantané, réfutée au cycle 0062;
3. invariance dynamique de l'orthant modal, réfutée ici.

Conformément au protocole, la piste de phase modale est abandonnée. Le
nouveau verrou est
`GAP-TYPE-I-CRITICAL-WEIGHTED-HAAR-DEFECT-OR-RSS-INTERMEDIATE-RIGIDITY`.

La prochaine expérience décisive utilisera l'observable intrinsèque critique

```text
D_H(Z)=integral |(I-A)Z(y)|^2/|y| dy,
```

où `A` est la moyenne covariante de Haar autour de l'axe fixé. Cette quantité
est invariante sous l'échelle Clay. Il faut dériver son budget exact,
pression pondérée comprise, puis chercher deux champs de Schwartz donnant
des signes opposés. Un signe coercif survivant isolerait un lemme nouveau;
deux signes élimineraient la monotonie avant tout argument de compacité.
