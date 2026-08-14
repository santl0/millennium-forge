# Cycle 0026 — veille primaire : Lorentz, compensation conique et return-flow

Date de coupure : 2026-08-14.

Périmètre : sources primaires de l'inégalité d'intégration faible-Lorentz,
annulation de la moyenne d'un rotationnel, critères de régularité fondés sur la
direction de vorticité, et constructions voisines de tubes ou de contre-courants.
Cette revue n'attribue aucun statut **PAPER_PROOF** à la dérivation du laboratoire.

## Verdict différentiel

1. Pour la convention

   \[
   \|f\|_{L^{p,\infty}}
   =\sup_{\lambda>0}\lambda
     |\{|f|>\lambda\}|^{1/p},\qquad 1<p<\infty,
   \]

   l'estimation

   \[
   \int_E |f|
   \leq \frac p{p-1}\|f\|_{L^{p,\infty}}|E|^{1-1/p}
   \tag{L}
   \]

   est standard, immédiate par réarrangement décroissant, et sa constante
   \(p'=p/(p-1)\) est optimale pour cette quasi-norme. Au seuil \(p=3/2\), la
   constante est exactement \(3\).

2. Si \(U\in C_c^1(\mathbb R^3;\mathbb R^3)\), plus généralement
   \(U\in W^{1,1}(\mathbb R^3;\mathbb R^3)\), alors

   \[
   \int_{\mathbb R^3}\operatorname{curl}U\,dx=0.       \tag{C}
   \]

   C'est une intégration par parties élémentaire. En revanche, sur une boule,

   \[
   \int_B\operatorname{curl}U\,dx
   =\int_{\partial B}n\times U\,dS,                    \tag{CB}
   \]

   et l'annulation locale exige donc un contrôle de flux au bord. Cette
   différence bloque tout transfert automatique du lemme global vers les
   critères locaux de Grujić ou Lei–Ren–Tian.

3. Les critères publiés de Constantin–Fefferman, Beirão da Veiga–Berselli et
   Grujić mesurent principalement une cohérence *pairwise* par le sinus de
   l'angle. Ils identifient ainsi les directions \(e\) et \(-e\). Le critère de
   Miller mesure \(v\times\omega\) et possède la même insensibilité au signe.
   Lei–Ren–Tian autorise explicitement un **double** cône autour de
   \(\{e,-e\}\). Aucun de ces énoncés n'est une minoration de la mesure d'une
   phase opposée à partir d'une masse conique orientée et d'une norme
   faible-\(L^{3/2}\).

4. La prépublication Grujić 2026 est la source la plus proche parce qu'elle
   juxtapose précisément une borne de vorticité \(L^{3/2,\infty}\) et une
   petite oscillation moyenne logarithmique de sa direction. Elle **suppose**
   ces deux propriétés et ne dérive pas la masse conique normalisée utilisée au
   cycle 0026. Le corollaire du cycle fournit au mieux une condition nécessaire
   nouvelle pour un blob global à moyenne nulle; il ne valide ni ne réfute le
   théorème annoncé.

5. Chaque ingrédient du lemme du cycle est classique. La recherche ciblée n'a
   trouvé aucune source énonçant verbatim le chaînage

   \[
   \text{faible-}L^{3/2}+\int W=0+\text{masse conique orientée}
   \Longrightarrow \text{oscillation moyenne quantitative de }W/|W|.
   \]

   Cela inclut la version renforcée du cycle, de constante
   \(2\alpha^3/27\). Le statut sûr est donc : **dérivation interne élémentaire
   apparemment non cataloguée**, et non « nouveau théorème publié ». L'absence
   dans une veille ciblée n'est pas une preuve de nouveauté bibliographique
   exhaustive.

## 1. Source et constante de l'inégalité faible-Lorentz

La source historique des espaces est G. G. Lorentz,
[*Some new functional spaces*](https://doi.org/10.2307/1969496), *Annals of
Mathematics* **51** (1950), 37–55. Le cadre primaire de réarrangement et des
inégalités dans \(L(p,q)\) directement utilisé dans la littérature PDE est
Richard O'Neil,
[*Convolution operators and \(L(p,q)\) spaces*](https://projecteuclid.org/journals/duke-mathematical-journal/volume-30/issue-1/Convolution-operators-and-Lpq-spaces/10.1215/S0012-7094-63-03015-1.full),
*Duke Mathematical Journal* **30** (1963), 129–142,
[DOI 10.1215/S0012-7094-63-03015-1](https://doi.org/10.1215/S0012-7094-63-03015-1).
Les deux articles sont publiés.

Pour éviter toute ambiguïté de normalisation, fixons \(K\) par la fonction de
distribution, comme dans le rapport principal :

\[
K=\sup_{\lambda>0}\lambda\mu_f(\lambda)^{1/p},
\qquad \mu_f(\lambda)=|\{|f|>\lambda\}|.
\]

La réarrangée décroissante vérifie alors \(f^*(s)\leq Ks^{-1/p}\). L'inégalité
de Hardy–Littlewood appliquée à \(|f|\mathbf1_E\) donne

\[
\int_E|f|
 \leq\int_0^{|E|}f^*(s)\,ds
 \leq K\int_0^{|E|}s^{-1/p}\,ds
 =p'K|E|^{1/p'},
\]

ce qui est (L). Le profil réarrangé

\[
f^*(s)=Ks^{-1/p}\mathbf1_{(0,a)}(s)
\]

a quasi-norme faible exactement \(K\) et intégrale \(p'Ka^{1/p'}\); la
constante est donc sharp dans la classe scalaire mesurable. Avec la norme
équivalente fondée sur \(f^{**}\), ou une norme banachisée de Lorentz, cette
valeur numérique doit être remplacée par la constante correspondant à la
convention. Le facteur \(3\) du cycle est correct uniquement parce que \(K\) a
été défini explicitement par la distribution.

Cette inégalité restreinte n'utilise ni divergence, ni vorticité, ni équation
d'évolution. O'Neil fournit la filiation fonctionnelle; l'affichage (L) est une
conséquence directe par réarrangement, pas un nouveau résultat PDE.

## 2. Annulation de la moyenne d'un rotationnel

Pour \(U\in C_c^1(\mathbb R^3)\), composante par composante,

\[
\int(\operatorname{curl}U)_i\,dx
=\varepsilon_{ijk}\int\partial_jU_k\,dx=0
\]

par Fubini et le théorème fondamental du calcul. Le même énoncé vaut pour
\(U\in W^{1,1}(\mathbb R^3)\) par approximation. Pour un champ ou courant à
support compact traité distributionnellement, on teste contre une coupure
\(\chi\equiv1\) dans un voisinage du support :

\[
\langle\operatorname{curl}U,\chi\rangle
=\langle U,\operatorname{curl}\chi\rangle=0.
\]

Ainsi l'hypothèse du cycle est certaine pour \(W=\operatorname{curl}U\) avec
\(U\in C_c^1\), et également pour une donnée de vitesse de Schwartz. Sur le
tore, la moyenne d'un rotationnel périodique est nulle par périodicité.

Trois restrictions doivent rester visibles.

- Pour un champ non compact sans décroissance intégrable, l'intégrale peut ne
  pas exister ou un terme de bord à l'infini peut subsister.
- L'identité sur tout \(\mathbb R^3\) ne se localise pas : (CB) produit un flux
  de bord. Remplacer \(D\) par une boule de zoom requiert donc que le support
  de \(W\) soit contenu dans la boule ou que \(n\times U\) soit contrôlé.
- L'annulation est vectorielle et globale. Elle n'impose ni proximité spatiale
  entre les phases de signes opposés, ni borne sur la pression ou la vitesse
  reconstruite par Biot–Savart.

Un corollaire qualitatif classique est qu'un rotationnel compact non nul ne
peut avoir toute sa direction active dans un cône unilatéral strict
\(\xi\cdot e\geq\alpha>0\). Cela ne vaut pas pour un double cône
\(|\xi\cdot e|\geq\alpha\), où les branches \(+e\) et \(-e\) peuvent se
compenser.

## 3. Recalcul du maillon du cycle et portée exacte

Soient \(W\in L^{3/2,\infty}(D;\mathbb R^3)\), \(|D|<\infty\),
\(\int_DW=0\), et

\[
K=\sup_{\lambda>0}\lambda|\{|W|>\lambda\}|^{2/3}.
\]

Pour \(e\in S^2\), \(0<\alpha\leq1\), posons

\[
G=\{W\ne0:(W/|W|)\cdot e\geq\alpha\},\qquad
m=\int_G|W|,
\]

et définissons, avec \(\zeta=W/|W|\) sur \(\{W\ne0\}\),

\[
q=(-\zeta\cdot e)_+\in[0,1],\qquad
\nu_e=\int_D|W|q.
\]

Les valeurs de \(\zeta\) sur \(\{W=0\}\) sont arbitraires et n'affectent pas
\(\nu_e\). La projection de la moyenne nulle sur \(e\) impose

\[
\nu_e\geq\alpha m.
\]

Par (L), \(|G|\geq(m/(3K))^3\). Plus précisément, la formule des couches,
(L), Jensen pour la fonction concave \(s\mapsto s^{1/3}\), puis Cavalieri
donnent l'estimation pondérée

\[
\begin{aligned}
\int_D|W|q
 &=\int_0^1\int_{\{q>t\}}|W|\,dx\,dt\\
 &\leq3K\int_0^1|\{q>t\}|^{1/3}\,dt\\
 &\leq3K\left(\int_Dq\right)^{1/3}.
\end{aligned}                                                   \tag{3.1}
\]

Ainsi, avec \(Q=|D|^{-1}\int_Dq\) et \(a=|G|/|D|\),

\[
Q\geq\frac{\alpha^3m^3}{27K^3|D|},\qquad
a\geq\frac{m^3}{27K^3|D|}.
\]

Posons \(h=\zeta\cdot e\) et \(c=h_D\). Si \(c\geq0\), la partie négative
de \(h-c\) domine \(q\); si \(c<0\), sa partie positive est au moins
\(\alpha\) sur \(G\). Comme les intégrales des parties positive et négative
de \(h-c\) coïncident,

\[
\fint_D|\zeta-\zeta_D|
\geq\fint_D|h-h_D|
\geq2\min\{Q,\alpha a\}
\geq\frac{2\alpha^3m^3}{27K^3|D|}.             \tag{3.2}
\]

Sans utiliser l'annulation de la moyenne, le même calcul donne la forme
canonique

\[
\fint_D|\zeta-\zeta_D|
\geq\frac2{27K^3|D|}\min\{\nu_e^3,\alpha m^3\}.
\]

La borne antérieure obtenue en ne conservant que deux ensembles de niveaux,
\(\alpha^4m^3/(27K^3|D|)\), reste valide mais est strictement plus faible.
À exposant général \(p\), la même argumentation remplace le cube par
\(p'=p/(p-1)\), le facteur \(3\) par \(p'\), et donne

\[
\fint_D|\zeta-\zeta_D|
\geq\frac{2\alpha^{p'}m^{p'}}{(p')^{p'}K^{p'}|D|}.
\]

Le choix \(p=3/2\) est critique pour la vorticité NS : sous
\(W_\ell(x)=\ell^{-2}W(x/\ell)\), \(K\) est invariant, \(m_\ell=\ell m\),
\(|D_\ell|=\ell^3|D|\), et le membre droit de (3.2) est invariant.

La littérature primaire certifie séparément (L), la représentation par
couches/Cavalieri, Jensen, (C), et les mécanismes de cohérence directionnelle
ci-dessous. L'étape (3.1) peut aussi se lire comme une application standard de
Lorentz–Hölder à \(L^{3/2,\infty}\times L^{3,1}\), suivie de la borne obtenue
pour \(0\leq q\leq1\); les constantes dépendent alors des conventions de norme,
d'où la dérivation directe ci-dessus. Aucune source primaire ciblée
n'anticipe précisément le chaînage pondéré (3.1), la compensation conique,
puis l'identité des parties positive et négative conduisant à (3.2). Le lemme
doit rester étiqueté
**AI_DERIVATION** ou équivalent interne : il assemble des briques classiques,
mais n'est ni un théorème publié repéré ni une preuve du problème Clay. Le
facteur \(3\) est sharp dans (L) et l'exposant cubique est atteint à l'échelle
par le modèle atomique du cycle; cela ne démontre pas que la constante
\(2/27\) est simultanément sharp sous les contraintes spatiales
\(W=\operatorname{curl}U\), support compact et régularité.

## 4. Comparaison exacte avec les critères de direction

| Source primaire | Équation, domaine, solution et hypothèse | Sensibilité au signe | Conclusion | Rapport exact au lemme 0026 |
|---|---|---|---|---|
| Peter Constantin et Charles Fefferman, [*Direction of Vorticity and the Problem of Global Regularity for the Navier–Stokes Equations*](https://iumj.org/article/3627/), *Indiana Univ. Math. J.* **42** (1993), 775–789, [DOI](https://doi.org/10.1512/iumj.1993.42.42034) | NS incompressible non forcé sur \(\mathbb R^3\), \(\nu>0\), solution faible issue de \(H^1\); cohérence lipschitzienne pairwise de \(\xi\) là où les deux vorticités dépassent un seuil | \(|\xi(x)\times\xi(y)|=\sin\theta\) ne distingue pas parallèle et antiparallèle | la solution devient forte/régulière | mécanisme dynamique de déplétion du stretching; aucune masse conique, aucune norme faible-Lorentz, aucune minoration de phase opposée |
| Hugo Beirão da Veiga et Luigi C. Berselli, [*On the regularizing effect of the vorticity direction in incompressible viscous flows*](https://people.dm.unipi.it/beiraodaveiga/pdf/hbv-79.pdf), *Differential and Integral Equations* **15** (2002), 345–356, [DOI](https://doi.org/10.57262/die/1356060864) | NS non forcé sur \(\mathbb R^3\), \(\nu>0\), solution faible de Leray–Hopf, \(u_0\in H^1\); pour \(\beta\in[1/2,1]\), \(\sin\theta(x,x+y,t)\leq g(t,x)|y|^\beta\) sur les paires high–high, avec \(2/a+3/b=\beta-1/2\) et \(g\in L^a_tL^b_x\) | insensible à \(\xi\mapsto-\xi\) | solution forte; en particulier la cohérence uniforme \(1/2\)-Hölder suffit | condition spatio-temporelle pondérée sur chaque paire, et non bilan orienté à temps gelé; (3.2) ne produit pas le module de Hölder |
| Zoran Grujić, [*Localization and Geometric Depletion of Vortex-Stretching in the 3D NSE*](https://doi.org/10.1007/s00220-008-0726-8), *Commun. Math. Phys.* **290** (2009), 861–870 | NS incompressible sur un cylindre espace-temps arbitrairement petit; localisation du stretching et des critères de cohérence pour une solution de Leray | le noyau géométrique est contrôlé par \(\sin\theta\), donc projectif | critère de régularité localisé | le flux de bord (CB) empêche d'insérer directement \(\int_DW=0\) dans une boule locale |
| Zoran Grujić et Rafaela Guberović, [*Localization of Analytic Regularity Criteria on the Vorticity and Balance Between the Vorticity Magnitude and Coherence of the Vorticity Direction in the 3D NSE*](https://doi.org/10.1007/s00220-010-1000-4), *Commun. Math. Phys.* **298** (2010), 407–418 | NS localisé; classes critiques hybrides combinant magnitude et cohérence, notamment des intégrales du type \(\int|\omega|^2\rho_{1/2}^2\), où \(\rho_\gamma\) mesure le quotient Hölder de \(\sin\theta\) | projectif via \(\sin\theta\) | contrôle local d'enstrophie/régularité sous la classe hybride | c'est une cohérence pondérée pertinente, mais ni une occupation de cône ni un contrôle faible-\(L^{3/2}\) du return-flow |
| Evan Miller, [*A Locally Anisotropic Regularity Criterion for the Navier–Stokes Equation in Terms of Vorticity*](https://arxiv.org/abs/2002.02152), v1 du 2020-02-06, publié dans *Proc. Amer. Math. Soc. Ser. B* **8** (2021), 60–74, [DOI](https://doi.org/10.1090/bproc/74) | solution mild \(u\in C([0,T_{max});H^1(\mathbb R^3))\); champ unitaire auxiliaire global \(v\), \(\nabla v\in L^\infty_{loc,t}L^\infty_x\); si \(T_{max}<\infty\), alors \(\int_0^{T_{max}}\|v\times\omega\|_2^4dt=\infty\) | \(v\times\omega=0\) pour \(\omega\) parallèle **ou** antiparallèle à \(v\) | critère critique anisotrope global | une petite masse hors d'un cône ne contrôle ni \(\nabla v\) ni la norme temporelle \(L^4_tL^2_x\); (3.2) ne déclenche pas Miller |
| Zhen Lei, Xiao Ren et Gang Tian, [*A Geometric Characterization of Potential Navier-Stokes Singularities*](https://arxiv.org/abs/2501.08976), arXiv:2501.08976v1 du 2025-01-15 | solution faible adaptée locale dans \(Q(1)\); aux points réguliers, soit \(|\omega|\leq M\), soit \(|\xi\times e|\leq1-\delta\) | double cône autour de \(+e\) et \(-e\) | régularité dans \(Q(1/2)\); une singularité doit avoir des directions limites rencontrant tout grand cercle | source la plus proche du mot « cône », mais les deux branches peuvent compenser leur moyenne sans sortir du double cône; aucun faible-Lorentz n'intervient |
| Zachary Bradshaw et Zoran Grujić, [*A spatially localized \(L\log L\) estimate on the vorticity in the 3D NSE*](https://arxiv.org/abs/1309.2519), v5, publié dans *Indiana Univ. Math. J.* **64** (2015), 433–440, [DOI](https://doi.org/10.1512/iumj.2015.64.5496) | solution de Leray sur \(\mathbb R^3\); borne uniforme de la direction coupée \(\psi\xi\) dans un log-BMO ancré | BMO du vecteur orienté distingue \(+e\) et \(-e\) | borne locale \(L\log L\) de la magnitude | (3.2) donne une obstruction nécessaire sur un blob global, mais ne produit pas l'hypothèse log-BMO et ne contrôle pas le flux de coupure |
| Zoran Grujić, [*Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier–Stokes Equations*](https://arxiv.org/abs/2607.08866), arXiv:2607.08866v2 du 2026-07-13 | NS non forcé sur \(\mathbb R^3\), scénario ponctuel conditionnel; \(\omega\in L^\infty_tL^{3/2,\infty}_x\) et \(\xi\) dans un BMO pondéré par \(1/|\log r|\), plus hypothèses de profil/uniformité | l'oscillation BMO du vecteur est orientée | exclusion conditionnelle revendiquée du scénario critique par commutateur, gain logarithmique, De Giorgi et sparseness | juxtapose les deux quantités de 0026, mais suppose leur contrôle séparément; aucune masse conique normalisée n'est produite |

Les articles Constantin–Fefferman, Beirão da Veiga–Berselli, Grujić 2009,
Grujić–Guberović 2010, Miller et Bradshaw–Grujić sont publiés. Lei–Ren–Tian
reste en v1 sans référence de revue affichée à la date de coupure. Grujić 2026
reste en v2 sans référence de revue. Aucune version plus récente n'a été
utilisée.

### Double cône, hémisphère et masse conique ne sont pas synonymes

Le théorème 1.1 de Lei–Ren–Tian est sign-symétrique :
\(|\xi\times e|\leq1-\delta\) équivaut à une union de deux calottes autour de
\(\pm e\). La compensation \(\int W=0\) peut donc être entièrement réalisée à
l'intérieur du cône admissible par des vorticités presque \(+e\) et presque
\(-e\). Le lemme 0026 ne contredit pas cette régularité et ne l'améliore pas.

Leur remarque 1.3 signale comme non trivial le cas unilatéral
\(\omega_3\geq0\), même axisymétrique. Sur tout \(\mathbb R^3\), si la vorticité
est intégrable, de moyenne nulle et \(\omega_3\geq0\), alors nécessairement
\(\omega_3=0\) presque partout. Mais LRT travaille localement dans \(Q(1)\) :
le flux (CB), la petite vorticité hors du superniveau et l'extérieur du cylindre
peuvent porter la compensation. L'observation globale ne résout donc pas leur
question locale.

Les critères Constantin–Fefferman, Beirão da Veiga–Berselli et le premier
programme Grujić sont encore plus éloignés d'une orientation : une inversion
brutale \(e\leftrightarrow-e\) a un sinus d'angle nul. C'est cohérent avec la
physique de leur preuve, car alignement et anti-alignement déplètent tous deux
le noyau du stretching. Le lemme 0026, lui, voit précisément l'inversion de
signe par \(\zeta\cdot e\). Il répond à une autre question cinématique.

## 5. Critères faibles-Lorentz et « masse conique »

La recherche primaire ciblée a retrouvé de nombreux critères de magnitude en
espaces de Lorentz, mais pas de critère publié formulé comme

\[
\frac{\int_{\{\xi\cdot e\geq\alpha\}}|\omega|}
     {\|\omega\|_{L^{3/2,\infty}}|D|^{1/3}}
\quad\text{ou comme mesure minimale de l'hémisphère opposé.}
\]

Grujić 2026 est le seul résultat primaire repéré combinant explicitement, dans
le même scénario de vorticité, le faible-\(L^{3/2}\) critique et un contrôle de
direction par oscillation moyenne logarithmique. Sa borne Lorentz est une
hypothèse globale; elle ne donne aucune minoration de la masse conique \(m\).
Le modèle atomique à deux amplitudes du cycle montre pourquoi : toute la masse
critique forte peut résider dans le compensateur rare pendant que la masse
orientée \(m/K\) tend vers zéro.

Inversement, si une famille de domaines \(D_n\) contenant effectivement le
support des blobs vérifie

\[
\fint_{D_n}|\zeta-\zeta_{D_n}|\leq B\phi(\rho_n),
\]

alors (3.2) impose seulement

\[
\frac{m_n}{K_n|D_n|^{1/3}}
\leq \left(\frac{27B}{2\alpha^3}\phi(\rho_n)\right)^{1/3}.
\]

Au poids \(\phi(r)=1/(1+\log(R_*/r))\), la masse conique normalisée doit donc
disparaître comme au moins la racine cubique du logarithme. C'est un pont
quantitatif falsifiable vers les hypothèses BMO, mais seulement sous
l'annulation **sur le même domaine**. Une coupure locale réintroduit (CB).

## 6. Tubes, solénoïdes et contre-courants disponibles

### Décomposition de Smirnov

S. K. Smirnov,
[*Decomposition of solenoidal vector charges into elementary solenoids, and the
structure of normal one-dimensional flows*](https://www.unige.ch/~smirnov/papers/solenoid-j.pdf),
*Algebra i Analiz* **5** (1993), 206–238; traduction *St. Petersburg Math.
J.* **5** (1994), 841–867, démontre qu'une charge vectorielle de masse finie
et de divergence nulle se décompose en solénoïdes élémentaires, représentés
par des circulations moyennées le long de courbes récurrentes.

Cette source formalise l'intuition « un flux solénoïdal doit revenir » beaucoup
mieux qu'un dessin de tube. Elle ne fournit toutefois ni support compact lisse,
ni axe privilégié, ni estimation de la mesure du return-flow en fonction d'une
norme faible-\(L^{3/2}\), ni contrôle de \(U=\operatorname{curl}^{-1}W\). Elle
n'implique donc pas (3.2), mais suggère de tester le prochain modèle sur une
boucle fermée ou une superposition de boucles plutôt que sur deux phases
atomiques sans géométrie.

### Mikado flows : un modèle périodique de flux signé, pas de vorticité conique

Sara Daneri et László Székelyhidi Jr.,
[*Non-uniqueness and \(h\)-principle for Hölder-continuous weak solutions of the
Euler equations*](https://arxiv.org/abs/1603.09714), arXiv:1603.09714v3,
publié dans *Arch. Rational Mech. Anal.* **224** (2017), 471–514,
[DOI 10.1007/s00205-017-1081-8](https://doi.org/10.1007/s00205-017-1081-8),
introduit les Mikado flows : champs périodiques stationnaires, divergence-free,
de moyenne nulle, concentrés dans de fins tubes rectilignes et capables de
réaliser un tenseur de Reynolds prescrit.

Pour une direction rationnelle \(k\), le bloc type a la forme
\(W_k(x)=\psi_k(x)k\), avec \(k\cdot\nabla\psi_k=0\) et moyenne nulle. Le
profil scalaire doit donc changer de signe : c'est un contre-courant
quasi-unidirectionnel explicite sur \(\mathbb T^3\). C'est l'antécédent
constructif le plus proche du test à deux amplitudes.

Mais quatre écarts sont décisifs :

1. \(W_k\) est un **champ de vitesse** Euler périodique, non le blob de
   vorticité \(W=\operatorname{curl}U\) du cycle;
2. sa vorticité \(\nabla\psi_k\times k\) est transverse à \(k\), donc n'est pas
   directionnellement concentrée autour de l'axe du tube;
3. le support est tubulaire dans le tore et se répète périodiquement, pas
   compact dans \(\mathbb R^3\);
4. l'article ne suit pas la norme faible-\(L^{3/2}\), le coût Biot–Savart, la
   pression NS ou la saturation de (3.2).

Les flots de Beltrami intermittents de Tristan Buckmaster et Vlad Vicol,
[*Nonuniqueness of weak solutions to the Navier–Stokes equation*](https://annals.math.princeton.edu/2019/189-1/p03),
*Annals of Mathematics* **189** (2019), 101–144,
[DOI 10.4007/annals.2019.189.1.3](https://doi.org/10.4007/annals.2019.189.1.3),
emploient des ondes de Beltrami modulées sur le tore et un correcteur
d'incompressibilité dans l'itération. Ils démontrent qu'une réalisation
solénoïdale de structures très intermittentes est possible par convex
integration. Ils construisent des solutions faibles de basse régularité, pas
un blow-up classique admissible Clay, et leurs blocs ne certifient pas le lemme
de vorticité recherché.

### Tubes de vorticité fermés

Alberto Enciso et Daniel Peralta-Salas,
[*Existence of knotted vortex tubes in steady Euler flows*](https://arxiv.org/abs/1210.6271),
*Acta Mathematica* **214** (2015), 61–134,
[DOI 10.1007/s11511-015-0123-z](https://doi.org/10.1007/s11511-015-0123-z),
construisent des champs de Beltrami stationnaires pour Euler sur \(\mathbb R^3\)
possédant de minces tubes de vorticité noués ou enlacés, avec des tores
invariants de mesure positive et des lignes périodiques. Comme
\(\operatorname{curl}u=\lambda u\), vitesse et vorticité y sont colinéaires.

Ces tubes rendent géométriquement manifeste le retour de direction le long
d'une courbe fermée, mais les champs sont analytiques, non compacts, d'énergie
infinie et décroissent seulement à l'ordre \(1/|x|\). Ils résolvent Euler, pas
Navier–Stokes visqueux, et ne sont pas bornés dans le faible-\(L^{3/2}\) global
pertinent. Ils ne fournissent pas un compensateur rare presque unidirectionnel.

Les anneaux visqueux de Hao Feng et Vladimír Šverák,
[*On the Cauchy problem for axi-symmetric vortex rings*](https://arxiv.org/abs/1301.6317),
*Arch. Rational Mech. Anal.* **215** (2015), 89–123, et de Thierry Gallay et
Vladimír Šverák,
[*Uniqueness of axisymmetric viscous flows originating from circular vortex
filaments*](https://www.numdam.org/articles/10.24033/asens.2402/), *Ann. Sci.
ENS* **52** (2019), 1025–1071, sont de vraies solutions NS axisymétriques sans
swirl issues de filaments circulaires. Leur direction azimutale parcourt tout le
cercle : elles réalisent un retour distribué, pas une direction globale plate.
À circulation et rayon majeur fixés, amincir le cœur fait diverger la norme
faible-\(L^{3/2}\) selon le comptage déjà audité au cycle 0025.

## 7. Ce qui se transfère, et ce qui ne se transfère pas à Clay

Implication valide et limitée : pour une donnée de vitesse Clay
\(u_0\in C_c^\infty(\mathbb R^3)\), divergence-free, la vorticité
\(\omega_0=\operatorname{curl}u_0\) est compacte, intégrable et de moyenne
nulle. Sur tout domaine fini contenant son support, une masse conique orientée
\(m>0\) et une borne faible-\(L^{3/2}\) \(K\) imposent alors (3.2). Pour une
donnée Clay seulement de Schwartz, la moyenne globale reste nulle mais aucun
domaine fini ne contient le support : il faut ajouter une erreur de queue. À
temps positif, la diffusion détruit en général le support compact; (3.2) ne se
réapplique donc pas localement sans borne de queue ou de flux.

L'implication suivante est **fausse sans nouveaux lemmes** :

\[
\text{(3.2)}\Longrightarrow
\text{cohérence CF/BdVB, critère Miller ou double cône LRT}
\Longrightarrow\text{régularité globale}.
\]

Les lacunes précises sont :

- (3.2) est une minoration sur une moyenne de domaine, tandis que CF/BdVB
  imposent un module pairwise sur toutes les paires high–high;
- une moyenne petite sur \(D\) ne contrôle pas les sous-boules traversant une
  interface de return-flow;
- une moyenne globale n'est pas disponible après localisation sans contrôler
  \(\int_{\partial D}n\times U\);
- le double cône LRT autorise justement la branche antipodale nécessaire à
  l'annulation;
- la norme faible-Lorentz ne donne pas la masse conique \(m\);
- aucune vitesse, pression, énergie, équation NS ou évolution temporelle n'est
  construite par le modèle à deux amplitudes.

## 8. Conclusion de veille et expérience discriminante

Le résultat bibliographique négatif est précis : aucune source primaire
repérée ne ferme le maillon « compensation vectorielle globale vers contrôle
local de toutes les sous-boules ». Les constructions existantes se partagent
en deux familles non raccordées :

- tubes/solénoïdes géométriquement fermés, où le retour est distribué mais la
  criticalité faible-\(L^{3/2}\) n'est pas suivie;
- Mikado/flots de Beltrami intermittents, où la moyenne nulle et la
  concentration sont
  explicites, mais pour une vitesse périodique ou une solution faible de convex
  integration, non pour une vorticité compacte admissible.

La prochaine expérience à plus forte valeur informationnelle est donc de
partir d'un profil de Mikado signé à deux amplitudes, de le **fermer en une
boucle compacte**, puis de calculer exactement :

1. \(\operatorname{div}W\) et un potentiel compact \(U\) tel que
   \(W=\operatorname{curl}U\);
2. la norme \(L^{3/2,\infty}\) et les masses des deux hémisphères;
3. l'oscillation de \(\xi\) sur toutes les boules qui résolvent les interfaces;
4. le coût des correcteurs de courbure et de fermeture;
5. la queue Biot–Savart et le résidu NS après remise à l'échelle.

Un échec uniforme dès les points 1–3 établirait une obstruction géométrique
substantielle à la cascade de return-flow. Une réussite ne serait encore qu'un
contre-profil statique : il faudrait ensuite contrôler pression, énergie,
évolution et passage au continuum avant toute implication Clay.
