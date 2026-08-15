# Cycle 0043 — veille primaire sur Bogovskiĭ aux ordres négatifs

**Date de vérification :** 15 août 2026

**Nature :** revue bibliographique contradictoire interne, sources primaires

**Objet borné :** inverse de la divergence sur la couronne fixe

\[
A=\{x\in\mathbb R^3:1<|x|<2\},
\]

dans les échelles de Sobolev négatives et de Lorentz, avec conservation du
support et commutateurs avec le laplacien et la dilatation.

## Verdict exécutable

Les deux affirmations demandées n'ont pas le même statut.

1. **Oui, la borne**

   \[
   \mathcal B:W^{-1,p}_0(A)\longrightarrow L^p(A;\mathbb R^3),
   \qquad 1<p<\infty,                                      \tag{1}
   \]

   **est publiée.** C'est le cas (s=-1) du théorème 2.5 de
   Geißert–Heck–Hieber (2006). Leur convention est cruciale :

   \[
   W^{-1,p}_0(A):=(W^{1,p'}(A))',
   \qquad
   W^{-1,p}(A):=(W^{1,p'}_0(A))'.                           \tag{2}
   \]

   Le premier espace est celui qui encode la condition de bord complète. La
   droite-inverse vérifie
   \(\operatorname{div}\mathcal Bf=f\) sur le sous-espace compatible
   \(\langle f,1\rangle=0\). Pour la valeur utilisée au cycle 0043,
   (p=4/3), le seuil publié est bien satisfait :

   \[
   -1>-2+\frac1p=-\frac54.
   \]

2. **Non, Geißert–Heck–Hieber ne publie pas**

   \[
   \mathcal B:W^{-2,p}_0(A)\longrightarrow W^{-1,p}_0(A),  \tag{3}
   \]

   car son seuil (s>-2+1/p) exclut toujours (s=-2).
   **Mais Costabel–McIntosh publie les ingrédients qui donnent (3)** dans
   l'échelle précisément supportée

   \[
   F^{-2}_{p,2,\overline A}(\mathbb R^3)
      \longrightarrow
   F^{-1}_{p,2,\overline A}(\mathbb R^3),                   \tag{4}
   \]

   pour (1<p<\infty), après suppression de l'obstruction de masse. Comme
   (F^s_{p,2}=H^{s,p}), (4) est la réalisation Bessel–Sobolev des
   distributions supportées dans \(\overline A\). Sur un domaine lisse, elle
   représente naturellement le dual de l'espace de restriction
   (W^{2,p'}(A)), donc le (W^{-2,p}_0) de la convention (2).

3. **Aucune source primaire auditée ne publie la formulation non qualifiée**

   \[
   \mathcal B:(W^{2,p'}_0(A))'
      \longrightarrow (W^{1,p'}_0(A))'                     \tag{5}
   \]

   pour toute donnée, avec droite-inverse, support, Lorentz et commutateurs.
   Dans (5), même le moment \(\langle f,1\rangle\) n'est pas défini
   canoniquement puisque (1\notin W^{2,p'}_0(A)). Écrire simplement
   « (W^{-2,p}\to W^{-1,p}) » sans fixer la convention confond donc deux
   énoncés différents.

4. Costabel–McIntosh prouve que l'opérateur régularisé est
   pseudodifférentiel d'ordre (-1). Sur la couronne compacte fixe, le calcul
   symbolique standard donne

   \[
   [\Delta,\mathcal B]\in\Psi^0,
   \qquad
   [\mathcal B,D]\in\Psi^{-1},
   \qquad D=x\cdot\nabla.                                  \tag{6}
   \]

   Les bornes issues de (6) ne sont **pas énoncées mot pour mot** dans leur
   article : elles sont des corollaires directs de leur théorème 3.2, pour
   une réalisation fixée de l'opérateur. Elles ne découlent pas de la seule
   borne classique (L^p_0\to W^{1,p}_0).

5. Une borne de Lorentz publiée existe pour la sous-classe compatible en
   forme divergence : Albritton–Barker obtient

   \[
   \|\mathcal B(\operatorname{div}G)\|_{L^{p,\infty}(A)}
   \le C\|G\|_{L^{p,\infty}(A)},                            \tag{7}
   \]

   par interpolation réelle, sous la condition de trace normale nulle. Ce
   n'est pas un théorème publié sur un espace abstrait complet
   (W^{-1,(p,\infty)}_0(A)).

## 1. Conventions qui ne peuvent pas être omises

Soit \(1<p<\infty\), \(p'=p/(p-1)\). Geißert–Heck–Hieber définit, pour
(s<0),

\[
W^{s,p}(A)=(W^{-s,p'}_0(A))',
\qquad
W^{s,p}_0(A)=(W^{-s,p'}(A))'.                               \tag{8}
\]

Ainsi :

| notation | espace test dual | information au bord |
|---|---|---|
| \(W^{-1,p}(A)\) | \(W^{1,p'}_0(A)\) | plus grand espace négatif; la constante n'est pas un test admissible |
| \(W^{-1,p}_0(A)\) | \(W^{1,p'}(A)\) | plus petit espace négatif; \(\langle f,1\rangle\) est défini |
| \(H^{s,p}_{\overline A}(\mathbb R^3)\) | réalisation sur tout l'espace, support dans \(\overline A\) | condition de Dirichlet complète au sens des distributions supportées |

La compatibilité est nécessaire, indépendamment de toute formule. Si
(v\) est supporté dans \(\overline A\), alors

\[
\langle\operatorname{div}v,1\rangle
=-\langle v,\nabla1\rangle=0.                              \tag{9}
\]

Une droite-inverse à support préservé ne peut donc agir comme droite-inverse
que sur

\[
X^{s,p}_0(A)=
\{f\in X^{s,p}_{\overline A}:\langle f,1\rangle=0\}.        \tag{10}
\]

Comme (A\) est connexe, c'est l'unique obstruction de degré supérieur.
Pour un ouvert ayant plusieurs composantes connexes, il faut une annulation
sur chacune d'elles.

## 2. Geißert–Heck–Hieber : le raccord fort exact

Matthias Geißert, Horst Heck et Matthias Hieber,
[*On the Equation div u = g and Bogovskii's Operator in Sobolev Spaces of
Negative Order*](https://doi.org/10.1007/3-7643-7601-5_7), dans *Partial
Differential Equations and Functional Analysis*, OTAA 168, Birkhäuser,
2006, p. 113–121, DOI `10.1007/3-7643-7601-5_7`.

**Statut.** Chapitre publié. Le texte intégral déposé par un auteur et les
métadonnées de l'éditeur ont été recoupés.

Le théorème 2.5 porte sur tout domaine borné à bord localement lipschitzien.
Il construit le même opérateur

\[
\mathcal B:C_c^\infty(A)\to C_c^\infty(A;\mathbb R^3)
\]

et établit

\[
\mathcal B:W^{s,p}_0(A)\to W^{s+1,p}_0(A;\mathbb R^3)
\quad\text{si}\quad s>-2+\frac1p.                          \tag{11}
\]

Pour (s=-1), (11) est valable pour tout (1<p<\infty). À l'ordre zéro,
(W^{0,p}_0=L^p), ce qui donne (1). L'identité de divergence s'étend par
densité et continuité au noyau de la fonctionnelle de masse. Sur une donnée
générale, la formule locale de Bogovskiĭ donne plutôt, avec une fonction de
lissage normalisée \(\omega\),

\[
\operatorname{div}\mathcal Bf
=f-\omega\langle f,1\rangle.                                \tag{12}
\]

**Ce que le théorème ne donne pas.** À (s=-2), la condition de (11)
deviendrait (-2>-2+1/p), impossible. Le passage
(W^{-2,p}_0\to W^{-1,p}_0) ne doit donc jamais être attribué à ce
théorème.

Le précurseur cité pour (s=-1) est Wolfgang Borchers et Hermann Sohr,
[*On the equations rot v=g and div u=f with zero boundary
conditions*](https://doi.org/10.14492/hokmj/1381517172), *Hokkaido
Mathematical Journal* **19** (1990), 67–87, DOI
`10.14492/hokmj/1381517172`. L'article traite bien les conditions de bord
nulles; il ne remplace pas le théorème tous (p) et tous (s) de 2006.

### Cas requis au cycle 0043

Pour (p=4/3\), (p'=4), l'énoncé transférable est exactement

\[
\|\mathcal Bf\|_{L^{4/3}(A)}
\le C_A\|f\|_{(W^{1,4}(A))'},
\qquad \langle f,1\rangle=0.                               \tag{13}
\]

Il serait incorrect de remplacer le membre droit de (13) par la norme dans
((W^{1,4}_0(A))'\) sans un lemme supplémentaire.

## 3. Galdi : la compatibilité de trace n'est pas cosmétique

Giovanni P. Galdi, [*An Introduction to the Mathematical Theory of the
Navier–Stokes Equations: Steady-State Problems*, 2e
éd.](https://doi.org/10.1007/978-0-387-09620-9), Springer, 2011, DOI
`10.1007/978-0-387-09620-9`, section III.3.

**Statut.** Monographie primaire publiée. Les théorèmes III.3.3–III.3.4
donnent le cadre classique :

\[
\mathcal B:L^p_0(A)\to W^{1,p}_0(A;\mathbb R^3)             \tag{14}
\]

et, si (G\in L^p(A;\mathbb R^3)),
(\operatorname{div}G\in L^p(A)) et la trace normale vérifie
(G\cdot n=0\) sur \(\partial A\),

\[
\|\mathcal B(\operatorname{div}G)\|_{L^p(A)}
\le C\|G\|_{L^p(A)}.                                      \tag{15}
\]

La trace normale assure simultanément
(\int_A\operatorname{div}G=0\) et l'absence d'un terme de bord dans la
dualité. C'est la réalisation concrète, pour des données en forme divergence,
de l'appartenance à (W^{-1,p}_0=(W^{1,p'})'\). La discussion de Galdi ne
permet pas d'étendre (15) à un champ (G) arbitraire dont la trace normale
est non nulle.

**Audit adverse.** L'écriture formelle

\[
|\langle\operatorname{div}G,\varphi\rangle|
\le \|G\|_p\|\nabla\varphi\|_{p'}                         \tag{16}
\]

contrôle naturellement un dual de (W^{1,p'}_0\), mais ne contrôle le dual
de (W^{1,p'}\) qu'après élimination du flux de bord. Utiliser (16) pour
justifier (13) sans cette élimination inverse précisément les espaces de
(2).

## 4. Costabel–McIntosh : tous les ordres, mais dans l'échelle supportée

Martin Costabel et Alan McIntosh,
[*On Bogovskiĭ and regularized Poincaré integral operators for de Rham
complexes on Lipschitz domains*](https://doi.org/10.1007/s00209-009-0517-8),
*Mathematische Zeitschrift* **265** (2010), 297–320, DOI
`10.1007/s00209-009-0517-8`,
[`arXiv:0808.2614v2`](https://arxiv.org/abs/0808.2614v2).

**Statut.** Article publié; version primaire arXiv v2 du 30 mars 2009 auditée.

### 4.1 Résultat imprimé

Le théorème 3.2 démontre que les opérateurs régularisés de Poincaré et de
Bogovskiĭ (R_\ell,T_\ell\) sont des opérateurs pseudodifférentiels d'ordre
(-1), de symbole dans (S^{-1}_{1,0}\).

Le théorème 4.6 construit, sur tout domaine lipschitzien borné, des
opérateurs (T_\ell\) d'ordre (-1) et (L_\ell\) d'ordre (-\infty) tels
que, pour tout (s\in\mathbb R\),

\[
T_\ell:H^s_{\overline A}(\mathbb R^3;\Lambda^\ell)
\longrightarrow
H^{s+1}_{\overline A}(\mathbb R^3;\Lambda^{\ell-1}),        \tag{17}
\]

et

\[
dT_\ell+T_{\ell+1}d=I-L_\ell.                             \tag{18}
\]

Le support dans \(\overline A\) est conservé. Le théorème 4.9 décrit le
cokernel fini, et la remarque 4.10 donne, au degré supérieur,

\[
dH^{s+1}_{\overline A}(\mathbb R^3;\Lambda^2)
=\left\{f\in H^s_{\overline A}(\mathbb R^3;\Lambda^3):
\int f=0\right\}.                                          \tag{19}
\]

Enfin, la remarque 4.12 étend tous les résultats de la section aux espaces
de Besov (B^s_{p,q}) et de Triebel–Lizorkin (F^s_{p,q}). En choisissant
(F^s_{p,2}=H^{s,p}\), on obtient (17) pour tout (s\in\mathbb R\) et
(1<p<\infty\).

Le choix d'un complément au cokernel de dimension un, ou de façon équivalente
une correction lissante de rang fini de (T_3\), fournit une réalisation
linéaire \(\mathcal B_A\) telle que

\[
\begin{aligned}
\mathcal B_A &:H^{s,p}_{\overline A,0}(\mathbb R^3)
\longrightarrow H^{s+1,p}_{\overline A}(\mathbb R^3;\mathbb R^3),\\
\operatorname{div}\mathcal B_Af&=f,
\end{aligned}                                               \tag{20}
\]

où l'indice zéro dans la source signifie \(\langle f,1\rangle=0\).
Prendre (s=-2) donne bien la version supportée de (3).

### 4.2 Ce qui est démontré et ce qui est déduit

La chaîne de statut est la suivante :

| assertion | statut exact |
|---|---|
| (T_\ell\in\Psi^{-1}\) | théorème 3.2 publié |
| support et (H^s\to H^{s+1}\), tout (s\) | théorème 4.6 publié |
| même conclusion en (F^s_{p,q}\) | remarque 4.12 publiée |
| cokernel supérieur = masse | théorème 4.9 + remarque 4.10 publiés |
| opérateur exact (20) après correction de rang fini | conséquence constructive des résultats publiés |
| commutateurs (6) | corollaire de calcul pseudodifférentiel, non énoncé textuellement |

La dernière ligne se vérifie sur la couronne compacte par le calcul des
ordres. Le symbole de \(\Delta\) est indépendant de (x\); le symbole
principal d'ordre (1) dans
(\Delta\mathcal B_A-\mathcal B_A\Delta\) s'annule, laissant l'ordre zéro.
Pour (D=x\cdot\nabla\), la règle générale du commutateur donne
(-1+1-1=-1\). La correction de rang fini est lissante et ne change pas ces
ordres. Puisque (D\), \(\Delta\) et \(\mathcal B_A\) préservent tous le
support dans \(\overline A\), les commutateurs le préservent également.

On obtient notamment, pour (1<p<\infty\),

\[
\|[\Delta,\mathcal B_A]f\|_{L^p}
\le C_{A,p}\|f\|_{L^p},
\qquad
\|[\mathcal B_A,D]f\|_{W^{s+1,p}}
\le C_{A,s,p}\|f\|_{W^{s,p}},                              \tag{21}
\]

dans la réalisation supportée. La première borne est même plus forte que la
borne (L^p\to W^{-1,p}\) envisagée au début du cycle.

**Limite.** (21) ne vaut pas automatiquement pour « n'importe quelle droite
inverse ». Deux droites inverses diffèrent d'un opérateur à valeurs
divergence-free, qui peut détruire toute borne de commutateur. La réalisation
pseudodifférentielle doit être figée.

## 5. Confirmation moderne de (W^{-1,p}_0\to L^p)

Patrick Tolksdorf et Keiichi Watanabe,
[*The Navier–Stokes equations in exterior Lipschitz domains:
\(L^p\)-theory*](https://doi.org/10.1016/j.jde.2020.04.015), *Journal of
Differential Equations* **269** (2020), 5765–5801, DOI
`10.1016/j.jde.2020.04.015`,
[`arXiv:1906.02713v1`](https://arxiv.org/abs/1906.02713v1).

La proposition 4.2 énonce explicitement, pour un domaine lipschitzien borné
(D\),

\[
\mathcal B:W^{-1,p}_0(D)\to L^p(D;\mathbb C^n),             \tag{22}
\]

et précise dans la même phrase que (W^{-1,p}_0(D)) est le dual de
(W^{1,p'}(D)). Cette source est une confirmation publiée sans ambiguïté de
notation de (1), utilisée dans une théorie de Stokes/Navier–Stokes en domaine
extérieur. Elle ne donne pas (s=-2).

## 6. Saari–Schwarzacher : l'ordre deux révèle la perte au bord

Olli Saari et Sebastian Schwarzacher,
[*Construction of a Right Inverse for the Divergence in Non-cylindrical Time
Dependent Domains*](https://doi.org/10.1007/s40818-023-00150-z), *Annals of
PDE* **9** (2023), article 8, DOI `10.1007/s40818-023-00150-z`,
[`arXiv:2107.09573v3`](https://arxiv.org/abs/2107.09573v3).

**Équation et cadre.** L'article résout

\[
\operatorname{div}_x\mathcal Bf=f,
\qquad \mathcal Bf|_{\partial\Omega_t}=0,
\qquad \langle f(t),1\rangle=0,                            \tag{23}
\]

sur des tranches spatiales connexes d'un domaine espace-temps non
cylindrique à bord Hölder. Ce n'est pas une équation de Navier–Stokes; les
applications concernent la reconstruction de pression pour des solutions
faibles ou très faibles de Navier–Stokes incompressible visqueux en domaine
mobile.

La phrase précédant le théorème 4.5 est directement discriminante :

- dans le cas lipschitzien classique non pondéré, les estimations à trace
  nulle valent pour (k<2-1/p);
- (k=1\), \(\beta=1\) redonne le contrôle non pondéré d'ordre (-1);
- (k=2\) fait déjà apparaître un poids en distance au bord, destiné à
  quantifier l'échec possible de la borne non pondérée;
- les auteurs indiquent ne pas avoir démontré l'énoncé avec donnée dans le
  dual du Sobolev inhomogène.

Le théorème 4.5 porte en conséquence sur leurs espaces négatifs pondérés,
pas sur la flèche intrinsèque non qualifiée (5). Cette source confirme la
frontière conceptuelle entre l'ordre (-1) classique et l'ordre (-2) : elle
ne supprime pas la nécessité de l'échelle supportée de Costabel–McIntosh.

## 7. Lorentz et localisation Navier–Stokes réellement publiés

Dallas Albritton et Tobias Barker,
[*Localised necessary conditions for singularity formation in the
Navier–Stokes equations with curved
boundary*](https://doi.org/10.1016/j.jde.2020.06.009), *Journal of
Differential Equations* **269** (2020), 7529–7573, DOI
`10.1016/j.jde.2020.06.009`,
[`arXiv:1811.00507v2`](https://arxiv.org/abs/1811.00507v2).

**Équation exacte.** Navier–Stokes incompressible non forcé en dimension
trois,

\[
\partial_tu-\Delta u+(u\cdot\nabla)u+\nabla p=0,
\qquad \operatorname{div}u=0,                              \tag{24}
\]

sur un domaine borné à bord courbe, avec condition de non-glissement sur la
portion de bord considérée et notion de solution faible adaptée au bord.

Dans la remarque 2.4, pour un domaine borné lipschitzien étoilé par rapport à
une boule, les auteurs supposent

\[
G\in L^p,\quad \operatorname{div}G\in L^p,
\quad G\cdot n|_{\partial A}=0,                             \tag{25}
\]

et écrivent leur estimation (2.13), identique à (15). Par interpolation
réelle du même opérateur, ils obtiennent explicitement (2.14), la borne
faible-(L^p) (7). Elle est ensuite utilisée pour contrôler la troncation
solénoïdale d'une solution près d'une singularité candidate.

Cette application est le meilleur raccord publié vers la localisation
Navier–Stokes du cycle, mais sa portée exacte reste :

- une couronne fixe ou sélectionnée dans une région déjà régulière;
- une donnée spéciale \(\operatorname{div}G\) avec compatibilité de trace;
- une estimation spatiale, sans commutateur temporel d'un cutoff qui
  s'effondre;
- aucune preuve de régularité globale ni de blow-up.

Par interpolation entre deux exposants forts, on peut dériver des variantes
(L^{p,r}), mais aucune source primaire auditée n'énonce une droite-inverse
sur tout l'espace abstrait (W^{-1,(p,r)}_0\), ni un endpoint Lorentz des
commutateurs de (6). Ces extensions doivent garder le statut
`AI_INTERNAL_DERIVATION` tant qu'elles ne sont pas démontrées séparément.

## 8. Veille différentielle 2025–2026

La veille a été effectuée le **15 août 2026** sur les sources primaires et
leurs versions courantes, avec les requêtes combinant *divergence right
inverse*, *Bogovskii*, *negative Sobolev*, *Lorentz*, *support preserving*,
*annulus*, *commutator*, *Laplacian* et *Navier–Stokes localization*.

### 8.1 Isett–Mao–Oh–Tao 2025

Philip Isett, Yuchen Mao, Sung-Jin Oh et Zhongkai Tao,
[*Integral formulas for under/overdetermined differential operators via
recovery on curves and the finite-dimensional cokernel condition I: General
theory*](https://arxiv.org/abs/2509.04617v1),
`arXiv:2509.04617v1`, 4 septembre 2025, prépublication.

Le théorème 1.2 construit, sur un ouvert borné satisfaisant leur hypothèse
géométrique de récupération et d'« (x\)-étoilement », un opérateur à support
prescrit, optimalement régularisant,

\[
\widetilde W^{s,p}\to\widetilde W^{s+m,p},
\qquad 1<p<\infty,\ s\in\mathbb R,                          \tag{26}
\]

modulo le cokernel fini. La divergence appartient aux opérateurs auxquels la
méthode s'applique. C'est une nouvelle source primaire pertinente et elle
confirme la robustesse conceptuelle du gain d'un ordre à support prescrit.

Deux réserves empêchent d'en faire un meilleur fondement que
Costabel–McIntosh pour la couronne présente :

1. le théorème 1.15 sur un domaine lipschitzien borné général est annoncé
   explicitement comme provenant de leur référence [38], *Part II: Sharp
   solvability, preprint (2025)*;
2. cette Part II n'a, dans la version auditée de Part I, ni preuve incorporée
   ni identifiant arXiv vérifiable.

Part I ne publie en outre ni constante Lorentz annulaire, ni formule de
commutateur avec \(\Delta\) ou (D\), ni contrôle uniforme d'une couronne en
collapse. Le théorème 1.15 ne doit donc pas être compté comme preuve auditée
indépendante de ces points.

### 8.2 Chan–Chen–Su 2026

Chi Hin Chan, Jun-Shuo Chen et Cheng-Fang Su,
[*Real Analytic Solutions to the Divergence
Equation*](https://arxiv.org/abs/2602.21925v1),
`arXiv:2602.21925v1`, 25 février 2026, prépublication.

Les auteurs construisent une solution réelle analytique de
(\operatorname{div}v=f\) sur une couronne sphérique fermée, pour une donnée
réelle analytique de moyenne nulle, avec (v=0\) sur les deux composantes du
bord. C'est exactement la géométrie annulaire, mais l'article ne fournit pas
la borne (W^{-2,p}\to W^{-1,p}\), ni de norme de Lorentz, ni de calcul de
commutateur. Il ne remplace donc aucun des raccords (13), (20) ou (21).

### 8.3 Résultat négatif de la veille

Aucune source primaire 2025–2026 trouvée et vérifiée ne publie simultanément :

- la couronne lipschitzienne ou lisse fixe;
- la droite-inverse exacte à support préservé;
- le domaine intrinsèque complet ((W^{2,p'}_0(A))'\);
- un endpoint Lorentz;
- les commutateurs quantitatifs avec laplacien et dilatation;
- et une application au cutoff Navier–Stokes contractant.

La veille n'invalide donc pas le diagnostic : le bon socle actuel est
Geißert–Heck–Hieber à l'ordre (-1), et Costabel–McIntosh pour l'échelle
supportée tous ordres et le calcul symbolique.

## 9. Lemme transférable au cycle 0043

Le premier maillon que les sources permettent de figer est le suivant.

> **Lemme de couronne fixe — ingrédients publiés, commutateurs dérivés.**
> Soit (A=\{1<|x|<2\}\), (1<p<\infty\). Il existe une réalisation linéaire
> à support préservé \(\mathcal B_A\), fixée une fois pour toutes, telle que,
> pour tout (s\in\mathbb R\) et toute distribution
> (f\in H^{s,p}_{\overline A}(\mathbb R^3)\) de masse nulle,
> \[
> \operatorname{div}\mathcal B_Af=f,
> \qquad
> \|\mathcal B_Af\|_{H^{s+1,p}}
> \le C_{A,s,p}\|f\|_{H^{s,p}}.
> \]
> De plus,
> \([\Delta,\mathcal B_A]\in\Psi^0\) et
> \([\mathcal B_A,x\cdot\nabla]\in\Psi^{-1}\), avec support dans
> \(\overline A\).

La première partie est une reformulation de Costabel–McIntosh, théorèmes
3.2, 4.6, 4.9, remarque 4.10 et remarque 4.12. La seconde est une dérivation
de calcul symbolique standard. Le lemme ne doit donc pas être catalogué en
bloc comme `PAPER_PROOF`; son étiquette correcte est
`PUBLISHED_INGREDIENTS + AI_INTERNAL_DERIVATION`.

Pour l'emploi plus étroit à (p=4/3\), la flèche
(W^{-1,4/3}_0\to L^{4/3}\) est, elle, directement `PAPER_PROOF` par
Geißert–Heck–Hieber et Tolksdorf–Watanabe.

Sous homothétie (A_R=RA\), conjuguer **ce même opérateur** conserve les
constantes sans changer le rapport d'aspect. Cela n'élimine ni le facteur
(R'/R\) d'une dilatation dépendant du temps, ni la pression projetée, ni la
question de l'intégrabilité temporelle jusqu'au collapse.

## 10. Passe contradictoire et résidu

### Test A — masse

Choisir une donnée (f\) avec \(\langle f,1\rangle\ne0\). L'identité (9)
réfute immédiatement l'existence d'un correcteur supporté satisfaisant
(\operatorname{div}\mathcal Bf=f\).

**Résidu certifié :** obstruction scalaire de masse; aucune estimation ne la
compense.

### Test B — inversion des deux espaces négatifs

Dans ((W^{2,p'}_0(A))'\), le test constant n'est pas disponible. La
compatibilité de masse utilisée par toutes les constructions supportées n'est
donc pas une condition continue intrinsèque sur tout cet espace.

**Résidu certifié :** la flèche non sous-scriptée (5) n'est pas couverte par
les théorèmes audités.

### Test C — laplacien traité terme à terme

La seule borne (W^{-1,p}_0\to L^p\) ne permet pas d'estimer
(\mathcal B\Delta f\), puisque \(\Delta f\) est d'ordre (-2). L'amélioration
vient de l'annulation du symbole principal dans le commutateur complet
([\Delta,\mathcal B]\), pas de bornes séparées sur ses deux termes.

**Résidu certifié :** il faut conserver le même opérateur
pseudodifférentiel dans les deux compositions.

### Test D — droite-inverse non canonique

Ajouter à \(\mathcal B_A\) un opérateur arbitraire à valeurs
divergence-free conserve l'identité de divergence mais pas les normes ni les
commutateurs.

**Résidu certifié :** toute expérience ou preuve doit enregistrer la formule
ou au moins la classe symbolique de la réalisation employée.

### Test E — extrapolation Lorentz

L'estimation (7) agit sur (G\mapsto\mathcal B\operatorname{div}G\) avec
trace normale nulle. Elle ne prouve pas que toute distribution d'une norme
nommée (W^{-1,(p,\infty)}\) possède une telle représentation avec coût
uniforme.

**Résidu certifié :** représentation divergence + contrôle de trace à
démontrer pour chaque force localisée réelle.

### Test F — transfert Clay

Les opérateurs audités résolvent une équation elliptique de divergence. Ils
ne fournissent ni solution de Navier–Stokes, ni lissage d'une force critique,
ni compacité forte, ni contrôle de la pression non locale. Dans l'application
d'Albritton–Barker, l'équation (24) est bien la Navier–Stokes incompressible
3D standard, mais le correcteur intervient après sélection d'une région
régulière et ne produit pas une régularité globale.

**Résidu Clay :** montrer que chaque entrée réelle du correcteur appartient à
l'échelle supportée, annule la masse, n'engendre pas de delta de bord après
extension par zéro, puis contrôler la somme complète de la force localisée
dans une classe espace-temps pertinente.

## 11. Sources primaires et empreintes SHA256

Les empreintes ci-dessous portent sur les octets PDF effectivement audités le
15 août 2026. Elles permettent de détecter une modification ultérieure du
fichier servi; elles ne certifient pas à elles seules l'identité éditoriale.

| source PDF primaire | version/état | octets | SHA256 |
|---|---:|---:|---|
| `https://arxiv.org/pdf/0808.2614` | Costabel–McIntosh v2 | 237140 | `B0D388C55DEBA9ED916EAAC56906DD49C6CA34EEE322679A7F7ABF2D7457D53B` |
| `https://arxiv.org/pdf/2107.09573` | Saari–Schwarzacher v3 | 596233 | `5B7412E349E1AA0F2B33783D9BF65F7480E38813443996D3AE01B9B0147267F4` |
| `https://arxiv.org/pdf/1811.00507` | Albritton–Barker v2 | 476336 | `FDD91E657B5CF503286B4E45CC084C12C8B202AAF24BCDAD67EDEA46EDFA4102` |
| `https://arxiv.org/pdf/1906.02713` | Tolksdorf–Watanabe v1 | 351488 | `1A03464CD45E70F4589C75B2C93C954511D8CE8FE441791F5134829A7B022565` |
| `https://arxiv.org/pdf/2509.04617` | Isett–Mao–Oh–Tao v1, prépublication | 1156634 | `B54A8E6C0AB71491C58B8D07A41FAF56F4976AD5B303E4686DBDB39845C4BB41` |
| `https://arxiv.org/pdf/2602.21925` | Chan–Chen–Su v1, prépublication | 532512 | `AD351C254C8BAB7C7F1CC058A77DFB62975BB827D93E319C727EBF8EE9A825D0` |

Autres sources primaires vérifiées par leur version éditeur ou leur texte
auteur, sans figer ici les octets d'une copie tierce :

- Geißert–Heck–Hieber 2006, DOI `10.1007/3-7643-7601-5_7`;
- Borchers–Sohr 1990, DOI `10.14492/hokmj/1381517172`;
- Galdi 2011, DOI `10.1007/978-0-387-09620-9`;
- Costabel–McIntosh 2010, DOI `10.1007/s00209-009-0517-8`;
- Tolksdorf–Watanabe 2020, DOI `10.1016/j.jde.2020.04.015`;
- Albritton–Barker 2020, DOI `10.1016/j.jde.2020.06.009`;
- Saari–Schwarzacher 2023, DOI `10.1007/s40818-023-00150-z`.

## Conclusion

Le raccord requis par la dérivation principale est valide :

\[
\boxed{\mathcal B:W^{-1,4/3}_0(A)\to L^{4/3}(A)}
\]

est un résultat publié, avec
(W^{-1,4/3}_0=(W^{1,4}(A))'\) et condition de masse nulle. Le contrôle du
commutateur laplacien ne vient toutefois pas de cette seule flèche. Il devient
disponible en fixant l'opérateur supporté de Costabel–McIntosh, d'ordre
pseudodifférentiel (-1); alors
([\Delta,\mathcal B]\in\Psi^0\) est un corollaire falsifiable du calcul
symbolique.

Le point non couvert demeure toute formulation qui remplace silencieusement
l'échelle supportée/Dirichlet complète par le grand espace intrinsèque
((W^{2,p'}_0(A))'\), ou qui transforme la borne Lorentz en forme divergence
en borne sur un Sobolev–Lorentz abstrait. C'est ce quantificateur, et non
l'existence classique de Bogovskiĭ, qui doit rester explicitement ouvert dans
le cycle 0043.
