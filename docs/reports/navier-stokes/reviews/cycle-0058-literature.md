# Cycle 0058 — dérivée temporelle, compacité de Bochner et rotation rapide de profil

**Date de coupure :** 15 août 2026
**Nature :** veille primaire indépendante, audit d'implication et passe
contradictoire
**Périmètre :** bornes de dérivée temporelle pour Navier–Stokes 3D,
Aubin–Lions–Simon, pénalisation à grand coefficient et générateur de rotation
de profil
**Question active :** une hypothèse de type Bochner ferme-t-elle le passage

\[
  \beta_n(s)\,\mathcal R Z_n
  =\partial_s Z_n-r_n,
  \qquad \operatorname*{ess\,inf}_{s\in I}|\beta_n(s)|\longrightarrow\infty,
  \tag{Q}
\]

vers une limite axisymétrique, puis stationnaire ?

## Verdict

1. **Aucun résultat primaire identifié n'énonce exactement le théorème PDE
   complet recherché** : suite de solutions locales faibles adaptées ou de
   Leray, générateur géométrique de rotation de profil \(\mathcal R\), vitesse
   mesurable \(\beta_n(s)\) uniformément divergente, bornes Bochner, limite
   axisymétrique et stationnaire, puis conservation de l'admissibilité. Les
   sources trouvées donnent séparément la compacité temporelle, les bornes de
   dérivée, la stabilité *suitable*, ou des limites de Coriolis.

2. **Le maillon cinématique est cependant fermé par un lemme élémentaire du
   laboratoire dans un espace de Bochner complet.** Si, pour un espace de
   Banach spatial \(X\),

   \[
     \sup_n\bigl(
       \|\partial_s Z_n\|_{L^q(I;X)}+
       \|r_n\|_{L^q(I;X)}
     \bigr)<\infty,
     \qquad
     b_n:=\operatorname*{ess\,inf}_{I}|\beta_n|\to\infty,
     \tag{B}
   \]

   alors

   \[
     \|\mathcal RZ_n\|_{L^q(I;X)}
     \le b_n^{-1}
       \bigl(\|\partial_s Z_n\|_{L^q(I;X)}+
             \|r_n\|_{L^q(I;X)}\bigr)
     \longrightarrow0.                                      \tag{C}
   \]

   Aucune dérivée de \(\beta_n^{-1}\) n'apparaît : l'identité (Q) est
   divisée comme égalité de fonctions de Bochner, et non après intégration par
   parties d'une dérivée seulement distributionnelle. Si
   \(Z_n\to Z\) dans les distributions et \(\mathcal R\) est continu dans ce
   sens, alors \(\mathcal RZ=0\).

3. **La stationnarité exige davantage.** Pour la moyenne angulaire de Haar
   \(\mathcal A\), on a

   \[
     \partial_s\mathcal AZ_n=\mathcal A r_n.                 \tag{D}
   \]

   Donc \(\mathcal RZ=0\), puis \(\mathcal AZ=Z\), mais
   \(\partial_sZ=0\) ne suit que si
   \(\mathcal Ar_n\to0\) dans les distributions — en particulier si
   \(r_n\to0\). Une borne uniforme de \(r_n\) seule ne suffit pas.

4. **L'espace dual est une hypothèse mathématique, pas une commodité de
   notation.** Une estimation de \(\partial_sZ_n\) obtenue uniquement contre
   des tests solénoïdaux donne l'annulation de la projection de Leray de
   \(\mathcal RZ\), et non nécessairement \(\mathcal RZ=0\) localement. Pour
   une conclusion vectorielle locale sans ambiguïté de gradient, il faut soit
   contrôler la pression et écrire l'équation complète dans un espace négatif,
   soit travailler globalement avec une classe d'intégrabilité qui élimine les
   gradients harmoniques.

5. **Aubin–Lions–Simon fournit la compacité forte, mais ne crée ni la borne de
   dérivée, ni la pression, ni l'inégalité d'énergie locale.** Dans le paquet
   énergétique 3D usuel, la voie sûre est

   \[
     L^2(I;H^1(K))\cap W^{1,4/3}(I;H^{-1}(K))
       \Subset L^2(I;L^2(K)),                               \tag{E}
   \]

   puis interpolation avec la borne \(L^{10/3}\) pour obtenir la convergence
   forte dans tout \(L^p\), \(p<10/3\), notamment \(L^3\). Le passage à une
   limite faible adaptée requiert encore un contrôle de pression et le passage
   de l'inégalité d'énergie locale.

6. **Les théorèmes de rotation rapide physique ne couvrent pas (Q).** Ils
   pénalisent l'opérateur de Coriolis projeté \(\mathbb P(Ju)\), dont le noyau
   est géostrophique, tandis que \(\mathcal R=J-(Jy\cdot\nabla)\) est le
   générateur de l'action combinée sur un profil. De plus, l'équation physique
   non filtrée contient typiquement \(\varepsilon^{-1}\mathbb P(Ju)\), de
   sorte qu'une borne uniforme de \(\partial_tu_\varepsilon\) n'est précisément
   pas une conséquence de l'énergie.

Le résultat de ce cycle est donc **positif pour l'annulation du générateur sous
bornes Bochner complètes**, **conditionnel pour la stationnarité**, et
**négatif quant à l'existence d'un théorème publié couvrant tout le raccord
Clay**. Le statut approprié du lemme est `AI_DERIVATION` ou équivalent, jamais
`PAPER_PROOF`.

## 1. Cadre exact et échelle

Le cadre PDE de raccord est Navier–Stokes incompressible 3D, viscosité un,
sans force, sur \(\mathbb R^3\) ou sur un cylindre intérieur :

\[
  \partial_tu-\Delta u+(u\cdot\nabla)u+\nabla p=0,
  \qquad \nabla\cdot u=0.                                  \tag{1.1}
\]

Sous les variables backward auto-similaires

\[
  y=\frac{x}{\sqrt{-t}},\qquad s=-\log(-t),\qquad
  V(y,s)=\sqrt{-t}\,u(x,t),\qquad P(y,s)=(-t)p(x,t),
\]

l'équation devient

\[
  \partial_sV-\Delta V+\frac12V+\frac12y\cdot\nabla V
  +(V\cdot\nabla)V+\nabla P=0,
  \qquad \nabla\cdot V=0.                                 \tag{1.2}
\]

Pour les rotations autour de \(e_3\), avec \(R_\theta\in SO(3)\) et
\(J=R'_0\),

\[
  (\rho_\theta Z)(y,s)=R_\theta Z(R_{-\theta}y,s),
  \qquad
  \mathcal RZ=JZ-(Jy\cdot\nabla)Z.                         \tag{1.3}
\]

L'action \(\rho_\theta\) et \(\mathcal R\) préservent la divergence. Sur
un intervalle \(I\) et une boule \(B_R\) centrée sur l'axe, \(s\),
\(\partial_s\), \(\beta_n\) et \(\mathcal R\) sont sans dimension dans les
variables (1.2). Le facteur \(y\) de \(\mathcal R\) est borné sur \(B_R\),
mais toute constante d'opérateur locale peut dépendre de \(R\); il n'existe
pas d'uniformité automatique quand \(R\to\infty\).

Les normes \(L^3_x\) de vitesse et \(L^{3/2}_x\) de pression sont critiques
sous l'échelle Clay

\[
  u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),
  \qquad p_\lambda(x,t)=\lambda^2p(\lambda x,\lambda^2t).
\]

Les bornes d'énergie locales utilisées ci-dessous sont supercritiques par
rapport à cette échelle; elles servent à la compacité, pas à une estimation
globale critique nouvelle.

## 2. Lemme minimal transférable : effondrement Bochner du générateur

### Énoncé borné

Soient \(I\subset\mathbb R\) un intervalle borné, \(X\) un espace de Banach
continûment injecté dans \(\mathcal D'(B_R)^3\), \(1\le q\le\infty\), et
\(Z_n,r_n\) tels que

\[
  \partial_sZ_n,r_n\in L^q(I;X),
  \qquad
  \beta_n\mathcal RZ_n=\partial_sZ_n-r_n
  \quad\hbox{dans }L^q(I;X).                               \tag{2.1}
\]

Supposons \(\beta_n:I\to\mathbb R\) mesurable et

\[
  b_n=\operatorname*{ess\,inf}_{s\in I}|\beta_n(s)|\to\infty,
  \qquad
  \sup_n(\|\partial_sZ_n\|_{L^qX}+\|r_n\|_{L^qX})<\infty. \tag{2.2}
\]

Alors (C) vaut. Si \(Z_n\to Z\) dans \(\mathcal D'(I\times B_R)^3\), alors
\(\mathcal RZ=0\) dans ce cylindre.

### Preuve auditée

La fonction \(\beta_n^{-1}\) appartient à \(L^\infty(I)\), avec
\(\|\beta_n^{-1}\|_\infty\le b_n^{-1}\). La multiplication scalaire agit
continûment sur \(L^q(I;X)\). L'identité (2.1) donne donc directement

\[
  \mathcal RZ_n=\beta_n^{-1}(\partial_sZ_n-r_n)
\]

et l'inégalité triangulaire donne (C). Enfin, la continuité de l'opérateur
différentiel \(\mathcal R:\mathcal D'\to\mathcal D'\) identifie la limite.
La preuve ne requiert ni signe constant de \(\beta_n\), ni
\(\partial_s\beta_n\), ni compacité forte de \(Z_n\).

### Stationnarité

Sur une boule invariante par rotation, définissons

\[
  \mathcal AZ=\frac1{2\pi}\int_0^{2\pi}\rho_\theta Z\,d\theta.
\]

On a \(\mathcal A\mathcal R=0\),
\(\ker\mathcal R=\operatorname{Ran}\mathcal A\) et
\(\mathcal A\partial_s=\partial_s\mathcal A\). L'application de
\(\mathcal A\) à (2.1) donne (D). Par conséquent :

- si \(r_n\to0\) dans \(\mathcal D'\), alors
  \(\partial_s\mathcal AZ=0\), et \(\mathcal RZ=0\) implique
  \(\mathcal AZ=Z\), donc \(\partial_sZ=0\) ;
- si seulement \(r_n\) est borné dans \(L^q(I;X)\), on obtient
  l'axisymétrie mais aucune stationnarité.

Ce découplage doit apparaître explicitement dans toute affirmation du
laboratoire : « grand coefficient + dérivée bornée » sélectionne le noyau de
\(\mathcal R\); « moyenne angulaire du résidu tendant vers zéro » gèle le
temps similaire.

## 3. Dérivée temporelle de Navier–Stokes : ce que donne réellement l'énergie

### 3.1 Équation projetée, tests solénoïdaux

Sur un domaine borné régulier ou \(\mathbb T^3\), notons \(H\) la fermeture
dans \(L^2\) des champs solénoïdaux et \(V\) celle dans \(H^1\). Une solution
de Leray–Hopf vérifie

\[
  u\in L^\infty(0,T;H)\cap L^2(0,T;V).
\]

Pour \(\varphi\in V\), l'interpolation 3D et Sobolev donnent

\[
  |\langle (u\cdot\nabla)u,\varphi\rangle|
  \le C\|u\|_2^{1/2}\|\nabla u\|_2^{3/2}\|\nabla\varphi\|_2.
  \tag{3.1}
\]

Le terme non linéaire appartient donc à \(L^{4/3}(0,T;V')\), le terme
visqueux à \(L^2(0,T;V')\), et l'équation projetée implique

\[
  \partial_tu\in L^{4/3}(0,T;V').                          \tag{3.2}
\]

Cette estimation est indépendante d'une normalisation de pression parce que
la pression a été supprimée par les tests solénoïdaux. Elle ne doit pas être
réécrite silencieusement comme une identité dans
\(W^{-1,4/3}(\Omega)^3\) contre tous les tests.

### 3.2 Équation complète locale et pression

Pour une solution faible adaptée intérieure, le paquet usuel est localement

\[
 u\in L^\infty_tL^2_x\cap L^2_tH^1_x,
 \qquad p\in L^{3/2}_{t,x}.
 \tag{3.3}
\]

Il entraîne \(u\in L^{10/3}_{t,x}\) et
\(u\otimes u\in L^{5/3}_{t,x}\). Sur un cylindre strictement intérieur,
l'équation complète

\[
 \partial_tu=\Delta u-\operatorname{div}(u\otimes u)-\nabla p
 \tag{3.4}
\]

donne, après restriction par une coupure, une borne dans un espace négatif
complet; un choix conservateur sur une boule bornée est

\[
 \partial_tu\in L^{3/2}(I;W^{-1,3/2}(B_R)^3).              \tag{3.5}
\]

Les plongements utilisés ici dépendent du cylindre fixé. Dans les variables
similaires, les termes \(V\) et \(y\cdot\nabla V\) sont d'ordre inférieur sur
chaque \(B_R\) et entrent dans le même type d'espace négatif avec constante
dépendant de \(R\). Le contrôle de \(\nabla P\) reste indispensable pour
l'identité contre tous les tests.

### 3.3 Défaut exact des seuls tests solénoïdaux

Si un champ distributionnel \(F\) annule tous les tests compacts
solénoïdaux, alors localement \(F=\nabla h\); si en plus
\(\nabla\cdot F=0\), \(h\) est harmonique. Cela n'impose pas \(F=0\).

Le défaut n'est pas abstrait. Prenons le champ constant divergence-free
\(Z=-e_2\). Le terme spatial de (1.3) s'annule et

\[
  \mathcal RZ=J(-e_2)=e_1=\nabla y_1\ne0.                  \tag{3.6}
\]

Or \(e_1\) annule tout test compact solénoïdal. Ainsi une identité pénalisée
connue seulement dans \(V'_\sigma(B_R)\) peut être satisfaite modulo gradient
sans établir l'axisymétrie locale du profil. Sur \(\mathbb R^3\), une
intégrabilité globale appropriée peut éliminer un gradient harmonique entier;
elle doit être énoncée et prouvée, non présumée.

## 4. Compacité : théorèmes primaires et chaîne exacte

### Jacques Simon, 1986

**Source primaire publiée :** Jacques Simon, *Compact Sets in the Space
\(L^p(0,T;B)\)*, *Annali di Matematica Pura ed Applicata* 146 (1986),
65–96, DOI
[10.1007/BF01762360](https://doi.org/10.1007/BF01762360).

Le corollaire 4 du texte établit notamment : si
\(X\Subset B\hookrightarrow Y\), si une famille est bornée dans
\(L^p(0,T;X)\), \(1\le p<\infty\), et si sa dérivée est bornée dans
\(L^1(0,T;Y)\), alors elle est relativement compacte dans
\(L^p(0,T;B)\). Pour une borne \(L^\infty_tX\) et une dérivée
\(L^r_tY\), \(r>1\), le même corollaire donne une compacité dans
\(C(0,T;B)\). Le théorème est fonctionnel et ne mentionne ni pression, ni
solution faible adaptée, ni rotation.

**Application exacte à la suite énergétique :** avec
\(X=H^1(B_R)\), \(B=L^2(B_R)\), \(Y=H^{-1}(B_R)\), les bornes
\(L^2_tH^1_x\) et \(L^{4/3}_tH^{-1}_x\) donnent une sous-suite fortement
convergente dans \(L^2_tL^2_x\). La borne énergétique donne aussi
\(L^{10/3}_{t,x}\); par interpolation,

\[
  Z_n\to Z\quad\hbox{fortement dans }L^p(I\times B_R)
  \quad\text{pour tout }p<10/3.                            \tag{4.1}
\]

En particulier \(p=3\) est accessible, mais pas l'endpoint \(10/3\).

**Antécédent primaire :** Jean-Pierre Aubin, *Un théorème de compacité*,
*Comptes rendus de l'Académie des sciences de Paris* 256 (1963), 5042–5044,
[copie du texte](https://heuklyd.github.io/papers/pdf/Aubin-1963.pdf), publié,
sans DOI identifié. Pour l'usage exact ci-dessus, Simon fournit l'énoncé le
plus directement vérifiable.

### Berselli–Fagioli–Spirito, 2019

**Source primaire publiée :** Luigi C. Berselli, Simone Fagioli et Stefano
Spirito, *Suitable weak solutions of the Navier–Stokes equations constructed
by a space–time numerical discretization*, *Journal de Mathématiques Pures et
Appliquées* 125 (2019), 189–208, DOI
[10.1016/j.matpur.2018.09.004](https://doi.org/10.1016/j.matpur.2018.09.004),
[arXiv:1710.01579v2](https://arxiv.org/abs/1710.01579), article publié.

L'équation est Navier–Stokes incompressible 3D, viscosité un, sur
\(\mathbb T^3\), sans force dans le corps principal; la remarque 1.2 autorise
des forces convenables. Le schéma est une discrétisation complète : méthode
\(\theta\) en temps, \(1/2<\theta\le1\), et familles spécifiques d'éléments
finis en espace. Le théorème 1.1 suppose en outre
\(u_0\in H^1_{\rm div}\) et les propriétés discrètes de commutation et de
stabilité précisées à la section 3.1 de l'article.

La proposition 4.4 donne, uniformément en \(h,\Delta t\),

\[
\begin{aligned}
 &\|v_h^{\Delta t}\|_{L^\infty_tL^2_x}\le C,\\
 &\|u_h^{\Delta t}\|_{L^\infty_tL^2_x\cap L^2_tH^1_x}\le C,\\
 &\|p_h^{\Delta t}\|_{L^{4/3}_tL^2_x}\le C,\\
 &\|\partial_tv_h^{\Delta t}\|_{L^{4/3}_tH^{-1}_x}\le C.
\end{aligned}                                                \tag{4.2}
\]

Le théorème 1.1 extrait une limite avec convergence forte
\(L^2((0,T)\times\mathbb T^3)\), convergence faible du gradient en \(L^2\),
pression faible dans \(L^{4/3}_tL^2_x\), et démontre que le couple limite est
une solution faible adaptée. La convenabilité n'est pas une conséquence du
seul Aubin–Lions : la preuve utilise les propriétés de commutation du schéma
et passe séparément l'inégalité d'énergie locale.

**Non-transfert :** ce résultat ne porte ni sur une suite arbitraire de
solutions adaptées, ni sur le générateur \(\mathcal R\), ni sur une
pénalisation \(\beta_n\mathcal RZ_n\). Il fournit cependant un exemple
primaire exact où le paquet « pression + dérivée négative + compacité forte +
énergie locale » est suivi jusqu'à la limite.

### Albritton–Barker, 2020 (`NS-SRC-0187`)

**Source primaire publiée :** Dallas Albritton et Tobias Barker, *Localised
Necessary Conditions for Singularity Formation in the Navier–Stokes
Equations with Curved Boundary*, *Journal of Differential Equations* 269
(2020), 7529–7573, DOI
[10.1016/j.jde.2020.06.009](https://doi.org/10.1016/j.jde.2020.06.009),
[arXiv:1811.00507v2](https://arxiv.org/abs/1811.00507), article publié.

Le lemme A.2 traite des solutions faibles adaptées au bord des équations de
Navier–Stokes aplaties dans un demi-cylindre. Sous les bornes uniformes

\[
  \|v^{(k)}\|_{L^3(Q^+(R))}
  +\|q^{(k)}\|_{L^{3/2}(Q^+(R))}\le M                     \tag{4.3}
\]

et la convergence \(C^2\) des aplatissements, il extrait, sur tout cylindre
strictement plus petit, une convergence forte \(L^3\) de la vitesse, faible
\(L^{3/2}\) de la pression, vers une solution faible adaptée. Les auteurs
indiquent que la preuve combine l'inégalité d'énergie locale et Aubin–Lions.

**Portée exacte :** c'est un théorème publié de compacité locale adaptée avec
pression, y compris au bord. Il n'énonce aucune rotation de profil ni grand
coefficient. Ses hypothèses fortes \(L^3/L^{3/2}\) ne sont pas produites par
une seule borne faible \(L^{3,\infty}\).

## 5. Grand coefficient : Coriolis physique versus rotation de profil

| Source primaire | Opérateur grand | Information uniforme | Limite sélectionnée | Pourquoi ce n'est pas (Q) |
|---|---|---|---|---|
| Babin–Mahalov–Nicolaenko, *Indiana Univ. Math. J.* 48 (1999), DOI [10.1512/iumj.1999.48.1856](https://doi.org/10.1512/iumj.1999.48.1856), publié (`NS-SRC-0211`) | Coriolis physique, après projection | estimations et dynamique résonante dans les domaines de l'article | système résonant / régularité forte sous rotation rapide | autre équation, autre noyau, solution forte, aucun paquet *suitable* local |
| Gallagher–Saint-Raymond, *C. R. Math.* 336 (2003), DOI [10.1016/S1631-073X(03)00066-9](https://www.numdam.org/articles/10.1016/S1631-073X%2803%2900066-9/), publié (`NS-SRC-0212`) | \(\varepsilon^{-1}u\times B\), projeté dans l'équation incompressible inhomogène | énergie de Leray uniforme et relations de défaut pondérées par \(\varepsilon\) | noyau de l'opérateur de Coriolis projeté, avec compacité compensée | \(\partial_tu_\varepsilon\) non uniformément bornée dans la variable non filtrée; noyau géostrophique, pas \(\ker\mathcal R\) |
| Gallagher–Higaki–Maekawa, *Math. Nachr.* 292 (2019), DOI [10.1002/mana.201700400](https://doi.org/10.1002/mana.201700400), [arXiv:1710.01029](https://arxiv.org/abs/1710.01029), publié (`NS-SRC-0213`) | rotation d'un obstacle, modes angulaires | estimations modales et couche limite | suppression quantitative de modes non nuls dans un problème stationnaire 2D | domaine extérieur à bord, dimension 2, problème elliptique stationnaire |
| Bradshaw–Tsai, *Adv. Differential Equations* 22 (2017), DOI [10.1080/03605302.2017.1323922](https://doi.org/10.1080/03605302.2017.1323922), publié (catalogue existant) | symétrie rotatoirement auto-similaire exacte à vitesse fixée | construction de solutions faibles dans la classe imposée | profil rotatoirement auto-similaire | ne traite ni \(|\beta_n|\to\infty\), ni résidu, ni compacité de Bochner |
| Pineau–Vicol, [arXiv:2607.09619v2](https://arxiv.org/abs/2607.09619), prépublication v2 (`NS-SRC-0051`) | rotation exacte dans les profils backward RSS/RDSS | borne Type I et régimes de rotation extrêmes | exclusion de sous-classes de profils lisses exacts | auto-similarité imposée; pas de suite *suitable* approximative ni théorème (Q) |

L'équation de Coriolis projetée schématique

\[
  \partial_tu_\varepsilon+\varepsilon^{-1}\mathbb P(Ju_\varepsilon)
  =F_\varepsilon                                             \tag{5.1}
\]

ne donne une borne uniforme de \(\partial_tu_\varepsilon\) que si le terme
rapide est déjà contrôlé, ce qui est précisément la conclusion recherchée.
Les travaux de limite rapide emploient filtrage oscillant, analyse spectrale,
dispersion ou compacité compensée. Les citer comme preuve d'une borne Bochner
non filtrée serait circulaire.

Par contraste, dans (Q), une borne uniforme de \(\partial_sZ_n\) est une
hypothèse coercive additionnelle : associée à la borne de \(r_n\), elle
interdit directement les oscillations rapides hors du noyau de
\(\mathcal R\).

## 6. Passe contradictoire reproductible

### Test A — pointe de vitesse : l'ess-inf est nécessaire

Soient \(U\in C_c^\infty(B_R)^3\) divergence-free et non axisymétrique,
\(s_0\in I\), et \(\chi\in C_c^\infty((-1,1))\). Posons

\[
  Z_n(s,y)=U(y),\qquad
  \beta_n(s)=n\chi(n^2(s-s_0)),\qquad
  r_n=-\beta_n\mathcal RU.                                 \tag{6.1}
\]

Alors \(\partial_sZ_n=0\), l'identité (Q) est exacte,
\(\sup_s|\beta_n(s)|\sim n\), et

\[
  \|r_n\|_{L^1(I;L^3(B_R))}
   =n^{-1}\|\chi\|_{L^1}\|\mathcal RU\|_{L^3}.           \tag{6.2}
\]

Le résidu tend vers zéro mais \(Z_n\to U\) non axisymétrique. Ce test réfute
la substitution de \(\sup|\beta_n|\to\infty\) à
\(\operatorname{ess\,inf}|\beta_n|\to\infty\). Il ne réfute pas le lemme
Bochner, car \(\beta_n^{-1}\notin L^\infty\).

### Test B — résidu borné : la stationnarité ne suit pas

Soient \(U\) un champ axisymétrique divergence-free non nul et
\(h\in C_c^\infty(I)\) non constant. Posons

\[
  Z_n(s,y)=h(s)U(y),\qquad \beta_n=n,
  \qquad r_n=h'(s)U(y).                                    \tag{6.3}
\]

Alors \(\mathcal RZ_n=0\), (Q) est exacte,
\(\partial_sZ_n\) et \(r_n\) sont uniformément bornés dans tous les espaces
de Bochner naturels, mais la limite dépend de \(s\). Ce test réfute
« résidu borné \(\Rightarrow\) stationnarité ». Il confirme que le bon terme
à faire tendre vers zéro est \(\mathcal Ar_n\).

### Test C — tests solénoïdaux : la pression ne peut être oubliée localement

Le champ (3.6) vérifie

\[
  \langle \mathcal RZ,\varphi\rangle
   =\int_{B_R}e_1\cdot\varphi\,dy=0
\]

pour tout \(\varphi\in C_c^\infty(B_R)^3\) avec
\(\nabla\cdot\varphi=0\), alors que \(\mathcal RZ=e_1\ne0\). Ce test réfute
le passage d'une annulation dans le dual solénoïdal à l'annulation vectorielle
locale. Le résidu après projection de Leray ne suffit pas sans jauge de
pression ou condition globale.

### Test D — rayon du domaine : absence d'uniformité cachée

Sur \(B_R\), l'adjoint de \((Jy\cdot\nabla)\) contient un coefficient de
taille \(O(R)\). Une preuve locale sur chaque \(B_R\) ne donne donc pas une
borne uniforme sur \(\mathbb R^3\). Le passage \(R\to\infty\) doit suivre
séparément les normes et la pression; l'inégalité (C), elle, reste uniforme
seulement si l'espace \(X\) et la borne de (2.2) le sont.

## 7. Implication recommandée pour le graphe de preuve

La chaîne suivante est exacte si chaque hypothèse est consignée :

\[
\begin{array}{c}
 Z_n\text{ bornée dans }L^2_sH^1_y
 \quad+\quad
 \partial_sZ_n\text{ bornée dans }L^{4/3}_sH^{-1}_y
 \\
 \Downarrow\ \text{Simon}\quad
 Z_n\to Z\text{ fortement dans }L^2_{s,y}
 \quad\stackrel{L^{10/3}\text{ uniforme}}{\Longrightarrow}\quad
 Z_n\to Z\text{ fortement dans }L^3_{s,y}
 \\
 \Downarrow\quad
 Z_n\otimes Z_n\to Z\otimes Z\text{ dans }L^{3/2}_{s,y}
 \\
 \beta_n\mathcal RZ_n=\partial_sZ_n-r_n
 \text{ dans un espace négatif complet},\quad
 \operatorname*{ess\,inf}|\beta_n|\to\infty,\quad r_n\text{ borné}
 \\
 \Downarrow\quad
 \mathcal RZ=0
 \\
 \mathcal Ar_n\to0
 \quad\Longrightarrow\quad
 \partial_sZ=0.
\end{array}                                                  \tag{7.1}
\]

Pour que (7.1) produise une solution faible adaptée admissible, il faut encore
ajouter : pression normalisée bornée dans \(L^{3/2}_{\rm loc}\), convergence
faible correspondante, borne locale de gradient, passage de l'inégalité
d'énergie locale et non-trivialité de la limite. Albritton–Barker fournit un
paquet publié de stabilité sous bornes fortes \(L^3/L^{3/2}\); il ne produit
pas ces bornes depuis une hypothèse Clay endpoint plus faible.

## 8. Delta de sources recommandé — sans modification du catalogue

### À ajouter en priorité

1. **Jacques Simon, 1986** — source fonctionnelle primaire exacte pour le
   maillon compacité temporelle.

   - DOI : `10.1007/BF01762360`
   - URL : https://doi.org/10.1007/BF01762360
   - statut : article publié
   - notion : théorème abstrait sur espaces de Bochner, aucune notion de
     solution Navier–Stokes
   - résultat à enregistrer : corollaire 4, en distinguant la branche
     \(L^p_tX+L^1_tY\) et la branche \(L^\infty_tX+L^r_tY\), \(r>1\)
   - limite : ne fournit pas la borne de dérivée ni le passage *suitable*.

2. **Berselli–Fagioli–Spirito, 2019** — source primaire explicite pour le
   paquet discret de dérivée négative, pression et convenabilité.

   - DOI : `10.1016/j.matpur.2018.09.004`
   - arXiv : `1710.01579v2`
   - URL : https://arxiv.org/abs/1710.01579
   - statut : article publié
   - équation : Navier–Stokes incompressible 3D périodique, viscosité un,
     schéma \(\theta\)–éléments finis
   - résultats à enregistrer : proposition 4.4 et théorème 1.1
   - limite : suite discrète structurée; aucune pénalisation de profil.

3. **Jean-Pierre Aubin, 1963** — ajout historique utile, priorité inférieure
   à Simon pour l'usage opérationnel.

   - URL primaire accessible :
     https://heuklyd.github.io/papers/pdf/Aubin-1963.pdf
   - statut : note publiée, *C. R. Acad. Sci. Paris* 256, 5042–5044
   - DOI : aucun identifié
   - limite : formulation ancienne; Simon est la source de vérification la
     plus précise pour les exposants utilisés ici.

### Déjà cataloguées, à relier sans créer de doublon

- `NS-SRC-0187` Albritton–Barker 2020 : compacité locale adaptée avec
  pression ;
- `NS-SRC-0211` Babin–Mahalov–Nicolaenko 1999 : rotation de Coriolis forte ;
- `NS-SRC-0212` Gallagher–Saint-Raymond 2003 : convergence faible vers le
  noyau d'une pénalisation de Coriolis ;
- `NS-SRC-0213` Gallagher–Higaki–Maekawa 2019 : modes angulaires autour d'un
  obstacle tournant ;
- `NS-SRC-0051` Pineau–Vicol 2026 : profils backward rotatoirement
  auto-similaires exacts.

### Résultat d'absence

La recherche différentielle, arrêtée au 15 août 2026, n'a trouvé aucun article
primaire assemblant les hypothèses exactes de (2.1)–(2.2), la compacité
*suitable*, la rotation de profil \(\mathcal R\), la stationnarité et le
raccord à une limite de blow-up Clay. Cette absence est un résultat de veille,
pas une preuve bibliographique absolue d'inexistence.

## 9. Traçabilité de l'audit primaire

Les énoncés centraux ont été contrôlés dans les textes intégraux suivants :

| Fichier de travail temporaire | Taille | SHA-256 | Passage contrôlé |
|---|---:|---|---|
| `simon-1987.pdf` | 1 777 278 octets | `86B81EB6BE3BE81AFD97FD43F185F63929F552FDAAAF13EE7A9D89F6483A3DB3` | corollaire 4, page PDF rendue 21 |
| `berselli-fagioli-spirito-2019.pdf` | 248 955 octets | `5F14DAC401F687EC85FD394520DA2F59590E3C128B85DA243B19DA967D316A94` | théorème 1.1; proposition 4.4, page PDF 10 |
| `albritton-barker-2020.pdf` | 476 336 octets | `FDD91E657B5CF503286B4E45CC084C12C8B202AAF24BCDAD67EDEA46EDFA4102` | lemme A.2, page PDF 25 |

Les métadonnées arXiv vérifiées au jour de coupure sont :

- Berselli–Fagioli–Spirito : soumission v1 le 4 octobre 2017, v2 le
  13 septembre 2018, DOI publié relié ;
- Albritton–Barker : soumission v1 le 1er novembre 2018, v2 le
  18 novembre 2019 ;
- Pineau–Vicol : prépublication v2, non convertie ici en résultat publié.

Les fichiers PDF et images de rendu restent des artefacts temporaires d'audit;
ils ne sont pas ajoutés au dépôt.

## 10. Décision scientifique

**État : CONTINUER.** Le meilleur lemme actif n'est plus « diviser une dérivée
distributionnelle par une vitesse variable », mais :

> produire, pour la suite de profils issue d'une normalisation de blow-up, une
> borne uniforme de \(\partial_sZ_n\) dans un espace négatif **complet** où
> l'identité avec \(\beta_n\mathcal RZ_n\) et le résidu est vraie, tout en
> conservant pression, énergie locale et non-trivialité.

La prochaine expérience discriminante doit mesurer séparément, sur des
cylindres invariants par rotation :

1. \(\|\partial_sZ_n\|_{L^qX}\) avec tests complets et avec tests
   solénoïdaux ;
2. \(\|r_n\|_{L^qX}\) et \(\|\mathcal Ar_n\|\) ;
3. \(b_n^{-1}(\|\partial_sZ_n\|+\|r_n\|)\), qui est le résidu certifié de
   l'annulation de \(\mathcal RZ_n\) ;
4. la composante gradient/harmonique manquante entre les deux espaces duaux.

Un échec à borner la dérivée complète, accompagné d'une croissance d'ordre
\(|\beta_n|\) dans la composante non axisymétrique, réfuterait l'applicabilité
du lemme Bochner à cette normalisation sans réfuter le lemme lui-même.
