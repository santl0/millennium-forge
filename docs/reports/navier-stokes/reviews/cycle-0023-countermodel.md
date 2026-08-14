# Cycle 0023 — axes radiaux tournants et budget logarithmique

Date : 2026-08-14.

Type de passe : calcul adverse indépendant par la même famille de modèle;
ce document n'est pas une revue externe indépendante.

## Verdict

Pour un champ directionnel radial

\[
 \xi(x)=e(s),\qquad s=\log(R_*/|x|),\qquad |e(s)|=1,
 \tag{1}
\]

la moyenne sur \(B_r\), avec \(S=\log(R_*/r)\), est exactement une moyenne
exponentielle vers les petites échelles :

\[
 m(S):=(\xi)_{B_r}
 =\int_0^\infty3e^{-3t}e(S+t)dt.
 \tag{2}
\]

La variance quadratique et l'oscillation moyenne \(D_1\) sont

\[
 V_2(S)=1-|m(S)|^2,
 \qquad
 D_1(S)=\int_0^\infty3e^{-3t}|e(S+t)-m(S)|dt,
 \tag{3}
\]

avec

\[
 \frac12V_2(S)\leq D_1(S)\leq\sqrt{V_2(S)}.
 \tag{4}
\]

Deux régimes se séparent exactement.

1. Pour une rotation plane à vitesse constante
   \(e(s)=(\cos\beta s,\sin\beta s,0)\),

   \[
   |m|^2=\frac9{9+\beta^2},
   \qquad V_2=\frac{\beta^2}{9+\beta^2}.
   \tag{5}
   \]

   Une minoration plus forte donne

   \[
   D_1\geq
   \frac{6|\beta|}{36+\beta^2}
   \coth\!\left(\frac{3\pi}{|\beta|}\right)>0.
   \tag{6}
   \]

   Ainsi \(S D_1(S)\to\infty\) pour tout \(\beta\ne0\) : une rotation à
   vitesse constante échoue au test log-BMO sur les seules boules centrées.

2. Pour la rotation lente
   \(e(s)=(\cos(\beta\log(1+s)),
   \sin(\beta\log(1+s)),0)\),

   \[
   D_1(S)\leq\frac{|\beta|}{3(1+S)},
   \qquad
   V_2(S)\leq\frac{\beta^2}{9(1+S)^2}.
   \tag{7}
   \]

   Cette famille passe le budget logarithmique centré et, par un contrôle
   local du gradient, le budget sur les petites boules décentrées. Son axe ne
   converge pourtant pas : sa variation totale croît comme
   \(|\beta|\log(1+s)\).

Le lien avec la porte solénoïdale du cycle 0022 est négatif. Pour maintenir
une magnitude \(0<c\leq\Phi\leq C\), un axe mobile doit fournir
asymptotiquement une variation totale au moins

\[
 \int_S^T|e'(s)|ds
 \geq\frac{4c}{3C}(T-S)-O(1)-O(\log(T/S)).
 \tag{8}
\]

La vitesse constante possède ce budget mais viole log-BMO; la vitesse
\(1/s\) respecte log-BMO mais ne possède pas ce budget. La seule échappatoire
cinématique restante consiste à accumuler une grande variation dans une
petite amplitude ou un petit rapport cyclique. Cela ne contredit pas BMO,
mais produit de grandes dérivées logarithmiques et donc un coût visqueux qui
doit être contrôlé séparément.

## 1. Mesure radiale exacte sur une boule

Écrivons \(\rho=re^{-t}\). Alors

\[
 \rho^2d\rho=-r^3e^{-3t}dt,
 \qquad
 \frac{4\pi\rho^2|d\rho|}{|B_r|}=3e^{-3t}dt.
 \tag{9}
\]

La variable \(T=t\) sous la moyenne de boule suit donc exactement une loi
exponentielle de paramètre trois :

\[
 \mathbb P(T\in dt)=3e^{-3t}dt,
 \quad
 \mathbb ET=\frac13,
 \quad
 \operatorname{Var}T=\frac19.
 \tag{10}
\]

Les formules (2)–(3) en découlent. Comme \(|e|=1\),

\[
 \begin{aligned}
 V_2
 &=\mathbb E|e(S+T)-m|^2\\
 &=\mathbb E|e(S+T)|^2-|m|^2=1-|m|^2.
 \end{aligned}
 \tag{11}
\]

Avec \(T'\) indépendant de même loi,

\[
 V_2=\frac12\mathbb E|e(S+T)-e(S+T')|^2.
 \tag{12}
\]

Puisque \(|e-m|\leq2\), on a \(|e-m|^2\leq2|e-m|\), ce qui donne la
borne inférieure de (4); la borne supérieure est Cauchy–Schwarz. Une autre
inégalité utile est

\[
 D_1\leq\mathbb E|e(S+T)-e(S+T')|,
 \tag{13}
\]

obtenue en écrivant \(e(S+T)-m\) comme une moyenne en \(T'\).

La moyenne exponentielle satisfait aussi l'identité de résolvante

\[
 \boxed{m'(S)=3(m(S)-e(S)).}
 \tag{14}
\]

Elle est valable au sens faible pour \(e\) localement intégrable, et
ponctuellement aux points de régularité.

## 2. Rotation à vitesse constante

Identifions le plan de rotation à \(\mathbb C\). Pour
\(e(s)=e^{i\beta s}\),

\[
 \begin{aligned}
 m(S)
 &=e^{i\beta S}\int_0^\infty3e^{-(3-i\beta)t}dt\\
 &=e^{i\beta S}\frac3{3-i\beta}.
 \end{aligned}
 \tag{15}
\]

Cela prouve (5). La borne élémentaire de (4) donnerait déjà

\[
 D_1\geq\frac{\beta^2}{2(9+\beta^2)}.
 \tag{16}
\]

On peut obtenir (6) en utilisant deux copies indépendantes. La différence
\(Z=T-T'\) a la densité de Laplace

\[
 f_Z(z)=\frac32e^{-3|z|}.
 \tag{17}
\]

Comme la corde entre deux phases vaut
\(2|\sin(\beta Z/2)|\), l'inégalité triangulaire donne

\[
 D_1\geq\frac12\mathbb E|e^{i\beta T}-e^{i\beta T'}|
 =3\int_0^\infty e^{-3t}|\sin(\beta t/2)|dt.
 \tag{18}
\]

Pour \(a,b>0\), la sommation exacte sur les demi-périodes donne

\[
 \int_0^\infty e^{-at}|\sin(bt)|dt
 =\frac{b}{a^2+b^2}\coth\left(\frac{a\pi}{2b}\right).
 \tag{19}
\]

Les choix \(a=3\) et \(b=|\beta|/2\) donnent (6). Pour
\(|\beta|\ll1\), cette minoration est
\(|\beta|/6+o(|\beta|)\), plus informative que la borne quadratique (16).

## 3. Rotation logarithmiquement lente

Posons

\[
 \theta(s)=\beta\log(1+s),
 \qquad e(s)=(\cos\theta(s),\sin\theta(s),0).
 \tag{20}
\]

Pour \(t,t'\geq0\),

\[
 |\theta(S+t)-\theta(S+t')|
 \leq\frac{|\beta|}{1+S}|t-t'|.
 \tag{21}
\]

La longueur d'une corde est au plus l'angle. Or

\[
 \mathbb E|T-T'|=\frac13,
 \qquad
 \mathbb E|T-T'|^2=\frac29.
 \tag{22}
\]

Les identités (12)–(13) donnent exactement les majorants (7).

La moyenne complexe possède aussi la représentation fermée

\[
 m(S)=3^{-i\beta}e^{3(1+S)}
 \Gamma(1+i\beta,3(1+S)),
 \tag{23}
\]

où \(\Gamma(\cdot,\cdot)\) est la gamma incomplète supérieure. Cette formule
n'est pas utilisée dans le certificat. L'expansion issue des moments (10)
est

\[
 m(S)=e^{i\beta\log(1+S)}\left[
 1+\frac{i\beta}{3(1+S)}
 -\frac{\beta^2+i\beta}{9(1+S)^2}
 +O((1+S)^{-3})\right].
 \tag{24}
\]

Elle entraîne

\[
 V_2(S)=\frac{\beta^2}{9(1+S)^2}+O((1+S)^{-3}).
 \tag{25}
\]

Pour l'oscillation \(L^1\), la convergence dominée appliquée à la
linéarisation de la phase donne la constante asymptotique exacte

\[
 \boxed{
 (1+S)D_1(S)\longrightarrow
 |\beta|\mathbb E|T-1/3|
 =\frac{2|\beta|}{3e}.}
 \tag{26}
\]

La borne log-BMO centrée est donc finie et non triviale.

### Boules décentrées

Le gradient physique de la direction vérifie

\[
 |\nabla\xi(x)|=\frac{|\beta|}{|x|(1+s)}.
 \tag{27}
\]

Sur une boule \(B_\rho(x_0)\) avec \(\rho\leq|x_0|/2\), Poincaré et (27)
donnent, à constante géométrique absolue près,

\[
 \operatorname{MO}_{B_\rho(x_0)}\xi
 \lesssim |\beta|\frac{\rho}{|x_0|(1+s_0)}.
 \tag{28}
\]

En posant \(q=\rho/|x_0|\), le poids logarithmique ajoute
\(s_0+\log(1/q)\). La quantité

\[
 q\frac{s_0+\log(1/q)}{1+s_0}
 \tag{29}
\]

est uniformément bornée pour \(0<q\leq1/2\). Les boules qui rencontrent
l'origine se ramènent, avec des constantes géométriques, aux boules centrées.
Ainsi la rotation lente fournit bien un exemple directionnel local dans la
classe log-BMO; elle n'est pas seulement un artefact du test centré.

## 4. Budget de variation imposé par la porte solénoïdale

Relions ce calcul directionnel à

\[
 W=r^{-2}\Omega,qquad \Omega=\Phi\xi,qquad
 0<c\leq\Phi\leq C.
 \tag{30}
\]

Décomposons \(\Omega=An+B\), \(B\cdot n=0\), et supposons
\(\operatorname{div}_{S^2}B=A_s\). Pour un axe mobile \(e(s)\), posons

\[
 \mu(s,n)=e(s)\cdot n,
 \qquad M(s)=\int_{S^2}\mu(s,n)A(s,n)d\sigma.
 \tag{31}
\]

Si

\[
 \int_{S^2}|\xi(s,n)-e(s)|d\sigma\leq K/s,
 \tag{32}
\]

alors le calcul du cycle 0022, avec le terme nouveau \(\mu_s\), donne

\[
 \begin{aligned}
 M'(s)
 &=\int_{S^2}(e'(s)\cdot n)A\,d\sigma
 -\int_{S^2}\Phi\nabla_{S^2}\mu\cdot\xi\,d\sigma\\
 &\leq2\pi C|e'(s)|-\frac{8\pi c}{3}+\frac{CK}{s}.
 \end{aligned}
 \tag{33}
\]

Ici \(\int_{S^2}|e'\cdot n|d\sigma=2\pi|e'|\) et
\(|M|\leq4\pi C\). L'intégration de (33) donne la borne nécessaire

\[
 \boxed{
 \int_S^T|e'(s)|ds
 \geq\frac{4c}{3C}(T-S)-4
 -\frac{K}{2\pi}\log(T/S).}
 \tag{34}
\]

Le terme constant \(-4\) vient de la variation maximale \(8\pi C\) du
moment borné. Cette inégalité ne garantit pas qu'une grande variation suffise
à résoudre la contrainte : elle est seulement nécessaire.

Pour (20),

\[
 \int_S^T|e'|ds
 =|\beta|\log\frac{1+T}{1+S},
 \tag{35}
\]

ce qui est sous-linéaire et contredit (34) pour \(T\to\infty\). Une rotation
constante fournit \(|\beta|(T-S)\), mais (6) l'exclut de log-BMO. Cette
tension ferme l'échappatoire la plus régulière : **un axe tournant de façon
monotone et lente ne répare pas une magnitude critique non dégénérée**.

## 5. Échappatoires adverses

### 5.1 Oscillations rapides de petite amplitude

Considérons l'angle

\[
 \theta(s)=\frac{\sin(s^3)}s,
 \qquad e(s)=(\cos\theta(s),\sin\theta(s),0).
 \tag{36}
\]

Pour tout \(t\geq0\), \(|\theta(S+t)|\leq1/S\). La direction reste donc
dans un cap de rayon \(1/S\), et

\[
 D_1(S)\leq\mathbb E|e(S+T)-e(S+T')|leq\frac2S.
 \tag{37}
\]

Cependant

\[
 \theta'(s)=3s\cos(s^3)-s^{-2}\sin(s^3),
 \tag{38}
\]

dont la variation totale croît quadratiquement. Ainsi une petite oscillation
peut satisfaire le budget BMO tout en fournissant une variation énorme.

Ce n'est pas une réparation PDE gratuite. La seconde dérivée contient un
terme de taille \(s^3\), et, dans

\[
 \Delta(r^{-2}\Omega)
 =r^{-4}(\partial_s^2+3\partial_s+2+\Delta_{S^2})\Omega,
 \tag{39}
\]

elle engendre un résidu visqueux amplifié. Surtout, (34) utilise une variation
non signée : des allers-retours rapides ne produisent le bon signe dans
\(M'\) que si l'anisotropie de \(\Phi\) se synchronise avec eux. Ce raccord
reste une condition supplémentaire falsifiable.

### 5.2 Sauts rares et impulsions minces

Pour un saut isolé de \(a\) vers \(b\) à \(s=s_0\), observé depuis
\(S<s_0\), posons \(d=s_0-S\). Les poids des deux phases sont

\[
 p=e^{-3d},\qquad1-p,
 \tag{40}
\]

et l'oscillation moyenne est exactement

\[
 D_1=2p(1-p)|a-b|.
 \tag{41}
\]

Au choix \(d=(\log2)/3\), elle vaut \(|a-b|/2\). Rendre les sauts rares ne
les cache donc pas aux boules centrées : tout saut d'amplitude fixe situé à
\(s_0\to\infty\) viole le budget logarithmique.

Une impulsion qui retourne à \(a\) après une largeur logarithmique \(\delta\)
est différente. Sa masse radiale maximale est

\[
 p\leq1-e^{-3\delta},
 \tag{42}
\]

et le mélange à deux valeurs vérifie

\[
 D_1\leq2|a-b|(1-e^{-3\delta})=O(|a-b|\delta).
 \tag{43}
\]

Le test **centré** autorise donc des impulsions d'amplitude fixe avec
\(\delta=O(1/s_0)\). Mais un saut discontinu échoue immédiatement sur les
petites boules décentrées traversant la sphère de saut. Après lissage sur une
épaisseur physique \(w\asymp R_*e^{-s_0}\delta\), une boule de taille \(w\)
voit la transition complète et paie un poids
\(s_0+|\log\delta|\). Une impulsion d'amplitude fixe ne satisfait donc pas le
log-BMO global; son amplitude doit elle aussi décroître, sauf annulation
géométrique plus fine.

### 5.3 Axe non unique

Si \(D_1(S)\leq K/S\), alors (4) donne

\[
 1-|m(S)|^2=V_2(S)\leq\frac{2K}{S}.
 \tag{44}
\]

Pour \(S>2K\), la moyenne est non nulle et l'axe
\(m(S)/|m(S)|\) est unique. Une non-unicité persistante de l'axe moyen est
donc incompatible avec la petite oscillation logarithmique. L'axe unique peut
néanmoins dériver sans converger, comme dans (20).

## 6. Certificat reproductible, bibliothèque standard

Le script vérifie les moments exponentiels, les constantes de la rotation
uniforme, la minoration par paires, les bornes de la rotation lente, le saut
équilibré et les coefficients du budget de variation.

```python
from fractions import Fraction as F
from math import e as EULER, exp, factorial, isclose, log, pi, tanh


# T has density 3 exp(-3t): exact polynomial moments.
def moment(k):
    return F(factorial(k), 3 ** k)


assert moment(0) == 1
assert moment(1) == F(1, 3)
assert moment(2) == F(2, 9)
variance_T = moment(2) - moment(1) ** 2
assert variance_T == F(1, 9)

# Independent exponentials: exact moments of T-T'.
mean_abs_difference = F(1, 3)
mean_square_difference = 2 * variance_T
assert mean_square_difference == F(2, 9)

# Constant speed beta=2: exact rotating-frame mean and variance.
beta = F(2)
mean_real = F(9, 9 + beta * beta)
mean_imag = F(3) * beta / (9 + beta * beta)
mean_modulus_squared = mean_real ** 2 + mean_imag ** 2
variance_direction = 1 - mean_modulus_squared
assert mean_modulus_squared == F(9, 13)
assert variance_direction == F(4, 13)
assert variance_direction / 2 == F(2, 13)

# Stronger pairwise lower bound from the Laplace difference law.
beta_float = float(beta)
coth = lambda x: 1.0 / tanh(x)
pair_lower = (
    6 * abs(beta_float) / (36 + beta_float ** 2)
    * coth(3 * pi / abs(beta_float))
)
assert pair_lower > float(variance_direction / 2)

# Slow rotation: pairwise Lipschitz bounds.
# E|T-T'|=1/3 and E|T-T'|^2=2/9 imply (7).
S = F(10)
slow_L1_upper_coefficient = abs(beta) * mean_abs_difference / (1 + S)
slow_L2_variance_upper = (
    F(1, 2) * beta * beta * mean_square_difference / (1 + S) ** 2
)
assert slow_L1_upper_coefficient == F(2, 33)
assert slow_L2_variance_upper == F(4, 1089)

# Exact centered absolute deviation of Exp(3) about its mean.
mean_abs_centered = F(2, 3) / EULER
assert isclose(mean_abs_centered, 2 / (3 * EULER),
               rel_tol=0, abs_tol=1e-15)

# Isolated jump: choose d=log(2)/3, hence p=1/2.
d = log(2) / 3
p = exp(-3 * d)
assert isclose(p, 0.5, rel_tol=0, abs_tol=1e-15)
jump_mean_oscillation_over_distance = 2 * p * (1 - p)
assert isclose(jump_mean_oscillation_over_distance, 0.5,
               rel_tol=0, abs_tol=1e-15)

# Moving-axis moment gate after removing pi:
# alpha=8c/3, speed coefficient=2C, moment range=8C.
c, C, K = F(1, 2), F(2), F(3)
linear_variation_rate = (F(8) * c / 3) / (2 * C)
assert linear_variation_rate == F(1, 3)
moment_range_after_division = (8 * C) / (2 * C)
assert moment_range_after_division == 4

# Small-amplitude high-frequency example:
# amplitude 1/S gives centered S*D1 <=2, despite theta'=O(S).
assert S * (F(2) / S) == 2

print("exponential ball moments and constant rotation: PASS")
print("slow rotation, jumps and axis uniqueness gates: PASS")
print("moving-axis variation budget: PASS")
```

Commande de reproduction : extraire le bloc et exécuter `python -` depuis la
racine du dépôt. Dépendances : bibliothèque standard Python. Graine : aucune.
Les identités décisionnelles sont rationnelles; les trois évaluations
transcendantes ne servent qu'à vérifier leurs substitutions explicites.

## 7. Statut PDE et obligations falsifiables

Les champs de ce rapport sont d'abord des **directions cinématiques**. Ils ne
définissent une vorticité que lorsqu'une magnitude \(\Phi r^{-2}\) leur est
attachée, et cette vorticité doit encore satisfaire la divergence, le flux,
Biot–Savart, l'énergie et l'équation d'évolution. En particulier, une grande
variation de \(e\) n'est ni du stretching favorable ni une compensation
visqueuse démontrée.

```json
{
  "cycle": "0023",
  "direction": "xi(x)=e(log(R*/abs(x)))",
  "claims": [
    {
      "id": "NS-C0023-CONSTANT-SPEED-BMO",
      "status": "REFUTED",
      "statement": "a nonzero constant logarithmic angular speed satisfies centered log-BMO",
      "residual": "D1 >= 6 abs(beta)/(36+beta^2) coth(3 pi/abs(beta))"
    },
    {
      "id": "NS-C0023-LOG-SLOW-DIRECTION",
      "status": "PROVED_FOR_DIRECTION_FIELD",
      "statement": "theta(s)=beta log(1+s) has D1<=abs(beta)/(3(1+S)) and finite local log-BMO"
    },
    {
      "id": "NS-C0023-SLOW-AXIS-SOLENOIDAL",
      "status": "REFUTED_UNDER_NONDEGENERACY",
      "statement": "a speed O(1/s) supplies enough variation to evade the solenoidal moment obstruction with 0<c<=Phi<=C",
      "gate": "integral speed >=(4c/(3C))(T-S)-4-(K/(2pi))log(T/S)"
    },
    {
      "id": "NS-C0023-BMO-CONTROLS-DERIVATIVES",
      "status": "REFUTED",
      "statement": "the centered log-BMO budget controls logarithmic derivatives of the axis",
      "witness": "theta(s)=sin(s^3)/s"
    }
  ],
  "decision": "ABANDON_MONOTONE-SLOW-AXIS_AS_SOLENOIDAL_ESCAPE",
  "next_test": "couple small-amplitude fast phase with anisotropic Phi and measure harmonic and viscous costs"
}
```

## Conclusion

La moyenne de boule ne voit qu'une fenêtre exponentielle de largeur
\(O(1)\) en variable logarithmique. Elle interdit une rotation persistante
d'ordre un par unité de \(s\), mais autorise une dérive sans limite à vitesse
\(1/s\). Cette dérive est trop lente pour payer le déficit solénoïdal d'une
magnitude uniformément critique.

La seule porte encore ouverte est intermittente : petite amplitude et haute
fréquence, éventuellement synchronisées avec une anisotropie de \(\Phi\).
Elle est falsifiable au cycle suivant par la décomposition harmonique de
\(\Phi\xi\) et par le terme \(r^{-4}\partial_s^2\Omega\), qui transforme la
fréquence logarithmique cachée en coût visqueux.
