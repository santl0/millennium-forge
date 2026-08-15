# Cycle 0048 — correcteur de Duhamel faible-`L3` et porte énergétique

Date : 2026-08-15.

## Décision adaptative

Le verrou relu est
`GAP-TYPE-I-ANCIENT-WEAK-L3-RIGIDITY-OR-MILDNESS`. Trois actions ont été
notées avant la dérivation :

| action | nouveauté | tractabilité | falsifiabilité | levier | total |
|---|---:|---:|---:|---:|---:|
| établir la formule de Duhamel et suivre le correcteur global | 3 | 4 | 5 | 5 | **17** |
| promouvoir directement vers la classe énergétique scindée BSS | 4 | 2 | 4 | 5 | 15 |
| appliquer immédiatement un Liouville mild borné | 3 | 1 | 3 | 5 | 12 |

La première action est sélectionnée. Le lemme actif est borné : déterminer
ce que l'équation globale et la seule borne critique imposent au correcteur
sur une bande temporelle finie. La dissipation globale et la rigidité ne sont
pas incluses par définition.

## Cadre exact

Soit `I=[t_0,t_1]`, avec `-infinity<t_0<t_1<=0`. La sortie du cycle 0047 est
une paire `(v,q)` sur `R3 x I` telle que

```text
partial_t v-Delta v+div(v tensor v)+nabla q=0,
div v=0,
q=R_iR_j(v_i v_j),                              (48.1)
```

dans les distributions, avec

```text
ess sup_(t in I) ||v(t)||_(L^(3,infinity)) <= M, (48.2)
```

et `(v,q)` faible adaptée locale. Le résultat ci-dessous utilise (48.1),
(48.2) et la jauge globale; la suitability locale n'intervient que pour
situer la paire dans le pipeline précédent et ne doit pas être confondue
avec une inégalité d'énergie globale.

On note `X=L^(3,infinity)(R3)` muni de sa norme duale équivalente et
`X_*=L^(3/2,1)(R3)` son prédual séparable.

## Représentant faible-étoile continu

Pour `phi` solénoïdale et lisse compacte, la projection de Leray donne

```text
d/dt <v,phi>
 =<v,Delta phi>+<v tensor v,nabla phi>.           (48.3)
```

Les estimations de Lorentz sont

```text
|<v,Delta phi>| <= C M ||Delta phi||_(L^(3/2,1)),
|<v tensor v,nabla phi>|
  <= C M² ||nabla phi||_(L^(3,1)).                (48.4)
```

Ainsi `t -> <v(t),phi>` possède un représentant absolument continu. Pour un
test arbitraire de `X_*`, on approche par des tests lisses; la borne uniforme
de (48.2) contrôle l'erreur aux deux temps. Il existe donc un représentant

```text
v in C_w* (I;L^(3,infinity)).                     (48.5)
```

En particulier la trace globale

```text
a:=v(t_0) in L^(3,infinity), div a=0              (48.6)
```

est définie sans extraction dépendant du test. Cette continuité est faible-
étoile; la forte continuité dans faible-`L3` reste fausse en général, déjà
pour le semi-groupe de la chaleur sur une donnée homogène de degré `-1`.

## Formule de variation des constantes

Appliquons la projection de Leray à (48.1) :

```text
partial_t v-Delta v=-P div(v tensor v).           (48.7)
```

La variation des constantes dans les distributions tempérées donne, pour
`t_0<=t<=t_1`, `h=t-t_0`,

```text
v(t)=S(h)a-B_(t_0)(v,v)(t),                       (48.8)

B_(t_0)(v,v)(t)
 :=integral_(t_0)^t S(t-s)P div(v tensor v)(s) ds.
```

Pour le justifier, on teste l'équation par la solution rétrograde de la
chaleur. Tous les termes sont intégrables contre Schwartz, et (48.5) fournit
les valeurs aux bords temporels. Aucun passage par une solution classique ni
par une troncature spatiale n'est requis.

Cette identité est d'abord une formule de Duhamel **distributionnelle**. Le
mot `mild` ne sera utilisé qu'avec la topologie et les clauses globales de la
définition visée.

## Fermeture endpoint par dualité de Meyer--Yamazaki

La divergence logarithmique de la norme d'opérateur ponctuelle ne clôt pas
la question endpoint. Le lemme 7 de Taniuchi (2024, `NS-SRC-0190`), qui
réénonce explicitement l'estimation de Yamazaki (2000, `NS-SRC-0118`), donne
dans le cas de l'espace entier

```text
integral_s^t |<F(tau),nabla S(t-tau)P phi>| d tau
 <= C ||F||_(L-infinity_(s,t)L^(3/2,infinity))
      ||phi||_(L^(3/2,1)),                       (48.8a)
```

pour `phi` solénoïdale et `F in L-infinity_t L^(3/2,infinity)_x`. Appliquée
à `F=v tensor v`, cette estimation construit **avant** l'usage de (48.8),
par dualité `L^(3,infinity)=(L^(3/2,1))^*`, un élément

```text
B_(s,t)(v,v) in L^(3,infinity),
||B_(s,t)(v,v)||_(L^(3,infinity)) <= C M^2.       (48.8b)
```

Il s'agit d'une intégrale de Gelfand faible-étoile : (48.8a) intègre après
avoir fixé `phi`. Elle ne démontre pas l'intégrabilité de la norme du champ
vectoriel. L'identité distributionnelle l'identifie ensuite au terme de
Duhamel, si bien que (48.8) vaut comme égalité dans `L^(3,infinity)` contre
tout le prédual, simultanément pour tous `t_0<=s<t<=t_1` après choix du
représentant (48.5).

Pour chaque test fixé, l'absolue continuité de l'intégrale scalaire donne

```text
B_(s,t)(v,v) -> 0 weak-star in L^(3,infinity)
when t decreases to s.                           (48.8c)
```

La constante critique de (48.8b) ne porte cependant aucun facteur tendant
vers zéro avec `t-s`. On n'obtient ni convergence forte du terme dans
faible-`L3`, ni continuité forte du semi-groupe sur tout cet espace. La
définition publiée de Taniuchi exige précisément
`v in C_t L^(3,infinity)` en norme pour employer le terme « solution mild
`L^(3,infinity)` ». Le résultat de ce cycle ferme donc le Duhamel endpoint
faible-étoile, pas cette mildness forte.

## Gain global sous-critique du correcteur

Soit `K_r` le noyau matriciel de `S(r)P div`. Il possède l'échelle d'une
dérivée du noyau d'Oseen :

```text
K_r(x)=r^-2 K_1(x/sqrt(r)).                       (48.9)
```

Pour `3/2<p<3`, posons `k` par

```text
1/k=1/3+1/p.                                      (48.10)
```

Alors `1<k<3/2`, `K_1 in L^(k,1)` et

```text
||K_r||_(L^(k,1))
 =C_k r^[-3/2+3/(2p)].                            (48.11)
```

Le produit et la convolution d'O'Neil donnent

```text
||v tensor v||_(L^(3/2,infinity)) <= C_L M²,

||K_r*(v tensor v)(s)||_Lp
 <=C_p M² r^[-3/2+3/(2p)].                        (48.12)
```

La puissance temporelle est intégrable exactement pour `p<3`. Par
Minkowski,

```text
||B_(t_0)(v,v)(t)||_Lp
 <= C_p M² h^[(3-p)/(2p)],
              3/2<p<3.                            (48.13)
```

La même décomposition de l'intégrale en une couche proche de `t` et une
partie éloignée, jointe à la continuité de `r -> K_r` dans `L^(k,1)`, donne

```text
B_(t_0)(v,v) in C([t_0,t_1];L^p),
B_(t_0)(v,v)(t_0)=0.                              (48.14)
```

Le cas décisif `p=2` est

```text
w(t):=v(t)-S(t-t_0)a=-B_(t_0)(v,v)(t),

w in C([t_0,t_1];L2),
||w(t)||_2 <= C M² (t-t_0)^(1/4).                 (48.15)
```

La sortie du cycle 0047 possède donc, à tout temps de redémarrage fini, une
scission calorique canonique dont le correcteur a énergie instantanée globale
finie et trace forte nulle. Cette conclusion améliore le ledger 0047 : la
trace forte du **correcteur** n'est plus le premier obstacle.

## Ce que le logarithme endpoint interdit encore

Pour `p=3`, l'exposant de (48.11) vaut `-1`; l'intégration terme à terme
produit

```text
integral_0^h r^-1 dr.                             (48.16)
```

Elle ne certifie aucune borne endpoint par **intégration de la norme
ponctuelle**. Contrairement à la première dérivation, la passe
contradictoire montre que (48.8a) fournit bien une borne bilinéaire autonome
faible-étoile dans `L-infinity_tL^(3,infinity)_x`. Le logarithme interdit
seulement de la remplacer par une intégrale de Bochner ou d'en déduire une
petitesse de court temps et une continuité forte critique.

Trois notions doivent rester séparées :

1. **Duhamel endpoint faible-étoile** : (48.8)--(48.8c), avec trace
   faible-étoile, intégrale de Gelfand et correcteur fort dans tout `L^p`,
   `3/2<p<3`;
2. **solution faible `L^(3,infinity)` de Barker–Seregin–Šverák** : en plus,
   `w in L-infinity_tL2_x inter L2_t Hdot1_x`, continuité faible `L2`, trace
   forte nulle, inégalité d'énergie perturbée et inégalité locale;
3. **ancienne mild bornée de KNSS/Albritton–Barker** : formule d'Oseen dans
   la classe bornée, redémarrages cohérents vers `-infinity` et exclusion des
   modes parasites.

(48.15) ferme seulement `L-infinity_tL2_x`, la continuité forte et la trace
nulle du correcteur sur chaque bande finie. Elle n'établit pas les autres
clauses des classes 2 ou 3.

## Première clause non obtenue : dissipation globale

Différencier une fois de plus le noyau remplace (48.11), pour `p=2`, par

```text
||nabla K_r||_(L^(6/5,1)) = C r^(-5/4).           (48.17)
```

Cette puissance n'est pas intégrable à zéro. La seule borne
`v tensor v in L-infinity_tL^(3/2,infinity)_x` ne donne donc pas

```text
nabla w in L2(I x R3).                            (48.18)
```

Un ledger adverse le montre sans singularité locale imposée. Prenons un
champ solénoïdal `W in C_c^infinity`, des échelles `lambda_n=2^n` et des
centres très séparés, puis

```text
V_N(x)=sum_(n<=N) lambda_n W(lambda_n(x-x_n)).     (48.19)
```

Les supports de `V_N` sont disjoints et

```text
sup_N ||V_N||_(L^(3,infinity)) < infinity,
sup_N ||V_N tensor V_N||_(L^(3/2,infinity))<infinity.
                                                               (48.20)
```

Pour la réponse de Stokes à chaque stress statique, l'énergie `L2` du bloc
à temps fixé se remet à l'échelle comme `lambda_n^-1`, tandis que son
énergie de gradient se remet comme `lambda_n`. Des translations
super-géométriques rendent les interactions du noyau d'Oseen arbitrairement
petites sur les coeurs. La somme de (48.20) peut donc garder une réponse
`L2` bornée tout en faisant diverger la somme des masses `Hdot1` locales.

Le certificat indépendant emploie en outre le témoin solénoïdal exact

```text
U(x)=(-x_2,x_1,0)/|x|^2,
K_3(U)^3=pi^2/4,
||U||_(L2(B_R))^2=(8pi/3)R.                     (48.20a)
```

Ses coupures radiales préservent la divergence, mais la queue extérieure
conserve toute sa quasi-norme faible-`L3`. Il réfute donc aussi le split
naïf « coeur d'énergie + queue critique petite » sous la seule borne (48.2).

Ce profil est un test de mapping : `V_N` n'est pas une trajectoire
Navier–Stokes. Il ne réfute pas qu'équation, suitability locale et structure
quadratique réparent ensemble (48.18). Il réfute toute preuve qui déduirait
la dissipation globale de la seule taille critique et du noyau de Duhamel.

## Porte énergétique restante

Pour appartenir à la classe BSS sur `[t_0,t_1]`, il reste à démontrer

```text
w in L2(t_0,t_1;Hdot1(R3))                       (48.21)
```

et l'inégalité perturbée globale

```text
||w(t)||_2²+2 integral_(t_0)^t ||nabla w||_2²
 <=2 integral_(t_0)^t integral_R3
      [S(s-t_0)a tensor w+S(s-t_0)a tensor S(s-t_0)a]
       :nabla w.                                  (48.22)
```

Le flot calorique satisfait, pour `r>3`,

```text
||S(h)a||_r <= C_r M h^[-1/2+3/(2r)].             (48.23)
```

Les choix `r=4,5` rendent les termes de droite formellement presque
intégrables. La borne nouvelle `||w(h)||_2²<=CM^4h^(1/2)` compense le
coefficient critique `||S(h)a||_5^5~h^-1` dans le ledger de Young. Mais
utiliser (48.22) pour prouver (48.21) sans avoir justifié le test global de
l'équation serait circulaire. La suitability est locale et les queues de
pression faible-`L^(3/2)` ne sont pas absolument continues.

Le prochain lemme doit donc être un théorème de **globalisation de l'énergie
relative**, avec cutoffs, pression et défaut à l'infini suivis. S'il réussit,
la solution appartient à la classe scindée BSS sur toute bande finie. Il ne
la rend toujours ni bornée, ni KNSS-mild, ni rigide.

## Passe contradictoire principale

1. Une trace faible-étoile de `v` ne devient pas une trace forte faible-`L3`;
   seule la trace `L2` du correcteur est forte.
2. La formule endpoint faible-étoile (48.8)--(48.8c) ne reçoit pas
   automatiquement le nom de mildness forte ou bornée.
3. Le gain `L2` utilise le noyau d'Oseen projeté global; un calcul local de
   pression ne suffit pas.
4. L'exposant `1/4` vient du noyau `L^(6/5,1)` et du temps, pas d'une
   interpolation avec une énergie déjà supposée.
5. La borne de Yamazaki est test par test; inverser intégrale et supremum
   recrée le logarithme (48.16) et invente à tort une intégrale de Bochner.
6. `w in C_tL2_x` n'implique pas `nabla w in L2`; (48.17) localise la perte
   d'une demi-dérivée temporelle.
7. Tester globalement par `w` avant (48.21) utilise précisément la conclusion
   recherchée. La local energy inequality doit être globalisée sans ce cercle.
8. Même la classe BSS ne donne pas la bornitude ou le Liouville général 3D.
9. Aucun argument ne transmet ici une singularité à `t=0`.
10. Type II reste absent : `M` et les constantes du pipeline sont fixés.

## Portée Clay et prochain verrou

Le claim candidat du cycle est strictement conditionnel au pipeline Type I :

```text
ancienne suitable locale + Riesz + L-infinity_tL^(3,infinity)_x
 -> C_w* L^(3,infinity)
 -> Duhamel endpoint faible-etoile dans L^(3,infinity)
 -> correcteur C_tL2, trace forte nulle.           (48.24)
```

Il ne prouve ni régularité globale ni blow-up. Le verrou est raffiné en

```text
GAP-TYPE-I-RELATIVE-ENERGY-GLOBALIZATION.          (48.25)
```

L'expérience décisive suivante doit appliquer l'inégalité locale à des
cutoffs `chi_R` dans l'équation du correcteur, sommer les flux de pression et
convection par coquilles, puis établir soit une limite nulle uniforme lorsque
`R->infinity`, soit un contre-profil PDE-compatible d'influx énergétique à
l'infini.
