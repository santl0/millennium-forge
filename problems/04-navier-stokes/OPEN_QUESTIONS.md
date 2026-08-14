# Questions ouvertes priorisées

Mise à jour : 2026-08-14. Une question descend dans la liste lorsqu'un test
réduit son incertitude ou lorsqu'un verrou préalable est découvert. L'historique
des décisions reste dans les checkpoints.

| Priorité | Question falsifiable | Pourquoi maintenant | Critère de sortie |
|---:|---|---|---|
| 1 | une désingularisation du profil initial homogène `-1` de Hou–Wang–Yang possède-t-elle une estimation de stabilité uniforme dans un espace compatible avec des données Clay ? | résultat primaire récent et premier raccord possible | estimation uniforme sourcée/démontrée, ou divergence nécessaire de toutes les constantes de la méthode |
| 2 | la borne `R^-4` de pression distante centrée reste-t-elle uniforme dans la normalisation exacte d'une suite de blow-up, et que contrôle-t-elle de la pression proche ? | le cycle 0002 ferme la queue à énergie globale fixée mais expose la constante remise à l'échelle | suivi exact de l'énergie rescalée ou contre-suite multi-échelle |
| 3 | une contrainte géométrique locale de vorticité, strictement plus forte que l'hélicité globale mais déductible de NS, impose-t-elle une déplétion triadique ? | le contre-profil exact ferme la version globale naïve | inégalité signée prouvée ou nouveau contre-profil |
| 4 | quelle classe minimale de solutions anciennes adaptées admet un théorème de Liouville sans supposer `L^3` borné ? | arête finale de la chaîne de rigidité | théorème de rigidité ou solution ancienne non triviale |
| 5 | un problème renormalisé NS peut-il être réduit à un opérateur compact avec bornes de queue certifiables ? | préalable à toute preuve assistée par ordinateur | rayon de contraction validable sous raffinement |
| 6 | le noyau Fourier fini énergie–Leray peut-il être formalisé sans axiome ni `sorry` en Lean ? | petite brique stable, indépendante des scénarios spéculatifs | build épinglé + `#print axioms` vide hors logique standard |

## Questions suspendues

- Reproduire le CAP Hou–Wang–Yang : suspendu faute des quelque 800 Go de RAM
  annoncés et d'un manifeste Julia effectivement présent dans le dépôt inspecté.
- Auditer intégralement les manuscrits Shahmurov 2026 : veille conservée, mais
  une revendication unilatérale non publiée ne dépasse pas les verrous mieux
  bornés ci-dessus sans vérification indépendante.

## Règle de pivot

Après trois stratégies mathématiquement différentes bloquées sur la même
question, ajouter leurs échecs au registre, abaisser la question et sélectionner
la meilleure valeur informationnelle suivante. Un simple renommage de norme ou
de profil ne compte pas comme stratégie distincte.
