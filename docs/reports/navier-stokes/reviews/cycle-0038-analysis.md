# Cycle 0038 — Calibration des ponts ou arbre de fusion

**Statut :** `AI_INTERNAL_DERIVATION` — ne pas classer `PAPER_PROOF`

**Verrou :** `GAP-BRIDGE-SCALE-CALIBRATION-OR-MERGE-TREE`.

**Verdict :** la dichotomie binaire uniforme ne se déduit pas des claims C36
et C37. Le rapport endpoint n'est pas monotone le long d'une retroncature et
une suite arbitrairement profonde de fusions à persistance évanescente est
compatible avec toutes leurs inégalités. Une trichotomie quantitative est en
revanche démontrable : goutte déjà bornée, branche longue nécessairement non
calibrée, ou niveau de scission géométrique sans contrôle endpoint hérité.
L'arbre abstrait exact réfute toute conclusion à constantes indépendantes de
sa profondeur. Il ne constitue pas encore une réalisation lisse pure-swirl de
tout l'arbre.

## Cadre et quantificateurs

Soit une troncature pure-swirl déjà sélectionnée

\[
 G_A=\mathbf1_C(\sigma F-A)_+,
 \qquad
 U_A=\frac RrG_Ae_\theta,
 \qquad
 W_A=\operatorname{curl}U_A,                  \tag{1}
\]

supportée dans \(R/2<r<3R/2\). Notons

\[
 K=\|U_A\|_{L^{3,\infty}}>0,
 \qquad
 L=\|W_A\|_{L^{3/2,\infty}},
 \qquad q=K/L>0.                               \tag{2}
\]

Le cutoff \(A\) n'est pas une quasi-norme : il dépend du niveau absolu choisi
avant la troncature. Les quatre rapports critiques sont

\[
 q,\qquad \frac{AR}{K},\qquad \frac DR,
 \qquad \frac{b-A}{A}.                         \tag{3}
\]

Une dichotomie « bornée » doit fixer ses quantificateurs. La version naturelle
la plus forte serait la suivante.

> Pour tout \(q_0>0\), il existe
> \(\kappa,\Lambda,c,\beta>0\), dépendant seulement de \(q_0\), tels que
> toute composante vérifiant \(q\ge q_0\) contient soit une branche de
> superniveaux persistante avec \(sR\ge\kappa K\), soit une retroncature à un
> niveau supérieur, supportée dans une boîte axiale de taille
> \(\Lambda R\), dont la vitesse est au moins \(cK\) et le rapport endpoint
> au moins \(cq^\beta\).

Sans la minoration de la vitesse locale, une pointe arbitrairement petite mais
de bon rapport rendrait la seconde alternative sans effet pour le programme.
Sans une puissance ou une fonction explicite de \(q\), le mot « uniforme »
n'a pas de contenu falsifiable.

## Ce que C36 fournit en une étape

Appliquons C36 à \(G_A\). Pour \(0<\eta<1\), choisissons \(\lambda>0\) tel
que

\[
 \lambda|\{|U_A|>\lambda\}|^{1/3}
 \ge(1-\eta)K.                                 \tag{4}
\]

Avec

\[
 c_H=C_I/648,
\]

C36 sélectionne une composante \(C_1\) de
\(\{\tau G_A>\lambda/4\}\), rencontrant
\(\{\tau G_A>\lambda/2\}\), et sa troncature \(U_1\) vérifie

\[
 K_1:=\|U_1\|_{L^{3,\infty}}
 \ge c_H(1-\eta)^3qK,                          \tag{5}
\]

\[
 q_1:=\frac{K_1}{L_1}
 \ge c_H(1-\eta)^3q^2.                         \tag{6}
\]

Ces bornes ne dépendent ni du nombre de composantes ni de leurs distances.
Elles concernent exactement \(C_1\) au cutoff inférieur
\(s=\lambda/4\). Elles ne sont transmises à aucun descendant défini à un
autre niveau.

## Trichotomie quantitative démontrable

Fixons \(\Lambda>1\). Pour les composantes des superniveaux de \(G_A\) dans
la bande

\[
 I=(\lambda/4,\lambda/2),
\]

une des trois situations suivantes a lieu.

### L — composante localisée

La composante sélectionnée par C36 satisfait

\[
 \operatorname{diam}_z C_1\le\Lambda R.        \tag{7}
\]

Alors (5)--(6) donnent directement une goutte endpoint, et le gate
directionnel lipschitzien de C36 s'applique dans une boule
\(O_\Lambda(R)\).

### P — diamètre persistant

Pour presque tout \(t\in I\), une composante du superniveau
\(\{\tau G_A>t\}\) a un diamètre axial au moins \(\Lambda R\). C37, avec

\[
 a=\lambda/4,
 \qquad b=\lambda/2,
 \qquad D=\Lambda R,
\]

donne

\[
 \frac{\lambda^2}{16}R(\Lambda R)
 \le\frac{9}{8\pi}KL.
\]

Ainsi

\[
 \boxed{
 \frac{\lambda R}{K}
 \le\left(\frac{18}{\pi\Lambda q}\right)^{1/2}}. \tag{8}
\]

Une branche longue n'est donc pas forcée d'être calibrée ; C37 impose au
contraire que son niveau soit **petit** relativement à \(K/R\) lorsque
\(\Lambda q\) est grand.

Si l'on suppose séparément

\[
 \frac{\lambda R}{4}\ge\kappa K,               \tag{9}
\]

alors C37 donne

\[
 \frac DR\le\frac{9}{8\pi\kappa^2q}.          \tag{10}
\]

En choisissant
\(\Lambda>9/(8\pi\kappa^2q)\), les situations P et (9) sont incompatibles.
Mais (9) reste une hypothèse, jamais une conséquence de C36.

### M — scission dans la bande

La situation P échoue. Il existe alors un ensemble de niveaux de mesure
positive dans \(I\) pour lesquels toutes les composantes pertinentes ont un
diamètre inférieur à \(\Lambda R\). C'est une information géométrique réelle
sur l'arbre de fusion.

Elle ne fournit cependant ni

\[
 \|U_t\|_{L^{3,\infty}}\gtrsim K,
 \qquad\text{ni}\qquad
 \frac{\|U_t\|_{L^{3,\infty}}}
      {\|\operatorname{curl}U_t\|_{L^{3/2,\infty}}}
 \gtrsim q^\beta                              \tag{11}
\]

pour une composante au niveau \(t\). Les ratios de deux quasi-normes
décroissantes ne sont pas monotones sous retroncature. C'est exactement le
troisième cas omis par la dichotomie proposée.

## Premier quantificateur faux

Le passage incorrect est

\[
 \exists C_1\text{ bon au cutoff }\lambda/4
 \quad\Longrightarrow\quad
 \exists t>\lambda/4\text{ dont un descendant géométriquement borné
 hérite des mêmes gates}.                      \tag{12}
\]

C36 choisit simultanément un niveau et une composante. Après déplacement du
niveau, la fonction de distribution de la vitesse et celle du curl changent
à des seuils différents. On sait seulement

\[
 K_u(t_2)\le K_u(t_1),
 \qquad
 K_w(t_2)\le K_w(t_1)
 \quad(t_2>t_1),                               \tag{13}
\]

mais aucun sens n'est imposé à \(K_u(t)/K_w(t)\). Échanger le quantificateur
« il existe un couple niveau--composante » avec « il existe un descendant à
un niveau de scission choisi géométriquement » est donc illégitime.

## Contre-modèle abstrait exact : arbre de profondeur arbitraire

Ce modèle ne prétend pas être déjà un potentiel pure-swirl lisse. Il montre
que les **seules conclusions numériques de C36 et C37** ne peuvent impliquer
une dichotomie uniforme.

Fixons \(0<q_0<1\), \(K_0=1\) et \(c_H=C_I/648<1\). Pour
\(n=0,\ldots,N-1\), définissons récursivement

\[
 q_{n+1}=c_Hq_n^2,
 \qquad
 K_{n+1}=c_Hq_nK_n,
 \qquad
 L_n=K_n/q_n.                                  \tag{14}
\]

Alors, exactement,

\[
 K_{n+1}=c_H\frac{K_n^2}{L_n},
 \qquad
 q_{n+1}=c_H\left(\frac{K_n}{L_n}\right)^2.   \tag{15}
\]

Chaque arête de l'arbre sature donc les deux minorations C36. Les formules
fermées sont

\[
 q_n=c_H^{2^n-1}q_0^{2^n},                    \tag{16}
\]

et

\[
 K_n=K_0\prod_{j=0}^{n-1}(c_Hq_j).
\]

Ainsi \(q_n\to0\) et \(K_n\to0\) plus vite qu'une progression géométrique.

À chaque profondeur, choisissons un rapport de cutoff

\[
 \varepsilon_n=\frac{A_nR}{K_n}<\kappa        \tag{17}
\]

et une longueur \(D_n=M_nR\), avec \(M_n\) arbitrairement grande. Pour que
le budget C37 soit respecté sur une fenêtre relative
\(b_n-A_n=\theta_nA_n\), il suffit de poser

\[
 0<\theta_n
 \le\frac{9}{16\pi}
       \frac{1}{q_n\varepsilon_n^2M_n}.        \tag{18}
\]

En effet,

\[
 A_n(b_n-A_n)RD_n
 =\theta_n\varepsilon_n^2K_n^2M_n
 \le\frac{9}{16\pi}\frac{K_n^2}{q_n}
 <\frac{9}{8\pi}K_nL_n.                       \tag{19}
\]

Les ponts peuvent donc être arbitrairement longs à chaque étage, pourvu que
leur persistance verticale \(\theta_n\) décroisse. Après cette fenêtre, une
fusion se défait et le descendant \(n+1\) porte exactement le budget (15).

Tous les frères hors du chemin principal peuvent recevoir des endpoints
strictement inférieurs à ceux du descendant. À la profondeur \(N\), déclarons
la feuille géométriquement bornée. Pour toutes constantes proposées
\(c_*>0\) et \(\Phi(q_0)>0\), choisir \(N\) assez grand donne

\[
 K_N<c_*K_0,
 \qquad q_N<\Phi(q_0).                         \tag{20}
\]

L'arbre satisfait donc à chaque étage les bornes disponibles, ne possède
aucune branche calibrée par (17), et n'atteint une géométrie bornée qu'après
perte arbitraire du budget endpoint. Cela réfute toute dichotomie à constantes
indépendantes de la profondeur **comme conséquence logique de C36--C37**.

## Réalisabilité et portée du contre-modèle

Tout arbre fini peut être réalisé topologiquement comme arbre de fusion d'une
fonction de Morse lisse. Cette observation ne suffit pas à réaliser
simultanément les valeurs prescrites de \(K_n,L_n\) et l'identité
\(W=\operatorname{curl}U\). Les parois, caps et raccords de chaque étage
doivent encore être comptés dans la même fonction de distribution globale.

Le contre-modèle établit donc le résultat négatif précis suivant :

\[
 \boxed{
 \text{C36 + C37 + scaling n'impliquent pas la dichotomie bornée.}} \tag{21}
\]

Il ne constitue pas encore un contre-exemple pure-swirl lisse au renforcement
universel. Une preuve positive devrait utiliser une information absente des
deux claims : borne de profondeur, budget cumulatif de variation sur l'arbre,
quasi-additivité des endpoints entre générations, ou contrôle quantitatif des
valeurs critiques.

## Fusions multiples et absence de borne de profondeur

La compacité et la marge entre deux niveaux rendent fini le nombre de
composantes actives dans une **bande fixée**, comme en C36. Elles ne bornent
pas uniformément le nombre de valeurs critiques lorsqu'on retronque
successivement. Une suite de fonctions lisses peut avoir un nombre de selles
arbitrairement grand, et une fonction \(C^\infty\) non Morse peut même avoir
une structure critique infinie.

La coaire fournit un budget additif

\[
 2\pi R\int\sum_i\operatorname{Per}_2(E_{t,i})\,dt,      \tag{22}
\]

mais une persistance \(\theta_n\) arbitrairement petite rend sommable le coût
de branches de longueurs arbitraires. C37 facture

\[
 \text{diamètre}\times\text{largeur verticale},        \tag{23}
\]

pas le nombre de fusions. Aucun argument de pigeonhole ne fournit donc un
étage de largeur verticale relative uniforme sans un budget d'entropie
supplémentaire.

## Fonctions de distribution : test adverse minimal

Même hors géométrie, le rapport endpoint n'est pas héréditaire. Prenons un
couple parent de fonctions étagées de quasi-normes

\[
 K_u=1,\qquad K_w=1,
\]

et une partie haute imbriquée ayant

\[
 K_u^{\rm high}=\epsilon,
 \qquad K_w^{\rm high}=1.                      \tag{24}
\]

Les deux quasi-normes diminuent lors du passage à la partie haute, mais le
rapport passe de un à \(\epsilon\). Des fonctions indicatrices sur des
ensembles emboîtés réalisent exactement ces quatre valeurs après choix de
l'amplitude et du volume. Ce modèle n'est pas curl-compatible ; il isole le
quantificateur analytique qu'une réalisation pure-swirl devrait empêcher.

La règle correcte est de recalculer les deux fonctions de distribution après
chaque retroncature. Ni le périmètre du niveau de scission, ni la topologie de
l'arbre ne déterminent leur quotient.

## Scaling

Sous

\[
 U_\rho(x)=\rho U(\rho x),
 \qquad W_\rho(x)=\rho^2W(\rho x),
 \qquad R_\rho=R/\rho,
\]

les quantités \(K_n,L_n,q_n\), \(A_nR/K_n\), \(D_n/R\) et
\((b_n-A_n)/A_n\) sont invariantes. Les récurrences (14), la contrainte (18)
et la trichotomie L/P/M sont donc critiques. Une normalisation d'amplitude ou
de rayon ne supprime pas la profondeur de l'arbre.

## Passe contradictoire

1. **Cutoff absolu contre excès tronqué.** \(A\) et la quasi-norme de
   \((F-A)_+\) ne sont pas comparables sans hypothèse supplémentaire.
2. **Bon parent contre bon enfant.** Le quotient des endpoints n'est pas
   monotone sous restriction, même si chaque endpoint l'est séparément.
3. **Persistance à un niveau unique.** C37 exige une fenêtre de niveaux de
   mesure positive ; un pont rasant le cutoff échappe avec un coût
   proportionnel à cette fenêtre.
4. **Composante longue à niveau bas.** Elle peut se scinder avant le niveau
   haut ; son diamètre n'est alors pas persistant.
5. **Finitude locale contre profondeur uniforme.** Un nombre fini de
   composantes par bande ne borne pas le nombre d'itérations.
6. **Somme de périmètres.** Elle contrôle le coût BV total, pas la répartition
   des deux quasi-normes faibles entre générations.
7. **Réalisation abstraite prise pour un curl.** L'arbre (14)--(20) est un
   contre-modèle logique des claims, pas encore une famille
   \(F\in C_c^\infty\) certifiée.
8. **Direction.** Le gate directionnel ne s'applique qu'après sélection d'une
   troncature de diamètre \(O(R)\) ayant conservé son rapport endpoint.
9. **PDE.** Pression, projection de Leray, diffusion, stretching et évolution
   ne figurent dans aucun étage.

## Résultat, falsificateur et prochaine réduction

La dichotomie binaire uniforme est **`RÉVISER`** : elle devient correcte
seulement après ajout d'une hypothèse contrôlant la profondeur ou la perte
endpoint à travers les fusions. La trichotomie L/P/M est **`CONTINUER`**.

Un falsificateur complet du renforcement pure-swirl serait une famille
explicite \(F_N\in C_c^\infty\) réalisant des arbres de profondeur
\(N\to\infty\), avec rapport racine \(q_0>0\) uniforme, aucune branche
calibrée, et tout descendant de diamètre \(O(R)\) satisfaisant

\[
 \frac{K_{u,\mathrm{desc}}}{K_{w,\mathrm{desc}}}\to0
 \quad\text{ou}\quad
 K_{u,\mathrm{desc}}/K_0\to0.                 \tag{25}
\]

La prochaine réduction falsifiable est un **lemme de budget d'arbre** :
prouver qu'une fonction pure-swirl impose

\[
 \sum_{\text{générations}}\Psi(q_n,K_n/K_0)\le C(q_0) \tag{26}
\]

pour une fonction coercive \(\Psi\), ou construire un profil lisse à étages
qui viole toute telle coercivité tout en suivant les parois et caps. Sans
(26), l'itération de C36 dégrade les constantes comme (16) et ne ferme pas le
gate directionnel.

## Addendum contradictoire du 2026-08-15 — lemme adaptatif one-cell

Cet addendum audite un renforcement utilisant une donnée absente de l'arbre
abstrait précédent : la largeur radiale uniforme de l'anneau. Le résultat est
positif et invalide cet arbre comme obstruction au lemme one-cell précis.

### Énoncé et verdict

Soient

\[
 F\in C_c^\infty((0,\infty)\times\mathbb R),\qquad
 \operatorname{supp}F\subset\{R/2<r<3R/2\},
\]

\[
 U=(R/r)Fe_\theta,\quad W=\operatorname{curl}U,\quad
 K=\|U\|_{L^{3,\infty}}>0,\quad
 H=\|W\|_{L^{3/2,\infty}},\quad q=K/H.          \tag{A1}
\]

Choisissons \(\lambda>0\) avec

\[
 \lambda\mu_U(\lambda)^{1/3}\ge K/2.          \tag{A2}
\]

Pour les cores signés

\[
 E_\sigma=\{\sigma F>\lambda/2\},\qquad
 V=\sum_{\sigma=\pm1}|E_\sigma|_3,             \tag{A3}
\]

les deux conclusions annoncées sont valides :

\[
 \boxed{\lambda R\ge K^2/(432H)},              \tag{A4}
\]

et il existe un niveau régulier
\(t\in(\lambda/4,3\lambda/8)\) et une composante active
\(C_\beta\) de \(\{\sigma F>t\}\) telle que, pour

\[
 G_\beta=\mathbf1_{C_\beta}(\sigma F-t)_+,
 \qquad U_\beta=(R/r)G_\beta e_\theta,
\]

\[
 \frac{\operatorname{diam}_zC_\beta}{R}
 \le2\,239\,488q^{-3},                         \tag{A5}
\]

\[
 K_\beta\ge\frac{C_I}{20\,736}\frac{K^2}{H},
 \qquad
 q_\beta\ge\frac{C_I}{20\,736}q^2.           \tag{A6}
\]

Une composante est active si elle rencontre le core de même signe.

### Preuve de la calibration 432

Sur l'anneau,

\[
 2/3\le R/r\le2.                               \tag{A7}
\]

Ainsi \(\{|U|>\lambda\}\subset\{|F|>\lambda/2\}\), et (A2) donne

\[
 V\ge\mu_U(\lambda)\ge K^3/(8\lambda^3).      \tag{A8}
\]

Si un ensemble méridien \(E\) est contenu dans une bande radiale de largeur
\(R\), le tranchage horizontal donne

\[
 \operatorname{Per}_2(E)\ge2|E|_2/R.          \tag{A9}
\]

Son volume de révolution vérifie

\[
 |\operatorname{Rot}E|_3
 =2\pi\int_Er\,dr\,dz\le3\pi R|E|_2.          \tag{A10}
\]

Pour \(s\in(\lambda/4,\lambda/2)\), le superniveau signé contient son core.
Les équations (A9)--(A10), puis la coaire cylindrique exacte, donnent

\[
 \begin{aligned}
 \int_{\{\lambda/4<|F|<\lambda/2\}}|W|\,dx
 &=2\pi R\sum_\sigma\int_{\lambda/4}^{\lambda/2}
   \operatorname{Per}_2(\{\sigma F>s\})\,ds\\
 &\ge\lambda V/(3R).                           \tag{A11}
 \end{aligned}
\]

La bande est contenue dans \(\{|U|>\lambda/6\}\). L'intégration faible-
\(L^{3/2}\), avec constante trois, donne

\[
 \int_{\{\lambda/4<|F|<\lambda/2\}}|W|
 \le18HK/\lambda.                              \tag{A12}
\]

Donc \(\lambda^2V\le54RHK\). Avec (A8),

\[
 K^3/(8\lambda)\le54RHK,
\]

ce qui est exactement (A4). Le cas \(H=0\) est incompatible avec \(K>0\),
car (A1) et la compacité donnent alors \(\nabla F=0\), puis \(F=0\).

### Niveau moyen et constante de diamètre

Posons \(I=(\lambda/4,3\lambda/8)\), de longueur \(\lambda/8\). Pour presque
tout niveau régulier, le périmètre des composantes actives donne

\[
 2\sum_\beta\operatorname{diam}_zC_\beta(t)
 \le\sum_\sigma\operatorname{Per}_2(\{\sigma F>t\}). \tag{A13}
\]

Coaire et Lorentz sur la bande associée impliquent

\[
 \int_I\sum_\beta\operatorname{diam}_zC_\beta(t)\,dt
 \le\frac{9HK}{2\pi\lambda R}.                \tag{A14}
\]

Il existe donc un niveau régulier \(t\in I\) tel que

\[
 \sum_\beta\frac{\operatorname{diam}_zC_\beta(t)}R
 \le\frac{36HK}{\pi\lambda^2R^2}.             \tag{A15}
\]

En utilisant (A4) puis \(\pi>3\),

\[
 \frac{36HK}{\pi\lambda^2R^2}
 \le\frac{36\cdot432^2}{\pi}q^{-3}
 <12\cdot432^2q^{-3}
 =2\,239\,488q^{-3}.                           \tag{A16}
\]

Chaque composante active au niveau choisi satisfait donc (A5), pas seulement
la somme en moyenne.

### Finitude et sélection endpoint au même niveau

Le compact \(\{\sigma F\ge\lambda/2\}\) est contenu avec une marge
\(\lambda/8\) dans l'ouvert \(\{\sigma F>t\}\). Les composantes de cet
ouvert forment un recouvrement ouvert disjoint du compact ; une
sous-couverture finie montre que seules un nombre fini de composantes sont
actives. Leur endpoint maximal est atteint.

Notons

\[
 \begin{aligned}
 V_\beta&=|C_\beta\cap E_\sigma|_3,\\
 \varepsilon&=\max_\beta K_\beta,\\
 \sum_\beta V_\beta&=V.
 \end{aligned}                                  \tag{A17}
\]

Sur le core, puisque \(t<3\lambda/8\),

\[
 G_\beta>\lambda/8,\qquad |U_\beta|>\lambda/12.
\]

Par conséquent,

\[
 K_\beta\ge(\lambda/12)V_\beta^{1/3},\qquad
 V_\beta^{2/3}\ge\frac{\lambda}{12\varepsilon}V_\beta. \tag{A18}
\]

Pour \(s\in(3\lambda/8,\lambda/2)\), le superniveau contenu dans
\(C_\beta\) contient son core. Coaire tridimensionnelle, isopérimétrie et
\(R/r\ge2/3\) donnent

\[
 \int|W_\beta|\,dx
 \ge(C_I\lambda/12)V_\beta^{2/3}.              \tag{A19}
\]

Après sommation,

\[
 \sum_\beta\int|W_\beta|
 \ge\frac{C_I\lambda^2V}{144\varepsilon}.     \tag{A20}
\]

L'union des supports positifs est contenue dans
\(\{|U|>\lambda/6\}\), donc le membre gauche est au plus
\(18HK/\lambda\). Avec (A8),

\[
 \varepsilon\ge
 \frac{C_I}{20\,736}\frac{K^2}{H},            \tag{A21}
\]

où \(20\,736=144\cdot18\cdot8\). Restreindre aussi la borne supérieure à
la bande fixe \(3\lambda/8<|F|<\lambda/2\) remplacerait \(18\) par \(12\)
et améliorerait le dénominateur en \(13\,824\), mais le claim conservateur
est correct.

### Troncature par composante et domination de \(H_\beta\)

La fonction \(h=(\sigma F-t)_+\) est lipschitzienne et nulle sur
\(\partial C_\beta\). Son morceau prolongé par zéro reste lipschitzien et la
règle de chaîne Sobolev donne

\[
 \nabla G_\beta=\sigma\mathbf1_{C_\beta}\nabla F,
 \qquad
 W_\beta=\sigma\mathbf1_{C_\beta}W
 \quad\text{presque partout}.                  \tag{A22}
\]

Il n'existe aucune mesure de bord. La domination pointwise entraîne celle
des fonctions de distribution :

\[
 H_\beta:=\|W_\beta\|_{L^{3/2,\infty}}\le H.  \tag{A23}
\]

La composante qui atteint \(\varepsilon\) satisfait simultanément (A5),
(A6) et

\[
 K_\beta/H_\beta\ge K_\beta/H
 \ge(C_I/20\,736)q^2,                          \tag{A24}
\]

ce qui prouve le claim complet.

### Passe contradictoire finale

1. Le facteur \(R/r\le2\) donne l'inclusion dans le sens requis pour (A8).
2. Aire méridienne et volume 3D sont séparés par le facteur \(3\pi R\) de
   (A10), source du facteur 432.
3. Les deux signes sont disjoints et reconstruisent la bande de \(|F|\).
4. Sard laisse un ensemble plein de niveaux réguliers dans l'estimation
   moyenne ; le niveau choisi peut donc être régulier.
5. La finitude concerne seulement les composantes rencontrant le core, pas
   toutes les composantes du superniveau.
6. Le niveau est choisi d'abord par la moyenne des diamètres ; la sélection
   endpoint est ensuite faite parmi les composantes de ce **même** niveau.
7. La frontière de niveau ne crée aucun curl singulier grâce à la trace nulle
   de la troncature.
8. \(H_\beta\le H\) est une domination pointwise avant passage à Lorentz,
   non une inégalité triangulaire de quasi-normes.
9. \(\lambda R\), \(K^2/H\), les rapports endpoint et
   \(\operatorname{diam}_z/R\) sont invariants sous le scaling
   Navier--Stokes.

**Premier quantificateur faux recherché : aucun dans l'énoncé audité.** Le
premier prolongement faux serait de fixer \(t\) avant la moyenne, ou d'exiger
une constante de diamètre indépendante de \(q\).

**Verdict exact : `VALIDER_COMME_DÉRIVATION_INTERNE`.** Les constantes
\(432\), \(20\,736\) et \(2\,239\,488\) sont correctes. Le résultat ferme le
contre-modèle logique (14)--(20) dans la classe one-cell pure-swirl annulaire :
la largeur radiale et la sélection moyenne du niveau fournissent le budget
d'arbre manquant. Il reste statique, pure-swirl et sans évolution de
Navier--Stokes.
