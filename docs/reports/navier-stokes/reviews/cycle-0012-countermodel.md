# Cycle 0012 — contre-modèle asymptotique versus Cauchy fini

Date de la passe adverse : 2026-08-14.

## Verdict

Une condition commune à `tau=-infinity` n'est pas une donnée de Cauchy commune
à un temps fini. Cette différence subsiste même pour une équation autonome à
champ globalement Lipschitz et même lorsque la convergence asymptotique est
uniforme sur toute une famille bornée.

Le contre-modèle minimal est

\[
 x'=x,\qquad x_c(\tau)=c e^\tau,\qquad \tau\leq0.
\]

Toutes les trajectoires avec `|c|<=1` convergent uniformément vers zéro quand
`tau->-infinity`, mais `x_c(0)=c`. À tout temps fini, l'état distingue donc les
branches. En revanche, si deux trajectoires ont le même état à un temps fini,
la propriété Lipschitz impose qu'elles soient identiques.

Ce test réfute exactement le faux transfert

```text
même condition asymptotique à tau=-infinity
    => même donnée de Cauchy à un tau_0 fini.
```

Il ne réfute pas Hou–Wang–Yang : leur construction prescrit précisément les
coordonnées instables à `tau=0`, différentes d'une branche à l'autre, tout en
obtenant la même trace singulière lorsque `tau->-infinity`. Il réfute leur
réutilisation comme si ces coordonnées terminales restaient libres après
fixation d'une donnée lisse et d'un flot fort à temps fini.

## 1. Audit anti-duplication des cycles antérieurs

Les artefacts existants ont été relus en lecture seule avant de choisir ce
test.

| Artefact antérieur | Résultat déjà acquis | Différence avec le présent test |
| --- | --- | --- |
| cycle 0010, `HWY-INNER-CUTOFF-GATE-1` | convergence `L2` et borne `L3,weak` n'impliquent pas la compacité forte `L3` d'un coeur `1/r` | test fonctionnel statique, sans sémantique d'une condition à `-infinity` |
| cycle 0011, `HWY-PARITY-PROJECTION-GATE-1` | une régularisation paire ne projette pas sur le mode HWY impair | test de symétrie et de projection, pas de quantificateur temporel |
| revue PDE du cycle 0011, point 7 puis attaque 11 | les coordonnées HWY sont prescrites à `tau=0`; une donnée lisse fixe l'état à temps fini | observation correcte, mais sans contre-modèle autonome isolant sa nécessité |
| `FAIL-NS-0009` | une pression affine permet des solutions anciennes parasites de trace terminale nulle hors jauge mild | porte de pression et trace à `tau=0-`, pas frontière asymptotique à `-infinity` |
| `FAIL-NS-0012` | le temps terminal physique devient une extrémité mobile dans le zoom maximum KNSS | permutation de deux limites de blow-up, pas liberté d'une variété instable |
| cycle 0011, audit des artefacts | adjoint, projecteur quantitatif et constantes de semi-groupe manquants | conditionnement spectral; le présent contre-modèle reste exact même si ces artefacts sont fournis |

Le nouveau résultat ne répète donc ni `FAIL-NS-0013` ni `FAIL-NS-0014`.
Il ferme une arête logique située en aval : même un projecteur parfait et une
couche impaire non nulle ne convertiraient pas une famille ancienne en deux
solutions d'un **même** problème de Cauchy fort à temps fini.

## 2. Modèle Lipschitz exact

### 2.1 Forme en temps de similarité

Fixons l'équation scalaire autonome

\[
 \frac{dx}{d\tau}=x\quad\hbox{sur }(-\infty,0].
 \tag{1}
\]

Son champ `f(x)=x` est globalement Lipschitz de constante `1`. Pour chaque
`c in [-1,1]`, posons

\[
 x_c(\tau)=c e^\tau.
 \tag{2}
\]

Le résidu est identiquement nul : `x_c'-x_c=0`. La convergence à l'infini
passé est plus forte qu'une convergence branche par branche :

\[
 \sup_{|c|\leq1}|x_c(\tau)|=e^\tau\longrightarrow0
 \qquad(\tau\to-\infty).
 \tag{3}
\]

Pourtant, pour tout `tau_0` fini,

\[
 x_c(\tau_0)-x_d(\tau_0)=(c-d)e^{\tau_0},
 \tag{4}
\]

donc `x_c(tau_0)=x_d(tau_0)` si et seulement si `c=d`.

Cette famille sépare deux phénomènes souvent confondus :

- la borne à l'infini passé élimine les modes qui explosent lorsque
  `tau->-infinity`, mais ne fixe pas l'amplitude des modes qui y décroissent ;
- une donnée à un temps fini fixe cette amplitude par injectivité du flot.

Le coefficient perdu par la trace d'ordre zéro reste visible au premier ordre
asymptotique :

\[
 e^{-\tau}(x_c-x_d)=c-d.
 \tag{5}
\]

Ainsi, exiger seulement `x_c-x_d=o(1)` laisse `c-d` libre. Dans ce modèle,
exiger la condition plus forte `x_c-x_d=o(e^tau)` force au contraire `c=d`.
Tout argument de variété instable doit donc annoncer le taux et l'ordre
asymptotique, pas seulement une « même limite ».

### 2.2 Forme dégénérée au temps physique

Avec `t=e^tau`, l'infini passé devient `t=0+` et (1) devient

\[
 t\frac{dx}{dt}=x,
 \qquad x_c(t)=ct,
 \qquad 0<t\leq1.
 \tag{6}
\]

Chaque solution s'étend continûment par `x_c(0)=0`. L'équation dégénère
précisément à `t=0`; la valeur commune `0` n'y détermine pas la pente `c`.
À tout `t_0>0`, l'équation est régulière et `x_c(t_0)=ct_0` détermine `c`.

Cette écriture empêche un autre faux raisonnement : l'unicité de l'ODE
`x'=x` à un temps fini ne peut pas être appliquée directement à la frontière
`tau=-infinity`, et l'extension continue de (6) n'en fait pas une ODE
Lipschitz standard au point dégénéré `t=0`.

## 3. Dictionnaire exact avec le mode instable HWY

Dans les variables de similarité de
[Hou–Wang–Yang, arXiv:2509.25116v2](https://arxiv.org/abs/2509.25116v2),
un mode linéaire de taux `a>0` a la forme

\[
 \phi_c(\xi,\tau)=c e^{a\tau}v(\xi).
 \tag{7}
\]

À `tau=0`, sa coordonnée est `c`. Lorsque `tau->-infinity`, elle tend vers zéro
pour tout `c`; la trace asymptotique ne fixe donc pas cette coordonnée. C'est
pourquoi la construction HWY peut choisir des `U_j0=P_jU(0)` distincts et
intégrer les coordonnées instables vers le passé.

En variables physiques,

\[
 w_c(t,x)=t^{-1/2}\phi_c(x/\sqrt t,\log t)
 =c\,t^{a-1/2}v(x/\sqrt t).
 \tag{8}
\]

Si `v in L2`, alors

\[
 \|w_c(t)-w_d(t)\|_2^2
 =|c-d|^2t^{2a+1/2}\|v\|_2^2
 \longrightarrow0.
 \tag{9}
\]

Ainsi des branches distinctes à chaque `t>0` peuvent avoir exactement la même
trace `L2` à `t=0`. Ce mécanisme est compatible avec une non-unicité faible
issue de la donnée singulière HWY. Il ne donne pas une seconde solution forte
issue d'une donnée Clay lisse : pour une telle donnée, la théorie locale forte
et l'unicité faible–forte déterminent un seul état aux temps positifs assez
petits.

Plus généralement, si `v in Lq`,

\[
 \|w_c(t)-w_d(t)\|_q
 =|c-d|t^{a-1/2+3/(2q)}\|v\|_q.
 \tag{10}
\]

Le choix de topologie est donc un quantificateur substantiel. Une trace
commune en `L2` n'implique ni égalité à temps positif, ni trace commune dans
une norme plus forte, ni continuité du flot dans une norme critique.

Pour chaque régularisation lisse fixée `epsilon`, la donnée est posée au temps
physique `t=0` dans la classe forte locale. Elle détermine donc un état unique
à tout `t_epsilon>0` antérieur au temps maximal, c'est-à-dire à un
`tau_epsilon=log(t_epsilon)` fini. Réintroduire alors plusieurs valeurs de `c`
suppose déjà une perte d'unicité avant `t_epsilon`; ce n'est pas une liberté
héritée de la frontière `tau=-infinity`.

L'identité (9) est seulement un dictionnaire de changement d'échelle pour un
mode. Elle ne prétend pas que (7) seul résout l'équation Navier–Stokes non
linéaire; les termes de correction de HWY sont nécessaires.

## 4. Quantificateurs attaqués

Soit `C=[-1,1]`. La famille (2) vérifie le quantificateur uniforme

\[
 \forall\varepsilon>0\ \exists T<0\ \forall c\in C\ \forall\tau<T,
 \quad |x_c(\tau)|<\varepsilon.
 \tag{11}
\]

Elle réfute chacune des conclusions suivantes :

\[
 \exists\tau_0> -\infty\ \forall c,d\in C,
 \quad x_c(\tau_0)=x_d(\tau_0),
 \tag{12}
\]

et même

\[
 \exists\tau_0> -\infty\ \exists c\ne d,
 \quad x_c(\tau_0)=x_d(\tau_0).
 \tag{13}
\]

Le remplacement illégal est donc celui de « pour tout epsilon, assez loin
dans le passé » par « il existe un temps fini commun où l'écart est zéro ».
La convergence uniforme de (11) ne répare pas cette inversion.

Autres faux transferts isolés :

1. `x_c-x_d -> 0` n'implique pas que le coefficient asymptotique de premier
   ordre soit le même; (5) le conserve exactement.
2. Une coordonnée choisie librement à `tau=0` dans une construction ancienne
   n'est pas une coordonnée libre à la sortie du flot en avant d'une donnée
   lisse fixée.
3. Deux familles de données lisses `u_epsilon^+` et `u_epsilon^-` qui
   convergent vers la même donnée singulière ne sont pas une même donnée lisse
   pour `epsilon>0`.
4. Deux limites de régularisations différentes peuvent montrer une sélection
   non unique de la donnée singulière; elles ne montrent pas deux évolutions
   pour un membre fixé de la famille régularisée.
5. Une projection spectrale non nulle au temps de couche ne donne pas une
   seconde solution du même problème de Cauchy : elle décrit l'état unique de
   ce flot, sauf perte préalable de l'unicité dans la classe considérée.
6. Fixer après coup une coordonnée terminale et ajuster rétrospectivement la
   couche est un problème de tir à deux bords, pas la résolution en avant d'une
   donnée initiale déjà fixée.

## 5. Cas non-Lipschitz : pourquoi la classe de solution est indispensable

La réciproque « même donnée à temps fini implique même trajectoire » exige une
hypothèse d'unicité. Considérons sur `[0,2]`

\[
 y'=2\sqrt{\max(y,0)},\qquad y(0)=0.
 \tag{14}
\]

Pour tout temps d'attente `theta>=0`, la fonction

\[
 y_\theta(t)=
 \begin{cases}
 0,&t\leq\theta,\\
 (t-\theta)^2,&t\geq\theta
 \end{cases}
 \tag{15}
\]

est `C1` et satisfait (14) ponctuellement. Les solutions `y_0` et `y_1` ont la
même donnée finie `y(0)=0`, mais
`y_0(1/2)-y_1(1/2)=1/4`.

Le défaut de Lipschitz est exact. Pour `h>0`,

\[
 \frac{|2\sqrt{h^2}-0|}{|h^2-0|}=\frac2h\to\infty.
 \tag{16}
\]

Ce modèle n'est pas une réduction de Navier–Stokes et ne prouve aucune
non-unicité PDE. Il interdit seulement de citer l'unicité d'un flot sans
préciser la classe. Pour Navier–Stokes 3D :

- dans la classe forte/mild locale associée à une donnée Clay lisse, le flot
  est unique et l'unicité faible–forte verrouille toute branche Leray–Hopf tant
  que la solution forte existe ;
- dans une classe faible où l'unicité n'est pas acquise, une donnée finie
  commune peut en principe admettre plusieurs solutions, mais cela doit être
  démontré dans cette classe exacte ;
- importer le modèle d'attente comme mécanisme PDE serait un faux transfert
  supplémentaire.

## 6. Obligations machine-readable proposées

Le bloc JSON suivant est l'artefact minimal proposé. Les obligations `A*`
portent sur le modèle Lipschitz et les quantificateurs; `N*` sont les gardes
non-Lipschitz; `P*` empêchent le faux transfert à Navier–Stokes. Les résidus
cibles sont symboliques ou rationnels exacts.

```json
{
  "artifact_id": "ASYMPTOTIC-VS-FINITE-CAUCHY-GATE-1",
  "version": 1,
  "arithmetic": "Fraction/integer; no floating point",
  "models": {
    "asymptotic_lipschitz": {
      "equation_tau": "dx/dtau=x on (-infinity,0]",
      "equation_t": "t*dx/dt=x on (0,1]",
      "family": "x_c(t)=c*t, c in [-1,1]"
    },
    "finite_non_lipschitz": {
      "equation": "dy/dt=2*sqrt(max(y,0)) on [0,2]",
      "family": "y_theta(t)=max(t-theta,0)^2"
    }
  },
  "obligations": [
    {
      "id": "A1_LINEAR_RESIDUAL",
      "assertion": "t*d(c*t)/dt-c*t=0",
      "expected_residual": "0"
    },
    {
      "id": "A2_UNIFORM_ZERO_TRACE",
      "assertion": "sup_|c|<=1 |x_c(2^-n)|<=2^-n",
      "expected": true
    },
    {
      "id": "A3_FINITE_SEPARATION",
      "assertion": "x_1(1)-x_0(1)=1",
      "expected": "1"
    },
    {
      "id": "A4_FINITE_INJECTIVITY",
      "assertion": "q0>0 and x_c(q0)=x_d(q0) imply c=d",
      "method": "cancel the nonzero rational q0"
    },
    {
      "id": "A5_LEADING_COEFFICIENT_SURVIVES",
      "assertion": "2^n*(x_1(2^-n)-x_0(2^-n))=1",
      "expected": "1"
    },
    {
      "id": "A6_L2_TRACE_SCALING",
      "assertion": "for a=1, ||v||_2=1, t_n=4^-n: ||w_1(t_n)-w_0(t_n)||_2^2=2^(-5n)",
      "expected_limit": "0"
    },
    {
      "id": "N1_WAITING_RESIDUAL",
      "assertion": "d max(t-theta,0)^2/dt=2*sqrt(max(y_theta,0))",
      "expected_residual": "0 on both pieces and at t=theta"
    },
    {
      "id": "N2_SAME_FINITE_DATA_DIFFERENT_FUTURE",
      "assertion": "y_0(0)=y_1(0)=0 and y_0(1/2)-y_1(1/2)=1/4",
      "expected": true
    },
    {
      "id": "N3_LIPSCHITZ_QUOTIENT_DIVERGES",
      "assertion": "for h_n=2^-n, |f(h_n^2)-f(0)|/h_n^2=2^(n+1)",
      "expected": true
    },
    {
      "id": "P1_NO_PDE_PROMOTION",
      "assertion": "ODE identities are not a Navier-Stokes solution or proof",
      "required_status": "logical countermodel only"
    },
    {
      "id": "P2_FIXED_SMOOTH_DATUM",
      "assertion": "two regularization signs or amplitudes at fixed epsilon are different Cauchy data",
      "required_evidence_for_override": "exact equality in the strong-data topology"
    },
    {
      "id": "P3_UNIQUENESS_CLASS",
      "assertion": "any inference from equal finite data to equal evolution names a well-posed solution class and interval",
      "required_evidence_for_override": "a class-specific uniqueness theorem"
    }
  ]
}
```

## 7. Test exact reproductible

Le script de contrôle ci-dessous n'utilise que `fractions.Fraction`. Les
identités générales sont démontrées par les calculs (1)--(16); le script
vérifie leur transcription sur une plage finie de rationnels et n'est pas
présenté comme une preuve numérique de ces identités.

```powershell
@'
from fractions import Fraction as F

# Modèle Lipschitz, écrit avec t=exp(tau).
for n in range(1, 33):
    t = F(1, 2**n)
    for c in (F(-1), F(0), F(1)):
        x = c*t
        residual = t*c - x                 # t*x'(t)-x(t)
        assert residual == 0
        assert abs(x) <= t                  # convergence uniforme |c|<=1
    assert 2**n * (F(1)*t - F(0)*t) == 1  # coefficient asymptotique

assert F(1)*F(1) - F(0)*F(1) == 1          # séparation à tau=0, t=1

# Dictionnaire L2 pour a=1, ||v||_2=1, t_n=4^-n.
for n in range(1, 17):
    t = F(1, 4**n)
    l2_squared = F(1, 2**(5*n))
    assert l2_squared > 0
    assert l2_squared*l2_squared == t**5  # (t^(5/2))^2=t^5

# Modèle non-Lipschitz aux points rationnels, theta=0 et theta=1.
def y(t, theta):
    return max(t-theta, F(0))**2

assert y(F(0), F(0)) == y(F(0), F(1)) == 0
assert y(F(1, 2), F(0)) - y(F(1, 2), F(1)) == F(1, 4)
for n in range(1, 17):
    h = F(1, 2**n)
    quotient = 2/h
    assert quotient == 2**(n+1)

print("A1-A6: PASS (exact rational arithmetic)")
print("N1-N3: PASS (analytic pieces; rational witnesses)")
print("P1-P3: semantic guards, not numerical claims")
'@ | python -
```

Sortie attendue :

```text
A1-A6: PASS (exact rational arithmetic)
N1-N3: PASS (analytic pieces; rational witnesses)
P1-P3: semantic guards, not numerical claims
```

Le test ne contient ni discrétisation PDE, ni pas temporel, ni flottant, ni
graine. Son résidu algébrique est zéro. Sa limite est explicite : il certifie
une obstruction logique et non une propriété nouvelle de l'opérateur
Navier–Stokes.

## 8. Statut scientifique et décision

Statuts proposés, sans créer automatiquement de claim dans cette passe :

- implication universelle « trace asymptotique commune à `-infinity` implique
  donnée finie commune » : **REFUTED** par (1)--(5) ;
- garde « donnée finie commune implique trajectoire commune » :
  **CONDITIONNELLE À LA CLASSE D'UNICITÉ**, réfutée sans cette hypothèse par
  (14)--(16) ;
- contre-modèle et dictionnaire d'échelle produits par l'agent :
  **COMPUTATION_ONLY**, revue contradictoire interne, aucun `PAPER_PROOF` ;
- fait que HWY prescrit les coordonnées instables à `tau=0` et obtient la trace
  à `tau=-infinity` : **SOURCE_VERIFIED** par leur section 2.2 ;
- transfert direct vers deux solutions pour une même donnée Clay lisse :
  **NON ÉTABLI** et arête à classer `REFUTED` si elle utilise seulement le faux
  transfert de quantificateurs ci-dessus.

Décision : **ABANDONNER** la route « choisir deux coordonnées HWY terminales,
puis les attribuer à une même régularisation lisse ». Une réouverture exige au
minimum l'un des deux objets suivants :

1. une perte de régularité forte démontrée avant le temps de séparation, ce qui
   constituerait déjà un breakdown de type Clay ;
2. un théorème de shadowing à deux branches dans une classe où la donnée de
   Cauchy finie est exactement identique et où l'unicité faible–forte ne les
   force pas à coïncider.

La prochaine obligation décisive n'est donc plus une meilleure projection de
la couche : c'est un contrat de quantificateurs vérifiant, pour un même
`u_epsilon` fixé, le même temps initial fini, la même notion de trace, la même
classe de solution et l'instant précis où l'unicité forte cesse de s'appliquer.
