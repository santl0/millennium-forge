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
- [ ] Calibrer `AR/K_u` sur la composante sélectionnée ou construire une
  retroncature certifiée sur son arbre de fusion qui conserve le rapport
  endpoint et produit des morceaux de diamètre `O(R)`.
- [ ] Étendre ou réfuter le registre lorsque les supports de curl se
  chevauchent et peuvent s'annuler.
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
