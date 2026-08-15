# Cycle 0042 — revue primaire : localisation solénoïdale mobile et force critique

Date de coupure : **2026-08-15**

Objet : audit des inverses de divergence sur domaines dépendant du temps, des
localisations de pression et des théorèmes de lissage local susceptibles de
s'appliquer à

\[
V(t)=\chi_{R(t)}u(t)-\mathcal B_{R(t)}
       \bigl(\nabla\chi_{R(t)}\!\cdot u(t)\bigr),
\qquad R(t)=c\sqrt{T_*-t}.
\]

La revue distingue systématiquement l'équation de Navier–Stokes non forcée
sur `\mathbb R^3`, l'équation forcée satisfaite par `V`, et les équations
posées dans un **domaine physique mobile**. Ces trois cadres ne sont pas
interchangeables.

## Verdict

1. La correction de Bogovskii est exacte à tout temps `t<T_*`. Sur des
   anneaux homothétiques de rapport fixé, ses constantes **spatiales** sont
   uniformes en `R`; le collapse de `R(t)` n'introduit donc pas à lui seul une
   perte géométrique dans `\mathcal B_R:L^p_0\to W^{1,p}_0`.
2. La dépendance temporelle n'est toutefois pas gratuite. La conjugaison de
   l'opérateur de référence donne un commutateur explicite proportionnel à
   `R'(t)`. Pour la donnée de divergence
   `g_R=\nabla\chi_R\cdot u`, il est de taille typique
   `(|R'|/R)|u|`. Avec `R=c\sqrt{T_*-t}`, on a
   `|R'|/R\asymp R^{-2}`.
3. Après projection de Leray, `V` satisfait une équation de Navier–Stokes
   **forcée**. La force contient la dérivée du cutoff, le commutateur de
   Bogovskii, les termes diffusifs de coque, le défaut quadratique et le
   terme non local `\mathbb P(p\nabla\chi_R)`. Sous une mise à l'échelle Type
   I (`u\sim R^{-1}`, `\nabla u\sim R^{-2}`, `p\sim R^{-2}`), chacun de ces
   termes est d'ordre `R^{-3}` sur une coque de volume `R^3`.
4. C'est exactement l'échelle naturelle d'une force de Navier–Stokes. Pour
   `2/q+3/p=3`, sa norme `L^q_tL^p_x` diverge génériquement comme
   `\int_0 R(t)^{-2}\,dt=\int_0 d\tau/\tau`. Au mieux, le comptage brut donne
   un endpoint faible en temps. Aucun théorème primaire audité ne fournit un
   lissage local au bord de cet endpoint pour la **combinaison structurée**
   ci-dessus.
5. Les articles de lissage local de Jia–Šverák, Kang–Miura–Tsai,
   Barker–Prange et Kwon utilisent des régions ou cutoffs spatiaux fixes et
   l'équation non forcée, ou une force perturbative contrôlée par la solution.
   Ils ne permettent pas d'absorber une force arbitraire de coque à
   `R^{-3}`.
6. Saari–Schwarzacher (2023) est le premier résultat publié directement
   transférable sur la **dérivation temporelle** d'un inverse de divergence
   dans un domaine mobile. Il donne des estimations pondérées par la distance
   au bord, mais ne garantit aucune constante uniforme lors du collapse. Dans
   le cas homothétique présent, la formule de conjugaison ci-dessous est plus
   précise.
7. Breit (2025), seule nouveauté analytique publiée en 2025–2026 trouvée qui
   traite simultanément Navier–Stokes et un bord mobile, suppose notamment une
   vitesse de bord dans `L^3_t`. Or
   `|R'(t)|\asymp(T_*-t)^{-1/2}\notin L^3_t` près de `T_*`. Son résultat
   confirme la localisation exacte du verrou; il ne le franchit pas.
8. La prépublication de Q. S. Zhang construit un blow-up pour une équation
   forcée avec une force dite « critique » au sens du potentiel de chaleur.
   Cette criticité (`3/p+2/q=2`) n'est pas la criticité de la force sous
   l'échelle Clay (`3/p+2/q=3`). Elle interdit néanmoins d'invoquer un principe
   vague selon lequel toute force borderline préserverait automatiquement le
   lissage.

**Premier maillon publié transférable.** Un inverse de divergence peut être
construit, localisé et différentié en temps; sur l'anneau homothétique, la
conjugaison donne même des constantes spatiales uniformes et le commutateur
exact.

**Trou exact.** Il manque une estimation exploitant une annulation de la
**force projetée complète** qui place celle-ci dans une classe de lissage
fortement critique et uniforme jusqu'à `T_*`. Estimer séparément
`\partial_t\chi_R`, `\partial_t\mathcal B_R`, `p\nabla\chi_R` et le défaut
quadratique produit une divergence logarithmique; les théorèmes publiés ne
fournissent ni l'annulation requise ni un endpoint faible-en-temps adapté.

## 1. Cadre exact et lois d'échelle

Le comparateur Clay est l'équation non forcée sur l'espace entier, viscosité
normalisée à un :

\[
\partial_tu-\Delta u+\operatorname{div}(u\otimes u)+\nabla p=0,
\qquad \operatorname{div}u=0,
\qquad (x,t)\in\mathbb R^3\times(0,T_*).
\]

Les calculs formels ci-dessous sont exacts pour une solution lisse sur
`[0,T_*)`. Leur usage pour une solution de Leray–Hopf ou une solution faible
adaptée requiert mollification, convergence du correcteur et justification
des produits de pression. Aucun passage faible n'est affirmé ici.

La remise à l'échelle est

\[
u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),\qquad
p_\lambda(x,t)=\lambda^2p(\lambda x,\lambda^2t),
\qquad F_\lambda(x,t)=\lambda^3F(\lambda x,\lambda^2t).
\]

Ainsi une force est invariante dans `L^q_tL^p_x` lorsque

\[
\frac2q+\frac3p=3. \tag{1}
\]

Cette relation est différente de `2/q+3/p=2`, qui est le seuil de certaines
estimations de potentiel de chaleur pour une force. L'emploi du mot
« critique » doit donc toujours préciser la convention.

On fixe `0<a<b`, un cutoff radial
`\chi\in C_c^\infty(B_b)` égal à un sur `B_a`, puis

\[
\chi_R(x)=\chi(x/R),\qquad
A_R=\{aR<|x|<bR\},\qquad R(t)=c\sqrt{\tau},\quad \tau=T_*-t.
\]

Alors

\[
R'(t)=-\frac{c}{2\sqrt\tau},\qquad
\frac{R'(t)}{R(t)}=-\frac1{2\tau}=-\frac{c^2}{2R(t)^2}. \tag{2}
\]

## 2. Correction solénoïdale sur un anneau homothétique

Soit `\mathcal B_A` un inverse de Bogovskii sur l'anneau de référence
`A=A_1`. Pour une fonction de moyenne nulle sur `A_R`, on définit

\[
(\mathcal B_Rf)(x)
=R\,[\mathcal B_A(f(R\,\cdot))](x/R). \tag{3}
\]

La formule donne

\[
\operatorname{div}\mathcal B_Rf=f,
\qquad
\|\nabla\mathcal B_Rf\|_{L^p(A_R)}
\le C_{A,p}\|f\|_{L^p(A_R)}, \tag{4}
\]

avec `C_{A,p}` indépendant de `R`. Plus généralement, les facteurs de `R`
des normes homogènes se lisent exactement par changement de variables. C'est
la conséquence transférable des théories statiques de Bogovskii sur domaines
lipschitziens/John : la géométrie **normalisée** reste fixe.

Pour

\[
g_R=\nabla\chi_R\cdot u,
\]

la condition de compatibilité est satisfaite : en prolongeant le produit par
zéro hors de la coque,

\[
\int_{A_R}g_R\,dx
=\int_{\mathbb R^3}\operatorname{div}(\chi_Ru)\,dx=0. \tag{5}
\]

On pose

\[
b_R=\mathcal B_Rg_R,
\qquad V=\chi_Ru-b_R. \tag{6}
\]

Alors `\operatorname{div}V=0`; avec le choix usuel du correcteur à trace
nulle, `V=u` sur `B_{aR}` et `V=0` hors `B_{bR}`. Ce constat est spatial et
ne contrôle pas `\partial_tV`.

### 2.1 Dérivée temporelle exacte

Écrivons `y=x/R(t)` et `h(y,t)=f(R(t)y,t)`. À `x` fixé, la dérivation de
(3) donne

\[
\partial_t(\mathcal B_Rf)
=\mathcal B_R(\partial_tf)
+R'\{\mathcal B_Ah+\mathcal B_A(y\cdot\nabla h)
-y\cdot\nabla\mathcal B_Ah\}(x/R). \tag{7}
\]

Le second terme est le commutateur de dilation. Pour
`f=g_R\sim R^{-1}u` sur `A_R`, son échelle brute est

\[
\operatorname{Comm}_t(\mathcal B_R,g_R)
\sim \frac{|R'|}{R}|u|. \tag{8}
\]

Il serait incorrect de remplacer simplement
`\partial_t\mathcal B_Rg_R` par `\mathcal B_R\partial_tg_R`. Il serait
également incorrect de conclure à une perte des constantes **spatiales** de
Bogovskii : la perte vient de la vitesse de la dilatation.

## 3. Équation forcée exacte et pression

Un calcul produit d'abord

\[
\begin{aligned}
&\partial_t(\chi_Ru)-\Delta(\chi_Ru)
+\operatorname{div}(\chi_Ru\otimes u)+\chi_R\nabla p\\
&\quad=G_{\chi,R},
\end{aligned}
\]

où

\[
G_{\chi,R}
=(\partial_t\chi_R-\Delta\chi_R)u
-2(\nabla\chi_R\cdot\nabla)u
+(u\cdot\nabla\chi_R)u. \tag{9}
\]

En utilisant
`-\chi_R\nabla p=-\nabla(\chi_Rp)+p\nabla\chi_R`, puis la projection de
Leray globale `\mathbb P`, on obtient pour `V=\chi_Ru-b_R`

\[
\partial_tV-\Delta V+\mathbb P\operatorname{div}(V\otimes V)=F_R, \tag{10}
\]

avec

\[
\boxed{
F_R=\mathbb P\!\left[
G_{\chi,R}-(\partial_t-\Delta)b_R
+\operatorname{div}(V\otimes V-\chi_Ru\otimes u)
+p\nabla\chi_R
\right].} \tag{11}
\]

La formule (11) est le bon objet à tester. Elle empêche quatre
simplifications abusives :

- `V` ne satisfait pas l'équation non forcée;
- le défaut quadratique ne se réduit pas à un terme linéaire;
- la projection de Leray est non locale;
- le terme de pression de coque ne disparaît pas par multiplication par un
  cutoff.

En effet,

\[
\mathbb P(\chi_R\nabla p)
=-\mathbb P(p\nabla\chi_R). \tag{12}
\]

L'expression projetée est indépendante du choix de jauge `p\mapsto p+c(t)`,
car `\mathbb P(c(t)\nabla\chi_R)=0`. Mais aucune petitesse locale ne découle
de cette invariance. Une expansion locale de pression doit conserver la
partie lointaine/harmonique.

## 4. Test d'échelle adverse

Supposons seulement le comptage Type I sur la coque parabolique :

\[
u\sim R^{-1},\qquad \nabla u\sim R^{-2},\qquad
p\sim R^{-2},\qquad b_R\sim R^{-1}. \tag{13}
\]

Comme `\nabla\chi_R\sim R^{-1}`,
`\Delta\chi_R\sim R^{-2}` et, par (2),
`\partial_t\chi_R\sim |R'|/R\sim R^{-2}`, on obtient :

| Terme | Ordre sur `A_R` |
|---|---:|
| `(\partial_t\chi_R)u` | `R^{-3}` |
| `(\Delta\chi_R)u` | `R^{-3}` |
| `(\nabla\chi_R\cdot\nabla)u` | `R^{-3}` |
| `(u\cdot\nabla\chi_R)u` | `R^{-3}` |
| commutateur temporel de `b_R` | `R^{-3}` |
| `\Delta b_R` | `R^{-3}` |
| `p\nabla\chi_R` | `R^{-3}` |
| défaut quadratique différentié | `R^{-3}` |

La coque ayant un volume comparable à `R^3`, une force sans annulation de
taille `R^{-3}` vérifie

\[
\|F_R(t)\|_{L^p_x}\asymp R(t)^{-3+3/p}. \tag{14}
\]

À l'égalité critique (1), pour `q<\infty`,

\[
\|F_R(t)\|_{L^p_x}^q
\asymp R(t)^{-2}
\asymp (T_*-t)^{-1}, \tag{15}
\]

d'où une divergence logarithmique. Les exemples caractéristiques sont
`L^{5/3}_{t,x}` et `L^2_tL^{3/2}_x`. Le comptage est compatible avec un
endpoint `L^{q,\infty}_tL^p_x`; pour `q=\infty`, l'espace critique est
`L^\infty_tL^1_x`, mais `p=1` est précisément hors du cadre standard de
bornitude forte des opérateurs de Calderón–Zygmund, de Leray et de
Bogovskii.

Ce test ne prouve pas que la force (11) diverge : des annulations entre ses
termes sont possibles. Il prouve la proposition négative utile suivante :
**aucune estimation terme à terme, fondée seulement sur l'échelle Type I, ne
peut livrer une norme forte critique uniforme jusqu'à `T_*`.**

## 5. Audit des sources primaires

### 5.1 Inverses statiques : ce qui est déjà acquis

#### Costabel–McIntosh 2010 — catalogue `NS-SRC-0103`

M. Costabel et A. McIntosh, *On Bogovskiĭ and regularized Poincaré integral
operators for de Rham complexes on Lipschitz domains*, *Mathematische
Zeitschrift* **265** (2010), 297–320, DOI
[`10.1007/s00209-009-0517-8`](https://doi.org/10.1007/s00209-009-0517-8),
[`arXiv:0808.2614`](https://arxiv.org/abs/0808.2614).

L'article construit des opérateurs réguliers préservant le support et gagnant
une dérivée dans les échelles de Sobolev, Besov et Triebel–Lizorkin sur des
domaines lipschitziens. C'est une preuve analytique publiée. Le domaine est
fixe; il n'y a ni équation de Navier–Stokes, ni variable temporelle. Après
dilatation d'un anneau fixe, il justifie (3)–(4), pas (7).

#### Acosta–Durán–Muschietti 2006 — catalogue `NS-SRC-0176`

G. Acosta, R. G. Durán et M. A. Muschietti, *Solutions of the divergence
operator on John domains*, *Advances in Mathematics* **206** (2006),
373–401, DOI
[`10.1016/j.aim.2005.09.004`](https://doi.org/10.1016/j.aim.2005.09.004).

Le résultat donne un inverse de divergence sur les domaines de John, avec
constantes dépendant de la géométrie du domaine. Un anneau de rapport fixé
reste uniformément John sous homothétie. Le résultat ne suit pas la dérivée
de la famille d'opérateurs.

#### Guzmán–Salgado 2021 — catalogue `NS-SRC-0111`

J. Guzmán et A. J. Salgado, *Estimation of the continuity constants for
Bogovskiĭ and regularized Poincaré integral operators*, *Journal of
Mathematical Analysis and Applications* **502** (2021), 125246, DOI
[`10.1016/j.jmaa.2021.125246`](https://doi.org/10.1016/j.jmaa.2021.125246),
[`arXiv:2010.04105`](https://arxiv.org/abs/2010.04105).

Les dépendances en géométrie et rapport d'aspect y sont rendues explicites.
Cela renforce le diagnostic : sur une famille homothétique, le rapport
d'aspect ne change pas. La difficulté de (7) est temporelle, pas une
dégénérescence du rapport d'aspect.

### 5.2 Inverse de divergence dans un domaine mobile

O. Saari et S. Schwarzacher, *Construction of a Right Inverse for the
Divergence in Non-cylindrical Time Dependent Domains*, *Annals of PDE* **9**
(2023), article 8, DOI
[`10.1007/s40818-023-00150-z`](https://doi.org/10.1007/s40818-023-00150-z),
[`arXiv:2107.09573`](https://arxiv.org/abs/2107.09573).

**Cadre.** L'ouvert est un sous-ensemble espace-temps
`\Omega\subset\mathbb R^{1+n}` dont les tranches spatiales connexes
`\Omega_t` ont un bord à régularité Hölder contrôlée. L'opérateur résout
`\operatorname{div}_x\mathcal Bf=f` dans chaque tranche, avec trace nulle et
moyenne nulle de `f`. Il ne s'agit pas d'une solution de Navier–Stokes.

**Conclusion pertinente.** Pour une géométrie de classe
`C^{\alpha,1,\theta}`, `1<p<\infty`, le théorème 1.1 contrôle schématiquement

\[
\|\partial_t^\kappa\mathcal Bf(t)\|_{\dot W^{k+1,p}(\Omega_t)}
\le C
\left(\sum_{\lambda=0}^{\kappa}
\int_{\Omega_t}|\partial_t^\lambda\nabla^kf|^p
d(x,\partial\Omega_t)^{p(\lambda-\kappa)/\alpha}\,dx
\right)^{1/p}. \tag{16}
\]

Le théorème général `C^{\alpha,\beta,\theta}` comporte des pertes analogues,
avec exposant de distance lié à `1/(\alpha\beta)`. La proposition 1.5 traite
aussi `\partial_tf` dans un espace négatif, au prix d'une perte d'intégrabilité.
Les constantes dépendent de la géométrie espace-temps; elles ne sont pas
annoncées uniformes pour une tranche qui s'effondre à un temps terminal.

**Transfert.** L'article établit rigoureusement que répéter à chaque temps un
opérateur statique n'autorise pas à commuter `\partial_t` et `\mathcal B`.
Lorsque les tranches restent uniformément étoilées par rapport à une boule
fixe, un opérateur indépendant du temps peut commuter avec `\partial_t`;
cette hypothèse échoue pour un anneau qui se contracte vers un point. Pour la
famille homothétique `A_{R(t)}`, la conjugaison (3) produit néanmoins la
formule plus précise (7). Les poids de (16) et le facteur `R'/R` de (7)
signalent le même obstacle au temps de collapse.

**Statut catalogue.** Source primaire publiée et absente du catalogue au
début du cycle; nouvel identifiant recommandé : `NS-SRC-0180`.

### 5.3 Pression locale : les composantes qui ne peuvent être omises

#### Wolf 2017

J. Wolf, *On the local pressure of the Navier–Stokes equations and related
systems*, *Advances in Differential Equations* **22** (2017), 305–338, DOI
[`10.57262/ade/1489802453`](https://doi.org/10.57262/ade/1489802453),
[`arXiv:1611.01482`](https://arxiv.org/abs/1611.01482).

Sur un domaine générique `\nabla_q`-régulier, Wolf décompose une distribution
qui s'annule sur les tests solénoïdaux en une pression harmonique locale et
une pression associée à la force. Cette preuve analytique publiée permet de
formuler des solutions locales avec pression sans supposer une pression
globale régulière. Les projections et sous-domaines sont fixes. Elle justifie
la nécessité de suivre la pression harmonique/non locale, mais ne dérive ni
(7) ni (11).

**Statut catalogue.** Source primaire publiée, absente et probante pour le
terme de pression; nouvel identifiant recommandé : `NS-SRC-0181`.

#### Bradshaw–Tsai 2022

Z. Bradshaw et T.-P. Tsai, *On the local pressure expansion for the
Navier–Stokes equations*, *Journal of Mathematical Fluid Mechanics* **24**
(2022), article 3, [`arXiv:2001.11526`](https://arxiv.org/abs/2001.11526).

Dans l'espace entier, les auteurs caractérisent la compatibilité entre une
expansion locale de la pression d'une solution distributionnelle et la
formulation mild. L'expansion sépare contribution proche, contribution
lointaine et jauge harmonique/BMO sur des boules fixes. Elle ne donne aucune
petitesse de `p\nabla\chi_R` sur une coque mobile. Elle montre au contraire
pourquoi la partie lointaine ne peut être supprimée d'une estimation locale.

La source est absente du catalogue et pertinente, mais elle recoupe le rôle
documenté par Wolf et Kwon. Aucun nouvel identifiant prioritaire n'est proposé
dans ce cycle afin de réserver les IDs aux maillons directement utilisés.

#### Kwon 2023

H. Kwon, *The role of the pressure in the regularity theory for the
Navier–Stokes equations*, *Journal of Differential Equations* **357** (2023),
1–31, DOI
[`10.1016/j.jde.2023.01.049`](https://doi.org/10.1016/j.jde.2023.01.049),
[`arXiv:2104.03160`](https://arxiv.org/abs/2104.03160).

Pour Navier–Stokes incompressible non forcé en dimension trois, Kwon utilise
une projection de Leray localisée, de forme
`\mathbb P_\varphi u=-\operatorname{curl}\Delta^{-1}
(\varphi\operatorname{curl}u)`, et écrit localement `u=v+h` avec `h`
harmonique. Le champ `v` satisfait une équation perturbée dont pression et
force solénoïdale sont contrôlées par `u`; cette décomposition permet des
énoncés de régularité locale pour des solutions dissipatives avec pression
distributionnelle. Le cutoff `\varphi` et le domaine borné sont fixes : il
n'y a ni `\partial_t\varphi`, ni support qui s'effondre, ni force générique à
l'endpoint (1).

Kwon fournit le dictionnaire publié le plus proche pour réorganiser la
pression et les champs harmoniques de (11), mais pas l'estimation critique
mobile. Source absente et probante; nouvel identifiant recommandé :
`NS-SRC-0182`.

### 5.4 Lissage local publié : hypothèses exactes

#### Jia–Šverák 2014

H. Jia et V. Šverák, *Local-in-space estimates near initial time for weak
solutions of the Navier–Stokes equations and forward self-similar solutions*,
*Inventiones Mathematicae* **196** (2014), 233–265, DOI
[`10.1007/s00222-013-0468-x`](https://doi.org/10.1007/s00222-013-0468-x),
[`arXiv:1204.0529`](https://arxiv.org/abs/1204.0529).

Équation non forcée sur `\mathbb R^3`, solutions faibles locales/Leray avec
donnée initiale localement régulière et contrôle `L^2_{uloc}`. La conclusion
est un lissage à court temps dans une région spatiale fixe. Le théorème ne
prend pas en entrée une équation forcée par (11), et l'instant lissé est un
instant initial, non un temps terminal avec support contractant.

#### Kang–Miura–Tsai 2021

K. Kang, H. Miura et T.-P. Tsai, *Short Time Regularity of Navier–Stokes
Flows with Locally `L^3` Initial Data and Applications*, *International
Mathematics Research Notices* **2021**(11), 8763–8805, DOI
[`10.1093/imrn/rnz327`](https://doi.org/10.1093/imrn/rnz327),
[`arXiv:1812.10509`](https://arxiv.org/abs/1812.10509).

Équation non forcée en dimension trois et solutions faibles adaptées/locales.
Le lissage part d'une donnée localement `L^3`, avec petitesse critique dans
les formes les plus fortes, sur des cylindres fixes. Le résultat ne couvre
pas une force de coque mobile ayant seulement le comptage (15).

#### Barker–Prange 2020 — catalogue `NS-SRC-0146`

T. Barker et C. Prange, *Localized smoothing for the Navier–Stokes equations
and concentration of critical norms near singularities*, *Archive for
Rational Mechanics and Analysis* **236** (2020), 1487–1541, DOI
[`10.1007/s00205-020-01495-6`](https://doi.org/10.1007/s00205-020-01495-6),
[`arXiv:1812.09115`](https://arxiv.org/abs/1812.09115).

Le théorème concerne l'équation non forcée sur `\mathbb R^3`, une solution
d'énergie locale, une petite donnée `L^3` (ou faible-`L^3` dans l'appendice)
sur une boule fixe et un contrôle global `L^2_{uloc}`. Il conduit à une
concentration nécessaire au rayon parabolique près d'un point singulier Type
I. Comme établi au cycle 0041, ce rayon dépend du contrôle critique; le
théorème ne crée pas un cutoff mobile dans l'équation et n'accepte pas (11)
comme une perturbation arbitraire.

#### Barker 2023 — catalogue `NS-SRC-0154`

T. Barker, *Localized Quantitative Estimates and Potential Blow-Up Rates for
the Navier–Stokes Equations*, *SIAM Journal on Mathematical Analysis* **55**
(2023), 5221–5259, DOI
[`10.1137/22M1527179`](https://doi.org/10.1137/22M1527179).

L'équation est non forcée dans un cylindre fixe `B(0,4)\times(0,T_*)`; la
solution est une solution faible adaptée, lisse avant un éventuel point
singulier terminal. La preuve emploie des troncatures et corrections de
divergence sur des régions fixes. Elle fournit le précédent publié le plus
proche pour la partie **spatiale** de (6), mais aucune estimation de
`\partial_t\mathcal B_{R(t)}` et aucun lissage forcé à l'échelle (15).

#### Albritton–Barker–Prange 2023

D. Albritton, T. Barker et C. Prange, *Localized smoothing and concentration
for the Navier–Stokes equations in the half space*, *Journal of Functional
Analysis* **284** (2023), 109729, DOI
[`10.1016/j.jfa.2022.109729`](https://doi.org/10.1016/j.jfa.2022.109729),
[`arXiv:2112.10705`](https://arxiv.org/abs/2112.10705).

Équation non forcée dans `\mathbb R^3_+`, condition de non-glissement et
solutions d'énergie locale. La pression est séparée en parties de Helmholtz
et harmonique liées au bord; elle possède une non-localité et une singularité
temporelle supplémentaires. Les régions restent fixes. Le résultat renforce
l'avertissement sur la pression mais ne traite pas une frontière artificielle
qui s'effondre dans l'espace entier.

**Conclusion de la pile de lissage.** Ces résultats donnent des mécanismes
conditionnels robustes pour une équation non forcée ou une perturbation
contrôlée, sur géométrie fixe. Aucun ne contient un théorème du type :

\[
F\in L^{q,\infty}_tL^p_x,\quad 2/q+3/p=3
\quad\Longrightarrow\quad
\text{lissage local uniforme}, \tag{17}
\]

encore moins au endpoint `p=1`, et aucun n'exploite automatiquement les
annulations croisées de (11).

### 5.5 Domaine physique dépendant du temps : Breit 2025

D. Breit, *Partial boundary regularity for the Navier–Stokes equations in
time-dependent domains*, *Journal of Differential Equations* **434** (2025),
113299, DOI
[`10.1016/j.jde.2025.113299`](https://doi.org/10.1016/j.jde.2025.113299),
[`arXiv:2305.02602`](https://arxiv.org/abs/2305.02602).

**Équation et domaine.** Breit étudie

\[
\partial_tu+(u\cdot\nabla)u=\Delta u-\nabla\pi+f,
\qquad \operatorname{div}u=0
\]

dans un domaine physique mobile `\Omega_{\eta(t)}`, avec condition de
non-glissement au bord mobile. Le bord est un graphe normal au-dessus d'une
surface de référence lisse et ne dégénère pas.

**Hypothèses.** La théorie de régularité maximale utilisée dans la preuve
suppose notamment, pour certains `p>15/4` et `q_0>2`,

\[
\eta\in C_tW_y^{2-1/p,p},
\qquad \partial_t\eta\in L^3_tW_y^{1,q_0}.
\]

Pour l'énoncé de régularité partielle conditionnel à l'existence, la vitesse
peut être affaiblie à une classe comprenant
`L^3_t(L^3\cap W^{1,1})`. L'article construit des solutions faibles adaptées
au bord, une théorie de Stokes en domaine mobile et montre que l'ensemble
singulier de bord a mesure de Hausdorff parabolique `5/3` nulle. La preuve
utilise un correcteur de Bogovskii dépendant de `\Omega_{\eta(t)}`.

**Échec du transfert.** Pour un bord sphérique de rayon
`R(t)=c\sqrt{T_*-t}`,

\[
|\partial_t\eta|\asymp |R'(t)|\asymp(T_*-t)^{-1/2},
\qquad
\int^{T_*}|R'(t)|^3dt=\infty. \tag{18}
\]

De plus, `A_{R(t)}` s'effondre au temps terminal et n'est pas un domaine
physique non dégénéré avec condition de non-glissement. Le théorème ne
s'applique donc pas. La violation exacte de (18) est informative : l'échelle
parabolique mobile se trouve au-delà de la régularité temporelle publiée.

**Statut catalogue.** Source primaire publiée en 2025, absente et directement
probante; nouvel identifiant recommandé : `NS-SRC-0183`.

### 5.6 Force borderline et blow-up : Zhang 2024, prépublication

Q. S. Zhang, *A blow up solution of the Navier–Stokes equations with a
critical force*, [`arXiv:2411.13896v3`](https://arxiv.org/abs/2411.13896v3),
version 3 du 29 décembre 2024. Statut : **prépublication analytique**, non
traitée ici comme un théorème publié ou accepté.

Avec la convention de signe de l'article,

\[
\Delta v-v\cdot\nabla v-\nabla P-\partial_tv=F,
\qquad \operatorname{div}v=0,
\]

sur un domaine de `\mathbb R^3` contenant l'origine (ou sur l'espace entier),
l'auteur construit des vitesses lisses pour `t<T`, d'énergie finie, qui
deviennent non bornées à `T`. Dans la version sur l'espace entier, la force
principale est comparable à

\[
-\frac{e^{-|x|^2}}{(|x|^2+T-t)
 [1+|\log(|x|^2+T-t)|]},e_1,
\]

et appartient à `L^\infty_tL^{3/2}_x`; la donnée initiale peut être nulle et
l'amplitude arbitrairement petite selon l'énoncé.

Le terme « critique » renvoie dans l'article au seuil du potentiel de chaleur
`3/p+2/q=2`. Sous la remise à l'échelle Navier–Stokes d'une **force**, le seuil
est (1), donc `L^\infty_tL^{3/2}_x` n'est pas invariant. La force de Zhang est
de taille radiale `R^{-2}`, tandis que chaque terme brut de (11) est de taille
`R^{-3}`. La source ne construit ni la structure (11), ni une solution de
l'équation Clay non forcée. Elle réfute seulement toute extrapolation non
quantifiée d'un lissage « pour force critique » d'une convention à l'autre.

**Statut catalogue.** Source primaire absente et très probante comme
contre-garde, mais prépublication; nouvel identifiant recommandé :
`NS-SRC-0184`, avec `publication_status: preprint_v3`. Une affirmation
cataloguant son énoncé peut être `SOURCE_VERIFIED`; aucune dérivation du
présent cycle ne doit recevoir automatiquement `PAPER_PROOF`.

## 6. Veille différentielle 2025–2026

La recherche différentielle a combiné les expressions *time-dependent
Bogovskii*, *moving domain Navier–Stokes regularity*, *moving cutoff local
smoothing*, *local pressure projection*, *critical force Navier–Stokes* et
leurs variantes. Les conclusions vérifiables à la date de coupure sont :

- **2025, analytique publié :** Breit est le résultat nouveau le plus proche.
  Il concerne un bord physique mobile non dégénéré et son hypothèse de vitesse
  `L^3_t` exclut précisément le rayon parabolique contractant.
- **2025–2026, lissage local :** aucun article primaire trouvé ne démontre
  (17) pour la force structurée (11), ni une estimation uniforme de
  `\partial_t\mathcal B_{R(t)}` jusqu'au collapse.
- **2026, calcul numérique en domaine mobile :** des travaux ALE/DG
  pression-robustes et des méthodes unfitted/Ghost-FEM préservent la
  divergence discrète sur des maillages mobiles. Ils concernent la stabilité
  et la convergence de discrétisations de Stokes/Navier–Stokes en domaine
  mobile; ils ne fournissent pas une borne analytique de continuum à
  l'endpoint (15). Ils ne sont donc pas ajoutés au catalogue pour ce lemme.
- Aucune annonce 2025–2026 trouvée ne supprime le terme de pression de coque,
  ne transforme une frontière artificielle mobile en solution non forcée, ou
  ne prouve une annulation universelle de la force complète (11).

Ce résultat de veille est négatif et daté; il ne constitue pas une preuve
d'inexistence d'une publication non indexée. Il fixe néanmoins le différentiel
par rapport au catalogue `NS-SRC-0001`–`NS-SRC-0179` au début du cycle.

## 7. Tableau d'implication vers le comparateur `V`

| Source | Domaine / solution | Maillon transférable | Hypothèse ou conclusion absente |
|---|---|---|---|
| Costabel–McIntosh; Acosta–Durán–Muschietti; Guzmán–Salgado | domaine fixe; problème de divergence | `\mathcal B_R` uniforme spatialement par homothétie | aucune dérivée temporelle |
| Saari–Schwarzacher 2023 | domaine mobile Hölder; problème de divergence | existence et contrôle de `\partial_t\mathcal B` avec poids | pas d'uniformité au collapse; pas de lissage NS |
| Wolf 2017 | domaine fixe; systèmes faibles | pression locale harmonique + pression de force | pas de cutoff mobile |
| Bradshaw–Tsai 2022 | `\mathbb R^3`; solutions distributionnelles/mild | expansion proche/lointaine de pression | pas de petitesse de `p\nabla\chi_R` |
| Kwon 2023 | NS 3D non forcé; solution dissipative | projection localisée, `u=v+h` | cutoff fixe; force liée à `u`, pas endpoint mobile |
| Jia–Šverák; Kang–Miura–Tsai; Barker–Prange | NS 3D non forcé; solutions faibles locales/adaptées | lissage court sous hypothèses locales critiques | pas de force (11), région fixe |
| Barker 2023 | cylindre fixe; solution adaptée lisse avant `T_*` | troncature solénoïdale quantitative fixe | pas de `R'(t)` |
| Breit 2025 | NS dans un domaine physique mobile | correcteur mobile et régularité partielle au bord | `R'\notin L^3_t`; domaine qui ne doit pas s'effondrer |
| Zhang 2024, préprint | NS forcé; solution d'énergie lisse avant blow-up | avertissement sur force borderline | autre criticité; force non issue de (11); pas Clay |

## 8. Tests contradictoires et résidus

### Test A — compatibilité du correcteur

La moyenne nulle (5) tient seulement si `\chi_Ru` a un flux total nul et si
la divergence est traitée sans contribution de frontière à l'infini. Pour
une solution locale dans un domaine borné ou une condition au bord différente,
une correction de flux supplémentaire peut être nécessaire.

**Résidu :** nul pour une solution lisse divergence-free sur `\mathbb R^3`
et un cutoff compact; non certifié pour une solution faible sans passage par
approximation.

### Test B — commutation temporelle

La formule (7) a été recalculée à `x` fixé. Les trois termes de dilation ont
des signes distincts. Omettre le dernier terme
`-y\cdot\nabla\mathcal B_Ah` revient à dériver à `y` fixé et donne une formule
fausse dans les coordonnées physiques.

**Résidu :** commutateur exact `R'\mathcal C_Ah`; sa norme n'est pas petite
pour `R\sim\sqrt\tau`.

### Test C — projection de la pression

L'identité (12) montre que `\mathbb P\nabla(\chi_Rp)=0`, pas que
`\mathbb P(\chi_R\nabla p)=0`. La multiplication et la projection ne
commutent pas.

**Résidu :** `\mathbb P(p\nabla\chi_R)`, support source dans la coque mais
champ projeté non compact et non local.

### Test D — norme critique

Le calcul (15) est indépendant de `p,q` le long de la droite critique (1).
Choisir un autre couple critique fort ne supprime donc pas le logarithme.

**Résidu :** endpoint faible en temps ou annulation structurelle à démontrer;
aucune des sources auditées ne la donne.

### Test E — confusion domaine mobile / cutoff mobile

Dans Breit, le bord transporte une condition physique de non-glissement et la
formulation ALE modifie les opérateurs. Ici, `u` reste une solution sur tout
`\mathbb R^3`; seule sa représentation `V` a un support mobile et reçoit une
force de commutateur.

**Résidu :** aucun lemme de raccord publié entre ces deux formulations dans
la géométrie contractante.

### Test F — transfert au problème Clay

Même si (10) était lissée, il faudrait relier le lissage de `V` à celui de
`u` sur `B_{aR(t)}` jusqu'au point terminal, avec des constantes uniformes.
Comme le rayon intérieur tend vers zéro, une régularité sur chaque temps
strictement antérieur ne suffit pas.

**Résidu :** uniformité terminale et stabilité au passage `t\uparrow T_*`.

## 9. Décision de catalogue et lemme suivant

Sources réellement absentes et prioritaires recommandées pour le prochain
lot de `sources.json` :

| ID proposé | Source | Statut à enregistrer | Raison |
|---|---|---|---|
| `NS-SRC-0180` | Saari–Schwarzacher 2023 | preuve publiée | dérivée temporelle de l'inverse de divergence |
| `NS-SRC-0181` | Wolf 2017 | preuve publiée | décomposition locale de pression générique |
| `NS-SRC-0182` | Kwon 2023 | preuve publiée | projection de Leray localisée et force solénoïdale |
| `NS-SRC-0183` | Breit 2025 | preuve publiée | NS en domaine mobile; obstruction `R'\notin L^3_t` |
| `NS-SRC-0184` | Zhang 2024 v3 | prépublication | contre-garde sur blow-up forcé et convention de criticité |

Conformément au mandat, cette revue ne modifie pas le catalogue et ne crée
pas elle-même ces IDs.

Le lemme analytique à isoler ensuite n'est pas « Bogovskii commute avec le
temps », qui est faux, ni « chaque terme de force est critique fort », qui
échoue logarithmiquement. Il doit porter sur la combinaison complète :

> **Lemme candidat falsifiable.** Sous une hypothèse critique précisément
> choisie sur `u` et avec un cutoff radial, la projection de la somme entre
> crochets dans (11), calculée avec le correcteur homothétique (3), possède
> une annulation de moment ou une structure de divergence qui améliore
> strictement la borne `R^{-3}` dans une norme adaptée au propagateur de
> Stokes.

Le test décisif est un calcul symbolique puis pseudo-spectral sur des champs
solénoïdaux Type I localisés dans l'anneau de référence : mesurer séparément
les huit contributions de (11), leur somme projetée et le coefficient du mode
`R^{-3}`. Un seul champ admissible pour lequel ce coefficient reste non nul
réfute toute annulation universelle et impose d'ajouter une hypothèse
géométrique ou de moment.

## Conclusion

La littérature publiée transfère rigoureusement le **montage spatial** et la
possibilité de dériver un inverse de divergence mobile. Elle ne transfère pas
un théorème de lissage jusqu'au collapse. L'anneau homothétique évite la perte
des constantes spatiales, mais la vitesse `R'/R`, la pression non locale et le
défaut non linéaire se rejoignent exactement à l'ordre force `R^{-3}`. Le
premier obstacle n'est donc plus l'existence de `V`; c'est l'absence d'une
annulation démontrée de sa force complète dans une classe critique assez
forte. Le résidu quantitatif publié est la divergence logarithmique (15), et
la veille 2025–2026 ne fournit aucun endpoint qui l'absorbe.
