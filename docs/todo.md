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
- [ ] Construire ou exclure une cascade multicoeur sans axe global : définir
  une mesure d'occupation angulaire, suivre la non-dégénérescence de sa
  moyenne active, le faible-`L^(3/2)`, Biot–Savart et le résidu visqueux.
- [ ] Quantifier une formulation pré-singulière cohérente par rayon de cœur
  `r_c(t)` ou convergence de profils remis à l'échelle.
- [ ] Formaliser le lemme scalaire de séparation de phases
  `MO>=4ab/(a+b)` dans un environnement épinglé.
- [ ] Formaliser la rigidité sous récurrence de dilatation du cycle 0021.
- [ ] Obtenir une revue externe indépendante du lemme du cycle 0018.
