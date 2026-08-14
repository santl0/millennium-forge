# Revue bibliographique contradictoire — cycle 0010

Date de coupure de la veille : **2026-08-14**
Objet : construction Hou–Wang–Yang de non-unicité Leray–Hopf pour Navier–Stokes 3D non forcé.

## Verdict synthétique

La source primaire actuellement la plus récente est la version **v2** de Thomas Hou, Yixuan Wang et Changhe Yang, *Nonuniqueness of Leray-Hopf solutions to the unforced incompressible 3D Navier-Stokes Equation*, [arXiv:2509.25116](https://arxiv.org/abs/2509.25116), soumise initialement le 29 septembre 2025 et révisée le 19 mars 2026 (PDF daté du 20 mars 2026). À la date de coupure, aucune v3, référence de revue, publication avec comité de lecture ni DOI éditorial n’a été trouvé dans les sources primaires consultées. Le statut exact est donc : **prépublication affirmant une preuve assistée par ordinateur**, avec code public, mais sans reproduction indépendante réalisée dans ce cycle.

Le résultat revendiqué porte sur une donnée initiale compacte et d’énergie finie, mais **singulière comme \(1/|x|\) à l’origine** et en général hors de \(L^3\). Il produit une infinité de solutions de Leray–Hopf adaptées, toutes lisses pour \(t>0\), ayant cette même trace initiale. Il ne construit ni blow-up en temps positif à partir d’une donnée lisse, ni non-unicité pour une donnée admissible dans la formulation positive de Clay.

Des estimations uniformes en un rayon \(R\) existent bien dans la localisation **extérieure** de la preuve. Elles ne constituent pas un lemme de désingularisation uniforme à l’origine : la donnée reste singulière, dépend de \(R\), et la taille admissible des coordonnées instables décroît comme \(R^{-1/8}\). Aucun énoncé primaire trouvé ne fournit un passage uniforme d’un cutoff intérieur \(\rho\downarrow0\) vers des données lisses.

## 1. Version, auteurs et statut

| Élément | Résultat de l’audit |
|---|---|
| Auteurs | Thomas Hou, Yixuan Wang, Changhe Yang |
| Source canonique | [arXiv:2509.25116](https://arxiv.org/abs/2509.25116) |
| Version initiale | v1, 29 septembre 2025, 71 pages ([PDF v1](https://arxiv.org/pdf/2509.25116v1)) |
| Version courante | v2, 19 mars 2026, 74 pages ([PDF v2](https://arxiv.org/pdf/2509.25116v2)) |
| Publication | Aucune référence de revue ou DOI éditorial indiqué sur arXiv ; aucune version publiée ultérieure repérée au 2026-08-14 |
| Nature | Prépublication ; preuve analytique conditionnée par des inégalités vérifiées par calcul assisté |
| Reproduction de ce cycle | Audit des énoncés et artefacts publics seulement ; le calcul d’environ 800 Go de RAM n’a pas été réexécuté |

La v2 rend explicite dans le Théorème 1 la régularité
\[
u_{\mathrm{loc}}\in C^\infty(\mathbb R^3\setminus\{0\})\cap L^q(\mathbb R^3)
\quad\text{pour tout }q<3,
\]
qui n’apparaissait pas sous cette forme dans l’énoncé affiché de la v1. Cette précision ne lisse pas l’origine ; elle souligne au contraire que le point \(x=0\) est exclu.

## 2. Équation, domaine, donnée et conclusion exactes

L’équation traitée est Navier–Stokes incompressible tridimensionnel, non forcé, sur l’espace entier, avec viscosité normalisée à \(1\) :
\[
\partial_tu+(u\cdot\nabla)u-\Delta u+\nabla p=0,\qquad
\nabla\cdot u=0,\qquad
u|_{t=0}=u_{\mathrm{loc}},
\]
sur \(\mathbb R^3\times[0,1]\), sans frontière.

Le Théorème 1 de la v2 affirme l’existence d’une donnée \(u_{\mathrm{loc}}\), divergence nulle et à support compact, telle qu’il existe une infinité de solutions distinctes de Leray–Hopf adaptées ayant cette donnée. Plus précisément :

- \(u_{\mathrm{loc}}\in C^\infty(\mathbb R^3\setminus\{0\})\cap L^q(\mathbb R^3)\) pour tout \(q<3\), donc en particulier \(u_{\mathrm{loc}}\in L^2\) ;
- au voisinage de l’origine,
  \[
  u_{\mathrm{loc}}(x)=|x|^{-1}A(x/|x|),
  \]
  pour un champ angulaire divergence-free approprié ;
- cette singularité est localement dans \(L^q\) exactement pour \(q<3\), mais pas génériquement dans \(L^3\) ;
- les solutions appartiennent à \(L^s([0,1];L^q(\mathbb R^3))\) pour tout \(q>2\) et tout \(s\) tel que
  \[
  \frac3q+\frac2s>1,
  \]
  et sont lisses pour chaque temps strictement positif.

La loi d’échelle est
\[
u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t).
\]
La norme \(L^q_x\) se transforme par \(\|u_\lambda\|_q=\lambda^{1-3/q}\|u\|_q\), et \(L^s_tL^q_x\) est critique quand \(3/q+2/s=1\). L’intégrabilité annoncée est donc du côté **supercritique** \(3/q+2/s>1\), et ne déclenche pas les critères de Prodi–Serrin. L’énergie \(L^2\) est supercritique sous cette mise à l’échelle.

### Notion de solution

La définition utilisée impose
\[
u\in L^\infty_{\mathrm{loc}}([0,T);L^2_\sigma)
\cap L^2_{\mathrm{loc}}([0,T);H^1_\sigma),
\]
l’équation distributionnelle contre les champs tests compacts divergence-free et l’inégalité globale d’énergie. « Adaptée » signifie en outre l’inégalité locale d’énergie
\[
(\partial_t-\Delta)\frac{|u|^2}{2}+|\nabla u|^2
+\nabla\cdot\left[\left(\frac{|u|^2}{2}+p\right)u\right]\leq0
\]
au sens des distributions. Pour les branches construites, qui sont lisses lorsque \(t>0\), l’identité locale vaut alors avec égalité hors du temps initial. La preuve établit aussi la trace forte
\[
\|u(t)-u_{\mathrm{loc}}\|_{L^2}\longrightarrow0
\quad(t\downarrow0).
\]

Il s’agit donc bien de solutions faibles énergétiques et adaptées, et non de solutions classiques sur l’intervalle fermé \([0,1]\). Leur lissité pour \(t>0\) n’efface pas la singularité de la trace initiale.

## 3. Profil auto-similaire et eigenmode instable

La branche de base est une solution auto-similaire avant :
\[
u_e(x,t)=t^{-1/2}U_e(x/\sqrt t),
\]
où \(\xi=x/\sqrt t\) et
\[
-\frac12U_e-\frac12\xi\cdot\nabla U_e
+\mathbb P(U_e\cdot\nabla U_e)-\Delta U_e=0,
\qquad \nabla\cdot U_e=0.
\]
Son champ lointain satisfait
\[
U_e(\xi)=|\xi|^{-1}A(\xi/|\xi|)+O(|\xi|^{-3}).
\]

Dans la convention d’évolution, la linéarisation est
\[
L_Uv=\frac12v+\frac12\xi\cdot\nabla v
-\mathbb P(U\cdot\nabla v+v\cdot\nabla U)+\Delta v.
\]
Le papier résout numériquement puis certifie une formulation elliptique utilisant le signe opposé : la valeur propre certifiée \(\widetilde\lambda<0\) correspond ainsi à une valeur propre de \(L_U\) de partie réelle positive. Confondre ces deux conventions inverserait à tort la conclusion de stabilité.

Le Théorème 2 affirme l’existence exacte, au sens faible, d’un triplet \((U_e,v_e,\lambda_e)\) proche des approximants, avec \(U_e\in H^1_{\mathrm{loc}}\), \(v_e\in H^1\), \(v_e\neq0\), et le signe spectral strict requis. Les propositions ultérieures donnent la régularité et le comportement lointain. Le calcul candidat est axisymétrique ; le profil de base est pair en \(z\), tandis que l’eigenmode choisi est impair en \(z\) et brise cette symétrie. Ce mécanisme spectral est le germe des branches, mais il n’est pas à lui seul un théorème abstrait de stabilité ou de robustesse sous modification de la donnée initiale.

## 4. Construction et quantificateurs des branches

La donnée homogène \(u_{\mathrm{in}}(x)=|x|^{-1}A(x/|x|)\) n’est pas dans \(L^2(\mathbb R^3)\) à l’infini. Une localisation de Bogovskiĭ à grand rayon \(R\) produit
\[
u_{\mathrm{in}}=u_{\mathrm{loc}}+w,
\]
où \(u_{\mathrm{loc}}\) est divergence-free, compacte, égale à \(u_{\mathrm{in}}\) près de l’origine, et \(w=0\) pour \(|x|<R\). Pour \(p>3\),
\[
\|w\|_{L^p}\lesssim R^{-(p-3)/p}.
\]
Le terme
\[
u_{\mathrm{cut}}=-e^{t\Delta}w
\]
annule la trace lointaine. L’ansatz est
\[
u=u_e+u_{\mathrm{cut}}+u_{\mathrm{cor}},\qquad
u_{\mathrm{cor}}(x,t)=t^{-1/2}U_{\mathrm{cor}}(x/\sqrt t,\log t).
\]

La dynamique de \(U_{\mathrm{cor}}\) est écrite par Duhamel et scindée par les projecteurs de Riesz entre un sous-espace instable de dimension finie et son complément stable. Les coordonnées stables sont intégrées depuis \(\tau=-\infty\), tandis que les coordonnées instables sont prescrites à \(\tau=0\), c’est-à-dire à \(t=1\), puis intégrées en arrière.

Pour le choix \(p=4\), \(\alpha=1-3/p=1/4\), la norme de contraction contient
\[
\|U\|_X=\sup_{\tau<0}R^{1/8}e^{-\delta\tau}
\|U(\tau)\|_{H^3}.
\]
La structure des quantificateurs extraite de la section 2.2 est :
\[
\exists R_0,\eta>0\ \forall R\ge R_0\
\forall (U_{j0})_j\text{ satisfaisant }
\sum_jR^{1/8}\|U_{j0}\|_{H^3}\le\eta,
\]
le problème de point fixe admet une branche correspondante. La variation des coordonnées terminales dans cette boule produit une infinité de solutions, distinctes notamment par leur valeur à \(t=1\), et leurs corrections convergent vers zéro dans \(L^2\) lorsque \(t\downarrow0\).

Cette lecture n’ajoute pas un théorème au papier : les constantes génériques restent implicites et la formulation ci-dessus synthétise les choix successifs de la preuve.

## 5. Audit du « cutoff uniforme »

| Question | Ce que la source établit | Ce qu’elle n’établit pas |
|---|---|---|
| Uniformité des estimations de chaleur | Les constantes de l’équation (2.10) sont annoncées indépendantes de \(R\) et de \(\tau\) | Pas de valeur numérique explicite de toutes ces constantes |
| Fermeture du point fixe | Les estimations (2.18)–(2.20) gagnent \(R^{-\alpha/2}=R^{-1/8}\) ; \(R\) est choisi assez grand, puis \(\eta\) assez petit | Pas de \(R_0\) numérique entièrement reconstruit à partir des constantes de semigroupe/résolvante |
| Taille des branches | \(\sum_jR^{1/8}\|U_{j0}\|_{H^3}\le\eta\) | Pas de séparation inférieure non nulle indépendante de \(R\) : la taille admissible décroît comme \(R^{-1/8}\) |
| Donnée commune | Pour chaque \(R\) fixé, les branches partagent le même \(u_{\mathrm{loc}}\) | \(u_{\mathrm{loc}}\) dépend de \(R\) |
| Nature du cutoff | Le cutoff est extérieur et restaure l’énergie finie à l’infini | Il ne régularise pas \(x=0\) |
| Passage à une donnée lisse | Aucun | Aucun cutoff intérieur \(\rho\downarrow0\), aucune persistance uniforme des branches, aucun théorème de désingularisation |

Conclusion : il existe un **mécanisme d’estimations uniformes en cutoff extérieur**, dispersé dans la preuve, mais aucun lemme autonome trouvé qui fournisse à la fois des constantes explicites, une séparation uniforme des branches et un passage à une donnée initiale lisse. Employer l’expression « lemme uniforme en cutoff » sans préciser « extérieur » serait trompeur.

## 6. Rôle exact du calcul assisté et du dépôt

L’Assumption 1 du papier demande un profil et un eigenpair approximatifs, divergence-free et normalisés, avec résidus \(L^2\) suffisamment petits, orthogonalités et asymptotiques contrôlées. Les Propositions 1 et 2 convertissent ces bornes en un profil et un eigenpair exacts par un argument de point fixe : partie coercive plus perturbation compacte, cette dernière étant approchée par un opérateur de rang fini.

Le candidat numérique est obtenu par éléments finis sur un grand domaine, après compactification radiale \(r=\tan\beta\), puis interpolé dans une base trigonométrique exactement divergence-free. La vérification des inégalités (4.44)–(4.63) couvre notamment les résidus \(L^2\), les compensations en normes \(W^{k,\infty}\), la normalisation, les matrices de Gram, les interactions non linéaires et les bornes d’inversibilité du problème de rang fini. La section 7 décrit une représentation trigonométrique finie, une formule de Newton–Cotes composite à sept points avec reste borné par la dérivée d’ordre huit, des bornes de Bernstein/interpolation et l’enclosure par intervalles des constantes de Bessel.

La portée logique est :

1. le calcul par intervalles revendiqué certifie les hypothèses quantitatives près des approximants ;
2. les arguments fonctionnels en déduisent un profil et un eigenpair exacts ;
3. la construction de l’infinité de branches et la localisation extérieure sont ensuite analytiques.

Le dépôt [HouGroup2026/3d-navier-stokes-nonuniqueness](https://github.com/HouGroup2026/3d-navier-stokes-nonuniqueness) fournit six notebooks Julia à exécuter dans un ordre documenté. Son README exige Julia 1.11 ou ultérieur et au moins 800 Go de RAM. Au moment de l’audit :

- la branche principale pointe sur le commit [615ee6f3eca3abad7b5814fe9334bcd80bea0328](https://github.com/HouGroup2026/3d-navier-stokes-nonuniqueness/commit/615ee6f3eca3abad7b5814fe9334bcd80bea0328) ;
- aucun tag ni release n’est publié ;
- le [Project.toml à ce commit](https://raw.githubusercontent.com/HouGroup2026/3d-navier-stokes-nonuniqueness/615ee6f3eca3abad7b5814fe9334bcd80bea0328/Project.toml) énumère les dépendances, mais n’impose pas de bornes de compatibilité ;
- aucun Manifest.toml n’est présent ; le README précise que les versions sont résolues automatiquement, malgré un passage de présentation qui évoque une reproduction exacte par manifeste.

L’absence de manifeste, de release immuable et de petit vérificateur indépendant n’invalide pas les estimations publiées. Elle empêche toutefois de qualifier l’artefact public actuel d’environnement intégralement épinglé et reproduit. Le statut de laboratoire approprié reste donc **CAP revendiquée dans une prépublication — reproduction indépendante en attente**, et non « calcul de haute précision seulement » ni « preuve reproduite ».

## 7. Sources primaires connexes et portée

### Origine du mécanisme

- Hao Jia et Vladimír Šverák, [*Are the incompressible 3d Navier–Stokes equations locally ill-posed in the natural energy space?*](https://arxiv.org/abs/1306.2136), arXiv:1306.2136, publié dans *Journal of Functional Analysis* 268 (2015), 3734–3766. Ce travail établit le mécanisme conditionnel : une instabilité spectrale appropriée d’un profil auto-similaire permet, après localisation, une non-unicité issue d’une donnée énergétique singulière.
- Hao Jia et Vladimír Šverák, [*Local-in-space estimates near initial time for weak solutions of the Navier–Stokes equations and forward self-similar solutions*](https://arxiv.org/abs/1204.0529), arXiv:1204.0529, *Inventiones Mathematicae* 196 (2014), 233–265. C’est une source primaire pour l’existence et le contrôle local des profils avant.
- Julien Guillod et Vladimír Šverák, [*Numerical investigations of non-uniqueness for the Navier–Stokes initial value problem in borderline spaces*](https://arxiv.org/abs/1704.00560), arXiv:1704.00560. Cette étude fournit l’évidence numérique précurseure, sans certification assistée par ordinateur.

### Développements postérieurs disponibles au 2026-08-14

- Alexandru Ionescu, Hao Jia et Samuel Palasek, [arXiv:2606.07501](https://arxiv.org/abs/2606.07501), v1 du 5 juin 2026. Les auteurs calculent un **autre** profil axisymétrique sans swirl, avec un résidu ponctuel global annoncé de l’ordre de \(10^{-10}\), et donnent un théorème analytique conditionnel : si un profil et un mode exacts avec les décroissances requises existent, alors des branches non uniques existent dans des cadres critiques/Sobolev plus forts. Le calcul est présenté comme une forte évidence numérique, non comme une CAP. Cette source ne reproduit pas le certificat Hou–Wang–Yang et ne lisse pas l’origine.
- Daniel Binz et Daniel Coiculescu, [*Homothetic Self-Similar Solutions and a Singularity Formation Mechanism for the Navier–Stokes Equations*](https://arxiv.org/abs/2607.12159), arXiv:2607.12159v1, 13 juillet 2026. Leur résultat négatif montre, sous les hypothèses de régularité/Morrey précisées, l’absence de profils homothétiques tridimensionnels non triviaux nécessaires à une stratégie de limite singulière en amplitude de type Euler. Il contraint une voie de stabilité/désingularisation, mais ne réfute pas Hou–Wang–Yang : cette construction certifie directement un profil Navier–Stokes fixé et emploie un cutoff spatial extérieur, non une limite homothétique d’amplitude.

Aucune de ces sources primaires postérieures ne démontre :

- la stabilité non linéaire de la construction Hou–Wang–Yang sous lissage de la singularité \(1/|x|\) ;
- deux branches partant de la même donnée \(C^\infty_c\) ;
- une séparation des branches uniforme sous un cutoff intérieur ;
- une reproduction indépendante complète des notebooks par intervalles.

## 8. Implication explicite pour le problème Clay

La chaîne réellement établie, sous validation de la CAP, est
\[
\text{profil avant instable exact}
\Longrightarrow
\text{branches faibles énergétiques multiples}
\Longrightarrow
\text{non-unicité Leray--Hopf adaptée pour une donnée }L^2
\text{ singulière}.
\]

La chaîne requise pour toucher directement l’alternative Clay serait plutôt
\[
\text{donnée initiale lisse admissible}
\Longrightarrow
\text{solution classique maximale}
\Longrightarrow
\text{perte de régularité en temps fini},
\]
ou une preuve de prolongement global. Le premier maillon de raccord est absent : \(u_{\mathrm{loc}}\notin C^\infty(\mathbb R^3)\) et généralement \(u_{\mathrm{loc}}\notin L^3\). Toutes les branches Hou–Wang–Yang sont lisses pour \(t>0\), si bien qu’aucune singularité positive n’est produite.

La faible-forte unicité renforce l’obstacle. Pour une donnée lisse, deux solutions de Leray–Hopf ne peuvent se séparer tant qu’une solution forte correspondante existe. Une désingularisation réussie devrait donc non seulement préserver l’instabilité, mais aussi forcer ou dépasser le temps de rupture de la solution forte. C’est précisément ce que les estimations de cutoff extérieur ne contrôlent pas.

## 9. Recommandation falsifiable

Le prochain test borné à meilleure valeur informationnelle est un **audit quantitatif du cutoff extérieur**, préalable à toute conjecture de désingularisation :

> Reconstruire, à partir des constantes de semigroupe, résolvante, projections de Riesz et estimations bilinéaires de la section 2.2, des nombres explicites \(R_0,\eta,C\) tels que, pour tout \(R\ge R_0\) et toute coordonnée instable vérifiant \(\sum_jR^{1/8}\|U_{j0}\|_{H^3}\le\eta\), le point fixe ferme et deux choix donnés restent séparés à \(t=1\).

Critère de réussite : toutes les inégalités de contraction sont fermées avec des intervalles numériques reproductibles et une borne de séparation positive pour chaque \(R\) fixé. Critère de réfutation : une constante cachée dépend de \(R\), un projecteur n’est pas borné dans l’espace utilisé, ou la séparation calculée n’est pas déductible des coordonnées terminales.

Le résultat devra être consigné comme **uniformité extérieure seulement**. La proposition Clay-relevante, distincte et actuellement non démontrée, serait :
\[
\exists t_*,c>0\ \forall \rho\in(0,\rho_0],\
\exists u_\rho^{(1)},u_\rho^{(2)}
\quad
\|u_\rho^{(1)}(t_*)-u_\rho^{(2)}(t_*)\|_2\ge c,
\]
pour une même donnée divergence-free lisse \(u_{\mathrm{loc},\rho}\) obtenue par cutoff intérieur de taille \(\rho\). Elle est falsifiée pour tout \(t_*\) situé dans l’intervalle d’existence forte commun ; toute tentative doit donc suivre explicitement la durée de vie forte et les constantes lorsque \(\rho\downarrow0\). Aucune source auditée ne fournit aujourd’hui ces quantificateurs.

## Sources primaires principales

- Hou, Wang, Yang, [arXiv:2509.25116v2](https://arxiv.org/abs/2509.25116), [PDF v2](https://arxiv.org/pdf/2509.25116v2).
- Dépôt CAP, [HouGroup2026/3d-navier-stokes-nonuniqueness](https://github.com/HouGroup2026/3d-navier-stokes-nonuniqueness).
- Jia, Šverák, [arXiv:1306.2136](https://arxiv.org/abs/1306.2136).
- Jia, Šverák, [arXiv:1204.0529](https://arxiv.org/abs/1204.0529).
- Guillod, Šverák, [arXiv:1704.00560](https://arxiv.org/abs/1704.00560).
- Ionescu, Jia, Palasek, [arXiv:2606.07501](https://arxiv.org/abs/2606.07501).
- Binz, Coiculescu, [arXiv:2607.12159](https://arxiv.org/abs/2607.12159).
