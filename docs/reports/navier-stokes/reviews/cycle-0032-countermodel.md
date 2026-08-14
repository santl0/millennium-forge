# Cycle 0032 — deux couches axisymétriques décalées

Date : 2026-08-14.

Type de passe : construction non séparable, calcul exact et attaque
contradictoire. Cette passe est une dérivation IA interne, et non une revue
externe indépendante.

## Verdict

Deux couches décalées réalisent un **masquage directionnel réel** : la
composante verticale du curl de la seconde couche peut dominer la
composante radiale produite par la calotte de la première. Une annulation
exacte de deux composantes verticales est aussi possible localement.

Ces deux mécanismes ne franchissent toutefois pas les portes critiques :

1. \(W_r\) et \(W_z\) sont orthogonaux. Ils ne s'annulent jamais entre eux;
   le masquage angulaire exige une composante supplémentaire, qui consomme
   elle-même du budget faible-\(L^{3/2}\);
2. une annulation exacte de \(W_z\) sur un ouvert signifie que la somme des
   potentiels radiaux y est constante; elle crée un plateau
   \(U=C/r\,e_\theta\), mais reporte le curl aux extrémités du plateau;
3. avec deux supports axiaux décalés, une sous-région d'une calotte interne
   peut être masquée par une transition radiale de l'autre couche, mais la
   calotte supérieure de la couche la plus haute et la calotte inférieure
   de la couche la plus basse restent terminales;
4. sur une calotte terminale, la direction du curl vaut exactement
   \(\pm e_r\). Une boule tridimensionnelle de rayon
   \(c\min(a,b)\) conserve donc l'obstruction directionnelle du cycle 0031.

Pour le modèle explicite à deux couches de mêmes épaisseurs \(a,b\), de
translations fixes et d'amplitudes \(V_1,V_2>0\), posons

\[
 V_*=\max(V_1,V_2),
 \qquad
 M=Rab.
 \tag{1}
\]

Des boîtes témoins où une seule transition est active donnent

\[
 \|U\|_{L^{3,\infty}}\asymp V_*M^{1/3},
 \tag{2}
\]

\[
 \|\nabla\times U\|_{L^{3/2,\infty}}
 \geq
 cV_*M^{2/3}\max(a^{-1},b^{-1}).
 \tag{3}
\]

Par conséquent

\[
 \boxed{
 \|U\|_{L^{3,\infty}}
 \leq CK
 \min\left\{
 \left(\frac{a^2}{Rb}\right)^{1/3},
 \left(\frac{b^2}{Ra}\right)^{1/3}
 \right\},
 }
 \tag{4}
\]

où \(K=\|\nabla\times U\|_{L^{3/2,\infty}}\). C'est le même verrou
d'aspect que pour une couche; le décalage ne change aucune puissance.

Le masquage interne a l'angle exact

\[
 \varepsilon
 =
 \frac{|W_r^{(1)}|}{|W_z^{(2)}|}
 =
 \frac{V_1a}{V_2b}.
 \tag{5}
\]

Il peut tendre vers zéro lorsque \(b/a\to\infty\) ou
\(V_2/V_1\to\infty\). Mais (3) augmente alors par la transition radiale ou
la calotte terminale de la couche 2. Le gain directionnel local n'est pas
un gain critique global.

Le résultat scientifique du cycle est négatif mais constructif :

- le premier maillon du masquage non séparable existe exactement;
- une cascade finie à deux niveaux ne se ferme pas;
- l'obstacle précis est la frontière terminale du support et non une
  impossibilité locale de masquer \(e_r\).

## 1. Formulation exacte à deux couches

### 1.1 Potentiel et translations

Écrivons

\[
 U=\psi e_\theta,
 \tag{6}
\]

\[
 \psi(r,z)
 =\frac Rr
 \sum_{i=1}^2
 V_i
 \eta_i\!\left(\frac{r-R-\delta_i}{a_i}\right)
 \chi_i\!\left(\frac{z-\zeta_i}{b_i}\right).
 \tag{7}
\]

Les supports restent dans \(r>R/2\). Les paramètres
\(\delta_i,\zeta_i\) décalent réellement les transitions; si les rapports
\(a_1/a_2\) et \(b_1/b_2\) diffèrent, la somme n'est pas un produit
séparable.

Posons

\[
 s_i=\frac{r-R-\delta_i}{a_i},
 \qquad
 t_i=\frac{z-\zeta_i}{b_i}.
 \tag{8}
\]

Comme

\[
 r\psi
 =R\sum_{i=1}^2V_i\eta_i(s_i)\chi_i(t_i),
 \tag{9}
\]

le curl exact est

\[
 \boxed{
 W_r
 =-\frac Rr
 \sum_{i=1}^2\frac{V_i}{b_i}
 \eta_i(s_i)\chi_i'(t_i),
 }
 \tag{10}
\]

\[
 \boxed{
 W_z
 =\frac Rr
 \sum_{i=1}^2\frac{V_i}{a_i}
 \eta_i'(s_i)\chi_i(t_i).
 }
 \tag{11}
\]

Il n'y a toujours aucun résidu de courbure. La divergence s'annule terme à
terme :

\[
 \frac1r\partial_r(rW_r)+\partial_zW_z=0.
 \tag{12}
\]

### 1.2 Annulations possibles et impossibles

Puisque \(e_r\perp e_z\),

\[
 |W|^2=|W_r|^2+|W_z|^2.
 \tag{13}
\]

Une couche verticale ne peut donc pas annuler une couche radiale. Elle peut
seulement diminuer l'angle radial de la direction normalisée :

\[
 \frac{|W_r|}{|W|}
 =
 \frac{|W_r|}
 {\sqrt{|W_r|^2+|W_z|^2}}.
 \tag{14}
\]

En revanche, les deux contributions à \(W_z\) peuvent s'annuler si

\[
 \frac{V_1}{a_1}\eta_1'\chi_1
 =-\frac{V_2}{a_2}\eta_2'\chi_2.
 \tag{15}
\]

Sur un rectangle où \(\chi_1=\chi_2=1\), \(V_1=V_2=V\) et

\[
 \eta_2=1-\eta_1,
 \tag{16}
\]

on a exactement

\[
 W_z=0,
 \qquad
 r\psi=RV.
 \tag{17}
\]

Ainsi

\[
 U=\frac{RV}{r}e_\theta
 \tag{18}
\]

est non nul et curl-free sur ce rectangle. L'annulation est réelle, mais
(16) ne peut pas être compacte sur toute la droite radiale. Les dérivées
réapparaissent aux deux extrémités de la partition.

## 2. Modèle étagé décalé reproductible

### 2.1 Profil chapeau

Pour rendre les boîtes témoins explicites, utilisons le profil continu
étagé

\[
 H(x)=
 \begin{cases}
 0,&x\leq-2,\\
 x+2,&-2<x<-1,\\
 1,&-1\leq x\leq1,\\
 2-x,&1<x<2,\\
 0,&x\geq2.
 \end{cases}
 \tag{19}
\]

Sa dérivée vaut successivement \(0,1,0,-1,0\). Le modèle n'est pas
\(C^\infty\) aux quatre jonctions. Une mollification sur une fraction fixe
de \(a\) et \(b\) conserve les volumes témoins et toutes les puissances
ci-dessous.

Prenons

\[
 a_1=a_2=a,\qquad b_1=b_2=b,
 \tag{20}
\]

\[
 \eta_1(r)=H((r-R)/a),
 \qquad
 \eta_2(r)=H((r-R-a)/a),
 \tag{21}
\]

\[
 \chi_1(z)=H((z+b)/b),
 \qquad
 \chi_2(z)=H((z-b)/b).
 \tag{22}
\]

Les centres radiaux sont séparés de \(a\), et les centres axiaux de \(2b\).
Les supports se chevauchent mais aucune couche n'est un multiple global de
l'autre.

### 2.2 Boîte de masquage exacte

Dans la boîte

\[
 R-a<r<R,\qquad 0<z<b,
 \tag{23}
\]

on peut choisir un sous-rectangle de proportions fixes où

\[
 \eta_1=1,\quad \eta_1'=0,\quad
 \eta_2'>0,
 \tag{24}
\]

\[
 \chi_1'<0,\quad
 \chi_2=1,\quad\chi_2'=0.
 \tag{25}
\]

Au point central

\[
 r=R-\frac a2,\qquad z=\frac b2,
 \tag{26}
\]

le profil étagé donne exactement

\[
 W_r=\frac Rr\frac{V_1}{b}e_r,
 \qquad
 W_z=\frac Rr\frac{V_2}{a}e_z.
 \tag{27}
\]

L'angle radial vaut

\[
 \frac{|W_r|}{|W|}
 =
 \frac{\varepsilon}{\sqrt{1+\varepsilon^2}},
 \qquad
 \varepsilon=\frac{V_1a}{V_2b}.
 \tag{28}
\]

Le masquage est donc exact et réglable.

### 2.3 Calottes terminales

La couche 1 est la plus basse. Dans sa calotte inférieure, il existe une
boîte où

\[
 \chi_1'\ne0,\qquad
 \chi_2=0,\qquad
 \eta_1=1,\qquad
 \eta_1'=0.
 \tag{29}
\]

La couche 2 est la plus haute. Dans sa calotte supérieure,

\[
 2b<z<3b,
 \tag{30}
\]

et sur son plateau radial, on a

\[
 W=\frac Rr\frac{V_2}{b}e_r
 \tag{31}
\]

à un signe près. Aucune contribution de la couche 1 n'est présente.

Des sous-boîtes des deux calottes internes, proches de \(z=0\), peuvent
être masquées par une transition radiale de l'autre couche. Le profil
explicite ne masque pas leur totalité. Les deux calottes extérieures ne
peuvent même pas bénéficier de ce mécanisme. Ce fait est un ordre de
support : un intervalle compact ayant l'extrémité supérieure maximale n'a
aucune couche placée au-dessus pour masquer sa dernière transition.

### 2.4 Transitions radiales terminales

La transition radiale interne de la couche 1 contient une boîte où
\(\eta_2=0\), et la transition radiale externe de la couche 2 une boîte où
\(\eta_1=0\). Sur des plateaux axiaux correspondants,

\[
 |W_z|
 =\frac Rr\frac{V_i}{a}.
 \tag{32}
\]

Ainsi une annulation locale comme (17) ne supprime pas les deux transitions
radiales terminales.

## 3. Proxies faible-Lorentz

### 3.1 Distribution exacte

Pour

\[
 F(r,z)
 =\sum_{i=1}^2V_i\eta_i(r)\chi_i(z),
 \tag{33}
\]

on a

\[
 |U|=\frac Rr|F|,
 \tag{34}
\]

\[
 |W|^2
 =\left(\frac Rr\right)^2
 \left[
 \left(\sum_iV_i\eta_i\dot\chi_i\right)^2
 +
 \left(\sum_iV_i\dot\eta_i\chi_i\right)^2
 \right],
 \tag{35}
\]

où les points désignent les dérivées dans les variables physiques.

Les fonctions de distribution exactes sont

\[
 \mu_U(\lambda)
 =2\pi\iint
 r\,
 \mathbf1_{\{(R/r)|F|>\lambda\}}
 \,dr\,dz,
 \tag{36}
\]

\[
 \mu_W(\lambda)
 =2\pi\iint
 r\,
 \mathbf1_{\{|W|>\lambda\}}
 \,dr\,dz.
 \tag{37}
\]

Les quasi-normes sont

\[
 \|U\|_{L^{3,\infty}}
 =\sup_{\lambda>0}\lambda\mu_U(\lambda)^{1/3},
 \quad
 \|W\|_{L^{3/2,\infty}}
 =\sup_{\lambda>0}\lambda\mu_W(\lambda)^{2/3}.
 \tag{38}
\]

### 3.2 Boîtes témoins

Le support total a des dimensions comparables à

\[
 R\times a\times b
 \tag{39}
\]

dans les directions azimutale, radiale et axiale. Les translations de
(21)--(22) ne changent le volume que par une constante.

Chaque couche possède une boîte de plateau où l'autre est absente. Sur
celle de la couche d'amplitude \(V_*\),

\[
 |U|\geq cV_*
 \tag{40}
\]

sur un volume \(cRab\). Inversement
\(|U|\leq C(V_1+V_2)\leq2CV_*\) sur un volume \(CRab\). Donc

\[
 cV_*(Rab)^{1/3}
 \leq
 \|U\|_{L^{3,\infty}}
 \leq
 CV_*(Rab)^{1/3}.
 \tag{41}
\]

La transition radiale terminale de cette même couche donne

\[
 \|W\|_{L^{3/2,\infty}}
 \geq
 c\frac{V_*}{a}(Rab)^{2/3}.
 \tag{42}
\]

Sa calotte axiale terminale donne indépendamment

\[
 \|W\|_{L^{3/2,\infty}}
 \geq
 c\frac{V_*}{b}(Rab)^{2/3}.
 \tag{43}
\]

Les boîtes de (42)--(43) sont choisies dans une région où l'autre couche
est identiquement nulle; aucune annulation de quasi-norme n'est invoquée.
Les inégalités (41)--(43) prouvent (3)--(4).

### 3.3 Coût critique du masque

La boîte (23) a un volume \(cRab\). Pour imposer

\[
 |W_r|\leq\varepsilon|W_z|,
 \tag{44}
\]

il faut

\[
 \frac{V_2}{a}
 \geq
 \frac1\varepsilon\frac{V_1}{b}.
 \tag{45}
\]

La même boîte impose alors

\[
 K
 \geq
 c\frac{V_2}{a}(Rab)^{2/3}
 \geq
 \frac c\varepsilon
 \frac{V_1}{b}(Rab)^{2/3}.
 \tag{46}
\]

Augmenter \(V_2\) améliore (28), mais augmente (46) et la calotte
terminale (43). Pour \(V_1=V_2\), on obtient
\(\varepsilon=a/b=A^{-1}\); le grand aspect masque bien la première
calotte, tout en renforçant la contrainte radiale (42).

## 4. Énergie et enstrophie exactes

Pour les profils généraux de (7), définissons les fonctions physiques

\[
 E_i(r)=\eta_i((r-R-\delta_i)/a_i),
 \qquad
 C_i(z)=\chi_i((z-\zeta_i)/b_i).
 \tag{47}
\]

L'énergie contient les termes croisés :

\[
 \boxed{
 \|U\|_2^2
 =
 2\pi R^2
 \sum_{i,j=1}^2V_iV_j
 \left(\int_0^\infty\frac{E_iE_j}{r}\,dr\right)
 \left(\int_{\mathbb R}C_iC_j\,dz\right).
 }
 \tag{48}
\]

Cette matrice de Gram est positive. Pour des amplitudes positives et les
profils décalés (19)--(22),

\[
 \|U\|_2^2\asymp V_*^2Rab.
 \tag{49}
\]

Les composantes du curl étant orthogonales,

\[
 \boxed{
 \begin{aligned}
 \|W\|_2^2
 =2\pi R^2\sum_{i,j=1}^2V_iV_j
 \Bigg[
 &\left(\int_0^\infty\frac{E_iE_j}{r}\,dr\right)
 \left(\int_{\mathbb R}\dot C_i\dot C_j\,dz\right)\\
 +&
 \left(\int_0^\infty\frac{\dot E_i\dot E_j}{r}\,dr\right)
 \left(\int_{\mathbb R}C_iC_j\,dz\right)
 \Bigg].
 \end{aligned}
 }
 \tag{50}
\]

Les termes croisés de (50) peuvent être négatifs et enregistrent les
annulations réelles. La somme totale reste positive. Les boîtes terminales
imposent malgré tout

\[
 \|W\|_2^2
 \geq
 cV_*^2R\left(\frac ab+\frac ba\right)
 \tag{51}
\]

pour le modèle décalé.

Avec énergie cinétique \(E(U)=\frac12\|U\|_2^2\),

\[
 E(U)\asymp V_*^2Rab.
 \tag{52}
\]

Sous la normalisation critique \(K\leq K_0\),

\[
 V_*
 \leq
 CK_0(Rab)^{-2/3}\min(a,b),
 \tag{53}
\]

donc

\[
 E(U)
 \leq
 CK_0^2\frac{\min(a,b)^2}{(Rab)^{1/3}}.
 \tag{54}
\]

## 5. Boules directionnelles

### 5.1 Boule interne masquée

Dans la boîte (23), la direction a la forme

\[
 \xi
 =
 \frac{\varepsilon e_r+e_z}
 {\sqrt{1+\varepsilon^2}},
 \tag{55}
\]

à des facteurs de profil fixes près. Sur une boule de rayon
\(\rho\leq c\min(a,b)\), centrée à distance \(R+O(a)\) de l'axe,

\[
 \operatorname{MO}_B(\xi)
 \asymp
 \frac{\varepsilon}{\sqrt{1+\varepsilon^2}}
 \frac{\rho}{R}.
 \tag{56}
\]

Le masque diminue donc réellement l'oscillation azimutale de la calotte
interne.

### 5.2 Boule terminale

Dans la calotte supérieure de la couche 2, (31) donne
\(\xi=\pm e_r\). Il existe une boule

\[
 \rho=c_0\min(a,b)
 \tag{57}
\]

entièrement contenue dans cette calotte et son plateau radial. Deux
sous-boules azimutalement opposées à l'échelle \(\rho\) donnent

\[
 \operatorname{MO}_{B_\rho}(\xi)
 \geq
 c\min\left\{1,\frac aR,\frac bR\right\}.
 \tag{58}
\]

La même minoration vaut dans la calotte inférieure de la couche 1. Une
extension logarithmique de la direction sur \(\{W=0\}\) ne change pas cette
boule, qui est contenue dans \(\{W\ne0\}\).

Pour la semi-norme log-BMO,

\[
 [\xi]_{\log{\rm BMO}}
 \geq
 c\min\left\{1,\frac aR,\frac bR\right\}
 |\log(c_0\min(a,b))|.
 \tag{59}
\]

En combinant avec (4), toute famille concentrée satisfaisant

\[
 K+[\xi]_{\log{\rm BMO}}\leq C
 \tag{60}
\]

vérifie encore

\[
 \|U\|_{L^{3,\infty}}
 \leq
 CK
 \left[
 1+|\log(c_0\min(a,b))|
 \right]^{-1/3}
 \longrightarrow0.
 \tag{61}
\]

## 6. Diffusion et durée du masque

Les temps visqueux géométriques sont

\[
 \tau_a=\frac{a^2}{\nu},
 \qquad
 \tau_b=\frac{b^2}{\nu},
 \qquad
 \tau_{\rm cross}=\frac{\min(a,b)^2}{\nu}.
 \tag{62}
\]

Le masque de (27) exige que la transition radiale de la couche 2 reste
alignée avec la calotte axiale de la couche 1. La diffusion déplace et
élargit ces deux transitions dès

\[
 t\asymp\tau_{\rm cross}.
 \tag{63}
\]

Si les jonctions du profil étagé sont régularisées sur des épaisseurs
\(\sigma_ra\) et \(\sigma_zb\), leur premier temps diffusif est

\[
 \tau_{\rm smooth}
 =
 \frac1\nu
 \min\{\sigma_r^2a^2,\sigma_z^2b^2\}.
 \tag{64}
\]

Pour une extension directionnelle logarithmique dans un corridor où
\(W=0\),

\[
 h=qe^{-L},
 \qquad
 \tau_h=\frac{q^2}{\nu}e^{-2L}.
 \tag{65}
\]

Une borne log-BMO à poids \(S\) exige \(L\gtrsim S\). Le temps
\(\tau_h\) devient alors exponentiellement plus court que le temps du
profil macroscopique. Le masque est une identité cinématique à \(t=0\);
aucune stabilité par l'évolution de Navier--Stokes n'est démontrée.

## 7. Test standard-library reproductible

Le script vérifie :

- le curl exact sur le profil chapeau;
- la boîte de masquage avec des rationnels;
- la calotte terminale purement \(e_r\);
- une annulation verticale locale avec profils complémentaires;
- les proxies Lorentz et leur optimisation en aspect;
- la géométrie angulaire et l'échelle diffusive.

~~~python
from fractions import Fraction as F
from math import asin, exp, log, sin


def hat(x):
    if x <= -2:
        return F(0)
    if x < -1:
        return x + 2
    if x <= 1:
        return F(1)
    if x < 2:
        return 2 - x
    return F(0)


def hat_prime(x):
    if -2 < x < -1:
        return F(1)
    if 1 < x < 2:
        return F(-1)
    return F(0)


R = F(10)
a = F(1)
b = F(4)
V1 = F(3)
V2 = F(5)


def fields(r, z):
    s1 = (r - R) / a
    s2 = (r - R - a) / a
    t1 = (z + b) / b
    t2 = (z - b) / b

    f = V1 * hat(s1) * hat(t1) + V2 * hat(s2) * hat(t2)
    wr_scalar = -(R / r) * (
        V1 * hat(s1) * hat_prime(t1) / b
        + V2 * hat(s2) * hat_prime(t2) / b
    )
    wz_scalar = (R / r) * (
        V1 * hat_prime(s1) * hat(t1) / a
        + V2 * hat_prime(s2) * hat(t2) / a
    )
    return (R / r) * f, wr_scalar, wz_scalar


# Internal masked cap: layer 1 contributes e_r and layer 2 contributes e_z.
r_mask = R - a / 2
z_mask = b / 2
u_mask, wr_mask, wz_mask = fields(r_mask, z_mask)
assert wr_mask == (R / r_mask) * V1 / b
assert wz_mask == (R / r_mask) * V2 / a
epsilon = abs(wr_mask / wz_mask)
assert epsilon == V1 * a / (V2 * b)

# Terminal top cap of layer 2: no layer 1 and no vertical component.
r_terminal = R + a
z_terminal = F(5, 2) * b
u_terminal, wr_terminal, wz_terminal = fields(
    r_terminal, z_terminal
)
assert wr_terminal == (R / r_terminal) * V2 / b
assert wz_terminal == 0

# A unique inner radial transition of layer 1 witnesses V1/a.
r_inner = R - F(3, 2) * a
z_inner = -b
_, wr_inner, wz_inner = fields(r_inner, z_inner)
assert wr_inner == 0
assert wz_inner == (R / r_inner) * V1 / a

# Local exact W_z cancellation: eta_2=1-eta_1 on a common plateau.
for eta1 in (F(1, 8), F(1, 3), F(2, 3), F(7, 8)):
    eta2 = 1 - eta1
    eta1_prime = F(5, 7)
    eta2_prime = -eta1_prime
    potential_sum = V1 * (eta1 + eta2)
    vertical_curl_sum = V1 * (eta1_prime + eta2_prime)
    assert potential_sum == V1
    assert vertical_curl_sum == 0

# Lorentz proxy with equal scales.  Aspect one maximizes the smaller gate.
for S in (8, 16, 32, 64):
    x = 1.0 / S
    best = -1.0
    for aspect in (1.0, 2.0, S**0.5, float(S)):
        radial_gate = (x / aspect) ** (1.0 / 3.0)
        axial_gate = (x * aspect * aspect) ** (1.0 / 3.0)
        gate = min(radial_gate, axial_gate)
        best = max(best, gate)

        radius = 1.0
        radial_width = x * radius
        axial_width = aspect * radial_width
        volume_scale = radius * radial_width * axial_width
        u_factor = volume_scale ** (1.0 / 3.0)
        wz_factor = volume_scale ** (2.0 / 3.0) / radial_width
        wr_factor = volume_scale ** (2.0 / 3.0) / axial_width
        normalized_u = u_factor / max(wz_factor, wr_factor)
        assert abs(normalized_u - gate) < 2.0e-14

    assert abs(best - x ** (1.0 / 3.0)) < 2.0e-14

# Direction variation in a terminal pure-e_r cap.
for m in (1.0 / 8.0, 1.0 / 16.0, 1.0 / 64.0):
    rho = m
    theta = 2.0 * asin(rho / 4.0)
    point_radius = 2.0 * sin(theta / 2.0)
    direction_gap = 2.0 * sin(theta)
    assert abs(point_radius - rho / 2.0) < 2.0e-15
    assert direction_gap > 0.9 * rho

# Diffusion ratio of a logarithmic corridor.
for depth in (8, 16, 32, 64):
    h_over_q = exp(-float(depth))
    time_ratio = h_over_q * h_over_q
    assert abs(log(time_ratio) + 2.0 * depth) < 3.0e-14

print("two-layer exact mask: PASS")
print("terminal pure-er cap: PASS")
print("local vertical-curl cancellation: PASS")
print("Lorentz aspect obstruction: PASS")
print("direction and diffusion checks: PASS")
~~~

Commande PowerShell de reproduction, depuis la racine du dépôt :

~~~powershell
$text = Get-Content docs/reports/navier-stokes/reviews/cycle-0032-countermodel.md
$start = [Array]::IndexOf($text, '~~~python') + 1
$stop = [Array]::IndexOf($text, '~~~', $start)
$text[$start..($stop - 1)] | python -
~~~

Arithmétique : rationnels exacts pour les champs sur les boîtes témoins et
l'annulation locale; double IEEE 754 pour les racines cubiques, les angles
et la diffusion. Tolérance maximale : \(3\times10^{-14}\). Graine :
aucune. Dépendances : bibliothèque standard Python uniquement.

Le test ne certifie pas un supremum BMO continu ni la stabilité dynamique
du masque.

Exécution locale observée le 2026-08-14 : les identités rationnelles des
deux boîtes et de l'annulation locale sont exactes; les quatre tests
d'aspect, les trois tests angulaires et les quatre profondeurs diffusives
passent avec une tolérance maximale de \(3\times10^{-14}\).

## 8. Passe contradictoire

### 8.1 Le modèle est réellement non séparable

Les translations de (21)--(22) empêchent de factoriser la somme globale en
\(\eta(r)\chi(z)\). Sur la boîte (23), les deux couches contribuent à deux
composantes orthogonales du curl. Le masque n'est donc pas un simple
renommage du produit du cycle 0031.

### 8.2 Les amplitudes inégales ne ferment pas la cascade

Si \(V_2/V_1\) augmente, l'angle (28) diminue. Mais la boîte radiale
terminale et la calotte supérieure portent toutes deux l'amplitude \(V_2\).
Si \(V_1/V_2\) augmente, les boîtes terminales de la couche 1 jouent le même
rôle. L'utilisation de \(V_*=\max(V_1,V_2)\) dans (41)--(43) couvre les
deux cas.

### 8.3 Une annulation locale n'est pas une annulation globale

L'identité (17) construit un plateau curl-free exact. Elle ne donne pas un
champ compact curl-free non nul sur tout \(\mathbb R^3\). Les transitions
terminales sont requises pour passer de \(r\psi=RV\) à zéro. Les boîtes
(32) les détectent sans utiliser une intégration globale ni une constante
non suivie.

### 8.4 Profils lisses

Le chapeau (19) est un proxy continu à dérivée étagée. Une mollification
sur une fraction fixe conserve des sous-boîtes où les dérivées sont
minorées et l'autre couche nulle. Si la mollification occupe une fraction
qui tend vers zéro, le volume témoin diminue mais l'amplitude de dérivée
augmente; l'inégalité de variation totale faible-Lorentz reproduit les
mêmes puissances.

### 8.5 Portée du no-go

Le résultat couvre deux couches à supports rectangulaires décalés possédant
des plateaux et des extrémités ordonnées. Il ne prouve pas qu'un
streamfunction général à frontière méridienne inclinée possède une boule
terminale de capacité polynomiale. Une frontière cuspidale ou une cascade
infinie peut réduire la capacité de la dernière calotte; elle doit payer
séparément sa variation totale, son énergie et son temps diffusif.

### 8.6 Dynamique et problème Clay

Après mollification, \(U\) est une donnée initiale lisse, compacte,
axisymétrique avec swirl et divergence-free sur \(\mathbb R^3\). Ce cycle
ne construit ni une solution ancienne, ni une solution auto-similaire, ni
un résidu Navier--Stokes petit. La pression non locale et l'évolution ne
sont pas calculées.

L'échec du gate faible-\(L^3\) non petit exclut seulement cette famille
comme contre-profil du mécanisme étudié. Il ne résout pas le problème Clay.

## 9. Énoncé falsifiable et décision

### Lemme actif C32

Pour le modèle décalé (19)--(22), il existe des boîtes de volume
\(cRab\) qui donnent (41)--(43), indépendamment du chevauchement interne.
La boîte (23) réalise le masque exact (27), tandis qu'une calotte terminale
réalise (31) et la minoration BMO (58).

Statut : dérivation analytique IA interne, testée par arithmétique exacte
sur les boîtes, sans revue externe indépendante.

Falsificateur décisif : exhiber, avec les profils et translations
(19)--(22), une suite telle que

\[
 \|\nabla\times U_n\|_{L^{3/2,\infty}}
 +[\xi_n]_{\log{\rm BMO}}\leq C,
 \tag{66}
\]

\[
 \min(a_n,b_n)\to0,
 \qquad
 \liminf_n\|U_n\|_{L^{3,\infty}}>0.
 \tag{67}
\]

Une telle suite devrait invalider au moins une boîte terminale explicite.

~~~json
{
  "cycle": "0032",
  "claim": "TWO_LAYER_SHIFTED_AXISYMMETRIC_MASK",
  "status": "LOCAL_MASK_POSITIVE_GLOBAL_TWO_LAYER_NO_GO",
  "equation": "3D incompressible Navier-Stokes initial-data kinematics",
  "domain": "R^3",
  "solution_type": "smooth compact divergence-free initial velocity after fixed mollification",
  "proved": [
    "exact orthogonal mask on an internal cap",
    "exact local cancellation of vertical curl on a complementary radial plateau",
    "terminal radial and axial witness boxes",
    "same weak-Lorentz aspect obstruction as one layer",
    "terminal pure-e_r directional ball"
  ],
  "limits": [
    "piecewise-linear proxy requires fixed mollification",
    "continuous all-ball BMO supremum is not interval-certified",
    "cuspidal boundaries and infinite cascades are not covered",
    "no Navier-Stokes evolution claim"
  ],
  "next_test": "finite-N terminal-cap induction or cuspidal infinite masking cascade"
}
~~~

État : **ABANDONNER** deux couches décalées à extrémités rectangulaires
comme fermeture du masque. **CONSERVER** le masque local (27) comme brique
positive pour une éventuelle cascade.

Prochaine expérience décisive : formaliser par induction l'existence d'au
moins une calotte terminale pour \(N<\infty\) couches ordonnées, puis tester
si une cascade infinie peut faire tendre sa capacité vers zéro sans faire
diverger

\[
 \sum_i
 \left[
 \frac{V_i}{a_i}(Ra_ib_i)^{2/3}
 +
 \frac{V_i}{b_i}(Ra_ib_i)^{2/3}
 \right]
 \tag{68}
\]

ni introduire un temps diffusif nul.
