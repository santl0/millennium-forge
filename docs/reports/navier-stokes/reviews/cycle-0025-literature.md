# Cycle 0025 — veille primaire : idempotents VMO et blobs critiques

Date de coupure : **2026-08-14**.

Périmètre : fonctions caractéristiques et applications à valeurs discrètes dans
VMO, prolongements de direction de vorticité, incidence de l'analyticité
spatiale sur l'ensemble nodal, et constructions de blobs ou d'anneaux
tourbillonnaires à l'échelle critique \(L^{3/2,\infty}\) de la vorticité.

Type de revue : veille bibliographique différentielle sur sources primaires,
complétée par deux calculs élémentaires du laboratoire — le test de densité
pour \(\zeta=\xi\mathbf 1_A\) et le comptage de distribution d'une famille de
blobs solénoïdaux. Ces calculs ne reçoivent pas le statut PAPER_PROOF. La
revue est produite par la même famille de modèle que l'agent principal et ne
constitue pas une reproduction indépendante des preuves citées.

## Verdict différentiel

Le lemme qualitatif recherché est **standard** : sur un domaine connexe, une
fonction à valeurs entières dans VMO est constante presque partout. Brezis–
Nirenberg prouvent plus généralement la connexité de l'image essentielle d'une
application VMO sur un connexe ; Bourgain–Brezis–Mironescu rappellent
explicitement le cas entier et donnent l'identité d'oscillation d'une fonction
caractéristique. Puisque

\[
 \zeta=\xi\mathbf 1_A,\qquad |\xi|=1\text{ sur }A,
 \qquad |\zeta|^2=\mathbf 1_A,
\]

la composition lipschitzienne implique
\(\zeta\in VMO\Rightarrow\mathbf 1_A\in VMO\), donc \(A\) est nul ou conull
sur chaque composante connexe. Une version quantitative encore plus directe
donne, sur toute balle \(B\),

\[
 \theta_B(1-\theta_B)
 \le \fint_B|\zeta-\zeta_B|,
 \qquad \theta_B=\frac{|A\cap B|}{|B|}.
\tag{V1}
\]

Ainsi un module global d'oscillation sur les petites balles qui tend vers zéro
exclut uniformément les densités intermédiaires. La formule (V1) n'a pas été
trouvée mot pour mot pour le champ vectoriel \(\zeta\), mais sa preuve en deux
lignes et le théorème qualitatif sous-jacent sont déjà contenus dans la théorie
classique. Ce n'est donc pas un nouveau verrou analytique.

La veille corrige toutefois la portée Navier–Stokes attribuée à ce fait au
cycle 0024. À tout temps positif où une solution forte sur \(\mathbb R^3\) est
régulière, elle est spatialement analytique. Si
\(\omega(\cdot,t)\not\equiv0\), l'ensemble commun de ses zéros est de mesure
nulle. L'ensemble actif \(A(t)=\{|\omega|>0\}\) est alors conull, et toutes les
conventions mesurables prises **exactement** sur \(Z(t)\) définissent le même
élément de BMO. L'obstruction idempotente ne réfute donc ni Bradshaw–Grujić ni
Grujić v2 pendant l'intervalle classique précédant un premier temps singulier.
L'obstruction réelle est le comportement de \(\xi\) **au voisinage** des zéros :
un changement de signe transversal peut empêcher VMO même si le lieu nodal a
mesure nulle.

Enfin, les sources primaires sur les anneaux visqueux partent d'un filament
circulaire, c'est-à-dire d'une mesure de vorticité. Un anneau de rayon majeur
fixe et de cœur \(\delta\) a, par simple comptage d'échelle,
\(\|\omega\|_{L^{3/2,\infty}}\asymp\delta^{-2/3}\) à circulation fixée : il
n'est pas une famille uniformément critique \(L^{3/2,\infty}\). Des blobs
compacts solénoïdaux obtenus par la remise à l'échelle Navier–Stokes sont, eux,
uniformément critiques et fournissent un test adverse admissible à temps
initial, mais aucune source trouvée ne les fait interagir en une solution
candidate de blow-up.

## 1. Équation et échelle fixées

La comparaison Clay porte sur Navier–Stokes incompressible non forcé sur
\(\mathbb R^3\), de viscosité \(1\) :

\[
 \partial_tu-\Delta u+(u\cdot\nabla)u+\nabla p=0,
 \qquad \nabla\cdot u=0,
 \qquad \omega=\nabla\times u.
\tag{NS}
\]

La loi d'échelle est

\[
 u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),
 \qquad
 \omega_\lambda(x,t)=\lambda^2\omega(\lambda x,\lambda^2t).
\tag{1.1}
\]

Pour \(1\le p<\infty\),

\[
 \|\omega_\lambda(\cdot,0)\|_{L^{p,\infty}}
 =\lambda^{2-3/p}\|\omega(\cdot,0)\|_{L^{p,\infty}}.
\tag{1.2}
\]

Le seuil vorticité faible est donc \(p=3/2\). La direction
\(\xi=\omega/|\omega|\) est sans dimension et la seminorme BMO est invariante
par la dilatation. Le module VMO demande en plus que les oscillations moyennes
sur les balles tendent uniformément vers zéro avec le rayon.

## 2. Sources primaires, versions et statuts

| Source primaire | Statut au 2026-08-14 | Fait exact utilisé ici |
|---|---|---|
| Haïm Brezis et Louis Nirenberg, [*Degree theory and BMO. Part I: Compact manifolds without boundaries*](https://doi.org/10.1007/BF01671566), *Selecta Math.* **1** (1995), 197–263 | publié, DOI 10.1007/BF01671566 | §I.5 : l'image essentielle d'une application VMO restreinte à un ensemble connexe est connexe ; lemme A.7 : la composition uniformément continue préserve VMO |
| Jean Bourgain, Haïm Brezis et Petru Mironescu, [*A new function space and applications*](https://ems.press/journals/jems/articles/12580), *J. Eur. Math. Soc.* **17** (2015), 2083–2101 | publié, [DOI 10.4171/JEMS/551](https://doi.org/10.4171/JEMS/551) | introduction : une fonction mesurable entière dans VMO sur un domaine connexe est constante ; formules (0.2)–(0.4) pour l'oscillation pairwise et \(\mathbf1_A\) |
| Peter W. Jones, [*Extension Theorems for BMO*](https://iumj.org/article/2860/), *Indiana Univ. Math. J.* **29** (1980), 41–66 | publié, [DOI 10.1512/iumj.1980.29.29005](https://doi.org/10.1512/iumj.1980.29.29005) | extension linéaire BMO depuis un domaine uniforme ; aucune préservation de la sphère ni extension depuis un ensemble actif arbitraire |
| Zoran Grujić et Igor Kukavica, [*Space Analyticity for the Navier–Stokes and Related Equations with Initial Data in \(L^p\)*](https://doi.org/10.1006/jfan.1997.3167), *J. Funct. Anal.* **152** (1998), 447–466 | publié, DOI 10.1006/jfan.1997.3167 | analyticité spatiale sur \(\mathbb R^3\) pour les solutions régulières dans leur cadre \(L^p\) |
| Ira Herbst et Erik Skibsted, [*Analyticity estimates for the Navier–Stokes equations*](https://arxiv.org/abs/0907.4351), arXiv:0907.4351v1 du 24 juillet 2009 | prépublication v1, aucune référence de revue sur arXiv | pour toute solution forte sur \((0,T]\) dans les classes de Sobolev considérées, rayon d'analyticité strictement positif à tout \(t>0\) |
| Zachary Bradshaw et Zoran Grujić, [*A spatially localized \(L\log L\) estimate on the vorticity in the 3D NSE*](https://arxiv.org/abs/1309.2519), v5 du 7 février 2014 | publié, *Indiana Univ. Math. J.* **64** (2015), 433–440, [DOI 10.1512/iumj.2015.64.5496](https://doi.org/10.1512/iumj.2015.64.5496) | solution de Leray sur \(\mathbb R^3\), hypothèse uniforme sur \(\psi\xi\) en log-BMO, conclusion locale \(L\log L\) |
| Zoran Grujić, [*Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier–Stokes Equations*](https://arxiv.org/abs/2607.08866), v2 du 13 juillet 2026 | prépublication v2, aucune référence de revue sur arXiv | exclusion conditionnelle revendiquée d'une concentration ponctuelle critique \(L^{3/2,\infty}\) sous contrôle log-BMO de la direction |
| Zhen Lei, Xiao Ren et Gang Tian, [*A Geometric Characterization of Potential Navier-Stokes Singularities*](https://arxiv.org/abs/2501.08976), v1 du 15 janvier 2025 | prépublication v1, aucune référence de revue sur arXiv | solution faible adaptée locale ; le double cône n'est évalué qu'à forte vorticité et le critère pairwise seulement lorsque les deux vorticités sont non nulles |
| Evan Miller, [*A locally anisotropic regularity criterion for the Navier–Stokes equation in terms of vorticity*](https://arxiv.org/abs/2002.02152), v1 du 6 février 2020 | publié, *Proc. Amer. Math. Soc. Ser. B* **8** (2021), 60–74, [DOI 10.1090/bproc/74](https://doi.org/10.1090/bproc/74) | solution mild \(H^1(\mathbb R^3)\), champ unitaire auxiliaire global \(v\), \(\nabla v\) borné et critère critique sur \(v\times\omega\) |
| Hao Feng et Vladimír Šverák, [*On the Cauchy problem for axi-symmetric vortex rings*](https://arxiv.org/abs/1301.6317), v1 du 27 janvier 2013 | publié, *Arch. Ration. Mech. Anal.* **215** (2015), 89–123, [DOI 10.1007/s00205-014-0775-4](https://doi.org/10.1007/s00205-014-0775-4) | existence axisymétrique sans restriction de taille pour une vorticité initiale mesure concentrée sur un cercle ou une combinaison finie de cercles coaxiaux |
| Thierry Gallay et Vladimír Šverák, [*Uniqueness of axisymmetric viscous flows originating from circular vortex filaments*](https://www.numdam.org/articles/10.24033/asens.2402/), arXiv:1609.02030v1 | publié, *Ann. Sci. ENS* **52** (2019), 1025–1071, [DOI 10.24033/asens.2402](https://doi.org/10.24033/asens.2402) | unicité de la solution axisymétrique sans swirl issue d'un filament circulaire, circulation arbitraire |
| Thierry Gallay et Vladimír Šverák, [*Vanishing viscosity limit for axisymmetric vortex rings*](https://arxiv.org/abs/2301.01092), v3 du 3 juin 2024 | publié, *Invent. Math.* **237** (2024), 275–348, [DOI 10.1007/s00222-024-01261-5](https://doi.org/10.1007/s00222-024-01261-5) | filament circulaire initial, viscosité \(\nu>0\), anneau lisse de largeur \(\sqrt{\nu t}\) à temps positif et approximation asymptotique contrôlée |

Aucune version postérieure à Grujić v2 ou Lei–Ren–Tian v1 n'apparaît dans
leurs historiques arXiv à la date de coupure. La recherche primaire n'a trouvé
ni article publié ni prépublication fournissant une famille dynamique de
blobs solénoïdaux multi-échelles uniformément bornée dans
\(L^{3/2,\infty}\) et reliée à un blow-up admissible de (NS).

## 3. Le théorème idempotent est standard

Soit \(\Omega\subset\mathbb R^n\) connexe et \(A\subset\Omega\) mesurable.
Le résultat cité explicitement par Bourgain–Brezis–Mironescu est

\[
 f:\Omega\to\mathbb Z,\quad f\in VMO(\Omega)
 \quad\Longrightarrow\quad f\text{ est constante p.p.}
\tag{3.1}
\]

Pour \(\zeta=\xi\mathbf1_A\), \(|\xi|=1\) sur \(A\), choisir une fonction
globalement lipschitzienne \(F:\mathbb R^3\to\mathbb R\) qui coïncide avec
\(|z|^2\) sur la boule unité, par exemple
\(F(z)=\min(|z|^2,1)\). Le lemme de composition VMO donne

\[
 \zeta\in VMO(\Omega;\mathbb R^3)
 \quad\Longrightarrow\quad
 F\circ\zeta=\mathbf1_A\in VMO(\Omega).
\tag{3.2}
\]

Puis (3.1) implique

\[
 |A|=0\quad\text{ou}\quad|\Omega\setminus A|=0.
\tag{3.3}
\]

Sur \(\mathbb R^3\), il suffit d'appliquer (3.3) à des boules connexes et de
propager la constante par recouvrement. Une hypothèse VMO locale sur chaque
compact suffit qualitativement ; un module global uniforme est plus fort que
nécessaire.

Brezis–Nirenberg donnent une formulation géométrique équivalente : l'image
essentielle d'une application VMO sur un connexe est connexe. L'image
essentielle de \(\mathbf1_A\) ne peut donc pas contenir simultanément \(0\) et
\(1\). Cette source établit aussi que la composition uniformément continue
préserve VMO. Le maillon (3.2)–(3.3) est ainsi une conséquence directe de
résultats publiés, et non une conjecture du laboratoire.

## 4. Version quantitative : exclusion des densités intermédiaires

Pour une balle \(B\), posons

\[
 M_B(\zeta)=\fint_B|\zeta-\zeta_B|,
 \qquad
 M_B^*(\zeta)=\fint_B\fint_B|\zeta(y)-\zeta(z)|\,dy\,dz.
\]

Jensen et l'inégalité triangulaire donnent les constantes exactes usuelles

\[
 M_B(\zeta)\le M_B^*(\zeta)\le2M_B(\zeta).
\tag{4.1}
\]

Si l'un des deux points appartient à \(A\) et l'autre à son complément,
\(|\zeta(y)-\zeta(z)|=1\). Les deux ordres de ces paires ont une mesure
normalisée \(2\theta_B(1-\theta_B)\). Par conséquent,

\[
 2\theta_B(1-\theta_B)
 \le M_B^*(\zeta)
 \le2M_B(\zeta),
\]

ce qui prouve (V1).

Définissons le module global des petites balles

\[
 \beta(r)=\sup_{x\in\mathbb R^3}\sup_{0<\rho\le r}
 \fint_{B_\rho(x)}|\zeta-\zeta_{B_\rho(x)}|.
\tag{4.2}
\]

Pour tout \(\delta\in(0,1/2)\), si
\(\beta(r)<\delta(1-\delta)\), aucune balle de rayon au plus \(r\) ne peut
satisfaire

\[
 \delta\le\frac{|A\cap B|}{|B|}\le1-\delta.
\tag{4.3}
\]

La condition \(\beta(r)\to0\) exclut donc uniformément les frontières
**mesure-théoriques** à densité intermédiaire. Bourgain–Brezis–Mironescu
calculent directement, pour \(f=\mathbf1_A\),

\[
 M_B(f)=M_B^*(f)=2\theta_B(1-\theta_B),
\tag{4.4}
\]

ce qui est la version scalaire exacte du même mécanisme.

Limites indispensables :

1. toutes les fonctions caractéristiques bornées appartiennent à BMO ; une
   borne BMO fixe sans disparition aux petites échelles ne donne pas (3.3) ;
2. une frontière topologique de mesure nulle peut subsister : par exemple
   \(A=\mathbb R^3\setminus\{x_1=0\}\) est conull et
   \(\mathbf1_A=1\) presque partout ;
3. une hypothèse seulement sur les balles centrées dans un superniveau, ou
   une moyenne relative à \(A\cap B\), ne contrôle pas les paires croisées ;
4. pour un prolongement global unitaire \(\Xi\), on a
   \(|\Xi|^2=1\) partout presque partout : l'argument idempotent ne voit plus
   l'ensemble actif ;
5. l'argument détecte l'occupation actif/inactif mais pas les sauts de phase
   entre deux directions unitaires.

## 5. Analyticité : la correction décisive pour Navier–Stokes

Herbst–Skibsted travaillent avec Navier–Stokes sur \(\mathbb R^3\), projection
de Leray et données de Sobolev \(H^r\), \(r\ge1/2\). Leur texte établit que
toute solution forte de leur classe possède un rayon d'analyticité spatial
strictement positif à tout \(t>0\), y compris pour une solution définie
seulement sur \((0,T]\). Le résultat publié de Grujić–Kukavica donne également
l'analyticité spatiale dans un cadre \(L^p\) sur \(\mathbb R^3\).

À un temps régulier \(t>0\), \(\omega(\cdot,t)\) est donc analytique réelle.
Si un de ses trois composants n'est pas identiquement nul, son ensemble de
zéros a mesure de Lebesgue nulle ; l'ensemble commun

\[
 Z(t)=\{x:\omega(x,t)=0\}
\]

est un sous-ensemble de ce lieu nul. Ainsi

\[
 \omega(\cdot,t)\not\equiv0
 \quad\Longrightarrow\quad |Z(t)|=0,
 \quad A(t)\text{ conull}.
\tag{5.1}
\]

La conclusion (5.1) est une déduction du laboratoire combinant l'analyticité
citée et le fait classique sur les zéros d'une fonction analytique réelle ;
elle n'est pas présentée comme un théorème formulé ainsi dans les articles.
Si \(\omega(\cdot,t)\equiv0\), alors \(u(\cdot,t)\in L^2\), sans divergence et
sans rotationnel, est nul à ce temps. Il est donc prudent de formuler (5.1)
conditionnellement à la non-trivialité au temps considéré, sans invoquer ici
un théorème de rétro-unicité.

Ce fait distingue deux questions auparavant confondues :

- modifier \(\xi\) exactement sur \(Z(t)\) ne change aucune classe BMO, car
  BMO identifie les fonctions égales presque partout ;
- le comportement de \(\xi\) lorsque \(x\to Z(t)\) peut rester singulier. Le
  modèle local analytique \(\omega(x)=(0,x_1,0)\), qui est sans divergence,
  donne \(\xi=(0,\operatorname{sgn}x_1,0)\) hors du plan nodal : le plan a
  mesure nulle, mais l'oscillation de la direction ne disparaît pas sur les
  balles qui le traversent.

Le lemme idempotent ferme donc une ambiguïté de définition, mais il ne produit
aucune régularité géométrique nouvelle de la direction.

## 6. Comparaison Grujić v2 / Bradshaw–Grujić / Jones / LRT / Miller

### Bradshaw–Grujić

Le théorème publié suppose une borne uniforme de
\(\psi\xi\) dans un espace local log-BMO et conclut une borne locale
\(L\log L\) de la vorticité. Avant le premier temps potentiellement singulier,
la solution considérée est régulière ; à tout temps positif non trivial,
(5.1) rend la valeur de \(\xi\) sur \(Z(t)\) sans effet sur la norme. Le facteur
\(\psi\) est une coupure lisse, pas la caractéristique de l'ensemble actif.
Le test idempotent ne réfute donc pas l'hypothèse du théorème.

Ce qui reste conditionnel est substantiel : ni l'énergie de Leray–Hopf ni la
divergence nulle ne fournissent la borne log-BMO de \(\psi\xi\), et la
conclusion \(L\log L\) n'est pas à elle seule un critère de régularité Clay.

### Grujić v2

La v2, déposée le 9 juillet 2026 et révisée le 13 juillet, traite un scénario
de concentration ponctuelle critique \(L^{3/2,\infty}\) et appelle \(\xi\) un
champ unitaire global appartenant à
\(\mathrm{bmo}_{1/|\log r|}\). Sur l'intervalle classique positif précédant
le temps \(T^*\), (5.1) permet effectivement de choisir n'importe quelles
valeurs unitaires sur le lieu nodal sans modifier l'élément BMO. L'objection
« aucun prolongement depuis un ensemble actif de mesure intermédiaire » du
cycle 0024 ne s'applique donc pas dans ce régime.

Cela ne valide pas la prépublication. Restent à auditer indépendamment ses
hypothèses exactes de concentration, les constantes uniformes en temps, le
passage du gain Lorentz–Zygmund à la parcimonie géométrique et la fermeture au
temps \(T^*\). Le lemme idempotent ne touche aucun de ces maillons.

### Jones

Jones prolonge composante par composante une fonction BMO définie sur un
domaine uniforme. Il ne traite ni un ensemble actif mesurable arbitraire, ni
une contrainte \(\mathbb S^2\), ni un module logarithmique prescrit. Ce résultat
reste impropre à construire un champ unitaire depuis une direction donnée
seulement sur un superniveau irrégulier.

En revanche, pour une solution forte à temps positif, aucun prolongement à
travers \(Z(t)\) n'est nécessaire au sens des classes a.e. : le vrai problème
est de montrer que la direction elle-même possède la régularité BMO requise au
voisinage du lieu nodal. Jones ne la crée pas.

### Lei–Ren–Tian (LRT)

LRT travaille avec une solution faible adaptée locale dans \(Q(1)\), classe
pour laquelle l'analyticité globale précédente n'est pas disponible. Le
théorème 1.1 n'évalue la direction que là où \(|\omega|>M\), et le corollaire
pairwise seulement aux couples de points où les deux vorticités sont non
nulles. Les zéros sont donc évités par les quantificateurs mêmes du critère.

Ni (V1) ni la connexité de l'image essentielle ne donnent le double cône
ponctuel requis : VMO est un contrôle moyen, tandis que LRT impose la
géométrie à tous les points pertinents. Le petit ensemble exceptionnel peut
encore porter la forte vorticité.

### Miller

Miller introduit un champ unitaire auxiliaire global \(v\), pas nécessairement
la direction canonique, avec \(\nabla_xv\in L^\infty\) localement en temps et
\(v\times\omega\in L^4_tL^2_x\). Le produit transversal s'annule
automatiquement aux zéros. Pour une solution mild forte à temps positif,
changer \(v\) sur le lieu nodal nul ne modifie pas sa classe de Sobolev ; mais
prendre \(v=\xi\) exige encore de contrôler ses variations en approchant ce
lieu. VMO ou log-BMO n'implique pas \(\nabla v\in L^\infty\).

Le bilan comparatif exact est

\[
 \boxed{\text{analyticité + non-trivialité}}
 \Longrightarrow
 \boxed{|Z(t)|=0\text{ et convention a.e. inoffensive}}
 \not\Longrightarrow
 \boxed{\xi\in VMO,\ \text{double cône LRT, ou }\nabla\xi\in L^\infty}.
\tag{6.1}
\]

## 7. Anneaux visqueux et échelle faible \(L^{3/2}\)

Les trois sources Feng–Šverák et Gallay–Šverák portent sur Navier–Stokes
incompressible axisymétrique sans swirl sur \(\mathbb R^3\), avec vorticité
initiale concentrée sur un cercle. Cette donnée est une mesure, non une
fonction de \(L^{3/2,\infty}\), et son champ de vitesse n'est pas une donnée
initiale Clay lisse de Schwartz.

À temps positif, l'anneau a un cœur de largeur
\(\delta\simeq\sqrt{\nu t}\). Pour circulation fixée \(\Gamma\) et rayon majeur
fixe \(R\), la géométrie de tube donne

\[
 |\omega|\asymp\Gamma\delta^{-2},
 \qquad
 |\operatorname{supp}\omega|\asymp R\delta^2.
\tag{7.1}
\]

Le quasi-norme de Lorentz vérifie alors, au niveau d'amplitude principal,

\[
 \|\omega\|_{L^{p,\infty}}
 \asymp
 \Gamma\delta^{-2}(R\delta^2)^{1/p}.
\tag{7.2}
\]

Pour \(p=3/2\),

\[
 \|\omega\|_{L^{3/2,\infty}}
 \asymp \Gamma R^{2/3}\delta^{-2/3}
 \asymp \Gamma R^{2/3}(\nu t)^{-1/3}.
\tag{7.3}
\]

Les relations (7.1)–(7.3) sont un calcul d'échelle du laboratoire à partir de
la géométrie établie dans les sources ; elles ne sont pas citées comme un
théorème de ces articles. Elles montrent qu'un filament de rayon majeur fixe
est naturellement critique comme mesure/L¹ transverse, pas comme
concentration ponctuelle uniforme \(L^{3/2,\infty}\).

Si l'on réduit simultanément le rayon majeur et le cœur comme
\(R\asymp\delta\asymp r\), le volume devient \(r^3\), l'amplitude \(r^{-2}\),
et la norme faible \(L^{3/2}\) devient invariante. Mais il s'agit alors de la
remise à l'échelle ponctuelle d'un anneau entier, non du régime de filament
circulaire fixe étudié par les trois articles. Aucun résultat primaire trouvé
ne contrôle une superposition dynamique de tels anneaux rétrécissants.

## 8. Contretest reproductible : blobs solénoïdaux critiques

Ce contretest est analytique et cinématique ; il ne simule pas (NS).
Choisir un champ non nul

\[
 U\in C_c^\infty(\mathbb R^3;\mathbb R^3),
 \qquad \nabla\cdot U=0,
 \qquad \Omega=\nabla\times U.
\]

Pour \(\lambda\ge1\) et un centre \(x_0\), poser

\[
 U_{\lambda,x_0}(x)=\lambda U(\lambda(x-x_0)),
 \qquad
 \Omega_{\lambda,x_0}(x)=\lambda^2
 \Omega(\lambda(x-x_0)).
\tag{8.1}
\]

Alors \(U_{\lambda,x_0}\) est lisse, compact, sans divergence,
\(\nabla\times U_{\lambda,x_0}=\Omega_{\lambda,x_0}\), et

\[
 \|\Omega_{\lambda,x_0}\|_{L^{3/2,\infty}}
 =\|\Omega\|_{L^{3/2,\infty}},
 \qquad
 \|U_{\lambda,x_0}\|_2^2=\lambda^{-1}\|U\|_2^2.
\tag{8.2}
\]

Prendre \(\lambda_j=2^j\) et des centres tels que les supports soient
disjoints, puis

\[
 U^{(N)}=\sum_{j=1}^NU_{\lambda_j,x_j},
 \qquad
 \Omega^{(N)}=\sum_{j=1}^N\Omega_{\lambda_j,x_j}.
\tag{8.3}
\]

Si \(M=\|\Omega\|_\infty\) et \(V=|\operatorname{supp}\Omega|\), alors

\[
 \begin{aligned}
 |\{|\Omega^{(N)}|>\alpha\}|
 &\le V\sum_{j:\,M\lambda_j^2>\alpha}\lambda_j^{-3} \\
 &\le C_{M,V}\alpha^{-3/2},
 \end{aligned}
\tag{8.4}
\]

avec une constante indépendante de \(N\). De plus,

\[
 \|U^{(N)}\|_2^2
 =\|U\|_2^2\sum_{j=1}^N2^{-j}
 \le\|U\|_2^2.
\tag{8.5}
\]

Chaque \(U^{(N)}\) est donc une donnée initiale lisse, compacte et admissible
pour le cas \(\mathbb R^3\) du problème Clay, avec énergie et vorticité faible
critique uniformément bornées en \(N\). Elle falsifie toute implication
cinématique du type

\[
 \nabla\cdot\omega=0,\quad
 \|\omega\|_{L^{3/2,\infty}}+\|u\|_2\le C
 \quad\Longrightarrow\quad
 \frac{\omega}{|\omega|}\mathbf1_{\{|\omega|>0\}}\in VMO.
\tag{8.6}
\]

En effet, à temps initial, l'ensemble actif de cette vorticité compacte a
mesure positive et son complément aussi ; le théorème idempotent interdit le
VMO du prolongement nul. Cela reste vrai pour un seul blob non trivial.

Limites du contretest :

- il ne construit qu'une donnée, pas une solution ancienne, un profil limite
  ni un blow-up ;
- les supports sont choisis disjoints, donc aucune interaction de pression ou
  d'étirement n'est estimée ;
- pour chaque \(N\), la diffusion rend la solution analytique à temps positif
  tant qu'elle est forte, et l'obstruction par support compact disparaît alors
  au sens a.e. ;
- l'uniformité de (8.4) n'est pas une compacité forte et ne contrôle ni les
  translations, ni les phases, ni le stretching multi-échelle.

## 9. Implication exacte pour le programme Clay

Les maillons désormais établis sont

\[
 \boxed{\zeta=\xi\mathbf1_A\in VMO}
 \Longrightarrow
 \boxed{A\text{ nul ou conull sur un connexe}},
\tag{9.1}
\]

et, pour une solution forte non triviale à temps positif,

\[
 \boxed{\text{analyticité spatiale de }\omega}
 \Longrightarrow
 \boxed{A(t)\text{ conull}}.
\tag{9.2}
\]

Ils ne donnent ni une borne VMO de la direction, ni une déplétion de
l'étirement, ni un critère de prolongement. À temps initial, (8.3) montre que
les seules bornes critiques et l'incompressibilité n'imposent pas (9.1). À
temps positif, le support essentiel devient trivial mais les défauts de phase
près du lieu nodal restent entièrement ouverts.

La veille sur les anneaux donne également un résultat négatif précis : les
solutions issues d'un filament circulaire fixe ne sont pas le laboratoire
uniformément critique \(L^{3/2,\infty}\) recherché. Pour obtenir cette échelle,
il faut contracter le diamètre entier du blob ou de l'anneau, puis contrôler
les interactions non locales entre échelles — exactement le maillon absent.

## 10. Décision scientifique

- **Résultat bibliographique positif :** la rigidité des idempotents VMO est
  standard et sourcée par Brezis–Nirenberg et Bourgain–Brezis–Mironescu ; la
  constante quantitative (V1) est explicite.
- **Rectification :** l'objection de prolongement aux zéros du cycle 0024 ne
  s'applique pas aux temps positifs réguliers non triviaux sur \(\mathbb R^3\),
  car le lieu nodal analytique est nul. Elle reste pertinente pour une solution
  faible non analytique, une donnée initiale compacte, ou un superniveau de
  mesure intermédiaire.
- **Résultat négatif sur les anneaux :** les filaments circulaires publiés
  sont des données mesures et leur lissage à rayon majeur fixe n'est pas
  uniformément borné dans \(L^{3/2,\infty}\) lorsque le cœur tend vers zéro.
- **Test adverse :** la famille (8.3) est solénoïdale, Clay-admissible à temps
  initial, uniformément énergétique et uniformément critique faible ; son
  prolongement nul de direction n'est pas VMO.
- **Écart Clay :** aucune dynamique de blow-up, aucune borne uniforme du
  stretching et aucune compacité forte multi-échelle ne découlent de ce
  contretest.
- **Statut :** **CONTINUER**, en abandonnant le verrou « choix ponctuel de la
  direction sur \(Z(t)\) » pour les solutions fortes positives.
- **Prochaine expérience décisive :** placer deux ou trois blobs de (8.1) à
  échelles et séparations variables, calculer exactement le terme croisé
  \(\int (\omega\cdot\nabla)u\cdot\omega\) avec projection de Leray, puis
  chercher soit une borne uniforme critique, soit une séquence signée qui la
  viole. Le calcul doit suivre la contribution de pression/non-localité et la
  dépendance aux rapports d'échelle ; le seul comptage Lorentz (8.4) ne suffit
  pas.
