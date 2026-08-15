# Cycle 0059 — vitesse tangentielle canonique dans un Hilbert négatif

Date : 2026-08-15.

Statut : `AI_INTERNAL_DERIVATION`; lemme fonctionnel conditionnel, aucune
conclusion Clay.

## Décision adaptative

Le verrou relu est
`GAP-TYPE-I-CANONICAL-PHASE-DEFECT-BOUND-OR-RSS-RIGIDITY`. Les actions sont
notées avant la dérivation :

| action | nouveauté | tractabilité | falsifiabilité | levier | total |
|---|---:|---:|---:|---:|---:|
| projeter la dérivée PDE sur la tangente SO(2) dans un Hilbert négatif | 4 | 5 | 5 | 5 | **19** |
| imposer une tranche à gabarit fixe et inverser sa matrice de Gram | 4 | 4 | 5 | 4 | 17 |
| synchroniser directement des phases locales sur une exhaustion | 4 | 3 | 4 | 4 | 15 |

La première action est sélectionnée. Elle évite d'inverser la norme du
générateur pour borner le défaut : le produit vitesse--générateur est un
projecteur orthogonal, donc reste contractif jusque sur le stabilisateur.

## Équation et ledger

Sur un intervalle borné `J`, les approximants `Z_n` sont divergence-free et
résolvent sur `R3`, sans frontière et avec viscosité un,

```text
partial_s Z_n-Delta Z_n+div(Z_n tensor Z_n)+nabla Pi_n
 +kappa(1+y dot nabla)Z_n=F_n,       kappa>0.             (59.1)
```

La pression est fixée par la jauge globale de Riesz et `F_n` est le défaut de
cutoff localement uniforme du pipeline. La limite et le problème Clay sont
non forcés. Le ledger du cycle 0045 donne, pour chaque entier `m>=1`,

```text
D_m^raw:=sup_n ||partial_sZ_n||_(L-infinity(J;W^(-2,4/3)(B_m)))<infinity,
sup_n ||Z_n||_(L-infinity(J;L2(B_m)))<infinity.           (59.2)
```

L'action centrée autour de `e_3` et son générateur sont

```text
(Q_theta U)(y)=R_theta U(R_(-theta)y),
mathcal RU=JU-(Jy dot nabla)U.                            (59.3)
```

L'axe, le centre et les boules sont communs à toute la suite.

## Un Hilbert local invariant contenant le ledger brut

Posons d'abord

```text
X_m=H^(-3)(B_m)^3=(H_0^3(B_m)^3)^*.                     (59.4)
```

En dimension trois,

```text
H_0^3(B_m) -> W_0^(2,4)(B_m),
W^(-2,4/3)(B_m) -> H^(-3)(B_m).                          (59.5)
```

La première flèche est l'injection de Sobolev; la seconde est sa duale. Le
coût dépend de `m`. À partir d'un produit scalaire hilbertien quelconque sur
`X_m`, on définit le produit invariant

```text
<f,h>_(m,rot)
 =(1/(2pi)) integral_0^(2pi)<Q_theta f,Q_theta h>_(X_m) dtheta. (59.6)
```

Il induit une norme équivalente et rend chaque `Q_theta` unitaire. Les
constantes d'équivalence ne sont jamais déclarées uniformes en `m`.

Pour `phi in H_0^3(B_m)`, le déplacement du générateur sur le test donne

```text
<mathcal RZ_n,phi>
 =<Z_n,(Jy dot nabla)phi-Jphi>,                           (59.7)
```

d'où `mathcal RZ_n` borné dans `L-infinity(J;H^(-1)(B_m))`, donc dans
`L-infinity(J;X_m)`. Après inclusion (59.5) et équivalence (59.6), notons
par `D_m<infinity` l'enveloppe de `partial_sZ_n` dans `X_m`, et par
`G_m<infinity` celle de `mathcal RZ_n`.

## Un seul espace sur toute l'exhaustion

Une projection effectuée séparément sur chaque boule donnerait des vitesses
différentes et ne construirait pas une modulation commune. Pour l'éviter,
fixons explicitement

```text
w_m=2^(-m)/(1+D_m^2+G_m^2)>0.                            (59.8)
```

Pour `k>=m`, la restriction distributionnelle
`rho_(k,m):X_k->X_m` est continue : son adjoint est l'extension par zéro
`H_0^3(B_m)->H_0^3(B_k)`. Dans la somme hilbertienne pondérée, définissons

```text
X={ (f_m): sum_m w_m||f_m||_(m,rot)^2<infinity,
             rho_(k,m)f_k=f_m pour tous k>=m }.           (59.9)
```

Les conditions de compatibilité sont les noyaux d'applications continues;
`X` est donc un sous-espace fermé, complet et séparable. Chaque famille se
recolle en une distribution unique sur `R3`. Sa norme est la somme de (59.9),
les restrictions vérifient
`||f_m||_(X_m)<=w_m^(-1/2)||f||_X`, et l'action SO(2) diagonale est unitaire.
Après réunion des ensembles temporels négligeables,

```text
sup_n ||partial_sZ_n||_(L-infinity(J;X))<=1,
sup_n ||mathcal RZ_n||_(L-infinity(J;X))<=1,              (59.10)
```

à une constante universelle de somme géométrique près. Les valeurs exactes
des enveloppes peuvent être absorbées dans (59.8). Ce choix est canonique une
fois le ledger et ses poids épinglés; il dépend de la suite, de `J` et de la
métrique. Il n'est pas une jauge intrinsèque de Navier--Stokes.

La forte mesurabilité dans `X` suit de la mesurabilité dans chaque coordonnée
et de la queue uniforme
`sum_(m>M)w_m||d_n|_(B_m)||^2<=sum_(m>M)2^(-m)`, de même pour
`g_n`. Les poids sont strictement positifs, fixés sur `J` et indépendants de
`n,s`; des poids mobiles détruiraient le Hilbert commun.

## Vitesse tangentielle par projection orthogonale

Écrivons, presque partout en `s`,

```text
d_n(s)=partial_sZ_n(s),
g_n(s)=mathcal RZ_n(s).                                  (59.11)
```

Définissons

```text
beta_n(s)=<d_n(s),g_n(s)>_X/||g_n(s)||_X^2 si g_n(s)!=0,
beta_n(s)=0 sinon,
r_n=d_n-beta_n g_n.                                      (59.12)
```

Les champs `d_n,g_n` sont fortement mesurables dans le Hilbert séparable
`X`; produits scalaires et normes le sont aussi. Ainsi `beta_n` et `r_n`
sont mesurables. Lorsque `g_n!=0`, `beta_n g_n` est le projecteur orthogonal
de `d_n` sur la droite `R g_n`. Lorsque `g_n=0`, le produit vaut encore zéro
et le choix `beta_n=0` épingle le stabilisateur.

On a exactement

```text
<r_n,g_n>_X=0,
||d_n||_X^2=|beta_n|^2||g_n||_X^2+||r_n||_X^2,           (59.13)
```

donc

```text
||r_n||_X<=||d_n||_X,
||beta_n g_n||_X<=||d_n||_X.                             (59.14)
```

La dégénérescence de Gram `||g_n||_X->0` peut rendre `beta_n` grand, mais ne
fait exploser ni le défaut ni le produit tangent. C'est le gain précis par
rapport à l'inversion d'une tranche à gabarit fixe.

La formule minimise `b -> ||d_n-b g_n||_X`. Elle construit une vitesse de
régression tangentielle, pas nécessairement la dérivée d'une phase globale.
Une reconstruction `theta_n'=beta_n` exige en plus
`beta_n in L1_loc`, qui n'est pas déduite de (59.10)--(59.14).

La construction est équivariante. Une rotation fixe `Q_gamma` conserve
`beta_n`. Pour une jauge absolument continue dépendant du temps,

```text
Z_tilde=Q_gamma Z,
d_tilde=Q_gamma(d+gamma' g),
g_tilde=Q_gamma g,
beta_tilde=beta+gamma',
r_tilde=Q_gamma r,                                       (59.15)
```

tant que `g!=0`. Au stabilisateur, la vitesse redevient non identifiable.
Cette loi est celle d'une connexion de phase, mais ne rend pas la grandeur de
`beta` invariante sous un changement de repère temporel.

## Collapse canonique à grande vitesse

Supposons, sur `J`,

```text
b_(n,J):=ess inf_(s in J)|beta_n(s)| ->infinity.          (59.16)
```

Dans le repère similaire fixe de (59.1), pour les grands `n`, `g_n!=0`
presque partout. Les identités (59.13)--(59.14) donnent le majorant plus fort
que celui du cycle 0058 :

```text
||mathcal RZ_n||_(L^p(J;X))
 <=b_(n,J)^(-1)||partial_sZ_n||_(L^p(J;X)),
1<=p<=infinity.                                           (59.17)
```

Si `Z_n->Z` dans les distributions, alors `mathcal RZ_n->mathcal RZ` dans
les distributions. Comme chaque restriction `X->X_m` est continue, (59.16)
et (59.17) imposent

```text
mathcal RZ=0.                                              (59.18)
```

La limite est exactement axisymétrique, swirl permis. Aucun résidu externe,
aucune borne d'inverse de Gram, aucun signe de `beta_n` et aucune variation
de son réciproque ne sont requis. L'hypothèse forte reste (59.16) : la
construction ne prouve pas qu'une suite Type I générale entre dans ce régime.

## Ce que la projection ne contrôle pas

Soit `mathcal A` la moyenne de Haar. Comme
`mathcal A mathcal R=0`, (59.12) donne exactement

```text
mathcal A r_n=mathcal A d_n=partial_s mathcal A Z_n.      (59.19)
```

L'orthogonalité `<r_n,g_n>_X=0` n'annule pas la composante invariante du
défaut : au contraire, toute cette composante est dans `r_n`. La
stationnarité exige encore

```text
mathcal A r_n ->0 dans D'.                                (59.20)
```

Sous (59.20), (59.18) donne `mathcal AZ=Z` puis `partial_sZ=0`. Le ledger
suitable, la pression de Riesz, la borne globale faible-`L3` et la capture
permettent alors seulement l'endgame déjà audité par Guevara--Phuc.

## Contre-profil de Gram exact

Le mécanisme minimal vit dans

```text
H=span(e_0) direct_sum span(e_1,e_2),
mathcal R e_0=0, mathcal R e_1=e_2,
mathcal R e_2=-e_1.                                      (59.21)
```

Pour `epsilon_n=1/n^2`, `theta_n'=n`, et une fonction non constante `h`,

```text
Z_n(s)=h(s)e_0+epsilon_n[
          cos(theta_n(s))e_1+sin(theta_n(s))e_2].         (59.22)
```

Alors

```text
g_n=mathcal RZ_n,
||g_n||=epsilon_n,
beta_n=n,
||beta_n g_n||=1/n,
r_n=h'(s)e_0,
mathcal A r_n=h'(s)e_0.                                  (59.23)
```

La partie tournante s'effondre, `Z_n` converge vers la trajectoire invariante
non stationnaire `h(s)e_0`, le défaut reste borné et le Gram tend vers zéro.
La projection ferme donc exactement l'axisymétrie et rien de plus.

## Pression, suitability et capture

Le choix de `X` utilise l'équation vectorielle complète. Si (59.2) n'est
connu que contre des tests solénoïdaux, le projecteur tangent vit dans un dual
quotienté par les gradients et peut manquer une composante harmonique locale.
La pression de Riesz ou une élimination globale explicite de ces gradients
est nécessaire.

La forte convergence `L3_loc` n'intervient pas dans (59.16)--(59.17). Elle
reste nécessaire pour fermer `Z_n tensor Z_n`, passer la pression et la
capture. Les bornes d'énergie/dissipation et l'inégalité locale doivent être
uniformes séparément; la projection hilbertienne ne les crée pas.

## Échelle et constantes

Dans les variables similaires, `beta_n` est sans dimension puisque `d_n` et
`g_n` ont la même dimension. Le Hilbert local `H^-3` n'est pas critique. Pour
un terme de force physique `f_lambda=lambda^3 f(lambda x)`, la norme homogène
`dot H^-3` porte le facteur `lambda^(-3/2)`. Les poids `w_m`, la fenêtre `J`
et les enveloppes `D_m,G_m` sont épinglés et suivis; aucune invariance sous
changement de ces choix n'est revendiquée.

La borne de collapse est exactement

```text
||partial_sZ_n||_(L^pX)/b_(n,J).                         (59.24)
```

La construction pondérée ne cache pas un passage uniforme au domaine infini :
chaque contrôle local est récupéré avec le facteur explicite `w_m^(-1/2)`.

## Veille différentielle

Beyn--Thümmler (`NS-SRC-0209`) est l'antécédent primaire pertinent pour les
conditions de phase et le gel d'équations d'évolution équivariantes. Leur
cadre reconstruit une phase classique sous inversibilité locale d'une matrice
de phase et stabilisateur approprié. Il ne traite ni solution suitable,
faible-`L3`, pression non locale, Hilbert négatif pondéré, ni limite de
blow-up. La recherche primaire différentielle n'a identifié aucun théorème
Navier--Stokes donnant (59.16) ou (59.20) depuis Type I.

Rowley--Marsden (`NS-SRC-0220`) donnent l'antécédent géométrique de connexion
mécanique et distinguent Gram courant et frontière d'une tranche fixe.
Willis--Cvitanović--Avila (`NS-SRC-0221`) appliquent une tranche à une DNS de
pipe flow forcée avec bord; ce calcul flottant ne certifie aucun passage au
continuum et ne relève pas de la formulation Clay.

## Passe contradictoire

1. **Projection versus phase.** `beta_n` est un coefficient de régression;
   sans intégrabilité temporelle, aucune phase `theta_n` n'est reconstruite.
2. **Métrique.** La vitesse dépend des poids et du produit scalaire. Le mot
   canonique signifie seulement « minimiseur unique pour la métrique
   épinglée ».
3. **Gram nul.** Au stabilisateur, toute vitesse physique est
   non identifiable; le choix zéro est une convention et (59.16) échoue.
4. **Gram petit.** La vitesse peut diverger, mais (59.14) empêche le produit
   tangent et le défaut d'exploser. Cela force seulement `g_n->0`.
5. **Moyenne de Haar.** L'orthogonalité tangentielle ne contrôle pas
   `mathcal A r_n`; le contre-profil (59.22)--(59.23) le réfute exactement.
6. **Exhaustion.** Des projections boule par boule ne donnent pas la même
   vitesse. Les poids (59.8) sont indispensables à un coefficient commun.
7. **Fenêtre.** Les poids sont construits sur `J`; aucune vitesse globale sur
   un intervalle ancien infini n'est produite.
8. **Pression.** Un dual seulement solénoïdal peut annuler uniquement la
   projection de Leray de `mathcal RZ`.
9. **Compacité.** La projection ne transmet ni stress, ni dissipation, ni
   suitability; ces arêtes restent celles du ledger complet.
10. **Type II.** Si les enveloppes locales ne sont pas uniformes, les poids
    ne donnent aucune borne commune utile au passage d'une suite Type II.
11. **Clay.** Ni (59.16), ni (59.20), ni la capture ne découlent d'une
    singularité générale. Le résultat n'est pas un critère global de
    régularité.

## Résultat et nouveau verrou

Le résultat positif est

```text
ledger PDE complet local sur une fenêtre bornée
  --> Hilbert négatif SO(2)-invariant pondéré X
  --> vitesse tangentielle beta_n calculée depuis Z_n
  --> ||r_n||_X et ||beta_n mathcal RZ_n||_X
      bornés par ||partial_sZ_n||_X, même au Gram dégénéré;

ess inf|beta_n|->infinity
  --> mathcal RZ=0;

mathcal A r_n->0
  --> stationnarité, puis endgame conditionnel.           (59.25)
```

Le verrou de borne du défaut canonique est fermé pour cette métrique. Le
verrou actif devient

```text
GAP-TYPE-I-HAAR-DEFECT-DECAY-OR-RSS-RIGIDITY.             (59.26)
```

L'expérience décisive suivante doit appliquer la projection à l'équation
renormalisée et déterminer si l'autonomie, la pression et la capture donnent
un signe ou une décroissance à
`partial_s mathcal A Z_n=mathcal A r_n`. Un contre-profil PDE axisymétrique
non stationnaire satisfaisant tout le ledger sur une fenêtre montre déjà que
la seule énergie locale ne peut suffire; sa vitesse canonique vaut toutefois
zéro, donc il ne réfute pas une éventuelle rigidité PDE sous (59.16). Il faut
une hypothèse asymptotique ou une rigidité ancienne supplémentaire.
