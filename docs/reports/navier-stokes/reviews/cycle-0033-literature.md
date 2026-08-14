# Cycle 0033 — veille primaire : degré des extrema, Gauss map et défaut VMO

Date de coupure : 2026-08-14.

Objet : audit différentiel du verrou topologique suggéré par les profils de
streamfunction axisymétriques. On cherche à savoir si un extremum isolé de la
streamfunction force une oscillation de

\[
 \xi=\frac{\nabla^\perp F}{|\nabla F|}
\]

assez quantitative pour contredire une hypothèse log-BMO, et si les endpoints
Lorentz critiques permettent de rattacher ce défaut à une boule portant une
masse de vorticité. Les passages marqués **AI_DERIVATION** sont des
conséquences du laboratoire à partir de théorèmes publiés; ils ne doivent pas
être promus automatiquement en PAPER_PROOF.

## Verdict différentiel

1. Si \(p\) est un extremum local strict et un zéro critique isolé d'une
   fonction \(F\in C^1\) dans le plan, l'indice local de \(\nabla F\) en
   \(p\) vaut \(+1\). Pour un maximum, le signe reste \(+1\) en dimension
   deux parce que \(\deg(-I_{\mathbb R^2})=+1\). La rotation fixe
   \(J(a,b)=(-b,a)\) ne change pas le degré.

2. Si \(c\) est une valeur régulière proche de \(F(p)\), la composante fermée
   de \(\{F=c\}\) qui entoure \(p\) est une courbe simple régulière. Sa Gauss
   map tangentielle

   \[
     \Gamma_c\ni x\longmapsto
     \frac{J\nabla F(x)}{|\nabla F(x)|}\in S^1
   \]

   a degré \(+1\) ou \(-1\) selon l'orientation. C'est le théorème de
   rotation des tangentes de Hopf, non une estimation ponctuelle de courbure.

3. Le degré fournit une obstruction **ambiante**. Si un petit disque \(D\)
   contient \(p\) et aucun autre zéro de \(\nabla F\), toute définition
   arbitraire de \(\xi\) au point \(p\) laisse une application \(S^1\)-valuée
   presque partout. Cette application ne peut appartenir à \(VMO(D)\).
   Sinon le degré VMO avec trace de Brezis–Nirenberg donnerait

   \[
      \deg(\xi,D,0)=\deg(\xi|_{\partial D},S^1)=1,
   \]

   donc \(0\in\operatorname{essR}(\xi)\), en contradiction avec
   \(|\xi|=1\) presque partout. Ce raccord est une **AI_DERIVATION** courte
   et falsifiable.

4. Par conséquent, avec

   \[
   \Omega_\xi(\rho)=
   \sup_{\substack{B_s(x)\Subset D\\0<s\le \rho}}
       \fint_{B_s(x)}|\xi-\xi_{B_s(x)}|,
   \]

   on a

   \[
      \lim_{\rho\downarrow0}\Omega_\xi(\rho)>0.             \tag{1}
   \]

   Il existe des boules euclidiennes \(B_j\Subset D\), de rayons
   \(r_j\downarrow0\), et une constante \(c_\xi>0\), dépendant a priori du
   profil, telles que

   \[
      \fint_{B_j}|\xi-\xi_{B_j}|\ge c_\xi.                  \tag{2}
   \]

   Sous la convention

   \[
     [f]_{\mathrm{bmo}_{1/|\log r|}}
     =\sup_{r<r_0}|\log r|\,
       \fint_{B_r}|f-f_{B_r}|,
   \]

   (2) implique

   \[
      [\xi]_{\mathrm{bmo}_{1/|\log r|}(D)}=\infty.           \tag{3}
   \]

5. Pour un champ axisymétrique supporté loin de l'axe, le défaut méridien se
   relève en trois dimensions le long du cercle obtenu par rotation de \(p\).
   Un argument local produit–Fubini, dans une carte cylindrique
   bi-lipschitz, transfère (2) à des boules tridimensionnelles. Le défaut n'est
   donc pas un artefact d'une tranche de mesure nulle.

6. Cela ne ferme pas le raccord Lorentz. Le degré ne donne ni valeur
   explicite de \(c_\xi\), ni minoration du rayon d'une boule mauvaise, ni
   minoration de \(|\nabla F|\) ou de la masse de vorticité sur cette boule.
   La rotation totale peut être comprimée dans des arcs arbitrairement petits
   et placée là où \(|\nabla F|\) est très faible.

7. Une extension \(S^1\to\overline{B^2}\) existe toujours, mais un degré de
   bord non nul l'oblige à rencontrer \(0\). Une extension BMO de Jones est
   vectorielle et ne préserve pas la cible \(S^1\). La renormaliser exige une
   minoration de son module, précisément interdite par le degré non nul.

8. La veille 2025–2026 ne change pas ce verdict. Lei–Ren–Tian reste en
   arXiv:2501.08976v1; leur double cône ne porte que sur les fortes
   vorticités. Grujić arXiv:2607.08866 reste en v2 et suppose le log-BMO de la
   direction; (3) identifie une classe de profils qui ne peut satisfaire
   cette hypothèse. Grujić arXiv:2511.00725 reste en v3 et décrit un
   mécanisme conditionnel. Aucune source primaire repérée ne transforme le
   degré d'un extremum en masse Lorentz localisée.

## 1. Cadre exact, équation et échelles

Le problème Clay de référence reste Navier–Stokes incompressible non forcé
sur \(\mathbb R^3\), avec \(\nu>0\),

\[
 \partial_tu+(u\cdot\nabla)u+\nabla p=\nu\Delta u,
 \qquad \nabla\cdot u=0.                                    \tag{4}
\]

L'objet topologique de ce cycle est cinématique et à temps fixé. Dans le
demi-plan méridien \(H=\{(r,z):r>0\}\), loin de l'axe, on considère

\[
 U=\frac{F(r,z)}r e_\theta,\qquad
 W=\operatorname{curl}U
 =-\frac{F_z}{r}e_r+\frac{F_r}{r}e_z.                        \tag{5}
\]

Sur \(\{\nabla F\ne0\}\), la direction de la vorticité totale est

\[
 \xi_W
 =\frac{-F_z e_r+F_r e_z}{|\nabla F|},                      \tag{6}
\]

qui s'identifie dans le demi-plan à \(J\nabla F/|\nabla F|\). Le facteur
\(1/r>0\) n'affecte pas la direction. Si le support touche l'axe, la base
\(e_r\) dégénère et les conditions au pôle de **NS-SRC-0102** doivent être
réintroduites; le présent audit exclut ce cas.

Sous l'échelle Navier–Stokes,

\[
 U_\lambda(x)=\lambda U(\lambda x),\qquad
 W_\lambda(x)=\lambda^2W(\lambda x),
\]

on a \(F_\lambda(r,z)=F(\lambda r,\lambda z)\) et
\(\xi_\lambda(r,z)=\xi(\lambda r,\lambda z)\).

| Quantité | Loi d'échelle |
|---|---|
| \(\|U\|_{L^{3,\infty}(\mathbb R^3)}\) | invariante |
| \(\|W\|_{L^{3/2,\infty}(\mathbb R^3)}\) | invariante |
| semi-norme BMO de \(\xi\) | invariante |
| rayon d'une boule mauvaise | \(r\mapsto r/\lambda\) |
| \(|\log r|\operatorname{MO}_{B_r}(\xi)\) | non homogène; détecte le défaut aux petites échelles |

Une obstruction de degré est invariante par dilatation. Elle peut donc suivre
une concentration vers zéro, sans fixer une échelle physique absolue.

## 2. Indice du gradient autour d'un extremum

### Source primaire

Herbert Amann,
[*A note on degree theory for gradient mappings*](https://doi.org/10.1090/S0002-9939-1982-0660610-2),
*Proc. Amer. Math. Soc.* **85** (1982), 591–595, démontre notamment que
l'indice local du gradient d'une fonctionnelle \(C^1\) à un minimum local
isolé vaut \(1\). Le résultat contient le cas fini-dimensionnel utilisé ici.

Soit \(p\) un zéro isolé de \(\nabla F\), qui est aussi un minimum local
strict. Pour un disque \(D=B_R(p)\) assez petit,
\(\nabla F\ne0\) sur \(\partial D\), et

\[
 \operatorname{ind}_p(\nabla F)
 =\deg\!\left(\frac{\nabla F}{|\nabla F|},
              \partial D,S^1\right)
 =1.                                                        \tag{7}
\]

Si \(p\) est un maximum, on applique le résultat à \(-F\). En dimension deux,

\[
 \deg\!\left(\frac{-\nabla F}{|\nabla F|}\right)
 =\deg(-I_{\mathbb R^2})
  \deg\!\left(\frac{\nabla F}{|\nabla F|}\right)
 =1.                                                        \tag{8}
\]

Enfin \(J\in SO(2)\), donc

\[
 \deg\!\left(\frac{J\nabla F}{|\nabla F|}\right)=1.          \tag{9}
\]

Les hypothèses « extremum strict » et « zéro critique isolé » ne doivent pas
être fusionnées. Un extremum strict peut être accumulé par d'autres points
critiques; il faut isoler le zéro pour définir l'indice local.

## 3. Gauss map des courbes de niveau

### Sources primaires

Heinz Hopf,
[*Über die Drehung der Tangenten und Sehnen ebener
Kurven*](https://www.numdam.org/item/CM_1935__2__50_0/),
*Compositio Math.* **2** (1935), 50–62, donne une preuve du théorème de
rotation : la direction tangentielle d'une courbe plane simple fermée
régulière accomplit une rotation totale de \(\pm2\pi\).

Hassler Whitney,
[*On regular closed curves in the
plane*](https://www.numdam.org/item/CM_1937__4__276_0/),
*Compositio Math.* **4** (1937), 276–284, systématise le nombre de rotation
et la classification des courbes régulières fermées.

Si \(c\) est une valeur régulière de \(F\), toute composante compacte
\(\Gamma_c\) de \(\{F=c\}\) est une courbe simple fermée. Sa tangente unité
est

\[
 \tau=\pm\frac{J\nabla F}{|\nabla F|}.                       \tag{10}
\]

Hopf implique

\[
 \deg(\tau:\Gamma_c\to S^1)=\pm1.                            \tag{11}
\]

Pour des valeurs régulières proches d'un extremum isolé, (11) est la version
géométrique de (9). Il ne dit pas que la courbure est uniformément distribuée.
Une famille de courbes en forme de stade, avec deux segments presque plats et
des calottes de plus en plus petites, garde le nombre de rotation \(1\) tout
en concentrant la rotation sur une fraction de longueur tendant vers zéro.

### Petit BMO sur le cercle

Paramétrons \(\Gamma_c\) par longueur d'arc normalisée
\(\gamma:S^1\to\Gamma_c\). La map
\(g=\xi\circ\gamma:S^1\to S^1\) est continue et de degré non nul. Le théorème
4 et le lemme A.18 de Brezis–Nirenberg Part I, déjà **NS-SRC-0090**, donnent
une constante \(\delta_{S^1}>0\), dépendant de la normalisation BMO du cercle,
telle qu'une map \(S^1\)-valuée de semi-norme BMO inférieure à ce seuil est
topologiquement triviale après régularisation. Par contraposition,

\[
  [g]_{BMO(S^1)}\ge\delta_{S^1}.                             \tag{12}
\]

Il existe un arc paramétrique avec oscillation moyenne minorée. La source ne
fournit pas une valeur numérique canonique de \(\delta_{S^1}\), et (12) n'est
pas encore une boule du plan : convertir l'arc en disque avec une proportion
d'aire contrôlée requiert une constante chord–arc, un reach ou une borne de
courbure.

## 4. Degré VMO sur un domaine et défaut log-BMO

### Source primaire nouvelle

Haïm Brezis et Louis Nirenberg,
[*Degree theory and BMO; Part II: Compact manifolds with
boundaries*](https://doi.org/10.1007/BF01587948),
*Selecta Math. (N.S.)* **2** (1996), 309–368, étendent le degré aux maps VMO
sur des domaines. Les points utilisés ici sont :

- §II.2, propriété 1 : si \(\deg(u,\Omega,p)\ne0\), alors
  \(p\in\operatorname{essR}(u)\);
- §II.3 : définition des classes \(VMO_\varphi(\Omega)\) ayant une trace VMO;
- §II.4, théorème 3 : le degré intérieur est égal au degré de la trace
  normalisée sur le bord;
- appendice 3 : l'extension harmonique d'une trace VMO appartient à la classe
  VMO correspondante, sans préserver une cible sphérique.

### Lemme candidat : un extremum isolé interdit VMO

**Énoncé (AI_DERIVATION, candidat TOOL_LEMMA).** Soit
\(D=B_R(p)\Subset\mathbb R^2\) et \(F\in C^1(\overline D)\). Supposons que
\(p\) soit un extremum local strict, que

\[
 \nabla F(x)\ne0\qquad x\in\overline D\setminus\{p\},        \tag{13}
\]

et définissons \(\xi=J\nabla F/|\nabla F|\) sur
\(D\setminus\{p\}\), avec une valeur arbitraire en \(p\). Alors

\[
 \xi\notin VMO(D;\mathbb R^2).                               \tag{14}
\]

**Preuve.** Par (9), la trace continue
\(\varphi=\xi|_{\partial D}:\partial D\to S^1\) a degré \(1\). Supposons
\(\xi\in VMO(D)\). Comme \(\xi\) est continue dans un collier du bord, elle
appartient à \(VMO_\varphi(D)\). Le théorème 3 de Brezis–Nirenberg donne

\[
 \deg(\xi,D,0)=\deg(\varphi,\partial D,S^1)=1.
\]

La propriété 1 donne \(0\in\operatorname{essR}(\xi)\). Or
\(|\xi|=1\) presque partout, donc
\(\operatorname{essR}(\xi)\subset S^1\), contradiction. \(\square\)

La valeur choisie au point critique ne change rien, puisqu'un point est de
mesure nulle. En revanche, (13) est essentielle : si l'ensemble des zéros est
une courbe ou possède une aire positive, la direction et sa trace doivent
être reformulées.

### De non-VMO à une suite de boules

Une application bornée est BMO. Sur un domaine lisse, la caractérisation VMO
par petites boules de Brezis–Nirenberg Part II donne

\[
 \xi\in VMO(D)
 \quad\Longleftrightarrow\quad
 \Omega_\xi(\rho)\longrightarrow0.                          \tag{15}
\]

Comme (14) exclut le membre gauche, la limite monotone de
\(\Omega_\xi(\rho)\) est un nombre \(a_\xi>0\). Pour tout \(j\), on peut
choisir \(B_j=B_{r_j}(x_j)\Subset D\), avec \(r_j<1/j\), telle que

\[
 \fint_{B_j}|\xi-\xi_{B_j}|\ge a_\xi/2.                      \tag{16}
\]

La continuité uniforme de \(\xi\) sur tout compact de
\(\overline D\setminus\{p\}\) impose \(x_j\to p\). En multipliant (16) par
\(|\log r_j|\), on obtient (3).

Cette conséquence produit de vraies boules euclidiennes de rayons
arbitrairement petits. Mais la constante \(a_\xi\) n'est pas suivie
explicitement. Une version uniforme demanderait de reprendre
quantitativement la régularisation, la projection sur \(S^1\) et les
constantes d'équivalence des normes BMO sur le disque.

### Raccord du défaut méridien au champ tridimensionnel

Pour (5), un point critique méridien \(p=(R,z_0)\), avec \(R>0\), engendre en
trois dimensions un cercle de vorticité nulle. Ce changement de codimension
ne répare pas VMO. Dans un tube de rayon \(o(R)\), les coordonnées

\[
 (y_1,y_2,y_3)=(r-R,z-z_0,R(\theta-\theta_0))
\]

forment une carte \(C^1\) uniformément bi-lipschitz. Les coefficients de (6)
sont indépendants de \(y_3\); seule la base \(e_r(\theta)\) effectue une
rotation lisse de taille \(O(|y_3|/R)\). En prenant le produit d'une boule
plane mauvaise de (16) avec un intervalle de longueur comparable à son rayon,
Fubini conserve l'oscillation moyenne, à une erreur \(O(r_j/R)\).
L'équivalence BMO entre cubes, cylindres d'excentricité bornée et boules,
ainsi que l'invariance par difféomorphisme \(C^1\) de Brezis–Nirenberg Part
II, donnent des boules tridimensionnelles \(\widetilde B_j\) telles que

\[
 \fint_{\widetilde B_j}
   |\xi_W-(\xi_W)_{\widetilde B_j}|
 \ge c_\xi/C-o(1).                                          \tag{17}
\]

Ainsi le champ tridimensionnel n'est pas VMO près du cercle et échoue au
petit-rayon log-BMO. Ce raccord est une **AI_DERIVATION** par produit local;
il suppose \(R>0\). Sur l'axe, la carte n'est plus bi-lipschitz.

## 5. Extensions dans le cercle et dans la boule

Il faut distinguer trois problèmes d'extension.

### 5.1 Extension à valeurs dans \(S^1\)

Une map continue \(g:\partial D\to S^1\) s'étend continûment en
\(G:D\to S^1\) si et seulement si \(\deg g=0\). Brezis–Nirenberg Part I
étend cette dichotomie aux relèvements VMO : une map
\(g\in VMO(S^1,S^1)\) de degré zéro s'écrit \(g=e^{i\phi}\) avec
\(\phi\in VMO(S^1,\mathbb R)\), et réciproquement. Pour un degré non nul, une
extension \(S^1\)-valuée sans défaut est impossible.

### 5.2 Extension à valeurs dans la boule fermée

Toute map continue \(g:S^1\to S^1\) possède une extension dans
\(\overline{B^2}\), par exemple

\[
 G(\rho e^{i\theta})=\rho\,g(e^{i\theta}).                   \tag{18}
\]

Si \(\deg g\ne0\), toute extension continue doit atteindre \(0\). Plus
fortement, si \(G\in VMO_g(D;\mathbb R^2)\), si la trace vérifie
\(|g|=1\) et a degré \(k\ne0\), alors pour chaque \(y\in B^2\),

\[
 \deg(G,D,y)=k,\qquad y\in\operatorname{essR}(G).             \tag{19}
\]

La boule ouverte est donc contenue dans l'image essentielle. Le prix est la
perte de la contrainte \(|G|=1\).

### 5.3 Extension BMO de Jones

Peter Jones, **NS-SRC-0074**, construit des extensions BMO scalaires ou
vectorielles sur les domaines uniformes, avec constante uniforme sur les
boules. Appliquée composante par composante à une direction, cette extension
prend ses valeurs dans \(\mathbb R^2\), pas dans \(S^1\). Une projection
radiale \(G\mapsto G/|G|\) n'est licite que si

\[
 \operatorname*{ess\,inf}|G|>0.                              \tag{20}
\]

Pour une trace de degré non nul, (19) interdit (20). Jones permet donc la
localisation analytique d'une semi-norme BMO, mais ne peut effacer le défaut
topologique tout en conservant une direction unité.

## 6. Quelle « boule quantitative » obtient-on ?

| Conclusion | Statut obtenu par le degré | Trou restant |
|---|---|---|
| arc de niveau avec \(MO\ge\delta_{S^1}\) | oui, petit BMO et degré sur \(S^1\) | conversion arc–boule sans chord–arc/reach |
| boules planes \(r_j\downarrow0\), \(MO\ge c_\xi>0\) | oui, via non-VMO | constante universelle non suivie |
| boules 3D près du cercle critique | oui, par produit local loin de l'axe | constante de carte, cas de l'axe |
| rayon comparable au coeur de concentration | non | reach, courbure ou non-dégénérescence |
| fraction uniforme de masse \(|W|\) ou Lorentz | non | minoration de \(|\nabla F|\) et épaisseur |

Pour exclure \(\mathrm{bmo}_{1/|\log r|}\), une constante universelle n'est
pas nécessaire : tout \(c_\xi>0\) fixé pour le profil suffit dans (16). Le
point négatif est que certains critères Navier–Stokes ne regardent la
direction que sur la zone de forte vorticité. Le défaut topologique peut être
logé là où \(|W|\) est arbitrairement petit.

### Contre-profil géométrique reproductible

Considérons des courbes simples lisses \(\Gamma_\varepsilon\) en forme de
stade, de longueur normalisée, dont les calottes ont longueur relative
\(O(\varepsilon)\). Il existe une fonction lisse \(F_\varepsilon\) dans un
tube de \(\Gamma_\varepsilon\) telle que
\(\Gamma_\varepsilon=\{F_\varepsilon=c\}\) et

\[
 |\nabla F_\varepsilon|(s,0)=a_\varepsilon(s)>0,             \tag{21}
\]

où \(a_\varepsilon\) est très petit sur les calottes. Alors :

- la Gauss map a toujours degré \(1\);
- la rotation se concentre sur des arcs \(O(\varepsilon)\);
- la direction y oscille d'ordre un;
- la masse de \(|\nabla F_\varepsilon|\), donc de \(|W|\), portée par ces
  arcs peut tendre vers zéro;
- aucune borne supérieure faible-\(L^{3/2}\) n'empêche ce choix.

Ce test ne réfute pas (14)–(17). Il réfute le raccord non justifié

\[
 \text{défaut topologique}
 \Longrightarrow
 \text{défaut porté par une masse critique de vorticité}.    \tag{22}
\]

## 7. Pourquoi les endpoints Lorentz ne ferment pas le raccord

Dans la classe (5), les gates critiques sont

\[
 \|U\|_{L^{3,\infty}}\ge\kappa,\qquad
 \|W\|_{L^{3/2,\infty}}\le K.                                \tag{23}
\]

Ils portent sur les distributions de **magnitude**. La direction (6) est
inchangée si l'on multiplie localement \(\nabla F\) par un facteur positif,
tandis que la masse Lorentz peut changer arbitrairement. Les endpoints (23)
ne contrôlent pas :

- le reach d'une courbe de niveau;
- sa courbure ou son caractère chord–arc;
- l'épaisseur d'un tube où la direction reste proche de sa trace;
- une minoration de \(|\nabla F|\) sur la zone de rotation;
- la distance de cette zone à \(\{W=0\}\);
- la fraction du gate vitesse portée par le coeur topologique.

La borne globale \(\|U\|_{L^{3,\infty}}\ge\kappa\) peut être réalisée loin du
défaut. La borne supérieure sur \(\|W\|_{L^{3/2,\infty}}\) autorise que la
vorticité soit petite là où la direction tourne. Aucun théorème de
réarrangement ne couple le degré et la magnitude.

En particulier, **aucune des sources topologiques auditées ne donne** une
minoration de la forme

\[
 \operatorname{MO}_{B}(\xi)
 \ge c_\Lambda\left(\frac{K_U}{K_W}\right)^6,                \tag{24}
\]

ni même une boule portant une fraction contrôlée de la distribution de
\(|W|\). Le degré donne le nombre \(c_\xi>0\) de (16), dépendant du profil et
sans relation publiée avec \(K_U/K_W\). La borne (24) obtenue indépendamment
dans l'analyse principale du cycle par troncature, coaire et cône doit donc
être enregistrée comme une dérivation analytique distincte; elle n'est ni une
conséquence de Hopf/Whitney, ni une conséquence de Brezis–Nirenberg.

Un lemme transférable devrait ajouter au minimum une hypothèse du type

\[
 \begin{aligned}
 &\Gamma\text{ chord–arc avec constante }C_{ca},\qquad
   \operatorname{reach}(\Gamma)\ge\rho,\\
 &|\nabla F|\ge m>0\text{ dans un tube de largeur }\eta\rho.
 \end{aligned}                                               \tag{25}
\]

Sous (25), l'arc de (12) peut être épaissi en une boule avec proportion
d'aire et masse contrôlées. Mais (25) est superposé aux endpoints; il n'en
découle pas.

## 8. Raccord aux critères récents de direction

### Lei–Ren–Tian, 2025

**NS-SRC-0061**, Zhen Lei, Xiao Ren et Gang Tian,
[*A geometric characterization of potential Navier-Stokes
singularities*](https://arxiv.org/abs/2501.08976v1), reste une v1 soumise le
15 janvier 2025, sans publication indiquée au 2026-08-14. Le cadre est une
solution faible adaptée locale dans \(Q(1)\), viscosité \(1\), sans force. La
condition impose que les vecteurs de forte vorticité restent dans un double
cône fixe; elle implique la régularité dans \(Q(1/2)\).

Un degré \(1\) sur une courbe complète force la direction méridienne à couvrir
\(S^1\), mais ne contredit le double cône que si les points hors du cône
appartiennent au superniveau de forte vorticité. Le contre-profil (21) montre
pourquoi cette implication manque.

### Grujić, 2026

**NS-SRC-0059**, Zoran Grujić,
[*Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the
3D Navier-Stokes Equations*](https://arxiv.org/abs/2607.08866v2), reste une
v2 du 13 juillet 2026, sans publication indiquée. Le cadre annoncé est
Navier–Stokes incompressible non forcé sur \(\mathbb R^3\), dans un scénario
ponctuel critique avec
\(\omega\in L_t^\infty L_x^{3/2,\infty}\) et direction localement dans
\(\mathrm{bmo}_{1/|\log r|}\).

Le lemme (14), son raccord 3D (17) et (3) donnent l'implication

\[
 \boxed{
 \begin{gathered}
 \omega\text{ méridienne issue d'un }F,\\
 F\text{ possède un extremum critique isolé loin de l'axe}
 \end{gathered}
 }
 \Longrightarrow
 \xi_W\notin\mathrm{bmo}_{1/|\log r|}\text{ local}.          \tag{26}
\]

Le transfert vers l'hypothèse exacte de la prépublication exige que sa
direction BMO soit évaluée sur des boules qui traversent le cercle de zéro. Si
la direction n'est imposée que sur un superniveau de \(|\omega|\), une
extension depuis l'ensemble actif est un lemme supplémentaire, et Jones ne
préserve pas la cible unité.

**NS-SRC-0112**, Grujić,
[*On taming Moffatt–Kimura vortices of doom in the viscous
case*](https://arxiv.org/abs/2511.00725v3), reste une v3 du 10 juin 2026. Le
texte propose un mécanisme conditionnel à deux couches et une cancellation
Hardy/log-composite-bmo; il ne fournit pas le raccord topologie–magnitude de
(22).

### Veille négative

Les recherches primaires ciblées « vorticity direction/alignment » pour
2025–2026 n'ont pas fait apparaître, au-delà de ces sources déjà cataloguées,
de théorème publié ou de nouvelle version arXiv qui :

1. déduise un confinement ou un log-BMO depuis un degré de streamfunction;
2. couple un indice de gradient non nul à une masse
   \(L^{3/2,\infty}\) localisée;
3. fournisse une constante chord–arc ou de reach depuis les seuls endpoints;
4. transforme une extension BMO vectorielle en direction \(S^1\)-valuée sans
   zéro.

L'annonce **NS-WATCH-0004** sur la régularité axisymétrique avec swirl reste
arXiv:2606.07869v1 du 5 juin 2026 et n'est pas utilisée ici.

## 9. Sources nouvelles proposées pour le catalogue

Le catalogue s'arrête à **NS-SRC-0135** au HEAD audité. Les identifiants
suivants sont provisoires.

| ID proposé | Source primaire | Statut vérifié | Rôle exact | Classe maximale |
|---|---|---|---|---|
| **NS-SRC-0136** | Heinz Hopf, [*Über die Drehung der Tangenten und Sehnen ebener Kurven*](https://www.numdam.org/item/CM_1935__2__50_0/), *Compositio Math.* 2 (1935), 50–62 | publié, texte primaire NUMDAM | rotation totale \(\pm2\pi\) de la tangente d'une courbe simple fermée | TOOL_LEMMA géométrique |
| **NS-SRC-0137** | Herbert Amann, [DOI 10.1090/S0002-9939-1982-0660610-2](https://doi.org/10.1090/S0002-9939-1982-0660610-2), *Proc. AMS* 85 (1982), 591–595 | publié, article évalué | indice local \(+1\) du gradient à un minimum isolé; maximum par changement de signe en 2D | TOOL_LEMMA |
| **NS-SRC-0138** | Haïm Brezis et Louis Nirenberg, [DOI 10.1007/BF01587948](https://doi.org/10.1007/BF01587948), *Selecta Math.* 2 (1996), 309–368 | publié, texte primaire relu par sections | degré VMO sur domaines, trace et image essentielle | TOOL_LEMMA; (14)–(26) restent AI_DERIVATION |
| **NS-SRC-0139** | Hassler Whitney, [*On regular closed curves in the plane*](https://www.numdam.org/item/CM_1937__4__276_0/), *Compositio Math.* 4 (1937), 276–284 | publié, texte primaire NUMDAM | nombre de rotation des courbes régulières fermées | BACKGROUND/TOOL_LEMMA |

La source **NS-SRC-0090** (Brezis–Nirenberg Part I) et la source
**NS-SRC-0074** (Jones) doivent être enrichies plutôt que dupliquées : Part I
contient aussi petit BMO, stabilité du degré et relèvements \(S^1\); Jones ne
préserve pas la cible unité.

## 10. Passe contradictoire

1. **Extremum non isolé.** Sans isolement du zéro de \(\nabla F\), l'indice
   local n'est pas défini comme en (7).
2. **Dimension oubliée.** Un maximum donne \((-1)^n\) après changement de
   signe; le maintien de \(+1\) est propre à \(n=2\).
3. **Courbe non simple.** Une composante compacte d'un niveau régulier plan
   est plongée. Un niveau critique n'autorise pas (11).
4. **Gauss map prise pour une borne de courbure.** Le degré fixe seulement la
   rotation totale; les calottes du stade concentrent la courbure.
5. **Arc BMO pris pour une boule plane.** Il faut une géométrie
   chord–arc/reach.
6. **Tranche 2D prise pour une conclusion 3D.** Le raccord exige le produit
   local (17), \(R>0\) et le contrôle de la base cylindrique.
7. **Non-VMO pris pour constante universelle.** (14) donne \(a_\xi>0\) pour
   chaque profil; la présente dérivation ne suit pas une valeur uniforme.
8. **Extension dans la boule prise pour direction.** (18) traverse \(0\);
   elle n'est plus \(S^1\)-valuée.
9. **Jones pris pour une rétraction.** La projection radiale est singulière à
   zéro, que le degré force.
10. **Valeur au zéro de vorticité.** Modifier \(\xi(p)\) ne répare pas VMO;
    le défaut vit à toutes les échelles.
11. **Endpoint Lorentz pris pour minoration.** Une borne supérieure
    faible-\(L^{3/2}\) n'empêche pas \(|W|\) d'être minuscule là où \(\xi\)
    tourne.
12. **Gate vitesse global pris pour gate local.** Une norme faible-\(L^3\)
    non petite peut être portée loin de l'extremum.
13. **Critère high-vorticity pris pour contrôle global.** Le degré peut se
    réaliser dans la zone low-vorticity.
14. **BMO et bmo pondéré confondus.** (3) utilise le petit-rayon
    \(MO/\phi(r)\), avec \(\phi(r)=1/|\log r|\).
15. **Profil cinématique pris pour solution NS.** Aucun \(F\) construit ici
    ne satisfait l'évolution (4), le calcul de pression ou une notion Clay.
16. **Statut récent.** Les arXiv v1/v2/v3 ne sont pas promus en résultats
    publiés, et aucune dérivation IA ne reçoit PAPER_PROOF.

## 11. Lemme actif et test adverse décisif

Le premier maillon transférable est

\[
 \boxed{
 \text{extremum critique isolé de }F
 \Longrightarrow
 \xi=\nabla^\perp F/|\nabla F|\notin VMO
 \Longrightarrow
 [\xi]_{\mathrm{bmo}_{1/|\log r|}}=\infty.}                 \tag{27}
\]

Le test adverse doit chercher à casser **l'uniformité** et le raccord de
masse, non le degré :

1. construire des \(F_\varepsilon\in C_c^\infty(H)\), à distance fixe de
   l'axe, avec un unique maximum dans le coeur et des niveaux en stade de
   reach \(\rho_\varepsilon\downarrow0\);
2. imposer un facteur transverse \(a_\varepsilon(s)\) très petit sur les
   calottes où la tangente tourne;
3. calculer les vraies quantités du champ total

   \[
   K_U=\|F_\varepsilon/r\|_{L^{3,\infty}},\quad
   K_W=\|\nabla F_\varepsilon/r\|_{L^{3/2,\infty}},\quad
   M(\rho)=\sup_{r_B\le\rho}\operatorname{MO}_B(\xi_\varepsilon);
   \]

4. vérifier que \(M(\rho)\) ne tend pas vers zéro, puis mesurer si les boules
   responsables portent une fraction de masse de \(|W|\) tendant vers zéro;
5. enregistrer reach, courbure, épaisseur du tube, minimum de
   \(|\nabla F|\), divergence et erreurs de quadrature.

Deux issues sont discriminantes :

- si la masse sur toute boule topologiquement mauvaise peut tendre vers zéro
  alors que \(K_U\ge\kappa\) et \(K_W\le K\), (22) est réfuté sous les seuls
  endpoints et l'axe doit pivoter vers une hypothèse de superniveau/reach;
- si une minoration uniforme survit aux dégénérescences et peut être prouvée,
  elle devient le nouveau lemme de raccord à tester contre les sommes non
  séparables.

Même dans la seconde issue, le résultat restera cinématique jusqu'à ce qu'une
solution ancienne, une limite de blow-up ou l'évolution Navier–Stokes
produise les hypothèses géométriques requises.
