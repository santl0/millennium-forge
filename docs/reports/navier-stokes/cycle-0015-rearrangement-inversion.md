# Cycle 0015 — inversion quantitative réarrangée vers distribution

Date : 2026-08-14. Lemme actif : `REARRANGEMENT-INVERSION-1`.

## Décision adaptative

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total | Décision |
|---|---:|---:|---:|---:|---:|---|
| rendre exacte l'implication (47) → (49), plateaux inclus | 3 | 5 | 5 | 5 | **18/20** | sélectionnée |
| auditer les intégrales d'O'Neil (41) → (47) | 4 | 4 | 5 | 5 | **18/20** | cycle suivant possible |
| auditer la queue dyadique du commutateur, théorème 4.1 | 5 | 2 | 4 | 5 | 16/20 | différée |

Le premier candidat gagne le départage parce qu'il isole l'usage exact de la
réarrangée décroissante, indépendamment de la validité de l'estimation PDE qui
produit l'enveloppe (47).

## Équation et portée

La prépublication ciblée étudie Navier–Stokes incompressible 3D non forcé sur
`R³`, viscosité `nu>0`, donnée `u_0∈L∞(R³)` et solution mild analytique avant un
premier temps singulier possible `T*` :

```text
partial_t u+(u·nabla)u-nu Delta u+nabla p=0,
div u=0.
```

Le présent lemme est un résultat de théorie de la mesure. Il suppose
conditionnellement l'enveloppe (47) et teste seulement son inversion en (49).
Il ne valide ni O'Neil (41) dans cette application, ni le gain sur la
vorticité, ni le commutateur, ni le théorème 7.4.

## Passage primaire audité

La v2, toujours datée du 13 juillet 2026, affirme pour les petits volumes `v`
et uniformément en temps :

```text
u*(v,t) <= C v^(-1/3) log^(-1)(e/v).                     (47)
```

Elle pose ensuite

```text
lambda approx C v^(-1/3) log^(-1)(e/v),                 (48)
```

avec `v=|{|u|>lambda}|`, puis conclut

```text
|{|u|>lambda}| <= C_u/[lambda^3(log lambda)^3].          (49)
```

La formule (47) est une inégalité, tandis que (48) est présentée comme une
équivalence asymptotique. La question est de savoir si (49) suit avec des
quantificateurs et constantes exacts, y compris lorsque `u` a des plateaux.

## Définitions exactes

Sur un espace mesuré, pour une fonction mesurable `f`, posons

```text
d_f(lambda)=mu({|f|>lambda}),
f*(v)=inf{a>=0 : d_f(a)<=v}.
```

Avec cette convention stricte sur le superniveau, on a l'équivalence de
quantile

```text
d_f(lambda)<=v  <=>  f*(v)<=lambda.                      (Q)
```

En revanche, l'égalité `lambda=f*(d_f(lambda))` est fausse en présence de
plateaux. Le lemme ne doit pas l'utiliser.

Le logarithme doit être sans dimension. Fixons un volume de référence
`V_*>0` et écrivons

```text
L(v)=log(e V_*/v).
```

Soient `0<v_0<=V_*` et `A>0`, uniformes dans le paramètre temporel éventuel.
L'hypothèse exacte est

```text
f*(v)<=A v^(-1/3)L(v)^(-1),    0<v<=v_0.                (H)
```

La quantité d'amplitude naturelle associée au volume de référence est

```text
Lambda_*=A V_*^(-1/3).
```

## Lemme quantitatif réparé

Définissons le seuil d'entrée dans le domaine où (H) est connu :

```text
Lambda_0=A v_0^(-1/3)L(v_0)^(-1).
```

Pour tout

```text
lambda>=max(Lambda_0,Lambda_*),
```

le superniveau a une mesure finie `m=d_f(lambda)<=v_0` et

```text
m <= A^3 /
     {lambda^3[1+3log(lambda/Lambda_*)]^3}.              (I)
```

En particulier, pour `lambda>Lambda_*`,

```text
m <= A^3 /
     {27 lambda^3 log^3(lambda/Lambda_*)}.               (I')
```

Une forme régularisée, proche de (49) et valable sur le même domaine
`lambda>=max(Lambda_0,Lambda_*)`, est

```text
m <= log^3(e+1) A^3 /
     {lambda^3 log^3(e+lambda/Lambda_*)}.                (I'')
```

Elle suit de
`log(e+x)<=log(e+1)[1+3log x]` pour `x>=1`. Dans la
paramétrisation `f*(v)<=A_0(V_*/v)^(1/3)/L(v)`, on a
`A=A_0 V_*^(1/3)` et `Lambda_*=A_0`; la conclusion devient
`V_* A_0^3` fois le facteur de queue sans dimension.

La constante et le seuil sont uniformes en temps exactement lorsque
`A,v_0,V_*` le sont.

## Preuve sans égalité de quantile

Le seuil `lambda>=Lambda_0` et (Q) donnent `m<=v_0`. Si `m=0`, le résultat est
immédiat. Sinon, pour tout `0<v<m`,

```text
d_f(lambda)>v,
```

donc (Q) donne `f*(v)>lambda`. Avec (H),

```text
lambda < A v^(-1/3)L(v)^(-1).
```

En faisant croître `v` vers `m` et par continuité de l'enveloppe,

```text
lambda <= A m^(-1/3)L(m)^(-1),
m <= (A/lambda)^3 L(m)^(-3).                            (1)
```

Comme `m<=V_*`, `L(m)>=1`; (1) fournit d'abord

```text
m <= (A/lambda)^3.                                      (2)
```

Cette borne grossière est réinjectée dans le logarithme :

```text
L(m)=log(eV_*/m)
    >=log(eV_* lambda^3/A^3)
     =1+3log(lambda/Lambda_*).                          (3)
```

Les équations (1) et (3) donnent (I). Enfin,
`1+3log x>=3log x` pour `x>1`, ce qui donne (I'). Il ne faut
ni équivalence asymptotique, ni hypothèse de variation lente, ni inversion
explicite d'une fonction transcendante.

## Test adverse de plateau

Considérons une fonction simple sur un espace de mesure un :

```text
|f|=4 sur une masse 1/8,
|f|=2 sur une masse 3/8,
|f|=0 sur la masse restante 1/2.
```

Au niveau `lambda=3`,

```text
d_f(3)=1/8,
f*(1/8)=2 != 3,
f*(1/16)=4>3.
```

Ce profil réfute l'égalité littérale de (48), mais confirme exactement le
quantificateur utilisé dans la preuve : pour tout `v<d_f(lambda)`, on a
`f*(v)>lambda`. Ainsi le défaut de rédaction est réel et localement réparable;
il ne réfute pas (49).

Une seconde famille adverse montre que « pour `v` assez petit » doit être
uniforme en temps. Si des réarrangées coïncident avec l'enveloppe seulement sur
`(0,v_n]`, avec `v_n->0`, puis gardent un plateau jusqu'à une masse fixe, leurs
seuils de plateau tendent vers l'infini mais leurs superniveaux gardent une
masse d'ordre un. Une constante uniforme accompagnée de cutoffs `v_n`
dégénérés ne fournit donc aucun niveau d'entrée commun dans (49).

## Loi d'échelle

Sous l'échelle Navier–Stokes

```text
u_kappa(x,t)=kappa u(kappa x,kappa^2t),
```

les objets se transforment par

```text
d_(u_kappa)(lambda)=kappa^-3 d_u(lambda/kappa),
u_kappa*(v)=kappa u*(kappa^3 v),
V_* -> kappa^-3 V_*,
A -> A,
Lambda_* -> kappa Lambda_*.
```

Le rapport `lambda/Lambda_*` est invariant et le membre droit de (I) porte le
facteur `kappa^-3`. Le lemme réparé est donc exactement compatible avec le
scaling critique; le logarithme non normalisé `log lambda` ne l'est pas.

## Certificat reproductible

Commande :

```text
python -B experiments/navier-stokes/rearrangement-inversion/rearrangement_inversion_audit.py
```

Le script standard-library utilise seulement `fractions.Fraction`. Il vérifie :

- l'équivalence (Q) sur une grille complète de seuils et volumes du profil en
  plateaux;
- le contre-exemple exact à `lambda=f*(d_f(lambda))`;
- toutes les puissances et constantes de (1)–(3);
- des encadrements rationnels stricts de `log 2`, puis des bornes pour les
  rapports `lambda/Lambda_*=2,4,8,16`;
- la covariance d'échelle pour `kappa=3` avec résidu rationnel nul.

Les logarithmes sont encadrés par la série exacte

```text
log x=2 sum_(k>=0) z^(2k+1)/(2k+1),  z=(x-1)/(x+1),
```

et un reste géométrique rationnel. Aucun flottant n'est utilisé.

Empreinte SHA-256 du script exécuté :
`0b306177085e584f1a658b4b9534ea74d7ca0ce07c599c7bf9295a95fdc804f7`.

L'enveloppe saturante

```text
g*(v)=A v^(-1/3)/log(eV_*/v)
```

est réalisable comme réarrangée sur un espace non atomique dans le régime où
elle décroît. Son inverse satisfait asymptotiquement

```text
d_g(lambda) ~ A^3/
  [27 lambda^3 log^3(lambda/Lambda_*)].
```

La puissance `3` et le facteur principal `1/27` sont donc optimaux à l'ordre
dominant sous la seule hypothèse (H).

## Passe contradictoire pilote

Les attaques suivantes sont conservées :

1. ne jamais identifier un niveau arbitraire au quantile terminal d'un
   plateau;
2. fixer la convention `>` ou `>=` des superniveaux avant d'utiliser (Q);
3. conserver le seuil `v<=v_0` où (47) est effectivement disponible;
4. exiger l'uniformité temporelle de `A,v_0,V_*`, pas seulement une constante
   finie à chaque temps;
5. normaliser le logarithme par un volume et l'amplitude par `Lambda_*`;
6. ne pas promouvoir une borne sur `u*` en profil spatial radial
   `|u(x)|≈|x|^-1|log|x||^-1` sans hypothèse de symétrie ou de saturation;
7. séparer l'inversion valide de l'obtention encore non auditée de (47).

## Revues contradictoires séparées

Trois passes Codex séparées, de même famille de modèle et donc non
indépendantes au sens externe, convergent :

- la passe formelle prouve (I), (I'') et le scaling en traitant la continuité
  à droite de la fonction de distribution, les plateaux et le cutoff uniforme;
- la passe bibliographique confirme qu'O'Neil 1963 fournit la structure de
  convolution de (41), mais relève qu'une composante harmonique de la vitesse
  doit être exclue et que le reste positif de (46) exige encore une borne
  uniforme;
- la passe contre-modèle réfute l'égalité de (48) avec deux plateaux de
  hauteurs `5,2` et masses `3,4`, confirme le crochet de pseudo-inverses et
  construit une famille réfutant tout cutoff small-volume dépendant du temps.

Les trois passes confirment aussi l'optimalité asymptotique du facteur
`A^3/27`. Leur accord justifie `adversarial_pass`, pas une revue indépendante
externe.

## Décision

Le passage `(47) -> (49)` est **valide après révision** : l'égalité de (48)
doit être remplacée par le lemme de quantile ci-dessus, avec seuils et
normalisations explicites. La conclusion porte uniquement sur la fonction de
distribution et ne justifie pas le profil physique ponctuel affirmé ensuite.

Le prochain verrou est l'arête `(40) -> (41) -> (47)` : vérifier
quantitativement l'inversion de la
distribution de vorticité, l'inégalité d'O'Neil et les deux intégrales
logarithmiques, avant de remonter à la queue du commutateur.
