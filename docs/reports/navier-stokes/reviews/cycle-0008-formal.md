# Cycle 0008 — revue PDE du lemme de trace ancienne

Date de coupure : **2026-08-14**. Cette passe est séparée de la dérivation
initiale, mais elle n'est pas une revue externe par un autre modèle.

## Verdict

Le lemme suivant est **démontré**, sous la définition `mild` précise donnée
ci-dessous :

> Soit `u` une solution ancienne mild de Navier–Stokes incompressible 3D sur
> `R^3 x (-infinity,0)`, de viscosité `nu=1`, telle que
> `M=sup_(x,t)|u(x,t)|<infinity`. Si `u(t)->0` dans
> `D'(R^3)` lorsque `t->0-`, alors `u` est identiquement nulle.

Le même résultat vaut pour toute viscosité constante `nu>0` après changement
d'échelle parabolique. Il n'exige ni énergie globale finie, ni décroissance
spatiale, ni valeur de pression. Il exige en revanche réellement la mildness,
la bornitude uniforme jusqu'au bord terminal et une **limite** en `D'`, et non
une valeur arbitrairement assignée à `t=0`.

La preuve utilise la régularité des solutions mild bornées de
[Koch–Nadirashvili–Seregin–Sverak (KNSS)](https://www-users.cse.umn.edu/~sverak/publications/liouville.pdf)
et le théorème d'unicité rétrograde d'
[Escauriaza–Seregin–Sverak (ESS)](https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&option_lang=rus&paperid=609&what=fullteng).

## Convention mild exacte

On emploie la définition de KNSS. Il existe une suite `T_j->-infinity` telle
que `u(T_j)` soit définie et que, pour tout `T_j<t<0`,

```text
u(t)=exp((t-T_j)Delta)u(T_j)
     -integral_(T_j)^t exp((t-s)Delta) P div(u tensor u)(s) ds.
```

La convolution est celle du noyau d'Oseen ; elle est bien définie pour
`u tensor u in L^infinity`. Par la propriété de semi-groupe, cette formule se
redémarre à tout temps `s<t<0` :

```text
u(t)=exp((t-s)Delta)u(s)
     -integral_s^t exp((t-r)Delta) P div(u tensor u)(r) dr.       (1)
```

Cette exigence exclut les solutions parasites `u=b(t)`,
`p=-b'(t) dot x`, qui satisfont l'équation avec pression mais pas (1) lorsque
`b` varie.

## Étape 1 — dérivées uniformes jusqu'à `t=0`

Le bord `t=0` n'est pas un bord initial pour l'évolution. Pour obtenir des
constantes uniformes, on redémarre plutôt (1) un temps parabolique fixe avant
chaque instant observé.

Supposons `M>0`, le cas `M=0` étant immédiat. La Proposition 4.1 de KNSS donne,
pour une solution mild issue d'une donnée `L^infinity`,

```text
h^(k/2+l) ||nabla^k partial_t^l u(s+h)||_infinity
  <= C_(k,l) ||u(s)||_infinity
```

tant que `0<h<=epsilon_(k,l)||u(s)||_infinity^-2`. Comme
`||u(s)||_infinity<=M`, on peut choisir
`h=epsilon_(k,l)/(2M^2)` indépendamment de `s`. En redémarrant à
`s=t-h`, on obtient, pour tous `t<0`,

```text
||nabla^k partial_t^l u(t)||_infinity
  <= C'_(k,l) M^(k+2l+1).                                      (2)
```

Les constantes numériques dépendent de la normalisation du noyau et ne sont
pas utilisées ensuite. Le point essentiel est leur indépendance de `t`, de la
suite définissant la solution ancienne et de la distance de `t` à zéro.

Cette étape serait fausse avec la seule hypothèse
`u in L^infinity(R^3 x (-infinity,-delta))` pour chaque `delta>0` : les
constantes pourraient alors exploser lorsque `delta->0`.

## Étape 2 — promotion de la trace distributionnelle

Fixons un compact spatial `K` et un entier `m`. Les bornes (2), jusqu'à l'ordre
`m+1`, rendent la famille des tranches `{u(t): -1<t<0}` précompacte dans
`C^m(K)` par Arzela–Ascoli.

Pour toute suite `t_n->0-`, toute sous-limite dans `C^m(K)` est aussi sa limite
dans `D'(K)`. L'hypothèse de trace impose que cette sous-limite soit zéro. Un
argument séquentiel par contradiction donne donc

```text
u(t) -> 0 dans C^m_loc(R^3), pour tout m, lorsque t->0-.          (3)
```

En particulier, pour `omega=curl u`,

```text
omega(t) -> 0 dans C^0_loc(R^3).                                (4)
```

Les bornes temporelles de (2) permettent de prolonger `u`, `omega` et les
dérivées nécessaires continûment jusqu'à `t=0`. Ainsi (4) est bien la condition
terminale ponctuelle requise par l'unicité rétrograde. Aucune permutation entre
une limite de solutions et la limite `t->0` n'intervient ici : il s'agit d'une
seule solution.

## Étape 3 — unicité rétrograde pour la vorticité

La vorticité lisse vérifie

```text
partial_t omega-Delta omega
  =(omega dot nabla)u-(u dot nabla)omega.
```

Les bornes (2) donnent donc, sur tout ruban fini `[-T,0)`,

```text
|partial_t omega-Delta omega|
  <= C_M (|omega|+|nabla omega|),                               (5)
```

où `C_M` ne dépend pas de `T`. Posons
`W(x,tau)=omega(x,-tau)` pour `0<tau<T`. Alors

```text
|partial_tau W+Delta W|<=C_M(|W|+|nabla W|),   W(x,0)=0.        (6)
```

Le Théorème 5.1 d'ESS s'applique à (6) sur un demi-espace et un ruban unitaire.
Ses hypothèses sont toutes vérifiées :

- `W`, `partial_tau W` et `nabla^2 W` sont localement de carré intégrable par
  (2) ;
- `W` est bornée, donc satisfait la croissance gaussienne admise par ESS
  (après division par une constante si nécessaire) ;
- (6) fournit l'inégalité différentielle avec coefficients bornés ;
- (4) fournit la donnée terminale nulle.

Une translation spatiale et une remise à l'échelle parabolique ramènent tout
demi-espace `{x_3>c}` et tout `T<infinity` au cadre d'ESS ; elles changent
`C_M` en une autre constante finie, ce que le théorème autorise. On obtient

```text
W=0 sur {x_3>c} x (0,T), pour tout c réel.
```

L'union de ces demi-espaces est `R^3`. Par conséquent,

```text
omega=0 sur R^3 x (-T,0).
```

Comme `T` est arbitraire, `omega` est nulle sur tout
`R^3 x (-infinity,0)`. **Aucun théorème de continuation unique spatiale
supplémentaire n'est requis** : il serait nécessaire dans ESS lorsque la
vorticité n'est connue nulle que dans une région extérieure, mais pas ici où
la trace terminale est globale.

## Étape 4 — classification du champ curl-free

Pour tout temps fixé,

```text
Delta u=nabla div u-curl curl u=0.
```

Chaque composante de `u(t)` est une fonction harmonique bornée sur tout
`R^3`; le théorème de Liouville harmonique donne donc

```text
u(x,t)=b(t).
```

Ce passage n'utilise aucune décroissance à l'infini. La bornitude globale
remplace ici l'intégrabilité qui servirait normalement à éliminer les champs
harmoniques.

## Étape 5 — la formule mild élimine `b(t)`

Dans (1), le semi-groupe de la chaleur conserve les constantes spatiales et
`div(b tensor b)=0`. Pour tous `s<t<0`, la formule devient donc

```text
b(t)=b(s).
```

C'est exactement la Remarque 6.1 de KNSS. Il existe ainsi un vecteur constant
`b_*` tel que `u(x,t)=b_*`. La convergence dans `D'` vers zéro force
`b_*=0` : il suffit de tester contre une fonction dont l'intégrale n'est pas
nulle. Le lemme est démontré.

## Passe contradictoire

### Affaiblissements réellement faux

1. **Sans mildness.** Pour toute fonction bornée lisse non constante `b(t)`
   tendant vers zéro en `t=0`, le couple
   `u=b(t)`, `p=-b'(t) dot x` est une solution classique ancienne, bornée et
   localement adaptée avec trace nulle. Il réfute la version faible/suitable.
2. **Sans véritable limite terminale.** Puisque le domaine temporel est ouvert,
   on peut prendre une solution mild constante non nulle sur `t<0` et lui
   assigner artificiellement la valeur zéro à `t=0`. La conclusion échoue si
   `u(0)=0` n'est pas défini comme une limite dans une topologie annoncée.
3. **Sans contrôle uniforme jusqu'à zéro.** Une bornitude seulement sur chaque
   `(-infinity,-delta]` ne donne pas (2). La trace distributionnelle ne se
   promeut alors pas en trace de vorticité, et (6) n'est pas disponible.

### Hypothèses qu'il ne faut pas ajouter silencieusement

- La convergence `D'` est une convergence de la **même solution** quand
  `t->0-`. Une convergence de tranches `u_n(t_n)` pour une suite de solutions
  ne la remplace pas sans compacité uniforme en temps.
- La bornitude concerne tout `R^3 x (-infinity,0)`, pas seulement l'extérieur
  d'une boule ni les cylindres compacts.
- Le mot `mild` signifie la formule d'Oseen sur des intervalles remontant vers
  `-infinity`, pas seulement une solution distributionnelle avec une pression
  choisie par Poisson.
- Le théorème d'ESS comporte une hypothèse de croissance spatiale. Elle n'est
  pas gratuite en général, mais elle est automatiquement satisfaite ici par
  la bornitude de la vorticité.

### Compatibilité avec les chaînes de blow-up

Le lemme ne ferme pas à lui seul une chaîne Clay :

- une limite ESS possède une trace locale suffisamment forte, mais n'est pas
  obtenue comme solution mild globalement bornée au cœur singulier ; ESS doit
  appliquer l'unicité rétrograde dans une région extérieure puis une
  continuation unique ;
- un élément critique GKP est mild dans `L^3` avant son temps maximal et peut
  tendre vers zéro dans `S'`, mais il n'est pas uniformément borné en
  `L^infinity_x` jusqu'au bord terminal ;
- la limite ancienne de KNSS est mild et bornée, mais sa construction conserve
  une normalisation non nulle au point terminal, plutôt qu'une trace nulle.

Le raccord falsifiable restant est donc : produire pour une **même** limite
ancienne les trois propriétés « mild globale », « borne `L^infinity`
uniforme » et « trace terminale nulle dans `D'` », tout en conservant une
normalisation non triviale. Le présent lemme montrerait immédiatement que ces
quatre propriétés sont incompatibles.

## Statut de la revue

- Résultat : dérivation analytique à partir de résultats primaires publiés.
- Calcul numérique : aucun.
- Formalisation dans un assistant de preuve : aucune.
- Revue : contradictoire séparée, non indépendante au sens d'un autre modèle.
- Portée : lemme de rigidité conditionnel ; aucune résolution de Navier–Stokes
  3D et aucune affirmation nouvelle sur l'existence de la limite requise.
