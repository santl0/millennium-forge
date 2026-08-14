# Cycle 0023 — veille primaire sur axes errants et cônes mobiles

Date de coupure : **2026-08-14**.

Périmètre : direction de vorticité à axe variable ou rotatif, cônes mobiles,
image directionnelle sur \(\mathbb S^2\), critères de double cône, BMO
logarithmique radial et scénarios de blow-up Type I/II pour Navier–Stokes
incompressible 3D.

Type de revue : passe bibliographique distincte de la dérivation et du calcul
du cycle 0023. Elle est produite par la même famille de modèle que l'agent
principal et ne constitue donc pas une reproduction indépendante des preuves.

## Verdict différentiel

La veille ne trouve **aucune source primaire qui fournisse le raccord**

\[
 \xi\in \mathrm{bmo}_{1/|\log r|}
 \quad\Longrightarrow\quad
 \text{axe unitaire }e(s),\ s=\log(1/r),
 \text{ à variation sous-linéaire contrôlant les grands niveaux}.
\tag{V}
\]

Le résultat fonctionnel disponible est plus faible : les moyennes sur des
balles dyadiques ont des incréments \(O(1/k)\), donc une dérive cumulée
\(O(\log k)=o(k)\). Ces moyennes appartiennent toutefois à la boule unité,
pas à \(\mathbb S^2\), et peuvent s'annuler. Aucune source ne donne la
non-dégénérescence permettant de les normaliser en axes, ni le confinement
des directions de forte vorticité autour de ces axes.

Deux nuances resserrent le verrou.

1. Un axe qui ne varie **qu'en temps** n'est pas une échappatoire générale :
   Lei–Ren–Tian autorise implicitement un axe par tranche sous une hypothèse
   pairwise sur toute vorticité non nulle, et Miller autorise explicitement
   un plan \(v(x,t)^\perp\) variable sans aucune dérivée temporelle de \(v\).
2. Le poids \(1/|\log r|\) échoue au critère de Dini. Les sources primaires
   de BMO pondéré, ainsi que Grujić 2026, confirment qu'il permet des défauts
   oscillants du type \(\sin(\log|\log |x||)\). Il ne force donc ni limite
   directionnelle ni cône fixe.

Le sous-problème ouvert reste un **axe spatial errant entre les échelles**,
ou plusieurs axes actifs, qui échappe à tout double cône fixe tout en étant
la direction d'une vorticité solénoïdale issue d'une solution admissible.

## 1. Équation et échelle fixées

Sauf mention d'un domaine à bord, les résultats sont comparés à

\[
\partial_tu-\Delta u+(u\cdot\nabla)u+\nabla p=0,
\qquad \nabla\cdot u=0,
\qquad \omega=\nabla\times u,
\tag{NS}
\]

sur \(\mathbb R^3\), viscosité normalisée à \(1\), sans force. La remise à
l'échelle est

\[
u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),
\qquad
\omega_\lambda(x,t)=\lambda^2\omega(\lambda x,\lambda^2t).
\]

Ainsi :

- \(\|\omega\|_{L^{3/2,\infty}}\) est critique ;
- \(\|v\times\omega\|_{L^4_tL^2_x}\) est critique pour tout champ unitaire
  sans dimension \(v\) ;
- un confinement de l'image de \(\xi=\omega/|\omega|\) dans un cône est
  invariant d'échelle ;
- une borne physique \(\|\nabla v\|_\infty<\infty\) introduit une longueur et
  n'est pas uniforme sous un zoom singulier ;
- le poids \(1/|\log r|\) est borderline non-Dini et n'est pas une puissance
  de Hölder.

Une donnée Clay lisse de Schwartz engendre, avant son temps maximal, une
solution classique et mild, et sa solution de Leray–Hopf est localement une
solution faible adaptée. Les critères ci-dessous peuvent donc s'appliquer
conditionnellement, mais aucun ne produit ses propres hypothèses géométriques
depuis l'énergie.

## 2. Lei–Ren–Tian : axe fixe, axe par tranche et image sur la sphère

### Source et statut

Zhen Lei, Xiao Ren et Gang Tian, *A Geometric Characterization of Potential
Navier-Stokes Singularities*,
[arXiv:2501.08976v1](https://arxiv.org/abs/2501.08976), soumis le 15 janvier
2025.

- **Statut au 2026-08-14 :** prépublication v1, sans référence de revue.
- **Équation :** (NS), locale dans \(Q(1)=B(1)\times(-1,0)\).
- **Solution :** solution faible adaptée locale, avec pression
  \(L^{3/2}_{\rm loc}\) et inégalité locale d'énergie.
- **Preuve :** analytique revendiquée ; non reproduite dans cette revue.

Le théorème 1.1 exige un **vecteur fixe** \(e\in\mathbb S^2\) et des
constantes fixes \(M,\delta>0\) tels qu'à chaque point régulier,

\[
|\omega|\le M
\quad\text{ou}\quad
|\xi\times e|\le1-\delta.
\tag{2.1}
\]

Il conclut à la régularité dans \(\overline{Q(1/2)}\). Il ne couvre donc pas
directement un cône dont l'axe \(e=e(x,t)\) parcourt toutes les orientations.

### Corollaire pairwise : un axe temporel peut bouger

Le corollaire 1.6 est différent. Il suppose que, pour toute paire de points
réguliers **à même temps** où la vorticité est non nulle,

\[
|\xi(x,t)\times\xi(y,t)|<1-\delta,
\tag{2.2}
\]

et conclut que l'origine est régulière. Il n'impose aucune continuité en
temps. Il couvre donc, par exemple, une vorticité exactement parallèle à
\(\{\pm e(t)\}\) pour un axe mesurable qui tourne arbitrairement vite.

Plus généralement, un cône mobile par tranche, d'ouverture assez petite
pour que toutes ses directions restent uniformément séparées de
l'orthogonalité pairwise, satisfait (2.2). Deux restrictions sont décisives :

- la condition porte sur **toute vorticité non nulle**, non seulement sur
  \(|\omega|>M\) ;
- une famille radiale qui contient des directions orthogonales à deux
  échelles échoue, même si sa vitesse angulaire logarithmique tend vers zéro.

La source souligne elle-même qu'elle ne sait pas retirer la restriction aux
petites vorticités dans ce corollaire.

### Image limite sur \(\mathbb S^2\)

La source définit

\[
\mathcal I=
\bigcap_{0<r<1}\bigcap_{M>0}
\overline{\{\xi(x,t):(x,t)\in Q(r)\text{ régulier},\ |\omega|>M\}}.
\]

Son corollaire 1.5 affirme que, si l'origine est singulière, \(\mathcal I\)
rencontre tout grand cercle de \(\mathbb S^2\). Cette condition nécessaire
n'impose pas que \(\mathcal I=\mathbb S^2\). Un seul grand cercle suffit,
car deux grands cercles se rencontrent toujours. Un axe errant dont la
fermeture est l'équateur est donc **compatible** avec cette caractérisation.

## 3. Critères qui tolèrent une orientation variable

### Miller 2021 : plan variable en espace-temps

Evan Miller, *A Locally Anisotropic Regularity Criterion for the
Navier–Stokes Equation in Terms of Vorticity*, *Proceedings of the American
Mathematical Society, Series B* **8** (2021), 60–74,
[DOI 10.1090/bproc/74](https://doi.org/10.1090/bproc/74),
[arXiv:2002.02152v1](https://arxiv.org/abs/2002.02152).

- **Statut :** article publié ; arXiv est resté à v1.
- **Équation/domaine :** (NS) sur \(\mathbb R^3\).
- **Solution :** solution mild
  \(u\in C([0,T_{\max});H^1(\mathbb R^3))\).
- **Champ mobile :** \(v:\mathbb R^3\times[0,\infty)\to\mathbb S^2\),
  borné, avec \(\nabla_xv\in L^\infty_{\rm loc,t}L^\infty_x\). Aucune
  dérivée temporelle de \(v\) n'est requise.

Le théorème 1.6 donne notamment le critère critique

\[
v\times\omega\in L^4(0,T_{\max};L^2(\mathbb R^3))
\quad\Longrightarrow\quad
\text{prolongement},
\tag{3.1}
\]

avec une estimation explicite de \(\|u(t)\|_{\dot H^1}\) contenant
\(\|\nabla v\|^2_{L^\infty_tL^\infty_x}\).

Conséquences exactes :

- pour \(v(x,t)=e(t)\), \(\nabla_xv=0\), donc la rotation temporelle seule
  est admise ;
- pour \(v(x,t)=e(\log(1/|x|))\),
  \(|\nabla v|=|e'(s)|/|x|\), ce qui diverge généralement même lorsque
  \(|e'(s)|\to0\) ;
- le théorème ne transforme pas une petite oscillation moyenne BMO en la
  borne ponctuelle de gradient requise ;
- il faut encore contrôler la composante transverse \(v\times\omega\) dans
  \(L^4_tL^2_x\), contrôle non fourni par l'énergie Clay.

Miller est donc le résultat publié le plus directement formulé avec un axe
spatial variable, mais il ne couvre pas la dérive logarithmique singulière.

### Giga–Miura 2011 : continuité spatiale, axe temporel libre

Yoshikazu Giga et Hideyuki Miura, *On Vorticity Directions near
Singularities for the Navier-Stokes Flows with Infinite Energy*,
*Communications in Mathematical Physics* **303** (2011), 289–300,
[DOI 10.1007/s00220-011-1197-x](https://doi.org/10.1007/s00220-011-1197-x).

- **Statut :** publié.
- **Solution :** solution mild lisse bornée sur \(\mathbb R^3\), énergie
  éventuellement infinie.
- **Hypothèses :** borne Type I
  \(\sup_{t<T}\sqrt{T-t}\|u(t)\|_\infty<\infty\), et continuité spatiale
  uniforme de \(\xi\) dans une région de forte vorticité, uniformément près
  de \(T\).
- **Conclusion :** absence de blow-up à \(T\).

Le module est comparé seulement à temps égal ; un axe commun \(e(t)\) peut
donc tourner sans régularité temporelle. En revanche, si tous les rayons
jusqu'au cœur sont actifs et si \(e(\log(1/r))\) parcourt indéfiniment un
grand cercle, il existe des points arbitrairement proches portant des
directions séparées d'un angle fixe. La continuité uniforme échoue.

Les critères publiés de Peter Constantin et Charles Fefferman,
[*Direction of Vorticity and the Problem of Global Regularity for the
Navier–Stokes Equations*](https://doi.org/10.1512/iumj.1993.42.42034)
(1993), et de Hugo Beirão da Veiga et Luigi C. Berselli,
[*On the Regularizing Effect of the Vorticity Direction in Incompressible
Viscous Flows*](https://doi.org/10.57262/die/1356060864) (2002), ont la
même tolérance temporelle, mais exigent respectivement une cohérence spatiale
de type Lipschitz et \(1/2\)-Hölder dans la région active. Une dérive
\(|\nabla\xi|\simeq 1/(r|\log r|)\) n'entre dans aucune de ces classes.

### Domaine à bord : Barker–Prange 2020

Tobias Barker et Christophe Prange, *Scale-Invariant Estimates and
Vorticity Alignment for Navier–Stokes in the Half-Space with No-Slip
Boundary Conditions*, *Archive for Rational Mechanics and Analysis*
**235** (2020), 881–926,
[DOI 10.1007/s00205-019-01435-z](https://doi.org/10.1007/s00205-019-01435-z),
[arXiv:1906.08225v1](https://arxiv.org/abs/1906.08225).

Ce résultat publié localise, sous borne Type I, la continuité uniforme de la
direction aux ensembles de forte vorticité dans des régions de taille
\(O(\sqrt{T-t})\). Il concerne le demi-espace avec condition no-slip et ne se
transfère pas littéralement au problème Clay sur \(\mathbb R^3\). Comme
Giga–Miura, il exige une vraie continuité spatiale et non une BMO non-Dini.

## 4. Ce que donne réellement la BMO logarithmique

### Sources primaires et seuil de Dini

S. Spanne, *Some Function Spaces Defined Using the Mean Oscillation over
Cubes*, *Annali della Scuola Normale Superiore di Pisa* **19** (1965),
593–608,
[texte primaire NUMDAM](http://www.numdam.org/item/ASNSP_1965_3_19_4_593_0/),
introduit les espaces d'oscillation pondérée pertinents.

Marco Bramanti et Luca Brandolini, *Estimates of BMO Type for Singular
Integrals on Spaces of Homogeneous Type and Applications to Hypoelliptic
PDEs*, *Revista Matemática Iberoamericana* **21** (2005), 511–556,
[DOI 10.4171/RMI/428](https://doi.org/10.4171/RMI/428), rappelle et étend le
seuil exact : si

\[
\int_0^\delta \frac{\phi(r)}r\,dr<\infty,
\tag{4.1}
\]

alors les fonctions de \(\mathrm{BMO}_\phi\) sont continues avec un module
contrôlé par cette intégrale ; lorsque cette condition échoue, la classe
contient des fonctions discontinues, même non bornées. Pour
\(\phi(r)=1/|\log r|\), l'intégrale diverge. Leur terminologie est `LMO`, et
la continuité n'est plus garantie.

### Grujić 2026 : le critère vise directement les défauts errants

Zoran Grujić, *Logarithmic Depletion of Vortex Stretching and Singularity
Evasion in the 3D Navier-Stokes Equations*,
[arXiv:2607.08866v2](https://arxiv.org/abs/2607.08866), révisé le 13 juillet
2026.

- **Statut :** prépublication v2, non publiée.
- **Équation :** (NS) en formulation vorticité sur
  \(\mathbb R^3\times(0,T^*)\), \(\nu>0\), force nulle.
- **Solution/scénario :** solution régulière avant un premier temps
  singulier et singularité ponctuelle critique conditionnelle.
- **Hypothèses clés :** borne uniforme
  \(\omega\in L^\infty_tL^{3/2,\infty}_x\), profil de cœur prescrit et
  \(\xi\in L^\infty_t\mathrm{bmo}_{1/|\log r|}\) globalement en espace.
- **Nature :** preuve analytique revendiquée ; chaîne auditée
  conditionnellement dans les cycles 0014–0019, sans production des
  hypothèses amont depuis Clay.

La source dit explicitement que la classe non-Dini permet des phases comme
\(\sin(\log|\log|x||)\). Si un axe errant est réellement la direction d'une
vorticité admissible et satisfait toutes les hypothèses uniformes du
préprint, le théorème revendiqué l'exclut **directement** : aucune extraction
d'un axe fixe n'est nécessaire.

Son équation (16) donne néanmoins le seul raccord proche de (V). Pour les
moyennes \(c_k=(\xi)_{B_{2^{-k}}}\), la définition implique

\[
|c_{k+1}-c_k|\le C\phi(2^{-k})\lesssim \frac Ck,
\qquad
|c_n-c_m|\lesssim \sum_{k=m}^{n-1}\frac1k
\lesssim \log\frac nm.
\tag{4.2}
\]

Cette dérive est sous-linéaire en l'indice logarithmique, mais ce n'est pas
un axe : \(|c_k|\) peut tendre vers zéro. Même sous l'hypothèse additionnelle
\(|c_k|\ge m_0>0\), la normalisation \(e_k=c_k/|c_k|\) ne donnerait que des
incréments \(O(1/(m_0k))\), dont la somme diverge. Une rotation lente mais
infinie reste possible.

**Conclusion explicite demandée : aucune source primaire trouvée ne fournit
le raccord log-BMO \(\to\) axe unitaire à variation sous-linéaire contrôlant
les grands niveaux de vorticité.** Grujić fournit une dérive de moyennes,
pas leur non-annulation, leur normalisation ni une géométrie mono-cœur.

## 5. Test adverse fonctionnel reproductible

Ce test est une dérivation élémentaire du laboratoire, **pas** un résultat
Navier–Stokes ni une affirmation attribuée à une source. Sur
\(0<|x|<e^{-2}\), posons

\[
s(x)=\log\frac e{|x|},
\qquad
a(x)=\bigl(\cos(\log s(x)),\ \sin(\log s(x)),\ 0\bigr).
\tag{5.1}
\]

Alors :

1. \(|a|=1\), la phase \(\theta(s)=\log s=o(s)\) et
   \(\theta'(s)=1/s\to0\), mais \(a\) n'a aucune limite lorsque \(x\to0\).
2. L'image limite est l'équateur entier. Elle rencontre donc tout grand
   cercle, comme l'exige le corollaire 1.5 de Lei–Ren–Tian à un point
   singulier, et elle n'est contenue dans aucun double cône fixe strict.
3. \(|\nabla a(x)|=1/(|x|s(x))\). Le champ n'est ni uniformément continu au
   cœur ni admissible dans le critère à gradient borné de Miller.
4. Il satisfait pourtant localement
   \[
   \fint_{B_\rho(z)}|a-a_{B_\rho(z)}|
   \le \frac{C}{\log(e/\rho)}.
   \tag{5.2}
   \]

Pour (5.2), si \(|z|\le2\rho\), on compare à \(a(3\rho)\) et on intègre
\(\log(1+\log(3\rho/r)/s(3\rho))\) avec le poids volumique \(r^2dr\). Si
\(|z|>2\rho\), l'inégalité de Poincaré et la borne du gradient donnent

\[
\fint_{B_\rho(z)}|a-a_{B_\rho(z)}|
\lesssim
\frac{\rho}{|z|\log(e/|z|)}
\lesssim \frac1{\log(e/\rho)}.
\]

Ce champ réalise donc le comportement annoncé dans le préprint de Grujić :
log-BMO, vitesse angulaire logarithmique tendant vers zéro, mais rotation
totale infinie.

Limite essentielle du test : \(a\) n'est qu'un champ de directions. Il ne
construit pas une vorticité \(\omega=|\omega|a\) avec
\(\nabla\cdot\omega=0\), encore moins une vitesse Biot–Savart, une pression,
une inégalité locale d'énergie ou une solution de (NS). Il réfute seulement
les implications fonctionnelles « log-BMO \(\Rightarrow\) limite » et
« variation locale lente \(\Rightarrow\) cône fixe ».

## 6. Rotation auto-similaire et Type I

Ben Pineau et Vlad Vicol, *On Rotated Backwards Self-Similar Solutions of
the Incompressible 3D Navier-Stokes Equations*,
[arXiv:2607.09619v2](https://arxiv.org/abs/2607.09619), révisé le 6 août
2026.

- **Statut :** prépublication v2.
- **Équation :** (NS) non forcé sur \(\mathbb R^3\), solution lisse
  backward.
- **Objet :** profils exactement invariants sous dilatation parabolique et
  rotation autour d'un axe fixe à vitesse angulaire constante en temps
  similaire ; variantes RDSS.
- **Conclusion :** sous borne Type I, trivialité pour rotations assez petites
  ou assez grandes ; résultats RDSS analogues avec facteur proche de \(1\),
  et critère local quasi-auto-similaire.

Cette source traite une rotation structurée et récurrente en temps similaire.
Elle ne traite ni une phase radiale \(\theta(s)=\log s\), ni une loi de
rotation apériodique, ni le régime Type II. Le régime de rotation constante
intermédiaire demeure en outre ouvert dans la prépublication.

Le rapprochement « axe errant = rotated self-similar » serait donc faux sans
un lemme identifiant une symétrie exacte de l'équation et une convergence du
profil dans les espaces du théorème.

## 7. Type II : aucun critère directionnel transférable trouvé

Les versions primaires récentes pertinentes restent :

| Source | Statut au 2026-08-14 | Objet | Écart avec l'axe errant |
|---|---|---|---|
| Gregory Seregin, [arXiv:2606.29468v1](https://arxiv.org/abs/2606.29468) | préprint v1, 28 juin 2026 | scénarios Type II locaux, zoom d'échelle Euler | aucune hypothèse de cône mobile ou log-BMO ; l'équation limite est Euler |
| Gregory Seregin, [arXiv:2402.13229v3](https://arxiv.org/abs/2402.13229) | préprint v3, 8 août 2026 | Type II axisymétrique, zoom Euler | axisymétrie exacte et hypothèses supplémentaires ; pas d'axe errant général |
| Grujić, [arXiv:2607.08866v2](https://arxiv.org/abs/2607.08866) | préprint v2 | concentration critique faible-\(L^{3/2}\) | la borne critique uniforme et le profil prescrits n'englobent pas un Type II général |
| Giga–Miura 2011 | publié | Type I mild borné | Type II explicitement hors hypothèses |
| Pineau–Vicol 2026 | préprint v2 | Type I RSS/RDSS | Type II et dérive apériodique hors hypothèses |

Dans les zooms Type II de Seregin, la viscosité disparaît et la limite est une
solution ancienne Euler. Les critères Lei–Ren–Tian, Miller, Giga–Miura et
Grujić portent sur Navier–Stokes visqueux et ne peuvent être appliqués à cette
limite sans nouveau théorème. Réciproquement, les Liouville Euler de Seregin
requièrent des bornes pondérées ou symétries non produites par une simple loi
de direction.

Une recherche primaire ciblée jusqu'au 14 août 2026 n'a révélé aucune version
plus récente des prépublications ci-dessus ni un nouveau théorème sur cônes
mobiles couvrant un axe \(e(\log(1/r))\) apériodique.

## 8. Matrice de transfert vers Clay

| Géométrie supposée près d'un premier point singulier | Source la plus proche | Transfert exact | Maillon manquant |
|---|---|---|---|
| toute forte vorticité dans un double cône fixe | Lei–Ren–Tian v1, théorème 1.1 | solution Clay locale adaptée \(\Rightarrow\) régularité conditionnelle | produire le cône depuis (NS) |
| toutes les directions non nulles alignées autour de \(e(t)\), pairwise loin de \(\pi/2\) | Lei–Ren–Tian v1, corollaire 1.6 | l'axe temporel peut être arbitraire | contrôle requis jusque dans la petite vorticité |
| composante de \(\omega\) dans le plan mobile \(v(x,t)^\perp\) contrôlée | Miller 2021 | prolongement si \(\nabla_xv\in L^\infty\) et \(v\times\omega\in L^4_tL^2_x\) | le gradient d'un axe radial errant diverge |
| direction uniformément continue sur les grands niveaux | Giga–Miura 2011 | exclusion publiée sous Type I | log-BMO non-Dini et Type II hors champ |
| direction globale uniforme log-BMO + vorticité critique | Grujić v2 | exclusion conditionnelle revendiquée sans axe fixe | hypothèses amont, zéros, multi-cœurs et preuve éditoriale |
| axe \(e(s)\) à rotation exacte constante en temps similaire | Pineau–Vicol v2 | exclusions Type I pour rotations extrêmes | rotation intermédiaire, dérive apériodique et Type II |
| axe radial sous-linéaire extrait de log-BMO | aucune | seulement dérive \(O(\log k)\) des moyennes | non-annulation, normalisation, contrôle des grands niveaux, admissibilité NS |

## 9. Décision scientifique

- **Résultat positif de veille :** la rotation temporelle pure est déjà
  couverte par des critères publiés/annoncés sous hypothèses spatiales ; elle
  ne doit plus être présentée comme le verrou.
- **Résultat négatif :** aucune source ne convertit la BMO logarithmique en
  axe unitaire mobile contrôlant une vorticité de solution.
- **Test adverse :** (5.1) montre qu'une phase
  \(\theta(s)=\log s=o(s)\), avec \(\theta'(s)\to0\), peut appartenir à la
  classe log-BMO tout en parcourant un grand cercle entier et en échappant à
  tout cône fixe.
- **Écart Clay :** aucune dynamique, pression, contrainte solénoïdale ou
  compacité ne force une moyenne directionnelle non dégénérée à toutes les
  échelles ; Type II peut en outre conduire à Euler.
- **Statut :** **CONTINUER** sur `GAP-WANDERING-AXIS-PROFILE`, mais définir
  l'axe comme une dérive **spatiale inter-échelles**, non comme une simple
  rotation en temps.
- **Prochain lemme minimal :** sous une hypothèse explicitement
  solution-admissible, établir ou réfuter une borne uniforme
  \[
  |(\xi)_{B_r\cap\{|\omega|>M(r)\}}|\ge m_0>0
  \]
  et quantifier les incréments de sa normalisation. Sans cette
  non-dégénérescence, le passage des moyennes log-BMO à un axe est impossible.
- **Prochain test décisif :** imposer la direction (5.1) à une amplitude
  critique \(r^{-2}\), résoudre exactement la contrainte
  \(\nabla\cdot\omega=0\) par harmoniques sphériques, puis mesurer si le coût
  de correction détruit la faible norme \(L^{3/2,\infty}\) ou crée un défaut
  Navier–Stokes non sommable.
