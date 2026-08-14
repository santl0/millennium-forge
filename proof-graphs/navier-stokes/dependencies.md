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
| alignement critique de vorticité | régularité | conditionnelle, sourcée | Constantin–Fefferman | alignement non déduit de NS |
| hélicité globale nulle | petit flux instantané universel | réfutée | contre-triade exacte | pas de positivité modale |
| profil Euler IA | profil NS perturbatif | réfutée pour l'ansatz mono-échelle `lambda>-1/2` | rapport visqueux exact | viscosité dominante |
| donnée homogène `-1` non unique | donnée Clay non unique | manquante | Hou–Wang–Yang v2 | singularité initiale et unicité faible–forte |
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
| `GAP-SIGN-FLUX` | positivité | flux d'énergie inter-échelles | contre-triades exactes |
| `GAP-LIMIT-ADMISSIBLE` | stabilité/admissibilité | profil singulier vers donnée de Schwartz | troncature `epsilon` et temps local |
| `GAP-NUM-CONTINUUM` | calcul vers continuum | discrétisation finie | résidu d'intervalle + queue analytique |

## Arêtes prioritaires

1. `GAP-LIMIT-ADMISSIBLE` : faible coût pour déterminer si la nouvelle
   construction non unique a un premier maillon vers Clay.
2. rigidité des solutions anciennes mild : la jauge parasite est maintenant
   isolée; comparer ensuite la trace terminale et la non-trivialité réellement
   transmises par ESS, GKP et KNSS avant tout Liouville 3D.
3. `GAP-SIGN-FLUX` : élimination rapide de fonctionnelles candidates.

`GAP-COMPACT-Q` est suspendu sous énergie seule après trois stratégies
distinctes réfutées. Il ne sera rouvert qu'avec une hypothèse structurelle
explicitement héritée d'un premier blow-up.

Une arête ne passe à « classique et sourcée » qu'avec une source primaire et
des hypothèses identiques. Une expérience finie reste « numérique » ou
`COMPUTATION_ONLY` jusqu'à un raccord analytique certifié.
