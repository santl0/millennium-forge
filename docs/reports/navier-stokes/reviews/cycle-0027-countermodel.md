# Cycle 0027 — lift axisymétrique du compensateur rare

Date : 2026-08-14.

Type de passe : construction contradictoire et audit de quantificateurs. La
passe utilise le même cadre scientifique que les cycles précédents et ne
constitue pas une revue externe indépendante.

## Verdict

Le lift axisymétrique **séparable** le plus naturel échoue au test BMO. Pour

\[
 U=\psi(r,z)e_\theta,\qquad \psi(r,z)=\chi(z)A(r),
 \tag{1}
\]

on a exactement

\[
 W=\nabla\times U
 =-\chi'(z)A(r)e_r+\chi(z)f(r)e_z,
 \qquad
 f(r)=\frac1r\partial_r(rA(r)).
 \tag{2}
\]

La famille radiale à deux amplitudes peut être réalisée, avant lissage, par

\[
 h_n=n^{-3/2},\qquad
 f_n(r)=
 \begin{cases}
 -b_n,&0<r<h_n,\\
 a_n,&h_n<r<1,
 \end{cases}
 \quad
 a_n=\frac{n^2}{n^3-1},\quad b_n=n^2.
 \tag{3}
\]

Les fractions volumiques sont \(n^{-3}\) et \(1-n^{-3}\), et le flux
vertical total est nul. Pourtant :

1. dans toute tranche où \(\chi=1\) et \(\chi'=0\), l'interface \(r=h_n\)
   porte les directions antipodales \(-e_z\) et \(e_z\); une boule ou un cube
   demi-rempli a une oscillation moyenne égale à un;
2. sur un cap axial, le terme
   \(W_r=-\chi'Ae_r\) n'est pas une erreur scalaire : sa direction parcourt
   toutes les directions radiales lorsque l'angle azimutal varie;
3. pour un cap linéaire d'épaisseur \(\delta\), le contrôle
   \(L^{3/2,\infty}\) ou \(L^{3/2}\) impose
   \(\delta\gtrsim a_n^3\asymp n^{-3}\) sur un anneau radial fixe;
4. deux secteurs azimutaux opposés du cap ont alors des directions séparées
   d'une constante sur une fraction au moins \(c n^{-3}\). John--Nirenberg
   donne un coût BMO au moins \(c/\log n\), donc un coût log-BMO au moins
   \(c n/\log n\) après insertion à l'échelle
   \(\ell_n\asymp2^{-n}/n\).

Ces quatre points éliminent le produit séparable avec interface directe et
aspect ratio uniformément borné.

Ils ne prouvent pas un no-go pour **tout** potentiel axisymétrique compact.
Pour un \(\psi(r,z)\) général, le flux de retour radial peut être masqué par
une composante verticale plus grande et distribué sur des couches
emboîtées. Sous les seules hypothèses

\[
 \|W\|_{L^{3/2,\infty}}\leq K,\qquad
 \int_D|W_r|\gtrsim q_n,\qquad q_n\asymp n^{-1},
 \tag{4}
\]

un argument flux--angle universel n'extrait qu'un ensemble de mesure
\(\gtrsim q_n^3\) où l'écart azimutal est \(\gtrsim q_n\). La minoration BMO
correspondante est seulement

\[
 \|\xi\|_{\mathrm{BMO}}
 \gtrsim\frac1{n\log n}.
 \tag{5}
\]

Multipliée par \(|\log\ell_n|\asymp n\), la **minoration ainsi obtenue** tend
vers zéro comme \(1/\log n\). La méthode ne ferme donc pas le lift
axisymétrique général.
Pour obtenir \(c/\log n\), il faut une région où
\(|W_r|\gtrsim |W|\), par exemple un corridor de flux vertical nul, ou une
hypothèse quantitative équivalente.

Le résultat du cycle est donc double :

- obstruction reproductible du lift séparable et des raccords directs;
- plafond précis de l'obstruction pour un lift général, qui identifie la
  cascade de masquage comme seul échappatoire encore ouvert.

## 1. Géométrie exacte du curl axisymétrique

On travaille sur \(\mathbb R^3\) en coordonnées cylindriques
\((r,\theta,z)\). Le potentiel (1) est une vitesse azimutale. Son curl n'a
pas de composante azimutale et vérifie (2). La divergence s'annule
identiquement :

\[
\begin{aligned}
 \nabla\cdot W
 &=\frac1r\partial_r(rW_r)+\partial_zW_z\\
 &=-\frac{\chi'}r\partial_r(rA)+\chi'f=0.
\end{aligned}
\tag{6}
\]

Pour que \(U\) soit lisse sur l'axe, il faut \(A(r)=O(r)\). Pour qu'il soit
compact radialement, on impose

\[
 \int_0^\infty r f(r)\,dr=0,
 \qquad
 A(r)=\frac1r\int_0^r s f(s)\,ds.
 \tag{7}
\]

L'identité de flux (7) n'est pas l'annulation tridimensionnelle abstraite du
cycle 0026 : elle est la condition précise qui annule le potentiel
azimutal au-delà du support radial.

Une vérification BMO ne peut pas être réduite au demi-plan \((r,z)\).
L'élément de volume est \(r\,dr\,d\theta\,dz\) et

\[
 e_r(\theta+\pi)=-e_r(\theta).
 \tag{8}
\]

Une petite variation dans le dessin méridien peut donc cacher une variation
vectorielle d'ordre un entre secteurs azimutaux.

## 2. Réalisation radiale exacte des deux amplitudes

Dans un cylindre de rayon un et de hauteur fixée, la fraction du disque
\(r<h_n\) est \(h_n^2=n^{-3}\). Avec (3),

\[
 b_nh_n^2=\frac1n
 =a_n(1-h_n^2),
 \tag{9}
\]

et

\[
 \int_0^1 r f_n(r)\,dr
 =\frac12[-b_nh_n^2+a_n(1-h_n^2)]=0.
 \tag{10}
\]

Le potentiel radial associé est

\[
 A_n(r)=
 \begin{cases}
 -\dfrac{b_nr}{2},&0<r<h_n,\\[2mm]
 \dfrac{a_n(r^2-1)}{2r},&h_n<r<1,\\[2mm]
 0,&r>1.
 \end{cases}
 \tag{11}
\]

Les deux formules coïncident en \(r=h_n\), avec

\[
 A_n(h_n)=-\frac{\sqrt n}{2}.
 \tag{12}
\]

Le champ étagé (3) n'est pas lisse aux interfaces. Il sert de modèle exact
pour les constantes. Un lissage compact doit conserver (10), modifier une
mince région radiale et traiter séparément le bord \(r=1\). Aucun argument
ci-dessous ne transforme silencieusement le champ étagé en donnée de
Schwartz.

## 3. Première obstruction : l'interface radiale

Supposons que \(\chi=1\) et \(\chi'=0\) sur une tranche axiale non vide. Dans
cette tranche,

\[
 W_n=f_n(r)e_z.
 \tag{13}
\]

À l'interface \(r=h_n\), la direction normalisée prend les valeurs
\(-e_z\) et \(e_z\). Pour deux valeurs antipodales occupant des proportions
\(p\) et \(1-p\) d'une boule ou d'un cube,

\[
 \operatorname{MO}=4p(1-p).
 \tag{14}
\]

Les cellules symétriques à une interface régulière ont \(p\to1/2\), donc

\[
 \sup_Q\dashint_Q|\xi-\xi_Q|\geq1.
 \tag{15}
\]

Un lissage **scalaire** de \(f_n\) ne répare pas (15). Si \(f_n\) traverse
zéro transversalement et \(W_r=0\), la direction reste \(-e_z\) d'un côté et
\(e_z\) de l'autre. La valeur attribuée sur la surface nodale, de mesure
nulle, n'affecte pas l'oscillation.

Pour éviter (15), il faut au moins l'une des modifications suivantes :

- séparer les plateaux par une région ouverte où \(W=0\), puis choisir une
  extension unitaire;
- rendre \(W_r\) non nul pendant le changement de signe afin de faire tourner
  la direction;
- casser la tranche \(\chi'=0\) et distribuer la transition sur plusieurs
  échelles en \(r\) et \(z\).

Chacune abandonne le produit étagé direct.

## 4. Deuxième obstruction : le cap axial

### 4.1 Taille exacte du terme radial

Sur l'anneau fixe

\[
 J=\{1/4\leq r^2\leq1/2\},
 \tag{16}
\]

la seconde formule de (11) donne

\[
 |A_n(r)|
 =a_n\frac{1-r^2}{2r}
 \geq\frac{\sqrt2}{4}a_n.
 \tag{17}
\]

L'aire de \(J\) est \(\pi/4\). Considérons le cap affine

\[
 \chi(z)=1-\frac z\delta,\qquad 0<z<\delta.
 \tag{18}
\]

Sur \(J\times(0,\delta)\),

\[
 |W_r|\geq\frac{\sqrt2\,a_n}{4\delta}.
 \tag{19}
\]

Ainsi, pour la quasi-norme
\(\sup_{\lambda>0}\lambda|\{|W|>\lambda\}|^{2/3}\),

\[
 \|W\|_{L^{3/2,\infty}}
 \geq
 \frac{\sqrt2\,a_n}{4\delta}
 \left(\frac{\pi\delta}{4}\right)^{2/3}.
 \tag{20}
\]

Si le membre gauche est au plus \(K\), alors

\[
 \delta\geq
 \frac{\sqrt2\pi^2}{512}\frac{a_n^3}{K^3}.
 \tag{21}
\]

La même constante apparaît pour la masse forte sur ce niveau constant :

\[
 \int_{J\times(0,\delta)}|W_r|^{3/2}
 \geq
 \left(\frac{\sqrt2\,a_n}{4\delta}\right)^{3/2}
 \frac{\pi\delta}{4}.
 \tag{22}
\]

Une borne du membre gauche par \(M\) impose

\[
 \delta\geq
 \frac{\sqrt2\pi^2}{512}\frac{a_n^3}{M^2}.
 \tag{23}
\]

Comme \(a_n\asymp n^{-1}\), une couche axiale qui porte une chute d'ordre un
ne peut être rendue exponentiellement mince sous un contrôle critique
uniforme. Son épaisseur effective est au moins d'ordre \(n^{-3}\).

### 4.2 La phase normalisée ne voit pas la petite amplitude

Dans le même cap,

\[
 W_z=\chi a_ne_z,
 \qquad
 W_r=-\chi'A_ne_r.
 \tag{24}
\]

À deux points ayant les mêmes \(r,z\) et des angles séparés de \(\pi\), les
composantes verticales sont identiques et les composantes radiales opposées.
La distance entre directions normalisées vaut

\[
 d(r,z)=
 \frac{2|W_r|}{\sqrt{|W_r|^2+|W_z|^2}}.
 \tag{25}
\]

Pour \(0<\delta\leq1\), (17)--(19) et \(|W_z|\leq a_n\) donnent

\[
 d(r,z)\geq\frac23
 \tag{26}
\]

sur tout \(J\times(0,\delta)\). La petite taille absolue
\(a_n\asymp1/n\) disparaît après normalisation.

Le cap contient donc deux secteurs azimutaux de mesures comparables à
\(\delta\), sur lesquels les directions sont séparées par une constante. La
forme quantitative de John--Nirenberg implique que, si deux sous-ensembles
de mesure relative au moins \(\mu\) dans un cube portent des valeurs séparées
par \(d_0\), alors

\[
 \|\xi\|_{\mathrm{BMO}}
 \geq\frac{c\,d_0}{\log(C/\mu)}.
 \tag{27}
\]

Avec (21), \(d_0\geq2/3\) et \(\mu\gtrsim n^{-3}\),

\[
 \|\xi\|_{\mathrm{BMO}}\gtrsim\frac1{\log n}.
 \tag{28}
\]

Les constantes \(c,C\) de (27) dépendent de la convention boules/cubes et
des constantes de John--Nirenberg. Elles ne sont pas identifiées au calcul
algébrique de (21); aucune constante numérique certifiée n'est revendiquée
pour (28).

### 4.3 Un cutoff lisse ne supprime pas le coût principal

Un cutoff \(C^\infty_c\) est plat à l'extrémité de son support. Dans une zone
où \(\chi\) est très petite, le quotient
\(|\chi'|/\chi\) peut devenir très grand alors que \(|\chi'|\) est très
petit. La direction peut y devenir radiale sur un ensemble de très petite
capacité. Ce fait interdit d'inférer un coût d'ordre un depuis la seule
limite au bord.

Mais la chute principale de \(\chi\), par exemple de \(3/4\) à \(1/4\),
transporte une variation absolue \(1/2\). Sur un intervalle de longueur au
plus \(L_0\), la région où
\(|\chi'|\geq1/(4L_0)\) porte au moins \(1/4\) de cette variation : son
complément ne peut en porter plus que \(L_0/(4L_0)=1/4\). Le terme radial
porte donc une masse \(L^1\) d'ordre \(a_n\) sur cette région de l'anneau
\(J\), et \(|W_r|/|W|\) y est minoré par une constante dépendant seulement de
\(L_0\). L'inégalité faible-Lorentz

\[
 \int_E|W|\leq3K|E|^{1/3}
 \tag{29}
\]

force encore une mesure tridimensionnelle
\(\gtrsim(a_n/K)^3\). Le même argument (27) donne (28). La queue plate finale
ne peut effacer la chute principale.

## 5. Aspect ratio : échappatoire réelle, mais non gratuite

Si le cap s'étend sur une longueur \(L_n\gg1\), la pente principale peut être
\(O(1/L_n)\). Sur \(J\),

\[
 \frac{|W_r|}{|W_z|}
 \asymp\frac1{L_n}
 \tag{30}
\]

tant que \(\chi\) reste d'ordre un. La séparation azimutale de (25) peut
alors décroître comme \(1/L_n\). L'analogue de (28) devient au mieux

\[
 \|\xi\|_{\mathrm{BMO}}
 \gtrsim\frac1{L_n\log n}.
 \tag{31}
\]

Choisir \(L_n\gtrsim n/\log n\) neutralise la minoration log-BMO issue du
cap. Ce n'est pas une contradiction : le support de la forme de base a alors
un aspect ratio non uniforme.

Cette échappatoire ne répare pas l'interface radiale (15). Elle ne devient
pertinente qu'après remplacement simultané du changement de signe direct par
une rotation ou une cascade radiale.

L'aspect ne peut pas être supprimé par une phrase « après rescaling ». Le
rescaling isotrope de Navier--Stokes conserve l'aspect ratio. Pour insérer
une forme de longueur \(L_n\) dans le train du cycle 0025, il faut recalculer :

- le diamètre physique \(\ell_nL_n\) et la séparation des supports;
- le volume actif et la quasi-norme faible;
- la norme \(\dot H^{-1}\) de la vorticité, donc l'énergie de la vitesse;
- la masse critique par coquille;
- les queues de Biot--Savart et de pression.

Un rescaling anisotrope qui comprime seulement \(z\) ne préserve ni le
Laplacien isotrope, ni la loi d'échelle Clay. Il ne peut pas être utilisé
comme raccord silencieux.

## 6. Interfaces et zéros : audit complet

### Interface radiale interne

Un changement scalaire direct de signe donne (15). Une rotation active évite
le saut seulement si une composante transverse reste quantitativement
présente pendant tout le changement.

### Interface radiale externe

La condition \(A(1)=0\) issue du flux ne suffit pas à rendre \(U\) lisse. Le
profil étagé a encore un saut de dérivée à \(r=1\). Un cutoff radial ajoute
une couche où \(f=(rA)'/r\) change et peut créer une nouvelle transition
directionnelle. Ses constantes doivent être suivies indépendamment de celles
du cap axial.

### Interface axiale plateau--cap

Un cap affine raccordé brutalement fait passer \(\chi'\) de zéro à
\(-1/\delta\) et crée directement une transition verticale--radiale. Un
raccord lisse peut l'étaler, mais (29) empêche de concentrer une chute
d'ordre un sur une capacité arbitrairement petite sous borne critique.

### Extrémité axiale du support

On a \(W=0\) lorsque \(\chi=\chi'=0\). La direction n'y est pas définie. Le
prolongement par zéro n'est pas unitaire; un prolongement unitaire doit être
le **même champ global** pour toutes les boules et tous les blobs.

### Axe \(r=0\)

Le vecteur \(e_r\) est indéfini sur l'axe, mais \(A(r)=O(r)\) entraîne
\(W_r=O(r)\). Le champ vectoriel peut être lisse alors que son écriture
cylindrique est singulière. En revanche, près d'un zéro simultané de
\(W_r,W_z\), la direction normalisée peut ne pas avoir de limite. La
régularité de \(W\) ne fournit pas automatiquement une extension BMO de
\(W/|W|\).

### Boules tridimensionnelles

Tester uniquement des rectangles méridiens manque (8). Tester uniquement des
bols centrés sur l'axe manque les interfaces locales. Le semi-norme global
doit prendre le supremum sur toutes les boules ou tous les cubes euclidiens,
y compris ceux centrés dans un cap et décentrés de l'axe.

## 7. Plafond de l'obstruction pour un potentiel général

La partie précédente exploite une région où la composante radiale représente
une fraction fixe du champ. Sans cette hypothèse, le flux seul est trop
faible.

Soit \(D\) un domaine de volume \(V\), et supposons

\[
 \|W\|_{L^{3/2,\infty}(D)}\leq K,\qquad
 \int_D|W_r|\geq q.
 \tag{32}
\]

Par (29),

\[
 \int_D|W|\leq3KV^{1/3}.
 \tag{33}
\]

Posons

\[
 \alpha=\frac{q}{6KV^{1/3}},
 \qquad
 E_\alpha=\{|W_r|\geq\alpha|W|\}.
 \tag{34}
\]

Sur le complément,

\[
 \int_{D\setminus E_\alpha}|W_r|
 \leq\alpha\int_D|W|\leq\frac q2.
 \tag{35}
\]

Donc \(\int_{E_\alpha}|W_r|\geq q/2\), et (29) donne

\[
 |E_\alpha|
 \geq\left(\frac q{6K}\right)^3.
 \tag{36}
\]

Par axisymétrie, deux secteurs opposés de \(E_\alpha\) voient leurs
composantes radiales changer de signe. Il faut encore séparer le signe de
\(W_r\) et partitionner la composante verticale normalisée en
\(O(1/\alpha)\) intervalles. Un des sous-ensembles ainsi obtenus a une mesure
\(\gtrsim\alpha|E_\alpha|\), et ses deux secteurs opposés portent des
directions séparées par \(c\alpha\). L'argument de capacité (27) ne fournit
donc que

\[
 \|\xi\|_{\mathrm{BMO}}
 \gtrsim
 \frac{q/(KV^{1/3})}
      {\log(CK^4V^{4/3}/q^4)}.
 \tag{37}
\]

Pour \(K,V\asymp1\) et \(q\asymp1/n\), on obtient (5), pas (28). Après le
poids \(|\log\ell_n|\asymp n\), la minoration obtenue n'est encore que
\(\gtrsim1/\log n\) et tend vers zéro; elle ne contredit donc aucune borne
uniforme.

Cette perte d'un facteur \(n\) est irréductible dans l'argument : un champ
peut transporter le flux radial avec un angle \(O(1/n)\) sur un volume
d'ordre un. Pour exclure ce scénario, il faudrait démontrer que la structure
à deux amplitudes force une zone où \(|W_r|/|W|\geq c>0\). C'est précisément
ce que garantit un corridor \(W_z=0\), et ce qu'un masquage vertical emboîté
cherche à éviter.

Ainsi, une affirmation universelle

\[
 \text{axisymétrie + compacité + flux }1/n
 \Longrightarrow \mathrm{BMO}\gtrsim1/\log n
 \tag{38}
\]

n'est pas démontrée et ne suit pas des normes critiques seules.

## 8. Contre-profils et limites de portée

### Contre-profil fonctionnel à l'ordre un

Le champ unitaire axisymétrique

\[
 \eta_\varepsilon(r,\theta)
 =\frac{e_z+\varepsilon g(r)e_r(\theta)}
 {\sqrt{1+\varepsilon^2g(r)^2}},
 \tag{39}
\]

avec \(g=0\) près de l'axe et \(0\leq g\leq1\), a une variation azimutale
\(O(\varepsilon)\), pas d'ordre un. Il réfute toute obstruction purement
topologique fondée sur le tour complet de \(e_r\). Il ne prouve pas
l'existence d'une magnitude compacte \(m\) telle que
\(W=m\eta_\varepsilon\) soit divergence-free.

### Contre-profil de capacité

Deux directions séparées sur des ensembles de mesure relative \(\mu\)
n'imposent qu'un coût \(O(1/\log(1/\mu))\) dans le problème d'extension BMO.
Une cascade de corridors de zéros peut atteindre cette échelle
logarithmique. Elle n'est pas encore un curl compact et ne doit pas être
présentée comme tel.

### Ce qui reste irréalisé

Aucun \(\psi_n\in C_c^\infty\) explicite n'est construit ici avec,
simultanément :

- les deux amplitudes et fractions du cycle 0026;
- faible-\(L^{3/2}\) uniforme;
- masse forte critique non dégénérée;
- extension directionnelle log-BMO uniforme sur toutes les boules;
- énergie de Biot--Savart uniforme;
- résidu Navier--Stokes contrôlé.

Le lift séparable est réfuté; le lift axisymétrique général reste ouvert.

## 9. Certificat reproductible en bibliothèque standard

Le script vérifie les flux exacts du profil radial, la continuité du
streamfunction à l'interface en variable \(s=r^2\), les constantes des bornes
de cap, la séparation azimutale minimale et les deux échelles distinctes de
l'argument générique.

```python
from fractions import Fraction as F
from math import log, pi, sqrt


cap_constant = sqrt(2.0) * pi**2 / 512.0

for n in list(range(2, 65)) + [128, 256, 1024]:
    eps = F(1, n**3)
    a = F(n**2, n**3 - 1)
    b = F(n**2, 1)

    # Radial volume fractions and zero vertical flux.
    assert b * eps == F(1, n)
    assert a * (1 - eps) == F(1, n)
    assert (-b * eps + a * (1 - eps)) / 2 == 0

    # Streamfunction numerator F(r)=int_0^r s f(s) ds.
    # At s=r^2=eps, both pieces equal -1/(2n).
    interface_core = -b * eps / 2
    interface_outer = a * (eps - 1) / 2
    assert interface_core == interface_outer == -F(1, 2 * n)

    # On the outer phase, F(s)=a(s-1)/2 and F(1)=0.
    for s in [F(1, 4), F(1, 3), F(1, 2), F(3, 4), F(1, 1)]:
        outer_direct = (-b * eps + a * (s - eps)) / 2
        outer_closed = a * (s - 1) / 2
        assert outer_direct == outer_closed
    assert a * (F(1, 1) - 1) / 2 == 0

    # The cap lower bounds equal one when delta takes the threshold value
    # cap_constant*a^3 and K=M=1.
    delta_min = cap_constant * float(a) ** 3
    amplitude_floor = float(a) * sqrt(2.0) / (4.0 * delta_min)
    cap_volume = pi * delta_min / 4.0
    weak_lower = amplitude_floor * cap_volume ** (2.0 / 3.0)
    strong_lower = amplitude_floor ** 1.5 * cap_volume
    assert abs(weak_lower - 1.0) < 3e-13
    assert abs(strong_lower - 1.0) < 3e-13

    # n^3 delta_min stays between fixed constants.
    scaled_delta = n**3 * delta_min
    assert cap_constant < scaled_delta
    assert scaled_delta <= cap_constant * (F(8, 7) ** 3)

# If delta<=1, the opposite-azimuth direction gap is at least 2/3.
c0 = sqrt(2.0) / 4.0
minimum_gap = 2.0 * c0 / sqrt(1.0 + c0**2)
assert abs(minimum_gap - F(2, 3)) < 2e-15

# Generic flux-angle extraction versus a true radial-dominance region.
generic_weighted = []
dominant_weighted = []
for k in range(3, 15):
    n = 2**k
    q = 1.0 / n
    alpha = q / 6.0
    extracted_measure = (q / 6.0) ** 3
    assert abs(extracted_measure - alpha**3) < 1e-30

    generic_direction_gap = 2.0 * alpha
    # One additional alpha factor records sign/vertical-direction binning.
    clustered_measure = alpha * extracted_measure
    capacity_log = log(1.0 / clustered_measure)
    generic_bmo_scale = generic_direction_gap / capacity_log
    dominant_bmo_scale = 1.0 / capacity_log

    physical_log_weight = n * log(2.0) + log(n)
    generic_weighted.append(physical_log_weight * generic_bmo_scale)
    dominant_weighted.append(physical_log_weight * dominant_bmo_scale)

assert generic_weighted[-1] < generic_weighted[0]
assert dominant_weighted[-1] > dominant_weighted[0]
assert dominant_weighted[-1] > 100.0 * generic_weighted[-1]

print("axisymmetric radial flux and streamfunction identities: PASS")
print("critical cap thickness and azimuthal gap: PASS")
print("generic flux-angle ceiling versus radial dominance: PASS")
```

Commande de reproduction : extraire le bloc Python puis exécuter python -
depuis la racine du dépôt. Dépendances : bibliothèque standard Python.
Graine : aucune. Les identités de flux sont rationnelles exactes. Les
flottants servent uniquement aux constantes contenant \(\pi\), aux puissances
fractionnaires et aux logarithmes. Le script ne certifie pas les constantes
de John--Nirenberg ni un supremum BMO continu.

## 10. Prochain test discriminant

Le prochain test doit viser la seule échappatoire restante : un
streamfunction non séparable qui masque chaque retour radial par une couche
verticale suivante.

**Ansatz à tester.** Construire une somme finie

\[
 \psi_n(r,z)=\sum_{j=0}^{N_n}A_{n,j}(r)\chi_{n,j}(z),
 \tag{40}
\]

où la couche \(j+1\) maintient \(|W_z|\) pendant que
\(-\partial_z\psi_{n,j}\) ferme la couche \(j\). Imposer analytiquement :

\[
 \psi_n=O(r)\text{ sur l'axe},\qquad
 \psi_n=0\text{ près du bord},\qquad
 W_n=\nabla\times(\psi_ne_\theta).
 \tag{41}
\]

**Test de décision.** Pour chaque niveau, calculer :

1. le flux vertical enfermé \(2\pi r\psi_n(r,z)\);
2. la masse faible-\(L^{3/2}\) de \(W_r\) et \(W_z\);
3. la fraction angulaire \(|W_r|/|W|\);
4. la capacité des ensembles où cette fraction dépasse \(1/4\);
5. le BMO sur des paires de secteurs azimutaux opposés;
6. l'aspect ratio total et les normes après rescaling isotrope;
7. le résidu de divergence, qui doit être exactement nul avant discrétisation.

Abandonner l'ansatz si un niveau conserve
\[
 |\{ |W_r|\geq|W|/4\}|\geq n^{-C}
 \]
avec \(C\) fixe : (27) produit alors un coût \(c/\log n\), incompatible avec
le poids physique. Le poursuivre seulement si la capacité radiale décroît
plus vite que toute puissance **et** si les normes critiques, l'énergie et
l'aspect ratio restent uniformes. Ce double test empêche de gagner le BMO en
cachant une perte dans une couche exponentiellement mince ou un support
exponentiellement long.

```json
{
  "cycle": "0027",
  "claim": "AXISYMMETRIC_TWO_AMPLITUDE_COMPACT_LIFT",
  "status": "SEPARABLE_LIFT_REFUTED_GENERAL_LIFT_OPEN",
  "proved": [
    "exact radial two-amplitude zero-flux streamfunction",
    "order-one BMO at a direct radial sign interface",
    "critical cap thickness of order at least n^-3 for an affine cap",
    "fixed-aspect cap BMO obstruction of order one over log n",
    "generic flux-angle method yields only one over n log n"
  ],
  "quantifier_limits": [
    "John-Nirenberg constants are not numerically certified",
    "general nonseparable streamfunctions may mask radial flux",
    "unbounded aspect ratio requires a full rescaling audit",
    "direction on vorticity zeros requires one global unit extension"
  ],
  "next_test": "finite nested nonseparable return-flow streamfunction"
}
```
