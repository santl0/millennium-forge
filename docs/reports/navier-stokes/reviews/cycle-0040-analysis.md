# Cycle 0040 — Audit du correcteur de Bogovskii sur une couronne

**Statut :** `AI_INTERNAL_DERIVATION` — ne pas classer `PAPER_PROOF`

**Verdict :** le lemme de localisation est valide dans la classe de Sobolev,
avec des constantes uniformes en \(x_0\) et \(R\), à condition de fixer une
couronne de géométrie non dégénérée et un même opérateur linéaire de
Bogovskii borné. Il donne un champ divergence-free, égal à \(U\) dans le
cœur, et une borne critique explicite sur son curl. Il ne donne pas, à lui
seul, une sélection conservant le quotient endpoint : la première hypothèse
scientifique manquante est que le cœur capture une fraction quantitative du
numérateur faible-\(L^3\). En outre, la seule trace nulle du correcteur ne
suffit pas à conclure que le champ prolongé est \(C_c^\infty\).

## Cadre exact et conventions

Soient \(x_0\in\mathbb R^3\), \(R>0\),

\[
 D_0=B(x_0,R),\qquad D_2=B(x_0,2R),\qquad
 A_R=D_2\setminus\overline{D_0}.               \tag{1}
\]

La couronne \(A_R\) est ouverte, bornée, connexe et lisse. Elle est l'image
de la couronne fixe

\[
 A_1=B(0,2)\setminus\overline{B(0,1)}          \tag{2}
\]

par une translation et une homothétie. Fixons

\[
 U\in C_c^\infty(\mathbb R^3;\mathbb R^3),
 \qquad \operatorname{div}U=0,                 \tag{3}
\]

et un cutoff réel

\[
 \chi\in C_c^\infty(D_2),\qquad
 0\le\chi\le1,\qquad \chi=1\text{ sur }D_0,
 \qquad \|\nabla\chi\|_\infty\le C_\chi/R,   \tag{4}
\]

avec \(\operatorname{supp}\nabla\chi\subset\overline{A_R}\). Posons

\[
 f=\nabla\chi\cdot U.                           \tag{5}
\]

La quasi-norme utilisée est

\[
 \|g\|_{L^{p,\infty}(E)}
 =\sup_{t>0}t\,|\{x\in E:|g(x)|>t\}|^{1/p}.    \tag{6}
\]

Pour abréger, notons

\[
 N_E=\|\mathbf1_EU\|_{L^{3,\infty}},\qquad
 K_E=\|\mathbf1_E\operatorname{curl}U
       \|_{L^{3/2,\infty}}.                    \tag{7}
\]

## Compatibilité de moyenne : calcul exact

Comme \(\operatorname{div}U=0\),

\[
 f=\operatorname{div}(\chi U).                 \tag{8}
\]

Le support de \(f\) est contenu dans la couronne. L'intégration sur tout
l'espace donne immédiatement

\[
 \int_{A_R}f\,dx
 =\int_{\mathbb R^3}\operatorname{div}(\chi U)\,dx
 =0.                                           \tag{9}
\]

Le même fait, écrit en termes de flux, montre l'hypothèse réellement
utilisée. Sur la frontière extérieure, \(\chi=0\). Sur la frontière
intérieure, la normale sortante à la couronne est l'opposée de la normale
sortante à \(D_0\). Ainsi

\[
 \begin{aligned}
 \int_{A_R}f\,dx
 &=\int_{\partial A_R}\chi U\cdot n_{A_R}\,dS\\
 &=-\int_{\partial D_0}U\cdot n_{D_0}\,dS
 =-\int_{D_0}\operatorname{div}U\,dx=0.        \tag{10}
 \end{aligned}
\]

La compatibilité n'est donc pas une conséquence de la seule divergence
nulle **dans la couronne** : elle utilise l'absence de source dans le cœur,
ou de façon équivalente le flux nul à travers la sphère intérieure.

## Choix quantitatif de l'opérateur de Bogovskii

Il faut choisir un opérateur linéaire déterminé

\[
 \mathcal B_{A_R}:L^p_0(A_R)
 \longrightarrow W^{1,p}_0(A_R;\mathbb R^3),
 \qquad
 \operatorname{div}\mathcal B_{A_R}g=g,        \tag{11}
\]

et non une solution arbitraire de l'équation de divergence. Pour
\(1<p<\infty\), la couronne fixe admet un tel opérateur, borné avec

\[
 \|\nabla\mathcal B_{A_R}g\|_{L^p(A_R)}
 +R^{-1}\|\mathcal B_{A_R}g\|_{L^p(A_R)}
 \le C_{B,p}\|g\|_{L^p(A_R)}.                 \tag{12}
\]

La constante dépend de \(p\) et de la géométrie de \(A_1\), mais ni de
\(x_0\), ni de \(R\). En effet, si

\[
 \widetilde g(y)=g(x_0+Ry),\qquad
 \widetilde b=\mathcal B_{A_1}\widetilde g,
 \qquad b(x)=R\widetilde b((x-x_0)/R),         \tag{13}
\]

alors \(\operatorname{div}_x b=g\), tandis que

\[
 \|g\|_{L^{p,\infty}(A_R)}
 =R^{3/p}\|\widetilde g\|_{L^{p,\infty}(A_1)},
 \quad
 \|\nabla b\|_{L^{p,\infty}(A_R)}
 =R^{3/p}\|\nabla\widetilde b\|_{L^{p,\infty}(A_1)}. \tag{14}
\]

Prenons le **même** opérateur de Bogovskii aux exposants voisins
\(p_-<p<p_+\). L'interpolation réelle de ses estimations fortes donne, y
compris pour le second indice de Lorentz \(q=\infty\),

\[
 \|\nabla\mathcal B_{A_R}g\|_{L^{p,\infty}}
 +R^{-1}\|\mathcal B_{A_R}g\|_{L^{p,\infty}}
 \le C_{B,p,\infty}\|g\|_{L^{p,\infty}}.      \tag{15}
\]

Ce passage ne découle pas par densité d'une seule estimation forte à
l'exposant \(p\) : \(L^{p,\infty}\) n'a pas la propriété de densité normique
requise. Les estimations à deux exposants voisins, pour un opérateur commun,
sont le raccord correct.

Définissons désormais

\[
 b=\mathcal B_{A_R}f
\]

dans \(A_R\), puis prolongeons \(b\) par zéro hors de \(A_R\).

## Support, égalité dans le cœur et divergence

La trace nulle implique que le prolongement satisfait

\[
 b\in W^{1,p}(\mathbb R^3),\qquad
 \operatorname{supp}b\subset\overline{A_R}.    \tag{16}
\]

Posons

\[
 V=\chi U-b.                                    \tag{17}
\]

Alors

\[
 \operatorname{supp}V\subset\overline{D_2},
 \qquad V=U\quad\text{p.p. sur }D_0.           \tag{18}
\]

La trace nulle élimine tout terme de bord dans la divergence du prolongement.
Par (5), (11) et (8),

\[
 \operatorname{div}V
 =\nabla\chi\cdot U+\chi\operatorname{div}U
  -\operatorname{div}b
 =0                                             \tag{19}
\]

au sens des distributions sur \(\mathbb R^3\).

### Réserve de régularité

La conclusion (16) est une conclusion \(W^{1,p}\), pas une conclusion
\(C_c^\infty\). Une fonction peut avoir une trace nulle tout en ayant, après
prolongement par zéro, un saut de dérivée normale. Pour obtenir

\[
 V\in C_c^\infty(\mathbb R^3;\mathbb R^3),     \tag{20}
\]

il faut ajouter l'un des raccords suivants :

1. choisir \(\operatorname{supp}\nabla\chi\Subset A_R\) avec des colliers
   fixes autour des deux frontières et utiliser un opérateur de Bogovskii
   envoyant \(C_{c,0}^\infty(A_R)\) dans
   \(C_c^\infty(A_R;\mathbb R^3)\) ;
2. ou démontrer séparément que le correcteur choisi s'annule à tout ordre
   aux deux frontières.

La seule phrase « résoudre avec trace nulle » ne démontre pas (20). Elle
suffit cependant à toutes les identités distributionnelles et estimations
ci-dessous.

## Curl exact

Avec \(\omega=\operatorname{curl}U\), la règle de Leibniz donne exactement

\[
 \boxed{
 \operatorname{curl}V
 =\chi\omega+\nabla\chi\times U
  -\operatorname{curl}b.}                      \tag{21}
\]

Cette identité vaut classiquement si le raccord lisse précédent est imposé,
et dans les distributions sous les seules hypothèses \(W^{1,p}_0\). Aucun
terme surfacique n'apparaît dans \(\operatorname{curl}b\), précisément parce
que le vecteur trace de \(b\) est nul. Une condition portant seulement sur la
composante normale ne suffirait pas pour cette assertion sur le curl.

## Estimation faible-\(L^{3/2}\) avec constantes suivies

Le volume exact de la couronne est

\[
 |A_R|=\frac{4\pi}{3}(8-1)R^3
 =c_A R^3,\qquad c_A=\frac{28\pi}{3}.           \tag{22}
\]

Pour \(E\) de mesure finie et \(1\le q<p<\infty\), la convention (6) donne

\[
 \|h\|_{L^{q,\infty}(E)}
 \le |E|^{1/q-1/p}\|h\|_{L^{p,\infty}(E)}.    \tag{23}
\]

En prenant \(q=3/2\), \(p=3\), puis en utilisant (4),

\[
 \begin{aligned}
 \|f\|_{L^{3/2,\infty}(A_R)}
 &\le \frac{C_\chi}{R}
       \|U\|_{L^{3/2,\infty}(A_R)}\\
 &\le C_\chi c_A^{1/3}N_{A_R}.                \tag{24}
 \end{aligned}
\]

Avec la norme euclidienne sur le curl et la norme de Frobenius sur le
gradient,

\[
 |\operatorname{curl}b|\le\sqrt2|\nabla b|.    \tag{25}
\]

Les équations (15), (24) et (25) donnent donc

\[
 \|\operatorname{curl}b\|_{L^{3/2,\infty}}
 \le \sqrt2 C_{B,3/2,\infty}C_\chi c_A^{1/3}
       N_{A_R}.                                 \tag{26}
\]

Pour trois fonctions, la quasi-norme (6) satisfait la borne conservatrice

\[
 \|g_1+g_2+g_3\|_{L^{p,\infty}}
 \le3\sum_{j=1}^3\|g_j\|_{L^{p,\infty}},      \tag{27}
\]

obtenue en partageant le seuil en trois. En combinant (21), (24), (26) et
\(|\chi|\le1\), on obtient

\[
 \boxed{
 \|\operatorname{curl}V\|_{L^{3/2,\infty}}
 \le3\left[K_{D_2}+C_{\rm ann}N_{A_R}\right],}
                                                               \tag{28}
\]

où

\[
 C_{\rm ann}
 =C_\chi c_A^{1/3}
  \left(1+\sqrt2 C_{B,3/2,\infty}\right).      \tag{29}
\]

Toutes les constantes de (28) sont sans dimension et indépendantes de
\(x_0,R,U\). Elles dépendent du profil normalisé du cutoff, de l'exposant et
de la géométrie de la couronne de référence.

## Contrôle du numérateur

L'égalité dans le cœur donne la seule minoration automatique :

\[
 \boxed{
 \|V\|_{L^{3,\infty}(\mathbb R^3)}\ge N_{D_0}.} \tag{30}
\]

On dispose également d'une majoration. L'estimation (15) à \(p=3\) et (4)
donnent

\[
 \|b\|_{L^{3,\infty}}
 \le R C_{B,3,\infty}\|f\|_{L^{3,\infty}}
 \le C_{B,3,\infty}C_\chi N_{A_R}.             \tag{31}
\]

La version à deux termes de (27) implique

\[
 \|V\|_{L^{3,\infty}}
 \le2\left[N_{D_2}
 +C_{B,3,\infty}C_\chi N_{A_R}\right].         \tag{32}
\]

Si \(N_{D_0}>0\), le champ \(V\) est non nul. Un champ compact,
divergence-free et sans curl est nul ; son dénominateur endpoint est donc
également non nul. Les bornes (28) et (30) donnent le seul quotient local
automatique :

\[
 q(V)
 \ge\frac{N_{D_0}}
 {3\left[K_{D_2}+C_{\rm ann}N_{A_R}\right]}.
                                                               \tag{33}
\]

## Absorption globale et première hypothèse manquante

Pour le champ global de (3), la représentation de Biot--Savart et
l'inégalité de potentiel de Riesz dans les espaces de Lorentz donnent

\[
 \|U\|_{L^{3,\infty}}
 \le C_{\rm BS}
 \|\operatorname{curl}U\|_{L^{3/2,\infty}}.   \tag{34}
\]

Ainsi \(N_{A_R}\le C_{\rm BS}K_{\mathbb R^3}\) et
\(K_{D_2}\le K_{\mathbb R^3}\). L'équation (28) devient

\[
 \|\operatorname{curl}V\|_{L^{3/2,\infty}}
 \le C_{\rm loc}K_{\mathbb R^3},\qquad
 C_{\rm loc}=3(1+C_{\rm ann}C_{\rm BS}).      \tag{35}
\]

Par conséquent,

\[
 q(V)\ge
 \frac1{C_{\rm loc}}
 \frac{N_{D_0}}{\|U\|_{L^{3,\infty}}}\,q(U). \tag{36}
\]

La **première hypothèse scientifique manquante** pour déduire
\(q(V)\gtrsim q(U)\) est donc une capture quantitative du numérateur :

\[
 \boxed{
 N_{D_0}\ge\alpha\|U\|_{L^{3,\infty}}
 \quad\text{avec }\alpha>0\text{ uniforme}.}  \tag{37}
\]

Si l'objectif est plus fort et exige que le curl localisé soit contrôlé
uniquement par le curl **local** dans \(D_2\), l'absorption globale (34) est
interdite. Il faut alors aussi une hypothèse de couronne, par exemple

\[
 N_{A_R}\le\beta K_{D_2}                      \tag{38}
\]

avec \(\beta\) uniforme, ou un correcteur disposant d'une estimation locale
plus fine. L'équation (28) expose exactement ce second verrou.

## Invariance d'échelle

Sous le scaling Navier--Stokes

\[
 U_\lambda(x)=\lambda U(\lambda x),\qquad
 \omega_\lambda(x)=\lambda^2\omega(\lambda x), \tag{39}
\]

on a

\[
 \|U_\lambda\|_{L^{3,\infty}}=
 \|U\|_{L^{3,\infty}},\qquad
 \|\omega_\lambda\|_{L^{3/2,\infty}}=
 \|\omega\|_{L^{3/2,\infty}}.                \tag{40}
\]

Le terme de cutoff a amplitude \(R^{-1}U\) sur un volume \(O(R^3)\) : sa
norme faible-\(L^{3/2}\) est donc du même ordre que la norme faible-\(L^3\)
de \(U\). C'est précisément l'annulation des facteurs \(R^{-1}\) et
\(|A_R|^{1/3}\asymp R\) visible dans (24). Il n'existe aucune petite
puissance de \(R\) à exploiter.

Si la couronne a une épaisseur \(\delta R\) au lieu d'une épaisseur
comparable à \(R\), alors

\[
 \|\nabla\chi\|_\infty\gtrsim(\delta R)^{-1},
 \qquad |A|^{1/3}\asymp\delta^{1/3}R,           \tag{41}
\]

et le coût élémentaire de (24) croît au moins comme
\(\delta^{-2/3}\). La constante de Bogovskii peut elle aussi dégénérer avec
la géométrie. Une épaisseur relative minorée est donc indispensable à toute
uniformité.

## Corollaire adverse : explosion sur une couronne mince

Cette dégénérescence de Bogovskii est nécessaire, et pas seulement un défaut
d'une construction connue. Posons

\[
 A_{R,h}=\{x\in\mathbb R^3:R<|x|<R+h\},
 \qquad 0<h\le R,                               \tag{41a}
\]

et soit \(1<p<\infty\). Supposons qu'une application, linéaire ou non,
\(\mathcal T_{R,h}\) sélectionne pour tout
\(f\in L^p_0(A_{R,h})\) un champ
\(b=\mathcal T_{R,h}f\in W^{1,p}_0(A_{R,h};\mathbb R^3)\) tel que

\[
 \operatorname{div}b=f,\qquad
 \|\nabla b\|_{L^p}\le M_{R,h,p}\|f\|_{L^p}.   \tag{41b}
\]

Alors

\[
 \boxed{M_{R,h,p}\ge c_p\,\frac Rh.}            \tag{41c}
\]

Voici une preuve par inf-sup avec constantes suivies. Écrivons
\(p'=p/(p-1)\) et prenons

\[
 q(x)=\frac{x_1}{|x|}.                          \tag{41d}
\]

La symétrie donne \(\int_{A_{R,h}}q=0\). Plus précisément,

\[
 \|q\|_{L^{p'}(A_{R,h})}
 =(p'+1)^{-1/p'}|A_{R,h}|^{1/p'},\qquad
 \|\nabla q\|_{L^{p'}(A_{R,h})}
 \le\frac1R|A_{R,h}|^{1/p'}.                   \tag{41e}
\]

La distribution de \(q\) est symétrique ; par convexité, la constante zéro
minimise \(c\mapsto\|q-c\|_{L^{p'}}\). La norme de \(q\) dans le dual de
\(L^p_0\) est donc exactement la première norme de (41e).

Pour \(b\in W^{1,p}_0(A_{R,h})\), la Poincaré unidimensionnelle sur chaque
rayon, puis la comparaison \(R^2\le r^2\le4R^2\), donnent

\[
 \|b\|_{L^p(A_{R,h})}
 \le C_p h\|\partial_rb\|_{L^p(A_{R,h})}
 \le C_p h\|\nabla b\|_{L^p(A_{R,h})}.         \tag{41f}
\]

Pour tout \(f\in L^p_0\), avec \(b=\mathcal T_{R,h}f\), l'intégration par
parties et (41b), (41e), (41f) donnent

\[
 \left|\int f q\right|
 =\left|-\int b\cdot\nabla q\right|
 \le C_p(p'+1)^{1/p'}\frac hR\,
 M_{R,h,p}\|f\|_{L^p}\|q\|_{L^{p'}}.           \tag{41g}
\]

Le supremum sur \(\|f\|_{L^p}\le1\), \(f\in L^p_0\), prouve (41c). Pour
l'exposant demandé \(p=3/2\), on a \(p'=3\) et

\[
 \|q\|_{L^3} =4^{-1/3}|A_{R,h}|^{1/3},\qquad
 \|\nabla q\|_{L^3}\le R^{-1}|A_{R,h}|^{1/3};
\]

on peut donc prendre \(c_{3/2}=(C_{3/2}4^{1/3})^{-1}\) avec la constante de
Poincaré radiale de (41f).

Ce corollaire concerne la norme forte
\(L^{3/2}_0\to W^{1,3/2}_0\). Il suffit à réfuter toute famille d'inverses
forts uniformes quand \(h/R\to0\). Une minoration analogue dans les espaces
faibles demande d'écrire l'inf-sup avec le couple associé
\(L^{3/2,\infty}\)--\(L^{3,1}\) et la Poincaré-Lorentz ; elle ne doit pas
être déclarée comme conséquence formelle de (41c).

## Passe contradictoire

### 1. Trou topologique de la couronne

Le trou d'une couronne sphérique ne crée pas de condition supplémentaire
pour l'équation scalaire \(\operatorname{div}b=f\) avec trace vectorielle
nulle. Sur un domaine lipschitzien **connexe**, l'unique compatibilité est
\(\int f=0\). Il ne faut pas confondre ce fait avec les obstructions
cohomologiques rencontrées pour d'autres complexes différentiels.

En revanche, si « couronne » désigne une union disjointe
\(A=A_1\cup A_2\), la moyenne totale n'est pas suffisante. Une solution à
trace nulle impose

\[
 \int_{A_1}f=\int_{A_2}f=0.                   \tag{42}
\]

Deux moyennes non nulles opposées donnent un contre-exemple immédiat. La
connexité, ou les compatibilités composante par composante, doit être écrite.

### 2. Flux non nul caché dans le cœur

Sur \(1<|x|<2\), le champ

\[
 U(x)=\frac{x}{|x|^3}                           \tag{43}
\]

est lisse et divergence-free localement, mais son flux à travers toute
sphère centrée vaut \(4\pi\). Pour un cutoff radial décroissant de \(1\) à
\(0\),

\[
 \int_A\nabla\chi\cdot U\,dx
 =4\pi\int_1^2\chi'(r)\,dr=-4\pi.             \tag{44}
\]

Aucun \(b\in W^{1,p}_0(A)\) ne peut alors avoir cette divergence. Ce champ
n'appartient pas à (3), car il cache une source dans le cœur ; il prouve que
l'hypothèse globale de divergence nulle ne peut être remplacée sans contrôle
du flux.

### 3. Non-unicité du correcteur

Si \(b\) résout \(\operatorname{div}b=f\), alors \(b+c\) le résout aussi pour
tout \(c\in C_c^\infty(A_R)\) divergence-free. En choisissant \(c\) très
oscillant, on rend \(\|\operatorname{curl}(b+c)\|_{L^{3/2,\infty}}\)
arbitrairement grand. Les estimations (26)--(35) portent sur la sortie d'un
opérateur borné fixé, pas sur « une solution » quelconque.

### 4. Endpoint de Lorentz

Le second indice \(q=\infty\) dans \(L^{3/2,q}\) n'est pas un endpoint
interdit pour Bogovskii : (15) l'obtient par interpolation entre deux
exposants principaux strictement compris entre \(1\) et \(\infty\). Ce qui
serait invalide est un argument de densité à partir du seul espace
\(L^{3/2}\), ou une extrapolation jusqu'à l'exposant principal \(p=1\).

Si « \(q=\infty\) » désigne plutôt le quotient

\[
 q(U)=\frac{\|U\|_{L^{3,\infty}}}
 {\|\operatorname{curl}U\|_{L^{3/2,\infty}}}, \tag{45}
\]

ce cas n'existe pas pour un champ non nul satisfaisant (3). Curl nul et
divergence nulle impliquent \(\Delta U=0\), puis la compacité impose \(U=0\).
Le quotient du champ nul est \(0/0\), donc indéfini, et non infini. La borne
(34) fournit en outre une majoration universelle de (45).

### 5. Numérateur absent du cœur

Soit \(W\in C_c^\infty(\mathbb R^3;\mathbb R^3)\) non nul et
divergence-free. Une translation suffisamment grande

\[
 U_a(x)=W(x-a)                                  \tag{46}
\]

a son support disjoint de \(D_2\). Elle conserve toutes les quasi-normes et
son quotient. Pourtant \(f=0\), le Bogovskii linéaire donne \(b=0\), et

\[
 V=0.                                           \tag{47}
\]

Aucune minoration uniforme du numérateur localisé, ni aucun quotient local
positif, ne peut donc résulter du seul choix arbitraire de la boule. Une
sélection préalable de \(x_0,R\) réalisant (37) est indispensable.

### 6. Support et lissité

Le prolongement par zéro d'un élément de \(W^{1,p}_0(A_R)\) reste dans
\(W^{1,p}(\mathbb R^3)\) et ne produit pas de mesure de bord au premier ordre.
Cela prouve (18), (19) et (21). Cela ne contrôle pas les dérivées d'ordre
deux et supérieur. Toute utilisation ultérieure exigeant une donnée
classique \(C_c^\infty\) doit insérer le raccord indiqué après (20), ou
procéder par approximation avec constantes uniformes et passage à la limite.

### 7. Pression et dynamique

Le lemme est statique. Il ne localise pas une solution de Navier--Stokes :
la multiplication par \(\chi\) et le correcteur modifient le terme non
linéaire, la diffusion et la pression non locale. Aucune conclusion sur une
solution forte, faible adaptée ou de Leray--Hopf ne découle de (17) sans un
lemme dynamique distinct.

## Verdict final

La partie démontrée est

\[
 \boxed{
 \begin{gathered}
 \operatorname{div}V=0,\qquad
 \operatorname{supp}V\subset\overline{B(x_0,2R)},\qquad
 V=U\text{ sur }B(x_0,R),\\
 \|\operatorname{curl}V\|_{L^{3/2,\infty}}
 \le3\left[K_{D_2}+C_{\rm ann}N_{A_R}\right].
 \end{gathered}}                                \tag{48}
\]

Elle est `VALIDER_COMME_DÉRIVATION_INTERNE` dans \(W^{1,p}\). La version
\(C_c^\infty\) est `À_COMPLÉTER` tant que le cutoff à colliers et
l'opérateur préservant le support lisse ne sont pas fixés explicitement.
Toute conclusion de conservation du quotient est `NON_DÉMONTRÉE` sans la
capture du numérateur (37), et, pour une conclusion purement locale, sans le
contrôle de couronne (38).

Le prochain test décisif consiste à partir d'un quasi-maximiseur de la norme
faible-\(L^3\), à sélectionner une boule vérifiant (37), puis à rechercher
parmi un nombre borné de couronnes dyadiques une couronne satisfaisant (38)
avec constantes explicites. Un échec uniforme de cette sélection établirait
que la localisation de Bogovskii ne peut remplacer la structure signée des
superniveaux.
