# DÉCISION DU CYCLE

Retenir le lemme périmètre–diamètre d'une branche persistante, score `20/20`,
devant le ledger direct du pont (`18/20`) et l'arbre de fusion récursif
(`16/20`). Fermer le pont de persistance relative fixe lorsqu'il est calibré
à l'échelle endpoint locale, et activer
`GAP-BRIDGE-SCALE-CALIBRATION-OR-MERGE-TREE`.

# ÉQUATION ET TYPE DE SOLUTION

Référence : Navier–Stokes incompressible non forcé sur `R3`, viscosité
`nu>0`. Objet effectivement traité : donnée lisse compacte divergence-free
pure-swirl `U=(R/r)F e_theta` et son curl exact à un temps fixé. Aucune
solution en temps, pression, singularité admissible, solution ancienne ou
solution de Leray–Hopf n'est construite.

# ÉCHELLE DES QUANTITÉS

Sous `U_rho(x)=rho U(rho x)`, les quasi-normes
`K_u=||U||_(L^(3,infinity))` et
`K_w=||curl U||_(L^(3/2,infinity))` sont invariantes. Amplitudes et longueurs
se transforment comme `A->rho A`, `R,D->R/rho,D/rho`; ainsi
`a(b-a)RD`, `A^2RD`, `K_uK_w`, `AR/K_u`, `D/R` et `K_u/K_w` sont critiques.

# AFFIRMATIONS AJOUTÉES OU MODIFIÉES

Ajout de `NS-PURE-SWIRL-PERSISTENT-BRIDGE-DIAMETER`, statut
`COMPUTATION_ONLY`, revue `adversarial_pass`. Si un diamètre axial `D`
persiste presque partout sur `(a,b)`, alors
`a(b-a)RD<=9K_uK_w/(8pi)`. Un pont restant au-dessus du cutoff `A` vérifie
`A^2RD<=9K_uK_w/(2pi)<=(3/2)K_uK_w`. Le registre compte 73 claims.

# PREUVE / SOURCE / CALCUL

Dayrens–Masnou–Novaga–Pozzetta (`NS-SRC-0163`, publié) donnent
`2 diam(E^1)<=P_2(E)` pour une composante M-indécomposable. Coaire,
additivité des périmètres, annulation exacte du jacobien cylindrique par
`R/r` et intégration faible-`L^(3/2)` donnent la constante `9/(8pi)`.
Carr–Snoeyink–Axen et Edelsbrunner–Letscher–Zomorodian fournissent seulement
le bookkeeping discret des fusions. Cinq sources sont ajoutées; corpus à 167.

# ÉCART AVEC LE PROBLÈME CLAY

Le résultat est statique, pure-swirl, annulaire et scalaire en section
méridienne. Le calibrage `AR>=kappa K_u` n'est pas automatique pour la
composante sélectionnée; une fusion tardive peut persister sur une fenêtre
d'amplitude évanescente. Chevauchements de curls, composante poloïdale,
pression, projection de Leray, diffusion, stretching, compacité temporelle,
Type II et sélection de `R(t)->0` restent absents.

# TEST ADVERSE ET RÉSIDU CERTIFIÉ

Le certificat principal parcourt 1 035 familles et 5 197 assertions
rationnelles : zéro échec, résidu arithmétique exact nul. La réplication
indépendante ajoute 240 contrôles et résidu nul. Pour
`delta=L^-1`, `eta=L^-3/2`, le curl tronqué reste borné mais le cube du curl
original croît comme `L^3`. Empreinte principale
`d4be10a24de48f196a64515b1f1fc9916c51b51332244f50e443cefc326be946`.
Aucun résidu PDE ni lissage intervalle-certifié n'est revendiqué.

# ARTEFACTS MIS À JOUR

Un claim, rapport principal, trois revues, expérience, cinq sources,
catalogue/audit/veille, état de l'art, carte, graphe, questions, registre
supercritique, deux échecs, backlog formel, contexte, décisions et todo. Les
quatre validations contractuelles, le certificat principal et sa réplication
réussissent; aucun historique externe n'est réécrit.

# ÉTAT : CONTINUER / RÉVISER / ABANDONNER / À REPRENDRE

CONTINUER vers le calibrage local ou la retroncature par arbre de fusion.
ABANDONNER le pont à persistance relative fixe et l'inférence
`niveau global -> AR>=kappa K_u` pour chaque goutte. À REPRENDRE pour
chevauchements, dynamique Type I/II et passage au problème Clay.

# PROCHAINE EXPÉRIENCE DÉCISIVE

Construire un merge tree enrichi exact pour des gouttes d'amplitudes et
volumes dyadiques : stocker intervalle de persistance, diamètre essentiel,
budget coaire et endpoints locaux. Décider par arithmétique rationnelle si
toute branche non calibrée admet un niveau de coupe conservant un rapport
endpoint uniforme dans des composantes de diamètre `O(R)`, ou produire une
famille explicite qui réfute cette dichotomie.
