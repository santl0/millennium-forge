# Cycle 0055 — classification des orbites relatives de rotation exactes

Date : 2026-08-15.

Statut : `AI_INTERNAL_DERIVATION`; aucune conclusion Clay.

## Décision adaptative

Le verrou relu est
`GAP-TYPE-I-RENORMALIZED-TANGENTIAL-ACTIVITY-CLASSIFICATION`. Les trois
actions candidates sont notées avant la dérivation :

| action | nouveauté | tractabilité | falsifiabilité | levier | total |
|---|---:|---:|---:|---:|---:|
| classifier les orbites SO(2) exactes à vitesse variable | 4 | 5 | 5 | 5 | **19** |
| étendre l'observabilité pondérée Pineau--Vicol au faible-`L3` suitable | 5 | 2 | 4 | 5 | 16 |
| calculer directement le flux calorifié sur un ansatz RSS | 4 | 3 | 5 | 3 | 15 |

La première action est sélectionnée. Le lemme actif est unique : montrer
qu'une trajectoire exacte de l'équation renormalisée qui reste sur une même
orbite de rotations a nécessairement une vitesse angulaire constante, sauf
si le profil est invariant par rotation et la trajectoire stationnaire.

## Cadre exact

Fixons `kappa>0`. Sur `R3 x I`, sans frontière, avec viscosité un et force
nulle, écrivons l'équation projetée renormalisée

```text
partial_s Z+F_kappa(Z)=0,
F_kappa(Z)=-Delta Z+P div(Z tensor Z)+kappa D Z,
D Z=(1+y dot nabla)Z,
div Z=0.                                                   (55.1)
```

L'intervalle `I` est connexe et non dégénéré. La projection de Leray est la
projection globale sur `R3`; la pression équivalente est dans la jauge de
Riesz. Pour le lemme algébrique, il suffit que `U` soit une distribution
solénoïdale telle que `U tensor U` définisse une distribution. En
particulier, `U in L^(3,infinity)` convient localement puisque
`U tensor U in L^(3/2,infinity)_loc subset L1_loc`.

La rotation est autour de l'axe `e_3`, passant par l'origine des variables
similaires. Soient `R_theta=exp(theta J)` et l'action sur les champs

```text
(Q_theta U)(y)=R_theta U(R_(-theta)y).                    (55.2)
```

Une rotation autour d'un axe déplacé ne commute pas avec le drift `D` et ne
relève pas de ce lemme sans recentrage explicite.

## Générateur et équivariance

Le générateur infinitésimal de (55.2) est

```text
mathcal R U=J U-(J y dot nabla)U.                         (55.3)
```

En distributions,

```text
d/dtheta Q_theta U=Q_theta mathcal R U.                   (55.4)
```

Le Laplacien, le drift isotrope `D`, la divergence et la projection de
Leray commutent avec les rotations orthogonales. Le produit tensoriel est
covariant. Par conséquent,

```text
F_kappa(Q_theta U)=Q_theta F_kappa(U).                    (55.5)
```

Cette formule conserve la pression non locale : les doubles transformées de
Riesz se transforment comme un tenseur sous `SO(3)`. Aucune annulation locale
de pression n'est utilisée.

## Lemme de classification exacte

Supposons

```text
theta in W^(1,1)_loc(I),
Z(s)=Q_(theta(s))U                                      (55.6)
```

et que `Z` résolve (55.1) dans les distributions espace--temps. La règle de
chaîne faible pour l'orbite fortement continue donne, pour presque tout `s`,

```text
partial_s Z=theta'(s)Q_(theta(s))mathcal R U.             (55.7)
```

En utilisant (55.5) et en appliquant `Q_(-theta(s))` à (55.1),

```text
theta'(s)mathcal R U+F_kappa(U)=0                         (55.8)
```

dans les distributions spatiales, pour presque tout `s`.

Deux cas seulement sont possibles.

### Cas invariant

Si `mathcal R U=0`, alors (55.4) implique `Q_theta U=U` pour tout `theta`.
Ainsi `Z(s)=U` pour presque tout `s`, quelle que soit la représentation
redondante `theta(s)`, et

```text
F_kappa(U)=0.                                             (55.9)
```

La trajectoire physique est stationnaire en temps similaire. Ce cas inclut
les profils axisymétriques autour de `e_3`; il ne suppose pas que `U=0` avant
d'appliquer un théorème de Liouville.

### Cas de groupe libre infinitésimalement

Si `mathcal R U` n'est pas la distribution nulle, choisissons un test
solénoïdal lisse compact `phi` tel que
`c=<mathcal R U,phi> != 0`. En appariant (55.8),

```text
theta'(s)c+<F_kappa(U),phi>=0.                            (55.10)
```

Le second terme est indépendant de `s`; donc

```text
theta'(s)=alpha:=-<F_kappa(U),phi>/c                      (55.11)
```

presque partout. La connexité de `I` et l'absolue continuité donnent

```text
theta(s)=alpha s+theta_0.                                 (55.12)
```

En absorbant `theta_0` dans le profil, `Z` est une orbite RSS exacte à
vitesse constante. Le profil satisfait

```text
alpha mathcal R U-Delta U+P div(U tensor U)+kappa D U=0. (55.13)
```

Avec pression de Riesz, (55.13) devient

```text
alpha[J U-(J y dot nabla)U]
+kappa(U+y dot nabla U)-Delta U
+(U dot nabla)U+nabla Pi=0,
div U=0.                                                   (55.14)
```

Pour `kappa=1/2`, c'est exactement l'équation RSS utilisée par
Pineau--Vicol, à convention de rotation fixée.

## Stabilisateur et unicité du paramètre

Un profil peut avoir un stabilisateur discret, par exemple
`Q_(2pi/m)U=U`, sans vérifier `mathcal R U=0`. Cela rend la phase globale
définie modulo `2pi/m`, mais ne modifie pas (55.11) : toute représentation
localement absolument continue a la même vitesse `alpha` presque partout.
Seul un stabilisateur continu produit `mathcal R U=0` et rend `theta`
entièrement non identifiable.

Changer de paramétrisation sur un ensemble de mesure nulle ne change pas la
trajectoire ni la conclusion presque partout. En revanche, autoriser des
sauts entiers de période sans choisir un relèvement absolument continu
sort de l'hypothèse (55.6).

## Raccords rigoureux disponibles

1. Si `mathcal R U=0`, `U in W1,2_loc inter L^(3,infinity)` et `U` est le
   profil faible de Leray de coefficient `kappa>0`, la normalisation du cycle
   0053 puis le théorème publié de Guevara--Phuc imposent `U=0`.
2. Si `mathcal R U!=0`, le lemme ne conclut pas `U=0`; il réduit seulement
   l'orbite exacte à (55.14).
3. Sous la borne ponctuelle Type I
   `|U(y)|<=C/(1+|y|)`, la régularité de profil et les autres hypothèses de la
   prépublication Pineau--Vicol v2, (55.14) est triviale lorsque `|alpha|`
   est suffisamment petit ou suffisamment grand, avec seuils dépendant de
   `C`.
4. Le régime intermédiaire de `alpha` demeure explicitement ouvert dans
   cette prépublication. Une borne faible-`L3` n'implique pas la borne
   ponctuelle Type I et ne permet pas d'importer ses seuils.

Ainsi le lemme ferme la classe des rotations exactes à vitesse variable,
mais ne ferme ni toutes les RSS, ni les RDSS, ni les pseudo-orbites.

## Veille primaire et antériorité

Bradshaw--Tsai 2017 (`NS-SRC-0206`, publié) dérive l'équation dans un
repère similaire tournant avec vitesse `theta'(s)` variable. La covariance
RSS imposée pour tous les facteurs d'échelle donne chez eux une phase
logarithmique, donc une vitesse constante. Leur construction est forward et
ils ne formulent pas la réciproque distributionnelle (55.16) pour une
ancienne suitable.

Pineau--Vicol v2 (`NS-SRC-0051`, prépublication) énonce dans sa remarque 1.8
une classification informelle voisine des solitons Navier--Stokes, sous
conditions additionnelles de vitesse bornée et de décroissance de pression.
Ce n'est ni un théorème numéroté avec preuve faible détaillée, ni une
publication évaluée. Field 1980 (`NS-SRC-0207`) et Krupa 1990
(`NS-SRC-0208`) fournissent le cadre classique des systèmes dynamiques
équivariants et des équilibres relatifs en dimension finie.

L'apport vérifiable du présent cycle est donc borné : preuve
distributionnelle à axe fixe sous un relèvement `W^(1,1)_loc`, raccord exact
aux espaces faible-`L3` du pipeline et inventaire des constantes qui manquent
à la stabilité. Aucune priorité conceptuelle sur la théorie des équilibres
relatifs n'est revendiquée.

## Loi d'échelle

La norme `L^(3,infinity)` est invariante sous l'échelle physique
`u_lambda=lambda u(lambda x,lambda^2t)`. En temps similaire, `s` et l'angle
sont sans dimension; `alpha=dtheta/ds` est donc sans dimension. Les actions
`Q_theta` sont isométriques dans `L^(3,infinity)` et préservent les boules
centrées, la capture locale `L3`, `W1,2_loc` et la divergence nulle.

Le défaut modulé naturel

```text
M_R(s)=inf_(beta in R)
 ||partial_s Z(s)-beta mathcal R Z(s)||_(W_0^(1,(3,1))(B_R))*  (55.15)
```

est invariant par rotation à rayon fixé, mais pas encore contrôlé par une
quantité critique intégrable. Sa définition instantanée demande un
représentant presque partout; une version sur fenêtre est préférable pour
les solutions faibles.

## Pourquoi l'énoncé approché ne suit pas

Le passage de `M_R(s_n)->0` à une RSS limite exige au minimum :

1. une même sous-suite pour tous les rayons;
2. une borne puis une convergence des paramètres minimisants `beta_n`;
3. la convergence forte locale nécessaire au stress quadratique;
4. la persistance de `mathcal R U`, ou un traitement séparé de sa
   dégénérescence;
5. un contrôle de la pression globale et des queues après rotation;
6. l'alignement des fenêtres temporelles et des phases.

Sans borne de `beta_n`, le produit `beta_n mathcal R Z_n` peut rester fini
alors que `mathcal R Z_n->0`. Sans autonomie, (55.8) contient un terme
dépendant de `s` et `theta'` peut varier. Avec un résidu seulement petit,
(55.10) ne donne qu'une oscillation de vitesse divisée par
`|<mathcal R U,phi>|`; cette constante peut dégénérer.

## Passe contradictoire

1. **Signe du générateur.** La convention (55.2) donne
   `mathcal R U=JU-(Jy dot nabla)U`; inverser l'action inverse `alpha`.
2. **Pression.** La preuve utilise l'équation projetée globale; une pression
   locale modulo harmonique ne suffit pas à établir (55.5) sans raccord.
3. **Axe.** L'axe passe par l'origine similaire. Une translation mobile
   ajoute un générateur de transport et change la classification.
4. **Temps.** `theta` est localement absolument continue. Une phase seulement
   mesurable ne possède pas la règle de chaîne (55.7).
5. **Stabilisateur.** Symétrie discrète ne signifie pas
   `mathcal R U=0`; seule l'invariance continue rend la trajectoire
   stationnaire.
6. **Faible-`L3`.** La classification distributionnelle est compatible avec
   faible-`L3`, mais les Liouville RSS récents demandent davantage.
7. **Suitability.** Elle n'est pas utilisée dans l'algèbre; elle redevient
   nécessaire pour produire le profil depuis une singularité et passer aux
   limites.
8. **Approximation.** Petit défaut modulé n'implique pas orbite exacte sans
   compacité des paramètres et borne inférieure du générateur rotationnel.
9. **RDSS.** Une trajectoire périodique générale n'est pas contenue dans une
   unique orbite `Q_theta U`; le lemme ne la rend pas RSS.
10. **Clay.** La réduction reste conditionnelle au pipeline Type I et ne
    traite ni Type II ni l'existence d'un profil non trivial.

## Résultat et pivot

Le résultat positif est la dichotomie exacte

```text
orbite SO(2) exacte d'une PDE autonome équivariante
  => profil invariant et trajectoire stationnaire
     ou vitesse constante et équation RSS.                (55.16)
```

Le résultat négatif est

```text
petit défaut modulé local
  -/-> RSS limite sans contrôle de beta et de mathcal R Z. (55.17)
```

La vitesse variable exacte n'est donc pas un nouveau scénario. Le verrou est
raffiné en

```text
GAP-TYPE-I-APPROXIMATE-ROTATION-MODULATION-COMPACTNESS.    (55.18)
```

La prochaine expérience décisive doit tester une suite
`partial_s Z_n-beta_n mathcal R Z_n -> 0` sous les bornes compactes du
pipeline, en séparant `beta_n` borné, `|beta_n|->infinity` et
`mathcal R Z_n->0`. Le cas borné doit converger vers RSS; le cas dégénéré
doit être raccordé au profil stationnaire plutôt que divisé par un angle qui
tend vers zéro. Avant même cette estimation, il faut vérifier qu'une
trajectoire seulement connue comme appartenant à l'orbite admet un relèvement
de phase absolument continu dans la topologie distributionnelle disponible.
