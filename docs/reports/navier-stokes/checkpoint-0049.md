## DÉCISION DU CYCLE

Sélectionner la globalisation de l'énergie relative par cutoffs et pression
de Riesz, score `18/20`. Fermer la dissipation du correcteur et l'inégalité
globale perturbée sur toute bande finie, conserver le statut interne, puis
pivoter vers la cohérence des redémarrages anciens.

## ÉQUATION ET TYPE DE SOLUTION

Sur `R3`, viscosité un, sans force ni frontière, `v` est conditionnellement
une solution ancienne faible adaptée locale, uniformément
`L-infinity_tL^(3,infinity)_x`, avec pression globale
`q=R_iR_j(v_iv_j)`. Sur `[t_0,t_1]`, le correcteur
`w=v-S(t-t_0)v(t_0)` est désormais dans
`C_tL2_x inter L2_tHdot1_x` et satisfait les inégalités locale et globale
perturbées de la classe BSS. Il n'est pas déclaré mild fort, borné, unique,
classique ou Leray–Hopf global sur tout le passé.

## ÉCHELLE DES QUANTITÉS

La norme `L^(3,infinity)` est critique. `||w||_2²` et
`integral||nabla w||_2²` se transforment avec le facteur `lambda^-1`.
Le lissage donne `||V(h)||_4~Mh^-1/8`; le coefficient nu
`||V||_4^8~M^8h^-1` est critique, mais le taux indépendant
`||w(h)||_2²~M^4h^1/2` rend leur produit `M^12h^-1/2` intégrable. Le cutoff
fournit `R^-1`, l'inclusion annulaire coûte `R^1/2` et Young laisse un reste
`O(M^4/R)`.

## AFFIRMATIONS AJOUTÉES OU MODIFIÉES

Ajout de `NS-WEAK-L3-RELATIVE-ENERGY-GLOBALIZATION`, statut
`COMPUTATION_ONLY`, portant le registre à 87 claims. Ajout de
`FAIL-NS-0085`, qui réfute la disparition des flux depuis les seules bornes
fonctionnelles. Le verrou `GAP-TYPE-I-RELATIVE-ENERGY-GLOBALIZATION` est
fermé au statut interne sur bande finie et remplacé par
`GAP-TYPE-I-BSS-ANCIENT-RIGIDITY` et
`GAP-TYPE-I-BSS-TO-STRONG-MILD-CONTINUITY`.

## PREUVE / SOURCE / CALCUL

La première passe combine identité relative locale, inclusion
`L^(3/2,infinity)(A_R)->L^(6/5)(A_R)`, Sobolev, Gagliardo--Nirenberg et
Young pour construire la dissipation sans la supposer. La seconde passe
conserve le signe exact du transfert. Barker--Seregin--Sverak
(`NS-SRC-0188`) définit la classe; Albritton--Barker (`NS-SRC-0192`) publie
le transfert après hypothèse préalable de dissipation, non sa construction.
La veille différentielle ne trouve aucun raccord publié identique. Le corpus
atteint 192 sources; aucune dérivation IA ne reçoit `PAPER_PROOF`.

## ÉCART AVEC LE PROBLÈME CLAY

La branche suppose un scénario Type I et une borne globale faible-`L3`, non
déduits de l'énergie Clay. Les constantes dépendent de la longueur de la
bande et le fond calorifique dépend de `t_0`; aucun passage uniforme vers
`t_0=-infinity` n'est obtenu. Continuité forte critique, mildness bornée,
unicité, rigidité ancienne, Type II, données périodiques et conclusion Clay
restent ouverts.

## TEST ADVERSE ET RÉSIDU CERTIFIÉ

Le certificat passe 97 assertions exactes. Un empilement solénoïdal
multi-annulaire appartient à `L2 inter L^(3,infinity)` et respecte le taux
temporel `h^(1/4)`, mais son flux cubique diagonal normalisé reste exactement
égal à un pour `R_n=4^n`. Sa dissipation diverge : il réfute le raccourci
fonctionnel sans réfuter le raccord suitable. Résidu rationnel nul, aucune
discrétisation PDE, empreinte
`b2ae64c546e0d155a305b43dd0d9f726aef67624af52d654091ca391467bd64d`.

## ARTEFACTS MIS À JOUR

Rapport principal, trois revues indépendantes, script exact, claim JSON,
source primaire `NS-SRC-0192`, audit bibliographique, état de l'art, carte et
graphe, questions ouvertes, journal supercritique, registre des échecs,
index des expériences, backlog formel, contexte, décisions, tâches et ce
checkpoint. Le contrat du dépôt, 87 claims, six prompts, 192 sources, les
certificats de 97 et 144 assertions, les empreintes d'évidence et le diff Git
sont validés.

## ÉTAT : CONTINUER / RÉVISER / ABANDONNER / À REPRENDRE

CONTINUER. La globalisation sur bande finie est conservée comme résultat
interne falsifiable. L'absorption critique grossière, l'annulation des flux
par les seules normes et toute promotion vers une rigidité ancienne sont
abandonnées sans lemme supplémentaire. Aucun résultat Clay n'est revendiqué.

## PROCHAINE EXPÉRIENCE DÉCISIVE

Comparer deux temps de base `s<t_0` et écrire le cocycle exact entre
`S(t-s)v(s)` et `S(t-t_0)v(t_0)`. Tester si les deux correcteurs BSS se
recollent avec une borne uniforme lorsque `s->-infinity`, ou construire un
contre-profil compatible avec les lois d'énergie montrant que la croissance
`(t_1-s)^(1/2)` est inévitable, sans invoquer l'unicité à grande donnée.
