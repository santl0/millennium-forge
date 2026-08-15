## DÉCISION DU CYCLE

Action sélectionnée : tester la croissance `t^(1/4)` sur une vraie solution
forward auto-similaire de Navier--Stokes; score `19/20` contre `17/20` pour
le critère dyadique et `16/20` pour une tightness annulaire directe. La borne
forward universelle est réfutée. La passe indépendante ferme en plus les
hautes fréquences et réduit le verrou ancien à l'infrarouge.

## ÉQUATION ET TYPE DE SOLUTION

Navier--Stokes incompressible standard sur `R3`, sans frontière, viscosité
un et force nulle. Objet adverse : solution globale forward auto-similaire
de Leray locale, faible adaptée et lisse pour `t>0`, issue d'une donnée
faible-`L3` moins-un homogène. Objet conditionnel du critère : solution
ancienne faible adaptée locale, à pression globale de Riesz et uniformément
bornée dans `L-infinity_tL^(3,infinity)_x`, avec correcteurs énergétiques sur
chaque bande finie.

## ÉCHELLE DES QUANTITÉS

Sous `u_lambda(x,t)=lambda u(lambda x,lambda²t)`, la norme
`L^(3,infinity)` est invariante, `||w_lambda||_2=lambda^(-1/2)||w||_2` et
`||w(t)||_2=C_*t^(1/4)`. La dissipation cumulée a le poids longueur et croît
comme `t^(1/2)`. Le seuil fréquentiel mobile est
`2^j comparable (r-s)^(-1/2)`; la queue haute fixée `j>J` est uniformément
`O(M^4 2^(-J))` en énergie.

## AFFIRMATIONS AJOUTÉES OU MODIFIÉES

Ajout de `NS-FORWARD-SELFSIMILAR-CORRECTOR-SATURATION` et
`NS-WEAK-L3-ANCIENT-INFRARED-CRITERION`, tous deux
`COMPUTATION_ONLY` avec passe adverse. Le premier enregistre le saturateur
PDE et sa portée strictement forward; le second établit la borne dyadique,
le contrôle uniforme des hautes fréquences et l'équivalence du critère bas.
Le registre contient 90 claims.

## PREUVE / SOURCE / CALCUL

Jia--Sverak (`NS-SRC-0194`, Invent. Math. 2014) fournit l'existence local
Leray/suitable et la décroissance du profil. Le calcul du curl force le
correcteur non nul; le scaling donne ensuite les identités exactes. La veille
ajoute `NS-SRC-0194` à `NS-SRC-0202`; le corpus atteint 202 sources. Le
Duhamel projeté et le noyau Lorentz `L^(6/5,1)` donnent le critère
infrarouge. Le script exact exécute 615 assertions rationnelles.

## ÉCART AVEC LE PROBLÈME CLAY

La donnée auto-similaire est singulière et d'énergie infinie. Les bandes
translatées ne constituent pas une solution ancienne unique. La réduction
ancienne reste conditionnelle à Type I et n'établit pas le gain infrarouge,
la rigidité L2, une singularité terminale, l'exclusion Type II, la régularité
globale ou un blow-up admissible pour les données Clay.

## TEST ADVERSE ET RÉSIDU CERTIFIÉ

Pour `a=(-x_2,x_1,0)/|x|²`, le résidu de linéarité est certifié par
`curl((a dot nabla)a)=4x_3(-x_2,x_1,0)/|x|^6`, donc `C_*=||W||_2>0`.
Le ledger dyadique donne exactement la masse `2^j`, le proxy total
`(15/7)2^n`, l'enveloppe calorifique `[(1/3)2^n,(4/3)2^n]` et les deux
ordres de limites `15/7` contre `0`. Résidu rationnel : zéro pour 615
assertions; largeur normalisée de l'enveloppe : un. Le certificat ne prouve
pas le théorème PDE.

## ARTEFACTS MIS À JOUR

Rapport principal et trois revues du cycle 0051; expérience
`experiments/navier-stokes/low-frequency-tail`; deux claims; neuf sources
et audit bibliographique; état de l'art, questions, carte, graphe de
dépendances, journal supercritique, registre des échecs, backlog formel et
mémoires de gouvernance. Contrat du dépôt, 90 claims, six prompts, expérience
0051, régression 0050 et `git diff --check` validés.

## ÉTAT : CONTINUER / RÉVISER / ABANDONNER / À REPRENDRE

CONTINUER. Résultat négatif : `FAIL-NS-0087` réfute toute borne forward
uniforme en horizon dépendant seulement de la norme faible-`L3`, même avec
PDE et suitability. Résultat positif : les hautes fréquences sont fermées et
le verrou est exactement infrarouge. Abandonner les estimations forward
uniformes; conserver la branche d'une même orbite ancienne.

## PROCHAINE EXPÉRIENCE DÉCISIVE

Tester, sur les intégrales vectorielles basses
`B_j(s,r)=-integral_s^r Delta_jS(r-tau)Pdiv(v tensor v)(tau)dtau`, un gain
signé uniforme `2^(epsilon(j-J))` le long d'une suite ancienne. Le test doit
conserver phases et triades, fixer `J` avant la limite et vérifier si une
annulation de moment ou une récurrence de blow-down est réellement héritée
du scénario Type I.
