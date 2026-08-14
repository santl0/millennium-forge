# Cycle 0004 — Défaut quadratique et pression sur une trace mobile

Date : 2026-08-14.

## Décision du cycle

Trois actions ont été notées : solution NS oscillatoire exacte créant un défaut
de trace (19/20), champ statique divergence-free à défaut quadratique (16/20),
extraction abstraite Aubin–Lions sur cylindre fixé (15/20). La première est
retenue : elle teste le verrou dans l'équation elle-même, sans erreur numérique.

## Équation et type de solution

Navier–Stokes incompressible 3D sur
`T³=(R/2piZ)³`, conditions périodiques, viscosité `nu=1`, force extérieure
nulle. Chaque membre de la famille est une solution globale analytique, donc
classique, forte, mild, Leray–Hopf et adaptée. La pression est normalisée par
une moyenne spatiale nulle.

Pour `N>=1`,

```text
u_N^0=(-sin(x_1)sin(Nx_2),-N^-1 cos(x_1)cos(Nx_2),0),
u_N(t)=exp(-(N²+1)t)u_N^0,
p_N(t)=exp(-2(N²+1)t)
       [(1/4)cos(2x_1)-(1/(4N²))cos(2Nx_2)].
```

## Échelle des quantités

La fréquence active est `N`, le temps dissipatif `N^-2` et le temps testé
`t_N=log(2)/(N²+1)`. Sous la moyenne normalisée du tore,

```text
||u_N^0||_2²=(1/4)(1+N^-2),
||u_N(t_N)||_2²=(1/16)(1+N^-2).
```

La vitesse conserve donc un défaut d'ordre un sur cette trace parabolique. Le
produit faible limite contient `(1/8)sin²(x_1)`, et la pression converge même
fortement vers `(1/16)cos(2x_1)` dans tout `L^q` fini. À tout temps fixé positif, l'amortissement
`exp(-(N²+1)t)` impose au contraire la convergence forte vers zéro.

## Affirmations ajoutées ou modifiées

- `NS-OSCILLATORY-TRACE-DEFECT-FAMILY`, `COMPUTATION_ONLY` : famille exacte et
  limites faibles explicites.
- `NS-WEAK-TRACE-IMPLIES-PRESSURE-COMPACTNESS`, `REFUTED` : énergie,
  dissipation et convergence faible d'une trace mobile ne suffisent pas.
- `NS-STRONG-L3-PRESSURE-COMPACTNESS`, `COMPUTATION_ONLY` : la convergence
  forte `L³` suffit au produit et à la pression en `L^(3/2)`.
- `FAIL-NS-0007` conserve la portée négative et les restrictions.

## Preuve / source / calcul

Le champ est le rotationnel de
`N^-1 sin(x_1)cos(Nx_2)e_3`. Le calcul direct donne

```text
div u_N^0=0,
(u_N^0 dot nabla)u_N^0
 =((1/2)sin(2x_1),-(1/(2N))sin(2Nx_2),0)=nabla q_N,
Delta u_N^0=-(N²+1)u_N^0,
p_N^0=-q_N+mean(q_N).
```

Transport et gradient de pression s'annulent exactement; le facteur de chaleur
ferme l'équation visqueuse. Les limites faibles suivent de l'orthogonalité de
Fourier : toutes les fréquences de la vitesse fuient ou ont une amplitude
`N^-1`, tandis que `sin²(Nx_2)` laisse sa moyenne `1/2` dans le produit.

Le script en fractions exactes vérifie neuf résidus pour huit fréquences. Son
empreinte avant revue est
`9c85df21a8e847f17568c5e54e2bbd57fccc45775b0994383af2d93da89756f7`.

## Écart avec le problème Clay

Il n'y a aucun blow-up : chaque solution est globale lisse. La donnée initiale
change avec `N`, les temps d'observation tendent vers la borne initiale et la
famille converge fortement dans tout cylindre espace-temps fixé. Le résultat ne
réfute ni la compacité d'une approximation de Leray dans le volume, ni une
extraction de blow-up disposant déjà d'une borne critique ou d'une trace forte.
Il montre seulement qu'une étape de trace fondée sur l'énergie et la convergence
faible serait invalide sans équicontinuité supplémentaire.

## Test adverse et résidu certifié

Le test recalcule la divergence, les deux composantes non nulles du transport,
les deux composantes du gradient de pression, l'équation de Poisson, la valeur
propre du Laplacien et l'identité d'énergie. Résidu maximal exact : `0/1`;
arrondi, grille et graine : sans objet.

La passe contradictoire séparée confirme les signes, les facteurs deux, les
quantificateurs et l'empreinte du script. Elle relève que la pression converge
fortement, et corrige la qualification de `L³` fort : ce critère est suffisant,
non minimal, car `L²` local fort suffit déjà à la convergence distributionnelle
du produit. Les trois claims passent à `adversarial_pass`, sans prétention de
revue indépendante externe.

## Artefacts mis à jour

Script et protocole d'expérience, veille différentielle, trois claims, graphe
de dépendances, carte adaptative, journal supercritique, registre d'échecs,
questions prioritaires et présent checkpoint.

## État : continuer

Le test primaire est positif comme certificat et négatif pour l'implication
universelle. Le verrou `GAP-COMPACT-Q` est réduit : la compacité intérieure
standard ne doit pas être confondue avec la compacité forte d'une trace mobile.

## Prochaine expérience décisive

Formuler une hypothèse d'équicontinuité de trace invariant sous l'échelle NS,
calculer sa loi d'échelle et tester si elle est effectivement héritée dans une
extraction de premier blow-up. Si elle exige déjà une norme de Prodi–Serrin ou
`L∞_tL³_x`, enregistrer la circularité et pivoter vers la rigidité des solutions
anciennes.
