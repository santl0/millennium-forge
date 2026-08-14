# DÉCISION DU CYCLE

Abandonner comme échappement toute superposition pure-swirl dont l'aire
méridienne est `o(R^2)`. Activer
`GAP-THICK-CROSS-SECTION-GRADIENT-DIRECTION`.

# ÉQUATION ET TYPE DE SOLUTION

Référence : Navier–Stokes incompressible non forcé sur `R3`, viscosité
`nu>0`. Objet audité à temps fixé : donnée lisse compacte divergence-free
`U=(R/r)F(r,z)e_theta`, `supp F subset {R/2<r<3R/2}`; aucune trajectoire,
pression ou solution stationnaire n'est construite.

# ÉCHELLE DES QUANTITÉS

`||U||_(L^(3,infinity))` et
`||curl U||_(L^(3/2,infinity))` sont invariantes sous le scaling Clay;
`S_2/R^2`, avec `S_2=|supp F|_(dr dz)`, est adimensionné et invariant.

# AFFIRMATIONS AJOUTÉES OU MODIFIÉES

Ajout de `NS-THIN-PURE-SWIRL-LORENTZ-COLLAPSE`, statut
`COMPUTATION_ONLY`, et de `FAIL-NS-0064`. Le claim affirme
`K_U<=C(S_2/R^2)^(1/6)K_W` sous les seules hypothèses géométriques déclarées.

# PREUVE / SOURCE / CALCUL

La dérivation combine potentiel bidimensionnel, weak HLS vérifié aussi par
interpolation réelle, inclusion faible sur support fini et comparaisons
cylindriques. O'Neil et Peetre sourcent les outils; Fleming–Rishel,
Bourgain–Brezis, Van Schaftingen et Spector–Van Schaftingen sont ajoutés comme
outils primaires `NS-SRC-0132`–`0135`. Le corpus atteint 135 sources.

# ÉCART AVEC LE PROBLÈME CLAY

Le résultat est statique, axisymétrique, pure-swirl, séparé de l'axe et ne
couvre que le régime `S_2/R^2->0`. Il ne contrôle ni section épaisse,
composante poloïdale, champ non axisymétrique, pression, stretching, temps
maximal ou profil limite.

# TEST ADVERSE ET RÉSIDU CERTIFIÉ

384 masques P1 signés et décalés sur quatre maillages rationnels; 272 726
assertions exactes, zéro échec. Pire quotient carré
`4212353969604/482173039025<9`; empreinte du script
`597dc2e2828df34d836556c5419904d39e6ee240aa93b353a49683699ae40443`.
Trois passes séparées attaquent analyse fonctionnelle, contre-profils et
littérature. Le calcul fini ne certifie pas la constante HLS du continuum.

# ARTEFACTS MIS À JOUR

Claim, rapport principal, trois revues, expérience, catalogue et audit des
sources, veille, état de l'art, carte de recherche, graphe de dépendances,
registre supercritique, questions, échecs, backlog formel et journaux de
contexte/décision.

# ÉTAT : CONTINUER / RÉVISER / ABANDONNER / À REPRENDRE

CONTINUER sur le verrou épais; ABANDONNER la branche mince non séparable.
Contrat du dépôt, 65 claims canoniques, six prompts et `git diff --check`
validés; expérience exacte sans échec.

# PROCHAINE EXPÉRIENCE DÉCISIVE

Construire une famille de potentiels compacts à support épais avec extrema en
plateau et compensateurs rares; calculer les superniveaux, la capacité des
transitions et l'oscillation all-ball de
`nabla_perp F/|nabla F|`. Réfuter le lemme topologique si toute rotation peut
être confinée à capacité critique négligeable sous les deux gates endpoints.
