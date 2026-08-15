# Cycle 0056 - audit primaire du raccord compacité--modulation--RSS

Date de coupure : **2026-08-15**.  Cette note est une veille bibliographique
indépendante et bornée. Elle répond à une question précise : existe-t-il un
théorème primaire, publié ou prépublié, qui transforme une suite de solutions
de Navier--Stokes à défaut de rotation modulé borné en une limite RSS qui soit
à la fois adaptée (*suitable*) et uniformément faible-$L^3$ ?

## Verdict

**Non dans le corpus primaire vérifié.** Deux distinctions rendent ce verdict
plus fort qu'une simple absence de résultat trouvé.

1. Si le « défaut modulé borné » signifie seulement

   \[
     D_n:=\partial_sV_n-\beta_n(s)\mathcal RV_n
     \quad\hbox{borné dans un espace de distributions},                 \tag{1}
   \]

   alors l'implication vers une limite RSS est **fausse comme principe de
   compacité**. Une sous-suite peut avoir $D_n\rightharpoonup D\ne0$; la limite
   vérifie alors $\partial_sV-\beta\mathcal RV=D$, non l'équation d'orbite
   $\partial_sV=\beta\mathcal RV$. Il faut au minimum $D_n\to0$ dans les
   distributions, et non une borne uniforme.

2. Après avoir remplacé « borné » par « tend vers zéro », les trois briques
   nécessaires existent séparément : reconstruction de phase pour des PDE
   classiques dans un espace de Banach; compacité forte locale de solutions
   adaptées sous bornes d'énergie et de pression; stabilité faible-étoile
   d'une classe **structurée** de solutions faibles $L^{3,\infty}$. Aucun des
   textes vérifiés ne les assemble pour des solutions anciennes adaptées,
   uniformément $L^{3,\infty}$, avec rotation modulée.

Le résultat bibliographique est donc négatif mais actionnable : le premier
lemme transférable n'est pas un nouveau théorème abstrait de phase. C'est un
lemme de fermeture conditionnel qui doit fournir simultanément

\[
 \boxed{
 \begin{gathered}
 V_n\to V\ \hbox{fortement dans }L^3_{\rm loc},\qquad
 P_n\rightharpoonup P\ \hbox{dans }L^{3/2}_{\rm loc},\\
 \beta_n\stackrel{*}{\rightharpoonup}\beta\ \hbox{dans }L^\infty_{\rm loc},
 \qquad D_n\to0\ \hbox{dans }\mathcal D',
 \end{gathered}}                                                     \tag{2}
\]

puis préserver l'inégalité d'énergie locale et la non-trivialité. La borne
$L^\infty_sL^{3,\infty}_y$ seule ne donne pas ces conclusions dans les sources
auditées.

## 1. Formulation exacte auditée

Le cadre actif est Navier--Stokes incompressible 3D, viscosité un, sans force,
sur $\mathbb R^3\times(-\infty,0)$ :

\[
 \partial_tu-\Delta u+(u\cdot\nabla)u+\nabla p=0,
 \qquad \nabla\cdot u=0.                                             \tag{3}
\]

Avec

\[
 y=\frac{x}{\sqrt{-t}},\qquad s=-\log(-t),\qquad
 V(y,s)=\sqrt{-t}\,u(x,t),\qquad P(y,s)=(-t)p(x,t),                  \tag{4}
\]

l'équation devient

\[
 \partial_sV-\Delta V+\frac12V+\frac12y\cdot\nabla V
 +(V\cdot\nabla)V+\nabla P=0,
 \qquad \nabla\cdot V=0.                                            \tag{5}
\]

Pour les rotations autour de $e_3$,

\[
 (\rho_\theta U)(y)=R_\theta U(R_{-\theta}y),\qquad
 \mathcal RU=JU-(Jy\cdot\nabla)U,                                  \tag{6}
\]

où $J=R'_0$. Une limite **RSS** dans cette note signifie qu'il existe un profil
fixe $U$, une constante $\alpha$ et une phase $\theta_0$ tels que

\[
 V(s)=\rho_{\theta_0+\alpha s}U                                    \tag{7}
\]

au sens distributionnel, avec la pression transformée de la même façon à une
fonction additive du temps près. Elle doit en outre provenir par (4) d'une
solution faible adaptée de (3), et vérifier

\[
 \mathop{\rm ess\,sup}_{s\in\mathbb R}
 \|V(s)\|_{L^{3,\infty}(\mathbb R^3)}<\infty.                        \tag{8}
\]

Une limite **RDSS** est un autre objet : pour un $S>0$ et une phase $\phi$,

\[
 V(s+S)=\rho_\phi V(s).                                             \tag{9}
\]

Elle peut varier dans l'espace quotient pendant une période. L'annulation de
$\partial_sV-\beta\mathcal RV$ force au contraire une orbite pure et ne
constitue donc pas un critère général de RDSS.

### Échelle

Sous $u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t)$,
$\|u(t)\|_{L^{3,\infty}}$ est invariant. La rotation est une isométrie de cet
espace. Dans les variables (4), $V$, $\partial_sV$ et
$\beta\mathcal RV$ sont sans dimension supplémentaire; (1) est donc un défaut
critique si sa norme est elle-même choisie invariante. Une petite norme locale
sous-critique du défaut ne peut pas être remplacée silencieusement par une
simple borne critique.

## 2. Sources primaires et quantificateurs

| Source et statut au 2026-08-15 | Cadre exact | Résultat utilisable | Trou par rapport au raccord demandé |
|---|---|---|---|
| W.-J. Beyn, V. Thümmler, *Freezing Solutions of Equivariant Evolution Equations*, *SIAM J. Appl. Dyn. Syst.* **3**(2) (2004), 85--116, [DOI 10.1137/030600515](https://doi.org/10.1137/030600515), **publié** | Évolution $u_t=F(u)$ sur Banach, action d'un groupe de Lie fini-dimensionnel; applications réaction--diffusion | Th. 2.6 : équivalence avec le repère mobile; th. 2.9 : phase locale par fonction implicite; prop. 2.10 : non-dégénérescence si stabilisateur trivial | Solutions $C_tX\cap C_t^1X$ prenant leurs valeurs dans un domaine régulier $Y$; pas de suite faible, pas de Navier--Stokes suitable, pas de compacité faible-$L^3$ |
| C. W. Rowley, I. G. Kevrekidis, J. E. Marsden, K. Lust, *Reduction and Reconstruction for Self-Similar Dynamical Systems*, *Nonlinearity* **16** (2003), 1257--1275, [DOI 10.1088/0951-7715/16/4/304](https://doi.org/10.1088/0951-7715/16/4/304), **publié** | Champ de vecteurs sur variété lisse avec action de groupe et covariance permettant une remise à l'échelle du temps | Th. 2.1 : un point fixe de la dynamique en tranche correspond à un équilibre relatif, donc à une solution auto-similaire; équations de reconstruction | Cadre différentiable et réduction exacte; aucune fermeture par compacité, aucune inégalité d'énergie locale |
| J. Simon, *Compact Sets in the Space $L^p(0,T;B)$*, *Ann. Mat. Pura Appl.* **146** (1987), 65--96, [DOI 10.1007/BF01762360](https://doi.org/10.1007/BF01762360), **publié** | Théorème fonctionnel $X\Subset B\hookrightarrow Y$ | Cor. 4 : borne spatiale plus contrôle de dérivée temporelle négative donnent compacité forte espace--temps | Ne crée ni les estimations de Navier--Stokes, ni la pression, ni une phase, ni une trace non nulle |
| D. Albritton, T. Barker, *Localised Necessary Conditions for Singularity Formation in the Navier--Stokes Equations with Curved Boundary*, *J. Differential Equations* **269** (2020), 7529--7573, [DOI 10.1016/j.jde.2020.06.009](https://doi.org/10.1016/j.jde.2020.06.009), **publié** | Solutions faibles adaptées des équations aplaties près d'un bord; vitesse $L^3$, pression $L^{3/2}$ | Lemme A.2 : après extraction, vitesse forte $L^3$ et pression faible $L^{3/2}$ sur les sous-cylindres; la limite reste adaptée | Les bornes fortes endpoint sont des hypothèses; elles ne découlent pas d'une seule borne $L^\infty_tL^{3,\infty}_x$; aucune modulation |
| T. Barker, G. Seregin, V. Šverák, *On Stability of Weak Navier--Stokes Solutions with Large $L^{3,\infty}$ Initial Data*, *Comm. PDE* **43**(4) (2018), 628--651, [DOI 10.1080/03605302.2018.1449219](https://doi.org/10.1080/03605302.2018.1449219), **publié** | Problème de Cauchy forward sur $\mathbb R^3$; solutions faibles globales $L^{3,\infty}$ spécialement définies par $v=S(t)u_0+u$ avec correcteur énergétique et inégalité locale | Th. 1.3 : données $u_{0,n}\stackrel *\rightharpoonup u_0$ dans $L^{3,\infty}$ donnent, après extraction, une solution limite; dans la preuve, $u_n\to u$ dans $C_tL^{9/8}_{\rm loc}$ et dans $L^q_{\rm loc}$ pour tout $1<q<10/3$, donc $q=3$ | Temps initial fixe, classe calorique scindée, non une suite ancienne arbitraire; aucune phase; aucune garantie de non-trivialité |
| R. O'Neil, *Convolution Operators and $L(p,q)$ Spaces*, *Duke Math. J.* **30**(1) (1963), 129--142, [DOI 10.1215/S0012-7094-63-03015-1](https://doi.org/10.1215/S0012-7094-63-03015-1), **publié** | Espaces de Lorentz et inégalités de produit/convolution | Fournit le calcul fonctionnel Lorentz sous-jacent à l'appariement $L^{3,\infty}$--$L^{3/2,1}$ | Un appariement linéaire ne fait pas converger $u_n\otimes u_n$ lorsque les deux facteurs ne convergent que faiblement |
| Z. Bradshaw, T.-P. Tsai, *Rotationally Corrected Scaling Invariant Solutions to the Navier--Stokes Equations*, *Comm. PDE* **42**(7) (2017), 1065--1087, [DOI 10.1080/03605302.2017.1323922](https://doi.org/10.1080/03605302.2017.1323922), **publié** | Navier--Stokes incompressible 3D, espace entier ou demi-espace, non forcé; solutions faibles forward, grandes données $L^{3,\infty}$ | Définitions RSS/RDSS, équation en repère tournant; constructions exactes à vitesse angulaire constante | Construit depuis une covariance exacte; ne prend pas une limite de défauts modulés; direction temporelle opposée au blow-up backward |
| D. Chae, J. Wolf, *Removing Discretely Self-Similar Singularities for the 3D Navier--Stokes Equations*, *Comm. PDE* **42**(9) (2017), 1359--1374, [DOI 10.1080/03605302.2017.1358275](https://doi.org/10.1080/03605302.2017.1358275), **publié** | Solution backward lisse exactement DSS, espace entier, borne ponctuelle Type I | Exclusion si le facteur DSS $\lambda>1$ est assez proche de un | Ni rotation, ni faible-$L^3$ suitable, ni passage d'une symétrie approchée à une symétrie exacte |
| B. Pineau, V. Vicol, *On Rotated Backwards Self-Similar Solutions of the Incompressible 3D Navier--Stokes Equations*, [`arXiv:2607.09619v2`](https://arxiv.org/abs/2607.09619v2), v2 du 2026-08-06, **prépublication** | Solution backward globale lisse sur $\mathbb R^3\times[-1,0)$, ansatz RSS/RDSS exact, borne ponctuelle Type I | Th. 1.4 : trivialité RSS pour $|\alpha|$ petit ou grand; th. 1.7 : analogue RDSS pour période courte et régimes extrêmes | Commence après le raccord recherché; Type I ponctuel strictement plus fort que faible-$L^3$; vitesses intermédiaires ouvertes; pas de théorème de compacité |

Les sources de dynamique équivariante de Field et Krupa, déjà auditées au
cycle 0055, restent plus éloignées encore : champs lisses de dimension finie,
flot classique et hypothèses de groupe compact ou de variété compacte. Elles
ne fournissent pas la stabilité d'une orbite relative sous convergence faible
de solutions PDE.

## 3. Ce que la reconstruction de phase publiée donne réellement

Beyn--Thümmler supposent une action continue sur $X$, différentiable sur un
espace plus régulier $Y$, et une solution

\[
 u\in C([0,T);X)\cap C^1((0,T);X),\qquad u(t)\in Y.                  \tag{10}
\]

Pour $u(t)=a(\gamma(t))v(t)$, le théorème 2.6 justifie l'équation gelée.
Le théorème 2.9 reconstruit localement $\gamma\in C^1$ si la dérivée de la
condition de phase est inversible. La proposition 2.10 obtient cette
inversibilité pour deux conditions de distance lorsque le stabilisateur du
profil initial est trivial.

Pour la condition adaptative qui minimise $\|v_t\|^2$, le coefficient de phase
résout

\[
 (S^*S)(v,\gamma)\lambda=S^*(v,\gamma)F(v).                         \tag{11}
\]

Le texte exige que $S^*S$ soit inversible et indique explicitement qu'une
existence unique pour l'ODE de reconstruction demande plus de régularité que
le théorème 2.9. Ainsi, même dans ce cadre classique, la reconstruction n'est
ni globale ni uniforme près d'un stabilisateur.

Pour une suite, « stabilisateur trivial pour chaque $n$ » ne suffit pas. Il
faudrait une borne quantitative uniforme

\[
 \lambda_{\min}\big((S_n^*S_n)(s)\big)\ge c_*>0                     \tag{12}
\]

sur chaque fenêtre. La limite faible peut acquérir une symétrie et faire
tendre ce minimum vers zéro. Aucun théorème de Beyn--Thümmler ne remplace
(12) par une borne $L^{3,\infty}$.

Rowley--Kevrekidis--Marsden--Lust incorporent aussi les dilatations et montrent
qu'un point fixe de la dynamique réduite est une solution auto-similaire.
Mais leur théorème commence avec un champ de vecteurs et une tranche lisses;
il ne dit pas qu'une suite à petit résidu possède un point fixe limite, encore
moins que cette limite satisfait l'inégalité d'énergie locale de
Navier--Stokes.

## 4. Compacité et passage du terme quadratique

### 4.1 Route énergétique locale publiée

Sur un cylindre intérieur, des bornes uniformes

\[
 \|V_n\|_{L^\infty_sL^2_y}
 +\|\nabla V_n\|_{L^2_{s,y}}
 +\|P_n-(P_n)_{B}\|_{L^{3/2}_{s,y}}\le C                           \tag{13}
\]

donnent $V_n$ borné dans $L^{10/3}$ et $\partial_sV_n$ dans un espace
négatif tel que $L^{4/3}_sW^{-1,4/3}_y$. Simon donne alors la forte convergence
$L^2_{\rm loc}$; l'interpolation avec $L^{10/3}$ donne

\[
 V_n\to V\quad\hbox{fortement dans }L^q_{\rm loc},
 \qquad 2\le q<10/3.                                                \tag{14}
\]

Le choix $q=3$ identifie $V_n\otimes V_n$ dans $L^{3/2}_{\rm loc}$.
Albritton--Barker A.2 publie directement la fermeture adaptée sous des bornes
$L^3/L^{3/2}$, y compris au bord courbe.

La difficulté endpoint est antérieure à cette conclusion : sur un cylindre
de mesure finie, $L^{3,\infty}$ s'injecte dans $L^q$ pour $q<3$, pas dans
$L^3$. Une borne uniforme (8) ne fournit donc pas à elle seule (13) ni la
pression $L^{3/2}$ requise.

### 4.2 La stabilité Barker--Seregin--Šverák est structurée

Le théorème 1.3 de Barker--Seregin--Šverák est le résultat publié le plus
proche de l'endpoint. Il utilise cependant la décomposition imposée

\[
 v_n=S(t)u_{0,n}+u_n,
 \qquad
 u_n\in L^\infty_tL^2_x\cap L^2_t\dot H^1_x,                         \tag{15}
\]

avec trace forte nulle du correcteur, inégalité d'énergie globale perturbée et
inégalité d'énergie locale. La preuve obtient

\[
 u_n\to u\ \hbox{dans }C([0,T];L^{9/8}(B_R)),\qquad
 u_n\to u\ \hbox{dans }L^q(B_R\times(0,T)),\quad1<q<10/3.           \tag{16}
\]

La forte convergence $q=3$ ferme le produit. Le théorème ne s'applique pas à
une suite arbitraire de solutions adaptées satisfaisant seulement (8), et sa
décomposition dépend d'une donnée initiale forward fixe. Une diagonale vers
une solution ancienne doit reconstruire cette architecture sur toutes les
fenêtres reculées; ce passage n'est pas dans l'article.

### 4.3 Produit faible-étoile $L^\infty$ fois fort

La partie scalaire de la modulation n'est pas le verrou si l'on possède déjà
la convergence forte. Le lemme élémentaire suivant suffit.

Si $\beta_n\stackrel *\rightharpoonup\beta$ dans $L^\infty(I)$ et
$g_n\to g$ dans $L^1(I)$, alors

\[
 \int_I\beta_ng_n\,ds\longrightarrow\int_I\beta g\,ds.             \tag{17}
\]

En effet, on sépare $\int\beta_n(g_n-g)$ et
$\int(\beta_n-\beta)g$. Pour un test compact $\varphi$,

\[
 g_n(s)=\langle\mathcal RV_n(s),\varphi(s)\rangle
       =\langle V_n(s),\mathcal R^*\varphi(s)\rangle.               \tag{18}
\]

Ainsi $V_n\to V$ fortement dans $L^1_{\rm loc}$ implique
$g_n\to g$ dans $L^1(I)$, malgré la dérivée présente dans $\mathcal R$ : elle
est transférée au test. Avec $\|\beta_n\|_{L^\infty}\le C$, on obtient

\[
 \beta_n\mathcal RV_n\longrightarrow\beta\mathcal RV
 \quad\hbox{dans }\mathcal D'.                                     \tag{19}
\]

Ce calcul est une dérivation standard du laboratoire, pas un nouveau
`PAPER_PROOF`. Il ne ferme ni $V_n\otimes V_n$ ni l'énergie locale; pour ces
deux opérations, la forte convergence $L^3$ et la pression de (2) restent
nécessaires.

## 5. Lemme de raccord conditionnel réellement défendable

Le corpus permet le lemme conditionnel suivant, par juxtaposition de résultats
publiés et du calcul (17)--(19).

> **Lemme conditionnel (statut : `STANDARD_DERIVATION`).** Soient
> $(V_n,P_n)$ des solutions faibles adaptées de (5) sur chaque cylindre compact
> de $\mathbb R^3\times\mathbb R$. Supposons les bornes locales d'énergie et de
> pression qui donnent (14), une borne
> $\|\beta_n\|_{L^\infty(I)}\le C_I$ sur chaque intervalle compact, et
> $D_n\to0$ dans $\mathcal D'$. Alors une sous-suite vérifie (2); la limite est
> adaptée, satisfait (5), et
> $\partial_sV=\beta(s)\mathcal RV$ dans $\mathcal D'$.

La borne faible-$L^3$ passe faible-étoile si elle est uniforme, mais elle ne
fournit pas les hypothèses compactes du lemme. Il reste ensuite deux portes.

1. **Rigidité de la vitesse.** L'autonomie et l'unicité classique donnent
   automatiquement une vitesse de groupe constante pour un équilibre relatif.
   Dans la classe faible suitable, le lemme distributionnel à axe fixe du cycle
   0055 donne seulement l'alternative : $\beta$ est constante, ou
   $\mathcal RV=0$ (stabilisateur). Cette étape n'est pas publiée dans le cadre
   exact faible-$L^3$ audité.

2. **Non-trivialité.** Ni la compacité locale ni la réduction de phase
   n'empêchent $V\equiv0$. Il faut une concentration persistante, une
   normalisation compacte ou un module de trace distinct.

Même ce lemme conditionnel ne produit pas une RDSS générale : (9) demande une
compacité des translations temporelles et des paramètres $(S_n,\phi_n)$, pas
l'annulation du défaut tangent (1).

## 6. Tests adverses reproductibles

### Test A - une borne du défaut ne l'annule pas

Prendre une solution lisse non stationnaire de (5) sur une fenêtre compacte,
poser $V_n=V$, $\beta_n=0$. Alors $D_n=\partial_sV$ est borné dans toute norme
locale compatible avec la régularité, mais la limite n'est pas une orbite RSS.
Plus généralement, toute extraction de (1) ne donne que
$D_n\rightharpoonup D$.

**Résidu analytique :** la conclusion RSS exige $D=0$, information absente de
l'hypothèse « borné ». Ce test réfute le maillon sur les fenêtres locales; il ne
prétend pas construire une solution ancienne singulière.

### Test B - deux convergences faibles ne ferment pas un produit

Sur $I=(0,2\pi)$, prendre $a_n=b_n=\sin(ns)$. Alors

\[
 a_n\stackrel *\rightharpoonup0,qquad
 b_n\stackrel *\rightharpoonup0\quad\hbox{dans }L^\infty(I),
 \qquad a_nb_n\rightharpoonup\frac12.                              \tag{20}
\]

**Résidu analytique :** une convergence forte d'un facteur est indispensable
dans (17). Remplacer la forte compacité de $V_n$ par une seconde convergence
faible invalide (19).

### Test C - dégénérescence de la jauge près d'un stabilisateur

Dans un espace de Hilbert de profils, poser $U_n=U_{\rm sym}+\varepsilon_nW$
avec $\mathcal RU_{\rm sym}=0$, $\mathcal RW\ne0$ et
$\varepsilon_n\downarrow0$. La matrice de Gram de la direction de groupe
vérifie

\[
 \|\mathcal RU_n\|^2=\varepsilon_n^2\|\mathcal RW\|^2.             \tag{21}
\]

Chaque profil peut avoir un stabilisateur trivial, tandis que la constante de
l'inverse dans (11) diverge comme $\varepsilon_n^{-2}$.

**Résidu analytique :** l'hypothèse qualitative de Beyn--Thümmler ne donne pas
la borne uniforme (12). La faible-$L^3$ ne détecte pas cette transversalité.

### Test D - perte de non-trivialité par translation

Pour un champ solénoïdal $U\in C_c^\infty(\mathbb R^3)$,
$U_n(y)=U(y-ne_1)$ conserve sa norme $L^{3,\infty}$ mais converge vers zéro
sur tout compact.

**Résidu analytique :** une limite compacte et même suitable peut être nulle;
une phase de rotation ne corrige pas une fuite translationnelle ou
multi-échelle.

### Test E - RDSS n'est pas RSS

Un profil $W(s)$ périodique et non constant dans le quotient peut satisfaire
$W(s+S)=W(s)$, donc donner (9) après reconstruction, tout en ayant
$\partial_sW$ non tangent à l'orbite de rotation.

**Résidu analytique :** un critère basé sur (1) ne doit pas annoncer une
classification RDSS sans une hypothèse séparée de périodicité modulo groupe.

## 7. Passe contradictoire des quantificateurs

1. **Borné / petit / nul.** Ces trois propriétés du défaut ne sont pas
   interchangeables. Seule la convergence vers zéro identifie une orbite
   exacte à la limite.
2. **Chaque profil / uniformément dans la suite.** Un stabilisateur trivial
   point par point ne contrôle pas uniformément l'inverse de la condition de
   phase.
3. **Faible-$L^3$ spatial / fort $L^3$ espace--temps.** Le premier est une
   borne critique; le second est la topologie qui ferme le terme quadratique et
   l'énergie locale.
4. **Solution adaptée / solution faible $L^{3,\infty}$ de BSS.** La seconde
   inclut une scission calorique et un correcteur énergétique; ce n'est pas un
   synonyme de la première.
5. **Forward / backward ancienne.** Une stabilité à temps initial fixe ne se
   transfère pas sans uniformité lorsque le temps initial recule.
6. **Orbites exactes / orbites approchées.** Bradshaw--Tsai et Pineau--Vicol
   supposent la covariance RSS/RDSS avant leur analyse; ils ne la produisent
   pas par compacité.
7. **Lisse Type I / suitable faible-$L^3$.** La borne ponctuelle
   $|u(x,t)|\lesssim(|x|+\sqrt{-t})^{-1}$ implique une borne faible-$L^3$,
   mais la réciproque est fausse.
8. **Compacité / persistance.** Une convergence locale forte n'empêche ni la
   fuite à l'infini, ni la perte de masse au temps terminal.
9. **Vitesse bornée / phase compacte.** Une borne de $\beta_n$ donne une
   compacité faible-étoile; sans normalisation de la phase initiale, les phases
   elles-mêmes ne sont définies qu'à une constante du groupe près.
10. **Pression de Poisson / pression locale contrôlée.** La partie harmonique
    doit être normalisée; l'équation
    $-\Delta P=\partial_i\partial_j(V_iV_j)$ ne suffit pas localement.

## 8. Recherche d'absence bornée

La recherche a couvert, jusqu'au 15 août 2026 :

- les pages éditeur et textes primaires associés aux DOI de Simon,
  Beyn--Thümmler, Rowley et al., O'Neil, Barker--Seregin--Šverák,
  Albritton--Barker, Bradshaw--Tsai et Chae--Wolf;
- la notice et le texte `arXiv:2607.09619v2` de Pineau--Vicol;
- les chaînes de références sur *freezing method*, *phase condition*,
  *reconstruction equation*, *relative equilibrium*, *self-similar dynamical
  systems*, *weak-star stability*, *suitable weak solution*, *rotated
  self-similar*, *modulated defect* et *compactness*;
- des requêtes croisées ciblant explicitement « Navier--Stokes + phase
  reconstruction/relative equilibrium + suitable weak/weak $L^3$ » et
  « rotated self-similar + compactness/modulated defect ».

Une recherche négative n'est jamais une preuve d'inexistence absolue. Le
verdict est borné aux index consultables et aux chaînes de références de ces
sources. Toutefois, aucune source retournée ne contient simultanément les six
éléments suivants :

\[
 \begin{array}{c}
 \text{Navier--Stokes 3D incompressible backward}\ +\
 \text{solution suitable}\ +\ L^\infty_sL^{3,\infty}_y\ +\
 \text{défaut modulé tendant vers zéro}\ +\
 \text{reconstruction de phase compacte}\ +\
 \text{conclusion RSS/RDSS exacte}.
 \end{array}                                                        \tag{22}
\]

A fortiori, aucune ne prouve cette conclusion sous la seule **borne** du
défaut.

## 9. Traçabilité des PDF audités

| PDF primaire | Vérification | SHA256 |
|---|---|---|
| Beyn--Thümmler, prépublication institutionnelle correspondant à l'article SIAM 2004 | texte intégral; contrôle visuel des pages 7 et 9, th. 2.9, prop. 2.10 et condition adaptative | `240522FAE2761F879B7E406D62D5337EF06C271F10E88D72BA1D11455D60909D` |
| Barker--Seregin--Šverák, PDF éditeur 2018 | texte intégral; contrôle visuel de la page 631 (th. 1.2) et de la page 644 (3.46--3.50) | `1C3FD9544009A62D310B1D379866D920E4366C8FC41D4E6F8FB2C5A6F02D99FC` |
| Simon, PDF éditeur 1987, audit du cycle 0045 réutilisé | cor. 4 vérifié | `86B81EB6BE3BE81AFD97FD43F185F63929F552FDAAAF13EE7A9D89F6483A3DB3` |
| Bradshaw--Tsai, `arXiv:1610.05680v1`, audit du cycle 0055 réutilisé | définitions et repère tournant vérifiés | `DE297541695B1E52AEE702930F8C5F723EFFC5DB13FA208B80CBAD7EFEE47C52` |
| Pineau--Vicol, `arXiv:2607.09619v2`, audit du cycle 0055 réutilisé | théorèmes 1.4, 1.7 et remarque 1.8 vérifiés | `379591AA3C1036C9140702EBE71AAAB309FE207439A57DB5CEFF893F15D0AE8E` |

Les empreintes certifient seulement l'identité des octets relus, non la vérité
des théorèmes. Le premier téléchargement institutionnel Beyn--Thümmler a
présenté une chaîne de certificat incomplète; le même fichier primaire a été
récupéré explicitement sans validation de cette chaîne, puis son DOI, ses
métadonnées éditeur, son texte et ses pages décisives ont été contrôlés
séparément. Cette limite de transport est consignée.

## Décision scientifique

**État : CONTINUER, après révision de l'hypothèse active.** Abandonner toute
formulation « défaut modulé borné $\Rightarrow$ RSS ». Le prochain test doit
viser le lemme conditionnel de la section 5 avec un défaut **vanishing**, une
borne uniforme des vitesses de phase et les estimations (13). Il doit échouer
explicitement si l'une des trois quantités suivantes diverge :

\[
 \|P_n-(P_n)_B\|_{L^{3/2}},\qquad
 \|\beta_n\|_{L^\infty(I)},\qquad
 \lambda_{\min}(S_n^*S_n)^{-1}.                                    \tag{23}
\]

Même en cas de succès, la conservation de la non-trivialité reste un lemme
indépendant. Les théorèmes RSS/RDSS de rigidité ne doivent être invoqués
qu'après obtention d'une covariance exacte dans leur classe de régularité.
