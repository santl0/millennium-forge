# Passe analytique indépendante — cycle 0028 : masquage non séparable et échappatoire torique

Date : 2026-08-14

Statut : **dérivation IA interne**, non publiée, non indépendante au sens inter-familles et jamais `PAPER_PROOF`

## Verdict

Le verrou `GAP-NONSEPARABLE-RETURN-FLOW-MASKING` se sépare en deux questions qui n’ont pas la même réponse.

1. Pour tout champ poloïdal axisymétrique
   \[
   W=-\frac{F_z}{r}e_r+\frac{F_r}{r}e_z,
   \qquad F=r\psi,
   \]
   le défaut de masquage
   \[
   \Delta_\Omega
   =\int_{\Omega^*}|W_r|dx
   -\frac1{\sqrt{15}}
    \int_{\Omega^*}|W_z|dx
   \]
   force exactement
   \[
   \left|\Omega^*\cap
   \{|W_r|\geq|W|/4\}\right|
   \geq
   \left(\frac{(\Delta_\Omega)_+}{3K}\right)^3.
   \]
   C’est le lemme terminal correct pour une somme finie. Le rang séparé ne donne cependant **aucune minoration uniforme de `Δ_Ω`** : les profils `C^∞` arbitraires ne contrôlent ni la courbure, ni le reach, ni l’épaisseur de la dernière couche. La finitude algébrique de la somme n’est pas une hypothèse géométrique.

2. Le champ torique
   \[
   W_h=a_h b(d/h)e_\theta
   \]
   est lisse, compact et exactement divergence-free. Il vérifie `W_r=W_z=0`; il échappe donc complètement au lemme précédent. Sa direction peut être prolongée unitairement de `e_θ` vers `e_z` dans un corridor `h<d<H` avec
   \[
   [\zeta]_{\mathrm{BMO}}
   \asymp\frac1{\log(H/h)}
   \]
   lorsque `H/R` est subordonné à ce logarithme. Le contrôle porte sur **toutes** les boules, pas seulement sur les boules centrées sur le tore.

3. Cette voie torique n’est pas un candidat de blow-up Clay. Sur `R³`, le champ de vitesse de Biot–Savart a une queue multipolaire, car l’impulsion du tore de signe unique est non nulle; il n’est donc pas une donnée de Schwartz du cas (A). Il est en outre axisymétrique sans swirl, classe globalement régulière. Une périodisation donne bien une donnée lisse du cas Clay (B), mais sa norme critique de vitesse satisfait la borne directe `||u||₃³≤CK³(h/R+(h/R)²)` et tend vers zéro.

La recommandation est d’abandonner « rang fini » comme substitut de capacité et de retenir deux lemmes minimaux : le **lemme d’excès radial localisé** ci-dessous, déjà démontré, puis un **gate de correction des moments toriques** qui décide si une correction Clay-admissible peut préserver le coût log-BMO sans créer d’interface antipodale.

## 1. Cadre commun et seuil angulaire exact

Soit `D⊂R³` de mesure finie et

\[
K=\sup_{\lambda>0}
\lambda|\{|W|>\lambda\}|^{2/3}<\infty.
\tag{1}
\]

On utilise avec sa constante exacte

\[
\int_E|W|dx\leq3K|E|^{1/3}.
\tag{2}
\]

Pour un champ poloïdal axisymétrique, posons

\[
E_{1/4}
=\left\{x\in D:
|W_r(x)|\geq\frac14|W(x)|\right\}.
\tag{3}
\]

Comme `|W|²=|W_r|²+|W_z|²`,

\[
x\in E_{1/4}
\quad\Longleftrightarrow\quad
|W_r(x)|\geq\frac1{\sqrt{15}}|W_z(x)|.
\tag{4}
\]

Le facteur `1/√15` est donc imposé par le seuil `1/4`; le remplacer par `1/4` serait une perte inutile.

## 2. Voie A — somme finie non séparable

Considérons

\[
\psi_n(r,z)
=\sum_{j=1}^{J_n}A_{n,j}(r)\chi_{n,j}(z),
\qquad
F_n=r\psi_n
=\sum_{j=1}^{J_n}f_{n,j}(r)\chi_{n,j}(z),
\tag{5}
\]

où `f_{n,j}=rA_{n,j}`. Le curl exact est

\[
W_r=-\frac1r
\sum_j f_{n,j}(r)\chi_{n,j}'(z),
\qquad
W_z=\frac1r
\sum_j f_{n,j}'(r)\chi_{n,j}(z).
\tag{6}
\]

L’identité `div W=0` est automatique par commutation de `F_{rz}` et `F_{zr}`. Toutes les possibilités de masquage sont visibles dans (6) : la dérivée verticale d’un niveau est masquée par les dérivées radiales de tous les autres niveaux.

### 2.1 Lemme terminal d’excès radial

Soit `Ω` un ensemble mesurable du demi-plan méridien et

\[
\Omega^*
=\{(r,\theta,z):(r,z)\in\Omega,\ 0\leq\theta<2\pi\}
\subset D.
\]

Définissons

\[
\begin{aligned}
\Delta_\Omega
&=\int_{\Omega^*}|W_r|dx
-\frac1{\sqrt{15}}
 \int_{\Omega^*}|W_z|dx\\
&=2\pi\int_\Omega
\left(
|F_z|-\frac1{\sqrt{15}}|F_r|
\right)drdz.
\end{aligned}
\tag{7}
\]

Alors

\[
\boxed{
|E_{1/4}\cap\Omega^*|
\geq
\left(
\frac{(\Delta_\Omega)_+}{3K}
\right)^3.}
\tag{8}
\]

#### Preuve

Sur le complément de `E_{1/4}`, (4) donne

\[
|W_r|<\frac1{\sqrt{15}}|W_z|.
\]

Par conséquent,

\[
\begin{aligned}
\int_{E_{1/4}\cap\Omega^*}|W_r|dx
&\geq
\int_{\Omega^*}|W_r|dx
-\frac1{\sqrt{15}}
 \int_{\Omega^*}|W_z|dx\\
&=\Delta_\Omega.
\end{aligned}
\]

Puis

\[
(\Delta_\Omega)_+
\leq\int_{E_{1/4}\cap\Omega^*}|W|dx
\leq3K|E_{1/4}\cap\Omega^*|^{1/3},
\]

ce qui prouve (8). Aucune séparabilité, régularité de second ordre ou hypothèse de signe n’est utilisée.

### 2.2 Version capacité

Avec la convention

\[
\operatorname{Cap}_2(E)
=\inf_{\substack{\varphi\in C_c^\infty(\mathbb R^3)\\
\varphi\geq1\text{ près de }E}}
\int_{\mathbb R^3}|\nabla\varphi|^2dx,
\tag{9}
\]

et la constante `S₃` de

\[
\|\varphi\|_6
\leq S_3\|\nabla\varphi\|_2,
\]

l’inégalité isocapacitaire donne

\[
\boxed{
\operatorname{Cap}_2(E_{1/4}\cap\Omega^*)
\geq
\frac{(\Delta_\Omega)_+}{3S_3^2K}.}
\tag{10}
\]

Cette capacité newtonienne n’est pas automatiquement la capacité logarithmique pertinente pour une extension BMO. Elle ne garantit ni une boule intérieure de rayon comparable, ni deux secteurs directionnels de densité relative uniforme.

### 2.3 Ledger d’une cascade finie

Soient `Ω₁,…,Ω_J` des régions terminales de multiplicité de recouvrement au plus `M`, et posons

\[
q_j=\int_{\Omega_j^*}|W_r|dx.
\]

Si chaque couche est totalement masquée au sens `Δ_{Ω_j}≤0`, alors

\[
\sqrt{15}\sum_{j=1}^Jq_j
\leq
\sum_{j=1}^J
\int_{\Omega_j^*}|W_z|dx
\leq M\int_D|W_z|dx
\leq3MK|D|^{1/3}.
\tag{11}
\]

Donc

\[
\boxed{
\sum_{j=1}^Jq_j
\leq\frac{3M}{\sqrt{15}}K|D|^{1/3}.}
\tag{12}
\]

Ce budget est utile seulement si les `Ω_j` sont géométriquement identifiées et si `M` est uniforme. Compter deux fois le même masque vertical invalide la deuxième inégalité de (11).

### 2.4 Pourquoi le rang fini ne ferme pas le verrou

La donnée `J_n<∞` ne contrôle aucune des quantités suivantes :

- le nombre de changements d’échelle cachés dans une seule fonction `A_{n,j}`;
- la fréquence radiale de `f_{n,j}`;
- la platitude infinie de `χ_{n,j}` au bord de son support;
- le conditionnement des familles `(f_{n,j})` et `(χ_{n,j})`;
- le reach ou la courbure des niveaux de `F_n`;
- la multiplicité `M` d’un recouvrement de régions de masquage.

Le rang n’est même pas intrinsèque : un terme peut être scindé en plusieurs termes proportionnels sans changer `F_n`. Il ne peut donc entrer seul dans une minoration géométrique canonique.

Un `F∈C_c^∞` non nul possède bien des niveaux réguliers compacts. Sur toute composante fermée d’un tel niveau, la normale atteint une direction verticale à un point de hauteur maximale; `E_{1/4}` est donc non vide et contient un ouvert. Mais la mesure et la capacité de cet ouvert peuvent tendre vers zéro sans borne sur les dérivées secondes ou le reach. Cette conclusion qualitative ne produit aucun `n^{-C}` uniforme.

### 2.5 Lemme géométrique conditionnel avec constante

Le substitut correct à « rang fini » est une hypothèse de géométrie d’un niveau de flux.

Soit `Γ={F=t}` une composante régulière simple, contenue dans `r≥r₀>0`. Supposons :

1. la courbure de `Γ` est au plus `κ`;
2. son tube normal de largeur `τ` est injectif, avec `τκ≤1/2`;
3. dans ce tube, la direction `∇F/|∇F|` s’écarte d’au plus `1/4` de la normale transportée depuis `Γ`.

Au point supérieur de `Γ`, la normale vaut `±e_z`. Sur un arc de longueur totale `1/(2κ)`, elle garde une composante verticale au moins `3/4`. Après la perte `1/4` du tube, `|F_z|/|∇F|≥1/2`, donc ce tube est inclus dans `E_{1/4}`. Le jacobien des coordonnées normales est au moins `1/2`. On obtient

\[
\boxed{
|E_{1/4}|
\geq\pi r_0\frac{\tau}{\kappa}.}
\tag{13}
\]

Cette borne est falsifiable directement sur `F_n`. Elle expose les deux seules voies de fuite : `τ→0` ou `κ→∞`. Ni (1), ni le rang de (5), ni l’énergie seuls ne les excluent.

## 3. Voie B — tube de vorticité torique

### 3.1 Construction exacte

Fixons un rayon majeur `R>0`, un rayon de cœur `0<h<R/8`, et le cercle

\[
\Gamma_R
=\{(R\cos\theta,R\sin\theta,0):0\leq\theta<2\pi\}.
\]

Dans le tube `d(x):=dist(x,Γ_R)<R/4`,

\[
d=\sqrt{(r-R)^2+z^2}.
\]

Prenons `b(s)=\bar b(s²)` avec `\bar b∈C_c^∞([0,1))`, `b>0` sur `[0,1)`, `b=1` sur `[0,1/2]`, et posons

\[
\boxed{
W_h(x)=a_h b(d(x)/h)e_\theta(x).}
\tag{14}
\]

Le support reste dans `r≥R-h>0`; le champ est donc `C_c^∞`. En coordonnées cylindriques,

\[
\operatorname{div}W_h
=\frac1r\partial_\theta(a_hb(d/h))=0.
\tag{15}
\]

L’intégrale vectorielle est nulle car

\[
\int_0^{2\pi}e_\theta(\theta)d\theta=0.
\tag{16}
\]

Ce champ est purement toroïdal :

\[
W_r=W_z=0,
\qquad
E_{1/4}=\varnothing.
\tag{17}
\]

Il ne « masque » donc pas le retour poloïdal : il change la topologie des lignes de vorticité en les fermant directement sur des cercles.

### 3.2 Volume et faible-`L^{3/2}`

Les coordonnées toriques

\[
x(\theta,\rho,\phi)
=((R+\rho\cos\phi)\cos\theta,
  (R+\rho\cos\phi)\sin\theta,
  \rho\sin\phi)
\]

ont le jacobien

\[
(R+\rho\cos\phi)\rho.
\]

En particulier,

\[
|\{d<h\}|=2\pi^2Rh^2.
\tag{18}
\]

Pour `t>0`, définissons

\[
M_b(t)=4\pi^2
\int_{\{0<s<1:b(s)>t\}}sds,
\qquad
\kappa_b=\sup_{t>0}tM_b(t)^{2/3}.
\tag{19}
\]

La fonction de distribution est exactement

\[
|\{|W_h|>\lambda\}|
=Rh^2M_b(\lambda/a_h),
\]

d’où

\[
\boxed{
K_h=a_hR^{2/3}h^{4/3}\kappa_b.}
\tag{20}
\]

Le choix

\[
a_h=\kappa_b^{-1}R^{-2/3}h^{-4/3}
\tag{21}
\]

normalise `K_h=1`. La norme forte critique est également uniforme :

\[
\|W_h\|_{3/2}^{3/2}
=4\pi^2a_h^{3/2}Rh^2
\int_0^1b(s)^{3/2}sds
=C_b.
\tag{22}
\]

En revanche,

\[
\|W_h\|_2^2
=4\pi^2a_h^2Rh^2
\int_0^1b(s)^2sds
\asymp R^{-1/3}h^{-2/3}.
\tag{23}
\]

### 3.3 Masse conique

Prenons `e=e_y` et `α=1/2`. Comme `e_θ·e_y=cosθ`, le cône occupe exactement un tiers des angles. Avec

\[
I_b=\int_0^1b(s)sds,
\]

sa masse est

\[
\boxed{
m_h=\frac{4\pi^2}{3}a_hRh^2I_b.}
\tag{24}
\]

Dans le domaine `D_R=B_{2R}(0)`, de volume `(32π/3)R³`,

\[
\frac{m_h}{K_h|D_R|^{1/3}}
=C_{b,\rm cone}
\left(\frac hR\right)^{2/3}.
\tag{25}
\]

Le quotient cubique est donc d’ordre `(h/R)²`, exactement la fraction volumique du cœur torique.

En écrivant `q=h/R`, (21) devient

\[
a_h=\kappa_b^{-1}R^{-2}q^{-4/3}.
\tag{26}
\]

Le facteur `R^{-2}` est exactement celui du scaling Navier–Stokes de la vorticité. À aspect `q` fixé, `K_h` est invariant, la masse conique est proportionnelle à `R`, et l’énergie calculée plus bas est proportionnelle à `R`, conformément au facteur `λ^{-1}` de l’énergie sous la remise à l’échelle `λ=R^{-1}`.

## 4. Extension logarithmique de la direction

Fixons

\[
h<H<R/4,
\qquad
L=\log(H/h).
\]

Sur les zéros de `W_h`, définissons l’angle

\[
\Theta(d)=
\begin{cases}
\pi/2,&0\leq d\leq h,\\
\displaystyle
\frac\pi{2L}\log\frac Hd,&h<d<H,\\
0,&d\geq H,
\end{cases}
\tag{27}
\]

et le champ unitaire

\[
\boxed{
\zeta_h
=\sin\Theta(d)e_\theta
+\cos\Theta(d)e_z.}
\tag{28}
\]

Ainsi `ζ_h=W_h/|W_h|=e_θ` sur `{W_h≠0}` et `ζ_h=e_z` hors du corridor. La fonction est continue et `W^{1,∞}` par morceaux; un lissage dans des sous-corridors multiplicatifs fixes conserve les estimations ci-dessous à constante universelle.

### 4.1 Deux identités de corridor

Dans `h<d<H`,

\[
|\Theta'(d)|=\frac\pi{2Ld}.
\tag{29}
\]

En posant `q=h/H`, une intégration exacte donne

\[
\boxed{
\int_0^H\Theta(\rho)\rho d\rho
=\frac{\pi H^2}{8L}(1-q^2).}
\tag{30}
\]

Le terme `h²/2` du cœur s’annule exactement avec le terme inférieur de l’intégrale logarithmique. L’ordre moyen du défaut dans une section de rayon `H` est donc `1/L`, pas `h²/H²`.

### 4.2 BMO sur toutes les boules : borne supérieure

Pour une boule euclidienne `B_s(x)`, deux estimations géométriques uniformes valent lorsque `H<R/4` :

\[
s\fint_{B_s(x)}
\frac{\mathbf1_{\{d<H\}}}{d}dy
\leq C_{\rm tube}
\qquad(0<s\leq H),
\tag{31}
\]

et, pour `s≥H`,

\[
\fint_{B_s(x)}
\Theta(d)\mathbf1_{\{d<H\}}dy
\leq\frac{C_{\rm tube}}L.
\tag{32}
\]

La première vient de l’intégrabilité codimension deux de `1/d` : une intersection de longueur `O(s)` le long du cercle et de rayon transverse `s` donne une intégrale `O(s²)`. La seconde suit de (30), d’une longueur d’arc interceptée `O(s)` pour `s<R/2`, puis de l’intégrale totale pour les boules macroscopiques.

Comme

\[
|\nabla\zeta_h|
\leq|\Theta'(d)|
+\frac{\sin\Theta(d)}r
\leq
\frac\pi{2Ld}\mathbf1_{\{h<d<H\}}
+\frac4{3R}\mathbf1_{\{d<H\}},
\tag{33}
\]

Poincaré sur les boules `s≤H`, puis la comparaison à la constante `e_z` pour `s≥H`, donnent

\[
\boxed{
[\zeta_h]_{\mathrm{BMO}(\mathbb R^3)}
\leq C
\left(
\frac1L+\frac HR
\right).}
\tag{34}
\]

Cette preuve traite :

- les boules contenues dans le cœur, où seule la variation azimutale `O(s/R)` subsiste;
- les boules coupant `d=h` ou `d=H`;
- les boules décentrées le long du tore;
- les boules plus grandes que le corridor, par dilution du défaut compact.

Elle ne remplace pas le suprémum continu par une grille de centres.

### 4.3 Nécessité de l’ordre logarithmique

Soit `x₀∈Γ_R`. Une boule `B_{h/4}(x₀)` voit une direction proche de `e_θ(x₀)`, alors qu’une boule de rayon comparable à `H` a une moyenne proche de `e_z` par (30). Pour `L` assez grand et `H/R` assez petit, ces deux moyennes restent séparées d’une constante universelle.

Pour deux boules concentriques `B_s⊂B_{2s}` en dimension trois,

\[
|\zeta_{B_s}-\zeta_{B_{2s}}|
\leq8[\zeta]_{\mathrm{BMO}}.
\tag{35}
\]

Une chaîne de `N≤L/log 2+4` doublements donne donc

\[
\boxed{
[\zeta_h]_{\mathrm{BMO}}
\geq\frac cL}
\tag{36}
\]

sous les conditions quantitatives précédentes. Avec `H/R≤c/L`, (34) et (36) donnent `BMO≍1/L`.

### 4.4 Semi-norme BMO logarithmique

Sur `R³`, `ζ_h` est unitaire et égal à `e_z` à l’infini; son terme `L¹` est donc infini. La quantité localisable correcte est `ζ_h-e_z`, ou une coupure spatiale de la direction. Le semi-norme BMO est inchangé par soustraction de `e_z`.

Pour les petites boules, la preuve de (34) se raffine en

\[
\operatorname{MO}_{B_s}(\zeta_h)
\leq C
\begin{cases}
\displaystyle
\frac{s}{Lh}+\frac sR,&0<s<h,\\[2mm]
\displaystyle
\frac1L+\frac sR,&h\leq s\leq H,\\[2mm]
\displaystyle
\frac{H^2}{Ls^2},&H<s<R/2,
\end{cases}
\tag{37}
\]

avec dilution supplémentaire aux échelles macroscopiques. Il s’ensuit

\[
\boxed{
\sup_{x,\,0<s<1/2}
|\log s|\,
\operatorname{MO}_{B_s(x)}(\zeta_h)
\leq C
\left(
\frac{|\log h|}{L}
+\frac{H|\log H|}{R}
+1
\right).}
\tag{38}
\]

Une famille concrète satisfaisant une borne uniforme est

\[
R_N=e^{-\beta N},
\qquad
H_N=\frac{R_N}{N},
\qquad
h_N=H_Ne^{-N},
\qquad \beta>0.
\tag{39}
\]

En effet,

\[
L_N=N,
\qquad
\frac{|\log h_N|}{L_N}
=\beta+1+o(1),
\qquad
\frac{H_N|\log H_N|}{R_N}
=\beta+o(1).
\tag{40}
\]

Le corridor torique atteint donc réellement l’échelle borderline log-BMO. La constante `C` de (34), (37)–(38) est géométrique et universelle, mais elle n’est pas numériquement optimisée dans cette passe.

## 5. Énergie et Biot–Savart du tore

Puisque `W_h` est lisse, compact, divergence-free et de moyenne nulle, son champ de vitesse décroissant est

\[
U_h=\nabla\times(-\Delta)^{-1}W_h
=\frac1{4\pi}
\int_{\mathbb R^3}
\frac{W_h(y)\times(x-y)}{|x-y|^3}dy.
\tag{41}
\]

L’identité de Fourier ou de Hodge donne

\[
\|U_h\|_2^2
=\langle W_h,(-\Delta)^{-1}W_h\rangle
=\frac1{4\pi}
\iint
\frac{W_h(x)\cdot W_h(y)}{|x-y|}dxdy.
\tag{42}
\]

Une décomposition des paires selon la distance le long de `Γ_R` donne, pour `h/R` assez petit,

\[
c_ba_h^2Rh^4\log\frac Rh
\leq
\|U_h\|_2^2
\leq
C_ba_h^2Rh^4\log\frac Rh.
\tag{43}
\]

Pour la borne supérieure, le potentiel newtonien d’une section est `O(h²)` à distance `O(h)` et `O(h²/s)` à distance longitudinale `s`; l’intégration de `h` à `R` produit le logarithme. Pour la borne inférieure, les paires d’arcs proches ont `e_θ(x)·e_θ(y)≥c>0` et produisent le même logarithme; les paires lointaines ne contribuent qu’un terme sans logarithme, absorbé lorsque `R/h` est assez grand.

Sous la normalisation (21),

\[
\boxed{
\|U_h\|_2^2
\asymp
R^{-1/3}h^{4/3}
\log\frac Rh
=R\left(\frac hR\right)^{4/3}
\log\frac Rh.}
\tag{44}
\]

L’énergie tend vers zéro quand `h/R→0` à `R` fixé. Ce fait ne donne pas à lui seul la petitesse d’une norme critique de vitesse.

### 5.2 Audit direct de la norme critique sur `T³`

La borne plus forte annoncée dans le rapport racine est valide, mais sa justification exige un lemme de potentiel tubulaire et la cancellation de moyenne dans la zone lointaine. Plaçons le tore dans une boule d’injectivité fixe de `T³`, supposons `0<h<R/8<R_*`, notons `d(x)=dist(x,Γ_R)` et choisissons le représentant périodique de vitesse de moyenne nulle.

Le noyau périodique de Biot–Savart est la somme du noyau euclidien `O(|x|^{-2})` et d’un reste lisse. Pour une amplitude maximale `A`, une paramétrisation par longueur d’arc du cercle et section transverse donne

\[
|u(x)|\leq CA
\begin{cases}
h,&d(x)\leq2h,\\
h^2/d(x),&2h<d(x)<R,\\
R^2h^2/d(x)^3,&d(x)\geq R.
\end{cases}
\tag{BS-3Z}
\]

Les deux premières lignes viennent respectivement de

\[
\int_{|y-x|\lesssim h}|x-y|^{-2}dy=O(h)
\]

et

\[
h^2\int_{-CR}^{CR}\frac{ds}{d^2+s^2}
\leq C\frac{h^2}{d}.
\]

Pour la troisième ligne, la région `R≤d≤2R` est couverte par la borne absolue `CAh²/R`. Lorsque `d≥2R`, on soustrait la valeur du noyau au centre du tore grâce à `∫_{T³}W=0`; le théorème des accroissements finis fournit `C d^{-3}` pour le noyau singulier et une dérivée bornée pour le reste périodique. Le premier moment absolu vaut `O(AR²h²)`. Puisque `d` reste borné sur le tore, le reste lisse est absorbé par `CAR²h²d^{-3}`.

Les volumes tubulaires vérifient `|{d<ρ}|≤CRρ²` pour `ρ≤R`; au-delà, une majoration sphérique `Cρ²dρ` suffit. En cubant (BS-3Z),

\[
\begin{aligned}
\|u\|_3^3
&\leq CA^3\left[
Rh^5
+Rh^6\int_h^R\rho^{-2}d\rho
+R^6h^6\int_R^1\rho^{-7}d\rho
\right]\\
&\leq CA^3(Rh^5+h^6).
\end{aligned}
\tag{BS-L3}
\]

Pour un profil fixe, `K\asymp A(Rh²)^{2/3}`. Ainsi

\[
\boxed{
\|u\|_3^3
\leq CK^3
\left(
\frac hR+\frac{h^2}{R^2}
\right).}
\tag{BS-K}
\]

La conclusion directe `\|u\|₃=O((h/R)^{1/3})` est donc rigoureuse sous les hypothèses géométriques ci-dessus. La borne adverse obtenue seulement par HLS, `L∞` et interpolation,

\[
\|u\|_3\leq C(h/R)^{1/9},
\]

est sûre mais non optimale. Il ne faut pas dégrader le rapport racine vers `1/9`; il faut y ajouter les trois justifications manquantes : potentiel d’un tube courbe, cancellation du noyau périodique lointain et intégration des trois volumes.

## 6. Compatibilité exacte avec les formulations Clay

### 6.1 Espace entier

Le champ `W_h` est une vorticité lisse compacte, mais `U_h` de (41) n’est pas de Schwartz. Son impulsion hydrodynamique

\[
I_h=\frac12\int_{\mathbb R^3}x\times W_h(x)dx
\]

a une composante axiale strictement positive :

\[
I_h\cdot e_z
=\frac12\int r|W_h|dx>0.
\tag{45}
\]

Ce moment non nul produit une queue dipolaire algébrique dans Biot–Savart. La donnée n’appartient donc pas, telle quelle, à la classe rapidement décroissante avec toutes ses dérivées de l’alternative Clay (A).

Annuler (45) exige au moins un correcteur torique de signe opposé ou une géométrie de moments compensés. Un contact direct de deux signes recrée l’interface antipodale que le corridor logarithmique cherchait à éviter. La conservation des bornes (20), (34), (BS-K) et (44) sous cette correction est ouverte.

De plus, `W_h=w^θe_θ` engendre sur `R³` une vitesse axisymétrique sans swirl. Cette sous-classe lisse est globalement régulière; le profil ne peut donc pas produire un blow-up Clay, même après relaxation de la décroissance de Schwartz.

### 6.2 Cas périodique

Si le tore et son corridor sont contenus dans une cellule et si l’on périodise `W_h`, sa moyenne sur la cellule reste nulle par (16). L’inversion périodique du curl fournit une vitesse lisse, divergence-free et périodique, à moyenne fixée arbitrairement. C’est une donnée admissible pour l’alternative Clay (B).

Cette périodisation ne conserve pas la symétrie axisymétrique globale dans le réseau cubique et modifie Biot–Savart par les images périodiques. Aux échelles `s≪1`, les estimations locales de direction restent valides; aucune conclusion dynamique ou singularité n’en découle.

### 6.3 Évolution

Les constructions (5) et (14) sont des profils statiques. Elles ne contrôlent ni

\[
\partial_tW+(U\cdot\nabla)W-(W\cdot\nabla)U-\nu\Delta W,
\]

ni la pression, ni un temps maximal, ni un critère de prolongement. Elles ne constituent donc ni une preuve de régularité, ni un blow-up admissible.

## 7. Comparaison adversariale des deux voies

| Test | Voie A : somme finie poloïdale | Voie B : tore `e_θ` |
|---|---|---|
| `div W=0` | exacte par `F_{rz}=F_{zr}` | exacte par indépendance en `θ` |
| moyenne de `W` | nulle si `F` compact | nulle par intégration de `e_θ` |
| lieu `|W_r|≥|W|/4` | contrôlé par (8) si `Δ_Ω>0` | vide |
| fermeture des lignes | retour méridien à masquer | cercles fermés sans retour axial |
| faible-`L^{3/2}` | dépend du ledger de toutes les couches | formule exacte (20), normalisable |
| BMO toutes boules | non fermé sans reach/épaisseur | `Θ(1/log(H/h))` par (34)–(36) |
| log-BMO | couche terminale potentiellement fatale | uniforme sous (38)–(40) |
| énergie | calculable si `ψ` est la vitesse | (44), petite mais vitesse non compacte |
| Clay `R³` | possible si `U=ψe_θ` est compact | échoue à Schwartz par (45) |
| Clay périodique | possible après périodisation compatible | donnée lisse admissible |
| pertinence blow-up | statique, aucune évolution | classe sans swirl régulière sur `R³` |

### Attaques décisives

1. **Quantificateur inversé.** L’existence d’un niveau régulier pour chaque `n` ne donne pas un `τ` ou un `κ` uniforme. La borne (13) est conditionnelle.
2. **Double comptage des masques.** La somme de (11) exige une multiplicité `M`; le rang `J` ne la remplace pas gratuitement.
3. **Mesure contre BMO local.** (8) donne une mesure globale. Sans boule porteuse ou densité relative, elle ne donne pas une constante BMO numérique.
4. **Rotation azimutale.** Elle coûte `H/R` dans (34); l’oublier rend la borne fausse pour un tore épais ou proche de l’axe.
5. **Toutes les boules.** La borne torique utilise Poincaré sous `H` et dilution au-dessus de `H`; une vérification limitée aux sections méridiennes est insuffisante.
6. **Terme `L¹` du bmo localisé.** Le champ unitaire `ζ_h` n’est pas intégrable sur `R³`; il faut employer `ζ_h-e_z` ou la coupure spatiale exacte du critère.
7. **Énergie contre admissibilité.** Une énergie finie, même petite, ne remplace pas la décroissance de Schwartz exigée par Clay (A).
8. **Vorticité contre vitesse.** Le champ compact prescrit est `W`, tandis que la vitesse `U` est non locale et non compacte.

## 8. Lemme minimal recommandé

### Résultat déjà démontré à enregistrer

> **Lemme d’excès radial localisé.** Soit `W=curl(ψe_θ)` axisymétrique dans un domaine fini, avec quasi-norme faible-`L^{3/2}` `K`. Pour toute région méridienne `Ω`, le défaut `Δ_Ω` de (7) implique les bornes de mesure (8) et de capacité (10). Les constantes `1/√15`, `3` et la puissance `3` sont explicites.

Ce lemme remplace toutes les formulations vagues disant qu’« un dernier niveau doit émerger ». Il suffit désormais de calculer `Δ_Ω`; si tous les défauts sont non positifs, le masquage a effectivement payé son budget axial.

### Prochain gate falsifiable

> **MOMENT-CORRECTED-TORUS-GATE.** Construire, ou réfuter, une famille `\widehat W_N∈C_c^∞(R³)` divergence-free obtenue à partir du tore (14), telle que :
> 1. tous les moments nécessaires à une vitesse de Biot–Savart de Schwartz soient annulés;
> 2. `||\widehat W_N||_{L^{3/2,∞}}` reste uniforme;
> 3. une extension unitaire de `\widehat W_N/|\widehat W_N|` garde le budget log-BMO (38) sur toutes les boules;
> 4. le correcteur ne réduit pas toute quantité critique de vitesse à zéro et ne ramène pas la donnée dans une classe globalement régulière connue.

Le premier test doit porter seulement sur l’impulsion (45). Si son annulation force une interface antipodale de capacité comparable au cœur, la voie torique est abandonnée. Si une paire de tores opposés séparés par des corridors logarithmiques conserve (20), (38), (44) et (BS-K), on passe au moment multipolaire suivant. Cette progression évite de demander d’emblée une infinité de corrections sans borne uniforme.

## 9. Décision

- **Voie A : RÉVISER.** Le lemme terminal (8) est valide, mais `J_n<∞` n’est pas une hypothèse suffisante. Toute poursuite doit fournir `Δ_Ω>0` ou les paramètres géométriques `τ,κ` de (13).
- **Voie B : CONTINUER COMME CONTRE-TEST, PAS COMME BLOW-UP.** Elle réalise rigoureusement l’échappatoire log-BMO et réfute une obstruction purement topologique. Son premier verrou est l’impulsion non nulle, puis la dynamique sans swirl.
- **Priorité :** tester une paire torique à impulsions opposées avec corridors disjoints. C’est moins coûteux et plus décisif qu’augmenter le rang de (5) sans hypothèse de conditionnement.

## 10. Statut de preuve

Les calculs (4), (7)–(8), (12), (15)–(25), (29)–(30), (41)–(42) et (45) sont exacts. Les bornes BMO (34), (37)–(38) utilisent des constantes universelles de Poincaré et de géométrie tubulaire qui ne sont pas numériquement optimisées. Les équivalences énergétiques (43)–(44) sont asymptotiques à constantes dépendant du profil fixe `b`. La borne (BS-K) est rigoureuse sous les hypothèses d’injectivité, de profil fixe et de normalisation du mode moyen énoncées dans sa preuve.

Toutes les affirmations nouvelles restent des dérivations IA internes sans revue par les pairs, validation inter-familles ou formalisation. Aucune ne doit être étiquetée `PAPER_PROOF`.
