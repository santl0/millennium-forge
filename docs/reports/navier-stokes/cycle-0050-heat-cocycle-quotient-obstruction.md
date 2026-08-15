# Cycle 0050 — cocycle calorique et obstruction quotient faible-`L3`

Date : 2026-08-15.

## Décision adaptative

Le verrou relu est `GAP-TYPE-I-BSS-ANCIENT-RIGIDITY`. Trois actions ont été
notées avant la dérivation :

| action | nouveauté | tractabilité | falsifiabilité | levier | total |
|---|---:|---:|---:|---:|---:|
| identifier le cocycle exact et son obstruction dans le quotient faible-`L3` modulo énergie | 4 | 5 | 5 | 5 | **19** |
| extraire une énergie BSS uniforme lorsque le temps de base tend vers `-infinity` | 3 | 2 | 5 | 5 | 15 |
| promouvoir directement toutes les traces vers `tilde L^(3,infinity)` | 3 | 2 | 4 | 4 | 13 |

La première action est sélectionnée. Le lemme actif est borné : comparer
exactement les scissions issues de deux temps de base, puis décider si leur
seule cohérence peut fournir une contrainte ancienne nouvelle.

## Cadre exact

Sur `R3 x (-infinity,0]`, sans frontière, force nulle et viscosité un, on
considère la solution ancienne conditionnelle des cycles 0047--0049 :

```text
partial_t v-Delta v+div(v tensor v)+nabla q=0,
div v=0,
q=R_iR_j(v_i v_j),
sup_(t<=0)||v(t)||_(L^(3,infinity))<=M.             (50.1)
```

La paire est faible adaptée locale. Le représentant faible-étoile temporel
est choisi de manière cohérente sur les bandes qui se recouvrent. Pour tout
`s<t<=0`, posons

```text
V_s(t)=S(t-s)v(s),
g_(s,t)=w_s(t)=v(t)-V_s(t).                       (50.2)
```

Les cycles 0048--0049 donnent, sur chaque bande finie,

```text
g_(s,.) in C([s,T];L2) inter L2([s,T];Hdot1),
g_(s,s)=0,
||g_(s,t)||_2<=C_D M²(t-s)^(1/4),                 (50.3)
```

ainsi que les inégalités énergétiques perturbées locale et globale. Aucune
constante de (50.3) n'est uniforme lorsque `t-s->infinity`.

## Identité exacte de cocycle

Soient `s<r<t`. Le semi-groupe et la trace au temps `r` donnent

```text
V_s(t)=S(t-r)V_s(r),
v(r)=V_s(r)+g_(s,r),
V_r(t)=S(t-r)v(r)
      =V_s(t)+S(t-r)g_(s,r).                     (50.4)
```

Par conséquent,

```text
g_(s,t)=g_(r,t)+S(t-r)g_(s,r).                   (50.5)
```

Cette identité ne requiert ni unicité à grande donnée, ni identification de
deux solutions construites séparément : toutes les scissions portent sur le
même champ distributionnel `v`. Pour quatre temps, l'associativité de (50.5)
est exactement celle du semi-groupe.

Le champ de transition

```text
H_(s,r)(t)=V_r(t)-V_s(t)=S(t-r)g_(s,r)            (50.6)
```

est calorique et vérifie l'identité énergétique exacte

```text
||H_(s,r)(t)||_2²
 +2 integral_r^t||nabla H_(s,r)(tau)||_2² d tau
 =||g_(s,r)||_2².                                (50.7)
```

Ainsi, la cohérence existe déjà et est contractive dans l'espace d'énergie.
Le verrou n'est pas l'algèbre du recollement, mais la taille de la donnée de
transition `g_(s,r)` lorsque `s->-infinity`.

## Limite locale quand le temps de base recule

Pour tout entier `k>=0`, tout compact `K`, tout `1<=p<=infinity` et toute
bande fixe `[r,T]`, le lissage faible-Lorentz donne

```text
sup_(tau in [r,T])||nabla^k V_s(tau)||_(L^p(K))
 <=C_(k,p,K) M (r-s)^(-(1+k)/2).                  (50.8)
```

Donc

```text
V_s ->0 dans L-infinity([r,T];W^(k,p)(K)),
g_(s,.)=v-V_s ->v localement,                     (50.9)
```

lorsque `s->-infinity`. Cette convergence est forte et quantitative sur tout
compact, mais ne dit rien sur la somme des queues spatiales. Le correcteur
absorbe localement toute la solution ancienne tandis que son énergie globale
peut s'échapper vers les échelles `|x|~sqrt(r-s)`.

## Porte uniforme et coût en énergie totale

Fixons `r<=0`. Si une suite `s_n->-infinity` satisfaisait

```text
sup_n||g_(s_n,r)||_2<=E,                           (50.10)
```

alors (50.8) donne la convergence forte
`g_(s_n,r)->v(r)` dans `L2(B_R)` pour chaque `R`. Par Fatou puis convergence
monotone en `R`,

```text
v(r) in L2(R3),
||v(r)||_2<=E.                                    (50.11)
```

Une énergie de transition uniforme ne serait donc pas une amélioration
technique mineure : elle forcerait une trace ancienne d'énergie totale finie.
La borne disponible (50.3) vaut seulement

```text
||g_(s,r)||_2<=C_D M²(r-s)^(1/4),                 (50.12)
```

et diverge lorsque le temps de base recule. Les inégalités du cycle 0049 ne
fournissent aucune tightness spatiale qui permettrait de remplacer (50.12)
par (50.10).

## Quotients algébrique et séparé

Posons

```text
X=L^(3,infinity)_sigma(R3),
Y=X inter L2_sigma(R3).                           (50.13)
```

`Y` est stable par le semi-groupe de chaleur. Le quotient **algébrique**
`Q_alg=X/Y` est exact pour le cocycle; aucune norme quotient n'y est invoquée,
car `Y` n'est pas fermé dans `X`. Une construction par blocs solénoïdaux
disjoints, d'amplitude `n^-3` et de volume `n^6`, donne en effet une limite
faible-`L3` non `L2` de sommes partielles dans `Y`. Comme `g_(s,t)` appartient
à `Y`, (50.2) devient

```text
[v(t)]=[S(t-s)v(s)] dans X/Y.                     (50.14)
```

Les scissions BSS sur toutes les bandes disent donc que la classe de `v`
évolue calorifiquement modulo énergie finie. Pour conclure que cette classe
est nulle, il faudrait un théorème de rigidité du semi-groupe induit sur ce
quotient, ou une information PDE supplémentaire sur les basses fréquences et
les queues.

Le quotient topologique correct est

```text
Q_H=X/closure_X(Y).                                    (50.14a)
```

Il est séparé et banachique; le semi-groupe y induit une action bornée, sans
que la forte continuité soit affirmée sur tout `X`. La relation (50.14) y
reste vraie. En revanche, une classe nulle dans `Q_H` signifie seulement
`v(t) in closure_X(Y)`, non `v(t) in L2`. Le critère énergétique (50.10)
reste donc strictement plus fort que l'annulation dans le quotient séparé.

## Contre-profil quotient homogène

Considérons le champ solénoïdal homogène

```text
U(x)=(-x_2,x_1,0)/|x|².                           (50.15)
```

Il est tangent aux sphères, divergence-free au sens des distributions et
homogène de degré `-1`. Sa fonction de distribution vérifie exactement

```text
K_3(U)^3=pi²/4,                                   (50.16)
```

donc `U in X`, tandis que `U notin L2(R3)`. Pour `h>0`, l'homogénéité donne

```text
S(h)U(x)=h^(-1/2)(S(1)U)(x/sqrt(h)),
(I-S(h))U(x)=h^(-1/2)G(x/sqrt(h)),
G=U-S(1)U.                                       (50.17)
```

Le champ `G` appartient à `L2`. Avec la convention
`hat(f)(xi)=integral exp(-i x dot xi)f(x) dx`, le calcul de Fourier donne

```text
C_U²=(8 pi^(5/2)/3)(1-1/sqrt(2)) in (0,infinity),
```

et l'homogénéité donne l'identité exacte

```text
||(I-S(h))U||_2=C_U h^(1/4).                     (50.18)
```

Ainsi `(I-S(h))U in Y`, donc

```text
[S(h)U]=[U] !=0 dans Q_alg et Q_H.               (50.19)
```

Le semi-groupe induit sur le quotient possède des classes fixes non nulles.
La non-nullité dans `Q_H` suit d'une minoration uniforme de la distance à
`Y` sur des cônes annulaires où `|U|~R^-1`: la masse faible-`L3` du profil
ne peut être retirée par une queue `L2`.
Le cocycle fonctionnel

```text
z_(s,t)=(I-S(t-s))U                               (50.20)
```

satisfait exactement (50.5) et sature la puissance temporelle `1/4`.

Cette saturation possède un résidu de quantificateurs exact. Si

```text
E(T,R)=integral_(B_R)|(I-S(T))U|²,
```

alors, pour `T` fixé, le défaut est globalement `L2`, tandis que pour `R`
fixé il converge vers `U` dans `L2(B_R)`. Par conséquent,

```text
lim_(T->infinity) lim_(R->infinity) E(T,R)/R =0,
lim_(R->infinity) lim_(T->infinity) E(T,R)/R =8pi/3.  (50.20a)
```

Le passage au domaine entier et le recul du temps de base ne commutent pas.
Le résidu `8pi/3` est l'énergie locale linéaire exacte de (50.15), pas une
erreur de discrétisation.

## Variante lisse à énergie locale globale par tranche

Soit `chi_0` radiale, lisse, nulle sur `B_1` et égale à un hors de `B_2`, et

```text
U_sharp=chi_0 U.                                  (50.21)
```

Comme `U` est tangent aux sphères, `U_sharp` reste divergence-free. Il est
lisse, appartient à `X inter Hdot1`, mais pas à `L2`. Puisque
`d=U_sharp-U` appartient à `L2`, la contraction calorique donne

```text
||(I-S(h))U_sharp-(I-S(h))U||_2<=2||d||_2,

||(I-S(h))U_sharp||_2=C_U h^(1/4)+O(1)            (50.22)
```

lorsque `h->infinity`. Chaque incrément est dans `L2 inter Hdot1`, possède
une trace `L2` nulle lorsque `h decreases to0`, et satisfait le même cocycle.
La régularité énergétique bande par bande et l'algèbre de recollement ne
produisent donc toujours pas une borne uniforme.

De plus, `U_sharp` est borné. Il appartient donc déjà au sous-espace
`tilde L^(3,infinity)` défini par Taniuchi comme la fermeture dans
`L^(3,infinity)` des champs également `L-infinity`. La continuité forte du
semi-groupe au **temps initial** n'annule pas pour autant sa classe quotient
aux **grands temps**. La branche
`GAP-TYPE-I-BSS-TO-STRONG-MILD-CONTINUITY`, même si elle était fermée, ne
suffirait donc pas seule à la rigidité ancienne.

Ni `U` ni `U_sharp` ne sont présentés comme solutions de Navier--Stokes. La
variante lisse ne satisfait pas l'inégalité relative PDE du cycle 0049. Ces
champs réfutent une implication **fonctionnelle et semi-groupale**, pas un
théorème futur exploitant toute la suitability, la pression et le transfert
non linéaire.

## Passe contradictoire principale

1. Le quotient de (50.13) est algébrique et non séparé; le qualifier de
   Banach sans fermer `Y` serait faux. Le quotient séparé (50.14a) ne doit
   pas davantage être confondu avec l'appartenance `L2`.
2. La convergence locale (50.9) n'implique aucune convergence globale `L2`.
3. Une borne uniforme (50.10) impose déjà `v(r) in L2`; elle ne peut pas être
   supposée comme simple propriété de cohérence.
4. L'énergie calorique (50.7) conserve la taille initiale de transition; elle
   ne crée aucune décroissance uniforme au bord `t=r`.
5. Le découpage d'un long intervalle en petits intervalles ne répare pas
   (50.12): la somme des bornes `h^(1/4)` empire sous subdivision.
6. `V_s->0` dans `L-infinity_x` localement et même globalement en norme
   `L-infinity_x`, mais cette norme ne contrôle pas son énergie totale.
7. Le contre-profil homogène sature la puissance temporelle, pas la puissance
   quadratique `M²` propre au Duhamel Navier--Stokes.
8. La variante lisse est cinématique; elle ne réfute pas une amélioration qui
   utiliserait le signe complet de l'inégalité relative ou la pression PDE.
9. Aucun résultat n'est transféré vers Type II.
10. Une classe quotient fixe n'est ni une singularité ni une solution
    ancienne admissible.

## Résultat et pivot

Le maillon positif fermé est

```text
scissions BSS sur toutes bandes
 -> cocycle L2 exact et transition calorique contractive
 -> convergence locale du correcteur vers v quand s->-infinity.   (50.23)
```

Le résultat négatif est

```text
cocycle + régularité énergétique bande par bande + faible-L3
 -/-> borne L2 uniforme des transitions
 -/-> annulation de la classe dans X/Y.                         (50.24)
```

Le verrou `GAP-TYPE-I-BSS-BASE-TIME-COHERENCE` est donc fermé algébriquement,
mais sa version uniforme est abandonnée sans hypothèse de tightness ou
d'annulation des basses fréquences. Le verrou est raffiné en

```text
GAP-TYPE-I-ANCIENT-QUOTIENT-RIGIDITY,
GAP-TYPE-I-BSS-ENERGY-TAIL-TIGHTNESS.                       (50.25)
```

L'expérience décisive suivante doit tester une quantité PDE qui voit la
classe quotient : soit une annulation basse fréquence uniforme de
`v(t)-S(t-s)v(s)`, soit une tightness énergétique dérivée de la pression et
du défaut local d'énergie. Rejouer uniquement le cocycle calorique est
abandonné.
