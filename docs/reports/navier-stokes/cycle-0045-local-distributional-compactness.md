# Cycle 0045 — compacité locale adaptée et porte de trace critique

Date : 2026-08-15.

## Décision adaptative

Trois actions distinctes ont été notées sur 5 en nouveauté, tractabilité,
falsifiabilité et effet de levier.

| action | nouveauté | tractabilité | falsifiabilité | levier | total |
|---|---:|---:|---:|---:|---:|
| Caccioppoli locale, remplissage des trous, puis Simon | 4 | 5 | 5 | 5 | **19** |
| régularité parabolique strictement sous-critique | 4 | 4 | 5 | 4 | 17 |
| transport direct de la capture faible-`L3` à la trace | 4 | 2 | 5 | 5 | 16 |

La première action est sélectionnée. Le brouillon initial du cycle ne
revendiquait qu'une compacité distributionnelle sous-critique. La passe
contradictoire analytique a identifié une estimation plus forte et corrigé
l'affirmation erronée selon laquelle la borne faible-`L3`, jointe à la PDE,
ne fournirait aucune énergie locale. La norme seule ne fournit pas cette
énergie; l'équation lisse, la pression de Riesz, l'absorption et le
remplissage des trous la fournissent.

Le lemme actif devient donc la compacité **adaptée** locale. L'expérience
décisive attaque séparément la persistance de la trace critique.

## Cadre exact

Fixons `I=[-S,0]`, `S>0`, et une constante réelle `kappa`. Pour chaque `j`,
on considère un champ classique solénoïdal `Z_j` sur `R3 x I` satisfaisant

```text
partial_s Z_j-Delta Z_j+div(Z_j tensor Z_j)+nabla Pi_j
  +kappa D Z_j=F_j,
div Z_j=0,                                      (45.1)
D=1+y dot nabla,
Pi_j=R_aR_b(Z_(j,a)Z_(j,b)).
```

La viscosité vaut un, le domaine est sans frontière et la pression est dans
la jauge globale de Riesz. Les champs proviennent de la troncation externe
`Z_j=Q_(L_j)U_j`, avec `L_j->infinity`, par conjugaison d'un même opérateur
de Bogovskii. On suppose

```text
sup_j ess sup_(s in I) K_3(Z_j(s)) <= C_Q M,    (45.2)
F_j ->0 dans C^infinity_x(K),
uniformément pour s in I et tout compact K.     (45.3)
```

La convergence (45.3) implique en particulier une borne uniforme locale de
la force. Chaque `L_j` est constant sur la fenêtre; un choix dépendant du
temps ajouterait un terme `partial_s Q_(L_j)` absent de (45.1).

Les `Z_j` sont lisses individuellement parce que les temps physiques sont
strictement antérieurs au premier temps singulier. Cette lissité autorise le
test d'énergie, mais ne donne aucune constante uniforme sans l'estimation
ci-dessous.

## Échelle des quantités

Pour l'échelle Navier–Stokes physique

```text
u_lambda(x,t)=lambda u(lambda x,lambda^2t),
p_lambda=lambda^2 p(lambda x,lambda^2t),
f_lambda=lambda^3 f(lambda x,lambda^2t),
```

`K_3(u)` et `K_(3/2)(u tensor u)` sont invariants. Les quantités locales

```text
r^-1 ess sup_t integral_(B_r)|u|^2,
r^-1 integral_(Q_r)|nabla u|^2,
r^-2 integral_(Q_r)|u|^3,
r^-2 integral_(Q_r)|p|^(3/2)                 (45.4)
```

sont également invariantes. L'équation renormalisée (45.1), avec drift
fixé `kappa D`, encode une horloge et n'est pas déclarée invariante sous une
nouvelle dilatation parabolique à `kappa` fixé.

Sur un ensemble spatial de mesure finie `E`, pour `1<=a<3`,

```text
||Z_j(s)||_(L^a(E))
 <=(3/(3-a))^(1/a)|E|^(1/a-1/3) C_Q M.          (45.5)
```

La bornitude des Riesz dans les espaces de Lorentz donne

```text
K_(3/2)(Pi_j(s)) <=C_R C_O (C_QM)^2.           (45.6)
```

En particulier `Z_j` est uniformément dans `L^infinity_s L2_x,loc`, et
`Pi_j` dans `L^infinity_s L^(4/3)_x,loc`. L'endpoint fort `L3` n'est pas
supposé.

## Lemme actif : énergie locale uniforme

Fixons `B_r` compactement incluse dans `B_rho`. On teste (45.1) par
`eta^2 Z_j`, avec `eta=1` sur `B_r`, supportée dans `B_rho`. Le drift ne
perd aucune dérivée car

```text
Z_j dot D Z_j
 =div(y |Z_j|^2/2)-|Z_j|^2/2.                  (45.7)
```

Après intégration sur `[-S,tau]`, les termes de cutoff conduisent à

```text
D_j(r)<=theta D_j(rho)
 +C[1+integral_I ||Z_j||_3^3
      +integral_I ||Pi_j Z_j||_1],             (45.8)
D_j(r)=integral_(I x B_r)|nabla Z_j|^2,
```

où la constante suit `R,S,M,kappa`, les dérivées du cutoff et la borne
locale de `F_j`, mais pas `j` ni `L_j`. Les puissances de `(rho-r)^-1` sont
conservées dans `C`.

La borne locale `L2` issue de (45.5), Gagliardo–Nirenberg et Young donnent,
pour tout `epsilon>0`,

```text
||Z_j||_3^3
 <=epsilon ||nabla Z_j||_2^2+C_(epsilon,R,M),  (45.9)

||Z_j||_4
 <=C ||Z_j||_2^(1/4)
       (||nabla Z_j||_2+R^-1||Z_j||_2)^(3/4), (45.10)

||Pi_j Z_j||_1
 <=||Pi_j||_(4/3)||Z_j||_4
 <=epsilon ||nabla Z_j||_2^2+C_(epsilon,R,M). (45.11)
```

En choisissant les coefficients d'absorption assez petits,

```text
D_j(r)<=theta D_j(rho)+C_(R,S,M,kappa).         (45.12)
```

Le remplissage des trous choisit `theta` plus petit que l'inverse du facteur
géométrique des cutoffs. Le reste `theta^nD_j(4R)` tend vers zéro pour chaque
`j`; sa valeur initiale n'entre pas dans la constante finale. On obtient

```text
sup_j [
  ||Z_j||_(L^infinity(I;L2(B_R)))
 +||nabla Z_j||_(L2(I x B_R)) ]
 <=C_(R,S,M,kappa).                             (45.13)
```

Cette implication est PDE-dépendante. Les contre-profils fonctionnels qui
gardent `K_3` mais font diverger l'enstrophie ne la réfutent pas parce que
leur résidu (45.1) n'est pas petit.

## Simon, produit et pression

Avant même (45.13), l'équation et (45.5)–(45.6) donnent localement

```text
partial_s Z_j borne dans
L^infinity(I;W^(-2,4/3)).                       (45.14)
```

Les triplets compacts utilisés sont exactement

```text
L2 compactement inclus dans H^-1
   continument inclus dans W^(-2,4/3),          (45.15)

H1 compactement inclus dans L2
   continument inclus dans W^(-2,4/3).          (45.16)
```

Le corollaire 4 de Simon fournit, après extraction,

```text
Z_j ->Z dans C(I;H^-1_loc),                     (45.17)
Z_j ->Z fortement dans L2_loc(R3 x I).          (45.18)
```

L'énergie locale implique en outre une borne `L^(10/3)_loc`. L'interpolation
avec (45.18) donne

```text
Z_j ->Z fortement dans L^q_loc pour tout q<10/3,
en particulier dans L3_loc,                    (45.19)

Z_j tensor Z_j ->Z tensor Z
fortement dans L^(3/2)_loc.                    (45.20)
```

Il n'y a donc aucun défaut de Reynolds intérieur.

Pour ne pas localiser faussement la pression non locale, on écrit, avec
`zeta=1` sur le cylindre observé,

```text
Pi_j=R_aR_b(zeta Z_(j,a)Z_(j,b))+h_j.          (45.21)
```

La partie proche converge fortement dans `L^(3/2)_loc` par (45.20). Le reste
`h_j` est harmonique en espace; (45.6) et les estimations intérieures le
bornent dans `L^infinity_s C^m_x` sur les compacts. Après extraction, il
passe faible-étoile contre la vitesse forte. La pression complète n'est pas
déclarée fortement compacte.

Les égalités locales d'énergie des champs lisses passent alors à la limite :
les termes quadratiques et cubiques par (45.18)–(45.20), le flux de pression
par (45.21), la force par (45.3), et la dissipation par semi-continuité
inférieure. La limite vérifie

```text
partial_s |Z|^2/2-Delta |Z|^2/2+|nabla Z|^2
 +div[(|Z|^2/2+Pi)Z]
 +kappa div(y|Z|^2/2)-kappa |Z|^2/2 <=0.       (45.22)
```

Elle est donc une solution faible adaptée locale de l'équation renormalisée
non forcée

```text
partial_s Z-Delta Z+div(Z tensor Z)+nabla Pi
 +kappa D Z=0,
div Z=0.                                       (45.23)
```

Si les fenêtres remontent vers tout `[-S,0]`, `S<infinity`, une diagonale
produit une solution ancienne de (45.23) sur `R3 x (-infinity,0]`. La
dérenormalisation exacte, la mildness globale et la rigidité ne font pas
partie du lemme.

## Porte restante : trace critique non triviale

(45.17) donne seulement

```text
Z_j(0)->Z(0) fortement dans H^-1_loc.           (45.24)
```

Une minoration de `||Z_j(0)||_2`, de `K_3(Z_j(0))`, d'enstrophie ou d'un
superniveau non signé n'est pas stable sous cette convergence. La compacité
forte espace-temps (45.18) ne contrôle pas une tranche de mesure temporelle
nulle.

Une condition minimale suffisante est l'existence d'un observable fixe :

```text
il existe psi dans C_c^infinity(B_R;R3), c_*>0,
tel que |<Z_j(0),psi>|>=c_* pour tout j.         (45.25)
```

Alors (45.24) donne `Z(0) non nul`. Le nouveau verrou est précisément de
déduire (45.25), ou un substitut fortement compact, de la capture Type I du
cycle 0041 sans choisir `psi` après avoir vu `j`.

## Tests adverses reproductibles

### Concentration critique compacte

Pour `A` lisse compact et `V=curl A` non nul, posons

```text
C_n(x)=nV(nx).                                   (45.26)
```

Le certificat exact vérifie

```text
K_3(C_n)=K_3(V),
||C_n||_r=n^(1-3/r)||V||_r,
||nabla C_n||_q=n^(2-3/q)||nabla V||_q,          (45.27)
||C_n||_2^2=n^-1||V||_2^2,
||nabla C_n||_2^2=n||nabla V||_2^2.
```

En écrivant `V=div T`, on a aussi

```text
||C_n||_(W^(-1,q))<=n^(-3/q)||T||_q.            (45.28)
```

La capture faible-`L3` survit tandis que tous les observables fixes et les
normes sous-critiques peuvent disparaître. Le résidu Navier–Stokes a toutefois
une échelle principale `n^3` et ne tend pas dans `C^infinity_loc`; ce profil
réfute le transfert fonctionnel abstrait, pas le lemme PDE.

### Couche terminale forcée

Sur `T3`, avec `W_n=sin(nx_1)e_2`,

```text
Y_n(t,x)=(1+n^2t)_+ W_n(x),  -1<=t<=0,          (45.29)
```

est une solution exacte de Navier–Stokes forcée, de pression nulle et de
non-linéarité nulle. Le certificat donne

```text
||Y_n||_(L2_(t,x))^2=1/(6n^2),
||nabla Y_n||_(L2_(t,x))^2=1/6,
||F_n||_(L2_t H^-1_x)^2=7/6,
sqrt(2)||F_n||_(L1_t H^-1_x)=3/(2n),            (45.30)
||Y_n(0)||_2^2=1/2.
```

La force tend vers zéro dans une topologie négative intégrée tandis que la
trace ne converge pas fortement. Elle ne tend pas dans la topologie forte
`C^infinity_x,loc` uniforme en temps de (45.3), donc ne réfute ni le lemme ni
le problème Clay.

Le script exécute 401 assertions rationnelles exactes, sans discrétisation,
erreur d'arrondi ni graine aléatoire.

## Raccord à la littérature primaire

- Simon fournit le mécanisme abstrait de (45.15)–(45.19), sans donner une
  trace terminale forte `L2`.
- Albritton–Barker (`NS-SRC-0187`) obtient une forte `L3` adaptée sous bornes
  fortes `L3/L^(3/2)` et conserve une singularité avec une hypothèse
  supplémentaire d'explosion persistante; leur autre route emploie une
  normalisation ponctuelle et une compacité höldérienne.
- Barker–Seregin–Šverák (`NS-SRC-0188`) prouve une stabilité faible-étoile
  pour une classe faible-`L3` scindée en flot calorique et correcteur
  énergétique. Cette structure publiée confirme la possibilité d'une
  compacité endpoint, sans fournir la non-trivialité de la limite du cycle.

La veille différentielle 2025–2026 n'a identifié aucun théorème transformant
la seule capture Type I faible-`L3` en un observable fixe non nul à la trace.

## Résultat et pivot

Les sous-gaps

```text
GAP-TYPE-I-LOCAL-DISTRIBUTIONAL-COMPACTNESS
GAP-TYPE-I-LOCAL-SUITABILITY-ENERGY
```

sont fermés au statut interne `COMPUTATION_ONLY` sous les hypothèses exactes
(45.1)–(45.3). Le gap antérieur est remplacé par

```text
GAP-TYPE-I-CRITICAL-TRACE-PERSISTENCE
  : obtenir un moment fixe signé, une trace forte ou une persistance de
    singularité compatible avec la capture Type I;

GAP-TYPE-I-ANCIENT-WEAK-L3-RIGIDITY
  : seulement après dérenormalisation et non-trivialité.
```

La prochaine expérience décisive doit rechercher un mécanisme PDE qui
propage la capture non signée vers (45.25), ou construire une cascade
PDE-compatible qui conserve la capture faible-`L3` tout en annulant chaque
observable fixe.
