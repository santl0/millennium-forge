# Cycle 0036 — revue primaire : sélection de boule, fragmentation BV et centres multiples Navier–Stokes

Date de coupure : **2026-08-14**
Objet : décomposition isopérimétrique en composantes, fonctions de
concentration, recouvrements de Besicovitch/Vitali, isopérimétrie
quantitative, concentration locale BV et localisation de plusieurs centres
singuliers Navier–Stokes.
Statut : revue indépendante; aucun catalogue ni claim JSON n'est modifié.

## Verdict falsifiable

Il faut distinguer trois énoncés.

1. **Sélection locale vraie.** Si \(E\subset\mathbb R^3\) a volume
   \(V=|E|>0\) et périmètre \(P=P(E)<\infty\), une source publiée implique
   l'existence d'une boule à l'échelle naturelle \(r=V/P\) telle que

   \[
   |E\cap B_r(x)|\ge c\left(\frac VP\right)^3.
   \]

   C'est une conséquence directe de l'inégalité locale BV de Frank–Lieb.
   Le diamètre de la boule est donc contrôlé par \(2V/P\), mais la masse
   capturée n'est en général qu'une fraction
   \(cV^2/P^3\) du volume total.

2. **Sélection d'une fraction universelle fausse sans hypothèse
   supplémentaire.** Une union de \(N\) boules égales arbitrairement
   éloignées montre qu'aucune boule de rayon \(C V/P\) ne peut capter une
   fraction de \(V\) indépendante du rapport isopérimétrique. La dépendance
   \(V^2/P^3\) a la bonne taille sur cet exemple.

3. **Confinement global faux.** Le volume et le périmètre ne bornent ni le
   diamètre de \(E\), ni celui d'une composante indécomposable. Des gouttes
   séparées donnent la dichotomie par translation; une goutte reliée à un
   satellite lointain par un tube très mince conserve volume et périmètre
   uniformément bornés tout en ayant un diamètre arbitrairement grand.

L'isopérimétrie quantitative change la conclusion seulement sous petite
déficience isopérimétrique : elle fournit alors une boule de même volume qui
capte presque tout \(E\). Les résultats Navier–Stokes à centres multiples
font intervenir une solution, l'epsilon-régularité, une borne critique et un
budget espace-temps; ils ne suivent pas du seul couple volume+périmètre.

## 1. Échelle et quantité exacte à sélectionner

Pour \(E\subset\mathbb R^d\), on pose

\[
Q_E(r)=\sup_{x\in\mathbb R^d}|E\cap B_r(x)|.
\]

Sous la dilatation \(E_\rho=\rho E\),

\[
|E_\rho|=\rho^d|E|,\qquad
P(E_\rho)=\rho^{d-1}P(E),\qquad
Q_{E_\rho}(\rho r)=\rho^dQ_E(r).
\]

Ainsi \(V/P\) est une longueur, \((V/P)^d\) est un volume, et

\[
\frac{(V/P)^d}{V}=\frac{V^{d-1}}{P^d}
\]

est une fraction sans dimension. En dimension trois, toute conclusion
uniforme fondée sur le seul couple \((V,P)\) doit donc naturellement faire
apparaître \(V^2/P^3\), sauf information géométrique additionnelle.

## 2. Le théorème publié qui donne une boule

Rupert L. Frank et Elliott H. Lieb, *A Compactness Lemma and Its Application
to the Existence of Minimizers for the Liquid Drop Model*, *SIAM J. Math.
Anal.* 47 (2015), 4436–4450, DOI
[10.1137/15M1010658](https://doi.org/10.1137/15M1010658), arXiv
[1503.00192](https://arxiv.org/abs/1503.00192), publié en ligne le
2015-11-19, proposé **NS-SRC-0159**.

### 2.1 Inégalité locale BV

L'équation (2.2) du papier, étendue de \(W^{1,1}\) à \(BV\), implique pour
un ensemble de périmètre fini dans \(\mathbb R^d\), tout \(r>0\),

\[
P(E)+C_dr^{-1}|E|
\ge c_d Q_E(r)^{-1/d}|E|.
\]

Donc

\[
\boxed{
Q_E(r)\ge
\left(\frac{c_d|E|}{P(E)+C_dr^{-1}|E|}\right)^d.}
\]

Les constantes du papier dépendent seulement de la dimension et du
mollificateur fixé. En choisissant \(r=V/P\),

\[
\boxed{
Q_E(V/P)\ge c'_d(V/P)^d.}
\]

En dimension trois, il existe donc \(x_E\) tel que

\[
|E\cap B_{V/P}(x_E)|\ge c'_3(V/P)^3,
\qquad
\frac{|E\cap B_{V/P}(x_E)|}{|E|}
\ge c'_3\frac{V^2}{P^3}.
\]

Ce résultat répond positivement à la version **locale** de la question. Il
ne dit pas que la boule contient une composante entière, qu'elle est unique,
ou qu'elle contient une fraction universelle de \(V\).

### 2.2 Exclusion de l'évanescence BV

La proposition 2.1 de Frank–Lieb affirme que pour une suite \(E_n\) dont le
périmètre est uniformément borné, soit \(|E_n|\to0\), soit, après extraction
et translations, \(E_n-a_n\) converge localement vers un ensemble de mesure
strictement positive.

Ainsi, si

\[
\inf_n|E_n|>0,
\qquad
\sup_nP(E_n)<\infty,
\]

l'évanescence au sens
\(\sup_x|E_n\cap B_1(x)|\to0\) est impossible. Cela affine le diagnostic de
Lions : pour des indicatrices BV, le coût de périmètre interdit une
fragmentation en gouttes toutes infinitésimales lorsque la masse totale reste
positive.

La dichotomie demeure possible. Le lemme 2.2 de Frank–Lieb sépare précisément
une partie principale convergente et une partie manquante qui s'échappe de
tout compact, avec additivité asymptotique du périmètre.

## 3. Décomposition en composantes et ce qu'elle sélectionne

Luigi Ambrosio, Vicent Caselles, Simon Masnou et Jean-Michel Morel,
*Connected components of sets of finite perimeter and applications to image
processing*, *J. Eur. Math. Soc.* 3 (2001), 39–92, DOI
[10.1007/PL00011302](https://doi.org/10.1007/PL00011302),
[texte primaire EMS](https://ems.press/journals/jems/articles/120), publié le
2001-03-31, proposé **NS-SRC-0156**.

Le théorème de décomposition donne, à ensembles négligeables près, une
famille finie ou dénombrable de composantes M-indécomposables \(E_i\),
deux à deux disjointes, telle que

\[
E=\bigcup_iE_i,qquad
P(E)=\sum_iP(E_i).
\]

Avec l'isopérimétrie euclidienne de Federer–Fleming, proposée au cycle
précédent sous **NS-SRC-0148**,

\[
c_{\rm iso}|E_i|^{2/3}\le P(E_i),
\qquad c_{\rm iso}=(36\pi)^{1/3},
\]

on déduit

\[
\sum_i|E_i|^{2/3}\le P/c_{\rm iso}.
\]

Comme

\[
V=\sum_i |E_i|
\le \left(\sup_i|E_i|^{1/3}\right)
\sum_i|E_i|^{2/3},
\]

il existe une composante vérifiant

\[
\boxed{
|E_i|\ge\left(\frac{c_{\rm iso}V}{P}\right)^3.}
\]

Cette dernière constante suivie est une **AI_DERIVATION** à partir de deux
théorèmes publiés, pas un énoncé attribué textuellement à Ambrosio et al.

### Non-transfert au diamètre

L'indécomposabilité est une notion de connexité mesurée par le périmètre;
elle n'implique ni bornitude, ni convexité, ni rayon intérieur uniforme. Un
ensemble peut comporter une masse principale, un tube de rayon très petit et
un satellite très éloigné. Par exemple, un tube lisse de longueur \(L\) et
de rayon \(L^{-2}\) coûte

\[
O(L^{-1})\quad\text{en surface},
\qquad O(L^{-3})\quad\text{en volume},
\]

tout en portant le diamètre à \(L\). Raccordé à une boule fixe, il donne des
ensembles connexes lisses de volumes et périmètres uniformément contrôlés,
mais de diamètres divergents.

La décomposition sélectionne donc une composante de **volume** contrôlé, pas
une composante de diamètre contrôlé. La boule de Frank–Lieb est une
conclusion différente : elle capture une partie locale, sans prétendre
contenir la composante.

## 4. Fragmentation et translation : contre-profils exacts

### 4.1 Translation pure

Soit

\[
E_L=B_1(0)\cup B_1(Le_1),\qquad L>3.
\]

Le volume et le périmètre sont indépendants de \(L\), tandis que
\(\operatorname{diam}E_L\to\infty\). Après translation vers la première
goutte, la seconde disparaît localement : c'est une dichotomie, non une
évanescence.

Cet exemple réfute toute boule de diamètre contrôlé par \(V,P\) qui devrait
contenir **tout** \(E\), mais il ne réfute pas la sélection locale de
Frank–Lieb.

### 4.2 Fragmentation en \(N\) gouttes égales

Soit

\[
E_N=\bigcup_{k=1}^NB_a(x_k),
\]

avec centres séparés de beaucoup plus que \(a\). En notant
\(\omega_3=4\pi/3\),

\[
V=N\omega_3a^3,
\qquad
P=3N\omega_3a^2,
\qquad
\frac VP=\frac a3.
\]

Pour tout \(C\) fixé, on peut séparer les centres assez fortement pour
qu'une boule de rayon \(CV/P=Ca/3\) ne rencontre qu'une goutte. Elle capte
alors au plus \(V/N\). Or

\[
\frac1N=27\omega_3\frac{V^2}{P^3}.
\]

La fraction \(V^2/P^3\) fournie par Frank–Lieb est donc correcte à constante
dimensionnelle près. Il est impossible de la remplacer par une constante
universelle indépendante de l'indice isopérimétrique.

Lorsque \(V\) est fixé, le périmètre de cet exemple croît comme \(N^{1/3}\).
Il ne contredit donc pas l'exclusion de l'évanescence sous borne uniforme de
périmètre; il explique exactement le prix de la fragmentation.

## 5. Concentration-compacité et recouvrements

### 5.1 Lions : compacité, évanescence, dichotomie

P.-L. Lions, *The concentration-compactness principle in the Calculus of
Variations. The locally compact case, part 1*, *Ann. IHP ANL* 1 (1984),
109–145, DOI
[10.1016/S0294-1449(16)30428-0](https://doi.org/10.1016/S0294-1449(16)30428-0),
déjà **NS-SRC-0140**.

La fonction de concentration d'une mesure \(\mu_n\),

\[
Q_n(r)=\sup_x\mu_n(B_r(x)),
\]

organise l'alternative compacité/évanescence/dichotomie. Sans structure
variationnelle ou stricte sous-additivité, la dichotomie n'est pas une
contradiction. Les ensembles \(E_L\) ci-dessus la réalisent exactement.

Frank–Lieb ajoutent l'information spécifique BV : volume inférieur positif
et périmètre supérieur fini excluent l'évanescence, mais pas la dichotomie ni
la perte de masse à l'infini.

### 5.2 Besicovitch et Vitali

A. S. Besicovitch, *A general form of the covering principle and relative
differentiation of additive functions*, *Proc. Cambridge Philos. Soc.* 41
(1945), 103–110, DOI
[10.1017/S0305004100022453](https://doi.org/10.1017/S0305004100022453),
proposé **NS-SRC-0157**, publié. La partie II, *ibid.* 42 (1946), 1–10, DOI
[10.1017/S0305004100022660](https://doi.org/10.1017/S0305004100022660),
étend le principe à des suites régulières d'ensembles de recouvrement.

Un recouvrement de Besicovitch permet d'extraire des boules avec multiplicité
bornée par une constante dimensionnelle. Combiné à l'isopérimétrie relative
de Korte–Lahti, proposée **NS-SRC-0149**, il permet de sommer des contrôles
locaux de volume par le périmètre.

Mais le théorème de recouvrement seul :

- ne fournit aucune minoration de masse dans une boule;
- ne contrôle pas le diamètre de l'union;
- ne choisit pas une composante;
- ne supprime pas la dichotomie par translation.

Pour le besoin présent, l'inégalité de Frank–Lieb est plus directe et évite
de cacher la constante de multiplicité dans une chaîne de recouvrements.

## 6. Isopérimétrie quantitative : l'hypothèse qui donne presque une boule

Nicola Fusco, Francesco Maggi et Aldo Pratelli, *The sharp quantitative
isoperimetric inequality*, *Ann. Math.* 168 (2008), 941–980, DOI
[10.4007/annals.2008.168.941](https://doi.org/10.4007/annals.2008.168.941),
[texte primaire](https://annals.math.princeton.edu/2008/168-3/p06), proposé
**NS-SRC-0158**, publié.

Pour un ensemble \(E\) et une boule \(B_E\) de même volume, définissons, à
normalisation dimensionnelle près,

\[
\delta(E)=\frac{P(E)}{P(B_E)}-1,
\qquad
\alpha(E)=\inf_x\frac{|E\triangle(x+B_E)|}{|E|}.
\]

Le théorème quantitatif sharp donne

\[
\alpha(E)^2\le C_d\delta(E).
\]

Il existe donc une boule de diamètre
\(2(V/\omega_3)^{1/3}\) telle que

\[
|E\cap(x+B_E)|
\ge \left(1-\frac{C_3}{2}\sqrt{\delta(E)}\right)V.
\]

Cette conclusion est nettement plus forte que Frank–Lieb lorsque
\(\delta(E)\ll1\), mais sa petite déficience est une hypothèse additionnelle
substantielle. Une borne arbitraire sur \(P\) ne rend pas \(E\) presque
sphérique.

## 7. Plusieurs centres ou gouttes critiques en Navier–Stokes

### 7.1 Seregin 2001 : nombre de points singuliers à temps fixé

Gregory A. Seregin, *On the number of singular points of weak solutions to
the Navier-Stokes equations*, *Comm. Pure Appl. Math.* 54 (2001), 1019–1028,
DOI [10.1002/cpa.3002](https://doi.org/10.1002/cpa.3002), proposé
**NS-SRC-0160**, publié le 2001-04-03.

Cadre : solution faible adaptée des équations de Navier–Stokes
incompressibles tridimensionnelles dans un cylindre
\(\Omega\times(0,T)\), avec pression et inégalité d'énergie locale. Le papier
borne le nombre de points singuliers de la tranche temporelle dans un
sous-domaine intérieur.

Ce résultat traite réellement plusieurs centres, mais son budget est celui
de l'epsilon-régularité locale d'une solution adaptée. Il n'est pas une
décomposition de superniveau par volume et périmètre.

### 7.2 Seregin 2020/2021 : contrôle local faible-\(L^3\)

Gregory Seregin, *A note on weak solutions to the Navier–Stokes equations
that are locally in \(L_\infty(L^{3,\infty})\)*, *Algebra i Analiz* 32
(2020), 238–253; traduction *St. Petersburg Math. J.* 32 (2021), 565–576,
DOI [10.1090/spmj/1662](https://doi.org/10.1090/spmj/1662),
[notice primaire MathNet](https://www.mathnet.ru/eng/aa1707), proposé
**NS-SRC-0161**, publié.

La conclusion dit, sous contrôle local temporel faible-\(L^3\), que le nombre
de points singuliers à chaque temps est fini dans le sens précis du papier,
y compris une analyse au voisinage d'une frontière plate.

Non-transfert : la quantité est celle de la vitesse d'une solution adaptée;
la pression, l'énergie locale et le temps sont essentiels. Aucun ensemble BV
statique de volume \(V\) et périmètre \(P\) n'est sélectionné.

### 7.3 Barker 2024 : packing quantitatif de centres singuliers

Tobias Barker, *Higher integrability and the number of singular points for
the Navier-Stokes equations with a scale-invariant bound*, *Proc. Amer. Math.
Soc. Ser. B* 11 (2024), 436–451, DOI
[10.1090/bproc/193](https://doi.org/10.1090/bproc/193), arXiv
[2111.14776v2](https://arxiv.org/abs/2111.14776v2), proposé
**NS-SRC-0162**. Prépublication v2 du 2021-11-30; article publié le
2024-09-12.

Cadre exact : solution faible de Leray–Hopf sur
\(\mathbb R^3\times[-1,0]\), premier temps de blow-up à \(0\), et suite
\(s_n\uparrow0\) telle que

\[
\sup_n\|v(\cdot,s_n)\|_{L^{3,\infty}(\mathbb R^3)}\le M.
\]

Le théorème borne le nombre de points singuliers à \(t=0\) par
\(O(M^{20})\). La preuve choisit une famille finie de centres, remonte assez
près de \(0\) pour que les boules paraboliques rescalées soient disjointes,
utilise l'epsilon-régularité pour imposer un budget positif dans chaque
cylindre, puis somme sous une borne espace-temps globale
\(O(M^{20})\).

C'est le parallèle Navier–Stokes le plus net avec un argument de packing de
gouttes multiples. Il ne fournit toutefois pas la boule BV recherchée :

- les centres sont déjà des points singuliers;
- le rayon est l'échelle parabolique \(\sqrt{-s_n}\);
- la masse minimale est une quantité espace-temps d'epsilon-régularité
  impliquant vitesse et pression;
- le budget global vient du faible-\(L^3\), de l'énergie et de la dynamique;
- aucune conclusion n'est formulée à partir de \(|E|\) et \(P(E)\) seuls.

Barker–Prange 2021, déjà **NS-SRC-0147**, contient aussi un bound effectif
du nombre de points singuliers sous scénario Type I, ainsi qu'une
concentration autour de chaque point. La version de Barker 2024 améliore le
coût en \(M\) à une puissance polynomiale dans son cadre, sans créer de
théorème géométrique statique.

## 8. Tableau des implications et non-transferts

| Source | Ce qu'elle implique | Ce qu'elle n'implique pas |
|---|---|---|
| Ambrosio–Caselles–Masnou–Morel 2001 | décomposition unique en composantes indécomposables, additivité du périmètre | diamètre ou boule contenant une composante |
| Besicovitch 1945/1946 | sous-recouvrements à multiplicité dimensionnelle contrôlée | masse locale sans inégalité de périmètre; confinement global |
| Lions 1984 | alternative compacité/évanescence/dichotomie via \(Q_n(r)\) | exclusion automatique de la dichotomie |
| Frank–Lieb 2015 | boule à l'échelle \(V/P\) avec masse \(\gtrsim(V/P)^3\); non-évanescence BV | fraction universelle, unicité du centre, diamètre de \(E\) |
| Fusco–Maggi–Pratelli 2008 | proximité d'une boule sous petite déficience isopérimétrique | proximité sphérique depuis une borne arbitraire de périmètre |
| Seregin 2001/2021 | finitude/contrôle des centres singuliers sous hypothèses de solution adaptée | sélection statique depuis volume+périmètre |
| Barker 2024 | packing quantitatif \(O(M^{20})\) de points singuliers | décomposition BV, contrôle Type II général, conclusion Clay |

## 9. Identifiants proposés à partir de NS-SRC-0156

| ID proposé | Source et statut | Rôle |
|---|---|---|
| **NS-SRC-0156** | Ambrosio–Caselles–Masnou–Morel 2001, DOI 10.1007/PL00011302, publié | composantes M-indécomposables et additivité du périmètre |
| **NS-SRC-0157** | Besicovitch 1945, DOI 10.1017/S0305004100022453, publié | covering/différentiation; multiplicité dimensionnelle |
| **NS-SRC-0158** | Fusco–Maggi–Pratelli 2008, DOI 10.4007/annals.2008.168.941, publié | isopérimétrie quantitative sharp |
| **NS-SRC-0159** | Frank–Lieb 2015, DOI 10.1137/15M1010658, publié | concentration locale BV et compacité après translations |
| **NS-SRC-0160** | Seregin 2001, DOI 10.1002/cpa.3002, publié | nombre de points singuliers à temps fixé |
| **NS-SRC-0161** | Seregin 2020/2021, DOI 10.1090/spmj/1662, publié | finitude locale sous contrôle faible-\(L^3\) |
| **NS-SRC-0162** | Barker 2024, DOI 10.1090/bproc/193, publié | packing polynomial de centres singuliers sous borne critique |

Ne pas créer de nouveaux IDs pour Lions 1984 (**NS-SRC-0140**),
Federer–Fleming (**NS-SRC-0148**, proposé au cycle 0035), Korte–Lahti
(**NS-SRC-0149**, proposé au cycle 0035) ou Barker–Prange 2021
(**NS-SRC-0147**).

## 10. Passe contradictoire

### Quantificateurs

- « Il existe une boule qui contient une masse positive » n'implique pas
  « une boule contient une fraction universelle de la masse ».
- « Une suite ne s'évanouit pas après translation » n'implique pas
  « la suite est globalement compacte modulo une seule translation ».
- « Une composante a un volume minoré » n'implique pas « cette composante a
  un diamètre contrôlé ».
- L'alternative de Lions laisse la dichotomie ouverte tant qu'une stricte
  sous-additivité ou une autre rigidité ne l'exclut pas.

### Constantes et échelles

- La borne locale Frank–Lieb contient le terme
  \(C_dr^{-1}V\). Le supprimer avant de choisir \(r\) serait une erreur.
- Le rayon naturel \(V/P\) devient petit lorsque le périmètre est grand; il
  ne peut être remplacé par \(V^{1/3}\) sans petit déficit ou borne supérieure
  de l'indice isopérimétrique.
- Les constantes de covering dépendent de la dimension. Une somme de
  périmètres locaux peut compter plusieurs fois les mêmes morceaux de bord.
- Dans Barker 2024, le nombre \(O(M^{20})\) dépend de la borne critique et des
  constantes d'epsilon-régularité; ce n'est pas un nombre universel de
  singularités.

### Notions de solution et écart Clay

- Les résultats géométriques portent sur des indicatrices BV, pas sur une
  solution Navier–Stokes ni sur un superniveau dont l'évolution est contrôlée.
- Les théorèmes multi-centres Navier–Stokes supposent des solutions adaptées
  ou Leray–Hopf, un temps singulier, et des budgets impliquant la pression.
- Une finitude de points singuliers sous Type I ou faible-\(L^3\) ne couvre
  pas un blow-up Type II général et ne résout pas le problème Clay.
- Pour utiliser la boule de Frank–Lieb sur un superniveau de vitesse ou
  vorticité, il faut encore obtenir un périmètre de ce superniveau au bon
  instant et à la bonne échelle. Le cycle 0035 l'obtient seulement pour les
  bandes explicites pure-swirl.

## Conclusion opérationnelle

La littérature fournit bien le lemme géométrique minimal suivant :

\[
\boxed{
\exists x\in\mathbb R^3:\quad
|E\cap B_{|E|/P(E)}(x)|
\ge c\left(\frac{|E|}{P(E)}\right)^3.}
\]

Elle ne fournit pas, depuis volume+périmètre seuls, une boule contenant une
fraction universelle de \(E\), une composante entière, ou tout \(E\). Les
contre-profils de translation et de fragmentation sont compatibles avec les
théorèmes et montrent que la perte \(|E|^2/P(E)^3\) est structurelle.

Le prochain test décisif n'est donc pas de chercher une meilleure covering
lemma générale. Il consiste à déterminer si les bandes de transition du
programme Navier–Stokes possèdent en plus soit :

1. un déficit isopérimétrique uniformément petit;
2. une quasi-minimalité excluant les tubes et la dichotomie;
3. ou un budget dynamique d'epsilon-régularité sommable sur plusieurs
   centres.

Sans l'une de ces informations, la boule Frank–Lieb est optimale au niveau
des lois d'échelle et ne se renforce pas en sélection d'une fraction
universelle.
