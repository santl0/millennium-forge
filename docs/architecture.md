# Architecture

## Flux canonique

```text
source primaire
  → affirmation structurée
  → dépendances
  → expérience ou dérivation
  → contradiction
  → réplication
  → formalisation éventuelle
  → promotion de statut
```

Git reste la source de vérité. Une interface, une base de données ou un graphe interactif doit être dérivé des fichiers versionnés et pouvoir être reconstruit.

## Composants

- `problems/` : cadrage scientifique et index des six cellules ;
- `claims/` : affirmations canoniques validées ;
- `proof-graphs/` : vues dérivées des dépendances ;
- `experiments/` : code reproductible, jamais les sorties lourdes ;
- `formal/` : ponts vers Lean et autres certificats ;
- `literature/` : métadonnées et audits de sources ;
- `failures/` : contre-exemples et pistes abandonnées ;
- `agents/` : protocole commun et missions spécialisées ;
- `schemas/` : contrats JSON ;
- `scripts/` : validation et génération déterministes.

## Rôles logiques

Les rôles peuvent être exécutés par des humains, des agents distincts ou des passes séparées d'un même système : archiviste, cartographe, reproducteur, conjectureur, expérimentateur, contradicteur, formaliseur et arbitre.

Une passe d'arbitrage ne doit pas se fier à la chaîne de raisonnement privée du producteur. Elle examine l'énoncé, les dépendances et les artefacts exposés.

## Extension future

Le stockage de gros artefacts, l'ordonnancement 24/7 et le calcul distribué ne doivent pas modifier le format canonique des affirmations. Ils consomment et produisent des artefacts référencés par identifiant et empreinte cryptographique.
