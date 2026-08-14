# Cycle 0012 — Trace asymptotique et donnée de Cauchy finie

Date de gel : 2026-08-14.

## Décision du cycle

La veille différentielle n'a trouvé aucun résultat primaire transférant la
multiplicité issue d'une trace critique singulière à une même donnée Clay
lisse. Trois actions ont été notées sur 5 :

| Action | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| tester l'injectivité du flot fort à temps fini face à une trace commune à `tau=-infinity` | 4 | 5 | 5 | 5 | **19** |
| construire une couche impaire divergence-free et suivre son coefficient spectral formel | 4 | 5 | 5 | 3 | 17 |
| formaliser immédiatement les projecteurs de parité finis en Lean | 3 | 3 | 5 | 3 | 14 |

La première action est sélectionnée. Lemme actif unique : une donnée de Cauchy
forte fixée à un temps fini détermine une trajectoire unique sur l'intervalle
fort commun, tandis qu'une condition asymptotique trop faible à
`tau=-infinity` peut laisser libres des coordonnées instables. Expérience
active unique : `ASYMPTOTIC-TRACE-CAUCHY-GATE-1`.

## Équation et types de solution

Le cadre exact est

```text
partial_t u + (u dot nabla)u - Delta u + nabla p = 0,
div u = 0
```

sur `R³`, sans frontière ni force, avec viscosité `nu=1`. On compare une
solution forte/classique `u` et une solution de Leray–Hopf `v` sur un intervalle
commun `[t0,T]`, issues de la même donnée dans `L²` au temps fini `t0`.

Le résultat HWY porte sur une donnée compacte mais singulière en zéro. En
variables de similarité `tau=log t`, la donnée physique à `t=0` devient une
condition asymptotique quand `tau->-infinity`. Les coordonnées instables sont
prescrites à `tau=0` puis intégrées vers le passé; elles disparaissent dans la
trace critique singulière. Cette situation n'est pas le problème de Cauchy fort
posé à un temps de similarité fini.

## Veille primaire différentielle

- Hou–Wang–Yang reste `arXiv:2509.25116v2`, prépublication du 19 mars 2026;
  aucun théorème de stabilité sous lissage intérieur n'a été ajouté.
- Ionescu–Jia–Palasek `arXiv:2606.07501v1` demeure conditionnel à un profil et
  un mode exacts; sa donnée est également critique et singulière.
- Coiculescu–Palasek, publié en ligne en décembre 2025 dans
  *Inventiones Mathematicae*, volume 244 (2026), construit deux solutions
  globales lisses pour `t>0` sur `T³` depuis une même donnée dans
  `BMO^-1(T³)` hors `L²`. Ce résultat renforce précisément la distinction :
  la trace est critique, d'énergie infinie et non lisse, donc hors donnée Clay
  classique.
- Cheskidov–Zeng–Zhang `arXiv:2503.05692v1` construit une infinité de
  solutions faibles à énergie continue et décroissante depuis toute donnée
  `H^{1/2}(T³)`, mais précise qu'elles ne satisfont pas l'inégalité d'énergie
  de Leray–Hopf. La monotonie d'un scalaire ne remplace donc pas
  l'admissibilité faible–forte.
- Palasek `arXiv:2509.18595v1` construit des données lisses **distinctes**,
  uniformément bornées dans `B^{-1}_{infinity,1}`, dont les solutions fortes
  globales ont une croissance arbitraire. Cela réfute certaines bornes
  critiques, pas l'unicité ni la globalité.
- Liao–Qin `arXiv:2602.12666v1` est un calcul CNS d'un écoulement de
  Kolmogorov 2D forcé depuis des données différentes de `10^-10` à `10^-40`.
  La sensibilité chaotique observée n'est pas une non-unicité de Cauchy 3D.
- Cheskidov–Dai–Palasek `arXiv:2511.09556v2` construit des branches faibles
  depuis des données lisses, mais l'injection instantanée depuis les fréquences
  infinies quitte la classe Leray–Hopf près de l'événement. Elle ne constitue
  pas deux continuations fortes de la solution classique Clay.
- Galdi–Gazzola `arXiv:2606.15189v3` construit sur `R³` une solution
  Leray–Hopf forcée, unique, globale au sens faible et ayant des instants de
  blow-up. Cela ne réfute pas (A), où `f=0`, et ne réalise pas (C), car la
  force n'est pas `C∞` rapidement décroissante au sens Clay : elle appartient
  seulement aux classes d'intégrabilité spécialement ajustées au blow-up.

Aucune de ces sources ne rend multivoque le flot fort local à partir d'une
même donnée lisse.

## Lemme borné : injectivité sur l'intervalle fort

Posons `w=v-u`. Pour deux solutions lisses, la soustraction donne

```text
partial_t w - Delta w
  + (w dot nabla)u + (v dot nabla)w + nabla q = 0,
div w = 0.
```

Le transport par `v` et la pression ne travaillent pas contre `w`. Avec la
convention `E=(1/2)||w||_2²`,

```text
dE/dt + ||nabla w||_2²
  = -integral_R3 (w dot nabla)u dot w
  <= ||nabla u||_infinity ||w||_2²
  = 2 ||nabla u||_infinity E.
```

La même inégalité sous forme intégrée est l'identité de relative énergie de
l'unicité faible–forte quand `v` est seulement Leray–Hopf. Si

```text
integral_(t0)^T ||nabla u(t)||_infinity dt < infinity,
```

alors

```text
E(t) <= E(t0)
  exp(2 integral_(t0)^t ||nabla u(s)||_infinity ds).
```

La constante devant le coefficient de Grönwall est exactement `2` avec cette
normalisation de `E`. Lorsque `u(t0)=v(t0)`, on obtient `E=0`. La projection de
Leray ou, équivalemment, l'annulation du pairing avec les gradients recalcule
explicitement la pression non locale; elle ne crée pas de degré de liberté.

Une revue PDE séparée a également recalculé la version de Serrin stricte. Pour
`q>3`, `2/s+3/q=1`, l'estimation par Hölder, Gagliardo–Nirenberg et Young donne
un coefficient intégrable de la forme

```text
C_q nu^(-(q+3)/(q-3)) ||u||_q^s.
```

L'endpoint `L^infinity_t L³_x` n'est pas obtenu par cette dérivation
élémentaire et n'est pas introduit silencieusement ici.

Conclusion conditionnelle exacte : deux branches Leray–Hopf issues d'une même
donnée lisse ne peuvent se séparer avant la perte de la solution forte. Si
cette perte survient en temps fini, elle constitue déjà le breakdown demandé
par l'alternative négative Clay; si elle ne survient pas, l'unicité
faible–forte interdit le transfert de multiplicité.

## Contre-modèle logistique exact

Considérons, pour `a>0`,

```text
b'=a b-b²,
q=exp(a tau),
b_A(tau)=a A q/(a+Aq),  A>0.
```

Le script vérifie exactement

```text
b_A'=a b_A-b_A²,
lim_(tau->-infinity) b_A(tau)=0,
lim_(tau->-infinity) b_A(tau)/exp(a tau)=A.
```

Toutes les trajectoires partagent donc la trace asymptotique zéro. À tout
temps fini, `q0>0`, l'état satisfait `0<b<a` et inverse exactement le
paramètre :

```text
A = a b/[q0(a-b)].
```

Pour `A!=B`,

```text
b_A-b_B = a²(A-B)q/[(a+Aq)(a+Bq)] != 0
```

dès que `q>0`. La condition à moins l'infini écrase donc l'information portée
par la première coordonnée asymptotique; une donnée finie ne l'écrase pas.

Dans le dictionnaire HWY, `a>=217/2000` et une coordonnée instable se comporte
comme `A exp(a tau)` vers le passé. Mesurer un coefficient adjoint d'une donnée
lissée peut identifier une trajectoire ou une sensibilité de sélection; cela
ne rend pas le problème de Cauchy multivoque pour cette donnée lisse fixée.
Plus précisément, une différence physique
`delta u=(c-d)t^(a-1/2) v(x/sqrt(t))` vérifie

```text
||delta u(t)||²_2=|c-d|² t^(2a+1/2)||v||²_2.
```

Elle peut donc avoir trace `L²` nulle tout en séparant les branches à chaque
temps strictement positif.

## Test adverse non lipschitzien

Le contrôle

```text
x'=2 sqrt(x), x>=0,
x_c(t)=(t-c)_+², c>=0
```

admet une infinité de solutions depuis la même donnée finie `x(0)=0`. Le
script vérifie le résidu exact zéro pour `c=0,1,2`; à `t=3`, les états sont
respectivement `9`, `4` et `1`.

La différence est localisée : `2sqrt(x)` n'est pas localement lipschitzien en
zéro. Le contre-test interdit donc d'étendre le lemme d'injectivité à une classe
faible arbitraire. Pour Navier–Stokes, la perte de la classe forte est
précisément l'endroit où la question Clay reste ouverte.

## Échelle, quantificateurs et limites

Sous

```text
u_lambda(x,t)=lambda u(lambda x,lambda²t),
```

`t=0` reste `tau=-infinity`; aucune remise à l'échelle ne transforme cette
extrémité asymptotique en une donnée forte commune à `tau0` fini. Pour chaque
donnée lissée fixée, l'état à `t_epsilon=kappa epsilon²` est déjà déterminé par
le flot fort depuis `t=0`.

Le résultat ne prouve pas une borne globale de
`integral ||nabla u||_infinity`, ne prolonge pas la solution forte, et
n'interdit pas une non-unicité faible après un breakdown. Le modèle ODE n'est
ni une réduction de Navier–Stokes ni un calcul de pression ou de projecteur
HWY.

## Passe contradictoire

1. **Quantificateur inversé.** Même limite quand `tau->-infinity` ne signifie
   pas même état à un `tau0` fini.
2. **Coefficient de Grönwall.** L'intégrabilité de
   `||nabla u||_infinity` n'est affirmée que sur l'intervalle fort, jamais
   uniformément jusqu'à un temps maximal supposé singulier.
3. **Notion de solution.** Le contrôle non lipschitzien et les constructions
   faibles récentes montrent que l'injectivité forte ne doit pas être attribuée
   à toute solution distributionnelle.
4. **Pression.** Elle disparaît du pairing seulement grâce à la divergence
   nulle et aux espaces autorisant l'intégration par parties; elle demeure
   non locale dans toute tentative de shadowing.
5. **Données différentes.** Deux lissages impairs de signes opposés restent
   deux données Clay différentes, même s'ils convergent vers la même trace
   singulière.
6. **Circularité.** Supposer deux branches distinctes avant la perte forte
   contredit l'unicité locale; supposer la perte forte fournit déjà l'événement
   Clay que la route cherchait à construire.

Trois revues contradictoires ont été produites séparément : analyse PDE,
contre-modèles/quantificateurs et veille primaire. Elles convergent sur la
porte négative; la revue PDE a ajouté le coefficient de Serrin, la revue des
contre-modèles le facteur physique `t^(2a+1/2)`, et la veille a corrigé
Galdi–Gazzola vers la version courante `v3`. Ces revues proviennent toutefois
de sous-agents Codex de la même famille de modèle : elles ne constituent pas
une validation externe indépendante.

## Règle des trois stratégies et pivot

Le raccord HWY vers une même donnée Clay lisse a maintenant subi trois attaques
réellement différentes :

1. cycle 0010 — la convergence `L²` et la borne `L^{3,infinity}` ne donnent
   aucune compacité forte `L³` du cutoff intérieur;
2. cycle 0011 — le lissage radial pair projette exactement zéro sur le mode
   instable impair certifié;
3. cycle 0012 — une trace commune à `tau=-infinity` ne devient pas une donnée
   de Cauchy finie commune, laquelle est injective tant que la classe forte
   subsiste.

Le verrou `GAP-LIMIT-ADMISSIBLE` est suspendu. Il ne sera rouvert qu'avec un
mécanisme démontré de perte forte pour une donnée lisse fixée, ou un nouveau
théorème de stabilité non perturbatif qui ne réutilise aucune des trois
inférences réfutées.

Pour le pivot, les prochains axes sont notés : géométrie locale de la vorticité
et triades signées `17/20`; opérateur renormalisé compact à queues certifiables
`16/20`; noyau Fourier–Leray formel `15/20`. Le premier est sélectionné pour le
cycle suivant.

## Décision

La route HWY par simple désingularisation est classée **À REPRENDRE** et
`FAIL-NS-0015` conserve l'inférence réfutée. Le programme pivote vers une
question locale de vorticité : déterminer par un contre-profil Fourier exact si
une cohérence directionnelle quantitative, plus forte que l'hélicité globale,
impose réellement un signe ou une déplétion du terme d'étirement.
