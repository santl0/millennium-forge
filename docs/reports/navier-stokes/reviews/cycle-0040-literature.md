# Cycle 0040 — revue primaire : coupure solénoïdale et opérateur de Bogovskiĭ sur couronnes

Date de coupure : **2026-08-15**
Objet : auditer les droites inverses de la divergence qui permettent de
localiser un champ incompressible, avec un contrôle explicite du support, de
la géométrie, de l'échelle et du endpoint Lorentz secondaire `q=∞`.

## Verdict

Le maillon fonctionnel nécessaire à une coupure solénoïdale est valide, mais
dans un cadre plus étroit que l'énoncé informel « Bogovskiĭ a une constante
uniforme sur les couronnes ».

1. Sur une couronne de forme fixe
   `A_R=B_{2R}\setminus\overline{B_R}`, il existe une droite inverse linéaire
   de la divergence

   \[
   \mathcal B_R:L^{p,q}_0(A_R)\longrightarrow
   W^{1,(p,q)}_0(A_R)^3,
   \qquad 1<p<\infty,\quad 1\le q\le\infty,
   \]

   telle que `div B_R f=f`. La constante de
   `||∇B_Rf||_{L^{p,q}}\lesssim ||f||_{L^{p,q}}` est indépendante de `R`.
   Le cas `q=∞` vient d'une interpolation réelle entre deux exposants
   **forts** `1<p_0<p<p_1<∞`; ce n'est ni le endpoint primaire `p=1`, ni
   `p=∞`.
2. Cette uniformité est une invariance par translation et homothétie d'un
   domaine de référence. Elle ne couvre pas les couronnes minces
   `A_{R,h}={R<|x|<R+h}` lorsque `h/R→0`, ni une chaîne dont le nombre de
   patches diverge.
3. Une passe adverse par inf-sup donne une obstruction quantitative nouvelle :
   toute droite inverse

   \[
   L^p_0(A_{R,h})\to W^{1,p}_0(A_{R,h})^3
   \]

   a une norme au moins `c_p R/h`, pour `0<h≤R`. Une constante uniforme sur
   les couronnes dégénérantes est donc impossible pour cette condition de
   bord, quel que soit le choix de l'opérateur.
4. Pour une coupure `χ_R` et un champ `U` divergence-free, la correction
   `b_R=B_R(∇χ_R·U)` produit bien

   \[
   \widetilde U_R=\chi_RU-b_R,
   \qquad \operatorname{div}\widetilde U_R=0,
   \]

   égale à `U` sur `B_R` et nulle hors de `B_{2R}`. Elle conserve des bornes
   d'échelle critique dans `L^{3,∞}` et, si
   `curl U∈L^{3/2,∞}`, dans `L^{3/2,∞}` pour le curl.
5. La correction ne préserve cependant ni la direction, ni le signe, ni le
   rapport cellule/vorticité, ni une masse positive de vorticité. Elle peut
   être du même ordre critique que le col original. Elle ne neutralise donc
   pas le contre-modèle de cancellation du cycle 0039.
6. Aucun article primaire 2025–2026 trouvé dans la veille ciblée ne fournit
   le gain manquant. Les nouveautés donnent soit une construction analytique
   sur une couronne sans estimation Lorentz quantitative, soit une théorie de
   support générale encore sans application Navier–Stokes quantitative, soit
   un opérateur discret.

Le résultat transférable au verrou actif est donc exactement : **la
localisation solénoïdale à rapport d'échelles fixé est licite avec constantes
critiques uniformes; elle n'est pas une hypothèse d'anti-cancellation et ne
reste pas uniforme lorsque la géométrie dégénère.**

## 1. Cadre exact et échelle

La partie opérateur concerne un domaine borné connexe Lipschitz
`Ω⊂R³`, un exposant `1<p<∞` et

\[
L^p_0(\Omega)=\left\{f\in L^p(\Omega):
\int_\Omega f=0\right\}.
\]

Une droite inverse de Bogovskiĭ est un opérateur linéaire borné

\[
\mathcal B_\Omega:L^p_0(\Omega)\to W^{1,p}_0(\Omega)^3,
\qquad \operatorname{div}\mathcal B_\Omega f=f.
\]

La cible `W^{1,p}_0` impose la trace nulle sur toutes les composantes du bord;
l'extension par zéro est donc supportée dans `\overline Ω` au sens Sobolev.
Sur un domaine connexe, la condition `∫f=0` est nécessaire par le théorème de
Gauss et suffisante pour une droite inverse sur un domaine Lipschitz. Sur un
domaine non connexe, elle doit être imposée composante par composante.

Le raccord Clay visé reste l'équation incompressible 3D non forcée

\[
\partial_tu-\nu\Delta u+(u\cdot\nabla)u+\nabla p=0,
\qquad \operatorname{div}u=0,
\]

sur `R³×(0,T)` ou le tore périodique, avec `ν>0`, donnée initiale lisse
divergence-free et solution classique/forte jusqu'au temps maximal. Sous

\[
u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),
\qquad
\omega_\lambda(x,t)=\lambda^2\omega(\lambda x,\lambda^2t),
\]

on a

\[
\|u_\lambda(t)\|_{L^{3,\infty}}
=\|u(\lambda^2t)\|_{L^{3,\infty}},\qquad
\|\omega_\lambda(t)\|_{L^{3/2,\infty}}
=\|\omega(\lambda^2t)\|_{L^{3/2,\infty}}.
\]

L'opérateur de divergence est d'ordre un. La bonne estimation homogène est
donc celle de `∇Bf`; le terme sans dérivée porte une longueur :

\[
\|\nabla\mathcal B_Rf\|_{L^{p,q}(A_R)}
+R^{-1}\|\mathcal B_Rf\|_{L^{p,q}(A_R)}
\le C\|f\|_{L^{p,q}(A_R)}.
\]

## 2. Réaudit de `NS-SRC-0103` : ce que Costabel–McIntosh établit

Martin Costabel et Alan McIntosh, *On Bogovskiĭ and Regularized Poincaré
Integral Operators for de Rham Complexes on Lipschitz Domains* (version arXiv
v2 du 30 mars 2009; version publiée, *Mathematische Zeitschrift* 265 (2010),
297–320),
[DOI 10.1007/s00209-009-0517-8](https://doi.org/10.1007/s00209-009-0517-8),
[arXiv:0808.2614v2](https://arxiv.org/abs/0808.2614).

### Énoncé utile

Pour un domaine étoilé par rapport à une boule ouverte, l'opérateur de type
Bogovskiĭ préserve le support imposé par la condition de Dirichlet complète
et relève d'un ordre de Sobolev : pour `m≥0`, `1<p<∞`, il envoie
`W^{m-1,p}_0` dans `W^{m,p}_0`. Pour le degré supérieur, la condition de
compatibilité est l'intégrale nulle et l'identité d'homotopie donne
`div Bf=f`. Les auteurs montrent aussi que leurs opérateurs régularisés sont
des opérateurs pseudodifférentiels d'ordre `-1` et obtiennent des applications
aux échelles de Besov et Triebel–Lizorkin.

Pour un domaine borné Lipschitz, ils passent par un recouvrement fini de
domaines étoilés et obtiennent la même régularité de complexe. Une couronne
sphérique est Lipschitz mais **n'est pas étoilée par rapport à une boule** : le
théorème Lipschitz/recouvrement, et non la formule à un seul centre, est le
bon maillon.

### Précisions nécessaires au catalogue

- La source donne l'existence et la bornitude sur chaque domaine fixé. Elle
  ne dit pas qu'une même constante vaut pour une famille arbitraire de
  domaines Lipschitz.
- Le support local vient de la condition de Dirichlet complète et de la
  construction compacte; il ne signifie pas que l'opérateur est ponctuel.
  Sa valeur en un point reste une intégrale non locale à l'intérieur du
  domaine de correction.
- La théorie de de Rham sur un domaine Lipschitz général contient des espaces
  de cohomologie lisses de dimension finie. Pour l'équation scalaire
  `div b=f` au degré supérieur sur une couronne connexe, le seul cokernel est
  l'intégrale. Les trous redeviennent pertinents aux degrés inférieurs
  (potentiels de curl, périodes, circulations).
- Les échelles Besov/Triebel–Lizorkin de la source sont compatibles avec une
  analyse Lorentz, mais elles ne doivent pas être citées seules comme un
  théorème `L^{p,∞}`. Le passage Lorentz utilisé ici est l'interpolation
  explicite de la section 4.

Statut après réaudit : `NS-SRC-0103` reste **correct et central**; sa portée
doit être limitée au domaine fixé, ou à une famille dont la géométrie est
contrôlée par un argument additionnel.

## 3. Réaudit de `NS-SRC-0111` : constantes géométriques, mais borne supérieure

Johnny Guzmán et Abner J. Salgado, *Estimation of the Continuity Constants for
Bogovskiĭ and Regularized Poincaré Integral Operators* (arXiv v1 du 8 octobre
2020; version publiée, *Journal of Mathematical Analysis and Applications*
502 (2021), 125246),
[DOI 10.1016/j.jmaa.2021.125246](https://doi.org/10.1016/j.jmaa.2021.125246),
[arXiv:2010.04105](https://arxiv.org/abs/2010.04105).

La source étudie les opérateurs sur les formes différentielles comme
applications de `L²` vers `H¹`. Si `Ω` est étoilé par rapport à une boule
`B`, elle suit la dépendance en

\[
R=\operatorname{diam}\Omega,
\qquad \rho=\operatorname{diam}B,
\qquad R/\rho.
\]

Le théorème 26 et son corollaire donnent des majorations explicites pour
l'opérateur de Bogovskiĭ; selon le degré, apparaissent le rapport de diamètres
et des facteurs de volume ou logarithmiques. La source traite aussi certaines
unions finies de domaines étoilés; les estimations obtenues peuvent dépendre
du nombre de pièces de la chaîne.

Deux corrections de lecture sont indispensables.

1. C'est une théorie quantitative `L²→H¹`, pas un théorème publié dans toute
   l'échelle `L^{p,q}`.
2. Les formules sont des **bornes supérieures pour les opérateurs construits**.
   Leur croissance lorsque `R/ρ` ou le nombre de patches croît ne prouve pas,
   à elle seule, qu'aucun meilleur opérateur uniforme n'existe.

La non-uniformité intrinsèque des couronnes minces est établie séparément par
la minoration inf-sup de la section 6. `NS-SRC-0111` doit donc être conservée
comme quantification constructive de la dépendance géométrique, pas comme une
borne inférieure d'impossibilité.

## 4. Passage rigoureux au Lorentz `q=∞`

Fixons un domaine Lipschitz `Ω` et deux exposants

\[
1<p_0<p<p_1<\infty,
\qquad
\frac1p=\frac{1-\theta}{p_0}+\frac\theta{p_1}.
\]

Choisissons une fonction lisse `η` d'intégrale un dans `Ω` et le projecteur
borné

\[
Qf=f-\left(\int_\Omega f\right)\eta.
\]

La composition `BΩQ` est définie sur tout `L^{p_i}` et ses composantes ainsi
que leurs dérivées sont bornées sur `L^{p_i}`, `i=0,1`. L'interpolation réelle
donne

\[
(L^{p_0},L^{p_1})_{\theta,q}=L^{p,q},
\qquad 1\le q\le\infty,
\]

et donc, sur les fonctions de moyenne nulle,

\[
\|\nabla\mathcal B_\Omega f\|_{L^{p,q}}
\le C_{\Omega,p,q}\|f\|_{L^{p,q}},
\qquad 1\le q\le\infty.
\]

Cette preuve contourne deux confusions fréquentes :

- `q=∞` est admis comme paramètre secondaire de l'espace interpolé, parce
  que `p` reste strictement entre `p_0` et `p_1`;
- elle ne donne aucune borne à `p=1` ou `p=∞`, où la théorie de Calderón–
  Zygmund exige d'autres espaces (`H¹`, `BMO`, mesures) et où la surjectivité
  sous la forme ci-dessus ne peut pas être supposée.

Le zéro de moyenne est stable grâce au projecteur de rang un `Q`; il ne faut
pas interpoler naïvement deux sous-espaces sans identifier leur complément
commun.

## 5. Homothétie : uniformité exacte sur les couronnes de forme fixe

Soit `Ω_R=x_0+RΩ` et, pour `f` sur `Ω_R`, posons

\[
g(y)=f(x_0+Ry),\qquad
(\mathcal B_{\Omega_R}f)(x)
=R(\mathcal B_\Omega g)\!\left(\frac{x-x_0}{R}\right).
\]

Alors

\[
\operatorname{div}_x\mathcal B_{\Omega_R}f=f,
\]

la trace nulle et le support sont transportés, et les lois de changement de
variables Lorentz donnent

\[
\|\nabla\mathcal B_{\Omega_R}f\|_{L^{p,q}(\Omega_R)}
\le C_{\Omega,p,q}\|f\|_{L^{p,q}(\Omega_R)},
\]

\[
R^{-1}\|\mathcal B_{\Omega_R}f\|_{L^{p,q}(\Omega_R)}
\le C_{\Omega,p,q}\|f\|_{L^{p,q}(\Omega_R)}.
\]

La constante est exactement celle du domaine de référence, modulo les
conventions équivalentes de quasi-norme Lorentz. En prenant
`Ω=B_2\setminus\overline{B_1}`, on obtient l'uniformité en `R` sur
`A_R=B_{2R}\setminus\overline{B_R}`.

Cette déduction ne requiert pas une estimation explicite du rapport étoilé :
elle requiert seulement un opérateur borné sur **une** couronne de référence,
puis le transporte. Elle cesse d'être applicable dès que le rapport
`R_2/R_1`, l'épaisseur relative, la constante de John/Lipschitz ou le nombre
de patches varie sans contrôle.

## 6. Passe adverse indépendante : impossibilité uniforme sur une couronne mince

Cette section est une dérivation interne falsifiable, statut
`AI_INTERNAL_DERIVATION`, et non une attribution aux sources précédentes.

Soit

\[
A_{R,h}=\{x\in\mathbb R^3:R<|x|<R+h\},
\qquad 0<h\le R,
\]

et `1<p<∞`, avec exposant conjugué `p'`. Prenons

\[
q(x)=\frac{x_1}{|x|}.
\]

Par symétrie, `q` a moyenne nulle. De plus

\[
\|\nabla q\|_{L^{p'}(A_{R,h})}
\le \frac C R\|q\|_{L^{p'}(A_{R,h})}.
\]

Pour tout `v∈W^{1,p}_0(A_{R,h})^3`, l'inégalité de Poincaré le long des
segments radiaux, avec poids radial comparable puisque `h≤R`, donne

\[
\|v\|_{L^p(A_{R,h})}\le C_ph
\|\nabla v\|_{L^p(A_{R,h})}.
\]

L'intégration par parties, sans terme de bord, implique alors

\[
\begin{aligned}
\left|\int_{A_{R,h}}q\,\operatorname{div}v\right|
&=\left|\int_{A_{R,h}}\nabla q\cdot v\right|\\
&\le C_p\frac hR
\|q\|_{L^{p'}(A_{R,h})}
\|\nabla v\|_{L^p(A_{R,h})}.
\end{aligned}
\]

Dans la formulation inf-sup de la divergence, `q` représente bien une classe
non nulle de `L^{p'}/R`; par symétrie, zéro est son meilleur représentant
constant, à équivalence uniforme près. Ainsi

\[
\beta_p(A_{R,h})
:=\inf_{[r]\ne0}\sup_{v\ne0}
\frac{\int r\,\operatorname{div}v}
{\inf_c\|r-c\|_{p'}\,\|\nabla v\|_p}
\le C_p\frac hR.
\]

Si une droite inverse `B_{R,h}` vérifie

\[
\|\nabla B_{R,h}f\|_p\le C_{R,h}\|f\|_p,
\]

la dualité impose `β_p≥C_{R,h}^{-1}`. Par conséquent

\[
\boxed{C_{R,h}\ge c_p\frac Rh.}
\]

Le test adverse ne dépend ni de la formule de Bogovskiĭ, ni d'un recouvrement
particulier. Il réfute toute extension « uniforme pour toutes les couronnes »
avec trace nulle complète. Il est cohérent avec l'uniformité du cas
`h\asymp R`.

Points à vérifier lors d'une formalisation : densité de `C_c^∞` dans
`W^{1,p}_0`, constante uniforme de Poincaré radial pour `h≤R`, identification
du dual de `L^p_0` à `L^{p'}/R`, et optimalité du représentant constant de la
fonction impaire `q`. Aucun de ces points n'utilise Navier–Stokes.

## 7. Lemme de coupure solénoïdale critique

Prenons `χ_R∈C_c^∞(B_{2R})`, `χ_R=1` sur `B_R` et
`|∇χ_R|≤C/R`. Pour un champ divergence-free `U` suffisamment régulier sur
`B_{2R}`, posons sur `A_R`

\[
f_R=\operatorname{div}(\chi_RU)=\nabla\chi_R\cdot U.
\]

Comme `χ_RU` est compactement supporté et `div U=0`, on a

\[
\int_{A_R}f_R=0.
\]

La mesure de `A_R` est comparable à `R³`. L'inclusion Lorentz sur un ensemble
de mesure finie donne

\[
\|f_R\|_{L^{3/2,\infty}(A_R)}
\le C|A_R|^{1/3}\|f_R\|_{L^{3,\infty}(A_R)}
\le C\|U\|_{L^{3,\infty}(A_R)}.
\]

Définissons `b_R=B_Rf_R`, prolongé par zéro hors de la couronne, puis

\[
\widetilde U_R=\chi_RU-b_R.
\]

Alors, au sens des distributions,

\[
\operatorname{div}\widetilde U_R=0,
\qquad
\widetilde U_R=U\ \text{sur }B_R,
\qquad
\operatorname{supp}\widetilde U_R\subset\overline{B_{2R}}.
\]

La borne de Bogovskiĭ et l'injection de Sobolev–Lorentz
`W^{1,(3/2,∞)}_0↪L^{3,∞}` donnent

\[
\|\nabla b_R\|_{L^{3/2,\infty}}
+\|b_R\|_{L^{3,\infty}}
\le C\|U\|_{L^{3,\infty}(A_R)}.
\]

Si `W=curl U∈L^{3/2,∞}`, alors

\[
\operatorname{curl}\widetilde U_R
=\chi_RW+\nabla\chi_R\times U-\operatorname{curl}b_R
\]

et donc

\[
\|\widetilde U_R\|_{L^{3,\infty}}
\le C\|U\|_{L^{3,\infty}(B_{2R})},
\]

\[
\|\operatorname{curl}\widetilde U_R\|_{L^{3/2,\infty}}
\le C\left(
\|W\|_{L^{3/2,\infty}(B_{2R})}
+\|U\|_{L^{3,\infty}(A_R)}
\right).
\]

Toutes les constantes sont indépendantes de `R`, mais aucun terme du membre
de droite n'est petit sans une hypothèse supplémentaire de petitesse dans le
collier. Le champ `curl b_R` est non local dans `A_R` et peut recouvrir le col
`∇χ_R×U`. La construction ne conserve donc pas :

- la direction ou le signe ponctuel de la vorticité;
- l'orthogonalité de cellules étiquetées;
- une minoration de masse critique par cellule;
- une équation de Navier–Stokes non forcée pour le champ localisé.

Si `U=U(t)`, la différentiation de la correction produit

\[
\partial_tb_R
=\mathcal B_R(\nabla\chi_R\cdot\partial_tU),
\]

avant même les commutateurs avec `Δ`, le terme quadratique et la pression. Une
borne statique critique ne contrôle pas ce résidu. Les articles de
localisation Navier–Stokes qui utilisent Bogovskiĭ complètent donc la coupure
par une équation de Stokes/Navier–Stokes forcée, une décomposition de pression
ou une unicité faible-forte; ils ne prétendent pas que `U~_R` résout
automatiquement l'équation Clay.

## 8. Usage Navier–Stokes publié et directement vérifiable

Dallas Albritton, Tobias Barker et Christophe Prange, *Epsilon Regularity for
the Navier–Stokes Equations via Weak-Strong Uniqueness*, *Journal of
Mathematical Fluid Mechanics* 25, article 49 (2023), version publiée le
24 mai 2023,
[DOI 10.1007/s00021-023-00780-0](https://doi.org/10.1007/s00021-023-00780-0),
[arXiv:2211.16188](https://arxiv.org/abs/2211.16188).

L'équation est Navier–Stokes incompressible 3D, viscosité normalisée à un,
non forcée dans le cylindre local considéré. Dans la preuve, les auteurs
choisissent une coupure égale à un sur `B_{7/8}`, supportée dans `B_{15/16}`,
et appliquent Bogovskiĭ sur la couronne fixe
`B_{15/16}\setminus\overline{B_{7/8}}`. Ils construisent ainsi une extension
compactement supportée et divergence-free, égale au champ dans la boule
intérieure, avec une estimation `L⁴` à constante universelle pour cette
géométrie normalisée. L'extension est ensuite intégrée à un argument de
Stokes/chaleur et d'unicité faible-forte.

Cette source valide un usage réel de la coupure solénoïdale sur une couronne
fixe. Elle ne publie pas la borne faible-`L³` dérivée à la section 7 et ne
donne pas de constante uniforme pour des couronnes minces.

## 9. Topologie, flux et support : tableau des compatibilités

| Problème | Compatibilité nécessaire | Situation sur une couronne connexe |
|---|---|---|
| `div b=f`, `b∈W^{1,p}_0` | `∫f=0` | suffisante sur domaine Lipschitz/John |
| même problème sur domaine non connexe | moyenne nulle sur chaque composante | une condition par composante |
| potentiel `curl a=F` ou degré inférieur de de Rham | périodes/flux selon la cohomologie | le trou peut créer une obstruction |
| extension divergence-free égale à un champ intérieur | flux net nul à travers toute interface fermée conservée | nécessaire par Gauss |
| champ lisse divergence-free défini dans toute la boule | flux à travers toute sphère nul | obstruction absente |
| domaine extérieur ou poncturé avec flux imposé | le flux peut être non nul | raccord compact impossible sans modifier l'intérieur |

Il faut distinguer « `b` a trace nulle sur le bord de la couronne » de « le
champ original peut être coupé sans changer son flux ». Pour un champ Clay
lisse dans tout `R³`, le flux à travers une sphère fermée est nul; la source
`f_R=∇χ_R·U` satisfait alors automatiquement la compatibilité. Cette
conclusion ne se transporte pas sans vérification aux domaines extérieurs,
aux champs avec singularité intérieure ou aux potentiels de curl.

Une source de géométrie plus générale est Gabriel Acosta, Ricardo G. Durán et
María A. Muschietti, *Solutions of the Divergence Operator on John Domains*,
*Advances in Mathematics* 206 (2006), 373–401,
[DOI 10.1016/j.aim.2005.09.004](https://doi.org/10.1016/j.aim.2005.09.004),
[PDF de la version publiée](https://bibliotecadigital.exactas.uba.ar/download/paper/paper_00018708_v206_n2_p373_Acosta.pdf).
Ils construisent une droite inverse explicite
`L^p_0→W^{1,p}_0`, `1<p<∞`, sur les domaines de John. Pour les domaines ayant
la propriété de séparation et `1<p<n`, ils donnent aussi une réciproque; les
domaines à cusp externe fournissent la frontière négative. Cette source
confirme que la géométrie, et non la seule topologie, gouverne l'uniformité
quantitative.

## 10. Veille différentielle 2025–2026

### 10.1 Construction analytique exacte sur une couronne

Chi Hin Chan, Jun-Shuo Chen et Cheng-Fang Su, *Real Analytic Solutions to the
Divergence Equation*,
[arXiv:2602.21925v1](https://arxiv.org/abs/2602.21925), soumis le 25 février
2026, **prépublication non évaluée** au jour de coupure.

Pour une couronne `A(R_1,R_2)⊂R^n`, `n≥2`, et une donnée réelle-analytique
sur la couronne fermée, d'intégrale nulle, les auteurs construisent un champ
réel-analytique jusqu'au bord, nul sur les deux composantes du bord et de
divergence égale à la donnée. La méthode est différentielle-topologique et se
distingue des formules de Bogovskiĭ et Kapitanskii–Pileckas.

La source ne fournit, dans son énoncé principal, ni borne `L^p`/Lorentz de
type Calderón–Zygmund, ni constante uniforme quand `R_2/R_1→1`, ni
localisation temporelle Navier–Stokes. Une extension par zéro d'un champ de
trace nulle est Sobolev, mais ne devient pas pour autant réelle-analytique à
travers le bord. Il n'y a donc aucun gain actuel sur le lemme critique.

### 10.2 Opérateurs à support prescrit par récupération sur des courbes

Philip Isett, Yuchen Mao, Sung-Jin Oh et Zhongkai Tao, *Integral Formulas for
Under/Overdetermined Differential Operators via Recovery on Curves and the
Finite-Dimensional Cokernel Condition I: General Theory*,
[arXiv:2509.04617v1](https://arxiv.org/abs/2509.04617), soumis le 4 septembre
2025, **prépublication non évaluée**.

Les auteurs construisent pour une classe d'opérateurs sous-déterminés, dont
la divergence, des droites inverses modulo un opérateur de rang fini, avec
ordre de régularisation optimal et propriétés de support prescrites. La
méthode généralise notamment Bogovskiĭ. L'article annonce que les applications
seront traitées dans des travaux suivants. À ce stade, il ne fournit pas le
théorème spécialisé requis ici : constante faible-`L³` uniforme sur une
famille de couronnes, correction de vorticité, ou raccord à une solution Clay.
Il mérite une veille parce que le contrôle géométrique du support est
exactement le paramètre actif.

### 10.3 Version discrète

Johnny Guzmán, Anil N. Hirani, Bingyan Liu et Pratyush Potu, *Discrete
Poincaré and Bogovskiĭ Operators on Cochains and Whitney Forms*,
[arXiv:2603.29018v2](https://arxiv.org/abs/2603.29018), version du 2 avril
2026, **prépublication non évaluée**.

La source construit des opérateurs discrets sur cochaînes et formes de
Whitney, et un Bogovskiĭ discret sur des domaines étoilés qui préserve les
conditions au bord homogènes. C'est pertinent pour une future expérience
FEEC ou une certification d'inf-sup. Ce n'est pas une droite inverse continue
dans `L^{p,∞}`, et aucune extrapolation au continuum ou au problème Clay n'est
permise.

### Conclusion de la veille

La recherche ciblée n'a identifié aucun résultat primaire 2025–2026 qui
contredise la frontière suivante : support local et uniformité critique sont
disponibles pour une géométrie normalisée fixe; la dégénérescence d'épaisseur
force une perte, et le contrôle solénoïdal seul ne produit aucune
anti-cancellation de vorticité.

## 11. Implication exacte vers le problème Clay

Le graphe d'implication vérifié est

\[
\begin{array}{c}
U\in L^{3,\infty},\quad \operatorname{div}U=0,
\quad \operatorname{curl}U\in L^{3/2,\infty}
\\[2mm]
\Downarrow\ \text{coupure fixe + compatibilité de moyenne}
\\[2mm]
\widetilde U_R\text{ compactement supporté, divergence-free}
\\[1mm]
\|\widetilde U_R\|_{3,\infty}
+\|\operatorname{curl}\widetilde U_R\|_{3/2,\infty}
\le C(\|U\|_{3,\infty}+\|\operatorname{curl}U\|_{3/2,\infty})
\\[2mm]
\not\Downarrow
\\[-1mm]
\text{petitesse, positivité, absence de cancellation,
ou évolution Navier--Stokes non forcée.}
\end{array}
\]

Pour une solution classique Clay, la coupure est donc un outil légitime pour
construire un champ test, une donnée locale solénoïdale ou un contre-profil à
une échelle fixée. Elle ne donne ni critère de prolongement, ni borne uniforme
en temps, ni contrôle de la pression, ni exclusion d'une solution ancienne.

Sur le tore, une construction dans une boule strictement plus petite que le
rayon d'injectivité peut être transportée dans une carte, mais la périodisation
et la moyenne globale doivent être revérifiées. Le théorème sur `R³` ne doit
pas être cité mot pour mot comme un théorème torique.

## 12. Attaques contradictoires et résultat

| Attaque | Résultat |
|---|---|
| « Toute couronne est étoilée » | Faux : une couronne trouée n'est pas étoilée; utiliser le théorème Lipschitz/John. |
| « La constante est uniforme parce que l'opérateur est d'ordre `-1` » | Insuffisant : l'ordre fixe l'échelle, pas la géométrie. |
| « `q=∞` est un endpoint interdit » | Faux ici : seul l'exposant secondaire vaut `∞`; interpolation entre deux `p` intérieurs. |
| « Guzmán–Salgado prouve une minoration géométrique » | Faux : leurs estimations citées sont des majorations constructives. |
| « Le trou impose plus que `∫f=0` pour `div b=f` » | Faux au degré supérieur sur une couronne connexe Lipschitz; vrai potentiellement pour curl/périodes. |
| « La correction est petite parce que `|∇χ_R|∼R^{-1}` » | Faux au niveau critique : le volume `∼R³` compense exactement ce facteur. |
| « Une correction divergence-free préserve la vorticité de cellule » | Faux : `curl b_R` est un nouveau terme critique non local dans le collier. |
| « Le champ coupé résout encore Navier–Stokes » | Faux : commutateurs, force effective et pression doivent être reconstruits. |
| « Une constante uniforme vaut aussi si `h/R→0` » | Réfuté par `C_{R,h}≥cR/h`. |
| « Le calcul discret 2026 certifie le continuum » | Faux sans convergence et bornes d'erreur uniformes. |

Résultat scientifique du cycle : **positif** pour le lemme de coupure
solénoïdale critique à rapport fixé; **négatif et quantitatif** pour toute
uniformité sur les couronnes minces; **négatif** pour le transfert vers une
hypothèse anti-cancellation ou une résolution Clay.

## 13. Propositions de catalogue et décisions

Les identifiants ci-dessous sont proposés après `NS-SRC-0175`; vérifier leur
absence de collision lors de l'intégration par le pilote.

| ID proposé | Source | Statut | Décision |
|---|---|---|---|
| `NS-SRC-0176` | Acosta–Durán–Muschietti 2006, domaines de John | `PUBLISHED_PRIMARY` | promouvoir : frontière géométrique de la droite inverse |
| `NS-SRC-0177` | Albritton–Barker–Prange 2023 | `PUBLISHED_PRIMARY` | promouvoir : usage NS exact sur couronne fixe |
| `NS-SRC-0178` | Chan–Chen–Su 2026, arXiv:2602.21925v1 | `PREPRINT_PRIMARY` | promouvoir avec réserve : construction analytique sans borne critique |
| `NS-SRC-0179` | Isett–Mao–Oh–Tao 2025, arXiv:2509.04617v1 | `PREPRINT_PRIMARY` | veille prioritaire : support prescrit, applications différées |
| non promu ce cycle | Guzmán–Hirani–Liu–Potu 2026, arXiv:2603.29018v2 | `PREPRINT_PRIMARY_DISCRETE` | conserver en veille pour une expérience FEEC |

Correction recommandée pour `NS-SRC-0111` : remplacer toute phrase laissant
entendre que la croissance de leurs majorations « prouve » l'impossibilité
d'une constante uniforme par : « la source quantifie la dépendance
géométrique des opérateurs construits; une obstruction intrinsèque exige une
borne inférieure séparée ».

## 14. Prochaine expérience décisive

Formaliser et tester le quotient inf-sup de la section 6 sur la famille
`A_{1,h}` :

1. dériver une constante explicite dans la Poincaré radiale pondérée;
2. calculer numériquement la plus petite valeur singulière du couple
   divergence/gradient sur deux familles de maillages indépendantes;
3. vérifier que `β_p` est d'ordre `h` pour `p=2`, avec convergence de maillage;
4. si l'expérience devient assistée par ordinateur, enfermer la valeur propre
   discrète et ajouter une estimation certifiée de l'erreur de discrétisation;
5. utiliser le cas de rapport fixe comme contrôle négatif, où `β_2` doit rester
   borné sous changement d'échelle.

Le calcul ne serait pas une preuve de la minoration analytique; il servirait à
détecter une perte supplémentaire ou une erreur de constante. Pour le verrou
Navier–Stokes, l'expérience suivante est de mesurer, sur les contre-profils du
cycle 0040, le rapport

\[
\frac{\|\operatorname{curl}b_R\|_{L^{3/2,\infty}}}
{\|\nabla\chi_R\times U\|_{L^{3/2,\infty}}}
\]

et de tenter de le rendre arbitrairement grand ou proche d'un, afin de
réfuter toute petite correction implicite.

## Sources primaires auditées

- Costabel–McIntosh 2010 :
  [version primaire](https://arxiv.org/abs/0808.2614),
  [DOI](https://doi.org/10.1007/s00209-009-0517-8).
- Guzmán–Salgado 2021 :
  [version primaire](https://arxiv.org/abs/2010.04105),
  [DOI](https://doi.org/10.1016/j.jmaa.2021.125246).
- Acosta–Durán–Muschietti 2006 :
  [version publiée](https://bibliotecadigital.exactas.uba.ar/download/paper/paper_00018708_v206_n2_p373_Acosta.pdf),
  [DOI](https://doi.org/10.1016/j.aim.2005.09.004).
- Albritton–Barker–Prange 2023 :
  [version publiée](https://doi.org/10.1007/s00021-023-00780-0),
  [arXiv](https://arxiv.org/abs/2211.16188).
- Chan–Chen–Su 2026 :
  [arXiv:2602.21925v1](https://arxiv.org/abs/2602.21925).
- Isett–Mao–Oh–Tao 2025 :
  [arXiv:2509.04617v1](https://arxiv.org/abs/2509.04617).
- Guzmán–Hirani–Liu–Potu 2026 :
  [arXiv:2603.29018v2](https://arxiv.org/abs/2603.29018).

## Statut de preuve

- théorèmes de droite inverse et régularité sur domaines Lipschitz/John :
  `PAPER_PROOF`, sources publiées;
- construction NS sur couronne fixe de la section 8 : `PAPER_PROOF`, source
  publiée;
- interpolation Lorentz, homothétie, lemme de coupure et minoration de
  couronne mince : `AI_INTERNAL_DERIVATION`, à revoir/formaliser avant toute
  promotion comme affirmation;
- articles 2025–2026 : `PREPRINT`, aucune validation indépendante présumée;
- implication vers une résolution Clay : **aucune**.
