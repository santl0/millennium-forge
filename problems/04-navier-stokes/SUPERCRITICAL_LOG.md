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
