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
