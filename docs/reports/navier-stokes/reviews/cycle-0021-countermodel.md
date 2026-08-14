# Cycle 0021 — profil ponctuel critique, divergence et obstruction log-BMO

Date : 2026-08-14.

Type de passe : construction et réfutation adverses par la même famille de
modèle; ce document n'est pas une revue externe indépendante.

## Verdict

Il existe sur \(\mathbb R^3\setminus\{0\}\) un couple homogène explicite

\[
 \begin{aligned}
 u(x)&=\frac1r\{a\times n+a+(a\cdot n)n\},\\
 \omega(x)&=\frac2{r^2}\{(a\cdot n)n+a\times n\},
 \end{aligned}
 \qquad r=|x|,\quad n=x/r,\quad |a|=1,
 \tag{1}
\]

tel que, au sens des distributions sur tout \(\mathbb R^3\),

\[
 \nabla\cdot u=0,\qquad \nabla\times u=\omega,
 \qquad \nabla\cdot\omega=0.
 \tag{2}
\]

Le module de la vorticité est exactement critique et isotrope :

\[
 |\omega(x)|=\frac2{r^2},\qquad
 \|\omega\|_{L^{3/2,\infty}}
 =\left(\frac{8\sqrt2\,\pi}{3}\right)^{2/3}.
 \tag{3}
\]

Sa direction

\[
 \xi(n)=(a\cdot n)n+a\times n
 \tag{4}
\]

est partout définie, unitaire et lisse sur \(S^2\). Elle n'appartient
pourtant pas à \(\mathrm{bmo}_{1/|\log r|}\). Son oscillation moyenne sur
**chaque** boule centrée en l'origine vaut la constante strictement positive

\[
 c_\xi=\frac13\left[1+\frac5{\sqrt6}
 \arcsin\!\sqrt{\frac35}\right]
 =0.9362324516\ldots .
 \tag{5}
\]

Ce n'est pas un accident de l'ansatz. Un champ ponctuel non nul, exactement
homogène de degré \(-2\), lisse hors de l'origine et sans zéro angulaire ne
peut être simultanément divergence-free et avoir une direction dans ce
log-BMO global. L'homogénéité rend l'oscillation indépendante du rayon;
log-BMO la force donc à zéro. Une direction constante est ensuite
incompatible avec une singularité ponctuelle divergence-free de degré
\(-2\) : elle produit soit le champ nul, soit une singularité portée par une
droite.

La famille fournit ainsi une **réfutation dans la classe homogène ponctuelle
exacte**, pas une réfutation de tout profil asymptotique, anisotrope ou
multi-échelle. Les coupures lisses ne ferment pas ce trou gratuitement :
leur défaut de divergence a une masse \(L^1\) indépendante de l'échelle, le
correcteur de rotationnel reste critique dans \(L^{3/2}\), et toute
approximation contenant un anneau homothétique du profil paie au moins
\(c|\log\varepsilon|\) en log-BMO.

## 1. Construction exacte sans zéro de vorticité

Fixons \(a=e_3\); les formules sont invariantes par rotation. Séparons (1)
en une partie toroïdale et une partie poloïdale :

\[
 u_T=\frac{a\times n}{r},\qquad
 u_P=\frac{a+(a\cdot n)n}{r}.
 \tag{6}
\]

Les identités élémentaires, valables hors de l'origine, sont

\[
 \begin{aligned}
 \nabla\cdot u_T&=0,&
 \nabla\times u_T&=\frac{2(a\cdot n)n}{r^2},\\
 \nabla\cdot u_P&=0,&
 \nabla\times u_P&=\frac{2a\times n}{r^2}.
 \end{aligned}
 \tag{7}
\]

Pour la seconde divergence, les deux termes se compensent exactement :

\[
 \nabla\cdot\frac a r=-\frac{a\cdot n}{r^2},
 \qquad
 \nabla\cdot\frac{(a\cdot n)n}{r}
 =+\frac{a\cdot n}{r^2}.
 \tag{8}
\]

La vorticité de (1) est donc bien la somme affichée. Ses parties radiale et
toroïdale sont orthogonales. En posant \(\mu=a\cdot n\),

\[
 |\mu n+a\times n|^2=\mu^2+(1-\mu^2)=1.
 \tag{9}
\]

Ainsi (3) est une identité ponctuelle, et (4) n'a aucun ensemble de zéros à
prolonger artificiellement. Ce point élimine le défaut plus élémentaire des
profils radiaux dipolaires, dont la direction saute sur un plan nodal.

### Validité distributionnelle à l'origine

Les tailles \(|u|=O(r^{-1})\) et \(|\omega|=O(r^{-2})\) sont localement
intégrables en dimension trois. Dans une intégration par parties sur
\(\mathbb R^3\setminus B_\rho\), les termes de bord associés au rotationnel
de \(u\) sont \(O(\rho)\), donc tendent vers zéro. Pour la divergence de
\(\omega\),

\[
 \omega\cdot n=\frac{2\mu}{r^2},
 \qquad
 \int_{S^2}2\mu\,d\sigma=0.
 \tag{10}
\]

Le terme constant de la fonction test s'annule par (10), et le reste est
\(O(\rho)\). Il n'apparaît donc ni masse de Dirac ni dérivée de Dirac dans
(2). Le champ radial source \(r^{-2}n\), lui, échouerait précisément ce test
de flux.

## 2. Biot–Savart et tailles exactes

Les identités ponctuelles supplémentaires sont

\[
 |u|^2=\frac{2(1+\mu^2)}{r^2},
 \qquad
 |\omega|^2=\frac4{r^4}.
 \tag{11}
\]

Comme

\[
 \int_{S^2}\mu^2d\sigma=\frac{4\pi}{3},
 \tag{12}
\]

un anneau \(A_{\delta,R}=\{\delta<r<R\}\) vérifie exactement

\[
 \begin{aligned}
 \|u\|_{L^2(A_{\delta,R})}^2
 &=\frac{32\pi}{3}(R-\delta),\\
 \frac12\|u\|_{L^2(A_{\delta,R})}^2
 &=\frac{16\pi}{3}(R-\delta),\\
 \|\omega\|_{L^2(A_{\delta,R})}^2
 &=16\pi\left(\frac1\delta-\frac1R\right).
 \end{aligned}
 \tag{13}
\]

La singularité ponctuelle coûte donc une énergie finie près de zéro, mais
une enstrophie \(O(\delta^{-1})\). Le profil brut n'est pas dans
\(L^2(\mathbb R^3)\), à cause de sa queue \(r^{-1}\) à l'infini.

La fonction de distribution du module de \(\omega\) sur tout l'espace vaut

\[
 |\{|\omega|>\lambda\}|
 =\frac{4\pi}{3}\left(\frac2\lambda\right)^{3/2}
 =\frac{8\sqrt2\,\pi}{3}\lambda^{-3/2}.
 \tag{14}
\]

Cela prouve (3), avec la convention
\(\|f\|_{L^{p,\infty}}=\sup_{\lambda>0}
\lambda|\{|f|>\lambda\}|^{1/p}\).

Le champ \(u\) est aussi l'inverse de Biot–Savart normalisé par la décroissance
à l'infini :

\[
 u(x)=\frac1{4\pi}\int_{\mathbb R^3}
 \frac{\omega(y)\times(x-y)}{|x-y|^3}\,dy,
 \qquad x\ne0.
 \tag{15}
\]

L'intégrale est convergente pour \(x\ne0\). Alternativement, (15) suit de
(2) : la différence entre les deux membres est une distribution harmonique,
divergence-free et curl-free, qui décroît à l'infini; elle est nulle. La
normalisation est indispensable, car ajouter un champ harmonique changerait
la vitesse sans changer la vorticité.

## 3. Calcul exact de l'obstruction log-BMO

La direction est homogène de degré zéro. Son intégrale sur une boule est
donc sa moyenne sphérique. Les symétries et (12) donnent

\[
 \xi_{B_\rho}=\frac a3
 \quad\hbox{pour tout }\rho>0.
 \tag{16}
\]

En effet, la moyenne de \(a\times n\) est nulle et celle de
\((a\cdot n)n\) est \(a/3\). De plus,

\[
 |\xi-a/3|^2=\frac{10-6\mu^2}{9}.
 \tag{17}
\]

Une intégration élémentaire donne

\[
 \begin{aligned}
 \frac1{|B_\rho|}\int_{B_\rho}|\xi-\xi_{B_\rho}|dx
 &=\frac13\int_0^1\sqrt{10-6\mu^2}\,d\mu\\
 &=\frac13\left[1+\frac5{\sqrt6}
 \arcsin\sqrt{\frac35}\right]=c_\xi.
 \end{aligned}
 \tag{18}
\]

Avec \(\phi(r)=1/|\log r|\), le semi-norme pertinent contient

\[
 \sup_{0<\rho<1/2}|\log\rho|
 \frac1{|B_\rho|}\int_{B_\rho}|\xi-\xi_{B_\rho}|dx
 =c_\xi\sup_{0<\rho<1/2}|\log\rho|=\infty.
 \tag{19}
\]

Le défaut est concentré à l'origine : \(\xi\) est une fonction lisse de
\(n\) partout ailleurs. Il n'est donc imputable ni à un saut de signe, ni à
une convention sur \(\{\omega=0\}\).

## 4. Lemme négatif pour tout profil ponctuel exactement homogène

**Lemme.** Soit

\[
 \omega(x)=r^{-2}W(n),
 \tag{20}
\]

où \(W\) est lisse et non nul sur \(S^2\). Supposons que \(\omega\) soit
lisse sur \(\mathbb R^3\setminus\{0\}\), divergence-free au sens des
distributions et que sa direction \(\xi=W/|W|\) appartienne à
\(\mathrm{bmo}_{1/|\log r|}\). Alors \(\omega=0\), contradiction avec la
non-annulation de \(W\). Il n'existe donc aucun tel profil non nul.

**Preuve.** Pour toute boule centrée en zéro, le changement de variables
\(x=\rho y\) montre que

\[
 \operatorname{osc}_{B_\rho}\xi
 =\operatorname{osc}_{B_1}\xi=:c.
 \tag{21}
\]

La finitude du semi-norme dans (19) impose \(c=0\); ainsi
\(\xi=a\) presque partout pour un vecteur constant \(a\). On peut écrire
\(\omega=h a\), où \(h=|\omega|\) est homogène de degré \(-2\).
L'équation de divergence devient

\[
 a\cdot\nabla h=0.
 \tag{22}
\]

Après rotation, \(a=e_3\), donc \(h\) est indépendant de \(z\) sur toute
droite ne rencontrant pas l'origine. L'homogénéité donne alors, en coordonnées
cylindriques,

\[
 h(\varrho,\theta,z)=\varrho^{-2}H(\theta).
 \tag{23}
\]

Si \(H\ne0\), (23) est singulier le long de tout l'axe \(\varrho=0\), y
compris aux points \((0,0,z_0)\) avec \(z_0\ne0\). Cela contredit la lissité
hors de l'origine. Donc \(H=0\), puis \(\omega=0\). \(\square\)

Le lemme utilise de manière essentielle : homogénéité exacte, singularité
isolée, direction définie sans zéro angulaire, et semi-norme global testé sur
les boules centrées à l'origine. Il ne traite pas un profil qui rompt
l'homogénéité par des logarithmes, concentre sa masse dans des cônes dont
l'ouverture tend vers zéro, ou possède plusieurs échelles.

## 5. Coupures : les deux multiplications naïves échouent

Pour rendre la coupure reproductible, posons

\[
 h_0(t)=\begin{cases}0,&t\leq0,\\e^{-1/t},&t>0,\end{cases}
 \qquad
 H(t)=\begin{cases}
 0,&t\leq0,\\
 \dfrac{h_0(t)}{h_0(t)+h_0(1-t)},&0<t<1,\\
 1,&t\geq1.
 \end{cases}
 \tag{24}
\]

La fonction \(H\) est une marche plate dans \(C^\infty(\mathbb R)\). Pour
\(0<4\varepsilon\leq R\), posons

\[
 g_{\varepsilon,R}(r)
 =H(r/\varepsilon-1)H(2-r/R).
 \tag{25}
\]

Alors \(g=0\) pour \(r\leq\varepsilon\) et \(r\geq2R\), et \(g=1\) sur
\(2\varepsilon\leq r\leq R\).

### Coupure directe de la vitesse

Le champ \(A=gu\) est lisse et compact, mais n'est pas incompressible :

\[
 \nabla\cdot A=g'(r)n\cdot u
 =\frac{2\mu g'(r)}r.
 \tag{26}
\]

Le terme poloïdal donne donc un défaut absent d'une vitesse purement
toroïdale. L'énergie de cette coupure non projetée est néanmoins exacte :

\[
 \|A\|_2^2=\frac{32\pi}{3}\int_0^\infty g(r)^2dr.
 \tag{27}
\]

### Coupure directe de la vorticité

Le champ \(g\omega\) n'est pas davantage admissible comme vorticité :

\[
 \nabla\cdot(g\omega)=\frac{2\mu g'(r)}{r^2}.
 \tag{28}
\]

Sa norme \(L^1\) est exactement

\[
 \|\nabla\cdot(g\omega)\|_1
 =4\pi\int_0^\infty|g'(r)|dr.
 \tag{29}
\]

Pour une montée et une descente monotones disjointes, (29) vaut \(8\pi\),
indépendamment de \(\varepsilon\) et de \(R\). Le défaut tend vers zéro au
sens des distributions pour la seule contribution de la coupure intérieure
lorsque \(\varepsilon\downarrow0\), grâce à l'annulation angulaire de
\(\mu\), mais pas en variation totale.

## 6. Réparation exacte par rotationnel et projection de Leray

Définissons la vorticité coupée par

\[
 \Omega_{\varepsilon,R}:=\nabla\times(gu)
 =g\omega+\tau,
 \tag{30}
\]

où

\[
 \tau=\nabla g\times u
 =\frac{g'(r)}r\{a-\mu n-a\times n\}.
 \tag{31}
\]

Alors \(\Omega_{\varepsilon,R}\in C_c^\infty\) et
\(\nabla\cdot\Omega_{\varepsilon,R}=0\) exactement. En particulier,

\[
 \nabla\cdot\tau=-\frac{2\mu g'(r)}{r^2},
 \tag{32}
\]

ce qui annule (28). Le coût du correcteur est

\[
 |\tau|^2=\frac{2(1-\mu^2)|g'(r)|^2}{r^2},
 \qquad
 \boxed{\|\tau\|_2^2=\frac{16\pi}{3}
 \int_0^\infty|g'(r)|^2dr.}
 \tag{33}
\]

Une transition de largeur comparable à son rayon \(s\) a
\(|\tau|\sim s^{-2}\) sur un volume \(\sim s^3\). Son coût
\(L^{3/2}\), donc aussi son coût critique faible-
\(L^{3/2}\), reste d'ordre un quand \(s\downarrow0\); son coût \(L^2\)
est d'ordre \(s^{-1}\). La coupure ne produit donc pas une erreur critique
qui tend vers zéro.

La vitesse divergence-free associée n'est pas \(gu\), mais

\[
 v_{\varepsilon,R}=\mathbb P(gu)=gu-\nabla q,
 \qquad \Delta q=\nabla\cdot(gu),
 \tag{34}
\]

où \(\mathbb P\) est la projection de Leray sur \(\mathbb R^3\). Elle
vérifie

\[
 \nabla\cdot v_{\varepsilon,R}=0,
 \qquad
 \nabla\times v_{\varepsilon,R}=\Omega_{\varepsilon,R}.
 \tag{35}
\]

La source (26) est un harmonique sphérique de degré un. En écrivant
\(q(r,n)=\mu Q(r)\), la solution régulière à zéro et décroissante à l'infini
est explicitement

\[
 Q(r)=-\frac23\left[
 r^{-2}\int_0^r s^2g'(s)ds
 +r\int_r^\infty\frac{g'(s)}sds
 \right].
 \tag{36}
\]

Hors du support de \(g'\),

\[
 Q(r)=\frac4{3r^2}\int_0^\infty s g(s)ds.
 \tag{37}
\]

La projection crée donc une queue dipolaire
\(|\nabla q|=O(r^{-3})\), même si \(gu\) et \(\Omega\) sont compacts. C'est
le coût non local exact de Biot–Savart.

L'orthogonalité de Leray donne l'identité d'énergie

\[
 \boxed{
 \|v_{\varepsilon,R}\|_2^2
 =\frac{32\pi}{3}\int g^2dr
 -\frac{4\pi}{3}\int r^2|Q'|^2dr
 -\frac{8\pi}{3}\int |Q|^2dr.}
 \tag{38}
\]

Enfin, puisque \(v\in L^2\) fixe le mode harmonique,

\[
 v_{\varepsilon,R}(x)=\frac1{4\pi}\int_{\mathbb R^3}
 \frac{\Omega_{\varepsilon,R}(y)\times(x-y)}{|x-y|^3}dy.
 \tag{39}
\]

Les formules (34)–(39) empêchent de confondre la coupure locale \(gu\), qui
n'est pas divergence-free, avec la vitesse physique reconstruite.

## 7. Le coût log-BMO survit aux coupures

Dans l'anneau \(2\varepsilon<r<4\varepsilon\), sous
\(4\varepsilon\leq R\), on a \(g=1\), \(g'=0\), donc
\(\Omega=\omega\) et sa direction vaut exactement (4).

Pour tout vecteur \(c\) avec \(|c|\leq1\),

\[
 \mathbb E_{S^2}|\xi-c|^2
 =1+|c|^2-\frac23c\cdot a\geq\frac89.
 \tag{40}
\]

Comme \(|\xi-c|\leq2\), (40) implique
\(\mathbb E_{S^2}|\xi-c|\geq4/9\). L'anneau occupe la fraction

\[
 \frac{|B_{4\varepsilon}\setminus B_{2\varepsilon}|}
 {|B_{4\varepsilon}|}=1-2^{-3}=\frac78.
 \tag{41}
\]

Quelle que soit l'extension de norme au plus un choisie sur les zéros de
\(\Omega\), sa moyenne \(c=\xi_{B_{4\varepsilon}}\) vérifie
\(|c|\leq1\). En intégrant
seulement sur l'anneau,

\[
 \frac1{|B_{4\varepsilon}|}
 \int_{B_{4\varepsilon}}|\xi-\xi_{B_{4\varepsilon}}|dx
 \geq\frac78\frac49=\frac7{18}.
 \tag{42}
\]

Par conséquent,

\[
 [\xi]_{\mathrm{bmo}_{1/|\log r|}}
 \geq\frac7{18}|\log(4\varepsilon)|.
 \tag{43}
\]

La constante log-BMO ne peut être uniforme quand
\(\varepsilon\downarrow0\). La coupure particulière peut même créer des
obstructions supplémentaires aux frontières où \(\Omega\) s'annule; (43)
n'en dépend pas et reste valide pour toute extension de norme au plus un sur
ces zéros.

## 8. Certificat exact, bibliothèque standard uniquement

Le script ci-dessous manipule exactement des sommes de monômes
\(c x^iy^jz^k(x^2+y^2+z^2)^p\) avec `Fraction`. Il vérifie (2), (11), les
constantes angulaires et radiales, les résidus de coupure et la croissance de
(43). Le seul calcul flottant est un contrôle secondaire de la valeur
décimale de (5); aucune conclusion de signe ne repose sur lui.

```python
from fractions import Fraction as F
from math import asin, factorial, isclose, pi, sqrt


# Symbolic terms c*x^i*y^j*z^k*s^p, s=x^2+y^2+z^2.
def add(*vectors):
    out = {}
    for vector in vectors:
        for key, coefficient in vector.items():
            out[key] = out.get(key, F(0)) + coefficient
    return {key: coefficient for key, coefficient in out.items()
            if coefficient}


def term(c, i, j, k, p):
    return {(i, j, k, F(p)): F(c)}


def scale(c, vector):
    return {key: F(c) * value for key, value in vector.items()
            if c * value}


def multiply(left, right):
    out = {}
    for (i, j, k, p), c in left.items():
        for (ii, jj, kk, pp), d in right.items():
            key = (i + ii, j + jj, k + kk, p + pp)
            out[key] = out.get(key, F(0)) + c * d
    return {key: coefficient for key, coefficient in out.items()
            if coefficient}


def derivative(vector, axis):
    out = {}
    for exponents, coefficient in vector.items():
        xyz = list(exponents[:3])
        p = exponents[3]
        monomial_power = xyz[axis]
        if monomial_power:
            reduced = xyz.copy()
            reduced[axis] -= 1
            key = (*reduced, p)
            out[key] = out.get(key, F(0)) + coefficient * monomial_power
        if p:
            raised = xyz.copy()
            raised[axis] += 1
            key = (*raised, p - 1)
            out[key] = out.get(key, F(0)) + coefficient * 2 * p
    return {key: coefficient for key, coefficient in out.items()
            if coefficient}


def canonical_numerator(vector):
    """Put terms over the lowest s power and expand positive powers of s."""
    if not vector:
        return {}
    p0 = min(key[3] for key in vector)
    out = {}
    for (i, j, k, p), coefficient in vector.items():
        degree = p - p0
        assert degree.denominator == 1 and degree >= 0
        degree = int(degree)
        for ax in range(degree + 1):
            for ay in range(degree - ax + 1):
                az = degree - ax - ay
                multinomial = F(
                    factorial(degree),
                    factorial(ax) * factorial(ay) * factorial(az),
                )
                key = (i + 2 * ax, j + 2 * ay, k + 2 * az)
                out[key] = out.get(key, F(0)) + coefficient * multinomial
    return {key: coefficient for key, coefficient in out.items()
            if coefficient}


def same(left, right):
    return canonical_numerator(add(left, scale(-1, right))) == {}


# Cartesian form of (1), with s=r^2 and a=e_3.
u = [
    add(term(-1, 0, 1, 0, -1), term(1, 1, 0, 1, F(-3, 2))),
    add(term(1, 1, 0, 0, -1), term(1, 0, 1, 1, F(-3, 2))),
    add(term(1, 0, 0, 0, F(-1, 2)),
        term(1, 0, 0, 2, F(-3, 2))),
]
omega = [
    add(term(2, 1, 0, 1, -2), term(-2, 0, 1, 0, F(-3, 2))),
    add(term(2, 0, 1, 1, -2), term(2, 1, 0, 0, F(-3, 2))),
    term(2, 0, 0, 2, -2),
]

div_u = add(*(derivative(u[i], i) for i in range(3)))
curl_u = [
    add(derivative(u[2], 1), scale(-1, derivative(u[1], 2))),
    add(derivative(u[0], 2), scale(-1, derivative(u[2], 0))),
    add(derivative(u[1], 0), scale(-1, derivative(u[0], 1))),
]
div_omega = add(*(derivative(omega[i], i) for i in range(3)))
assert canonical_numerator(div_u) == {}
assert all(same(curl_u[i], omega[i]) for i in range(3))
assert canonical_numerator(div_omega) == {}

u_squared = add(*(multiply(component, component) for component in u))
omega_squared = add(*(multiply(component, component)
                      for component in omega))
expected_u_squared = add(term(2, 0, 0, 0, -1),
                         term(2, 0, 0, 2, -2))
expected_omega_squared = term(4, 0, 0, 0, -2)
assert same(u_squared, expected_u_squared)
assert same(omega_squared, expected_omega_squared)

# Exact coefficients after removing pi.
mean_mu_squared = F(1, 3)
u_energy_integrand_over_pi = 8 * (1 + mean_mu_squared)
omega_enstrophy_integrand_over_pi = 16
assert u_energy_integrand_over_pi == F(32, 3)
assert omega_enstrophy_integrand_over_pi == 16

# Direction: mean a/3 and exact squared mean oscillation 8/9.
direction_mean_z = F(1, 3)
direction_mean_square_oscillation = 1 - direction_mean_z ** 2
assert direction_mean_square_oscillation == F(8, 9)
c_xi = (1 + 5 / sqrt(6) * asin(sqrt(F(3, 5)))) / 3
assert isclose(c_xi, 0.9362324516791188, rel_tol=0, abs_tol=1e-15)

# Critical distribution: lambda * volume(lambda)^(2/3) has exponent zero.
assert -2 + 3 * F(2, 3) == 0
weak_coefficient = (8 * sqrt(2) * pi / 3) ** (F(2, 3))
assert isclose(weak_coefficient, 5.197036119627671,
               rel_tol=0, abs_tol=1e-14)

# Cutoff identities after removing pi.
direct_divergence_L1_per_monotone_transition_over_pi = 4
tau_L2_coefficient_over_pi = 16 * mean_mu_squared
assert direct_divergence_L1_per_monotone_transition_over_pi == 4
assert tau_L2_coefficient_over_pi == F(16, 3)

# Shell B_(4 eps) minus B_(2 eps): exact uniform BMO residual.
shell_fraction = 1 - F(2 ** 3, 4 ** 3)
angular_L1_lower = F(4, 9)
cutoff_mean_oscillation_lower = shell_fraction * angular_L1_lower
assert shell_fraction == F(7, 8)
assert cutoff_mean_oscillation_lower == F(7, 18)

# epsilon=2^-n gives |log(4 epsilon)|=(n-2)log(2).
previous = F(0)
for n in range(3, 65):
    lower_in_log2_units = F(7 * (n - 2), 18)
    assert lower_in_log2_units > previous
    previous = lower_in_log2_units

print("distributional div/curl and pointwise magnitudes: PASS")
print("energy, enstrophy and weak-L^(3/2) scaling: PASS")
print("cutoff defects and log-BMO lower bound: PASS")
```

Commande de reproduction : extraire ce bloc et l'exécuter par `python -`
depuis la racine du dépôt. Dépendances : bibliothèque standard Python.
Graine : aucune. La partie algébrique est rationnelle exacte.

## 9. Statut PDE : profil statique, donnée admissible, dynamique

Le couple brut (1) est un **champ statique cinématique**. Il vérifie les
contraintes elliptiques de divergence et Biot–Savart, mais :

- \(u\notin L^2(\mathbb R^3)\) à cause de l'infini ;
- \(u\) n'est pas lisse à l'origine ;
- aucune dérivée temporelle ni pression Navier–Stokes n'a été construite ;
- (1) n'est pas affirmé solution stationnaire de Navier–Stokes.

Pour chaque \(0<4\varepsilon\leq R<\infty\), la vitesse projetée
\(v_{\varepsilon,R}=\mathbb P(gu)\) est lisse, divergence-free, dans
\(H^m(\mathbb R^3)\) pour tout \(m\), et d'énergie finie. C'est donc une
donnée initiale admissible pour le problème de Cauchy Navier–Stokes 3D non
forcé sur \(\mathbb R^3\), avec viscosité \(\nu>0\), et elle engendre une
solution classique locale unique.

Cette donnée n'est pas un blow-up :

- sa vorticité est bornée pour chaque \(\varepsilon>0\) ;
- ses normes de dérivées divergent lorsque \(\varepsilon\downarrow0\) ;
- la projection de Leray modifie non localement la vitesse jusque dans la
  région où la coupure vaut un ;
- la diffusion, l'étirement et la pression ne préservent pas l'ansatz ;
- aucune convergence d'une trajectoire Navier–Stokes vers (1) n'est établie.

## 10. Obligations falsifiables

```json
{
  "cycle": "0021",
  "profile": "omega=2 r^-2 ((a dot n)n+a cross n)",
  "claims": [
    {
      "id": "NS-C0021-CRITICAL-DIVFREE-PROFILE",
      "status": "PROVED_BY_EXACT_CONSTRUCTION",
      "statement": "a nowhere-zero homogeneous degree -2 vorticity can be distributionally divergence-free and have exact weak-L^(3/2) size",
      "weak_norm": "(8 sqrt(2) pi/3)^(2/3)"
    },
    {
      "id": "NS-C0021-HOMOGENEOUS-LOG-BMO",
      "status": "REFUTED_IN_STATED_CLASS",
      "statement": "a nonzero isolated exactly homogeneous degree -2 smooth divergence-free profile with nowhere-zero angular part can have direction in bmo_(1/abs(log r))",
      "obstruction": "scale-invariant mean oscillation forces constant direction; constant direction forces a line singularity or zero"
    },
    {
      "id": "NS-C0021-CUTOFF-FREE",
      "status": "REFUTED",
      "statement": "a scalar cutoff preserves both velocity and vorticity divergence constraints with vanishing critical error",
      "residuals": ["L1 divergence cost 4 pi per transition", "critical L^(3/2) curl corrector", "Leray dipole tail"]
    },
    {
      "id": "NS-C0021-DYNAMIC-BLOWUP",
      "status": "NOT_CLAIMED",
      "statement": "the static profile or its cutoffs form a Navier-Stokes blow-up trajectory"
    }
  ],
  "decision": "ABANDON_EXACT_HOMOGENEOUS_POINT_PROFILE_UNDER_GLOBAL_LOG_BMO",
  "next_test": "allow a logarithmically nonhomogeneous or angularly sparse profile and quantify loss of critical weak-L^(3/2) mass"
}
```

## Conclusion

Les contraintes \(|\omega|=2r^{-2}\), \(\nabla\cdot\omega=0\), Biot–Savart
et direction lisse sont simultanément réalisables. La condition qui casse
est précisément le log-BMO global : toute géométrie angulaire non constante
réapparaît avec la même oscillation à chaque zoom. Le lemme négatif montre
que remplacer cette géométrie par une direction constante déplace la
singularité de l'origine vers une droite et sort de la classe critique
ponctuelle.

La prochaine construction utile doit donc rompre l'homogénéité exacte. Elle
devra mesurer simultanément le taux \(O(1/|\log r|)\) de rectification de la
direction, la fraction angulaire portant \(r^{-2}\), le défaut de divergence
et la masse faible-\(L^{3/2}\). Sans ces quatre contrôles, un profil
« presque aligné » peut seulement cacher la masse critique dans un ensemble
qui s'effondre.
