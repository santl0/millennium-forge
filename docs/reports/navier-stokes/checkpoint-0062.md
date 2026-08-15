# DÉCISION DU CYCLE

Sélection du contre-test PDE exact, noté `20/20`, devant un défaut de Haar
critique (`16/20`) et une coercivité triadique directe (`15/20`). La
cohérence universelle de signe des numérateurs modaux est réfutée par deux
mécanismes indépendants. Le verrou est révisé vers l'invariance dynamique
d'un cône modal, puis un pivot intrinsèque en cas d'échec.

# ÉQUATION ET TYPE DE SOLUTION

Champ vectoriel renormalisé incompressible 3D sur `R3`, sans frontière,
viscosité un et force extérieure nulle :
`d(Z)=Delta Z-P div(Z tensor Z)-kappa(1+y dot nabla)Z`. Les champs tests sont
réels, divergence-free et de Schwartz, donc données admissibles pour la
théorie forte locale. Le calcul est instantané : aucune solution ancienne,
suitable, Type I ou trajectoire globale n'est construite.

# ÉCHELLE DES QUANTITÉS

Sous `Z_lambda(y)=lambda Z(lambda y)`, le Gram modal
`||mathcal RZ_m||²` porte `lambda^-1`, le numérateur convectif `lambda` et le
numérateur de drift `lambda^-1`. La vitesse convective porte `lambda²`; la
vitesse de drift est invariante. Le drift renormalisé fixe une échelle, donc
le numérateur complet n'a pas une homogénéité unique lorsque `kappa!=0`.

# AFFIRMATIONS AJOUTÉES OU MODIFIÉES

Ajout de `NS-TYPE-I-INSTANTANEOUS-MODAL-SIGN-COUNTEREXAMPLE`, statut
`COMPUTATION_ONLY`, revue `adversarial_pass`. Le claim d'enveloppe métrique
précise maintenant que le cycle 0062 réfute le signe instantané universel,
pas une contrainte dynamique d'orbite critique. Ajout de `FAIL-NS-0098`. Le
registre atteint 103 claims. Ajout de `NS-SRC-0225` à `NS-SRC-0227`; le
corpus atteint 227 sources.

# PREUVE / SOURCE / CALCUL

La diffusion satisfait `C_m^diff=0`; Leray est retiré seulement dans
l'appariement global avec `mathcal RZ_m` divergence-free; le drift est la
forme signée `-kappa m<(y dot nabla)Z_m,J_mZ_m>`; la convection sélectionne
`k+l=m` sans signer la phase. Waleffe et Yeung--Chu--Schmidt annulent des
transferts radiaux collectifs, Charnyi et al. testent le moment angulaire
contre `x cross e_i`, et Pineau--Vicol v2 conservent un couplage tangent RSS :
aucune source ne donne `C_m=0` ou `sum C_m=0`.

# ÉCART AVEC LE PROBLÈME CLAY

Le contre-exemple appartient à l'espace des données lisses instantanées,
mais rien ne le prolonge en solution ancienne capturée, uniformément
faible-`L3`, Type I ou minimale. La réduction SO(2) continue est propre à
`R3` et ne se transpose pas globalement au tore cubique. Type II, axe mobile,
suitability, capture et rigidité RSS intermédiaire restent ouverts.

# TEST ADVERSE ET RÉSIDU CERTIFIÉ

La triade `m=1,2,3` donne
`C=(-8/9,16/9,-16/3)*(pi/3)^(3/2)`, diffusion et drift nuls. La famille
`m=1,3` donne à `kappa=1`
`C=(7/2,-99/2)*(pi/2)^(3/2)`, diffusion et convection nulles. Une famille
`m=1,2` échoue sur 576 orientations avec `C_2=2C_1`. Le certificat passe
1201 assertions `Fraction`; divergence, isotypie et appariements annoncés
ont un résidu exactement nul. Empreinte :
`41bd221e7408fc1b02a2bc93ee6d08abe61e4e3533ba09eca1dbb5c7d3dedca4`.

# ARTEFACTS MIS À JOUR

Rapport principal, trois revues indépendantes, claim JSON, certificat exact
et résultats, catalogue/audit des sources, état de l'art, graphe de preuve,
questions ouvertes, registres supercritique/échecs/expériences, backlog
formel et mémoire de gouvernance. Validations réussies : contrat du dépôt,
103 claims, six prompts, 227 sources uniques, expérience 0062 et
`git diff --check`. Commits : `b2f1714`, `43ad8a0`, `7ccc9ad`, `c798736`.

# ÉTAT : CONTINUER / RÉVISER / ABANDONNER / À REPRENDRE

RÉVISER. Le signe universel instantané est abandonné. Une contrainte
dynamique propre aux orbites critiques reste falsifiable. Aucune résolution
Clay, borne globale ou construction de blow-up n'est revendiquée.

# PROCHAINE EXPÉRIENCE DÉCISIVE

Dériver exactement `dC_m/ds` le long du champ vectoriel renormalisé, y
compris dérivée de la tangente et projection de Leray. Construire une donnée
sur la frontière d'un cône modal unilatéral et chercher une dérivée sortante.
Un franchissement réfutera l'invariance locale du cône; une tangence
systématique isolera un lemme dynamique. Après cet échec distinct, pivoter
vers un défaut de Haar critique intrinsèque ou la rigidité RSS faible-`L3`
à rotation intermédiaire.
