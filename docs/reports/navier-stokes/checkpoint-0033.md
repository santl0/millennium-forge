# DÉCISION DU CYCLE

Retenir la troncature presque optimale et la compensation conique, score
`20/20`. Fermer les profils pure-swirl dont le diamètre axial est `O(R)` et
activer `GAP-AXIALLY-DISPERSED-PURE-SWIRL-SELECTION`; abaisser l'argument par
degré seul, qui ne contrôle ni masse ni rayon.

# ÉQUATION ET TYPE DE SOLUTION

Référence : Navier–Stokes incompressible non forcé sur `R3`, viscosité
`nu>0`. Objet effectivement traité à temps fixé : donnée lisse compacte
divergence-free `U=(R/r)F(r,z)e_theta`, avec
`supp F subset {R/2<r<3R/2, |z-z_0|<Lambda R}`. Aucune trajectoire, pression,
solution stationnaire ou solution ancienne n'est construite.

# ÉCHELLE DES QUANTITÉS

Sous `U_mu(x)=mu U(mu x)`, `W_mu=mu^2 W(mu x)`, les normes
`K_u=||U||_(L^(3,infinity))`, `K_w=||W||_(L^(3/2,infinity))`, leur rapport et
`MO_B` sont invariants; `R` et le rayon de la boule sont divisés par `mu`. Le
poids `|log r_B|` n'est pas homogène et diverge sous concentration.

# AFFIRMATIONS AJOUTÉES OU MODIFIÉES

Ajout de `NS-BOUNDED-CROSS-SECTION-DIRECTION-GATE`, statut
`COMPUTATION_ONLY`, passe contradictoire `adversarial_pass`. Pour toute
extension `L1` de `W/|W|`, une vraie boule de rayon
`R sqrt(Lambda^2+9/4)+0+` vérifie
`MO_B>=c(Lambda^2+9/4)^(-3/2)(K_u/K_w)^6`. Ajout de `FAIL-NS-0065` et du
verrou axial dispersé.

# PREUVE / SOURCE / CALCUL

La preuve interne chaîne niveau presque optimal, scission signée, weak HLS
plan, coaire/isopérimétrie, identité cylindrique `||W_G||_1=2pi R TV(G)`,
moyenne nulle du curl, sélection de masse conique et compensation Lorentz.
Hopf, Amann, Brezis–Nirenberg Part II et Whitney sont ajoutés comme outils
`NS-SRC-0136`–`0139`; ils ne sourcent pas la borne quantitative. Le corpus
atteint 139 sources.

# ÉCART AVEC LE PROBLÈME CLAY

Le résultat est cinématique, axisymétrique, pure-swirl, séparé de l'axe et
suppose un diamètre axial uniforme. Il ne contrôle ni dispersion
multi-échelle, composante poloïdale, pression non locale, stretching,
diffusion, temps maximal, compacité d'une suite de blow-up ou théorème de
rigidité. Il n'implique donc ni régularité globale ni blow-up admissible.

# TEST ADVERSE ET RÉSIDU CERTIFIÉ

Le certificat exécute 2 884 contrôles rationnels exacts sur échelles, coques
minces, retours antipodaux rares et cellules séparées : zéro échec, empreinte
`4759238f59a46f64f0a547881f8aeb86ca6755ceea06c4a1728648db57847f8f`.
Trois passes IA séparées valident la chaîne bornée, corrigent la perte de vraie
boule de `Lambda^-1` à `Lambda^-3`, et réfutent une minoration fondée sur deux
directions antipodales seules. Le proxy BMO torique n'est pas certifié par
intervalles et aucune revue humaine externe n'est disponible.

# ARTEFACTS MIS À JOUR

Claim, rapport principal, trois revues, expérience, catalogue et audit des
sources, veille, état de l'art, carte de recherche, graphe de dépendances,
registre supercritique, questions, échecs, backlog formel et journaux de
contexte/décision. Les commits sont petits et la branche de travail est
poussée; `main` local reste intact. Aucune pull request n'est possible tant
que le remote ne publie pas une branche de base distincte.

# ÉTAT : CONTINUER / RÉVISER / ABANDONNER / À REPRENDRE

CONTINUER sur la sélection d'une cellule hétérogène; ABANDONNER les plateaux,
retours rares et superpositions confinés dans une tranche `O(R)` comme
échappements simultanés aux gates. La suppression de la borne de diamètre est
À REPRENDRE.

# PROCHAINE EXPÉRIENCE DÉCISIVE

Construire la fonction de distribution exacte d'une famille de cellules
hétérogènes `(V_j,R_j,S_j)` et décider si les deux endpoints globaux forcent
une cellule avec rapport local non dégénéré. Un exemple gardant les gates
globaux alors que tout rapport local tend vers zéro réfuterait la sélection et
imposerait un ledger collectif non local.
