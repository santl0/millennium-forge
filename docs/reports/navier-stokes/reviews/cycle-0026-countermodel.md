# Cycle 0026 — compensation conique et blob à deux niveaux

Date : 2026-08-14.

Type de passe : audit adverse de constantes et de quantificateurs. Cette
passe est produite par la même famille de modèles que la dérivation
principale; elle n'est donc pas une revue externe indépendante.

## Verdict

La famille mesurée à deux niveaux proposée est algébriquement correcte. Sur
un ensemble de volume un, avec une direction fixée \(e\in\mathbb S^2\), on
pose pour \(n\geq2\)

\[
 \varepsilon_n=n^{-3},\qquad
 a_n=\frac{n^2}{n^3-1},\qquad b_n=n^2,
 \tag{1}
\]

et

\[
 W_n= a_ne\,\mathbf 1_{G_n}-b_ne\,\mathbf 1_{B_n},
 \qquad |B_n|=\varepsilon_n,
 \qquad |G_n|=1-\varepsilon_n.
 \tag{2}
\]

Alors, exactement,

\[
 \int W_n=0,\qquad
 \|W_n\|_{L^{3/2,\infty}}=1,
 \qquad
 \int_{B_n}|W_n|=\frac1n,
 \tag{3}
\]

pour la quasi-norme de distribution précisée ci-dessous. De plus,

\[
 \int |W_n|^{3/2}
 =1+\frac1{\sqrt{n^3-1}},
 \tag{4}
\]

et l'oscillation moyenne de la direction sur l'ensemble entier vaut

\[
 \operatorname{MO}_{G_n\cup B_n}(\xi_n)
 =4\varepsilon_n(1-\varepsilon_n).
 \tag{5}
\]

Ces identités réfutent toute implication de la forme

\[
 \text{moyenne vectorielle nulle + contrôle critique}
 \Longrightarrow
 \text{volume uniforme dans le contre-cône ou MO uniforme}.
 \tag{6}
\]

L'inégalité conique correcte est seulement une compensation en masse
\(L^1\) : si \(G_\theta=\{e\mathbin\cdot W\geq
\cos\theta |W|\}\), \(0\leq\theta<\pi/2\), et
\(\int W=0\), alors

\[
 \int_{G_\theta^c}|W|
 \geq \cos\theta\int_{G_\theta}|W|.
 \tag{7}
\]

Elle ne donne ni une mesure de Lebesgue minimale, ni une oscillation BMO.
Dans (2), les deux masses \(L^1\) opposées valent \(1/n\), tandis que le
contre-cône n'occupe que \(n^{-3}\) et porte asymptotiquement toute la masse
\(L^{3/2}\) forte.

Il faut toutefois séparer deux conclusions BMO :

1. la petite valeur (5) est la moyenne sur **un ensemble prescrit**, pas le
   semi-norme BMO, qui prend un supremum sur toutes les boules ou tous les
   cubes;
2. si les deux phases se touchent par une interface régulière, une petite
   boule demi-remplie donne une oscillation exactement égale à un;
3. si les phases sont séparées par une région où \(W=0\), un prolongement
   unitaire logarithmique peut étaler la rotation de \(-e\) vers \(e\) et
   réduire le BMO à \(O(1/\log(R/h))\). Un défaut d'ordre un n'est donc pas
   imposé par les seuls moments et volumes.

Enfin, (2) n'est pas encore une vorticité compacte admissible. Un champ
exactement collinéaire \(W=f e\), divergence-free et compactement supporté
dans \(\mathbb R^3\), est nécessairement nul. Tout relèvement non trivial
\(W=\nabla\times U\) doit ajouter des composantes transverses, fermer les
lignes de vorticité, ou séparer les phases par des zéros. Ce passage peut
réintroduire une transition directionnelle; aucune borne uniforme d'ordre un
n'est cependant démontrée sans une hypothèse géométrique supplémentaire.

## 1. Cadre exact et conventions

Cette section est purement cinématique. Elle ne suppose ni l'équation de
Navier--Stokes, ni une pression, ni une évolution temporelle. On prend un
ensemble mesurable \(Q\subset\mathbb R^3\) de volume un et une partition
\(Q=G_n\mathbin\dot\cup B_n\), modulo les ensembles nuls, avec les mesures de
(2).

Pour \(f\) mesurable, la convention faible utilisée est

\[
 \|f\|_{L^{3/2,\infty}}
 :=\sup_{\lambda>0}
 \lambda\,|\{|f|>\lambda\}|^{2/3}.
 \tag{8}
\]

Pour un champ unitaire \(\xi\) sur un ensemble \(E\) de mesure positive,

\[
 \xi_E=\dashint_E\xi,
 \qquad
 \operatorname{MO}_E(\xi)
 =\dashint_E|\xi-\xi_E|.
 \tag{9}
\]

La valeur exacte un de (3) dépend de (8). Une norme de Lorentz équivalente
fondée sur \(f^{**}\) change la constante. Cette dépendance de convention ne
change aucun des passages à zéro utilisés dans la réfutation.

## 2. Vérification exacte du profil à deux niveaux

### 2.1 Annulation vectorielle et masses coniques

Les deux masses orientées valent

\[
 (1-\varepsilon_n)a_n
 =\frac{n^3-1}{n^3}\frac{n^2}{n^3-1}
 =\frac1n,
 \qquad
 \varepsilon_n b_n=\frac1n.
 \tag{10}
\]

Donc la moyenne vectorielle s'annule. Pour tout cône strict d'axe \(e\) et
de demi-angle inférieur à \(\pi/2\), la phase \(G_n\) est dans le cône et la
phase \(B_n\) dans le contre-cône. Sa masse absolue est \(1/n\), son volume
est \(n^{-3}\), et sa proportion de la masse \(L^1\) totale reste \(1/2\).
Il serait donc également erroné de dire que la compensation est petite en
**masse relative**.

### 2.2 Quasi-norme faible critique

Pour \(n\geq2\), on a \(0<a_n<1<b_n\). La fonction de distribution de
\(|W_n|\), avec le signe strict de (8), est

\[
 |\{|W_n|>\lambda\}|=
 \begin{cases}
 1,&0<\lambda<a_n,\\
 \varepsilon_n,&a_n\leq\lambda<b_n,\\
 0,&\lambda\geq b_n.
 \end{cases}
 \tag{11}
\]

Par conséquent

\[
 \|W_n\|_{L^{3/2,\infty}}
 =\max\{a_n,b_n\varepsilon_n^{2/3}\}
 =\max\{a_n,1\}=1.
 \tag{12}
\]

Le supremum associé au second niveau est une limite lorsque
\(\lambda\uparrow b_n\); il n'est pas atteint avec la convention stricte.

### 2.3 Masse forte critique et coût supercritique

Le calcul fort donne

\[
\begin{aligned}
 \int_Q|W_n|^{3/2}
 &=(1-\varepsilon_n)a_n^{3/2}
   +\varepsilon_n b_n^{3/2}\\
 &=\frac1{\sqrt{n^3-1}}+1.
\end{aligned}
\tag{13}
\]

La masse est donc comprise entre \(1\) et \(1+1/\sqrt7\), puis converge vers
un. Sa partie portée par \(B_n\) vaut exactement un. La partie conique
majoritaire en volume ne porte plus qu'une masse critique
\(1/\sqrt{n^3-1}\).

En revanche,

\[
 \int_Q|W_n|^2
 =n+\frac{n}{n^3-1},
 \tag{14}
\]

qui diverge. La famille ne fournit donc aucun contrôle uniforme de
l'enstrophie.

### 2.4 Oscillation sur le blob entier

La direction active est \(e\) sur \(G_n\) et \(-e\) sur \(B_n\). Sa moyenne
vaut \((1-2\varepsilon_n)e\). Les deux écarts à la moyenne ont les modules
\(2\varepsilon_n\) et \(2(1-\varepsilon_n)\). Ainsi

\[
\begin{aligned}
 \operatorname{MO}_Q(\xi_n)
 &=(1-\varepsilon_n)2\varepsilon_n
   +\varepsilon_n2(1-\varepsilon_n)\\
 &=4\varepsilon_n(1-\varepsilon_n).
\end{aligned}
\tag{15}
\]

Si ce blob est placé à une échelle physique
\(\ell_n\asymp2^{-n}/n\), la contribution du **seul cube entier** au test
logarithmique est

\[
 |\log\ell_n|\operatorname{MO}_Q(\xi_n)
 =O(n\,n^{-3})=O(n^{-2}).
 \tag{16}
\]

Cette observation ne contrôle pas les sous-cubes.

## 3. Ce que l'inégalité conique dit réellement

Soit \(W\in L^1(\mathbb R^3;\mathbb R^3)\), avec \(\int W=0\), et soit
\(c=\cos\theta>0\). Sur \(G_\theta\),
\(e\mathbin\cdot W\geq c|W|\); sur son complément, on dispose seulement de
\(e\mathbin\cdot W\geq-|W|\). Il vient

\[
 0=\int e\mathbin\cdot W
 \geq c\int_{G_\theta}|W|
      -\int_{G_\theta^c}|W|,
 \tag{17}
\]

d'où (7). En particulier,

\[
 \int_{G_\theta^c}|W|
 \geq\frac{c}{1+c}\int|W|.
 \tag{18}
\]

La constante un pour le cône dégénéré d'angle zéro est saturée par (2). Pour
un angle positif, la constante \(c\) de (17) est optimale si la direction de
la bonne phase approche le bord du cône et la mauvaise direction approche
\(-e\).

Les quantificateurs indispensables sont :

- \(W\in L^1\), afin que la moyenne vectorielle soit définie;
- une annulation sur le même domaine que les deux intégrales;
- un axe **fixe** \(e\), et non un axe dépendant de \(x\) ou de l'échelle;
- un cône strict, \(c>0\);
- une masse pondérée par \(|W|\), pas une mesure de l'ensemble des directions.

Pour \(W=\nabla\times U\) avec \(U\in C_c^1(\mathbb R^3)\), l'annulation
\(\int W=0\) suit par intégration des dérivées. Elle est globale. Elle ne
donne pas \(\int_BW=0\) sur chaque boule : une localisation produit un flux
de bord. Appliquer (17) indépendamment sur chaque boule sans ce terme est une
inversion de quantificateur.

## 4. Contre-exemples aux extrapolations de constantes

La famille (2) donne simultanément :

| Extrapolation proposée | Contre-calcul |
|---|---|
| \(\int_{G^c}|W|\geq c_0\|W\|_{L^{3/2,\infty}}\) avec \(c_0>0\) universel | membre gauche \(1/n\), quasi-norme égale à un |
| \(|G^c|\geq c_0\) depuis la moyenne nulle | \(|G^c|=n^{-3}\) |
| MO de la direction au moins \(c_0\) sur le blob entier | MO \(=4n^{-3}(1-n^{-3})\) |
| masse \(L^{3/2}\) majoritairement dans la phase majoritaire en volume | la mauvaise phase porte exactement un; la bonne tend vers zéro |
| contrôle critique implique enstrophie uniforme | l'enstrophie abstraite croît comme \(n\) |
| annulation globale implique compensation sur toute boule | le terme de bord local n'est pas nul |

La première ligne n'est pas une simple rescaling d'amplitude : la
quasi-norme critique est déjà normalisée à un et la masse forte critique
reste d'ordre un. L'échec provient de la concentration.

## 5. Moyenne sur un blob contre semi-norme BMO

### 5.1 Une interface directe redonne une oscillation d'ordre un

Pour deux directions antipodales occupant des fractions \(p\) et \(1-p\)
d'un cube \(K\), le calcul de (15) donne

\[
 \operatorname{MO}_K(\xi)=4p(1-p).
 \tag{19}
\]

Si \(B_n\) est, par exemple, un petit cube inclus dans \(Q\) et partage une
face régulière avec \(G_n\), il existe des cubes arbitrairement petits
centrés sur l'intérieur de cette face pour lesquels \(p=1/2\). Alors

\[
 \|\xi_n\|_{\mathrm{BMO}}
 \geq 1,
 \tag{20}
\]

malgré (15). Toute conclusion BMO tirée seulement de la moyenne sur \(Q\)
est donc fausse.

Le même phénomène apparaît pour un lissage scalaire qui traverse zéro : de
part et d'autre d'une surface nodale régulière, \(W/|W|\) tend vers \(e\) et
\(-e\). La valeur choisie exactement sur la surface, de mesure nulle, ne
change pas (20).

### 5.2 Un prolongement unitaire peut éviter le saut brutal

L'ordre un n'est pourtant pas une conséquence des deux phases seules.
Supposons une boule négative \(B_h(0)\), une phase positive située au-delà de
\(B_R(0)\), et \(W=0\) dans le corridor \(h<|x|<R\). Sur les zéros, posons

\[
 \vartheta(r)=
 \begin{cases}
 \pi,&r\leq h,\\
 \displaystyle\pi\frac{\log(R/r)}{\log(R/h)},&h<r<R,\\
 0,&r\geq R,
 \end{cases}
 \qquad
 \widetilde\xi(x)=(\sin\vartheta(|x|),0,\cos\vartheta(|x|)).
 \tag{21}
\]

Ce prolongement est unitaire, vaut \(-e_3\) dans le cœur et \(e_3\) à
l'extérieur. Comme \(\log|x|\in\mathrm{BMO}(\mathbb R^3)\), la troncature
scalaire est lipschitzienne, et l'application
\(t\mapsto(\sin t,0,\cos t)\) est lipschitzienne, l'estimation standard donne

\[
 \|\widetilde\xi\|_{\mathrm{BMO}}
 \leq \frac{C}{\log(R/h)}.
 \tag{22}
\]

Cette borne peut aussi être obtenue directement : sur les boules éloignées
de zéro on utilise \(r|\vartheta'(r)|\leq
\pi/\log(R/h)\); sur les boules rencontrant zéro on compare à une boule
concentrique et on intègre la fonction logarithmique. La constante \(C\) ne
dépend ni de \(h\), ni de \(R\).

Ainsi une affirmation « tout prolongement unitaire coûte une constante BMO
universelle » est fausse lorsque le rapport \(R/h\) peut croître.

### 5.3 Le coût logarithmique est aussi nécessaire dans ce modèle

Soit \(\delta=\|\widetilde\xi\|_{\mathrm{BMO}}\), avec la définition par
boules. Pour deux boules concentriques \(B_r\subset B_{2r}\) en dimension
trois,

\[
 |\widetilde\xi_{B_r}-\widetilde\xi_{B_{2r}}|
 \leq 8\delta.
 \tag{23}
\]

Partant de \(B_h\), où la moyenne est \(-e_3\), on double le rayon jusqu'à
\(B_{2^m h}\), dont le rayon appartient à \([2R,4R)\). La composante selon
\(e_3\) de la moyenne finale est au moins \(3/4\) : la partie extérieure à
\(B_R\), de fraction au moins \(7/8\), vaut \(e_3\), et le huitième restant
est au pire \(-e_3\). Avec

\[
 m=\left\lceil\log_2(2R/h)\right\rceil,
 \tag{24}
\]

le télescopage de (23) donne

\[
 \delta\geq\frac{7}{32m}.
 \tag{25}
\]

Les bornes (22) et (25) montrent un coût
\(\Theta(1/\log(R/h))\), à constantes près, pour ce problème annulaire. Si
la mauvaise phase est une boule de fraction \(n^{-3}\) dans une boule unité,
alors \(h/R\asymp n^{-1}\). Le coût peut donc tendre vers zéro, mais seulement
comme \(1/\log n\). Après insertion à l'échelle
\(\ell_n\asymp2^{-n}/n\), le poids logarithmique global produit encore

\[
 |\log\ell_n|\,\delta_n
 \gtrsim \frac{n}{\log n}\longrightarrow\infty.
 \tag{26}
\]

Cette conclusion est conditionnelle à une épaisseur géométrique comparable
à une boule. Le seul volume \(n^{-3}\) n'assure aucun rayon intérieur : une
phase fractale, feuilletée ou très allongée échappe à (25) sous cette forme.

## 6. Le profil collinéaire ne se relève pas directement en curl compact

Supposons \(W=f e\in\mathcal D'(\mathbb R^3;\mathbb R^3)\), de support
compact, et \(\nabla\mathbin\cdot W=0\). Après rotation, \(e=e_3\), donc

\[
 \partial_3 f=0
 \tag{27}
\]

au sens des distributions. Le champ \(f\) est indépendant de \(x_3\). Un tel
champ ne peut être à la fois non nul et compactement supporté dans la
direction \(x_3\). Par conséquent

\[
 W=f e,\quad \operatorname{supp}W\Subset\mathbb R^3,
 \quad\nabla\mathbin\cdot W=0
 \quad\Longrightarrow\quad W=0.
 \tag{28}
\]

Or toute vorticité \(W=\nabla\times U\) est divergence-free. Le profil (2),
pris littéralement dans un domaine compact tridimensionnel, ne peut donc pas
être le curl d'un \(U\in C_c^\infty(\mathbb R^3)\).

L'annulation vectorielle n'est qu'une condition nécessaire. Elle ne remplace
pas (27). Une projection de Leray du champ étagé corrige la divergence mais
est non locale et détruit en général le support compact. Une correction
locale de type Bogovskii conserve le support dans un domaine étoilé, mais sa
norme n'est pas petite par la seule petitesse de \(|B_n|\); elle peut modifier
la direction sur les deux niveaux.

### 6.1 Trois géométries de relèvement et leurs défauts

**Lift périodique scalaire.** Sur \(\mathbb T^3\), un champ
\(W=f(x_1,x_2)e_3\) est divergence-free. Si sa moyenne est nulle, il possède
un potentiel vectoriel périodique. Cela montre que l'obstruction (28) est
spécifique au support compact dans \(\mathbb R^3\). Mais un lissage scalaire
qui relie les deux signes traverse une courbe nodale; la direction a alors
le saut antipodal de (20). Ce lift direct ne résout pas la porte BMO.

**Lift axisymétrique.** Pour un potentiel azimutal
\(U=\psi(r,z)e_\theta\),

\[
 \nabla\times U
 =-\partial_z\psi\,e_r
  +\frac1r\partial_r(r\psi)\,e_z.
 \tag{29}
\]

On peut imposer deux plateaux verticaux dans une tranche où
\(\partial_z\psi=0\), avec flux radial total nul. Cependant tout cutoff en
\(z\) crée le terme radial \(-\partial_z\psi e_r\). Dans une région où le
plateau vertical s'annule, même un terme radial de petite amplitude fixe la
direction normalisée. Sa petite amplitude ne suffit donc pas à obtenir un
petit BMO directionnel.

**Tube fermé à section variable.** Un tube de flux peut porter une branche
large d'amplitude \(a_n\) et une branche étroite d'amplitude \(b_n\), le flux
conservé valant \(1/n\). Il faut néanmoins fermer le tube et tourner sa
tangente de \(e\) vers \(-e\). Une courbure concentrée à l'échelle de la
section produit une boule d'oscillation d'ordre un. Une courbure étalée peut
réduire cette oscillation, mais le calcul annulaire (22)--(25) indique un
coût logarithmique tant qu'un rapport géométrique contrôlé relie les deux
branches.

Aucune de ces observations ne prouve un no-go pour tous les curls compacts.
Elles montrent exactement l'hypothèse manquante : une borne de capacité,
d'épaisseur ou de longueur de raccord transformant la compensation en une
minoration BMO quantitative.

## 7. Pression, énergie et portée Clay

Le modèle mesuré ne détermine pas une vitesse. Même après construction d'un
curl compact, il faudrait reconstruire \(U\), contrôler sa norme \(L^2\), et
suivre les constantes sous rescaling. Les nombres (3)--(5) ne contrôlent pas
la norme négative \(\dot H^{-1}\) qui gouverne l'énergie de Biot--Savart.

La pression de Navier--Stokes dépendrait ensuite de

\[
 -\Delta p=\partial_i\partial_j(U_iU_j),
 \tag{30}
\]

et non de la seule distribution de \(|W|\). Ni (7), ni l'annulation
\(\int W=0\) ne contrôlent ces interactions non locales.

Enfin, un champ statique \(W=\nabla\times U\) ne constitue pas une solution
de Navier--Stokes. Il faudrait vérifier l'équation, la donnée initiale lisse,
le résidu, l'évolution et un scénario à temps maximal. Le présent résultat
ne démontre ni régularité, ni blow-up pour l'une des formulations Clay.

## 8. Certificat reproductible en bibliothèque standard

Le script suivant vérifie les identités rationnelles, les deux candidats
exacts de la quasi-norme faible, les masses forte et quadratique, la formule
d'oscillation, la saturation conique à angle zéro et l'échelle logarithmique
du test annulaire.

```python
from fractions import Fraction as F
from math import ceil, log, pi, sqrt


def parameters(n):
    assert n >= 2
    eps = F(1, n**3)
    a = F(n**2, n**3 - 1)
    b = F(n**2, 1)
    return eps, a, b


for n in list(range(2, 65)) + [128, 256, 1024]:
    eps, a, b = parameters(n)

    good_l1 = (1 - eps) * a
    bad_l1 = eps * b
    assert good_l1 == F(1, n)
    assert bad_l1 == F(1, n)
    assert good_l1 - bad_l1 == 0

    weak_low_level = a
    weak_high_level = float(b) * float(eps) ** (2.0 / 3.0)
    assert a < 1
    assert abs(weak_high_level - 1.0) < 2e-14
    assert max(float(weak_low_level), weak_high_level) == weak_high_level

    strong = float(1 - eps) * float(a) ** 1.5 + float(eps) * float(b) ** 1.5
    strong_closed = 1.0 + 1.0 / sqrt(n**3 - 1)
    assert abs(strong - strong_closed) < 2e-13
    assert 1.0 < strong <= 1.0 + 1.0 / sqrt(7)

    enstrophy = (1 - eps) * a * a + eps * b * b
    assert enstrophy == F(n, 1) + F(n, n**3 - 1)

    direction_mo = 4 * eps * (1 - eps)
    direct_definition = (1 - eps) * 2 * eps + eps * 2 * (1 - eps)
    assert direction_mo == direct_definition

    # theta=0: bad L1 >= good L1 is saturated.
    assert bad_l1 == good_l1

# A half-filled local cube has order-one antipodal oscillation.
p = F(1, 2)
assert 4 * p * (1 - p) == 1

# Spherical bad phase: volume fraction h^3=n^-3, hence h=1/n.
# The nested-ball lower bound is 7/(32 ceil(log_2(2/h))).
weighted_lower = []
for k in range(3, 13):
    n = 2**k
    h = 1.0 / n
    m = ceil(log(2.0 / h, 2.0))
    lower = 7.0 / (32.0 * m)
    assert m == k + 1
    assert lower > 0.0

    # Angular change per dyadic logarithmic shell for (21).
    shell_rotation = pi * log(2.0) / log(1.0 / h)
    assert abs(shell_rotation - pi / k) < 2e-15

    physical_log_weight = n * log(2.0) + log(n)
    weighted_lower.append(physical_log_weight * lower)

assert weighted_lower[-1] > weighted_lower[0]
assert weighted_lower[-1] > 40.0

print("two-level cancellation and Lorentz normalization: PASS")
print("critical mass, enstrophy and directional MO: PASS")
print("cone saturation and logarithmic extension scale: PASS")
```

Commande de reproduction : extraire le bloc Python puis exécuter python -
depuis la racine du dépôt. Dépendances : bibliothèque standard Python.
Graine aléatoire : aucune. Les identités de moyenne, \(L^1\), \(L^2\) et MO
sont rationnelles exactes. Les seules tolérances flottantes concernent les
puissances \(3/2\) et les logarithmes explicitement affichés.

## 9. Prochain test discriminant

Le prochain test doit séparer « coût BMO d'ordre un » et « coût seulement
logarithmique » dans un véritable curl compact.

**Lemme actif.** Soit \(W_n\in C_c^\infty(B_1;\mathbb R^3)\),
\(\nabla\mathbin\cdot W_n=0\), avec une phase presque parallèle à \(e\) de
volume d'ordre un et un compensateur presque parallèle à \(-e\), de volume
\(n^{-3}\) et de masse \(L^1\) \(1/n\). Sous une hypothèse explicite
d'épaisseur ou de capacité du compensateur, démontrer soit

\[
 \inf_{\widetilde\xi= W_n/|W_n|\text{ sur }\{W_n\ne0\}}
 \|\widetilde\xi\|_{\mathrm{BMO}}
 \gtrsim \frac1{\log n},
 \tag{31}
\]

soit construire une famille violant (31). Le volume seul ne doit pas être
utilisé comme substitut de capacité.

**Expérience décisive.** Construire le lift axisymétrique (29) avec fonctions
plateau lisses et paramètres rationnels, puis mesurer séparément :

1. \(\nabla\mathbin\cdot W_n\) et l'identité curl, qui doivent être exactes
   analytiquement;
2. la distribution faible-\(L^{3/2}\), la masse forte critique et
   \(\|W_n\|_{\dot H^{-1}}\);
3. le supremum d'oscillation sur des boules centrées aux interfaces radiale
   et axiale;
4. la contribution forcée par le cutoff
   \(-\partial_z\psi\,e_r\);
5. le meilleur prolongement unitaire dans les régions de vorticité nulle.

Si une boule d'interface conserve une MO minorée indépendamment de \(n\),
l'ansatz axisymétrique est abandonné. Si toutes les minorations décroissent,
la géométrie est remise à l'échelle dans le train du cycle 0025 et le produit
\(|\log\ell_n|\operatorname{MO}\) devient le test final.

```json
{
  "cycle": "0026",
  "claim": "CONE_COMPENSATION_TO_BMO",
  "status": "REFUTED_WITHOUT_GEOMETRIC_THICKNESS",
  "proved": [
    "sharp amplitude-weighted L1 cone compensation",
    "exact two-level weak-L3/2 normalization and critical mass",
    "no nonzero compactly supported collinear divergence-free lift",
    "conditional annular BMO cost comparable to one over log scale ratio"
  ],
  "not_proved": [
    "order-one BMO cost for every compact curl lift",
    "existence of a smooth compact two-level lift preserving all critical bounds",
    "any Navier-Stokes evolution or Clay-admissible singularity"
  ],
  "next_test": "axisymmetric compact-curl lift plus interface-ball BMO audit"
}
```
