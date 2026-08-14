# Cycle 0018 — commutateur localisé et uniformité multi-échelle

Date : 2026-08-14. Lemme actif : `LOCALIZED-LOG-COMMUTATOR-1`.

## Décision adaptative

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total | Décision |
|---|---:|---:|---:|---:|---:|---|
| auditer exactement `(8) -> (22)`, extension BMO et toutes les queues | 5 | 4 | 5 | 5 | **19/20** | sélectionnée |
| synchroniser l'endgame analytique `(49) -> (58)` | 4 | 3 | 5 | 5 | 17/20 | prochaine |
| tester l'admissibilité PDE d'un profil critique multi-échelle | 4 | 3 | 4 | 5 | 16/20 | différée |

Le cycle 0017 avait fermé conditionnellement la chaîne d'énergie
`(23) -> (40)` et identifié (22) comme sa première prémisse non reproduite.
Le cycle présent ne traite qu'un objet : l'estimation statique du commutateur
localisé. L'expérience décisive est la somme annulaire exacte avec tous les
incréments de moyennes de même signe.

## Équation, domaine et type de solution

La prépublication auditée considère Navier–Stokes incompressible 3D non forcé
sur `R³`, sans frontière et avec viscosité `nu>0` :

```text
partial_t u+(u dot nabla)u-nu Delta u+nabla p=0,
div u=0,
boldomega=curl u,
omega=|boldomega|,
xi=boldomega/omega sur {omega>0}.
```

Avant un premier temps singulier possible `T*`, la solution est classique.
Sur `I=(T*−epsilon,T*)`, le théorème 4.1 de la source ajoute une borne
uniforme

```text
M=sup_(t in I)||omega(t)||_(L^(3/2,infinity)(R³))<infinity
```

et une hypothèse uniforme `bmo_phi` sur une extension de la direction, avec
`phi(r)=1/|log r|` dans les unités de la source. Le calcul ne construit ni
solution, ni scénario de blow-up. Il vérifie une implication d'analyse
harmonique, à temps fixé, puis suit l'uniformité si les prémisses le sont.

La vorticité satisfait formellement

```text
(partial_t+u dot nabla-nu Delta)omega <= alpha omega,
alpha=xi dot S xi,
S=(nabla u+nabla u^T)/2.
```

La formule de Biot–Savart fournit une matrice finie `T` d'opérateurs de
Calderón–Zygmund de degré zéro. La cancellation unidirectionnelle donne,
après contraction des indices,

```text
|alpha(x)| <= C_con |[T,xi]omega(x)|.                 (C)
```

Cette passe accepte (C) comme raccord tensoriel explicite; elle ne le confond
pas avec le théorème fonctionnel ci-dessous.

## Veille différentielle

La notice primaire d'`arXiv:2607.08866` consultée le 2026-08-14 indique
toujours la v2, soumise le 9 juillet et révisée le 13 juillet 2026. Elle ne
signale ni v3, ni erratum, ni publication évaluée. Le théorème 4.1 revendique
le gain restreint faible-`L^(3/2)` et attribue son champ proche à Jones,
Coifman–Rochberg–Weiss et Hunt.

Les sources primaires contrôlées ajoutent trois points :

- Jones étend la **semi-norme** BMO d'une boule avec une constante uniforme
  par translation et dilatation;
- Coifman–Rochberg–Weiss borne le commutateur sur chaque `L^p`,
  `1<p<infinity`;
- John–Nirenberg convertit la semi-norme BMO en moments locaux d'ordre deux
  et quatre.

La phrase de la v2 qualifiant `L^(3/2,infinity)` de réflexif est fausse. La
borne faible reste valide par interpolation réelle entre deux bornes fortes,
par exemple `p_0=4/3`, `p_1=2`, `theta=1/3`.

## Normalisation critique

Une écriture dimensionnée commode est

```text
q=R/R_*,
phi_*(R)=1/[1+log(R_*/R)],
0<R<=R_*/64.
```

Elle est comparable au poids `1/|log R|` de la source après fixation des
unités. On suppose

```text
sup_(t,z,0<r<=R_*) mean_(B_r(z)) |xi-xi_(B_r(z))|
  /phi_*(r) <= B_xi,
|xi|<=1,
sup_t ||omega(t)||_(L^(3/2,infinity)) <= M.           (H)
```

Les constantes `M` et `||alpha||_(L^(3/2,infinity))` ont le scaling de la
viscosité; `B_xi`, `q` et `phi_*` sont sans dimension. Le logarithme n'est
jamais appliqué à une longueur nue.

## Lemme minimal réparé

### `LOCALIZED-LOG-COMMUTATOR-1`

Soit `T` une matrice finie d'opérateurs de Calderón–Zygmund de convolution
sur `R³`, dont les noyaux vérifient

```text
|K(x)| <= C_K |x|^-3
```

et les bornes de commutateur de Coifman–Rochberg–Weiss. Sous (H) et (C),
pour tout centre `z`, tout temps de l'intervalle commun et
`0<R<=R_*/64`,

```text
||alpha(t)||_(L^(3/2,infinity)(B_R(z)))
  <= C_* M(B_xi+1) phi_*(R).                         (22q)
```

`C_*` dépend de la dimension, de la matrice `T`, des conventions de Lorentz
et des constantes de Jones, Coifman–Rochberg–Weiss, John–Nirenberg et
Hölder–Lorentz. Elle ne dépend pas de `R`, `z`, `t`, `omega` ou `xi`.

Ce résultat reçoit le statut `COMPUTATION_ONLY` : la dérivation est nouvelle
dans le laboratoire, n'est pas formalisée et les trois passes sont de la même
famille de modèle.

## Preuve à constantes séparées

On écrit

```text
omega_in =omega 1_(B_(2R)(z)),
omega_out=omega 1_(R³\B_(2R)(z)),
c_R=mean_(B_R(z)) xi.
```

La partie lointaine se sépare algébriquement en

```text
[T,xi](omega_out)
 =(c_R-xi)T(omega_out)+T(omega_out(xi-c_R))
 =I_1+I_2.
```

### Champ proche

Sur `B_(2R)(z)`, la semi-norme BMO est au plus
`B_xi phi_*(2R)`. Le théorème de Jones donne une extension `xi_tilde` telle
que

```text
[xi_tilde]_(BMO(R³)) <= C_J B_xi phi_*(2R),
```

avec `C_J` indépendant de `R,z,t`. L'extension n'a pas à rester unitaire ni
bornée; elle ne sert que comme symbole et coïncide avec `xi` sur le support de
`omega_in`. L'invariance `[T,b+c]=[T,b]` montre pourquoi une semi-norme suffit.

Interpolation des bornes fortes du commutateur, puis restriction, donne

```text
||[T,xi](omega_in)||_(L^(3/2,infinity)(B_R))
 <= C_N M B_xi phi_*(R).                             (N)
```

Une extension naïve par zéro ne convient pas : la fonction constante un sur
la boule a semi-norme locale nulle, mais une oscillation `1/2` sur une boule
symétrique traversant le bord de son extension par zéro.

### Réarrangée du noyau tronqué

Pour `h_a(y)=|y|^-3 1_(|y|>a)` et `v_3=|B_1|`, la formule exacte est

```text
h_a^*(s)=1/(a³+s/v_3),
||h_a||_(L^(3,1))
  =(2pi/sqrt(3)) v_3^(1/3) a^-2.                    (K31)
```

La formule `min(a^-3,Cs^-1)` de la v2 est seulement une comparabilité. Elle
donne la bonne puissance mais pas l'identité annoncée.

### Terme `I_1`

Pour `x in B_R(z)` et `y` hors `B_(2R)(z)`, le noyau est séparé de sa
singularité. (K31) donne

```text
|T(omega_out)(x)| <= C M R^-2.
```

John–Nirenberg puis l'inclusion sur un ensemble de mesure finie donnent

```text
||xi-c_R||_(L^(3/2,infinity)(B_R))
 <= C B_xi R² phi_*(R).
```

Donc

```text
||I_1||_(L^(3/2,infinity)(B_R))
 <= C_I1 M B_xi phi_*(R).                            (I1)
```

Les facteurs `R^-2` et `R²` se compensent exactement.

### Queue macroscopique de `I_2`

On coupe à la longueur dimensionnée `ell=sqrt(RR_*)`. Sur la queue
`|y-z|>ell`, `|xi(y)-c_R|<=2`. Hölder–Lorentz et (K31) donnent un majorant
ponctuel `C M ell^-2`. La restriction à `B_R` apporte `R²`, donc

```text
||I_(2,far)||_(L^(3/2,infinity)(B_R))
 <= C_F M R/R_* <= C_F M phi_*(R).                  (F)
```

Un paquet critique à distance `ell` sature l'ordre `M R/R_*`; cette queue
est petite, mais elle n'est pas supprimable.

### Queue intermédiaire de `I_2`

Pour

```text
A_k=B_(2^(k+1)R)(z)\B_(2^kR)(z),
N=floor((1/2)log_2(R_*/R)),
c_k=mean_(B_(2^kR)(z)) xi,
```

le rapport volumique des boules vaut exactement huit et fournit

```text
|c_(k+1)-c_0|
 <=8B_xi sum_(j=1)^(k+1) phi_*(2^jR).               (Moy)
```

John–Nirenberg d'ordre quatre et l'injection locale `L^4 -> L^(3,1)` donnent

```text
||(xi-c_R)1_(A_k)||_(L^(3,1))
 <=C_L B_xi (2^kR)
      sum_(j=1)^(k+1) phi_*(2^jR).                  (L31)
```

Le noyau apporte `(2^kR)^-3`; le `k`-ième anneau est donc majoré par

```text
C M B_xi R^-2 4^-k
  sum_(j=1)^(k+1) phi_*(2^jR).                      (Ak)
```

Pour `T=log_2(R_*/R)>=6`, `j<=floor(T/2)+1` implique

```text
phi_*(2^jR) <=3 phi_*(R).
```

Par conséquent,

```text
sum_(k>=1) 4^-k sum_(j=1)^(k+1) phi_*(2^jR)
 <=3phi_*(R) sum_(k>=1)(k+1)4^-k
 =(7/3)phi_*(R).                                    (S)
```

Le majorant ponctuel est `C M B_xi R^-2 phi_*(R)` et la norme faible de
`1_(B_R)` apporte `R²`. On obtient

```text
||I_(2,mid)||_(L^(3/2,infinity)(B_R))
 <=C_M M B_xi phi_*(R).                             (Mid)
```

La quasi-inégalité triangulaire de la convention faible choisie ajoute au
plus une constante universelle. (N), (I1), (F) et (Mid) donnent (22q).

## Défauts littéraux et portée des réparations

| Passage de la v2 | Verdict | Réparation | Effet sur l'exposant |
|---|---|---|---|
| petite « norme » BMO de l'extension | ambigu/faux si la norme est ancrée | semi-norme modulo constantes et extension de Jones | aucun |
| `L^(3/2,infinity)` « réflexif » | faux | interpolation réelle entre `L^(4/3)` et `L²` | aucun |
| `h_a^*=min(a^-3,Cs^-1)` exactement | faux | `h_a^*(s)=1/(a³+s/v_3)` | aucun |
| `phi(2^jR)<=2phi(R)` jusqu'à `N+1` | faux | facteur trois pour `T>=6`, ou dernier anneau tronqué | aucun |
| somme de quatre quasi-normes avec coefficient un | non justifié | norme équivalente par `f**` ou constante triangulaire | aucun |
| `R^(1/2)` et `log R` | non dimensionnés | `sqrt(RR_*)` et `log(R_*/R)` | aucun |

Le claim `NS-DYADIC-PHI-FACTOR-TWO` reste `REFUTED`; le nouveau calcul ajoute
le résidu général et la réparation uniforme. Le claim séparé
`NS-TRUNCATED-KERNEL-MIN-REARRANGEMENT` enregistre l'identité fausse, sans
transformer une correction locale en réfutation du théorème 4.1.

## Expérience décisive

Artefact : `COMMUTATOR-UNIFORMITY-AUDIT-1`.

Question falsifiable : une dérive maximale, avec tous les incréments de
moyennes positifs, peut-elle faire croître la somme intermédiaire plus vite
que `phi(R)` ?

Le script utilise uniquement `fractions.Fraction`. Il n'a ni grille PDE, ni
pas de temps, ni donnée aléatoire. Les balayages finis sont accompagnés des
inégalités analytiques valables à toutes les échelles.

Résultats :

- le facteur deux est réfuté par le ratio exact `8/3`;
- le facteur trois est uniforme pour `T>=6`;
- `sum_(k>=1)(k+1)4^-k=7/9`;
- la somme adverse exacte sur `T=6,...,512` a pour maximum `697/640`, avec
  une marge `2389/1920` sous le majorant sûr `7/3`;
- sans `4^-k`, le rapport dérive/`phi(R)` est au moins
  `floor(T/2)+1` et diverge;
- l'interpolation faible, la porte d'extension BMO et le ledger de scaling
  passent.

Commande :

```text
python -B experiments/navier-stokes/commutator-uniformity/commutator_uniformity_audit.py
```

Empreinte du script :
`387898492a0dc370d6ca50aadbc18e7e524ebdc0d7326fe2347952cbce57ebbf`.

Le calcul certifie huit identités ou enveloppes rationnelles, zéro résidu en
échec. Il ne certifie pas les théorèmes de Jones, CRW ou John–Nirenberg, le
raccord tensoriel (C), ni l'existence d'une solution Navier–Stokes portant
les hypothèses.

## Passe contradictoire

Trois passes séparées ont été exécutées : analyse fonctionnelle et constantes,
audit bibliographique, puis contre-profil annulaire/log-log. Elles restent de
la même famille de modèle et ne sont pas indépendantes au sens externe.

Le contre-profil prend une amplitude critique `M r_j^-2` sur chaque anneau
`r_j=2^jR` et une variation directionnelle `phi_*(r_j)` par échelle. Sa norme
faible-`L^(3/2)` reste uniforme. La dérive des moyennes jusqu'à
`sqrt(RR_*)` peut être d'ordre un, ce qui réfute toute simplification

```text
|c_k-c_0| <= C phi_*(R) uniformément en k.
```

Mais le noyau fournit précisément `4^-k`; la somme pondérée reste
`O(phi_*(R))`. Aucun contre-exemple au lemme réparé n'est produit.

Ce profil est un test de l'enveloppe fonctionnelle : il ne construit pas une
vorticité divergence-free issue d'une solution NS. Des secteurs coniques
permettent de garder un signe de composante de noyau et montrent que les
majorations absolues ont les bonnes puissances.

## Échelle

Sous

```text
u_kappa(x,t)=kappa u(kappa x,kappa²t),
omega_kappa(x,t)=kappa² omega(kappa x,kappa²t),
alpha_kappa(x,t)=kappa² alpha(kappa x,kappa²t),
R_kappa=R/kappa,
R_(star,kappa)=R_*/kappa,
```

les normes `L^(3/2,infinity)` de `omega` et `alpha` sont invariantes. Le
rapport `R/R_*`, le poids `phi_*` et la semi-norme pondérée sont invariants.
Sur un anneau,

```text
r^-3 (noyau) × r^-2 (amplitude) × r³ (volume) = r^-2,
```

puis la restriction à `B_R` apporte `R²`. Aucun exposant spatial n'est perdu.

## Écart avec le problème Clay

Le maillon `(8) -> (22)` survit après corrections, mais uniquement sous une
hypothèse géométrique globale et uniforme sur l'extension de la direction.
Il ne prouve pas que cette hypothèse :

- est satisfaite par toute donnée de Schwartz Clay;
- est propagée jusqu'au temps maximal;
- peut être formulée seulement sur `{omega>lambda}` puis étendue avec la même
  constante;
- coexiste avec tous les zéros de vorticité et plusieurs cœurs de
  concentration;
- donne une conclusion analogue sur le tore, où l'opérateur et les queues
  doivent être recalculés.

Le résultat n'est donc ni un nouveau critère inconditionnel, ni une exclusion
de blow-up. Il ferme une arête fonctionnelle conditionnelle dans une chaîne
beaucoup plus longue.

## Décision

`GAP-COMMUTATOR-UNIFORMITY` est fermé **conditionnellement** au raccord
tensoriel (C), aux théorèmes classiques cités et à l'hypothèse globale (H).
Les erreurs littérales de la v2 sont locales et réparables. Le premier verrou
en aval devient `GAP-ENDGAME-SYNCHRONIZATION` : vérifier `(49) -> (58)` avec
un temps d'échappement, un rayon d'analyticité, un rayon de sparseness et des
constantes tous quantifiés sur le même temps et dans le bon sens.

La prochaine expérience décisive sera un solveur exact d'inégalités pour les
équations (49)–(58), incluant les deux branches du critère harmonique et un
contre-test où les constantes asymptotiques ne deviennent petites qu'après le
temps admissible.

## Sources et revues

- Z. Grujić, `arXiv:2607.08866v2`, théorème 4.1 et équations (8)–(22).
- R. R. Coifman, R. Rochberg et G. Weiss, *Annals of Mathematics* 103
  (1976), 611–635, DOI `10.2307/1970954`.
- P. W. Jones, *Indiana University Mathematics Journal* 29 (1980), 41–66,
  DOI `10.1512/iumj.1980.29.29005`.
- F. John et L. Nirenberg, *Communications on Pure and Applied Mathematics*
  14 (1961), 415–426, DOI `10.1002/cpa.3160140317`.
- R. A. Hunt, *L'Enseignement Mathématique* 12 (1966), 249–276.
- `reviews/cycle-0018-analysis.md` : recalcul des constantes.
- `reviews/cycle-0018-literature.md` : provenance et conventions BMO.
- `reviews/cycle-0018-countermodel.md` : contre-profil multi-échelle.
