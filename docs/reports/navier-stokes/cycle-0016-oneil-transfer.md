# Cycle 0016 — transfert O'Neil de la vorticité vers la vitesse

Date : 2026-08-14. Lemme actif : `ONEIL-TRANSFER-1`.

## Décision adaptative

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total | Décision |
|---|---:|---:|---:|---:|---:|---|
| rendre exact `(40) -> (41) -> (47)`, jauge et reste inclus | 3 | 5 | 5 | 5 | **18/20** | sélectionnée |
| auditer la queue dyadique du commutateur du théorème 4.1 | 5 | 2 | 4 | 5 | 16/20 | différée |
| synchroniser les constantes de (49) avec l'analyticité et la mesure harmonique | 4 | 3 | 5 | 5 | 17/20 | différée |

Le premier candidat ferme le premier raccord PDE immédiatement en amont du
lemme d'inversion du cycle 0015. Il se décompose en une inversion scalaire,
deux opérateurs de Hardy et une normalisation globale de Biot–Savart.

## Équation, domaine et notion de solution

La source ciblée considère Navier–Stokes incompressible 3D non forcé sur
`R³`, avec viscosité `nu>0` :

```text
partial_t u+(u·nabla)u-nu Delta u+nabla p=0,
div u=0,
omega=curl u.
```

Le théorème 7.4 de la prépublication part de `u_0∈L∞(R³)` et d'une solution
unique spatialement analytique avant un premier temps singulier possible
`T*`. Il ajoute, sur `(T*−epsilon,T*)`, une borne uniforme
`omega∈L^{3/2,infinity}` et des hypothèses de profil critique et de direction
de vorticité. Le présent cycle suppose la queue (40) et n'audite pas encore sa
dérivation dynamique par De Giorgi.

Le lemme actif est fonctionnel. Il ne construit ni solution faible, ni
solution de Leray–Hopf, ni singularité, et ne conclut aucune régularité.

## Veille différentielle et passage primaire

La notice arXiv contrôlée le 2026-08-14 contient toujours seulement la v1 du
9 juillet et la v2 du 13 juillet 2026. Aucune v3 ni publication évaluée n'est
indiquée.

La v2 affiche successivement :

```text
mu_omega(lambda,t)
  <=C_omega/[lambda^(3/2)(log lambda)^(3/2)],             (40)

u*(v,t)<=C[v^(-2/3) integral_0^v omega*(s,t) ds
             +integral_v^infinity s^(-2/3)omega*(s,t)ds], (41)

u*(v,t)<=C v^(-1/3)log^(-1)(e/v).                        (47)
```

Entre (41) et (47), le coeur est traité en (42)–(43), la queue est coupée en
`1` en (44)–(45), puis une intégration par parties produit en (46) un reste
positif présenté comme absorbé dans un `O(1)`. Les volumes `1`, les niveaux
et les logarithmes sont écrits dans des unités implicitement normalisées.

## Hypothèses quantitatives normalisées

Fixons uniformément dans le temps :

- une amplitude de vorticité `Omega>0`;
- un volume de référence `V>0`;
- un contrôle critique global
  `M=sup_(s>0) s^(2/3)omega*(s,t)<infinity`;
- une constante d'O'Neil–Biot–Savart `C_K`;
- une composante harmonique bornée `h`, avec `||h||_infinity<=H`.

La version dimensionnelle de la queue (40) utilisée ici est

```text
mu_omega(lambda,t)
 <=V[(Omega/lambda)/log(lambda/Omega)]^(3/2),
lambda>=e Omega.                                         (H40)
```

La représentation globale est

```text
u=B[omega]+h,                                             (BS)
```

où `B` est le potentiel de Biot–Savart. L'inégalité d'O'Neil est supposée
sous la forme sûre

```text
B[omega]*(v)
 <=C_K[v^(-2/3) integral_0^v omega*(s)ds
       +integral_v^infinity s^(-2/3)omega*(s)ds].         (ON)
```

Pour `h=0`, c'est (41) à constante dimensionnelle près. Une donnée
`u∈L²(R³)`, une décroissance à l'infini ou une normalisation de Hodge impose
`h=0`. Sous la seule hypothèse `u∈L∞`, la composante harmonique peut être une
constante spatiale non nulle et doit être conservée.

## Lemme 1 — inversion quantitative de (40)

Posons

```text
R=log(V/s),
q=(V/s)^(2/3).
```

Pour `0<s<=V exp(-3)`, donc `R>=3`, définissons

```text
lambda_s=3 Omega q/R.
```

Alors `lambda_s>=e Omega` et

```text
omega*(s,t)<=lambda_s
             <=4 Omega(V/s)^(2/3)/log(eV/s).             (R40)
```

### Preuve

Écrivons `y=lambda_s/Omega=3exp(2R/3)/R`. Cette fonction est croissante pour
`R>=3` et vaut `exp(2)` à `R=3`; (H40) est donc applicable. De plus,

```text
log y-R/3=log[3exp(R/3)/R]>=0,
```

car `exp(R/3)>=1+R/3`. Ainsi `y log y>=q`, puis

```text
mu_omega(lambda_s)
 <=V[y log y]^(-3/2)
 <=V q^(-3/2)=s.
```

La propriété de pseudo-inverse donne `omega*(s)<=lambda_s`. Enfin,
`R>=3` implique `3/R<=4/(1+R)`, ce qui donne (R40). Aucun équivalent, aucune
fonction de Lambert et aucune hypothèse de stricte décroissance ne sont
nécessaires.

Notons

```text
C_0=4 Omega V^(2/3),
L(v)=log(eV/v).
```

Alors (R40) s'écrit `omega*(s)<=C_0 s^(-2/3)/L(s)`.

## Lemme 2 — les deux intégrales d'O'Neil

Pour `0<v<=V exp(-6)`, on a

```text
v^(-2/3) integral_0^v omega*(s)ds
 <=3C_0 v^(-1/3)/L(v),                                  (C)
```

car `L(s)>=L(v)` pour `s<=v` et
`integral_0^v s^(-2/3)ds=3v^(1/3)`.

Pour la queue intermédiaire, posons `v=Vexp(-T)`, `T>=6`. Le changement de
variable `s=Vexp(-t)` ramène l'intégrale logarithmique à

```text
V^(-1/3) integral_0^T exp(t/3)/(1+t)dt.
```

La fonction

```text
G(T)=20exp(T/3)/(1+T)
```

est un supersolution exact pour `T>=3` : après retrait du facteur positif,
`G'(T)-exp(T/3)/(1+T)` a pour numérateur `17T-43>=8`. Au point `T=3`,

```text
integral_0^3 exp(t/3)/(1+t)dt
 <=3(e-1)<5e=G(3).
```

On obtient donc

```text
integral_v^(Vexp(-3)) s^(-2/3)omega*(s)ds
 <=20C_0 v^(-1/3)/L(v).                                 (I)
```

Enfin, le contrôle global critique donne

```text
integral_(Vexp(-3))^infinity s^(-2/3)omega*(s)ds
 <=3e M V^(-1/3)
 <=9M V^(-1/3).                                          (F)
```

Pour `T>=6`, `exp(T/3)/(1+T)>=exp(2)/7>1`; le terme (F) s'absorbe donc dans
`9M v^(-1/3)/L(v)`.

## Lemme minimal réparé `(40) -> (47)`

Sous (H40), le contrôle global `M`, (BS) et (ON), pour tout
`0<v<=Vexp(-6)`, uniformément en temps,

```text
u*(v,t)<=Q v^(-1/3)/L(v),                                (47q)

Q=C_K(23C_0+9M)+H V^(1/3).                              (Q)
```

Les nombres `23=3+20` proviennent du coeur et de la queue intermédiaire. La
majoration `u*(v)<=B[omega]*(v)+H` traite la composante harmonique; le facteur
`H V^(1/3)` est absorbable parce que
`v^(-1/3)/L(v)>=V^(-1/3)` sur le domaine retenu.

Ce lemme ferme le contenu fonctionnel de `(40) -> (47)` après ajout des
prémisses effectivement nécessaires. Il ne prouve pas que la prépublication
établit (H40) avec les mêmes références et seuils.

## Résultat négatif — le reste de (46) n'est pas `O(1)`

L'intégration par parties exacte de la queue locale contient

```text
R(v)=3 integral_v^1 s^(-4/3)/log^2(e/s) ds.
```

Avec `v=exp(-T)`, cela devient

```text
R(T)=3 integral_0^T exp(t/3)/(1+t)^2 dt.
```

Pour `T=3n`, `n>=2`, l'intégration seulement sur `[T-3,T]`, l'inégalité
`exp(n-1)>=(n-1)^3/6` et les bornes polynomiales élémentaires donnent

```text
R(exp(-3n))>=3n/256 -> infinity.                         (A46)
```

L'étiquette additive `O(1)` autour de (46) est donc réfutée. Le vrai
comportement est

```text
R(v)~9v^(-1/3)/log^2(e/v),
```

qui diverge mais reste inférieur d'un logarithme au terme principal. La borne
directe par supersolution utilisée dans (I) l'absorbe avec une constante
uniforme; l'exposant de (47) survit.

## Tests adverses

### Composante harmonique

Le champ constant

```text
u=(2,-3,6),  |u|=7,
```

est analytique, divergence-free et de vorticité nulle. Sur `R³`, sa
réarrangée vaut `7` à tout volume fini, tandis que le membre droit littéral de
(41) vaut zéro. Ainsi `u=B[omega]` est faux sous la seule hypothèse `L∞`.
Ce test ne réfute pas Navier–Stokes ni le théorème de régularité : il réfute
uniquement la normalisation omise dans ce maillon de preuve.

### Seuil de grande amplitude non uniforme

Une fonction de hauteur `n` sur une masse un satisfait trivialement toute
queue au-dessus du seuil dépendant de l'indice `2n`, mais sa réarrangée à
volume `1/2` vaut `n`. Une formule « pour lambda assez grand » n'est donc
uniforme en temps que si son seuil l'est.

### Queue globale absente

Pour `f_R*=1` sur `(0,R³)` et zéro ensuite, une même enveloppe peut être
imposée sur `0<s<=exp(-6)`, mais

```text
integral_1^(R³) s^(-2/3)f_R*(s)ds=3(R-1).
```

La petite queue logarithmique seule ne contrôle pas le second opérateur
d'O'Neil. Le contrôle global `M` ou une hypothèse de queue équivalente est
indispensable.

## Loi d'échelle

Sous

```text
u_kappa(x,t)=kappa u(kappa x,kappa^2t),
omega_kappa(x,t)=kappa^2 omega(kappa x,kappa^2t),
```

on a

```text
mu_(omega_kappa)(lambda)=kappa^(-3)mu_omega(lambda/kappa^2),
V -> kappa^(-3)V,
Omega -> kappa^2 Omega,
C_0=4Omega V^(2/3) -> C_0,
M -> M,
H V^(1/3) -> H V^(1/3).
```

La constante `Q` est invariante, `v^(-1/3)` porte `kappa` et (47q) suit
exactement le scaling de la vitesse. Aucune puissance d'échelle n'est perdue.

## Certificat reproductible

Commande :

```text
python -B experiments/navier-stokes/oneil-transfer/oneil_transfer_audit.py
```

Le script standard-library utilise uniquement `Fraction` et des séries
finies exactes. Il vérifie :

- les marges de l'inversion normalisée de (40);
- le supersolution de queue et sa marge minimale `8`;
- `exp(2)>7` par somme partielle rationnelle;
- l'absence de résidu de divergence et de rotationnel du champ constant;
- la divergence du reste de (46) sur une suite explicite;
- les deux familles adverses de seuil et de queue globale.

Empreinte SHA-256 :
`cab6da2b536cfd5a72fd669887fe7dc444a283eba081bbfb9b02b9889897c06f`.

Aucun maillage, pas de temps, flottant, graine aléatoire ou extrapolation de
calcul fini vers une solution PDE n'intervient.

## Passes contradictoires séparées

Trois passes séparées, de même famille de modèle et donc non indépendantes au
sens scientifique externe, convergent sur le verdict fonctionnel :

- la passe d'analyse reconstruit le transfert avec un seuil plus conservateur,
  suit le facteur `3` de `K**` dans O'Neil et prouve que le reste de (46) est
  inférieur d'un logarithme mais non borné;
- la passe bibliographique confirme la v2 courante, la source primaire
  d'O'Neil et l'absence, dans le théorème 7.4, d'une condition éliminant le
  mode harmonique sous la seule hypothèse `u_0∈L∞`;
- la passe contre-modèle ajoute une famille galiléenne, des plateaux à seuils
  non uniformes et une masse basse fréquence. Elle confirme que la constante
  finale dépend nécessairement du contrôle global, pas seulement de la queue
  logarithmique à grande amplitude.

Les formulations quantitatives diffèrent dans leurs constantes de sécurité,
mais toutes conservent les exposants `2/3`, `1/3` et un seul logarithme. Aucun
rapport ne valide la production dynamique de (40).

## Décision

Le passage fonctionnel `(40) -> (47)` est **valide après révision** sous quatre
prémisses explicites : queue (40) dimensionnée avec seuil uniforme, contrôle
global faible `L^{3/2}`, inégalité d'O'Neil et composante harmonique fixée ou
bornée. La v2 ne fournit pas cette formulation complète.

Deux assertions littérales sont réfutées : le reste positif de (46) n'est pas
`O(1)`, et (41) appliquée à la vitesse entière est fausse sans normalisation
de Biot–Savart. Les deux défauts sont localement réparables et ne réfutent pas
l'exposant logarithmique de (47).

Le prochain verrou remonte à la dérivation dynamique de (40) : suivre le
premier seuil de troncature, le coefficient de Grönwall, la constante de
Poincaré sur le superniveau et l'uniformité de l'itération De Giorgi.
