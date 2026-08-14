# Revue bibliographique contradictoire — cycle 0011

Date de la veille : 2026-08-14
Périmètre : projecteurs de Riesz, modes instables, constantes de semi-groupe, quantificateurs de séparation et stabilité sous désingularisation intérieure dans Hou–Wang–Yang, Jia–Šverák, Albritton–Brué–Colombo et Ionescu–Jia–Palasek.

## Verdict différentiel

La veille primaire ne fournit aucun maillon nouveau reliant la construction de Hou–Wang–Yang à des données initiales lisses du problème Clay non forcé. Hou–Wang–Yang certifient par ordinateur un profil auto-similaire exact et au moins un mode propre droit instable, puis démontrent analytiquement une famille de solutions faibles de Leray–Hopf pour une donnée compacte mais singulière à l’origine. Ils n’enferment pas un mode propre adjoint exact, la multiplicité algébrique de la valeur propre, la norme d’un projecteur spectral, ni une constante positive de séparation uniforme lorsque le rayon de coupure extérieure tend vers l’infini.

Ionescu–Jia–Palasek, postérieur à Hou–Wang–Yang, écrit explicitement le projecteur de Riesz sur tout le sous-espace instable et une formule de variété instable, mais son profil et son mode propre restent une conjecture appuyée par un calcul flottant de haute précision. Ce travail ne certifie ni adjoint, ni norme du projecteur, ni désingularisation intérieure. Jia–Šverák donne le prototype analytique conditionnel, tandis qu’Albritton–Brué–Colombo donne une construction analytique publiée avec un mode instable et des semi-groupes, mais pour Navier–Stokes forcé.

Le premier test falsifiable à haute valeur informationnelle est donc un certificat adjoint–projecteur autour du profil exact de Hou–Wang–Yang. Il doit enfermer un mode propre adjoint, prouver la simplicité algébrique, séparer un contour du reste du spectre et majorer la condition du projecteur. Ce test quantifierait réellement la séparation des branches à rayon fixé. Il ne résoudrait toutefois pas l’obstacle distinct de la singularité initiale en \(1/|x|\).

## Classification des quatre sources

| Source | Équation et données | Résultat pertinent | Statut vérifié |
|---|---|---|---|
| Hou–Wang–Yang, arXiv:2509.25116v2, 19 mars 2026 | Navier–Stokes 3D incompressible, non forcé, \(\mathbb R^3\); donnée compacte mais singulière à l’origine | Profil stationnaire auto-similaire exact, mode propre droit instable exact et famille non unique Leray–Hopf | Prépublication : noyau spectral/profil certifié par preuve assistée par ordinateur; construction non linéaire analytique |
| Jia–Šverák, JFA 2015 | Navier–Stokes 3D incompressible, non forcé, \(\mathbb R^3\); localisation d’un profil auto-similaire | Variété instable et non-unicité conditionnelle | Théorème analytique conditionnel à une hypothèse spectrale non démontrée dans l’article |
| Albritton–Brué–Colombo, Annals 2022 | Navier–Stokes 3D incompressible forcé, \(\mathbb R^3\); vitesse initiale nulle | Deux solutions adaptées de Leray–Hopf et construction d’une trajectoire instable | Preuve analytique publiée; ne concerne pas l’équation Clay non forcée |
| Ionescu–Jia–Palasek, arXiv:2606.07501v1, 5 juin 2026 | Navier–Stokes 3D incompressible, non forcé, \(\mathbb R^3\); donnée compacte mais singulière à l’origine | Théorème conditionnel et profil instable candidat | Théorème analytique conditionnel; profil et valeur propre issus d’un calcul de haute précision non certifié |

La terminologie « preuve assistée par ordinateur » est réservée ici aux inclusions avec bornes rigoureuses annoncées par Hou–Wang–Yang. Un résidu petit sur une grille dense, même de l’ordre de \(10^{-10}\), reste un calcul non certifié s’il n’est accompagné ni d’arithmétique dirigée, ni d’une réduction à un ensemble compact, ni d’une borne de troncature.

## 1. Hou–Wang–Yang : projecteurs exacts mais constantes non quantifiées

### 1.1 Opérateur linéarisé

Dans les variables auto-similaires \((\xi,\tau)\), autour du profil exact \(\widetilde U\), l’opérateur d’évolution linéarisé est

\[
\mathcal L_{\widetilde U}v
=\frac12v+\frac12\xi\cdot\nabla v
-\Pi\bigl(\widetilde U\cdot\nabla v+v\cdot\nabla\widetilde U\bigr)
+\Delta v.
\]

La présence de la projection de Leray \(\Pi\) est essentielle : le terme de pression n’est pas local et ne peut pas être supprimé dans une perturbation du profil.

### 1.2 Projecteurs de Riesz et espaces spectraux

Pour chaque valeur propre instable \(\lambda_j\), \(\Re\lambda_j>0\), Hou–Wang–Yang définissent

\[
P_{\lambda_j}
=\frac{1}{2\pi i}\int_{\Gamma_j}
(\lambda-\mathcal L_{\widetilde U})^{-1}\,d\lambda,
\tag{HWY 2.14}
\]

où \(\Gamma_j\) entoure \(\lambda_j\) et aucune autre partie du spectre. Ils posent ensuite

\[
P_s=I-\sum_jP_{\lambda_j},\qquad
X_j=\operatorname{Ran}P_{\lambda_j},\qquad
X_s=\operatorname{Ran}P_s,
\tag{HWY 2.15}
\]

et

\[
A_j=\mathcal L_{\widetilde U}|_{X_j},\qquad
A_s=\mathcal L_{\widetilde U}|_{X_s}.
\tag{HWY 2.16}
\]

Chaque \(X_j\) est de dimension finie. Une base généralisée est autorisée :

\[
(A_j-\lambda_j)^{k_j}f_{j,k}=0.
\]

Conséquence contradictoire importante : la formule de contour est valide même en présence d’un bloc de Jordan, mais une formule projective de rang un ne l’est pas tant que la simplicité algébrique n’est pas prouvée.

### 1.3 Constantes et quantificateurs de semi-groupe

Pour tout \(\delta>0\), les estimations sur chaque sous-espace instable sont

\[
e^{\Re\lambda_j\tau-\delta|\tau|}\|f\|_2
\lesssim
\|e^{\tau A_j}f\|_2
\lesssim
e^{\Re\lambda_j\tau+\delta|\tau|}\|f\|_2,
\qquad f\in X_j,\quad \tau\in\mathbb R.
\tag{HWY 2.18}
\]

Sur le sous-espace stable,

\[
\|e^{\tau A_s}f\|_2
\lesssim e^{\delta\tau}\|f\|_2,
\qquad f\in X_s,\quad \tau>0,
\tag{HWY 2.19}
\]

et, pour \(\tau>0\) et \(\sigma_2\geq\sigma_1\geq0\),

\[
\|e^{\tau A_s}f_s\|_{H^{\sigma_2}}
\lesssim
\tau^{-(\sigma_2-\sigma_1)/2}
e^{\delta\tau}
\|f_s\|_{H^{\sigma_1}}.
\tag{HWY 2.20}
\]

La constante implicite de la dernière estimation dépend de
\(\delta,\sigma_1,\sigma_2\), le profil exact étant fixé. L’article ne donne pas de valeur numérique de ces constantes et ne les certifie pas uniformément sous variation du profil, de la coupure ou d’une désingularisation intérieure.

### 1.4 Formule de Duhamel et quantificateurs du point fixe

La branche stable est intégrée depuis \(-\infty\),

\[
\mathcal T(U)_s(\tau)
=\int_{-\infty}^{\tau}
e^{(\tau-s)A_s}P_s
\bigl(\mathcal L_{\mathrm{far}}U+F+N(U,U)\bigr)\,ds,
\]

tandis que chaque coordonnée instable est prescrite à \(\tau=0\),

\[
\mathcal T(U)_j(\tau)
=e^{\tau A_j}U_{j0}
-\int_\tau^0
e^{(\tau-s)A_j}P_j
\bigl(\mathcal L_{\mathrm{far}}U+F+N(U,U)\bigr)\,ds,
\]

avec \(U_{j0}=P_jU(0)\).

Le choix explicite est \(p=4\), donc

\[
\alpha=1-\frac3p=\frac14,
\qquad
\delta=
\frac12\min\left\{
\frac{p-3}{2p},
\min_j\Re\lambda_j
\right\}
=\frac12\min\left\{\frac18,\min_j\Re\lambda_j\right\}>0.
\]

La norme du point fixe est

\[
\|U\|_X
=\sup_{\tau<0}
R^{(p-3)/(2p)}
e^{-\delta\tau}
\|U(\tau)\|_{H^3}
=\sup_{\tau<0}
R^{1/8}e^{-\delta\tau}\|U(\tau)\|_{H^3}.
\]

L’ensemble admissible satisfait

\[
\mathcal D_{R,\eta,U_{j0}}
=
\left\{
\|U\|_X\leq1:
P_jU(0)=U_{j0}\ \text{pour tout }j
\right\},
\]

avec

\[
\sum_jR^{\alpha/2}\|U_{j0}\|_{H^3}\leq\eta,
\qquad \alpha/2=\frac18.
\]

Si \(C\) désigne le maximum des constantes implicites utilisées dans les estimations (2.18)–(2.20), les choix imposés sont

\[
C\sum_jR^{-\alpha/2}\leq\frac1{12},
\qquad
C\eta\leq\frac14.
\]

La borne d’auto-application devient au plus

\[
\frac14+\frac12<1,
\]

et le facteur de contraction est au plus \(1/2\).

Ces quantificateurs montrent exactement la dépendance cachée : les amplitudes instables admissibles décroissent comme \(R^{-1/8}\). La construction prouve une non-unicité pour chaque rayon suffisamment grand fixé; elle ne fournit pas une séparation strictement positive uniforme en \(R\).

### 1.5 Séparation des branches : ce qui est prouvé et ce qui est seulement dérivé

Pour deux paramètres terminaux \(a=(U_{j0})\) et \(b=(V_{j0})\), la construction donne exactement

\[
P_j\bigl(U^a(0)-U^b(0)\bigr)
=U_{j0}-V_{j0}.
\]

Dans \(H^3\), la bornitude du projecteur implique la conséquence élémentaire

\[
\|U^a(0)-U^b(0)\|_{H^3}
\geq
\frac{\|U_{j0}-V_{j0}\|_{H^3}}
{\|P_j\|_{H^3\to H^3}}.
\tag{Audit 1}
\]

Cette inégalité est une dérivation de l’audit, non une constante annoncée dans Hou–Wang–Yang. Elle est valide pour un profil exact et un rayon \(R\) fixés. L’article ne fournit ni valeur calculable de
\(\|P_j\|_{H^3\to H^3}\), ni borne uniforme lorsque \(R\to\infty\). De plus, le numérateur permis par le domaine du point fixe est lui-même d’ordre au plus \(R^{-1/8}\).

### 1.6 Mode adjoint : présent dans la recherche numérique, absent du certificat final

La section numérique introduit formellement des vecteurs propres droit et gauche pour un opérateur approché :

\[
\mathcal L(\widetilde U)v^r=\lambda v^r,
\qquad
\mathcal L(\widetilde U)^*v^l=\lambda v^l.
\]

La formule de gradient employée pour chercher le profil candidat est

\[
\frac{\delta\lambda(\bar U_n)}{\delta\widetilde U}
=
\frac{
v_n^l\cdot\nabla^Tv_n^r
-v_n^r\cdot\nabla v_n^l
}{
\langle v_n^l,v_n^r\rangle
}.
\tag{HWY 5.1}
\]

Elle vient de la formule non auto-adjointe de Hellmann–Feynman

\[
\partial\lambda
=
\frac{\langle v^l,(\partial\mathcal L)v^r\rangle}
{\langle v^l,v^r\rangle}.
\]

Ce vecteur gauche sert à l’optimisation numérique du candidat. Le certificat exact localisé dans l’article enferme le profil et un mode propre droit; il ne certifie pas un mode propre adjoint exact, un intervalle inférieur strict pour
\(|\langle v^l,v^r\rangle|\), la simplicité algébrique, la totalité du spectre instable ou une norme de projecteur.

Les inclusions numériques certifiées annoncées sont notamment

\[
x_0^U\leq1.44\times10^{-5},\qquad
x_1^U\leq6.2\times10^{-6},
\]

\[
x_0^v\leq5.67\times10^{-4},\qquad
x_1^v\leq4.3\times10^{-4},
\]

et

\[
|\lambda-\bar\lambda|\leq0.0045,
\qquad |\bar\lambda|\approx0.113
\]

dans la convention de signe elliptique de leur validation. Ces bornes suffisent à conserver le signe instable dans la convention d’évolution. Elles ne sont pas des bornes de résolvante ou de semi-groupe.

Si une valeur propre exacte isolée était algébriquement simple, avec vecteurs propres droit \(v\) et adjoint \(v^*\) tels que
\(\langle v^*,v\rangle\neq0\), alors on aurait

\[
P_\lambda f
=
\frac{\langle v^*,f\rangle}
{\langle v^*,v\rangle}v
\]

et, dans un espace de Hilbert,

\[
\|P_\lambda\|
=
\frac{\|v^*\|\,\|v\|}
{|\langle v^*,v\rangle|}.
\tag{Audit 2}
\]

Les formules (Audit 2) sont des faits standards de théorie spectrale appliqués conditionnellement; elles ne sont pas certifiées pour l’opérateur exact de Hou–Wang–Yang. Le dénominateur mesure précisément le conditionnement non normal manquant.

## 2. Jia–Šverák : matrice conceptuelle, théorème conditionnel

### 2.1 Espace, opérateur et hypothèse spectrale

L’espace utilisé est

\[
X=
\left\{
\phi\in L^2(\mathbb R^3)\cap L^4(\mathbb R^3):
\operatorname{div}\phi=0
\right\},
\qquad
\|\phi\|_X=\|\phi\|_2+\|\phi\|_4.
\]

L’opérateur est

\[
\mathcal L_\sigma\phi
=
\Delta\phi+\frac x2\cdot\nabla\phi+\frac12\phi
-U_\sigma\cdot\nabla\phi
-\phi\cdot\nabla U_\sigma+\nabla P.
\]

L’hypothèse spectrale (A) demande, pour \(\sigma\leq\sigma_0\),

\[
\sigma(\mathcal L_\sigma)
\subset
\{\Re\lambda<-\delta<0\}
\cup
\{\lambda_1(\sigma),\overline{\lambda_1(\sigma)}\},
\]

avec une paire simple telle que

\[
\Re\lambda_1(\sigma)<0\quad(\sigma<\sigma_0),
\]

\[
\Re\lambda_1(\sigma_0)=0,\qquad
\Im\lambda_1(\sigma_0)>0,
\]

et

\[
\left.
\frac{d}{d\sigma}\Re\lambda_1(\sigma)
\right|_{\sigma=\sigma_0}>0.
\]

Pour \(\sigma>\sigma_0\) assez proche, les auteurs prennent

\[
\beta=\Re\lambda_1(\sigma)\in(0,1/32),
\]

tandis que le reste du spectre est dans
\(\{\Re\lambda<-3\delta/4\}\). Cette hypothèse n’est pas démontrée dans l’article.

### 2.2 Modes, semi-groupes et séparation

La décomposition est \(X=X_u\oplus X_s\), avec
\(\dim X_u=2\), restrictions \(A_u,A_s\) et projecteurs spectraux
\(P_u,P_s\). La formule de contour n’est pas réécrite à cet endroit, mais ces projecteurs sont les projecteurs spectraux de l’hypothèse isolée.

Pour \(f\in X_u\) et \(t<0\),

\[
c_1e^{\beta t}\|f\|_X
\leq
\|e^{A_ut}f\|_X
\leq
c_2e^{\beta t}\|f\|_X,
\qquad 0<c_1<c_2,
\tag{JS 4.17}
\]

et, pour \(f\in X_s\), \(t<0\),

\[
\|e^{-A_st}f\|_X
\leq
C(\sigma)e^{\delta t/2}\|f\|_X.
\tag{JS 4.18}
\]

La formule de variété instable est

\[
\phi_u(t)
=
e^{A_ut}\phi_{u0}
-\int_0^t
e^{A_u(t-\tau)}
P_u\mathbb P(\phi\cdot\nabla\phi)(\tau)\,d\tau,
\]

\[
\phi_s(t)
=
-\int_{-\infty}^t
e^{A_s(t-\tau)}
P_s\mathbb P(\phi\cdot\nabla\phi)(\tau)\,d\tau.
\]

Après le choix

\[
\|\phi_{u0}\|_X=\gamma\varepsilon,
\]

les corrections sont d’ordre
\(O(e^{\beta t}\varepsilon^2)\) et les auteurs obtiennent, pour
\(\varepsilon\) suffisamment petit,

\[
\|\phi(t)\|_{L^4}
\geq
c(\alpha,\delta,\gamma)
\varepsilon e^{\beta t},
\qquad t<0.
\]

En particulier,

\[
\inf_{t<0}e^{-\beta t}\|\phi(t)\|_{L^4}>0.
\]

Les constantes \(c_1,c_2,C(\sigma)\) et
\(c(\alpha,\delta,\gamma)\) existent sous l’hypothèse spectrale, mais ne sont pas données numériquement. La séparation est asymptotique et conditionnelle.

Une estimation générale utilisée en amont est

\[
\|e^{\mathcal Ls}\phi_0\|_X
\leq Ce^{-s/4}\|\phi_0\|_X.
\]

Pour une perturbation \(\mathcal K(a)\), si
\(\|a\|_Y\leq M\), si le taux de croissance est au plus
\(\omega_*\), et si

\[
\beta>\max\{\omega_*,-1/4\},
\]

alors

\[
\|e^{(\mathcal L-\mathcal K(a))t}\|_{X\to X}
\leq
C(M,\beta,\omega_*)e^{\beta t}.
\]

Ce théorème explicite les dépendances paramétriques, mais pas une constante calculable.

## 3. Albritton–Brué–Colombo : mode maximisant et séparation asymptotique, avec force

### 3.1 Opérateur et mode propre

Pour un profil de fond \(\bar U\), l’opérateur auto-similaire est écrit

\[
-\mathbf L_{\mathrm{ss}}U
=
-\frac12(1+\xi\cdot\nabla)U
-\Delta U
+\mathbb P
\bigl(
\bar U\cdot\nabla U
+U\cdot\nabla\bar U
\bigr).
\]

Son domaine est

\[
D=
\left\{
U\in L^2_\sigma:
U\in H^2,\\
\xi\cdot\nabla U\in L^2
\right\}.
\]

Si

\[
a=s(\mathbf L_{\mathrm{ss}})>0,
\]

une valeur propre de croissance maximale est choisie,
\(\lambda=a+ib\), avec

\[
\mathbf L_{\mathrm{ss}}\eta=\lambda\eta.
\]

Le mode réel est

\[
U^{\mathrm{lin}}(\xi,\tau)
=
\Re\bigl(e^{\lambda\tau}\eta(\xi)\bigr).
\]

La solution construite a le développement

\[
U
=
\bar U+U^{\mathrm{lin}}+U^{\mathrm{per}},
\qquad
\|U^{\mathrm{per}}(\tau)\|_{H^k}
\lesssim_k e^{2a\tau}.
\]

La séparation est donc portée par un terme d’ordre \(e^{a\tau}\), tandis que le reste est d’ordre \(e^{2a\tau}\).

### 3.2 Projecteur et constantes de semi-groupe

Dans la construction spectrale qui relie l’instabilité d’Euler à celle de Navier–Stokes, les auteurs emploient

\[
\operatorname{Pr}_\beta
=
\frac{1}{2\pi i}
\int_{\vec c}
R(\lambda,\mathbf T_\beta)\,d\lambda.
\tag{ABC 3.36}
\]

Cette formule sert à montrer la persistance d’une composante spectrale non triviale. Elle ne fournit pas un projecteur quantitatif pour le profil exact de Hou–Wang–Yang.

Pour tout \(\delta>0\),

\[
\|e^{\tau\mathbf L_{\mathrm{ss}}}U_0\|_2
\leq
M(\delta)e^{\tau(a+\delta)}\|U_0\|_2.
\tag{ABC 4.7}
\]

Pour \(\sigma_2\geq\sigma_1\geq0\), \(\delta>0\) et \(\tau>0\),

\[
\|e^{\tau\mathbf L_{\mathrm{ss}}}U_0\|_{H^{\sigma_2}}
\leq
\frac{
M(\sigma_1,\sigma_2,\delta)
}{
\tau^{(\sigma_2-\sigma_1)/2}
}
e^{\tau(a+\delta)}
\|U_0\|_{H^{\sigma_1}}.
\tag{ABC 4.8}
\]

La dépendance au profil fixé \(\bar U\) est supprimée de la notation. Les constantes sont existentielles et non numériques.

Dans le point fixe non linéaire, les auteurs choisissent

\[
\varepsilon_0=a/2,
\qquad
\|U\|_X
=
\sup_{\tau<T}
e^{-(a+\varepsilon_0)\tau}
\|U(\tau)\|_{H^N},
\]

puis \(T<0\) suffisamment négatif, avec dépendance

\[
T=T(\bar U,U^{\mathrm{lin}},N).
\]

Il n’y a pas de valeur numérique universelle pour \(T\). La différence entre les deux branches est néanmoins analytique et asymptotiquement non nulle. Le raccord au problème Clay échoue au niveau de la force extérieure : le théorème porte sur une équation forcée.

## 4. Ionescu–Jia–Palasek : source postérieure, projecteur abstrait, profil non certifié

### 4.1 Projecteur de Riesz

L’opérateur est

\[
\mathcal L_U\phi
=
\Delta\phi+\frac12x\cdot\nabla\phi+\frac12\phi
-\Pi
\bigl(
U\cdot\nabla\phi+\phi\cdot\nabla U
\bigr).
\]

Sur \(X=L^2\cap L^4\), divergence nulle, les auteurs définissent

\[
P_u
=
\frac{1}{2\pi i}
\oint_{\Gamma_u}
(zI-\mathcal L_U)^{-1}\,dz,
\qquad
P_{cs}=I-P_u,
\tag{IJP 3.32}
\]

où \(\Gamma_u\) entoure tout le spectre dans le demi-plan droit. Ils posent

\[
\gamma_u
=
\min_{\lambda\in\sigma_u}\Re\lambda>0.
\]

### 4.2 Constantes de semi-groupe

Pour \(s\leq0\),

\[
\|e^{s\mathcal L_U}P_ug\|_X
+\|\nabla e^{s\mathcal L_U}P_ug\|_X
\lesssim
e^{\gamma_us/2}\|g\|_X.
\tag{IJP 3.33u}
\]

Pour \(s>0\) et tout \(\varepsilon>0\),

\[
\|e^{s\mathcal L_U}P_{cs}g\|_X
+\min(1,s^{1/2})
\|\nabla e^{s\mathcal L_U}P_{cs}g\|_X
\lesssim_\varepsilon
e^{\varepsilon s}\|g\|_X.
\tag{IJP 3.33cs}
\]

Le semi-groupe libre satisfait

\[
\begin{aligned}
\|e^{t\mathcal L_0}g\|_X
&+\min(t^{1/2},1)\|\nabla e^{t\mathcal L_0}g\|_X\\
&+\min(t,1)\|\nabla^2e^{t\mathcal L_0}g\|_X
\lesssim e^{-t/4}\|g\|_X.
\end{aligned}
\tag{IJP 3.11}
\]

Pour l’opérateur complet et

\[
m>\max\left\{-\frac14,\Re\lambda_j\right\},
\]

on a

\[
\begin{aligned}
\|e^{t\mathcal L_U}g\|_X
&+\min(t^{1/2},1)\|\nabla e^{t\mathcal L_U}g\|_X\\
&+\min(t,1)\|\nabla^2e^{t\mathcal L_U}g\|_X
\lesssim_{\|U\|_Y,m}
e^{mt}\|g\|_X.
\end{aligned}
\tag{IJP 3.12}
\]

Les dépendances sont indiquées mais les constantes ne sont pas calculées.

### 4.3 Variété instable et séparation

Pour une donnée terminale
\(\phi_{u0}\in\operatorname{Ran}P_u\),

\[
\begin{aligned}
H(s)
=\;&e^{s\mathcal L_U}\phi_{u0}\\
&+\int_{-\infty}^s
e^{(s-\tau)\mathcal L_U}
P_{cs}\mathcal N(H)(\tau)\,d\tau\\
&-\int_s^0
e^{(s-\tau)\mathcal L_U}
P_u\mathcal N(H)(\tau)\,d\tau.
\end{aligned}
\tag{IJP 3.34}
\]

Ils choisissent

\[
\eta=\min\{1/100,\gamma_u/4\},
\qquad
\|h\|_{E_\eta}
=
\sup_{s\leq0}e^{-\eta s}\|h(s)\|_{X^1},
\]

et obtiennent

\[
\sup_{s\leq0}
e^{-\eta s}\|H(s)\|_{X^1}
\lesssim
\varepsilon_R+\|\phi_{u0}\|_{X^1},
\]

pour \(\|\phi_{u0}\|_{X^1}\) suffisamment petit et \(R\) suffisamment grand, avec
\(\varepsilon_R\to0\).

Comme

\[
P_uH(0)=\phi_{u0},
\]

deux paramètres terminaux distincts produisent deux solutions distinctes sous les hypothèses du théorème. L’audit en déduit, pour \(a\neq b\),

\[
\|H^a(0)-H^b(0)\|_{X^1}
\geq
\frac{\|a-b\|_{X^1}}
{\|P_u\|_{X^1\to X^1}}.
\tag{Audit 3}
\]

L’article ne donne ni \(\|P_u\|\), ni un seuil numérique pour
\(\|\phi_{u0}\|_{X^1}\), ni une séparation uniforme en \(R\).

### 4.4 Statut du calcul

Le candidat numérique annoncé a la valeur propre

\[
\lambda_*=0.235059597921.
\]

Les résidus globaux évalués sur des grilles denses descendent approximativement jusqu’à
\(3\times10^{-10}\). Les auteurs formulent néanmoins l’existence exacte du profil et du mode comme une conjecture, puis prouvent leur théorème de non-unicité conditionnellement à cette existence avec décroissance. Aucune inclusion par intervalles, borne rigoureuse de troncature, preuve de compacité numérique ou certificat de résolvante n’est fourni. Le statut correct est donc : calcul de haute précision non certifié, et non preuve assistée par ordinateur.

Aucun mode adjoint n’est utilisé ou certifié dans cette prépublication. Le projecteur \(P_u\) est abstrait et conditionnel au profil exact conjecturé.

## 5. Comparaison des quantificateurs réellement disponibles

| Source | Projecteur | Constante de semi-groupe | Séparation | Uniformité manquante |
|---|---|---|---|---|
| Hou–Wang–Yang | Contours \(P_{\lambda_j}\) exacts pour le profil certifié | Constantes implicites dépendant de \(\delta\) et des indices de Sobolev | Coordonnées terminales exactement distinctes; borne (Audit 1) conditionnée par \(\|P_j\|\) | Pas de norme certifiée du projecteur; amplitudes \(O(R^{-1/8})\) |
| Jia–Šverák | Décomposition spectrale conditionnelle \(P_u\oplus P_s\) | \(c_1,c_2,C(\sigma)\) existent sous l’hypothèse spectrale | \(c(\alpha,\delta,\gamma)\varepsilon e^{\beta t}\) | Hypothèse spectrale non prouvée; constantes non numériques |
| Albritton–Brué–Colombo | Projecteur de contour dans la persistance spectrale | \(M(\delta)\), \(M(\sigma_1,\sigma_2,\delta)\) | Mode \(e^{a\tau}\) contre reste \(O(e^{2a\tau})\) | Dépendance au profil et au temps initial \(T\); équation forcée |
| Ionescu–Jia–Palasek | \(P_u\) entoure tout le spectre instable | Constantes implicites dépendant de \(\varepsilon,\|U\|_Y,m\) | \(P_uH(0)=\phi_{u0}\); borne (Audit 3) | Profil non certifié; \(\|P_u\|\) et seuil d’amplitude inconnus |

## 6. Recherche d’une source postérieure sur l’adjoint ou la désingularisation

La recherche différentielle menée jusqu’au 2026-08-14 n’a trouvé aucune source primaire postérieure à Hou–Wang–Yang qui :

1. certifie un mode propre adjoint pour leur opérateur exact;
2. prouve la simplicité algébrique de la valeur propre instable certifiée;
3. donne une formule de rang un validée ou une borne numérique de
   \(\|P_{\lambda}\|\);
4. certifie le nombre total de valeurs propres instables;
5. maintient l’instabilité et la non-unicité après lissage intérieur de la singularité initiale en \(1/|x|\).

Ionescu–Jia–Palasek est la source ultérieure la plus directement voisine. Elle apporte la formule abstraite (IJP 3.32), mais ne ferme aucun des cinq points.

Le préprint de Binz–Coiculescu, arXiv:2607.12159, étudie des profils homothétiques et fournit une obstruction dans une classe de profils. Il ne construit ni adjoint de Hou–Wang–Yang ni stabilité sous lissage intérieur.

Un faux positif important est Cheskidov–Dai–Palasek, arXiv:2511.09556v2. Ce travail construit sur le tore des solutions faibles générales avec singularité instantanée et non-unicité à partir de données lisses. Les auteurs précisent toutefois que leurs solutions ne sont ni dans
\(L^\infty_tL^2_x\), ni dans \(L^2_tH^1_x\) au voisinage de l’instant singulier; l’énergie est injectée depuis les fréquences infinies. Ce ne sont donc pas des solutions de Leray–Hopf et ce résultat ne désingularise pas la construction de Hou–Wang–Yang dans la classe admissible du problème Clay.

## 7. Obstacle distinct : la désingularisation intérieure

La coupure de Hou–Wang–Yang et d’Ionescu–Jia–Palasek est une localisation extérieure. Elle rend la donnée compacte mais conserve une singularité d’ordre \(1/|x|\) à l’origine. Faire tendre le rayon extérieur \(R\) vers l’infini n’est pas un lissage intérieur.

Une famille lissée \(u_{0,\rho}\), divergence nulle et régulière dans
\(|x|\lesssim\rho\), doit engendrer une solution forte unique sur un intervalle initial non trivial. Par unicité faible–forte, deux solutions de Leray–Hopf partageant cette donnée ne peuvent se séparer tant que cette solution forte existe. Une preuve de stabilité de la variété instable sous \(\rho\downarrow0\) devrait donc contrôler simultanément :

- le temps de vie forte de \(u_{0,\rho}\);
- le transport de la coordonnée instable au-delà de ce temps;
- les normes de projecteur et de résolvante;
- la pression non locale créée par la correction intérieure;
- une séparation qui ne soit pas absorbée par les erreurs de raccord;
- les limites de Leray–Hopf et l’inégalité d’énergie.

Aucune des quatre sources auditées ne fournit ces contrôles. L’adjoint–projecteur est un premier maillon quantitatif, mais il ne contourne pas l’unicité faible–forte.

## 8. Recommandation falsifiable

### Lemme expérimental actif proposé

Pour le profil exact \(\widetilde U\) certifié par Hou–Wang–Yang et une valeur propre instable certifiée \(\lambda\), établir par calcul validé :

1. un contour \(\Gamma\) dont la résolvante est uniformément bornée et qui sépare \(\lambda\) du reste du spectre;
2. la multiplicité algébrique un de \(\lambda\);
3. un vecteur propre adjoint exact \(v^*\);
4. une inclusion

\[
0<m
\leq
|\langle v^*,v\rangle|;
\]

5. des bornes certifiées

\[
\|v\|\leq M_r,\qquad
\|v^*\|\leq M_l,\qquad
\|P_\lambda\|\leq K_P:=\frac{M_lM_r}{m}.
\]

Pour deux branches dont les coordonnées terminales sont \(a\) et \(b\) le long d’un mode normalisé, le certificat doit alors produire

\[
\|u^a(1)-u^b(1)\|_{H^3}
\geq
\frac{|a-b|}{K_P},
\]

avec toutes les conversions entre variables auto-similaires et physiques, ainsi que la dépendance
\(|a|+|b|\lesssim R^{-1/8}\), explicitement suivies.

### Critères de réfutation

Le lemme expérimental est réfuté dans sa forme proposée si l’une des situations suivantes est certifiée :

- aucun contour isolant ne peut être fermé avec les bornes de résolvante disponibles;
- l’intervalle de \(|\langle v^*,v\rangle|\) contient zéro;
- la valeur propre n’est pas algébriquement simple;
- \(K_P\) diverge sous les perturbations déjà admises par le certificat du profil;
- la borne de séparation est dominée par les erreurs de coupure pour tout \(R\) admissible.

Un succès donnerait une constante de séparation falsifiable à rayon fixé et une mesure du conditionnement non normal. Il ne devrait pas être présenté comme une désingularisation intérieure ni comme une avancée directe sur les données lisses Clay. L’étape suivante, séparée, serait un test de raccord intérieur \(u_{0,\rho}\) avec constantes uniformes en \(\rho\); l’approche devra être abandonnée si les constantes spectrales ou de raccord divergent avant le premier temps où l’unicité faible–forte cesse d’être disponible.

## Sources primaires

- T. Y. Hou, Y. Wang, C. Yang, [A computer-assisted proof of nonuniqueness for the 3D Navier–Stokes equations, arXiv:2509.25116](https://arxiv.org/abs/2509.25116), version 2 du 19 mars 2026; [PDF v2 des auteurs](https://users.cms.caltech.edu/~hou/papers/Nonuniqueness_NSE_v2.pdf).
- H. Jia, V. Šverák, [Are the incompressible 3D Navier–Stokes equations locally ill-posed in the natural energy space?, arXiv:1306.2136](https://arxiv.org/abs/1306.2136), Journal of Functional Analysis 268 (2015), 3734–3766.
- D. Albritton, E. Brué, M. Colombo, [Non-uniqueness of Leray solutions of the forced Navier–Stokes equations, Annals of Mathematics 196 (2022)](https://annals.math.princeton.edu/2022/196-1/p03), [DOI 10.4007/annals.2022.196.1.3](https://doi.org/10.4007/annals.2022.196.1.3).
- A. D. Ionescu, H. Jia, S. Palasek, [Nonuniqueness of Leray–Hopf solutions to the 3D Navier–Stokes equations, arXiv:2606.07501](https://arxiv.org/abs/2606.07501), version 1 du 5 juin 2026.
- S. Binz, C. Coiculescu, [arXiv:2607.12159](https://arxiv.org/abs/2607.12159), juillet 2026.
- A. Cheskidov, M. Dai, S. Palasek, [Instantaneous Type I blow-up and non-uniqueness of smooth solutions of the Navier–Stokes equations, arXiv:2511.09556](https://arxiv.org/abs/2511.09556), version 2.

## Conclusion de l’audit contradictoire

Le maillon transférable immédiat n’est pas une preuve de régularité ou de blow-up Clay, mais une question de conditionnement spectral précisément formulée. Le projecteur de Riesz existe abstraitement; sa norme et sa stabilité ne sont pas certifiées. Le mode adjoint apparaît comme outil de découverte chez Hou–Wang–Yang, pas comme objet validé. Le meilleur progrès court terme consiste à transformer cette lacune en un certificat adjoint–résolvante–projecteur, puis à mesurer si la séparation obtenue survit aux erreurs de localisation. L’obstacle de désingularisation intérieure reste indépendant et ouvert.
