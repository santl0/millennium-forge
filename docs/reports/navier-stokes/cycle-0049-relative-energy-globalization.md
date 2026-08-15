# Cycle 0049 — globalisation de l'énergie relative faible-`L3`

Date : 2026-08-15.

## Décision adaptative

Le verrou relu est `GAP-TYPE-I-RELATIVE-ENERGY-GLOBALIZATION`. Trois actions
ont été notées avant la dérivation :

| action | nouveauté | tractabilité | falsifiabilité | levier | total |
|---|---:|---:|---:|---:|---:|
| globaliser l'inégalité relative par cutoffs et pression de Riesz | 4 | 4 | 5 | 5 | **18** |
| obtenir la dissipation par régularité maximale du Duhamel | 3 | 2 | 5 | 4 | 14 |
| identifier la solution à une solution BSS construite séparément | 2 | 1 | 4 | 4 | 11 |

La première action est sélectionnée. Le lemme actif est borné : sur une
bande forward finie, promouvoir le correcteur `C_tL2` du cycle 0048 vers le
correcteur énergétique de Barker--Seregin--Šverák (BSS), sans invoquer une
unicité à grande donnée.

## Cadre exact

Soit `I=[t_0,t_1]`, `H=t_1-t_0<infinity`. Sur
`R3 x I`, sans frontière, force nulle et viscosité un, on suppose

```text
partial_t v-Delta v+div(v tensor v)+nabla q=0,
div v=0,
q=R_iR_j(v_i v_j),
ess sup_(t in I)||v(t)||_(L^(3,infinity))<=M.       (49.1)
```

La paire `(v,q)` est faible adaptée locale. Le cycle 0048 donne un
représentant `C_w*L^(3,infinity)`, la trace solénoïdale
`a=v(t_0) in L^(3,infinity)`, puis

```text
V(t)=S(t-t_0)a,
w(t)=v(t)-V(t),
w in C(I;L2),
||w(t)||_2<=C_0 M²(t-t_0)^(1/4).                  (49.2)
```

La forte continuité locale de `S(h)a` dans `L2` et (49.2) donnent aussi la
trace locale forte de `v` au temps `t_0`. La suitability peut donc être
intégrée à partir de ce redémarrage intérieur de la solution ancienne.

## Lemme de croissance locale

Pour `R>=sqrt(H)` et une constante dépendant seulement de `M`, des
conventions Lorentz et des cutoffs fixes,

```text
sup_(t in I) integral_(B_(8R)) |v(t)|²
 + integral_I integral_(B_(4R)) |nabla v|² <= C_M R,

sup_(t in I) integral_(B_(8R)) |V(t)|²
 + integral_I integral_(B_(4R)) |nabla V|² <= C_M R,

integral_I integral_(B_(4R)) |nabla w|² <= C_M R. (49.3)
```

La première ligne est la Caccioppoli adaptée du cycle 0045 remise à
l'échelle : faible-`L3` donne
`integral_(B_R)|v|²<=C M²R`, la pression de Riesz est uniformément dans
faible-`L^(3/2)`, et le cylindre temporel normalisé a longueur
`H/R²<=1`. La seconde est l'inégalité d'énergie locale du flot calorique,
avec la même borne locale de la donnée. La troisième suit de
`nabla w=nabla v-nabla V`.

Cette croissance linéaire est locale. Elle ne suppose pas la conclusion
globale `nabla w in L2(I x R3)`.

## Inégalité d'énergie relative locale

Posons `e=|w|²/2`. Pour `tau>t_0`, le fond `V` est lisse et `w` appartient à
la classe énergétique sur tout compact. Soustraire de l'inégalité locale de
`v` l'identité calorique de `V` et l'identité croisée `v dot V` donne, au
sens des distributions,

```text
partial_t e-Delta e+|nabla w|²
 +div(e v+q w)
 + (w tensor w):nabla V
 + (V dot nabla V) dot w <=0.                    (49.4)
```

Le point délicat est l'absence de flux pur en `V`. Dans le calcul brut,
`(v tensor v):nabla V` apparaît. Les deux termes

```text
(V tensor V):nabla V=div(|V|²V/2),
(V tensor w):nabla V=div(|V|²w/2)                (49.5)
```

annulent exactement le flux `-|V|²v/2` issu de la soustraction. Omettre
(49.5) laisse un terme cubique calorique endpoint qui n'est pas globalement
intégrable et fausse la globalisation.

Sous forme intégrée, pour toute fonction test positive `phi`, (49.4) donne

```text
integral e(t)phi(t)+integral_tau^t integral |nabla w|²phi
 <= integral e(tau)phi(tau)
   +integral_tau^t integral e(partial_t phi+Delta phi)
   +integral_tau^t integral (e v+q w) dot nabla phi
   -integral_tau^t integral
      [(w tensor w):nabla V+(V dot nabla V) dot w]phi.     (49.6)
```

## Intégrabilité au temps de redémarrage

Les estimations calorifiques faible-Lorentz, pour `h=t-t_0>0`, sont

```text
||V(h)||_infinity <= C M h^(-1/2),
||nabla V(h)||_infinity <= C M h^(-1),
||V(h)||_4 <= C M h^(-1/8),
||nabla V(h)||_4 <= C M h^(-5/8).                (49.7)
```

Combinées avec (49.2), elles donnent les deux majorants exacts

```text
integral |w|²|nabla V|
 <= C M^5 h^(-1/2),

integral |V||nabla V||w|
 <= C M^4 h^(-1/2).                              (49.8)
```

Les sources de (49.4) sont donc dans `L1(I)` jusqu'à `t_0`. Le premier
coefficient de Grönwall potentiel n'est pas `h^-1` : le taux fort
`||w(h)||_2²=O(h^(1/2))` le transforme en `h^-1/2` intégrable.

## Cutoffs spatiaux et flux sans pression

Soit `chi_R(x)=chi(x/R)`, radiale, égale à un sur `B_R`, supportée dans
`B_(2R)`, avec

```text
|nabla chi_R|<=C/R,
|Delta chi_R|<=C/R².                              (49.9)
```

Le terme de Laplacien vérifie

```text
integral_I integral e|Delta chi_R|
 <= C H R^-2 sup_I||w||_2² ->0.                  (49.10)
```

Le flux mixte est lui aussi négligeable :

```text
R^-1 integral_I integral_(A_R)|w|²|V|
 <= C R^-1 integral_0^H ||V(h)||_infinity||w(h)||_2² dh
 <= C_(M,H) R^-1.                                (49.11)
```

Pour le flux cubique, la Gagliardo--Nirenberg localisée et (49.3) donnent

```text
R^-1 integral_I integral_(A_R)|w|³
 <= C R^-1 E_*^(3/4) H^(1/4)
      [integral_I integral_(B_(4R))|nabla w|²
       +H R^-2 E_*]^(3/4)
 <= C_(M,H,E_*) R^(-1/4),                        (49.12)
```

où `E_*=sup_I||w||_2²<infinity`. Cette estimation utilise la croissance
locale linéaire, pas une dissipation globale déjà supposée.

## Pression de Riesz

La jauge globale permet la décomposition exacte

```text
q=q_(ww)+q_(Vw)+q_(VV),
q_(ww)=R_iR_j(w_iw_j),
q_(Vw)=R_iR_j(V_iw_j+w_iV_j),
q_(VV)=R_iR_j(V_iV_j).                           (49.13)
```

Les deux parties contenant `V` sont globalement dans `L2` :

```text
||q_(Vw)||_2<=C||V||_infinity||w||_2,
||q_(VV)||_2<=C||V||_4².                         (49.14)
```

Ainsi leur flux contre `w nabla chi_R` est `O(R^-1)` et temporellement
intégrable jusque `t_0`; les puissances de `h` s'annulent grâce à (49.2).

Pour `q_(ww)`, sur l'anneau `A_R={R<|x|<2R}`, écrivons

```text
q_(ww)=R_iR_j(1_(B_(4R))w_iw_j)
       +R_iR_j(1_(R3\B_(4R))w_iw_j)
       =q_near+q_far.                            (49.15)
```

Calderón--Zygmund et le même ledger que (49.12) donnent

```text
R^-1 integral_I integral_(A_R)|q_near||w|
 <=C R^-1 integral_I ||w||_(L3(B_(4R)))³
 <=C R^(-1/4).                                   (49.16)
```

Pour `x in A_R`, la partie lointaine satisfait

```text
|q_far(x,t)|<=C R^-3||w(t)||_2²,

R^-1 integral_I integral_(A_R)|q_far||w|
 <=C H E_*^(3/2)R^(-5/2).                       (49.17)
```

Les puissances `R^-1/4` et `R^-5/2` sont strictement positives. La pression
non locale n'est ni supprimée ni remplacée par une pression locale modulo
une fonction du temps.

## Fermeture coercive retenue après les audits

La passe analytique indépendante fournit une route plus directe que la
séparation (49.12)--(49.17), et c'est elle qui est retenue pour le claim.
Avec `phi_R=chi_R²`, l'identité croisée donne exactement

```text
(1/2) integral phi_R|w(t)|²
 +integral_delta^t integral phi_R|nabla w|²
 <=(1/2) integral phi_R|w(delta)|²
   +(1/2) integral_delta^t integral |w|² Delta phi_R
   +integral_delta^t integral phi_R
       (V tensor w+V tensor V):nabla w
   +integral_delta^t integral F dot nabla phi_R,          (49.17a)

F=((v dot w)-|w|²/2)v+q w.
```

Posons `G=|v|²+|V|²+|q|`. La borne globale de Riesz donne
`||G||_(L^(3/2,infinity))<=CM²`. Sur l'anneau `A_R`,

```text
||G||_(L^(6/5)(A_R))<=C M² R^(1/2),
||chi_R w||_6<=C||nabla(chi_R w)||_2,

|integral F dot nabla phi_R|
 <=C M²R^(-1/2)||nabla(chi_R w)||_2
 <=epsilon||chi_R nabla w||_2²
   +C_epsilon M^4/R+C R^-2||w||_2².              (49.17b)
```

Les termes intérieurs sont absorbés à rayon fini par
Gagliardo--Nirenberg et Young :

```text
|integral phi_R(V tensor w):nabla w|
 <=epsilon||chi_R nabla w||_2²
   +C_epsilon||V||_4^8||w||_2²
   +o_R(1),

|integral phi_R(V tensor V):nabla w|
 <=epsilon||chi_R nabla w||_2²+C_epsilon||V||_4^4. (49.17c)
```

Les deux restes temporels valent `O(h^-1/2)` par (49.2) et (49.7). Après
absorption, Fatou et `R->infinity`, cette première passe construit
`nabla w in L2` sans la supposer. Elle évite la borne plus grossière
`CM||nabla w||_2²`, non absorbable à grande donnée, relevée par l'audit
bibliographique. Le petit coefficient est `epsilon`, tandis que la grande
norme `M` est reléguée dans un terme source intégrable.

## Passage `R->infinity`, puis `tau->t_0`

La première passe (49.17a)--(49.17c), puis `delta->t_0`, prouve d'abord

```text
w in L-infinity(I;L2) inter L2(I;Hdot1).          (49.19)
```

On revient ensuite à l'inégalité locale non majorée. La dissipation globale
rend maintenant les termes intérieurs absolument intégrables et les flux de
bord tendent vers zéro. Pour presque tout `t` et tout `tau>t_0`, on obtient

```text
(1/2)||w(t)||_2²+integral_tau^t||nabla w||_2²
 <=(1/2)||w(tau)||_2²
   -integral_tau^t integral
      [(w tensor w):nabla V+(V dot nabla V) dot w].       (49.18)
```

La limite `tau decreases to t_0` utilise (49.2), (49.7) et les majorants
intégrables de (49.17c). L'inégalité obtenue d'abord pour presque tout `t`
s'étend à tout `t in I`
par la forte continuité `w in C_tL2`, l'absolue continuité des sources de
(49.8) et la monotonie de l'intégrale de dissipation.

Après (49.19), les intégrations par parties globales sont légitimes et

```text
-integral (w tensor w):nabla V
 =integral (V tensor w):nabla w,

-integral (V dot nabla V) dot w
 =integral (V tensor V):nabla w.                 (49.20)
```

En multipliant (49.18) par deux,

```text
||w(t)||_2²+2 integral_(t_0)^t||nabla w||_2²
 <=2 integral_(t_0)^t integral_R3
      (V tensor w+V tensor V):nabla w.           (49.21)
```

C'est exactement l'inégalité d'énergie perturbée globale de la définition
BSS, avec `w(t)->0` fortement dans `L2` au temps initial. L'inégalité locale
de la paire complète est déjà une hypothèse. Sur toute bande finie, la sortie
du cycle 0048 appartient donc à la classe globale faible `L^(3,infinity)`
scindée de BSS.

## Passe contradictoire principale

1. `w in C_tL2` seul ne donne pas (49.3); la suitability locale, la pression
   de Riesz et la borne critique de `v` fournissent la croissance linéaire.
2. Tester directement par `w` avant (49.19) serait circulaire; tous les tests
   sont compacts jusqu'au passage `R->infinity`.
3. Le terme pur `V³` disparaît seulement après l'identité exacte (49.5).
4. La partie `q_(ww)` n'est pas estimée globalement dans `L^(3/2)` avant la
   dissipation; elle est scindée en Riesz proche et queue lointaine.
5. La constante de Calderón--Zygmund est indépendante de `R`; la croissance
   locale est exactement `O(R)`, ce qui laisse le résidu `R^-1/4`.
6. Le passage `tau->t_0` utilise le taux `h^(1/4)`, pas la seule trace faible.
7. La classe BSS n'impose pas à elle seule `v in C_tL^(3,infinity)` en norme,
   la bornitude spatiale ou l'unicité à grande donnée.
8. Aucun Liouville KNSS/Albritton--Barker ne s'applique encore.
9. La branche reste conditionnelle au scénario Type I; aucune constante
   n'est uniforme lorsque la borne Type I diverge.
10. Le résultat ne construit aucune singularité terminale et ne traite pas
    le cas périodique Clay.
11. BSS et Albritton--Barker ne sont pas cités comme prouvant la promotion
    dissipative : leurs définitions la supposent déjà. Ils valident la forme
    de la classe et du transfert une fois l'énergie acquise. La promotion
    (49.17a)--(49.19) reste une dérivation interne.

## Portée et prochain verrou

Le claim candidat est

```text
ancienne suitable locale + Riesz + Linfinity_tL^(3,infinity)
 -> C_w* et Duhamel Gelfand
 -> correcteur C_tL2
 -> correcteur énergétique global + inégalité BSS.       (49.22)
```

Cette promotion ne prouve ni régularité globale ni blow-up. Le verrou
`GAP-TYPE-I-RELATIVE-ENERGY-GLOBALIZATION` est fermé au statut interne et se
scinde maintenant en deux branches :

```text
GAP-TYPE-I-BSS-TO-STRONG-MILD-CONTINUITY,
GAP-TYPE-I-BSS-ANCIENT-RIGIDITY.                         (49.23)
```

L'expérience décisive suivante doit tester si la cohérence des redémarrages
BSS sur toutes les bandes anciennes place les traces dans
`tilde L^(3,infinity)` ou fournit une condition de rigidité indépendante de
la continuité forte. Toute tentative doit conserver la possibilité de
non-unicité à grande donnée et ne pas identifier une sélection BSS à un flot
univoque.
