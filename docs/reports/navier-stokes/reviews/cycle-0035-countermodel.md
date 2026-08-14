# Cycle 0035 — Contre-modèle géométrique : longue queue axiale d'une cellule pure-swirl

Date : 2026-08-14
Statut : calcul exact sur un squelette lipschitzien, puis stabilité quantitative par lissage ; aucune assertion de dynamique Navier–Stokes
Portée : une cellule à section radiale fixe et queue axiale monotone, puis union de cellules disjointes ; les chevauchements et les sections variables sont exclus

## Décision falsifiable

La fuite laissée ouverte au cycle 0034 n'est **pas réalisée** par une longue queue axiale monotone à section fixe. Le volume de la boîte support peut satisfaire

\[
\frac{|Q|}{v_{\rm coeur}}\simeq \frac{L}{R}\longrightarrow\infty,
\]

mais ce quotient ne mesure pas le volume vu par la fonction de distribution. À chaque demi-niveau axial, il existe un sous-halo dont le volume est comparable au superniveau correspondant de \(U\). Deux coûts complémentaires y apparaissent :

* si la chute axiale est rapide, \(W_r\) est grand ;
* si elle est lente, le superniveau de \(U\) est réellement long et le raccord radial \(W_z\) est grand sur toute cette longueur.

Plus précisément, sur un slab où l'amplitude axiale passe de \(a\) à \(a/2\) sur une longueur \(d\), les témoins explicites ci-dessous donnent, à constantes absolues près,

\[
\begin{aligned}
K_U(d,a)&\asymp AaR\left(\frac dR\right)^{1/3},\\
K_{W_z}(d,a)&\gtrsim AaR\left(\frac dR\right)^{2/3},\\
K_{W_r}(d,a)&\gtrsim AaR\left(\frac Rd\right)^{1/3},
\end{aligned}
\tag{35.1}
\]

où \(K_U=\|U\|_{L^{3,\infty}}\) et \(K_W=\|W\|_{L^{3/2,\infty}}\). Par conséquent,

\[
K_W\gtrsim AaR\max\left\{(d/R)^{2/3},(R/d)^{1/3}\right\}\gtrsim AaR.
\tag{35.2}
\]

L'optimum du faux contre-profil est \(d\simeq R\), pas \(d\gg R\). Une queue extrêmement longue ne peut être invisible qu'à amplitude extrêmement basse ; elle ne modifie alors pas le seuil qui sélectionne le coeur. Si elle reste visible à un seuil, son propre superniveau fournit le sous-halo contrôlé.

Ce résultat est négatif pour le contre-modèle, mais positif pour la stratégie de sélection BV : dans cette classe, il faut remplacer la boîte support arbitraire \(Q_j\) par un halo sélectionné par amplitude \(Q^*_{j,k}\).

## 1. Géométrie, équation cinématique et nature de l'objet

On emploie les coordonnées cylindriques \((r,\theta,z)\), avec une échelle géométrique \(R>0\). Le champ est

\[
U(r,\theta,z)=\frac{R}{r}F(r,z)e_\theta,
\qquad
F(r,z)=A H\!\left(\frac{r-R}{R}\right)\chi(z),
\tag{35.3}
\]

où \(A>0\), \(H\) est compactement supportée dans \((-1/2,1/2)\), et \(\chi\) est une bosse axiale compacte, paire et décroissante sur \([0,+\infty)\). Le support radial est donc inclus dans \(R/2<r<3R/2\), loin de l'axe.

Le champ est exactement divergence-free :

\[
\nabla\cdot U=\frac1r\partial_\theta U_\theta=0.
\]

Son rotationnel est

\[
W=\nabla\times U
=-\frac{R}{r}\partial_zF\,e_r
+\frac{R}{r}\partial_rF\,e_z,
\tag{35.4}
\]

donc

\[
W_r=-\frac{AR}{r}H\chi',
\qquad
W_z=\frac{A}{r}H'\chi.
\tag{35.5}
\]

Le facteur \(R/r\) annule exactement le terme de courbure \(U_\theta/r\). C'est la raison de ce choix, et non une approximation de tore plat.

**Type de résultat.** (35.3) est une donnée initiale lisse et compacte après le lissage de la section 8. Elle est admissible comme donnée classique de Navier–Stokes incompressible non forcé sur \(\mathbb R^3\), mais aucun champ dépendant du temps n'est construit ici. Les conclusions portent seulement sur une obstruction géométrique à une inégalité de sélection ; elles ne démontrent ni blow-up ni régularité globale.

### Échelle

Sous la remise à l'échelle Navier–Stokes

\[
U_\lambda(x)=\lambda U(\lambda x),
\qquad W_\lambda(x)=\lambda^2W(\lambda x),
\]

les quantités \(\|U\|_{L^{3,\infty}}\) et \(\|W\|_{L^{3/2,\infty}}\) sont invariantes. Dans (35.3), \([A]=L/T\), \([R]=L\), et les deux quasi-normes ont la même dimension \(L^2/T\), d'où le facteur commun \(AR\) dans (35.1).

## 2. Squelette explicite et queue dyadique

Les calculs fermés sont faits sur le chapeau radial lipschitzien

\[
H(x)=
\begin{cases}
1,&|x|\le1/4,\\
2-4|x|,&1/4<|x|<1/2,\\
0,&|x|\ge1/2.
\end{cases}
\tag{35.6}
\]

Il vérifie exactement

\[
\int H=\frac34,
\quad \int H^2=\frac23,
\quad \int |H'|=2,
\quad \int |H'|^2=8.
\tag{35.7}
\]

Le coeur axial est \(|z|\le R/2\), où \(\chi=1\). Sur chaque côté, pour \(k=0,\ldots,m-1\), \(\chi\) descend linéairement de

\[
a_k=2^{-k}\quad\hbox{à}\quad a_k/2
\]

sur une longueur \(d_k\). La dernière tranche descend de \(a_m=2^{-m}\) à zéro sur \(d_m\). La queue est paire. Sa longueur support totale est

\[
L_{\rm ax}=R+2\sum_{k=0}^{m}d_k.
\tag{35.8}
\]

La famille adverse à un paramètre est

\[
d_k=R,2^{\alpha k},\qquad \alpha>0.
\tag{35.9}
\]

Ainsi \(L_{\rm ax}/R\asymp2^{\alpha m}\to\infty\). Le coeur plateau garde cependant le volume exact

\[
v_{\rm coeur}=\pi R^3
\tag{35.10}
\]

sur la sous-région \(3R/4\le r\le5R/4\), \(|z|\le R/2\). Une boîte englobante a volume \(\asymp R^2L_{\rm ax}\), donc le quotient demandé diverge.

## 3. Fonctions de distribution complètes

Pour un champ scalaire ou vectoriel \(G\), on note

\[
\mu_G(\lambda)=|\{x\in\mathbb R^3:|G(x)|>\lambda\}|.
\]

Les formules suivantes décrivent le champ complet, pas seulement les exposants d'échelle.

### 3.1 Distribution axiale

Posons \(D_\chi(t)=|\{z:\chi(z)>t\}|\). Pour \(0<t<1\),

\[
D_\chi(t)=R
+2\sum_{k=0}^{m-1}\Phi_k(t)
+2\Phi_m^{\rm fin}(t),
\tag{35.11}
\]

avec

\[
\Phi_k(t)=
\begin{cases}
d_k,&0<t<a_k/2,\\
2d_k(1-t/a_k),&a_k/2\le t<a_k,\\
0,&t\ge a_k,
\end{cases}
\tag{35.12}
\]

et

\[
\Phi_m^{\rm fin}(t)=
\begin{cases}
d_m(1-t/a_m),&0<t<a_m,\\
0,&t\ge a_m.
\end{cases}
\tag{35.13}
\]

On a \(D_\chi(t)=0\) pour \(t\ge1\) et \(D_\chi(0)=L_{\rm ax}\) au sens de la limite à droite.

### 3.2 Distribution complète de \(U\)

En adoptant la convention \(D_\chi(+\infty)=0\), la formule exacte est

\[
\boxed{
\mu_U(\lambda)
=2\pi\int_{R/2}^{3R/2}
r\,D_\chi\!\left(
\frac{\lambda r}{AR,H((r-R)/R)}
\right)dr.}
\tag{35.14}
\]

Cette intégrale est élémentaire morceau par morceau, car \(H\) et \(D_\chi\) sont affines par morceaux. Elle conserve le facteur cylindrique \(r\) et le facteur non localement constant \(R/r\) ; aucune approximation \(r\simeq R\) n'est utilisée dans (35.14).

Sur le plateau radial, on obtient le témoin fermé

\[
\mu_U(\lambda)\ge
\pi R^2 D_\chi\!\left(\frac{5\lambda}{4A}\right),
\tag{35.15}
\]

car \(R/r\ge4/5\). Sur tout le support radial,

\[
\mu_U(\lambda)\le
2\pi R^2D_\chi\!\left(\frac{\lambda}{2A}\right).
\tag{35.16}
\]

### 3.3 Distributions des composantes de \(W\)

Sur les deux rampes radiales, \(|H'|=4\). Par (35.5),

\[
\boxed{
\mu_{W_z}(\lambda)
=2\pi\!\int_{\{R/2<r<3R/2:\,H'\ne0\}}
r\,D_\chi\!\left(\frac{\lambda r}{4A}\right)dr.}
\tag{35.17}
\]

Sur le plateau radial, chaque paire de tranches \(k<m\) a longueur totale \(2d_k\) et \(|\chi'|=a_k/(2d_k)\). La tranche terminale a longueur totale \(2d_m\) et \(|\chi'|=a_m/d_m\). La distribution complète de \(W_r\) est donc

\[
\boxed{
\begin{aligned}
\mu_{W_r}(\lambda)
={}&4\pi\sum_{k=0}^{m-1}d_k
\int_{R/2}^{3R/2}
r\,\mathbf1_{\{ARH(r)a_k/(2rd_k)>\lambda\}}dr\\
&+4\pi d_m
\int_{R/2}^{3R/2}
r\,\mathbf1_{\{ARH(r)a_m/(rd_m)>\lambda\}}dr,
\end{aligned}}
\tag{35.18}
\]

où \(H(r)\) abrège \(H((r-R)/R)\). Le facteur \(4\pi d_k\) contient les deux queues.

Enfin, la distribution du rotationnel vectoriel, et non celle d'une composante, est exactement

\[
\boxed{
\mu_W(\lambda)=2\pi\int_{\mathbb R}\int_{R/2}^{3R/2}
r\,\mathbf1_{\left\{
(ARH\chi'/r)^2+(AH'\chi/r)^2>\lambda^2
\right\}}dr\,dz.}
\tag{35.19}
\]

Les fonctions dans l'indicatrice sont affines par morceaux ; (35.19) est une expression complète et reproductible. Les inégalités \(\mu_W\ge\max(\mu_{W_r},\mu_{W_z})\) suffisent aux tests adverses. Additionner \(\mu_{W_r}\) et \(\mu_{W_z}\) serait incorrect, car les deux composantes coexistent sur les rampes.

## 4. Variation totale et coût des raccords

Les deux fermetures axiales — queue supérieure et queue inférieure — ont chacune variation totale unitaire :

\[
\int_0^\infty|\chi'|dz=1,
\qquad
\int_{-\infty}^0|\chi'|dz=1,
\qquad
\operatorname{TV}(\chi)=2.
\tag{35.20}
\]

Le coût \(L^1\) exact de leur vorticité radiale est indépendant de \(L_{\rm ax}\) :

\[
\begin{aligned}
\|W_r\|_{L^1}
&=2\pi AR\left(\int_{R/2}^{3R/2}H((r-R)/R)dr\right)
\left(\int_{\mathbb R}|\chi'|dz\right)\\
&=3\pi AR^2.
\end{aligned}
\tag{35.21}
\]

Chaque fermeture axiale coûte donc exactement \(3\pi AR^2/2\).

Les deux raccords radiaux, intérieur et extérieur, ont chacun variation unitaire. Leur coût est

\[
\|W_z\|_{L^1}=4\pi AR\int_{\mathbb R}\chi(z)dz,
\tag{35.22}
\]

soit \(2\pi AR\int\chi\) par raccord radial. C'est ici que la longueur effectivement occupée, pondérée par l'amplitude, réapparaît. Plus explicitement,

\[
\int\chi
=R+\frac32\sum_{k=0}^{m-1}a_kd_k+a_md_m.
\tag{35.23}
\]

Les identités quadratiques utiles au contrôle d'une reproduction sont

\[
\int\chi^2
=R+\frac76\sum_{k=0}^{m-1}a_k^2d_k
+\frac23a_m^2d_m,
\tag{35.24}
\]

\[
\int|\chi'|^2
=\frac12\sum_{k=0}^{m-1}\frac{a_k^2}{d_k}
+2\frac{a_m^2}{d_m}.
\tag{35.25}
\]

Par séparation des variables,

\[
\|U\|_2^2
=2\pi A^2R^2
\left(\int_{R/2}^{3R/2}\frac{H^2}{r}dr\right)
\left(\int\chi^2dz\right),
\tag{35.26}
\]

\[
\|W\|_2^2
=2\pi A^2R^2\left[
\left(\int\frac{H^2}{r}dr\right)\int|\chi'|^2
+\frac1{R^2}\left(\int\frac{|H'|^2}{r}dr\right)\int\chi^2
\right].
\tag{35.27}
\]

Ces formules montrent aussi qu'un corridor long à amplitude non négligeable paie en énergie et en enstrophie radiale ; ce constat énergétique n'est toutefois pas utilisé comme preuve au niveau critique.

## 5. Faible-\(L^3\), faible-\(L^{3/2}\) et sous-halo

Pour \(p>0\), posons

\[
K_p(G)=\sup_{\lambda>0}\lambda\mu_G(\lambda)^{1/p}.
\]

Considérons le sous-halo \(Q_k^*\) formé des deux tranches axiales de demi-niveau \(k<m\) et du support radial. Son volume est \(4\pi R^2d_k\). Sur des sous-régions de volume \(2\pi R^2d_k\), les bornes pointwise donnent

\[
\begin{aligned}
K_3(U;Q_k^*)&\ge
\frac25Aa_k(2\pi R^2d_k)^{1/3},\\
K_{3/2}(W_z;Q_k^*)&\ge
\frac43\frac{Aa_k}{R}(2\pi R^2d_k)^{2/3},\\
K_{3/2}(W_r;Q_k^*)&\ge
\frac25\frac{Aa_k}{d_k}(2\pi R^2d_k)^{2/3}.
\end{aligned}
\tag{35.28}
\]

La première ligne utilise \(H=1\), \(R/r\ge4/5\), \(\chi\ge a_k/2\). La deuxième utilise les rampes, \(|H'|=4\), \(r\le3R/2\), \(\chi\ge a_k/2\). La troisième utilise le plateau radial et \(|\chi'|=a_k/(2d_k)\).

Le même niveau satisfait aussi une borne supérieure

\[
K_3(U;Q_k^*)\le C Aa_k(R^2d_k)^{1/3}.
\tag{35.29}
\]

Les exposants de (35.1) sont donc exacts. En posant \(x=d_k/R\), la paire de raccords impose

\[
K_{3/2}(W;Q_k^*)\ge cAa_kR\max(x^{2/3},x^{-1/3}).
\tag{35.30}
\]

Il n'existe aucune valeur de \(x\) qui rende simultanément petits les deux coûts. Si \(x\gg1\), le volume \(R^2d_k\) n'est pas un halo vide : il est inclus, à constante près, dans \(\{U\gtrsim Aa_k\}\). Si \(x\ll1\), la variation axiale est concentrée et \(W_r\) la détecte.

Une version globale plus courte est visible directement dans les distributions. Pour tout \(0<t<1\), le coeur donne \(D_\chi(t)\ge R\). Les rampes radiales donnent donc

\[
K_{3/2}(W_z)
\ge \frac83A\pi^{2/3}R^{1/3}
\sup_{0<t<1}tD_\chi(t)^{2/3},
\tag{35.31}
\]

tandis que (35.16) donne

\[
K_3(U)
\le 2A(2\pi)^{1/3}R^{2/3}
\sup_{0<t<1}tD_\chi(t)^{1/3}.
\tag{35.32}
\]

Au seuil qui maximise le membre de droite de (35.32), \(D_\chi(t)\ge R\). Il s'ensuit, avec une constante explicite non optimisée,

\[
\boxed{K_3(U)\le C_0K_{3/2}(W_z)\le C_0K_{3/2}(W),}
\tag{35.33}
\]

uniformément en \(m\), \(L_{\rm ax}\), \(A\) et \(R\), pour cette famille à section fixe. Cette implication utilise la présence obligatoire des deux rampes radiales pendant toute la queue. Elle ne vaut pas encore pour une section radiale qui s'élargit ou se fragmente avec \(z\).

### Famille géométrique \(d_k=R2^{\alpha k}\)

Les contributions caractéristiques du niveau \(k\) valent

\[
\begin{aligned}
K_{U,k}&\asymp AR\,2^{(-1+\alpha/3)k},\\
K_{W_z,k}&\gtrsim AR\,2^{(-1+2\alpha/3)k},\\
K_{W_r,k}&\gtrsim AR\,2^{(-1-\alpha/3)k}.
\end{aligned}
\tag{35.34}
\]

Trois régimes réfutent les réglages possibles :

1. \(0<\alpha\le3/2\) : la queue peut devenir arbitrairement longue, mais \(K_{W_z}\) reste uniforme et les niveaux de \(U\) décroissent au moins comme \(2^{-k/2}\). Le coeur ou les premiers halos dominent.
2. \(3/2<\alpha\le3\) : les niveaux de \(U\) ne croissent pas, tandis que \(K_{W_z}\) diverge avec \(m\).
3. \(\alpha>3\) : la queue fait croître \(K_U\), mais \(K_{W_z}\) croît plus vite ; le ratio critique se dégrade.

Ainsi aucun \(\alpha>0\) ne réalise une masse faible-\(L^3\) cachée dans une boîte longue à coût faible-\(L^{3/2}\) borné.

## 6. Signes, amplitudes échelonnées et plusieurs cellules

Pour des cellules disjointes

\[
U=\sum_j\sigma_jU_j,
\qquad \sigma_j\in\{-1,+1\},
\qquad A_j>0,
\]

les fonctions de distribution s'additionnent exactement :

\[
\mu_U(\lambda)=\sum_j\mu_{U_j}(\lambda),
\qquad
\mu_W(\lambda)=\sum_j\mu_{W_j}(\lambda).
\tag{35.35}
\]

Les signes n'ont donc aucun effet. Les amplitudes échelonnées ne font que déplacer les seuils \(\lambda\mapsto\lambda/A_j\). Pour un seuil global \(\lambda\), on sélectionne dans la cellule \(j\) le premier niveau \(k\) tel que \(A_ja_k\simeq\lambda\), et non sa boîte support complète. Le volume de \(Q^*_{j,k}\) est alors comparable à la contribution réelle de cette cellule à \(\mu_U(\lambda)\).

Ce mécanisme ferme la fuite \(|Q_j|/v_{\rm coeur,j}\to\infty\) **pour la famille étudiée**. Il ne prouve pas encore le lemme abstrait de sélection pour toutes les cellules pure-swirl : une superposition spatiale, une section dépendant de \(z\), ou un arrangement multi-échelle non monotone peut invalider la partition simple (35.35).

## 7. Passe contradictoire indépendante

### Attaque A — prendre \(d_k\gg R\) pour diluer \(\chi'\)

Succès local : \(W_r\) baisse comme \(d_k^{-1/3}\) dans la quasi-norme critique.
Échec global : \(W_z\) occupe un volume \(\asymp R^2d_k\) à amplitude \(\asymp Aa_k/R\), donc croît comme \(d_k^{2/3}\). Le slab long est aussi un superniveau long de \(U\), pas une boîte vide.

### Attaque B — rendre la queue très basse mais immensément longue

Pour \(a_k=2^{-k}\) et \(d_k=R2^{\alpha k}\), une queue de longueur exponentielle est compatible avec un \(K_W\) uniforme seulement lorsque \(\alpha\le3/2\). Dans ce régime sa contribution faible-\(L^3\) décroît. Dès qu'elle devient capable de dominer \(K_U\), \(W_z\) a déjà divergé.

### Attaque C — changer les signes et les amplitudes entre cellules

Sur des supports disjoints, les signes disparaissent des distributions. Une amplitude \(A_j\) multiplie à la fois \(U_j\) et \(W_j\). Elle ne change donc pas le bilan de niveau. La possible cancellation entre cellules qui se chevauchent est volontairement hors cycle.

### Attaque D — confondre \(\|W_r\|_1\) uniforme avec un contrôle faible-\(L^{3/2}\)

(35.21) seule ne suffit pas : une masse \(L^1\) peut être étalée et avoir une faible-\(L^{3/2}\) arbitrairement petite. Le raisonnement valide utilise le couple local (35.28), ou directement la distribution de \(W_z\) dans (35.17). Le résultat ne repose donc pas sur cette confusion.

### Attaque E — supprimer les rampes radiales le long de la queue

Cela sort de la famille séparable \(F=AH\chi\). Une queue dont la largeur radiale varie pourrait échanger le coût \(W_z\) contre un volume transversal croissant, des gradients obliques ou de la courbure. C'est le contre-profil restant le plus informatif. (35.33) ne doit pas être extrapolée à cette classe sans preuve de coaire anisotrope.

## 8. Passage à une famille \(C_c^\infty\)

Le squelette (35.6), (35.11) est seulement lipschitzien. Pour \(0<\varepsilon<10^{-2}\), on remplace chaque rampe par un raccord monotone \(C^\infty\) dans une couche d'épaisseur relative \(\varepsilon\), sans modifier les plateaux centraux. On obtient \(H_\varepsilon,\chi_\varepsilon\in C_c^\infty\) tels que :

\[
\operatorname{TV}(H_\varepsilon)=2,
\qquad
\operatorname{TV}(\chi_\varepsilon)=2,
\tag{35.36}
\]

et les régions témoins de (35.28) perdent au plus une proportion \(C\varepsilon\) de leur volume. Les trois bornes y restent valides avec constantes multipliées par \(1-C\varepsilon\). Les fonctions de distribution convergent aux points de continuité quand \(\varepsilon\downarrow0\). En particulier, les conclusions uniformes en \(L_{\rm ax}\) ne sont pas un artefact des coins du squelette.

La famille lisse falsifiable finale est donc

\[
U_{m,\alpha,\varepsilon}
=\frac{R}{r}A H_\varepsilon((r-R)/R)
\chi_{m,\alpha,\varepsilon}(z)e_\theta.
\tag{35.37}
\]

Une réfutation numérique de ce rapport consisterait à trouver, pour \(\varepsilon\to0\), \(m\to\infty\), un rapport

\[
\frac{\|U_{m,\alpha,\varepsilon}\|_{L^{3,\infty}}}
{\|\nabla\times U_{m,\alpha,\varepsilon}\|_{L^{3/2,\infty}}}
\longrightarrow\infty.
\tag{35.38}
\]

Les bornes analytiques ci-dessus excluent ce comportement pour toute suite à section radiale fixe.

## 9. Test Python standard library embarqué

Le script contrôle : les identités axiales, les deux coûts \(L^1\), la longueur support, les fonctions de distribution axiales et les trois régimes de (35.34). Il emploie `Fraction` pour les identités rationnelles et des flottants seulement pour les quasi-normes exploratoires. Il ne certifie pas un calcul PDE.

Commande de reproduction : copier le bloc dans un fichier temporaire puis exécuter `python fichier.py`.

```python
from fractions import Fraction
from math import pi


def dyadic_tail(alpha, m):
    # Dimensionless A=R=1. Levels 0,...,m-1 are half-drops;
    # the terminal level m drops from 2^-m to zero.
    a = [2.0 ** (-k) for k in range(m + 1)]
    d = [2.0 ** (alpha * k) for k in range(m + 1)]
    length = 1.0 + 2.0 * sum(d)
    i1 = 1.0 + 1.5 * sum(a[k] * d[k] for k in range(m)) \
         + a[m] * d[m]
    i2 = 1.0 + (7.0 / 6.0) * sum(a[k] ** 2 * d[k] for k in range(m)) \
         + (2.0 / 3.0) * a[m] ** 2 * d[m]
    id2 = 0.5 * sum(a[k] ** 2 / d[k] for k in range(m)) \
          + 2.0 * a[m] ** 2 / d[m]
    return a, d, length, i1, i2, id2


def D_chi(t, alpha, m):
    if t >= 1.0:
        return 0.0
    a, d, *_ = dyadic_tail(alpha, m)
    out = 1.0                         # core length R=1
    for k in range(m):
        if t < a[k] / 2.0:
            phi = d[k]
        elif t < a[k]:
            phi = 2.0 * d[k] * (1.0 - t / a[k])
        else:
            phi = 0.0
        out += 2.0 * phi              # top and bottom tails
    if t < a[m]:
        out += 2.0 * d[m] * (1.0 - t / a[m])
    return out


def proxy_norms(alpha, m):
    # Rigorous lower witnesses from the radial plateau/ramps,
    # evaluated on a dense deterministic threshold set.
    thresholds = {2.0 ** (-q / 32.0) for q in range(0, 32 * (m + 2) + 1)}
    thresholds.update(2.0 ** (-k) for k in range(m + 1))
    thresholds.update(2.0 ** (-k - 1) for k in range(m))
    ku = 0.0
    kwz = 0.0
    for t in thresholds:
        D = D_chi(t, alpha, m)
        ku = max(ku, (4.0 / 5.0) * t * (pi * D) ** (1.0 / 3.0))
        kwz = max(kwz, (8.0 / 3.0) * t * (pi * D) ** (2.0 / 3.0))

    a, d, *_ = dyadic_tail(alpha, m)
    kwr = 0.0
    for k in range(m):
        amplitude = (2.0 / 5.0) * a[k] / d[k]
        volume = 2.0 * pi * d[k]
        kwr = max(kwr, amplitude * volume ** (2.0 / 3.0))
    amplitude = (4.0 / 5.0) * a[m] / d[m]
    volume = 2.0 * pi * d[m]
    kwr = max(kwr, amplitude * volume ** (2.0 / 3.0))
    return ku, kwz, kwr


# Exact rational bookkeeping for arbitrary rational d_k.
m_exact = 12
a_q = [Fraction(1, 2 ** k) for k in range(m_exact + 1)]
d_q = [Fraction(2 ** k, 1) for k in range(m_exact + 1)]  # alpha=1
tv_one_side = sum(a_q[k] / 2 for k in range(m_exact)) + a_q[m_exact]
tv_both = 2 * tv_one_side
assert tv_one_side == 1
assert tv_both == 2

# Closed integrals (alpha=1) agree with their defining sums exactly.
i1_q = Fraction(1) + Fraction(3, 2) * sum(
    (a_q[k] * d_q[k] for k in range(m_exact)), Fraction(0)
) + a_q[m_exact] * d_q[m_exact]
i2_q = Fraction(1) + Fraction(7, 6) * sum(
    (a_q[k] ** 2 * d_q[k] for k in range(m_exact)), Fraction(0)
) + Fraction(2, 3) * a_q[m_exact] ** 2 * d_q[m_exact]
assert i1_q == Fraction(3 * m_exact + 4, 2)
assert i2_q > 1

# Exact variation costs after dividing by pi*A*R^2 (A=R=1).
l1_wr_over_pi = Fraction(3)            # top + bottom axial closures
assert l1_wr_over_pi / 2 == Fraction(3, 2)

print("exact TV(chi) =", tv_both)
print("exact int chi, alpha=1 =", i1_q)
print("exact int chi^2, alpha=1 =", i2_q)
print("exact ||Wr||_1/pi =", l1_wr_over_pi)

for alpha in (1.0, 1.5, 2.0, 3.0, 4.0):
    previous_length = 0.0
    rows = []
    for m in (4, 8, 12, 16):
        _, _, length, i1, i2, id2 = dyadic_tail(alpha, m)
        ku, kwz, kwr = proxy_norms(alpha, m)
        assert length > previous_length
        assert i1 > 0.0 and i2 > 0.0 and id2 > 0.0
        assert kwz > 0.0 and kwr > 0.0
        # The fixed radial ramps give a uniform distributional control.
        assert ku / kwz < 1.0
        rows.append((m, length, ku, kwz, kwr, ku / max(kwz, kwr)))
        previous_length = length
    print("alpha=", alpha)
    for row in rows:
        print("  m=%2d L/R=%12.4e Ku_lb=%9.3e Kwz_lb=%9.3e "
              "Kwr_lb=%9.3e witness_ratio=%9.3e" % row)

# Direct levelwise dichotomy: min over d occurs near d=R.
worst_residual = 0.0
for q in range(-120, 121):
    x = 2.0 ** (q / 12.0)
    penalty = max(x ** (2.0 / 3.0), x ** (-1.0 / 3.0))
    worst_residual = max(worst_residual, max(0.0, 1.0 - penalty))
assert worst_residual == 0.0
print("floating dichotomy residual =", worst_residual)
```

### Résidu et niveau de certification

* \(\operatorname{TV}(\chi)=2\), \(\|W_r\|_1/(\pi AR^2)=3\) et les identités rationnelles du cas \(\alpha=1\) sont vérifiées exactement par `Fraction` : résidu exact nul.
* La dichotomie \(\max(x^{2/3},x^{-1/3})\ge1\) est une identité analytique ; le balayage flottant ne fait qu'en tester l'implémentation. Résidu flottant attendu : `0.0`.
* Les quasi-normes imprimées sont des témoins inférieurs déterministes, pas des valeurs certifiées de la norme complète.
* Aucune discrétisation spatiale ou temporelle de Navier–Stokes n'est exécutée. Il n'y a ni schéma PDE, ni pas de temps, ni résidu d'équation.

## 10. Verdict et prochain test discriminant

**Verdict : ABANDONNER comme contre-modèle** la queue axiale monotone, séparable et à section fixe. Le ratio \(|Q|/v_{\rm coeur}\to\infty\) est une inflation du support formel, pas une destruction du mécanisme de sélection. Un sous-halo de demi-niveau est contrôlé par la fonction de distribution elle-même, et l'un des deux raccords produit nécessairement le coût critique.

**Résultat réellement acquis :** dans la famille (35.37), la sélection doit être formulée par superniveaux et non par boîtes englobantes. Les formules (35.14)–(35.19) et la borne uniforme (35.33) sont falsifiables indépendamment.

**Trou restant :** le passage à une cellule pure-swirl générale \(F(r,z)\), dont la largeur radiale et la topologie des superniveaux varient avec \(z\), n'est pas traité. Le prochain contre-test à meilleure valeur informationnelle est un corridor en trompette : amplitude \(a(z)\), largeur radiale \(b(z)\), aire de superniveau conservée, avec optimisation simultanée de \(\partial_rF\) et \(\partial_zF\). Il faut tester si une inégalité coaire anisotrope locale remplace (35.33) ou si la variation de section fournit enfin un vrai échappement.
