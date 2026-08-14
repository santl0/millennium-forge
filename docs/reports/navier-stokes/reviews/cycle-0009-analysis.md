# Revue d'analyse — cycle 0009

> **Correction de synthèse.** Dans cette note brute de sous-agent, les termes
> « terminal » ou « tranche terminale » appliqués à `s=0` désignent en réalité
> le temps-record `t_k`. Le temps physique `T` correspond à
> `B_k=M_k²(T-t_k)>0`. La synthèse canonique du cycle distingue ces horloges;
> cette note est conservée pour la traçabilité de la passe adverse.

## Verdict

Le verrou n'est pas la formule de changement d'échelle, mais un échange de quantificateurs. Une trace physique

\[
u(t)\longrightarrow 0\quad\text{dans }\mathcal D'(\mathbb R^3),\qquad t\uparrow T,
\]

contrôle chaque fonction test **fixe**. Le zoom maximum-normalisé de Koch–Nadirashvili–Seregin–Šverák (KNSS) exige au contraire de contrôler une suite de tests qui se concentre à l'échelle \(M_k^{-1}\) et se translate vers \(x_k\). La convergence dans \(\mathcal D'\), même jointe à une borne uniforme dans \(L^3\), ne transmet donc pas une trace nulle au profil limite.

Une hypothèse suffisante au niveau critique est l'équi-intégrabilité locale uniforme de \(|u(t_k)|^3\), ou plus précisément la non-concentration

\[
\forall R>0,\qquad
\|u(t_k)\|_{L^3(B(x_k,R/M_k))}\longrightarrow0.
\tag{NC3}
\]

Mais, pour la suite KNSS, (NC3) est incompatible avec \(|v_k(0,0)|=1\) et les estimations paraboliques uniformes. Ainsi, (NC3) est bien un critère excluant ce blow-up, et non une propriété disponible gratuitement au point singulier.

## Cadre exact

On considère une solution classique/mild incompressible de

\[
\partial_tu-\Delta u+(u\cdot\nabla)u+\nabla p=0,
\qquad \nabla\cdot u=0,
\]

sur \(\mathbb R^3\times[0,T)\), sans force et avec viscosité normalisée à \(1\). Dans la réduction KNSS d'une singularité en temps fini, on choisit \(t_k\uparrow T\), des points \(x_k\), et

\[
M_k=|u(x_k,t_k)|\longrightarrow\infty,
\]

puis

\[
v_k(y,s)=M_k^{-1}u\!\left(x_k+\frac{y}{M_k},
t_k+\frac{s}{M_k^2}\right).
\tag{1}
\]

La construction donne \(|v_k|\leq\gamma_k\) pour \(s\leq0\), \(\gamma_k\downarrow1\), et

\[
|v_k(0,0)|=1.
\tag{2}
\]

Après extraction, elle produit un profil ancien mild borné. C'est la construction de la proposition 6.1 et du lemme 6.1 de [Koch–Nadirashvili–Seregin–Šverák, *Liouville theorems for the Navier–Stokes equations and applications*, Acta Math. 203 (2009)](https://www-users.cse.umn.edu/~sverak/publications/liouville.pdf).

## Formule exacte du pairing

Soit \(\varphi\in C_c^\infty(\mathbb R^3;\mathbb R^3)\). Pour tout \(s\) appartenant au domaine de \(v_k\), avec

\[
\tau_{k,s}=t_k+\frac{s}{M_k^2},
\]

le changement de variable \(y=M_k(x-x_k)\), \(dy=M_k^3dx\), donne

\[
\begin{aligned}
\langle v_k(s),\varphi\rangle_y
&=M_k^{-1}\int_{\mathbb R^3}
u\!\left(x_k+\frac y{M_k},\tau_{k,s}\right)\cdot\varphi(y)\,dy\\
&=M_k^2\int_{\mathbb R^3}u(x,\tau_{k,s})\cdot
\varphi\bigl(M_k(x-x_k)\bigr)\,dx\\
&=\langle u(\tau_{k,s}),\Phi_k\rangle_x,
\end{aligned}
\tag{3}
\]

où

\[
\Phi_k(x)=M_k^2\varphi\bigl(M_k(x-x_k)\bigr).
\tag{4}
\]

Pour chaque \(k\), \(\Phi_k\) est une fonction test, mais la famille n'est pas bornée dans \(\mathcal D\) :

\[
\operatorname{supp}\Phi_k=x_k+M_k^{-1}\operatorname{supp}\varphi,
\qquad
\|\partial^\alpha\Phi_k\|_\infty
=M_k^{2+|\alpha|}\|\partial^\alpha\varphi\|_\infty.
\tag{5}
\]

De plus, pour \(1\leq q\leq\infty\),

\[
\|\Phi_k\|_{L^q}=M_k^{2-3/q}\|\varphi\|_{L^q}.
\tag{6}
\]

En particulier \(\|\Phi_k\|_{3/2}=\|\varphi\|_{3/2}\), ce qui exhibe exactement le caractère critique de \(L^3\). Si \(x_k\to\infty\), la trace distributionnelle physique perd en plus la concentration par fuite spatiale.

Les fonctions \(\varphi\) et \(\Phi_k\) sont des **champs tests**, pas des solutions de Navier–Stokes. La définition usuelle de \(\mathcal D'\) autorise tout test vectoriel compactement supporté. Si l'on travaille dans le quotient solénoïdal, choisir \(\nabla\cdot\varphi=0\) préserve cette propriété dans (4) et ne supprime pas l'obstruction.

## Les deux limites qui ne commutent pas

La trace du profil ancien est

\[
A(\varphi)=\lim_{s\uparrow0}\lim_{k\to\infty}
\langle v_k(s),\varphi\rangle,
\tag{7}
\]

tandis que la tranche terminale des approximants correspond à

\[
B(\varphi)=\lim_{k\to\infty}\langle v_k(0),\varphi\rangle
=\lim_{k\to\infty}\langle u(t_k),\Phi_k\rangle.
\tag{8}
\]

Ni la convergence locale de \(v_k(s)\) pour chaque \(s<0\), ni la continuité temporelle de chaque \(v_k\) séparément n'impliquent \(A=B\). Une condition suffisante abstraite et directement vérifiable est :

1. \(v_k(s)\to v(s)\) dans \(\mathcal D'\) pour chaque \(s<0\) fixé ;
2. \(v_k(0)\to0\) dans \(\mathcal D'\) ;
3. pour tout \(\varphi\in C_c^\infty\),
   \[
   \lim_{s\uparrow0}\sup_k
   |\langle v_k(s)-v_k(0),\varphi\rangle|=0.
   \tag{UT}
   \]

Alors

\[
|\langle v(s),\varphi\rangle|
\leq\limsup_k|\langle v_k(s)-v_k(0),\varphi\rangle|,
\]

et \(v(s)\to0\) dans \(\mathcal D'\) quand \(s\uparrow0\). La condition (UT) découle par exemple d'une équicontinuité temporelle locale uniforme des \(v_k\) jusqu'à \(s=0\). Pour des solutions mild uniformément bornées sur un intervalle commun \([-\delta,0]\), les estimations paraboliques après redémarrage à un temps négatif fixe fournissent une telle compacité terminale.

Le véritable maillon manquant est donc généralement le point 2, non (UT).

## Hypothèses concrètes suffisantes pour la tranche terminale

Si \(\operatorname{supp}\varphi\subset B_R\), Hölder et (3) donnent

\[
|\langle v_k(0),\varphi\rangle|
\leq
M_k^{3/p-1}
\|u(t_k)\|_{L^p(B(x_k,R/M_k))}
\|\varphi\|_{L^{p'}},
\tag{9}
\]

où \(1/p+1/p'=1\). Il en résulte les conditions suffisantes suivantes.

| Contrôle physique | Condition suffisante pour \(v_k(0)\to0\) localement dans \(\mathcal D'\) | Statut d'échelle |
|---|---|---|
| \(p>3\) | \(\sup_k\|u(t_k)\|_{L^p}<\infty\) | le facteur \(M_k^{3/p-1}\to0\) |
| \(p=3\) | (NC3), ou équi-intégrabilité uniforme de \(|u(t_k)|^3\) | critique ; une simple borne \(L^3\) ne suffit pas |
| \(p=2\) | \(M_k^{1/2}\|u(t_k)\|_{L^2(B(x_k,R/M_k))}\to0\) | équivaut à \(M_k\int_{B(x_k,R/M_k)}|u|^2\to0\) |
| trace forte \(L^3\) | \(u(t_k)\to u_T\) fortement dans \(L^3\) | implique (NC3) par absolue continuité de l'intégrale |

La formulation la plus faible adaptée au zoom est simplement la convergence des pairings de (8). (NC3) est une hypothèse concrète, critique et indépendante du test ; elle est plus exploitable dans une preuve PDE.

Une convergence faible dans \(L^3\), une borne globale dans \(L^3\), ou une trace dans \(\mathcal D'\) sans taux ne suffit pas. Dans un espace négatif, il faudrait une vitesse de convergence compensant la croissance des semi-normes de \(\Phi_k\) dans (5).

## Contre-profil reproductible au niveau des champs

Prenons un champ \(w\in C_c^\infty(\mathbb R^3;\mathbb R^3)\), divergence-free, tel que

\[
\|w\|_\infty=|w(0)|=1.
\]

Un tel champ s'obtient en prenant le rotationnel d'un potentiel compactement supporté non nul, puis en translatant un point de maximum et en normalisant. Pour \(M_k\to\infty\), posons

\[
U_k(x)=M_kw(M_kx).
\tag{10}
\]

Alors

\[
\nabla\cdot U_k=0,
\qquad \|U_k\|_3=\|w\|_3,
\qquad |U_k(0)|=M_k.
\]

Pour toute fonction test physique fixe \(\psi\),

\[
|\langle U_k,\psi\rangle|
\leq M_k^{-2}\|w\|_1\|\psi\|_\infty\longrightarrow0.
\tag{11}
\]

Ainsi \(U_k\to0\) dans \(\mathcal D'\), avec borne critique \(L^3\). Pourtant son zoom maximum-normalisé est exactement

\[
M_k^{-1}U_k(y/M_k)=w(y),
\tag{12}
\]

qui est non nul et vaut \(1\) à l'origine. Cela réfute l'implication fonctionnelle

\[
\bigl[U_k\to0\text{ dans }\mathcal D',\ \sup_k\|U_k\|_3<\infty\bigr]
\Longrightarrow
\bigl[v_k\to0\text{ dans }\mathcal D'\bigr].
\]

Limite essentielle : les \(U_k\) de (10) sont des champs divergence-free admissibles comme données, mais ne sont pas démontrés être les tranches temporelles d'une **même** solution de Navier–Stokes approchant son temps maximal. Ils réfutent le passage fonctionnel proposé ; ils ne construisent pas un blow-up Navier–Stokes.

## Compatibilité avec la normalisation ponctuelle

La seule condition \(|v_k(0,0)|=1\) est compatible avec \(v_k(0)\to0\) dans \(\mathcal D'\) : des pics de largeur décroissante peuvent conserver leur valeur ponctuelle et disparaître distributionnellement.

Elle cesse de l'être dès que la suite possède un module spatial uniforme. Supposons

\[
\sup_k\|\nabla v_k(0)\|_\infty\leq L<\infty.
\tag{13}
\]

Après extraction, \(e_k=v_k(0,0)\to e\), \(|e|=1\). Pour \(k\) assez grand et \(|y|\leq r\), avec \(r>0\) choisi en fonction de \(L\),

\[
e\cdot v_k(y,0)\geq\frac12.
\tag{14}
\]

Une fonction \(\eta\geq0\), non nulle, supportée dans \(B_r\), et le test fixe \(\varphi=e\eta\) donnent alors

\[
\langle v_k(0),\varphi\rangle
\geq\frac12\int\eta>0.
\tag{15}
\]

Donc \(v_k(0)\not\to0\) dans \(\mathcal D'\). Les bornes KNSS \(|v_k|\leq\gamma_k\) sur un intervalle passé commun, combinées au lissage mild, fournissent précisément des estimations dérivées uniformes au temps terminal. C'est pourquoi la construction conserve une limite non triviale avec \(|v(0,0)|=1\).

On peut exprimer la même contradiction dans \(L^3\) : (13) et (2) imposent une masse \(L^3\) positive sur une boule fixe en variables \(y\), donc

\[
\liminf_k\|u(t_k)\|_{L^3(B(x_k,r/M_k))}>0,
\tag{16}
\]

ce qui contredit (NC3).

## Audit des quantificateurs et de la circularité \(L^3\)

1. **Test fixe contre test mobile.** La trace distributionnelle dit
   \(\forall\psi\in\mathcal D,\ \langle u(t),\psi\rangle\to0\). Elle ne dit pas
   \(\langle u(t_k),\Phi_k\rangle\to0\) pour une suite \(\Phi_k\).

2. **Absolue continuité non uniforme.** Pour chaque \(k\) et \(\varepsilon\), l'intégrabilité de \(|u(t_k)|^3\) fournit un rayon \(r_{k,\varepsilon}\). Le zoom requiert un rayon valable uniformément en \(k\). L'inversion
   \[
   \forall k\ \exists r_{k,\varepsilon}
   \quad\not\Rightarrow\quad
   \exists r_\varepsilon\ \forall k
   \]
   est précisément la possibilité de concentration critique.

3. **Borne \(L^3\) contre compacité \(L^3\).** La borne \(\sup_k\|u(t_k)\|_3<\infty\) est invariante d'échelle et le contre-profil (10) la sature. L'utiliser comme si elle impliquait (NC3) réintroduit illicitement la compacité manquante.

4. **Trace forte circulaire.** Supposer une trace forte dans \(L^3\) donne bien (NC3), mais constitue déjà une information de continuation critique. Dans une tentative de redémontrer la régularité endpoint \(L^3\), cette hypothèse absorbe le verrou au lieu de le résoudre.

5. **Temps fixé contre limite diagonale.** La convergence de \(v_k(s)\) pour chaque \(s<0\) et la continuité de chaque \(v_k\) en \(s=0\) ne donnent pas (UT) sans module uniforme.

6. **Translation à l'infini.** Si \(|x_k|\to\infty\), tout test physique fixe peut manquer le paquet concentré. La recentration du zoom annule cette fuite ; une trace dans \(\mathcal D'_{\mathrm{loc}}\) ne la voit pas.

7. **Champ divergence-free contre solution.** Les identités (3)–(6) et le contre-profil (10) sont cinématiques. Les estimations dérivées, la compacité temporelle et la relation entre différentes tranches sont dynamiques et nécessitent réellement l'équation de Navier–Stokes.

## Lemme falsifiable retenu

**Lemme de transmission terminale conditionnelle.** Soit \(v_k\) la suite maximum-normalisée (1), convergeant vers \(v\) sur tout compact de \(\mathbb R^3\times(-\infty,0)\). Supposons (UT) et (NC3). Alors

\[
v(s)\longrightarrow0\quad\text{dans }\mathcal D'(\mathbb R^3)
\quad\text{quand }s\uparrow0.
\]

Si, de plus, les bornes mild donnent (13), les hypothèses sont incompatibles avec (2). Par conséquent, toute singularité produisant un profil KNSS doit porter une quantité \(L^3\) uniformément positive dans au moins une boule de rayon comparable à \(M_k^{-1}\), comme dans (16).

Ce lemme est exact mais conditionnel. Il ne ferme pas le problème Clay : le verrou restant est de déduire ou de contredire (NC3) à partir d'une quantité contrôlée par les équations, sans supposer la régularité critique recherchée.

## Résultat de la passe contradictoire

- La formule (3) a été vérifiée avec le jacobien \(M_k^3\) et l'amplitude \(M_k^{-1}\) ; le facteur final est bien \(M_k^2\).
- Le test critique est bien \(L^{3/2}\), dont la norme est invariante dans (6).
- La trace distributionnelle physique seule est réfutée par le contre-profil explicite (10)–(12).
- La non-trivialité ponctuelle seule ne réfute pas une limite distributionnelle nulle ; l'estimation uniforme (13) est indispensable.
- Aucune propriété d'une famille arbitraire de champs n'a été promue en propriété d'une trajectoire Navier–Stokes.
- Aucune exclusion de profil auto-similaire n'est utilisée et aucune conclusion de régularité globale n'est revendiquée.

**État : CONTINUER.** Prochaine expérience décisive : chercher une quantité effectivement propagée par Navier–Stokes qui implique une version quantitative de (NC3), ou construire un paquet divergence-free multi-échelle saturant simultanément l'énergie, la borne mild normalisée et la pression non locale afin de réfuter une candidate précise.
