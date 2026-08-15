# Cycle 0041 — revue primaire : lissage local et concentration critique Type I

Date de coupure : **2026-08-15**

Objet : audit intégral des deux articles Barker–Prange consacrés au lissage
local et à la concentration quantitative près d'une singularité Type I, avec
une vérification spécifique du endpoint `L^{3,\infty}`, des quantificateurs en
temps et en rayon, et de l'absence de raccord automatique aux scénarios Type
II ou au problème Clay.

## Verdict

Les deux articles établissent des résultats robustes mais strictement
**conditionnels à un contrôle critique uniforme**.

1. Barker–Prange 2020 démontre un lissage local à partir d'une petite donnée
   `L^3` locale, sous contrôle global `L^2_{uloc}`, puis en déduit qu'une
   singularité Type I satisfaisant une borne locale de Morrey-énergie doit
   concentrer une quantité `L^3` universelle sur une boule de rayon
   parabolique `C(M)\sqrt{T_*-t}` à **tout** temps suffisamment proche de
   `T_*`. L'appendice étend le mécanisme à une petite donnée locale
   `L^{3,\infty}`, avec des constantes ajustées.
2. Barker–Prange 2021 part de la borne globale
   `u\in L^\infty_tL^{3,\infty}_x`, qu'il appelle Type I. À chaque temps
   assez proche d'un premier temps singulier, il obtient sur une boule un peu
   plus grande que l'échelle parabolique une minoration logarithmique de
   **l'intégrale** `\int |u|^3`, et non directement une minoration
   logarithmique de la norme `L^3`.
3. Les trois notions parfois regroupées sous « Type I » ne sont pas
   identiques : borne ponctuelle
   `\sqrt{T_*-t}\,\|u(t)\|_\infty`, borne locale de Morrey-énergie de 2020,
   et borne globale faible-`L^3` de 2021. La dernière implique la borne de
   Morrey locale, mais les réciproques utiles ne sont pas établies ici.
4. La conclusion 2021 est compatible avec l'hypothèse faible-`L^3` : un
   profil critique `|x|^{-1}` possède une norme `L^{3,\infty}` bornée alors
   que son intégrale cubique sur des couronnes emboîtées croît
   logarithmiquement. Le théorème impose donc une concentration nécessaire;
   il ne produit pas une contradiction et n'exclut pas un blow-up Type I.
5. Le passage Type II échoue exactement sur l'uniformité. Après zoom, la
   constante critique effective peut tendre vers l'infini; le temps de
   lissage, le rayon utile, les bonnes époques et les constantes de Carleman
   dégénèrent. Dans les limites eulériennes Type II, la viscosité peut en
   outre disparaître.
6. La veille primaire 2025–2026 ne fournit pas de prolongement général de ces
   résultats au Type II. Elle apporte des exclusions pour des profils
   structurés, des réductions eulériennes conditionnelles et des critères
   supplémentaires. Tous les documents pertinents sont déjà présents dans le
   catalogue sous les identifiants `NS-SRC-0032`, `0034`, `0035`, `0045`,
   `0048`, `0051` et `0059`; aucun nouvel identifiant après `0179` n'est
   recommandé.

Le maillon transférable est donc : **une borne critique Type I uniforme rend
quantitativement persistante une concentration locale forte près d'un point
singulier connu**. Le maillon manquant reste : **déduire de l'énergie Clay
une telle borne uniforme, ou convertir la concentration compatible avec
`L^{3,\infty}` en contradiction ou en théorème de rigidité**.

## 1. Équation, solutions et échelle

Les deux articles étudient les Navier–Stokes incompressibles non forcées sur
l'espace entier :

\[
\partial_tu-\Delta u+(u\cdot\nabla)u+\nabla p=0,
\qquad \nabla\cdot u=0,
\qquad (x,t)\in\mathbb R^3\times I.
\]

La viscosité est normalisée à `\nu=1`; il n'y a ni frontière ni force
extérieure. La remise à l'échelle est

\[
u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),
\qquad
p_\lambda(x,t)=\lambda^2p(\lambda x,\lambda^2t),
\qquad
\omega_\lambda(x,t)=\lambda^2\omega(\lambda x,\lambda^2t).
\]

Les quantités utilisées ont les lois suivantes :

| Quantité | Loi sous remise à l'échelle | Statut |
|---|---:|---|
| `\|u(t)\|_{L^3}` et `\|u(t)\|_{L^{3,\infty}}` | invariante | critique |
| `r^{-1/2}\|u(t)\|_{L^2(B_r)}` | invariante | critique locale |
| `\int_{B_r}|u|^3` | invariante si la boule est redimensionnée | critique locale |
| `r\int_{B_r}|\omega|^2` | invariante | enstrophie locale critique |
| `\sqrt{T_*-t}\,\|u(t)\|_\infty` | invariante | Type I ponctuel classique |

Sous une borne `\|u(t)\|_{L^{3,\infty}(\mathbb R^3)}\le M`, l'inégalité de
Lorentz sur une boule donne

\[
r^{-1/2}\|u(t)\|_{L^2(B_r(x_0))}\le C M.
\]

Ainsi, le Type I global faible-`L^3` de 2021 implique le contrôle local de
2020, à changement de constante près. Cette implication ne donne ni petite
norme locale faible-`L^3`, ni contrôle fort `L^3`, ni borne issue de
l'inégalité d'énergie.

## 2. Barker–Prange 2020 : lissage localisé

### 2.1 Source et statut

- Tobias Barker et Christophe Prange, *Localized smoothing for the Navier–
  Stokes equations and concentration of critical norms near singularities*,
  `arXiv:1812.09115v2`, soumis le 21 décembre 2018, version 2 du 9 janvier
  2019.
- Publication : *Archive for Rational Mechanics and Analysis* **236**
  (2020), 1487–1541, DOI
  [`10.1007/s00205-020-01495-6`](https://doi.org/10.1007/s00205-020-01495-6).
- Texte primaire audité :
  [`arXiv:1812.09115v2`](https://arxiv.org/abs/1812.09115v2), notamment les
  théorèmes 1–2, la preuve du théorème 2 et l'appendice B.

Statut : **preuve analytique publiée**, sans composante assistée par
ordinateur.

### 2.2 Notion de solution

Le théorème de lissage porte sur une **solution d'énergie locale** sur
`\mathbb R^3\times(0,T)`. Les hypothèses comprennent la formulation
distributionnelle, les bornes locales d'énergie, l'inégalité d'énergie
locale et une décomposition admissible de la pression. Le théorème de
concentration est appliqué à une solution faible de **Leray–Hopf** sur
`\mathbb R^3\times(0,\infty)`; celle-ci fournit le contrôle global d'énergie
et appartient au cadre local requis après translation et remise à l'échelle.

Ce ne sont ni des solutions sur le tore, ni des solutions avec frontière, ni
des solutions d'Euler, ni des solutions forcées.

### 2.3 Théorème 1 : énoncé exact utile

Pour tout `M>0`, il existe

\[
S^*(M)\in(0,1/4]
\]

et une constante universelle `\gamma_{univ}>0` tels que le résultat suivant
soit vrai. Soit `u` une solution d'énergie locale dont la donnée initiale
solénoïdale satisfait

\[
u_0\in L^2_{uloc,\sigma}(\mathbb R^3),
\qquad
\|u_0\|_{L^2_{uloc}}\le M,
\]

avec disparition de la queue locale

\[
\sup_{|\bar x|\ge R}\|u_0\|_{L^2(B_1(\bar x))}\longrightarrow0
\quad(R\to\infty),
\]

et petite donnée critique sur la boule `B_2` :

\[
u_0\in L^3(B_2),
\qquad
\|u_0\|_{L^3(B_2)}\le\gamma_{univ}.
\]

Alors, pour chaque `\beta\in(0,S^*(M))`,

\[
u\in L^\infty(B_{1/3}\times(\beta,S^*(M))).
\]

La preuve construit une extension solénoïdale compacte de la donnée locale,
sa solution mild globale petite `a`, puis écrit `u=a+v`. La partie perturbée
`v` appartient à un espace parabolique de Hölder
`C^{0,\nu}_{par}(\overline{B}_{1/3}\times[0,S^*(M)])`, pour un
`\nu\in(0,1/2)`, avec trace initiale locale nulle.

Deux restrictions sont essentielles :

- la conclusion `L^\infty` est formulée avec `t\ge\beta>0`; elle n'affirme
  pas que la donnée initiale arbitrairement rugueuse devient uniformément
  bornée jusqu'à `t=0`;
- `S^*(M)` dépend du contrôle `L^2_{uloc}` global. Le théorème ne fournit pas
  un temps universel indépendant de la taille de la solution hors de la
  boule où la donnée est petite.

La pression est recalculée dans le cadre des solutions d'énergie locales et
la coupure solénoïdale; elle n'est pas traitée comme une variable locale
indépendante.

### 2.4 Hypothèse Type I du théorème 2

L'hypothèse notée (14) dans l'article est, pour un `r_0\in(0,\infty]`
fixé,

\[
\sup_{\bar x\in\mathbb R^3}
\sup_{0<r<r_0}
\sup_{T_*-r^2<t<T_*}
r^{-1/2}\left(\int_{B_r(\bar x)}|u(x,t)|^2\,dx\right)^{1/2}
\le M.
\tag{BP20-Type-I}
\]

C'est une borne locale uniforme de type Morrey-énergie. Elle est critique et
porte simultanément sur tous les centres, toutes les échelles sous `r_0` et
tous les temps de la fenêtre parabolique correspondante. Elle ne doit pas
être remplacée silencieusement par une borne ponctuelle `L^\infty_x`.

### 2.5 Théorème 2 : concentration à tous les temps tardifs

Soit `u` une solution de Leray–Hopf sur `\mathbb R^3\times(0,\infty)` qui
satisfait `(BP20-Type-I)`, dont le premier temps singulier est `T_*>0`, et
supposons que `(0,T_*)` est un point singulier. Alors il existe

\[
t_*=t_*(T_*,M,r_0)<T_*
\]

tel que, pour **tout** `t\in(t_*,T_*)`,

\[
\left\|u(t)\right\|_{L^3\!\left(
B_{2\sqrt{(T_*-t)/S^*(M)}}(0)
\right)}
>\gamma_{univ}.
\tag{BP20-concentration}
\]

Si `r_0=\infty`, on peut prendre `t_*=0`. Pour `r_0<\infty`, la preuve
choisit `t_*` afin que

\[
\lambda(t):=\sqrt{\frac{T_*-t}{S^*(M)}}\le r_0;
\]

la condition dimensionnellement exacte est donc
`T_*-t\le S^*(M)r_0^2`. L'affichage de l'équation (90) dans la version
primaire consultée écrit `T_*-S^*(M)r_0`, sans carré; cette formule est
dimensionnellement incohérente et ne suffit pas à l'étape `\lambda\le r_0`.
La preuve elle-même impose sans ambiguïté `r_0^2`. Le rapport traite donc
l'affichage (90) comme une coquille et conserve la condition effectivement
utilisée, sans attribuer aux auteurs une nouvelle estimation.

Le rayon est parabolique avec préfacteur

\[
C(M)=\frac{2}{\sqrt{S^*(M)}}.
\]

Le résultat vaut à chaque temps suffisamment proche de `T_*`, pas seulement
le long d'une sous-suite. Le centre singulier est toutefois une hypothèse :
le théorème ne découvre ni le temps ni la position d'une singularité.

L'implication logique de la preuve est la contraposée du lissage local : si,
à un temps tardif, la norme locale `L^3` sur la boule indiquée était au plus
`\gamma_{univ}`, la remise à l'échelle placerait la solution sous le seuil du
théorème 1 pendant un intervalle qui atteint le sommet; `(0,T_*)` serait
régulier.

## 3. Appendice B de Barker–Prange 2020 : endpoint faible-`L^3`

L'appendice B ne contient pas un nouveau théorème autonome avec une
numérotation complète et les mêmes symboles numériques. Il explique et
vérifie les substitutions nécessaires pour étendre les résultats au cadre
`L^{3,\infty}`. Il faut donc distinguer une extension prouvée par les auteurs
d'une identité non établie entre les constantes du cas fort et celles du cas
faible.

Les ingrédients explicites sont :

1. Pour une donnée globale petite dans `L^{3,\infty}_\sigma`, il existe une
   solution mild lisse `a`, faiblement-* continue au temps initial, et des
   constantes universelles `\widetilde\gamma,K'_0` telles que

   \[
   \sup_{t>0}\left(
   \|a(t)\|_{L^{3,\infty}}
   +t^{1/8}\|a(t)\|_{L^4}
   +t^{1/5}\|a(t)\|_{L^5}
   +t^{1/2}\|a(t)\|_{L^\infty}
   \right)
   \le K'_0\|a_0\|_{L^{3,\infty}}.
   \]

2. Les produits sont contrôlés par les inégalités de Lorentz d'O'Neil et de
   Hunt; la perturbation est petite dans une somme du type
   `L^\infty_tL^{3,\infty}_x+L^{5,\infty}_tL^5_x`.
3. L'extension solénoïdale de la donnée locale satisfait, sur la couronne de
   coupure, l'estimation critique affichée dans (115) :

   \[
   \|\widetilde u_{0,a}\|_{L^{3,\infty}}
   \le C\|\nabla\widetilde u\|_{L^2}
   \le C(\chi)\|u_0\|_{L^2(B_2)}
   \le C(\chi)\|u_0\|_{L^{3,\infty}(B_2)}.
   \]

La conclusion fidèle est : il existe un seuil universel faible-`L^3` et un
temps de lissage `S^*_{Lor}(M)>0` donnant les analogues des théorèmes 1 et 2,
avec la même structure parabolique et le quantificateur « pour tout temps
tardif ». Il n'est pas justifié d'identifier
`S^*_{Lor}=S^*` ou les deux seuils sans retracer toutes les constantes.
En notant distinctement ces constantes, l'analogue de concentration a la
forme

\[
\|u(t)\|_{L^{3,\infty}(B_{2\sqrt{(T_*-t)/S^*_{Lor}(M)}}(0))}
>\gamma_{Lor}
\]

pour tout temps suffisamment proche de `T_*`, sous la même borne de
Morrey-énergie et les mêmes hypothèses de premier temps et point singuliers.
Cette formule encode la structure prouvée par les substitutions de
l'appendice; les indices `Lor` sont ajoutés ici précisément pour ne pas
inventer une égalité numérique entre constantes.

Ce que l'appendice **ne** démontre pas :

- un lissage pour une donnée locale faible-`L^3` de taille arbitraire;
- une borne globale faible-`L^3` obtenue à partir de l'énergie;
- une compacité forte de l'espace non séparable `L^{3,\infty}`;
- un contrôle de `\omega` dans `L^{3/2,\infty}`;
- une préservation du signe, de la direction ou d'un rapport local entre
  vitesse et vorticité lors de la coupure solénoïdale.

La topologie faible-* et la classe de petite solution mild sont importantes :
l'unicité invoquée est celle de la classe critique petite considérée, et non
une unicité générale de toutes les solutions faibles.

## 4. Barker–Prange 2021 : concentration quantitative spatiale

### 4.1 Source et statut

- Tobias Barker et Christophe Prange, *Quantitative regularity for the
  Navier–Stokes equations via spatial concentration*,
  `arXiv:2003.06717v3`, version 3 du 25 mai 2020.
- Publication : *Communications in Mathematical Physics* **385** (2021),
  717–792, DOI
  [`10.1007/s00220-021-04122-x`](https://doi.org/10.1007/s00220-021-04122-x).
- Texte primaire audité :
  [`arXiv:2003.06717v3`](https://arxiv.org/abs/2003.06717v3), théorèmes 1–3,
  proposition 2, propositions 7–8 et corollaires associés.

Statut : **preuve analytique publiée**, sans calcul certifié ni preuve
assistée par ordinateur.

### 4.2 Classes de solutions

L'article travaille avec des solutions mild lisses avant le temps final,
ayant une décroissance spatiale suffisante pour les manipulations globales,
et avec des solutions faibles adaptées d'énergie finie pour certaines
applications. Une solution faible adaptée d'énergie finie appartient à

\[
C_w(I;L^2_\sigma(\mathbb R^3))
\cap L^2(I;\dot H^1(\mathbb R^3)),
\]

satisfait l'équation au sens des distributions, l'inégalité d'énergie
globale et l'inégalité d'énergie locale dans chaque boule.

Pour les données de Schwartz du problème Clay, la solution forte maximale
est dans la classe mild/lisse considérée avant son temps maximal. Mais la
borne Type I supplémentaire n'est pas une conséquence connue de ces données.

### 4.3 Définition Type I dans cet article

L'hypothèse centrale est

\[
\|u\|_{L^\infty(0,T_*;L^{3,\infty}(\mathbb R^3))}\le M.
\tag{BP21-Type-I}
\]

C'est cette borne globale critique que les auteurs appellent Type I. Elle est
plus structurée que l'énergie Leray–Hopf et distincte de la seule borne
ponctuelle classique. Elle fournit uniformément la borne locale de Morrey de
2020, mais elle permet encore des concentrations fortes `L^3` logarithmiques.

### 4.4 Théorème 1 : énoncé et quantificateurs

Il existe une constante universelle `M_0\ge1`. Soient `M\ge M_0` et
`\delta\in(0,1)`. Soit `u` une solution mild sur
`\mathbb R^3\times[0,T_*)`, localement bornée en `L^\infty` avant `T_*`,
avec la régularité et la décroissance précisées dans l'article. Supposons
`(BP21-Type-I)` et que `(0,T_*)` soit singulier. Alors il existe
`c=c(\delta,M,T_*)>0` tel que, pour tout

\[
t\in\left(\max\{T_*/2,T_*-c\},T_*\right),
\]

on ait

\[
\int_{B_{R_\delta(t)}(0)}|u(x,t)|^3\,dx
\ge
\frac{\log\!\left((T_*-t)^{-\delta/2}\right)}
{\exp(\exp(M^{1025}))},
\tag{BP21-main}
\]

avec

\[
R_\delta(t)=T_*^{1/2}(T_*-t)^{(1-\delta)/2}.
\]

La preuve affiche même, à une étape, un dénominateur plus précis de la forme

\[
4M^{1023}\exp(\exp(M^{1024})),
\]

mais le théorème publié retient la constante simplifiée ci-dessus.

Points de lecture décisifs :

- le rayon décroît comme `(T_*-t)^{1/2-\delta/2}`; il est donc plus grand que
  l'échelle parabolique quand `t\uparrow T_*`;
- la minoration vaut à **chaque** temps assez tardif;
- le centre `0` est un point singulier supposé, non une localisation produite
  par le théorème;
- le membre de gauche est `\int|u|^3=\|u\|_{L^3}^3`. La minoration de la
  norme elle-même n'est donc que de l'ordre
  `C(M)^{1/3}\log^{1/3}((T_*-t)^{-1})`.

L'abstract emploie une formulation abrégée susceptible d'être lue comme une
croissance logarithmique de la norme `L^3`. L'énoncé numéroté fait foi :
c'est l'intégrale cubique qui possède l'exposant logarithmique `1`.

### 4.5 Mécanisme de preuve et constantes

Le point de départ est la concentration parabolique de Barker–Prange 2020.
La propagation quantitative en arrière, des arguments d'unique continuation
de type Carleman, la production d'époques et de couronnes « bonnes », puis
l'addition sur des couronnes disjointes transforment une masse critique
constante en croissance logarithmique sur la boule élargie.

Les constantes sont effectives au sens analytique de l'article mais très
dégradées. Un paramètre de courte durée satisfait

\[
S^\sharp(M)=O(M^{-100}),
\]

et les estimations finales sont doublement ou triplement exponentielles en de
grandes puissances de `M`. Elles ne sont pas uniformes lorsque `M\to\infty`.
L'article ne prétend pas optimiser les exposants `100`, `1023`, `1024` ou
`1025`.

La pression et la non-localité sont incluses dans la localisation, les
estimations de vorticité et les arguments d'unique continuation; elles ne
fournissent cependant pas un critère séparé de pression accessible depuis la
seule énergie.

### 4.6 Proposition 2 : concentration d'enstrophie et échelle

La proposition quantitative centrale considère une solution lisse à
décroissance suffisante sur `[t_0-T,t_0]`, sous la borne
`L^\infty_tL^{3,\infty}_x\le M`. À une époque `t'_0<t_0`, elle suppose une
concentration de vorticité du type

\[
\int_{B_{4(S^\sharp)^{-1/2}(t_0-t'_0)^{1/2}}(0)}
|\omega(x,t'_0)|^2\,dx
>
M^2(t_0-t'_0)^{-1/2}\sqrt{S^\sharp},
\]

avec

\[
\frac{t_0-t'_0}{T}<C^\sharp M^{-548}.
\]

La combinaison
`\sqrt{t_0-t'_0}\int|\omega|^2` est bien sans dimension. Sous ces
hypothèses, la proposition borne quantitativement l'écart temporel en
fonction d'une intégrale locale terminale de `|u|^3`. Cette proposition est
un mécanisme conditionnel; elle ne prouve pas que l'enstrophie requise se
concentre pour toute solution Clay.

### 4.7 Théorème 2 : tranches temporelles critiques, sans hypothèse Type I

Un second résultat quantifie le critère de Seregin. Pour une solution lisse
d'énergie finie sur `\mathbb R^3\times(-1,0)`, supposons qu'il existe une
suite `t_k\uparrow0` telle que

\[
\|u(t_k)\|_{L^3(\mathbb R^3)}\le M.
\]

Après sélection d'une suite suffisamment séparée, avec

\[
\sup_k\frac{-t_{k+1}}{-t_k}
<\exp\!\left(-2(M^\flat)^{1223}\right),
\qquad
M^\flat=\exp(L_*M^5/2),
\]

et

\[
j=\left\lceil\exp\!\left(\exp((M^\flat)^{1224})\right)\right\rceil+1,
\]

les auteurs obtiennent

\[
\|u\|_{L^\infty(\mathbb R^3\times(t_{j+1}/4,0))}
\le \frac{C_1M^{-23}}{\sqrt{-t_{j+1}}}.
\]

Ce résultat n'assume pas `(BP21-Type-I)`, mais suppose une borne globale
forte `L^3` le long d'une suite. Il ne convertit pas une borne d'énergie en
cette hypothèse et ne sélectionne pas un centre ou rayon Type II.

### 4.8 Autres conséquences auditées

- Sous `(BP21-Type-I)`, une petite norme terminale locale
  `L^{3,\infty}` au point considéré, au seuil doublement exponentiel en `M`,
  implique la régularité locale (proposition 7).
- Un critère quantitatif de mesure/sparsité est donné avec un seuil du type
  `\exp(-4\exp(M^{1023}))` (proposition 8).
- Le nombre de points singuliers au temps terminal est borné par une quantité
  de l'ordre `\exp(\exp(M^{1024}))` (corollaire 9).
- Le théorème 3 est un lissage local sous-critique à partir d'une donnée
  locale `L^6`, avec un temps annoncé de l'ordre
  `M^{-30}N^{-70}`; le corollaire Type I associé emploie un temps de l'ordre
  `M^{-100}`. Ce sont des outils quantitatifs, pas une suppression de
  l'hypothèse critique.

## 5. Comparaison des deux résultats

| Élément | Barker–Prange 2020 | Barker–Prange 2021 |
|---|---|---|
| Source catalogue | `NS-SRC-0146` | `NS-SRC-0147` |
| Équation | NS 3D, `R^3`, `\nu=1`, sans force | identique |
| Classe principale | énergie locale; Leray–Hopf pour la concentration | mild/lisse; adaptée d'énergie finie pour applications |
| Hypothèse dite Type I | Morrey-énergie locale uniforme `(BP20-Type-I)` | `L^\infty_tL^{3,\infty}_x\le M` global |
| Point singulier | supposé, premier temps singulier | supposé, premier temps singulier |
| Rayon | `2\sqrt{(T_*-t)/S^*(M)}` | `T_*^{1/2}(T_*-t)^{(1-\delta)/2}` |
| Quantité concentrée | norme locale `L^3>\gamma` | `\int|u|^3\gtrsim_M\log((T_*-t)^{-1})` |
| Temps | tout temps suffisamment tardif | tout temps suffisamment tardif |
| Force du résultat | masse critique constante, échelle parabolique | accumulation logarithmique, boule élargie |
| Endpoint faible-`L^3` | petite donnée locale via appendice B | hypothèse globale de taille finie |
| Exclut un blow-up Type I ? | non | non |
| Traite Type II ? | non | non |

## 6. Passe adverse : pourquoi la conclusion 2021 ne contredit pas son hypothèse

Considérons uniquement comme contre-profil fonctionnel scalaire

\[
f_\varepsilon(x)=\frac{a}{|x|}
\mathbf 1_{\{\varepsilon<|x|<1\}}.
\]

Sa fonction de distribution montre que

\[
\sup_{0<\varepsilon<1}
\|f_\varepsilon\|_{L^{3,\infty}(\mathbb R^3)}
\le C|a|,
\]

tandis que, pour `\varepsilon<R<1`,

\[
\int_{B_R}|f_\varepsilon|^3\,dx
=4\pi|a|^3\log\frac{R}{\varepsilon}.
\]

Ainsi une famille peut garder une borne critique faible-`L^3` uniforme tout
en accumulant une masse forte `L^3` logarithmique sur plusieurs échelles. Ce
calcul réfute l'implication fonctionnelle

\[
\|u\|_{L^{3,\infty}}\le M
\quad\Longrightarrow\quad
\sup_{R}\int_{B_R}|u|^3<C(M).
\]

Il explique exactement pourquoi `(BP21-main)` ne ferme pas l'argument de
régularité.

**Limite du test :** `f_\varepsilon` n'est ni un champ divergence-free ni une
solution Navier–Stokes. Il ne réfute aucun théorème dynamique; il réfute
seulement le raccord fonctionnel qui transformerait automatiquement la
concentration logarithmique en contradiction avec la borne faible-`L^3`.
Statut : `AI_INTERNAL_COUNTERPROFILE`, calcul élémentaire reproductible.

Autres attaques effectuées :

1. **Quantificateur inversé.** Les deux théorèmes donnent « pour tout temps
   tardif », mais seulement après avoir supposé un point singulier et une
   borne Type I uniforme. Ils ne donnent pas « pour toute solution ».
2. **Norme contre intégrale.** Remplacer `\int|u|^3\gtrsim\log` par
   `\|u\|_3\gtrsim\log` fait perdre une racine cubique et est faux comme
   transcription du théorème 2021.
3. **Constante cachée.** `S^*(M)`, `S^\sharp(M)`, les époques bonnes et les
   constantes de Carleman dépendent de `M`; aucune uniformité en
   `M\to\infty` n'est revendiquée.
4. **Notion de solution.** La construction de solutions faibles non uniques
   hors Leray–Hopf ne réfute pas ces résultats sur solutions mild,
   Leray–Hopf ou faibles adaptées.
5. **Pression.** La pression est non locale et contrôlée dans les preuves;
   aucune estimation locale de vitesse seule ne peut être isolée sans la
   décomposition de pression correspondante.
6. **Domaine.** Aucun transfert au tore ou à un domaine borné n'est contenu
   dans les énoncés. Un tel transfert requiert son propre lemme pour le noyau
   de pression, les images périodiques ou la frontière.

## 7. Point exact de non-transfert au Type II

Prenons une suite de zooms autour de `(x_j,t_j)\to(x_*,T_*)`, d'échelle
`\lambda_j\downarrow0`. Dans le régime Type I des articles, la quantité
critique qui contrôle chaque zoom reste bornée par un même `M`. On obtient
alors :

- un contrôle `L^2_{uloc}` uniforme de la donnée remise à l'échelle;
- un temps de lissage `S^*(M)>0` indépendant de `j`;
- des rayons et fenêtres temporelles compatibles avec le sommet singulier;
- des constantes uniformes dans les étapes de Carleman et d'empilement des
  couronnes.

Dans un scénario Type II, le meilleur contrôle disponible peut être
`M_j\to\infty`. Les conclusions deviennent alors

\[
S^*(M_j)\downarrow0,
\qquad
S^\sharp(M_j)=O(M_j^{-100})\downarrow0,
\]

et les constantes exponentielles se dégradent. Le rayon
`2\sqrt{(T_*-t)/S^*(M_j)}` s'élargit en unités physiques tandis que la fenêtre
de lissage en temps renormalisé se rétracte; rien ne garantit simultanément
la localisation, la petite donnée et l'atteinte du sommet. C'est le premier
coefficient non uniforme qui casse la contraposée.

Pour certaines remises à l'échelle Type II, la limite candidate est une
solution ancienne d'Euler : le terme visqueux tend vers zéro. Les outils de
lissage parabolique et de Carleman visqueux des deux articles ne passent pas
directement à cette limite. Il faut alors un théorème de rigidité eulérien et
une compacité assez forte pour conserver les hypothèses; ces deux maillons ne
sont pas fournis.

## 8. Écart logique avec le problème Clay

Pour une donnée de Schwartz divergence-free sur `\mathbb R^3`, supposons que
la solution forte maximale ait un premier temps fini `T_*`. Les résultats
audités s'appliqueraient **si**, en plus, on démontrait soit
`(BP20-Type-I)`, soit `(BP21-Type-I)` selon le théorème utilisé. Or l'identité
d'énergie ne contrôle que

\[
u\in L^\infty_tL^2_x\cap L^2_t\dot H^1_x,
\]

cadre supercritique par rapport à la concentration. Elle ne fournit aucune
des deux bornes Type I uniformes.

Même sous `(BP21-Type-I)`, la conclusion ne dit pas que la solution est
régulière. Elle impose une concentration forte compatible avec la norme
faible-`L^3`. L'implication disponible est donc

\[
\text{blow-up Clay}+
\text{borne Type I globale}
\Longrightarrow
\text{concentration logarithmique locale nécessaire},
\]

et non

\[
\text{donnée Clay}
\Longrightarrow
\text{borne Type I}
\Longrightarrow
\text{régularité}.
\]

Le résultat ne construit pas non plus un blow-up admissible : le temps et le
point singuliers sont supposés, et aucune limite singulière n'est produite.

## 9. Veille différentielle primaire 2025–2026

| ID existant | Source primaire et statut au 2026-08-15 | Apport pertinent | Pourquoi le verrou reste ouvert |
|---|---|---|---|
| `NS-SRC-0035` | Feng–He–Wang, [`arXiv:2201.04656`](https://arxiv.org/abs/2201.04656), publié en ligne dans *DCDS-B* 37 (2026), DOI [`10.3934/dcdsb.2026048`](https://doi.org/10.3934/dcdsb.2026048) | Régularité quantitative dans les Lorentz critiques `L^{3,q}`, `3\le q<\infty`, avec constantes très grandes et taux de blow-up | Le endpoint `q=\infty` est explicitement absent; résultat global, pas une résolution de la concentration locale Type II |
| `NS-SRC-0048` | Seregin, [`arXiv:2507.08733v2`](https://arxiv.org/abs/2507.08733v2), prépublication révisée le 3 janvier 2026 | Scénarios Type II pour solutions faibles adaptées, fonctionnelles supplémentaires et réductions de type Liouville | Hypothèses conditionnelles; pas d'exclusion générale ni borne Type I issue de l'énergie |
| `NS-SRC-0034` | Seregin, [`arXiv:2606.29468v1`](https://arxiv.org/abs/2606.29468v1), prépublication | Analyse locale Type II et mise à l'échelle vers Euler | La limite eulérienne exige compacité et rigidité additionnelles; le lissage visqueux Barker–Prange ne se transfère pas |
| `NS-SRC-0045` | Seregin, [`arXiv:2402.13229v3`](https://arxiv.org/abs/2402.13229v3), révisé le 8 août 2026 | Type II axisymétrique sous contrôles supercritiques supplémentaires; solution ancienne eulérienne limite | Axisymétrie et hypothèses additionnelles; pas de théorème pour le cas général Clay |
| `NS-SRC-0051` | Pineau–Vicol, [`arXiv:2607.09619v2`](https://arxiv.org/abs/2607.09619v2), révisé le 6 août 2026 | Exclusion de profils backward auto-similaires tournés/discrets dans des régimes de rotation ou de facteur d'échelle spécifiques; critère local d'auto-similarité approximative à une tranche | Profils très structurés; exclure cette classe ne couvre ni Type I arbitraire ni Type II |
| `NS-SRC-0059` | Grujić, [`arXiv:2607.08866v2`](https://arxiv.org/abs/2607.08866v2), prépublication | Critères géométriques/logarithmiques sur concentration critique de vorticité et direction | Les hypothèses `L^{3/2,\infty}` et BMO pondéré de direction ne découlent pas de Barker–Prange ni de l'énergie Clay |
| `NS-SRC-0032` | Cheskidov–Dai–Palasek, [`arXiv:2511.09556v2`](https://arxiv.org/abs/2511.09556v2), prépublication | Branches faibles périodiques à comportement Type I instantané et non-unicité depuis des données lisses | Les branches pertinentes sortent du régime Leray–Hopf/énergie locale autour de l'événement; aucune contradiction avec la continuation classique Clay |

Cette veille n'a révélé aucun article primaire 2025–2026 établissant l'une
des implications manquantes suivantes :

\[
\text{énergie Clay}\Rightarrow L^\infty_tL^{3,\infty}_x,
\qquad
\text{concentration BP21}\Rightarrow\text{contradiction},
\qquad
\text{Type II général}\Rightarrow\text{rigidité}.
\]

## 10. Recommandations au catalogue

### Aucun nouvel identifiant après `NS-SRC-0179`

Toutes les sources primaires utiles à ce cycle sont déjà cataloguées. Créer
des doublons masquerait la veille différentielle. Il faut plutôt enrichir les
deux notices existantes.

### Corrections recommandées pour `NS-SRC-0146`

- enregistrer l'hypothèse Type I exacte `(BP20-Type-I)` avec ses trois
  supremums, `r_0` et la fenêtre `T_*-r^2<t<T_*`;
- enregistrer le rayon exact
  `2\sqrt{(T_*-t)/S^*(M)}` et le quantificateur « tout temps tardif »;
- distinguer le lissage `L^3` principal de l'extension faible-`L^3` de
  l'appendice B;
- ne pas identifier les constantes fortes et faibles sans reconstruction;
- noter que le point singulier et le premier temps de blow-up sont supposés.

### Corrections recommandées pour `NS-SRC-0147`

- inscrire l'hypothèse exacte
  `\|u\|_{L^\infty_tL^{3,\infty}_x}\le M` et la définition Type I propre à
  l'article;
- enregistrer `R_\delta(t)=T_*^{1/2}(T_*-t)^{(1-\delta)/2}`;
- écrire la conclusion comme minoration de `\int|u|^3`, avec racine cubique
  si elle est convertie en norme `L^3`;
- suivre la dépendance doublement exponentielle en `M` et
  `S^\sharp(M)=O(M^{-100})`;
- distinguer le théorème principal du théorème de tranches `L^3` globales;
- ajouter explicitement `NO_TYPE_II_TRANSFER` et `NO_CLAY_RESOLUTION`.

Statut de preuve recommandé pour les deux notices : `PAPER_PROOF`. Le
contre-profil de la section 6 doit conserver le statut
`AI_INTERNAL_COUNTERPROFILE`; il ne doit jamais recevoir `PAPER_PROOF`.

## 11. Lemme unique transférable et prochaine expérience décisive

Le lemme minimal réellement utile à conserver dans le graphe est :

> **Persistance critique conditionnelle.** Pour une solution NS 3D sur
> `R^3`, un premier point singulier et une borne Type I critique uniforme
> impliquent une masse forte `L^3` non nulle à chaque temps tardif sur
> l'échelle parabolique; sous la borne globale `L^{3,\infty}`, cette masse
> s'accumule au moins logarithmiquement sur une boule légèrement
> super-parabolique.

Les dépendances sont

\[
\text{borne critique uniforme}
\to\text{contrôle local après zoom}
\to\text{lissage petite donnée}
\to\text{concentration par contraposée}
\to\text{propagation/Carleman}
\to\text{accumulation logarithmique}.
\]

La prochaine expérience décisive doit être analytique et reproductible :

1. extraire des preuves les dépendances monotones utilisables de
   `S^*(M)`, `S^\sharp(M)` et des seuils de Carleman;
2. injecter une famille Type II abstraite `M_j\uparrow\infty`;
3. calculer la fenêtre physique, le nombre de couronnes disjointes et la
   minoration finale effectivement survivante;
4. falsifier l'existence d'un régime de croissance non trivial de `M_j` pour
   lequel toutes les constantes resteraient compatibles.

Le résultat négatif attendu — disparition de la fenêtre ou de la minoration
avant l'échelle terminale — localiserait quantitativement le premier
coefficient à remplacer. Un résultat positif ne résoudrait pas Clay, mais
isolerait une classe « faiblement Type II » où le mécanisme Barker–Prange
pourrait encore fonctionner.

## Sources primaires

1. Barker, T.; Prange, C., *Localized smoothing for the Navier–Stokes
   equations and concentration of critical norms near singularities*,
   [`arXiv:1812.09115v2`](https://arxiv.org/abs/1812.09115v2),
   [`ARMA 236 (2020)`](https://doi.org/10.1007/s00205-020-01495-6).
2. Barker, T.; Prange, C., *Quantitative regularity for the Navier–Stokes
   equations via spatial concentration*,
   [`arXiv:2003.06717v3`](https://arxiv.org/abs/2003.06717v3),
   [`CMP 385 (2021)`](https://doi.org/10.1007/s00220-021-04122-x).
3. Feng, Y.; He, C.; Wang, B.,
   [`arXiv:2201.04656`](https://arxiv.org/abs/2201.04656),
   [`DCDS-B 37 (2026)`](https://doi.org/10.3934/dcdsb.2026048).
4. Seregin, G., [`arXiv:2507.08733v2`](https://arxiv.org/abs/2507.08733v2).
5. Seregin, G., [`arXiv:2606.29468v1`](https://arxiv.org/abs/2606.29468v1).
6. Seregin, G., [`arXiv:2402.13229v3`](https://arxiv.org/abs/2402.13229v3).
7. Pineau, R.; Vicol, V.,
   [`arXiv:2607.09619v2`](https://arxiv.org/abs/2607.09619v2).
8. Grujić, Z., [`arXiv:2607.08866v2`](https://arxiv.org/abs/2607.08866v2).
9. Cheskidov, A.; Dai, M.; Palasek, S.,
   [`arXiv:2511.09556v2`](https://arxiv.org/abs/2511.09556v2).
