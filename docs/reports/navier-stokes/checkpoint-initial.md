# Checkpoint initial — Navier–Stokes 3D

Date : 2026-08-14. Branche :
`codex/millennium-forge/navier-stokes-state-of-art`. Base locale :
`58aa8b316ebe3f5d7675dede6f18d37d0b844a30`.

## État précis du sous-problème

Le problème Clay est figé pour NS incompressible visqueux 3D sur `R^3` et
`R^3/Z^3`, avec les quatre alternatives officielles (A)–(D). L'existence faible
globale est connue; l'arête manquante est un contrôle critique uniforme ou une
construction de breakdown issue de données exactement admissibles. Aucune
source primaire auditée ne ferme cette arête.

## Fichiers créés ou modifiés

- formulation Clay, état de l'art, carte de recherche, questions et journal
  supercritique sous `problems/04-navier-stokes/` ;
- catalogue primaire et audit sous `literature/navier-stokes/` ;
- graphe annoté sous `proof-graphs/navier-stokes/` ;
- dix affirmations structurées sous `claims/navier-stokes/` ;
- registre d'échecs, registre d'expériences et audit formel ;
- manifeste exhaustif des 22 fichiers historiques, sans écriture dans la
  source historique.

## Sources ajoutées

Le corpus central contient 42 sources primaires ou artefacts producteurs,
complétés par une watchlist 2026. Il couvre l'énoncé CMI, Leray–Hopf,
régularité partielle et adaptée, Prodi–Serrin et endpoint `L^3`, espaces
critiques, profils et solutions anciennes, vorticité, axisymétrie, cascade,
non-unicité, calcul validé, IA et formalisation. Les versions et limites sont
dans `literature/navier-stokes/source-audit.md`.

## Affirmations et statuts

| Statut | Nombre | Contenu |
|---|---:|---|
| `SOURCE_VERIFIED` | 7 | formulation Clay et six résultats/sources centraux, dont la revendication exacte de Hou–Wang–Yang v2 |
| `COMPUTATION_ONLY` | 2 | porte visqueuse mono-échelle et intégrales de coquille `r^-1` |
| `REFUTED` | 1 | déplétion triadique universelle sous seules divergence et hélicité nulle |
| `PAPER_PROOF` / `FORMALIZED` | 0 | aucune promotion automatique |

`SOURCE_VERIFIED` pour une prépublication signifie que son énoncé et sa version
ont été lus, pas que sa preuve a été acceptée.

## Résultat scientifique positif ou négatif

- Positif borné : chaîne de dépendances et pertes explicites, avec pression,
  compacité et constants de troncature séparées.
- Négatif : les singularités IA 2025 auditées concernent des systèmes
  inviscides ou avec frontière; la viscosité domine leur ansatz mono-échelle
  lorsque `lambda>-1/2`. Aucun maillon PDE direct vers Clay n'est établi.
- Négatif : non-unicité faible, force extérieure ou donnée initiale singulière
  ne constituent pas un breakdown Clay.
- Négatif exact : un contre-profil Fourier invalide une déplétion de flux
  universelle basée seulement sur divergence et hélicité nulle.

## Attaques effectuées

- quantificateurs A–D, force et périodicité comparés au PDF CMI ;
- auto-similarité exacte distinguée de Type II et multi-échelles ;
- classes de solutions des résultats de non-unicité comparées à la solution
  lisse Clay ;
- pression et projection de Leray recalculées dans la formulation ;
- deux scripts historiques comparés par empreinte et sortie ;
- audit formel : `sorry`, prémisses conditionnelles et existence faible séparés
  d'une preuve de régularité.

## Tests exécutés

```text
python -B experiments/navier-stokes/viscosity-gate/test_viscosity_gate.py
python -B experiments/navier-stokes/triad-phase/test_triad_phase.py
python -B experiments/navier-stokes/desingularization-gate/desingularization_gate.py
python .github/scripts/check_repo_contract.py .
python scripts/validate_claims.py
python scripts/render_prompts.py --check
git diff --check
```

Résultat : trois scripts passent; résidus rationnels nuls; contrat, dix claims,
prompts et diff valides. Aucun compilateur Lean/Coq/Isabelle n'est installé :
aucun build formel local n'est revendiqué.

## Limites

- Les preuves papier n'ont pas été reproduites ligne à ligne.
- Le calcul d'intervalles Hou–Wang–Yang n'a pas été reproduit : environ 800 Go
  de RAM sont annoncés et aucun manifeste Julia présent n'a été trouvé dans le
  dépôt inspecté.
- Le distant Git ne publie aucune référence, donc il n'existe pas de base
  `origin/main` contre laquelle ouvrir proprement une pull request. Le socle
  local non fusionné est préservé sans réécriture.
- Les revues par sous-agents restent de la même famille de modèle et ne sont pas
  qualifiées de revues externes indépendantes.

## Prochain verrou

Stabilité sous désingularisation d'une donnée homogène de degré `-1`, puis
contrôle des queues de pression si les seules normes usuelles ne fournissent
aucune constante uniforme.

## Prochaine action autonome

Exécuter `DESINGULARIZATION-GATE-1`, soumettre sa conclusion à un contre-test
dynamique, réviser le claim, puis sélectionner automatiquement l'expérience de
pression à deux paquets si l'arête directe vers Clay reste manquante.
