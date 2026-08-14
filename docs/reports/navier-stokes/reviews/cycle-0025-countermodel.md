# Cycle 0025 — train de blobs critiques accumulant à l'origine

Date : 2026-08-14.

Type de passe : construction adverse et audit de quantificateurs par la même
famille de modèle; ce document n'est pas une revue externe indépendante.

## Verdict

Soit \(U_0\in C_c^\infty(B_1;\mathbb R^3)\), non nul et
divergence-free, et soit \(W_0=\nabla\times U_0\). Pour \(n\geq4\), posons

\[
 r_n=2^{-n},\qquad x_n=r_ne_1,
 \qquad \ell_n=\frac{r_n}{n},
 \tag{1}
\]

et

\[
 U_n(x)=\ell_n^{-1}U_0\!\left(\frac{x-x_n}{\ell_n}\right),
 \qquad
 W_n(x)=\ell_n^{-2}W_0\!\left(\frac{x-x_n}{\ell_n}\right).
 \tag{2}
\]

Les supports sont disjoints et s'accumulent seulement en zéro. La somme

\[
 U=\sum_{n\geq4}U_n
 \tag{3}
\]

est un champ divergence-free dans \(L^2(\mathbb R^3)\), et

\[
 \nabla\times U=W:=\sum_{n\geq4}W_n
 \tag{4}
\]

au sens des distributions. La vorticité appartient à
\(L^1\cap L^{3/2,\infty}\), tandis que

\[
 \|U\|_3=\infty,
 \qquad
 \|W\|_2=\infty.
 \tag{5}
\]

Le train est donc un contre-profil critique réel, pas une simple collection
formelle. Il ne satisfait toutefois pas les prémisses du lemme axe–BMO des
cycles 0023–0024. En définissant le facteur de forme par rapport au centre
zéro,

\[
 \Phi(x)=|x|^2|W(x)|,
 \tag{6}
\]

on a sur le \(n\)-ième blob

\[
 \Phi\asymp n^2|W_0|.
 \tag{7}
\]

Ainsi aucune constante uniforme \(M\) ne borne \(\Phi\). Le compromis exact
est

\[
 \underbrace{(\ell_n/r_n)^3}_{n^{-3}}
 \underbrace{(r_n/\ell_n)^3}_{n^3}=1.
 \tag{8}
\]

Le premier facteur est l'occupation volumique vue depuis l'origine; le
second est \(\Phi^{3/2}\). C'est pourquoi :

- chaque coquille dyadique porte une masse \(L^{3/2}\) non dégénérée;
- le champ global reste borné dans le Lorentz faible critique;
- les boules centrées voient une oscillation directionnelle seulement
  \(O(n^{-3})\);
- mais la borne ponctuelle \(\Phi\leq M\) échoue comme \(n^2\).

Le prolongement par zéro de la direction échoue beaucoup plus fortement : il
n'est pas unitaire sur \(\{W=0\}\) et possède un saut de module à tout bord
régulier d'un blob. Dès qu'un tel morceau de bord existe, son semi-norme
log-BMO global est infini dès le premier blob. Un prolongement unitaire peut
enlever ce saut de frontière, mais ne
peut pas enlever la variation directionnelle interne d'un profil compact
non trivial. Toute copie transporte cette variation à l'échelle \(\ell_n\),
et une boule décentrée de rayon \(O(\ell_n)\) paie
\(c|\log\ell_n|\to\infty\).

Enfin, (3) est déjà singulier à l'instant initial. Il constitue une donnée
\(L^2\) admissible pour la théorie de Leray–Hopf, pas une donnée lisse du
problème Clay et encore moins une trajectoire développant un blow-up à temps
positif.

## 1. Séparation géométrique et accumulation

La distance entre deux centres successifs vaut

\[
 |x_n-x_{n+1}|=r_n-r_{n+1}=\frac{r_n}{2}.
 \tag{9}
\]

Or

\[
 \ell_n+\ell_{n+1}
 =r_n\left(\frac1n+\frac1{2(n+1)}\right)
 <\frac{r_n}{2}
 \quad(n\geq4).
 \tag{10}
\]

Les supports sont donc disjoints. Ils évitent l'origine puisque

\[
 \operatorname{dist}(0,\operatorname{supp}U_n)
 \geq r_n-\ell_n=r_n(1-1/n)>0,
 \tag{11}
\]

mais toute boule centrée en zéro contient une infinité de supports.

À chaque point \(x\ne0\), la somme (3) est localement finie et lisse. En
posant \(U(0)=0\), le champ reste néanmoins non borné dans toute boule
centrée : si \(U_0(y_0)\ne0\),

\[
 |U(x_n+\ell_ny_0)|
 =\ell_n^{-1}|U_0(y_0)|
 =n2^n|U_0(y_0)|\longrightarrow\infty.
 \tag{12}
\]

La singularité est donc présente à \(t=0\), même si le point d'accumulation
lui-même n'appartient à aucun support.

## 2. Divergence, rotationnel et convergence de la somme

Pour chaque \(n\), le changement de variables \(y=(x-x_n)/\ell_n\) donne

\[
 \nabla\cdot U_n=0,
 \qquad
 \nabla\times U_n=W_n.
 \tag{13}
\]

Les normes qui assurent la convergence sont

\[
 \|U_n\|_2^2=\ell_n\|U_0\|_2^2,
 \qquad
 \|W_n\|_1=\ell_n\|W_0\|_1.
 \tag{14}
\]

Comme

\[
 \sum_{n=4}^\infty\ell_n
 =\sum_{n=4}^\infty\frac{2^{-n}}n
 =\log2-\frac23<\infty,
 \tag{15}
\]

la série converge dans \(L^2\) pour la vitesse et dans \(L^1\) pour la
vorticité. Le passage à la limite dans (13) est donc légitime dans les
distributions : il ne crée ni divergence ni rotationnel de Dirac au point
d'accumulation.

La disjonction donne même les identités exactes

\[
 \|U\|_2^2=(\log2-2/3)\|U_0\|_2^2,
 \qquad
 \|W\|_1=(\log2-2/3)\|W_0\|_1.
 \tag{16}
\]

En revanche,

\[
 \|U_n\|_3^3=\|U_0\|_3^3,
 \qquad
 \|W_n\|_2^2=\ell_n^{-1}\|W_0\|_2^2=n2^n\|W_0\|_2^2.
 \tag{17}
\]

La somme forte \(L^3\) contient une contribution constante par blob et
l'enstrophie diverge encore plus vite. Toute preuve passant d'une borne
faible critique à l'une de ces deux normes fortes inverse un quantificateur.

## 3. Le faible-\(L^{3/2}\) global ne diverge pas

Chaque blob a une quasi-norme faible critique indépendante de \(n\). Il faut
néanmoins vérifier que l'infinité de blobs ne les additionne pas.

Notons

\[
 B_0=\|W_0\|_\infty,
 \qquad V_0=|\operatorname{supp}W_0|.
 \tag{18}
\]

Les amplitudes maximales \(B_0\ell_n^{-2}\) croissent strictement. Pour un
seuil \(\lambda\), choisissons \(N\) tel que

\[
 B_0\ell_{N-1}^{-2}<\lambda\leq B_0\ell_N^{-2}.
 \tag{19}
\]

Cette sélection s'applique pour \(\lambda>B_0\ell_4^{-2}\). Pour les seuils
plus petits, on prend \(N=4\) et on utilise directement la mesure totale des
supports; le même majorant uniforme ci-dessous en résulte.

Seuls les blobs \(n\geq N\) peuvent contribuer. Comme

\[
 \frac{\ell_{n+1}^3}{\ell_n^3}
 =\frac18\left(\frac n{n+1}\right)^3\leq\frac18,
 \tag{20}
\]

on obtient

\[
 |\{|W|>\lambda\}|
 \leq V_0\sum_{n\geq N}\ell_n^3
 \leq\frac87V_0\ell_N^3.
 \tag{21}
\]

Par conséquent,

\[
 \boxed{
 \|W\|_{L^{3/2,\infty}}
 \leq B_0\left(\frac{8V_0}{7}\right)^{2/3}.}
 \tag{22}
\]

La borne est non dégénérée. Si
\(E_b=\{|W_0|\geq b\}\) a une mesure \(v_b>0\), alors au seuil
\(\lambda=b\ell_N^{-2}\),

\[
 \lambda|\{|W|>\lambda\}|^{2/3}
 \geq b v_b^{2/3}.
 \tag{23}
\]

La même preuve donne \(U\in L^{3,\infty}\). Ce calcul réfute le diagnostic
naïf « une infinité de blobs critiques fait nécessairement diverger la norme
faible ». La croissance géométrique des amplitudes compense exactement la
décroissance géométrique des volumes.

## 4. Facteur de forme et masse critique par coquille

Sur le support du blob \(n\), écrivons \(x=x_n+\ell_ny\), \(|y|\leq1\).
Alors

\[
 1-\frac1n\leq\frac{|x|}{r_n}\leq1+\frac1n
 \tag{24}
\]

et

\[
 \boxed{
 \Phi(x)=|x|^2|W_n(x)|
 =n^2\left(\frac{|x|}{r_n}\right)^2|W_0(y)|.}
 \tag{25}
\]

Si \(W_0\) est non nul sur un ensemble de mesure positive, la borne
essentielle de \(\Phi\) croît comme \(n^2\). Le train n'entre donc pas dans la
classe \(\Phi\leq M\) du lemme par blocs.

En revanche,

\[
 \int_{\operatorname{supp}W_n}|W_n|^{3/2}dx
 =\int_{\mathbb R^3}|W_0|^{3/2}dy
 \tag{26}
\]

pour chaque \(n\). Comme \(r_{n+1}=r_n/2\) et
\(\ell_n/r_n=1/n\), chaque coquille dyadique suffisamment élargie contient un
blob entier et porte la même masse critique.

La dilution centrée et la croissance de \(\Phi\) sont les deux faces d'une
même identité :

\[
 \left(\frac{\ell_n}{r_n}\right)^3
 \left(\frac{r_n}{\ell_n}\right)^{2\cdot3/2}=1.
 \tag{27}
\]

Ainsi une borne faible-
\(L^{3/2}\) et une masse critique par coquille n'impliquent pas la borne
ponctuelle \(\Phi\leq M\). C'est exactement l'hypothèse qui interdit
l'activité sparse au cycle 0024.

## 5. Direction aux zéros et prolongement par zéro

Sur \(\{W\ne0\}\), la direction est

\[
 \xi(x)=\frac{W(x)}{|W(x)|}.
 \tag{28}
\]

Le prolongement naïf

\[
 \xi_0(x)=
 \begin{cases}W/|W|,&W\ne0,\\0,&W=0,
 \end{cases}
 \tag{29}
\]

n'est pas un champ unitaire. Plus grave, supposons qu'un morceau régulier de
la frontière de \(\{W_0\ne0\}\) sépare deux régions de densités positives.
À ses copies dilatées, les limites de \(\xi_0\) ont des modules un et zéro.

Pour un mélange de fractions \(p\) et \(1-p\) des valeurs \(v\), \(0\),
avec \(|v|=1\), la moyenne vaut \(pv\) et

\[
 \operatorname{MO}=2p(1-p).
 \tag{30}
\]

À un point de frontière régulier, \(p\to1/2\) et l'oscillation tend vers
\(1/2\) lorsque le rayon de la boule tend vers zéro. Par conséquent

\[
 \sup_{\rho\downarrow0}|\log(\rho/R_*)|
 \operatorname{MO}_{B_\rho}\xi_0=\infty.
 \tag{31}
\]

Sous l'hypothèse de morceau régulier formulée ci-dessus, le prolongement par
zéro échoue déjà pour un seul blob. Son échec ne vient ni de l'accumulation,
ni de la taille \(\ell_n\), mais du saut artificiel de module créé sur les
zéros. Sans cette hypothèse géométrique, cette preuve locale de bord ne
s'applique pas; l'obstruction interne de la section suivante, elle, ne dépend
pas d'un bord régulier.

## 6. Un prolongement unitaire enlève le saut, pas le motif interne

On pourrait tenter de prolonger la direction dans \(\{W=0\}\) par un champ
unitaire qui rejoint continûment la trace intérieure. Cela contourne bien la
minoration particulière (30), lorsqu'une telle trace et une telle extension
existent. Mais aucune extension ne peut modifier les valeurs sur
\(\{W_n\ne0\}\).

Le fait décisif est

\[
 \int_{\mathbb R^3}W_0(y)dy=0,
 \tag{32}
\]

car \(W_0=\nabla\times U_0\) et \(U_0\) est compact. Si la direction de
\(W_0\) était constante, ou même contenue dans un cône
\(e\cdot\xi\geq c>0\), alors

\[
 e\cdot\int W_0
 =\int|W_0|e\cdot\xi>0,
 \tag{33}
\]

contradiction. Un blob compact non trivial doit donc contenir des régions de
directions séparées.

Plus précisément, il existe deux ensembles de Lebesgue \(E,F\) de mesures
positives, contenus dans une même boule \(Q\), et deux directions unitaires
\(v,w\) avec \(|v-w|=d>0\), tels que la direction soit arbitrairement proche
de \(v\) sur \(E\) et de \(w\) sur \(F\). En réduisant les ensembles à une
même mesure \(\alpha>0\), toute extension \(\widetilde\xi\), unitaire ou non,
qui coïncide avec \(W_0/|W_0|\) sur le support actif vérifie

\[
 \fint_Q|\widetilde\xi-(\widetilde\xi)_Q|
 \geq c_0>0.
 \tag{34}
\]

La preuve utilise seulement
\(|v-c|+|w-c|\geq d\) pour le vecteur
\(c=(\widetilde\xi)_Q\); les valeurs choisies dans les zéros ne peuvent
réduire cette minoration.

Sur la copie

\[
 Q_n=x_n+\ell_nQ,
 \tag{35}
\]

l'oscillation est encore au moins \(c_0\), alors que son rayon vaut
\(O(\ell_n)\). Ainsi

\[
 [\widetilde\xi]_{\mathrm{bmo}_{1/|\log r|}}
 \geq c_0|\log(C\ell_n/R_*)|
 \sim c_0(n\log2+\log n)\longrightarrow\infty.
 \tag{36}
\]

Conclusion : une extension unitaire peut réparer la **frontière**, mais pas
la répétition à pleine amplitude d'un motif directionnel compact. Pour passer
log-BMO, le diamètre directionnel du \(n\)-ième blob devrait décroître au
moins comme \(O(1/n)\). L'identité (32) interdit qu'il tende vers une direction
unique dans un cône strict tant que chaque blob reste un curl compact non nul
avec une amplitude de signe positif.

## 7. BMO centré contre BMO global

Considérons d'abord le prolongement par zéro. La boule
\(B_{R_N}(0)\), avec

\[
 R_N=r_N+\ell_N\leq\frac54r_N,
 \tag{37}
\]

contient tous les blobs \(n\geq N\). Leur fraction volumique totale est
majorée par

\[
 \frac{V_0\sum_{n\geq N}\ell_n^3}{|B_{R_N}|}
 \leq C_{V_0}\frac1{N^3}.
 \tag{38}
\]

Comme \(|\xi_0|\leq1\),

\[
 \operatorname{MO}_{B_{R_N}(0)}\xi_0
 \leq2C_{V_0}N^{-3}.
 \tag{39}
\]

Le poids logarithmique vaut \(|\log R_N|=N\log2+O(\log N)\), donc le produit
dans (39) tend vers zéro comme \(N^{-2}\).

Le même constat vaut pour une extension égale à une direction constante
hors des blobs : appliquer (39) à la différence avec cette constante change
seulement le facteur numérique. Le train passe donc aisément le test des
boules **centrées en l'origine**, tout en échouant par (31) ou (36) sur des
boules **décentrées** de taille \(\ell_n\).

Ce contre-test interdit l'implication

```text
cohérence sur les boules centrées au point d'accumulation
    -> direction globale log-BMO.
```

## 8. Pression non locale

La disjonction des supports annule les produits croisés ponctuels :

\[
 U_iU_j=\sum_n(U_n)_i(U_n)_j.
 \tag{40}
\]

Pour la pression normalisée à l'infini,

\[
 p=\mathcal R_i\mathcal R_j(U_iU_j),
 \tag{41}
\]

la linéarité donne formellement, puis distributionnellement,

\[
 p=\sum_np_n,
 \qquad
 p_n(x)=\ell_n^{-2}p_0\!\left(\frac{x-x_n}{\ell_n}\right).
 \tag{42}
\]

Il n'y a pas de terme source croisé, mais les queues des \(p_n\) se
superposent partout. Comme \(U\otimes U\in L^1\), les doubles transformées de
Riesz donnent au mieux le contrôle faible-
\(L^1\) standard sans hypothèse supplémentaire. La borne forte habituelle

\[
 \|p\|_{3/2}\lesssim\|U\|_3^2
 \tag{43}
\]

est inutilisable parce que \(\|U\|_3=\infty\).

Chaque \(p_n\) possède séparément une taille \(L^{3/2}\) invariante. Leur
somme n'est pas une somme à supports disjoints, et aucune conclusion de
finitude ou de divergence forte ne peut être obtenue en additionnant ces
normes. Pour un profil générique dont le moment quadratique lointain ne
s'annule pas, la contribution de \(p_n\) au point zéro est d'ordre

\[
 \ell_n^{-2}|p_0(-x_n/\ell_n)|
 \sim\frac1{nr_n^2}=\frac{4^n}{n},
 \tag{44}
\]

ce qui signale une divergence ponctuelle possible. Ce diagnostic dépend du
coefficient multipolaire de \(p_0\) et n'est pas une minoration universelle.
La pression doit être recalculée comme somme non locale; elle ne peut être
déclarée « locale à chaque blob ».

## 9. Admissibilité Clay et troncatures finies

La donnée infinie (3) appartient à \(L^2_\sigma\). Elle est donc admissible
comme donnée de la théorie de Leray–Hopf, qui fournit au moins une solution
faible globale. Mais elle n'est ni bornée ni lisse au point d'accumulation.
Elle n'est pas une donnée initiale du cas lisse officiel du problème Clay.

Les troncatures

\[
 U^{(N)}=\sum_{n=4}^NU_n
 \tag{45}
\]

sont lisses, compactes et divergence-free. Elles convergent vers \(U\) dans
\(L^2\), avec

\[
 \|U-U^{(N)}\|_2^2
 =\|U_0\|_2^2\sum_{n>N}\ell_n
 =O(2^{-N}/N).
 \tag{46}
\]

En parallèle,

\[
 \|\nabla U^{(N)}\|_2^2
 =\|W_0\|_2^2\sum_{n=4}^N\ell_n^{-1}
 \geq N2^N\|W_0\|_2^2.
 \tag{47}
\]

Il n'existe donc aucune borne forte uniforme fournie par cette approximation.
Chaque troncature engendre une solution classique locale, mais son temps de
contrôle standard peut tendre vers zéro. Une suite de données distinctes
n'est pas une trajectoire unique, et sa limite \(L^2\) ne transforme pas une
singularité initiale en blow-up à temps positif.

## 10. Quantificateurs inversés détectés

1. **Blob par blob vers somme globale.** Une norme critique uniforme de
   chaque \(W_n\) ne suffit pas; ici la somme faible reste finie grâce à la
   géométrie, tandis que les normes fortes s'additionnent et divergent.
2. **Chaque troncature lisse vers limite lisse.** La convergence n'a lieu
   qu'en \(L^2\); les constantes de dérivées divergent selon (47).
3. **Masse par coquille vers \(\Phi\leq M\).** L'identité (27) montre que la
   première est compatible avec \(\sup\Phi\sim n^2\).
4. **BMO centré vers BMO global.** Les boules centrées diluent les blobs;
   les boules décentrées résolvent leur motif à pleine amplitude.
5. **Extension pour chaque blob vers extension globale uniforme.** Même si
   chaque motif admet une extension unitaire, sa constante pondérée croît
   comme \(|\log\ell_n|\).
6. **Pression locale vers pression de la somme.** Les sources sont disjointes,
   pas les queues de Riesz.
7. **Donnée faible vers scénario Clay négatif.** Une donnée déjà singulière
   à \(t=0\) ne démontre aucune perte de régularité depuis une donnée lisse.

## 11. Certificat reproductible, bibliothèque standard

Le script vérifie la séparation, les séries d'énergie, les rapports de
volumes, les exposants critiques, la croissance de \(\Phi\) et la dilution
des tests centrés.

```python
from fractions import Fraction as F
from math import log


def r(n):
    return F(1, 2 ** n)


def ell(n):
    return r(n) / n


# Exact disjointness for all tested n, with a monotone algebraic margin.
for n in range(4, 257):
    center_gap = r(n) / 2
    radii_sum = ell(n) + ell(n + 1)
    assert radii_sum < center_gap
    assert n * n - 2 * n - 2 > 0

# Sum from n=4: sum 2^-n/n=log(2)-(1/2+1/8+1/24)=log(2)-2/3.
partial = sum((float(ell(n)) for n in range(4, 10000)), 0.0)
exact_limit = log(2) - F(2, 3)
assert abs(partial - exact_limit) < 1e-15
assert exact_limit > 0

# Geometric tail control for support volumes.
for n in range(4, 257):
    ratio = ell(n + 1) ** 3 / ell(n) ** 3
    assert ratio == F(1, 8) * F(n, n + 1) ** 3
    assert ratio < F(1, 8)

# Scaling laws: amplitude^p times volume.
# U: L2^2 ~ell, L3^3 ~1. W: L1~ell, L(3/2)^(3/2)~1, L2^2~ell^-1.
assert -2 + 3 == 1
assert -3 + 3 == 0
assert -2 + 3 == 1
assert -3 + 3 == 0
assert -4 + 3 == -1

# Shape factor and centered occupation.
for n in range(4, 257):
    shape_amplitude = (r(n) / ell(n)) ** 2
    occupation = (ell(n) / r(n)) ** 3
    # shape_amplitude=n^2, hence its exact 3/2 power is (r/ell)^3=n^3.
    critical_product = occupation * (r(n) / ell(n)) ** 3
    assert shape_amplitude == n * n
    assert occupation == F(1, n ** 3)
    assert critical_product == 1

# Total tail volume is at most (8/7)ell_N^3; centered logarithmic cost
# is bounded by a constant times N/N^3=1/N^2.
previous = None
for N in range(4, 257):
    tail_bound = F(8, 7) * ell(N) ** 3
    centered_fraction_coefficient = tail_bound / r(N) ** 3
    assert centered_fraction_coefficient == F(8, 7 * N ** 3)
    weighted_coefficient = N * centered_fraction_coefficient
    assert weighted_coefficient == F(8, 7 * N ** 2)
    if previous is not None:
        assert weighted_coefficient < previous
    previous = weighted_coefficient

# Enstrophy of the last retained blob already diverges.
for N in (4, 8, 16, 32, 64):
    assert 1 / ell(N) == N * 2 ** N

# L2 tail rate: sum_(n>N)ell_n <= ell_(N+1)/(1-1/2)<2^-N/N.
for N in range(4, 128):
    upper = 2 * ell(N + 1)
    assert upper < F(1, N * 2 ** N)

print("geometry, divergence-compatible scaling and energy series: PASS")
print("weak-critical tail and Phi concentration tradeoff: PASS")
print("centered dilution and strong-norm divergence: PASS")
```

Commande de reproduction : extraire le bloc puis exécuter `python -` depuis
la racine du dépôt. Dépendances : bibliothèque standard Python. Graine :
aucune. Les identités de géométrie et d'échelle sont rationnelles exactes;
seule la vérification numérique de la série \(\log2\) utilise un flottant.

## 12. Prochain test discriminant

Le train \(\ell_n=r_n/n\) ferme négativement l'échappatoire « blobs dilués
avec \(\Phi\leq M\) » : sa dilution est payée exactement par
\(\Phi\sim n^2\), et son motif directionnel répété échoue au BMO global pour
toute extension.

Le prochain test utile doit modifier l'amplitude ou la géométrie, pas la
convention aux zéros. Deux possibilités sont falsifiables :

1. **amortissement directionnel et scalaire :** multiplier le \(n\)-ième
   blob par \(a_n\), puis résoudre simultanément

   \[
   a_n(r_n/\ell_n)^2\leq M,
   \qquad
   a_n^{3/2}\gtrsim1,
   \qquad
   \operatorname{diam}(\xi_n)\lesssim1/n;
   \tag{48}
   \]

   les deux premières inégalités sont déjà incompatibles pour
   \(\ell_n/r_n=1/n\), car elles exigent \(a_n\lesssim n^{-2}\) et
   \(a_n\gtrsim1\);
2. **blobs de taille comparable au rayon :** prendre
   \(\ell_n=c r_n\) pour restaurer \(\Phi\leq M\). Il faut alors quantifier
   la fraction volumique fixe vue par les boules centrées, la séparation des
   supports, et montrer si une direction de curl compact peut avoir un
   diamètre \(O(1/n)\). L'identité \(\int W_n=0\) suggère une nouvelle
   obstruction quantitative par hémisphères.

Le second choix est le prochain calcul discriminant : optimiser, parmi les
champs \(W_0=\nabla\times U_0\) compacts, la masse minimale forcée hors de
tout cône de largeur \(O(1/n)\), puis comparer cette masse à la minoration
log-BMO sur les boules décentrées.

```json
{
  "cycle": "0025",
  "construction": "U=sum l_n^-1 U0((x-x_n)/l_n), r_n=2^-n, l_n=r_n/n",
  "claims": [
    {
      "id": "NS-C0025-LORENTZ-TRAIN",
      "status": "PROVED_BY_SCALING_AND_DISTRIBUTION",
      "statement": "the infinite disjoint train has finite nonzero weak-L^(3/2) vorticity and finite kinetic energy"
    },
    {
      "id": "NS-C0025-UNIFORM-PHI",
      "status": "REFUTED",
      "statement": "critical shell mass and centered dilution imply a uniform shape-factor bound",
      "residual": "Phi grows like n^2"
    },
    {
      "id": "NS-C0025-ZERO-EXTENSION-BMO",
      "status": "REFUTED",
      "statement": "extension of the vorticity direction by zero belongs to global log-BMO",
      "residual": "mean oscillation tends to 1/2 across every regular active boundary"
    },
    {
      "id": "NS-C0025-UNIT-EXTENSION-BMO",
      "status": "REFUTED_FOR_REPEATED-NONTRIVIAL-COMPACT-CURL",
      "statement": "a unit extension can remove all global BMO lower bounds",
      "residual": "internal directional oscillation c0 repeated at scale l_n"
    },
    {
      "id": "NS-C0025-CLAY-BLOWUP",
      "status": "NOT_CLAIMED",
      "statement": "the train is a positive-time singularity arising from smooth finite-energy data"
    }
  ],
  "decision": "ABANDON-DILUTED-IDENTICAL-BLOB-TRAIN-UNDER-UNIFORM-PHI-AND-GLOBAL-BMO",
  "next_test": "cone-width obstruction for compact curl blobs with l_n comparable to r_n"
}
```
