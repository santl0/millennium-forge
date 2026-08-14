# Cycle 0040 — cutoff solénoïdal annulaire du champ total

Date : 2026-08-15
Statut : `AI_INTERNAL_DERIVATION`; aucun résultat Clay.
Portée : localisation cinématique statique, indépendante de tout axe.

## Décision adaptative

| Action | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| correcteur de Bogovskiĭ sur une couronne fixe | 3 | 5 | 5 | 5 | **18** |
| minoration directe après projection globale de Leray | 4 | 3 | 5 | 4 | 16 |
| deux swirls à axes distincts et matrice de Gram numérique | 5 | 2 | 5 | 4 | 16 |

La première action est sélectionnée. Elle demande le premier raccord vraiment
intrinsèque depuis le champ total : construire un champ compact
divergence-free qui coïncide avec lui dans une boule, sans décomposition en
cellules et avec un coût critique explicite dans la couronne.

## Cadre exact

Le problème de référence reste Navier–Stokes incompressible non forcé sur
`R3`, viscosité `nu>0`, donnée initiale lisse compacte divergence-free. Le
lemme actif porte seulement sur un champ statique

```text
U in C_c^infinity(R3;R3), div U=0, W=curl U.
```

Pour `p>0`, la convention est

```text
K_p(f)=sup_(s>0) s |{|f|>s}|^(1/p).
```

Fixons une fois pour toutes `chi_0 in C_c^infinity(B_2)`,
`0<=chi_0<=1`, `chi_0=1` sur `B_1`, constante près des deux bords de la
couronne, et posons

```text
C_chi=||grad chi_0||_infinity,
chi_(x0,R)(x)=chi_0((x-x0)/R),
A_(x0,R)=B(x0,2R) minus closure(B(x0,R)),
c_A=|B_2 minus B_1|=28pi/3.
```

Le domaine annulaire a une forme fixe. Toute constante géométrique ci-dessous
est donc indépendante de `x0` et `R`; elle n'est pas uniforme pour une
couronne dont le rapport des rayons ou l'aspect dégénère.

## Lemme actif — localisation solénoïdale critique

Notons

```text
K_core=K_3(1_(B(x0,R)) U),
G_col=K_3(1_(A_(x0,R)) U),
H_out=K_(3/2)(1_(B(x0,2R)) W).
```

Soit `C_B` la norme d'un inverse de Bogovskiĭ fixé sur la couronne unité,
prolongé à `L^(3/2,infinity)` par interpolation entre deux exposants forts :

```text
K_(3/2)(grad B_A g) <= C_B K_(3/2)(g),
integral_A g=0.
```

Pour la conclusion lisse, on fixe en plus une réalisation régularisée qui
envoie `C_(c,0)^infinity(A)` dans `C_c^infinity(A;R3)`. Sans cette propriété
de support lisse, les identités et estimations ci-dessous restent valides pour
le prolongement dans `W_c^(1,(3/2,infinity))`, mais la seule trace nulle ne
justifie pas `C_c^infinity` après prolongement par zéro.

Alors il existe `V in C_c^infinity(B(x0,2R);R3)` tel que

```text
div V=0,
V=U sur B(x0,R),
K_3(V)>=K_core,                                      (40.1)
K_(3/2)(curl V)
 <=3[H_out+C_chi c_A^(1/3)(1+sqrt(2)C_B)G_col].     (40.2)
```

En particulier, si `K_core>0`,

```text
K_3(V)/K_(3/2)(curl V)
 >=K_core/{3[H_out+C_chi c_A^(1/3)
                    (1+sqrt(2)C_B)G_col]}.          (40.3)
```

La constante `3` vient directement de la convention de quasi-norme par
fonctions de distribution; elle n'est pas absorbée dans un changement de
norme de Lorentz.

## Preuve du défaut de divergence et de sa compatibilité

Posons `chi=chi_(x0,R)` et

```text
g=div(chi U)=grad chi dot U.
```

Le champ `chi U` est compact, donc

```text
integral_(R3) g=integral_(R3) div(chi U)=0.          (40.4)
```

Comme `grad chi` est compactement supporté dans la couronne, `g` appartient à
`C_c^infinity(A_(x0,R))` et sa moyenne sur cette couronne est nulle. La seule
condition de compatibilité du problème de divergence à trace nulle est donc
satisfaite. Un opérateur de Bogovskiĭ à support contrôlé donne

```text
b=B_A g, div b=g, supp b subset A_(x0,R).
```

La réalisation support-lisse fixée ci-dessus donne `b in C_c^infinity(A)`.
Une solution arbitraire à trace nulle ne suffirait qu'au niveau Sobolev.

Définissons

```text
V=chi U-b.                                           (40.5)
```

Alors `div V=0`, `V=U` dans la boule intérieure et `V=0` hors de la boule
extérieure. L'identité du curl est exacte :

```text
curl V=chi W+grad chi cross U-curl b.                (40.6)
```

Il n'y a ni pression, ni projection implicite, ni terme omis.

## Passage endpoint et constantes

La couronne unité est un domaine Lipschitz fixe. Choisissons par exemple
`p_0=4/3` et `p_1=2`. Le même opérateur linéaire de Bogovskiĭ est borné de
`L_0^(p_i)` vers `W_0^(1,p_i)` pour `i=0,1`. L'interpolation réelle à
`theta=1/3` donne l'opérateur endpoint

```text
L_0^(3/2,infinity) -> W_0^(1,(3/2,infinity)).        (40.7)
```

Cette étape utilise un opérateur unique aux deux exposants. Elle ne suit pas
d'une simple existence séparée pour chaque `p`.

Pour toute fonction `f` supportée dans un ensemble `E` de mesure finie,

```text
K_(3/2)(f)<=|E|^(1/3)K_3(f).                         (40.8)
```

En effet, sa fonction de distribution est majorée simultanément par `|E|` et
`(K_3(f)/s)^3`; le maximum est atteint au point de croisement. Ainsi

```text
K_(3/2)(g)
 <=(C_chi/R)|A_(x0,R)|^(1/3)G_col
 =C_chi c_A^(1/3)G_col.                              (40.9)
```

Avec la norme euclidienne/Frobenius,

```text
|curl b|<=sqrt(2)|grad b|.                           (40.10)
```

Les trois termes de (40.6) vérifient, directement par l'inclusion des
superniveaux à seuil `s/3`,

```text
K_(3/2)(f_1+f_2+f_3)<=3 sum_i K_(3/2)(f_i).         (40.11)
```

Les équations (40.9)–(40.11) donnent (40.2). Enfin `V=U` dans le core, donc
chaque superniveau du core est inclus dans celui de `V`; ceci donne (40.1).

## Absorption par le curl global

Pour un champ compact divergence-free sur `R3`, Biot–Savart et le potentiel
de Riesz d'ordre un donnent la borne faible de Sobolev

```text
K_3(U)<=C_BS K_(3/2)(W).                              (40.12)
```

En posant `K_global=K_3(U)` et `H_global=K_(3/2)(W)`, on a donc
`G_col<=C_BS H_global` et `H_out<=H_global`. L'équation (40.2) implique

```text
K_(3/2)(curl V)<=C_loc H_global,
C_loc=3[1+C_chi c_A^(1/3)(1+sqrt(2)C_B)C_BS],        (40.13)
```

Pour tout champ `F` dont les deux quasi-normes sont finies et dont le
dénominateur est non nul, posons

```text
q(F)=K_3(F)/K_(3/2)(curl F).
```

Si `K_global>0` et `H_global>0`, on obtient alors

```text
q(V)>=C_loc^-1 (K_core/K_global) q(U).                (40.14)
```

Le premier quantificateur encore manquant n'est donc pas l'existence du
correcteur : c'est la sélection, à une échelle géométriquement pertinente,
d'une boule vérifiant `K_core>=alpha K_global` avec `alpha>0` uniforme.

## Scaling Clay

Sous

```text
U_rho(x)=rho U(rho x), W_rho(x)=rho^2 W(rho x),
R_rho=R/rho,
```

les trois quantités `K_core`, `G_col`, `H_out`, la norme du champ localisé et
la norme de son curl sont invariantes. Le facteur `R^-1` du gradient de cutoff
est exactement compensé par l'inclusion de support
`L^(3,infinity)->L^(3/2,infinity)` sur un volume `O(R^3)`.

Le coût du col est donc **critique**, jamais sous-critique par le seul choix
de `R`.

## Barrière des couronnes minces

La forme fixe est essentielle. Sur

```text
A_(R,h)={R<|x|<R+h}, 0<h<=R,
```

pour tout `1<p<infinity`, dans l'échelle forte `L^p`,
la norme de tout inverse droit
`T: L_0^p(A_(R,h))->W_0^(1,p)(A_(R,h))` de la divergence vérifie

```text
||T|| >= c_p R/h.                                    (40.15)
```

En effet, prendre `q(x)=x_1/|x|`, de moyenne nulle. Sa dérivée tangentielle
vérifie `||grad q||_(p')<=C_p R^-1||q||_(p')`. Pour
`v in W_0^(1,p)` la Poincaré radiale donne
`||v||_p<=C_p h||grad v||_p`; par intégration par parties,

```text
|integral q div v|
 <=C_p(h/R)||q||_(p')||grad v||_p.                   (40.16)
```

Choisir le dual impair de `q`, qui est encore de moyenne nulle, puis
`v=Tg`, donne (40.15). Ainsi réduire l'épaisseur du col n'achète pas un petit
coût : cela détériore au contraire la constante du correcteur comme `R/h`.
Cette minoration n'est pas revendiquée ici dans la quasi-norme faible
`L^(3/2,infinity)` : un tel énoncé demanderait une dualité
`L^(3/2,infinity)`--`L^(3,1)` et une Poincaré--Lorentz suivies séparément.

## Ce que le lemme ferme

1. La construction part du champ total après toutes les annulations.
2. Elle est indépendante d'un axe, d'une symétrie ou d'une décomposition.
3. Elle conserve exactement le champ dans le core.
4. Elle produit un champ compact divergence-free sans queue de Leray.
5. Toutes les constantes sont uniformes par translation et dilatation d'une
   couronne de rapport fixé.

Elle ferme donc le sous-gap `GAP-MULTIAXIS-SOLENOIDAL-CUTOFF`.

## Ce que le lemme ne ferme pas

1. Rien ne sélectionne encore une boule où `K_core` capture une fraction du
   numérateur global à une échelle intrinsèque.
2. Le terme de col n'a aucune petite constante : un plateau de vitesse dans
   toute la couronne sature (40.8).
3. `C_B` est suivi symboliquement mais pas évalué numériquement pour la
   couronne choisie.
4. La correction peut modifier la direction du curl dans la couronne.
5. Aucune pression associée à l'évolution issue de `V` n'est estimée.
6. Aucune relation avec un rayon pré-singulier `R(t)->0` n'est obtenue.

Le nouveau verrou est donc
`GAP-WEAK-L3-CORE-CAPTURE-AT-PRESINGULAR-SCALE`, pas la simple existence d'un
cutoff divergence-free. Sans contrainte sur `R`, une boule assez grande
capture trivialement tout champ compact; le quantificateur utile exige que
`R` appartienne à une gamme dictée par la concentration et tende vers zéro
dans un scénario pré-singulier. Si l'on interdit l'absorption globale (40.12)
et exige un dénominateur purement local, le contrôle séparé du col reste aussi
nécessaire.

## Test adverse décisif

Le test fini doit supprimer toute racine en cubant les quasi-normes. Sur une
couronne abstraite de volume `beta R^3`, plaçons une vitesse de taille `a/R`
sur une fraction `theta`. Alors

```text
K_3(U)^3=a^3 beta theta,
K_(3/2)((C_chi/R)U)^3=C_chi^3 a^3(beta theta)^2,
[C_chi beta^(1/3)K_3(U)]^3
 =C_chi^3 a^3 beta^2 theta.                          (40.17)
```

Le résidu de (40.8) cubée est

```text
C_chi^3 a^3 beta^2 theta(1-theta)>=0.                (40.18)
```

Il s'annule pour `theta=1`. Cette famille plateau démontre que le coût
`O(G_col)` de (40.2) est optimal en échelle et ne peut être remplacé par
`o_R(1)G_col` à partir des seuls endpoints.

Cette saturation possède aussi un raccord divergence-free spatial. Fixons un
vecteur constant non nul `c`, un cutoff `phi` égal à un sur `B_2` et nul hors
`B_3`, puis posons

```text
A(x)=(1/2)c cross x,
U_1=curl(phi A).
```

Alors `U_1` est lisse, compact, divergence-free et vaut exactement `c` dans
`B_2`. La famille Clay

```text
U_R(x)=R^-1 U_1((x-x0)/R)
```

est constante dans chaque couronne active. Le terme
`grad chi_R cross U_R` est la remise à l'échelle critique d'un champ fixe non
nul; sa quasi-norme faible-`L^(3/2)` est indépendante de `R`. Ainsi aucune
amélioration `o_R(1)` n'est possible même dans la classe lisse compacte
divergence-free. Le ledger atomique vérifie la constante d'inclusion; cette
famille fournit séparément le raccord spatial.

Le certificat exécute en outre seize profils étagés rationnels, aux rayons
`R=2^-m`, `0<=m<=64`, ainsi que le plateau pour
`2^-40<=R<=2^80`. Il vérifie 9 167 assertions `Fraction`, sans tolérance
flottante, et obtient un résidu arithmétique nul. Son empreinte est
`510be7b9354f6e18a188afd87bbec510ecde01d97e187671fe6334c2529ba6e5`.
Il ne certifie ni l'opérateur de Bogovskiĭ ni un résidu PDE.

## Passe contradictoire interne

1. **Moyenne nulle.** Elle est calculée sur `div(chi U)` compact, pas supposée
   depuis un flux local informel.
2. **Topologie de la couronne.** Le problème `div b=g` à trace nulle exige la
   moyenne nulle, pas la trivialité du premier groupe d'homologie. Les
   constantes dépendent toutefois de cette géométrie fixe.
3. **Endpoint faible.** Il vient de l'interpolation d'un même opérateur entre
   deux exposants forts; une preuve uniquement à `p=3/2` fort serait
   insuffisante.
4. **Support.** Le correcteur de Bogovskiĭ est choisi à support dans la
   couronne; la projection globale de Leray n'aurait pas cette propriété.
5. **Numérateur.** La minoration utilise seulement l'égalité `V=U` dans le
   core, jamais une borne inférieure fausse pour le projecteur de Leray.
6. **Quasi-triangle.** Le facteur trois est conservé explicitement.
7. **Dégénérescence.** Aucune uniformité n'est revendiquée si la couronne
   devient mince, longue ou perforée autrement.
8. **PDE.** `V` est une donnée admissible lisse; ce n'est pas une solution au
   même instant d'une évolution donnée et aucune pression n'est transportée.

## Résultat et prochain verrou

Le cutoff solénoïdal du champ total est disponible avec une constante critique
uniforme sur les boules homothétiques. Le prix exact est un budget de curl
extérieur plus un budget de vitesse dans la couronne; Biot–Savart les absorbe
dans le curl global. Le prochain cycle doit soit sélectionner intrinsèquement,
à une échelle liée à la concentration, une boule vérifiant

```text
K_core >= alpha K_global,
```

à partir d'une hypothèse globale pertinente, soit construire un champ lisse
multi-échelle pour lequel ce quotient tend vers zéro sur toute boule de la
gamme candidate.
