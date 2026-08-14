# AGENTS.md

## Mission

Millennium Forge est un laboratoire ouvert de recherche mathématique assistée par IA consacré aux six problèmes du millénaire encore ouverts. Le dépôt privilégie la traçabilité, la falsifiabilité, la reproductibilité et la vérification formelle.

## Règles durables

- Dépôt public : `santl0/millennium-forge`.
- Branche stable : `main`.
- Branches de travail : `codex/millennium-forge/<sujet>`.
- Une issue porte un objectif scientifique borné ; une pull request porte un changement auditable.
- Ne jamais présenter une annonce, une prépublication ou une sortie d'IA comme un résultat établi.
- Chaque affirmation non élémentaire doit avoir un identifiant, un statut, une source ou une dérivation, des hypothèses et des dépendances.
- Conserver les tentatives réfutées dans le registre des échecs ; ne pas réécrire l'histoire.
- Ne pas versionner les caches, clones temporaires, PDF sous licence, sorties lourdes ni secrets.
- Les actions locales réversibles et validations non destructives sont autorisées sans demande. Les écritures externes, dépenses, publications et actions destructives exigent une autorisation explicite.

## Statuts canoniques

`SPECULATION`, `COMPUTATION_ONLY`, `SOURCE_VERIFIED`, `PAPER_PROOF`, `FORMALIZED`, `REFUTED`, `SUPERSEDED`.

Un agent ne promeut pas seul sa propre affirmation. Toute promotion vers `PAPER_PROOF` ou `FORMALIZED` exige une revue indépendante et les artefacts correspondants.

## Validations obligatoires

- `python .github/scripts/check_repo_contract.py .`
- `python scripts/validate_claims.py`
- `git diff --check`
- tests propres à chaque expérience modifiée
- compilation Lean lorsqu'un projet formel est touché

## Limites

Le dépôt n'est ni une revue scientifique ni une autorité sur le statut des problèmes Clay. Une preuve candidate doit être évaluée indépendamment par des spécialistes et satisfaire les critères officiels applicables.
