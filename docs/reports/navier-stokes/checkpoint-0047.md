## DÉCISION DU CYCLE

Sélectionner le transport exact de l'équation, de la pression et de
l'inégalité d'énergie locale, score `18/20`. Fermer au statut interne
`GAP-TYPE-I-DERENORMALIZATION-CLASS`; refuser les promotions automatiques
mild et Leray–Hopf, puis pivoter vers la première clause globale manquante.

## ÉQUATION ET TYPE DE SOLUTION

Sur `R3`, viscosité un, sans force ni frontière, la branche part
conditionnellement d'une solution de Leray–Hopf lisse avant un premier
blow-up Type I. La limite renormalisée `Z` est ancienne, faible adaptée
locale, non triviale et uniformément faible-`L3`, avec pression globale de
Riesz. Sa dérenormalisation `v` est exactement une solution ancienne
standard de la même classe sur `R3 x (-infinity,0]`; elle n'est pas déclarée
Leray–Hopf, local-energy avec trace forte, mild, bornée ou classique.

## ÉCHELLE DES QUANTITÉS

Avec `r=e^(-kappa s)`, `tau=(1-r²)/(2kappa)`, `x=x_0+ry`,
`v=r^-1Z`, `q=r^-2Pi`, on a `tau_s=r²`, `dx d tau=r^5dy ds`,
`N_renormalise=r³N_standard`, `div_yZ=r²div_xv` et
`L_renormalise=r^4L_standard`. `K_3(v(tau))=K_3(Z(s))` exactement. Les
intégrales espace–temps de `|v|³`, `|q|^(3/2)` et `|nabla v|²` portent
respectivement les poids `r²`, `r²` et `r` sur les variables renormalisées.

## AFFIRMATIONS AJOUTÉES OU MODIFIÉES

Ajout de `NS-TYPE-I-DERENORMALIZED-ANCIENT-LOCAL-SUITABLE`, statut
`COMPUTATION_ONLY`, portant le registre à 85 claims. Ajout de
`FAIL-NS-0083`, qui réfute la promotion fonctionnelle automatique vers
Leray–Hopf ou mild. Fermeture interne de
`GAP-TYPE-I-DERENORMALIZATION-CLASS`; ouverture de
`GAP-TYPE-I-ANCIENT-WEAK-L3-RIGIDITY-OR-MILDNESS`.

## PREUVE / SOURCE / CALCUL

La dérivation distributionnelle suit séparément l'horloge, le jacobien, la
pression de Riesz et le test positif de l'énergie locale. Deux audits
contradictoires indépendants confirment la classe obtenue et les clauses non
héritées. Albritton–Barker 2019 est ajouté comme `NS-SRC-0189` : ses
théorèmes exigent une ancienne mild bornée avec contrôle Type I, ou mild avec
`L3` fort le long d'une suite reculée. Le corpus atteint 189 sources. La
composition du laboratoire n'est attribuée à aucune source et ne reçoit pas
`PAPER_PROOF`.

## ÉCART AVEC LE PROBLÈME CLAY

La branche suppose déjà un blow-up Type I et une borne uniforme
`L-infinity_tL^(3,infinity)_x`, non donnée par l'énergie Clay. La sortie est
une ancienne suitable locale à énergie potentiellement infinie, sans formule
de Duhamel, bornitude ni singularité terminale. Aucun théorème général
n'exclut cette classe. Type II, le cas périodique et la construction d'un
blow-up admissible restent hors de la conclusion.

## TEST ADVERSE ET RÉSIDU CERTIFIÉ

Le certificat passe 420 assertions rationnelles exactes. Un mauvais signe
d'échelle laisse `-2kappa r^-3DZ`; un mauvais signe du drift laisse
`+2kappa r^-3DZ`; une horloge gelée laisse le coefficient `r²-1`; les
amplitudes de vitesse ou pression erronées laissent aussi des coefficients
non nuls. L'opérateur d'énergie local et le poids de test `r` sont certifiés.
Résidu exact nul pour la transformation correcte; empreinte
`dcb59c2a926846be15d2f088ffbd4484b8b2838ce24c6a2e721d5f1404872050`.

## ARTEFACTS MIS À JOUR

Rapport principal, trois revues, script de dérenormalisation, claim JSON,
catalogue et audit des sources, état de l'art, carte et graphe, questions
ouvertes, journal supercritique, échecs, expériences, backlog formel,
contexte, décisions, tâches et checkpoint. Le contrat du dépôt, 85 claims,
six prompts, 189 sources, les certificats de 420 et 417 assertions et le
diff Git sont validés.

## ÉTAT : CONTINUER / RÉVISER / ABANDONNER / À REPRENDRE

CONTINUER. La conjugaison est conservée comme résultat interne falsifiable;
les promotions Leray–Hopf et mild sont abandonnées sans lemme de raccord.
Aucun résultat Clay n'est revendiqué.

## PROCHAINE EXPÉRIENCE DÉCISIVE

Fixer un temps fini `tau_0<0` et tester si l'ancienne obtenue admet
uniformément sur `[tau_0,0)` la scission
`v=e^((tau-tau_0)Delta)v(tau_0)+w` de Barker–Seregin–Šverák, avec `w` dans
la classe énergétique globale. Suivre séparément la queue faible-`L3`, la
trace de redémarrage et tout reste calorique homogène; construire un
contre-profil PDE-compatible si l'une de ces clauses échoue.
