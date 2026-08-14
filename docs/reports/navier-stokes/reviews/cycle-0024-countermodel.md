# Cycle 0024 — frontière du passage log-BMO vers un axe

Date : 2026-08-14.

Type de passe : contre-modèles fonctionnels et calcul adverse par la même
famille de modèle; ce document n'est pas une revue externe indépendante.

## Verdict

L'implication informelle

```text
direction log-BMO + Phi<=M + masse critique par blocs
    -> axe mobile à variation et erreur sublinéaires
```

est **vraie sous une formulation précise**, mais fausse ou non intrinsèque
dès que l'on retire l'une de ses conventions silencieuses.

La formulation suffisante minimale obtenue ici est la suivante. Soit

\[
 r_s=R_*e^{-s},\qquad
 a(s)=\fint_{B_{r_s}}\xi(x)dx,
 \tag{1}
\]

où une **même extension unitaire** \(|\xi|=1\) est fixée sur tout le
voisinage, y compris sur \(\{\Phi=0\}\). Supposons

\[
 \fint_{B_{r_s}}|\xi-a(s)|dx\leq\frac K{1+s}
 \quad(s\geq s_0),
 \tag{2}
\]

et \(0\leq\Phi\leq M\). Pour tout pas logarithmique fixé \(L>0\), les axes

\[
 e_k=\frac{a(s_k)}{|a(s_k)|},\qquad s_k=s_0+kL,
 \tag{3}
\]

sont définis pour \(s_k\) assez grand et satisfont

\[
 \sum_{k<N}|e_{k+1}-e_k|=O_{K,L}(\log N),
 \tag{4}
\]

ainsi que

\[
 \sum_{k<N}\int_{s_k}^{s_k+L}
 \left\langle\Phi|\xi-e_k|\right\rangle ds
 =O_{K,L,M}(\log N).
 \tag{5}
\]

La masse critique n'est pas nécessaire pour construire les axes. Elle sert à
empêcher que leur pertinence pondérée disparaisse. Si chaque bloc contigu
vérifie

\[
 \int_{s_k}^{s_k+L}\langle\Phi^{3/2}\rangle ds\geq\kappa,
 \tag{6}
\]

alors

\[
 \int_{s_k}^{s_k+L}\langle\Phi\rangle ds
 \geq\frac\kappa{\sqrt M},
 \qquad
 |\{\Phi>0\}\cap(I_k\times S^2)|_{\rm norm}
 \geq\frac\kappa{M^{3/2}}.
 \tag{7}
\]

Ainsi les moyennes pondérées ne peuvent ni s'annuler durablement, ni être
portées par une activité de mesure tendant vers zéro.

Les essais adverses donnent la frontière exacte suivante.

- La propriété n'est pas intrinsèque sans convention d'extension aux zéros :
  un même champ \(\Phi\xi\) admet une extension constante de semi-norme nulle
  et une extension antipodale de semi-norme infinie.
- Une activité de fraction \(O(1/s)\) peut cacher n'importe quelle phase au
  test centré, mais elle viole (6) sous \(\Phi\leq M\).
- Deux phases antipodales de masses pondérées persistantes imposent une erreur
  linéaire pour tout axe orienté; elles violent donc (5), ou bien (2).
- Des blocs actifs séparés par des lacunes de longueur comparable à leur
  profondeur permettent une rotation de phase compatible avec log-BMO, mais
  ne satisfont pas la version contiguë de (6).
- Les boules centrées suffisent à construire (3)–(5), mais ne suffisent pas à
  établir la semi-norme log-BMO globale requise par un argument de
  commutateur. Des coquilles minces passent tous les tests centrés et échouent
  sur des boules décentrées.

Le prochain échappatoire réel n'est donc plus une moyenne annulée dans un
cœur unique. C'est une cascade **multi-centres** où chaque cœur possède sa
propre extension et son propre axe, tandis qu'aucune famille unique de boules
emboîtées ne voit une masse contiguë.

## 1. Lemme positif : la moyenne ne peut pas s'annuler

Notons

\[
 q(s)=\fint_{B_{r_s}}|\xi-a(s)|dx.
 \tag{8}
\]

Comme \(|\xi|=1\) presque partout,

\[
 1-|a(s)|
 \leq\fint_{B_{r_s}}\big||\xi|-|a(s)|\big|dx
 \leq q(s).
 \tag{9}
\]

Sous (2), \(|a(s)|\geq1-K/(1+s)\). En particulier, pour
\(1+s\geq2K\),

\[
 |a(s)|\geq\frac12,
 \tag{10}
\]

et l'axe normalisé (3) est unique. Cette estimation exclut directement
l'échappatoire « moyenne annulée » pour une extension unitaire log-BMO.

### Erreur sur un bloc

Avec la variable radiale \(t=\log(r_s/|x|)\), la moyenne de boule porte le
poids \(3e^{-3t}\). Sur \(0\leq t\leq L\), ce poids est au moins
\(3e^{-3L}\), donc

\[
 \int_0^L\left\langle|\xi(s+t,\cdot)-a(s)|\right\rangle dt
 \leq\frac{e^{3L}}3q(s).
 \tag{11}
\]

De plus,

\[
 |e(s)-a(s)|=1-|a(s)|\leq q(s).
 \tag{12}
\]

En posant

\[
 C_L=L+\frac{e^{3L}}3,
 \tag{13}
\]

on obtient

\[
 \boxed{
 \int_s^{s+L}\langle|\xi-e(s)|\rangle du
 \leq C_Lq(s)\leq\frac{C_LK}{1+s}.}
 \tag{14}
\]

La borne \(\Phi\leq M\) transforme (14) en l'estimation pondérée utilisée
dans (5).

### Variation des axes

La boule \(B_{r_{s+L}}\) occupe la fraction \(e^{-3L}\) de
\(B_{r_s}\). Par conséquent,

\[
 |a(s+L)-a(s)|
 \leq e^{3L}q(s).
 \tag{15}
\]

Pour deux vecteurs de norme au moins \(1/2\),

\[
 \left|\frac a{|a|}-\frac b{|b|}\right|
 \leq4|a-b|.
 \tag{16}
\]

Ainsi

\[
 |e_{k+1}-e_k|
 \leq\frac{4e^{3L}K}{1+s_k}.
 \tag{17}
\]

La sommation harmonique prouve (4); la sommation de (14), multipliée par
\(M\), prouve (5). Ces deux conclusions utilisent seulement les boules
centrées et une extension unitaire. La semi-norme globale sur toutes les
boules est une hypothèse plus forte.

## 2. Ce que la masse par blocs ajoute exactement

Sous \(0\leq\Phi\leq M\),

\[
 \Phi^{3/2}\leq\sqrt M\,\Phi,
 \qquad
 \Phi^{3/2}\leq M^{3/2}\mathbf1_{\{\Phi>0\}}.
 \tag{18}
\]

L'intégration sur un bloc donne (7). Si

\[
 P_k=\int_{I_k}\langle\Phi\rangle ds,
 \qquad
 R_k=\int_{I_k}\langle\Phi\xi\rangle ds,
 \tag{19}
\]

alors (14) implique

\[
 |R_k-P_ke_k|
 \leq\frac{MC_LK}{1+s_k}.
 \tag{20}
\]

En combinant (7) et (20),

\[
 |R_k|geq\frac\kappa{\sqrt M}
 -\frac{MC_LK}{1+s_k}>0
 \tag{21}
\]

pour tout bloc assez profond. La direction du résultat pondéré devient donc
elle aussi canonique et proche de \(e_k\). Une moyenne pondérée exactement
nulle est incompatible avec les trois prémisses : extension unitaire (2),
borne \(M\), et masse uniforme (6).

## 3. Extension aux zéros : même vorticité, deux verdicts BMO

Fixons un ensemble actif angulaire \(A\subset S^2\) de fraction normalisée
\(\delta\in(0,1)\), et posons sur chaque bloc

\[
 \Phi=M\mathbf1_A,
 \qquad
 \xi=e_0\quad\hbox{sur }A.
 \tag{22}
\]

Alors

\[
 \int_{I_k}\langle\Phi^{3/2}\rangle ds
 =LM^{3/2}\delta.
 \tag{23}
\]

Le produit physique \(\Phi\xi=M e_0\mathbf1_A\) ne fixe aucune valeur de
\(\xi\) sur \(A^c\). Deux extensions unitaires donnent :

\[
 \xi_+(n)=e_0\quad\hbox{partout},
 \tag{24}
\]

dont l'oscillation est nulle, et

\[
 \xi_-(n)=
 \begin{cases}e_0,&n\in A,\\-e_0,&n\notin A,
 \end{cases}
 \tag{25}
\]

qui possède un saut sur \(\partial A\). Toute petite boule traversant cette
interface a une oscillation d'ordre un; son semi-norme pondéré est infini.

Le même champ \(\Phi\xi\), la même borne \(M\) et la même masse (23) ont
donc deux statuts opposés. La phrase « la direction de la vorticité appartient
à log-BMO » n'est pas intrinsèque en présence de zéros. Il faut fixer :

- soit une extension unitaire particulière;
- soit l'existence d'une extension avec constante contrôlée;
- soit une norme définie directement sur l'ensemble actif, accompagnée d'un
  véritable théorème d'extension.

Ces trois formulations ne sont pas équivalentes.

## 4. Activité sparse : pourquoi la masse uniforme est nécessaire

Considérons un modèle moyenné où \(\Phi=M\) sur une fraction

\[
 \delta(s)=\frac1{1+s}
 \tag{26}
\]

et vaut zéro ailleurs. Avec l'extension nulle, toute phase active arbitraire
ne contribue qu'à \(O(1/s)\) à une oscillation centrée moyenne. Mais, sur un
bloc fixe,

\[
 \int_s^{s+L}\langle\Phi^{3/2}\rangle du
 \leq\frac{LM^{3/2}}{1+s},
 \tag{27}
\]

qui tend vers zéro. Ce modèle réfute tout passage « activité sparse vers
axe » dépourvu de (6), mais ne réfute pas le lemme correctement quantifié.

Réciproquement, (7) est la borne optimale issue des seules hypothèses
\(\Phi\leq M\) et (6) : elle est atteinte par \(\Phi=M\) sur un ensemble de
mesure \(\kappa/M^{3/2}\) et zéro ailleurs. Aucune meilleure
anti-concentration ne peut être invoquée sans hypothèse supplémentaire.

### Pourquoi la borne supérieure est indispensable

Si \(M\) est retiré, une fraction \(\delta(s)=s^{-2}\) peut porter une
amplitude \(\Phi=s^2\). Une mauvaise phase d'oscillation non pondérée
\(O(s^{-2})\) produit alors une erreur pondérée d'ordre un par tranche :

\[
 \delta(s)\Phi(s)=1.
 \tag{28}
\]

Elle contribue même \(\delta\Phi^{3/2}=s\) à la masse critique. Une borne
BMO non pondérée ne contrôle donc pas l'erreur \(\Phi|\xi-e|\) sans une borne
ponctuelle sur \(\Phi\), ou un remplacement de Hölder explicitement plus
fort. Ce contre-profil est un modèle de moyenne centrée; des interfaces
angulaires abruptes échoueraient en plus au BMO global.

## 5. Moyennes annulées et phases antipodales

Supposons qu'un bloc porte deux phases \(+v\) et \(-v\), de masses pondérées

\[
 P_+=\int_{E_+}\Phi,
 \qquad P_-=\int_{E_-}\Phi.
 \tag{29}
\]

Pour tout axe **orienté** \(e\in S^2\), l'inégalité triangulaire donne

\[
 \boxed{
 P_+|v-e|+P_-|-v-e|
 \geq2\min(P_+,P_-).}
 \tag{30}
\]

La constante est optimale, atteinte par \(e=v\) ou \(e=-v\). Si les deux
phases portent chacune une masse positive uniforme sur une densité positive
de blocs, l'erreur cumulée est linéaire. Elles ne peuvent satisfaire (5).

Dans le cas équilibré \(P_+=P_-=P/2\), le résultat pondéré \(R_k\) de (19)
est nul et l'erreur minimale vaut \(P\). Cela montre que
\(\Phi\leq M\) et la masse (6), **sans BMO**, ne construisent aucun axe.

Inversement, si une extension unitaire prend les valeurs antipodales sur des
fractions fixes d'une même boule, sa moyenne reste à distance fixe de la
sphère unité. Par (9), son oscillation ne peut être \(O(1/s)\). La
cancellation antipodale n'est donc pas une échappatoire sous (2); elle est un
contre-exemple à toute preuve qui omet (2).

Si l'objet géométrique est une ligne non orientée, \(+v\) et \(-v\) sont
identifiés dans \(\mathbb{RP}^2\), et (30) ne s'applique plus. La vorticité
\(\omega/|\omega|\) est un vecteur orienté. Remplacer silencieusement son axe
par une ligne change le lemme.

## 6. Lacunes radiales : masse sur des blocs choisis contre blocs contigus

Prenons

\[
 s_n=2^n,
 \qquad I_n=[s_n,s_n+L],
 \tag{31}
\]

et posons \(\Phi=M\) sur \(I_n\), \(\Phi=0\) dans les lacunes. Sur les bons
blocs, choisissons les phases \((-1)^ne_0\). Dans la lacune
\([s_n+L,s_{n+1}]\), faisons tourner une extension unitaire à vitesse

\[
 O\!\left((s_{n+1}-s_n)^{-1}\right)=O(1/s_n).
 \tag{32}
\]

Le critère de gradient radial du cycle 0023 donne une constante log-BMO
locale uniforme. Chaque bloc sélectionné satisfait (6) avec
\(\kappa=LM^{3/2}\), mais presque tous les blocs d'une partition contiguë
fixe sont vides.

Le nombre de retournements avant la profondeur \(S\) est \(O(\log S)\). Une
sélection d'axe suivant l'extension a donc encore une variation sublinéaire;
ce modèle ne réfute pas (3)–(5). Il réfute en revanche deux sommations
incorrectes :

- compter une coercivité positive sur les seuls bons blocs comme si leur
  nombre était proportionnel à \(S\);
- ignorer que le moment solénoïdal peut se recharger dans les lacunes.

La frontière correcte est : blocs contigus de longueur supérieure et
inférieure contrôlées, ou bien une densité inférieure positive de bons blocs
avec un budget explicite sur toutes les lacunes.

## 7. Boules centrées contre boules décentrées

Le test concentrique peut être trompé par des coquilles extrêmement minces.
Soit

\[
 s_n=2^n,
 \qquad \delta_n=s_n^{-2},
 \tag{33}
\]

et prenons \(\xi=-e_0\) dans la coquille logarithmique
\([s_n,s_n+\delta_n]\), \(\xi=e_0\) ailleurs. Pour une boule centrée dont la
profondeur initiale est proche de \(s_n\), la fraction volumique de la phase
négative est au plus

\[
 p_n\leq1-e^{-3\delta_n}\leq3\delta_n.
 \tag{34}
\]

Un mélange de fractions \(p\) et \(1-p\) des valeurs \(-e_0,+e_0\) a
l'oscillation exacte

\[
 \operatorname{MO}=4p(1-p)\leq4p.
 \tag{35}
\]

Les coquilles suivantes sont exponentiellement amorties par leur distance en
\(s\). Ainsi les boules centrées paient

\[
 s_n\operatorname{MO}=O(s_n\delta_n)=O(1/s_n),
 \tag{36}
\]

et passent le test.

Mais \(\xi\) saute sur chaque sphère bordant une coquille. Une boule
décentrée traversant cette sphère possède une oscillation d'ordre un à des
rayons arbitrairement petits : la semi-norme log-BMO globale est infinie.
Après lissage monotone sur l'épaisseur physique

\[
 w_n\asymp R_*e^{-s_n}\delta_n,
 \tag{37}
\]

une boule de rayon comparable à \(w_n\) voit toujours une portion fixe de la
transition et coûte \(c(s_n+|\log\delta_n|)\). Le test global diverge encore.

Cet exemple établit deux faits distincts :

- les boules centrées suffisent aux estimations algébriques (3)–(5);
- elles ne certifient pas l'hypothèse globale log-BMO utilisée dans les
  estimations de commutateur ou de multiplicateur.

## 8. Certificat exact et reproductible

Le script vérifie les constantes du lemme positif et des contre-profils avec
`Fraction`. Les exponentielles servent uniquement aux évaluations explicites
de volumes radiaux.

```python
from fractions import Fraction as F
from math import exp, log


# A rational parameter choice for the block-mass gates.
M = F(4)                 # M^(1/2)=2, M^(3/2)=8
sqrt_M = F(2)
M_three_halves = F(8)
L = F(2)
kappa = F(1)

active_measure_lower = kappa / M_three_halves
L1_mass_lower = kappa / sqrt_M
assert active_measure_lower == F(1, 8)
assert L1_mass_lower == F(1, 2)

# Sharpness: Phi=M on measure kappa/M^(3/2).
assert M_three_halves * active_measure_lower == kappa
assert M * active_measure_lower == L1_mass_lower

# Antipodal phases: equal masses P/2 have minimum oriented-axis error P.
P = F(3, 5)
P_plus = P_minus = P / 2
antipodal_error_lower = 2 * min(P_plus, P_minus)
assert antipodal_error_lower == P

# Unit-extension normalization: q<=K/(1+s), and q<=1/2 gives |a|>=1/2.
K = F(3)
s = F(11)
q = K / (1 + s)
assert q == F(1, 4)
assert 1 - q == F(3, 4) > F(1, 2)

# Harmonic sums make block-axis variation and weighted error sublinear.
def harmonic_sum(n):
    return sum((F(1, k) for k in range(1, n + 1)), F(0))

for n in (16, 64, 256):
    assert harmonic_sum(n) / n < F(1, 2)

# Sparse activity delta=1/(1+s) loses uniform fixed-block mass.
for depth in (16, 64, 256):
    sparse_mass_upper = L * M_three_halves / (1 + depth)
    assert sparse_mass_upper < (L * M_three_halves / depth)
    if depth >= 64:
        assert sparse_mass_upper < kappa

# Thin antipodal shell: exact centered mixture and its logarithmic decay.
previous_weighted = None
for n in range(4, 13):
    shell_depth = F(2 ** n)
    delta = 1 / (shell_depth * shell_depth)
    p = 1 - exp(-3 * float(delta))
    mean_oscillation = 4 * p * (1 - p)
    assert p <= 3 * float(delta)
    weighted = float(shell_depth) * mean_oscillation
    assert weighted <= 12 / float(shell_depth)
    if previous_weighted is not None:
        assert weighted < previous_weighted
    previous_weighted = weighted

# A balanced radial step has maximum centered mixing at p=1/2.
d = log(2) / 3
p = exp(-3 * d)
assert abs(p - 0.5) < 1e-15
assert abs(4 * p * (1 - p) - 1) < 1e-15

print("unit-extension axis constants: PASS")
print("block mass, sparse activity and antipodal gate: PASS")
print("centered thin-shell countertest: PASS")
```

Commande de reproduction : extraire le bloc puis exécuter `python -` depuis
la racine du dépôt. Dépendances : bibliothèque standard Python. Graine :
aucune. Les seuils structurels sont rationnels exacts; les exponentielles
évaluent les volumes de coquilles explicitement définies.

## 9. Portée et prochain échappatoire

Ces résultats sont fonctionnels et cinématiques. Les contre-profils ne sont
pas annoncés comme des vorticités divergence-free, des données Clay ou des
solutions Navier–Stokes. La pression, Biot–Savart, la viscosité et l'évolution
ne sont pas engagés.

La frontière transférable est :

> **Extraction d'axe par moyennes emboîtées.** Une extension unitaire unique
> dont l'oscillation sur les boules concentriques est \(O(1/s)\) possède des
> moyennes non nulles. Leur normalisation sur des blocs contigus de longueur
> fixe a variation \(O(\log s)\). Sous \(\Phi\leq M\), l'erreur pondérée
> cumulée est aussi \(O(\log s)\). Une masse critique uniforme par bloc rend
> les résultantes pondérées non nulles aux grandes profondeurs.

Ce lemme ne doit pas être appliqué si :

1. la direction n'est définie que sur \(\{\Phi>0\}\) sans extension unitaire
   globale contrôlée;
2. la borne disponible est seulement pondérée par \(\Phi\) ou seulement
   tranche par tranche;
3. \(\Phi\) n'a pas de borne supérieure uniforme;
4. les bons blocs sont lacunaires sans contrôle des lacunes;
5. le centre des boules change avec le bloc;
6. les axes sont des lignes non orientées alors que l'erreur porte sur des
   vecteurs orientés.

Le prochain test décisif est donc un **contre-profil multi-centres** : placer
une masse \(\kappa\) dans chaque bloc, mais la faire migrer entre des boules
dont les centres sont séparés à l'échelle locale. Il faudra vérifier si une
extension globale log-BMO force tout de même la cohérence des phases entre
composantes, ou si la non-localité de Biot–Savart et les régions de vorticité
nulle permettent de casser l'emboîtement utilisé dans (15).

```json
{
  "cycle": "0024",
  "claim": "BMO_TO_AXIS_BY_NESTED_MEANS",
  "status": "PROVED_UNDER_EXPLICIT_EXTENSION_AND_CENTERING",
  "requirements": [
    "single unit-valued extension on zeros",
    "centered mean oscillation K/(1+s)",
    "uniform Phi upper bound for weighted error",
    "fixed contiguous logarithmic blocks"
  ],
  "countermodels": [
    "two inequivalent extensions of the same zero-containing field",
    "sparse activity without uniform block mass",
    "balanced antipodal phases without BMO",
    "lacunary active blocks",
    "thin radial shells passing centered but failing off-center balls"
  ],
  "next_gap": "MULTICENTER-NONNESTED-AXIS-EXTRACTION",
  "pde_scope": "functional geometry only; no Navier-Stokes trajectory"
}
```
