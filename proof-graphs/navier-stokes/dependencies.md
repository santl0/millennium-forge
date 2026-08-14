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
| hélicité globale nulle | petit flux instantané universel | réfutée | contre-triade exacte | pas de positivité modale |
| profil Euler IA | profil NS perturbatif | réfutée pour l'ansatz mono-échelle `lambda>-1/2` | rapport visqueux exact | viscosité dominante |
| donnée homogène `-1` non unique | donnée compacte énergétique singulière non unique | source vérifiée, CAP non reproduite | Hou–Wang–Yang v2; cutoff extérieur, gain `R^-1/8` pour `p=4` | le coeur `1/r` est conservé |
| donnée compacte singulière `1/r` | famille de données Clay lisses divergence-free convergeant en `L²` | classique et dérivé | convolution par mollificateur radial | aucune convergence forte critique |
| convergence `L²` + borne uniforme `L^{3,infinity}` de cutoffs intérieurs | compacité forte `L³` | réfutée | `HWY-INNER-CUTOFF-GATE-1`, gap positif entre `epsilon` et `2epsilon` | l'empilement logarithmique des échelles persiste |
| lissage intérieur radial du profil HWY pair | excitation du mode instable certifié impair | réfutée | `[L_U,J]=0`, `Q_-g_epsilon=0`, `HWY-PARITY-PROJECTION-GATE-1` | un mode pair ou une perturbation impaire ne sont pas exclus |
| couche impaire `epsilon^beta` à `t=kappa epsilon²` | coordonnée instable bornée à `tau=0` | conditionnelle | facteur linéaire exact `kappa^-a epsilon^(beta-2a)`; nécessaire `beta>=2a>=217/1000` | adjoint, conditionnement, cutoff extérieur, non-linéarité et pression projetée non certifiés |
| profil/couche pairs + solution forte unique | préservation de la parité avant le temps maximal | classique et dérivé par équivariance | unicité forte locale et commutation de NS avec la réflexion | n'interdit pas une brisure de symétrie faible après perte d'unicité forte |
| branche HWY singulière | deux solutions Leray–Hopf pour une même donnée Clay lisse | manquante | unicité faible–forte sur la durée classique | il faut d'abord une perte de régularité forte, déjà un breakdown Clay |
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
| `GAP-LIMIT-ADMISSIBLE` | stabilité/admissibilité | profil singulier vers donnée de Schwartz | la convolution donne l'admissibilité `L²`, `FAIL-NS-0013` réfute la compacité `L³`, puis `FAIL-NS-0014` annule exactement la projection sur le mode impair pour tout lissage symétrique; restent asymétrie, adjoint certifié et shadowing non linéaire |
| `GAP-NUM-CONTINUUM` | calcul vers continuum | discrétisation finie | résidu d'intervalle + queue analytique |

## Arêtes prioritaires

1. `GAP-LIMIT-ADMISSIBLE` : certifier l'adjoint et la balance d'une couche
   intérieure impaire ajustée à l'ordre `epsilon^(2a)`; le raccord critique
   statique et l'excitation du mode impair par lissage symétrique sont fermés
   négativement.
2. `GAP-SIGN-FLUX` : élimination rapide de fonctionnelles candidates.
3. `GAP-NUM-CONTINUUM` : isoler un opérateur compact à queues certifiables.

`GAP-COMPACT-Q` est suspendu sous énergie seule après trois stratégies
distinctes réfutées. Il ne sera rouvert qu'avec une hypothèse structurelle
explicitement héritée d'un premier blow-up.

`GAP-HYBRID-INHERITANCE` est également suspendu dans la normalisation maximum
KNSS : une réouverture exige une extraction différente ou un lemme
d'équivalence de profils, et non une nouvelle permutation des mêmes limites.

Une arête ne passe à « classique et sourcée » qu'avec une source primaire et
des hypothèses identiques. Une expérience finie reste « numérique » ou
`COMPUTATION_ONLY` jusqu'à un raccord analytique certifié.
