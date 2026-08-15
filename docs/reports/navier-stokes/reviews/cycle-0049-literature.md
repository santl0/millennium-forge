# Cycle 0049 — globalisation de l'énergie relative à partir de la suitability locale

**Date de coupure :** 15 août 2026

**Nature :** audit bibliographique primaire contradictoire indépendant

**Verrou audité :** déterminer s'il existe un lemme publié transformant une
solution localement adaptée, scindée autour d'un flot calorique issu d'une
donnée faible-\(L^3\), dont le correcteur est seulement globalement dans
\(C_tL^2_x\), en une solution dont le correcteur appartient à
\(L^2_t\dot H^1_x\) et satisfait l'inégalité globale d'énergie perturbée.

L'équation est Navier--Stokes incompressible non forcé, de viscosité un, sur
\(\mathbb R^3\) :

\[
 \partial_t v-\Delta v+\operatorname{div}(v\otimes v)+\nabla q=0,
 \qquad \operatorname{div}v=0.                            \tag{1}
\]

Sur une fenêtre \([t_0,T]\), on fixe

\[
 a=v(t_0),\qquad V(t)=e^{(t-t_0)\Delta}a,qquad w=v-V.     \tag{2}
\]

## Verdict

1. **Il existe un résultat publié presque exactement ajusté une fois la
   dissipation déjà connue.** La proposition 3.2 d'Albritton--Barker (ARMA
   2019) transfère l'inégalité d'énergie locale de \(v\) vers le correcteur
   \(w\), puis la globalise par des cutoffs. Pour
   \(a\in L^{3,\infty}\), sa spécialisation \(p=4\), itéré de Picard
   \(k=0\), donne bien l'inégalité perturbée BSS.

2. **Cette proposition suppose cependant**

   \[
    w\in L^\infty_tL^2_x\cap L^2_t\dot H^1_x.             \tag{3}
   \]

   Elle ne produit donc pas la seconde moitié de (3) à partir du seul
   \(w\in C_tL^2_x\). La dissipation globale manquante est une hypothèse du
   lemme publié, pas sa conclusion.

3. **Le corollaire 3.9 d'Albritton--Barker atteint le temps initial**, avec
   trace nulle et taux \(\|w(t)\|_2\lesssim t^{1/4}\), mais seulement pour
   une solution faible Besov dont la définition contient déjà (3). Son
   argument ne peut pas servir de bootstrap non circulaire pour construire
   \(L^2_t\dot H^1_x\).

4. **Le lemme 3.3 de Barker--Seregin--Šverák est également insuffisant pour
   le verrou actif.** Son énoncé part d'une solution BSS au sens de leur
   définition 1.1, laquelle exige déjà (3) et l'inégalité globale perturbée.
   Il globalise une nouvelle scission de Calderón, mais ne démontre pas que
   la suitability locale et une borne globale \(L^2\) seules impliquent la
   classe BSS.

5. **Les solutions d'énergie locale de Lemarié-Rieusset, Jia--Šverák et
   Bradshaw--Tsai restent locales.** Leurs définitions suivent la pression
   par une expansion locale avec soustraction du noyau lointain et une
   jauge temporelle. Elles n'imposent ni pression globale intégrable, ni
   énergie globale, ni scission calorique énergétique. Une trace forte sur
   tout compact n'est pas une trace forte globale du correcteur.

6. **La veille 2025--2026 ne ferme pas le gap endpoint.** Popkin (2025)
   construit simultanément suitability et énergie pour un correcteur autour
   d'un fond strictement sous-critique; sa définition perturbée suppose déjà
   (3). Jarrín (`NS-SRC-0191`, arXiv v1, 2026) obtient une véritable
   promotion local-vers-global, mais pour l'équation non perturbée, une
   donnée globale \(L^2\) et une hypothèse supplémentaire de Morrey qui
   n'est pas impliquée par la seule borne
   \(L^\infty_tL^{3,\infty}_x\).

**Conclusion négative exacte.** Aucun lemme primaire contrôlé ne démontre

\[
 \boxed{
 \begin{gathered}
 v=V+w\text{ adaptée localement},\quad
 a\in L^{3,\infty},\quad w\in C_tL^2_x\\
 \Longrightarrow
 w\in L^2_t\dot H^1_x
 \text{ et énergie perturbée globale.}
 \end{gathered}}                                          \tag{4}
\]

Le premier maillon publié commence après l'ajout de
\(w\in L^2_t\dot H^1_x\), ou après l'ajout d'une condition de décroissance
spatiale de type Morrey suffisamment forte dans le problème non perturbé.

## 1. Résultat publié le plus proche : Albritton--Barker

### 1.1 Source, équation et définition

Dallas Albritton et Tobias Barker,
[*Global Weak Besov Solutions of the Navier--Stokes Equations and
Applications*](https://doi.org/10.1007/s00205-018-1319-0), *Archive for
Rational Mechanics and Analysis* **232** (2019), 197--263;
[`arXiv:1802.03164v2`](https://arxiv.org/abs/1802.03164v2).

L'article traite (1) sur \(Q_T=\mathbb R^3\times(0,T)\), éventuellement
avec une force extérieure \(\operatorname{div}F\). Pour une donnée dans
\(\dot B^{-1+3/p}_{p,\infty}\), \(p>3\), il introduit les itérés de Picard
\(P_k\) et le défaut

\[
 F_k=P_k\otimes P_k-P_{k-1}\otimes P_{k-1},
 \qquad P_{-1}=0.                                         \tag{5}
\]

La définition 1.5 d'une solution faible Besov basée sur \(P_k\) exige :

- l'équation distributionnelle avec
  \(q\in L^{3/2}_{\rm loc}(Q_T)\);
- la scission \(v=P_k+w\);
- **les deux bornes**
  \(w\in L^\infty_tL^2_x\cap L^2_t\dot H^1_x\);
- la continuité faible \(L^2\) sur \([0,T]\) et la trace forte
  \(\|w(t)\|_2\to0\);
- \(F_\ell\in L^2(Q_T)\) pour tout \(\ell\ge k\);
- l'inégalité locale d'énergie pour la paire complète \((v,q)\).

Contrairement à la définition BSS, l'inégalité **globale** d'énergie du
correcteur n'est pas placée dans cette définition. Elle est dérivée ensuite.
Mais l'appartenance dissipative \(L^2_t\dot H^1_x\) y est explicitement
placée.

### 1.2 Proposition 3.2 : transfert local puis cutoff global

Écrivons \(p=q-\pi_k\), où \(\pi_k\) est la pression de l'itéré. La
proposition 3.2 démontre l'inégalité locale du correcteur

\[
\begin{aligned}
 \int\phi|w(t)|^2+2\int_0^t\!\int\phi|\nabla w|^2
 \le{}&\int_0^t\!\int |w|^2(\partial_t\phi+\Delta\phi)\\
 &+\big[|w|^2(w+P_k)+2pw\big]\cdot\nabla\phi\\
 &+2\big[P_k\otimes w+F_k\big]:\nabla(\phi w),
                                                               \tag{6}
\end{aligned}
\]

puis, pour presque tout \(t_1>0\) et tout \(t_2>t_1\),

\[
\begin{aligned}
 \|w(t_2)\|_2^2+2\int_{t_1}^{t_2}\|\nabla w\|_2^2
 \le \|w(t_1)\|_2^2
 +2\int_{t_1}^{t_2}\!\int
   (P_k\otimes w+F_k):\nabla w.                         \tag{7}
\end{aligned}
\]

La première étape soustrait l'égalité locale de \(P_k\) à l'inégalité
locale de \(v\) au moyen d'une identité faible-forte. La seconde utilise
\(\Phi_{\varepsilon,R}(x,t)=\eta_\varepsilon(t)\psi(x/R)\), laisse
\(R\to\infty\), puis \(\varepsilon\to0\).

Les hypothèses employées pour annuler les flux à l'infini sont indiquées
explicitement dans la preuve :

\[
 w\in L^\infty_tL^2_x\cap L^2_t\dot H^1_x,
 \quad p\in L^{3/2}(Q_T)+L^2_{t,\rm loc}L^2_x,
 \quad P_k\in L^\infty(\mathbb R^3\times[\delta,T]),
 \quad F_k\in L^2(Q_T).                                  \tag{8}
\]

Ainsi, les queues spatiales de \(w\), de \(\nabla w\), du produit cubique
et de la pression sont déjà sommables globalement. La preuve n'établit pas
ces propriétés à partir de la borne \(L^2\) de \(w\).

### 1.3 Spécialisation exacte à une donnée faible-\(L^3\)

L'estimation calorique de Lorentz donne

\[
 L^{3,\infty}(\mathbb R^3)
 \hookrightarrow \dot B^{-1/4}_{4,\infty}(\mathbb R^3),
 \qquad
 \sup_{t>0}t^{1/8}\|e^{t\Delta}a\|_4
 \le C\|a\|_{3,\infty}.                                 \tag{9}
\]

On peut donc choisir \(p=4\). Alors
\(k(p)=\lceil p/2\rceil-2=0\),

\[
 P_0=V=e^{t\Delta}a,qquad F_0=V\otimes V,                \tag{10}
\]

et

\[
 \|V\|_{L^4(Q_T)}\le C T^{1/8}\|a\|_{3,\infty},
 \qquad
 \|V\otimes V\|_{L^2(Q_T)}
 \le C T^{1/4}\|a\|_{3,\infty}^2.                       \tag{11}
\]

L'inégalité (7) devient exactement

\[
 \|w(t_2)\|_2^2+2\int_{t_1}^{t_2}\|\nabla w\|_2^2
 \le \|w(t_1)\|_2^2
 +2\int_{t_1}^{t_2}\!\int
  (V\otimes w+V\otimes V):\nabla w,                     \tag{12}
\]

qui est l'inégalité perturbée recherchée.

**Transfert valide :** suitability de \(v\) + scission calorique +
correcteur dans la **classe d'énergie complète** impliquent (12).

**Transfert invalide :** remplacer dans cet énoncé la classe d'énergie
complète par \(w\in C_tL^2_x\). Cela supprime une hypothèse utilisée dans le
passage \(R\to\infty\).

### 1.4 Atteindre \(t_1=0\) n'est pas gratuit

La proposition 3.5 obtient

\[
 \|w(t)\|_2\le C(M,p,k)t^{1/4}.                            \tag{13}
\]

Le corollaire 3.9 en déduit \(P_k\otimes w\in L^2(Q_T)\) et
l'inégalité globale depuis zéro. Pour \(k=0\), elle coïncide avec (12),
\(t_1=0\) et \(w(0)=0\).

La preuve de (13) scinde toutefois encore les données, introduit un
correcteur \(w_k\) qui appartient déjà à
\(L^\infty L^2\cap L^2\dot H^1\), puis applique une inégalité d'énergie
globale à ce correcteur. Le corollaire 3.9 améliore le temps initial et
l'intégrabilité du terme mixte; il ne construit pas la dissipation à partir
de zéro.

## 2. Barker--Seregin--Šverák : ce que fait réellement le lemme 3.3

La source est H. Barker, G. Seregin et V. Šverák,
[*On Stability of Weak Navier--Stokes Solutions with Large
\(L^{3,\infty}\) Initial Data*](https://doi.org/10.1080/03605302.2018.1449219),
*CPDE* **43** (2018), 628--651;
[`arXiv:1603.03211v1`](https://arxiv.org/abs/1603.03211v1).

### 2.1 Dépendances de la définition 1.1

La définition BSS impose à \(v=V+u\), \(V=e^{t\Delta}u_0\) :

\[
 u\in L^\infty_tL^2_x\cap L^2_t\dot H^1_x,                \tag{14}
\]

la continuité faible \(L^2\), l'inégalité globale perturbée, une pression
locale \(q\in L^{3/2}_{\rm loc}\) et l'inégalité locale d'énergie pour
\((v,q)\). La remarque 1.2 déduit de l'inégalité globale la trace forte
\(u(t)\to0\) dans \(L^2\).

Par conséquent, tout lemme énoncé « soit \(v\) comme dans la définition
1.1 » peut utiliser (14) et l'inégalité que le cycle 0049 cherche justement
à démontrer.

### 2.2 Scission de Calderón et lemme 3.3

Le lemme 2.1 scinde, pour un seuil \(N\),

\[
 u_0=\bar u_0^N+\widetilde u_0^N,qquad
 \bar u_0^N\in L^{10/3},quad
 \widetilde u_0^N\in L^2,                                \tag{15}
\]

avec des bornes explicites dépendant de \(N\) et de
\(\|u_0\|_{3,\infty}\). BSS pose

\[
 \bar V^N=e^{t\Delta}\bar u_0^N,qquad
 \widetilde V^N=e^{t\Delta}\widetilde u_0^N,qquad
 w^N=u+\widetilde V^N=v-\bar V^N.                         \tag{16}
\]

Le lemme 3.3 démontre

\[
\begin{aligned}
 \|w^N(t)\|_2^2+2\int_0^t\|\nabla w^N\|_2^2
 \le \|\widetilde u_0^N\|_2^2
 +2\int_0^t\!\int
  (\bar V^N\otimes w^N+\bar V^N\otimes\bar V^N):\nabla w^N.
                                                               \tag{17}
\end{aligned}
\]

Sa preuve commence par transférer l'inégalité locale de \(v\) à \(w^N\),
puis utilise des cutoffs spatiaux. Pour le flux de pression, elle décompose
\((u,q)=\sum_{i=1}^3(u_i,p_i)\) par régularité maximale de Stokes et emploie
globalement

\[
 (u_i,\nabla p_i)\in
 W^{2,1}_{9/8,3/2}\times L_{9/8,3/2},\quad
 W^{2,1}_{11/7}\times L_{11/7},\quad
 W^{2,1}_{5/4,3/2}\times L_{5/4,3/2}.                     \tag{18}
\]

Les estimations (3.23)--(3.25) font tendre les trois flux annulaire de
pression vers zéro grâce aux queues globales de \(w^N\) et des gradients de
pression. Or le lemme 3.2 qui fournit (18) suppose déjà (14).

**Lecture contradictoire.** L'inégalité BSS (1.10) ne semble pas réutilisée
directement dans chaque ligne du cutoff du lemme 3.3, sauf notamment via la
trace invoquée par la remarque 1.2. Mais l'appartenance
\(L^2_t\dot H^1_x\), indispensable à (18) et aux limites annulaires, reste
une hypothèse explicite de son énoncé. Extraire du calcul une version qui ne
suppose que \(C_tL^2_x\) serait un nouveau lemme, non le lemme 3.3 publié.

## 3. Solutions d'énergie locale : local ne signifie pas global

### 3.1 Jia--Šverák

Dans Hao Jia et Vladimír Šverák,
[*Local-in-space estimates near initial time for weak solutions of the
Navier--Stokes equations and forward self-similar
solutions*](https://doi.org/10.1007/s00222-013-0468-x), *Inventiones
Mathematicae* **196** (2014), 233--265;
[`arXiv:1204.0529`](https://arxiv.org/abs/1204.0529), la définition 3.1 d'une
solution de Leray locale impose :

- énergie et dissipation uniformément locales sur chaque échelle finie;
- disparition de l'énergie locale intégrée lorsque le centre spatial tend
  vers l'infini;
- équation distributionnelle et trace forte dans \(L^2(K)\) pour tout
  compact \(K\);
- inégalité locale d'énergie.

La pression est représentée sur \(B_r(x_0)\) par

\[
\begin{aligned}
 p(x,t)={}&-\Delta^{-1}\operatorname{divdiv}
            (u\otimes u\,\chi)(x,t)\\
 &-\int_{\mathbb R^3}
   [K(x-y)-K(x_0-y)](u\otimes u)(y,t)(1-\chi(y))\,dy+c(t).
                                                               \tag{19}
\end{aligned}
\]

La différence de noyaux décroît comme \(|y|^{-4}\), ce qui rend (19)
localement définie. Elle ne place pas nécessairement \(p\) dans un espace
global dont la queue sur \(B_{2R}\setminus B_R\) tend vers zéro.

Jia--Šverák remarquent que toute solution Leray--Hopf adaptée entre dans
cette classe locale. Ils n'affirment pas la réciproque à partir d'une borne
globale \(L^2\) de la vitesse ou d'un correcteur.

### 3.2 Bradshaw--Tsai et le cadre Lemarié-Rieusset

Zachary Bradshaw et Tai-Peng Tsai,
[*Global existence, regularity, and uniqueness of infinite energy solutions
to the Navier--Stokes equations*](https://doi.org/10.1080/03605302.2020.1761386),
*CPDE* **45** (2020), 1168--1201;
[`arXiv:1907.00256v1`](https://arxiv.org/abs/1907.00256v1), donnent dans la
définition 1.1 une version moderne des solutions d'énergie locale de
Lemarié-Rieusset.

Elle exige des bornes \(L^2_{\rm uloc}\), une dissipation uniformément
locale, une pression de la forme (19) à toute échelle, la trace forte locale,
la suitability et la continuité faible contre les tests \(L^2\) compacts.
Elle autorise explicitement une énergie totale infinie et n'impose aucune
scission \(e^{t\Delta}a+w\).

Cette formulation montre trois écarts indépendants avec (4) :

1. \(u(t)\to u_0\) dans \(L^2(K)\) ne donne pas
   \(w(t)\to0\) dans \(L^2(\mathbb R^3)\);
2. \(\nabla u\in L^2_{\rm loc}\) ne donne pas la somme sur toutes les
   coquilles spatiales;
3. la pression locale (19), définie modulo \(c(t)\), ne fournit pas la queue
   globale requise par le cutoff de la proposition 3.2.

Le cadre Lemarié-Rieusset est donc une source pour la **suitability locale et
la pression**, non pour le raccord énergétique global recherché.

## 4. Ledger pression, trace et dissipation

| Cadre | Trace au temps initial | Pression | Dissipation globale | Énergie perturbée globale |
|---|---|---|---|---|
| Cycle 0048, hypothèses actives | \(w\in C_tL^2\), \(w(t_0)=0\) | Riesz globale supposée pour \(v\) | non démontrée | non démontrée |
| BSS, définition 1.1 | faible \(L^2\), puis forte par l'énergie | \(L^{3/2}_{\rm loc}\), décomposition Stokes dans la preuve | supposée | supposée |
| BSS, lemme 3.3 | forte pour \(w^N\) | trois composantes globalement contrôlées | supposée via la définition | démontrée pour la nouvelle scission |
| Albritton--Barker, définition 1.5 | faible \(L^2\) + forte nulle | locale pour \(v\), relative pour \(w\) | supposée | pas supposée |
| Albritton--Barker, proposition 3.2 | même trace | \(L^{3/2}+L^2_{t,\rm loc}L^2_x\) pour la partie relative | supposée | démontrée depuis presque tout \(t_1>0\) |
| Albritton--Barker, corollaire 3.9 | taux \(t^{1/4}\) | idem | supposée en amont | démontrée depuis zéro |
| Jia--Šverák / Bradshaw--Tsai | forte sur tout compact | expansion locale soustraite + jauge \(c(t)\) | seulement locale | absente |

## 5. Pourquoi le cutoff ne se ferme pas avec le seul \(C_tL^2\)

Supposons que (6) soit déjà établie localement avec \(P_0=V\). Un cutoff
\(\psi_R\) produit notamment :

\[
 R^{-2}\int_{A_R}|w|^2,qquad
 R^{-1}\int_{A_R}|w|^3,qquad
 R^{-1}\int_{A_R}|p||w|,qquad
 \int\psi_R(V\otimes w):\nabla w,                         \tag{20}
\]

où \(A_R=B_{2R}\setminus B_R\).

- Le premier terme est compatible avec \(w\in L^\infty_tL^2_x\).
- Les deuxième et troisième demandent respectivement une sommabilité
  globale issue de \(L^2_t\dot H^1_x\) et une vraie information de queue sur
  la pression relative.
- Le quatrième est critique. Si \(w\in\dot H^1\), Sobolev--Lorentz donne

  \[
   \left|\int(V\otimes w):\nabla w\right|
   \le C\|V\|_{3,\infty}\|w\|_{6,2}\|\nabla w\|_2
   \le C\|a\|_{3,\infty}\|\nabla w\|_2^2.                \tag{21}
  \]

  À grande norme, le coefficient de (21) ne peut pas être absorbé. Réduire
  l'intervalle temporel ne le rend pas petit.
- Le terme \(V\otimes V\) est moins problématique, car (11) le place dans
  \(L^2(Q_T)\), mais cela ne répare pas le terme mixte critique.

Ainsi, utiliser (21) pour démontrer
\(\int\|\nabla w\|_2^2<\infty\) suppose déjà que cette intégrale est un
objet global fini, ou requiert une scission supplémentaire qui rétablit la
coercivité. C'est le cercle exact évité dans les constructions de Calderón,
BSS, Albritton--Barker et Popkin par une approximation énergétique en amont.

## 6. Passe contradictoire sur les lemmes candidats

### 6.1 Quantificateur inversé

La proposition 3.2 dit :

\[
 \text{solution faible Besov, donc (3), + suitability}
 \Longrightarrow \text{énergie globale}.                 \tag{22}
\]

Elle ne dit pas :

\[
 \text{suitability + }L^\infty L^2
 \Longrightarrow (3).                                    \tag{23}
\]

### 6.2 Hypothèse silencieuse de pression

Remplacer la pression relative globale d'Albritton--Barker par la seule
pression locale de Jia--Šverák supprime la propriété de queue utilisée pour
laisser \(R\to\infty\). La constante temporelle de pression disparaît contre
\(\operatorname{div}w=0\), mais la partie harmonique spatiale et le terme
lointain ne disparaissent pas par une simple jauge.

### 6.3 Trace locale versus globale

La trace forte locale d'une solution d'énergie locale n'empêche pas une
quantité \(L^2\) de se déplacer vers l'infini lorsque \(t\downarrow t_0\).
Le \(C_tL^2\) global obtenu au cycle 0048 est donc une amélioration réelle,
mais il ne contrôle toujours pas la somme de la dissipation sur les
coquilles.

### 6.4 Le premier lemme réellement transférable

La scission (15)--(16) suggère le candidat non circulaire suivant :

\[
\begin{gathered}
 w^N\in C_tL^2_x\cap L^2_t\dot H^1_{\rm loc},
 \quad \bar V^N\text{ sous-critique},
 \quad \text{inégalité relative locale},\\
 \text{pression relative avec queue contrôlée}
 \Longrightarrow
 w^N\in L^2_t\dot H^1_x\text{ et (17)}.                  \tag{24}
\end{gathered}
\]

Le fond \(\bar V^N\), issu de \(L^{10/3}\), fournit un coefficient de
Gronwall temporellement intégrable, contrairement au fond critique non
scindé. Aucun des énoncés audités ne donne (24) sans avoir déjà construit
\(w^N\) par une méthode de Galerkin ou supposé son énergie globale. (24) est
donc un lemme de recherche légitime, pas une citation disponible.

## 7. Veille différentielle 2025--2026 limitée au verrou

### 7.1 Popkin 2025 : construction sous-critique, pas caractérisation

Henry Popkin,
[*On Rough Calderón Solutions to the Navier--Stokes Equations and
Applications to the Singular Set*](https://doi.org/10.1007/s00021-025-00930-6),
*Journal of Mathematical Fluid Mechanics* **27** (2025), article 25;
[`arXiv:2410.07816`](https://arxiv.org/abs/2410.07816), est un article publié
le 4 mars 2025.

Sa définition 2.8 d'une solution adaptée de l'équation perturbée autour
d'un fond \(m\) suppose

\[
 m\in L^p_tL^q_x,\qquad 2/p+3/q<1, q>3,qquad
 w\in L^\infty_tL^2_x\cap L^2_t\dot H^1_x,                \tag{25}
\]

ainsi qu'une pression relative \(L^{3/2}\) et l'inégalité locale
perturbée. Le théorème A construit \(m\) et \(w\), puis affirme séparément
la trace, l'énergie globale perturbée et la suitability. La coercivité vient
du caractère **strictement sous-critique** du fond et de la construction
Galerkin. Le cas critique \(m=e^{t\Delta}a\),
\(a\in L^{3,\infty}\) grand, n'est pas obtenu par ce théorème.

### 7.2 Jarrín 2026 : promotion réelle, mais non perturbée et avec Morrey

Oscar Jarrín,
[*A remark on very weak suitable solutions and Leray solutions of the
Navier--Stokes equations*](https://arxiv.org/abs/2607.03602v1),
`arXiv:2607.03602v1`, 3 juillet 2026, est une prépublication non publiée
identifiée dans le catalogue comme `NS-SRC-0191`.

Son théorème 1.1 part d'une solution très faible adaptée de l'équation
**non perturbée**, avec donnée \(u_0\in L^2\), continuité faible locale et
trace forte locale au temps zéro. Il suppose en plus

\[
 u\in\mathcal M^{p,\gamma}_{t,x},qquad
 0<\gamma<3\le p<\infty,qquad
 \frac\gamma p-\frac3p+\frac23<0.                         \tag{26}
\]

Il applique l'inégalité locale à un cutoff et obtient directement la borne
globale d'énergie en faisant \(R\to\infty\). Le mécanisme est donc un analogue
positif de (24), mais :

- le champ complet a une donnée globale \(L^2\);
- il n'y a ni drift calorique, ni force \(\operatorname{div}(V\otimes V)\);
- (26) impose une décroissance moyenne spatiale stricte; les exemples
  Lorentz de l'article ont \(3\le p<q<9/2\), et non la seule borne
  \(L^\infty_tL^{3,\infty}_x\);
- le théorème ne fournit pas la pression relative de (24).

Jarrín valide la stratégie « contrôler quantitativement les flux de cutoff »
mais ne ferme aucune arête endpoint BSS.

**Verdict de veille :** aucune source primaire 2025--2026 vérifiée ne
démontre (4). Popkin confirme la route sous-critique par construction;
Jarrín confirme qu'une condition de décroissance Morrey peut suffire dans
le problème non perturbé.

## 8. Échelle et arêtes de dépendance

Sous \(v_\lambda(x,t)=\lambda v(\lambda x,\lambda^2t)\) :

\[
 \|a_\lambda\|_{3,\infty}=\|a\|_{3,\infty},qquad
 \|w_\lambda(t)\|_2^2=\lambda^{-1}\|w(\lambda^2t)\|_2^2,
 \qquad
 \int\|\nabla w_\lambda\|_2^2dt
 =\lambda^{-1}\int\|\nabla w\|_2^2dt.                   \tag{27}
\]

L'inégalité (12) est donc homogène. En revanche, (11) porte une puissance de
\(T\) et ne donne pas à elle seule une coercivité critique uniforme.

| Arête | Statut | Source / obstacle |
|---|---|---|
| suitable \(v\) + itéré régulier \(P_k\) \(\to\) inégalité relative locale pour \(w\) | publiée | Albritton--Barker, prop. 3.2 |
| inégalité relative locale + classe d'énergie globale \(\to\) énergie perturbée depuis \(t_1>0\) | publiée | Albritton--Barker, prop. 3.2 |
| données critiques Besov + classe d'énergie globale \(\to\) taux \(t^{1/4}\) et énergie depuis zéro | publiée | Albritton--Barker, prop. 3.5 et cor. 3.9 |
| solution BSS \(\to\) énergie pour une scission Calderón modifiée | publiée | BSS, lemme 3.3 |
| solution locale-énergie \(\to\) pression locale cohérente | publiée | Jia--Šverák; Bradshaw--Tsai |
| solution très faible adaptée + Morrey (26) \(\to\) Leray | prépublication 2026 | Jarrín, th. 1.1 |
| suitable relative + \(C_tL^2\) seulement \(\to L^2_t\dot H^1\) | **manquante** | flux cubique, pression et drift critique |
| arête précédente après scission sous-critique (24) | **non trouvée comme théorème de caractérisation** | constructions Galerkin disponibles, promotion abstraite absente |

## 9. Sources et empreintes contrôlées

| Source primaire | Version contrôlée | SHA-256 du PDF local |
|---|---|---|
| Barker--Seregin--Šverák, CPDE 2018 | `arXiv:1603.03211v1` et manuscrit accepté | `ADEACBBB2E18A2E4C2C29E057AEA8B7293949602066F68AC0BCD8C999A1003A2` (arXiv); `E623CCA4A7F5622BB2BFE27681395B2578ED65E402882236D0F6990BD58699DB` (accepté) |
| Albritton--Barker, ARMA 2019 | `arXiv:1802.03164v2`, 3 juin 2018 | `0834BAF4A72A9E8278EE9CF7EC80A87ADF2D00EC8624B6784E2069EA3BF7923D` |
| Jia--Šverák, Invent. Math. 2014 | `arXiv:1204.0529` | `1E8685FBE09C669854357278010F345FA5C98845C5888BA6720936A0B3F1591F` |
| Bradshaw--Tsai, CPDE 2020 | `arXiv:1907.00256v1` | `60C8773D2C7EA90B6DA2D534905F436D6AFE2A68112E54DD054F378DC3ED4AF7` |
| Jarrín 2026 | `arXiv:2607.03602v1` | `A56BBD3C009C64D9584847183F66A4F114AA6B34527E9DF82337932CAF7B02CB` |
| Popkin, JMFM 2025 | version publiée et `arXiv:2410.07816` | version publiée primaire contrôlée en ligne; aucun hash local retenu après échec TLS du téléchargement arXiv |

### Entrée source réellement nécessaire

Une seule nouvelle entrée du catalogue est nécessaire pour porter le verdict
positif de ce cycle : **Albritton--Barker, ARMA 2019**, avec la proposition
3.2, la proposition 3.5 et le corollaire 3.9 comme localisateurs. C'est la
source primaire exacte de l'arête

\[
 \text{classe d'énergie complète + suitability locale}
 \Longrightarrow \text{énergie perturbée globale}.        \tag{28}
\]

BSS est déjà catalogué sous `NS-SRC-0188` et Jarrín sous
`NS-SRC-0191`. Jia--Šverák et Bradshaw--Tsai servent ici à borner la notion
local-energy; leur ajout éventuel peut être mutualisé avec le registre général,
mais n'est pas requis pour attribuer (28). Popkin 2025 est une veille
différentielle utile et négative pour l'endpoint; il n'est pas nécessaire de
l'ajouter pour soutenir le lemme actif, puisqu'il construit une classe
sous-critique différente et ne fournit pas le raccord manquant.

## Décision bibliographique

**CONTINUER**, mais sous le statut `AI_INTERNAL_DERIVATION` pour tout essai
de prouver (24). La proposition 3.2 d'Albritton--Barker doit être enregistrée
comme le raccord publié une fois la classe d'énergie complète acquise.
**RÉVISER** toute attribution de la dissipation globale au lemme 3.3 BSS.
**ABANDONNER** le cutoff non scindé fondé sur l'absorption de (21) à grande
norme. La prochaine expérience décisive doit tester (24) avec la scission
BSS \(L^{10/3}+L^2\), en suivant explicitement les trois composantes de
pression et en interdisant toute utilisation préalable de
\(\int\|\nabla w^N\|_2^2<\infty\).
