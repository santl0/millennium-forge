# Cycle 0058 — division de Bochner à grande vitesse angulaire

Date : 2026-08-15.

Statut : `AI_INTERNAL_DERIVATION`; audit fonctionnel local, sans résultat
Clay. Le gain de symétrie est démontré; la stationnarité depuis un résidu
seulement borné est réfutée.

## Verdict

La régularité temporelle uniforme du ledger 0045 rend inutile toute borne de
variation de \(1/\beta_n\) pour obtenir

\[
 \mathcal RZ_n\longrightarrow0.                                           \tag{1}
\]

Le mécanisme est une division algébrique dans un espace de Bochner commun :

\[
 \beta_n\mathcal RZ_n=\partial_sZ_n-r_n.                                  \tag{2}
\]

Si, sur une fenêtre \(J\Subset I\),

\[
 b_{n,J}:=\operatorname*{ess\,inf}_{s\in J}|\beta_n(s)|\longrightarrow\infty,
                                                                            \tag{3}
\]

et si, pour un Banach \(X_R^*\),

\[
 \sup_n\|\partial_sZ_n\|_{L^q(J;X_R^*)}\leq C_{T,J,R},\qquad
 \sup_n\|r_n\|_{L^q(J;X_R^*)}\leq C_{r,J,R},                              \tag{4}
\]

alors

\[
 \boxed{
 \|\mathcal RZ_n\|_{L^q(J;X_R^*)}
 \leq\frac{C_{T,J,R}+C_{r,J,R}}{b_{n,J}}\longrightarrow0.}               \tag{5}
\]

Il suffit que \(\beta_n\) soit mesurable et non nulle presque partout pour
les grands \(n\). Ni \(\beta_n'\), ni
\(\operatorname{Var}(1/\beta_n)\), ni même
\(\beta_n\in W^{1,1}\) n'interviennent dans (5).

Pour le ledger brut du cycle 0045, le choix robuste est

\[
 X_R=W^{2,4}_0(B_R)^3,\qquad
 X_R^*=W^{-2,4/3}(B_R)^3,\qquad q=\infty                         \tag{6}
\]

pour \(\partial_sZ_n\); si \(r_n\) n'est borné que dans \(L^p_tX_R^*\), on
prend \(q=p\) et utilise la fenêtre finie. Après le ledger d'énergie, le choix
spatial plus fort

\[
 \widetilde X_R=W^{1,4}_0(B_R)^3,\qquad
 \widetilde X_R^*=W^{-1,4/3}(B_R)^3,\qquad q=2                  \tag{7}
\]

est également disponible.

En revanche, le prolongement

\[
 \mathcal RZ=0\quad\Longrightarrow\quad\partial_sZ=0                       \tag{8}
\]

est **faux** sous la seule bornitude de \(r_n\). La moyenne de Haar donne
seulement

\[
 \partial_s\mathcal AZ_n=\mathcal Ar_n,                                   \tag{9}
\]

et le membre droit n'a aucune raison de tendre vers zéro. Toute solution
renormalisée axisymétrique lisse non stationnaire, répétée comme
\(Z_n=Z\), avec \(\beta_n=n\), fournit un contre-exemple exact :
\(\mathcal RZ_n=0\), \(r_n=\partial_sZ\) est uniformément borné dans les
espaces du ledger, mais \(\partial_sZ\neq0\).

Le lemme corrigé conclut donc à l'invariance rotationnelle de la limite. Pour
conclure à la stationnarité, il faut ajouter
\(\mathcal Ar_n\to0\) dans les distributions — en particulier
\(r_n\to0\) suffit — ou imposer \(\mathcal Ar_n=0\) exactement.

## 1. Cadre local et action de rotation

Soit \(I\) un intervalle et soit \(Q_\gamma\) le groupe de rotations autour
d'un axe fixe passant par l'origine. Avec une matrice antisymétrique \(K\),

\[
 (Q_\gamma W)(y)=e^{\gamma K}W(e^{-\gamma K}y),\qquad
 \mathcal RW=KW-(Ky\cdot\nabla)W.                                        \tag{10}
\]

Pour les distributions,

\[
 \langle\mathcal RW,\varphi\rangle
 =\langle W,(Ky\cdot\nabla)\varphi-K\varphi\rangle.                       \tag{11}
\]

Sur une boule centrée \(B_R\), le coefficient \(Ky\) est borné et les
rotations préservent le domaine. Ainsi \(\mathcal R\) envoie continûment
\(L^2(B_R)\) dans \(H^{-1}(B_R)\), donc aussi dans les espaces plus négatifs
de (6)--(7).

Le résidu est

\[
 r_n=\partial_sZ_n-\beta_n\mathcal RZ_n.                                  \tag{12}
\]

L'axe, le centre et le coefficient du drift renormalisé sont fixes en \(n\)
et en temps. Un axe mobile ajouterait d'autres générateurs; une rotation
excentrée ne commuterait pas avec \(y\cdot\nabla\).

## 2. Premier espace : ledger brut sans dissipation

Fixons \(J\Subset I\), \(R<\infty\). Le ledger brut du cycle 0045 fournit,
sur une boule légèrement plus grande utilisée pour les coupures,

\[
 \sup_n\|Z_n\|_{L^\infty(J;L^2(B_{2R}))}<\infty,                           \tag{13}
\]

\[
 Z_n\otimes Z_n,\ \Pi_n
 \text{ bornés dans }L^\infty(J;L^{4/3}(B_{2R})),                         \tag{14}
\]

et l'équation renormalisée

\[
 \partial_sZ_n-\Delta Z_n
 +\operatorname{div}(Z_n\otimes Z_n)+\nabla\Pi_n
 +\kappa(1+y\cdot\nabla)Z_n=0.                                           \tag{15}
\]

Pour \(\varphi\in W^{2,4}_0(B_R)^3\),

\[
\begin{aligned}
 |\langle\Delta Z_n,\varphi\rangle|
 &\leq |B_R|^{1/4}\|Z_n\|_2\|\Delta\varphi\|_4,\\
 |\langle\operatorname{div}(Z_n\otimes Z_n),\varphi\rangle|
 &\leq\|Z_n\otimes Z_n\|_{4/3}\|\nabla\varphi\|_4,\\
 |\langle\nabla\Pi_n,\varphi\rangle|
 &\leq\|\Pi_n\|_{4/3}\|\nabla\varphi\|_4,\\
 |\langle(1+y\cdot\nabla)Z_n,\varphi\rangle|
 &\leq C_R\|Z_n\|_2\|\varphi\|_{W^{1,2}}.                              \tag{16}
\end{aligned}
\]

Dans la dernière ligne, on utilise

\[
 \langle(1+y\cdot\nabla)Z_n,\varphi\rangle
 =-\int Z_n\cdot(2\varphi+y\cdot\nabla\varphi).                           \tag{17}
\]

Les injections sur la boule finie transforment (16) en

\[
 \boxed{
 \sup_n\|\partial_sZ_n\|_{L^\infty(J;W^{-2,4/3}(B_R))}
 \leq C^{(2)}_{J,R}<\infty.}                                              \tag{18}
\]

La constante dépend de \(R\), \(\kappa\), de la borne faible-\(L^3\) et
des constantes uniformes de pression/coupure du ledger, mais pas de \(n\).

Si

\[
 \sup_n\|r_n\|_{L^p(J;W^{-2,4/3}(B_R))}\leq C^{(r)}_{J,R,p},            \tag{19}
\]

avec \(1\leq p<\infty\), alors (2)--(3) donnent

\[
 \boxed{
 \|\mathcal RZ_n\|_{L^p(J;W^{-2,4/3})}
 \leq\frac{|J|^{1/p}C^{(2)}_{J,R}+C^{(r)}_{J,R,p}}{b_{n,J}}.}             \tag{20}
\]

Pour \(p=\infty\), le facteur \(|J|^{1/p}\) vaut un. Cette estimation est
locale en \(J,R\); aucune constante uniforme lorsque \(R\to\infty\) ou
\(J\uparrow I\) n'est revendiquée.

## 3. Formulation solénoïdale

Si l'on ne veut pas transporter la pression, posons

\[
 X_{R,\sigma}
 =\overline{C_{c,\sigma}^\infty(B_R)^3}^{W^{2,4}},\qquad
 X_{R,\sigma}^*=(X_{R,\sigma})^*.                                        \tag{21}
\]

L'équation (15) testée sur \(X_{R,\sigma}\) élimine \(\nabla\Pi_n\). Les
trois autres estimations de (16) donnent

\[
 \sup_n\|\partial_sZ_n\|_{L^\infty(J;X_{R,\sigma}^*)}
 \leq C^{(2,\sigma)}_{J,R}.                                               \tag{22}
\]

Si \(r_n\) est borné dans \(L^p(J;X_{R,\sigma}^*)\), la même estimation
(20) vaut avec ces espaces. Cette formulation est la plus conservatrice
lorsque les pressions ne sont connues que localement modulo une composante
harmonique.

La conclusion \(\mathcal RZ_n\to0\) dans le dual solénoïdal identifie a
priori seulement la partie de \(\mathcal RZ_n\) vue par les tests
solénoïdaux. Toutefois \(\mathcal RZ_n\) est lui-même divergence-free, car
les rotations préservent la divergence. Sur une boule, un champ
divergence-free qui s'annule contre tous les tests solénoïdaux peut encore
être représenté localement par un gradient harmonique; pour conclure
\(\mathcal RZ=0\) sans cette ambiguïté, on utilise soit le dual vectoriel
complet de (6), soit la convergence distributionnelle globale et la classe
spatiale qui exclut les parasites de gradient. Le choix complet (6) est donc
préférable lorsque (14) est disponible.

## 4. Second espace : ledger après énergie

Le ledger complet fournit en plus

\[
 \sup_n\|\nabla Z_n\|_{L^2(J\times B_{2R})}
 \leq C_{\nabla,J,R}.                                                     \tag{23}
\]

Pour \(\varphi\in W^{1,4}_0(B_R)^3\),

\[
 |\langle\Delta Z_n,\varphi\rangle|
 =\left|\int\nabla Z_n:\nabla\varphi\right|
 \leq |B_R|^{1/4}\|\nabla Z_n\|_2\|\nabla\varphi\|_4.                  \tag{24}
\]

Les autres termes de (16) sont bornés dans
\(L^\infty_tW^{-1,4/3}_x\). Par conséquent,

\[
 \boxed{
 \sup_n\|\partial_sZ_n\|_{L^2(J;W^{-1,4/3}(B_R))}
 \leq C^{(1)}_{J,R}<\infty.}                                              \tag{25}
\]

Si \(r_n\) est borné dans \(L^p(J;W^{-1,4/3})\), posons

\[
 q=\min\{2,p\}.                                                           \tag{26}
\]

Les injections de Lebesgue sur la fenêtre finie donnent la constante exacte

\[
\boxed{
 \|\mathcal RZ_n\|_{L^q(J;W^{-1,4/3})}
 \leq\frac{
 |J|^{1/q-1/2}C^{(1)}_{J,R}
 +|J|^{1/q-1/p}C^{(r)}_{J,R,p}}
 {b_{n,J}}.}                                                              \tag{27}
\]

Pour \(p=\infty\), on interprète \(1/p=0\). Le choix \(p=2\) donne la
forme la plus simple, avec numérateur
\(C^{(1)}_{J,R}+C^{(r)}_{J,R,2}\).

La version solénoïdale de (7) se définit en fermant les tests solénoïdaux
dans \(W^{1,4}_0\); elle retire de nouveau le terme de pression.

## 5. Pourquoi aucune variation inverse n'apparaît

Pour les grands \(n\), (3) permet de choisir un représentant mesurable de
\(1/\beta_n\), arbitraire sur l'ensemble nul des zéros éventuels, avec

\[
 \|1/\beta_n\|_{L^\infty(J)}\leq b_{n,J}^{-1}.                             \tag{28}
\]

L'égalité (2) a lieu dans le même espace de Bochner que ses deux membres de
droite. La multiplication par le scalaire \(1/\beta_n(s)\) est un opérateur
borné sur \(L^q(J;X_R^*)\), de norme au plus \(b_{n,J}^{-1}\). Il n'y a
aucune intégration par parties temporelle et donc aucun terme
\((1/\beta_n)'\).

C'est la différence exacte avec le cycle 0057. Là, on ne postulait pas que
\(r_n\) et \(\partial_sZ_n\) vivaient uniformément dans un même espace de
Bochner assez fort; la division était réalisée contre un test temporel et
créait une dérivée de l'inverse. Ici, le ledger de Bochner ferme directement
la division.

## 6. Passage à l'invariance rotationnelle

Supposons, comme dans le ledger compact du cycle 0045,

\[
 Z_n\to Z\quad\text{fortement dans }L^3_{\rm loc}.                         \tag{29}
\]

Alors

\(\mathcal RZ_n\to\mathcal RZ\) dans les distributions, car
\(\mathcal R\) se déplace sur le test selon (11). Les estimations (20) ou
(27) donnent simultanément

\[
 \mathcal RZ_n\to0\quad\text{dans }\mathcal D'.                           \tag{30}
\]

Par unicité de la limite distributionnelle,

\[
 \boxed{\mathcal RZ=0.}                                                    \tag{31}
\]

Ainsi \(Q_\gamma Z=Z\) pour tout angle et

\[
 \mathcal AZ=Z,\qquad
 \mathcal A=\frac1{2\pi}\int_0^{2\pi}Q_\gamma\,d\gamma.                \tag{32}
\]

Ce résultat est une symétrie spatiale à presque tout temps, pas une
stationnarité.

## 7. Réfutation de la stationnarité par Haar

La moyenne vérifie exactement

\[
 \mathcal A\mathcal R=0.                                                  \tag{33}
\]

En appliquant \(\mathcal A\) à (12),

\[
 \boxed{\partial_s\mathcal AZ_n=\mathcal Ar_n.}                            \tag{34}
\]

La bornitude de \(r_n\) donne seulement une borne de
\(\partial_s\mathcal AZ_n\). Après extraction, on peut obtenir

\[
 \partial_s\mathcal AZ=g                                                   \tag{35}
\]

pour une limite faible \(g\) de \(\mathcal Ar_n\), mais rien n'impose
\(g=0\). Comme \(\mathcal AZ=Z\), (35) autorise toute évolution
axisymétrique compatible avec Navier--Stokes.

### Contre-exemple PDE exact

Choisissons une donnée initiale lisse, décroissante, divergence-free,
axisymétrique et ne satisfaisant pas l'équation stationnaire de profil. La
théorie locale forte fournit, sur un intervalle compact assez court, une
solution lisse non stationnaire de l'équation renormalisée. L'unicité forte
préserve l'axisymétrie. Notons-la \(Z\) et posons

\[
 Z_n=Z,\qquad \beta_n=n.                                                   \tag{36}
\]

Alors

\[
 b_{n,J}=n\to\infty,\qquad
 \mathcal RZ_n=0,\qquad
 r_n=\partial_sZ.                                                          \tag{37}
\]

Le résidu est uniformément borné dans tous les espaces locaux de Bochner du
ledger, et même \(\operatorname{Var}(1/\beta_n)=0\). Pourtant

\[
 \partial_sZ\neq0.                                                        \tag{38}
\]

Ce contre-exemple est une vraie solution Navier--Stokes renormalisée locale,
pas seulement une courbe abstraite. Il réfute toute inférence
« grande vitesse + résidu borné + autonomie \(\Rightarrow\) stationnarité ».
L'autonomie n'interdit évidemment pas les solutions axisymétriques
dépendantes du temps.

## 8. Hypothèse minimale restaurant la stationnarité

L'équation (34) montre que la condition exacte est

\[
 \mathcal Ar_n\longrightarrow0
 \quad\text{dans }\mathcal D'(I\times\mathbb R^3).                         \tag{39}
\]

Sous (29), (32), (34) et (39),

\[
 \partial_sZ=\partial_s\mathcal AZ=0.                                     \tag{40}
\]

Chacune des hypothèses suivantes suffit à (39) :

- \(r_n\to0\) dans un espace de distributions ou de Bochner local;
- \(\mathcal Ar_n=0\) exactement pour tout \(n\);
- \(\mathcal Ar_n\rightharpoonup0\) dans le dual Bochner considéré.

La petitesse de la seule composante non axisymétrique
\((I-\mathcal A)r_n\) ne suffit pas; elle laisse précisément intact le terme
qui pilote \(\partial_s\mathcal AZ_n\).

## 9. Quantificateurs et compatibilité des espaces

Le lemme corrigé doit être lu dans l'ordre suivant :

1. fixer \(J\Subset I\) et \(R<\infty\);
2. choisir un espace \(X_R^*\) dans lequel **les deux** suites
   \(\partial_sZ_n\) et \(r_n\) sont uniformément bornées;
3. choisir un exposant temporel commun, ou abaisser les deux exposants à
   \(q\) sur la fenêtre finie;
4. seulement ensuite diviser (2) par \(\beta_n\) et utiliser \(b_{n,J}\);
5. répéter sur une exhaustion dénombrable des fenêtres et boules pour obtenir
   (31) globalement.

Dire seulement « \(r_n\) est borné dans un espace de Bochner \(X^*\) » est
sous-spécifié. Si le ledger ne borne pas \(\partial_sZ_n\) dans le même
espace, ou si les deux espaces n'ont pas de plongement dans un dual commun,
l'addition de (2) n'a pas de sens normé exploitable. Les choix (6)--(7)
réparent précisément cette lacune.

La borne (3) est essentielle sur chaque fenêtre. Une vitesse grande seulement
en moyenne, ou une suite possédant de petites zones temporelles où
\(\beta_n=0\), ne permet pas la division \(L^q\) sans estimer séparément ces
zones.

## 10. Pression, stress et suitability

Le ledger 0045 donne la forte convergence (29), donc

\[
 Z_n\otimes Z_n\to Z\otimes Z
 \quad\text{fortement dans }L^{3/2}_{\rm loc}.                            \tag{41}
\]

La limite satisfait l'équation renormalisée contre les tests solénoïdaux,
sans défaut de Reynolds. Dans la jauge globale de Riesz et sous la borne
uniforme faible-\(L^3\), la décomposition proche/harmonique ou la dualité
Lorentz avec contrôle de queue identifie aussi

\[
 \Pi=R_iR_j(Z_iZ_j).                                                       \tag{42}
\]

Les bornes uniformes

\[
 Z_n\text{ dans }L^\infty_tL^2_{x,\rm loc}\cap L^2_tH^1_{x,\rm loc},\qquad
 \Pi_n\text{ dans }L^{3/2}_{t,x,\rm loc}                                  \tag{43}
\]

et l'inégalité locale d'énergie passent comme au cycle 0045 : vitesse forte,
gradient faible, pression proche forte/harmonique faible et dissipation
semi-continue. La limite \(Z\) est donc suitable sous ce ledger complet.

La conclusion (31) rend \(Z\) axisymétrique, mais pas stationnaire. Il
n'existe alors aucun profil spatial fixe \(U\) auquel appliquer directement
Guevara--Phuc.

Si l'hypothèse supplémentaire (39) fournit (40), on obtient un profil

\[
 U\in W^{1,2}_{\rm loc}(\mathbb R^3)
 \cap L^{3,\infty}(\mathbb R^3)                                           \tag{44}
\]

résolvant l'équation stationnaire de Leray avec \(\kappa>0\). Le théorème
1.3 publié de Guevara--Phuc impose alors \(U=0\).

## 11. Capture

Une capture cylindrique uniforme passe par (29). Si

\[
 \int_J\int_{B_1}|Z_n|^3\geq c_*>0,                                      \tag{45}
\]

alors

\[
 \int_J\int_{B_1}|Z|^3\geq c_*.                                          \tag{46}
\]

Cela prouve que la limite axisymétrique dépendante du temps est non triviale,
mais ne la rend pas stationnaire. Sous (39)--(40), (46) devient

\[
 |J|\|U\|_{L^3(B_1)}^3\geq c_*,                                          \tag{47}
\]

en contradiction avec la rigidité de Guevara--Phuc lorsque (44) est
disponible. Une capture à une seule trace ne passe pas par la seule forte
convergence espace-temps.

## 12. Passe contradictoire

1. **Variation inverse.** Elle est absente parce qu'aucune intégration par
   parties temporelle n'est effectuée. Introduire
   \((1/\beta_n)'\) dans (5) serait une perte artificielle.
2. **Zéros de \(\beta_n\).** L'infimum essentiel (3) suffit; une régularité
   AC de \(\beta_n\) n'est pas nécessaire. Les valeurs sur un ensemble nul
   n'affectent pas la multiplication de Bochner.
3. **Espaces différents.** Une borne de \(r_n\) dans un dual non comparable à
   celui de \(\partial_sZ_n\) ne ferme pas (2). Il faut un espace ambiant
   commun.
4. **Endpoint Lorentz.** Faible-\(L^{3/2}\) ne s'apparie pas à tout
   \(L^3\). Le passage local par \(L^{4/3}\) et des tests
   \(W^{1,4}\) ou \(W^{2,4}\) évite cet endpoint.
5. **Diffusion.** Sans énergie, elle est placée dans
   \(W^{-2,4/3}\) en déplaçant deux dérivées sur le test. Avec dissipation,
   une seule dérivée suffit et donne (25).
6. **Pression complète.** Le dual vectoriel complet requiert une borne de
   pression locale uniforme. La version solénoïdale l'élimine, mais doit
   exclure l'ambiguïté gradient pour conclure sur tout \(\mathcal RZ\).
7. **Temps.** Les facteurs de \(|J|\) dans (20), (27) sont indispensables
   lorsqu'on abaisse un exposant temporel. Il n'y a aucune uniformité sur un
   intervalle ancien infini.
8. **Rayon.** Toutes les constantes dépendent de \(R\); une diagonale locale
   ne donne pas de borne uniforme au domaine infini.
9. **Haar.** \(\mathcal A\mathcal R=0\) tue la partie rotationnelle, mais
   laisse \(\mathcal Ar_n\). Borné n'est pas petit.
10. **Autonomie.** Une équation autonome possède des trajectoires
    axisymétriques non stationnaires. Elle ne ferme pas (8).
11. **Capture.** Une masse persistante ne supprime pas la dépendance en temps
    d'une solution axisymétrique.
12. **Guevara--Phuc.** Leur théorème porte sur un profil stationnaire; il ne
    s'applique pas après la seule conclusion (31).
13. **Portée Clay.** Ni la grande vitesse uniforme (3), ni la borne de résidu
    dans le bon dual, ni la petitesse moyenne (39) ne découlent d'un blow-up
    Clay général.

## 13. Statut logique

| Implication | Statut |
|---|---|
| ledger brut \(\Rightarrow\partial_sZ_n\) borné dans \(L^\infty W^{-2,4/3}\) | **PROUVÉ**, cycle 0045 redérivé par (16)--(18) |
| ledger d'énergie \(\Rightarrow\partial_sZ_n\) borné dans \(L^2W^{-1,4/3}\) | **PROUVÉ** par (23)--(25) |
| borne commune de \(\partial_sZ_n,r_n\) + (3) \(\Rightarrow\mathcal RZ_n\to0\) | **PROUVÉ** avec constantes (20), (27) |
| conclusion précédente sans \(\operatorname{Var}(1/\beta_n)\) | **PROUVÉ**; aucune dérivée de \(\beta_n\) requise |
| compacité locale \(\Rightarrow\mathcal RZ=0\) | **PROUVÉ** |
| \(\mathcal RZ=0\) + autonomie NS \(\Rightarrow\partial_sZ=0\) | **RÉFUTÉ** par (36)--(38) |
| \(\mathcal Ar_n\to0\Rightarrow\partial_sZ=0\) | **PROUVÉ** |
| ledger complet \(\Rightarrow\) limite suitable et pression (42) | **PROUVÉ conditionnellement aux bornes uniformes du cycle 0045** |
| stationnarité supplémentaire + (44) \(\Rightarrow U=0\) | **SOURCE_VERIFIED**, Guevara--Phuc |
| division de Bochner \(\Rightarrow\) résolution Clay | **NON DÉMONTRÉ** |

**Décision analytique : RÉVISER.** Conserver la division de Bochner comme un
lemme propre et plus fort que la méthode de variation inverse pour obtenir la
symétrie. Abandonner l'inférence de stationnarité depuis un résidu seulement
borné. La prochaine condition discriminante doit porter exactement sur la
composante moyenne \(\mathcal Ar_n\), car c'est elle qui gouverne l'évolution
sur le sous-espace invariant.
