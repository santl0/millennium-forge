# Cycle 0042 — équation exacte du cutoff solénoïdal mobile

Date : 2026-08-15
Statut : `AI_INTERNAL_DERIVATION`; aucun résultat Clay.

## Décision adaptative

| Action | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| conjuguer le cutoff mobile et calculer sa PDE exacte | 4 | 5 | 5 | 5 | **19** |
| borner directement la force dans un espace critique mixte | 4 | 3 | 4 | 5 | 16 |
| injecter immédiatement une famille Type II dans les constantes | 4 | 3 | 5 | 4 | 16 |

La première action est sélectionnée. Le lemme actif n'est pas une estimation
de régularité : c'est l'identité exacte qui sépare le défaut de localisation,
le drift dû au rayon mobile, la pression et les commutateurs. Le test décisif
cherche ensuite si le seul facteur `R(t)->0` rend ce défaut sous-critique.

## Cadre exact

On fixe Navier–Stokes incompressible tridimensionnel, non forcé, viscosité un,
sur `R3` :

```text
partial_t u-Delta u+(u dot nabla)u+nabla p=0,
div u=0.                                             (42.1)
```

La solution est lisse sur un intervalle ouvert `I subset (0,T_*)` dans un
voisinage de toutes les boules employées. Dans l'application conditionnelle
du cycle 0041, il s'agit de la solution de Leray–Hopf lisse avant son premier
temps singulier `T_*`, le centre est le point singulier fixe `x_*`, et

```text
R(t)=2 sqrt((T_*-t)/S_w^*(C_M M)).                  (42.2)
```

Le calcul ci-dessous vaut d'abord pour toute fonction `R in C^1(I;(0,infty))`
et un centre fixe `x_0`. Un centre mobile produirait un terme de transport
supplémentaire et n'est pas inclus.

## Opérateur unité et conjugaison

Fixons la couronne unité `A={1<|y|<2}`, un cutoff
`chi in C_c^infinity(B_2)` égal à un sur `B_1`, et

```text
a=nabla_y chi.
```

Soit `B` la réalisation linéaire support-lisse de Bogovskii du cycle 0040.
Pour un champ divergence-free lisse `W`, la moyenne de `a dot W` est nulle et
l'opérateur fixe

```text
Q W=chi W-B(a dot W)                                (42.3)
```

est divergence-free, égal à `W` dans `B_1` et nul hors `B_2`.

Avec `y=(x-x_0)/R`, posons

```text
U(y,t)=R(t)u(x_0+R(t)y,t),
P(y,t)=R(t)^2p(x_0+R(t)y,t),
Z=Q U,
C=B(a dot U).                                       (42.4)
```

L'opérateur physique est exactement

```text
B_R g(x)=R B[g(x_0+R dot)](y),
Q_R u=chi_R u-B_R(nabla chi_R dot u)=R^-1 Z(y,t).  (42.5)
```

Cette formule fixe les puissances de `R`; il ne faut pas dériver un symbole
`B_R` abstrait sans sa conjugaison.

## Dérivée exacte de Bogovskii sous homothétie

Pour `h(y,t)=g(x_0+R(t)y,t)` et `b=B_Rg`, la dérivée à `x` fixé vaut

```text
partial_t b
 =B_R(partial_t g)
  +R'[B h-y dot nabla(B h)+B(y dot nabla h)].       (42.6)
```

Toutes les entrées de `B` ont moyenne nulle. En particulier, si

```text
D W=W+y dot nabla W,
```

alors la dérivée du cutoff solénoïdal s'écrit

```text
partial_t(Q_Ru)
 =Q_R(partial_tu)+(R'/R^2)[Q,D]U.                  (42.7)
```

Le signe est important : `[Q,D]=QD-DQ`. Pour le rayon (42.2),

```text
R'/R=-1/[2(T_*-t)],
kappa=-RR'=2/S_w^*(C_M M)>0.                       (42.8)
```

Ainsi le terme mobile de (42.7) devient
`R^-3 kappa[D,Q]U`. Son coefficient est constant dans le temps remis à
l'échelle, mais dépend de la taille Type I par `S_w^*`.

## Temps renormalisé et équation de base

Définissons `sigma` par

```text
d sigma/dt=R(t)^-2,
kappa(sigma)=-R(t)R'(t).                            (42.9)
```

L'équation (42.1) devient exactement

```text
partial_sigma U-Delta U+(U dot nabla)U+nabla P
 +kappa D U=0,
div U=0.                                            (42.10)
```

Pour (42.2), `kappa` est la constante de (42.8). Cette équation est une
formulation renormalisée conditionnelle; elle ne suppose aucune convergence
de `U` lorsque `sigma->infinity`.

## Identité locale forcée exacte

Dans les variables physiques, `V=Q_Ru=R^-1Z` satisfait

```text
partial_t V-Delta V+(V dot nabla)V+nabla(chi_R p)
 =R^-3 F(y,sigma),                                  (42.11)
```

où

```text
F=
 (Z dot nabla)Z-chi(U dot nabla)U
 +P a
 +(kappa y dot a-Delta chi)U
 -2(a dot nabla)U
 -(partial_sigma-Delta+kappa D)C,                  (42.12)
C=B(a dot U).
```

La dérivation utilise

```text
(partial_sigma-Delta+kappa D)(chi U)
 =chi(partial_sigma-Delta+kappa D)U
  +(kappa y dot a-Delta chi)U-2(a dot nabla)U
```

et `-chi nabla P+nabla(chi P)=P a`. Aucun morceau de pression n'est traité
comme local avant cette identité.

Chaque terme de `F` est supporté dans la couronne unité : dans `B_1`,
`Z=U`, `C=0` et toutes les dérivées de `chi` s'annulent; hors `B_2`, tous les
champs coupés sont nuls. La force physique est donc annulaire. Elle n'est pas
nécessairement divergence-free; sa partie gradient appartient à la pression
forcée.

## Forme projetée et non-localité

Posons `H(U,P)=(U dot nabla)U+nabla P`. Ce champ est divergence-free lorsque
`P` est la pression Navier–Stokes correspondante. On peut donc appliquer `Q`
à **la somme** `H`, mais pas en général séparément à `(U dot nabla)U` et à
`nabla P`, car chacune peut violer la condition de moyenne de Bogovskii.

Avec `P_L` la projection globale de Leray, l'identité équivalente est

```text
(partial_sigma-Delta+kappa D)Z+P_L[(Z dot nabla)Z]
 =F_sol,
F_sol=P_L[(Z dot nabla)Z]-QH
      -[Delta,Q]U+kappa[D,Q]U.                     (42.13)
```

`F_sol` est divergence-free, mais `P_L[(Z dot nabla)Z]` a une queue non
locale. On ne peut donc conserver simultanément, sans calcul supplémentaire,
la force annulaire explicite de (42.12) et une force projetée compacte.

## Échelle de la force

La force physique a la loi

```text
f_R(x,t)=R^-3 F((x-x_0)/R,sigma).                  (42.14)
```

Ainsi

```text
||f_R||_L1=||F||_L1,
K_p(f_R)=R^(3/p-3)K_p(F),
||G_R||_(L^(3/2,infinity))=||G||_(L^(3/2,infinity))
pour G_R=R^-2G((x-x_0)/R).                         (42.15)
```

Les classes instantanées `L1` pour une force et
`div L^(3/2,infinity)` pour un stress sont critiques. Sur une fenêtre de
longueur `O(R^2)`, les classes `L_t^qL_x^p` critiques satisfont
`2/q+3/p=3`.

La borne Type I donne, par Calderon–Zygmund dans les espaces de Lorentz,

```text
K_(3/2)(P)<=C_CZ M^2.                              (42.16)
```

Sur la couronne de volume fixe, les termes sans dérivée non compensée de
(42.12) ont donc un budget critique dépendant de `M` et `kappa`. Mais la
seule borne faible-`L3` n'établit pas encore une estimation uniforme complète
de

```text
[Delta,Q]U et [D,Q]U                                (42.17)
```

dans une classe critique mixte. Il faut soit une estimation de commutateur de
l'opérateur support-lisse choisi, soit réécrire ces termes comme somme
`L1+div L^(3/2,infinity)` avec constantes suivies. Les bornes statiques du
cycle 0040 ne suffisent pas automatiquement à cette dérivée d'opérateur.

## Test adverse : le rayon ne fournit aucune petitesse

Un profil de plateau critique a amplitude physique `R^-1` sur une région de
volume `beta R^3`. Puisque `|partial_t chi_R|` est de taille
`|R'|/R=kappa R^-2`, le terme de frontière mobile a

```text
amplitude =kappa R^-3,
norme L1 =kappa beta,
norme faible-L1 =kappa beta,                        (42.18)
```

indépendamment de `R`. Les termes `Delta chi_R u`, `p nabla chi_R` et
`(u dot nabla chi_R)u` possèdent la même puissance de force `R^-3`.
Les termes écrits comme divergence ont un stress `R^-2` de norme
faible-`L^(3/2)` constante.

Ce ledger ne prouve pas que la **somme** (42.12) est non nulle pour toute
solution : des annulations PDE sont possibles. Il réfute néanmoins toute
inférence terme par terme

```text
R(t)->0  ==>  force de cutoff=o(1)                 (42.19)
```

fondée seulement sur le support qui rétrécit. Le calcul n'est ni une
simulation Navier–Stokes ni un passage au continuum.

## Passe contradictoire interne

1. **Opérateur dépendant du temps.** `partial_t B_Rg` n'est pas
   `B_R(partial_tg)`; le crochet de (42.6) est obligatoire.
2. **Dérivée à variable fixée.** Les dérivées à `x` fixé et à `y` fixé sont
   séparées par le générateur `D`; les confondre inverse le signe du drift.
3. **Pression.** `Q[(U dot nabla)U]+Q[nabla P]` n'est pas une écriture licite
   sans vérifier séparément deux moyennes nulles. Seule la somme `QH` est
   utilisée dans (42.13). La jauge `p->p+c(t)` déplace simultanément
   `c(t)nabla chi_R` entre force et pression; l'estimation (42.16) choisit la
   jauge globale de Riesz.
4. **Support contre projection.** La forme locale (42.11) a une force
   annulaire non solénoïdale; la forme solénoïdale (42.13) réintroduit une
   queue de Leray.
5. **Type I.** `kappa=2/S_w^*(C_MM)` est uniforme en temps mais pas universel
   en `M`; aucune limite `M->infinity` n'est autorisée.
6. **Dérivées.** La régularité avant `T_*` rend toutes les identités
   classiques à temps fixé, mais ne donne pas une borne renormalisée uniforme
   des dérivées lorsque `t->T_*`.
7. **Force critique.** Une borne critique, même démontrée, ne serait pas une
   petite force et ne fournirait pas un théorème de rigidité non forcé.
8. **Profil limite.** Aucun sous-ensemble compact de profils, aucune
   convergence forte et aucune pression limite ne sont produits.
9. **Viscosité.** Toutes les formules utilisent `nu=1`; pour `nu>0`, les
   termes de diffusion et la normalisation temporelle doivent être modifiés.
10. **Clay.** Le cutoff transforme une solution non forcée en une équation
    forcée. Sans élimination ou rigidité de cette force, il n'y a aucun
    transfert vers une solution ancienne non forcée.

## Résultat et verrou suivant

Le cutoff solénoïdal mobile possède maintenant une équation exacte, dans une
forme locale et une forme projetée. Le rayon parabolique ne rend aucun terme
sous-critique : la vitesse de la frontière compense exactement la diminution
du support. Le résultat est un progrès négatif et structurel, pas une
exclusion de blow-up.

Le verrou se précise en deux sous-gaps :

```text
GAP-TYPE-I-MOVING-COMMUTATOR-BOUND
  : borner [Delta,Q]U et [D,Q]U dans
    L1+div L^(3/2,infinity), avec constante C(M);

GAP-TYPE-I-FORCED-RIGIDITY
  : même avec cette borne, exclure ou classifier une limite ancienne
    soumise à une force annulaire critique non évanescente.
```

La prochaine expérience décisive doit choisir une réalisation intégrale
explicite de `B`, intégrer par parties dans les deux commutateurs et tester si
la norme critique mixte dépend seulement de `M`, ou si une suite
haute-fréquence à `K_3(U)<=M` la fait diverger.

## Veille différentielle du cycle

Le catalogue ajoute cinq sources primaires (`NS-SRC-0180`–`0184`) et atteint
184 entrées. Saari–Schwarzacher 2023 traite la dérivée temporelle d'un inverse
de divergence sur domaine mobile; Wolf 2017 et Kwon 2023 imposent de suivre
les composantes locales, harmoniques et projetées de la pression; Breit 2025
requiert une vitesse de bord en `L3_t`, violée par
`R'(t)~(T_*-t)^(-1/2)`; Zhang 2024 v3 concerne un blow-up **forcé** avec une
autre convention de criticité. Aucun de ces résultats ne produit une
annulation de la force complète (42.12), un lissage uniforme au collapse ou
un raccord à l'équation Clay non forcée.
