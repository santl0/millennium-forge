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
