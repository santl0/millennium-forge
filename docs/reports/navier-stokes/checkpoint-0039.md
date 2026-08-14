# DÉCISION DU CYCLE

Retenir le contre-profil lisse `Z_n,-Z_n`, score `20/20`, devant l'agrégation
commune axe–anneau (`17/20`) et la décomposition ondelette (`15/20`). Fermer
`GAP-OVERLAPPING-CURL-CANCELLATION` négativement pour les sommants étiquetés,
positivement par agrégation dans la géométrie commune, et activer
`GAP-MULTIAXIS-TOTAL-FIELD-LOCALIZATION`.

# ÉQUATION ET TYPE DE SOLUTION

Référence : Navier–Stokes incompressible non forcé sur `R3`, viscosité
`nu>0`. Objet effectivement traité : champs statiques pure-swirl, lisses,
compacts, divergence-free, dans un anneau commun; aucune solution en temps,
pression, force, singularité, solution ancienne ou Leray–Hopf n'est
construite. La veille `NS-SRC-0175` concerne séparément un système forcé dans
un cylindre à frontière mixte.

# ÉCHELLE DES QUANTITÉS

Sous `U_rho(x)=rho U(rho x)` et
`curl U_rho=rho^2 curl U(rho x)`, les quasi-normes
`L^(3,infinity)` et `L^(3/2,infinity)`, leur rapport, la multiplicité et
l'identité d'annulation sont invariants. Pour le témoin à rayon `R`, volume
`~R^3` et curl `~n/R` donnent encore un rapport local `O(n^-1)`.

# AFFIRMATIONS AJOUTÉES OU MODIFIÉES

Ajout de `NS-BOUNDED-MULTIPLICITY-OVERLAP-SELECTION`, statut `REFUTED`, revue
`adversarial_pass`. Une minoration positive du rapport d'un sommant par le
rapport total et la multiplicité deux n'existe pas. Le registre compte 75
claims. La réparation même axe–rayon–anneau est une identité d'agrégation,
pas un claim Clay.

# PREUVE / SOURCE / CALCUL

Le témoin lisse de volume exact `4pi^2/3` force les curls individuels à croître
comme `n`, tandis que le total reste le fond fixe `B`. Deux calculs exacts
reproduisent l'algèbre des fonctions de distribution. La veille ajoute
`NS-SRC-0172`–`0175` : frontière `q<infinity` des bases ondelettes, théorie
Littlewood–Paley, ondelettes divergence-free et prépublication forcée récente;
corpus à 175 sources.

# ÉCART AVEC LE PROBLÈME CLAY

Le résultat est une obstruction cinématique à une stratégie de preuve, pas
un blow-up ni un critère de prolongement. Pour plusieurs axes, aucun potentiel
méridien total unique n'est disponible. Cutoff divergence-free, curl de col,
projection non locale de Leray, pression, diffusion, stretching, compacité
temporelle, rayon `R(t)->0`, Type II et cas périodique général restent absents.

# TEST ADVERSE ET RÉSIDU CERTIFIÉ

Le certificat principal exécute 344 121 assertions `Fraction` sur 20 445
modèles, fréquences `8..4096`, cinq scalings et suite dyadique jusqu'à `2^40` :
zéro échec, résidu pointwise nul, empreinte
`1ee45f22210ad7fd5ff11c20d2e09a31b0b081a4b8dbac62d7ac10214bbfbecb`.
La réplication indépendante exécute 1 216 assertions exactes, résidu nul,
empreinte `90f25bb65f13db51e8350065bbbbaf4085ad49d07020b303a5cc3a96f53353a8`.
Aucun résidu PDE ni passage calcul–continuum n'est revendiqué.

# ARTEFACTS MIS À JOUR

Un claim, rapport principal, trois revues, expérience, quatre sources,
catalogue et audit bibliographique, état de l'art, carte, graphe, questions,
registre supercritique, échec `FAIL-NS-0075`, backlog formel, contexte,
décisions, todo et ce checkpoint. Les validations contractuelles, les deux
certificats et `git diff --check` sont exécutés avant le checkpoint Git.

# ÉTAT : CONTINUER / RÉVISER / ABANDONNER / À REPRENDRE

CONTINUER vers une localisation intrinsèque multi-axe du champ total. RÉVISER
les carrés-fonctions seulement sous coercivité anti-annulation explicite.
ABANDONNER la sélection universelle parmi sommants arbitraires et la base
norm-convergente du plein faible-Lorentz. À REPRENDRE pour la pression, le
temps, Type I/II et le raccord Clay.

# PROCHAINE EXPÉRIENCE DÉCISIVE

Construire deux paquets pure-swirl lisses à axes distincts puis localiser leur
champ total par cutoff et projection de Leray. Mesurer exactement ou borner par
intervalles le curl de col, la correction non locale, la matrice de Gram et le
rapport critique dans chaque boule. Soit une règle canonique conserve une
cellule avec constante suivie, soit un contre-profil multi-axe réfute ce
premier candidat de localisation intrinsèque.
