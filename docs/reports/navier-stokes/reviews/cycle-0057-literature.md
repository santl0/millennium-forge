# Cycle 0057 — rotation de profil à vitesse divergente et moyenne angulaire

**Date de coupure :** 15 août 2026
**Nature :** veille primaire indépendante, dérivation bornée et passe
contradictoire
**Question :** existe-t-il un théorème de PDE couvrant une suite

\[
 \beta_n\longrightarrow\infty,\qquad
 r_n:=\partial_s Z_n-\beta_n\mathcal RZ_n\longrightarrow0,
 \qquad Z_n\longrightarrow Z\quad\hbox{fortement dans }L^3_{\rm loc},
 \tag{Q}
\]

et concluant que la limite est axisymétrique et stationnaire ?

## Verdict

1. **Aucun théorème primaire trouvé ne possède exactement les hypothèses et
   la conclusion de (Q).** La recherche a couvert les méthodes de gel de
   phase, les équilibres relatifs, les fluides à rotation de Coriolis rapide,
   les obstacles tournants, l'axisymétrisation par dissipation renforcée et
   les Liouville stationnaires/axisymétriques. Les résultats trouvés portent
   soit sur une autre équation, soit sur une solution classique exacte, soit
   sur un domaine avec frontière, soit sur une pénalisation de Coriolis dont
   le noyau n'est pas celui de \(\mathcal R\).

2. **Pour des vitesses \(\beta_n\in\mathbb R\) constantes avec
   \(|\beta_n|\to\infty\), le résultat recherché est néanmoins vrai, et plus
   général que (Q).** La convergence distributionnelle \(Z_n\to Z\) suffit;
   la convergence forte \(L^3_{\rm loc}\) n'est pas utilisée pour la seule
   conclusion cinématique. Le lemme élémentaire démontré ci-dessous donne

   \[
     \mathcal RZ=0,\qquad \partial_sZ=0.                 \tag{V1}
   \]

   Il s'agit d'une **dérivation du laboratoire**, pas d'un `PAPER_PROOF`.

3. **Le quantificateur sur la vitesse est essentiel.** Si
   « \(\beta_n\to\infty\) » signifie seulement
   \(\sup_s|\beta_n(s)|\to\infty\), l'implication vers l'axisymétrie est
   fausse. Un contre-exemple lisse, divergence-free et à résidu certifié
   \(O(n^{-1})\) est donné à la section 7. Pour une vitesse dépendant de
   \(s\), il faut au minimum une hypothèse uniforme sur son inverse et ses
   variations; on ne peut pas diviser une dérivée distributionnelle par
   \(\beta_n(s)\) sans faire apparaître
   \(\partial_s(\beta_n^{-1})\).

4. **La forte convergence \(L^3_{\rm loc}\) intervient au maillon PDE, pas au
   maillon de symétrie.** Elle fait converger
   \(Z_n\otimes Z_n\to Z\otimes Z\) dans \(L^{3/2}_{\rm loc}\), mais elle ne
   transmet à elle seule ni la pression, ni l'inégalité d'énergie locale, ni
   la non-trivialité. Des bornes locales de pression et de gradient restent
   nécessaires pour obtenir une limite faible adaptée.

5. **Ożański--Palasek 2023 (`NS-SRC-0088`) ferme déjà la branche ancienne
   axisymétrique dans sa classe exacte : solution forte/classique et borne
   uniforme \(L^{3,\infty}\).** Son corollaire de Liouville exclut alors toute
   ancienne non triviale, sans avoir besoin de la stationnarité en \(s\).
   Mais une limite seulement faible adaptée (*suitable*) n'entre pas
   automatiquement dans cette classe : invoquer ce corollaire avant un lemme
   de régularisation serait un changement silencieux de notion de solution.

6. **Si les bornes PDE adaptées sont ajoutées et si la borne globale
   \(L^{3,\infty}\) est héritée, la stationnarité de (V1) fournit une seconde
   fermeture.** Le profil stationnaire en temps similaire satisfait
   l'équation faible stationnaire de Leray. Le théorème 1.3 publié de
   Guevara--Phuc l'annule dans
   \(W^{1,2}_{\rm loc}\cap L^{3,\infty}\), classe compatible avec un raccord
   faible adapté muni d'énergie locale. Une limite non triviale donnerait
   alors une contradiction. Le verrou Clay se déplace donc vers la production
   simultanée du défaut vanissant, de la compacité adaptée et de la
   non-trivialité; aucune de ces propriétés ne découle actuellement d'un
   blow-up arbitraire.

## 1. Équation, action de rotation et échelle

Le cadre Clay pertinent est Navier--Stokes incompressible 3D, viscosité un,
sans force, sur \(\mathbb R^3\times(-\infty,0)\) :

\[
 \partial_tu-\Delta u+(u\cdot\nabla)u+\nabla p=0,
 \qquad \nabla\cdot u=0.                                  \tag{1}
\]

Avec

\[
 y=\frac{x}{\sqrt{-t}},\qquad s=-\log(-t),\qquad
 V(y,s)=\sqrt{-t}\,u(x,t),\qquad P(y,s)=(-t)p(x,t),        \tag{2}
\]

on obtient

\[
 \partial_sV-\Delta V+\frac12V+\frac12y\cdot\nabla V
 +(V\cdot\nabla)V+\nabla P=0,
 \qquad \nabla\cdot V=0.                                  \tag{3}
\]

Soit \(R_\theta\) la rotation autour de l'axe \(e_3\), \(J=R'_0\), et

\[
 (\rho_\theta Z)(y,s)=R_\theta Z(R_{-\theta}y,s),\qquad
 \mathcal RZ=JZ-(Jy\cdot\nabla)Z.                          \tag{4}
\]

La moyenne de Haar de cette action compacte est

\[
 \mathcal AZ=\frac1{2\pi}\int_0^{2\pi}\rho_\theta Z\,d\theta.
                                                               \tag{5}
\]

Elle est continue sur les distributions, commute avec \(\partial_s\), et

\[
 \mathcal A\mathcal R=0,\qquad
 \ker\mathcal R=\operatorname{Ran}\mathcal A.              \tag{6}
\]

La seconde égalité vaut aussi pour les distributions : si
\(\mathcal RZ=0\), alors
\(\partial_\theta(\rho_\theta Z)=\rho_\theta\mathcal RZ=0\), donc
\(\rho_\theta Z=Z\), puis \(\mathcal AZ=Z\).

Sous l'échelle Clay
\(u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t)\), la norme spatiale
\(L^{3,\infty}\) est invariante. Le temps \(s\), la vitesse angulaire
\(\beta\) mesurée par unité de \(s\), \(V\), \(\partial_sV\) et
\(\beta\mathcal RV\) sont sans dimension supplémentaire. La rotation est une
isométrie de \(L^{3,\infty}\). La convergence locale forte \(L^3\) est au bon
exposant spatial pour le produit quadratique, mais elle n'est pas une borne
globale critique.

## 2. Lemme minimal : haute vitesse constante

> **Lemme 0057-L (cinématique, distributionnel).** Soit
> \(I\subset\mathbb R\) un intervalle ouvert. Soient
> \(Z_n\in\mathcal D'(I\times\mathbb R^3)^3\),
> \(\beta_n\in\mathbb R\setminus\{0\}\) des constantes telles que
> \(|\beta_n|\to\infty\), et
> \(r_n=\partial_sZ_n-\beta_n\mathcal RZ_n\). Si
> \(Z_n\to Z\) et \(r_n\to0\) dans
> \(\mathcal D'(I\times\mathbb R^3)^3\), alors
> \(\mathcal RZ=0\) et \(\partial_sZ=0\).

### 2.1 Axisymétrie

Dans les distributions,

\[
 \mathcal RZ_n=\beta_n^{-1}\partial_sZ_n-\beta_n^{-1}r_n. \tag{7}
\]

Pour tout test \(\varphi\),

\[
 \left\langle\beta_n^{-1}\partial_sZ_n,\varphi\right\rangle
 =-\beta_n^{-1}\left\langle Z_n,\partial_s\varphi\right\rangle
 \longrightarrow0.                                             \tag{8}
\]

Les appariements dans le membre de droite sont bornés puisque
\(Z_n\to Z\) dans \(\mathcal D'\). De même,
\(\beta_n^{-1}r_n\to0\). Ainsi \(\mathcal RZ_n\to0\), tandis que la
continuité de \(\mathcal R\) donne
\(\mathcal RZ_n\to\mathcal RZ\). Donc

\[
 \mathcal RZ=0.                                                  \tag{9}
\]

### 2.2 Stationnarité

Appliquons directement la moyenne angulaire au défaut :

\[
 \mathcal Ar_n
 =\partial_s\mathcal AZ_n-\beta_n\mathcal A\mathcal RZ_n
 =\partial_s\mathcal AZ_n.                                     \tag{10}
\]

Le passage à la limite donne \(\partial_s\mathcal AZ=0\). Par (6) et (9),
\(\mathcal AZ=Z\), d'où

\[
 \partial_sZ=0.                                                  \tag{11}
\]

### 2.3 Portée exacte

- Aucune équation de Navier--Stokes n'a été utilisée.
- Aucune norme \(L^3\), aucune pression et aucune inégalité d'énergie n'ont
  été utilisées.
- La convergence forte de (Q) est donc surdimensionnée pour (V1), mais reste
  utile pour transmettre le terme non linéaire de (3).
- Le résultat ne conclut pas \(Z=0\); il conclut seulement invariance
  angulaire et stationnarité en temps similaire.
- La constance de \(\beta_n\) est utilisée dans (8). Une version à coefficients
  variables doit expliciter une classe de multiplicateurs pour
  \(\beta_n^{-1}\), le contrôle de
  \(\partial_s(\beta_n^{-1})\), les zéros éventuels et le sens de
  \(\beta_n\to\infty\).

## 3. Résultats primaires les plus proches

### 3.1 Limites à rotation physique rapide

| Source primaire et statut | Équation, domaine, solution | Résultat exact utile | Pourquoi ce n'est pas (Q) |
|---|---|---|---|
| A. Babin, A. Mahalov, B. Nicolaenko, *Global Regularity of 3D Rotating Navier--Stokes Equations for Resonant Domains*, *Indiana Univ. Math. J.* **48**(3) (1999), 1133--1176, [DOI 10.1512/iumj.1999.48.1856](https://doi.org/10.1512/iumj.1999.48.1856), **publié** | Navier--Stokes 3D en repère physique tournant, après projection \(\partial_tu-\nu\Delta u+\Omega\mathbb P J\mathbb Pu+\mathbb P(u\cdot\nabla u)=0\); domaines périodiques ou avec conditions *stress-free* | Régularité globale pour rotation de Coriolis assez grande, y compris domaines résonants; passage par des équations limites résonantes | Le grand opérateur est \(\mathbb P J\mathbb P\), pas le générateur géométrique \(J-(Jy\cdot\nabla)\); le noyau est un espace lent géostrophique/colonnaire, pas l'ensemble des champs axisymétriques. |
| I. Gallagher, L. Saint-Raymond, *Weak Convergence Results for Inhomogeneous Rotating Fluid Equations*, *C. R. Math.* **336**(5) (2003), 401--406, [DOI 10.1016/S1631-073X(03)00066-9](https://doi.org/10.1016/S1631-073X(03)00066-9), [texte primaire](https://www.numdam.org/articles/10.1016/S1631-073X%2803%2900066-9/), **publié** | \(\partial_tu+u\cdot\nabla u-\nu\Delta u+\varepsilon^{-1}u\wedge B+\nabla p=0\), \(B=b(x_h)e_3\), sur \(\Omega_h\times\Omega_3\), données divergence-free \(L^2\), solutions faibles de type Leray | Sous (H0)--(H2), convergence faible \(L^2_{\rm loc}\) vers \(\ker\mathbb P(\cdot\wedge B)\); si \(\Omega_3=\mathbb R\), limite nulle; si \(\Omega_3=\mathbb T\), NS 2D là où \(b\) est constant et équation de chaleur projetée ailleurs | C'est le précédent PDE conceptuellement le plus proche d'une pénalisation divergente, mais la force de Coriolis, l'énergie \(L^2\), le projecteur de Leray et la géométrie produit changent le noyau et la limite non linéaire. Il ne traite ni variables similaires, ni \(r_n\), ni faible-\(L^3\). |

Ces deux résultats établissent que « grand coefficient antisymétrique » ne
signifie pas automatiquement « axisymétrie ». La conclusion est l'appartenance
au noyau de **l'opérateur effectivement pénalisé**. Pour (Q), cet opérateur est
\(\mathcal R\), dont le noyau est précisément l'axisymétrie autour de l'axe
fixé.

### 3.2 Rotation d'un obstacle et axisymétrisation

| Source primaire et statut | Cadre exact | Résultat | Écart avec (Q) |
|---|---|---|---|
| I. Gallagher, M. Higaki, Y. Maekawa, *On Stationary Two-Dimensional Flows around a Fast Rotating Disk*, *Math. Nachr.* **292**(2) (2019), 273--308, [DOI 10.1002/mana.201700400](https://doi.org/10.1002/mana.201700400), [arXiv:1710.01029](https://arxiv.org/abs/1710.01029), **publié** | 2D, extérieur du disque \(\Omega=\{|x|>1\}\), système stationnaire forcé. Après retrait de la solution circulaire, le linéaire contient \(-\alpha(x^\perp\!\cdot\nabla v-v^\perp)+\alpha U^\perp\operatorname{rot}v\), avec no-slip au bord | Existence/unicité dans \(X=P_0W^{1,\infty}_0\times Q_0W^{1,2}_0\); pour une force fixée, \(\|Q_0v(\alpha)\|_{L^2}=O(|\alpha|^{-2/3})\) et \(\|Q_0v(\alpha)\|_{L^\infty}=O((\log|\alpha|)^{1/2}|\alpha|^{-1/2})\); couche limite d'épaisseur \(|2\alpha n|^{-1/3}\) pour certains modes | Le premier terme est structurellement le générateur de rotation de profil, mais l'équation est elliptique, 2D, extérieure, forcée, avec couche limite et solution construite dans une petite classe. Ce n'est ni une suite faible adaptée sur \(\mathbb R^3\), ni un théorème de défaut compact. |
| T. Gallay, *Enhanced Dissipation and Axisymmetrization of Two-Dimensional Viscous Vortices*, *Arch. Ration. Mech. Anal.* **230** (2018), 939--975, [DOI 10.1007/s00205-018-1262-0](https://doi.org/10.1007/s00205-018-1262-0), [arXiv:1707.05525](https://arxiv.org/abs/1707.05525), **publié** | Vorticité NS 2D près du vortex de Lamb--Oseen, perturbations fortement localisées, grand Reynolds de circulation | Relaxation vers l'axisymétrie sur une échelle proportionnelle à \(Re^{2/3}\), via estimations de résolvante et dissipation renforcée | Rotation différentielle d'un vortex de base, stabilité quantitative et 2D; aucune vitesse de groupe \(\beta_n\), aucun défaut de phase ni limite suitable 3D. |

Gallagher--Higaki--Maekawa confirme analytiquement que le générateur
\(x^\perp\cdot\nabla v-v^\perp\) peut tuer les modes angulaires non nuls à
grande vitesse. Son estimation dépend toutefois du Laplacien, du profil
circulaire \(U\), de la frontière et de la décomposition de Fourier; elle ne
remplace pas le lemme distributionnel 0057-L.

### 3.3 Gel de phase et équilibres relatifs

Les sources déjà cataloguées restent négatives pour la vitesse divergente.

- Beyn--Thümmler, *Freezing Solutions of Equivariant Evolution Equations*,
  [DOI 10.1137/030600515](https://doi.org/10.1137/030600515), donnent une
  équivalence locale entre PDE régulière et système gelé avec condition de
  phase. L'inversion repose sur une matrice de Gram non dégénérée. Le texte ne
  fournit ni compacité uniforme lorsque la vitesse de phase diverge, ni
  passage à une solution faible adaptée.
- Bradshaw--Tsai, *Rotationally Corrected Scaling Invariant Solutions to the
  Navier--Stokes Equations*,
  [DOI 10.1080/03605302.2017.1323922](https://doi.org/10.1080/03605302.2017.1323922),
  dérivent le repère similaire tournant et construisent des RSS/RDSS forward
  à vitesse constante. Ils partent d'une covariance exacte; ils ne prennent
  pas une limite de défauts avec \(|\beta_n|\to\infty\).
- Pineau--Vicol,
  [arXiv:2607.09619v2](https://arxiv.org/abs/2607.09619v2), prépublication
  révisée le 6 août 2026, traitent les RSS/RDSS backward **exactes**, lisses,
  sous borne Type I. Leur analyse par moyenne angulaire exclut notamment des
  RSS pour \(|\alpha|\) assez grand. Elle n'énonce pas de théorème de
  fermeture pour \(r_n\to0\), ni pour une limite faible-\(L^3\) adaptée.

Ainsi aucune source de *freezing* ne couvre l'approche d'un stabilisateur où
la matrice de phase dégénère et où la vitesse reconstruite peut exploser. Le
lemme 0057-L contourne la jauge : il ne reconstruit pas la phase, il projette
directement sur le noyau du groupe compact.

## 4. Trois rotations à ne pas identifier

| Mécanisme | Terme | Objet invariant à grande vitesse | Transfert |
|---|---|---|---|
| Rotation de profil en variables similaires | \(\beta\mathcal RZ=\beta[JZ-(Jy\cdot\nabla)Z]\) | \(\ker\mathcal R\) : champs axisymétriques autour de \(e_3\) | C'est (Q). Changement de représentation d'une même solution de (1); aucune force physique ajoutée. |
| Coriolis physique | \(\Omega e_3\times u\), ou après projection \(\Omega\mathbb PJ\mathbb Pu\) | Noyau/variété lente géostrophique ou colonnaire, dépendant du domaine et des résonances | Babin--Mahalov--Nicolaenko et Gallagher--Saint-Raymond. N'implique pas \(\mathcal Ru=0\). |
| Obstacle ou domaine tournant | \(-\alpha(x^\perp\cdot\nabla u-u^\perp)\), avec condition de bord tournante | Mode angulaire zéro plus couche limite imposée par le bord | Proche algébriquement de \(\mathcal R\), mais l'équation et le domaine ne sont pas Clay. |

Le projecteur de Leray ne commute pas gratuitement avec toutes les
localisations ou tous les coefficients. Dans la rotation physique homogène,
le grand opérateur est non local après projection. Dans (4), le générateur est
l'infinitésimal d'une action géométrique compacte qui préserve exactement la
divergence nulle et commute avec le Laplacien sur l'espace entier.

## 5. Liouville après axisymétrie ou stationnarité

Il faut aussi distinguer deux équations stationnaires.

### 5.1 Stationnaire physique

\[
 -\Delta u+(u\cdot\nabla)u+\nabla p=0,
 \qquad \nabla\cdot u=0\quad\hbox{dans }\mathbb R^3.          \tag{12}
\]

- Koch--Nadirashvili--Seregin--Šverák,
  [DOI 10.1007/s11511-009-0039-6](https://doi.org/10.1007/s11511-009-0039-6),
  donnent des Liouville pour des solutions anciennes sous hypothèses
  supplémentaires, dont des sous-classes axisymétriques; pas de Liouville 3D
  général.
- Korobkov--Pileckas--Russo,
  [DOI 10.1007/s00021-015-0202-0](https://doi.org/10.1007/s00021-015-0202-0),
  annulent les \(D\)-solutions stationnaires axisymétriques **sans swirl**.
- Chae--Weng, *DCDS* **36**(10) (2016), 5267--5285,
  [DOI 10.3934/dcds.2016031](https://doi.org/10.3934/dcds.2016031),
  [arXiv:1512.03491](https://arxiv.org/abs/1512.03491), obtiennent des
  Liouville axisymétriques sous absence de swirl, conditions sur \(u_r/r\),
  ou décroissance/intégrabilité du swirl \(ru_\theta\). L'axisymétrie seule
  ne suffit pas dans leur théorème.
- Chae, *Commun. Math. Phys.* **407**, article 53 (2026),
  [DOI 10.1007/s00220-026-05555-y](https://doi.org/10.1007/s00220-026-05555-y),
  **publié le 5 février 2026**, considère une solution faible ou lisse à
  intégrale de Dirichlet finie et pression de tête
  \(Q=|u|^2/2+p\). Ses théorèmes 1.1--1.2 imposent une borne inférieure
  quantitative sur \(|Q|\) à l'infini et une décroissance de \(u\) ou de
  \(\nabla Q\); ils concluent respectivement \(u=0\) ou \(u\) constant. Ces
  hypothèses ne suivent pas de (Q). La version HTML comporte une coquille
  apparente dans l'affichage (1.2); sa définition quantifiée (1.3) porte bien
  sur \(|x|\to\infty\).
- Wang--Yang,
  [arXiv:2608.06040v1](https://arxiv.org/abs/2608.06040v1), prépublication du
  6 août 2026 déjà cataloguée, déclare explicitement que le Liouville des
  \(D\)-solutions 3D reste ouvert même en axisymétrie. Ils améliorent des
  décroissances axisymétriques et prouvent la nullité sous enveloppes
  cylindriques critiques avec gain logarithmique. Ces enveloppes ne sont pas
  héritées de (Q).

### 5.2 Stationnaire en temps similaire

La conclusion \(\partial_sZ=0\) dans (3) donne, avec \(U(y)=Z(y,s)\),

\[
 -\Delta U+\frac12U+\frac12y\cdot\nabla U
 +(U\cdot\nabla)U+\nabla P=0,
 \qquad \nabla\cdot U=0.                                   \tag{13}
\]

Ce n'est pas (12). Les termes de dérive et d'amortissement interdisent
d'appliquer directement Chae 2026, Chae--Weng ou Wang--Yang.

En revanche, Guevara--Phuc, *Leray's Self-Similar Solutions to the
Navier--Stokes Equations with Profiles in Marcinkiewicz and Morrey Spaces*,
*SIAM J. Math. Anal.* **50**(1) (2018), 541--556,
[DOI 10.1137/16M110099X](https://doi.org/10.1137/16M110099X),
[arXiv:1509.08177v2](https://arxiv.org/abs/1509.08177), démontrent au théorème
1.3

\[
 U\in W^{1,2}_{\rm loc}(\mathbb R^3)\cap L^{q,\infty}(\mathbb R^3),
 \qquad \frac{12}{5}<q<6
 \quad\Longrightarrow\quad U=0.                            \tag{14}
\]

La plage contient \(q=3\). Une fois (11) établie, l'axisymétrie (9) n'est donc
même plus nécessaire au dernier Liouville.

La source cataloguée `NS-SRC-0088`, Ożański--Palasek, *Quantitative Control of
Solutions to the Axisymmetric Navier--Stokes Equations in Terms of the Weak
\(L^3\) Norm*, *Annals of PDE* **9**, article 15 (2023),
[DOI 10.1007/s40818-023-00156-7](https://doi.org/10.1007/s40818-023-00156-7),
[arXiv:2210.10030v3](https://arxiv.org/abs/2210.10030v3), établit pour une
**solution forte axisymétrique** sur \([0,T]\times\mathbb R^3\), sous
\(\|u\|_{L_t^\infty L_x^{3,\infty}}\le A\), des estimations quantitatives de
toutes les dérivées, avec dépendance doublement exponentielle en une puissance
de \(A\). Son corollaire exclut les solutions anciennes axisymétriques
classiques non triviales uniformément faible-\(L^3\).

Cette voie est plus forte que nécessaire une fois (11) acquis, mais moins
robuste au niveau de la notion de solution : `suitable` signifie distribution,
pression locale et inégalité d'énergie locale; cela ne donne pas par
définition une solution forte classique. Il faudrait prouver séparément que la
limite suitable axisymétrique obtenue est dans la classe forte du théorème.
Guevara--Phuc évite ce saut après stationnarité, car son théorème porte
directement sur un profil faible \(W^{1,2}_{\rm loc}\).

## 6. Raccord PDE conditionnel et implication Clay

Considérons une suite \((Z_n,P_n)\) de solutions de (3) sur des cylindres
croissants, ou de solutions exactes plus des défauts PDE tendant vers zéro.
Le raccord sûr exige séparément :

1. \(Z_n\to Z\) fortement dans \(L^3_{\rm loc}\), donc
   \(Z_n\otimes Z_n\to Z\otimes Z\) fortement dans
   \(L^{3/2}_{\rm loc}\);
2. \(P_n\rightharpoonup P\) dans \(L^{3/2}_{\rm loc}\), après normalisation
   locale de la pression et recalcul par la projection de Leray;
3. \(\nabla Z_n\rightharpoonup\nabla Z\) dans \(L^2_{\rm loc}\), avec les
   bornes temporelles nécessaires;
4. passage de l'inégalité d'énergie locale, pour conserver le caractère
   faible adapté;
5. borne globale uniforme
   \(\sup_{n,s}\|Z_n(s)\|_{L^{3,\infty}(\mathbb R^3)}<\infty\), pour obtenir
   \(U\in L^{3,\infty}\), et non seulement \(L^3_{\rm loc}\);
6. normalisation de concentration garantissant \(Z\ne0\).

Sous 1--5, le lemme 0057-L et (14) donnent \(Z=0\). Sous 1--6, ils donnent une
contradiction. La chaîne transférable est donc

\[
 \begin{aligned}
 &\text{compacité adaptée + défaut de phase vanissant + }|\beta_n|\to\infty\\
 &\quad\Longrightarrow
 \text{profil BSS axisymétrique faible-}L^3
 \Longrightarrow U=0.                                      \tag{15}
 \end{aligned}
\]

**Écart Clay.** Aucun résultat audité ne montre qu'un blow-up éventuel de (1)
produit une suite satisfaisant simultanément le défaut de phase de (Q), la
forte compacité locale, la borne globale faible-\(L^3\) et la non-trivialité.
Le scénario Type II et les concentrations multi-échelles restent entièrement
hors de (15). Exclure cette voie de profil ne résout donc pas le problème Clay.

## 7. Passe contradictoire et résidus certifiés

### Test A — un supremum de vitesse divergent ne suffit pas

Choisir un champ \(U\in C_c^\infty(\mathbb R^3)^3\), divergence-free et non
axisymétrique, donc \(\mathcal RU\ne0\). Pour
\(\chi\in C_c^\infty((-1,1))\), poser sur un intervalle contenant \(s_0\)

\[
 Z_n(s,y)=U(y),\qquad
 \beta_n(s)=n\chi(n^2(s-s_0)).                              \tag{16}
\]

Alors \(Z_n\to U\) fortement dans tout \(L^3_{\rm loc}\) et
\(\sup_s|\beta_n(s)|=n\|\chi\|_\infty\to\infty\), mais

\[
 r_n=-\beta_n\mathcal RU,qquad
 \|r_n\|_{L^1_sL^3_y}
 =\frac{\|\chi\|_{L^1}\|\mathcal RU\|_{L^3}}{n}
 \longrightarrow0.                                         \tag{17}
\]

La limite \(U\) n'est pas axisymétrique. Le résidu (17) est exact; il réfute
l'interprétation « vitesse grande quelque part ». Il ne réfute pas le lemme,
où chaque \(\beta_n\) est une constante de module divergent.

### Test B — résidu borné n'implique pas stationnarité

Prendre un champ axisymétrique divergence-free non nul \(U\) et une fonction
lisse non constante \(h(s)\). Poser

\[
 Z_n=h(s)U,qquad \beta_n=n.
\]

Comme \(\mathcal RZ_n=0\),

\[
 r_n=h'(s)U.                                                  \tag{18}
\]

Le défaut est uniformément borné et la limite est axisymétrique, mais elle
n'est pas stationnaire. La convergence \(r_n\to0\), pas une simple borne, est
nécessaire pour (11).

### Test C — la rotation rapide exacte détruit la compacité forte

Pour un \(U\) non axisymétrique, poser

\[
 Z_n(s)=\rho_{ns}U,qquad \beta_n=n,qquad r_n=0.             \tag{19}
\]

La moyenne faible temporelle peut converger vers \(\mathcal AU\), mais la
partie \((I-\mathcal A)Z_n\) conserve sa taille sur les compacts invariants par
rotation. Elle ne converge pas fortement vers zéro dans
\(L^3_{s,y,\rm loc}\). Ainsi la forte compacité de (Q) est une vraie hypothèse
de rigidité, pas une conséquence automatique des oscillations. Avec une seule
convergence faible, le produit quadratique peut conserver un défaut de
Reynolds.

### Test D — fuite de concentration

La suite \(U_n(y)=U(y-ne_1)\) conserve sa norme globale
\(L^{3,\infty}\) mais converge fortement vers zéro sur tout compact. Ce test
ne satisfait pas en général le défaut rotationnel (Q); il attaque le maillon
suivant : même une limite adaptée et stationnaire peut être triviale si la
normalisation n'empêche pas translations, changements d'échelle ou
intermittence.

## 8. Delta bibliographique

### Sources primaires importantes absentes du catalogue avant ce cycle

1. Babin--Mahalov--Nicolaenko 1999,
   [DOI 10.1512/iumj.1999.48.1856](https://doi.org/10.1512/iumj.1999.48.1856) :
   rotation de Coriolis rapide et régularité globale sur domaines résonants.
2. Gallagher--Saint-Raymond 2003,
   [DOI 10.1016/S1631-073X(03)00066-9](https://doi.org/10.1016/S1631-073X(03)00066-9) :
   convergence faible de solutions de Leray sous pénalisation rotationnelle
   inhomogène.
3. Gallagher--Higaki--Maekawa 2019,
   [DOI 10.1002/mana.201700400](https://doi.org/10.1002/mana.201700400),
   [arXiv:1710.01029](https://arxiv.org/abs/1710.01029) : générateur de repère
   tournant, Fourier angulaire, couche limite et axisymétrisation quantitative.
4. Gallay 2018,
   [DOI 10.1007/s00205-018-1262-0](https://doi.org/10.1007/s00205-018-1262-0),
   [arXiv:1707.05525](https://arxiv.org/abs/1707.05525) : dissipation renforcée
   et axisymétrisation 2D autour du vortex d'Oseen.
5. Korobkov--Pileckas--Russo 2015,
   [DOI 10.1007/s00021-015-0202-0](https://doi.org/10.1007/s00021-015-0202-0),
   et Chae--Weng 2016,
   [DOI 10.3934/dcds.2016031](https://doi.org/10.3934/dcds.2016031) : frontières
   publiées du Liouville stationnaire axisymétrique.
6. Chae 2026,
   [DOI 10.1007/s00220-026-05555-y](https://doi.org/10.1007/s00220-026-05555-y) :
   Liouville stationnaire récent sous hypothèses de pression de tête et de
   décroissance.

### Sources cataloguées réutilisées, sans nouvelle revendication

- Beyn--Thümmler 2004, DOI `10.1137/030600515`;
- Bradshaw--Tsai 2017, DOI `10.1080/03605302.2017.1323922`;
- Guevara--Phuc 2018, DOI `10.1137/16M110099X`;
- Koch--Nadirashvili--Seregin--Šverák 2009, DOI
  `10.1007/s11511-009-0039-6`;
- Ożański--Palasek 2023, DOI `10.1007/s40818-023-00156-7`;
- Pineau--Vicol, `arXiv:2607.09619v2`;
- Wang--Yang, `arXiv:2608.06040v1`.

## 9. Recherche d'absence et traçabilité

La recherche bornée a croisé, dans arXiv, pages d'éditeurs, Numdam et chaînes
de références primaires : `fast rotation`, `angular averaging`, `unbounded
phase speed`, `freezing method`, `relative equilibrium compactness`, `rotating
Navier--Stokes`, `axisymmetrization`, `high-frequency group action`,
`stationary axisymmetric Liouville`, `rotated self-similar` et `suitable weak
L3`. Aucune source trouvée ne réunit simultanément :

1. le générateur (4) en variables backward similaires;
2. des vitesses constantes \(|\beta_n|\to\infty\);
3. un défaut \(r_n\to0\);
4. une forte compacité \(L^3_{\rm loc}\);
5. la stabilité de solutions faibles adaptées;
6. les conclusions (V1).

Cette absence est un résultat de veille borné, non une preuve d'inexistence
absolue. Le lemme 0057-L rend toutefois inutile la recherche d'un théorème PDE
pour les points 1--4 pris isolément : la vraie question bibliographique et
analytique restante est désormais la production de ces hypothèses depuis une
suite Clay.

Textes primaires téléchargés et contrôlés :

| Texte | SHA-256 | Contrôle |
|---|---|---|
| Gallagher--Saint-Raymond 2003, PDF Numdam | `399FED4093C9FD3D4BBF0C6773044C0C44572A81E26845EFEDAD10EE1858FD48` | équation, théorème 1.1, noyau de la pénalisation et première page rendue visuellement |
| Gallagher--Higaki--Maekawa, `arXiv:1710.01029v1` | `E10A0846A9A783883D5541E724753B020D23532A7BA060D26F3EA6F446C73103` | équation \((NS_\alpha)\), théorèmes 1.1--1.3, estimations modales et première page rendue visuellement |
| Wang--Yang, `arXiv:2608.06040v1` | `CBB95814EE44689142303B7ECF46199F79413AE08FE8DBD148EFA4EE2D2C3918` | équation stationnaire, théorèmes 1.1, 1.5, 1.6 et première page rendue visuellement |

La version de référence HTML ouverte de Chae 2026 a été contrôlée directement
sur la page de l'éditeur : équation (1.1), théorèmes 1.1--1.2, date de
publication et DOI. Le point d'accès PDF a renvoyé une page anti-JavaScript et
n'a donc pas été compté comme texte PDF vérifié.

## 10. Décision scientifique

**Résultat positif borné :** le maillon

\[
 \boxed{\ |\beta_n|\to\infty\ \text{(constantes)},\quad
 r_n\to0,\quad Z_n\to Z\text{ dans }\mathcal D'
 \Longrightarrow \mathcal RZ=0,\ \partial_sZ=0\ }
\]

est fermé par une preuve courte et falsifiable.

**Résultat négatif :** aucun transfert automatique n'existe depuis la rotation
physique rapide, la rotation d'un obstacle, une jauge de phase à vitesse
divergente ou un Liouville stationnaire standard vers ce lemme de profil.

**Prochain verrou recommandé :** formuler puis tester un lemme de
non-dégénérescence disant qu'une séquence de zooms suitable normalisée,
fortement compacte en \(L^3_{\rm loc}\), ne peut converger vers zéro après
projection angulaire. Le test décisif doit inclure translations, deux bulles à
échelles séparées et pression non locale. Sans ce maillon, (15) n'exclut qu'un
canal compact déjà conditionnel et ne produit aucun progrès global Clay.
