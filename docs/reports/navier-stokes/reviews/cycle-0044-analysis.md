# Cycle 0044 — fuite locale de la force sous cutoff externe

Date : 2026-08-15

Statut : \`AI_INTERNAL_DERIVATION\`; aucun résultat Clay, aucune preuve
assistée par ordinateur.

## Verdict

Le lemme local est **vrai**, avec deux qualifications indispensables :

1. la pression doit être fixée dans la jauge globale de Riesz, de sorte que
   \(H=\mathbb P\operatorname{div}(U\otimes U)\) ;
2. \(Q_L\) doit être la dilatation exacte d'une même réalisation unité de
   Bogovskii, avec une borne uniforme
   \(L^{3,\infty}\to L^{3,\infty}\).

Alors, pour tout compact \(B_R\), tout \(L\ge2R\) et tout multi-indice
\(\alpha\),

\[
 \left.F_L\right|_{B_R}
 =\left.\mathbb P\operatorname{div}
   (Z_L\otimes Z_L-U\otimes U)\right|_{B_R},       \tag{1}
\]

et

\[
 \boxed{
 \|\partial^\alpha F_L\|_{L^\infty(B_R)}
 \le C_\alpha(1+C_Q^2)M^2L^{-3-|\alpha|}.}         \tag{2}
\]

La constante ne dépend ni de \(L\), ni de \(R\), ni du temps. Elle dépend de
la convention de norme de Lorentz, de \(\alpha\), de la dimension et de la
borne unité \(C_Q\).

Cette décroissance est strictement locale. Lorsque \(\kappa\ne0\), une
famille pure-swirl à l'échelle \(L\) vérifie

\[
 \|U_L\|_{L^{3,\infty}}=\|V\|_{L^{3,\infty}},
 \qquad
 \|F_L\|_X\ge c|\kappa|L^2-C,                    \tag{3}
\]

pour

\[
 X=L^1+\operatorname{div}L^{3/2,\infty}.
\]

Ainsi une force peut tendre vers zéro avec toutes ses dérivées sur chaque
compact fixé, tout en croissant dans la norme critique globale \(X\).

## 1. Conventions exactes

Tous les champs vivent sur \(\mathbb R^3\). La divergence d'un tenseur est
prise sur le second indice :

\[
 (\operatorname{div}T)_i=\partial_jT_{ij}.        \tag{4}
\]

La projection globale de Leray est

\[
 \mathbb P
 =I+\nabla(-\Delta)^{-1}\operatorname{div},       \tag{5}
\]

où

\[
 \Gamma(x)=\frac1{4\pi|x|},\qquad
 (-\Delta)^{-1}f=\Gamma*f.                       \tag{6}
\]

Cette convention a le symbole
\(I-\xi\otimes\xi/|\xi|^2\).

On fixe

\[
 A=\{1<|y|<2\},\qquad
 \chi\in C_c^\infty(B_2),\qquad
 \chi=1\text{ sur un voisinage de }\overline{B_1},
                                                               \tag{7}
\]

avec \(\operatorname{supp}\nabla\chi\Subset A\). Pour \(L\ge1\),

\[
 \chi_L(y)=\chi(y/L),\qquad
 a_L=\nabla\chi_L=L^{-1}(\nabla\chi)(y/L),
 \qquad A_L=\{L<|y|<2L\}.                       \tag{8}
\]

### Conjugaison de Bogovskii

Soit \(\mathcal B\) la réalisation unité supportée fixée au cycle 0043.
Pour une distribution scalaire \(h\) de moyenne nulle supportée dans
\(A_L\), posons

\[
 (\mathcal B_Lh)(y)
 =L\,\mathcal B[h(L\,\cdot)](y/L).              \tag{9}
\]

Alors

\[
 \operatorname{div}\mathcal B_Lh=h,\qquad
 \operatorname{supp}\mathcal B_Lh\subset A_L.   \tag{10}
\]

Le cutoff solénoïdal est

\[
 Q_LW=\chi_LW-\mathcal B_L(a_L\cdot W),\qquad
 Z_L=Q_LU.                                      \tag{11}
\]

Si

\[
 (\mathcal D_LV)(y)=L^{-1}V(y/L),               \tag{12}
\]

alors un changement de variable dans (9) donne l'identité de conjugaison

\[
 Q_L\mathcal D_L=\mathcal D_LQ.                 \tag{13}
\]

Comme \(\mathcal D_L\) est une isométrie de \(L^{3,\infty}\),

\[
 \|Q_LW\|_{L^{3,\infty}}
 \le C_Q\|W\|_{L^{3,\infty}}                    \tag{14}
\]

avec le même \(C_Q\) pour tout \(L\), dès que l'opérateur unité \(Q\) est
borné sur \(L^{3,\infty}\). La réalisation pseudodifférentielle d'ordre
moins un du cycle 0043 possède cette propriété après composition avec
\(a=\nabla\chi\).

Le seul énoncé « \(Q_L\) est solénoïdal sur \(A_L\) » ne suffit pas à (14).
Une famille de droites inverses choisie indépendamment pour chaque \(L\)
pourrait avoir une norme d'opérateur arbitrairement grande. L'uniformité de
(2) serait alors indémontrée.

## 2. Pression, \(H\) et définition de la force

On fixe la pression de Riesz

\[
 P=(-\Delta)^{-1}\partial_i\partial_j(U_iU_j)
   =R_iR_j(U_iU_j).                              \tag{15}
\]

Avec

\[
 S=U\otimes U+PI,\qquad
 H=\operatorname{div}S
   =\operatorname{div}(U\otimes U)+\nabla P,     \tag{16}
\]

on a

\[
 \operatorname{div}H=0,\qquad
 H=\mathbb P\operatorname{div}(U\otimes U).      \tag{17}
\]

L'égalité (17), et non la seule identité
\(\operatorname{div}H=0\), est le raccord de pression nécessaire au lemme.
Une pression munie d'une composante harmonique spatiale non fixée pourrait
modifier \(H\). Une constante dépendant du temps ne le modifie pas.

Posons

\[
 D=I+y\cdot\nabla,\qquad
 K_L=-[\Delta,Q_L]U+\kappa[D,Q_L]U,              \tag{18}
\]

et

\[
 F_L
 =\mathbb P\operatorname{div}(Z_L\otimes Z_L)
  -Q_LH+K_L.                                    \tag{19}
\]

Comme l'identité commute avec tout opérateur,
\([D,Q_L]=[y\cdot\nabla,Q_L]\).

Les calculs sont classiques pour \(U\) lisse. Ils restent distributionnels
pour \(U\in L^{3,\infty}\) lorsque les prolongements de \(Q_L\) employés dans
(19) sont ceux du cycle 0043.

## 3. Support exact et identité sur le core

Sur \(B_L\), on a

\[
 Q_LW=W,                                        \tag{20}
\]

pour toute entrée admissible \(W\) : le multiplicateur vaut un et le
correcteur de Bogovskii est supporté dans \(A_L\). En particulier,

\[
 Z_L=U,\qquad Q_LH=H
 \quad\text{sur }B_L.                            \tag{21}
\]

De même,

\[
 [\Delta,Q_L]U=0,\qquad [D,Q_L]U=0
 \quad\text{sur }B_L,                            \tag{22}
\]

car \(Q_LU=U\), \(Q_L\Delta U=\Delta U\) et
\(Q_LDU=DU\) sur un voisinage de chaque point du core. Ainsi
\(K_L=0\) sur \(B_L\).

Pour \(L\ge2R\), les équations (17), (19), (21) et (22) donnent sur \(B_R\)

\[
 \begin{aligned}
 F_L
 &=\mathbb P\operatorname{div}(Z_L\otimes Z_L)-H\\
 &=\mathbb P\operatorname{div}(Z_L\otimes Z_L)
   -\mathbb P\operatorname{div}(U\otimes U)\\
 &=\mathbb P\operatorname{div}
   (Z_L\otimes Z_L-U\otimes U).
 \end{aligned}                                  \tag{23}
\]

C'est (1). Cette égalité est une égalité de restrictions de distributions,
et non une égalité globale : hors du core, \(Q_LH-H\) et \(K_L\) ne
s'annulent pas.

Posons

\[
 T_L=Z_L\otimes Z_L-U\otimes U.                 \tag{24}
\]

Alors

\[
 T_L=0\text{ sur }B_L.                           \tag{25}
\]

Mais \(T_L\) n'est généralement pas compact : hors de \(B_{2L}\),
\(Z_L=0\) et

\[
 T_L=-U\otimes U.                               \tag{26}
\]

La source de la queue locale est donc tout l'extérieur de \(B_L\), pas
seulement la couronne de transition.

## 4. Terme delta de Leray et queue de pression

Pour un tenseur \(T\),

\[
 (\mathbb P\operatorname{div}T)_i
 =\partial_jT_{ij}
  +\partial_i(-\Delta)^{-1}\partial_k\partial_jT_{kj}.
                                                               \tag{27}
\]

La première sommation est le terme local provenant de l'identité dans
\(\mathbb P\). La dérivée distributionnelle du noyau de Riesz contient elle
aussi une partie locale à l'origine. Il serait donc faux de remplacer
globalement \(\mathbb P\operatorname{div}\) par le noyau classique
\(\nabla^3\Gamma\).

Ici cette difficulté disparaît pour une raison explicite : si
\(x\in B_R\), alors \(T_L\) est nul dans un voisinage de \(x\). Le terme
\(\partial_j(T_L)_{ij}\) et toutes les contributions delta sont nuls à cet
endroit. L'équation (27) devient l'intégrale absolument convergente

\[
 (\partial^\alpha F_L)_i(x)
 =\int_{|y|\ge L}
   \partial^\alpha\partial_i\partial_k\partial_j
   \Gamma(x-y)\,(T_L)_{kj}(y)\,dy.              \tag{28}
\]

Cette formule recalcule la pression au lieu de supposer la projection
locale. Elle montre aussi que, dans \(B_L\), \(F_L\) est le gradient d'un
potentiel harmonique et est simultanément divergence-free.

Pour \(x\in B_R\), \(L\ge2R\) et \(|y|\ge L\),

\[
 |x-y|\ge |y|-R\ge\frac{|y|}{2}.                \tag{29}
\]

Les dérivées du noyau newtonien satisfont

\[
 |\partial^\alpha\nabla^3\Gamma(x-y)|
 \le C_\alpha|y|^{-4-|\alpha|}.                 \tag{30}
\]

## 5. Estimation Lorentz et puissance de \(L\)

Le produit faible de Lorentz et (14) donnent

\[
 \begin{aligned}
 \|T_L\|_{L^{3/2,\infty}}
 &\le C\left(
   \|Z_L\|_{L^{3,\infty}}^2
   +\|U\|_{L^{3,\infty}}^2\right)\\
 &\le C(1+C_Q^2)M^2.                            \tag{31}
 \end{aligned}
\]

Par changement d'échelle,

\[
 \big\{|y|^{-4-|\alpha|}\mathbf1_{\{|y|\ge L\}}\big\}
 \text{ a une norme }L^{3,1}
 \le C_\alpha L^{-3-|\alpha|}.                 \tag{32}
\]

L'inégalité de Hölder \(L^{3/2,\infty}\)-\(L^{3,1}\), appliquée à
(28), produit

\[
 \begin{aligned}
 |\partial^\alpha F_L(x)|
 &\le
 C_\alpha\|T_L\|_{L^{3/2,\infty}}
 \big\||y|^{-4-|\alpha|}
       \mathbf1_{\{|y|\ge L\}}\big\|_{L^{3,1}}\\
 &\le
 C_\alpha(1+C_Q^2)M^2L^{-3-|\alpha|}.
 \end{aligned}                                  \tag{33}
\]

Prendre le supremum sur \(x\in B_R\) démontre (2). Le facteur \(L^{-3}\)
est la puissance critique attendue pour une force issue d'un tenseur
faible-\(L^{3/2}\) situé à distance \(L\).

Cette preuve n'utilise aucune borne sur les dérivées de \(U\). Toutes les
dérivées de \(F_L\) tombent sur le noyau lisse séparé du support.

## 6. Quantificateurs temporels

Soit \(J\) un intervalle de temps renormalisé. Si

\[
 \operatorname*{ess\,sup}_{\sigma\in J}
 \|U(\sigma)\|_{L^{3,\infty}}\le M,             \tag{34}
\]

alors (2) vaut pour presque tout \(\sigma\in J\), avec une constante commune.
Pour une solution classique, elle vaut pour tout \(\sigma\in J\).
La même conclusion vaut pour une famille \(U_L(\sigma)\) dépendant de \(L\),
dès que le supremum de ses normes dans (34) reste borné par le même \(M\).

L'estimation est purement spatiale :

- elle ne donne pas de borne sur \(\partial_\sigma F_L\) ;
- elle ne donne aucune équicontinuité temporelle ;
- elle ne justifie pas le passage de
  \(U_n\otimes U_n\) à une limite ;
- elle reste indépendante de \(\kappa(\sigma)\), parce que \(K_L\) s'annule
  exactement dans le core.

Ici \(L\) est un paramètre spatial fixe. Si \(L=L(\sigma)\), la dérivée
\(\partial_\sigma Q_{L(\sigma)}\) crée un commutateur supplémentaire absent
de (18)--(19). Le lemme ne couvre pas cette situation.

## 7. Contre-profil : croissance globale \(L^2\)

La disparition locale ne donne pas
\(\|F_L\|_X\to0\). On le voit déjà sur un profil lisse explicite.

Supposons \(\chi\) radial et non constant dans \(A\). Choisissons
\(\phi\in C_c^\infty(A)\), axisymétrique, supportée hors de l'axe et dans une
zone où \(y\cdot\nabla\chi\ne0\), puis posons

\[
 V(r,\theta,z)=\phi(r,z)e_\theta.               \tag{35}
\]

Alors

\[
 \operatorname{div}V=0,\qquad
 \nabla\chi\cdot V=0,\qquad
 QV=\chi V.                                     \tag{36}
\]

Par suite,

\[
 A:=[D,Q]V=(y\cdot\nabla\chi)V\ne0.             \tag{37}
\]

Définissons

\[
 U_L=\mathcal D_LV=L^{-1}V(y/L).                \tag{38}
\]

La norme critique est constante :

\[
 \|U_L\|_{L^{3,\infty}}=\|V\|_{L^{3,\infty}}.  \tag{39}
\]

Soit \(P_V\) la pression de Riesz de \(V\),
\(H_V=\mathbb P\operatorname{div}(V\otimes V)\), et

\[
 B_0=
 \mathbb P\operatorname{div}(QV\otimes QV)
 -QH_V-[\Delta,Q]V.                             \tag{40}
\]

La conjugaison (13), l'invariance de \(\mathbb P\) par dilatation et les
ordres respectifs du laplacien et de \(D\) donnent l'identité globale

\[
 \boxed{
 F_L(y)
 =L^{-3}B_0(y/L)+\kappa L^{-1}A(y/L).}          \tag{41}
\]

Le premier terme a l'échelle critique d'une force. Le second n'a qu'une
puissance \(L^{-1}\) : le générateur de dilatation est invariant sous
l'agrandissement externe, tandis que l'espace \(X\) attend une amplitude
\(L^{-3}\).

### Minoration de la norme quotient

Pour

\[
 X=L^1(\mathbb R^3)
   +\operatorname{div}L^{3/2,\infty}(\mathbb R^3),              \tag{42}
\]

toute fonction test vectorielle \(\psi\) vérifie

\[
 |\langle F,\psi\rangle|
 \le \|F\|_X
 \max\left\{\|\psi\|_\infty,
       C_H\|\nabla\psi\|_{L^{3,1}}\right\}.     \tag{43}
\]

Prenons \(\psi=A\) et \(\psi_L(y)=A(y/L)\). Alors

\[
 \|\psi_L\|_\infty=\|A\|_\infty,\qquad
 \|\nabla\psi_L\|_{L^{3,1}}
 =\|\nabla A\|_{L^{3,1}},                       \tag{44}
\]

et (41) donne

\[
 \langle F_L,\psi_L\rangle
 =\kappa L^2\int_{\mathbb R^3}|A|^2
  +\langle B_0,A\rangle.                        \tag{45}
\]

Comme \(A\ne0\), (43)--(45) impliquent

\[
 \boxed{
 \|F_L\|_X\ge c_A|\kappa|L^2-C_{A,B_0}.}         \tag{46}
\]

Pour la branche Type I du cycle 0043, \(\kappa>0\) est une constante en
temps : la croissance est donc quadratique. Si \(\kappa=0\), ce
contre-profil précis ne croît pas ; les termes restants gardent l'échelle
critique et une borne globale uniforme est compatible avec (41).

Le profil (38) est un test cinématique à temps fixé. Il est lisse,
divergence-free et admissible comme donnée d'une solution locale forte, mais
il n'est pas revendiqué comme profil ancien ni comme solution stationnaire
de l'équation renormalisée. Il suffit à réfuter toute estimation spatiale
globale uniforme déduite uniquement de (39).

## 8. Passe contradictoire

1. **Projection supposée locale.** Faux globalement. L'identité delta de
   \(\mathbb P\) s'annule sur \(B_R\), mais la pression extérieure produit la
   queue (28).
2. **Support de la différence tensorielle.** \(T_L\) est nul dans \(B_L\),
   mais vaut \(-U\otimes U\) hors de \(B_{2L}\). Le remplacer par une source
   seulement annulaire est faux.
3. **Pression silencieuse.** La seule divergence nulle de \(H\) ne prouve pas
   \(H=\mathbb P\operatorname{div}(U\otimes U)\). La jauge de Riesz et (15)
   sont nécessaires.
4. **Convention tensorielle.** Avec la divergence sur le premier indice, les
   indices du noyau dans (27)--(28) changent. La convention (4) est utilisée
   partout.
5. **Delta du noyau.** \(\nabla^2\Gamma\) et ses dérivées sont des
   distributions avec parties locales. La formule classique (28) n'est
   licite que grâce à la séparation \(\operatorname{dist}(B_R,
   \operatorname{supp}T_L)\ge L/2\).
6. **Intégrabilité absolue.** Faible-\(L^{3/2}\) seul ne rend pas \(T_L\)
   intégrable, mais le noyau extérieur appartient à \(L^{3,1}\), ce qui
   ferme exactement le pairing.
7. **Uniformité de Bogovskii.** Elle vient de la conjugaison (9), pas du mot
   « solénoïdal ». Changer de réalisation avec \(L\) détruit potentiellement
   \(C_Q\).
8. **Dérivées de \(U\).** Aucune n'est cachée dans (33) ; différencier la
   formule globale avant d'éliminer le terme delta en introduirait
   artificiellement.
9. **Quantificateur temps.** Une borne essentielle en temps donne (2)
   presque partout, pas une convergence temporelle uniforme.
10. **Cutoff mobile.** Un \(L(\sigma)\) variable ajoute
    \(\partial_\sigma Q_L\). L'omettre serait une identité PDE fausse.
11. **Norme locale contre norme globale.** La convergence
    \(C^\infty_{\rm loc}\) de \(F_L\) vers zéro n'implique aucune convergence
    dans \(X\); (46) donne même une divergence.
12. **Cas \(\kappa=0\).** La croissance \(L^2\) n'existe pas dans le profil
    construit. Toute affirmation sans la condition \(\kappa\ne0\) est
    fausse.
13. **Signe du drift dans la PDE.** À partir de l'équation de base
    \(\partial_\sigma U-\Delta U+H+\kappa DU=0\), la force (19), qui contient
    \(+\kappa[D,Q_L]U\), correspond à une équation localisée dont le membre
    gauche contient \(+\kappa DZ_L\). Écrire \(-\kappa DZ_L\) tout en
    conservant (19) est incohérent.

## 9. Statut exact du lemme

| Assertion | Statut | Motif |
|---|---|---|
| identité (1) sur \(B_R\) | **PROUVÉ** | support de \(Q_L-I\), (17) et annulation de \(K_L\) |
| borne (2) pour la famille conjuguée (9) | **PROUVÉ** | noyau extérieur et Hölder de Lorentz |
| constante indépendante de \(R,L,\sigma\) | **PROUVÉ** sous (14) et (34) | séparation \(L\ge2R\), borne Type I uniforme |
| même borne pour une famille arbitraire de corrections solénoïdales | **NON DÉMONTRÉ / FAUX EN GÉNÉRAL** | aucune uniformité d'opérateur |
| \(F_L\) est supportée dans \(A_L\) | **FAUX** | queue globale de Leray |
| \(T_L\) est supporté dans \(A_L\) | **FAUX** | (26) |
| \(F_L\to0\) dans \(C^\infty(B_R)\) pour chaque \(R\) | **PROUVÉ** | (2) |
| \(F_L\to0\) dans \(X\) | **FAUX si \(\kappa\ne0\)** | contre-profil (35)--(46) |
| raccord à une solution ancienne non forcée | **NON DÉMONTRÉ** | absence de compacité globale et temporelle |

## 10. Conclusion falsifiable

L'agrandissement de la couronne expulse bien la force projetée de tout
compact spatial :

\[
 F_L\longrightarrow0
 \quad\text{dans }C^\infty_{\rm loc}(\mathbb R^3)
 \quad\text{à taux }L^{-3-|\alpha|}.            \tag{47}
\]

Ce résultat ne ferme pas
\`GAP-TYPE-I-FORCE-COMPACTNESS\`. Le contre-profil montre que le drift
renormalisé peut simultanément stocker un budget \(X\) de taille \(L^2\)
dans une couronne qui part à l'infini. Le prochain lemme utile doit donc
choisir explicitement entre :

- une topologie locale où la fuite à l'infini est acceptable et où les
  produits \(Z_L\otimes Z_L\) passent à la limite ;
- un contrôle global pondéré qui interdit le profil (38) ;
- ou une formulation de rigidité autorisant une perte de masse/force à
  l'infini.

Aucune de ces trois marches ne découle de la seule borne
\(\|U\|_{L^{3,\infty}}\le M\).
