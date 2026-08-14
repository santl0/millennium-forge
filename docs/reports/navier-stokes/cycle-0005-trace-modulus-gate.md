# Cycle 0005 — Porte critique du module temporel de trace

Date : 2026-08-14.

## Décision du cycle

Trois actions ont été notées : seuil critique du module de trace et test NS
exact (19/20), endpoint de trace par Aubin–Lions local (15/20), module temporel
dans un espace de Besov critique (15/20). La première est retenue parce qu'elle
mesure exactement la perte d'échelle identifiée au cycle 0004.

## Équation et type de solution

La loi d'échelle concerne NS incompressible 3D sur `R³`, sans frontière :

```text
partial_t u+(u dot nabla)u+nabla p=nu Delta u,
div u=0,
u_lambda(x,t)=lambda u(lambda x,lambda²t).
```

L'estimation énergétique est formulée pour une solution Leray–Hopf de moyenne
nulle sur `T³`, `nu>0`, force nulle, avec la norme spectrale `dot H^-1`. Le test adverse réutilise les solutions
globales analytiques périodiques du cycle 0004 avec `nu=1`.

## Échelle des quantités

Pour les espaces homogènes de `R³`,

```text
[u_lambda]_(C_t^alpha dot H_x^sigma)
 =lambda^(sigma-1/2+2alpha)[u]_(C_t^alpha dot H_x^sigma).
```

Le seuil critique est `alpha=1/4-sigma/2`. Ainsi
`C_t^(1/4)L²` et `C_t^(3/4)dot H^-1` sont critiques. Le module énergétique
`C_t^(1/4)dot H^-1` se transforme avec `lambda^-1` et devient incontrôlé sous le
zoom de blow-up `lambda->0`.

## Affirmations ajoutées ou modifiées

- `NS-TIME-TRACE-SCALING-LAW`, `COMPUTATION_ONLY` : loi générale et deux
  seuils critiques.
- `NS-ENERGY-HMINUS1-TIME-MODULUS`, `COMPUTATION_ONLY` : estimation temporelle
  avec `C_GN`, énergie et dissipation suivies.
- `NS-ENERGY-IMPLIES-CRITICAL-TRACE-MODULUS`, `REFUTED` : aucune borne
  uniforme des deux modules critiques ne découle de l'énergie seule.
- `NS-PRECOMPACT-DATA-UNIFORM-INITIAL-TRACE`, `COMPUTATION_ONLY` : une famille
  initiale fortement précompacte et le module `V'` rétablissent une trace forte
  uniforme, sans taux critique `L²` supposé.
- `FAIL-NS-0008` et l'obstacle consolidé enregistrent le troisième échec sur
  `GAP-COMPACT-Q` sous énergie seule.

## Preuve / source / calcul

La dérivée temporelle vérifie dans `dot H^-1`

```text
||partial_t u||_(dot H^-1)
 <= nu||nabla u||_2+C_GN²||u||_2^(1/2)||nabla u||_2^(3/2).
```

Sur `I=[s,t]`, Hölder donne, avec
`M_I=sup_I||u||_2` et
`D_I²=integral_I||nabla u||_2²`,

```text
||u(t)-u(s)||_(dot H^-1)
 <=nu |I|^(1/2)D_I
   +C_GN² M_I^(1/2)|I|^(1/4)D_I^(3/2).
```

Sur `[0,T]`, le semi-module est donc borné par
`nu T^(1/4)D_T+C_GN²M_T^(1/2)D_T^(3/2)`.

Pour la famille exacte et `t_N=log(2)/(N²+1)`, les quotients critiques sur la
paire `(0,t_N)` ont des quatrièmes puissances proportionnelles à
`(N²+1)^3/N^4~N²`, donc divergent comme `N^(1/2)`. Le quotient énergétique
faible a une quatrième puissance proportionnelle à
`(N²+1)/N^4~N^-2` et tend vers zéro comme `N^(-1/2)`.

Le script exact a pour SHA-256
`131dbc3439a065a408ef24aa49b9a892979cd9dd6c65d44eacf54223b871c1cf`.

L'audit bibliographique ajoute Foias–Rosa–Temam 2013 (`NS-SRC-0043`) : il
sépare continuité forte initiale individuelle, compacité faible de trajectoire
et uniformité sur une famille. Une projection de Fourier finie montre en plus
que des données initiales précompactes `L²`, contrairement à la famille
adverse, suffisent à rendre la trace forte uniforme.

## Écart avec le problème Clay

Le résultat ne construit aucune singularité et n'exclut pas une structure de
trace supplémentaire propre à une solution minimale de blow-up. La loi
d'échelle est sur `R³`, tandis que le contre-test est périodique. Elle suffit à
réfuter une estimation universelle issue des seules bornes énergétiques, pas à
décrire toutes les limites de premier blow-up.

## Test adverse et résidu certifié

Le script vérifie les exposants d'échelle, l'identité spectrale `dot H^-1`, trois
quotients normalisés et leurs asymptotiques pour `N=1,2,4,...,128`. `log(2)`
reste symbolique. Résidu maximal exact : `0/1`; grille, arrondi et graine : sans
objet.

La passe contradictoire séparée a recalculé la convention d'échelle, les
puissances de `log(2)`, les exposants de Hölder, la norme spectrale
`dot H^-1`, l'horizon fini et la distinction entre tore et espace entier. Les
quatre claims passent à `adversarial_pass`, sans revue externe revendiquée.

## Artefacts mis à jour

Veille différentielle, source primaire `NS-SRC-0043`, extraction des topologies
temporelles, script et protocole `TRACE-MODULUS-1`, quatre claims, graphe de
dépendances, carte adaptative, journal supercritique, registre d'échecs,
questions prioritaires et présent checkpoint.

## État : continuer

Le lemme de porte est positif, mais son application depuis l'énergie est
réfutée. Après trois stratégies distinctes bloquées sur `GAP-COMPACT-Q` sous
énergie seule, cet axe est suspendu conformément au protocole.

## Prochaine expérience décisive

Pivoter vers les solutions anciennes : extraire, source par source, la classe
exacte obtenue par ESS/GKP/KNSS à partir d'un premier blow-up, puis tester le
premier théorème de Liouville proposé contre les solutions anciennes triviales,
stationnaires, auto-similaires, discrètement auto-similaires et Type II. Le
premier résultat attendu est un lemme unique de rigidité avec toutes ses
hypothèses, ou un contre-exemple qui force leur renforcement.
