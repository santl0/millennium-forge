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

## Backlog issu du cycle 0043 — décomposition négative critique

Le noyau stable à formaliser est :

1. définir `X=L1+div L^(3/2,infinity)` comme norme quotient;
2. prouver les lois d'échelle séparées de `f` et du stress `G`;
3. développer `[Delta,M_chi]U` et `[D,M_chi]U` avec les signes de (43.5);
4. encoder comme interface papier les propriétés
   `T in Psi^(-1)`, `[Delta,T] in Psi^0`, `[D,T] in Psi^(-1)`;
5. prouver l'inclusion faible-`L3` vers `L2(A)` avec constante
   `sqrt(3)|A|^(1/6)`;
6. prouver l'inclusion faible-`L^(3/2)` vers `L^(4/3)(A)` avec constante
   `3^(3/2)|A|^(1/12)`;
7. vérifier la décomposition de `Q div S` et toutes les moyennes nulles;
8. formaliser la composition algébrique donnant
   `C[M²+(1+|kappa|)M]`;
9. formaliser séparément les 222 assertions rationnelles du mode
   haute fréquence.

Les points 4 et la bornitude négative de Bogovskii restent des interfaces de
source, non des théorèmes présents dans une bibliothèque formelle épinglée.
Une compilation de 1–9 certifierait la composition fonctionnelle, pas la
compacité temporelle, la convergence des produits ou la rigidité forcée.

## Backlog issu du cycle 0044 — queue externe de Leray

Le noyau stable à formaliser est séparé de la PDE :

1. définir `Q_L` par conjugaison et prouver `Q_LW=W` dans `B_L`;
2. montrer que la partie locale de `P_L div T` est nulle lorsque
   `supp T` est séparé du compact observé;
3. formaliser les dérivées troisième et quatrième de
   `N(x)=1/(4pi|x|)` avec les majorants rationnels `2|x|^-4` et
   `17|x|^-5`;
4. prouver `||f||_L1(E)<=3|E|^(1/3)K_(3/2)(f)` par couches;
5. sommer les coquilles et obtenir `11904/35` puis `134912/25`;
6. encoder l'invariance des normes du test `psi(y/L)` dans la dualité de
   `X=L1+div L^(3/2,infinity)`;
7. vérifier l'identité de scaling
   `F_L=L^-3B_0(y/L)+kappa L^-1A(y/L)` et la minoration quadratique;
8. garder comme interfaces papier la borne uniforme de `Q_L`, la pression de
   Riesz et la dualité Lorentz.

Les points 3–5 possèdent un certificat rationnel de 253 assertions. Leur
formalisation certifierait une estimation de noyau et un contre-scaling, pas
la compacité d'une suite de solutions, l'inégalité d'énergie locale, une
trace terminale ou un résultat Clay.

## Backlog issu du cycle 0045 — énergie locale et porte de trace

Le noyau stable est à formaliser avant toute tentative sur une solution
ancienne complète :

1. formaliser l'inclusion de mesure finie
   `L^(3,infinity)(E)->L2(E)` avec constante `sqrt(3)|E|^(1/6)`;
2. enregistrer la bornitude papier des Riesz
   `L^(3/2,infinity)->L^(3/2,infinity)` et l'inclusion locale vers `L^(4/3)`;
3. vérifier l'identité du drift
   `Z dot (Z+y dot nabla Z)=div(y|Z|²/2)-|Z|²/2` en dimension trois;
4. formaliser les estimations de Gagliardo–Nirenberg conduisant à
   l'absorption de `||Z||_3³` et `||Pi Z||_1`;
5. isoler un lemme abstrait de remplissage des trous avec toutes les
   puissances de `(rho-r)^-1` et aucune dépendance de la borne extérieure;
6. encoder les inclusions
   `L2 compact->H^-1->W^(-2,4/3)` et
   `H1 compact->L2->W^(-2,4/3)` comme interfaces de Simon;
7. formaliser l'interpolation : convergence forte `L2` plus borne
   `L^(10/3)` implique convergence forte `Lq` pour tout `q<10/3`;
8. séparer dans le type de pression la partie de Riesz proche et la partie
   harmonique, sans déclarer la pression complète fortement compacte;
9. formaliser le lemme de trace élémentaire : convergence dans `H^-1` et
   minoration d'un moment contre un test fixe impliquent une limite non nulle;
10. conserver comme contre-objets les scalings exacts de `C_n=nV(n dot)` et
    de la couche terminale forcée.

Les points 1, 3, 7, 9 et 10 sont les premières cibles élémentaires. Simon,
Calderón–Zygmund et le passage complet de l'inégalité d'énergie restent des
interfaces papier tant qu'aucune bibliothèque épinglée n'en porte les
versions requises. Leur compilation ne certifierait ni l'existence d'un
moment fixe issu de Barker–Prange, ni la dérenormalisation, ni un résultat
Clay.

## Backlog issu du cycle 0046 — persistance mesurée et horloge Type I

Le noyau élémentaire remplace la porte de moment signé dans la branche Type I :

1. définir la quasi-norme locale
   `K_3(f;E)=sup_(lambda>0) lambda |{|f|>lambda} inter E|^(1/3)`;
2. formaliser `K_3(f;E)^3<=integral_E|f|^3` par Chebyshev;
3. intégrer sur un ensemble temporel mesurable et obtenir
   `|J|gamma³<=||f||_(L3(J x E))³`;
4. formaliser la conservation de cette minoration sous convergence forte
   `L3`;
5. vérifier l'invariance exacte de `K_3` sous
   `f(y)=R u(x_*+Ry)`;
6. vérifier, depuis `R²=a(T_*-t)` et `d sigma/dt=R^-2`, que
   `d(log R)/d sigma=-a/2=-kappa`;
7. formaliser : une fonction non nulle dans `L3(I x E)` possède une tranche
   de Lebesgue non nulle;
8. formaliser la translation temporelle de l'équation autonome avec drift
   constant.

Les points 1–8 sont indépendants de Calderón–Zygmund et de Simon. Le théorème
Barker–Prange et le claim de compacité restent des interfaces papier. Leur
composition formelle certifierait une limite renormalisée non triviale, pas
sa dérenormalisation, sa mildness, sa rigidité ni un résultat Clay.

## Backlog issu du cycle 0047 — conjugaison du drift

1. formaliser `r_s=-kappa r`, `tau_s=r²` et la bijection des demi-droites;
2. formaliser les identités de chaîne pour `Z=r v(x_0+ry,tau)`;
3. vérifier les puissances communes `r³` de l'équation et `r²` de la
   divergence;
4. formaliser `dx d tau=r^5dy ds` et le pullback `r²phi` des tests faibles;
5. prouver en dimension trois
   `kappa div(yE)-kappa E=kappa(2E+y dot nabla E)`;
6. formaliser `L_Z=r^4L_v` et le pullback positif `r phi` des tests d'énergie;
7. formaliser l'invariance de la fonction de distribution faible-`L3`;
8. encoder séparément les contre-exposants du certificat et le témoin
   `L^(3,infinity)` non inclus dans `L2`.

Les points 1–7 sont stables et élémentaires. La continuité faible-étoile des
Riesz, la suitability issue de compacité et toute mildness restent des
interfaces papier. Compiler ce noyau certifierait la conjugaison, pas le
claim conditionnel complet ni Clay.

## Backlog issu du cycle 0048 — trace faible-étoile et correcteur sous-critique

1. définir les Lorentz abstraits `L^(3,infinity)` et leur prédual
   `L^(3/2,1)` comme interface papier, sans prétendre construire leur théorie
   de réarrangement dans le premier noyau;
2. formaliser le principe élémentaire : continuité des pairings sur un
   sous-espace dense plus borne uniforme implique un représentant
   `C_w*` unique;
3. encoder la variation des constantes dans un espace de distributions pour
   l'équation projetée;
4. isoler comme interface publiée l'estimation intégrée de Meyer--Yamazaki,
   avec l'ordre exact des quantificateurs « fixer le test, puis intégrer »;
5. formaliser les exposants
   `1/k=1/3+1/p` et
   `integral_0^h r^(-3/2+3/(2p))dr
     =C_p h^((3-p)/(2p))` pour `3/2<p<3`;
6. spécialiser `p=2` pour obtenir la puissance `h^(1/4)` et une trace forte
   nulle du correcteur dans `L2`;
7. formaliser le résidu endpoint : à `p=3`, chaque coquille dyadique de
   `r^-1` a masse constante et la somme croît linéairement;
8. formaliser la fonction de distribution du champ
   `(-x_2,x_1,0)/|x|²`, les constantes `pi²/4` et `(8pi/3)R`, et
   l'invariance de la queue faible-`L3` sous coupure radiale;
9. garder comme interfaces papier O'Neil, le noyau d'Oseen et la projection
   de Leray; ne pas encoder avant stabilisation l'inégalité énergétique BSS.

Les points 2, 5–8 forment le premier noyau compilable. Une formalisation de
ces éléments certifierait le ledger d'exposants, pas l'estimation analytique
de Yamazaki, la dissipation globale, la classe BSS, la rigidité ancienne ou
le problème Clay.

## Backlog issu du cycle 0049 — cutoff relatif et absorption endpoint

1. définir le cutoff `chi_R`, ses supports emboîtés et les bornes
   `|nabla chi_R|<=C/R`, `|Delta chi_R|<=C/R²`;
2. formaliser l'identité relative lisse obtenue par polarisation entre une
   solution suitable et un fond calorifique;
3. isoler comme interface papier le passage de l'inégalité suitable à cette
   identité pour des fonctions seulement énergétiques localement;
4. encoder l'inclusion sur ensemble fini
   `L^(3/2,infinity)(A_R)->L^(6/5)(A_R)` avec facteur `|A_R|^(1/6)`;
5. combiner Sobolev sur `chi_R w` et Young pour obtenir le reste exact
   `C_epsilon M^4/R` sans hypothèse de petitesse sur `M`;
6. formaliser Gagliardo--Nirenberg
   `||z||_4<=C||z||_2^(1/4)||nabla z||_2^(3/4)` et le résidu
   `||V||_4^8||w||_2²`;
7. vérifier les exposants temporels `-1/2` et la covariance d'échelle de la
   borne finale en `T^(1/2)`;
8. séparer dans le type logique la première passe coercive, qui perd le
   signe, de la seconde passe donnant l'inégalité BSS exacte;
9. encoder le contre-profil multi-annulaire comme réfutation d'une implication
   purement fonctionnelle, sans lui attribuer le type de solution PDE.

Les points 1, 4–9 forment un noyau algébrique stable. Les points 2–3 et les
limites faibles restent des interfaces papier. Une compilation certifierait
le ledger de cutoff, pas la suitability de la limite ancienne, la rigidité,
la régularité Clay ou un blow-up.

## Backlog issu du cycle 0050 — cocycle et quotient faible-`L3`

1. formaliser l'identité de cocycle pour une famille dans un espace de
   distributions munie d'un semi-groupe;
2. encoder l'identité énergétique exacte de `S(t)f` pour `f in L2`;
3. formaliser le critère compact-local : convergence `L2_loc` plus borne
   `L2` le long d'une suite implique que la limite est dans `L2`;
4. distinguer dans les types le quotient algébrique `X/Y` du quotient séparé
   `X/closure(Y)` et interdire toute norme sur le premier;
5. encoder l'homogénéité de `U`, sa fonction de distribution, son énergie
   locale et le calcul spectral de `||(I-S(h))U||_2`;
6. formaliser la coupure radiale solénoïdale `U_sharp`, ses incréments
   énergétiques et la non-commutation des limites;
7. isoler comme interface papier les propriétés de Lorentz, la transformée
   de Fourier de `log|x|` et les sorties BSS des cycles précédents;
8. typer explicitement les profils comme contre-modèles calorifiques, jamais
   comme solutions de Navier--Stokes.

Les points 1--6 constituent le prochain noyau stable. Leur compilation
certifierait l'obstruction fonctionnelle, pas la pression PDE, la tightness
ancienne, la rigidité ou le problème Clay.

## Backlog issu du cycle 0051 — saturation et critère infrarouge

1. formaliser le scaling `t^(-1/2)W(x/sqrt(t))` dans `L2` et `Hdot1`, avec
   les puissances exactes `t^(1/4)` et `t^(-1/2)`;
2. encoder le calcul polynomial-rationnel de
   `curl((a dot nabla)a)=4x_3(-x_2,x_1,0)/|x|^6` hors origine;
3. laisser comme interface papier l'existence Jia--Sverak, la classe
   `N(a)` et la décroissance du profil;
4. formaliser le ledger de noyau
   `2^j * 2^(j/2) * integral_0^h exp(-ct2^(2j))dt` et ses deux branches;
5. sommer exactement la queue haute `sum_(j>J)2^(-j)` et les deux branches
   autour de `2^(2j_*) comparable h^(-1)`;
6. formaliser l'équivalence Littlewood--Paley uniquement pour le correcteur
   `L2`, avec un type empêchant de l'appliquer aux traces séparées;
7. encoder la borne
   `||(I-S(a))g||_2<=CM²a^(1/4)` et les quantificateurs « un `a` fixe, une
   suite ancienne »;
8. intégrer le certificat rationnel des coquilles, du proxy `15/7` et des
   limites non commutatives;
9. typer la famille forward translatée séparément d'une orbite ancienne.

Les points 1--2 et 4--9 forment un noyau algébrique stable. Une compilation
certifierait les exposants, sommes et quantificateurs; elle ne certifierait
ni le théorème d'existence publié, ni le mapping Lorentz, ni l'annulation
infrarouge manquante, ni Clay.

## Backlog issu du cycle 0052 — flux de base et triades signées

1. définir abstraitement `G_a(s;r)` dans un espace de Hilbert et formaliser
   la dérivation de l'intégrale de Bochner à borne inférieure mobile;
2. encoder `E_a=||G_a||²`, le facteur deux et l'identité
   `E_a(s;r)=integral_s^rPhi_a`;
3. formaliser les transformations d'échelle
   `E_a^lambda=lambda^(-1)E_(lambda²a)` et
   `Phi_a^lambda=lambda Phi_(lambda²a)`;
4. isoler comme interfaces papier O'Neil, le mapping
   `S(h)Pdiv:L^(3/2,infinity)->L2` et la dualité
   `L^(3/2,infinity)`--`L^(3,1)`;
5. encoder la différence de quarts de puissance et prouver que son majorant
   absolu a l'asymptotique `h^(-1/2)` non intégrable;
6. formaliser les vecteurs d'onde, la divergence, la projection de Leray et
   la réalité des six modes de la triade adverse;
7. prouver exactement les transferts `(-2ABC,0,+2ABC)`, leur somme nulle,
   l'inversion de signe et la polarisation de sortie nulle;
8. typer le certificat comme algèbre instantanée sur `T3`, jamais comme
   solution ancienne sur `R3`.

Les points 1--3 et 5--8 forment un noyau algébrique stable. Les mappings
Lorentz et le passage de l'équation faible au Duhamel lissé restent des
interfaces papier. Une compilation ne certifierait ni cancellation
temporelle, ni rigidité ancienne, ni Clay.

## Backlog issu du cycle 0053 — défaut distributionnel et diagonale

Le noyau stable à formaliser est logique et fonctionnel, sans importer la
preuve PDE complète :

1. définir une famille monotone de semi-normes distributionnelles `D_R` sur
   des fenêtres unitaires et tests `W_0^(1,(3,1))(B_R)`;
2. prouver que la négation de
   `exists R, epsilon, S, forall s<=S, D_R(s)>=epsilon` fournit une suite
   unique `s_n->-infinity` avec `D_R(s_n)->0` pour chaque rayon fixe;
3. formaliser `partial_t U=0` à partir de l'annulation des appariements
   contre les produits de tests temps--espace;
4. formaliser séparément l'invariance de `L^(3,infinity)` sous
   `U(y)=lambda V(lambda y)` et la normalisation
   `lambda=sqrt(2kappa)` du drift.

Le passage suitable, la compacité forte `L3_loc`, la pression de Riesz et le
théorème de Guevara--Phuc restent des dépendances papier non encodées. Aucun
objet Lean, Isabelle ou Coq n'est modifié dans ce cycle.

## Backlog issu du cycle 0054 — conjugaison et projection radiale

Le noyau algébrique stable peut être séparé des mappings PDE :

1. formaliser `rho_s=-kappa rho`, `tau_s=rho²`,
   `B_s=(a-tau)/rho²` et `B_s'=2kappa B_s-1`;
2. encoder `[D,Delta]=-2Delta` et
   `D S(B)=S(B)D-2B Delta S(B)` sur un domaine abstrait adéquat;
3. déduire la conjugaison
   `d_s[T_rho S(B_s)Z]=T_rho S(B_s)L_kappa Z`;
4. dans un espace de Hilbert, formaliser
   `J=2<G,T L>=-d_s||G||²` et le contre-modèle tournant exact;
5. prouver les formules fermées `integral J=1`, `||G'||²>=1/2` et la
   divergence linéaire de l'action sur les coquilles dyadiques;
6. typer séparément la réalisation de Fourier sur `T3` et son résidu non
   nul, afin qu'elle ne puisse être instanciée comme solution NS.

La covariance du semi-groupe, les espaces de Lorentz, la projection de
Leray globale et l'absolue continuité `L2` restent des interfaces papier.
Aucun projet formel n'est modifié dans ce cycle.
