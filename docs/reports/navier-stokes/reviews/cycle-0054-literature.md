# Cycle 0054 — rotation, générateur renormalisé et observabilité

**Date de coupure :** 15 août 2026

**Nature :** veille primaire indépendante et audit contradictoire des
quantificateurs

**Question bornée :** les résultats publiés ou prépubliés sur les solutions
backward RSS/RDSS, ou sur un petit générateur de dilatation en variables
similaires, excluent-ils déjà une activité purement rotationnelle sous la seule
hypothèse suitable faible-$L^3$ ? Existe-t-il une coercivité publiée reliant ce
générateur à un flux ou à une quantité énergétique critique ?

## Verdict

1. **Pineau--Vicol `arXiv:2607.09619v2` est le premier résultat primaire
   direct identifié qui traite quantitativement les profils backward RSS/RDSS
   de Navier--Stokes incompressible 3D standard.** Au 15 août 2026, il reste
   une prépublication sans DOI ni référence de journal dans la notice arXiv.

2. **Le résultat RSS est partiel.** Sous une borne Type I ponctuelle globale,
   un profil $C^2$ et une auto-similarité tournée exacte, le théorème 1.4
   impose la trivialité lorsque la vitesse angulaire est assez petite ou assez
   grande, avec des seuils dépendant de la constante Type I. La plage
   intermédiaire reste explicitement ouverte.

3. **Le résultat RDSS est également partiel.** Le théorème 1.7 exige une
   période similaire courte, donc un facteur de dilatation proche de un, en
   plus d'une rotation petite ou grande quantifiée. Il ne couvre ni période
   arbitraire, ni rotation intermédiaire, ni orbite non périodique.

4. **Pineau--Vicol contient bien une estimation d'observabilité locale du
   générateur vers l'enstrophie.** À une tranche similaire, une identité de
   Bernoulli pondérée conduit à

   \[
    \int_{B_R}|\Omega|^2w_R
    \le K_1R^{-2}+K_2\delta,
   \]

   lorsque la norme gaussienne pondérée de $\partial_sV$ est au plus
   $\delta$. Mais cette estimation utilise une solution lisse, une borne Type I
   ponctuelle, un contrôle de pression sur une couronne et un poids adjoint
   dépendant du champ. Elle appartient à une **prépublication**, n'est pas une
   conséquence de l'inégalité d'énergie et ne part pas du seul
   $L^{3,\infty}$ spatial.

5. **Une activité purement tangentielle à l'orbite des rotations n'est pas
   observable par une énergie radiale.** Pour le générateur de rotation
   $\mathcal R$, toute énergie quadratique à poids radial vérifie
   $DE_a(V)[\mathcal RV]=0$, même lorsque $\mathcal RV\ne0$. Une coercivité
   contrôlant la norme du générateur par la dérivée signée d'une telle énergie
   est donc impossible sans modulation, observable non radial ou usage plus
   fin de l'équation.

6. **Sous faible-$L^3$ suitable seulement, l'activité RSS/RDSS non triviale
   n'est pas exclue par les sources auditées.** Le $L^3$ spatial fort est
   exclu par Escauriaza--Seregin--Šverák; le vrai Lorentz
   $L^{3,\infty}_x$ ne l'est pas. La borne ponctuelle Type I utilisée par
   Pineau--Vicol implique le faible-$L^3$, mais la réciproque est fausse.

7. **Aucun théorème publié exactement raccordé
   « générateur renormalisé petit $\Rightarrow$ flux/enstrophie petit
   $\Rightarrow$ régularité » dans la classe suitable faible-$L^3$ n'a été
   identifié.** Ce constat est borné aux index et textes primaires décrits en
   section 8; il ne constitue pas une preuve d'absence dans toute la
   littérature.

## 1. Équation, variables et trois générateurs à ne pas confondre

Le cadre principal est Navier--Stokes incompressible standard, non forcé,
viscosité un, sur $\mathbb R^3\times(-1,0)$ :

\[
 \partial_tu-\Delta u+(u\cdot\nabla)u+\nabla p=0,
 \qquad \nabla\cdot u=0.                                  \tag{1}
\]

Dans les variables backward similaires

\[
 y=\frac{x}{\sqrt{-t}},\qquad s=-\log(-t),\qquad
 V(y,s)=\sqrt{-t}\,u(x,t),\qquad P(y,s)=(-t)p(x,t),        \tag{2}
\]

on obtient

\[
 \partial_sV-\Delta V+\frac12V+\frac12y\cdot\nabla V
 +(V\cdot\nabla)V+\nabla P=0,
 \qquad\nabla\cdot V=0.                                   \tag{3}
\]

Le générateur de dilatation mesuré par Pineau--Vicol est

\[
 \partial_sV=\sqrt{-t}\left[(-t)\partial_tu-\frac12u
 -\frac12(x\cdot\nabla)u\right].                          \tag{4}
\]

Soit $R(\theta)$ la rotation autour de l'axe $e_3$, $J=R'(0)$, et

\[
 \mathcal RF:=JF-(Jy\cdot\nabla)F.                        \tag{5}
\]

Pour une RSS backward exacte,

\[
 u(x,t)=\frac1{\sqrt{-t}}R(\alpha s)
 U\!\left(\frac{R(-\alpha s)x}{\sqrt{-t}}\right),         \tag{6}
\]

le champ dans le repère similaire fixe est

\[
 V(y,s)=R(\alpha s)U(R(-\alpha s)y),
 \qquad \partial_sV=\alpha\mathcal RV.                   \tag{7}
\]

Le profil stationnaire dans le repère **co-tournant** satisfait en revanche

\[
 \alpha\mathcal RU+\frac12U+\frac12y\cdot\nabla U
 -\Delta U+(U\cdot\nabla)U+\nabla P=0.                   \tag{8}
\]

Ainsi « stationnaire dans le repère co-tournant », « générateur de
dilatation nul dans le repère fixe » et « générateur rotationnel nul » sont
trois propriétés différentes. Pour une RDSS, le profil co-tournant dépend en
outre périodiquement de $s$ et résout

\[
 \partial_sU+\alpha\mathcal RU+\frac12U
 +\frac12y\cdot\nabla U-\Delta U
 +(U\cdot\nabla)U+\nabla P=0,                             \tag{9}
\]

avec période $S=2\log\lambda$.

### Échelle

- $\|u(t)\|_{L^{3,\infty}_x}$ et $\|u(t)\|_{L^3_x}$ sont invariants sous
  l'échelle Navier--Stokes.
- La borne $|u(x,t)|\le C/(|x|+\sqrt{-t})$ est ponctuellement critique et
  implique une borne uniforme $L^{3,\infty}$.
- La réciproque est fausse : faible-$L^3$ ne donne ni majorant ponctuel, ni
  contrôle des dérivées, ni borne annulaire de pression.
- En variables similaires, $\partial_sV$ a la même dimension que $V$; sa
  norme gaussienne dans la remarque 1.11 de Pineau--Vicol est sans perte
  d'échelle physique après (2).

## 2. Sources primaires et statut exact

| Source et statut au 2026-08-15 | Équation et notion de solution | Hypothèses utiles | Conclusion | Limite pour la question active |
|---|---|---|---|---|
| Escauriaza--Seregin--Šverák, *$L_{3,\infty}$-solutions of the Navier--Stokes equations and backward uniqueness*, *Russian Math. Surveys* 58(2) (2003), 211--250, [DOI 10.1070/RM2003v058n02ABEH000609](https://doi.org/10.1070/RM2003v058n02ABEH000609), **publié** | (1), problème de Cauchy; la notation historique $L_{3,\infty}$ désigne ici $L^\infty_tL^3_x$ | borne endpoint en $L^3_x$ fort | régularité | Exclut RSS/DSS/RDSS dont l'orbite reste dans $L^3$ fort; ne traite pas le Lorentz spatial $L^{3,\infty}_x$. |
| Bradshaw--Tsai, *Rotationally Corrected Scaling Invariant Solutions to the Navier--Stokes Equations*, *Comm. PDE* 42(7) (2017), 1065--1087, [DOI 10.1080/03605302.2017.1323922](https://doi.org/10.1080/03605302.2017.1323922), [arXiv:1610.05680v1](https://arxiv.org/abs/1610.05680), **publié** | (1), espace entier et demi-espace; solutions faibles/énergétiques perturbées **forward** | données initiales arbitrairement grandes dans $L^3_w=L^{3,\infty}$, avec symétrie RSS/RDSS forward | construction de solutions forward tournées | L'appendice 5 formule le problème backward sous la borne Type I comme ouvert; aucune exclusion backward. |
| Chae--Wolf, *Removing Discretely Self-Similar Singularities for the 3D Navier--Stokes Equations*, *Comm. PDE* 42(9) (2017), 1359--1374, [DOI 10.1080/03605302.2017.1358275](https://doi.org/10.1080/03605302.2017.1358275), [arXiv:1610.09464v2](https://arxiv.org/abs/1610.09464), **publié** | (1), $\mathbb R^3\times(-\infty,0)$, solution $C^\infty$ exactement $\lambda$-DSS | $\lvert u\rvert\le C_*/(\lvert x\rvert+\sqrt{-t})$ | théorème 1.3 : $u=0$ si $1<\lambda<\lambda_*(C_*)$ | Pas de rotation; période courte et solution lisse. La preuve est une compacité $\lambda\to1$, pas une observabilité du générateur à une tranche. |
| Guevara--Phuc, *Leray's Self-Similar Solutions to the Navier--Stokes Equations with Profiles in Marcinkiewicz and Morrey Spaces*, *SIAM J. Math. Anal.* 50(1) (2018), 541--556, [DOI 10.1137/16M110099X](https://doi.org/10.1137/16M110099X), [arXiv:1509.08177v2](https://arxiv.org/abs/1509.08177), **publié** | équation stationnaire de Leray sans terme rotationnel; profil faible $W^{1,2}_{\rm loc}$ | $U\in L^{3,\infty}$, cas du théorème 1.3 | $U=0$ | Ne s'applique pas à (8) lorsque $\alpha\mathcal RU\ne0$. |
| Chae, *Removing Rotated Discretely Self-Similar Singularity for the Euler Equations*, *J. Differential Equations* 377 (2023), 113--120, [DOI 10.1016/j.jde.2023.08.037](https://doi.org/10.1016/j.jde.2023.08.037), **publié** | Euler incompressible 3D, donc viscosité nulle | singularité isolée et décroissance de la vorticité à l'infini | exclusion RDSS dans la classe énoncée | Mauvaise équation pour Clay; le maximum principle eulérien ne fournit pas le terme coercif visqueux de (1). |
| Grujić--Xu, *Time-Global Regularity of the Navier--Stokes System with Hyper-Dissipation: Turbulent Scenario*, *Ann. PDE* 11, art. 9 (2025), [DOI 10.1007/s40818-025-00199-y](https://doi.org/10.1007/s40818-025-00199-y), [arXiv:2012.05692v5](https://arxiv.org/abs/2012.05692), **publié** | $\partial_tu+(-\Delta)^\beta u+u\cdot\nabla u+\nabla p=0$, $1<\beta<5/4$ | scénarios de parcimonie et profils dynamiquement rescalés presque auto-similaires | régularité de scénarios hyperdissipatifs | Modèle voisin : $\beta>1$, pas le Laplacien standard $\beta=1$. |
| Pineau--Vicol, *On Rotated Backwards Self-Similar Solutions of the Incompressible 3D Navier--Stokes Equations*, [arXiv:2607.09619v2](https://arxiv.org/abs/2607.09619v2), v1 du 10 juillet, v2 du 6 août 2026, **prépublication** | (1), profils RSS/RDSS globaux lisses; critère local sur $B_1\times[-1,0)$ | Type I ponctuel, symétrie exacte pour les théorèmes globaux; petit générateur à une tranche pour le critère local | exclusions partielles RSS/RDSS et régularité locale quantitative | Résultat direct le plus proche, mais non publié et plus fort que suitable faible-$L^3$. |

## 3. Audit exact de Pineau--Vicol v2

La notice arXiv primaire donne `2607.09619v2`, soumission le 10 juillet 2026,
révision le 6 août 2026, 37 pages et le commentaire « Additional results and
comments added ». Elle ne contient au jour de coupure ni champ DOI ni
`journal-ref`. Le mot « published » parfois affiché par des moteurs désigne la
mise en ligne arXiv, pas une publication évaluée.

### 3.1 RSS : théorème 1.4

Les hypothèses sont :

- solution de (1) sur $\mathbb R^3\times[-1,0)$;
- borne globale $|u(x,t)|\le C_{U,0}/(|x|+\sqrt{-t})$;
- ansatz RSS backward exact (6), avec $U\in C^2(\mathbb R^3)$;
- $C_{U,0}$ indépendant de $\alpha$.

Il existe

\[
 0<\underline\alpha(C_{U,0})\ll1
 \quad\text{et}\quad
 1\ll\overline\alpha(C_{U,0})<\infty                     \tag{10}
\]

tels que $U=0$ si $|\alpha|<\underline\alpha$ ou
$|\alpha|>\overline\alpha$. Le cas $\alpha$ d'ordre un reste explicitement
ouvert. Les seuils ne sont pas uniformes en la taille Type I.

### 3.2 DSS/RDSS : théorèmes 1.6 et 1.7

Le théorème 1.6 retrouve Chae--Wolf pour une DSS lisse : à constante Type I
fixée, $U=0$ si $1<\lambda<\bar\lambda(C_{U,0})$.

Pour la RDSS, le profil $U(y,s)\in C^2(\mathbb R^3\times[0,S])$ est périodique
de période $S=2\log\lambda$. Le théorème 1.7 donne deux régimes :

\[
 \begin{aligned}
 |\alpha|&\le\underline\alpha(C_{U,0}),
 &1<\lambda&<\underline\lambda(C_{U,0}),\\
 |\alpha|&\ge\overline\alpha(C_{U,0}),
 &1<\lambda&<\overline\lambda(C_{U,0})^{1/(1+\alpha^2)}.
 \end{aligned}                                           \tag{11}
\]

Le second régime équivaut quantitativement à
$S(1+\alpha^2)\ll1$. Il ne suffit donc pas de prendre une rotation grande à
période fixée.

### 3.3 Petit générateur à une tranche : théorème 1.9

Le théorème considère une solution **lisse** sur
$B_1\times[-1,0)$ telle que

\[
 |u(x,t)|\le\frac{C_u}{\sqrt{-t}+|x|},                    \tag{12}
\]

et $|p|\le C_p$ sur
$\{1/2<|x|<3/4\}\times[-1,0)$. Il existe
$\delta_0(C_u)>0$ et $s_0(C_u,C_p)$ tels que, si à une seule tranche
$\bar s\ge s_0$,

\[
 \|\partial_sV(\bar s)\|_{L^\infty(B_{e^{\bar s/2}})}
 \le\delta_0,                                             \tag{13}
\]

alors $(0,0)$ est régulier. La remarque 1.11 permet de remplacer (13) par

\[
 \int_{B_{e^{\bar s/2}}}|\partial_sV(y,\bar s)|
 (1+|y|)e^{-|y|^2/8}\,dy\lesssim\delta_0.                 \tag{14}
\]

La note 27 attachée à la proposition 9.5 précise que l'hypothèse annulaire de
pression, non quantitative, peut être remplacée par l'hypothèse que $(u,p)$
est une solution faible adaptée dans $Q_1$, toujours sous (12). Cette note ne
supprime pas à elle seule les autres hypothèses de régularité nécessaires pour
donner un sens fort à (13) dans le théorème 1.9.

## 4. La véritable estimation générateur--enstrophie

À la tranche $s=\bar s$, Pineau--Vicol introduisent

\[
 \Pi=P+\frac12|V|^2+\frac12y\cdot V,
 \qquad
 \bar L=-\Delta+(V+\tfrac12y)\cdot\nabla.                 \tag{15}
\]

L'identité ponctuelle (9.20) est

\[
 \bar L\Pi+|\Omega|^2
 =-(V+\tfrac12y)\cdot\partial_sV.                         \tag{16}
\]

Soit $w_R>0$ la fonction propre principale de $\bar L^*$ dans $B_R$, nulle
au bord, de valeur propre $\lambda_R\ge0$. L'intégration de (16) donne
l'identité exacte (9.21)

\[
 \begin{split}
 \int_{B_R}|\Omega|^2w_R={}&
 -\lambda_R\int_{B_R}\Pi w_R
 -\int_{\partial B_R}\Pi\,\partial_nw_R\\
 &-\int_{B_R}(V+\tfrac12y)\cdot\partial_sV\,w_R.
 \end{split}                                               \tag{17}
\]

Les bornes gaussiennes sur $w_R$, le contrôle de pression et
$\lambda_R\lesssim R^{-2}$ produisent (9.25) :

\[
 \int_{B_R}|\Omega(\bar s)|^2w_R
 \le K_1(C_u,C_p)R^{-2}+K_2(C_u)\delta_0.                 \tag{18}
\]

Une inégalité de Harnack convertit (18) en petite enstrophie non pondérée sur
une boule fixe. Le lemme 9.4 propage cette petitesse vers les temps similaires
ultérieurs, puis un critère $\varepsilon$-régulier de
Caffarelli--Kohn--Nirenberg conclut.

### Ce que (18) est, et ce qu'elle n'est pas

- C'est une observabilité **à une tranche**, du défaut de stationnarité vers
  l'enstrophie locale, modulo un défaut de bord $R^{-2}$.
- Ce n'est pas une borne de $\partial_sV$ obtenue depuis l'énergie de Leray.
- Ce n'est pas une identité de flux cinétique inter-échelles.
- Le côté droit utilise la norme absolue pondérée de $\partial_sV$, pas une
  moyenne signée susceptible d'annulations.
- Le poids $w_R$ est construit à partir de l'adjoint d'un opérateur dont la
  dérive contient $V$; ce n'est pas un poids universel fixé a priori.
- Les constantes et les bornes gaussiennes reposent sur le contrôle ponctuel
  Type I et les estimations de dérivées qui en découlent.
- La pression non locale réapparaît dans les deux termes de bord de (17).

Ainsi, (18) est exactement le maillon primaire le plus proche du raccord
générateur--énergie demandé, mais il ne ferme pas le raccord suitable
faible-$L^3$ et son statut reste `PREPRINT_CLAIM`.

## 5. Obstruction : l'énergie radiale ne voit pas une orbite de rotation

Pour un poids radial lisse $a=a(|y|)$, posons

\[
 E_a(V)=\int_{\mathbb R^3}|V(y)|^2a(|y|)\,dy.              \tag{19}
\]

Comme $J$ est antisymétrique, $\nabla\cdot(Jy)=0$ et
$(Jy)\cdot\nabla a=0$, une intégration par parties donne, pour un champ lisse
assez décroissant,

\[
 \begin{split}
 DE_a(V)[\mathcal RV]
 &=2\int aV\cdot JV
   -\int a(Jy)\cdot\nabla|V|^2\\
 &=0.                                                       \tag{20}
 \end{split}
\]

Par (7), une RSS peut donc vérifier

\[
 \frac{d}{ds}E_a(V(s))=0
 \quad\text{tout en ayant}\quad
 \|\partial_sV\|_X=|\alpha|\|\mathcal RV\|_X>0.          \tag{21}
\]

La même invariance vaut pour une énergie radiale de la vorticité. En
conséquence, aucune estimation du type

\[
 \|\partial_sV\|_X
 \le C\left|\frac{d}{ds}E_a(V)\right|                     \tag{22}
\]

ne peut être vraie sur une classe contenant des orbites rotationnelles non
triviales. Pour une vraie solution de (1), (21) ne dit **pas** que chaque flux
de bord est nul : dissipation, transport, pression et flux de coupure peuvent
se compenser dans le bilan. Elle dit seulement que la variation d'une énergie
radiale est aveugle à la direction tangentielle du groupe.

Pineau--Vicol évitent précisément (22) :

- pour $|\alpha|\ll1$, ils bornent l'enstrophie pondérée par une erreur
  proportionnelle à $|\alpha|$;
- pour $|\alpha|\gg1$, la proposition 6.5 montre, sous les bornes Type I et de
  dérivées,

  \[
   |\alpha|\|\mathcal RU\|_{L^2(e^{-|y|^2/4}dy)}le\varepsilon
                                                               \tag{23}
  \]

  lorsque $|\alpha|$ dépasse un seuil dépendant de
  $(\varepsilon,C_{U,0})$;
- à une tranche non exactement RSS, ils emploient l'identité de Bernoulli
  (16), et non la dérivée d'une énergie radiale.

## 6. Réponse exacte pour suitable faible-$L^3$

Considérons l'hypothèse seulement

\[
 (u,p)\text{ faible adaptée},\qquad
 \operatorname*{ess\,sup}_{t<0}
 \|u(t)\|_{L^{3,\infty}(\mathbb R^3)}<\infty,              \tag{24}
\]

plus une covariance RSS ou RDSS distributionnelle.

### Ce qui est exclu

- Si le Lorentz faible de (24) est renforcé en $L^3_x$ fort uniforme, le
  théorème endpoint d'Escauriaza--Seregin--Šverák donne la régularité. Une
  solution backward exactement RSS/DSS/RDSS régulière au sommet ne peut alors
  porter un profil singulier non nul.
- Si la RSS est lisse et vérifie la borne ponctuelle Type I, Pineau--Vicol
  exclut les rotations petites ou grandes.
- Si la RDSS est lisse, Type I, de période assez courte et dans l'un des
  régimes de rotation de (11), Pineau--Vicol l'exclut.
- Si $\mathcal RU=0$, le profil est axisymétrique autour de l'axe choisi et la
  prétendue rotation n'engendre aucune activité tangentielle dans (7).

### Ce qui n'est pas exclu par ces théorèmes

- profil seulement $L^{3,\infty}$ sans majorant
  $C/(1+|y|)$;
- solution seulement faible adaptée avec générateur défini en topologie
  négative;
- RSS Type I à rotation intermédiaire;
- RDSS à période arbitraire ou à rotation intermédiaire;
- activité apériodique ou rotation dont l'axe/vitesse dérive avec $s$;
- petite dérivée moyenne sur fenêtres au lieu de (13) ou (14) à une tranche;
- obtention de (13)/(14) depuis la seule inégalité d'énergie locale.

Il n'existe donc pas, dans le corpus audité, de théorème général

\[
 \text{suitable}+L^\infty_tL^{3,\infty}_x
 +\text{ activité seulement rotationnelle}
 \Longrightarrow u=0\text{ ou point régulier}.             \tag{25}
\]

Cette phrase décrit la frontière des théorèmes vérifiés; elle ne revendique
ni l'existence d'une solution non triviale satisfaisant (25), ni une preuve
que le problème est ouvert dans toute formulation imaginable.

## 7. Le raccord générateur--flux est-il déjà publié ?

Trois mécanismes différents doivent être séparés.

1. **Compacité de périodes courtes, publiée.** Chae--Wolf 2017 fait tendre
   $\lambda\to1$ et extrait une limite BSS. C'est un argument par
   contradiction sur une suite de solutions lisses Type I, non une inégalité
   quantitative qui estime le flux depuis $\partial_sV$.
2. **Rigidité pondérée quantitative, prépubliée.** Pineau--Vicol v2 fournit
   (17)--(18), puis propagation et $\varepsilon$-régularité. C'est le raccord
   le plus proche, mais avec des hypothèses ponctuelles fortes et sans
   dérivation de la petitesse du générateur depuis l'énergie.
3. **Énergie locale suitable, publiée classiquement.** Elle contrôle la
   dissipation intégrée et les flux testés, mais aucun résultat primaire
   identifié ne la rend strictement coercive dans la direction tangentielle
   aux rotations; (20) montre pourquoi une simple énergie radiale ne peut le
   faire.

Le maillon encore manquant pour le programme actif peut être formulé ainsi :

\[
 \begin{gathered}
 (u,p)\text{ suitable},\quad
 \sup_s\|V(s)\|_{L^{3,\infty}}\le M,\\
 \text{défaut renormalisé/flux contrôlé sur une fenêtre alignée}
 \end{gathered}
 \Longrightarrow
 \int_{B_R}|\Omega(s_*)|^2\le\varepsilon                 \tag{26}
\]

avec $R$, $\varepsilon$ et toutes les constantes indépendants des
troncatures, et avec une observable qui sépare la rotation du défaut réel de
stationnarité. Ni (18), ni Chae--Wolf, ni l'énergie locale classique ne donne
(26) sous ces seules prémisses.

## 8. Recherche d'absence bornée

La veille a été exécutée à la date de coupure dans :

- l'API primaire arXiv, avec les requêtes exactes
  `rotated + Navier-Stokes`, `rotationally + self-similar + Navier-Stokes`,
  `discretely self-similar + backward + Navier-Stokes`,
  `scaling generator + Navier-Stokes`,
  `self-similar time + Navier-Stokes`,
  `approximately self-similar + Navier-Stokes` et
  `weighted enstrophy + Navier-Stokes`;
- Crossref, du 1er janvier 1990 au 15 août 2026, avec les titres/termes
  `rotated backward self-similar`, `approximately self-similar regularity`,
  `scaling generator`, `renormalized generator` et `weighted enstrophy`;
- les références des PDF Pineau--Vicol v2, Bradshaw--Tsai et Chae--Wolf.

Après reclassement par équation, sens du temps et notion de solution :

- le seul résultat arXiv direct 2025--2026 sur le générateur de dilatation de
  (1) et les RSS/RDSS backward est Pineau--Vicol v2;
- Grujić--Xu 2025 concerne $(-\Delta)^\beta$, $\beta>1$;
- Bedrossian--Germain--Harrop-Griffiths concerne des filaments **forward**;
- Chae 2023 concerne Euler sans viscosité;
- Bradshaw--Tsai 2017 construit des branches tournées **forward** et formule
  le cas backward comme problème ouvert;
- les résultats DSS backward publiés retrouvés imposent $L^3$ fort,
  convergence vers un profil, ou Type I avec période courte.

Crossref n'a retourné aucune publication correspondant au titre de
Pineau--Vicol ni au paquet exact de (26). Ce constat porte sur les sources
indexées et les chaînes interrogées. Un manuscrit non indexé, une terminologie
différente ou une publication postérieure à la coupure restent possibles.

## 9. Passe contradictoire

1. **Statut.** `arXiv:2607.09619v2` est une prépublication, même si ses
   preuves sont détaillées et ses constantes qualitativement suivies.
2. **Inclusion stricte.** Type I ponctuel implique faible-$L^3$; l'inverse est
   faux. On ne peut transférer aucun seuil $\alpha(C_{U,0})$ depuis (24).
3. **Notion de solution.** Les théorèmes globaux 1.4 et 1.7 portent sur des
   profils lisses exacts, non sur toutes les solutions faibles adaptées.
4. **Pression.** L'identité (17) contient des termes de bord de pression. La
   projection de Leray ou l'incompressibilité ne les annule pas dans ce calcul
   local.
5. **Rotation intermédiaire.** Petite et grande rotation ne couvrent pas par
   continuité la zone médiane; les seuils dépendent de la taille Type I.
6. **Grande rotation RDSS.** Il faut simultanément raccourcir la période selon
   $S(1+\alpha^2)\ll1$.
7. **Énergie aveugle.** Une dérivée d'énergie radiale n'observe pas
   $\mathcal RV$; confondre « énergie constante » et « générateur nul » serait
   une erreur de symétrie.
8. **Flux.** (18) contrôle l'enstrophie via Bernoulli et un poids adjoint; la
   présenter comme une coercivité universelle du flux énergétique serait
   inexact.
9. **Une tranche.** Le théorème 1.9 demande une norme absolue petite à une
   tranche tardive; une moyenne signée, une récurrence ou une petitesse sur une
   fenêtre non alignée ne suffit pas.
10. **Modèles voisins.** Les théorèmes Euler, hyperdissipatifs et les
    constructions forward ne sont pas des arêtes vers Clay sans lemme de
    raccord séparé.

## 10. Traçabilité des textes audités

| PDF primaire | SHA-256 |
|---|---|
| Pineau--Vicol, `2607.09619v2` | `379591AA3C1036C9140702EBE71AAAB309FE207439A57DB5CEFF893F15D0AE8E` |
| Chae--Wolf, `1610.09464v2` | `1F537BC2B6B2E7752DB275A1EB1C903782068510C4D7BCD68DBDD45D14C0EFDC` |
| Bradshaw--Tsai, `1610.05680v1` | `DE297541695B1E52AEE702930F8C5F723EFFC5DB13FA208B80CBAD7EFEE47C52` |

Les pages 7--9 et 32--35 de Pineau--Vicol v2 ont également été rendues et
inspectées visuellement afin de vérifier les exposants de (11), les domaines
de (13)--(14), la note de suitability et les termes de bord de (17).

## 11. Décision pour le programme

**CONTINUER**, mais ne pas rechercher une coercivité issue d'une énergie
radiale seule.

Le lemme à meilleure valeur informationnelle est une version robuste de
(17)--(18) pour une dérive seulement critique : construire un poids adjoint
positif et contrôler les termes de pression sous
$V\in L^{3,\infty}$, avec des constantes uniformes en $R$, ou produire un
contre-profil montrant que cela est impossible. L'observable devra être
modulée par les rotations, par exemple en mesurant

\[
 \inf_{\beta\in\mathbb R}
 \|\partial_sV-\beta\mathcal RV\|_X,                      \tag{27}
\]

et conserver séparément une équation pour le paramètre $\beta$. Sans cette
modulation, (20) laisse une direction tangentielle non coercive; sans contrôle
de pression et de trace, (17) ne passe pas à une solution faible adaptée.
