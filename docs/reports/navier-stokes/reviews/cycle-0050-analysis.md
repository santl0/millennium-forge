# Cycle 0050 — cocycle des redémarrages anciens et quotient énergétique

Date : 2026-08-15.

Statut : AI_INTERNAL_DERIVATION; audit analytique indépendant, sans
simulation et sans conclusion Clay.

## Verdict

Soit \(v\) la solution ancienne conditionnelle issue du cycle 0049 :
solution faible adaptée locale des équations de Navier--Stokes
incompressibles non forcées sur
\(\mathbb R^3\times(-\infty,T)\), de viscosité un, avec pression globale

\[
 q=\mathcal R_i\mathcal R_j(v_iv_j),\qquad
 \sup_{\tau<T}\|v(\tau)\|_{L^{3,\infty}}\le M.             \tag{1}
\]

On utilise son représentant
\(v\in C_{w^*}((-\infty,T);L^{3,\infty}_\sigma)\). Pour
\(s<t<T\), posons

\[
 V_s(t)=S(t-s)v(s),\qquad
 w_s(t)=v(t)-V_s(t),\qquad
 g_{s,t}=w_s(t),\qquad S(h)=e^{h\Delta}.                  \tag{2}
\]

Le cycle 0049 donne, sur chaque bande finie,

\[
\begin{aligned}
 &g_{s,\cdot}\in
 C([s,t];L^2_\sigma)\cap L^2(s,t;\dot H^1_\sigma),\\
 &g_{s,s}=0,\qquad
 \|g_{s,t}\|_2\le C_D M^2(t-s)^{1/4}.                    \tag{3}
\end{aligned}
\]

Les six points demandés ont le statut suivant.

1. **Cocycle : positif.** Pour tous \(s<r<t<T\),

   \[
    \boxed{g_{s,t}=g_{r,t}+S(t-r)g_{s,r}}                 \tag{4}
   \]

   dans \(L^2_\sigma\cap L^{3,\infty}_\sigma\), après fixation du
   représentant temporel.
2. **Énergie de transition : positive et exacte.** Le champ
   \(z_{s,r}(\tau)=S(\tau-r)g_{s,r}\) vérifie l'égalité calorifique

   \[
    \boxed{\|z_{s,r}(t)\|_2^2+
    2\int_r^t\|\nabla z_{s,r}(\tau)\|_2^2\,d\tau
    =\|g_{s,r}\|_2^2.}                                    \tag{5}
   \]

3. **Disparition du fond calorique : positive mais locale/sous-critique.**
   Pour \(t<T\) fixé,

   \[
    \|V_s(t)\|_\infty\le CM(t-s)^{-1/2}\longrightarrow0
    \quad(s\to-\infty),                                   \tag{6}
   \]

   donc \(V_s(t)\to0\) fortement dans tout \(L^p_{\rm loc}\),
   \(1\le p\le\infty\), en particulier dans \(L^2_{\rm loc}\).
   Aucune convergence en norme \(L^{3,\infty}\) n'en résulte.
4. **Uniformité énergétique : positive comme critère de rigidité.** Si,
   pour un \(r<T\), il existe seulement une suite \(s_n\to-\infty\) telle
   que

   \[
    \sup_n\|g_{s_n,r}\|_2<\infty,                          \tag{7}
   \]

   alors \(v(r)\in L^2_\sigma\). La borne uniforme pour tous les temps de
   base est donc plus que suffisante. Le majorant (3), qui croît comme
   \((r-s)^{1/4}\), ne donne pas (7).
5. **Quotient : à réviser topologiquement.** Le quotient
   \(L^{3,\infty}_\sigma/(L^2_\sigma\cap L^{3,\infty}_\sigma)\) est
   parfaitement défini comme quotient algébrique, mais le sous-espace
   dénominateur n'est pas fermé dans \(L^{3,\infty}\). Sa « norme quotient »
   n'est donc qu'une semi-norme et le quotient n'est pas séparé. Pour un
   quotient de Banach, il faut diviser par la fermeture du sous-espace.
6. **Profil \(U\) : positif comme contre-profil calorifique, négatif comme
   profil Navier--Stokes.** Pour

   \[
    U(x)=\frac{(-x_2,x_1,0)}{|x|^2},                       \tag{8}
   \]

   on a \(U\in L^{3,\infty}_\sigma\setminus L^2\) et, pour tout \(h>0\),

   \[
    (I-S(h))U\in L^2_\sigma\cap L^{3,\infty}_\sigma,
    \qquad
    \boxed{\|(I-S(h))U\|_2=C_Uh^{1/4}},                   \tag{9}
   \]

   avec \(C_U>0\) explicite. Ainsi \([S(h)U]=[U]\), et cette classe est
   non nulle même dans le quotient séparé. En revanche, \(U\) ne satisfait
   pas les équations stationnaires de Navier--Stokes non forcées, même loin
   de l'origine. Il ne constitue donc ni une solution ancienne admissible,
   ni un contre-exemple PDE.

   La variante lisse

   \[
    U_\sharp=\chi(|x|)U,\qquad
    \chi=0\text{ sur }[0,1],\quad \chi=1\text{ sur }[2,\infty),       \tag{9a}
   \]

   est solénoïdale, bornée,
   \(U_\sharp\in\widetilde L^{3,\infty}_\sigma\cap\dot H^1_\sigma\)
   mais \(U_\sharp\notin L^2\). Ses incréments appartiennent à
   \(L^2\cap\dot H^1\) et

   \[
    \|(I-S(h))U_\sharp\|_2
    =C_Uh^{1/4}+O(1)\quad(h\to\infty).                     \tag{9b}
   \]

   Cette variante élimine les défauts de régularité à l'origine du profil
   brut, sans réparer sa faille Navier--Stokes.

Le résultat scientifique est un **critère négatif précis** : la cohérence
des redémarrages et l'énergie exacte de leur transition ne donnent pas la
borne uniforme (7). Le profil \(U\) montre que la croissance
\((r-s)^{1/4}\) est compatible exactement avec la structure calorifique et
avec une classe quotient ancienne non nulle. Tout progrès de rigidité doit
donc utiliser une propriété Navier--Stokes supplémentaire, et non le seul
cocycle.

## 1. Traces et espaces où les identités valent

Sans choix de représentant, \(v(s)\) n'est défini que pour presque tout
\(s\), et (4) ne pourrait être affirmée qu'aux temps de Lebesgue. Le cycle
0048 a construit un représentant unique

\[
 v\in C_{w^*}((-\infty,T);X),\qquad
 X=L^{3,\infty}_\sigma(\mathbb R^3),                       \tag{10}
\]

pour lequel la formule de Duhamel faible-étoile vaut à tous les temps.
Toutes les traces de (2) sont prises dans ce représentant. Le semi-groupe
\(S(h)\) est borné sur \(X\), préserve la divergence nulle et satisfait la
loi de semi-groupe dans \(X\) et dans les distributions tempérées.

Pour chaque bande finie \([s,t]\), (3) place \(g_{s,t}\) dans \(L^2\).
Par ailleurs,

\[
 g_{s,t}=v(t)-S(t-s)v(s)\in X.                            \tag{11}
\]

Ainsi \(g_{s,t}\in Y:=L^2_\sigma\cap X\). L'égalité d'éléments de \(X\)
obtenue algébriquement ci-dessous est donc simultanément une égalité dans
\(L^2\), puisque ses trois termes appartiennent à \(L^2\).

La pression n'intervient pas dans l'identité de cocycle. Pour chaque temps
de base, \(w_s\) satisfait la même équation perturbée avec la pression
complète \(q\); la différence de deux fonds est calorifique, sans pression.
On ne soustrait aucune inégalité d'énergie BSS pour démontrer (4).

## 2. Identité de cocycle

Pour \(s<r<t\), la loi de semi-groupe donne

\[
 S(t-r)S(r-s)=S(t-s).                                    \tag{12}
\]

Par définition,

\[
\begin{aligned}
 g_{r,t}+S(t-r)g_{s,r}
 &=
 v(t)-S(t-r)v(r)\\
 &\quad+S(t-r)\bigl(v(r)-S(r-s)v(s)\bigr)\\
 &=v(t)-S(t-s)v(s)=g_{s,t}.                              \tag{13}
\end{aligned}
\]

Aucune unicité des solutions à grande donnée n'est utilisée : les trois
correcteurs proviennent de la même solution distributionnelle \(v\).
L'identité n'identifie pas deux solutions BSS construites séparément.

Le même calcul donne, pour \(\tau\ge r\),

\[
 w_s(\tau)=w_r(\tau)+z_{s,r}(\tau),\qquad
 z_{s,r}(\tau)=S(\tau-r)g_{s,r}.                          \tag{14}
\]

Le champ \(z_{s,r}\) est la transition calorique exacte entre les deux
scissions.

## 3. Énergie exacte de la transition calorique

Soit \(f=g_{s,r}\in L^2_\sigma\). Le semi-groupe calorifique donne

\[
 z(\tau)=S(\tau-r)f\in
 C([r,\infty);L^2_\sigma)\cap
 L^2(r,\infty;\dot H^1_\sigma).                           \tag{15}
\]

Avec la convention
\(\widehat{S(h)f}(\xi)=e^{-h|\xi|^2}\widehat f(\xi)\),
Plancherel donne

\[
\begin{aligned}
 \|z(t)\|_2^2
2\int_r^t\|\nabla z(\tau)\|_2^2\,d\tau
={}&
 \int e^{-2(t-r)|\xi|^2}|\widehat f(\xi)|^2\,d\mu(\xi)\\
 &+\int
 \bigl(1-e^{-2(t-r)|\xi|^2}\bigr)
 |\widehat f(\xi)|^2\,d\mu(\xi)\\
={}&\|f\|_2^2,                                           \tag{16}
\end{aligned}
\]

où \(d\mu\) contient la constante de Plancherel propre à la convention de
Fourier. Ceci prouve (5) pour tout \(t\ge r\), y compris par approximation
si \(f\notin\dot H^1\).

En laissant \(t\to\infty\),

\[
 \|S(t-r)f\|_2\to0,\qquad
 2\int_r^\infty\|\nabla S(\tau-r)f\|_2^2\,d\tau=\|f\|_2^2.
                                                               \tag{17}
\]

Cette égalité ne donne pas d'énergie exacte pour \(g_{s,t}\) en fonction de
celle de \(g_{r,t}\). En effet, (4) entraîne

\[
\begin{aligned}
 \|g_{s,t}\|_2^2
={}&\|g_{r,t}\|_2^2+\|S(t-r)g_{s,r}\|_2^2\\
 &+2\langle g_{r,t},S(t-r)g_{s,r}\rangle,                \tag{18}
\end{aligned}
\]

et aucun signe ni aucune annulation n'est disponible pour le terme croisé.
Soustraire deux inégalités BSS ne créerait pas une orthogonalité. C'est la
première faille d'une tentative de monotonie des redémarrages.

## 4. Disparition locale du fond lorsque \(s\to-\infty\)

Le noyau de chaleur appartient à \(L^{3/2,1}\). L'inégalité de convolution
de Lorentz donne, uniformément par rapport à la trace \(v(s)\),

\[
 \|S(t-s)v(s)\|_\infty
 \le \|G_{t-s}\|_{3/2,1}\|v(s)\|_{3,\infty}
 \le C M(t-s)^{-1/2}.                                    \tag{19}
\]

Pour tout rayon \(R<\infty\),

\[
 \|V_s(t)\|_{L^2(B_R)}
 \le |B_R|^{1/2}\|V_s(t)\|_\infty
 \le CMR^{3/2}(t-s)^{-1/2}\longrightarrow0.               \tag{20}
\]

Plus généralement, pour \(k\ge0\),

\[
 \|\nabla^kV_s(t)\|_\infty
 \le C_kM(t-s)^{-(k+1)/2}.                                \tag{21}
\]

On obtient donc la convergence dans
\(C^\infty_{\rm loc}\) après toute marge temporelle positive, ainsi que
dans les distributions. À l'instant fixé \(t\), (6) est même une
convergence globale en \(L^\infty_x\). Elle ne donne pourtant pas

\[
 \|V_s(t)\|_{3,\infty}\to0,                               \tag{22}
\]

car la norme critique du semi-groupe n'a aucun facteur décroissant. Le
profil homogène de la section 7 sature cette distinction.

Comme

\[
 g_{s,t}=v(t)-V_s(t),                                     \tag{23}
\]

on a, pour \(t\) fixé,

\[
 g_{s,t}\longrightarrow v(t)
 \quad\text{fortement dans }L^2_{\rm loc}
 \text{ et dans }\mathcal D'.                             \tag{24}
\]

Cette convergence locale ne contrôle pas les queues \(L^2\) de
\(g_{s,t}\).

## 5. Ce que donnerait une borne \(L^2\) uniforme

Fixons \(r<T\). Supposons qu'il existe une suite \(s_n\to-\infty\) telle
que

\[
 \sup_n\|g_{s_n,r}\|_2\le K.                              \tag{25}
\]

Par (20) et (23), pour tout \(R<\infty\),

\[
 \|v(r)-g_{s_n,r}\|_{L^2(B_R)}
 =\|V_{s_n}(r)\|_{L^2(B_R)}\to0.                          \tag{26}
\]

Il s'ensuit

\[
 \|v(r)\|_{L^2(B_R)}
 =\lim_{n\to\infty}\|g_{s_n,r}\|_{L^2(B_R)}
 \le K.                                                   \tag{27}
\]

En laissant \(R\to\infty\) et en utilisant la convergence monotone,

\[
 \boxed{v(r)\in L^2_\sigma,\qquad \|v(r)\|_2\le K.}        \tag{28}
\]

On peut aussi extraire une sous-suite faible dans \(L^2\); sa limite
distributionnelle est nécessairement \(v(r)\). La preuve locale (26) est
plus forte et ne demande pas d'identifier deux représentants.

Le quantificateur minimal est donc

\[
 \liminf_{s\to-\infty}\|g_{s,r}\|_2<\infty.                \tag{29}
\]

Il suffit de choisir une suite réalisant ce \(\liminf\). En revanche, (3)
donne seulement

\[
 \|g_{s,r}\|_2\le C_DM^2(r-s)^{1/4},                      \tag{30}
\]

qui diverge avec la longueur de la bande. L'énergie exacte (5) conserve
\(\|g_{s,r}\|_2^2\) comme énergie totale de la transition; elle ne réduit
pas son amplitude initiale.

Si (28) est obtenue, alors \(v(t)\in L^2\) pour tout \(t\ge r\), car

\[
 v(t)=S(t-r)v(r)+g_{r,t}                                  \tag{31}
\]

est la somme de deux champs \(L^2\). Rien dans ce raisonnement ne propage
l'information vers les temps antérieurs à \(r\).

## 6. Quotient critique : formulation correcte

Fixons une norme de Banach équivalente sur l'espace de Lorentz et posons

\[
 X=L^{3,\infty}_\sigma(\mathbb R^3),\qquad
 Y=L^2_\sigma(\mathbb R^3)\cap X.                          \tag{32}
\]

### 6.1 Quotient algébrique

Le quotient algébrique

\[
 Q_{\rm alg}=X/Y                                          \tag{33}
\]

est l'ensemble des classes

\[
 [f]_{\rm alg}=f+Y,\qquad
 f\sim g\Longleftrightarrow f-g\in Y.                     \tag{34}
\]

Il est exact pour le cocycle, puisque \(g_{s,r}\in Y\) :

\[
 \boxed{[v(r)]_{\rm alg}
 =\overline S(r-s)[v(s)]_{\rm alg},}                       \tag{35}
\]

où \(\overline S(h)[f]=[S(h)f]\). Cette action est bien définie, car
\(S(h)Y\subset Y\). L'équation (35) ne dit pas
\([v(r)]=[v(s)]\) : le semi-groupe induit n'est pas démontré égal à
l'identité sur tout le quotient.

### 6.2 Le dénominateur n'est pas fermé

Le sous-espace \(Y\) n'est pas fermé dans \(X\). Une construction
solénoïdale explicite le montre. Soit
\(\Phi\in C_c^\infty(B_1;\mathbb R^3)\), non nulle et divergence-free.
Choisissons des centres \(x_n\) de sorte que les supports suivants soient
disjoints, puis posons

\[
 F_n(x)=n^{-3}\Phi\left(\frac{x-x_n}{n^2}\right),\qquad
 F=\sum_{n=1}^\infty F_n.                                 \tag{36}
\]

Les blocs ont amplitude \(n^{-3}\), volume \(O(n^6)\), et

\[
 \|F_n\|_2^2=\|\Phi\|_2^2.                                \tag{37}
\]

Donc \(F\notin L^2\). En revanche, pour la queue \(F^{>N}\), la fonction de
distribution donne

\[
\begin{aligned}
 \lambda^3
 |\{|F^{>N}|>\lambda\}|
 &\le C\lambda^3
 \sum_{N<n\le C\lambda^{-1/3}}n^6\\
 &\le C N^{-2},                                           \tag{38}
\end{aligned}
\]

avec le membre gauche nul si la somme est vide. Ainsi

\[
 \|F^{>N}\|_{3,\infty}\le C N^{-2/3}\to0.                 \tag{39}
\]

Les sommes partielles appartiennent à \(Y\) et convergent vers
\(F\in X\setminus Y\). Par conséquent \(Y\) n'est pas fermé.

La formule

\[
 \|[f]\|_{\rm q}
 :=\inf_{y\in Y}\|f-y\|_X                                 \tag{40}
\]

n'est donc qu'une semi-norme sur \(Q_{\rm alg}\); certaines classes
algébriques non nulles y ont taille zéro. Il serait incorrect d'appeler
\(Q_{\rm alg}\) un espace de Banach ou d'utiliser sans preuve la compacité
d'une boule quotient.

### 6.3 Quotient séparé

Le quotient topologique correct est

\[
 Q_{\rm H}=X/\overline Y^{\,X}.                            \tag{41}
\]

Il est séparé et banachique avec la norme quotient. Comme \(S(h)\) est
borné sur \(X\), préserve \(Y\), puis préserve sa fermeture, il induit aussi
une action bornée sur \(Q_{\rm H}\). Cette action n'est pas déclarée
fortement continue : le semi-groupe de chaleur n'est pas fortement continu
sur tout \(L^{3,\infty}\).

Les relations de cocycle (35) restent vraies dans \(Q_{\rm H}\), mais la
conclusion \([v(r)]=0\) y signifie seulement
\(v(r)\in\overline Y^{\,X}\), pas nécessairement \(v(r)\in L^2\). Le
critère (29), lui, donne bien l'appartenance forte \(L^2\).

## 7. Le champ homogène \(U\)

### 7.1 Divergence, normes et homogénéité

Écrivons

\[
 U=e_3\times\nabla\log|x|
 =\frac{(-x_2,x_1,0)}{|x|^2}.                              \tag{42}
\]

La fonction \(\log|x|\) est localement intégrable en dimension trois et les
dérivées distributionnelles commutent. Donc

\[
 \operatorname{div}U=0\quad\text{dans }\mathcal D'.       \tag{43}
\]

Le champ est homogène de degré \(-1\). Si
\(\rho=(x_1^2+x_2^2)^{1/2}\), alors

\[
 |U(x)|=\frac{\rho}{|x|^2}=\frac{\sin\theta}{|x|}.         \tag{44}
\]

Un calcul en coordonnées sphériques donne exactement

\[
 |\{|U|>\lambda\}|
 =\frac{\pi^2}{4}\lambda^{-3},\qquad \lambda>0.            \tag{45}
\]

Ainsi \(U\in L^{3,\infty}_\sigma\), avec la convention
\(\|f\|_{3,\infty}=\sup_{\lambda>0}
\lambda|\{|f|>\lambda\}|^{1/3}\),

\[
 \|U\|_{3,\infty}=\left(\frac{\pi^2}{4}\right)^{1/3}.      \tag{46}
\]

De plus,

\[
 \int_{B_R}|U|^2dx=\frac{8\pi}{3}R.                       \tag{47}
\]

La singularité à l'origine est donc localement \(L^2\), tandis que la
divergence linéaire quand \(R\to\infty\) montre \(U\notin L^2\).

### 7.2 Différence calorifique dans \(L^2\)

Prenons la convention

\[
 \widehat f(\xi)=\int_{\mathbb R^3}e^{-ix\cdot\xi}f(x)\,dx,
 \qquad
 \|f\|_2^2=(2\pi)^{-3}\|\widehat f\|_2^2.                 \tag{48}
\]

Comme, au sens des distributions,

\[
 \Delta\log|x|=|x|^{-2},\qquad
 \widehat{|x|^{-2}}=2\pi^2|\xi|^{-1},                     \tag{49}
\]

on obtient, à un terme multiple de \(\delta_0\) éliminé par la dérivée près,

\[
 \widehat U(\xi)
 =-2\pi^2i\,\frac{e_3\times\xi}{|\xi|^3}.                 \tag{50}
\]

Par conséquent,

\[
\begin{aligned}
 \|(I-S(h))U\|_2^2
={}&\frac{4\pi^4}{(2\pi)^3}
 \int_{\mathbb R^3}
 (1-e^{-h|\xi|^2})^2
 \frac{|e_3\times\xi|^2}{|\xi|^6}\,d\xi\\
={}&\frac{4\pi^2}{3}
 \int_0^\infty(1-e^{-h\rho^2})^2\rho^{-2}\,d\rho.         \tag{51}
\end{aligned}
\]

L'intégrale converge : près de zéro, le multiplicateur fournit
\(h^2\rho^4\); à l'infini, l'intégrande est \(O(\rho^{-2})\). Le changement
de variable \(y=\sqrt h\,\rho\), puis une intégration par parties, donnent

\[
\begin{aligned}
 \int_0^\infty(1-e^{-h\rho^2})^2\rho^{-2}\,d\rho
 &=h^{1/2}
 \int_0^\infty(1-e^{-y^2})^2y^{-2}\,dy\\
 &=2\sqrt\pi\left(1-\frac1{\sqrt2}\right)h^{1/2}.         \tag{52}
\end{aligned}
\]

Ainsi

\[
\boxed{
 C_U=
 \left[
 \frac{8\pi^{5/2}}3\left(1-\frac1{\sqrt2}\right)
 \right]^{1/2},\qquad
 \|(I-S(h))U\|_2=C_Uh^{1/4}.}                             \tag{53}
\]

La constante est strictement positive. Comme \(S(h)\) est borné sur
\(L^{3,\infty}\), la différence appartient aussi à cet espace; (9) est
donc démontrée.

Le même résultat suit sans constante par homogénéité :

\[
 (I-S(h))U(x)=h^{-1/2}
 \bigl[(I-S(1))U\bigr](x/\sqrt h),                         \tag{54}
\]

dont la norme \(L^2\) est exactement \(h^{1/4}\) fois celle à \(h=1\).

### 7.3 Classe quotient fixe et non nulle

Puisque \((I-S(h))U\in Y\),

\[
 [S(h)U]_{\rm alg}=[U]_{\rm alg}\ne0.                     \tag{55}
\]

La non-nullité algébrique résulte déjà de \(U\notin L^2\). Elle persiste
dans le quotient séparé. En effet, choisissons un cône angulaire
\(\Gamma\) sur lequel \(\sin\theta\ge3/4\), et posons

\[
 E_R=\Gamma\cap\{R<|x|<2R\}.                              \tag{56}
\]

On a \(|E_R|=c_\Gamma R^3\) et
\(|U|\ge3/(8R)\) sur \(E_R\). Pour tout \(y\in Y\), Chebyshev donne, avec
\(\lambda_R=3/(16R)\),

\[
 |\{x\in E_R:|y(x)|>\lambda_R\}|
 \le C R^2\int_{E_R}|y|^2dx=o(R^3).                       \tag{57}
\]

Pour \(R\) assez grand, un sous-ensemble de \(E_R\) de mesure au moins
\(c_\Gamma R^3/2\) vérifie donc
\(|U-y|\ge\lambda_R\). Il existe une constante universelle
\(c_0>0\), indépendante de \(y\), telle que

\[
 \|U-y\|_{3,\infty}\ge c_0.                               \tag{58}
\]

Ainsi

\[
 \operatorname{dist}_X(U,Y)\ge c_0,\qquad
 [U]_{\rm H}\ne0.                                         \tag{59}
\]

Le profil est donc un véritable mode non énergétique du quotient, et pas
seulement un artefact de la non-fermeture de \(Y\).

### 7.4 Cocycle modèle et saturation

Pour la trajectoire artificielle constante \(v(t)=U\),

\[
 g_{s,r}=U-S(r-s)U=(I-S(r-s))U,                            \tag{60}
\]

et (53) donne

\[
 \|g_{s,r}\|_2=C_U(r-s)^{1/4}.                            \tag{61}
\]

Le cocycle (4), la convergence locale (6), l'énergie calorifique (5) et la
classe quotient fixe sont tous satisfaits. La borne (7) échoue exactement
à la puissance autorisée par (3). Ceci réfute toute dérivation purement
fonctionnelle de l'uniformité depuis les points (i)--(iii).

Le modèle ne satisfait pas non plus la clause dissipative du cycle 0049.
Pour tout \(h>0\), (50) donne

\[
 \|\nabla(I-S(h))U\|_2^2
 \simeq\int_1^\infty
 (1-e^{-h\rho^2})^2\,d\rho=\infty.                        \tag{61a}
\]

La transition calorique issue d'un endpoint fixé
\((I-S(r-s))U\in L^2\) possède bien l'énergie (5) pour les temps
ultérieurs, mais la trajectoire artificielle
\(\tau\mapsto(I-S(\tau-s))U\) n'appartient pas à
\(L^2_\tau\dot H^1_x\). Le profil n'est donc compatible qu'avec la partie
linéaire et quotient du ledger, pas avec la sortie BSS complète.

### 7.5 Variante lisse \(U_\sharp\)

Choisissons une fonction radiale
\(\chi\in C^\infty([0,\infty);[0,1])\), nulle sur \([0,1]\) et égale à
un sur \([2,\infty)\), puis posons

\[
 U_\sharp(x)=\chi(|x|)U(x).                                \tag{61b}
\]

La multiplication ne crée pas de divergence :

\[
 \operatorname{div}U_\sharp
 =\chi\,\operatorname{div}U+
 \chi'(|x|)\frac{x}{|x|}\cdot U=0,                         \tag{61c}
\]

car \(x\cdot U(x)=0\). Le champ est \(C^\infty\), nul près de l'origine,
borné et égal à \(U\) pour \(|x|\ge2\). Par conséquent,

\[
\begin{aligned}
 &U_\sharp\in
 L^\infty_\sigma\cap L^{3,\infty}_\sigma
 \subset\widetilde L^{3,\infty}_\sigma,\\
 &\nabla U_\sharp\in L^2,\qquad
 U_\sharp\notin L^2.                                     \tag{61d}
\end{aligned}
\]

Ici

\[
 \widetilde L^{3,\infty}
 :=\overline{L^\infty\cap L^{3,\infty}}^{\,
 \|\cdot\|_{3,\infty}},                                  \tag{61e}
\]

donc l'appartenance est immédiate : \(U_\sharp\) appartient déjà à
l'ensemble dont on prend la fermeture. La borne
\(\nabla U_\sharp\in L^2\) vient de
\(|\nabla U(x)|\le C|x|^{-2}\) à l'infini; la non-appartenance \(L^2\)
vient de la même queue \(1/|x|\) que dans (47).

L'inégalité spectrale

\[
 |1-e^{-h|\xi|^2}|^2\le h|\xi|^2                         \tag{61f}
\]

donne, pour tout \(h>0\),

\[
 (I-S(h))U_\sharp\in L^2_\sigma\cap\dot H^1_\sigma,
 \qquad
 \|(I-S(h))U_\sharp\|_2
 \le h^{1/2}\|\nabla U_\sharp\|_2.                        \tag{61g}
\]

L'appartenance \(\dot H^1\) de l'incrément suit aussi directement de
\[
 \|\nabla(I-S(h))U_\sharp\|_2
 \le2\|\nabla U_\sharp\|_2.                               \tag{61h}
\]

Sur toute bande finie \(0<h<H\), la trajectoire
\(h\mapsto(I-S(h))U_\sharp\) appartient donc à

\[
 C([0,H];L^2_\sigma)\cap L^2(0,H;\dot H^1_\sigma),        \tag{61i}
\]

avec trace forte nulle. Elle vérifie les espaces énergétiques du correcteur,
contrairement au profil brut.

Pour suivre la croissance aux grands temps, écrivons

\[
 K=U_\sharp-U=(\chi-1)U\in L^2_\sigma,\qquad
 (I-S(h))U_\sharp=(I-S(h))U+(I-S(h))K.                    \tag{61j}
\]

La contraction \(L^2\) donne

\[
 \|(I-S(h))K\|_2\le2\|K\|_2.                              \tag{61k}
\]

En combinant (53), (61j) et l'inégalité triangulaire inverse,

\[
\begin{aligned}
 \left|
 \|(I-S(h))U_\sharp\|_2-C_Uh^{1/4}
 \right|
 &\le2\|K\|_2,\\
 \|(I-S(h))U_\sharp\|_2
 &=C_Uh^{1/4}+O(1),\\
 h^{-1/4}\|(I-S(h))U_\sharp\|_2
 &\longrightarrow C_U.                                  \tag{61l}
\end{aligned}
\]

Ainsi le lissage intérieur ne change ni la puissance ni la constante
asymptotique de la transition ancienne. Comme l'incrément est dans \(Y\),

\[
 [S(h)U_\sharp]=[U_\sharp]\ne0                            \tag{61m}
\]

dans les quotients algébrique et séparé. La non-nullité séparée suit de la
preuve (56)--(59), inchangée à l'infini.

La fuite d'uniformité apparaît également par la non-commutation exacte des
limites. Posons

\[
 E_\sharp(h,R)=
 \int_{B_R}|(I-S(h))U_\sharp|^2dx.                         \tag{61n}
\]

Pour tout \(h<\infty\), l'incrément est globalement \(L^2\), donc

\[
 \lim_{R\to\infty}\frac{E_\sharp(h,R)}R=0.                 \tag{61o}
\]

Pour tout \(R<\infty\), le lissage (19) donne
\(S(h)U_\sharp\to0\) dans \(L^2(B_R)\) lorsque \(h\to\infty\). Comme
\(U_\sharp=U\) hors de \(B_2\), (47) implique

\[
 \lim_{R\to\infty}
 \frac1R\int_{B_R}|U_\sharp|^2dx=\frac{8\pi}{3}.           \tag{61p}
\]

Par conséquent,

\[
\boxed{
\begin{aligned}
 \lim_{h\to\infty}\lim_{R\to\infty}
 \frac{E_\sharp(h,R)}R&=0,\\
 \lim_{R\to\infty}\lim_{h\to\infty}
 \frac{E_\sharp(h,R)}R&=\frac{8\pi}{3}.
\end{aligned}}                                            \tag{61q}
\]

Le premier ordre prend l'énergie globale de chaque transition finie avant
de reculer la base; le second capture d'abord la limite locale non
énergétique. Les échanger reviendrait précisément à supposer l'uniformité
recherchée.

La trajectoire artificielle constante \(v(t)=U_\sharp\) satisfait donc le
cocycle, la trace énergétique des incréments, leur dissipation sur chaque
bande et la classe fixe dans
\(\widetilde L^{3,\infty}\). Elle ne satisfait toujours pas l'équation de
Navier--Stokes ni l'inégalité d'énergie adaptée associée. Ce profil montre
que ni la continuité forte du semi-groupe dans
\(\widetilde L^{3,\infty}\), ni les seuls espaces
\(C_tL^2\cap L^2_t\dot H^1\), ne fournissent la borne uniforme (7).

### 7.6 Faille Navier--Stokes

La trajectoire \(v(t)=U\) n'est pas une solution stationnaire de
Navier--Stokes. Notons \(A x=e_3\times x=(-x_2,x_1,0)\). Pour
\(x\ne0\),

\[
 U=|x|^{-2}Ax,\qquad
 -\Delta U=\frac{2Ax}{|x|^4},\qquad
 (U\cdot\nabla)U=-\frac{(x_1,x_2,0)}{|x|^4}.              \tag{62}
\]

Sur le cercle de rayon cylindrique \(\rho>0\) à hauteur \(x_3=z\), la
circulation de la composante azimutale de
\(-\Delta U+(U\cdot\nabla)U\) vaut

\[
 \oint
 \bigl[-\Delta U+(U\cdot\nabla)U\bigr]\cdot d\ell
 =\frac{4\pi\rho^2}{(\rho^2+z^2)^2}\ne0.                  \tag{63}
\]

La circulation d'un gradient de pression monovalué est nulle. Il n'existe
donc pas de pression \(p\) telle que

\[
 -\Delta U+(U\cdot\nabla)U+\nabla p=0                     \tag{64}
\]

même localement sur ces cercles loin de l'origine. Les éventuels défauts
distributionnels à l'origine ne réparent pas cette obstruction classique
sur \(\mathbb R^3\setminus\{0\}\).

Le profil \(U\) ne respecte donc ni l'équation PDE de l'hypothèse, ni sa
pression de Riesz, ni la suitability. Son rôle est strictement adverse :
il montre que cocycle, chaleur, échelle et quotient ne suffisent pas seuls.

Le même défaut subsiste pour \(U_\sharp\). Sur toute région
\(|x|>2\), les deux champs coïncident, donc la circulation non nulle (63)
est inchangée. Le cutoff lisse ne peut être compensé par une pression et
ne transforme pas le contre-profil en solution admissible.

## 8. Passe contradictoire

1. **Temps exceptionnels.** (4) vaut pour tous les temps seulement après
   construction du représentant \(C_{w^*}\). Pour une classe
   \(L^\infty_t\) brute, il faut écrire « presque tous \(s,r,t\) ».
2. **Espace de l'identité.** L'algèbre donne d'abord (4) dans
   \(L^{3,\infty}\) ou \(\mathcal S'\). Le résultat BSS sur chaque bande
   place ensuite chaque terme dans \(L^2\), ce qui promeut l'identité à
   \(L^2\).
3. **Énergie contre orthogonalité.** L'égalité (5) concerne seulement la
   transition calorique. Le terme croisé (18) interdit toute additivité
   des énergies des correcteurs.
4. **Local contre critique.** La convergence globale \(L^\infty\) de
   \(V_s(t)\) vers zéro n'implique pas la convergence dans
   \(L^{3,\infty}\), qui voit le volume spatial croissant.
5. **Uniformité.** Une borne le long d'une seule suite \(s_n\to-\infty\)
   suffit à forcer \(v(r)\in L^2\). Le taux disponible (30) ne contient
   aucune telle sous-suite bornée.
6. **Quotient non séparé.** \(X/Y\) ne doit pas être muni sans avertissement
   d'une norme de Banach. Les affirmations topologiques doivent être
   formulées dans \(X/\overline Y^X\).
7. **Action du semi-groupe.** (35) est une évolution par le semi-groupe
   induit, pas une constance de classe. La constance de \([U]\) utilise la
   propriété spéciale (9).
8. **Classe nulle.** Dans le quotient algébrique,
   \([f]=0\) équivaut à \(f\in L^2\cap X\). Dans le quotient séparé, elle
   équivaut seulement à \(f\in\overline Y^X\).
9. **Singularité de \(U\).** \(U\) est localement \(L^2\) à l'origine et
   distributionnellement solénoïdal; sa non-énergie vient de l'infini.
   La variante \(U_\sharp\) montre que lisser l'origine et ajouter
   \(\dot H^1\) ne restaure aucune uniformité ancienne.
10. **Sous-espace \(\widetilde L^{3,\infty}\).** La forte continuité
    calorifique critique à temps court ne contrôle pas le recul
    \(h\to\infty\). Le champ borné \(U_\sharp\) appartient à ce sous-espace
    et conserve pourtant une classe quotient non nulle.
11. **Ordre des limites.** Les deux valeurs de (61q) interdisent de passer
    simultanément au domaine entier et à la base \(-\infty\) sans borne
    uniforme.
12. **PDE de \(U\).** Le défaut n'est pas seulement une force ponctuelle à
    l'origine : la circulation (63) exclut déjà l'équation non forcée sur le
    domaine poncturé.
13. **Pression.** Le cocycle ne construit ni ne modifie une pression. La
    pression de Riesz reste celle de \(v\); le profil adverse \(U\) n'a pas
    de pression Navier--Stokes compensatrice.
14. **Clay.** Même une classe quotient non nulle d'une vraie ancienne ne
    fournirait ni blow-up admissible, ni trace terminale singulière, ni
    théorème de rigidité.

## 9. Statut logique et prochain verrou

La chaîne rigoureuse est

\[
\begin{aligned}
 &v\text{ ancienne suitable, Riesz, }
   \sup_t\|v(t)\|_{3,\infty}\le M\\
 &\Longrightarrow
 g_{s,t}\in L^2\cap L^{3,\infty}
 \text{ sur toute bande finie}\\
 &\Longrightarrow
 g_{s,t}=g_{r,t}+S(t-r)g_{s,r}\\
 &\Longrightarrow
 [v(r)]=\overline S(r-s)[v(s)]
 \text{ dans le quotient algébrique et le quotient séparé}.     \tag{65}
\end{aligned}
\]

Le maillon manquant est

\[
 \boxed{
 \liminf_{s\to-\infty}\|g_{s,r}\|_2<\infty,}               \tag{66}
\]

ou une propriété de quotient PDE assez forte pour remplacer (66). L'énergie
calorifique exacte ne ferme pas ce maillon; elle transporte le coût
\(\|g_{s,r}\|_2^2\) sans le borner. Le profil \(U\) montre que la puissance
\((r-s)^{1/4}\) et une classe quotient non nulle sont cohérentes avec toutes
les identités linéaires. Le profil lisse \(U_\sharp\) montre en plus que
cette obstruction persiste dans
\(\widetilde L^{3,\infty}\cap\dot H^1\), avec incréments dans la classe
d'énergie sur chaque bande et limites itérées \(0\) contre \(8\pi/3\).

**Décision : CONTINUER.** Conserver (4)--(7) et la formulation séparée du
quotient. Consigner \(U\) et \(U_\sharp\) comme contre-profils
calorifiques exacts, jamais comme solutions de Navier--Stokes. Le prochain
test décisif doit chercher une
identité issue du terme non linéaire ou de la pression de Riesz qui force
une réduction du coût de transition sur une suite
\(s_n\to-\infty\); répéter l'énergie du semi-groupe seule est désormais
abandonné.
