# Cycle 0060 — système exact moyenne de Haar / fluctuation

Date : 2026-08-15.

Statut : **AI_INTERNAL_DERIVATION**. Dérivation algébrique et énergétique
pour des champs lisses décroissants, puis audit de sa portée
distributionnelle. Aucun résultat de régularité Clay.

## Verdict

Pour l'équation de Navier--Stokes renormalisée

\[
 \partial_sZ-\Delta Z+\operatorname{div}(Z\otimes Z)+\nabla\Pi
 +\kappa(1+y\cdot\nabla)Z=F,\qquad \operatorname{div}Z=0,       \tag{1}
\]

sur \(\mathbb R^3\), soit \(\mathcal A\) la moyenne de Haar de l'action
covariante des rotations autour d'un axe fixe passant par l'origine. Posons

\[
 V=\mathcal AZ,\qquad W=(I-\mathcal A)Z,\qquad
 \overline F=\mathcal AF,\qquad F'=F-\overline F,              \tag{2}
\]

et, pour les scalaires,

\[
 \overline\Pi=\mathcal A_0\Pi,\qquad \pi'=\Pi-\overline\Pi.     \tag{3}
\]

La contrainte de Reynolds de Haar est

\[
 \mathscr R=\mathcal A_2(W\otimes W).                          \tag{4}
\]

Les équations exactes sont

\[
 \boxed{
 \begin{aligned}
 \partial_sV-\Delta V
 &+\operatorname{div}(V\otimes V+\mathscr R)
 +\nabla\overline\Pi
 +\kappa(1+y\cdot\nabla)V=\overline F,\\
 \operatorname{div}V&=0,
 \end{aligned}}                                                \tag{5}
\]

et

\[
 \boxed{
 \begin{aligned}
 \partial_sW-\Delta W
 &+\operatorname{div}\!\left(
 V\otimes W+W\otimes V+W\otimes W-\mathscr R\right)
 +\nabla\pi'\\
 &+\kappa(1+y\cdot\nabla)W=F',\\
 \operatorname{div}W&=0,\qquad \mathcal AW=0.
 \end{aligned}}                                                \tag{6}
\]

Pour des champs lisses et suffisamment décroissants, définissons

\[
 \mathcal T(s)=
 \int_{\mathbb R^3}\mathscr R:\nabla V\,dy
 =
 \int_{\mathbb R^3}(W\otimes W):\nabla V\,dy.                 \tag{7}
\]

Les budgets sont

\[
 \boxed{
 \frac12\frac d{ds}\|V\|_2^2+\|\nabla V\|_2^2
 -\frac\kappa2\|V\|_2^2
 =\langle\overline F,V\rangle+\mathcal T,}                    \tag{8}
\]

\[
 \boxed{
 \frac12\frac d{ds}\|W\|_2^2+\|\nabla W\|_2^2
 -\frac\kappa2\|W\|_2^2
 =\langle F',W\rangle-\mathcal T.}                            \tag{9}
\]

Ainsi \(\mathcal T>0\) transfère, selon cette convention, de l'énergie de la
fluctuation vers la moyenne; \(\mathcal T<0\) produit le transfert inverse.
Le tenseur \(\mathscr R\) est positif semi-défini, mais
\(\mathscr R:\nabla V\) n'a aucun signe. Le drift écrit au membre gauche de
(1) contribue \(-\kappa\|U\|_2^2/2\); déplacé au membre droit, il est une
source \(+\kappa\|U\|_2^2/2\).

Les identités globales (8)--(9) ne sont pas justifiées par une seule borne
faible-\(L^3\) ou par le ledger local d'une solution suitable. Dans ce cadre,
(5)--(6) restent des identités distributionnelles locales, tandis que les
budgets exigent coupures, mollification, contrôle de pression et analyse des
flux à l'infini.

## 1. Actions covariantes

Soit \(R_\theta=e^{\theta K}\), avec \(K^T=-K\), une rotation autour de
l'axe fixé. Les actions sur scalaires, vecteurs et tenseurs d'ordre deux
sont respectivement

\[
 \begin{aligned}
 (Q_\theta^{(0)}q)(y)
 &=q(R_{-\theta}y),\\
 (Q_\theta^{(1)}u)(y)
 &=R_\theta u(R_{-\theta}y),\\
 (Q_\theta^{(2)}T)(y)
 &=R_\theta T(R_{-\theta}y)R_\theta^T.
 \end{aligned}                                                \tag{10}
\]

Le contexte indiquera l'indice de \(Q_\theta\) et de
\(\mathcal A_j=(2\pi)^{-1}\int_0^{2\pi}Q_\theta^{(j)}\,d\theta\).
Les actions sont unitaires sur les espaces \(L^2\) correspondants. Chaque
\(\mathcal A_j\) est donc la projection orthogonale sur le sous-espace
invariant :

\[
 \mathcal A_j^2=\mathcal A_j,\qquad
 \mathcal A_j^*=\mathcal A_j,\qquad
 \|\mathcal A_j f\|_2\leq\|f\|_2.                            \tag{11}
\]

Ces formules s'étendent aux distributions par dualité. La compacité du
groupe permet de prendre la moyenne sans sommabilité angulaire
supplémentaire.

## 2. Commutations

Les rotations sont indépendantes de \(s\), orthogonales et centrées. Pour
des champs lisses, puis par dualité pour les distributions,

\[
 \begin{aligned}
 \partial_sQ_\theta^{(1)}u
 &=Q_\theta^{(1)}\partial_su,\\
 \Delta Q_\theta^{(1)}u
 &=Q_\theta^{(1)}\Delta u,\\
 \nabla Q_\theta^{(0)}q
 &=Q_\theta^{(1)}\nabla q,\\
 \operatorname{div}Q_\theta^{(1)}u
 &=Q_\theta^{(0)}\operatorname{div}u,\\
 \operatorname{div}Q_\theta^{(2)}T
 &=Q_\theta^{(1)}\operatorname{div}T,\\
 Q_\theta^{(1)}(y\cdot\nabla u)
 &=y\cdot\nabla Q_\theta^{(1)}u.
 \end{aligned}                                                \tag{12}
\]

En particulier,

\[
 \begin{aligned}
 \partial_s\mathcal A_1&=\mathcal A_1\partial_s,&
 \Delta\mathcal A_1&=\mathcal A_1\Delta,\\
 \nabla\mathcal A_0&=\mathcal A_1\nabla,&
 \operatorname{div}\mathcal A_2&=\mathcal A_1\operatorname{div},\\
 (y\cdot\nabla)\mathcal A_1&=\mathcal A_1(y\cdot\nabla).
 \end{aligned}                                                \tag{13}
\]

La moyenne préserve donc la divergence nulle :

\[
 \operatorname{div}V=\mathcal A_0\operatorname{div}Z=0,\qquad
 \operatorname{div}W=0.                                      \tag{14}
\]

L'égalité de commutation avec \(y\cdot\nabla\) échouerait sous cette forme
pour une rotation autour d'un centre mobile ou différent de l'origine. Une
action dépendant du temps ajouterait également un terme de générateur dans
la première ligne de (12).

## 3. Décomposition exacte du tenseur convectif

L'action tensorielle respecte les produits :

\[
 Q_\theta^{(2)}(u\otimes v)
 =(Q_\theta^{(1)}u)\otimes(Q_\theta^{(1)}v).                  \tag{15}
\]

Comme \(\mathcal A_1V=V\) et \(\mathcal A_1W=0\),

\[
 \begin{aligned}
 \mathcal A_2(V\otimes V)&=V\otimes V,\\
 \mathcal A_2(V\otimes W)
 &=V\otimes\mathcal A_1W=0,\\
 \mathcal A_2(W\otimes V)
 &=(\mathcal A_1W)\otimes V=0.
 \end{aligned}                                                \tag{16}
\]

Il ne faut pas factoriser le dernier terme :

\[
 \mathcal A_2(W\otimes W)=\mathscr R
 \neq(\mathcal A_1W)\otimes(\mathcal A_1W)=0
 \quad\text{en général}.                                      \tag{17}
\]

Par conséquent,

\[
 \mathcal A_2(Z\otimes Z)=V\otimes V+\mathscr R.              \tag{18}
\]

Le tenseur \(\mathscr R\) est symétrique, invariant et positif
semi-défini point par point :

\[
 \xi^T\mathscr R(y)\xi
 =\frac1{2\pi}\int_0^{2\pi}
   \left|\xi\cdot Q_\theta^{(1)}W(y)\right|^2d\theta\geq0.     \tag{19}
\]

Sa trace vaut

\[
 \operatorname{tr}\mathscr R
 =\mathcal A_0(|W|^2).                                        \tag{20}
\]

La positivité de (19) ne donne aucun signe à sa contraction avec la partie
sans trace du gradient de \(V\).

## 4. Équations moyenne et fluctuation

Appliquons \(\mathcal A_1\) à (1). Les commutations (13) et l'identité
(18) donnent (5), avec

\[
 \overline\Pi=\mathcal A_0\Pi,\qquad
 \overline F=\mathcal A_1F.                                  \tag{21}
\]

Soustraire (5) de (1) et développer

\[
 Z\otimes Z
 =V\otimes V+V\otimes W+W\otimes V+W\otimes W                \tag{22}
\]

donne (6). Les deux termes croisés sont présents dans l'équation de
fluctuation même si leur moyenne est nulle. Avec la convention
\((u\otimes v)_{ij}=u_iv_j\),

\[
 \begin{aligned}
 \operatorname{div}(V\otimes W)&=(W\cdot\nabla)V,\\
 \operatorname{div}(W\otimes V)&=(V\cdot\nabla)W,
 \end{aligned}                                                \tag{23}
\]

car \(V\) et \(W\) sont divergence-free.

Les équations sont fermées algébriquement pour le couple \((V,W)\), mais
l'équation de \(V\) seule ne l'est pas : \(\mathscr R\) dépend de la
fluctuation complète.

## 5. Pression et projection de Leray

En prenant la divergence de (1), le drift ne contribue pas, car

\[
 \operatorname{div}(y\cdot\nabla Z)
 =y\cdot\nabla\operatorname{div}Z+\operatorname{div}Z=0.      \tag{24}
\]

Ainsi

\[
 -\Delta\Pi
 =\partial_i\partial_j(Z_iZ_j)-\operatorname{div}F.            \tag{25}
\]

La pression moyenne satisfait

\[
 -\Delta\overline\Pi
 =\partial_i\partial_j
   (V_iV_j+\mathscr R_{ij})
 -\operatorname{div}\overline F,                              \tag{26}
\]

et la pression fluctuante

\[
 \begin{aligned}
 -\Delta\pi'
 ={}&\partial_i\partial_j\big(
 V_iW_j+W_iV_j+W_iW_j-\mathscr R_{ij}\big)\\
 &-\operatorname{div}F'.                                     \tag{27}
 \end{aligned}
\]

Si \(F\) est divergence-free et la jauge globale de Riesz est admissible,

\[
 \begin{aligned}
 \overline\Pi
 &=R_iR_j(V_iV_j+\mathscr R_{ij}),\\
 \pi'
 &=R_iR_j\big(
 V_iW_j+W_iV_j+W_iW_j-\mathscr R_{ij}\big),
 \end{aligned}                                                \tag{28}
\]

à une fonction du temps près. La covariance isotrope des transformées de
Riesz implique que la moyenne de Haar commute avec cette reconstruction.

Sur \(\mathbb R^3\), la projection de Leray

\[
 \mathbb P=I-\nabla\Delta^{-1}\operatorname{div}              \tag{29}
\]

est un multiplicateur de Fourier isotrope et homogène de degré zéro. Elle
commute avec les rotations, la moyenne de Haar, les dérivées constantes et
le générateur de dilatation. Les formes sans pression sont donc

\[
 \begin{aligned}
 \partial_sV-\Delta V
 &+\mathbb P\operatorname{div}(V\otimes V+\mathscr R)
 +\kappa(1+y\cdot\nabla)V=\mathbb P\overline F,\\
 \partial_sW-\Delta W
 &+\mathbb P\operatorname{div}\big(
 V\otimes W+W\otimes V+W\otimes W-\mathscr R\big)\\
 &+\kappa(1+y\cdot\nabla)W=\mathbb PF'.
 \end{aligned}                                                \tag{30}
\]

Une projection de Leray locale sur une boule dépend de la frontière et ne
se substitue pas automatiquement à (29). Dans une formulation uniquement
locale, la pression possède une composante harmonique et sa moyenne doit
être suivie séparément.

## 6. Orthogonalités utiles

Pour des champs dans \(L^2(\mathbb R^3)\), \(\mathcal A_j\) est
orthogonale. Par conséquent,

\[
 (V,W)_{L^2}=0,\qquad
 \|Z\|_2^2=\|V\|_2^2+\|W\|_2^2.                              \tag{31}
\]

La covariance du gradient donne

\[
 \mathcal A_2(\nabla W)=\nabla\mathcal A_1W=0,\qquad
 \mathcal A_2(\nabla V)=\nabla V.                             \tag{32}
\]

Ainsi

\[
 (\nabla V,\nabla W)_{L^2}=0,\qquad
 \|\nabla Z\|_2^2
 =\|\nabla V\|_2^2+\|\nabla W\|_2^2.                          \tag{33}
\]

Si \(F\in L^2\), la même orthogonalité donne

\[
 \langle F,Z\rangle
 =\langle\overline F,V\rangle+\langle F',W\rangle.            \tag{34}
\]

Enfin, puisque \(\mathscr R\) est invariant et \(\nabla W\) a moyenne
nulle,

\[
 \int_{\mathbb R^3}\mathscr R:\nabla W\,dy=0.                 \tag{35}
\]

L'auto-adjonction de \(\mathcal A_2\) et l'invariance de \(\nabla V\)
donnent

\[
 \int_{\mathbb R^3}\mathscr R:\nabla V\,dy
 =
 \int_{\mathbb R^3}(W\otimes W):\nabla V\,dy.                 \tag{36}
\]

## 7. Identité d'énergie de la moyenne

Supposons dans cette section \(Z,\Pi,F\) lisses et assez décroissants pour
justifier toutes les intégrations par parties; des champs de Schwartz
suffisent. Multiplions (5) par \(V\) et intégrons.

Les termes temporel et visqueux donnent

\[
 \int V\cdot\partial_sV
 =\frac12\frac d{ds}\|V\|_2^2,\qquad
 -\int V\cdot\Delta V=\|\nabla V\|_2^2.                      \tag{37}
\]

L'advection propre et la pression s'annulent :

\[
 \int V\cdot\operatorname{div}(V\otimes V)=0,\qquad
 \int V\cdot\nabla\overline\Pi=0.                             \tag{38}
\]

Le tenseur de Reynolds donne

\[
 \int V\cdot\operatorname{div}\mathscr R
 =-\int\mathscr R:\nabla V=-\mathcal T.                       \tag{39}
\]

En dimension trois,

\[
 \begin{aligned}
 \int V\cdot(1+y\cdot\nabla)V
 &=\|V\|_2^2+\frac12\int y\cdot\nabla|V|^2\\
 &=\left(1-\frac32\right)\|V\|_2^2
 =-\frac12\|V\|_2^2.
 \end{aligned}                                                \tag{40}
\]

En rassemblant (37)--(40), on obtient d'abord

\[
 \frac12\frac d{ds}\|V\|_2^2+\|\nabla V\|_2^2
 -\frac\kappa2\|V\|_2^2-\mathcal T
 =\langle\overline F,V\rangle,
\]

puis la forme (8). Le signe \(+\mathcal T\) au membre droit de (8) est donc
fixé par la convention (7).

## 8. Identité d'énergie de la fluctuation

Multiplions (6) par \(W\). Le transport par \(V\) s'annule :

\[
 \int W\cdot(V\cdot\nabla)W=0.                               \tag{41}
\]

L'autre terme croisé vaut

\[
 \int W\cdot(W\cdot\nabla)V
 =\int(W\otimes W):\nabla V=\mathcal T.                       \tag{42}
\]

L'auto-advection de \(W\), la pression et la contrainte soustraite donnent

\[
 \begin{aligned}
 \int W\cdot\operatorname{div}(W\otimes W)&=0,\\
 \int W\cdot\nabla\pi'&=0,\\
 -\int W\cdot\operatorname{div}\mathscr R
 &=\int\mathscr R:\nabla W=0,
 \end{aligned}                                                \tag{43}
\]

où la dernière égalité est (35). Le drift donne encore
\(-\|W\|_2^2/2\). On obtient

\[
 \frac12\frac d{ds}\|W\|_2^2+\|\nabla W\|_2^2
 -\frac\kappa2\|W\|_2^2+\mathcal T
 =\langle F',W\rangle,
\]

soit (9). Le transfert apparaît avec le signe opposé à celui de (8).

## 9. Budget total et contrôle des signes

En additionnant (8) et (9), \(\mathcal T\) s'annule. Les orthogonalités
(31), (33) et (34) donnent

\[
 \boxed{
 \frac12\frac d{ds}\|Z\|_2^2+\|\nabla Z\|_2^2
 -\frac\kappa2\|Z\|_2^2
 =\langle F,Z\rangle.}                                       \tag{44}
\]

C'est exactement l'identité obtenue directement depuis (1). Ce test
indépendant fixe simultanément les deux signes de transfert et le signe du
drift.

Le terme de drift a, en dimension \(d\), le coefficient général

\[
 \int U\cdot(1+y\cdot\nabla)U
 =\left(1-\frac d2\right)\|U\|_2^2.                           \tag{45}
\]

Pour \(d=3\), il vaut \(-\|U\|_2^2/2\) au membre gauche. L'appeler
« dissipatif » sans préciser de quel côté de l'équation il est placé
inverserait le bilan : dans la forme

\[
 \frac12E'(s)+D(s)
 =\frac\kappa2E(s)+\langle F,U\rangle,
\]

le drift est une source d'énergie renormalisée.

Bien que \(\mathscr R\geq0\), seul le tenseur de déformation

\[
 S(V)=\frac12(\nabla V+\nabla V^T)
\]

contribue à \(\mathcal T\), car \(\mathscr R\) est symétrique. Comme
\(\operatorname{tr}S(V)=0\), ni positivité ni partie isotrope de
\(\mathscr R\) ne fixent le signe de
\(\mathscr R:S(V)\).

## 10. Portée distributionnelle et faible-\(L^3\)

### 10.1 Ce qui reste exact

Si

\[
 Z\in L^\infty_{\mathrm{loc}}
   (J;L^{3,\infty}(\mathbb R^3))
\]

et (1) vaut dans les distributions avec un ledger de pression compatible,
la moyenne de Haar est bien définie sur les distributions et bornée sur les
espaces de Lorentz concernés. On conserve

\[
 V=\mathcal AZ,\qquad W=(I-\mathcal A)Z,\qquad
 \mathcal AW=0,
\]

ainsi que toutes les commutations (13). Le produit vérifie

\[
 Z\otimes Z\in L^{3/2,\infty}(\mathbb R^3),
\]

et appartient localement à \(L^p\) pour tout \(1\leq p<3/2\). Les équations
(5)--(6) ont donc un sens distributionnel local. Dans la jauge globale de
Riesz, les pressions de (28) appartiennent formellement au même espace de
Lorentz, sous les hypothèses globales permettant cette reconstruction.

### 10.2 Ce qui ne suit pas

Une borne \(L^{3,\infty}(\mathbb R^3)\) n'implique pas
\(L^2(\mathbb R^3)\). Par conséquent :

- les énergies globales de \(Z,V,W\) peuvent être infinies;
- les orthogonalités (31)--(34) ne donnent pas de budgets finis;
- l'intégrale \(\mathcal T\) de (7) peut ne pas être définie;
- l'intégration par parties du drift peut laisser un flux à l'infini;
- la pression globale ne peut pas être écartée sans vérifier ses queues.

Même pour une solution suitable avec

\[
 Z\in L^\infty_{\mathrm{loc}}(J;L^2_{\mathrm{loc}})
 \cap L^2_{\mathrm{loc}}(J;H^1_{\mathrm{loc}}),
\]

l'inégalité locale d'énergie de \(Z\) ne se scinde pas automatiquement en
deux égalités pour \(V\) et \(W\). Tester leurs équations exige une
régularisation temporelle et spatiale; les coupures créent :

- des flux convectifs à travers leur support;
- des termes de pression;
- des commutateurs de localisation avec \(\mathcal A\) si la coupure n'est
  pas axisymétrique;
- des termes de drift sur le bord de la coupure;
- un éventuel défaut dans le passage à la limite des produits cubiques.

Une coupure radiale centrée commute avec \(\mathcal A\), mais ne supprime ni
le flux de pression ni le flux à l'infini. La semi-continuité de la
dissipation fournit en général une inégalité, pas les égalités (8)--(9).

### 10.3 Niveau minimal pour les budgets

Les identités globales précédentes sont sûres, par exemple, sous

\[
 V,W\in C^1_s\mathcal S_y(\mathbb R^3)^3,\qquad
 \Pi,\overline\Pi,\pi',F\text{ suffisamment décroissants}.
\]

Elles peuvent être étendues par densité à des classes d'énergie si :

1. \(V,W\in L^\infty_sL^2_y\cap L^2_sH^1_y\);
2. les équations moyenne et fluctuation sont valides dans les duaux
   correspondants;
3. les produits convectifs et \(\mathcal T\) sont intégrables;
4. les traces temporelles autorisent le test par \(V,W\);
5. les flux de pression et de drift à l'infini s'annulent.

Ces cinq propriétés ne sont pas contenues dans la seule hypothèse
faible-\(L^3\).

## 11. Passe contradictoire

1. **Mauvaise action sur les tenseurs.** Moyenner chaque composante sans les
   deux facteurs \(R_\theta\) de (10) détruit la covariance de la divergence.
2. **Factorisation illicite.**
   \(\mathcal A_2(W\otimes W)\neq\mathcal AW\otimes\mathcal AW\).
3. **Termes croisés oubliés.** Ils disparaissent de (5), mais restent tous
   deux dans (6).
4. **Convention tensorielle.** Avec
   \((u\otimes v)_{ij}=u_iv_j\), les identités (23) fixent quel terme produit
   \(\mathcal T\).
5. **Pression moyenne.** Elle dépend de \(V\otimes V+\mathscr R\), pas de
   \(V\otimes V\) seul.
6. **Leray local.** La projection globale est non locale; une formulation
   sur boule possède des conditions de bord et une pression harmonique.
7. **Positivité.** \(\mathscr R\geq0\) ne donne aucun signe au transfert.
8. **Signe du transfert.** L'addition des budgets doit annuler
   \(\mathcal T\); sinon un signe a été inversé.
9. **Signe du drift.** En dimension trois,
   \(\int U\cdot(1+y\cdot\nabla)U=-\|U\|_2^2/2\). Le drift est une source
   lorsqu'il est déplacé au membre droit.
10. **Orthogonalité du gradient.** Elle utilise la covariance tensorielle de
    \(\nabla\), pas seulement \(\mathcal AW=0\).
11. **Contrainte dans le budget fluctuant.**
    \(\int\mathscr R:\nabla W=0\) requiert l'intégrabilité globale ou une
    justification par coupures.
12. **Faible-\(L^3\).** Cette classe ne fournit pas une énergie globale
    finie et ne justifie aucune des intégrations par parties de (8)--(9).
13. **Suitability.** L'inégalité locale d'énergie du champ total n'implique
    pas deux égalités séparées après projection.
14. **Portée Clay.** La décomposition est une identité structurelle. Elle ne
    borne ni \(\mathscr R\), ni \(\mathcal T\), ni une norme critique.

## 12. Statut logique

| Affirmation | Statut |
|---|---|
| commutations (12)--(13) | **PROUVÉ** par covariance des rotations centrées |
| moyenne des termes croisés égale à zéro | **PROUVÉ** par (15)--(16) |
| système moyen (5) | **PROUVÉ** au sens classique ou distributionnel |
| système fluctuant (6) | **PROUVÉ** par soustraction exacte |
| pression moyenne contient \(\mathscr R\) | **PROUVÉ** par (25)--(28) |
| formulation de Leray (30) | **PROUVÉ** sur \(\mathbb R^3\) lorsque \(\mathbb P\) est définie |
| \(\mathscr R\) positif semi-défini | **PROUVÉ** par (19) |
| identités d'énergie (8)--(9) | **PROUVÉ** pour champs lisses décroissants |
| transferts opposés | **PROUVÉ** et contrôlé par le budget total (44) |
| signe du drift | **PROUVÉ** par (40) et (45) |
| budgets globaux sous seule borne faible-\(L^3\) | **NON JUSTIFIÉ** |
| fermeture de l'équation moyenne par signe de \(\mathscr R\) | **RÉFUTÉ** : \(\mathcal T\) est indéfini en signe |
| décomposition Haar \(\Rightarrow\) régularité Clay | **NON DÉMONTRÉ** |

**Décision formelle : CONTINUER.** Le système exact (5)--(6) isole le verrou
dans la contrainte \(\mathscr R\) et le transfert signé \(\mathcal T\). Une
expérience ou un lemme utile doit contrôler ce transfert dans une quantité
critique, avec localisation et pression suivies; la positivité de
\(\mathscr R\) seule est insuffisante.
