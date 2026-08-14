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
