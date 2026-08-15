# Todo

## Priorité 1 — bootstrap

- [ ] Publier le dépôt GitHub public.
- [x] Installer le schéma des affirmations et sa validation CI.
- [x] Créer les six espaces de problèmes.
- [x] Ajouter les protocoles et missions autonomes versionnés.
- [ ] Importer uniquement les documents stables du laboratoire local.

## Priorité 2 — pilotes

- [ ] Brancher l'hypothèse de Riemann sur un premier graphe d'audit sourcé.
- [x] Brancher Navier–Stokes sur une première expérience reproductible.
- [ ] Relier les formulations de `LeanMillenniumPrizeProblems` sans les dupliquer silencieusement.

## Questions ouvertes

- Choix du format final des graphes de preuve : YAML, JSON-LD ou base dérivée.
- Politique de conservation des gros artefacts : Git LFS, stockage objet ou régénération.
- Processus de nomination des réviseurs spécialisés.
- Niveau de formalisation réaliste par problème.

## Navier–Stokes — prochaine reprise

- [x] Auditer à constantes suivies le commutateur localisé `(8)->(22)`.
- [x] Synchroniser `(49)->(58)` au même temps d'échappement et vérifier les
  deux branches du critère harmonique.
- [x] Tester l'extension d'une direction connue seulement sur le cœur actif
  vers la prémisse globale `bmo_phi`, zéros et multicœurs inclus.
- [x] Auditer l'admissibilité du profil critique ponctuel sous
  `div omega=0`, Biot–Savart, énergie finie, coupures et `bmo_phi` global.
- [x] Construire ou exclure un profil à direction
  `e+O(1/|log r|)` avec masse faible-`L^(3/2)` non dégénérée et résidu PDE
  sous-critique après coupure, dans la sous-classe à axe fixe, amplitude
  bornée et masse critique par bloc : exclusion cinématique au cycle 0022;
  l'échappatoire dégénérée n'est pas stationnaire.
- [x] Exclure, sous borne de tranche et masse critique par bloc, les axes
  `e(s)` dont la variation et l'erreur directionnelle sont sublinéaires;
  séparer rotation uniforme et phase logarithmique par un test BMO centré.
- [x] Exclure une cascade multicoeur sans axe global sous amplitude critique
  bornée, masse par bloc et même extension log-BMO : la fraction active
  produit un axe à variation et erreur `O(log N)` au cycle 0024.
- [x] Construire et auditer une intermittence angulaire à amplitude non
  bornée : le train sparse de forme fixe passe divergence, curl, énergie,
  faible-Lorentz, masse par bloc et Biot–Savart; le BMO global et le résidu
  stationnaire échouent au cycle 0025.
- [x] Quantifier le coût d'un blob directionnellement plat sous annulation et
  faible-`L^(3/2)` : borne conique cubique et famille mesurable sharp au cycle
  0026; l'exposant est optimal mais le modèle n'est pas un curl spatial.
- [x] Lever le compensateur rare via un premier
  `U=psi(r,z)e_theta` séparable; curl, composantes transverses, Biot–Savart et
  résidu certifiés, mais le supremum BMO all-ball est réfuté à aspect fixé.
- [x] Réaliser le lift axisymétrique séparable et suivre flux, faible-Lorentz,
  énergie, boule de calotte et résidu; aspect fixé réfuté au cycle 0027.
- [x] Tester la sharpness compacte div–curl du cube sur le domaine parent;
  variante `C_c^infinity` obtenue, mais BMO all-ball non certifié.
- [x] Construire ou borner une somme non séparable
  `psi_n=sum_j A_(n,j)(r)chi_(n,j)(z)`; mesurer à chaque niveau la capacité de
  `{|W_r|>=|W|/4}` : le rang seul est insuffisant; le lemme d'excès radial
  conditionnel est isolé et l'échappatoire torique ferme la nécessité de cette
  architecture.
- [x] Tester une paire de tores signés à impulsions opposées : impulsion,
  criticité et log-BMO conservés, axisymétrie brisée, mais
  `||u||_3^3~h/R->0` et queue `|x|^-4`; cardinal fixé abandonné.
- [x] Auditer `N_n->infinity` : normalisation des amplitudes, packing des
  corridors, moments signés et termes croisés de la vitesse `L^3`.
- [x] Tester en parallèle un ansatz de vitesse compacte divergence-free dont
  la vorticité satisfait faible-`L^(3/2)` et log-BMO : le stacking passe les
  normes critiques mais échoue au log-BMO interne; gate fonctionnel réfuté.
- [ ] Construire ou exclure un bloc compact divergence-free dont le curl a une
  oscillation active `O(1/|log r|)`, sans petitesse faible-`L^3`.
- [x] Exclure toute superposition pure-swirl séparée de l'axe dont l'aire
  méridienne est `o(R^2)` : weak HLS et support fini au cycle 0032.
- [ ] Sur la branche restante `|supp F|~R^2`, construire ou minorer une boule
  d'oscillation de `nabla_perp F/|nabla F|`; attaquer d'abord par plateaux et
  compensateurs rares.
- [x] Fermer les sections épaisses de diamètre axial `O(R)` par troncature,
  coaire et compensation conique; puissance directionnelle six au cycle 0033.
- [x] Pour des cellules axialement dispersées et hétérogènes, sélectionner un
  bloc dont le rapport endpoint local reste non dégénéré, ou construire une
  distribution exacte sans bloc dominant.
- [x] Réfuter la sélection fondée sur les seules quasi-normes par une
  distribution dyadique exacte; rétablir une sélection pour cellules épaisses
  disjointes sous registre BV uniforme au cycle 0034.
- [x] Étendre la sélection endpoint pure-swirl lorsque `|Q_j|/v_j->infinity`
  ou que les plateaux dégénèrent : bande commune et isopérimétrie R3 au cycle
  0035, sans borne axiale ni volume support.
- [x] Décomposer une bande commune en gouttelettes axialement dispersées et
  sélectionner une troncature de bon rapport : constante `C_I/648` au cycle
  0036; les filaments strictement sous `lambda/4` sont coupés sans défaut.
- [x] Construire ou exclure un pont pure-swirl mince qui reste au-dessus de
  `lambda/4`, fusionne deux gouttes distantes et conserve les deux endpoints :
  persistance fixe calibrée exclue par périmètre–diamètre au cycle 0037;
  fenêtre de fusion évanescente isolée comme seul échappement statique.
- [x] Calibrer le niveau et contrôler le diamètre sans héritage le long d'un
  arbre : sélection adaptative au même niveau, constantes `432`, `20 736` et
  `2 239 488` au cycle 0038; l'alternative récursive est réfutée.
- [x] Étendre ou réfuter le registre lorsque les supports de curl se
  chevauchent et peuvent s'annuler : sélection parmi sommants arbitraires
  réfutée à multiplicité deux au cycle 0039; agrégation même axe–anneau valide.
- [x] Construire une localisation intrinsèque statique du champ total sous
  axes multiples : cutoff de Bogovskiĭ sur couronne fixe au cycle 0040, curl
  de col et constantes géométriques suivis; pression et temps non inclus.
- [ ] À une échelle pré-singulière imposée `R(t)->0`, sélectionner une boule
  capturant une fraction uniforme de `||u(t)||_(L^(3,infinity))`, ou construire
  un contre-profil lisse multi-échelle qui réfute toute gamme candidate.
- [ ] Si cette capture survit, calculer l'équation exacte du champ localisé :
  dérivée temporelle du correcteur, diffusion, convection, force effective et
  pression non locale, avec constantes uniformes.
- [ ] Certifier numériquement l'inf-sup `p=2` sur `A_(1,h)` par deux familles
  de maillages indépendantes et bornes d'erreur; ne pas confondre cette
  expérience avec la minoration analytique forte déjà dérivée.
- [ ] Tester une hypothèse de coercivité Gram/angle sur une décomposition
  canonique de phase-espace, en exigeant qu'elle soit calculable depuis le
  champ total et stable à l'endpoint faible-Lorentz.
- [ ] Relier la cellule de bon rapport à une échelle `R_j(t)->0`; auditer
  d'abord le raccord Type I de Barker–Prange, puis le trou Type II.
- [ ] Formuler un ledger Morrey–Carleson pour des tubes hétérogènes
  `A_j,h_j,q_j`; tester si le budget faible-Lorentz force le collapse.
- [ ] Si un gate statique survit, obtenir un temps d'interaction uniforme face
  au temps diffusif `r_min^2/nu` et recalculer la pression de Leray.
- [ ] Quantifier une formulation pré-singulière cohérente par rayon de cœur
  `r_c(t)` ou convergence de profils remis à l'échelle.
- [ ] Formaliser le lemme scalaire de séparation de phases
  `MO>=4ab/(a+b)` dans un environnement épinglé.
- [ ] Formaliser la rigidité sous récurrence de dilatation du cycle 0021.
- [ ] Obtenir une revue externe indépendante du lemme du cycle 0018.

### Cycle 0041

- [x] Réauditer Barker–Prange 2020, théorème 2 et appendice B, avec hypothèse
  Morrey exacte, rayon, temps et constantes Lorentz distinctes.
- [x] Prouver et certifier l'inclusion
  `||f||_2^2<=3K_3(f)^2|E|^(1/3)` et l'optimalité de trois.
- [x] Fermer la capture relative au rayon parabolique sous borne Type I
  pointwise : `K_core/K_global>gamma_w/M`.
- [x] Réfuter la fraction relative tirée de la seule concentration absolue
  par deux paquets disjoints exacts.
- [x] Généraliser le cutoff solénoïdal aux champs lisses localement près de la
  boule externe, sans généraliser silencieusement le corollaire Biot–Savart.
- [x] Calculer l'équation exacte de
  `V(t)=chi_(R(t))u(t)-B_(R(t))(grad chi_(R(t)) dot u(t))`, avec
  `R(t)=2sqrt((T_*-t)/S_w^*(C_MM))`.
- [x] Isoler la dérivée de l'opérateur de Bogovskiĭ sous homothétie et le
  terme `R'(t)`; vérifier leur scaling dans un espace de force critique.
- [x] Recalculer la pression localisée et séparer projection de Leray, force
  annulaire et non-linéarité de `V`.
- [ ] Injecter une famille abstraite `M_j->infinity` dans les constantes
  Barker–Prange pour localiser quantitativement le premier échec Type II.
- [ ] Formaliser l'inclusion faible-`L3` de mesure finie et l'algèbre de la
  fraction dans un environnement épinglé.

### Cycle 0042

- [x] Conjuguer explicitement `B_R` depuis une réalisation unité fixe et
  calculer sa dérivée temporelle complète.
- [x] Dériver l'équation locale forcée de `V=chi_Ru-B_R(nabla chi_R dot u)`
  avec pression, diffusion, convection et terme `R'(t)`.
- [x] Distinguer la force annulaire locale de sa projection solénoïdale non
  locale.
- [x] Certifier les puissances `R^-3`, les normes spatiales et l'accumulation
  logarithmique sur un témoin pure-swirl annulant le correcteur.
- [x] Réfuter la petitesse de force fondée uniquement sur `R(t)->0`.
- [x] Fixer une formule intégrale support-lisse précise de Bogovskii sur la
  couronne unité et établir ses bornes dans les espaces négatifs de Lorentz.
- [x] Calculer `[Delta,Q]U` et `[D,Q]U` sur
  `U_N=epsilon phi(r,z)sin(Nz)e_theta`; suivre le terme principal en `N` dans
  la somme complète.
- [x] Prouver ou réfuter une borne uniforme
  `L1+div L^(3/2,infinity)` dépendant seulement de la taille Type I `M`.
- [ ] Si cette borne tient, formuler un problème de rigidité pour une solution
  ancienne avec force annulaire critique non évanescente.
- [ ] Garder le passage Type II séparé : injecter `M_j->infinity` seulement
  après fermeture ou réfutation du commutateur Type I.

### Cycle 0043

- [x] Fixer une réalisation exacte, support-preserving et
  pseudodifférentielle d'ordre `-1` de Bogovskii sur la couronne unité.
- [x] Calculer les ordres de `[Delta,B M_a]` et `[D,B M_a]` et suivre leurs
  constantes comme normes d'opérateur nommées.
- [x] Tester le mode pure-swirl haute fréquence dans une norme positive et
  dans `L1+div L^(3/2,infinity)`.
- [x] Composer commutateur, pression, non-linéarité et projection de Leray
  pour obtenir une borne critique uniforme en `R`.
- [x] Introduire une transition externe à facteur `L` et suivre la croissance
  de toutes les constantes géométriques et pseudodifférentielles.
- [x] Tester si la force annulaire disparaît sur chaque compact lorsque
  `L->infinity`, sans perdre la capture du core.
- [x] Réfuter une borne globale uniforme dans `X` sous `L->infinity` par une
  minoration duale quadratique sur un pure-swirl critique.
- [ ] Définir la topologie distributionnelle locale compatible avec `X` et
  construire un test de passage des produits quadratiques.
- [ ] Conserver le cas Type II séparé jusqu'à un contrôle uniforme des
  constantes Barker–Prange et de `kappa(M)`.

### Cycle 0044

- [x] Prouver l'identité locale
  `F_L=P_L div(Z_L tensor Z_L-U tensor U)` et conserver la queue extérieure
  non compacte.
- [x] Établir le taux `L^(-3-|alpha|)` sur tout compact par dualité Lorentz
  et somme dyadique.
- [x] Certifier les constantes du noyau pour `|alpha|=0,1` sur 253 assertions
  rationnelles.
- [x] Construire le contre-profil global
  `F_L=L^-3B_0(dot/L)+kappa L^-1A(dot/L)` et suivre sa norme quotient.
- [x] Écrire un ledger Aubin–Lions local avec espaces exacts pour
  `partial_sigma Z_j`, pression, force et produit quadratique.
- [x] Construire ou exclure une concentration temporelle qui préserve les
  bornes spatiales disponibles mais empêche la compacité forte locale.
- [ ] Transporter la capture du core vers une trace non triviale de la limite.
- [ ] Dérenormaliser l'équation à drift avec l'horloge exacte avant toute
  application d'un théorème sur les solutions anciennes.

### Cycle 0045

- [x] Fermer une Caccioppoli locale uniforme par pression `L^(4/3)`,
  Gagliardo–Nirenberg, Young et remplissage des trous.
- [x] Appliquer Simon avec les espaces exacts et obtenir forte `L2_loc`, puis
  forte `L3_loc` par interpolation sous `L^(10/3)`.
- [x] Passer le produit quadratique, la pression proche/harmonique et
  l'inégalité d'énergie locale de l'équation renormalisée.
- [x] Certifier 401 assertions exactes sur oscillation, couche terminale et
  concentration critique compacte.
- [x] Réfuter la transmission automatique d'une norme terminale par la
  compacité volumique (`FAIL-NS-0081`).
- [ ] Déduire de la capture Type I un moment fixe
  `|<Z_j(0),psi>|>=c_*`, ou construire une cascade PDE-compatible qui
  l'interdit.
- [ ] Tester quantitativement la condition de persistance de singularité
  d'Albritton–Barker A.5 sur la suite réelle.
- [ ] Dérenormaliser seulement après obtention d'une trace non nulle et
  conserver séparé le cas Type II.

### Cycle 0046

- [x] Recalculer l'horloge translatée et vérifier
  `R(sigma_j+s)/R_j=exp(-kappa s)` avec le bon ordre des quantificateurs.
- [x] Transporter la capture Barker–Prange au même `B_1` sur toute fenêtre
  normalisée fixe et vérifier `Q_(L_j)=I` dans ce coeur.
- [x] Composer cette capture avec la forte `L3_loc` du cycle 0045 pour
  obtenir une limite renormalisée non triviale.
- [x] Certifier l'inégalité optimale en mesure-temps, ses contre-profils et
  l'horloge sur 417 assertions exactes.
- [x] Corriger la portée de `FAIL-NS-0081` et enregistrer `FAIL-NS-0082`
  sans supprimer l'historique.
- [ ] Dérenormaliser la limite avec `R=e^(-kappa s)` et `dt/ds=R²`; passer
  l'équation, la pression et l'inégalité d'énergie locale dans les
  distributions.
- [ ] Identifier la classe standard obtenue avant de choisir un théorème de
  rigidité ancienne faible-`L3`.
- [ ] Garder séparées non-trivialité, trace à l'ancien endpoint et
  persistance d'un point singulier.

### Cycle 0047

- [x] Dérenormaliser exactement le drift avec domaine temporel, jacobien,
  divergence et pression suivis.
- [x] Transporter l'inégalité d'énergie locale dans les distributions et
  certifier le poids positif de la fonction test.
- [x] Identifier la sortie comme ancienne faible adaptée locale,
  uniformément faible-`L3`, non triviale et à pression de Riesz.
- [x] Certifier 420 assertions rationnelles et les résidus des mauvais
  signes, amplitudes, horloges et puissances de pression.
- [x] Refuser les promotions automatiques Leray–Hopf, local-energy avec trace
  forte et mild; enregistrer `FAIL-NS-0083`.
- [ ] Tester sur une bande forward finie si l'ancienne obtenue admet la
  scission calorique plus correcteur énergétique de `NS-SRC-0188`.
- [ ] Identifier ou réfuter une condition de trace faible-étoile annulant le
  reste calorique homogène à l'endpoint `L^(3,infinity)`.
- [ ] Garder séparées rigidité faible-`L3`, singularité terminale et Type II.

### Cycle 0048

- [x] Construire le représentant `C_w*L^(3,infinity)` sur toute bande finie.
- [x] Justifier Duhamel dans `L^(3,infinity)` comme intégrale faible-étoile
  de Gelfand via Meyer--Yamazaki.
- [x] Dériver le gain fort `L^p`, `3/2<p<3`, et le correcteur
  `C_tL2` avec taux `h^(1/4)`.
- [x] Distinguer la définition mild forte de Taniuchi, la classe énergétique
  BSS et la classe mild bornée KNSS.
- [x] Certifier 144 assertions exactes et le contre-profil solénoïdal à
  queue faible-`L3` persistante.
- [x] Enregistrer `FAIL-NS-0084` et raffiner le graphe vers la globalisation
  d'énergie relative.
- [ ] Appliquer l'inégalité locale au correcteur avec des cutoffs `chi_R` et
  suivre séparément convection, pression et flot calorique.
- [ ] Prouver que tous les flux de couronne tendent uniformément vers zéro,
  ou construire un contre-profil PDE-compatible d'influx à l'infini.
- [ ] Ne promouvoir vers BSS qu'après obtention indépendante de
  `w in L2_tHdot1_x` et de l'inégalité d'énergie perturbée globale.

### Cycle 0049

- [x] Dériver l'inégalité relative locale par identité croisée, sans test
  global prématuré par `w`.
- [x] Absorber le flux total convection--pression avec constantes uniformes
  en `R`, puis obtenir `w in L2_tHdot1_x` par Fatou.
- [x] Repasser dans l'inégalité non majorée pour conserver le signe BSS.
- [x] Certifier 97 assertions exactes et un contre-profil multi-annulaire à
  flux cubique diagonal constant.
- [x] Auditer BSS, Albritton--Barker et la veille 2025--2026; enregistrer
  `NS-SRC-0192` sans attribuer la nouvelle dérivation à la littérature.
- [ ] Comparer les scissions issues de deux temps de base distincts sans
  supposer l'unicité des solutions faibles à grande donnée.
- [ ] Tester si une différence calorifique explicite donne un cocycle
  énergétique contrôlé uniformément quand `t_0->-infinity`.
- [ ] Formuler puis attaquer un Liouville minimal pour ancienne faible-`L3`
  munie de scissions BSS sur toutes les bandes finies.

### Cycle 0050

- [x] Comparer exactement les scissions issues de trois temps de base et
  établir leur cocycle dans `L2 inter L^(3,infinity)`.
- [x] Séparer quotient algébrique non fermé et quotient de Banach par la
  fermeture du sous-espace énergétique.
- [x] Construire et auditer `U` puis `U_sharp`, avec saturation `h^(1/4)`,
  classe quotient fixe et résidu de limites itérées `8pi/3`.
- [x] Vérifier par circulation que les contre-profils ne satisfont pas
  Navier--Stokes non forcé.
- [x] Auditer Taniuchi, KNSS, Albritton--Barker, BSS et ajouter
  Bradshaw--Hudson `NS-SRC-0193` comme prépublication v1.
- [ ] Tester une identité PDE de basse fréquence ou une tightness annulaire
  qui réduirait `||g_(s,r)||_2` le long d'une suite `s->-infinity`.
- [ ] Ne pas utiliser de compacité quotient sans fermeture ni confondre
  classe quotient nulle et appartenance `L2`.

### Cycle 0051

- [x] Auditer Jia--Sverak et cataloguer les sources SS/DSS, Herz/Besov et
  Liouville spatialement pertinentes (`NS-SRC-0194` à `NS-SRC-0202`).
- [x] Construire un saturateur Navier--Stokes forward exact et prouver
  `W!=0` sans supposer l'unicité.
- [x] Établir `||w(t)||_2=C_*t^(1/4)` et la dissipation exacte, puis
  enregistrer `FAIL-NS-0087` avec sa portée non ancienne et non Clay.
- [x] Dériver la borne dyadique du correcteur et fermer uniformément toutes
  les fréquences `j>J`.
- [x] Réduire le critère `liminf L2` à un cutoff bas fixe, ou à un unique
  lissage calorifique `S(a)` fixé avant la limite.
- [x] Certifier 615 assertions rationnelles sur la fuite infrarouge et les
  ordres de limites.
- [ ] Tester un gain signé `2^(epsilon(j-J))` pour les intégrales vectorielles
  basses `B_j` d'une même orbite ancienne.
- [ ] Déterminer si une annulation de moment, une déplétion triadique ou une
  récurrence de blow-down est héritée du scénario Type I.
- [ ] Ne jamais remplacer l'orbite ancienne par une famille de solutions
  forward translatées ni sommer les normes avant les phases.

### Cycle 0052

- [x] Dériver l'identité lissée en temps de base avec signe, facteur deux,
  double paramètre calorifique et pairing de pression justifiés.
- [x] Séparer primitive signée, variation absolue et intégrale impropre; en
  déduire le quantificateur minimal sur une suite ancienne.
- [x] Suivre l'échelle de `E_a`, `Phi_a` et `Phi_a ds`.
- [x] Certifier l'absence de signe et de coercivité triadiques universels par
  1058 assertions exactes sur `T3`.
- [x] Auditer les Liouville backward SS/DSS et enregistrer seulement le
  sous-cas faible-`L3` exact effectivement publié.
- [ ] Décomposer `Phi_a` en flux Littlewood--Paley signés et tester un gain
  après somme des triades et intégration temporelle.
- [ ] Chercher une propriété de récurrence de blow-down héritée par la même
  orbite ancienne, sans la supposer auto-similaire.
- [ ] Ne pas réutiliser une valeur absolue, une triade instantanée isolée ou
  un théorème DSS à petit paramètre comme rigidité générale.

### Cycle 0053

- [x] Définir un défaut de générateur sur fenêtres avec le partenaire
  Lorentz endpoint exact de la pression faible-`L^(3/2)`.
- [x] Vérifier la diagonale commune en rayon et le passage
  `petit générateur -> limite stationnaire`.
- [x] Conserver la capture espace-temps par forte convergence `L3_loc` et
  normaliser explicitement le coefficient positif du drift.
- [x] Auditer Guevara--Phuc, Chae--Wolf et la veille récente sans ajouter de
  source redondante.
- [x] Certifier concentration, fuite, récurrence et erreurs de diagonale par
  1814 assertions rationnelles exactes.
- [ ] Relier une minoration de `D_R` à une composante signée du flux
  calorifique `Phi_a`, avec pression et changement de variables suivis.
- [ ] Construire ou exclure une orbite récurrente non stationnaire où le
  générateur reste actif mais la primitive infrarouge demeure bornée.
- [ ] Ne pas promouvoir la dérivation au-delà de `COMPUTATION_ONLY` sans
  revue humaine ou formalisation du paquet compactité--pression.

### Cycle 0054

- [x] Conjuguer exactement l'horloge, la dilatation, la chaleur et le
  générateur renormalisé, avec signe, facteur `rho²` et pression suivis.
- [x] Distinguer le filtre de la dérivée `B_s` du second temps calorifique du
  test de stress.
- [x] Établir que `D_R` ne contrôle pas le flux par les normes disponibles :
  fenêtre/tranche, local/global, dérivée/résidu et norme/direction.
- [x] Certifier un contre-modèle tangent par 47259 assertions exactes et
  vérifier que sa réalisation sur `T3` a un résidu NS non nul.
- [x] Auditer Pineau--Vicol v2 comme prépublication RSS/RDSS, sans transfert
  automatique depuis faible-`L3`.
- [ ] Écrire l'équation de profil RSS dans les conventions du laboratoire et
  reproduire les seuils extrêmes de rotation avec constantes suivies.
- [ ] Tester une rotation intermédiaire et une modulation lente contre le
  flux calorifié, en séparant calcul de découverte et preuve PDE.
- [ ] Ne pas présenter l'exclusion RSS exacte comme exclusion des orbites
  apériodiques, Type II ou du problème Clay.

### Cycle 0055

- [x] Vérifier l'équivariance de l'opérateur renormalisé, projection de
  Leray, pression de Riesz, drift et terme quadratique compris.
- [x] Prouver distributionnellement la dichotomie orbite stationnaire ou RSS
  à vitesse constante sous une phase `W^(1,1)_loc`.
- [x] Traiter séparément stabilisateur continu, stabilisateur discret,
  rotation centrée et convention de signe.
- [x] Raccorder sans promotion abusive la branche stationnaire à
  Guevara--Phuc et la branche RSS extrême à Pineau--Vicol v2.
- [x] Certifier les limites de la version approchée par 960 assertions
  rationnelles exactes.
- [ ] Prouver le passage au profil RSS lorsque `beta_n` est uniformément
  borné et que le défaut modulé tend vers zéro sur toute boule fixe.
- [ ] Construire l'alternative compacte lorsque
  `mathcal R Z_n->0`, sans diviser par une constante angulaire dégénérée.
- [ ] Tester séparément `|beta_n|->infinity`, moyenne axisymétrique et perte
  de phase, sans importer les estimations Type I ponctuelles depuis
  faible-`L3`.

### Cycle 0056

- [x] Extraire une sous-suite faible-étoile commune de vitesses de
  modulation uniformément bornées.
- [x] Prouver le passage de `beta_n mathcal RZ_n` par adjoint du générateur
  et convergence forte locale, sans convergence des gradients.
- [x] Reconstruire une phase `W^(1,infinity)` et un profil spatial fixe sans
  supposer de trace forte.
- [x] Fermer la dichotomie stationnaire/RSS et conserver séparément le
  ledger uniforme requis pour suitability et pression.
- [x] Certifier les frontières faible--faible, vitesse non bornée,
  générateur dégénéré, sous-suite non commune et test mobile par 1288
  assertions rationnelles exactes.
- [ ] Déterminer si `|beta_n|->infinity` force une moyenne axisymétrique sous
  les bornes Type I disponibles ou permet un produit compensé non nul.
- [ ] Produire le défaut modulé depuis le pipeline Type I, au lieu de le
  prendre comme hypothèse dynamique.
- [ ] Attaquer la rigidité RSS faible-`L3` à rotation intermédiaire sans
  importer une borne Type I ponctuelle absente.

### Cycle 0057

- [x] Introduire `q_n=1/beta_n` et suivre séparément sa norme uniforme et sa
  variation totale sur chaque fenêtre compacte.
- [x] Prouver l'estimation contre `q_n phi` dans le couple
  `L-infinity_tL2_x`--`L1_tH^(-1)_x`.
- [x] Déduire `mathcal RZ=0`, puis la stationnarité par moyenne de Haar et
  annulation du défaut.
- [x] Raccorder le profil stationnaire capturé à Guevara--Phuc sans utiliser
  la route axisymétrique classique comme hypothèse silencieuse.
- [x] Certifier une stroboscopie à vitesses positives `N,N^4`, les zéros,
  tests mobiles et moyennes par 44218 assertions rationnelles exactes.
- [ ] Construire une condition de phase depuis `Z_n` dont
  `Var(1/beta_n)` est contrôlée par des quantités suitable uniformes.
- [ ] Déterminer si l'autonomie de Navier--Stokes interdit la stroboscopie
  positive malgré son admissibilité cinématique forte `L3_loc`.
- [ ] Auditer le raccord exact « limite suitable axisymétrique faible-`L3`
  -> ancienne classique » avant d'utiliser Ożański--Palasek sans
  stationnarité.
