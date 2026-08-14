# Cycle 0033 — plateau épais à retour rare

Date : 2026-08-14.

Type de passe : contre-profil compact, calcul de distributions et attaque
adversariale. Cette passe est une dérivation IA interne, et non une revue
externe indépendante.

## Verdict

Une section méridienne authentiquement épaisse permet de garder
simultanément une vitesse faible-\(L^3\) non petite et un curl
faible-\(L^{3/2}\) borné **si le retour occupe une fraction fixe**. Mais la
direction du retour possède alors une oscillation d'ordre un à l'échelle
physique de la section, et le poids logarithmique diverge.

Rendre le retour rare réfute bien une obstruction BMO fondée seulement sur
deux directions terminales antipodales. Un plateau compact entouré d'une
coquille de retour de fraction

\[
 \delta=h/R
 \tag{1}
\]

admet une extension directionnelle globale dont la BMO non pondérée est

\[
 O\!\left(\frac1L\right),
 \qquad
 L=\log(R/h)=\log(1/\delta).
 \tag{2}
\]

Les deux endpoints ne suffisent donc pas : leur capacité et les corridors
de zéros sont décisifs.

Ce gain directionnel a cependant un coût critique exact. Soit
\(\mathcal R=\Lambda R\), \(\Lambda>4\), le rayon majeur du tore. Pour le
modèle construit ci-dessous,

\[
 K_u:=\|U\|_{L^{3,\infty}}
 \asymp VR\Lambda^{1/3},
 \tag{3}
\]

\[
 K_w:=\|\nabla\times U\|_{L^{3/2,\infty}}
 \asymp
 VR\Lambda^{2/3}\delta^{-1/3}.
 \tag{4}
\]

Par suite

\[
 \boxed{
 K_u\leq C K_w
 \Lambda^{-1/3}\delta^{1/3}.
 }
 \tag{5}
\]

Pour que l'extension de (2) reste uniformément log-BMO lorsque
\(R\to0\), il faut

\[
 L\gtrsim|\log R|,
 \qquad
 \delta\lesssim e^{-c|\log R|}.
 \tag{6}
\]

Sous \(K_w\leq K\), (5) impose alors

\[
 K_u
 \leq CK\Lambda^{-1/3}
 e^{-c|\log R|/3}
 \longrightarrow0.
 \tag{7}
\]

Inversement, normaliser \(K_u\geq\kappa>0\) fait diverger \(K_w\) comme
\(\delta^{-1/3}\).

Décision :

- **réfutée** : toute minoration BMO universelle utilisant seulement
  l'existence de deux directions antipodales;
- **abandonnée** : la coquille rare d'un plateau épais comme moyen de
  satisfaire simultanément \(K_u\geq\kappa\), \(K_w\leq K\) et log-BMO
  uniforme;
- **ouverte** : une fonction compacte générale dont les retours ont une
  distribution multi-échelle non comparable à une coquille.

## 1. Modèle compact exact

### 1.1 Géométrie

En coordonnées cylindriques, fixons

\[
 \mathcal R=\Lambda R,\qquad
 \Lambda>4,\qquad
 0<h<R/2.
 \tag{8}
\]

La distance méridienne au cercle central est

\[
 s(r,z)=\sqrt{(r-\mathcal R)^2+z^2}.
 \tag{9}
\]

Définissons le plateau à retour linéaire

\[
 A_{R,h}(s)=
 \begin{cases}
 1,&0\leq s\leq R-h,\\[1mm]
 (R-s)/h,&R-h<s<R,\\[1mm]
 0,&s\geq R.
 \end{cases}
 \tag{10}
\]

Puis

\[
 U=\psi e_\theta,
 \qquad
 \psi(r,z)=V\frac{\mathcal R}{r}A_{R,h}(s).
 \tag{11}
\]

Le champ est compact, divergence-free et nul près de l'axe. Le profil
étagé est lipschitzien. Une mollification des deux jonctions sur une
fraction fixée de \(h\) conserve toutes les puissances et les sous-régions
utilisées.

La section formelle du support est le disque \(s<R\), d'aire

\[
 \pi R^2.
 \tag{12}
\]

La région où \(U\) atteint son plateau a l'aire

\[
 \pi(R-h)^2\asymp R^2.
 \tag{13}
\]

Le support n'est donc pas épaissi par une queue de petite amplitude : une
fraction tendant vers un du disque porte \(|U|\asymp V\).

### 1.2 Volumes exacts

Par le théorème de Pappus, le volume du tore plein est

\[
 |\mathcal T_R|
 =2\pi^2\mathcal R R^2.
 \tag{14}
\]

Le plateau et la coquille ont respectivement

\[
 |\mathcal P_{R,h}|
 =2\pi^2\mathcal R(R-h)^2,
 \tag{15}
\]

\[
 |\mathcal S_{R,h}|
 =2\pi^2\mathcal R(2Rh-h^2).
 \tag{16}
\]

Ainsi

\[
 |\mathcal S_{R,h}|
 \asymp\Lambda R^3\delta,
 \qquad
 |\mathcal P_{R,h}|
 \asymp\Lambda R^3.
 \tag{17}
\]

## 2. Curl et direction

Comme

\[
 r\psi=V\mathcal R A_{R,h}(s),
 \tag{18}
\]

le terme de courbure s'annule exactement. On obtient

\[
 W_r=-\partial_z\psi
 =-V\frac{\mathcal R}{r}A'(s)\frac zs,
 \tag{19}
\]

\[
 W_z=\frac1r\partial_r(r\psi)
 =V\frac{\mathcal R}{r}A'(s)
 \frac{r-\mathcal R}{s}.
 \tag{20}
\]

Dans la coquille,

\[
 A'(s)=-1/h,
 \qquad
 |W|=\frac Vh\frac{\mathcal R}{r}.
 \tag{21}
\]

Le curl est nul dans le plateau et à l'extérieur. Sur la coquille, sa
direction vaut

\[
 \xi
 =\frac W{|W|}
 =
 \frac zs e_r
 -\frac{r-\mathcal R}{s}e_z.
 \tag{22}
\]

Avec

\[
 r-\mathcal R=s\cos\varphi,\qquad
 z=s\sin\varphi,
 \tag{23}
\]

on a

\[
 \xi(\varphi,\theta)
 =\sin\varphi\,e_r(\theta)-\cos\varphi\,e_z.
 \tag{24}
\]

La direction parcourt notamment les valeurs antipodales \(e_z\) et
\(-e_z\). Elle tourne une fois autour de la section méridienne.

## 3. Fonctions de distribution totales

### 3.1 Coordonnées toriques

Le jacobien exact est

\[
 dx
 =(\mathcal R+s\cos\varphi)s\,
 ds\,d\varphi\,d\theta.
 \tag{25}
\]

La distribution complète de la vitesse est

\[
 \begin{aligned}
 \mu_U(\lambda)
 =\int_0^R\int_0^{2\pi}\int_0^{2\pi}
 &(\mathcal R+s\cos\varphi)s\\
 {}\times&
 \mathbf1_{\left\{
 V\frac{\mathcal R}{\mathcal R+s\cos\varphi}
 A_{R,h}(s)>\lambda
 \right\}}
 \,d\theta\,d\varphi\,ds.
 \end{aligned}
 \tag{26}
\]

La distribution totale du curl est

\[
 \begin{aligned}
 \mu_W(\lambda)
 =\int_{R-h}^R\int_0^{2\pi}\int_0^{2\pi}
 &(\mathcal R+s\cos\varphi)s\\
 {}\times&
 \mathbf1_{\left\{
 \frac Vh\frac{\mathcal R}
 {\mathcal R+s\cos\varphi}>\lambda
 \right\}}
 \,d\theta\,d\varphi\,ds.
 \end{aligned}
 \tag{27}
\]

Ces formules incluent tout le tore; aucune section méridienne ni aucun
niveau d'amplitude n'est omis.

### 3.2 Encadrements faibles

Pour \(\Lambda>4\) et \(s<R\),

\[
 \frac{\Lambda}{\Lambda+1}
 \leq\frac{\mathcal R}{r}
 \leq\frac{\Lambda}{\Lambda-1}.
 \tag{28}
\]

Les volumes (14)--(16) et les niveaux (28) donnent

\[
 cVR\Lambda^{1/3}
 \leq K_u
 \leq CVR\Lambda^{1/3},
 \tag{29}
\]

\[
 c\frac Vh(\Lambda R^2h)^{2/3}
 \leq K_w
 \leq
 C\frac Vh(\Lambda R^2h)^{2/3}.
 \tag{30}
\]

Après \(h=\delta R\), (30) devient (4). Les constantes sont uniformes en
\(R,h,V\) et \(\Lambda\geq4+\varepsilon\).

Le quotient exact des puissances est

\[
 \frac{K_u}{K_w}
 \asymp
 \Lambda^{-1/3}\left(\frac hR\right)^{1/3}.
 \tag{31}
\]

Un retour rare n'est donc pas gratuit : son amplitude \(V/h\) compense plus
que son petit volume \(\Lambda R^2h\) dans l'exposant faible
\(3/2\).

## 4. Énergie et enstrophie

L'intégrale classique

\[
 \int_0^{2\pi}
 \frac{d\varphi}{\mathcal R+s\cos\varphi}
 =
 \frac{2\pi}{\sqrt{\mathcal R^2-s^2}}
 \tag{32}
\]

donne l'énergie exacte

\[
 \boxed{
 \|U\|_2^2
 =
 4\pi^2V^2\mathcal R^2
 \int_0^R
 \frac{A_{R,h}(s)^2s}
 {\sqrt{\mathcal R^2-s^2}}\,ds.
 }
 \tag{33}
\]

Ainsi

\[
 \|U\|_2^2\asymp V^2\Lambda R^3.
 \tag{34}
\]

Le même calcul appliqué à (21) donne

\[
 \boxed{
 \|W\|_2^2
 =
 \frac{4\pi^2V^2\mathcal R^2}{h^2}
 \left[
 \sqrt{\mathcal R^2-(R-h)^2}
 -\sqrt{\mathcal R^2-R^2}
 \right].
 }
 \tag{35}
\]

En particulier,

\[
 \|W\|_2^2
 \asymp
 \frac{V^2\Lambda R}{\delta}.
 \tag{36}
\]

Sous la normalisation \(K_u\asymp1\), on a
\(V\asymp R^{-1}\Lambda^{-1/3}\), donc

\[
 \|U\|_2^2\asymp R\Lambda^{1/3},
 \qquad
 \|W\|_2^2
 \asymp
 R^{-1}\Lambda^{1/3}\delta^{-1}.
 \tag{37}
\]

L'énergie tend vers zéro lorsque \(R\to0\) à \(\Lambda\) modéré, tandis que
l'enstrophie diverge.

## 5. Extension directionnelle et réfutation des endpoints

### 5.1 Pourquoi les endpoints ne suffisent pas

Les directions (24) ont un écart d'ordre un, mais elles vivent sur une
coquille de fraction volumique \(\delta\). Entre la coquille et le coeur,
ainsi qu'à l'extérieur du support, \(W=0\). La direction y est libre, sous
la contrainte d'utiliser une seule extension unitaire globale.

La boucle

\[
 (\varphi,\theta)
 \longmapsto
 \sin\varphi\,e_r(\theta)-\cos\varphi\,e_z
 \tag{38}
\]

a degré nul comme application du tore vers \(S^2\). Elle est donc
homotope à une direction constante. Fixons une homotopie lipschitzienne
une fois pour toutes.

Dans les deux corridors de zéros, faisons avancer cette homotopie selon la
distance \(d\) à la coquille, avec le paramètre tronqué

\[
 \alpha(d)=
 \begin{cases}
 0,&0\leq d\leq h,\\[1mm]
 \displaystyle
 \frac{\log(d/h)}{\log(q/h)},&h<d<q,\\[2mm]
 1,&d\geq q,
 \end{cases}
 \tag{39}
\]

où \(q=cR\). Sur la coquille, l'extension coïncide avec (24); à distance
\(q\), elle est constante.

Le logarithme tronqué vérifie une borne BMO uniforme avant division par
\(L=\log(q/h)\). Une analyse par tailles de boules donne

\[
 \sup_B\operatorname{MO}_B(\widetilde\xi)
 \leq C\left(\frac1L+\frac hR\right).
 \tag{40}
\]

En effet :

- pour \(\rho\leq h\), la variation tangentielle est
  \(O(\rho/R+\rho/\mathcal R)\);
- pour \(h<\rho<q\), la variation logarithmique coûte \(C/L\), et la
  courbure est multipliée par la part non contractée de l'homotopie;
- pour \(\rho\geq q\), l'intégrale de la déviation dans le corridor est
  \(O(q/L)\) par unité de surface et se dilue;
- les boules contenant le tore entier ne voient que la fraction
  \(O(1/L)\) où l'extension diffère substantiellement de la constante.

Ainsi, pour \(\delta=e^{-L}\), la BMO tend vers zéro malgré la présence de
directions antipodales exactes. Une minoration universelle

\[
 \{\text{deux endpoints antipodaux}\}
 \Longrightarrow
 \|\widetilde\xi\|_{\rm BMO}\geq c
 \tag{41}
\]

est fausse sans hypothèse de capacité.

### 5.2 Poids logarithmique physique

La plus petite boule pertinente a un rayon comparable à \(h\). Le poids
maximal est

\[
 |\log h|
 =|\log R|+L+O(1).
 \tag{42}
\]

Les estimations (40)--(42) donnent

\[
 [\widetilde\xi]_{\log{\rm BMO}}
 \leq
 C\frac{|\log R|+L}{L}
 +C\delta|\log h|.
 \tag{43}
\]

Choisir

\[
 L\geq c|\log R|
 \tag{44}
\]

rend (43) uniforme. Cette construction répond positivement à la question
directionnelle seule : il existe au moins une extension all-ball
admissible.

Elle répond négativement à la question simultanée. Par (5),

\[
 K_w\leq K
 \quad\Longrightarrow\quad
 K_u\leq
 CK\Lambda^{-1/3}e^{-L/3}.
 \tag{45}
\]

Avec (44), le membre droit tend vers zéro.

## 6. Retours épais, rares et rayon majeur

Le compromis peut se lire sans choisir \(L\).

### Retour épais

Si \(\delta\geq c>0\) et \(\Lambda\asymp1\), (3)--(4) permettent
\(K_u\asymp K_w\asymp1\). Mais la coquille occupe une fraction fixe des
boules de rayon \(R\), et sa direction tourne d'un angle d'ordre un. La
semi-norme log-BMO croît comme \(|\log R|\).

### Retour rare

Si \(\delta\to0\), l'extension (39) réduit l'oscillation, mais

\[
 K_w/K_u\asymp\Lambda^{1/3}\delta^{-1/3}.
 \tag{46}
\]

### Grand rayon majeur

Augmenter \(\Lambda=\mathcal R/R\) réduit la variation azimutale locale de
\(e_r\), mais augmente le volume du tore. Même sans retour rare,

\[
 K_u/K_w\lesssim\Lambda^{-1/3}.
 \tag{47}
\]

La géométrie ne fournit donc aucune troisième échappatoire.

## 7. Composants séparés

Considérons \(N\) copies disjointes de mêmes \(R,\Lambda,h,V\). Dans le
modèle étagé, leurs distributions s'additionnent exactement. On obtient

\[
 K_u^{(N)}
 \asymp
 VR\Lambda^{1/3}N^{1/3},
 \tag{48}
\]

\[
 K_w^{(N)}
 \asymp
 VR\Lambda^{2/3}\delta^{-1/3}N^{2/3}.
 \tag{49}
\]

Donc

\[
 \frac{K_u^{(N)}}{K_w^{(N)}}
 \asymp
 N^{-1/3}\Lambda^{-1/3}\delta^{1/3}.
 \tag{50}
\]

Les corridors de zéros permettent de construire les homotopies
directionnelles composant par composant, puis de les raccorder à la même
direction extérieure. Mais le nombre croissant de composants rend le
rapport critique plus petit, et non plus grand.

Pour des amplitudes \(V_j\) inégales à échelle fixe, les distributions
prennent la forme

\[
 \mu_U(\lambda)
 \asymp
 \Lambda R^3
 \#\{j:V_j\gtrsim\lambda\},
 \tag{51}
\]

\[
 \mu_W(\lambda)
 \asymp
 \Lambda R^3\delta
 \#\{j:V_j/(R\delta)\gtrsim\lambda\}.
 \tag{52}
\]

Une forte concentration des amplitudes ramène à un nombre borné de
composants; une distribution diffuse paie le facteur de comptage
\(N^{2/3}\) dans le curl.

## 8. Support épais artificiel et queues

Le support topologique n'est pas une quantité de distribution. Pour le
voir exactement, considérons un modèle à deux amplitudes dans un volume
total \(C R^3\) :

- amplitude \(V\) sur une fraction \(\mu\);
- amplitude \(\tau V\), \(0<\tau<1\), sur la fraction \(1-\mu\).

La distribution totale est

\[
 \mu_U(\lambda)
 =
 CR^3\left[
 \mu\mathbf1_{\{\lambda<V\}}
 +(1-\mu)\mathbf1_{\{\lambda<\tau V\}}
 \right].
 \tag{53}
\]

Par conséquent,

\[
 \boxed{
 \|U\|_{L^{3,\infty}}
 =
 C^{1/3}VR
 \max\{\mu^{1/3},\tau\}.
 }
 \tag{54}
\]

Si

\[
 \tau\ll\mu^{1/3},
 \tag{55}
\]

la queue épaissit le support formel sans contribuer au gate \(K_u\). La
bonne échelle active est celle du coeur, pas le diamètre de
\(\operatorname{supp}U\).

Si \(\tau\gtrsim\mu^{1/3}\), la queue contribue réellement à \(K_u\). Elle
doit alors être fermée vers zéro et crée son propre curl. Elle ne peut être
ignorée dans \(\mu_W\).

Le modèle (10) évite cette ambiguïté : son plateau de niveau un occupe
\((1-\delta)^2\) de la section.

## 9. Temps diffusifs

Les deux temps géométriques sont

\[
 \tau_R=\frac{R^2}{\nu},
 \qquad
 \tau_h=\frac{h^2}{\nu}
 =\frac{R^2}{\nu}e^{-2L}.
 \tag{56}
\]

La coquille rare est modifiée par la diffusion dès \(t\asymp\tau_h\).
Sous la condition log-BMO (44),

\[
 \tau_h
 \leq
 \frac{R^2}{\nu}
 e^{-c|\log R|}.
 \tag{57}
\]

Le temps directionnel devient donc beaucoup plus court que le temps
diffusif macroscopique \(\tau_R\). L'extension BMO vit dans les corridors de
zéros; elle n'empêche pas la chaleur de mélanger le plateau et le retour.

## 10. Test standard-library reproductible

Le script vérifie :

- les volumes exacts du plateau et de la coquille;
- les exposants des proxies faible-Lorentz;
- le coût de \(N\) composants;
- la distribution totale du modèle coeur--queue;
- la variance exacte du logarithme tronqué sur une grille d'intervalles;
- le temps diffusif du corridor.

La variance majore l'oscillation moyenne. Pour

\[
 g_L(x)=
 \begin{cases}
 0,&0\leq x\leq e^{-L},\\
 (\log x+L)/L,&e^{-L}<x\leq1,
 \end{cases}
 \tag{58}
\]

le test retrouve

\[
 \sup_I\sqrt{\operatorname{Var}_I(g_L)}
 \leq\frac{1+10^{-11}}L
 \tag{59}
\]

sur tous les intervalles dont les extrémités appartiennent à une grille
géométrique de 65 niveaux.

~~~python
from fractions import Fraction as F
from math import exp, log, sqrt


max_exact_residual = F(0)

# Exact torus-volume coefficients after removing the common factor 2*pi^2.
for n in (4, 8, 16, 32):
    radius = F(1, 2**n)
    major_ratio = F(5)
    major_radius = major_ratio * radius
    delta = F(1, 2**n)
    thickness = delta * radius

    total = major_radius * radius * radius
    plateau = major_radius * (radius - thickness) ** 2
    shell = major_radius * (
        2 * radius * thickness - thickness * thickness
    )
    residual = total - plateau - shell
    assert residual == 0
    max_exact_residual = max(max_exact_residual, abs(residual))

    # Cubes of the critical proxies, with profile constants suppressed.
    velocity_cube = (
        radius**3 * major_ratio
    )
    curl_cube = (
        radius**3 * major_ratio**2 / delta
    )
    ratio_cube = velocity_cube / curl_cube
    assert ratio_cube == delta / major_ratio

# N equal separated components add N to both distribution volumes.
for component_count in (1, 8, 64, 512):
    ku_factor = component_count ** (1.0 / 3.0)
    kw_factor = component_count ** (2.0 / 3.0)
    ratio = ku_factor / kw_factor
    assert abs(
        ratio - component_count ** (-1.0 / 3.0)
    ) < 2.0e-14

# Exact two-level distribution: only the two jump levels can maximize it.
for denominator in (8, 32, 128):
    mu = F(1, denominator)
    tau = F(1, denominator)
    velocity = F(7, 3)
    total_volume = F(5, 2)

    core_candidate_cube = velocity**3 * total_volume * mu
    tail_candidate_cube = (
        tau**3 * velocity**3 * total_volume
    )
    exact_weak_cube = max(core_candidate_cube, tail_candidate_cube)
    formula_cube = (
        velocity**3
        * total_volume
        * max(mu, tau**3)
    )
    residual = exact_weak_cube - formula_cube
    assert residual == 0
    max_exact_residual = max(max_exact_residual, abs(residual))


def integral_log(x):
    if x == 0.0:
        return 0.0
    return x * log(x) - x


def integral_log_squared(x):
    if x == 0.0:
        return 0.0
    lx = log(x)
    return x * (lx * lx - 2.0 * lx + 2.0)


def clipped_log_variance(left, right, inner, depth):
    length = right - left
    active_left = max(left, inner)
    if right <= active_left:
        return 0.0

    log_inner = log(inner)
    first = (
        integral_log(right)
        - integral_log(active_left)
        - log_inner * (right - active_left)
    ) / depth
    second = (
        integral_log_squared(right)
        - integral_log_squared(active_left)
        - 2.0
        * log_inner
        * (
            integral_log(right)
            - integral_log(active_left)
        )
        + log_inner**2 * (right - active_left)
    ) / depth**2

    mean = first / length
    return max(0.0, second / length - mean * mean)


max_scaled_standard_deviation = 0.0
for depth in (8, 16, 32, 64):
    inner = exp(-float(depth))
    endpoints = [0.0, inner] + [
        inner * exp(depth * k / 64.0)
        for k in range(1, 65)
    ]
    maximum = 0.0
    for index, left in enumerate(endpoints[:-1]):
        for right in endpoints[index + 1:]:
            variance = clipped_log_variance(
                left, right, inner, float(depth)
            )
            maximum = max(maximum, sqrt(variance))

    scaled = depth * maximum
    max_scaled_standard_deviation = max(
        max_scaled_standard_deviation, scaled
    )
    assert scaled <= 1.0 + 1.0e-11

    diffusion_ratio = inner * inner
    assert abs(
        log(diffusion_ratio) + 2.0 * depth
    ) < 3.0e-14

print("maximum exact algebraic residual:", max_exact_residual)
print(
    "maximum depth times log standard deviation: %.12f"
    % max_scaled_standard_deviation
)
print("thick-support Lorentz tradeoff: PASS")
print("separated-component distribution: PASS")
print("core-tail total distribution: PASS")
print("log-corridor and diffusion checks: PASS")
~~~

Commande PowerShell de reproduction, depuis la racine du dépôt :

~~~powershell
$text = Get-Content docs/reports/navier-stokes/reviews/cycle-0033-countermodel.md
$start = [Array]::IndexOf($text, '~~~python') + 1
$stop = [Array]::IndexOf($text, '~~~', $start)
$text[$start..($stop - 1)] | python -
~~~

Arithmétique : rationnels exacts pour les volumes, les puissances critiques
et la distribution coeur--queue; double IEEE 754 pour les racines, les
logarithmes et les temps diffusifs. Tolérance maximale :
\(3\times10^{-14}\), sauf la marge explicite \(10^{-11}\) du proxy BMO.
Graine : aucune. Dépendances : bibliothèque standard Python uniquement.

Le test de variance porte sur une grille géométrique et n'est pas une
certification par intervalles du supremum BMO tridimensionnel. La borne
analytique (40), et non cette grille, porte le quantificateur all-ball.

Exécution locale observée le 2026-08-14 : résidu algébrique maximal nul;
maximum observé de
\(L\sqrt{\operatorname{Var}_I(g_L)}=1.000000000000341\);
les quatre profondeurs, quatre nombres de composants et trois distributions
coeur--queue passent.

## 11. Passe contradictoire

### 11.1 Une extension, pas toutes

La construction (39) prouve l'existence d'une extension globale à faible
BMO. Elle ne dit pas que toute extension est bonne. Le prolongement brutal
par une direction constante crée des interfaces d'ordre un.

La minoration de type endpoints est réfutée dans sa forme universelle sur
toutes les extensions : les endpoints prescrits admettent au moins une
extension logarithmique de coût \(C/L\).

### 11.2 Homotopie et constante all-ball

La boucle (38) a bien degré nul, mais une homotopie lipschitzienne explicite
n'est pas discrétisée dans le test. La constante \(C\) de (40) dépend de ce
choix et de la géométrie du tore; elle n'est pas certifiée numériquement.
Une singularité cachée de l'homotopie invaliderait la majoration, pas le
calcul Lorentz (3)--(5).

### 11.3 Lissage

Le profil (10) est seulement lipschitzien. Un lissage fixe près de
\(s=R-h,R\) conserve une coquille de volume comparable et une dérivée
comparable à \(1/h\). Si la zone de lissage devient beaucoup plus mince que
\(h\), son propre budget faible-\(L^{3/2}\) doit être ajouté.

### 11.4 Pression et évolution

Le modèle est une donnée initiale cinématique. La pression non locale, le
terme convectif et la diffusion à temps positif ne sont pas équilibrés.
Aucun résidu Navier--Stokes petit, aucune solution ancienne et aucun
blow-up admissible ne sont construits.

### 11.5 Portée du no-go

L'obstruction simultanée est démontrée pour :

- un plateau de niveau non dégénéré sur une section d'aire
  \(\asymp R^2\);
- un retour porté par une coquille de largeur comparable à \(h\);
- un rayon majeur \(\mathcal R=\Lambda R\);
- un nombre fini ou un nombre croissant de copies égales séparées.

Elle ne couvre pas une distribution continue d'amplitudes et d'épaisseurs,
une frontière cuspidale, des rayons de composants tous différents, ni une
cascade infinie où aucune coquille ne porte une fraction fixée de la
variation totale.

### 11.6 Support versus support effectif

Toute revendication utilisant seulement
\(|\operatorname{supp}F|\asymp R^2\) est invalide face à (53)--(55). Il
faut imposer un plateau de niveau fixé, ou enregistrer toute la fonction de
distribution. Le modèle principal satisfait cette exigence par (13).

## 12. Énoncés falsifiables

### Résultat négatif C33-A

Pour le plateau torique (10)--(11), les distributions exactes (26)--(27)
impliquent (5). Si une extension du type homotopie logarithmique satisfait
une borne log-BMO uniforme sous \(R\to0\), alors \(K_w\leq K\) implique
\(K_u\to0\).

Falsificateur : une suite de paramètres
\((R,h,\Lambda,V)\) dans ce modèle telle que

\[
 R\to0,\qquad
 K_u\geq\kappa,\qquad
 K_w\leq K,
 \tag{60}
\]

et (43) reste bornée. Elle contredirait directement le quotient (31).

### Résultat positif C33-B

Deux directions antipodales portées par une coquille de capacité
\(\delta=e^{-L}\) n'imposent pas une BMO d'ordre un : elles admettent une
extension globale de coût \(C/L\).

Falsificateur : démontrer que toute homotopie globale prolongeant (24)
possède une boule de moyenne oscillation \(\geq c>0\), uniformément en
\(L\), malgré les deux corridors de zéros.

~~~json
{
  "cycle": "0033",
  "claim": "THICK_PLATEAU_RARE_RETURN_TRADEOFF",
  "status": "ENDPOINT_BMO_LOWER_REFUTED_SIMULTANEOUS_GATE_NO_GO",
  "equation": "3D incompressible Navier-Stokes initial-data kinematics",
  "domain": "R^3",
  "solution_type": "compact pure-swirl initial velocity after mollification",
  "proved": [
    "exact total distributions for toroidal plateau and shell return",
    "Ku over Kw scales as Lambda^(-1/3) delta^(1/3)",
    "exact energy and enstrophy formulas",
    "separated equal components worsen the critical ratio",
    "formal thick support from low-amplitude tails is insufficient"
  ],
  "constructed": [
    "degree-zero logarithmic direction homotopy with predicted all-ball BMO C/L"
  ],
  "limits": [
    "homotopy constant not interval-certified",
    "piecewise-linear return requires mollification",
    "multiscale cuspidal and infinite cascades remain open",
    "no Navier-Stokes evolution claim"
  ],
  "next_test": "dyadic distribution of shell widths and amplitudes with exact Lorentz rearrangement"
}
~~~

État : **ABANDONNER** le plateau à coquille unique et les copies égales.
**CONSERVER** la réfutation de l'argument endpoints-only.

Prochaine expérience décisive : remplacer la coquille unique par des
coquilles dyadiques \((h_j,V_j)\), calculer les deux fonctions de
distribution complètes sans somme triangulaire, et déterminer si une loi
de type

\[
 \sum_{j:\,V_j/h_j>\lambda}
 \mathcal R R h_j
 \tag{61}
\]

peut garder \(K_w\) borné tout en fournissant assez de capacité
logarithmique pour une extension all-ball et un \(K_u\) non petit.
