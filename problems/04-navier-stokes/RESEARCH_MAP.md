# Carte adaptative de recherche

Mise à jour : 2026-08-14. Cible : NS incompressible 3D, viscosité constante
positive, `R^3` ou `T^3`, sans force en priorité, donnée initiale lisse Clay.

## Chaîne principale

```text
donnée Clay
  -> solution classique locale unique
  -> temps maximal T_*
  -> critère critique de prolongement
  -> concentration si T_* est fini
  -> solution ancienne / profil / mesure de défaut
  -> rigidité dans la classe limite
  -> contradiction et régularité globale
```

Le graphe annoté et les arêtes manquantes sont détaillés dans
[`dependencies.md`](../../proof-graphs/navier-stokes/dependencies.md).

## Axes distincts

### A — Compacité–rigidité critique

- Verrou : obtenir un élément minimal sans supposer la borne critique que l'on
  cherche précisément à démontrer.
- Lemme minimal : toute séquence de premier blow-up ayant une borne critique
  donnée admet, après translation et changement d'échelle, une limite ancienne
  non nulle, adaptée, avec pression convergente localement.
- Échec actuel : l'énergie seule permet dichotomie et cascade; la convergence
  faible ne passe pas dans le terme quadratique sans information locale.
- Test discriminant : construire des paquets divergence-free multi-échelles et
  mesurer le défaut de compacité de `u_n tensor u_n` et des Riesz de pression.
- Circularité : introduire une borne `L^3` uniforme sous un autre nom.
- Coût : élevé (analyse de profils et pression).
- Abandon local : contre-suite certifiée montrant qu'une hypothèse candidate ne
  contrôle pas le défaut quadratique.

### B — Fonctionnelle coercive critique

- Verrou : remplacer l'énergie supercritique par une quantité de signe.
- Lemme minimal : une fonctionnelle invariante d'échelle `F(u)` contrôle une
  norme de prolongement et satisfait `dF/dt <= C(nu,F)` sans norme
  supercritique cachée.
- Échec actuel : les normes critiques utiles ne sont ni quadratiques ni
  monotones; pression et transport produisent des commutateurs sans signe.
- Test discriminant : optimisation adversariale sur polynômes trigonométriques
  divergence-free, en suivant exactement les triades signées.
- Circularité : coefficient de Grönwall dépendant de `||u||_infinity` ou d'une
  intégrale Serrin non contrôlée.
- Coût : moyen; calcul fini exact possible pour réfuter des candidats.
- Abandon local : une famille multi-échelle rend la dérivée positive sans borne
  en fonction de `F` seul.

### C — Géométrie de la vorticité

- Verrou : transformer l'alignement observé en déplétion déterministe.
- Lemme minimal : dans toute région de grande vorticité, une cohérence de
  direction quantitativement critique suit des seules contraintes NS et de
  l'énergie.
- Échec actuel : le terme `omega dot nabla u` est non local et sans signe; des
  champs divergence-free peuvent avoir hélicité nulle mais flux instantané non
  nul.
- Test discriminant : chercher des champs à tubes minces, hélicité prescrite et
  étirement maximal sous contraintes exactes de divergence.
- Circularité : supposer une régularité Hölder de la direction là où `omega`
  est grand.
- Coût : moyen à élevé.
- Abandon local : contre-profils maintenant les invariants tout en violant la
  déplétion proposée.

### D — Pression non locale et localisation

- Verrou : fermer une énergie locale critique sans perte par les queues.
- Lemme minimal : un commutateur localisé de la projection de Leray est borné
  uniformément par une quantité critique locale plus un terme de queue
  sommable.
- Échec actuel révisé : la queue distante centrée est petite sous la tension
  pondérée `L²(|y|^-4dy)`, et une borne globale `L³` donne cette tension en
  `A^-3`. L'énergie seule ne la donne pas après zoom. Même parmi des solutions
  NS globales lisses, la convergence faible de traces mobiles ne suffit pas à
  la compacité quadratique; l'intérieur espace-temps reste compact sous les
  hypothèses usuelles d'approximation. Le module énergétique
  `C_t^(1/4)H^-1` perd en outre une puissance d'échelle et ne contrôle pas la
  trace forte.
- Test discriminant : axe suspendu sous énergie seule après trois stratégies
  distinctes. Ne le rouvrir qu'avec une structure explicitement héritée d'un
  premier blow-up.
- Circularité : absorber la queue par une norme globale critique non disponible.
- Coût : moyen.
- Abandon local : famille éloignée à énergie bornée dont le commutateur ne tend
  pas à zéro à l'échelle exigée.

### E — Solutions anciennes et profils Type II

- Verrou : théorème de Liouville dans une classe assez large pour toute limite
  de blow-up.
- Lemme minimal fermé conditionnellement : une ancienne mild KNSS globalement
  bornée et de vraie trace terminale nulle dans `D'` est triviale, par lissage
  uniforme, rétro-unicité de la vorticité et jauge mild.
- Échec actuel révisé : la rigidité du paquet exact n'est plus le premier trou.
  Aucune extraction auditée ne transmet ce paquet à un même objet non trivial :
  ESS a la trace sans borne ponctuelle/mildness, KNSS a la borne et mildness
  avec la normalisation terminale opposée. Type II échappe en outre aux bornes
  naturelles Type I.
- Test discriminant : chercher un critère critique de trace compatible avec la
  normalisation maximum KNSS, puis tester s'il est transmis par la même suite
  sans supposer une borne `L³` ou une compacité terminale circulaire.
- Circularité : imposer la décroissance ou l'intégrabilité qui donne déjà le
  théorème de Liouville.
- Coût : très élevé.
- Abandon local : profil non trivial stable dans la classe exacte ou perte de
  compacité démontrée.

### F — Stabilité des constructions de non-unicité singulières

- Verrou : savoir si la construction Hou–Wang–Yang fournit une information sur
  des données lisses Clay.
- Lemme minimal : une branche instable autour du profil singulier persiste sous
  une troncature lisse à rayon `epsilon`, avec un contrôle uniforme jusqu'à un
  temps indépendant de `epsilon` et un raccord admissible.
- Échec actuel : le cutoff HWY est extérieur. Une régularisation intérieure
  peut converger en `L²`, mais une suite divergence-free bornée dans
  `L^{3,infinity}` garde un gap `L³` strict; `L^infinity` et `H^1` divergent en
  puissances. L'unicité faible–forte interdit une bifurcation pendant la durée
  classique de chaque donnée lissée.
- Test discriminant : projeter l'erreur à `t~epsilon²` sur l'eigenmode adjoint
  instable et suivre la constante jusqu'à un temps fixe; reconstruire la
  pression et séparer explicitement lissage parabolique et amplification.
- Circularité : supposer une stabilité uniforme dans une norme qui diverge.
- Coût : faible pour l'obstruction d'échelle, extrême pour reproduire la preuve
  assistée (environ 800 Go annoncés).
- Abandon local : après trois mécanismes dynamiques distincts, divergence
  nécessaire de toute constante de shadowing ou perte de séparation des
  branches; conserver alors le résultat comme barrière négative de transfert.

### G — Calcul validé conditionnel

- Verrou : convertir un profil numérique NS en objet PDE exact et admissible.
- Lemme minimal : réduction à un opérateur compact sur un domaine borné, résidu
  d'intervalle et borne rigoureuse d'inverse, avec erreurs de troncature et de
  domaine explicites.
- Échec actuel : la plupart des simulations candidates n'ont ni ensemble
  compact analytique ni passage certifié au continuum.
- Test discriminant : certifier d'abord une identité finie et une borne de queue
  sur un modèle renormalisé non singulier.
- Circularité : définir le voisinage validé avec une norme qui suppose déjà la
  régularité recherchée.
- Coût : élevé en mémoire et en génie de preuve.
- Abandon local : rayon de Newton/Kantorovich non contractant sous raffinement.

## Cycle initial : décision automatisée

Échelle : 1 faible, 5 forte. Le total n'est pas une probabilité de succès.

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| désingularisation du profil `|x|^-1` de Hou–Wang–Yang | 4 | 5 | 5 | 4 | **18** |
| commutateur de pression pour deux paquets éloignés | 4 | 3 | 4 | 5 | 16 |
| recherche d'un Liouville Type II général | 5 | 1 | 2 | 5 | 13 |

Décision : travailler sur F. Lemme actif borné : quantifier les contributions
de coquille d'une donnée homogène de degré `-1` et identifier les estimations
qui ne peuvent être uniformes sous cutoff. Expérience décisive : calcul
symbolique/exact des exposants et test multi-`epsilon`. Le résultat visé est une
barrière pour certaines méthodes de transfert, pas une obstruction dynamique
générale ni une réfutation de la prépublication.

## Cycle 0003 : décision automatisée

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| contre-profil de pression après zoom multi-échelle | 4 | 5 | 5 | 5 | **19** |
| défaut quadratique par oscillations faibles | 3 | 5 | 5 | 4 | 17 |
| extraction Liouville Type II théorème par théorème | 3 | 4 | 3 | 5 | 15 |

Décision : tester l'implication « norme physique `L²` bornée -> tension uniforme
de la pression distante après zoom ». Le critère positif minimal est la tension
de `integral |U_n|²|y|^-4`; l'expérience cherche une suite lisse qui la viole
tout en conservant une norme physique `L²` bornée.

Résultat : implication réfutée par des paquets lisses; critère pondéré positif
isolé. L'extraction ESS/GKP montre qu'une borne globale uniforme `L³` implique
ce critère avec taux `A^-3`. La queue distante n'est donc pas un verrou nouveau
dans leurs chaînes conditionnelles; le programme pivote vers le défaut
quadratique et la pression proche.

## Cycle 0004 : décision automatisée

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| défaut de trace par une solution NS oscillatoire exacte | 4 | 5 | 5 | 5 | **19** |
| défaut quadratique d'un champ statique divergence-free | 3 | 5 | 5 | 3 | 16 |
| extraction abstraite par Aubin–Lions sur cylindre fixé | 3 | 4 | 3 | 5 | 15 |

Décision : tester l'implication « énergie uniforme + convergence faible d'une
trace mobile -> compacité du produit et de la pression » dans l'équation NS
elle-même, sur `T³`, sans discrétisation.

Résultat : l'implication est réfutée par une famille de solutions globales
lisses exacte. Le défaut est cependant limité aux temps `t_N->0`; les mêmes
solutions convergent fortement à tout temps fixé positif et en volume
espace-temps. Le verrou se resserre donc sur une équicontinuité de trace
compatible avec les zooms de blow-up, et non sur la compacité d'approximation
bulk standard.

## Cycle 0005 : décision automatisée

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| seuil critique du module de trace + test NS exact | 4 | 5 | 5 | 5 | **19** |
| endpoint de trace par Aubin–Lions local | 3 | 4 | 4 | 4 | 15 |
| module temporel dans un espace de Besov critique | 5 | 2 | 3 | 5 | 15 |

Décision : calculer la loi d'échelle de
`C_t^alpha dot H_x^sigma`, dériver avec constantes le module réellement donné
par l'énergie, puis utiliser la solution exacte du cycle 0004 comme test
adverse.

Résultat : `alpha=1/4-sigma/2` est le seuil critique. L'énergie donne
`C_t^(1/4)H^-1`, alors que le seuil en `H^-1` est `3/4`; le facteur manquant est
exactement `lambda^-1`. La famille adverse respecte le module faible mais fait
diverger les modules critiques `C_t^(1/4)L²` et
`C_t^(3/4)dot H^-1` comme `N^(1/2)`.

Pivot : les cycles 0003–0005 constituent trois stratégies différentes bloquées
sur la fermeture de `GAP-COMPACT-Q` depuis l'énergie seule. Conformément au
protocole, cet axe est suspendu et le prochain lemme actif portera sur la classe
de solutions anciennes produite par un premier blow-up et le théorème de
rigidité manquant.

## Cycle 0006 : décision automatisée

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| solution ancienne parasite et porte de pression | 4 | 5 | 5 | 5 | **19** |
| audit abstrait de la préservation de mildness par zoom | 3 | 4 | 4 | 5 | 16 |
| recherche directe d'un Liouville Type II général | 5 | 1 | 2 | 5 | 13 |

Décision : tester d'abord si les propriétés locales souvent conservées par
compacité — lissité, bornitude, adaptation et trace terminale nulle — suffisent
à la rigidité ancienne.

Résultat : non. Une solution spatialement constante, accélérée par une pression
affine harmonique, satisfait toutes ces propriétés et reste non triviale. Le
lemme minimal positif est exact : dans la sous-classe `u=b(t)`, mildness ou une
pression BMO modulo constantes force `b` à être constante. Le premier trou du
Liouville n'est donc pas seulement la vorticité; c'est déjà la jauge globale de
pression.

## Cycle 0007 : décision automatisée

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| matrice exacte d'héritage ESS/GKP/KNSS/Seregin et test de non-composition | 4 | 5 | 5 | 5 | **19** |
| démonstration directe « ancienne mild bornée + trace `D'` nulle implique zéro » par unicité rétrograde | 4 | 3 | 3 | 5 | 15 |
| transfert direct des nouveaux Liouville stationnaires/auto-similaires 2026 | 3 | 3 | 4 | 3 | 13 |

Décision : construire la matrice machine et tester si le Liouville hybride
réunit des propriétés réellement transmises par une seule extraction.

Résultat : aucune des quatre chaînes n'envoie simultanément vers une ancienne
Navier–Stokes mild, globalement bornée en vitesse, non triviale et de trace
terminale nulle dans `L²_loc`. ESS fournit la trace nulle et `L∞_tL³_x`, KNSS
fournit mildness, bornitude ponctuelle et `|v(0,0)|=1`, GKP reste forward avec
une trace seulement `S'`, et le zoom Type II de Seregin devient Euler. La
couverture minimale du paquet hybride est la réunion ESS+KNSS, donc deux objets
différents : cette réunion ne constitue aucune arête de preuve.

Le lemme analytique suivant est désormais borné : auditer complètement si une
ancienne mild bornée au sens KNSS qui tend réellement vers zéro dans `D'`
quand `t` monte vers `0` est nulle par unicité rétrograde de la vorticité. Même
s'il est confirmé, il ne s'appliquera à Clay qu'après un nouveau raccord
transmettant simultanément bornitude, mildness et trace depuis une même suite.

## Cycle 0008 : décision automatisée

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| fermer le lemme ancien mild borné par lissage KNSS + rétro-unicité ESS | 3 | 5 | 5 | 5 | **18** |
| appliquer directement l'unicité finale Lei–Yang–Yuan après pont `D' -> L-infinity` | 4 | 4 | 4 | 4 | 16 |
| chercher un contre-exemple dans la classe faible/adaptée élargie | 3 | 4 | 5 | 3 | 15 |

Décision : fermer d'abord la route vorticité KNSS–ESS, plus ancienne et
indépendante du traitement direct de la pression. Lei–Yang–Yuan, dont le statut
publié a été vérifié, sert de route corroborante; trois anomalies de son arXiv
v1 interdisent de l'utiliser comme unique support avant comparaison éditeur.

Résultat positif conditionnel : si `M=sup|u|<infinity`, le redémarrage des
estimations KNSS donne

```text
||nabla^k partial_t^l u||_infinity
  <= C_(k,l) M^(k+2l+1)
```

uniformément jusqu'à `t=0`. La trace `D'` devient une trace lisse locale nulle;
la vorticité satisfait les hypothèses ESS sur chaque bande finie, donc s'annule.
Le champ est alors spatialement constant, et la mildness puis la trace
l'annulent. Le test machine rapporte zéro échec sur neuf obligations et cinq
contre-profils.

Le verrou dominant devient `GAP-HYBRID-INHERITANCE` : produire — ou réfuter
quantitativement — une trace terminale nulle pour la **même** limite
maximum-normalisée KNSS sans perdre la normalisation non triviale ni supposer
le contrôle critique recherché.

## Cycle 0009 : décision automatisée

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| auditer exactement les deux limites du zoom KNSS et la masse critique qu'elles imposent | 4 | 5 | 5 | 5 | **19** |
| poser directement une équi-intégrabilité locale `L³` comme critère de régularité | 3 | 5 | 5 | 4 | 17 |
| construire une autre normalisation censée préserver simultanément trace ESS et borne KNSS | 4 | 2 | 3 | 5 | 14 |

Décision : traiter d'abord la commutation elle-même, car elle peut falsifier
le raccord sans inventer une nouvelle extraction.

Résultat négatif décisif : les estimations de lissage KNSS sur la bande passée
commune donnent un module temporel uniforme jusqu'à `s=0`. Les deux ordres de
limite commutent en `D'_local` et leur valeur commune au temps-record conserve
`|v(0,0)|=1`; elle n'est donc pas nulle. Attention : `s=0` correspond à
`t_k`, non à `T`. Le temps physique `T` devient
`B_k=M_k²(T-t_k)>0`; le défaut de raccord terminal vient de cette extrémité
mobile et des tests

```text
Phi_k(x)=M_k² phi(M_k(x-x_k)),
```

pas d'une ambiguïté du bord dans la suite normalisée.

Corollaire quantitatif : si `G` borne les gradients normalisés au temps zéro,
tout blow-up maximum-normalisé impose

```text
integral_(B_(1/(2GM_k))(x_k)) |u(x,t_k)|³ dx
  >= pi/(48G³).
```

Une équi-intégrabilité locale uniforme de `|u|³` exclut donc cette
concentration, mais ce n'est pas un nouveau critère : elle implique la
condition à seuil fixe de Constantin 2023, déjà suffisante au prolongement.
Elle n'est pas héritée de l'énergie. Le contre-test à pression affine réalise une
non-commutation avec résidu PDE nul en perdant exactement la mildness; un
cisaillement calorique mild sur `T³` la paie par une croissance rétrograde
exponentielle.

Pivot : les cycles 0007–0009 constituent trois stratégies distinctes sur le
paquet hybride — audit de transmission, rigidité abstraite, puis audit exact
des horloges et de la commutation au temps-record. La recherche d'une trace ESS
dans le zoom maximum KNSS est suspendue. L'axe actif suivant devient le raccord
des données homogènes `-1` de Hou–Wang–Yang vers des données Clay lisses,
conformément au score priorisé.

## Cycle 0010 : décision automatisée

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| distinguer le cutoff extérieur HWY d'une régularisation intérieure Clay et tester la topologie critique | 5 | 5 | 5 | 5 | **20** |
| projeter l'erreur intérieure sur le mode adjoint instable | 5 | 2 | 3 | 5 | 15 |
| reproduire un sous-calcul CAP léger et auditer l'environnement | 3 | 3 | 5 | 3 | 14 |

Décision : fermer d'abord le faux raccord perturbatif. La source v2 utilise
`u_in=u_loc+w`, avec `w=0` près de l'origine, puis
`u_cut=-exp(t Delta)w`; son gain `R^-1/8` pour `p=4` est une petitesse de
**queue extérieure**. Il ne dépend d'aucun rayon intérieur `epsilon` et laisse
`u_loc~1/r` en zéro.

Une convolution de `u_loc` fournit bien des données compactes, lisses et
divergence-free convergeant en `L²`. Mais toute approximation localement
bornée reste à distance `L³` infinie et à distance `L^{3,infinity}` positive
du profil singulier. Plus fortement, le contre-profil tangent exact construit
une suite lisse avec

```text
||u_epsilon-u_(2epsilon)||_2 -> 0,
sup_epsilon ||u_epsilon||_{L^{3,infinity}} < infinity,
inf_epsilon ||u_epsilon-u_(2epsilon)||_3 > 0.
```

Le module universel « convergence énergétique + borne critique faible donne
compacité critique forte » est donc réfuté. L'unicité faible–forte ajoute une
porte logique : pour chaque donnée lisse fixée, les branches ne peuvent se
séparer avant une perte de la solution forte, événement qui constituerait déjà
un breakdown Clay. Le prochain lemme borné doit être dynamique et
non perturbatif : mesurer, à l'échelle `t~epsilon²`, la projection de la couche
intérieure sur l'eigenmode adjoint instable certifié, puis suivre sa séparation
jusqu'à un temps fixe avec les constantes de semigroupe et de projection.

## Cycle 0011 : décision automatisée

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| tester la sélection exacte par parité et l'horloge de couche | 5 | 5 | 5 | 5 | **20** |
| reconstruire un adjoint quantitatif depuis les artefacts publics | 4 | 3 | 5 | 4 | 16 |
| établir un shadowing non linéaire jusqu'à un temps fixe | 5 | 1 | 3 | 5 | 14 |

Décision : tester d'abord l'hypothèse de couplage. Avec
`(Ju)(x)=S u(Sx)`, `S=diag(1,1,-1)`, le profil HWY et toute régularisation
radiale sont pairs, tandis que le mode instable certifié est impair. La
projection de Leray satisfait `P(Sxi)=S P(xi)S`; l'opérateur linéarisé commute
donc avec `J`. Il en résulte `Q_-g_epsilon=0` exactement, et la solution forte
locale conserve cette parité par unicité.

La couche au temps `t=kappa epsilon²` reste pourtant d'ordre un dans les
variables de similarité. Une composante impaire artificielle
`epsilon^beta` porterait le facteur linéaire
`kappa^-a epsilon^(beta-2a)`; `a>=217/2000` rend
`beta>=217/1000` nécessaire. Cette balance n'est pas un shadowing : une couche
`O(1)` sort du régime perturbatif à temps `O(epsilon²)`, et la condition de tir
doit intégrer cutoff extérieur, non-linéarité et pression projetée.

Résultat négatif décisif : le lissage symétrique naturel n'excite pas le mode
impair certifié (`FAIL-NS-0014`). Les artefacts publics audités ne livrent pas
non plus un adjoint dynamique normalisé et certifié, ni une borne de résolvante
permettant le calcul asymétrique. Le verrou est révisé vers le certificat
minimal résolvante–simplicité–adjoint–pairing. Une perturbation asymétrique
servira seulement de test de sensibilité vers la donnée singulière : ses
variantes sont des données Clay différentes.

## Cycle 0012 : décision automatisée

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| tester l'injectivité du flot fort à temps fini face à une trace commune à `tau=-infinity` | 4 | 5 | 5 | 5 | **19** |
| construire une couche impaire divergence-free et suivre son coefficient spectral formel | 4 | 5 | 5 | 3 | 17 |
| formaliser immédiatement les projecteurs de parité finis en Lean | 3 | 3 | 5 | 3 | 14 |

Décision : isoler la porte de Cauchy avant tout nouveau calcul spectral. Pour
`w=v-u`, avec `u` forte et `v` Leray–Hopf de même donnée à un temps fini,

```text
(1/2)d||w||²_2/dt+||nabla w||²_2
  <= ||nabla u||_infinity ||w||²_2.
```

Ainsi le flot reste injectif tant que le coefficient de Grönwall est
intégrable. Une perte de cette classe à temps fini serait déjà l'événement
négatif Clay recherché; elle ne peut pas être supposée pour obtenir le raccord.

Le contre-modèle exact `b'=ab-b²` possède la famille
`b_A=aA exp(a tau)/(a+A exp(a tau))`. Toutes les branches ont la trace zéro à
`tau=-infinity`, mais l'état à tout temps fini récupère injectivement `A`. Le
contrôle adverse `x'=2sqrt(x)` montre que plusieurs trajectoires depuis une
même donnée finie réapparaissent seulement après perte de l'unicité locale.

Résultat négatif décisif : l'arête

```text
même trace critique singulière à tau=-infinity
  -> même donnée de Cauchy lisse à temps fini
```

est réfutée (`FAIL-NS-0015`). Avec les échecs indépendants de compacité
critique (`0013`) et de parité (`0014`), cela atteint le seuil de trois
stratégies. `GAP-LIMIT-ADMISSIBLE` est suspendu.

Pivot noté : géométrie locale de vorticité + triades signées `17/20`, opérateur
renormalisé compact `16/20`, noyau Fourier–Leray formel `15/20`. Le prochain
cycle sélectionne le premier axe et cherchera un contre-profil divergence-free
exact contre une déplétion géométrique quantitative.

## Cycle 0013 : cohérence locale contre strain non local

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| contre-profil périodique exact de cohérence locale et stretching signé | 4 | 5 | 5 | 5 | **19** |
| audit complet de `arXiv:2607.08866v2` | 5 | 2 | 4 | 5 | 16 |
| formalisation du noyau Fourier vorticité–strain | 3 | 4 | 5 | 3 | 15 |

Le champ

```text
u_a=(sin y+a sin x cos z,0,-a cos x sin z),  a=+-1,
```

est analytique, divergence-free et satisfait

```text
omega_a=(0,-2a sin x sin z,-cos y),
omega_a·S_a omega_a=-a cos x cos z cos²y.
```

Les deux signes sont reliés par translation, partagent énergie, enstrophie,
palinstrophie, hélicité et vorticité centrale, et ont le même module pairwise
de cohérence sur `Q_r`. Le stretching garde pourtant des signes opposés et un
module strictement positif tandis que le défaut angulaire centre–boule tend
vers zéro comme `r²`. L'arête

```text
cohérence locale de xi + quantités quadratiques
  -> signe ou petite déplétion ponctuelle sans queue
```

est réfutée (`FAIL-NS-0016`). Ce résultat est cinématique et instantané : les
critères Constantin–Fefferman et Beirão da Veiga–Berselli restent hors portée,
car ils sont uniformes en temps, high–high et intégrés.

Nouvelle arête active :

```text
géométrie sur tout le high-vorticity set
  + queue de strain contrôlée
  -> absorption intégrée / sparseness au rayon analytique.
```

Le prochain test fige les quantificateurs de la conversion géométrique de
`arXiv:2607.08866v2` et cherche un ensemble mesurable adverse avant d'auditer
les estimations PDE plus longues.

## Cycle 0014 : volume 3D vers tranche 1D

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| restriction sharp `delta -> delta^(1/3)` au même point et rayon | 3 | 5 | 5 | 5 | **18** |
| inversion logarithmique quantitative des équations (47)–(49) | 4 | 4 | 5 | 5 | **18** |
| queue dyadique du commutateur du théorème 4.1 | 5 | 2 | 4 | 5 | 16 |

Le premier candidat gagne le départage parce qu'il isole une proposition de
théorie de la mesure indépendante des estimations PDE. La formule polaire
signée et le réarrangement croissant donnent

```text
|S∩B_r|/|B_r| >= average_(nu∈S²) L(nu)^3,
```

où `L(nu)` est la densité sur la droite centrale. Il existe donc une direction
avec `L≤delta^(1/3)`. La boule concentrique sature toute la chaîne. Depuis un
majorant global `B`, le rayon sûr vérifie
`r³=B/(delta|B_1|)` et la propriété persiste pour les rayons plus grands; une
boule centrale réfute la lecture inverse.

Arête confirmée, `COMPUTATION_ONLY` :

```text
majorant global de volume du superniveau
  -> sparseness 3D au rayon construit
  -> sparseness 1D sharp au même rayon.
```

Le verrou se déplace d'une arête vers l'amont : rendre quantitatives et
uniformes les équations (47)–(49). En cas d'échec, la queue dyadique du
commutateur devient l'expérience suivante.

## Cycle 0015 : pseudo-inverse logarithmique

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| audit exact de `(47) -> (49)`, plateaux inclus | 3 | 5 | 5 | 5 | **18** |
| audit des intégrales d'O'Neil `(41) -> (47)` | 4 | 4 | 5 | 5 | **18** |
| queue dyadique du commutateur du théorème 4.1 | 5 | 2 | 4 | 5 | 16 |

Le premier candidat gagne le départage parce qu'il sépare une inversion de
fonction monotone d'une estimation PDE. Pour
`mu_f(lambda)=|{|f|>lambda}|` et
`f*(v)=inf{a≥0:mu_f(a)≤v}`, l'équivalence exacte est

```text
mu_f(lambda)>v  <=>  f*(v)>lambda.
```

L'égalité terminale `lambda=f*(mu_f(lambda))` est fausse sur les plateaux.
En utilisant tous les `v<mu_f(lambda)`, l'enveloppe (47) fournit néanmoins

```text
mu_f(lambda) ≤ A^3 /
  [lambda^3 (1+3 log(lambda/Lambda_*))^3],
Lambda_*=A V_*^(-1/3),
```

au-dessus d'un seuil explicite fixé par le cutoff uniforme `v_0`. La famille
saturante montre que la puissance trois et la constante asymptotique `1/27`
ne peuvent être améliorées avec cette seule prémisse.

Arête confirmée après correction, `COMPUTATION_ONLY` :

```text
enveloppe uniforme de réarrangée de vitesse (47)
  -> queue de distribution logarithmique quantitative (49)
  -> majorant de volume utilisable par le maillon de sparseness.
```

Le verrou actif remonte à `(40) -> (41) -> (47)`: représentation Biot–Savart,
deux intégrales d'O'Neil, reste positif de (46) et uniformité temporelle.

## Cycle 0016 : transfert O'Neil et noyau harmonique

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| rendre exact `(40) -> (41) -> (47)`, jauge et reste inclus | 3 | 5 | 5 | 5 | **18** |
| synchroniser (49) avec les constantes d'analyticité | 4 | 3 | 5 | 5 | 17 |
| queue dyadique du commutateur du théorème 4.1 | 5 | 2 | 4 | 5 | 16 |

Sous une queue (40) à seuil uniforme, un contrôle global faible
`L^{3/2}` et `u=B[omega]+h`, l'inversion de distribution donne

```text
omega*(s)<=4Omega(V/s)^(2/3)/log(eV/s),
0<s<=Vexp(-3).
```

Le coeur d'O'Neil coûte exactement `3`, une supersolution explicite coûte
`20` pour la queue intermédiaire et le contrôle global coûte `9M`. Pour
`0<v<=Vexp(-6)`,

```text
u*(v)<=Qv^(-1/3)/log(eV/v),
Q=C_K(23C_0+9M)+HV^(1/3).
```

Le maillon fonctionnel est confirmé, `COMPUTATION_ONLY`, mais deux arêtes
littérales sont réfutées :

```text
reste positif de (46) -> O(1)                    [faux]
u bornée, div u=0, omega=curl u -> u=B[omega]    [faux sans jauge].
```

Le reste vaut asymptotiquement
`9v^(-1/3)/log²(e/v)` et reste absorbable. Le mode constant est absorbable
après écriture `u=B[omega]+h`. Le verrou remonte donc à la production dynamique
uniforme de (40), avant toute nouvelle utilisation des raccords aval.

## Cycle 0017 : énergie tronquée à un niveau

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| auditer `(23) -> (40)`, absorption, support et Grönwall | 3 | 5 | 5 | 5 | **18** |
| synchroniser l'endgame `(49) -> (58)` | 4 | 3 | 5 | 5 | 17 |
| auditer toute la queue du commutateur `(8) -> (22)` | 5 | 2 | 4 | 5 | 16 |

Sous la borne dimensionnée uniforme

```text
||alpha||_(L^(3/2,infinity)(A_lambda))
 <=A/log(lambda/Lambda_*),
```

la chaîne à un niveau est valide pour une solution classique. Le seuil
d'absorption est au moins `Lambda_*exp(2C_H A S_L²/nu)`, la coercivité vaut
`X_lambda>=lambda E_lambda/(S_6²M)` et l'ODE a le coefficient
`nu lambda/(2S_6²M)`. Avec une ancre où le tronqué est nul, Chebyshev donne
`U_(2lambda)<=C lambda^-3/2 log^-3/2`.

Il n'existe aucune récurrence de niveaux : l'étiquette « De Giorgi » masque
une troncation fixe, une interpolation et un ODE linéaire. Trois portes ont
été rendues explicites : faible-`L^(3/2)` seul ne fournit pas `H¹` au
tronqué; l'estimation terminale ne s'étend pas à tout `(0,T*)`; et le facteur
dyadique `2` avant (21) est réfuté par le ratio exact `8/3`, bien que `3`
répare cette étape à petite échelle.

Arête confirmée conditionnellement, `COMPUTATION_ONLY` :

```text
commutateur uniforme (22) + régularité classique + borne critique uniforme
  -> énergie tronquée amortie
  -> distribution logarithmique (40).
```

Le verrou actif remonte à `GAP-COMMUTATOR-UNIFORMITY`, c'est-à-dire à la
preuve complète et quantitative de (8)–(22), et non à Poincaré ou Grönwall.

## Cycle 0018 : commutateur localisé

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| auditer `(8) -> (22)`, extension BMO et queues | 5 | 4 | 5 | 5 | **19** |
| synchroniser l'endgame `(49) -> (58)` | 4 | 3 | 5 | 5 | 17 |
| tester l'admissibilité PDE d'un profil multi-échelle | 4 | 3 | 4 | 5 | 16 |

Sous une borne uniforme `M` de la vorticité en faible-`L^(3/2)`, une
semi-norme directionnelle pondérée `B_xi/[1+log(R_*/r)]` et le raccord
tensoriel de Biot–Savart, la chaîne réparée donne

```text
||alpha||_(L^(3/2,infinity)(B_R(z)))
 <=C M(B_xi+1)/[1+log(R_*/R)],
0<R<=R_*/64.
```

Le champ proche utilise Jones, CRW et interpolation réelle; `I1` compense
`R^-2` par `R²`; la queue au-delà de `sqrt(RR_*)` vaut `O(MR/R_*)`; et la
queue intermédiaire est sauvée par `4^-k`. La dérive non pondérée des moyennes
croît comme le nombre d'échelles et interdit toute preuve qui la remplacerait
par `O(phi(R))` uniforme.

Arête confirmée après correction, `COMPUTATION_ONLY` :

```text
borne globale faible-L^(3/2) + direction globale bmo_phi
  -> commutateur localisé logarithmique (22)
  -> énergie tronquée uniforme (cycle 0017)
  -> queue de vorticité (40).
```

Trois réparations sont indispensables : semi-norme BMO modulo constantes,
interpolation sans réflexivité du Lorentz faible et facteur trois au dernier
anneau. La formule `min` pour la réarrangée du noyau est aussi remplacée par
sa valeur exacte. `GAP-COMMUTATOR-UNIFORMITY` est fermé conditionnellement;
`GAP-ENDGAME-SYNCHRONIZATION` devient actif sur les temps, rayons et constantes
de `(49)->(58)`.

## Cycle 0019 : temps garanti et fermeture harmonique

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| synchroniser temps, niveau, rayons et `M` dans `(49)->(58)` | 4 | 4 | 5 | 5 | **18** |
| étendre `bmo_phi` depuis le cœur actif | 5 | 3 | 5 | 5 | 18 |
| tester l'admissibilité espace-temps du profil critique | 4 | 3 | 4 | 5 | 16 |

Le choix `s=t+T_t` de la v2 est faux sous la lecture « temps maximal » : le
résidu `T*−s` peut être exactement nul. La réparation publiée est

```text
tau_t=nu/[c_1(M)U(t)²],
t+tau_t>=T* -> prolongement direct,
t+tau_t<T*  -> endgame au temps s=t+tau_t.
```

Dans la branche intérieure, la queue uniforme construit

```text
r_s=C_4/[U(s)log(e+theta U(s)/U_*)],
rho_s=nu/[c_AU(s)].
```

Le seuil `log(e+theta U(s)/U_*)>=c_A C_4/nu` garantit `r_s<=rho_s`.
La combinaison harmonique ferme les deux cas si et seulement si le même
facteur `M` vérifie `h*/2+(1-h*)M=1` et `theta M=1/2`.

Arête confirmée conditionnellement, `COMPUTATION_ONLY` :

```text
queue uniforme (49) + analyticité mild locale + dichotomie temporelle
  -> rayon sparse au même temps et sous-rayon analytique
  -> mesure harmonique
  -> U(s)<=U(t), contradiction au temps d'échappement.
```

`GAP-ENDGAME-SYNCHRONIZATION` est fermé sous (49). Le prochain verrou est
l'extension depuis le cœur actif : des directions constantes sur des cœurs
séparés peuvent encore imposer une oscillation macroscopique à l'échelle de
leur distance, malgré une cohérence parfaite sur chaque composante.

## Cycle 0020 : obstruction inter-cœurs `bmo_phi`

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| quantifier l'extension depuis plusieurs cœurs actifs | 5 | 5 | 5 | 5 | **20** |
| tester l'admissibilité PDE du profil critique ponctuel | 4 | 3 | 4 | 5 | 16 |
| construire une dynamique annulaire de déplétion | 4 | 3 | 4 | 5 | 16 |

Pour deux phases antipodales de fractions `a,b` dans un même domaine test,
toute extension vérifie la borne optimale

```text
MO_D(xi)>=4ab/(a+b).
```

La valeur de corridor `(a-b)e/(a+b)` atteint l'égalité, même sous `|xi|<=1`.
Ainsi le contraste angulaire ne suffit pas : le volume relatif de la phase
minoritaire intervient nécessairement.

Deux boules de rayon `epsilon` dans une boule de rayon `3epsilon` ont
`a=b=1/27`, donc `MO>=2/27`. Aux échelles
`3epsilon_n=exp(-n)`, toute extension coûte au moins `2n/27` dans la norme
logarithmique. Un potentiel compact lisse réalise exactement des vorticités
opposées dans les cœurs, avec divergence nulle et scaling critique
faible-`L^(3/2)`; il ne réalise pas une trajectoire singulière.

La solution nulle montre séparément que l'hypothèse n'est pas intrinsèque
sans convention aux zéros : une extension constante a semi-norme zéro, une
extension par saut a semi-norme infinie, pour la même vorticité nulle.

Arête réfutée :

```text
cohérence sur chaque composante active
  -> extension globale bmo_phi uniforme.
```

`GAP-ACTIVE-CORE-BMO` est fermé négativement sous ces seules prémisses. Une
réouverture exige un packing de phases de taille `O(phi(r))`. Le verrou actif
devient `GAP-CRITICAL-PROFILE-ADMISSIBILITY` : compatibilité simultanée du
profil critique ponctuel avec `div omega=0`, Biot–Savart, énergie finie,
direction globale log-BMO, coupures et constantes uniformes.

## Cycle 0021 : admissibilité et rigidité du profil critique

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| rigidité sous récurrence spatiale exacte et log-BMO | 5 | 5 | 5 | 5 | **20** |
| filtre solénoïdal et défaut exact des coupures | 4 | 5 | 5 | 4 | 18 |
| profil presque homogène rectifié logarithmiquement | 5 | 2 | 4 | 5 | 16 |

La Definition 2.1 de `arXiv:2607.08866v2` décrit une magnitude scalaire
`omega=Phi r^-2`; elle ne quantifie ni échelle de cœur pré-singulière, ni
limite rescalée, ni raccord vectoriel. Pour
`W=r^-2 Omega(theta)`, ce raccord exige exactement

```text
div_(S²)Omega_T=0,
integral_(S²)Omega_r dS=0.
```

Le champ explicite

```text
W=r^-2[a cross theta+(a dot theta)theta]
```

est un curl divergence-free, vérifie `|W|=r^-2` et appartient au faible-
`L^(3/2)`. Sa direction unitaire a pourtant une oscillation au moins `2/3`
sur toute boule centrée et échoue dans log-BMO.

Plus généralement, si `W(qx)=q^-2W(x)`, la direction est récurrente. La
condition `MO<=K phi(r)` avec `phi(r)->0` la force à être constante. Une
vorticité de direction constante, divergence-free et globalement faible-
`L^p`, `p<infinity`, est nécessairement nulle. La classe vectorielle
exactement récurrente et non dégénérée est donc exclue.

Les coupures ne réparent pas gratuitement ce résultat :

```text
||div(chi W)||_1=Var(chi)||Omega_r||_L1
```

est invariant d'échelle, et le correcteur sphérique conserve une taille
critique. Les doubles coupures par potentiel produisent bien des données Clay
lisses divergence-free, mais leur `L³` et la borne standard de pression
perdent un logarithme; elles ne forment pas une trajectoire de blow-up.

Après les trois portes distinctes — définition scalaire, rigidité de la
direction, défaut de coupure — `GAP-CRITICAL-PROFILE-ADMISSIBILITY` est
suspendu pour l'homogénéité exacte. Le verrou actif devient
`GAP-LOG-RECTIFIED-PROFILE`, où la direction doit rompre la récurrence avec un
taux précisément compatible avec `1/|log r|`.

## Cycle 0022 : budget de moment d'une rectification fixe

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| moment sphérique de degré un pour une direction rectifiée | 5 | 5 | 5 | 5 | **20** |
| perturbation harmonique avec borne sur `partial_s xi` | 4 | 4 | 5 | 4 | 17 |
| jet angulairement intermittent et résidu validé | 5 | 2 | 4 | 4 | 15 |

Avec `s=log(R_*/r)`, la contrainte correcte est

```text
div[r^-2 Omega(s,theta)]
=r^-3[div_(S²)Omega_T-partial_s Omega_r].
```

Le signe moins corrige la formule provisoire du pivot précédent. Pour un axe
fixe `e`, le premier harmonique `mu=e dot theta` donne le budget

```text
J=<mu Omega_r>,
J'=-<Phi(1-mu²)>-<Phi(xi-e) dot nabla_(S²)mu>.
```

Si `0<=Phi<=M`, si tout bloc logarithmique de longueur `L` porte au moins
`kappa` de moyenne `Phi^(3/2)` et si la direction se rectifie vers `e` en
moyenne pondérée, la minoration optimale par calottes force

```text
J(S+L)-J(S)<=-kappa²/(3M²L).
```

Or `|J|<=M/2`; après au plus `3M³L/kappa²` blocs, la contradiction est
inévitable. Une magnitude homogène ou log-périodique non nulle satisfait
automatiquement la non-dégénérescence de bloc. Elle ne peut donc être sauvée
par une direction `e+O(1/s)` tout en restant solénoïdale.

L'échappatoire dégénérée est explicite :

```text
W=(s²-s)e+s(e dot theta)theta,
u=(s²/2)e cross x.
```

Elle est divergence-free, vérifie `curl u=W` et a une direction à distance
`O(1/s)` de `e`, mais son facteur critique vaut `Phi~e^-2s s²`; la masse
`r^-2` disparaît. Sans borne angulaire uniforme, des calottes de mesure
`2^-3n` et amplitude `2^2n` montrent aussi que la masse `L^(3/2)` peut rester
fixe tandis que le moment transverse tend vers zéro.

La veille resserre encore la classe : Lei–Ren–Tian `2501.08976v1` exclut
conditionnellement, pour une solution faible adaptée, tout confinement
uniforme de la forte vorticité dans un double cône fixe. La rectification
uniforme espace-temps vers `+/-e` satisfait cette porte. `bmo_phi` seul ne
produit toutefois ni axe fixe, ni contrôle ponctuel de tous les grands
niveaux.

`GAP-LOG-RECTIFIED-PROFILE` est fermé négativement pour l'axe fixe sous
amplitude bornée et masse critique par bloc. Le verrou actif devient
`GAP-WANDERING-AXIS-PROFILE` : un axe `e(s)` ou plusieurs cœurs doivent
échapper à tout cône fixe, et le terme de recharge du moment, les harmoniques,
Biot–Savart, la pression et le résidu visqueux doivent être suivis ensemble.

## Cycle 0023 : budget de moment pour un axe mobile

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| budget du premier harmonique pour un axe mobile | 5 | 5 | 5 | 5 | **20** |
| test centré log-BMO pour rotation lente/persistante | 4 | 5 | 5 | 5 | 19 |
| construction par harmoniques angulaires croissants | 5 | 2 | 4 | 4 | 15 |

Pour une sélection absolument continue `e(s)∈S²`, le moment mobile vérifie

```text
J'=<[e' dot theta]Omega_r>
   -<Phi(1-(e dot theta)²)>
   -<Phi(xi-e) dot nabla_S(e dot theta)>.
```

La moyenne sphérique donne le coût optimal sans information additionnelle
`|<[e' dot theta]Omega_r>|<=M|e'|/2`. Sous `Phi<=M` et masse critique
`kappa` sur chaque bloc de longueur `L`, on obtient donc

```text
N*2kappa²/(3M²L)
 <= M+(M/2)Var(e;[S,S+NL])+D(S,S+NL).
```

Si l'erreur directionnelle `D` est sublinéaire, tout profil survivant exige
une vitesse moyenne asymptotique au moins
`4kappa²/(3M³L²)`. Les axes `|e'|=O(1/s)` sont exclus.

Le test radial sur les boules centrées sépare deux familles. Une rotation
uniforme de vitesse `alpha` a une oscillation au moins
`alpha²/[2(9+alpha²)]`, indépendante de l'échelle, donc échoue au taux
log-BMO. La rotation lente de phase `beta log(1+s)` a l'oscillation au plus
`beta/[3(1+s)]`, mais seulement une variation logarithmique, insuffisante pour
le budget solénoïdal.

La variation totale ne suffit pas à mesurer l'échappement : de petites boucles
rapides autour d'un axe fixe peuvent être longues, et retombent alors dans
l'obstruction fixe du cycle 0022. `GAP-WANDERING-AXIS-PROFILE` est fermé
négativement pour une sélection unique à variation sublinéaire et erreur
pondérée sublinéaire. Le verrou actif devient
`GAP-MULTICORE-ANGULAR-CASCADE` : construire ou exclure une occupation
angulaire multivaluée, intermittente ou à centre mobile sans axe global
admissible.

## Cycle 0024 : extraction d'un axe actif depuis log-BMO

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| extraire un axe depuis log-BMO et une fraction active minimale | 5 | 5 | 5 | 5 | **20** |
| coercivité par matrice de covariance sans axe | 5 | 3 | 5 | 4 | 17 |
| jet intermittent à amplitude non bornée | 5 | 2 | 4 | 4 | 15 |

Pour `W=r^-2 Omega(s,theta)`, `Phi=|Omega|<=M`, une masse critique au moins
`kappa` par bloc de longueur `L=-log q` donne dans chaque boule centrée la
fraction active grossière

```text
a_*=3q³kappa/M^(3/2).
```

Si une même extension `zeta`, bornée par un et unitaire sur le cœur, a une
oscillation centrée `epsilon_k<=B/(1+S_k)`, alors sa moyenne `m_k` vérifie
`|m_k|>=1-epsilon_k/a_*`. Les axes `e_k=m_k/|m_k|` sont donc définis à petite
échelle. La comparaison des boules imbriquées et l'interpolation géodésique
donnent

```text
Var(e)+integral <Phi|xi-e|> ds = O(sum epsilon_k)=O(log N).
```

Le budget mobile du cycle 0023 exige au contraire une dépense linéaire en
`N`; le profil est impossible. Un champ global unitaire rend même la masse
inutile pour normaliser la moyenne, via
`average|zeta-m|²=1-|m|²`, mais son existence sur les zéros n'est pas
intrinsèque à la vorticité.

Le falsificateur `a_n=n^-3`, `Phi_n=n²` conserve la masse `Phi^(3/2)` et fait
tendre la moyenne de l'extension par zéro vers zéro. La borne de tranche ne
peut donc être supprimée par la seule criticité faible. Le verrou actif est
`GAP-UNBOUNDED-ANGULAR-INTERMITTENCY` : produire soit une inégalité coercive
avec contrôle critique faible, soit un profil intermittent solénoïdal dont le
résidu Navier–Stokes et les queues non locales sont quantifiés.

## Cycle 0025 : train critique de blobs solénoïdaux

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| train explicite de blobs critiques + test BMO global | 5 | 5 | 5 | 5 | **20** |
| remplacer la borne d'amplitude par un moment angulaire | 5 | 3 | 5 | 5 | 18 |
| évolution Galerkin validée d'un train tronqué | 4 | 2 | 4 | 3 | 13 |

La construction canonique utilise

```text
U_n=ell_n^-1 U_0((x-x_n)/ell_n),
W_n=ell_n^-2 curl U_0((x-x_n)/ell_n),
r_n=2^-n,                         ell_n=r_n/(8n).
```

Les supports disjoints donnent exactement

```text
u∈L²,       W=curl u∈L¹ intersection L^(3/2,infinity),
div u=div W=0,
integral_blob |W|^(3/2)=constant,
r_n²|W_n(x_n)|=1024n².
```

La direction par zéro a une oscillation `O(n^-3)` sur
`B_(3r_n/2)(0)`, mais toute extension a une oscillation au moins `c_dir>0`
sur des boules internes de rayon `ell_n/2`. Le test centré est donc strictement
insuffisant pour le `bmo_phi` global. Le curl du résidu stationnaire est non
nul; le champ n'est pas une solution.

Le motif fixe est abandonné. `GAP-DIRECTIONALLY-FLAT-INTERMITTENCY` devient
actif : construire une famille de blobs dont la direction interne devient
constante en oscillation, tout en compensant l'identité
`integral curl U_n=0` par une sous-région opposée et en suivant son amplitude,
sa mesure, le faible-Lorentz et le résidu.

## Cycle 0026 : compensation conique sous faible-Lorentz

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| inégalité masse conique–Lorentz–oscillation | 5 | 5 | 5 | 5 | **20** |
| retour compact explicite à deux amplitudes | 5 | 2 | 4 | 5 | 16 |
| évolution validée d'un train tronqué | 4 | 2 | 4 | 3 | 13 |

Pour `K=||W||_(L^(3/2,infinity))` selon la quasi-norme de distribution fixée,

```text
integral_E|W|<=3K|E|^(1/3).
```

Si `integral_D W=0` et la masse `m` est dans `xi·e>=alpha`, la projection
négative pondérée porte au moins `alpha m`. Une intégration de Lorentz
pondérée et l'équilibre des parties positive/négative donnent

```text
MO_D(zeta)>=2alpha³m³/(27K³|D|).
```

Cette constante renforcée remplace le premier jet `alpha^4/27` après passe
contradictoire; elle n'est pas annoncée optimale.

La famille rationnelle `epsilon=n^-3`, amplitudes `n²/(n³-1)` et `-n²`
montre `K=1`, masse conique `1/n`, masse critique non dégénérée et
`MO=4n^-3(1-n^-3)`. L'exposant trois est sharp; une masse critique seule ne
ferme pas le compensateur.

`GAP-DIRECTIONALLY-FLAT-INTERMITTENCY` est réduit à une perte quantitative de
masse conique. `GAP-NESTED-RETURN-FLOW-CASCADE` devient actif : construire une
réalisation div–curl où le retournement est distribué sur assez de sous-échelles
pour éviter toute interface à oscillation d'ordre un. La passe adverse montre
qu'un corridor de zéros autorise un coût BMO annulaire de taille
`Theta(1/log(R/h))`, mais qu'un champ collinéaire compact divergence-free est
nécessairement nul. L'expérience suivante utilise donc un potentiel
axisymétrique `U=psi(r,z)e_theta` et teste explicitement les composantes
transverses créées par les cutoffs.

## Cycle 0027 : lift axisymétrique et porte de calotte

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| porte BMO du lift axisymétrique à aspect fixé | 5 | 5 | 5 | 5 | **20** |
| construction torique à aspect croissant | 5 | 2 | 5 | 5 | 17 |
| évolution validée du retour compact | 4 | 1 | 3 | 4 | 12 |

Le profil `U=chi(z)A_n(r)e_theta` ferme exactement les portes statiques :

```text
curl U=(-chi'A_n)e_r+chi f_n e_z,
div curl U=0,
integral r f_n dr=0,
B_n=3n^5/(8n^3+1)~(3/8)n².
```

Le faible-`L^(3/2)` est uniformément encadré, la masse forte critique du
retour ne dégénère pas et l'énergie vaut `O(n^-2)`. Mais dans une calotte où
`f_n=0`, la direction active est exactement `e_r`. Deux sous-boules donnent

```text
MO_B>=3w/[2048(R+w)],
```

soit `3/26624` dans le certificat. Cette valeur est indépendante de `n` et de
l'échelle isotrope. Le log-BMO échoue à aspect fixé et le résidu toroidal
interdit aussi une fermeture stationnaire.

La calotte équilibrée de largeur `n^-3` conserve la borne faible-Lorentz et
donne sur le domaine parent

```text
4n^-3/27<=MO_D<=n^-3.
```

La variante lisse de la passe analytique confirme `K~1`,
`m~epsilon^(1/3)`, `MO_D~epsilon` et Biot–Savart exact. Elle ferme négativement
toute amélioration du cube par les seules contraintes compactes div–curl,
mais sa norme de vitesse `L³` tend vers zéro et elle ne contrôle pas le
supremum BMO local.

`GAP-NESTED-RETURN-FLOW-CASCADE` est donc fermé pour le lift séparable à aspect
fixé. L'aspect croissant ne contrôle pas à lui seul les transitions
verticale–radiale. `GAP-NONSEPARABLE-RETURN-FLOW-MASKING` devient actif :
construire `psi_n=sum_j A_(n,j)chi_(n,j)`, puis abandonner si un niveau garde
une capacité polynomiale où `|W_r|>=|W|/4`.

## Cycle 0028 : échappatoire torique et porte de vitesse critique

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| fermeture torique mince et audit all-ball | 5 | 5 | 5 | 4 | **19** |
| no-go de rang tensoriel fini | 4 | 4 | 5 | 3 | 16 |
| évolution pseudospectrale du retour | 4 | 2 | 3 | 3 | 12 |

```text
vorticité toroïdale critique
  -- classique/géométrique --> div omega=0 et moyenne nulle
  -- dérivation interne ----> extension statique log-BMO uniforme
  -- dérivation interne ----> ||u||_3^3<=C[(h/R)+(h/R)^2]
  -- résultat négatif ------> petite donnée critique, aucun profil de blow-up
  -- obstacle R3 -----------> impulsion non nulle, queue non-Schwartz
  -- obstacle dynamique ----> diffusion unisignée, MO axiale=1 à t>0.
```

Le maillon poloidal auxiliaire est

```text
Delta_Omega>0
  --> |{|W_r|>=|W|/4}|>=((Delta_Omega)/(3K))^3
  --> Cap_2>=Delta_Omega/(3S_3^2K).
```

Aucun rang fini ne produit `Delta_Omega>0`.
`GAP-NONSEPARABLE-RETURN-FLOW-MASKING` est abaissé et
`GAP-MOMENT-CORRECTED-TOROIDAL-CASCADE` devient actif : tester une paire de
tores d'impulsions opposées avec corridors disjoints, `liminf ||u||_3>0` et
sortie explicite de la classe sans swirl.

## Cycle 0029 : correction du premier moment

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| paire signée à impulsion annulée | 5 | 5 | 5 | 5 | **20** |
| paire non parallèle à vitesse critique | 5 | 2 | 5 | 5 | 17 |
| correcteur de Hodge compact quantifié | 4 | 3 | 4 | 4 | 15 |

```text
deux tores minces +/-
  -- exact --> impulsion totale nulle
  -- exact --> axes transverses, hors axisymétrie globale
  -- conditionnel/all-ball --> log-BMO statique uniforme
  -- exact + multipolaire --> queue R3 d'ordre |x|^-4, non-Schwartz
  -- Stokes + Biot-Savart --> ||u||_3^3 ~ K^3 h/R ->0
  -- cardinal fixé --> même effondrement après moments finis
  -- ouvre --> GAP-MANY-TORUS-CRITICAL-ACCUMULATION.
```

La perte de `L^3` est locale et ne vient pas de l'impulsion. L'arête manquante
est désormais une accumulation cohérente de vitesses sous faible-Lorentz et
packing, avec `N_n->infinity`; annuler plus de moments à cardinal fixé est une
branche fermée.

## Cycle 0030 : collapse poreux et pivot directionnel compact

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| borne Biot–Savart poreuse pour `N_n->infinity` | 5 | 5 | 5 | 5 | **20** |
| vitesse compacte divergence-free construite en amont | 5 | 4 | 5 | 5 | 19 |
| simulation pseudospectrale d'un réseau cohérent | 4 | 2 | 4 | 4 | 14 |

```text
tubes homogènes localement packés
  -- classique/sourcé --> HLS I_1:L^(6/5)->L^2
  -- dérivation interne --> densité D=A(h/q)^2
  -- Hedberg + interpolation --> ||u_far||_3^3<=CK^3(h/q)^(4/3)
  -- potentiel tubulaire --> ||u_loc||_3^3<=CK^3 h/mathcal L
  -- résultat négatif --> cardinal croissant uniforme ne restaure pas L^3
  -- reste périodique --> +CK^3S, donc S->0 requis.
```

La voie compacte se décompose désormais exactement comme suit :

```text
u_j compact divergence-free
  -- Hodge exact --> BS[curl u_j]=u_j
  -- supports disjoints --> somme cubique forte L^3
  -- rayons super-géométriques --> faibles L^3 et L^(3/2) bornés
  -- réfute --> gate fondé seulement sur les normes critiques
  -- boule active remise à l'échelle --> coût directionnel |log r_j|
  -- ouvre --> GAP-COMPACT-VELOCITY-WEAK-CRITICAL-DIRECTION.
```

L'arête manquante n'est plus la compacité de la vitesse mais l'existence d'un
bloc dont le curl devient intérieurement plat à chaque échelle, tout en
conservant un budget faible-`L^3` non perturbatif et un temps d'interaction
indépendant de la plus petite échelle.

## Cycle 0031 : gate d'aspect du curl compact

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| budget Lorentz anisotrope d'un swirl compact | 5 | 5 | 5 | 5 | **20** |
| no-go universel pour toute vitesse compacte | 5 | 2 | 5 | 5 | 17 |
| évolution pseudospectrale d'un profil torique | 4 | 2 | 4 | 4 | 14 |

```text
U=V(R/r)eta((r-R)/a)chi(z/b)e_theta
  -- exact --> div U=0 et U compact
  -- exact --> W_z=V(R/r)eta'chi/a
  -- exact --> W_r=-V(R/r)etachi'/b
  -- faible-Lorentz --> K_U^3~V^3Rab
  -- faible-Lorentz --> K_W^3>=cV^3 max(R^2b^2/a,R^2a^2/b)
  -- gates critiques --> a/R,b/R>=c(kappa/K)^3
  -- boule de calotte --> MO(direction)>=c(kappa/K)^3
  -- concentration --> divergence log-BMO
  -- réfute --> grand aspect sauve le produit compact séparable
  -- ouvre --> GAP-NONSEPARABLE-COMPACT-CURL-FLATNESS.
```

La perte est un budget de dérivées, pas une queue de Biot–Savart : amincir la
transition radiale charge `W_z`, amincir la calotte charge `W_r`. Le lemme de
flux local de la passe contradictoire montre parallèlement que
`integral curl U=0` ne produit pas une boule oscillante arbitraire sans terme
de bord. Une extension universelle exigera donc un ledger non séparable des
zones de transition, et non la seule compensation globale.

## Cycle 0032 : arête universelle de support méridien

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| collapse universel par aire de section | 5 | 5 | 5 | 5 | **20** |
| ledger transition par transition à deux couches | 4 | 4 | 5 | 5 | 18 |
| optimisation numérique du BMO all-ball | 5 | 2 | 4 | 4 | 15 |

```text
F compact arbitraire, supp F subset {R/2<r<3R/2}
  -- exact --> U=(R/r)F e_theta est compact et divergence-free
  -- exact --> curl U=(R/r)nabla_perp F
  -- HLS/Lorentz sourcé --> ||F||_(6,infinity)<=C||nabla F||_(3/2,infinity)
  -- support fini --> ||F||_(3,infinity)<=S_2^(1/6)||F||_(6,infinity)
  -- poids cylindriques --> K_U<=C(S_2/R^2)^(1/6)K_W
  -- gates critiques --> S_2/R^2>=C^-6(kappa/K)^6
  -- réfute --> couches minces, signées ou décalées sauvent le gate vitesse
  -- manque --> oscillation de nabla_perp F quand S_2 comparable à R^2
  -- ouvre --> GAP-THICK-CROSS-SECTION-GRADIENT-DIRECTION.
```

La perte restante n'est plus une annulation de transitions mais la possibilité
qu'un potentiel compact sur une section épaisse possède une direction de
gradient suffisamment plate sur toutes les boules actives. Coaire et
opérateurs canceling contrôlent le champ total sans fournir cette localisation
directionnelle.

## Priorité après le cycle 0032

1. `GAP-THICK-CROSS-SECTION-GRADIENT-DIRECTION` — actif; tester si degré,
   lignes de niveau ou extrema compacts forcent une boule d'oscillation de
   `nabla_perp F/|nabla F|` lorsque `S_2/R^2>=c>0`.
2. Plateaux et compensateurs rares — passe adverse; chercher une suite qui
   concentre tout changement de direction sur un ensemble de faible capacité
   sans rendre `K_U` petit ni `K_W` grand.
3. Propagation/diffusion — encore différée jusqu'à survie simultanée des trois
   gates statiques.

## Cycle 0033 : troncature critique et compensation conique

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| troncature presque optimale puis compensation conique sur diamètre `O(R)` | 5 | 5 | 5 | 5 | **20** |
| obstruction universelle par degré sans diamètre | 5 | 2 | 4 | 5 | 16 |
| optimisation numérique directe du BMO des plateaux | 4 | 3 | 4 | 3 | 14 |

```text
superniveau presque optimal de |F|
  -- scission signée --> A={sigma F>lambda}
  -- weak HLS --> |A|^(1/6)>=c K_f/K_g
  -- coaire + isopérimétrie --> TV(G)>=c K_f^2/K_g
  -- lift cylindrique --> ||W_G||_1>=c R K_f^2/K_g
  -- curl compact --> integral W_G=0
  -- couverture finie de S^2 --> masse dans un cône orienté
  -- NS-LORENTZ-CONE-COMPENSATION --> MO_B>=c(K_u/K_w)^6
  -- diamètre axial O(R) --> |B|<=C R^3
  -- concentration --> divergence du log-BMO directionnel
  -- réfute --> plateau/retour rare dans une cellule bornée
  -- ouvre --> GAP-AXIALLY-DISPERSED-PURE-SWIRL-SELECTION.
```

La nouvelle perte est localisée : sans borne sur le diamètre axial, la boule
globale peut avoir un volume arbitrairement grand. L'expérience montre que des
cellules égales paient leur cardinal et que des amplitudes dyadiques conservent
une cellule dominante; le cas hétérogène sans dominance reste manquant.

## Priorité après le cycle 0033

1. `GAP-AXIALLY-DISPERSED-PURE-SWIRL-SELECTION` — actif; prouver une sélection
   Lorentz d'une cellule dont `K_(u,j)/K_(w,j)` reste non petit, sans supposer
   des volumes ou profils identiques.
2. Construire une matrice exacte de cellules hétérogènes `(V_j,R_j,S_j)` et
   chercher une distribution où aucun bloc ne domine mais les deux endpoints
   globaux restent non dégénérés.
3. Sortir du swirl pur seulement si cette sélection est réfutée; recalculer
   alors la projection de Leray et les composantes poloïdales.

## Cycle 0034 : sélection hétérogène et registre de fermeture

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| pigeonhole direct sur quasi-normes cellulaires | 2 | 5 | 5 | 4 | 16 |
| contre-distribution dyadique puis sélection BV | 4 | 5 | 5 | 5 | **19** |
| profils faible-endpoint curl-compatibles généraux | 5 | 2 | 4 | 5 | 16 |

```text
endpoints faibles globaux seuls
  -- contre-exemple dyadique --> aucune cellule normiquement dominante
  -- réfute --> NS-WEAK-LORENTZ-CELL-SELECTION

plateau effectif dans Q_j
  -- coaire/isopérimétrie --> integral_(Q_j)|W_j|>=cA_jv_j^(2/3)
  -- niveau global presque optimal --> lambda S^(1/3)>=cK_u
  -- faible-L^(3/2) sur union Q_j --> max_j K_(u,j)>=cK_u^2/K_w
  -- monotonie locale --> max_j K_(u,j)/K_(w,j)>=c(K_u/K_w)^2
  -- NS-BOUNDED-CROSS-SECTION-DIRECTION-GATE
       --> MO_(B_j)>=c(K_u/K_w)^12
  -- ferme --> cellules épaisses disjointes enregistrées
  -- ouvre --> GAP-DEGENERATE-CELL-REGISTER-OR-OVERLAP.
```

Arêtes manquantes :

```text
endpoints globaux
  -/-> rayon sélectionné tendant vers zéro,
queue/corridor de volume >> volume actif
  -?-> registre BV localisable,
supports de curl superposés
  -?-> contrôle après annulations,
cutoff local
  -- perte critique --> nabla chi cross U + projection de Leray non locale.
```

## Priorité après le cycle 0034

1. `GAP-DEGENERATE-CELL-REGISTER-OR-OVERLAP` — actif; construire ou exclure
   une suite où `|Q_j|/v_j->infinity` ou les supports de curl se chevauchent.
2. Tester un registre Morrey–Carleson des cols qui reste stable sous cutoff et
   projection de Leray.
3. Relier la cellule sélectionnée à une échelle pré-singulière `R_j(t)->0`,
   éventuellement sous Type I avant d'attaquer Type II.

## Cycle 0035 : bande dynamique et perte de diamètre

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| halo fixe `O(v_j)` depuis le registre total | 3 | 4 | 5 | 4 | 16 |
| fuite pure-swirl par queue axiale longue | 4 | 5 | 5 | 4 | 18 |
| bande absolue au niveau global commun | 5 | 5 | 5 | 5 | **20** |

```text
plateau témoin + registre BV global
  -/-> halo de volume O(v_j)
  -- dilatation critique --> NS-FIXED-CORE-HALO-LOCALIZATION [REFUTED]

niveau lambda presque optimal de U
  -- facteurs annulaires --> D_lambda(U) subset union E_(j,+/-)
  -- bande H_(j,+/-) --> H subset D_(lambda/6)(U)
  -- coaire R3 + isopérimétrie --> integral_H|W|>=c lambda sum V^(2/3)
  -- faible-L^(3/2) --> max K_(u,j)>=cK_u^2/K_w
  -- disjonction --> rapport local >=c(K_u/K_w)^2
  -- NS-PURE-SWIRL-COMMON-LEVEL-CELL-SELECTION [COMPUTATION_ONLY]
  -- ferme --> volume support/volume coeur dégénéré pour sélection endpoint
  -/-> boule de diamètre contrôlé ou gate directionnel.
```

Arêtes manquantes :

```text
volume contrôlé de H
  -/-> diamètre ou nombre de composantes contrôlé,
composantes dispersées
  -?-> sélection d'une boule portant rapport endpoint + compensation,
supports de curl chevauchants
  -?-> registre après annulations,
boule statique sélectionnée
  -?-> rayon dynamique tendant vers zéro.
```

Priorité : `GAP-ACTIVE-HALO-DIAMETER-OR-OVERLAP`. Le premier test porte sur
une seule cellule à gouttelettes dispersées; les chevauchements intercellules
sont différés au cycle suivant.

## Cycle 0036 — composantes actives et pont mince

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| boule Vitali depuis le volume total | 2 | 4 | 5 | 4 | 15 |
| troncature signée par composante | 5 | 5 | 5 | 5 | **20** |
| contre-profil multi-gouttes exact | 4 | 4 | 5 | 5 | 18 |

```text
niveau global lambda
  -- composantes C_alpha de {sigma F_j>lambda/4}
  -- trace nulle --> G_alpha lipschitzien, aucun curl de bord
  -- coaire R3 par composante --> sum V_alpha^(2/3)
  -- faible-Lorentz --> K_(u,alpha)>=C_I K_u^2/(648K_w)
  -- disjonction --> rapport local >=C_I(K_u/K_w)^2/648
  -- interface W_c^(1,infinity) du gate 0033
  -- diamètre de C_alpha=O(R_j) --> MO local >=c(K_u/K_w)^12
  --> NS-PURE-SWIRL-COMPONENTWISE-DROPLET-SELECTION
  -- ferme --> gouttes reliées strictement sous lambda/4
  -/-> pont restant au-dessus de lambda/4.
```

Arêtes adverses :

```text
volume+périmètre -- Frank–Lieb --> boule locale de masse c(V/P)^3
volume+périmètre -/-> fraction universelle ou diamètre de composante
m copies identiques --> rapport global m^(-1/3)
pont sous lambda/4 --> supprimé sans mesure de bord
pont au-dessus de lambda/4 -?-> coût curl critique ou grand diamètre
supports originaux chevauchants -?-> survie après annulation.
```

Priorité : `GAP-ABOVE-THRESHOLD-THIN-BRIDGE`. Tester deux gouttes distantes
reliées par un tube d'amplitude juste supérieure au cutoff et suivre
simultanément longueur, section, couches de transition et endpoints faibles.

## Cycle 0037 — persistance en amplitude et diamètre méridien

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| ledger direct du pont linéaire | 4 | 5 | 5 | 4 | 18 |
| périmètre–diamètre d'une branche persistante | 5 | 5 | 5 | 5 | **20** |
| arbre de fusion et retroncature récursive | 5 | 2 | 4 | 5 | 16 |

```text
composante M-indécomposable méridienne E_t
  -- Dayrens et al. --> P_2(E_t)>=2 diam_z(E_t^1)
  -- persistance sur (a,b) --> P_2({sigma F>t})>=2D presque partout
  -- coaire pondérée et curl exact --> integral_H|W|>=4pi RD(b-a)
  -- H subset {|U|>2a/3} + faible-L^(3/2)
       --> a(b-a)RD<=9K_uK_w/(8pi)
  --> NS-PURE-SWIRL-PERSISTENT-BRIDGE-DIAMETER [COMPUTATION_ONLY]

pont au-dessus du cutoff A
  -- coaire sous le cutoff --> A^2RD<=9K_uK_w/(2pi)
  -- AR>=kappa K_u --> D/R<=9(K_w/K_u)/(2pi kappa^2)
  -- raccord conditionnel C36/C33 --> boule directionnelle
  -- ferme --> pont de persistance relative fixe et calibrée
  -/-> calibrage local automatique depuis le niveau global
  -/-> composante basse créée par fusions sur une fenêtre évanescente.
```

Arêtes adverses :

```text
diamètre topologique d'un représentant BV : faux; employer E^1;
périmètre 3D -> diamètre : faux par tube mince;
périmètre 2D -> diamètre essentiel : classique sourcé;
merge tree discret -> arbre BV continuum : manquant sans certification;
niveau global presque optimal -> AR>=kappa K_u local : réfuté;
excès du pont eta->0 -> petit curl tronqué : possible;
excès eta->0 -> petit curl original : réfuté;
gate statique -> dynamique Clay : manquant.
```

Priorité : `GAP-BRIDGE-SCALE-CALIBRATION-OR-MERGE-TREE`. Prouver une
dichotomie critique : soit la branche sélectionnée persiste sur une fenêtre
calibrée et son diamètre est borné, soit un niveau intermédiaire la scinde en
composantes de diamètre `O(R)` tout en conservant un rapport endpoint local.

## Cycle 0038 — sélection simultanée du niveau, du diamètre et de l'endpoint

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| niveau moyen coaire + endpoint au même niveau | 5 | 5 | 5 | 5 | **20** |
| merge tree certifié et dynamique finie | 4 | 4 | 5 | 4 | 17 |
| retroncature récursive avec héritage | 4 | 3 | 4 | 4 | 15 |

```text
niveau lambda presque optimal dans une cellule
  -- volume du core + diamètre méridien --> intégrale basse du curl
  -- bande incluse dans {|U|>lambda/6} + Lorentz
       --> lambda R>=K^2/(432H)
  -- moyenne coaire sur (lambda/4,3lambda/8)
       --> somme diam_z/R<=2 239 488(H/K)^3 à un niveau régulier t
  -- même t + cores + isopérimétrie R3
       --> K_beta>=(C_I/20 736)K^2/H
       --> q_beta>=(C_I/20 736)q^2
  --> NS-PURE-SWIRL-ADAPTIVE-DIAMETER-SELECTION [COMPUTATION_ONLY]

NS-PURE-SWIRL-COMMON-LEVEL-CELL-SELECTION
  -- cellule j à rapport quadratique
  -- sélection adaptative one-cell
       --> K_beta/K_global>=c q_global^3
       --> q_beta>=c q_global^4
       --> diam_z/R_j<=C q_global^-6
  -- NS-PURE-SWIRL-LIPSCHITZ-DIRECTION-GATE
       --> oscillation locale positive pour q_global minoré.
```

Arêtes adverses :

```text
bon parent -> bon descendant à un autre niveau : réfuté;
merge tree + persistences + endpoints -> coercivité uniforme : réfuté;
barcode H0 long -> marge col-cutoff : réfuté;
coaire moyenne -> niveau et composante au même niveau : dérivation auditée;
restriction d'un curl unique -> H_beta<=H : valide;
curls intercellulaires superposés -> même monotonie : manquante;
bloc statique -> rayon pré-singulier R(t)->0 : manquante.
```

Priorité : `GAP-OVERLAPPING-CURL-CANCELLATION`. Construire deux cellules
pure-swirl à supports de vitesse identifiables mais curls superposés avec
annulation critique, ou prouver un registre de multiplicité/signature qui
conserve une cellule sélectionnable. La pression et la dynamique restent le
verrou suivant, pas une conséquence de la fermeture statique.

## Cycle 0039 — obstruction de jauge et agrégation avant sélection

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| paire lisse `Z_n,-Z_n` dans deux cellules étiquetées | 5 | 5 | 5 | 5 | **20** |
| agréger d'abord les cellules de même axe et même anneau | 3 | 5 | 5 | 4 | 17 |
| décomposition canonique par ondelettes/carré-fonction | 4 | 2 | 4 | 5 | 15 |

```text
U_(1,n)=B+Z_n, U_(2,n)=-Z_n
  -- multiplicité deux et curl-compatible
  -- volume témoin fixe 4pi^2/3
  -- ||curl Z_n||_(L^(3/2,infinity)) >= c n
  -- vitesses uniformément bornées
       --> q(U_(1,n)),q(U_(2,n))=O(n^-1)
  -- somme exacte --> q(U_(1,n)+U_(2,n))=q(B)>0
  --> NS-BOUNDED-MULTIPLICITY-OVERLAP-SELECTION [REFUTED]

même axe + même R + même anneau
  -- agréger avant valeurs absolues --> F_total=sum_j F_j
  -- NS-PURE-SWIRL-ADAPTIVE-DIAMETER-SELECTION
       --> sélection intrinsèque du champ total
  -- ferme --> overlap commun axe–anneau
  -/-> axes ou géométries locales différents.
```

Arêtes adverses :

```text
multiplicité bornée -> anti-annulation : réfuté;
divergence-free et curl-compatible -> anti-annulation : réfuté;
base ondelette du plein L^(p,infinity) : impossible par non-séparabilité;
carré-fonction du total -> récupération des labels annulés : faux;
cutoff + Leray -> localisation sans coût : faux, curl de col critique;
agrégation même axe–anneau -> cycle 0038 : identité exacte;
champ total multi-axe -> potentiel scalaire méridien unique : manquant;
localisation statique -> dynamique Clay : manquant.
```

Priorité : `GAP-MULTIAXIS-TOTAL-FIELD-LOCALIZATION`. Partir uniquement du
champ total, construire une localisation divergence-free canonique et suivre
au même endpoint le curl de col, la correction non locale, la pression et le
packing des axes. Abandonner toute sélection universelle parmi des sommants
dont l'étiquetage peut être modifié par ajout de `+Z,-Z`.

## Cycle 0040 — coupure solénoïdale intrinsèque à rapport fixé

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| correcteur de Bogovskiĭ sur une couronne fixe | 3 | 5 | 5 | 5 | **18** |
| minoration directe après projection globale de Leray | 4 | 3 | 5 | 4 | 16 |
| deux swirls à axes distincts et matrice de Gram numérique | 5 | 2 | 5 | 4 | 16 |

```text
U lisse compact divergence-free, W=curl U
  -- chi_R U --> défaut g=grad chi_R dot U, moyenne exactement nulle
  -- Bogovskii sur A_R=B_2R\Bbar_R, même opérateur interpolé
       --> b_R compact dans A_R, div b_R=g
  -- V_R=chi_R U-b_R
       --> div V_R=0, V_R=U sur B_R, supp V_R subset Bbar_2R
       --> ||curl V_R||_(3/2,infinity)
           <=3[H_out+C_chi c_A^(1/3)(1+sqrt(2)C_B)G_col]
  --> NS-SOLENOIDAL-ANNULAR-CUTOFF [COMPUTATION_ONLY]

Biot-Savart faible HLS
  --> G_col<=C_BS H_global et H_out<=H_global
  --> q(V_R)>=C_loc^-1(K_core/K_global)q(U)

couronne mince A_(R,h)
  -- test q=x_1/|x| + Poincare radiale + inf-sup fort
  --> ||B_(R,h)||>=c_pR/h
  --> NS-THIN-ANNULUS-DIVERGENCE-COST [COMPUTATION_ONLY].
```

Nature des arêtes :

```text
droite inverse sur domaine Lipschitz/John : classique sourcée;
usage NS sur couronne fixe : classique sourcé;
interpolation Lorentz et constantes 3,sqrt(2),c_A : dérivation auditée;
saturation du coût de col : calcul rationnel exact + raccord lisse;
uniformité sous homothétie fixe : valide;
uniformité quand h/R->0 : réfutée dans L^p fort;
capture K_core>=alpha K_global sans contrainte d'échelle : triviale par grande boule;
capture à une échelle pré-singulière R(t)->0 : manquante;
champ statique coupé -> solution NS non forcée localisée : manquante;
pression, diffusion et temps maximal : absents.
```

Le sous-gap `GAP-MULTIAXIS-SOLENOIDAL-CUTOFF` est fermé pour une couronne de
rapport fixé. Le verrou actif devient
`GAP-WEAK-L3-CORE-CAPTURE-AT-PRESINGULAR-SCALE` : sélectionner depuis une
solution réelle une boule dont le rayon appartient à la gamme de
concentration et capture une fraction uniforme du numérateur critique. Une
existence sans contrainte sur le rayon n'a aucune valeur, car le champ est
compact.

## Cycle 0041 — capture parabolique dans la branche Type I

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| composer la concentration Lorentz publiée avec l'inclusion locale | 3 | 5 | 5 | 5 | **18** |
| construire un contre-profil statique à rayon imposé | 4 | 4 | 5 | 3 | 16 |
| chercher un inverse faible-HLS sans hypothèse Type I | 5 | 2 | 4 | 5 | 16 |

Pour la quasi-norme `K_3(f)=sup_s s|{|f|>s}|^(1/3)`, la formule des couches
donne exactement

```text
integral_E |f|^2 <= 3 K_3(f)^2 |E|^(1/3),
C_M=sqrt(3)(4pi/3)^(1/6).
```

Ainsi une borne pointwise `sup_t K_3(u(t))<=M` implique l'hypothèse Morrey
Type I de Barker–Prange avec `A=C_M M`. Leur théorème 2 et son appendice B
donnent, au premier point singulier, pour tout `0<t<T_*`,

```text
R_M(t)=2 sqrt((T_*-t)/S_w^*(C_M M)),
K_3(u(t);B(x_*,R_M(t)))>gamma_w,
K_core/K_global>gamma_w/M.
```

Les constantes `gamma_w,S_w^*` sont propres à l'extension Lorentz et ne sont
pas identifiées aux constantes `L3`. Le certificat rationnel montre que la
constante trois est optimale et qu'une concentration absolue ne donne aucune
fraction sans borne globale.

```text
GAP-WEAK-L3-CORE-CAPTURE-AT-PRESINGULAR-SCALE
  -- fermé sous borne Type I globale pointwise
  --> GAP-TYPE-I-LOCALIZED-EVOLUTION
       dérivée de R(t), Bogovskii dépendant du temps, pression et force;
  --> GAP-TYPE-II-RELATIVE-CORE-CAPTURE
       aucune constante M uniforme, fenêtre S_w^*(M) dégénérante.
```

Priorité : calculer l'équation forcée exacte du cutoff solénoïdal mobile dans
la branche Type I. Le profil localisé est un champ test, pas une solution
Navier–Stokes non forcée; le raccord Type II reste un verrou séparé.

## Cycle 0042 — cutoff mobile et force critique annulaire

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| conjuguer le cutoff mobile et calculer sa PDE exacte | 4 | 5 | 5 | 5 | **19** |
| borner directement la force dans un espace critique mixte | 4 | 3 | 4 | 5 | 16 |
| injecter une famille Type II dans les constantes | 4 | 3 | 5 | 4 | 16 |

Pour `U=Ru(x_*+Ry,t)`, `P=R^2p`,
`Z=chi U-B(nabla chi dot U)`, `d sigma/dt=R^-2` et `kappa=-RR'`, la
localisation physique `V=R^-1Z` satisfait exactement

```text
partial_t V-Delta V+(V dot nabla)V+nabla(chi_Rp)=R^-3 F,

F=(Z dot nabla)Z-chi(U dot nabla)U+P nabla chi
  +(kappa y dot nabla chi-Delta chi)U
  -2(nabla chi dot nabla)U
  -(partial_sigma-Delta+kappa(1+y dot nabla))
      B(nabla chi dot U).
```

Pour le rayon Barker–Prange,
`kappa=2/S_w^*(C_MM)` est constant en temps mais dépend de `M`. La forme
locale a une force annulaire non solénoïdale; sa projection de Leray est
solénoïdale mais non compacte.

```text
capture Type I au rayon R(t)
  + cutoff solénoïdal statique
  + conjugaison B_R
  --> NS-MOVING-SOLENOIDAL-CUTOFF-FORCED-EQUATION
      [COMPUTATION_ONLY]

R(t)->0
  -/-> petitesse du terme (partial_t chi_R)u
      [NS-SHRINKING-MOVING-CUTOFF-SMALLNESS, REFUTED]

borne Type I faible-L3
  --> termes d'ordre zéro critiques contrôlés
  -?-> GAP-TYPE-I-MOVING-COMMUTATOR-BOUND
      [Delta,Q]U et [D,Q]U dans L1+div L^(3/2,infinity)
  -?-> GAP-TYPE-I-FORCED-RIGIDITY.
```

Priorité : choisir une formule intégrale précise de Bogovskii, intégrer par
parties dans les commutateurs et tester une famille pure-swirl haute fréquence.
Même une borne critique uniforme ne supprimerait pas la force et demanderait
ensuite un théorème de rigidité forcé distinct.

## Cycle 0043 — force complète dans un espace négatif critique

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| exploiter l'ordre pseudodifférentiel de Bogovskii dans `L1+div faible-L^(3/2)` | 4 | 4 | 5 | 5 | **18** |
| réfuter toute borne par le mode haute fréquence | 3 | 5 | 5 | 2 | 15 |
| remplacer Bogovskii par la projection de Leray globale | 3 | 4 | 5 | 3 | 15 |

On fixe une droite inverse support-preserving d'ordre `-1` sur la couronne
unité, `T=B M_(nabla chi)` et `Q=M_chi-T`. Le calcul fonctionnel donne

```text
K_kappa(U)=-[Delta,Q]U+kappa[D,Q]U
           =f_kappa(U)+div G(U),

G(U)=-2U tensor nabla chi,
f_kappa=[Delta,T]U-kappa[D,T]U
        +[(Delta chi)+kappa(y dot nabla chi)]U.
```

Comme `[Delta,T]` est d'ordre zéro et `[D,T]` d'ordre `-1`, le faible-`L3`
sur la couronne fixe donne

```text
||K_kappa(U)||_(L1+div L^(3/2,infinity))
 <=C_(A,chi,B,kappa)K_3(U).
```

En écrivant `H=div(U tensor U+P I)`, la marche négative
`B:W^(-1,4/3)_0->L^(4/3)` contrôle `QH`. La projection du défaut quadratique
reste la divergence d'un stress faible-`L^(3/2)`. Ainsi

```text
borne Type I faible-L3
  + B exact, support-preserving, Psi^(-1)
  --> NS-TYPE-I-MOVING-CUTOFF-CRITICAL-FORCE-BOUND
      ||F_sol||_X<=C[M^2+(1+|kappa|)M]
      [COMPUTATION_ONLY]

mode pure-swirl U_N
  --> ||[Delta,chi]U_N||_2=Theta(N)
  -/-> divergence de ||[Delta,chi]U_N||_X
      [budget exact indépendant de N]

borne dans X
  -?-> GAP-TYPE-I-FORCE-COMPACTNESS
  -?-> GAP-TYPE-I-FORCED-RIGIDITY.
```

Priorité : déplacer la couronne externe vers `|y|~L`, suivre les constantes
en `L` et déterminer si la force disparaît sur tout compact lorsque
`L->infinity`, avant de chercher une rigidité globale forcée.

## Cycle 0044 — fuite locale, croissance globale

La même réalisation de Bogovskii est dilatée sur
`A_L={L<|y|<2L}`. Le cutoff `Q_L` est l'identité dans `B_L` et reste borné
sur faible-`L3` avec une constante indépendante de `L`. Pour tout compact
`B_rho`, `L>=2rho` donne exactement

```text
F_L=P_L div(Z_L tensor Z_L-U tensor U) dans B_rho.
```

Le tenseur entre parenthèses est nul dans `B_L`, mais vaut
`-U tensor U` hors de `B_(2L)`. Le noyau extérieur de `P_L div` est d'ordre
quatre. Une somme sur toutes les coquilles donne

```text
||partial^alpha F_L||_(L-infinity(B_rho))
 <=C_alpha(1+C_Q²)M²L^(-3-|alpha|).
```

Le graphe adaptatif devient

```text
capture Type I dans B_1
  + Q_L=I dans B_L
  --> termes locaux de cutoff nuls sur tout compact
      [identité interne exacte]

stress extérieur faible-L3/2
  + noyau de P_L div de degré -4
  --> F_L->0 dans C^infinity_(x,loc)
      [NS-TYPE-I-OUTER-CUTOFF-LOCAL-FORCE-ESCAPE]
  --> GAP-TYPE-I-FORCE-LOCAL-ESCAPE fermé

pure-swirl U_L=L^-1U_*(dot/L), kappa!=0
  --> F_L=L^-3B_0(dot/L)+kappa L^-1A(dot/L)
  --> ||F_L||_X>=c|kappa|L²-C
      [FAIL-NS-0080]
  -/-> convergence globale dans X

fuite locale de la force
  -?-> GAP-TYPE-I-LOCAL-COMPACTNESS-TRACE
  -?-> dérenormalisation ancienne
  -?-> GAP-TYPE-I-ANCIENT-WEAK-L3-RIGIDITY
  -?-> régularité Clay.
```

La diagonale admissible doit satisfaire simultanément `L_j->infinity` et
`L_jR_j->0`. Le prochain lemme ne porte plus sur la taille instantanée de la
force, mais sur la compacité forte locale, l'inégalité d'énergie et la
non-trivialité de la trace.

## Cycle 0045 — compacité adaptée fermée, trace ouverte

```text
borne Type I faible-L3
  + pression globale de Riesz faible-L3/2
  + force F_j->0 dans C-infinity_x,loc uniformément en temps
  + solutions tronquées lisses
  --> Caccioppoli + absorption + remplissage des trous
  --> L-infinity_tL2_x,loc inter L2_tH1_x,loc
      [dérivation interne]

énergie locale + dérivée W^(-2,4/3)
  --> Simon: forte L2_loc
  --> interpolation: forte L3_loc
  --> produit fort L3/2_loc, aucun défaut de Reynolds
  --> pression proche + harmonique
  --> solution faible adaptée renormalisée non forcée
      [NS-TYPE-I-WEAK-L3-LOCAL-SUITABLE-COMPACTNESS]

forte espace-temps + C_tH^-1_loc
  -/-> trace critique non nulle
      [FAIL-NS-0081]

capture Type I non signée
  -?-> moment fixe |<Z_j(0),psi>|>=c_*
      [GAP-TYPE-I-CRITICAL-TRACE-PERSISTENCE]
  -?-> dérenormalisation ancienne non triviale
  -?-> GAP-TYPE-I-ANCIENT-WEAK-L3-RIGIDITY
  -?-> régularité Clay.
```

Les arêtes énergie–compacité–produit sont internes et revues
contradictoirement; Simon, Albritton–Barker et Barker–Seregin–Šverák sont les
ingrédients publiés voisins. L'arête de trace demeure manquante et ne peut
être remplacée par une simple semi-continuité de norme.

## Cycle 0046 — non-trivialité sans trace prescrite

```text
NS-TYPE-I-WEAK-L3-PARABOLIC-CORE-CAPTURE
  + R²=4(T_*-t)/S_w^*(C_MM)
  + d sigma/dt=R^-2
  --> R(sigma_j+s)/R_j=exp(-kappa s)
  --> capture dans B_1 pour tout/a.e. s d'une fenêtre fixe
      [quantificateur publié + horloge interne]

Q_(L_j)=I dans B_1
  + forte Z_j->Z dans L3(J x B_1)
  + K_3(f;B_1)^3<=integral_(B_1)|f|³
  --> integral_(J x B_1)|Z|³>=|J|gamma_w³
  --> Z non identiquement nulle
      [NS-TYPE-I-PERSISTENT-CAPTURE-SPACETIME-NONTRIVIALITY]

capture sur une tranche isolée
  -/-> non-trivialité espace-temps
      [FAIL-NS-0081, toujours valide]

moment signé à l'ancien endpoint
  -/-> nécessaire à la seule non-trivialité
      [FAIL-NS-0082]

limite ancienne renormalisée non triviale
  -?-> dérenormalisation standard avec classe exacte
      [GAP-TYPE-I-DERENORMALIZATION-CLASS]
  -?-> rigidité ancienne faible-L3
      [GAP-TYPE-I-ANCIENT-WEAK-L3-RIGIDITY]
  -?-> problème Clay.
```

La forte `L3` espace–temps ne conserve ni un point singulier terminal ni la
valeur de l'ancien endpoint. Ces conclusions plus fortes restent séparées.

## Cycle 0047 — conjugaison vers la classe ancienne standard

```text
NS-TYPE-I-PERSISTENT-CAPTURE-SPACETIME-NONTRIVIALITY
  + NS-TYPE-I-WEAK-L3-LOCAL-SUITABLE-COMPACTNESS
  + extraction faible-étoile globale du produit et pression de Riesz
  --> Z ancienne renormalisée suitable locale, faible-L3, non nulle

r=e^(-kappa s), tau=(1-r²)/(2kappa), x=x_0+ry
  + v=r^-1Z, q=r^-2Pi
  + dx d tau=r^5dy ds
  --> équation NS standard, divergence et énergie locale
  --> NS-TYPE-I-DERENORMALIZED-ANCIENT-LOCAL-SUITABLE
      [COMPUTATION_ONLY, double revue contradictoire]

ancienne standard suitable locale + Riesz + Linfinity_t L^(3,infinity)_x
  -/-> Leray-Hopf global          [FAIL-NS-0083: queue |x|^-1]
  -/-> mild/scindée               [trace et identité de Duhamel absentes]
  -?-> GAP-TYPE-I-ANCIENT-WEAK-L3-RIGIDITY-OR-MILDNESS
  -?-> problème Clay.
```

Les pertes de signe, jacobien, pression et énergie locale sont fermées. La
première perte restante n'est plus une puissance d'échelle : c'est la
structure globale de Cauchy à l'endpoint faible-Lorentz, puis la rigidité.

## Cycle 0048 — Duhamel faible-étoile et porte d'énergie relative

```text
NS-TYPE-I-DERENORMALIZED-ANCIENT-LOCAL-SUITABLE
  + Linfinity_t L^(3,infinity)_x
  + pression globale Riesz / projection de Leray
  --> C_w* L^(3,infinity)
      [équation testée + densité du prédual L^(3/2,1)]
  --> Duhamel dans L^(3,infinity), intégrale de Gelfand
      [Yamazaki NS-SRC-0118; Taniuchi NS-SRC-0190, lemme 7]

stress v tensor v in Linfinity_t L^(3/2,infinity)_x
  + noyau Oseen K_h in L^(k,1), 1/k=1/3+1/p
  --> B(v,v) in C_tL^p_x, 3/2<p<3
  --> w=v-S(t-t_0)v(t_0) in C_tL2_x
  --> ||w(t)||_2<=CM²(t-t_0)^(1/4)
      [NS-WEAK-L3-DUHAMEL-L2-CORRECTOR]

estimation ponctuelle endpoint h^-1
  -/-> intégrale de Bochner / petite constante temporelle
      [FAIL-NS-0084, résidu logarithmique]

C_w* L^(3,infinity) + Duhamel Gelfand
  -/-> C_tL^(3,infinity) en norme
  -/-> mildness Taniuchi/Yamazaki
  -/-> mildness bornée KNSS

w in C_tL2
  -/-> w in L2_tHdot1_x
      [nabla K_h: h^-5/4]
  -/-> inégalité d'énergie perturbée globale BSS
  -?-> GAP-TYPE-I-RELATIVE-ENERGY-GLOBALIZATION
  -?-> rigidité ancienne
  -?-> problème Clay.
```

La continuité faible-étoile et l'identité endpoint sont désormais des arêtes
fermées conditionnellement au pipeline Type I. Les pertes restantes sont la
continuité critique forte ou, sur la branche BSS sélectionnée, la dissipation
globale, les flux de cutoff et la pression à l'infini.

## Cycle 0049 — fermeture énergétique sur bande finie

```text
NS-WEAK-L3-DUHAMEL-L2-CORRECTOR
  + suitability locale de v
  + q=R_iR_j(v_iv_j) globalement
  --> inégalité locale relative pour w=v-S(t-t_0)v(t_0)
      [identité calorifique + identité croisée]

||w(h)||_2=O(h^(1/4))
  + ||V(h)||_4=O(h^(-1/8))
  --> ||V||_4^4 + ||V||_4^8||w||_2² in L1_h
      [singularité h^-1/2]

cutoff chi_R + q in L^(3/2,infinity)
  + inclusion locale L^(3/2,infinity)->L^(6/5)(A_R)
  + Sobolev sur chi_R w
  --> absorption locale + reste O(R^-1)
  --> w in L2_tHdot1_x
  --> seconde passe sans perte de signe
  --> inégalité d'énergie perturbée globale BSS
  --> NS-WEAK-L3-RELATIVE-ENERGY-GLOBALIZATION
      [COMPUTATION_ONLY]

C_tL2 inter Linfinity_tL^(3,infinity) seuls
  -/-> disparition du flux cubique à l'infini
      [FAIL-NS-0085: profil multi-annulaire, flux diagonal constant]

classe scindée BSS sur chaque bande finie
  -/-> cohérence uniforme quand t_0->-infinity
  -?-> GAP-TYPE-I-BSS-ANCIENT-RIGIDITY
  -?-> GAP-TYPE-I-BSS-TO-STRONG-MILD-CONTINUITY
  -?-> rigidité ancienne
  -?-> régularité Clay.
```

La dissipation et les flux de pression sont fermés conditionnellement sur
chaque bande finie. La première perte restante est temporelle et globale :
les constantes dépendent du temps de base et aucune unicité ne recolle les
différentes scissions anciennes.

## Cycle 0050 — cocycle exact et obstruction de quotient

```text
scissions BSS de la même solution ancienne sur toutes bandes finies
  --> g_(s,t)=g_(r,t)+S(t-r)g_(s,r)
      [identité exacte; pas d'unicité grande donnée]
  --> transition calorifique avec énergie exacte
  --> S(t-s)v(s)->0 localement quand s->-infinity

liminf_(s->-infinity)||g_(s,r)||_2<infinity
  --> v(r) in L2(R3)
      [convergence locale + monotonie des boules]

X=L^(3,infinity)_sigma, Y=L2_sigma inter X
  --> orbite dans Q_alg=X/Y
  --> orbite dans Q_H=X/closure_X(Y)
      [Q_alg non séparé; Q_H banachique]

U=(-x_2,x_1,0)/|x|², U_sharp=chi U
  --> [S(h)U]=[U] !=0 dans Q_alg et Q_H
  --> ||(I-S(h))U||_2=C_U h^(1/4)
  --> incréments de U_sharp dans C_tL2 inter L2_tHdot1
  --> limites itérées 0 contre 8pi/3
      [HEAT-COCYCLE-AUDIT-1; FAIL-NS-0086]

profils calorifiques
  -/-> solutions Navier--Stokes
      [circulation azimutale du résidu non nulle]

cocycle + énergie bande par bande + faible-L3
  -/-> uniformité L2 au passé
  -/-> annulation quotient / mildness / rigidité
  -?-> GAP-TYPE-I-BSS-ENERGY-TAIL-TIGHTNESS
  -?-> GAP-TYPE-I-ANCIENT-QUOTIENT-RIGIDITY
  -?-> problème Clay.
```

La cohérence algébrique est fermée. La première arête manquante est désormais
PDE : une tightness des queues ou une annulation basse fréquence uniforme
qui améliore le coût `h^(1/4)` le long d'une suite ancienne.

## Cycle 0051 — saturation forward et localisation infrarouge

```text
Jia--Sverak NS-SRC-0194
  + a=(-x_2,x_1,0)/|x|²
  --> solution forward auto-similaire local Leray/suitable
  --> W=U-S(1)a in L2 inter Hdot1

curl((a dot nabla)a) != 0
  --> W != 0
  --> ||u(t)-S(t)a||_2=C_*t^(1/4)
  --> dissipation relative=2t^(1/2)||nabla W||_2²
  --> NS-FORWARD-SELFSIMILAR-CORRECTOR-SATURATION
      [COMPUTATION_ONLY]

borne faible-L3 + PDE forward + suitability sur chaque bande
  -/-> borne de correcteur uniforme en longueur
      [FAIL-NS-0087; famille de bandes, pas ancienne unique]

Duhamel global de l'ancienne conditionnelle
  + v tensor v in L^(3/2,infinity)
  + noyau dyadique dans L^(6/5,1)
  --> ||Delta_jg||_2<=CM²2^(-j/2)min(1,h2^(2j))
  --> sup_s sum_(j>J)||Delta_jg||_2²<=CM^4 2^(-J)
  --> NS-WEAK-L3-ANCIENT-INFRARED-CRITERION
      [COMPUTATION_ONLY]

un a>0 fixe + une suite s_n->-infinity
  + sup_n||S(a)g_(s_n,r)||_2<infinity
  --> sup_n||g_(s_n,r)||_2<infinity
  --> v(r) in L2(R3)
      [interne; pas encore vérifié pour l'orbite ancienne]

structure d'une même orbite ancienne
  -?-> gain signé des B_j aux basses fréquences
      [GAP-TYPE-I-ANCIENT-INFRARED-STRESS-DEPLETION]
  -?-> récurrence/cohérence au passé
      [GAP-TYPE-I-SINGLE-ANCIENT-ORBIT-RECURRENCE]
  -?-> rigidité L2 ancienne / Liouville / problème Clay.
```

Arêtes publiées : existence et décroissance forward de Jia--Sverak. Arêtes
internes : non-nullité du profil, saturation exacte, noyau dyadique et
critère calorifique. Arête réfutée : uniformité forward dépendant seulement
de la norme critique. Arête manquante : toute annulation infrarouge propre à
une même trajectoire ancienne.

## Cycle 0052 — flux signé et frontière de la rigidité auto-similaire

```text
NS-WEAK-L3-ANCIENT-INFRARED-CRITERION
  + G_a(s;r)=S(a)[v(r)-S(r-s)v(s)]
  + Duhamel lissé en L2
  --> partial_s E_a(s;r)=-Phi_a(s;r)
  --> E_a(s;r)=integral_s^r Phi_a(sigma;r)dsigma
  --> NS-WEAK-L3-BASE-TIME-SIGNED-FLUX-IDENTITY
      [COMPUTATION_ONLY]

borne de Lorentz + valeurs absolues
  --> |Phi_a|<=CM^4(r-s)^(-1/2) au passé
  -/-> primitive uniformément bornée
      [FAIL-NS-0088]

incompressibilité + projection de Leray sur une triade T3
  -/-> signe/coercivité de la réception basse
      [1058 identités exactes; résidu rationnel nul]

profil backward SS exact U in W1,2_loc inter L^(3,infinity)
  --> U=0
      [Guevara--Phuc; Chae--Wolf; SOURCE_VERIFIED]

ancienne faible-L3 générale
  -/-> auto-similarité backward exacte
  -/-> DSS avec paramètre arbitraire
  -/-> récurrence faible-étoile/modulée
  -?-> GAP-TYPE-I-ANCIENT-SIGNED-BASE-FLUX-CANCELLATION
  -?-> rigidité ancienne / problème Clay.
```

L'identité de flux ne crée aucune nouvelle estimation : elle expose le
quantificateur et les corrélations à préserver. La seule arête publiée
ajoutée ferme le sous-cas auto-similaire exact; le raccord depuis le scénario
Type I vers ce sous-cas est manquant.

## Cycle 0053 — activité renormalisée persistante

```text
limite Type I renormalisée suitable
  + borne uniforme L^(3,infinity)
  + capture persistante dans B_1
  + compacité forte L3_loc des translations
  + pression globale de Riesz
  --> si D_R(s_n)->0 pour tout R sur une même suite
  --> profil stationnaire U non nul
      dans W1,2_loc inter L^(3,infinity)

profil stationnaire + kappa>0
  --> normalisation au profil backward SS
  --> U=0 [Guevara--Phuc, SOURCE_VERIFIED]
  --> contradiction
  --> NS-TYPE-I-RENORMALIZED-GENERATOR-NONVANISHING
      [COMPUTATION_ONLY]

borne faible-L3 seule
  -/-> dual (W_0^(1,3))*
      [contre-profil endpoint; FAIL-NS-0089]

récurrence exacte / extraction séparée / capture sans tightness
  -/-> sous-suite stationnaire non triviale
      [1814 assertions exactes; résidu nul]

activité locale persistante du générateur
  -?-> flux calorifique signé non compensé
      [GAP-TYPE-I-RENORMALIZED-GENERATOR-TO-SIGNED-FLUX]
  -?-> critère infrarouge / L2 / rigidité ancienne / problème Clay.
```

Les arêtes compactes et le raccord suitable sont internes; la dernière
rigidité stationnaire est publiée. L'arête nouvelle exclut seulement une
asymptotique stationnaire globale sur une sous-suite de fenêtres. Elle ne
produit aucune borne quantitative universelle et laisse possibles les
orbites récurrentes non stationnaires, DSS, apériodiques et Type II.
