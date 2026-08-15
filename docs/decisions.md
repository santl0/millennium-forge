# Décisions

## Décisions validées

### 2026-08-14 — dépôt public autonome

- Nom : `Millennium Forge`.
- Dépôt cible : `santl0/millennium-forge`.
- Visibilité : publique, conformément à l'objectif open source et collaboratif.
- Branche stable : `main`.
- Licence initiale : MIT.
- Le dossier de recherche local actif reste séparé pendant son exécution afin d'éviter d'importer des fichiers partiels, clones imbriqués ou sources sous licence.

### 2026-08-14 — Git comme registre canonique

- Une affirmation possède un identifiant stable et un statut contrôlé.
- Les idées spéculatives vivent dans les issues ou branches ; elles n'entrent dans le corpus canonique que par pull request.
- Les résultats négatifs sont conservés.
- Les contributions IA doivent enregistrer modèle, date, objectif, artefacts et revue indépendante.

### 2026-08-14 — validation progressive

- Le calcul explore et falsifie ; il ne remplace pas une preuve universelle.
- Lean est utilisé lorsque les fondations nécessaires existent.
- Une preuve candidate générale requiert une expertise humaine indépendante en plus des contrôles automatisés.

### 2026-08-14 — fermeture conditionnelle du commutateur localisé

- `GAP-COMMUTATOR-UNIFORMITY` est fermé seulement sous les hypothèses globales
  faible-`L^(3/2)` et `bmo_phi`, le raccord tensoriel et les théorèmes
  classiques de Jones, CRW et John–Nirenberg.
- Les corrections de semi-norme BMO, interpolation faible, réarrangée exacte
  et dernier anneau sont enregistrées; aucun statut `PAPER_PROOF` n'est créé.
- `GAP-ENDGAME-SYNCHRONIZATION` devient le verrou actif.

### 2026-08-14 — endgame conditionnel et extension active réfutée

- `GAP-ENDGAME-SYNCHRONIZATION` est fermé conditionnellement au cycle 0019,
  après remplacement du temps maximal par un temps garanti et séparation des
  branches prolongement direct / temps intérieur.
- L'implication « cohérence sur chaque cœur actif vers `bmo_phi` global
  uniforme » est réfutée au cycle 0020 par deux phases antipodales; la borne
  optimale d'oscillation est `4ab/(a+b)`.
- La direction de vorticité doit comporter une convention ou un quantificateur
  d'extension sur `{omega=0}`; sinon son appartenance à `bmo_phi` n'est pas
  intrinsèque.
- `GAP-ACTIVE-CORE-BMO` est fermé négativement sans packing inter-composantes.
  `GAP-CRITICAL-PROFILE-ADMISSIBILITY` devient le verrou actif.

### 2026-08-14 — profil vectoriel exactement récurrent exclu

- La Definition 2.1 de `arXiv:2607.08866v2` est conservée comme description
  conditionnelle à réviser : ses quantificateurs ne définissent ni cœur
  régularisé avant `T*`, ni limite remise à l'échelle.
- Un profil `r^-2 Omega(theta)` doit satisfaire une divergence tangentielle
  sphérique nulle et un flux radial moyen nul avant tout usage de Biot–Savart.
- `NS-DILATION-RECURRENT-BMO-RIGIDITY` exclut la classe vectorielle exactement
  récurrente, non nulle et globalement faible-Lorentz sous log-BMO; statut
  `COMPUTATION_ONLY`, aucune promotion en preuve publiée.
- Trois portes distinctes ferment l'ansatz exact : définition scalaire,
  rigidité directionnelle et défaut critique des coupures.
- Le programme pivote vers `GAP-LOG-RECTIFIED-PROFILE`, sans réétiqueter un
  profil asymptotique comme homogène exact.

### 2026-08-14 — rectification à axe fixe exclue sous masse par bloc

- Pour `s=log(R_*/r)`, la contrainte solénoïdale porte le signe
  `div_S Omega_T-partial_s Omega_r`; le signe provisoire contraire est
  corrigé avant tout usage.
- `NS-LOG-RECTIFIED-SOLENOIDAL-OBSTRUCTION` exclut, au statut
  `COMPUTATION_ONLY`, une amplitude angulaire uniformément bornée, une masse
  critique non dégénérée par bloc et une direction rectifiée vers un axe
  fixe. Aucun statut publié ou formalisé n'est attribué.
- Le faible-`L^(3/2)` global ne remplace pas ces hypothèses : des calottes
  intermittentes gardent la masse critique avec amplitude non bornée.
- Une construction div–curl exacte réalise la rectification en perdant la
  singularité critique; son résidu stationnaire ne s'annule pas.
- Lei–Ren–Tian `2501.08976v1` est enregistré `SOURCE_VERIFIED` pour le critère
  conditionnel du double cône, sans reproduction de la preuve.
- `GAP-LOG-RECTIFIED-PROFILE` est fermé pour l'axe fixe sous les prémisses
  suivies. `GAP-WANDERING-AXIS-PROFILE` devient le verrou actif.

### 2026-08-14 — budget de l'axe mobile et pivot multicoeur

- `NS-WANDERING-AXIS-MOMENT-BUDGET` borne la recharge du premier harmonique
  par `(M/2)Var(e)` et exclut toute sélection absolument continue à variation
  et erreur pondérée sublinéaires sous amplitude bornée et masse critique par
  bloc.
- La rotation radiale uniforme échoue au taux log-BMO centré; la phase
  logarithmique lente passe ce test mais ne fournit pas la variation linéaire
  nécessaire.
- Grande variation ne signifie pas échappement : de petites boucles rapides
  peuvent rester dans un cône fixe. Aucune conclusion n'est tirée de la
  variation seule.
- Miller 2021 est ajouté comme critère publié à plan variable; Lei–Ren–Tian
  v1 est relu en distinguant le cône fixe du théorème 1.1 et le corollaire
  pairwise tolérant un axe temporel.
- Le résultat reste `COMPUTATION_ONLY`, sans pression, vitesse, évolution ou
  passage au continuum.
- Le programme active `GAP-MULTICORE-ANGULAR-CASCADE` : moyennes actives
  dégénérées, occupation angulaire multivaluée et intermittence.

### 2026-08-14 — axe actif extrait et pivot vers l'intermittence non bornée

- Correction du cycle 0023 : un champ global unitaire log-BMO a des moyennes
  non dégénérées; l'ambiguïté subsiste dans l'existence et la convention du
  prolongement aux zéros.
- `NS-BMO-ACTIVE-AXIS-EXTRACTION` ferme au statut `COMPUTATION_ONLY` les
  configurations multicoeurs sous amplitude critique bornée, masse par bloc
  et extension commune à oscillation logarithmique.
- Les constantes de fraction active, comparaison de volumes, interpolation
  géodésique et raccord au budget mobile sont suivies; trois passes Codex
  séparées ont attaqué la dérivation sans constituer une revue externe.
- Le contre-profil d'amplitude `n²` sur une fraction `n^-3` conserve la masse
  critique et annule l'axe moyen. Il interdit de remplacer silencieusement la
  borne de tranche par le seul faible-Lorentz.
- `GAP-MULTICORE-ANGULAR-CASCADE` est fermé sous les prémisses suivies et
  `GAP-UNBOUNDED-ANGULAR-INTERMITTENCY` devient actif.

### 2026-08-14 — train critique réalisé, forme fixe abandonnée

- `NS-CRITICAL-BLOB-TRAIN-BMO-GATE` construit au statut `COMPUTATION_ONLY` un
  champ statique d'énergie finie dont la vorticité est divergence-free,
  faible-`L^(3/2)`, de masse critique par bloc et d'amplitude angulaire `n²`.
- Le raccord Biot–Savart `L²` est valide; la pression et l'évolution ne sont
  pas produites.
- Les boules centrées diluent l'occupation comme `n^-3`, mais le motif
  directionnel interne récurrent impose une oscillation positive sur des
  boules décentrées de rayon tendant vers zéro, indépendamment de l'extension
  aux zéros.
- Le curl du résidu stationnaire est non nul; aucune pression ne transforme
  le train en solution stationnaire.
- Le blob de forme fixe est abandonné. Le programme active
  `GAP-DIRECTIONALLY-FLAT-INTERMITTENCY`, où une région de compensation forte
  doit satisfaire `integral curl U=0` sans réintroduire une oscillation BMO.
- Correction de portée : pour une solution forte non triviale à temps positif,
  les choix sur le lieu nodal analytique, nul en mesure, ne changent pas BMO;
  les prochains tests portent sur la phase près des zéros.

### 2026-08-14 — compensation conique quantifiée, cascade emboîtée activée

- `NS-LORENTZ-CONE-COMPENSATION` donne au statut `COMPUTATION_ONLY` la borne
  critique `MO_D>=2alpha^3m^3/(27K^3|D|)` sous moyenne vectorielle nulle;
  une passe adverse a amélioré la première constante `alpha^4/27`.
- La convention de quasi-norme faible-`L^(3/2)` est fixée explicitement; la
  constante trois de l'intégration pondérée et la constante `2/27` sont
  suivies sans discrétisation.
- La famille rationnelle à deux amplitudes montre que l'exposant cubique est
  sharp dans la classe mesurable et que la masse forte critique ne minore pas
  la masse conique `L¹`.
- Ce modèle n'est ni spatial, ni solénoïdal, ni un curl compact. Une interface
  régulière possède une oscillation locale égale à un malgré sa petite
  oscillation sur le domaine parent.
- Un corridor de zéros autorise une extension unitaire de coût
  `Theta(1/log(R/h))`; une minoration BMO d'ordre un sans hypothèse d'épaisseur
  est abandonnée.
- Le lift collinéaire compact est impossible par `partial_e f=0`. Le premier
  relèvement testé sera axisymétrique et conservera ses termes transverses.
- Le programme active `GAP-NESTED-RETURN-FLOW-CASCADE` : construction div–curl
  axisymétrique, contrôle de toutes les sous-boules, puis Biot–Savart et résidu.

### 2026-08-14 — lift axisymétrique réalisé, produit séparable abandonné

- `NS-AXISYMMETRIC-RETURN-FLOW-BMO-GATE` certifie au statut
  `COMPUTATION_ONLY` la minoration
  `MO_B>=3w/[2048(R+w)]` sur une boule entièrement active de calotte.
- Le profil polynomial ferme exactement flux, curl, divergence, moyenne,
  faible-Lorentz et énergie; son cutoff est `C^4`, sans promotion Clay.
- La variante équilibrée et la construction `C_c^infinity` de la passe
  analytique donnent `K~1`, `m~epsilon^(1/3)`, `MO_D~epsilon`. Le cube du
  cycle 0026 reste sharp dans la classe compacte div–curl.
- Cette sharpness porte seulement sur un domaine parent. Les interfaces et
  transitions locales ne fournissent aucune borne log-BMO all-ball.
- `||U_epsilon||_3->0`; la famille lisse est éliminée comme candidate au
  blow-up par le régime perturbatif critique.
- La composante azimutale du résidu stationnaire est non nulle. Une pression
  ne ferme pas la construction.
- L'aspect croissant est enregistré comme coût auxiliaire, non comme solution.
  Le programme active `GAP-NONSEPARABLE-RETURN-FLOW-MASKING`.

### 2026-08-14 — échappatoire torique admise, candidat dynamique abandonné

- `NS-TOROIDAL-LOG-BMO-VELOCITY-COLLAPSE` est enregistré au statut
  `COMPUTATION_ONLY` : le tore mince passe divergence, moyenne, criticité de
  vorticité et log-BMO statique all-ball.
- La borne directe auditée
  `||u||_3^3<=CK^3(h/R+(h/R)^2)` élimine la famille comme profil critique de
  vitesse; la borne interpolée `O((h/R)^(1/9))` n'est pas utilisée.
- Le corridor à zéros n'est pas propagé par la diffusion d'un anneau unisigné
  sans swirl sur `R^3`; l'obstruction axiale vaut exactement un à temps
  positif. Cette conclusion n'est pas transférée silencieusement au tore
  périodique ou aux données signées.
- `NS-AXISYMMETRIC-RADIAL-EXCESS-CAPACITY` conserve le seul noyau positif de
  la voie poloidale. Sans `Delta_Omega>0`, le rang fini ne donne aucune
  capacité uniforme.
- `GAP-NONSEPARABLE-RETURN-FLOW-MASKING` est abaissé. Le programme active
  `GAP-MOMENT-CORRECTED-TOROIDAL-CASCADE` avec première porte limitée à
  l'annulation de l'impulsion.

### 2026-08-14 — impulsion annulée, cardinal fini abandonné

- `NS-IMPULSE-CORRECTED-TORUS-PAIR-COLLAPSE` est enregistré au statut
  `COMPUTATION_ONLY`.
- Une paire transversale `+/-` annule exactement l'impulsion, conserve les
  normes critiques de vorticité et le log-BMO statique, et sort de la classe
  axisymétrique globale.
- Le second multipôle reste non nul : la vitesse entière décroît comme une
  puissance, pas comme une fonction de Schwartz.
- Stokes fournit la minoration qui manquait et confirme
  `||u||_3^3~K^3h/R`; la petite vitesse n'est pas due à une estimation lâche.
- La paire coaxiale signée échoue dynamiquement au log-BMO sur son plan nodal;
  ce test ne couvre pas automatiquement la paire transversale.
- Kato n'est raccordé qu'à `R3`; le seuil périodique `L3` reste à sourcer ou
  dériver avec constantes.
- Toute famille de cardinal fixé et de rapports d'aspect tendant vers zéro est
  fermée, même après un nombre fini d'annulations de moments.
- `GAP-MANY-TORUS-CRITICAL-ACCUMULATION` devient actif; l'alternative
  « vitesse compacte d'abord » est conservée comme second candidat.

### 2026-08-14 — cardinal croissant homogène fermé, gate compact affiné

- `NS-POROUS-MANY-TORUS-L3-COLLAPSE` est enregistré au statut
  `COMPUTATION_ONLY` sous amplitude, coeur, corridor et packing local communs.
- La borne collective est
  `||u||_3^3<=CK^3[h/mathcal L+(h/q)^(4/3)]`; le cas périodique conserve le
  terme supplémentaire `CK^3S` et exige `S->0`.
- L'exposant `4/3`, la troncature à `q/2`, la normalisation faible-Lorentz et
  le reste périodique ont subi des passes adversariales séparées. Les
  constantes géométriques ne sont pas interval-certified.
- `NS-COMPACT-VELOCITY-ENDPOINT-SEPARATION` réfute le gate « vitesse compacte,
  vorticité faible critique bornée, `L^3` fort non nul » : les endpoints
  faibles et la norme forte se séparent sur une cascade de supports disjoints.
- Yamazaki ferme la variante normalisée par petite donnée faible-`L^3`; la
  variante non normalisée échoue encore à la cohérence directionnelle interne.
- Trois stratégies tubulaires homogènes sont maintenant fermées : tore unique,
  moments à cardinal fixé, cardinal croissant localement packé. Cette branche
  est abandonnée sans ledger hétérogène nouveau.
- `GAP-COMPACT-VELOCITY-WEAK-CRITICAL-DIRECTION` devient actif. Le prochain
  gate exige une direction active log-BMO uniforme, une norme faible-`L^3`
  non perturbative et un temps d'interaction indépendant de la plus petite
  échelle.

### 2026-08-14 — rapport d'aspect séparable fermé

- Le facteur `R/r` est retenu pour le swirl compact car il annule exactement
  la courbure dans le curl et rend visibles les deux coûts de dérivée.
- Sous gates vitesse/vorticité, les deux largeurs sont minorées par une
  fraction du grand rayon; l'échappement par aspect est abandonné.
- Une boule de calotte reste directionnellement active, mais l'extension à
  des couches non séparables est laissée ouverte plutôt que supposée.

### 2026-08-14 — superpositions minces fermées par weak HLS

- La meilleure action du cycle est le lemme universel de support, score
  `20/20`, devant le ledger transitionnel (`18/20`) et l'optimisation BMO
  numérique (`15/20`).
- Le champ total `F`, après toutes les annulations, remplace définitivement
  les budgets additifs par couche.
- La branche à aire méridienne `o(R^2)` est abandonnée :
  `K_U<=C(S_2/R^2)^(1/6)K_W` force la petite donnée faible-`L3`.
- Le statut reste `COMPUTATION_ONLY`, conformément à la politique qui interdit
  de promouvoir une dérivation IA nouvelle en preuve papier.
- Le prochain verrou est `GAP-THICK-CROSS-SECTION-GRADIENT-DIRECTION`; aucune
  pression ou évolution n'est calculée avant survie du gate statique.

### 2026-08-14 — diamètre borné fermé par troncature conique

- La troncature d'un superniveau presque optimal est retenue avec le score
  `20/20`; le degré topologique sans contrôle de volume est abaissé.
- Coaire porte sur la somme tronquée réelle, ce qui conserve les annulations
  internes sans réintroduire un ledger par couche.
- Le support axial `O(R)` fournit une vraie boule de volume `O(R^3)`; sur cette
  boule, la compensation conique donne la puissance endpoint six.
- Les plateaux, retours rares et superpositions non séparables dans une cellule
  bornée sont abandonnés comme échappements aux trois gates.
- `GAP-AXIALLY-DISPERSED-PURE-SWIRL-SELECTION` devient actif. Aucune inférence
  vers la pression ou le temps n'est autorisée avant sélection d'un bloc local.

### 2026-08-14 — sélection hétérogène réparée par registre BV

- Toute sélection reposant seulement sur les quasi-normes cellulaires est
  abandonnée : une distribution dyadique exacte réfute le pigeonhole commun.
- Une nouvelle sélection est admise sous plateau effectif, boîte de volume
  comparable et coût BV uniforme de fermeture compacte.
- Pour des cellules pure-swirl épaisses, disjointes et à aspect borné, coaire
  produit ce coût; le rapport local sélectionné est quadratique dans le
  rapport global.
- La composition avec le cycle 0033 donne une puissance directionnelle douze,
  sans prétendre sélectionner une échelle de concentration.
- Les théorèmes de profils avec espace source plus fort et Barker–Prange sous
  Type I sont des comparateurs sourcés, pas une preuve du lemme statique.
- `GAP-DEGENERATE-CELL-REGISTER-OR-OVERLAP` devient actif. Pression, cutoff de
  Leray et évolution restent différés jusqu'à survie de ce nouveau gate.

### 2026-08-14 — boîte supprimée par bande de niveau commune

- L'inférence « volume témoin `v_j` vers halo `O(v_j)` » est abandonnée après
  un contre-exemple pure-swirl lisse et curl-compatible par dilatation.
- Le niveau global presque optimal est retenu comme seul calibrage de volume :
  la bande entre `lambda/4` et `lambda/2` reste dans le superniveau
  `lambda/6` de la vitesse.
- Coaire tridimensionnelle et isopérimétrie remplacent le registre de boîte;
  la constante finale est `C_I/324` et ne dépend pas de la longueur axiale,
  du volume support, du nombre de composantes ou d'un plateau.
- Le claim positif reste `COMPUTATION_ONLY`; trois passes IA ne constituent
  pas une revue éditoriale indépendante.
- Aucune puissance directionnelle douze n'est composée sans boule de diamètre
  contrôlé. Le volume de la bande ne suffit pas.
- `GAP-ACTIVE-HALO-DIAMETER-OR-OVERLAP` devient actif. Le test mono-cellule à
  gouttelettes dispersées précède tout recouvrement intercellulaire.

### 2026-08-14 — gouttelettes sous le seuil fermées par troncature

- La troncature composante par composante est retenue avec le score `20/20`;
  elle évite le faux passage volume vers diamètre.
- La fonction tronquée est lipschitzienne à trace nulle et son curl est
  exactement la restriction signée du curl original, sans mesure de bord.
- Une goutte porte un rapport endpoint
  `>=(C_I/648)(K_u/K_w)^2`; si chaque goutte a diamètre `O(R_j)`, le gate
  directionnel fournit la puissance globale douze.
- L'extension explicite du gate 0033 à `W_c^{1,infinity}` est enregistrée
  comme claim interne distinct, et non cachée dans la composition.
- Les copies identiques et les filaments strictement sous `lambda/4` sont
  abandonnés comme échappements. Volume+périmètre seuls ne contrôlent pas le
  diamètre d'une composante.
- `GAP-ABOVE-THRESHOLD-THIN-BRIDGE` devient actif; chevauchement des supports
  et dynamique restent différés.

### 2026-08-15 — pont persistant fermé par périmètre–diamètre planaire

- Le lemme de branche persistante est retenu avec le score `20/20`; le ledger
  direct du pont est conservé comme test adverse et l'arbre de fusion complet
  est différé.
- L'annulation exacte du jacobien cylindrique par `R/r` fixe la constante
  `9/(8pi)`, plus forte que la première borne annulaire grossière.
- Un pont de persistance relative fixe et calibré par `AR>=kappa K_u` est
  abandonné comme échappement : son diamètre normalisé est borné par le rapport
  endpoint inverse.
- L'excès évanescent réduit le curl de la troncature, pas le curl original;
  la famille `eta=L^-3/2`, `delta=L^-1` est conservée comme test de frontière.
- L'inférence `niveau global -> AR>=kappa K_u pour chaque goutte` est
  abandonnée; des gouttes multiples la réfutent par le facteur `m^-1/3`.
- Le prochain verrou est
  `GAP-BRIDGE-SCALE-CALIBRATION-OR-MERGE-TREE`; pression et dynamique restent
  différées.

### 2026-08-15 — niveau et composante sélectionnés simultanément

- La sélection adaptative directe est retenue avec le score `20/20`; le merge
  tree certifié (`17/20`) reste un outil d'expérience, pas la preuve active.
- L'itération d'une bonne composante vers un descendant géométrique est
  abandonnée : le rapport endpoint n'est pas monotone sous retroncature.
- Le niveau presque optimal vérifie automatiquement
  `lambda R>=K^2/(432H)` dans une cellule annulaire pure-swirl.
- La moyenne de coaire puis la sélection endpoint au même niveau donnent
  `diam/R<=2 239 488q^-3` et un rapport local `>=C_I q^2/20 736`.
- La composition ferme le diamètre pour les familles pure-swirl à supports
  complets disjoints; elle ne produit ni pression, ni temps, ni résultat Clay.
- Un barcode H0 long est abandonné comme substitut à la marge `col-cutoff`;
  un calcul topologique utile doit porter un maximin spatial et une erreur
  uniforme certifiée.
- `GAP-OVERLAPPING-CURL-CANCELLATION` devient actif; la dynamique Type I/II
  reste le verrou suivant.

### 2026-08-15 — abandon des cellules étiquetées sous recouvrement

- La paire lisse `Z_n,-Z_n` est retenue avec le score `20/20`; elle réfute la
  sélection universelle sous multiplicité deux sans quitter la classe
  pure-swirl lisse, compacte et divergence-free.
- La multiplicité de supports et la compatibilité curl sont abandonnées comme
  substituts à une coercivité anti-annulation.
- Une décomposition peut être modifiée par ajout de `+Z,-Z` sans changer le
  champ total; toute règle admissible doit donc être intrinsèque ou imposer
  une jauge canonique quantitativement testable.
- Pour un axe, un rayon et un anneau communs, les potentiels sont agrégés avant
  toute valeur absolue; le claim 0038 s'applique alors au champ total.
- La réparation par base ondelette du plein `L^(p,infinity)` est abandonnée :
  non-séparabilité et indice secondaire infini bloquent la convergence en
  norme. Les carrés-fonctions restent des outils du champ total, pas des labels.
- `GAP-MULTIAXIS-TOTAL-FIELD-LOCALIZATION` devient actif. Projection de Leray,
  curl de col, pression et dynamique doivent désormais être estimés ensemble.

### 2026-08-15 — localisation solénoïdale à géométrie fixe

- Le correcteur de Bogovskiĭ sur la couronne homothétique fixe est retenu
  avec le score `18/20`; la projection globale de Leray et la matrice de Gram
  multi-axe restent des alternatives non sélectionnées.
- La compatibilité de moyenne est calculée exactement depuis
  `div(chi_RU)`; aucun flux nul local n'est supposé silencieusement.
- Le passage faible-`L^(3/2)` utilise un même opérateur interpolé entre deux
  exposants forts. La conclusion lisse exige séparément la préservation du
  support `C_c^infinity`.
- Le coût du col est critique et saturé par un plateau lisse; toute petitesse
  `o_R(1)` fondée sur le seul rayon est abandonnée.
- Les couronnes minces sont abandonnées comme moyen de gagner du volume : la
  norme forte de toute droite inverse croît au moins comme `R/h`.
- `GAP-MULTIAXIS-SOLENOIDAL-CUTOFF` est fermé statiquement. La pression et la
  dynamique ne sont pas incluses dans cette décision.
- `GAP-WEAK-L3-CORE-CAPTURE-AT-PRESINGULAR-SCALE` devient actif. Une capture
  par grande boule est déclarée triviale; seul un rayon lié à une
  concentration et tendant vers zéro est admissible.

### 2026-08-15 — fermeture conditionnelle de la capture Type I

- L'audit et la composition du théorème publié Barker–Prange sont retenus
  avec le score `18/20`; le contre-profil statique et l'inverse faible-HLS
  restent des alternatives non sélectionnées.
- Les constantes de l'extension Lorentz sont renommées `gamma_w,S_w^*`; elles
  ne sont pas identifiées aux constantes du théorème `L3` imprimé.
- La borne temporelle du claim est pointwise. Sous un simple supremum
  essentiel, la fraction doit être formulée presque partout ou accompagnée
  d'un lemme de représentant.
- `GAP-WEAK-L3-CORE-CAPTURE-AT-PRESINGULAR-SCALE` est fermé sous borne Type I
  globale, avec fraction `gamma_w/M`; il n'est pas déclaré fermé en Type II.
- La concentration absolue sans borne globale est abandonnée comme source
  d'une fraction : deux paquets disjoints exacts la réfutent.
- Le claim de cutoff 0040 est généralisé aux champs localement lisses près de
  la boule externe. L'absorption Biot–Savart demeure conditionnelle à des
  normes globales.
- `GAP-TYPE-I-LOCALIZED-EVOLUTION` devient actif : la prochaine dérivation
  doit inclure `R'(t)`, la dépendance temporelle de Bogovskiĭ, la pression et
  chaque puissance d'échelle.

### 2026-08-15 — équation forcée du cutoff mobile

- La conjugaison exacte et la PDE forcée sont retenues avec le score `19/20`;
  la borne directe en espace critique et le saut Type II obtiennent `16/20`.
- Un même opérateur de Bogovskii unité est fixé puis conjugué. Toute dérivée
  omettant son commutateur de dilatation est déclarée fausse.
- La forme locale conserve le support annulaire au prix d'une force non
  solénoïdale; la forme projetée conserve la divergence nulle au prix d'une
  queue de Leray. Ces formulations ne sont pas confondues.
- La petitesse fondée sur `R(t)->0` est abandonnée : le transport de frontière
  est `R^-3` et sa norme `L1` est critique, même lorsque le correcteur vaut
  exactement zéro.
- Le contre-profil ne réfute pas une cancellation de la somme complète pour
  une vraie solution; cette réserve reste explicite dans les deux claims.
- `GAP-TYPE-I-LOCALIZED-EVOLUTION` est raffiné en
  `GAP-TYPE-I-MOVING-COMMUTATOR-BOUND` puis
  `GAP-TYPE-I-FORCED-RIGIDITY`.
- La prochaine action fixe une formule intégrale de Bogovskii et teste les
  commutateurs sur une famille pure-swirl haute fréquence.

### 2026-08-15 — commutateur fermé dans un espace négatif critique

- La réalisation de Bogovskii est désormais fixée comme droite inverse
  exacte, support-preserving et pseudodifférentielle d'ordre `-1`; le seul
  mapping qualitatif sur les tests n'est plus accepté comme hypothèse cachée.
- La marche `W_0^(-1,4/3)->L^(4/3)` utilise la notation exacte de
  Geißert–Heck–Hieber et des données strictement supportées dans la couronne.
- La croissance haute fréquence positive est abandonnée comme obstruction à
  `L1+div L^(3/2,infinity)` : la dérivée passe exactement dans le stress.
- Le claim `NS-TYPE-I-MOVING-CUTOFF-CRITICAL-FORCE-BOUND` reste
  `COMPUTATION_ONLY`; trois passes IA et des sources opératorielles ne le
  transforment pas en preuve publiée.
- La borne obtenue dépend de `M`, de `kappa`, du cutoff et de l'opérateur
  fixé. Elle est uniforme en `R` et en temps, mais n'est pas petite.
- `GAP-TYPE-I-MOVING-COMMUTATOR-BOUND` est fermé pour ce choix.
  `GAP-TYPE-I-FORCE-COMPACTNESS` devient actif avant la rigidité forcée.
- La prochaine expérience déplace la couronne vers le facteur externe `L`
  et suit toutes les constantes avant tout passage `L->infinity`.

### 2026-08-15 — échappement local de la force, borne globale réfutée

- L'estimation directe de la queue de Leray est retenue avec le score
  `19/20`; la borne globale uniforme (`15/20`) et la topologie faible-étoile
  abstraite (`13/20`) ne sont pas sélectionnées.
- Un même opérateur de Bogovskii est dilaté. Changer de réalisation avec `L`
  n'est pas admis comme preuve d'une constante uniforme.
- Dans tout compact contenu dans `B_L`, `Q_LH=H` et les deux commutateurs
  s'annulent exactement. La pression globale de Riesz reste indispensable
  pour identifier `H=P_L div(U tensor U)`.
- La queue tensorielle n'est pas compacte : elle vaut `-U tensor U` au-delà
  de `B_(2L)`. Toutes les coquilles sont sommées, sans supposer l'absolue
  continuité du faible-Lorentz.
- `GAP-TYPE-I-FORCE-LOCAL-ESCAPE` est fermé avec taux spatial
  `L^(-3-|alpha|)`.
- La borne globale en `X` est abandonnée : `FAIL-NS-0080` donne une
  minoration `c|kappa|L²-C` pour la force complète sur un pure-swirl
  cinématique.
- Le signe du drift est fixé à `+kappa D` au membre gauche; le signe opposé
  détecté pendant la passe formelle est rejeté.
- La diagonale physique doit vérifier `L_jR_j->0`; aucune fonction `L(t)`
  variable n'est introduite.
- Le prochain verrou est `GAP-TYPE-I-LOCAL-COMPACTNESS-TRACE`, avant
  dérenormalisation et rigidité ancienne faible-`L3`.

### 2026-08-15 — compacité adaptée locale et pivot vers la trace

- La passe contradictoire corrige le brouillon initial : faible-`L3` seul ne
  donne pas d'énergie, mais faible-`L3` **plus l'équation lisse**, la pression
  de Riesz et la force localement bornée ferment une Caccioppoli uniforme.
- Le remplissage des trous est retenu avec le score `19/20`; la régularité
  parabolique sous-critique reste une route de secours et aucun endpoint
  Calderón–Zygmund parabolique n'est invoqué.
- Simon est appliqué avec les triplets exacts
  `L2 compact->H^-1->W^(-2,4/3)` puis
  `H1 compact->L2->W^(-2,4/3)`.
- La convergence est forte dans tout `Lq_loc`, `q<10/3`, donc dans `L3`; le
  produit converge dans `L^(3/2)` et l'énergie locale passe.
- La pression complète n'est pas déclarée fortement compacte : sa partie
  proche converge fortement et sa partie harmonique passe faible-étoile.
- `GAP-TYPE-I-LOCAL-DISTRIBUTIONAL-COMPACTNESS` et
  `GAP-TYPE-I-LOCAL-SUITABILITY-ENERGY` sont fermés au statut interne
  `COMPUTATION_ONLY`.
- La transmission d'une norme terminale est abandonnée : `FAIL-NS-0081`
  montre qu'elle n'impose aucun moment fixe.
- `GAP-TYPE-I-CRITICAL-TRACE-PERSISTENCE` devient actif, avant horloge,
  mildness et rigidité ancienne faible-`L3`.

### 2026-08-15 — non-trivialité intégrée sous capture Type I persistante

- L'intégration de la capture obtient `19/20`; la persistance A.5 et la
  construction directe d'un moment signé obtiennent chacune `15/20`.
- Le quantificateur « tout temps tardif » de Barker–Prange est conservé. Il
  ne doit plus être réduit à une information sur la tranche terminale.
- L'horloge est fixée par `d(log R)/d sigma=-kappa`; sur une fenêtre fixe,
  `R(sigma_j+s)/R_j=exp(-kappa s)`.
- `Q_(L_j)` est exactement l'identité dans `B_1`; aucune convergence de
  cutoff ni centre mobile n'est utilisée pour la capture.
- La forte `L3` espace–temps conserve la masse cubique intégrée. Une trace
  prescrite au temps zéro n'est pas nécessaire pour conclure que la limite
  ancienne est non nulle.
- `FAIL-NS-0081` reste valide pour une tranche isolée. `FAIL-NS-0082` réfute
  uniquement la nécessité du moment signé dans la suite Type I persistante.
- Le claim reste `COMPUTATION_ONLY` : la composition est interne, même si la
  capture est publiée et les ingrédients de compacité sont sourcés.
- Le verrou actif devient `GAP-TYPE-I-DERENORMALIZATION-CLASS`; la
  singularité terminale, la mildness et la rigidité restent séparées.

### 2026-08-15 — classe dérenormalisée fixée avant rigidité

- La conjugaison exacte de l'équation, de la pression et de l'énergie locale
  obtient `18/20`; la promotion mild et l'application directe d'une rigidité
  obtiennent chacune `15/20` et ne sont pas sélectionnées.
- L'horloge est fixée par `tau=(1-e^(-2kappa s))/(2kappa)`; sur `s<=0`, elle
  couvre exactement `tau<=0`. Le signe, l'amplitude, la pression et le
  jacobien sont désormais des invariants testés, pas des conventions libres.
- La pression globale de Riesz est retenue seulement après extraction
  faible-étoile du produit dans `L^(3/2,infinity)` et identification par la
  forte convergence locale.
- `NS-TYPE-I-DERENORMALIZED-ANCIENT-LOCAL-SUITABLE` reste
  `COMPUTATION_ONLY`; une identité algébrique et deux revues IA ne valent pas
  une preuve publiée indépendante.
- `FAIL-NS-0083` interdit les promotions automatiques vers Leray–Hopf ou
  mild. Il ne réfute pas un raccord PDE futur vers une classe scindée.
- `GAP-TYPE-I-DERENORMALIZATION-CLASS` est fermé au statut interne. Le verrou
  actif devient `GAP-TYPE-I-ANCIENT-WEAK-L3-RIGIDITY-OR-MILDNESS`.

### 2026-08-15 — Duhamel faible-étoile fermé, énergie relative sélectionnée

- La construction Duhamel et du correcteur obtient `17/20`; le split BSS
  direct obtient `15/20` et le Liouville direct `12/20`.
- Le représentant `C_w*L^(3,infinity)` est construit avant d'écrire la
  formule pour tous les temps de redémarrage.
- L'estimation de Yamazaki est utilisée dans son ordre de quantificateurs
  exact : pairing fixé puis intégration. L'intégrale est de Gelfand, pas de
  Bochner.
- Le gain sous-critique est retenu en espace **fort** `L^p` pour
  `3/2<p<3`; à `p=2`, le correcteur est `C_tL2` avec taux `h^(1/4)`.
- La continuité forte critique, la dissipation BSS et la bornitude KNSS ne
  sont pas promues. `NS-WEAK-L3-DUHAMEL-L2-CORRECTOR` reste
  `COMPUTATION_ONLY`.
- `FAIL-NS-0084` enregistre le logarithme endpoint, le profil solénoïdal à
  queue persistante et l'absence d'implication `C_tL2 -> L2_tHdot1`.
- Le verrou actif devient `GAP-TYPE-I-RELATIVE-ENERGY-GLOBALIZATION` :
  cutoffs, flux de pression et défaut d'énergie à l'infini doivent être
  suivis sans tester circulairement par le correcteur.

### 2026-08-15 — énergie relative globalisée sur bande finie

- La globalisation relative obtient `18/20`; la régularité maximale Duhamel
  `14/20` et l'identification par unicité BSS `11/20`.
- La première passe combine le flux total, l'inclusion Lorentz locale et
  Sobolev, puis absorbe avec un reste `O(R^-1)` indépendant du rayon.
- Le coefficient critique `||V||_4^8~h^-1` n'est jamais intégré seul : le
  taux déjà établi de `w` le transforme en `h^-1/2`.
- Une seconde passe est exigée pour retrouver le signe exact du transfert;
  la première ne sert qu'à construire la dissipation.
- `NS-SRC-0192` confirme le transfert publié une fois la classe d'énergie
  supposée, mais pas sa construction. Le claim interne reste donc
  `COMPUTATION_ONLY`.
- `FAIL-NS-0085` enregistre le contre-profil multi-annulaire et interdit la
  promotion depuis les seules normes fonctionnelles.
- Le prochain verrou est la cohérence des scissions quand le temps de base
  tend vers moins l'infini, puis la rigidité ancienne ou la mildness forte.

### 2026-08-15 — cocycle exact, uniformité ancienne réfutée fonctionnellement

- Le cocycle des correcteurs et l'énergie de la transition calorifique sont
  retenus comme lemmes exacts; aucune unicité faible à grande donnée n'est
  utilisée.
- Le quotient `X/(L2 inter X)` reste algébrique et non séparé. Toute
  formulation topologique passe par `X/closure_X(L2 inter X)`.
- `U` et `U_sharp` sont conservés comme contre-profils calorifiques. Leur
  croissance `h^(1/4)` et le résidu `8pi/3` interdisent d'inférer une borne
  ancienne uniforme depuis le seul cocycle, mais leur défaut PDE interdit
  toute conclusion sur une vraie solution Navier--Stokes.
- `GAP-TYPE-I-BSS-BASE-TIME-COHERENCE` est fermé algébriquement. Le prochain
  test doit exploiter un effet PDE de tightness des queues ou de basse
  fréquence; rejouer la contraction calorifique seule est abandonné.
