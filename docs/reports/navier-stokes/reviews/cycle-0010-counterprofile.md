# Cycle 0010 — audit CAP et contre-profil de désingularisation

Date de l'audit : 2026-08-14.

## Verdict court

Le dépôt primaire de Hou–Wang–Yang contient bien une chaîne de vérification
Julia par intervalles pour le profil auto-similaire et son mode instable, mais
pas une reproduction légère ni entièrement verrouillée : le `Manifest.toml`
est absent, plusieurs candidats sont fournis comme données binaires
pré-calculées, les notebooks demandent au moins 800 Go de RAM, et aucune
exécution indépendante n'a été faite ici. Le rayon `R=32` du code coupe la
matrice auxiliaire coercive `Q`; ce n'est pas le rayon, seulement choisi
« assez grand », de la localisation de Bogovskii qui produit la donnée
compactement supportée.

Le test adverse léger ci-dessous ferme trois omissions du gate local de cycle
0001 : il donne une famille `C^infinity_c`, exactement divergence-free, issue
d'un cœur homogène de degré `-1`, reconstruit sa pression non locale et fournit
des bornes analytiques. La famille converge fortement en `L^2` vers une donnée
singulière et reste uniformément bornée dans `L^{3,infinity}`, mais deux
régularisations successives restent séparées d'au moins `1.105` en `L^3`.
Elle réfute donc toute stabilité uniforme qui prétendrait convertir ces deux
seuls contrôles en convergence forte critique. Elle ne réfute ni la CAP de
Hou–Wang–Yang ni une stabilité pour des temps `t >= tau > 0`.

## 1. Source primaire inspectée en lecture seule

- Article : Thomas Hou, Yixuan Wang, Changhe Yang,
  [*Nonuniqueness of Leray-Hopf solutions to the unforced incompressible 3D
  Navier-Stokes Equation*, arXiv:2509.25116v2](https://arxiv.org/abs/2509.25116v2).
  La métadonnée arXiv indique une soumission le 29 septembre 2025 et une
  révision v2 le 19 mars 2026. Il s'agit toujours d'une prépublication arXiv
  dans l'état consulté.
- Code :
  [`HouGroup2026/3d-navier-stokes-nonuniqueness`](https://github.com/HouGroup2026/3d-navier-stokes-nonuniqueness),
  branche `main`, commit audité
  [`615ee6f3eca3abad7b5814fe9334bcd80bea0328`](https://github.com/HouGroup2026/3d-navier-stokes-nonuniqueness/tree/615ee6f3eca3abad7b5814fe9334bcd80bea0328),
  daté du 23 mars 2026. Aucun tag ni release n'était publié lors de l'audit.

L'équation de l'article est Navier–Stokes incompressible, non forcé, sur
`R^3`, avec viscosité normalisée à `1` :

\[
 \partial_tu+(u\cdot\nabla)u-\Delta u+\nabla p=0,
 \qquad \nabla\cdot u=0.
\]

Le résultat revendiqué est la non-unicité de solutions de Leray–Hopf
convenables pour une même donnée `L^2`, compactement supportée, lisse hors de
l'origine et appartenant à `L^q` pour tout `q<3`. Ce n'est ni un blow-up à
partir d'une donnée lisse, ni une résolution du problème Clay.

### Ce que certifie le dépôt, et ce qu'il ne calcule pas

La chaîne auditable porte sur deux systèmes stationnaires en variables
auto-similaires : le profil `U` et un eigenpair instable du linéarisé. Elle
certifie des résidus, des enveloppes `L^infinity`, une compensation coercive,
une approximation de rang fini et l'inversion sur son image. La localisation
finale de la donnée est analytique : le papier écrit

\[
 u_{in}=u_{loc}+w,\qquad u^{cut}=-e^{t\Delta}w,
\]

avec une correction de Bogovskii qui assure `div u_loc=0`. Cette étape n'est
pas une simulation du dépôt. De même, la coupure près/loin du profil est

\[
 U_{far}=\mathbb P(\widetilde\chi\,\overline U),
 \qquad \widetilde\chi=0\ (|x|\leq1),\quad
 \widetilde\chi=1\ (|x|\geq2),
\]

et la projection de Leray ajoute une correction de pression non locale. Une
multiplication scalaire par une coupure n'est donc pas tenue pour
divergence-free dans l'argument général.

## 2. Paramètres et troncatures réellement présents

Les valeurs suivantes ont été relevées dans les cellules du commit épinglé,
dans les formes des fichiers `.mat` et, lorsqu'indiqué, dans la v2 du papier.
Les sorties enregistrées dans les notebooks n'ont pas été recalculées.

| Objet | Valeur effectivement présente | Rôle et réserve |
| --- | ---: | --- |
| Type certifié | `Interval{Float64}` | Fixé dans `src/NS_Numerics.jl`; la variante `Float64` est commentée. |
| Grille des candidats | `300 x 150` en `(beta,theta)` | Confirmée par `UP.mat` et `up_eig.mat`; `r=tan(beta)` compactifie tout `R^3`. |
| Coupure spectrale du profil | `M_beta=600`, `M_theta=300` | Valeurs déclarées dans la v2; les produits doublent les fréquences. |
| Grilles profil | `8000 x 4000`, `12000 x 6000`, `24000 x 12000` | Résidu, dérivées, puis enveloppes/positivité. |
| Grilles eigenpair | `16000 x 2000`, `12000 x 6000`, `36000 x 18000` | Résidu et bornes de dérivées. |
| Support de `Q` | `R_0=32` | `Q=0` pour `r>=32`; cette coupure auxiliaire n'est pas la localisation de la donnée initiale. |
| Approximation de `Q` | `L=150`, `M=300`, 5 itérations de Fejér | `eta_0=0.19`, `eta_1=0.199`; `Q` compense la partie négative du gradient symétrisé. |
| Norme coercive | `eta_2=0.005` | Coefficient `L^2` dans la norme `E`. |
| Racines de Bessel | seuil `100` | Notebook Python, `rtol=1e-15`, `mpmath` à 50 chiffres; données `Y:96 x 32`, `Z:95 x 31`. |
| Espaces spectraux | dimensions `1257` (pair) et `1260` (impair) | Colonnes de `eig_vec_even/odd`. |
| Rang compact retenu | `19` pour `U`, `24` pour `v` | Le papier coupe à `lambda^Q >= 0.46`; le notebook emploie aussi `thr=0.456`, marge à expliquer lors d'une reproduction. |
| Assemblage radial | `N0=18000`, stencil `k=8` | Quadrature/assemblage de rang fini sur le domaine de rayon 32. |
| Inversions de rang fini | grilles jusqu'à `12000 x 6000` | 19 puis 24 résolutions; les fichiers `phi_*` contiennent chacun des tableaux proches de `300 x 150`. |

Les sorties stockées annoncent notamment : résidu du profil dans
`[6.40737e-7, 6.40861e-7]`, eigenvalue candidate `-0.113142`, résidu de
l'eigenpair dans `[1.65374e-5, 1.86929e-5]`, et
`||lambda_max(Q)||_infinity` proche de `4.49794`. Ce sont des traces de
l'exécution des auteurs, pas une certification indépendante par Millennium
Forge.

### Dépendances et limites de reproduction

- Le README exige Julia `>=1.11`, tandis que les métadonnées des notebooks
  Julia indiquent `1.12.4`; les sorties enregistrées mentionnent 56 threads et
  le README au moins 800 Go de RAM.
- Le [`Project.toml`](https://github.com/HouGroup2026/3d-navier-stokes-nonuniqueness/blob/615ee6f3eca3abad7b5814fe9334bcd80bea0328/Project.toml)
  déclare notamment `IntervalArithmetic`, `Arblib`, `ArbExtras`, `MAT`,
  `SpecialFunctions`, `SymPy` et `PyPlot`, sans section `[compat]`. Le dépôt ne
  contient pas le `Manifest.toml` annoncé dans son schéma de fichiers; le
  README reconnaît ensuite son absence.
- Le calcul des zéros requiert séparément Python, NumPy, SciPy et mpmath. Un
  notebook Mathematica de 136 Ko documente aussi des formules auxiliaires.
- Les 43 solutions d'inversion `phi_even/phi_odd`, le profil, l'eigenpair et
  d'autres candidats sont livrés comme binaires `.mat`. Le notebook de rang
  fini engendre `data/rhs.mat` pour les deux notebooks suivants, mais la
  génération FEM amont des candidats binaires n'est pas fournie comme chaîne
  exécutable complète. Aucun hash publié ne lie ces binaires au papier.
- Aucun workflow CI, test automatisé global, release immuable ou licence
  racine n'apparaît dans l'arbre audité. Ces lacunes concernent la
  reproductibilité indépendante; elles ne réfutent pas les inégalités de la
  preuve.

Conclusion opérationnelle : ne pas lancer la CAP sur une machine ordinaire.
Une reproduction sérieuse doit d'abord figer Julia et toutes les dépendances,
hasher les `.mat`, expliquer `0.456` versus `0.46`, puis fractionner les
enveloppes pour déterminer le vrai pic mémoire.

## 3. État du gate local de désingularisation

L'artefact
`experiments/navier-stokes/desingularization-gate/desingularization_gate.py`
(SHA-256
`70a7b82de2f93117e525e4ceb4e85d2282e28dd508047cc2f81fbbce18482b49`)
vérifie exactement les intégrales radiales d'un champ supposé égal à
`r^-1 A(theta)` sur `epsilon<=r<=1`. Il établit correctement

\[
 \|u_\epsilon\|_q^q=C_q\int_\epsilon^1r^{2-q}\,dr,
 \qquad
 \|\nabla u_\epsilon\|_2^2=C_{grad}(\epsilon^{-1}-1).
\]

Il ne construit toutefois ni `A`, ni une coupure globale, ni une correction
de divergence, ni la pression. Il ne teste aucune évolution. Le contre-profil
suivant rend ces quatre points explicites tout en conservant le même mécanisme
radial.

## 4. Contre-profil lisse, compact et exactement divergence-free

Fixons `a=e_3`, `r=|x|` et

\[
 U(x)=\frac{a\times x}{|x|^2}
     =\frac{(-x_2,x_1,0)}{r^2},\qquad x\ne0.
\]

Ce champ est homogène de degré `-1`, tangentiel aux sphères, et

\[
 \nabla\cdot U=0,\qquad U\cdot e_r=0,
 \qquad |U|=\frac{\sin\theta}{r},
 \qquad |\nabla U|^2=\frac{2}{r^4}.
\]

Pour obtenir une coupure `C^infinity`, posons

\[
 b(s)=\begin{cases}e^{-1/s},&s>0,\\0,&s\leq0,\end{cases}
 \qquad H(s)=\frac{b(s)}{b(s)+b(1-s)}.
\]

Alors `H=0` sur `(-infinity,0]`, `H=1` sur `[1,infinity)` et `H` est
croissante. Pour `0<epsilon<=1/8`, définissons

\[
 f_\epsilon(r)=H\!\left(\frac{r-\epsilon}{\epsilon}\right)H(2-r),
 \qquad u_\epsilon(x)=f_\epsilon(|x|)U(x).
\]

On a `u_epsilon in C_c^infinity(R^3)`, `u_epsilon=U` sur
`2epsilon<=r<=1` et `supp u_epsilon` inclus dans `epsilon<r<2`. Surtout,

\[
 \nabla\cdot u_\epsilon
 =f_\epsilon\nabla\cdot U+f_\epsilon'(r)e_r\cdot U=0
\]

ponctuellement, donc aussi distributionnellement. Aucun Bogovskii et aucune
projection discrète ne sont requis pour cette géométrie particulière. Cela
ne se généralise pas à un profil `A(theta)` ayant une composante radiale.

## 5. Bornes analytiques et échelle

Avec

\[
 C_q=\int_{S^2}|a\times\omega|^q\,d\omega
 =2\pi\int_0^\pi\sin^{q+1}\theta\,d\theta,
\]

on a `C_2=8pi/3`, `C_3=3pi^2/4`, `C_4=32pi/15`. Puisque
`0<=f_epsilon<=1`, les bornes suivantes sont rigoureuses :

\[
 C_3\log\frac1{2\epsilon}
 \leq \|u_\epsilon\|_3^3
 \leq C_3\log\frac2\epsilon,
\]

\[
 C_4\left(\frac1{2\epsilon}-1\right)
 \leq \|u_\epsilon\|_4^4
 \leq C_4\left(\frac1\epsilon-\frac12\right),
\]

et, en n'intégrant que le cœur où la coupure vaut un,

\[
 \|\nabla u_\epsilon\|_2^2
 \geq 8\pi\left(\frac1{2\epsilon}-1\right).
\]

Pour tout `q<3`, si `u_0(x)=H(2-r)U(x)`, alors

\[
 \|u_\epsilon-u_0\|_q^q
 \leq \frac{C_q}{3-q}(2\epsilon)^{3-q}.
\]

En particulier, `u_epsilon -> u_0` fortement dans `L^2` avec

\[
 \|u_\epsilon-u_0\|_2\leq\sqrt{2C_2\epsilon}.
\]

La norme faible critique reste uniformément bornée. En effet,
`|u_epsilon(x)|<=r^-1 1_{r<2}`, donc, pour la quasi-norme de distribution,

\[
 \|u_\epsilon\|_{L^{3,\infty}}
 \leq \left(\frac{4\pi}{3}\right)^{1/3}
\]

indépendamment de `epsilon`. Sous l'échelle Navier–Stokes
`u_lambda(x)=lambda u(lambda x)`, `L^3` et `L^{3,infinity}` sont invariantes,
tandis que `||nabla u_lambda||_2=lambda^{1/2}||nabla u||_2`. Les divergences
logarithmique `L^3` et `epsilon^-1/2` de `H^1` sont donc exactement placées à
la porte critique/supercritique attendue.

## 6. Pression non locale

Le champ ci-dessus est une donnée, pas une solution stationnaire de
Navier–Stokes. Si l'on évalue le terme non linéaire, la pression compatible est
reconstruite sur tout `R^3` par

\[
 p_\epsilon=R_iR_j(u_{\epsilon,i}u_{\epsilon,j}),
 \qquad
 -\Delta p_\epsilon=\partial_i\partial_j
 (u_{\epsilon,i}u_{\epsilon,j}),
\]

avec la normalisation `p_epsilon in L^2`. Par Plancherel, le multiplicateur
qui contracte un tenseur avec `(xi/|xi|) tensor (xi/|xi|)` a norme un; ainsi

\[
 \|p_\epsilon\|_2
 \leq\|u_\epsilon\otimes u_\epsilon\|_2
 =\|u_\epsilon\|_4^2
 \leq\left[C_4\left(\epsilon^{-1}-\frac12\right)\right]^{1/2}.
\]

Cette borne est un contrôle supérieur, pas une preuve de divergence de la
pression. Elle montre en revanche qu'une validation PDE ne peut limiter la
pression au support de `u_epsilon`; la coupure de vitesse produit une queue de
pression globale.

## 7. Défaut critique exact et critère de réfutation

Sur l'anneau `2epsilon<=r<=5epsilon/2`, on a `f_epsilon=1` et

\[
 f_{2\epsilon}(r)
 \leq H(1/4)=\frac1{1+e^{8/3}}.
\]

En posant

\[
 \delta=1-H(1/4)=\frac{e^{8/3}}{1+e^{8/3}},
\]

on obtient la séparation indépendante de l'échelle

\[
 \|u_\epsilon-u_{2\epsilon}\|_3^3
 \geq \delta^3 C_3\log\frac54,
 \qquad
 \|u_\epsilon-u_{2\epsilon}\|_3\geq 1.105285\ldots .
\]

En même temps,

\[
 \|u_\epsilon-u_{2\epsilon}\|_2
 \leq\sqrt{4C_2\epsilon}\longrightarrow0,
\]

et les deux suites ont des bornes uniformes en `L^2` et
`L^{3,infinity}`.

Le test réfute donc exactement l'assertion de stabilité uniforme suivante :

> Pour chaque `M`, il existe un module `omega_M(s)->0` tel que, pour tous
> champs lisses compacts divergence-free `v,w` avec
> `||v||_2+||w||_2+||v||_{3,infinity}+||w||_{3,infinity}<=M`, on ait
> `||v-w||_3 <= omega_M(||v-w||_2)`.

La même famille réfute toute estimation de flot qui contiendrait `t=0` et
aurait cette conclusion `L^3` avec des constantes dépendant seulement de `M`.
Un résultat proposé est déclaré **réfuté** dès qu'il implique cette estimation
par spécialisation à `v=u_epsilon`, `w=u_{2epsilon}`.

Ce que le test ne réfute pas : une stabilité en topologie faible, une
estimation pour `t>=tau>0`, une constante dépendant de la norme forte `L^3` ou
`H^1`, ou une stabilité exploitant la forme angulaire particulière du profil
certifié par Hou–Wang–Yang. Il montre seulement que la désingularisation ne
peut être raccordée par « convergence `L^2` + borne faible critique » sans un
nouveau lemme compactifiant.

## 8. Reproduction légère

Le script suivant n'utilise que la bibliothèque standard. Les garanties sont
les identités analytiques ci-dessus; les décimales ne sont qu'un contrôle de
transcription. Il n'y a ni grille, ni pas temporel, ni graine aléatoire.

```powershell
@'
from math import exp, log, pi, sqrt

C2 = 8*pi/3
C3 = 3*pi*pi/4
C4 = 32*pi/15
delta = exp(8/3)/(1+exp(8/3))
gap = (delta**3*C3*log(5/4))**(1/3)

assert gap > 1.105
for k in (4, 8, 12, 16):
    eps = 2.0**(-k)
    l3_lo = C3*log(1/(2*eps))
    l3_hi = C3*log(2/eps)
    h1sq_lo = 8*pi*(1/(2*eps)-1)
    p_l2_hi = sqrt(C4*(1/eps-0.5))
    assert 0 < l3_lo <= l3_hi
    assert h1sq_lo > 0 and p_l2_hi > 0
    print(k, l3_lo, l3_hi, h1sq_lo, p_l2_hi)

print("C2,C3,C4 =", C2, C3, C4)
print("delta =", delta)
print("uniform L3 gap >=", gap)
print("analytic divergence residual = 0")
'@ | python -
```

Sortie de référence observée localement pour les constantes finales :

```text
C2,C3,C4 = 8.377580409572781 7.4022033008170185 6.702064327658225
delta = 0.935030830871336
uniform L3 gap >= 1.1052852665795316
analytic divergence residual = 0
```

## 9. Portée pour le transfert vers Clay

Le papier et son dépôt portent sur la non-unicité de solutions faibles
admissibles à partir d'une donnée singulière `L^2`, pas sur la perte de
régularité d'une solution classique issue d'une donnée lisse. Le passage vers
Clay demanderait de lisser le cœur singulier tout en conservant, uniformément
en `epsilon`, deux branches distinctes au-delà d'un temps positif commun.

Le contre-profil produit ici un résultat négatif précis : la compacité forte
`L^2` et la borne critique faible ne suffisent pas à rendre les
régularisations Cauchy dans l'espace critique fort `L^3`; les bornes `H^1`
divergent au moins comme `epsilon^-1/2`. Toute stratégie de transfert qui
utilise l'une de ces deux inférences est abandonnée. Le verrou restant est un
lemme dynamique réellement nouveau — lissage positif uniforme avec contrôle
des deux branches, ou autre compacité critique — et non une amélioration de la
quadrature de la CAP.

État de la sous-tâche : **CONTINUER** sur ce verrou dynamique; **ABANDONNER**
l'inférence fonctionnelle uniforme réfutée ci-dessus.
