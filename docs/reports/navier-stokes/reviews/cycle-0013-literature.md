# Cycle 0013 — veille primaire : direction de la vorticité et déplétion du vortex stretching

Date de coupure : **2026-08-14**
Périmètre : équations de Navier–Stokes incompressibles 3D, non forcées, principalement sur \(\mathbb R^3\), avec une section séparée sur Euler 3D et sur les résultats locaux.
Statut : audit bibliographique et contradictoire ; aucune affirmation nouvelle de ce document n'est une preuve papier.

## 1. Conclusion exécutable

Les critères géométriques classiques ne disent pas que le terme ponctuel

\[
  \omega(x,t)\cdot S(x,t)\omega(x,t)
\]

est négatif, ni même non positif lorsque les directions de vorticité voisines sont alignées. Ils exploitent une annulation angulaire dans une **intégrale singulière non locale**, puis contrôlent une norme ou un bilan d'enstrophie. Un énoncé universel de signe ponctuel est faux : on peut conserver exactement la même vorticité, donc une direction parfaitement constante, dans une boule, tout en modifiant le strain dans cette boule par une vorticité située dans un anneau extérieur.

La veille primaire 2025–2026 ajoute trois objets à suivre :

1. Lei–Ren–Tian, arXiv:2501.08976v1 (2025), obtiennent un critère local pour solutions faibles adaptées : dans les régions de forte vorticité, confiner les vecteurs vorticité dans un double cône fixe implique la régularité. C'est un vrai changement de géométrie, sans module de continuité spatial, mais encore une hypothèse conditionnelle.
2. Yu, arXiv:2606.27560v1 (2026), donne des estimations exactes à échelle filtrée. Le stretching proche est absorbé par la diffusion filtrée, mais il reste explicitement des pertes de filtre, le strain lointain, les commutateurs et les résidus de localisation. Ce n'est pas une fermeture globale.
3. Grujić, arXiv:2607.08866v2 (2026), annonce l'exclusion d'un scénario de singularité ponctuelle critique sous une hypothèse uniforme \(L^{3/2,\infty}\) sur la vorticité et \(\mathrm{bmo}_{1/|\log r|}\) sur sa direction. C'est une prépublication très récente, non encore validée indépendamment dans cette veille, et son théorème ne couvre pas un blow-up Clay général.

Le maillon falsifiable recommandé est donc :

> **Lemme local à réfuter.** Une bonne cohérence de \(\xi=\omega/|\omega|\) dans une boule impose un signe, ou une petite valeur ponctuelle, à \(\alpha=\xi\cdot S\xi\) au centre.

Ce lemme est faux par non-localité. Le test adverse analytique de la section 8 le réfute sans contredire Constantin–Fefferman, Beirão da Veiga–Berselli, Grujić, Giga–Miura ou Lei–Ren–Tian.

## 2. Équation, solutions et échelle

Dans le cadre principal,

\[
\begin{cases}
\partial_t u-\nu\Delta u+(u\cdot\nabla)u+\nabla p=0,\\
\nabla\cdot u=0,
\end{cases}
\qquad (x,t)\in\mathbb R^3\times(0,T),\qquad \nu>0,
\]

avec \(\omega=\nabla\times u\), \(S=(\nabla u+\nabla u^{\mathsf T})/2\), et

\[
  \partial_t\omega-\nu\Delta\omega+(u\cdot\nabla)\omega=S\omega.
\]

Pour une solution forte suffisamment décroissante,

\[
 \frac12\frac{d}{dt}\|\omega(t)\|_2^2
 +\nu\|\nabla\omega(t)\|_2^2
 =\int_{\mathbb R^3}\omega\cdot S\omega\,dx.
\]

La loi d'échelle est

\[
u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),\quad
p_\lambda(x,t)=\lambda^2p(\lambda x,\lambda^2t),\quad
\omega_\lambda(x,t)=\lambda^2\omega(\lambda x,\lambda^2t).
\]

Donc :

- \(\xi=\omega/|\omega|\) est invariant ;
- \(S_\lambda=\lambda^2S(\lambda x,\lambda^2t)\) ;
- \(\omega\cdot S\omega\) est ponctuellement d'homogénéité \(6\), et son intégrale spatiale d'homogénéité \(3\) ;
- \(\|\omega\|_2^2\) est d'homogénéité \(1\) ;
- \(\|\omega\|_{L^{3/2,\infty}}\) est critique ;
- un coefficient de cohérence \(|\xi(x)-\xi(y)|\le C|x-y|^\beta\) a dimension \(L^{-\beta}\) et n'est uniforme sous zoom que s'il est renormalisé ;
- \((T-t)\|\omega(t)\|_\infty\) et \((T-t)^{1/2}\|u(t)\|_\infty\) sont des quantités Type I invariantes.

Les énoncés ci-dessous distinguent : solution de Leray–Hopf ou faible adaptée, solution forte avant un temps candidat, solution mild bornée, et solution classique d'Euler. Ces catégories ne sont pas interchangeables.

## 3. Le mécanisme non local exact

Sur \(\mathbb R^3\), pour un champ suffisamment régulier et décroissant,

\[
 u(x)=\frac1{4\pi}\int_{\mathbb R^3}
 \omega(y)\times\frac{x-y}{|x-y|^3}\,dy.
\]

La représentation de Calderón–Zygmund du strain est

\[
S(x)=\frac{3}{8\pi}\operatorname{p.v.}\!\int_{\mathbb R^3}
\frac{(\widehat z\times\omega(x-z))\otimes\widehat z
+\widehat z\otimes(\widehat z\times\omega(x-z))}{|z|^3}\,dz.
\]

En posant \(\xi=\omega/|\omega|\) sur \(\{\omega\ne0\}\) et
\(\alpha=\xi\cdot S\xi\), Constantin obtient

\[
\alpha(x)=\frac{3}{4\pi}\operatorname{p.v.}\!\int_{\mathbb R^3}
D(\widehat y,\xi(x+y),\xi(x))|\omega(x+y)|\frac{dy}{|y|^3},
\]

où

\[
D(a,b,c)=(a\cdot c)\det(a,b,c),\qquad
|D(\widehat y,\xi(x+y),\xi(x))|
\le |\xi(x+y)\times\xi(x)|.
\]

Cette formule implique :

- l'alignement **ou l'anti-alignement** annule le noyau géométrique ;
- une cohérence \(C|y|^\beta\) adoucit \(|y|^{-3}\) en \(|y|^{-3+\beta}\) ;
- les preuves majorent la valeur absolue de l'intégrale ou son apport intégré ; elles ne fixent pas son signe ;
- \(S(x)\), donc \(\alpha(x)\), dépend de toute la vorticité, pas seulement du jet local de \(\xi\).

La pression est elle aussi non locale, mais elle disparaît de l'équation de vorticité après curl. Elle réapparaît dans les arguments locaux sur \(u\), les solutions faibles adaptées et les passages à la limite. Le caractère non local pertinent ici est déjà présent dans \(S=\mathcal T\omega\).

## 4. Résultats établis et quantificateurs exacts

### 4.1 Constantin–Fefferman (1993) — Lipschitz dans la zone de forte vorticité

**Source primaire.** Peter Constantin et Charles Fefferman, “Direction of Vorticity and the Problem of Global Regularity for the Navier–Stokes Equations”, *Indiana University Mathematics Journal* **42**(3), 775–789 (1993), DOI [10.1512/iumj.1993.42.42034](https://doi.org/10.1512/iumj.1993.42.42034), [notice du journal](https://iumj.org/article/3627/).

**Cadre.** Navier–Stokes incompressible 3D, \(\mathbb R^3\), \(\nu>0\), sans force ni frontière. Le résultat est formulé pour une solution faible de type Leray, déjà forte avant le temps terminal considéré, avec donnée \(H^1\) ; la preuve originale utilise en outre le contrôle \(L^1\) de la vorticité issu de \(\omega_0\in L^1\).

**Hypothèse géométrique.** Il existe des constantes fixes \(C,M>0\) telles que, à temps égal, pour chaque paire \(x,y\),

\[
\min(|\omega(x,t)|,|\omega(y,t)|)<M
\quad\text{ou}\quad
|\xi(x,t)\times\xi(y,t)|\le C|x-y|.
\]

Autrement dit, la cohérence Lipschitz n'est imposée que lorsque les **deux** points appartiennent à la région de forte vorticité. Des formulations originales utilisent \(x\in\Omega_t(M)\) et \(x+y\), le partenaire de faible vorticité étant traité séparément ; la forme « high–high » ci-dessus rend le quantificateur effectif explicite.

**Conclusion.** L'enstrophie reste bornée jusqu'au temps terminal, la solution faible devient/reste forte, donc aucune singularité n'apparaît sous cette hypothèse.

**Ce que le théorème ne dit pas.** Il ne donne ni \(\alpha(x,t)\le0\), ni \(\omega\cdot S\omega\le0\), ni une petite valeur ponctuelle de ces quantités. Il contrôle l'intégrale singulière après découpage haut/bas et intégration en espace.

### 4.2 Constantin–Fefferman–Majda (1996) — Euler, pas Navier–Stokes

**Source primaire.** Peter Constantin, Charles Fefferman et Andrew J. Majda, “Geometric constraints on potentially singular solutions for the 3-D Euler equations”, *Communications in Partial Differential Equations* **21**(3–4), 559–571 (1996), [notice institutionnelle et métadonnées publiées](https://collaborate.princeton.edu/en/publications/geometric-constraints-on-potentially-singular-solutions-for-the-3/).

**Cadre.** Euler incompressible 3D sur \(\mathbb R^3\), **sans viscosité**, donnée initiale lisse et localisée, solution classique sur \([0,T)\). Les trajectoires matérielles sont \(X(q,t)\) et \(W_t=X(W_0,t)\).

Un ensemble matériel \(W_0\) est « smoothly directed » s'il existe \(\rho>0\) et \(0<r\le\rho/2\) tels que :

1. \(\xi(\cdot,t)\) possède une extension Lipschitz à \(B_{4\rho}(X(q,t))\) pour chaque \(q\in W_0\) où \(\omega_0(q)\ne0\), avec
   \[
   \limsup_{t\uparrow T}\sup_q\int_0^t
   \|\nabla\xi(\cdot,s)\|_{L^\infty(B_{4\rho}(X(q,s)))}^2\,ds<\infty;
   \]
2. la vorticité est comparable dans deux voisinages emboîtés,
   \[
   \sup_{B_{3r}(W_t)}|\omega(t)|\le m\sup_{B_r(W_t)}|\omega(t)|;
   \]
3. la vitesse est uniformément bornée dans \(B_{4\rho}(W_t)\).

**Conclusion.** Une borne locale de vorticité se propage sur un intervalle de temps uniforme ; la version « regularly directed » contrôle directement la vorticité le long de \(W_t\).

**Écart Clay.** C'est Euler, avec transport matériel exact des lignes de vortex, sans diffusion ni reconnexion visqueuse. La structure est conceptuellement pertinente, mais aucun transfert à Navier–Stokes ne peut être invoqué sans lemme de raccord. Ce résultat ne donne pas non plus un signe ponctuel du stretching.

### 4.3 Beirão da Veiga–Berselli (2002) — seuil demi-Hölder

**Source primaire.** Hugo Beirão da Veiga et Luigi C. Berselli, “On the regularizing effect of the vorticity direction in incompressible viscous flows”, *Differential and Integral Equations* **15**(3), 345–356 (2002), accepté en janvier 2001, DOI [10.57262/die/1356060864](https://doi.org/10.57262/die/1356060864), [PDF auteur](https://people.dm.unipi.it/beiraodaveiga/pdf/hbv-79.pdf).

**Cadre.** Navier–Stokes incompressible 3D, \(\mathbb R^3\), \(\nu>0\), force posée à zéro, donnée lisse puis \(u_0\in H^1\). Une solution faible vérifie

\[
u\in C_w(0,T;L^2)\cap L^2(0,T;H^1),
\]

et « forte » signifie dans l'article

\[
u\in L^\infty(0,T;H^1)\cap L^2(0,T;H^2).
\]

**Famille d'hypothèses.** Pour \(\beta\in[1/2,1]\),

\[
|\xi(x,t)\times\xi(y,t)|
\le g(t,x)|x-y|^\beta,
\]

avec

\[
g\in L^a(0,T;L^b(\mathbb R^3)),\qquad
\frac2a+\frac3b=\beta-\frac12,qquad
a\in\left[\frac4{2\beta-1},\infty\right].
\]

L'énoncé publié est donné presque partout pour toutes les paires ; les reformulations des auteurs et les versions localisées indiquent que l'hypothèse peut être restreinte aux paires où les deux modules dépassent un seuil fixe, les autres interactions étant des termes d'ordre inférieur.

**Endpoint central.** Pour \(\beta=1/2\), un coefficient borné constant suffit :

\[
|\xi(x,t)\times\xi(y,t)|\le C|x-y|^{1/2}.
\]

**Conclusion.** La solution faible est forte sur \([0,T]\), donc régulière et unique dans la classe faible considérée. Contrairement à la route Constantin–Fefferman, la preuve ne requiert pas \(\omega_0\in L^1\).

**Perte exacte.** Le facteur \(|x-y|^{1/2}\) rend le noyau juste assez intégrable pour fermer l'estimation d'enstrophie par Hardy–Littlewood–Sobolev, Sobolev et Young. Descendre sous \(1/2\) sans contrôle supplémentaire de la magnitude laisse une puissance critique non absorbée.

### 4.4 Grujić–Ruzmaikina (2004) — interpolation géométrie/magnitude

**Source primaire.** Zoran Grujić et Anastasia Ruzmaikina, “Interpolation between algebraic and geometric conditions for smoothness of the vorticity in the 3D NSE”, *Indiana University Mathematics Journal* **53**(4), 1073–1080 (2004), [PDF auteur](https://zgrujic.faculty.virginia.edu/sites/g/files/jsddwu601/files/2020-12/iumj_2004.pdf).

**Cadre.** Navier–Stokes 3D non forcé sur \(\mathbb R^3\), solution régulière sur \((0,T)\) examinée à un éventuel premier temps singulier ; donnée de vitesse d'énergie finie, vorticité initiale dans les espaces nécessaires aux estimations.

**Énoncé représentatif.** Pour \(q\ge2\), si

\[
\|\omega(t)\|_q^{q/(q-1)}\in L^1(0,T)
\]

et, dans la région de forte vorticité,

\[
|\xi(x+y,t)\times\xi(x,t)|\le C|y|^{1/q},
\]

alors \(\sup_{t<T}\|\omega(t)\|_q<\infty\).

**Lecture.** Ce n'est pas une amélioration géométrique gratuite sous \(1/2\) : l'exposant angulaire plus faible est compensé par une hypothèse d'intégrabilité sur la magnitude.

### 4.5 Grujić (2009) — localisation espace-temps complète

**Source primaire.** Zoran Grujić, “Localization and Geometric Depletion of Vortex-Stretching in the 3D NSE”, *Communications in Mathematical Physics* **290**, 861–870 (2009), DOI [10.1007/s00220-008-0726-8](https://doi.org/10.1007/s00220-008-0726-8), [PDF auteur](https://zgrujic.faculty.virginia.edu/sites/g/files/jsddwu601/files/2020-12/cmp_2009.pdf).

**Cadre.** Navier–Stokes 3D, \(\nu=1\) après remise à l'échelle, sur un ouvert \(\Omega\subset\mathbb R^3\), solution de Leray. On travaille dans un cylindre parabolique compactement inclus

\[
Q_{2r}(x_0,t_0)=B_{2r}(x_0)\times(t_0-(2r)^2,t_0).
\]

**Résultat.** Le transport et le stretching peuvent être localisés, les commutateurs avec les cutoffs étant contrôlés comme termes d'ordre inférieur. La condition demi-Hölder sur la direction peut donc être imposée dans un cylindre arbitrairement petit et donne la régularité intérieure.

**Précaution frontière.** « Indépendamment du domaine ou des conditions au bord » signifie que le critère est intérieur, loin du bord. Ce n'est pas à lui seul un théorème de régularité jusqu'à une frontière no-slip.

**Rôle pour le test adverse.** Une propriété dans une boule à un seul temps est encore trop faible : le théorème requiert une condition espace-temps sur le cylindre et contrôle explicitement les termes issus de l'extérieur/cutoff.

### 4.6 Giga–Miura (2011) — continuité uniforme, mais Type I

**Source primaire.** Yoshikazu Giga et Hideyuki Miura, “On Vorticity Directions near Singularities for the Navier–Stokes Flows with Infinite Energy”, *Communications in Mathematical Physics* **303**(2), 289–300 (2011), DOI [10.1007/s00220-011-1197-x](https://doi.org/10.1007/s00220-011-1197-x), [version ouverte de 2010](https://eprints.lib.hokudai.ac.jp/dspace/bitstream/2115/69763/1/pre956.pdf).

**Cadre.** Solution mild lisse et spatialement bornée sur \(\mathbb R^3\times(0,T)\), donnée seulement bornée et possiblement d'énergie infinie.

**Hypothèses.** Le taux de croissance est Type I,

\[
\sup_{0<t<T}(T-t)^{1/2}\|u(t)\|_\infty<\infty,
\]

et \(\xi\) est uniformément continue en espace dans les régions où \(|\omega|\) est grand, uniformément près du temps candidat.

**Conclusion.** La solution se prolonge sans blow-up à \(T\). Le blow-up renormalisé devient bidimensionnel sous l'hypothèse d'alignement, puis un théorème de Liouville exclut la limite.

**Écart.** La continuité est plus faible que Hölder/Lipschitz, mais le prix est une hypothèse Type I critique absente du problème Clay général. Les scénarios Type II restent hors portée.

### 4.7 Berselli (2023) — petits sauts à incréments discrets

**Source primaire.** Luigi C. Berselli, “On the vorticity direction and the regularity of 3D Navier–Stokes equations”, *Nonlinearity* **36**, 4303–4313 (2023), DOI [10.1088/1361-6544/ace096](https://doi.org/10.1088/1361-6544/ace096), publié le 3 juillet 2023.

**Cadre.** Cas périodique 3D traité directement, avec adaptation au problème de Cauchy sur \(\mathbb R^3\). Donnée suffisamment régulière, notamment \(H^5\) dans la preuve par Taylor ; solution forte avant le temps terminal.

**Hypothèse/conclusion.** Une petitesse quantitative des sauts de direction n'a besoin d'être testée, pour chaque \(x\), qu'aux points \(x+h e_j\) situés à distance fixe le long des axes de coordonnées. La petitesse dépend de \(\nu\), de la donnée et de \(|h|\). Elle ferme une borne \(H^1\), puis les normes supérieures, et empêche le blow-up.

**Limite.** C'est une condition discrète plus testable, mais pas une loi de signe locale. La preuve paie des estimations \(H^5\) et des constantes très défavorables ; elle n'établit pas que la dynamique génère spontanément cette petitesse.

## 5. Veille différentielle 2025–2026

### 5.1 Lei–Ren–Tian (2025), v1 — confinement dans un double cône

**Source primaire et version.** Zhen Lei, Xiao Ren et Gang Tian, “A Geometric Characterization of Potential Navier-Stokes Singularities”, [arXiv:2501.08976v1](https://arxiv.org/abs/2501.08976), soumis le 15 janvier 2025. À la date de coupure, la page arXiv n'expose qu'une v1 et aucune publication évaluée par les pairs n'a été identifiée dans cette veille.

**Équation et solution.** Navier–Stokes incompressible 3D, viscosité unité, sans force, localement dans

\[
Q(1)=B(1)\times(-1,0).
\]

\((v,p)\) est une solution faible adaptée locale : énergie locale finie, équations distributionnelles et inégalité d'énergie locale ; \(p\in L^{3/2}_{\mathrm{loc}}\).

**Théorème 1.1.** S'il existe \(e\in\mathbb S^2\) et \(\delta,M>0\) tels qu'en tout point régulier de \(Q(1)\),

\[
|\omega(x,t)|\le M
\quad\text{ou}\quad
|\xi(x,t)\times e|\le1-\delta,
\]

alors \(v\) est régulier dans \(\overline{Q(1/2)}\). La seconde alternative confine la vorticité forte dans un double cône autour de \(\pm e\), sans exiger que son ouverture soit petite.

**Corollaire 1.6.** Si, pour toutes les paires de points réguliers à vorticité non nulle,

\[
|\xi(x,t)\times\xi(y,t)|<1-\delta,
\]

alors l'origine est régulière. Contrairement au théorème principal et aux critères high–high, cette hypothèse porte sur toute la région \(|\omega|>0\).

**Mécanisme.** Le papier contrôle des flux locaux de vorticité, obtient une borne critique de type \(L_t^\infty L_{x_3}^\infty L_{x_h}^1\), produit une limite ancienne Type I, puis gagne de la petitesse par De Giorgi–Nash–Moser. Il n'utilise pas un signe de \(\omega\cdot S\omega\).

**Portée Clay.** Tout blow-up local compatible avec le problème Clay doit, d'après ce préprint, faire explorer aux directions de forte vorticité un ensemble rencontrant chaque grand cercle de \(\mathbb S^2\). Cela exclut une classe substantielle de profils, mais ne prouve pas que tout blow-up est confiné dans un double cône.

### 5.2 Yu (2026), v1 — stretching filtré et défauts sous-maille

**Source primaire et version.** Runlong Yu, “Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier–Stokes Equations”, [arXiv:2606.27560v1](https://arxiv.org/abs/2606.27560), soumis le 25 juin 2026 ; prépublication non évaluée identifiée comme v1.

**Cadre.** Navier–Stokes 3D sur \(\mathbb R^3\), viscosité unité. Les estimations cinématiques proches valent pour tout champ divergence-free

\[
u\in L_t^\infty L_x^2,
\]

après filtrage spatial \(U_\ell=\varphi_\ell*u\), \(\Omega_\ell=\nabla\times U_\ell\). Les bilans dynamiques sont ensuite formulés pour une solution de Leray–Hopf.

**Résultat non conditionnel à échelle finie.** Pour un cylindre d'échelle \(r\) et \(\ell=\sigma r\), la partie positive proche du stretching filtré satisfait schématiquement

\[
\mathcal V_{r,\ell}^{+,\mathrm{near}}
\le (1-\varepsilon)\mathcal P_{r,\ell}^{\rho}
+C_{\varepsilon,\rho,\varphi}M_{r,\rho}(u)
\left(\frac r\ell\right)^5\mathcal O_{r,\ell}.
\]

À rapport \(\sigma\) fixé, la constante est uniforme en \(r\), mais elle dégénère comme \(\sigma^{-5}\) lorsque le filtre disparaît relativement à l'échelle observée.

**Ce qui reste.** Le strain lointain, la contrainte de packing annulaire, le forcing de commutateur et les résidus de localisation. Le théorème de surplus non pondéré est conditionnel à leur sommabilité. La prépublication isole donc proprement les obstacles ; elle ne ferme pas le passage \(\ell/r\to0\) et ne donne pas la régularité globale.

### 5.3 Grujić (2026), v2 — déplétion logarithmique conditionnelle

**Source primaire et version.** Zoran Grujić, “Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier-Stokes Equations”, [arXiv:2607.08866v2](https://arxiv.org/abs/2607.08866), v1 le 9 juillet 2026, v2 le 13 juillet 2026. Commentaire arXiv de v2 : corrections typographiques et reformulations. Aucun statut évalué par les pairs n'a été identifié à la date de coupure.

**Cadre annoncé.** Solution unique, spatialement analytique sur \((0,T^*)\), donnée \(u_0\in L^\infty(\mathbb R^3)\), \(T^*\) premier temps singulier possible. Le scénario est une singularité ponctuelle critique avec

\[
\omega\in L_t^\infty L_x^{3/2,\infty},
\]

plus une factorisation locale \(|\omega(x,t)|\sim |x|^{-2}\) dont le facteur de forme est borné, scale-invariant ou log-périodique, avec gradient critique contrôlé.

**Hypothèse géométrique.** Uniformément près de \(T^*\),

\[
\xi\in L_t^\infty\mathrm{bmo}_{1/|\log r|}(\mathbb R^3).
\]

**Conclusion revendiquée.** Le théorème 7.4 affirme que \(T^*\) n'est pas singulier. La route est : commutateur de Calderón–Zygmund \(\to\) gain logarithmique local pour \(\alpha\) \(\to\) Lorentz–Zygmund pour \(\omega\) puis \(u\) \(\to\) sparseness sous le rayon d'analyticité \(\to\) principe du maximum harmonique.

**Statut d'audit.** Conserver au statut **PREPRINT_CLAIM / NEEDS_INDEPENDENT_CHECK**, pas PAPER_PROOF dans le laboratoire avant vérification détaillée des quatre raccords suivants : extension BMO locale et queue lointaine ; interpolation/troncature De Giorgi ; transfert de la réarrangée de \(\omega\) à celle de \(u\) ; conversion d'une mesure globale de superniveau en sparseness linéaire uniforme au rayon analytique. Même si tous ces raccords sont corrects, l'hypothèse de profil critique ponctuel n'épuise pas les scénarios Clay, notamment Type II, multi-points ou multi-échelles.

### 5.4 Calculs voisins, sans preuve de régularité

- Tsuyoshi Yoneda, “Vortex Stretching in the Navier-Stokes Equations and Information Dissipation in Diffusion Models”, [arXiv:2602.01071v1](https://arxiv.org/abs/2602.01071), 1er février 2026 : formulation inverse en temps et trajectoires lagrangiennes apprises par réseau neuronal pour un champ axisymétrique discret. Statut : calcul exploratoire, pas preuve ni critère Clay.
- Dhawal Buaria, John M. Lawson et Michael Wilczek, “Twisting vortex lines regularize Navier-Stokes turbulence”, [arXiv:2409.13125v1](https://arxiv.org/abs/2409.13125), soumis le 19 septembre 2024, puis *Science Advances*, DOI [10.1126/sciadv.ado1969](https://doi.org/10.1126/sciadv.ado1969) : mécanisme statistique/numérique d'anti-twist dans la turbulence. Statut : résultat physique et numérique, pas théorème excluant le blow-up.

La recherche différentielle n'a pas identifié d'autre article primaire 2025–2026 établissant un signe ponctuel de \(\omega\cdot S\omega\) ou une amélioration publiée et évaluée du seuil demi-Hölder sans hypothèse compensatrice.

## 6. Tableau des quantificateurs à ne pas confondre

| Résultat | Domaine / solution | Où porte la géométrie ? | Régularité de direction | Hypothèse compensatrice | Conclusion |
|---|---|---|---|---|---|
| Constantin–Fefferman 1993 | \(\mathbb R^3\), Leray/forte avant \(T\) | paires high–high, uniformément en temps | Lipschitz | route originale : \(L^1\) de \(\omega\) | enstrophie bornée, prolongement |
| CFM 1996 | \(\mathbb R^3\), Euler classique | voisinages de trajectoires matérielles | Lipschitz intégré en temps | comparabilité locale de \(|\omega|\), vitesse bornée | pas de blow-up local Euler |
| BdV–Berselli 2002 | \(\mathbb R^3\), faible \(\to\) forte | toutes paires dans l'énoncé, réductible high–high | \(1/2\)-Hölder à Lipschitz | \(g\in L_t^aL_x^b\) aux autres endpoints | régularité |
| Grujić–Ruzmaikina 2004 | \(\mathbb R^3\), régulière avant \(T\) | forte vorticité | \(1/q\)-Hölder | \(\|\omega\|_q^{q/(q-1)}\in L_t^1\) | \(L^q\) borné |
| Grujić 2009 | cylindre intérieur, Leray | cylindre arbitrairement petit | notamment \(1/2\)-Hölder | contrôle des commutateurs de cutoff | régularité intérieure |
| Giga–Miura 2011 | \(\mathbb R^3\), mild bornée | forte vorticité près du blow-up | continuité uniforme | Type I | prolongement |
| Berselli 2023 | \(\mathbb T^3\), extension \(\mathbb R^3\) | incréments discrets axiaux | petits sauts | données/normes hautes | prolongement |
| Lei–Ren–Tian 2025 v1 | \(Q(1)\), faible adaptée locale | points réguliers de forte vorticité | aucune continuité ; image dans double cône | flux local + DGNM dans la preuve | régularité dans \(Q(1/2)\) |
| Yu 2026 v1 | \(\mathbb R^3\), filtrée/Leray–Hopf | partie proche à échelle \((r,\ell)\) | défaut pairwise filtré | pertes \((r/\ell)^5\), queues/résidus | estimation, fermeture conditionnelle |
| Grujić 2026 v2 | \(\mathbb R^3\), analytique avant \(T^*\) | cœur ponctuel critique | \(\mathrm{bmo}_{1/|\log r|}\) | profil \(L^{3/2,\infty}\) uniforme | exclusion conditionnelle revendiquée |

## 7. Verdict sur le signe ponctuel

### 7.1 Aucun des théorèmes audités ne pose ou ne conclut un signe

La quantité

\[
\omega\cdot S\omega=|\omega|^2\,\xi\cdot S\xi
\]

est positive si \(\xi\) pointe vers une direction propre extensive de \(S\), négative vers une direction compressive, et nulle sur un cône intermédiaire. Comme \(\operatorname{tr}S=0\), le strain possède en général les deux signes. La cohérence de \(\xi\) adoucit le noyau non local ; elle n'oriente pas \(\xi\) par rapport aux vecteurs propres du strain total.

Les articles classiques emploient :

- une majoration de \(|D|\) par un sinus d'angle ;
- des inégalités sur \(|\int\omega\cdot S\omega|\) ou sur sa partie positive ;
- une absorption dans \(\nu\|\nabla\omega\|_2^2\) ;
- ou un argument de compacité/flux/rigidité.

Ils n'emploient pas une positivité ou négativité ponctuelle cachée.

### 7.2 Contre-exemple cinématique local exact

Dans une boule autour de l'origine, considérons le jet affine \(u(x)=Ax\) avec

\[
A=S+K,\qquad
S=\operatorname{diag}(-1,-1,2),\qquad
K=\begin{pmatrix}0&-1/2&0\\1/2&0&0\\0&0&0\end{pmatrix}.
\]

Alors \(\operatorname{tr}A=0\), donc \(u\) est incompressible localement,

\[
\omega=\nabla\times u=e_3,qquad
\xi=e_3,qquad
\omega\cdot S\omega=2>0.
\]

En remplaçant \(S\) par \(\operatorname{diag}(1,1,-2)\), on obtient \(-2<0\), avec exactement la même vorticité locale constante. Avec \(S=\operatorname{diag}(1,-1,0)\), on obtient zéro.

Ces jets admettent des extensions \(C_c^\infty(\mathbb R^3)\) divergence-free qui leur sont identiques dans une boule : multiplier par un cutoff puis corriger la divergence, supportée dans l'anneau de transition, au moyen de l'opérateur de Bogovskiĭ. Chaque extension est une donnée initiale lisse admissible donnant une solution forte locale. Ainsi les trois signes sont compatibles avec une direction localement parfaitement cohérente.

### 7.3 Version qui isole la non-localité

On peut séparer rotation locale et strain lointain :

1. construire un champ divergence-free compactement supporté qui vaut \(Kx\) dans \(B_1\), donc \(\omega=e_3\) dans \(B_1\) ;
2. construire un second champ divergence-free compactement supporté qui vaut \(Sx\) dans \(B_1\), avec \(S=S^{\mathsf T}\), \(\operatorname{tr}S=0\) ; son curl est nul dans \(B_1\) et sa vorticité est portée dans un anneau ;
3. additionner les deux champs.

La vorticité et sa direction dans \(B_1\) ne changent pas, mais le strain au centre change de \(S\). Cette construction est l'analogue exact d'une perturbation lointaine dans la loi de Biot–Savart.

## 8. Ce qu'un contre-profil local réfute — et ne réfute pas

### Réfuté

Un contre-profil du type précédent réfute tout lemme ayant l'une des formes suivantes :

\[
\xi\ \text{constante ou Hölder dans }B_r
\Longrightarrow \omega\cdot S\omega(x_0)\le0,
\]

ou

\[
[\xi]_{C^\beta(B_r)}\ \text{petit}
\Longrightarrow |\xi(x_0)\cdot S(x_0)\xi(x_0)|\ \text{petit},
\]

si le membre de droite ne contient aucun terme de strain extérieur, aucune queue Biot–Savart et aucune hypothèse globale.

Il réfute également une preuve qui remplace silencieusement \(S=\mathcal T\omega\) par un opérateur local sur \(\xi\), ou qui conclut d'un angle local faible que la production d'enstrophie est localement négative.

### Non réfuté

Le même profil ne contredit pas :

- Constantin–Fefferman ou Beirão da Veiga–Berselli, car leurs hypothèses portent sur toutes les paires high–high pertinentes et sur un intervalle de temps, et leur conclusion est intégrée ;
- Grujić 2009, car les termes de cutoff et l'extérieur du cylindre sont conservés ;
- Giga–Miura, car il manque le scénario Type I complet et la persistance temporelle de la continuité ;
- Lei–Ren–Tian, car le double cône est une hypothèse espace-temps sur une solution faible adaptée et le mécanisme passe par les flux, pas par un signe instantané ;
- Yu 2026, parce que le strain lointain, le commutateur et les résidus sont précisément laissés dans le budget ;
- Grujić 2026, qui impose un profil critique global/uniforme et un espace BMO logarithmique, non une simple cohérence dans une boule.

## 9. Test adverse reproductible recommandé

**Question falsifiable.** À vorticité identique dans \(B_1\), peut-on faire varier continûment et changer le signe de \(\omega(0)\cdot S(0)\omega(0)\) en ne modifiant la vorticité que dans \(B_2\setminus B_1\) ?

**Construction analytique.** Utiliser les deux champs de la section 7.3, avec un paramètre \(a\in[-1,1]\) multipliant \(Sx\). Vérifier exactement :

\[
\nabla\cdot u_a=0,\qquad
\omega_a|_{B_1}=e_3,\qquad
S_a(0)=aS,
\qquad
\omega_a(0)\cdot S_a(0)\omega_a(0)=2a.
\]

**Version numérique indépendante.** Sur un grand tore, approximer les extensions compactes par projection spectrale divergence-free ; recalculer \(S\) à partir de \(\omega\) par le multiplicateur de Leray/Biot–Savart, jamais par différentiation du champ cible seulement. Publier pour chaque résolution \(N\) :

- erreur \(\|\nabla\cdot u_N\|_2\) ;
- erreur de vorticité dans \(B_1\) ;
- valeur de \(\omega_N(0)\cdot S_N(0)\omega_N(0)\) ;
- queue spectrale et écart entre résolutions \(N,2N\) ;
- sensibilité au rayon de l'anneau et au cutoff ;
- comparaison du strain obtenu par gradient spectral et par Biot–Savart.

**Résultat attendu.** Le signe suit \(a\) alors que le défaut de cohérence local tend vers zéro avec l'erreur d'approximation. Une validation réussie clôt définitivement les pistes de « signe local par alignement » et force toute inégalité utile à porter un terme de queue non local explicite.

## 10. Maillon de recherche transférable

Le premier lemme qui resterait compatible avec toutes les sources est une inégalité **locale avec queue** : pour \(x_0\), \(r>0\) et un champ lisse divergence-free,

\[
\bigl(\omega\cdot S\omega\bigr)_+(x_0)
\le F_{\mathrm{near}}\!left(
|\omega|,[\xi]_{C^\beta(B_{2r})},r
\right)
+|\omega(x_0)|^2\,\mathcal T_{\mathrm{far}}(x_0,r),
\]

avec \(\mathcal T_{\mathrm{far}}\) explicitement défini par la partie \(|y|>r\) du strain. Le travail scientifique n'est pas d'éliminer cette queue par rhétorique, mais de déterminer si elle admet :

1. un packing annulaire uniforme ;
2. une sommation de Carleson ;
3. une compensation signée multi-échelle ;
4. ou un contre-exemple montrant qu'aucune de ces fermetures ne suit de l'énergie seule.

Ce maillon relie directement Constantin–Fefferman/BdV–Berselli (noyau angulaire), Grujić 2009 (localisation), Yu 2026 (budget filtré) et le test adverse (nécessité de la queue). Il est falsifiable sans prétendre résoudre le problème Clay.

## 11. Références primaires retenues

1. Constantin–Fefferman 1993, DOI [10.1512/iumj.1993.42.42034](https://doi.org/10.1512/iumj.1993.42.42034).
2. Constantin–Fefferman–Majda 1996, *Comm. PDE* 21, 559–571, [métadonnées institutionnelles](https://collaborate.princeton.edu/en/publications/geometric-constraints-on-potentially-singular-solutions-for-the-3/).
3. Beirão da Veiga–Berselli 2002, DOI [10.57262/die/1356060864](https://doi.org/10.57262/die/1356060864), [PDF auteur](https://people.dm.unipi.it/beiraodaveiga/pdf/hbv-79.pdf).
4. Grujić–Ruzmaikina 2004, [PDF auteur](https://zgrujic.faculty.virginia.edu/sites/g/files/jsddwu601/files/2020-12/iumj_2004.pdf).
5. Grujić 2009, DOI [10.1007/s00220-008-0726-8](https://doi.org/10.1007/s00220-008-0726-8).
6. Giga–Miura 2011, DOI [10.1007/s00220-011-1197-x](https://doi.org/10.1007/s00220-011-1197-x), [version ouverte](https://eprints.lib.hokudai.ac.jp/dspace/bitstream/2115/69763/1/pre956.pdf).
7. Berselli 2023, DOI [10.1088/1361-6544/ace096](https://doi.org/10.1088/1361-6544/ace096).
8. Lei–Ren–Tian 2025, [arXiv:2501.08976v1](https://arxiv.org/abs/2501.08976).
9. Yu 2026, [arXiv:2606.27560v1](https://arxiv.org/abs/2606.27560).
10. Grujić 2026, [arXiv:2607.08866v2](https://arxiv.org/abs/2607.08866).
11. Yoneda 2026, [arXiv:2602.01071v1](https://arxiv.org/abs/2602.01071).
12. Buaria–Lawson–Wilczek 2024, [arXiv:2409.13125v1](https://arxiv.org/abs/2409.13125), DOI [10.1126/sciadv.ado1969](https://doi.org/10.1126/sciadv.ado1969).

## 12. Statuts proposés pour le registre d'affirmations

- `CF_1993_HIGH_VORTICITY_LIPSCHITZ_REGULARITY` — `PAPER_PROOF`, publié, whole-space, conditionnel.
- `BDVB_2002_HALF_HOLDER_REGULARITY` — `PAPER_PROOF`, publié, whole-space, conditionnel.
- `CFM_1996_SMOOTHLY_DIRECTED_EULER` — `PAPER_PROOF`, mais `NEIGHBORING_EQUATION`; aucun transfert automatique à Clay.
- `GRUJIC_2009_LOCALIZATION` — `PAPER_PROOF`, régularité intérieure/localisation.
- `GIGA_MIURA_2011_TYPE_I_UNIFORM_CONTINUITY` — `PAPER_PROOF`, condition Type I.
- `BERSELLI_2023_DISCRETE_SMALL_JUMPS` — `PAPER_PROOF`, périodique/Cauchy, constantes dépendantes des hautes normes.
- `LEI_REN_TIAN_2025_DOUBLE_CONE` — `PREPRINT_PROOF`, v1, audit indépendant requis.
- `YU_2026_FILTERED_STRETCHING` — `PREPRINT_PROOF`, v1 ; distinguer estimation inconditionnelle et fermeture conditionnelle.
- `GRUJIC_2026_LOG_DEPLETION` — `PREPRINT_CLAIM`, v2, audit indépendant prioritaire.
- `YONEDA_2026_INFORMATION_DISSIPATION` — `NUMERICAL_EVIDENCE`.
- `LOCAL_COHERENCE_IMPLIES_POINTWISE_SIGN` — `REFUTED`, contre-construction cinématique exacte de la section 7.
