# Cycle 0027 — veille primaire : potentiel axisymétrique, retour poloïdal et BMO

Date de coupure : 2026-08-14.

Périmètre : antériorité et admissibilité de l'ansatz
\(U=\psi(r,z)e_\theta\), champs axisymétriques solénoïdaux, vorticités
compactes, vortex rings, opérateurs de Bogovskiĭ et de Poincaré régularisés,
tubes de flux et critères BMO de direction. Cette revue distingue les résultats
publiés, les prépublications et les simples annonces. Elle n'attribue aucun
statut **PAPER_PROOF** à une dérivation du laboratoire.

## Verdict différentiel

1. L'ansatz du cycle n'est pas nouveau. Jian-Guo Liu et Wei-Cheng Wang donnent
   explicitement la représentation axisymétrique

   \[
   u=u^\theta e_\theta+\nabla\times(\psi e_\theta)
   \]

   et caractérisent les conditions au pôle nécessaires et suffisantes pour
   qu'elle définisse un champ régulier sur l'axe. Leur article est publié dans
   *SIAM Journal on Mathematical Analysis* en 2009.

2. Pour \(U=\psi e_\theta\), la vorticité \(W=\nabla\times U\) est
   **poloïdale**, compacte si \(\psi\) l'est, et ses lignes sont les courbes de
   niveau de \(r\psi\). L'ansatz réalise donc exactement un retour par boucles
   fermées lorsque les niveaux réguliers sont compacts et restent loin de
   l'axe. Cette identité est classique; l'éventuelle nouveauté du cycle ne peut
   porter que sur une famille quantitative de profils et ses bornes uniformes
   Lorentz/BMO/résidu.

3. Un vortex ring axisymétrique sans swirl a la géométrie duale : sa
   **vitesse** est poloïdale et sa **vorticité** est toroïdale
   \(\omega^\theta e_\theta\). Les théorèmes de Norbury, Feng–Šverák et
   Gallay–Šverák ne construisent donc pas le \(W\) poloïdal recherché, même
   s'ils fournissent des modèles rigoureux de support torique, concentration et
   diffusion.

4. Les opérateurs de Bogovskiĭ/Poincaré régularisés permettent de corriger une
   divergence ou de construire un potentiel de rotationnel en préservant le
   support et en gagnant une dérivée sur des domaines adaptés. Ils règlent
   l'admissibilité div–curl, pas la direction du correcteur. Les constantes
   dépendent de la géométrie du domaine; sur un tube de rapport d'aspect
   divergent, aucune uniformité ne peut être présumée.

5. Les critères BMO publiés demandent une borne uniforme en temps et en échelle
   de la direction localisée. Un profil lisse fixé satisfait facilement des
   conditions qualitatives loin de ses zéros, mais une cascade de retours
   contenant des virages d'angle macroscopique à l'échelle \(h\) peut avoir un
   coût \(\widetilde{bmo}_{1/|\log r|}\) de taille \(\log(1/h)\). Aucun
   résultat primaire repéré ne déduit la borne BMO requise de la seule forme
   \(\nabla\times(\psi e_\theta)\).

6. Deux développements 2026 sont à séparer. Cao–Zhan est désormais publié et
   construit des vortex rings d'Euler, avec ou sans swirl. Guo–Jeong–Zhao,
   Peralta-Salas–Slobodeanu, Grujić et plusieurs manuscrits de Shahmurov sont
   encore des prépublications sans référence de revue dans leur fiche arXiv à
   la date de coupure. Les revendications de régularité axisymétrique avec swirl
   de Shahmurov seraient directement pertinentes pour l'évolution de
   \(U=\psi e_\theta\), mais la veille ciblée n'a trouvé ni publication ni
   validation indépendante : elles restent **PREPRINT_CLAIM**.

## 1. Formule exacte et antériorité de l'ansatz

Dans les coordonnées cylindriques \((r,\theta,z)\), avec \(\psi\) indépendante
de \(\theta\), posons

\[
U=\psi(r,z)e_\theta,\qquad \Phi=r\psi.
\]

Le calcul exact donne

\[
\operatorname{div}U=0,
\qquad
W=\operatorname{curl}U
=-\partial_z\psi\,e_r
 +\frac1r\partial_r(r\psi)\,e_z
=\frac1r\bigl(-\partial_z\Phi\,e_r+\partial_r\Phi\,e_z\bigr),
\tag{1.1}
\]

et donc \(\operatorname{div}W=0\). En outre,

\[
W\cdot\nabla\Phi=0.                                      \tag{1.2}
\]

Les lignes de \(W\) dans chaque demi-plan méridien sont ainsi portées par les
niveaux de \(\Phi\). Un niveau régulier compact contenu dans \(r>0\) est une
union de courbes fermées : le return-flow n'est pas ajouté après coup, il est
imposé par la fonction de courant.

La source primaire moderne la plus directe est Jian-Guo Liu et Wei-Cheng Wang
(`NS-SRC-0102`),
[*Characterization and Regularity for Axisymmetric Solenoidal Vector Fields
with Application to Navier–Stokes Equation*](https://doi.org/10.1137/080739744),
*SIAM J. Math. Anal.* **41** (2009), 1825–1850. Leur formule (avec \(x\) comme
variable axiale) est

\[
u=u^\theta e_\theta+\nabla\times(\psi e_\theta)
=u^\theta e_\theta+\frac{\partial_r(r\psi)}r e_x
-\partial_x\psi\,e_r.
\]

Leur lemme de caractérisation montre aussi qu'écrire des composantes lisses sur
le demi-plan \(r\geq0\) ne suffit pas : il faut les conditions de parité au
pôle. Pour le potentiel azimutal, elles imposent en particulier

\[
\partial_r^{2j}\psi(z,0)=0
\]

aux ordres disponibles. Dans la classe \(C^\infty\), cela équivaut localement à
une structure \(\psi(r,z)=r\,a(r^2,z)\) avec \(a\) lisse. Deux choix sûrs sont
donc :

- supporter \(\psi\) dans \(\{r\geq r_*>0\}\), ce qui évite entièrement le
  pôle;
- imposer et tester toutes les conditions de parité si le support touche
  l'axe.

Si \(\psi\in C_c^\infty\) satisfait ces conditions, alors
\(U,W\in C_c^\infty(\mathbb R^3)\), \(\operatorname{div}U=0\), et

\[
\int_{\mathbb R^3}W\,dx=0.                               \tag{1.3}
\]

Ainsi, l'admissibilité cinématique recherchée est standard. Ne sont pas
catalogués dans les sources ciblées : le profil anisotrope précis du cycle, la
répartition quantitative de masse entre branches montante et descendante, la
saturation faible-\(L^{3/2}\), et une borne BMO uniforme sur une cascade. Ces
éléments doivent rester **AI_DERIVATION** ou **COMPUTATIONAL_TEST** selon leur
nature.

## 2. Support compact, div–curl et coût des correcteurs

Martin Costabel et Alan McIntosh (`NS-SRC-0103`),
[*On Bogovskiĭ and regularized Poincaré integral operators for de Rham
complexes on Lipschitz domains*](https://doi.org/10.1007/s00209-009-0517-8),
*Math. Z.* **265** (2010), 297–320
([arXiv:0808.2614v2](https://arxiv.org/abs/0808.2614)), construisent des
opérateurs pseudodifférentiels d'ordre \(-1\) qui réalisent les homotopies du
complexe de de Rham. Sur un domaine étoilé par rapport à une boule, leurs
propriétés de support donnent notamment :

- un inverse à droite de la divergence pour les données de moyenne nulle, de
  type Bogovskiĭ, avec conditions de Dirichlet complètes;
- un potentiel d'une forme fermée, de type Poincaré;
- un gain d'une dérivée dans les échelles de Sobolev, et des extensions aux
  échelles de Besov et Triebel–Lizorkin.

En langage vectoriel tridimensionnel, une \(2\)-forme fermée compacte représente
un champ divergence-free compact. Sur \(\mathbb R^3\), où
\(H_c^2(\mathbb R^3)=0\), elle admet un potentiel compact \(U\) tel que
\(W=\operatorname{curl}U\). Sur un domaine borné non contractile, par exemple
un voisinage torique, les classes de cohomologie et les flux à travers les
sections doivent être vérifiés : un potentiel supporté dans exactement le même
tore n'est pas automatique.

Pour corriger une troncature \(\chi W\), on peut écrire

\[
f=\operatorname{div}(\chi W)=\nabla\chi\cdot W,
\qquad b=\mathcal B f,
\qquad \widetilde W=\chi W-b,
\]

si \(\int f=0\). Alors \(\operatorname{div}\widetilde W=0\). Mais cette
opération ne préserve en général ni l'axisymétrie locale, ni un cône de
direction, ni la distribution exacte de \(|W|\). Une symétrisation par rotations
préserve l'axisymétrie lorsque le domaine et l'opérateur le permettent, sans
résoudre le coût directionnel.

Le point quantitatif à ne pas omettre est

\[
\|\mathcal B f\|_{W^{1,p}(\Omega)}
\leq C_{p,\Omega}\|f\|_{L^p(\Omega)},\qquad1<p<\infty.    \tag{2.1}
\]

Sous dilatation homothétique, la constante se renormalise proprement. Sous
dégénérescence de forme — tube de longueur \(L\), rayon \(h\),
\(L/h\to\infty\) — l'uniformité de \(C_{p,\Omega}\) n'est pas fournie par le
théorème général. Guzmán et Salgado (`NS-SRC-0111`) suivent précisément, dans
le cadre \(L^2\to H^1\), la dépendance au rapport entre le diamètre du domaine
et celui d'une boule étoilante. L'ansatz direct (1.1) évite ce coût;
Bogovskiĭ doit rester un outil de correction avec constante mesurée, pas un
argument abstrait d'uniformité.

## 3. Vortex rings : même topologie, composantes inversées

| Source primaire et statut | Équation et géométrie exacte | Ce qui est utile | Ce qui ne se transfère pas |
|---|---|---|---|
| J. Norbury, [*A steady vortex ring close to Hill's spherical vortex*](https://doi.org/10.1017/S0305004100047083), *Math. Proc. Cambridge Philos. Soc.* **72** (1972), 253–284, publié | Euler 3D, \(\mathbb R^3\), onde progressive axisymétrique sans swirl; vorticité azimutale compacte, proportionnelle à \(r\) dans le cœur | support torique, fermeture géométrique, asymptotiques de cœur | la vorticité est toroïdale, non poloïdale; la vitesse n'est pas compacte et l'équation est inviscide |
| Hao Feng et Vladimír Šverák, [*On the Cauchy Problem for Axi-Symmetric Vortex Rings*](https://doi.org/10.1007/s00205-014-0775-4), *Arch. Ration. Mech. Anal.* **215** (2015), 89–123, publié | Navier–Stokes 3D sur \(\mathbb R^3\), axisymétrique sans swirl; donnée de vorticité mesure portée par un cercle ou combinaison coaxiale | estimations uniformes pour régularisations de filaments, existence sans petite circulation | donnée initiale singulière, vorticité toroïdale, classe sans swirl déjà globalement régulière; aucun blow-up Clay |
| Thierry Gallay et Vladimír Šverák, [*Remarks on the Cauchy problem for the axisymmetric Navier–Stokes equations*](https://doi.org/10.5802/cml.25), *Confluentes Math.* **7** (2015), 67–92, publié | NS axisymétrique sans swirl; \(\omega^\theta\in L^1(dr\,dz)\), puis mesures à petite partie atomique | cadre critique exact et loi de Biot–Savart axisymétrique | solutions potentiellement d'énergie infinie; orientation toroïdale |
| Gallay–Šverák, [*Uniqueness of axisymmetric viscous flows originating from circular vortex filaments*](https://doi.org/10.24033/asens.2402), *Ann. Sci. Éc. Norm. Supér.* **52** (2019), 1025–1071, publié | NS, filament circulaire arbitrairement intense, solution axisymétrique sans swirl unique | contrôle non perturbatif à petit temps | ne produit pas de return-flow poloïdal ni de cascade singulière |
| Gallay–Šverák, [*Vanishing viscosity limit for axisymmetric vortex rings*](https://doi.org/10.1007/s00222-024-01261-5), *Invent. Math.* **237** (2024), 275–348, publié; arXiv v3 | NS à petite viscosité issu d'un filament circulaire; anneau d'épaisseur \(\sqrt{\nu t}\), vitesse de Kelvin | contrôle précis de diffusion, translation et erreurs d'approximation | limite \(\nu\to0\), pas temps de blow-up; le support compact est immédiatement perdu |
| Daomin Cao et Weicheng Zhan, [*On the Steady Axisymmetric Vortex Rings for 3D Incompressible Euler Flows*](https://doi.org/10.1137/24M1678076), *SIAM J. Math. Anal.* **58** (2026), 1288–1315, publié le 2026-04-01 | Euler 3D sur \(\mathbb R^3\), anneaux stationnaires/relatifs avec ou sans swirl par fonction de courant de Stokes | source récente publiée sur support torique et desingularisation avec swirl | Euler, non NS; ansatz Grad–Shafranov couplé, pas le seul potentiel \(U=\psi e_\theta\) |
| Dengjun Guo, In-Jee Jeong et Lifeng Zhao, [*Global dynamics of a single vortex ring*](https://arxiv.org/abs/2602.20131), arXiv:2602.20131v1 du 2026-02-23 | Euler 3D axisymétrique sans swirl; concentration globale, translation de Kelvin–Hicks et filamentation linéaire du support pour une large classe de données | avertit qu'un anneau fin n'est pas géométriquement stationnaire dans des normes fortes | prépublication; Euler; vorticité toroïdale; aucune conséquence directe pour l'ansatz poloïdal |

Une annonce de séminaire 2026 de Noah Stevenson sur un travail à venir avec
Razvan Radu, « Smooth and swirling steady vortex rings near the Hill–Norbury
family », mentionne des anneaux d'Euler lisses à l'ordre infini convergeant vers
le vortex de Hill. Aucun article primaire ou préprint correspondant n'a été
repéré à la date de coupure; ce contenu est classé **ANNOUNCEMENT_ONLY** et n'est
pas utilisé comme résultat.

La distinction des composantes est décisive :

\[
\begin{array}{c|c|c}
 & \text{vitesse} & \text{vorticité}\\ \hline
\text{vortex ring sans swirl} & u^r e_r+u^z e_z & \omega^\theta e_\theta\\
\text{ansatz 0027} & \psi e_\theta &
-\psi_z e_r+r^{-1}(r\psi)_r e_z.
\end{array}
\]

Confondre ces deux lignes inverse le rôle du champ de courant et invalide le
raccord à Clay.

## 4. Tubes de flux et solutions compactes voisines

S. K. Smirnov,
[*Decomposition of solenoidal vector charges into elementary solenoids, and
the structure of normal one-dimensional flows*](https://www.unige.ch/~smirnov/papers/solenoid-j.pdf),
*Algebra i Analiz* **5** (1993), 206–238; traduction *St. Petersburg Math. J.*
**5** (1994), 841–867, décompose les charges solénoïdales de masse finie en
solénoïdes élémentaires portés par des courbes récurrentes. C'est un résultat
structurel de return-flow, mais sans contrôle Lorentz critique, BMO directionnel
ou constante d'épaisseur.

Alberto Enciso et Daniel Peralta-Salas,
[*Existence of knotted vortex tubes in steady Euler flows*](https://doi.org/10.1007/s11511-015-0123-z),
*Acta Math.* **214** (2015), 61–134, réalisent des tubes de vorticité noués dans
des champs d'Euler stationnaires. Les champs de Beltrami utilisés ne sont pas
compacts et ont une queue; la topologie des tubes est transférable, les bornes
du cycle ne le sont pas.

Deux constructions publiées sont plus proches de la compacité simultanée de la
vitesse et de sa vorticité :

- A. V. Gavrilov,
  [*A steady Euler flow with compact support*](https://doi.org/10.1007/s00039-019-00476-6),
  *Geom. Funct. Anal.* **29** (2019), 190–197, construit un champ d'Euler
  stationnaire \(C_c^\infty(\mathbb R^3)\), localisé près d'un cercle;
- Peter Constantin, Joonhyun La et Vlad Vicol,
  [*Remarks on a paper by Gavrilov: Grad–Shafranov equations, steady solutions
  ...*](https://doi.org/10.1007/s00039-019-00516-1), *Geom. Funct. Anal.*
  **29** (2019), 1773–1793, donnent une construction par équations de
  Grad–Shafranov localisables.

Ces travaux démontrent qu'un champ lisse compact avec circulation interne et
retour n'est pas topologiquement impossible. Ils ne fournissent pas une
solution stationnaire de Navier–Stokes non forcé : en insérant un champ d'Euler
stationnaire dans NS, le résidu visqueux \(-\nu\Delta U\) demeure. Un champ
harmonique compact étant nul, cette différence ne peut être supprimée par une
simple identification Euler/NS.

Daniel Peralta-Salas et Radu Slobodeanu,
[*A symmetry theorem for localizable steady solutions of the 3D Euler
equations*](https://arxiv.org/abs/2606.13462), arXiv:2606.13462v1 du
2026-06-11, montrent que les écoulements d'Euler localisables analytiques dans
un domaine borné sont axisymétriques, avec section transverse disque ou anneau
à bords convexes. C'est une prépublication sans référence de revue. Elle
renforce l'intérêt de la géométrie axisymétrique pour les champs compacts
localisables, sans produire de contrôle NS ni BMO.

## 5. Critères BMO de direction et test de l'ansatz

Zachary Bradshaw et Zoran Grujić,
[*A spatially localized \(L\log L\) estimate on the vorticity in the 3D
NSE*](https://arxiv.org/abs/1309.2519), arXiv v5, publié dans *Indiana Univ.
Math. J.* **64** (2015), 433–440,
[DOI 10.1512/iumj.2015.64.5496](https://doi.org/10.1512/iumj.2015.64.5496),
considèrent une solution de Leray sur \(\mathbb R^3\), \(\nu=1\), et supposent

\[
\sup_{0<t<T}\|\chi\xi(\cdot,t)\|_{
\widetilde{bmo}_{1/|\log r|}}<\infty,                  \tag{5.1}
\]

où \(\chi\) est une coupure spatiale et
\(\xi=\omega/|\omega|\). Ils en déduisent une borne locale uniforme
\(L\log L\) sur \(|\omega|\). Pour une fonction intégrable,

\[
\|f\|_{\widetilde{bmo}_{\phi}}
=\|f\|_{L^1}
+\sup_{x,\,0<r<1/2}
\frac{\fint_{Q_r(x)}|f-f_{Q_r(x)}|}{\phi(r)},
\qquad \phi(r)=\frac1{|\log r|}.                       \tag{5.2}
\]

La condition est une borne, non une petiteness. Elle est toutefois uniforme
jusqu'au premier temps singulier potentiel et porte sur **toutes** les petites
cubes, notamment celles centrées sur les virages et les interfaces de retour.

La prépublication de Zoran Grujić,
[*Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D
Navier–Stokes Equations*](https://arxiv.org/abs/2607.08866),
arXiv:2607.08866v2 du 2026-07-13, suppose simultanément un profil critique
\(\omega\in L_t^\infty L_x^{3/2,\infty}\) et
\(\xi\in L_t^\infty bmo_{1/|\log r|}\), puis revendique un gain logarithmique
par commutateur et De Giorgi. Sa fiche arXiv ne donne pas de référence de revue
à la date de coupure. Elle est la cible comparative la plus proche, mais elle
**suppose** exactement l'uniformité directionnelle que la cascade 0027 cherche
à tester.

Pour (1.1), sur \(\{W\ne0\}\),

\[
\xi=\frac{-\Phi_z e_r+\Phi_r e_z}
{\sqrt{\Phi_z^2+\Phi_r^2}}.                             \tag{5.3}
\]

Trois coûts sont distincts :

1. **Virage méridien.** Une boucle régulière fermée fait tourner sa tangente
   d'un tour. Si un virage d'angle d'ordre un est concentré dans une zone de
   diamètre \(h\), une boule de rayon comparable à \(h\) peut avoir une
   oscillation moyenne d'ordre un; le quotient (5.2) coûte alors
   \(\Theta(\log(1/h))\).
2. **Rotation azimutale.** La composante \(e_r\) dépend de \(\theta\). À rayon
   majeur \(R\), son changement sur une boule de taille \(h\ll R\) est
   \(O(h/R)\), donc subordonné si \(R/h\to\infty\); il devient d'ordre un près
   de l'axe ou sur une boule macroscopique.
3. **Zéros de vorticité.** La direction n'est pas définie là où
   \(\nabla\Phi=0\). Une extension arbitraire peut créer un saut. Placer les
   virages dans une zone de faible magnitude aide les critères limités aux
   hautes vorticités, mais pas automatiquement la norme (5.1), qui localise la
   direction par une coupure spatiale et non par \(|\omega|\).

Ces trois estimations sont des diagnostics géométriques du laboratoire, pas des
théorèmes sourcés. Le test décisif doit calculer le suprémum BMO sur les boules
de virage, pas seulement une moyenne sur le support entier.

## 6. Veille 2025–2026 sur le cas axisymétrique avec swirl

Le cas publié classique sans swirl est globalement régulier. Pour le swirl non
nul, les résultats publiés ciblés restent conditionnels ou perturbatifs; par
exemple Hui Chen, Daoyuan Fang et Ting Zhang,
[*Regularity of 3D axisymmetric Navier–Stokes equations*](https://doi.org/10.3934/dcds.2017081),
*Discrete Contin. Dyn. Syst.* **37** (2017), 1923–1939, obtiennent des critères
Prodi–Serrin sur \(u^\theta\) et une régularité globale lorsque le swirl initial
est suffisamment petit dans \(L^3\).

Une série récente de Rishad Shahmurov revendique beaucoup plus :

- [arXiv:2604.21213v1](https://arxiv.org/abs/2604.21213), 2026-04-23, décrit un
  « master manuscript » mais dit encore réduire la tâche finale à une estimation
  locale;
- [arXiv:2605.01875v3](https://arxiv.org/abs/2605.01875), 2026-05-15, revendique
  une continuation grandes données dans la classe axisymétrique avec swirl;
- [arXiv:2605.09797v2](https://arxiv.org/abs/2605.09797), 2026-05-15, revendique
  en plus une réduction du système 3D complet;
- [arXiv:2606.07869v1](https://arxiv.org/abs/2606.07869), 2026-06-05, revendique
  la régularité globale pour toute donnée axisymétrique lisse d'énergie finie
  avec swirl arbitraire.

Aucune de ces quatre fiches ne porte de référence de revue. La succession
rapide d'architectures et l'ampleur croissante des conclusions exigent un audit
ligne par ligne des premières inégalités critiques, constantes de seuil,
compacités de paquets et passages à la limite. En l'absence de cet audit et
d'une validation publiée indépendante, aucun de ces énoncés n'est utilisé comme
lemme.

Si le dernier préprint était validé, il couvrirait l'évolution NS issue de
\(U_0=\psi e_\theta\), car cette donnée est axisymétrique avec swirl. Il ne
résoudrait toutefois pas le problème Clay positif pour les données 3D
arbitraires. La revendication plus large de 2605.09797, elle, toucherait Clay et
doit donc être soumise au niveau d'examen maximal.

## 7. Transfert exact au problème Clay

Prenons le problème Clay non forcé sur \(\mathbb R^3\), viscosité \(\nu>0\),
avec donnée initiale \(u_0\in C_c^\infty\), divergence nulle.

Implication valide : si \(\psi\in C_c^\infty((0,\infty)\times\mathbb R)\) est
supportée loin de l'axe, alors

\[
u_0=\psi e_\theta
\]

est une donnée Clay admissible et sa vorticité est exactement (1.1). Si le
support touche l'axe, il faut ajouter les conditions de pôle de Liu–Wang.

Limites du raccord :

- « purement swirl » n'est pas une classe stationnaire générale. À l'instant
  initial,

  \[
  (U\cdot\nabla)U=-\frac{\psi^2}{r}e_r,
  \]

  et si \(\partial_z(\psi^2/r)\ne0\), ce terme n'est pas un gradient global;
  l'évolution génère des composantes méridiennes. Seule l'axisymétrie, pas la
  forme purement azimutale, est préservée par unicité locale.
- la chaleur et la pression sont non locales; pour \(t>0\), le support compact
  est en général perdu;
- un profil statique div–curl ne contrôle ni le temps maximal, ni la norme
  critique dynamique, ni le vortex stretching;
- les vortex rings sans swirl sont une sous-classe globalement régulière et ne
  constituent pas des candidats de blow-up;
- une solution stationnaire d'Euler compacte n'est pas une solution
  stationnaire de NS non forcé à cause de \(-\nu\Delta u\);
- une construction Bogovskiĭ prouve la divergence nulle, mais pas une borne
  BMO ou Lorentz uniforme du champ corrigé.

Une singularité NS rigoureuse issue de cet ansatz suffirait bien à la branche
négative de Clay, puisque Clay n'exclut pas les données axisymétriques. Mais
aucune source ci-dessus ne fournit un tel mécanisme; au contraire, les résultats
sans swirl et les revendications 2026 sur le swirl rendent indispensable de
tester d'abord si l'axe est dynamiquement trop régulier.

## 8. Expérience discriminante recommandée

La meilleure expérience de 0027 est une famille explicite
\(\Phi_{L,h,R}=r\psi_{L,h,R}\) dont les niveaux sont des rectangles arrondis
allongés, supportés dans \(r\in[R-2h,R+L+2h]\) avec \(R>3h\). Pour chaque
profil, il faut certifier ou borner :

1. les identités (1.1)–(1.3), le support et les conditions de pôle;
2. \(\|W\|_{L^{3/2,\infty}}\), les masses orientées \(\pm e_z\) et la masse des
   virages;
3. l'oscillation de (5.3) sur une grille couvrante de boules, raffinée autour
   des quatre virages et des zéros de \(\nabla\Phi\);
4. la quantité

   \[
   \sup_{0<\rho<1/2}|\log\rho|
   \sup_x\fint_{B_\rho(x)}|\xi-\xi_{B_\rho(x)}|;
   \]

5. le coût de toute correction div–curl et sa dépendance en \(L/h\);
6. si le profil est testé comme quasi-état, le résidu NS projeté
   \(\mathbb P[(U\cdot\nabla)U]-\nu\Delta U\), avec pression recalculée.

Critère d'abandon falsifiable : si toute famille maintenant une masse conique
normalisée non nulle possède une boule de virage de rayon \(\Theta(h)\) avec
oscillation \(\geq c>0\), alors sa norme BMO logarithmique croît au moins comme
\(c\log(1/h)\). Cela éliminerait l'axe « return-flow axisymétrique compatible
avec BMO uniforme » sans éliminer l'ansatz comme contre-profil statique.

Critère de poursuite : si les virages peuvent être placés dans une région dont
la masse de vorticité et le coût BMO pondéré décroissent tout en conservant
uniformément la masse conique, le faible-\(L^{3/2}\), la régularité au pôle et
le résidu projeté, le premier lemme nouveau serait précisément cette borne
uniforme. Aucune source primaire repérée ne l'anticipe.
