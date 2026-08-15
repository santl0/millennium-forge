# Cycle 0056 — fermeture d'une orbite asymptotiquement rotationnelle

Date : 2026-08-15.

Statut : `AI_INTERNAL_DERIVATION`; lemme de passage à la limite et de
reconstruction de phase. Aucun résultat Clay. Les passages de suitability et
de pression sont conditionnels aux bornes uniformes explicitées ci-dessous.

## Verdict

Le cœur cinématique du lemme est **vrai**. Soit \(I\subset\mathbb R\) un
intervalle connexe et soit \(\mathcal R\) le générateur d'un sous-groupe fixe
de rotations autour d'un axe passant par l'origine. Supposons

\[
 Z_n\longrightarrow Z
 \quad\text{fortement dans }L^3_{\rm loc}(I\times\mathbb R^3),             \tag{1}
\]

\[
 \sup_n\|\beta_n\|_{L^\infty(I)}\leq M_\beta,                            \tag{2}
\]

et

\[
 r_n:=\partial_sZ_n-\beta_n\mathcal RZ_n
 \longrightarrow0
 \quad\text{dans }\mathcal D'(I\times\mathbb R^3).                       \tag{3}
\]

Après extraction,

\[
 \beta_n\stackrel{*}{\rightharpoonup}\beta
 \quad\text{dans }L^\infty(I),qquad
 \|\beta\|_\infty\leq M_\beta,                                          \tag{4}
\]

et

\[
 \boxed{
 \beta_n\mathcal RZ_n\longrightarrow\beta\mathcal RZ
 \quad\text{dans }\mathcal D'(I\times\mathbb R^3).}                     \tag{5}
\]

Par conséquent,

\[
 \boxed{\partial_sZ=\beta(s)\mathcal RZ}                                 \tag{6}
\]

dans les distributions. Pour tout \(s_0\in I\), la phase

\[
 \theta(s)=\theta_0+\int_{s_0}^s\beta(\sigma)\,d\sigma                   \tag{7}
\]

appartient à \(W^{1,\infty}(I)\), avec \(\theta'=\beta\) presque partout,
et il existe une distribution spatiale fixe \(U\) telle que

\[
 \boxed{Z(s)=Q_{\theta(s)}U}                                               \tag{8}
\]

pour presque tout \(s\), donc dans \(\mathcal D'(I\times\mathbb R^3)\).

Si \(Z\) est en outre une solution distributionnelle de l'équation
Navier--Stokes renormalisée autonome, dans la formulation projetée ou avec
pression de Riesz, le cycle 0055 s'applique :

\[
 \mathcal RU=0\Longrightarrow Z\text{ stationnaire},                      \tag{9}
\]

tandis que

\[
 \mathcal RU\neq0\Longrightarrow
 \beta(s)=\alpha\text{ p.p., }\theta(s)=\alpha s+\theta_0,
 \quad Z\text{ RSS exacte}.                                               \tag{10}
\]

La faille se situe ailleurs : le fait que chaque \(Z_n\) soit suitable ne
donne pas, à lui seul, des bornes locales uniformes en \(n\). Sans un ledger
uniforme d'énergie, de dissipation et de pression, (1) suffit au passage de
l'équation contre les tests solénoïdaux, mais ne suffit pas à conclure que
\(Z\) est suitable ni que \(U\in W^{1,2}_{\rm loc}\).

## 1. Action de rotation et adjoint du générateur

Fixons une matrice antisymétrique \(A\) et
\(R_\gamma=e^{\gamma A}\). Avec la convention du cycle 0055,

\[
 (Q_\gamma W)(y)=R_\gamma W(R_{-\gamma}y),qquad
 \mathcal RW=AW-(Ay\cdot\nabla)W.                                        \tag{11}
\]

Pour une distribution vectorielle, le générateur est défini par

\[
 \langle\mathcal RW,\varphi\rangle
 =\langle W,\mathcal R^*\varphi\rangle,qquad
 \mathcal R^*\varphi=(Ay\cdot\nabla)\varphi-A\varphi.                    \tag{12}
\]

Le coefficient \(Ay\) est borné sur tout compact spatial. Ainsi, pour un
test espace-temps \(\Phi\), \(\mathcal R^*\Phi\) est encore lisse et de même
support compact. Cette intégration par parties est le mécanisme qui évite de
demander une convergence forte des gradients de \(Z_n\).

Le produit \(\beta_n\mathcal RZ_n\) est bien défini comme distribution par

\[
 \langle\beta_n\mathcal RZ_n,\Phi\rangle
 =\int_I\beta_n(s)
   \langle Z_n(s),\mathcal R^*\Phi(s)\rangle\,ds.                          \tag{13}
\]

Le membre droit est intégrable dès que \(Z_n\in L^1_{\rm loc}\) et
\(\beta_n\in L^\infty\). La forte \(L^3_{\rm loc}\) de (1) est donc plus
que suffisante.

## 2. Extraction faible-étoile de \(\beta_n\)

L'espace \(L^1(I)\) est séparable, y compris lorsque \(I\) est non borné.
La bornitude (2), Banach--Alaoglu et la métrisabilité faible-étoile de la
boule sur les suites donnent une sous-suite, non renommée, satisfaisant (4).

Le quantificateur est global : une même sous-suite est utilisée pour tous les
tests espace-temps. Si l'on ne disposait que de
\(\sup_n\|\beta_n\|_{L^\infty(J)}<\infty\) pour chaque
\(J\Subset I\), il faudrait une diagonale sur une exhaustion de \(I\), et la
conclusion serait seulement \(\beta\in L^\infty_{\rm loc}(I)\), donc
\(\theta\in W^{1,\infty}_{\rm loc}\).

## 3. Produit faible–fort

Soit \(K\Subset I\times\mathbb R^3\) contenant le support de \(\Phi\).
Décomposons

\[
\begin{aligned}
 \langle\beta_n\mathcal RZ_n-\beta\mathcal RZ,\Phi\rangle
 ={}&\langle\beta_n\mathcal R(Z_n-Z),\Phi\rangle\\
 &+\langle(\beta_n-\beta)\mathcal RZ,\Phi\rangle.                         \tag{14}
\end{aligned}
\]

Pour le premier terme, (12) et Hölder donnent

\[
 \left|\langle\beta_n\mathcal R(Z_n-Z),\Phi\rangle\right|
 \leq M_\beta
 \|Z_n-Z\|_{L^3(K)}
 \|\mathcal R^*\Phi\|_{L^{3/2}(K)}\longrightarrow0.                    \tag{15}
\]

Pour le second, posons

\[
 g_\Phi(s)=\langle Z(s),\mathcal R^*\Phi(s)\rangle.                       \tag{16}
\]

Comme \(Z\in L^3_{\rm loc}\) et \(\Phi\) est compacte,
\(g_\Phi\in L^1(I)\). La convergence faible-étoile (4) donne

\[
 \int_I(\beta_n-\beta)g_\Phi\,ds\longrightarrow0.                        \tag{17}
\]

Les équations (14)--(17) prouvent (5). Il n'y a ni lemme de produit
compensé, ni convergence ponctuelle de \(\beta_n\), ni borne de
\(\mathcal RZ_n\) dans un espace positif.

La bornitude \(L^\infty\) de \(\beta_n\) est utilisée exactement dans
(15). Une convergence seulement faible dans \(L^1\), sans
équi-intégrabilité ou meilleur contrôle du facteur fort, ne fermerait pas le
même argument.

## 4. Passage du résidu à l'équation de transport

La convergence (1) implique

\[
 \partial_sZ_n\longrightarrow\partial_sZ
 \quad\text{dans }\mathcal D',                                           \tag{18}
\]

car la dérivation est continue sur les distributions. Avec (3) et (5),

\[
 \partial_sZ-\beta\mathcal RZ=0                                          \tag{19}
\]

dans \(\mathcal D'\), ce qui est (6).

Toutes les égalités impliquant \(\beta\) ou une dérivée temporelle valent
presque partout après choix de représentants; (19) est l'énoncé invariant,
sans choix de tranche. Une famille dénombrable dense de tests spatiaux sur
une exhaustion par boules permet, si nécessaire, de choisir un seul ensemble
temporel de mesure pleine pour tous les appariements.

## 5. Reconstruction de la phase et du profil fixe

Définissons \(\theta\) par (7). La borne (4) donne

\[
 \theta\in W^{1,\infty}(I),qquad
 \operatorname{Lip}(\theta)\leq M_\beta.                                  \tag{20}
\]

Considérons dans les distributions

\[
 W(s)=Q_{-\theta(s)}Z(s).                                                  \tag{21}
\]

La règle de chaîne distributionnelle est valable avec une phase
\(W^{1,\infty}\) — le cycle 0055 montre même que
\(W^{1,1}_{\rm loc}\) suffit. En utilisant que \(\mathcal R\) commute avec
\(Q_\gamma\),

\[
\begin{aligned}
 \partial_sW
 &=Q_{-\theta}
   (\partial_sZ-\theta'\mathcal RZ)\\
 &=Q_{-\theta}(\partial_sZ-\beta\mathcal RZ)=0.                            \tag{22}
\end{aligned}
\]

Une distribution sur un intervalle dont la dérivée temporelle est nulle est
indépendante du temps. Il existe donc
\(U\in\mathcal D'(\mathbb R^3)\) tel que

\[
 W(s)=U\quad\text{dans }\mathcal D'(I\times\mathbb R^3).                  \tag{23}
\]

Cela prouve (8). Aucune trace forte \(Z(s_0)\) n'est requise. On peut définir
\(U\) par une moyenne temporelle de \(W\) contre une fonction de masse un.
Si un représentant faiblement continu est disponible, alors
\(U=Q_{-\theta(s_0)}Z(s_0)\).

La constante additive \(\theta_0\) change \(U\) en un profil tourné mais ne
change ni \(Z\), ni \(\beta\). Un stabilisateur fini de \(U\) ne crée pas de
phase variable supplémentaire sous la régularité AC.

## 6. Passage de l'équation Navier--Stokes

Chaque \(Z_n\) résout, contre les tests solénoïdaux compacts,

\[
 \partial_sZ_n-\Delta Z_n
 +\operatorname{div}(Z_n\otimes Z_n)
 +\kappa(1+y\cdot\nabla)Z_n=0.                                            \tag{24}
\]

Les termes linéaires passent dans les distributions par (1). Le stress passe
fortement :

\[
 Z_n\otimes Z_n\longrightarrow Z\otimes Z
 \quad\text{dans }L^{3/2}_{\rm loc}.                                      \tag{25}
\]

La divergence nulle passe elle aussi. Par conséquent \(Z\) résout (24) dans
la formulation solénoïdale, sans défaut de Reynolds et sans qu'une pression
doive être extraite. Cela suffit à la classification équivariante du cycle
0055, formulée sur les tests solénoïdaux.

Pour employer l'équation projetée globale

\[
 \partial_sZ+\mathcal F_\kappa(Z)=0,                                     \tag{26}
\]

il faut en plus une classe tempérée compatible avec \(\mathbb P\). Une
hypothèse suffisante dans le cadre actif est

\[
 \sup_n\|Z_n\|_{L^\infty(I;L^{3,\infty}(\mathbb R^3))}\leq M.             \tag{27}
\]

Alors les stress sont uniformément bornés dans
\(L^\infty_tL^{3/2,\infty}_x\). Si

\[
 \Pi_n=R_iR_j((Z_n)_i(Z_n)_j),                                            \tag{28}
\]

la convergence locale forte (25), la dualité
\(L^{3/2,\infty}\)--\(L^{3,1}\) et le contrôle des queues des doubles
Riesz donnent

\[
 \Pi_n\longrightarrow
 \Pi=R_iR_j(Z_iZ_j)\quad\text{dans }\mathcal D'.                           \tag{29}
\]

Sans (27)--(28), les pressions locales peuvent conserver une composante
harmonique. Cela ne bloque pas (24), mais interdit d'affirmer sans preuve la
jauge globale (29).

## 7. Suitability et bornes locales nécessaires

La propriété « \(Z_n\) est suitable » est individuelle. Pour la transmettre
à la limite, il faut au minimum, pour tout
\(J\Subset I\) et tout \(R<\infty\), des bornes indépendantes de \(n\) du
type

\[
\begin{aligned}
 \sup_n\|Z_n\|_{L^\infty(J;L^2(B_R))}&<\infty,\\
 \sup_n\|\nabla Z_n\|_{L^2(J\times B_R)}&<\infty,\\
 \sup_n\|\Pi_n\|_{L^{3/2}(J\times B_R)}&<\infty,                           \tag{30}
\end{aligned}
\]

ou la décomposition proche/harmonique uniforme équivalente du cycle 0045.
Après extraction,

\[
 \nabla Z_n\rightharpoonup\nabla Z
 \quad\text{dans }L^2_{\rm loc},                                         \tag{31}
\]

la pression passe comme dans (29) ou localement, les flux cubiques passent
par (1), et la dissipation passe par semi-continuité inférieure. On obtient
alors l'inégalité locale d'énergie renormalisée pour \(Z\).

Sans (30), (1) ne contrôle aucune dérivée spatiale. Des approximations lisses
peuvent converger fortement en \(L^3\) vers un champ hors de
\(W^{1,2}_{\rm loc}\) tout en ayant des gradients divergents. Ce constat
fonctionnel ne construit pas une suite de solutions Navier--Stokes, mais il
montre que le mot « suitable » sans uniformité ne ferme pas le passage.

La conclusion conservatrice est donc :

- \(Z\) est toujours une solution distributionnelle solénoïdale de (24) sous
  (1);
- \(Z\) est suitable seulement sous le ledger uniforme (30) et un passage de
  pression approprié.

## 8. Héritage de \(W^{1,2}_{\rm loc}\) par le profil

Sous (30), \(Z\in L^2(J;W^{1,2}(B_R))\). La représentation (8) utilise des
rotations centrées, qui préservent \(B_R\) et la norme du gradient. Ainsi

\[
 \int_J\int_{B_R}|\nabla Z(s,y)|^2\,dy\,ds
 =|J|\int_{B_R}|\nabla U(y)|^2\,dy.                              \tag{32}
\]

Pour tout \(J\) de longueur positive, (32) donne

\[
 U\in W^{1,2}_{\rm loc}(\mathbb R^3).                                    \tag{33}
\]

Sous la borne globale (27), la semi-continuité faible-étoile donne aussi

\[
 U\in L^{3,\infty}(\mathbb R^3),qquad
 \|U\|_{3,\infty}\leq M.                                                 \tag{34}
\]

Les conclusions (33)--(34) ne doivent pas être attribuées à la seule
convergence (1).

## 9. Capture et non-trivialité

Une capture robuste sur un cylindre passe par (1). Par exemple, si pour un
\(J\Subset I\) de mesure positive

\[
 \int_J\int_{B_1}|Z_n|^3\,dy\,ds\geq c_*>0                              \tag{35}
\]

uniformément en \(n\), alors

\[
 \int_J\int_{B_1}|Z|^3\,dy\,ds\geq c_*.                                  \tag{36}
\]

Comme les rotations préservent \(B_1\), (8) donne

\[
 |J|\|U\|_{L^3(B_1)}^3
 =\int_J\int_{B_1}|Z|^3\geq c_*,                                         \tag{37}
\]

donc \(U\neq0\). Une minoration seulement sur une tranche temporelle ne
passe pas par la convergence espace-temps (1) sans compacité forte de cette
trace. Une capture dans une boule non centrée à l'origine n'est pas
automatiquement préservée par \(Q_\theta\).

## 10. Application de la classification autonome

L'opérateur de (26) commute avec les rotations centrées. En insérant (8) et
\(\theta'=\beta\), le cycle 0055 donne

\[
 \beta(s)\mathcal RU+\mathcal F_\kappa(U)=0
 \quad\text{dans }\mathcal D'_x\text{ pour presque tout }s.               \tag{38}
\]

Deux branches sont possibles.

### 10.1 Stabilisateur continu

Si \(\mathcal RU=0\), alors \(Q_\gamma U=U\) pour tout \(\gamma\), (8) est
stationnaire et

\[
 \mathcal F_\kappa(U)=0.                                                  \tag{39}
\]

La fonction \(\beta\) peut rester arbitraire : elle paramètre une direction
de groupe qui n'agit pas sur le profil. Sous (33)--(34), le théorème publié de
Guevara--Phuc donne \(U=0\). Une capture telle que (37) exclut donc cette
branche.

### 10.2 Générateur non nul

Si \(\mathcal RU\neq0\), choisissons un test spatial
\(\varphi_0\) avec
\(\langle\mathcal RU,\varphi_0\rangle\neq0\). L'équation (38) donne

\[
 \beta(s)
 =-\frac{\langle\mathcal F_\kappa(U),\varphi_0\rangle}
         {\langle\mathcal RU,\varphi_0\rangle}
 =:\alpha                                                        \tag{40}
\]

sur un ensemble de temps de mesure pleine. Ainsi

\[
 \theta(s)=\alpha s+\theta_0,qquad
 Z(s+\tau)=Q_{\alpha\tau}Z(s),                                  \tag{41}
\]

et \(Z\) est RSS exacte. La classification n'impose aucune borne ni aucun
signe à \(\alpha\). Les exclusions de Pineau--Vicol v2 demandent en plus une
borne Type I ponctuelle et un régime de rotation petit ou grand; elles ne
suivent pas de (27), (33) ou (34).

## 11. Quantificateurs et ensembles exceptionnels

Le ledger exact est :

1. fixer l'intervalle connexe \(I\), l'axe, \(\kappa\) et la borne uniforme
   \(M_\beta\);
2. extraire une seule sous-suite faible-étoile de \(\beta_n\);
3. utiliser cette même sous-suite dans (1), (3), (5) et, si disponibles,
   (27)--(31);
4. obtenir (6) dans les distributions, avant tout choix de représentant
   temporel;
5. définir une phase AC par (7), puis un profil distributionnel fixe par
   (21)--(23);
6. choisir un ensemble temporel commun de pleine mesure pour (38) à l'aide
   d'une famille dénombrable dense de tests;
7. conclure que \(\beta=\alpha\) presque partout seulement dans la branche
   \(\mathcal RU\neq0\).

Si \(I\) n'est pas connexe, la constante de phase initiale et la vitesse
\(\alpha\) peuvent être différentes sur chaque composante. Aucun énoncé de
trace aux extrémités de \(I\) n'est requis.

## 12. Passe contradictoire

1. **Produit faible–faible.** Sans la forte convergence locale de \(Z_n\),
   le produit \(\beta_n\mathcal RZ_n\) n'est pas stable. La convergence de
   distributions seule ne suffit pas.
2. **Dérivée spatiale apparente.** Il ne faut pas demander
   \(\mathcal RZ_n\to\mathcal RZ\) dans une norme positive. (12) déplace le
   générateur sur le test.
3. **Borne de \(\beta_n\).** Elle est indispensable dans (15). Une suite
   non bornée peut compenser un défaut \(Z_n-Z\) petit.
4. **Faible-étoile contre mauvais test.** Le facteur
   \(g_\Phi\) doit appartenir à \(L^1_t\); la compacité temporelle de
   \(\Phi\) et \(Z\in L^3_{\rm loc}\) le garantissent.
5. **Phase.** La bonne équation est \(\theta'=\beta\) avec la convention
   (11). Prendre \(-\beta\) rend (22) égal à \(2\beta\mathcal RZ\).
6. **Trace cachée.** Le profil \(U\) est construit comme distribution
   constante en temps. Il n'est pas nécessaire de supposer
   \(Z_n(s_0)\to Z(s_0)\).
7. **Stress.** La forte \(L^3\) donne exactement la forte
   \(L^{3/2}\) du produit; aucun tenseur de Reynolds local ne reste.
8. **Pression.** La formulation solénoïdale passe sans pression. Identifier
   la jauge de Riesz demande le contrôle global (27)--(29).
9. **Suitability individuelle.** Sans constantes uniformes dans (30), la
   limite n'est pas démontrée suitable et (33) n'est pas acquis.
10. **Capture terminale.** Une norme non nulle à un seul temps peut
    disparaître malgré (1). La capture espace-temps (35) est la forme stable.
11. **Stabilisateur.** Dans la branche \(\mathcal RU=0\), \(Z\) est
    stationnaire mais \(\beta\) n'a aucune raison d'être constante.
12. **Classification approchée.** Le résidu disparaît seulement après le
    passage à la limite. Le lemme ne fournit aucun taux quantitatif de
    proximité à une RSS pour un indice \(n\) fini.
13. **Portée Clay.** Rien ne produit les hypothèses (1)--(3) depuis une
    singularité Clay générale. Type II, axes mobiles, profils multi-échelles
    et résidus non compacts restent hors champ.

## 13. Statut logique

| Implication | Statut |
|---|---|
| (1)--(4) \(\Rightarrow\) produit (5) | **PROUVÉ** par dualité faible–forte |
| (3), (5), (18) \(\Rightarrow\) transport (6) | **PROUVÉ** dans \(\mathcal D'\) |
| (6), \(\beta\in L^\infty\Rightarrow\) phase et profil (7)--(8) | **PROUVÉ**; \(W^{1,1}_{\rm loc}\) suffirait localement |
| solutions NS + (1) \(\Rightarrow\) limite NS solénoïdale | **PROUVÉ**, sans défaut de stress |
| suitable individuel + (1) \(\Rightarrow Z\) suitable | **NON DÉMONTRÉ** sans (30) |
| (27)--(30) \(\Rightarrow\) pression Riesz et suitability de la limite | **PROUVÉ conditionnellement** par le ledger compact standard |
| (30), (8) \(\Rightarrow U\in W^{1,2}_{\rm loc}\) | **PROUVÉ** |
| capture cylindrique + (1), (8) \(\Rightarrow U\neq0\) | **PROUVÉ** |
| autonomie + \(\mathcal RU\neq0\Rightarrow\beta=\alpha\) p.p. | **PROUVÉ**, cycle 0055 réappliqué |
| autonomie + \(\mathcal RU=0\Rightarrow Z\) stationnaire | **PROUVÉ** |
| RSS faible-\(L^3\Rightarrow\) trivialité pour toute rotation | **NON DÉMONTRÉ** |
| lemme de fermeture \(\Rightarrow\) résolution Clay | **NON DÉMONTRÉ** |

**Décision analytique : CONTINUER sous bornes uniformes explicites.** Le
résidu tangent compactifie bien vers une orbite exacte, puis l'autonomie la
rigidifie en stationnaire ou RSS. Le prochain verrou est la production des
hypothèses (1)--(3) avec un ledger uniforme de pression et d'énergie, ou une
rigidité RSS au faible-\(L^3\) au-delà des régimes Type I ponctuels connus.
