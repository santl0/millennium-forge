# Expériences Navier–Stokes

Les expériences de ce répertoire sont des tests analytiques finis. Elles ne
simulent pas une solution Navier–Stokes et ne constituent ni une preuve de
régularité ni un blow-up. Toutes utilisent la graine « sans objet » et écrivent
leur rapport JSON sur la sortie standard.

## Matrice de reproduction

| ID | Question falsifiable | Arithmétique / discrétisation | Commande | Erreur certifiée |
|---|---|---|---|---|
| `VAS-1` | quand la viscosité est-elle perturbative dans un ansatz mono-échelle ? | rationnels exacts; aucune grille | `python -B experiments/navier-stokes/viscosity-gate/test_viscosity_gate.py` | zéro pour les identités testées |
| `TRI-PHASE-1` | divergence nulle et hélicité nulle imposent-elles un flux sous-linéaire universel ? | modes Fourier finis, rationnels gaussiens exacts | `python -B experiments/navier-stokes/triad-phase/test_triad_phase.py` | zéro |
| `DESINGULARIZATION-GATE-1` | les normes d'une troncature de `r^-1` restent-elles uniformes quand `epsilon -> 0` ? | intégrales radiales exactes; logarithme symbolique | `python -B experiments/navier-stokes/desingularization-gate/desingularization_gate.py` | zéro pour les identités rationnelles |
| `PRESSURE-TAIL-1` | centrer la pression d'un paquet distant gagne-t-il une puissance de distance ? | noyau multipolaire exact, tenseur ponctuel | `python -B experiments/navier-stokes/pressure-tail/pressure_tail.py` | zéro |
| `PRESSURE-MULTISCALE-1` | une borne physique `L²` seule impose-t-elle la tension uniforme de la pression après zoom ? | lois d'échelle et moments exacts | `python -B experiments/navier-stokes/pressure-multiscale/pressure_multiscale.py` | zéro |

Environnement reproduit au checkpoint initial : Windows, Python 3.13.14,
bibliothèque standard uniquement. Les scripts ne lisent aucun fichier, n'ont
aucune dépendance réseau et ne produisent pas d'artefact lourd.

## `VAS-1` — seuil visqueux

- Équations testées : exposants de `partial_t u`, `(u dot nabla)u`, `nabla p`
  et `nu Delta u` pour
  `u=tau^lambda U(x/tau^(1+lambda))`.
- Entrées : intervalles rationnels documentaires pour deux profils inviscides,
  seuil NS `lambda=-1/2` et contrôle adverse `lambda=-3/4`. Les valeurs CCF et
  IPM proviennent respectivement de `arXiv:2509.14185` et
  `arXiv:2511.22819`; elles sont diagnostiques et ne sont pas nécessaires au
  claim de seuil.
- Résidu : six identités d'exposants exactement nulles.
- Sensibilité : le signe change exactement en `lambda=-1/2`.
- Limite : ne teste ni l'existence de `U`, ni ses queues, ni une construction
  NS multi-échelle.
- Provenance : import byte-for-byte du script historique, SHA-256
  `201cc2e97cb6ec35618019512fc6e9225459034e1bd6c65ac67165e5be08fb0a`.

## `TRI-PHASE-1` — triade signée

- Équation testée : terme non linéaire projeté de NS/Euler incompressible sur
  le tore normalisé, sur six modes Fourier explicites.
- Données : `a=(N,0,0)`, `b=(0,N,0)`, `c=(N,N,0)`, modes opposés conjugués et
  phase `sigma=+-1`; `N` parcourt `1,2,4,8,16,32,64`.
- Préservation : divergence, réalité, travail de pression et bilan d'énergie
  sont vérifiés exactement.
- Sortie décisive : `E=6`, hélicité modale et totale nulle,
  `|Pi_N|=2N`, somme absolue `4N`, ratio normalisé au carré `1/54`.
- Définitions :
  `E=(1/2)sum_k |u_hat(k)|²`,
  `Q_k=-i P_k sum_(p+q=k)(q dot u_hat(p))u_hat(q)` et
  `Pi_N=-sum_(0<|k|<=N) Re(conj(u_hat(k)) dot Q_k)`, avec coupure
  euclidienne et `N` entier positif.
- Certificat pour tout `N` : le calcul symbolique donne
  `T_(+-a)=0`, `T_(+-b)=sigma N`, `T_(+-c)=-sigma N`. Les modes `a,b`
  sont sous la coupure et `c` au-dessus, d'où `Pi_N=-2 sigma N`; la
  dépendance en `N` est algébrique, pas extrapolée des sept cas exécutés.
- Résidu et précision : nombres rationnels gaussiens, résidu exact zéro.
- Sensibilité : changer la phase inverse le sens du flux sans changer les
  invariants quadratiques.
- Limite : champ instantané, pas trajectoire NS; aucune conclusion sur une
  hypothèse géométrique locale plus forte.
- Provenance : dérivé du script historique SHA-256
  `a02b6959a5c00dbb248864ccd43ba55336769869d83bc73fd21d05ad4419e493`;
  suppression d'un helper inutilisé et renommage anglais. Empreinte Forge :
  `c469d9a9984753c95fa0f21cd8fbeb723bd6ed1f8c6a500376af02d13ce5da33`.

## `DESINGULARIZATION-GATE-1` — premier cycle autonome

- Question : la contribution de coquille d'un champ homogène
  `u_0(r,theta)=r^-1 A(theta)`, conservé sur `epsilon<=r<=1`, reste-t-elle
  uniforme dans plusieurs normes usuelles quand `epsilon` tend vers zéro ?
- Donnée : `0<epsilon<1`, profil angulaire fixe avec
  `0<C_q=integral_S2 |A|^q<infinity`; pour le gradient,
  `A in H^1(S2)` et
  `C_grad=integral_S2 (|A|²+|grad_S A|²)>0`. Le test ne reconstruit pas le
  profil précis de Hou–Wang–Yang.
- Résolution : `epsilon=10^-k`, `k=1,2,4,8,16`; aucune discrétisation spatiale
  ou temporelle.
- Résultat : `L^q`, `q<3`, reste borné; `||u||_3^3` croît comme
  `log(1/epsilon)`; pour `q>3`,
  `||u||_q~epsilon^(3/q-1)`; et
  `||grad u||_2~epsilon^-1/2`.
- Résidu : identités rationnelles zéro; `log(10)` est laissé symbolique.
- Analyse d'erreur : aucune erreur d'arrondi; les constantes angulaires sont
  explicitement hors calcul et doivent être non nulles pour conclure dans le
  canal correspondant.
- Limite : pour une troncature globale, le calcul n'est qu'une borne inférieure
  de coquille et n'estime pas les couches de raccord. Il ne teste ni divergence,
  ni PDE, ni temps d'existence. Des solutions de cisaillement lisses peuvent
  avoir ces normes grandes tout en étant globales; les divergences interdisent
  seulement de supposer gratuitement leur uniformité.

## Passage au continuum

Aucune des cinq expériences ne part d'une discrétisation PDE : il n'y a donc
pas de passage grille-vers-continuum. Le raccord analytique restant est
explicite dans chaque cas. Tout futur solveur doit ajouter divergence mesurée,
convergence multi-résolution, second schéma, bornes de troncature, contrôle des
frontières, énergie/enstrophie/normes critiques, versions logicielles et
empreintes des sorties.

## `PRESSURE-TAIL-1` — pression distante et jauge

- Objet : noyau de pression sur `R^3`,
  `K_ij(z)=(3z_i z_j-|z|² delta_ij)/(4 pi |z|^5)`.
- Lemme analytique testé : pour un paquet divergence-free `v` supporté dans
  `B_rho(R e_1)`, `R>a+rho`, et `x in B_a(0)`, le théorème des accroissements
  finis donne

  ```text
  |p_v(x)-p_v(0)|
    <= (21/pi) a (R-a-rho)^(-4) ||v||_2².
  ```

  En effet, la dérivée directionnelle de chaque `K_ij` est au plus
  `7/pi |z|^-4`, et
  `sum_(i,j)|v_i v_j| <= 3|v|²`.
- Jauge : pour tout champ test compact divergence-free `w` et cutoff `phi`,
  `integral p_v(0) w dot grad(phi)=0`. La constante distante d'ordre `R^-3`
  ne travaille donc pas dans l'énergie locale; la variation active gagne une
  puissance `R^-4`.
- Expérience : moment principal `M=diag(1,1,0)` à distance `R`; après
  normalisation par `4 pi`, `p_R(0)=R^-3` et
  `p_R(e_1)-p_R(0)=(R-1)^-3-R^-3`. Le résidu de l'identité rationnelle est
  exactement zéro et `R^4` fois la différence tend vers `3`.
- Réalisabilité : `M` est le moment d'un paquet lisse compact divergence-free
  `v=(partial_2 psi,-partial_1 psi,0)` avec `psi` radial dans les deux premières
  variables et pair dans la troisième, après normalisation.
- Sensibilité : distances `R=2,4,...,128`; aucun flottant, graine ou pas de
  temps.
- Limite décisive : la borne contient l'énergie globale du paquet. Sous un zoom
  de blow-up, cette constante n'est pas automatiquement uniforme, et une somme
  de paquets proches de l'échelle active relève du terme de pression proche,
  non de cette queue. Le résultat ne ferme donc pas compacité–rigidité.
- Covariance : sous `v_lambda(x)=lambda v(lambda x)`, la géométrie devient
  `(a,rho,R)/lambda`, tandis que
  `||v_lambda||_2²=lambda^-1||v||_2²`; le membre droit acquiert exactement
  `lambda²`, comme `p_lambda`. Le lemme ne crée donc aucun gain d'échelle caché.

## `PRESSURE-MULTISCALE-1` — défaut de tension après zoom

### Lemme positif borné

Pour une famille `U_n`, définissons directement la différence distante, sans
supposer l'existence séparée des deux pressions brutes,

```text
D_n^far(x;A)=integral_(|y|>A)
  [K_ij(x-y)-K_ij(-y)] U_(n,i)(y)U_(n,j)(y) dy.
```

Pour `|y|>A>2a`, la même borne directionnelle du noyau donne

```text
sup_(|x|<=a) |D_n^far(x;A)|
 <= (21/pi) a (1-a/A)^(-4)
    integral_(|y|>A) |U_n(y)|² |y|^(-4) dy.
```

La condition de tension pondérée

```text
lim_(A->infinity) sup_n
  integral_(|y|>A) |U_n(y)|² |y|^(-4) dy = 0
```

suffit donc à rendre la pression distante centrée uniformément petite sur les
boules fixes. Ce lemme ne contrôle pas la pression proche.

Une borne critique `L³` implique cette tension par Hölder :

```text
integral_(|y|>A)|U(y)|²|y|^-4dy
 <= ||U||_3² (integral_(|y|>A)|y|^-12dy)^(1/3)
 = (4pi/9)^(1/3) A^-3 ||U||_3².
```

Par conséquent, si `sup_n||U_n||_3<=M`, le supremum des queues est au plus
`(4pi/9)^(1/3)A^-3M²` et tend vers zéro avec `A`.

Ainsi, dans une chaîne de compacité qui suppose déjà
`sup_n ||U_n||_3<infinity`, la pression lointaine centrée n'est pas le verrou.
Cette observation ne produit évidemment pas la borne `L³` depuis l'énergie.

### Famille adverse lisse

Fixons `0<kappa<1/4` et un champ

```text
w=(partial_2 psi,-partial_1 psi,0) in C_c^infinity(B_kappa)
```

où `psi` est radial, puis normalisons-le pour que

```text
integral w_i w_j = diag(1,1,0)_ij,
||w||_2²=2.
```

Pour `n>=1`, posons

```text
L_n=2^(-6n),  r_n=2^(-7n),  mu_n=2^(-3n),
v_n(x)=sqrt(mu_n/r_n³) w((x-L_n e_1)/r_n).
```

Chaque `v_n` est lisse, compact, divergence-free et
`||v_n||_2²=2mu_n->0`. Après le zoom NS
`U_n(y)=r_n v_n(r_n y)`, le paquet est centré en

```text
R_n=L_n/r_n=2^n,
```

et son moment vaut `mu_n/r_n=R_n^4`. Par convergence uniforme sur le support
fixe de `w`,

```text
integral |U_n(y)|² |y|^-4 dy -> 2,
P_n(e_1)-P_n(0) -> 3/(4 pi).
```

Le passage multipolaire se lit directement, uniformément pour
`|z|<=kappa` :

```text
R^4 [K(e_1-R e_1-z)-K(-R e_1-z)]
 = R [K(-e_1+(e_1-z)/R)-K(-e_1-z/R)]
 -> partial_1 K(-e_1).
```

La contraction de `partial_1 K(-e_1)` avec `diag(1,1,0)` vaut
`3/(4pi)`. De même,
`R^4/|R e_1+z|^4->1` uniformément, ce qui donne la limite pondérée `2`.

La pression brute `P_n(0)` diverge comme `R_n/(4 pi)`, mais c'est sa constante
de jauge; la différence centrée reste finie et non nulle. Ainsi l'énergie
cinétique physique `mu_n`, et même `||v_n||_2²=2mu_n`, tendent vers zéro sans
imposer la tension pondérée après un zoom arbitrairement plus fin que le paquet.

### Certificat et limites

- Le script vérifie exactement
  `R_n=2^n`, `mu_n/r_n=R_n^4`,
  `mu_n r_n³/L_n^4=1`, la queue ponctuelle pondérée `2`, et
  `4 pi (P_n(e_1)-P_n(0))->3`.
- Empreinte du script :
  `c69d3c45b5383596cb3ccc1b804ad94ef3ccbfa9b5d49c7e7f237c72abbe12fd`.
- Arithmétique : fractions exactes, aucune discrétisation, résidus nuls, graine
  sans objet.
- La limite du paquet lisse repose sur un développement multipolaire uniforme
  sur un support compact; le script ne formalise pas cette étape.
- Les `v_n` sont des données initiales admissibles prises séparément, pas des
  tranches d'une même solution NS ni un scénario de blow-up.
- Le résultat réfute seulement une déduction depuis l'énergie globale. Une
  borne critique, une tension pondérée ajoutée ou la dynamique peuvent exclure
  cette famille.
