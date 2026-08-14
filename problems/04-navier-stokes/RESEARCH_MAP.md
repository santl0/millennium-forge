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
- Lemme minimal : toute solution ancienne adaptée avec énergie locale uniforme,
  non-concentration de pression et normalisation critique est triviale.
- Échec actuel révisé : même « lisse + bornée + adaptée + trace terminale
  nulle » permet les solutions parasites `u=b(t)` si la pression affine n'est
  pas exclue. KNSS travaille dans la classe mild précisément pour fermer cette
  jauge. Type II échappe encore aux bornes naturelles Type I.
- Test discriminant : vérifier désormais, source par source, quelle notion de
  trace terminale, mildness et normalisation de pression survit au zoom; puis
  attaquer le premier Liouville uniquement dans cette classe exacte.
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
- Échec actuel : pour un profil `|x|^(-1)`, `||u||_3^3` est logarithmiquement
  divergent, `L^infinity` et `H^1` divergent en puissances; l'unicité
  faible–forte interdit une bifurcation pendant la durée classique de chaque
  donnée lissée.
- Test discriminant : suivre exactement les normes de la troncature et la durée
  locale garantie; vérifier si un paramètre uniforme subsiste.
- Circularité : supposer une stabilité uniforme dans une norme qui diverge.
- Coût : faible pour l'obstruction d'échelle, extrême pour reproduire la preuve
  assistée (environ 800 Go annoncés).
- Abandon local : divergence nécessaire de toute constante de stabilité connue;
  conserver alors le résultat comme barrière négative de transfert.

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
