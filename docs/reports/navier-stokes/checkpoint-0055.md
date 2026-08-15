## DÉCISION DU CYCLE

Action sélectionnée : classifier les orbites SO(2) exactes à vitesse
variable, score `19/20`; extension de l'observabilité pondérée au
faible-`L3` `16/20`; calcul direct du flux RSS `15/20`. La vitesse variable
exacte est éliminée hors stabilisateur. Le verrou devient
`GAP-TYPE-I-APPROXIMATE-ROTATION-MODULATION-COMPACTNESS`.

## ÉQUATION ET TYPE DE SOLUTION

Équation renormalisée autonome de Navier--Stokes incompressible standard,
non forcé, viscosité un, sur `R3 x I`, sans frontière :
`partial_s Z+F_kappa(Z)=0`,
`F_kappa=-Delta+Pdiv(Z tensor Z)+kappa(1+y dot nabla)`, `kappa>0`,
`div Z=0`. Objet : solution distributionnelle, et pour les raccords solution
ancienne faible adaptée locale uniformément faible-`L3`, pression globale de
Riesz. L'ansatz relatif exact `Z=Q_theta U` et
`theta in W^(1,1)_loc` sont des hypothèses structurelles supplémentaires.

## ÉCHELLE DES QUANTITÉS

`Q_theta U(y)=R_theta U(R_(-theta)y)` préserve faible-`L3`, `W1,2_loc`, les
boules centrées, la capture et la divergence. L'angle, le temps similaire et
`alpha=theta'` sont sans dimension. Après normalisation du drift à `1/2`, la
vitesse RSS est `omega=alpha/(2kappa)`. Un axe déplacé ne commute pas avec le
drift et ajouterait un transport.

## AFFIRMATIONS AJOUTÉES OU MODIFIÉES

Ajout de `NS-TYPE-I-EXACT-RELATIVE-ROTATION-CLASSIFICATION`, statut
`COMPUTATION_ONLY`. Si `mathcal R U=0`, l'orbite est stationnaire; sinon
`theta(s)=alpha s+theta_0` et
`F_kappa(U)+alpha mathcal R U=0`. Le registre contient 95 claims. Ajout de
Bradshaw--Tsai, Field et Krupa (`NS-SRC-0206` à `0208`); le corpus atteint
208 sources.

## PREUVE / SOURCE / CALCUL

La règle de chaîne distributionnelle vaut sous
`theta in W^(1,1)_loc`; l'équivariance du Laplacien, du drift, du stress et
de la projection donne
`theta' mathcal R U+F_kappa(U)=0`. Si `mathcal R U!=0`, un test compact non
nul fixe `theta'` presque partout; sinon l'action de groupe est constante.
Bradshaw--Tsai publie le repère à `dot(theta)` variable et la phase RSS
logarithmique; Pineau--Vicol v2 mentionne une classification voisine dans une
remarque de prépublication, sans théorème suitable faible-`L3`.

## ÉCART AVEC LE PROBLÈME CLAY

Rien ne montre qu'une limite de blow-up appartient exactement à une orbite
de rotation d'un profil fixe ou admet un relèvement de phase absolument
continu. La branche RSS tournante faible-`L3` n'est pas annulée en général;
Pineau--Vicol exige une borne Type I ponctuelle et laisse les rotations
intermédiaires ouvertes. Type II et les données Clay générales restent hors
du raccord.

## TEST ADVERSE ET RÉSIDU CERTIFIÉ

Avec résidus de norme `epsilon`, l'algèbre donne seulement
`|beta(s)-beta(t)| ||mathcal R U||<=2epsilon`. Des modèles exacts séparent
non-autonomie, générateur dégénéré, profils non compacts et opérateur
discontinu au stabilisateur. Le script exécute 960 assertions rationnelles
exactes, résidu nul, empreinte
`c9a2ca834951ea18ac5fca89d06d24cd73601181b99268a50f1749f21c9bb207`.
Ces modèles sont finis et abstraits, non des solutions Navier--Stokes.

## ARTEFACTS MIS À JOUR

Rapport principal, audits analytique, primaire et contradictoire, expérience
`relative-rotation`, claim 0055, trois sources, état de l'art, questions,
carte, graphe, journal supercritique, `FAIL-NS-0091`, registre des
expériences, backlog formel et mémoires de gouvernance. Commit scientifique
`ef6146f`. Contrat du dépôt, 95 claims, six prompts, trois expériences
exactes, empreintes et `git diff --check` validés.

## ÉTAT : CONTINUER / RÉVISER / ABANDONNER / À REPRENDRE

CONTINUER. La dichotomie exacte est conservée. ABANDONNER sa promotion naïve
à un énoncé approché sans borne sur `beta`, non-dégénérescence ou quotient du
générateur, compacité du profil et continuité de l'opérateur. L'objectif
persistant reste actif; aucune conclusion de régularité Clay n'est annoncée.

## PROCHAINE EXPÉRIENCE DÉCISIVE

Attaquer d'abord le relèvement de phase et le cas compact : sous les bornes
suitable du pipeline, supposer l'appartenance à une orbite et un défaut
`partial_s Z_n-beta_n mathcal R Z_n->0` avec `beta_n` borné. Construire une
coordonnée de phase par un test détectant `mathcal R U`, extraire
`beta_n->alpha` et vérifier le passage fort du stress et de la pression. Si
le détecteur dégénère, basculer explicitement vers la branche axisymétrique
stationnaire au lieu de diviser par une constante tendant vers zéro.
