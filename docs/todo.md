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
- [ ] Calculer l'équation exacte de
  `V(t)=chi_(R(t))u(t)-B_(R(t))(grad chi_(R(t)) dot u(t))`, avec
  `R(t)=2sqrt((T_*-t)/S_w^*(C_MM))`.
- [ ] Isoler la dérivée de l'opérateur de Bogovskiĭ sous homothétie et le
  terme `R'(t)`; vérifier leur scaling dans un espace de force critique.
- [ ] Recalculer la pression localisée et séparer projection de Leray, force
  annulaire et non-linéarité de `V`.
- [ ] Injecter une famille abstraite `M_j->infinity` dans les constantes
  Barker–Prange pour localiser quantitativement le premier échec Type II.
- [ ] Formaliser l'inclusion faible-`L3` de mesure finie et l'algèbre de la
  fraction dans un environnement épinglé.
