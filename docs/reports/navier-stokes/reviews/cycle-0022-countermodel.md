# Cycle 0022 — porte harmonique d'un profil critique log-rectifié

Date : 2026-08-14.

Type de passe : calcul adverse indépendant par la même famille de modèle;
ce document n'est pas une revue externe indépendante.

## Verdict

Écrivons, près d'un cœur ponctuel,

\[
 W(x)=r^{-2}\Omega(s,n),\qquad
 s=\log(R_*/r),\quad n=x/r,
 \tag{1}
\]

et décomposons

\[
 \Omega=A(s,n)n+B(s,n),\qquad B\cdot n=0.
 \tag{2}
\]

Dans les calculs distributionnels ci-dessous, \(\Omega\) est supposé
\(C^1\) en \(s\), lisse en \(n\), et uniformément borné lorsque
\(s\to\infty\). Les identités sur l'espace ponctué demandent moins de
régularité; la borne uniforme sert à contrôler le terme de bord en zéro.

La contrainte solénoïdale exacte est

\[
 \boxed{\operatorname{div}_{S^2}B=\partial_s A,}
 \qquad
 \boxed{\int_{S^2}A(s,n)d\sigma=0.}
 \tag{3}
\]

La première identité vaut sur l'espace ponctué; la seconde élimine la masse
de Dirac à l'origine. En harmoniques sphériques, chaque mode poloïdal de
degré \(\ell\geq1\) est donc entièrement fixé par la dérivée logarithmique
du mode radial :

\[
 b_{\ell m}(s)=-\frac{a'_{\ell m}(s)}{\ell(\ell+1)}.
 \tag{4}
\]

Le mode \(\ell=1\) montre l'obstruction. Une direction constante \(e\) se
décompose comme

\[
 e=\mu n+\nabla_{S^2}\mu,qquad \mu=e\cdot n.
 \tag{5}
\]

Pour que le champ de degré un tende vers cette direction, il faut
\(b/a=1+O(1/s)\). Or (4) impose

\[
 \frac{a'}a=-2+O(1/s),
 \qquad
 a(s)=e^{-2s}s^{O(1)}.
 \tag{6}
\]

Le facteur de forme \(|\Omega|\) tend alors vers zéro comme
\(e^{-2s}\) à une puissance logarithmique près. La vorticité physique perd
son comportement \(r^{-2}\) et ne croît plus qu'en puissances de \(\log1/r\).

Cette perte ne dépend pas d'un ansatz monomodal. Si
\(\Omega=\Phi\xi\), avec \(0<c\leq\Phi\leq C\), et si la direction se
rectifie vers un axe fixe \(e\) au taux

\[
 \int_{S^2}|\xi(s,n)-e|d\sigma\leq K/s,
 \tag{7}
\]

alors (3) donne une identité de moment dont le membre droit reste strictement
négatif. Un moment borné devrait décroître linéairement en \(s\), ce qui est
impossible. Il n'existe donc aucun profil défini pour tout \(s\to\infty\)
qui satisfasse simultanément (1), (3), la non-dégénérescence de \(\Phi\) et
(7).

Le résultat est une obstruction exacte et falsifiable à la **rectification
vers un axe fixe en moyenne sphérique**. Il ne déduit pas (7) de la seule
semi-norme log-BMO sur les boules, et n'exclut ni un axe dépendant de \(s\),
ni une concentration dans une fraction angulaire qui tend vers zéro, ni une
amplitude qui dégénère.

## 1. Calcul solénoïdal en coordonnées logarithmiques

Comme \(ds/dr=-1/r\), la divergence de la partie radiale vaut

\[
 \frac1{r^2}\partial_r(r^2W_r)
 =-r^{-3}\partial_s A.
 \tag{8}
\]

La partie tangentielle donne

\[
 \operatorname{div}(r^{-2}B)=r^{-3}
 \operatorname{div}_{S^2}B.
 \tag{9}
\]

Ainsi

\[
 \operatorname{div}W=r^{-3}
 \left(\operatorname{div}_{S^2}B-\partial_sA\right)
 \quad\text{sur }\mathbb R^3\setminus\{0\}.
 \tag{10}
\]

Après intégration de (3) sur la sphère, la moyenne de \(A\) est constante en
\(s\). Le flux de \(W\) à travers une sphère vaut cette constante. Sous la
borne uniforme annoncée après (2), le reste de Taylor d'une fonction test
coûte \(O(r)\). Pour que la divergence distributionnelle ne contienne aucun
monopôle à l'origine, il faut et il suffit donc que le flux soit nul, ce qui
donne la seconde condition de (3).

## 2. Décomposition complète en harmoniques sphériques

Soit \((Y_{\ell m})\) une base réelle orthonormée telle que

\[
 -\Delta_{S^2}Y_{\ell m}=\lambda_\ell Y_{\ell m},
 \qquad \lambda_\ell=\ell(\ell+1).
 \tag{11}
\]

La décomposition de Hodge tangentielle donne

\[
 \begin{aligned}
 A(s,n)&=\sum_{\ell,m}a_{\ell m}(s)Y_{\ell m}(n),\\
 B(s,n)&=\sum_{\ell\geq1,m}
 \left[b_{\ell m}(s)\nabla_{S^2}Y_{\ell m}
 +c_{\ell m}(s)n\times\nabla_{S^2}Y_{\ell m}\right].
 \end{aligned}
 \tag{12}
\]

Les modes toroïdaux \(c_{\ell m}\) ont une divergence sphérique nulle et
restent libres. En substituant dans (3), on obtient exactement

\[
 -\lambda_\ell b_{\ell m}=a'_{\ell m}
 \quad(\ell\geq1),
 \qquad a'_{00}=0.
 \tag{13}
\]

L'absence de monopôle impose en plus \(a_{00}=0\). Par conséquent tout champ
solénoïdal de la forme (1) admet la représentation

\[
 \boxed{
 \Omega=\sum_{\ell\geq1,m}
 \left[
 a_{\ell m}Y_{\ell m}n
 -\frac{a'_{\ell m}}{\lambda_\ell}
 \nabla_{S^2}Y_{\ell m}
 +c_{\ell m}n\times\nabla_{S^2}Y_{\ell m}
 \right].}
 \tag{14}
\]

La taille quadratique du correcteur poloïdal est également exacte :

\[
 \int_{S^2}\left|
 \frac{a'_{\ell m}}{\lambda_\ell}\nabla Y_{\ell m}
 \right|^2d\sigma
 =\frac{|a'_{\ell m}|^2}{\lambda_\ell}
 \int_{S^2}|Y_{\ell m}|^2d\sigma.
 \tag{15}
\]

Le prix minimal est atteint à \(\ell=1\), avec le facteur \(1/2\). Des
hautes fréquences diminuent la norme \(L^2\) du correcteur de divergence à
dérivée radiale fixée, mais augmentent ses dérivées angulaires; elles ne
reproduisent pas une direction constante, qui appartient précisément au
secteur \(\ell=1\).

## 3. Obstruction quantitative sans ansatz monomodal

Supposons désormais

\[
 \Omega(s,n)=\Phi(s,n)\xi(s,n),
 \quad |\xi|=1,
 \quad 0<c\leq\Phi\leq C,
 \tag{16}
\]

et fixons un vecteur unitaire \(e\). Posons

\[
 \mu=e\cdot n,qquad
 M(s)=\int_{S^2}\mu A(s,n)d\sigma.
 \tag{17}
\]

Comme \(|A|\leq|\Omega|\leq C\),

\[
 |M(s)|\leq4\pi C.
 \tag{18}
\]

En testant la première équation de (3) par \(\mu\), puis en intégrant par
parties sur la sphère,

\[
 \begin{aligned}
 M'(s)
 &=\int_{S^2}\mu\,\operatorname{div}_{S^2}B\,d\sigma\\
 &=-\int_{S^2}\nabla_{S^2}\mu\cdot B\,d\sigma\\
 &=-\int_{S^2}\Phi\nabla_{S^2}\mu\cdot\xi\,d\sigma.
 \end{aligned}
 \tag{19}
\]

Or \(e=\mu n+\nabla_{S^2}\mu\), donc

\[
 \nabla_{S^2}\mu\cdot e=|\nabla_{S^2}\mu|^2,
 \qquad
 \int_{S^2}|\nabla_{S^2}\mu|^2d\sigma=\frac{8\pi}{3}.
 \tag{20}
\]

Les hypothèses (7) et (16) donnent alors

\[
 \boxed{
 M'(s)\leq-\frac{8\pi c}{3}+\frac{CK}{s}.}
 \tag{21}
\]

Sur tout intervalle \(S<T\),

\[
 \frac{8\pi c}{3}(T-S)
 \leq8\pi C+CK\log(T/S).
 \tag{22}
\]

Le membre gauche croît linéairement et le membre droit seulement
logarithmiquement. L'inégalité est impossible pour \(T\to\infty\).

Cette preuve localise le verrou dans le seul mode de test \(\ell=1\). Elle
ne suppose ni convergence de \(\Phi\), ni petitesse de ses dérivées, ni
symétrie axiale. Elle tolère toutes les harmoniques supérieures, tant que la
magnitude reste entre \(c\) et \(C\) et que l'axe limite \(e\) est fixe.

## 4. Construction exacte log-rectifiée, mais dégénérée

L'obstruction est tranchante : la rectification elle-même est réalisable dès
que l'on abandonne la borne inférieure de \(\Phi\). Prenons le mode
\(Y_{10}=\mu\) et

\[
 a(s)=e^{-2s}s^2,
 \qquad
 b(s)=-\frac{a'(s)}2=e^{-2s}(s^2-s).
 \tag{23}
\]

Alors

\[
 \Omega=a\mu n+b\nabla_{S^2}\mu
 =e^{-2s}\left[s^2\mu n+(s^2-s)\nabla_{S^2}\mu\right]
 \tag{24}
\]

satisfait (3) exactement. Comme \(e^{-2s}=(r/R_*)^2\), la vorticité
physique devient

\[
 W(x)=R_*^{-2}\left[(s^2-s)e+s\mu n\right]
 =R_*^{-2}s^2\left[e-\frac1s\nabla_{S^2}\mu\right].
 \tag{25}
\]

Pour \(s\geq2\), si \(\xi=W/|W|\),

\[
 \left|e-\frac1s\nabla\mu\right|\geq1-\frac1s,
 \qquad
 |\xi-e|\leq\frac{2}{s-1}.
 \tag{26}
\]

En particulier, pour \(s_\rho=\log(R_*/\rho)>2\),

\[
 \operatorname{MO}_{B_\rho}(\xi)
 \leq2\fint_{B_\rho}|\xi-e|dx
 \leq\frac4{s_\rho-1}.
 \tag{27}
\]

La direction est donc rectifiée au taux logarithmique souhaité sur les boules
centrées. En revanche,

\[
 e^{-2s}s^2(1-1/s)
 \leq|\Omega(s,n)|\leq e^{-2s}s^2,
 \tag{28}
\]

et le facteur \(\Phi=|\Omega|\) dégénère exponentiellement. Le champ
physique n'a qu'une singularité logarithmique \(|W|\asymp s^2\), très en
dessous de \(r^{-2}\).

### Vitesse explicite

Avec \(R_*=1\), posons

\[
 u(x)=\frac{s^2}{2}e\times x.
 \tag{29}
\]

Un calcul direct donne

\[
 \nabla\cdot u=0,
 \qquad
 \nabla\times u=(s^2-s)e+s\mu n=W.
 \tag{30}
\]

Ainsi la construction respecte aussi le raccord div–curl. Près de
l'origine, \(|u|=O(rs^2)\) et \(|W|=O(s^2)\); l'énergie et l'enstrophie
locales sont finies. Le champ n'est toutefois pas lisse au centre, car ses
dérivées finissent par diverger.

## 5. Coût dérivatif et résidu visqueux

Pour toute composante cartésienne de (1),

\[
 \boxed{
 \Delta W=r^{-4}
 \left(\partial_s^2+3\partial_s+2+\Delta_{S^2}\right)\Omega.}
 \tag{31}
\]

Le Laplacien sphérique dans (31) agit composante par composante, et non comme
le Laplacien scalaire sur les seuls coefficients dans la base mobile
\((n,\nabla Y,n\times\nabla Y)\).

Pour la construction (25), la décomposition cartésienne

\[
 \mu n=\frac13e+\left(\mu n-\frac13e\right)
 \tag{32}
\]

sépare un mode scalaire \(\ell=0\) et un mode \(\ell=2\). En utilisant les
valeurs propres \(0\) et \(6\), on obtient exactement

\[
 \boxed{
 \Delta W=r^{-2}\left[3e-(1+6s)\mu n\right].}
 \tag{33}
\]

Le choix solénoïdal annule le terme naïf \(r^{-2}s^2\) et gagne un facteur
\(1/s\), mais le résidu visqueux \(\nu\Delta W\) reste de taille
\(\nu r^{-2}s\). Il n'est pas petit près du cœur.

Le champ (29) est un swirl axisymétrique pur. Son terme non linéaire dans
l'équation de vorticité est également explicite :

\[
 (u\cdot\nabla)W-(W\cdot\nabla)u
 =\nabla\times((u\cdot\nabla)u)
 =s^3\mu\,e\times n.
 \tag{34}
\]

Les vecteurs de (33) sont dans le plan engendré par \(e,n\), tandis que (34)
est orthogonal à ce plan. Aucune annulation point par point entre viscosité
et non-linéarité n'est donc possible. Le profil n'est une solution
stationnaire ni d'Euler ni de Navier–Stokes.

### Défaut d'une coupure intérieure

Pour une coupure scalaire \(\chi(r/\varepsilon)\),

\[
 [\Delta,\chi]W
 =2\nabla\chi\cdot\nabla W+(\Delta\chi)W.
 \tag{35}
\]

La multiplication \(\chi W\) n'est en général déjà plus solénoïdale. Le
calcul suivant isole uniquement son commutateur visqueux; toute réparation de
divergence doit être ajoutée et ne peut améliorer ce majorant sans une
annulation spécialement démontrée.

Dans la coquille \(r\asymp\varepsilon\), avec
\(s_\varepsilon=\log(R_*/\varepsilon)\),

\[
 |W|=O(s_\varepsilon^2),\qquad
 |\nabla W|=O(s_\varepsilon/\varepsilon),
 \tag{36}
\]

donc, pour une coupure de référence fixée,

\[
 |[\Delta,\chi]W|
 =O(\varepsilon^{-2}s_\varepsilon^2).
 \tag{37}
\]

La coupure détruit le gain d'un logarithme présent dans (33). Sur une
coquille de volume \(O(\varepsilon^3)\), le coût critique est

\[
 \|[\Delta,\chi]W\|_{L^{3/2}}
 =O(s_\varepsilon^2),
 \tag{38}
\]

et diverge. Les constantes dépendent des deux premières dérivées de la
coupure. Une coupure tensorielle adaptée pourrait créer des annulations
supplémentaires; une coupure scalaire arbitraire ne fournit aucune erreur
visqueuse uniforme.

## 6. Certificat symbolique rationnel

Le script suivant vérifie avec `Fraction` :

- la relation modale \(b=-a'/2\) après factorisation de \(e^{-2s}\) ;
- la divergence exacte du champ (25) ;
- sa provenance comme rotationnel de (29) ;
- la décomposition \(\ell=0\oplus\ell=2\) et (32) ;
- le coefficient du terme non linéaire (34) ;
- les constantes \(8\pi/3\) et l'inégalité de profondeur (22).

```python
from fractions import Fraction as F


# Polynomials in s, stored with increasing powers.
def trim(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return tuple(p)


def add(*polynomials):
    degree = max((len(p) for p in polynomials), default=0)
    out = [F(0)] * degree
    for p in polynomials:
        for i, coefficient in enumerate(p):
            out[i] += coefficient
    return trim(out)


def scale(c, p):
    return trim(F(c) * coefficient for coefficient in p)


def derivative(p):
    return trim(F(i) * p[i] for i in range(1, len(p)))


def multiply(left, right):
    if not left or not right:
        return ()
    out = [F(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return trim(out)


one = (F(1),)
s = (F(0), F(1))
s2 = multiply(s, s)

# a=e^-2s P and b=e^-2s Q. Verify P'-2P=-2Q.
P = s2
Q = add(s2, scale(-1, s))
assert add(derivative(P), scale(-2, P)) == scale(-2, Q)

# Physical W=f(s)e+g(s) mu*n. Its divergence coefficient is
# -f'+2g-g'.
f = Q
g = s
divergence_coefficient = add(
    scale(-1, derivative(f)), scale(2, g), scale(-1, derivative(g))
)
assert divergence_coefficient == ()

# u=k(s)e cross x has curl (2k-k')e+k' mu*n.
k = scale(F(1, 2), s2)
assert add(scale(2, k), scale(-1, derivative(k))) == f
assert derivative(k) == g

# Componentwise spherical split: mu*n=e/3+Q_2, lambda_2=6.
l0 = add(f, scale(F(1, 3), g))
lap_l0 = add(derivative(derivative(l0)),
             scale(-1, derivative(l0)))
lap_l2 = add(derivative(derivative(g)),
             scale(-1, derivative(g)), scale(-6, g))
lap_e = add(lap_l0, scale(F(-1, 3), lap_l2))
assert lap_e == (F(3),)
assert lap_l2 == (F(-1), F(-6))

# Pure-swirl acceleration has q=k^2=s^4/4 and curl coefficient q'=s^3.
q = multiply(k, k)
assert derivative(q) == (F(0), F(0), F(0), F(1))

# Exact spherical moment coefficients after removing pi.
grad_mu_squared_over_pi = F(8, 3)
assert grad_mu_squared_over_pi == F(8, 3)

# Finite-depth gate: alpha(T-S)<=8*pi*C+C*K*log(T/S),
# alpha/pi=8c/3. Once CK/s <=4*pi*c/3, M'<=-4*pi*c/3.
c, C, K = F(1, 2), F(2), F(3)
pi_times_threshold = F(3) * C * K / (F(4) * c)
assert pi_times_threshold == 9

# Cutoff shell: eps^-2*s_eps^2 on eps^3 has invariant algebraic
# L^(3/2) scaling, leaving the logarithmic factor s_eps^2.
assert -2 + 3 * F(2, 3) == 0

print("spherical harmonic solenoidal gate: PASS")
print("log-rectified degenerate mode and viscous residual: PASS")
print("moment obstruction and cutoff scaling: PASS")
```

Commande de reproduction : extraire le bloc et exécuter `python -` depuis la
racine du dépôt. Dépendances : bibliothèque standard Python. Graine : aucune.
Tous les tests décisionnels sont rationnels exacts.

## 7. Passe contradictoire et portée PDE

1. **Log-BMO contre axe fixe.** La borne (7) est une rectification explicite
   en moyenne sphérique. Une semi-norme log-BMO sur les boules ne fournit pas
   automatiquement un même axe \(e\) sur toutes les coquilles.
2. **Magnitude non dégénérée.** L'obstruction exige une borne ponctuelle
   \(c\leq\Phi\). Une masse faible-\(L^{3/2}\) peut être portée par une
   fraction angulaire décroissante sans satisfaire cette hypothèse.
3. **Direction tournante.** Un axe \(e(s)\) pourrait déplacer le moment
   testé. Son coût \(|e'(s)|\), la cohérence entre coquilles et le log-BMO
   spatial resteraient à quantifier.
4. **Hautes fréquences.** La relation (4) rend le correcteur \(L^2\) plus
   petit quand \(\ell\) augmente, mais son gradient angulaire conserve le
   coût \(|a'|\); une cascade en \(\ell(s)\) n'est pas exclue par (15) seule.
5. **Laplacien vectoriel.** Employer seulement
   \(-\ell(\ell+1)\) sur les coefficients de la base mobile donne une formule
   fausse. Le calcul (31) est cartésien et (32) effectue la bonne
   décomposition scalaire.
6. **Coupure.** Les bornes (37)–(38) sont des majorants d'échelle pour une
   coupure de référence fixée, pas une minoration universelle sur tous les
   correcteurs solénoïdaux.
7. **Champ statique.** Les champs (25) et (28) sont définis sur un voisinage
   ponctué. Ils ne constituent ni une donnée Clay lisse globale, ni une
   trajectoire Navier–Stokes.
8. **Résidu vorticité.** Les formules (33)–(34) excluent la stationnarité de
   cet ansatz, mais n'excluent pas une compensation par \(\partial_tW\) dans
   un profil dépendant du temps.

Après coupures intérieure et extérieure, puis correction solénoïdale, on
peut fabriquer des données initiales lisses et d'énergie finie. Elles sont
distinctes pour chaque \(\varepsilon\); les constantes critiques de la
coupure ne sont pas uniformes, et aucune évolution ne les relie.

## 8. Obligations falsifiables

```json
{
  "cycle": "0022",
  "ansatz": "W=r^-2 Omega(log(R*/r),theta)",
  "claims": [
    {
      "id": "NS-C0022-SPHERICAL-SOLENOIDAL-GATE",
      "status": "PROVED_BY_EXACT_DECOMPOSITION",
      "statement": "div_S2 B=partial_s A and b_lm=-a_lm'/[l(l+1)], with zero l=0 radial mode"
    },
    {
      "id": "NS-C0022-FIXED-AXIS-NONDEGENERATE",
      "status": "REFUTED_IN_STATED_CLASS",
      "statement": "a globally log-rectified fixed-axis direction with 0<c<=Phi<=C can satisfy the solenoidal gate for all s to infinity",
      "certificate": "(8*pi*c/3)(T-S)<=8*pi*C+C*K*log(T/S)"
    },
    {
      "id": "NS-C0022-DEGENERATE-RECTIFICATION",
      "status": "PROVED_BY_EXACT_CONSTRUCTION",
      "statement": "logarithmic directional rectification is possible with Phi approximately e^-2s s^2, but the r^-2 critical magnitude is lost"
    },
    {
      "id": "NS-C0022-STATIONARY-NS",
      "status": "REFUTED_FOR_EXPLICIT_ANSATZ",
      "statement": "the explicit rectified field is stationary Navier-Stokes",
      "residuals": ["Delta W=r^-2(3e-(1+6s)mu n)", "nonlinear=s^3 mu e cross n"]
    }
  ],
  "decision": "ABANDON_FIXED-AXIS_LOG-RECTIFICATION_WITH_POINTWISE-NONDEGENERATE-PHI",
  "next_test": "allow e=e(s) or angular support fraction alpha(s), and track l(s), weak-L^(3/2) mass and viscous cost"
}
```

## Conclusion

La contrainte solénoïdale ne se contente pas d'ajouter un petit correcteur à
une direction presque constante. Dans le secteur qui porte une direction
constante, elle identifie la composante tangentielle à une dérivée en
\(s=\log(R_*/r)\). Maintenir cette composante d'ordre un force une décroissance
\(e^{-2s}\), exactement assez forte pour annuler le facteur \(r^{-2}\).

Le prochain test discriminant est donc une cascade angulaire : autoriser un
axe \(e(s)\) ou un support de mesure \(\alpha(s)\to0\), puis déterminer si la
masse faible-\(L^{3/2}\) peut rester non nulle sans que les fréquences
\(\ell(s)\), le Laplacien et les coupures fassent diverger le résidu.
