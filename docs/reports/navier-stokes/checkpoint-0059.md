# DÉCISION DU CYCLE

Sélection de la projection de la dérivée PDE sur la tangente SO(2) dans un
Hilbert négatif, notée `19/20`, devant la tranche à gabarit fixe (`17/20`) et
la synchronisation directe de phases locales (`15/20`). La borne du défaut
canonique est fermée. La stabilité du coefficient, la reconstruction d'une
phase et la stationnarité automatiques sont abandonnées.

# ÉQUATION ET TYPE DE SOLUTION

Navier--Stokes incompressible 3D renormalisé sur `R3 x J`, `J` borné, sans
frontière, viscosité un et drift `kappa(1+y dot nabla)`, `kappa>0`. Le cutoff
extérieur est localement contrôlé; la limite et Clay sont non forcés. Le
ledger utilise l'équation vectorielle complète, la pression de Riesz et des
représentants de Bochner. L'endgame reste conditionné à une limite suitable,
faible-`L3` globale et capturée.

# ÉCHELLE DES QUANTITÉS

La vitesse `beta_n` est sans dimension en temps similaire, mais dépend de la
métrique, de la fenêtre et de l'exhaustion. Les `H^-3(B_m)` sont locaux et
sous-critiques; pour une force physique, le facteur homogène est
`lambda^(-3/2)`. Les poids
`w_m=2^-m/(1+D_m²+G_m²)` sont fixes et la récupération sur `B_m` coûte
exactement `w_m^(-1/2)`. Aucune uniformité en rayon n'est cachée.

# AFFIRMATIONS AJOUTÉES OU MODIFIÉES

Ajout de `NS-TYPE-I-CANONICAL-HILBERT-PHASE-COLLAPSE`, statut
`COMPUTATION_ONLY`, revue `adversarial_pass`. Le registre contient 99 claims.
Ajout de `FAIL-NS-0095`, qui réfute phase stable, intégrabilité temporelle et
stationnarité depuis la seule projection tangentielle. Le verrou actif devient
`GAP-TYPE-I-HAAR-DEFECT-DECAY-OR-RSS-RIGIDITY`.

# PREUVE / SOURCE / CALCUL

Les familles compatibles de `H^-3(B_m)` forment un sous-espace fermé de la
somme pondérée; les restrictions et la forte mesurabilité sont contrôlées.
Avec `d_n=partial_sZ_n`, `g_n=mathcal RZ_n` et
`beta_n=<d_n,g_n>/||g_n||²`, Pythagore donne
`||beta_ng_n||²+||r_n||²=||d_n||²`. Ainsi
`ess inf|beta_n|->infinity` impose `mathcal RZ=0`. Beyn--Thümmler (`0209`),
Rowley--Marsden (`0220`) et Willis--Cvitanović--Avila (`0221`) fixent les
antécédents de phase/connexion et leurs non-transferts. Le corpus atteint 221
sources.

# ÉCART AVEC LE PROBLÈME CLAY

La projection ne prouve ni la divergence de la vitesse canonique, ni
`mathcal A r_n->0`, ni l'intégrabilité de `beta_n`. Elle ne crée pas la forte
compacité du stress, la suitability, la capture ou une rigidité axisymétrique
avec swirl. Elle dépend d'une métrique sous-critique et ne traite pas Type II,
les axes mobiles ou une singularité Clay arbitraire.

# TEST ADVERSE ET RÉSIDU CERTIFIÉ

Le certificat vérifie exactement orthogonalité, Pythagore, minimisation et
contraction. Un Gram `N^-2` rend `beta_N=N` mal conditionné; le modèle
`Z_N(s)=s e_0+N^-2Q_(Ns)e_1` a `mathcal RZ_N->0` et
`beta_N mathcal RZ_N->0`, mais `mathcal A r_N=e_0` et une limite non
stationnaire. Le script passe 37763 assertions rationnelles, résidu nul, sans
PDE numérique ni arrondi, empreinte
`e20050eecda07b8776b3a420a5b69b7a149c38bcb2117759330eb661109885b4`.

# ARTEFACTS MIS À JOUR

Rapport principal, trois revues indépendantes, certificat exact, claim JSON,
deux notices primaires, graphe de dépendances, état de l'art, questions
ouvertes, journaux supercritique/échecs/expériences, backlog formel et mémoire
de gouvernance. Validation réussie : contrat du dépôt, 99 claims, six prompts,
expérience 0059 et trois régressions 0056--0058, catalogue de 221 sources,
puis `git diff --check`. Commits scientifique et normalisation d'évidence :
`b7166d0`, `0a7c956`.

# ÉTAT : CONTINUER / RÉVISER / ABANDONNER / À REPRENDRE

CONTINUER. Le projecteur tangent canonique pour une métrique épinglée est
conservé. L'inférence de stationnarité et la reconstruction automatique d'une
phase sont abandonnées. Aucune condition terminale globale n'est atteinte.

# PROCHAINE EXPÉRIENCE DÉCISIVE

Appliquer la moyenne de Haar à l'équation renormalisée complète, recalculer
le stress et la pression moyens, puis tester si dissipation, asymptotique
ancienne ou capture peuvent forcer
`partial_s mathcal A Z_n=mathcal A r_n->0`. Après trois mécanismes PDE
réellement distincts en échec, documenter l'obstacle et pivoter vers la
rigidité RSS faible-`L3` intermédiaire.
