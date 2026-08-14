# Cycle 0021 — audit primaire de la « critical point singularity »

Date de coupure : **2026-08-14**  
Objet : Zoran Grujić, *Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier-Stokes Equations*, [arXiv:2607.08866v2](https://arxiv.org/abs/2607.08866), 13 juillet 2026.  
Nature de la revue : audit bibliographique primaire, même famille de modèle ; **ne constitue pas** la passe contradictoire indépendante requise par le protocole du laboratoire.

## Verdict exécutif

La Definition 2.1 de la v2 ne définit pas encore une classe de scénarios de blow-up munie de quantificateurs suffisants. Elle juxtapose :

1. une croissance locale annoncée \(O(|x|^{-2})\) pour la **magnitude** de la vorticité ;
2. une factorisation \(\omega=\Phi |x|^{-2}\) ;
3. une description « scale-invariant or log-periodic at the core » de \(\Phi\) ;
4. une borne critique \(|\nabla\Phi|\lesssim |x|^{-1}\), uniforme en temps ;
5. une concentration radiale des sur-niveaux à l'échelle \(R\lesssim\lambda^{-1/2}\) ;
6. ailleurs dans l'article, deux hypothèses globales et uniformes en temps :
   \(\omega\in L^\infty_tL^{3/2,\infty}_x\) et
   \(\xi\in L^\infty_t\mathrm{bmo}_{1/|\log r|,x}\).

Ces propriétés ne s'impliquent pas mutuellement sans hypothèses supplémentaires. En particulier, une borne locale \(O(|x|^{-2})\) n'est pas une définition de singularité ; une borne faible-\(L^{3/2}\) ne localise pas les sur-niveaux dans une boule centrée ; et l'invariance d'échelle ou la log-périodicité ne donnent la borne sur \(\nabla\Phi\) qu'après avoir imposé une régularité angulaire/logarithmique. La v2 ne fixe ni rayon de cœur, ni seuil d'amplitude, ni constante uniforme pour chaque propriété, ni convergence vers un profil, ni échelle de cœur dépendant du temps.

Il existe donc une dichotomie falsifiable :

- lecture littérale \(O(|x|^{-2})\) comme simple majoration : la condition est trop faible pour caractériser un blow-up, car toute vorticité localement bornée la satisfait près de l'origine ;
- lecture non dégénérée \(\omega\asymp |x|^{-2}\) ou \(\Phi\not\to0\) au cœur : la factorisation décrit déjà une vorticité non bornée à chaque temps où elle vaut jusqu'à \(x=0\), ce qui n'est pas compatible avec la solution spatialement analytique postulée pour tout \(t<T^*\), sauf si l'on introduit une limite remise à l'échelle ou une échelle de cœur — absentes du texte.

Conclusion bibliographique : **RÉVISER** la définition avant de lui attribuer une portée de théorème conditionnel sur un scénario précisément défini. Aucun erratum primaire ni v3 n'a été trouvé au 2026-08-14.

## 1. Statut primaire et contrôle de version

| Élément | Constat primaire au 2026-08-14 | Statut |
|---|---|---|
| Auteur | Zoran Grujić | texte arXiv |
| Titre | *Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier-Stokes Equations* | texte arXiv |
| v1 | soumise le 2026-07-09 | [HTML v1](https://arxiv.org/html/2607.08866v1) |
| v2 | soumise le 2026-07-13 ; version courante | [notice](https://arxiv.org/abs/2607.08866), [HTML v2](https://arxiv.org/html/2607.08866v2), [source TeX](https://arxiv.org/src/2607.08866v2) |
| Commentaire de version | corrections de coquilles et reformulations annoncées | notice arXiv |
| Statut éditorial | prépublication ; aucune référence de revue affichée | inférence directe de la notice |
| DOI | [10.48550/arXiv.2607.08866](https://doi.org/10.48550/arXiv.2607.08866) | DOI DataCite d'arXiv, **pas** DOI d'un article accepté |
| Date « August 11, 2026 » dans le corps HTML | ne correspond pas à une nouvelle version arXiv | métadonnée interne au manuscrit, pas date de dépôt |
| Correction post-v2 | aucune v3, correction ou erratum primaire retrouvé | recherche au jour de coupure |

La version à citer pour toute affirmation ci-dessous est donc **arXiv:2607.08866v2**, et non la date affichée sous l'affiliation dans le rendu HTML.

### Différence pertinente entre v1 et v2

La comparaison directe des [§2.1 v1](https://arxiv.org/html/2607.08866v1#S2.SS1) et [§2.1 v2](https://arxiv.org/html/2607.08866v2#S2.SS1) donne :

| Point | v1 | v2 | Conséquence d'audit |
|---|---|---|---|
| croissance | « scales critically » | « locally scales » | le qualificatif critique disparaît, pas l'exposant |
| rôle de \(\Phi\) | variations spatiales d'ordre inférieur | variations spatiales | la notion d'ordre inférieur disparaît |
| hypothèse sur \(\Phi\) | \(\Phi\) explicitement uniformément bornée sur \((T^*-\varepsilon,T^*)\) | \(\Phi\) scale-invariante ou log-périodique au cœur ; « profile itself » uniformément borné dans l'espace-temps | le référent de « profile itself » devient grammaticalement ambigu |
| gradient | \(|\nabla\Phi|\sim |x|^{-1}\) | \(|\nabla\Phi|\lesssim |x|^{-1}\) | correction substantielle : équivalence remplacée par majoration |
| concentration radiale | présentée comme inhérente | présentée comme conséquence directe | aucune nouvelle démonstration ni hypothèse extérieure au cœur |

**Inférence contrôlée.** La v1 montre que, dans la v2, « profile itself is uniformly bounded » vise très probablement le **shape factor** \(\Phi\), et non \(\omega\). Cette lecture n'est toutefois plus le texte grammaticalement univoque de la v2. Si « profile » désignait \(\omega\), l'exemple \((2+\sin\log(1/|x|))|x|^{-2}\) la contredirait immédiatement.

## 2. Definition 2.1 — transcription mathématique fidèle

Ce paragraphe normalise la notation sans citer longuement la prose. Les éléments suivants sont ceux que la v2 associe à une « critical point singularity » :

- centre spatial fixé, ramené à \(0\) ;
- magnitude scalaire de la vorticité
  \[
  \omega(x,t):=|\boldsymbol\omega(x,t)| ;
  \]
- comportement local annoncé
  \[
  \omega(x,t)=O(|x|^{-2}) ;
  \]
- appartenance annoncée à
  \[
  L^{3/2,\infty}(\mathbb R^3) ;
  \]
- factorisation de profil
  \[
  \boxed{\omega(x,t)=\Phi(x,t)|x|^{-2}} ;
  \]
- exemples de shape factor :
  \[
  \Phi(x,t)=U\!\left(\frac{x}{|x|}\right),
  \qquad
  \Phi(x)=2+\sin\!\left(\log\frac1{|x|}\right) ;
  \]
- hypothèse qualitative : \(\Phi\) est invariante par échelle ou log-périodique au cœur ;
- bornes annoncées, uniformes en temps :
  \[
  \Phi\ \text{(lecture probable) uniformément bornée},
  \qquad
  |\nabla\Phi(x,t)|\lesssim |x|^{-1} ;
  \]
- pour les seuils \(\lambda\) grands,
  \[
  A_\lambda(t):=\{x\in\mathbb R^3:\omega(x,t)>\lambda\}
  \subset B_R,
  \qquad R\le C\lambda^{-1/2},
  \]
  avec \(C\) indépendant du temps.

La définition emploie le mot « locally » pour la loi \(O(|x|^{-2})\), mais écrit la factorisation sans préciser \(0<|x|<r_0\), tout \(\mathbb R^3\), ou une région de sur-niveau. Il est donc impossible d'en extraire honnêtement un domaine de validité plus fort.

### Quantificateurs présents, absents ou seulement suggérés

| Objet | Écrit en v2 | Quantificateur nécessaire non écrit |
|---|---|---|
| centre | un point, WLOG \(0\) | centre fixe ou \(x_*(t)\) ; unicité ; exclusion ou non de plusieurs centres |
| temps | profil potentiel de blow-up ; uniformité en temps de certaines bornes | intervalle exact ; \(T^*<\infty\) ; sens de la convergence quand \(t\uparrow T^*\) |
| cœur | « at the core » | rayon \(r_0\), dépendance éventuelle en \(t\), domaine puncturé |
| \(O(|x|^{-2})\) | ordre local | constante \(M\), uniformité en \(t\), majoration seule ou équivalence, seuil radial |
| factorisation | \(\omega=\Phi|x|^{-2}\) | locale ou globale ; presque partout ou ponctuelle ; régularité de \(\Phi\) |
| scale-invariant | adjectif | invariance continue \(\Phi(\rho x,t)=\Phi(x,t)\), ensemble des \(\rho\), rôle du temps |
| log-periodic | adjectif | période \(P\), variable \(\log r\), phase, uniformité en angle et temps |
| borne de \(\Phi\) | probable mais ambiguë | constante \(M_\Phi\), intervalle et région |
| gradient | \(\lesssim |x|^{-1}\), uniforme en temps | constante, sens faible/classique, région, comportement angulaire |
| faible-\(L^{3/2}\) | « naturally inhabits » | hypothèse ou conclusion ; norme globale ; borne uniforme en temps |
| sur-niveaux | pour \(\lambda\) grand, \(C\) indépendant de \(t\) | seuil \(\lambda_0\) uniforme ; centre ; contrôle hors cœur |
| signe | \(\omega\ge0\) est une magnitude | \(\Phi\ge0\) ; l'exemple angulaire \(U\) n'est pas explicitement contraint |

## 3. Hypothèses effectivement utilisées dans les résultats du manuscrit

La Definition 2.1 ne doit pas être lue isolément comme si elle contenait les hypothèses fonctionnelles des théorèmes.

### Lorentz

La v2 définit, pour \(1\le p<\infty\), \(1\le q<\infty\),

\[
\|f\|_{L^{p,q}}
=\left(\int_0^\infty [s^{1/p}f^*(s)]^q\,\frac{ds}{s}\right)^{1/q},
\qquad
\|f\|_{L^{p,\infty}}=\sup_{s>0}s^{1/p}f^*(s).
\]

Les théorèmes 4.1 et 7.4 supposent explicitement

\[
\boxed{\omega\in L^\infty\!\left((T^*-\varepsilon,T^*);
L^{3/2,\infty}(\mathbb R^3)\right)}.
\]

Il s'agit d'une hypothèse **globale en espace** et **uniforme en temps**, plus précise que la phrase narrative de la Definition 2.1.

### BMO logarithmique

La norme écrite à l'équation (2) est

\[
\|f\|_{\mathrm{bmo}_\phi}
=\|f\|_{L^\infty}
+\sup_{x\in\mathbb R^3,\,0<r<1/2}
\frac1{\phi(r)}\fint_{B_r(x)}|f(y)-c_{B_r(x)}|\,dy,
\qquad
\phi(r)=\frac1{|\log r|}.
\]

Les mêmes théorèmes supposent

\[
\boxed{\xi\in L^\infty\!\left((T^*-\varepsilon,T^*);
\mathrm{bmo}_{1/|\log r|}(\mathbb R^3)\right)},
\qquad
\xi=\frac{\boldsymbol\omega}{{|\boldsymbol\omega|}}.
\]

Le supremum est global en centre \(x\), bien que limité aux rayons \(r<1/2\). La v2 ne fixe pas la convention de \(\xi\) sur l'ensemble \(\{\boldsymbol\omega=0\}\). Le terme \(L^\infty\) de la norme rend cette convention pertinente à la définition de la classe, même si une modification sur un ensemble de mesure nulle serait invisible.

### Équation et type de solution

Le manuscrit travaille sur Navier–Stokes incompressible, visqueux et non forcé dans \(\mathbb R^3\), avec \(\nu>0\). Au niveau de la magnitude de vorticité, il écrit

\[
(\partial_t+u\cdot\nabla-\nu\Delta)\omega\le \alpha\omega,
\qquad
\alpha=\xi\cdot S\xi,
\qquad
S=\frac12(\nabla u+\nabla u^{\mathsf T})
=\mathcal T(\omega\xi).
\]

Le théorème 7.4 part de \(u_0\in L^\infty(\mathbb R^3)\) et parle de la solution unique spatialement analytique sur \((0,T^*)\), \(T^*\) étant le premier temps singulier possible. Le théorème local 7.3 est présenté comme un résultat de solution mild/analyticité, avec \(u\in C_w([0,T];L^\infty)\).

La référence [22] est en réalité **Rafaela Guberović**, et non « Gu » : [*Smoothness of Koch-Tataru solutions to the Navier-Stokes equations revisited*](https://doi.org/10.3934/dcds.2010.27.231), *Discrete and Continuous Dynamical Systems* 27 (2010), 231–236. Son résumé primaire traite l'analyticité spatiale des solutions de Koch–Tataru. L'adéquation exacte entre les hypothèses de cette source et la formulation \(L^\infty\) très large donnée au théorème 7.3 doit être contrôlée dans un audit séparé ; elle n'est pas certifiée ici par le seul résumé.

Le théorème 7.4 ne précise pas, dans son énoncé, une classe de pression, une condition d'énergie finie, une inégalité d'énergie, une décroissance à l'infini, ni une notion de solution faible adaptée/Leray–Hopf. Il s'agit d'un énoncé conditionnel portant sur une solution pré-singulière classique/analytique, pas d'un théorème de construction faible.

## 4. Vérifications analytiques élémentaires

### 4.1 Échelle

Sous l'échelle de Navier–Stokes

\[
u_\rho(x,t)=\rho u(\rho x,\rho^2t),
\qquad
\omega_\rho(x,t)=\rho^2\omega(\rho x,\rho^2t),
\]

on a

\[
\|\omega_\rho(t)\|_{L^{3/2,\infty}}=
\|\omega(\rho^2t)\|_{L^{3/2,\infty}},
\qquad
\Phi=|x|^2\omega
\]

sans dimension physique. L'exposant \(3/2\) est donc critique pour la vorticité.

La norme \(\mathrm{bmo}_\phi\) écrite avec le seuil absolu \(r<1/2\) et \(\phi(r)=1/|\log r|\) n'est pas littéralement invariante sous toutes les dilatations : \(r\) devient \(\rho r\) et le poids logarithmique change. Il faut fixer une longueur de référence, écrire \(\phi(r/R_*)\), ou n'affirmer qu'une comparabilité/asymptotique. Le manuscrit ne donne pas cette convention dimensionnelle.

### 4.2 Enveloppe ponctuelle vers sur-niveaux et faible-\(L^{3/2}\)

Si l'on **ajoute** l'hypothèse globale uniforme

\[
\omega(x,t)\le M|x|^{-2},
\]

alors

\[
A_\lambda(t)\subset B_{\sqrt{M/\lambda}},
\qquad
|A_\lambda(t)|\le \frac{4\pi}{3}\left(\frac M\lambda\right)^{3/2}.
\]

Cette dérivation justifie l'exposant \(\lambda^{-1/2}\), mais pas la formulation v2 telle quelle : une enveloppe valable seulement pour \(|x|<r_0\) exige encore

\[
\sup_{t\in I,\,|x|\ge r_0}\omega(x,t)<\infty
\]

pour obtenir la contenance centrée pour tous les \(\lambda\) au-dessus d'un seuil uniforme.

Réciproquement, une borne uniforme faible-\(L^{3/2}\), de taille \(K\), ne donne que

\[
|A_\lambda(t)|\le \left(\frac K\lambda\right)^{3/2}.
\]

Elle ne donne ni connexité, ni radialité, ni contenance de \(A_\lambda\) dans une boule centrée. Une famille de petits îlots éloignés ou plusieurs cœurs peut avoir la même fonction de distribution.

Enfin, une propriété des seuls grands niveaux ne contrôle pas la norme faible globale aux petits niveaux sans information de décroissance ou de mesure finie. La séparation, dans les théorèmes, entre l'hypothèse Lorentz globale et la géométrie de sur-niveau est donc mathématiquement nécessaire.

### 4.3 Invariance/log-périodicité et gradient

L'implication annoncée vers \(|\nabla\Phi|\lesssim |x|^{-1}\) n'est vraie qu'avec une hypothèse de régularité :

- si \(\Phi(x)=U(x/|x|)\), il faut par exemple \(U\in W^{1,\infty}(\mathbb S^2)\), donnant
  \(|\nabla\Phi(x)|\le \|\nabla_{\mathbb S^2}U\|_\infty/|x|\) ;
- si \(\Phi(x)=F(\log|x|,x/|x|)\), périodique dans la première variable, il faut borner \(\partial_sF\) et \(\nabla_{\mathbb S^2}F\).

La périodicité seule ne borne pas la dérivée : une fonction périodique bornée peut être non lipschitzienne, voire non différentiable. La v2 n'énonce pas les espaces de \(U\) ou \(F\), la période, la phase, ou l'uniformité temporelle de ces dérivées.

### 4.4 Centre fixe

Une translation constante permet bien de ramener un centre fixe à l'origine. Cela ne traite pas un centre \(x_*(t)\) mobile : dans les coordonnées \(y=x-x_*(t)\), le terme temporel acquiert une dérive \(-\dot x_*(t)\cdot\nabla_y\). La mention « without loss of generality » ne justifie donc ni l'exclusion des centres mobiles ni celle de plusieurs centres de concentration.

## 5. Test adverse reproductible de cohérence

Le test minimal ne demande aucun calcul flottant.

### Branche A — lecture majorante

Prendre une vorticité lisse localement bornée, par exemple

\[
\omega(x,t)=e^{-|x|^2}.
\]

Pour \(0<|x|<1\), \(\omega(x,t)\le |x|^{-2}\), donc \(\omega=O(|x|^{-2})\). On peut écrire \(\Phi=|x|^2e^{-|x|^2}\), bornée, et

\[
|\nabla\Phi|=2|x|e^{-|x|^2}|1-|x|^2|\lesssim |x|^{-1}
\quad (0<|x|<1).
\]

Ce profil est régulier au centre et n'est pas log-périodique/non dégénéré. Il montre que les seules relations \(O(|x|^{-2})\), factorisation et borne supérieure du gradient ne définissent pas une singularité. L'adjectif scale-invariant/log-periodic doit donc être formalisé et jouer un rôle non dégénéré si tel est l'objectif.

### Branche B — lecture non dégénérée

Prendre l'exemple explicite de la v2,

\[
\Phi(x)=2+\sin\left(\log\frac1{|x|}\right),
\qquad 1\le\Phi\le3.
\]

Alors \(\omega(x)=\Phi(x)|x|^{-2}\ge |x|^{-2}\), donc \(\omega\) est non bornée dans toute boule centrée en \(0\). Une solution spatialement analytique à un temps fixé \(t<T^*\) ne peut pas posséder ce profil ponctuel jusqu'au centre. Pour réconcilier l'exemple avec un scénario pré-singulier, il faut au moins l'un des objets absents suivants :

- un rayon de cœur \(r_c(t)>0\) à l'intérieur duquel le profil est régularisé, avec \(r_c(t)\downarrow0\) ;
- une suite \(t_n\uparrow T^*\), d'échelles \(r_n\downarrow0\), et une convergence des profils remis à l'échelle ;
- une égalité seulement à \(t=T^*\), avec notion de trace/limite explicitée.

**Résultat adverse.** La Definition 2.1, sans ajout de quantificateurs, ne passe pas simultanément le test de non-vacuité et le test de compatibilité avec l'analyticité pré-\(T^*\).

## 6. Sources primaires citées autour du scénario

La Definition 2.1 ne porte pas elle-même de citation. Les sources suivantes fournissent du contexte, mais aucune ne démontre que tout blow-up Navier–Stokes incompressible en \(\mathbb R^3\) a le profil de la définition.

| Source primaire | Résultat effectivement pertinent | Ce qu'elle ne transfère pas |
|---|---|---|
| J. Leray, *Sur le mouvement d'un liquide visqueux emplissant l'espace*, *Acta Math.* 63 (1934), [DOI 10.1007/BF02547354](https://doi.org/10.1007/BF02547354), [PDF primaire](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/5537-11511_2006_Article_BF02547354.pdf) | solutions faibles et cadre historique des profils auto-similaires | pas la Definition 2.1 ni un blow-up admissible |
| J. Nečas, M. Růžička, V. Šverák, *On Leray's self-similar solutions of the Navier–Stokes equations*, *Acta Math.* 176 (1996), [DOI 10.1007/BF02551584](https://doi.org/10.1007/BF02551584), [PDF primaire](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6533-11511_2006_Article_BF02551584.pdf) | le profil stationnaire backward self-similaire \(U\in L^3(\mathbb R^3)\) est nul | n'exclut pas tous profils discrets, asymptotiques, Type II ou multi-échelles |
| T.-P. Tsai, *On Leray's self-similar solutions of the Navier–Stokes equations satisfying local energy estimates*, *Arch. Rational Mech. Anal.* 143 (1998), [DOI 10.1007/s002050050099](https://doi.org/10.1007/s002050050099) | exclusions de solutions de Leray auto-similaires sous hypothèses larges incluant l'énergie locale | pas un théorème sur toute singularité ponctuelle critique |
| L. Escauriaza, G. Seregin, V. Šverák, *\(L_{3,\infty}\)-solutions of Navier–Stokes equations and backward uniqueness*, *Russian Math. Surveys* 58 (2003), [DOI 10.1070/RM2003v058n02ABEH000609](https://doi.org/10.1070/RM2003v058n02ABEH000609), [texte primaire Math-Net](https://www.mathnet.ru/eng/rm609) | endpoint vitesse \(u\in L^\infty_tL^3_x\) régulier | ne convertit pas \(\omega\in L^{3/2,\infty}\) en \(u\in L^3\) fort ; Biot–Savart ne donne en général qu'un endpoint faible |
| T. Barker, C. Prange, *Quantitative regularity for the Navier–Stokes equations via spatial concentration*, *Comm. Math. Phys.* 385 (2021), [DOI 10.1007/s00220-021-04122-x](https://doi.org/10.1007/s00220-021-04122-x) | régularité/concentration quantitatives, notamment dans un cadre critique faible pour la vitesse | pas la radialité ponctuelle de la vorticité de Definition 2.1 |
| T. Y. Hou, *Potentially Singular Behavior of the 3D Navier–Stokes Equations*, *Found. Comput. Math.* 23 (2023), [DOI 10.1007/s10208-022-09578-4](https://doi.org/10.1007/s10208-022-09578-4) | calcul numérique d'un scénario axisymétrique adaptatif | domaine cylindrique \(0\le r\le1,\ z\in\mathbb T\), frontière radiale de Dirichlet ; indice numérique non certifié, pas preuve sur \(\mathbb R^3\) |
| D. Wang et al., *Discovery of Unstable Singularities*, [arXiv:2509.14185v1](https://arxiv.org/abs/2509.14185) | calcul de haute précision / découverte assistée de singularités candidates instables dans CCF, IPM, Boussinesq et un analogue Euler avec frontière | aucune construction de blow-up pour Navier–Stokes incompressible visqueux 3D ; v1 seulement au jour de coupure |
| Z. Bradshaw, Z. Grujić, *A spatially localized \(L\log L\) estimate on the vorticity in the 3D NSE*, *Indiana Univ. Math. J.* 64 (2015), [DOI 10.1512/iumj.2015.64.5496](https://doi.org/10.1512/iumj.2015.64.5496), [arXiv:1309.2519](https://arxiv.org/abs/1309.2519) | antécédent pour le contrôle BMO pondéré de la direction et le gain \(L\log L\) | ne définit ni ne force le profil radial critique de la v2 |
| D. Goldberg, *A local version of real Hardy spaces*, *Duke Math. J.* 46 (1979), [DOI 10.1215/S0012-7094-79-04603-9](https://doi.org/10.1215/S0012-7094-79-04603-9) | convention historique pour espaces Hardy/BMO locaux | ne résout pas la convention exacte de \(\mathrm{bmo}_\phi\), de l'échelle \(1/2\), ou de \(\xi\) aux zéros dans la v2 |

## 7. Veille différentielle au 2026-08-14

Une source primaire postérieure à Grujić v2 et pertinente pour les conventions est : Tobias Barker, *Quantitative classification of potential Navier–Stokes singularities beyond the blow-up time*, [arXiv:2510.20757v3](https://arxiv.org/abs/2510.20757), révisé le 2026-08-11.

Cette v3 définit explicitement :

- un point singulier via l'absence de borne \(L^\infty\) de la vitesse dans tout petit cylindre parabolique ;
- une solution de Leray–Hopf dans \(C_wL^2_\sigma\cap L^2\dot H^1\), avec équations distributionnelles et inégalité globale d'énergie ;
- le domaine cylindrique et les conditions au bord lorsqu'elle discute le scénario de Hou.

Cette source fournit un contraste utile : elle montre le niveau de précision attendu pour « singular point » et « Leray–Hopf solution ». Elle **n'est ni un erratum de Grujić, ni une validation de Definition 2.1**, et ne démontre pas le profil radial de vorticité.

Les recherches sur l'identifiant exact, le titre, « erratum » et « correction » n'ont révélé aucune autre mise à jour primaire de 2607.08866 après v2 à la date de coupure. Cette absence est un constat de veille, non une preuve qu'aucune discussion privée ou future n'existe.

## 8. Écart explicite avec le problème Clay

L'énoncé primaire est C. Fefferman, *Existence and Smoothness of the Navier–Stokes Equation*, [document officiel Clay](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf), [page du problème](https://www.claymath.org/millennium/Navier-Stokes-Equation/).

Pour le cas \(\mathbb R^3\), une résolution positive doit couvrir les données initiales lisses, divergence nulle et rapidement décroissantes (et la formulation de force admissible ; on peut prendre \(f=0\)), produire une solution lisse globale et satisfaire la borne d'énergie demandée. L'alternative négative exige des données/forces admissibles conduisant à une rupture de la conclusion. Le document Clay traite aussi le cas périodique.

Le manuscrit de Grujić v2 :

- ne traite que \(\mathbb R^3\), pas le cas périodique ;
- est non forcé et visqueux ;
- suppose un unique scénario ponctuel centré, avec concentration radiale annoncée ;
- ajoute les hypothèses globales uniformes \(\omega\in L^\infty_tL^{3/2,\infty}_x\) et \(\xi\in L^\infty_t\mathrm{bmo}_\phi\) ;
- énonce \(u_0\in L^\infty\), sans faire figurer dans le théorème 7.4 la décroissance rapide, l'énergie finie ou l'inégalité d'énergie Clay ;
- ne montre pas que toute singularité issue d'une donnée Clay satisfait la Definition 2.1 et les deux hypothèses fonctionnelles ;
- ne couvre pas explicitement les cœurs mobiles ou multiples, les concentrations non radiales, les scénarios Type II/multi-échelles, ni les limites anciennes sans ce profil ;
- n'est pas une construction d'un blow-up admissible.

L'implication correcte est donc seulement de la forme

\[
\begin{aligned}
&\text{solution pré-singulière de la classe du théorème 7.4}\\
&+\ \text{profil Definition 2.1 correctement quantifié}\\
&+\ \omega\in L^\infty_tL^{3/2,\infty}_x\\
&+\ \xi\in L^\infty_t\mathrm{bmo}_{1/|\log r|,x}\\
&+\ \text{validité de toutes les estimations intermédiaires}\\
&\Longrightarrow \text{évasion du blow-up dans cette classe conditionnelle}.
\end{aligned}
\]

Le maillon indispensable vers Clay serait

\[
\boxed{\text{tout premier blow-up Clay satisfait ces hypothèses de profil et de géométrie}.}
\]

Aucun résultat primaire identifié ici ne fournit ce maillon. Même une preuve complète du théorème conditionnel de la v2 ne résoudrait donc pas le problème Clay sans un théorème de réduction supplémentaire.

## 9. Formulation minimale falsifiable à substituer avant réemploi

Pour transformer la notion en hypothèse mathématique testable, il faudrait au minimum choisir **une** des deux formulations suivantes.

### Option instantanée régularisée

Il existe \(T^*<\infty\), \(\varepsilon,r_0,M,c,C>0\), un centre fixe \(x_*\), et une échelle \(r_c(t)\downarrow0\) tels que, pour tout \(t\in(T^*-\varepsilon,T^*)\),

\[
c\le \Phi(x,t)\le M,
\qquad
|\nabla\Phi(x,t)|\le C|x-x_*|^{-1},
\]

sur \(r_c(t)\le|x-x_*|\le r_0\), avec une règle explicite à l'intérieur du cœur, un contrôle uniforme hors \(B_{r_0}(x_*)\), et une définition exacte de l'invariance/log-périodicité.

### Option limite remise à l'échelle

Il existe \(t_n\uparrow T^*\), \(x_n\to x_*\), \(r_n\downarrow0\), une normalisation explicitée et une topologie \(X\) telles que les vorticités remises à l'échelle convergent dans \(X\) vers

\[
\Omega_*(y)=\Phi_*(y)|y|^{-2},
\]

avec \(0<c\le\Phi_*\le M\), régularité angulaire/logarithmique prescrite, et assez de compacité pour passer l'équation, la pression, l'énergie locale et les hypothèses \(\mathrm{bmo}_\phi\) à la limite.

Sans ce choix, « critical point singularity » reste une description phénoménologique mêlant profil limite, borne critique et géométrie des sur-niveaux.

## 10. Décision bibliographique du cycle

- **Affirmation soutenue par source primaire :** la v2 contient bien la factorisation, les deux exemples de \(\Phi\), la borne de gradient, la concentration \(R\lesssim\lambda^{-1/2}\), ainsi que les hypothèses uniformes faible-\(L^{3/2}\) et \(\mathrm{bmo}_\phi\) dans ses théorèmes.
- **Affirmation négative vérifiée :** les quantificateurs nécessaires pour une classe de blow-up pré-singulière cohérente ne sont pas donnés dans Definition 2.1.
- **Test adverse :** la lecture majorante inclut des profils lisses ; la lecture non dégénérée explicite est déjà non bornée au centre avant \(T^*\).
- **Convention/correction :** v2 affaiblit correctement \(\sim\) en \(\lesssim\) pour le gradient mais introduit/maintient des ambiguïtés de référent, de région et de temps.
- **Transfert Clay :** aucun transfert universel ; seulement une exclusion conditionnelle si le reste de la preuve est valide.
- **État recommandé :** **RÉVISER**.
- **Prochaine vérification primaire :** auditer ligne par ligne si les théorèmes 4.1 et 7.4 utilisent la concentration radiale comme hypothèse indépendante ou la déduisent illégitimement de la seule norme faible-\(L^{3/2}\), puis suivre toutes les constantes \(r_0,\lambda_0,C\) dans le passage aux estimations localisées.

