# Gouvernance scientifique

## Principe

Le dépôt récompense la qualité de la preuve et de la réfutation, pas la force rhétorique d'une conclusion.

## Promotions

| De | Vers | Exigence minimale |
|---|---|---|
| `SPECULATION` | `COMPUTATION_ONLY` | expérience reproductible |
| `SPECULATION` | `SOURCE_VERIFIED` | source primaire et énoncé fidèle |
| `COMPUTATION_ONLY` | `PAPER_PROOF` | démonstration complète et revue indépendante |
| `SOURCE_VERIFIED` | `PAPER_PROOF` | dérivation nouvelle complète et revue indépendante |
| `PAPER_PROOF` | `FORMALIZED` | certificat formel compilé et correspondance avec l'énoncé papier |
| tout statut | `REFUTED` | contre-exemple ou faille reproductible |
| tout statut | `SUPERSEDED` | remplacement explicite conservant la provenance |

## Contributions IA

Toute contribution substantielle produite avec une IA enregistre : fournisseur ou famille de modèle lorsque connue, date, mission, fichiers affectés, outils utilisés, tests, limites et identité du réviseur indépendant.

Une IA ne peut pas être à la fois producteur et unique réviseur d'une promotion. Deux exécutions du même modèle avec le même contexte ne constituent pas automatiquement deux revues indépendantes.

## Conflits et priorité

- La priorité d'une idée est attribuée par l'historique Git et les sources citées.
- Une idée antérieure retrouvée entraîne une correction d'attribution, pas sa suppression.
- Les conflits scientifiques sont résolus par des affirmations plus précises et des tests discriminants.

## Revendications de résolution

Une pull request prétendant résoudre un problème du millénaire reste en brouillon, reçoit le label de revue maximale et doit expliciter chaque raccord avec l'énoncé officiel. Le dépôt ne remplace pas les procédures de validation du Clay Mathematics Institute.
