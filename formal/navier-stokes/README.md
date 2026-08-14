# Formalisation de Navier–Stokes — audit initial

Date de coupure : **2026-08-14**. Cet inventaire distingue l'encodage d'un
énoncé, la vérification d'une implication conditionnelle, la construction d'une
solution faible et une preuve du problème Clay. Ces quatre objets ne sont pas
interchangeables.

## Verdict

À la date de coupure, cet audit n'a trouvé dans les corpus primaires examinés
**aucune preuve formelle de la régularité globale ni d'un blow-up admissible pour
le problème Clay**.

Les résultats formels réellement pertinents sont les suivants :

- le dépôt Lean `formal-conjectures` contient un encodage explicite des quatre
  alternatives Clay ; les quatre théorèmes terminaux contiennent `sorry` ;
- le projet Lean `uda-lab/leray-hopf` contient une construction annoncée et
  attestée de solutions faibles globales sur le tore et sur `ℝ³`, mais ne prouve
  ni régularité, ni unicité, ni équivalence de sa formulation faible séparée avec
  la formulation espace-temps standard ;
- le corpus Isabelle/AFP audité contient des fondations d'analyse, notamment des
  espaces `Lp`, mais aucune entrée Navier–Stokes dédiée n'a été trouvée ;
- le dépôt Coq/Rocq de Ryan Fields est un squelette conditionnel qui peut être
  accepté par le noyau tout en supposant les étapes décisives. Son type terminal
  n'est pas un théorème sur une solution de Navier–Stokes.

Par conséquent, aucun artefact cité ci-dessous ne reçoit ici le statut local
`FORMALIZED` pour la résolution Clay. Les compilations externes sont rapportées
comme telles ; elles n'ont pas été rejouées localement, car `lean`, `lake`,
`coqc`, `coqchk` et `isabelle` ne sont pas installés dans l'environnement du
laboratoire.

## Échelle de statut employée

| Libellé d'audit | Sens |
|---|---|
| `STATEMENT_ONLY` | L'énoncé est typé, mais le théorème recherché est laissé ouvert. |
| `KERNEL_CHECKED_CONDITIONAL` | Le noyau vérifie l'implication à partir de prémisses ou axiomes explicités ; il ne certifie pas ces prémisses. |
| `BUILD_ATTESTED` | Une CI ou une attestation primaire rapporte une compilation réussie pour un SHA et un environnement épinglés. |
| `SOURCE_INSPECTED_NOT_REBUILT` | Les sources ont été inspectées, mais aucun compilateur local n'était disponible. |
| `NOT_FOUND_IN_AUDITED_CORPUS` | Aucun artefact dédié n'a été trouvé dans les instantanés et catalogues indiqués ; ce n'est pas une preuve universelle d'inexistence. |

## Lean 4

### Énoncés Clay

Le fichier
[`FormalConjectures/Millenium/NavierStokes.lean`](https://github.com/google-deepmind/formal-conjectures/blob/942fb149e782a56c2719c543ab58e093f733acb4/FormalConjectures/Millenium/NavierStokes.lean)
du dépôt Google DeepMind `formal-conjectures`, instantané
[`942fb149`](https://github.com/google-deepmind/formal-conjectures/commit/942fb149e782a56c2719c543ab58e093f733acb4),
encode :

- les données initiales lisses, à divergence nulle et à décroissance rapide sur
  `ℝ³` ;
- les données et solutions 1-périodiques ;
- la viscosité strictement positive, le terme de convection, le laplacien, la
  pression, la force et l'incompressibilité ;
- les quatre alternatives (A)–(D) de l'énoncé Fefferman, y compris une force
  admissible pour les alternatives de breakdown.

La dépendance est épinglée sur Lean `v4.27.0` et mathlib
[`a3a10db0`](https://github.com/leanprover-community/mathlib4/commit/a3a10db0e9d66acbebf76c5e6a135066525ac900).
Les quatre déclarations terminales
`navier_stokes_existence_and_smoothness_R3`,
`navier_stokes_existence_and_smoothness_periodic`,
`navier_stokes_breakdown_R3` et `navier_stokes_breakdown_periodic` se terminent
par `sorry`. Statut : `STATEMENT_ONLY`.

Points à revoir avant d'adopter ce fichier comme spécification canonique du
laboratoire :

- démontrer formellement que la norme de `iteratedFDeriv` utilisée est bien
  équivalente aux bornes multi-indices de l'énoncé Clay ;
- contrôler précisément la dérivée temporelle `derivWithin` au bord `t = 0` ;
- comparer chaque quantificateur de décroissance et d'énergie à la version et
  aux errata Clay retenus par `FORMULATION_CLAY.md`.

Un encodage alternatif existe dans
[`lean-dojo/LeanMillenniumPrizeProblems`](https://github.com/lean-dojo/LeanMillenniumPrizeProblems/tree/fd5207106c8c13c40cd4eeb0acb169c2c4e58aeb/Problems/NavierStokes),
instantané [`fd520710`](https://github.com/lean-dojo/LeanMillenniumPrizeProblems/commit/fd5207106c8c13c40cd4eeb0acb169c2c4e58aeb),
sous Lean `v4.31.0` et mathlib
[`fabf563a`](https://github.com/leanprover-community/mathlib4/commit/fabf563a7c95a166b8d7b6efca11c8b4dc9d911f).
Il sépare équations, espace entier, domaine périodique et alternative globale,
mais le théorème `clay_prize_navier_stokes` contient lui aussi `sorry`.

### Existence faible de Leray–Hopf

Le projet primaire
[`uda-lab/leray-hopf`](https://github.com/uda-lab/leray-hopf) fournit le résultat
formel le plus directement pertinent trouvé par l'audit. La version
[`v0.2.1`](https://github.com/uda-lab/leray-hopf/releases/tag/v0.2.1) pointe sur
le commit
[`e704400f`](https://github.com/uda-lab/leray-hopf/commit/e704400f2fb2f26b2ee7f4372c3e1ecbbc82f3dc),
avec Lean `v4.31.0-rc2` et mathlib
[`15a89b24`](https://github.com/leanprover-community/mathlib4/commit/15a89b2468bc01f1a6230d6e49ef5efc5286e502).
L'[attestation GitHub Actions 31261178496](https://github.com/uda-lab/leray-hopf/actions/runs/31261178496)
rapporte un succès pour ce SHA. Le registre
[`Reservoir`](https://reservoir.lean-lang.org/@uda-lab/lerayHopf) confirme la
compatibilité avec l'environnement épinglé, mais rapporte des échecs lorsque le
paquet est testé sans adaptation sous Lean `v4.32.2` à `v4.33.0` : la
reproductibilité dépend donc bien du verrouillage de version.

Les quatre capstones annoncés construisent, sur tout horizon puis globalement,
une même courbe faible sur le tore unité et sur `ℝ³`, à partir d'une donnée
divergence-free de `L²` et pour `ν > 0`. Le contrat public transporte :

- une identité faible non forcée ;
- l'inégalité d'énergie ;
- la trace forte unilatérale en `t = 0` ;
- l'appartenance `H¹` presque partout et la dissipation intégrable ;
- la mesurabilité forte dans l'espace ambiant `L²`.

L'inspection de
[`docs/claims-and-scope.md`](https://github.com/uda-lab/leray-hopf/blob/e704400f2fb2f26b2ee7f4372c3e1ecbbc82f3dc/docs/claims-and-scope.md)
donne les limites exactes : tests faibles de la forme séparée `ψ(t) w(x)`, pas
de preuve de l'équivalence avec tous les tests espace-temps ; pas de champ
`u ∈ C_w([0,T];L²)` dans l'interface publique ; pas d'appartenance littérale à
un espace de Bochner `L²_t H¹_x` ; aucune régularité supérieure, aucune
unicité. Les six `sorry` résiduels sont annoncés dans un import expérimental
hors du cône des capstones.

Statut de cet audit : `BUILD_ATTESTED` et
`SOURCE_INSPECTED_NOT_REBUILT` pour le théorème Lean effectivement typé ;
**aucun raccord formel au résultat de régularité Clay**. Une revue sémantique
indépendante de l'ensemble des définitions reste requise avant toute promotion
locale.

Le site [`navier-stokes.dev`](https://navier-stokes.dev/) annonce par ailleurs
plus de 190 lemmes Lean et douze axiomes pour une réduction de type Gevrey. À
la date de l'audit, la page consultée ne liait aucun dépôt de sources ni SHA ;
la compilation et la correspondance mathématique ne sont donc pas auditables à
partir de cette seule source. Statut : information de découverte, non importable.

### Fondations mathlib utiles

Instantané inspecté : mathlib
[`618f225e`](https://github.com/leanprover-community/mathlib4/commit/618f225e1ff4a6b2790a944e01b806b7c68bdc56),
daté du 2026-08-14. Les briques directement réutilisables comprennent :

- espaces `Lp`, intégrale de Bochner, Hölder et convergence mesurée ;
- espaces de Hilbert et projections orthogonales ;
- Picard–Lindelöf et Grönwall ;
- mesure de Haar et analyse de Fourier sur `AddCircle` ;
- transformée de Fourier et Plancherel sur `L²(ℝ^d)` ;
- fonctions de Schwartz, distributions tempérées et multiplicateurs de
  Fourier ;
- espaces de Sobolev/Bessel sur `ℝ^d` comme prédicat sur les distributions
  tempérées dans
  [`Analysis/Distribution/Sobolev.lean`](https://github.com/leanprover-community/mathlib4/blob/618f225e1ff4a6b2790a944e01b806b7c68bdc56/Mathlib/Analysis/Distribution/Sobolev.lean) ;
- inégalité de Gagliardo–Nirenberg–Sobolev pour fonctions `C¹` à support
  compact dans
  [`Analysis/FunctionalSpaces/SobolevInequality.lean`](https://github.com/leanprover-community/mathlib4/blob/618f225e1ff4a6b2790a944e01b806b7c68bdc56/Mathlib/Analysis/FunctionalSpaces/SobolevInequality.lean).

Une recherche exacte des chemins du même instantané ne trouve aucun module
nommé Aubin–Lions, Rellich, Helmholtz, Leray, Stokes, Gevrey,
Littlewood–Paley, Besov ou transformée de Riesz. Cela ne démontre pas que toute
variante de chaque lemme est absente, mais identifie les raccords qui ne peuvent
pas être supposés disponibles sous une API canonique sans vérification
supplémentaire. Le dépôt `uda-lab/leray-hopf` implémente plusieurs de ces
briques localement.

## Isabelle/HOL

Les instantanés primaires inspectés sont :

- AFP développement
  [`724ecf9f`](https://github.com/isabelle-prover/mirror-afp-devel/commit/724ecf9fdfef3099915303ca81870ae37aa5ad5e) ;
- Isabelle développement
  [`83280fb8`](https://github.com/isabelle-prover/mirror-isabelle/commit/83280fb8df05e7fc78e8ce23f111483f09eb7038).

La recherche dans le catalogue AFP et dans l'arbre complet de ces instantanés
n'a trouvé ni entrée ni chemin dédié à Navier–Stokes, Leray–Hopf ou aux espaces
de Sobolev. Elle a trouvé l'entrée AFP
[`Lp`](https://www.isa-afp.org/entries/Lp.html), qui formalise notamment Hölder,
Minkowski, complétude, dualité et produits `Lp`–`Lq`, ainsi que l'intégrale de
Bochner dans `HOL-Analysis`. Ces fondations restent loin d'une formulation
faible de Navier–Stokes : dérivées faibles vectorielles, espaces solénoïdaux,
projection de Leray, compacité de type Rellich/Aubin–Lions et passage du terme
convectif ne sont pas raccordés dans un développement trouvé par cet audit.

Statut : `NOT_FOUND_IN_AUDITED_CORPUS` pour une formalisation Navier–Stokes ;
fondations `Lp` disponibles et compilées par l'AFP, mais non testées localement.

## Coq / Rocq

### Dépôt « Angular Cancellation » de Ryan Fields

Le dépôt primaire ouvert est la version Figshare archivée sous le DOI
[`10.6084/m9.figshare.31937415`](https://doi.org/10.6084/m9.figshare.31937415)
et le miroir
[`Zenodo 19743001`](https://zenodo.org/records/19743001), publié le 2026-04-04.
Il contient trois sources :

| Fichier | Empreinte primaire |
|---|---|
| `NavierStokesACL.v` | `md5:9f44631913dd7dc1dee9b32030225a0a` |
| `section5to9_revised.v` | `md5:c1f9abb309b3d9d4bbb142694fdcb47f` |
| `discharge.v` | `md5:cc7cc020e3a6b6ae858cd9f2289bc6f9` |

Le manuscrit rapporte une compilation avec Coq Platform `8.20.1`, MathComp
`2.x` et `coqchk`. Le dépôt ne fournit toutefois ni fichier de verrouillage des
dépendances ni journal de compilation indépendant. La vérification n'a pas été
rejouée ici. Une inspection statique confirme l'absence du jeton `Admitted` dans
les trois sources, mais ce fait ne réduit pas les hypothèses de section.

La passe contradictoire sur les types donne un résultat négatif net :

1. `NavierStokesACL.v` définit un réseau fini, des coefficients `u_hat` et une
   quantité scalaire `VSj`, mais suppose notamment `per_mode_res_bound`,
   `shell_energy_def`, `shell_wavenumber`, `coll_count`, `trans_count`,
   `mode_energy_le` et `shell_size_bound`. Le théorème
   `angular_cancellation_lemma` est une conséquence de ces prémisses ; il ne
   formalise pas leur validité pour toute solution de Navier–Stokes.
2. `section5to9_revised.v` ne définit aucun champ dépendant du temps, aucune
   équation de Navier–Stokes et aucune notion de solution. `Y` est une somme
   finie de scalaires. `is_global`, `is_unique`, `is_L2_stable` et `is_smooth`
   sont des `Prop` arbitraires. Les hypothèses
   `continuation_criterion : Y <= finite_bound -> is_global` et
   `parabolic_regularity : is_global -> is_smooth` impliquent directement les
   composantes homonymes de `main_global_regularity`.
3. `discharge.v` ne décharge pas le verrou principal :
   `subcritical_gronwall_proved : Y <= finite_bound` est prouvé par
   `exact: subcritical_gronwall`, où `subcritical_gronwall : Y <= finite_bound`
   est une hypothèse. `case2_subcritical` et `kp2_split` sont également supposés.
4. Les trois fichiers sont annoncés et écrits comme des modules indépendants ;
   ils ne s'importent pas entre eux. La similitude textuelle de deux énoncés ne
   constitue donc pas un raccord typé entre l'ACL, le squelette global et le
   fichier de « discharge ».

Les hypothèses de `Section` deviennent des arguments universels du théorème à
la fermeture de la section. Ainsi, `coqchk` peut parfaitement accepter le terme
de preuve sans certifier une seule de ces prémisses. Statut :
`KERNEL_CHECKED_CONDITIONAL` selon le rapport du producteur,
`SOURCE_INSPECTED_NOT_REBUILT` ici, et **réfuté comme preuve formelle du problème
Clay par inspection du type**.

Le dépôt GitHub
[`KaworuHaitani/navier-stokes-proof-2025`](https://github.com/KaworuHaitani/navier-stokes-proof-2025/tree/375b18c7a08066a04d8d0c89d7721a4b7136e0ab)
se décrit comme « fully formalized in Coq », mais l'instantané indiqué ne
contient que des fichiers PDF/TeX et aucun fichier `.v`. Il n'apporte donc pas
d'artefact Coq reproductible.

### Fondations Rocq réutilisables

Le paquet officiel
[`rocq-num-analysis 2.2.0`](https://rocq-prover.org/p/rocq-num-analysis/2.2.0)
regroupe intégration de Lebesgue et de Bochner, Lax–Milgram et éléments finis.
Le sous-paquet Lebesgue est épinglé pour Rocq `9.0`–`9.1`/Coq `8.20`,
Coquelicot `3.4` et Flocq `4.2`. Le dépôt
[`math-comp/analysis`](https://github.com/math-comp/analysis/tree/a362cf02999d950c91eb058855f318afd86d71fb)
fournit une bibliothèque d'analyse réelle sous MathComp. L'audit n'y a pas
trouvé de formalisation Navier–Stokes, de théorie Sobolev complète ni de chaîne
Galerkin–Aubin–Lions prête à l'emploi.

## Graphe des trous formels

| Maillon | État formel audité | Trou exact avant le problème Clay |
|---|---|---|
| Énoncé classique sur `ℝ³` et tore | Lean : encodé avec `sorry` | Revue quantificateur par quantificateur et raccord aux errata. |
| Calcul différentiel classique | Lean/mathlib : largement disponible | Relier les opérateurs ponctuels aux opérateurs faibles et aux classes a.e. |
| Espaces `L²`, Hilbert, Bochner | Disponibles dans les trois écosystèmes à des degrés différents | Construire les sous-espaces solénoïdaux et les opérateurs PDE avec les bonnes mesures. |
| Fourier/Plancherel sur `ℝ^d` | Lean/mathlib : disponible | Version vectorielle, tore, convolution et constantes normalisées. |
| Sobolev sur `ℝ^d` | Lean : Bessel-potentiel comme prédicat ; GNS à support compact | Espaces normés exploitables, tore, interpolation, produits et constantes suivies. |
| Projection de Leray et pression | Projet Lean `uda-lab`, pas d'API mathlib canonique trouvée | Équivalence Helmholtz, non-localité, continuité dans les espaces requis. |
| Existence Leray–Hopf | Projet Lean `uda-lab`, build épinglé attesté | Équivalence avec la formulation faible standard et revue sémantique indépendante. |
| Solution forte locale et temps maximal | Aucun développement canonique complet trouvé | Semigroupe de Stokes, bilinéaire critique, alternative de blow-up. |
| Critère critique de prolongement | Non trouvé comme chaîne formelle Navier–Stokes | Formaliser espaces critiques, pression, compacité et rétro-unicité. |
| Régularité globale ou blow-up Clay | Absent | Verrou mathématique ouvert, pas seulement dette de bibliothèque. |

## Premier noyau formalisable minimal

### Frontière de formalisation après le cycle 0008

Le lemme « ancienne mild bornée + vraie trace terminale nulle implique zéro »
n'est pas encore une bonne cible monolithique. Son noyau analytique dépend de
la sémantique exacte de la formule d'Oseen sur le domaine infini, des
estimations de lissage KNSS et d'un théorème de Carleman/unicité rétrograde
ESS; formaliser l'énoncé complet maintenant risquerait de masquer ces
dépendances dans des axiomes.

Trois sous-lemmes stables peuvent en revanche rejoindre le backlog après le
noyau Fourier :

1. la loi d'échelle
   `nabla^k partial_t^l u_lambda = lambda^(k+2l+1)` après composition;
2. le lemme abstrait « précompacité `C^m(K)` + limite unique dans `D'(K)`
   implique convergence `C^m(K)` »;
3. `div u=0`, `curl u=0` implique `Delta u=0`, suivi du Liouville harmonique
   sous bornitude.

Aucun de ces sous-lemmes n'est créé ni compilé dans ce cycle. Le statut du
claim reste donc `COMPUTATION_ONLY`, et non `FORMALIZED`.

Le premier développement propre à Millennium Forge ne doit pas tenter Leray–Hopf
ou un critère critique complet. Le noyau proposé est une **identité d'énergie
Fourier finie sur le tore**, suffisamment petite pour être revue et suffisamment
centrale pour détecter les erreurs de projection ou de pression.

Énoncé cible `NS-FORMAL-0001` : pour un ensemble fini symétrique
`K ⊂ ℤ³`, des coefficients complexes `û(k)` satisfaisant
`k · û(k) = 0` et `û(-k) = conj(û(k))`, définir

```text
B̂(u,u)(k) = -i P_k Σ_{p+q=k} (q · û(p)) û(q),
P_k z = z - k (k · z) / |k|²     pour k ≠ 0.
```

Prouver, avec toutes les sommes finies explicites :

1. `P_k` est idempotent, auto-adjoint et annule la direction `k` ;
2. le terme de pression/Leray ne travaille pas contre un mode divergence-free ;
3. après fermeture du support sous les triades nécessaires,
   `Σ_k re ⟪B̂(u,u)(k), û(k)⟫ = 0` ;
4. la donnée reconstruite est réelle et l'identité est indépendante de la base
   hélicoïdale choisie.

Ce noyau est fini-dimensionnel : il évite mesure, distributions, compacité et
passage à la limite, tout en fixant les conventions `2π`, conjugaison, produit
hermitien et projection non locale. Un échec produira un contre-exemple fini ;
un succès fournira la brique contrôlable de toute preuve d'énergie ultérieure.

Environnement proposé, non installé lors de cet audit :

```text
Lean               leanprover/lean4:v4.31.0
mathlib            v4.31.0 / fabf563a7c95a166b8d7b6efca11c8b4dc9d911f
commande ciblée    lake build MillenniumForge.NavierStokes.FourierEnergy
audit des axiomes  lake env lean formal/navier-stokes/PrintAxioms.lean
```

Le premier fichier formel devra faire échouer la CI sur `sorry`, `axiom`,
`unsafe` ou dépendance non épinglée dans son cône d'import. Aucun outil lourd
n'a été installé pour produire le présent inventaire ; la création du projet
Lean et le téléchargement du cache mathlib constituent une étape future
explicite, à exécuter seulement lorsque le noyau sera ajouté.

## Commandes de reproduction de l'audit de sources

Les liens ci-dessus sont fixés sur des commits ou versions immuables. Pour les
artefacts externes, les commandes annoncées par leurs producteurs sont :

```bash
# uda-lab/leray-hopf, au tag v0.2.1 et avec son lean-toolchain
lake exe cache get
lake build
bash scripts/agent-preflight.sh

# dépôt Fields, avec Coq Platform 8.20.1 + MathComp 2.x
coqc NavierStokesACL.v
coqc section5to9_revised.v
coqc discharge.v
coqchk -Q . "" NavierStokesACL
coqchk -Q . "" section5to9_revised
coqchk -Q . "" discharge
```

Le succès de ces commandes certifie l'acceptation des termes par le noyau dans
leur environnement ; il ne remplace jamais l'audit de la correspondance entre
le type formel et l'énoncé mathématique revendiqué.
