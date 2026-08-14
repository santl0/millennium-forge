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
  `A^-3`. L'énergie seule ne la donne pas après zoom; la pression proche et la
  compacité forte du produit restent ouvertes.
- Test discriminant : construire des suites divergence-free qui convergent
  faiblement mais gardent un défaut non nul de `u_n tensor u_n` et de pression
  proche sous les bornes exactes disponibles.
- Circularité : absorber la queue par une norme globale critique non disponible.
- Coût : moyen.
- Abandon local : famille éloignée à énergie bornée dont le commutateur ne tend
  pas à zéro à l'échelle exigée.

### E — Solutions anciennes et profils Type II

- Verrou : théorème de Liouville dans une classe assez large pour toute limite
  de blow-up.
- Lemme minimal : toute solution ancienne adaptée avec énergie locale uniforme,
  non-concentration de pression et normalisation critique est triviale.
- Échec actuel : des classes anciennes non triviales existent dès que les
  hypothèses sont trop faibles; Type II échappe aux bornes naturelles Type I.
- Test discriminant : solveur renormalisé multi-résolution cherchant un point
  fixe ou un cycle, puis contrôle des résidus sans prétention de preuve.
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
