# Millennium Forge

Laboratoire open source de recherche mathématique assistée par IA autour des six problèmes du millénaire encore ouverts.

## But

Le projet ne collectionne pas des « preuves » invérifiables. Il organise un processus reproductible :

```text
source primaire
  → affirmation structurée
  → graphe de dépendances
  → calcul ou dérivation
  → attaque contradictoire
  → réplication
  → formalisation lorsque possible
```

## Principes

- fidélité aux énoncés officiels ;
- sources primaires et versions explicites ;
- séparation entre preuve, calcul, heuristique et spéculation ;
- conservation des échecs et contre-exemples ;
- expériences reproductibles ;
- contribution humaine ou IA avec provenance ;
- aucune revendication de résolution sans audit indépendant.

## Structure cible

```text
problems/       espaces des six problèmes
claims/         affirmations structurées
proof-graphs/   graphes de dépendances
experiments/    calculs reproductibles
formal/         projets et ponts Lean
literature/     index de sources, sans copies illégitimes
failures/       pistes réfutées
agents/         prompts et protocoles autonomes
schemas/        contrats machine-readable
docs/           contexte, décisions et feuille de route
```

## Démarrage

```powershell
python .github/scripts/check_repo_contract.py .
python scripts/validate_claims.py
```

Voir [CONTRIBUTING.md](CONTRIBUTING.md) avant de proposer une affirmation ou une expérience.

## Projets apparentés

- [Lean Millennium Prize Problems](https://github.com/lean-dojo/LeanMillenniumPrizeProblems)
- [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures)
- [Mathlib](https://github.com/leanprover-community/mathlib4)
- [LeanDojo](https://github.com/lean-dojo/LeanDojo)

## Statut

Bootstrap expérimental. Aucun problème du millénaire n'est revendiqué comme résolu par ce dépôt.

## Licence

MIT. Les sources externes conservent leurs licences respectives et ne doivent pas être recopiées sans autorisation.
