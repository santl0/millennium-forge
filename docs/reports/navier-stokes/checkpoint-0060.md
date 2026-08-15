# DÉCISION DU CYCLE

Sélection du système Haar moyen/fluctuant et du signe du stress, noté
`19/20`, devant l'asymptotique ancienne (`16/20`) et un observable moyen de
capture (`13/20`). Le stress est fermé; sa coercivité est réfutée. La revue
primaire ferme ensuite l'endgame axisymétrique sans stationnarité. Le verrou
remonte à la robustesse métrique de la grande vitesse canonique.

# ÉQUATION ET TYPE DE SOLUTION

Navier--Stokes incompressible 3D renormalisé sur `R3 x J`, sans frontière,
viscosité un, drift `kappa(1+y dot nabla)`, axe SO(2) fixe passant par
l'origine, cutoff extérieur localement évanescent et pression globale de
Riesz. Les approximants sont classiques; la limite est faible adaptée locale
et, après dérenormalisation, ancienne suitable. Le résultat publié de rigidité
porte sur la NS physique non forcée, axisymétrique avec swirl permis.

# ÉCHELLE DES QUANTITÉS

`V,W` ont le poids vitesse `lambda`; le stress
`Sigma=mathcal A_2(W tensor W)` et la pression ont le poids `lambda²`;
`div Sigma` a le poids `lambda³`. `L3` et `L^(3/2)` sont les espaces critiques
de vitesse et stress. `integral Sigma:nabla V` a le poids du taux de
dissipation. Les `H^-3` et leurs poids du cycle 0059 restent sous-critiques et
métrique-dépendants.

# AFFIRMATIONS AJOUTÉES OU MODIFIÉES

Ajout de `NS-AXISYMMETRIC-ANCIENT-WEAK-L3-RIGIDITY`, statut
`SOURCE_VERIFIED`, et de `NS-TYPE-I-HAAR-REYNOLDS-STRESS-CLOSURE`, statut
`COMPUTATION_ONLY`, revue `adversarial_pass`. Modification du claim de phase
canonique : la stationnarité reste non déduite, mais n'est plus requise dans
l'endgame axisymétrique suitable. Le registre atteint 101 claims. Ajout de
`FAIL-NS-0096`.

# PREUVE / SOURCE / CALCUL

La moyenne covariante donne exactement
`A_2(Z tensor Z)=V tensor V+Sigma`. La forte `L3_loc` et `mathcal RZ=0`
imposent `W_n->0` dans `L3_loc`, puis `Sigma_n->0` dans `L^(3/2)_loc`; la
dualité Lorentz et la jauge de Riesz ferment sa pression dans les
distributions. Seregin 2020 (`0222`) régularise l'ancienne suitable
axisymétrique faible-`L3`; Ożański--Palasek 2023 (`0088`) l'annulent en
faisant reculer le temps initial. Lei--Ren 2024 (`0223`) confirme une marge
logarithmique locale. Le corpus atteint 223 sources.

# ÉCART AVEC LE PROBLÈME CLAY

Le pipeline ne produit pas encore `ess inf|beta_n|->infinity` depuis une
singularité Type I arbitraire, et cette propriété dépend de la métrique
SO(2)-invariante choisie. L'endgame exige encore forte compacité, suitability,
pression globale, borne faible-`L3` uniforme sur tout le passé et capture.
Type II, axe mobile et limites non axisymétriques ne sont pas traités.

# TEST ADVERSE ET RÉSIDU CERTIFIÉ

Les potentiels `A_V=z exp(-|x|²)(-y,x,0)` et
`A_W=x exp(-|x|²)e_3` produisent des champs de Schwartz divergence-free avec
`mathcal AV=V`, `mathcal AW=0`, mais
`integral(W tensor W):nabla V=-(8/27)(pi/3)^(3/2)`; `V->-V` inverse le signe.
Le script passe 20 assertions exactes, sans discrétisation ni flottant,
résidu nul, empreinte
`2295e890391f8ed34044a1e35ca16a90748f27743ea0a081a677ff590df5fc50`.

# ARTEFACTS MIS À JOUR

Rapport principal, trois revues indépendantes, deux claims JSON, certificat
exact et résultats, catalogue/audit des sources, graphe de dépendances, état
de l'art, questions ouvertes, journaux supercritique/échecs/expériences,
backlog formel et mémoire de gouvernance. Validations réussies : contrat du
dépôt, 101 claims, six prompts, expérience 0060, quatre régressions 0056--0059,
223 sources uniques et `git diff --check`. Commits : `98f8610`, `11f0e93`,
`0116b47`.

# ÉTAT : CONTINUER / RÉVISER / ABANDONNER / À REPRENDRE

CONTINUER. La fermeture du stress et la rigidité ancienne axisymétrique sont
conservées. L'argument de signe dissipatif et l'exigence de stationnarité pour
cet endgame sont abandonnés. Aucune résolution Clay complète n'est revendiquée.

# PROCHAINE EXPÉRIENCE DÉCISIVE

Décomposer `partial_sZ` et `mathcal RZ` en modes azimutaux dans le Hilbert
pondéré. Vérifier si `beta=<partial_sZ,mathcal RZ>/||mathcal RZ||²` est une
moyenne pondérée de vitesses modales et caractériser quand sa divergence est
uniforme pour tous les poids SO(2)-invariants admissibles. Un contre-exemple
éliminera la production automatique du régime rapide; une borne uniforme
fournira un critère intrinsèque d'axisymétrisation.
