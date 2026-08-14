# Cycle 0025 — train critique de blobs solénoïdaux

Date de gel : 2026-08-14.

Statut : construction statique exacte, dérivation interne et certificat
rationnel. Aucun résultat n'est une preuve Clay et aucune trajectoire
Navier–Stokes n'est calculée.

## Décision du cycle

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| train explicite de blobs critiques + test BMO global | 5 | 5 | 5 | 5 | **20** |
| remplacer `Phi<=M` par un moment angulaire `L^p` | 5 | 3 | 5 | 5 | 18 |
| évolution Galerkin validée d'un train tronqué | 4 | 2 | 4 | 3 | 13 |

Le verrou actif est `GAP-UNBOUNDED-ANGULAR-INTERMITTENCY`. Le lemme teste si
la concentration sparse du cycle 0024 peut être réalisée par une vraie
vorticité divergence-free, avec vitesse d'énergie finie et raccord
Biot–Savart, tout en conservant l'hypothèse directionnelle globale.

## Équation et type de solution

La cible Clay reste Navier–Stokes incompressible non forcé sur `R³`, avec
viscosité normalisée à un :

```text
partial_t u-Delta u+(u dot nabla)u+nabla p=0,
div u=0,                    omega=curl u.
```

La construction ci-dessous n'est qu'un champ statique `u∈L²`, divergence-free,
lisse par morceaux hors du point d'accumulation. Elle fournit une donnée de
Leray admissible, mais pas une donnée initiale lisse de l'énoncé Clay et pas
une solution stationnaire.

## Lemme actif

Posons, avec prolongement nul hors de `[-1,1]`,

```text
P(t)=(1-t²)^4_+,
psi(x,y,z)=P(x)P(y)P(z),
U_0=(partial_y psi,-partial_x psi,0),
W_0=curl U_0.
```

Alors `P∈C³`, `U_0∈C²_c`, `W_0∈C¹_c`, et

```text
div U_0=0,       curl U_0=W_0,       div W_0=0           (1)
```

au sens classique dans le cube et distributionnel sur `R³`.

Pour `n>=1`, définissons

```text
r_n=2^-n,
ell_n=r_n/(8n),
x_n=r_n e_3,
U_n(x)=ell_n^-1 U_0((x-x_n)/ell_n),
W_n(x)=ell_n^-2 W_0((x-x_n)/ell_n),                 (2)
```

et `u=sum U_n`, `W=sum W_n`. Les supports sont disjoints et s'accumulent
uniquement en zéro.

Le résultat borné du cycle est :

1. `u∈L²(R³)`, `div u=0`, `W=curl u`, `div W=0`;
2. `W∈L¹(R³)∩L^(3/2,infinity)(R³)` avec une masse critique non dégénérée dans chaque
   bloc logarithmique dyadique;
3. l'amplitude du facteur angulaire `r²|W|` vaut `1024n²` au centre du
   `n`-ième blob;
4. l'extension par zéro de la direction a une oscillation sur les boules
   **centrées en l'origine** au plus `1/(378n³)`;
5. pourtant toute extension localement intégrable coïncidant avec `W/|W|`
   sur `{W!=0}` a une oscillation au moins `c_dir>0` sur une suite de boules
   de rayon `ell_n/2->0` situées dans les blobs;
6. aucune telle extension n'appartient donc à `VMO` ni au
   `bmo_(1/|log r|)` global;
7. le résidu stationnaire n'est pas un gradient et ne peut être annulé par
   une pression.

## Étape 1 — base div–curl exacte

Dans le cube actif,

```text
W_0=(P'(x)P(y)P'(z),
     P(x)P'(y)P'(z),
    -[P''(x)P(y)+P(x)P''(y)]P(z)).                    (3)
```

La commutation des dérivées donne (1). Comme les dérivées de `P` jusqu'à
l'ordre trois s'annulent en `+/-1`, aucune mesure de bord n'apparaît dans les
identités distributionnelles utilisées.

Deux valeurs rationnelles suffisent à certifier que la direction de base
n'est pas constante :

```text
W_0(0,0,0)=(0,0,16),
[W_0(0) cross W_0(1/2,0,1/2)]_2 !=0.                 (4)
```

## Étape 2 — séparation et énergie

Les intervalles de support suivant `e_3` vérifient

```text
r_n-ell_n > r_(n+1)+ell_(n+1),
```

car, après division par `r_n`, la marge est au moins

```text
1/2-1/8-1/32=11/32.                                  (5)
```

La séparation rend les identités terme à terme non ambiguës. Le scaling de
vitesse donne

```text
||U_n||_2²=ell_n ||U_0||_2²,
sum ell_n <=1/8.                                      (6)
```

Le calcul polynomial exact fournit

```text
||U_0||_2²=1125899906842624/539065498096125.
```

Ainsi `u∈L²`. Dans `L²`, le champ divergence-free est déterminé par son curl
sans mode harmonique non nul; le raccord de Fourier donne donc

```text
u=curl(-Delta)^-1 W                                (7)
```

au sens distributionnel. Cette égalité fixe le Biot–Savart statique, pas une
pression ni une évolution.

Le même calcul donne `||W_n||_1=ell_n||W_0||_1`, donc `W∈L¹`. En revanche,
`||U_n||_3³` et `||W_n||_(3/2)^(3/2)` sont indépendants de `n`; les normes
fortes `L³` de la vitesse et `L^(3/2)` de la vorticité divergent.

## Étape 3 — faible-`L^(3/2)` et masse par bloc

Une borne volontairement grossière issue de (3) est `|W_0|<=224`. Comme
`ell_(n+1)/ell_n<=1/2`, si `N` est le premier indice pouvant dépasser un
seuil `lambda`,

```text
|{|W|>lambda}| <= 8 sum_(n>=N)ell_n³
                 <=(64/7)ell_N³.
```

Il s'ensuit

```text
lambda |{|W|>lambda}|^(2/3) <=3584.                  (8)
```

Réciproquement, sur le cube `[-1/8,1/8]³`,

```text
|W_0|>=|W_(0,3)|
 >=(63/64)^12(57/4)>10.                              (9)
```

Au seuil `5ell_n^-2`, le quasi-norme est donc au moins `5/16`. Le champ est
réellement critique, non seulement majoré par un espace faible.

Le changement de variables donne pour chaque blob

```text
integral |W_n|^(3/2) dx=integral |W_0|^(3/2) dx.     (10)
```

Les annuli logarithmiques de longueur `log 2`, centrés sur `r_n`, contiennent
chacun le support correspondant; (9) fournit une masse uniforme. En revanche,

```text
r_n²|W_n(x_n)|=16(r_n/ell_n)²=1024n².                (11)
```

Le mécanisme intermittent exact du cycle 0024 est ainsi réalisé avec
divergence, curl, énergie et Biot–Savart suivis.

## Étape 4 — le test centré est trompeur

La boule `B_(3r_N/2)(0)` contient les blobs `n>=N` et aucun blob extérieur.
Leur volume de support satisfait

```text
sum_(n>=N)8ell_n³ <=(64/7)ell_N³.
```

En utilisant `pi>3`, la fraction active est inférieure à `1/(756N³)`. Pour
l'extension par zéro `zeta_0`, `|zeta_0|<=1`, donc

```text
average_B |zeta_0-(zeta_0)_B|
 <=2 average_B|zeta_0|
 <1/(378N³).                                          (12)
```

Cette famille passe largement le taux `O(1/N)` si l'on ne teste que les
boules centrées au point d'accumulation.

## Étape 5 — la BMO globale détecte chaque blob

Il existe deux petits cubes rationnels `E,F` contenus dans
`B((1/4,0,1/4),1/2)` où `W_0` ne s'annule pas et où la première composante de
`W_0/|W_0|` est séparée par une constante rationnelle positive. Pour toute
extension `zeta` de la direction et tout vecteur moyen `m`, l'inégalité
triangulaire appliquée à la première composante donne

```text
average_B|zeta-m| >= c_dir
 =2384963/22109421704515245593067520000 >0.           (13)
```

La constante est minuscule parce que le certificat utilise seulement les
sommes absolues des coefficients; sa positivité uniforme est le point utile.

Après translation et scaling, la même minoration vaut dans

```text
B_n=x_n+ell_n B((1/4,0,1/4),1/2),
radius(B_n)=ell_n/2 ->0.                              (14)
```

Elle ne dépend pas de la convention sur les zéros : `E_n` et `F_n` sont dans
l'ensemble actif. Comme tout poids `phi(r)->0`, en particulier
`phi(r)=1/[1+log(R_*/r)]`, satisfait `c_dir/phi(ell_n/2)->infinity`, aucune
extension n'est dans le `bmo_phi` global.

Pour l'extension par zéro, une obstruction plus forte apparaît sur chaque
face régulière. Une boule centrée sur `x=1` dans les coordonnées du blob est
exactement à moitié active. Pour une fraction active `a=1/2`,

```text
average|zeta-zeta_B|
 >=average ||zeta|-|zeta_B|| >=1/2.                  (15)
```

## Étape 6 — résidu stationnaire

À viscosité un, posons dans le cube de base

```text
R_0=-Delta U_0+(U_0 dot nabla)U_0.
```

Le certificat trouve 1804 monômes non nuls dans `curl R_0`. Il n'existe donc
aucune pression `p_0` telle que `R_0+nabla p_0=0`. Sous (2),

```text
R_n=ell_n^-3 R_0((x-x_n)/ell_n),                     (16)
```

et sa masse `L¹` est invariante d'échelle. La somme de ces coûts ne décroît
pas. La construction est un contre-profil statique, pas un blow-up ni même
une solution stationnaire.

## Échelle des quantités

Chaque blob emploie exactement le scaling Navier–Stokes

```text
U_n=ell_n^-1 U_0(. /ell_n),
W_n=ell_n^-2 W_0(. /ell_n),
R_n=ell_n^-3 R_0(. /ell_n).
```

La masse `L^(3/2)` de `W_n` et la masse `L¹` du résidu sont invariantes;
l'énergie cinétique porte le facteur sous-critique `ell_n`. L'amplitude
angulaire croît comme `n²` et l'occupation centrée décroît comme `n^-3`.

## Passe contradictoire

1. La faible norme critique et l'énergie finie sont globales, mais `u` n'est
   ni borné ni lisse au point d'accumulation.
2. La construction donne une donnée de Leray; l'existence faible associée ne
   conserve pas nécessairement la géométrie du train.
3. La petite oscillation centrée (12) ne contrôle pas la semi-norme sur toutes
   les boules. La confusion est réfutée par (13) et (15).
4. Changer seulement les valeurs aux zéros ne répare pas (13), qui utilise
   deux sous-ensembles actifs.
5. Le raccord Biot–Savart (7) n'implique aucune estimation de pression pour
   le résidu non linéaire.
6. Une troncature à un nombre fini de blobs est régulière à l'origine mais ne
   teste aucune limite uniforme; ses constantes BMO se dégradent avec le
   dernier blob.
7. Une échappatoire doit modifier la **forme directionnelle interne** à chaque
   échelle, et pas seulement réduire la fraction active.

## Passes contradictoires séparées

Trois rapports sont conservés sans les qualifier de revues externes :

- `reviews/cycle-0025-analysis.md` refait la construction avec la variante
  `ell_n=r_n/(4n)`, une énergie exacte et une minoration de face pour
  l'extension par zéro;
- `reviews/cycle-0025-countermodel.md` traite une base lisse générique,
  distingue normes faibles et fortes, recalcule les queues de pression et
  montre que le motif interne, non les seuls zéros, condamne toute extension;
- `reviews/cycle-0025-literature.md` replace l'indicateur actif dans la théorie
  VMO classique et corrige la portée des conventions aux zéros à temps
  positif régulier.

Les constantes `256n²` de la première variante et `1024n²` du profil
canonique ne sont pas contradictoires : elles correspondent respectivement
aux facteurs `1/4` et `1/8` dans `ell_n/r_n`. Le claim canonique et le script
utilisent partout `ell_n=r_n/(8n)`.

## Veille différentielle

La veille primaire est consignée dans `reviews/cycle-0025-literature.md`.
Brezis–Nirenberg 1995 et Bourgain–Brezis–Mironescu 2015 montrent que la
rigidité des idempotents VMO est standard. Pour `zeta=xi 1_A`, on a directement

```text
theta_B(1-theta_B)<=average_B|zeta-zeta_B|.           (17)
```

Grujić–Kukavica 1998 et Herbst–Skibsted 2009 apportent une correction de
portée : à tout temps positif où une solution forte non triviale est régulière,
sa vorticité est analytique et son lieu nodal commun a mesure nulle. Deux
conventions qui diffèrent seulement **sur** les zéros représentent alors le
même élément BMO. Le vrai défaut dynamique est la phase au voisinage du lieu
nodal. La minoration interne (13) reste pertinente car elle porte sur deux
ensembles où `W!=0`, mais le saut de support (15) est surtout un test de donnée
initiale compacte.

Les travaux publiés de Feng–Šverák et Gallay–Šverák sur les anneaux visqueux
ne fournissent pas une alternative uniformément critique : à circulation et
rayon majeur fixes, un cœur de largeur `delta` a une norme
`L^(3/2,infinity)` d'ordre `delta^(-2/3)`. Aucun théorème publié n'est attribué
à la construction du train.

## Verdict et écart avec Clay

Résultat positif borné : l'intermittence non bornée peut coexister avec
`div W=0`, une vitesse d'énergie finie, Biot–Savart, une borne globale
faible-`L^(3/2)` et une masse critique par bloc. Ces conditions ne suffisent
donc pas à éliminer un train sparse.

Résultat négatif : répéter une géométrie de blob non constante à des échelles
qui tendent vers zéro viole automatiquement la prémisse log-BMO globale, même
si toutes les moyennes centrées décroissent beaucoup plus vite que le taux
requis. Le scénario exact construit n'est pas une singularité admissible.

Le verrou est resserré en `GAP-DIRECTIONALLY-FLAT-INTERMITTENCY` : construire
un blob solénoïdal dont l'amplitude se concentre tandis que l'oscillation de sa
direction interne tend vers zéro, ou démontrer une minoration uniforme de
cette oscillation depuis divergence, curl et localisation.

## Reproduction

```text
python -B experiments/navier-stokes/critical-blob-train/critical_blob_train_audit.py
```

Le script utilise Python 3.13.14, la bibliothèque standard et
`fractions.Fraction`. Il effectue 104 contrôles exacts, sans grille, flottant
ni graine. Les résidus des identités polynomiales sont nuls; le résidu
Navier–Stokes stationnaire, lui, est certifié non nul modulo pression.
Empreinte SHA-256 :
`129921806266636a46a5202bd0f2912491aaf557a02cda229c17ef80a529cb15`.
