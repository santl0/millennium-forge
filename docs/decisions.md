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
