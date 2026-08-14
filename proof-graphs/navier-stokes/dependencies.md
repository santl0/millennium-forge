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
| limite locale de vitesse | limite de pression | conditionnelle | Calderón–Zygmund + queues | non-localité et constante de jauge |
| profil rétrograde `L³` | trivialité | classique et sourcée | Nečas–Růžička–Šverák | ne couvre pas Type II/DSS général |
| solution ancienne bornée générale 3D | trivialité | manquante | Liouville partiel seulement | rigidité |
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
| `GAP-COMPACT-Q` | compacité | passage `u_n tensor u_n` | défaut de produit sous convergence faible |
| `GAP-PRESSURE-TAIL` | pression/localisation | `R_iR_j(u_i u_j)` | deux paquets éloignés |
| `GAP-SIGN-FLUX` | positivité | flux d'énergie inter-échelles | contre-triades exactes |
| `GAP-LIMIT-ADMISSIBLE` | stabilité/admissibilité | profil singulier vers donnée de Schwartz | troncature `epsilon` et temps local |
| `GAP-NUM-CONTINUUM` | calcul vers continuum | discrétisation finie | résidu d'intervalle + queue analytique |

## Arêtes prioritaires

1. `GAP-LIMIT-ADMISSIBLE` : faible coût pour déterminer si la nouvelle
   construction non unique a un premier maillon vers Clay.
2. `GAP-PRESSURE-TAIL` : fort levier sur compacité–rigidité.
3. `GAP-SIGN-FLUX` : élimination rapide de fonctionnelles candidates.

Une arête ne passe à « classique et sourcée » qu'avec une source primaire et
des hypothèses identiques. Une expérience finie reste « numérique » ou
`COMPUTATION_ONLY` jusqu'à un raccord analytique certifié.
