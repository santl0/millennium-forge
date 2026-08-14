# Cycle 0007 — Héritage des propriétés sous zoom

Date : 2026-08-14.

## Décision du cycle

Trois actions ont été notées : matrice exacte ESS/GKP/KNSS/Seregin et test de
non-composition (19/20), preuve directe par backward uniqueness du Liouville
borné à trace nulle (15/20), transfert des nouveaux Liouville
stationnaires/auto-similaires 2026 (13/20). La première est retenue : elle
attaque le raccord logique préalable à tout nouveau théorème de rigidité.

## Équation et type de solution

Les objets comparés ne sont pas interchangeables :

- ESS : NS 3D visqueux, paire éternelle adaptée dans `L∞_tL³_x`;
- GKP : NS 3D visqueux, solution forte/mild forward dans `L³`;
- KNSS : NS visqueux sur `R^n`, ancienne mild à vitesse bornée;
- Seregin `2606.29468v1` : ancienne Euler dissipative issue d'un zoom Type II
  conditionnel de NS.

Toutes les chaînes sont non forcées et sans frontière dans leur domaine
limite. La viscosité est `1` dans les trois premières et disparaît dans la
quatrième.

## Échelle des quantités

Sous `u_lambda=lambda u(lambda x,lambda²t)`, `L³_x` est invariant. Une borne
ponctuelle globale n'est pas la même donnée : KNSS choisit l'échelle par le
maximum afin d'obtenir `|v|<=1` et `|v(0,0)|=1`. Les zooms Type II d'échelle
Euler modifient le coefficient visqueux jusqu'à zéro. Enfin, une trace nulle
est une propriété de convergence topologique (`L²_loc` chez ESS, `S'` chez
GKP), pas une norme que l'on peut transporter par simple comptage d'échelle.

## Affirmations ajoutées ou modifiées

- `NS-HYBRID-ANCIENT-GATE-NOT-INHERITED`, `COMPUTATION_ONLY` : aucune chaîne
  unique du corpus fermé ne transmet le paquet hybride.
- L'extraction ESS est corrigée : limite éternelle et non-trivialité
  `>=epsilon_*`.
- La ligne KNSS sépare mildness de toute convergence explicite de pression.
- Cinq sources récentes sont ajoutées sous `NS-SRC-0044` à `0048`, sans claim
  théorématique promu.

## Preuve / source / calcul

La matrice contient treize propriétés et quatre chaînes. Une porte est franchie
si toutes ses propriétés valent `SOURCE` ou `INFERENCE` dans une **même**
colonne. Les contrôles exacts retrouvent une colonne pour la porte ESS, une pour
la sortie KNSS, une pour la limite Euler Type II, et aucune pour

```text
NS visqueux + ancien + mild + borne globale de vitesse
+ trace terminale L²_loc nulle + non-trivialité.
```

La seule couverture minimale de ce paquet par une réunion de colonnes est
`ESS_LOCAL_L3_ZOOM + KNSS_MAXIMUM_ZOOM`. Puisqu'il s'agit de deux objets
limites produits par deux normalisations différentes, cette couverture n'est
pas une implication mathématique.

Empreintes :

- matrice :
  `798d661f73056b12c5502af6c0548241c23a0e11adb3b7ba3cb73beddb2a3657`;
- validateur :
  `4c2f6711491d062191276093c180f8f155942a2d8f75d254ede70a181593791a`.

## Veille différentielle

Les pages et énoncés primaires ciblés ont été contrôlés pour :

- Cheskidov–Hou `arXiv:2603.03666v2`, mildness singulière dans des Besov
  négatifs, hors classe KNSS/Clay;
- Seregin `arXiv:2402.13229v3`, révisé le 8 août 2026, Type II axisymétrique de
  limite Euler sans swirl;
- Wang–Yang `arXiv:2608.06040v1`, Liouville stationnaire pour `D`-solutions
  sous décroissance;
- Binz–Coiculescu `arXiv:2607.12159v1`, profils homothétiques forward;
- Seregin `arXiv:2507.08733v2`, anciennes Euler dissipatives conditionnelles.

Aucun ne fournit la combinaison hybride ni un Liouville ancien mild borné 3D
général. L'HTML de `2402.13229v3` affiche une formule de `C(v,r)` incompatible
avec l'invariance annoncée; l'anomalie est consignée, non réparée par le
laboratoire.

## Écart avec le problème Clay

Le résultat ne démontre ni régularité ni blow-up. Il élimine une inférence de
preuve : emprunter la trace ESS et la bornitude/mildness KNSS. Les chaînes ESS
et GKP ferment déjà leur rigidité sous la borne critique `L³`, non issue de
l'énergie Clay. KNSS ne fournit aucun Liouville 3D général. Les zooms Type II
Seregin produisent Euler sous hypothèses supplémentaires.

## Test adverse et résidu certifié

Le validateur contrôle vocabulaire, complétude des treize colonnes, exclusivité
des équations obtenues, compatibilité des traces et correspondance exacte des
quatre portes. Résultat : `assertion_failure_count=0`, sans flottant.

Trois passes séparées ont attaqué les notions de trace, de pression, de
mildness et de domaine temporel. Elles ont détecté et fait corriger :

1. `>epsilon_*` en `>=epsilon_*` pour ESS;
2. « ancienne » en « éternelle, puis restreinte » pour ESS;
3. une jauge de pression trop forte attribuée à KNSS;
4. des noms d'auteurs erronés dans un signal de veille, remplacés depuis les
   métadonnées primaires.

## Artefacts mis à jour

Matrice et validateur, protocole d'expérience, claim, extraction primaire,
registre de sources, veille, état de l'art, audit des sources, graphe,
questions, carte adaptative, journal supercritique, registre d'échecs et ce
checkpoint.

## État : continuer

L'approche hybride sans raccord est abandonnée. Le Liouville abstrait reste un
candidat distinct et non promu.

## Prochaine expérience décisive

Auditer les hypothèses exactes du théorème de backward uniqueness utilisé par
ESS et les estimations de dérivées des anciennes mild bornées de KNSS. Tenter
une preuve à constantes suivies de :

```text
ancienne mild globalement bornée + u(t)->0 dans D' quand t->0-
  => u=0,
```

puis tester séparément, sans permutation des limites, si une construction de
blow-up connue transmet jamais ces prémisses sur le même objet.
