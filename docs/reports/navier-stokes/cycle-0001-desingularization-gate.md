# Cycle 0001 — Porte de désingularisation `r^-1`

Date : 2026-08-14.

## Décision du cycle

Parmi trois actions, la contribution de coquille d'une désingularisation
`r^-1` obtient 18/20 (nouveauté 4, tractabilité 5, falsifiabilité 5, levier 4),
devant le commutateur de pression (16/20) et un Liouville Type II général
(13/20). Un seul lemme et une seule expérience sont actifs.

## Équation et type de solution

Le calcul porte sur une donnée test de `R^3`,
`u_epsilon(r,theta)=r^-1 A(theta)` sur
`epsilon<=r<=1`. Il ne résout aucune évolution PDE et ne suppose ni solution
faible, ni forte. Sa pertinence pour Hou–Wang–Yang est conditionnelle à
l'identification de ce cœur homogène dans leur donnée précise.

## Échelle des quantités

Avec `A` fixe, `0<C_q=integral_S2 |A|^q<infinity`, et
`C_grad=integral_S2(|A|²+|grad_S A|²)>0`, on obtient

```text
||u_epsilon||_q^q = C_q integral_epsilon^1 r^(2-q) dr,
||nabla u_epsilon||_2² = C_grad (epsilon^-1-1).
```

Ainsi `q<3` est borné, `||u||_3^3=C_3 log(1/epsilon)`,
`||u||_q~epsilon^(3/q-1)` pour `q>3`, et
`||nabla u||_2~epsilon^-1/2`.

## Affirmations ajoutées ou modifiées

- `NS-HWY-UNFORCED-NONUNIQUENESS-V2` : source et non-transfert Clay explicites.
- `NS-DESINGULARIZATION-RMINUS1-GATE` : `COMPUTATION_ONLY`, hypothèses
  angulaires et portée de coquille ajoutées après attaque.
- `FAIL-NS-0005` : réfutation de l'inférence « grandes normes impliquent une
  obstruction dynamique ».

## Preuve / source / calcul

La dérivation est l'intégration sphérique exacte, vérifiée pour plusieurs
puissances et `epsilon=10^-k`, `k=1,2,4,8,16`, par
`DESINGULARIZATION-GATE-1`. Le logarithme est gardé symbolique; les résidus
rationnels sont exactement zéro. Le script a pour SHA-256
`70a7b82de2f93117e525e4ceb4e85d2282e28dd508047cc2f81fbbce18482b49`.

## Écart avec le problème Clay

Le test ne contrôle ni divergence, ni raccord de cutoff, ni pression, ni
évolution. Pour une troncature lisse globale, il donne seulement une borne
inférieure due à la coquille. Surtout, la divergence de normes usuelles ne
prouve pas que le temps classique tende vers zéro. L'arête
« donnée singulière non unique -> donnée lisse Clay non unique » reste
manquante; l'unicité faible–forte bloque toute bifurcation avant la perte de la
solution forte.

## Test adverse et résidu certifié

La passe séparée a imposé un contre-test dynamique. Sur `T^3`,

```text
u_N(t,x)=a_N exp(-nu N²t) sin(N x_2)e_1,  p=0
```

est globale lisse, car `div u_N=0` et `(u_N dot nabla)u_N=0`. Pour
`a_N=(log N)^(1/3)` et
`epsilon_N=[N²(log N)^(2/3)]^-1`, ses normes initiales ont les mêmes ordres
divergents suivis par le gate. Donc ces divergences seules n'ont aucune
conclusion dynamique. Le résidu PDE analytique du transport est zéro; cette
famille n'a pas été ajoutée au script car son rôle est de réfuter
l'extrapolation, pas le lemme radial.

## Artefacts mis à jour

- `experiments/navier-stokes/desingularization-gate/desingularization_gate.py` ;
- `experiments/navier-stokes/README.md` ;
- claim `NS-DESINGULARIZATION-RMINUS1-GATE` ;
- carte, graphe, journal supercritique, questions et registre d'échecs.

## État : continuer

Le lemme radial restreint survit; la conclusion dynamique est abandonnée. Il
s'agit d'une barrière contre les preuves qui exigent une borne uniforme dans
ces normes, pas d'une barrière universelle au transfert.

## Prochaine expérience décisive

Pivoter vers `GAP-PRESSURE-TAIL` : deux paquets divergence-free séparés, calcul
du terme `R_iR_j(u_i u_j)` dans la boule active, avec distance de séparation
variable et borne analytique de la queue. Le test doit distinguer l'effet
harmonique distant d'un défaut de localisation critique.
