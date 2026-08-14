# Cycle 0031 — tore axisymétrique compact à courbure annulée

Date : 2026-08-14.

Type de passe : dérivation constructive, contre-modèle reproductible et
obstruction quantitative. Cette passe est une dérivation IA interne, et non
une revue externe indépendante.

## Verdict

Le facteur \(R/r\) annule exactement le terme de courbure du curl, mais un
grand aspect ne permet pas de franchir simultanément les portes
faible-\(L^3\), faible-\(L^{3/2}\) et log-BMO.

Considérons

\[
 U(r,\theta,z)
 =\psi(r,z)e_\theta,
 \qquad
 \psi(r,z)
 =V\frac Rr
 \eta\!\left(\frac{r-R}{a}\right)
 \chi\!\left(\frac zb\right),
 \tag{1}
\]

avec \(0<a<R/2\). Les profils fixes \(\eta,\chi\) sont compacts, possèdent
un plateau non nul et des zones de transition non dégénérées. Alors

\[
 \boxed{
 \nabla\times U
 =
 -\frac{VR}{rb}\eta\chi'e_r
 +\frac{VR}{ra}\eta'\chi e_z.
 }
 \tag{2}
\]

Il n'existe aucun terme résiduel \(V\eta\chi/r\) dans la composante
verticale : il est exactement compensé par la dérivée de \(R/r\).

Avec la convention

\[
 \|f\|_{L^{p,\infty}}
 =\sup_{\lambda>0}
 \lambda|\{|f|>\lambda\}|^{1/p},
 \tag{3}
\]

les trois budgets ont les ordres exacts

\[
 \|U\|_{L^{3,\infty}}
 \asymp V(Rab)^{1/3},
 \tag{4}
\]

\[
 \|(\nabla\times U)_z\|_{L^{3/2,\infty}}
 \asymp
 \frac Va(Rab)^{2/3},
 \qquad
 \|(\nabla\times U)_r\|_{L^{3/2,\infty}}
 \asymp
 \frac Vb(Rab)^{2/3}.
 \tag{5}
\]

Les constantes ne dépendent pas de \(R,a,b,V\). Par conséquent, si

\[
 K=\|\nabla\times U\|_{L^{3/2,\infty}},
 \tag{6}
\]

alors

\[
 \boxed{
 \|U\|_{L^{3,\infty}}
 \leq CK
 \min\left\{
 \left(\frac{a^2}{Rb}\right)^{1/3},
 \left(\frac{b^2}{Ra}\right)^{1/3}
 \right\}.
 }
 \tag{7}
\]

Pour l'aspect \(A=b/a\), les deux facteurs sont

\[
 \left(\frac{a}{RA}\right)^{1/3},
 \qquad
 \left(\frac{aA^2}{R}\right)^{1/3}.
 \tag{8}
\]

Le minimum est maximal à \(A=1\). Un aspect \(A\to\infty\) rend le premier
budget plus contraignant; \(A\to0\) rend le second plus contraignant.

La calotte axiale contient en outre une région où
\(\eta'=0\), \(\eta\ne0\), \(\chi'\ne0\), donc

\[
 \frac{\nabla\times U}{|\nabla\times U|}
 =\pm e_r.
 \tag{9}
\]

Une boule tridimensionnelle de rayon
\(\rho\asymp\min(a,b)\), contenue dans cette calotte, impose

\[
 \operatorname{MO}_B
 \left(\frac{\nabla\times U}{|\nabla\times U|}\right)
 \geq c\min\left\{1,\frac aR,\frac bR\right\}.
 \tag{10}
\]

Cette oscillation est intrinsèque au support de la vorticité; aucune
extension dans l'ensemble où le curl s'annule ne peut la modifier.

Posons

\[
 m=\min\{1,a/R,b/R\},
 \qquad
 S=1+|\log(c\min(a,b))|.
 \tag{11}
\]

Une borne log-BMO uniforme par \(M\) entraîne \(m\leq CM/S\). D'autre part,
(7) implique

\[
 \|U\|_{L^{3,\infty}}\leq CKm^{1/3}.
 \tag{12}
\]

Ainsi

\[
 \boxed{
 \|U\|_{L^{3,\infty}}
 \leq CK\left(\frac{CM}{S}\right)^{1/3}.
 }
 \tag{13}
\]

Pour toute famille concentrée, \(S\to\infty\), le membre droit tend vers
zéro. Le résultat est un no-go quantifié pour l'ansatz produit (1), même
après concession de corridors directionnels logarithmiques optimaux.

## 1. Cadre exact

### 1.1 Profils et géométrie

On suppose

\[
 \eta,\chi\in C_c^\infty((-1,1)),
 \qquad
 0\leq\eta,\chi\leq1.
 \tag{14}
\]

Chaque profil vaut un sur un intervalle central de longueur fixée. Sur deux
intervalles de transition de longueur fixée, sa dérivée a un signe fixé,
une variation totale minorée et un module minoré sur un sous-intervalle.
Ces hypothèses sont uniformes et peuvent être remplacées par des bornes de
variation totale.

Le support est contenu dans

\[
 R-a<r<R+a,\qquad |z|<b.
 \tag{15}
\]

Sa boîte torique a exactement le volume

\[
 \begin{aligned}
 |\mathcal T_{R,a,b}|
 &=2\pi\int_{R-a}^{R+a}r\,dr\int_{-b}^b dz\\
 &=8\pi Rab.
 \end{aligned}
 \tag{16}
\]

Ses dimensions sont :

- rayon majeur \(R\);
- épaisseur radiale \(2a\);
- hauteur axiale \(2b\);
- aire méridienne \(4ab\);
- aspect transverse \(A=b/a\).

Puisque \(R-a>0\), le champ est identiquement nul près de l'axe. Il est
donc lisse en coordonnées cartésiennes malgré l'écriture avec \(e_\theta\).
Il est compact et

\[
 \nabla\cdot U=\frac1r\partial_\theta\psi=0.
 \tag{17}
\]

### 1.2 Loi d'échelle

Sous la remise à l'échelle Navier--Stokes

\[
 (R,a,b)\mapsto(\ell R,\ell a,\ell b),
 \qquad
 V\mapsto\ell^{-1}V,
 \tag{18}
\]

les deux normes critiques

\[
 \|U\|_{L^{3,\infty}},
 \qquad
 \|\nabla\times U\|_{L^{3/2,\infty}}
 \tag{19}
\]

sont invariantes. L'énergie cinétique est multipliée par \(\ell\), et tous
les temps diffusifs sont multipliés par \(\ell^2\).

Un rescaling anisotrope de \(a\) ou \(b\) ne préserve pas le Laplacien
isotrope de l'équation Clay.

## 2. Curl exact et annulation de courbure

Pour un champ azimutal indépendant de \(\theta\),

\[
 \nabla\times(\psi e_\theta)
 =-\partial_z\psi\,e_r
 +\frac1r\partial_r(r\psi)\,e_z.
 \tag{20}
\]

Écrivons

\[
 s=\frac{r-R}{a},
 \qquad
 t=\frac zb.
 \tag{21}
\]

La composante radiale est

\[
 W_r=-\partial_z\psi
 =-\frac{VR}{rb}\eta(s)\chi'(t).
 \tag{22}
\]

Pour la composante verticale, la bonne opération est de dériver
\(r\psi\), et non \(\psi\) seule :

\[
 r\psi=VR\eta(s)\chi(t),
 \tag{23}
\]

d'où

\[
 W_z=\frac1r\partial_r(r\psi)
 =\frac{VR}{ra}\eta'(s)\chi(t).
 \tag{24}
\]

En développant séparément,

\[
 \partial_r\psi
 =-\frac{VR}{r^2}\eta\chi
 +\frac{VR}{ra}\eta'\chi,
 \qquad
 \frac\psi r=\frac{VR}{r^2}\eta\chi.
 \tag{25}
\]

Les deux premiers termes de (25) s'annulent exactement. Le résidu de
courbure est donc nul, pas seulement \(O(a/R)\).

La divergence du curl se recalcule sans invoquer une identité formelle :

\[
 \begin{aligned}
 \nabla\cdot W
 &=\frac1r\partial_r(rW_r)+\partial_zW_z\\
 &=-\frac{VR}{rab}\eta'\chi'
 +\frac{VR}{rab}\eta'\chi'=0.
 \end{aligned}
 \tag{26}
\]

## 3. Distributions exactes et normes faibles

### 3.1 Formules de distribution

Dans les variables \((s,\theta,t)\),

\[
 dx=ab(R+as)\,ds\,d\theta\,dt.
 \tag{27}
\]

La fonction de distribution exacte de \(U\) est

\[
 \begin{aligned}
 \mu_U(\lambda)
 =2\pi ab\int_{-1}^1\int_{-1}^1
 &(R+as)\\
 {}\times&
 \mathbf1_{\left\{
 \frac{VR}{R+as}|\eta(s)\chi(t)|>\lambda
 \right\}}
 \,ds\,dt.
 \end{aligned}
 \tag{28}
\]

Pour le curl, posons

\[
 \mathcal W(s,t)^2
 =
 \left[
 \frac{VR}{(R+as)b}\eta(s)\chi'(t)
 \right]^2
 +
 \left[
 \frac{VR}{(R+as)a}\eta'(s)\chi(t)
 \right]^2.
 \tag{29}
\]

Alors

\[
 \mu_W(\lambda)
 =2\pi ab\int_{-1}^1\int_{-1}^1
 (R+as)
 \mathbf1_{\{\mathcal W(s,t)>\lambda\}}
 \,ds\,dt.
 \tag{30}
\]

Les quasi-normes faibles sont exactement

\[
 \|U\|_{L^{3,\infty}}
 =\sup_{\lambda>0}\lambda\mu_U(\lambda)^{1/3},
 \quad
 \|W\|_{L^{3/2,\infty}}
 =\sup_{\lambda>0}\lambda\mu_W(\lambda)^{2/3}.
 \tag{31}
\]

Les formules (28)--(31) conservent le facteur cylindrique \(R+as\); aucun
volume cartésien \(abR\) n'est substitué avant l'estimation.

### 3.2 Budget de la vitesse

Sur un rectangle de plateau de mesure bidimensionnelle fixe en
\((s,t)\), on a \(\eta=\chi=1\). Comme

\[
 \frac23\leq\frac Rr\leq2
 \quad\text{pour }a<R/2,
 \tag{32}
\]

un ensemble de volume au moins \(cRab\) porte \(|U|\geq cV\). Sur tout le
support, \(|U|\leq2V\). Par conséquent

\[
 c_\eta c_\chi V(Rab)^{1/3}
 \leq
 \|U\|_{L^{3,\infty}}
 \leq
 2(8\pi)^{1/3}V(Rab)^{1/3}.
 \tag{33}
\]

### 3.3 Deux budgets indépendants du curl

La composante verticale est d'ordre \(V/a\) sur un produit :

- transition radiale de taille \(a\);
- plateau axial de taille \(b\);
- longueur azimutale d'ordre \(R\).

La composante radiale est d'ordre \(V/b\) sur le produit symétrique. Il
vient

\[
 c_z\frac Va(Rab)^{2/3}
 \leq
 \|W_z\|_{L^{3/2,\infty}}
 \leq
 C_z\frac Va(Rab)^{2/3},
 \tag{34}
\]

\[
 c_r\frac Vb(Rab)^{2/3}
 \leq
 \|W_r\|_{L^{3/2,\infty}}
 \leq
 C_r\frac Vb(Rab)^{2/3}.
 \tag{35}
\]

Les minorations ne nécessitent pas que les dérivées soient constantes.
Pour \(p=3/2\),

\[
 \int_E|f|
 \leq3\|f\|_{L^{3/2,\infty}}|E|^{1/3}.
 \tag{36}
\]

La variation totale radiale de \(\eta\), testée sur le plateau de \(\chi\),
donne une masse \(L^1\) au moins \(cVRb\) dans un volume \(CRab\).
L'inégalité (36) redonne la minoration de (34). La variation totale d'une
calotte de \(\chi\), testée sur le plateau de \(\eta\), donne une masse au
moins \(cVRa\) dans le même ordre de volume et redonne (35).

Pour le champ vectoriel,

\[
 \|W\|_{L^{3/2,\infty}}
 \geq
 \max\{
 \|W_r\|_{L^{3/2,\infty}},
 \|W_z\|_{L^{3/2,\infty}}
 \}.
 \tag{37}
\]

La combinaison de (33)--(37) prouve (7).

### 3.4 Audit de l'aspect

Posons

\[
 x=a/R,\qquad y=b/R,\qquad A=y/x=b/a.
 \tag{38}
\]

Les deux rapports critiques de (7) sont

\[
 q_z=(x^2/y)^{1/3}=(x/A)^{1/3},
 \qquad
 q_r=(y^2/x)^{1/3}=(xA^2)^{1/3}.
 \tag{39}
\]

Leur minimum est maximal lorsque \(A=1\). En particulier,

\[
 A\to\infty
 \quad\Longrightarrow\quad
 \min(q_z,q_r)\leq x^{1/3}A^{-1/3}\to0
 \tag{40}
\]

si \(a/R\) reste borné.

Plus généralement,

\[
 \min(q_z,q_r)
 \leq(q_zq_r)^{1/2}
 =(xy)^{1/6}
 =\left(\frac{ab}{R^2}\right)^{1/6}.
 \tag{41}
\]

Garder \(\|U\|_{L^{3,\infty}}\geq u_0>0\) et \(K\leq K_0\)
imposerait simultanément

\[
 a^2\geq cRbu_0^3/K_0^3,
 \qquad
 b^2\geq cRau_0^3/K_0^3.
 \tag{42}
\]

En multipliant,

\[
 ab\geq cR^2u_0^6/K_0^6.
 \tag{43}
\]

Une section transverse vraiment mince, ou un aspect qui l'amincit dans une
direction, est incompatible avec le gate non petit.

## 4. Énergie et enstrophie

Définissons les constantes de profil

\[
 J_\eta(a/R)
 =\int_{-1}^1
 \frac{\eta(s)^2}{1+(a/R)s}\,ds,
 \qquad
 J_\chi=\int_{-1}^1\chi(t)^2\,dt.
 \tag{44}
\]

Un changement de variables exact donne

\[
 \boxed{
 \|U\|_2^2
 =2\pi V^2Rab\,
 J_\eta(a/R)J_\chi.
 }
 \tag{45}
\]

Ainsi l'énergie cinétique est

\[
 E(U)=\frac12\|U\|_2^2
 \asymp V^2Rab.
 \tag{46}
\]

Les deux composantes du curl sont orthogonales. Avec

\[
 J_{\eta'}(a/R)
 =\int_{-1}^1
 \frac{\eta'(s)^2}{1+(a/R)s}\,ds,
 \quad
 J_{\chi'}=\int_{-1}^1\chi'(t)^2\,dt,
 \tag{47}
\]

on obtient aussi l'identité

\[
 \boxed{
 \|W\|_2^2
 =2\pi V^2R
 \left[
 \frac ab J_\eta J_{\chi'}
 +\frac ba J_{\eta'}J_\chi
 \right].
 }
 \tag{48}
\]

Le grand aspect déplace donc l'enstrophie d'une composante à l'autre; il ne
la supprime pas.

Sous le seul contrôle critique \(K\), (34)--(35) donnent

\[
 V
 \leq CK(Rab)^{-2/3}\min(a,b),
 \tag{49}
\]

et

\[
 E(U)
 \leq CK^2
 \frac{\min(a,b)^2}{(Rab)^{1/3}}.
 \tag{50}
\]

Cette énergie est celle de la donnée initiale \(U\), pas une conservation
démontrée pour une évolution candidate.

## 5. Oscillation directionnelle sur toutes les boules

### 5.1 Direction de la vitesse

Sur \(\{U\ne0\}\),

\[
 U/|U|=e_\theta.
 \tag{51}
\]

Une boule de rayon \(\rho\ll R\), contenue dans le support, voit une
variation \(O(\rho/R)\). Pour
\(\rho\asymp\min(a,b)\), cette oscillation est au moins
\(c\min(a,b)/R\).

Ce constat concerne la direction de la vitesse. Les critères géométriques
de régularité audités dans les cycles précédents portent sur la direction
de la vorticité; les deux ne doivent pas être confondues.

### 5.2 Boule de calotte purement radiale

Choisissons un sous-intervalle radial du plateau de \(\eta\), où
\(\eta'=0\) et \(\eta\geq c_\eta\), et un sous-intervalle d'une calotte de
\(\chi\), où \(|\chi'|\geq c_\chi\). Sur leur produit, (2) devient

\[
 W=-\frac{VR}{rb}\eta\chi'e_r.
 \tag{52}
\]

Soit

\[
 \rho=c_0\min(a,b),
 \tag{53}
\]

avec \(c_0\) dépendant seulement des plateaux de profil. Il existe une boule
euclidienne tridimensionnelle \(B_\rho\), centrée à distance comparable à
\(R\) de l'axe, entièrement contenue dans cette région.

Deux sous-boules de mesure relative fixée, déplacées dans la direction
azimutale de \(\pm\rho/4\), voient des angles séparés de
\(c\rho/R\). Par l'inégalité élémentaire entre deux populations,

\[
 \dashint_{B_\rho}|\xi-\xi_{B_\rho}|
 \geq c\frac\rho R,
 \qquad
 \xi=W/|W|.
 \tag{54}
\]

Si \(\rho\gtrsim R\), la minoration se sature à une constante. Ceci prouve
(10).

Cette boule est tridimensionnelle et décentrée de l'axe. Un test limité au
demi-plan méridien ne voit pas la variation de \(e_r(\theta)\).

### 5.3 Conséquence log-BMO nécessaire

Pour la semi-norme locale

\[
 [\xi]_{\log{\rm BMO}}
 =
 \sup_{0<\operatorname{rad}(B)<r_0}
 |\log\operatorname{rad}(B)|
 \dashint_B|\xi-\xi_B|,
 \tag{55}
\]

la boule (53) impose

\[
 [\xi]_{\log{\rm BMO}}
 \geq
 c\min\left\{1,\frac aR,\frac bR\right\}
 |\log(c_0\min(a,b))|.
 \tag{56}
\]

Après insertion isotrope à l'échelle \(\ell\), le dernier facteur devient

\[
 |\log(c_0\ell\min(a,b))|.
 \tag{57}
\]

L'extension de \(\xi\) sur \(\{W=0\}\) ne change pas (54), puisque toute la
boule est contenue dans \(\{W\ne0\}\).

### 5.4 Corridors logarithmiques : concession optimale

Le profil brut peut avoir des transitions directionnelles d'ordre un entre
les couches \(+e_z\), \(\pm e_r\) et \(-e_z\). Une admissibilité log-BMO
requiert une seule extension unitaire globale, et non une extension
différente pour chaque boule.

Dans les régions ouvertes où \(W=0\), accordons le meilleur mécanisme connu :
une rotation tronquée logarithmique entre une échelle intérieure \(h\) et
une échelle extérieure \(q\),

\[
 L=\log(q/h).
 \tag{58}
\]

L'audit all-ball du cycle 0030 donne alors, de façon optimiste,

\[
 \sup_B\operatorname{MO}_B(\xi)
 \leq C\left(
 \frac1L+\frac qR+
 \min\left\{1,\frac aR,\frac bR\right\}
 \right).
 \tag{59}
\]

Les trois termes correspondent respectivement à la rotation logarithmique,
à la courbure azimutale et à la calotte intrinsèque. Les grandes boules
diluent les corridors; les petites boules voient soit le gradient
logarithmique, soit la variation locale de \(e_r\).

Pour un poids logarithmique de taille \(S\), les choix

\[
 L\gtrsim S,\qquad
 q/R\lesssim S^{-1},\qquad
 \min\{1,a/R,b/R\}\lesssim S^{-1}
 \tag{60}
\]

sont suffisants au niveau des ordres. La dernière condition est déjà
nécessaire par (56). Même sous cette concession,

\[
 \|U\|_{L^{3,\infty}}
 \leq CK S^{-1/3}.
 \tag{61}
\]

Les corridors réparent donc éventuellement la continuité directionnelle,
mais pas le budget critique.

## 6. No-go simultané

Supposons une suite de champs (1) telle que

\[
 \|\nabla\times U_n\|_{L^{3/2,\infty}}\leq K,
 \qquad
 [\xi_n]_{\log{\rm BMO}}\leq M,
 \tag{62}
\]

avec \(K,M\) indépendants de \(n\), et

\[
 \rho_n=c_0\min(a_n,b_n)\longrightarrow0.
 \tag{63}
\]

Par (56),

\[
 m_n
 :=\min\{1,a_n/R_n,b_n/R_n\}
 \leq\frac{CM}{1+|\log\rho_n|}.
 \tag{64}
\]

Si \(a_n\leq b_n\), le premier facteur de (7) satisfait

\[
 \left(\frac{a_n^2}{R_nb_n}\right)^{1/3}
 \leq(a_n/R_n)^{1/3}=m_n^{1/3}.
 \tag{65}
\]

Si \(b_n\leq a_n\), le second donne la même conclusion. Ainsi

\[
 \|U_n\|_{L^{3,\infty}}
 \leq
 CK
 \left(
 \frac{M}{1+|\log\rho_n|}
 \right)^{1/3}
 \longrightarrow0.
 \tag{66}
\]

L'aspect optimal pour les deux budgets Lorentz est \(a_n=b_n\), pas un
aspect croissant. Un aspect croissant ne peut donc pas compenser (66).

Réciproquement, si

\[
 \liminf_n\|U_n\|_{L^{3,\infty}}\geq u_0>0,
 \tag{67}
\]

alors (12) force \(m_n\geq c(u_0/K)^3\), et (56) donne

\[
 [\xi_n]_{\log{\rm BMO}}
 \geq
 c(u_0/K)^3|\log\rho_n|
 \longrightarrow\infty.
 \tag{68}
\]

Il est donc impossible de passer les deux gates dans cette classe produit.

## 7. Temps diffusifs

Avec viscosité \(\nu>0\), les échelles géométriques donnent

\[
 \tau_R=\frac{R^2}{\nu},
 \qquad
 \tau_a=\frac{a^2}{\nu},
 \qquad
 \tau_b=\frac{b^2}{\nu}.
 \tag{69}
\]

La première déformation visqueuse substantielle du profil transverse
intervient au plus tard à

\[
 \tau_{\rm cross}
 =\frac{\min(a,b)^2}{\nu}.
 \tag{70}
\]

Si une interface directionnelle est lissée par un corridor logarithmique
de profondeur \(L\), avec \(h=qe^{-L}\), l'échelle la plus fine est

\[
 \tau_h=\frac{h^2}{\nu}
 =\frac{q^2}{\nu}e^{-2L}.
 \tag{71}
\]

La condition \(L\gtrsim S\) de (60) implique

\[
 \tau_h\leq\frac{q^2}{\nu}e^{-cS}.
 \tag{72}
\]

Cette échelle peut être exponentiellement plus courte que
\(\tau_{\rm cross}\). Le corridor est une construction cinématique de
direction dans une région où \(W=0\); il ne constitue pas une barrière
dynamique à la diffusion. Dès que la longueur de diffusion
\(\sqrt{\nu t}\) atteint \(h\), les couches séparées commencent à se
mélanger.

Sous (18), toutes les quantités de (69)--(72) sont multipliées par
\(\ell^2\), comme l'exige l'équation visqueuse.

## 8. Certificat reproductible

Le script standard-library suivant vérifie :

- l'annulation de courbure avec des rationnels exacts;
- la divergence exacte du curl;
- les identités d'exposants des deux budgets Lorentz;
- le fait que l'aspect un est optimal;
- la géométrie de deux secteurs azimutaux dans la boule de calotte;
- l'échelle diffusive exponentielle du corridor.

~~~python
from fractions import Fraction as F
from math import asin, exp, log, sin


def eta(s):
    return 1 - s * s


def eta_prime(s):
    return -2 * s


def chi(t):
    return 1 - t * t


def chi_prime(t):
    return -2 * t


max_exact_residual = F(0)

# Exact pointwise audit of d_r psi + psi/r and of div(curl U).
for R in (F(3), F(5)):
    for a in (F(1, 4), F(1, 3)):
        for b in (F(2, 5), F(3, 7)):
            for r in (R - a / 2, R + a / 3):
                for z in (-b / 3, b / 4):
                    V = F(7, 5)
                    s = (r - R) / a
                    t = z / b

                    psi = V * R * eta(s) * chi(t) / r
                    dr_psi = V * R * (
                        -eta(s) * chi(t) / (r * r)
                        + eta_prime(s) * chi(t) / (r * a)
                    )
                    curvature = psi / r
                    wz_expected = (
                        V * R * eta_prime(s) * chi(t) / (r * a)
                    )
                    curvature_residual = (
                        dr_psi + curvature - wz_expected
                    )
                    assert curvature_residual == 0

                    wr = -V * R * eta(s) * chi_prime(t) / (r * b)
                    # Differentiate r*wr in r and wz in z.
                    div_r = (
                        -V
                        * R
                        * eta_prime(s)
                        * chi_prime(t)
                        / (r * a * b)
                    )
                    div_z = (
                        V
                        * R
                        * eta_prime(s)
                        * chi_prime(t)
                        / (r * a * b)
                    )
                    divergence_residual = div_r + div_z
                    assert divergence_residual == 0
                    max_exact_residual = max(
                        max_exact_residual,
                        abs(curvature_residual),
                        abs(divergence_residual),
                    )

# Dimensionless Lorentz ratios.  For x=a/R and A=b/a:
# q_z^3=x/A and q_r^3=x*A^2.
for S in (8, 16, 32, 64):
    x = 1.0 / S
    aspects = (1.0, 2.0, S**0.5, float(S))
    best = -1.0
    for A in aspects:
        q_z = (x / A) ** (1.0 / 3.0)
        q_r = (x * A * A) ** (1.0 / 3.0)
        gate = min(q_z, q_r)
        best = max(best, gate)

        R = 1.0
        a = x * R
        b = A * a
        volume_scale = R * a * b
        wz_factor = volume_scale ** (2.0 / 3.0) / a
        wr_factor = volume_scale ** (2.0 / 3.0) / b
        V = 1.0 / max(wz_factor, wr_factor)
        u_proxy = V * volume_scale ** (1.0 / 3.0)
        assert abs(u_proxy - gate) < 2.0e-14

    assert abs(best - x ** (1.0 / 3.0)) < 2.0e-14

# Two points at angles +/-theta lie in the cap ball and their radial
# directions are separated by a constant times rho/R.
for m in (1.0 / 8.0, 1.0 / 16.0, 1.0 / 64.0):
    R = 1.0
    rho = m * R
    theta = 2.0 * asin(rho / (4.0 * R))
    distance_to_center = 2.0 * R * sin(theta / 2.0)
    direction_gap = 2.0 * sin(theta)
    assert abs(distance_to_center - rho / 2.0) < 2.0e-15
    assert direction_gap > 0.9 * rho / R

# Logarithmic corridor and diffusion ratio.
for S in (8, 16, 32, 64):
    q = 1.0
    L = float(S)
    h = q * exp(-L)
    diffusion_ratio = (h / q) ** 2
    assert abs(log(diffusion_ratio) + 2.0 * L) < 3.0e-14

print("exact curvature residual:", max_exact_residual)
print("exact divergence residual:", max_exact_residual)
print("Lorentz aspect budget: PASS")
print("pure-er cap geometry: PASS")
print("log-corridor diffusion scale: PASS")
~~~

Commande de reproduction PowerShell, depuis la racine du dépôt :

~~~powershell
$text = Get-Content docs/reports/navier-stokes/reviews/cycle-0031-countermodel.md
$start = [Array]::IndexOf($text, '~~~python') + 1
$stop = [Array]::IndexOf($text, '~~~', $start)
$text[$start..($stop - 1)] | python -
~~~

Arithmétique : rationnels exacts pour le curl et sa divergence; double IEEE
754 pour les racines cubiques, la géométrie angulaire et les exponentielles.
Tolérance maximale demandée : \(3\times10^{-14}\). Graine : aucune.
Dépendances : bibliothèque standard Python uniquement.

Le script vérifie les identités et les exposants. Il ne certifie pas le
supremum BMO continu ni les constantes implicites dépendant des profils.

Exécution locale observée le 2026-08-14 : résidus rationnels de courbure et
de divergence exactement nuls; quatre tests d'aspect et quatre profondeurs
de corridor passent; aucun résidu flottant ne dépasse
\(3\times10^{-14}\).

## 9. Passe contradictoire

### 9.1 Portée exacte

Le no-go porte sur le produit compact (1), avec facteur \(R/r\), profils de
forme uniformes, plateaux non dégénérés et calottes axiales. Il reste vrai
si les dérivées ne sont pas constantes, grâce à la variation totale et à
(36).

Si une dérivée est concentrée sur une fraction qui tend vers zéro, son
épaisseur effective doit remplacer \(a\) ou \(b\). La norme faible augmente
comme l'inverse de la racine cubique de cette épaisseur; on ne gagne pas le
budget Lorentz en cachant la transition.

### 9.2 Hypothèse de plateau

La boule purement \(e_r\) utilise une région où \(\eta'=0\) et
\(\eta\ne0\). Un profil sans aucun plateau peut masquer \(W_r\) par
\(W_z\) dans toute la calotte. Une telle construction abandonne l'ansatz à
corridor curl-free testé ici et doit être auditée comme un streamfunction
non séparable ou à transitions superposées. Le no-go BMO n'est pas affirmé
pour ce régime.

### 9.3 Extension directionnelle

La majoration (59) est une concession optimiste inspirée des corridors
logarithmiques du cycle 0030. Elle suppose que les composantes de
\(\{W\ne0\}\) laissent assez de régions ouvertes pour construire une seule
extension globale. Le résultat négatif n'en dépend pas : les minorations
(54) et (56) sont internes à \(\{W\ne0\}\).

### 9.4 Pression et dynamique

Le champ \(U\) est une donnée initiale lisse, compacte et divergence-free.
La pression de Navier--Stokes serait obtenue non localement par

\[
 p=\mathcal R_i\mathcal R_j(U_iU_j),
 \tag{73}
\]

mais elle n'intervient pas dans l'obstruction cinématique. Aucun résidu
Navier--Stokes en temps, aucun prolongement d'une solution et aucun profil
de blow-up n'est construit.

### 9.5 Classe axisymétrique

La vitesse \(U=\psi e_\theta\) est axisymétrique avec swirl pur. Son curl
est poloïdal. Elle ne relève donc pas de la classe axisymétrique sans swirl
globalement régulière utilisée pour éliminer le paquet coaxial du cycle
0030. Cette distinction ne sauve pas le candidat : il échoue avant
l'évolution, au couple de gates critiques.

### 9.6 Faible versus fort

Les estimations utilisent les quasi-normes faibles exactes. Aucune
inégalité forte-\(L^p\) n'est substituée au gate. L'énergie (45) est une
quantité sous-critique différente; sa petitesse éventuelle ne prouve pas à
elle seule la régularité.

## 10. Énoncé falsifiable et décision

### Lemme actif C31

Pour la famille (1), avec profils uniformes possédant des plateaux et des
transitions de variation totale non nulle, il existe une constante \(C\)
de profils telle que (7) soit vraie. De plus, toute extension unitaire de la
direction du curl satisfait (56). Par suite, (66) vaut pour toute famille
concentrée vérifiant (62).

Statut : dérivation analytique IA interne, testée algébriquement, non revue
par un évaluateur externe indépendant.

Falsificateur décisif : construire des paramètres et profils satisfaisant
les hypothèses ci-dessus, avec

\[
 K_n+[\xi_n]_{\log{\rm BMO}}\leq C,
 \qquad
 \rho_n\to0,
 \qquad
 \liminf_n\|U_n\|_{L^{3,\infty}}>0.
 \tag{74}
\]

Un tel exemple invaliderait soit l'un des deux budgets de variation totale,
soit la boule de calotte (54).

~~~json
{
  "cycle": "0031",
  "claim": "COMPACT_AXISYMMETRIC_R_OVER_R_ASPECT_NO_GO",
  "status": "AI_DERIVATION",
  "equation": "3D incompressible Navier-Stokes initial-data kinematics",
  "domain": "R^3",
  "solution_type": "smooth compact divergence-free initial velocity; no evolution claim",
  "hypotheses": [
    "U=V(R/r) eta((r-R)/a) chi(z/b) e_theta",
    "uniform nondegenerate plateaus and transition variations",
    "bounded weak-L^(3/2) norm of curl U",
    "bounded logarithmically weighted BMO extension of curl direction"
  ],
  "conclusion": "weak-L3(U) <= C K M^(1/3) [1+|log min(a,b)|]^(-1/3)",
  "adversarial_status": "internal same-model review completed; no external independent review",
  "next_test": "nonseparable cap with W_z masking W_r and no pure-e_r ball"
}
~~~

État : **ABANDONNER** le grand aspect du produit compact (1) comme moyen de
conserver une vitesse faible-\(L^3\) non petite sous les deux gates.

Prochain test discriminant : remplacer le produit par un
\(\psi(r,z)\) non séparable qui maintient une composante \(W_z\) dans toute
calotte où \(\partial_z\psi\ne0\), puis vérifier si la variation totale
bidimensionnelle reproduit malgré tout l'un des deux facteurs de (7). Ce
test est exactement la branche de masquage laissée ouverte par le cycle
0027.
