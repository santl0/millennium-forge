# Graphe de dépendances — Navier–Stokes 3D

Mise à jour : 2026-08-14. Les nœuds `C-*` renvoient aux affirmations JSON du
dépôt. Une arête « classique » peut rester seulement `SOURCE_VERIFIED` dans le
laboratoire : ce statut vérifie la source, pas la preuve ligne à ligne.

## Graphe principal

```text
[Donnée lisse Clay]
   -- classique, sourcé --> [Solution forte locale unique]
   -- classique, sourcé --> [Temps maximal T_*]

[T_* fini]
   -- classique, conditionnel --> [Explosion de toute norme de prolongement]
   -- ESS 2003 --> [||u||_{L∞_t L³_x} non bornée]

[Séquence de concentration]
   -- conditionnel: borne critique + compacité --> [Solution ancienne non nulle]
   -- heuristique sous énergie seule -----------> [Mesure de défaut / cascade]

[Solution ancienne non nulle]
   -- manquant en classe générale --> [Contradiction de Liouville]
   -- sourcé sous classes spéciales --> [Contradiction partielle]

[Contradiction de toute concentration]
   -- classique --> [Prolongement au-delà de T_*]
   -- itération --> [Régularité globale Clay]

[Profil singulier ou solution faible non unique]
   -- MANQUANT: donnée lisse + branche classique exclue --> [Breakdown Clay]
```

## Registre des arêtes

| De | Vers | Statut | Source ou condition | Trou suivi |
|---|---|---|---|---|
| donnée lisse divergence-free | solution locale | classique et sourcée | théorie mild/forte | constantes de durée dépendent de normes surcritiques |
| solution locale | temps maximal | classique et sourcée | alternative de prolongement | aucune borne uniforme en données arbitraires |
| `T_*<infinity` | divergence `L∞L³` | classique et sourcée | Escauriaza–Seregin–Šverák | ne borne pas `L³` |
| borne Prodi–Serrin | prolongement | classique et sourcée | Prodi, Serrin | hypothèse conditionnelle |
| borne critique + minimalité | profil compact modulo symétries | conditionnelle | décomposition de profils | dichotomie et pression |
| suite de blow-up sous énergie seule | solution ancienne | manquante | — | une puissance d'échelle et compacité forte |
| tension pondérée `sup_n integral |U_n|²|y|^-4` | petite pression lointaine centrée | dérivation locale, `COMPUTATION_ONLY` | pression proche encore incontrôlée |
| borne critique uniforme `L³` | tension pondérée `A^-3` | Hölder à constante explicite, passe adverse; compatible ESS/GKP | la borne `L³` n'est pas issue de l'énergie |
| norme `L²` physique bornée | tension pondérée après zoom | réfutée | contre-paquets lisses multi-échelles | structure dynamique ou borne critique nécessaire |
| convergence faible d'une trace mobile + énergie | convergence du produit et de la pression | réfutée | solution NS oscillatoire exacte, `t_N~N^-2` | équicontinuité ou compacité forte de trace nécessaire |
| énergie Leray–Hopf | module `C_t^(1/4)H^-1` | dérivation locale, `COMPUTATION_ONLY` | équation dans `H^-1` + Gagliardo–Nirenberg | facteur d'échelle `lambda^-1`, donc supercritique au zoom |
| énergie Leray–Hopf | module critique `C_t^(1/4)L²` ou `C_t^(3/4)dot H^-1` | réfutée | famille oscillatoire exacte | les quotients croissent comme `N^(1/2)` |
| donnée initiale forte `L²` + module uniforme `C_t^(1/4)L²` | trace mobile forte `L²` | dérivation conditionnelle | inégalité triangulaire à constante 1 | prémisse critique non issue de l'énergie |
| données initiales précompactes `L²` + énergie + module `V'` | trace initiale uniforme forte `L²` | dérivation locale, `COMPUTATION_ONLY` | projection Fourier finie + inégalité d'énergie | les tranches rescalées de blow-up ne sont pas précompactes a priori |
| convergence forte `L³(T³)` | convergence forte produit/pression en `L^(3/2)` | dérivation locale, `COMPUTATION_ONLY` | Hölder + Riesz périodique | obtenir `L³` fort sans supposer le critère critique recherché |
| convergence forte espace-temps `L²` + borne `L^(10/3)` | convergence forte locale `L³` | conditionnelle | interpolation sur cylindres fixés | ne donne pas automatiquement une trace forte à `t_n->0` |
| limite locale de vitesse | limite de pression | conditionnelle | Calderón–Zygmund + tension pondérée | pression proche: convergence forte; queue: tension uniforme |
| profil rétrograde `L³` | trivialité | classique et sourcée | Nečas–Růžička–Šverák | ne couvre pas Type II/DSS général |
| solution ancienne mild à vitesse bornée générale 3D | trivialité | manquante | Liouville partiel seulement | rigidité |
| solution ancienne faible/adaptée à vitesse bornée + trace terminale nulle | trivialité | réfutée | solution parasite `u=b(t)`, pression affine | mildness ou jauge globale indispensable |
| solution ancienne spatialement constante + mildness | constance temporelle | classique et sourcée | KNSS remarque 6.1 | ne traite aucun mode spatial non nul |
| pression ancienne `BMO_x` modulo constantes | exclusion du mode affine parasite | dérivation locale, `COMPUTATION_ONLY` | oscillation moyenne `R/2` | ne donne pas la rigidité des modes non constants |
| zoom de blow-up KNSS borné | solution ancienne mild non nulle | classique et sourcée sous hypothèses KNSS | compacité mild + normalisation ponctuelle | pas disponible pour tout blow-up Clay général |
| zoom KNSS par temps records | valeur locale non nulle au temps-record redimensionné `s=0` + concentration `L³` critique | dérivation laboratoire, `COMPUTATION_ONLY` | lissage KNSS uniforme : limites `k/s` commutables à `t_k`, `|v(0,0)|=1`, masse `>=pi/(48G³)` | le temps physique `T` est l'extrémité mobile `B_k`; aucune non-concentration issue de l'énergie |
| non-concentration uniforme `lim_(r->0)sup_(t,x) integral_(B_r(x))|u|³=0` | absence de temps maximal fini dans la classe mild KNSS | dérivation conditionnelle, déjà couverte par le critère plus faible de Constantin 2023 | contraposée de la concentration du zoom maximum + condition (23) publiée | prémisse critique non démontrée pour toute donnée Clay |
| zoom ESS sous `L∞_tL³_x` | solution NS éternelle, adaptée, non triviale, trace `L²_loc` nulle | classique et sourcée | ESS, convergence forte locale et pression scindée | aucune borne ponctuelle globale; la borne `L³` est déjà critique |
| élément critique GKP sous `A_c<infinity` | solution mild forward, trace terminale nulle dans `S'` | classique et sourcée | GKP théorèmes 5–7 | ni objet ancien ni borne ponctuelle globale |
| ancienne mild bornée + vraie trace terminale nulle dans `D'` | trivialité par unicité rétrograde | dérivation laboratoire, `COMPUTATION_ONLY`, passe adverse | lissage KNSS + vorticité + ESS sur bandes finies + Liouville harmonique + jauge mild; Lei–Yang–Yuan publié en contrôle | aucune chaîne auditée ne transmet toutes les prémisses au même objet |
| réunion des sorties ESS et KNSS | ancienne mild bornée + trace nulle | non transférable | `BLOWUP-INHERITANCE-AUDIT-1` : propriétés portées par deux objets différents | lemme de raccord absent |
| zoom Type II d'échelle Euler | ancienne dissipative Euler non triviale | conditionnel et sourcé | Seregin `2507.08733v2`, `2606.29468v1`, `2402.13229v3` | un Liouville Navier–Stokes ne s'applique pas à l'équation limite |
| alignement critique de vorticité | régularité | conditionnelle, sourcée | Constantin–Fefferman | alignement non déduit de NS |
| cohérence locale dans un patch + énergie/enstrophie/palinstrophie/hélicité | signe ou petite déplétion ponctuelle de `omega·S omega` | réfutée | paire Fourier exacte `a=+-1`, `FAIL-NS-0016` | strain lointain et quantificateurs globaux absents |
| cohérence high–high uniforme en temps sur `R³` | régularité | conditionnelle, sourcée | Constantin–Fefferman; Beirão da Veiga–Berselli | module non déduit de la dynamique générale |
| cohérence locale sur cylindre | absorption du stretching localisé | conditionnelle, sourcée | Grujić 2009 | commutateurs de cutoff et queue extérieure à conserver |
| majorant global `|V|≤B` | 3D `delta`-sparseness au rayon construit `r=[B/(delta|B_1|)]^(1/3)` | dérivation exacte, `COMPUTATION_ONLY` | mesure globale et volume de la boule; rayon uniforme en centre | les rayons plus petits ne sont pas garantis; majorant PDE amont requis |
| 3D `delta`-sparseness dans `B_r(x_0)` | 1D `delta^(1/3)`-sparseness sur une droite centrale au même rayon | dérivation exacte sharp, sources publiées `0065`–`0066`, passe adverse | formule polaire signée + réarrangement radial; boule centrale extrémale | aucun trou géométrique; direction dépendante de `x_0` |
| `omega∈L∞_tL^(3/2,infinity)` + direction globale uniforme `bmo_phi` + raccord tensoriel | borne localisée de commutateur (22) | conditionnelle, dérivation exacte après corrections, `COMPUTATION_ONLY` | `NS-LOCALIZED-LOG-COMMUTATOR`, Jones/CRW/John–Nirenberg, cycle 0018 | l'hypothèse globale de direction n'est pas produite par NS; zéros et multicœurs non raccordés |
| borne uniforme de commutateur (22) + solution classique pré-singulière + `omega∈L∞_tL^(3/2,infinity)` | distribution de vorticité (40) à seuil uniforme | conditionnelle, chaîne énergétique confirmée après révision | `NS-DEGIORGI-ONE-LEVEL-TRANSFER`, cycle 0017 | seuil exponentiel non absolu; logarithme et intervalle à normaliser |
| faible-`L^(3/2)` de la vorticité seulement | tronqué `(omega-lambda)_+∈H¹` | réfutée | `NS-WEAK-L32-TRUNCATION-H1`, profil `|x|^-2` | la régularité classique pré-singulière doit justifier l'énergie |
| estimation de stretching seulement sur `(T*−epsilon,T*)` | absorption sur tout `(0,T*)` | réfutée | `NS-DEGIORGI-ENTIRE-INTERVAL-ABSORPTION` | restreindre l'ODE à l'intervalle terminal suffit |
| distribution de vorticité (40) + contrôle global faible + Biot–Savart/O'Neil normalisé | enveloppe de réarrangée de vitesse (47) | dérivation exacte après correction, `COMPUTATION_ONLY` | `NS-SRC-0059`, `0067`, `0068`, `ONEIL-TRANSFER-1` | exige seuil uniforme, queue globale et mode harmonique fixé ou borné |
| reste positif de (46) | terme `O(1)` quand `v->0` | réfutée | `R(exp(-3n))>=3n/256`, `FAIL-NS-0018` | vrai ordre `9v^-1/3log^-2(e/v)`, absorbable mais divergent |
| `u∈L∞`, `div u=0`, `omega=curl u` | `u=B[omega]` sans mode harmonique | réfutée | champ constant exact, `FAIL-NS-0019` | imposer décroissance/intégrabilité ou écrire `u=B[omega]+h` |
| enveloppe uniforme de réarrangée de vitesse (47) | majorant quantitatif de distribution de vitesse (49) | dérivation exacte après correction, `COMPUTATION_ONLY` | pseudo-inverse strict, bootstrap logarithmique, plateaux adverses, `REARRANGEMENT-INVERSION-1` | exige un cutoff `v_0` uniforme; ne donne aucun profil ponctuel radial |
| identité terminale `lambda=f*(mu_f(lambda))` pour toute fonction mesurable | égalité de l'équation (48) sur tous les niveaux | réfutée | profil exact à deux plateaux, `FAIL-NS-0017` | remplacer par `v<mu_f(lambda) -> f*(v)>lambda` |
| queue uniforme (49) + analyticité mild locale + mesure harmonique | exclusion d'un premier temps singulier dans ce scénario | conditionnelle, dérivation exacte après corrections, `COMPUTATION_ONLY` | `NS-CONDITIONAL-ENDGAME-SYNCHRONIZATION`, Grujić 2013, Guberović, Solynin et Ransford, cycle 0019 | temps garanti et dichotomie requis; ne produit pas (49) depuis une donnée Clay générale |
| `s=t+T_t` avec `T_t` durée maximale | temps intérieur `s∈(t,T*)` | réfutée | `NS-ENDGAME-MAXIMAL-TIME-SELECTION`, résidu exact `T*−s=0` | remplacer par `tau_t` garanti et séparer prolongement direct / branche intérieure |
| cohérence de direction seulement sur chaque cœur `{omega>lambda}` | direction globale uniforme `bmo_phi` | réfutée sans contrôle inter-composantes | `NS-ACTIVE-CORE-BMO-EXTENSION`, cycle 0020 : deux cœurs antipodaux de fractions fixes imposent un coût logarithmique divergent | ajouter un packing de phases `4ab/(a+b)=O(phi(r))`, une convention aux zéros et une sélection mesurable en temps |
| phases directionnelles `+e/-e` de fractions `a,b` dans un domaine test | `MO_D(xi)>=4ab/(a+b)` | dérivation exacte optimale, `COMPUTATION_ONLY` | `NS-BMO-PHASE-SEPARATION-BOUND`, cycle 0020 | lemme géométrique seulement; la dynamique NS ne fournit pas `a,b` |
| identité `omega=|omega|xi` sans convention sur `{omega=0}` | appartenance intrinsèque de `xi` à `bmo_phi` | réfutée | `NS-VORTICITY-DIRECTION-ZERO-CANONICITY`, solution nulle et deux extensions unitaires | formuler une convention ou l'existence d'une extension espace-temps mesurable |
| magnitude scalaire `|W|=r^-2 Phi` | vorticité vectorielle globale admissible | manquante et fausse sans contraintes angulaires | cycle 0021 : `div_(S²)Omega_T=0` et flux radial nul sont nécessaires; `e/r²` et `theta/r²` séparent les deux défauts | coupler explicitement magnitude et direction avant Biot–Savart |
| magnitude `r^-2` + `div W=0` + faible-`L^(3/2)` | direction globale `bmo_phi` | réfutée | `NS-CRITICAL-MAGNITUDE-IMPLIES-BMO`, profil exact du cycle 0021 | l'hypothèse directionnelle reste indépendante |
| champ vectoriel critique exactement récurrent par dilatation + direction `bmo_phi` | profil solénoïdal non nul faible-`L^p` | exclu, `COMPUTATION_ONLY` | `NS-DILATION-RECURRENT-BMO-RIGIDITY` | ne couvre ni récurrence de la seule magnitude, ni profil asymptotique, ni rectification logarithmique |
| amplitude critique bornée + masse `L^(3/2)` non dégénérée par bloc + direction rectifiée vers un axe fixe | profil log-radial solénoïdal jusqu'au centre | exclu, `COMPUTATION_ONLY` | `NS-LOG-RECTIFIED-SOLENOIDAL-OBSTRUCTION`, budget du premier harmonique, cycle 0022 | faible-Lorentz seul ne donne ni borne de tranche ni masse par bloc; axe errant hors champ |
| mêmes bornes + axe mobile absolument continu + erreur directionnelle pondérée sublinéaire | profil solénoïdal avec variation d'axe sublinéaire | exclu, `COMPUTATION_ONLY` | `NS-WANDERING-AXIS-MOMENT-BUDGET`, cycle 0023 : recharge au plus `(M/2)Var(e)` | axe non canonique, multicœurs, intermittence angulaire et centre mobile hors champ |
| amplitude critique bornée + masse par bloc + même extension à oscillation centrée `O(1/k)` | axe mobile à variation et erreur `O(log N)`, puis exclusion du profil | dérivation exacte, `COMPUTATION_ONLY` | `NS-BMO-ACTIVE-AXIS-EXTRACTION`, cycle 0024 | aucune de ces prémisses n'est héritée d'un blow-up général; amplitude non bornée hors champ |
| train de blobs critiques de forme fixe + énergie + faible-`L^(3/2)` + masse par bloc | direction globale `bmo_phi` | réfutée | `NS-CRITICAL-BLOB-TRAIN-BMO-GATE`, cycle 0025 : tests centrés `O(n^-3)` mais oscillation interne uniforme sur des boules de rayon `ell_n/2` | une forme interne dépendant de l'échelle et asymptotiquement plate reste ouverte |
| moyenne vectorielle nulle + faible-`L^(3/2)` + masse `L¹` dans un cône | oscillation directionnelle `MO_D>=2alpha^3m^3/(27K^3|D|)` | dérivation exacte renforcée par passe adverse, `COMPUTATION_ONLY` | `NS-LORENTZ-CONE-COMPENSATION`, cycle 0026 | la masse critique totale ne minore pas la masse conique; modèle sharp non spatial |
| lift séparable `U=chi(z)A(r)e_theta` + corridor de flux non nul | boule active de direction `e_r` avec `MO>=3w/[2048(R+w)]` | dérivation exacte, `COMPUTATION_ONLY` | `NS-AXISYMMETRIC-RETURN-FLOW-BMO-GATE`, cycle 0027 | la borne décroît comme l'inverse de l'aspect; elle ne traite pas `R_n/w_n->infinity` |
| moyenne nulle + support compact + div–curl axisymétrique | amélioration de l'exposant cubique de l'oscillation parentale | réfutée | `NS-AXISYMMETRIC-DIVCURL-CUBIC-SHARPNESS`, cycle 0027 : `K~1`, `m~epsilon^(1/3)`, `MO_D~epsilon` | ne calcule pas le supremum BMO sur toutes les boules; `||U||_3->0` |
| solution forte non triviale à temps positif | conventions BMO distinctes par valeurs sur `{omega=0}` | réfutée dans cette classe | analyticité `NS-SRC-0092`–`0093`; lieu nodal commun nul en mesure | ne contrôle ni phase près des zéros, ni solution faible terminale, ni superniveau actif |
| rotation radiale uniforme en profondeur logarithmique | direction globale `bmo_(1/|log r|)` | réfutée déjà sur les boules centrées | variance exacte `alpha²/(9+alpha²)`, `WANDERING-AXIS-1` | ne traite pas des chemins irréguliers ou multivalués |
| toute forte vorticité confinée uniformément dans un double cône fixe | régularité intérieure d'une solution faible adaptée | `SOURCE_VERIFIED`, prépublication v1 | `NS-LRT-DOUBLE-CONE-REGULARITY`, Lei–Ren–Tian `2501.08976v1` | preuve non reproduite; le cône n'est pas produit depuis Clay |
| direction dans `bmo_(1/|log r|)` | axe fixe ou double cône uniforme sur tous les grands niveaux | manquante | séparation multicœur et moyenne contre contrôle ponctuel | un axe errant ou des phases multiples peuvent échapper à tout cône fixe |
| profil solénoïdal homogène + coupure radiale scalaire | profil tronqué solénoïdal avec erreur critique petite | réfutée | défaut exact `Var(chi)||Omega_r||_L1`, cycle 0021 | correcteur sphérique explicite requis; sa taille critique ne décroît pas |
| hélicité globale nulle | petit flux instantané universel | réfutée | contre-triade exacte | pas de positivité modale |
| profil Euler IA | profil NS perturbatif | réfutée pour l'ansatz mono-échelle `lambda>-1/2` | rapport visqueux exact | viscosité dominante |
| donnée homogène `-1` non unique | donnée compacte énergétique singulière non unique | source vérifiée, CAP non reproduite | Hou–Wang–Yang v2; cutoff extérieur, gain `R^-1/8` pour `p=4` | le coeur `1/r` est conservé |
| donnée compacte singulière `1/r` | famille de données Clay lisses divergence-free convergeant en `L²` | classique et dérivé | convolution par mollificateur radial | aucune convergence forte critique |
| convergence `L²` + borne uniforme `L^{3,infinity}` de cutoffs intérieurs | compacité forte `L³` | réfutée | `HWY-INNER-CUTOFF-GATE-1`, gap positif entre `epsilon` et `2epsilon` | l'empilement logarithmique des échelles persiste |
| lissage intérieur radial du profil HWY pair | excitation du mode instable certifié impair | réfutée | `[L_U,J]=0`, `Q_-g_epsilon=0`, `HWY-PARITY-PROJECTION-GATE-1` | un mode pair ou une perturbation impaire ne sont pas exclus |
| couche impaire `epsilon^beta` à `t=kappa epsilon²` | coordonnée instable bornée à `tau=0` | conditionnelle | facteur linéaire exact `kappa^-a epsilon^(beta-2a)`; nécessaire `beta>=2a>=217/1000` | adjoint, conditionnement, cutoff extérieur, non-linéarité et pression projetée non certifiés |
| profil/couche pairs + solution forte unique | préservation de la parité avant le temps maximal | classique et dérivé par équivariance | unicité forte locale et commutation de NS avec la réflexion | n'interdit pas une brisure de symétrie faible après perte d'unicité forte |
| même donnée `L²` à temps fini + une branche forte sur l'intervalle | coïncidence de toute branche Leray–Hopf sur cet intervalle | classique et sourcée; dérivation à constante suivie | relative énergie, Prodi/Grönwall; coefficient `2||nabla u||_infinity` pour `E=(1/2)||w||²_2` | s'arrête au premier temps où la classe forte ou le coefficient est perdu |
| même trace critique quand `tau->-infinity` | même donnée de Cauchy à un temps fini | réfutée | famille exacte `b_A=aA exp(a tau)/(a+A exp(a tau))`, `ASYMPTOTIC-TRACE-CAUCHY-GATE-1` | la trace oublie le coefficient `A`, récupérable à tout temps fini |
| branche HWY singulière | deux solutions Leray–Hopf pour une même donnée Clay lisse | manquante | unicité faible–forte sur la durée classique | il faut d'abord une perte de régularité forte, déjà un breakdown Clay |
| énergie `L²` seulement continue et décroissante | inégalité d'énergie Leray–Hopf | réfutée en général | Cheskidov–Zeng–Zhang `2503.05692v1` construit explicitement hors classe Leray–Hopf | la monotonie scalaire n'impose pas l'inégalité entre deux temps |
| solutions depuis des données arbitrairement proches | non-unicité depuis une même donnée | non transférable | Palasek `2509.18595v1`; Liao–Qin `2602.12666v1` | quantificateurs de Cauchy différents; le second cadre est 2D forcé et numérique |
| blow-up d'une solution Leray–Hopf forcée unique | alternative négative Clay (C) | non transférable | Galdi–Gazzola `2606.15189v3` | force seulement dans des classes d'intégrabilité singulières, pas `C∞` rapidement décroissante avec toutes ses dérivées |
| calcul flottant convergé | solution PDE exacte | manquante | — | compact analytique, bornes de queue, intervalles |
| non-unicité faible forcée | breakdown (A)/(B) | non transférable | Albritton–Brué–Colombo | force et notion de conclusion |

## Dictionnaire des pertes

| Identifiant | Type de perte | Localisation précise | Test |
|---|---|---|---|
| `GAP-SCALE-ENERGY` | puissance d'échelle | `||u_lambda||_2²=lambda^-1||u||_2²` | paquets concentrés à énergie fixée |
| `GAP-DERIV-NL` | dérivée | `u dot nabla u` dans l'énergie haute | triades haute–basse signées |
| `GAP-CONST-TRUNC` | constante | Galerkin ou troncature renormalisée | tracer la constante avec le cutoff |
| `GAP-COMPACT-Q` | compacité | passage `u_n tensor u_n` | trois échecs sous énergie seule: queue, défaut de trace, module supercritique; pivot requis |
| `GAP-PRESSURE-TAIL` | pression/localisation | défaut de tension de `integral |U_n|²|y|^-4` après zoom | paquets multi-échelles; extraction ESS/GKP |
| `GAP-PRESSURE-HARMONIC` | jauge de pression | équation de Poisson sur `R³` ne fixe pas les composantes affines | solution ancienne parasite exacte |
| `GAP-HYBRID-INHERITANCE` | stabilité des hypothèses | mildness/bornitude KNSS et trace nulle ESS appartiennent à deux limites distinctes; dans la normalisation maximum, les limites commutent au temps-record `t_k`, tandis que `T` devient l'extrémité mobile `B_k` | matrice d'héritage + rigidité à trace nulle + audit des horloges/commutateur; axe suspendu après trois stratégies |
| `GAP-SIGN-FLUX` | positivité | flux d'énergie inter-échelles | contre-triades exactes |
| `GAP-VORTICITY-TAIL` | non-localité/quantificateurs | direction locale vers strain total et stretching positif | `FAIL-NS-0016`; exiger une queue Biot–Savart annulaire explicite |
| `GAP-DEGIORGI-UNIFORMITY` | constante/troncature | production de (40) depuis (22) par énergie tronquée | fermé conditionnellement au cycle 0017 : pas d'itération, coefficient `nu lambda/(2S_6²M)`, seuil fixe et Chebyshev suivis; la finitude des tronqués vient de la solution classique, pas du faible-`L^(3/2)` |
| `GAP-COMMUTATOR-UNIFORMITY` | non-localité/constante | production de (22) depuis la cohérence `bmo_phi`, extension locale et queues dyadiques | fermé conditionnellement au cycle 0018 : semi-norme de Jones, interpolation CRW, réarrangée exacte, facteur trois et poids `4^-k`; l'hypothèse géométrique globale reste une prémisse |
| `GAP-ENDGAME-SYNCHRONIZATION` | quantificateur/constante | passage de la queue de vitesse (49) au rayon de sparseness puis au critère analytique (58) | fermé conditionnellement au cycle 0019 : temps garanti, dichotomie, seuil uniforme, rayon témoin et même `M`; le choix maximal littéral est réfuté |
| `GAP-ACTIVE-CORE-BMO` | géométrie/extension | direction cohérente seulement sur `{omega>lambda}` vers prémisse globale `bmo_phi` | fermé négativement au cycle 0020 pour l'implication universelle : optimum `4ab/(a+b)`, famille divergence-free à deux cœurs et ambiguïté aux zéros; une réouverture exige un packing inter-composantes quantitatif |
| `GAP-CRITICAL-PROFILE-ADMISSIBILITY` | admissibilité/pression | profil critique ponctuel de vorticité vers champ divergence-free énergétique et direction globale `bmo_phi` | fermé négativement au cycle 0021 pour la classe vectorielle exactement récurrente : porte sphérique, rigidité log-BMO et défaut de coupure; la Definition 2.1 scalaire reste sous-quantifiée |
| `GAP-LOG-RECTIFIED-PROFILE` | géométrie/admissibilité | direction vers un axe fixe, amplitude critique bornée et masse non dégénérée vers profil solénoïdal | fermé négativement au cycle 0022 sous masse par bloc : signe radial corrigé, budget de degré un et construction dégénérée tranchante; le faible-Lorentz seul reste insuffisant |
| `GAP-WANDERING-AXIS-PROFILE` | géométrie/multi-échelle | axe `e=e(s)` échappant à tout double cône fixe vers profil critique solénoïdal | fermé négativement au cycle 0023 pour variation et erreur pondérée sublinéaires; une rotation uniforme assez rapide échoue au test log-BMO centré |
| `GAP-MULTICORE-ANGULAR-CASCADE` | géométrie/multi-échelle | phases multiples sans axe global vers profil critique solénoïdal | fermé négativement au cycle 0024 sous `Phi<=M`, masse critique par bloc et même extension bornée log-BMO : la fraction active extrait un axe à variation et erreur `O(log N)` |
| `GAP-UNBOUNDED-ANGULAR-INTERMITTENCY` | géométrie/multi-échelle | faible-`L^(3/2)` et log-BMO vers contrôle d'une amplitude critique concentrée | cycle 0025 : divergence, énergie, masse et Biot–Savart sont compatibles avec le train sparse, mais une forme interne fixe échoue au BMO global et le résidu stationnaire reste critique |
| `GAP-DIRECTIONALLY-FLAT-INTERMITTENCY` | géométrie/div–curl | direction interne asymptotiquement constante + compensation de `integral curl U=0` vers blob critique localisé | quantifié au cycle 0026 : `MO_D>=2alpha^3m^3/(27K^3|D|)` pour la masse conique `m`; le faible-Lorentz n'empêche pas `m->0` et une interface simple garde une oscillation locale d'ordre un |
| `GAP-NESTED-RETURN-FLOW-CASCADE` | géométrie/div–curl/multi-échelle | compensateur rare à deux amplitudes vers curl compact dont la direction est log-BMO sur toutes les sous-boules | cycle 0027 : lift axisymétrique compact et bornes critiques réalisés, mais l'aspect fixé échoue sur une boule radiale et le résidu toroidal est non nul |
| `GAP-GROWING-ASPECT-RETURN-FLOW` | géométrie/multi-échelle/constante | aspect torique croissant vers disparition du coût `w/R` sans perte faible-Lorentz, énergie ou compacité | condition nécessaire possible mais insuffisante : les transitions verticale–radiale d'un produit séparable et les interfaces directes restent visibles localement |
| `GAP-NONSEPARABLE-RETURN-FLOW-MASKING` | géométrie/capacité/dynamique | somme de couches où `W_z` masque successivement chaque retour `W_r` vers log-BMO all-ball | actif : construire un streamfunction non séparable fini, mesurer les ensembles `|W_r|>=|W|/4`, leurs capacités, les normes critiques, l'énergie et le résidu |
| `GAP-LIMIT-ADMISSIBLE` | stabilité/admissibilité | profil singulier vers donnée de Schwartz | trois portes distinctes fermées : `FAIL-NS-0013` réfute la compacité `L³`, `0014` annule le mode impair sous lissage symétrique, `0015` réfute l'identification trace asymptotique/donnée finie; axe suspendu |
| `GAP-NUM-CONTINUUM` | calcul vers continuum | discrétisation finie | résidu d'intervalle + queue analytique |

## Arêtes prioritaires

1. `GAP-NONSEPARABLE-RETURN-FLOW-MASKING` : construire une somme finie
   `psi_n=sum_j A_(n,j)(r)chi_(n,j)(z)` et abandonner si une couche garde une
   capacité polynomiale où `|W_r|>=|W|/4`.
2. `GAP-GROWING-ASPECT-RETURN-FLOW` : suivre l'aspect comme coût auxiliaire;
   ne pas le confondre avec un contrôle des transitions locales all-ball.
3. `GAP-NESTED-RETURN-FLOW-CASCADE` : l'aspect fixé est fermé par la boule de
   calotte; ne le rouvrir qu'avec aspect croissant ou géométrie non séparable.
4. `GAP-DIRECTIONALLY-FLAT-INTERMITTENCY` : le coût conique est maintenant
   explicite; ne rouvrir la version à masse conique uniforme qu'en cassant
   l'annulation, la borne faible-Lorentz ou le taux log-BMO.
5. `GAP-UNBOUNDED-ANGULAR-INTERMITTENCY` : le train de forme fixe est fermé
   par BMO global; ne le rouvrir qu'avec une forme interne dépendant de
   l'échelle ou une formulation intrinsèque pondérée sur l'ensemble actif.
6. `GAP-MULTICORE-ANGULAR-CASCADE` : fermé négativement sous amplitude bornée,
   masse par bloc et extension log-BMO commune; ne le rouvrir qu'en cassant
   explicitement une de ces prémisses.
7. `GAP-WANDERING-AXIS-PROFILE` : fermé négativement pour variation et erreur
   sublinéaires; ne le rouvrir qu'avec une sélection non `BV`, un centre mobile
   ou un terme de recharge effectif non contrôlé par la variation.
8. `GAP-LOG-RECTIFIED-PROFILE` : fermé négativement pour l'axe fixe sous
   amplitude bornée et masse par bloc; ne le rouvrir qu'en quantifiant une
   intermittence angulaire non bornée ou une perte de masse.
9. `GAP-CRITICAL-PROFILE-ADMISSIBILITY` : fermé négativement pour la
   récurrence vectorielle exacte; ne le rouvrir qu'avec un profil non
   récurrent ou une limite espace-temps quantifiée.
10. `GAP-VORTICITY-TAIL` : confronter la queue de strain annulaire réparée à
   un contre-profil multi-échelle divergence-free issu d'une dynamique.
11. `GAP-NUM-CONTINUUM` : isoler un opérateur compact à queues certifiables.
12. Noyau Fourier–Leray formel : certifier les identités d'énergie finies avant
   toute formalisation de scénario PDE.

`GAP-COMPACT-Q` est suspendu sous énergie seule après trois stratégies
distinctes réfutées. Il ne sera rouvert qu'avec une hypothèse structurelle
explicitement héritée d'un premier blow-up.

`GAP-HYBRID-INHERITANCE` est également suspendu dans la normalisation maximum
KNSS : une réouverture exige une extraction différente ou un lemme
d'équivalence de profils, et non une nouvelle permutation des mêmes limites.

`GAP-LIMIT-ADMISSIBLE` est suspendu après les trois stratégies
`FAIL-NS-0013`–`0015`. Une réouverture exige un mécanisme de perte forte pour
une donnée lisse fixée ou une stabilité non perturbative qui ne réutilise pas
compacité `L³`, excitation impaire symétrique ou identification des traces.

`GAP-CRITICAL-PROFILE-ADMISSIBILITY` est suspendu dans la classe exactement
homogène/log-périodique après trois portes différentes : la magnitude scalaire
ne fixe pas une vorticité, la récurrence vectorielle contredit log-BMO pour un
profil non nul, et la coupure radiale porte un défaut critique invariant. Le
pivot `GAP-LOG-RECTIFIED-PROFILE` a rompu la récurrence exacte mais échoue à
axe fixe sous masse critique par bloc. `GAP-WANDERING-AXIS-PROFILE` échoue à
son tour pour tout axe à variation et erreur pondérée sublinéaires. Le cycle
0024 montre que les multicœurs ne suppriment pas cet axe lorsque amplitude,
masse et extension log-BMO sont uniformes. Le cycle 0025 concentre bien
l'amplitude sans perdre divergence, énergie, faible-Lorentz ni Biot–Savart,
mais la répétition d'un motif interne non constant échoue sur les boules
décentrées et son résidu stationnaire est critique. Le cycle 0026 quantifie
le coût de compensation : toute masse conique normalisée
`mu=m/(K|D|^(1/3))` force `MO_D>=2alpha^3mu^3/27`. L'exposant cubique est sharp
dans la classe mesurable, mais la masse critique peut rester non dégénérée
alors que `m->0`; une interface à deux phases garde toutefois un BMO local
égal à un. Le pivot actif `GAP-NESTED-RETURN-FLOW-CASCADE` doit réaliser ce
compensateur rare comme curl compact et étaler sa transition sur des
sous-échelles emboîtées sans perdre la borne critique. Une extension annulaire
peut réduire le coût à `Theta(1/log(R/h))`, mais le lift exactement collinéaire
est nul; le premier test spatial doit donc conserver les composantes
transverses d'un curl axisymétrique. Le cycle 0027 réalise ce lift avec flux
pondéré nul, retour d'amplitude `~n²`, faible-Lorentz uniforme et énergie
`O(n^-2)`. Sur la calotte, la composante axiale s'annule et la direction vaut
exactement `e_r`; une boule impose `MO>=3w/[2048(R+w)]`. L'aspect fixé et la
stationnarité sont donc fermés. Une variante à calotte `n^-3` réalise en plus
`MO_D~n^-3` sur le domaine parent et montre que div–curl compact n'améliore
pas l'exposant cubique; elle ne contrôle pas le supremum all-ball et sa vitesse
`L³` tend vers zéro. Le pivot `GAP-NONSEPARABLE-RETURN-FLOW-MASKING` doit
masquer chaque transition radiale par une couche verticale suivante, sans
cacher une capacité polynomiale, un aspect divergent ou un résidu critique.

Le cycle 0028 ferme négativement cette nécessité topologique : un tore
azimutal mince réalise `div omega=0`, moyenne nulle et extension statique
log-BMO sans composante radiale. L'arête

```text
NS-TOROIDAL-LOG-BMO-VELOCITY-COLLAPSE
  -- réfute --> fermeture implique retour radial
  -- réfute --> vorticité critique + log-BMO implique liminf ||u||_3>0
  -- ouvre --> GAP-MOMENT-CORRECTED-TOROIDAL-CASCADE
```

est `COMPUTATION_ONLY` avec dérivation analytique auditée. La perte exacte est
Biot–Savart : `||u||_3^3<=CK^3(h/R+(h/R)^2)`. Sur `R^3`, s'ajoutent l'impulsion
non nulle, la queue non-Schwartz et la régularité de la classe sans swirl.

Le claim `NS-AXISYMMETRIC-RADIAL-EXCESS-CAPACITY` ajoute l'arête conditionnelle

```text
Delta_Omega>0 --> mesure radiale >0 --> capacité newtonienne >0.
```

Le trou est explicite : ni rang fini, ni criticité Lorentz ne force
`Delta_Omega>0`, et la capacité newtonienne ne donne pas automatiquement une
boule de densité BMO. La propagation statique vers une direction globale
échoue pour l'anneau unisigné sans swirl à temps positif; cette arête est
« réfutée dans la sous-classe », non dans le cas périodique signé.

Le cycle 0029 ajoute

```text
NS-IMPULSE-CORRECTED-TORUS-PAIR-COLLAPSE
  -- exact --> I(W)=0
  -- réfute --> I(W)=0 implique vitesse de Schwartz
  -- exact --> cK^3h/R <= ||u||_3^3 <= CK^3(h/R+(h/R)^2)
  -- réfute --> correction finie des moments préserve une vitesse critique
  -- ouvre --> GAP-MANY-TORUS-CRITICAL-ACCUMULATION.
```

L'impulsion est translation-invariante parce que chaque tore a moyenne
vectorielle nulle. La queue `|x|^-4` provient du second moment translaté; le
minorant `L^3` vient de Stokes sur une section active et reste vrai pour le
champ total. Pour tout cardinal fixé et rapports d'aspect tendant vers zéro,
Minkowski ferme la branche indépendamment des signes. Le trou suivant porte
donc sur cardinal croissant, packing et cohérence des termes croisés, non sur
un multipôle supplémentaire isolé.

`GAP-SIGN-FLUX` est borné par deux résultats négatifs : l'hélicité globale ne
fixe pas le flux triadique et la cohérence d'un seul patch ne fixe pas le
stretching ponctuel. Une réouverture doit porter une hypothèse globale,
uniforme en temps, et conserver explicitement `GAP-VORTICITY-TAIL`.

Une arête ne passe à « classique et sourcée » qu'avec une source primaire et
des hypothèses identiques. Une expérience finie reste « numérique » ou
`COMPUTATION_ONLY` jusqu'à un raccord analytique certifié.

## Cycle 0030 — arêtes poreuses et compactes

```text
NS-POROUS-MANY-TORUS-L3-COLLAPSE
  -- classique/sourcé --> HLS I_1:L^(6/5)->L^2
  -- hypothèse géométrique --> packing local length(B_r)<=P r^3/q^2
  -- dérivation interne --> ||u||_3^3<=CK^3[h/mathcal L+(h/q)^(4/3)]
  -- périodique conditionnel --> ajouter CK^3S
  -- réfute --> N->infinity homogène restaure une vitesse critique
  -- manque --> ledger Morrey–Carleson pour A_j,h_j,q_j variables.
```

```text
NS-COMPACT-VELOCITY-ENDPOINT-SEPARATION
  -- exact --> BS[curl U_N]=U_N pour U_N compact divergence-free
  -- exact --> L3 fort se somme cubiquement sur supports disjoints
  -- contre-profil --> faible-L3 et faible-L^(3/2) ne contrôlent pas L3 fort
  -- petite donnée sourcée --> normalisation N^(-1/3) globalement régulière
  -- obstacle --> oscillation interne de direction × |log r_N|
  -- ouvre --> GAP-COMPACT-VELOCITY-WEAK-CRITICAL-DIRECTION.
```

Le raccord au problème Clay reste **manquant** : il faut simultanément un
budget faible-`L^3` non perturbatif, une direction de vorticité intérieurement
plate sur toutes les boules actives et un temps d'interaction uniforme. La
compacité et les seules normes critiques ne les fournissent pas.

## Priorité après le cycle 0030

1. `GAP-COMPACT-VELOCITY-WEAK-CRITICAL-DIRECTION` — actif; isoler un bloc
   compact dont l'oscillation active décroît comme `1/|log r|`, ou démontrer
   que `integral curl U=0` impose une boule d'oscillation uniforme.
2. Ledger tubulaire hétérogène — conditionnel; chercher une mesure de
   Carleson pondérée compatible à la fois avec la distribution faible-Lorentz
   et le packing des corridors.
3. Propagation/diffusion — manquante; ne l'ouvrir qu'après un gate statique
   non perturbatif, puis suivre `t_int/(r_min^2/nu)` et la pression non locale.

## Cycle 0031 — arête d'aspect compacte

```text
NS-COMPACT-SWIRL-ASPECT-ENDPOINT-GATE
  -- exact --> div U=0 pour U=V(R/r)eta chi e_theta
  -- exact --> annulation du terme cylindrique de courbure
  -- dérivation interne --> K_U^3~V^3Rab
  -- dérivation interne --> K_W^3>=cV^3 max(R^2b^2/a,R^2a^2/b)
  -- condition endpoint --> K_U>=kappa et K_W<=K
  -- implique --> a/R,b/R>=c(kappa/K)^3
  -- géométrie sourcée en interne --> boule pure e_r avec MO>=c min(a,b)/R
  -- réfute dans l'ansatz --> aspect divergent compatible avec les deux gates
  -- manque --> ledger de transitions pour couches non séparables
  -- ouvre --> GAP-NONSEPARABLE-COMPACT-CURL-FLATNESS.
```

La passe de flux ajoute une arête distincte, non suffisante :

```text
integral_B curl U = integral_(partial B) n cross U
  -- terme manquant --> contrôle du flux de bord
  -- sous petit L^(3,infinity)/L^(3/2,infinity) --> bonne sphère annulaire
  -- contre-profil compact --> aucune minoration sur chaque boule active.
```

## Priorité après le cycle 0031

1. `GAP-NONSEPARABLE-COMPACT-CURL-FLATNESS` — actif; tester deux couches
   décalées et sommer leurs coûts de distribution sans utiliser Minkowski.
2. Flux de bord local — conditionnel; relier une masse conique non dégénérée à
   une bonne sphère sans imposer une petitesse perturbative de la vitesse.
3. Propagation/diffusion — toujours différée jusqu'à un gate statique complet.

## Cycle 0032 — arête de support mince non séparable

```text
NS-THIN-PURE-SWIRL-LORENTZ-COLLAPSE
  -- hypothèse exacte --> F in C_c^infinity, supp F subset {R/2<r<3R/2}
  -- identité cylindrique --> curl[(R/r)F e_theta]=(R/r)nabla_perp F
  -- NS-SRC-0067/0070/0126 --> potentiel et weak HLS bidimensionnel
  -- exact --> L^(6,infinity)(supp F) vers L^(3,infinity), facteur S_2^(1/6)
  -- exact --> comparaisons cylindriques R^(1/3) et R^(2/3)
  -- conclut --> K_U<=C(S_2/R^2)^(1/6)K_W
  -- Yamazaki NS-SRC-0118 --> petite donnée globale lorsque K_U devient petit
  -- réfute --> superposition mince non séparable comme candidat de blow-up
  -- ne transfère pas --> section épaisse, vitesse poloïdale, pression, temps
  -- ouvre --> GAP-THICK-CROSS-SECTION-GRADIENT-DIRECTION.
```

Arêtes adverses complémentaires :

```text
coaire NS-SRC-0132 --> ||curl U||_1=2pi TV(rU_theta)
TV(sum F_j) -/-> sum TV(F_j)        [arête réfutée par annulation]
canceling NS-SRC-0133--0135 -/-> anti-annulation couche par couche
deux couches décalées --> masquage local exact
masquage local exact -/-> survie globale du gate de support.
```

## Priorité après le cycle 0032

1. De `S_2/R^2>=c` à une boule de rotation du gradient — manquant.
2. De cette boule à une minoration log-BMO all-ball — conditionnel.
3. Des trois gates statiques à un temps d'interaction et au profil limite —
   manquant.

## Cycle 0033 — arête directionnelle de diamètre borné

```text
NS-BOUNDED-CROSS-SECTION-DIRECTION-GATE
  -- niveau presque optimal --> lambda^3|{|F|>lambda}|>=K_f^3/2
  -- scission signée --> G=(sigma F-lambda/2)_+
  -- weak HLS --> aire active >=c(K_f/K_g)^6
  -- NS-SRC-0132 --> TV(G)>=cK_f^2/K_g
  -- identité cylindrique --> ||curl U_G||_1=2pi R TV(G)
  -- curl compact --> moyenne vectorielle nulle
  -- couverture de S^2 --> masse conique >=c||curl U_G||_1
  -- NS-LORENTZ-CONE-COMPENSATION --> MO_B>=c m^3/(K_w^3|B|)
  -- diamètre axial O(R) --> |B|<=C_Lambda R^3
  -- comparaisons cylindriques --> MO_B>=c_Lambda(K_u/K_w)^6
  -- concentration --> log-BMO non uniforme
  -- réfute --> profil pure-swirl borné passant les trois gates
  -- ouvre --> GAP-AXIALLY-DISPERSED-PURE-SWIRL-SELECTION.
```

Arêtes non fermées :

```text
endpoints globaux de cellules hétérogènes
  -- ? --> sélection d'un rapport local non dégénéré
diamètre axial >>R
  -- perte --> volume de la boule globale
degré de la Gauss map
  -- insuffisant seul --> aucune masse/épaisseur quantitative.
```

## Priorité après le cycle 0033

1. Sélection Lorentz d'une cellule dominante — manquante.
2. Packing axial hétérogène sans dominance — expérience décisive.
3. Temps, pression et profil limite — toujours différés.

## Cycle 0034 — sélection par registre BV

```text
quasi-normes faibles cellulaires seules
  -- niveaux de curl échelonnés --> NS-WEAK-LORENTZ-CELL-SELECTION [REFUTED]

plateau effectif + boîte comparable
  -- coaire/isopérimétrie --> registre BV A_j v_j^(2/3)
  -- distribution globale de U --> niveau lambda et volume S
  -- concavité --> sum v_j^(2/3)>=c lambda S/epsilon
  -- intégrale faible-L^(3/2) --> epsilon>=cK_u^2/K_w
  -- monotonie --> rapport local >=c(K_u/K_w)^2
  -- NS-BV-REGISTERED-HETEROGENEOUS-CELL-SELECTION
  -- NS-BOUNDED-CROSS-SECTION-DIRECTION-GATE
  --> MO local >=c(K_u/K_w)^12
  -- ferme --> cellules pure-swirl épaisses disjointes enregistrées
  -- ouvre --> GAP-DEGENERATE-CELL-REGISTER-OR-OVERLAP.
```

Nature des arêtes :

```text
coaire/isopérimétrie cylindrique : classique sourcée + spécialisation interne;
sélection BV : dérivation interne COMPUTATION_ONLY;
contre-distribution : contre-exemple exact REFUTED;
profiles faible-endpoint -> même cellule : manquante;
Barker-Prange Type I -> même centre dynamique : classique sourcée conditionnelle;
même centre Type I -> Type II général : manquante;
rapport local -> rayon R_j tendant vers zéro : manquante.
```

## Priorité après le cycle 0034

1. Registre stable sous queues/corridors dégénérés ou contre-exemple lisse.
2. Packing signé lorsque les curls se chevauchent.
3. Sélection dynamique de l'échelle et contrôle du cutoff de Leray.

## Cycle 0035 — bande de niveau globale pure-swirl

```text
volume témoin v_j
  -/-> halo O(v_j) portant le registre
  -- dilatation critique --> NS-FIXED-CORE-HALO-LOCALIZATION [REFUTED]

Ku faible-L3 global
  -- niveau eta-presque optimal lambda --> mu_U(lambda)
  -- anneau R_j/2<r<3R_j/2
       --> {|U|>lambda} subset union {|F_j|>lambda/2}
       --> H subset {|U|>lambda/6}
  -- Fleming–Rishel coaire + Federer–Fleming isopérimétrie
       --> integral_H|W|>=c lambda sum V_i^(2/3)
  -- max K_(u,j)=epsilon --> sum V_i^(2/3)>=lambda V/(3epsilon)
  -- Lorentz faible-L^(3/2) --> epsilon>=(C_I/324)K_u^2/K_w
  -- disjonction des curls --> rapport local quadratique
  --> NS-PURE-SWIRL-COMMON-LEVEL-CELL-SELECTION [COMPUTATION_ONLY]
  -- ferme --> longues queues et sections variables pour sélection endpoint
  -- ouvre --> GAP-ACTIVE-HALO-DIAMETER-OR-OVERLAP.
```

Nature des arêtes :

```text
coaire/isopérimétrie/Lorentz : classiques et sourcées;
composition à niveau commun : dérivation interne auditée;
halo fixe v_j : contre-exemple lisse curl-compatible;
volume de H -> diamètre de H : manquante et fausse sans structure;
composante active -> boule directionnelle : manquante;
supports disjoints -> recouvrement/annulation : manquante;
boule statique -> échelle pré-singulière : manquante.
```

## Cycle 0036 — arête par composante

```text
NS-PURE-SWIRL-COMMON-LEVEL-CELL-SELECTION
  -- raffinement connexe --> composantes de {sigma F_j>lambda/4}
  -- zéro sur le bord --> troncature W_c^(1,infinity), curl sans mesure
  -- coaire/isopérimétrie composante --> registre additif
  -- fonctions de distribution --> constante C_I/648
  --> NS-PURE-SWIRL-COMPONENTWISE-DROPLET-SELECTION

NS-BOUNDED-CROSS-SECTION-DIRECTION-GATE
  -- chaîne Sobolev + coaire BV + curl compact
  --> NS-PURE-SWIRL-LIPSCHITZ-DIRECTION-GATE
  -- boîte O_Lambda(R_j) de chaque composante
  --> MO_B>=c_Lambda(K_u/K_w)^12.
```

Nature des arêtes :

```text
coaire/isopérimétrie/Lorentz : classiques et sourcées;
troncature par composante : dérivation interne auditée;
interface C-infinity vers W^(1,infinity) : dérivation interne explicite;
Frank–Lieb volume+périmètre -> boule locale : classique sourcée;
volume+périmètre -> diamètre de composante : réfutée;
pont au-dessus du cutoff -> sous-composante bornée : manquante;
chevauchement des curls -> monotonicité locale : manquante;
gate statique -> rayon pré-singulier : manquante.
```

## Cycle 0037 — coût critique d'une branche persistante

```text
NS-SRC-0156 (composantes M-indécomposables)
  + NS-SRC-0163 (2 diam(E^1)<=P_2(E))
  + NS-SRC-0132 (coaire)
  -- composition interne --> integral_H|W|>=4pi RD(b-a)

H={a<sigma F<b}
  -- facteur annulaire --> H subset {|U|>2a/3}
  -- faible-L3 --> |H|^(1/3)<=3K_u/(2a)
  -- intégration faible-L^(3/2) --> integral_H|W|<=9K_uK_w/(2a)
  --> NS-PURE-SWIRL-PERSISTENT-BRIDGE-DIAMETER

composante au-dessus du cutoff A
  -- persiste sur (A/2,A) --> A^2RD<=9K_uK_w/(2pi)
  -- AR>=kappa K_u --> diamètre D/R contrôlé
  -- NS-PURE-SWIRL-COMPONENTWISE-DROPLET-SELECTION
  -- NS-PURE-SWIRL-LIPSCHITZ-DIRECTION-GATE
  --> oscillation directionnelle locale conditionnelle de type q^15.
```

Nature des arêtes :

```text
périmètre-diamètre planaire : classique, publié et source-vérifié;
coaire/composantes/Lorentz : classiques sourcés;
constante axisymétrique 9/(8pi) : dérivation interne COMPUTATION_ONLY;
pont explicite : calcul rationnel exact, pas preuve du continuum;
niveau global -> calibrage AR/K_u local : réfuté;
composante basse -> branche persistante : faux lors d'une fusion tardive;
merge tree discret -> arbre continuum certifié : manquant;
diamètre statique -> solution pré-singulière : manquant;
pression/projection de Leray : absentes.
```

## Priorité après le cycle 0037

1. Calibrage critique local ou retroncature sur arbre de fusion.
2. Test multi-gouttes hétérogène avec persistance et diamètre intégrés.
3. Chevauchements de curls, puis raccord Type I/Type II seulement après
   fermeture des deux premières arêtes.

## Cycle 0038 — fermeture adaptative du diamètre dans le modèle disjoint

```text
NS-SRC-0132 (coaire)
  + NS-SRC-0148 (isopérimétrie R3)
  + NS-SRC-0156 (composantes et périmètre additif)
  + NS-SRC-0163 (2 diam(E^1)<=P_2(E))
  -- composition axisymétrique interne
       --> lambda R>=K^2/(432H)
       --> niveau régulier t avec somme des diamètres O(q^-3 R)
       --> composante au même t avec endpoint quadratique
  --> NS-PURE-SWIRL-ADAPTIVE-DIAMETER-SELECTION

NS-PURE-SWIRL-COMMON-LEVEL-CELL-SELECTION
  + NS-PURE-SWIRL-ADAPTIVE-DIAMETER-SELECTION
       --> cellule tronquée de taille O(q_global^-6 R_j)
       --> rapport local >=c q_global^4
  + NS-PURE-SWIRL-LIPSCHITZ-DIRECTION-GATE
       --> obstruction directionnelle locale statique.

NS-SRC-0168 + NS-SRC-0169 + NS-SRC-0170
  -- erreur L-infinity certifiée --> topologie PL stable
  -/-> labels spatiaux, diamètre, coaire ou PDE
  -- maximin étiqueté + erreur uniforme --> marge col-cutoff certifiable.
```

Nature des arêtes :

```text
coaire/isopérimétrie/périmètre-diamètre/Lorentz : classiques sourcés;
calibration 432 et sélection 20 736 : dérivation interne auditée;
certificat rationnel : calcul exact, pas preuve des entrées continues;
héritage du rapport sous retroncature : réfuté;
arbre topologique seul -> registre coercif : réfuté;
supports de curls disjoints -> curls superposés : manquant;
obstruction statique -> solution pré-singulière : manquant;
pression/projection/diffusion/stretching : absents.
```

## Priorité après le cycle 0038

1. Annulations critiques entre curls superposés et registre local survivant.
2. Cutoff divergence-free et projection de Leray avec constante critique.
3. Raccord dynamique Type I, puis localisation exacte du trou Type II.

## Cycle 0039 — fermeture négative de la sélection étiquetée

```text
NS-PURE-SWIRL-ADAPTIVE-DIAMETER-SELECTION
  -- requiert un curl unique ou des curls disjoints
  -/-> sélection parmi sommants recouvrants

Z_n,-Z_n lisses, divergence-free, même axe–anneau
  -- multiplicité deux
  -- curls individuels ~n sur volume fixe
  -- somme exacte fixe
  --> NS-BOUNDED-MULTIPLICITY-OVERLAP-SELECTION [REFUTED]

NS-SRC-0172 (ondelettes, q<infinity)
  + NS-SRC-0173/0069 (carré-fonction)
  + NS-SRC-0174 (ondelettes divergence-free)
  -/-> base norm-convergente du plein endpoint
  -/-> récupération des labels annulés avant sommation

même axe + même rayon + même anneau
  -- agrégation F_total=sum F_j
  --> NS-PURE-SWIRL-ADAPTIVE-DIAMETER-SELECTION sur le total

axes multiples ou géométries Hodge distinctes
  -- cutoff --> curl de col critique
  -- Leray --> correction non locale
  -?-> GAP-MULTIAXIS-TOTAL-FIELD-LOCALIZATION.
```

Nature des arêtes :

```text
identités de somme/curl et volume témoin : dérivation exacte auditée;
certificats atomiques : calculs rationnels exacts, pas continuum;
sélection universelle sous multiplicité deux : réfutée;
agrégation commune axe–anneau : identité algébrique exacte;
non-séparabilité du plein L^(p,infinity) : dérivation fonctionnelle standard;
ondelettes q<infinity et Littlewood–Paley : classiques sourcés;
localisation intrinsèque multi-axe : manquante;
pression, dynamique et passage au temps maximal : manquants.
```

## Priorité après le cycle 0039

1. Localisation divergence-free intrinsèque du champ total sous axes multiples.
2. Coût critique du curl de col, de Leray et de la pression dans une même boule.
3. Hypothèse anti-annulation canonique falsifiable, puis raccord Type I/Type II.

## Cycle 0040 — fermeture du cutoff solénoïdal statique

```text
NS-SRC-0103 + NS-SRC-0176
  -- droite inverse de divergence sur domaine Lipschitz/John fixé
  -- support et gain d'une dérivée
  + interpolation réelle d'un même opérateur
  + homothétie A_1 -> A_R
       --> correction Bogovskii uniforme en R

div U=0 + chi_RU compact
  --> integral div(chi_RU)=0
  --> b_R=B_R(grad chi_R dot U)
  --> V_R=chi_RU-b_R
  --> NS-SOLENOIDAL-ANNULAR-CUTOFF [COMPUTATION_ONLY]

NS-SRC-0177
  --> usage Navier-Stokes publié sur une couronne fixe
  -/-> borne faible-L3 interne ou régularité globale

plateau critique lisse
  --> coût du col indépendant de R
  --> gain o_R(1) [REFUTED]

A_(R,h) + q=x_1/|x| + Poincare radiale
  --> inf-sup <=C_ph/R
  --> NS-THIN-ANNULUS-DIVERGENCE-COST [COMPUTATION_ONLY]
  --> uniformité h/R->0 [REFUTED dans L^p fort]

Biot-Savart faible HLS
  + NS-SOLENOIDAL-ANNULAR-CUTOFF
  --> q(V_R)>=C_loc^-1(K_core/K_global)q(U)
  -?-> GAP-WEAK-L3-CORE-CAPTURE-AT-PRESINGULAR-SCALE.
```

Nature des arêtes :

```text
Bogovskii Lipschitz/John et usage NS : classiques sourcés;
interpolation Lorentz, homothétie et composition du curl : dérivation auditée;
saturation du cutoff : calcul exact et raccord lisse;
minoration R/h : dérivation forte auditée, pas de claim Lorentz faible;
capture par boule sans contrainte de rayon : triviale et non pertinente;
capture avec R(t)->0 : manquante;
champ coupé statique -> évolution NS non forcée : manquant;
pression, diffusion, non-linéarité, compacité temporelle : manquantes.
```

## Priorité après le cycle 0040

1. Capture faible-`L3` à une échelle pré-singulière imposée.
2. Contre-profil multi-échelle lisse testant toute gamme candidate de rayons.
3. Équation forcée exacte du champ localisé, seulement si la capture survit.

## Cycle 0041 — fermeture conditionnelle de la capture Type I

```text
borne pointwise sup_t ||u(t)||_(3,infinity)<=M
  + inclusion de mesure finie, constante optimale 3
  --> borne Morrey Type I A=C_M M
      [dérivation exacte auditée]

borne Morrey Type I + premier point singulier
  + Barker-Prange 2020, théorème 2 et appendice B
  --> K_3(u(t);B(x_*,R_M(t)))>gamma_w
      pour tout 0<t<T_*
      [classique sourcée, conditionnelle]

concentration absolue + K_3(u(t))<=M
  --> K_core/K_global>gamma_w/M
      [dérivation exacte]

capture Type I + cutoff solénoïdal local
  --> champ test compact conservant le core
      [dérivation statique]
  -?-> GAP-TYPE-I-LOCALIZED-EVOLUTION
      [dérivée temporelle, pression, force et commutateurs manquants]

énergie Leray-Hopf
  -/-> borne Type I faible-L3
      [manquante; perte d'une puissance critique]

Type II, M_j->infinity
  -/-> fraction gamma_w/M_j uniforme
  -/-> durée S_w^*(M_j) uniforme
      [contre-ledger fonctionnel et dépendance source]
  -?-> GAP-TYPE-II-RELATIVE-CORE-CAPTURE.
```

Nature des arêtes : la concentration Lorentz est publiée; la constante
`C_M=sqrt(3)(4pi/3)^(1/6)` et la fraction relative sont des dérivations
internes; le certificat exact ne simule aucune PDE. La capture ne fournit ni
contrôle de vorticité au même centre, ni compacité forte, ni solution ancienne,
ni rigidité.

## Priorité après le cycle 0041

1. Équation forcée exacte du cutoff mobile Type I et scaling de chaque terme.
2. Contre-profil faisant diverger la force localisée, ou borne uniforme dans
   un espace critique.
3. Dégénérescence quantitative Type II de `S_w^*(M)` et des constantes de
   propagation, sans inversion de quantificateurs temporels.

## Cycle 0042 — de la capture Type I à une équation forcée critique

```text
NS-TYPE-I-WEAK-L3-PARABOLIC-CORE-CAPTURE
  + NS-SOLENOIDAL-ANNULAR-CUTOFF
  + B_R obtenu par conjugaison d'un B unité fixe
  --> V(t)=chi_Ru-B_R(nabla chi_R dot u)
  --> NS-MOVING-SOLENOIDAL-CUTOFF-FORCED-EQUATION
      [identité interne auditée]

R=c sqrt(T_*-t)
  --> R'/R=-1/[2(T_*-t)]
  --> kappa=-RR'=2/S_w^*(C_MM)
  --> force physique=R^-3 F(y,sigma)
      [scaling exact]

support annulaire de volume O(R^3)
  -/-> petitesse de la force
  --> norme L1 critique constante
      [NS-SHRINKING-MOVING-CUTOFF-SMALLNESS, REFUTED]

forme locale avec pression chi_Rp
  --> force annulaire non solénoïdale;
projection globale de Leray
  --> force solénoïdale avec queue non locale;
localité + solénoïdalité compacte simultanées
  -?-> manquantes.

borne Type I faible-L3
  --> U,Z dans faible-L3 et P dans faible-L3/2
  --> budgets d'ordre zéro critiques
  -?-> [Delta,Q]U et [D,Q]U
      dans L1+div L^(3/2,infinity)
      [GAP-TYPE-I-MOVING-COMMUTATOR-BOUND]
  -?-> compacité forte d'une suite renormalisée
  -?-> rigidité avec force critique
      [GAP-TYPE-I-FORCED-RIGIDITY].
```

Nature des arêtes : la conjugaison de Bogovskii repose sur les sources
elliptiques déjà cataloguées; la dérivée, la PDE et le scaling sont des
dérivations internes; le témoin pure-swirl est un contre-profil cinématique,
pas une solution Navier–Stokes. La cancellation de la somme complète n'est
ni démontrée ni réfutée.

## Priorité après le cycle 0042

1. Fixer un noyau intégral de Bogovskii et calculer les symboles principaux
   de `[Delta,Q]` et `[D,Q]`.
2. Tester la famille pure-swirl haute fréquence sur la somme complète dans
   `L1+div L^(3/2,infinity)`.
3. Si la borne critique tient, formuler un théorème de rigidité forcé; sinon,
   enregistrer le contre-profil et pivoter vers une localisation intrinsèque
   sans frontière mobile.

## Cycle 0043 — borne critique négative et nouveau trou compact

```text
Costabel–McIntosh: opérateur supporté Psi^(-1)
  + Geißert–Heck–Hieber: échelle Sobolev négative
  --> [Delta,B M_a] d'ordre 0
  --> [D,B M_a] d'ordre -1
      [classique et sourcé au niveau opérateur]

U dans faible-L3 sur la couronne fixe
  --> U dans L2 et dans faible-L3/2 local
  --> -[Delta,Q]U+kappa[D,Q]U dans X
      [dérivation interne]

P=R_iR_j(U_iU_j), H=div(U tensor U+P I)
  --> P,S dans faible-L3/2
  --> B(a dot H) dans L4/3 local
  --> QH dans X
      [dérivation interne + source négative]

P_L div(Z tensor Z)
  --> div(stress faible-L3/2 non local)
      [Calderon–Zygmund classique]

les trois branches
  --> NS-TYPE-I-MOVING-CUTOFF-CRITICAL-FORCE-BOUND
      [COMPUTATION_ONLY]
  --> GAP-TYPE-I-MOVING-COMMUTATOR-BOUND fermé pour B fixé
  -?-> GAP-TYPE-I-FORCE-COMPACTNESS
  -?-> GAP-TYPE-I-FORCED-RIGIDITY
  -?-> régularité globale Clay.
```

Le mode haute fréquence ne détruit que les normes positives. Son terme
`Theta(N)` est exactement la divergence d'un stress d'amplitude uniforme;
il ne constitue donc pas une arête négative vers l'espace `X`.

## Priorité après le cycle 0043

1. Introduire un cutoff externe de facteur `L` et suivre la croissance des
   constantes de l'inverse de divergence avec la géométrie normalisée.
2. Tester l'échappement de la force sur les compacts quand `L->infinity`.
3. Si l'échappement échoue, isoler la topologie faible-étoile minimale dans
   laquelle pression et produits quadratiques passent à la limite.

## Cycle 0044 — arête locale de la force vers zéro

```text
Q_L, même opérateur unité dilaté
  --> Q_LW=W dans B_L
      [classique + conjugaison exacte]
  --> K_L=0 et Q_LH=H dans B_L
      [dérivation interne]

H=P_L div(U tensor U), jauge de Riesz
  + Z_L=U dans B_L
  --> F_L=P_L div(E_L) dans B_rho, E_L=0 dans B_L
      [dérivation interne, L>=2rho]

K_(3/2)(E_L)<=C(1+C_Q²)M²
  + |partial^alpha nabla^3N(y)|<=C_alpha|y|^(-4-|alpha|)
  + L^(3/2,infinity)-L^(3,1)
  --> ||partial^alpha F_L||_Linf(B_rho)
      <=C_alpha M²L^(-3-|alpha|)
      [COMPUTATION_ONLY]
  --> GAP-TYPE-I-FORCE-LOCAL-ESCAPE fermé

kappa[D,Q_L] sur U_L=L^-1U_*(dot/L)
  --> amplitude L^-1, pairing dual de taille L²
  --> norme globale X non uniforme
      [REFUTED comme estimation universelle]

force locale ->0
  -?-> compacité forte locale des vitesses
  -?-> passage de l'énergie et trace non nulle
      [GAP-TYPE-I-LOCAL-COMPACTNESS-TRACE]
  -?-> solution ancienne faible-L3 et rigidité
      [GAP-TYPE-I-ANCIENT-WEAK-L3-RIGIDITY].
```

L'arête vers zéro est spatiale et locale. Elle ne porte aucune dérivée
temporelle et ne peut pas être remplacée par une convergence dans le `X`
global, explicitement fausse pour `kappa!=0`.

## Cycle 0045 — arête de compacité adaptée

```text
NS-TYPE-I-OUTER-CUTOFF-LOCAL-FORCE-ESCAPE
  + borne uniforme K_3(Z_j)
  + jauge de Riesz Pi_j=R_iR_j(Z_j tensor Z_j)
  --> vitesse L2_loc, pression L4/3_loc
  --> Caccioppoli + hole-filling
  --> grad Z_j dans L2_loc
      [COMPUTATION_ONLY, revue contradictoire]

grad Z_j dans L2_loc
  + partial_s Z_j dans W^(-2,4/3)_loc
  --> forte L2_loc par Simon
  + borne L10/3_loc
  --> forte L3_loc
  --> Z_j tensor Z_j fort L3/2_loc
  --> inégalité d'énergie locale avec pression proche/harmonique
  --> NS-TYPE-I-WEAK-L3-LOCAL-SUITABLE-COMPACTNESS

C_tH^-1_loc + forte espace-temps
  -/-> norme terminale non nulle
      [FAIL-NS-0081]

NS-TYPE-I-WEAK-L3-PARABOLIC-CORE-CAPTURE
  -?-> moment signé contre un test fixe
      [GAP-TYPE-I-CRITICAL-TRACE-PERSISTENCE]
  -?-> limite ancienne renormalisée non triviale
  -?-> dérenormalisation mild
  -?-> GAP-TYPE-I-ANCIENT-WEAK-L3-RIGIDITY
  -?-> problème Clay.
```

La compacité intérieure, le produit et l'admissibilité sont fermés sous les
hypothèses du claim. La nouvelle arête manquante est linéaire et terminale :
elle doit empêcher concentration, oscillation ou fuite contre tout test fixe.

## Cycle 0046 — arête de non-trivialité intégrée

```text
Barker-Prange, théorème 2 + appendice B
  --> K_3(u(t);B(x_*,R(t)))>gamma_w pour tout temps tardif
      [classique sourcée, conditionnelle au blow-up Type I]

R²=4(T_*-t)/S_w^*(C_MM)
  + d sigma/dt=R^-2
  --> d(log R)/d sigma=-kappa
  --> chaque fenêtre translatée fixe reste dans (0,T_*)
      [calcul exact]

zoom mobile au centre x_*
  + Q_(L_j)=I dans B_1
  --> K_3(Z_j(s);B_1)>gamma_w pour tout/a.e. s dans J
      [dérivation interne]

NS-TYPE-I-WEAK-L3-LOCAL-SUITABLE-COMPACTNESS
  + K_3(f;B_1)^3<=integral_(B_1)|f|³
  --> integral_(J x B_1)|Z|³>=|J|gamma_w³>0
  --> NS-TYPE-I-PERSISTENT-CAPTURE-SPACETIME-NONTRIVIALITY
      [COMPUTATION_ONLY, revue contradictoire]

Z non triviale dans le volume
  -/-> Z(0) non nulle à l'ancien endpoint
  -/-> (0,0) singulier
      [conclusions plus fortes, non obtenues]

Z ancienne renormalisée non triviale
  -?-> solution ancienne standard de classe identifiée
      [GAP-TYPE-I-DERENORMALIZATION-CLASS]
  -?-> GAP-TYPE-I-ANCIENT-WEAK-L3-RIGIDITY
  -?-> problème Clay.
```

`FAIL-NS-0081` conserve l'arête négative pour une tranche isolée.
`FAIL-NS-0082` retire seulement l'exigence injustifiée d'un moment terminal
avant la non-trivialité espace–temps.

## Cycle 0047 — dérenormalisation et frontière de classe

```text
NS-TYPE-I-WEAK-L3-LOCAL-SUITABLE-COMPACTNESS
  + NS-TYPE-I-PERSISTENT-CAPTURE-SPACETIME-NONTRIVIALITY
  + Pi_j=R_iR_j(Z_j tensor Z_j), faible-étoile global
  --> Z ancienne renormalisée, suitable locale, faible-L3, non nulle

N_s[Z,Pi]=0
  + r_s/r=-kappa, tau_s=r²
  + N_s=r³N_tau, div_yZ=r²div_xv, E_s=r^4E_tau
  --> NS-TYPE-I-DERENORMALIZED-ANCIENT-LOCAL-SUITABLE
      [COMPUTATION_ONLY]

NS-TYPE-I-DERENORMALIZED-ANCIENT-LOCAL-SUITABLE
  -/-> Leray-Hopf                    [énergie globale absente]
  -/-> local-energy avec trace forte [clause de Cauchy absente]
  -/-> mild/scindée                  [Duhamel endpoint absent]
  -?-> rigidité ancienne faible-L3   [GAP actif]
  -?-> régularité Clay.
```

`NS-SRC-0189` ferme seulement la documentation de la cible mild bornée et
de son Liouville `L3` fort; ses hypothèses ne sont pas héritées.

## Cycle 0048 — arête Duhamel endpoint et correcteur énergétique instantané

```text
NS-TYPE-I-DERENORMALIZED-ANCIENT-LOCAL-SUITABLE
  + Linfinity_tL^(3,infinity)_x
  + équation projetée globale
  --> C_w*L^(3,infinity)
      [interne: équation scalaire + densité du prédual]

Yamazaki NS-SRC-0118
  + Taniuchi NS-SRC-0190, définition 1 et lemme 7
  --> bilinéaire endpoint borné test par test
  --> Duhamel Gelfand dans L^(3,infinity) pour tout s<t
      [classique sourcée + application interne]

noyau Oseen + O'Neil Lorentz
  --> B(v,v) in C_tL^p, 3/2<p<3
  --> w in C_tL2, ||w(t)||_2<=CM²(t-t_0)^(1/4)
  --> NS-WEAK-L3-DUHAMEL-L2-CORRECTOR
      [COMPUTATION_ONLY]

Duhamel Gelfand + C_w*L^(3,infinity)
  -/-> C_tL^(3,infinity) en norme
      [Taniuchi mild exige cette clause]
  -/-> intégrale de Bochner / petite constante temporelle
      [FAIL-NS-0084: h^-1 logarithmique]

w in C_tL2
  -/-> w in L2_tHdot1
      [nabla K_h~h^-5/4; contre-profils de mapping]
  -/-> inégalité d'énergie globale perturbée BSS
  -?-> GAP-TYPE-I-RELATIVE-ENERGY-GLOBALIZATION
  -?-> classe BSS
  -?-> rigidité ancienne
  -?-> régularité Clay.
```

L'arête « Duhamel endpoint absent » du cycle 0047 est donc fermée au sens
faible-étoile seulement. Les arêtes de continuité forte, dissipation et
globalisation énergétique restent explicitement manquantes.
