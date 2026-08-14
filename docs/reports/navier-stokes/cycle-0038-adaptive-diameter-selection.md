# Cycle 0038 — Sélection adaptative simultanée du niveau et du diamètre

Date : 2026-08-15
Statut : `AI_INTERNAL_DERIVATION`, à conserver `COMPUTATION_ONLY`
Portée : obstruction cinématique statique dans une famille pure-swirl à
supports disjoints; aucune évolution Navier–Stokes n'est construite.

## Décision adaptative

| Action | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| niveau moyen coaire et sélection endpoint au même niveau | 5 | 5 | 5 | 5 | **20** |
| arbre de fusion certifié et programmation dynamique | 4 | 4 | 5 | 4 | 17 |
| retroncature récursive avec héritage endpoint | 4 | 3 | 4 | 4 | 15 |

La première action est sélectionnée. Elle évite l'héritage faux du rapport
endpoint le long d'un arbre : le niveau est choisi par une moyenne de coaire,
puis la composante endpoint est choisie parmi les composantes actives de ce
même niveau.

## Cadre exact

Soient `R>0` et

```text
F in C_c^infinity((0,infinity) x R),
supp F subset {R/2 < r < 3R/2},
U=(R/r)F(r,z)e_theta,
W=curl U=(R/r)(-partial_z F e_r+partial_r F e_z).
```

Le champ `U` est lisse, compact et exactement divergence-free sur `R3`.
Posons, avec la convention faible-Lorentz du laboratoire,

```text
K=||U||_(L^(3,infinity))>0,
H=||W||_(L^(3/2,infinity))>0,
q=K/H.
```

La constante isopérimétrique `C_I` est fixée par
`Per_3(E)>=C_I |E|^(2/3)` pour les ensembles de périmètre fini de `R3`.

## Lemme actif : sélection adaptative one-cell

Il existe `lambda>0`, un niveau régulier
`t in (lambda/4,3lambda/8)`, un signe `sigma` et une composante active
`C_beta` de `{sigma F>t}` telle que, pour

```text
G_beta=(sigma F-t)_+ 1_(C_beta),
U_beta=(R/r)G_beta e_theta,
W_beta=curl U_beta,
K_beta=||U_beta||_(L^(3,infinity)),
H_beta=||W_beta||_(L^(3/2,infinity)),
q_beta=K_beta/H_beta,
```

on ait simultanément

```text
lambda R >= K^2/(432 H),
diam_z(C_beta)/R <= 2 239 488 q^(-3),
K_beta >= (C_I/20 736) K^2/H,
q_beta >= (C_I/20 736) q^2.
```

Une composante est dite active si elle rencontre le core signé
`{sigma F>lambda/2}`. La troncature appartient à
`W_c^(1,infinity)`; elle n'ajoute aucune mesure de curl au bord.

## Étape 1 — calibration critique du niveau

Choisissons `lambda` presque optimal avec

```text
lambda |{|U|>lambda}|^(1/3) >= K/2.
```

Notons `V` la somme des volumes tridimensionnels des deux cores signés
`{+/-F>lambda/2}`. Comme `R/r<=2`,

```text
V >= |{|U|>lambda}| >= K^3/(8 lambda^3).                 (38.1)
```

Pour chaque niveau `s in (lambda/4,lambda/2)`, les composantes actives
contiennent tout le core. Pour une composante méridienne `E` dans l'anneau,

```text
|Rot(E)| <= 3 pi R |E|_2 <= 3 pi R^2 diam_z(E).
```

Le périmètre planaire contrôle deux fois le diamètre axial. La coaire
pondérée exacte donne donc

```text
integral_(lambda/4<|F|<lambda/2) |W| dx >= lambda V/(3R). (38.2)
```

Cette bande est incluse dans `{|U|>lambda/6}`. L'intégration de la fonction
de distribution faible-`L^(3/2)` donne

```text
integral_(lambda/4<|F|<lambda/2) |W| dx <= 18HK/lambda.  (38.3)
```

La comparaison de (38.1)–(38.3) prouve

```text
lambda R >= K^2/(432H).                                  (38.4)
```

Le niveau global calibre ainsi l'échelle `R` sans supposer
`lambda R>=kappa K`.

## Étape 2 — niveau moyen à somme de diamètres bornée

Sur l'intervalle `I=(lambda/4,3lambda/8)`, de longueur `lambda/8`, la coaire
et `P_2>=2 sum diam_z` donnent

```text
integral_I sum_beta diam_z(C_beta(t)) dt
    <= 9HK/(2 pi R lambda).
```

Il existe donc un niveau régulier `t in I` tel que

```text
sum_beta diam_z(C_beta(t))/R
    <= 36HK/(pi R^2 lambda^2)
    <= (36*432^2/pi) q^(-3)
    < 2 239 488 q^(-3),                                  (38.5)
```

où la dernière constante rationnelle utilise seulement `pi>3`. En
particulier, chaque composante active au niveau choisi satisfait la même
borne de diamètre.

## Étape 3 — sélection endpoint au même niveau

Les composantes actives sont en nombre fini : le core compact est séparé du
bord `{sigma F=t}` par la marge `lambda/2-t>lambda/8`, et un recouvrement
ouvert disjoint du core admet une sous-couverture finie.

Pour chaque composante active, posons

```text
V_beta=|C_beta intersect {sigma F>lambda/2}|,
epsilon=max_beta K_beta.
```

Sur le core, `G_beta>lambda/8` et donc `|U_beta|>lambda/12`. Ainsi

```text
K_beta >= (lambda/12)V_beta^(1/3),
sum_beta V_beta^(2/3) >= lambda V/(12 epsilon).           (38.6)
```

Entre `3lambda/8` et `lambda/2`, chaque superniveau contenu dans
`C_beta` contient son core. Coaire tridimensionnelle, isopérimétrie et
`R/r>=2/3` donnent

```text
integral |W_beta| dx >= (C_I lambda/12)V_beta^(2/3).      (38.7)
```

Les supports des troncatures sont disjoints et inclus dans
`{|U|>lambda/6}`. Après sommation, (38.1), (38.6), (38.7) et la borne
Lorentz (38.3) donnent

```text
epsilon >= (C_I/20 736) K^2/H.                           (38.8)
```

La composante qui atteint `epsilon` vérifie aussi `H_beta<=H`, car
`W_beta=sigma 1_(C_beta)W` presque partout. Elle satisfait donc le rapport
quadratique annoncé. Une restriction plus fine de la borne supérieure à la
bande fixe améliore `20 736` en `13 824`; le claim conserve la constante
adversarialement auditée la plus prudente.

## Corollaire pour une famille disjointe

Appliquons d'abord la sélection cellulaire commune du cycle 0035 à une
famille de cellules pure-swirl dont les supports complets sont disjoints.
Avec `K_*`, `H_*`, `q_*=K_*/H_*` globaux et `c_H=C_I/324`, elle fournit une
cellule `j` telle que

```text
K_j >= c_H q_* K_*,
q_j >= c_H q_*^2.
```

Le lemme one-cell, avec `c_R=C_I/20 736`, fournit ensuite une composante
tronquée telle que

```text
K_beta >= c_R c_H^2 q_*^3 K_*,
q_beta >= c_R c_H^2 q_*^4,
diam_z(C_beta)/R_j
    <= 2 239 488 c_H^(-3) q_*^(-6),             (38.9)
c_R c_H^2 = C_I^3/2 176 782 336.
```

Le gate directionnel lipschitzien du cycle 0036 s'applique donc dans une
boule `O_(Lambda(q_*))(R_j)` et donne une minoration positive d'oscillation
locale dès que `q_*` est minoré. La forme sûre est
`c_(Lambda(q_*))(c_R c_H^2 q_*^4)^6`; aucune conclusion dynamique n'est
attachée à cette composition statique.

## Test adverse reproductible

Le certificat `ADAPTIVE-DIAMETER-SELECTION-1` utilise uniquement
`fractions.Fraction`. Il teste 2 016 registres de volumes cubiques
hétérogènes, jusqu'à 32 composantes, et 24 profondeurs d'un arbre abstrait.
Les constantes `432`, `20 736`, `2 239 488` et `2 176 782 336` sont vérifiées
après cubage sans tolérance flottante.

L'arbre adverse a `N=2^n` feuilles, une somme de diamètres égale à un sur la
majeure partie de la bande et un diamètre racine `N` sur une fenêtre de
largeur `1/(Nn)`. Son intégrale reste `2-1/N`. Il montre qu'une branche peut
être arbitrairement longue à persistance évanescente, mais confirme qu'une
moyenne de coaire contient toujours un niveau de petite somme de diamètres.

Une seconde réplication indépendante énumère toutes les retroncatures d'un
arbre dyadique avec endpoints faibles exacts. Elle réfute tout argument fondé
sur le seul bookkeeping merge-tree, mais ses feuilles violent le registre
de fermeture compacte
`integral|W| >= c |E|^(2/3)`; ce n'est donc pas un contre-exemple pure-swirl.

## Passe contradictoire

1. **Niveau fixé trop tôt.** Faux : le niveau est choisi après intégration,
   puis l'endpoint est sélectionné au même niveau.
2. **Rapport hérité.** Aucune monotonie de `K_u/K_w` sous retroncature n'est
   utilisée.
3. **Composantes infinies.** Seules celles rencontrant un core séparé du bord
   sont sélectionnées; elles sont en nombre fini.
4. **Mesure de bord.** La troncature a trace nulle sur la frontière de sa
   composante; sa dérivée est la restriction de `nabla F` presque partout.
5. **Volume 3D contre diamètre 2D.** Le facteur `3 pi R^2` est explicite et
   utilise la largeur radiale `R` de l'anneau.
6. **Diamètre topologique BV.** Le raisonnement emploie les superniveaux
   réguliers ouverts; la version BV devrait utiliser les représentants de
   densité un et les composantes M-indécomposables.
7. **Barcode pris pour marge de col.** Une longue barre H0 contrôle
   `maximum-col`, pas `col-cutoff`; le certificat pertinent est le niveau
   maximin avec erreur uniforme contrôlée.
8. **Ledger abstrait pris pour curl.** Le contre-arbre exact échoue au coût
   coaire de ses feuilles et n'est pas un champ admissible.
9. **Chevauchements.** `H_beta<=H` dépend de la restriction d'un champ unique;
   la sélection familiale préalable dépend encore de supports de curls
   disjoints.
10. **PDE.** Pression, projection de Leray, diffusion, stretching, temps
    maximal et compacité ne figurent pas dans le lemme.

## Scaling et portée

Sous `U_rho(x)=rho U(rho x)` et `W_rho(x)=rho^2W(rho x)`, les quantités
`K`, `H`, `q`, `lambda R`, `K^2/H`, `diam_z/R`, `K_beta/K` et `q_beta`
sont invariantes. Le lemme est exactement critique.

Le résultat ferme `GAP-BRIDGE-SCALE-CALIBRATION-OR-MERGE-TREE` pour une
cellule pure-swirl annulaire et, après sélection du cycle 0035, pour une
famille à supports complets disjoints. Il ne ferme pas la régularité de
Navier–Stokes 3D. Le prochain verrou est
`GAP-OVERLAPPING-CURL-CANCELLATION` : décider si la sélection survit lorsque
les curls de cellules se recouvrent et s'annulent avant toute fonction de
distribution locale.
