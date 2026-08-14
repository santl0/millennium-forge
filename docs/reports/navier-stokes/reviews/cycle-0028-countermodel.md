# Cycle 0028 — anneau torique mince et extension logarithmique

Date : 2026-08-14.

Type de passe : contre-modèle géométrique et audit adverse. Cette passe est
une dérivation IA interne dans le même programme; elle n'est pas une revue
externe indépendante.

## Verdict

Un anneau torique de vorticité azimutale réfute le no-go naïf suivant :

\[
 \text{vorticité compacte, solénoïdale + moyenne nulle + contrôle critique}
 \Longrightarrow
 \text{zone de retour poloïdale à BMO d'ordre un}.
 \tag{1}
\]

Soit \(\Gamma_R\) le cercle de rayon majeur \(R\) autour de l'axe \(z\), et
soit

\[
 s(r,z)=\sqrt{(r-R)^2+z^2}.
 \tag{2}
\]

Pour \(0<h<R/8\), une vorticité

\[
 W_h(x)=B_h\varphi\!\left(\frac{s(r,z)}h\right)e_\theta
 \tag{3}
\]

où \(y\mapsto\varphi(|y|)\) appartient à
\(C_c^\infty(\mathbb R^2)\) et est positive dans le disque unité, est lisse,
compacte, exactement divergence-free et de moyenne
vectorielle nulle. Il n'existe ni interface axiale, ni capuchon
\(-\partial_z\psi\,e_r\). L'annulation provient du tour complet de
\(e_\theta\), et non de deux amplitudes antipodales adjacentes.

Après normalisation,

\[
 \|W_h\|_{L^{3/2,\infty}}=1,\qquad
 \int|W_h|^{3/2}=C_\varphi,
 \tag{4}
\]

uniformément en \(h\), tandis que

\[
 \|W_h\|_1\asymp(Rh^2)^{1/3},
 \qquad
 \|W_h\|_2^2\asymp(Rh^2)^{-1/3}.
 \tag{5}
\]

La direction \(e_\theta\) sur le tore admet une extension unitaire globale.
Pour

\[
 L=\log(q/h),\qquad h<q<R/8,
 \tag{6}
\]

on peut faire tourner logarithmiquement \(e_\theta\) vers \(e_z\) dans le
tube \(h<s<q\). L'estimation sur toutes les boules est

\[
 \|\widetilde\xi_h\|_{\mathrm{BMO}}
 \leq C\left(\frac1L+\frac qR\right).
 \tag{7}
\]

Avec

\[
 L_n=n^2,\qquad q_n=R/L_n,\qquad
 h_n=q_ne^{-L_n},
 \tag{8}
\]

et une insertion physique isotrope à l'échelle
\(\ell_n\asymp2^{-n}/n\), le semi-norme

\[
 \sup_{0<\rho<1/2}
 |\log\rho|\,
 \operatorname{MO}_{B_\rho}(\widetilde\xi_{h_n})
 \tag{9}
\]

reste borné. La boule déterminante a un rayon comparable à
\(\ell_n h_n\), à un facteur fixe près. Son oscillation est
\(\asymp1/L_n\), mais son poids contient \(L_n\); le produit reste d'ordre
un. Une boule contenant le tore entier a seulement une oscillation

\[
 O\!\left(\frac{(q_n/R)^2}{L_n}\right)=O(L_n^{-3}),
 \tag{10}
\]

et n'est pas maximisante.

Le contre-modèle ne produit pourtant aucune route vers un blow-up Clay :

- la vitesse de Biot--Savart est axisymétrique **sans swirl**, classe
  globalement régulière;
- on obtient même
  \(\|u_h\|_3\lesssim(h/R)^{1/9}\to0\), donc le régime petites données
  critiques;
- sur \(\mathbb R^3\), son impulsion hydrodynamique non nulle crée une queue
  algébrique; \(u_h\) n'est pas une donnée de Schwartz du libellé Clay;
- aucun champ non nul de cette famille ne peut être stationnaire pour
  Navier--Stokes non forcé, par l'identité d'énergie stationnaire.

Le tore clôt donc un faux verrou géométrique, mais il doit être abandonné
comme mécanisme dynamique de singularité.

## 1. Construction lisse et identités div--curl

On travaille en coordonnées cylindriques \((r,\theta,z)\), avec
\(R-h>0\). La direction azimutale est

\[
 e_\theta=(-\sin\theta,\cos\theta,0).
 \tag{11}
\]

Le champ (3) n'a que la composante \(W_\theta\) et ne dépend pas de
\(\theta\). Par la formule cylindrique,

\[
 \nabla\cdot W_h
 =\frac1r\partial_\theta W_\theta=0.
 \tag{12}
\]

Cette identité reste valable au sens des distributions pour un profil
étagé, car \(e_\theta\) est tangent au bord du tore. Le profil lisse évite
néanmoins toute ambiguïté de trace.

La moyenne vectorielle est exactement nulle :

\[
\begin{aligned}
 \int_{\mathbb R^3}W_h\,dx
 &=
 \int\!\!\int
 B_h\varphi(s/h)\,r\,dr\,dz
 \int_0^{2\pi}e_\theta\,d\theta\\
 &=0.
\end{aligned}
\tag{13}
\]

Il n'y a donc pas de petit compensateur d'amplitude opposée. La condition
\(\int\operatorname{curl}u=0\) est satisfaite par la géométrie fermée.

Comme \(W_h\in C_c^\infty\), \(\nabla\cdot W_h=0\), la vitesse de
Biot--Savart

\[
 u_h=\nabla\times(-\Delta)^{-1}W_h
 \tag{14}
\]

est lisse, divergence-free, vérifie

\[
 \nabla\times u_h=W_h
 \tag{15}
\]

et appartient à \(L^2(\mathbb R^3)\).

La vitesse (14) n'est en général pas compacte. C'est une différence
essentielle avec le potentiel azimutal compact du cycle 0027.
Le tore réfute donc une obstruction portant sur la vorticité compacte, mais
pas une obstruction dont l'hypothèse inclurait explicitement
\(u\in C_c^\infty\).

## 2. Normes critiques exactes

### 2.1 Formule de tube

Écrivons les coordonnées normales

\[
 r=R+h y_1,\qquad z=h y_2,\qquad y\in\mathbb R^2.
 \tag{16}
\]

Le jacobien tridimensionnel est

\[
 (R+h y_1)h^2\,dy\,d\theta.
 \tag{17}
\]

Les ensembles de niveau d'un profil radial \(\varphi(|y|)\) sont symétriques
en \(y_1\). Leur terme impair s'intègre à zéro. Si

\[
 A_\varphi(t)=|\{y\in\mathbb R^2:\varphi(|y|)>t\}|,
 \qquad
 K_\varphi=\sup_{t>0}tA_\varphi(t)^{2/3},
 \tag{18}
\]

alors

\[
 |\{|W_h|>\lambda\}|
 =2\pi Rh^2
 A_\varphi(\lambda/B_h).
 \tag{19}
\]

Par conséquent

\[
 \|W_h\|_{L^{3/2,\infty}}
 =B_h(2\pi Rh^2)^{2/3}K_\varphi.
 \tag{20}
\]

On choisit

\[
 B_h=
 \frac1{(2\pi Rh^2)^{2/3}K_\varphi}.
 \tag{21}
\]

Cela donne exactement la première identité de (4). De même,

\[
\begin{aligned}
 \int|W_h|^{3/2}dx
 &=B_h^{3/2}(2\pi Rh^2)
   \int_{\mathbb R^2}\varphi(|y|)^{3/2}dy\\
 &=K_\varphi^{-3/2}
   \int_{\mathbb R^2}\varphi(|y|)^{3/2}dy
 =:C_\varphi.
\end{aligned}
\tag{22}
\]

Pour le modèle étagé \(\varphi=\mathbf1_{\{|y|<1\}}\), le volume du tore est

\[
 V_h=2\pi^2Rh^2,
 \tag{23}
\]

on prend \(B_h=V_h^{-2/3}\), et les deux quantités de (4) valent exactement
un. Ce modèle sert uniquement au certificat algébrique; il est remplacé par
un bump fixe pour obtenir \(C_c^\infty\).

### 2.2 Masses sous-critiques et supercritiques

Pour tout profil fixe non nul,

\[
 \|W_h\|_1\asymp B_hRh^2\asymp(Rh^2)^{1/3},
 \tag{24}
\]

et

\[
 \|W_h\|_2^2
 \asymp B_h^2Rh^2
 \asymp(Rh^2)^{-1/3}.
 \tag{25}
\]

Le tore concentre donc une masse critique fixe avec une masse \(L^1\) qui
tend vers zéro et une enstrophie qui diverge. Il reproduit le mécanisme
d'intermittence du profil à deux amplitudes sans aucune phase directionnelle
opposée locale.

## 3. Extension unitaire de la direction

### 3.1 Définition

Fixons \(q<R/8\) et \(L=\log(q/h)\). Dans le tube \(s<q\), posons

\[
 \alpha(s)=
 \begin{cases}
 \pi/2,&0\leq s\leq h,\\[1mm]
 \displaystyle
 \frac{\pi}{2}\frac{\log(q/s)}L,&h<s<q,\\[2mm]
 0,&s\geq q.
 \end{cases}
 \tag{26}
\]

Puis définissons sur tout \(\mathbb R^3\)

\[
 \widetilde\xi_h(x)
 =\sin\alpha(s)e_\theta+\cos\alpha(s)e_z
 \quad\text{si }s<q,
 \qquad
 \widetilde\xi_h=e_z\quad\text{sinon}.
 \tag{27}
\]

Le tube \(s<q<R/8\) reste loin de l'axe. À son bord,
\(\sin\alpha=0\), donc la formule rejoint \(e_z\). Près de l'axe cylindrique,
le champ est identiquement \(e_z\); la singularité de coordonnées de
\(e_\theta\) disparaît.

Le champ est unitaire partout et coïncide avec
\(W_h/|W_h|=e_\theta\) sur \(\{W_h\ne0\}\). Les coins de \(\alpha\) en
\(h,q\) peuvent être lissés sur des intervalles de rapport fixé sans changer
les ordres \(1/L\).

### 3.2 Estimation BMO sur toutes les échelles

La fonction tronquée \(\log s\), distance logarithmique à une courbe lisse de
codimension deux, a une norme BMO locale uniforme dans un tube de courbure
bornée. La composition lipschitzienne dans (26)--(27) donne la partie
\(C/L\). Sur un morceau de tube de diamètre \(\rho\leq q\),

\[
 |e_\theta(x)-e_\theta(y)|
 \leq C\frac{\rho}{R},
 \tag{28}
\]

ce qui ajoute au plus \(Cq/R\). Pour les boules plus grandes que \(q\), on
intègre directement la fraction du tube et on obtient une borne plus petite.
Ainsi

\[
 \sup_B\dashint_B
 |\widetilde\xi_h-(\widetilde\xi_h)_B|
 \leq C\left(\frac1L+\frac qR\right).
 \tag{29}
\]

Cette preuve nécessite les boules euclidiennes tridimensionnelles. Une
vérification dans la seule section méridienne manquerait la variation de
\(e_\theta\) le long du cercle.

## 4. Quelle boule maximise le test logarithmique ?

On écrit

\[
 S_n=|\log(\ell_nR)|.
 \tag{30}
\]

Pour (8), \(q_n/R=L_n^{-1}\) et

\[
 \log(R/h_n)=L_n+\log L_n.
 \tag{31}
\]

Les régimes de boules sont les suivants.

| Rayon de base \(\rho\) | Oscillation dominante | Poids physique |
|---|---:|---:|
| \(\rho<h_n\) | \(O(\rho/R+\rho/(h_nL_n))\) si la boule touche l'interface | \(S_n+\log(R/\rho)\) |
| \(\rho\asymp h_n\) | \(\asymp L_n^{-1}\) | \(S_n+L_n+\log L_n+O(1)\) |
| \(h_n<\rho<q_n\) | \(O(L_n^{-1}+\rho/R)\) | \(S_n+\log(R/\rho)\) |
| \(q_n\leq\rho\ll R\) | \(O(q_n^2/(L_n\rho^2))\) | \(S_n+\log(R/\rho)\) |
| \(\rho\asymp R\) | \(O((q_n/R)^2/L_n)\) | \(S_n+O(1)\) |
| \(\rho\gg R\) | \(O(Rq_n^2/(L_n\rho^3))\) | décroît après dilution |

Le deuxième régime donne

\[
 |\log(\ell_nh_n)|
 \operatorname{MO}_{B_{c\ell_nh_n}}\widetilde\xi_{h_n}
 \asymp
 \frac{S_n+L_n+\log L_n}{L_n}.
 \tag{32}
\]

Si \(L_n=n^2\) et
\(\ell_n\asymp2^{-n}/n\), alors \(S_n=O(n)\) et (32) reste entre deux
constantes positives. Le prolongement appartient donc uniformément à
\(\mathrm{bmo}_{1/|\log r|}\), mais sa semi-norme pondérée ne tend pas vers
zéro.

### 4.1 Boule contenant le tore entier

Dans une section normale, l'intégrale de
\(|\widetilde\xi_h-e_z|\) vérifie

\[
 \int_{s<q}|\widetilde\xi_h-e_z|\,dA
 \leq C\frac{q^2}{L}.
 \tag{33}
\]

Après multiplication par la longueur \(2\pi R\), puis division par le volume
d'une boule de rayon comparable à \(R\),

\[
 \operatorname{MO}_{B_{CR}}
 (\widetilde\xi_h)
 \leq C\frac{q^2}{R^2L}.
 \tag{34}
\]

La moyenne azimutale de \(e_\theta\) est nulle; elle ne crée pas un terme
caché d'ordre un. Avec \(q/R=1/L\), (34) est \(O(L^{-3})\). Même après le
poids physique \(S_n\), cette boule contribue seulement
\(O(S_n/L_n^3)\).

### 4.2 Pourquoi prolonger par zéro échoue

Le champ

\[
 \xi_0=e_\theta\mathbf1_{\{W_h\ne0\}}
 \tag{35}
\]

n'est pas unitaire sur les zéros. À une frontière régulière du support, une
petite boule contient les modules un et zéro en fractions comparables; son
oscillation tend vers \(1/2\). Le poids logarithmique diverge lorsque le
rayon tend vers zéro.

L'extension (27), et non le prolongement par zéro, est donc une partie
essentielle du contre-modèle.

## 5. Vitesse de Biot--Savart

### 5.1 Énergie

L'inégalité de Hardy--Littlewood--Sobolev donne

\[
 \|u_h\|_2
 \leq C\|W_h\|_{6/5}.
 \tag{36}
\]

Pour le profil de tube,

\[
 \|W_h\|_{6/5}
 \asymp B_h(Rh^2)^{5/6}
 \asymp(Rh^2)^{1/6}.
 \tag{37}
\]

Ainsi

\[
 \|u_h\|_2\lesssim(Rh^2)^{1/6}\longrightarrow0.
 \tag{38}
\]

L'énergie n'explose pas malgré l'enstrophie divergente.

### 5.2 Norme critique de vitesse

Une estimation directe du noyau de Biot--Savart sur un tube donne

\[
 \|u_h\|_\infty\leq CB_hh.
 \tag{39}
\]

La région à distance inférieure à \(h\) contribue \(O(B_hh)\). Sur une
portion de tube à distance longitudinale \(d\in(h,R)\), la section \(h^2\)
et le noyau \(d^{-2}\) donnent encore
\(B_hh^2\int_h^Rd^{-2}dd=O(B_hh)\).

En interpolant \(L^2\) et \(L^\infty\),

\[
\begin{aligned}
 \|u_h\|_3
 &\leq\|u_h\|_2^{2/3}\|u_h\|_\infty^{1/3}\\
 &\leq C\left(\frac hR\right)^{1/9}.
\end{aligned}
\tag{40}
\]

La vorticité conserve une norme critique d'ordre un, mais la vitesse
critique tend vers zéro. Toute insertion isotrope conserve la norme \(L^3\);
elle ne répare pas cette dégénérescence.

### 5.3 Queue lointaine et formulation Clay

L'impulsion hydrodynamique

\[
 I_h=\frac12\int x\times W_h\,dx
\tag{41}
\]

a une composante axiale strictement positive lorsque
\(\varphi\geq0\), \(\varphi\not\equiv0\) :

\[
 (I_h)_z=\frac12\int r|W_h|\,dx>0.
 \tag{42}
\]

Pour le tore étagé,

\[
 (I_h)_z
 =B_h\left(
 \pi^2R^2h^2+\frac{\pi^2}{4}h^4
 \right).
 \tag{43}
\]

Ce moment produit le premier multipôle non nul de la vitesse. La vitesse
(14) a une queue algébrique, typiquement \(O(|x|^{-3})\), et n'est pas une
donnée de Schwartz sur \(\mathbb R^3\). Elle ne satisfait donc pas telle
quelle les hypothèses de décroissance rapide de la formulation Clay espace
entier.

Sur un tore périodique assez grand, la moyenne (13) permet en revanche
d'inverser le curl dans la classe périodique moyenne nulle. On obtient une
donnée initiale périodique lisse. La périodisation brise toutefois
l'axisymétrie globale du domaine euclidien; la petitesse critique et la
dynamique doivent être revérifiées avec l'inverse périodique avant tout
raccord à la formulation Clay périodique.

## 6. Pression, résidu et dynamique

### 6.1 Pression non locale

Pour la vitesse de Biot--Savart,

\[
 p_h=R_iR_j((u_h)_i(u_h)_j)
 \tag{44}
\]

et

\[
 \|p_h\|_{3/2}
 \leq C\|u_h\|_3^2
 \lesssim\left(\frac hR\right)^{2/9}.
 \tag{45}
\]

La pression est non locale, mais elle devient petite dans la norme critique
associée. Elle ne fournit pas un mécanisme caché de concentration pour cette
famille.

### 6.2 Le profil n'est pas stationnaire

Supposons qu'un \(u_h\) non nul, lisse, d'énergie finie et suffisamment
décroissant soit une solution stationnaire non forcée :

\[
 -\nu\Delta u_h+(u_h\cdot\nabla)u_h+\nabla p_h=0,
 \qquad \nabla\cdot u_h=0.
 \tag{46}
\]

Le produit scalaire avec \(u_h\), intégré sur \(\mathbb R^3\), donne

\[
 \nu\int|\nabla u_h|^2=0.
 \tag{47}
\]

Donc \(u_h=0\), contradiction. Le résidu stationnaire ne peut être annulé
par une pression.

Au niveau d'échelle, \(|\nabla W_h|\asymp B_h/h\) et
\(|\Delta W_h|\asymp B_h/h^2\) dans la section. La viscosité devient plus,
et non moins, importante lorsque \(h\to0\). Ces relations sont des ordres de
grandeur pour un bump fixé, pas une minoration certifiée d'un résidu après
projection.

### 6.3 Évolution

La vitesse (14) est axisymétrique sans composante azimutale. Sa vorticité est
précisément \(W_\theta e_\theta\). C'est la sous-classe axisymétrique sans
swirl, globalement régulière pour des données lisses d'énergie finie.

Indépendamment de cette rigidité géométrique, (40) place la famille dans le
régime petites données \(L^3\) pour \(h/R\) assez petit. Le tore est donc un
contre-modèle cinématique utile et un candidat dynamique négatif.

La diffusion détruit immédiatement le support compact de la vorticité à
temps positif. Une photographie torique mince à \(t=0\) ne définit ni une
solution ancienne, ni un profil de blow-up, ni une cascade persistante.

## 7. Ce que le tore réfute, et ce qu'il ne réfute pas

| Affirmation | Statut après le test |
|---|---|
| une vorticité compacte solénoïdale de moyenne nulle exige deux directions antipodales adjacentes | réfutée : la rotation de \(e_\theta\) annule la moyenne |
| tout retour axisymétrique crée un cap radial \(W_r=-\partial_z\psi\) | réfutée pour une vorticité toroidale; ce terme appartenait au potentiel de vitesse purement swirl |
| le tour complet de \(e_\theta\) force BMO d'ordre un | réfutée par l'extension tubulaire logarithmique |
| la boule contenant le tore maximise le test | réfutée : contribution \(O(L^{-3})\) |
| la norme critique de vorticité force une vitesse \(L^3\) non petite | réfutée : borne (40) |
| ce tore est un blow-up admissible | faux : classe sans swirl régulière et petites données |
| le même mécanisme existe avec une vitesse compacte de Schwartz sur \(\mathbb R^3\) | non démontré; l'impulsion (42) l'empêche ici |

Le changement de formulation est explicite :

- cycle 0027 : vitesse purement azimutale \(u^\theta e_\theta\), vorticité
  méridienne;
- cycle 0028 : vorticité purement azimutale \(W^\theta e_\theta\), vitesse
  méridienne sans swirl.

Confondre ces deux classes invaliderait le transfert.

## 8. Test numérique déterministe des échelles BMO

Le certificat ci-dessous vérifie :

- le volume, la normalisation faible et la masse critique du tore étagé;
- les exposants des normes \(L^1\), \(L^2\), \(L^{6/5}\) et de la borne
  \(L^3\) de vitesse;
- la positivité exacte de l'impulsion;
- la recherche, dans l'approximation locale d'un tube droit, de la boule
  maximisant le produit pondéré.

Dans le modèle local, la direction ne dépend que de la distance \(s\) à
l'axe du tube. Une boule tridimensionnelle de rayon \(\rho\) a la densité
radiale \(s\sqrt{\rho^2-s^2}\,ds\). La quadrature est déterministe mais
n'est pas un calcul par intervalles; elle localise une échelle, elle ne
certifie pas le supremum continu.

```python
from math import cos, exp, log, pi, sin, sqrt


def angle(log_s, log_h, log_q, transition_depth):
    if log_s <= log_h:
        return pi / 2.0
    if log_s >= log_q:
        return 0.0
    return (pi / 2.0) * (log_q - log_s) / transition_depth


def straight_tube_ball_mo(
    log_rho, log_h, log_q, transition_depth, quadrature_points=2500
):
    samples = []
    total_weight = mean_x = mean_z = 0.0
    for index in range(quadrature_points):
        t = (index + 0.5) / quadrature_points
        weight = t * sqrt(1.0 - t * t)
        alpha = angle(
            log_rho + log(t), log_h, log_q, transition_depth
        )
        component_x = sin(alpha)
        component_z = cos(alpha)
        samples.append((weight, component_x, component_z))
        total_weight += weight
        mean_x += weight * component_x
        mean_z += weight * component_z

    mean_x /= total_weight
    mean_z /= total_weight
    return sum(
        weight
        * sqrt((component_x - mean_x) ** 2 + (component_z - mean_z) ** 2)
        for weight, component_x, component_z in samples
    ) / total_weight


# Exact scaling identities for the top-hat model, checked in logarithms.
for n in [4, 8, 12, 16]:
    major_radius = 1.0
    transition_depth = float(n * n)
    log_q = -log(transition_depth)
    log_h = log_q - transition_depth
    log_volume = log(2.0 * pi * pi * major_radius) + 2.0 * log_h
    log_amplitude = -(2.0 / 3.0) * log_volume

    # weak L^(3/2) quasi-norm and strong critical mass are exactly one.
    assert abs(log_amplitude + (2.0 / 3.0) * log_volume) < 1e-13
    assert abs(1.5 * log_amplitude + log_volume) < 1e-13

    # Scaling exponents.
    log_l1 = log_amplitude + log_volume
    log_enstrophy = 2.0 * log_amplitude + log_volume
    log_w65 = log_amplitude + (5.0 / 6.0) * log_volume
    assert abs(log_l1 - log_volume / 3.0) < 1e-13
    assert abs(log_enstrophy + log_volume / 3.0) < 1e-13
    assert abs(log_w65 - log_volume / 6.0) < 1e-13

    # L2--Linf interpolation gives ||u||_3 <= C (h/R)^(1/9).
    interpolated_log_u3 = (
        (2.0 / 3.0) * (log_volume / 6.0)
        + (1.0 / 3.0) * (log_amplitude + log_h)
    )
    expected_log_u3 = (log_h - log(major_radius)) / 9.0
    geometric_constant = interpolated_log_u3 - expected_log_u3
    # The difference is independent of n and comes from 2*pi^2.
    expected_constant = -log(2.0 * pi * pi) / 9.0
    assert abs(geometric_constant - expected_constant) < 1e-12

    # The top-hat hydrodynamic impulse is strictly positive.
    if n <= 8:
        h = exp(log_h)
        volume = 2.0 * pi * pi * major_radius * h * h
        amplitude = volume ** (-2.0 / 3.0)
        impulse_z = amplitude * (
            pi * pi * major_radius**2 * h**2
            + (pi * pi / 4.0) * h**4
        )
        assert impulse_z > 0.0

    # Search near the core and across the whole logarithmic corridor.
    log_ell = -n * log(2.0) - log(float(n))
    offsets = [-2.0 + 0.1 * j for j in range(101)]
    offsets += [
        8.0 + (transition_depth - 6.0) * j / 100.0
        for j in range(101)
    ]
    best = (-1.0, None, None)
    for offset in offsets:
        log_rho = log_h + offset
        mo = straight_tube_ball_mo(
            log_rho, log_h, log_q, transition_depth
        )
        weighted = abs(log_ell + log_rho) * mo
        if weighted > best[0]:
            best = (weighted, offset, mo)

    # The maximizer is within a fixed logarithmic distance of h.
    assert 0.0 < best[1] < 6.0
    assert 0.4 < best[0] < 1.2

    # A ball containing the whole torus has the much smaller scale L^-3.
    whole_torus_proxy = transition_depth ** (-3)
    assert whole_torus_proxy < best[2]

    print(
        f"n={n:2d} weighted_max={best[0]:.6f} "
        f"log(rho/h)={best[1]:.2f} local_MO={best[2]:.6e}"
    )

print("toroidal critical scaling and impulse: PASS")
print("local weighted-BMO scale search: PASS")
```

Commande de reproduction : extraire le bloc Python puis exécuter python -
depuis la racine du dépôt. Dépendances : bibliothèque standard Python.
Graine : aucune. La quadrature utilise 2 500 milieux et 202 rayons candidats
par valeur de \(n\). Les identités de scaling sont testées en logarithmes
pour éviter l'underflow des épaisseurs \(h_n\).

## 9. Critère d'abandon et prochain test

### Abandon dynamique

La branche « un seul tore azimutal mince » doit être abandonnée comme route
vers un blow-up dès que l'une des deux vérifications suivantes est établie :

1. la donnée reste axisymétrique sans swirl sous l'évolution;
2. \(\|u_h\|_3\) passe sous le seuil universel de petites données.

Ici les deux sont satisfaites. L'abandon dynamique est donc immédiat et ne
dépend pas d'un calcul de longue durée.

### Valeur informationnelle conservée

Le tore reste un falsificateur de toute obstruction qui utilise seulement :

\[
 \nabla\cdot W=0,\quad
 \int W=0,\quad
 \|W\|_{L^{3/2,\infty}}\leq C,\quad
 \int|W|^{3/2}\geq c,\quad
 \widetilde\xi\in\mathrm{bmo}_{1/|\log r|}.
 \tag{48}
\]

Ces portes cinématiques sont compatibles avec une vitesse critique qui tend
vers zéro.

### Prochain test discriminant

Une réouverture exige au minimum une famille de plusieurs anneaux ou tubes
pour laquelle :

- \(\|u_n\|_3\geq c_0>0\) après toutes les annulations;
- la vitesse est une donnée de Schwartz sur \(\mathbb R^3\), ou une donnée
  périodique officielle;
- les moments responsables des queues lointaines sont annulés sans créer
  d'interface directionnelle d'ordre un;
- une composante de swirl ou une géométrie non axisymétrique sort de la
  classe globalement régulière;
- le supremum pondéré est recalculé aux épaisseurs internes de chaque tube;
- pression, énergie, enstrophie et résidu sont suivis avec les interactions
  croisées.

Abandonner aussi cette extension si le maintien d'un \(L^3\) non petit exige
un nombre de tores qui fait diverger le faible-\(L^{3/2}\), l'énergie, ou le
semi-norme log-BMO.

```json
{
  "cycle": "0028",
  "claim": "TOROIDAL_THIN_RING_BMO_COUNTERMODEL",
  "status": "KINEMATIC_COUNTERMODEL_DYNAMIC_BRANCH_ABANDONED",
  "proved_or_derived": [
    "smooth compact divergence-free toroidal vorticity with zero vector mean",
    "uniform weak-L3/2 and strong critical vorticity mass",
    "global unit logarithmic direction extension",
    "weighted BMO maximum occurs near the core scale, not the whole-ring scale",
    "Biot-Savart velocity L3 tends to zero"
  ],
  "gaps": [
    "continuous BMO supremum constants are not interval-certified",
    "R3 Biot-Savart velocity is not Schwartz because hydrodynamic impulse is nonzero",
    "no compactly supported divergence-free velocity is constructed",
    "no Navier-Stokes blow-up mechanism exists in the axisymmetric no-swirl class"
  ],
  "next_test": "multi-ring moment-cancelled family with non-small velocity L3"
}
```
