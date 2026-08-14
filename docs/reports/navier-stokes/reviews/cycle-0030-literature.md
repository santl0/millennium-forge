# Cycle 0030 — veille primaire : assemblages de tubes et blocs compacts

Date de coupure : 2026-08-14 (Europe/Paris).

Périmètre : ensembles finis ou croissants d'anneaux et de tubes de vortex,
Biot–Savart et espaces de Lorentz sur supports disjoints, cohérence des
directions, packing/capacité, vitesses divergence-free compactes et veille
différentielle 2025–2026.

Statut : revue bibliographique contradictoire indépendante. Les calculs
signalés « recalculé ici » sont des dérivations du laboratoire, jamais des
`PAPER_PROOF`.

## Verdict exécutif

1. La disjonction des **supports de vorticité** n'annule pas les interactions :
   Biot–Savart est non local et chaque vitesse traverse en général tous les
   autres cœurs. La disjonction des **supports de vitesse** est différente.
   Si l'on choisit d'abord des vitesses compactes divergence-free
   \(u_j\), puis \(\omega_j=\nabla\times u_j\), alors
   \(\operatorname{BS}[\omega_j]=u_j\) exactement et l'interaction
   cinématique extérieure est nulle à l'instant initial.
2. Pour des blocs à supports disjoints et de même forme, les distributions
   de niveau de la vorticité s'additionnent, tandis que
   \(\|\sum u_j\|_3^3=\sum\|u_j\|_3^3\). Cette différence d'exposants ferme
   négativement les empilements à une seule échelle, mais autorise un
   empilement sur des échelles très séparées.
3. Un contre-profil explicite, recalculé ici, donne des données Clay lisses
   compactes \(U_N\) telles que
   \[
   \|\nabla\times U_N\|_{L^{3/2,\infty}}\to0,
   \qquad \|U_N\|_{L^3}=c_0>0.
   \]
   Il ne contredit aucune estimation connue : simultanément
   \(\|U_N\|_{L^{3,\infty}}\to0\). Pour \(N\) grand, la petite donnée faible
   \(L^3\) place donc ces profils dans une classe globale perturbative.
   Une norme forte \(L^3\) non dégénérée n'est pas un test suffisant pour
   éviter les théories de petite donnée.
4. Le packing volumique contrôle les défauts directionnels seulement s'il
   est logarithmiquement parcimonieux dans **toute** boule. La capacité
   newtonienne, qui compte les rayons plutôt que les volumes, n'est ni une
   condition suffisante ni un substitut au contrôle all-ball log-BMO.
5. Le verrou restant est interne à chaque bloc : une direction de vorticité
   présentant une oscillation d'ordre un à l'échelle du support produit un
   coût \(|\log r_j|\) après concentration. Une extension choisie sur
   \(\{\omega=0\}\) peut réparer le corridor extérieur, mais pas les
   oscillations sur le support actif.
6. Les résultats 2025–2026 sur plusieurs anneaux ou hélices sont des
   constructions Euler ou des régimes filamentaires Navier–Stokes déjà
   globaux. Aucun ne suit simultanément le nombre de tubes, une norme
   faible-\(L^{3/2}\), la direction log-BMO, la pression et une limite
   \(N\to\infty\).
7. Le lemme porosité–Hedberg proposé est vrai, avec preuve interne courte,
   si la variation totale vérifie
   \(|\mu|(B(x,r))\le Dr^3\) à **toutes** les échelles :
   \(\|I_1|\mu|\|_\infty\lesssim D^{2/3}M^{1/3}\), puis HLS donne
   \(\|I_1|\mu|\|_2\lesssim D^{1/6}M^{5/6}\). Une porosité seulement
   au-dessus du rayon de cœur ne suffit pas sans un contrôle supplémentaire
   des échelles inférieures.

## 1. Cadre exact et quantités critiques

Le problème Clay entier est Navier–Stokes incompressible, non forcé, sur
\(\mathbb R^3\), avec \(\nu>0\) et donnée initiale lisse rapidement
décroissante :

\[
\partial_tu+(u\cdot\nabla)u=-\nabla p+\nu\Delta u,
\qquad \nabla\cdot u=0.
\]

Sous

\[
u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),
\qquad
\omega_\lambda(x,t)=\lambda^2\omega(\lambda x,\lambda^2t),
\]

les normes \(L^3\) et \(L^{3,\infty}\) de la vitesse, ainsi que
\(L^{3/2,\infty}\) de la vorticité, sont critiques. On fixe la quasi-norme

\[
\|f\|_{L^{p,\infty}}^*
=\sup_{\alpha>0}\alpha
 |\{x:|f(x)|>\alpha\}|^{1/p}.
\]

Les constructions filamentaires citées plus loin doivent être distinguées :
Euler a \(\nu=0\), une symétrie hélicoïdale produit souvent une structure
infinie dans la direction axiale, et une vorticité compacte dans chaque
**section** n'est pas une donnée compacte dans \(\mathbb R^3\).

## 2. Supports disjoints et Biot–Savart

### 2.1 Ce que donne exactement la disjonction

Si \(f_j\) ont des supports deux à deux disjoints, alors

\[
|\{|\textstyle\sum_j f_j|>\alpha\}|
=\sum_j|\{|f_j|>\alpha\}|.
\]

Il s'ensuit, pour \(p>0\),

\[
\left\|\sum_jf_j\right\|_{L^{p,\infty}}^*
\le
\left(\sum_j\|f_j\|_{L^{p,\infty}}^{*p}\right)^{1/p}.
\tag{2.1}
\]

L'inégalité peut être saturée pour des copies de même amplitude et de même
échelle. Elle n'est pas une équivalence uniforme lorsque les amplitudes et
les échelles sont séparées : la quasi-norme faible ne somme que les blocs
visibles au même seuil.

En revanche, pour \(p=3\), la disjonction donne l'identité forte

\[
\left\|\sum_ju_j\right\|_3^3=\sum_j\|u_j\|_3^3.
\tag{2.2}
\]

Les sources déjà cataloguées `NS-SRC-0067` (O'Neil) et `NS-SRC-0097`
(Lorentz) suffisent pour le cadre Lorentz. L'identité de distribution et
(2.1) sont recalculées ici avec la convention affichée.

### 2.2 Deux notions de support à ne pas confondre

Pour des vorticités compactes disjointes,

\[
u=\sum_j\nabla\times(-\Delta)^{-1}\omega_j
\]

n'a en général aucun support disjoint. Même si chaque impulsion est annulée,
les multipôles suivants créent des queues et des interactions.

On peut inverser la construction. Soient
\(u_j\in C_c^\infty(\mathbb R^3)^3\),
\(\nabla\cdot u_j=0\), avec supports disjoints, et posons
\(\omega_j=\nabla\times u_j\). Alors l'identité de Hodge donne

\[
\nabla\times(-\Delta)^{-1}\omega_j=u_j.
\tag{2.3}
\]

Chaque bloc satisfait donc automatiquement l'infinité de compatibilités
multipolaires nécessaire à une vitesse compacte. Cela ne demande pas que le
bloc soit une solution d'Euler : prendre un potentiel vectoriel compact
\(A\) et \(u=\nabla\times A\) fournit déjà une donnée initiale admissible.

Les travaux de Gavrilov (`NS-SRC-0107`) et de Constantin–La–Vicol
(`NS-SRC-0108`) montrent davantage : on peut choisir un bloc non trivial qui
est une solution stationnaire lisse et compacte d'Euler. Des copies
translatées et remises à l'échelle, avec leurs pressions normalisées et
supports complets disjoints, peuvent être sommées en un état stationnaire
d'Euler fini. Cela reste inviscide. Pour Navier–Stokes, le terme
\(\nu\Delta u\) diffuse immédiatement chaque bloc.

### 2.3 Pression et projection de Leray

Même si \(u_i u_j=0\) ponctuellement pour \(i\ne j\),

\[
-\Delta p=\partial_i\partial_j(u_i u_j)
\]

est non local. Pour des blocs arbitraires, la projection
\(\mathbb P\nabla\cdot(u\otimes u)\) a donc des queues. Une somme de blocs
stationnaires Euler localisables évite ce défaut à l'instant initial parce
que chaque non-linéarité projetée est nulle ; elle ne contrôle pas les temps
positifs visqueux. La disjonction initiale n'est jamais un argument de
découplage dynamique uniforme.

## 3. Barrière à une échelle et échappement multi-échelle

### 3.1 Copies critiques d'un bloc compact

Fixons un bloc non nul
\(u_0\in C_c^\infty(B(0,1))^3\), divergence-free, et
\(\omega_0=\nabla\times u_0\). Pour un rayon \(r_j\), un centre \(c_j\) et
un coefficient sans dimension \(a_j\), posons

\[
u_j(x)=a_jr_j^{-1}u_0\!\left(\frac{x-c_j}{r_j}\right),
\qquad
\omega_j(x)=a_jr_j^{-2}\omega_0\!\left(\frac{x-c_j}{r_j}\right).
\tag{3.1}
\]

Alors

\[
\|u_j\|_3=|a_j|\|u_0\|_3,
\qquad
\|\omega_j\|_{L^{3/2,\infty}}^*
=|a_j|\|\omega_0\|_{L^{3/2,\infty}}^*.
\tag{3.2}
\]

À une échelle commune et pour des coefficients comparables, (2.1) exige un
budget de taille \(N^{2/3}|a|\) pour la vorticité, alors que
\(\|\sum u_j\|_3=N^{1/3}|a|\|u_0\|_3\). Normaliser le premier à l'ordre un
force le second à décroître comme \(N^{-1/3}\). Ajouter de nombreux blocs à
une même échelle ne répare donc pas la dégénérescence du cycle 0029.

### 3.2 Contre-profil de stacking — recalculé ici

La conclusion précédente devient fausse si les échelles de pointe sont
séparées. Prenons, après une constante géométrique inoffensive,

\[
c_j=2^{-j}e_1,
\qquad r_j=2^{-j^2-10},
\qquad 1\le j\le N.
\]

Les boules \(B(c_j,r_j)\) sont disjointes et contenues dans une boule fixe.
Dans (3.1), choisissons le même coefficient
\(a_N=N^{-1/3}\) et définissons

\[
U_N=\sum_{j=1}^Nu_{j,N},
\qquad W_N=\nabla\times U_N.
\]

Chaque \(U_N\) est lisse, compacte, divergence-free et
\(\operatorname{BS}[W_N]=U_N\). Par (2.2),

\[
\|U_N\|_3^3
=Na_N^3\|u_0\|_3^3
=\|u_0\|_3^3.
\tag{3.3}
\]

Notons \(M=\|\omega_0\|_\infty\) et
\(V=|\operatorname{supp}\omega_0|\). Pour tout seuil \(\alpha\), seuls les
blocs satisfaisant \(\alpha<a_NMr_j^{-2}\) contribuent, et

\[
|\{|W_N|>\alpha\}|
\le V\sum_{r_j<(a_NM/\alpha)^{1/2}}r_j^3
\le C V(a_NM/\alpha)^{3/2}.
\]

La dernière inégalité utilise la sommabilité géométrique de la queue des
\(r_j^3\). Ainsi

\[
\|W_N\|_{L^{3/2,\infty}}^*\le C_0a_N\longrightarrow0.
\tag{3.4}
\]

Le même calcul, avec amplitude ponctuelle \(a_Nr_j^{-1}\), donne

\[
\|U_N\|_{L^{3,\infty}}^*\le C_1a_N\longrightarrow0.
\tag{3.5}
\]

Enfin,

\[
\|U_N\|_2^2
=a_N^2\|u_0\|_2^2\sum_{j=1}^Nr_j
\le C N^{-2/3}.
\]

Ce profil falsifie toute inégalité universelle
\(\|\operatorname{BS}\omega\|_3\le C
\|\omega\|_{L^{3/2,\infty}}\). L'estimation correcte à l'endpoint ne donne
que \(L^{3,\infty}\), conformément à O'Neil/HLS.

Il falsifie aussi le gate proposé au cycle 0029 : les trois conditions
« vorticité faible critique bornée, vitesse compacte, norme forte \(L^3\)
non dégénérée » peuvent être satisfaites simultanément de façon élémentaire.
Mais ce n'est pas un candidat de blow-up. Le théorème de petite donnée dans
\(L^{3,\infty}(\mathbb R^3)\) place (3.5), pour \(N\) grand, dans une classe
globale perturbative. La source primaire à ajouter pour ce raccord est
Yamazaki (2000), auditée en section 7.

## 4. Cohérence directionnelle, packing et capacité

### 4.1 Condition d'occupation suffisante

Soit \(e\in S^2\) fixe et \(\zeta=e+f\), avec \(|f|\le2\) et
\(\operatorname{supp}f\subset D\). Pour toute boule \(B\),

\[
\operatorname{MO}_B(\zeta)
\le2\fint_B|f|
\le4\frac{|B\cap D|}{|B|}.
\tag{4.1}
\]

Par conséquent, la condition de packing all-ball

\[
\sup_x\frac{|B_\rho(x)\cap D|}{|B_\rho|}
\le\frac C{|\log\rho|},
\qquad0<\rho<\tfrac12,
\tag{4.2}
\]

suffit à contrôler la partie « dilution des défauts » de la semi-norme
log-BMO. Elle ne contrôle pas les boules internes à un défaut ; celles-ci
doivent satisfaire un lemme local indépendant.

Un simple packing disjoint dans \(B_R\) donne seulement
\(\sum r_j^3\lesssim R^3\), donc une fraction volumique d'ordre un. Le
facteur \(|\log\rho|\) exige la parcimonie supplémentaire (4.2). Les
couvertures à multiplicité bornée des travaux de Dascaliuc–Grujić
(`NS-SRC-0024`) servent à comparer des moyennes d'ensemble ; elles ne
prouvent pas (4.2) pour le support réel de la vorticité et ne suppriment pas
la queue de Biot–Savart.

### 4.2 Pourquoi la capacité ne ferme pas le lemme

En dimension trois, la capacité newtonienne d'une boule est proportionnelle
à son rayon, alors que son volume est proportionnel à \(r^3\). Pour une
union de boules,

\[
\operatorname{Cap}\!\left(\bigcup_jB_j\right)
\le\sum_j\operatorname{Cap}(B_j)\asymp\sum_jr_j,
\]

mais la quantité apparaissant dans (4.1) est une densité volumique locale.
Un contrôle de \(\sum r_j\) n'impose ni (4.2), ni la cohérence interne, ni
une annulation multipolaire. Réciproquement, un packing volumique très rare
peut avoir un comportement capacitaire différent. Aucune source primaire
trouvée ne transforme une borne capacitaire de tubes en critère log-BMO de
direction pour Navier–Stokes.

### 4.3 Obstruction interne après concentration

Supposons qu'une copie du bloc de base contienne une boule relative sur
laquelle l'oscillation moyenne de
\(\xi_0=\omega_0/|\omega_0|\) est au moins \(c_0>0\). Après concentration à
l'échelle \(r_j\), une boule de rayon \(Cr_j\) a encore la même oscillation,
donc

\[
|\log r_j|\operatorname{MO}(\xi_j)\ge c_0|\log r_j|\to\infty.
\]

Attribuer une direction dans le vide autour du support ne change pas cette
boule active. Pour un empilement compact à plusieurs échelles, le lemme
directionnel doit donc produire des blocs dont l'oscillation **interne**
décroît comme \(1/|\log r_j|\), ou remplacer la condition orientée par un
critère projectif réellement applicable.

Les critères de Constantin–Fefferman et Beirão da Veiga–Berselli sont
projectifs via \(\sin\angle(\xi(x),\xi(y))\) et ne distinguent pas
\(+e\) de \(-e\). Le log-BMO vectoriel orienté les distingue. Or
\(\int\nabla\times u_j=0\) pour toute vitesse compacte : un bloc presque
unidirectionnel doit cacher une compensation ou un return-flow. C'est ce
return-flow, et non le packing extérieur, qui reste le verrou analytique.

## 5. Ensembles de vortex rings : ce que prouvent les sources

### 5.1 Plusieurs anneaux coaxiaux

**Dávila–del Pino–Musso–Wei.** J. Dávila, M. del Pino, M. Musso et J. Wei,
*Leapfrogging vortex rings for the 3-dimensional incompressible Euler
equations*, Communications on Pure and Applied Mathematics 77(10) (2024),
3843–3957, DOI
[10.1002/cpa.22199](https://doi.org/10.1002/cpa.22199),
[arXiv:2207.03263v4](https://arxiv.org/abs/2207.03263).

- Équation : Euler 3D incompressible sur \(\mathbb R^3\), \(\nu=0\),
  axisymétrique sans swirl.
- Conclusion : construction lisse de la dynamique leapfrogging de deux
  anneaux coaxiaux minces par collage inner–outer.
- Limite : nombre fini fixé, symétrie sans swirl, inviscide ; aucune
  estimation uniforme de Lorentz ou de packing lorsque le nombre croît.

**Buttà–Cavallaro–Marchioro.** P. Buttà, G. Cavallaro et C. Marchioro,
*Leapfrogging vortex rings as scaling limit of Euler Equations*, SIAM Journal
on Mathematical Analysis 57 (2025), 789–824, DOI
[10.1137/24M1642391](https://doi.org/10.1137/24M1642391),
[arXiv:2310.00732v2](https://arxiv.org/abs/2310.00732).

- Équation : Euler 3D incompressible, axisymétrique sans swirl.
- Donnée : \(N\) anneaux initiaux disjoints, très concentrés, d'épaisseur
  \(\varepsilon\), dans le régime précis de l'article.
- Conclusion : pour \(N\) fixé, convergence vers un système dynamique sur
  un temps positif ; pour deux anneaux et grand rayon, contrôle assez long
  pour plusieurs dépassements.
- Limite : la constante n'est pas annoncée uniforme pour \(N\to\infty\) ;
  le rayon principal et les masses suivent une normalisation logarithmique
  propre au scaling limit. Ce n'est pas un packing dans un domaine fixe.

Les résultats de Feng–Šverák et Lévy–Liu déjà catalogués couvrent aussi des
combinaisons de filaments circulaires visqueux, avec positivité explicite
pour l'unicité multi-filaments de Lévy–Liu. Ils n'apportent pas la limite
\(N\to\infty\) requise ici.

### 5.2 Hélices multiples

**Guerra–Musso.** I. Guerra et M. Musso, *Nearly parallel helical vortex
filaments in the three dimensional Euler equations*, Mathematische Annalen
394(1) (2026), article 25, DOI
[10.1007/s00208-026-03337-4](https://doi.org/10.1007/s00208-026-03337-4),
[arXiv:2502.01470v2](https://arxiv.org/abs/2502.01470).

- Équation : Euler 3D sur \(\mathbb R^3\), symétrie hélicoïdale sans swirl.
- Conclusion : configurations de \(N\) hélices sur un polygone régulier, et
  de \(N+1\) filaments avec un filament axial, concentrées au sens des
  distributions ; séparation transversale de l'ordre
  \(|\log\varepsilon|^{-1/2}\).
- Limite : les hélices sont infinies dans la direction axiale ; ni énergie
  globale finie ni donnée compacte Clay n'en découle. \(N\) est fixé dans la
  désingularisation.

**Averkiou–Musso.** A. Averkiou et M. Musso, *Helical vortex filaments with
compactly supported cross-sectional vorticity for the incompressible Euler
equations in \(\mathbb R^3\)*, Journal of Differential Equations 464 (2026),
114244, DOI
[10.1016/j.jde.2026.114244](https://doi.org/10.1016/j.jde.2026.114244),
[arXiv:2511.12296v1](https://arxiv.org/abs/2511.12296).

- Équation : Euler 3D, \(\mathbb R^3\), hélicoïdal sans swirl.
- Conclusion : vorticité lisse à support transverse compact autour d'une
  hélice, avec extension à plusieurs hélices sur un polygone régulier.
- Limite essentielle : « support transverse compact » ne signifie pas
  support compact tridimensionnel. La symétrie par translation-vis hérite
  d'une structure infinie en \(z\).

**Averkiou–Musso–Yu.** A. Averkiou, M. Musso et F. Yu, *Clustered vortex
helices with compactly supported cross-sectional vorticity in the 3D Euler
equations*, [arXiv:2604.09546v1](https://arxiv.org/abs/2604.09546), soumis
le 2026-04-10, 32 pages, sans référence de revue identifiée.

- Équation : Euler 3D, hélicoïdal sans swirl.
- Conclusion annoncée : solution multi-vortex lisse dans \(\mathbb R^3\),
  cluster d'hélices qui se rapprochent, vorticité transverse compacte.
- Statut : `PREPRINT_CLAIM`. Le « collapsing » porte sur la configuration
  asymptotique hélicoïdale et n'est pas un blow-up fini de Navier–Stokes.

## 6. Résultats visqueux récents sur les filaments

**Gancedo–Hidalgo-Torné.** F. Gancedo et A. Hidalgo-Torné, *On the Cauchy
problem for 3D Navier–Stokes helical vortex filament*, Advances in
Mathematics 471 (2025), 110268, DOI
[10.1016/j.aim.2025.110268](https://doi.org/10.1016/j.aim.2025.110268),
[arXiv:2311.15413v2](https://arxiv.org/abs/2311.15413).

- Équation : Navier–Stokes incompressible 3D, vorticité initiale mesure sur
  une hélice, périodicité dans une direction et symétrie hélicoïdale.
- Conclusion : bien-posé local dans le cadre filamentaire, préservation de
  la symétrie, puis prolongement global unique par solutions faibles
  d'énergie locale, sans petite circulation et sans hypothèse de swirl nul.
- Portée : résultat visqueux global positif pour un filament très structuré,
  non construction de singularité et non ensemble de \(N\to\infty\) tubes.

**Fontelos–Ispizua–Vega.** M. A. Fontelos, M. Ispizua et L. Vega,
*Evolution of viscous vortex filaments and soliton-type propagation*,
[arXiv:2607.21439v1](https://arxiv.org/abs/2607.21439), soumis le 2026-07-23,
39 pages, sans référence de revue identifiée.

- Équation : Navier–Stokes incompressible visqueux issu d'une vorticité
  portée par une courbe ouverte lisse.
- Régime : \(\nu t\ll1\) et nombre de Reynolds de circulation
  \(\Gamma/\nu\) suffisamment petit.
- Conclusion annoncée : profil principal de Lamb–Oseen autour d'une courbe
  suivant le flot binormal, perturbation contrôlée en espace de Morrey, et
  déplacement macroscopique d'une portion localisée d'énergie pour le
  soliton de Hasimoto.
- Statut : `PREPRINT_CLAIM`. Le régime de petite circulation et le temps
  admissible ne produisent aucun blow-up Clay.

Ces deux sources renforcent le verdict dynamique : la diffusion détruit la
compacité des supports, mais les régimes rigoureusement contrôlés sont
globaux ou à petite circulation, pas singuliers.

## 7. Petite donnée faible-\(L^3\) : source manquante décisive

M. Yamazaki, *The Navier–Stokes equations in the weak-\(L^n\) space with
time-dependent external force*, Mathematische Annalen 317(4) (2000),
635–675, DOI
[10.1007/PL00004418](https://doi.org/10.1007/PL00004418).

- Équation : Navier–Stokes incompressible en dimension \(n\ge3\), dans
  l'espace entier, le demi-espace ou un domaine extérieur ; le cas non forcé
  est inclus en prenant la force nulle.
- Conclusion pertinente : existence globale et unicité de petites solutions
  bornées dans le faible-\(L^n\), donc faible-\(L^3\) en dimension trois,
  sous les hypothèses exactes de l'article.
- Portée pour (3.5) : les données \(U_N\) sont lisses compactes et deviennent
  petites dans \(L^{3,\infty}\). Elles sont donc du côté régulier du seuil,
  malgré leur norme forte \(L^3\) constante.
- Prudence : le seuil dépend de \(\nu\), du domaine et de la convention de
  norme. Aucune valeur numérique n'est extraite dans cette passe.

H. Jia, *Uniqueness of solutions to Navier–Stokes equation with small
initial data in \(L^{3,\infty}(\mathbb R^3)\)*,
[arXiv:1409.8382v1](https://arxiv.org/abs/1409.8382), est une source
complémentaire ciblée sur l'unicité. Yamazaki suffit pour le raccord
existence globale utilisé ici ; Jia peut être ajouté séparément si le
registre distingue construction et unicité dans les classes faibles.

## 8. Audit du lemme porosité–Hedberg demandé au cycle

### 8.1 Énoncé exact qui est vrai

Soit \(\mu\) une mesure de Radon vectorielle finie sur \(\mathbb R^3\),
\(\sigma=|\mu|\) sa variation totale et
\(M=\sigma(\mathbb R^3)\). Supposons

\[
  \sigma(B(x,r))\le D r^3
  \qquad(x\in\mathbb R^3,\ r>0).                 \tag{8.1}
\]

Pour le potentiel non normalisé

\[
  \mathcal I_1\sigma(x)
  :=\int_{\mathbb R^3}\frac{d\sigma(y)}{|x-y|^2},
\]

on a, pour tout \(R>0\),

\[
  \mathcal I_1\sigma(x)
  \le 8DR+\frac{M}{R^2}.                         \tag{8.2}
\]

En effet, sur l'anneau
\(2^{-k-1}R<|x-y|\le2^{-k}R\), (8.1) donne au plus
\(4DR2^{-k}\). La somme sur \(k\ge0\) vaut au plus \(8DR\), et
la partie \(|x-y|>R\) vaut au plus \(M/R^2\). Le choix
\(R=(M/D)^{1/3}\) donne donc

\[
  \|\mathcal I_1\sigma\|_\infty
  \le 9D^{2/3}M^{1/3}.                           \tag{8.3}
\]

Le facteur change avec la normalisation de \(I_1\). L'exposant, lui, est
imposé par l'échelle. Pour
\(\omega_\lambda(x)=\lambda^2\omega(\lambda x)\),

\[
 D_\lambda=\lambda^2D,\qquad M_\lambda=\lambda^{-1}M,
 \qquad D_\lambda^{2/3}M_\lambda^{1/3}
 =\lambda D^{2/3}M^{1/3},
\]

comme la vitesse \(u_\lambda(x)=\lambda u(\lambda x)\).

**Statut de preuve.** La constante 9 et la forme mesure de (8.2)–(8.3)
sont **recalculées ici** par sommation dyadique ; il ne faut pas les encoder
comme un théorème cité mot à mot. La source primaire de la méthode de
séparation potentiel proche/lointain par fonction maximale est L. I.
Hedberg, *On Certain Convolution Inequalities*, Proc. Amer. Math. Soc. 36
(1972), 505–510, DOI
[`10.1090/S0002-9939-1972-0312232-4`](https://doi.org/10.1090/S0002-9939-1972-0312232-4).
La monographie de référence est D. R. Adams et L. I. Hedberg,
*Function Spaces and Potential Theory*, Grundlehren 314, Springer (1996),
DOI
[`10.1007/978-3-662-03282-4`](https://doi.org/10.1007/978-3-662-03282-4),
chapitre 3, « Estimates for Bessel and Riesz Potentials ».

### 8.2 Raccord HLS \(L^{6/5}\to L^2\)

L'hypothèse (8.1) à **toutes** les échelles force
\(\sigma=f\,dx\) avec \(f\in L^\infty\) et
\(\|f\|_\infty\lesssim D\) ; c'est une conséquence de la différentiation
de Lebesgue et de la décomposition de Radon–Nikodym. Puis

\[
 \|f\|_{6/5}
 \le \|f\|_\infty^{1/6}\|f\|_1^{5/6}
 \lesssim D^{1/6}M^{5/6}.                        \tag{8.4}
\]

L'inégalité de Hardy–Littlewood–Sobolev donne

\[
 \|I_1f\|_2\le C_{\rm HLS}\|f\|_{6/5}
 \lesssim D^{1/6}M^{5/6}.                        \tag{8.5}
\]

La source primaire moderne avec constantes optimales est E. H. Lieb,
*Sharp Constants in the Hardy–Littlewood–Sobolev and Related
Inequalities*, Ann. of Math. (2) 118 (1983), 349–374, DOI
[`10.2307/2007032`](https://doi.org/10.2307/2007032). Le passage
\(p=6/5,\alpha=1,n=3\) à \(q=2\) suit
\(1/q=1/p-\alpha/n\). Pour Biot–Savart,

\[
 |u(x)|\le \frac1{4\pi}\mathcal I_1(|\omega|)(x),
\]

donc (8.3) et (8.5) s'appliquent à \(u\), à la constante \(1/(4\pi)\)
près. L'échelle de (8.5),
\(D_\lambda^{1/6}M_\lambda^{5/6}=\lambda^{-1/2}
D^{1/6}M^{5/6}\), est bien celle de \(\|u_\lambda\|_2\).

### 8.3 Attaque de l'hypothèse « tube poreux »

L'écriture (8.1) ne décrit pas une mesure filamentaire : une mesure portée
par une courbe vérifie typiquement \(\sigma(B(x,r))\asymp r\), non
\(r^3\). Elle décrit une densité volumique essentiellement bornée. De même,
si un ensemble tubulaire \(E\) a un volume positif, une condition

\[
 |E\cap B(x,r)|\le\theta |B(x,r)|,\qquad \theta<1,
\]

ne peut pas valoir pour toutes les petites boules centrées dans \(E\) :
aux points de densité de Lebesgue, le quotient tend vers 1. La porosité d'un
tube épais doit donc commencer à une échelle \(\rho>0\), comparable au rayon
du cœur.

Si (8.1) n'est connue que pour \(r\ge\rho\), (8.3) ne contrôle pas le
potentiel entier. Une mesure atomique ou filamentaire peut avoir un
potentiel infini dans le cœur. Avec, en plus, une densité
\(f\in L^\infty\), \(\|f\|_\infty\le A\), la même preuve donne seulement

\[
 \|I_1 f\|_\infty
 \lesssim A\rho+D^{2/3}M^{1/3},                  \tag{8.6}
\]

lorsque le rayon d'optimisation est au moins \(\rho\) ; sinon on doit garder
la borne non optimisée \(D\rho+M/\rho^2\). Si « \(I_1^{\rm far}\) » désigne
réellement la région \(|x-y|\ge\rho\), son contrôle brut est
\(M/\rho^2\) et il faut définir précisément où intervient \(D\).

### 8.4 Résultats proches, mais aucun transfert automatique

- Grujić, DOI `10.1088/0951-7715/26/1/289` (`NS-SRC-0064`), et
  Farhat–Grujić–Leitmeyer, DOI `10.1007/s00021-016-0288-z` avec erratum
  `10.1007/s00021-016-0295-0` (`NS-SRC-0065`), utilisent la sparseness de
  **superniveaux** à une échelle sélectionnée et un argument
  analytité–mesure harmonique. Ils ne prouvent pas (8.1) pour la variation
  totale de la vorticité à toutes les échelles.
- Gancedo–Hidalgo-Torné (2025), source déjà auditée en section 6, place une
  mesure filamentaire hélicoïdale dans un espace de Morrey adapté. La
  croissance d'une mesure de courbe est de dimension un, et non l'hypothèse
  cubique de (8.1) ; leur théorème global repose sur la symétrie hélicoïdale
  et la structure de l'équation, pas sur (8.3).
- Les constructions hélicoïdales 2026 recensées en sections 5–6 contrôlent
  des cœurs transverses et des limites filamentaires, mais ne fournissent
  ni constante \(D\) uniforme pour un nombre croissant de tubes, ni
  propagation dynamique de (8.1).

La veille différentielle ciblée n'a donc identifié **aucun théorème
2025–2026** établissant exactement (8.3) pour des ensembles croissants de
tubes poreux dans Navier–Stokes 3D. Le contenu nouveau utilisable est la
réduction interne (8.2), sous une hypothèse qui doit être formulée sur la
variation totale et à toutes les échelles.

## 9. Implication explicite vers Clay

La chaîne cinématique positive est

\[
\begin{aligned}
u_j\in C_c^\infty,\ \nabla\cdot u_j=0
&\Longrightarrow \omega_j=\nabla\times u_j\in C_c^\infty,\\
&\Longrightarrow \operatorname{BS}[\omega_j]=u_j,\\
&\Longrightarrow \sum_{j=1}^Nu_j
\text{ est une donnée Clay admissible.}
\end{aligned}
\]

Ce qui ne suit pas est

\[
\text{packing initial}
\centernot\Longrightarrow
\text{packing pour }t>0
\centernot\Longrightarrow
\text{contrôle de la pression ou du stretching}
\centernot\Longrightarrow
\text{blow-up}.
\]

Le contre-profil (3.3)–(3.5) montre en outre

\[
\inf_N\|U_N\|_3>0
\centernot\Longrightarrow
\inf_N\|U_N\|_{L^{3,\infty}}>0.
\]

Un prochain gate pertinent doit donc exiger une non-petitesse dans un espace
où une théorie globale perturbative est disponible, ou démontrer que les
blocs restent couplés à un temps commun indépendant de la plus petite
échelle. Ni la littérature multi-anneaux à \(N\) fixé, ni une borne de
capacité, ne fournit ce raccord.

## 10. Recommandations exactes pour `sources.json`

Le catalogue n'est pas modifié ici. Les identifiants sont provisoires et à
réattribuer après lecture du `HEAD`.

### Entrées nécessaires, priorité haute

| ID provisoire | Source | Champs à encoder et limite essentielle |
|---|---|---|
| `NS-SRC-0118` | Yamazaki, Math. Ann. 317 (2000), 635–675, DOI `10.1007/PL00004418` | `published`; NS incompressible, \(n\ge3\), espace entier/demi-espace/extérieur, force dépendant du temps admise ; globalité/unicité pour petite donnée faible-\(L^n\) ; seuil non extrait. Nécessaire pour fermer le contre-profil multi-échelle. |
| `NS-SRC-0119` | Buttà; Cavallaro; Marchioro, SIAM JMA 57 (2025), 789–824, DOI `10.1137/24M1642391`, arXiv `2310.00732v2` | `published`; Euler 3D axisymétrique sans swirl ; \(N\) anneaux disjoints, scaling limit et leapfrogging ; \(N\) fixé, aucune constante Lorentz/log-BMO uniforme. |
| `NS-SRC-0120` | Gancedo; Hidalgo-Torné, Adv. Math. 471 (2025), 110268, DOI `10.1016/j.aim.2025.110268`, arXiv `2311.15413v2` | `published`; NS 3D, filament hélicoïdal mesure, cadre périodique axial/local energy ; bien-posé global sans petite circulation ; symétrie forte, pas packing croissant. |
| `NS-SRC-0121` | Guerra; Musso, Math. Ann. 394(1) (2026), article 25, DOI `10.1007/s00208-026-03337-4`, arXiv `2502.01470v2` | `published`; Euler hélicoïdal sans swirl, \(N\) et \(N+1\) filaments ; concentration distributionnelle, \(N\) fixé ; hélices non compactes globalement. |
| `NS-SRC-0122` | Averkiou; Musso, JDE 464 (2026), 114244, DOI `10.1016/j.jde.2026.114244`, arXiv `2511.12296v1` | `published`; Euler hélicoïdal sans swirl ; support **transverse** compact, extension multi-hélices ; ne pas encoder comme vitesse/vorticité compacte dans \(\mathbb R^3\). |
| `NS-SRC-0123` | Averkiou; Musso; Yu, arXiv `2604.09546v1` | `preprint`; Euler hélicoïdal sans swirl ; cluster multi-vortex à support transverse compact ; `PREPRINT_CLAIM`, aucune revue identifiée. |
| `NS-SRC-0124` | Fontelos; Ispizua; Vega, arXiv `2607.21439v1` | `preprint`; NS visqueux, courbe ouverte, \(\nu t\ll1\), petit \(\Gamma/\nu\), contrôle Morrey et propagation soliton ; `PREPRINT_CLAIM`, pas blow-up. |
| `NS-SRC-0125` | Hedberg, Proc. AMS 36 (1972), 505–510, DOI `10.1090/S0002-9939-1972-0312232-4` | `published`; méthode de séparation proche/lointain pour potentiels de Riesz par fonction maximale. Encoder comme antécédent méthodologique ; la constante 9 de (8.3) reste une dérivation du laboratoire. |
| `NS-SRC-0126` | Lieb, Ann. Math. 118 (1983), 349–374, DOI `10.2307/2007032` | `published`; HLS avec constantes optimales. Usage exact ici : \(I_1:L^{6/5}(\mathbb R^3)\to L^2(\mathbb R^3)\). |
| `NS-SRC-0127` | Adams; Hedberg, *Function Spaces and Potential Theory*, Grundlehren 314, Springer (1996), DOI `10.1007/978-3-662-03282-4` | `monograph`; référence de synthèse, chapitre 3 sur les estimations de potentiels de Bessel et Riesz ; ne remplace pas les deux sources primaires précédentes. |

### Entrées utiles, priorité moyenne

- Dávila–del Pino–Musso–Wei, CPAM 77 (2024), 3843–3957, DOI
  `10.1002/cpa.22199`, arXiv `2207.03263v4` : source constructive publiée
  pour deux anneaux leapfrogging ; à ajouter si la carte des anneaux doit
  couvrir les solutions exactes et non seulement les scaling limits.
- Hao Jia, arXiv `1409.8382v1` : complément d'unicité petite donnée
  \(L^{3,\infty}\), utile si ce point est séparé de Yamazaki.

### Aucune nouvelle entrée nécessaire

O'Neil, Lorentz, Majda–Bertozzi, Dascaliuc–Grujić, Feng–Šverák,
Lévy–Liu, Smirnov, Daneri–Székelyhidi, Enciso–Peralta-Salas, les opérateurs
de Bogovskiĭ/Poincaré, Gavrilov, Constantin–La–Vicol et
Peralta-Salas–Slobodeanu sont déjà catalogués. Ils doivent seulement être
reliés au nouveau lemme de stacking.

## 11. Passe contradictoire et décision

| Proposition attaquée | Verdict |
|---|---|
| Supports de vorticité disjoints \(\Rightarrow\) vitesses disjointes | Faux par non-localité de Biot–Savart. |
| Vitesses compactes disjointes \(\Rightarrow\) découplage cinématique initial | Vrai par (2.3), mais pas dynamique à \(t>0\). |
| Packing volumique \(\Rightarrow\) log-BMO uniforme | Faux sans gain logarithmique all-ball et contrôle interne. |
| Capacité bornée \(\Rightarrow\) cohérence de direction | Non établi et dimensionnellement inadéquat. |
| Faible-\(L^{3/2}\) de la vorticité borné + \(L^3\) vitesse non nul \(\Rightarrow\) hors petite donnée | Faux par (3.3)–(3.5). |
| Support transverse compact d'une hélice \(\Rightarrow\) donnée Clay compacte | Faux : l'hélice reste infinie axialement. |
| Résultats multi-filaments 2025–2026 \(\Rightarrow\) contrôle uniforme en nombre de tubes | Faux : \(N\) est fixé ou les constantes ne sont pas suivies dans cette limite. |

**Décision : abandonner** le gate du cycle 0029 sous sa forme actuelle. Le
stacking de vitesses compactes franchit ses trois conditions mais retombe
dans la petite donnée \(L^{3,\infty}\).

Le prochain lemme minimal doit tester une famille de blocs compacts avec :

\[
\inf_N\|U_N\|_{L^{3,\infty}}>\varepsilon_*>0,
\quad
\sup_N\|\nabla\times U_N\|_{L^{3/2,\infty}}<\infty,
\]

une direction log-BMO uniforme **sur le support actif**, et un temps
d'interaction indépendant de la plus petite échelle. Le test d'abandon est
la réapparition de l'une des trois pertes : petite donnée faible-\(L^3\),
oscillation interne \(|\log r_N|\), ou temps diffusif
\(t_N\asymp r_N^2/\nu\to0\).
