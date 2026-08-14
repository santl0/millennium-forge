# Cycle 0014 — certificat volume 3D vers ligne 1D

Date de la passe adverse : 2026-08-14.

## Verdict

La restriction géométrique annoncée dans la Définition 7.1 de
[Grujić, arXiv:2607.08866v2](https://arxiv.org/abs/2607.08866v2) est correcte :
si un ensemble mesurable occupe au plus une fraction `delta` d'une boule 3D,
alors il existe une **droite non orientée passant par le centre** sur laquelle
sa densité linéaire est au plus `delta^(1/3)`. La constante est optimale; une
boule concentrique la sature sur toutes les droites.

Pour `delta=3/4`, la constante volumique est exactement

\[
 |B_r|=\frac{4\pi}{3}r^3,
 \qquad
 \delta|B_r|=\frac34\frac{4\pi}{3}r^3=\pi r^3.
 \tag{1}
\]

En revanche, le sens de l'inégalité doit être séparé soigneusement dans le
passage (55)--(56). Si `m=|V_s|`, la majoration globale garantit la
3D-sparseness à tout centre seulement lorsque

\[
 r_s\geq r_{min}:=(m/\pi)^{1/3},
 \tag{2}
\]

et non pour un rayon arbitraire vérifiant une borne supérieure. L'équation
(55) implique bien une **borne supérieure sur ce rayon minimal** :

\[
 r_{min}\leq
 \frac{(C/\pi)^{1/3}}
 {\lambda\|u(s)\|_\infty
  \log(e+\lambda\|u(s)\|_\infty)}.
 \tag{3}
\]

Ainsi, (56) est réparable et compatible avec l'argument d'existence si
`r_s` y désigne explicitement `r_min`, ou mieux le rayon sûr construit depuis
le majorant de (55). Lue comme « tout rayon inférieur au membre droit est
sparse », (56) a le sens faux : la sparseness issue d'un majorant global
s'améliore avec les grands rayons, pas avec les petits.

Le test central exact ci-dessous le montre : une masse `m=pi/8` est
`3/4`-sparse au rayon `1/2`, mais une boule centrale de cette masse remplit
entièrement `B_(1/4)` et n'y est pas sparse. Ce défaut de quantificateur ne
réfute pas à lui seul le théorème 7.4; il impose de remplacer (56) par une
définition constructive et de conserver simultanément la contrainte
`r_min<=r_s<=rho_s`.

Ici, `r_min` signifie le plus petit seuil universel garanti par la seule masse
totale. Un ensemble mieux dispersé peut être sparse à un rayon plus petit; la
boule centrale montre que ce seuil de classe ne peut pas être abaissé.

## 1. Énoncés primaires audités

La v2, datée du 13 juillet 2026, définit :

- la 3D `delta`-sparseness autour de `x_0` au rayon `r` par
  `|S intersection B_r(x_0)|/|B_r|<=delta` ;
- la 1D `delta`-sparseness par l'existence d'une unité `nu` telle que
  `|S intersection (x_0-r nu,x_0+r nu)|/(2r)<=delta` ;
- la conversion revendiquée `delta -> delta^(1/3)` au même rayon ;
- `delta=3/4`, donc une densité linéaire `(3/4)^(1/3)` et une fraction de vide
  `1-(3/4)^(1/3)` ;
- le superniveau
  `V_s={|u(x,s)|>lambda||u(s)||_infinity}`.

L'équation (55) donne

\[
 |V_s|\leq\mathcal M_s:=
 \frac{C}{\lambda^3A_s^3\log^3(e+\lambda A_s)},
 \qquad A_s=\|u(s)\|_\infty.
 \tag{4}
\]

L'équation (56) écrit `r_s<=c_4/[A_s log(e+lambda A_s)]`. La lettre
`M` employée ailleurs dans l'article désigne le majorant holomorphe et fixe
`lambda=1/(2M)`; elle ne doit pas être confondue avec le majorant volumique
`mathcal M_s` de (4).

## 2. Preuve exacte de la conversion 3D vers ligne

Fixons un ensemble mesurable `E`, un centre `x_0` et un rayon `R`. Pour chaque
direction orientée `theta in S2`, posons

\[
 \ell_+(\theta)
 =|\{t\in(0,R):x_0+t\theta\in E\}|.
\]

Sur une demi-droite, la réarrangement croissant du poids `t^2` donne

\[
 \int_{\{t:x_0+t\theta\in E\}}t^2dt
 \geq\int_0^{\ell_+(\theta)}t^2dt
 =\frac{\ell_+(\theta)^3}{3}.
 \tag{5}
\]

Cette inégalité est saturée lorsque l'occupation est collée au centre. Pour
une droite non orientée `[theta]={theta,-theta}`, choisissons un hémisphère
`H` comme ensemble de représentants et posons

\[
 d(\theta)=
 \frac{\ell_+(\theta)+\ell_+(-\theta)}{2R}.
\]

L'identité algébrique

\[
 a^3+b^3-\frac{(a+b)^3}{4}
 =\frac34(a+b)(a-b)^2\geq0
 \tag{6}
\]

permet de **pairer les deux orientations**. Les coordonnées sphériques donnent

\[
 \begin{aligned}
 |E\cap B_R(x_0)|
 &\geq\int_H\frac{\ell_+(\theta)^3+
                         \ell_+(-\theta)^3}{3}\,d\theta\\
 &\geq\frac{2R^3}{3}\int_Hd(\theta)^3\,d\theta.
 \end{aligned}
 \tag{7}
\]

Puisque `|H|=2pi` et `|B_R|=4pi R^3/3`, on obtient

\[
 \frac1{2\pi}\int_Hd(\theta)^3d\theta
 \leq\frac{|E\cap B_R(x_0)|}{|B_R|}.
 \tag{8}
\]

Si le membre droit est au plus `delta`, au moins une droite satisfait
`d(theta)^3<=delta`, donc `d(theta)<=delta^(1/3)`. Cette preuve vaut pour un
ensemble mesurable; l'ouverture du superniveau n'est pas nécessaire.

### Droites orientées et non orientées

Un argument appliqué séparément sur `S2` donne bien l'existence d'une
**demi-droite orientée** de densité au plus `delta^(1/3)`. Mais une bonne
demi-droite peut avoir une demi-droite opposée entièrement occupée. Elle ne
donne pas automatiquement le segment symétrique requis par la Définition 7.1.
Le pairage (6)--(8) est l'étape qui certifie la droite non orientée avec la
même constante.

La direction obtenue peut dépendre du centre `x_0`. C'est compatible avec une
application point par point du principe harmonique après rotation, mais pas
avec un énoncé demandant une direction unique pour tous les points.

## 3. Constante optimale : boule centrale

Posons

\[
 q=(3/4)^{1/3},
 \qquad E_{ball}=B_{qR}(x_0).
\]

Alors

\[
 \frac{|E_{ball}|}{|B_R|}=q^3=3/4,
 \qquad
 \frac{|E_{ball}\cap(x_0-R\theta,x_0+R\theta)|}{2R}=q
 \tag{9}
\]

pour toute direction. Toutes les inégalités (5)--(8) sont des égalités. Aucune
constante strictement inférieure à `delta^(1/3)` ne peut donc suivre du seul
volume.

Les encadrements rationnels

\[
 (9/10)^3<3/4<(10/11)^3
\]

donnent exactement `9/10<q<10/11`. La fraction de vide linéaire
`alpha=1-q` est donc strictement comprise entre `1/11` et `1/10`. La v2 écrit
correctement `|K|>=2R alpha`; le mot « strictement » employé dans la phrase ne
transforme pas ce `>=` en `>`.

## 4. Rayon sûr, majorant global et sens de (56)

Pour `delta=3/4`, un majorant global `|E|<=mathcal M` donne, pour tout centre,

\[
 \frac{|E\cap B_r(x_0)|}{|B_r|}
 \leq\frac{\mathcal M}{(4\pi/3)r^3}
 \leq\frac34
\]

dès que

\[
 r\geq R_{safe}(\mathcal M)
 :=(\mathcal M/\pi)^{1/3}.
 \tag{10}
\]

Cette prescription est uniforme en `x_0`. En substituant (4),

\[
 R_{safe}(\mathcal M_s)
 =\frac{(C/\pi)^{1/3}}
 {\lambda A_s\log(e+\lambda A_s)}.
 \tag{11}
\]

Comme `lambda` est fixé en amont, il peut être absorbé dans `c_4`. La chaîne
géométrique rigoureuse est donc :

```text
|V_s| <= mathcal M_s
  => V_s est 3D-(3/4)-sparse pour tout r >= R_safe(mathcal M_s)
  => il existe à chaque centre une droite (3/4)^(1/3)-sparse
     au rayon choisi r=R_safe(mathcal M_s).
```

Pour entrer dans le disque analytique, il faut ensuite vérifier

\[
 R_{safe}(\mathcal M_s)\leq\rho_s.
 \tag{12}
\]

Si (12) tient, l'intervalle admissible des rayons contient au moins
`[R_safe,rho_s]`. Il n'y a aucune nécessité de choisir un rayon plus petit que
`R_safe`.

Si `mathcal M_s=0`, le superniveau est vide à mesure nulle et tout rayon
positif dans le domaine analytique convient; la formule cubique n'a pas à
produire le rayon interdit `0`.

### Contre-test exact au mauvais sens

Prenons `mathcal M=pi/8`. Le rayon sûr est `R_safe=1/2`, puisque

\[
 (3/4)|B_{1/2}|=\pi/8.
\]

Soit `E` la boule centrale de volume `pi/8`; son rayon `rho` vérifie
`rho^3=3/32`. Alors

\[
 1/4<\rho<1/2.
\]

Au rayon `1/2`, la densité vaut exactement `3/4`. Au rayon `1/4`, pourtant
plus petit que le rayon sûr, `B_(1/4)` est contenu dans `E` et la densité vaut
`1`. Ainsi

```text
r <= R_safe  n'implique pas la sparseness;
r >= R_safe  l'implique depuis le seul majorant global.
```

Verdict sur (55)--(56) : (3) est une borne correcte sur le **plus petit rayon
sélectionné à partir de la masse réelle**, et (11) donne directement un rayon
sûr calculable depuis le majorant. La rédaction de (56) omet ce choix et place
visuellement `<=` après une « exigence » de sparseness, ce qui inverse la
condition suffisante si `r_s` est lu comme un rayon arbitraire. Le raccord est
localement réparable en définissant `r_s:=R_safe(mathcal M_s)`; aucune
réfutation du théorème complet n'est revendiquée sur ce seul point.

## 5. Contre-profils extrémaux et anisotropes

### Coquille concentrique

Soit `sigma=(1/4)^(1/3)` et

\[
 E_{shell}=B_R(x_0)\setminus B_{\sigma R}(x_0).
\]

Son volume relatif est `1-sigma^3=3/4`, mais toutes les droites centrales ont
une densité `1-sigma`. Les encadrements
`(3/5)^3<1/4<(2/3)^3` donnent

\[
 1/3<1-\sigma<2/5<q.
\]

La coquille est donc beaucoup plus sparse en 1D que la boule centrale de même
volume. Elle montre que la position radiale de la masse est essentielle dans
l'inégalité pondérée (5).

### Double cône

Prenons le double cône de sommet `x_0`, tronqué à `R`, dont les deux calottes
directionnelles ont demi-angle `theta` avec `cos(theta)=1/4`. Leur fraction de
surface totale est

\[
 1-\cos\theta=3/4,
\]

donc le cône a une fraction volumique `3/4`. Les droites dont la classe
directionnelle appartient au cône ont une densité `1`; les autres ont une
densité `0`. Le volume n'impose donc rien sur une orientation prescrite, même
s'il garantit l'existence de nombreuses bonnes orientations.

### Tube mince

Dans `B_1(0)`, considérons le cylindre

\[
 T=\{|x_1|<L,\ x_2^2+x_3^2<\varepsilon^2\},
 \qquad L=15/16,\quad\varepsilon=1/8.
\]

Il est contenu dans `B_1` car `L^2+epsilon^2=229/256<1`. Sa fraction volumique
est

\[
 \frac{2\pi L\varepsilon^2}{4\pi/3}=\frac{45}{2048},
\]

mais sa densité sur l'axe `e_1` vaut `L=15/16>q`. Une direction transverse est
au contraire très sparse. Une petite mesure ne permet donc jamais de choisir
la direction avant l'ensemble.

### Ellipsoïde anisotrope

L'ellipsoïde centré d'axes relatifs `(1,1,3/4)` est contenu dans `B_1`, a une
fraction volumique `3/4`, des densités linéaires `1,1,3/4` sur les axes, et
seulement la troisième est inférieure à `q`. Plus généralement, pour des axes
`a_1,a_2,a_3<=1`, le volume relatif est leur produit et les densités axiales
sont les `a_i`. L'inégalité

\[
 \min_i a_i\leq(a_1a_2a_3)^{1/3}
\]

retrouve le bon exposant; l'égalité isotrope redonne la boule saturante.

## 6. Quantificateurs et inégalités strictes

Le lemme utilisable doit conserver l'ordre suivant :

\[
 \forall x_0\ \exists\nu(x_0)
 \quad\text{tel que la section au rayon fixé }r_s\text{ est sparse}.
\]

Les permutations suivantes sont fausses ou non démontrées :

1. `exists nu forall x_0` : le tube et l'ellipsoïde montrent que la bonne
   orientation dépend de la géométrie locale ;
2. `forall nu` : le double cône et le tube ont des orientations entièrement
   occupées ;
3. choisir `r_s` plus petit après avoir obtenu un rayon sûr : le contre-test
   central donne une densité `1` ;
4. remplacer une droite non orientée par une seule bonne demi-droite sans
   pairer l'orientation opposée ;
5. employer le rayon calculé depuis `|E intersection B_r(x_0)|` comme s'il
   était uniforme en `x_0` ; le majorant global est ce qui fournit
   l'uniformité ;
6. déduire une inégalité stricte de `|E|<=mathcal M` : la boule centrale
   réalise l'égalité. Pour obtenir `<3/4`, il faut `r>R_safe` ou une borne
   volumique stricte ;
7. confondre le `M` holomorphe fixé en amont, le maximum `A_s` et le majorant
   volumique `mathcal M_s`.

Le fait que `x_0` soit arbitraire dans le papier est compatible avec le
majorant global de (55), mais la rotation de la ligne doit être refaite pour
chaque point. L'orientation n'est pas un champ global produit par la seule
mesure.

## 7. Obligations machine-readable proposées

```json
{
  "artifact_id": "VOLUME3D-TO-LINE1D-GATE-1",
  "version": 1,
  "source": "arXiv:2607.08866v2, Definition 7.1 and equations (55)-(56)",
  "arithmetic": "Fraction plus one exact cubic algebraic relation q^3=3/4; pi represented by its rational coefficient",
  "parameters": {"delta": "3/4", "ball_volume_coefficient": "4/3"},
  "obligations": [
    {"id": "G1_BALL_CONSTANT", "expected": "delta*(4/3)=1, hence delta*|B_r|=pi*r^3"},
    {"id": "G2_ORIENTED_BATHTUB", "expected": "integral_A t^2 dt >= |A|^3/3"},
    {"id": "G3_PAIRED_CONVEXITY", "expected": "a^3+b^3 >= (a+b)^3/4"},
    {"id": "G4_UNORIENTED_LINE", "expected": "3D density <=delta implies existence of a symmetric line density <=delta^(1/3)"},
    {"id": "G5_SHARPNESS", "expected": "the concentric q-ball, q^3=delta, saturates every direction"},
    {"id": "R1_SAFE_RADIUS", "expected": "global mass <=mathcal_M implies sparseness for r^3>=mathcal_M/pi"},
    {"id": "R2_WRONG_DIRECTION", "expected": "mass pi/8 is sparse at r=1/2 but may have density one at r=1/4"},
    {"id": "R3_EQUATION_56_REPAIR", "expected": "define r_s=(mathcal_M_s/pi)^(1/3), then prove r_s<=rho_s"},
    {"id": "P1_CENTRAL_BALL", "expected": "volume density 3/4 and every line density q"},
    {"id": "P2_SHELL", "expected": "volume density 3/4 and every line density 1-(1/4)^(1/3)<2/5"},
    {"id": "P3_DOUBLE_CONE", "expected": "volume density 3/4; line densities are zero or one"},
    {"id": "P4_TUBE", "expected": "volume density 45/2048; prescribed axial density 15/16>q"},
    {"id": "P5_ELLIPSOID", "expected": "axes (1,1,3/4), volume density 3/4, axial densities (1,1,3/4)"},
    {"id": "Q1_POINT_ORDER", "expected": "for every center there exists a direction; direction may depend on center"},
    {"id": "Q2_NONSTRICT", "expected": "non-strict volume bound yields only non-strict sparseness"},
    {"id": "Q3_MAJORANT_NAMES", "expected": "distinguish analytic M, amplitude A_s and volume majorant mathcal_M_s"}
  ]
}
```

## 8. Certificat Python stdlib exact

Le script utilise `fractions.Fraction`. La constante `pi` n'est jamais
approchée : les volumes sont stockés comme coefficients rationnels de `pi`.
Le nombre `q=(3/4)^(1/3)` est représenté dans l'extension algébrique exacte
`Q[q]/(q^3-3/4)`.

```python
from fractions import Fraction as F

DELTA = F(3, 4)

class Cubic:
    """a+b*q+c*q^2 in Q[q]/(q^3-3/4)."""
    def __init__(self, a=0, b=0, c=0):
        self.coefficients = (F(a), F(b), F(c))

    def __eq__(self, other):
        return isinstance(other, Cubic) and self.coefficients == other.coefficients

    def __add__(self, other):
        return Cubic(*(self.coefficients[i] + other.coefficients[i]
                       for i in range(3)))

    def __mul__(self, other):
        if not isinstance(other, Cubic):
            other = Cubic(other)
        raw = [F(0) for _ in range(5)]
        for i, a in enumerate(self.coefficients):
            for j, b in enumerate(other.coefficients):
                raw[i+j] += a*b
        for degree in (4, 3):
            raw[degree-3] += DELTA*raw[degree]
        return Cubic(raw[0], raw[1], raw[2])

    def __rmul__(self, other):
        return self*other

    def __pow__(self, exponent):
        result, base = Cubic(1), self
        while exponent:
            if exponent & 1:
                result = result*base
            base = base*base
            exponent //= 2
        return result

q = Cubic(0, 1, 0)
assert q**3 == Cubic(DELTA)
assert F(4, 3)*(q**3) == Cubic(1)  # central q-ball has pi coefficient 1

# |B_r|=(4*pi/3)r^3 and delta=3/4.
assert DELTA*F(4, 3) == 1
assert F(9, 10)**3 < DELTA < F(10, 11)**3

def delta_ball_pi_coefficient(r):
    return DELTA*F(4, 3)*r**3

# Exact witness for the direction of the radius inequality.
volume_majorant_pi_coefficient = F(1, 8)
assert delta_ball_pi_coefficient(F(1, 2)) == volume_majorant_pi_coefficient
assert delta_ball_pi_coefficient(F(1, 4)) == F(1, 64)
assert F(1, 64) < volume_majorant_pi_coefficient
central_mass_radius_cubed = F(3, 32)
assert F(1, 4)**3 < central_mass_radius_cubed < F(1, 2)**3

# Shell: sigma^3=1/4, so its volume fraction is 3/4.
assert F(3, 5)**3 < F(1, 4) < F(2, 3)**3

# Double cone: two caps have surface/volume fraction 1-cos(theta)=3/4.
cos_theta = F(1, 4)
assert 1 - cos_theta == DELTA

# Tube in B_1: L=15/16, epsilon=1/8.
L, epsilon = F(15, 16), F(1, 8)
assert L*L + epsilon*epsilon == F(229, 256) < 1
tube_volume_fraction = F(3, 2)*L*epsilon*epsilon
assert tube_volume_fraction == F(45, 2048) < DELTA
assert L > F(10, 11)  # q<10/11<L: the prescribed axis is not q-sparse

# Ellipsoid with relative axes (1,1,3/4).
axes = (F(1), F(1), F(3, 4))
assert axes[0]*axes[1]*axes[2] == DELTA
assert min(axes) < F(9, 10)  # min axis < q since q>9/10

# The exact paired-orientation inequality on rational witnesses.
for denominator in range(1, 17):
    for ia in range(denominator + 1):
        for ib in range(denominator + 1):
            a = F(ia, denominator)
            b = F(ib, denominator)
            assert a**3 + b**3 >= (a+b)**3/F(4)
            assert (a**3 + b**3 - (a+b)**3/F(4)
                    == F(3, 4)*(a+b)*(a-b)**2)

print("ball constant 4*pi/3 and delta=3/4: PASS")
print("central ball/shell/cone/tube/ellipsoid profiles: PASS")
print("oriented-pair convexity and radius-direction gate: PASS")
```

Sortie observée :

```text
ball constant 4*pi/3 and delta=3/4: PASS
central ball/shell/cone/tube/ellipsoid profiles: PASS
oriented-pair convexity and radius-direction gate: PASS
```

Le test n'emploie ni flottant, ni grille, ni graine. La preuve pour tous les
ensembles mesurables est (5)--(8); les boucles finies vérifient la transcription
algébrique et les témoins extrémaux, pas une discrétisation de la sphère.

## 9. Statut scientifique

- conversion `3D delta -> 1D delta^(1/3)` au même centre et au même rayon :
  **DÉRIVATION EXACTE / COMPUTATION_ONLY**, constante optimale ;
- constante `4pi/3` et spécialisation `delta=3/4` : **VÉRIFIÉES** ;
- lecture de (56) comme condition suffisante pour un rayon arbitrairement plus
  petit : **REFUTED** par la boule centrale ;
- lecture existentielle « le rayon minimal est majoré par le membre droit » :
  **VALIDE**, mais doit être explicitée ;
- théorème 7.4 de la prépublication : **NON RÉFUTÉ PAR CE MAILLON SEUL** et
  toujours `PREPRINT_CLAIM / NEEDS_INDEPENDENT_CHECK` dans le laboratoire.

Décision : **RÉVISER** le raccord (55)--(56), sans abandonner la conversion
géométrique. La version auditée doit définir

\[
 r_s:=R_{safe}(\mathcal M_s)
 =\frac{(C/\pi)^{1/3}}
 {\lambda A_s\log(e+\lambda A_s)},
\]

prouver `r_s<=rho_s`, puis appliquer (8) séparément à chaque centre avec une
direction dépendant de ce centre. Une revendication plus forte — rayon plus
petit, direction globale, toutes les orientations ou stricte sparseness — est
exclue par les contre-profils conservés ici.
