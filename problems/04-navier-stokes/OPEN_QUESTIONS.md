# Questions ouvertes priorisées

Mise à jour : 2026-08-14. Une question descend dans la liste lorsqu'un test
réduit son incertitude ou lorsqu'un verrou préalable est découvert. L'historique
des décisions reste dans les checkpoints.

| Priorité | Question falsifiable | Pourquoi maintenant | Critère de sortie |
|---:|---|---|---|
| 1 | la projection de la couche de régularisation intérieure, à `t~epsilon²`, sur le mode adjoint instable HWY peut-elle être bornée puis propagée jusqu'à un temps fixe ? | le cycle 0010 réfute le raccord statique `L² + L^{3,infinity} -> L³`; seul un shadowing dynamique non perturbatif peut encore préserver l'instabilité | borne sourcée/certifiée avec séparation de branches, ou divergence d'une constante de projection/semigroupe |
| 2 | une contrainte géométrique locale de vorticité, strictement plus forte que l'hélicité globale mais déductible de NS, impose-t-elle une déplétion triadique ? | le contre-profil exact ferme la version globale naïve | inégalité signée prouvée ou nouveau contre-profil |
| 3 | un problème renormalisé NS peut-il être réduit à un opérateur compact avec bornes de queue certifiables ? | préalable à toute preuve assistée par ordinateur | rayon de contraction validable sous raffinement |
| 4 | le noyau Fourier fini énergie–Leray peut-il être formalisé sans axiome ni `sorry` en Lean ? | petite brique stable, indépendante des scénarios spéculatifs | build épinglé + `#print axioms` vide hors logique standard |

## Questions suspendues

- Reproduire le CAP Hou–Wang–Yang : suspendu faute des quelque 800 Go de RAM
  annoncés. Au commit primaire `615ee6f`, le `Project.toml` existe mais aucun
  `Manifest.toml`; le README se contredit sur ce point. Les candidats `.mat`
  amont ne sont pas tous reliés à une chaîne génératrice et des empreintes.
- Auditer intégralement les manuscrits Shahmurov 2026 : veille conservée, mais
  une revendication unilatérale non publiée ne dépasse pas les verrous mieux
  bornés ci-dessus sans vérification indépendante.
- Forcer une trace nulle dans le zoom maximum KNSS : suspendu après trois
  stratégies. Le cycle 0009 montre que les limites commutent déjà dans la
  classe mild au temps-record `s=0`, où elles conservent une valeur non nulle;
  le temps physique `T` est l'extrémité mobile `B_k`. Une réouverture demande
  une nouvelle extraction, pas une autre topologie sur la même suite.
- Déduire une compacité critique de trace depuis l'énergie seule : suspendu
  après les trois échecs `FAIL-NS-0006` à `0008`.

## Question fermée conditionnellement au cycle 0008

Une ancienne mild au sens KNSS sur `R³ x (-infinity,0)`, globalement bornée et
ayant une vraie trace nulle dans `D'` quand `t->0-`, est nécessairement nulle.
Le statut reste `COMPUTATION_ONLY` parce que le chaînage est une dérivation du
laboratoire non revue extérieurement. Le raccord de ces hypothèses à une
extraction Clay reste ouvert mais est suspendu après le troisième test du
cycle 0009; la priorité active est désormais la désingularisation
Hou–Wang–Yang.

## Résultat négatif du cycle 0010

La localisation HWY est extérieure et conserve le coeur `1/r`. Pour une
régularisation intérieure, la convergence `L²` et une borne uniforme
`L^{3,infinity}` ne donnent pas de compacité `L³` : une famille
`C_c^infinity`, divergence-free, satisfait ces deux prémisses tout en gardant
un écart `L³` strict entre les échelles `epsilon` et `2epsilon`. Toute preuve
de transfert reposant uniquement sur ce module statique est abandonnée. Une
stabilité à temps strictement positif, avec projection instable et couche
parabolique explicites, n'est pas réfutée.

## Règle de pivot

Après trois stratégies mathématiquement différentes bloquées sur la même
question, ajouter leurs échecs au registre, abaisser la question et sélectionner
la meilleure valeur informationnelle suivante. Un simple renommage de norme ou
de profil ne compte pas comme stratégie distincte.
