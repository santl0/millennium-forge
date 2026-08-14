# Cycle 0037 — revue primaire : diamètre planaire, coaire par composantes et persistance des ponts

Date de veille : 2026-08-15.

Périmètre : ensembles de périmètre fini dans \(\mathbb R^2\), composantes
indécomposables de superniveaux, arbres de fusion et persistance en degré zéro,
puis analogues Navier–Stokes portant réellement sur des filaments, la
géométrie des superniveaux ou plusieurs centres. Cette revue ne modifie ni le
catalogue ni le statut d'une affirmation du laboratoire.

## Verdict transférable

1. **Le cas planaire est strictement plus rigide que le cas tridimensionnel.**
   Si \(E\subset\mathbb R^2\) est indécomposable, de volume positif fini et de
   périmètre fini, alors

   \[
   2\,\operatorname{diam}(E^{(1)})\le P(E),                 \tag{1}
   \]

   où \(E^{(1)}\) est le représentant des points de densité un. C'est le
   lemme 2.13 publié de Dayrens–Masnou–Novaga–Pozzetta. Ainsi, contrairement à
   la conclusion générale tridimensionnelle du cycle 0036, **une composante
   indécomposable méridienne possède bien un diamètre essentiel contrôlé par
   son périmètre**.

2. Fleming–Rishel et Ambrosio–Caselles–Masnou–Morel donnent, pour presque tout
   niveau, la chaîne exacte

   \[
   |Df|(\mathbb R^2)
   =\int_{-\infty}^{\infty}P(\{f>t\})\,dt
   =\int_{-\infty}^{\infty}\sum_iP(E_{t,i})\,dt,           \tag{2}
   \]

   où \((E_{t,i})_i\) sont les composantes M-indécomposables de
   \(\{f>t\}\). Avec (1),

   \[
   |Df|(\mathbb R^2)
   \ge 2\int_{-\infty}^{\infty}
            \sum_i\operatorname{diam}(E_{t,i}^{(1)})\,dt. \tag{3}
   \]

   La seconde égalité et (3) sont des compositions analytiques des théorèmes
   publiés, pas un nouvel énoncé attribué à leurs auteurs.

3. Un arbre de fusion peut suivre **pendant combien de niveaux** deux gouttes
   restent dans la même composante. Si deux ensembles compacts distants de
   \(d>0\) rencontrent une même composante M-indécomposable pour presque tout
   \(t\in(a,b)\), (1)–(2) donnent le coût falsifiable

   \[
   |D T_{a,b}(f)|(\mathbb R^2)\ge 2(b-a)d,                 \tag{4}
   \]

   avec \(T_{a,b}(s)=\min\{(s-a)_+,b-a\}\). Le facteur
   \(b-a\) est la persistance en amplitude du pont; \(d\) est sa portée
   spatiale. L'arbre seul ne fournit ni \(d\), ni périmètre, ni variation
   totale.

4. **Le trou restant est exactement la persistance verticale.** Un pont qui
   ne dépasse le cutoff \(a\) que de \(\varepsilon\) n'est facturé par (4) que
   de \(2\varepsilon d\) dans la bande tronquée. Une connexité observée à un
   niveau unique ne donne donc aucune marge uniforme. Il faut soit sélectionner
   une branche de durée \(\gtrsim\lambda\), soit utiliser la variation située
   sous le cutoff, soit abandonner le renforcement.

5. Aucun article Navier–Stokes primaire trouvé ne combine actuellement :
   arbre de fusion des superniveaux, diamètre métrique de chaque branche,
   coaire pondérée méridienne, pression et évolution jusqu'à un temps maximal.
   Les sources Navier–Stokes pertinentes déjà cataloguées restent des critères
   conditionnels de parcimonie, des constructions filamentaires très
   structurées, ou des théorèmes de concentration multi-centres sous hypothèse
   critique. **Aucun nouvel identifiant Navier–Stokes n'est nécessaire.**

## 1. Les trois notions de connexité à ne pas confondre

### 1.1 Continu topologique

Si \(K\subset\mathbb R^2\) est un compact connexe rectifiable, alors

\[
\mathcal H^1(K)\ge\operatorname{diam}K.                    \tag{5}
\]

C'est une conséquence élémentaire : pour deux points presque diamétraux, la
fonction distance à l'un d'eux est 1-lipschitzienne et son image connexe
contient un intervalle de longueur presque égale au diamètre. Ce calcul interne
ne concerne pas le périmètre de De Giorgi d'un ensemble de volume positif.

Une courbe de Jordan fermée \(\Gamma\) vérifie plus fortement
\(\mathcal H^1(\Gamma)\ge2\operatorname{diam}\Gamma\) : les deux arcs entre
deux points diamétraux ont chacun une longueur au moins égale à leur distance.
C'est cette géométrie extérieure qui intervient dans la preuve de (1).

### 1.2 Connexité d'un représentant mesurable

Le diamètre topologique d'un représentant arbitraire n'est pas contrôlé par
le périmètre. Ajouter à un disque un segment de mesure bidimensionnelle nulle,
de longueur \(L\), ne change ni sa classe presque partout ni son périmètre de
De Giorgi, mais rend ce représentant connexe et augmente son diamètre de
\(L\). Toute affirmation correcte doit donc porter sur \(E^{(1)}\), sa
fermeture essentielle, ou un représentant ouvert régulier explicitement fixé.

### 1.3 Indécomposabilité BV

Un ensemble de périmètre fini \(E\) est indécomposable s'il ne peut pas être
écrit, à ensembles négligeables près, comme \(E=A\cup B\), avec
\(|A|,|B|>0\) et \(P(E)=P(A)+P(B)\). C'est la notion adaptée à la coaire.

Ambrosio–Caselles–Masnou–Morel (`NS-SRC-0156`) établissent l'existence et
l'unicité de la décomposition en composantes M-indécomposables, avec
additivité du périmètre. Dayrens et al. rappellent aussi qu'un ouvert connexe
dont le bord a une longueur finie est indécomposable. Pour un superniveau
lisse compact à valeur régulière, les composantes topologiques ouvertes et
les composantes M-indécomposables coïncident dans le sens nécessaire ici.

## 2. Source décisive : périmètre, diamètre et coût d'un connecteur planaire

### Métadonnées vérifiées

François Dayrens, Simon Masnou, Matteo Novaga et Marco Pozzetta,
[*Connected perimeter of planar sets*](https://arxiv.org/abs/1906.09814),
arXiv:1906.09814v3 du 2020-05-26; *Advances in Calculus of Variations*
15(2), 213–234 (2022), DOI
[10.1515/acv-2019-0050](https://doi.org/10.1515/acv-2019-0050), publié.
Identifiant proposé : **NS-SRC-0163**.

### Énoncés exacts utiles

- Le lemme 2.13 affirme (1) pour tout ensemble indécomposable de
  \(\mathbb R^2\) avec \(0<|E|<\infty\). Il s'agit du diamètre de
  \(E^{(1)}\), pas de celui d'un représentant arbitraire.
- La preuve sature \(E\), identifie la frontière extérieure à une courbe de
  Jordan lipschitzienne et utilise
  \(P(E)\ge P(\operatorname{sat}E)\ge2\operatorname{diam}(E^{(1)})\).
- Le théorème 4.1 donne, sous l'hypothèse de bord précisée dans l'article,

  \[
  \overline P_C(E)=P(E)+2\,St(E),                          \tag{6}
  \]

  où \(\overline P_C\) est la relaxation \(L^1\) du périmètre sous
  contrainte de connexité et \(St(E)\) la longueur de Steiner nécessaire pour
  connecter les parties de \(\overline{E^{(1)}}\).

La formule (6) interdit qu'un connecteur planaire de largeur tendant vers zéro
devienne gratuit en périmètre. Pour deux gouttes limites séparées de distance
\(d\), toute approximation connectée paie au moins \(2d\) au-dessus de leurs
périmètres propres.

### Portée exacte

Ce résultat ferme le faux contre-profil « deux gouttes méridiennes reliées par
un pont de longueur arbitraire mais de périmètre borné ». En dimension deux,
la largeur du pont peut tendre vers zéro, mais ses deux côtés conservent un
coût asymptotique égal à deux fois sa longueur.

Il ne ferme pas un pont qui n'existe que sur un intervalle de niveaux
arbitrairement court : après coaire, son coût est multiplié par sa persistance
en amplitude.

## 3. Coaire composante par composante

### Sources déjà suffisantes

- Wendell H. Fleming et Raymond Rishel, *An integral formula for total
  gradient variation*, *Archiv der Mathematik* 11 (1960), 218–222, DOI
  [10.1007/BF01236935](https://doi.org/10.1007/BF01236935),
  `NS-SRC-0132`, publié : formule de coaire BV.
- Luigi Ambrosio, Vicent Caselles, Simon Masnou et Jean-Michel Morel,
  *Connected components of sets of finite perimeter and applications to
  image processing*, *JEMS* 3 (2001), 39–92, DOI
  [10.1007/PL00011302](https://ems.press/journals/jems/articles/120),
  `NS-SRC-0156`, publié : décomposition M-connexe et additivité du
  périmètre.
- Dayrens–Masnou–Novaga–Pozzetta, lemme 2.13 : diamètre de chaque composante
  planaire.

Aucune quatrième source de « coaire par composantes » n'est nécessaire : (2)
est littéralement la composition de la coaire et de l'additivité du périmètre.

### Lemme composé à tester

Pour \(f\in W^{1,1}(\mathbb R^2)\) compactement supportée et
\(-\infty<a<b<\infty\), notons \(E_{t,i}\) les composantes
M-indécomposables de \(\{f>t\}\). Alors

\[
\int_{\{a<f<b\}}|\nabla f|\,dx
\ge2\int_a^b\sum_i\operatorname{diam}(E_{t,i}^{(1)})\,dt. \tag{7}
\]

Statut : **AI_DERIVATION**, à vérifier formellement quant aux représentants et
à la mesurabilité; elle n'est pas classée `PAPER_PROOF`. Pour l'expérience
pure-swirl lisse, il suffit de travailler aux valeurs régulières, qui ont
complément négligeable, puis d'intégrer l'inégalité pointwise.

### Scaling

Dans le plan, \(P(E)\) et \(\operatorname{diam}E\) ont l'homogénéité d'une
longueur. Si \(f_\rho(x)=A f(x/\rho)\),

\[
\int_{\mathbb R^2}|\nabla f_\rho|=A\rho\int|\nabla f|,
\]

et le membre droit de (4) vaut aussi amplitude fois longueur. Dans la bande
annulaire pure-swirl \(r\simeq R\), le relèvement axisymétrique ajoute le poids
\(2\pi r\), comparable à \(R\) avec les constantes annularies déjà suivies
par le laboratoire. Cette comparabilité est statique; elle ne produit ni
pression ni contrôle temporel.

## 4. Arbres de fusion et persistance : ce qu'ils certifient

### Arbre de jointure / contour tree

Hamish Carr, Jack Snoeyink et Ulrike Axen,
[*Computing contour trees in all dimensions*](https://www.sciencedirect.com/science/article/pii/S0925772102000937),
*Computational Geometry* 24(2), 75–94 (2003), DOI
[10.1016/S0925-7721(02)00093-7](https://doi.org/10.1016/S0925-7721(02)00093-7),
article publié; rapport technique UBC TR-99-09 du 1999-08-26 disponible sur
[le site institutionnel](https://www.cs.ubc.ca/tr/1999/tr-99-09).
Identifiant proposé : **NS-SRC-0164**.

Pour une fonction scalaire piecewise-linear sur un complexe simplicial, le
join tree suit les composantes connexes des superniveaux lors d'un balayage
descendant et enregistre leurs fusions. Le contour tree est obtenu en combinant
les arbres de jointure et de séparation. C'est le bon objet algorithmique pour
identifier le niveau auquel un pont fusionne deux gouttes.

### Persistance topologique

Herbert Edelsbrunner, David Letscher et Afra Zomorodian,
[*Topological persistence and simplification*](https://doi.org/10.1007/s00454-002-2885-2),
*Discrete & Computational Geometry* 28(4), 511–533 (2002), DOI
10.1007/s00454-002-2885-2, article publié. Identifiant proposé :
**NS-SRC-0165**.

L'article formalise la durée de vie de classes topologiques dans une
filtration finie. En degré zéro, les classes représentent les composantes qui
naissent et fusionnent. Cette persistance fournit l'intervalle vertical
\((a,b)\) de (4), sous les conventions d'appariement de la filtration.

### Non-implications

- Un arbre de fusion sans attribut métrique ne connaît pas la distance entre
  deux gouttes.
- Un diagramme de persistance \(H_0\) retient les durées de vie, mais pas toute
  la relation généalogique ni la géométrie spatiale de la branche.
- Ni Carr–Snoeyink–Axen ni Edelsbrunner–Letscher–Zomorodian ne donnent une
  borne de périmètre, de variation totale ou de curl.
- Leurs algorithmes travaillent sur une filtration discrète/tame. Un
  \(W^{1,1}\) ou BV arbitraire peut avoir une infinité de valeurs critiques et
  ne produit pas automatiquement un arbre fini.
- Un arbre calculé sur une grille ne devient une preuve du continuum qu'après
  certification des erreurs d'interpolation, des valeurs critiques et des
  connexions susceptibles de passer entre les mailles.

Le protocole utile est donc un **merge tree enrichi** : pour chaque branche,
stocker son intervalle de niveaux et une minoration certifiée du diamètre
essentiel. L'inégalité analytique (7), et non le code de persistance, transforme
ensuite ces attributs en coût BV.

## 5. Test adverse reproductible au niveau analytique

Fixons deux gouttes planaires lisses de diamètre \(O(R)\), séparées de
\(d=LR\), et un cutoff \(a=\lambda/4\).

### Pont à marge fixe

Si le pont appartient au même superniveau sur tout
\((a,a+\eta\lambda)\), avec \(\eta>0\) indépendant de \(L\), alors (4)
impose

\[
\int_{\{a<f<a+\eta\lambda\}}|\nabla f|
\ge 2\eta\lambda LR.                                      \tag{8}
\]

À budget BV fixé et paramètres \(\lambda,R\) fixés, \(L\) est borné. Réduire
la largeur transverse du pont ne change pas cette conclusion planaire.

### Pont rasant le cutoff

Si sa hauteur minimale vaut seulement
\(a+\varepsilon_L\lambda\), (8) devient

\[
2\varepsilon_L\lambda LR.                                \tag{9}
\]

Le choix \(\varepsilon_L\asymp L^{-1}\) garde ce coût de bande borné. Ce
contre-profil ne réfute pas (7); il montre que la persistance uniforme est une
hypothèse indispensable. Une expérience décisive doit donc faire varier
indépendamment longueur \(L\), largeur \(\delta\) et marge de niveau
\(\varepsilon\), puis vérifier que le coût converge vers
\(2\varepsilon\lambda LR\).

### Passage dimensionnel adverse

Dans \(\mathbb R^3\), deux boules unitaires éloignées de \(L\), reliées par
un tube lisse de rayon \(L^{-2}\), forment un ouvert connexe et
indécomposable de diamètre \(\simeq L\), tandis que l'aire latérale du tube
est \(O(L^{-1})\) et que le périmètre total reste borné. Ainsi (1) est
spécifiquement planaire et ne peut être appliquée aux composantes 3D du champ
général.

## 6. Analogues Navier–Stokes réellement pertinents

| Source primaire | Équation et statut | Information géométrique réelle | Non-transfert au verrou |
|---|---|---|---|
| Grujić 2001, *The geometric structure of the super-level sets and regularity for 3D Navier-Stokes equations*, DOI [10.1512/iumj.2001.50.1900](https://doi.org/10.1512/iumj.2001.50.1900), publié | NS 3D périodique, viscosité positive, critère conditionnel pour solution régulière | parcimonie par projections coordonnées des superniveaux de vitesse à l'échelle d'analyticité | ni composantes, ni arbre de fusion, ni diamètre/périmètre; la formulation R3 plus directement utile est déjà cataloguée sous `NS-SRC-0064` |
| Grujić 2013, `NS-SRC-0064`, publié | NS 3D non forcé sur \(\mathbb R^3\), solution mild avant temps singulier | parcimonie linéaire locale des superniveaux et prolongement | hypothèse conditionnelle; un filament connexe peut être sparse sans que son arbre soit contrôlé |
| Farhat–Grujić–Leitmeyer 2017, `NS-SRC-0065`, publié avec erratum | NS 3D sur \(\mathbb R^3\) | parcimonie volumique puis directionnelle à une échelle éventuellement plus petite | mesure de volume, pas généalogie des composantes ni coût d'un pont |
| Gancedo–Hidalgo-Torné 2025, `NS-SRC-0120`, publié | NS 3D visqueux, filament hélicoïdal, solution faible d'énergie locale puis lissage | filament véritable et régularité globale dans la classe hélicoïdale | symétrie forte et donnée mesure; ne contrôle pas un pont de superniveau d'une grande donnée Clay générale |
| Fontelos–Ispizua–Vega 2026, `NS-SRC-0124`, arXiv v1 | NS 3D visqueux sur \(\mathbb R^3\), petit rapport circulation/viscosité, temps court | vorticité concentrée autour d'une courbe et propagation de type soliton | prépublication, régime perturbatif; confirme qu'une géométrie filamentaire n'implique pas un blow-up |
| Barker–Prange 2021, `NS-SRC-0147`, publié | NS 3D non forcé, solution adaptée, hypothèse Type I faible-\(L^3\) | concentration quantitative près d'un premier point singulier | centre fourni par la singularité et hypothèse Type I; aucune composante de superniveau suivie |
| Seregin 2001 et 2020/21, `NS-SRC-0160`–`0161`, publiés | solutions faibles adaptées dans des cylindres locaux | finitude de points singuliers à temps fixé, avec hypothèse faible-\(L^3\) pour le second | packing espace-temps, pas connexion par pont ni diamètre de superniveau |
| Barker 2024, `NS-SRC-0162`, publié | Leray–Hopf sur \(\mathbb R^3\), borne faible-\(L^3\) le long d'une suite de temps | \(O(M^{20})\) centres singuliers par packing et epsilon-régularité | hypothèse critique additionnelle, Type II général non couvert, arbre de fusion absent |

La veille du 2026-08-15 a aussi contrôlé Benaroya–Enciso–Peralta-Salas,
[*Splitting and Merging of Stagnation Points of Solutions to the 2D
Navier-Stokes Equations*](https://arxiv.org/abs/2510.00784), arXiv v1 du
2025-10-01. Le papier construit en dimension deux des trajectoires prescrites
de points de stagnation. Ces points sont des zéros de vitesse, pas des
composantes de superniveaux, et la dimension deux est globalement régulière.
Il ne reçoit donc pas d'identifiant dans le corpus actif de ce verrou.

## 7. Implication explicite vers le programme pure-swirl

Le transfert statique exige les prémisses suivantes :

1. le potentiel méridien scalaire \(F_j(r,z)\) est continu ou lipschitzien et
   compactement supporté dans une bande \(r\simeq R_j\);
2. pour presque tout niveau, les objets suivis sont les composantes
   M-indécomposables planaires de \(\{\sigma F_j>t\}\), pas les composantes
   d'un représentant 3D arbitraire;
3. une même branche reliant deux coeurs séparés persiste sur un intervalle de
   niveaux de longueur quantifiée;
4. la coaire pondérée du relèvement cylindrique est comparée au curl réel sans
   annulation entre supports.

Sous ces prémisses, (4) transforme un pont de longueur \(LR_j\) et de
persistance \(\Delta t\) en un coût méridien au moins
\(2\Delta t\,LR_j\), puis en un coût 3D pondéré comparable à
\(R_j\Delta t\,LR_j\). Cela peut borner le diamètre de la composante active
si \(\Delta t\) est uniformément comparable à \(\lambda\).

Sans la prémisse 3, le pont peut raser le cutoff et l'argument ne compose pas
avec le gate directionnel. Sans les prémisses 1–2, (1) n'est pas applicable.
Sans la prémisse 4, la non-localité de la pression, les annulations du curl et
les chevauchements restent entièrement ouverts.

## 8. Passe contradictoire

1. **Mauvais diamètre.** (1) contrôle \(E^{(1)}\), jamais un représentant
   obtenu en ajoutant des ensembles nuls.
2. **Mauvaise dimension.** L'analogue périmètre–diamètre est faux en
   dimension trois; le dumbbell tubulaire ci-dessus le réfute.
3. **Topologique versus M-connexe.** Pour des niveaux BV irréguliers, les
   composantes à utiliser sont celles d'Ambrosio et al.; une implémentation par
   pixels calcule autre chose tant qu'un raccord n'est pas démontré.
4. **Niveau unique.** Un grand diamètre à \(t=a\) ne minore pas l'intégrale
   de coaire; une durée positive en niveau est indispensable.
5. **Persistance sans métrique.** Une longue branche verticale peut
   correspondre à deux gouttes spatialement proches; le facteur \(d\) doit
   être certifié séparément.
6. **Métrique sans persistance.** Deux gouttes éloignées qui fusionnent juste
   au cutoff ont un grand diamètre mais un coût de bande arbitrairement petit.
7. **Discrétisation.** Un pont plus fin qu'une maille peut être créé ou détruit
   par l'échantillonnage; aucun barcode flottant n'est une preuve.
8. **Filament n'est pas singularité.** Les constructions visqueuses
   `NS-SRC-0120` et `NS-SRC-0124` montrent des filaments réguliers dans leurs
   classes; la géométrie tubulaire seule n'a aucun signe de blow-up.
9. **Centres singuliers ne sont pas gouttes de niveau.** `NS-SRC-0160`–`0162`
   utilisent epsilon-régularité et budgets espace-temps; ils ne donnent pas
   la composante méridienne demandée.
10. **Clay.** Le lemme composé est statique et pure-swirl. Il n'ajoute ni
    temps maximal, ni pression, ni stretching, ni compactness–rigidity.

## 9. Identifiants proposés après NS-SRC-0162

| ID proposé | Source | Nécessité |
|---|---|---|
| **NS-SRC-0163** | Dayrens–Masnou–Novaga–Pozzetta 2022, DOI 10.1515/acv-2019-0050, publié | inégalité planaire exacte \(2\operatorname{diam}E^{(1)}\le P(E)\) et relaxation par longueur de Steiner |
| **NS-SRC-0164** | Carr–Snoeyink–Axen 2003, DOI 10.1016/S0925-7721(02)00093-7, publié | arbre de jointure des composantes de superniveaux et niveaux de fusion |
| **NS-SRC-0165** | Edelsbrunner–Letscher–Zomorodian 2002, DOI 10.1007/s00454-002-2885-2, publié | durée de vie des composantes dans une filtration |

Aucun ID supplémentaire n'est proposé pour la coaire, la décomposition BV ou
les analogues Navier–Stokes : les entrées `0132`, `0156`, `0064`, `0065`,
`0120`, `0124`, `0147` et `0160`–`0162` couvrent déjà exactement les briques
primaires pertinentes. Le papier Grujić 2001 est un antécédent historique de
`0064`, et le papier 2D sur les points de stagnation traite un objet différent.

## Conclusion opérationnelle

La veille invalide en dimension méridienne l'assertion trop large « le
périmètre ne contrôle pas le diamètre d'une composante ». La version correcte
est :

\[
\boxed{
E\subset\mathbb R^2\ \text{M-indécomposable}
\quad\Longrightarrow\quad
2\operatorname{diam}(E^{(1)})\le P(E).}
\]

Combinée à la coaire, elle facture un pont par le produit

\[
\boxed{\text{distance spatiale}\times\text{persistance en amplitude}.}
\]

Le prochain test décisif doit donc construire le merge tree enrichi des deux
gouttes du cycle 0036 et mesurer, avec intervalles certifiés, la hauteur exacte
du col qui les relie. Si cette hauteur reste à distance uniforme de
\(\lambda/4\), le diamètre est coercif par (8). Si elle converge vers le
cutoff comme \(L^{-1}\) ou plus vite tout en préservant les deux endpoints
faibles, l'approche par la seule bande doit être révisée.
