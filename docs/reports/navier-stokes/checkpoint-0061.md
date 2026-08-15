# DÉCISION DU CYCLE

Sélection de la décomposition isotypique et de l'enveloppe métrique, notée
`20/20`, devant une coercivité PDE directe (`16/20`) et le pivot RSS
intermédiaire (`14/20`). La vitesse canonique est une moyenne convexe des
vitesses modales; son interprétation intrinsèque est réfutée. Le programme
pivote vers un test PDE de cohérence de signe ou un défaut d'axisymétrie
indépendant de la métrique.

# ÉQUATION ET TYPE DE SOLUTION

Pipeline Navier--Stokes incompressible 3D renormalisé sur `R3 x J`, sans
frontière, viscosité un, drift `kappa(1+y dot nabla)`, force de cutoff
localement évanescente et pression globale de Riesz. Les approximants sont
classiques; la limite conditionnelle est faible adaptée locale puis ancienne
suitable. Le lemme modal et son contre-test sont hilbertiens et ne résolvent
pas cette PDE.

# ÉCHELLE DES QUANTITÉS

Dans le temps similaire, `partial_sZ` et `mathcal RZ` ont le même poids;
`beta`, `beta_m` et les poids modaux normalisés sont sans dimension. Les
Grams `G_m=||mathcal RZ_m||²` dépendent du Hilbert local `H^-3`, de
l'exhaustion et de ses poids : ils ne sont pas invariants sous l'échelle
Clay. Les projecteurs azimutaux commutent avec les dilatations centrées sur
le même axe.

# AFFIRMATIONS AJOUTÉES OU MODIFIÉES

Ajout de `NS-TYPE-I-MODAL-METRIC-CONVEX-HULL`, statut `COMPUTATION_ONLY`,
revue `adversarial_pass`. Modification du claim de phase canonique : son
collapse reste valide pour une métrique épinglée, mais `FAIL-NS-0097` réfute
l'intrinsécité de la prémisse rapide. Le registre atteint 102 claims. Ajout
de `NS-SRC-0224`; le corpus atteint 224 sources.

# PREUVE / SOURCE / CALCUL

La décomposition réelle donne `mathcal R|H_m=mJ_m` et
`beta_omega=sum omega_mG_mbeta_m/sum omega_mG_m`. L'infimum pointwise sur
tous les poids scalaires est la distance de zéro à l'enveloppe convexe des
vitesses actives; une borne robuste exige un signe commun et un gap modal.
Fedele--Abessi--Roberts 2015 écrit la formule finie analogue pour un scalaire
passif en pipe flow. Pineau--Vicol v2 reste limité aux profils RSS exacts,
Type I et rotations extrêmes.

# ÉCART AVEC LE PROBLÈME CLAY

Aucune loi Navier--Stokes ne produit encore un signe commun des
`<partial_sZ_m,mathcal RZ_m>`, et les triades couplent les modes. Le
contre-test n'est ni un champ 3D divergence-free ni une solution. Pression,
suitability, capture, borne faible-`L3` globale et passage au continuum
restent requis. Type II, axe mobile et rotation RSS intermédiaire ne sont pas
traités.

# TEST ADVERSE ET RÉSIDU CERTIFIÉ

Dans `R2 direct sum R2`, `mathcal R=J direct sum 2J`, deux isotypes de Grams
unitaires et vitesses `+N,-N` donnent `beta_(1,1)=0` et
`beta_(2,1)=N/3` sous deux métriques fixes de conditionnement relatif deux.
Le certificat passe 1809 assertions `Fraction`; erreurs de reconstruction et
d'orthogonalité exactement nulles, sans graine, discrétisation ni flottant.
Empreinte :
`e38b2c7ff22c0821b28c71b2067543a2c5cd186362db88bb7b5039df44cafbe3`.

# ARTEFACTS MIS À JOUR

Rapport principal, trois revues indépendantes, nouveau claim JSON, claim de
phase corrigé, certificat exact et résultats, catalogue/audit des sources,
état de l'art, graphe de dépendances, questions ouvertes, registres
supercritique/échecs/expériences, backlog formel et mémoire de gouvernance.
Validations réussies : contrat du dépôt, 102 claims, six prompts, 224 sources
uniques, expérience 0061 et `git diff --check`. Commits : `c6091b0`,
`78b1c63`, `723a082`.

# ÉTAT : CONTINUER / RÉVISER / ABANDONNER / À REPRENDRE

RÉVISER. Le collapse dans une métrique fixée est conservé. La production
automatique d'une grande vitesse métriquement robuste est abandonnée. Aucune
résolution Clay complète n'est revendiquée.

# PROCHAINE EXPÉRIENCE DÉCISIVE

Construire un champ de Schwartz divergence-free à au moins deux modes
azimutaux et calculer exactement
`d=Delta Z-P div(Z tensor Z)-kappa(1+y dot nabla)Z`. Séparer diffusion,
drift, pression de Leray et triades dans chaque numérateur modal. Deux signes
opposés élimineront une cohérence PDE universelle; un signe survivant sur une
famille adverse isolera un lemme coercif à démontrer.
