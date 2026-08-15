## DÉCISION DU CYCLE

Composer le théorème de concentration Type I publié de Barker–Prange avec
l'inclusion exacte faible-`L3` vers `L2` local. Score `18/20`, devant le
contre-profil statique (`16/20`) et l'inverse faible-HLS sans Type I
(`16/20`). Le verrou de capture est fermé sous borne Type I et scindé du cas
Type II.

## ÉQUATION ET TYPE DE SOLUTION

Navier–Stokes incompressible 3D non forcé sur `R3`, sans frontière,
viscosité normalisée à un. Solution de Leray–Hopf d'énergie finie, lisse sur
`(0,T_*)`, avec premier point singulier `(x_*,T_*)`. Hypothèse additionnelle
pointwise `sup_(0<t<T_*)||u(t)||_(L^(3,infinity))<=M<infinity`.

## ÉCHELLE DES QUANTITÉS

Sous `u_rho(x,t)=rho u(rho x,rho^2t)`, la quasi-norme faible-`L3`, la borne
Morrey `r^-1/2||u||_(L2(B_r))`, `M`, `gamma_w`, le quotient local/global et
`R_M(t)/sqrt(T_*-t)` sont invariants. Le rayon exact est
`R_M(t)=2sqrt((T_*-t)/S_w^*(C_MM))`, avec
`C_M=sqrt(3)(4pi/3)^(1/6)`.

## AFFIRMATIONS AJOUTÉES OU MODIFIÉES

Ajout de `NS-TYPE-I-WEAK-L3-PARABOLIC-CORE-CAPTURE`, statut
`COMPUTATION_ONLY` pour la composition interne :
`K_core>gamma_w` et `K_core/K_global>gamma_w/M` pour tout `0<t<T_*` sous les
hypothèses déclarées. Modification de `NS-SOLENOIDAL-ANNULAR-CUTOFF` : le
champ initial peut être seulement lisse et divergence-free au voisinage de la
boule externe; le corollaire Biot–Savart conserve ses hypothèses globales.
Le registre contient 78 claims canoniques.

## PREUVE / SOURCE / CALCUL

Barker–Prange, ARMA 236 (2020), théorème 2 et appendice B, fournit la
concentration Lorentz conditionnelle. La formule des couches donne
`integral_E|f|^2<=3K_3(f)^2|E|^(1/3)`, puis l'hypothèse Morrey avec
`A=C_MM`. Barker–Prange, CMP 385 (2021), est réaudité : sa croissance
logarithmique concerne `integral|u|^3`, non directement la norme `L3`.
Aucune source 2025–2026 ne ferme Type II; le catalogue reste à 179 entrées
uniques. Les validations du contrat, des 78 claims, des six prompts, du JSON
et de `git diff --check` réussissent.

## ÉCART AVEC LE PROBLÈME CLAY

La borne Type I faible-`L3` et l'existence d'un premier point singulier sont
supposées; aucune ne découle de l'énergie Clay. Le théorème n'exclut pas un
blow-up Type I, ne couvre pas Type II, ne construit pas de singularité et ne
fournit ni compacité forte, ni solution ancienne, ni rigidité. Le cutoff
localisé n'est pas une solution Navier–Stokes non forcée.

## TEST ADVERSE ET RÉSIDU CERTIFIÉ

Des profils étagés rationnels ont `K_3=1` exactement et
`L2^2=(1+q^-1+q^-2)(1-q^-N)+q^-N<3`; au cas `m=128,N=2048`, la valeur est
`2.976804041858` et l'écart `0.023195958142`. Deux paquets disjoints exacts
font tendre la fraction locale/globale vers zéro sans borne `M`. Le script
exécute 1 346 assertions exactes, zéro échec; SHA-256
`8337e0aced23e4bd815f1d759e226a41a8867c4de826932dcf261aa3f051de76`.

## ARTEFACTS MIS À JOUR

Rapport de dérivation 0041, claim de capture, claim de cutoff, certificat
Python, trois revues indépendantes, notices sources 0146–0147, carte de
recherche, graphe de preuves, état de l'art, questions ouvertes, journal
supercritique, registre des échecs, journal d'expériences, backlog formel,
contexte, décisions et tâches. Aucun fichier historique ni artefact lourd
n'est importé.

## ÉTAT : CONTINUER / RÉVISER / ABANDONNER / À REPRENDRE

CONTINUER. Le résultat positif est une fermeture conditionnelle Type I; le
claim reste interne et aucune résolution Clay n'est revendiquée.

## PROCHAINE EXPÉRIENCE DÉCISIVE

Calculer exactement l'équation de
`V(t)=chi_(R(t))u(t)-B_(R(t))(grad chi_(R(t)) dot u(t))` au rayon Type I.
Isoler la dérivée de l'opérateur de Bogovskiĭ sous homothétie, le terme
`R'(t)`, diffusion, convection, pression et force annulaire; certifier toutes
les puissances d'échelle et tenter de faire diverger la norme critique de la
force par un profil adverse.
