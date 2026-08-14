# Contribuer à Millennium Forge

## Avant de commencer

1. Ouvrir une issue avec un objectif borné.
2. Identifier le problème, l'affirmation visée et les sources primaires.
3. Créer une branche courte ; les agents Codex utilisent `codex/millennium-forge/<sujet>`.
4. Ne jamais committer de secret, cache, clone imbriqué, PDF non redistribuable ou sortie lourde.

## Contributions scientifiques

Une affirmation doit inclure :

- un identifiant stable ;
- un énoncé exact et ses quantificateurs ;
- un statut canonique ;
- ses hypothèses et dépendances ;
- une source primaire ou une dérivation complète ;
- les tentatives de réfutation ;
- les artefacts reproductibles ;
- l'identité du producteur humain ou IA ;
- l'état de la revue indépendante.

Une expérience doit documenter environnement, versions, paramètres, précision, graine, erreurs et commande de reproduction.

## Revue

- Une pull request commence en brouillon.
- L'auteur ou l'agent producteur ne peut pas être l'unique réviseur d'une promotion de statut.
- Un résultat négatif valide est une contribution de première classe.
- Une assertion spectaculaire reçoit davantage de contrôle, pas davantage de visibilité automatique.

## Validation locale

```powershell
python .github/scripts/check_repo_contract.py .
python scripts/validate_claims.py
git diff --check
```
