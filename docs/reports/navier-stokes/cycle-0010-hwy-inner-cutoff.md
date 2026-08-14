# Cycle 0010 — Porte critique de régularisation intérieure Hou–Wang–Yang

Date de gel : 2026-08-14.

## Décision du cycle

La veille différentielle n'a trouvé ni version postérieure à
`arXiv:2509.25116v2` (19 mars 2026), ni publication évaluée. Trois actions ont
été notées sur 5 :

| Action | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| séparer exactement le cutoff extérieur HWY d'un cutoff intérieur Clay et tester la topologie critique | 5 | 5 | 5 | 5 | **20** |
| projeter l'erreur intérieure sur le mode adjoint instable certifié | 5 | 2 | 3 | 5 | 15 |
| reproduire un sous-calcul CAP léger et auditer l'environnement | 3 | 3 | 5 | 3 | 14 |

Le premier est sélectionné. Lemme actif unique : une régularisation qui enlève
le coeur `r^-1` peut être petite en énergie, mais ne l'est pas dans `L^3` ni
dans `L^{3,infinity}`. Expérience active unique :
`HWY-INNER-CUTOFF-GATE-1`.

## Équation et type de solution

La source traite

```text
partial_t u + (u dot nabla)u - Delta u + nabla p = 0,
div u = 0
```

sur `R^3 x [0,1]`, sans frontière ni force, avec viscosité `nu=1`. Son
théorème 1 revendique une infinité de solutions **adaptées de Leray–Hopf**,
lisses pour `t>0`, issues d'une même donnée compacte
`u_loc in C-infinity(R^3\{0}) intersection L^q`, tout `q<3`. La donnée reste
singulière en zéro et n'est pas une donnée Clay.

Pour la donnée HWY localisée exacte `a_HWY=u_loc`, une désingularisation qui
préserve automatiquement la divergence est

```text
a_HWY^epsilon = rho_epsilon * a_HWY,
rho_epsilon(x)=epsilon^-3 rho(x/epsilon),
```

avec `rho` lisse, radiale, compacte et d'intégrale un. Elle est lisse,
compacte, divergence-free et converge fortement vers `a_HWY` dans `L^2`.
Elle fournit donc une vraie famille de données Clay. L'expérience exacte,
qui ne résout aucune évolution, choisit le modèle tangent

```text
a(x)=(-x_2,x_1,0)/|x|^2,
u_0=eta(|x|)a(x),
u_0^epsilon=chi(|x|/epsilon)u_0,
```

où les cutoffs sont radiaux et lisses, `eta=1` sur `r<=1`, `eta=0` sur
`r>=2`, `chi=0` sur `r<=1` et `chi=1` sur `r>=2`. La tangence
`x dot a=0` et l'antisymétrie de la matrice définissant `a` rendent les deux
champs divergence-free. Chaque `u_0^epsilon` est lisse et compacte, donc
admissible comme donnée dans le cas Clay `R^3`.

## Veille primaire et statut CAP

- [Hou–Wang–Yang v2](https://arxiv.org/abs/2509.25116) demeure une
  prépublication. L'en-tête arXiv porte `v2`, 19 mars 2026; la date interne
  « August 11, 2026 » du rendu HTML n'est pas une nouvelle version arXiv.
- Le cutoff de la preuve est **extérieur** :
  `u_in=u_loc+w`, `w=0` pour `|x|<R`,
  `||w||_Lp lesssim R^{-(p-3)/p}`, puis
  `u_cut=-exp(t Delta)w`. Il conserve explicitement le comportement
  `1/|x|` de `u_loc` à l'origine.
- Pour `p=4`, les constantes de (2.10) sont indépendantes de `R` et du temps
  rescalé; la contraction (2.19)–(2.20) utilise `R^{-1/8}`. Ce paramètre ne
  mesure aucune régularisation du coeur.
- Le [dépôt CAP primaire](https://github.com/HouGroup2026/3d-navier-stokes-nonuniqueness)
  a été audité en lecture seule au commit
  `615ee6f3eca3abad7b5814fe9334bcd80bea0328`. Il annonce Julia `>=1.11` et
  au moins 800 Go de RAM. Aucun `Manifest.toml` n'est présent à la racine.
  Le README est contradictoire : son arbre documentaire en annonce un, sa
  note finale confirme son absence. La CAP n'a pas été exécutée.

## Échelle et lemme borné

Sous l'échelle Navier–Stokes
`u_lambda(x,t)=lambda u(lambda x,lambda^2 t)`, les normes de donnée suivent

| Quantité | Facteur |
|---|---:|
| `||u||_2` | `lambda^-1/2` |
| `||u||_3`, `||u||_{L^{3,infinity}}` | `lambda^0` |
| `||nabla u||_2` | `lambda^1/2` |
| `||u||_infinity` | `lambda` |

Plus généralement, si `u_0=r^-1 A(theta)` dans une boule, avec `A` continue
et non nulle, toute régularisation lisse `v_epsilon` est bornée dans une boule
autour de zéro, avec une borne `M_epsilon` qui peut diverger. Choisir
`E subset S^2`, `|E|=m>0`, et `alpha>0` tels que `|A|>=alpha` sur `E` donne,
pour `lambda>=M_epsilon` et les rayons
`r<alpha/(2lambda)`,

```text
|u_0-v_epsilon| >= alpha/(2r),
integral |u_0-v_epsilon|^3 = infinity,

|{|u_0-v_epsilon|>lambda}| >= m alpha^3/(24 lambda^3),
||u_0-v_epsilon||_{L^{3,infinity}} >= alpha (m/24)^(1/3).
```

La conclusion s'applique en particulier à la convolution divergence-free de
la donnée HWY exacte. Elle ne dit pas que la donnée régularisée elle-même a
une norme `L^3` infinie : celle-ci est lisse pour chaque epsilon; c'est la
**distance à la donnée singulière** qui n'est jamais une distance `L^3`
finie. Pour la mollification canonique, les calculs de coquilles donnent aussi
`||a_HWY^epsilon||_3^3=C_A log(1/epsilon)+O(1)` et
`||a_HWY^epsilon||_{H^1}=Theta(epsilon^-1/2)`, à constantes dépendant du profil.

Pour le swirl explicite, avec `d_epsilon=u_0-u_0^epsilon`, le calcul exact
renforce le test :

```text
(8*pi/3)epsilon <= ||d_epsilon||_2^2 <= (16*pi/3)epsilon,
||d_epsilon||_3 = infinity,
||d_epsilon||_{L^{3,infinity}} >= (pi^2/4)^(1/3),
||nabla u_0^epsilon||_2^2 >= 4*pi/epsilon-8*pi,
||u_0^epsilon||_infinity >= 1/(2epsilon).
```

Ainsi `u_0^epsilon -> u_0` fortement dans `L^2`, mais ni dans `L^3` ni dans
`L^{3,infinity}`; les contrôles `H^1` et `L^infinity` ne sont pas uniformes.
Avec le cutoff plat explicite de la revue contradictoire, deux membres lisses
successifs satisfont même

```text
||u_epsilon-u_(2epsilon)||_2^2 <= (32*pi/3)epsilon,
sup_epsilon ||u_epsilon||_{L^{3,infinity}} <= (4*pi/3)^(1/3),
||u_epsilon-u_(2epsilon)||_3^3 >=
  [exp(8/3)/(1+exp(8/3))]^3 (3*pi^2/4) log(5/4) > 0.
```

La suite est donc Cauchy en énergie et bornée au seuil faible, mais non Cauchy
dans l'espace critique fort. Ce contre-profil réfute un module universel
`L^2 + borne L^{3,infinity} -> compacité L^3`.

La pression n'est pas localisée avec la vitesse. Avec la jauge Leray/Riesz,

```text
p_epsilon=R_i R_j(u_epsilon,i u_epsilon,j),
-Delta p_epsilon=partial_i partial_j(u_epsilon,i u_epsilon,j),
||p_epsilon||_2 <= ||u_epsilon||_4²
  <= [(32*pi/15)(epsilon^-1-1/2)]^(1/2).
```

Cette dernière relation est une borne supérieure et ne prouve pas que la
pression diverge; elle interdit seulement de traiter le cutoff comme un objet
local sans queue de pression. Aucune évolution n'étant calculée, aucun résidu
de l'équation de quantité de mouvement n'est revendiqué.

## Implication falsifiable et écart Clay

Le maillon transférable négatif est précis : une preuve de stabilité de la
construction HWY fondée sur une petite perturbation de la donnée dans `L^3`,
`L^{3,infinity}`, ou sur une borne uniforme `H^1` de cette famille ne peut pas
utiliser une régularisation intérieure de ce type. Le petit paramètre
`R^{-1/8}` de HWY agit sur la queue et ne répare pas ce défaut critique au
coeur.

Ce résultat ne ferme pas le transfert vers Clay. Pour chaque epsilon, la
théorie locale fournit une solution forte et l'unicité faible–forte interdit
deux branches de Leray–Hopf tant que cette solution forte existe. Mais les
estimations présentes ne prouvent ni que cette durée tend vers zéro, ni qu'une
branche singulière ne peut être suivie après une éventuelle perte de
régularité. Une route restante devrait être non perturbative : contrôler une
couche parabolique de taille `t environ epsilon^2`, transporter les coordonnées
instables, puis prouver une séparation de branches compatible avec
l'unicité faible–forte. Aucun tel théorème n'apparaît dans v2.

## Passe contradictoire

Quatre attaques ont été appliquées.

1. **Divergence silencieuse.** Un cutoff radial ne préserve pas tout champ
   homogène divergence-free si celui-ci possède une composante radiale. La
   donnée HWY exacte est donc mollifiée par convolution, qui commute avec la
   divergence; le certificat numérique explicite utilise un champ tangent.
2. **Confusion donnée/différence.** `u_0^epsilon` est dans `L^3`; seule
   `u_0-u_0^epsilon`, contenant encore le coeur singulier, n'y appartient pas.
3. **Grandes normes donc blow-up.** Cette inférence est rejetée : des données
   lisses à grandes normes peuvent engendrer des solutions globales. Le résultat
   exclut une classe de preuves uniformes, pas une dynamique.
4. **Compacité énergétique ignorée.** La convergence `L^2` est explicitement
   conservée. Elle peut donner des sous-limites de Leray–Hopf, mais aucune
   stabilité des différentes branches ni de leur coordonnée instable.

Le script vérifie exactement `B+B^T=0`, `tr B=0`, la tangence, les coefficients
angulaires et toutes les identités rationnelles sur cinq échelles. Le gap
transcendant est conservé comme expression symbolique strictement positive.
Résidu algébrique maximal : `0`; borne d'arrondi : `0`; aucune discrétisation
PDE.

Trois revues séparées sont conservées : veille/version/statut, analyse PDE et
contre-profil/CAP. Elles ont été produites par des sous-agents de la même
famille Codex; elles constituent des passes contradictoires distinctes par
tâche et contexte, mais pas une revue scientifique indépendante externe.

## Décision

Le raccord perturbatif critique est **abandonné** pour les régularisations
intérieures qui suppriment le coeur. La question globale est **à réviser**, pas
réfutée : le prochain maillon est la projection de l'erreur de couche sur le
mode adjoint instable et sa propagation entre `t environ epsilon^2` et un temps
fixe. Si cette projection ne peut pas être bornée avec les données publiques,
le cycle suivant doit isoler exactement l'artefact CAP minimal manquant plutôt
que lancer les 800 Go de calcul.
