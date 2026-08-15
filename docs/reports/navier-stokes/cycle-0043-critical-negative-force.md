# Cycle 0043 — fermeture du commutateur dans un espace négatif critique

Date : 2026-08-15

Statut : `AI_INTERNAL_DERIVATION`; aucun résultat Clay.

## Décision adaptative

| Action | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| exploiter l'ordre pseudodifférentiel de Bogovskii dans `L1+div L^(3/2,infinity)` | 4 | 4 | 5 | 5 | **18** |
| utiliser la croissance haute fréquence pour réfuter toute borne | 3 | 5 | 5 | 2 | 15 |
| remplacer la coupure compacte par la projection de Leray globale | 3 | 4 | 5 | 3 | 15 |

La première action est sélectionnée. La deuxième confond une norme positive
avec la norme négative réellement invariante; la troisième perd l'égalité au
champ original dans le core.

## Cadre exact

On conserve Navier–Stokes incompressible tridimensionnel non forcé, viscosité
un, sur `R3`, et les notations du cycle 0042. Dans les variables normalisées,

```text
U(y,sigma)=R u(x_*+Ry,t),
P(y,sigma)=R^2p(x_*+Ry,t),
d sigma/dt=R^-2,
kappa=-RR'.
```

Pour la branche Type I,

```text
sup_sigma ||U(sigma)||_(L^(3,infinity)(R3)) <= M,
kappa=2/S_w^*(C_M M).
```

La pression est fixée dans la jauge de Riesz

```text
P=R_iR_j(U_iU_j),
```

de sorte que

```text
K_(3/2)(P)<=C_CZ M^2.
```

Toutes les identités sont d'abord établies pour `U,P` lisses. Leur forme
distributionnelle utilise ensuite les prolongements bornés explicités
ci-dessous.

## Choix fixé de l'inverse de divergence

Soit `A={1<|y|<2}`. On choisit `delta>0` et
`chi in C_c^infinity(B_(2-delta))` égale à un sur `B_(1+delta)`, puis
`a=nabla chi`; ainsi `supp a` est compactement contenu dans `A`. On fixe une
fois pour toutes une droite inverse
support-preserving

```text
B_A : distributions scalaires de moyenne nulle supportées dans A
      -> champs vectoriels supportés dans A,
div B_A g=g.
```

On choisit la réalisation obtenue par les opérateurs régularisés de
Bogovskii–de Rham de Costabel–McIntosh, avec correction du sous-espace
cohomologique de degré supérieur. Sur une couronne lipschitzienne connexe, la
seule obstruction compacte en degré trois est l'intégrale; elle disparaît
pour les données de moyenne nulle. L'opérateur exact ainsi obtenu est un
pseudodifférentiel proprement supporté d'ordre `-1`, à un opérateur lissant
près. Il vérifie, pour tout `s in R`, les bornes de gain d'une dérivée dans
les espaces de Sobolev utilisés ici.

Plus précisément, sous l'identification standard entre champs et formes, leur
opérateur compactement supporté vérifie au degré supérieur

```text
d T_3 g=g-L_3g,
T_3 in Psi^(-1),
L_3 de rang fini et lissant.
```

Sur le sous-espace `integral_A g=0`, `L_3g` a encore intégrale nulle. On fixe
une droite inverse lisse `S` de `d` sur l'image finie correspondante et l'on
prend

```text
B_A=T_3+S L_3.                                  (43.0)
```

Alors `dB_Ag=g`; la correction `S L_3` est lissante et de rang fini, donc
(43.0) reste d'ordre `-1` et préserve le support dans la couronne.

Ce choix est plus précis qu'un symbole abstrait `B`: les constantes suivantes
dépendent uniquement de `A`, du noyau régularisant fixé et de `chi`. Elles ne
dépendent ni de `R`, ni du temps, ni de `U`.

Posons

```text
T=B_A M_a,
Q=M_chi-T,
```

où `M_a U=a dot U`. Si `div U=0`, alors

```text
integral_A a dot U=integral_R3 div(chi U)=0,
```

donc `Q` est licite et `div QU=0`.

## Espace critique de force

On utilise

```text
X(A)=L1(A)+div L^(3/2,infinity)(A),

||F||_X=inf_(F=f+div G)
  [||f||_L1+||G||_(L^(3/2,infinity))].          (43.1)
```

Si `f_R(x)=R^-3f((x-x_*)/R)` et
`G_R(x)=R^-2G((x-x_*)/R)`, alors

```text
||f_R||_L1=||f||_L1,
||G_R||_(L^(3/2,infinity))=||G||_(L^(3/2,infinity)).
```

L'espace (43.1) est donc exactement invariant pour une force physique. Il ne
doit pas être remplacé par `L1` terme à terme.

## Lemme actif : commutateur mobile

Définissons `D=1+y dot nabla` et

```text
K_kappa(U)=-[Delta,Q]U+kappa[D,Q]U.             (43.2)
```

Comme `T` est d'ordre `-1`, le calcul pseudodifférentiel donne

```text
[Delta,T] in Psi^0,
[D,T]     in Psi^(-1).                          (43.3)
```

Les coefficients de `D` sont bornés sur le support fixe de `T`. Par ailleurs,

```text
[Delta,M_chi]U
 =2(a dot nabla)U+(Delta chi)U
 =div(2U tensor a)-(Delta chi)U,

[D,M_chi]U=(y dot a)U.                          (43.4)
```

Les signes de (43.2)–(43.4) donnent l'identité exacte

```text
K_kappa(U)=f_kappa(U)+div G(U),                 (43.5)

G(U)=-2U tensor a,

f_kappa(U)=
  [(Delta chi)+kappa(y dot a)]U
  +[Delta,T]U-kappa[D,T]U.                     (43.6)
```

Notons

```text
C_DeltaT=||[Delta,T]||_(L2->L2),
C_DT=||[D,T]||_(L2->L2),
m_A=|A|.
```

L'inclusion faible-`L3` sur un ensemble de mesure finie donne

```text
||U||_(L2(A))<=sqrt(3)m_A^(1/6)K_3(U),
K_(3/2)(U 1_A)<=m_A^(1/3)K_3(U).                (43.7)
```

Il résulte de (43.5)–(43.7) que

```text
||K_kappa(U)||_X
 <=C_K(A,chi,B_A,kappa) K_3(U),                 (43.8)

C_K=
  2||a||_infinity m_A^(1/3)
  +sqrt(3)m_A^(2/3)
   [||Delta chi||_infinity
    +|kappa|||y dot a||_infinity
    +C_DeltaT+|kappa|C_DT].                     (43.9)
```

La constante est uniforme en temps et sous homothétie. Elle dépend de `M`
dans l'application Type I par `kappa=2/S_w^*(C_MM)`; aucune uniformité Type II
n'est affirmée.

## Force projetée complète

Le cycle 0042 donne

```text
F_sol=P_L div(Z tensor Z)-QH+K_kappa(U),         (43.10)

Z=QU,
H=div S,
S=U tensor U+P I.
```

Le choix de pression rend `div H=0`. La projection de Leray commute aux
dérivées constantes; ainsi

```text
P_L div(Z tensor Z)=div G_NL,
K_(3/2)(G_NL)<=C_L K_3(Z)^2<=C M^2.             (43.11)
```

Pour `QH`, on ne sépare pas illégalement convection et pression. Posons

```text
r=a dot H
 =partial_j(a_i S_ij)-(partial_j a_i)S_ij.      (43.12)
```

Puisque `div H=0`, `r` a moyenne nulle. Sur la couronne fixe,
`S in L^(3/2,infinity)` implique `S in L^(4/3)`. Le prolongement négatif

```text
B_A:W^(-1,4/3)_0(A)->L^(4/3)(A)                 (43.13)
```

est donc suffisant; aucun endpoint Lorentz de Bogovskii n'est requis. Plus
précisément,

```text
||S||_(L^(4/3)(A))
 <=3^(3/2)m_A^(1/12)K_(3/2)(S),                (43.13a)

||B_A r||_(L^(4/3))
 <=C_(B,-1,4/3)
   [||a||_infinity+||nabla a||_infinity]
   ||S||_(L^(4/3)(A)).                         (43.13b)
```

Le facteur `3^(3/2)` vient de l'intégration exacte de la distribution
faible-`L^(3/2)` jusqu'à l'exposant `4/3`; l'inclusion finale vers `L1`
coûte `m_A^(1/4)`. Enfin,

Dans (43.13), la notation est celle de Geißert–Heck–Hieber :
`W_0^(-1,p)(A)=(W^(1,p')(A))'`, espace plus petit que le dual de
`W_0^(1,p')`. La donnée (43.12) appartient bien à ce sous-espace car ses
coefficients sont supportés strictement à l'intérieur de `A`; sa moyenne est
nulle. Cette compatibilité de bord ne doit pas être omise.

```text
-QH=-div(chi S)+S a+B_A r.                      (43.14)
```

Le premier terme de (43.14) est la divergence d'un stress faible-
`L^(3/2)`; les deux autres appartiennent à `L1` par support fini et (43.13).
Avec (43.8) et (43.11), on obtient

```text
||F_sol(sigma)||_X
 <=C_(A,chi,B_A,CZ)[M^2+(1+|kappa|)M].          (43.15)
```

Cette borne ferme `GAP-TYPE-I-MOVING-COMMUTATOR-BOUND` pour la réalisation
fixée. Elle ne donne aucune petitesse : le membre droit de (43.15) peut être
grand et la force ne tend pas vers zéro.

## Test adverse haute fréquence

Pour

```text
U_N=epsilon phi(r,z)sin(Nz)e_theta,
```

avec `phi` axisymétrique supportée dans la couronne hors de l'axe, on a

```text
div U_N=0,
a dot U_N=0,
T U_N=0.
```

La norme positive de `[Delta,chi]U_N` croît comme `epsilon N` sur une fraction
fixe du support. Mais (43.5) se réduit exactement à

```text
K_kappa(U_N)
=div(-2U_N tensor a)
 +[(Delta chi)+kappa(y dot a)]U_N.              (43.16)
```

Les deux budgets de (43.16) sont `O(epsilon)` indépendamment de `N`. La haute
fréquence réfute donc une borne `L1` terme à terme, mais **ne réfute pas** la
borne négative (43.8). Chercher seulement le coefficient `O(N)` en norme
positive était un test mal adapté au verrou réel.

Le témoin exact séparé rend cette frontière quantitative. Pour `N>=16`, il
certifie

```text
||[Delta,chi]U_N||_L2
 >=epsilon(5N/32-8/15),

||f_(0,N)||_L1<=99epsilon/140,
||G_(0,N)||_(L^(3/2,infinity))<=8epsilon/5.      (43.17)
```

Le même audit construit un champ poloidal divergence-free pour lequel
`a dot U=3/5` en un point : le correcteur est réellement activé hors de la
sous-classe pure-swirl, mais sa valeur ne devient quantitative qu'après le
choix de (43.0).

## Passe contradictoire

1. **Exactitude de Bogovskii.** Un opérateur homotopique avec reste lissant
   n'est pas automatiquement une droite inverse. La composante cohomologique
   de degré trois doit être retirée; la moyenne nulle est indispensable.
2. **Ordre du commutateur.** `Delta T` et `T Delta` sont séparément d'ordre
   un. Seule leur différence est d'ordre zéro. Les estimer séparément perd une
   dérivée. La passe formelle séparée retrouve exactement la marche manquante
   `B:W^(-2,p)->W^(-1,p)`; elle est fournie ici par l'ordre `-1` de la
   réalisation (43.0), pas par le seul caractère support-lisse.
3. **Norme positive.** La croissance `O(N)` survit dans la divergence du
   stress. Elle ne fait pas croître la norme (43.1).
4. **Endpoint.** (43.13) utilise `p=4/3`, pas une extension non démontrée à
   `W^(-1,(3/2,infinity))`.
5. **Pression.** La jauge globale de Riesz est fixée avant de former `S`.
   Changer la jauge sans déplacer simultanément le gradient modifierait les
   termes locaux.
6. **Projection.** Le stress de (43.11) n'est pas compactement supporté à
   cause des transformées de Riesz. La borne est globale, la localité ne l'est
   pas.
7. **Temps.** (43.15) est une borne `L^infinity_sigma X`; elle n'apporte ni
   équicontinuité temporelle ni compacité forte.
8. **Faible-Lorentz.** `L^(3/2,infinity)` et `L1` ne sont pas réflexifs. Une
   suite bornée ne fournit pas automatiquement la convergence nécessaire des
   produits quadratiques.
9. **Force.** La borne critique n'élimine pas `F_sol`; une limite éventuelle
   reste forcée.
10. **Clay.** Aucune estimation de (43.15) ne contrôle la norme critique de la
    solution originale depuis l'énergie Clay.

## Résultat et pivot

Le premier verrou du cycle 0042 est fermé conditionnellement et à constante
suivie : le commutateur mobile ainsi que la force projetée complète sont
uniformément bornés dans l'espace critique négatif `X` sous la borne Type I
faible-`L3`.

Le progrès est analytique mais limité. Il ne transforme pas le champ localisé
en solution non forcée et ne fournit pas le passage au continuum. Le verrou
suivant est scindé en

```text
GAP-TYPE-I-FORCE-COMPACTNESS
  : extraire une limite compatible avec les produits et la pression
    depuis une borne non réflexive dans X;

GAP-TYPE-I-FORCED-RIGIDITY
  : éliminer ou classifier la force critique limite.
```

La prochaine expérience décisive est une localisation à facteur externe `L`:
mettre le core dans `B_1`, la transition dans `B_L\B_(L/2)`, suivre la
croissance des constantes de Bogovskii et tester si, pour tout compact fixé,
la force locale s'échappe vers l'infini lorsque `L->infinity` sans détruire la
capture Type I.
