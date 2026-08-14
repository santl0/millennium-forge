# Journal supercritique et contre-profils

Journal append-only. Chaque entrée fixe l'équation, le domaine, la notion de
solution ou précise qu'il s'agit seulement d'un champ test.

## 2026-08-14 — Échelle NS

- Équation : NS incompressible 3D, `R^3`, viscosité inchangée.
- Transformation : `u_lambda=lambda u(lambda x,lambda^2 t)`.
- Lois : `||u_lambda||_q=lambda^(1-3/q)||u||_q`,
  `||u_lambda||_dotH^s=lambda^(s-1/2)||u||_dotH^s`,
  `||u_lambda||_2²=lambda^-1||u||_2²`.
- Perte : l'énergie est supercritique vers les petites échelles; aucune
  interpolation entre énergie et dissipation ne donne seule `L∞_tL³_x`.
- Test adverse futur : paquets divergence-free concentrés et séparés.

## 2026-08-14 — Porte visqueuse d'un profil mono-échelle

- Objet : ansatz formel, pas solution démontrée.
- Domaine : localement `R^3`; `tau=T-t`.
- Calcul : inertie `~tau^(lambda-1)`, viscosité
  `~nu tau^(-lambda-2)`, rapport `~nu tau^(-1-2lambda)`.
- Seuil : perturbatif seulement pour `lambda<-1/2`, équilibré pour
  `lambda=-1/2`, dominant pour `lambda>-1/2`.
- Contre-portée : ne traite pas une cascade multi-échelle ni une annulation de
  `Delta U`.
- Artefact : `VAS-1`, résidu rationnel zéro.

## 2026-08-14 — Contre-triade de flux

- Objet : champ test réel divergence-free, pas trajectoire.
- Domaine : tore tridimensionnel normalisé.
- Modes : `+-a`, `+-b`, `+-c`, avec `c=a+b`.
- Invariants : `E=6`, `Z=9N²`, hélicité nulle mode par mode.
- Transfert : `Pi_N=-2 sigma N`, donc ratio au carré `1/54`.
- Conclusion négative : ni divergence nulle, ni hélicité globale nulle ne
  produisent un facteur universel `epsilon_N->0`.
- Résidus : tous nuls en rationnels gaussiens.

## 2026-08-14 — Désingularisation d'un profil homogène `-1`

- Objet : donnée initiale sur coquille, pas évolution PDE.
- Domaine : `R^3`, `u_0=r^-1 A(theta)` pour `epsilon<=r<=1`.
- Intégrale : `||u_0||_q^q=C_q integral_epsilon^1 r^(2-q)dr`.
- Seuil : borné pour `q<3`, logarithmique pour `q=3`, puissance pour `q>3`.
- Régularité : `||nabla u_0||_2²=C_grad(epsilon^-1-1)` si
  `C_grad>0`.
- Obstacle : aucune constante de stabilité dépendant uniformément de ces normes
  ne survit au cutoff; une stabilité exotique n'est pas exclue.
- Artefact : `DESINGULARIZATION-GATE-1`, résidu rationnel zéro.

## 2026-08-14 — Pression multi-échelle après zoom

- Objet : suite de données lisses compactes divergence-free, pas trajectoire.
- Échelles : distance `L_n=2^-6n`, zoom `r_n=2^-7n`, moment
  `mu_n=2^-3n`, distance rescalée `R_n=2^n`.
- Énergie : `||v_n||_2²=2mu_n->0`, mais
  `||r_n v_n(r_n·)||_2²=2R_n^4`.
- Quantité critique de queue :
  `Theta_n(A)=integral_(|y|>A)|U_n(y)|²|y|^-4dy`.
- Contre-profil : pour tout `A`, des indices avec `R_n>A` gardent
  `Theta_n(A)` proche de `2`; la pression centrée converge vers `3/(4pi)`.
- Perte localisée : l'énergie globale ne donne aucune tension uniforme après
  des zooms plus fins que l'échelle porteuse de l'énergie.
- Artefact : `PRESSURE-MULTISCALE-1`, résidus rationnels zéro.

## 2026-08-14 — Couche initiale oscillatoire et défaut de trace

- Équation : NS incompressible 3D périodique, `nu=1`, sans force, solutions
  globales analytiques explicites.
- Fréquence et temps : fréquence principale `N`, dissipation `N²+1`, temps
  d'observation `t_N=log(2)/(N²+1)`.
- Énergie : `||u_N^0||_2²=(1/4)(1+N^-2)` avec moyenne normalisée; elle est
  uniforme et reste d'ordre un au temps `t_N`.
- Défaut : la vitesse converge faiblement vers zéro, mais son carré conserve
  le mode lent `(1/8)sin²(x_1)`; la projection de Leray produit la pression
  lente `(1/16)cos(2x_1)`.
- Perte localisée : aucune compacité forte uniforme des traces aux temps
  paraboliques mobiles ne suit de la seule énergie. À temps fixé positif, la
  chaleur élimine le défaut.
- Artefact : `QUADRATIC-PRESSURE-DEFECT-1`, résidus rationnels zéro.

## 2026-08-14 — Perte d'une puissance dans le module temporel

- Équation : loi d'échelle NS sur `R³`; estimation énergétique et contre-test
  exact périodique.
- Loi générale :
  `[u_lambda]_(C_t^alpha dot H_x^sigma)
  =lambda^(sigma-1/2+2alpha)[u]`.
- Seuils critiques : `C_t^(1/4)L²` et `C_t^(3/4)dot H^-1`.
- Contrôle énergétique : l'équation et Gagliardo–Nirenberg donnent seulement
  `C_t^(1/4)H^-1`, de facteur d'échelle `lambda^-1`.
- Contre-profil : sur la famille exacte, les quotients critiques croissent
  comme `N^(1/2)`, alors que le quotient énergétique faible décroît comme
  `N^(-1/2)`.
- Perte localisée : une dérivée spatiale négative n'est compensée par aucun
  gain temporel critique; la compacité faible de trajectoire ne devient pas une
  compacité forte de trace.
- Artefact : `TRACE-MODULUS-1`, résidus rationnels zéro.

## 2026-08-14 — Mode zéro et pression harmonique ancienne

- Équation : NS incompressible non forcé sur `R³ x (-infinity,0]`.
- Contre-profil : `u=b(t)e_1` avec `b=-t/(1+t²)` et
  `p=-b'(t)x_1`.
- Échelle spatiale : mode de fréquence zéro; convection et viscosité
  s'annulent. L'évolution est entièrement portée par une pression affine
  harmonique, invisible à l'équation de Poisson.
- Bornes : `||u||_infinity=1/2`, mais toutes les normes globales `L^q_x` finies
  avec `q<infinity` divergent pour les temps où `b(t) !=0`.
- Perte localisée : la régularité locale, l'adaptation et la trace terminale ne
  fixent pas la composante harmonique de pression au domaine infini.
- Porte positive : mildness, pression BMO modulo constantes, ou jauge
  Leray/Riesz force `b'=0` dans la classe spatialement constante.
- Artefact : `ANCIENT-PRESSURE-GAUGE-1`, résidus rationnels zéro.

## 2026-08-14 — Héritage non composable des zooms de blow-up

- Équations : ESS, GKP et KNSS conservent Navier–Stokes de viscosité `1`;
  le zoom Type II Seregin encodé fait tendre la viscosité effective vers zéro
  et produit Euler.
- Échelles : `L³_x` est invariant sous `u_lambda=lambda u(lambda x,lambda²t)`;
  la borne ponctuelle est normalisée par le maximum dans KNSS mais n'est pas
  une borne `L³` globale. Une trace terminale est une propriété topologique,
  pas une norme interchangeable avec ces deux contrôles.
- ESS : limite éternelle, `L∞_tL³_x`, trace forte `L²_loc` nulle, pression
  proche/lointaine suivie, non-trivialité énergétique `>=epsilon_*`.
- GKP : élément critique mild forward, niveau `A_c`, trace seulement `S'` au
  temps maximal; aucune ancienne extraite par ce théorème.
- KNSS : ancienne mild, vitesse globalement bornée, normalisation
  `|v(0,0)|=1`; aucune convergence de pression ni trace nulle.
- Perte localisée : la réunion ESS+KNSS couvre formellement le paquet
  « ancienne + mild + bornée + trace nulle », mais les propriétés appartiennent
  à deux objets et deux normalisations. Aucun passage à la limite ne réalise
  leur intersection.
- Artefact : `BLOWUP-INHERITANCE-AUDIT-1`, treize propriétés, quatre chaînes,
  zéro échec d'assertion exacte.

## 2026-08-14 — Lissage d'une ancienne mild bornée et trace terminale

- Équation : NS incompressible 3D non forcé sur
  `R³ x (-infinity,0)`, viscosité `1`, solution ancienne mild au sens KNSS.
- Hypothèses : `M=sup|u|<infinity` et vraie limite `u(t)->0` dans `D'` quand
  `t->0-` sur le même objet.
- Échelle : `nabla^k partial_t^l u` porte le facteur
  `lambda^(k+2l+1)` sous `u_lambda=lambda u(lambda x,lambda²t)`.
- Borne redémarrée : la proposition 4.1 de KNSS, appliquée à distance
  `h=epsilon_(k,l)/(2M²)` avant chaque temps, donne
  `||nabla^k partial_t^l u||_infinity <= C_(k,l) M^(k+2l+1)` avec constante
  indépendante de la distance au bord terminal.
- Conséquence : la trace distributionnelle devient nulle dans `C^m_loc`; la
  vorticité satisfait l'unicité rétrograde ESS sur chaque bande finie. La
  mildness élimine ensuite le mode spatial constant.
- Perte localisée : la classe `L-infinity_(x,t)` est sous-critique pour la
  vitesse et n'est pas héritée par l'extraction ESS; la trace nulle n'est pas
  héritée par l'extraction maximum-normalisée KNSS. La rigidité ne crée donc
  aucune borne critique depuis l'énergie.
- Artefact : `ANCIENT-ZERO-TRACE-RIGIDITY-AUDIT-1`, neuf obligations directes,
  cinq contre-profils, résidu d'assertion nul.

## 2026-08-14 — Trace mobile et concentration critique du zoom maximum

- Équation : NS incompressible 3D non forcé sur `R³`, viscosité `1`, zooms
  mild KNSS centrés sur des temps records d'un temps maximal fini supposé.
- Horloges : `s=0` représente le temps-record physique `t_k`; le temps
  singulier `T` représente l'extrémité future mobile
  `B_k=M_k²(T-t_k)>0`. La commutation ci-dessous ne porte donc pas sur `T`.
- Pairing exact : pour un test fixe `phi` dans les variables zoomées,

  ```text
  <v_k(s),phi>
    =M_k² integral u(x,t_k+s/M_k²) phi(M_k(x-x_k)) dx.
  ```

  La trace physique agit donc sur des tests mobiles de taille `M_k²`, supportés
  à l'échelle `M_k^-1`; la convergence contre chaque test physique fixe ne se
  transfère pas automatiquement.
- Échelle locale :
  `integral_(B_R)|v_k|^q=M_k^(3-q)
  integral_(B_(R/M_k)(x_k))|u|^q`. Le seuil invariant est exactement `q=3`.
- Dynamique mild : la borne passée `|v_k|<=2` fournit des modules spatiaux et
  temporels uniformes jusqu'au temps-record `s=0`. Les deux limites y
  commutent; la normalisation donne une valeur commune non nulle.
- Concentration : une borne normalisée `||nabla v_k(0)||_infinity<=G` force
  une masse critique au moins `pi/(48G³)` dans
  `B_(1/(2GM_k))(x_k)`.
- Perte localisée : une simple borne globale `L³` n'impose pas
  l'équi-intégrabilité uniforme de `|u(t_k)|³`. Supposer cette
  équi-intégrabilité exclut déjà le blow-up maximum-normalisé; ce n'est ni un
  raccord gratuit vers une trace nulle, ni un nouveau critère, car la condition
  (23) plus faible de Constantin 2023 donne déjà un prolongement quantitatif.
- Artefact : `MAXIMUM-ZOOM-TRACE-COMMUTATOR-1`, neuf obligations, résidu
  d'assertion nul.

## 2026-08-14 — Couche intérieure d'une donnée homogène `-1`

- Équation : données initiales pour NS incompressible 3D non forcé sur `R³`,
  viscosité `1`; aucune évolution résolue dans le test.
- Source : la localisation Hou–Wang–Yang est extérieure. Pour `p=4`, son
  petit paramètre `R^-1/8` enlève la queue, mais laisse intact le coeur `1/r`.
- Échelles : sous `u_lambda=lambda u(lambda x)`, `L³` et
  `L^{3,infinity}` sont invariants, `L²` porte `lambda^-1/2`, `Hdot¹` porte
  `lambda^1/2` et `L-infinity` porte `lambda`.
- Famille exacte : cutoffs radiaux du swirl
  `a=(-x_2,x_1,0)/|x|²`; divergence nulle sans projection grâce à
  `x dot a=0`.
- Bornes : distance au profil singulier infinie en `L³`, minorant uniforme en
  `L^{3,infinity}`, mais distance `L²=O(epsilon^1/2)`. La donnée lisse a
  `||nabla u_epsilon||_2` au moins d'ordre `epsilon^-1/2`.
- Contre-compacité : `u_epsilon` et `u_(2epsilon)` restent séparés par une
  constante positive dans `L³`, tout en devenant proches dans `L²` et en
  restant uniformément bornés dans `L^{3,infinity}`.
- Perte localisée : une borne critique **faible** ne somme pas les
  `log(1/epsilon)` échelles actives; elle ne remplace donc pas une compacité
  critique forte. La chaleur peut encore lisser à `t>0`, ce qui laisse ouvert
  un shadowing dynamique non perturbatif après `t~epsilon²`.
- Artefact : `HWY-INNER-CUTOFF-GATE-1`, résidus rationnels et arrondi zéro.
