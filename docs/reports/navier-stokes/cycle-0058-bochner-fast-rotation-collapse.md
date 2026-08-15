# Cycle 0058 — collapse Bochner des rotations rapides

Date : 2026-08-15.

Statut : `AI_INTERNAL_DERIVATION`; amélioration conditionnelle du cycle 0057,
aucune conclusion Clay.

## Décision adaptative

Le verrou relu est
`GAP-TYPE-I-FAST-ROTATION-STROBOSCOPIC-OR-RSS-RIGIDITY`. Trois actions
réellement distinctes sont notées avant la dérivation :

| action | nouveauté | tractabilité | falsifiabilité | levier | total |
|---|---:|---:|---:|---:|---:|
| exploiter la dérivée temporelle de Bochner fournie par la PDE | 5 | 5 | 5 | 5 | **20** |
| dériver une condition de phase et contrôler sa matrice de Gram | 4 | 4 | 5 | 4 | 17 |
| reproduire les seuils RSS extrêmes puis attaquer l'intervalle intermédiaire | 3 | 3 | 4 | 4 | 14 |

La première action est sélectionnée. Le cycle 0057 divisait une dérivée
temporelle seulement distributionnelle par `beta_n`; le test mobile
`phi/beta_n` faisait alors apparaître `partial_s(1/beta_n)` et exigeait une
petite variation totale. Mais le ledger Navier--Stokes du cycle 0045 contient
une information supplémentaire : `partial_s Z_n` est déjà une fonction de
Bochner uniformément bornée dans un espace spatial négatif. La division peut
donc être effectuée presque partout dans cet espace, sans intégration par
parties temporelle.

## Cadre exact

Fixons un intervalle ouvert `I`, `kappa>0` et l'action centrée de `SO(2)`
autour de l'axe `e_3` :

```text
(Q_theta U)(y)=R_theta U(R_(-theta)y),
mathcal R U=J U-(Jy dot nabla)U.                         (58.1)
```

Pour chaque `n`, `Z_n` est un champ classique divergence-free sur
`R3 x I`, solution de

```text
partial_s Z_n-Delta Z_n+div(Z_n tensor Z_n)+nabla Pi_n
 +kappa(1+y dot nabla)Z_n=F_n,
div Z_n=0.                                               (58.2)
```

Le domaine est `R3`, sans frontière, la viscosité vaut un. Dans le pipeline
Type I, `F_n` est la force du cutoff extérieur et tend vers zéro sur tout
compact; pour l'équation limite et le problème Clay non forcé, `F_n=0`.

Sur tout `J compactement inclus dans I` et toute boule centrée `B_(2R)`, on
suppose le ledger brut uniforme

```text
sup_n ||Z_n||_(L-infinity(J;L^(3,infinity)(R3)))<=M,
Pi_n=R_iR_j((Z_n)_i(Z_n)_j),
sup_n ||F_n||_(L1(J;W^(-2,4/3)(B_(2R))))<=C^F_(J,R).
                                                               (58.3)
```

La forte `L3_loc`, l'énergie locale et la capture ne sont pas utilisées dans
le cœur de collapse; elles reviennent au passage PDE, à suitability et à la
non-trivialité.

La vitesse de phase est seulement mesurable :

```text
beta_n:J->R,
b_(n,J):=ess inf_(s in J)|beta_n(s)| ->infinity.         (58.4)
```

Aucune hypothèse `W^(1,1)`, aucun signe fixe et aucune variation de
`q_n=1/beta_n` ne sont imposés. Enfin,

```text
r_n:=partial_s Z_n-beta_n mathcal R Z_n                  (58.5)
```

est supposé représenté dans l'espace de Bochner

```text
sup_n ||r_n||_(L1(J;W^(-2,4/3)(B_R)))<=C^r_(J,R).        (58.6)
```

Pour la stationnarité, la condition minimale porte seulement sur la partie
moyenne du défaut :

```text
mathcal A r_n ->0 dans D'(I x R3).                       (58.7)
```

La condition plus forte `r_n->0` suffit bien sûr.

Chaque champ est lisse individuellement, donc le produit temporel
`beta_n mathcal R Z_n` est défini. L'hypothèse (58.6) ne prétend pas que la
vitesse de phase est construite depuis `Z_n`; elle mesure le défaut d'une
modulation déjà sélectionnée.

## Dérivée temporelle de Bochner fournie par l'équation

Posons

```text
X_R=W^(-2,4/3)(B_R)=(W_0^(2,4)(B_R))^*.                 (58.8)
```

Sur une boule de mesure finie, les inclusions faible--fort donnent

```text
||Z_n||_(L^(4/3)(B_R))<=C_R M,
||Z_n tensor Z_n||_(L^(4/3)(B_R))<=C_R M^2,
||Pi_n||_(L^(4/3)(B_R))<=C_R C_CZ M^2.                  (58.9)
```

Pour `phi in W_0^(2,4)(B_R)`, les termes de (58.2) satisfont

```text
|<Delta Z_n,phi>|<=||Z_n||_(4/3)||Delta phi||_4,
|<div(Z_n tensor Z_n),phi>|
  <=||Z_n tensor Z_n||_(4/3)||nabla phi||_4,
|<nabla Pi_n,phi>|<=||Pi_n||_(4/3)||div phi||_4,
|<(1+y dot nabla)Z_n,phi>|
  <=C(1+R)||Z_n||_(4/3)||phi||_(W^(1,4)).                (58.10)
```

La pression est recalculée : elle n'est ni omise ni remplacée par une
pression locale arbitraire. Les équations (58.2), (58.9)--(58.10) donnent

```text
||partial_s Z_n||_(L1(J;X_R))
 <=C_(J,R,C_CZ)[M+(1+|kappa|)M+M^2]+C^F_(J,R)
 =:C^dot_(J,R).                                          (58.11)
```

Dans le pipeline du cycle 0045, le membre de droite est même uniforme dans
`L-infinity(J;X_R)` avant l'estimation d'énergie locale. La version `L1`
suffit ici. Une formulation seulement suitable locale peut aussi fournir
(58.11) à partir de `Z in L3_loc`, `Pi in L^(3/2)_loc` et du ledger
d'énergie, mais ces constantes doivent être supposées uniformes sur la
suite; le mot « suitable » isolé ne les remplace pas.

## Lemme de division Bochner

L'identité (58.5) est une égalité presque partout à valeurs dans `X_R` :

```text
beta_n(s) mathcal R Z_n(s)
 =partial_s Z_n(s)-r_n(s).                             (58.12)
```

Pour les grands `n`, (58.4) autorise la division scalaire presque partout.
Par homogénéité de la norme,

```text
||mathcal R Z_n||_(L1(J;X_R))
 <=b_(n,J)^(-1)[
      ||partial_s Z_n||_(L1(J;X_R))
     +||r_n||_(L1(J;X_R))]
 <=[C^dot_(J,R)+C^r_(J,R)]/b_(n,J).                    (58.13)
```

Le membre droit tend vers zéro. Aucun test ne dépend de `n`; surtout, aucune
dérivée de `1/beta_n` n'apparaît. Si `Z_n->Z` dans les distributions, la
continuité du générateur donne aussi

```text
mathcal R Z_n ->mathcal R Z dans D'.                    (58.14)
```

Les équations (58.13)--(58.14) imposent

```text
mathcal R Z=0.                                           (58.15)
```

La limite est exactement axisymétrique autour de l'axe centré, swirl permis.
La convergence forte `L3_loc` du pipeline est beaucoup plus forte que la
convergence distributionnelle requise par ce seul passage.

Le même argument vaut plus généralement dans tout espace de Banach spatial
`X_R` où `partial_sZ_n` et `r_n` possèdent des représentants de Bochner
uniformément `L^p`, `1<=p<=infinity`. Il donne

```text
||mathcal RZ_n||_(L^p X_R)
 <=b_(n,J)^(-1)(||partial_sZ_n||_(L^pX_R)
                 +||r_n||_(L^pX_R)).                    (58.16)
```

La topologie doit être la même pour les deux termes. Une borne de
`partial_sZ_n` dans `X_R` et une convergence de `r_n` seulement dans `D'` ne
permettent pas (58.16).

## Moyenne de Haar et stationnarité

Définissons sur les distributions

```text
mathcal A W=(1/(2pi)) integral_0^(2pi)Q_theta W dtheta.
                                                               (58.17)
```

Sur les boules centrées, `mathcal A` est contractive dans les espaces
négatifs définis par dualité avec les normes de Sobolev invariantes. Elle
commute avec `partial_s` et

```text
mathcal A mathcal R=0.                                   (58.18)
```

En appliquant `mathcal A` à (58.5), sans aucune dérivée de `beta_n`, on
obtient

```text
partial_s(mathcal A Z_n)=mathcal A r_n.                  (58.19)
```

Sous (58.7), le passage à la limite donne

```text
partial_s(mathcal A Z)=0.                                (58.20)
```

L'identité (58.15) implique `mathcal AZ=Z`; donc

```text
partial_s Z=0.                                           (58.21)
```

La limite est un profil stationnaire en temps similaire.

## Passage Navier--Stokes et endgame

La forte convergence `Z_n->Z` dans `L3_loc` ferme le stress :

```text
Z_n tensor Z_n ->Z tensor Z dans L^(3/2)_loc.            (58.22)
```

Le ledger du cycle 0045 transmet séparément la pression proche/harmonique,
la dissipation et l'inégalité d'énergie locale. Sous la borne globale
faible-`L3`, la limite stationnaire `U=Z` satisfait

```text
-Delta U+P div(U tensor U)+kappa(1+y dot nabla)U=0,
U in W1,2_loc(R3) inter L^(3,infinity)(R3).               (58.23)
```

Après normalisation de `kappa>0`, le théorème publié de Guevara--Phuc donne
`U=0`. La capture cylindrique persistante du cycle 0046 donne au contraire
`U!=0`. Aucune suite capturée du pipeline Type I ne peut donc satisfaire
simultanément (58.3)--(58.7) et le ledger complet.

Pour une famille RSS exacte

```text
Z_n(s)=Q_(alpha_n s)U_n,
|alpha_n|->infinity,
r_n=0,                                                   (58.24)
```

la seule borne PDE uniforme de `partial_sZ_n` dans `X_R` force
`mathcal RZ_n->0` dans `L1X_R`. Une limite compacte capturée est donc
stationnaire puis interdite. Cette conclusion porte sur une famille sous un
ledger commun; elle ne prouve toujours pas la trivialité d'un profil RSS
individuel à vitesse donnée.

## Pourquoi la stroboscopie du cycle 0057 est exclue

Dans le contre-modèle positif du cycle 0057, `beta_N` vaut `N` ou `N^4`, la
phase effectue exactement `N^2` tours et

```text
Z_N(s)=Q_(theta_N(s))U,
r_N=0,
partial_sZ_N=beta_N Q_(theta_N)mathcal RU.               (58.25)
```

Sur une boule centrée contenant l'orbite de `U`, l'action est isométrique.
Pour tout espace négatif où `mathcal RU!=0`,

```text
||partial_sZ_N||_(L1X_R)
 =||mathcal RU||_(X_R) integral_0^1 beta_N(s)ds
 =N^2||mathcal RU||_(X_R)                                (58.26)
```

si la période angulaire est normalisée à un. La suite viole donc exactement
le ledger temporel (58.11). La stroboscopie reste un contre-exemple correct
au lemme purement cinématique du cycle 0057 sans borne de dérivée; elle n'est
pas compatible avec le paquet PDE uniforme utilisé ici.

Trois autres portes sont nécessaires :

1. avec `Z_n=U` non axisymétrique et `beta_n=n`, on a
   `partial_sZ_n=0` mais `r_n=-n mathcal RU`; omettre la borne uniforme sur le
   défaut rend la conclusion fausse;
2. si `Z` est une solution renormalisée axisymétrique lisse non stationnaire,
   alors `Z_n=Z`, `beta_n=n` et `r_n=partial_sZ` satisfont le ledger de
   collapse avec `Var(1/beta_n)=0`, mais `partial_sZ!=0`; la bornitude de
   `r_n` ne remplace donc pas (58.7), même pour une vraie solution PDE;
3. près du stabilisateur, `mathcal RZ_n->0` peut rendre `beta_n` arbitraire
   sans effet sur le champ. Le lemme conclut correctement l'axisymétrie mais
   ne construit ni ne rend unique la phase.

## Échelle et constantes

`beta_n` est une vitesse par unité de temps similaire et est sans dimension.
La constante de collapse est exactement

```text
[C^dot_(J,R)+C^r_(J,R)]/b_(n,J).                        (58.27)
```

L'espace local `W^(-2,4/3)(B_R)` est une topologie de compacité, pas une
norme critique globale. Sous la remise à l'échelle physique d'un terme de
force `f_lambda=lambda^3f(lambda x)`, la norme homogène correspondante porte
un facteur `lambda^(-5/4)`. Aucun passage uniforme `R->infinity` ou changement
d'échelle n'est caché dans (58.13). Le résultat est appliqué sur chaque
cylindre fixé du repère renormalisé, puis sur une exhaustion dénombrable.

La pression est non locale mais son contrôle global faible-Lorentz rend sa
restriction locale uniforme. Avec une pression seulement locale, une
composante harmonique et sa constante doivent être incluses dans
`C^dot_(J,R)`; l'équation testée seulement contre des champs solénoïdaux ne
suffit pas à revendiquer directement une borne vectorielle complète sans
raccord de Helmholtz.

## Passe contradictoire

1. **Bochner contre distribution.** La division presque partout est licite
   seulement parce que `partial_sZ_n` et `r_n` sont représentés dans le même
   `L1(J;X_R)`. Elle est fausse comme manipulation de distributions
   temporelles arbitraires.
2. **Défaut séparé.** Une borne de la dérivée PDE ne borne pas `r_n`; le champ
   constant non axisymétrique avec `beta_n=n` fait croître ce défaut comme
   `n`.
3. **Pression.** La projection solénoïdale élimine formellement la pression,
   mais la borne vectorielle (58.11) la recalcule dans la jauge de Riesz.
4. **Force.** Le cutoff externe est admis seulement avec constante locale
   uniforme; sa fuite globale dans l'espace critique reste celle du cycle
   0044.
5. **Zéros et signe.** (58.4) exclut les zéros presque partout pour les grands
   `n`, mais autorise des sauts de signe. Aucun théorème des valeurs
   intermédiaires n'est utilisé.
6. **Axe mobile.** Un axe ou centre dépendant de `n` change le générateur et
   détruit la moyenne de Haar commune.
7. **Stabilisateur.** Lorsque `mathcal RZ_n` est petit, la vitesse peut être
   grande ou non unique; seule la petitesse du produit déduite de (58.12)
   importe.
8. **Forte compacité.** Elle n'est pas nécessaire à (58.15), mais reste
   indispensable au stress, à la capture et à l'endgame suitable.
9. **Stationnarité.** La bornitude de `r_n` suffit au collapse, pas à
   (58.20); l'annulation distributionnelle de `mathcal Ar_n` en (58.7) reste
   nécessaire. Une solution axisymétrique autonome peut dépendre du temps.
10. **Type II.** Le ledger uniforme dépend de la borne Type I `M`; aucune
    constante uniforme lorsque `M_n->infinity` n'est produite.
11. **Clay.** Le résultat suppose toujours l'existence d'une modulation dont
    le défaut est uniformément borné. L'équation seule ne sélectionne pas
    `beta_n` et ne montre pas qu'une singularité arbitraire entre dans cette
    branche.

## Résultat et pivot

Le résultat positif renforcé est

```text
derivee PDE bornee dans L1_t W^(-2,4/3)_loc
+ defaut module borne dans le meme espace
+ ess inf|beta_n|->infinity
+ convergence distributionnelle
  => mathcal RZ=0 sans Var(1/beta_n);

+ mathcal A r_n->0 dans D'
  => Z stationnaire;

+ ledger suitable faible-L3 + capture
  => contradiction par Guevara--Phuc.                   (58.28)
```

Le cycle 0057 devient un lemme cinématique valide mais non optimal dans le
pipeline PDE. La prochaine porte est désormais

```text
GAP-TYPE-I-CANONICAL-PHASE-DEFECT-BOUND-OR-RSS-RIGIDITY. (58.29)
```

L'expérience décisive suivante doit construire une condition de phase
calculable depuis le champ total et déterminer si son défaut `r_n` est
uniformément borné dans `L1W^(-2,4/3)` lorsque la matrice de Gram dégénère.
Une simple estimation de `Var(1/beta_n)` n'est plus nécessaire. Si trois
sélections canoniques distinctes échouent sur la borne du défaut, la branche
pivotera vers la rigidité RSS faible-`L3` intermédiaire.
