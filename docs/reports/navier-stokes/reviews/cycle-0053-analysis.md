# Cycle 0053 — presque-stationnarité locale et rigidité du profil

Date : 2026-08-15.

Statut : `AI_INTERNAL_DERIVATION`; la dernière flèche utilise le théorème
publié de Guevara--Phuc déjà audité au cycle 0052. Aucun résultat Clay et
aucun calcul numérique.

## Verdict

Le lemme proposé est **vrai sous le paquet exact de compacité locale et de
capture persistante déjà construit**, avec deux qualifications importantes.

Soit (Z) une solution ancienne faible adaptée locale de

\[
 \partial_s Z-\Delta Z+\operatorname{div}(Z\otimes Z)+\nabla\Pi
 +\kappa(1+y\cdot\nabla)Z=0,
 \qquad \operatorname{div}Z=0,                 \tag{1}
\]

sur \(\mathbb R^3\times(-\infty,0]\), avec \(\kappa>0\) **fixe**, pression
globale dans la jauge de Riesz,

\[
 \Pi=R_iR_j(Z_iZ_j),\qquad
 \operatorname*{ess\,sup}_{s\leq0}
 \|Z(s)\|_{L^{3,\infty}(\mathbb R^3)}\leq M,    \tag{2}
\]

et capture persistante, sous la forme

\[
 \|Z(s)\|_{L^3(B_1)}\geq\gamma>0
 \quad\text{pour presque tout }s\leq0.          \tag{3}
\]

La minoration faible-Lorentz du cycle 0046 implique (3), car
\(K_3(f;B_1)\leq\|f\|_{L^3(B_1)}\). Supposons en outre le paquet de
compacité locale uniforme sous translations temporelles : sur toute fenêtre
bornée et toute boule fixe, les translations sont bornées dans
\(L^\infty_tL^2_x\cap L^2_tH^1_x\), leur dérivée possède la borne négative
du cycle 0045, et une sous-suite converge fortement dans \(L^3_{t,x,\rm loc}\).

Pour

\[
 D_R(s)=\int_{s-1}^{s}
 \|\partial_\sigma Z(\sigma)\|_{(W^{1,3}_0(B_R))^*}\,d\sigma, \tag{4}
\]

si une même suite \(s_n\to-\infty\) vérifie

\[
 D_R(s_n)\longrightarrow0\qquad\text{pour tout }R>0,       \tag{5}
\]

alors les translations \(Z_n(y,\tau)=Z(y,s_n+\tau)\) ont une limite locale
forte \(U(y)\), indépendante de \(\tau\), telle que

\[
 U\in W^{1,2}_{\rm loc}(\mathbb R^3)
       \cap L^{3,\infty}(\mathbb R^3),
 \qquad \|U\|_{L^3(B_1)}\geq\gamma.             \tag{6}
\]

Elle résout faiblement l'équation stationnaire de Leray avec coefficient
\(\kappa\). Après une dilatation critique qui normalise \(\kappa\) à
\(1/2\), le théorème 1.3 de Guevara--Phuc s'applique avec \(q=3\) et impose
\(U=0\), en contradiction avec (6). Par conséquent,

\[
 \boxed{\exists R_*<\infty:\quad
 \liminf_{s\to-\infty}D_{R_*}(s)>0.}            \tag{7}
\]

La première qualification est que (4) n'est pas une conséquence formelle de
la seule borne faible-\(L^3\) : l'énergie locale et la décomposition de
pression sont nécessaires pour rendre la norme duale forte bien définie. La
seconde est que la capture doit porter un intervalle de temps de mesure
positive; une capture sur une seule trace ne passerait pas par la seule
compacité espace-temps.

## 1. L'endpoint de la définition de \(D_R\)

### 1.1 Pourquoi faible-\(L^3\) seul ne suffit pas

La borne (2) donne seulement

\[
 Z\otimes Z,\ \Pi\in L^{3/2,\infty}(\mathbb R^3).          \tag{8}
\]

Or le partenaire de Hölder exact de \(L^{3/2,\infty}\) est
\(L^{3,1}\), pas \(L^3\). Il est donc faux, au seul niveau de (8), que
\(\nabla\Pi\) ou \(\operatorname{div}(Z\otimes Z)\) appartiennent à
\((W^{1,3}_0)^*\).

Le défaut est réel. Sur une boule centrée en zéro, prenez près de zéro

\[
 q(x)=|x|^{-2},\qquad
 g(x)=|x|^{-1}\bigl(\log(e/|x|)\bigr)^{-1/2}.    \tag{9}
\]

Alors \(q\in L^{3/2,\infty}\) et \(g\in L^3\), mais
\(\int qg=+\infty\). Après soustraction de la moyenne de \(g\), l'opérateur
de Bogovskii fournit un champ \(\varphi\in W^{1,3}_0\) de divergence
\(g-\overline g\); le terme constant ajouté est intégrable contre \(q\),
donc \(q\,\operatorname{div}\varphi\) reste non intégrable. Ainsi la pression
faible-\(L^{3/2}\) n'agit pas continûment sur tout \(W^{1,3}_0\).

### 1.2 Pourquoi (4) est néanmoins licite ici

La suitability locale donne, uniformément sur chaque fenêtre translatée et
chaque boule fixe,

\[
 Z\in L^\infty_tL^2_x\cap L^2_tH^1_x
 \quad\Longrightarrow\quad
 Z\in L^4_tL^3_x.                               \tag{10}
\]

Choisissons une coupure \(\zeta=1\) sur \(B_{2R}\), supportée dans
\(B_{4R}\), et écrivons sur \(B_{2R}\)

\[
 \Pi=R_iR_j(\zeta Z_iZ_j)+h_R.                  \tag{11}
\]

La partie proche appartient à \(L^2_tL^{3/2}_x\) par (10), tandis que
\(h_R\) est harmonique et borné dans \(L^\infty_tC^m(B_R)\) par (2) et les
estimations intérieures. Par conséquent, pour
\(X_R=W^{1,3}_0(B_R)^3\), tous les termes de (1) appartiennent à
\(L^1_tX_R^*\) :

\[
\begin{aligned}
 |\langle\Delta Z,\varphi\rangle|
 &\leq C_R\|\nabla Z\|_2\|\varphi\|_{W^{1,3}},\\
 |\langle\operatorname{div}(Z\otimes Z)+\nabla\Pi,\varphi\rangle|
 &\leq C\bigl(\|Z\|_3^2+\|\Pi\|_{3/2}\bigr)
        \|\varphi\|_{W^{1,3}},\\
 |\langle(1+y\cdot\nabla)Z,\varphi\rangle|
 &\leq C_R\|Z\|_2\|\varphi\|_{W^{1,3}}.        \tag{12}
\end{aligned}
\]

Le dernier appariement est pris après intégration par parties. Puisque
\(X_R\) est séparable et réflexif et que le membre de droite de (1) fournit
un représentant fortement mesurable dans \(L^1_tX_R^*\), l'intégrale de (4)
est bien définie. Cette justification doit accompagner (4); l'étiquette
« uniforme \(L^{3,\infty}\) » ne la remplace pas.

### 1.3 Variante endpoint robuste

Si l'on veut formuler l'observable avant d'avoir acquis (10)--(11), le bon
espace de tests est

\[
 X_R^{\rm Lor}=\overline{C_c^\infty(B_R)^3}^{
 \|\cdot\|_{L^{3,1}}+\|\nabla\cdot\|_{L^{3,1}}}.            \tag{13}
\]

Pour éviter toute question de mesurabilité forte dans son dual, on peut
définir directement

\[
\begin{aligned}
 \widehat D_R(s)=\sup\Bigl\{&\left|
 \int_{s-1}^{s}\langle\partial_\sigma Z,\psi(\sigma)\rangle
 \,d\sigma\right|:
 \psi\in C_c^\infty((s-1,s)\times B_R)^3,\\
 &\operatorname*{ess\,sup}_{\sigma}
 \|\psi(\sigma)\|_{X_R^{\rm Lor}}\leq1\Bigr\}.           \tag{14}
\end{aligned}
\]

Hölder--Lorentz rend (14) compatible avec (8). Sous le paquet suitable,
\(D_R\to0\) implique \(\widehat D_R\to0\), puisque
\(X_R^{\rm Lor}\hookrightarrow W^{1,3}_0(B_R)\). Pour une dérivée
fortement mesurable dans \(L^1_t(X_R^{\rm Lor})^*\), le supremum de (14),
après densité et sélection mesurable, coïncide avec l'intégrale de la norme
duale. Sans cette représentation, (14) est la définition conservatrice; la
preuve de stationnarité ci-dessous n'utilise que ses appariements avec des
tests lisses.

## 2. Translation et compacité locale

Posons, pour \(\tau\in[-1,0]\),

\[
 Z_n(y,\tau)=Z(y,s_n+\tau),\qquad
 \Pi_n(y,\tau)=\Pi(y,s_n+\tau).                 \tag{15}
\]

L'équation est autonome et \(\kappa\) ne dépend ni de \(n\), ni du temps.
Les estimations locales uniformes et le ledger de Simon du cycle 0045
donnent, après une extraction diagonale en espace,

\[
\begin{aligned}
 Z_n&\rightharpoonup U
     &&\text{dans }L^2((-1,0);W^{1,2}(B_R)),\\
 Z_n&\longrightarrow U
     &&\text{fortement dans }L^3((-1,0)\times B_R)
\end{aligned}                                                \tag{16}
\]

pour tout \(R<\infty\). Une même sous-suite est utilisée pour tous les
rayons entiers. La convergence forte (16) identifie

\[
 Z_n\otimes Z_n\longrightarrow U\otimes U
 \quad\text{dans }L^{3/2}_{\rm loc}.            \tag{17}
\]

La borne faible-\(L^3\) passe à la limite, par extraction faible-étoile ou
par convergence presque partout sur les boules et semi-continuité des
fonctions de distribution :

\[
 \operatorname*{ess\,sup}_{\tau\in(-1,0)}
 \|U(\tau)\|_{L^{3,\infty}(\mathbb R^3)}\leq M.             \tag{18}
\]

## 3. La petitesse de \(D_R\) force la stationnarité

Pour tout
\(\eta\in C_c^\infty((-1,0)\times B_R)^3\), (4)--(5) donnent

\[
\begin{aligned}
 |\langle\partial_\tau U,\eta\rangle|
 &=\lim_{n\to\infty}
 \left|\int_{-1}^{0}
 \langle\partial_\tau Z_n,\eta(\tau)\rangle\,d\tau\right|\\
 &\leq\lim_{n\to\infty}
 D_R(s_n)\sup_{\tau}\|\eta(\tau)\|_{W^{1,3}_0(B_R)}=0.    \tag{19}
\end{aligned}
\]

Il n'est pas nécessaire de sélectionner un « bon instant » dans la fenêtre :
la variation duale totale sur toute la fenêtre tend vers zéro. Ainsi
\(\partial_\tau U=0\) dans les distributions et

\[
 U(y,\tau)=U(y)\quad\text{pour presque tout }(y,\tau).      \tag{20}
\]

La borne faible des gradients dans (16), jointe à (20), donne
\(U\in W^{1,2}_{\rm loc}(\mathbb R^3)\). Le même argument fonctionne avec
\(\widehat D_R\) de (14).

## 4. Passage de l'équation et suivi de la pression

Pour les tests solénoïdaux compacts, (16)--(17) suffisent à passer à la
limite dans tous les termes de (1), sans utiliser la pression. Le drift ne
cache aucune dérivée perdue :

\[
 \langle(1+y\cdot\nabla)U,\varphi\rangle
 =-\int_{\mathbb R^3}U\cdot(2\varphi+y\cdot\nabla\varphi). \tag{21}
\]

On obtient donc, pour tout
\(\varphi\in C_{c,\sigma}^\infty(\mathbb R^3)^3\),

\[
 \int\nabla U:\nabla\varphi
 -\int(U\otimes U):\nabla\varphi
 -\kappa\int U\cdot(2\varphi+y\cdot\nabla\varphi)=0.       \tag{22}
\]

C'est exactement la formulation faible stationnaire de Leray associée à
(1).

La jauge de pression peut aussi être suivie, et elle exclut un défaut
harmonique silencieux. Les produits sont uniformément bornés dans
\(L^{3/2,\infty}(\mathbb R^3)\). Pour un test espace-temps compact \(\Phi\),
la dualité
\(L^{3/2,\infty}\)--\(L^{3,1}\), la bornitude des Riesz sur
\(L^{3,1}\), (17), puis la petitesse de la queue de
\(R_iR_j\Phi\) dans \(L^{3,1}\), donnent

\[
 R_iR_j((Z_n)_i(Z_n)_j)
 \longrightarrow R_iR_j(U_iU_j)
 \quad\text{dans les distributions}.           \tag{23}
\]

Autrement dit,

\[
 P=R_iR_j(U_iU_j)\in L^{3/2,\infty}(\mathbb R^3),          \tag{24}
\]

et aucun champ harmonique venu de l'infini ne subsiste lorsque la jauge
globale est conservée. Puisque \(U\) est indépendant de \(\tau\), (24) l'est
aussi. Avec des pressions seulement locales, on obtiendrait au plus
\(P(y)+c(\tau)\); ce terme disparaît dans (22), mais la jauge de Riesz fixe
également cette ambiguïté.

La divergence du drift est nulle lorsque \(\operatorname{div}U=0\), donc la
formule de Riesz n'acquiert aucun terme supplémentaire dépendant de
\(\kappa\).

## 5. La capture rend le profil non nul

Fixons un intervalle intérieur \(J=(-3/4,-1/4)\). Par (3),

\[
 \int_J\int_{B_1}|Z_n|^3\,dy\,d\tau
 \geq |J|\gamma^3.                              \tag{25}
\]

La forte convergence de (16) sur \(J\times B_1\), puis la stationnarité,
donnent

\[
 |J|\|U\|_{L^3(B_1)}^3
 =\int_J\int_{B_1}|U|^3
 \geq |J|\gamma^3.                              \tag{26}
\]

Ainsi \(U\neq0\). Cette étape n'emploie aucune convergence forte à
\(\tau=0\). Si la capture n'était connue qu'à la tranche terminale, (25)
serait faux et l'argument s'arrêterait ici.

## 6. Coefficient \(\kappa\) et contradiction de Guevara--Phuc

Le profil obtenu satisfait

\[
 -\Delta U+\operatorname{div}(U\otimes U)+\nabla P
 +\kappa(U+y\cdot\nabla U)=0.                  \tag{27}
\]

Le signe et la positivité de \(\kappa\) sont essentiels. Pour rejoindre la
normalisation usuelle à coefficient \(1/2\), posons

\[
 \lambda=\sqrt{2\kappa},\qquad
 U(y)=\lambda V(\lambda y),\qquad
 P(y)=\lambda^2Q(\lambda y).                   \tag{28}
\]

Après division par \(\lambda^3\), (27) devient

\[
 -\Delta V+\operatorname{div}(V\otimes V)+\nabla Q
 +\tfrac12(V+x\cdot\nabla V)=0.                \tag{29}
\]

La transformation (28) préserve exactement la norme
\(L^{3,\infty}\), la classe \(W^{1,2}_{\rm loc}\) et la non-nullité. Le
théorème 1.3 de Guevara--Phuc, *SIAM J. Math. Anal.* 50 (2018), 541--556,
DOI `10.1137/16M110099X`, s'applique à (29) avec
\(q=3\in(12/5,6)\) et impose \(V=0\), donc \(U=0\). Cela contredit (26).

Si \(\kappa=0\), cette normalisation est impossible et le théorème cité ne
ferme pas le profil stationnaire Navier--Stokes ordinaire. Si
\(\kappa=\kappa_n\), il faut d'abord extraire une limite strictement positive
et suivre le coefficient dans (27). Dans la construction active,
\(\kappa=2/A_*>0\) est fixe, de sorte qu'aucun de ces deux défauts ne se
produit.

## 7. Audit complet de la diagonale en rayon

La norme de (4) est monotone avec le rayon. Si \(0<R<R'\), l'extension par
zéro envoie isométriquement
\(W^{1,3}_0(B_R)\) dans \(W^{1,3}_0(B_{R'})\). Par conséquent,

\[
 \|f\|_{(W^{1,3}_0(B_R))^*}
 \leq\|f\|_{(W^{1,3}_0(B_{R'}))^*},
 \qquad D_R(s)\leq D_{R'}(s).                  \tag{30}
\]

La même inclusion de tests prouve la monotonie de \(\widehat D_R\).

Supposons la négation de (7). Comme \(D_R\geq0\), elle s'écrit exactement

\[
 \forall R>0,\qquad
 \liminf_{s\to-\infty}D_R(s)=0.                \tag{31}
\]

Pour chaque entier \(n\geq1\), la définition du liminf permet de choisir

\[
 s_n<-n,\qquad D_n(s_n)<\frac1n.                \tag{32}
\]

Pour tout rayon fixe \(R\), dès que \(n\geq\lceil R\rceil\), (30)--(32)
donnent

\[
 D_R(s_n)\leq D_n(s_n)<\frac1n\longrightarrow0.            \tag{33}
\]

Il s'agit donc d'une **même suite de temps pour tous les rayons**; aucune
inversion de quantificateur et aucune intersection dénombrable de sous-suites
temporelles n'est cachée. Cette suite satisfait (5), qui vient d'être exclue.
Ainsi (31) est fausse et (7) est démontrée. En particulier, il existe
\(\delta_*>0\) et \(S_*<0\) tels que

\[
 D_{R_*}(s)\geq\delta_*
 \quad\text{pour tout }s<S_*.                  \tag{34}
\]

## 8. Passe contradictoire indépendante

1. **Pairing endpoint.** \(L^{3/2,\infty}\) ne s'apparie pas à tout
   \(L^3\). Le contre-exemple (9) réfute toute dérivation de (4) depuis (2)
   seule. La preuve utilise explicitement (10)--(11), ou la variante (14).
2. **Mesurabilité du dual.** La norme intégrée de (4) est licite parce que
   l'équation suitable fournit un représentant fortement mesurable dans le
   dual du Banach séparable \(W^{1,3}_0\). La définition distributionnelle
   (14) est disponible si ce représentant n'a pas encore été établi.
3. **Un instant presque stationnaire ne suffit pas.** Aucune valeur
   \(\partial_sZ(s_n)\) n'est sélectionnée. C'est la variation totale sur
   \([s_n-1,s_n]\) qui annule la dérivée distributionnelle de la limite.
4. **Produit quadratique.** Une convergence faible-étoile
   \(L^{3,\infty}\) ne suffit pas. La forte \(L^3_{t,x,\rm loc}\) de (16)
   est indispensable à (17).
5. **Pression non locale.** La convergence locale du produit ne suffit pas à
   identifier directement toute la pression. L'argument de queue dans la
   dualité Lorentz, ou la décomposition proche/harmonique, est nécessaire à
   (23).
6. **Capture de trace.** Une minoration à \(s_n\) seulement pourrait
   disparaître dans une couche temporelle. La capture a.e. sur chaque fenêtre
   donne (25) et ferme exactement ce trou.
7. **Notion de solution.** La limite n'est pas déclarée mild. Guevara--Phuc
   demande ici seulement le profil faible
   \(W^{1,2}_{\rm loc}\), obtenu par (16), et la formulation solénoïdale
   (22).
8. **Coefficient.** Le théorème de profil backward exige \(\kappa>0\). Le
   cas \(\kappa=0\), un signe opposé ou une suite \(\kappa_n\to0\) ne sont
   pas couverts.
9. **Rayons.** Choisir séparément une suite pour chaque \(R\) serait une
   erreur. La monotonie par extension nulle autorise le choix unique (32).
10. **Portée Clay.** (7) est une propriété conditionnelle d'une limite
    ancienne renormalisée déjà construite sous un scénario Type I. Elle ne
    borne pas encore \(D_R\) depuis les données Clay et n'exclut ni une orbite
    temporelle persistante, ni DSS, ni Type II, ni blow-up général.

## 9. Statut logique

| Implication | Statut |
|---|---|
| suitable locale + faible-\(L^3\) uniforme \(\Rightarrow D_R<\infty\) sur toute fenêtre compacte | **PROUVÉ**, via énergie locale et pression proche/harmonique |
| faible-\(L^3\) seul \(\Rightarrow \partial_sZ\in(W^{1,3}_0)^*\) | **FAUX comme implication fonctionnelle**, contre-profil (9) |
| (5) + compacité forte locale \(\Rightarrow\partial_\tau U=0\) | **PROUVÉ** |
| pression des translations \(\Rightarrow P=R_iR_j(U_iU_j)\) | **PROUVÉ** dans les distributions, avec contrôle de queue Lorentz |
| capture persistante + forte \(L^3_{t,x,\rm loc}\) \(\Rightarrow U\neq0\) | **PROUVÉ** |
| profil faible stationnaire, \(\kappa>0\), \(W^{1,2}_{\rm loc}\cap L^{3,\infty}\) \(\Rightarrow U=0\) | **SOURCE_VERIFIED**, Guevara--Phuc |
| négation de (7) \(\Rightarrow\) une suite commune satisfaisant (5) | **PROUVÉ**, monotonie et diagonale entière |
| (7) \(\Rightarrow\) régularité globale Clay | **NON DÉMONTRÉ** |

**Décision analytique : CONTINUER.** Le maillon « presque stationnaire sur
des fenêtres unitaires \(\Rightarrow\) profil BSS interdit » est fermé. Le
verrou suivant est quantitatif et dynamique : exploiter la borne inférieure
(34), ou montrer qu'une fonctionnelle coercive intégrable en temps force au
contraire une suite avec \(D_R(s_n)\to0\). Si cette intégrabilité ne peut pas
être produite, (34) identifie précisément l'activité temporelle locale
persistante que toute orbite ancienne non triviale doit conserver.
