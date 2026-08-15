## DÉCISION DU CYCLE

Action sélectionnée : conjuguer exactement générateur renormalisé et flux
signé, puis isoler l'angle manquant, score `19/20`; triade visqueuse intégrée
`16/20`; observabilité locale de pression `15/20`. L'identité est fermée,
mais le raccord coercif direct est réfuté. Le verrou devient
`GAP-TYPE-I-RENORMALIZED-TANGENTIAL-ACTIVITY-CLASSIFICATION`.

## ÉQUATION ET TYPE DE SOLUTION

Navier--Stokes incompressible standard, non forcé, viscosité un, sur
`R3 x (-infinity,0]`, sans frontière, dans les variables renormalisées :
`partial_s Z-Delta Z+Pdiv(Z tensor Z)+kappa(1+y dot nabla)Z=0`, `div Z=0`,
`kappa>0`. Objet : ancienne faible adaptée locale, pression globale de
Riesz, uniformément faible-`L3`, issue conditionnellement du pipeline Type I.
Ce n'est ni une solution Leray--Hopf globale, ni une donnée Clay générale.

## ÉCHELLE DES QUANTITÉS

`rho=e^(-kappa s)`, `tau=(1-rho²)/(2kappa)` et `dt/ds=rho²`. Le filtre
`B_s=(a-tau)/rho²` reste entre `a` et `1/(2kappa)`. La quantité
`J_a ds=I_a dt` a le même poids `lambda^(-1)` que l'énergie calorifiée
`E_a`; le pairing du stress est
`L^(3/2,infinity)`--`L^(3,1)`. Le facteur `rho²`, la dilatation de `L2` et
la projection de Leray globale sont conservés.

## AFFIRMATIONS AJOUTÉES OU MODIFIÉES

Ajout de `NS-TYPE-I-GENERATOR-FLUX-CONJUGACY`, statut `COMPUTATION_ONLY` :
`J_a=rho²I_a=-partial_s||G_a||_2²`
`=2<G_a,T_rho S(B_s)L_kappa Z>`, avec
`L_kappa=partial_s-Delta+kappa D`. Le registre contient 94 claims. La notice
`NS-SRC-0051` est revérifiée au 15 août 2026; le corpus reste à 205 sources.

## PREUVE / SOURCE / CALCUL

La covariance de la chaleur, `[D,Delta]=-2Delta` et
`B_s'=2kappa B_s-1` donnent
`partial_s[T_rho S(B_s)Z]=T_rho S(B_s)L_kappa Z`; l'identité physique du
cycle 0052 fixe ensuite signe et facteur d'horloge. Un audit analytique
séparé confirme pression, double lissage et validité presque partout. La
veille primaire confirme Pineau--Vicol `arXiv:2607.09619v2` comme
prépublication : RSS Type I exclues pour rotations assez petites ou grandes,
rotation intermédiaire ouverte, sans transfert depuis le seul faible-`L3`.

## ÉCART AVEC LE PROBLÈME CLAY

L'identité ne fournit aucun signe, aucune borne uniforme de primitive, aucun
contrôle `L2` et aucune rigidité de l'ancienne. Elle suppose le pipeline Type
I suitable faible-`L3`, ne traite pas Type II, les orbites modulées ou les
données initiales Clay générales, et ne démontre ni régularité globale ni
blow-up admissible.

## TEST ADVERSE ET RÉSIDU CERTIFIÉ

Le modèle `G=(1-e^s)e(s)` dans une base orthonormée tournante vérifie
`G(0)=0`, `J=-E'=2e^s(1-e^s)`, `integral J=1`, mais
`||G'||²>=1/2`. Sur `N` coquilles, le flux tend vers un tandis que l'action
croît au moins comme `N log(2)/2`. La réalisation solénoïdale sur `T3` a un
résidu NS `G'+G` partout non nul : c'est un contre-test fonctionnel, pas une
solution PDE. Le script exécute 47259 assertions rationnelles exactes, résidu
nul, empreinte
`d5de9de189ed2f2a2db7887b88aa6530a6fe365388c6db0de99ce2c30814693e`.

## ARTEFACTS MIS À JOUR

Rapport principal, trois revues séparées, expérience `tangential-flux`, claim
0054, état de l'art, questions, carte, graphe, journal supercritique, échec
`FAIL-NS-0090`, registre des expériences, backlog formel, audit de source et
mémoires de gouvernance. Commit scientifique `9647653`. Contrat du dépôt,
94 claims, six prompts, trois expériences exactes, empreintes et
`git diff --check` validés.

## ÉTAT : CONTINUER / RÉVISER / ABANDONNER / À REPRENDRE

CONTINUER la classification PDE de l'activité tangentielle. ABANDONNER
l'inférence « activité du générateur ou flux scalaire intégrable implique
coercivité » sans inégalité angulaire supplémentaire. Le résultat positif est
une conjugaison exacte; le résultat négatif élimine un raccord fonctionnel,
pas une branche Navier--Stokes.

## PROCHAINE EXPÉRIENCE DÉCISIVE

Écrire dans les conventions du laboratoire l'orbite relative
`Z(s,y)=R(alpha s)U(R(-alpha s)y)` et son équation RSS. Reproduire les deux
régimes extrêmes de Pineau--Vicol avec constantes Type I suivies, puis tester
le régime intermédiaire et l'observable modulée
`inf_beta||partial_s Z-beta RZ||`, en contrôlant séparément poids adjoint,
pression de bord et différence entre faible-`L3` et borne ponctuelle Type I.
