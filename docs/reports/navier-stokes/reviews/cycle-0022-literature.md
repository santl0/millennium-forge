# Cycle 0022 — veille primaire sur profils non récurrents et solutions anciennes

Date de coupure : **2026-08-14**.
Périmètre : Navier–Stokes incompressible 3D, profils critiques de vorticité non récurrents ou rectifiés logarithmiquement, direction asymptotiquement constante, solutions anciennes et théorèmes d'exclusion auto-similaires.
Type de revue : bibliographie primaire ciblée, produite par la même famille de modèle que l'agent principal ; **pas** une validation indépendante des preuves.

## Verdict différentiel

La veille ne révèle **aucun résultat primaire nouveau qui ferme le verrou général**

\[
\boldsymbol\omega(x,t)\simeq |x-x_*(t)|^{-2}
\Phi(x,t)\xi(x,t),
\qquad
\xi(x,t)=e+O\!\left(\frac1{|\log |x-x_*||}\right),
\]

lorsque le profil est non récurrent, multi-échelle, sans limite périodique en temps logarithmique, ou Type II. Les théorèmes publiés d'exclusion self-similaire exigent une invariance exacte, une périodicité en variables similaires, ou une convergence forte vers un tel profil. Les théorèmes de Liouville pour solutions anciennes restent partiels : axisymétrie, bornitude/mildness, faible-\(L^3\), stationnarité ou hypothèses de décroissance.

Il existe toutefois une **porte déjà présente dans le registre, plus forte que la récurrence**, qui réduit substantiellement le verrou. Le préprint de Lei–Ren–Tian [arXiv:2501.08976v1](https://arxiv.org/abs/2501.08976) affirme que, pour une solution faible adaptée locale, le confinement de toute vorticité forte dans un double cône fixe implique la régularité. Par conséquent :

> Un profil log-rectifié dont toutes les directions de forte vorticité convergent uniformément, dans l'espace-temps, vers un axe fixe \(\{\pm e\}\), et dont la vorticité est uniformément bornée hors de ce cœur, tombe déjà sous ce critère.

Cette implication est élémentaire et explicite ci-dessous. Elle est conditionnée à la validité du préprint v1, qui n'est ni publié ni reproduit indépendamment ici. Le sous-problème véritablement non couvert doit donc rompre au moins une de ces propriétés : axe fixe, uniformité espace-temps, confinement de tous les grands niveaux, unicité du cœur, ou classe de solution faible adaptée.

## 1. Objet mathématique visé

Le profil statique du cycle 0021 a montré que la récurrence exacte par dilatation est incompatible avec une direction globale dans \(\mathrm{bmo}_{1/|\log r|}\), sauf direction constante, elle-même incompatible avec une singularité ponctuelle solénoïdale non triviale. Le pivot naturel est une famille non homogène

\[
W(r,\theta,s)
=r^{-2}\Phi(r,\theta,s)\xi(r,\theta,s),
\qquad
\nabla\cdot W=0,
\]

où \(s=-\log(T-t)\) ou \(s=\log(1/r)\), et où la direction se rectifie :

\[
\sup_{\theta}|\xi(r,\theta,s)-e|
\le \frac{C}{1+|\log(r/R_*)|}.
\tag{1}
\]

Cette écriture ne définit pas encore un scénario Navier–Stokes. Il faut distinguer :

- une loi spatiale à un temps fixé ;
- une famille pré-singulière uniforme pour \(t<T\) ;
- une limite après remise à l'échelle ;
- une solution ancienne limite ;
- une simple asymptotique de magnitude, sans équation pour le champ vectoriel.

La veille cherche des théorèmes dont les hypothèses recouvrent réellement l'une de ces notions. Le mot « profil » dans les sources auto-similaires désigne généralement la **vitesse** en variables similaires, et non directement la magnitude scalaire de la vorticité.

## 2. Résultat géométrique le plus proche : le double cône

### Source et statut

Zhen Lei, Xiao Ren et Gang Tian, *A Geometric Characterization of Potential Navier-Stokes Singularities*, [arXiv:2501.08976v1](https://arxiv.org/abs/2501.08976), soumis le 15 janvier 2025.

- **Statut au 2026-08-14 :** prépublication v1 ; aucune v2 ni référence de revue affichée.
- **Équation :** Navier–Stokes incompressible 3D, viscosité \(1\), force nulle.
- **Domaine :** cylindre intérieur \(Q(1)=B(1)\times(-1,0)\).
- **Solution :** solution faible adaptée locale : énergies locales finies, \(p\in L^{3/2}_{\mathrm{loc}}\), équations distributionnelles et inégalité locale d'énergie.

Le théorème 1.1 suppose qu'il existe \(e\in\mathbb S^2\) et \(\delta,M>0\) tels qu'en chaque point régulier de \(Q(1)\),

\[
|\omega(x,t)|\le M
\quad\text{ou}\quad
|\xi(x,t)\times e|\le 1-\delta.
\tag{2}
\]

Il conclut que la solution est régulière dans \(\overline{Q(1/2)}\). La source n'impose pas que l'angle du double cône soit petit. Son corollaire 1.5 reformule la contraposée : au voisinage d'un point singulier, l'ensemble limite des directions de grande vorticité doit rencontrer tout grand cercle de \(\mathbb S^2\).

### Lemme de transfert vers une direction asymptotiquement constante

**Inférence à partir du théorème 1.1, pas énoncé textuel de la source.** Supposons qu'il existe \(e\in\mathbb S^2\), \(r_0>0\), \(M<\infty\) et \(0<\eta<1\) tels que, uniformément pour les temps considérés,

\[
|x-x_*|<r_0,\quad |\omega(x,t)|>M
\Longrightarrow |\xi(x,t)-\sigma(x,t)e|\le\eta
\]

pour un signe \(\sigma(x,t)\in\{-1,+1\}\), et que \(|\omega|\le M\) sur les points réguliers de \(Q(1)\) hors de ce cœur. Alors

\[
|\xi\times e|
=|(\xi-\sigma e)\times e|
\le |\xi-\sigma e|
\le\eta=1-\delta,
\]

avec \(\delta=1-\eta>0\). L'hypothèse (2) est satisfaite.

Si (1) vaut uniformément, on choisit \(r_0\) assez petit pour que

\[
\frac{C}{1+|\log(r_0/R_*)|}<1.
\]

Le taux logarithmique n'est donc pas borderline pour ce théorème : **toute convergence uniforme vers un axe fixe suffit**, même arbitrairement lente.

### Ce qui échappe encore au double cône

Le transfert échoue si :

- \(e=e(t)\) ou \(e=e(r)\) explore des axes sans cône fixe ;
- la convergence n'est que presque partout, en moyenne, ou tranche par tranche, sans contrôle de toute la région de forte vorticité ;
- des îlots éloignés de grande vorticité portent d'autres directions ;
- plusieurs cœurs ont des axes dont l'union rencontre tous les grands cercles ;
- la direction approche \(e\) à un temps isolé, sans uniformité sur un cylindre ;
- l'objet limite n'est pas une solution faible adaptée Navier–Stokes ;
- le zoom Type II produit Euler plutôt que Navier–Stokes.

Ainsi, « direction asymptotiquement constante » doit être quantifiée avant d'être annoncée comme une classe ouverte. La version uniforme et mono-cœur est déjà conditionnellement exclue par Lei–Ren–Tian.

## 3. Critères publiés portant sur la direction

### Constantin–Fefferman et Beirão da Veiga–Berselli

Les critères classiques imposent un contrôle par paires dans la région de grande vorticité. La source primaire du premier critère est Peter Constantin et Charles Fefferman, *Direction of Vorticity and the Problem of Global Regularity for the Navier–Stokes Equations*, *Indiana University Mathematics Journal* 42(3) (1993), 775–789, [DOI 10.1512/iumj.1993.42.42034](https://doi.org/10.1512/iumj.1993.42.42034) :

\[
|\xi(x,t)\times\xi(y,t)|
\lesssim |x-y|
\]

dans Constantin–Fefferman, puis à l'exposant \(1/2\) dans H. Beirão da Veiga et L. C. Berselli, *On the regularizing effect of the vorticity direction in incompressible viscous flows*, *Differential and Integral Equations* 15 (2002), 345–356, [DOI 10.57262/die/1356060864](https://doi.org/10.57262/die/1356060864), [PDF auteur](https://people.dm.unipi.it/beiraodaveiga/pdf/hbv-79.pdf).

- **Statut :** articles publiés.
- **Équation :** NS incompressible 3D sur \(\mathbb R^3\), visqueux, cadre Leray–Hopf rendu fort par le critère.
- **Transfert :** la seule amplitude \(O(1/|\log r|)\) vers un axe ne fournit pas une semi-norme \(C^{1/2}\). Par exemple, une variation radiale logarithmique peut avoir un gradient d'ordre \(1/(r|\log r|^2)\).
- **Clay :** critères conditionnels ; aucune estimation de leur module depuis l'énergie.

### Giga–Miura

Yoshikazu Giga et Hideyuki Miura, *On Vorticity Directions near Singularities for the Navier-Stokes Flows with Infinite Energy*, *Communications in Mathematical Physics* 303 (2011), 289–300, [DOI 10.1007/s00220-011-1197-x](https://doi.org/10.1007/s00220-011-1197-x), [version auteur](https://eprints.lib.hokudai.ac.jp/dspace/bitstream/2115/69763/1/pre956.pdf).

- **Statut :** publié.
- **Équation/domaine :** NS incompressible 3D sur \(\mathbb R^3\), force nulle, solution mild lisse et bornée, énergie éventuellement infinie.
- **Hypothèse compensatrice :**
  \[
  \sup_{0<t<T}(T-t)^{1/2}\|u(t)\|_\infty<\infty
  \]
  et continuité spatiale uniforme de la direction dans la région de forte vorticité, uniformément près de \(T\).
- **Conclusion :** prolongement au temps \(T\).

Une convergence uniforme de \(\xi\) vers un même axe sur toute la région active fournit la petite oscillation nécessaire près du cœur, mais il faut encore contrôler uniformément la région de forte vorticité hors du cœur. Ce résultat ne traite pas Type II. La revendication plus récente de Lei–Ren–Tian couvre une géométrie de double cône plus large dans la classe faible adaptée, mais reste un préprint v1 ; Giga–Miura demeure le résultat publié sous hypothèse Type I.

### Grujić 2026

Zoran Grujić, *Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier-Stokes Equations*, [arXiv:2607.08866v2](https://arxiv.org/abs/2607.08866), révisé le 13 juillet 2026.

- **Statut :** prépublication v2, non publiée.
- **Hypothèses annoncées :** \(\omega\in L^\infty_tL^{3/2,\infty}_x\), direction globale uniforme dans \(\mathrm{bmo}_{1/|\log r|}\), profil ponctuel critique.
- **Lien :** une borne ponctuelle uniforme \(|\xi-e|\lesssim1/|\log r|\) contrôle l'oscillation moyenne sur les boules centrées au cœur, mais ne produit pas automatiquement la norme globale en tous centres, la convention aux zéros, ni l'uniformité temporelle.
- **Statut de transfert :** conditionnel et déjà audité avec réparations dans les cycles 0014–0021 ; ce préprint ne construit pas le profil log-rectifié.

## 4. Exclusions self-similaires : ce qu'elles couvrent exactement

### Tableau primaire

| Source | Statut | Équation / solution | Récurrence exigée | Conclusion | Trou restant |
|---|---|---|---|---|---|
| Nečas–Růžička–Šverák, *Acta Math.* 176 (1996), [DOI 10.1007/BF02551584](https://doi.org/10.1007/BF02551584) | publié | NS 3D, \(\mathbb R^3\), profil backward exact | stationnaire en temps similaire ; profil \(L^3\) | profil trivial | pas DSS, non récurrent, Type II |
| Tsai, *Arch. Rational Mech. Anal.* 143 (1998), [DOI 10.1007/s002050050099](https://doi.org/10.1007/s002050050099) | publié | NS 3D, \(\mathbb R^3\), solution self-similaire avec estimations locales d'énergie | stationnaire exacte | exclusion dans une classe locale-énergie plus large | pas de dérive non périodique |
| Chae, *Math. Ann.* 338 (2007), [DOI 10.1007/s00208-007-0082-6](https://doi.org/10.1007/s00208-007-0082-6), [arXiv:math/0604234](https://arxiv.org/abs/math/0604234) | publié | NS 3D classique avant \(T\), \(\mathbb R^3\) | convergence locale en \(L^q\) vers un profil self-similaire | exclusion sous les normes/intégrabilités prescrites | la convergence vers un profil est une hypothèse |
| Hou–Li, *DCDS* 18 (2007), [DOI 10.3934/dcds.2007.18.637](https://doi.org/10.3934/dcds.2007.18.637) | publié | NS 3D classique, local autour du point | profil local self-similaire avec convergence \(L^p,\ p>3\) | exclusion | pas endpoint faible ni profil sans limite |
| Chae, *Nonlinear Analysis* 125 (2015), 251–259, [DOI 10.1016/j.na.2015.05.026](https://doi.org/10.1016/j.na.2015.05.026), [arXiv:1306.0305v5](https://arxiv.org/abs/1306.0305) | publié | NS 3D classique avant blow-up | profil limite périodique en temps similaire, \(C^1(\mathbb R;L^3\cap C^2)\) | pas de blow-up localement asymptotiquement DSS | ne couvre pas une dérive sans orbite périodique |
| Chae–Wolf, *CPDE* 42 (2017), 1359–1374, [DOI 10.1080/03605302.2017.1358275](https://doi.org/10.1080/03605302.2017.1358275), [arXiv:1610.09464](https://arxiv.org/abs/1610.09464) | publié | NS 3D, solution \(\lambda\)-DSS dans \(L^p\), \(p\ge3\), et application à une solution classique | DSS exacte ou convergence vers une fonction DSS | singularité DSS supprimée pour \(\lambda\) proche de \(1\) sous borne Type I ; exclusion asymptotique correspondante | \(\lambda\) général et non-récurrence |
| Pineau–Vicol, [arXiv:2607.09619v2](https://arxiv.org/abs/2607.09619) | préprint v2, 6 août 2026 | NS 3D lisse, \(\mathbb R^3\times[-1,0)\), borne Type I | RSS/RDSS exacte ; quasi-auto-similarité quantitative à une tranche pour un critère local | rotation petite ou grande ; RDSS avec facteur proche de \(1\) ; critère local supplémentaire | rotation intermédiaire, Type II, dérive apériodique |

### Conséquence pour un profil log-rectifié

En variables similaires \(y=x/\sqrt{T-t}\), \(s=-\log(T-t)\), une correction logarithmique peut devenir une dérive lente en \(s\). Trois situations doivent être séparées :

1. \(U(y,s)\to U_*(y)\) : les exclusions asymptotiquement self-similaires peuvent s'appliquer si la convergence est dans leurs normes.
2. \(U(y,s)\to U_*(y,s)\) avec \(U_*\) périodique : Chae 2015 ou Chae–Wolf 2017 peuvent s'appliquer sous leurs classes.
3. \(U(y,s)\) dérive sans limite ni orbite périodique : aucune des exclusions du tableau ne s'applique directement.

La seule petitesse d'un défaut de récurrence,

\[
\|U(s+S)-U(s)\|_X\longrightarrow0,
\]

ne produit pas automatiquement une orbite périodique limite. Il faut une précompacité dans \(X\), une extraction, la stabilité de l'équation et une identification de toutes les limites. Aucune source primaire trouvée ne fournit ce paquet pour la classe faible-\(L^3\)/faible-\(L^{3/2}\) non axisymétrique visée.

## 5. Solutions anciennes et rigidité

### Koch–Nadirashvili–Seregin–Šverák

Gabriel Koch, Nikolai Nadirashvili, Gregory Seregin et Vladimir Šverák, *Liouville theorems for the Navier–Stokes equations and applications*, *Acta Mathematica* 203 (2009), 83–105, [DOI 10.1007/s11511-009-0039-6](https://doi.org/10.1007/s11511-009-0039-6), [arXiv:0709.3599](https://arxiv.org/abs/0709.3599).

- **Statut :** publié.
- **Équation :** NS incompressible, non forcé, sur \(\mathbb R^n\times(-\infty,0)\).
- **Notions :** solutions anciennes faibles bornées et solutions anciennes mild bornées, soigneusement distinguées.
- **Résultat :** rigidité complète en 2D selon la notion, résultats partiels axisymétriques 3D, et route blow-up \(\to\) solution ancienne.
- **Obstacle :** le Liouville général pour toute solution ancienne mild bornée 3D demeure hors de portée. Sans mildness, les champs parasites \(u=b(t)\), \(p=-b'(t)\cdot x\) interdisent une formulation naïve.

Un profil log-rectifié non récurrent pourrait produire une ancienne non stationnaire. KNSS ne la force pas à être nulle dans la classe 3D générale.

### Lei–Zhang–Zhao

Zhen Lei, Qi S. Zhang et Na Zhao, *Improved Liouville theorems for axially symmetric Navier-Stokes equations*, [arXiv:1701.00868v1](https://arxiv.org/abs/1701.00868), publication/traduction référencée par [DOI 10.1360/N012016-00149](https://doi.org/10.1360/N012016-00149).

- **Statut :** publié ; arXiv v1 est la traduction anglaise.
- **Solution :** ancienne mild lisse, axisymétrique.
- **Résultats :** rigidité sous décroissance/growth de vorticité dans le cas sans swirl ; avec swirl, rigidité des solutions anciennes mild bornées si \(\Gamma=rv_\theta\in L^\infty_tL^p_x\), \(1\le p<\infty\).
- **Trou :** ni profil général non axisymétrique, ni simple convergence de direction vers un axe.

### Ożański–Palasek

W. S. Ożański et S. Palasek, *Quantitative Control of Solutions to the Axisymmetric Navier-Stokes Equations in Terms of the Weak \(L^3\) Norm*, *Annals of PDE* 9, article 15 (2023), [DOI 10.1007/s40818-023-00156-7](https://doi.org/10.1007/s40818-023-00156-7), [arXiv:2210.10030](https://arxiv.org/abs/2210.10030).

- **Statut :** publié, accès ouvert.
- **Équation/solution :** NS 3D incompressible non forcé sur \(\mathbb R^3\), solution classique forte axisymétrique.
- **Théorème principal :** une borne \(L^\infty_tL^{3,\infty}_x\) donne des bornes quantitatives sur toutes les dérivées.
- **Corollaire annoncé dans le texte publié :** absence de solution ancienne axisymétrique non triviale dans \(L^\infty_tL^{3,\infty}_x\).
- **Transfert :** exclut tout profil critique de vitesse dans cette classe **si l'axisymétrie complète et la norme uniforme faible-\(L^3\) passent au zoom**. Il ne s'applique pas à une géométrie simplement proche d'un axe.

### Unicité rétrograde avec donnée finale

Zhen Lei, Zhaojie Yang et Cheng Yuan, *Backward Uniqueness for 3D Navier–Stokes Equations With Non-Trivial Final Data and Applications*, *IMRN* 2024, 13417–13431, [DOI 10.1093/imrn/rnae208](https://doi.org/10.1093/imrn/rnae208), [arXiv:2311.02429v1](https://arxiv.org/abs/2311.02429).

- **Statut :** publié.
- **Classe :** deux solutions mild bornées sur un intervalle fini fermé, vorticités bornées, même force, même donnée finale.
- **Conclusion :** les vitesses et gradients de pression coïncident.
- **Limite :** le théorème ne construit ni la trace terminale bornée, ni la solution ancienne, ni la bornitude de sa vorticité. Un profil critique \(r^{-2}\) ne satisfait pas directement cette dernière.

## 6. Type II : les limites récentes sont souvent Euler

Les sources de Gregory Seregin restent inchangées au jour de coupure :

| Source | Version au 2026-08-14 | Objet limite | Portée |
|---|---|---|---|
| [arXiv:2606.29468v1](https://arxiv.org/abs/2606.29468), soumis le 28 juin 2026 | préprint v1 | anciennes Euler via zoom à échelle Euler | scénarios Type II locaux conditionnels |
| [arXiv:2402.13229v3](https://arxiv.org/abs/2402.13229), révisé le 8 août 2026 | préprint v3 | ancienne Euler dissipative, axisymétrique sans swirl | sous-scénario axisymétrique et bornes supplémentaires |
| [arXiv:2507.08733v2](https://arxiv.org/abs/2507.08733), révisé le 3 janvier 2026 | préprint v2 | anciennes Euler avec bornes pondérées | exclusions conditionnelles de sous-classes self/DSS |

Le terme visqueux disparaît dans ces zooms. Les théorèmes de Liouville KNSS, Lei–Zhang–Zhao ou Ożański–Palasek portent sur Navier–Stokes et ne se transfèrent donc pas. Réciproquement, une rigidité Euler conditionnelle n'exclut pas un Type II général si les fonctionnelles pondérées ne sont pas contrôlées depuis l'énergie Clay.

## 7. Autres sources récentes vérifiées

| Source | Statut au 2026-08-14 | Résultat pertinent | Pourquoi le verrou reste |
|---|---|---|---|
| Wang–Yang, [arXiv:2608.06040v1](https://arxiv.org/abs/2608.06040), 6 août 2026 | préprint v1 | décroissance et Liouville pour \(D\)-solutions **stationnaires**, avec ou sans axisymétrie selon les théorèmes | stationnarité et décroissance à l'infini ; pas une ancienne non stationnaire issue d'un zoom |
| Binz–Coiculescu, [arXiv:2607.12159v1](https://arxiv.org/abs/2607.12159), 13 juillet 2026 | préprint v1 | Liouville pour profils homothétiques **forward** suffisamment réguliers ; lien à non-unicité faible | direction temporelle forward et donnée homogène singulière |
| Pineau–Vicol, [arXiv:2607.09619v2](https://arxiv.org/abs/2607.09619), 6 août 2026 | préprint v2 | RSS/RDSS backward Type I et critère local quasi-auto-similaire | impose une orbite structurée ou une proximité quantitative à une tranche |
| Barker, [arXiv:2510.20757v3](https://arxiv.org/abs/2510.20757), 11 août 2026 | préprint v3 | classifications quantitatives pour solutions approximativement axisymétriques ; v3 ajoute un raccord blow-up gauche/droite | ne produit ni Liouville général ni profil log-rectifié |
| Grujić, [arXiv:2607.08866v2](https://arxiv.org/abs/2607.08866), 13 juillet 2026 | préprint v2 | exclusion conditionnelle annoncée sous faible-\(L^{3/2}\) et log-BMO de la direction | hypothèses critiques non produites depuis Clay ; profil non construit |

Aucune révision plus récente de ces notices n'a été observée. Une recherche primaire ciblée du 12 au 14 août 2026 n'a identifié aucun nouveau préprint NS 3D sur profil ancien, self-similaire ou log-rectifié.

## 8. Calculs et modèles voisins

La recherche n'a identifié **aucun calcul certifié** construisant ou excluant un profil non récurrent de vorticité NS 3D avec :

\[
|\omega|\sim r^{-2},
\qquad
\xi\to e\ \text{à taux logarithmique},
\qquad
\nabla\cdot\omega=0,
\]

et un résidu Navier–Stokes continu borné.

Le calcul de Hou, *Potentially Singular Behavior of the 3D Navier–Stokes Equations*, *FoCM* 23 (2023), [DOI 10.1007/s10208-022-09578-4](https://doi.org/10.1007/s10208-022-09578-4), reste une simulation adaptative d'un scénario axisymétrique avec swirl dans un cylindre à frontière radiale, non une preuve et non un profil \(\mathbb R^3\) Clay. Les calculs de profils forward à donnée homogène singulière ou les singularités assistées par IA dans Euler/modèles réduits ne transfèrent pas au verrou présent.

## 9. Implication exacte vers Clay

Pour une solution issue d'une donnée Clay lisse, divergence-free et rapidement décroissante sur \(\mathbb R^3\), le raccord le plus direct serait :

\[
\begin{aligned}
&\text{premier point singulier }(x_*,T)
+\text{ solution faible adaptée locale}\\
&+\ \exists e,M,\delta>0\ \text{tels que toute vorticité } >M
\text{ reste dans le double cône de }e\\
&\Longrightarrow \text{régularité locale, contradiction},
\end{aligned}
\]

selon Lei–Ren–Tian v1.

Une version uniforme de (1), jointe à la concentration de **tous** les grands sur-niveaux dans le cœur, fournit le deuxième maillon. Elle ne résout pas Clay car aucune estimation issue des données générales ne produit cette convergence directionnelle.

Les exclusions self-similaires donnent seulement

\[
\text{blow-up}
+\text{ convergence vers profil stationnaire/périodique admissible}
\Longrightarrow \text{contradiction}.
\]

Elles ne fournissent pas la convergence. Les routes par solutions anciennes donnent

\[
\text{blow-up}
+\text{ borne critique compacte}
\Longrightarrow \text{ancienne non triviale},
\]

mais la rigidité générale de cette ancienne manque, et Type II peut produire Euler. Aucun de ces résultats ne constitue une résolution positive ou négative du problème Clay.

## 10. Sources primaires à ajouter ultérieurement au registre

Le fichier **sources.json** n'a pas été modifié, conformément au périmètre de cette tâche. Quatre entrées publiées sont directement pertinentes et devraient être enregistrées lors d'un prochain cycle de maintenance :

1. Chae 2015, [DOI 10.1016/j.na.2015.05.026](https://doi.org/10.1016/j.na.2015.05.026), asymptotique DSS.
2. Chae–Wolf 2017, [DOI 10.1080/03605302.2017.1358275](https://doi.org/10.1080/03605302.2017.1358275), DSS proche de l'identité.
3. Giga–Miura 2011, [DOI 10.1007/s00220-011-1197-x](https://doi.org/10.1007/s00220-011-1197-x), direction uniformément continue sous Type I.
4. Ożański–Palasek 2023, [DOI 10.1007/s40818-023-00156-7](https://doi.org/10.1007/s40818-023-00156-7), faible-\(L^3\) axisymétrique et corollaire ancien.

## 11. Décision scientifique

- **Résultat différentiel positif :** la direction asymptotiquement constante uniforme n'est pas un sous-cas neuf libre ; avec confinement complet des grands niveaux, elle implique le double cône de Lei–Ren–Tian.
- **Résultat différentiel négatif :** aucune source primaire ne traite un profil critique non récurrent dont l'image directionnelle échappe à tout double cône fixe, sans limite périodique et sans axisymétrie.
- **Statut des preuves :** les exclusions classiques, Chae 2015, Chae–Wolf 2017, Giga–Miura 2011, KNSS 2009 et Ożański–Palasek 2023 sont publiées ; Lei–Ren–Tian, Pineau–Vicol, Seregin 2025–2026, Wang–Yang, Binz–Coiculescu, Barker et Grujić restent des prépublications aux versions indiquées.
- **Calcul :** aucune certification pertinente trouvée.
- **Écart Clay :** absence de lemme forçant, depuis l'énergie et l'équation, soit un cône fixe de directions, soit une orbite compacte stationnaire/périodique en variables similaires.
- **État :** **CONTINUER**, mais reformuler **GAP-LOG-RECTIFIED-PROFILE** comme :

\[
\boxed{
\begin{gathered}
\text{profil critique vectoriel, non récurrent, solution-admissible,}\\
\text{dont les directions de forte vorticité ne sont contenues}\\
\text{dans aucun double cône fixe sur un cylindre espace-temps.}
\end{gathered}}
\]

- **Prochain test bibliographique/mathématique décisif :** vérifier si la contrainte solénoïdale et une rectification logarithmique mono-cœur forcent automatiquement un double cône uniforme ; si oui, cet axe est déjà conditionnellement fermé par Lei–Ren–Tian, et le prochain profil adverse doit avoir un axe errant ou plusieurs cœurs tout en conservant la norme faible-\(L^{3/2}\), la pression et l'énergie locale.

## Post-scriptum de synthèse

Après remise de cette veille indépendante, l'agent principal a intégré les
quatre sources signalées sous les identifiants `NS-SRC-0085` à `0088`. Cette
note documente la résolution de la dette bibliographique; elle ne modifie ni
le verdict scientifique ni la provenance de la revue.
