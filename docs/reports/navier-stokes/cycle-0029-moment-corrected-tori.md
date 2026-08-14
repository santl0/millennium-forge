# Cycle 0029 — paire toroïdale à impulsion compensée

Date de gel : 2026-08-14.

Statut : dérivation analytique interne et audit rationnel exact; aucune
résolution Clay, aucune trajectoire singulière et aucune preuve assistée par
ordinateur du continuum.

## Décision adaptative

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| paire de tores signés, impulsion annulée | 5 | 5 | 5 | 5 | **20** |
| paire non parallèle conservant une vitesse critique | 5 | 2 | 5 | 5 | 17 |
| correcteur de Hodge compact à constantes suivies | 4 | 3 | 4 | 4 | 15 |

Le premier gate du pivot 0028 est sélectionné. La question falsifiable est :

> Deux tores minces de signes opposés peuvent-ils annuler exactement
> l'impulsion hydrodynamique, conserver une direction statique uniformément
> log-BMO et empêcher la vitesse critique `L^3` de s'annuler ?

Le lemme actif porte uniquement sur une paire finie. Une cascade infinie ou
une évolution n'est pas supposée.

## Équation, domaine et notion de solution

Les équations Clay restent

```text
partial_t u+(u·nabla)u=-nabla p+nu Delta u,
div u=0,
nu>0,
f=0.
```

Deux lectures sont séparées.

1. Sur `R^3`, la vorticité prescrite est `C_c^infinity`, divergence-free, et
   la vitesse est sa reconstruction de Biot–Savart décroissante. Elle est une
   donnée lisse énergétique, mais l'annulation du seul moment d'impulsion ne
   lui donne pas la décroissance de Schwartz exigée par l'alternative Clay A.
2. Sur `T^3`, on place la paire dans une cellule, on périodise la vorticité et
   on fixe la vitesse périodique de moyenne nulle par le multiplicateur de
   Biot–Savart. C'est une donnée lisse admissible pour l'alternative Clay B.

Aucune évolution, pression ou solution faible n'est construite dans ce cycle.
Les objets sont des données initiales classiques. Sur `R^3`, la petitesse
finale de `||u_0||_3` permet d'appliquer Kato (`NS-SRC-0010`). Sur `T^3`,
l'adaptation par semi-groupe est standard, mais le corpus ne contient pas
encore un raccord primaire audité avec constantes en viscosité et période;
le cycle n'utilise donc pas ce théorème périodique comme preuve.

## Construction

Pour `n>=4`, posons

```text
R_n=2^(-n),
q_n=2^(-2n),
h_n=2^(-n^2),
a_n=3R_n,
V_n=R_n h_n^2,
A_n=V_n^(-2/3).
```

Soit `c_+=(a_n,0,0)`, `c_-=(-a_n,0,0)`. Autour de la droite parallèle à
`e_z` passant par `c`, notons `r_c` la distance à l'axe et `e_(theta,c)` la
direction azimutale. Pour une bosse fixe `beta>=0`, supportée dans le disque
unité et égale à un sur le demi-disque, définissons

```text
W_(n,c,sigma)(x)
 =sigma A_n beta(((r_c-R_n)^2+x_3^2)/h_n^2)e_(theta,c),

W_n=W_(n,c_+,+1)+W_(n,c_-,-1).                       (1)
```

Les deux tubes et leurs corridors de rayon `q_n` sont disjoints. Chaque terme
de (1) est lisse, divergence-free et de moyenne vectorielle nulle :

```text
div[f(r_c,x_3)e_(theta,c)]=0,
integral_0^(2pi)e_(theta,c)dtheta=0.                  (2)
```

La translation transverse brise toute symétrie axisymétrique continue
commune. La paire ne relève donc pas du théorème global sans swirl, même si
chacun de ses deux termes y appartient après recentrage.

## Normes critiques

À constantes ne dépendant que de `beta`, un tube a volume `V_n` et amplitude
`A_n`. Pour l'union disjointe,

```text
||W_n||_(L^(3/2,infinity))^3 <= C A_n^3(2V_n)^2=4C,
||W_n||_(L^(3/2))^3          = C_beta A_n^3(2V_n)^2
                              =4C_beta.               (3)
```

Les deux quantités restent uniformément bornées et non dégénérées. Elles sont
invariantes sous le scaling vorticité
`W_lambda(x)=lambda^2 W(lambda x)`.

## Annulation exacte de l'impulsion

Pour une vorticité compacte de moyenne nulle, posons

```text
I(W)=(1/2) integral_(R3) x cross W(x) dx.             (4)
```

La translation vérifie

```text
I(W(·-c))=I(W)+(1/2)c cross integral W=I(W).          (5)
```

Le tore positif a `I=J_n e_z`, avec

```text
J_n=pi A_n integral r^2 beta(((r-R_n)^2+z^2)/h_n^2)
                         dr dz >0.                    (6)
```

Le signe opposé change `I` en `-I`; (5) donne donc

```text
I(W_n)=0.                                             (7)
```

Cette annulation est exacte, pas asymptotique.

## Le premier moment ne suffit pas à la classe de Schwartz

La vitesse d'un tore unique possède au premier ordre le champ dipolaire

```text
D_I(x)=c_0[3(I·x)x/|x|^5-I/|x|^3].                   (8)
```

La paire translatée et signée donne

```text
D_I(x-c_+)-D_I(x-c_-)
 =-2(a_n e_x·nabla)D_I(x)+O(|x|^(-5)),               (9)
```

et le terme de degré `-4` n'est pas nul lorsque `I` est parallèle à `e_z` et
la séparation à `e_x`. Par exemple, sur l'axe `e_x`, la dérivée de
`-I/(4pi|x|^3)` donne ici la formule explicite

```text
u_n(t e_x)=-(9R_n J_n)/(2pi t^4)e_z+O(t^-5).         (10)
```

Le même défaut apparaît dans les moments. Si
`M_(ji)=integral x_j W_i`, le tore centré vérifie

```text
M_(12)=J_n,
M_(21)=-J_n.                                         (11)
```

Pour `N_(jk,i)=integral x_j x_k W_i`, la paire satisfait

```text
N_(11,2)(W_n)=4a_n J_n=12R_n J_n !=0.                (12)
```

L'équation (12) seule n'est pas un critère abstrait de non-Schwartz pour tout
curl compact; ici (8)–(9) identifient en plus la composante multipolaire qui
survit. Annuler l'impulsion améliore donc la queue d'une puissance, mais ne
produit pas une vitesse rapidement décroissante à tout ordre.

## Extension directionnelle de la paire

Dans le corridor du tore positif, on interpole géodésiquement
`+e_(theta,c_+)` vers `e_z` selon
`log(q_n/d_+)/log(q_n/h_n)`. Dans celui du tore négatif, on interpole
`-e_(theta,c_-)` vers le même fond `e_z`. Hors des deux corridors, la direction
étendue vaut `e_z`.

Comme les corridors sont séparés de `4R_n+O(q_n)`, une petite boule n'en voit
qu'un. Une boule les voyant tous deux a rayon `rho>=cR_n` et leur défaut total
occupe au plus `C R_n q_n^2`. La décomposition all-ball du cycle 0028 donne
donc

```text
[zeta_n]_(bmo_log)
 <=2C E_n,
E_n<4,                                               (13)
```

où `E_n` est l'enveloppe rationnelle à six termes déjà auditée. Le changement
de signe n'impose aucune interface antipodale : chaque phase tourne dans son
propre corridor nul vers le même fond.

Cette conclusion est encore statique. Elle ne dit pas que les deux corridors
sont propagés par Navier–Stokes. Pour la réalisation coaxiale impaire en `z`,
la diffusion et le principe du maximum rendent les signes stricts dans les
deux demi-espaces à tout temps positif. Toute petite boule centrée sur le plan
`z=0`, loin de l'axe, voit alors des directions opposées sur deux demi-boules :
la moyenne vectorielle est nulle et l'oscillation moyenne vaut exactement un.
Le log-BMO global dynamique échoue. Cette preuve par symétrie ne s'applique
pas automatiquement à la paire transversale (1), pour laquelle la propagation
reste non établie.

## Équivalent décisif de la vitesse

Notons `u_(n,+)` et `u_(n,-)` les vitesses des deux tores. La translation ne
change pas la borne tubulaire du cycle 0028 :

```text
||u_(n,+)||_3^3+||u_(n,-)||_3^3
 <=2C[(h_n/R_n)+(h_n/R_n)^2].                        (14)
```

Par Minkowski et `(a+b)^3<=4(a^3+b^3)`,

```text
||u_n||_3^3
 <=8C[(h_n/R_n)+(h_n/R_n)^2]
 ->0.                                                (15)
```

Cette borne possède la bonne puissance. Dans chaque demi-cœur, un disque
méridien `D_(theta,rho)`, `h_n/4<=rho<=h_n/2`, ne rencontre pas l'autre tore.
Stokes et Hölder donnent pour le **champ total**

```text
integral_(partial D) u_n·dl=A_n pi rho^2,
integral_(partial D)|u_n|^3 dl>=A_n^3 pi rho^4/4.
```

L'intégration en `theta` et `rho` dans les coordonnées tubulaires fournit

```text
||u_n||_3^3>=c A_n^3 R_n h_n^5
            =c h_n/R_n.                              (16)
```

Ainsi

```text
c h_n/R_n<=||u_n||_3^3
          <=C[(h_n/R_n)+(h_n/R_n)^2].                (17)
```

La séparation et les interactions ne peuvent inverser cette borne supérieure.
Le premier correcteur de moment quitte bien la classe axisymétrique globale,
mais reste une petite donnée critique. Sur `R^3`, Kato l'élimine comme profil
de blow-up; sur `T^3`, l'effondrement critique est établi mais le seuil
périodique exact reste une dette bibliographique ou analytique.

Le même argument ferme tout cardinal fixé. Pour `m` tubes actifs disjoints,
notons `K_j` leur quasi-norme faible critique et `eta_j=h_j/R_j`. La
monotonie des fonctions de distribution donne `K_j<=K` pour la quasi-norme du
champ total. La borne tubulaire et Minkowski impliquent

```text
||sum_(j=1)^m u_j||_3
 <=C K sum_(j=1)^m [eta_j+eta_j^2]^(1/3).            (18)
```

Si `m` est uniforme et `max_j eta_j->0`, le membre droit tend vers zéro,
quels que soient les signes et tout nombre fini de moments annulés. Une
construction à trois coefficients `(1,-2,1)` peut annuler l'impulsion et son
premier moment axial, mais n'échappe pas à (18).

## Passe contradictoire

1. **Impulsion contre tous les moments.** (7) n'implique pas Schwartz; (10)
   exhibe la queue suivante.
2. **Sortie de la classe sans swirl.** Elle exige la séparation transverse.
   Deux tores coaxiaux resteraient dans la classe régulière connue.
3. **Interaction supposée constructive.** La norme de la somme est contrôlée
   par Minkowski avant toute hypothèse de phase. Inversement, la circulation
   locale donne déjà le minorant (16), que l'autre tore ne peut annuler.
4. **BMO local.** Les signes opposés ne se touchent jamais dans la zone active;
   les corridors nuls sont essentiels. Une interpolation directe créerait une
   interface d'oscillation d'ordre un.
5. **Domaine.** Le profil périodique est une donnée Clay B, mais aucune
   singularité n'est construite et le raccord de petite donnée périodique
   n'est pas attribué à Kato. Le profil entier échoue à la décroissance Clay A.
6. **Propagation signée.** La paire coaxiale impaire échoue au log-BMO global
   à temps positif sur toute boule coupant son plan nodal; la paire transversale
   n'est pas couverte par cette symétrie.
7. **Échelle.** `L^3(u)` et faible-`L^(3/2)(W)` sont critiques; la limite zéro
   de (17) vient de la dégénérescence de forme `h_n/R_n`, pas d'une simple
   remise à l'échelle.

## Verdict et pivot

Le gate `MOMENT-CORRECTED-TORUS-GATE` est fermé négativement pour toute paire
finie de copies du profil 0028 à même rapport d'aspect : elle peut annuler
l'impulsion, éviter l'interface antipodale et quitter la classe axisymétrique,
mais elle ne conserve pas une vitesse critique non dégénérée. Une correction
finie des moments ne répare pas non plus la décroissance de Schwartz.

Le verrou suivant est `GAP-MANY-TORUS-CRITICAL-ACCUMULATION` : déterminer si
une famille de nombres de composants `N_n->infinity`, avec amplitudes et
aspects distribués, peut satisfaire simultanément

```text
sup_n ||W_n||_(L^(3/2,infinity)) < infinity,
sup_n [zeta_n]_(bmo_log) < infinity,
liminf_n ||u_n||_3 >0,
moments requis annulés.                              (19)
```

Le premier test doit être un budget de comptage abstrait. Si la contrainte
faible-Lorentz impose pour toute distribution disjointe une somme de vitesses
`L^3` tendant vers zéro, la voie multi-tore est abandonnée avant toute
simulation PDE.

## Reproduction

```text
python -B experiments/navier-stokes/moment-corrected-tori/moment_corrected_tori_audit.py
```

Le script emploie `fractions.Fraction`, sans grille, flottant ni graine. Il
contrôle les échelles, l'annulation du coefficient d'impulsion, le premier
coefficient multipolaire non nul, l'enveloppe BMO de paire et l'échelle
bilatérale (17).
Les constantes tubulaires, la réduction all-ball et l'expansion (8) restent
des lemmes analytiques.

Audits contradictoires conservés :

- analyse PDE, multipôle, all-ball et Stokes :
  `f334101c35087ff65a5816f828d692c53b9d051cdb1e16367224709b0ea5d55a`;
- contre-modèle, triplet et cardinal fixé :
  `b4e6b693b050bbd510364196fb33c2e14b2d50eeae2e91f7365542f07ee6dd5a`;
- veille primaire, domaines critiques et interface visqueuse :
  `d7abe1e54338f4cddd37f144fede9c68810ab715257f47fcdba9fe1288707d52`.

Ces passes sont séparées mais utilisent la même famille de modèles Codex;
elles ne constituent pas une revue externe.
