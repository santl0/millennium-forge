# Cycle 0060 — moyenne de Haar et transfert de Reynolds signé

Date d'exécution : 2026-08-15

## Verdict

Il existe des champs explicites

\[
V,W\in\mathcal S(\mathbb R^3;\mathbb R^3)
\]

tels que :

\[
\nabla\cdot V=\nabla\cdot W=0,
\]

\[
V\text{ est invariant sous SO(2) autour de }e_3,
\]

\[
\mathsf HW=0,
\]

mais

\[
\boxed{
T(V,W)
:=
\int_{\mathbb R^3}(W\otimes W):\nabla V\,dx
=-\frac8{27}\left(\frac{\pi}{3}\right)^{3/2}\ne0.}
\tag{1}
\]

De plus,

\[
T(-V,W)=-T(V,W)>0.
\tag{2}
\]

L'axisymétrie du champ moyen et l'annulation de la moyenne de Haar de la fluctuation n'imposent donc ni annulation ni signe au transfert quadratique.

Ces champs sont des tests statiques de Schwartz. Ils ne sont pas présentés comme des solutions de Navier–Stokes.

## 1. Définition exacte des champs

Posons

\[
G(x,y,z)=e^{-(x^2+y^2+z^2)}
\]

et choisissons les potentiels vecteurs

\[
A_V=zG(-y,x,0),
\qquad
A_W=xG(0,0,1).
\tag{3}
\]

Définissons

\[
V=\nabla\times A_V,
\qquad
W=\nabla\times A_W.
\tag{4}
\]

Le calcul exact donne

\[
V
=G\left(
-x+2xz^2,\,
-y+2yz^2,\,
2z-2x^2z-2y^2z
\right),
\tag{5}
\]

\[
W
=G\left(
-2xy,\,
2x^2-1,\,
0
\right).
\tag{6}
\]

Chaque composante est un polynôme multiplié par une gaussienne. Les deux champs appartiennent donc à la classe de Schwartz ; ils sont en particulier lisses et rapidement décroissants avec toutes leurs dérivées.

Comme ils sont construits par rotationnel,

\[
\nabla\cdot V=\nabla\cdot W=0.
\tag{7}
\]

Le script ne se contente pas d'invoquer cette identité : il recalcule les rotationnels en dérivant exactement les facteurs polynomial–gaussiens, puis vérifie que les deux polynômes de divergence sont identiquement nuls.

## 2. Action SO(2) et moyenne de Haar

Pour la rotation \(Q_\theta\) autour de \(e_3\), l'action sur un champ est

\[
(\rho_\theta U)(x)=Q_\theta U(Q_{-\theta}x).
\tag{8}
\]

Le potentiel \(A_V\) est invariant : \(G\) et \(z\) sont invariants, tandis que

\[
Q_\theta\bigl(-(Q_{-\theta}x)_2,(Q_{-\theta}x)_1,0\bigr)
=(-y,x,0).
\]

Le rotationnel commute avec les rotations, donc

\[
\rho_\theta V=V
\]

pour tout \(\theta\). Ainsi \(V\) est exactement axisymétrique, avec swirl dans le potentiel et composantes poloidales dans (5).

Pour \(A_W\),

\[
\rho_\theta A_W
=G(x\cos\theta+y\sin\theta)e_3.
\]

Sa moyenne angulaire est nulle :

\[
\frac1{2\pi}\int_0^{2\pi}\rho_\theta A_W\,d\theta=0.
\]

Par équivariance du rotationnel,

\[
\boxed{\mathsf HW=0.}
\tag{9}
\]

Le certificat donne aussi une vérification infinitésimale indépendante. Si \(\mathcal A\) est le générateur de (8), alors

\[
\mathcal AV=0,
\qquad
\mathcal A^2W=-W.
\tag{10}
\]

La première identité certifie l'invariance. Pour la seconde, la projection de Haar \(\mathsf H\) commute avec \(\mathcal A\), tandis que \(\mathcal A\mathsf HW=0\). En appliquant \(\mathsf H\) à \(\mathcal A^2W=-W\), on obtient

\[
0=-\mathsf HW.
\]

Le script vérifie enfin l'invariance de \(V\) et l'annulation de la moyenne de \(W\) sur les quatre quarts de tour. Cette dernière vérification finie est un contrôle supplémentaire ; la conclusion Haar complète provient de (9) ou (10), pas de la seule moyenne cyclique.

## 3. Calcul exact du transfert

Nous utilisons la convention

\[
(W\otimes W):\nabla V
=
\sum_{i,j=1}^3W_iW_j\,\partial_jV_i.
\tag{11}
\]

Puisque chaque \(W_i\) porte un facteur \(G\) et chaque \(\partial_jV_i\) un facteur \(G\), l'intégrande vaut

\[
P(x,y,z)e^{-3(x^2+y^2+z^2)},
\]

où le polynôme exact est

\[
\begin{aligned}
P={}&-1+2z^2+2y^2-4y^2z^2+4x^2-8x^2z^2\\
&-4x^2y^2+8x^2y^2z^2-4x^4+8x^4z^2.
\end{aligned}
\tag{12}
\]

Les moments impairs s'annulent. Pour \(k\ge0\),

\[
\frac{\displaystyle\int_{\mathbb R}x^{2k}e^{-3x^2}\,dx}
{\sqrt{\pi/3}}
=
\frac{(2k-1)!!}{6^k}.
\tag{13}
\]

Le produit tensoriel des trois moments réduit donc l'intégrale à une somme rationnelle. Le script obtient

\[
\frac{T(V,W)}{(\pi/3)^{3/2}}
=-\frac8{27},
\]

ce qui prouve (1) sans approximation flottante.

Le transfert est linéaire en \(V\). Le certificat recalcule néanmoins tout le polynôme pour \(-V\) et vérifie

\[
P_{-V,W}=-P_{V,W},
\qquad
\frac{T(-V,W)}{(\pi/3)^{3/2}}
=\frac8{27}.
\]

## 4. Conclusion adverse

Ce calcul falsifie les implications non assorties d'hypothèses supplémentaires :

\[
V\text{ axisymétrique et }\mathsf HW=0
\;\not\Longrightarrow\;
T(V,W)=0,
\]

et

\[
V\text{ axisymétrique et }\mathsf HW=0
\;\not\Longrightarrow\;
T(V,W)\ge0
\quad\text{ou}\quad
T(V,W)\le0.
\]

La moyenne de Haar annule le mode linéaire \(W\), mais pas nécessairement le tenseur invariant de Reynolds \(\mathsf H(W\otimes W)\). C'est ce tenseur quadratique qui se contracte avec \(\nabla V\).

Toute tentative de coercivité doit donc contrôler au moins l'un des objets suivants :

- la structure tensorielle de \(\mathsf H(W\otimes W)\) ;
- la partie symétrique de \(\nabla V\) ;
- une orthogonalité quadratique plus forte que \(\mathsf HW=0\) ;
- une identité dynamique propre aux solutions considérées.

## 5. Séparation stricte avec Navier–Stokes

Les champs (5) et (6) satisfont exactement incompressibilité et décroissance rapide, mais ce sont des champs tests statiques. Aucun \(u(t,x)\), aucune pression et aucune force ne sont construits. Le calcul n'établit :

- ni l'équation de quantité de mouvement ;
- ni une identité d'énergie le long d'une solution ;
- ni une estimation uniforme temporelle ;
- ni un raccord à une solution de Leray–Hopf, suitable, forte ou classique ;
- ni régularité globale, ni blow-up.

Le résultat négatif est limité mais exact : la symétrie linéaire et la moyenne de Haar n'imposent pas à elles seules un signe au transfert de Reynolds.

## 6. Reproduction et artefacts

Commande :

~~~powershell
python -B experiments/navier-stokes/haar-reynolds-transfer/haar_reynolds_transfer.py
git diff --check
~~~

Sortie validée :

~~~text
haar_reynolds_transfer: PASS
exact_assertions=20
regularity=polynomial_times_exp(-|x|^2)_is_Schwartz
divergence=div(V)=div(W)=0_exact
symmetry=SO2_generator(V)=0_and_generator^2(W)=-W
haar=Haar(W)=0
transfer=T=-(8/27)*(pi/3)^(3/2)_nonzero
sign_flip=T(-V,W)=-T(V,W)
field_sha256=5123d2008f8b1fe4196c01e3c181dc090ad3b90cc1148d2361cbbcb3464e4437
seed=n/a; arithmetic=Fraction; no Navier-Stokes PDE claim
sha256_self=2295e890391f8ed34044a1e35ca16a90748f27743ea0a081a677ff590df5fc50
~~~

Artefacts :

- script : experiments/navier-stokes/haar-reynolds-transfer/haar_reynolds_transfer.py ;
- protocole : experiments/navier-stokes/haar-reynolds-transfer/README.md ;
- résultat machine : experiments/navier-stokes/haar-reynolds-transfer/results.json.

Les 20 assertions portent sur des égalités de polynômes entiers ou rationnels, des moments gaussiens rationnels normalisés et deux non-annulations exactes. Graine : non applicable.

Validation de propreté exécutée :

~~~text
git_diff_check=PASS
~~~

Empreinte SHA-256 du script :

~~~text
2295e890391f8ed34044a1e35ca16a90748f27743ea0a081a677ff590df5fc50
~~~

Empreinte SHA-256 du contenu polynomial canonique :

~~~text
5123d2008f8b1fe4196c01e3c181dc090ad3b90cc1148d2361cbbcb3464e4437
~~~

## Décision

**CONSERVER** ce contre-modèle comme réfutation exacte d'une coercivité issue de la seule moyenne de Haar. **RÉVISER** tout lemme de transfert pour porter sur \(\mathsf H(W\otimes W)\) ou sur une structure dynamique plus forte. Aucune revendication PDE.
