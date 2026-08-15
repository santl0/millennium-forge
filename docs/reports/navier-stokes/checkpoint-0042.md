## DÉCISION DU CYCLE

Sélectionner l'identité exacte du cutoff solénoïdal mobile (score `19/20`)
et abandonner la petitesse déduite du seul support contractant. Le verrou
devient la borne critique de la force projetée complète, avant toute rigidité
ancienne forcée.

## ÉQUATION ET TYPE DE SOLUTION

Navier–Stokes incompressible 3D non forcé, viscosité un, domaine `R3`, sans
frontière. La dérivation suppose `u,p` classiques avant `T_*`; l'application
conditionnelle part d'une solution de Leray–Hopf lisse avant son premier temps
singulier et bornée uniformément dans faible-`L3`.

## ÉCHELLE DES QUANTITÉS

`u_R=R^-1U`, `p_R=R^-2P`, force `f_R=R^-3F`. La norme spatiale `L1` de la
force est invariante, sa norme faible-`L^(3/2)` croît comme `R^-1` et sa norme
`Hdot^-1` comme `R^-1/2`. Les couples espace-temps critiques vérifient
`2/q+3/p=3`; pour `q<infini`, un profil persistant accumule un logarithme.

## AFFIRMATIONS AJOUTÉES OU MODIFIÉES

- `NS-MOVING-SOLENOIDAL-CUTOFF-FORCED-EQUATION` — `COMPUTATION_ONLY` :
  conjugaison, dérivée temporelle et PDE forcée exactes.
- `NS-SHRINKING-MOVING-CUTOFF-SMALLNESS` — `REFUTED` : `R(t)->0` ne rend pas
  le terme de frontière mobile petit dans la norme critique `L1`.

Le registre contient 80 claims canoniques validés.

## PREUVE / SOURCE / CALCUL

La dérivation principale est recoupée par trois passes séparées : audit
analytique, contre-profil et veille primaire. Le catalogue ajoute
`NS-SRC-0180`–`0184` et atteint 184 sources : inverse de divergence mobile,
pression locale, domaine physique mobile et blow-up forcé. Aucune source ne
fournit l'annulation critique manquante.

## ÉCART AVEC LE PROBLÈME CLAY

Le champ localisé satisfait une équation **forcée** et non l'équation Clay
non forcée. La projection de Leray rend la force solénoïdale mais non locale.
Ni compacité forte, ni limite ancienne admissible, ni théorème de rigidité
pour la force critique ne sont obtenus. Le cas Type II reste séparé.

## TEST ADVERSE ET RÉSIDU CERTIFIÉ

Le témoin pure-swirl lisse annule exactement le correcteur de Bogovskii mais
vérifie, en `y_0=(3/2,0,0)`,
`R^3(partial_t chi_R)u_R=(0,-9c^2/4,0)`. Le script déterministe valide 499
assertions rationnelles, zéro échec. Résidu scientifique : le témoin n'est
pas une trajectoire Navier–Stokes et ne réfute pas une annulation de la force
complète imposée par la PDE.

## ARTEFACTS MIS À JOUR

Rapport et trois revues du cycle 0042; deux claims JSON; script
`moving_cutoff_audit.py`; catalogue et audit des sources; état de l'art,
carte de recherche, questions ouvertes, graphe de preuve, journal
supercritique, expériences, échecs, backlog formel et mémoire du laboratoire.
Validations : expérience exacte, contrat du dépôt, claims, prompts et
whitespace Git.

## ÉTAT : CONTINUER / RÉVISER / ABANDONNER / À REPRENDRE

CONTINUER sur `GAP-TYPE-I-MOVING-COMMUTATOR-BOUND`; ABANDONNER la petitesse
fondée uniquement sur `R(t)->0`; garder `GAP-TYPE-I-FORCED-RIGIDITY` en aval.

## PROCHAINE EXPÉRIENCE DÉCISIVE

Fixer une formule intégrale support-lisse de Bogovskii sur la couronne unité,
calculer `[Delta,Q]U_N` et `[D,Q]U_N` pour
`U_N=epsilon phi(r,z)sin(Nz)e_theta`, puis déterminer si le terme principal
en `N` survit dans la force projetée complète en
`L1+div L^(3/2,infinity)`.
