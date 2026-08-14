# Cycle 0032 — collapse de support pour les swirls purs non séparables

Date de gel : 2026-08-14.

Statut : dérivation analytique interne fondée sur un plongement
Sobolev–Lorentz classique et audit exact d'éléments finis affines. Aucun
calcul d'évolution, aucune preuve de singularité et aucune certification par
arithmétique d'intervalles.

## Décision adaptative

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| collapse universel par aire de section | 5 | 5 | 5 | 5 | **20** |
| ledger transition par transition pour deux couches | 4 | 4 | 5 | 5 | 18 |
| optimisation numérique du BMO all-ball | 5 | 2 | 4 | 4 | 15 |

Le verrou `GAP-NONSEPARABLE-COMPACT-CURL-FLATNESS` est sélectionné. Le lemme
actif demande si les annulations pointwise entre deux couches peuvent conserver
une vitesse faible-`L^3` non petite lorsque toute la section méridienne devient
mince. La première action est retenue parce qu'elle couvre toute fonction de
stream non séparable, indépendamment du nombre, des signes et du décalage des
couches.

## Équation et type d'objet

Le cadre Clay de référence est toujours

```text
partial_t u+(u·nabla)u=-nabla p+nu Delta u,
div u=0,
nu>0,
f=0,
```

sur `R^3` ou `T^3`. Le cycle travaille seulement sur `R^3`, à temps fixé. Pour
`R>0`, soit `F in C_c^infinity(R^2_(r,z))`, avec

```text
supp F subset {R/2<r<3R/2},
S_2=|supp F|_(dr dz).
```

Posons

```text
U=(R/r)F(r,z)e_theta.                                    (1)
```

Alors `U in C_c^infinity(R^3)^3`, `div U=0`, et

```text
W=curl U=(R/r)[-partial_z F e_r+partial_r F e_z].        (2)
```

Le facteur `R/r` annule exactement la courbure. La fonction `F` peut être une
somme arbitraire de couches et n'est ni séparable ni de signe fixé. L'objet est
une donnée initiale admissible, pas une solution stationnaire ou une trajectoire
Navier–Stokes.

## Lemme bidimensionnel de support

Pour une fonction `f` sur `R^2`, écrivons

```text
||f||_(p,infinity)^*=sup_(lambda>0)
  lambda |{|f|>lambda}|^(1/p).
```

### Étape 1 — potentiel du gradient

La représentation par la solution fondamentale du Laplacien bidimensionnel
donne pour `F` compacte

```text
|F(x)|<=C I_1(|nabla F|)(x),
I_1g(x)=integral_(R^2)|x-y|^-1 g(y)dy.                   (3)
```

L'inégalité de convolution de Lorentz d'O'Neil, appliquée à
`|x|^-1 in L^(2,infinity)(R^2)`, donne

```text
||F||_(6,infinity)<=C_H||nabla F||_(3/2,infinity).       (4)
```

Le domaine est bien bidimensionnel :
`1/6=2/3-1/2`. La constante `C_H` ne dépend ni de `F`, ni de son support, ni
des couches qui la composent.

La contre-revue fonctionnelle vérifie aussi (4) sans dépendre d'une lecture
fragile des indices secondaires dans O'Neil : elle interpole réellement les
deux cas HLS forts `I_1:L^(4/3)->L^4` et
`I_1:L^(12/7)->L^12` au paramètre `1/2`. La sortie est exactement
`I_1:L^(3/2,infinity)->L^(6,infinity)`.

### Étape 2 — restriction à un support fini

Si `K_6=||F||_(6,infinity)` et `mu_F(lambda)` est la distribution de `|F|`,

```text
mu_F(lambda)<=min(S_2,(K_6/lambda)^6).
```

L'optimisation au point où les deux termes coïncident donne exactement

```text
||F||_(3,infinity)<=S_2^(1/6)||F||_(6,infinity).         (5)
```

Aucune norme forte n'est substituée à l'endpoint faible.

### Étape 3 — poids cylindrique

Sur le support, `R/r` et le jacobien `2pi r` sont comparables à des constantes
universelles et à `R`. Les fonctions de distribution donnent

```text
||U||_(L^(3,infinity)(R^3))
 <=C R^(1/3)||F||_(L^(3,infinity)(R^2)),                 (6)

||nabla F||_(L^(3/2,infinity)(R^2))
 <=C R^(-2/3)||W||_(L^(3/2,infinity)(R^3)).              (7)
```

En combinant (4)--(7), on obtient le lemme actif

```text
boxed{
||U||_(L^(3,infinity)(R^3))
 <=C (S_2/R^2)^(1/6)
      ||curl U||_(L^(3/2,infinity)(R^3)).}               (8)
```

La constante dépend seulement de la dimension, de la convention de
quasi-norme et de la marge annulaire `[R/2,3R/2]`. Elle ne dépend d'aucune
décomposition de `F`.

## Échelle et corollaire de section mince

Sous le scaling Navier–Stokes

```text
U_lambda(x)=lambda U(lambda x),
W_lambda(x)=lambda^2W(lambda x),
```

les deux quasi-normes sont invariantes, tandis que
`R_lambda=R/lambda` et `S_(2,lambda)=S_2/lambda^2`. Le quotient
`S_2/R^2` est donc exactement critique.

Si le support méridien est contenu dans un disque ou un carré de diamètre
`Ch`, alors `S_2<=Ch^2` et (8) devient

```text
||U||_(L^(3,infinity))
 <=C (h/R)^(1/3)||W||_(L^(3/2,infinity)).                (9)
```

Par conséquent, pour toute famille de swirls purs compacts telle que

```text
h_n/R_n->0,
sup_n ||W_n||_(L^(3/2,infinity))<infinity,               (10)
```

on a

```text
||U_n||_(L^(3,infinity))->0.                             (11)
```

Le résultat ne demande aucune hypothèse directionnelle. Une rotation log-BMO,
une annulation exacte entre couches ou un packing interne ne peuvent réparer
le gate vitesse tant que l'aire totale de la section reste `o(R^2)`.
À viscosité fixée, la famille passe finalement sous le seuil de petite donnée
faible-`L^3` de Yamazaki (`NS-SRC-0118`) et engendre donc des solutions mild
globales dans le cadre entier correspondant. Ce raccord élimine ces données
comme candidates au blow-up; il ne produit pas une borne pour les données
Clay générales.

## Application aux deux couches décalées

Considérons notamment

```text
F=V_1 eta_1((r-r_1)/a_1)chi_1((z-z_1)/b_1)
 +V_2 eta_2((r-r_2)/a_2)chi_2((z-z_2)/b_2).             (12)
```

Les profils, signes, amplitudes, largeurs et centres peuvent tous différer.
La preuve n'est pas une application de Minkowski aux deux vorticités : elle
porte sur `F` et `nabla F` après toutes les annulations. Si les couches
s'annulent sur une région, le support réel `S_2` diminue et (8) devient plus
fort. Si leurs gradients s'annulent, (4) empêche que `F` conserve en même temps
un endpoint vitesse arbitrairement grand.

Ainsi le « masquage de calotte » à deux couches est fermé dans tout régime où
leur union méridienne a aire `o(R^2)`. Le nombre de couches peut même croître :
seule l'aire du support de la somme intervient.

## Expérience adverse exacte

Le certificat construit des fonctions `F` continues et affines par morceaux
sur quatre triangulations rationnelles du carré `[-2,2]^2`, aux résolutions
`8,12,16,20`. Chaque champ est la somme de deux pyramides tensorisées avec :

- six rapports d'amplitude, positifs ou négatifs;
- quatre décalages bidimensionnels;
- quatre couples de largeurs différents.

Cela produit 384 formes, dont des masquages réellement non séparables. Sur
chaque triangle, `nabla F` est constant et rationnel. Le script calcule
exactement :

```text
S=somme des aires des triangles actifs,
M=||F||_infinity,
G^2=[sup_lambda lambda^3 |{|nabla F|>lambda}|^2]^2.
```

Le carré du quotient de forme

```text
Q_shape^2=M^6S^2/G^2                                    (13)
```

reste au plus

```text
4212353969604/482173039025 < 8.737.                       (14)
```

La valeur maximale apparaît au maillage 20, coefficient 2, centre
`(0,1/2)` et largeurs `(3/2,1/2)`; les annulations signées testées donnent des
quotients plus petits ou comparables.

Pour

```text
R_n=2^-n,
h_n=2^-2n,
2<=n<=30,                                                (15)
```

le script vérifie exactement, pour les 384 formes,

```text
[(K_U^3 upper)/(K_W^3 proxy)]^2
 =Q_shape^2(h_n/R_n)^2.                                  (16)
```

Le pire quotient carré est divisé par quatre à chaque incrément de `n`. Le
calcul porte sur des champs P1 et ne certifie pas (4); il cherche une erreur de
scaling ou une annulation finie contredisant le ledger analytique.

## Passe contradictoire

1. **Annulation pointwise.** (8) est appliquée à la somme finale, jamais aux
   couches séparées. Aucune inégalité triangulaire ne masque une cancellation.
2. **Endpoint faible.** (4), (5), (6) et (7) utilisent les quasi-normes
   faibles; le `L^infinity` n'apparaît que comme majorant conservateur dans le
   certificat fini.
3. **Dimension.** Le gain `S_2^(1/6)` vient du plongement en dimension deux;
   traiter la section comme un domaine tridimensionnel donnerait une mauvaise
   puissance.
4. **Poids cylindrique.** Les constantes reposent sur
   `R/2<r<3R/2`. Un support touchant l'axe exige une autre formulation et
   n'est pas couvert.
5. **Support épais.** Si `S_2` est comparable à `R^2`, (8) donne seulement la
   borne critique elliptique sans petit facteur. Cette branche reste ouverte.
6. **Direction.** Le lemme ne prouve pas qu'une direction log-BMO existe ou
   échoue; il rend cette question inutile dans la sous-classe mince.
7. **Régularité P1.** L'expérience emploie des fonctions affines par morceaux.
   La dérivation analytique porte séparément sur `C_c^infinity`; aucune limite
   de maillage n'est invoquée comme preuve.
8. **Pression.** La projection de Leray et la pression ne sont pas calculées.
   Elles ne peuvent restaurer une norme initiale déjà petite.
9. **Dynamique.** Aucun temps visqueux, stretching ou intervalle commun n'est
   établi. Le résultat est purement cinématique.
10. **Clay.** Une exclusion de swirls purs minces n'exclut ni les vitesses à
    composante poloïdale, ni les profils non axisymétriques, ni tout blow-up.

## Résultat négatif et pivot

Le masquage non séparable ne sauve aucune construction de swirl pur dont la
section méridienne devient mince. Le mécanisme est un collapse
Sobolev–Lorentz bidimensionnel, plus général que les budgets de dérivées du
cycle 0031.

Le verrou est révisé en `GAP-THICK-CROSS-SECTION-GRADIENT-DIRECTION`. Toute
construction pure-swirl encore viable doit satisfaire

```text
liminf S_(2,n)/R_n^2>0                                   (17)
```

et faire néanmoins décroître l'oscillation de la direction de
`nabla_perp F_n` comme `1/|log R_n|`. Le prochain test décisif est topologique :
chercher une minoration de l'oscillation directionnelle issue du degré de
`nabla F` autour d'un extremum compact, puis l'attaquer par des plateaux
dégénérés et des compensateurs de faible aire.

## Veille différentielle et portée des outils

Quatre sources primaires sont ajoutées au catalogue. Fleming–Rishel
(`NS-SRC-0132`) source la coaire et confirme que la quantité correcte pour une
superposition est `TV(sum F_j)`, jamais `sum TV(F_j)`. Bourgain–Brezis,
Van Schaftingen et Spector–Van Schaftingen (`NS-SRC-0133`–`0135`) décrivent les
gains limites dus aux contraintes div–curl et aux opérateurs canceling. Ils ne
fournissent aucune quasi-inégalité inverse entre couches : `W+(-W)=0` reste un
contre-exemple algébrique.

La veille 2025–2026 reconfirme Grujić `2511.00725v3`, Lei–Ren–Tian
`2501.08976v1` et Grujić `2607.08866v2` aux versions déjà consignées. Aucun de
ces textes ne démontre un raccord dynamique du swirl compact vers un blow-up
Navier–Stokes incompressible admissible. Le corpus atteint 135 sources.

## Reproduction

```text
python -B experiments/navier-stokes/two-layer-pure-swirl/two_layer_pure_swirl_audit.py
```

Le script utilise seulement `fractions.Fraction`. Il exécute 272 726 contrôles
exacts, sans flottant ni graine. Il ne certifie ni la constante de HLS–Lorentz,
ni le passage P1 vers `C_c^infinity`, ni une évolution Navier–Stokes.

Empreinte SHA-256 :
`597dc2e2828df34d836556c5419904d39e6ee240aa93b353a49683699ae40443`.
