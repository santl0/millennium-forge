# Contexte de Millennium Forge

## Objet

Millennium Forge centralise, sous Git et de manière ouverte, les sources, graphes de dépendances, expériences reproductibles, résultats négatifs et formalisations liés aux six problèmes du millénaire encore ouverts :

1. P versus NP ;
2. hypothèse de Riemann ;
3. existence de Yang–Mills et gap de masse ;
4. existence et régularité de Navier–Stokes ;
5. conjecture de Hodge ;
6. conjecture de Birch et Swinnerton-Dyer.

Le dépôt GitHub public cible est `santl0/millennium-forge`. `main` contient uniquement des éléments relus et reproductibles. Les explorations utilisent des branches `codex/millennium-forge/*` et des pull requests en brouillon.

## Positionnement

Le projet complète les formulations Lean existantes et les corpus de conjectures formelles ; il ne prétend pas les remplacer. Sa valeur propre est la couche de recherche : registre des affirmations, provenance, graphes de preuve, expériences, contradictions et reprise autonome par agents.

## Principe de sûreté scientifique

Une ressemblance, un calcul numérique ou une preuve générée par IA ne change jamais seul le statut d'une affirmation. Les conclusions canoniques doivent rester proportionnées à la meilleure preuve effectivement disponible.

## État Navier–Stokes au cycle 0021

Le programme actif a reproduit conditionnellement la chaîne fonctionnelle et
l'endgame `(8)->(58)` de `arXiv:2607.08866v2`, avec corrections des temps,
seuils, constantes, semi-normes et queues. Cette synthèse reste
`COMPUTATION_ONLY` et suppose une vorticité critique ainsi qu'une direction
globale `bmo_phi`; elle n'est pas une résolution Clay.

Le cycle 0020 réfute le raccord universel depuis une cohérence seulement
composante par composante : deux cœurs antipodaux imposent le coût optimal
`4ab/(a+b)` et une divergence logarithmique lorsque leurs fractions restent
fixes à petite échelle. La solution nulle montre aussi que la direction n'est
pas intrinsèque sans convention aux zéros. Le verrou actif est désormais
l'admissibilité PDE complète du profil critique ponctuel supposé en amont.

Le cycle 0021 ferme négativement la sous-classe vectorielle exactement
récurrente. Un profil critique homogène doit satisfaire une porte sphérique de
divergence et de flux; un exemple explicite montre que magnitude `r^-2`,
faible-`L^(3/2)`, divergence et Biot–Savart peuvent coexister tandis que la
direction échoue dans log-BMO. Plus généralement, log-BMO rigidifie toute
direction récurrente par dilatation en une constante, ensuite incompatible
avec une vorticité solénoïdale globale faible-Lorentz non nulle.

La coupure ne fournit pas d'échappatoire perturbative : son défaut de
divergence est invariant d'échelle et son correcteur reste critique. Le verrou
actif devient un profil non récurrent dont la direction se rectifie seulement
comme `1/|log r|`, avec pression et résidu PDE suivis.
