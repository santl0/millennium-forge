# Cycle 0036 — Sélection d'une goutte active et gate directionnel local

**Statut :** `AI_INTERNAL_DERIVATION` — ne pas classer `PAPER_PROOF`

**Verrou :** `GAP-ACTIVE-HALO-DIAMETER` pour un superniveau pure-swirl
dispersé en \(m\) composantes de diamètre \(O(R_j)\).

**Verdict :** sous finitude et diamètre axial uniforme des composantes du
superniveau inférieur, les gates globaux sélectionnent une **troncature de
goutte** dont le rapport endpoint est minoré indépendamment de \(m\). Le gate
du cycle 0033 fournit ensuite une boule de rayon \(O(R_j)\) à oscillation
directionnelle minorée par une puissance douze du rapport global. Aucun
contre-exemple curl-compatible ne satisfait toutes ces hypothèses. La simple
restriction du champ original à une goutte, et le champ cellulaire entier,
doivent rester distingués de la troncature sélectionnée.

## Équation, domaine et objet

Le problème Clay de référence reste

\[
 \partial_tu+(u\cdot\nabla)u=-\nabla p+\nu\Delta u,
 \qquad \nabla\cdot u=0,
 \qquad \nu>0,
 \qquad f=0,
\]

sur \(\mathbb R^3\). Le résultat présent est statique. Pour une famille finie,

\[
 U_j=\frac{R_j}{r}F_j(r,z)e_\theta,
 \qquad
 W_j=\operatorname{curl}U_j
 =\frac{R_j}{r}
   (-\partial_zF_j e_r+\partial_rF_j e_z),      \tag{1}
\]

où \(F_j\in C_c^\infty((0,\infty)\times\mathbb R)\),

\[
 \operatorname{supp}F_j\subset\{R_j/2<r<3R_j/2\},     \tag{2}
\]

et les supports tridimensionnels complets sont disjoints. On pose

\[
 U=\sum_jU_j,
 \quad W=\sum_jW_j,
 \quad K_u=\|U\|_{L^{3,\infty}}>0,
 \quad K_w=\|W\|_{L^{3/2,\infty}}<\infty.       \tag{3}
\]

Comme au cycle 0035, \(K_u>0\) impose \(K_w>0\) : si \(W=0\), la disjonction
et (1) donnent \(\nabla F_j=0\), puis la compacité donne \(F_j=0\).

## Énoncé audité

Soient \(0<\eta<1\) et \(\lambda>0\) tels que

\[
 \lambda\mu_U(\lambda)^{1/3}\ge(1-\eta)K_u,   \tag{4}
\]

avec \(\mu_U(t)=|\{|U|>t\}|\). Pour chaque cellule et chaque signe
\(\sigma\in\{-1,+1\}\), décomposons les composantes connexes
\(C_\alpha\) de

\[
 \{\sigma F_j>\lambda/4\}                      \tag{5}
\]

qui rencontrent \(\{\sigma F_j>\lambda/2\}\). L'indice \(\alpha\) contient
donc \(j\) et \(\sigma\). Supposons ces composantes en nombre fini et, pour
une constante \(\Lambda\) uniforme,

\[
 C_\alpha\subset
 \{R_j/2<r<3R_j/2,\ |z-z_\alpha|<\Lambda R_j\}. \tag{6}
\]

Définissons la troncature étendue par zéro hors de \(C_\alpha\),

\[
 G_\alpha=
 \mathbf1_{C_\alpha}(\sigma F_j-\lambda/4)_+,
 \qquad
 U_\alpha=\frac{R_j}{r}G_\alpha e_\theta,
 \qquad
 W_\alpha=\operatorname{curl}U_\alpha,          \tag{7}
\]

et

\[
 E_\alpha=C_\alpha\cap\{\sigma F_j>\lambda/2\},
 \qquad V_\alpha=|E_\alpha|.                   \tag{8}
\]

Alors il existe \(\alpha_*\) tel que

\[
 \boxed{
 K_{u,\alpha_*}:=\|U_{\alpha_*}\|_{L^{3,\infty}}
 \ge\frac{C_I}{648}\frac{K_u^2}{K_w}},         \tag{9}
\]

\[
 \boxed{
 \frac{K_{u,\alpha_*}}{K_{w,\alpha_*}}
 \ge\frac{C_I}{648}\left(\frac{K_u}{K_w}\right)^2}, \tag{10}
\]

où \(K_{w,\alpha}=\|W_\alpha\|_{L^{3/2,\infty}}\) et
\(C_I\) est une constante de

\[
 \operatorname{Per}(E)\ge C_I|E|^{2/3}         \tag{11}
\]

dans \(\mathbb R^3\). De plus, pour toute extension globale \(\zeta\) de la
direction \(W/|W|\), il existe une boule
\(B_{\alpha_*}\) de rayon \(C_\Lambda R_j\) telle que

\[
 \boxed{
 \operatorname{MO}_{B_{\alpha_*}}(\zeta)
 \ge c_\Lambda
 \left(\frac{C_I}{648}\right)^6
 \left(\frac{K_u}{K_w}\right)^{12}}.           \tag{12}
\]

## Régularité de la troncature et absence de mesure de bord

La fonction globale \(h=(\sigma F_j-\lambda/4)_+\) est lipschitzienne et
nulle sur la frontière de chaque composante de \(\{h>0\}\). Son morceau
\(G_\alpha=h\mathbf1_{C_\alpha}\), prolongé par zéro, reste lipschitzien :
pour un point intérieur et un point extérieur, tout segment joignant les deux
rencontre une frontière où \(h=0\), ce qui conserve la constante de
Lipschitz.

La règle de chaîne Sobolev donne donc

\[
 \nabla G_\alpha
 =\sigma\mathbf1_{C_\alpha}\nabla F_j
 \quad\text{presque partout}.                  \tag{13}
\]

Il n'apparaît aucune mesure surfacique sur \(\partial C_\alpha\) : la trace de
\(G_\alpha\) y est nulle. Par (1),

\[
 W_\alpha
 =\sigma\mathbf1_{C_\alpha}W_j
 \quad\text{presque partout}.                  \tag{14}
\]

L'égalité porte sur l'ouvert positif presque partout, pas littéralement sur
la fermeture topologique du support. Si le niveau \(\lambda/4\) possède une
zone de mesure positive, \(\nabla F_j=0\) presque partout sur cette zone et
(14) reste valable.

Les composantes sont disjointes, même si leurs fermetures se touchent. Les
connecteurs sur lesquels \(|F_j|<\lambda/4\) sont exactement supprimés par
(7).

## Fonctions de distribution et plateau local

Sur l'anneau,

\[
 \frac23\le\frac{R_j}{r}\le2.                 \tag{15}
\]

Tout point de \(\{|U|>\lambda\}\) vérifie
\(|F_j|>\lambda/2\) et appartient donc à un unique \(E_\alpha\). Ainsi, avec

\[
 V=\sum_\alpha V_\alpha,
\]

on a

\[
 V\ge\mu_U(\lambda).                           \tag{16}
\]

Sur \(E_\alpha\),

\[
 G_\alpha>\lambda/4,
 \qquad |U_\alpha|>\lambda/6,
\]

d'où

\[
 K_{u,\alpha}\ge\frac{\lambda}{6}V_\alpha^{1/3}. \tag{17}
\]

La quasi-norme de la somme n'est jamais remplacée par une somme de
quasi-normes ; seules (16) et les fonctions de distribution globales sont
utilisées.

## Coaire par composante

Posons

\[
 H_\alpha=C_\alpha\cap
 \{\lambda/4<\sigma F_j<\lambda/2\}.           \tag{18}
\]

Pour presque tout \(t\in(\lambda/4,\lambda/2)\), le superniveau

\[
 C_\alpha\cap\{\sigma F_j>t\}
\]

contient \(E_\alpha\). La coaire tridimensionnelle et (11) donnent

\[
 \int_{H_\alpha}|\nabla F_j|\,dx
 \ge\frac{C_I\lambda}{4}V_\alpha^{2/3}.        \tag{19}
\]

Par (15), (14) et (19),

\[
 \int_{H_\alpha}|W_\alpha|
 \ge\frac{C_I\lambda}{6}V_\alpha^{2/3}.        \tag{20}
\]

Il s'agit du périmètre de **chaque composante**. L'isopérimétrie donne
\(\sum_\alpha V_\alpha^{2/3}\), qui est au moins
\((\sum_\alpha V_\alpha)^{2/3}\), mais la preuve suivante conserve la somme
plus forte afin de sélectionner une composante.

## Sélection et constante 648

Soit

\[
 \varepsilon=\max_\alpha K_{u,\alpha}.
\]

L'équation (17) implique, pour chaque \(V_\alpha>0\),

\[
 V_\alpha^{1/3}\le\frac{6\varepsilon}{\lambda},
 \qquad
 V_\alpha^{2/3}
 =\frac{V_\alpha}{V_\alpha^{1/3}}
 \ge\frac{\lambda}{6\varepsilon}V_\alpha.      \tag{21}
\]

En sommant (20)--(21),

\[
 \int_H|W|
 =\sum_\alpha\int_{H_\alpha}|W_\alpha|
 \ge\frac{C_I\lambda^2}{36\varepsilon}V
 \ge\frac{C_I\lambda^2}{36\varepsilon}
       \mu_U(\lambda),                          \tag{22}
\]

où \(H=\bigcup_\alpha H_\alpha\). L'égalité ne subit aucune annulation,
car les bandes sont disjointes et (14) identifie leur module au module du
curl global.

Tout point de \(H\) satisfait

\[
 |U|>\frac23\frac\lambda4=\frac\lambda6,
\]

donc

\[
 |H|^{1/3}\le\mu_U(\lambda/6)^{1/3}
 \le\frac{6K_u}{\lambda}.                      \tag{23}
\]

L'inégalité faible-Lorentz donne en sens opposé

\[
 \int_H|W|
 \le3K_w|H|^{1/3}
 \le\frac{18K_wK_u}{\lambda}.                 \tag{24}
\]

La comparaison de (22) et (24) donne

\[
 \varepsilon
 \ge\frac{C_I}{648}
 \frac{\lambda^3\mu_U(\lambda)}{K_wK_u}
 \ge\frac{C_I(1-\eta)^3}{648}
       \frac{K_u^2}{K_w}.                      \tag{25}
\]

Ainsi

\[
 648=36\times18.                               \tag{26}
\]

En laissant \(\eta\downarrow0\), la finitude permet de choisir une
composante atteignant le maximum et donne (9). Par (14),

\[
 K_{w,\alpha_*}\le K_w,
\]

donc (10). Tous les facteurs \(6,36,18,648\) et tous les sens d'inégalité
sont cohérents.

## Annulation vectorielle locale

La bande \(H_\alpha\) seule ne convient pas au gate directionnel : en général

\[
 \int_{H_\alpha}W\,dx\ne0.                    \tag{27}
\]

Le bon objet est le curl complet de la troncature (7). Puisque
\(U_\alpha\) est compact et lipschitzien,

\[
 \int_{\mathbb R^3}W_\alpha\,dx=0.            \tag{28}
\]

L'identité est distributionnelle. Elle se vérifie aussi en cylindriques : la
composante radiale s'annule après intégration en \(\theta\), tandis que la
composante verticale contient
\(2\pi R_j\int\partial_rG_\alpha\,dr\,dz=0\).

Ainsi chaque goutte paie son propre retour vectoriel. Une annulation entre
gouttes éloignées ou seulement à l'échelle de la cellule entière n'est jamais
utilisée.

## Boule locale et extension directionnelle

L'hypothèse (6) place le support de \(W_\alpha\) dans une boule

\[
 B_\alpha=B((0,0,z_\alpha),C_\Lambda R_j),
 \qquad |B_\alpha|=O_\Lambda(R_j^3).           \tag{29}
\]

Sur \(\{W_\alpha\ne0\}\), (14) donne

\[
 \frac{W_\alpha}{|W_\alpha|}
 =\sigma\frac{W}{|W|}.                         \tag{30}
\]

Si \(\zeta\) est une extension globale de \(W/|W|\), alors
\(\sigma\zeta|_{B_\alpha}\) est une extension admissible de la direction de
\(W_\alpha\). Les éventuelles valeurs imposées par une autre goutte située
dans la même boule sont seulement des contraintes supplémentaires là où
\(W_\alpha=0\) ; le gate C33 vaut pour toute extension et reste applicable.
Comme la moyenne d'oscillation est invariante par multiplication globale par
\(-1\), C33 et (10) donnent (12).

### Objection explicite : interface lipschitzienne avec le cycle 0033

Le **théorème énoncé** au cycle 0033 commence avec un profil
\(C_c^\infty\), tandis que \(G_\alpha\) est en général seulement
\(W^{1,\infty}_c\). La composition n'est donc pas littéralement couverte par
la signature écrite de ce théorème.

Sa **preuve**, en revanche, s'étend sans changement substantiel : weak HLS
vaut pour le gradient faible, coaire vaut en BV, la règle de chaîne donne
(13), le curl compact a l'annulation (28), et la compensation conique est
mesurable. Une mollification naïve n'est pas la meilleure justification, car
elle fuit hors de \(C_\alpha\) et détruit l'identité exacte (30). Le raccord
correct est un lemme explicite « gate C33 pour profils
\(W^{1,\infty}_c\) », démontré directement par les mêmes étapes ou par une
approximation qui conserve la direction presque partout avant passage à la
limite.

**Verdict sur cette interface :** aucune objection analytique identifiée,
mais une dette d'énoncé existe. Tant que le lemme lipschitzien n'est pas ajouté
au registre, (12) reste une dérivation interne auditée, non une composition
formelle littérale de deux claims.

## Dépendance en \(m\) et modèle de copies identiques

Pour \(m\) copies translatées, disjointes et identiques d'un profil de goutte,
les fonctions de distribution sont exactement multipliées par \(m\). Si
\(k_u,k_w\) sont les endpoints d'une copie,

\[
 K_u=m^{1/3}k_u,
 \qquad
 K_w=m^{2/3}k_w,
 \qquad
 \frac{K_u}{K_w}=m^{-1/3}\frac{k_u}{k_w}.       \tag{31}
\]

La somme des quasi-normes n'est pas utilisée ; (31) vient du calcul exact des
distributions à chaque niveau. Sous \(K_u\ge\kappa>0\) et \(K_w\le K\),

\[
 m\le\left(\frac{k_uK}{k_w\kappa}\right)^3.    \tag{32}
\]

Des copies identiques ne fournissent donc aucun contre-exemple à gates
uniformes lorsque \(m\to\infty\). Pour des gouttes hétérogènes, leur nombre
peut être arbitraire si la plupart sont négligeables ; (9)--(10) sélectionnent
une goutte dominante avec une constante indépendante de \(m\).

## Finitude et composantes dénombrables

Tout ouvert de \(\mathbb R^3\) a au plus un nombre dénombrable de composantes.
Les sommes de (16), (20) et (22) passent à une famille dénombrable par
convergence monotone, et l'on peut remplacer le maximum par
\(\varepsilon=\sup_\alpha K_{u,\alpha}\).

La borne sur le supremum reste alors (25), mais celui-ci peut ne pas être
atteint. Pour tout \(c<C_I/648\), il existe néanmoins une composante vérifiant

\[
 K_{u,\alpha}\ge c\frac{K_u^2}{K_w},
 \qquad
 \frac{K_{u,\alpha}}{K_{w,\alpha}}
 \ge c\left(\frac{K_u}{K_w}\right)^2.          \tag{33}
\]

La finitude n'est donc nécessaire que pour atteindre la constante limite
exacte et pour éviter des questions d'accumulation géométrique. Une extension
dénombrable du gate exige en outre que chaque composante pertinente conserve
la même constante \(\Lambda\).

## Distinctions indispensables

1. **Goutte sélectionnée.** C'est le champ admissible tronqué
   \(U_\alpha=(R_j/r)G_\alpha e_\theta\), pas
   \(U_j\mathbf1_{C_\alpha}\). Cette restriction brute possède un saut de
   bord et son curl contient une mesure surfacique.
2. **Boule sélectionnée.** Elle contient le support du curl tronqué et permet
   l'annulation (28). La bande de coaire seule n'est pas un substitut.
3. **Cellule entière.** Elle peut avoir un diamètre axial arbitraire et ne
   tient dans aucune boule \(O(R_j)\). Le théorème ne prétend pas appliquer
   C33 au champ cellulaire complet.
4. **Connecteur sous \(\lambda/4\).** Il appartient au champ original mais est
   annulé par la troncature. S'il atteint \(\lambda/4\), il peut fusionner les
   composantes et faire perdre (6) ; c'est exactement la frontière du
   théorème.

## Scaling

Sous

\[
 U_\rho(x)=\rho U(\rho x),
 \qquad W_\rho(x)=\rho^2W(\rho x),
 \qquad R_{j,\rho}=R_j/\rho,
\]

les endpoints globaux et locaux sont invariants. Le niveau devient
\(\rho\lambda\), les volumes deviennent \(\rho^{-3}V_\alpha\), et

\[
 \lambda V_\alpha^{2/3}\mapsto
 \rho^{-1}\lambda V_\alpha^{2/3},
 \qquad
 \int|W_\alpha|\mapsto\rho^{-1}\int|W_\alpha|.
\]

Les conclusions (9), (10) et (12) sont critiques ; ni \(m\), ni les distances
entre gouttes n'entrent dans les constantes.

## Passe adverse, premier quantificateur faux et falsificateur

- **Périmètres additionnés.** Coaire est appliquée séparément à chaque
  composante avant sommation ; remplacer
  \(\sum V_\alpha^{2/3}\) par seulement \(V^{2/3}\) perdrait précisément la
  sélection locale.
- **Annulation globale prise pour locale.** La bande ne s'annule pas. Le curl
  de la troncature complète s'annule exactement, ce qui ferme l'attaque.
- **Distances arbitraires.** Elles n'affectent ni les distributions ni coaire.
  Elles empêchent seulement de mettre la cellule entière dans une boule.
- **Recouvrement.** Si des supports complets de cellules différentes se
  recouvrent, (14) et l'égalité dans (22) peuvent échouer par annulation ; ce
  cas n'est pas couvert.
- **PDE.** Aucune pression, diffusion, évolution ou sélection d'échelle
  pré-singulière n'est obtenue.

Le **premier quantificateur faux** de l'approche négative est : « une cellule
de grand diamètre doit être placée tout entière dans la boule du gate ». Il
suffit de sélectionner une composante du superniveau inférieur et de la
fermer par une troncature à trace nulle. À l'inverse, l'énoncé « toute
composante pertinente tient dans une boîte \(O(R_j)\) » reste une hypothèse,
pas une conséquence des gates.

Un falsificateur décisif de (9)--(10) serait une famille finie satisfaisant
(1)--(8), avec

\[
 \max_\alpha K_{u,\alpha}
 <\frac{C_I}{648}\frac{K_u^2}{K_w}.
\]

Il devrait nécessairement exhiber une mesure de bord absente de (13), une
défaillance du périmètre par composante, une annulation sur des supports non
disjoints, ou une erreur dans la fonction de distribution (23). Un
falsificateur de la conclusion directionnelle (12) pourrait aussi viser
l'extension du gate C33 à \(W^{1,\infty}_c\) ; c'est le prochain test formel
minimal.

**État :** `CONTINUER` pour la sélection endpoint ; `À REPRENDRE` pour rendre
explicite le gate lipschitzien et pour les composantes dont le diamètre axial
n'est pas \(O(R_j)\).
