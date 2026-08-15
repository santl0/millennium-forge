# Cycle 0061 — revue primaire indépendante de la formule modale

Date de gel : 2026-08-15.

Statut : audit bibliographique indépendant. Aucune nouvelle affirmation de
régularité, de singularité ou de résolution du problème Clay.

## Question auditée

Le cycle 0061 décompose, dans un Hilbert réel `X` portant une action unitaire
de `SO(2)`, la vitesse de phase projetée

```text
d=partial_s Z,                 g=mathcal R Z,
beta=<d,g>_X/||g||_X^2.                                  (A61.1)
```

Après complexification et décomposition en caractères `+/-k`, il obtient

```text
G_k=2 k^2||Z_k||^2,
C_k=2 Re<d_k,ikZ_k>,
b_k=C_k/G_k,
beta=(sum_k G_k b_k)/(sum_k G_k).                         (A61.2)
```

Pour une repondération scalaire positive des blocs isotypiques,

```text
beta_lambda
 =(sum_k lambda_k G_k b_k)/(sum_k lambda_k G_k),          (A61.3)
```

d'où l'enveloppe convexe des vitesses modales et le contre-modèle métrique du
rapport principal.

L'audit cherche quelles parties de `(A61.2)--(A61.3)` sont écrites dans des
sources primaires, lesquelles ne sont que des conséquences de théorie de la
représentation ou de la connexion mécanique, et si un article récent sur les
profils Navier--Stokes rotatoirement auto-similaires fournit le raccord PDE
manquant.

## Verdict

Une source primaire contient presque littéralement la formule modale finie :
Fedele--Abessi--Roberts 2015, équations (4.17), (4.20)--(4.23). Pour une série
de Fourier scalaire périodique, les auteurs écrivent la tangente de groupe

```text
T(z)_m=i m k_0 z_m
```

et la vitesse de connexion

```text
U_d=Re(overline(T(z)) dot z_t)/|T(z)|^2.                  (FAR-1)
```

Ils donnent aussi explicitement

```text
|T(z)|^2=sum_m m^2 k_0^2 |z_m|^2                        (FAR-2)
```

et le numérateur modal. Si `z_m=a_m exp(i theta_m)`, `(FAR-1)` devient

```text
U_d=
 [sum_m m^2 k_0^2 a_m^2 {theta_m'/(m k_0)}]
 /[sum_m m^2 k_0^2 a_m^2].                              (FAR-3)
```

C'est exactement une moyenne des vitesses du paramètre de groupe, pondérée
par les Grams tangentiels. À une convention de signe, d'action et de produit
hermitien près, `(FAR-3)` est l'analogue fini de `(A61.2)`.

La portée est néanmoins strictement plus faible que celle visée au cycle :
le champ analysé est une concentration scalaire mesurée dans un tuyau,
tronquée à `N` modes, avec produit standard. Le papier ne traite ni le Hilbert
local `H^-3`, ni une solution faible adaptée, ni la pression, ni une limite de
blow-up.

Les autres antécédents se complètent sans qu'aucun ne contienne seul tout le
lemme :

- Budanur--Cvitanovic--Davidchack--Siminos donne exactement l'action réelle
  bloc-diagonale `diag(R(theta),R(2theta),...)` et ses générateurs `kJ`;
- Peter--Weyl et, dans un Hilbert concret, Hadani--Singer donnent la
  décomposition isotypique;
- Rowley--Marsden donne la connexion mécanique à Gram courant;
- Beyn--Thümmler donne les équations normales de la condition de phase
  adaptative dans un Hilbert;
- Fedele--Abessi--Roberts assemble connexion, Fourier et dépendance au produit
  scalaire dans le cas fini scalaire.

En revanche, aucune source localisée ne démontre dans le cadre exact du cycle
les facteurs réels `+/-k`, le domaine du générateur sur la somme hilbertienne,
la convergence infinie, les métriques agissant dans les espaces de
multiplicité, l'enveloppe convexe métrique ou le critère de signe modal. Ces
éléments doivent rester `AI_INTERNAL_DERIVATION`, même s'ils sont des
conséquences naturelles de résultats classiques.

La veille 2025--2026 ne fournit pas le raccord manquant. Pineau--Vicol v2
prouve une rigidité substantielle pour des profils RSS **exacts** à vitesse
constante sous borne Type I, lorsque la rotation est assez petite ou assez
grande. Il ne définit pas une phase adaptative par `(A61.1)`, ne prouve pas la
cohérence de signe des `b_k` et ne traite pas une métrique `H^-3` choisie par
le cycle.

## 1. Matrice de soutien exact

| composante du cycle 0061 | source primaire la plus proche | niveau de soutien | manque restant |
|---|---|---|---|
| action du caractère `k` et générateur `kJ` | Budanur et al. (2), (5), (6) | **exact**, troncature Fourier réelle | action covariante de champs vectoriels sur `R3` |
| somme isotypique d'un Hilbert unitaire `SO(2)` | Peter--Weyl; Hadani--Singer (3.1) | **exact comme structure abstraite** | paire réelle, domaine du générateur et norme `H^-3` du cycle |
| projection `beta=<d,g>/||g||^2` | Rowley--Marsden (B.2)--(B.4); Beyn--Thümmler (2.30)--(2.33) | **exact** dans un cadre lisse hilbertien | faiblesse temporelle, pression, suitability |
| numérateur et dénominateur modaux | Fedele et al. (4.20)--(4.23) | **exact**, fini, scalaire, périodique | multiplicité, modes infinis et champ vectoriel covariant |
| dépendance au produit scalaire | Fedele et al. (4.17), texte après (4.25); Willis et al. | **explicite** | aucune classification de toutes les métriques invariantes |
| moyenne pondérée `(A61.3)` | conséquence immédiate de Fedele (4.17), (4.20)--(4.23) | **dérivable**, non énoncée comme théorème | admissibilité/topologie des poids infinis |
| enveloppe convexe et critère de signe | aucune source localisée | **dérivation interne** | revue mathématique autonome requise |
| modulation PDE près d'une orbite relative | Beyn--Thümmler; Sandstede--Scheel--Wulff | **arrière-plan abstrait** | pas de solution suitable, pas de blow-up |
| grande rotation `=>` déplétion axisymétrique | Pineau--Vicol v2, cas RSS exact | **exact sous ansatz RSS et Type I** | aucune phase projetée, aucun scénario Type I général |

Le statut bibliographique correct de `(A61.2)` est donc : **formule classique
finie confirmée, extension hilbertienne exacte mais composée de plusieurs
antécédents**. La robustesse métrique et son contre-modèle ne doivent pas être
attribués à ces articles.

## 2. Fedele--Abessi--Roberts 2015 : formule modale la plus proche

### Source, version et statut

- Francesco Fedele, Ozeair Abessi et Philip J. Roberts, *Symmetry reduction
  of turbulent pipe flows*, Journal of Fluid Mechanics 779, 390--410
  (2015), DOI
  [10.1017/jfm.2015.423](https://doi.org/10.1017/jfm.2015.423),
  [arXiv:1412.6711v3](https://arxiv.org/abs/1412.6711).
- Soumission v1 : 2014-12-21; v3 : 2015-07-05; article publié et évalué par
  les pairs.
- Empreinte du PDF v3 contrôlé :
  `SHA256 BDE9DA7138FA673E736868495B7DFBFF2469DC9ADBC7E8E604599DE45447C034`.
- Les pages PDF 3 et 10--13, dont les équations (2.5), (2.8),
  (4.3)--(4.5), (4.17) et (4.20)--(4.25), ont été contrôlées; les pages
  12--13 ont aussi été rendues visuellement.

### Équation et objet réellement étudiés

Le cadre physique est un champ de vitesse incompressible tridimensionnel
`v_0=(U_0,V_0,W_0)` dans un tuyau à paroi sans glissement. Le champ de vitesse
est supposé satisfaire Navier--Stokes, mais il n'est pas reconstruit. L'objet
mesuré est le scalaire passif

```text
partial_t C_0+v_0 dot nabla C_0
 =D_m Delta C_0+f_0.                                      (FAR-4)
```

L'application est une mesure LIF bidimensionnelle de concentration dans un
tuyau turbulent à nombre de Reynolds 3200. Elle n'est ni une solution
Navier--Stokes sur `R3` ou `T3`, ni un calcul validé, ni une preuve de
continuum.

Pour le développement périodique unidimensionnel

```text
c(x,t)=c_0(t)+sum_(m=1)^N z_m(t) exp(i m k_0 x)+conjugue,
```

la translation de longueur `ell` agit par

```text
g_ell(z)_m=z_m exp(i m k_0 ell).                            (4.3)
```

Le choix d'un mode non nul `z_j` donne une tranche de Fourier; le bord de
tranche est `z_j=0`. La première tranche de Fourier est le cas `j=1`.

### Connexion, formule modale et métrique

La tangente d'orbite est

```text
T(Z)_m=i m k_0 Z_m.                                        (4.12)
```

Les auteurs autorisent dans (4.17) un produit hermitien pondéré par une
matrice `W=W*`. Ils choisissent ensuite le produit standard. La condition de
transversalité fournit

```text
U_d=Re(overline(T(z)) dot z_t)/|T(z)|^2.                   (4.20)
```

Parseval donne les identités modales

```text
<|partial_x c|^2>_x
 =sum_(m=1)^N m^2 k_0^2 |z_m|^2=|T(z)|^2,                 (4.21)

<partial_t c partial_x c>_x
 =Re sum_(m=1)^N i m k_0 conjugate(z_m) z_m'
 =-Re(overline(T(z)) dot z_t),                            (4.22)

U_d=-<partial_t c partial_x c>_x/<|partial_x c|^2>_x.     (4.23)
```

Ces équations soutiennent exactement le calcul modal de `(A61.2)` dans une
troncature. Pour `z_m=a_m exp(i theta_m)`, le terme modal du numérateur vaut
`m k_0 a_m^2 theta_m'`; sa vitesse du paramètre de groupe est
`theta_m'/(m k_0)`, et son poids de Gram est `m^2 k_0^2 a_m^2`.

Le texte suivant (4.25) dit explicitement que des produits scalaires
différents peuvent filtrer les grandes ou petites échelles et produire des
représentations de tranche différentes. C'est un soutien primaire direct à
la dépendance métrique. Il ne contient cependant ni l'enveloppe convexe de
tous les poids positifs, ni le critère nécessaire et suffisant de cohérence
de signe du cycle 0061.

### Non-transfert explicite

Cette source ne démontre aucune implication du type

```text
solution Type I suitable de Navier--Stokes
 => formule modale dans H^-3
 => cohérence de signe des vitesses modales
 => axisymétrie ou régularité.
```

La formule est exacte comme identité de connexion/Fourier. L'expérience LIF,
la paroi, le scalaire passif, le nombre fini de modes et la norme standard
interdisent de la citer comme résultat sur la formulation Clay.

## 3. Budanur--Cvitanovic--Davidchack--Siminos 2015

### Source et statut

- Nazmi Burak Budanur, Predrag Cvitanovic, Ruslan L. Davidchack et Evangelos
  Siminos, *Reduction of SO(2) symmetry for spatially extended dynamical
  systems*, Physical Review Letters 114, 084102 (2015), DOI
  [10.1103/PhysRevLett.114.084102](https://doi.org/10.1103/PhysRevLett.114.084102),
  [arXiv:1405.1096v4](https://arxiv.org/abs/1405.1096).
- v1 : 2014-05-05; v4 : 2015-01-16; article publié.
- Empreinte du PDF contrôlé :
  `SHA256 98D470842E6F5E80CB2AF76DDBB23A050D5979A0EB0D10CB7DB20CE43AECA2E1`.

### Ce que la source soutient exactement

Pour une fonction périodique scalaire,

```text
u_tilde_k -> u_tilde_k exp(i k theta),                     (2)
```

et, dans la représentation réelle tronquée,

```text
D(theta)=diag[R(theta),R(2theta),...,R(m theta)],           (5)
T_k=[[0,-k],[k,0]].                                         (6)
```

Ces formules sont l'antécédent direct des blocs réels `kJ` et des facteurs
`k^2` du Gram. Elles montrent aussi que le mode zéro est fixe.

La reconstruction du papier utilise toutefois une **tranche à gabarit
fixe** :

```text
theta'= <v(a_hat),t_template>/<t(a_hat),t_template>.         (9)
```

Ce Gram croisé n'est pas le Gram courant de `(A61.1)`. La première tranche
de Fourier fixe la phase du seul premier mode et devient singulière lorsque
son amplitude s'annule; elle ne calcule pas une moyenne mécanique sur tous
les modes. La régularisation par changement de temps ne supprime pas le bord
`z_1=0` et ne donne aucune borne faible PDE.

L'application démonstrative est Kuramoto--Sivashinsky unidimensionnelle,
tronquée à quinze modes. L'article mentionne l'emploi dans des codes de
fluides périodiques, mais cela n'est pas un théorème de régularité
Navier--Stokes.

## 4. Décomposition isotypique : source exacte et limites

### Peter--Weyl

- Fritz Peter et Hermann Weyl, *Die Vollständigkeit der primitiven
  Darstellungen einer geschlossenen kontinuierlichen Gruppe*, Mathematische
  Annalen 97, 737--755 (1927), DOI
  [10.1007/BF01447892](https://doi.org/10.1007/BF01447892).
- Statut : article fondateur publié.

Le théorème de Peter--Weyl est l'antécédent général de la somme hilbertienne
orthogonale des types irréductibles d'un groupe compact. Pour `SO(2)`
complexe, les irréductibles sont les caractères `exp(i k theta)`.

Cette référence ne doit pas être sur-citée : elle ne formule pas le lemme du
cycle dans le Hilbert pondéré `H^-3`, ne donne pas la vitesse projetée et ne
traite pas les métriques variables. Les projecteurs explicites, la paire
réelle `+/-k` et le domaine

```text
sum_k k^2||Z_k||^2<infinity
```

sont des conséquences de Peter--Weyl et de la théorie du générateur
unitaire, pas un théorème Navier--Stokes de cet article.

### Hadani--Singer : une occurrence moderne explicite

- Ronny Hadani et Amit Singer, *Representation Theoretic Patterns in
  Three-Dimensional Cryo-Electron Microscopy II--The Class Averaging
  Problem*, Foundations of Computational Mathematics 11(5), 589--616
  (2011), DOI
  [10.1007/s10208-011-9095-3](https://doi.org/10.1007/s10208-011-9095-3),
  [arXiv:1104.1131v1](https://arxiv.org/abs/1104.1131).
- Statut : article publié; v1 du 2011-04-06.

L'équation (3.1) écrit explicitement, pour un Hilbert complexe concret de
fonctions sur le fibré des repères,

```text
H=direct_sum_(k in Z) H_k,
s in H_k iff s(x g)=g^k s(x).                              (HS-1)
```

La source confirme donc exactement le langage isotypique complexe. Elle ne
porte ni sur un Hilbert réel de champs de vitesse, ni sur le générateur
non borné, ni sur la projection de phase. Sa propriété de multiplicité un
est spécifique à la représentation cryo-EM supplémentaire `SO(3)`; elle ne
peut surtout pas être transférée aux champs sur `R3`, où les multiplicités
radiales, axiales et vectorielles sont généralement infinies.

### Conclusion de portée

Le passage

```text
decomposition complexe H_C=sum_(k in Z)H_k
 -> blocs reels H_0 plus sum_(k>=1)H_k^R
 -> mathcal R=kJ_k
 -> ||mathcal R Z||^2=sum k^2||Z_k||^2
```

est mathématiquement standard et falsifiable, mais il est composé de
théorie de la représentation et de théorie des groupes unitaires. Aucun
papier localisé ne l'énonce avec les conventions, les facteurs deux et la
topologie précise du cycle 0061. Le statut `AI_INTERNAL_DERIVATION` de cette
instanciation est approprié.

## 5. Connexion mécanique, freezing et métrique

### Rowley--Marsden 2000

- Clarence W. Rowley et Jerrold E. Marsden, *Reconstruction Equations and
  the Karhunen--Loeve Expansion for Systems with Symmetry*, Physica D
  142(1--2), 1--19 (2000), DOI
  [10.1016/S0167-2789(00)00042-7](https://doi.org/10.1016/S0167-2789(00)00042-7).
- Source cataloguée : `NS-SRC-0220`; article publié.
- PDF contrôlé au cycle 0059 :
  `SHA256 4E43B93161EA08FFEFBB2AC67706B8157D40681C2997E62F41EE93C1A82B08C0`.

L'annexe B définit la connexion mécanique

```text
A(v_u)=I(u)^(-1)J(v_u),                                   (B.1)
```

où `I(u)` est la matrice de Gram des tangentes de groupe. Pour une action à
un paramètre,

```text
A(v_u)=<<v_u,u'>>/<<u',u'>>.                              (B.2)
```

C'est exactement `(A61.1)` dans une métrique riemannienne fixée. Le papier
ne fournit pas sa décomposition en caractères et suppose une action lisse,
libre et propre. Il ne couvre pas le stabilisateur, les distributions
`H^-3` ou les solutions faibles adaptées.

### Beyn--Thümmler 2004

- Wolf-Jurgen Beyn et Volker Thümmler, *Freezing Solutions of Equivariant
  Evolution Equations*, SIAM Journal on Applied Dynamical Systems 3(2),
  85--116 (2004), DOI
  [10.1137/030600515](https://doi.org/10.1137/030600515).
- Source cataloguée : `NS-SRC-0209`; article publié.
- PDF contrôlé :
  `SHA256 240522FAE2761F879B7E406D62D5337EF06C271F10E88D72BA1D11455D60909D`.

La condition adaptative minimise

```text
||F(v)-S(v,gamma)lambda||^2                              (2.30)
```

et donne les équations normales

```text
(S* S)lambda=S*F(v).                                     (2.33)
```

Pour une action unitaire à un paramètre, c'est `(A61.1)`. Cette source
confirme l'origine hilbertienne du quotient, mais pas ses sommes isotypiques.
Elle signale aussi que son théorème de reconstruction par fonction implicite
ne s'applique pas automatiquement à la condition adaptative, car celle-ci
dépend de `lambda=gamma_t`. Une ODE et des hypothèses classiques de
continuité/Lipschitz sont nécessaires.

### Dépendance à la métrique

La dépendance n'est pas une découverte bibliographique nouvelle :

- Rowley--Marsden définit la connexion à partir de la métrique choisie;
- Beyn--Thümmler minimise dans la norme hilbertienne choisie;
- Fedele et al. introduit explicitement une matrice hermitienne `W` en
  (4.17) et indique que changer le produit filtre différemment les échelles;
- Willis--Cvitanovic--Avila 2013, `NS-SRC-0221`, utilise une norme d'énergie
  pour le pipe flow et dit que ce choix dépend de l'application.

Aucune de ces sources ne prouve que deux métriques invariantes uniformément
équivalentes donnent la même vitesse. Le contre-modèle du cycle 0061 est donc
compatible avec la littérature et réfute précisément une invariance que les
sources ne revendiquent pas.

## 6. Tranche fixe, première phase de Fourier et connexion mécanique

Trois constructions voisines ne doivent pas être identifiées :

1. une tranche à gabarit fixe donne un **Gram croisé** entre tangente
   courante et tangente du gabarit;
2. la première tranche de Fourier fixe la phase d'un **seul mode** et échoue
   lorsque ce mode s'annule;
3. la connexion mécanique/adaptative projette sur la **tangente courante**
   et somme tous les modes dans la métrique choisie.

Budanur et al. et Willis--Cvitanovic--Avila documentent principalement les
deux premières constructions. Rowley--Marsden (annexe B), Beyn--Thümmler
(2.30)--(2.33) et Fedele et al. (4.20) soutiennent la troisième.

Une divergence de vitesse de tranche peut donc avoir deux causes distinctes
:

```text
Gram croise -> 0     : frontiere de carte;
||mathcal R Z|| -> 0 : approche du stabilisateur pour la connexion courante.
```

Les sources ne donnent aucune constante uniforme séparant ces Grams de zéro
le long d'une suite de blow-up.

## 7. Modulation dans les PDE : seulement un arrière-plan classique

### Sandstede--Scheel--Wulff 1997

- Bjorn Sandstede, Arnd Scheel et Claudia Wulff, *Dynamics of spiral waves
  on unbounded domains using center-manifold reductions*, Journal of
  Differential Equations 141(1), 122--149 (1997), DOI
  [10.1006/jdeq.1997.3326](https://doi.org/10.1006/jdeq.1997.3326).
- Statut : article publié.

L'article développe une réduction de variété centrale équivariante près
d'équilibres relatifs pour des semi-flots sur des espaces de Banach, puis
l'applique aux ondes spirales de réaction--diffusion. Il est pertinent pour
le dictionnaire « profil + paramètres de groupe + dynamique réduite », y
compris lorsque l'action euclidienne est techniquement peu régulière.

Il ne soutient pas `(A61.2)` : il n'énonce pas la connexion mécanique modale,
ne considère pas les solutions faibles adaptées de Navier--Stokes et repose
sur une structure locale de variété centrale, des hypothèses spectrales et
une régularité semi-linéaire absentes du scénario Clay.

### Portée générale

La littérature de modulation justifie qu'une phase doit être fixée par une
condition transverse et que sa reconstruction exige davantage qu'une
identité instantanée. Elle ne permet pas le passage

```text
projection mesurable dans H^-3
 => phase AC
 => solution modulee classique
 => rigidite de blow-up.
```

La dette `beta in L1_loc` et la compatibilité de la pression avec la métrique
locale restent entièrement hors des théorèmes audités.

## 8. Veille différentielle Navier--Stokes RSS/rotation 2025--2026

### Pineau--Vicol v2 : résultat primaire pertinent

- Ben Pineau et Vlad Vicol, *On rotated backwards self-similar solutions of
  the incompressible 3D Navier-Stokes equations*,
  [arXiv:2607.09619v2](https://arxiv.org/abs/2607.09619).
- v1 : 2026-07-10; v2 : 2026-08-06, « additional results and comments
  added »; 37 pages; prépublication, aucun DOI de revue identifié au gel.
- Source cataloguée : `NS-SRC-0051`.
- Empreinte du PDF v2 contrôlé :
  `SHA256 379591AA3C1036C9140702EBE71AAAB309FE207439A57DB5CEFF893F15D0AE8E`.

L'équation est Navier--Stokes incompressible standard, non forcée, viscosité
un, sur `R3 x [-1,0)`. Pour la rotation `R(s)` autour d'un axe et son
générateur matriciel `J`, l'ansatz RSS backward est

```text
u(x,t)=(-t)^(-1/2) R(alpha s)
       U(R(-alpha s)x/sqrt(-t)),
s=-log(-t).                                                (1.7)
```

Le profil lisse stationnaire satisfait

```text
alpha [JU-(Jy dot nabla)U]
 +1/2 U+1/2(y dot nabla)U-Delta U
 +(U dot nabla)U+nabla P=0,
div U=0.                                                   (1.8)
```

Le générateur covariant pertinent pour les champs vectoriels est donc

```text
mathcal R U=JU-(Jy dot nabla)U,                            (PV-1)
```

et non le numéro de Fourier de chaque composante cartésienne prise
séparément. Cette formule soutient la convention de l'action covariante du
cycle 0061.

Le théorème 1.4 impose la borne Type I

```text
|u(x,t)|<=C/(|x|+sqrt(-t))
```

et l'ansatz RSS global exact. Il conclut `U=0` lorsque `|alpha|` est assez
petit ou assez grand, les seuils dépendant de `C`. Le régime intermédiaire
reste ouvert. Pour `|alpha|` grand, les auteurs contrôlent directement une
norme pondérée de `mathcal R U` par l'équation stationnaire et obtiennent une
petitesse plus forte que `O(1/alpha)` avec un poids uniforme en `alpha`.

Les théorèmes 1.6--1.7 traitent DSS/RDSS lorsque la période similaire est
petite, donc lorsque le facteur de dilatation est proche de un, avec des
hypothèses quantitatives supplémentaires. Le théorème 1.9 donne un critère
local de régularité sous borne Type I et quasi-auto-similarité à une tranche
temporelle, avec contrôle de pression loin du centre.

### Ce qui ne se transfère pas au cycle 0061

Dans Pineau--Vicol, `alpha` est un paramètre constant imposé par un ansatz
RSS exact. Il n'est ni obtenu par minimisation, ni dépendant de la métrique,
ni égal à une moyenne de vitesses modales concurrentes. Le terme
`alpha mathcal R U` appartient à l'équation de profil elle-même; c'est cette
structure PDE, combinée à la stationnarité et aux poids adjoints, qui produit
la déplétion axisymétrique.

Le papier ne démontre donc aucune implication

```text
essinf |beta_n^X| -> infinity pour une projection H^-3
 => ansatz RSS exact de parametre alpha=beta_n
 => petitesse uniforme de mathcal R Z_n.
```

Il ne prouve pas davantage la cohérence de signe des vitesses `b_k` du cycle
0061. Son résultat indique plutôt la donnée structurelle manquante : une
grande vitesse devient coercive lorsqu'elle est un coefficient exact de
l'équation stationnaire RSS, pas lorsqu'elle est seulement le quotient d'une
projection arbitraire.

### Bradshaw--Tsai 2017 : antécédent publié, pas annonce récente

- Zachary Bradshaw et Tai-Peng Tsai, *Rotationally Corrected Scaling
  Invariant Solutions to the Navier--Stokes Equations*, Communications in
  Partial Differential Equations 42(7), 1065--1087 (2017), DOI
  [10.1080/03605302.2017.1323922](https://doi.org/10.1080/03605302.2017.1323922),
  [arXiv:1610.05680v1](https://arxiv.org/abs/1610.05680).
- Source cataloguée : `NS-SRC-0206`; article publié.
- PDF contrôlé :
  `SHA256 DE297541695B1E52AEE702930F8C5F723EFFC5DB13FA208B80CBAD7EFEE47C52`.

Cette source construit des solutions **forward** RSS/RDSS pour des données
critiques potentiellement grandes dans l'espace entier et le demi-espace.
Elle soutient l'équation en repère tournant et la phase logarithmique à
vitesse constante. Elle ne fournit ni blow-up backward, ni phase adaptative,
ni rigidité d'une ancienne solution suitable.

### Négatifs explicites de la veille

Les recherches primaires ciblées sur arXiv et les éditeurs, avec les termes
`Navier-Stokes`, `rotated self-similar`, `rotationally self-similar`, `RSS`,
`RDSS`, `rotation`, `phase` et les années 2025--2026, n'ont localisé au gel
aucune autre annonce qui :

- démontre la formule `(A61.2)` dans un Hilbert faible de profils Type I;
- dérive une phase métriquement robuste depuis une solution suitable;
- traite le régime RSS backward à rotation intermédiaire;
- transforme une phase projetée variable en ansatz RSS/RDSS exact;
- fournisse un calcul assisté par ordinateur certifié sur cette question.

Ce résultat de veille est négatif et borné aux requêtes effectuées; ce n'est
pas une preuve d'absence dans toute la littérature.

La révision v3 du 2026-08-08 de Seregin,
[arXiv:2402.13229v3](https://arxiv.org/abs/2402.13229), est voisine par la
date et les scénarios Type II axisymétriques, mais sa limite est une solution
ancienne dissipative d'Euler sans swirl sous hypothèses supplémentaires.
Elle ne traite ni RSS, ni une phase `SO(2)`, ni `(A61.2)`.

Enfin, les articles sur les équations de fluides en rotation avec terme de
Coriolis (`NS-SRC-0211` et `NS-SRC-0212`) ne portent pas sur une rotation de
profil dans le temps similaire. « Navier--Stokes tournant » et « profil RSS »
sont des équations différentes et aucune implication ne doit être inférée
du vocabulaire commun.

## 9. Multiplicité, réalité et produit scalaire : points adversariaux

### Modes `+k` et `-k`

Pour un champ réel, les caractères complexes satisfont

```text
Z_(-k)=conjugate(Z_k).
```

Ils constituent un seul bloc réel, pas deux degrés de liberté métriques
indépendants. Budanur et al. utilise directement le bloc réel `R(k theta)`;
Fedele et al. travaille avec un champ réel reconstruit à partir des modes
complexes. Ces sources soutiennent les facteurs de paire, mais ne fixent pas
les conventions de norme du cycle. Les facteurs deux doivent donc être
recalculés, comme dans `(A61.2)`, et non copiés aveuglément.

### Multiplicité interne

Dans un champ vectoriel tridimensionnel sur `R3`, un caractère azimutal fixé
contient encore les variables radiale et axiale, les composantes du champ et
les degrés de liberté solénoïdaux. La multiplicité est généralement infinie.
Une métrique invariante peut agir par un opérateur positif non scalaire sur
cet espace de multiplicité tout en commutant avec `SO(2)`.

Aucune source auditée ne réduit toutes ces métriques aux poids scalaires
`lambda_k`. L'enveloppe convexe scalaire du cycle est donc :

- suffisante pour produire un contre-exemple à toute robustesse plus large;
- insuffisante pour caractériser toutes les métriques invariantes;
- sans portée PDE tant que `d` n'est pas contraint par Navier--Stokes.

### Topologie et domaine

Une suite arbitraire de poids positifs peut changer la topologie du Hilbert.
Les articles finis ne rencontrent pas cette question. Sur une somme infinie,
il faut conserver au minimum

```text
sum lambda_k||d_k||^2<infinity,
0<sum lambda_k k^2||Z_k||^2<infinity.
```

Pour une norme équivalente uniforme, des bornes
`0<c<=lambda_k<=C<infinity` suffisent. Sans ces bornes, `(A61.3)` peut être
formellement calculable sur des sommes partielles tout en ne définissant pas
le même espace fonctionnel.

### Pression

La décomposition `SO(2)` commute avec la pression de Riesz globale lorsque
l'action covariante et l'espace entier sont utilisés correctement. Cela ne
rend pas pour autant tout produit `H^-3` local compatible avec le projecteur
de Leray. Aucun article de phase audité ne prouve l'orthogonalité des
gradients et des champs solénoïdaux dans la métrique locale du cycle.

Ainsi les numérateurs `C_k` peuvent changer sous une modification de jauge
ou de localisation si la métrique n'est pas construite sur le dual
solénoïdal global. Fedele et al. évite entièrement cette difficulté en
projetant un scalaire observé.

## 10. Absence de transfert au problème Clay

Les sources auditées n'établissent aucune des arêtes suivantes :

```text
singularite Type I de Navier--Stokes sur R3 ou T3
  => limite suitable non triviale dans le Hilbert du cycle;

limite suitable
  => decompositions temporelles d_k et Z_k compatibles avec la pression;

grande beta pour une metrique epinglee
  => meme signe et meme taille pour tous les b_k;

coherence des b_k
  => residu orthogonal petit ou orbite RSS exacte;

projection modale
  => preservation de l'inegalite locale d'energie;

axisymetrie de la limite
  => regularite globale en presence de swirl.
```

Pineau--Vicol exclut une sous-classe structurée de profils Type I, mais
n'exclut ni tout Type I, ni le régime RSS intermédiaire, ni Type II, ni toute
solution ancienne. Exclure RSS/RDSS ne suffit pas à exclure un blow-up Clay
général.

La formule `(A61.2)` est cinématique. Le verrou analytique reste de déduire
de l'équation renormalisée soit une cohérence modale intrinsèque, soit un
défaut d'axisymétrie indépendant du produit scalaire. Aucun des articles
audités ne fournit ce lemme.

## 11. Delta bibliographique recommandé, sans modification du catalogue

À ajouter ultérieurement à `sources.json`, sous revue séparée :

1. **priorité haute** — Fedele--Abessi--Roberts 2015, comme antécédent exact
   du quotient modal, de la connexion en Fourier et de la dépendance au
   produit scalaire; limites obligatoires : scalaire passif, tuyau, données
   LIF, troncature, non certifié;
2. **priorité haute** — Budanur--Cvitanovic--Davidchack--Siminos 2015, comme
   antécédent de l'action réelle `SO(2)`, du générateur `kJ`, de la première
   tranche de Fourier et de sa singularité;
3. **priorité moyenne** — Peter--Weyl 1927, comme source fondatrice de la
   décomposition isotypique, sans lui attribuer les formules `H^-3`;
4. **priorité basse** — Hadani--Singer 2011, seulement si le catalogue veut
   une occurrence moderne explicite de `H=direct_sum H_k`; l'application
   cryo-EM n'ajoute aucun transfert Navier--Stokes;
5. **priorité basse** — Sandstede--Scheel--Wulff 1997, comme arrière-plan de
   modulation PDE près d'équilibres relatifs, avec étiquette
   `adjacent_framework`.

Ne pas dupliquer `NS-SRC-0206`, `NS-SRC-0209`, `NS-SRC-0220`,
`NS-SRC-0221` ou `NS-SRC-0051`.

## 12. Résultat scientifique de la revue

Le statut bibliographique et logique à conserver est

```text
action modale SO(2), generateur kJ
  = antecedent primaire exact;

connexion mecanique beta=<d,RZ>/||RZ||^2
  = antecedent primaire exact;

formule modale finie et poids de Gram
  = antecedent primaire presque litteral chez Fedele et al.;

extension reelle infinie H^-3, multiplicites et domaines
  = derivation interne soutenue par Peter--Weyl et la theorie des generateurs,
    non sourcee mot a mot;

enveloppe convexe, robustesse conditionnee et contre-modele
  = derivation interne, aucune attribution PAPER_PROOF;

coherence de signe modale imposee par Navier--Stokes
  = non demontree;

grande phase projetee => RSS exact => rigidite Pineau--Vicol
  = implication absente;

transfert suitable/pression/Clay
  = absent.
```

La source Fedele--Abessi--Roberts falsifie l'idée que le quotient modal serait
sans antécédent, mais confirme simultanément le point central du cycle : la
vitesse dépend du produit scalaire choisi. La prochaine expérience décisive
reste donc PDE et non bibliographique : calculer, sur un champ de Schwartz
divergence-free, les numérateurs modaux du vrai champ vectoriel renormalisé et
chercher deux signes opposés en suivant séparément diffusion, drift,
non-linéarité et projection de Leray.
