# Cycle 0057 — limite à rotation rapide et projection axisymétrique

Date : 2026-08-15.

Statut : `AI_INTERNAL_DERIVATION`; lemme de moyennisation distributionnelle,
sans résultat Clay. Le raccord final à Guevara--Phuc est conditionnel au
ledger uniforme de suitability et de faible-\(L^3\).

## Verdict

Le lemme de rotation rapide est **vrai** sous les quantificateurs locaux
exacts ci-dessous. Soit \(I\subset\mathbb R\) un intervalle, soit
\(Q_\gamma\) un sous-groupe de rotations autour d'un axe fixe passant par
l'origine, \(\mathcal R\) son générateur et

\[
 \mathcal AW=\frac1{2\pi}\int_0^{2\pi}Q_\gamma W\,d\gamma                 \tag{1}
\]

la moyenne de Haar. Supposons

\[
 Z_n\to Z\quad\text{fortement dans }L^3_{\rm loc}(I\times\mathbb R^3),    \tag{2}
\]

et, pour tout \(J\Subset I\), \(R<\infty\),

\[
 C_{J,R}:=\sup_n
 \|Z_n\|_{L^\infty(J;L^2(B_R))}<\infty.                                  \tag{3}
\]

Soient \(\beta_n\in W^{1,1}_{\rm loc}(I)\) et

\[
 b_{n,J}:=\operatorname*{ess\,inf}_{s\in J}|\beta_n(s)|\longrightarrow\infty,
                                                                            \tag{4}
\]

\[
 \left\|\left(\frac1{\beta_n}\right)'\right\|_{L^1(J)}\longrightarrow0. \tag{5}
\]

Enfin, supposons

\[
 r_n:=\partial_sZ_n-\beta_n\mathcal RZ_n
 \longrightarrow0
 \quad\text{dans }L^1(J;H^{-1}(B_R))                                     \tag{6}
\]

sur toute fenêtre et toute boule, au sens des restrictions compatibles. Alors

\[
 \boxed{\mathcal RZ=0}                                                     \tag{7}
\]

dans \(\mathcal D'(I\times\mathbb R^3)\). Par ailleurs,

\[
 \boxed{\partial_s\mathcal AZ=0.}                                         \tag{8}
\]

Comme (7) implique \(\mathcal AZ=Z\), on obtient

\[
 \boxed{\partial_sZ=0.}                                                    \tag{9}
\]

La limite est donc un profil spatial fixe, invariant sous tout le sous-groupe
de rotations choisi. Aucun choix d'une suite d'instants ni aucune convergence
de \(\beta_n\) n'est nécessaire.

Les hypothèses (3) et (5) ont un rôle irréductible dans la preuve. La forte
\(L^3_{t,x}\) seule ne contrôle pas le terme où la mesure temporelle
\((1/\beta_n)'ds\) peut se concentrer. La formulation abrégée « suitable » ne
remplace pas non plus les bornes uniformes nécessaires au passage de
l'inégalité locale d'énergie.

## 1. Action de rotation et moyenne de Haar

Fixons une matrice antisymétrique \(K\), avec
\(R_\gamma=e^{\gamma K}\), et adoptons la convention

\[
 (Q_\gamma W)(y)=R_\gamma W(R_{-\gamma}y),qquad
 \mathcal RW=KW-(Ky\cdot\nabla)W.                                        \tag{10}
\]

Pour les distributions,

\[
 \langle\mathcal RW,\varphi\rangle
 =\langle W,\mathcal R^*\varphi\rangle,qquad
 \mathcal R^*\varphi=(Ky\cdot\nabla)\varphi-K\varphi.                   \tag{11}
\]

Le signe négatif du transport dans (10) vient de la variable
\(R_{-\gamma}y\). Changer la convention de l'action change simultanément le
signe de \(\mathcal R\) et de \(\beta_n\), mais pas les conclusions
(7)--(9).

La moyenne (1) est bien définie sur \(L^p_{\rm loc}\), les Sobolev locaux et
les distributions. Sur chaque boule centrée \(B_R\), les rotations sont des
isométries, donc

\[
 \|\mathcal AW\|_{L^p(B_R)}\leq\|W\|_{L^p(B_R)},qquad
 \|\mathcal AW\|_{H^{-1}(B_R)}\leq\|W\|_{H^{-1}(B_R)}.                   \tag{12}
\]

La seconde inégalité utilise l'action duale isométrique sur
\(H^1_0(B_R)\). La rotation doit être centrée à l'origine; sinon \(B_R\)
n'est pas préservée et, pour Navier--Stokes renormalisé, le drift
\(y\cdot\nabla\) n'est plus équivariant.

Enfin,

\[
 \boxed{\mathcal A\mathcal R=0,qquad
 \mathcal R\mathcal A=0.}                                                \tag{13}
\]

En effet,

\[
 \mathcal A\mathcal RW
 =\frac1{2\pi}\int_0^{2\pi}
 \frac d{d\gamma}Q_\gamma W\,d\gamma=0                                 \tag{14}
\]

par périodicité; l'autre identité suit de l'invariance de \(\mathcal AW\).

## 2. Absence de zéros et inverse \(W^{1,1}\)

Fixons désormais \(J\Subset I\). Une fonction de
\(W^{1,1}(J)\) possède un représentant absolument continu, donc continu. Dès
que \(b_{n,J}>0\), ce représentant ne s'annule pas sur \(J\). En effet, une
valeur nulle ou une valeur de module strictement inférieur à \(b_{n,J}\)
créerait, par continuité, un ensemble de mesure positive contredisant
l'infimum essentiel.

Sur chaque composante connexe de \(J\), \(\beta_n\) a donc un signe fixe et

\[
 \frac1{\beta_n}\in W^{1,1}(J),qquad
 \left(\frac1{\beta_n}\right)'
 =-\frac{\beta_n'}{\beta_n^2}\quad\text{p.p.}                            \tag{15}
\]

De plus,

\[
 \left\|\frac1{\beta_n}\right\|_{L^\infty(J)}\leq b_{n,J}^{-1}.        \tag{16}
\]

Les hypothèses (4)--(5) doivent être lues « pour chaque fenêtre \(J\Subset
I\), lorsque \(n\to\infty\) ». Les premiers indices pour lesquels
\(\beta_n\) pourrait s'annuler sont sans effet; on travaille à partir de
l'indice où \(b_{n,J}>0\).

## 3. Test divisé par \(\beta_n\)

Prenons

\[
 \eta\in C_c^\infty(J),qquad
 \varphi\in C_c^\infty(B_R)^3.                                           \tag{17}
\]

Posons

\[
 z_{n,\varphi}(s)=\langle Z_n(s),\varphi\rangle,qquad
 h_{n,\varphi}(s)=\langle\mathcal RZ_n(s),\varphi\rangle.                 \tag{18}
\]

Par (3), (11) et (6), ces fonctions vérifient sur \(J\)

\[
 z_{n,\varphi}'
 =\beta_nh_{n,\varphi}+\langle r_n,\varphi\rangle                         \tag{19}
\]

au sens des distributions, et le membre droit appartient à \(L^1(J)\) pour
chaque \(n\). En particulier \(z_{n,\varphi}\in W^{1,1}(J)\).

La fonction \(\eta/\beta_n\) appartient à \(W^{1,1}_0(J)\). On peut donc
l'utiliser dans l'intégration par parties scalaire de (19), sans prétendre
qu'une distribution temporelle arbitraire accepte un test non lisse. On
obtient exactement

\[
\begin{aligned}
 \int_J\eta\,h_{n,\varphi}\,ds
 ={}&-\int_J\frac{\eta'}{\beta_n}z_{n,\varphi}\,ds\\
 &-\int_J\eta
 \left(\frac1{\beta_n}\right)'z_{n,\varphi}\,ds\\
 &-\int_J\frac{\eta}{\beta_n}
 \langle r_n,\varphi\rangle\,ds.                                        \tag{20}
\end{aligned}
\]

Les trois signes négatifs proviennent respectivement de l'intégration par
parties et du signe \(-r_n/\beta_n\) dans
\(\mathcal RZ_n=\beta_n^{-1}\partial_sZ_n-\beta_n^{-1}r_n\).

## 4. Constantes exactes et passage à zéro

La borne (3) donne

\[
 |z_{n,\varphi}(s)|\leq C_{J,R}\|\varphi\|_{L^2(B_R)}                   \tag{21}
\]

pour presque tout \(s\). Les équations (16), (20)--(21) donnent

\[
\boxed{
\begin{aligned}
 \left|\int_J\eta
 \langle\mathcal RZ_n,\varphi\rangle\,ds\right|
 \leq{}&C_{J,R}\|\varphi\|_2
 \left[b_{n,J}^{-1}\|\eta'\|_{L^1(J)}
 +\|\eta\|_\infty
 \left\|\left(\frac1{\beta_n}\right)'\right\|_{L^1(J)}\right]\\
 &+b_{n,J}^{-1}\|\eta\|_\infty
 \|r_n\|_{L^1(J;H^{-1}(B_R))}
 \|\varphi\|_{H^1_0(B_R)}.
\end{aligned}}                                                            \tag{22}
\]

Chaque constante est indépendante de \(n\). Le premier terme tend vers zéro
par (4), le second par (5), et le troisième par (4) et (6). Pour ce dernier,
la convergence de \(r_n\) donne en particulier sa bornitude; la seule
bornitude aurait déjà suffi après multiplication par \(b_{n,J}^{-1}\).

Par (2) et (11),

\[
 \int_J\eta\langle\mathcal RZ_n,\varphi\rangle\,ds
 \longrightarrow
 \int_J\eta\langle\mathcal RZ,\varphi\rangle\,ds.                        \tag{23}
\]

En combinant (22)--(23), ce dernier appariement est nul. Les sommes finies de
tests séparables \(\eta(s)\varphi(y)\) sont denses dans l'espace des tests
espace-temps; une exhaustion dénombrable de \(I\times\mathbb R^3\) donne
(7) sans ensemble exceptionnel dépendant du test.

La forte convergence \(L^3_{\rm loc}\) est plus forte que nécessaire pour
(23) : une forte \(L^1_{\rm loc}\) suffirait. En revanche, elle ne remplace
pas la borne temporelle (3) dans le terme contenant la mesure
\((1/\beta_n)'ds\).

## 5. Stationnarité de la moyenne

Appliquons \(\mathcal A\) à la définition de \(r_n\). Par (13),

\[
 \mathcal Ar_n
 =\partial_s\mathcal AZ_n-\beta_n\mathcal A\mathcal RZ_n
 =\partial_s\mathcal AZ_n.                                                \tag{24}
\]

La contraction (12) et (6) donnent

\[
 \mathcal Ar_n\longrightarrow0
 \quad\text{dans }L^1(J;H^{-1}(B_R)).                                    \tag{25}
\]

Par convexité et invariance des boules centrées,

\[
 \mathcal AZ_n\longrightarrow\mathcal AZ
 \quad\text{fortement dans }L^3(J\times B_R).                            \tag{26}
\]

Le passage à la limite dans (24) donne (8) dans les distributions.

## 6. De \(\mathcal RZ=0\) à \(\mathcal AZ=Z\)

Pour chaque angle \(\gamma\),

\[
 \frac d{d\gamma}Q_\gamma Z=Q_\gamma\mathcal RZ=0                       \tag{27}
\]

dans \(\mathcal D'(I\times\mathbb R^3)\). L'orbite angulaire est donc
constante :

\[
 Q_\gamma Z=Z\quad\text{pour tout }\gamma.                              \tag{28}
\]

En moyennant (28),

\[
 \mathcal AZ=Z.                                                           \tag{29}
\]

Les équations (8) et (29) donnent alors (9). Ainsi il existe une distribution
spatiale \(U\) telle que

\[
 Z(s,y)=U(y)                                                              \tag{30}
\]

pour presque tout \(s\), sans utiliser de trace temporelle. Le profil est
invariant sous le sous-groupe de rotations, donc axisymétrique au sens
vectoriel correspondant à l'action (10).

## 7. Bord des fenêtres et ensembles exceptionnels

Le support de \(\eta\) est strictement contenu dans \(J\), donc
\(\eta/\beta_n\in W^{1,1}_0(J)\) et aucun terme de bord n'apparaît dans
(20). Il n'est pas nécessaire de contrôler les valeurs de \(Z_n\) aux
extrémités de \(J\).

Les identités (15), (19) et les dérivées temporelles valent presque partout
pour les représentants AC. Les conclusions (7)--(9) sont formulées dans les
distributions et ne dépendent pas de ces représentants. Pour obtenir des
énoncés simultanés presque partout, on choisit une famille dénombrable dense
de tests dans chaque boule et une exhaustion dénombrable des fenêtres.

Si \(I\) n'est pas connexe, la preuve vaut sur chaque composante. La
stationnarité distributionnelle reste globale sur chacune d'elles; aucune
égalité entre profils de composantes différentes n'est fournie.

## 8. Passage de l'équation Navier--Stokes

Supposons maintenant que les \(Z_n\) soient des solutions distributionnelles
de l'équation renormalisée autonome

\[
 \partial_sZ_n-\Delta Z_n
 +\operatorname{div}(Z_n\otimes Z_n)+\nabla\Pi_n
 +\kappa(1+y\cdot\nabla)Z_n=0,
 \qquad\operatorname{div}Z_n=0,                                          \tag{31}
\]

avec \(\kappa>0\) fixe. Contre les tests solénoïdaux compacts, la pression
disparaît. La convergence (2) implique

\[
 Z_n\otimes Z_n\to Z\otimes Z
 \quad\text{fortement dans }L^{3/2}_{\rm loc},                            \tag{32}
\]

et tous les termes linéaires passent dans les distributions. La limite
stationnaire \(U\) satisfait donc

\[
 -\Delta U+\mathbb P\operatorname{div}(U\otimes U)
 +\kappa(1+y\cdot\nabla)U=0                                              \tag{33}
\]

dans la formulation solénoïdale locale. Aucun défaut de Reynolds ne reste.

Pour identifier une pression globale, il faut une hypothèse supplémentaire,
par exemple

\[
 \sup_n\|Z_n\|_{L^\infty(I;L^{3,\infty}(\mathbb R^3))}\leq M,qquad
 \Pi_n=R_iR_j((Z_n)_i(Z_n)_j).                                           \tag{34}
\]

Alors les stress sont uniformément bornés dans
\(L^{3/2,\infty}\). La forte convergence locale (32), la dualité
\(L^{3/2,\infty}\)--\(L^{3,1}\) et la petitesse des queues des Riesz
appliquées à un test compact donnent

\[
 \Pi_n\to P_U=R_iR_j(U_iU_j)\quad\text{dans }\mathcal D'.               \tag{35}
\]

Sans (34), une composante harmonique locale de pression peut subsister. Cela
ne bloque pas l'équation solénoïdale (33), mais interdit de revendiquer la
jauge de Riesz.

## 9. Suitability et \(W^{1,2}_{\rm loc}\)

La borne (3) ne contrôle pas la dissipation. Même si chaque \(Z_n\) est
suitable, le passage de suitability exige des constantes uniformes. Une
hypothèse suffisante est, pour tous \(J\Subset I\) et \(R<\infty\),

\[
 \sup_n\left[
 \|Z_n\|_{L^\infty(J;L^2(B_R))}
 +\|\nabla Z_n\|_{L^2(J\times B_R)}
 +\|\Pi_n\|_{L^{3/2}(J\times B_R)}\right]<\infty,                         \tag{36}
\]

avec une normalisation de pression compatible. Le ledger proche/harmonique
du cycle 0045 est une variante suffisante.

Sous (36), les gradients convergent faiblement localement, les flux cubiques
passent par (2), le flux de pression passe par (35) ou la décomposition
locale, et la dissipation par semi-continuité inférieure. La limite \(Z=U\)
est alors suitable et

\[
 U\in W^{1,2}_{\rm loc}(\mathbb R^3).                                     \tag{37}
\]

Sans la borne de gradient dans (36), ni (37), ni l'inégalité locale d'énergie
de la limite ne sont démontrées. La convergence forte \(L^3\) ne contrôle pas
les hautes fréquences des gradients.

Dans le cadre des cycles 0045--0053, la borne globale faible-\(L^3\), la
pression de Riesz et la Caccioppoli uniforme peuvent précisément produire le
ledger (36). Ce raccord doit être cité, non remplacé par la suitability
individuelle.

## 10. Capture et non-trivialité

Une capture espace-temps uniforme passe par la forte convergence. Si, pour
un \(J\Subset I\) de longueur positive,

\[
 \int_J\int_{B_1}|Z_n|^3\,dy\,ds\geq c_*>0,                              \tag{38}
\]

alors

\[
 |J|\|U\|_{L^3(B_1)}^3
 =\int_J\int_{B_1}|Z|^3\,dy\,ds\geq c_*.                                 \tag{39}
\]

Ainsi \(U\neq0\). Une capture seulement sur une tranche terminale n'est pas
stable sous (2). La boule doit être centrée sur l'axe/origine fixé si l'on
veut utiliser directement l'invariance de la rotation; dans la conclusion
stationnaire (30), ce dernier point devient sans effet, mais il est nécessaire
dans les étapes moyennées antérieures.

## 11. Rigidité de Guevara--Phuc

Sous (34), (36), le profil stationnaire satisfait

\[
 U\in W^{1,2}_{\rm loc}(\mathbb R^3)
 \cap L^{3,\infty}(\mathbb R^3)                                          \tag{40}
\]

et l'équation stationnaire de Leray (33), avec coefficient \(\kappa>0\).
Après la dilatation critique qui normalise \(\kappa\) à \(1/2\), le théorème
1.3 publié de Guevara--Phuc, *SIAM J. Math. Anal.* 50 (2018), 541--556, DOI
`10.1137/16M110099X`, s'applique avec \(q=3\) et donne

\[
 U=0.                                                                     \tag{41}
\]

Si la capture (39) est également disponible, (39) et (41) se contredisent.
La conclusion scientifique conditionnelle est donc l'exclusion d'une suite
à rotation arbitrairement rapide satisfaisant simultanément : défaut tangent
(6), faible variation inverse (5), compacité forte, ledger suitable uniforme,
faible-\(L^3\) global et capture persistante.

Sans (34)--(36), Guevara--Phuc ne peut pas être invoqué : (33) est bien une
équation distributionnelle solénoïdale, mais les classes
\(W^{1,2}_{\rm loc}\) et \(L^{3,\infty}\) du profil ne sont pas toutes deux
acquises.

## 12. Passe contradictoire

1. **Signe.** Avec (10), le résidu est
   \(\partial_sZ_n-\beta_n\mathcal RZ_n\). La division donne trois termes
   négatifs dans (20). L'autre convention de rotation inverse simultanément
   \(\mathcal R\) et \(\beta_n\).
2. **Zéros de \(\beta_n\).** L'infimum essentiel positif et la continuité du
   représentant \(W^{1,1}\) excluent réellement les zéros sur chaque fenêtre
   pour les grands \(n\).
3. **Changement de signe.** Une fonction continue non nulle ne change pas de
   signe sur une composante connexe. Aucun choix de branche complexe de
   l'inverse n'est impliqué.
4. **Régularité de l'inverse.** (15) est valide pour une fonction AC éloignée
   de zéro. L'hypothèse (5) porte sur ce représentant et sur chaque fenêtre.
5. **Test non lisse.** On n'insère pas naïvement \(\eta/\beta_n\) dans une
   distribution arbitraire. On réduit à l'équation scalaire \(W^{1,1}\)
   (19), où l'intégration par parties est licite.
6. **Bord temporel.** \(\eta\Subset J\) annule tous les termes de bord. Aucun
   contrôle de trace n'est caché.
7. **Espace du test.** Le résidu \(H^{-1}\) exige
   \(\varphi\in H^1_0(B_R)\); le choix lisse compact de (17) satisfait cette
   exigence. Le terme vitesse utilise séparément \(\varphi\in L^2\).
8. **Concentration temporelle.** La norme
   \(\|(1/\beta_n)'\|_{L^1}\), et non sa primitive signée, est nécessaire.
   Une cancellation de signe ne contrôlerait pas le second terme de (20).
9. **Borne \(L^\infty_tL^2_x\).** Elle est indispensable contre la mesure
   temporelle de variation de l'inverse. La forte \(L^3_{t,x}\) ne la
   remplace pas.
10. **Axe et centre.** \(\mathcal A\) est contractive sur les boules centrées
    seulement parce que l'axe passe par l'origine. Un centre mobile ou
    excentré ajoute transport et domaines mobiles.
11. **Moyenne contre générateur.** Les deux identités de (13) sont exactes;
    \(\mathcal A\mathcal R=0\) ne signifie pas que
    \(\mathcal RZ_n=0\) avant le passage à la limite.
12. **Ensembles exceptionnels.** Les conclusions finales sont
    distributionnelles. Une diagonale dénombrable produit, si demandé, un
    ensemble de temps commun pour les appariements.
13. **Pression.** La forte convergence locale identifie le stress, pas les
    queues de la pression. La jauge globale exige (34)--(35).
14. **Suitability.** Une suite de solutions suitable sans dissipation
    uniformément bornée ne donne pas automatiquement une limite suitable.
15. **Capture.** Une minoration à un temps unique ne passe pas par la seule
    convergence espace-temps.
16. **Portée Clay.** Le régime \(b_{n,J}\to\infty\), la petite variation de
    l'inverse et le défaut tangent fort (6) ne sont pas produits par une
    singularité Clay générale.

## 13. Statut logique

| Implication | Statut |
|---|---|
| (3)--(6) \(\Rightarrow\) estimation exacte (22) | **PROUVÉ** |
| (2), (22) \(\Rightarrow\mathcal RZ=0\) | **PROUVÉ** dans \(\mathcal D'\) |
| \(\mathcal A\mathcal R=0\), (6) \(\Rightarrow\partial_s\mathcal AZ=0\) | **PROUVÉ** |
| \(\mathcal RZ=0\Rightarrow\mathcal AZ=Z\) | **PROUVÉ** par l'action de groupe |
| conclusions précédentes \(\Rightarrow\partial_sZ=0\) | **PROUVÉ** |
| équations NS + (2) \(\Rightarrow\) équation stationnaire solénoïdale (33) | **PROUVÉ**, stress fort sans défaut |
| suitable individuel + (2)--(6) \(\Rightarrow U\in W^{1,2}_{\rm loc}\) | **NON DÉMONTRÉ** sans (36) |
| (34)--(36) \(\Rightarrow\) pression Riesz, suitability et (40) | **PROUVÉ conditionnellement** par le ledger compact standard |
| capture cylindrique + (2) \(\Rightarrow U\neq0\) | **PROUVÉ** |
| (40), (33), \(\kappa>0\Rightarrow U=0\) | **SOURCE_VERIFIED**, Guevara--Phuc |
| lemme de rotation rapide \(\Rightarrow\) résolution Clay | **NON DÉMONTRÉ** |

**Décision analytique : CONTINUER sous ledger uniforme.** La moyennisation
rapide ferme réellement le sous-scénario exact : une fréquence dont l'inverse
varie peu, jointe à un défaut tangent \(L^1H^{-1}\) petit, force une limite
axisymétrique puis stationnaire. Le verrou restant est de produire ces
hypothèses avec constantes uniformes depuis la dynamique Type I, ou de
construire un contre-scénario où la variation de \(1/\beta_n\) ne tend pas
vers zéro.
