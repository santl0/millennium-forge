# Expériences Navier–Stokes

Les expériences de ce répertoire sont des tests analytiques finis. Elles ne
simulent pas une solution Navier–Stokes et ne constituent ni une preuve de
régularité ni un blow-up. Les vingt et une expériences utilisent la graine « sans
objet » et écrivent
leur rapport JSON sur la sortie standard.

## Matrice de reproduction

| ID | Question falsifiable | Arithmétique / discrétisation | Commande | Erreur certifiée |
|---|---|---|---|---|
| `VAS-1` | quand la viscosité est-elle perturbative dans un ansatz mono-échelle ? | rationnels exacts; aucune grille | `python -B experiments/navier-stokes/viscosity-gate/test_viscosity_gate.py` | zéro pour les identités testées |
| `TRI-PHASE-1` | divergence nulle et hélicité nulle imposent-elles un flux sous-linéaire universel ? | modes Fourier finis, rationnels gaussiens exacts | `python -B experiments/navier-stokes/triad-phase/test_triad_phase.py` | zéro |
| `VORTICITY-LOCAL-COHERENCE-SIGN-GATE-1` | une cohérence locale arbitrairement fine de la direction fixe-t-elle le signe ou déplète-t-elle sans échelle le stretching central ? | six modes Fourier, fractions rationnelles gaussiennes exactes; aucune grille | `python -B experiments/navier-stokes/vorticity-local-coherence/local_coherence_audit.py` | zéro pour les identités, la pression et les lois d'échelle |
| `SPARSENESS-RESTRICTION-1` | une densité volumique `delta` impose-t-elle une tranche linéaire `delta^(1/3)` au même point et rayon ? | preuve polaire + fractions exactes, profils radiaux et colonnes angulaires | `python -B experiments/navier-stokes/sparseness-restriction/sparseness_restriction_audit.py` | zéro pour toutes les identités algébriques |
| `REARRANGEMENT-INVERSION-1` | une enveloppe `v^-1/3 log^-1` de la réarrangée impose-t-elle une queue `lambda^-3 log^-3` malgré les plateaux ? | pseudo-inverses sur fonctions simples, fractions exactes et encadrements rationnels de logarithmes | `python -B experiments/navier-stokes/rearrangement-inversion/rearrangement_inversion_audit.py` | zéro pour toutes les identités et aucun flottant |
| `ONEIL-TRANSFER-1` | la queue logarithmique de vorticité se transfère-t-elle à la vitesse avec seuils, queue macroscopique et jauge harmonique suivis ? | fractions exactes, supersolutions analytiques et contre-profils en escalier; aucune grille | `python -B experiments/navier-stokes/oneil-transfer/oneil_transfer_audit.py` | zéro arrondi; marge rationnelle minimale huit |
| `DEGIORGI-UNIFORMITY-AUDIT-1` | la chaîne à un niveau `(23)->(40)` conserve-t-elle seuil, amortissement et logarithme uniformes sous (22) ? | fractions exactes et ledger symbolique; aucune grille | `python -B experiments/navier-stokes/degiorgi-uniformity/degiorgi_uniformity_audit.py` | douze contrôles; zéro échec |
| `COMMUTATOR-UNIFORMITY-AUDIT-1` | la dérive multi-échelle des moyennes détruit-elle le taux logarithmique de `(8)->(22)` ? | fractions exactes, sommes dyadiques et ledger de scaling; aucune grille | `python -B experiments/navier-stokes/commutator-uniformity/commutator_uniformity_audit.py` | huit contrôles; zéro échec |
| `ENDGAME-SYNCHRONIZATION-AUDIT-1` | temps garanti, niveau relatif, rayon sparse et rayon analytique peuvent-ils être choisis simultanément dans `(49)->(58)` ? | fractions exactes, branches temporelles et ledger de scaling; aucune grille | `python -B experiments/navier-stokes/endgame-synchronization/endgame_synchronization_audit.py` | onze contrôles; zéro échec |
| `DESINGULARIZATION-GATE-1` | les normes d'une troncature de `r^-1` restent-elles uniformes quand `epsilon -> 0` ? | intégrales radiales exactes; logarithme symbolique | `python -B experiments/navier-stokes/desingularization-gate/desingularization_gate.py` | zéro pour les identités rationnelles |
| `HWY-INNER-CUTOFF-GATE-1` | une régularisation intérieure divergence-free petite en `L²` et bornée en `L^{3,infinity}` est-elle compacte dans `L³` ? | matrices et intégrales exactes; transcendantes symboliques | `python -B experiments/navier-stokes/hwy-inner-cutoff/inner_cutoff_audit.py` | zéro pour les identités rationnelles et l'arrondi |
| `HWY-PARITY-PROJECTION-GATE-1` | un lissage intérieur respectant la réflexion HWY peut-il exciter le mode certifié impair ? | projecteurs de parité et exposants rationnels exacts; aucune grille | `python -B experiments/navier-stokes/hwy-parity-projection/parity_projection_audit.py` | zéro pour dix obligations; aucun arrondi |
| `ASYMPTOTIC-TRACE-CAUCHY-GATE-1` | une trace asymptotique commune à `tau=-infinity` impose-t-elle une même donnée de Cauchy à temps fini ? | fractions rationnelles exactes et exponentielle symbolique; aucune grille | `python -B experiments/navier-stokes/asymptotic-trace-cauchy-gate/trace_cauchy_audit.py` | zéro pour toutes les identités; aucun arrondi |
| `PRESSURE-TAIL-1` | centrer la pression d'un paquet distant gagne-t-il une puissance de distance ? | noyau multipolaire exact, tenseur ponctuel | `python -B experiments/navier-stokes/pressure-tail/pressure_tail.py` | zéro |
| `PRESSURE-MULTISCALE-1` | une borne physique `L²` seule impose-t-elle la tension uniforme de la pression après zoom ? | lois d'échelle et moments exacts | `python -B experiments/navier-stokes/pressure-multiscale/pressure_multiscale.py` | zéro |
| `QUADRATIC-PRESSURE-DEFECT-1` | énergie uniforme et convergence faible d'une trace imposent-elles la convergence du produit et de la pression ? | solution NS de Fourier exacte, fractions rationnelles | `python -B experiments/navier-stokes/quadratic-pressure-defect/quadratic_pressure_defect.py` | zéro |
| `TRACE-MODULUS-1` | le module temporel déduit de l'énergie atteint-il le seuil critique nécessaire à une trace forte ? | lois d'échelle et solution NS exacte, fractions rationnelles | `python -B experiments/navier-stokes/trace-modulus/trace_modulus.py` | zéro |
| `ANCIENT-PRESSURE-GAUGE-1` | ancienne, à vitesse bornée, adaptée et trace terminale nulle suffisent-elles à la rigidité sans normalisation de pression ? | solution NS exacte, fractions rationnelles | `python -B experiments/navier-stokes/ancient-pressure-gauge/ancient_pressure_gauge.py` | zéro |
| `BLOWUP-INHERITANCE-AUDIT-1` | une seule chaîne ESS/GKP/KNSS/Seregin transmet-elle toutes les hypothèses du Liouville hybride « ancienne + mild + vitesse bornée + trace locale nulle » ? | matrice sourcée et inclusion finie exacte | `python -B experiments/navier-stokes/blowup-inheritance-audit/inheritance_audit.py` | zéro échec d'assertion |
| `ANCIENT-ZERO-TRACE-RIGIDITY-AUDIT-1` | les hypothèses exactes « ancienne mild bornée + vraie trace `D'` nulle » franchissent-elles toutes les portes de rigidité, et les contre-profils usuels en violent-ils une explicitement ? | graphe d'obligations, ensembles finis et fractions rationnelles | `python -B experiments/navier-stokes/ancient-zero-trace-rigidity/rigidity_audit.py` | zéro échec d'assertion |
| `MAXIMUM-ZOOM-TRACE-COMMUTATOR-1` | les limites du zoom KNSS commutent-elles au temps-record `s=0`, et que reste-t-il à contrôler au temps physique `T` ? | graphe d'obligations, exposants et résidus rationnels exacts; `pi` symbolique | `python -B experiments/navier-stokes/maximum-zoom-trace/commutator_audit.py` | zéro échec d'assertion |

Environnement reproduit au checkpoint initial : Windows, Python 3.13.14,
bibliothèque standard uniquement. Les trois audits structurés lisent leur JSON
versionné voisin; les autres scripts sont autonomes. Aucun n'a de dépendance
réseau ni ne produit d'artefact lourd.

## `VAS-1` — seuil visqueux

- Équations testées : exposants de `partial_t u`, `(u dot nabla)u`, `nabla p`
  et `nu Delta u` pour
  `u=tau^lambda U(x/tau^(1+lambda))`.
- Entrées : intervalles rationnels documentaires pour deux profils inviscides,
  seuil NS `lambda=-1/2` et contrôle adverse `lambda=-3/4`. Les valeurs CCF et
  IPM proviennent respectivement de `arXiv:2509.14185` et
  `arXiv:2511.22819`; elles sont diagnostiques et ne sont pas nécessaires au
  claim de seuil.
- Résidu : six identités d'exposants exactement nulles.
- Sensibilité : le signe change exactement en `lambda=-1/2`.
- Limite : ne teste ni l'existence de `U`, ni ses queues, ni une construction
  NS multi-échelle.
- Provenance : import byte-for-byte du script historique, SHA-256
  `201cc2e97cb6ec35618019512fc6e9225459034e1bd6c65ac67165e5be08fb0a`.

## `TRI-PHASE-1` — triade signée

- Équation testée : terme non linéaire projeté de NS/Euler incompressible sur
  le tore normalisé, sur six modes Fourier explicites.
- Données : `a=(N,0,0)`, `b=(0,N,0)`, `c=(N,N,0)`, modes opposés conjugués et
  phase `sigma=+-1`; `N` parcourt `1,2,4,8,16,32,64`.
- Préservation : divergence, réalité, travail de pression et bilan d'énergie
  sont vérifiés exactement.
- Sortie décisive : `E=6`, hélicité modale et totale nulle,
  `|Pi_N|=2N`, somme absolue `4N`, ratio normalisé au carré `1/54`.
- Définitions :
  `E=(1/2)sum_k |u_hat(k)|²`,
  `Q_k=-i P_k sum_(p+q=k)(q dot u_hat(p))u_hat(q)` et
  `Pi_N=-sum_(0<|k|<=N) Re(conj(u_hat(k)) dot Q_k)`, avec coupure
  euclidienne et `N` entier positif.
- Certificat pour tout `N` : le calcul symbolique donne
  `T_(+-a)=0`, `T_(+-b)=sigma N`, `T_(+-c)=-sigma N`. Les modes `a,b`
  sont sous la coupure et `c` au-dessus, d'où `Pi_N=-2 sigma N`; la
  dépendance en `N` est algébrique, pas extrapolée des sept cas exécutés.
- Résidu et précision : nombres rationnels gaussiens, résidu exact zéro.
- Sensibilité : changer la phase inverse le sens du flux sans changer les
  invariants quadratiques.
- Limite : champ instantané, pas trajectoire NS; aucune conclusion sur une
  hypothèse géométrique locale plus forte.
- Provenance : dérivé du script historique SHA-256
  `a02b6959a5c00dbb248864ccd43ba55336769869d83bc73fd21d05ad4419e493`;
  suppression d'un helper inutilisé et renommage anglais. Empreinte Forge :
  `c469d9a9984753c95fa0f21cd8fbeb723bd6ed1f8c6a500376af02d13ce5da33`.

## `VORTICITY-LOCAL-COHERENCE-SIGN-GATE-1` — cohérence locale et stretching signé

- Question : la cohérence locale de `xi=omega/|omega|`, jointe à l'énergie,
  l'enstrophie, la palinstrophie et l'hélicité globale, détermine-t-elle le
  signe ou une petite borne sans échelle sur `omega·S omega` au centre ?
- Équation réellement testée : donnée initiale analytique pour Navier–Stokes
  incompressible 3D non forcé, `nu>0`, sur le tore normalisé; aucune évolution
  discrétisée.
- Champs :
  `u_a=(sin y+a sin x cos z,0,-a cos x sin z)`, `a=+-1`, et
  `omega_a=(0,-2a sin x sin z,-cos y)`.
- Préservation : réalité et divergence nulles mode par mode; pression de
  moyenne nulle reconstruite par la convolution de Poisson,
  `p_a=(a²/4)(cos 2x+cos 2z)`.
- Données appariées : `E=1/2`, `Z=3/4`, palinstrophie `5/2`, hélicité zéro,
  même vorticité `-e_3` et même premier jet nul à l'origine. Le changement
  `a->-a` est la translation exacte `x->x+pi`.
- Sortie décisive : `omega·S omega=-a cos x cos z cos²y`; il vaut `-a` au
  centre et garde ce signe sur `Q_r`, `0<r<=1/2`, avec module au moins
  `(1-r²/2)^4`.
- Cohérence certifiée :
  `sin angle(xi(X),xi(0))<=2r²/(1-r²/2)` et
  `sin angle(xi(X),xi(Y))<=(2r/(1-r²/2))||X-Y||_1` sur `Q_r`.
- Échelle : pour `U_N=N u(Nx)`, énergie `N²`, enstrophie `N⁴`,
  palinstrophie et production ponctuelle `N⁶`, tandis que le ratio critique
  `(omega·S omega)/|omega|³` au centre reste `-a`. Le lift `u(Nx)` est aussi
  contrôlé séparément.
- Arithmétique : six modes Fourier, `fractions.Fraction`, aucune grille,
  graine, FFT ou valeur flottante; tous les résidus algébriques sont nuls.
- Sensibilité : les bornes de direction deviennent arbitrairement petites en
  rétrécissant le cube, sans diminuer le stretching central.
- Limites : instant initial seulement; pas de borne énergétique uniforme sous
  scaling critique, pas de contrôle de tout le high-vorticity set, pas de
  persistance temporelle. Les critères intégrés de Constantin–Fefferman et
  Beirão da Veiga–Berselli ne sont pas réfutés.
- Empreinte :
  `04112a48e77a5286fd3e98a73471577a7f30a9b0acbd027699177b6204649708`.

## `SPARSENESS-RESTRICTION-1` — volume 3D vers tranche linéaire

- Question falsifiable : pour un borélien `S⊂R³`, une densité au plus `delta`
  dans `B_r(x_0)` impose-t-elle une direction centrale dont la densité sur
  `(-r,r)` est au plus `delta^(1/3)`, avec le même point et le même rayon ?
- Dérivation : la formule polaire signée porte un facteur `1/2`; parmi les
  ensembles `A⊂(-r,r)` de longueur `m`, le moment
  `integral_A t² dt` est minimal sur l'intervalle centré et vaut `m³/12`.
  Après normalisation par `|B_r|`, une direction vérifie le seuil annoncé.
- Optimalité : `S=B_(r delta^(1/3))(x_0)` sature la borne dans toutes les
  directions. En dimension `d`, la même preuve donne `delta^(1/d)`.
- Application : si `|V|≤B`, le rayon construit
  `r_B=[B/(delta |B_1|)]^(1/3)` fonctionne pour tout centre, avec une direction
  pouvant dépendre du centre. Les rayons garantis par la seule mesure vérifient
  `r³≥B/(delta|B_1|)`; les rayons arbitrairement plus petits ne sont pas
  certifiés. Pour `delta=3/4`, `delta|B_1|=pi`.
- Test adverse : la boule centrale est extrémale; coquilles, colonnes
  angulaires et dimensions `1,...,6` testent les constantes. Le certificat
  emploie `Fraction`, aucune grille, aucun flottant et aucune graine.
- Résidus : toutes les identités algébriques valent `0/1`; le seuil
  `(3/4)^(1/3)` est encadré strictement par `90856/100000` et
  `90857/100000`.
- Empreinte du script :
  `efe3ccaa41bd97988a7bd7c58c728af35f8dc6665d53d3f9df7052a1f34fe19b`.
- Limite : le test ne valide ni la borne de distribution, ni le commutateur,
  ni l'analyticité, ni le maximum harmonique de `arXiv:2607.08866v2`.

## `REARRANGEMENT-INVERSION-1` — quantile logarithmique exact

- Question falsifiable : une borne uniforme
  `f*(v)<=A_0(V_0/v)^(1/3)/log(eV_0/v)` sur un même intervalle
  `0<v<=theta_0V_0` implique-t-elle une queue uniforme
  `lambda^-3 log^-3` ?
- Lemme : pour
  `lambda>=A_0 max(1,theta_0^(-1/3)/log(e/theta_0))`,

  ```text
  mu_f(lambda)
    <=V_0(A_0/lambda)^3/[1+3log(lambda/A_0)]^3.
  ```

- Réparation : l'égalité `lambda=f*(mu_f(lambda))` est fausse sur les
  plateaux. La preuve utilise l'équivalence
  `mu_f(lambda)>v <=> f*(v)>lambda` pour tout `v<mu_f(lambda)`, puis la limite
  croissante vers la masse du superniveau.
- Contre-profil : pour les valeurs `4,2,0` sur les masses
  `1/8,3/8,1/2`, `mu_f(3)=1/8`, mais `f*(1/8)=2`; en revanche
  `f*(1/16)=4>3`, exactement comme l'exige la preuve réparée.
- Optimalité : l'enveloppe saturante donne asymptotiquement le coefficient
  principal `A^3/27` devant `lambda^-3log^-3`.
- Échelle : sous NS, `V_0` porte `kappa^-3`, `A_0` et le niveau portent
  `kappa`, leur rapport est invariant et la distribution porte `kappa^-3`.
- Discrétisation : aucune PDE, aucun maillage ni pas de temps. Les logarithmes
  sont encadrés par une série de `atanh` et un reste géométrique rationnel.
- Résidus : pseudo-inverse, puissances, constantes et scaling exactement
  nuls; graine sans objet; aucun arrondi.
- Empreinte :
  `0b306177085e584f1a658b4b9534ea74d7ca0ce07c599c7bf9295a95fdc804f7`.
- Limite : suppose (47) avec constante et cutoff uniformes; ne valide ni sa
  dérivation par O'Neil, ni la représentation Biot–Savart, ni le théorème 7.4.

## `ONEIL-TRANSFER-1` — queue de vorticité vers vitesse

- Question falsifiable : une queue uniforme
  `mu_omega(lambda)<=V[(Omega/lambda)/log(lambda/Omega)]^(3/2)`, complétée
  par le contrôle global faible `L^(3/2)` et une jauge Biot–Savart explicite,
  implique-t-elle (47) ?
- Inversion : pour `0<s<=Vexp(-3)`,
  `omega*(s)<=4Omega(V/s)^(2/3)/log(eV/s)`.
- Intégrales : sur `0<v<=Vexp(-6)`, le coeur a la constante `3`, une
  supersolution donne `20` pour la queue logarithmique et la queue globale
  coûte `9M`.
- Conclusion : si `u=B[omega]+h`, `||h||_infinity<=H`, alors

  ```text
  u*(v)<=Qv^(-1/3)/log(eV/v),
  Q=C_K(23C_0+9M)+HV^(1/3),  C_0=4Omega V^(2/3).
  ```

- Résultat négatif : le reste positif de (46) n'est pas `O(1)`;
  `R(exp(-3n))>=3n/256` et
  `R(v)~9v^(-1/3)/log²(e/v)`. Il reste absorbable.
- Jauge adverse : `u=(2,-3,6)` a divergence et rotationnel nuls, mais une
  réarrangée égale à sept; (41) est faux pour la vitesse entière sans
  normalisation harmonique.
- Queue adverse : un plateau de masse `R³` produit exactement
  `3(R-1)` dans l'intégrale macroscopique; le petit-volume seul ne suffit pas.
- Échelle : `C_0`, `M` et `HV^(1/3)` sont invariants sous le scaling NS;
  le membre droit porte `kappa` comme la vitesse.
- Discrétisation : aucune PDE, aucun maillage ni pas de temps. Toutes les
  obligations sont rationnelles ou réduites à des inégalités de séries à
  coefficients positifs.
- Résidus : algèbre, divergence et rotationnel exactement nuls; marge minimale
  du supersolution `8`; aucun flottant ni graine.
- Empreinte :
  `cab6da2b536cfd5a72fd669887fe7dc444a283eba081bbfb9b02b9889897c06f`.
- Limite : suppose (40), O'Neil et la décomposition de Hodge; ne valide ni
  l'étape De Giorgi qui produit (40), ni le commutateur, ni le théorème 7.4.

## `DESINGULARIZATION-GATE-1` — premier cycle autonome

- Question : la contribution de coquille d'un champ homogène
  `u_0(r,theta)=r^-1 A(theta)`, conservé sur `epsilon<=r<=1`, reste-t-elle
  uniforme dans plusieurs normes usuelles quand `epsilon` tend vers zéro ?
- Donnée : `0<epsilon<1`, profil angulaire fixe avec
  `0<C_q=integral_S2 |A|^q<infinity`; pour le gradient,
  `A in H^1(S2)` et
  `C_grad=integral_S2 (|A|²+|grad_S A|²)>0`. Le test ne reconstruit pas le
  profil précis de Hou–Wang–Yang.
- Résolution : `epsilon=10^-k`, `k=1,2,4,8,16`; aucune discrétisation spatiale
  ou temporelle.
- Résultat : `L^q`, `q<3`, reste borné; `||u||_3^3` croît comme
  `log(1/epsilon)`; pour `q>3`,
  `||u||_q~epsilon^(3/q-1)`; et
  `||grad u||_2~epsilon^-1/2`.
- Résidu : identités rationnelles zéro; `log(10)` est laissé symbolique.
- Analyse d'erreur : aucune erreur d'arrondi; les constantes angulaires sont
  explicitement hors calcul et doivent être non nulles pour conclure dans le
  canal correspondant.
- Limite : pour une troncature globale, le calcul n'est qu'une borne inférieure
  de coquille et n'estime pas les couches de raccord. Il ne teste ni divergence,
  ni PDE, ni temps d'existence. Des solutions de cisaillement lisses peuvent
  avoir ces normes grandes tout en étant globales; les divergences interdisent
  seulement de supposer gratuitement leur uniformité.

## `HWY-INNER-CUTOFF-GATE-1` — régularisation intérieure exacte

- Question : supprimer le coeur `r^-1` d'une donnée singulière par une famille
  `C_c^infinity`, exactement divergence-free, donne-t-il une compacité dans
  l'espace critique fort `L³` à partir de la convergence `L²` et d'une borne
  `L^{3,infinity}` ?
- Donnée : `a(x)=(-x_2,x_1,0)/|x|²`, cutoff extérieur radial fixe et cutoff
  intérieur radial plat à l'échelle `epsilon`. La tangence `x dot a=0`
  préserve exactement la divergence; chaque donnée est Clay-admissible sur
  `R³`.
- Échelles : `epsilon=10^-k`, `k=1,2,4,8,16`; aucune grille ni évolution PDE.
- Résultat : la différence à la limite singulière a une norme `L³` infinie et
  une quasi-norme `L^{3,infinity}` au moins `(pi²/4)^(1/3)`. La famille lisse
  converge en `L²`, reste uniformément bornée en `L^{3,infinity}`, mais
  `||u_epsilon-u_(2epsilon)||_3³` garde le minorant strict
  `[e^(8/3)/(1+e^(8/3))]^3(3pi²/4)log(5/4)`.
- Régularité :
  `||nabla u_epsilon||_2² >= 4pi/epsilon-8pi` et
  `||u_epsilon||_infinity>=1/(2epsilon)`.
- Pression : reconstruite analytiquement par
  `p=R_iR_j(u_i u_j)`; la borne de multiplicateur
  `||p||_2<=||u||_4²<=[(32pi/15)(epsilon^-1-1/2)]^(1/2)` est globale. Le
  script l'enregistre symboliquement mais ne résout aucune évolution.
- Résidu et précision : antisymétrie, trace, tangence, constantes angulaires et
  coefficients radiaux vérifiés par fractions; transcendantes laissées
  symboliques positives; zéro arrondi.
- Limite : réfute un module fonctionnel universel au temps initial, pas une
  stabilité pour `t>=tau>0`, un temps maximal uniforme, la CAP HWY ou un
  blow-up Clay.

## Passage au continuum

Aucune des vingt expériences ne part d'une discrétisation PDE : il n'y a donc
pas de passage grille-vers-continuum. Le raccord analytique restant est
explicite dans chaque cas. Tout futur solveur doit ajouter divergence mesurée,
convergence multi-résolution, second schéma, bornes de troncature, contrôle des
frontières, énergie/enstrophie/normes critiques, versions logicielles et
empreintes des sorties.

## `HWY-PARITY-PROJECTION-GATE-1` — sélection exacte par réflexion

- Question : une convolution ou un cutoff radial du coeur HWY, donc pair pour
  l'involution `(Ju)(x)=S u(Sx)`, peut-il projeter une composante sur le mode
  d'instabilité certifié impair ?
- Équation : NS incompressible 3D non forcé sur `R³`, viscosité `1`; seule
  l'équivariance de la solution forte locale, de la chaleur, de la projection
  de Leray et de la linéarisation est utilisée. Aucune trajectoire PDE n'est
  discrétisée.
- Échelle : pour `g_epsilon=epsilon^-1 g(x/epsilon)` et
  `t=kappa epsilon²`, le profil de similarité
  `sqrt(t)e^(tDelta)g_epsilon(sqrt(t)xi)` est indépendant d'`epsilon`.
- Résultat : `Q_-g_epsilon=0` exactement dans le cas symétrique. Si une
  composante impaire `epsilon^beta` a un pairing adjoint non nul, le facteur
  linéaire est `kappa^-a epsilon^-2a`; la borne source
  `a>=217/2000` impose nécessairement `beta>=217/1000`, sans suffire au
  contrôle non linéaire.
- Test adverse : un couplage pair vers impair donne un commutateur maximal `2`
  et une excitation impaire `3`; la commutation est donc testée et essentielle.
- Résidu et précision : dix obligations rationnelles exactement nulles,
  aucune conversion flottante, aucune graine, aucune discrétisation.
- Limite : le modèle matriciel encode la logique des secteurs, pas l'opérateur
  HWY. Il n'exclut ni mode instable pair, ni asymétrie, ni brisure faible après
  perte de l'unicité forte; il ne certifie aucun adjoint dynamique.
- Empreinte : SHA-256
  `432f9eda20dbb7ee3ea70562f83359be9c0ad7877a8f9a76efadbb70d0ccb06e`.

## `PRESSURE-TAIL-1` — pression distante et jauge

- Objet : noyau de pression sur `R^3`,
  `K_ij(z)=(3z_i z_j-|z|² delta_ij)/(4 pi |z|^5)`.
- Lemme analytique testé : pour un paquet divergence-free `v` supporté dans
  `B_rho(R e_1)`, `R>a+rho`, et `x in B_a(0)`, le théorème des accroissements
  finis donne

  ```text
  |p_v(x)-p_v(0)|
    <= (21/pi) a (R-a-rho)^(-4) ||v||_2².
  ```

  En effet, la dérivée directionnelle de chaque `K_ij` est au plus
  `7/pi |z|^-4`, et
  `sum_(i,j)|v_i v_j| <= 3|v|²`.
- Jauge : pour tout champ test compact divergence-free `w` et cutoff `phi`,
  `integral p_v(0) w dot grad(phi)=0`. La constante distante d'ordre `R^-3`
  ne travaille donc pas dans l'énergie locale; la variation active gagne une
  puissance `R^-4`.
- Expérience : moment principal `M=diag(1,1,0)` à distance `R`; après
  normalisation par `4 pi`, `p_R(0)=R^-3` et
  `p_R(e_1)-p_R(0)=(R-1)^-3-R^-3`. Le résidu de l'identité rationnelle est
  exactement zéro et `R^4` fois la différence tend vers `3`.
- Réalisabilité : `M` est le moment d'un paquet lisse compact divergence-free
  `v=(partial_2 psi,-partial_1 psi,0)` avec `psi` radial dans les deux premières
  variables et pair dans la troisième, après normalisation.
- Sensibilité : distances `R=2,4,...,128`; aucun flottant, graine ou pas de
  temps.
- Limite décisive : la borne contient l'énergie globale du paquet. Sous un zoom
  de blow-up, cette constante n'est pas automatiquement uniforme, et une somme
  de paquets proches de l'échelle active relève du terme de pression proche,
  non de cette queue. Le résultat ne ferme donc pas compacité–rigidité.
- Covariance : sous `v_lambda(x)=lambda v(lambda x)`, la géométrie devient
  `(a,rho,R)/lambda`, tandis que
  `||v_lambda||_2²=lambda^-1||v||_2²`; le membre droit acquiert exactement
  `lambda²`, comme `p_lambda`. Le lemme ne crée donc aucun gain d'échelle caché.

## `PRESSURE-MULTISCALE-1` — défaut de tension après zoom

### Lemme positif borné

Pour une famille `U_n`, définissons directement la différence distante, sans
supposer l'existence séparée des deux pressions brutes,

```text
D_n^far(x;A)=integral_(|y|>A)
  [K_ij(x-y)-K_ij(-y)] U_(n,i)(y)U_(n,j)(y) dy.
```

Pour `|y|>A>2a`, la même borne directionnelle du noyau donne

```text
sup_(|x|<=a) |D_n^far(x;A)|
 <= (21/pi) a (1-a/A)^(-4)
    integral_(|y|>A) |U_n(y)|² |y|^(-4) dy.
```

La condition de tension pondérée

```text
lim_(A->infinity) sup_n
  integral_(|y|>A) |U_n(y)|² |y|^(-4) dy = 0
```

suffit donc à rendre la pression distante centrée uniformément petite sur les
boules fixes. Ce lemme ne contrôle pas la pression proche.

Une borne critique `L³` implique cette tension par Hölder :

```text
integral_(|y|>A)|U(y)|²|y|^-4dy
 <= ||U||_3² (integral_(|y|>A)|y|^-12dy)^(1/3)
 = (4pi/9)^(1/3) A^-3 ||U||_3².
```

Par conséquent, si `sup_n||U_n||_3<=M`, le supremum des queues est au plus
`(4pi/9)^(1/3)A^-3M²` et tend vers zéro avec `A`.

Ainsi, dans une chaîne de compacité qui suppose déjà
`sup_n ||U_n||_3<infinity`, la pression lointaine centrée n'est pas le verrou.
Cette observation ne produit évidemment pas la borne `L³` depuis l'énergie.

### Famille adverse lisse

Fixons `0<kappa<1/4` et un champ

```text
w=(partial_2 psi,-partial_1 psi,0) in C_c^infinity(B_kappa)
```

où `psi` est radial, puis normalisons-le pour que

```text
integral w_i w_j = diag(1,1,0)_ij,
||w||_2²=2.
```

Pour `n>=1`, posons

```text
L_n=2^(-6n),  r_n=2^(-7n),  mu_n=2^(-3n),
v_n(x)=sqrt(mu_n/r_n³) w((x-L_n e_1)/r_n).
```

Chaque `v_n` est lisse, compact, divergence-free et
`||v_n||_2²=2mu_n->0`. Après le zoom NS
`U_n(y)=r_n v_n(r_n y)`, le paquet est centré en

```text
R_n=L_n/r_n=2^n,
```

et son moment vaut `mu_n/r_n=R_n^4`. Par convergence uniforme sur le support
fixe de `w`,

```text
integral |U_n(y)|² |y|^-4 dy -> 2,
P_n(e_1)-P_n(0) -> 3/(4 pi).
```

Le passage multipolaire se lit directement, uniformément pour
`|z|<=kappa` :

```text
R^4 [K(e_1-R e_1-z)-K(-R e_1-z)]
 = R [K(-e_1+(e_1-z)/R)-K(-e_1-z/R)]
 -> partial_1 K(-e_1).
```

La contraction de `partial_1 K(-e_1)` avec `diag(1,1,0)` vaut
`3/(4pi)`. De même,
`R^4/|R e_1+z|^4->1` uniformément, ce qui donne la limite pondérée `2`.

La pression brute `P_n(0)` diverge comme `R_n/(4 pi)`, mais c'est sa constante
de jauge; la différence centrée reste finie et non nulle. Ainsi l'énergie
cinétique physique `mu_n`, et même `||v_n||_2²=2mu_n`, tendent vers zéro sans
imposer la tension pondérée après un zoom arbitrairement plus fin que le paquet.

### Certificat et limites

- Le script vérifie exactement
  `R_n=2^n`, `mu_n/r_n=R_n^4`,
  `mu_n r_n³/L_n^4=1`, la queue ponctuelle pondérée `2`, et
  `4 pi (P_n(e_1)-P_n(0))->3`.
- Empreinte du script :
  `c69d3c45b5383596cb3ccc1b804ad94ef3ccbfa9b5d49c7e7f237c72abbe12fd`.
- Arithmétique : fractions exactes, aucune discrétisation, résidus nuls, graine
  sans objet.
- La limite du paquet lisse repose sur un développement multipolaire uniforme
  sur un support compact; le script ne formalise pas cette étape.
- Les `v_n` sont des données initiales admissibles prises séparément, pas des
  tranches d'une même solution NS ni un scénario de blow-up.
- Le résultat réfute seulement une déduction depuis l'énergie globale. Une
  borne critique, une tension pondérée ajoutée ou la dynamique peuvent exclure
  cette famille.

## `QUADRATIC-PRESSURE-DEFECT-1` — défaut exact sur une trace parabolique

### Solution réellement testée

Sur `T³=(R/2piZ)³`, avec viscosité `nu=1`, force nulle et conditions
périodiques, posons pour tout entier `N>=1`

```text
psi_N(x_1,x_2)=N^-1 sin(x_1)cos(Nx_2),
u_N^0=curl(psi_N e_3)
     =(-sin(x_1)sin(Nx_2),-N^-1 cos(x_1)cos(Nx_2),0).
```

Le champ est analytique et divergence-free. Un calcul direct donne

```text
(u_N^0 dot nabla)u_N^0
  =((1/2)sin(2x_1),-(1/(2N))sin(2Nx_2),0)=nabla q_N,
q_N=(1/2)sin²(x_1)+(1/(4N²))cos(2Nx_2),
Delta u_N^0=-(N²+1)u_N^0.
```

La pression moyenne nulle associée est

```text
p_N^0=(1/4)cos(2x_1)-(1/(4N²))cos(2Nx_2)=-q_N+1/4.
```

Par conséquent

```text
u_N(t)=a_N(t)u_N^0,
p_N(t)=a_N(t)²p_N^0,
a_N(t)=exp(-(N²+1)t)
```

est une solution globale lisse exacte des équations de Navier–Stokes non
forcées. Le calcul recalcule donc la pression de Leray; il ne la prescrit pas
indépendamment.

### Test falsifiable et résultat

Au temps `t_N=log(2)/(N²+1)`, `a_N(t_N)=1/2`. Lorsque `N->infinity`,
l'orthogonalité de Fourier implique

```text
u_N(t_N) converge faiblement vers 0 dans L²(T³),
u_N(t_N) tensor u_N(t_N)
  converge faiblement vers diag((1/8)sin²(x_1),0,0),
p_N(t_N) converge fortement vers (1/16)cos(2x_1) dans tout L^q fini.
```

La pression moyenne nulle du champ limite `u=0` vaut pourtant zéro. Ainsi,
une borne uniforme d'énergie et de dissipation, combinée à la seule convergence
faible d'une trace, ne suffit pas au passage à la limite quadratique ni à la
continuité de l'opérateur pression sur cette topologie.

Avec la moyenne normalisée du tore,

```text
||u_N^0||_2²=(1/4)(1+N^-2),
||u_N(t_N)||_2²=(1/16)(1+N^-2).
```

L'identité d'énergie est vérifiée exactement : l'énergie cinétique à `t_N`
plus la dissipation intégrée vaut l'énergie cinétique initiale.

### Résidu, sensibilité et portée

- Résolutions fréquentielles : `N=1,2,4,...,128`; aucun maillage ni pas de
  temps. La formule est symbolique pour tout entier positif.
- Précision : fractions rationnelles exactes; `log(2)` est conservé comme
  symbole. Résidus de divergence, équation de quantité de mouvement, Poisson
  pour la pression, valeur propre du Laplacien et énergie : `0/1`.
- Graine : sans objet. Environnement : Python standard épinglé par le dépôt.
- Sensibilité : à tout temps fixe `t>0`, l'amortissement tend exponentiellement
  vers zéro et la convergence devient forte. Le défaut est confiné à une couche
  initiale parabolique `t_N~N^-2`.
- Limite : cette famille ne produit ni singularité, ni défaut dans l'intérieur
  espace-temps, ni contre-exemple à la compacité d'Aubin–Lions sur un cylindre
  fixé. Elle falsifie seulement une implication portant sur des traces mobiles
  sans équicontinuité temporelle forte.

### Hypothèse suffisante qui élimine le défaut local

Sur un compact `K`, si `u_n->u` fortement dans `L³(K)`, alors

```text
||u_n tensor u_n-u tensor u||_(L^(3/2)(K))
 <= (||u_n||_3+||u||_3)||u_n-u||_3 -> 0.
```

Après localisation, les transformées de Riesz donnent la même convergence
`L^(3/2)` pour la pression proche. L'énergie seule ne fournit pas cette
convergence sur une trace; dans un cylindre espace-temps, les bornes d'énergie
et la compacité forte `L²` permettent en revanche, par interpolation avec la
borne `L^(10/3)`, d'obtenir `L^q` fort pour chaque `q<10/3`, donc `q=3`.
Ce critère n'est pas minimal pour la seule convergence distributionnelle du
produit : une convergence locale forte `L²` y suffit déjà.

## `TRACE-MODULUS-1` — seuil critique d'une trace temporelle

### Question et loi d'échelle

La question falsifiable est : les bornes uniformes de Leray–Hopf imposent-elles
un module temporel fort, invariant sous l'échelle NS, qui élimine le défaut de
trace du cycle 0004 ?

Sur `R³`, pour

```text
u_lambda(x,t)=lambda u(lambda x,lambda²t),
```

on a, dans les espaces homogènes,

```text
||u_lambda(t)||_(dot H^sigma)
 =lambda^(sigma-1/2)||u(lambda²t)||_(dot H^sigma),
[u_lambda]_(C_t^alpha dot H_x^sigma)
 =lambda^(sigma-1/2+2alpha)[u]_(C_t^alpha dot H_x^sigma).
```

Le seuil critique est donc `alpha=1/4-sigma/2`. En particulier,
`C_t^(1/4)L²_x` et `C_t^(3/4)dot H^-1_x` sont critiques. Le module
`C_t^(1/4)H^-1_x` issu de l'énergie porte au contraire le facteur
`lambda^-1`; il perd exactement une puissance d'échelle lors d'un zoom
`lambda->0`.

### Module réellement fourni par l'énergie

Sur le tore, soit une solution Leray–Hopf de moyenne nulle. On note
`dot H^-1` la norme de Fourier sans mode nul et, pour
`I=[s,t]`,

```text
M_I=sup_(tau in I)||u(tau)||_2,
D_I=(integral_I ||nabla u||_2² d tau)^(1/2),
h=t-s.
```

L'équation dans `H^-1`, Hölder en temps et
`||u||_4<=C_GN||u||_2^(1/4)||nabla u||_2^(3/4)` donnent

```text
||u(t)-u(s)||_(dot H^-1)
 <= nu h^(1/2)D_I
    +C_GN² M_I^(1/2)h^(1/4)D_I^(3/2).
```

La constante `C_GN` dépend seulement du tore et de la normalisation; elle est
indépendante de la solution et de la troncature. Sur un horizon fini `[0,T]`,
en remplaçant `D_I` par `D_T` et en utilisant `h^(1/2)<=T^(1/4)h^(1/4)`, on
obtient

```text
[u]_(C_t^(1/4)dot H^-1;[0,T])
 <=nu T^(1/4)D_T+C_GN² M_T^(1/2)D_T^(3/2).
```

L'énergie donne donc ce module faible sur chaque horizon fini, mais pas le
module critique `C_t^(3/4)dot H^-1` ni un module fort `L²`.

### Test adverse exact

Reprenons la solution périodique du cycle 0004. Tous ses modes ont
`|k|²=N²+1`; à `t_N=log(2)/(N²+1)`,

```text
||u_N(t_N)-u_N(0)||_2²=(N²+1)/(16N²),
||u_N(t_N)-u_N(0)||_(dot H^-1)²=1/(16N²).
```

Pour les quotients sur la seule paire `(0,t_N)`, le script certifie

```text
256 log(2) [Q_N^(L²,1/4)]^4
 =256 log(2)^3 [Q_N^(H^-1,3/4)]^4
 =(N²+1)^3/N^4 ~ N²,

256 log(2) [Q_N^(H^-1,1/4)]^4
 =(N²+1)/N^4 ~ N^-2.
```

Les deux modules critiques divergent au moins comme `N^(1/2)`, tandis que le
quotient faible fourni par l'énergie tend vers zéro comme `N^(-1/2)`. Pour le
semi-module faible complet, l'identité de semi-groupe et
`1-exp(-z)<=min(z,1)` donnent aussi

```text
[u_N]_(C_t^(1/4)dot H^-1)
 <= ||u_N^0||_2 (N²+1)^(-1/4),
```

donc une borne uniforme qui ne supprime pourtant pas le défaut quadratique.

### Lemme de raccord et limites

Si `u_n(0)->u_0` fortement dans `L²` et si
`sup_n[u_n]_(C_t^(1/4)L²)<infinity`, alors, pour toute suite `t_n->0`,

```text
||u_n(t_n)-u_0||_2
 <= C t_n^(1/4)+||u_n(0)-u_0||_2 ->0.
```

Les produits convergent alors dans `L¹`, et les pressions convergent comme
distributions après application de la projection de Leray. Ce raccord est
critique mais conditionnel : l'expérience prouve que l'énergie ne fournit pas
sa prémisse uniformément.

Un raccord plus faible, mais utile, ne demande pas ce taux `L²`. Si les données
`u_n(0)` appartiennent à un compact `K` de `L²`, l'inégalité d'énergie et le
module uniforme dans `V'` suffisent. Pour un projecteur de Fourier fini `P_m`,

```text
||u_n(t)-u_n(0)||_2²
 <=2 omega(t) sup_(v in K)||P_m v||_V
   +4 sup_(v in K)||v||_2 sup_(v in K)||(I-P_m)v||_2.
```

Prendre d'abord `m` grand par compacité de `K`, puis `t` petit, donne une trace
forte uniforme. La famille adverse n'a précisément pas de données initiales
fortement précompactes : elle converge seulement faiblement et conserve une
norme `L²` non nulle.

- Résolutions : `N=1,2,4,...,128`; aucune grille ou intégration temporelle.
- Précision : fractions exactes; les puissances de `log(2)` restent
  symboliques. Résidu maximal `0/1`; graine sans objet.
- Portée : l'invariance est calculée sur `R³`, tandis que le contre-test est
  périodique. Il réfute une estimation énergétique universelle, mais ne prouve
  pas qu'une suite minimale de blow-up réalise ce défaut.
- Résultat négatif : une compacité temporelle dans une topologie trop faible
  peut coexister avec un défaut de Reynolds et de pression sur la trace.

## `ANCIENT-PRESSURE-GAUGE-1` — solution parasite et jauge harmonique

### Équation et contre-exemple exact

Sur `R³ x (-infinity,0]`, pour toute viscosité `nu>0`, posons

```text
a(t)=-t/(1+t²),
u(x,t)=a(t)e_1,
p(x,t)=-a'(t)x_1=((1-t²)/(1+t²)²)x_1.
```

Alors `div u=0`, `Delta u=0`, `(u dot nabla)u=0` et
`partial_t u+nabla p=0`. La solution est lisse, ancienne, non forcée et

```text
sup_(t<=0,x)|u(x,t)|=1/2,
u(x,0)=0,
u(x,-1)=(1/2)e_1.
```

Elle est donc non triviale malgré une trace terminale nulle. La pression est
locale `L^(3/2)` et l'identité locale d'énergie est exacte :

```text
partial_t(|u|²/2)+div((|u|²/2+p)u)
 =a a'+a(-a')=0.
```

La famille est ainsi classique et adaptée localement, mais n'a ni énergie
globale finie, ni décroissance spatiale, ni norme globale `L³`.

### Pourquoi la solution n'est pas mild

Pour une vitesse spatialement constante `b(t)`, la formule mild entre `s<t`
se réduit à

```text
b(t)=exp((t-s)Delta)b(s)=b(s),
```

car `div(b tensor b)=0`. Elle impose donc que `b` soit constante. Pour
`s=-1`, `t=0`, la solution adverse a un défaut mild exact `-1/2`.

La même obstruction se lit dans la pression. L'équation de Poisson donne
seulement

```text
-Delta p=partial_i partial_j(u_i u_j)=0,
```

et ne détecte pas le terme harmonique affine `-a'(t)x_1`. Une normalisation
par les transformées de Riesz donne un gradient nul pour le tenseur constant,
alors que le gradient réel vaut `e_1` à `t=0`.

### Porte BMO et lemme minimal

Une fonction affine non constante n'appartient pas à `BMO(R³)`. À `t=0`,
`p=x_1`; sur le cube `Q_R=[-R,R]³`, sa moyenne est zéro et

```text
average_(Q_R)|p-average_(Q_R)p|=R/2 -> infinity.
```

Plus généralement, toute solution spatialement constante `u=b(t)` a
`p=-b'(t) dot x+c(t)`. L'une ou l'autre des conditions suivantes force
`b'(t)=0` :

1. la formule mild sur chaque intervalle compact;
2. une pression appartenant à `BMO_x` modulo les constantes temporelles;
3. la normalisation de pression de Leray/Riesz excluant toute partie affine.

Avec la trace terminale `b(0)=0`, chacune donne `u=0`. La mildness n'est donc
pas un raffinement cosmétique : elle ferme exactement une liberté harmonique
que l'équation de Poisson et l'inégalité locale d'énergie laissent ouverte.

### Reproduction et limites

- Temps testés : `0,-1,-2,-4,-8,-16`; la formule est symbolique pour tout
  `t<=0`.
- Arithmétique : fractions exactes; divergence, momentum, Poisson, énergie
  locale et borne de vitesse ont un résidu maximal `0/1`.
- Pression : témoin BMO exact sur `R=1,2,4,8,16,32`; aucune quadrature.
- Graine, grille et pas de temps : sans objet.
- Portée : réfute un Liouville formulé pour les solutions faibles/adaptées à
  vitesse bornée sans jauge de pression. Elle ne réfute aucun théorème KNSS, qui
  emploie précisément la notion mild, ni un profil de blow-up déjà obtenu comme
  limite de solutions mild avec normalisation héritée.

## `BLOWUP-INHERITANCE-AUDIT-1` — non-composition des chaînes de zoom

### Question falsifiable et données

Le test demande si une **même** chaîne primaire auditée transmet simultanément

```text
équation NS visqueuse
+ intervalle ancien
+ formule mild
+ borne globale ponctuelle de vitesse
+ trace terminale nulle dans L²_loc
+ non-trivialité.
```

La matrice machine couvre quatre constructions, dans leurs versions figées :

- ESS 2003, zoom local sous borne globale `L-infinity_t L³_x` ;
- GKP `arXiv:1012.0145v3`, élément critique forward dans `L³` ;
- KNSS `arXiv:0709.3599v1`, zoom normalisé par le maximum ;
- Seregin `arXiv:2606.29468v1`, zoom Type II conditionnel de limite Euler.

Chaque cellule vaut `SOURCE`, `INFERENCE`, `NOT_PROVIDED`, `CONTRADICTED` ou
`NOT_APPLICABLE`. `NOT_PROVIDED` ne signifie jamais que la propriété est
impossible; seulement que cette arête ne peut pas être invoquée depuis la
source encodée.

### Lemme de raccord testé

Pour appliquer un théorème de rigidité de prémisses `H` à une chaîne de zoom
`C`, chaque propriété de `H` doit être une sortie de `C`, ou être ajoutée par un
lemme de raccord explicite. La réunion ensembliste de sorties provenant de
deux constructions différentes n'est pas une preuve de transmission.

Le garde-fou est élémentaire, mais son application est discriminante :

```text
ESS  fournit : trace L²_loc nulle + borne L-infinity_t L³_x + pression scindée;
KNSS fournit : ancienne mild + borne ponctuelle + |v(0,0)|=1;
GKP  fournit : mild L³ forward + trace S' au temps maximal;
Type II Seregin fournit : ancienne Euler dissipative pondérée.
```

La classe hybride « ancienne mild ponctuellement bornée, non triviale et de
trace `L²_loc` nulle » n'est donc la sortie d'aucune des quatre chaînes. Elle
n'apparaît qu'en réunissant artificiellement ESS et KNSS.

### Passe adverse intégrée

Le script vérifie exactement :

1. que chaque chaîne renseigne les mêmes treize propriétés ;
2. que chaque statut appartient au vocabulaire fermé ;
3. qu'une chaîne n'est pas simultanément visqueuse et inviscide ;
4. qu'elle ne porte pas simultanément une trace nulle et une normalisation
   terminale ponctuelle non nulle ;
5. les sorties uniques attendues des portes ESS, KNSS et Euler Type II ;
6. l'absence de chaîne unique et l'unique couverture minimale à deux chaînes
   pour la porte hybride.

`explicit_pressure_control` signifie une convergence ou décomposition de
pression effectivement suivie. La formule mild de KNSS élimine bien le mode
affine parasite, mais le lemme 6.1 ne transmet aucune suite de pressions : sa
cellule reste donc `NOT_PROVIDED`.

### Reproduction, précision et limites

- Commande :
  `python -B experiments/navier-stokes/blowup-inheritance-audit/inheritance_audit.py`.
- Arithmétique : inclusions d'ensembles finis exactes, aucun flottant.
- Discrétisation, pas de temps, graine, divergence numérique : sans objet.
- Critère de succès : `assertion_failure_count=0`.
- Résultat : aucune chaîne unique pour la porte hybride; couverture minimale
  artificielle `ESS_LOCAL_L3_ZOOM + KNSS_MAXIMUM_ZOOM`.
- Empreintes SHA-256 : enregistrées dans le claim et le checkpoint du cycle.
- Limite : la matrice certifie la cohérence du corpus encodé, pas l'exhaustivité
  de toute la littérature ni la fausseté intrinsèque du Liouville hybride. Une
  nouvelle source ou un lemme de raccord peut falsifier le résultat borné au
  corpus et doit alors modifier la matrice.

## `ANCIENT-ZERO-TRACE-RIGIDITY-AUDIT-1` — rigidité conditionnelle

- Question falsifiable : une ancienne mild KNSS, bornée sur tout
  `R³ x (-infinity,0)` et ayant une vraie trace nulle dans `D'`, satisfait-elle
  toutes les hypothèses d'une chaîne de rétro-unicité sans ajouter décroissance,
  énergie finie ou pression normalisée ?
- Équation : Navier–Stokes incompressible 3D standard, `nu=1`, force nulle,
  `R³`, sans frontière. La pression disparaît dans la route principale après
  passage à la vorticité; la formule mild conserve la jauge de Leray.
- Discrétisation : aucune grille spatiale ou temporelle. Le script vérifie un
  graphe fini de neuf obligations, les lois d'échelle et deux modules exacts
  avec `Fraction`.
- Constantes suivies : la proposition 4.1 de KNSS redémarrée à distance
  `h~M^-2` donne

  ```text
  ||nabla^k partial_t^l u||_infinity
    <= C_(k,l) M^(k+2l+1).
  ```

  Le script certifie l'exposant `k+2l+1` pour `0<=k<=3`, `0<=l<=2`. Pour les
  valeurs rationnelles de test `M=2`, `C=3`, il vérifie exactement le module
  temporel `24h`. Il vérifie aussi la queue d'Oseen
  `2 C_K M² sqrt(delta)` pour `delta=4^-j`; elle est divisée par deux à chaque
  raffinement.
- Test adverse : cinq familles sont confrontées aux sept propriétés requises.
  Le parasite accéléré échoue seulement à la mildness; la constante avec
  endpoint assigné et la limite maximum KNSS échouent seulement à la vraie
  trace nulle; les hautes fréquences perdent vorticité uniforme et identité de
  trajectoire; les translations à l'infini perdent le module mild global.
- Route principale : lissage KNSS, promotion locale de la trace, équation de
  vorticité, unicité rétrograde ESS sur bandes finies et demi-espaces
  translatés, Liouville harmonique, puis remarque 6.1 de KNSS.
- Contrôle : Lei–Yang–Yuan 2024 donne une route directe au niveau vitesse après
  extension mild à `t=0`. Trois anomalies de l'arXiv v1 sont consignées; cette
  route corroborante n'est pas l'unique support.
- Résultat : `assertion_failure_count=0`; aucune famille adverse n'ouvre toutes
  les portes. C'est un contrôle exact de la dérivation, pas une formalisation
  du théorème d'ESS ni une preuve numérique de PDE.
- Graine : sans objet. Sensibilité : rationnelle exacte, aucun flottant.
- Empreintes : obligations
  `d0d6da661fb195f8eb44caf013e0ffe430fbb31b575212172d07ceccf860e078`;
  script
  `5bd28f4e420744e3ebdda9b672afb6d6c050b906bec160476510709ba5588cf5`.
- Limite Clay : aucune extraction auditée ne transmet simultanément mildness,
  borne ponctuelle, trace nulle et non-trivialité au même objet. Le calcul ne
  change pas ce statut.

## `MAXIMUM-ZOOM-TRACE-COMMUTATOR-1` — trace du zoom par maximum

- Question falsifiable : pour les temps records KNSS, le défaut de raccord
  vient-il d'une non-commutation de `k->infinity` avec `s->0-` au temps-record,
  ou du déplacement du vrai temps terminal hors de cette horloge ?
- Équation : Navier–Stokes incompressible 3D standard sur `R³`, `nu=1`, force
  nulle, solution mild jusqu'à un temps maximal fini hypothétiquement singulier.
- Normalisation :

  ```text
  v_k(y,s)=M_k^-1 u(x_k+M_k^-1 y,t_k+M_k^-2 s),
  |v_k|<=gamma_k sur s<=0, gamma_k->1, |v_k(0,0)|=1.
  ```

  Ici `s=0` correspond à `t_k`, non à `T`; le temps physique `T` correspond à
  l'extrémité future mobile `B_k=M_k²(T-t_k)>0`.

- Discrétisation : aucune. Le script contrôle neuf obligations, le facteur
  `M_k²` dans les pairings, l'exposant `3-q` de la masse locale `L^q`, le
  module au temps-record et quatre contre-profils par ensembles finis et
  `Fraction`.
- Résultat analytique : les estimations KNSS redémarrées sur un intervalle
  passé commun donnent des bornes uniformes sur `nabla v_k` et `partial_s v_k`
  jusqu'à `s=0`. Les deux limites commutent donc dans `D'_local` au temps-record
  et leur valeur commune est non nulle. Cette conclusion n'est pas une trace
  au temps physique `T`.
- Concentration critique : si `||nabla v_k(0)||_infinity<=G`, alors

  ```text
  integral_(B_(1/(2GM_k))(x_k)) |u(x,t_k)|³ dx
    >= pi/(48G³).
  ```

  Par contraposée, la disparition uniforme de la masse `L³` sur les petites
  boules exclut ce blow-up. Ce n'est pas un nouveau critère : l'hypothèse
  d'équi-intégrabilité complète est plus forte que la condition uniforme à
  seuil fixe (23) de Constantin 2023, qui donne déjà le prolongement. Aucune de
  ces hypothèses n'est déduite de l'énergie.
- Test adverse exact : `u_k=e^(k²s)e_1`,
  `p_k=-k²e^(k²s)x_1` réalise une non-commutation avec résidu PDE, divergence,
  convection, Laplacien et Poisson tous nuls. Il échoue précisément à la
  mildness et au module temporel uniforme; sa pression affine n'est pas la
  jauge Leray/Riesz.
- Second contrôle : un cisaillement calorique mild sur `T³` conserve une
  oscillation au bord `s=0` seulement au prix d'une croissance rétrograde
  `e^(k²|s|)`; il perd toute borne uniforme sur un intervalle passé commun et
  n'est pas une extraction Clay sur `R³`.
- Résultat machine : `assertion_failure_count=0`; `pi` reste symbolique, aucun
  flottant. Aucun théorème de compacité ou de lissage n'est certifié par le
  script : il vérifie seulement la cohérence algébrique du chaînage.
- Empreintes : obligations
  `2fa2148a5ebb7b8fcce370655faca1df4b2c4a56990f99704481e54bf060d51e`;
  script
  `00334a12f7b51cb4f5a397e28f014230d2126cfd1cbbe8b2ffec90aa9c729451`.

## `DEGIORGI-UNIFORMITY-AUDIT-1` — énergie tronquée à un niveau

- Question falsifiable : la chaîne (23)–(40) conserve-t-elle un seuil fixe,
  un coefficient d'amortissement et les exposants logarithmiques uniformes,
  une fois la borne restreinte (22) admise ?
- Équation : NS incompressible 3D non forcé sur `R³`, `nu>0`, solution
  classique sur l'intervalle terminal; le script ne simule pas cette PDE.
- Entrées analytiques : borne faible uniforme `M`, déplétion restreinte
  `A/log(lambda/Lambda_*)`, Hölder–Lorentz, Sobolev–Lorentz, Sobolev et
  interpolation à constantes nommées.
- Discrétisation : aucune grille spatiale ou temporelle. Calculs par
  `Fraction` et registre symbolique d'exposants; aucun flottant.
- Résultat positif : absorption au seuil
  `Lambda_*exp(2C_H A S_L²/nu)`, coercivité
  `X>=lambda E/(S_6²M)`, ODE de coefficient
  `nu lambda/(2S_6²M)` et sortie
  `U_(2lambda)<=C lambda^-3/2 log^-3/2`.
- Tests adverses : seuils non uniformes, terme initial non nul, profil
  critique faible-`L^(3/2)` à énergie tronquée infinie, tente radiale
  saturant l'échelle et ratio dyadique `8/3>2`.
- Résidus : ODE, scaling et exposants exactement nuls; marge d'absorption
  rationnelle `1/5`, marge de Chebyshev `28/15`; douze contrôles passent.
- Sensibilité : le test dyadique montre que le facteur trois, pas deux,
  couvre le bord choisi; il ne certifie pas le commutateur complet.
- Commande :

  ```text
  python -B experiments/navier-stokes/degiorgi-uniformity/degiorgi_uniformity_audit.py
  ```

- Environnement : Python standard library; graine sans objet; aucun artefact
  binaire. Empreinte du script :
  `cbdca92eec11a287c31bb67d48dfeda339768863b2ccfa58b6cd8f66e3682721`.
- Limite : le calcul ne certifie ni Kato, ni les inégalités fonctionnelles,
  ni (8)–(22), ni la régularité ou le blow-up Clay.

## `ASYMPTOTIC-TRACE-CAUCHY-GATE-1` — trace asymptotique et état fini

- Question falsifiable : des branches qui ont toutes la trace zéro quand
  `tau->-infinity` donnent-elles plusieurs trajectoires depuis un même état
  posé à un temps fini ?
- Cadre NS analytique : incompressible 3D non forcé sur `R³`, `nu=1`. Pour une
  solution forte `u` et une solution de Leray–Hopf `v` de même donnée finie,
  `w=v-u` satisfait

  ```text
  (1/2)d||w||²_2/dt+||nabla w||²_2
    =-integral (w dot nabla)u dot w.
  ```

  Si `integral ||nabla u||_infinity dt<infinity`, Grönwall impose `w=0`.
  L'identité PDE est une dérivation papier; le script ne simule pas NS.
- Contre-modèle exact : pour `a=217/2000`,
  `b_A=aAq/(a+Aq)`, `q=exp(a tau)`, résout `b'=ab-b²`. Toutes les trajectoires
  ont la trace zéro, mais `b_A/q->A` et
  `A=ab/[q(a-b)]` à tout temps fini.
- Test adverse : `x'=2sqrt(x)` admet les solutions retardées
  `x_c(t)=(t-c)_+²` depuis le même état `x(0)=0`. Il montre que l'injectivité
  dépend bien de la classe localement lipschitzienne/forte.
- Dictionnaire HWY : une différence modale physique de la forme
  `(c-d)t^(a-1/2) v(x/sqrt(t))` a carré de norme `L²` proportionnel à
  `|c-d|² t^(2a+1/2)||v||²_2`; elle peut donc disparaître dans la trace alors
  que les états diffèrent pour chaque `t>0`.
- Résidus : ODE logistique, coefficient asymptotique, inverse à temps fini,
  différence de deux branches et solutions retardées tous exactement nuls;
  ordre strict sans échec, aucun flottant, aucune discrétisation.
- Limite : l'ODE n'est pas une réduction de NS. Le test ne borne pas le temps
  fort maximal et n'exclut aucune non-unicité faible après breakdown.
- Empreinte du script :
  `f78d90967e7546b5f4c04658f9537b70f3e7df8f7530e4b592734fbb6fb86375`.

## `COMMUTATOR-UNIFORMITY-AUDIT-1` — enveloppe annulaire exacte

- Question falsifiable : sous les seules enveloppes faible-`L^(3/2)` et
  `bmo_phi`, la dérive maximale des moyennes peut-elle faire dépasser à la
  queue intermédiaire l'ordre `phi(R)` revendiqué en (21) ?
- Équation : application conditionnelle à NS incompressible 3D non forcé sur
  `R³`, `nu>0`, solution classique avant `T*`; le script ne simule aucune PDE.
- Discrétisation : aucune grille spatiale ou temporelle. Sommes dyadiques et
  ledgers d'exposants en `fractions.Fraction`; balayages `T=6,...,512`
  accompagnés de bornes analytiques toutes échelles.
- Données adverses : incréments de moyennes tous positifs et au plafond
  `phi(2^jR)`; amplitude critique annulaire implicite `r_j^-2`; aucune graine.
- Résultats : facteur deux réfuté par `8/3`; facteur trois uniforme; budget
  géométrique `7/9`; maximum exact de la double somme `697/640`, marge
  `2389/1920` sous `7/3`; dérive sans `4^-k` non uniformément petite.
- Contrôles auxiliaires : interpolation `p_0=4/3`, `p_1=2`, `theta=1/3`;
  échec exact de l'extension naïve par zéro; invariance du ledger de scaling;
  queue macroscopique `R/R_*`.
- Résidus : huit contrôles passent, `assertion_failure_count=0`; aucun
  flottant, résidu d'égalité rationnelle nul dans les portes déclarées.
- Sensibilité : le pire balayé se trouve à `T=6`; la preuve analytique
  `phi(2^jR)<=3phi(R)` et la série géométrique couvrent tout `T>=6`.
- Commande :

  ```text
  python -B experiments/navier-stokes/commutator-uniformity/commutator_uniformity_audit.py
  ```

- Environnement : Python standard library; graine sans objet; aucun artefact
  binaire. Empreinte du script :
  `387898492a0dc370d6ca50aadbc18e7e524ebdc0d7326fe2347952cbce57ebbf`.
- Limite : le calcul ne certifie ni Jones, ni CRW, ni John–Nirenberg, ni le
  raccord tensoriel de Biot–Savart, ni l'existence d'une solution portant les
  hypothèses, ni une conclusion Clay.

## `ENDGAME-SYNCHRONIZATION-AUDIT-1` — temps, niveaux et rayons communs

- Question falsifiable : le raccord conditionnel `(49)->(58)` ferme-t-il avec
  un seul temps intérieur, un seuil uniforme, un rayon sparse construit et le
  même facteur analytique `M` dans les deux branches harmoniques ?
- Équation : application à NS incompressible 3D non forcé sur `R³`,
  `nu>0`, solution classique avant `T*`; aucune PDE n'est simulée.
- Discrétisation : aucune grille. Toutes les égalités sont calculées avec
  `fractions.Fraction`; les extensions toutes échelles sont des certificats
  algébriques affichés.
- Temps adverse : `T*=1,t=3/4,T_t=1/4` donne `s=T*` et résidu strict nul.
  La partition corrigée `t+tau_t>=T*` / `<T*` est exclusive et exhaustive.
- Paramètres harmoniques : cinq valeurs rationnelles de `h` vérifient
  `M=(2-h)/[2(1-h)]`, `theta=(1-h)/(2-h)`, `theta M=1/2` et coefficient un.
- Rayons : le témoin normalisé `r=1/600`, `rho=1/480` donne la marge cubée
  exacte `61/13824000000`; le seuil logarithmique vaut exactement douze dans
  ce test.
- Logarithme : le maintien de la même constante est réfuté par l'ordre strict
  `log(e+beta)>log(beta)`; le facteur huit est certifié sous
  `beta/Lambda_*>=3`.
- Scaling : amplitude `+1`, temps `-2`, rayons `-1`, volume `-3`, viscosité et
  logarithme normalisé invariants.
- Résidus : onze contrôles passent, `assertion_failure_count=0`; aucun
  flottant, aucune graine, aucun artefact binaire.
- Commande :

  ```text
  python -B experiments/navier-stokes/endgame-synchronization/endgame_synchronization_audit.py
  ```

- Environnement : bibliothèque standard Python. Empreinte du script :
  `41b27f8649977c8a2d564c80418678017eb5d409956c8f3c5e3eb9016f916a3b`.
- Limite : le calcul ne certifie ni le théorème d'analyticité, ni la queue de
  distribution uniforme, ni Ransford/Solynin, ni l'existence des temps
  d'échappement, ni une solution ou une conclusion Clay.

## `ACTIVE-CORE-BMO-OBSTRUCTION-1` — séparation de phases directionnelles

- Question falsifiable : une direction constante sur chaque composante d'un
  cœur actif admet-elle automatiquement une extension globale dont la norme
  logarithmique `bmo_phi` est uniforme à petite échelle ?
- Équation : application visée à NS incompressible 3D non forcé sur `R³`,
  `nu>0`; le script construit des données `C_c^infinity` divergence-free mais
  ne simule aucune trajectoire PDE.
- Discrétisation : aucune grille. Fractions exactes, suites symboliques et
  certificats analytiques toutes échelles; aucun flottant ni graine.
- Données adverses : deux boules de rayon `epsilon`, centrées en
  `+/-2epsilon e_1`, portent les directions `+e_3` et `-e_3` dans une boule
  commune de rayon `3epsilon`.
- Résultat : chaque cœur a une oscillation interne nulle, mais toute extension
  a une oscillation moyenne au moins `2/27` sur la boule commune. Aux rayons
  `r_n=exp(-n)`, le coût pondéré est au moins `2n/27`.
- Réalisation : potentiel compact lisse, vitesse égale à son rotationnel
  vectoriel, divergence exactement nulle et vorticité constante opposée dans
  les deux cœurs. La rotation solide non coupée a un résidu stationnaire nul;
  la pression et le résidu des coquilles coupées ne sont pas certifiés.
- Scaling : pour `A=epsilon^-2`, vitesse `epsilon^-1`, énergie
  `epsilon`, volume `epsilon³`, vorticité faible-`L^(3/2)` critique.
- Résidus : douze contrôles passent, `assertion_failure_count=0`; le cas
  symétrique du lemme optimal `4ab/(a+b)` est exact.
- Commande :

  ```text
  python -B experiments/navier-stokes/active-core-bmo/active_core_bmo_audit.py
  ```

- Environnement : bibliothèque standard Python; aucun artefact binaire.
  Empreinte du script :
  `df595323ec3630d25747548feb53295b9a849cef8aba1d6b22c101d4136644ae`.
- Limite : chaque `epsilon` définit une donnée initiale distincte. Le calcul ne
  produit ni trajectoire multi-échelle, ni pression globale dans les coquilles,
  ni régularité, ni blow-up Clay.

## `CRITICAL-PROFILE-ADMISSIBILITY-1` — profil homogène et rigidité log-BMO

- Question falsifiable : un profil vectoriel ponctuel exactement récurrent,
  de magnitude `r^-2`, peut-il satisfaire simultanément divergence nulle,
  faible-`L^(3/2)` global et direction `bmo_phi` ?
- Équation : raccord cinématique à NS incompressible 3D non forcé sur `R³`,
  `nu>0`. Le profil singulier ne résout pas l'évolution; ses doubles coupures
  sont seulement des données initiales `C_c^infinity` divergence-free.
- Profil :

  ```text
  u=(1/2)[a/r+(a.x)x/r^3+a cross x/r^2],
  omega=a cross x/r^3+(a.x)x/r^4,
  |omega|=r^-2.
  ```

- Discrétisation : aucune grille ni intégrateur temporel. Fractions exactes,
  identités vectorielles et différentiation automatique rationnelle sur 25
  points stéréographiques; aucune graine.
- Résultats : `div u=0`, `curl u=omega`, flux nul, distribution faible exacte
  et `MO_(B_r)(xi)>=2/3`. Aux rayons `exp(-N)`, le coût log-BMO est au moins
  `2N/3`.
- Lemme : toute direction exactement récurrente par dilatation et dans un
  `bmo_phi` avec `phi(r)->0` est constante; divergence nulle plus faible-
  `L^p` global force alors la vorticité à être nulle.
- Coupures : `A=-x cross u`, puis `u_(epsilon,R)=curl(chi A)`, conserve
  exactement la divergence. Énergie de coquille `O(epsilon)`, vorticité de
  coquille `O(epsilon^-2)` et norme critique uniforme; `L³` croît
  logarithmiquement.
- Pression : la pression de chaque donnée est recalculée par la projection de
  Leray globale. Aucun résidu stationnaire nul ni borne uniforme de pression
  n'est certifié.
- Résidus : seize contrôles passent, `assertion_failure_count=0`.
- Commande :

  ```text
  python -B experiments/navier-stokes/critical-profile-admissibility/critical_profile_admissibility_audit.py
  ```

- Empreinte du script :
  `95bbb128522b9c90437c05903ab86dd4f7cfc42f687218993ee9324ece5a0f85`.
- Limite : aucune exclusion des directions seulement asymptotiques ou
  rectifiées logarithmiquement, et aucune trajectoire de blow-up Clay.

## `LOG-RECTIFIED-PROFILE-1` — budget du premier harmonique sphérique

- Question falsifiable : un profil `W=r^-2 Omega(log(R*/r),theta)` peut-il
  rester solénoïdal, conserver une masse critique non dégénérée par coquille
  et rectifier sa direction vers un axe fixe au taux `O(1/|log r|)` ?
- Équation : porte cinématique `div W=0` nécessaire à NS incompressible 3D
  non forcé sur `R³`, `nu>0`; aucune trajectoire PDE n'est simulée.
- Discrétisation : aucune grille. Les polynômes en `s`, constantes de calottes,
  budgets de moment et contrôles d'échelle utilisent exclusivement
  `fractions.Fraction`; aucune graine ni flottant.
- Résultat : si `0<=Phi<=M`, si chaque bloc logarithmique de longueur `L`
  porte une masse moyenne `Phi^(3/2)` au moins `kappa`, et si la direction se
  rectifie vers `e` en moyenne pondérée, le moment de degré un perd au moins
  `kappa²/(3M²L)` par bloc alors que sa plage totale vaut au plus `M`.
- Test quantitatif : `M=2`, `kappa=1/2`, `L=3`, `delta*=1/864`; le 289e bloc
  forcerait une baisse `289/144>2`. Les résidus d'identité sont exactement
  nuls.
- Contre-profils : des calottes de mesure `2^(-3n)` et amplitude `2^(2n)`
  gardent leur masse critique mais détruisent la coercivité si la borne
  `L∞` angulaire est retirée. Le champ constant est solénoïdal mais perd la
  masse critique.
- Construction tranchante :

  ```text
  W=(s²-s)e+s(e dot theta)theta,
  u=(s²/2)e cross x
  ```

  est divergence-free, vérifie `curl u=W` et rectifie sa direction comme
  `1/s`, mais son facteur critique vaut `e^(-2s)s²` et dégénère. Le calcul
  certifie aussi `Delta W=r^-2[3e-(1+6s)mu theta]` et une non-linéarité
  `s³mu e cross theta`, donc pas de profil stationnaire NS.
- Commande :

  ```text
  python -B experiments/navier-stokes/log-rectified-profile/log_rectified_profile_audit.py
  ```

- Résidus : 62 contrôles, `assertion_failure_count=0`. Empreinte :
  `e5c24374ab40c7d52d12ddbd8c96e7aedee51a3c6b35154b90142c6c12781efe`.
- Limites : l'hypothèse faible-`L^(3/2)` globale seule ne donne pas la masse
  par coquille ni la borne de trace. Aucun calcul de pression, coupure
  corrigée, évolution temporelle ou raccord Clay n'est fourni.

## `WANDERING-AXIS-1` — budget mobile et oscillation centrée

- Question falsifiable : un axe `e=e(s)` peut-il recharger le moment
  solénoïdal d'un profil critique non dégénéré tout en gardant une oscillation
  directionnelle `O(1/s)` ?
- Équation : porte cinématique `div W=0` pour
  `W=r^-2 Omega(log(R_*/r),theta)`; application nécessaire à NS
  incompressible 3D non forcé sur `R³`, `nu>0`, sans trajectoire simulée.
- Discrétisation : aucune grille ni intégrateur. Fractions rationnelles exactes,
  aucune graine et aucun flottant.
- Résultat analytique : avec `Phi<=M`, masse de bloc `kappa`, longueur `L` et
  erreur pondérée `D`, tout axe absolument continu satisfait

  ```text
  N*2kappa²/(3M²L) <= M+(M/2) Var(e;[S,S+NL])+D.
  ```

  Si `D=o(NL)`, une survie exige une vitesse moyenne asymptotique au moins
  `4kappa²/(3M³L²)`.
- Rotation uniforme : sur toute boule centrée,
  `MO>=alpha²/[2(9+alpha²)]`. La rotation persistante échoue donc au taux
  log-BMO centré.
- Dérive lente : pour la phase `beta log(1+s)`, l'oscillation centrée est au
  plus `beta/[3(1+S)]`, mais la variation totale `beta log(1+T)` est
  sublinéaire et ne peut payer le budget.
- Paramètres exacts : `M=2`, `kappa=1/2`, `L=3`, baisse positive `1/72`,
  vitesse minimale `1/216`, oscillation uniforme au seuil au moins
  `1/839810`.
- Commande :

  ```text
  python -B experiments/navier-stokes/wandering-axis/wandering_axis_audit.py
  ```

- Résidus : 44 contrôles, `assertion_failure_count=0`. Empreinte :
  `23802f4b094aaccd020ab6d5d0ae9b136cc8cf70738b069c712fa6cddc432ba4`.
- Limites : les oscillations sont testées seulement sur les boules centrées;
  aucun `Omega` mobile complet, vitesse, pression, résidu NS, coupure ou passage
  au continuum n'est construit. Une grande variation peut provenir de petites
  boucles qui restent dans un cône fixe.

## `BMO-ACTIVE-AXIS-EXTRACTION-1` — moyenne active et axes dyadiques

- Question falsifiable : une direction log-BMO peut-elle garder des moyennes
  non normalisables malgré une amplitude critique bornée et une masse positive
  sur chaque coquille logarithmique ?
- Équation : porte cinématique `div W=0` pour
  `W=r^-2 Omega(log(R_*/r),theta)`; aucune trajectoire NS n'est simulée.
- Extension : `|zeta|<=1` partout et `zeta=Omega/|Omega|` sur `{Phi>0}`;
  l'extension par zéro est admise.
- Fraction active : pour des rayons de rapport `q`, `Phi<=M` et masse de bloc
  `kappa`, toute boule centrée contient une fraction active au moins
  `a_*=3q³kappa/M^(3/2)`.
- Axe : si l'oscillation de boule vaut `epsilon_k`, la moyenne `m_k` vérifie
  `|m_k|>=1-epsilon_k/a_*`; son normalisé `e_k` a une erreur moyenne au plus
  `(1+1/a_*)epsilon_k`.
- Cumul : sous `epsilon_k=O(1/k)`, les incréments des axes, leur variation et
  l'erreur directionnelle pondérée sont `O(log N)`. Le budget de moment du
  cycle 0023 impose au contraire une dépense linéaire et exclut le profil.
- Témoin exact : `q=1/2`, `M=1`, `kappa=1/4`, `B=1/100` donne
  `a_*=3/32`, facteur d'axe `35/3` et une contradiction certifiée à
  `N=1023` blocs.
- Test adverse : fractions actives `n^-3` et amplitudes `n²` gardent
  `<Phi^(3/2)>=1` mais font tendre moyenne et oscillation de l'extension par
  zéro vers zéro. La borne `Phi<=M` ne peut pas être supprimée.
- Commande :

  ```text
  python -B experiments/navier-stokes/bmo-axis-extraction/bmo_axis_extraction_audit.py
  ```

- Discrétisation : aucune grille, aucun flottant, aucune graine. Le script
  utilise `fractions.Fraction`, encadre `log 2` par série rationnelle et
  exécute 66 contrôles sans échec.
- Empreinte :
  `e2603081b46d4aab9599e9681eaf50cbc460df46e3b6d1c3d2383b0a71005e0e`.
- Limites : ni la borne de tranche, ni la masse de bloc, ni l'ansatz ne sont
  extraits d'une solution Clay. Aucune vitesse, pression, coupure, viscosité
  ou évolution n'est calculée.

## `CRITICAL-SOLENOIDAL-BLOB-TRAIN-1` — intermittence critique exacte

- Question falsifiable : l'échappatoire sparse d'amplitude non bornée peut-elle
  satisfaire divergence, curl, énergie finie et faible-`L^(3/2)` tout en
  conservant seulement une petite oscillation centrée ?
- Construction : `P=(1-t²)^4_+`,
  `U_0=(partial_y psi,-partial_x psi,0)`, `W_0=curl U_0`, puis blobs aux rayons
  `r_n=2^-n` et échelles `ell_n=r_n/(8n)`.
- Équation réellement contrôlée : identités statiques
  `div u=0`, `curl u=W`, `div W=0`; aucune discrétisation temporelle.
- Résultat positif : `u∈L²`, `W∈L¹∩L^(3/2,infinity)`, Biot–Savart sans mode
  harmonique `L²`, masse critique par bloc et amplitude angulaire `1024n²`.
- Test centré : pour l'extension par zéro,
  `MO_(B_(3r_n/2)(0))<1/(378n³)`.
- Test global : toute extension de la direction garde une oscillation au moins
  `2384963/22109421704515245593067520000` sur des boules internes de rayon
  `ell_n/2`; le log-BMO global échoue.
- Résidu : `curl[-Delta U_0+(U_0 dot nabla)U_0]` contient 1804 monômes non
  nuls. Une pression ne rend donc pas le profil stationnaire; le coût `L¹` du
  résidu non projeté est invariant par blob.
- Commande :

  ```text
  python -B experiments/navier-stokes/critical-blob-train/critical_blob_train_audit.py
  ```

- Environnement : Python 3.13.14, bibliothèque standard uniquement.
- Discrétisation et erreur : aucune grille, aucun flottant, aucune graine;
  arithmétique polynomiale rationnelle exacte, 104 contrôles, zéro échec.
- Empreinte :
  `129921806266636a46a5202bd0f2912491aaf557a02cda229c17ef80a529cb15`.
- Limites : le champ infini est irrégulier dès `t=0`, les normes fortes
  critiques divergent, la pression dynamique et l'évolution ne sont pas
  construites.

## `LORENTZ-CONE-COMPENSATION-1` — retour directionnel critique

- Question falsifiable : l'annulation vectorielle d'un curl compact et une
  borne faible-`L^(3/2)` imposent-elles une oscillation quantitative dès qu'une
  masse `L¹` non nulle reste dans un cône ?
- Équation : aucune évolution; porte statique `integral W=0`, satisfaite par
  `W=curl U` compact sous régularité suffisante.
- Lemme certifié après passe adverse : si `K` est la quasi-norme fixée,
  `G={xi·e>=alpha}`, `m=integral_G|W|` et `integral W=0`, alors

  ```text
  MO_D(zeta)>=2alpha^3 m^3/[27K^3|D|].
  ```

- Test sharp : `epsilon=n^-3`, amplitudes `n²/(n³-1)` et `-n²` donnent
  moyenne nulle, `K=1`, masse conique `1/n` et
  `MO=4n^-3(1-n^-3)`.
- Conclusion adverse : l'exposant cubique est optimal et la masse critique
  `L^(3/2)` peut rester non dégénérée tandis que la masse conique `L¹` tend
  vers zéro.
- Commande :

  ```text
  python -B experiments/navier-stokes/cone-compensation/cone_compensation_audit.py
  ```

- Environnement : Python 3.13.14, bibliothèque standard uniquement.
- Discrétisation : aucune grille, aucun flottant, aucune graine; 670 contrôles
  rationnels exacts, zéro échec et résidus algébriques nuls.
- Empreinte :
  `12eadf58f6bf5fdec9855527f58d9a7e6ba98650c3fd8fca78adbbbcfc1e1727`.
- Limites : le modèle sharp n'a ni géométrie spatiale, ni divergence, ni
  vitesse, ni pression. Une interface régulière entre les phases garde une
  oscillation locale égale à un; un corridor de zéros peut abaisser ce coût à
  l'ordre `1/log(R/h)`. Un lift collinéaire compact divergence-free est
  nécessairement nul, d'où le prochain test axisymétrique.

## `AXISYMMETRIC-RETURN-FLOW-BMO-GATE-1` — lift compact à aspect fixé

- Question falsifiable : un potentiel compact
  `U=chi(z)A_n(r)e_theta` peut-il spatialiser le compensateur rare du cycle
  0026 tout en gardant une direction log-BMO uniforme après concentration ?
- Équation simulée : aucune évolution. Les identités statiques exactes sont
  `W=curl U`, `div W=0`, `integral W=0`.
- Profil : phase axiale positive d'amplitude `n^-1`, retour de largeur `n^-3`
  et amplitude `3n^5/(8n^3+1)~(3/8)n²`; flux radial pondéré exactement nul.
- Contrôles critiques : quasi-norme faible-`L^(3/2)` uniformément minorée et
  majorée, masse forte critique négative non dégénérée, énergie normalisée
  `<=1/(3528n²)`.
- Porte BMO : dans une boule entièrement active de la calotte, la direction
  vaut `e_r` et

  ```text
  MO_B>=3/26624.
  ```

  Une concentration isotrope à aspect fixé échoue donc au log-BMO global.
- Résidu : la composante azimutale visqueuse porte cinq coefficients
  polynomiaux non nuls; aucune pression ne rend le champ stationnaire.
- Commande :

  ```text
  python -B experiments/navier-stokes/axisymmetric-return-flow/axisymmetric_return_flow_audit.py
  ```

- Environnement : Python 3.13.14, bibliothèque standard uniquement.
- Discrétisation : aucune grille, aucun flottant, aucune graine; 1251 contrôles
  rationnels exacts, zéro échec.
- Empreinte :
  `cec8bd74aa0b5b1b9943fbd149fe06c4ca5b045b9a337bdfef2821a18c5d29a9`.
- Variante équilibrée : avec calotte de largeur `delta=n^-3`, la quasi-norme
  critique normalisée est `<=1/6` et la moyenne parentale vérifie
  `4delta/27<=MO_D<=delta`. Une réalisation `C_c^infinity` séparée montre que
  cette loi cubique persiste dans la classe div–curl compacte, sans conclure
  au BMO sur toutes les boules.
- Limites : cutoff calculé seulement `C^4`, quasi-norme complète encadrée mais
  non calculée exactement, `||U||_3->0` pour la variante lisse, masquage
  non séparable et évolution temporelle ouverts.

## `TOROIDAL-LOG-BMO-VELOCITY-COLLAPSE-1` — fermeture azimutale mince

- Question falsifiable : `div omega=0` force-t-elle une zone de retour
  transverse de capacité polynomiale, même si la vorticité se ferme sur un
  tore mince ?
- Équation simulée : aucune évolution. Sur `T^3`,
  `omega_n=A_n beta(d_n^2/h_n^2)e_theta` et
  `u_hat_n(k)=i k cross omega_hat_n(k)/|k|^2` pour `k!=0`.
- Échelles : `R_n=2^-n`, `q_n=2^-2n`, `h_n=2^-n^2`,
  `A_n=(R_n h_n^2)^(-2/3)`.
- Résultat : divergence et moyenne nulles, normes faible et forte
  `L^(3/2)` d'ordre un, extension unitaire à log-BMO uniforme, mais

  ```text
  ||u_n||_3^3<=C[h_n/R_n+(h_n/R_n)^2] -> 0.
  ```

- Passe adverse : trois zones tubulaires et cancellation du noyau lointain;
  une dérivation indépendante confirme la puissance forte.
- Dynamique : pour un anneau unisigné sans swirl sur `R^3`, la diffusion
  active `omega_theta>0` près de l'axe à `t>0`, où l'oscillation moyenne de
  `e_theta` sur une boule axiale vaut un.
- Commande :

  ```text
  python -B experiments/navier-stokes/toroidal-log-bmo/toroidal_log_bmo_audit.py
  ```

- Environnement : Python 3.13.14, bibliothèque standard uniquement.
- Discrétisation : aucune grille, aucun flottant, aucune graine; 2207
  contrôles rationnels exacts, zéro échec.
- Empreinte :
  `0e1ea53d24e3c241c67e24a35bedbd81a16043cea580581ddc6c4f1f5729d274`.
- Limites : constantes tubulaires non optimisées; ni trajectoire, ni pression,
  ni passage calcul-continuum ne sont certifiés.

## `MOMENT-CORRECTED-TORI-GATE-1` — paire signée translatée

- Question falsifiable : annuler exactement l'impulsion d'une paire de tores
  peut-il préserver une vitesse critique non dégénérée ?
- Objet : deux copies `+/-` du tore 0028, de centres axiaux parallèles
  translatés de `+/-3R_n e_1`; aucune évolution.
- Échelles : `R_n=2^-n`, `q_n=2^-2n`, `h_n=2^-n^2`,
  `A_n=(R_n h_n^2)^(-2/3)`.
- Résultat positif : divergence et moyenne nulles, impulsion totale exactement
  nulle, faible-`L^(3/2)` uniforme, corridors log-BMO disjoints et rupture de
  l'axisymétrie globale.
- Résultat négatif : Stokes et la borne tubulaire donnent

  ```text
  c h_n/R_n<=||u_n||_3^3
            <=C[(h_n/R_n)+(h_n/R_n)^2] -> 0.
  ```

  Un moment quadrupolaire translaté reste non nul; la vitesse `R^3` a une queue
  d'ordre `|x|^-4` et n'est pas de Schwartz.
- Cardinal fixé : si chaque rapport `eta_(n,j)->0`, faible-Lorentz et
  Minkowski imposent encore `||sum_j u_(n,j)||_3->0`.
- Dynamique adverse : la variante coaxiale impaire a `MO=1` à temps positif
  sur les boules coupant le plan nodal; la variante transversale reste ouverte.
- Commande :

  ```text
  python -B experiments/navier-stokes/moment-corrected-tori/moment_corrected_tori_audit.py
  ```

- Environnement : Python 3.13.14, bibliothèque standard uniquement.
- Discrétisation : aucune grille, aucun flottant, aucune graine; 1842
  contrôles rationnels exacts, zéro échec.
- Empreinte :
  `527be8971f4bc5e2d7f22a3fb18a3d626b12cecc7f5dc71e39d40488b4a4a70c`.
- Limites : l'équivalent `L^3`, la queue multipolaire et le BMO all-ball sont
  analytiques, non interval-certified; aucune dynamique n'est calculée.

## `MANY-TORUS-POROSITY-GATE-1` — cardinal croissant localement packé

- Question falsifiable : un nombre `N_n->infinity` de tubes minces peut-il
  vaincre l'effondrement `L^3` lorsque les corridors log-BMO restent disjoints
  et localement packés ?
- Équation simulée : aucune évolution; reconstruction instantanée de
  Biot–Savart sur `R^3`, avec reste lisse séparé pour `T^3`.
- Échelles exactes :

  ```text
  ell_n=2^(-3n), q_n=2^(-9n), h_n=2^(-12n),
  N_n=2^(12n-12), A_n^3 S_n^2=1.
  ```

- Résultat adverse : `N_n h_n/ell_n=2^(3n-12)` diverge, mais la borne
  collective donne les cubes `2^(-21n+12)` (proche), `2^(-4n)` (lointain) et
  `2^(-15n-12)` (reste périodique), tous convergents vers zéro.
- Discrétisation : aucune grille, aucun flottant, aucune graine; arithmétique
  `fractions.Fraction` et 776 contrôles dyadiques exacts.
- Commande :

  ```text
  python -B experiments/navier-stokes/many-torus-porosity/many_torus_porosity_audit.py
  ```

- Environnement : Python 3.13.14, bibliothèque standard uniquement.
- Résidu certifié : zéro échec; toutes les identités dyadiques vérifiées sont
  exactes. Empreinte :
  `821c0e7e442698397c5d426fefca42ca12e5949f904e3ce243d3277377ecbbae`.
- Limites : constantes tubulaires et all-ball non interval-certified;
  paramètres hétérogènes, pression, stretching, temps positif et passage
  calcul-continuum non traités. La réalisation coaxiale est axisymétrique sans
  swirl.

## `COMPACT-SWIRL-ASPECT-GATE-1` — budget critique anisotrope

- Question falsifiable : un rapport d'aspect toroïdal croissant peut-il
  neutraliser la boule directionnelle active tout en conservant les gates
  faible-`L^3` de la vitesse et faible-`L^(3/2)` de la vorticité ?
- Équation simulée : aucune; donnée statique
  `U=V(R/r)eta((r-R)/a)chi(z/b)e_theta` sur `R^3`.
- Discrétisation : aucune grille, aucun flottant, aucune graine; arithmétique
  `fractions.Fraction`.
- Quantités auditées : cubes `V^3Rab`, `V^3R^2b^2/a` et
  `V^3R^2a^2/b`, ainsi que leur invariance d'échelle.
- Famille adverse : `R_n=2^-n`, `a_n=b_n=2^-2n`. Sous gate vitesse un, les
  deux coûts vorticité valent `2^n`; sous coûts vorticité un, le gate vitesse
  vaut `2^-n`.
- Commande :

  ```text
  python -B experiments/navier-stokes/compact-swirl-aspect/compact_swirl_aspect_audit.py
  ```

- Environnement : Python 3.13.14, bibliothèque standard uniquement.
- Résidu certifié : zéro échec sur 37 214 contrôles rationnels exacts.
  Empreinte :
  `e392e3570e4de6f85bcb5f91a7eef6b36a1ed22c55bf8c483a918319b9a848e4`.
- Limites : constantes des profils et lemme all-ball analytiques, non
  interval-certified; superpositions non séparables, pression et évolution
  Navier–Stokes non traitées.

## `TWO-LAYER-PURE-SWIRL-SUPPORT-GATE-1` — collapse de support non séparable

- Question falsifiable : deux couches compactes signées et décalées peuvent-elles
  vaincre le facteur critique d'aire méridienne par annulation pointwise ?
- Équation simulée : aucune; cinématique statique
  `U=(R/r)F(r,z)e_theta`, `curl U=(R/r)nabla_perp F` sur `R3`.
- Discrétisation : fonctions continues P1 sur triangulations rationnelles du
  carré `[-2,2]^2`, maillages `8,12,16,20`; 384 masques à deux couches.
- Données : six coefficients signés, quatre centres et quatre couples de
  largeurs; aucune graine aléatoire.
- Précision : `fractions.Fraction`; les modules de gradient sont comparés par
  leurs carrés, sans racine ni flottant.
- Quantités certifiées : aire des triangles actifs, maximum nodal, fonction de
  distribution exacte du gradient P1 et loi dyadique du quotient.
- Famille : `R_n=2^-n`, `h_n=2^-2n`, `2<=n<=30`; le pire quotient carré est
  divisé exactement par quatre lorsque `n` augmente de un.
- Commande :

  ```text
  python -B experiments/navier-stokes/two-layer-pure-swirl/two_layer_pure_swirl_audit.py
  ```

- Environnement : Python 3.13.14, bibliothèque standard uniquement.
- Résidu certifié : 272 726 contrôles exacts, zéro échec; pire quotient de
  forme carré `4212353969604/482173039025<9`.
- Empreinte :
  `597dc2e2828df34d836556c5419904d39e6ee240aa93b353a49683699ae40443`.
- Limites : énumération finie, majorant `L-infinity` pour la vitesse, aucune
  certification de HLS continuum, de BMO, de pression ou d'évolution.

## `BOUNDED-CROSS-SECTION-DIRECTION-GATE-1` — plateaux et retours rares

- Question falsifiable : une coque directionnelle rare, un compensateur
  antipodal ou des cellules axialement séparées peuvent-ils réduire le BMO
  sans payer l'un des deux endpoints critiques ?
- Équation simulée : aucune; ledger statique de
  `U=(R/r)F e_theta`, `W=curl U`.
- Discrétisation : aucune grille; identités de cubes de quasi-normes et modèles
  à volumes finis calculés en `fractions.Fraction`.
- Familles : 32 rayons dyadiques et 12 couples de cubes de normes; 276 coques
  de plateau; 29 retours rares; `1<=N<=256` cellules séparées.
- Identités certifiées :

  ```text
  K_f^6/(K_g^3K_w^3)=(K_u^3/K_w^3)^2,
  K_w^3/K_u^3=R/delta,
  K_w^3(rare)=(1-epsilon)^3/epsilon,
  K_w^3/K_u^3=N pour N cellules égales.
  ```

- Amplitudes dyadiques : les deux endpoints sont exactement dominés par la
  première cellule; la séparation seule n'efface pas un bloc local.
- Commande :

  ```text
  python -B experiments/navier-stokes/bounded-cross-section-direction/bounded_cross_section_direction_audit.py
  ```

- Environnement : Python 3.13.14, bibliothèque standard, aucune graine.
- Résidu certifié : 2 884 contrôles rationnels exacts, zéro échec.
- Empreinte :
  `4759238f59a46f64f0a547881f8aeb86ca6755ceea06c4a1728648db57847f8f`.
- Limites : constantes de profil et cône non certifiées; aucun supremum BMO
  continu, aucune cellule hétérogène optimisée, aucune PDE en temps.

## `HETEROGENEOUS-CELL-SELECTION-1` — distributions et registre BV

- Question falsifiable : les deux endpoints globaux sélectionnent-ils une
  même cellule, et quel registre géométrique est indispensable ?
- Équation simulée : aucune; ledger statique d'atomes disjoints et modèle de
  fermeture `B_jq_j=A_jv_j^(2/3)`.
- Discrétisation : aucune grille; fonctions de distribution finies triées et
  calculées avec `fractions.Fraction`.
- Contre-exemple : quatre lignes fermées `N=8^n` et deux lignes entièrement
  matérialisées; `K_u^3=1`, `K_w^3<=64/49`, rapport local cubique `8^-n`.
- Registre : 1 152 familles hétérogènes, 9 792 cellules, amplitudes et tailles
  variables. Identités certifiées :

  ```text
  B_jq_j=A_jv_j^(2/3),
  epsilon>=K_u^2/(3K_w),
  max_j(K_(u,j)/K_(w,j))>=K_u^2/(3K_w^2).
  ```

- Commande :

  ```text
  python -B experiments/navier-stokes/heterogeneous-cell-selection/heterogeneous_cell_selection_audit.py
  ```

- Environnement : Python 3.13.14, bibliothèque standard, aucune graine.
- Résidu certifié : 31 746 assertions rationnelles exactes, zéro échec.
- Empreinte :
  `d918ff7ec5e200d388cde1d3ed5230ebdd4535bc65fc3b94a2c7ac21c0962763`.
- Limites : le contre-exemple n'est pas curl-compatible; le calcul encode mais
  ne prouve pas coaire/BV; chevauchement, pression, diffusion et temps absents.

## `COMMON-LEVEL-HALO-SELECTION-1` — bande commune et queues longues

- Question falsifiable : une queue pure-swirl de volume support arbitraire
  peut-elle détruire la sélection d'une même cellule aux deux endpoints ?
- Équation calculée : aucune évolution; ledger exact pour
  `U_j=(R_j/r)F_j e_theta` et
  `W_j=(R_j/r)(-partial_zF_j e_r+partial_rF_j e_z)`.
- Discrétisation : aucune grille; volumes de superniveaux finis et toutes les
  racines supprimées par cubage en arithmétique `fractions.Fraction`.
- Ledger : 1 536 familles, 12 288 superniveaux signés et constante
  isopérimétrique normalisée `C_I=1`. Il vérifie exactement

  ```text
  epsilon^3 324^3 K_w^3>=K_u^6.
  ```

- Contre-profil cœur–queue : amplitudes `2^-k`, volumes `8^k`, profondeur
  `4..24`; volume support/coeur maximal
  `5396990266136737387081`, mais `1<=K_u^3<8/7` et budget de curl forcé non
  nul au niveau commun.
- Commande :

  ```text
  python -B experiments/navier-stokes/common-level-halo-selection/common_level_halo_audit.py
  ```

- Environnement : Python 3.13.14, bibliothèque standard, aucune graine.
- Résidu certifié : 10 837 assertions rationnelles exactes, zéro échec,
  résidu algébrique maximal zéro.
- Empreinte :
  `b197d3b45af0f034c09c91d4b7bb6d3be55293ab1f458ec769c250c8998490f8`.
- Limites : coaire et isopérimétrie sont des entrées analytiques; le calcul ne
  certifie ni diamètre de la bande, ni chevauchement, pression, temps ou PDE.
