# Cycle 0062 — contre-test instantané de cohérence de signe modale

Date : 2026-08-15.

Statut : **AI_INTERNAL_DERIVATION + COMPUTATION_ONLY**. Le calcul porte sur
des champs de Schwartz divergence-free et sur le champ vectoriel exact de
l'équation renormalisée à un instant. Il ne construit ni solution ancienne,
ni orbite Type I, ni singularité.

## Décision adaptative

Le verrou relu est
`GAP-TYPE-I-INTRINSIC-AXISYMMETRY-DEFECT-OR-MODAL-SIGN-COHERENCE`.

| action candidate | nouveauté | tractabilité | falsifiabilité | levier | total |
|---|---:|---:|---:|---:|---:|
| champ de Schwartz multi-mode et numérateurs PDE exacts | 5 | 5 | 5 | 5 | **20** |
| chercher directement une coercivité signée des triades | 4 | 2 | 4 | 5 | 15 |
| remplacer la phase par un défaut critique de Haar | 4 | 3 | 4 | 5 | 16 |

La première action est sélectionnée. Le lemme adverse minimal est :

> **Lemme de signe universel candidat.** Pour tout champ de Schwartz réel
> divergence-free sur `R3`, les numérateurs non nuls
> `C_m=<P_m d(Z),mathcal R Z_m>_L2` du champ vectoriel renormalisé ont un
> signe commun.

Le cycle **réfute** ce lemme par deux mécanismes indépendants : une triade à
trois isotypes, puis une torsion radiale de phase à deux isotypes.

## Formulation figée

Sur `R3`, sans frontière, avec viscosité un et force extérieure nulle, on
considère à un instant similaire le champ vectoriel

```text
d(Z)=Delta Z-P div(Z tensor Z)-kappa(1+y dot nabla)Z,
div Z=0,
```

où `P` est la projection globale de Leray et `kappa` est fixé. Les champs
testés sont réels, lisses et de Schwartz. Ils sont donc des données
admissibles pour la théorie forte locale, mais aucune intégration temporelle
n'est effectuée ici.

L'action covariante autour de `e3` est

```text
(rho(theta)Z)(y)=Q_theta Z(Q_-theta y),
mathcal R Z = d/dtheta rho(theta)Z|_(theta=0).
```

Le projecteur réel `P_m` rassemble les fréquences complexes `+m` et `-m`.
Pour `Z_m=P_mZ`, on pose

```text
C_m(Z)=<P_m d(Z),mathcal R Z_m>_L2,
G_m(Z)=||mathcal R Z_m||_L2^2.
```

Ce sont les numérateurs et Grams de la vitesse modale du cycle 0061 dans la
métrique globale `L2`. Les `C_m/G_m` ont le signe des `C_m`, puisque
`G_m>0` sur chaque mode actif.

## Décomposition exacte des numérateurs

La passe formelle indépendante donne

```text
C_m=C_m^diff+C_m^conv+C_m^drift,
C_m^diff=0,
C_m^conv=integral P_m^(2)(Z tensor Z):nabla(mathcal R Z_m),
C_m^drift=-kappa m <(y dot nabla)Z_m,J_m Z_m>.
```

L'annulation diffusive utilise simultanément l'auto-adjonction de `Delta`,
l'antisymétrie de `mathcal R` et leur commutation. Le terme unité du drift
s'annule, mais `y dot nabla` multiplié par la structure complexe `J_m` est
une forme auto-adjointe qui n'a pas de signe.

Dans la complexification, avec `Z_C=sum_k z_k`, la contribution convective
s'écrit, avec la convention du rapport formel,

```text
C_m^conv
 =2m Im sum_(k+l=m) integral
   (z_k tensor z_l):nabla conjugate(z_m).
```

La règle `k+l=m` est exacte. Elle sélectionne les triades mais n'impose pas
le signe de leur phase.

### Pression et projection de Leray

La pression n'est pas supposée locale ni nulle. Sur `R3`, pour
`N=div(Z tensor Z)`, elle est recalculée par la jauge de Riesz globale,

```text
pi=(-Delta)^(-1) partial_i partial_j(Z_i Z_j),
P N=N+nabla pi
```

avec les conventions de signe correspondantes pour `Delta`. Comme
`mathcal RZ_m` est exactement divergence-free et de Schwartz,

```text
<P N,mathcal RZ_m>
 =<N,P mathcal RZ_m>
 =<N,mathcal RZ_m>.
```

Cette identité utilise l'auto-adjonction globale de `P`; elle ne justifierait
pas la suppression d'une pression harmonique après une coupure locale.

## Contre-modèle triadique à trois modes

Écrivons `r2=x^2+y^2+z^2` et

```text
h_1c=x,                    h_1s=y,
h_2c=x^2-y^2,              h_2s=2xy,
h_3c=x^3-3xy^2,            h_3s=3x^2y-y^3.
```

Pour un polynôme `h`, le champ

```text
Z[h]=curl(0,0,h exp(-r2))
```

est réel, divergence-free et de Schwartz. Le certificat choisit

```text
Z_1=Z[-h_1c-h_1s],
Z_2=Z[-h_2c-h_2s],
Z_3=Z[-h_3c+h_3s],
Z=Z_1+Z_2+Z_3.
```

Tous les calculs sont exacts dans `Fraction`. Les facteurs gaussiens communs
sont conservés symboliquement :

```text
(C_1,C_2,C_3)
 =(-8/9,+16/9,-16/3)*(pi/3)^(3/2),
(G_1,G_2,G_3)
 =(2,12,54)*(pi/2)^(3/2).
```

Les projections de la diffusion et du drift sont nulles mode par mode pour
ce champ. Les valeurs affichées sont donc celles du champ vectoriel complet,
indépendamment de `kappa`. Les modes actifs ont les signes `(-,+,-)` : la
cohérence universelle est réfutée.

La première famille adverse, limitée aux seuls modes `m=1,2` construits avec
les mêmes potentiels axiaux et toutes les orientations entières non nulles
dans `[-2,2]^2`, ne trouve aucun partage : sur 576 cas,
`C_2=2 C_1`. Cet échec est conservé; l'ajout du mode `m=3` crée la première
triade de phase capable de rompre le signe dans cette famille.

## Contre-modèle de drift à deux modes

Le second mécanisme ne dépend pas d'une triade active. Pour

```text
p_(m,a)=Re[(x+i y)^m(1+i a r2)],
Z_(m,a)=curl(0,0,p_(m,a) exp(-r2)),
```

on prend `Z=Z_(1,+1)+Z_(3,-1)`. Les sommes de fréquences de deux éléments de
`{+/-1,+/-3}` sont dans `{0,+/-2,+/-4,+/-6}`; la convection n'a donc aucune
projection sur les modes actifs `1,3`. Le certificat obtient

```text
(G_1,G_3)=(39/16,2349/16)*(pi/2)^(3/2),
C^diff=(0,0),
C^conv=(0,0),
<(1+y dot nabla)Z_m,mathcal RZ_m>
 =(-7/2,+99/2)*(pi/2)^(3/2).
```

Ainsi, pour `kappa=1`,

```text
(C_1,C_3)=(+7/2,-99/2)*(pi/2)^(3/2).
```

Plus généralement, les signes restent opposés pour tout `kappa` non nul.
Ce deuxième exemple empêche d'attribuer le contre-signe uniquement au choix
d'une triade particulière.

## Échelle et constantes

Sous l'échelle physique `Z_lambda(y)=lambda Z(lambda y)`,

```text
G_m(Z_lambda)=lambda^(-1)G_m(Z),
C_m^conv(Z_lambda)=lambda C_m^conv(Z),
C_m^drift(Z_lambda)=lambda^(-1)C_m^drift(Z).
```

La vitesse convective `C_m^conv/G_m` est multipliée par `lambda^2`, tandis
que la contribution du drift à `C_m/G_m` est invariante. Le champ vectoriel
renormalisé avec `kappa != 0` fixe donc une échelle et n'est pas homogène sous
la seule dilatation physique. Aucune constante uniforme de passage à une
orbite Type I n'est obtenue.

## Test adverse reproductible

Le script utilise uniquement la bibliothèque standard Python : dictionnaires
de polynômes, coefficients `Fraction` et moments gaussiens exacts. Il vérifie

- divergence nulle des champs et tangentes;
- identité isotypique `mathcal R^2Z_m=-m^2Z_m`;
- orthogonalité des isotypes;
- annulations diffusion, drift ou convection annoncées;
- réduction globale de Leray contre les tangentes solénoïdales;
- recherche exhaustive des 576 orientations à deux modes;
- valeurs rationnelles des deux contre-modèles.

Commande :

```powershell
python -B experiments/navier-stokes/instantaneous-modal-sign/instantaneous_modal_sign.py
```

Le résidu algébrique de chaque identité testée est exactement nul; il n'y a
ni quadrature, ni discrétisation, ni graine aléatoire.

## Veille primaire différentielle

La revue indépendante n'a trouvé aucune identité publiée imposant
`C_m=0` ou `sum_m C_m=0` dans ce cadre. Elle sépare trois objets souvent
confondus :

- Waleffe 1992 (`NS-SRC-0225`) annule la somme des transferts **radiaux**
  d'énergie d'une triade hélicoïdale, pas leur quadrature tangentielle;
- Charnyi--Heister--Olshanskii--Rebholz 2017 (`NS-SRC-0226`) testent le
  moment angulaire contre le champ de Killing fixe `x cross e_i`, distinct
  de la tangente d'état `mathcal RZ`;
- Yeung--Chu--Schmidt 2026 (`NS-SRC-0227`) donnent des cancellations
  collectives d'énergie par paires, sextuplets et somme globale, tout en
  conservant des transferts individuels signés;
- Willis--Cvitanović--Avila 2013 (`NS-SRC-0221`) sourcent l'action diagonale
  du générateur sur les modes azimutaux d'un pipe flow numérique, sans loi
  de signe;
- Pineau--Vicol 2026 v2 (`NS-SRC-0051`) obtiennent dans un produit gaussien
  RSS un couplage tangent entre rotation et non-linéarité-plus-pression, non
  une annulation par isotype.

Les domaines périodiques, les pipes forcés, les produits gaussiens, les
modèles décimés et les données turbulentes ne se transfèrent pas directement
au problème Clay sur `R3`. La veille soutient seulement le résultat négatif
de portée : les symétries sélectionnent les triades, elles n'en signent pas
la phase.

## Passe contradictoire et portée

1. **Instantané n'est pas ancien.** Une donnée de Schwartz produit une
   solution forte locale, mais rien ne montre que cette donnée appartient à
   une orbite ancienne suitable, Type I, capturée et minimale.
2. **Projection globale seulement.** L'annulation du gradient de pression
   ne survit pas telle quelle à une localisation spatiale.
3. **Bloc réel.** Les fréquences `+m,-m` forment un seul isotype réel; elles
   ne doivent pas être comptées comme deux vitesses indépendantes.
4. **Énergie.** Elle contraint `sum_m<d_m,Z_m>`, pas
   `sum_m<d_m,mathcal RZ_m>`.
5. **Moment angulaire.** Son test linéaire non `L2` et son identité propre ne
   donnent aucun signe à ces numérateurs quadratiques.
6. **Échelle.** Convection et drift renormalisé ne portent pas le même poids.
7. **Calcul exact mais fini.** Le certificat prouve les identités de cette
   famille, pas un théorème de classification des champs multi-modes.

Le résultat logique exact est donc :

```text
structure Navier--Stokes instantanée + divergence nulle + covariance SO(2)
  -/-> cohérence universelle de signe des vitesses modales.
```

Il ne réfute pas une cohérence supplémentaire imposée par l'ancienneté, la
capture Type I, la minimalité d'un élément critique ou une hypothèse
géométrique encore inconnue.

## Décision

`FAIL-NS-0098` abandonne la production du signe par les seules symétries,
l'énergie, le moment angulaire ou la structure instantanée de l'opérateur.
Le claim
`NS-TYPE-I-INSTANTANEOUS-MODAL-SIGN-COUNTEREXAMPLE` reste
`COMPUTATION_ONLY` et reçoit une revue contradictoire. Le verrou est resserré
en `GAP-TYPE-I-DYNAMIC-MODAL-CONE-OR-INTRINSIC-HAAR-DEFECT`.

L'expérience suivante doit tester un **cône dynamique**, et non répéter un
test instantané : dériver `dC_m/ds` le long du champ vectoriel renormalisé,
construire une donnée située sur la frontière d'un cône modal unilatéral et
chercher un franchissement exact. Un franchissement réfuterait l'invariance
locale du cône; une tangence systématique isolerait une structure nouvelle à
démontrer. Après cet essai distinct, un nouvel échec de la stratégie modale
imposera le pivot vers un défaut de Haar critique intrinsèque ou la rigidité
RSS faible-`L3` intermédiaire.
