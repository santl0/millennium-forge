# Cycle 0036 — Gouttelettes pure-swirl séparées et filament sous le seuil

Date : 2026-08-14
Statut : calcul cinématique exact sur un squelette lipschitzien, bornes stables par lissage \(C_c^\infty\)
Portée : \(\mathbb R^3\), cellules axisymétriques pure-swirl, aucune évolution Navier–Stokes construite

## Verdict

Le contre-modèle multi-gouttes ne fournit pas la fuite recherchée.

Pour \(m\) gouttes identiques de petit rayon méridien \(\rho\), placées dans
le même anneau de rayon majeur \(\mathcal R\), séparées axialement et reliées
seulement par un filament sous le seuil actif,

\[
 K_u\asymp A(m\mathcal R\rho^2)^{1/3},\qquad
 K_w\asymp {A\over\rho}(m\mathcal R\rho^2)^{2/3},
 \tag{36.1}
\]

dès que le filament est assez faible pour ne pas dominer le curl. Donc

\[
 \boxed{{K_u\over K_w}\asymp
 m^{-1/3}\left({\rho\over\mathcal R}\right)^{1/3}.}
 \tag{36.2}
\]

Le comptage pénalise le rapport par \(m^{-1/3}\). L'amplitude commune
\(A_m\) disparaît exactement du quotient. Pour garder \(K_u\asymp1\),
\(K_w\) diverge; pour garder \(K_w\asymp1\), \(K_u\) tend vers zéro.

Le filament sous \(\lambda/4\) ne relie pas les composantes du superniveau.
Sa troncature positive ne crée aucune mesure de bord. En répétant le registre
du cycle 0035 composante par composante, on obtient

\[
 \max_\alpha K_{u,\alpha}
 \ge {C_I\over648}{K_u^2\over K_w}.
 \tag{36.3}
\]

Si chaque composante tronquée est contenue dans une boule de rayon
\(C\mathcal R\), cette boule fournit le rapport local. La conclusion concerne
une boule **contenant la goutte entière**. Elle serait fausse pour toutes les
intersections arbitraires : une boule tangente peut découper un morceau de
plateau sans son raccord de curl.

## 1. Modèle reproductible

On distingue le rayon annulaire \(\mathcal R\), qui calibre aussi les boules,
du rayon méridien \(\rho_i\) des gouttes. On suppose

\[
 0<\rho_i\le {\mathcal R\over4},\qquad
 |z_i-z_j|>4C\mathcal R\quad(i\ne j),\qquad C\ge {3\over2}.
 \tag{36.4}
\]

Dans les coordonnées cylindriques, posons

\[
 U={\mathcal R\over r}F(r,z)e_\theta.
 \tag{36.5}
\]

Le chapeau unidimensionnel est

\[
 h(x)=
 \begin{cases}
 1,&|x|\le1/4,\\
 2-4|x|,&1/4<|x|<1/2,\\
 0,&|x|\ge1/2.
 \end{cases}
 \tag{36.6}
\]

Les gouttes et le filament sont

\[
 F_i(r,z)=\sigma_iA_i
 h\!\left({r-\mathcal R\over\rho_i}\right)
 h\!\left({z-z_i\over\rho_i}\right),\qquad
 \sigma_i\in\{-1,1\},
 \tag{36.7}
\]

\[
 F_{\rm fil}(r,z)=a_f
 h\!\left({r-\mathcal R\over s}\right)J(z),\qquad
 0<s\le{\min_i\rho_i\over16},\qquad
 0<a_f<{\lambda\over8}.
 \tag{36.8}
\]

Ici \(J=1\) entre les gouttes extrêmes et se ferme linéairement sur deux
caps de longueur \(\ell\). Sa longueur de plateau est \(L\). Enfin

\[
 F=\sum_{i=1}^mF_i+F_{\rm fil}.
 \tag{36.9}
\]

Comme \(\mathcal R/r\le8/7\) sur le filament, (36.8) implique
\(|U_{\rm fil}|<\lambda/7<\lambda/4\). Entre les gouttes, le filament est
donc invisible dans le niveau actif. Il rend seulement le support
topologique de \(F\) connexe.

Le squelette est lipschitzien. Le remplacement de chaque rampe par un profil
monotone \(C^\infty\), dans une fraction relative
\(\varepsilon<10^{-2}\), donne \(F_\varepsilon\in C_c^\infty\). Les
plateaux témoins perdent au plus \(O(\varepsilon)\) de leur volume et toutes
les constantes restent uniformes en \(m,L,A_i,\rho_i\).

## 2. Divergence et curl complet

Le champ (36.5) est exactement divergence-free. Pour tout \(F\) indépendant
de \(\theta\),

\[
 W=-{\mathcal R\over r}\partial_zF\,e_r
 +{\mathcal R\over r}\partial_rF\,e_z.
 \tag{36.10}
\]

Les contributions d'une goutte sont

\[
 W_{r,i}=-{\sigma_iA_i\mathcal R\over r\rho_i}
 h\!\left({r-\mathcal R\over\rho_i}\right)
 h'\!\left({z-z_i\over\rho_i}\right),
 \tag{36.11}
\]

\[
 W_{z,i}={\sigma_iA_i\mathcal R\over r\rho_i}
 h'\!\left({r-\mathcal R\over\rho_i}\right)
 h\!\left({z-z_i\over\rho_i}\right).
 \tag{36.12}
\]

Le filament apporte, y compris ses deux caps,

\[
 W_{r,f}=-{a_f\mathcal R\over r}
 h\!\left({r-\mathcal R\over s}\right)J'(z),\qquad
 W_{z,f}={a_f\mathcal R\over rs}
 h'\!\left({r-\mathcal R\over s}\right)J(z).
 \tag{36.13}
\]

Il n'y a pas de composante \(e_\theta\). Les formules (36.11)--(36.13)
inventorient deux raccords axiaux et deux raccords radiaux par goutte, deux
caps axiaux et deux parois radiales pour le filament.

Les variations exactes sont

\[
 \int h={3\over4},\quad \int h^2={2\over3},\quad
 \int|h'|=2,\quad \int|h'|^2=8,\quad
 \operatorname{TV}(J)=2.
 \tag{36.14}
\]

En particulier,

\[
 \|W_{r,f}\|_1=3\pi a_f\mathcal R s,\qquad
 \|W_{z,f}\|_1=4\pi a_f\mathcal R(L+\ell).
 \tag{36.15}
\]

La petite amplitude du filament ne supprime pas son coût radial quand sa
longueur croît.

## 3. Distributions globales et locales

On note \(\mu_G(t)=|\{|G|>t\}|\). Pour (36.9), les distributions complètes
sont les intégrales finies

\[
 \mu_U(t)=2\pi\int_{\mathbb R}\int_0^\infty
 r\,\mathbf1_{\{|\mathcal RF(r,z)/r|>t\}}\,dr\,dz,
 \tag{36.16}
\]

\[
 \mu_W(q)=2\pi\int_{\mathbb R}\int_0^\infty r\,
 \mathbf1_{\{(\mathcal R/r)^2(F_r^2+F_z^2)>q^2\}}\,dr\,dz.
 \tag{36.17}
\]

Toutes les fonctions dans les indicatrices sont affines par morceaux. Ces
formules suivent le jacobien cylindrique et incluent les recouvrements
goutte--filament.

### Gouttes

Le volume support exact d'une goutte est

\[
 V_i=2\pi\mathcal R\rho_i^2.
 \tag{36.18}
\]

Dans le plateau annulaire qui exclut le filament,
\(\rho_i/8<|r-\mathcal R|<\rho_i/4\),
\(|z-z_i|<\rho_i/4\), le volume est

\[
 v_i={\pi\over4}\mathcal R\rho_i^2,
 \tag{36.19}
\]

et \(|U|\ge(8/9)A_i\). Sur les deux rampes radiales, avec plateau
axial, un ensemble de volume \((\pi/2)\mathcal R\rho_i^2\) satisfait

\[
 |W|=|W_{z,i}|\ge {32\over9}{A_i\over\rho_i}.
 \tag{36.20}
\]

Le filament est nul sur ces rampes, donc aucune cancellation n'est cachée.
Sur tout le support,

\[
 |U_i|\le {8\over7}A_i,\qquad
 |W_i|\le {32\sqrt2\over7}{A_i\over\rho_i}.
 \tag{36.21}
\]

On a donc les sandwiches certifiés

\[
 \sum_i v_i\mathbf1_{\{t<(8/9)A_i\}}\le\mu_U(t),
 \tag{36.22}
\]

\[
 \mu_W(q)\ge
 \sum_i{\pi\over2}\mathcal R\rho_i^2
 \mathbf1_{\{q<(32/9)A_i/\rho_i\}}.
 \tag{36.23}
\]

Pour \(t>2a_f\),

\[
 \mu_U(t)\le
 \sum_iV_i\mathbf1_{\{t<(8/7)(A_i+a_f)\}}.
 \tag{36.24}
\]

La boule canonique

\[
 B_i=B((0,0,z_i),C\mathcal R),\qquad C\ge3/2,
 \tag{36.25}
\]

contient toute la goutte \(i\), donc toutes ses contributions dans
(36.18)--(36.23). La séparation (36.4) exclut les autres gouttes.

### Filament

Pour \(0<t<1\), la distribution axiale de \(J\) est

\[
 D_J(t)=L+2\ell(1-t).
 \tag{36.26}
\]

Ses distributions isolées sont exactement

\[
 \mu_{U_f}(q)=2\pi\int_{\mathcal R-s/2}^{\mathcal R+s/2}
 rD_J\!\left({qr\over a_f\mathcal Rh((r-\mathcal R)/s)}\right)dr,
 \tag{36.27}
\]

\[
 \mu_{W_{z,f}}(q)=2\pi\int_{\{h'\ne0\}}
 rD_J\!\left({qrs\over4a_f\mathcal R}\right)dr,
 \tag{36.28}
\]

\[
 \mu_{W_{r,f}}(q)=4\pi\ell
 \int_{\mathcal R-s/2}^{\mathcal R+s/2}
 r\mathbf1_{\{a_f\mathcal Rh/(r\ell)>q\}}dr.
 \tag{36.29}
\]

À constantes absolues,

\[
 K_{u,f}\asymp a_f(\mathcal RsL)^{1/3},\quad
 K_{w_z,f}\asymp {a_f\over s}(\mathcal RsL)^{2/3},\quad
 {K_{u,f}\over K_{w_z,f}}\asymp
 \left({s^2\over\mathcal RL}\right)^{1/3}.
 \tag{36.30}
\]

Un filament plus long aggrave son propre rapport. Pour \(s=\rho/16\),
\(L\simeq mD\) et

\[
 {a_f\over A}\le {1\over16}
 \left({\rho\over\mathcal R}\right)^{2/3},
 \tag{36.31}
\]

son coût faible-\(L^{3/2}\) reste une fraction contrôlée du coût des gouttes.
Avec une amplitude seulement comparable à \(\lambda/4\), il peut au
contraire dominer \(K_w\), rendant le contre-modèle encore moins favorable.

## 4. Normes, boules et normalisations

Pour des gouttes identiques et (36.31), (36.1)--(36.2) suivent des
distributions. Dans la boule complète \(B_i\),

\[
 {K_u(U;B_i)\over K_w(W;B_i)}
 \asymp\left({\rho\over\mathcal R}\right)^{1/3}.
 \tag{36.32}
\]

Le meilleur rapport parmi les boules canoniques contenant une composante a
le même ordre. Si \(\rho_m/\mathcal R\to0\), tous ces rapports tendent vers
zéro, mais le rapport global décroît encore plus vite.

Normaliser \(K_u=1\) impose

\[
 A_m\asymp(m\mathcal R\rho_m^2)^{-1/3},\qquad
 K_w^3\asymp {m\mathcal R\over\rho_m}\to\infty.
 \tag{36.33}
\]

Normaliser \(K_w=1\) impose

\[
 A_m\asymp \rho_m(m\mathcal R\rho_m^2)^{-2/3},\qquad
 K_u^3\asymp{\rho_m\over m\mathcal R}\to0.
 \tag{36.34}
\]

Garder \(K_u/K_w\ge c>0\) demanderait
\(\rho_m\gtrsim cm\mathcal R\), incompatible avec
\(\rho_m\le\mathcal R/4\).

Pour des amplitudes et rayons hétérogènes,

\[
 \mu_U(t)\simeq\sum_{A_i\gtrsim t}\mathcal R\rho_i^2,\qquad
 \mu_W(q)\gtrsim\sum_{A_i/\rho_i\gtrsim q}\mathcal R\rho_i^2.
 \tag{36.35}
\]

Fixons \(I_t=\{i:A_i\ge t\}\),
\(V_t=\sum_{i\in I_t}\mathcal R\rho_i^2\), et
\(\rho_*=\max_{i\in I_t}\rho_i\). Tous ces indices vérifient
\(A_i/\rho_i\ge t/\rho_*\), donc

\[
 { [tV_t^{1/3}]^3\over[(t/\rho_*)V_t^{2/3}]^3}
 ={\rho_*^3\over V_t}\le{\rho_*\over\mathcal R}.
 \tag{36.36}
\]

Le seuil presque optimal pour \(K_u\) montre que l'échelonnement des
amplitudes ne répare pas le quotient.

## 5. Troncature composante et facteur 648

Pour le seuil presque optimal \(\lambda\), un signe \(\sigma\), et une
composante \(\Omega_\alpha\) de \(\{\sigma F>\lambda/4\}\), définissons

\[
 G_\alpha=(\sigma F-\lambda/4)_+
 \mathbf1_{\Omega_\alpha},\qquad
 U_\alpha={\mathcal R\over r}G_\alpha e_\theta.
 \tag{36.37}
\]

La troncature est lipschitzienne et sa trace est nulle sur
\(\partial\Omega_\alpha\). La règle de chaîne Sobolev donne

\[
 \nabla G_\alpha=\sigma\mathbf1_{\Omega_\alpha}
 \mathbf1_{\{\sigma F>\lambda/4\}}\nabla F
 \quad\hbox{p.p.}
 \tag{36.38}
\]

Il n'existe **aucun terme de surface** sur
\(\{\sigma F=\lambda/4\}\). Le curl de cutoff est

\[
 \nabla\times U_\alpha=\sigma W
 \quad\hbox{p.p. sur }\Omega_\alpha,
 \tag{36.39}
\]

et zéro ailleurs. La direction y est \(\sigma W/|W|\), sans direction
parasite.

Posons \(E_\alpha=\{\sigma F>\lambda/2\}\cap\Omega_\alpha\),
\(V_\alpha=|E_\alpha|\), et
\(H_\alpha=\{\lambda/4<\sigma F<\lambda/2\}\cap\Omega_\alpha\).
Sur \(E_\alpha\), \(G_\alpha>\lambda/4\), donc

\[
 K_u(U_\alpha)\ge{\lambda\over6}V_\alpha^{1/3}.
 \tag{36.40}
\]

Si \(\varepsilon=\max_\alpha K_u(U_\alpha)\), alors
\(V_\alpha^{1/3}\le6\varepsilon/\lambda\). Coaire et isopérimétrie donnent

\[
 \int_H|W|\ge {C_I\lambda^2\over36\varepsilon}V,\qquad
 V=\sum_\alpha V_\alpha\ge\mu_U(\lambda).
 \tag{36.41}
\]

Comme \(H\subset\{|U|>\lambda/6\}\), Lorentz donne

\[
 \int_H|W|\le {18K_wK_u\over\lambda}.
 \tag{36.42}
\]

En cubant le seuil presque optimal,

\[
 \boxed{\varepsilon\ge {C_I\over648}{K_u^2\over K_w}},
 \qquad 648=36\times18.
 \tag{36.43}
\]

Le facteur supplémentaire \(2\) par rapport à \(324\) vient de la
soustraction \(\lambda/4\) : la vitesse tronquée est minorée par
\(\lambda/6\), non \(\lambda/3\).

Si \(\Omega_\alpha\subset B_\alpha\), alors

\[
 K_u(U;B_\alpha)\ge K_u(U_\alpha),\qquad
 K_w(W;B_\alpha)\le K_w(W),
 \tag{36.44}
\]

donc la boule contenant la goutte hérite de (36.3). Le filament lisse sous
seuil ne change ni les composantes ni (36.38). S'il dépasse
\(\lambda/4\), il les fusionne, mais son volume entre alors dans la bande
et son curl dans (36.41); ce n'est plus un raccord gratuit.

## 6. Coût BMO directionnel

Sur les rampes radiales intérieure et extérieure,
\(W/|W|=\sigma_i e_z\) et \(-\sigma_i e_z\). Une boule locale de rayon
\(c\rho_i\) rencontre deux sous-ensembles de fractions fixes portant ces
valeurs antipodales. Pour toute extension unitaire
\(\widetilde\xi\), l'inégalité triangulaire donne

\[
 [\widetilde\xi]_{\rm BMO}\ge c_0>0,
 \tag{36.45}
\]

uniformément en \(m,A_i,\rho_i\). Multiplier une composante par
\(\sigma_i\) ne change pas sa semi-norme.

Sous la convention log-BMO du cycle 0033,

\[
 [\widetilde\xi]_{\log{\rm BMO}}\gtrsim
 c_0(1+|\log\rho_i|).
 \tag{36.46}
\]

Le régime \(\rho_i\to0\), nécessaire pour faire disparaître les rapports
locaux, augmente donc le coût directionnel pondéré. Le filament possède
lui-même deux parois de directions \(\pm e_z\) à l'échelle \(s\). Son
amplitude peut être sous le seuil de vitesse, mais la direction normalisée
est insensible à cette amplitude. Pour un critère imposé seulement sur une
région de grande vorticité, il faut vérifier séparément si \(a_f/s\)
franchit le seuil; aucune conclusion automatique n'est revendiquée.

## 7. Passe contradictoire

1. **Mesure de bord du cutoff.** Il n'y en a pas : le positif-part est
   continu et nul sur la frontière. Une indicatrice seule aurait créé un
   défaut.
2. **Filament sous le seuil.** Il disparaît du superniveau, mais son curl
   subsiste. Les rampes témoins sont disjointes du filament, excluant toute
   cancellation dans (36.23).
3. **Filament au-dessus du seuil.** Il fusionne les composantes, mais est
   alors compté dans \(\mu_U\), la bande coaire et \(\mu_W\).
4. **Boule coupant une goutte.** Une boule tangente peut isoler un plateau
   sans raccord. Le théorème exige une boule contenant
   \(\Omega_\alpha\), pas toutes les coupures.
5. **Direction après signe.** (36.39) donne exactement \(\sigma W\).
6. **Pression et dynamique.** Le support connecté n'implique rien sur la
   pression non locale ni sur une évolution. Le champ lisse est seulement
   une donnée initiale divergence-free de finite énergie.

## 8. Test Python standard library

Le script vérifie rationnellement le facteur \(648\), la loi
\(m^{-1/3}\), les deux normalisations, (36.36), les coûts du filament et
des familles hétérogènes. Les racines affichées sont les seules opérations
flottantes. Aucune graine, aucune dépendance.

~~~python
from fractions import Fraction as Q


def weak_cube(amplitudes, volumes, p):
    # ||f||_(p,infinity)^3 for a disjoint step distribution.
    order = sorted(range(len(amplitudes)),
                   key=lambda i: amplitudes[i], reverse=True)
    volume = Q(0)
    best = Q(0)
    for i in order:
        volume += volumes[i]
        if p == 3:
            candidate = amplitudes[i] ** 3 * volume
        elif p == Q(3, 2):
            candidate = amplitudes[i] ** 3 * volume ** 2
        else:
            raise ValueError(p)
        best = max(best, candidate)
    return best


assert Q(648) == Q(36) * Q(18)
assert Q(36) == Q(6) * Q(6)
assert Q(18) == Q(3) * Q(6)

checks = 0
R = Q(1)
for beta in (1, 2, 3, 4):
    for m in range(1, 41):
        rho = Q(1, m ** beta)
        volume = R * rho ** 2
        A = Q(1)
        ku3 = A ** 3 * (m * volume)
        kw3 = (A / rho) ** 3 * (m * volume) ** 2
        ratio3 = ku3 / kw3
        assert ratio3 == rho / (m * R)
        assert ratio3 * m == rho / R
        kw3_if_ku_one = m * R / rho
        ku3_if_kw_one = rho / (m * R)
        assert kw3_if_ku_one * ku3_if_kw_one == 1
        checks += 1

# Heterogeneous levels: exact discrete distributions.
for n in range(2, 42):
    amplitudes = [Q(1, 2 ** (i % 7)) for i in range(n)]
    radii = [Q(1, (i + 2) ** (1 + i % 3)) for i in range(n)]
    volumes = [R * r ** 2 for r in radii]
    ku3_global = weak_cube(amplitudes, volumes, 3)
    vort_amp = [amplitudes[i] / radii[i] for i in range(n)]
    kw3_global = weak_cube(vort_amp, volumes, Q(3, 2))
    assert ku3_global / kw3_global <= max(radii) / R

    for t in sorted(set(amplitudes), reverse=True):
        selected = [i for i, a in enumerate(amplitudes) if a >= t]
        V = sum((volumes[i] for i in selected), Q(0))
        rho_star = max(radii[i] for i in selected)
        ku3_at_t = t ** 3 * V
        kw3_witness = (t / rho_star) ** 3 * V ** 2
        assert ku3_at_t / kw3_witness == rho_star ** 3 / V
        assert rho_star ** 3 / V <= rho_star / R
        checks += 1

# Filament scaling, s=rho/16 and L=mD.
D = Q(4)
for m in range(1, 41):
    rho = Q(1, m + 1)
    s = rho / 16
    L = m * D * R
    A = Q(1)
    af = A * rho / 16
    kuf3 = af ** 3 * R * s * L
    kwf3 = (af / s) ** 3 * (R * s * L) ** 2
    assert kuf3 / kwf3 == s ** 2 / (R * L)
    assert af < A / 8
    checks += 1

print("exact checks =", checks)
print("factor =", Q(36) * Q(18))
for m in (1, 8, 64, 512):
    rho = Q(1, m)
    ratio3 = rho / m
    print("m=%3d rho=%s (Ku/Kw)^3=%s Ku/Kw=%.12e" %
          (m, rho, ratio3, float(ratio3) ** (1.0 / 3.0)))
print("exact residual = 0")
~~~

## 9. Décision et prochain falsificateur

**ABANDONNER** les gouttes axialement séparées, identiques ou hétérogènes,
reliées sous seuil par un filament à section fixe, comme moyen de conserver
un rapport global non nul tout en détruisant les rapports des boules
contenant une composante.

**CONSERVER** la troncature (36.37) : elle ferme le trou « une cellule
connexe mais plusieurs composantes actives », au prix explicite \(648\),
sans curl de cutoff singulier.

Le prochain test réellement différent doit supprimer l'hypothèse de
diamètre contrôlé : composantes cuspidales ou branchées dont aucune boule
\(C\mathcal R\) ne contient le superniveau tronqué, avec contrôle simultané
de la coaire et du coût de recouvrement.
