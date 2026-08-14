# Cycle 0018 — audit contradictoire du théorème 4.1, équations (8)–(22)

Date de la passe : 2026-08-14

Source auditée : Zoran Grujić, *Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier–Stokes Equations*, [arXiv:2607.08866v2](https://arxiv.org/abs/2607.08866v2), théorème 4.1 et équations (8)–(22).

Portée : commutateur proche, extension BMO, \(I_1\), \(I_{2,\mathrm{far}}\), chaque anneau de \(I_{2,\mathrm{mid}}\), indices, sommes, normes de Lorentz, dimensions, centre et uniformité temporelle.

> **Statut de la revue.** Cette passe est produite par un agent de la même famille de modèle que les autres passes de Millennium Forge. Elle est contradictoire dans sa méthode, mais **n’est pas une revue externe ni une réplication indépendante**.

## Verdict

Le mécanisme annoncé par (8)–(22) est réparable : pour un opérateur de Calderón–Zygmund homogène d’ordre zéro, une vorticité uniformément bornée dans \(L^{3/2,\infty}\) et une direction dont les oscillations moyennes décroissent comme un logarithme, les quatre contributions satisfont

\[
\begin{array}{c|c}
\text{contribution}&
\|\cdot\|_{L^{3/2,\infty}(B_R)}\\ \hline
\text{proche}&O(MB_\xi\phi(R))\\
I_1&O(MB_\xi\phi(R))\\
I_{2,\mathrm{far}}&O(MR/R_*)=O(M\phi(R))\\
I_{2,\mathrm{mid}}&O(MB_\xi\phi(R)).
\end{array}
\]

Ici \(M=\sup_t\|\omega(t)\|_{L^{3/2,\infty}}\), \(B_\xi\) est la constante uniforme d’oscillation pondérée, \(R_*\) est une longueur de référence et

\[
\phi(R)=\frac{1}{1+\log(R_*/R)}.
\]

La conclusion conditionnelle correcte est donc

\[
\|\alpha(t)\|_{L^{3/2,\infty}(B_R(z))}
\le C_{\mathcal T}M(B_\xi+1)\phi(R)
\]

uniformément en \(t\), en \(z\), et pour \(R/R_*\) suffisamment petit.

Le texte contient néanmoins plusieurs énoncés faux ou incomplets :

1. l’extension proche est petite seulement en **semi-norme** BMO. Une norme BMO ancrée ne peut être \(O(\phi(R))\) pour une direction constante de module un ;
2. \(L^{3/2,\infty}\) n’est pas réflexif, contrairement à la phrase précédant (9). La borne de commutateur reste obtenable par interpolation réelle entre deux exposants forts ;
3. la réarrangée de \(|y|^{-3}\mathbf1_{|y|>a}\) n’est pas exactement un minimum comme affirmé avant (12), mais \((a^3+s/|B_1|)^{-1}\) ; les deux profils sont comparables et donnent bien \(a^{-2}\) ;
4. l’inégalité \(\phi(2^jR)\le2\phi(R)\) utilisée entre (20) et (21) est fausse au dernier anneau dyadique avec le choix de \(N\) du papier ; la constante \(3\) convient lorsque \(R/R_*\le2^{-6}\) ;
5. \(R^{1/2}\), \(|\log R|\) et la coupure \(r<1/2\) sont dimensionnellement indéfinis avant normalisation par \(R_*\).

Ces défauts n’invalident pas l’exposant de (22). Le premier énoncé littéralement faux dépend de la convention BMO : si « norme » signifie une norme ancrée, c’est la ligne 155 du HTML ; sous la convention usuelle de semi-norme modulo les constantes, le premier énoncé indiscutablement faux est la qualification de \(L^{3/2,\infty}\) comme réflexif, suivie de la formule exacte de réarrangement en (12). Le lemme minimal réparé est donné en section 9.

## 1. Cadre exact

À un temps fixé, considérons sur \(\mathbb R^3\) :

- une vorticité vectorielle \(\boldsymbol\omega=\omega\xi\), avec \(\omega=|\boldsymbol\omega|\ge0\) ;
- une direction mesurable \(\xi\), définie aussi sur \(\{\omega=0\}\) par une extension choisie, avec \(|\xi|\le1\) ;
- le tenseur de déformation \(S=\mathcal T(\omega\xi)\), où \(\mathcal T\) est la matrice d’opérateurs singuliers issue de Biot–Savart ;
- \(\alpha=\xi\cdot S\xi\).

Composante par composante, \(\mathcal T\) possède un noyau principal

\[
|K(x)|\le C_K|x|^{-3}
\tag{K}
\]

avec annulation sphérique. Dans la partie symétrique du gradient de Biot–Savart, les éventuels termes locaux issus des dérivées secondes du potentiel newtonien s’annulent ; le noyau pertinent est donc un Calderón–Zygmund principal de degré \(-3\).

La cancellation unidirectionnelle donne, après contraction des indices,

\[
|\alpha(x)|
\le C_{\rm con}
|[\mathcal T,\xi](\omega)(x)|.
\tag{C}
\]

Les constantes finies dues au nombre de composantes sont incluses dans \(C_{\rm con}\) ou \(C_K\). Cette passe ne réaudite pas la formule tensorielle complète de Biot–Savart, mais exige (C) comme raccord explicite.

### Normalisation des oscillations

Fixons une longueur \(R_*>0\) et posons, pour \(0<r\le R_*\),

\[
L(r)=1+\log\frac{R_*}{r},
\qquad
\phi(r)=L(r)^{-1}.
\]

Supposons

\[
\boxed{
\sup_t\sup_{z\in\mathbb R^3,\ 0<r\le R_*}
\frac{1}{\phi(r)}
\fint_{B_r(z)}|\xi(y,t)-\xi_{B_r(z)}(t)|\,dy
\le B_\xi.
}
\tag{BMOphi}
\]

Cette hypothèse est la version dimensionnée de la partie oscillation de la \(\mathrm{bmo}_\phi\) du papier. L’information \(\|\xi\|_\infty\le1\) est gardée séparément.

On note

\[
M=\sup_t\|\omega(t)\|_{L^{3/2,\infty}}.
\tag{M}
\]

Les deux quantités \(M\) et \(\|\alpha\|_{L^{3/2,\infty}}\) ont la dimension \(L^2T^{-1}\), identique à celle de la viscosité. La fonction \(\phi\) et \(B_\xi\) sont sans dimension.

## 2. Décomposition au centre arbitraire

Soit \(z\in\mathbb R^3\). Par translation, on peut effectuer les calculs avec \(z=0\), puis translater le résultat. Pour \(0<R\le R_*/64\), écrivons

\[
\omega_{\rm in}=\omega\mathbf1_{B_{2R}(z)},
\qquad
\omega_{\rm out}=\omega\mathbf1_{\mathbb R^3\setminus B_{2R}(z)},
\]

et

\[
c_R=\fint_{B_R(z)}\xi.
\]

La partie lointaine du commutateur se décompose exactement, à l’ordre des signes près selon la convention de commutateur, en

\[
[\mathcal T,\xi](\omega_{\rm out})(x)
=
(c_R-\xi(x))\mathcal T(\omega_{\rm out})(x)
+\mathcal T(\omega_{\rm out}(\xi-c_R))(x).
\]

On appelle les deux termes \(I_1\) et \(I_2\). Cette identité est correcte. Aucun argument temporel n’intervient : un centre \(z=z(t)\) peut varier, à condition que le confinement et les normes soient uniformes, car la translation est effectuée séparément à chaque temps.

## 3. Partie proche et extension BMO : (9)

### 3.1 Semi-norme locale

Pour toute boule \(B_\rho(y)\subset B_{2R}(z)\), on a \(\rho\le2R\). La monotonie de \(\phi\) et (BMOphi) impliquent

\[
[\xi]_{\mathrm{BMO}(B_{2R}(z))}
\le B_\xi\phi(2R).
\tag{BN}
\]

Il s’agit d’une semi-norme modulo les constantes. Si la notation \(\|\cdot\|_{\mathrm{BMO}}\) contient un terme d’ancrage, (BN) est fausse : pour \(\xi\equiv e_1\), la semi-norme vaut zéro mais toute norme conservant la taille de la moyenne vaut un. Le théorème de commutateur ne dépend que de la semi-norme, ce qui répare ce point.

### 3.2 Extension de Jones

Une boule est un domaine uniforme, avec constantes invariantes par translation et dilatation. Le théorème d’extension de Jones fournit donc une extension \(\widetilde\xi\), égale à \(\xi\) presque partout sur \(B_{2R}(z)\), telle que

\[
[\widetilde\xi]_{\mathrm{BMO}(\mathbb R^3)}
\le C_JB_\xi\phi(2R),
\tag{J}
\]

où \(C_J\) est indépendant de \(R,z,t\). Source primaire : P. W. Jones, *Extension Theorems for BMO*, Indiana Univ. Math. J. 29 (1980), 41–66, [DOI 10.1512/iumj.1980.29.29005](https://doi.org/10.1512/iumj.1980.29.29005).

Parce que \(x\in B_R(z)\), que \(\omega_{\rm in}\) est supportée dans \(B_{2R}(z)\) et que l’extension coïncide avec \(\xi\) aux points d’entrée et de sortie,

\[
[\mathcal T,\xi](\omega_{\rm in})(x)
=[\mathcal T,\widetilde\xi](\omega_{\rm in})(x).
\]

Cette identité de la ligne 156 est correcte, y compris pour la valeur principale.

### 3.3 Commutateur sur le Lorentz faible

Le théorème de Coifman–Rochberg–Weiss donne les bornes fortes \(L^p\to L^p\) pour \(1<p<\infty\), avec norme linéaire en \([\widetilde\xi]_{\rm BMO}\). En interpolant un exposant \(p_-<3/2\) et un exposant \(p_+>3/2\), on obtient aussi

\[
\|[\mathcal T,\widetilde\xi]g\|_{L^{3/2,\infty}}
\le C_{\rm CRW}
[\widetilde\xi]_{\rm BMO}
\|g\|_{L^{3/2,\infty}}.
\tag{CRW}
\]

Le résultat est valide, mais la justification textuelle du papier est fausse : \(L^{3/2,\infty}\) n’est pas réflexif. La réflexivité n’est pas nécessaire à l’interpolation réelle. Source primaire pour le commutateur : R. R. Coifman, R. Rochberg et G. Weiss, *Factorization theorems for Hardy spaces in several variables*, Ann. of Math. 103 (1976), 611–635, [DOI 10.2307/1970954](https://doi.org/10.2307/1970954). Source primaire pour les Lorentz : R. A. Hunt, *On \(L(p,q)\) spaces*, L’Enseignement Mathématique 12 (1966), 249–276.

Puisque la restriction et la multiplication par une indicatrice ne font pas croître la norme faible,

\[
\|[\mathcal T,\xi](\omega_{\rm in})\|_{L^{3/2,\infty}(B_R(z))}
\le C_{\rm CRW}C_JMB_\xi\phi(2R).
\]

Pour \(R/R_*\le2^{-6}\),

\[
\frac{\phi(2R)}{\phi(R)}
=\frac{L(R)}{L(R)-\log2}
\le\frac65,
\]

et finalement

\[
\boxed{
\|[\mathcal T,\xi](\omega_{\rm in})\|_{L^{3/2,\infty}(B_R(z))}
\le C_NMB_\xi\phi(R),
\quad
C_N=\frac65C_{\rm CRW}C_J.
}
\tag{Near}
\]

## 4. Réarrangée exacte du noyau tronqué

Ce calcul intervient dans \(I_1\) et \(I_{2,\mathrm{far}}\). Posons

\[
h_a(y)=|y|^{-3}\mathbf1_{\{|y|>a\}},
\qquad
\varpi_3=|B_1|=\frac{4\pi}{3}.
\]

Pour \(0<\tau<a^{-3}\),

\[
|\{h_a>\tau\}|=\varpi_3(\tau^{-1}-a^3),
\]

et cette mesure est nulle pour \(\tau\ge a^{-3}\). L’inversion donne l’expression exacte

\[
\boxed{
h_a^*(s)=\frac{1}{a^3+s/\varpi_3}.
}
\tag{h*}
\]

La formule \(\min(a^{-3},Cs^{-1})\) du texte n’est qu’une équivalence à constantes, pas une identité issue d’un « direct volume calculation ».

Avec la convention de norme du papier,

\[
\begin{aligned}
\|h_a\|_{L^{3,1}}
&=\int_0^\infty s^{-2/3}h_a^*(s)\,ds\\
&=\varpi_3^{1/3}a^{-2}
\int_0^\infty\frac{z^{-2/3}}{1+z}\,dz\\
&=\boxed{
\frac{2\pi}{\sqrt3}\varpi_3^{1/3}a^{-2}}.
\end{aligned}
\tag{K31}
\]

La puissance \(a^{-2}\) de (12) est donc exacte.

## 5. Terme \(I_1\) : (11)–(14)

Pour \(x\in B_R(z)\), \(y\notin B_{2R}(z)\),

\[
|x-y|\ge\frac12|y-z|.
\]

Hölder–Lorentz et (K31), avec \(a=2R\), donnent

\[
|\mathcal T(\omega_{\rm out})(x)|
\le
8C_KC_HM\|h_{2R}\|_{L^{3,1}}
=
\frac{4\pi}{\sqrt3}\varpi_3^{1/3}
C_KC_HMR^{-2}.
\tag{Tfar}
\]

Ici \(C_H=1\) avec la normalisation « sharp Hölder » du papier, mais il est affiché pour rendre les conventions visibles.

John–Nirenberg, avec constante \(C_{\rm JN,2}\), fournit

\[
\|\xi-c_R\|_{L^2(B_R(z))}
\le C_{\rm JN,2}B_\xi\phi(R)|B_R|^{1/2}.
\]

Sur un ensemble \(E\) de mesure finie,

\[
\|g\|_{L^{3/2,\infty}(E)}
\le |E|^{1/6}\|g\|_{L^2(E)}.
\]

Donc

\[
\|\xi-c_R\|_{L^{3/2,\infty}(B_R(z))}
\le C_{\rm JN,2}\varpi_3^{2/3}
B_\xi\phi(R)R^2.
\]

En multipliant cette borne par (Tfar),

\[
\boxed{
\|I_1\|_{L^{3/2,\infty}(B_R(z))}
\le C_{I_1}MB_\xi\phi(R),
\quad
C_{I_1}=\frac{16\pi^2}{3\sqrt3}
C_KC_HC_{\rm JN,2}.
}
\tag{I1}
\]

Les puissances \(R^{-2}\) et \(R^2\) de (11)–(14) se compensent exactement. Le passage \(L^2\to L^{3/2,\infty}\) et ses dimensions sont corrects.

## 6. Queue macroscopique \(I_{2,\mathrm{far}}\) : (15)

La coupure dimensionnée correspondant à \(R^{1/2}\) est

\[
r_m=\sqrt{RR_*}.
\]

Pour \(q=R/R_*\le2^{-6}\), \(R/r_m=\sqrt q\le1/8\). Ainsi, pour \(x\in B_R(z)\) et \(|y-z|>r_m\),

\[
|x-y|^{-3}
\le\left(\frac87\right)^3|y-z|^{-3}.
\]

Comme \(|c_R-\xi(y)|\le2\), (K31) donne

\[
\|I_{2,\mathrm{far}}\|_{L^\infty(B_R(z))}
\le
2C_KC_HM\left(\frac87\right)^3
\frac{2\pi}{\sqrt3}\varpi_3^{1/3}r_m^{-2}.
\]

Or

\[
\|\mathbf1_{B_R}\|_{L^{3/2,\infty}}
=|B_R|^{2/3}=\varpi_3^{2/3}R^2.
\]

Par conséquent,

\[
\boxed{
\|I_{2,\mathrm{far}}\|_{L^{3/2,\infty}(B_R(z))}
\le C_FM\frac{R}{R_*},
\quad
C_F=\frac{16\pi^2}{3\sqrt3}
C_KC_H\left(\frac87\right)^3.
}
\tag{Ifar}
\]

Pour \(0<q\le1\),

\[
q(1+\log(1/q))\le1,
\]

donc \(q\le\phi(R)\). La queue est ainsi \(O(M\phi(R))\), uniformément. Le calcul \(R^{-1}\times R^2=R\) du papier est correct après le choix implicite \(R_*=1\).

## 7. Chaque anneau de \(I_{2,\mathrm{mid}}\) : (16)–(19)

Posons

\[
N=\left\lfloor\frac12\log_2\frac{R_*}{R}\right\rfloor,
\qquad
\mathcal A_k=B_{2^{k+1}R}(z)\setminus B_{2^kR}(z),
\quad 1\le k\le N,
\]

et

\[
c_k=\fint_{B_{2^kR}(z)}\xi,
\qquad c_0=c_R.
\]

Les anneaux complets couvrent \(2R<|y-z|\le r_m\), quitte à dépasser \(r_m\) dans le dernier anneau. Comme les estimations portent sur la valeur absolue, ce dépassement est admissible ; il ne faut simplement pas interpréter les ensembles comme une partition exacte sans intersecter le dernier anneau avec \(B_{r_m}\).

### 7.1 Dérive des moyennes

Pour \(j\ge1\),

\[
\begin{aligned}
|c_j-c_{j-1}|
&\le\frac1{|B_{2^{j-1}R}|}
\int_{B_{2^{j-1}R}}|\xi-c_j|\\
&\le8\fint_{B_{2^jR}}|\xi-c_j|\\
&\le8B_\xi\phi(2^jR).
\end{aligned}
\]

Ainsi,

\[
\boxed{
|c_{k+1}-c_0|
\le8B_\xi\sum_{j=1}^{k+1}\phi(2^jR).
}
\tag{means}
\]

L’indice \(k+1\) de (16) est correct.

### 7.2 Norme \(L^{3,1}\) de l’oscillation

Pour \(|E|=m\), Hölder sur les réarrangées donne l’injection exacte à constante suivie

\[
\|g\|_{L^{3,1}(E)}
\le9^{3/4}m^{1/12}\|g\|_{L^4(E)}.
\tag{L4-31}
\]

John–Nirenberg sur \(B_{2^{k+1}R}\) implique

\[
\|\xi-c_{k+1}\|_{L^4(B_{2^{k+1}R})}
\le C_{\rm JN,4}B_\xi
\phi(2^{k+1}R)|B_{2^{k+1}R}|^{1/4}.
\]

En combinant,

\[
\|\xi-c_{k+1}\|_{L^{3,1}(\mathcal A_k)}
\le
2\,9^{3/4}C_{\rm JN,4}\varpi_3^{1/3}
B_\xi(2^kR)\phi(2^{k+1}R).
\]

Pour une constante vectorielle \(d\),

\[
\|d\mathbf1_E\|_{L^{3,1}}=3|d||E|^{1/3}.
\]

Avec (means), cela donne

\[
\|(c_{k+1}-c_0)\mathbf1_{\mathcal A_k}\|_{L^{3,1}}
\le48\varpi_3^{1/3}B_\xi(2^kR)
\sum_{j=1}^{k+1}\phi(2^jR).
\]

En définissant

\[
C_L=\varpi_3^{1/3}
\left(2\,9^{3/4}C_{\rm JN,4}+48\right),
\]

on obtient

\[
\boxed{
\|(\xi-c_R)\mathbf1_{\mathcal A_k}\|_{L^{3,1}}
\le C_LB_\xi(2^kR)
\sum_{j=1}^{k+1}\phi(2^jR).
}
\tag{ann-L}
\]

La puissance \((2^kR)^1\) de (18) est donc exacte.

### 7.3 Contribution du \(k\)-ième anneau

Pour \(x\in B_R(z)\), \(y\in\mathcal A_k\),

\[
|x-y|\ge(2^k-1)R\ge2^{k-1}R.
\]

Le noyau est donc au plus \(8C_K(2^kR)^{-3}\). Hölder–Lorentz et (ann-L) donnent

\[
\boxed{
J_k(x)
\le
8C_KC_HC_LMB_\xi
(2^kR)^{-2}
\sum_{j=1}^{k+1}\phi(2^jR).
}
\tag{Jk}
\]

Cette formule recalcule séparément chaque anneau et confirme le facteur \(4^{-k}R^{-2}\) de (19).

## 8. Indices et somme double : (20)–(21)

Posons

\[
S_N=\sum_{k=1}^N4^{-k}
\sum_{j=1}^{k+1}\phi(2^jR).
\]

L’inversion exacte de l’ordre est

\[
S_N
=\sum_{j=1}^{N+1}\phi(2^jR)
\sum_{k=\max(1,j-1)}^N4^{-k}.
\]

Pour tout \(j\),

\[
\sum_{k=\max(1,j-1)}^N4^{-k}
\le\frac{16}{3}4^{-j}.
\tag{geom}
\]

Le dernier rayon satisfait seulement

\[
2^{N+1}R\le2\sqrt{RR_*},
\]

et non \(2^{N+1}R\le\sqrt{RR_*}\). Avec \(q=R/R_*\le2^{-6}\),

\[
\frac{\phi(2\sqrt{RR_*})}{\phi(R)}
=
\frac{1+\log(1/q)}{1+\frac12\log(1/q)-\log2}
<3.
\]

Ainsi \(\phi(2^jR)\le3\phi(R)\) pour tous les indices actifs, et

\[
\boxed{
S_N
\le\frac{16}{3}\phi(R).
}
\tag{SN}
\]

La constante \(2\) du papier est fausse au dernier anneau, mais la somme reste uniformément \(O(\phi(R))\).

En sommant (Jk), puis en utilisant

\[
\|\mathbf1_{B_R}\|_{L^{3/2,\infty}}
=\varpi_3^{2/3}R^2,
\]

on obtient

\[
\boxed{
\|I_{2,\mathrm{mid}}\|_{L^{3/2,\infty}(B_R(z))}
\le C_MMB_\xi\phi(R),
\quad
C_M=\frac{128}{3}
\varpi_3^{2/3}C_KC_HC_L.
}
\tag{Imid}
\]

Le \(R^{-2}\) ponctuel et le \(R^2\) de la norme de l’indicatrice se compensent exactement.

## 9. Lemme conditionnel minimal exact

### Lemme 0018-A — commutateur local à gain logarithmique

Soit \(\mathcal T\) une matrice finie d’opérateurs de Calderón–Zygmund de convolution sur \(\mathbb R^3\), satisfaisant (K) et la borne de commutateur (CRW). Soient \(\omega\ge0\) et \(\xi\) telles que (M), \(|\xi|\le1\), (BMOphi) et le raccord (C) soient vrais uniformément en temps. Alors, pour tout centre \(z\in\mathbb R^3\), tout temps de l’intervalle uniforme et tout \(0<R\le R_*/64\),

\[
\boxed{
\|\alpha(\cdot,t)\|_{L^{3/2,\infty}(B_R(z))}
\le
C_*M(B_\xi+1)\phi(R),
}
\tag{22q}
\]

où l’on peut prendre

\[
C_*=C_{\rm con}C_\triangle
\max\{C_N+C_{I_1}+C_M,\,C_F\}.
\]

Les constantes \(C_N,C_{I_1},C_F,C_M\) sont celles calculées dans (Near), (I1), (Ifar) et (Imid). Elles dépendent uniquement :

- de la dimension ;
- du nombre de composantes et de la constante de noyau de \(\mathcal T\) ;
- des constantes de Jones, Coifman–Rochberg–Weiss, John–Nirenberg et Hölder–Lorentz ;
- de la constante triangulaire \(C_\triangle\) de la quasi-norme faible choisie ;
- de la convention de norme de Lorentz.

Elles sont indépendantes de \(R,z,t,\omega,\xi\). Toute dépendance sur les champs est exposée dans \(M(B_\xi+1)\).

### Démonstration

La partie proche est (Near), \(I_1\) est (I1), la queue macroscopique est (Ifar) avec \(R/R_*\le\phi(R)\), et la somme intermédiaire est (Imid). La quasi-inégalité triangulaire de \(L^{3/2,\infty}\) introduit éventuellement une constante finie supplémentaire selon la norme choisie ; elle est absorbée dans \(C_*\). Si l’on emploie la norme équivalente fondée sur \(f^{**}\), l’inégalité triangulaire est une vraie inégalité de norme.

Cette dernière précision manque à la conclusion (22) : avec la quasi-norme \(\sup s^{2/3}f^*(s)\) définie dans le papier, la somme des normes faibles est valide à une constante universelle près, pas nécessairement avec coefficient un.

## 10. Dimensions et scaling Navier–Stokes

Sous

\[
u_\rho(x,t)=\rho u(\rho x,\rho^2t),
\quad
\omega_\rho(x,t)=\rho^2\omega(\rho x,\rho^2t),
\quad
\alpha_\rho(x,t)=\rho^2\alpha(\rho x,\rho^2t),
\]

on a

\[
\|\omega_\rho\|_{L^{3/2,\infty}}
=\|\omega\|_{L^{3/2,\infty}},
\qquad
\|\alpha_\rho\|_{L^{3/2,\infty}}
=\|\alpha\|_{L^{3/2,\infty}}.
\]

Les longueurs deviennent

\[
R_\rho=\rho^{-1}R,
\qquad
R_{*,\rho}=\rho^{-1}R_*,
\]

donc \(R/R_*\), \(L(R)\), \(\phi(R)\), \(B_\xi\), \(M\) et le membre droit de (22q) sont invariants. Le théorème réparé est exactement critique.

Les estimations ponctuelles de \(I_1\) et \(I_{2,\mathrm{mid}}\) ont la dimension \(T^{-1}\), avec un facteur \(MR^{-2}\). Leur norme faible localisée multiplie cette taille par \(R^2\), produisant \(L^2T^{-1}\), comme requis. La queue macroscopique produit \(M(R/R_*)\), également correcte.

## 11. Uniformité temporelle et dépendance du centre

La constante finale est uniforme en temps si les quantités suivantes le sont sur le même intervalle :

\[
M,\qquad B_\xi,\qquad R_*,\qquad C_K,\qquad C_{\rm con}.
\]

Les constantes analytiques universelles ne dépendent pas du temps. Aucune dérivée du centre n’apparaît, mais la boule de conclusion doit être centrée sur le même \(z(t)\) que la décomposition. Pour utiliser (22q) sur un superniveau, il faut séparément établir

\[
\{\omega(\cdot,t)>\lambda\}
\subset B_{R_\lambda}(z(t))
\]

avec une relation \(R_\lambda\)–\(\lambda\) et des constantes uniformes. La translation « sans perte de généralité » n’autorise pas à remplacer plusieurs cœurs simultanés par un seul cœur.

La constante de (22) ne dépend donc pas « exclusivement » de deux nombres non précisés : elle dépend linéairement de \(M\), au plus linéairement de \(B_\xi+1\), des constantes de l’opérateur, et de la normalisation de la semi-norme. Son indépendance en temps est conditionnelle à l’uniformité de toutes ces données.

## 12. Tests adverses reproductibles

### Test A — norme ou semi-norme BMO

Prenons \(\xi\equiv e_1\). Alors

\[
[\xi]_{\rm BMO(B_{2R})}=0
\]

pour tout \(R\), tandis qu’une norme ancrée contenant \(|\xi_{B_{2R}}|\) ou \(\|\xi\|_\infty\) vaut un. L’affirmation

\[
\|\widetilde\xi\|_{\rm BMO(\mathbb R^3)}
\le C\phi(2R)\to0
\]

est donc impossible pour une telle norme. Le commutateur est pourtant nul, confirmant que la semi-norme est l’objet exact.

### Test B — réarrangée de (12)

Pour \(a=1\) et \(s=\varpi_3\), la vraie valeur est

\[
h_1^*(\varpi_3)=\frac12,
\]

alors que \(\min(1,\varpi_3/s)=1\). Cela réfute l’identité « min » sans aucun calcul asymptotique. L’intégrale exacte (K31) confirme néanmoins la puissance \(a^{-2}\).

### Test C — dernier anneau

Pour \(R/R_*=2^{-m}\), le rapport au rayon extrême \(2\sqrt{RR_*}\) vaut, avec le poids sans le \(+1\) utilisé littéralement dans le papier,

\[
\frac{\phi(2\sqrt{RR_*})}{\phi(R)}
=\frac{m}{m/2-1}>2.
\]

Il vaut \(3\) pour \(m=6\) et tend vers \(2\) par valeurs supérieures. Le facteur \(2\) est réfuté pour tout \(m\) fini ; le facteur \(3\) est uniforme pour \(m\ge6\).

### Test D — saturation dimensionnelle d’un anneau

Sur un anneau de rayon \(r_k=2^kR\), prenons abstraitement une amplitude de vorticité critique telle que

\[
\|\omega\mathbf1_{\mathcal A_k}\|_{L^{3/2,\infty}}\sim M
\]

et une oscillation de taille \(B_\xi\phi(r_k)\). Le volume est \(r_k^3\), la norme \(L^{3,1}\) de l’oscillation est donc \(r_kB_\xi\phi(r_k)\), tandis que le noyau vaut \(r_k^{-3}\). La contribution est \(Mr_k^{-2}B_\xi\phi(r_k)\), exactement celle de (Jk). Ce test exclut toute amélioration gratuite du facteur \(r_k^{-2}\) avant sommation.

## 13. Statut maillon par maillon

| Maillon | Statut | Défaut ou condition exacte |
|---|---|---|
| (7) → séparation proche/lointaine | Conditionnel | Requiert le raccord tensoriel (C) et une extension définie de \(\xi\) sur \(\{\omega=0\}\). |
| BMO local → extension globale | Correct pour la semi-norme | Faux si « norme » inclut un ancrage ; constante de Jones uniforme pour les boules. |
| CRW → \(L^{3/2,\infty}\) | Correct | L’espace cible n’est pas réflexif ; utiliser interpolation entre deux bornes fortes. |
| (11)–(12) | Puissance correcte, formule ponctuelle fausse | Réarrangée exacte donnée par (h*), norme exacte par (K31). |
| (13)–(14), \(I_1\) | Correct | John–Nirenberg et injection finie donnent exactement \(R^2\phi(R)\). |
| (15), \(I_{2,\mathrm{far}}\) | Correct après dimensionnement | Coupure \(\sqrt{RR_*}\), facteur de translation du noyau et résultat \(M R/R_*\). |
| (16), moyennes | Correct | Rapport volumique exact \(8\), indices \(1\) à \(k+1\). |
| (17)–(19), anneaux | Correct à constantes suivies | Injection \(L^4\to L^{3,1}\) valide ; chaque anneau donne \(4^{-k}R^{-2}\) fois la somme. |
| (20), inversion des sommes | Correct | Borne géométrique explicite (geom). |
| (21), extraction du poids | Réparable | Facteur \(2\) faux au dernier anneau ; facteur \(3\) uniforme à partir de \(R/R_*\le2^{-6}\). |
| (22), somme en faible Lorentz | Correct à constante | La quasi-norme \(f^*\) peut ajouter une constante triangulaire ; conclusion (22q). |

## 14. Écart avec le problème Clay et prochain verrou

Le lemme 0018-A est une estimation d’analyse harmonique conditionnelle et statique. Il ne démontre pas :

- que la direction d’une solution Clay arbitraire satisfait (BMOphi) uniformément près d’un temps singulier ;
- que toute concentration critique possède un centre unique et une échelle de confinement uniforme ;
- que \(M\) reste fini pour toute solution lisse maximale ;
- que la définition de \(\xi\) sur les zéros de vorticité peut être choisie avec la semi-norme requise ;
- une assertion analogue sur le tore ou un domaine borné, où l’opérateur et les queues changent.

Le premier verrou transférable est précis : relier une hypothèse géométrique intrinsèque portant seulement sur la direction là où \(\omega\) est grande à une extension globale \(\xi\) satisfaisant (BMOphi), avec constante uniforme. Le théorème 4.1 suppose directement une régularité globale de l’extension de direction ; il ne produit pas ce raccord depuis les données Clay.

## Sources primaires

- Z. Grujić, *Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier–Stokes Equations*, arXiv:2607.08866v2, sections 3–4, [HTML primaire](https://arxiv.org/html/2607.08866v2), [notice arXiv](https://arxiv.org/abs/2607.08866v2).
- P. W. Jones, *Extension Theorems for BMO*, Indiana Univ. Math. J. 29 (1980), 41–66, [page éditeur](https://iumj.org/article/2860/), [DOI](https://doi.org/10.1512/iumj.1980.29.29005).
- R. R. Coifman, R. Rochberg et G. Weiss, *Factorization theorems for Hardy spaces in several variables*, Ann. of Math. 103 (1976), 611–635, [page éditeur](https://annals.math.princeton.edu/1976/103-3/p13), [DOI](https://doi.org/10.2307/1970954).
- R. A. Hunt, *On \(L(p,q)\) spaces*, L’Enseignement Mathématique 12 (1966), 249–276, [archive primaire](https://www.e-periodica.ch/digbib/view?pid=ens-001%3A1966%3A12%3A%3A408).

## Conclusion de la passe

**Résultat positif borné :** le lemme 0018-A rétablit (22) avec normes, dimensions, centre, indices, constantes et uniformité explicités.

**Résultats négatifs :** la petite « norme » BMO doit être une semi-norme ; l’argument de réflexivité est faux ; la formule de réarrangement avant (12) et le facteur \(2\) avant (21) sont faux comme identités exactes.

**État recommandé :** `CONTINUER` sur le raccord géométrique entre direction définie dans le cœur actif et extension globale pondérée. Les erreurs locales de (8)–(22) sont réparables et ne suffisent pas, seules, à réfuter le théorème conditionnel.
