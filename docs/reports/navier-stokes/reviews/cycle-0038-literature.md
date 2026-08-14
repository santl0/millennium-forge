# Cycle 0038 — arbres de fusion certifiés, stabilité et coaire

Date de veille : **2026-08-15**
Périmètre : arbres de jointure/fusion et graphes de Reeb, stabilité sous erreur
uniforme, fonctions lisses et BV, raccord avec la coaire, usages dans les
écoulements de Navier–Stokes.
Objet actif : potentiel méridien scalaire (F(r,z)) d'un champ pure-swirl à
temps fixé; aucune dynamique Navier–Stokes n'est démontrée ici.

## 1. Verdict falsifiable

La couche topologique peut être rendue **certifiée**, mais seulement par une
composition de résultats distincts :

1. calcul combinatoire exact de l'arbre d'une fonction PL finie
   (`NS-SRC-0164`);
2. borne analytique ou par intervalles
   `||F-F_h||_∞ ≤ ε_h`;
3. stabilité de l'arbre ou du diagramme de persistance sous cette erreur;
4. ajout de labels géométriques certifiés, absents des arbres usuels;
5. application séparée de la coaire et de l'inégalité
   (2operatorname{diam}(E^{(1)})le P(E)) (`NS-SRC-0163`).

Deux corrections sont décisives pour le lemme actif.

- Une barre (H_0) longue mesure, pour une filtration de superniveaux, la
  différence « maximum local moins niveau de fusion ». Le coût de pont du
  cycle 0037 dépend au contraire de « niveau de fusion moins cutoff (a) ».
  Une grande persistance homologique n'empêche donc pas un col de raser le
  cutoff.
- La quantité minimale à certifier est le **niveau maximin de connexion de
  deux coeurs spatialement étiquetés**, pas seulement un barcode. Cette
  quantité est elle-même 1-lipschitzienne pour la norme uniforme et perd
  `ε_h`, au lieu de `2ε_h` pour une durée de barre.

Pour une fonction BV arbitraire, aucun arbre pointwise fini et invariant de la
classe (L^1) n'est disponible : une modification sur un ensemble nul peut
changer les connexions topologiques sans changer la fonction BV ni sa dérivée
distributionnelle. La réparation par représentants de densité un et
composantes M-indécomposables fonctionne niveau par niveau presque partout,
mais ne fournit pas encore une généalogie finie entre niveaux.

Enfin, la veille trouve des arbres de fusion/Reeb effectivement appliqués à
des écoulements numériques 2D ou compressibles. Aucun de ces travaux ne donne
un critère de régularité 3D, une borne coaire multi-niveaux, ni un certificat
continuum relié au problème Clay.

## 2. Sources primaires et statut exact

### 2.1 Stabilité des diagrammes de persistance

David Cohen-Steiner, Herbert Edelsbrunner et John Harer,
[*Stability of Persistence Diagrams*](https://doi.org/10.1007/s00454-006-1276-5),
*Discrete & Computational Geometry* **37** (2007), 103–120, DOI
`10.1007/s00454-006-1276-5`, publié en ligne le 2006-12-12, numéro de 2007.

Le théorème principal porte sur un espace triangulable (X) et deux fonctions
continues *tame* (f,g:X\to\mathbb R) :

\[
d_B(D(f),D(g))\le \lVert f-g\rVert _\infty .             \tag{2.1}
\]

Conséquence exacte : si `||f-g||_∞ ≤ ε`, une barre
de `f` de longueur strictement supérieure à `2ε` ne peut pas
être envoyée sur la diagonale; elle est appariée à une barre de (g), avec
déplacement de chaque extrémité d'au plus `ε`. Sa durée peut donc
diminuer de `2ε`.

**Transfert.** (2.1) certifie les naissances et morts (H_0), pas l'identité
spatiale des gouttes, tout l'arbre généalogique, un diamètre ou un périmètre.
La condition *tame* doit être vérifiée pour le continuum; elle est automatique
pour la filtration PL finie du calcul.

Identifiant proposé : **NS-SRC-0168**.

### 2.2 Stabilité des arbres de fusion

Robert Cardona, Justin Curry, Tung Lam et Michael Lesnick,
[*The Universal \(\ell^p\)-Metric on Merge Trees*](https://doi.org/10.4230/LIPIcs.SoCG.2022.24),
SoCG 2022, LIPIcs **224**, article 24, 24:1–24:20, DOI
`10.4230/LIPIcs.SoCG.2022.24`, publié; prépublication
[arXiv:2112.12165v2](https://arxiv.org/abs/2112.12165), 2022-03-21.

Les énoncés pertinents sont :

- pour des fonctions cellulaires monotones (f,g) sur le même complexe
  cellulaire régulier,
  (d_I^p(M_f,M_g)\le\lVert f-g\rVert_p) (théorème 1.2);
- (d_I^infty=d_I), la distance d'entrelacement ordinaire
  (théorème 1.4);
- le papier rappelle également le théorème de Morozov–Beketayev–Weber
  `d_I(M_f,M_g) ≤ ||f-g||_∞` pour deux fonctions sur un même
  espace.

Le manuscrit de Dmitriy Morozov, Kenes Beketayev et Gunther Weber,
[*Interleaving Distance between Merge Trees*](https://www.mrzv.org/publications/interleaving-distance-merge-trees/),
a été présenté à TopoInVis 2013, mais aucune publication avec DOI n'a été
trouvée. Cardona et al. fournit donc le point d'appui publié préférable pour
la stabilité et précise que son cadre d'universalité concerne des arbres à un
nombre fini de noeuds.

**Transfert.** Une erreur uniforme certifiée fournit un entrelacement de
taille `ε`. Elle ne fournit pas automatiquement un appariement
unique des branches, ni leurs positions dans le plan. Les labels géométriques
doivent rester attachés à des coeurs fixés ou être certifiés séparément.

Identifiant proposé : **NS-SRC-0169**.

### 2.3 Graphes de Reeb PL

Ulrich Bauer, Claudia Landi et Facundo Mémoli,
[*The Reeb Graph Edit Distance is Universal*](https://doi.org/10.1007/s10208-020-09488-3),
*Foundations of Computational Mathematics* **21** (2021), 1441–1464,
DOI `10.1007/s10208-020-09488-3`, version publiée le 2020-12-29.

Le cadre est celui de fonctions PL sur des espaces compacts triangulables.
Le graphe de Reeb quotient les composantes connexes des **ensembles de
niveau**, alors qu'un join/merge tree suit les composantes de
superniveaux/sous-niveaux. Les auteurs construisent une distance d'édition
stable et universelle. La stabilité signifie, pour deux réalisations sur un
domaine commun,

\[
d_U(R_f,R_g)\le\lVert f-g\rVert_\infty .                 \tag{2.2}
\]

**Transfert.** (2.2) traite correctement les cycles possibles d'un graphe de
Reeb, notamment sur un tore. Le domaine méridien actif n'a besoin que de
l'arbre de superniveaux. Le résultat n'ajoute ni coaire, ni métrique spatiale,
ni certificat BV.

Identifiant proposé : **NS-SRC-0170**.

### 2.4 Veille 2025–2026 directement pertinente, sans nouvel ID actif

- Qingsong Wang, Guanqun Ma, Raghavendra Sridharamurthy et Bei Wang,
  [*Measure-Theoretic Reeb Graphs and Reeb Spaces*](https://doi.org/10.1007/s00454-025-00789-4),
  *Discrete & Computational Geometry* **75** (2026), 511–536, DOI
  `10.1007/s00454-025-00789-4`, version of record du 2025-10-30;
  [arXiv:2401.06748v3](https://arxiv.org/abs/2401.06748). Le titre ne signifie
  pas « graphe de Reeb d'une fonction BV modulo égalité presque partout ».
  Les constructions équipent le domaine ou l'image d'une mesure, emploient
  un lissage local ou des fonctions distance-à-la-mesure/kernel, puis prouvent
  des stabilités. Elles ne résolvent pas la dépendance au représentant BV ni
  la décomposition coaire en composantes M-indécomposables.
- Thijs Beurskens, Tim Ophelders, Bettina Speckmann et Kevin Verbeek,
  [*Locally Correct Interleavings Between Merge Trees*](https://doi.org/10.4230/LIPIcs.SoCG.2026.11),
  SoCG 2026, LIPIcs **367**, article 11, DOI
  `10.4230/LIPIcs.SoCG.2026.11`, publié le 2026-05-27. Le papier construit des
  entrelacements localement corrects afin d'améliorer les appariements induits
  par une distance bottleneck. Il ne certifie ni l'approximation d'un champ
  lisse par un maillage, ni les labels spatiaux, ni la coaire.
- Matteo Pegoraro et Piercesare Secchi,
  [*Functional Data Representation with Merge Trees*](https://doi.org/10.1080/10618600.2026.2654769),
  *Journal of Computational and Graphical Statistics*, DOI
  `10.1080/10618600.2026.2654769`, manuscrit accepté le 2026-03-19 et version
  auteur acceptée mise en ligne le 2026-04-09; la page éditeur avertit que ce
  n'est pas encore la Version of Record. Les résultats d'estimation sont
  développés pour des données fonctionnelles, principalement sur un domaine
  unidimensionnel, et ne donnent pas l'arbre coaire d'un champ BV planaire.
- Daniel Perez,
  [*On \(C^0\)-persistent homology and trees*](https://arxiv.org/abs/2012.02634),
  arXiv `2012.02634v3` du 2022-11-23, prépublication sans DOI de journal trouvé.
  Le travail étend les arbres à des fonctions continues irrégulières; il ne
  s'applique toujours pas aux classes BV définies presque partout.
- Petar Hristov, Ingrid Hotz et Talha Bin Masood,
  [*Exact Computation of Trait-induced Merge Trees for Bivariate Fields*](https://arxiv.org/abs/2608.07181),
  arXiv `2608.07181v1` du 2026-08-07. Il calcule exactement un arbre spécialisé
  de distance à un trait pour un champ bivarié PL et borne l'erreur d'une
  interpolation particulière. Cette prépublication très récente ne traite
  pas l'arbre d'un scalaire lisse/BV général et n'est pas une brique du lemme
  actif.

Ces cinq références restent dans la veille : elles affinent l'algorithmique
ou la robustesse, mais aucune n'est nécessaire au raccord minimal ci-dessous.

## 3. Lisse, PL, continu et BV : domaines de validité

### 3.1 Fonction Morse ou PL finie

Pour une fonction de Morse sur une variété compacte, ou pour une fonction PL
sur un complexe fini avec ordre des sommets fixé, le graphe de Reeb et les
arbres de jointure/fusion sont des graphes finis. `NS-SRC-0164` calcule le
contour tree d'un champ PL en combinant join tree et split tree. Ce calcul est
exact **pour le problème PL donné** si les comparaisons de valeurs et les
opérations combinatoires sont exactes.

Un code en virgule flottante n'établit toutefois pas que :

- les valeurs proches ou égales sont ordonnées correctement;
- le champ PL approche le champ continu avec une erreur uniforme connue;
- aucun pont sous-maille n'a été détruit ou créé;
- les distances, diamètres ou périmètres des composantes sont certifiés.

### 3.2 Fonction lisse non tame

« Lisse sur un compact » ne suffit pas à garantir un arbre fini. Une fonction
(C^infty) plate et oscillante près d'un point peut posséder une infinité de
valeurs critiques et de changements de composantes. Les théorèmes formulés
pour fonctions tame, Morse ou arbres à nombre fini de noeuds ne peuvent donc
pas être appliqués à une fonction lisse générale sans hypothèse ou réduction
supplémentaire.

La stabilité reste utile après approximation, mais elle n'affirme pas que
l'arbre continu est combinatoirement identique à l'arbre PL : seules les
structures séparées par une marge supérieure à l'erreur sont robustes.

### 3.3 Fonction BV

Soit `f=0` presque partout dans un carré. Modifier ce représentant et poser
`f_rep=1` sur une courbe de mesure bidimensionnelle nulle ne change ni la
classe `L^1`, ni `Df`, ni `|Df|`. Pourtant
`{f>1/2}=∅` et `{f_rep>1/2}` contient une courbe; leur
topologie pointwise diffère. De même, enlever d'un représentant un mur nul
peut casser une connexion pointwise sans changer l'objet BV.

Le bon énoncé coaire utilise donc, pour presque tout (t), les représentants
de densité et les composantes M-indécomposables des ensembles de périmètre
fini (`NS-SRC-0156`, `NS-SRC-0163`). Cela donne une collection canonique de
composantes **à un niveau donné presque partout**, mais pas :

- une correspondance parent–enfant entre deux niveaux;
- un nombre fini de branches;
- des valeurs de fusion définies à tous les niveaux;
- une stabilité (L^1) d'un arbre de connexions.

Le résultat récent `NS-SRC-0166` sur la topologie 1-fine clarifie le
représentant connexe d'un ensemble indécomposable, mais reste une
prépublication et ne construit pas cette généalogie multi-niveaux.

## 4. Coaire pondérée par les composantes

Pour (f\in W^{1,1}_{\mathrm{loc}}(\mathbb R^2)), ou plus généralement BV
avec (|Df|), posons (E_t={f>t}). Pour presque tout (t), décomposons
(E_t) en composantes M-indécomposables (E_{t,i}). La coaire
(`NS-SRC-0132`), l'additivité du périmètre (`NS-SRC-0156`) et
`NS-SRC-0163` donnent, pour (a<b),

\[
\begin{aligned}
 |D T_{a,b}(f)|(\mathbb R^2)
 &=\int_a^b P(E_t)\,dt \\
 &=\int_a^b\sum_iP(E_{t,i})\,dt \\
 &\ge 2\int_a^b\sum_i
      \operatorname{diam}(E_{t,i}^{(1)})\,dt .           \tag{4.1}
\end{aligned}
\]

Ici (T_{a,b}) est la troncature à valeurs dans ([a,b]). (4.1) est un
théorème analytique niveau par niveau; aucun algorithme d'arbre n'est requis
pour sa validité. L'arbre sert uniquement à identifier de façon reproductible
quelle composante doit conserver un grand diamètre sur quel intervalle de
niveaux.

Il n'existe dans les sources auditées aucun théorème unique « coaire sur un
merge tree » qui fournirait à la fois la généalogie, les poids de périmètre et
les diamètres. Leur composition dans le laboratoire est donc une dérivation
nouvelle à garder sous statut `COMPUTATION_ONLY` ou `INTERNAL_DERIVATION`, pas
une preuve papier attribuable aux sources.

## 5. Raccord certifié minimal vers le lemme actif

### 5.1 Inclusions de superniveaux

Dans cette section, (F) et (F_h) sont des représentants continus sur le
même domaine planaire. Si le champ PL (F_h) vérifie

\[
\lVert F-F_h\rVert_\infty\le\varepsilon_h,               \tag{5.1}
\]

alors, pour tout (t),

\[
\{F_h>t+\varepsilon_h\}
\subset \{F>t\}
\subset \{F_h>t-\varepsilon_h\}.                        \tag{5.2}
\]

(5.2) est le raccord continu le plus direct. Une composante connectée de
l'ensemble intérieur à gauche reste connectée dans le vrai superniveau.
L'implication inverse, notamment le transfert d'une déconnexion, n'est pas
valide par simple inclusion.

### 5.2 Niveau maximin de connexion

Pour deux points/coeurs fixés (x_-,x_+), définissons

\[
m_f(x_-,x_+)
=\sup_{\gamma:x_-\leadsto x_+}\ \inf_{x\in\gamma} f(x),  \tag{5.3}
\]

où les chemins admissibles sont pris dans le domaine fixé. Alors

\[
|m_f(x_-,x_+)-m_g(x_-,x_+)|
\le\lVert f-g\rVert_\infty.                              \tag{5.4}
\]

Preuve : pour chaque chemin, les deux infima diffèrent d'au plus la norme
uniforme; prendre ensuite le supremum conserve la même borne. Cette dérivation
élémentaire est indépendante de toute finitude de l'arbre.

Pour un champ PL tame sur un complexe localement connexe, (5.3) est la hauteur
du sommet de fusion des deux labels dans le join tree. Pour une fonction
continue pathologique, (5.3) reste un certificat de connexion par chemins,
mais il ne faut pas l'identifier sans preuve à une fusion définie seulement
par composantes connexes.

Si (d=|x_--x_+|) et (m_F>a), pour presque tout
(t\in(a,m_F)), les deux coeurs appartiennent à une même composante de
({F>t}), dont le diamètre essentiel est au moins (d), sous le choix
rigoureux des représentants et coeurs. (4.1) donne donc

\[
|D T_{a,m_F}(F)|(\mathbb R^2)
\ge 2d(m_F-a).                                           \tag{5.5}
\]

Posons (b_h=m_{F_h}(x_-,x_+)-\varepsilon_h). En combinant (5.1),
(5.4) et (5.5), la sortie numérique falsifiable, entièrement paramétrée par
des quantités certifiées, est

\[
\boxed{
|D T_{a,b_h}(F)|(\mathbb R^2)
\ge 2d\,[m_{F_h}(x_-,x_+)-\varepsilon_h-a]_+ .}          \tag{5.6}
\]

Le crochet positif doit être strictement séparé de zéro pour produire une
information. Cette formule certifie exactement la marge « col moins cutoff »
requise au cycle 0037.

### 5.3 Pourquoi le barcode seul échoue

Dans une filtration de superniveaux, supposons que deux maxima valent
(M_1,M_2) et fusionnent au col (s). La barre tuée à la fusion a une durée
de type (min(M_1,M_2)-s), alors que (5.5) utilise (s-a). On peut garder
(min(M_1,M_2)-s\simeq 1) tout en imposant (s-a\to0). Ainsi :

\[
\text{barre longue}\centernot\Longrightarrow
\text{pont persistant au-dessus du cutoff}.              \tag{5.7}
\]

La stabilité bottleneck de (2.1) ne répare pas (5.7). Il faut enregistrer le
sommet de fusion (s), le cutoff (a), les coeurs spatiaux et leur distance.
Un arbre de fusion enrichi, ou directement (5.3), est donc nécessaire.

## 6. Chaîne de certification reproductible proposée

Pour l'expérience décisive du parent, la chaîne minimale est :

1. fixer un rectangle méridien compact et deux coeurs rationnels
   (x_-,x_+);
2. construire une triangulation explicite et un interpolant (F_h);
3. certifier (5.1) sur chaque simplex par bornes de dérivées ou arithmétique
   d'intervalles avec arrondi dirigé;
4. attribuer des valeurs rationnelles ou des intervalles disjoints aux
   sommets afin que toutes les comparaisons de l'union-find soient exactes;
5. calculer le join tree PL (`NS-SRC-0164`) et le niveau de fusion
   (m_{F_h}(x_-,x_+));
6. certifier la distance (d) et évaluer rationnellement le membre droit de
   (5.6);
7. répéter sous raffinement (h\mapsto h/2) et avec une seconde
   triangulation; exiger `ε_h → 0` et une marge positive stable;
8. seulement ensuite relever cylindriquement la borne coaire et vérifier les
   facteurs (R/r), les supports et les annulations possibles du curl.

Un arbre PL exact sans étape 3 certifie le discret, pas le continuum. Une
borne (5.1) sans étapes 4–5 certifie des inclusions mais pas la valeur de
fusion calculée. Ni l'un ni l'autre ne contrôle la pression ou l'évolution
temporelle.

## 7. Analogues dans les écoulements de Navier–Stokes

### 7.1 Analogue publié le plus récent

Mitsuaki Kimura, Takeshi Matsumoto, Takashi Sakajo, Hiroshi Takeuchi et Tomoo
Yokoyama,
[*Topological vortex identification for two-dimensional turbulent flows in doubly periodic domains*](https://doi.org/10.1016/j.physd.2025.135099),
*Physica D* **488** (avril 2026), 135099, DOI
`10.1016/j.physd.2025.135099`, publié; prépublication
[arXiv:2410.20010v2](https://arxiv.org/abs/2410.20010), 2025-09-15.

Équations réellement utilisées : Navier–Stokes incompressible **2D** visqueux
sur (mathbb T^2), non forcé pour la décroissance libre et forcé avec friction
grande échelle pour le régime statistiquement stationnaire. L'objet
topologique est le graphe de Reeb/COT des niveaux de la fonction de courant
instantanée, donc la topologie des lignes de courant, pas l'arbre des
superniveaux de vorticité 3D.

Le calcul spectral utilise un désaliasage (2/3); l'analyse annoncée prend
2 500 snapshots et grossit les grilles (2048^2) vers (256^2), de sorte que
les structures sous l'échelle (1/256) ne sont pas détectées. Il s'agit d'une
classification mathématique des Hamiltoniens structurellement stables puis
d'une analyse numérique/statistique de turbulence, pas d'une preuve assistée
par ordinateur avec erreur continuum.

**Non-transfert explicite :**

\[
\text{COT de }\psi(t)\text{ en 2D sur }\mathbb T^2
\not\Rightarrow
\text{borne multi-niveaux de }|\omega|\text{ en NS 3D},
\]

car manquent la dimension 3, l'étirement de vorticité, le contrôle de
pression, l'erreur de coarse-graining et une inégalité coaire coercive.

Identifiant proposé : **NS-SRC-0171**.

### 7.2 Antécédents numériques contrôlés, sans nouvel ID

- Koji Ohkitani et Fayeza Al Sulti,
  [*Quantification of topological changes of vorticity contours in two-dimensional Navier–Stokes flow*](https://doi.org/10.1103/PhysRevE.81.067302),
  *Physical Review E* **81** (2010), 067302, DOI
  `10.1103/PhysRevE.81.067302`, publié. Les auteurs suivent par DNS à nombre de
  Reynolds relativement faible les points critiques de la vorticité et de la
  fonction de courant, et vérifient numériquement un théorème d'indice. Ce
  n'est ni un join tree certifié ni un résultat 3D.
- Peer-Timo Bremer, Andrea Gruber, Janine C. Bennett, Attila Gyulassy,
  Hemanth Kolla, Jacqueline H. Chen et Ray W. Grout,
  [*Identifying Turbulent Structures through Topological Segmentation*](https://doi.org/10.2140/camcos.2016.11.37),
  *Communications in Applied Mathematics and Computational Science* **11**
  (2016), 37–53, DOI `10.2140/camcos.2016.11.37`, publié. Le papier utilise
  explicitement un merge tree d'indicateurs tourbillonnaires et des seuils
  locaux sur une DNS de jet transverse. Le solveur traite les équations de
  Navier–Stokes **compressibles réactives** multi-espèces. La sortie est une
  segmentation de structures, non une borne d'énergie/enstrophie ou un calcul
  validé.

Ces travaux établissent que l'idée multi-niveaux est computationnellement
non vide, mais aussi que son usage existant est descriptif : extraction de
structures, statistiques et visualisation. Ils ne fournissent aucune arête
nouvelle vers le problème Clay.

## 8. Passe contradictoire

1. **Mauvaise persistance.** Une barre (H_0) longue ne minore pas
   (s-a); (5.7) donne le contre-scénario.
2. **Appariement non spatial.** Une distance bottleneck ou d'entrelacement ne
   sait pas quelles deux gouttes physiques sont comparées. Les coeurs doivent
   être fixés ou labellisés.
3. **Erreur (L^1) utilisée comme (L^infty).** La convergence BV stricte
   ou (L^1) ne permet pas (5.2) et ne stabilise pas la connectivité
   pointwise.
4. **Fonction lisse supposée tame.** Une infinité de valeurs critiques peut
   subsister; la finitude doit être prouvée ou contournée par (5.3).
5. **Exactitude discrète confondue avec continuum.** L'union-find exact sur
   (F_h) ne donne aucune borne sur (F-F_h).
6. **Valeurs critiques presque égales.** Sans intervalles disjoints, une
   permutation due aux arrondis change la combinatoire de l'arbre.
7. **Inclusion utilisée dans le mauvais sens.** La connexité d'un ensemble
   intérieur se transfère au superensemble; la déconnexion d'un ensemble
   intérieur ne se transfère pas.
8. **Diamètre topologique au lieu du diamètre essentiel.** (4.1) contrôle
   (E_{t,i}^{(1)}), pas un représentant enrichi d'une courbe nulle.
9. **Reeb versus merge tree.** Le graphe de Reeb suit les niveaux; le join
   tree suit les superniveaux. Sur (mathbb T^2), le premier peut avoir une
   boucle et ne doit pas être remplacé silencieusement par un arbre.
10. **Mesure-théorique n'est pas BV.** Wang et al. enrichit le domaine ou
    l'image par une mesure; cela ne rend pas les superniveaux d'une classe BV
    indépendants du représentant.
11. **Analyse de flux n'est pas preuve PDE.** Kimura et al. grossit les
    snapshots et Bremer et al. travaille en compressible réactif; aucun
    passage validé au continuum 3D n'est présent.
12. **Clay.** Même (5.6) certifiée reste statique, planaire et pure-swirl.
    Elle ne contrôle ni pression non locale, ni stretching, ni temps maximal,
    ni compacité d'une suite de solutions.

## 9. Identifiants proposés après NS-SRC-0167

| ID proposé | Source primaire | Motif d'inclusion |
|---|---|---|
| **NS-SRC-0168** | Cohen-Steiner–Edelsbrunner–Harer 2007, DOI `10.1007/s00454-006-1276-5`, publié | stabilité bottleneck exacte sous erreur (L^infty) et seuil robuste (2\varepsilon) |
| **NS-SRC-0169** | Cardona–Curry–Lam–Lesnick 2022, DOI `10.4230/LIPIcs.SoCG.2022.24`, publié | stabilité/universalité publiée de la distance d'entrelacement des merge trees finis |
| **NS-SRC-0170** | Bauer–Landi–Mémoli 2021, DOI `10.1007/s10208-020-09488-3`, publié | définition/stabilité exacte des graphes de Reeb PL, utile pour distinguer graphe et arbre |
| **NS-SRC-0171** | Kimura–Matsumoto–Sakajo–Takeuchi–Yokoyama 2026, DOI `10.1016/j.physd.2025.135099`, publié | analogue Navier–Stokes 2D récent utilisant un Reeb/COT, avec non-transfert précisément auditable |

Aucun ID n'est proposé pour les cinq références de veille de §2.4 ni pour les
deux antécédents de §7.2 : ils n'ajoutent pas une prémisse nécessaire au lemme
actif. Ils peuvent être promus ultérieurement si le laboratoire ouvre un axe
algorithmique ou de visualisation des flux.

## 10. Conclusion opérationnelle

Le premier maillon transférable n'est pas « un barcode persistant implique un
pont coûteux ». Il est le lemme plus précis :

\[
\boxed{
\begin{gathered}
\lVert F-F_h\rVert_\infty\le\varepsilon_h,\qquad
d=|x_--x_+|,\\
m_{F_h}(x_-,x_+)>a+\varepsilon_h\\
\Longrightarrow
|D T_{a,m_{F_h}-\varepsilon_h}(F)|(\mathbb R^2)
\ge 2d\,[m_{F_h}(x_-,x_+)-a-\varepsilon_h].
\end{gathered}}
\]

Le test adverse décisif doit donc calculer exactement
`m_{F_h}(x_-,x_+)`, certifier `ε_h`, et vérifier si la marge
`m_{F_h}-a-ε_h` reste uniforme dans la famille dyadique du cycle
0037. Si elle décroît comme (L^{-1}), le merge tree confirme le
contre-profil du pont rasant; si elle reste positive, (5.6) fournit la borne
coaire–diamètre attendue. Dans les deux cas, le résultat est falsifiable et ne
requiert pas de confondre un calcul d'arbre avec une preuve Navier–Stokes.
