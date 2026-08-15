# Cycle 0059 — phase hilbertienne canonique, Gram dégénéré et dérive du stabilisateur

Date d'exécution : 2026-08-15

## Verdict

Dans un espace de Hilbert réel, la décomposition canonique d'une dérivée \(d\) suivant la tangente de groupe \(g\ne0\) est

\[
\boxed{
\beta=\frac{\langle d,g\rangle}{\langle g,g\rangle},
\qquad
r=d-\beta g.}
\tag{1}
\]

Elle vérifie exactement

\[
\langle r,g\rangle=0,
\tag{2}
\]

\[
\|d\|^2=\|\beta g\|^2+\|r\|^2,
\tag{3}
\]

et

\[
\|\beta g\|\le\|d\|.
\tag{4}
\]

Cette jauge contrôle la composante tangentielle \(\beta g\), pas le coefficient \(\beta\) lorsque le Gram \(\|g\|^2\) dégénère. Elle ne contrôle pas non plus la composante de \(r\) appartenant au stabilisateur \(\ker R\).

Un modèle SO(2) exact satisfait simultanément

\[
\beta_N\to\infty,
\qquad
\|g_N\|\to0,
\qquad
\|\beta_Ng_N\|\to0,
\]

mais

\[
\operatorname{Haar}(r_N)=e_0\ne0.
\]

La modulation rapide peut donc s'effondrer dans le plan tournant tandis qu'une dynamique non stationnaire persiste dans \(\ker R\).

Tous les calculs sont rationnels et de dimension finie. Aucune affirmation Navier–Stokes n'en est déduite.

## 1. Projection hilbertienne canonique

Soient \(H\) un espace de Hilbert réel, \(d,g\in H\), et \(g\ne0\). Pour tout \(\alpha\in\mathbb R\),

\[
d-\alpha g
=
r+(\beta-\alpha)g.
\]

Par (2), les deux termes du membre droit sont orthogonaux. Il vient

\[
\|d-\alpha g\|^2
=
\|r\|^2+(\alpha-\beta)^2\|g\|^2.
\tag{5}
\]

Ainsi, \(\beta\) est l'unique minimiseur de

\[
\alpha\longmapsto\|d-\alpha g\|^2.
\]

Le choix \(\alpha=0\) dans (5) donne (3) et (4). Le coefficient canonique est donc une projection orthogonale, non une estimation issue de la seule grandeur de la vitesse.

### Certificat rationnel général

Le script parcourt exactement :

- les dimensions \(2,\ldots,6\) ;
- les dénominateurs \(2,\ldots,13\) ;
- cinq décalages déterministes ;
- cinq compétiteurs rationnels \(\alpha\) pour chaque paire \((d,g)\).

Sur chacune de ces grilles dans \(\mathbb Q^m\), il vérifie :

- \(g\ne0\) ;
- la formule (1) ;
- l'orthogonalité (2) ;
- la reconstruction \(d=\beta g+r\) ;
- Pythagore (3) ;
- la contraction (4) ;
- l'identité de minimisation (5).

Aucune approximation flottante n'intervient.

## 2. Dégénérescence du Gram

Dans \(\mathbb Q^3\), fixons

\[
g_N=\varepsilon_Ne_1,
\qquad
\varepsilon_N=\frac1N,
\]

et décomposons

\[
d_N
=
\underbrace{e_1}_{\text{tangentielle}}
+
\underbrace{\frac23e_2-\frac35e_3}_{\text{transverse}}.
\]

Le Gram vaut

\[
\langle g_N,g_N\rangle
=\varepsilon_N^2
=\frac1{N^2}.
\]

La formule canonique donne

\[
\beta_N
=\frac{\varepsilon_N}{\varepsilon_N^2}
=N,
\]

et

\[
r_N=\frac23e_2-\frac35e_3.
\]

Par conséquent,

\[
\beta_N\to\infty,
\qquad
g_N\to0,
\]

alors que

\[
\beta_Ng_N=e_1
\]

reste borné et non nul. La composante transverse est entièrement placée dans le résidu et n'affecte pas \(\beta_N\).

Ce mécanisme est mal conditionné. Une perturbation tangentielle

\[
\delta d_N=\varepsilon_Ne_1
\]

vérifie

\[
\|\delta d_N\|=\frac1N\to0,
\]

mais change exactement le coefficient canonique de

\[
\delta\beta_N=1.
\]

Il n'existe donc aucune estimation uniforme de \(\beta\) en fonction de \(d\) lorsque \(\|g\|\to0\). La quantité stable est la projection \(\beta g\), conformément à (4).

À \(g=0\), le quotient (1) est indéfini. Le script traite ce cas comme une porte explicite et exige une erreur de division, plutôt que de choisir arbitrairement une vitesse.

## 3. Modèle SO(2) avec dérive dans le noyau

Décomposons

\[
H=\ker R\oplus P,
\]

où

\[
\ker R=\operatorname{span}\{e_0\},
\qquad
P=\operatorname{span}\{e_1,e_2\},
\]

et où le générateur de SO(2) agit par

\[
R(h,x,y)=(0,-y,x).
\]

Prenons l'action SO(2) standard

\[
Q_\theta=e^{\theta R},
\]

paramétrée par l'angle en radians et de période \(2\pi\). Pour \(N=2^m\), posons

\[
\varepsilon_N=\frac1{N^2}
\]

et considérons le chemin lisse abstrait

\[
Z_N(s)
=
s\,e_0+\varepsilon_NQ_{Ns}e_1,
\qquad
0\le s\le1.
\tag{6}
\]

Sa tangente de groupe est

\[
g_N(s)=RZ_N(s)
=
\varepsilon_NQ_{Ns}e_2,
\]

donc

\[
\|g_N(s)\|=\varepsilon_N=\frac1{N^2}.
\tag{7}
\]

La dérivée vaut

\[
d_N(s)=\partial_sZ_N(s)
=e_0+N g_N(s).
\tag{8}
\]

Comme \(e_0\perp g_N(s)\), la jauge canonique (1) fournit exactement

\[
\beta_N(s)=N,
\qquad
r_N(s)=e_0.
\tag{9}
\]

Nous avons donc

\[
\beta_N\to\infty,
\qquad
\|g_N\|=\frac1{N^2}\to0,
\qquad
\|\beta_Ng_N\|=\frac1N\to0.
\]

Soit \(\mathsf H\) la moyenne de Haar de l'action SO(2). Dans cette représentation, elle est la projection orthogonale sur \(\ker R\) :

\[
\mathsf H(h,x,y)=(h,0,0).
\]

Appliquée au résidu,

\[
\boxed{\mathsf Hr_N=e_0\ne0.}
\tag{10}
\]

De plus,

\[
\mathsf HZ_N(s)=s\,e_0,
\qquad
\partial_s(\mathsf HZ_N)=e_0.
\tag{11}
\]

La limite moyennée reste donc non stationnaire. Le collapse de la composante tournante ne peut pas éliminer une dérive dans le stabilisateur.

### Grille algébrique exacte

La trajectoire continue (6) contient des coefficients trigonométriques et n'est pas présentée comme un calcul rationnel. Sa différentiation et les identités (7)–(11) sont analytiques.

Le certificat rationnel échantillonne séparément :

\[
h_k=\frac{k}{4N},
\qquad
k=0,\ldots,4N,
\]

et les quatre états de quart de tour

\[
Q_{j\pi/2}e_1,
\qquad
j=0,1,2,3.
\]

Sur cette grille tensorielle, chaque profil \((h_k,\varepsilon_NQ_{j\pi/2}e_1)\), sa tangente \(g\) et la quantité \(d=e_0+Ng\) ont des coordonnées rationnelles. Cette grille ne prétend pas être une discrétisation temporelle rationnelle de \(\theta=Ns\) ; elle certifie les identités algébriques, indépendantes de la phase.

Sur sept échelles \(N=2,\ldots,128\), le script vérifie exactement :

- les analogues point par point de (7), (8) et (9) ;
- \(\langle r_N,g_N\rangle=0\) ;
- \(\mathsf Hr_N=\mathsf Hd_N=e_0\) ;
- \(\mathsf HZ=h_ke_0\) ;
- \(\|\beta_Ng_N\|^2=N^{-2}\) ;
- \(\mathsf HZ_N(1)-\mathsf HZ_N(0)=e_0\).

## 4. Implications et limites

Le certificat établit uniquement les implications algébriques suivantes :

1. hors de \(\ker R\), la phase canonique est l'unique projection hilbertienne ;
2. \(\beta g\) est contractivement contrôlé par \(d\) ;
3. \(\beta\) seul devient instable lorsque le Gram tend vers zéro ;
4. le résidu transverse à \(g\) peut contenir une composante dynamique non nulle dans \(\ker R\) ;
5. la moyenne de Haar commute avec cette dérive et ne la rend pas stationnaire.

Dans une application PDE, il faudrait encore préciser :

- l'espace de Hilbert et le domaine fermé du générateur \(R\) ;
- la régularité temporelle donnant \(d=\partial_sZ\) ;
- la compatibilité de la projection avec incompressibilité et pression ;
- la mesurabilité de \(\beta\) près du Gram nul ;
- l'uniformité des estimations sous troncature et passage à la limite ;
- un lemme séparé annulant ou contrôlant la composante \(\ker R\).

Le modèle ne contient ni convection, ni viscosité, ni projection de Leray, ni solution faible ou forte. Il ne prouve ni régularité ni blow-up pour Navier–Stokes.

## 5. Reproduction et certificat

Commande :

~~~powershell
python -B experiments/navier-stokes/canonical-hilbert-phase/canonical_phase_audit.py
~~~

Sortie validée :

~~~text
canonical_phase_audit: PASS
exact_assertions=37763
projection=beta=(d_dot_g)/(g_dot_g)_and_r=d-beta*g
orthogonality=r_dot_g=0_and_Pythagoras_exact
contraction=||beta*g||<=||d||
degenerate_Gram=g=epsilon*e1_beta=1/epsilon_transverse_residual_fixed
SO2=beta_to_infinity_g_to_zero_but_Haar(r)=e0
zero_Gram=canonical_beta_undefined
seed=n/a; arithmetic=Fraction; no Navier-Stokes PDE claim
~~~

Le script utilise uniquement la bibliothèque standard et **Fraction**. Les 37763 assertions sont exactes. Graine : non applicable.

Empreinte SHA-256 du script validé :

~~~text
e20050eecda07b8776b3a420a5b69b7a149c38bcb2117759330eb661109885b4
~~~

## Décision

**CONSERVER** la jauge hilbertienne canonique pour contrôler \(\beta g\). **ABANDONNER** toute conclusion uniforme sur \(\beta\) près du Gram nul. **RÉVISER** tout argument concluant à la stationnarité sans traiter séparément la projection de Haar du résidu.
