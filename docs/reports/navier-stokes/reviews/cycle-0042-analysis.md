# Cycle 0042 — Équation exacte de la localisation solénoïdale mobile

**Statut :** AI_INTERNAL_DERIVATION — ne pas classer PAPER_PROOF.

**Verdict :** l'équation forcée peut être écrite exactement, mais la formule
naïve
\[
 \partial_t\mathcal B_R g=\mathcal B_R(\partial_tg)
\]
est fausse lorsque \(R=R(t)\). Deux termes de dilatation apparaissent, dont
un commutateur avec l'opérateur de Bogovskii unité. Après correction,
\(V\) reste divergence-free, compact et égal à \(u\) dans le cœur, mais la
seule borne Type I
\(L^\infty_tL^{3,\infty}_x\) ne donne pas une borne uniforme de la force
dans \(L^{1,\infty}_x\), \(L^{5/3}_{x,t}\), ni dans une autre classe positive
capable de contrôler les dérivées. Une formulation critique en espace
négatif est plausible après réorganisation en divergences, mais requiert des
estimations de commutateurs de Bogovskii qui ne découlent pas du lemme
statique. La localisation mobile ne ferme donc pas le raccord dynamique.

## 1. Cadre exact

On considère, sur \(\mathbb R^3\times(0,T^*)\),

\[
 \partial_tu-\Delta u+(u\cdot\nabla)u+\nabla p=0,
 \qquad \nabla\cdot u=0,                         \tag{1}
\]

sans force extérieure et avec viscosité un. Le centre \(x^*\in\mathbb R^3\)
est fixe. Posons

\[
 \tau=T^*-t,\qquad R(t)=c\sqrt{\tau},\qquad c>0. \tag{2}
\]

Alors

\[
 R'(t)=-\frac{c}{2\sqrt{\tau}}
       =-\frac{c^2}{2R(t)},\qquad
 a(t):=\frac{R'}R=-\frac1{2\tau}
                   =-\frac{c^2}{2R^2}.          \tag{3}
\]

Soit la couronne unité

\[
 A=\{y\in\mathbb R^3:1<|y|<2\}.                 \tag{4}
\]

On fixe une fois pour toutes
\(\chi\in C_c^\infty(B(0,2))\), \(0\le\chi\le1\),
\(\chi=1\) sur un voisinage de \(\overline{B(0,1)}\), avec

\[
 \operatorname{supp}\nabla\chi\Subset A.        \tag{5}
\]

Les colliers dans (5) permettent d'éviter des problèmes de support lors de
la différentiation du domaine mobile. On définit

\[
 y=\frac{x-x^*}{R(t)},\qquad
 \chi_R(x)=\chi(y),\qquad
 A_R=x^*+RA.                                    \tag{6}
\]

Pour les calculs classiques, on suppose \(u,p\) lisses dans un voisinage du
support mobile pour tout \(t<T^*\). Pour une solution dont \(T^*\) est le
premier temps singulier, cette régularité est disponible à chaque temps
strictement antérieur à \(T^*\). Les identités peuvent ensuite être lues
distributionnellement sous les intégrabilités précisées plus bas.

## 2. Opérateur de Bogovskii conjugué

Fixons un opérateur linéaire

\[
 \mathcal B:L^q_0(A)\longrightarrow
 W^{1,q}_0(A;\mathbb R^3),\qquad
 \nabla_y\cdot\mathcal Bh=h,                    \tag{7}
\]

construit sur la couronne unité. Le même opérateur doit être utilisé à tous
les temps ; sinon sa dérivée temporelle n'est pas définie.

Pour une fonction scalaire \(g\) sur \(A_R\), posons

\[
 g^\sharp(y)=g(x^*+Ry).                         \tag{8}
\]

L'opérateur transporté est

\[
 \boxed{
 (\mathcal B_Rg)(x)
 =R\,[\mathcal B(g^\sharp)]
       \left(\frac{x-x^*}{R}\right).}            \tag{9}
\]

On vérifie directement

\[
 \nabla_x\cdot\mathcal B_Rg=g.                  \tag{10}
\]

Pour \(1<q<\infty\), et par interpolation pour les indices de Lorentz
admissibles,

\[
 \|\nabla\mathcal B_Rg\|_{L^{q,s}(A_R)}
 +R^{-1}\|\mathcal B_Rg\|_{L^{q,s}(A_R)}
 \le C_{B,q,s}\|g\|_{L^{q,s}(A_R)},             \tag{11}
\]

avec une constante indépendante de \(R,x^*\).

Définissons

\[
 g(t,x)=\nabla\chi_R(x)\cdot u(t,x),\qquad
 b(t)=\mathcal B_{R(t)}g(t).                    \tag{12}
\]

La compatibilité est exacte :

\[
 \int_{A_R}g\,dx
 =\int_{\mathbb R^3}\nabla\chi_R\cdot u\,dx
 =\int_{\mathbb R^3}\nabla\cdot(\chi_Ru)\,dx=0. \tag{13}
\]

Le correcteur est donc défini.

## 3. Support, cœur et divergence

Posons

\[
 V=\chi_Ru-b.                                    \tag{14}
\]

Après prolongement de \(b\) par zéro,

\[
 \operatorname{supp}b\subset\overline{A_R},
 \qquad
 \operatorname{supp}V\subset\overline{B(x^*,2R)}, \tag{15}
\]

et

\[
 V=u\quad\text{sur }B(x^*,R).                  \tag{16}
\]

Enfin,

\[
 \nabla\cdot V
 =\nabla\chi_R\cdot u-\nabla\cdot b=0.          \tag{17}
\]

Avec le seul codomaine \(W^{1,q}_0(A)\), (15)--(17) sont des assertions de
Sobolev et de distributions. Pour avoir
\(V\in C_c^\infty\), il faut choisir un opérateur envoyant les données
lisses à support compact dans \(A\) vers
\(C_c^\infty(A;\mathbb R^3)\), ou prouver un raccord lisse à tout ordre.

## 4. Dérivée temporelle exacte de \(\mathcal B_R\)

Introduisons le générateur de dilatation

\[
 D=y\cdot\nabla_y.                               \tag{18}
\]

Si \(\widetilde g(t,y)=g(t,x^*+R(t)y)\), alors

\[
 \partial_t\widetilde g
 =(\partial_tg)^\sharp+aD\widetilde g.          \tag{19}
\]

Par ailleurs, pour une fonction \(\widetilde h(t,y)\),

\[
 \partial_t\left[
 \widetilde h\left(t,\frac{x-x^*}{R(t)}\right)
 \right]
 =\left[\partial_t\widetilde h-aD\widetilde h\right](t,y).
                                                               \tag{20}
\]

En différentiant (9) à \(x\) fixé et en utilisant la linéarité de
\(\mathcal B\), on obtient

\[
 \begin{aligned}
 \partial_t(\mathcal B_Rg)
 &=\mathcal B_R(\partial_tg)\\
 &\quad
 +a\left\{
 \mathcal B_Rg
 +R\left[
  \mathcal B(Dg^\sharp)-D\mathcal B(g^\sharp)
 \right]^\flat_R
 \right\},                                      \tag{21}
 \end{aligned}
\]

où

\[
 h^\flat_R(x)=h((x-x^*)/R).                     \tag{22}
\]

Avec le commutateur

\[
 [\mathcal B,D]=\mathcal BD-D\mathcal B
\]

et

\[
 \mathcal C_Rg
 :=\mathcal B_Rg+
 R\bigl([\mathcal B,D]g^\sharp\bigr)^\flat_R,   \tag{23}
\]

la formule exacte est

\[
 \boxed{
 \partial_t(\mathcal B_{R(t)}g(t))
 =\mathcal B_R(\partial_tg)
 +\frac{R'}R\,\mathcal C_Rg.}                   \tag{24}
\]

Pour le rayon (2),

\[
 \boxed{
 \partial_tb
 =\mathcal B_R(\partial_tg)
 -\frac1{2\tau}\mathcal C_Rg.}                  \tag{25}
\]

La formule souvent écrite
\(\partial_tb=\mathcal B_R(\nabla\chi_R\cdot\partial_tu)\)
omet à la fois la dérivée du cutoff et les deux contributions de dilatation
dans (25).

Pour que \(\mathcal B(Dg^\sharp)\) soit licite, il faut sa moyenne nulle. Sous
le collar (5),

\[
 \int_A Dg^\sharp\,dy
 =-3\int_Ag^\sharp\,dy=0,                       \tag{26}
\]

car le terme de bord est nul. Sans support intérieur ou condition de trace
appropriée, un terme de bord doit être ajouté.

## 5. Dérivée exacte du défaut de divergence

Posons

\[
 Z(y)=D\chi(y),\qquad
 Z_R(x)=Z((x-x^*)/R).                           \tag{27}
\]

Les dérivées du cutoff sont

\[
 \partial_t\chi_R=-aZ_R
 =\frac1{2\tau}Z_R,                             \tag{28}
\]

et

\[
 \partial_t\nabla\chi_R=-a\nabla Z_R
 =\frac1{2\tau}\nabla Z_R.                     \tag{29}
\]

Par conséquent,

\[
 \boxed{
 \partial_tg
 =-a\,\nabla Z_R\cdot u
 +\nabla\chi_R\cdot\partial_tu.}                \tag{30}
\]

En remplaçant \(\partial_tu\) par (1),

\[
 \boxed{
 \partial_tg
 =\frac1{2\tau}\nabla Z_R\cdot u
 +\nabla\chi_R\cdot
  \bigl(\Delta u-(u\cdot\nabla)u-\nabla p\bigr).} \tag{31}
\]

Les équations (25) et (31) sont la forme développée de la dérivée du
correcteur. Elles montrent immédiatement que la borne statique de
\(\mathcal B_R\) ne contrôle pas \(\partial_tb\) depuis la seule norme de
vitesse.

La dérivée spatiale seconde du correcteur est, exactement,

\[
 \Delta_x(\mathcal B_Rg)
 =R^{-1}
 \left[\Delta_y\mathcal B(g^\sharp)\right]^\flat_R. \tag{32}
\]

Cette formule n'autorise pas à commuter \(\Delta_y\) avec
\(\mathcal B\).

## 6. Équation forcée exacte

Écrivons \(L=\partial_t-\Delta\). La règle du produit donne

\[
 L(\chi_Ru)
 =\chi_RLu+
  (\partial_t\chi_R-\Delta\chi_R)u
  -2(\nabla\chi_R\cdot\nabla)u.                 \tag{33}
\]

Par (1),

\[
 Lu=-(u\cdot\nabla)u-\nabla p.                 \tag{34}
\]

Choisissons la pression localisée

\[
 P=\chi_Rp.                                     \tag{35}
\]

Alors

\[
 \boxed{
 (\partial_t-\Delta)V+(V\cdot\nabla)V+\nabla P=F,} \tag{36}
\]

avec

\[
 \boxed{
 \begin{aligned}
 F={}&(\partial_t\chi_R-\Delta\chi_R)u
 -2(\nabla\chi_R\cdot\nabla)u
 +p\nabla\chi_R\\
 &-\partial_tb+\Delta b
 +(V\cdot\nabla)V-\chi_R(u\cdot\nabla)u.
 \end{aligned}}                                 \tag{37}
\]

En injectant (25),

\[
 \boxed{
 \begin{aligned}
 F={}&(\partial_t\chi_R-\Delta\chi_R)u
 -2(\nabla\chi_R\cdot\nabla)u
 +p\nabla\chi_R\\
 &-\mathcal B_R(\partial_tg)
 +\frac1{2\tau}\mathcal C_Rg
 +\Delta b\\
 &+(V\cdot\nabla)V-\chi_R(u\cdot\nabla)u,
 \end{aligned}}                                 \tag{38}
\]

où \(\partial_tg\) est donné exactement par (31).

### Développement du défaut non linéaire

Comme \(V=\chi_Ru-b\),

\[
 \boxed{
 \begin{aligned}
 &(V\cdot\nabla)V-\chi_R(u\cdot\nabla)u\\
 &={}\chi_R(\chi_R-1)(u\cdot\nabla)u
 +\chi_R(u\cdot\nabla\chi_R)u\\
 &\quad-\chi_R(u\cdot\nabla)b
 -(b\cdot\nabla\chi_R)u
 -\chi_R(b\cdot\nabla)u
 +(b\cdot\nabla)b.
 \end{aligned}}                                 \tag{39}
\]

Chaque terme de (39) est supporté dans la couronne de transition : les
facteurs \(\chi_R(\chi_R-1)\) et \(\nabla\chi_R\) y sont supportés, et \(b\)
y est supporté.

Le choix (35) rend aussi le terme de pression annulaire. Il dépend toutefois
de la jauge \(p\mapsto p+c(t)\) : le changement ajoute
\(c(t)\nabla\chi_R\) à \(F\) et \(\nabla(\chi_Rc(t))\) à la pression.
Toute estimation de \(p\nabla\chi_R\) doit fixer la pression, par exemple

\[
 p=\mathcal R_i\mathcal R_j(u_iu_j)             \tag{40}
\]

sur \(\mathbb R^3\), ou soustraire une constante temporelle locale.

## 7. Forme opératorielle et commutateurs cachés

Définissons l'opérateur de localisation solénoïdale

\[
 \mathcal T_Rw
 =\chi_Rw-\mathcal B_R(\nabla\chi_R\cdot w).    \tag{41}
\]

Alors \(V=\mathcal T_Ru\). Pour une entrée divergence-free,
\(\mathcal T_R\) est d'ordre spatial zéro au sens du scaling, mais il ne
commute ni avec \(\partial_t\), ni avec \(\Delta\), ni avec le terme
quadratique :

\[
 \begin{aligned}
 (\partial_t-\Delta)\mathcal T_Ru
 ={}&\mathcal T_R(\partial_t-\Delta)u
 +(\partial_t\mathcal T_R)u
 -[\Delta,\mathcal T_R]u.                      \tag{42}
 \end{aligned}
\]

La formule (24) est la partie exacte de
\((\partial_t\mathcal T_R)u\). La différence
\[
 (V\cdot\nabla)V-\mathcal T_R((u\cdot\nabla)u)
\]
est un autre commutateur, distinct de (39). Remplacer tous ces termes par
« erreurs de cutoff » sans préciser les opérateurs et leurs normes cache le
verrou principal.

## 8. Scaling normalisé

À un temps fixé, posons

\[
 U(y)=Ru(x^*+Ry,t),\qquad
 \Pi(y)=R^2p(x^*+Ry,t).                         \tag{43}
\]

Alors

\[
 g^\sharp(y)=R^{-2}G(y),\qquad
 G=\nabla\chi\cdot U.                           \tag{44}
\]

Par (9),

\[
 b(x,t)=R^{-1}\beta(y),\qquad
 \beta=\mathcal BG.                             \tag{45}
\]

Ainsi

\[
 V(x,t)=R^{-1}\mathcal V(y),\qquad
 \mathcal V=\chi U-\beta,                       \tag{46}
\]

et

\[
 P(x,t)=R^{-2}\chi(y)\Pi(y).                   \tag{47}
\]

Tous les termes de (38) ont la forme

\[
 F(x,t)=R^{-3}\mathcal F_t(y).                 \tag{48}
\]

Pour les termes mobiles, cela utilise l'identité sans dimension

\[
 R R'=-\frac{c^2}{2}.                           \tag{49}
\]

Les normes spatiales critiques naturelles sont donc

\[
 \|F(t)\|_{L^{1,\infty}_x},\qquad
 \|F(t)\|_{\dot W^{-1,(3/2,\infty)}_x},         \tag{50}
\]

ou, après écriture \(F=f_0+\nabla\cdot G_0\),

\[
 \|f_0(t)\|_{L^{1,\infty}_x}
 +\|G_0(t)\|_{L^{3/2,\infty}_x}.               \tag{51}
\]

Une norme parabolique critique possible est

\[
 \|F\|_{L^{5/3}_{x,t}(Q_R)},                   \tag{52}
\]

ou ses variantes de Lorentz, puisque la mesure parabolique a dimension cinq.
Le fait qu'une norme soit critique par dimension ne prouve pas qu'elle soit
finie ou uniformément bornée.

## 9. Ce que fournit réellement la borne Type I

Supposons

\[
 \sup_{0<t<T^*}\|u(t)\|_{L^{3,\infty}}\le M.   \tag{53}
\]

Les estimations statiques de Bogovskii donnent

\[
 \|b(t)\|_{L^{3,\infty}}
 +\|\nabla b(t)\|_{L^{3/2,\infty}}
 \le C_{\chi,B}M,                              \tag{54}
\]

et donc

\[
 \|V(t)\|_{L^{3,\infty}}\le C_{\chi,B}M.       \tag{55}
\]

Avec la normalisation globale (40), Hunt et Calderón–Zygmund donnent

\[
 \|p(t)\|_{L^{3/2,\infty}}
 \le C M^2.                                    \tag{56}
\]

Les facteurs de volume de la couronne annulent exactement les puissances de
\(R\). Par exemple,

\[
 \|(\partial_t\chi_R)u\|_{L^{1,\infty}}
 +\|(\Delta\chi_R)u\|_{L^{1,\infty}}
 \le C_{\chi,c}M,                              \tag{57}
\]

et

\[
 \|p\nabla\chi_R\|_{L^{1,\infty}}
 \le C_\chi M^2.                               \tag{58}
\]

De même, la partie purement géométrique
\((2\tau)^{-1}\mathcal C_Rg\) de (38) a la bonne échelle pour être
uniforme dans \(L^{1,\infty}\), à condition que
\([\mathcal B,D]\) soit borné sur le Lorentz utilisé.

En revanche, (53) ne contrôle directement aucun des termes

\[
 (\nabla\chi_R\cdot\nabla)u,\qquad
 \mathcal B_R(\nabla\chi_R\cdot\Delta u),\qquad
 \mathcal B_R(\nabla\chi_R\cdot\nabla p),       \tag{59}
\]

ni les dérivées présentes dans (39). Les évaluer séparément dans
\(L^{1,\infty}\) requiert au moins des bornes sur
\(\nabla u,\Delta u,\nabla p\).

On peut tenter de combiner les termes de (59) en commutateurs et d'intégrer
les dérivées par parties. Une borne du type

\[
 \|F(t)\|_{\dot W^{-1,(3/2,\infty)}}
 \le C(M+M^2)                                  \tag{60}
\]

est compatible avec le scaling, mais elle exige :

1. une extension de \(\mathcal B\) aux espaces de Sobolev négatifs de
   Lorentz ;
2. des bornes uniformes pour
   \([\Delta,\mathcal T_R]\) et
   \([\mathcal B,D]\) ;
3. un traitement de la pression modulo constantes ;
4. une définition distributionnelle de la dérivée de l'opérateur mobile.

Aucune de ces quatre estimations ne découle de la seule borne statique (11).
Même démontrée, (60) serait une borne dans un espace négatif ; elle ne
fournirait ni compacité forte ni régularité de \(V\).

## 10. Test adverse haute fréquence

Le défaut d'une estimation positive depuis la seule norme de vitesse est
visible avant tout scénario de blow-up. Prenons un cutoff radial \(\chi\) et
une couronne compacte évitant l'axe cylindrique. Soit

\[
 u_N(r,\theta,z)
 =\varepsilon\,\phi(r,z)\sin(Nz)e_\theta,       \tag{61}
\]

où \(\phi\in C_c^\infty(A)\) est axisymétrique et non nulle dans une région
où la dérivée radiale sphérique de \(\chi\) et \(z\) sont non nuls.

Chaque \(u_N\) est lisse, compact et divergence-free. Comme \(e_\theta\) est
tangent aux sphères,

\[
 \nabla\chi\cdot u_N=0,\qquad b_N=0,            \tag{62}
\]

et

\[
 \|u_N\|_{L^{3,\infty}}\le C_\phi\varepsilon   \tag{63}
\]

uniformément en \(N\). Pourtant, sur un sous-ensemble de volume fixe,

\[
 |(\nabla\chi\cdot\nabla)u_N|
 \ge c_{\chi,\phi}\varepsilon N               \tag{64}
\]

pour une fraction uniforme des oscillations. Sa norme
\(L^{1,\infty}\) croît donc comme \(N\).

Ces champs peuvent servir de données initiales à des solutions fortes locales.
À l'instant initial, la partie linéaire de la diffusion préserve la direction
azimutale, tandis que les contributions non linéaires sont d'ordre
\(\varepsilon^2\). Pour \(\varepsilon\) fixé assez petit, le commutateur
linéaire de cutoff détecté par (64) ne peut être estimé par une fonction de
la seule borne (63) au moyen d'une estimation terme à terme.

Ce test ne construit pas un blow-up Type I et ne réfute pas un éventuel
théorème exploitant toute la dynamique présingulière. Il réfute précisément
l'affirmation fonctionnelle suivante :

> une borne \(L^{3,\infty}\) de la vitesse suffit, par les estimations
> statiques de cutoff et de Bogovskii, à borner chaque terme de la force
> mobile dans \(L^{1,\infty}\).

Un falsificateur du test devrait démontrer une cancellation opératorielle
exacte du terme principal \(O(N)\) dans la somme complète (38), pour
l'opérateur \(\mathcal B\) fixé. Une telle cancellation n'est contenue ni
dans \(\nabla\cdot b=g\), ni dans les estimations (11).

## 11. Passe contradictoire complète

1. **Moyenne nulle.** Elle résulte de la divergence globale de \(u\), mais
   doit être revérifiée après chaque différentiation ; (26) utilise les
   colliers.
2. **Opérateur non fixé.** Ajouter à \(b\) un champ divergence-free dépendant
   du temps change arbitrairement \(\partial_tb\). La conjugaison (9) est
   indispensable.
3. **Domaine mobile oublié.** Même avec \(g\) indépendant du temps,
   \(\partial_t\mathcal B_Rg\ne0\). Le commutateur (23) subsiste.
4. **Mauvais signe de \(R'\).** Lorsque \(t\uparrow T^*\), \(R'<0\), mais
   \(\partial_t\chi_R=(2\tau)^{-1}D\chi_R\).
5. **Laplacien commuté illicitement.**
   \(\Delta\mathcal B_Rg\ne\mathcal B_R\Delta g\) en général.
6. **Non-linéarité.** \(\mathcal T_R((u\cdot\nabla)u)\) n'est pas
   \((V\cdot\nabla)V\). Les six termes de (39) restent.
7. **Pression.** Elle est non locale et définie modulo une fonction du temps.
   La jauge doit accompagner le choix de \(P\).
8. **Support temporel.** La trace nulle suffit au prolongement \(W^{1,q}\),
   pas à une identité classique à tout ordre sur une frontière mobile.
9. **Endpoint Lorentz.** Les estimations de \(\mathcal B\) et de ses
   commutateurs à second indice infini doivent être obtenues par un même
   opérateur et interpolation, pas par densité.
10. **Scaling pris pour une estimation.** Le fait que (50)--(52) soient
    critiques n'implique pas leur bornitude.
11. **Circularité.** Contrôler les dérivées de \(u\) dans (59) par un
    théorème de lissage présingulier peut déjà utiliser la localisation ou
    la régularité que l'équation de \(V\) devait établir.
12. **Temps terminal.** \(R(t)\to0\) et \(R'(t)\to-\infty\). Les formules
    valent pour \(t<T^*\), sans passage automatique à \(T^*\).
13. **Solution localisée.** \(V\) résout (36), pas Navier–Stokes non forcé.
    Aucune superposition ou unicité ne permet de supprimer \(F\).
14. **Type I.** La borne (53) porte sur \(u\), pas sur
    \(\partial_tu,\nabla u,\omega\) ou \(F\).

## 12. Verdict falsifiable

Les formules (24), (31), (38) et (39) sont les identités exactes à tester.
En particulier, tout calcul omettant

\[
 -\frac1{2\tau}
 \left[
 b+R\bigl([\mathcal B,D]g^\sharp\bigr)^\flat_R
 \right]                                       \tag{65}
\]

dans \(\partial_tb\) est faux.

La conclusion positive démontrée depuis la seule borne Type I est

\[
 \sup_{t<T^*}\|V(t)\|_{L^{3,\infty}}
 \le C_{\chi,B}M,                              \tag{66}
\]

ainsi que les bornes d'ordre zéro (56)--(58). La conclusion

\[
 \sup_{t<T^*}\|F(t)\|_{L^{1,\infty}}<\infty    \tag{67}
\]

n'est pas démontrée et est incompatible avec les estimations terme à terme,
comme le montre (61)--(64). Une borne critique négative telle que (60) reste
un lemme séparé à formuler et prouver ; elle ne doit pas être enregistrée
comme conséquence de Barker–Prange ou de Bogovskii.

La prochaine expérience décisive est de fixer une formule intégrale précise
pour \(\mathcal B\) sur \(A\), puis de calculer le symbole principal du
commutateur complet

\[
 [\Delta,\mathcal T_R]u-(\partial_t\mathcal T_R)u
\]

sur la famille pure-swirl (61). Si le terme \(O(N)\) survit dans une norme
critique, (67) est réfutée constructivement. S'il s'annule, cette cancellation
doit être convertie en une estimation uniforme de
\(\dot W^{-1,(3/2,\infty)}\), avec constantes et dépendance en \(c\)
explicitement suivies.
