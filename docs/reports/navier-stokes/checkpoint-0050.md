## DÉCISION DU CYCLE

Action sélectionnée : identifier le cocycle exact des redémarrages et tester
son pouvoir de rigidité dans le quotient faible-`L3` modulo énergie; score
`19/20` contre `15/20` pour une borne BSS ancienne uniforme et `13/20` pour
une promotion directe vers `tilde L^(3,infinity)`. La cohérence algébrique est
fermée; l'inférence d'uniformité depuis la seule structure calorifique est
abandonnée.

## ÉQUATION ET TYPE DE SOLUTION

Navier--Stokes incompressible standard sur
`R3 x (-infinity,0]`, sans frontière, viscosité un, force nulle :
`partial_t v-Delta v+div(v tensor v)+nabla q=0`, `div v=0`,
`q=R_iR_j(v_i v_j)`. Objet conditionnel : solution ancienne faible adaptée
locale, représentant `C_w*` dans `L^(3,infinity)`, uniformément bornée dans
cet espace, munie sur toute bande finie du correcteur BSS énergétique.

## ÉCHELLE DES QUANTITÉS

Sous `v_lambda(x,t)=lambda v(lambda x,lambda²t)`, la norme
`L^(3,infinity)` est invariante,
`||f_lambda||_2=lambda^(-1/2)||f||_2`, et une durée `h` produit le poids
`h^(1/4)` en `L2`. Le contre-profil homogène réalise exactement cette
puissance; l'énergie locale `(8pi/3)R` a le poids longueur attendu.

## AFFIRMATIONS AJOUTÉES OU MODIFIÉES

Ajout de `NS-WEAK-L3-HEAT-COCYCLE-QUOTIENT-OBSTRUCTION`, statut
`COMPUTATION_ONLY`. Le claim établit le cocycle exact, l'énergie de
transition, la convergence locale et le critère suffisant
`liminf_(s->-infinity)||g_(s,r)||_2<infinity => v(r) in L2`; il enregistre
séparément le contre-modèle calorifique, qui n'est pas une solution PDE. Le
registre contient 88 claims.

## PREUVE / SOURCE / CALCUL

La dérivation principale est auditée analytiquement et bibliographiquement.
BSS `NS-SRC-0188`, Taniuchi `NS-SRC-0190` et Albritton--Barker
`NS-SRC-0192` ne fournissent aucune uniformité lorsque la base recule.
Bradshaw--Hudson, arXiv:2508.00714v1, est ajouté comme `NS-SRC-0193` : le
rebasage reste fini et supercritique. Le script exact
`heat_cocycle_audit.py` exécute 161 assertions sans flottants. Le corpus
contient 193 sources.

## ÉCART AVEC LE PROBLÈME CLAY

Le pipeline reste conditionnel à un scénario Type I et à une solution
ancienne déjà construite. Ni `U` ni `U_sharp` ne satisfont Navier--Stokes.
Aucune borne uniforme des correcteurs, mildness ancienne, rigidité,
singularité terminale, exclusion Type II, régularité globale ou construction
de blow-up admissible n'est obtenue.

## TEST ADVERSE ET RÉSIDU CERTIFIÉ

Pour `U=(-x_2,x_1,0)/|x|²`, `K_3(U)^3=pi²/4` et
`||(I-S(h))U||_2=C_U h^(1/4)` avec
`C_U²=(8pi^(5/2)/3)(1-1/sqrt(2))`. La variante lisse `U_sharp` appartient à
`tilde L^(3,infinity) inter Hdot1` et possède des incréments énergétiques sur
chaque bande. Les deux ordres de limites de l'énergie normalisée valent
respectivement `0` et `8pi/3`. Le résidu Navier--Stokes adverse est une
circulation azimutale non nulle; il exclut explicitement ces profils de la
classe PDE. Résidu numérique : sans objet; erreur symbolique certifiée nulle
pour 161 assertions.

## ARTEFACTS MIS À JOUR

Rapport principal et trois revues du cycle 0050; expérience
`experiments/navier-stokes/heat-cocycle`; claim canonique; catalogue et audit
bibliographique; état de l'art, questions, carte, graphe de dépendances,
journal supercritique, registre des échecs, backlog formel et mémoire de
gouvernance.

## ÉTAT : CONTINUER / RÉVISER / ABANDONNER / À REPRENDRE

CONTINUER. Résultat positif : cocycle et critère `liminf` fermés. Résultat
négatif : `FAIL-NS-0086` réfute l'uniformité déduite des seules données
semi-groupales. La stratégie purement calorifique est abandonnée, pas le
verrou PDE.

## PROCHAINE EXPÉRIENCE DÉCISIVE

Tester une identité PDE sensible aux queues — annulation basse fréquence,
flux de pression de Riesz ou tightness annulaire — capable de produire une
sous-suite `s_n->-infinity` avec `||g_(s_n,r)||_2` bornée. Le test devra
suivre le résidu Navier--Stokes, la pression, la dissipation et l'inégalité
locale d'énergie; un nouveau profil purement cinématique ne suffira pas.
