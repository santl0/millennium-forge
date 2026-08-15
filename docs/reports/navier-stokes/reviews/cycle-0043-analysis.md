# Cycle 0043 — Commutateur unité du cutoff solénoïdal

**Statut :** AI_INTERNAL_DERIVATION — ne pas classer PAPER_PROOF.

**Verdict :** les identités algébriques du commutateur sont exactes et le
test pure-swirl montre que la croissance ponctuelle \(O(N)\) disparaît dans
la classe négative critique
\[
 L^{1,\infty}+\operatorname{div}L^{3/2,\infty}.
\]
Pour un champ général, une représentation uniforme de cette forme suit si
la réalisation fixée de Bogovskii possède une échelle négative quantitative,
en particulier
\[
 \mathcal B:W^{-1,p}\to L^p,\qquad
 \mathcal B:W^{-2,p}\to W^{-1,p},
\]
ou directement
\[
 [\Delta,\mathcal B]:L^p\to W^{-1,p}.
\]
La première extension seule ne contrôle pas le commutateur laplacien. Le
résultat général est donc conditionnel à ce lemme opératoriel ; la seule
propriété « support-lisse » sur \(C_c^\infty\) ne fournit pas ses constantes.
En revanche, une borne uniforme \(L^{1,\infty}\) du commutateur est fausse,
déjà sur la famille pure-swirl.

## 1. Cadre et conventions

Soit

\[
 A=\{y\in\mathbb R^3:1<|y|<2\},                 \tag{1}
\]

et soit

\[
 \chi\in C_c^\infty(B(0,2)),\qquad
 0\le\chi\le1,\qquad
 \chi=1\text{ près de }\overline{B(0,1)},       \tag{2}
\]

avec

\[
 \operatorname{supp}\nabla\chi\Subset A.        \tag{3}
\]

On fixe une réalisation linéaire, support-lisse, de l'inverse de divergence

\[
 \mathcal B:C^\infty_{c,0}(A)
 \longrightarrow C_c^\infty(A;\mathbb R^3),
 \qquad \nabla\cdot\mathcal Bh=h.               \tag{4}
\]

L'indice zéro signifie moyenne nulle. Soit

\[
 D=y\cdot\nabla.                                 \tag{5}
\]

Le rapport principal emploie la convention
\(D_{\rm src}=I+y\cdot\nabla\). Cela ne change pas le commutateur étudié,
car \([D_{\rm src},Q]=[D,Q]\). Dans toutes les règles de produit ci-dessous,
\(D\) désigne donc la partie dérivation \(y\cdot\nabla\).

Pour un champ lisse divergence-free \(U\), posons

\[
 g=\nabla\chi\cdot U,\qquad
 C=\mathcal Bg,\qquad
 QU=\chi U-C.                                    \tag{6}
\]

La moyenne de \(g\) est nulle :

\[
 \int_Ag
 =\int_{\mathbb R^3}\nabla\chi\cdot U
 =\int_{\mathbb R^3}\nabla\cdot(\chi U)=0.       \tag{7}
\]

L'opérateur \(Q\) produit donc un champ compact divergence-free, égal à
\(U\) dans \(B(0,1)\).

Le commutateur étudié est

\[
 \boxed{
 K(U)=-[\Delta,Q]U+\kappa[D,Q]U,}               \tag{8}
\]

où

\[
 [A,Q]=AQ-QA
\]

et \(\kappa\ge0\) est fixé. Dans l'application mobile du cycle 0042,
\(\kappa=2/S_{w,*}(C_MM)\), mais sa valeur n'intervient pas dans les
identités.

## 2. Commutateur laplacien exact

Comme

\[
 \Delta(\chi U)-\chi\Delta U
 =(\Delta\chi)U+2(\nabla\chi\cdot\nabla)U,      \tag{9}
\]

on obtient directement

\[
 \boxed{
 \begin{aligned}
 -[\Delta,Q]U
 ={}&-(\Delta\chi)U
 -2(\nabla\chi\cdot\nabla)U\\
 &+\Delta\mathcal Bg
 -\mathcal B(\nabla\chi\cdot\Delta U).
 \end{aligned}}                                 \tag{10}
\]

Cette formule est classique pour \(U\) lisse. Elle n'autorise ni
\(\Delta\mathcal B=\mathcal B\Delta\), ni l'application de
\(\mathcal B\) séparément à une distribution sans préciser son domaine.

### Réduction des dérivées de \(U\)

Définissons le champ scalaire-indexé

\[
 H_j=\sum_{i=1}^3(\partial_{ji}\chi)U_i,
 \qquad H=(\nabla^2\chi)U.                      \tag{11}
\]

Un calcul composante par composante donne

\[
 \begin{aligned}
 \Delta g
 &=\nabla\chi\cdot\Delta U
 +2\sum_{i,j}\partial_{ji}\chi\,\partial_jU_i
 +\nabla\Delta\chi\cdot U,\\
 \nabla\cdot H
 &=\sum_{i,j}\partial_{ji}\chi\,\partial_jU_i
 +\nabla\Delta\chi\cdot U.
 \end{aligned}                                  \tag{12}
\]

Par conséquent,

\[
 \boxed{
 \nabla\chi\cdot\Delta U
 =\Delta g-2\nabla\cdot H+\nabla\Delta\chi\cdot U.} \tag{13}
\]

En injectant (13) dans (10),

\[
 \boxed{
 \begin{aligned}
 -[\Delta,Q]U
 ={}&-(\Delta\chi)U
 -2(\nabla\chi\cdot\nabla)U\\
 &+[\Delta,\mathcal B]g
 +2\mathcal B(\nabla\cdot H)
 -\mathcal B(\nabla\Delta\chi\cdot U).
 \end{aligned}}                                 \tag{14}
\]

Toutes les données scalaires auxquelles \(\mathcal B\) est appliqué ont
moyenne nulle. En particulier,

\[
 \int_A\nabla\Delta\chi\cdot U
 =-\int_A\Delta\chi\,\nabla\cdot U=0,           \tag{15}
\]

et l'intégrale d'une divergence compacte est nulle.

Le premier couple de (14) s'écrit sans dérivée non compensée :

\[
 -(\Delta\chi)U-2(\nabla\chi\cdot\nabla)U
 =(\Delta\chi)U
 +\nabla\cdot G_\chi,                           \tag{16}
\]

où, avec la divergence prise sur le second indice,

\[
 (G_\chi)_{ij}=-2U_i\partial_j\chi.             \tag{17}
\]

## 3. Commutateur de dilatation exact

La règle du produit donne

\[
 Dg=(D\nabla\chi)\cdot U+\nabla\chi\cdot DU.    \tag{18}
\]

Ainsi

\[
 \begin{aligned}
 [D,Q]U
 &=(D\chi)U-D\mathcal Bg
   +\mathcal B(\nabla\chi\cdot DU)\\
 &=(D\chi)U+[\mathcal B,D]g
   -\mathcal B((D\nabla\chi)\cdot U).
 \end{aligned}                                  \tag{19}
\]

Donc

\[
 \boxed{
 [D,Q]U
 =(D\chi)U+[\mathcal B,D]g
 -\mathcal B((D\nabla\chi)\cdot U).}            \tag{20}
\]

La dernière donnée a également moyenne nulle. En effet,

\[
 D\nabla\chi=\nabla(D\chi)-\nabla\chi,
\]

d'où

\[
 \int_A(D\nabla\chi)\cdot U=0.                  \tag{21}
\]

## 4. Formule algébrique finale

Les équations (14), (16) et (20) donnent

\[
 \boxed{
 \begin{aligned}
 K(U)={}&f_{\rm alg}(U)+\nabla\cdot G_\chi\\
 &+[\Delta,\mathcal B]g
 +2\mathcal B(\nabla\cdot H)
 +\kappa[\mathcal B,D]g,
 \end{aligned}}                                 \tag{22}
\]

avec

\[
 \boxed{
 \begin{aligned}
 f_{\rm alg}(U)
 ={}&(\Delta\chi)U
 -\mathcal B(\nabla\Delta\chi\cdot U)\\
 &+\kappa(D\chi)U
 -\kappa\mathcal B((D\nabla\chi)\cdot U).
 \end{aligned}}                                 \tag{23}
\]

Cette identité est démontrée pour tout \(U\in C^\infty\) divergence-free
pour lequel les expressions ont un sens. Chaque terme est supporté dans une
sous-couronne compacte de \(A\), grâce au choix support-lisse (4).

## 5. Hypothèses opératorielles négatives

Pour \(1<p<\infty\), introduisons les hypothèses quantitatives suivantes,
pour la **même** réalisation de \(\mathcal B\) :

\[
 \begin{aligned}
 {\rm (B0)}\quad&
 \|\mathcal Bh\|_{W^{1,p}}
 \le C_p\|h\|_{L^p},\\
 {\rm (B-1)}\quad&
 \|\mathcal Bh\|_{L^p}
 \le C_p\|h\|_{W^{-1,p}},\\
 {\rm (B-2)}\quad&
 \|\mathcal Bh\|_{W^{-1,p}}
 \le C_p\|h\|_{W^{-2,p}}.
 \end{aligned}                                  \tag{24}
\]

Les espaces négatifs sont pris sur \(A\), modulo la compatibilité de moyenne
nécessaire. Une formule intégrale de Bogovskii suffisamment régulière est un
opérateur d'ordre moins un et devrait satisfaire cette échelle. Toutefois,
la seule assertion (4), qui porte sur les fonctions tests, n'est pas une
preuve quantitative de (24).

### Ce que contrôle (B-1)

Comme \(H\in L^p\),

\[
 \|\mathcal B(\nabla\cdot H)\|_{L^p}
 \le C_p\|H\|_{L^p}
 \le C_{\chi,p}\|U\|_{L^p}.                    \tag{25}
\]

De même,

\[
 Dg=\nabla\cdot(yg)-3g\in W^{-1,p},            \tag{26}
\]

et

\[
 \begin{aligned}
 \|[\mathcal B,D]g\|_{L^p}
 &\le\|\mathcal B(Dg)\|_{L^p}
   +\|D\mathcal Bg\|_{L^p}\\
 &\le C_{\chi,B,p}\|U\|_{L^p}.                 \tag{27}
 \end{aligned}
\]

Ainsi (B-1) contrôle tous les nouveaux termes de (22), sauf le commutateur
laplacien.

### Pourquoi (B-1) seule ne suffit pas

On a

\[
 [\Delta,\mathcal B]g
 =\nabla\cdot(\nabla\mathcal Bg)-\mathcal B(\Delta g). \tag{28}
\]

Le premier terme appartient à \(W^{-1,p}\) par (B0). Mais

\[
 \Delta g\in W^{-2,p},
\]

et non en général dans \(W^{-1,p}\). Pour contrôler le second terme dans
\(W^{-1,p}\), il faut (B-2), ou directement l'estimation

\[
 {\rm (BC)}\qquad
 \|[\Delta,\mathcal B]g\|_{W^{-1,p}}
 \le C_p\|g\|_{L^p}.                            \tag{29}
\]

Affirmer que l'extension \(W^{-1,p}\to L^p\) suffit à (29) inverse un ordre
de dérivation. C'est faux comme argument, même si (29) peut être vraie pour
une formule intégrale particulière.

Sous (B0) et (B-2),

\[
 \|[\Delta,\mathcal B]g\|_{W^{-1,p}}
 \le C_p\|g\|_{L^p}.                            \tag{30}
\]

## 6. Représentation \(f_0+\operatorname{div}G_0\)

Fixons une convention concrète :

\[
 W^{-1,p}(A)
 =\{f+\nabla\cdot G:
 f\in L^p(A;\mathbb R^3),\
 G\in L^p(A;\mathbb R^{3\times3})\},            \tag{31}
\]

avec la norme quotient. Sous (B0)--(B-2), (22) donne

\[
 \|K(U)\|_{W^{-1,p}(A)}
 \le C_{\chi,\mathcal B,p,\kappa}\|U\|_{L^p(A)}. \tag{32}
\]

Plus explicitement, écrivons

\[
 -\mathcal B(\Delta g)=f_g+\nabla\cdot G_g      \tag{33}
\]

avec

\[
 \|f_g\|_{L^p}+\|G_g\|_{L^p}
 \le C_p\|g\|_{L^p},                            \tag{34}
\]

ce qui est permis par (B-2) et la définition (31). Alors une représentation
exacte est

\[
 \boxed{
 \begin{aligned}
 f_0={}&f_{\rm alg}
 +2\mathcal B(\nabla\cdot H)
 +\kappa[\mathcal B,D]g+f_g,\\
 G_0={}&G_\chi+\nabla\mathcal Bg+G_g,
 \end{aligned}}                                 \tag{35}
\]

et

\[
 \boxed{K(U)=f_0+\nabla\cdot G_0.}              \tag{36}
\]

Toutes les égalités de (33)--(36) sont distributionnelles.

## 7. Passage à l'endpoint faible critique

La couronne unité a volume

\[
 |A|=\frac{28\pi}{3}.                            \tag{37}
\]

Pour \(U\in L^{3,\infty}(A)\),

\[
 \|U\|_{L^{3/2,\infty}(A)}
 \le |A|^{1/3}\|U\|_{L^{3,\infty}(A)}.          \tag{38}
\]

Supposons que (24) soit vraie pour deux exposants
\[
 1<p_-<3/2<p_+<\infty
\]
avec la même réalisation. L'interpolation réelle transporte alors les
estimations vers le second indice de Lorentz infini. Les équations
(32)--(38) donnent

\[
 \boxed{
 \|f_0\|_{L^{3/2,\infty}}
 +\|G_0\|_{L^{3/2,\infty}}
 \le C_{\chi,\mathcal B,\kappa}
 \|U\|_{L^{3,\infty}}.}                         \tag{39}
\]

Comme le support de \(f_0\) reste dans la couronne fixe,

\[
 \|f_0\|_{L^{1,\infty}}
 \le |A|^{1/3}\|f_0\|_{L^{3/2,\infty}}.         \tag{40}
\]

Ainsi

\[
 \boxed{
 \|f_0\|_{L^{1,\infty}}
 +\|G_0\|_{L^{3/2,\infty}}
 \le C_{\chi,\mathcal B,\kappa}
 \|U\|_{L^{3,\infty}}.}                         \tag{41}
\]

La paire d'espaces dans (41) est exactement critique après retour au rayon
physique : si

\[
 f_{0,R}(x)=R^{-3}f_0(x/R),\qquad
 G_{0,R}(x)=R^{-2}G_0(x/R),                     \tag{42}
\]

alors

\[
 \|f_{0,R}\|_{L^{1,\infty}}
 =\|f_0\|_{L^{1,\infty}},\qquad
 \|G_{0,R}\|_{L^{3/2,\infty}}
 =\|G_0\|_{L^{3/2,\infty}}.                    \tag{43}
\]

Le passage à \(L^{p,\infty}\) ne peut pas être obtenu par densité depuis un
seul exposant fort. Il requiert les estimations du même opérateur à deux
exposants voisins.

## 8. Ce qui est prouvé, conditionnel ou faux

| Assertion | Statut | Justification |
|---|---|---|
| formules (10), (14), (20), (22) | **prouvé** | règles de produit pour \(U\) lisse |
| moyenne nulle de toutes les données de \(\mathcal B\) | **prouvé** | divergence-free et supports compacts |
| contrôle des termes de dilatation depuis (B-1) | **prouvé conditionnellement à (B-1)** | (25)--(27) |
| \([\Delta,\mathcal B]:L^p\to W^{-1,p}\) depuis (B0) et (B-2) | **prouvé conditionnellement** | (28)--(30) |
| représentation critique (41) | **prouvé conditionnellement à l'échelle (24)** | (35)--(43) |
| support-lisse sur \(C_c^\infty\) implique à lui seul (24) avec constantes | **non démontré** | continuité qualitative insuffisante |
| (B-1) seule implique (29) | **faux comme déduction** | \(\Delta g\in W^{-2,p}\) |
| borne uniforme \(\|K(U)\|_{L^{1,\infty}}\lesssim\|U\|_{L^{3,\infty}}\) | **fausse** | test pure-swirl ci-dessous |
| croissance \(O(N)\) dans la norme négative critique | **fausse sur le test** | représentation exacte (49) |

## 9. Test pure-swirl haute fréquence

Prenons \(\chi=\chi(s)\) radial en
\[
 s=|y|,
\]
et choisissons une zone compacte de la couronne évitant l'axe cylindrique.
Soit

\[
 U_N(r,\theta,z)
 =\varepsilon\,\phi(r,z)\sin(Nz)e_\theta,       \tag{44}
\]

où \(\phi\in C_c^\infty(A)\) est axisymétrique. Chaque \(U_N\) est lisse,
compact et divergence-free.

Puisque \(e_\theta\) est tangent aux sphères,

\[
 \nabla\chi\cdot U_N=0.                         \tag{45}
\]

Le laplacien d'un swirl axisymétrique reste purement azimutal, et la
dilatation \(D\) conserve cette direction. Donc

\[
 \nabla\chi\cdot\Delta U_N=0,\qquad
 \nabla\chi\cdot DU_N=0.                        \tag{46}
\]

Il s'ensuit que

\[
 QU_N=\chi U_N,\qquad
 Q\Delta U_N=\chi\Delta U_N,\qquad
 QDU_N=\chi DU_N.                               \tag{47}
\]

Tous les termes de Bogovskii s'annulent **exactement**, pas seulement
asymptotiquement. Les commutateurs valent

\[
 \begin{aligned}
 -[\Delta,Q]U_N
 &=-(\Delta\chi)U_N
   -2(\nabla\chi\cdot\nabla)U_N,\\
 [D,Q]U_N&=(D\chi)U_N.                          \tag{48}
 \end{aligned}
\]

En utilisant (16),

\[
 \boxed{
 K(U_N)
 =(\Delta\chi+\kappa D\chi)U_N
 +\nabla\cdot(-2U_N\otimes\nabla\chi).}         \tag{49}
\]

### Norme positive

Sur une région où \(\phi\), \(z\) et la dérivée radiale de \(\chi\) ne
s'annulent pas,

\[
 |(\nabla\chi\cdot\nabla)U_N|
 \ge c_{\chi,\phi}\varepsilon N                \tag{50}
\]

sur une fraction de volume indépendante de \(N\). Ainsi

\[
 \|K(U_N)\|_{L^{1,\infty}}
 \ge c_{\chi,\phi}\varepsilon N-O(\varepsilon), \tag{51}
\]

tandis que

\[
 \|U_N\|_{L^{3,\infty}}\le C_\phi\varepsilon.  \tag{52}
\]

Cela réfute toute borne positive uniforme du type annoncé dans le tableau.

### Norme négative

La représentation (49) donne au contraire

\[
 f_{0,N}=(\Delta\chi+\kappa D\chi)U_N,\qquad
 G_{0,N}=-2U_N\otimes\nabla\chi.                \tag{53}
\]

Par conséquent,

\[
 \boxed{
 \|f_{0,N}\|_{L^{1,\infty}}
 +\|G_{0,N}\|_{L^{3/2,\infty}}
 \le C_{\chi,\phi,\kappa}\varepsilon,}          \tag{54}
\]

uniformément en \(N\). Le \(O(N)\) n'est pas rendu petit : il est absorbé
exactement comme divergence d'un stress critique d'amplitude \(O(1)\).

Ce calcul corrige le test adverse du cycle 0042 : celui-ci réfutait à juste
titre une estimation terme à terme en \(L^{1,\infty}\), mais il ne réfute
pas une estimation dans
\(L^{1,\infty}+\operatorname{div}L^{3/2,\infty}\).

## 10. Passe contradictoire

1. **Signe du commutateur.** Le signe de
   \(\Delta\mathcal Bg-\mathcal B(\nabla\chi\cdot\Delta U)\)
   dans (10) provient du signe moins dans \(QU=\chi U-\mathcal Bg\).
2. **Hessienne.** Le signe de \(\nabla\Delta\chi\cdot U\) dans (13) est
   positif ; une inversion détruit (14).
3. **Moyennes.** Les termes
   \(\nabla\Delta\chi\cdot U\) et
   \((D\nabla\chi)\cdot U\) ont moyenne nulle grâce à
   \(\nabla\cdot U=0\), pas séparément par parité.
4. **Ordre de \(\mathcal B\).** (B-1) gagne une dérivée, mais le laplacien en
   perd deux. Une seconde marche négative est requise.
5. **Support-lisse.** L'application
   \(C^\infty_{c,0}\to C_c^\infty\) ne contrôle pas la norme d'opérateur dans
   les complétions négatives.
6. **Endpoint faible.** L'interpolation doit utiliser un opérateur commun ;
   \(C_c^\infty\) n'est pas dense dans la norme faible-\(L^p\).
7. **Représentation non unique.** La paire \((f_0,G_0)\) de (35) dépend du
   représentant choisi de la norme quotient \(W^{-1,p}\). Seule l'existence
   avec borne est intrinsèque.
8. **Pure-swirl.** L'annulation de Bogovskii utilise un cutoff radial. Elle
   ne vaut pas pour un cutoff angulaire arbitraire.
9. **\(O(N)\).** La croissance demeure dans toute norme positive sensible
   à la dérivée ; elle disparaît seulement après passage à la divergence
   distributionnelle.
10. **Critique ne signifie pas petit.** La borne (41), même démontrée avec
    la constante complète, produit une force critique \(O(M)\), pas une
    force tendant vers zéro.
11. **Projection de Leray.** Projeter
    \(\nabla\cdot G_0\) rend la force solénoïdale mais non compacte.
12. **Dynamique.** Le présent calcul ne contrôle ni le défaut non linéaire
    \(Q((U\cdot\nabla)U)-(QU\cdot\nabla)QU\), ni la pression, ni une limite
    ancienne.

## 11. Verdict falsifiable et prochain lemme

Le résultat inconditionnel du cycle est :

\[
 K(U)\text{ satisfait les identités (22)--(23),} \tag{55}
\]

et, sur les modes pure-swirl,

\[
 \sup_N
 \left(
 \|f_{0,N}\|_{L^{1,\infty}}
 +\|G_{0,N}\|_{L^{3/2,\infty}}
 \right)<\infty,                               \tag{56}
\]

alors que

\[
 \|K(U_N)\|_{L^{1,\infty}}\to\infty.           \tag{57}
\]

Le résultat général

\[
 \|K(U)\|_{L^{1,\infty}
 +\operatorname{div}L^{3/2,\infty}}
 \le C_{\chi,\mathcal B,\kappa}
 \|U\|_{L^{3,\infty}}                          \tag{58}
\]

est `CONDITIONNEL` à (B-2) ou (BC), plus interpolation aux exposants
voisins. Il est faux de l'enregistrer comme conséquence du seul caractère
support-lisse de (4).

Le prochain test décisif doit partir de la formule intégrale effectivement
choisie pour \(\mathcal B\) et vérifier, par dualité ou estimations de noyau,

\[
 \boxed{
 \mathcal B:W^{-2,p}_0(A)\to W^{-1,p}_0(A)
 \quad\text{pour }p\text{ dans un voisinage de }3/2,} \tag{59}
\]

avec la même constante géométrique après interpolation Lorentz. Un
contre-exemple à (59), ou une dépendance non uniforme lors de
l'approximation support-lisse, invaliderait (58). Une preuve de (59)
fermerait le sous-gap linéaire, mais laisserait entière la rigidité de
l'équation forcée critique.
