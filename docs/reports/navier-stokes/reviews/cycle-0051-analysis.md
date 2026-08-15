# Cycle 0051 — critère infrarouge pour l'uniformité des redémarrages

Date : 2026-08-15.

Statut : AI_INTERNAL_DERIVATION; passe analytique indépendante, sans
simulation et sans conclusion Clay.

## Verdict

Fixons \(r<T\). Sous les hypothèses des cycles 0048--0050, le verrou

\[
 \liminf_{s\to-\infty}\|g_{s,r}\|_2<\infty,\qquad
 g_{s,r}=v(r)-S(r-s)v(s),                                  \tag{1}
\]

est **exactement un verrou de basses fréquences**. Toutes les fréquences
au-dessus d'un seuil spatial fixe sont uniformément contrôlées par
l'équation de Navier--Stokes et la borne
\(L^\infty_tL^{3,\infty}_x\).

Plus précisément, pour une décomposition homogène de Littlewood--Paley
\((\Delta_j)_{j\in\mathbb Z}\), on a

\[
 \boxed{
 \|\Delta_jg_{s,r}\|_2
 \le C M^2 2^{-j/2}
 \min\{1,(r-s)2^{2j}\}.}                                   \tag{2}
\]

Il s'ensuit, pour tout \(J\in\mathbb Z\),

\[
 \boxed{
 \sup_{s<r}
 \sum_{j>J}\|\Delta_jg_{s,r}\|_2^2
 \le C M^4 2^{-J}.}                                       \tag{3}
\]

Par conséquent, si

\[
 \mathcal L_J(s,r)
 :=\sum_{j\le J}\|\Delta_jg_{s,r}\|_2^2,                  \tag{4}
\]

alors, pour n'importe quel seuil fixe \(J\),

\[
\boxed{
\begin{aligned}
 \liminf_{s\to-\infty}\|g_{s,r}\|_2<\infty
 &\Longleftrightarrow
 \liminf_{s\to-\infty}\mathcal L_J(s,r)<\infty,\\
 \sup_{s<r}\|g_{s,r}\|_2<\infty
 &\Longleftrightarrow
 \sup_{s<r}\mathcal L_J(s,r)<\infty.
\end{aligned}}                                             \tag{5}
\]

Les équivalences sont à constantes de Littlewood--Paley près. Une version
calorifique, plus canonique et sans ambiguïté de cutoff, est la suivante.
Pour un seul \(a>0\) fixé, posons

\[
 \mathcal C_a(s,r)=\|S(a)g_{s,r}\|_2.                     \tag{6}
\]

Alors

\[
 \boxed{
\begin{aligned}
 \liminf_{s\to-\infty}\|g_{s,r}\|_2<\infty
 &\Longleftrightarrow
 \liminf_{s\to-\infty}\mathcal C_a(s,r)<\infty,\\
 \sup_{s<r}\|g_{s,r}\|_2<\infty
 &\Longleftrightarrow
 \sup_{s<r}\mathcal C_a(s,r)<\infty,
\end{aligned}}                                             \tag{7}
\]

car la partie complémentaire satisfait uniformément

\[
 \boxed{
 \sup_{s<r}\|(I-S(a))g_{s,r}\|_2
 \le C M^2a^{1/4}.}                                       \tag{8}
\]

Le quantificateur minimal dans la branche \(\liminf\) est donc :

\[
 \boxed{
 \exists a>0,\ \exists s_n\to-\infty,\quad
 \sup_n\|S(a)g_{s_n,r}\|_2<\infty.}                       \tag{9}
\]

Un seul \(a\) et une seule suite suffisent. Si (9) est vraie, le cycle 0050
implique \(v(r)\in L^2\). Aucun passage \(a\downarrow0\), aucune uniformité
en \(a\), et aucune convergence forte du semi-groupe dans
\(L^{3,\infty}\) ne sont nécessaires.

Le résultat positif du cycle est l'isolation rigoureuse de l'infrarouge.
Le résultat négatif est que les hypothèses actuelles ne bornent pas (4) ou
(6). La borne par taille du stress non linéaire reproduit exactement la
croissance

\[
 \|g_{s,r}\|_2\lesssim M^2(r-s)^{1/4}.                    \tag{10}
\]

Fermer (9) exige une annulation temporelle ou dyadique du stress
\(v\otimes v\), une déplétion de triades basses, ou une information globale
supplémentaire. La suitability locale et l'énergie BSS bande par bande ne
fournissent pas cette annulation.

## 1. Cadre exact et échelle

L'équation est, sur
\(\mathbb R^3\times(-\infty,T)\), sans frontière ni force, de viscosité
un,

\[
 \partial_tv-\Delta v+\operatorname{div}(v\otimes v)+\nabla q=0,
 \qquad \operatorname{div}v=0,                            \tag{11}
\]

avec

\[
 q=\mathcal R_i\mathcal R_j(v_iv_j),\qquad
 \sup_{t<T}\|v(t)\|_{3,\infty}\le M.                      \tag{12}
\]

La paire \((v,q)\) est faible adaptée localement. Le représentant
\(C_{w^*}L^{3,\infty}\) du cycle 0048 fixe \(v(t)\) à tout temps. Les
cycles 0048--0049 donnent, pour chaque \(s<r<T\),

\[
 g_{s,r}\in L^2_\sigma\cap L^{3,\infty}_\sigma,\qquad
 \|g_{s,r}\|_2\le C_DM^2(r-s)^{1/4}.                      \tag{13}
\]

Sous l'échelle

\[
 v_\lambda(x,t)=\lambda v(\lambda x,\lambda^2t),          \tag{14}
\]

on a

\[
\begin{aligned}
 \|v_\lambda(t)\|_{3,\infty}&=\|v(\lambda^2t)\|_{3,\infty},\\
 \|g^\lambda_{s,r}\|_2^2
 &=\lambda^{-1}
 \|g_{\lambda^2s,\lambda^2r}\|_2^2.                      \tag{15}
\end{aligned}
\]

Pour \(\lambda=2^k\), les indices dyadiques se décalent :

\[
 \|\Delta_jg^\lambda_{s,r}\|_2^2
 =\lambda^{-1}
 \|\Delta_{j-k}g_{\lambda^2s,\lambda^2r}\|_2^2,           \tag{16}
\]

à modification bornée des cutoffs. Un seuil \(J\) n'est donc pas une
échelle privilégiée : il se translate sous remise à l'échelle. La finitude
du critère (5) est covariante, et sa valeur porte le poids énergétique
\(\lambda^{-1}\).

Dans la formulation calorifique,

\[
 S(a)g^\lambda_{s,r}(x)
 =\lambda
 [S(\lambda^2a)g_{\lambda^2s,\lambda^2r}](\lambda x).     \tag{17}
\]

Le paramètre \(a\) se transforme comme un temps ou une longueur au carré,
et le membre droit de (8), au carré, a le poids
\(M^4a^{1/2}\), exactement celui d'une énergie.

## 2. Duhamel projeté : apport réel de la PDE

Posons \(F=v\otimes v\). Le produit de Lorentz d'O'Neil donne

\[
 \|F(t)\|_{3/2,\infty}
 \le C_O\|v(t)\|_{3,\infty}^2
 \le C_OM^2.                                              \tag{18}
\]

La pression de Riesz autorise l'équation projetée globale

\[
 \partial_tv-\Delta v+\mathbb P\operatorname{div}F=0      \tag{19}
\]

dans les distributions tempérées. La formule faible-étoile du cycle 0048
donne

\[
 \boxed{
 g_{s,r}
 =-\int_s^r
 S(r-\tau)\mathbb P\operatorname{div}F(\tau)\,d\tau.}     \tag{20}
\]

L'intégrale globale endpoint est une intégrale de Gelfand dans
\(L^{3,\infty}\). Après localisation sur une couronne fréquentielle, elle
devient une intégrale de Bochner dans \(L^2\), car la singularité temporelle
est intégrable à fréquence fixée. Plus précisément, l'intégrande lissé est
faiblement mesurable à valeurs dans le séparable \(L^2\); le théorème de
Pettis et (24) donnent la mesurabilité forte et l'intégrabilité de Bochner.

Cette identité est le seul apport PDE requis pour (2)--(8), en plus de
(18). La suitability locale et la globalisation BSS du cycle 0049 ne sont
pas utilisées pour l'estimation haute fréquence. Elles restent nécessaires
dans la chaîne globale ayant produit la solution ancienne et ses
correcteurs admissibles, mais elles ne donnent ici aucune amélioration
infrarouge.

## 3. Estimation dyadique exacte

Choisissons une partition homogène standard, avec
\(\varphi\in C_c^\infty(\{\tfrac12<|\xi|<2\})\) et

\[
 \Delta_jf=
 \mathcal F^{-1}\bigl[\varphi(2^{-j}\xi)\widehat f(\xi)\bigr].
                                                               \tag{21}
\]

On choisit une couronne élargie \(\widetilde\Delta_j\) égale à l'identité
sur le support de \(\Delta_j\). Le noyau de

\[
 \Delta_jS(h)\mathbb P\operatorname{div}                  \tag{22}
\]

est un noyau de Schwartz à fréquence \(2^j\). La convolution de Lorentz,
avec

\[
 \frac1{3/2}+\frac1{6/5}=1+\frac12,                       \tag{23}
\]

et le facteur d'une dérivée donnent

\[
\begin{aligned}
 \|\Delta_jS(h)\mathbb P\operatorname{div}H\|_2
 &\le
 C\,2^{3j/2}e^{-c h2^{2j}}
 \|\widetilde\Delta_jH\|_{3/2,\infty}\\
 &\le
 C\,2^{3j/2}e^{-c h2^{2j}}
 \|H\|_{3/2,\infty}.                                     \tag{24}
\end{aligned}
\]

Le facteur est

\[
 2^j
 \times2^{3j(2/3-1/2)}
 =2^{3j/2}.                                               \tag{25}
\]

Il ne manque donc ni la dérivée de la divergence, ni le demi-exposant de
Bernstein.

En appliquant (24) à (20), puis (18),

\[
\begin{aligned}
 \|\Delta_jg_{s,r}\|_2
 &\le CM^2
 2^{3j/2}\int_0^{r-s}e^{-ch2^{2j}}\,dh\\
 &\le CM^2
 2^{-j/2}\bigl(1-e^{-c(r-s)2^{2j}}\bigr).                 \tag{26}
\end{aligned}
\]

Les inégalités

\[
 1-e^{-x}\le\min\{1,x\}                                   \tag{27}
\]

donnent (2). Si

\[
 2^{2j_*}\simeq(r-s)^{-1},                                \tag{28}
\]

alors

\[
 \|\Delta_jg_{s,r}\|_2
 \lesssim
 \begin{cases}
 M^2(r-s)2^{3j/2},&j\le j_*,\\
 M^22^{-j/2},&j>j_*.
 \end{cases}                                              \tag{29}
\]

La somme des carrés des deux branches vaut

\[
\begin{aligned}
 \sum_{j\le j_*}
 M^4(r-s)^22^{3j}
 &\lesssim M^4(r-s)^{1/2},\\
 \sum_{j>j_*}M^42^{-j}
 &\lesssim M^4(r-s)^{1/2}.                               \tag{30}
\end{aligned}
\]

On retrouve (13) à la bonne échelle. Surtout, pour \(J\) fixé,
\(2^{-j/2}\) est sommable au carré sur \(j>J\), ce qui donne (3)
indépendamment de \(s\). Lorsque \(s\to-\infty\), l'indice de transition
\(j_*\to-\infty\) : toute croissance possible glisse vers les fréquences
basses.

## 4. Justification Littlewood--Paley et fréquence zéro

Pour chaque \(s<r\), \(g_{s,r}\in L^2\). Le théorème de
Littlewood--Paley dans \(L^2\) donne

\[
 c_{\rm LP}\|g_{s,r}\|_2^2
 \le\sum_{j\in\mathbb Z}\|\Delta_jg_{s,r}\|_2^2
 \le C_{\rm LP}\|g_{s,r}\|_2^2.                           \tag{31}
\]

Il n'y a pas de polynôme résiduel : un polynôme non nul n'appartient pas à
\(L^2(\mathbb R^3)\). L'usage de la décomposition homogène est donc
inoffensif pour \(g_{s,r}\).

Il serait en revanche incorrect d'appliquer séparément (31) à
\(v(r)\) ou à \(S(r-s)v(s)\). Ces champs appartiennent seulement à
\(L^{3,\infty}\) et peuvent ne pas être dans \(L^2\). Leurs transformées de
Fourier sont des distributions tempérées, pas nécessairement des fonctions
dont le carré est intégrable. L'annulation

\[
 v(r)-S(r-s)v(s)\in L^2                                  \tag{32}
\]

doit être conservée avant de prendre une énergie fréquentielle.

De même, l'identité formelle

\[
 \widehat g_{s,r}(\xi)
 =\widehat v(r,\xi)
 -e^{-(r-s)|\xi|^2}\widehat v(s,\xi)                      \tag{33}
\]

est une égalité de distributions dont le membre complet a un représentant
\(L^2_\xi\). Elle n'autorise pas à intégrer séparément le carré de ses deux
termes.

## 5. Équivalence infrarouge dyadique

Par (31) et (3),

\[
\begin{aligned}
 \|g_{s,r}\|_2^2
 &\le C\mathcal L_J(s,r)+CM^42^{-J},\\
 \mathcal L_J(s,r)
 &\le C\|g_{s,r}\|_2^2.                                  \tag{34}
\end{aligned}
\]

Les deux relations de (5) en découlent. Pour la première, si le
\(\liminf\) de \(\mathcal L_J\) est fini, on choisit une suite
\(s_n\to-\infty\) sur laquelle cette quantité est bornée; (34) borne alors
\(\|g_{s_n,r}\|_2\). La réciproque utilise la seconde ligne. Aucun échange
entre \(\liminf\) et somme infinie n'est effectué.

Le quantificateur le plus faible peut s'écrire

\[
 \exists J\in\mathbb Z,\ \exists s_n\to-\infty,\qquad
 \sup_n\sum_{j\le J}\|\Delta_jg_{s_n,r}\|_2^2<\infty.     \tag{35}
\]

Si (35) vaut pour un \(J\), elle vaut, avec une autre constante, pour tout
seuil fixe : diminuer \(J\) retire des termes; l'augmenter ajoute seulement
un nombre fini de blocs, chacun uniformément contrôlé par (2).

Une condition plus forte, telle que

\[
 \lim_{J\to-\infty}
 \sup_{s<r}\sum_{j\le J}\|\Delta_jg_{s,r}\|_2^2=0,        \tag{36}
\]

n'est pas nécessaire pour (1). Elle exprimerait une uniformité et une
équi-intégrabilité infrarouges bien supérieures. L'imposer sans mécanisme
PDE serait cacher le verrou dans l'hypothèse.

## 6. Formulation calorifique équivalente

Pour \(f\in L^2\), l'identité spectrale donne

\[
 \|S(a)f\|_2^2
 =2\int_a^\infty\|\nabla S(\theta)f\|_2^2\,d\theta.       \tag{37}
\]

En effet, le multiplicateur du membre droit est

\[
 2\int_a^\infty
 |\xi|^2e^{-2\theta|\xi|^2}\,d\theta
 =e^{-2a|\xi|^2}.                                        \tag{38}
\]

La quantité \(\mathcal C_a\) mesure donc exactement l'énergie calorifique
restant après le temps \(a\); elle est une version lisse de l'énergie
infrarouge (4).

Pour prouver (8), appliquons le multiplicateur
\(I-S(a)\) à la décomposition dyadique. Sur la couronne \(j\),

\[
 |1-e^{-a|\xi|^2}|
 \le C\min\{1,a2^{2j}\}.                                  \tag{39}
\]

Avec le majorant uniforme, obtenu de (26),

\[
 \|\Delta_jg_{s,r}\|_2\le CM^22^{-j/2},                   \tag{40}
\]

on trouve

\[
\begin{aligned}
 \|(I-S(a))g_{s,r}\|_2^2
 &\le CM^4
 \sum_j
 \min\{1,a2^{2j}\}^2\,2^{-j}\\
 &\le CM^4a^{1/2}.                                       \tag{41}
\end{aligned}
\]

La dernière somme est scindée à
\(2^{2j_a}\simeq a^{-1}\) :

\[
 a^2\sum_{j\le j_a}2^{3j}
 +\sum_{j>j_a}2^{-j}
 \lesssim a^{1/2}.                                       \tag{42}
\]

Ceci prouve (8), uniformément en \(s\) et \(r\). Comme

\[
 \|S(a)g_{s,r}\|_2\le\|g_{s,r}\|_2                       \tag{43}
\]

et

\[
 \|g_{s,r}\|_2
 \le\|S(a)g_{s,r}\|_2+CM^2a^{1/4},                       \tag{44}
\]

les équivalences (7) et le quantificateur (9) suivent.

Il est essentiel que \(a>0\) soit fixé indépendamment de \(s\). Prendre
\(a=r-s\) rendrait \(S(a)g\) artificiellement petit et déplacerait le
complément (8) vers le majorant divergent
\(CM^2(r-s)^{1/4}\).

## 7. Forme PDE exacte et critère suffisant sur le stress

La partie basse du correcteur n'est pas une donnée libre. En appliquant
\(\Delta_j\) à (20), posons

\[
 B_j(s,r)
 :=
 -\int_s^r
 \Delta_jS(r-\tau)\mathbb P\operatorname{div}
 (v\otimes v)(\tau)\,d\tau.                               \tag{45}
\]

Alors \(B_j(s,r)=\Delta_jg_{s,r}\). Le critère nécessaire et suffisant
issu de la PDE est donc

\[
 \exists J,\ \exists s_n\to-\infty,\qquad
 \sup_n\sum_{j\le J}\|B_j(s_n,r)\|_2^2<\infty.             \tag{46}
\]

Cette écriture expose où une annulation doit agir : dans l'intégrale
vectorielle en temps, puis dans la somme carrée des sorties.

Une condition plus forte mais directement vérifiable est obtenue en
définissant

\[
 A_j(s,r)
 :=
 2^{3j/2}
 \int_s^r e^{-c(r-\tau)2^{2j}}
 \|\widetilde\Delta_j(v\otimes v)(\tau)\|_{3/2,\infty}
 \,d\tau.                                                 \tag{47}
\]

Par (24),

\[
 \|B_j(s,r)\|_2\le C A_j(s,r).                            \tag{48}
\]

Ainsi la condition

\[
 \exists J,\ \exists s_n\to-\infty,\qquad
 \sup_n\sum_{j\le J}A_j(s_n,r)^2<\infty                  \tag{49}
\]

est suffisante pour \(v(r)\in L^2\).

Elle n'est pas nécessaire : la norme dans (47) est prise avant
l'intégration temporelle et détruit les cancellations signées. Elle est
aussi beaucoup plus forte que la seule taille critique. En remplaçant
\(\|\widetilde\Delta_j(v\otimes v)\|_{3/2,\infty}\) par \(CM^2\),
on retrouve (26), et la somme basse croît comme
\(M^4(r-s)^{1/2}\).

Le prochain lemme utile doit donc fournir soit :

- une sommabilité \(\ell^2\) basse de \(A_j\);
- une estimation directe des intégrales vectorielles \(B_j\) conservant
  leur signe et leur phase;
- une annulation triadique qui gagne une puissance stricte de \(2^j\) dans
  (24);
- ou une décroissance temporelle du stress sur une suite ancienne.

## 8. Défauts de carré-fonction à l'endpoint

### 8.1 Ce qui est valide

La somme carrée (31) est valide parce que \(g_{s,r}\in L^2\). Le théorème
vectoriel de Littlewood--Paley peut également être formulé dans plusieurs
espaces de Lorentz, mais il conserve alors la norme spatiale
\(L^{3,\infty}\) :

\[
 \left\|
 \left(\sum_j|\Delta_jv|^2\right)^{1/2}
 \right\|_{3,\infty}
 \lesssim\|v\|_{3,\infty}.                                \tag{50}
\]

Même lorsque (50) est disponible pour la décomposition choisie, il ne
donne pas

\[
 \sum_j\|\Delta_jv\|_2^2<\infty.                          \tag{51}
\]

Les opérations « norme faible-\(L^3\) en espace » et « somme d'énergies
\(L^2\) des blocs » ne sont pas interchangeables.

### 8.2 Le défaut \(q=\infty\)

Les estimations critiques de blocs fournissent typiquement une borne de
type Besov avec sommation extérieure \(\ell^\infty\), c'est-à-dire un
contrôle bloc par bloc. Elles ne donnent pas la sommabilité
\(\ell^2\) requise par l'énergie. Une infinité de coquilles infrarouges
peut donc contribuer une quantité comparable sur des échelles successives.

Dans (26), le facteur thermique rend la somme \(\ell^2\) finie pour chaque
intervalle fini. Quand \(s\to-\infty\), le seuil \(j_*\) recule et le
nombre de coquilles actives n'est pas uniformément borné. Remplacer le
\(\sup_j\) implicite par

\[
 \left(\sum_{j\le J}\cdots^2\right)^{1/2}                 \tag{52}
\]

sans gain supplémentaire est précisément l'erreur endpoint.

### 8.3 Fréquences des traces séparées

Il n'existe pas, sous les hypothèses actuelles, de borne générale

\[
 \|\Delta_jv(t)\|_2
 \lesssim 2^{-j/2}\|v(t)\|_{3,\infty}.                    \tag{53}
\]

L'inégalité de Bernstein va de \(L^{3,\infty}\) vers des exposants
spatiaux plus grands, pas vers \(L^2\), sans information globale
supplémentaire. Des paquets fréquentiels translatés peuvent préserver la
norme faible-\(L^3\) tout en accumulant une énergie infinie.

La borne (2) ne contredit pas ce fait : elle porte sur la différence PDE
\(g_{s,r}\) et vient du stress dans \(L^{3/2,\infty}\), pour lequel le
passage vers \(L^2\) est dans le sens admissible.

## 9. Passe contradictoire

1. **Séparer les deux traces.** Écrire l'énergie de
   \(v(r)-S(r-s)v(s)\) comme somme des énergies de ses termes est
   illégitime; chacun peut avoir une énergie infinie.
2. **Bernstein inversé.** Faible-\(L^3\) ne contrôle pas les blocs de la
   vitesse dans \(L^2\). Le passage dyadique \(L^{3/2,\infty}\to L^2\)
   s'applique au stress après la divergence, pas directement à \(v\).
3. **Dérivée manquante.** Le facteur correct dans (24) est
   \(2^{3j/2}\), pas \(2^{j/2}\).
4. **Leray et fréquence zéro.** La projection de Leray est traitée sur
   chaque couronne \(j\), où son symbole est lisse. Sommer jusqu'à
   \(j=-\infty\) avant d'établir (31) réintroduirait une ambiguïté
   homogène.
5. **Somme avant \(\liminf\).** La preuve de (5) choisit d'abord une suite
   réalisant le \(\liminf\), puis utilise la borne haute uniforme. Elle
   n'applique pas Fatou dans le mauvais sens à une famille non uniforme.
6. **Seuil mobile.** Choisir \(J=j_*(s)\) ou \(a=r-s\) rend le critère
   tautologiquement faible et laisse le reste croître comme
   \((r-s)^{1/4}\). Le cutoff doit être fixé avant
   \(s\to-\infty\).
7. **Carré-fonction endpoint.** Le contrôle
   \(L^{3,\infty}(\ell^2)\) éventuel n'est pas
   \(\ell^2(L^2)\). Aucune permutation de ces normes n'est autorisée.
8. **Norme avant temps.** Le critère (49) perd les cancellations et n'est
   que suffisant. Le critère équivalent est (46).
9. **Suitability.** L'inégalité locale d'énergie contrôle des cylindres
   fixés. Elle ne somme pas automatiquement les coquilles spatiales qui
   représentent \(\xi\to0\).
10. **Énergie BSS.** Pour chaque \(s\), elle donne une énergie finie sur
    \([s,r]\), avec une constante pouvant croître comme
    \((r-s)^{1/2}\). Utiliser sa finitude point par point comme borne
    uniforme inverserait les quantificateurs.
11. **Pression.** La formulation projetée utilise la jauge globale de
    Riesz. Une pression seulement locale ne justifie pas sans raccord
    l'identité globale (20).
12. **Cocycle.** L'identité du cycle 0050 transporte les correcteurs mais
    ne produit aucune annulation des \(B_j\). Elle est compatible avec une
    classe quotient infrarouge non nulle.
13. **Profil adverse.** Pour
    \(g_H=(I-S(H))U_\sharp\), où \(U_\sharp\) est le champ lisse du cycle
    0050,

    \[
     \|S(a)g_H\|_2=C_UH^{1/4}+O_a(1)
     \quad(H\to\infty).                                   \tag{54}
    \]

    Le profil appartient à
    \(\widetilde L^{3,\infty}\cap\dot H^1\) et ses incréments sont
    énergétiques sur chaque bande, mais le critère bas échoue. Il n'est
    pas une solution de Navier--Stokes. La borne d'erreur dans (54) vient
    de

    \[
     (I-S(a))g_H=(I-S(H))(I-S(a))U_\sharp
    \]

    et de la contraction \(L^2\), puisque
    \((I-S(a))U_\sharp\in L^2\).
14. **Clay.** Une borne infrarouge sur une solution ancienne conditionnelle
    ne fournirait pas encore la réduction de tout blow-up, la rigidité
    \(L^2\) ancienne, ni une conclusion sur Type II.

## 10. Corrections bloquantes

Toute utilisation future du critère doit conserver les corrections
suivantes.

- Le seuil dyadique \(J\), ou le temps calorifique \(a\), est fixé avant la
  limite ancienne.
- Le carré fréquentiel porte sur \(g_{s,r}\in L^2\), jamais séparément sur
  les deux traces faible-\(L^3\).
- Le quotient du cycle 0050 explique pourquoi les deux termes séparés
  peuvent être non énergétiques alors que leur différence l'est.
- La borne haute uniforme (3) vient réellement de la PDE projetée et du
  stress \(v\otimes v\in L^{3/2,\infty}\); le cocycle seul ne la donne pas.
- Le contrôle bloc par bloc à l'endpoint ne peut pas être promu en
  sommabilité \(\ell^2\) basse.
- Le critère par \(B_j\) est équivalent; le critère par \(A_j\) est
  seulement suffisant, car il détruit les phases temporelles.
- La suitability locale et la pression locale ne remplacent pas la formule
  de Duhamel globale.
- Obtenir (9) force \(v(r)\in L^2\), mais ne force pas à lui seul
  \(v\equiv0\) sur tout le passé.

## 11. Prochain lemme

Le prochain lemme borné à tester est une **déplétion infrarouge du stress**.
Une formulation falsifiable est :

\[
\boxed{
\begin{gathered}
 \exists\varepsilon>0,\ \exists J,\ \exists s_n\to-\infty
 \text{ tels que, pour tout }j\le J,\\
 \left\|
 \int_{s_n}^r
 \Delta_jS(r-\tau)\mathbb P\operatorname{div}
 (v\otimes v)(\tau)\,d\tau
 \right\|_2
 \le C_r\,2^{\varepsilon(j-J)}
 \quad\text{uniformément en }n.
\end{gathered}}                                             \tag{55}
\]

Alors la somme géométrique de (46), puis (9), puis \(v(r)\in L^2\)
suivent immédiatement. Le gain
\(2^{\varepsilon(j-J)}\) est strictement favorable quand
\(j\to-\infty\).
Il doit provenir d'une annulation de triades, d'un moment nul du stress
effectif ou d'une identité de flux signée; il ne peut être déduit de la
seule taille \(M\).

**Décision : CONTINUER.** Le verrou énergétique ancien est réduit à (46),
ou équivalemment (9). Abandonner toute tentative de sommer directement les
blocs de \(v\) dans \(L^2\), et toute utilisation d'un cutoff dépendant de
\(s\). La prochaine expérience décisive doit mesurer ou réfuter un gain
infrarouge uniforme dans les intégrales vectorielles \(B_j\), en conservant
les phases plutôt qu'en sommant leurs normes absolues.
