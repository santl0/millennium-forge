# Cycle 0031 — veille primaire : curl compact, direction log-BMO et swirl anisotrope

Date de coupure : 2026-08-14.

Périmètre : sources primaires concernant (i) la structure des rotationnels de
vitesses lisses compactes, (ii) les critères de régularité fondés sur la
direction de vorticité, en particulier aux seuils critiques faibles-Lorentz et
log-BMO, (iii) les données axisymétriques avec swirl et les déformations
anisotropes, et (iv) les annonces 2025–2026 directement voisines. Les calculs
marqués **AI_DERIVATION** ne sont ni des résultats publiés ni des preuves du
problème Clay.

## Verdict différentiel

1. Aucun article primaire publié repéré n'énonce le raccord exact

   \[
   u\in C_c^\infty(\mathbb R^3),\quad \nabla\cdot u=0,\quad
   \|u\|_{L^{3,\infty}}+\|\operatorname{curl}u\|_{L^{3/2,\infty}}<\infty,
   \quad \xi\text{ asymptotiquement plate}
   \Longrightarrow \text{existence ou impossibilité}.
   \]

   La source la plus proche est la prépublication Grujić
   [arXiv:2607.08866v2](https://arxiv.org/abs/2607.08866v2), qui juxtapose
   précisément une borne critique
   \(\omega\in L_t^\infty L_x^{3/2,\infty}\) et une hypothèse directionnelle
   \(\xi\in L_t^\infty\mathrm{bmo}_{1/|\log r|}\). Elle **suppose** ces
   contrôles dans un scénario de profil critique; elle ne construit pas de curl
   compact qui les réalise et ne les déduit pas de l'équation. Elle reste une
   v2 non publiée, dont la chaîne de preuve doit conserver le statut
   PREPRINT_CLAIM.

2. Il existe une obstruction orientée élémentaire, exacte et plus faible. Si
   \(u\in C_c^1(\mathbb R^3;\mathbb R^3)\), alors

   \[
   \int_{\mathbb R^3}\operatorname{curl}u\,dx=0.                 \tag{1}
   \]

   Par conséquent, un curl non nul ne peut avoir toutes ses directions dans
   un hémisphère **orienté strict**
   \(\{\eta\in S^2:\eta\cdot e\ge c\}\), \(c>0\). Ce fait n'interdit pas
   l'aplatissement projectif autour de \(\{+e,-e\}\), une compensation de
   faible amplitude sur grand volume, ni un coeur local presque unidirectionnel
   dont le retour se trouve dans une couche éloignée.

3. Les critères publiés de Constantin–Fefferman, Beirão da Veiga–Berselli,
   Giga–Miura et Miller utilisent un angle par \(\sin\theta\) ou un produit
   vectoriel. Ils ne distinguent donc pas \(+e\) et \(-e\). La prépublication
   Lei–Ren–Tian autorise explicitement un double cône autour de ces deux
   directions. Ils ne transforment pas (1) en contrôle log-BMO orienté.

4. Une famille axisymétrique pure-swirl, lisse et compacte loin de l'axe,
   réalise cinématiquement une direction de curl presque verticale au sens
   projectif. Mais le comptage critique donne, dans le régime d'aspect plat,

   \[
   \frac{\|\omega\|_{L^{3/2,\infty}}}
        {\|u\|_{L^{3,\infty}}}
   \asymp \left(\frac{RH}{h^2}\right)^{1/3}\longrightarrow\infty.
                                                               \tag{2}
   \]

   C'est un **no-go dimensionnel interne** pour cette famille simple : elle ne
   peut conserver simultanément une vitesse faible-\(L^3\) non petite, une
   vorticité faible-\(L^{3/2}\) uniformément bornée et un aspect
   \(h\ll H,R\). Ce n'est pas un théorème pour toutes les vitesses compactes;
   des oscillations, plusieurs tores ou des compensateurs multi-échelles
   pourraient changer le comptage.

5. Les résultats publiés sur le swirl axisymétrique restent conditionnels :
   petitesse du swirl, form-boundedness critique, décroissance logarithmique
   près de l'axe, ou borne a priori uniforme de la vitesse en
   \(L^{3,\infty}\). L'annonce Shahmurov
   [arXiv:2606.07869v1](https://arxiv.org/abs/2606.07869v1) revendique le cas
   axisymétrique à swirl arbitraire, mais n'a qu'une v1 non publiée et repose
   sur de nouveaux maillons porteurs. Elle demeure en quarantaine et ne peut
   être utilisée dans un raccord Clay.

## 1. Cadre exact et échelle

Le test cinématique porte sur

\[
 u\in C_c^\infty(\mathbb R^3;\mathbb R^3),\qquad
 \nabla\cdot u=0,\qquad \omega=\nabla\times u.                 \tag{3}
\]

Il ne suppose pas que \(u\) soit une tranche temporelle d'une solution. Pour
Navier–Stokes incompressible non forcé sur \(\mathbb R^3\), \(\nu>0\),

\[
 \partial_tu+(u\cdot\nabla)u+\nabla p=\nu\Delta u,
 \qquad \nabla\cdot u=0,                                      \tag{4}
\]

l'échelle est

\[
 u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),\qquad
 \omega_\lambda(x,t)=\lambda^2\omega(\lambda x,\lambda^2t).
                                                               \tag{5}
\]

Les quasi-normes \(\|u\|_{L^{3,\infty}}\) et
\(\|\omega\|_{L^{3/2,\infty}}\) sont toutes deux invariantes par (5). Une
simple remise à l'échelle isotrope ne peut donc améliorer leur quotient. La
direction \(\xi=\omega/|\omega|\) n'est définie que sur
\(\{\omega\ne0\}\); tout énoncé BMO doit préciser son extension ou sa coupure
sur l'ensemble nul.

## 2. Ce qu'impose réellement un rotationnel compact

### 2.1 Annulation globale et hémisphère strict

Pour chaque composante, l'intégration d'une dérivée compacte donne (1). Si,
sur \(\{\omega\ne0\}\),

\[
 \xi(x)\cdot e\ge c>0,
\]

alors

\[
 0=e\cdot\int\omega
   =\int |\omega|\,\xi\cdot e
   \ge c\int|\omega|,
\]

donc \(\omega=0\). De même, si \(\omega=f e\) pour une direction fixe,
\(\nabla\cdot\omega=0\) donne \(e\cdot\nabla f=0\); la compacité de \(f\)
force encore \(f=0\). Ces deux arguments sont **AI_DERIVATION** élémentaires.

Leur quantificateur est global. Sur une boule \(B\), l'identité correcte est

\[
 \int_B\omega\,dx=\int_{\partial B}n\times u\,dS,              \tag{6}
\]

de sorte qu'un coeur local exactement orienté est compatible avec un flux de
retour à travers le bord. L'obstruction ne voit pas non plus un double cône :
les masses proches de \(+e\) et \(-e\) peuvent s'annuler sans quitter ce
double cône.

### 2.2 Potentiels compacts et constructions Euler

Costabel et McIntosh, [*On Bogovskiĭ and regularized Poincaré integral
operators for de Rham complexes on Lipschitz
domains*](https://doi.org/10.1007/s00209-009-0517-8), *Math. Z.* **265**
(2010), 297–320, [arXiv:0808.2614](https://arxiv.org/abs/0808.2614),
construisent des opérateurs d'homotopie régularisés pour le complexe de de
Rham, avec contrôle de support et de régularité dans les domaines adaptés.
Cette source justifie qu'une donnée solénoïdale compatible puisse posséder un
potentiel à support contrôlé. Elle ne permet pas d'imposer arbitrairement la
direction de \(\operatorname{curl}u\), et les conditions de compatibilité ne
disparaissent pas.

Gavrilov, [*A steady Euler flow with compact
support*](https://doi.org/10.1007/s00039-019-00476-6), *Geom. Funct. Anal.*
**29** (2019), 190–197, [arXiv:1810.08020](https://arxiv.org/abs/1810.08020),
construit un champ lisse compact non nul satisfaisant Euler stationnaire

\[
 (u\cdot\nabla)u+\nabla p=0,\qquad \nabla\cdot u=0.            \tag{7}
\]

Constantin, La et Vicol, [*Remarks on a paper by Gavrilov: Grad–Shafranov equations,
steady solutions of the three-dimensional incompressible Euler equations with
compactly supported velocities, and
applications*](https://doi.org/10.1007/s00039-019-00516-1),
*Geom. Funct. Anal.* **29** (2019), 1773–1793,
[arXiv:1903.11699](https://arxiv.org/abs/1903.11699), développent le mécanisme
de localisabilité dans un cadre Grad–Shafranov axisymétrique.

Ces articles montrent que support compact, incompressibilité et géométrie
axisymétrique ne sont pas incompatibles. Le non-transfert à (4) est exact :
insérer un Euler stationnaire compact dans Navier–Stokes non forcé laisse le
résidu \(-\nu\Delta u\). Il devient une solution stationnaire NS seulement
avec une force adaptée \(f=-\nu\Delta u\), hors du cas Clay non forcé.

Deux prépublications 2026 affinent cette géométrie sans combler le raccord :

- Peralta-Salas et Slobodeanu, [*A symmetry theorem for localizable steady
  solutions of the 3D Euler equations*](https://arxiv.org/abs/2606.13462v1),
  arXiv:2606.13462v1, 11 juin 2026, étudient la rigidité axisymétrique de
  solutions Euler stationnaires analytiques localisables. Il s'agit d'Euler,
  sans viscosité ni endpoint Lorentz.
- Peralta-Salas et Wan, [*Piecewise smooth stationary Euler flows with support
  in a neighborhood of a helix*](https://arxiv.org/abs/2607.16141v1),
  arXiv:2607.16141v1, 17 juillet 2026, construisent des solutions Euler
  stationnaires hélicoïdales, seulement piècewise lisses, dont la section
  redimensionnée est intrinsèquement anisotrope. Le voisinage d'une hélice
  n'est pas un support compact admissible de donnée Clay, et l'équation est
  Euler, \(\nu=0\).

## 3. Critères directionnels : orientation ou droite projective

| Source primaire | Équation, domaine, solution et hypothèse | Conclusion | Non-transfert au verrou 0031 |
|---|---|---|---|
| Constantin–Fefferman, [*Direction of Vorticity and the Problem of Global Regularity for the Navier–Stokes Equations*](https://doi.org/10.1512/iumj.1993.42.42034), *Indiana Univ. Math. J.* **42** (1993), 775–789 | NS incompressible non forcé, \(\mathbb R^3\), \(\nu>0\), solution faible issue d'une donnée de type \(H^1\); cohérence lipschitzienne pairwise de la direction dans la région de forte vorticité | régularisation/solution forte | \(|\xi(x)\times\xi(y)|\) identifie \(+e\) et \(-e\); ni endpoint Lorentz ni moyenne nulle compacte |
| Beirão da Veiga–Berselli, [*On the regularizing effect of the vorticity direction in incompressible viscous flows*](https://doi.org/10.57262/die/1356060864), *Differential Integral Equations* **15** (2002), 345–356 | NS non forcé, \(\mathbb R^3\), Leray–Hopf avec donnée \(H^1\); cohérence Hölder, endpoint spatial \(1/2\) inclus | solution forte | module pairwise sign-insensible, beaucoup plus fort qu'une petite oscillation moyenne; aucune borne \(L^{3/2,\infty}\) |
| Giga–Miura, [*On vorticity directions near singularities for the Navier–Stokes flows with infinite energy*](https://doi.org/10.1007/s00220-011-1197-x), *Commun. Math. Phys.* **303** (2011), 289–300 | solution mild bornée sur \(\mathbb R^3\), énergie possiblement infinie; borne Type I de vitesse et continuité uniforme de \(\xi\) sur la zone de forte vorticité | pas de blow-up | hypothèses Type I et continuité uniforme; aucun curl compact ni endpoint faible-Lorentz de vorticité |
| Miller, [*A Locally Anisotropic Regularity Criterion for the Navier–Stokes Equation in Terms of Vorticity*](https://doi.org/10.1090/bproc/74), *Proc. Amer. Math. Soc. Ser. B* **8** (2021), 60–74, [arXiv:2002.02152](https://arxiv.org/abs/2002.02152) | solution mild \(C([0,T_{max});H^1(\mathbb R^3))\), champ unitaire auxiliaire \(v\) à gradient borné; critère via \(\int\|v\times\omega\|_2^4dt\) | sa finitude exclut le blow-up | parallèle et antiparallèle donnent tous deux zéro; condition spatio-temporelle \(L_t^4L_x^2\), non log-BMO |
| Barker–Prange, [*Scale-Invariant Estimates and Vorticity Alignment for Navier–Stokes in the Half-Space with No-Slip Boundary Conditions*](https://doi.org/10.1007/s00205-019-01435-z), *Arch. Ration. Mech. Anal.* **235** (2020), 881–926, [arXiv:1906.08225](https://arxiv.org/abs/1906.08225) | NS sur \(\mathbb R^3_+\), non-slip; solution adaptée/Type I, continuité uniforme de direction dans une région parabolique de forte vorticité | exclusion d'une singularité au bord | domaine à bord, Type I et continuité uniforme; pas le problème Clay entier ni l'endpoint log-BMO |
| Lei–Ren–Tian, [*A geometric characterization of potential Navier–Stokes singularities*](https://arxiv.org/abs/2501.08976v1), arXiv:2501.08976v1, 15 janvier 2025 | NS local non forcé, \(\nu=1\), solution faible adaptée dans \(Q(1)\); les grandes vorticités restent dans un double cône fixe autour de \(\{+e,-e\}\) | régularité dans \(Q(1/2)\) revendiquée | v1 non publiée; aucune hypothèse Lorentz. Une platitude seulement sur un coeur, une suite de profils ou des superniveaux non uniformes ne vérifie pas automatiquement le théorème |
| Grujić, [*Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier–Stokes Equations*](https://arxiv.org/abs/2607.08866v2), arXiv:2607.08866v2, 13 juillet 2026 | NS non forcé sur \(\mathbb R^3\); scénario conditionnel de profil critique, \(\omega\in L_t^\infty L_x^{3/2,\infty}\), direction dans \(\mathrm{bmo}_{1/|\log r|}\), hypothèses de forme et d'uniformité | exclusion conditionnelle revendiquée | seule source repérée combinant les deux endpoints visés; v2 non publiée et hypothèses posées, non produites par un curl compact |

### Réponse au théorème recherché

La veille n'a trouvé **aucun théorème publié** qui interdise ou construise une
direction de curl compact asymptotiquement plate tout en suivant simultanément
les deux endpoints

\[
 u\in L^{3,\infty},\qquad \operatorname{curl}u\in L^{3/2,\infty}. \tag{8}
\]

Il faut distinguer trois énoncés :

- la platitude **orientée dans un hémisphère strict global** est impossible par
  (1), sans utiliser (8);
- la platitude **projective** près de \(\{+e,-e\}\) est compatible avec (1) et
  même favorable aux noyaux classiques de déplétion;
- une petite oscillation BMO du vecteur orienté voit les interfaces
  \(+e/-e\), mais aucune source publiée ne déduit son comportement de (8) et
  de la seule compacité.

La prépublication Lei–Ren–Tian constitue une permission/exclusion
conditionnelle importante : un double cône uniforme sur **toute** la région de
forte vorticité d'un cylindre entraîne la régularité revendiquée. Elle ne
s'applique pas à la seule convergence d'un coeur redimensionné vers une droite.
La prépublication Grujić constitue le raccord conditionnel orienté le plus
proche, mais elle suppose directement la régularité log-BMO.

## 4. Swirl compact et déformation anisotrope

### 4.1 Famille pure-swirl admissible comme donnée initiale

En coordonnées cylindriques, prenons

\[
 u=u^\theta(r,z)e_\theta,
 \qquad
 u^\theta(r,z)=A\,\Phi\!\left(\frac{r-R}{h},\frac zH\right),   \tag{9}
\]

où \(\Phi\in C_c^\infty((-1,1)^2)\), \(R>2h\). Alors \(u\) est lisse,
compact, axisymétrique, supporté loin de l'axe, et \(\nabla\cdot u=0\). Son
rotationnel est exactement

\[
 \omega^r=-\partial_z u^\theta,\qquad
 \omega^\theta=0,\qquad
 \omega^z=\frac1r\partial_r(ru^\theta)
          =\partial_ru^\theta+\frac{u^\theta}{r}.              \tag{10}
\]

Dans le régime \(h\ll H\) et \(h\ll R\), la dérivée radiale domine sur les
zones non dégénérées de transition : \(\omega\) est presque parallèle ou
antiparallèle à \(e_z\). La variation du signe radial fournit la compensation
nécessaire à (1). La direction est donc plate **projectivement**, non orientée.

Le volume du tore est \(V\asymp RhH\). Pour une forme \(\Phi\) fixée et non
dégénérée, le comptage de fonction de distribution donne

\[
 \|u\|_{L^{3,\infty}}\asymp A(RhH)^{1/3},                     \tag{11}
\]

\[
 \|\omega\|_{L^{3/2,\infty}}
 \asymp \frac Ah(RhH)^{2/3},                                 \tag{12}
\]

d'où (2). Les constantes implicites dépendent de la forme fixe \(\Phi\), mais
pas de \(A,R,h,H\) tant que les rapports géométriques restent dans le régime
annoncé. (9)–(12) sont **AI_DERIVATION** et doivent être testés par fonctions de
distribution exactes ou arithmétique d'intervalles avant toute affirmation
uniforme sur une classe de profils.

Cette famille donne une donnée initiale admissible du cas Clay entier. Elle ne
donne pas un profil de blow-up : sous l'évolution axisymétrique avec swirl, les
termes centrifuges couplent le swirl au mouvement méridien, et la forme
pure-swirl n'est pas un ansatz dynamique fermé arbitraire.

### 4.2 Résultats publiés qui bornent le corridor axisymétrique

Zhen Lei et Qi S. Zhang, [*Criticality of the Axially Symmetric Navier–Stokes
Equations*](https://doi.org/10.2140/pjm.2017.289.169), *Pacific J. Math.*
**289** (2017), 169–187, [arXiv:1505.02628](https://arxiv.org/abs/1505.02628),
traitent (4) sur \(\mathbb R^3\) pour une solution forte axisymétrique issue
d'une donnée \(H^{1/2}\). Ils obtiennent la régularité globale sous une
condition critique de forme sur la circulation
\(\Gamma=ru^\theta\); la décroissance
\(|ru^\theta|\le C_*|\log r|^{-2}\) près de l'axe est une condition
suffisante. C'est un logarithme sur la **magnitude de circulation**, non le
log-BMO de la direction de vorticité.

Yanlin Liu, [*Solving the axisymmetric Navier–Stokes equations in critical
spaces (I): The case with small swirl
component*](https://doi.org/10.1016/j.jde.2022.01.011),
*J. Differential Equations* **314** (2022), 287–315, prouve l'existence globale
lisse sur \(\mathbb R^3\) pour des données axisymétriques dans des espaces
critiques, sous une petitesse explicite du swirl impliquant notamment
\(r^{-1/2}u_0^\theta\in L^2\) et \(u_0^\theta\in L^3\). Cette petitesse n'est
pas automatique pour (9) lorsque l'aspect devient extrême.

Ożański et Palasek, [*Quantitative Control of Solutions to the Axisymmetric
Navier–Stokes Equations in Terms of the Weak \(L^3\)
Norm*](https://doi.org/10.1007/s40818-023-00156-7), *Ann. PDE* **9** (2023),
article 15, [arXiv:2210.10030v3](https://arxiv.org/abs/2210.10030v3), prouvent
que, pour une solution forte axisymétrique sur \([0,T]\times\mathbb R^3\), une
borne \(\|u\|_{L_t^\infty L_x^{3,\infty}}\le A\) contrôle quantitativement
toutes les dérivées par une borne doublement exponentielle. Leur corollaire de
Liouville concerne les solutions anciennes axisymétriques uniformément
faible-\(L^3\). C'est le contrôle publié le plus directement utile pour
l'endpoint vitesse de (8), mais il suppose déjà la borne uniforme en temps et
ne fournit pas (12) ni une direction plate.

Chemin, Gallagher et Paicu, [*Global regularity for some classes of large
solutions to the Navier–Stokes
equations*](https://doi.org/10.4007/annals.2011.173.2.9),
*Ann. of Math.* **173** (2011), 983–1012,
[arXiv:0807.1265](https://arxiv.org/abs/0807.1265), construisent des classes de
grandes données variant lentement dans une direction et donnant une solution
globale lisse. Le domaine principal de l'article est
\(\mathbb T^2\times\mathbb R\), non \(\mathbb R^3\). Le message falsifiable est
néanmoins important : une anisotropie « lente dans une direction » peut
dépléter la non-linéarité et tomber dans une classe globale plutôt que créer une
singularité; aucun transfert au cas Clay entier ne suit sans lemme de passage de
domaine et correspondance exacte des données.

## 5. Veille 2025–2026 et statut

| Source primaire et version vérifiée | Équation exacte / cadre | Statut au 2026-08-14 | Pertinence et non-transfert |
|---|---|---|---|
| Lei–Ren–Tian, [arXiv:2501.08976v1](https://arxiv.org/abs/2501.08976v1), 15 janvier 2025 | NS local, solution faible adaptée dans \(Q(1)\), double cône des fortes vorticités | v1, aucune publication affichée | critère projectif le plus proche; pas de Lorentz, pas de construction compacte |
| Barker, [*Quantitative classification of potential Navier–Stokes singularities beyond the blow-up time*](https://arxiv.org/abs/2510.20757v3), arXiv:2510.20757v3, 11 août 2026 | NS 3D, classifications quantitatives pour données approximativement axisymétriques et voisinage des temps potentiels de blow-up | v3 non publiée | fournit des tests quantitatifs de candidats; ne donne ni curl plat ni critère log-BMO/Lorentz fermé |
| Shahmurov, [arXiv:2606.07869v1](https://arxiv.org/abs/2606.07869v1), 5 juin 2026 | NS incompressible sur \(\mathbb R^3\), revendication de régularité globale axisymétrique à swirl arbitraire, notamment donnée lisse compacte | v1 de 99 pages, aucune publication affichée; **quarantaine** | si valide, couvrirait un sous-cas strict du Clay, pas le problème général; les nouveaux lemmes de « typed zero-output » et d'amorçage énergétique doivent être reproduits avant usage |
| Peralta-Salas–Slobodeanu, [arXiv:2606.13462v1](https://arxiv.org/abs/2606.13462v1), 11 juin 2026 | Euler stationnaire localisable, théorème de symétrie | v1 non publiée | rigidité géométrique Euler; \(\nu=0\), pas NS ni Lorentz |
| Grujić, [arXiv:2607.08866v2](https://arxiv.org/abs/2607.08866v2), 13 juillet 2026 | NS \(\mathbb R^3\), scénario critique conditionnel faible-\(L^{3/2}\) + direction log-BMO | v2 non publiée | maillon exact le plus proche; hypothèses non dérivées et preuve non reproduite intégralement |
| Peralta-Salas–Wan, [arXiv:2607.16141v1](https://arxiv.org/abs/2607.16141v1), 17 juillet 2026 | Euler stationnaire hélicoïdal piècewise lisse, section anisotrope | v1 non publiée | construction anisotrope, mais Euler, non lisse globalement et non compacte au sens Clay |

La veille différentielle n'a trouvé aucune version publiée nouvelle qui change
le statut du verrou. En particulier, ni l'annonce axisymétrique de Shahmurov ni
la chaîne log-BMO de Grujić ne doivent être utilisées comme théorèmes établis.

## 6. Passe contradictoire et implication Clay

### Attaques effectuées

1. **Confusion direction/droite.** Réfutée : les critères en sinus voient
   \(+e\) et \(-e\) comme parfaitement cohérents, alors que l'oscillation BMO
   du vecteur orienté voit leur interface.
2. **Moyenne globale utilisée localement.** Réfutée par (6). Le flux de bord
   peut exporter toute la compensation hors du coeur.
3. **Endpoint faible-Lorentz transformé en intégrabilité forte.** Interdit :
   \(L^{3/2,\infty}\) n'a pas l'absolue continuité de norme nécessaire pour
   faire disparaître automatiquement une couche rare.
4. **Anisotropie assimilée à singularité.** Réfutée par les classes globales
   de Chemin–Gallagher–Paicu et les critères axisymétriques conditionnels.
5. **Euler compact transféré à NS.** Réfuté par le résidu visqueux
   \(-\nu\Delta u\).
6. **Pure swirl conservé par l'évolution.** Faux sans preuve : les équations
   axisymétriques couplent swirl, vorticité azimutale et vitesse méridienne.
7. **Constante uniforme dans (11)–(12).** Elle dépend de la forme
   normalisée; une famille de formes dégénérantes peut invalider le symbole
   \(\asymp\). C'est précisément la porte laissée ouverte au test numérique.
8. **Prépublication assimilée à résultat établi.** Lei–Ren–Tian, Barker,
   Grujić, Shahmurov et les deux prépublications Euler 2026 restent étiquetés
   par leur version et sans promotion PAPER_PROOF.

### Implication exacte vers Clay

Une donnée Clay lisse compacte et divergence-free vérifie bien (3), donc (1),
et les deux normes de (8) sont finies. C'est le seul transfert automatique.
Les implications suivantes restent manquantes :

\[
 \text{donnée compacte anisotrope}
 \not\Longrightarrow
 \sup_{t<T}\|u(t)\|_{L^{3,\infty}}<\infty,
\]

\[
 \text{platitude du curl initial}
 \not\Longrightarrow
 \xi(t)\in\mathrm{bmo}_{1/|\log r|}
 \quad\text{uniformément près d'un }T^*,
\]

\[
 \text{résultat Euler localisable}
 \not\Longrightarrow
 \text{solution NS non forcée},
\]

\[
 \text{double cône d'un profil extrait}
 \not\Longrightarrow
 \text{double cône uniforme de la solution dans }Q(1).
\]

Ainsi, cette veille ne fournit ni régularité globale ni blow-up admissible.
Elle ferme seulement le sous-chemin le plus naïf : « rendre un unique tore
pure-swirl arbitrairement plat tout en gardant les deux endpoints critiques
uniformes ».

## 7. Sources à intégrer ultérieurement au catalogue

Sans modifier literature/navier-stokes/sources.json dans ce travail, quatre
sources primaires vérifiées méritent une entrée dédiée si elles ne sont pas
déjà présentes au moment de la synthèse :

1. Chemin–Gallagher–Paicu 2011, DOI
   [10.4007/annals.2011.173.2.9](https://doi.org/10.4007/annals.2011.173.2.9),
   avec le domaine principal \(\mathbb T^2\times\mathbb R\) explicitement
   enregistré;
2. Lei–Zhang 2017, DOI
   [10.2140/pjm.2017.289.169](https://doi.org/10.2140/pjm.2017.289.169),
   condition de forme critique sur \(ru^\theta\);
3. Yanlin Liu 2022, DOI
   [10.1016/j.jde.2022.01.011](https://doi.org/10.1016/j.jde.2022.01.011),
   petitesse du swirl en espaces critiques;
4. Peralta-Salas–Wan 2026,
   [arXiv:2607.16141v1](https://arxiv.org/abs/2607.16141v1), en statut
   prépublication Euler, sans transfert NS.

Barker–Prange 2020 doit également être ajouté si l'audit du catalogue confirme
son absence; son domaine demi-espace/no-slip est un champ de métadonnées
indispensable.

## 8. Expérience décisive recommandée

Le prochain test à haute valeur informationnelle doit rester dans la famille
(9), mais remplacer les équivalences dimensionnelles par des calculs de
fonctions de distribution certifiés. Pour un profil polynomial par morceaux
lissé avec paramètres rationnels, calculer sur une grille d'intervalles :

1. les résidus exacts de \(\nabla\cdot u\) et de (10);
2. \(\|u\|_{L^{3,\infty}}\) et
   \(\|\omega\|_{L^{3/2,\infty}}\) avec encadrement supérieur et inférieur;
3. la proportion de masse hors du double cône
   \(\{|\xi\times e_z|\le\varepsilon\}\);
4. l'oscillation moyenne orientée sur toutes les boules rencontrant les couches
   de changement de signe;
5. la pente en \(h/H\) et \(h/R\) du quotient (2).

Issue discriminante : une borne inférieure certifiée

\[
 \frac{\|\omega\|_{L^{3/2,\infty}}}
      {\|u\|_{L^{3,\infty}}}
 \ge c_\Phi\left(\frac{RH}{h^2}\right)^{1/3}
\]

pour une classe non dégénérée de profils condamnerait rigoureusement le tore
pure-swirl simple. Une violation robuste signalerait soit une erreur dans le
comptage (11)–(12), soit un mécanisme de cancellation de niveau suffisamment
fort pour justifier un modèle multi-échelle. Même une réussite ne constituerait
qu'un résultat cinématique : pression, évolution, énergie et raccord à une
solution admissible de (4) resteraient entièrement ouverts.
