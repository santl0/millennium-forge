# Cycle 0055 — réduction par rotation relative et frontières d'hypothèses

Date d'exécution : 2026-08-15

## Verdict

Pour une équation autonome

\[
u_s+F(u)=0
\]

équivariante sous une action \(SO(2)\), un ansatz de rotation relative

\[
u(s)=Q_{\theta(s)}U
\]

se réduit exactement à

\[
\boxed{\beta(s)RU+F(U)=0,\qquad \beta=\theta'.}
\]

Si le profil \(U\) est fixe, l'opérateur réellement autonome et l'équation exacte, la soustraction à deux temps donne la dichotomie rigoureuse :

\[
\boxed{\beta\ \text{est constante},\quad\text{ou}\quad RU=0.}
\]

Dans le second cas, l'orbite est stationnaire et la réduction impose \(F(U)=0\). Dans le premier, on obtient seulement une **relative equilibrium** à vitesse angulaire constante ; elle n'est pas nécessairement stationnaire.

Les contre-modèles exacts montrent que les conclusions approchées exigent en plus : autonomie uniforme, petit résidu dans une norme identifiée, minoration de \(\|RU\|\), borne sur \(\beta\), compacité des profils et continuité de \(F\) près du sous-espace fixe. Aucun opérateur construit ci-dessous n'est l'opérateur de Navier–Stokes.

## 1. Action rationnelle de \(SO(2)\)

Sur \(H=\mathbb R^3\), considérons la rotation du plan \((x_1,x_2)\) laissant l'axe \(e_3\) fixe :

\[
Q_{c,s}=
\begin{pmatrix}
c&-s&0\\
s&c&0\\
0&0&1
\end{pmatrix},
\qquad
c^2+s^2=1.
\]

Son générateur est

\[
R=
\begin{pmatrix}
0&-1&0\\
1&0&0\\
0&0&0
\end{pmatrix}.
\]

Les identités structurales sont

\[
Q^TQ=I,
\qquad
\det Q=1,
\qquad
QR=RQ,
\qquad
\frac{d}{d\theta}Q_\theta=Q_\theta R.
\]

Le script utilise la paramétrisation rationnelle

\[
c=\frac{1-t^2}{1+t^2},
\qquad
s=\frac{2t}{1+t^2},
\qquad
t\in\mathbb Q,
\]

et vérifie exactement orthogonalité, déterminant, composition, préservation de norme et commutation avec \(R\). L'échantillonnage rationnel certifie le programme ; les identités matricielles affichées constituent la preuve pour tout angle réel.

## 2. Réduction autonome équivariante

Supposons

\[
F(Q_\theta x)=Q_\theta F(x)
\]

et posons \(u(s)=Q_{\theta(s)}U\), avec \(U\) indépendant de \(s\). Alors

\[
u_s=\beta(s)Q_{\theta(s)}RU,
\]

et

\[
F(u)=Q_{\theta(s)}F(U).
\]

Puisque \(Q_\theta\) est inversible,

\[
u_s+F(u)=0
\quad\Longleftrightarrow\quad
\beta(s)RU+F(U)=0.
\]

Pour deux temps \(s_1,s_2\),

\[
[\beta(s_1)-\beta(s_2)]RU=0.
\]

Si \(RU\ne0\), alors \(\beta(s_1)=\beta(s_2)\) pour tous les temps : \(\beta\) est constante. Si \(RU=0\), alors

\[
Q_\theta U=U
\]

pour tout \(\theta\), et la réduction devient \(F(U)=0\). L'orbite est véritablement stationnaire.

Le certificat teste également les opérateurs équivariants

\[
F_\omega(x)=-\omega Rx
\]

et

\[
F_{\mathrm{poly}}(x)=-\|x\|^2Rx.
\]

Pour \(F_\omega\), tout profil ayant \(RU\ne0\) donne une relative equilibrium exacte avec \(\beta=\omega\).

## 3. Ce que la dichotomie exacte ne dit pas

La branche \(\beta=\beta_0\ne0\) donne

\[
u(s)=Q_{\beta_0s+\theta_0}U.
\]

Cette orbite est périodique modulo \(2\pi\), récurrente et non stationnaire lorsque \(RU\ne0\). Exclure cette branche exige un théorème de rigidité supplémentaire : décroissance, condition de phase, absence de rotating waves, intégrabilité du générateur, ou autre structure PDE.

Ainsi, même dans le cas exact, « vitesse constante » ne doit jamais être remplacé par « vitesse nulle » sans argument séparé.

## 4. Contre-modèle sans autonomie

Fixons un profil \(U\) avec \(RU\ne0\), et choisissons une fonction arbitraire \(\beta(s)\). Définissons l'opérateur dépendant du temps

\[
F_s(x)=-\beta(s)Rx.
\]

Chaque \(F_s\) est équivariant sous \(SO(2)\), mais la famille n'est pas autonome. On a exactement

\[
\beta(s)RU+F_s(U)=0
\]

pour toute fonction \(\beta\), constante ou non.

La soustraction à deux temps échoue parce que les termes \(F_{s_1}(U)\) et \(F_{s_2}(U)\) ne sont plus identiques. L'équivariante instantanée ne remplace donc pas l'autonomie.

## 5. Résidu \(\varepsilon\) : conclusion quantitative seulement

Supposons maintenant

\[
\beta(s)RU+F(U)=r(s),
\qquad
\|r(s)\|\le\varepsilon.
\]

La soustraction donne

\[
[\beta(s)-\beta(t)]RU=r(s)-r(t),
\]

d'où

\[
\boxed{
|\beta(s)-\beta(t)|\,\|RU\|
\le2\varepsilon.}
\tag{1}
\]

Si \(\|RU\|\ge c>0\), on obtient

\[
|\beta(s)-\beta(t)|\le\frac{2\varepsilon}{c}.
\]

Cette borne est optimale au niveau algébrique. Pour \(U=e_1\), \(\|RU\|=1\), fixons \(F(U)=-\beta_0RU\) et prenons

\[
\beta_\pm=\beta_0\pm\varepsilon.
\]

Les deux résidus ont exactement la norme \(\varepsilon\), tandis que

\[
|\beta_+-\beta_-|=2\varepsilon.
\]

Un résidu petit ne donne donc pas une constance exacte.

## 6. Dégénérescence du générateur

Prenons

\[
U_\varepsilon=\varepsilon e_1,
\qquad
F(U_\varepsilon)=0,
\qquad
\beta_+=1,
\quad
\beta_-=-1.
\]

Alors

\[
\|RU_\varepsilon\|=\varepsilon,
\]

et les deux résidus ont la norme \(\varepsilon\), bien que

\[
|\beta_+-\beta_-|=2.
\]

Lorsque \(\varepsilon\to0\), les résidus tendent vers zéro sans que les vitesses se rapprochent. L'estimation (1) devient vide précisément parce que \(U_\varepsilon\) approche le sous-espace fixe \(\ker R\).

Une conclusion uniforme exige donc soit \(\|RU\|\ge c\), soit une formulation quotientant correctement l'isotropie et contrôlant la distance au sous-espace fixe.

## 7. Vitesses non bornées : deux mécanismes distincts

### 7.1 Perte de compacité du profil

Pour l'opérateur polynomial lisse, autonome et équivariant

\[
F_{\mathrm{poly}}(x)=-\|x\|^2Rx,
\]

choisissons

\[
U_n=ne_1,
\qquad
\beta_n=n^2.
\]

Alors

\[
\beta_nRU_n+F_{\mathrm{poly}}(U_n)=0
\]

exactement, mais \(\beta_n\to\infty\). Il n'y a aucune contradiction avec la dichotomie : chaque orbite possède une vitesse constante. C'est l'uniformité sur la famille qui échoue, avec \(\|U_n\|\to\infty\).

### 7.2 Approche singulière du sous-espace fixe

Sur \(H\setminus\ker R\), considérons l'opérateur autonome équivariant

\[
F_{\mathrm{sing}}(x)=-\frac{Rx}{\|Rx\|}.
\]

Pour

\[
U_n=\frac1n e_1,
\qquad
\beta_n=n,
\]

on a

\[
\beta_nRU_n=e_2,
\qquad
F_{\mathrm{sing}}(U_n)=-e_2.
\]

La réduction est exacte, \(U_n\to0\in\ker R\) et \(RU_n\to0\), mais

\[
\|\beta_nRU_n\|=1.
\]

Ce contre-modèle perd volontairement la continuité de \(F\) au sous-espace fixe. Il montre pourquoi cette continuité — avec une norme et un taux uniformes — doit être démontrée avant de passer à la limite. Il ne réfute aucune conclusion disposant déjà de cette hypothèse.

## 8. Registre exact des hypothèses

| Hypothèse | Rôle dans la preuve | Échec si elle manque |
|---|---|---|
| profil \(U\) indépendant du temps | permet de soustraire le même \(RU\) | modulation du profil non traitée |
| autonomie de \(F\) | garantit le même \(F(U)\) à deux temps | \(F_s=-\beta(s)R\) suit toute vitesse |
| équivariance exacte | factorise \(Q_\theta\) | termes de commutateur supplémentaires |
| équation exacte | donne la dichotomie algébrique | résidu \(\varepsilon\) : seulement (1) |
| \(\|RU\|\ge c>0\) | stabilise la division par le générateur | vitesses séparées avec résidus petits |
| borne sur \(\beta\) | contrôle \(\beta RU\) lorsque \(RU\to0\) | produit d'ordre un malgré \(RU\to0\) |
| compacité de \(U\) | borne les vitesses pour des opérateurs réguliers | exemple polynomial \(U_n=ne_1\) |
| continuité de \(F\) au sous-espace fixe | permet le passage à la limite | exemple singulier \(F_{\mathrm{sing}}\) |

## 9. Séparation stricte avec Navier–Stokes

Les espaces et opérateurs du certificat sont de dimension trois. Ils ne représentent ni la projection de Leray, ni la pression, ni le Laplacien, ni le terme quadratique de Navier–Stokes.

Pour appliquer la réduction à une vraie solution Navier–Stokes, il faudrait vérifier séparément :

1. que l'action choisie est une symétrie continue du domaine et des conditions aux limites ;
2. que la solution appartient au domaine du générateur de rotation, généralement non borné sur un espace de fonctions ;
3. que pression et projection de Leray sont équivariantes dans la classe considérée ;
4. que l'opérateur renormalisé est réellement autonome — une remise à l'échelle peut introduire une dépendance explicite en temps ;
5. que le résidu converge dans une topologie permettant le passage au terme quadratique ;
6. que \(\beta\), \(RU\) et les constantes de continuité sont uniformément contrôlés ;
7. qu'une relative equilibrium à \(\beta\ne0\) est exclue par un théorème de rigidité propre à la PDE.

Sur le tore cubique, les rotations spatiales arbitraires ne préservent pas le réseau \(\mathbb Z^3\) ; l'action rationnelle abstraite ci-dessus n'est donc pas une action spatiale \(SO(2)\) de \(\mathbb T^3\). Sur \(\mathbb R^3\), les rotations existent, mais les questions de domaine, décroissance, espaces critiques et pression restent entières.

Aucune solution ancienne, suitable, Leray–Hopf ou classique n'est construite. Aucun résultat de régularité ou de blow-up pour le problème Clay n'est revendiqué.

## 10. Reproduction et certificat

Commande :

```powershell
python -B experiments/navier-stokes/relative-rotation/relative_rotation_audit.py
```

Sortie validée :

```text
relative_rotation_audit: PASS
exact_assertions=960
action=exact_rational_SO2_on_Q3_with_generator_R
reduction=beta(s)*R*U+F(U)=0_for_autonomous_equivariant_F
dichotomy=beta_constant_or_RU_zero_and_orbit_stationary
nonautonomous=time-dependent_equivariant_F_tracks_arbitrary_beta
residual=epsilon_gives_only_quantitative_beta_control_if_||RU||>=c
degeneracy=beta_unbounded_times_RU_vanishing_can_stay_order_one
scope=abstract_finite-dimensional_models; no Navier-Stokes claim
```

Le script utilise uniquement la bibliothèque standard et `Fraction`. Les 960 assertions vérifient l'action de groupe, l'équivariance, la réduction, la dichotomie, les bornes de résidu et les contre-modèles multi-échelles. Résidu rationnel : zéro ; aucune approximation flottante.

Empreinte SHA-256 du script validé :

```text
c9a2ca834951ea18ac5fca89d06d24cd73601181b99268a50f1749f21c9bb207
```

## Décision contradictoire

**CONSERVER** la dichotomie exacte sous autonomie, équivariance, profil fixe et équation exacte. **RÉVISER** toute version approchée pour y inscrire explicitement la norme du résidu, une minoration ou un quotient du générateur, une borne de \(\beta\), la compacité des profils et la continuité de l'opérateur. **NE PAS TRANSFÉRER** la conclusion à Navier–Stokes avant vérification des sept portes PDE ci-dessus.
