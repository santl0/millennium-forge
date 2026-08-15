# Cycle 0063 — dérivée du numérateur tangent et critère de Nagumo

Date : 2026-08-15.

Statut : **AI_INTERNAL_DERIVATION**.

Cadre : calcul formel rigoureux pour une trajectoire classique suffisamment
régulière et décroissante sur \(\mathbb R^3\). Aucun résultat de régularité
globale ou d'existence ancienne.

## Verdict

Notons

\[
 \mathfrak F(Z)
 =\Delta Z-\mathbb P\operatorname{div}(Z\otimes Z)
 -\kappa(1+y\cdot\nabla)Z,\qquad \operatorname{div}Z=0,        \tag{1}
\]

et supposons

\[
 Z'(s)=\mathfrak F(Z(s)).                                     \tag{2}
\]

Pour un bloc isotypique réel \(m\geq1\), posons

\[
 z_m=P_mZ,\qquad
 u=\mathfrak F(Z),\qquad
 u_m=P_mu,\qquad
 g_m=\mathcal Rz_m,                                           \tag{3}
\]

et

\[
 C_m(Z)=\langle P_m\mathfrak F(Z),\mathcal RP_mZ\rangle_{L^2}
 =\langle u_m,g_m\rangle_{L^2}.                               \tag{4}
\]

La dérivée de Fréchet de \(\mathfrak F\) est

\[
 \boxed{
 D\mathfrak F(Z)[H]
 =\Delta H
 -\mathbb P\operatorname{div}(H\otimes Z+Z\otimes H)
 -\kappa(1+y\cdot\nabla)H.}                                  \tag{5}
\]

Le long de (2), la règle du produit donne

\[
 \frac d{ds}C_m
 =
 \left\langle P_mD\mathfrak F(Z)[u],g_m\right\rangle
 +
 \left\langle u_m,\mathcal Ru_m\right\rangle.                 \tag{6}
\]

Le second terme est nul par antisymétrie de \(\mathcal R\). Il représente
cependant bien la dérivée de la tangente \(g_m\); l'omettre avant
différentiation serait une erreur de chaîne. Par conséquent,

\[
 \boxed{
 \frac d{ds}C_m(Z(s))
 =
 \left\langle
 P_mD\mathfrak F(Z)[\mathfrak F(Z)],
 \mathcal RP_mZ
 \right\rangle.}                                             \tag{7}
\]

En développant (5), la formule exacte est

\[
 \boxed{
 \begin{aligned}
 C_m'
 ={}&
 \langle\Delta u_m,\mathcal Rz_m\rangle\\
 &+\int_{\mathbb R^3}
 P_m^{(2)}(u\otimes Z+Z\otimes u):
       \nabla\mathcal Rz_m\,dy\\
 &-\kappa
 \langle(1+y\cdot\nabla)u_m,\mathcal Rz_m\rangle.
 \end{aligned}}                                               \tag{8}
\]

Aucun des trois termes de (8) n'est nul en général. L'annulation
diffusive du cycle 0062 concernait
\(\langle\Delta z_m,\mathcal Rz_m\rangle\), avec le même champ dans les deux
places; elle ne s'applique pas à
\(\langle\Delta u_m,\mathcal Rz_m\rangle\).

Pour un ensemble fini \(M\subset\mathbb N_{\geq1}\), le critère de Nagumo
exact pour la région

\[
 \mathcal K_M^+
 =\{Z:C_m(Z)\geq0\ \text{pour tout }m\in M\}                  \tag{9}
\]

est

\[
 \boxed{
 \mathfrak F(Z)\in T_{\mathcal K_M^+}(Z)
 \quad\text{pour tout }Z\in\mathcal K_M^+.}                   \tag{10}
\]

Ici \(T_{\mathcal K_M^+}\) est le cône tangent contingent dans l'espace de
phase choisi. Aux points réguliers de la frontière, (10) équivaut à

\[
 C_m'(Z)\geq0
 \quad\text{pour tout }m\in M\text{ tel que }C_m(Z)=0.         \tag{11}
\]

Pour \(\mathcal K_M^-=\{C_m\leq0\}\), le signe de (11) est inversé.
La formule (11) n'est ni suffisante aux points singuliers de la frontière,
ni un théorème sur le semiflot Navier--Stokes sans vérification préalable
des hypothèses fonctionnelles de Nagumo.

## 1. Différentielle complète de \(C_m\)

Pour une direction admissible \(H\), la règle du produit donne

\[
 \boxed{
 DC_m(Z)[H]
 =
 \left\langle
 P_mD\mathfrak F(Z)[H],\mathcal RP_mZ
 \right\rangle
 +
 \left\langle
 P_m\mathfrak F(Z),\mathcal RP_mH
 \right\rangle.}                                             \tag{12}
\]

Les projecteurs \(P_m\) et \(\mathbb P\) sont auto-adjoints dans \(L^2\).
Le générateur \(\mathcal R\) est antisymétrique et commute avec \(P_m\).
Sur le bloc réel \(H_m=P_mL^2\),

\[
 \mathcal R=mJ_m,\qquad J_m^*=-J_m,\qquad J_m^2=-I.           \tag{13}
\]

En prenant \(H=u=\mathfrak F(Z)\), la seconde partie de (12) devient

\[
 \left\langle u_m,\mathcal Ru_m\right\rangle=0.               \tag{14}
\]

Les formules (7)--(8) suivent. Pour un mode fixé,
\(\mathcal R|_{H_m}\) est borné de norme \(m\); il n'est donc pas nécessaire
de sommer \(\sum_m m^2\|u_m\|_2^2\) pour donner un sens à (14). Une formule
simultanée sur tous les modes exigerait en revanche
\(u\in D(\mathcal R)\).

## 2. Dérivée de l'équation et équivariance

La partie quadratique de (1) a pour différentielle

\[
 D\!\left[-\mathbb P\operatorname{div}(Z\otimes Z)\right][H]
 =
 -\mathbb P\operatorname{div}(H\otimes Z+Z\otimes H),         \tag{15}
\]

ce qui prouve (5). L'action vectorielle covariante est

\[
 (Q_\theta Z)(y)=R_\theta Z(R_{-\theta}y),                    \tag{16}
\]

et l'action tensorielle comporte un facteur \(R_\theta\) de chaque côté.
On a

\[
 \mathfrak F(Q_\theta Z)=Q_\theta\mathfrak F(Z).              \tag{17}
\]

En différentiant (17) par rapport à \(\theta\),

\[
 D\mathfrak F(Z)[\mathcal RZ]
 =\mathcal R\mathfrak F(Z).                                  \tag{18}
\]

L'identité (18) ne simplifie pas le premier terme de (7), car sa direction
est \(u=\mathfrak F(Z)\), et non \(\mathcal RZ\). Confondre ces deux
directions remplacerait l'accélération réelle du flot par une variation de
jauge.

## 3. Diffusion dans la dérivée

Les commutations

\[
 [P_m,\Delta]=[\mathcal R,\Delta]=0                           \tag{19}
\]

donnent le premier terme de (8). Par auto-adjonction,

\[
 \begin{aligned}
 \langle\Delta u_m,\mathcal Rz_m\rangle
 &=\langle u_m,\Delta\mathcal Rz_m\rangle\\
 &=\langle u_m,\mathcal R\Delta z_m\rangle\\
 &=-\langle\mathcal Ru_m,\Delta z_m\rangle.
 \end{aligned}                                                \tag{20}
\]

La dernière expression n'est pas l'opposée de la première avec les mêmes
arguments; elle ne force donc pas zéro.

On peut retrouver ce fait en différentiant l'identité instantanée

\[
 \langle\Delta z_m,\mathcal Rz_m\rangle=0.
\]

Elle donne

\[
 \langle\Delta u_m,\mathcal Rz_m\rangle
 +
 \langle\Delta z_m,\mathcal Ru_m\rangle=0,                    \tag{21}
\]

qui est une compensation entre deux termes, pas leur annulation séparée.
Le second terme de (21) est caché dans la dérivée des autres composantes de
\(C_m\) lorsque \(u_m\) est remplacé par l'équation complète.

## 4. Convection linéarisée

La divergence est covariante et

\[
 P_m\mathbb P\operatorname{div}T
 =\mathbb P\operatorname{div}P_m^{(2)}T.                     \tag{22}
\]

Comme \(\mathcal Rz_m\) est divergence-free,

\[
 \langle\mathbb Pf,\mathcal Rz_m\rangle
 =\langle f,\mathcal Rz_m\rangle.                            \tag{23}
\]

Une intégration par parties donne

\[
 \begin{aligned}
 &-\left\langle
 \mathbb P\operatorname{div}
 P_m^{(2)}(u\otimes Z+Z\otimes u),
 \mathcal Rz_m\right\rangle\\
 &\qquad=
 \int_{\mathbb R^3}
 P_m^{(2)}(u\otimes Z+Z\otimes u):
       \nabla\mathcal Rz_m\,dy.                              \tag{24}
\end{aligned}
\]

C'est le second terme de (8). Les deux ordres
\(u\otimes Z\) et \(Z\otimes u\) sont nécessaires. Bien que \(u\) et \(Z\)
soient divergence-free, ils représentent respectivement

\[
 \operatorname{div}(u\otimes Z)=(Z\cdot\nabla)u,\qquad
 \operatorname{div}(Z\otimes u)=(u\cdot\nabla)Z.              \tag{25}
\]

La covariance impose les règles de sélection azimutales dans
\(P_m^{(2)}\), mais aucun signe au terme cubique-quartique obtenu après
substitution de \(u\).

## 5. Drift linéarisé

Avec

\[
 D=y\cdot\nabla,\qquad L=1+D,\qquad
 D_0=D+\frac32,                                               \tag{26}
\]

on a

\[
 D_0^*=-D_0,\qquad [D_0,P_m]=[D_0,\mathcal R]=0.              \tag{27}
\]

Le dernier terme de (8) est

\[
 -\kappa\langle Lu_m,\mathcal Rz_m\rangle.                   \tag{28}
\]

Contrairement au numérateur instantané du drift
\(-\kappa\langle Lz_m,\mathcal Rz_m\rangle\), le terme unité de (28) ne
s'annule pas :

\[
 \langle u_m,\mathcal Rz_m\rangle=C_m(Z).                    \tag{29}
\]

Ainsi

\[
 -\kappa\langle Lu_m,\mathcal Rz_m\rangle
 =
 -\kappa C_m
 -\kappa\langle Du_m,\mathcal Rz_m\rangle.                   \tag{30}
\]

L'adjoint de \(D\) donne seulement

\[
 \langle Du_m,\mathcal Rz_m\rangle
 =
 -3\langle u_m,\mathcal Rz_m\rangle
 -\langle u_m,\mathcal RDz_m\rangle,                         \tag{31}
\]

pas une annulation. Sur la frontière \(C_m=0\), le premier terme de (30)
disparaît, mais la corrélation dilatation--rotation de (31) reste signée.

## 6. Pression globale et projection de Leray

Pour un champ divergence-free suffisamment régulier, la jauge globale est

\[
 \Pi(Z)=R_iR_j(Z_iZ_j),                                      \tag{32}
\]

et

\[
 \mathfrak F(Z)
 =\Delta Z-\operatorname{div}(Z\otimes Z)
 -\nabla\Pi(Z)-\kappa LZ.                                    \tag{33}
\]

Sa différentielle est

\[
 D\Pi(Z)[H]
 =R_iR_j(H_iZ_j+Z_iH_j),                                    \tag{34}
\]

d'où

\[
 \begin{aligned}
 D\mathfrak F(Z)[H]
 ={}&\Delta H-\operatorname{div}(H\otimes Z+Z\otimes H)\\
 &-\nabla D\Pi(Z)[H]-\kappa LH.                              \tag{35}
 \end{aligned}
\]

Le terme de pression linéarisé ne contribue pas à (7) :

\[
 \langle\nabla D\Pi(Z)[u],\mathcal Rz_m\rangle
 =-\langle D\Pi(Z)[u],
        \operatorname{div}\mathcal Rz_m\rangle=0.             \tag{36}
\]

Les formules (23) et (36) sont globales. Sur une boule ou après une coupure,
la projection de Leray n'est pas la restriction de la projection globale;
une pression harmonique et des termes de bord doivent être ajoutés.

## 7. Régularité et domaines

La chaîne (7) est justifiée si, sur l'intervalle considéré,

\[
 Z\in C^1(I;X),\qquad
 u=\mathfrak F(Z)\in C(I;X),\qquad
 D\mathfrak F(Z)[u]\in C(I;L^2),                             \tag{37}
\]

pour un espace \(X\) sur lequel les produits de (5) sont définis et
\(\mathfrak F:X\to L^2\) est \(C^1\). Une condition concrète suffisante à
un temps fixé est

\[
 Z,u,\Delta u,Lu\in L^2,\qquad
 \operatorname{div}(u\otimes Z+Z\otimes u)\in L^2
\]

après application de \(\mathbb P\), avec assez de régularité pour les
intégrations par parties.

Un champ \(Z\) de Schwartz rend les calculs instantanés licites, mais
\(\mathbb P\operatorname{div}(Z\otimes Z)\) n'est pas nécessairement de
Schwartz : le multiplicateur de Leray est non local et non lisse à fréquence
nulle. Il faut vérifier les normes pondérées de \(u\) au lieu d'affirmer que
la classe de Schwartz est automatiquement stable.

Pour une solution forte parabolique, \(Z''=D\mathfrak F(Z)[u]\) peut être
interprété dans un espace plus faible que \(L^2\). La formule (7) subsiste
alors par dualité seulement si \(\mathcal Rz_m\) appartient au prédual
approprié. Une solution suitable ou Leray--Hopf ne possède pas, en général,
la seconde régularité temporelle nécessaire pour lire \(C_m'\) pointwise.

## 8. Scaling

Séparons

\[
 \mathfrak F_3(Z)
 =\Delta Z-\mathbb P\operatorname{div}(Z\otimes Z),\qquad
 \mathfrak F_1(Z)=-\kappa LZ.                                \tag{38}
\]

Sous la dilatation critique spatiale

\[
 (S_\lambda Z)(y)=\lambda Z(\lambda y),                       \tag{39}
\]

on a

\[
 \mathfrak F_3(S_\lambda Z)(y)
 =\lambda^3\mathfrak F_3(Z)(\lambda y),\qquad
 \mathfrak F_1(S_\lambda Z)(y)
 =\lambda\mathfrak F_1(Z)(\lambda y).                         \tag{40}
\]

Le numérateur se décompose en une partie convective cubique
\(C_m^{(3)}\) et une partie drift quadratique \(C_m^{(1)}\) :

\[
 C_m^{(3)}(S_\lambda Z)=\lambda C_m^{(3)}(Z),\qquad
 C_m^{(1)}(S_\lambda Z)=\lambda^{-1}C_m^{(1)}(Z).             \tag{41}
\]

La diffusion ne contribue pas à \(C_m\), mais elle contribue à sa dérivée
via \(\mathfrak F_3\). En développant

\[
 DC_m(Z)[\mathfrak F(Z)]
 =
 DC_m^{(3)}(Z)[\mathfrak F_3(Z)]
 +DC_m^{(3)}(Z)[\mathfrak F_1(Z)]
 +DC_m^{(1)}(Z)[\mathfrak F_3(Z)]
 +DC_m^{(1)}(Z)[\mathfrak F_1(Z)],                            \tag{42}
\]

les quatre termes ont respectivement les échelles

\[
 \lambda^3,\qquad\lambda,\qquad\lambda,\qquad\lambda^{-1}.    \tag{43}
\]

Ainsi

\[
 C_m'(S_\lambda Z)
 =
 \lambda^3A_m(Z)+\lambda B_m(Z)+\lambda^{-1}D_m(Z),           \tag{44}
\]

avec les trois coefficients définis par (42). Il n'existe pas de loi
homogène unique lorsque \(\kappa\neq0\). Pour \(\kappa=0\), la loi
parabolique homogène est \(\lambda^3\), cohérente avec une dérivée temporelle
de \(C_m\), lequel porte le facteur \(\lambda\).

## 9. Critère de Nagumo exact

Fixons un espace de phase réel \(X\) dans lequel :

1. le problème (2) engendre un semiflot local unique;
2. chaque \(C_m:X\to\mathbb R\), \(m\in M\), est continu et
   différentiable sur le domaine pertinent;
3. l'ensemble (9) est fermé.

Le cône tangent contingent est

\[
 T_{\mathcal K}(Z)
 =
 \left\{H\in X:
 \liminf_{h\downarrow0}
 \frac{\operatorname{dist}(Z+hH,\mathcal K)}{h}=0\right\}.    \tag{45}
\]

Sous les hypothèses standard de viabilité pour ce semiflot, la condition
(10) est le critère intrinsèque d'invariance positive. Il ne dépend pas
d'une représentation particulière de la frontière.

Si \(Z\in\partial\mathcal K_M^+\), notons

\[
 I(Z)=\{m\in M:C_m(Z)=0\}.                                   \tag{46}
\]

Lorsque les contraintes actives satisfont une qualification régulière
garantissant

\[
 T_{\mathcal K_M^+}(Z)
 =
 \{H:DC_m(Z)[H]\geq0\ \forall m\in I(Z)\},                   \tag{47}
\]

le critère devient (11), avec \(C_m'\) donné par (8). Pour la région
négative,

\[
 T_{\mathcal K_M^-}(Z)
 =
 \{H:DC_m(Z)[H]\leq0\ \forall m\in I(Z)\}.                   \tag{48}
\]

Une condition stricte

\[
 C_m'(Z)>0
\]

sur chaque face active positive est une barrière locale robuste, mais elle
est beaucoup plus forte que nécessaire et doit être uniforme pour produire
un contrôle quantitatif.

Le mot « cône » désigne rigoureusement l'orthant des valeurs

\[
 (C_m)_{m\in M}\in\mathbb R_{\geq0}^{|M|}.
\]

Sa préimage \(\mathcal K_M^+\) n'est généralement pas un cône dans l'espace
des champs : \(C_m\) contient une partie quadratique de drift et une partie
cubique de convection, qui changent différemment sous
\(Z\mapsto aZ\).

## 10. Frontière singulière et Grams nuls

Le Gram modal est

\[
 G_m(Z)=\|\mathcal RP_mZ\|_2^2=m^2\|Z_m\|_2^2.               \tag{49}
\]

Si \(G_m=0\), alors \(z_m=0\), \(C_m=0\), et la vitesse quotient

\[
 \beta_m=\frac{C_m}{G_m}
\]

est indéfinie. La convention \(\beta_m=0\) n'apporte aucune information de
tangence.

À un tel point, la différentielle (12) devient

\[
 DC_m(Z)[H]
 =
 \langle u_m,\mathcal RP_mH\rangle.                           \tag{50}
\]

Le long du flot,

\[
 DC_m(Z)[u]
 =\langle u_m,\mathcal Ru_m\rangle=0.                         \tag{51}
\]

La condition scalaire de premier ordre est donc automatiquement saturée,
même si les dérivées d'ordre supérieur peuvent créer ensuite un \(C_m\) de
l'un ou l'autre signe. Si \(u_m=0\) également, alors
\(DC_m(Z)=0\) : la fonction définissant la frontière est singulière et
(47) peut être faux.

Plus généralement, plusieurs contraintes actives peuvent avoir des
gradients dépendants ou nuls. L'intersection possède alors des coins,
cusps ou auto-intersections. Imposer séparément (11) sans prouver (47) n'est
pas un critère de Nagumo suffisant.

## 11. Attaque des quantificateurs

### 11.1 Un mode, plusieurs modes, tous les modes

Une condition pour un \(m\) fixé ne contrôle pas les autres blocs. Une
condition pour tout ensemble fini \(M\) avec des constantes dépendant de
\(M\) ne donne pas automatiquement une condition uniforme sur l'intersection
infinie

\[
 \bigcap_{m\geq1}\{C_m\geq0\}.
\]

Le passage \(M\uparrow\mathbb N\) exige fermeture, contrôle des hautes
fréquences et sommabilité des gradients \(DC_m\).

### 11.2 Pointwise contre uniforme

Vérifier (11) en un seul point de frontière ne prouve rien sur les autres
points visités par le flot. Pour une invariance positive, la condition doit
valoir sur toute la frontière accessible de \(\mathcal K_M^+\), dans un
espace où le semiflot est défini.

Une inégalité

\[
 C_m'(Z)\geq0\quad\text{lorsque }C_m(Z)=0
\]

sans constante de transversalité peut empêcher le franchissement dans un
ODE régulier, mais ne produit ni séparation quantitative, ni robustesse
sous passage à la limite.

### 11.3 Sens du temps

Nagumo donne une invariance **vers l'avant** pour un semiflot parabolique.
Il ne construit pas une trajectoire ancienne et ne permet pas de propager
le signe vers les temps antérieurs. Pour une solution définie sur
\((-\infty,s_0]\), il faudrait :

- connaître le signe à un temps antérieur fini et propager vers l'avant;
- ou contrôler une limite lorsque \(s\to-\infty\);
- ou disposer d'un flot inversible, absent pour Navier--Stokes dissipatif.

Une région positivement invariante n'est donc pas, à elle seule, un
mécanisme d'existence ou de classification des solutions anciennes.

### 11.4 Limites faibles

Le fonctionnel \(C_m\) contient les produits non linéaires et
\(\mathfrak F(Z)\). Il n'est pas continu sous une convergence faible
arbitraire. Une tangence prouvée sur des approximants de Galerkin ne passe
pas au continuum sans convergence forte suffisante, contrôle de pression et
uniformité des domaines.

## 12. Passe contradictoire

1. **Règle du produit.** La dérivée de la tangente produit le second terme
   de (6); il s'annule seulement après substitution de \(Z'=u\).
2. **Mauvaise direction.** L'équivariance contrôle
   \(D\mathfrak F(Z)[\mathcal RZ]\), pas
   \(D\mathfrak F(Z)[\mathfrak F(Z)]\).
3. **Diffusion.** L'annulation instantanée ne se transfère pas à sa dérivée;
   les arguments sont \(u_m\) et \(z_m\).
4. **Drift.** Son terme unité vaut \(-\kappa C_m\) dans (30), et ne
   disparaît que sur la frontière.
5. **Convection.** Les deux termes linéarisés de (15) sont indispensables.
6. **Leray.** Son retrait utilise auto-adjonction et divergence nulle du test
   global.
7. **Pression.** La pression linéarisée (34) est non locale; sa contribution
   disparaît dans le produit global, pas après localisation naïve.
8. **Schwartz.** La projection de Leray ne préserve pas automatiquement les
   poids de Schwartz requis.
9. **Seconde dérivée temporelle.** Une solution faible ne donne pas
   \(D\mathfrak F(Z)[u]\) pointwise dans \(L^2\).
10. **Pseudo-cône.** La préimage (9) n'est pas stable par multiplication
    scalaire à cause des degrés deux et trois.
11. **Nagumo régulier.** Les inégalités actives (11) ne remplacent le cône
    contingent que sous la qualification (47).
12. **Gram nul.** La dérivée le long du flot est automatiquement nulle en
    (51); le second ordre décide potentiellement le signe.
13. **Infinité de modes.** Un résultat uniforme ne suit pas d'une collection
    de résultats finis non uniformes.
14. **Ancienneté.** L'invariance positive ne se renverse pas dans le temps.
15. **Scaling.** Pour \(\kappa\neq0\), trois puissances distinctes apparaissent
    dans (44); aucune barrière homogène n'en découle.
16. **Portée Clay.** Aucune condition de tangence de signe n'est dérivée
    d'un scénario général de blow-up admissible.

## 13. Statut logique

| Affirmation | Statut |
|---|---|
| différentielle \(D\mathfrak F\), formule (5) | **PROUVÉ** |
| différentielle générale \(DC_m\), formule (12) | **PROUVÉ** |
| dérivée le long du flot, formule (7) | **PROUVÉ** |
| dérivée de la tangente automatiquement absente | **RÉFUTÉ**; elle est présente puis s'annule par (14) |
| diffusion absente de \(C_m'\) | **RÉFUTÉ** par (20)--(21) |
| formule linéarisée convective (24) | **PROUVÉ** |
| pression globale sans contribution directe | **PROUVÉ** sous les domaines indiqués |
| scaling (42)--(44) | **PROUVÉ** |
| tangence contingente (10) | **CRITÈRE EXACT** sous hypothèses de semiflot |
| inégalités de face (11) | **PROUVÉ conditionnellement** à la régularité (47) |
| condition de premier ordre suffisante aux Grams nuls | **NON DÉMONTRÉ**, et dégénérée par (51) |
| invariance positive \(\Rightarrow\) solution ancienne | **RÉFUTÉ** |
| tangence finie \(\Rightarrow\) contrôle de tous les modes | **NON DÉMONTRÉ** |
| critère de signe \(\Rightarrow\) régularité Clay | **NON DÉMONTRÉ** |

**Décision formelle : RÉVISER.** La formule (8) transforme l'idée de signe
en un test falsifiable sur une frontière finie, mais aucun terme n'y possède
un signe structurel. La prochaine étape utile serait un calcul certifié de
\(C_m'\) sur une famille compacte et régulière de champs, avec exclusion
séparée des Grams nuls; sans cette réduction, le vocabulaire de « cône
invariant » dépasse ce qui est démontré.
