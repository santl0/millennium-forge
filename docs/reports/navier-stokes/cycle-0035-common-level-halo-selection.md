# Cycle 0035 — sélection pure-swirl par bande de niveau commune

Date de gel : 2026-08-14.

Statut : dérivation analytique interne, expérience algébrique exacte et trois
passes contradictoires IA. Aucun résultat nouveau n'est classé `PAPER_PROOF`.
Aucune trajectoire de Navier–Stokes n'est construite.

## Décision adaptative

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| déduire un halo fixe `O(v_j)` du registre BV total | 3 | 4 | 5 | 4 | 16 |
| réaliser une fuite par queue axiale longue | 4 | 5 | 5 | 4 | 18 |
| remplacer la boîte par une bande de niveau globale | 5 | 5 | 5 | 5 | **20** |

La deuxième action est retenue. Elle teste le quantificateur qui manquait au
cycle 0034 : le curl peut être étalé sur un support immense, mais la partie du
curl utilisée par coaire peut-elle être confinée dans un ensemble dont le
volume est vu par la fonction de distribution de la vitesse ? La réponse est
positive pour toute famille finie de cellules pure-swirl annulaires à supports
complets disjoints. Ni volume de boîte, ni diamètre axial, ni plateau
d'amplitude uniforme ne sont requis pour la sélection des deux endpoints.

## Équation, domaine et type d'objet

Le problème Clay de référence reste

```text
partial_t u+(u·nabla)u=-nabla p+nu Delta u,
div u=0, nu>0, f=0,
```

sur `R3` ou `T3`. Le cycle travaille uniquement sur `R3`, à un temps fixé,
avec des champs lisses compacts divergence-free. Pour une famille finie,

```text
F_j in C_c^infinity((0,infinity)×R),
supp F_j subset {R_j/2<r<3R_j/2},
U_j=(R_j/r)F_j e_theta,
W_j=curl U_j=(R_j/r)(-partial_z F_j e_r+partial_r F_j e_z).
```

Les supports tridimensionnels complets des `F_j` sont supposés deux à deux
disjoints. Il n'y a aucune borne sur leur étendue en `z`, leur volume, leur
nombre de composantes de niveau ou leur profil d'amplitude. On pose

```text
U=sum_j U_j,
W=sum_j W_j,
K_u=||U||_(L^(3,infinity)),
K_w=||W||_(L^(3/2,infinity)).
```

Les champs sont des données initiales classiques admissibles sur `R3`, mais
aucune pression, viscosité ou évolution n'intervient dans le résultat.

## Lemme actif

Soit `C_I>0` une constante de l'inégalité isopérimétrique euclidienne

```text
Per(E)>=C_I |E|^(2/3)                             (1)
```

sur `R3`.

### Théorème 1 — sélection par bande commune

Si `K_u>0` et `K_w<infinity`, il existe une cellule `j_*` telle que

```text
K_(u,j_*)>=c_H K_u^2/K_w,
K_(u,j_*)/K_(w,j_*)>=c_H(K_u/K_w)^2,             (2)
c_H=C_I/324.
```

Ici `K_(u,j)=||U_j||_(L^(3,infinity))` et
`K_(w,j)=||W_j||_(L^(3/2,infinity))`. Si `K_w=0`, les hypothèses avec
`K_u>0` sont incompatibles; le quotient n'est donc utilisé que pour `K_w>0`.

Le théorème remplace, dans la classe pure-swirl annulaire, le corollaire du
cycle 0034 qui exigeait une boîte de volume comparable et un plateau effectif.
Il ne remplace pas le théorème BV abstrait pour des paires `(U_j,W_j)` sans
relation différentielle.

## Résultat négatif complémentaire : le halo fixé par `v_j`

Les hypothèses du cycle 0034 privées de `|Q_j|<=C_0v_j` ne produisent pas un
ensemble `H_j` de volume `O(v_j)` qui porte une fraction uniforme du registre
BV. Fixons un potentiel non constant `Phi`, compact dans
`{1/2<r<3/2, |z|<1}` et égal à un sur un ouvert. Pour `L>=1`, posons

```text
R_L=L,
A_L=L^-1,
F_L(r,z)=A_L Phi(r/L,z/L),
U_L=(L/r)F_L e_theta.
```

Alors les deux endpoints restent constants par scaling, tandis que

```text
|Q_L|~L^3,
integral|W_L|~L,
||W_L||_infinity~L^-2.
```

Dans le grand plateau, choisissons artificiellement un témoin de volume
`v_L=1`. Les minorations de plateau, la borne d'amplitude, la relation exacte
`W_L=curl U_L` et le registre global
`integral|W_L|>=cA_Lv_L^(2/3)` sont uniformes. Pourtant, pour tout
`|H_L|<=Gamma v_L`,

```text
integral_(H_L)|W_L|<=C Gamma L^-2
                  =o(A_Lv_L^(2/3)).
```

Le premier quantificateur faux est que `v_j`, qui minore seulement un ensemble
témoin, calibrerait par le haut tout le superniveau actif. La bande dynamique
du théorème 1 contourne ce faux énoncé : son volume est mesuré par la fonction
de distribution globale, jamais par un `v_j` choisi à l'avance.

## Preuve à constantes suivies

Pour `0<eta<1`, choisissons `lambda>0` tel que

```text
lambda |{|U|>lambda}|^(1/3)>=(1-eta)K_u.         (3)
```

Pour chaque cellule et chaque signe `sigma in {-1,+1}`, définissons les
ensembles tridimensionnels axisymétriques

```text
E_(j,sigma)={sigma F_j>lambda/2},
V_(j,sigma)=|E_(j,sigma)|,
H_(j,sigma)={lambda/4<sigma F_j<lambda/2}.       (4)
```

On ne conserve que les couples de volume positif, et on note `E`, `H` leurs
unions. Les facteurs annulaires donnent exactement les inclusions

```text
{|U|>lambda} subset E subset {|U|>lambda/3},
H subset {|U|>lambda/6}.                         (5)
```

En effet `1/2<r/R_j<3/2`, donc `2/3<R_j/r<2`. Par disjonction,

```text
V=sum_(j,sigma)V_(j,sigma)
 >=|{|U|>lambda}|,                               (6)
|H|<=(6K_u/lambda)^3.                            (7)
```

### Coaire localisée dans la bande

À presque tout niveau `s in (lambda/4,lambda/2)`, le superniveau
`{sigma F_j>s}` contient `E_(j,sigma)`. La formule de coaire en dimension
trois et (1) donnent

```text
integral_(H_(j,sigma)) |nabla F_j|
 >=(C_I lambda/4)V_(j,sigma)^(2/3).              (8)
```

Sur l'anneau, `|W_j|=(R_j/r)|nabla F_j|>=(2/3)|nabla F_j|`. Les bandes
signées et les supports cellulaires sont disjoints, donc

```text
integral_H |W|
 >=(C_I lambda/6)sum_(j,sigma)V_(j,sigma)^(2/3). (9)
```

Cette étape est le nouveau registre : la masse de curl n'est pas intégrée sur
la boîte support, mais uniquement là où `|F_j|` traverse un niveau absolu
commun.

### Sélection de cellule

Posons

```text
epsilon=max_j K_(u,j).
```

Sur `E_(j,sigma)`, `|U_j|>lambda/3`, d'où

```text
V_(j,sigma)^(1/3)<=3epsilon/lambda.              (10)
```

Par conséquent,

```text
sum V_(j,sigma)^(2/3)
 >=lambda V/(3epsilon).                          (11)
```

Les équations (3), (6), (9) et (11) impliquent

```text
integral_H |W|
 >=C_I(1-eta)^3 K_u^3/(18 epsilon lambda).       (12)
```

La borne de réarrangement faible-Lorentz, avec sa constante exacte trois,
et (7) donnent en sens opposé

```text
integral_H |W|
 <=3K_w|H|^(1/3)
 <=18K_wK_u/lambda.                              (13)
```

La comparaison de (12) et (13), puis `eta->0`, fournit

```text
epsilon>=(C_I/324)K_u^2/K_w.                    (14)
```

La famille finie atteint son maximum. Comme les supports des curls sont
disjoints, `K_(w,j_*)<=K_w`; (2) suit. Aucune somme triangulaire de
quasi-normes n'a été utilisée.

## Loi d'échelle

Sous

```text
U^(rho)(x)=rho U(rho x),
W^(rho)(x)=rho^2 W(rho x),
```

les quatre quasi-normes de (2) sont invariantes. Dans (8), `lambda` se
multiplie par `rho`, `V^(2/3)` par `rho^-2`, et les deux membres ont donc
l'homogénéité `rho^-1`, comme `integral_H|W|`. La constante `C_I/324` est
universelle une fois la convention de périmètre fixée; elle ne dépend jamais
de `R_j`, la longueur axiale ou le nombre de cellules.

## Expérience décisive

Le certificat `COMMON-LEVEL-HALO-SELECTION-1` sépare deux tests.

1. **Ledger commun.** Pour 1 536 familles, il génère 12 288 superniveaux
   signés de volumes cubes, place toutes les inégalités analytiques à leur
   bord algébrique et vérifie, après cubage,

   ```text
   epsilon^3 324^3 K_w^3>=K_u^6.
   ```

2. **Queue dyadique.** Les niveaux `2^-k` occupent des volumes `8^k`.
   Le quotient volume support/volume coeur atteint
   `5396990266136737387081`, tandis que `1<=K_u^3<8/7`. La bande commune
   conserve un budget de curl faible strictement positif; gonfler le support
   à faible amplitude ne supprime pas le niveau qui porte `K_u`.

Le script exécute 10 837 assertions en arithmétique `Fraction`, sans graine.
Résidu algébrique maximal : zéro. Empreinte SHA-256 :
`b197d3b45af0f034c09c91d4b7bb6d3be55293ab1f458ec769c250c8998490f8`.

Le calcul encode l'isopérimétrie avec `C_I=1`; il ne prouve pas la formule de
coaire au continuum et ne discrétise aucune PDE.

## Veille différentielle

Les briques publiées restent la formule de coaire de Fleming–Rishel
`NS-SRC-0132`, l'isopérimétrie euclidienne de Federer–Fleming
`NS-SRC-0148` et les règles de réarrangement Lorentz `NS-SRC-0067`. La veille
contrôlée n'a trouvé aucun
énoncé publié sélectionnant une même cellule pure-swirl par les deux endpoints
faibles selon (2); la composition est une dérivation interne.

Les notices primaires consultées le 2026-08-14 laissent inchangés
Lei–Ren–Tian `2501.08976v1`, Grujić `2511.00725v3`, Grujić
`2607.08866v2` et Barker `2510.20757v3`. Aucun de ces manuscrits ne contient
le lemme statique (2). Les résultats Barker–Prange `NS-SRC-0146`–`0147`
restent le raccord dynamique Type I le plus proche, sous solution singulière
déjà supposée.

Les sources `NS-SRC-0148`–`0155` ajoutent l'isopérimétrie globale, ses
variantes relatives, le cas limite de concentration-compacité, les outils de
covering/good-lambda et trois localisations dynamiques Navier–Stokes. Le corpus
atteint 155 sources; ces analogues ne sont pas attribués au théorème 1.

## Passes contradictoires séparées

- Audit analytique et quantificateurs :
  `c0ba565ecca14e107cfb88a0a92da4124c1c2b7d9e89088d9e92c74956d7d769`.
- Contre-modèle pure-swirl à queue dyadique :
  `a178fbf713eb79bfc0622e329bb2b4c057918658aa61e06e2a06ec40ebc8a1ec`.
- Audit primaire coaire, isopérimétrie et localisation :
  `f4a6798185a91808b6fb950425bb3b0055e7fa2c64d04acbd09554e584658642`.

Ces passes proviennent d'agents IA du même environnement. Elles sont séparées
et reproductibles, mais ne constituent pas une revue éditoriale indépendante.

## Passe contradictoire principale

1. **Coaire plane prise pour coaire tridimensionnelle.** Les volumes `V` sont
   tridimensionnels et (8) utilise directement le périmètre dans `R3`; aucun
   rapport d'aspect axial n'est perdu.
2. **Facteur cylindrique.** Le lift de `F_j` est lisse car son support reste
   loin de l'axe, et `R_j/r>=2/3` est suivi dans (5), (8) et (9).
3. **Signes.** Les superniveaux positifs et négatifs sont séparés avant
   coaire; leurs bandes sont disjointes.
4. **Queue de faible amplitude.** Si elle reste sous `lambda/4`, elle n'entre
   pas dans `H`; si elle dépasse ce niveau, son volume est compté dans
   `{|U|>lambda/6}` et donc dans (7).
5. **Section variable ou topologie compliquée.** L'isopérimétrie de `R3`
   dépend seulement du volume du superniveau, pas de sa paramétrisation.
6. **Supremum faible non atteint.** Le paramètre `eta` de (3) est conservé
   jusqu'à (12), puis tend vers zéro.
7. **Mauvaise somme de quasi-normes.** Seules les distributions des unions
   disjointes sont employées.
8. **Support du curl.** Pour des supports compacts complètement disjoints,
   `W=W_j` sur chaque bande; des cellules dont les closures se touchent ne sont
   pas couvertes.
9. **Constante de Lorentz.** `3` est exactement `p/(p-1)` pour `p=3/2`;
   combinée aux facteurs `6`, `3` et `6`, elle produit `324`.
10. **Diamètre pris pour volume.** (7) contrôle seulement `|H|`. Une bande de
    petit volume peut rester dispersée sur une très grande distance.
11. **Gate directionnel.** Sans diamètre `O(R_j)`, le théorème du cycle 0033
    ne s'applique pas automatiquement à la cellule sélectionnée; la puissance
    douze n'est pas revendiquée dans cette généralité.
12. **Clay.** Le résultat est cinématique et pure-swirl. Pression, diffusion,
    stretching, temps et sélection pré-singulière restent absents.

## Résultat scientifique et pivot

Le faux échappement `|Q_j|/v_j->infinity` est fermé pour la sélection endpoint
de toute famille pure-swirl annulaire disjointe : le support entier n'est
jamais le bon ensemble d'intégration. La bande à niveau absolu commun possède
à la fois le coût de coaire et le volume faible-Lorentz nécessaire.

Le résultat ne localise toutefois pas cette bande dans une boule. Le verrou
actif devient `GAP-ACTIVE-HALO-DIAMETER-OR-OVERLAP` : dispersion de nombreuses
composantes actives reliées par des filaments sous le seuil, puis seulement
chevauchement et annulation entre cellules.

## Prochaine expérience décisive

Construire une cellule pure-swirl dont le superniveau commun se décompose en
`m` gouttelettes de diamètre `R` séparées par des distances croissantes et
reliées par un filament sous `lambda/4`. Calculer la distribution du curl de
tous les raccords, puis décider si coaire et le budget faible-Lorentz
sélectionnent une goutte de bon rapport dans une boule de diamètre contrôlé,
ou si la dispersion réintroduit le contre-exemple dyadique du cycle 0034.
