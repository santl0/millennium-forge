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

## 2026-08-14 — Couche parabolique et sélection de parité HWY

- Équation : NS incompressible 3D non forcé sur `R³`, viscosité `1`; solution
  forte locale pour la symétrie et linéarisation en variables de similarité
  autour du profil HWY.
- Involution : `(Ju)(x)=S u(Sx)`, `S=diag(1,1,-1)`. Le profil et le lissage
  radial sont pairs; le mode instable certifié est impair.
- Non-localité : le symbole de Leray vérifie `P(Sxi)=S P(xi)S`. La pression
  projetée ne mélange donc pas les secteurs dans le cadre exact symétrique.
- Échelle : si `g_epsilon=epsilon^-1g(x/epsilon)` et
  `t=kappa epsilon²`, alors le profil chauffé redimensionné est indépendant
  d'`epsilon`. La petitesse énergétique physique ne devient pas une petitesse
  dans l'espace de profil.
- Amplification conditionnelle : une coordonnée impaire
  `epsilon^beta` porte `kappa^-a epsilon^(beta-2a)`; la borne
  `a>=217/2000` impose `beta>=217/1000`, mais une couche `O(1)` quitte le
  régime perturbatif à `O(epsilon²)` et la balance non linéaire reste entière.
- Annulation exacte : `Q_-g_epsilon=0`; le mode certifié ne peut pas être
  excité par la régularisation symétrique avant perte de l'unicité forte.
- Perte localisée : pour l'asymétrie, il manque un adjoint certifié, son
  conditionnement, la simplicité/isolation spectrale et les contributions de
  cutoff/pression. Un mode instable pair n'est pas exclu.
- Artefact : `HWY-PARITY-PROJECTION-GATE-1`, dix résidus rationnels nuls,
  opérateur adverse non équivariant explicitement détecté.

## 2026-08-14 — Trace asymptotique versus donnée de Cauchy finie

- Équation : NS incompressible 3D non forcé sur `R³`, viscosité `1`; solution
  forte `u` et solution de Leray–Hopf `v` sur le même intervalle.
- Identité : pour `E=(1/2)||v-u||²_2`,
  `dE/dt+||nabla(v-u)||²_2<=2||nabla u||_infinity E`. La constante `2` est
  exacte avec cette normalisation.
- Porte : si `integral ||nabla u||_infinity dt<infinity` et les données à un
  temps fini coïncident, Grönwall impose la coïncidence des solutions. Cette
  hypothèse est locale à l'intervalle fort; aucune borne jusqu'à un hypothétique
  temps singulier n'est revendiquée.
- Échelle : une différence de mode HWY
  `(c-d)t^(a-1/2) v(x/sqrt(t))` vérifie
  `||delta u(t)||²_2=|c-d|² t^(2a+1/2)||v||²_2`. Elle peut tendre vers zéro en
  `L²` à la trace tout en restant non nulle pour chaque `t>0`.
- Contre-modèle : `b_A=aAq/(a+Aq)`, `q=exp(a tau)`, partage la trace zéro mais
  vérifie `b_A/q->A` et `A=ab/[q(a-b)]` à temps fini.
- Pression : le gradient de pression s'annule dans le pairing global grâce à
  la divergence nulle. Cette annulation ne donne aucune localisation uniforme
  de la pression ni contrôle de couche asymétrique.
- Perte localisée : le passage `tau=-infinity -> tau0 fini` perd une coordonnée
  asymptotique; ce n'est pas une interpolation critique. La seule porte pour
  plusieurs continuations depuis le même état est la perte de la classe forte,
  exactement le verrou Clay.
- Artefact : `ASYMPTOTIC-TRACE-CAUCHY-GATE-1`, résidus rationnels nuls et aucun
  flottant.

## 2026-08-14 — Cohérence locale de vorticité et strain lointain

- Équation : donnée analytique pour NS incompressible 3D non forcé sur `T³`,
  viscosité positive; identité évaluée à l'instant initial.
- Famille : `u_a=(sin y+a sin x cos z,0,-a cos x sin z)`, `a=+-1`.
  Le changement de signe est une translation spatiale exacte.
- Quantités testées : `E=1/2`, `Z=3/4`, palinstrophie `5/2`, hélicité zéro,
  `omega(0)=-e_3`, `Domega(0)=0` pour les deux champs.
- Signe : `omega·S omega=-a cos x cos z cos²y`; il vaut `-a` au centre et
  garde ce signe sur `Q_r` avec module au moins `(1-r²/2)^4`.
- Cohérence : le sinus de l'angle centre–boule est au plus
  `2r²/(1-r²/2)`; le module pairwise `L¹` est au plus
  `2r/(1-r²/2)`. Le premier tend vers zéro sans dépléter le stretching.
- Pression/non-localité :
  `p_a=(a²/4)(cos 2x+cos 2z)` est reconstruite exactement et paire en `a`.
  Le défaut est le contrôle global du strain de Biot–Savart, pas une pression
  locale oubliée.
- Échelle : pour `U_N=N u(Nx)`, énergie `N²`, enstrophie `N⁴`, stretching
  `N⁶`, ratio critique ponctuel invariant. La cohérence au rayon critique ne
  s'accompagne donc pas ici d'une borne énergétique uniforme.
- Perte localisée : passer d'une direction locale à `S` perd la queue lointaine
  et l'ordre des quantificateurs. Les critères high–high uniformes en temps ne
  sont pas attaqués.
- Artefact : `VORTICITY-LOCAL-COHERENCE-SIGN-GATE-1`, tous résidus exacts
  nuls; `FAIL-NS-0016`.

## 2026-08-14 — Restriction de sparseness et seuil de rayon

- Objet : ensemble borélien dans `R³`; application conditionnelle à un
  superniveau d'une solution mild analytique de NS incompressible 3D non forcé.
- Échelle : sous `u_kappa(x,t)=kappa u(kappa x,kappa²t)`, l'amplitude porte
  `kappa`, le volume du superniveau relatif `kappa^-3` et le rayon construit
  `kappa^-1`. Les densités volumique et linéaire sont invariantes.
- Lemme sharp : densité 3D `≤delta` dans `B_r(x_0)` implique une direction de
  densité linéaire `≤delta^(1/3)` au même rayon. La boule concentrique sature.
- Rayon : depuis `|V|≤B`, le seul volume garantit
  `r³≥B/(delta|B_1|)`. Pour `delta=3/4`, le seuil est `r³≥B/pi`.
- Correction de quantificateur : le rayon minimal réel est majoré par le rayon
  calculé depuis le majorant global; cela n'autorise pas un rayon arbitraire
  plus petit. Une boule centrale donne une densité un à petite échelle.
- Gain/perte : le maillon géométrique est critique et sans perte de constante.
  Le gain logarithmique éventuel vient entièrement du majorant PDE amont, non
  de la restriction géométrique.
- Artefact : `SPARSENESS-RESTRICTION-1`, fractions rationnelles exactes,
  résidus algébriques nuls, statut `COMPUTATION_ONLY`.

## 2026-08-14 — Inversion logarithmique des réarrangées

- Objet : fonction mesurable sur un espace non atomique de dimension de volume
  trois; application conditionnelle à la vitesse d'une solution mild
  analytique de NS incompressible 3D non forcé sur `R³`.
- Hypothèse : `f*(v)≤A v^(-1/3)/log(eV_*/v)` pour `0<v≤v_0`, avec
  `A,V_*,v_0` uniformes dans le paramètre temporel.
- Pseudo-inverse exact : `mu_f(lambda)>v` si et seulement si
  `f*(v)>lambda`. L'identité au point terminal est fausse sur les plateaux.
- Conclusion : au-dessus du seuil imposé par `v_0` et
  `Lambda_*=A V_*^(-1/3)`,
  `mu_f(lambda)≤A³/[lambda³(1+3log(lambda/Lambda_*))³]`.
- Échelle : sous `u_kappa(x,t)=kappa u(kappa x,kappa²t)`, `A` est invariant,
  `V_*` et `mu` portent `kappa^-3`, `Lambda_*` et `lambda` portent `kappa`;
  le rapport logarithmique est invariant.
- Optimalité : l'enveloppe saturante a une inverse asymptotique
  `A³/[27lambda³log³(lambda/Lambda_*)]`; ni la puissance trois ni le facteur
  principal `1/27` ne s'améliorent sans nouvelle structure.
- Perte localisée : un cutoff `v_0(t)` qui tend vers zéro détruit le seuil
  uniforme même si `A` reste fixe. L'obtention PDE de l'enveloppe et la jauge
  harmonique de Biot–Savart restent ouvertes.
- Artefact : `REARRANGEMENT-INVERSION-1`, fractions et encadrements rationnels
  de logarithmes, aucun flottant, statut `COMPUTATION_ONLY`.

## 2026-08-14 — Transfert O'Neil et reste sous-dominant

- Équation : NS incompressible 3D non forcé sur `R³`, viscosité positive;
  application conditionnelle à une solution analytique avant `T*`.
- Entrée : queue uniforme de vorticité
  `mu_omega(lambda)<=V[(Omega/lambda)/log(lambda/Omega)]^(3/2)` au-dessus de
  `eOmega`, plus `M=sup_s s^(2/3)omega*(s)<infinity`.
- Inversion : pour `s<=Vexp(-3)`,
  `omega*(s)<=4Omega(V/s)^(2/3)/log(eV/s)`.
- O'Neil : le coeur coûte `3C_0`, la queue logarithmique `20C_0` et la queue
  globale `9M`, avec `C_0=4Omega V^(2/3)`.
- Jauge : si `u=B[omega]+h`, `||h||_infinity<=H`, alors le coefficient final
  est `Q=C_K(23C_0+9M)+HV^(1/3)`.
- Reste de (46) : il n'est pas borné;
  `R(v)~9v^(-1/3)/log²(e/v)`. Le ratio au terme principal est
  `O(1/log(e/v))`, donc l'absorption conserve un logarithme entier.
- Échelle : `C_0`, `M` et `HV^(1/3)` sont invariants; `v^(-1/3)` porte
  `kappa`, exactement comme la vitesse.
- Pertes localisées : une queue à grande amplitude sans seuil uniforme ne
  fournit aucun cutoff commun; une enveloppe aux petits volumes sans contrôle
  global laisse diverger le second opérateur d'O'Neil; `L∞` seule ne fixe pas
  le mode constant.
- Artefact : `ONEIL-TRANSFER-1`, fractions exactes, marge minimale huit,
  aucun flottant, statut `COMPUTATION_ONLY`.

## 2026-08-14 — Énergie tronquée, support et amortissement

- Objet : solution classique pré-singulière de NS incompressible 3D non
  forcé sur `R³`; vorticité scalaire `omega=|curl u|` et niveau fixe.
- Entrée : `M=sup_t||omega||_(L^(3/2,infinity))` et
  `||alpha||_(L^(3/2,infinity)(A_lambda))<=A/log(lambda/Lambda_*)`, avec
  toutes les constantes et le domaine temporel uniformes.
- Absorption : le seuil est au moins
  `Lambda_*exp(2C_H A S_L²/nu)`; il n'est pas absolu.
- Coercivité : `X_lambda>=lambda E_lambda/(S_6²M)`. Une tente radiale donne
  `X/E=10R^-2` et confirme l'optimalité de la puissance `lambda/M`.
- ODE : coefficient `nu lambda/(2S_6²M)`; le terme initial disparaît seulement
  si `lambda>=||omega(t_0)||_infinity`.
- Sortie : `U_(2lambda)<=C lambda^-3/2 log(lambda/Lambda_*)^-3/2`, sans
  itération De Giorgi et sans perte d'échelle.
- Contre-profil : `|x|^-2 1_(|x|<1)` est faible-`L^(3/2)` mais tous ses
  tronqués ont énergie infinie; une variante tangentielle est divergence-free.
  La régularité classique, non la norme faible seule, lance le calcul.
- Défaut amont : `R=2^-8`, `j=5` donne
  `phi(2^jR)/phi(R)=8/3`, réfutant le facteur deux de (20)–(21). Le facteur
  trois répare localement l'ordre, pas le commutateur complet.
- Artefact : `DEGIORGI-UNIFORMITY-AUDIT-1`, douze contrôles exacts, aucun
  flottant, empreinte
  `cbdca92eec11a287c31bb67d48dfeda339768863b2ccfa58b6cd8f66e3682721`.

## 2026-08-14 — Commutateur localisé et dérive des moyennes

- Objet : estimation statique du stretching d'une solution classique de NS
  incompressible 3D non forcé sur `R³`; aucune simulation PDE.
- Entrées : `M=sup_t||omega||_(L^(3/2,infinity))`, semi-norme directionnelle
  `B_xi/[1+log(R_*/r)]`, `|xi|<=1` et raccord Calderón–Zygmund.
- Champ proche : l'extension de Jones doit contrôler une semi-norme modulo
  constantes; CRW atteint faible-`L^(3/2)` par interpolation, non par
  réflexivité.
- Queue : `I1` et la partie intermédiaire portent `R^-2` ponctuellement et
  récupèrent `R²` par restriction. La queue au-delà de `sqrt(RR_*)` vaut
  `O(MR/R_*)`.
- Multi-échelle : la dérive non pondérée des moyennes est au moins
  `floor(T/2)+1` fois `phi(R)` et peut donc être macroscopique. Le facteur de
  noyau `4^-k` est le gain structurel exact;
  `sum_(k>=1)(k+1)4^-k=7/9`.
- Défauts : la constante deux au dernier anneau, la formule `min` exacte de la
  réarrangée et la réflexivité du Lorentz faible sont réfutées. Facteur trois,
  réarrangée `1/(a³+s/|B_1|)` et interpolation réelle réparent la chaîne.
- Échelle : `M` et la norme de sortie sont critiques; `R/R_*` et le logarithme
  sont invariants. Aucune puissance d'échelle n'est perdue.
- Perte restante : rien ne produit la prémisse globale `bmo_phi` depuis
  l'énergie ou les données Clay; l'extension depuis un cœur actif et les zéros
  de vorticité restent ouvertes.
- Artefact : `COMMUTATOR-UNIFORMITY-AUDIT-1`, huit contrôles exacts, zéro
  échec, empreinte
  `387898492a0dc370d6ca50aadbc18e7e524ebdc0d7326fe2347952cbce57ebbf`.

## 2026-08-14 — Synchronisation logarithmique de l'endgame

- Objet : solution classique maximale de NS incompressible 3D non forcé sur
  `R³`, viscosité `nu>0`; aucun calcul de solution.
- Entrée : queue uniforme
  `|{|u|>a}|<=C_mu/[a³log³(e+a/U_*)]` au-dessus d'un seuil fixe.
- Temps : remplacer le temps « maximal » par
  `tau_t=nu/[c_1(M)U(t)²]` et séparer prolongement direct / temps intérieur.
- Rayons : le volume donne le rayon témoin
  `r_s=C_4/[U(s)log(e+theta U(s)/U_*)]`; l'analyticité donne le sous-rayon
  `rho_s=nu/[c_AU(s)]`.
- Seuil : `r_s<=rho_s` dès que le logarithme dépasse `c_A C_4/nu`. Le seuil
  est fini mais exponentiel en `C_mu^(1/3)/nu`.
- Harmonicité : `M=(2-h*)/[2(1-h*)]` et
  `theta=(1-h*)/(2-h*)` donnent deux résidus nuls; la branche cœur sature la
  constante un.
- Pertes localisées : temps maximal non intérieur, seuil de niveau non
  uniforme, rayon arbitrairement plus petit, changement de logarithme sans
  facteur et `M` analytique désynchronisé.
- Échelle : `U,U_*` portent `+1`, temps `-2`, rayons `-1`, volume `-3`; le
  rapport logarithmique et `C_mu^(1/3)/nu` sont invariants.
- Perte restante : la queue uniforme n'est pas produite pour toute solution
  Clay; la prémisse globale `bmo_phi` sur la direction reste à raccorder aux
  zéros et aux configurations multi-cœurs.
- Artefact : `ENDGAME-SYNCHRONIZATION-AUDIT-1`, onze contrôles exacts, zéro
  échec, empreinte
  `41b27f8649977c8a2d564c80418678017eb5d409956c8f3c5e3eb9016f916a3b`.

## 2026-08-14 — Axe mobile et coût de variation logarithmique

- Objet : profil spatial de vorticité
  `W=r^-2 Omega(log(R_*/r),theta)` dans `R³` ponctué; porte cinématique
  `div W=0`, aucune évolution NS.
- Entrées : `Phi=|Omega|<=M`, masse critique de bloc
  `integral <Phi^(3/2)> ds>=kappa`, axe absolument continu `e(s)` et erreur
  `D=integral<Phi|xi-e|>ds`.
- Identité : le moment `J=<[e dot theta]Omega_r>` a un terme de recharge
  borné par `(M/2)|e'|`; sa plage totale est `M`.
- Budget : sur `N` blocs de longueur `L`,

  ```text
  N*2kappa²/(3M²L)<=M+(M/2)Var(e)+D.
  ```

- Gain/perte : toutes les quantités sont invariantes d'échelle. Sous
  `D=o(NL)`, la variation doit avoir une densité au moins
  `4kappa²/(3M³L²)`. L'énergie physique ne produit ni la borne de tranche, ni
  la masse de bloc.
- Test BMO : une rotation uniforme de vitesse `alpha` a une oscillation
  centrée au moins `alpha²/[2(9+alpha²)]`; une phase
  `beta log(1+s)` a une oscillation centrée au plus `beta/[3(1+s)]` mais une
  variation seulement logarithmique.
- Attaques : grande variation sans déplacement macroscopique, axe non unique,
  boules décentrées, intermittence de `Phi`, blocs lacunaires et absence de
  pression ou de résidu d'évolution.
- Artefact : `WANDERING-AXIS-1`, 44 contrôles rationnels exacts, zéro échec,
  empreinte
  `23802f4b094aaccd020ab6d5d0ae9b136cc8cf70738b069c712fa6cddc432ba4`.
- Pivot : l'axe unique lent est fermé sous les hypothèses suivies;
  `GAP-MULTICORE-ANGULAR-CASCADE` devient actif.

## 2026-08-14 — Extraction BMO de l'axe actif et intermittence non bornée

- Objet : même profil spatial `W=r^-2 Omega(s,theta)`; aucune simulation ni
  solution d'évolution.
- Entrées : `Phi<=M`, masse `integral_block<Phi^(3/2)>ds>=kappa`, même
  extension `|zeta|<=1` à toutes les échelles et oscillation centrée
  `epsilon_k<=B/(1+S_k)`.
- Fraction active : `a_k>=a_*=3q³kappa/M^(3/2)`; la constante de baignoire
  plus fine vaut `[exp(3Lalpha)-1]/[exp(3L)-1]`,
  `alpha=kappa/[LM^(3/2)]`.
- Axe : `|m_k|>=1-epsilon_k/a_*` et
  `average_B|zeta-e_k|<=(1+1/a_*)epsilon_k`.
- Multi-échelle : volumes imbriqués, interpolation géodésique et conversion
  boule–coquille donnent `Var(e)+D=O(log N)`, contredisant la dépense linéaire
  du budget mobile.
- Correction de veille : si `zeta` est globalement unitaire, l'identité
  quadratique `average|zeta-m|²=1-|m|²` normalise déjà les moyennes. Le passage
  de la direction sur `{omega!=0}` à un tel prolongement reste une hypothèse
  non intrinsèque et non fournie par les théorèmes d'extension BMO inspectés.
- Contre-profil : fraction `n^-3`, amplitude `n²`, masse critique fixe et
  oscillation binaire `2n^-3(1-n^-3)->0`. Il réfute toute suppression de
  `Phi<=M` fondée sur la masse seule.
- Artefact : `BMO-ACTIVE-AXIS-EXTRACTION-1`, 66 contrôles rationnels exacts,
  zéro échec, première contradiction certifiée à 1023 blocs, empreinte
  `e2603081b46d4aab9599e9681eaf50cbc460df46e3b6d1c3d2383b0a71005e0e`.
- Pivot : `GAP-MULTICORE-ANGULAR-CASCADE` est fermé sous amplitude bornée;
  `GAP-UNBOUNDED-ANGULAR-INTERMITTENCY` devient actif.

## 2026-08-14 — Train de blobs et défaut BMO décentré

- Objet : champ statique sur `R³`, somme de copies critiques compactes aux
  rayons `r_n=2^-n` et largeurs `ell_n=r_n/(8n)`.
- Identités : `div u=0`, `curl u=W`, `div W=0`; les supports sont disjoints et
  Biot–Savart reconstruit l'unique vitesse `L²`.
- Énergie : `||U_n||²_2=ell_n||U_0||²_2`, donc la somme est finie.
- Criticité : chaque blob garde la même masse `L^(3/2)`; la somme est dans
  `L¹ intersection L^(3/2,infinity)` mais pas dans `L^(3/2)` fort.
- Intermittence : occupation centrée `O(n^-3)`, amplitude angulaire exacte
  `1024n²` et produit critique invariant.
- Séparation des tests : l'extension par zéro a `MO_centree<O(n^-3)`, tandis
  que toute extension garde `MO>=c_dir>0` sur des boules internes de rayon
  `ell_n/2`. Une forme directionnelle fixe est incompatible avec tout poids
  BMO qui tend vers zéro.
- Résidu : `curl[-Delta U_0+(U_0 dot nabla)U_0]` a 1804 monômes non nuls;
  aucune pression stationnaire ne ferme le profil et le coût `L¹` est critique.
- Artefact : `CRITICAL-SOLENOIDAL-BLOB-TRAIN-1`, 104 contrôles exacts, zéro
  échec, empreinte
  `129921806266636a46a5202bd0f2912491aaf557a02cda229c17ef80a529cb15`.
- Pivot : le blob de forme fixe est fermé;
  `GAP-DIRECTIONALLY-FLAT-INTERMITTENCY` devient actif.

## 2026-08-14 — Compensation conique critique et exposant cubique

- Objet : champ mesurable `W` sur un domaine fini, moyenne vectorielle nulle;
  porte statique de tout curl compact, aucune évolution.
- Quasi-norme : `K=sup lambda |{|W|>lambda}|^(2/3)` et
  `integral_E|W|<=3K|E|^(1/3)`.
- Cône : si `m=integral_{xi·e>=alpha}|W|`, l'annulation force une masse au
  moins `alpha m` dans l'hémisphère opposé.
- Coercivité : toute extension `L¹` de la direction satisfait
  `MO_D>=2alpha³m³/(27K³|D|)` sous moyenne nulle; sans elle, le minimum
  canonique fait intervenir `nu_e=integral(-W·e)_+`. Le quotient est invariant
  d'échelle.
- Sharpness : fractions `1-n^-3,n^-3`, amplitudes `n²/(n³-1),-n²`, donnent
  `K=1`, `m=1/n`, masse forte critique entre un et deux, et
  `MO=4n^-3(1-n^-3)`.
- Perte exacte : la masse `L^(3/2)` ne minore pas la masse conique `L¹`; le
  compensateur rare peut porter toute la criticité.
- Test spatial : une interface régulière `+e/-e` a une oscillation locale un;
  la petite moyenne parentale n'est pas un BMO global.
- Test annulaire : une zone de zéros permet une extension unitaire de coût
  `Theta(1/log(R/h))`; au placement `ell_n~2^-n/n`, le poids log-BMO croît
  néanmoins comme `n/log n` pour une phase de rayon relatif `1/n`.
- Porte div–curl : `W=f e` compact et divergence-free implique `W=0`; le lift
  spatial doit introduire des composantes transverses ou fermer les tubes.
- Artefact : `LORENTZ-CONE-COMPENSATION-1`, 670 contrôles rationnels exacts,
  zéro échec, empreinte
  `12eadf58f6bf5fdec9855527f58d9a7e6ba98650c3fd8fca78adbbbcfc1e1727`.
- Pivot : la masse conique uniforme est fermée;
  `GAP-NESTED-RETURN-FLOW-CASCADE` devient actif.

## 2026-08-14 — Retour axisymétrique compact à aspect fixé

- Objet : `U_n=chi(z)A_n(r)e_theta`, champ statique compact; aucune évolution.
- Flux : phase `n^-1` sur `1<r<2`, retour de largeur `n^-3` et amplitude
  `3n^5/(8n^3+1)`; `integral r f_n dr=0` exactement.
- Criticité : faible-`L^(3/2)` uniformément encadré, masse forte critique
  négative non dégénérée, énergie normalisée `<=1/(3528n²)`.
- Perte directionnelle : dans le corridor de calotte, `W/|W|=e_r` malgré
  `|W_r|=O(1/n)`; normaliser détruit toute petitesse d'amplitude.
- Porte BMO : `MO_B>=3w/[2048(R+w)]`, soit `3/26624` pour le certificat. À
  aspect fixé, le poids logarithmique diverge sous concentration.
- Sharpness div–curl : une calotte `n^-3` donne
  `4n^-3/27<=MO_D<=n^-3` sur le parent et une variante `C_c^infinity` réalise
  `K~1`, `m~epsilon^(1/3)`, `MO_D~epsilon`; ceci ne borne pas le BMO all-ball.
- Porte dynamique : `||U_epsilon||_3->0`; la famille lisse est dans le régime
  de petites données et n'est pas une singularité candidate.
- Résidu : cinq coefficients non nuls dans `chi''`; la composante azimutale
  de `-Delta U` ne peut être un gradient. `||R_s||_1` est invariant d'échelle.
- Artefact : `AXISYMMETRIC-RETURN-FLOW-BMO-GATE-1`, 1251 contrôles rationnels
  exacts, zéro échec, empreinte
  `cec8bd74aa0b5b1b9943fbd149fe06c4ca5b045b9a337bdfef2821a18c5d29a9`.
- Pivot : produit séparable abandonné pour le BMO all-ball;
  `GAP-NONSEPARABLE-RETURN-FLOW-MASKING` actif.

## 2026-08-14 — Fermeture toroïdale logarithmique

- Objet : sur `T^3`, tore de rayon majeur `R_n=2^-n`, cœur
  `h_n=2^-n^2`, corridor `q_n=2^-2n`, vorticité azimutale lisse.
- Criticité : `A_n=(R_n h_n^2)^(-2/3)` conserve les normes forte et faible
  `L^(3/2)` à constantes de profil.
- Échappement : la rotation logarithmique `e_theta -> e_z` donne une enveloppe
  all-ball uniforme; le crochet adimensionné du certificat est `<4`.
- Porte Biot–Savart :
  `||u_n||_3^3<=C[h_n/R_n+(h_n/R_n)^2]`, donc la vitesse critique s'annule.
- Porte poloidale : l'excès radial `Delta_Omega` minore mesure et capacité,
  mais le rang d'une somme ne force pas sa positivité.
- Porte dynamique : le corridor statique disparaît pour un anneau unisigné
  sans swirl sur `R^3`; les boules axiales ont alors oscillation un.
- Artefact : 2207 contrôles rationnels exacts, zéro échec, empreinte
  `0e1ea53d24e3c241c67e24a35bedbd81a16043cea580581ddc6c4f1f5729d274`.
- Pivot : `GAP-MOMENT-CORRECTED-TOROIDAL-CASCADE` actif; annulation de
  l'impulsion, non-dégénérescence de `L^3` et sortie de la classe sans swirl.

## 2026-08-14 — Paire à impulsion corrigée

- Géométrie : deux tores signés congruents, axes parallèles déplacés de
  `+/-3R e_1`; les corridors tournent séparément vers le même fond `e_z`.
- Moment : moyenne vectorielle nulle pour chaque composante et impulsion totale
  exactement nulle; le second moment traduit `Q_(11,2)=4aI_ring` survit.
- Criticité : les normes forte et faible `L^(3/2)` restent d'ordre un.
- Équivalent de vitesse : Stokes et Biot–Savart donnent
  `cK^3h/R<=||u||_3^3<=CK^3(h/R+(h/R)^2)`.
- Cardinal fixé : toute somme disjointe avec `max h_j/R_j->0` garde
  `||u||_3->0`, même après correction d'un nombre fini de moments.
- Artefact : 1842 contrôles rationnels exacts, zéro échec, empreinte
  `527be8971f4bc5e2d7f22a3fb18a3d626b12cecc7f5dc71e39d40488b4a4a70c`.
- Pivot : `GAP-MANY-TORUS-CRITICAL-ACCUMULATION`; auditer d'abord le budget
  combiné faible-Lorentz, packing, cohérence de vitesse et moments.

## 2026-08-14 — Porosité tubulaire et endpoints compacts

- Objet : vorticités lisses statiques sur `R^3` ou `T^3`; aucune évolution.
- Packing : `length(Gamma intersection B_r)<=C r^3/q^2` pour tout `r>=q`.
- Partie proche : `||u_loc||_3^3<=CK^3h/mathcal L`.
- Partie lointaine : `D=A(h/q)^2`, puis Hedberg, HLS et interpolation donnent
  `||u_far||_3^3<=CK^3(h/q)^(4/3)`.
- Reste périodique : `CK^3S`; la conclusion exige `S->0` en plus des deux
  rapports de forme.
- Test exact : `N_n=2^(12n-12)`, somme triangulaire `2^(3n-12)->infinity`,
  mais termes cubes `2^(-21n+12)`, `2^(-4n)` et `2^(-15n-12)`.
- Contre-profil compact : les supports de vitesse disjoints séparent norme
  forte et quasi-normes faibles; la compacité ne force aucun collapse fort.
- Perte restante : la remise à l'échelle reproduit toute oscillation interne
  de direction et la pondère par `|log r_j|`; la diffusion agit au temps
  `r_j^2/nu`.
- Artefact : `MANY-TORUS-POROSITY-GATE-1`, 776 contrôles rationnels exacts,
  zéro échec, empreinte
  `821c0e7e442698397c5d426fefca42ca12e5949f904e3ce243d3277377ecbbae`.
- Pivot : branche tubulaire homogène abandonnée;
  `GAP-COMPACT-VELOCITY-WEAK-CRITICAL-DIRECTION` devient actif.

## 2026-08-14 — Budget d'aspect du swirl compact

- Objet : `U=V(R/r)eta((r-R)/a)chi(z/b)e_theta`, donnée compacte
  divergence-free; `W=curl U`, aucune évolution.
- Annulation exacte : le facteur `R/r` supprime le terme cylindrique de
  courbure et sépare `W_z~V/a` de `W_r~V/b`.
- Gates critiques : `K_U^3~V^3Rab`, tandis que
  `K_W^3>=cV^3 max(R^2b^2/a,R^2a^2/b)`.
- Perte irréductible : `K_U>=kappa` et `K_W<=K` imposent
  `a/R,b/R>=c(kappa/K)^3`; le profil ne peut devenir mince dans aucune des
  deux directions.
- Direction : une boule de rayon `c min(a,b)` porte exactement `+/-e_r` et
  conserve donc une oscillation d'ordre un sous les gates.
- Test adverse : aspect `2^n`; le proxy BMO pondéré `2n/2^n` s'annule, mais le
  cube vorticité croît comme `2^n`, ou le cube vitesse tombe comme `2^-n`.
- Artefact : `COMPACT-SWIRL-ASPECT-GATE-1`, 37 214 contrôles exacts, zéro
  échec, empreinte
  `e392e3570e4de6f85bcb5f91a7eef6b36a1ed22c55bf8c483a918319b9a848e4`.
- Pivot : le produit séparable est fermé à tout rapport d'aspect;
  `GAP-NONSEPARABLE-COMPACT-CURL-FLATNESS` devient actif.

## 2026-08-14 — Collapse Lorentz de support pour tout swirl pur mince

- Objet : `U=(R/r)F(r,z)e_theta`, `F` lisse compacte, support dans
  `R/2<r<3R/2`; aucune évolution.
- Quantité géométrique critique : `sigma=S_2/R^2`, où `S_2` est l'aire
  méridienne du support réel de la somme `F`.
- Lemme :

  ```text
  ||U||_(L^(3,infinity))
   <=C sigma^(1/6)||curl U||_(L^(3/2,infinity)).
  ```

- Perte irréductible : les gates `K_U>=kappa`, `K_W<=K` forcent
  `sigma>=C^-6(kappa/K)^6`; aucune annulation interne ne change cette puissance.
- Test adverse : 384 masques P1 signés et décalés, quatre maillages rationnels,
  272 726 contrôles exacts, zéro échec; le pire quotient carré vaut
  `4212353969604/482173039025` et le facteur d'échelle est divisé par quatre à
  chaque pas dyadique.
- Empreinte :
  `597dc2e2828df34d836556c5419904d39e6ee240aa93b353a49683699ae40443`.
- Limite : `sigma~1`, composantes poloïdales, direction BMO, pression et temps
  restent non contrôlés.
- Pivot : branche mince non séparable abandonnée;
  `GAP-THICK-CROSS-SECTION-GRADIENT-DIRECTION` devient actif.

## 2026-08-14 — Coercivité directionnelle d'une tranche axiale bornée

- Objet : tout `U=(R/r)F e_theta` avec
  `supp F subset {R/2<r<3R/2, |z-z_0|<Lambda R}`.
- Troncature : un niveau presque optimal fournit
  `TV(G)>=cK_f^2/K_g`, sans hypothèse de profil, signe ou séparabilité.
- Compensation : le curl tronqué est de moyenne nulle et porte une masse
  conique `>=cR K_f^2/K_g`.
- Gate : toute extension de direction satisfait

  ```text
  MO_B>=c_Lambda(K_u/K_w)^6
  ```

  sur une boule de rayon `C_Lambda R`.
- Conséquence : sous `K_u>=kappa`, `K_w<=K` et `R->0`, le coût log-BMO diverge
  comme `(kappa/K)^6|log R|`.
- Test adverse exact : coques de plateau, retours antipodaux rares et jusqu'à
  256 cellules séparées; 2 884 contrôles, zéro échec.
- Empreinte :
  `4759238f59a46f64f0a547881f8aeb86ca6755ceea06c4a1728648db57847f8f`.
- Limite : diamètre axial non borné, cellules hétérogènes, composantes
  poloïdales et dynamique non couverts.
- Pivot : `GAP-AXIALLY-DISPERSED-PURE-SWIRL-SELECTION`.

## 2026-08-14 — Registre BV de cellules hétérogènes

- Contre-profil normique : `K_u=1`, `K_w<=1.338`, mais tout rapport local
  vaut `N^-1/3`; les niveaux de curl sont géométriquement échelonnés.
- Défaut du contre-profil : il ne transporte pas la variation totale requise
  pour fermer chaque plateau, donc ne satisfait pas `W=curl U`.
- Registre positif :

  ```text
  integral_(Q_j)|W_j|>=cA_jv_j^(2/3),
  |Q_j|<=Cv_j.
  ```

- Sélection critique :

  ```text
  K_(u,j)>=cK_u^2/K_w,
  K_(u,j)/K_(w,j)>=c(K_u/K_w)^2.
  ```

- Gate directionnel composé :

  ```text
  MO_(B_j)>=c(K_u/K_w)^12.
  ```

- Échelle : toutes les normes et rapports sont invariants sous le scaling
  Clay; le volume `v_j` se transforme comme une longueur au cube et le registre
  BV comme la norme critique correspondante.
- Certificat : 31 746 assertions rationnelles exactes, zéro échec; empreinte
  `d918ff7ec5e200d388cde1d3ed5230ebdd4535bc65fc3b94a2c7ac21c0962763`.
- Limites : boîtes non comparables, chevauchements, projection de Leray,
  pression, diffusion et sélection de `R_j->0` non contrôlés.
- Pivot : `GAP-DEGENERATE-CELL-REGISTER-OR-OVERLAP`.

## 2026-08-14 — Bande commune et support dégénéré

- Contre-profil de halo fixe : sous dilatation critique, endpoints constants,
  `||W_L||_infinity~L^-2` et registre total `~L`; un témoin `v_L=1` ne
  localise aucune masse de curl `~A_Lv_L^(2/3)` dans volume borné.
- Premier quantificateur faux : un minorant de plateau n'est pas un calibrage
  bilatéral du superniveau.
- Réparation pure-swirl : au niveau global `lambda`, les bandes
  `lambda/4<+/-F_j<lambda/2` ont leur volume contrôlé par
  `{|U|>lambda/6}` et leur variation contrôlée par isopérimétrie R3.
- Sélection critique :

  ```text
  K_(u,j)>=(C_I/324)K_u^2/K_w,
  K_(u,j)/K_(w,j)>=(C_I/324)(K_u/K_w)^2.
  ```

- Échelle : toutes les quasi-normes et la constante sont critiques; aucune
  longueur axiale ni volume support n'entre.
- Certificat : 10 837 assertions rationnelles, zéro échec, résidu nul;
  empreinte
  `b197d3b45af0f034c09c91d4b7bb6d3be55293ab1f458ec769c250c8998490f8`.
- Limite : un contrôle de volume ne donne ni diamètre, ni boule, ni
  composition automatique avec le gate directionnel du cycle 0033.
- Pivot : `GAP-ACTIVE-HALO-DIAMETER-OR-OVERLAP`.

## 2026-08-14 — Troncature composante et pont au-dessus du seuil

- Objet : composantes connexes actives d'un swirl pur statique, aucune
  évolution Navier–Stokes.
- Troncature : `G_alpha=(sigma F-lambda/4)_+1_(C_alpha)` est lipschitzienne et
  n'ajoute aucune mesure de curl au bord.
- Sélection critique :

  ```text
  K_(u,alpha)>=(C_I/648)K_u^2/K_w,
  K_(u,alpha)/K_(w,alpha)>=(C_I/648)(K_u/K_w)^2.
  ```

- Composition conditionnelle : si `diam C_alpha=O(R_j)`, le gate
  lipschitzien donne `MO_B>=c(K_u/K_w)^12`.
- Contre-profils éliminés : un filament sous le cutoff est supprimé; `m`
  copies identiques font décroître le rapport global comme `m^-1/3`.
- Frontière géométrique sourcée : une boule Frank–Lieb à rayon `V/P` ne capte
  que la fraction `cV^2/P^3`; volume+périmètre ne bornent pas le diamètre.
- Certificat : 5 773 assertions rationnelles exactes, zéro échec, empreinte
  `f0550313e21e05a7cda46fd8d1264b982d3ab3b809b5c5b05ec1f77c5c56892a`.
- Limite : un pont d'amplitude au-dessus de `lambda/4` peut garder une
  composante de diamètre arbitraire; chevauchements, pression et temps restent
  ouverts.
- Pivot : `GAP-ABOVE-THRESHOLD-THIN-BRIDGE`.

## 2026-08-15 — Diamètre d'une branche persistante

- Objet : swirl pur statique
  `U=(R/r)F e_theta`, `W=curl U`, support méridien dans
  `R/2<r<3R/2`; aucune évolution.
- Brique planaire : toute composante M-indécomposable vérifie
  `P_2(E)>=2 diam(E^1)` (`NS-SRC-0163`).
- Coaire pondérée exacte : si un diamètre axial `D` persiste presque partout
  sur `(a,b)`, alors

  ```text
  integral_(a<sigma F<b)|W| >= 4 pi R D (b-a),
  a(b-a) R D <= 9 K_u K_w/(8 pi).
  ```

- Corollaire cutoff : un pont restant au-dessus de `A` vérifie
  `A^2RD<=9K_uK_w/(2pi)<=(3/2)K_uK_w`, indépendamment de son faible excès
  au-dessus de `A`.
- Scaling : `A^2RD`, `K_uK_w`, `AR/K_u`, `D/R` et `K_u/K_w` sont critiques.
- Test adverse : pour `delta=L^-1`, le curl tronqué reste borné seulement si
  `eta<~L^-3/2`; le cube du curl original croît comme `L^3`.
- Certificat : 1 035 familles, 5 197 assertions rationnelles exactes, zéro
  échec; empreinte
  `d4be10a24de48f196a64515b1f1fc9916c51b51332244f50e443cefc326be946`.
- Pertes restantes : `AR>=kappa K_u` n'est pas automatique pour chaque
  goutte; un grand diamètre au niveau bas peut résulter d'une fusion sur une
  fenêtre d'amplitude évanescente; pression, temps et Type II absents.
- Pivot : `GAP-BRIDGE-SCALE-CALIBRATION-OR-MERGE-TREE`.

## 2026-08-15 — Niveau adaptatif et fermeture du diamètre statique disjoint

- Objet : cellule pure-swirl annulaire statique, puis famille de cellules à
  supports complets disjoints; aucune évolution.
- Calibration obtenue sans hypothèse locale :

  ```text
  lambda R >= K^2/(432H).
  ```

- La moyenne de coaire sur `(lambda/4,3lambda/8)` sélectionne au même niveau
  une composante vérifiant

  ```text
  diam_z/R <= 2 239 488 (H/K)^3,
  K_beta >= (C_I/20 736)K^2/H,
  q_beta >= (C_I/20 736)q^2.
  ```

- Composition familiale : `K_beta/K_global>=c q_global^3`,
  `q_beta>=c q_global^4`, `diam/R_j<=C q_global^-6`.
- Scaling : `lambda R`, `K^2/H`, `diam/R` et tous les rapports endpoint sont
  critiques.
- Test : 12 243 assertions rationnelles principales et 9 513 indépendantes,
  résidus exacts nuls. Le contre-arbre abstrait réfute le bookkeeping
  topologique seul, mais échoue au registre coaire de fermeture compacte.
- Perte restante : la monotonie locale `H_beta<=H_j` n'est plus disponible
  après annulation entre curls superposés; pression, temps et sélection
  `R_j(t)->0` restent absents.
- Pivot : `GAP-OVERLAPPING-CURL-CANCELLATION`.

## 2026-08-15 — Annulation de curl à multiplicité deux

- Objet : deux champs pure-swirl lisses compacts statiques de même axe et
  même anneau; aucune évolution Navier–Stokes.
- Famille : `U_(1,n)=B+Z_n`, `U_(2,n)=-Z_n`, avec oscillation axiale de
  fréquence `n`; total exactement fixe `B`.
- Témoin : volume `4pi^2/3`, curl individuel `>=2n/5`, vitesse et support
  uniformément bornés.
- Échec critique : les deux rapports locaux tendent vers zéro comme `n^-1`,
  alors que le rapport global reste `q(B)>0`. Scaling Clay, multiplicité et
  divergence nulle sont conservés.
- Certificat : 20 445 modèles, 344 121 assertions rationnelles principales et
  1 216 indépendantes, résidus exacts nuls.
- Résultat négatif : multiplicité, support et compatibilité curl ne contrôlent
  pas l'anti-alignement. Une base dénombrable norm-convergente du plein
  faible-Lorentz est en outre exclue par non-séparabilité.
- Réparation : agréger le potentiel total avant sélection lorsque axe, rayon
  et anneau sont communs.
- Perte restante : aucune représentation scalaire unique pour plusieurs axes;
  cutoff de Leray, pression, temps et `R(t)->0` restent ouverts.
- Pivot : `GAP-MULTIAXIS-TOTAL-FIELD-LOCALIZATION`.

## 2026-08-15 — Cutoff solénoïdal du champ total

- Objet : champ statique `U in C_c^infinity(R3)`, divergence-free; aucune
  évolution Navier–Stokes.
- Quantités critiques : `K_core`, `G_col` en faible-`L3` et `H_out` en
  faible-`L^(3/2)` sont invariantes sous l'échelle Clay.
- Fermeture cinématique : `V=chi_RU-B_R(grad chi_R dot U)` est compact,
  divergence-free et égal à `U` dans le core, avec coût de curl critique à
  constante uniforme sur une couronne de rapport fixé.
- Absorption globale : faible HLS donne
  `q(V)>=C_loc^-1(K_core/K_global)q(U)`.
- Saturation : un plateau lisse divergence-free montre que le coût du col
  n'est jamais `o_R(1)`; 9 167 assertions rationnelles exactes, résidu nul.
- Dégénérescence : pour `A_(R,h)`, tout inverse droit fort `L^p->W_0^(1,p)`
  coûte au moins `c_pR/h`; l'épaisseur petite aggrave la constante.
- Perte restante : le quotient `K_core/K_global` n'est contrôlé à aucune
  échelle de concentration; une grande boule serait une capture triviale.
  Pression, temps, commutateurs et Type II sont absents.
- Pivot : `GAP-WEAK-L3-CORE-CAPTURE-AT-PRESINGULAR-SCALE`.

## 2026-08-15 — Capture Type I faible-`L3`

- Objet : solution de Leray–Hopf non forcée sur `R3`, lisse avant un premier
  temps singulier `T_*`, sous borne pointwise
  `sup_t||u(t)||_(3,infinity)<=M`.
- Inclusion critique exacte :
  `||u||_(L2(B_r))^2<=3(4pi/3)^(1/3)M^2r`; aucune puissance d'échelle perdue.
- Source : Barker–Prange 2020, théorème 2 plus appendice B. Le rayon est
  `R_M(t)=2sqrt((T_*-t)/S_w^*(C_MM))`; `S_w^*` dépend de `M`.
- Capture : `K_core>gamma_w` et `K_core/K_global>gamma_w/M` pour tout
  `0<t<T_*` sous la convention temporelle pointwise.
- Test : 1 346 assertions rationnelles; constante trois approchée par défaut
  exact `0.023195958142` au cas `m=128,N=2048`; paquets disjoints exacts
  forcent la fraction vers zéro en l'absence de borne globale.
- Perte restante : le cutoff mobile ne satisfait pas l'équation non forcée;
  sa dérivée temporelle, la pression et les commutateurs sont non calculés.
  En Type II, la disparition de `M` détruit la fraction uniforme.
- Pivot : `GAP-TYPE-I-LOCALIZED-EVOLUTION`, avec
  `GAP-TYPE-II-RELATIVE-CORE-CAPTURE` conservé séparément.

## 2026-08-15 — Force du cutoff mobile Type I

- Objet : même branche Type I que le cycle 0041, centre singulier fixe et
  rayon `R=2sqrt((T_*-t)/S_w^*(C_MM))`.
- Horloge : `R'/R=-1/[2(T_*-t)]` et
  `kappa=-RR'=2/S_w^*(C_MM)`.
- Identité : le cutoff solénoïdal satisfait une équation forcée locale; la
  dérivée de `B_R` contient le commutateur avec le générateur de dilatation.
- Scaling : force `R^-3`, norme `L1` invariante, norme
  faible-`L^(3/2)` d'une force brute comme `R^-1`, norme `Hdot^-1` comme
  `R^-1/2`; un stress `R^-2` est critique en faible-`L^(3/2)`.
- Témoin : swirl radial compact avec défaut de divergence nul, mais
  `R^3(partial_tchi_R)u_R=(0,-9c^2/4,0)` au point normalisé choisi.
- Certificat : 499 assertions rationnelles exactes; 48 horloges, 36 jets
  remis à l'échelle et 64 coquilles critiques, zéro échec.
- Résultat négatif : le rétrécissement du support ne produit aucune petitesse
  et les normes espace-temps critiques finies accumulent logarithmiquement si
  le profil persiste.
- Perte restante : cancellation éventuelle de la force complète, pression
  projetée et commutateurs de Bogovskii dans les espaces négatifs.
- Pivot : `GAP-TYPE-I-MOVING-COMMUTATOR-BOUND`, puis
  `GAP-TYPE-I-FORCED-RIGIDITY`.

## 2026-08-15 — Commutateur mobile dans l'espace négatif critique

- Objet : même branche Type I, mais avec une réalisation exacte et
  pseudodifférentielle d'ordre `-1` de Bogovskii sur la couronne unité.
- Espace invariant : `X=L1+div L^(3/2,infinity)`; les deux coefficients se
  remettent à l'échelle comme `R^-3f` et `R^-2G`.
- Identité : `-[Delta,Q]+kappa[D,Q]` est la somme d'un terme `L1` et de la
  divergence de `-2U tensor nabla chi`; les commutateurs restants sont
  d'ordre zéro ou inférieur.
- Force complète : pression de Riesz et non-linéarité coûtent `O(M²)`;
  mobilité et commutateurs coûtent `O((1+|kappa|)M)`.
- Test : la norme positive du mode pure-swirl croît au moins comme
  `epsilon(5N/32-8/15)`, mais les budgets négatifs restent bornés par
  `99epsilon/140` et `8epsilon/5`.
- Certificat : 222 assertions rationnelles exactes, zéro échec; aucune
  discrétisation et aucune intégration Navier–Stokes.
- Résultat : `GAP-TYPE-I-MOVING-COMMUTATOR-BOUND` est fermé pour l'opérateur
  fixé. La force est critique et grande, pas petite.
- Perte restante : `X` est non réflexif, la projection est non locale et
  aucune convergence forte des produits n'est acquise.
- Pivot : `GAP-TYPE-I-FORCE-COMPACTNESS`, puis
  `GAP-TYPE-I-FORCED-RIGIDITY`.

## 2026-08-15 — Cutoff externe : gain local, perte globale

- Objet : transition homothétique sur `A_L={L<|y|<2L}`, avec core Type I
  inchangé dans `B_1` et même inverse de divergence conjugué.
- Gain local : le stress extérieur est faible-`L^(3/2)` et le noyau de
  `P_L div` a le degré `-4`; la force décroît comme `L^-3` sur les compacts,
  et sa dérivée spatiale d'ordre `m` comme `L^(-3-m)`.
- Constantes certifiées : `11904/35` pour `m=0` et `134912/25` pour `m=1`
  dans la convention tensorielle du ledger; 253 assertions rationnelles.
- Perte globale : sur `U_L=L^-1U_*(dot/L)`, le terme de drift vaut
  `kappa L^-1[D,Q]U_*(dot/L)`, deux puissances au-dessus du scaling d'une
  force. La dualité de `X` impose `||F_L||_X>=c|kappa|L²-C`.
- Faux raccourci éliminé : la somme des budgets par coquille peut croître
  logarithmiquement alors que la quasi-norme faible de leur union reste
  uniforme; seule la minoration duale donne un échec global robuste.
- Diagonale physique : exiger `L_j->infinity` et `L_jR_j->0`; le choix
  `L_j=R_j^-1` est rejeté.
- Résultat : fuite locale fermée, convergence globale réfutée.
- Perte restante : aucune compacité temporelle, convergence forte du produit,
  inégalité d'énergie limite, trace non nulle ou dérenormalisation ancienne.
- Pivot : `GAP-TYPE-I-LOCAL-COMPACTNESS-TRACE`, puis
  `GAP-TYPE-I-ANCIENT-WEAK-L3-RIGIDITY`.

## 2026-08-15 — Dérenormalisation exacte, dette globale inchangée

- Objet : inverse exact du drift Type I constant sur toute la diagonale
  ancienne, sans supposer une trace terminale non nulle.
- Scaling : `v=r^-1Z`, `q=r^-2Pi`, `d tau=r²ds`, `dx=r³dy`; `K_3` est
  exactement invariant, l'énergie locale normalisée aussi.
- Énergie locale : l'opérateur standard coûte `r^-4`; le jacobien donne au
  test renormalisé le poids positif `r`. Aucun coefficient de Grönwall ni
  constante de troncature n'intervient dans cette conjugaison.
- Pression : le contrôle global faible-`L^(3/2)` passe faible-étoile par les
  Riesz; la convergence forte locale identifie le produit, sans prétendre à
  une compacité forte globale.
- Gain : ancienne standard suitable locale, faible-`L3`, non nulle, pression
  de Riesz.
- Perte restante : faible-`L3` n'est pas à queue absolument continue et ne
  fournit ni énergie globale, ni trace forte, ni formule mild compatible.
- Certificat : 420 assertions rationnelles; zéro discrétisation, zéro erreur
  d'arrondi, résidus adverses explicites.
- Pivot : `GAP-TYPE-I-ANCIENT-WEAK-L3-RIGIDITY-OR-MILDNESS`.

## 2026-08-15 — Énergie locale récupérée, trace critique perdue

- Objet : suites classiques de l'équation renormalisée sur `R3`, sous borne
  `L-infinity_tL^(3,infinity)_x`, pression de Riesz et force localement
  évanescente.
- Gain PDE : la norme critique donne localement vitesse `L2` et pression
  `L^(4/3)`; le test d'énergie absorbe le cubique et le flux de pression puis
  le remplissage des trous fournit `L2_tH1_x` uniformément.
- Compacité : Simon donne forte `L2`; l'énergie parabolique donne une borne
  `L^(10/3)` et donc forte `L3`, suffisante pour le produit et l'énergie
  locale.
- Pression : la partie de Riesz proche converge fortement; la queue
  harmonique reste faible-étoile mais spatialement lisse. Aucune localisation
  abusive de l'opérateur non local n'est faite.
- Perte critique : `C_n=nV(n dot)` conserve `K_3`, tend vers zéro dans tous
  les espaces sous-critiques et contre chaque test fixe, tandis que son
  enstrophie diverge. Son résidu d'échelle `n^3` montre pourquoi la PDE est
  indispensable à l'énergie, sans réparer la trace.
- Couche terminale : une solution forcée périodique exacte a volume `L2`
  tendant vers zéro et trace constante; une force petite seulement dans
  `L1_tH^-1_x` est insuffisante.
- Résultat : compacité adaptée locale fermée, transmission automatique de la
  trace réfutée.
- Pivot : `GAP-TYPE-I-CRITICAL-TRACE-PERSISTENCE`, puis dérenormalisation et
  `GAP-TYPE-I-ANCIENT-WEAK-L3-RIGIDITY`.

## 2026-08-15 — Capture persistante, non-trivialité conservée

- Objet : même branche Type I, suite exacte des translations de la
  trajectoire renormalisée mobile et cutoffs externes constants par fenêtre.
- Quantificateur récupéré : Barker–Prange donne la capture au point fixe pour
  tout temps; elle n'est pas limitée à la tranche terminale.
- Horloge : `d(log R)/d sigma=-kappa`, donc le rapport de rayons sur une
  fenêtre fixe est `exp(-kappa s)` et la fenêtre ne se contracte pas.
- Scaling : `K_3(Ru(x_*+R dot);B_1)=K_3(u;B(x_*,R))`; `Q_L=I` dans `B_1`.
- Gain critique : `K_3³<=||.||_3³` par tranche, donc la capture persistante
  paie au moins `|J|gamma_w³` dans la forte `L3` espace–temps. Cette masse
  passe à la limite.
- Frontière optimale : sur un ensemble de temps `E_j`, le coût exact minimal
  est `|E_j|gamma_j³`; une tranche isolée ou une fenêtre contractante peut
  encore disparaître.
- Certificat : 417 assertions rationnelles exactes, aucune discrétisation ni
  simulation PDE.
- Résultat : limite ancienne renormalisée non triviale; moment signé à
  l'ancien endpoint non nécessaire à cette conclusion.
- Perte restante : dérenormalisation distributionnelle, classe globale de la
  solution standard, mildness et rigidité faible-`L3`.
- Pivot : `GAP-TYPE-I-DERENORMALIZATION-CLASS`, puis
  `GAP-TYPE-I-ANCIENT-WEAK-L3-RIGIDITY`.

## 2026-08-15 — Duhamel endpoint fermé, dissipation globale perdue

- Objet : ancienne distributionnelle standard sur `R3`, non forcée,
  viscosité un, pression de Riesz, uniformément
  `L-infinity_tL^(3,infinity)_x`.
- Scaling : `L^(3,infinity)` est critique; le stress est critique dans
  `L^(3/2,infinity)`. Le noyau `S(h)Pdiv` agit sous-critically avec le gain
  `h^((3-p)/(2p))`, `3/2<p<3`, mais sa norme endpoint ponctuelle vaut
  `h^-1`.
- Gain endpoint : Meyer--Yamazaki intègre le pairing après fixation du test
  `L^(3/2,1)`. Le terme quadratique existe dans `L^(3,infinity)` comme
  intégrale de Gelfand avec borne `CM²`, sans intégrale de Bochner.
- Gain énergétique instantané : à `p=2`, le correcteur canonique est dans
  `C_tL2_x` et vaut `O(h^(1/4))` au redémarrage.
- Perte d'une dérivée : `nabla S(h)Pdiv` coûte `h^-5/4` dans le mapping
  choisi. La borne critique seule ne fournit pas `L2_tHdot1_x`.
- Contre-profil : `U=(-x_2,x_1,0)/|x|²` a
  `K_3(U)^3=pi²/4`, énergie tronquée `(8pi/3)R` et queue critique de taille
  constante. Aucun split radial coeur énergétique/queue petite n'est
  disponible uniformément.
- Résidu : 144 assertions symboliques exactes, résidu rationnel nul;
  croissance endpoint normalisée `N` sur `N` coquilles logarithmiques.
- Résultat : `C_w*`, Duhamel Gelfand et correcteur `C_tL2` fermés; continuité
  forte critique, dissipation, énergie BSS, bornitude et rigidité absentes.
- Pivot : `GAP-TYPE-I-RELATIVE-ENERGY-GLOBALIZATION`.

## 2026-08-15 — énergie relative fermée, uniformité ancienne perdue

- Objet : solution faible adaptée locale sur `R3`, viscosité un, non forcée,
  pression globale de Riesz, uniformément faible-`L3` sur une bande finie.
- Scaling : `||w||_2²` et `integral||nabla w||_2²` ont le poids longueur
  `lambda^-1`; la longueur temporelle apparaît comme `T^(1/2)`.
- Compensation temporelle : `||V||_4^8~h^-1` est critique, mais le taux
  indépendant `||w||_2²=O(h^(1/2))` ramène le produit à `h^-1/2`.
- Pression : `q in L^(3/2,infinity)` n'a pas de queue absolument continue.
  Sur `A_R`, l'inclusion vers `L^(6/5)` coûte `R^(1/2)`; le gradient de
  cutoff et Young laissent un reste `O(R^-1)` uniforme.
- Dissipation : une première passe relative absorbée donne
  `w in L2_tHdot1`; une seconde conserve le signe exact du transfert et
  produit l'inégalité BSS.
- Contre-profil : un empilement solénoïdal multi-annulaire appartient à
  `L2 inter L^(3,infinity)` mais garde un flux cubique diagonal égal à un.
  Son coût de gradient diverge; il isole la nécessité de la propriété PDE.
- Résidu : 97 assertions symboliques exactes, résidu rationnel nul, flux
  adverse normalisé un à chaque couronne.
- Perte restante : constante non uniforme lorsque `t_0->-infinity`, absence
  de cohérence entre redémarrages et de rigidité ancienne.
- Pivot : `GAP-TYPE-I-BSS-ANCIENT-RIGIDITY`, avec branche parallèle de
  continuité forte mild.

## 2026-08-15 — cocycle exact, énergie de queue non uniforme

- Objet : même ancienne suitable locale, faible-`L3`, pression de Riesz;
  correcteur canonique `g_(s,t)=v(t)-S(t-s)v(s)` sur toute bande finie.
- Scaling : `L^(3,infinity)` est critique, tandis que
  `||g||_2` a le poids longueur `lambda^-1/2`; le temps long autorise donc la
  croissance dimensionnelle `h^(1/4)`.
- Gain : le cocycle est exact et la transition calorifique conserve son
  énergie. Le fond disparaît localement lorsque la base recule.
- Porte forte : `liminf||g_(s,r)||_2<infinity` le long d'une suite force
  `v(r) in L2`; aucune borne du ledger ne satisfait cette porte.
- Contre-profils : `U` et `U_sharp` saturent `h^(1/4)`. Le second est lisse,
  borné, dans `tilde L^(3,infinity) inter Hdot1`, avec incréments énergétiques
  sur chaque bande.
- Quotient : le dénominateur énergétique n'est pas fermé; même après passage
  au quotient séparé, la classe du profil reste non nulle et fixe.
- Résidu : 161 assertions exactes; limites itérées `0` contre `8pi/3`.
- Limite : les profils échouent Navier--Stokes par circulation non nulle; le
  résultat est fonctionnel, non une exclusion PDE.
- Pivot : `GAP-TYPE-I-BSS-ENERGY-TAIL-TIGHTNESS`, puis
  `GAP-TYPE-I-ANCIENT-QUOTIENT-RIGIDITY`.

## 2026-08-15 — saturation PDE et fermeture des hautes fréquences

- Objet forward adverse : solution auto-similaire de Leray locale, suitable,
  non forcée sur `R3`, issue d'une donnée moins-un homogène faible-`L3`.
- Scaling : `||u||_(3,infinity)` est critique; le correcteur relatif a le
  poids `lambda^(-1/2)` en `L2`, donc `t^(1/4)` en norme et `t^(1/2)` en
  énergie.
- Saturation : `W!=0` par le curl du terme convectif; exactement
  `||w(t)||_2=||W||_2t^(1/4)`. La PDE, la pression et la suitability forward
  ne suppriment pas cette croissance.
- Haute fréquence : le noyau de
  `Delta_jS(h)Pdiv : L^(3/2,infinity)->L2` coûte
  `2^(3j/2)e^(-ch2^(2j))`; après intégration, la queue `j>J` est uniformément
  `O(M^4 2^(-J))` en énergie.
- Perte exacte : les modes actifs glissent vers
  `2^j comparable (r-s)^(-1/2)`. Le faible-`L3`, Herz/Besov avec indice
  infini et Morrey critique contrôlent une échelle à la fois, sans somme
  infrarouge.
- Certificat : 615 assertions rationnelles exactes; proxy total
  `(15/7)2^n`, enveloppe calorifique `[1/3,4/3]2^n`, résidu de limite
  `15/7` et résidu rationnel nul.
- Limite : le saturateur est une famille forward singulière, non une ancienne
  unique et non une donnée Clay. Le calcul spectral séparé n'est pas une
  trajectoire Navier--Stokes.
- Pivot : `GAP-TYPE-I-ANCIENT-INFRARED-STRESS-DEPLETION`, puis
  `GAP-TYPE-I-SINGLE-ANCIENT-ORBIT-RECURRENCE`.
