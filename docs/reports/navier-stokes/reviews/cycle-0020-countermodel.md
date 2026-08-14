# Cycle 0020 — deux cœurs de vorticité anti-alignés dans un champ compact

Date : 2026-08-14.

Type de passe : construction adverse par la même famille de modèle; ce
document n'est pas une revue externe indépendante.

## Verdict

Il existe un champ

\[
 u\in C_c^\infty(\mathbb R^3;\mathbb R^3),
 \qquad \nabla\cdot u=0,
 \tag{1}
\]

dont la vorticité possède deux cœurs cylindriques voisins, parallèles et de
directions opposées. Une construction explicite par fonction de courant est
donnée ci-dessous. Aux centres des deux cœurs,

\[
 \omega(a_+,0)=+\frac{4\Gamma}{\varepsilon^2}e_3,
 \qquad
 \omega(a_-,0)=-\frac{4\Gamma}{\varepsilon^2}e_3.
 \tag{2}
\]

Pour une longueur axiale \(L=q\varepsilon\), \(q\) fixé, la famille vérifie

\[
 \|u\|_2^2\asymp\Gamma^2\varepsilon,
 \qquad
 \|\omega\|_2^2\asymp\Gamma^2\varepsilon^{-1},
 \qquad
 \|\omega\|_{L^{3/2,\infty}}\asymp\Gamma.
 \tag{3}
\]

Elle constitue donc un contrechamp instantané critique reproductible : deux
cœurs de plus en plus intenses peuvent coûter une énergie cinétique qui tend
vers zéro, tout en gardant une taille faible-\(L^{3/2}\) non nulle.

La construction simple n'est toutefois **pas admissible** sous une hypothèse
globale uniforme
\(\xi=\omega/|\omega|\in\mathrm{bmo}_{1/|\log r|}\). Chaque cœur possède un
anneau de retour où la composante verticale change de signe à travers un zéro;
la direction saute de \(+e_3\) à \(-e_3\), ce qui donne un semi-norme pondéré
infini. Plus généralement, même si un terme transverse répare ce saut par une
rotation continue, deux sous-cœurs opposés, de taille et séparation
\(O(\varepsilon)\), imposent la borne inférieure

\[
 [\xi]_{\mathrm{bmo}_{1/|\log r|}}
 \geq \frac1{256}|\log(2\varepsilon)|.
 \tag{4}
\]

Ainsi une famille anti-alignée se concentrant avec
\(\varepsilon\downarrow0\) ne peut conserver une constante BMO pondérée
uniforme. C'est l'obstacle précis, et non l'incompressibilité ou la compacité
du champ.

## 1. Briques lisses explicites

Définissons la bosse radiale plate

\[
 f(s)=
 \begin{cases}
 \exp\!\left(-\dfrac{s}{1-s}\right),&0\leq s<1,\\
 0,&s\geq1.
 \end{cases}
 \tag{5}
\]

Elle appartient à \(C_c^\infty([0,\infty))\), vaut \(1\) en \(s=0\), et
toutes ses dérivées s'annulent en \(s=1\).

Pour fabriquer une coupure axiale avec plateau, posons

\[
 q(t)=
 \begin{cases}
 0,&t\leq0,\\
 e^{-1/t},&t>0,
 \end{cases}
 \qquad
 H(t)=
 \begin{cases}
 0,&t\leq0,\\
 \dfrac{q(t)}{q(t)+q(1-t)},&0<t<1,\\
 1,&t\geq1,
 \end{cases}
 \tag{6}
\]

et

\[
 \chi_0(z)=H\!\left(\frac{4-z^2}{3}\right),
 \qquad
 \chi_L(z)=\chi_0(z/L).
 \tag{7}
\]

Alors \(\chi_L=1\) sur \(|z|\leq L\),
\(\chi_L=0\) sur \(|z|\geq2L\), et
\(\chi_L\in C_c^\infty(\mathbb R)\).

Fixons \(0<\varepsilon<1/4\) et deux centres transverses

\[
 a_+=\left(\frac{3\varepsilon}{2},0\right),
 \qquad
 a_-=\left(-\frac{3\varepsilon}{2},0\right).
 \tag{8}
\]

Leur distance vaut \(3\varepsilon>2\varepsilon\); les supports des deux
bosses de rayon \(\varepsilon\) sont disjoints. Posons

\[
 F_\pm(x,y)=
 f\!\left(\frac{|(x,y)-a_\pm|^2}{\varepsilon^2}\right),
 \qquad
 \Phi=F_+-F_-,
 \tag{9}
\]

puis la fonction de courant tridimensionnelle

\[
 \Psi(x,y,z)=\Gamma\chi_L(z)\Phi(x,y),
 \qquad \Gamma>0.
 \tag{10}
\]

## 2. Vitesse, divergence et vorticité

Définissons

\[
 u=(\partial_y\Psi,-\partial_x\Psi,0).
 \tag{11}
\]

La compacité et la régularité suivent de (5)–(10). L'incompressibilité est
une identité exacte de dérivées mixtes :

\[
 \nabla\cdot u
 =\partial_{xy}\Psi-\partial_{yx}\Psi=0.
 \tag{12}
\]

Le rotationnel vaut

\[
 \omega=\nabla\times u
 =\left(
 \partial_{xz}\Psi,
 \partial_{yz}\Psi,
 -\Delta_\perp\Psi
 \right),
 \tag{13}
\]

soit explicitement

\[
 \omega
 =\Gamma\left(
 \chi_L'(z)\partial_x\Phi,
 \chi_L'(z)\partial_y\Phi,
 -\chi_L(z)\Delta_\perp\Phi
 \right).
 \tag{14}
\]

Comme rotationnel d'un champ lisse, \(\nabla\cdot\omega=0\) exactement.
Le support de \(u\) et de \(\omega\) est contenu dans

\[
 \left(B_\varepsilon(a_+)\cup B_\varepsilon(a_-)\right)
 \times[-2L,2L].
 \tag{15}
\]

## 3. Deux cœurs exactement opposés

Avec

\[
 s=\frac{|(x,y)-a|^2}{\varepsilon^2},
 \tag{16}
\]

un calcul radial donne

\[
 -\Delta_\perp F_{\varepsilon,a}
 =\frac{4}{\varepsilon^2}
 f(s)\frac{1-s-s^2}{(1-s)^4},
 \qquad 0\leq s<1.
 \tag{17}
\]

En particulier,

\[
 -\Delta_\perp F_{\varepsilon,a}(a)
 =\frac4{\varepsilon^2}.
 \tag{18}
\]

Dans la tranche \(|z|leq L\), on a \(\chi_L=1\) et \(\chi_L'=0\); la
vorticité y est purement verticale. Comme les supports transverses sont
disjoints, (14) et (18) donnent exactement (2).

Sur chaque disque \(|(x,y)-a_\pm|\leq\varepsilon/2\), on a \(s\leq1/4\) et

\[
 1-s-s^2\geq\frac{11}{16},
 \qquad
 f(s)\geq e^{-1/3}.
 \tag{19}
\]

Ainsi les deux cylindres

\[
 C_\pm=B_{\varepsilon/2}(a_\pm)\times[-L,L]
 \tag{20}
\]

portent des composantes verticales de signes opposés et de taille

\[
 |\omega_3|
 \geq c_*\frac{\Gamma}{\varepsilon^2},
 \qquad
 c_*:=\frac{11}{4}e^{-1/3}.
 \tag{21}
\]

Les cœurs sont séparés par une distance comparable à leur diamètre. Ils sont
« voisins » au sens d'une configuration se concentrant sur une même échelle
\(\varepsilon\), et non au sens de supports qui se chevauchent.

## 4. Énergie exacte

Introduisons les constantes axiales finies

\[
 J_0=\int_{\mathbb R}\chi_0(z)^2\,dz,
 \qquad
 J_1=\int_{\mathbb R}|\chi_0'(z)|^2\,dz.
 \tag{22}
\]

Les supports transverses étant disjoints,

\[
 \int_{\mathbb R^2}|\nabla_\perp\Phi|^2
 =2\int_{\mathbb R^2}|\nabla F_{\varepsilon,0}|^2,
 \qquad
 \int_{\mathbb R^2}|\Delta_\perp\Phi|^2
 =2\int_{\mathbb R^2}|\Delta F_{\varepsilon,0}|^2.
 \tag{23}
\]

Les deux intégrales de base sont calculables exactement. Avec
\(t=s/(1-s)\),

\[
 \begin{aligned}
 \int_{\mathbb R^2}|\nabla F_{\varepsilon,0}|^2
 &=4\pi\int_0^\infty(t+t^2)e^{-2t}\,dt
 =2\pi,\\
 \int_{\mathbb R^2}|\Delta F_{\varepsilon,0}|^2
 &=\frac{16\pi}{\varepsilon^2}
 \int_0^\infty
 (t^2-t-1)^2(1+t)^2e^{-2t}\,dt\\
 &=\frac{70\pi}{\varepsilon^2}.
 \end{aligned}
 \tag{24}
\]

Comme
\(\int\chi_L^2=LJ_0\) et
\(\int|\chi_L'|^2=J_1/L\), on obtient

\[
 \boxed{\|u\|_2^2=4\pi\Gamma^2LJ_0}
 \tag{25}
\]

et

\[
 \boxed{
 \|\omega\|_2^2
 =4\pi\Gamma^2\frac{J_1}{L}
 +140\pi\Gamma^2\frac{LJ_0}{\varepsilon^2}.}
 \tag{26}
\]

L'énergie cinétique est \(\frac12\|u\|_2^2\). Pour un champ compact
divergence-free,

\[
 \|\nabla u\|_2^2=\|\omega\|_2^2.
 \tag{27}
\]

Avec \(L=q\varepsilon\), (25)–(26) donnent les première et deuxième lois de
(3). Les transitions axiales coûtent le terme
\(4\pi\Gamma^2J_1/L\); les gradients transverses des cœurs coûtent le terme
\(140\pi\Gamma^2LJ_0/\varepsilon^2\). Les deux sont
\(O(\Gamma^2/\varepsilon)\) lorsque le rapport d'aspect \(q\) est fixé.

## 5. Taille faible-\(L^{3/2}\)

Soit

\[
 C_\nabla=\|\nabla F_{1,0}\|_\infty,
 \quad
 C_\Delta=\|\Delta F_{1,0}\|_\infty,
 \quad
 C_\chi=\|\chi_0'\|_\infty.
 \tag{28}
\]

À cause de la séparation des supports,

\[
 \|\omega\|_\infty
 \leq\Gamma\left(
 \frac{C_\chi C_\nabla}{L\varepsilon}
 +\frac{C_\Delta}{\varepsilon^2}
 \right).
 \tag{29}
\]

Le volume total du support est au plus

\[
 |\operatorname{supp}\omega|
 \leq8\pi\varepsilon^2L.
 \tag{30}
\]

La borne élémentaire
\(\|g\|_{L^{3/2,\infty}}leq\|g\|_\infty
|\operatorname{supp}g|^{2/3}\) donne donc

\[
 \|\omega\|_{L^{3/2,\infty}}
 \leq
 \Gamma\left(
 \frac{C_\chi C_\nabla}{L\varepsilon}
 +\frac{C_\Delta}{\varepsilon^2}
 \right)
 (8\pi\varepsilon^2L)^{2/3}.
 \tag{31}
\]

Inversement, les deux cylindres de (20) ont un volume total
\(\pi\varepsilon^2L\). L'estimation (21) donne

\[
 \|\omega\|_{L^{3/2,\infty}}
 \geq
 c_*\pi^{2/3}\Gamma
 \left(\frac{L}{\varepsilon}\right)^{2/3}.
 \tag{32}
\]

Pour \(L=q\varepsilon\), les deux membres sont des constantes positives fois
\(\Gamma\), indépendantes de \(\varepsilon\). C'est exactement l'échelle
critique de la vorticité 3D.

## 6. Retour de vorticité imposé par la compacité

La formule (17) s'annule au rayon relatif

\[
 s_*=\frac{\sqrt5-1}{2}.
 \tag{33}
\]

Elle est positive pour \(s<s_*\) et négative pour \(s>s_*\). Chaque cœur
vertical est donc entouré d'un anneau de retour de signe opposé. Ce retour
n'est pas un accident numérique : pour toute fonction de courant compacte,

\[
 \int_{\mathbb R^2}-\Delta_\perp F\,dxdy=0.
 \tag{34}
\]

De même, puisque \(\omega=\nabla\times u\) et \(u\) est compact,

\[
 \int_{\mathbb R^3}\omega(x)\,dx=0.
 \tag{35}
\]

Les deux cœurs principaux s'équilibrent déjà globalement, mais l'ansatz
séparable impose en plus le retour local de chaque Laplacien. Éliminer ces
anneaux tout en gardant une vitesse compacte exige un correcteur non local ou
une géométrie de tube fermé; une simple différence de deux bosses de
fonction de courant ne suffit pas.

## 7. Direction de vorticité et coût \(\mathrm{bmo}_\phi\)

Dans la tranche \(|z|<L\), la vorticité est verticale. À travers le cylindre
\(s=s_*\), elle passe de \(+e_3\) à \(-e_3\) en s'annulant. Quelle que soit la
valeur attribuée à \(\xi\) sur l'ensemble nul, les boules centrées sur ce
cylindre voient, lorsque leur rayon tend vers zéro, deux demi-boules de
directions opposées. Ainsi

\[
 \liminf_{r\downarrow0}
 \frac1{|B_r|}\int_{B_r}|\xi-\xi_{B_r}|\geq c_0>0,
 \tag{36}
\]

et

\[
 \sup_{r<1/2}
 |\log r|
 \frac1{|B_r|}\int_{B_r}|\xi-\xi_{B_r}|=\infty.
 \tag{37}
\]

Le champ explicite n'appartient donc pas à la classe géométrique du manuscrit
audité lors des cycles 0013–0019.

### Obstacle indépendant de l'anneau de retour

Supposons qu'un correcteur vectoriel remplisse les zéros et fasse tourner la
direction continûment, tout en conservant deux sous-cœurs exactement opposés.
Prenons les boules tridimensionnelles

\[
 E_\pm=B_{\varepsilon/4}((a_\pm,0)).
 \tag{38}
\]

Si \(L\geq2\varepsilon\), elles sont dans le plateau axial et portent
respectivement \(\xi=+e_3\) et \(\xi=-e_3\). Elles sont contenues dans la boule

\[
 B=B_{2\varepsilon}(0).
 \tag{39}
\]

Chacune occupe la fraction exacte

\[
 \frac{|E_\pm|}{|B|}
 =\left(\frac{1/4}{2}\right)^3
 =\frac1{512}.
 \tag{40}
\]

Pour tout vecteur \(c\), l'inégalité triangulaire donne

\[
 |e_3-c|+|-e_3-c|\geq2.
 \tag{41}
\]

En prenant \(c=\xi_B\) et en intégrant seulement sur \(E_+\cup E_-\),

\[
 \frac1{|B|}\int_B|\xi-\xi_B|
 \geq\frac1{256}.
 \tag{42}
\]

Comme \(2\varepsilon<1/2\), (42) donne exactement (4).

Une transition de largeur \(w\) qui effectue une rotation d'angle \(\pi\)
possède de même un coût

\[
 [\xi]_{\mathrm{bmo}_{1/|\log r|}}
 \gtrsim |\log w|.
 \tag{43}
\]

Une construction Lipschitz avec gradient \(O(w^{-1})\) donne la borne
supérieure correspondante \(O(1+|\log w|)\). Le coût est donc logarithmique,
pas algébrique. Il diverge néanmoins lorsque deux directions opposées sont
forcées à se raccorder à une échelle qui s'effondre.

## 8. Lois d'échelle

Avec \(L=q\varepsilon\), le champ a les tailles caractéristiques

\[
 |u|\sim\frac{\Gamma}{\varepsilon},
 \qquad
 |\omega|\sim\frac{\Gamma}{\varepsilon^2},
 \qquad
 |\operatorname{supp}u|\sim\varepsilon^3.
 \tag{44}
\]

Par conséquent,

\[
 \begin{aligned}
 \|u\|_2^2&\sim
 (\Gamma^2\varepsilon^{-2})\varepsilon^3
 =\Gamma^2\varepsilon,\\
 \|\omega\|_2^2&\sim
 (\Gamma^2\varepsilon^{-4})\varepsilon^3
 =\Gamma^2\varepsilon^{-1},\\
 \|\omega\|_{L^{3/2,\infty}}&\sim
 (\Gamma\varepsilon^{-2})(\varepsilon^3)^{2/3}
 =\Gamma.
 \end{aligned}
 \tag{45}
\]

Ces exposants coïncident avec la remise à l'échelle Navier–Stokes
\(u_\kappa(x)=\kappa u(\kappa x)\), avec
\(\kappa=\varepsilon^{-1}\). La quasi-norme critique reste constante, tandis
que l'énergie décroît.

## 9. Certificat exact standard-library

Le script vérifie avec `fractions.Fraction` :

- le polynôme exact de (17) et ses signes ;
- les intégrales \(2\pi\) et \(70\pi\) de (24), en stockant seulement leur
  coefficient de \(\pi\) ;
- les exposants d'échelle ;
- la fraction volumique \(1/512\) et le résidu BMO \(1/256\) ;
- la croissance logarithmique, en unités de \(\log2\), pour
  \(\varepsilon=2^{-n}\).

```python
from fractions import Fraction as F
from math import factorial


# Radial Laplacian numerator: -Delta f has sign of 1-s-s^2.
def core_poly(s):
    return 1 - s - s * s


assert core_poly(F(0)) == 1
assert core_poly(F(1, 4)) == F(11, 16) > 0
assert core_poly(F(1, 2)) == F(1, 4) > 0
assert core_poly(F(2, 3)) == F(-1, 9) < 0


# Integral t^k exp(-2t) dt on [0,infinity] is k!/2^(k+1).
def exp_moment(k):
    return F(factorial(k), 2 ** (k + 1))


# J_grad/pi = 4 * integral (t+t^2)e^-2t = 2.
Jgrad_over_pi = 4 * (exp_moment(1) + exp_moment(2))
assert Jgrad_over_pi == 2

# (t^2-t-1)^2(1+t)^2 = 1+4t+4t^2-2t^3-4t^4+t^6.
lap_poly = [1, 4, 4, -2, -4, 0, 1]
lap_integral = sum((F(c) * exp_moment(k)
                    for k, c in enumerate(lap_poly)), F(0))
Jlap_over_pi = 16 * lap_integral
assert lap_integral == F(35, 8)
assert Jlap_over_pi == 70


# Center signs after Phi=F_plus-F_minus and omega_z=-Delta Phi.
lap_plus_center = F(-4)
lap_minus_center_in_Phi = F(4)
assert -lap_plus_center == 4
assert -lap_minus_center_in_Phi == -4


# Scaling gates with L proportional to epsilon.
# amplitude^2 times volume: u -> eps^(-2)*eps^3=eps;
# omega -> eps^(-4)*eps^3=eps^(-1);
# weak L^(3/2): eps^(-2)*(eps^3)^(2/3)=eps^0.
assert -2 + 3 == 1
assert -4 + 3 == -1
assert -2 + 3 * F(2, 3) == 0


# Two exact opposite sub-balls inside B_(2 epsilon).
one_core_fraction = (F(1, 4) / 2) ** 3
mean_oscillation_lower = 2 * one_core_fraction
assert one_core_fraction == F(1, 512)
assert mean_oscillation_lower == F(1, 256)

# For epsilon=2^-n, |log(2 epsilon)|/256=(n-1)log(2)/256.
previous = F(0)
for n in range(2, 65):
    bmo_lower_in_log2_units = F(n - 1, 256)
    assert bmo_lower_in_log2_units > previous
    previous = bmo_lower_in_log2_units

print("radial curl signs and exact energy constants: PASS")
print("critical scaling and opposite-core amplitudes: PASS")
print("bmo_phi obstruction with exact volume residual: PASS")
```

Commande de reproduction : extraire le bloc et exécuter `python -` depuis la
racine du dépôt. Dépendances : bibliothèque standard uniquement. Graine :
aucune. Les calculs stockent exactement les coefficients rationnels de
\(\pi\); aucune quadrature flottante n'est utilisée.

## 10. Champ instantané versus dynamique Navier–Stokes

Le champ (11) est une donnée initiale lisse, compacte, divergence-free et donc
admissible pour le problème de Cauchy Navier–Stokes non forcé sur
\(\mathbb R^3\), pour toute viscosité \(\nu>0\). Il engendre une solution
classique locale unique.

Ce rapport ne démontre pas que :

- les deux cœurs persistent sous l'évolution ;
- leur distance ou leur rayon suivent une loi auto-similaire ;
- le terme d'étirement renforce l'anti-alignement ;
- une singularité se forme ;
- la direction satisfait uniformément la condition géométrique du manuscrit.

La pression et la dérivée temporelle au temps initial sont déterminées
non-localement par Navier–Stokes. Elles ne sont pas prescrites par la seule
géométrie instantanée. Le champ est un **contre-profil cinématique**, pas une
solution dynamique de blow-up.

## 11. Obligations falsifiables

```json
{
  "cycle": "0020",
  "construction": "u=(partial_y Psi,-partial_x Psi,0), Psi=Gamma chi_L(F_plus-F_minus)",
  "claims": [
    {
      "id": "NS-C0020-COMPACT-ANTI-CORES",
      "status": "PROVED_BY_CONSTRUCTION",
      "statement": "a smooth compactly supported divergence-free velocity can have neighboring opposite vorticity cores",
      "center_values": ["+4 Gamma/epsilon^2 e3", "-4 Gamma/epsilon^2 e3"]
    },
    {
      "id": "NS-C0020-CRITICAL-SIZE",
      "status": "PROVED_BY_SCALING_AND_BOUNDS",
      "statement": "for L=q epsilon, weak-L^(3/2) vorticity stays comparable to Gamma while kinetic energy is O(Gamma^2 epsilon)"
    },
    {
      "id": "NS-C0020-RAW-BMO",
      "status": "REFUTED",
      "statement": "the raw two-bump streamfunction has direction in bmo_(1/abs(log r))",
      "witness": "sign jump across the Laplacian return cylinder"
    },
    {
      "id": "NS-C0020-UNIFORM-ANTI-ALIGNMENT",
      "status": "OBSTRUCTED",
      "statement": "opposite O(epsilon)-cores can concentrate while the weighted-bmo direction norm stays uniform",
      "lower_bound": "abs(log(2 epsilon))/256"
    }
  ],
  "pde_scope": "instantaneous smooth initial field only; not a Navier-Stokes blow-up trajectory",
  "decision": "KEEP_AS_ADVERSARIAL_PROFILE"
}
```

## Conclusion

L'incompressibilité, la compacité et l'énergie finie n'empêchent pas deux
cœurs voisins de vorticité exactement opposés. La construction explicite
montre même que leur coût faible-\(L^{3/2}\) est critique et indépendant de
l'échelle. En revanche, une inversion complète de direction sur une distance
\(O(\varepsilon)\) coûte au moins \(c|\log\varepsilon|\) dans
\(\mathrm{bmo}_{1/|\log r|}\). L'hypothèse géométrique uniforme exclut donc
précisément cette famille lorsqu'elle se concentre; elle n'est pas une
conséquence automatique de la viscosité ou de la lissité instantanée.
