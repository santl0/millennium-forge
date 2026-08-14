# Questions ouvertes priorisées

Mise à jour : 2026-08-14. Une question descend dans la liste lorsqu'un test
réduit son incertitude ou lorsqu'un verrou préalable est découvert. L'historique
des décisions reste dans les checkpoints.

| Priorité | Question falsifiable | Pourquoi maintenant | Critère de sortie |
|---:|---|---|---|
| 1 | quelle hypothèse non circulaire sur une extraction maximum-normalisée KNSS permet d'échanger la limite des zooms avec `t->0-` et d'obtenir une vraie trace nulle dans `D'` sur le même profil ? | le cycle 0008 ferme la rigidité du paquet hybride; l'unique verrou restant est désormais son héritage simultané, incompatible avec la normalisation `|v(0,0)|=1` si la trace est effectivement transmise | module uniforme ou équi-intégrabilité critique démontré et hérité; ou contre-profil exact montrant que toute hypothèse suffisante réintroduit déjà un critère critique connu |
| 2 | une désingularisation du profil initial homogène `-1` de Hou–Wang–Yang possède-t-elle une estimation de stabilité uniforme dans un espace compatible avec des données Clay ? | résultat primaire récent et premier raccord possible | estimation uniforme sourcée/démontrée, ou divergence nécessaire de toutes les constantes de la méthode |
| 3 | une contrainte géométrique locale de vorticité, strictement plus forte que l'hélicité globale mais déductible de NS, impose-t-elle une déplétion triadique ? | le contre-profil exact ferme la version globale naïve | inégalité signée prouvée ou nouveau contre-profil |
| 4 | une extraction de premier blow-up fournit-elle une équicontinuité critique de trace par une structure absente de l'énergie seule ? | `C_t^(1/4)H^-1` est supercritique et coexiste avec le défaut exact; l'axe est suspendu après trois échecs | hypothèse structurelle explicitement sourcée et testée; sinon conserver la suspension |
| 5 | un problème renormalisé NS peut-il être réduit à un opérateur compact avec bornes de queue certifiables ? | préalable à toute preuve assistée par ordinateur | rayon de contraction validable sous raffinement |
| 6 | le noyau Fourier fini énergie–Leray peut-il être formalisé sans axiome ni `sorry` en Lean ? | petite brique stable, indépendante des scénarios spéculatifs | build épinglé + `#print axioms` vide hors logique standard |

## Questions suspendues

- Reproduire le CAP Hou–Wang–Yang : suspendu faute des quelque 800 Go de RAM
  annoncés et d'un manifeste Julia effectivement présent dans le dépôt inspecté.
- Auditer intégralement les manuscrits Shahmurov 2026 : veille conservée, mais
  une revendication unilatérale non publiée ne dépasse pas les verrous mieux
  bornés ci-dessus sans vérification indépendante.

## Question fermée conditionnellement au cycle 0008

Une ancienne mild au sens KNSS sur `R³ x (-infinity,0)`, globalement bornée et
ayant une vraie trace nulle dans `D'` quand `t->0-`, est nécessairement nulle.
Le statut reste `COMPUTATION_ONLY` parce que le chaînage est une dérivation du
laboratoire non revue extérieurement. Le raccord de ces hypothèses à une
extraction Clay reste ouvert et constitue la priorité 1 ci-dessus.

## Règle de pivot

Après trois stratégies mathématiquement différentes bloquées sur la même
question, ajouter leurs échecs au registre, abaisser la question et sélectionner
la meilleure valeur informationnelle suivante. Un simple renommage de norme ou
de profil ne compte pas comme stratégie distincte.
