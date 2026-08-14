# Formulation Clay — Navier–Stokes incompressible en dimension trois

Dernière vérification : 2026-08-14. Source normative : Charles L. Fefferman, *Existence and Smoothness of the Navier–Stokes Equation*, Clay Mathematics Institute, [PDF officiel](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf). Ce document reformule mathématiquement l'énoncé sans en modifier les quantificateurs.

## Équation commune

Pour `n=3`, une viscosité constante `nu>0`, une vitesse `u : D x [0,+infinity) -> R^3`, une pression `p : D x [0,+infinity) -> R` et une force extérieure `f`,

```text
partial_t u + (u dot nabla)u = nu Delta u - nabla p + f,
div u = 0,
u(x,0) = u_0(x).
```

Deux domaines sont autorisés par l'énoncé :

- espace entier `D=R^3` ;
- domaine périodique `D=R^3/Z^3`, c'est-à-dire période `1` dans chacune des trois directions.

Il n'y a pas de frontière dans ces deux formulations. Une équation dans un domaine borné, un demi-espace ou un cylindre avec paroi n'est donc pas l'équation de l'énoncé, même lorsque la condition au bord est physiquement naturelle.

## Données admissibles dans l'espace entier

La donnée initiale est `C^infinity`, divergence nulle, et rapidement décroissante avec toutes ses dérivées : pour chaque multi-indice `alpha` et chaque entier `K>=0`, il existe `C_(alpha,K)` tel que

```text
|partial_x^alpha u_0(x)| <= C_(alpha,K) (1+|x|)^(-K).
```

Dans les alternatives forcées, `f` est `C^infinity` et, pour tous `alpha,m,K`,

```text
|partial_x^alpha partial_t^m f(x,t)|
  <= C_(alpha,m,K) (1+|x|+t)^(-K).
```

Une solution admise par Clay vérifie

```text
u,p in C^infinity(R^3 x [0,+infinity))
```

et possède une énergie uniformément bornée : il existe une constante finie `C`, dépendant éventuellement des données mais pas de `t`, telle que

```text
integral_(R^3) |u(x,t)|^2 dx < C,  pour tout t>=0.
```

## Données admissibles dans le cas périodique

La donnée `u_0` est `C^infinity`, divergence nulle et `Z^3`-périodique. La force est lisse, périodique en espace, et toutes ses dérivées décroissent plus vite que toute puissance en temps conformément à l'équation (9) de Fefferman. La vitesse et la pression sont lisses et périodiques sur tout `[0,+infinity)`.

L'erratum joint au texte officiel précise que la pression doit elle aussi être périodique. Aucune hypothèse de moyenne spatiale nulle n'est imposée dans l'énoncé officiel. Sur une cellule de volume fini, la borne d'énergie découle de la régularité périodique à chaque temps ; l'énoncé (B) exige directement la lissité globale.

## Les quatre alternatives officielles

### (A) Existence et lissité sur `R^3`, sans force

Pour tout `nu>0` et toute donnée initiale admissible sur `R^3`, avec `f=0`, il existe des fonctions `u,p` lisses sur `R^3 x [0,+infinity)` satisfaisant l'équation, la condition initiale et la borne uniforme d'énergie.

### (B) Existence et lissité périodiques, sans force

Pour tout `nu>0` et toute donnée initiale admissible périodique, avec `f=0`, il existe des fonctions `u,p` lisses et périodiques sur tout `R^3 x [0,+infinity)` satisfaisant l'équation et la condition initiale.

### (C) Breakdown sur `R^3`, avec force autorisée

Il existe `nu>0`, une donnée initiale lisse, divergence-free et rapidement décroissante, ainsi qu'une force lisse rapidement décroissante, pour lesquelles aucune solution globale `u,p` satisfaisant simultanément l'équation, la lissité et la borne d'énergie demandées n'existe.

### (D) Breakdown périodique, avec force autorisée

Il existe `nu>0`, une donnée initiale lisse périodique divergence-free et une force lisse périodique admissible pour lesquelles aucune solution globale lisse et périodique demandée par l'énoncé n'existe.

Prouver l'une de (A)–(D) selon les critères du CMI constitue une réponse à l'énoncé. Un blow-up non forcé issu d'une donnée admissible réfuterait respectivement (A) ou (B), mais (C) et (D) autorisent explicitement une force.

## Notions de solution suivies

| Notion | Exigence minimale utilisée dans le laboratoire | Ce qu'elle ne garantit pas seule |
|---|---|---|
| distributionnelle faible | identité contre des fonctions test divergence-free | énergie, unicité, régularité |
| Leray–Hopf | `u in L_t^infinity L_x^2 cap L_t^2 H_x^1`, continuité faible, trace initiale et inégalité d'énergie | unicité et lissité |
| faible adaptée (*suitable*) | solution faible avec pression locale admissible et inégalité d'énergie locale | absence totale de points singuliers |
| dissipative | solution satisfaisant une inégalité d'énergie relative appropriée à la définition citée | équivalence automatique avec Leray–Hopf ou suitable |
| mild | formule de Duhamel avec semi-groupe de Stokes et projection de Leray dans un espace précisé | admissibilité Clay si la donnée ou la norme est hors cadre |
| forte | dérivées suffisantes pour interpréter l'équation presque partout et appliquer l'unicité faible-forte, dans les espaces précisés | existence globale |
| classique/lisse Clay | `u,p in C^infinity` sur tout le cylindre espace-temps, avec les conditions de décroissance ou périodicité | — |

Chaque affirmation du dépôt doit nommer la définition effectivement employée. « Solution de Navier–Stokes » sans espace, domaine et inégalité d'énergie est considéré comme incomplet.

## Énergie, pression et projection de Leray

Pour une solution classique suffisamment décroissante ou périodique,

```text
(1/2)||u(t)||_2^2 + nu integral_0^t ||nabla u(s)||_2^2 ds
 = (1/2)||u_0||_2^2 + integral_0^t <f(s),u(s)> ds.
```

En l'absence de force, le membre droit est l'énergie initiale. Une solution Leray–Hopf satisfait la version `<=` appropriée.

La pression n'est pas locale. En prenant la divergence,

```text
-Delta p = partial_i partial_j(u_i u_j) - div f.
```

La forme projetée est

```text
partial_t u + P div(u tensor u) = nu Delta u + P f,
P = I - nabla Delta^(-1) div.
```

Tout argument localisant le transport doit donc contrôler le commutateur avec `P` ou reconstruire la pression. La pression est déterminée à une constante temporelle près dans l'espace entier et à sa moyenne près sur le tore.

## Temps maximal et critères de résolution

Pour une donnée lisse admissible, la théorie locale fournit une solution classique unique sur un intervalle maximal `[0,T_*)`. Si `T_*<+infinity`, toute quantité apparaissant dans un critère de prolongement valide doit perdre sa borne à l'approche de `T_*`.

Une résolution positive exige une estimation a priori qui empêche `T_*<+infinity` pour **toute** donnée de l'alternative choisie, avec des constantes indépendantes des approximations de Galerkin, mollifications, troncatures et passages au domaine infini.

Une résolution négative exige des données exactement admissibles pour lesquelles aucune solution globale lisse demandée par (C) ou (D) n'existe. Les faits suivants ne suffisent pas :

- non-unicité de solutions faibles ;
- singularité d'une solution faible lorsqu'une branche classique pourrait encore exister ;
- donnée initiale singulière, seulement `L^2`, ou non décroissante ;
- équation forcée lorsque l'on prétend réfuter (A) ou (B) ;
- Euler (`nu=0`), système compressible, modèle moyenné/décimé ou domaine avec frontière ;
- divergence d'une discrétisation sans raccord certifié au continuum.

## Échelle

Dans `R^3`, pour `lambda>0`,

```text
u_lambda(x,t) = lambda u(lambda x,lambda^2 t),
p_lambda(x,t) = lambda^2 p(lambda x,lambda^2 t),
f_lambda(x,t) = lambda^3 f(lambda x,lambda^2 t).
```

La viscosité reste inchangée. Les facteurs de normes sont :

| Quantité | Facteur | Critique lorsque |
|---|---:|---:|
| `||u||_(L_x^q)` | `lambda^(1-3/q)` | `q=3` |
| `||u||_(L_t^p L_x^q)` | `lambda^(1-2/p-3/q)` | `2/p+3/q=1` |
| `||u||_(dot H_x^s)` | `lambda^(s-1/2)` | `s=1/2` |
| `||u||_2^2` | `lambda^(-1)` | supercritique aux petites échelles |
| `||omega||_(L_x^q)` | `lambda^(2-3/q)` | `q=3/2` |
| `||p||_(L_t^p L_x^q)` | `lambda^(2-2/p-3/q)` | `2/p+3/q=2` |

`L^3`, `dot H^(1/2)` et `BMO^(-1)` sont des cadres critiques de vitesse, mais ils ne sont pas interchangeables sans inclusions et hypothèses précises. Sur le tore fixe, la remise à l'échelle ne reste périodique que pour certains facteurs entiers et change différemment l'énergie par répétition de cellule ; toute comparaison avec `R^3` doit le signaler.

## Cadre actif du programme

Le programme suit en parallèle :

1. l'alternative (A), `R^3`, `f=0`, donnée de Schwartz ;
2. l'alternative (B), périodique, `f=0`, donnée lisse ;
3. les alternatives forcées seulement lorsqu'une source traite effectivement (C) ou (D).

Le raccord à l'une de ces quatre formulations est une arête obligatoire du graphe de preuve, jamais une convention implicite.
