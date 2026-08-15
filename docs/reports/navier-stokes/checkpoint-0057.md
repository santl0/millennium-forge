# DÉCISION DU CYCLE

Sélection du collapse par le réciproque BV d'une vitesse de rotation
divergente, noté `20/20`, devant la mesure de défaut/H-mesure (`16/20`) et la
rigidité RSS intermédiaire directe (`13/20`). Le régime adiabatique est fermé
conditionnellement; la seule grandeur de la vitesse est abandonnée après un
contre-profil stroboscopique exact.

# ÉQUATION ET TYPE DE SOLUTION

Navier--Stokes incompressible 3D renormalisé autonome sur `R3 x I`, sans
frontière, viscosité un, force nulle, drift `kappa(1+y dot nabla)` avec
`kappa>0`. Le cœur du lemme est distributionnel. Le raccord final exige une
limite suitable, `W1,2_loc`, à pression de Riesz et uniformément
`L-infinity_s L^(3,infinity)_y`; il ne concerne ni Euler, ni Coriolis, ni un
domaine tournant.

# ÉCHELLE DES QUANTITÉS

Le temps similaire, `beta_n`, `q_n=1/beta_n` et `Var_J(q_n)` sont sans
dimension. La forte `L3_loc` et la norme globale faible-`L3` sont critiques
pour l'échelle de vitesse. La norme locale `L1_sH^(-1)(B_R)` est suivie sur
chaque cylindre fixe et aucune uniformité cachée en `R` n'est revendiquée.

# AFFIRMATIONS AJOUTÉES OU MODIFIÉES

Ajout de `NS-TYPE-I-ADIABATIC-FAST-ROTATION-COLLAPSE`, statut
`COMPUTATION_ONLY`, revue `adversarial_pass`. Le registre contient 97 claims.
Ajout de `FAIL-NS-0093`, qui réfute l'implication fondée sur la seule
minoration de `|beta_n|`. Le verrou actif devient
`GAP-TYPE-I-FAST-ROTATION-STROBOSCOPIC-OR-RSS-RIGIDITY`.

# PREUVE / SOURCE / CALCUL

Sur chaque fenêtre compacte, la borne
`||q_n||_infinity+Var(q_n)->0`, la borne locale
`L-infinity_sL2_y` et un défaut modulé borné dans `L1_sH^-1_y` rendent nul
`mathcal RZ` par intégration par parties contre `q_n phi`. Si le défaut tend
en plus vers zéro dans les distributions, la moyenne de Haar donne
`partial_sZ=0`. Le ledger complet et la capture contredisent alors le
Liouville stationnaire publié de Guevara--Phuc. Sept sources publiées sur
rotation rapide et Liouville stationnaire sont ajoutées; le corpus atteint
217 entrées. Ożański--Palasek reste limité au raccord forte/classique pour la
route ancienne axisymétrique.

# ÉCART AVEC LE PROBLÈME CLAY

Aucune singularité Clay arbitraire ne fournit actuellement une phase
`W1,1`, la petite variation de `1/beta_n`, le défaut `L1H^-1`, la compacité
suitable uniforme, la borne globale faible-`L3` et la capture simultanément.
Type II, axes mobiles, concentration multi-échelle et RSS à vitesse
intermédiaire restent hors du lemme. L'exclusion d'une famille compacte de
profils extrêmes ne prouve ni régularité globale ni blow-up.

# TEST ADVERSE ET RÉSIDU CERTIFIÉ

Le certificat exact utilise des vitesses positives `N` et `N^4` sur `N^2`
cycles : `||q_N||_infinity=1/N`, mais
`Var(q_N)=(2N^2-1)(1/N-1/N^4)~2N`. Les passages rapides ont mesure
`1/(N^2+N+1)` et l'orbite converge fortement dans tout `L^p` fini vers un
profil non axisymétrique. Le script passe 44218 assertions rationnelles,
résidu arithmétique nul, sans PDE ni arrondi, empreinte
`ab815a4d6db1a1b956a50b87c428f8fb6aaf97bc6e16abb3e977685758a1ea69`.

# ARTEFACTS MIS À JOUR

Rapport principal et trois revues contradictoires, claim JSON, sept notices
bibliographiques, graphe de dépendances, état de l'art, questions ouvertes,
journaux supercritique/échecs/expériences, backlog formel et mémoire de
gouvernance. Validation réussie : contrat du dépôt, 97 claims, six prompts,
expérience 0057 et deux régressions des cycles 0055--0056, puis
`git diff --check`. Commit scientifique : `5af115a`.

# ÉTAT : CONTINUER / RÉVISER / ABANDONNER / À REPRENDRE

CONTINUER. Le sous-régime réciproque-BV est conservé; l'inférence depuis la
seule grande vitesse est abandonnée. Aucune condition terminale globale du
programme n'est atteinte.

# PROCHAINE EXPÉRIENCE DÉCISIVE

Sélectionner `beta_n` par une condition de phase canonique sur des
approximants suitable, dériver la matrice de Gram et son inverse, puis tester
si l'énergie locale et la décomposition de pression contrôlent uniformément
`Var(1/beta_n)`. Après trois mécanismes PDE réellement distincts échouant sur
ce verrou, consigner l'obstacle et pivoter vers la rigidité RSS faible-`L3`
ou la production directe du défaut modulé.
