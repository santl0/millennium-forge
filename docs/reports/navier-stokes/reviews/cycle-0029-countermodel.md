# Cycle 0029 — tores signés à impulsion corrigée

Date : 2026-08-14.

Type de passe : contre-modèle reproductible et obstruction quantitative.
Cette passe est une dérivation IA interne et non une revue externe
indépendante.

## Verdict

Une paire de tores azimutaux minces de signes opposés peut satisfaire
simultanément :

\[
 \nabla\cdot W_n=0,\qquad
 \int W_n=0,\qquad
 I(W_n):=\frac12\int x\times W_n\,dx=0,
 \tag{1}
\]

\[
 \|W_n\|_{L^{3/2,\infty}}=1,\qquad
 \int|W_n|^{3/2}=1
 \tag{2}
\]

dans le modèle étagé, avec des corridors directionnels disjoints et un
semi-norme \(\mathrm{bmo}_{1/|\log r|}\) uniforme après insertion à une
échelle physique \(\ell_n\to0\).

La correction du premier multipôle ne coûte donc ni une interface
directionnelle d'ordre un, ni une perte de la norme critique de vorticité.
Une famille à trois tores de coefficients \(1,-2,1\) annule en plus le
premier moment axial de l'impulsion. Une famille finie permet ainsi
d'annuler un nombre fini de moments sans rouvrir automatiquement le verrou
BMO.

En revanche, aucun contre-profil avec

\[
 \liminf_{n\to\infty}\|u_n\|_3>0
 \tag{3}
\]

n'apparaît pour un nombre **fixé** de tores. Si le \(j\)-ième tore a un
rapport d'aspect

\[
 \eta_{n,j}=h_{n,j}/R_{n,j}
 \tag{4}
\]

et une quasi-norme faible critique \(k_{n,j}\), alors sa vitesse de
Biot--Savart vérifie

\[
 \|u_{n,j}\|_3
 \leq C k_{n,j}\eta_{n,j}^{1/9}.
 \tag{5}
\]

La quasi-norme globale borne chaque \(k_{n,j}\). Pour garder le test
logarithmique uniforme à l'échelle \(\ell_n\), un corridor reliant
\(\pm e_\theta\) à une direction constante doit avoir une profondeur

\[
 L_{n,j}=\log(q_{n,j}/h_{n,j})
 \gtrsim|\log\ell_n|,
 \tag{6}
\]

donc \(\eta_{n,j}\lesssim e^{-c|\log\ell_n|}\). Pour \(m\) tores, avec \(m\)
fixé,

\[
 \left\|\sum_{j=1}^m u_{n,j}\right\|_3
 \leq CKm\max_j\eta_{n,j}^{1/9}
 \longrightarrow0.
 \tag{7}
\]

L'impulsion n'était donc pas la cause de la petitesse critique du cycle
0028. Elle provenait de la codimension deux et de l'épaisseur exponentielle
requise par le corridor BMO. La paire corrigée reste en outre
axisymétrique sans swirl, donc dans une classe globalement régulière.

Le résultat scientifique du cycle est négatif mais net :

- la correction d'un nombre fini de multipôles est compatible avec toutes
  les portes cinématiques testées;
- une famille d'un nombre fixé de tores ne peut pas conserver une vitesse
  \(L^3\) non petite dans ce régime;
- toute réouverture exige un nombre de composantes croissant, une cohérence
  non locale de leurs vitesses, ou une géométrie autre que des tubes
  azimutaux disjoints.

## 1. Paire exacte de tores signés

### 1.1 Géométrie

Fixons un rayon majeur \(R>0\), une séparation axiale \(d>0\), et
\(0<h<q<\min(R/8,d/4)\). Soient

\[
 \Gamma_\pm
 =\{(R\cos\theta,R\sin\theta,\pm d/2):
       0\leq\theta<2\pi\},
 \tag{8}
\]

et

\[
 s_\pm(r,z)
 =\sqrt{(r-R)^2+(z\mp d/2)^2}.
 \tag{9}
\]

Pour un profil radial
\(y\mapsto\varphi(|y|)\in C_c^\infty(\mathbb R^2)\), positif dans le disque
unité, posons

\[
 W_h(x)=B_h
 \left[
 \varphi(s_+(x)/h)-\varphi(s_-(x)/h)
 \right]e_\theta.
 \tag{10}
\]

Les deux supports sont disjoints. Chaque terme est tangent aux tores
\(s_\pm=\text{constante}\) et indépendant de \(\theta\). Ainsi

\[
 \nabla\cdot W_h
 =\frac1r\partial_\theta(W_h^\theta)=0.
 \tag{11}
\]

L'intégrale en \(\theta\) donne séparément

\[
 \int W_h^+\,dx=0,\qquad
 \int W_h^-\,dx=0.
 \tag{12}
\]

La moyenne vectorielle ne dépend donc pas de la correction de signe.

### 1.2 Impulsion

Pour un tore positif centré à une hauteur arbitraire \(z_0\),

\[
 I_z^+
 =\frac12\int r|W_h^+|\,dx>0.
 \tag{13}
\]

Une translation selon \(z\) ne change pas cette composante. Le tore négatif
de même \(R,h,B_h\) a exactement l'impulsion opposée. Donc

\[
 I(W_h^+)+I(W_h^-)=0.
 \tag{14}
\]

Pour le profil étagé, le module de l'impulsion individuelle est

\[
 I_{\rm ring}
 =B_h\left(
 \pi^2R^2h^2+\frac{\pi^2}{4}h^4
 \right).
 \tag{15}
\]

La composante horizontale de chaque impulsion est nulle par symétrie
azimutale.

L'annulation de (14) supprime le multipôle associé à l'impulsion dans le
développement lointain de Biot--Savart. Comme les deux tores sont translatés
et de signes opposés, le moment axial suivant vaut exactement

\[
 \left(\frac d2\right)I_{\rm ring}
 +\left(-\frac d2\right)(-I_{\rm ring})
 =dI_{\rm ring}\ne0.
\]

La queue n'est donc pas de Schwartz.

## 2. Normalisation faible-\(L^{3/2}\)

### 2.1 Paire étagée

Le volume d'un tore de section disque est

\[
 V=2\pi^2Rh^2.
 \tag{16}
\]

Pour deux supports disjoints de même amplitude \(B_h\), la fonction de
distribution du module est celle d'un ensemble de volume \(2V\). Le choix

\[
 B_h=(2V)^{-2/3}
 \tag{17}
\]

donne exactement

\[
 \|W_h\|_{L^{3/2,\infty}}
 =B_h(2V)^{2/3}=1
 \tag{18}
\]

et

\[
 \int|W_h|^{3/2}
 =B_h^{3/2}(2V)=1.
 \tag{19}
\]

De plus,

\[
 \|W_h\|_1=(2V)^{1/3},
 \qquad
 \|W_h\|_2^2=(2V)^{-1/3}.
 \tag{20}
\]

Un bump radial fixe remplace le profil étagé en multipliant ces identités
par des constantes indépendantes de \(h\).

### 2.2 Restriction à chaque composante

Notons

\[
 k_j=\|W_j\|_{L^{3/2,\infty}}.
 \tag{21}
\]

Pour des supports disjoints,

\[
 k_j\leq
 \left\|\sum_iW_i\right\|_{L^{3/2,\infty}},
 \tag{22}
\]

car chaque ensemble de niveau individuel est inclus dans l'ensemble de
niveau global. Cette monotonie suffit à l'obstruction (7); aucune inégalité
triangulaire de quasi-norme avec constante non suivie n'est utilisée.

## 3. Corridors directionnels disjoints

### 3.1 Extension globale

Soit

\[
 L=\log(q/h),
 \tag{23}
\]

et

\[
 \alpha(s)=
 \begin{cases}
 \pi/2,&s\leq h,\\
 \dfrac\pi2\dfrac{\log(q/s)}L,&h<s<q,\\
 0,&s\geq q.
 \end{cases}
 \tag{24}
\]

Puisque les tubes \(s_\pm<q\) sont disjoints, on définit sans conflit

\[
 \widetilde\xi_h(x)=
 \begin{cases}
 \sin\alpha(s_+)e_\theta+\cos\alpha(s_+)e_z,
   &s_+<q,\\
 -\sin\alpha(s_-)e_\theta+\cos\alpha(s_-)e_z,
   &s_-<q,\\
 e_z,&\text{ailleurs}.
 \end{cases}
 \tag{25}
\]

Ce champ est unitaire, vaut \(W_h/|W_h|\) sur l'ensemble actif et reste
constant près de l'axe cylindrique. Les coins de \(\alpha\) peuvent être
lissés à rapports fixés.

Un prolongement par zéro créerait au contraire un saut de module et un
semi-norme logarithmique infini à chaque bord régulier.

### 3.2 Boules rencontrant un seul corridor

Le calcul du cycle 0028 s'applique sans changement de constante d'échelle :

\[
 \operatorname{MO}_B\widetilde\xi_h
 \leq C\left(\frac1L+\frac qR\right)
 \tag{26}
\]

pour toute boule ne rencontrant qu'un tube. Une suite de boules de rayon
\(\rho\simeq ch\), avec \(c>1\) fixé, donne aussi

\[
 \operatorname{MO}_B\widetilde\xi_h
 \geq \frac cL
 \tag{27}
\]

à constantes géométriques près. C'est l'échelle qui impose (6).

### 3.3 Boules rencontrant les deux corridors

Une boule qui rencontre les deux tubes a un rayon au moins comparable à
\(d\). Dans une section normale,

\[
 \int_{s<q}|\widetilde\xi_h-e_z|\,dA
 \leq Cq^2/L.
 \tag{28}
\]

Les deux portions toriques contenues dans une boule de rayon
\(\rho\gtrsim d\) ont une longueur totale au plus \(CR\). Par conséquent

\[
 \operatorname{MO}_B\widetilde\xi_h
 \leq C\frac{Rq^2}{L\rho^3}
 \leq C\frac{Rq^2}{Ld^3}.
 \tag{29}
\]

Pour \(d\asymp R\) et \(q=R/L\), le coût est

\[
 O(L^{-3}).
 \tag{30}
\]

Le signe opposé des deux cœurs ne crée pas une oscillation d'ordre un :
les cœurs et leurs corridors occupent une capacité trop petite dans toute
boule capable de voir simultanément les deux.

### 3.4 Coût pondéré après insertion physique

Soit

\[
 S_n=|\log(\ell_nR)|.
 \tag{31}
\]

La boule locale critique donne

\[
 |\log(\ell_nh_n)|
 \operatorname{MO}_{B_{c\ell_nh_n}}\widetilde\xi_{h_n}
 \asymp
 \frac{S_n+\log(R/h_n)}{L_n}.
 \tag{32}
\]

Si \(q_n=R/L_n\), alors

\[
 \log(R/h_n)=L_n+\log L_n.
 \tag{33}
\]

Une borne uniforme de (32) exige

\[
 L_n\gtrsim S_n.
 \tag{34}
\]

Le choix

\[
 L_n=n^2,\qquad q_n=R/L_n,\qquad
 h_n=q_ne^{-L_n},\qquad
 \ell_n=2^{-n}/n
 \tag{35}
\]

donne une contribution locale d'ordre un et une contribution des boules
contenant la paire d'ordre

\[
 S_nL_n^{-3}=O(n^{-5}).
 \tag{36}
\]

## 4. Obstruction à une vitesse critique non petite

### 4.1 Une composante

Soit un tore de rapport \(\eta=h/R\) et de quasi-norme faible critique
\(k\). Son amplitude est

\[
 B\asymp k(Rh^2)^{-2/3}.
 \tag{37}
\]

Hardy--Littlewood--Sobolev et l'estimation directe du noyau donnent

\[
 \|u\|_2\leq Ck(Rh^2)^{1/6},
 \qquad
 \|u\|_\infty\leq Ck(Rh^2)^{-2/3}h.
 \tag{38}
\]

En interpolant,

\[
 \|u\|_3
 \leq
 \|u\|_2^{2/3}\|u\|_\infty^{1/3}
 \leq Ck(h/R)^{1/9}.
 \tag{39}
\]

Cette borne ne dépend pas du rayon majeur séparément. Augmenter ou diminuer
isotropiquement le tore ne répare pas la perte.

### 4.2 Famille d'un nombre fixé de tores

Supposons \(m\) fixé,

\[
 \left\|\sum_{j=1}^mW_{n,j}\right\|_{L^{3/2,\infty}}\leq K,
 \tag{40}
\]

et des corridors logarithmiques satisfaisant une borne uniforme de (32).
On suppose également que chaque rayon physique
\(\ell_nR_{n,j}\to0\), comme requis pour une famille de blobs se concentrant.
Par (22), \(k_{n,j}\leq K\). Par (34), puis
\(h_{n,j}<q_{n,j}\lesssim R_{n,j}\),

\[
 \eta_{n,j}
 \lesssim e^{-cS_n}.
 \tag{41}
\]

Les inégalités de Minkowski et (39) donnent

\[
\begin{aligned}
 \left\|\sum_{j=1}^mu_{n,j}\right\|_3
 &\leq\sum_{j=1}^m\|u_{n,j}\|_3\\
 &\leq CKm e^{-cS_n/9}
 \longrightarrow0.
\end{aligned}
\tag{42}
\]

Les signes, les annulations d'impulsion et le chevauchement des queues ne
peuvent invalider une borne supérieure par triangle. Ils peuvent seulement
rendre la somme plus petite.

Cette obstruction vaut pour tout nombre fixé de moments corrigés par un
nombre fixé de tores comparables.

## 5. Trois tores et correction d'un moment supplémentaire

Plaçons trois tores identiques aux hauteurs \(-d,0,d\), avec coefficients

\[
 c_- =1,\qquad c_0=-2,\qquad c_+=1.
 \tag{43}
\]

Alors

\[
 \sum_jc_j=0,\qquad
 \sum_jc_jz_j=0,\qquad
 \sum_jc_jz_j^2=2d^2\ne0.
 \tag{44}
\]

La première identité annule l'impulsion totale. La seconde annule le premier
moment axial de cette impulsion. La troisième montre que la correction ne se
poursuit pas automatiquement.

Pour des supports de volume \(V\), les amplitudes du module sont
\(B,2B,B\). La quasi-norme faible du champ étagé vaut

\[
 \max\{B(3V)^{2/3},\,2BV^{2/3}\}
 =B(3V)^{2/3},
 \tag{45}
\]

car \(3^{2/3}>2\). Avec \(B=(3V)^{-2/3}\), elle vaut un, tandis que

\[
 \int|W|^{3/2}
 =\frac{2+2\sqrt2}{3}.
 \tag{46}
\]

Les trois corridors peuvent être disjoints si \(d>2q\). Les estimations BMO
et \(L^3\) restent celles d'une famille de cardinal trois; (42) s'applique.

Cette construction montre qu'annuler un multipôle supplémentaire ne change
pas l'obstruction critique.

## 6. Pression, dynamique et portée Clay

La vitesse corrigée est encore axisymétrique sans swirl. La classe est
globalement régulière pour des données lisses d'énergie finie. De plus,
(42) place la famille dans le régime petites données \(L^3\).

La pression normalisée par décroissance à l'infini vérifie

\[
 \|p_n\|_{3/2}
 \leq C\|u_n\|_3^2\longrightarrow0.
 \tag{47}
\]

L'annulation d'impulsion améliore la décroissance lointaine d'un ordre
générique, mais un nombre fini de conditions de moments ne produit pas
automatiquement une vitesse compacte ou de Schwartz. La paire et le triplet
ne sont donc pas, tels quels, des données de Schwartz du cas Clay sur
\(\mathbb R^3\).

Ils peuvent être inversés sur un grand domaine périodique puisque la
vorticité est lisse, périodique, divergence-free et de moyenne nulle. Mais
la périodisation, la norme \(L^3\) de l'inverse curl et la perte de
l'axisymétrie euclidienne doivent être recalculées; aucune conclusion
dynamique périodique n'est importée automatiquement.

Aucun profil non nul de vitesse d'énergie finie n'est stationnaire pour
Navier--Stokes non forcé avec \(\nu>0\) : le test de l'équation stationnaire
par \(u\) donne

\[
 \nu\int|\nabla u|^2=0.
 \tag{48}
\]

La correction des moments ne change ni cette obstruction, ni la diffusion
immédiate des tubes à temps positif.

## 7. Pièges de quantificateurs

1. **Impulsion versus décroissance rapide.** \(I=0\) annule un multipôle,
   pas toute la queue de Biot--Savart.
2. **Moyenne versus impulsion.** Chaque tore a déjà \(\int W=0\);
   le signe opposé sert à annuler \(I\), quantité différente.
3. **Faible-Lorentz global.** Pour plusieurs niveaux d'amplitude, il faut
   tester tous les seuils; la somme des quasi-normes n'est pas une identité.
4. **BMO all-ball.** Les boules locales de rayon \(O(h)\) fixent le coût
   pondéré. Les boules contenant plusieurs tores sont diluées.
5. **Zéros.** Les corridors sont une seule extension unitaire globale. Le
   prolongement par zéro échoue.
6. **Cardinal fixé.** La preuve (42) n'est pas uniforme lorsque le nombre
   \(m=m_n\) croît.
7. **Cohérence des vitesses.** Une borne supérieure par triangle ferme le
   cas \(m\) fixé, mais ne décrit pas une éventuelle addition cohérente de
   \(m_n\to\infty\) queues non locales.
8. **Domaine.** Le raccord périodique n'est pas le raccord de Schwartz sur
   \(\mathbb R^3\).
9. **Dynamique.** Une famille de données distinctes n'est pas une cascade
   temporelle d'une solution unique.

## 8. Certificat standard-library

Le script vérifie en logarithmes :

- la normalisation exacte de la paire;
- l'annulation de l'impulsion et les moments du triplet;
- les seuils exacts de faible-Lorentz pour \(1,-2,1\);
- l'échelle \(L^3\) de la paire;
- la localisation numérique du maximum pondéré près de \(h\);
- la dilution d'une boule contenant les deux corridors.

La quadrature BMO utilise le modèle local de tube droit du cycle 0028. Elle
n'est pas un calcul par intervalles et ne certifie pas le supremum continu.

```python
from math import cos, exp, log, pi, sin, sqrt


def angle(log_s, log_h, log_q, depth):
    if log_s <= log_h:
        return pi / 2.0
    if log_s >= log_q:
        return 0.0
    return (pi / 2.0) * (log_q - log_s) / depth


def local_ball_mo(log_rho, log_h, log_q, depth, sign, points=2000):
    samples = []
    total = mean_tangent = mean_vertical = 0.0
    for index in range(points):
        t = (index + 0.5) / points
        weight = t * sqrt(1.0 - t * t)
        alpha = angle(log_rho + log(t), log_h, log_q, depth)
        tangent = sign * sin(alpha)
        vertical = cos(alpha)
        samples.append((weight, tangent, vertical))
        total += weight
        mean_tangent += weight * tangent
        mean_vertical += weight * vertical
    mean_tangent /= total
    mean_vertical /= total
    return sum(
        weight
        * sqrt(
            (tangent - mean_tangent) ** 2
            + (vertical - mean_vertical) ** 2
        )
        for weight, tangent, vertical in samples
    ) / total


for n in [4, 8, 12, 16]:
    radius = 1.0
    depth = float(n * n)
    log_q = -log(depth)
    log_h = log_q - depth
    log_single_volume = log(2.0 * pi * pi * radius) + 2.0 * log_h
    log_pair_volume = log(2.0) + log_single_volume
    log_amplitude = -(2.0 / 3.0) * log_pair_volume

    # Pair: global weak norm and strong critical mass are one.
    assert abs(log_amplitude + (2.0 / 3.0) * log_pair_volume) < 1e-13
    assert abs(1.5 * log_amplitude + log_pair_volume) < 1e-13

    # Equal and opposite top-hat impulses cancel exactly.
    if n <= 8:
        h = exp(log_h)
        amplitude = exp(log_amplitude)
        impulse = amplitude * (
            pi**2 * radius**2 * h**2 + (pi**2 / 4.0) * h**4
        )
        assert impulse > 0.0
        assert impulse + (-impulse) == 0.0

    # Pair L3 upper scale: 2 times the single-ring interpolation bound.
    log_single_u3_bound = (
        log_amplitude
        + (5.0 / 9.0) * log_single_volume
        + (1.0 / 3.0) * log_h
    )
    log_pair_u3_bound = log(2.0) + log_single_u3_bound
    expected = (
        (1.0 / 3.0) * log(2.0)
        - (1.0 / 9.0) * log(2.0 * pi * pi)
        + (1.0 / 9.0) * log_h
    )
    assert abs(log_pair_u3_bound - expected) < 1e-12

    # Weighted all-ball proxy: local core versus a ball seeing both tori.
    log_ell = -n * log(2.0) - log(float(n))
    offsets = [-2.0 + 0.1 * j for j in range(101)]
    offsets += [
        8.0 + (depth - 6.0) * j / 80.0
        for j in range(81)
    ]
    local_best = (-1.0, None, None)
    for offset in offsets:
        log_rho = log_h + offset
        positive_mo = local_ball_mo(
            log_rho, log_h, log_q, depth, sign=1.0
        )
        negative_mo = local_ball_mo(
            log_rho, log_h, log_q, depth, sign=-1.0
        )
        assert abs(positive_mo - negative_mo) < 2e-14
        weighted = abs(log_ell + log_rho) * positive_mo
        if weighted > local_best[0]:
            local_best = (weighted, offset, positive_mo)

    pair_ball_proxy = 2.0 * depth ** (-3)
    pair_ball_weighted = abs(log_ell) * pair_ball_proxy
    assert 0.0 < local_best[1] < 6.0
    assert 0.4 < local_best[0] < 1.2
    assert pair_ball_weighted < local_best[0] / 100.0

    print(
        f"n={n:2d} local_weighted={local_best[0]:.6f} "
        f"log(rho/h)={local_best[1]:.2f} "
        f"pair_ball_weighted={pair_ball_weighted:.3e}"
    )

# Three-ring coefficients cancel impulse and its first axial moment.
coefficients = [1, -2, 1]
heights = [-1, 0, 1]
assert sum(coefficients) == 0
assert sum(c * z for c, z in zip(coefficients, heights)) == 0
assert sum(c * z * z for c, z in zip(coefficients, heights)) == 2

# With single-ring volume one, test every amplitude threshold.
weak_low_threshold = 3.0 ** (2.0 / 3.0)
weak_high_threshold = 2.0
assert weak_low_threshold > weak_high_threshold
base_amplitude = weak_low_threshold ** (-1)
assert abs(base_amplitude * weak_low_threshold - 1.0) < 1e-15
assert base_amplitude * weak_high_threshold < 1.0

strong_three = base_amplitude ** 1.5 * (2.0 + 2.0 * sqrt(2.0))
assert abs(strong_three - (2.0 + 2.0 * sqrt(2.0)) / 3.0) < 2e-15

print("signed-pair critical normalization and impulse: PASS")
print("fixed-cardinality L3 decay scale: PASS")
print("three-ring moment and Lorentz thresholds: PASS")
```

Commande de reproduction : extraire le bloc Python puis exécuter python -
depuis la racine du dépôt. Dépendances : bibliothèque standard Python.
Graine : aucune. La quadrature emploie 2 000 milieux et 182 rayons par
valeur de \(n\). Aucun fichier externe n'est lu ou écrit.

## 9. Critère d'abandon et prochaine bifurcation

### Critère d'abandon

Abandonner toute famille de cardinal uniformément borné si :

1. chaque composante reste un tore azimutal de rapport
   \(h_{n,j}/R_{n,j}\to0\);
2. le faible-\(L^{3/2}\) global est uniforme;
3. les corridors unitaires satisfont le test logarithmique à des échelles
   physiques \(\ell_n\to0\).

Sous ces trois conditions, (42) impose \(\|u_n\|_3\to0\), quels que soient
les signes et les moments finis annulés.

### Seule bifurcation encore informative

Tester une famille \(m_n\to\infty\). Pour des tores identiques disjoints, la
normalisation faible impose une quasi-norme individuelle typique

\[
 k_{n,j}\lesssim m_n^{-2/3}.
 \tag{49}
\]

La borne triangulaire devient

\[
 \|u_n\|_3
 \lesssim m_n^{1/3}\eta_n^{1/9}.
 \tag{50}
\]

Ne poursuivre que si \(m_n\) est assez grand pour empêcher le membre droit
de tendre vers zéro **et** si :

- les corridors \(q_{n,j}\) restent disjoints;
- les tores tiennent dans un domaine physique contrôlé;
- les queues de vitesse s'additionnent de façon cohérente au lieu de
  s'annuler;
- la masse forte critique, l'énergie et la pression restent uniformes;
- les moments nécessaires au raccord Clay sont réellement annulés;
- la construction sort de la classe axisymétrique sans swirl.

Si ces contraintes forcent
\(m_n^{1/3}\eta_n^{1/9}\to0\), ou font diverger l'une des normes critiques,
la branche multi-tore doit être fermée.

```json
{
  "cycle": "0029",
  "claim": "MOMENT_CORRECTED_FINITE_TORI",
  "status": "KINEMATICALLY_FEASIBLE_CRITICAL_VELOCITY_OBSTRUCTED",
  "positive": [
    "exact two-ring impulse cancellation",
    "uniform weak-L3/2 and strong critical mass",
    "disjoint global unit logarithmic corridors",
    "three-ring cancellation of one additional axial moment"
  ],
  "negative": [
    "every fixed-cardinality thin-torus family has velocity L3 tending to zero",
    "finite moment cancellation does not produce a Schwartz velocity",
    "axisymmetric no-swirl dynamics cannot yield blow-up"
  ],
  "next_test": "growing-cardinality moment-corrected non-axisymmetric tube family"
}
```
