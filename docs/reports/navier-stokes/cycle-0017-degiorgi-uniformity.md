# Cycle 0017 — énergie tronquée et uniformité de Grönwall

Date : 2026-08-14. Lemme actif : `DEGIORGI-UNIFORMITY-1`.

## Décision adaptative

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total | Décision |
|---|---:|---:|---:|---:|---:|---|
| auditer exactement `(23) -> (40)`, absorption, Poincaré et Grönwall | 3 | 5 | 5 | 5 | **18/20** | sélectionnée |
| auditer la queue dyadique du commutateur `(8) -> (22)` | 5 | 2 | 4 | 5 | 16/20 | prochaine |
| synchroniser toutes les constantes de l'endgame `(49) -> (58)` | 4 | 3 | 5 | 5 | 17/20 | différée |

Le premier candidat est le premier raccord PDE non reproduit en amont des
cycles 0014–0016. Il est assez borné pour distinguer une perte réelle d'une
constante seulement omise.

## Équation, domaine et type de solution

La source ciblée considère Navier–Stokes incompressible 3D non forcé sur
`R³`, sans frontière, avec viscosité `nu>0` :

```text
partial_t u+(u dot nabla)u-nu Delta u+nabla p=0,
div u=0,
boldomega=curl u,
omega=|boldomega|.
```

Avant le premier temps singulier possible `T*`, la solution est supposée
classique et spatialement analytique. Sur
`I=(t_0,T*)=(T*−epsilon,T*)`, la prépublication ajoute

```text
M=sup_(t in I)||omega(t)||_(L^(3/2,infinity))<infinity
```

et des hypothèses de profil ponctuel critique et de direction de vorticité.
Le calcul ci-dessous porte sur une solution classique sur `I`; il ne construit
ni solution faible, ni solution de Leray–Hopf, ni solution convenable. Les
tests scalaires ne sont pas des solutions de Navier–Stokes.

Avec `xi=boldomega/omega` sur `{omega>0}`, `S` le tenseur de déformation et
`alpha=xi dot S xi`, l'inégalité de Kato issue de l'équation de vorticité est

```text
(partial_t+u dot nabla-nu Delta)omega <= alpha omega.    (K)
```

## Veille différentielle

La notice primaire d'`arXiv:2607.08866` contrôlée le 2026-08-14 indique
toujours la v2, soumise le 9 juillet et révisée le 13 juillet 2026. Aucune v3,
aucun erratum et aucune publication évaluée n'y sont signalés.

La section 5 de la v2 contient une estimation à **un niveau** : test par
`omega_lambda=(omega-lambda)_+`, interpolation de Lorentz, absorption,
inégalité de support, ODE linéaire et Chebyshev. Malgré le vocabulaire
« De Giorgi », aucune suite de niveaux et aucune récurrence d'itération
n'intervient dans les équations (23)–(40).

L'audit a aussi touché le raccord immédiatement antérieur (20)–(22). La
borne affichée `phi(2^jR)<=2phi(R)` est fausse au dernier indice : pour
`R=2^(-8)`, `N=4`, `j=N+1=5`, son ratio vaut exactement `8/3`. Une constante
trois à rayon assez petit conserve l'ordre final. Cette réparation locale ne
certifie ni les extensions BMO, ni les commutateurs, ni toute la queue
non locale du théorème 4.1.

## Hypothèses quantitatives réparées

Fixons la constante `C_H` de Hölder–Lorentz pour la convention de norme
choisie et deux constantes de Sobolev, afin de ne pas les identifier
silencieusement :

```text
||f||_(L^(6,2)) <= S_L ||nabla f||_2,
||f||_6         <= S_6 ||nabla f||_2.
```

Soit `C_I` la constante de l'interpolation réelle

```text
||f||_(L^(3,1))
 <=C_I ||f||_(L^(3/2,infinity))^(1/3)
         ||f||_(L^(6,2))^(2/3).                         (I)
```

Le logarithme doit porter sur un rapport sans dimension. On suppose qu'il
existe des constantes uniformes `A>0`, `Lambda_*>0` et `lambda_d>Lambda_*`
telles que, pour `t in I` et `lambda>=lambda_d`, en posant

```text
L_lambda=log(lambda/Lambda_*),
A_lambda(t)={x:omega(x,t)>lambda},
a_lambda(t)=||alpha(t)||_(L^(3/2,infinity)(A_lambda(t))),
```

on ait

```text
a_lambda(t) <= A/L_lambda.                              (D)
```

Dans l'application annoncée, (D) doit provenir du théorème 4.1 et de
`A_lambda(t) subset B_(C lambda^(-1/2))`. Avec une longueur de référence
`r_*`, le choix naturel est

```text
Lambda_*=C^2/r_*^2,
|log(C lambda^(-1/2)/r_*)|=(1/2)log(lambda/Lambda_*).
```

Cette normalisation restaure exactement l'invariance d'échelle omise par les
notations `log lambda` et `log R` de la source.

## Lemme 1 — absorption à seuil uniforme

Posons

```text
E_lambda=||omega_lambda||_2^2,
X_lambda=||nabla omega_lambda||_2^2.
```

Le test de (K) donne, pour presque tout `t in I`,

```text
(1/2)E_lambda'+nu X_lambda
 <= integral_(A_lambda) alpha omega_lambda^2
    +lambda integral_(A_lambda) alpha omega_lambda.     (23)
```

Hölder–Lorentz et Sobolev–Lorentz donnent

```text
integral alpha omega_lambda^2
 <=C_H a_lambda ||omega_lambda||_(L^(6,2))^2
 <=C_H a_lambda S_L^2 X_lambda.
```

Il suffit donc d'imposer

```text
L_lambda >= 2 C_H A S_L^2/nu.                          (A1)
```

Un seuil unique valable pour tout `t in I` est

```text
lambda_abs=Lambda_* exp(2 C_H A S_L^2/nu).
```

Il dépend de la viscosité et des constantes uniformes, mais ni de `t`, ni de
`T*−t`, ni d'une itération inexistante.

## Lemme 2 — source linéaire avec constante suivie

Le tronqué satisfait
`||omega_lambda||_(L^(3/2,infinity))<=M`. L'interpolation (I) donne

```text
lambda integral alpha omega_lambda
 <=B_lambda X_lambda^(1/3),
B_lambda=lambda (A/L_lambda) C_H C_I M^(1/3) S_L^(2/3).
```

L'inégalité de Young sûre

```text
B X^(1/3) <= epsilon X+B^(3/2)/sqrt(epsilon)
```

se réduit, après homogénéisation, à `z<=z^3+1`. Avec
`epsilon=nu/4`, on obtient

```text
(1/2)E_lambda'+(nu/4)X_lambda
 <=2 (C_H C_I)^(3/2) S_L A^(3/2) M^(1/2) nu^(-1/2)
      lambda^(3/2)L_lambda^(-3/2).                      (E1)
```

La constante n'est pas optimale, mais elle est explicite et uniforme.

## Lemme 3 — Poincaré de support et coefficient de Grönwall

La définition de la norme faible et Hölder sur le support donnent

```text
U_lambda=|A_lambda|<=M^(3/2)lambda^(-3/2),
E_lambda<=S_6^2 X_lambda U_lambda^(2/3)
          <=S_6^2 M lambda^(-1)X_lambda.
```

Ainsi

```text
X_lambda >=lambda E_lambda/(S_6^2 M).                  (P)
```

Cette constante ne dépend pas de la géométrie du superniveau. Elle dépend
nécessairement du contrôle **uniforme** `M`; elle n'est pas disponible depuis
une borne faible seulement ponctuelle en temps.

En multipliant (E1) par deux et en injectant (P), on trouve

```text
E_lambda'+mu lambda E_lambda <=K(lambda),
mu=nu/(2S_6^2 M),
K(lambda)=4 (C_H C_I)^(3/2) S_L A^(3/2) M^(1/2)nu^(-1/2)
              lambda^(3/2)L_lambda^(-3/2).             (ODE)
```

Le premier coefficient de Grönwall est donc positif, critique et uniforme.

## Lemme minimal `(22) -> (40)` réparé

À l'ancre `t_0=T*−epsilon`, la régularité classique donne
`Lambda_0=||omega(t_0)||_infinity<infinity`. Pour

```text
lambda >= lambda_dagger
 =max(lambda_d,Lambda_0,lambda_abs),                    (T)
```

on a `E_lambda(t_0)=0`. La résolution de (ODE) donne

```text
E_lambda(t)
 <=K(lambda)/(mu lambda)
 <=C_E lambda^(1/2)L_lambda^(-3/2),                    (E2)

C_E=8 (C_H C_I)^(3/2) S_L S_6^2 A^(3/2)M^(3/2)nu^(-3/2).
```

La dépendance totale en `M` n'est `M^(3/2)` que si `A` est tenu séparément.
Dans l'application du théorème 4.1, `A` dépend lui-même des normes uniformes
de vorticité et de direction; cette dépendance doit rester visible avant toute
comparaison quantitative avec l'analyticité.

Sur `A_(2lambda)`, `omega_lambda>lambda`; par conséquent

```text
U_(2lambda)(t)
 <=E_lambda(t)/lambda^2
 <=C_E lambda^(-3/2)L_lambda^(-3/2).                   (D40)
```

Cette implication ferme conditionnellement les équations (23)–(40), avec
constante et seuil indépendants du temps sur `I`. Elle utilise (D) comme
prémisse : elle ne prouve pas le commutateur (8)/(22).

Le changement de notation final `2lambda -> Lambda` n'est pas gratuit. Pour
`Lambda>=4Lambda_*`, on a
`log(Lambda/(2Lambda_*)) >= (1/2)log(Lambda/Lambda_*)`; une écriture au niveau
`Lambda` peut donc conserver l'exposant avec un facteur de sécurité huit et
un seuil final au moins `max(2lambda_dagger,4Lambda_*)`.

## Loi d'échelle

Sous

```text
u_kappa(x,t)=kappa u(kappa x,kappa^2t),
omega_kappa=kappa^2 omega(kappa x,kappa^2t),
alpha_kappa=kappa^2 alpha(kappa x,kappa^2t),
```

on a

```text
lambda,Lambda_*,lambda_dagger -> kappa^2 fois leur valeur,
M,A,nu,L_lambda               -> invariants,
E_lambda                      -> kappa E_lambda,
X_lambda et E_lambda'         -> kappa^3 fois leur valeur,
U_lambda                      -> kappa^(-3)U_lambda.
```

Chaque terme de (E1) et (ODE) porte `kappa^3`; (D40) porte
`kappa^(-3)`. Écrire `log lambda` sans `Lambda_*` détruirait cette covariance.

## Tests adverses

### Inversion de quantificateur sur le seuil

La famille abstraite

```text
a_n(lambda)=1 si lambda<n, 0 sinon
```

possède, pour chaque indice `n`, un seuil d'absorption fini. Aucun seuil
commun n'existe : au candidat `Lambda`, choisir `n=Lambda+1` laisse
`a_n(Lambda)=1`. Ce n'est pas un champ Navier–Stokes et cela ne réfute pas
le théorème 4.1, qui **affirme** l'uniformité. Il certifie que cette uniformité
est une prémisse logique indispensable, non une conséquence de la seule
convergence ponctuelle `a_lambda(t)->0`.

### La norme faible ne lance pas l'énergie tronquée

Le profil scalaire

```text
f(x)=|x|^(-2) 1_(0<|x|<1)
```

appartient exactement à `L^(3/2,infinity)`, car
`|{f>a}|=(4pi/3)a^(-3/2)` pour `a>=1`. Pourtant, pour tout niveau fini,

```text
||(f-lambda)_+||_2^2
 =4pi integral_0^(lambda^(-1/2))(r^(-2)-lambda)^2r^2dr
 =infinity.
```

Une variante tangentielle divergence-free
`(a cross x)/|x|^3`, coupée radialement, conserve cette divergence sur un
cône. Ce contre-profil n'est pas une solution NS et ne réfute pas le lemme
classique : il montre que la régularité/analyticité pré-singulière, et non la
seule borne faible critique, justifie la finitude de `E_lambda` et
`X_lambda`. Cette dépendance est explicite dans le claim.

### Intervalle extrapolé

Le théorème 4.1 et ses hypothèses portent sur `I=(T*−epsilon,T*)`, alors que
le texte après (25) affirme l'absorption sur tout `(0,T*)`. Une fonction
`a_lambda(t)` égale à l'enveloppe (D) sur `I`, mais égale à un au temps
antérieur, satisfait toutes les prémisses proches de `T*` et viole
l'absorption antérieure si `S_L^2>nu/2`. L'implication vers tout `(0,T*)` est
donc réfutée. Elle est inutile : l'intégration (36) commence bien à `t_0`.

### Dépendance de la constante faible

Si l'on remplace `M` par une famille `M_n->infinity`, alors
`mu_n=nu/(2S_6^2M_n)->0`. Le facteur `1/(mu_n lambda)` de l'ODE diverge.
La Poincaré de support ne crée aucune uniformité absente de l'hypothèse faible
`L^(3/2,infinity)`.

## Certificat reproductible

Commande :

```text
python -B experiments/navier-stokes/degiorgi-uniformity/degiorgi_uniformity_audit.py
```

Le script standard-library vérifie par `Fraction` et registres d'exposants :

- l'exposant d'interpolation `theta=2/3`;
- une marge d'absorption rationnelle `1/5` dans un cas normalisé;
- l'inégalité de Young sous la forme exacte `z<=z^3+1`;
- les poids d'échelle `3` de l'énergie et `−3` de la distribution;
- un modèle d'égalité de l'ODE avec deux résidus exactement nuls;
- Chebyshev sur des atomes rationnels, marge `28/15`;
- la famille adverse de seuils sur 64 niveaux, accompagnée de sa preuve pour
  tout niveau fini;
- les exposants finaux `lambda^(−3/2)L^(−3/2)`;
- la divergence des énergies tronquées du profil critique à cutoffs exacts;
- l'échelle optimale de Poincaré sur une tente radiale et le terme initial de
  l'ODE;
- le contre-test dyadique exact `8/3>2` au bord de (20)–(21).

Empreinte SHA-256 :
`cbdca92eec11a287c31bb67d48dfeda339768863b2ccfa58b6cd8f66e3682721`.

Il n'y a ni maillage, ni pas de temps, ni flottant, ni graine, ni passage
d'un calcul fini au continuum. Le certificat ne prouve aucune estimation de
commutateur, inégalité de Sobolev ou solution PDE.

## Passes contradictoires séparées

Trois passes Codex séparées sont conservées dans `reviews/`. Elles restent de
la même famille de modèle et ne constituent pas une revue externe
indépendante. La synthèse finale doit distinguer leurs objections contre
l'énergie tronquée de celles qui attaquent en réalité le théorème 4.1.

## Décision

La chaîne conditionnelle `(22)+(23) -> (40)` est **valide après révision** :
elle demande un logarithme dimensionné, un seuil
`lambda_dagger` explicite, deux constantes de Sobolev distinguées et le bon
intervalle `I`. Le coefficient de Grönwall et la Poincaré de support ne
présentent aucune dépendance cachée en `T*−t` ou en itération.

L'affirmation littérale d'une absorption sur tout `(0,T*)` depuis des
hypothèses seulement proches de `T*` est réfutée, mais non utilisée. Le verrou
`GAP-DEGIORGI-UNIFORMITY` est donc fermé **conditionnellement à (22)**. Le
premier maillon non reproduit devient `GAP-COMMUTATOR-UNIFORMITY` : vérifier
la queue dyadique, l'extension BMO et la borne faible de type `(8)/(22)` avec
une constante et un petit rayon réellement uniformes.
