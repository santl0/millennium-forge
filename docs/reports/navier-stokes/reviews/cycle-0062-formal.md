# Cycle 0062 — numérateurs azimutaux de la dérive Navier--Stokes renormalisée

Date : 2026-08-15.

Statut : **AI_INTERNAL_DERIVATION**. Calcul instantané pour un champ de
Schwartz divergence-free sur \(\mathbb R^3\). Aucun résultat de régularité
ou de blow-up.

## Verdict

Soit

\[
 d(Z)=\Delta Z-\mathbb P\operatorname{div}(Z\otimes Z)
 -\kappa(1+y\cdot\nabla)Z,\qquad \operatorname{div}Z=0,        \tag{1}
\]

où \(\mathbb P\) est la projection de Leray sur \(\mathbb R^3\), la
viscosité vaut un et \(\kappa\) est fixé. Pour l'action vectorielle
covariante de \(SO(2)\), écrivons

\[
 Z=\sum_{m\geq0}Z_m,\qquad Z_m=P_mZ,\qquad
 \mathcal RZ_m=mJ_mZ_m\quad(m\geq1),                          \tag{2}
\]

avec \(J_m^*=-J_m\) et \(J_m^2=-I\). Le numérateur isotypique est

\[
 C_m(Z)=
 \left\langle P_md(Z),\mathcal RP_mZ\right\rangle_{L^2},
 \qquad m\geq1.                                                \tag{3}
\]

Sa décomposition exacte est

\[
 \boxed{
 C_m=C_m^{\mathrm{diff}}+C_m^{\mathrm{conv}}
      +C_m^{\mathrm{drift}},}                                 \tag{4}
\]

avec

\[
 \boxed{C_m^{\mathrm{diff}}=0,}                               \tag{5}
\]

\[
 \boxed{
 C_m^{\mathrm{conv}}
 =
 \int_{\mathbb R^3}
 P_m^{(2)}(Z\otimes Z):\nabla\mathcal RZ_m\,dy,}              \tag{6}
\]

et

\[
 \boxed{
 C_m^{\mathrm{drift}}
 =-\kappa m
 \left\langle
 (y\cdot\nabla)Z_m,J_mZ_m
 \right\rangle_{L^2}.}                                       \tag{7}
\]

Le terme unité du drift s'annule, mais le terme de dilatation (7) ne
s'annule pas en général. La pression et la partie gradient retirée par
\(\mathbb P\) ne contribuent pas à (6), puisque
\(\mathcal RZ_m\) est divergence-free.

Il n'existe aucune contrainte algébrique

\[
 \sum_{m\geq1}C_m=0                                          \tag{8}
\]

issue de la seule covariance rotationnelle, de l'identité d'énergie ou de
la conservation du moment angulaire. La covariance impose les règles de
sélection triadiques; l'énergie contraint les productions **radiales**
\(\langle P_md(Z),Z_m\rangle\); le moment angulaire est un moment linéaire
distinct. Deux \(C_m\) de signes opposés sont donc algébriquement permis et,
pour \(\kappa\neq0\), peuvent déjà être réalisés par le drift sur des champs
de Schwartz divergence-free de petite amplitude.

## 1. Action covariante et projecteurs réels

Pour une rotation \(R_\theta=e^{\theta K}\) autour d'un axe fixé passant par
l'origine,

\[
 (Q_\theta^{(1)}U)(y)
 =R_\theta U(R_{-\theta}y),                                  \tag{9}
\]

et, sur les tenseurs,

\[
 (Q_\theta^{(2)}T)(y)
 =R_\theta T(R_{-\theta}y)R_\theta^T.                        \tag{10}
\]

Le générateur vectoriel est

\[
 \mathcal RU=KU-(Ky\cdot\nabla)U.                            \tag{11}
\]

Les projecteurs isotypiques réels sont

\[
 P_0=\frac1{2\pi}\int_0^{2\pi}Q_\theta^{(1)}\,d\theta,
\qquad
 P_m=\frac1\pi\int_0^{2\pi}
       \cos(m\theta)Q_\theta^{(1)}\,d\theta\quad(m\geq1).      \tag{12}
\]

On note \(P_m^{(2)}\) la formule analogue pour l'action tensorielle.
Chaque \(P_m\) est orthogonal dans \(L^2\), et

\[
 P_m\mathcal R=\mathcal RP_m,\qquad
 \mathcal R|_{H_m}=mJ_m.                                     \tag{13}
\]

Les composantes \(+m\) et \(-m\) de la complexification forment un seul
bloc réel \(H_m\). Elles ne doivent ni être comptées comme deux modes réels
indépendants, ni recevoir des constantes différentes.

L'indice \(m\) est celui de l'action covariante (9), qui tourne à la fois
l'argument et les composantes du vecteur. Il ne coïncide pas nécessairement
avec le numéro de Fourier de chaque composante cartésienne.

## 2. Commutations exactes

Les rotations centrées commutent avec le Laplacien et le générateur de
dilatation :

\[
 [Q_\theta^{(1)},\Delta]=0,\qquad
 [Q_\theta^{(1)},y\cdot\nabla]=0.                            \tag{14}
\]

La divergence est covariante :

\[
 \operatorname{div}Q_\theta^{(2)}T
 =Q_\theta^{(1)}\operatorname{div}T.                         \tag{15}
\]

La projection de Leray

\[
 \mathbb P=I-\nabla\Delta^{-1}\operatorname{div}
\]

est un multiplicateur de Fourier isotrope, homogène de degré zéro. Ainsi

\[
 [\mathbb P,Q_\theta^{(1)}]=0,\qquad
 [\mathbb P,P_m]=0,\qquad
 [\mathbb P,\mathcal R]=0.                                  \tag{16}
\]

Enfin,

\[
 Q_\theta^{(2)}(Z\otimes Z)
 =(Q_\theta^{(1)}Z)\otimes(Q_\theta^{(1)}Z),                 \tag{17}
\]

d'où l'équivariance non linéaire

\[
 d(Q_\theta Z)=Q_\theta d(Z).                                \tag{18}
\]

L'identité (18) ne signifie pas que \(d(Z)\) est orthogonal à l'orbite de
\(Z\). Une application équivariante peut parfaitement posséder une
composante tangentielle.

## 3. Diffusion : annulation mode par mode

Les commutations donnent

\[
 P_m\Delta Z=\Delta Z_m.
\]

Comme \(\Delta\) est auto-adjoint, \(\mathcal R\) antisymétrique et
\([\Delta,\mathcal R]=0\),

\[
 \begin{aligned}
 C_m^{\mathrm{diff}}
 &=\langle\Delta Z_m,\mathcal RZ_m\rangle\\
 &=\langle Z_m,\Delta\mathcal RZ_m\rangle\\
 &=\langle Z_m,\mathcal R\Delta Z_m\rangle\\
 &=-\langle\mathcal RZ_m,\Delta Z_m\rangle
 =-C_m^{\mathrm{diff}}.
 \end{aligned}                                               \tag{19}
\]

Cela prouve (5). Avec une viscosité constante \(\nu>0\), le terme devient
\(\nu C_m^{\mathrm{diff}}\) et reste exactement nul. L'annulation ne dépend
donc ni de \(m\), ni de \(\nu\).

## 4. Drift : seule l'unité s'annule

Posons

\[
 D=y\cdot\nabla,\qquad L=1+D.                                \tag{20}
\]

Sur \(L^2(\mathbb R^3)\), pour des champs de Schwartz,

\[
 D^*=-3-D,\qquad L^*=-2-D,\qquad
 D_0:=D+\frac32,\quad D_0^*=-D_0.                            \tag{21}
\]

Le drift commute avec \(P_m\), \(\mathcal R\) et \(J_m\). On a

\[
 \langle Z_m,\mathcal RZ_m\rangle
 =m\langle Z_m,J_mZ_m\rangle=0.                              \tag{22}
\]

Par conséquent,

\[
 \begin{aligned}
 C_m^{\mathrm{drift}}
 &=-\kappa\langle LZ_m,\mathcal RZ_m\rangle\\
 &=-\kappa m\langle DZ_m,J_mZ_m\rangle\\
 &=-\kappa m\langle D_0Z_m,J_mZ_m\rangle,
 \end{aligned}                                               \tag{23}
\]

ce qui est (7).

Deux opérateurs antisymétriques commutants n'ont pas un produit
antisymétrique : \(J_mD_0\) est auto-adjoint. En effet,

\[
 (J_mD_0)^*=D_0^*J_m^*=D_0J_m=J_mD_0.                       \tag{24}
\]

Ainsi le dernier produit dans (23) est une forme quadratique réelle sans
signe, et non une expression forcée à zéro. L'intégration par parties donne
seulement

\[
 \langle DZ_m,\mathcal RZ_m\rangle
 =-\langle Z_m,D\mathcal RZ_m\rangle,
\]

qui, après commutation et antisymétrie de \(\mathcal R\), reproduit la même
quantité; elle ne donne aucune annulation.

Le drift modal obéit à la borne exacte de Cauchy

\[
 |C_m^{\mathrm{drift}}|
 \leq|\kappa|\,m
 \|D_0Z_m\|_2\|Z_m\|_2.                                     \tag{25}
\]

Cette borne contient le facteur \(m\) du générateur et aucune constante
uniforme sur le domaine non borné de \(D_0\).

## 5. Convection, Leray et pression

Écrivons

\[
 N(Z)=-\mathbb P\operatorname{div}(Z\otimes Z).               \tag{26}
\]

Par (15)--(17),

\[
 P_mN(Z)
 =-\mathbb P\operatorname{div}
      P_m^{(2)}(Z\otimes Z).                                 \tag{27}
\]

Le champ \(\mathcal RZ_m\) est divergence-free. L'auto-adjonction de
\(\mathbb P\) donne

\[
 \langle\mathbb Pf,\mathcal RZ_m\rangle
 =\langle f,\mathbb P\mathcal RZ_m\rangle
 =\langle f,\mathcal RZ_m\rangle.                            \tag{28}
\]

Une intégration par parties dans (27) fournit donc

\[
 \begin{aligned}
 C_m^{\mathrm{conv}}
 &=-\left\langle
 \operatorname{div}P_m^{(2)}(Z\otimes Z),
 \mathcal RZ_m\right\rangle\\
 &=\int_{\mathbb R^3}
 P_m^{(2)}(Z\otimes Z):\nabla\mathcal RZ_m\,dy,
 \end{aligned}                                               \tag{29}
\]

soit (6). Aucun terme de pression ne subsiste. Si l'on part de

\[
 -(Z\cdot\nabla)Z-\nabla\Pi,
\]

alors

\[
 \langle\nabla\Pi,\mathcal RZ_m\rangle
 =-\langle\Pi,\operatorname{div}\mathcal RZ_m\rangle=0.       \tag{30}
\]

Cette annulation exige l'intégration globale sans bord, ou des conditions de
bord compatibles. Une localisation sur une boule crée un terme de coupure
et une pression harmonique; (30) n'est alors pas une annulation automatique.

## 6. Formule triadique complexe

Soit

\[
 Z_{\mathbb C}=\sum_{k\in\mathbb Z}z_k,\qquad
 Q_\theta z_k=e^{ik\theta}z_k,\qquad
 z_{-k}=\overline{z_k}.                                      \tag{31}
\]

Avec la convention complexe

\[
 \langle f,h\rangle_{\mathbb C}
 =\int_{\mathbb R^3}f\cdot\overline h\,dy,
\]

linéaire dans la première variable, le bloc réel \(m\geq1\) vérifie

\[
 \|Z_m\|_{L^2,\mathrm{real}}^2
 =2\|z_m\|_{L^2,\mathrm{complex}}^2.                          \tag{32}
\]

La composante complexe \(m\) de la non-linéarité est

\[
 N_m^{\mathbb C}
 =-\mathbb P\operatorname{div}
   \sum_{k+\ell=m}z_k\otimes z_\ell.                          \tag{33}
\]

Comme \(\mathcal Rz_m=imz_m\), (29) devient exactement

\[
 \boxed{
 C_m^{\mathrm{conv}}
 =2m\,\operatorname{Im}
 \sum_{k+\ell=m}
 \int_{\mathbb R^3}
 (z_k\otimes z_\ell):\nabla\overline{z_m}\,dy.}               \tag{34}
\]

Le facteur deux assemble les caractères conjugués \(+m\) et \(-m\); le
facteur \(m\) vient du générateur. Dans le langage des blocs réels,
\(P_m^{(2)}(Z_k\otimes Z_\ell)\) ne peut être non nul que si

\[
 m=k+\ell\quad\text{ou}\quad m=|k-\ell|                      \tag{35}
\]

pour des indices réels non négatifs convenablement associés. La formulation
complexe \(k+\ell=m\) évite cette ambiguïté de signes.

La règle (35) est la contrainte principale de covariance. Elle ne fixe pas
le signe de la partie imaginaire dans (34).

## 7. Somme des numérateurs tangentiels

Par orthogonalité des blocs et parce que \(\mathcal RZ_0=0\),

\[
 \sum_{m\geq1}C_m
 =\langle d(Z),\mathcal RZ\rangle.                           \tag{36}
\]

Les calculs précédents donnent

\[
 \boxed{
 \sum_{m\geq1}C_m
 =
 \int_{\mathbb R^3}
 (Z\otimes Z):\nabla\mathcal RZ\,dy
 -\kappa\langle DZ,\mathcal RZ\rangle.}                       \tag{37}
\]

La diffusion est absente, mais aucun des deux termes restants n'est nul en
général.

L'équivariance (18), différentiée en \(\theta\), donne

\[
 Dd(Z)[\mathcal RZ]=\mathcal Rd(Z).                           \tag{38}
\]

Elle ne donne pas \(\langle d(Z),\mathcal RZ\rangle=0\).
De même, pour la forme trilineaire

\[
 b(u,v,w)=\int_{\mathbb R^3}(u\cdot\nabla)v\cdot w\,dy,
\]

la covariance donne

\[
 b(\mathcal Ru,v,w)+b(u,\mathcal Rv,w)
 +b(u,v,\mathcal Rw)=0.                                      \tag{39}
\]

Avec \(u=v=w=Z\), l'antisymétrie

\[
 b(u,v,w)=-b(u,w,v)\qquad(\operatorname{div}u=0)              \tag{40}
\]

transforme (39) en une identité tautologique; elle n'annule pas
\(b(Z,Z,\mathcal RZ)\). La covariance fournit les triades (35), pas une
loi de signe ni la somme nulle (8).

## 8. Ce que l'identité d'énergie contraint réellement

Définissons les productions radiales

\[
 E_m=\langle P_md(Z),Z_m\rangle,\qquad m\geq0.                \tag{41}
\]

Pour chaque mode,

\[
 E_m^{\mathrm{diff}}=-\|\nabla Z_m\|_2^2,                    \tag{42}
\]

et, puisque

\[
 \langle(1+D)Z_m,Z_m\rangle
 =-\frac12\|Z_m\|_2^2,
\]

\[
 E_m^{\mathrm{drift}}
 =\frac\kappa2\|Z_m\|_2^2.                                   \tag{43}
\]

La convection redistribue l'énergie entre modes :

\[
 \sum_{m\geq0}E_m^{\mathrm{conv}}
 =\langle N(Z),Z\rangle=0.                                   \tag{44}
\]

Par conséquent,

\[
 \boxed{
 \sum_{m\geq0}E_m
 =-\|\nabla Z\|_2^2+\frac\kappa2\|Z\|_2^2.}                  \tag{45}
\]

Les relations (41)--(45) impliquent une somme sur les composantes parallèles
à \(Z_m\). Les numérateurs \(C_m\) sont les composantes parallèles à
\(\mathcal RZ_m=mJ_mZ_m\), orthogonales à \(Z_m\). Même dans un seul plan
réel isotypique, énergie radiale et vitesse tangentielle sont deux
coordonnées indépendantes. L'identité d'énergie n'impose donc aucune
relation supplémentaire à (37).

## 9. Moment angulaire

Pour un axe \(e\), soit

\[
 \xi_e(y)=e\times y,\qquad
 M_e(Z)=\int_{\mathbb R^3}\xi_e(y)\cdot Z(y)\,dy
       =e\cdot\int_{\mathbb R^3}y\times Z(y)\,dy.              \tag{46}
\]

Ce moment est bien défini pour \(Z\) de Schwartz, mais \(\xi_e\notin L^2\);
il ne s'agit pas d'un coefficient du produit hilbertien (3). Les calculs
suivants sont compris avec des coupures radiales tendant vers un, ou dans la
formulation vitesse--pression, lorsque les termes de bord ont une limite.
Ils ne résultent pas de l'auto-adjonction \(L^2\) de \(\mathbb P\) contre le
test non carré-intégrable \(\xi_e\).

Le Laplacien et la pression ne contribuent pas :

\[
 \Delta\xi_e=0,\qquad \operatorname{div}\xi_e=0.              \tag{47}
\]

Le gradient \(\nabla\xi_e\) est antisymétrique, tandis que
\(Z\otimes Z\) est symétrique, donc

\[
 \int_{\mathbb R^3}
 \xi_e\cdot[-\operatorname{div}(Z\otimes Z)]\,dy
 =
 \int_{\mathbb R^3}(Z\otimes Z):\nabla\xi_e\,dy=0.            \tag{48}
\]

Comme \(\xi_e\) est homogène de degré un,

\[
 \int_{\mathbb R^3}\xi_e\cdot DZ\,dy
 =-\int_{\mathbb R^3}
 Z\cdot(D\xi_e+3\xi_e)\,dy
 =-4M_e(Z).                                                    \tag{49}
\]

Le drift de (1) donne donc

Sous cette convention de limite,

\[
 \boxed{M_e(d(Z))=3\kappa M_e(Z).}                            \tag{50}
\]

Dans une trajectoire \(\partial_sZ=d(Z)\),

\[
 \frac d{ds}M_e(Z)=3\kappa M_e(Z).                            \tag{51}
\]

Pour \(\kappa=0\), on retrouve la conservation du moment angulaire du champ
non renormalisé. Pour l'axe même de l'action \(SO(2)\),
\(\xi_e\) est invariant et le fonctionnel (46) ne voit que le bloc
axisymétrique \(H_0\). Les composantes transverses du vecteur moment forment
un bloc réel de fréquence un. Dans tous les cas, (50) est une loi **linéaire**
sur \(Z\); elle ne contraint pas la somme quadratique tangentielle (36).

## 10. Deux signes opposés sont permis

La forme du drift sur \(H_m\) peut s'écrire

\[
 C_m^{\mathrm{drift}}
 =-\kappa m\langle B_mZ_m,Z_m\rangle,\qquad
 B_m=-J_mD_0=B_m^*.                                          \tag{52}
\]

Le groupe unitaire de dilatations a pour générateur \(D_0\) et commute avec
les rotations. Sur chaque bloc solénoïdal non trivial, \(B_m\) n'est pas un
opérateur de signe fixé. Une façon de le voir est que la transformation de
Fourier commute avec l'action rotationnelle et conjugue le générateur de
dilatation centré en son opposé :

\[
 \mathcal FD_0\mathcal F^{-1}=-D_0.                           \tag{53}
\]

Elle conjugue donc \(B_m\) en \(-B_m\). Des vecteurs de Schwartz
solénoïdaux, qui forment un cœur invariant, réalisent des valeurs strictement
positives et strictement négatives de la forme quadratique dès que
\(B_m\neq0\).

Choisissons deux indices actifs \(m\neq\ell\) et des champs
\(U_m\in H_m\), \(U_\ell\in H_\ell\), de Schwartz et divergence-free, tels
que

\[
 C_m^{\mathrm{drift}}(U_m)>0,\qquad
 C_\ell^{\mathrm{drift}}(U_\ell)<0.                          \tag{54}
\]

Pour

\[
 Z_\varepsilon=\varepsilon(U_m+U_\ell),
\]

les contributions de drift sont d'ordre \(\varepsilon^2\), tandis que tous
les numérateurs convectifs sont d'ordre \(\varepsilon^3\). La diffusion
reste nulle. Pour \(\varepsilon>0\) assez petit et \(\kappa\neq0\), les
signes stricts de (54) persistent donc dans les \(C_m(Z_\varepsilon)\) et
\(C_\ell(Z_\varepsilon)\).

Cette construction montre que deux signes opposés sont compatibles avec
toutes les symétries, la divergence nulle et l'identité d'énergie. Lorsque
\(\kappa=0\), la formule triadique (34) n'impose toujours aucun signe; la
réalisation doit alors utiliser une triade convective non nulle plutôt que
le petit régime dominé par le drift.

## 11. Constantes et loi d'échelle

Sous l'échelle spatiale critique de la vitesse

\[
 Z_\lambda(y)=\lambda Z(\lambda y),                           \tag{55}
\]

les projecteurs azimutaux et \(\mathcal R\) commutent avec la dilatation.
On a

\[
 \|\mathcal RZ_{\lambda,m}\|_2^2
 =\lambda^{-1}\|\mathcal RZ_m\|_2^2.                         \tag{56}
\]

La diffusion et la convection ont l'échelle

\[
 \Delta Z_\lambda,\quad
 \mathbb P\operatorname{div}(Z_\lambda\otimes Z_\lambda)
 =\lambda^3[\cdots](\lambda y),
\]

tandis que le drift a l'échelle de la vitesse :

\[
 (1+y\cdot\nabla)Z_\lambda
 =\lambda[(1+y\cdot\nabla)Z](\lambda y).                      \tag{57}
\]

Par conséquent,

\[
 C_m^{\mathrm{conv}}(Z_\lambda)
 =\lambda C_m^{\mathrm{conv}}(Z),\qquad
 C_m^{\mathrm{drift}}(Z_\lambda)
 =\lambda^{-1}C_m^{\mathrm{drift}}(Z),                        \tag{58}
\]

et \(C_m^{\mathrm{diff}}=0\) avant comme après changement d'échelle. Le
numérateur complet n'est donc pas homogène lorsque \(\kappa\neq0\); le drift
renormalisé fixe une échelle.

En divisant par le Gram (56), la contribution du drift à la vitesse modale
est invariante sous (55), tandis que la contribution convective est
multipliée par \(\lambda^2\). Cette dernière a bien l'échelle d'une
fréquence en temps physique. Aucun de ces calculs ne fournit une constante
uniforme après changement du cadre renormalisé.

Les constantes exactes visibles sont :

- le facteur de viscosité, sans effet car (5) est nul;
- le facteur \(\kappa m\) dans (7);
- le facteur \(2m\) dans la convention complexe (34);
- le facteur \(3\kappa\) du moment angulaire (50);
- les puissances \(\lambda^{-1}\) et \(\lambda\) de (58).

## 12. Passe contradictoire

1. **Action scalaire erronée.** Oublier la rotation des composantes dans
   (9) change le générateur et les indices azimutaux.
2. **Double comptage.** Les modes \(+m\) et \(-m\) constituent un seul bloc
   réel; le facteur deux de (34) doit être suivi.
3. **Diffusion.** Son annulation utilise à la fois auto-adjonction,
   antisymétrie et commutation. L'antisymétrie seule ne suffit pas.
4. **Drift.** Deux générateurs antisymétriques commutants ont un produit
   auto-adjoint; conclure que (7) est nul serait une erreur.
5. **Terme unité.** Il s'annule séparément par
   \(\langle Z_m,J_mZ_m\rangle=0\).
6. **Leray.** On peut retirer \(\mathbb P\) seulement dans le produit avec
   le champ global divergence-free \(\mathcal RZ_m\).
7. **Pression locale.** Une coupure détruit l'annulation globale (30) sans
   termes correctifs.
8. **Triades.** La covariance impose \(k+\ell=m\), pas le signe de la partie
   imaginaire de l'interaction.
9. **Somme tangentielle.** L'équivariance (38) ne donne pas
   \(\langle d,\mathcal RZ\rangle=0\).
10. **Énergie.** La somme nulle convective porte sur
    \(\langle N_m,Z_m\rangle\), pas sur \(C_m\).
11. **Moment angulaire.** Il utilise un test linéaire non \(L^2\) et ne
    contraint pas les numérateurs quadratiques.
12. **Signes opposés.** Le petit régime (54) les autorise déjà pour
    \(\kappa\neq0\); aucune positivité cachée ne subsiste.
13. **Échelle.** La somme convection-drift n'a pas une loi homogène unique
    dans les variables renormalisées.
14. **Portée Clay.** Les champs de Schwartz instantanés ne construisent ni
    trajectoire ancienne admissible, ni scénario de blow-up.

## 13. Statut logique

| Affirmation | Statut |
|---|---|
| diffusion \(C_m^{\mathrm{diff}}=0\) | **PROUVÉ** mode par mode |
| terme unité du drift nul | **PROUVÉ** par antisymétrie |
| terme de dilatation du drift nul | **RÉFUTÉ**; forme auto-adjointe (52) |
| pression/Leray sans contribution directe | **PROUVÉ** globalement |
| formule convective réelle (29) | **PROUVÉ** |
| formule triadique complexe (34) | **PROUVÉ** avec convention (32) |
| covariance \(\Rightarrow\sum_mC_m=0\) | **RÉFUTÉ** par (37)--(40) |
| énergie \(\Rightarrow\sum_mC_m=0\) | **RÉFUTÉ**; elle contraint (41) |
| moment angulaire \(\Rightarrow\sum_mC_m=0\) | **RÉFUTÉ**; loi distincte (50) |
| deux signes modaux opposés permis | **PROUVÉ** pour \(\kappa\neq0\) par petite amplitude |
| scaling des contributions | **PROUVÉ** par (55)--(58) |
| contraintes précédentes \(\Rightarrow\) robustesse modale | **NON DÉMONTRÉ** |

**Décision analytique : ABANDONNER toute tentative de signe obtenue par les
seules symétries.** Le calcul exact laisse deux sources signées indépendantes,
la torsion dilatation--rotation (7) et les phases triadiques (34). Une
contrainte de signe utile devrait provenir d'une hypothèse PDE ou géométrique
supplémentaire, et non de covariance, énergie ou moment angulaire seuls.
