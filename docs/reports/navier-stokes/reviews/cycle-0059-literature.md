# Cycle 0059 — revue primaire indépendante de la projection de phase

Date de gel : 2026-08-15.

Statut : audit bibliographique indépendant; aucune nouvelle affirmation de
régularité, de singularité ou de résolution du problème Clay.

## Question auditée

Le lemme interne du cycle 0059 définit, dans un Hilbert négatif réel `X`,

```text
d_n=partial_s Z_n,                 g_n=mathcal R Z_n,
beta_n=<d_n,g_n>_X/||g_n||_X^2    si g_n!=0,
r_n=d_n-beta_n g_n.                                      (L59)
```

Il affirme les identités de projection

```text
<r_n,g_n>_X=0,
||d_n||_X^2=|beta_n|^2||g_n||_X^2+||r_n||_X^2,
||beta_n g_n||_X<=||d_n||_X.                             (P59)
```

L'audit cherche l'antécédent exact de `(L59)`, puis sépare quatre questions
qui ne doivent pas être confondues :

1. la minimisation hilbertienne instantanée;
2. la reconstruction d'une phase temporelle;
3. l'inversibilité de la matrice de Gram et le stabilisateur;
4. le transfert aux solutions suitable de Navier--Stokes et au problème Clay.

## Verdict

Le noyau algébrique de `(L59)` n'est pas nouveau : dans une action de groupe à
un paramètre, il coïncide avec la condition adaptative de moindres carrés de
Beyn--Thümmler, équations (2.30)--(2.33), et avec la connexion mécanique de
Rowley--Marsden, appendice B. Il reste cependant utile dans le cycle 0059 par
son implantation dans un Hilbert `H^-3` pondéré adapté au ledger faible.

La distinction décisive est négative : le théorème 2.9 de Beyn--Thümmler ne
couvre pas leur condition adaptative, car celle-ci dépend de
`lambda=gamma_t`. Les auteurs le disent explicitement et reconstruisent alors
la phase par une ODE séparée, sous des hypothèses de régularité plus fortes.
Ainsi `(P59)` ne construit pas à lui seul une phase absolument continue.

Seule la projection hilbertienne instantanée se transfère sans difficulté
conceptuelle au `H^-3` du cycle, après justification de la mesurabilité et de
la différentiabilité de l'orbite dans cet espace. Aucun des textes audités ne
transfère la reconstruction classique, la suitability, la pression, la
compacité de blow-up ou une conclusion Clay.

## 1. Beyn--Thümmler 2004 : ce qui est réellement démontré

### Source et statut

- Wolf-Jürgen Beyn et Volker Thümmler, *Freezing Solutions of Equivariant
  Evolution Equations*, SIAM Journal on Applied Dynamical Systems 3(2),
  85--116 (2004), DOI
  [10.1137/030600515](https://doi.org/10.1137/030600515).
- Source déjà cataloguée : `NS-SRC-0209`.
- Statut : article publié; texte intégral primaire contrôlé.
- Empreinte du PDF contrôlé :
  `SHA256 240522FAE2761F879B7E406D62D5337EF06C271F10E88D72BA1D11455D60909D`.

### Équation, espace et notion de solution

Le cadre est une équation d'évolution abstraite

```text
u_t=F(u),    F:Y subset X -> X,                           (BT-1)
```

où `X` est un espace de Banach, `Y` un sous-espace dense, `G` un groupe de Lie
de dimension finie, non nécessairement compact, et
`a:G->GL(X)` une représentation. Les hypothèses 2.2 et 2.4 imposent notamment

```text
a(gamma)Y=Y,
F(a(gamma)u)=a(gamma)F(u),                               (BT-2)
```

ainsi que la continuité de l'orbite dans `X` et sa différentiabilité pour les
éléments de `Y`. La définition 2.5 porte sur une solution classique

```text
u in C([0,T);X) intersect C^1((0,T);X),    u(t) in Y.     (BT-3)
```

Il ne s'agit donc ni d'une solution faible de Leray--Hopf, ni d'une solution
faible adaptée, ni d'une solution distributionnelle à régularité négative.

### Gel exact et reconstruction avec phase donnée

La décomposition `u(t)=a(gamma(t))v(t)` conduit à

```text
v_t=F(v)-a(gamma^-1)a_gamma(gamma)v gamma_t.              (BT-4)
```

En posant `lambda=gamma_t`, le système gelé (2.20)--(2.22) est

```text
v_t=F(v)-a(gamma^-1)a_gamma(gamma)v lambda,
gamma_t=lambda,
0=psi(v,gamma).                                          (BT-5)
```

Le théorème 2.6 est une équivalence exacte pour un chemin de groupe `C^1`
donné. Cette équivalence ne produit pas ce chemin à partir de la seule
projection `(L59)`.

### Tranches fixes : portée exacte du théorème 2.9

L'hypothèse 2.8 demande l'inversibilité de

```text
psi_gamma(u0,1)-psi_v(u0,1)a_gamma(1)u0 : A -> A*.        (BT-6)
```

Le théorème 2.9 s'applique aux contraintes `psi(v,gamma)=0`, indépendantes de
`lambda`. Il donne localement un chemin `gamma in C^1` par le théorème des
fonctions implicites à partir d'une solution classique de `(BT-1)` et de
`(BT-6)`.

Les deux conditions de distance étudiées sont, pour tout `mu` dans l'algèbre
de Lie,

```text
<a_gamma(1)u0 mu,u0-v>=0,                                (2.26)
<a_gamma(1)v  mu,u0-v>=0.                                (2.27)
```

La proposition 2.10 montre que le stabilisateur trivial de `u0` suffit pour
l'inversibilité visée dans ces deux cas. Elle ne dit pas que tout stabilisateur
non trivial annule nécessairement le Gram infinitésimal : un stabilisateur
fini peut laisser l'application tangentielle injective tout en rendant la
phase globale multivaluée modulo ce stabilisateur.

### Condition adaptative : l'antécédent exact de `(L59)`

Dans le cas hilbertien, les auteurs minimisent instantanément

```text
||v_t||^2=||F(v)-S(v,gamma)lambda||^2,                   (2.30)
S(v,gamma)=a(gamma^-1)a_gamma(gamma)v.                   (2.31)
```

Le minimiseur résout les équations normales

```text
[S* S](v,gamma)lambda=S*(v,gamma)F(v).                   (2.33)
```

Pour `G=SO(2)` à un paramètre, une action unitaire et un générateur constant
`mathcal R`, on a `S lambda=lambda mathcal Rv`, donc

```text
lambda=<F(v),mathcal Rv>/||mathcal Rv||^2.               (BT-7)
```

À une convention de signe ou d'action près, `(BT-7)` est exactement `(L59)`
avec `F(v)` remplacé par la dérivée effective `d_n`. Les équations normales
donnent l'orthogonalité et Pythagore de `(P59)`.

### Point adversarial décisif : le théorème 2.9 ne s'applique pas

Beyn--Thümmler signalent explicitement que le théorème 2.9 ne s'applique pas à
(2.33), parce que la contrainte adaptative dépend de `lambda=gamma_t`. Pour
reconstruire une phase depuis une solution classique `u`, ils proposent
l'ODE (2.34), schématiquement

```text
gamma_t=[(S*S)^-1 S*](a(gamma^-1)u,gamma)
        a(gamma^-1)F(u),    gamma(0)=1.                  (BT-8)
```

Ils exigent alors davantage de régularité : le membre droit doit être continu
en `(gamma,t)` et localement lipschitzien en `gamma`. Ces hypothèses n'existent
pas dans le ledger `L^infinity_t H^-3` du cycle 0059.

La condition orthogonale (2.35) et la condition adaptative coïncident lorsque
`a(gamma^-1)a_gamma(gamma)v` est indépendant de `gamma`, comme pour une action
abélienne à un paramètre avec générateur constant. Cette coïncidence est
algébrique; elle ne rétablit pas les hypothèses de reconstruction.

## 2. Rowley--Marsden 2000 : tranche fixe versus connexion mécanique

### Source et statut

- Clarence W. Rowley et Jerrold E. Marsden, *Reconstruction Equations and the
  Karhunen--Loève Expansion for Systems with Symmetry*, Physica D 142(1--2),
  1--19 (2000), DOI
  [10.1016/S0167-2789(00)00042-7](https://doi.org/10.1016/S0167-2789(00)00042-7),
  [notice primaire Caltech](https://authors.library.caltech.edu/records/vnr3y-9ah91).
- Statut : article publié; source primaire non cataloguée au début du cycle.
- Empreinte de la copie intégrale contrôlée :
  `SHA256 4E43B93161EA08FFEFBB2AC67706B8157D40681C2997E62F41EE93C1A82B08C0`.

### Équation et notion de solution

L'application PDE principale est une équation périodique invariante par
translation,

```text
u_t=D(u),                                                  (RM-1)
```

traitée dans un cadre différentiable et avec le produit `L^2`. Les exemples
et la réduction de modèle concernent notamment Kuramoto--Sivashinsky; ce
n'est pas un théorème de solutions suitable de Navier--Stokes.

### Tranche à gabarit fixe

La condition de tranche

```text
<u(x-c,t),u0'(x)>=0                                      (2.14)
```

donne, après différentiation,

```text
c_t=<D(uhat),u0'>/<uhat_x,u0'>.                          (2.16)
```

Le dénominateur est un Gram croisé entre la tangente courante et la tangente
du gabarit. Il peut s'annuler alors que la tangente courante est non nulle :
c'est une frontière de carte, pas nécessairement un stabilisateur. L'annexe A
montre aussi que le centrage peut sauter et que le gabarit doit être remplacé
ou complété par un atlas.

### Connexion mécanique

L'annexe B définit le tenseur d'inertie verrouillé `I(u)` comme matrice de Gram
des tangentes de groupe et la connexion

```text
A(v_u)=I(u)^-1 J(v_u).                                   (RM-2)
```

Pour une translation à un paramètre,

```text
A(v_u)=<<v_u,u'>>/<<u',u'>>,                             (B.2)
g_t=<<X(utilde),utilde'>>/<<utilde',utilde'>>.           (B.4)
```

Ces formules à tangente courante sont l'antécédent géométrique direct de
`(L59)`. Leur cadre suppose néanmoins une variété lisse, une action libre et
propre et une métrique riemannienne; il n'aborde ni distributions `H^-3`, ni
stabilisateur atteint, ni pression.

## 3. Willis--Cvitanović--Avila 2013 : antécédent Navier--Stokes direct

### Source et statut

- A. P. Willis, P. Cvitanović et M. Avila, *Revealing the state space of
  turbulent pipe flow by symmetry reduction*, Journal of Fluid Mechanics 721,
  514--540 (2013), DOI
  [10.1017/jfm.2013.75](https://doi.org/10.1017/jfm.2013.75),
  [arXiv:1203.3701v1](https://arxiv.org/abs/1203.3701).
- Statut : article publié; source primaire non cataloguée au début du cycle.
- Empreinte du PDF contrôlé :
  `SHA256 8021BFAC44AC4584609FE7663927D0A57811C095B189AAC960C95E99E79F7935`.

### Équation exacte et discrétisation

Le champ est la déviation `u` à l'écoulement de Hagen--Poiseuille `U` dans un
tuyau tridimensionnel :

```text
u_t+U dot nabla u+u dot nabla U+u dot nabla u
 =-nabla p+(32 beta/Re)e_z+(1/Re)Delta u,
div u=0.                                                  (WCA-1)
```

Le bord radial est sans glissement, la cellule est périodique axialement, le
débit massique est imposé et le calcul utilise des modes de Fourier dans les
directions axiale et azimutale avec différences finies radiales. Les exemples
sont à `Re=2400`, dans un tuyau court et dans un sous-espace shift--reflect.
Il s'agit d'une DNS flottante à résolution finie, pas d'un calcul validé par
intervalles ni d'une preuve assistée par ordinateur.

### Formule de phase

Avec le produit d'énergie des vitesses et un gabarit fixé, les équations
(3.3)--(3.5) donnent

```text
<ahat,t'_theta>=0,
vhat(ahat)=v(ahat)-phi_t t(ahat),
phi_t=<v(ahat),t'>/<t(ahat),t'>.                         (WCA-2)
```

La frontière de carte est

```text
<t(ahat*),t'>=0,                                         (3.6)
```

où la vitesse de phase diverge. Les auteurs emploient plusieurs gabarits et
un atlas. Ils indiquent en outre que le choix de la norme dépend de
l'application : leur norme d'énergie n'a aucun statut canonique intrinsèque.

Le lien avec Navier--Stokes est donc réel mais strictement numérique. Les
trajectoires sont intégrées dans l'espace complet et la tranche sert au
post-traitement. Aucun argument ne porte sur une solution suitable faible, le
passage au continuum, le blow-up ou la formulation Clay.

## 4. Matrice de transfert vers le lemme `H^-3`

| composante | antécédent primaire | transfert au cycle 0059 | obstruction restante |
|---|---|---|---|
| minimiser `||d-beta g||_X` | Beyn--Thümmler (2.30)--(2.33), Rowley--Marsden (B.2)--(B.4) | oui, dans tout Hilbert réel | métrique à épingler |
| orthogonalité et Pythagore | équations normales hilbertiennes | oui, presque partout | aucune conclusion temporelle |
| borne `||beta g||<=||d||` | projection orthogonale | oui, même si le Gram tend vers zéro | `beta` peut diverger |
| phase `theta_t=beta` | ODE de reconstruction classique | non sans `beta in L1_loc` | ledger actuel insuffisant |
| tranche fixe | Beyn--Thümmler (2.26)--(2.27), Rowley--Marsden (2.14) | non utilisée par `(L59)` | Gram croisé/frontière de carte |
| inversibilité du Gram | stabilisateur trivial ou action libre | seulement hors stabilisateur infinitésimal | aucune borne uniforme d'inverse |
| action différentiable dans `H^-3` | hypothèse abstraite classique | à démontrer dans le cadre local pondéré | les sources ne le font pas |
| pression | absente des théorèmes abstraits; présente seulement dans la DNS de tuyau | non | compatibilité de Helmholtz du produit local |
| suitability et limite de blow-up | absentes | non | énergie locale, pression et compacité séparées |

## 5. Stabilisateur, Gram et quantificateurs

Pour une action à un paramètre, le Gram adaptatif est le scalaire
`||mathcal Rv||_X^2`.

- Si `mathcal Rv=0`, le profil a un stabilisateur infinitésimal continu. Toute
  vitesse tangentielle donne le même vecteur nul; le choix `beta=0` est une
  convention et non un minimiseur identifiable.
- Si `||mathcal Rv||_X` est petit mais non nul, `beta` peut être arbitrairement
  grand, tandis que le produit projeté `beta mathcal Rv` reste contractif.
- Un stabilisateur fini non trivial ne force pas `mathcal Rv=0`. Il crée une
  ambiguïté globale de phase, non une dégénérescence infinitésimale automatique.
- Un Gram croisé de tranche fixe peut s'annuler alors que
  `mathcal Rv!=0`; c'est le mécanisme de frontière de carte documenté par
  Rowley--Marsden et Willis--Cvitanović--Avila.

La proposition 2.10 de Beyn--Thümmler fournit une condition suffisante de
non-dégénérescence pour leurs conditions fixes. Elle ne donne aucune constante
uniforme le long d'une suite qui approche un stabilisateur.

## 6. Régularité temporelle : contre-test exact

La projection bornée ne rend pas `beta` intégrable. Dans `H=R e_1`, sur
`s in (0,1)`, prendre

```text
g(s)=s^2 e_1,    d(s)=s e_1.
```

Alors `d` et `g` sont bornés et fortement mesurables,

```text
beta(s)=1/s,
beta(s)g(s)=s e_1,
r(s)=0.
```

Toutes les identités `(P59)` sont satisfaites, mais
`beta notin L^1(0,1)`. Il n'existe donc pas de phase absolument continue sur
`[0,1]` ayant cette dérivée. Ce contre-test réfute tout passage automatique

```text
projection instantanée + borne sur d  =>  phase reconstruite AC.
```

## 7. Dépendance à la métrique : contre-test exact

Dans `H=R^2`, poser `g=e_1`, `d=e_1+e_2` et choisir le produit scalaire de
matrice

```text
M_rho=[[1,rho],[rho,1]],    |rho|<1.
```

Alors

```text
beta_M=<d,g>_M/||g||_M^2=1+rho.
```

La vitesse change avec la métrique, même si les vecteurs `d` et `g` ne
changent pas. Le qualificatif « canonique » du cycle 0059 signifie donc
uniquement « projection unique pour le Hilbert pondéré fixé »; il n'est pas
invariant sous le choix des poids, de la fenêtre ou du produit local.

## 8. Pression et dual solénoïdal

Pour Navier--Stokes, la dérivée complète contient `-nabla Pi`. Un produit
`H^-3` local construit arbitrairement puis moyenné sous `SO(2)` n'est pas
automatiquement compatible avec la décomposition de Helmholtz. Il peut exister
un champ divergence-free `g` et un gradient `h=nabla q` tels que

```text
<h,g>_X!=0.
```

Remplacer `d` par `d+h` modifie alors `beta`. La moyenne rotationnelle rend le
produit invariant sous `SO(2)`; elle ne rend pas gradients et champs
solénoïdaux orthogonaux.

Deux routes sont possibles, et aucune n'est fournie par les sources de phase :

1. conserver l'équation vectorielle complète et une pression globalement
   jauge-fixée, auquel cas `beta` est défini mais dépend de ce choix métrique;
2. travailler dans un dual solénoïdal compatible avec Leray, auquel cas la
   pression disparaît mais la conclusion locale peut être seulement modulo un
   gradient harmonique, sauf fermeture globale supplémentaire.

La norme de Bessel homogène ou inhomogène sur l'espace entier peut être rendue
compatible avec le projecteur de Leray, mais les profils locaux du cycle ne
sont pas assurés d'avoir une norme globale finie. C'est une dette analytique,
pas un détail de présentation.

## 9. Absence de transfert au problème Clay

Les trois sources auditées ne fournissent aucune des implications suivantes :

```text
singularité Type I de Navier--Stokes
  => ess inf_J |beta_n| -> infinity;

projection tangentielle
  => moyenne de Haar du résidu -> 0;

projection H^-3
  => stabilité de l'inégalité locale d'énergie;

réduction numérique dans un tuyau
  => solution suitable non triviale sur R3 ou T3;

axisymétrie d'une limite
  => régularité globale avec swirl.
```

Beyn--Thümmler et Rowley--Marsden sont des théories classiques lisses de
réduction/reconstruction. Willis--Cvitanović--Avila étudient Navier--Stokes,
mais avec viscosité `1/Re`, forçage à débit imposé, bord sans glissement,
périodicité axiale, symétrie imposée et discrétisation finie. Cette équation et
cette notion de trajectoire ne sont pas les alternatives officielles de Clay
sur `R3` ou `T3`.

Même si `(P59)` est correct, le saut vers Clay requerrait encore au minimum :

- la compacité forte nécessaire au terme quadratique;
- le contrôle de la pression et de sa jauge sous localisation;
- la stabilité de la suitability et de l'inégalité locale d'énergie;
- la non-trivialité/capture de la limite;
- une hypothèse ou un théorème imposant l'effondrement tangentiel;
- un théorème de rigidité axisymétrique pertinent avec swirl, ou la
  stationnarité obtenue par décroissance du résidu de Haar.

## 10. Sources à cataloguer ultérieurement

Sans modifier `sources.json` dans ce cycle, le delta bibliographique utile est
le suivant :

1. ajouter Rowley--Marsden 2000 comme antécédent primaire de la connexion
   mécanique, des tranches locales et des frontières de carte;
2. ajouter Willis--Cvitanović--Avila 2013 comme antécédent Navier--Stokes
   numérique direct, en conservant explicitement les limites tuyau/forçage/
   symétrie/discrétisation;
3. ne pas dupliquer Beyn--Thümmler 2004 (`NS-SRC-0209`) ni Rowley--Kevrekidis--
   Marsden--Lust 2003 (`NS-SRC-0210`); enrichir seulement leur audit si le
   schéma le permet.

## 11. Résultat scientifique de la revue

Le statut correct du lemme actif est :

```text
projection orthogonale instantanée dans le Hilbert X fixé
  = antécédent classique confirmé;

extension au Hilbert H^-3 pondéré du ledger
  = dérivation interne plausible, à vérifier comme lemme fonctionnel;

reconstruction d'une phase temporelle
  = non démontrée et fausse sans intégrabilité supplémentaire de beta;

transfert suitable/pression/Clay
  = absent.
```

Le test décisif pour le cycle suivant n'est donc pas de réétablir les
équations normales. Il doit déterminer si l'équation renormalisée complète et
la pression jauge-fixée donnent un contrôle vérifiable de
`partial_s A Z_n=A r_n` (où `A` est la moyenne de Haar), ou produire un
contre-profil PDE compatible avec tout le ledger montrant que ce contrôle est
impossible sans hypothèse asymptotique supplémentaire.

