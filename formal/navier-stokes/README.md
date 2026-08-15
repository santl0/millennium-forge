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

Le cycle 0009 isole deux autres noyaux finis, plus proches d'une formalisation
immédiate que le théorème de compacité :

1. le changement de variable
   `<v_k,phi>=M_k² integral u(x)phi(M_k(x-x_k))dx` et la loi
   `integral|v_k|^q=M_k^(3-q)integral|u|^q` sur les boules correspondantes;
2. le lemme métrique
   `|v(0)|=1` et `||nabla v||_infinity<=G` impliquent
   `integral_(B_(1/(2G)))|v|³>=pi/(48G³)`.

Ces identités n'exigent ni distributions vectorielles générales, ni
projection de Leray, ni Carleman. Elles sont ajoutées au backlog après
`NS-FORMAL-0001`, mais aucun fichier Lean n'est encore créé : les constantes de
lissage qui fournissent `G` restent un théorème source externe.

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

## Backlog issu du cycle 0010 — cutoff homogène tangent

Avant toute formalisation de la dynamique HWY, deux identités finies et une
intégrale radiale sont candidates après `NS-FORMAL-0001` :

1. pour la matrice antisymétrique
   `B=[[0,-1,0],[1,0,0],[0,0,0]]`, prouver
   `div(Bx/|x|²)=0` sur `R³\{0}` et
   `div(f(|x|)Bx/|x|²)=0` pour tout cutoff radial lisse;
2. prouver `|nabla(Bx/|x|²)|²=2/|x|⁴`;
3. évaluer exactement les intégrales sphériques
   `C₂=8pi/3`, `C₃=3pi²/4`, puis le minorant de séparation `L³` entre deux
   cutoffs plats successifs.

Ces énoncés certifieraient seulement le contre-profil fonctionnel
`FAIL-NS-0013`. Ils ne formaliseraient ni le profil CAP Hou–Wang–Yang, ni une
solution Navier–Stokes, ni un raccord Clay. Aucun fichier Lean n'est ajouté au
cycle 0010; le noyau Fourier fini reste prioritaire parce que son environnement
est déjà spécifié et que la non-localité de la projection y est explicite.

## Backlog issu du cycle 0011 — involution et projecteurs de parité

Après le noyau Fourier énergie–Leray, le certificat fini suivant peut être
formalisé sans dépendre du profil CAP :

1. définir une involution linéaire isométrique `J` et
   `Q_plus=(I+J)/2`, `Q_minus=(I-J)/2`;
2. prouver `Q_plus²=Q_plus`, `Q_minus²=Q_minus`,
   `Q_plus Q_minus=0` et `Q_plus+Q_minus=I`;
3. si `LJ=JL`, prouver l'invariance des deux secteurs et
   `Q_minus (exp(tL)x)=0` pour `Jx=x` dans un cadre fini;
4. pour la réflexion orthogonale `S=diag(1,1,-1)`, formaliser l'identité du
   symbole de Leray `P(Sxi)=S P(xi)S` lorsque `xi` est non nul.

Cette brique certifierait la logique de `FAIL-NS-0014`, pas la commutation d'un
opérateur PDE non borné ni le mode HWY. Le fichier Python exact reste
`COMPUTATION_ONLY`; aucune preuve formelle n'est revendiquée au cycle 0011.

## Backlog issu du cycle 0012 — porte de Cauchy finie

Deux noyaux stables peuvent être formalisés après `NS-FORMAL-0001`, sans
encoder une théorie faible PDE complète :

1. pour `a,A,q>0`, définir `b=aAq/(a+Aq)` et prouver les identités finies
   `db/dtau=ab-b²` sous `dq/dtau=aq`, puis
   `A=ab/[q(a-b)]` lorsque `0<b<a`;
2. formaliser le lemme de Grönwall scalaire avec la normalisation
   `E=(1/2)||w||²` et le coefficient `2g(t)`, en séparant clairement
   l'inégalité fonctionnelle abstraite de la légitimité de la relative énergie
   pour une solution de Leray–Hopf.

Le premier noyau certifierait seulement que trace asymptotique et état fini ont
des quantificateurs différents. Le second ne certifierait Navier–Stokes
qu'après formalisation des espaces, du pairing divergence-free, de la pression
et de l'inégalité d'énergie, absents du dépôt. Aucune preuve Lean n'est donc
revendiquée au cycle 0012; la priorité formelle reste le noyau Fourier–Leray.

## Backlog issu du cycle 0013 — champ périodique vorticité–strain

Le contre-profil offre un noyau fini stable, à formaliser seulement après
`NS-FORMAL-0001` :

1. définir les six coefficients Fourier de
   `u_a=(sin y+a sin x cos z,0,-a cos x sin z)` et prouver réalité,
   moyenne nulle et `k·u_hat(k)=0`;
2. calculer `omega=curl u`, `S=sym(nabla u)` et l'identité
   `omega·S omega=-a cos x cos z cos²y`;
3. prouver les moyennes exactes énergie, enstrophie, palinstrophie et
   hélicité, puis l'équation de Poisson de
   `p=(a²/4)(cos 2x+cos 2z)`;
4. encoder les bornes élémentaires sur `Q_r` à partir de
   `|sin s|<=|s|` et `cos s>=1-s²/2`, en gardant séparées cohérence
   centre–boule et cohérence pairwise;
5. vérifier le scaling entier `U_N=N u(Nx)` et distinguer les normes moyennes
   des quantités ponctuelles.

Cette formalisation certifierait un contre-exemple cinématique à une règle de
signe locale. Elle ne formaliserait ni une trajectoire Navier–Stokes, ni les
critères de Constantin–Fefferman, ni une implication Clay. Le script exact
reste `COMPUTATION_ONLY` et les trois passes Codex ne sont pas une revue
indépendante externe.

## Backlog issu du cycle 0014 — formule polaire et réarrangement radial

Après le noyau Fourier–Leray, le lemme géométrique stable peut être isolé sans
formaliser Navier–Stokes :

1. définir la densité d'un borélien dans une boule et la densité de sa section
   sur une droite centrale;
2. formaliser la formule polaire signée avec son facteur de double comptage
   `1/2`;
3. prouver que, parmi les ensembles de longueur `m` dans `(-r,r)`, le moment
   de `|t|^(d-1)` est minimal sur l'intervalle centré;
4. en déduire le seuil `delta^(1/d)` et l'optimalité par la boule concentrique;
5. formaliser séparément le corollaire global
   `r^d≥B/(delta omega_d)` afin de figer le sens du quantificateur.

Cette cible certifierait un lemme de théorie de la mesure et ses constantes,
pas le majorant de superniveau, l'analyticité ou le théorème 7.4 de la
prépublication 2026.

## Backlog issu du cycle 0015 — pseudo-inverse et bootstrap logarithmique

Après les noyaux finis prioritaires, le lemme scalaire stable peut être
formalisé indépendamment de Navier–Stokes :

1. définir la fonction de distribution avec superniveau strict et sa
   réarrangée décroissante généralisée;
2. prouver `mu_f(lambda)>v <-> f*(v)>lambda`, sans postuler d'égalité au
   quantile terminal;
3. encoder l'enveloppe
   `f*(v)≤A v^(-1/3)/log(eV_*/v)` sur un intervalle `0<v≤v_0`;
4. formaliser le bootstrap en deux étapes qui donne d'abord
   `mu≤(A/lambda)^3`, puis réinjecte ce majorant dans le logarithme;
5. vérifier la covariance sous le changement
   `(v,V_*,lambda)->(kappa^-3v,kappa^-3V_*,kappa lambda)`.

Cette cible certifierait l'inversion `(47) -> (49)` et l'échec de l'égalité
sur les plateaux. Elle ne certifierait ni l'inégalité d'O'Neil appliquée à
Biot–Savart, ni l'enveloppe (47), ni une conclusion de régularité Clay.

## Backlog issu du cycle 0016 — opérateurs de Hardy logarithmiques

Le transfert fonctionnel offre trois noyaux formalisables après les priorités
finies existantes :

1. formaliser l'inversion de
   `mu(lambda)≤V[(Omega/lambda)/log(lambda/Omega)]^(3/2)` par le candidat
   `lambda_s=3Omega(V/s)^(2/3)/log(V/s)`;
2. prouver le coeur de Hardy avec constante trois et le supersolution
   `G(T)=20exp(T/3)/(1+T)` pour la queue intermédiaire;
3. formaliser le contre-lemme
   `R(exp(-3n))≥3n/256`, qui réfute le statut `O(1)` du reste de (46);
4. séparer abstraitement un opérateur `B` d'un noyau harmonique `h` et prouver
   l'absorption de `||h||_infinity` dans l'enveloppe aux petits volumes.

Ces cibles certifieraient des inégalités scalaires et la logique de jauge, pas
l'inégalité d'O'Neil complète sur des espaces de Lorentz, la décomposition de
Hodge sur `R³`, ni la production dynamique de (40). La formalisation du noyau
Fourier–Leray reste prioritaire avant ces lemmes exponentiels.

## Backlog issu du cycle 0017 — coercivité de support et ODE amortie

Le bloc stable peut être découpé sans formaliser Navier–Stokes :

1. définir `f_lambda=(f-lambda)_+`, sa mesure de support et l'énergie;
2. prouver depuis `f∈L^(3/2,infinity)` seulement le majorant
   `|{f>lambda}|<=(M/lambda)^(3/2)`, sans conclure `f_lambda∈H¹`;
3. sous l'hypothèse séparée `f_lambda∈Hdot¹`, combiner Hölder sur le support
   et Sobolev pour obtenir `||nabla f_lambda||²>=lambda||f_lambda||²/(S_6²M)`;
4. formaliser l'ODE
   `E'+mu lambda E<=K(lambda)` avec son terme initial, puis le cas ancré
   `E(t_0)=0`;
5. prouver Chebyshev sur le niveau `2lambda` et suivre le changement de
   logarithme dimensionné;
6. formaliser le contre-lemme `|x|^-2∈L^(3/2,infinity)` mais tronqués non
   `L²`, et le calcul dyadique `8/3>2`.

Ces cibles certifieraient le chaînage fonctionnel conditionnel et deux
contre-exemples. Elles ne certifieraient pas la chaîne Kato pour une solution
faible, le théorème de commutateur (8)–(22) ou une conclusion Clay. La
formalisation Fourier–Leray reste prioritaire.

## Backlog issu du cycle 0018 — commutateur localisé logarithmique

Le bloc stable est surtout scalaire et peut être formalisé sans encoder
immédiatement Calderón–Zygmund :

1. définir `phi_*(r)=1/[1+log(R_*/r)]` et prouver sa covariance quand `R` et
   `R_*` sont dilatés ensemble;
2. formaliser le contre-lemme dyadique au facteur deux et la borne uniforme
   au facteur trois pour `log_2(R_*/R)>=6`;
3. prouver exactement `sum_(k>=1)(k+1)4^-k=7/9`, puis la borne de la double
   somme avec incréments positifs maximaux;
4. définir la distribution de `h_a(y)=|y|^-3 1_(|y|>a)` et établir
   `h_a^*(s)=1/(a³+s/|B_1|)`, ainsi que le contre-lemme à la formule `min`;
5. séparer une semi-norme modulo constantes d'une norme BMO ancrée et encoder
   l'identité algébrique `[T,b+c]=[T,b]` pour un opérateur linéaire abstrait;
6. formaliser le ledger d'exposants `R^-2 R²=1` et
   `(RR_*)^-1R²=R/R_*`.

Ces cibles certifieraient les noyaux arithmétiques et les portes logiques du
cycle. Elles ne formaliseraient ni les théorèmes de Jones, CRW ou
John–Nirenberg, ni le noyau tensoriel de Biot–Savart, ni le fait qu'une
direction de vorticité NS satisfasse `bmo_phi`. Le noyau Fourier–Leray reste
la première cible formelle compilable; le présent bloc vient ensuite.

## Backlog issu du cycle 0019 — dichotomie et fermeture harmonique

Le noyau stable est fini et presque entièrement ordonné :

1. formaliser la partition
   `t+tau>=T_star` ou `t+tau<T_star`, avec égalité dans la branche de
   prolongement, et le contre-lemme au choix « maximal »;
2. définir pour `h∈(0,1)`
   `M=(2-h)/[2(1-h)]` et `theta=(1-h)/(2-h)`, puis prouver
   `M>1`, `theta M=1/2` et `h/2+(1-h)M=1`;
3. prouver que `H/2+(1-H)M` décroît et reste au plus un pour `H>=h`;
4. formaliser le rayon témoin cubé issu d'un majorant de volume et le
   contre-lemme montrant que la propriété n'est pas monotone vers les petits
   rayons;
5. encoder le ledger de scaling et la condition suffisante
   `log(e+theta U/U_*)>=c_A C_4/nu`;
6. séparer dans l'interface les théorèmes externes admis — analyticité,
   Solynin et principe des deux constantes — de l'algèbre certifiée.

Ces lemmes formaliseraient les portes temporelles et la combinaison affine,
pas la queue de distribution (H49), l'existence d'un temps d'échappement pour
une solution NS, ni les théorèmes de théorie du potentiel eux-mêmes. Ils
restent derrière le noyau Fourier–Leray prioritaire mais constituent un bon
module fini sans dépendance PDE lourde.

## Backlog issu du cycle 0020 — séparation de phases et zéros

Le lemme géométrique est assez stable pour une formalisation finie :

1. définir l'oscillation moyenne vectorielle sur un espace de probabilité;
2. encoder deux ensembles disjoints de masses `a,b` où `xi=+e,-e`;
3. réduire par Jensen le corridor à sa moyenne et par projection au problème
   scalaire;
4. prouver l'optimum `4ab/(a+b)` et le minimiseur
   `(a-b)e/(a+b)`, y compris `a=0` ou `b=0`;
5. déduire la borne pondérée après division par `phi(r)>0`;
6. formaliser le cas `a=b=1/27`, puis la divergence de `2n/27`;
7. séparer explicitement `omega=0` de toute opération de normalisation et
   formaliser les deux extensions du contre-test nul.

Ce module ne certifierait ni que la direction provient d'une vorticité NS,
ni l'existence d'un packing de phases le long d'une trajectoire, ni le
théorème de commutateur. Il peut néanmoins certifier entièrement l'obstruction
d'extension qui ferme `GAP-ACTIVE-CORE-BMO` sous ses prémisses actuelles.

## Backlog issu du cycle 0021 — rigidité de dilatation et flux sphérique

Deux noyaux sont stables et finis :

1. formaliser l'invariance de la moyenne et de l'oscillation sur
   `B_(q^n r)` pour une fonction vérifiant `xi(qx)=xi(x)`;
2. déduire de `MO<=K phi(q^n r)` et `phi(q^n r)->0` que `xi` est constante;
3. formaliser que `partial_e m=0` rend `m` indépendant de la coordonnée `e`;
4. montrer qu'un superniveau transverse non vide répété le long de `R` a une
   mesure infinie, incompatible avec faible-`L^p`;
5. dans un module sphérique séparé, définir `Omega_r`, `Omega_T` et prouver
   `div(r^-2 Omega)=r^-3 div_S Omega_T` hors de zéro;
6. encoder le flux distributionnel à l'origine comme coefficient de
   `delta_0`;
7. formaliser les identités algébriques du profil explicite et la minoration
   `MO>=2/3` par l'inégalité triangulaire inverse.

La partie mesure/dilatation peut être certifiée sans bibliothèque PDE lourde.
La formule de divergence sphérique et le monopôle nécessitent davantage
d'analyse distributionnelle. Aucun de ces modules ne formaliserait la
pression, Biot–Savart singulier ou une trajectoire Navier–Stokes.

## Backlog issu du cycle 0022 — budget du premier harmonique

Le noyau nouveau se sépare en une partie finie et une interface analytique :

1. sur la mesure de probabilité de `S²`, formaliser pour
   `mu=e dot theta` les identités `<|mu|>=1/2` et
   `|nabla_S mu|²=1-mu²`;
2. pour `0<=Phi<=M`, formaliser le lemme de calottes
   `<Phi(1-mu²)> >= M(a²-a³/3) >= 2<Phi>²/(3M)`,
   `a=<Phi>/M`;
3. combiner `Phi^(3/2)<=sqrt(M)Phi`, Cauchy sur un bloc de longueur `L` et
   un budget scalaire borné pour obtenir la profondeur maximale
   `3M³L/kappa²`;
4. garder comme hypothèse externe l'identité distributionnelle
   `partial_s Omega_r=div_S Omega_T`, puis formaliser séparément son test
   contre `mu`;
5. certifier par polynômes la construction dégénérée
   `W=(s²-s)e+s mu theta`, `u=(s²/2)e cross x` et les coefficients de son
   résidu visqueux.

Les étapes 2, 3 et 5 sont des cibles finies sans bibliothèque Navier–Stokes.
Elles certifieraient les constantes du claim
`NS-LOG-RECTIFIED-SOLENOIDAL-OBSTRUCTION`, pas le passage depuis une solution
Clay, la pression ou le critère du double cône. Le noyau Fourier–Leray reste
prioritaire tant qu'aucun environnement formel n'est installé et compilé.

## Backlog issu des cycles 0023–0024 — axe mobile et moyenne active

Les noyaux de mesure suivants sont assez stables pour une formalisation
indépendante de la PDE :

1. sur la sphère normalisée, prouver
   `<|a dot theta|>=|a|/2` et le coût mobile `(M/2)Var(e)`;
2. formaliser la règle du produit pour un axe absolument continu, puis garder
   l'extension `BV` comme module séparé avec traces explicites;
3. sur un espace de probabilité, si `|zeta|<=1`, `|zeta|=1` sur un ensemble de
   mesure `a` et `epsilon=E|zeta-Ezeta|`, prouver
   `|Ezeta|>=1-epsilon/a`;
4. normaliser la moyenne non nulle et établir
   `E|zeta-e|<=(1+1/a)epsilon`;
5. formaliser le rapport de volumes de deux boules imbriquées et l'incrément
   `|e_(k+1)-e_k|<=q^-3 A_k+A_(k+1)`;
6. certifier l'enveloppe dyadique
   `sum_(k<2^n)1/k<=n` à la constante de bloc près;
7. combiner ce module avec le budget scalaire du cycle 0023 sans encoder
   Biot–Savart ou Navier–Stokes.

Ce module certifierait les constantes de
`NS-BMO-ACTIVE-AXIS-EXTRACTION`. Il ne produirait ni `Phi<=M`, ni la masse
critique par bloc, ni l'existence d'une extension directionnelle globale à
partir d'une solution. Le noyau Fourier–Leray reste la première cible
compilable.

## Backlog issu du cycle 0025 — train de blobs critiques

Le noyau polynomial peut être formalisé sans théorie complète des solutions :

1. définir `P(t)=(1-t²)^4` sur `[-1,1]` et son prolongement nul `C³`;
2. certifier par dérivation symbolique
   `div U_0=0`, `curl U_0=W_0`, `div W_0=0`;
3. formaliser le scaling translation–dilatation et la disjonction des cubes
   pour `r_n=2^-n`, `ell_n=r_n/(8n)`;
4. sommer l'énergie `sum ell_n` et les volumes `sum ell_n³`;
5. formaliser la borne de distribution faible-`L^(3/2)` sans construire toute
   la bibliothèque de Lorentz;
6. isoler le lemme fini : deux sous-ensembles actifs de mesure positive et de
   composantes directionnelles séparées imposent une oscillation moyenne
   positive pour toute extension;
7. certifier que le curl du résidu stationnaire polynomial n'est pas nul.

Ces modules certifieraient la construction statique et la porte BMO, pas la
reconstruction analytique complète de Biot–Savart, une pression, une solution
de Leray–Hopf ou un blow-up Clay. Le certificat Python reste
`COMPUTATION_ONLY` tant qu'aucun assistant de preuve épinglé ne compile ces
objets.

## Backlog issu du cycle 0026 — compensation conique Lorentz

Le nouveau noyau est presque entièrement mesurable et convient à une première
formalisation finie :

1. fixer la quasi-norme faible `K=sup lambda*measure(level)^(2/3)`;
2. prouver par réarrangement puis représentation en couches
   `(integral_E f)^3<=27K^3 measure(E)` et
   `(integral fq)^3<=27K^3 integral q` pour `0<=q<=1`;
3. encoder l'annulation vectorielle, `G={xi·e>=alpha}` et le poids négatif
   `q=(-xi·e)_+`;
4. formaliser l'égalité des intégrales des parties positive et négative d'une
   fonction intégrable de moyenne nulle;
5. combiner les modules en
   `MO>=2alpha^3m^3/(27K^3|D|)` avec cas `m=0` et `K=0` séparés;
6. certifier la famille rationnelle à deux amplitudes et son rapport
   `MO/m³=4(1-n^-3)`.

Le raccord `integral curl U=0` peut être formalisé séparément pour des champs
compacts lisses. Aucun de ces modules ne certifierait une réalisation spatiale
du compensateur, sa semi-norme BMO globale ou Navier–Stokes.

## Backlog issu du cycle 0027 — calotte axisymétrique

Le noyau géométrique est assez stable pour une formalisation finie :

1. définir les coordonnées cylindriques seulement sur `r>0` et le champ
   `e_r=(x/r,y/r,0)`;
2. certifier les formules de `curl(chi A e_theta)` et de sa divergence;
3. formaliser la conservation de flux
   `A(r)=r^-1 integral_0^r s f(s)ds` et le support compact sous flux total nul;
4. montrer qu'une boule cartésienne centrée à rayon cylindrique `R` reste dans
   `R-w<r<R+w`;
5. construire les deux sous-boules de fraction `1/512` et leurs bornes de
   projection sur `e_y`;
6. réutiliser le lemme scalaire de séparation de phases pour obtenir
   `MO>=3w/[2048(R+w)]`;
7. isoler le corollaire de divergence log-BMO sous scaling isotrope;
8. certifier que la composante azimutale `-Lpsi` du résidu ne peut être un
   gradient périodique en `theta` lorsqu'elle est non nulle.

La première cible formelle doit être le lemme des deux sous-boules, indépendant
des polynômes du certificat. Elle certifierait une obstruction à aspect fixé,
pas une solution Navier–Stokes ni l'optimalité du taux `w/R`.

Une seconde cible, séparée, est la réalisation compacte du scaling cubique :
formaliser `div(curl U)=0`, l'annulation de l'intégrale d'un curl compact et
les bornes d'échelle `K~1`, `m~epsilon^(1/3)`, `MO_D~epsilon`. L'objet formel
doit encoder explicitement que `MO_D` porte sur un domaine parent fixé et non
sur le supremum BMO de toutes les boules. Le calcul `||U||_3->0` doit apparaître
comme garde-fou empêchant tout étiquetage de profil de blow-up.

## Backlog issu du cycle 0028 — excès radial et tore mince

Deux noyaux finis sont prêts à être isolés, sans formaliser Navier–Stokes :

1. pour `E={|W_r|>=|W|/4}`, encoder
   `|W_r|<|W_z|/sqrt(15)` hors de `E`;
2. combiner avec `integral_E|W|<=3K|E|^(1/3)` pour obtenir
   `|E|>=((Delta_+)/(3K))^3`;
3. ajouter Sobolev pour
   `Cap_2(E)>=Delta_+/(3S_3^2K)`, sans confondre capacité newtonienne et
   boule de densité BMO;
4. formaliser `div(f(r,z)e_theta)=0` et la moyenne azimutale nulle;
5. certifier `A=(Rh^2)^(-2/3)` et
   `||u||_3^3<=CK^3(h/R+(h/R)^2)` sous hypothèses tubulaires explicites;
6. isoler le calcul : la moyenne de `e_theta` sur une boule axiale est nulle
   et son oscillation moyenne vaut un.

La réduction all-ball log-BMO et le potentiel tubulaire restent des lemmes
analytiques à importer. Le certificat Python ne remplace pas une évolution.

## Backlog issu du cycle 0029 — impulsion, multipôle et Stokes

Le noyau conseillé est maintenant bilatéral :

1. formaliser l'invariance par translation de
   `I(W)=1/2 integral x cross W` lorsque `integral W=0`;
2. calculer `M_12=I_3`, `M_21=-I_3` pour un tore azimutal et
   `Q_(11,2)=4aI_3` pour la paire translatée signée;
3. séparer soigneusement « second moment non nul » de « coefficient extérieur
   non nul », puis certifier une composante explicite de la dérivée du dipôle;
4. encoder Stokes sur les disques méridiens actifs et Hölder sur leurs cercles;
5. intégrer le jacobien tubulaire pour obtenir
   `cK^3h/R<=||u||_3^3`;
6. combiner avec la borne supérieure du cycle 0028 et déduire l'équivalent;
7. formaliser le corollaire de cardinal fixé sous disjonction des supports.

Ce module certifierait une obstruction elliptique pour des données initiales,
pas une solution de Navier–Stokes. Une voie alternative pour le raccord
Schwartz est de partir d'un `u` compact divergence-free puis de poser
`W=curl u`, au lieu d'annuler les multipôles un à un.

## Backlog issu du cycle 0030 — potentiel poreux et stacking compact

Le noyau analytique est modulaire mais dépasse encore la bibliothèque locale :

1. formaliser la fonction de distribution d'un profil commun sur des supports
   disjoints et `K^3=kappa_b^3 A^3 mathcal L^2h^4`;
2. encoder le packing local des axes et son passage au volume actif
   `mu(B_r)<=D r^3`, `D=C A(h/q)^2` pour `r>=q`;
3. formaliser la sommation dyadique tronquée
   `I_1^far mu<=C D^(2/3)M^(1/3)` avec les cas `r_0>=q` et `r_0<q`;
4. importer HLS `I_1:L^(6/5)(R^3)->L^2(R^3)` avant de certifier l'exposant
   `(h/q)^(4/3)`;
5. isoler le reste périodique lisse `||H*W||_3^3<=CK^3S` et le mode zéro;
6. formaliser séparément le stacking compact : scaling des normes, supports
   disjoints, queue super-géométrique de la fonction de distribution et
   identité de Hodge `BS[curl u]=u`.

La première cible raisonnable est le lemme dyadique de Hedberg tronqué, qui
ne dépend ni des coordonnées tubulaires ni de Navier–Stokes. La minoration par
Stokes et la réduction all-ball restent des modules distincts. Aucun de ces
objets ne certifierait la propagation de la direction, une solution en temps
ou une résolution Clay.

## Backlog issu du cycle 0031 — budget anisotrope du curl compact

Le noyau formel recommandé ne requiert pas Navier–Stokes en temps :

1. encoder le champ cylindrique
   `U=V(R/r)eta((r-R)/a)chi(z/b)e_theta` sur un support séparé de l'axe;
2. certifier `div U=0` et l'annulation exacte de la courbure dans
   `(partial_r+1/r)U_theta`;
3. isoler deux sous-ensembles de transition de mesure `>=cRab`;
4. déduire les minorants faibles-Lorentz par une seule valeur de seuil;
5. formaliser l'algèbre
   `x^2/y>=q`, `y^2/x>=q` implique `x,y>=q`;
6. réutiliser le lemme de boule radiale du cycle 0027 pour conclure à
   l'obstruction log-BMO sous concentration.

Le futur objet doit conserver les constantes des profils dans les hypothèses.
Il certifierait seulement un no-go cinématique pour un ansatz séparable, jamais
un critère de régularité ni une solution de Navier–Stokes.

## Backlog issu du cycle 0032 — plongement de support méridien

Le noyau à formaliser est désormais indépendant des profils et se décompose en
petits modules stables :

1. représentation ponctuelle plane
   `|F|<=C I_1(|nabla F|)` pour `F` lisse compacte;
2. interpolation réelle de
   `I_1:L^(4/3)->L4` et `I_1:L^(12/7)->L12` vers
   `L^(3/2,infinity)->L^(6,infinity)`;
3. inclusion exacte sur support fini
   `||F||_(3,infinity)<=S_2^(1/6)||F||_(6,infinity)`;
4. comparaison de fonctions de distribution entre `dr dz` et
   `r dr dtheta dz` sur `R/2<r<3R/2`;
5. identité cylindrique
   `curl[(R/r)F e_theta]=(R/r)nabla_perp F`;
6. composition et vérification d'échelle de
   `K_U<=C(S_2/R^2)^(1/6)K_W`.

La première cible raisonnable est le module 3, qui dépend seulement de la
définition de faible-`Lp`. Les modules HLS/Lorentz exigent une bibliothèque
d'interpolation épinglée. Même compilé, cet objet certifierait un lemme
elliptique statique pour swirls purs séparés de l'axe, pas la dynamique Clay.

## Backlog issu du cycle 0033 — troncature et masse conique

Le théorème directionnel se factorise en modules formels réutilisables :

1. sélection d'un niveau `lambda` à facteur deux dans une quasi-norme faible;
2. scission positive/négative et règle de chaîne pour
   `G=(sigma F-lambda/2)_+`;
3. déduction
   `|A|^(1/6)>=c||F||_(3,infinity)/||nabla F||_(3/2,infinity)` par weak HLS;
4. coaire plus isopérimétrie plane donnant
   `TV(G)>=c||F||_(3,infinity)^2/||nabla F||_(3/2,infinity)`;
5. identité `||curl[(R/r)G e_theta]||_1=2pi R TV(G)` et moyenne vectorielle
   nulle du curl lipschitzien compact;
6. couverture finie de `S^2` par cônes orientés;
7. réutilisation de `NS-LORENTZ-CONE-COMPENSATION` sur la boule axiale;
8. algèbre finale du sixième exposant endpoint.

Les modules 1, 2 et 8 sont les premières cibles raisonnables. Le module 4
exige BV/coaire, tandis que 7 dépend du noyau non encore formalisé du cycle
0026. La compilation éventuelle certifierait une obstruction statique à
diamètre borné, jamais une solution de Navier–Stokes.

## Backlog issu du cycle 0034 — sélection BV finie

Le théorème de sélection se décompose en un noyau fini plus accessible que le
corollaire pure-swirl :

1. définition de la fonction de distribution d'une somme à supports disjoints;
2. sélection d'un niveau presque optimal de faible-`L3` avec défaut `eta`;
3. passage du plateau effectif à
   `K_(u,j)>=a_0A_jv_j^(1/3)`;
4. inégalité finie
   `sum v_j^(2/3)>=c lambda S/epsilon`;
5. inégalité d'intégration faible-`L^(3/2)` avec constante trois;
6. algèbre donnant `epsilon>=cK_u^2/K_w` et le rapport quadratique;
7. contre-exemple fini dyadique réfutant la version sans registre;
8. corollaire analytique par coaire/isopérimétrie et lift cylindrique;
9. composition avec le gate directionnel du cycle 0033.

Les modules 4, 6 et 7 utilisent seulement des sommes finies et des puissances
rationnelles après cubage; ils sont les premières cibles formelles. Le module
8 exige la bibliothèque BV/coaire et le module 9 hérite du noyau conique non
formalisé. Une compilation ne certifierait qu'un lemme statique conditionnel,
pas la dynamique Clay.

## Backlog issu du cycle 0035 — bande commune pure-swirl

Le nouveau théorème fini se prête à une formalisation plus courte que le
registre BV cellulaire du cycle 0034 :

1. fonction de distribution et choix `eta`-presque optimal;
2. inclusions annulaires aux niveaux `lambda`, `lambda/3`, `lambda/6`;
3. séparation des deux signes et omission des volumes nuls;
4. coaire tridimensionnelle sur la bande
   `lambda/4<sigma F<lambda/2`;
5. isopérimétrie `Per(E)>=C_I|E|^(2/3)`;
6. identité exacte du curl pure-swirl et facteur `R/r>=2/3`;
7. somme finie
   `sum V_i^(2/3)>=lambda sum V_i/(3epsilon)`;
8. intégration faible-`L^(3/2)` avec constante trois;
9. arithmétique `324=18*18`, maximum fini et rapport local;
10. contradiction `K_u>0`, `K_w=0` par compacité du potentiel.

Les modules 1–3, 7, 9 et 10 sont élémentaires. Les modules 4–5 exigent une
bibliothèque de coaire/BV/isopérimétrie sur `R3`; le module 6 exige seulement
le calcul cylindrique loin de l'axe. Formaliser ce noyau certifierait une
sélection statique pure-swirl à supports disjoints, pas la localisation dans
une boule, la direction BMO ou Navier–Stokes en temps.

## Backlog issu du cycle 0036 — troncature par composante

Le noyau nouveau se factorise en six interfaces bornées :

1. prouver que, pour une fonction lipschitzienne `h>=0`, le morceau
   `h 1_C` d'une composante de `{h>0}`, prolongé par zéro, reste lipschitzien;
2. établir la règle de chaîne presque partout sans mesure de bord;
3. formaliser la finitude des composantes de `{sigma F>lambda/4}` rencontrant
   le compact `{sigma F>=lambda/2}`;
4. sommer coaire et isopérimétrie par composante;
5. certifier l'algèbre finie
   `q_max sum q_i^2>=sum q_i^3` et `648=36*18`;
6. étendre explicitement le gate directionnel 0033 de `C_c^infinity` à
   `W_c^{1,infinity}` par ses étapes BV, sans mollification qui changerait la
   direction active.

Les modules 1, 3 et 5 sont les premières cibles formelles. Les modules 2 et 4
requièrent une bibliothèque Sobolev/BV; le module 6 dépend encore de la
compensation conique non formalisée. Même compilé, ce bloc certifierait une
sélection cinématique conditionnelle, pas une solution Navier–Stokes.

## Backlog issu du cycle 0037 — diamètre d'une branche persistante

Le noyau se factorise en étapes courtes dont plusieurs sont formalisables sans
géométrie cylindrique lourde :

1. définir diamètre axial essentiel et composante M-indécomposable plane;
2. importer ou prouver `2 diam_z(E^1)<=Per(E)`;
3. établir l'additivité du périmètre sur les composantes d'un superniveau;
4. formaliser la coaire restreinte à `a<f<b`;
5. calculer exactement le curl de `U=(R/r)F e_theta` et l'annulation du
   jacobien `2 pi r` par `R/r`;
6. prouver l'intégration faible-Lorentz
   `integral_H |W|<=3 K_w |H|^(1/3)`;
7. vérifier l'inclusion annulaire
   `H subset {|U|>2a/3}`;
8. certifier l'algèbre finale `a(b-a)RD<=9 K_uK_w/(8 pi)` et le corollaire
   rationnel `A^2RD<=(3/2)K_uK_w`;
9. distinguer formellement une branche haute persistante d'une composante
   basse créée par fusion.

Les modules 6–8 sont les premières cibles Lean réalistes. Les modules 1–4
requièrent une bibliothèque BV/coaire suffisamment expressive. Une
compilation certifierait une obstruction cinématique pure-swirl, pas une
solution, un blow-up ou un critère de régularité Navier–Stokes.

## Backlog issu du cycle 0038 — sélection adaptative du diamètre

Le noyau nouveau évite toute formalisation d'un merge tree. Il se factorise
en dix interfaces :

1. choix `1/2`-presque optimal d'un niveau faible-`L3`;
2. comparaison volume de révolution–aire–diamètre dans l'anneau;
3. coaire pondérée et borne Lorentz donnant `lambda R>=K^2/(432H)`;
4. moyenne sur `(lambda/4,3lambda/8)` et sélection d'un niveau régulier;
5. algèbre rationnelle `12*432^2=2 239 488`;
6. finitude des composantes actives rencontrant un core compact séparé;
7. inégalité finie `max x_i sum x_i^2>=sum x_i^3`;
8. troncature d'une composante à trace nulle et domination pointwise du curl;
9. algèbre endpoint `20 736=144*18*8`;
10. composition avec la constante cellulaire `C_I/324`.

Les modules 5, 7, 9 et 10 sont purement algébriques et déjà couverts par un
certificat rationnel. Les modules 2–4 et 8 requièrent géométrie de la mesure,
coaire et Sobolev/BV. La formalisation certifierait seulement un lemme statique
pure-swirl; elle ne certifierait ni pression, ni temps, ni régularité Clay.

## Backlog issu du cycle 0039 — annulation sous recouvrement

Le contre-théorème se sépare en un noyau fini et un raccord lisse :

1. définir la quasi-norme faible sur une mesure finie atomique;
2. calculer exactement les distributions des quatre valeurs de
   `(1+p,1+Mz)` et `(-p,-Mz)`;
3. prouver `q_global^3=1`, `q_1^3=4/(M-1)^3` et `q_2^3=M^-3`;
4. conclure qu'aucune minoration positive ne dépend seulement de
   `(q_global,2)`;
5. formaliser l'identité cylindrique du curl de
   `(F/r)e_theta` loin de l'axe;
6. calculer la mesure exacte de
   `{3/4<=r<=5/4, 0<=z<=2pi, |cos(nz)|>=1/2}`;
7. dériver les deux bornes `q(U_(j,n))=O(n^-1)`;
8. formaliser la réparation positive
   `sum_j (R/r)F_j e_theta=(R/r)(sum_jF_j)e_theta` avant sélection.

Les modules 1–4 et 8 sont élémentaires et prioritaires. Les modules 5–7
requièrent intégration cylindrique et quasi-normes de Lorentz. Une compilation
certifierait l'échec d'une règle de sélection étiquetée, pas Navier–Stokes en
temps ni une implication vers Clay.

## Backlog issu du cycle 0040 — cutoff solénoïdal annulaire

Le lemme se décompose en interfaces indépendantes :

1. calculer `integral div(chi U)=0` pour `chi U` lisse compact;
2. formaliser l'inclusion de mesure finie
   `||f||_(L^(3/2,infinity)(E))<=|E|^(1/3)||f||_(L^(3,infinity)(E))`;
3. transporter un domaine annulaire et un inverse droit par homothétie;
4. enregistrer l'interpolation d'un **même** opérateur aux exposants
   `4/3`, `3/2` et `2`, indice Lorentz secondaire infini;
5. vérifier `|curl b|<=sqrt(2)|grad b|` et le facteur trois de la
   quasi-inégalité triangulaire;
6. séparer la sortie `W_c^(1,(3/2,infinity))` de la sortie `C_c^infinity`, qui
   requiert une propriété explicite de préservation du support lisse;
7. formaliser Biot–Savart faible HLS
   `||U||_(3,infinity)<=C_BS||curl U||_(3/2,infinity)`;
8. pour la couronne mince, prouver la Poincaré radiale pondérée et la dualité
   forte conduisant à `||T||>=c_pR/h`;
9. garder hors du théorème toute version faible-Lorentz de cette minoration
   tant que la dualité `L^(3/2,infinity)`–`L^(3,1)` n'est pas implantée.

Les étapes 1, 2 et 5 sont les premières cibles Lean élémentaires. Aucune
bibliothèque épinglée du dépôt ne fournit encore l'opérateur de Bogovskiĭ sur
une couronne Lipschitz avec support lisse. Une formalisation partielle ne
certifierait ni la sélection d'une boule critique, ni une évolution
Navier–Stokes.

## Backlog issu du cycle 0041 — inclusion faible-`L3` et interface Type I

Le noyau stable se décompose comme suit :

1. définir la fonction de distribution et la quasi-norme
   `K_3(f)=sup_s s mu_f(s)^(1/3)` sur un espace mesuré;
2. prouver `mu_(f|E)(s)<=min(|E|,K_3(f)^3s^-3)`;
3. intégrer les deux branches au seuil `s_0=K_3(f)|E|^-1/3` pour obtenir la
   constante exacte trois;
4. spécialiser à la boule de volume `(4pi/3)r^3` et vérifier l'homogénéité
   `r^-1/2||f||_2<=sqrt(3)(4pi/3)^(1/6)K_3(f)`;
5. formaliser les profils étagés finis et la formule rationnelle de leur
   défaut à trois;
6. formaliser l'algèbre `K_core>gamma`, `0<K_global<=M` implique
   `K_core/K_global>gamma/M`;
7. distinguer supremum temporel pointwise et supremum essentiel dans le type
   du théorème importé;
8. représenter Barker–Prange comme une interface papier versionnée avec
   domaine, classe de solution, premier point singulier et dépendance
   `S_w^*(A)`, sans la marquer comme preuve compilée.

Les étapes 5 et 6 ont déjà un certificat rationnel de 1 346 assertions. Une
formalisation de 1–6 certifierait l'inclusion et la composition algébrique,
pas le théorème PDE publié, l'existence d'un blow-up, ni la régularité Clay.

## Backlog issu du cycle 0042 — opérateur mobile et équation forcée

Le noyau formalisable se décompose ainsi :

1. définir les opérateurs de pullback/pushforward associés à
   `x=x_0+Ry` et prouver leurs règles de composition;
2. vérifier `B_Rg=R B(g sharp)` et `div B_Rg=g`;
3. formaliser la dérivée
   `partial_tB_Rg=B_Rg_t+R'[Bh-y·nabla Bh+B(y·nabla h)]`;
4. formaliser `partial_tQ_Ru=Q_Ru_t+(R'/R^2)[Q,1+y·nabla]U` pour des entrées
   divergence-free et toutes les conditions de moyenne;
5. vérifier `R'/R=-1/(2tau)` et `-RR'=c^2/2` pour `R=c sqrt(tau)`;
6. développer la règle du produit de `(partial_t-Delta)(chi_Ru)` et la jauge
   de pression `chi_Rp`;
7. prouver l'identité (42.11)–(42.12) du rapport principal;
8. certifier les lois de normes
   `L1:R^0`, faible-`L^(3/2):R^-1` et `Hdot^-1:R^-1/2`;
9. maintenir comme interface papier la bornitude de Bogovskii et de ses
   commutateurs sur les espaces de Lorentz/Sobolev négatifs.

Les étapes 5 et 8, ainsi que les jets du témoin, sont couvertes par 499
assertions rationnelles. Une compilation de 1–8 certifierait une identité de
changement d'échelle et une équation forcée, pas la bornitude uniforme des
commutateurs, la convergence vers une solution ancienne ou un résultat Clay.
