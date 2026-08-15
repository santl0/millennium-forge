# Cycle 0061 — décomposition modale et obstruction métrique

Date : 2026-08-15.

Statut : `AI_INTERNAL_DERIVATION`; lemme hilbertien exact et
contre-modèle fonctionnel, aucune conclusion Clay.

## Décision adaptative

Le verrou relu est
`GAP-TYPE-I-METRIC-ROBUST-FAST-AXISYMMETRIZATION`. Les trois actions sont
notées avant la dérivation :

| action | nouveauté | tractabilité | falsifiabilité | levier | total |
|---|---:|---:|---:|---:|---:|
| décomposer la vitesse canonique en isotypes SO(2) et calculer son enveloppe métrique | 5 | 5 | 5 | 5 | **20** |
| dériver directement une coercivité modale depuis l'équation renormalisée | 4 | 3 | 4 | 5 | 16 |
| pivoter immédiatement vers la rigidité RSS à rotation intermédiaire | 3 | 3 | 4 | 4 | 14 |

La première action est sélectionnée. Elle donne un test nécessaire avant
toute nouvelle estimation PDE : si la grande vitesse disparaît sous un
simple repondérage invariant et uniformément équivalent, elle ne peut pas
être qualifiée d'intrinsèque.

## Équation, solution et échelle

Le pipeline conditionnel reste la suite classique divergence-free sur
`R3 x J`, sans frontière, viscosité un,

```text
partial_s Z_n-Delta Z_n+div(Z_n tensor Z_n)+nabla Pi_n
 +kappa(1+y dot nabla)Z_n=F_n,       kappa>0.             (61.1)
```

La pression est la pression globale de Riesz et `F_n` tend localement vers
zéro le long de la diagonale Type I. La limite visée est faible adaptée
locale, puis ancienne suitable après dérenormalisation. Le lemme de ce cycle
est purement hilbertien : il ne suppose ni (61.1), ni suitability.

Dans le temps similaire `s`, `partial_sZ` et `mathcal RZ` ont le même poids;
leur quotient `beta` est une vitesse angulaire sans dimension. Le Hilbert
`X` du cycle 0059 est une somme locale de `H^-3` et n'est pas invariant par
l'échelle Clay. Les projecteurs azimutaux commutent avec les dilatations
centrées sur le même axe, mais leurs poids de Gram dépendent de la métrique
épinglée.

## Décomposition isotypique exacte

Soit `X` un Hilbert réel séparable portant une représentation fortement
continue et unitaire `Q_theta` de SO(2), de générateur antisymétrique
`mathcal R`. Complexifions `X` et posons

```text
P_k f=(1/(2pi)) integral_0^(2pi) exp(-ik theta)Q_theta f dtheta,
X_C=direct_sum_(k in Z) X_k,          X_k=P_kX_C.         (61.2)
```

Alors `P_kP_l=0` pour `k!=l`, `P_(-k)f=overline(P_kf)` pour `f` réel, et

```text
mathcal R P_k f=ik P_k f.                                 (61.3)
```

À une tranche temporelle où `Z in Dom(mathcal R)` et `d=partial_sZ in X`,
écrivons `Z_k=P_kZ`, `d_k=P_kd` et `g=mathcal RZ`. Pour `k>=1`, définissons

```text
G_k=2 k^2||Z_k||^2,
C_k=2 Re <d_k,ikZ_k>,
b_k=C_k/G_k              lorsque G_k>0.                  (61.4)
```

Le mode `k=0` est dans le stabilisateur et n'entre jamais au dénominateur.
Parseval et la conjugaison des modes `+/-k` donnent, lorsque `g!=0`,

```text
beta=<d,g>/||g||^2
    =(sum_(k>=1)G_k b_k)/(sum_(k>=1)G_k).                 (61.5)
```

Les séries du numérateur sont bien définies par Cauchy--Schwarz :
`sum |<d_k,g_k>|<=||d||||g||`. La formule reste vraie avec une infinité de
modes, mais le résultat de convexité ci-dessous est d'abord énoncé sur tout
ensemble actif fini afin de ne cacher aucun ordre de limite.

## Repondération invariante et enveloppe convexe

Fixons un ensemble fini `I` de modes actifs et, relativement au produit
scalaire précédent, repondérons chaque paire réelle `+/-k` par un scalaire
`lambda_k>0`. L'opérateur

```text
A_lambda=sum_(k in I)lambda_k(P_k+P_(-k))                (61.6)
```

est positif, auto-adjoint et commute avec SO(2). En complétant par l'identité
sur l'orthogonal, il définit un produit scalaire invariant équivalent. La
vitesse projetée pour cette métrique vaut exactement

```text
beta_lambda
 =(sum_(k in I)lambda_kG_kb_k)/(sum_(k in I)lambda_kG_k)
 =sum_(k in I)alpha_kb_k,
alpha_k=lambda_kG_k/sum_l(lambda_lG_l)>0.                (61.7)
```

Réciproquement, tout point de l'intérieur du simplexe est obtenu en prenant
`lambda_k=alpha_k/G_k`. Par fermeture,

```text
closure{beta_lambda:lambda_k>0}=conv{b_k:k in I},
inf_(lambda_k>0)|beta_lambda|
 =dist(0,conv{b_k:k in I}).                              (61.8)
```

Dans la droite réelle, ce dernier terme est nul si deux vitesses actives ont
des signes opposés; sinon il vaut `min_k|b_k|`. Le critère **pointwise
uniforme sur tous les repondérages scalaires** est donc exact : toutes les
vitesses modales actives doivent avoir un même signe et leur module minimal
doit diverger.

Ce critère n'est pas automatiquement celui de « toute métrique SO(2)-
invariante ». Si un isotype a multiplicité supérieure à un, un opérateur
positif commutant avec SO(2) peut agir non scalairement sur l'espace de
multiplicité et changer déjà la valeur de `b_k`. La famille scalaire (61.6)
est néanmoins un sous-ensemble admissible; un échec dans cette famille
réfute toute robustesse dans la famille plus large.

## Trois ordres de quantificateurs à ne pas confondre

Pour une suite temporelle, trois assertions sont différentes :

```text
(P)  une métrique M est épinglée et essinf_J|beta_n^M|->infinity;
(F)  pour toute métrique fixe M, essinf_J|beta_n^M|->infinity;
(U)  inf_M essinf_J|beta_n^M|->infinity.                 (61.9)
```

Le collapse du cycle 0059 n'utilise que `(P)`. L'assertion `(U)` implique
`(F)`, qui implique `(P)` pour chaque métrique choisie, mais les réciproques
sont fausses. En outre,

```text
inf_M essinf_s |beta_n^M(s)|
```

ne coïncide pas en général avec
`essinf_s inf_M |beta_n^M(s)|`, car une métrique admissible au cycle 0059
est fixée sur toute la fenêtre. La distance convexe (61.8) caractérise la
seconde expression pointwise, ou la première lorsque les coefficients
modaux ne dépendent pas du temps. Elle donne un critère suffisant propre pour
`(U)`, pas une permutation gratuite des quantificateurs.

Une restriction uniforme de conditionnement, par exemple
`K^-1<=lambda_k<=K`, réduit l'ensemble accessible mais ne répare pas le
contre-modèle suivant : deux métriques de conditionnement au plus deux
suffisent.

## Contre-modèle à deux modes et métriques fixes

Dans

```text
X=R2 direct_sum R2,
Q_theta=Rot(theta) direct_sum Rot(2theta),
mathcal R=J direct_sum 2J,                               (61.10)
```

posons, pour l'entier `N>=1`,

```text
Z_N(s)=Rot(Ns)e_1 direct_sum (1/2)Rot(-2Ns)e_1.          (61.11)
```

Les deux Grams valent un et les vitesses modales sont exactement

```text
G_1=G_2=1,              b_1=N,              b_2=-N.      (61.12)
```

Pour le produit invariant

```text
<x,y>_(a,b)=a x_1 dot y_1+b x_2 dot y_2,    a,b>0,
```

on obtient

```text
beta_N^(a,b)=N(a-b)/(a+b).                               (61.13)
```

Les poids fixes `(a,b)=(1,1)` donnent `beta_N=0` pour tout `N`, tandis que
`(a,b)=(2,1)` donnent `beta_N=N/3->infinity`. Les deux métriques sont
SO(2)-invariantes, fixes en `N,s` et uniformément équivalentes avec rapport
de conditionnement au plus deux. Ainsi la propriété rapide de `(P)` peut
changer sous une perturbation métrique bénigne.

Un second ledger, avec `G_1=1`, `b_1=N`, `G_2=N^-2`, `b_2=1`, montre la
distinction opposée. Les poids fixes `(1,1)` donnent
`beta_N=(N^3+1)/(N²+1)~N`; les poids mobiles `(1,N²)` restaurent une part de
Gram lente `1/2`, et `(1,N^4)` donnent
`beta_N=(N²+N)/(N²+1)->1`. Ce dernier poids dépendant de `N` est interdit
dans le Hilbert commun du cycle 0059 et son conditionnement diverge; il ne
doit pas servir à réfuter `(F)`. Il réfute seulement une permutation
illégitime entre métrique fixe et infimum pointwise.

## Passe contradictoire

1. **Modes réels.** Les facteurs deux des paires `+/-k` sont conservés dans
   (61.4); ils s'annulent dans le quotient mais pas dans les Grams.
2. **Stabilisateur.** `k=0` et tout mode de Gram nul sont retirés avant de
   former `b_k`; ils ne peuvent pas être repondérés pour créer une vitesse.
3. **Séries infinies.** (61.8) n'est revendiquée exactement que sur un bloc
   fini actif. Une extension exige fermeture du convexe et contrôle des
   domaines des métriques diagonales.
4. **Multiplicité.** Le repondérage scalaire n'épuise pas les produits
   invariants. Il suffit pour le résultat négatif mais pas pour un critère
   nécessaire dans la classe complète.
5. **Temps.** Les poids sont fixes sur `J`; l'infimum pointwise ne peut pas
   être sélectionné séparément à chaque `s` dans la preuve du cycle 0059.
6. **Jauge.** Une rotation temporelle AC ajoute `gamma'` à toutes les
   vitesses modales. Le cadre similaire fixe est donc une hypothèse réelle;
   la robustesse métrique ne crée pas une invariance de jauge temporelle.
7. **PDE.** (61.11) est une courbe hilbertienne exacte, pas une solution de
   (61.1). Elle réfute l'intrinsécité fonctionnelle, pas une éventuelle loi
   de signe modale imposée par Navier--Stokes.

## Décision scientifique

`NS-TYPE-I-CANONICAL-HILBERT-PHASE-COLLAPSE` reste valide pour toute
métrique épinglée qui satisfait son hypothèse rapide. En revanche, le verrou
`GAP-TYPE-I-METRIC-ROBUST-FAST-AXISYMMETRIZATION` est fermé négativement en
tant que propriété automatique de la projection : la grande vitesse n'est
pas intrinsèque, même dans une classe de métriques de conditionnement deux.

Le nouveau verrou est
`GAP-TYPE-I-INTRINSIC-AXISYMMETRY-DEFECT-OR-MODAL-SIGN-COHERENCE`. Il faut
soit produire depuis (61.1) une cohérence de signe et une minoration uniforme
des vitesses modales, soit remplacer `beta` par un défaut d'axisymétrie ne
dépendant d'aucun produit scalaire arbitraire.

## Prochaine expérience décisive

Construire un champ de Schwartz divergence-free possédant au moins deux
modes azimutaux, prendre pour `d` le champ vectoriel instantané exact de
Navier--Stokes renormalisé

```text
d=Delta Z-P div(Z tensor Z)-kappa(1+y dot nabla)Z,        (61.14)
```

et calculer les numérateurs modaux `Re<d_k,ikZ_k>` dans un produit `L2`
où diffusion, drift et pression sont suivis séparément. Deux signes opposés
sur une donnée lisse fourniraient un contre-exemple PDE local à toute
cohérence automatique; un signe universel survivant sur une famille
adversariale isolerait un nouveau lemme coercif à démontrer.
