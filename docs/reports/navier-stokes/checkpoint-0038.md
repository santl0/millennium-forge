# DÉCISION DU CYCLE

Retenir la sélection adaptative directe, score `20/20`, devant le merge tree
certifié (`17/20`) et la retroncature récursive (`15/20`). Le niveau moyen de
coaire et la composante endpoint sont choisis au même niveau; fermer
`GAP-BRIDGE-SCALE-CALIBRATION-OR-MERGE-TREE` dans la classe pure-swirl
annulaire à supports complets disjoints et activer
`GAP-OVERLAPPING-CURL-CANCELLATION`.

# ÉQUATION ET TYPE DE SOLUTION

Référence : Navier–Stokes incompressible non forcé sur `R3`, viscosité
`nu>0`. Objet effectivement traité : donnée lisse compacte divergence-free
pure-swirl `U=(R/r)F e_theta` et son curl à un temps fixé, puis famille
disjointe de telles cellules. Aucune solution en temps, pression, singularité,
solution ancienne ou solution de Leray–Hopf n'est construite.

# ÉCHELLE DES QUANTITÉS

Sous `U_rho(x)=rho U(rho x)`, `K=||U||_(L^(3,infinity))`,
`H=||curl U||_(L^(3/2,infinity))`, `q=K/H`, `lambda R`, `K^2/H`,
`diam_z/R`, `K_beta/K` et `q_beta` sont invariants. Toutes les bornes du
claim sont critiques.

# AFFIRMATIONS AJOUTÉES OU MODIFIÉES

Ajout de `NS-PURE-SWIRL-ADAPTIVE-DIAMETER-SELECTION`, statut
`COMPUTATION_ONLY`, revue `adversarial_pass`. Il donne
`lambda R>=K^2/(432H)`, `diam/R<=2 239 488q^-3`,
`K_beta>=(C_I/20 736)K^2/H` et `q_beta>=(C_I/20 736)q^2`. Le registre compte
74 claims. Deux inférences sont consignées comme réfutées : héritage du
rapport sous retroncature et coercivité d'un merge tree sans registre coaire.

# PREUVE / SOURCE / CALCUL

Coaire, isopérimétrie R3, périmètre–diamètre planaire, identité exacte du curl
et intégration faible-Lorentz donnent le lemme. Quatre sources primaires sont
ajoutées sur stabilité de persistance, merge trees, graphes de Reeb et
analogue Navier–Stokes 2D; corpus à 171. Elles ne contiennent pas la
composition nouvelle. Trois audits IA séparés valident les constantes,
réfutent le bookkeeping topologique seul et distinguent barcode de maximin.

# ÉCART AVEC LE PROBLÈME CLAY

Le résultat est statique, annulaire, axisymétrique pure-swirl et suppose les
supports cellulaires complets disjoints. Pour des curls superposés, les
annulations peuvent détruire la domination locale avant la fonction de
distribution. Projection de Leray, pression, diffusion, stretching, temps
maximal, compacité, sélection `R(t)->0`, Type II et cas périodique général
restent absents.

# TEST ADVERSE ET RÉSIDU CERTIFIÉ

Le certificat principal exécute 12 243 assertions `Fraction` sur 2 016
registres et 24 profondeurs : zéro échec, résidu exact nul, empreinte
`0f607fc228c6c552b323b0b342bfa83356afde2dff61831fe606c0e20a1e235e`.
La réplication dyadique indépendante exécute 9 513 assertions sur toutes les
retroncatures : résidu nul. Elle réfute le merge tree seul mais viole
explicitement le coût coaire des feuilles; aucun résidu PDE n'est revendiqué.

# ARTEFACTS MIS À JOUR

Un claim, rapport principal, trois revues, expérience, quatre sources,
catalogue/audit/veille, état de l'art, carte, graphe, questions, registre
supercritique, deux échecs, backlog formel, contexte, décisions, todo et ce
checkpoint. Les validations contractuelles, les certificats exacts et
`git diff --check` réussissent. Aucun historique externe n'est réécrit.

# ÉTAT : CONTINUER / RÉVISER / ABANDONNER / À REPRENDRE

CONTINUER vers les annulations de curls superposés. ABANDONNER l'héritage
endpoint récursif et le barcode/merge tree sans registre analytique.
À REPRENDRE pour projection de Leray, dynamique Type I/II et passage au
problème Clay.

# PROCHAINE EXPÉRIENCE DÉCISIVE

Construire deux cellules pure-swirl lisses dont les supports de vitesse sont
identifiables mais dont les curls se recouvrent avec signes opposés. Suivre
exactement les fonctions de distribution du curl individuel et total, la
matrice de Gram des directions, le coût de cutoff et le rapport endpoint.
Soit produire une annulation critique qui détruit toute sélection locale,
soit isoler l'hypothèse minimale de multiplicité/signature qui la préserve.
