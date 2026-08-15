# Cycle 0046 — capture persistante et non-trivialité espace–temps

Date : 2026-08-15.

## Décision adaptative

Le verrou relu est `GAP-TYPE-I-CRITICAL-TRACE-PERSISTENCE`. Les trois
actions candidates ont été notées avant calcul :

| action | nouveauté | tractabilité | falsifiabilité | levier | total |
|---|---:|---:|---:|---:|---:|
| intégrer la capture à chaque temps contre la forte `L3` espace–temps | 4 | 5 | 5 | 5 | **19** |
| vérifier la persistance de singularité d'Albritton–Barker A.5 | 3 | 3 | 4 | 5 | 15 |
| construire directement un moment signé à la tranche terminale | 4 | 2 | 5 | 4 | 15 |

La première action est sélectionnée. Elle teste si le checkpoint 0045 a
confondu « trace prescrite non nulle » et « limite non triviale ». Un seul
lemme est actif : transporter le quantificateur temporel du cycle 0041 dans
la convergence forte du cycle 0045.

## Équation et classe figées

On considère sur `R3`, sans frontière, viscosité un et force nulle,

```text
partial_t u-Delta u+div(u tensor u)+nabla p=0,
div u=0.                                             (46.1)
```

Le champ `u` est une solution de Leray–Hopf d'énergie finie, lisse sur
`(0,T_*)`, dont `T_*` est le premier temps singulier et `(x_*,T_*)` un point
singulier. On suppose la borne Type I pointwise

```text
sup_(0<t<T_*) K_3(u(t);R3)<=M<infinity.              (46.2)
```

Le représentant temporel ne pose donc pas de difficulté sur `(0,T_*)` : la
solution y est classique. La pression physique est la pression globale de
Riesz, à une fonction du temps près.

Après le zoom mobile et le cutoff externe des cycles 0042–0044, la suite
`Z_j` satisfait sur une fenêtre finie `I=[-S,0]`

```text
partial_s Z_j-Delta Z_j+div(Z_j tensor Z_j)+nabla Pi_j
  +kappa(1+y dot nabla)Z_j=F_j,
div Z_j=0,                                           (46.3)
```

où `kappa=2/S_w^*(C_MM)>0`, `Pi_j=R_aR_b(Z_(j,a)Z_(j,b))`,
`F_j->0` dans `C-infinity_x,loc` uniformément en temps, et `Z_j` est
classique. Le cycle 0045 donne, après extraction,

```text
Z_j->Z fortement dans L3(I x B_R)                   (46.4)
```

pour chaque `R<infinity`, et `Z` est faible adaptée locale pour l'équation
renormalisée non forcée.

## Horloge exacte et transport de la capture

Posons

```text
a=4/S_w^*(C_MM),
R(t)^2=a(T_*-t),
d sigma/dt=R(t)^(-2),
kappa=a/2.                                           (46.5)
```

La règle de chaîne donne exactement

```text
d(log R)/d sigma
 =[-1/(2(T_*-t))] R^2
 =-a/2=-kappa,                                      (46.6)
```

donc, pour toute translation `sigma_j+s`,

```text
R(sigma_j+s)/R(sigma_j)=exp(-kappa s).              (46.7)
```

Une fenêtre fixe en `s` ne se contracte donc pas. Pour `j` assez grand, elle
correspond entièrement à des temps physiques dans `(0,T_*)`; le rapport des
rayons y reste entre deux constantes dépendant seulement de `S` et `kappa`.

Le théorème 2 de Barker–Prange, avec son extension faible-`L3` de
l'appendice B, donne au point singulier fixe, pour **tout** `0<t<T_*`,

```text
K_3(u(t);B(x_*,R(t)))>gamma_w.                      (46.8)
```

Le quantificateur est « tout temps », et non une suite de temps. La loi
critique donne exactement

```text
K_3(R(t)u(x_*+R(t) dot,t);B_1)
 =K_3(u(t);B(x_*,R(t))).                             (46.9)
```

Enfin `Q_(L_j)` est l'identité dans `B_(L_j)` et `L_j->infinity`. Ainsi,
pour tout `j` assez grand et tout `s in I`, ou seulement presque tout `s`
si l'on choisit un représentant faible,

```text
K_3(Z_j(s);B_1)>gamma_w.                            (46.10)
```

Il n'est requis ni propagation nouvelle de la singularité, ni sélection
d'un temps dépendant de `j`, ni test signé.

## Lemme actif

Pour toute fonction mesurable `f` sur `B_1`, la définition par fonctions de
répartition donne

```text
K_3(f;B_1)^3<=integral_(B_1)|f|^3.                  (46.11)
```

En intégrant (46.10) sur `I`,

```text
integral_I integral_(B_1)|Z_j|^3
 >=|I| gamma_w^3.                                   (46.12)
```

La convergence forte (46.4) entraîne la convergence des normes `L3` sur ce
cylindre. Par conséquent,

```text
integral_I integral_(B_1)|Z|^3
 >=|I| gamma_w^3>0.                                 (46.13)
```

La limite renormalisée est donc non nulle. Sur des fenêtres
`[-S,0]` croissantes, la même sous-suite diagonale produit une solution
ancienne renormalisée non triviale sur `R3 x (-infinity,0]`.

De plus, (46.13) fournit un temps de Lebesgue `s_* in (-S,0)` tel que
`Z(s_*)` soit une distribution non nulle. La continuité
`Z in C(I;H^-1_loc)` identifie cette tranche avec le représentant compact du
cycle 0045. Comme (46.3) est autonome, une translation en `s` suivie d'une
restriction permet de placer cette tranche en zéro. Elle fournit donc une
trace renormalisée non nulle, mais pas nécessairement la trace correspondant
à l'ancien endpoint `s=0` de la suite initiale.

## Passe adverse indépendante

Le certificat exact et le contre-audit séparent cinq frontières.

1. Une capture à un seul temps a mesure nulle et reste invisible à `L3`
   espace–temps.
2. Si la longueur capturée est `delta_j` et la taille `gamma_j`, le seuil
   optimal est `delta_j gamma_j^3`; la conclusion échoue lorsque ce produit
   tend vers zéro.
3. Un profil spatial à un niveau atteint l'égalité dans (46.11) : aucune
   constante strictement meilleure que un n'est disponible.
4. Un centre ou une échelle mobiles ne diminuent pas le coût par tranche
   tant que la minoration est réellement formulée dans le même `B_1`.
5. Une borne supérieure faible-`L3` ne majore toujours pas la norme forte
   `L3`; seule la minoration (46.10) est utilisée ici.

Le script vérifie aussi en arithmétique rationnelle (46.5)–(46.6) et
l'invariance critique (46.9). Il ne simule pas Navier–Stokes et ne certifie
pas les ingrédients PDE publiés ou dérivés aux cycles antérieurs.

## Correction du graphe et portée Clay

`FAIL-NS-0081` reste exact pour une minoration portée par une tranche isolée.
Sa réparation par un moment signé n'est toutefois pas nécessaire dans la
suite Type I réelle, parce que (46.8) fournit une capture sur tout intervalle
renormalisé de mesure positive. Le gap
`GAP-TYPE-I-CRITICAL-TRACE-PERSISTENCE` est donc fermé dans cette branche et
doit être remplacé par l'horloge inverse exacte.

Ce résultat est conditionnel à l'existence d'un premier blow-up Type I avec
borne globale faible-`L3`. Il ne couvre pas Type II, ne construit pas de
blow-up, ne prouve aucune rigidité de la limite, ne dérenormalise pas encore
la solution avec drift, et ne résout aucun cas de l'énoncé Clay.

Le prochain lemme décisif est : pour une solution faible adaptée ancienne de
(46.3), vérifier avec toutes les puissances que

```text
R(s)=exp(-kappa s),
dt/ds=R(s)^2,
u(x,t(s))=R(s)^(-1)Z((x-x_*)/R(s),s)                (46.14)
```

transporte distributions, pression et inégalité d'énergie locale vers une
solution ancienne standard non forcée sur `R3`, puis identifier exactement
la classe obtenue. Aucun théorème de rigidité ne sera appliqué avant ce
raccord.

## Reproduction

~~~powershell
python -B experiments/navier-stokes/trace-persistence/trace_persistence_audit.py
~~~

La veille différentielle primaire et les deux revues indépendantes du cycle
sont consignées dans `docs/reports/navier-stokes/reviews/`.
