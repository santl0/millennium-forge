# Cycle 0063 - invariance, tangence et régions modales

Date de gel : 2026-08-15.

Statut : **audit de littérature primaire et dérivation interne bornée**. Ce
document ne démontre ni régularité globale ni blow-up. Les formules marquées
`[DÉRIVATION]` ne sont pas attribuées à un article.

## Verdict falsifiable

La théorie de Nagumo-Brezis fournit un test exact en dimension finie : pour
une EDO localement lipschitzienne `x'=F(x)` et un fermé `K`, l'invariance en
temps positif équivaut à

\[
 \lim_{h\downarrow0}\frac{\operatorname{dist}(x+hF(x),K)}h=0
 \quad\text{pour tout }x\in K.                              \tag{V1}
\]

Pour une face régulière `K={g_j>=0}`, ce test impose en particulier

\[
 g_j(x)=0\quad\Longrightarrow\quad Dg_j(x)F(x)\geq0.        \tag{V2}
\]

Les extensions aux équations d'évolution dans un Banach remplacent le pas
d'Euler par le semi-groupe ou le résolvant de la partie linéaire et ajoutent
des hypothèses substantielles : fermeture du domaine contraint, existence et
unicité mild, continuité ou Lipschitz de la non-linéarité, compacité ou
estimations de résolvante selon le théorème choisi. Elles ne transforment pas
un signe observé sur une trajectoire en région invariante.

Pour le fonctionnel du cycle 0062,

\[
 C_m(Z)=\langle P_m d(Z),\mathcal RZ_m\rangle_{L^2},
 \qquad Z_m=P_mZ,                                           \tag{V3}
\]

aucune source primaire localisée ne prouve, au 2026-08-15, l'invariance de

\[
 K_C=\{Z:C_m(Z)\geq0\ \text{pour tout }m\geq1\}             \tag{V4}
\]

pour Navier-Stokes 3D complet, physique ou renormalisé. Plus précisément :

1. un test Nagumo devrait être vérifié sur **tout le bord** de `K_C`, pas
   seulement sur une orbite ancienne candidate;
2. `K_C` n'est pas même établi comme un cône fermé dans un espace de phase
   où le flot, `d`, `P_m` et le générateur non borné `mathcal R` sont tous
   bien définis;
3. les régions spectrales effectivement publiées contrôlent la **magnitude**
   des coefficients, et non le signe d'une vitesse de phase;
4. les sous-espaces homochiraux sont invariants pour une équation
   **décimée**, parce que la non-linéarité est projetée à chaque instant;
5. Pineau--Vicol v2 traite des profils RSS/RDSS exacts sous borne Type I. Ce
   n'est ni un théorème de viabilité, ni une invariance de `(V4)`.

Un contre-test décisif est donc bien défini : construire un champ de
Schwartz solénoïdal `Z` dans le cadre exact ci-dessous, un indice `j`, et un
résidu certifié `delta>0` tels que

\[
 C_j(Z)=0,\qquad C_m(Z)\geq0\ (m\geq1),\qquad
 DC_j(Z)[d(Z)]\leq-\delta.                                  \tag{V5}
\]

Sous les hypothèses locales de solution forte et si la face est régulière,
`(V5)` réfute l'invariance de `K_C` pour **toutes** les solutions fortes. Il
ne réfute pas une propriété plus faible réservée à une solution ancienne
minimale ou à une classe RSS.

## 1. Cadres mathématiques séparés

### 1.1 Navier-Stokes renormalisé : cible du cycle

On fige, sur `R^3`, viscosité un, force nulle et absence de frontière,

\[
 \partial_s Z=d(Z)
 =\Delta Z-\mathbb P\operatorname{div}(Z\otimes Z)
 -\kappa(1+y\cdot\nabla)Z,
 \qquad \operatorname{div}Z=0,                              \tag{RNS}
\]

avec `kappa` réel fixé. Le noyau lisse de calcul est

\[
 X_{\rm core}=\mathcal S_\sigma(\mathbb R^3),               \tag{1.1}
\]

les champs de Schwartz réels et solénoïdaux. L'audit ne suppose pas que ce
noyau, muni de sa topologie de Fréchet, satisfasse automatiquement les
hypothèses d'un théorème abstrait de viabilité. Pour l'implication locale de
`(V5)`, la notion pertinente est une solution classique/forte unique issue
d'une donnée lisse, sur son intervalle maximal. Aucune assertion n'est faite
ici pour les solutions de Leray--Hopf ou les solutions faibles adaptées.

L'action covariante des rotations autour de `e_3` est

\[
 (Q_\theta Z)(y)=R_\theta Z(R_{-\theta}y),\qquad
 \mathcal RZ=JZ-(Jy\cdot\nabla)Z.                           \tag{1.2}
\]

Les `P_m` sont les projecteurs isotypiques réels de cette action. Ils ne sont
pas des coupures de Fourier radial et le label `m` n'est pas une norme de
fréquence complète.

### 1.2 Navier-Stokes physique : problème de raccord

Le système Clay voisin est

\[
 \partial_tu-\nu\Delta u+\mathbb P\operatorname{div}(u\otimes u)=0,
 \qquad \operatorname{div}u=0,\qquad \nu>0,                 \tag{NS}
\]

sur `R^3` ou sur `T^3`, avec donnée initiale lisse solénoïdale et, dans le
cas périodique, moyenne nulle. Une région invariante de `(RNS)` ne se
transfère à `(NS)` qu'après explicitation de la transformation de similarité,
de l'intervalle de temps et de la classe de solutions. Une région bornée,
forcée ou munie de conditions au bord n'est pas un résultat Clay.

### 1.3 EDO de Galerkin

Pour une coupure spectrale finie `Pi_N`, on obtient l'EDO polynomiale

\[
 \dot Z_N=F_N(Z_N):=\Pi_Nd(Z_N).                            \tag{G_N}
\]

Elle possède localement un flot classique unique. Nagumo-Brezis s'applique
directement à un fermé fini-dimensionnel `K_N`. Cela n'identifie ni `F_N` à
`d` hors de l'espace retenu, ni `K_N` à la trace d'un fermé invariant du
continuum.

### 1.4 Modèles décimés

Une équation du type

\[
 \partial_tv=\Pi\big[-(v\cdot\nabla)v-\nabla p\big]
 +\nu\Delta v+f,
 \qquad v=\Pi v,                                            \tag{dNS}
\]

est un modèle projeté. L'espace `Ran(Pi)` y est invariant par construction.
Il ne s'ensuit pas qu'il soit invariant sous `(NS)`, où la projection `Pi`
supplémentaire est absente.

## 2. Échelle et géométrie de la région `K_C`

Le cycle 0062 a établi, sur le noyau `(1.1)`,

\[
 C_m=C_m^{\rm conv}+C_m^{\rm drift},\qquad
 C_m^{\rm diff}=0.                                         \tag{2.1}
\]

Sous multiplication d'amplitude `Z -> aZ`,

\[
 C_m^{\rm drift}(aZ)=a^2C_m^{\rm drift}(Z),\qquad
 C_m^{\rm conv}(aZ)=a^3C_m^{\rm conv}(Z).                  \tag{2.2}
\]

Sous la dilatation spatiale Navier-Stokes `Z_lambda(y)=lambda
Z(lambda y)`,

\[
 C_m^{\rm conv}(Z_\lambda)=\lambda C_m^{\rm conv}(Z),
 \qquad
 C_m^{\rm drift}(Z_\lambda)=\lambda^{-1}C_m^{\rm drift}(Z).
                                                                    \tag{2.3}
\]

Ainsi `C_m` n'est homogène ni en amplitude ni sous la dilatation physique
de l'état renormalisé. Le nom « cône modal » est une commodité de travail :
la stabilité de `(V4)` par multiplication positive n'est pas acquise.

Trois autres propriétés doivent être démontrées avant d'invoquer un théorème
abstrait :

- choisir un Banach ou Hilbert `X` où `d` engendre le flot local considéré;
- prouver la continuité de chaque `C_m` et la fermeture de l'intersection
  dénombrable `(V4)` dans cette topologie;
- traiter le domaine de `mathcal R`, qui contient un coefficient linéaire en
  `y`, ainsi que le domaine de la partie parabolique de `d`.

Un signe seul n'est par ailleurs pas coercif. Même si `(V4)` était invariant
jusqu'au temps maximal, il ne bornerait a priori aucune norme critique et ne
constituerait donc pas encore un critère de prolongement.

## 3. Théorèmes de tangence réellement disponibles

### 3.1 Nagumo 1942 et Brezis 1970 : dimension finie

La source fondatrice est Mitio Nagumo, *Über die Lage der Integralkurven
gewöhnlicher Differentialgleichungen*, Proc. Phys.-Math. Soc. Japan 24
(1942), 551--559,
[DOI primaire](https://doi.org/10.11429/ppmsj1919.24.0_551) et
[notice/PDF J-STAGE](https://www.jstage.jst.go.jp/article/ppmsj1919/24/0/24_0_551/_article).

Haim Brezis donne la formulation exacte utile ici dans *On a
Characterization of Flow-Invariant Sets*, Comm. Pure Appl. Math. 23 (1970),
261--263,
[PDF auteur](https://sites.math.rutgers.edu/~brezis/PUBlications/9-journal.pdf),
[DOI](https://doi.org/10.1002/cpa.3160230211). Son théorème 1 suppose :

- un espace euclidien **de dimension finie** `E`;
- un ouvert `Omega subset E`;
- un fermé relatif `K subset Omega`;
- un champ `F:Omega->E` localement lipschitzien.

Il établit l'équivalence entre `(V1)` en tout point de `K` et la préservation
de `K` par le flot local. Brezis indique qu'en Banach général son argument
demande une version **uniforme dans un voisinage** du point; il ne publie pas
dans ces trois pages une application automatique à une PDE avec générateur
non borné.

Lorsque `K={g_1>=0,...,g_q>=0}`, que les `g_j` sont `C^1` et que la face
active est régulière, `(V1)` se réduit à l'appartenance au cône contingent;
elle donne `(V2)` pour chaque contrainte active. Aux coins, ou lorsque
`Dg_j=0`, le simple test de dérivée scalaire peut être insuffisant : la
condition de distance `(V1)` reste la formulation sûre.

### 3.2 EDO dans un Banach

R. H. Martin, *Differential Equations on Closed Subsets of a Banach Space*,
Trans. AMS 179 (1973), 399--414,
[PDF AMS](https://www.ams.org/journals/tran/1973-179-00/S0002-9947-1973-0318991-4/S0002-9947-1973-0318991-4.pdf),
[DOI](https://doi.org/10.1090/S0002-9947-1973-0318991-4), étudie
`u'=A(t,u)` sur un fermé d'un Banach. La tangence y est accompagnée de
conditions de type dissipatif garantissant l'existence. Cette source ferme
une confusion fréquente : dans un Banach infini-dimensionnel, continuité du
champ plus tangence ne remplace pas à elle seule une théorie d'existence.

### 3.3 Équations semi-linéaires et semi-groupes

N. H. Pavel, *Invariant Sets for a Class of Semi-Linear Equations of
Evolution*, Nonlinear Analysis 1 (1977), 187--196,
[DOI primaire](https://doi.org/10.1016/0362-546X(77)90009-8), considère

\[
 u'(t)=Au(t)+F(t,u(t)),                                     \tag{3.1}
\]

lorsque `A` engendre un semi-groupe `S(t)`. Dans le cadre publié où `S(t)`
est compact, `F` continue et le domaine contraint localement fermé, la
condition suffisante prend la forme

\[
 \liminf_{h\downarrow0}\frac1h
 \operatorname{dist}\big(S(h)x+hF(t,x),K\big)=0             \tag{3.2}
\]

pour tout point admissible. C'est `(3.2)`, et non
`dist(x+h(Ax+F(x)),K)` hors du domaine de `A`, qui est le bon premier test
mild.

Pour les semi-groupes de contractions non linéaires dans un Hilbert, Haim
Brezis et Amnon Pazy, *Semigroups of Nonlinear Contractions on Convex Sets*,
J. Funct. Anal. 6 (1970), 237--281,
[PDF auteur](https://sites.math.rutgers.edu/~brezis/PUBlications/012journal.pdf),
[DOI](https://doi.org/10.1016/0022-1236(70)90060-1), donnent une
caractérisation par les résolvantes pour un **fermé convexe**. Leur théorème
2.2 relie préservation par `J_lambda=(I+lambda A)^{-1}` et préservation par
le semi-groupe, avec des hypothèses de monotonie/maximalité. Le théorème 3.2
contrôle la convergence de semi-groupes lorsque les résolvantes convergent.
Il ne fournit pas un passage à la limite pour une famille de régions
non convexes dépendant de `N`.

### 3.4 Systèmes paraboliques et principe de maximum

Herbert Amann, *Invariant Sets and Existence Theorems for Semilinear
Parabolic and Elliptic Systems*, J. Math. Anal. Appl. 65 (1978), 432--467,
[DOI primaire](https://doi.org/10.1016/0022-247X(78)90192-0), et son
[résumé primaire EQUADIFF](https://dml.cz/bitstream/handle/10338.dmlcz/702196/Equadiff_04-1979-1_5.pdf),
traite un système parabolique diagonal sur un domaine borné lisse, avec
conditions de Dirichlet, Neumann ou obliques, solution classique, et une
région ponctuelle compacte convexe `D subset R^m`. La condition publiée est
un signe contre **toute normale extérieure** à `D`; le semi-groupe linéaire
préserve ensuite les fonctions à valeurs dans `D` grâce au principe de
maximum.

Ce mécanisme ne se transfère pas directement à `(RNS)` :

- `K_C` est défini par des fonctionnels globaux de l'état et du champ
  vectoriel, pas par `Z(y) in D` point par point;
- `mathbb P div(Z tensor Z)` et la pression sont non locaux;
- la non-linéarité perd une dérivée dans les espaces usuels;
- le domaine est `R^3`, non un domaine borné avec semi-groupe compact;
- aucune convexité de `K_C` n'est établie.

## 4. Obligation de tangence exacte pour `C_m`

Posons `F=d`. Sur un espace lisse où les différentiations suivantes sont
justifiées,

\[
 C_m(Z)=\langle P_mF(Z),\mathcal RP_mZ\rangle.              \tag{4.1}
\]

Le long de `Z_s=F(Z)`, la règle de chaîne donne

\[
 \frac d{ds}C_m(Z)
 =\langle P_mDF(Z)[F(Z)],\mathcal RZ_m\rangle
 +\langle P_mF(Z),\mathcal RP_mF(Z)\rangle.                 \tag{4.2}
\]

Comme `mathcal R` est antisymétrique sur son domaine et commute avec
`P_m`, le second terme est nul. Par conséquent

\[
 \boxed{\Gamma_m(Z):=DC_m(Z)[d(Z)]
 =\langle P_mDd(Z)[d(Z)],\mathcal RZ_m\rangle.}             \tag{4.3}
\]

Ici

\[
 Dd(Z)[H]=\Delta H
 -\mathbb P\operatorname{div}(H\otimes Z+Z\otimes H)
 -\kappa(1+y\cdot\nabla)H.                                \tag{4.4}
\]

Les formules `(4.2)--(4.4)` sont une **dérivation interne**, pas un résultat
de littérature. Elles fixent néanmoins le test falsifiable : sur une face
régulière `C_j=0`, l'invariance exige `Gamma_j>=0`.

### 4.1 Pression et projection de Leray

Dans `(4.3)`, l'appariement est global, non pondéré, et `mathcal RZ_m` est
solénoïdal. On peut donc retirer la projection de Leray de l'argument testé,
après avoir vérifié domaines et intégrabilité. Cela ne rend pas la pression
locale. Dès qu'on introduit une coupure spatiale, un poids gaussien ou une
norme de distance non compatible avec la décomposition solénoïdale,
`mathbb P` ne disparaît plus. Le calcul global ne doit donc pas être recyclé
comme condition de tangence locale.

### 4.2 Faces dégénérées

Si `Z_j=0`, alors `C_j=0` et `(4.3)` s'annule automatiquement, même lorsque
des triades produisent immédiatement le mode `j`. Le premier test scalaire
ne voit alors pas une sortie d'ordre deux. Il faut utiliser directement
`(V1)` ou calculer la première dérivée temporelle non nulle de `C_j`.

De même, à une intersection infinie de faces actives, les inégalités
`Gamma_m>=0` prises séparément ne sont suffisantes qu'après identification
du cône contingent de l'intersection dans la topologie choisie.

### 4.3 Quantificateur correct

La propriété

\[
 C_m(Z(s_0))\geq0\quad\text{sur une trajectoire particulière}             \tag{4.5}
\]

n'implique rien sur `(V1)` en tous les points du bord. Réciproquement, un
point satisfaisant `(V5)` réfute l'invariance universelle des solutions
fortes mais laisse ouvertes :

- une région atteignable plus petite;
- une contrainte seulement asymptotique lorsque `s->+infinity`;
- une propriété des solutions anciennes Type I capturées;
- une propriété d'un élément minimal obtenu par compacité-rigidité.

## 5. Régions et sous-espaces réellement invariants en Navier-Stokes

### 5.1 Régions de piégeage spectrales : Navier-Stokes complet

Piotr Zgliczynski, *Trapping Regions and an ODE-Type Proof of the Existence
and Uniqueness Theorem for Navier-Stokes Equations with Periodic Boundary
Conditions on the Plane*, Universitatis Iagellonicae Acta Mathematica 41
(2003), 89--113,
[version corrigée de l'auteur](https://ww2.ii.uj.edu.pl/~zgliczyn/papers/ns/ns.pdf),
[arXiv](https://arxiv.org/abs/math/0103053), construit des régions uniformes
pour les projections de Galerkin symétriques.

Pour `d=2`, viscosité `nu>0`, boîte périodique et force à support spectral
fini, la région associe une borne d'enstrophie et

\[
 |u_k|\leq D|k|^{-\gamma}\quad (|k|>K),\qquad \gamma\geq5/2. \tag{5.1}
\]

Sur chacune de ses faces, l'estimation publiée donne un champ strictement
entrant lorsque `K` et `D` satisfont des inégalités explicites. Les bornes
sont uniformes en dimension de Galerkin et permettent le passage à la PDE
2D. La version auteur avertit que la version publiée comportait des erreurs
dans l'énoncé et la preuve de son théorème 6, ainsi que des coquilles dans le
lemme 1; elle doit donc être préférée pour reproduction.

La même source donne en `d=3`, sur `T^3`, force nulle, un résultat de petites
données : pour `gamma>3.5`, il existe

\[
 D_0=\frac{\nu}{C_Q(3,\gamma)}>0                            \tag{5.2}
\]

tel que

\[
 W_D=\{(u_k):|u_k|\leq D|k|^{-\gamma}\ \forall k\ne0\},
 \qquad D<D_0,                                              \tag{5.3}
\]

est une région de piégeage pour toutes les projections et produit une
solution globale du système complet. C'est une vraie preuve analytique, pas
un calcul numérique.

Le non-transfert à `K_C` est précis : `(5.3)` est une région de **petite
amplitude super-lisse**, avec seuil proportionnel à `nu`; elle contrôle
`|u_k|` sans sélectionner la phase. Pour grandes données 3D, la borne
d'enstrophie qui ferme le cas 2D manque. Aucun `C_m` azimutal n'apparaît.

Le résultat original 2D de J. C. Mattingly et Ya. G. Sinai, *An Elementary
Proof of the Existence and Uniqueness Theorem for the Navier-Stokes
Equations*, Comm. Contemp. Math. 1 (1999), 497--516, est disponible en
[prépublication primaire](https://arxiv.org/abs/math/9903042) et sous
[DOI](https://doi.org/10.1142/S0219199799000183).

### 5.2 Sous-espaces de symétrie du flot complet

A. Mahalov, E. S. Titi et S. Leibovich, *Invariant Helical Subspaces for
the Navier-Stokes Equations*, Arch. Rational Mech. Anal. 112 (1990),
193--222, [DOI primaire](https://doi.org/10.1007/BF00381234), prouvent que
les champs à symétrie hélicoïdale forment un sous-espace invariant du système
3D dans les géométries compatibles étudiées. Ils obtiennent unicité des
solutions faibles hélicoïdales de Leray et régularité globale forte; une
application détaillée concerne un écoulement de Hagen--Poiseuille en tube.

Il faut distinguer deux sens de « hélicoïdal » :

- la **symétrie hélicoïdale** est une invariance géométrique sous une action
  vissée et peut être préservée par l'équivariance du système complet;
- la **décomposition hélicité positive/négative** est une base de
  polarisation de chaque mode de Fourier et n'est pas, seule, préservée par
  la non-linéarité complète.

Le premier est un sous-problème invariant de codimension infinie et dépend
de la géométrie; il ne produit pas la région de phase `(V4)` pour données
générales sur `R^3` ou `T^3`.

### 5.3 Hélicité de signe fixé : modèle décimé

Luca Biferale et Edriss S. Titi, *On the Global Regularity of a
Helical-Decimated Version of the 3D Navier-Stokes Equations*, J. Stat. Phys.
151 (2013), 1089--1098,
[arXiv primaire](https://arxiv.org/abs/1303.1215),
[DOI](https://doi.org/10.1007/s10955-013-0746-4), étudient sur le tore
tridimensionnel

\[
 \partial_tv^+-\nu\Delta v^+
 =-\mathcal P^+\mathbb P((v^+\cdot\nabla)v^+)+f^+.          \tag{5.4}
\]

La projection `mathcal P^+` est appliquée à la dynamique. Le sous-espace
`v^-=0` est donc invariant pour `(5.4)`. L'hélicité positive devient une
quantité quadratique coercive équivalente à `||v^+||_{H^{1/2}}^2`, ce qui
donne les bornes globales

\[
 v^+\in L^\infty_tH^{1/2}_x\cap L^2_tH^{3/2}_x.            \tag{5.5}
\]

Pour le système complet, le terme supprimé
`mathcal P^- mathbb P((v^+ dot nabla)v^+)` est en général non nul. L'article
est donc une preuve sur un modèle modifié, pas un théorème selon lequel le
cône d'hélicité positive serait invariant sous Navier-Stokes 3D.

### 5.4 Décimation Fourier récente : calcul numérique

Anikat Kankaria, Ritwik Mukherjee, Sugan Durai Murugan, Marco Edoardo Rosti
et Samriddhi Sankar Ray, *Reduction of Triadic Interactions Suppresses
Intermittency and Anomalous Dissipation in Turbulence*,
[arXiv:2603.19180v1](https://arxiv.org/abs/2603.19180), soumis le
2026-03-19, effectuent des DNS de Navier-Stokes Fourier-décimé forcé sur une
boîte triplement périodique. Le résultat est un indice numérique sur
l'intermittence et la dissipation anormale lorsque le réseau de triades est
aminci.

Cette source confirme expérimentalement que supprimer des triades change
fortement la dynamique; elle ne certifie ni une région invariante du système
complet, ni un signe de `C_m`. La projection gelée doit rester dans
l'équation pour conserver les modes retenus.

## 6. Pineau--Vicol v2 : raccord exact et non-raccord

Ben Pineau et Vlad Vicol, *On Rotated Backwards Self-Similar Solutions of
the Incompressible 3D Navier-Stokes Equations*,
[arXiv:2607.09619v2](https://arxiv.org/abs/2607.09619v2), prépublication
soumise le 2026-07-10 et révisée le 2026-08-06, considèrent le système
incompressible non forcé, viscosité un, sur `R^3 x [-1,0)`, avec solution
lisse. L'ansatz RSS donne le profil stationnaire

\[
 \alpha\mathcal RU+\tfrac12U+\tfrac12(y\cdot\nabla)U
 -\Delta U+(U\cdot\nabla)U+\nabla P=0,
 \qquad \operatorname{div}U=0.                             \tag{6.1}
\]

Sous la borne Type I

\[
 |U(y)|\leq \frac{C_{U,0}}{1+|y|},                         \tag{6.2}
\]

les auteurs prouvent `U=0` lorsque `|alpha|` est suffisamment petit ou
suffisamment grand en fonction de `C_{U,0}`. Le cas intermédiaire reste
ouvert. Ils obtiennent aussi des résultats RDSS lorsque la période de
similarité est petite, et un critère local à une tranche de temps sous borne
Type I.

Pour grande rotation, la preuve estime une norme gaussienne de
`mathcal RU`; elle ne prouve pas un signe modal. L'équation `(6.1)` est
stationnaire et `alpha` est un paramètre fixé de l'ansatz, non une vitesse de
phase projetée d'une trajectoire générale. Les profils RDSS sont périodiques
en temps similaire, mais toujours soumis à l'ansatz global et à `(6.2)`.

Le lien avec le cycle est donc :

\[
 \text{grande rotation RSS exacte}
 \Longrightarrow \|\mathcal RU\|_{L^2_\mu}\ \text{petite}
 \Longrightarrow \text{rigidité},                          \tag{6.3}
\]

et non

\[
 C_m\geq0\ \text{à un instant}
 \Longrightarrow K_C\ \text{invariant}
 \Longrightarrow \text{RSS}.                              \tag{6.4}
\]

Enfin, leur méthode pondérée garde un contrôle explicite de la pression.
Elle ne justifie pas la suppression de `mathbb P` dans une distance pondérée
à `K_C`.

## 7. Veille différentielle 2025--2026

La recherche primaire a porté sur `Nagumo`, `viability`, `flow invariance`,
`semilinear Cauchy problem`, `Navier-Stokes invariant cone`, `Fourier
trapping region`, `Galerkin invariant region`, `helical subspace`, `modal
sign` et `Pineau Vicol`. Les résultats récents pertinents sont les suivants.

| source | équation et notion | résultat publié | non-transfert vers `K_C` |
|---|---|---|---|
| K. Ezzinbi et Y. Staili, *JMAA* 548 (2025), 129350, [DOI](https://doi.org/10.1016/j.jmaa.2025.129350) | équation fonctionnelle semi-linéaire avec délai infini, opérateur à domaine non dense; solution mild | condition sous-tangentielle pour viabilité d'un fermé local | mémoire, hypothèses abstraites et existence viable; aucune application NS ou fonctionnel `C_m` |
| M. Dieye, R. Djidjou-Demasse et O. Seydi, *Acta Appl. Math.* 201 (2026), art. 15, [DOI et texte primaire](https://doi.org/10.1007/s10440-026-00775-9) | `u'=Au+F(t,u)` dans un Banach, opérateur éventuellement non-Hille--Yosida, contraintes dépendant du temps; solution intégrale/mild | nouvelle condition sous-tangentielle par semi-groupe intégré et résolvante, sous hypothèses explicites | la contrainte de base est fermée/convexe et le théorème suppose Lipschitz local, estimations de résolvante et existence; aucune vérification pour `(RNS)` ou `K_C` |
| Kankaria et al., [arXiv:2603.19180v1](https://arxiv.org/abs/2603.19180v1) | NS Fourier-décimé forcé sur `T^3`; DNS | intermittence et dissipation diminuent avec la décimation | système projeté, calcul flottant, aucune preuve de tangence |
| Pineau--Vicol, [arXiv:2607.09619v2](https://arxiv.org/abs/2607.09619v2) | NS 3D complet sur `R^3`, profils RSS/RDSS lisses Type I | rigidité pour rotations extrêmes; critère local quasi-auto-similaire | ansatz exact et contrôle pondéré, aucune région modale invariante |

La veille n'a localisé aucun article 2025--2026 démontrant une région de
phase ou un cône `C_m>=0` invariant pour Navier-Stokes incompressible 3D
complet. Les progrès récents en viabilité clarifient les obligations
fonctionnelles mais ne vérifient aucune d'elles pour `(V4)`.

## 8. Passage Galerkin vers continuum : obligations minimales

Une vérification positive sur `(G_N)` ne devient une affirmation PDE que si
les points suivants sont tous fermés.

1. **Même contrainte.** Définir `C_m^N` et prouver qu'il est la restriction,
   ou une approximation contrôlée, de `C_m`; la projection de la
   non-linéarité change le champ vectoriel.
2. **Données admissibles.** Prouver que `Pi_NZ_0 in K_N` lorsque
   `Z_0 in K_C`, ou construire une approximation interne. Une projection ne
   préserve pas automatiquement des inégalités non linéaires.
3. **Tangence globale.** Certifier le champ entrant sur tout le bord de
   `K_N`, y compris les intersections et faces dégénérées; échantillonner le
   bord ne suffit pas.
4. **Uniformité.** Suivre les constantes de tangence, de Lipschitz et de
   temps d'existence indépendamment de `N`.
5. **Compacité forte.** Obtenir une convergence des solutions assez forte
   pour passer dans `Z tensor Z`, `d(Z)`, `mathcal RZ_m` et `C_m`.
6. **Modes omis.** Contrôler les triades sortantes puis leur retour vers les
   modes bas. Une troncature rend nul ce canal par définition.
7. **Fermeture.** Montrer que la limite appartient à `K_C`; la semi-continuité
   faible du fonctionnel cubique n'est pas automatique.
8. **Continuation.** Relier l'invariance obtenue à une borne dans un espace
   critique ou sous-critique qui prolonge la solution. Un demi-espace de
   phase non borné ne suffit pas.

Les régions `(5.1)--(5.3)` de Zgliczynski satisfont ce programme grâce à des
bornes quantitatives de magnitude et, en 2D, à l'enstrophie. Elles montrent
le niveau de preuve exigé; elles ne constituent pas un précédent pour une
simple cohérence de signe.

## 9. Test adverse reproductible recommandé

### 9.1 Question falsifiable

Existe-t-il un champ `Z in S_sigma(R^3)` à support azimutal fini, un indice
`j` dont `Z_j` est non nul, et `delta>0`, satisfaisant `(V5)` pour le champ
vectoriel complet `(RNS)` ?

### 9.2 Famille compacte de recherche

Utiliser des champs de la forme

\[
 Z(a)=\sum_{q=1}^Q a_q\,\nabla\times
 \big(e^{-|y|^2}P_q(y)e_3\big),                             \tag{9.1}
\]

où les `P_q` sont des polynômes réels répartis entre quelques isotypes
azimutaux. Cette famille est exactement solénoïdale et de Schwartz. Les
produits, dérivées et intégrales gaussiennes de `(4.1)--(4.4)` se réduisent
à des polynômes dans `a`, évaluables rationnellement après extraction des
facteurs communs de `pi`, ou par arithmétique d'intervalles dirigée.

### 9.3 Certificat exigé

Le fichier d'expérience devra fournir :

- la liste exacte des polynômes `P_q`, coefficients `a_q` et convention des
  projecteurs `P_m`;
- `div Z=0` symboliquement;
- les valeurs ou intervalles de tous les `C_m` potentiellement non nuls;
- une face non dégénérée `C_j=0`, obtenue symboliquement, ou une racine
  isolée par intervalle de Newton/Krawczyk avec unicité dans la boîte;
- `Gamma_j<=-delta` avec `delta>0` certifié;
- le contrôle des queues azimutales, ici nul par support fini de `Z` et
  borné explicitement pour `d(Z)`;
- une borne sur la dérivée seconde temporelle dans un voisinage, donnant un
  temps `tau>0` tel que `C_j(Z(s))<0` pour `0<s<=tau`;
- deux évaluations indépendantes : calcul symbolique et arithmétique
  d'intervalles à précision augmentée.

Si `Gamma_j=0` parce que la face est dégénérée, le test doit basculer vers
le quotient de distance `(V1)` ou certifier le signe de la première dérivée
temporelle non nulle. Un résultat flottant `Gamma_j<0` sans borne d'arrondi
n'est qu'un indice numérique.

### 9.4 Ce que le test déciderait

| issue certifiée | implication | non-implication |
|---|---|---|
| `(V5)` sur le champ complet | `K_C` n'est pas invariant pour toutes les solutions fortes de `(RNS)` | aucune réfutation d'un sous-ensemble ancien Type I |
| sortie seulement pour `F_N` | le cône de cette EDO de Galerkin échoue | aucune sortie PDE sans contrôle de l'erreur de troncature |
| tangence certifiée sur une famille compacte | cette famille ne contient pas de contre-exemple transversal | aucune invariance globale de `K_C` |
| tangence globale uniforme en `N` et passage fort | candidat sérieux de région PDE invariante | aucune régularité Clay sans coercivité/prolongement |

## 10. Registre des implications auditées

| affirmation | statut | preuve ou obstruction |
|---|---|---|
| Nagumo-Brezis donne `(V1)` pour l'EDO de Galerkin localement lipschitzienne | **PAPER_PROOF** | Brezis 1970, dimension finie |
| sur une face régulière, l'invariance impose `DC_j[d]>=0` | **PAPER_PROOF + calcul standard** | cône contingent; `(V2)` |
| la dérivée de `C_m` est `(4.3)` | **AI_INTERNAL_DERIVATION** | antisymétrie de `mathcal R`; à revoir indépendamment |
| une vérification sur une seule trajectoire établit l'invariance | **RÉFUTÉ comme implication** | quantificateur « tout point du bord » dans `(V1)` |
| la théorie de semi-groupes s'applique automatiquement à `K_C` | **NON ÉTABLI** | espace de phase, fermeture, domaines, convexité et génération manquants |
| il existe des régions spectrales invariantes pour NS complet | **PAPER_PROOF, sous hypothèses** | Zgliczynski : 2D grandes données; 3D petites données très régulières |
| le sous-espace d'hélicité positive est invariant sous NS complet | **FAUX en général / modèle modifié** | Biferale--Titi projettent explicitement la non-linéarité |
| Pineau--Vicol v2 prouve un cône modal invariant | **NON** | profil RSS/RDSS exact, estimation pondérée, aucun théorème de viabilité |
| `K_C` invariant impliquerait à lui seul la régularité Clay | **NON ÉTABLI** | aucune borne critique coercive ni critère de prolongement |
| une source 2025--2026 ferme la tangence de `K_C` | **NON TROUVÉ** | veille différentielle primaire ci-dessus |

## Conclusion opérationnelle

Le premier maillon transférable n'est pas un théorème d'invariance existant,
mais une **obligation de bord** : `(4.3)` doit être non négatif sur chaque
face régulière de `(V4)`. C'est testable sur une famille gaussienne finie
sans résoudre la PDE longtemps. La priorité scientifique est donc de tenter
le certificat adverse `(V5)`. Une sortie certifiée ferme la stratégie du
cône universel; l'absence de sortie sur une famille finie ne justifie pas de
poursuivre vers Clay avant une certification globale et uniforme en
troncature.
