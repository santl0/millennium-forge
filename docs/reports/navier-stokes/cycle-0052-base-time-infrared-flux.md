# Cycle 0052 — identité de flux infrarouge en temps de base

Date : 2026-08-15.

Statut : `AI_INTERNAL_DERIVATION`; aucune conclusion Clay.

## Décision adaptative

Le verrou relu est `GAP-TYPE-I-ANCIENT-INFRARED-STRESS-DEPLETION`. Les trois
actions candidates, fixées avant la dérivation, sont :

| action | nouveauté | tractabilité | falsifiabilité | levier | total |
|---|---:|---:|---:|---:|---:|
| dériver l'identité exacte en temps de base et attaquer le signe par triades | 4 | 5 | 5 | 5 | **19** |
| auditer la réduction par récurrence backward-DSS et ses Liouville | 4 | 4 | 5 | 4 | 17 |
| imposer un moment `L1` uniforme au stress et mesurer le gain dyadique | 3 | 5 | 5 | 3 | 16 |

La première action est sélectionnée. Le lemme actif est borné : transformer
la condition calorifique du cycle 0051 en une identité scalaire de flux
signé, déterminer la perte de toute majoration absolue et tester si
l'incompressibilité impose un signe triadique exploitable.

## Cadre exact

Sur `R3 x (-infinity,T)`, sans frontière, viscosité un et force nulle,
considérons

```text
partial_t v-Delta v+P div(v tensor v)=0,
div v=0,                                                (52.1)
```

où `P` est la projection de Leray et où la pression est fixée globalement par
`q=R_iR_j(v_i v_j)`. La paire `(v,q)` est une solution ancienne faible
adaptée locale, avec représentant `C_w*L^(3,infinity)` et

```text
sup_(t<T)||v(t)||_(L^(3,infinity))<=M.                  (52.2)
```

Les cycles 0048--0051 donnent, pour `s<r<T`,

```text
g_(s,r)=v(r)-S(r-s)v(s)
       =-integral_s^r S(r-tau)P div(v tensor v)(tau)dtau,
g_(s,r) in L2_sigma,                                    (52.3)

||g_(s,r)||_2<=C_D M²(r-s)^(1/4).                       (52.4)
```

Pour un temps calorifique **fixe** `a>0`, posons

```text
E_a(s;r)=||S(a)g_(s,r)||_2².                            (52.5)
```

Le cycle 0051 établit qu'une seule suite `s_n->-infinity` sur laquelle
`E_a(s_n;r)` est bornée suffit à obtenir `v(r) in L2(R3)`.

## Régularité en temps de base

Notons `N(t)=P div(v tensor v)(t)` et
`G_a(s;r)=S(a)g_(s,r)`. Le Duhamel lissé s'écrit

```text
G_a(s;r)=-integral_s^r S(a+r-tau)N(tau)dtau.            (52.6)
```

En effet, `v tensor v in L^(3/2,infinity)` par O'Neil et le noyau de
`S(h)P div` appartient à `L^(6/5,1)` avec norme `O(h^(-3/4))`. Dans
(52.6), le paramètre calorifique est au moins `a>0`. Sur toute bande
compacte `[s_0,r]`, il s'agit donc d'une intégrale de Bochner dans `L2`, et

```text
s -> G_a(s;r) est AC([s_0,r];L2),
partial_s G_a(s;r)=S(a+r-s)N(s) pour presque tout s.     (52.7)
```

Cette dérivée porte le signe positif : le signe négatif de Duhamel est
compensé par la dérivation de sa borne inférieure. Dériver séparément les
deux traces seulement faible-`L3` n'est ni nécessaire ni autorisé.

## Identité exacte de flux

Par (52.7), auto-adjonction et propriété de semi-groupe,

```text
partial_s E_a(s;r)
 =2 <G_a(s;r),S(a+r-s)N(s)>
 =2 <S(2a+r-s)g_(s,r),P div(v tensor v)(s)>.             (52.8)
```

Comme `S(2a+r-s)g` est solénoïdal, la projection disparaît dans le pairing.
La convolution de Lorentz place son gradient dans `L^(3,1)`, dual de
`L^(3/2,infinity)`. L'intégration par parties donne donc

```text
partial_s E_a(s;r)=-I_a(s;r),                            (52.9)

I_a(s;r)=2 integral_R3 (v tensor v)(x,s)
                    :nabla S(2a+r-s)g_(s,r)(x) dx.       (52.10)
```

Puisque `g_(r,r)=0`, l'intégration sur `[s,r]` donne l'identité scalaire

```text
boxed: E_a(s;r)=integral_s^r I_a(sigma;r) dsigma.        (52.11)
```

Le membre droit est non négatif **après intégration sur tout l'intervalle**.
Cela ne donne aucun signe ponctuel à `I_a`. L'identité (52.11) est une
polarisation exacte du Duhamel non linéaire, pas une nouvelle inégalité
d'énergie de la solution complète.

## Critère équivalent et quantificateurs

Pour tout `a>0` et tout `r<T` fixés,

```text
liminf_(s->-infinity)||g_(s,r)||_2<infinity

<=> liminf_(s->-infinity)E_a(s;r)<infinity

<=> il existe s_n->-infinity tel que
    sup_n integral_(s_n)^r I_a(sigma;r)dsigma<infinity. (52.12)
```

La première équivalence utilise le complément haute fréquence uniforme du
cycle 0051. La seconde est (52.11). Sous (52.12), le cycle 0050 donne
`v(r) in L2(R3)`.

La version uniforme remplace les deux `liminf` par `sup_(s<r)`. Aucun passage
`a->0`, aucune positivité ponctuelle et aucune somme de normes absolues ne sont
requis. Le flux dépend du temps terminal `r` et du correcteur entier; ce n'est
pas le flux spectral instantané usuel de `v`.

## Échec exact de la valeur absolue

Le pairing de Lorentz et le lissage `L2->L^(3,1)` donnent

```text
|I_a(s;r)|
 <=C ||v(s)||_(3,infinity)²
      ||nabla S(a+r-s)G_a(s;r)||_(3,1)

 <=C M²(a+r-s)^(-3/4)E_a(s;r)^(1/2).
                                                               (52.13)
```

Le Duhamel lissé suit en outre la constante de bord :

```text
E_a(s;r)^(1/2)
 <=C M²[(a+r-s)^(1/4)-a^(1/4)].                         (52.14)
```

Ainsi

```text
|I_a(s;r)|
 <=C M^4(a+r-s)^(-3/4)
       [(a+r-s)^(1/4)-a^(1/4)].                         (52.15)
```

Quand `r-s` est grand, (52.15) vaut seulement

```text
|I_a(s;r)|<=C M^4(r-s)^(-1/2).                          (52.16)
```

Cette puissance n'est pas intégrable au passé et redonne exactement

```text
integral_s^r |I_a(sigma;r)|dsigma
 <=C M^4(r-s)^(1/2),                                    (52.17)
```

c'est-à-dire le carré du coût `M²(r-s)^(1/4)` déjà connu. Toute preuve qui
prend la valeur absolue avant l'intégration temporelle est donc fermée à la
mauvaise échelle. Une amélioration doit conserver les corrélations signées de
`I_a` sur une même orbite ancienne.

## Échelle

Sous

```text
v_lambda(x,t)=lambda v(lambda x,lambda²t),               (52.18)
```

on a

```text
E_a^lambda(s;r)
 =lambda^(-1)E_(lambda²a)(lambda²s;lambda²r),            (52.19)

I_a^lambda(s;r)
 =lambda I_(lambda²a)(lambda²s;lambda²r).                (52.20)
```

Le produit `I ds` a donc le poids énergétique `lambda^(-1)`, comme (52.11).
Une constante prétendument uniforme doit transformer simultanément `a`, `s`
et `r`; fixer un indice dyadique absolu après remise à l'échelle serait faux.

## Ce que peut et ne peut pas tester une triade

Sur `T3`, deux modes divergence-free `k,l` créent au mode `q=k+l` le
coefficient projeté

```text
C_q=P_q[(a dot l)b+(b dot k)a].                          (52.21)
```

Le test adverse du cycle vérifie exactement que `C_q` peut être non nul avec
`|q|=1` et `|k|,|l|` arbitrairement grands, et que son signe ainsi que le
transfert d'énergie du mode `q` s'inversent sans changer les énergies
modales. Cela exclut une positivité algébrique issue de la seule
incompressibilité.

Ce test périodique ne démontre pas que `I_a(s;r)` change de signe le long
d'une solution ancienne sur `R3`: dans (52.10), `g_(s,r)` est corrélé à tout
le futur `[s,r]`. Il interdit seulement de remplacer cette corrélation par un
argument de signe instantané triade par triade.

## Passe contradictoire

1. **Signe de la borne inférieure.** `partial_s g=+S(r-s)N(s)`; le signe
   opposé inverserait (52.11).
2. **Bochner versus Gelfand.** Le Duhamel endpoint global est de Gelfand,
   mais après lissage jusqu'au temps terminal le noyau `h^(-3/4)` est
   intégrable dans `L2`; c'est cette représentation qui est différentiée.
3. **Temps terminal.** `r` est fixé avant de dériver en `s`. Dériver une
   diagonale `r=r(s)` ajouterait un terme.
4. **Pression.** La jauge globale de Riesz est nécessaire pour écrire
   `P div(v tensor v)` sur `R3`; aucune pression locale n'est silencieusement
   projetée.
5. **Pairing endpoint.** `L^(3/2,infinity)` se paire avec `L^(3,1)`, pas avec
   un simple `L3` fort non raffiné.
6. **Positivité intégrée.** `integral_s^r I_a=E_a>=0` ne signifie pas
   `I_a>=0` presque partout.
7. **Circularité énergétique.** Imposer `v(s) in L2` rendrait le stress `L1`
   et fermerait facilement l'infrarouge, mais suppose essentiellement la
   sortie recherchée.
8. **Valeur absolue.** (52.15) est supercritique au passé et ne satisfait pas
   le critère (52.12).
9. **Triades.** Le certificat `T3` porte sur l'algèbre instantanée et non sur
   une orbite ancienne `R3`, la suitability ou la pression de Riesz globale.
10. **Récurrence.** Une auto-similarité backward exacte est un sous-cas
    beaucoup plus rigide et doit être raccordée à ses Liouville publiés; elle
    ne représente pas toute récurrence faible-étoile ou modulée.
11. **Clay.** Même `v(r) in L2` demanderait encore une rigidité ancienne et
    ne couvre pas Type II.

## Résultat et pivot

Le lemme positif du cycle est l'identité (52.11) et son équivalence (52.12).
Le résultat négatif est

```text
borne faible-L3 + Duhamel + valeurs absolues
-/-> primitive infrarouge uniforme au passé,                      (52.22)

incompressibilité + projection de Leray
-/-> signe instantané coercif des triades.                         (52.23)
```

Le verrou `GAP-TYPE-I-ANCIENT-INFRARED-STRESS-DEPLETION` est raffiné en

```text
GAP-TYPE-I-ANCIENT-SIGNED-BASE-FLUX-CANCELLATION.         (52.24)
```

La prochaine expérience décisive doit porter sur une **corrélation
temporelle de la même orbite**, par exemple une récurrence de blow-down qui
force deux primitives de (52.10) à se compenser. Une estimation absolue ou un
nouveau test instantané de triades est abandonné.
