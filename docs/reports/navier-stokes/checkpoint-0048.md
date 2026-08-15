## DÉCISION DU CYCLE

Sélectionner la formule de Duhamel et le correcteur global, score `17/20`.
Fermer `C_w*L^(3,infinity)`, le Duhamel endpoint de Gelfand et la trace
`C_tL2` du correcteur; refuser les promotions vers mildness forte ou BSS,
puis pivoter vers la globalisation de l'énergie relative.

## ÉQUATION ET TYPE DE SOLUTION

Sur `R3`, viscosité un, sans force ni frontière, on considère
conditionnellement la solution ancienne standard non triviale du cycle 0047,
distributionnelle, faible adaptée locale, uniformément
`L-infinity_tL^(3,infinity)_x`, avec
`q=R_iR_j(v_iv_j)`. Sur toute bande finie elle est `C_w*` et satisfait
Duhamel faible-étoile. Elle n'est pas déclarée mild forte, BSS, Leray–Hopf,
bornée ou classique.

## ÉCHELLE DES QUANTITÉS

La vitesse `L^(3,infinity)` et le stress `L^(3/2,infinity)` sont critiques.
Le noyau `S(h)Pdiv` a l'échelle `h^-2K_1(x/sqrt(h))`. Pour
`1/k=1/3+1/p`, son action donne la puissance temporelle
`h^(-3/2+3/(2p))`, intégrable pour `3/2<p<3`, puis le gain
`h^((3-p)/(2p))`. À `p=2`, le gain est `h^(1/4)`; à `p=3`, l'estimation
ponctuelle est `h^-1`. Une dérivée supplémentaire au niveau `p=2` coûte
`h^-5/4`.

## AFFIRMATIONS AJOUTÉES OU MODIFIÉES

Ajout de `NS-WEAK-L3-DUHAMEL-L2-CORRECTOR`, statut `COMPUTATION_ONLY`,
portant le registre à 86 claims. Révision de `FAIL-NS-0083` : Duhamel n'est
plus absent au sens faible-étoile. Ajout de `FAIL-NS-0084`, qui réfute
Bochner, continuité forte, dissipation et split énergétique comme
conséquences automatiques. Le verrou actif devient
`GAP-TYPE-I-RELATIVE-ENERGY-GLOBALIZATION`.

## PREUVE / SOURCE / CALCUL

La dérivation construit d'abord le représentant temporel, puis applique la
variation des constantes. Yamazaki 2000 (`NS-SRC-0118`) et Taniuchi 2024,
définition 1 et lemme 7 (`NS-SRC-0190`), ferment l'intégrale endpoint test
par test. Barker–Seregin–Šverák (`NS-SRC-0188`) fixe les clauses énergétiques
encore absentes. Jarrín 2026 (`NS-SRC-0191`) ne couvre pas l'endpoint ancien.
Le corpus atteint 191 sources. Trois audits séparés confirment les
quantificateurs et la frontière de classe; aucune composition IA ne reçoit
`PAPER_PROOF`.

## ÉCART AVEC LE PROBLÈME CLAY

La branche suppose un blow-up Type I et une borne critique faible-`L3`, qui
ne découlent pas de l'énergie Clay. Elle ne contrôle ni Type II, ni
continuité forte critique, ni dissipation globale, ni flux à l'infini, ni
bornitude, ni rigidité ancienne, ni singularité terminale. Les cas Clay
périodique et espace entier restent irrésolus.

## TEST ADVERSE ET RÉSIDU CERTIFIÉ

Le certificat passe 144 assertions exactes. L'intégration directe endpoint
accumule une unité par coquille logarithmique et un résidu normalisé `N` sur
`N` coquilles. Le champ solénoïdal
`U=(-x_2,x_1,0)/|x|²` vérifie exactement
`K_3(U)^3=pi²/4` et `||U||_(L2(B_R))²=(8pi/3)R`; sa queue radiale ne devient
pas petite. Résidu rationnel nul, aucune discrétisation, empreinte
`c5fcfef5a5cb3202cbc55bc7656c03651e281679badb4561ae34eabd7414a902`.

## ARTEFACTS MIS À JOUR

Rapport principal, trois revues, script exact, claim JSON, deux sources,
audit bibliographique, état de l'art, carte et graphe, questions ouvertes,
journal supercritique, registre des échecs, index des expériences, backlog
formel, contexte, décisions, tâches et checkpoint. Le contrat du dépôt, les
86 claims, six prompts, 191 sources, les certificats de 144 et 420
assertions et le diff Git sont validés.

## ÉTAT : CONTINUER / RÉVISER / ABANDONNER / À REPRENDRE

CONTINUER. Le Duhamel faible-étoile et le correcteur `C_tL2` sont conservés
comme résultat interne falsifiable. La mildness forte et la classe BSS sont
abandonnées sans leurs lemmes de raccord. Aucun résultat Clay n'est
revendiqué.

## PROCHAINE EXPÉRIENCE DÉCISIVE

Appliquer l'inégalité locale au correcteur avec des cutoffs `chi_R`, suivre
séparément les flux de convection, pression de Riesz et flot calorique, puis
certifier soit leur disparition uniforme lorsque `R->infinity`, soit un
contre-profil PDE-compatible d'influx énergétique à l'infini. Ne tester par
`w` qu'après avoir obtenu indépendamment `nabla w in L2`.
