# Cycle 0021 — admissibilité d'un profil critique ponctuel

Date de gel : 2026-08-14.

Statut : dérivation interne falsifiable, profil explicite, certificat exact et
trois passes contradictoires par la même famille de modèles. Aucun résultat
n'est une preuve de régularité globale ou de blow-up.

## Décision du cycle

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| rigidité d'une direction récurrente par dilatation sous log-BMO | 5 | 5 | 5 | 5 | **20** |
| filtre solénoïdal et défaut exact des coupures radiales | 4 | 5 | 5 | 4 | 18 |
| profil presque homogène rectifié à vitesse logarithmique | 5 | 2 | 4 | 5 | 16 |

Le verrou sélectionné est `GAP-CRITICAL-PROFILE-ADMISSIBILITY`. Le lemme
actif exclut la classe vectorielle exactement récurrente par dilatation. Le
test décisif construit un profil divergence-free dont la magnitude est
exactement `r^-2` et mesure la raison précise pour laquelle sa direction
échoue dans `bmo_phi`.

## Équation et type de solution

Le cadre Clay pertinent est Navier–Stokes incompressible, visqueux, non forcé,
sur `R³`, sans frontière :

```text
partial_t u+(u dot nabla)u=-nabla p+nu Delta u,
div u=0,                 omega_vec=curl u,                 nu>0.
```

La prépublication auditée considère une solution pré-singulière
classique/spatialement analytique sur `(0,T*)`. Le profil de ce cycle est un
champ distributionnel statique sur `R³`, singulier en `0`; il ne résout pas
l'équation d'évolution. Ses doubles coupures produisent des données
`C_c^infinity` divergence-free, donc Clay-admissibles et génératrices de
solutions classiques locales distinctes.

Pour chaque donnée coupée, la pression initiale est la pression globale de
Leray

```text
p=(-Delta)^(-1) partial_i partial_j(u_i u_j),
```

et non une pression locale choisie dans le cœur. Aucun résidu stationnaire nul
n'est attribué à ces champs.

## Définition primaire auditée

La Definition 2.1 de `arXiv:2607.08866v2` porte sur la magnitude scalaire
`omega=|omega_vec|` et écrit

```text
omega(x,t)=Phi(x,t)|x|^-2.
```

Elle décrit `Phi` comme scale-invariant ou log-périodique au cœur, annonce une
borne uniforme et `|nabla Phi|` d'ordre au plus `|x|^-1`, puis affirme que les
grands superniveaux sont contenus dans une boule de rayon
`C lambda^-1/2`. Les théorèmes ajoutent séparément

```text
omega in L^infinity_t L^(3/2,infinity)_x,
xi=omega_vec/|omega_vec| in L^infinity_t bmo_(1/|log r|)_x.
```

Au 2026-08-14, la notice primaire reste à la v2 du 13 juillet 2026, sans
référence de revue ni erratum. La v2 remplace le `sim` du gradient de la v1
par un majorant, mais ne fixe toujours pas : rayon de cœur, constante de la
loi `O(r^-2)`, seuil uniforme, centre mobile ou fixe, égalité avant `T*` ou
profil limite remis à l'échelle, ni topologie de convergence.

Deux lectures échouent différemment :

- une simple majoration `O(r^-2)` inclut toute vorticité bornée près de zéro;
- une égalité non dégénérée jusqu'au centre est déjà singulière à chaque
  `t<T*`, contrairement à l'analyticité pré-singulière, sauf à introduire une
  échelle de cœur ou une limite rescalée.

Ce défaut de quantification impose `RÉVISER`; il ne réfute pas à lui seul un
théorème conditionnel reformulé avec des quantificateurs complets.

## Porte solénoïdale sphérique

Soit

```text
W(x)=r^-2 Omega(theta),       r=|x|,       theta=x/r,
Omega=Omega_r theta+Omega_T.
```

Sur `R³\{0}`,

```text
div W=r^-3 div_(S²) Omega_T.                              (1)
```

Si le premier terme s'annule, la divergence sur tout `R³` vaut

```text
div W=[integral_(S²) Omega_r dS] delta_0.                 (2)
```

Ainsi un profil vectoriel homogène est une vorticité distributionnellement
admissible si et seulement si

```text
div_(S²) Omega_T=0,
integral_(S²) Omega_r dS=0.                               (3)
```

Ces contraintes couplent magnitude et direction. Le champ `e/r²` a une
direction constante mais échoue déjà dans `R³\{0}`. Le champ `theta/r²` est
solénoïdal hors de l'origine mais porte le monopôle `4pi delta_0`.

Sous (3), Biot–Savart converge absolument pour `x!=0`, produit une vitesse
homogène de degré `-1` et donne le majorant suivi

```text
|u(x)| <= (pi²/4) ||Omega||_infinity / |x|,               (4)
```

issu de

```text
integral_R3 |y|^-2 |x-y|^-2 dy=pi³/|x|.
```

## Lemme actif : rigidité sous récurrence de dilatation

Soient `0<q<1`, `1<=p<infinity` et un poids positif `phi(r)->0` quand
`r->0`. Supposons qu'un champ vectoriel `W` vérifie :

1. `W in L^1_loc(R³)` et `W in L^(p,infinity)(R³)`;
2. `div W=0` dans les distributions;
3. `|W|>0` presque partout;
4. `W(qx)=q^-2 W(x)` presque partout;
5. `xi=W/|W|` a une semi-norme `bmo_phi` finie sur toutes les petites boules.

Alors aucun tel champ non nul n'existe.

### Preuve

La direction est récurrente : `xi(qx)=xi(x)`. Pour toute petite boule centrée
`B_r`, changement de variable et récurrence donnent

```text
MO_(B_(q^n r))(xi)=MO_(B_r)(xi).                          (5)
```

La borne `bmo_phi` donne simultanément

```text
MO_(B_(q^n r))(xi)<=K phi(q^n r)->0.                      (6)
```

L'oscillation de `B_r` est donc nulle. La direction est constante presque
partout sur cette boule, puis sur `R³` par récurrence : `xi=e`.

Écrivons `W=m e`, avec `m=|W|>=0`. La contrainte `div W=0` devient
`partial_e m=0`. Après rotation, `m(x_perp,z)=g(x_perp)` presque partout. Si
`g` n'est pas nul, il existe `tau>0` et un ensemble transverse `E` de mesure
positive tel que `g>tau` sur `E`. Or

```text
{m>tau} contains E times (-L,L)
```

pour tout `L`, donc ce superniveau a une mesure infinie, en contradiction avec
`m in L^(p,infinity)(R³)`. Ainsi `m=0`, contradiction.

Le même argument couvre l'homogénéité continue et la périodicité logarithmique
**du champ vectoriel ou de sa direction**. Il ne couvre pas une magnitude
scalaire log-périodique accompagnée d'une direction non récurrente, ni un
profil seulement asymptotique.

## Profil adverse exact à magnitude constante

Fixons un vecteur unitaire `a` et posons

```text
u(x)=(1/2)[a/r+(a dot x)x/r³+a cross x/r²],
W(x)=a cross x/r³+(a dot x)x/r⁴.
```

Les identités exactes sont

```text
div u=0,
curl u=W,
div W=0,
W=r^-2[a cross theta+(a dot theta)theta].                 (7)
```

Les parties tangentielle et radiale de l'expression entre crochets sont
orthogonales et leurs carrés somment à un. Par conséquent

```text
|W(x)|=r^-2,              Phi=1,                          (8)
measure{|W|>lambda}=|B_1| lambda^-3/2.                   (9)
```

Ce champ satisfait exactement le gabarit scalaire le plus simple, la
criticalité faible-`L^(3/2)`, la divergence et la reconstruction div–curl.

Sa direction unitaire est

```text
xi(theta)=a cross theta+(a dot theta)theta.
```

Sa moyenne sur toute boule centrée vaut `a/3`. L'inégalité triangulaire
inverse donne point par point

```text
|xi-a/3|>=2/3,
MO_(B_r)(xi)>=2/3                                           (10)
```

pour tout `r`. Le calcul intégral indépendant donne même la valeur exacte

```text
c_xi=(1/3)[1+(5/sqrt(6)) asin(sqrt(3/5))].                (11)
```

Aux rayons `r_n=exp(-n)`, la norme de la v2 coûte au moins `2n/3`; la
direction n'est pas dans `bmo_(1/|log r|)`.

L'énergie locale est finie :

```text
integral_(epsilon<r<R)|u|² dx=(8pi/3)(R-epsilon),         (12)
```

mais l'énergie globale diverge à l'infini. La norme forte critique `L³` de la
vitesse diverge logarithmiquement aux coupures, tandis que sa norme faible
`L³` reste à l'échelle critique.

## Coupures, projection et constante de troncature

Une multiplication radiale naïve de `W` donne

```text
div(chi W)=chi'(r)r^-2 Omega_r(theta),                    (13)
||div(chi W)||_1=Var(chi)||Omega_r||_(L¹(S²)).            (14)
```

Le défaut est indépendant de l'échelle. Une double coupure monotone coûte
deux fois cette constante. Si le flux moyen est nul, la résolution

```text
Delta_(S²) psi=Omega_r,       V=nabla_(S²)psi
```

fournit le correcteur exact

```text
W^chi=chi W-[chi'(r)/r]V,
div W^chi=0,
||V||_2<=(1/sqrt(2))||Omega_r||_2.                        (15)
```

Le facteur `1/sqrt(2)` est optimal sur les harmoniques sphériques de degré
un. Le correcteur est de même taille critique et ne disparaît pas quand la
coupure se resserre.

Pour le profil explicite, une autre construction préserve directement la
divergence de la vitesse. Comme `u` est homogène de degré `-1` et divergence-
free,

```text
A=-x cross u,             curl A=u.
```

Avec une double coupure radiale lisse `chi_(epsilon,R)`,

```text
u_(epsilon,R)=curl(chi_(epsilon,R) A)
```

est dans `C_c^infinity`, divergence-free et coïncide avec `u` dans l'anneau
où `chi=1`. Si `C_k=||chi^(k)||_infinity` désigne les constantes de la coupure
fixe, les termes de la coquille intérieure ont les tailles

```text
|u_(epsilon,R)|<=C(C_1)epsilon^-1,
|curl u_(epsilon,R)|<=C(C_1,C_2)epsilon^-2,
energy_shell<=C(C_1)epsilon,
||curl u_(epsilon,R)||_(L^(3/2,infinity),shell)<=C(C_1,C_2).  (16)
```

Les constantes sont indépendantes de `epsilon`, mais pas de la coupure de
référence. Sur les boules `r_n=2^-n`, avec
`epsilon_n=2^-2n`, la fraction modifiée est au plus `8*2^-3n`. La stabilité
élémentaire

```text
|MO(f)-MO(g)|<=2 average|f-g|<=4 delta
```

montre que toute extension bornée de la direction coupée conserve une
oscillation d'ordre un; sa constante `bmo_phi` diverge au moins linéairement
en `n`.

Enfin, le commutateur visqueux `[Delta,chi]W` est d'ordre
`epsilon^-4`, exactement comme `Delta W`. Recalculer la vitesse par
Biot–Savart ou projection de Leray modifie le champ non localement. Le
majorant standard de pression

```text
||p_epsilon||_(L^(3/2))
 <=C_Riesz ||u_epsilon||_L3²
```

perd au moins la possibilité d'une constante uniforme puisque
`||u_epsilon||_L3³` croît comme `log(R/epsilon)`. Cette borne divergente n'est
pas une minoration de la pression : des annulations supplémentaires restent
possibles et doivent être calculées séparément.

## Passe contradictoire

1. **Magnitude contre champ vectoriel.** La Definition 2.1 ne contient pas
   les deux conditions sphériques (3).
2. **Divergence ponctuée contre globale.** `theta/r²` cache un monopôle
   `4pi delta_0`.
3. **Exactement homogène contre auto-similaire dynamique.** Le lemme porte sur
   la récurrence spatiale à un temps fixé; il n'exclut pas un profil de Leray
   général dépendant de la variable de similarité.
4. **Magnitude log-périodique contre direction log-périodique.** La première
   n'implique pas la seconde; l'exclusion ne peut être étendue sans cette
   hypothèse.
5. **Énergie locale contre Clay.** `u~r^-1` est localement énergétique mais
   pas globalement `L²` sans coupure extérieure.
6. **Coupure solénoïdale contre résidu PDE.** La correction de divergence ne
   contrôle ni diffusion, ni transport, ni étirement, ni pression.
7. **Suite de données contre trajectoire.** Les `u_(epsilon,R)` sont des
   données Clay distinctes; aucune évolution unique ne les visite.
8. **Borne de pression.** La constante standard dépend logarithmiquement de
   la coupure; aucune convergence du tenseur ou de la pression n'est obtenue.

## Verdict et écart avec Clay

Résultat positif : la porte cinématique (3), Biot–Savart et les constantes de
coupure sont explicites.

Résultat négatif : la classe des profils vectoriels non nuls, sans zéro
angulaire et exactement récurrents par dilatation est incompatible avec la
direction globale log-BMO et la criticalité Lorentz solénoïdale. Le profil
explicite montre que la condition qui casse peut être exactement `bmo_phi`,
alors que magnitude, divergence et Biot–Savart sont satisfaits.

Ce résultat exclut une sous-classe substantielle mais étroite. Il ne traite
pas les directions non récurrentes se rectifiant comme `1/|log r|`, les cœurs
mobiles ou multiples, les profils asymptotiques, Type II ou multi-échelles.
Il ne construit ni n'exclut un blow-up Clay général.

`GAP-CRITICAL-PROFILE-ADMISSIBILITY` est fermé négativement pour
l'homogénéité vectorielle exacte. Le verrou suivant est
`GAP-LOG-RECTIFIED-PROFILE` : déterminer si une direction

```text
xi(r,theta)=e+O(1/|log r|)
```

peut satisfaire simultanément `div(|x|^-2 Phi xi)=0`, conserver une masse
faible-`L^(3/2)` non dégénérée, admettre une vitesse énergétique après coupure
et avoir un résidu Navier–Stokes plus petit que les termes principaux.

## Reproduction

```text
python -B experiments/navier-stokes/critical-profile-admissibility/critical_profile_admissibility_audit.py
```

Le script utilise la bibliothèque standard, des fractions exactes et une
différentiation automatique rationnelle sur 25 points stéréographiques. Il
exécute seize contrôles, sans discrétisation PDE ni aléa. Empreinte SHA-256 :
`95bbb128522b9c90437c05903ab86dd4f7cfc42f687218993ee9324ece5a0f85`.

