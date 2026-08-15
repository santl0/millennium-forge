# Cycle 0051 — saturation PDE par une solution forward auto-similaire

Date : 2026-08-15.

## Décision adaptative

Le verrou relu est `GAP-TYPE-I-BSS-ENERGY-TAIL-TIGHTNESS`. Trois actions
réellement distinctes ont été notées avant la dérivation :

| action | nouveauté | tractabilité | falsifiabilité | levier | total |
|---|---:|---:|---:|---:|---:|
| tester la croissance `h^(1/4)` sur une vraie solution forward auto-similaire de Navier--Stokes | 4 | 5 | 5 | 5 | **19** |
| caractériser la porte uniforme par une décomposition dyadique basse fréquence | 4 | 4 | 5 | 4 | 17 |
| dériver directement une tightness annulaire depuis l'inégalité locale d'énergie et la pression de Riesz | 5 | 2 | 4 | 5 | 16 |

La première action est sélectionnée. Le lemme actif est borné : décider si
l'équation Navier--Stokes complète, la suitability et la borne faible-`L3`
peuvent, sur la seule base d'estimations forward uniformes, améliorer la
croissance du correcteur calorifique sur des bandes arbitrairement longues.

## Cadre exact

Sur `R3 x (0,infinity)`, sans frontière, force nulle et viscosité un,
considérons la donnée

```text
a(x)=(-x_2,x_1,0)/|x|².                              (51.1)
```

Elle est `C-infinity` sur `R3\{0}`, homogène de degré `-1`, solénoïdale au
sens des distributions et appartient à `L^(3,infinity)_sigma`. Le cycle 0050
a calculé

```text
K_3(a)^3=pi²/4,
integral_(B_R)|a|²=(8pi/3)R.                         (51.2)
```

La donnée n'est ni lisse à l'origine ni dans `L2`; elle n'est donc pas une
donnée Clay. Elle satisfait en revanche exactement les hypothèses du théorème
5.1 de Jia--Sverak : donnée `-1`-homogène, lisse hors de l'origine et
divergence-free.

## Interface publiée de Jia--Sverak

Le théorème 5.1 de Jia--Sverak, publié dans *Inventiones Mathematicae*
196(1), 233--265 (2014), DOI `10.1007/s00222-013-0468-x`, construit au
moins une solution globale
forward auto-similaire

```text
u(x,t)=t^(-1/2) mathcal U(x/sqrt(t)),
p(x,t)=t^(-1) mathcal P(x/sqrt(t)),                  (51.3)
```

qui appartient à la classe `N(a)` de leur définition 3.1 : solution de
Leray locale, avec inégalité locale d'énergie, satisfaisant Navier--Stokes
non forcé et lisse pour `t>0`. Leur théorème 4.1 et l'estimation (5.1)
donnent, avec

```text
A=exp(Delta)a,
W=mathcal U-A,                                      (51.4)
```

pour tout multi-indice `alpha`,

```text
|partial^alpha W(x)|<=C_(alpha,a)(1+|x|)^(-3-|alpha|).
                                                               (51.5)
```

En particulier,

```text
W in L2_sigma(R3) inter Hdot1_sigma(R3).            (51.6)
```

La partie existence, la notion de solution et la décroissance (51.5) sont
des résultats publiés dans `NS-SRC-0194`. La sélection de la donnée (51.1), la preuve de
non-nullité ci-dessous et les conséquences quantitatives pour le correcteur
sont des dérivations du laboratoire.

## Non-nullité du correcteur

La chaleur préserve l'auto-similarité de la donnée homogène :

```text
exp(t Delta)a(x)=t^(-1/2)A(x/sqrt(t)).               (51.7)
```

Supposons `W=0`. Les deux membres de (51.3) et (51.7) étant
auto-similaires, l'égalité de leurs profils au temps un donnerait

```text
u(x,t)=exp(t Delta)a(x) pour tout t>0.               (51.8)
```

Comme le membre droit satisfait l'équation de la chaleur, Navier--Stokes
imposerait

```text
curl((exp(t Delta)a dot nabla)exp(t Delta)a)=0        (51.9)
```

pour tout `t>0`. Le semi-groupe converge dans `C-infinity` sur tout compact
de `R3\{0}` lorsque `t decreases to 0`. Or un calcul direct donne

```text
(a dot nabla)a=-(x_1,x_2,0)/|x|^4,
curl((a dot nabla)a)=4x_3(-x_2,x_1,0)/|x|^6,         (51.10)
```

qui n'est pas nul. Le passage à la limite dans (51.9) contredit (51.10).
Ainsi

```text
C_*=||W||_2 in (0,infinity).                         (51.11)
```

Cette preuve n'affirme ni unicité de la solution de Jia--Sverak, ni valeur
explicite de `C_*`. Elle montre que toute solution auto-similaire fournie pour
la donnée (51.1) a un profil distinct du flot calorifique.

## Saturation exacte du correcteur BSS

Le correcteur canonique depuis le temps initial zéro est

```text
w(t)=u(t)-exp(t Delta)a
    =t^(-1/2)W(x/sqrt(t)).                            (51.12)
```

Le changement de variables `x=sqrt(t)y` donne exactement

```text
||w(t)||_2=C_* t^(1/4),
||nabla w(t)||_2²=t^(-1/2)||nabla W||_2²,             (51.13)

integral_0^T||nabla w(t)||_2²dt
 =2T^(1/2)||nabla W||_2².                             (51.14)
```

Ainsi

```text
w in C([0,T];L2) inter L2([0,T];Hdot1),
w(0)=0 en L2,                                        (51.15)
```

sur toute bande finie, tandis que son énergie et sa dissipation ne sont pas
uniformes lorsque `T->infinity`.

Le profil `mathcal U=A+W` est borné près de l'origine et décroît comme
`|x|^-1`; il appartient donc à `L^(3,infinity)`. Par auto-similarité,

```text
sup_(t>0)||u(t)||_(L^(3,infinity))
 =||mathcal U||_(L^(3,infinity))=:M_*<infinity.       (51.16)
```

La saturation (51.13) a donc lieu pour une vraie solution non forcée, à norme
critique uniforme fixée.

## Redémarrage à un temps intérieur

Pour `0<s<t`, le cocycle du cycle 0050 devient

```text
g_(s,t)=w(t)-exp((t-s)Delta)w(s),                     (51.17)
```

où `g_(s,t)=u(t)-exp((t-s)Delta)u(s)`. La contraction `L2` donne

```text
| ||g_(s,t)||_2-C_*t^(1/4) |
 <=||w(s)||_2=C_*s^(1/4).                             (51.18)
```

Par conséquent, pour tout `s>0` fixé,

```text
t^(-1/4)||g_(s,t)||_2 -> C_* quand t->infinity.       (51.19)
```

La croissance n'est donc pas un défaut propre à la trace singulière au temps
zéro; elle subsiste après rebasage à tout temps intérieur lisse.

## Réduction analytique indépendante : seules les basses fréquences restent

La passe analytique indépendante ne se contente pas du profil. Pour toute
ancienne conditionnelle des cycles 0048--0050, avec
`sup_t||v(t)||_(3,infinity)<=M`, le Duhamel projeté donne

```text
||Delta_j g_(s,r)||_2
 <= C M^2 2^(-j/2) min(1,(r-s)2^(2j)).                  (51.19a)
```

Le noyau de `Delta_j exp(hDelta) P div` est estimé dans
`L^(6/5,1)` : une dérivée apporte `2^j`, le changement
`L^(3/2,infinity)->L2` apporte `2^(j/2)`, puis l'intégration thermique
apporte `2^(-2j)`. Il s'ensuit, pour tout seuil fixe `J`,

```text
sup_(s<r) sum_(j>J)||Delta_j g_(s,r)||_2^2
 <= C M^4 2^(-J).                                      (51.19b)
```

Le verrou d'uniformité est donc exactement infrarouge. Par Littlewood--Paley
appliqué au **correcteur complet** `g_(s,r) in L2`, et jamais séparément aux
deux traces faible-`L3`,

```text
liminf_(s->-infinity)||g_(s,r)||_2<infinity
<=> liminf_(s->-infinity) sum_(j<=J)||Delta_jg_(s,r)||_2^2<infinity.
                                                               (51.19c)
```

Une forme canonique équivalente fixe un unique `a>0` avant la limite :

```text
sup_(s<r)||(I-exp(aDelta))g_(s,r)||_2 <= C M^2 a^(1/4),

liminf_(s->-infinity)||g_(s,r)||_2<infinity
<=> liminf_(s->-infinity)||exp(aDelta)g_(s,r)||_2<infinity.
                                                               (51.19d)
```

Ainsi une seule suite `s_n->-infinity` et un seul `a>0` suffisent. Le détail
des intégrales de Bochner après projection, de la fréquence zéro et des
quantificateurs est dans `reviews/cycle-0051-analysis.md`. Ce lemme positif
ne borne pas la partie calorifiée : il localise exactement l'estimation PDE
encore manquante.

## Forme en bandes reculées et impossibilité uniforme

Pour `T>0`, translatons la même solution :

```text
v^T(x,tau)=u(x,tau+T),  -T<=tau<=0.                   (51.20)
```

Chaque `v^T` est une solution exacte non forcée, lisse pour `tau>-T`, dans la
classe faible-`L3` scindée, et

```text
sup_(-T<tau<=0)||v^T(tau)||_(L^(3,infinity))=M_*,

||v^T(0)-exp(T Delta)v^T(-T)||_2=C_*T^(1/4).          (51.21)
```

Il n'existe donc aucune fonction finie `F(M)` telle que toutes les solutions
forward de cette classe vérifient sur toutes les longueurs de bande

```text
||v(t)-exp((t-s)Delta)v(s)||_2<=F(M).                 (51.22)
```

La conclusion utilise ici une famille de bandes translatées, pas une seule
solution ancienne définie sur `(-infinity,0]`.

## Passe contradictoire principale

1. **Quantificateur ancien.** (51.21) réfute une estimation universelle sur
   toutes solutions et toutes bandes. Elle ne construit pas une solution
   ancienne unique pour laquelle `s->-infinity`.
2. **Donnée Clay.** (51.1) est singulière et d'énergie infinie. Le résultat
   ne fournit ni donnée initiale admissible Clay, ni blow-up.
3. **Existence, pas unicité.** Jia--Sverak donnent au moins une solution. La
   preuve `W!=0` vaut pour toute solution auto-similaire issue de (51.1), mais
   ne sélectionne pas une branche unique.
4. **Constante inconnue.** `C_*` est strictement positive et finie, mais
   aucune valeur numérique ou borne inférieure quantitative n'est certifiée.
5. **Pression.** La source fournit une pression locale, définie à une jauge
   temporelle près. Pour `t>0`, la décroissance du profil permet la jauge de
   Riesz compatible avec l'équation; le test (51.10) emploie le curl
   précisément pour exclure toute compensation par un gradient. Aucune
   pression ancienne n'est construite.
6. **Suitability.** La solution appartient à la classe de Leray locale de la
   source; le test n'est plus seulement cinématique. Cela ne remplace pas la
   compatibilité d'une orbite ancienne sur tout le passé.
7. **Basse fréquence.** L'auto-similarité transporte le défaut vers
   `|xi|~t^(-1/2)`. Une estimation haute fréquence ou locale ne voit pas la
   masse `L2` croissante.
8. **Type II.** Aucun paramètre Type II n'est présent; aucune extrapolation
   n'est autorisée.

## Résultat et pivot

Le résultat négatif renforcé est

```text
NS exacte + suitability locale + pression PDE
+ borne uniforme L^(3,infinity) + classe BSS sur chaque bande
-/-> borne L2 du correcteur indépendante de la longueur
pour toute la classe des solutions forward.                     (51.23)
```

Le cycle 0050 avait réfuté l'inférence semi-groupale par un champ
cinématique. Le cycle 0051 montre que même la dynamique Navier--Stokes
forward complète ne répare pas (51.23). Toute fermeture ancienne doit donc
exploiter une propriété qui distingue une **même orbite compatible sur tout
le passé** d'une famille de problèmes forward sur des bandes de longueur
croissante.

`GAP-TYPE-I-BSS-ENERGY-TAIL-TIGHTNESS` est fermé négativement pour les bornes
universelles forward dépendant seulement de `M`. La passe dyadique ferme en
outre uniformément les hautes fréquences. Le verrou est raffiné en

```text
GAP-TYPE-I-SINGLE-ANCIENT-ORBIT-RECURRENCE,
GAP-TYPE-I-ANCIENT-INFRARED-STRESS-DEPLETION,
GAP-TYPE-I-ANCIENT-QUOTIENT-RIGIDITY.                  (51.24)
```

La prochaine expérience décisive doit tester une propriété véritablement
ancienne : un gain signé uniforme dans les intégrales dyadiques basses du
stress le long d'une même orbite. Répéter une estimation forward uniforme en
longueur est abandonné.
