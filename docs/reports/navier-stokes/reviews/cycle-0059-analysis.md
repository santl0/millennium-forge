# Cycle 0059 — projection hilbertienne sur la direction de rotation

Date : 2026-08-15.

Statut : **AI_INTERNAL_DERIVATION**. Audit analytique du lemme de projection
local et de sa variante hilbertienne globale pondérée; aucune implication
Clay. L'invariance rotationnelle conditionnelle est démontrée. La
stationnarité automatique est réfutée.

## Verdict révisé

La projection locale sur

\[
 X_R=H^{-3}(B_R)^3=(H_0^3(B_R)^3)^*
\]

est valide dès que le produit scalaire est fixé et \(SO(2)\)-invariant. Pour

\[
 d_n=\partial_s Z_n,\qquad g_n=\mathcal RZ_n,
\]

la définition

\[
 \beta_{n,R}(s)=
 \begin{cases}
 \displaystyle\frac{(d_n(s),g_n(s))_{X_R}}
 {\|g_n(s)\|_{X_R}^2},&g_n(s)\neq0,\\[1.1ex]
 0,&g_n(s)=0,
 \end{cases}
 \qquad
 r_n=d_n-\beta_{n,R}g_n                                      \tag{1}
\]

donne, presque partout,

\[
 (r_n,g_n)_{X_R}=0,\qquad
 \|d_n\|_{X_R}^2=\|r_n\|_{X_R}^2
       +|\beta_{n,R}|^2\|g_n\|_{X_R}^2.                       \tag{2}
\]

Ainsi

\[
 \boxed{\ \|r_n\|_{X_R}\leq\|d_n\|_{X_R},\qquad
 \|\beta_{n,R}g_n\|_{X_R}\leq\|d_n\|_{X_R}.\ }                \tag{3}
\]

La variante du rapport principal qui assemble toutes les boules dans une
somme hilbertienne pondérée est elle aussi valide, après une correction
définitionnelle précise. Pour une exhaustion \(B_m\uparrow\mathbb R^3\), des
bornes locales uniformes \(D_m,G_m<\infty\), et

\[
 w_m=\frac{2^{-m}}{1+D_m^2+G_m^2}>0,                         \tag{4}
\]

il faut définir \(X\) comme le sous-espace **fermé des familles compatibles**
de \(\bigoplus_m^{\,2}X_m\), ou, de manière équivalente, comme l'espace des
distributions localement dans tous les \(X_m\) et de norme pondérée finie.
L'expression « fermeture de l'image diagonale compatible » est insuffisante
si la classe diagonale initiale n'est pas précisée; elle ne constitue pas,
seule, une définition vérifiable.

Avec la définition corrigée, \(X\) est un Hilbert séparable, les restrictions
sont continues, l'action \(SO(2)\) est unitaire, et \(d_n,g_n:J\to X\) sont
fortement mesurables. La projection dans ce Hilbert fournit alors une seule
fonction \(\beta_n\), commune à tous les rayons. Si

\[
 b_{n,J}:=\operatorname*{ess\,inf}_{s\in J}|\beta_n(s)|
 \longrightarrow\infty,                                      \tag{5}
\]

alors

\[
 \|\mathcal RZ_n\|_{L^q(J;X)}
 \leq b_{n,J}^{-1}\|\partial_sZ_n\|_{L^q(J;X)}
 \longrightarrow0,                                           \tag{6}
\]

et chaque restriction locale tend vers zéro avec le facteur explicite
\(w_m^{-1/2}\). La construction globale répare donc le défaut de cohérence
en rayon de la projection locale.

Elle ne répare pas le verrou de stationnarité :

\[
 \partial_s\mathcal AZ_n=\mathcal Ar_n.                       \tag{7}
\]

La projection ne contrôle que la composante tangentielle instantanée. Une
hypothèse supplémentaire telle que
\(\mathcal Ar_n\to0\) dans les distributions demeure nécessaire.

## 1. Action de rotation et produit scalaire local

Soit \(K^T=-K\) le générateur d'un groupe de rotations autour d'un axe fixe
passant par le centre des boules. On pose

\[
 (Q_\gamma W)(y)=e^{\gamma K}W(e^{-\gamma K}y),\qquad
 \mathcal RW=KW-(Ky\cdot\nabla)W.                              \tag{8}
\]

Sur les distributions,

\[
 \langle\mathcal RW,\varphi\rangle
 =\langle W,(Ky\cdot\nabla)\varphi-K\varphi\rangle.             \tag{9}
\]

Le centrage est essentiel : \(Q_\gamma B_R=B_R\). L'action est fortement
continue et uniformément bornée sur \(H^{-3}(B_R)^3\). À partir d'un produit
scalaire hilbertien \((\cdot,\cdot)_0\) donnant cette topologie, on peut
définir

\[
 (f,h)_{X_R}=\frac1{2\pi}\int_0^{2\pi}
          (Q_\gamma f,Q_\gamma h)_0\,d\gamma.                 \tag{10}
\]

La norme obtenue est équivalente à la norme initiale. En effet, la compacité
du groupe fournit une borne uniforme \(M\) pour \(Q_\gamma\) et ses inverses,
donc

\[
 M^{-1}\|f\|_0\leq\|Q_\gamma f\|_0\leq M\|f\|_0.
\]

L'action \(Q_\gamma\) est unitaire pour (10). Sur le domaine de son
générateur, \(\mathcal R\) est antisymétrique. La moyenne de Haar

\[
 \mathcal A=\frac1{2\pi}\int_0^{2\pi}Q_\gamma\,d\gamma         \tag{11}
\]

est la projection orthogonale sur le sous-espace fixe et
\(\mathcal A\mathcal R=0\).

Le produit scalaire doit être fixé avant la projection. Le coefficient local
\(\beta_{n,R}\) dépend en général du produit choisi et du rayon \(R\); il
n'est pas une vitesse angulaire intrinsèque sans convention supplémentaire.

## 2. Plongement du ledger brut dans \(H^{-3}\)

En dimension trois et sur une boule bornée,

\[
 H_0^3(B_R)\hookrightarrow W_0^{2,4}(B_R).                    \tag{12}
\]

On peut utiliser

\[
 W^{3,2}(B_R)\hookrightarrow W^{2,6}(B_R)
                  \hookrightarrow W^{2,4}(B_R),               \tag{13}
\]

puis passer à la fermeture de \(C_c^\infty(B_R)\). Par dualité,

\[
 (W_0^{2,4})^*=W^{-2,4/3}
 \hookrightarrow(H_0^3)^*=H^{-3}.                             \tag{14}
\]

La constante \(C_{\mathrm{emb}}(R)\) dépend du rayon. La borne du ledger brut

\[
 \sup_n\|\partial_sZ_n\|_{L^\infty
          (J;W^{-2,4/3}(B_R))}
 \leq C^{(2)}_{J,R}                                           \tag{15}
\]

implique

\[
 \sup_n\|d_n\|_{L^\infty(J;X_R)}
 \leq C_{\mathrm{emb}}(R)C^{(2)}_{J,R}.                       \tag{16}
\]

Par ailleurs, \(Z_n\in L^\infty(J;L^2(B_R))\) suffit à placer
\(g_n=\mathcal RZ_n\) dans

\[
 H^{-1}(B_R)^3\hookrightarrow H^{-3}(B_R)^3,
\]

car \(Ky\) est borné sur \(B_R\) dans (9). Aucune dérivée spatiale forte de
\(Z_n\) n'est nécessaire pour construire \(g_n\).

Après le ledger d'énergie, la borne plus forte

\[
 \partial_sZ_n\text{ borné dans }
 L^2(J;W^{-1,4/3}(B_R)^3)                                     \tag{17}
\]

se plonge aussi dans \(L^2(J;X_R)\). Aucune uniformité lorsque
\(R\to\infty\) n'est obtenue par ces seuls plongements.

## 3. Mesurabilité locale

La borne de Bochner (15) fournit un représentant fortement mesurable
\(d_n:J\to X_R\). La forte mesurabilité de
\(Z_n:J\to L^2(B_R)^3\), suivie de l'application continue

\[
 \mathcal R:L^2(B_R)^3\longrightarrow H^{-1}(B_R)^3
                       \longrightarrow X_R,                  \tag{18}
\]

donne celle de \(g_n\). La continuité du produit scalaire implique la
mesurabilité de

\[
 a_n(s)=(d_n(s),g_n(s))_{X_R},\qquad
 c_n(s)=\|g_n(s)\|_{X_R}^2.                                  \tag{19}
\]

Le quotient \(a_n/c_n\) sur l'ensemble mesurable
\(\{c_n>0\}\), prolongé par zéro sur \(\{c_n=0\}\), est mesurable. Il en va
de même de \(\beta_{n,R}g_n\) et de \(r_n\).

Il n'en résulte aucune intégrabilité uniforme de \(\beta_{n,R}\). Dans une
direction unitaire \(e\), les choix

\[
 d_\varepsilon=\varepsilon e,\qquad
 g_\varepsilon=\varepsilon^2e
\]

donnent \(\beta_\varepsilon=\varepsilon^{-1}\), tandis que
\(\beta_\varepsilon g_\varepsilon=\varepsilon e\). La définition à zéro
évite une singularité de la projection vectorielle, pas celle du quotient
scalaire.

## 4. Orthogonalité et borne sans dégénérescence

Lorsque \(g_n(s)\neq0\), la définition (1) est l'unique minimiseur de

\[
 \lambda\longmapsto\|d_n(s)-\lambda g_n(s)\|_{X_R}^2.          \tag{20}
\]

Elle donne

\[
 (d_n-\beta_{n,R}g_n,g_n)_{X_R}=0.                            \tag{21}
\]

Sur \(\{g_n=0\}\), cette identité reste vraie et \(r_n=d_n\). Pythagore
donne donc (2), puis

\[
 |\beta_{n,R}|\,\|g_n\|_{X_R}
 =\|\beta_{n,R}g_n\|_{X_R}\leq\|d_n\|_{X_R}.                  \tag{22}
\]

Pour le résidu canonique, aucune borne indépendante sur \(r_n\) n'est
nécessaire : \(r_n\) est déjà une projection orthogonale de \(d_n\).

Si

\[
 b_{n,J,R}:=\operatorname*{ess\,inf}_{s\in J}
              |\beta_{n,R}(s)|\longrightarrow\infty,          \tag{23}
\]

alors \(\{g_n=0\}\) est de mesure nulle pour les grands \(n\), puisque la
convention (1) y impose \(\beta_{n,R}=0\). Pour
\(1\leq q\leq\infty\),

\[
 \|\mathcal RZ_n\|_{L^q(J;X_R)}
 \leq b_{n,J,R}^{-1}
       \|\partial_sZ_n\|_{L^q(J;X_R)}.                        \tag{24}
\]

En particulier,

\[
 \|\mathcal RZ_n\|_{L^\infty(J;X_R)}
 \leq
 \frac{C_{\mathrm{emb}}(R)C^{(2)}_{J,R}}{b_{n,J,R}}
 \longrightarrow0.                                           \tag{25}
\]

La quantité contrôlée uniformément est \(\beta_{n,R}g_n\), jamais
\(\beta_{n,R}\) seule.

## 5. Construction hilbertienne globale pondérée

### 5.1 Définition exacte

Fixons l'exhaustion centrée \(B_m\), \(m\geq1\), et écrivons

\[
 X_m=H^{-3}(B_m)^3
\]

avec les produits scalaires invariants de la section 1. Pour
\(k\geq m\), la restriction distributionnelle

\[
 \rho_{k,m}:X_k\longrightarrow X_m                              \tag{26}
\]

est continue. En effet, son adjoint est l'extension par zéro

\[
 E_{m,k}:H_0^3(B_m)^3\longrightarrow H_0^3(B_k)^3,
\]

qui est continue : elle se construit d'abord sur
\(C_c^\infty(B_m)^3\), puis par fermeture. Les normes invariantes peuvent
modifier la constante de (26), mais pas la continuité. Les restrictions sont
équivariantes :

\[
 \rho_{k,m}Q_\gamma=Q_\gamma\rho_{k,m}.                       \tag{27}
\]

Considérons la somme hilbertienne pondérée

\[
 \mathcal H_w=
 \left\{(f_m)_{m\geq1}:
   f_m\in X_m,\quad
   \sum_{m\geq1}w_m\|f_m\|_{X_m}^2<\infty\right\},             \tag{28}
\]

munie du produit scalaire correspondant. Définissons

\[
 X=
 \left\{(f_m)\in\mathcal H_w:
   \rho_{k,m}f_k=f_m\ \text{pour tous }k\geq m\right\}.        \tag{29}
\]

Pour chaque paire \(k\geq m\), l'application

\[
 (f_j)_j\longmapsto \rho_{k,m}f_k-f_m
\]

est continue de \(\mathcal H_w\) vers \(X_m\), puisque toute projection
coordonnée a une norme au plus \(w_j^{-1/2}\). Par conséquent, \(X\) est
l'intersection dénombrable de noyaux fermés. Il est fermé dans
\(\mathcal H_w\), donc complet et hilbertien. Comme les \(X_m\) sont
séparables, \(\mathcal H_w\), puis \(X\), sont séparables.

Chaque famille compatible de (29) se recolle en une unique distribution
\(f\in\mathcal D'(\mathbb R^3)^3\) : pour un test compactement supporté,
on choisit un \(m\) contenant son support et on utilise \(f_m\); la
compatibilité rend la valeur indépendante de \(m\). Réciproquement, toute
distribution dont les restrictions sont dans les \(X_m\) et vérifient

\[
 \sum_{m\geq1}w_m
       \|f|_{B_m}\|_{X_m}^2<\infty                              \tag{30}
\]

définit un élément de \(X\).

Ainsi, la formulation rigoureuse est

\[
 X\simeq
 \left\{f\in\mathcal D'(\mathbb R^3)^3:
 f|_{B_m}\in X_m,\ \|f\|_X^2
 =\sum_{m\geq1}w_m\|f|_{B_m}\|_{X_m}^2<\infty\right\}.         \tag{31}
\]

Avec (29) ou (31), aucune complétion supplémentaire n'est nécessaire. Si
l'on préfère parler de « fermeture de l'image diagonale », il faut nommer
la classe initiale et montrer que sa fermeture est le sous-espace voulu.
La fermeture d'une classe non spécifiée est un défaut définitionnel; elle
peut être un sous-espace fermé strict de (29). Ce défaut ne réfute pas la
construction, mais exige la correction (29).

### 5.2 Choix des poids et bornes uniformes

Sur la fenêtre bornée \(J\), supposons que les enveloppes

\[
 D_m=\sup_n\|d_n\|_{L^\infty(J;X_m)}<\infty,\qquad
 G_m=\sup_n\|g_n\|_{L^\infty(J;X_m)}<\infty                  \tag{32}
\]

soient calculées dans les normes invariantes fixées. Avec les poids (4),

\[
 \begin{aligned}
 \|d_n(s)\|_X^2
 &\leq\sum_{m\geq1}
 2^{-m}\frac{D_m^2}{1+D_m^2+G_m^2}\leq1,\\
 \|g_n(s)\|_X^2
 &\leq\sum_{m\geq1}
 2^{-m}\frac{G_m^2}{1+D_m^2+G_m^2}\leq1
 \end{aligned}                                                \tag{33}
\]

pour presque tout \(s\), après réunion des ensembles négligeables sur
l'ensemble dénombrable des rayons et des indices.

Les poids doivent être :

- strictement positifs;
- fixés une fois pour toute sur \(J\);
- indépendants de \(n\) et de \(s\);
- construits avec des enveloppes réellement uniformes.

S'ils variaient avec \(n\), les projections seraient prises dans des
Hilbert différents et la fonction \(\beta_n\) ne serait plus comparable
dans une géométrie commune. La construction dépend toutefois de la suite et
de \(J\). Pour traiter plusieurs fenêtres, il faut épingler une famille de
poids commune ou refaire explicitement la construction sur chaque fenêtre.
Elle est globale en espace, pas canonique au sens intrinsèque.

### 5.3 Unitarité et restrictions

L'action diagonale

\[
 Q_\gamma(f_m)_m=(Q_\gamma f_m)_m                             \tag{34}
\]

est unitaire sur \(\mathcal H_w\). Grâce à (27), elle préserve \(X\); elle
y est donc unitaire et fortement continue. La restriction

\[
 \operatorname{res}_m:X\longrightarrow X_m,\qquad
 f\longmapsto f_m
\]

est continue avec la constante explicite

\[
 \boxed{\ \|f|_{B_m}\|_{X_m}\leq w_m^{-1/2}\|f\|_X.\ }         \tag{35}
\]

Cette constante peut croître très vite avec \(m\). La construction
pondérée encode tous les contrôles locaux, mais ne produit aucune estimation
uniforme lors du passage \(m\to\infty\).

### 5.4 Forte mesurabilité dans \(X\)

Pour chaque \(m\), les applications

\[
 s\longmapsto d_n(s)|_{B_m},\qquad
 s\longmapsto g_n(s)|_{B_m}
\]

sont fortement mesurables dans \(X_m\). Après choix d'un ensemble nul commun,
elles sont compatibles. Les troncatures coordonnées dans
\(\mathcal H_w\) sont fortement mesurables et, par (32)--(33), leurs queues
satisfont uniformément

\[
 \sum_{m>M}w_m\|d_n(s)|_{B_m}\|_{X_m}^2
 \leq\sum_{m>M}2^{-m},                                       \tag{36}
\]

et de même pour \(g_n\). Elles convergent donc uniformément en \(s\), dans
\(\mathcal H_w\), vers les applications diagonales. Celles-ci sont
fortement mesurables; comme leurs valeurs appartiennent au sous-espace fermé
\(X\), elles sont fortement mesurables comme applications à valeurs dans
\(X\).

La même conclusion découle de Pettis : \(X\) est séparable et la
mesurabilité coordonnée donne la mesurabilité faible. L'argument par (36)
suit toutefois explicitement la constante de queue.

### 5.5 Projection globale et récupération locale

Dans \(X\), posons

\[
 \beta_n(s)=
 \begin{cases}
 \displaystyle\frac{(d_n(s),g_n(s))_X}{\|g_n(s)\|_X^2},
 &g_n(s)\neq0,\\[1.1ex]
 0,&g_n(s)=0,
 \end{cases}
 \qquad
 r_n=d_n-\beta_ng_n.                                         \tag{37}
\]

Les arguments des sections 3--4 s'appliquent sans changement :

\[
 (r_n,g_n)_X=0,\qquad
 \|d_n\|_X^2=\|r_n\|_X^2+|\beta_n|^2\|g_n\|_X^2,              \tag{38}
\]

et

\[
 \|r_n\|_X,\ \|\beta_ng_n\|_X\leq\|d_n\|_X.                  \tag{39}
\]

Cette \(\beta_n\) est une seule fonction scalaire pour toute l'exhaustion.
Sous (5),

\[
 \|g_n\|_{L^q(J;X)}
 \leq b_{n,J}^{-1}\|d_n\|_{L^q(J;X)}.                        \tag{40}
\]

En combinant (35) et (40), pour chaque rayon fixé,

\[
 \boxed{
 \|\mathcal RZ_n\|_{L^q(J;X_m)}
 \leq
 w_m^{-1/2}b_{n,J}^{-1}
 \|\partial_sZ_n\|_{L^q(J;X)}.}                              \tag{41}
\]

La convergence vaut donc simultanément sur chaque boule fixée. Une diagonale
supplémentaire en rayon n'est pas requise, même si les constantes locales
restent dépendantes de \(m\).

## 6. Passage à la limite distributionnelle

Supposons

\[
 Z_n\longrightarrow Z
 \quad\text{fortement dans }L^3_{\mathrm{loc}}.               \tag{42}
\]

Pour tout test \(\varphi\in C_c^\infty(J\times\mathbb R^3)^3\), (9) donne

\[
 \langle\mathcal R(Z_n-Z),\varphi\rangle
 =
 \langle Z_n-Z,(Ky\cdot\nabla)\varphi-K\varphi\rangle
 \longrightarrow0.                                           \tag{43}
\]

D'autre part, (41), appliquée à une boule contenant le support du test,
donne \(\mathcal RZ_n\to0\) dans les distributions. Par unicité,

\[
 \boxed{\mathcal RZ=0\quad\text{sur }
 J\times\mathbb R^3.}                                         \tag{44}
\]

Ainsi

\[
 Q_\gamma Z=Z\quad(\gamma\in\mathbb R),\qquad
 \mathcal AZ=Z.                                                \tag{45}
\]

La variante globale transforme donc correctement l'hypothèse unique (5) en
invariance sur tous les rayons.

## 7. Pression et dual solénoïdal

La borne de \(d_n\) dans le dual vectoriel complet utilise l'équation
complète et une pression locale uniformément contrôlée, par exemple la jauge
globale de Riesz

\[
 \Pi_n=R_iR_j(Z_{n,i}Z_{n,j}).                                \tag{46}
\]

Les termes de diffusion, convection, drift et pression placent alors
\(\partial_sZ_n\) dans \(W^{-2,4/3}(B_m)^3\), puis dans \(X_m\).

Si seule la formulation testée contre les champs divergence-free est
disponible, il faut construire des espaces \(X_{m,\sigma}\), puis leur somme
compatible pondérée. Le coefficient projeté dans ce dual solénoïdal peut
différer de (37). L'annulation dans ce dual ne doit pas être promue sans
preuve en annulation comme distribution vectorielle : une ambiguïté locale
de gradient demeure sans reconstruction de pression ou argument de de Rham.

Pour passer (46) à la limite, la forte convergence locale du stress dans
\(L^{3/2}\) traite la partie proche; la borne globale faible-\(L^{3/2}\) et
la dualité de Lorentz contrôlent la queue. La projection hilbertienne ne
fournit aucun nouveau contrôle de pression et ne remplace pas ce ledger.

## 8. Loi d'échelle

Les espaces \(H^{-3}(B_m)\), leurs normes inhomogènes, les poids \(w_m\) et
l'exhaustion ne sont pas invariants sous l'échelle Clay

\[
 u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t).              \tag{47}
\]

Sur l'espace entier homogène, pour la mise à l'échelle d'une vitesse

\[
 (S_\lambda f)(x)=\lambda f(\lambda x),
\]

on a

\[
 \|S_\lambda f\|_{\dot H^{-3}(\mathbb R^3)}
 =\lambda^{-7/2}\|f\|_{\dot H^{-3}(\mathbb R^3)}.              \tag{48}
\]

Pour un terme ayant l'échelle physique d'une force ou de
\(\partial_tu\),

\[
 (T_\lambda f)(x)=\lambda^3 f(\lambda x),
\]

le facteur est

\[
 \|T_\lambda f\|_{\dot H^{-3}(\mathbb R^3)}
 =\lambda^{-3/2}\|f\|_{\dot H^{-3}(\mathbb R^3)}.              \tag{49}
\]

Le générateur de rotation commute avec les dilatations centrées. Si \(d\) et
\(g\) subissent la même dilatation et sont mesurés dans un produit homogène,
le facteur quadratique s'annule dans le quotient définissant \(\beta\). Sur
le Hilbert pondéré (31), une dilatation change les boules, les normes locales
et les poids : aucune invariance de \(\beta_n\) ne doit être revendiquée.

Dans le temps similaire \(s\), \(\beta_n\) a la dimension d'une fréquence
en \(s\). Elle dépend de \(J\), des enveloppes \(D_m,G_m\), de l'exhaustion
et des produits scalaires. Il s'agit d'un coefficient de régression
tangentielle épinglé, pas d'une quantité critique intrinsèque de
Navier--Stokes.

## 9. Pourquoi la stationnarité ne suit pas

La moyenne de Haar est une contraction sur chaque \(X_m\), puis sur \(X\).
En appliquant \(\mathcal A\) à

\[
 d_n=r_n+\beta_ng_n                                           \tag{50}
\]

et en utilisant
\(\mathcal Ag_n=\mathcal A\mathcal RZ_n=0\), on obtient

\[
 \boxed{\partial_s\mathcal AZ_n=\mathcal Ar_n.}                \tag{51}
\]

L'orthogonalité \(r_n\perp g_n\) ne signifie pas
\(\mathcal Ar_n=0\). Elle retire une seule direction instantanée, alors que
le sous-espace invariant est de dimension infinie. Les bornes
\(\|r_n\|\leq\|d_n\|\) et \(g_n\to0\) donnent au plus une borne sur
l'évolution moyenne, jamais sa petitesse.

### Contre-modèle fonctionnel

Dans le Hilbert \(SO(2)\)-unitaire \(X\), choisissons une courbe lisse non
constante \(U(s)\) dans le sous-espace fixe et un champ lisse,
compactement supporté, divergence-free \(W\) tel que
\(\mathcal RW\neq0\). Posons

\[
 Z_n(s)=U(s)+\frac1nQ_{ns}W.                                  \tag{52}
\]

Alors

\[
 g_n=\frac1nQ_{ns}\mathcal RW,\qquad
 d_n=U'(s)+Q_{ns}\mathcal RW.                                 \tag{53}
\]

Le sous-espace fixe est orthogonal à l'image du générateur. L'unitarité
donne

\[
 (d_n,g_n)_X=\frac1n\|\mathcal RW\|_X^2,\qquad
 \|g_n\|_X^2=\frac1{n^2}\|\mathcal RW\|_X^2,                  \tag{54}
\]

d'où

\[
 \beta_n=n,\qquad r_n=U'(s),\qquad Z_n\to U.                  \tag{55}
\]

Toutes les identités de projection sont satisfaites, \(d_n\) et \(r_n\)
sont uniformément bornés, \(g_n\to0\), mais \(U(s)\) est rotationnel et non
stationnaire.

Ce contre-modèle n'est pas affirmé être une solution de Navier--Stokes. Il
réfute l'inférence fonctionnelle automatique depuis projection, compacité et
Haar. Une rigidité PDE pourrait encore exclure ces trajectoires, mais elle
n'est contenue dans aucun des arguments précédents. L'autonomie de
l'équation ne suffit pas : une équation autonome peut admettre des
trajectoires axisymétriques dépendantes du temps.

La condition discriminante exacte est

\[
 \mathcal Ar_n\longrightarrow0
 \quad\text{dans }\mathcal D'(J\times\mathbb R^3).             \tag{56}
\]

Avec (42), (45), (51) et (56),

\[
 \partial_sZ=\partial_s\mathcal AZ=0.
\]

La condition plus forte \(r_n\to0\) suffit; une simple bornitude de \(r_n\)
ne suffit pas.

## 10. Passe contradictoire

1. **Zéro de \(g_n\).** La convention \(\beta_n=0\) rend la projection
   mesurable, mais (5) force \(\{g_n=0\}\) à être nul pour les grands \(n\).
   Une suite exactement axisymétrique ne peut pas avoir une grande vitesse
   canonique selon (37).
2. **Explosion du quotient.** Pythagore borne \(\beta_ng_n\), pas
   \(\beta_n\). Aucune borne de variation ou intégrabilité de \(\beta_n\)
   n'en découle.
3. **Classe diagonale.** « Prendre la fermeture » sans espace de départ
   laisse \(X\) indéterminé. La définition par noyaux fermés (29) corrige ce
   défaut.
4. **Complétude.** Elle ne découle pas de la seule compatibilité verbale;
   elle découle du caractère fermé démontré après (29).
5. **Restriction négative.** La continuité de (26) repose sur l'extension
   par zéro de \(H_0^3(B_m)\), et non sur une restriction naïve de tests
   \(H^3\) ne satisfaisant pas les traces.
6. **Poids mobiles.** Si \(D_m,G_m\), donc \(w_m\), varient avec \(n\) ou
   \(s\), il n'existe plus un Hilbert commun. Ils peuvent dépendre de la
   suite et de la fenêtre, mais doivent ensuite être épinglés.
7. **Mesurabilité.** La mesurabilité locale seule doit être réunie sur un
   ensemble nul dénombrable; la queue (36) donne ensuite la forte
   mesurabilité globale.
8. **Domaine infini.** La norme pondérée ne donne pas une constante uniforme
   en rayon. Le coût exact est \(w_m^{-1/2}\).
9. **Pression.** La borne vectorielle complète de \(d_n\) exige le ledger de
   pression. La version solénoïdale est une autre géométrie de projection.
10. **Échelle.** \(X\) n'est pas critique et dépend de l'exhaustion. Une
    grande valeur de \(\beta_n\) n'est pas stable sous changement de ces
    choix.
11. **Passage à la limite.** La convergence de \(g_n\) dans \(X\) identifie
    \(\mathcal RZ\) seulement si \(Z_n\to Z\) au moins dans les
    distributions.
12. **Haar.** \(\mathcal A\mathcal R=0\) élimine la composante
    tangentielle, mais conserve \(\mathcal Ar_n\), qui porte précisément
    l'évolution du mode invariant.
13. **Stationnarité.** Le contre-modèle (52)--(55) interdit toute conclusion
    fonctionnelle automatique. Une preuve PDE doit établir (56) ou une
    rigidité équivalente.
14. **Portée Clay.** Ni (5), ni la cohérence temporelle des poids, ni (56)
    ne découlent d'un blow-up Clay général.

## 11. Statut logique

| Implication | Statut |
|---|---|
| moyenne locale (10) | **PROUVÉ** : norme hilbertienne équivalente et action unitaire |
| \(W^{-2,4/3}(B_R)\hookrightarrow H^{-3}(B_R)\) | **PROUVÉ** par (12)--(14) |
| restrictions \(\rho_{k,m}:X_k\to X_m\) | **PROUVÉ** continues par extension nulle des tests |
| sous-espace compatible (29) | **PROUVÉ** fermé, complet et séparable |
| recollement d'une famille compatible | **PROUVÉ** dans \(\mathcal D'(\mathbb R^3)^3\) |
| poids (4) et enveloppes (32) | **PROUVÉ** : bornes globales (33) |
| forte mesurabilité de \(d_n,g_n:J\to X\) | **PROUVÉ** par troncature et queue (36) |
| projection (37) | **PROUVÉ** mesurable, orthogonale et contractive |
| (5) \(\Rightarrow\mathcal RZ_n\to0\) dans chaque \(X_m\) | **PROUVÉ** avec le coût (41) |
| compacité de \(Z_n\) \(\Rightarrow\mathcal RZ=0\) globalement | **PROUVÉ** par (42)--(44) |
| « fermeture de l'image diagonale » sans classe initiale | **SOUS-SPÉCIFIÉ**, remplacé par (29) |
| \(\mathcal RZ=0\Rightarrow\partial_sZ=0\) | **RÉFUTÉ comme conséquence fonctionnelle automatique** par (52)--(55) |
| \(\mathcal Ar_n\to0\Rightarrow\partial_sZ=0\) | **PROUVÉ** sous la compacité indiquée |
| lemme de projection \(\Rightarrow\) résolution Clay | **NON DÉMONTRÉ** |

**Décision analytique révisée : CONTINUER.** La construction hilbertienne
globale pondérée est valide avec la définition fermée (29) et fournit bien
une seule \(\beta_n\) commune à tous les rayons d'une fenêtre \(J\). Elle
répare le problème de cohérence spatiale signalé dans la première version de
l'audit, au prix d'une métrique dépendant de la suite, de \(J\), des
enveloppes et de l'exhaustion. Elle ne produit ni quantité critique
intrinsèque ni stationnarité. Le prochain verrou reste la petitesse de la
composante de Haar \(\mathcal Ar_n\), ou une rigidité PDE équivalente.
