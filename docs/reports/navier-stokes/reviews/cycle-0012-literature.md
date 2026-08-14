# Revue bibliographique — cycle 0012

Date de la veille : 2026-08-14
Objet : unicité faible–forte depuis des données lisses, non-unicité auto-similaire forward avec trace à \(\tau=-\infty\), et recherche d’un transfert 2025–2026 vers une même donnée Clay lisse à temps fini.

## Statut d’indépendance

Cette revue a été produite par la même famille de modèles Codex que les cycles précédents. Elle constitue une passe contradictoire séparée par la tâche et par les sources consultées, mais pas une revue indépendante au sens d’un autre système, d’une autre équipe ou d’une reproduction humaine.

## Verdict

Aucun résultat primaire localisé au 2026-08-14 ne transfère la multiplicité de Hou–Wang–Yang ou le scénario conditionnel d’Ionescu–Jia–Palasek vers deux solutions de Leray–Hopf ayant une même donnée initiale Clay lisse à un temps fini.

L’obstruction est un théorème, pas seulement une difficulté technique. Pour une donnée lisse divergence-free, la solution forte locale est unique dans la classe de Leray–Hopf. Toute autre solution de Leray–Hopf issue de la même donnée coïncide avec elle jusqu’au temps maximal de régularité forte. Par conséquent,

\[
\left.
\begin{array}{c}
u_0\ \text{lisse et admissible Clay},\\
u^{(1)},u^{(2)}\ \text{Leray--Hopf},\\
u^{(1)}(0)=u^{(2)}(0)=u_0,\quad u^{(1)}\neq u^{(2)}
\end{array}
\right\}
\Longrightarrow
T_{\max}^{\mathrm{fort}}(u_0)<\infty.
\tag{1}
\]

Autrement dit, un tel transfert serait déjà une résolution négative du problème Clay : il ne peut pas être obtenu par un simple argument perturbatif qui éviterait de démontrer une perte préalable de régularité.

Les résultats récents qui paraissent s’en approcher échappent tous à au moins une hypothèse de (1) :

- donnée initiale singulière ou d’énergie infinie;
- solution faible hors de \(L^\infty_tL^2_x\cap L^2_tH^1_x\);
- énergie seulement décroissante, sans terme de dissipation de Leray–Hopf;
- solution mild singulière dont le produit est défini par paraproduit et qui n’est pas imposée dans \(L^2_{\mathrm{loc}}\);
- force extérieure;
- données seulement presque identiques;
- calcul numérique sans preuve.

## 1. Cadre exact de l’unicité faible–forte

### 1.1 Équation et classes

On fixe, sur \(\mathbb R^3\) ou \(\mathbb T^3\),

\[
\partial_tu+(u\cdot\nabla)u-\nu\Delta u+\nabla p=0,
\qquad
\nabla\cdot u=0,
\qquad
\nu>0,
\tag{2}
\]

sans force extérieure. Sur \(\mathbb R^3\), une donnée Clay positive est lisse, divergence-free et rapidement décroissante; sur le tore, elle est lisse, périodique et divergence-free.

Une solution de Leray–Hopf \(v\) sur \([0,T]\) satisfait notamment

\[
v\in L^\infty(0,T;L^2_\sigma)
\cap L^2(0,T;H^1_\sigma),
\tag{3}
\]

l’équation au sens des distributions, la trace forte appropriée à \(t=0\), et l’inégalité énergie–dissipation

\[
\frac12\|v(t)\|_2^2
+\nu\int_0^t\|\nabla v(s)\|_2^2\,ds
\leq
\frac12\|u_0\|_2^2
\tag{4}
\]

pour les temps admissibles, avec la formulation standard forte à partir de \(t=0\).

La seule décroissance de \(t\mapsto\|v(t)\|_2\) ne remplace pas (4) : le terme
\(\nu\int\|\nabla v\|_2^2\) est une partie décisive de la notion Leray–Hopf.

### 1.2 Existence forte locale depuis une donnée lisse

Les théories de Fujita–Kato et Kato donnent une solution forte ou mild locale unique dans des espaces beaucoup plus faibles que \(C^\infty\). En particulier, pour toute donnée lisse admissible, il existe

\[
u\in C([0,T_{\mathrm{str}}];H^m_\sigma)
\cap L^2(0,T_{\mathrm{str}};H^{m+1}_\sigma)
\]

pour \(m>5/2\), après choix d’un temps \(T_{\mathrm{str}}>0\). Cette solution est classique pour \(t>0\). Elle se prolonge de manière unique jusqu’à un temps maximal
\(T_{\max}^{\mathrm{fort}}\in(0,\infty]\).

Sources primaires :

- H. Fujita et T. Kato, [On the Navier–Stokes initial value problem. I](https://doi.org/10.1007/BF00276188), Archive for Rational Mechanics and Analysis 16 (1964), 269–315.
- T. Kato, [Strong \(L^p\)-solutions of the Navier–Stokes equation in \(\mathbb R^m\), with applications to weak solutions](https://eudml.org/doc/173504), Mathematische Zeitschrift 187 (1984), 471–480, DOI [10.1007/BF01174182](https://doi.org/10.1007/BF01174182).

### 1.3 Calcul relatif et quantificateurs

Soit \(u\) une solution forte de (2), soit \(v\) une solution de Leray–Hopf avec la même trace initiale, et posons

\[
w=v-u.
\]

Le calcul d’énergie relative, justifié par approximation de la solution forte, donne

\[
\frac12\|w(t)\|_2^2
+\nu\int_0^t\|\nabla w(s)\|_2^2\,ds
\leq
\int_0^t\int
u\cdot(w\cdot\nabla)w\,dx\,ds.
\tag{5}
\]

Pour \(3<q\leq\infty\), l’interpolation de Gagliardo–Nirenberg donne, si \(q<\infty\),

\[
\|w\|_{\frac{2q}{q-2}}
\leq
C_q
\|w\|_2^{1-\frac3q}
\|\nabla w\|_2^{\frac3q}.
\]

Ainsi,

\[
\left|
\int u\cdot(w\cdot\nabla)w\,dx
\right|
\leq
C_q\|u\|_q
\|w\|_2^{1-\frac3q}
\|\nabla w\|_2^{1+\frac3q}.
\]

Par Young,

\[
\left|
\int u\cdot(w\cdot\nabla)w\,dx
\right|
\leq
\frac{\nu}{2}\|\nabla w\|_2^2
+C_{q,\nu}
\|u\|_q^{\frac{2q}{q-3}}
\|w\|_2^2.
\tag{6}
\]

Une dépendance admissible est

\[
C_{q,\nu}
=
C_q\nu^{-\frac{q+3}{q-3}}.
\]

Le coefficient de Grönwall est intégrable dès que

\[
u\in L^s(0,T;L^q),
\qquad
\frac2s+\frac3q=1,
\qquad
3<q\leq\infty.
\tag{7}
\]

Comme \(w(0)=0\), les estimations (5)–(7) donnent

\[
w\equiv0\quad\text{sur }[0,T].
\tag{8}
\]

Une solution classique locale satisfait par exemple
\(u\in L^2(0,T;L^\infty)\), donc se situe dans cette classe. L’endpoint
\(L^\infty_tL^3_x\) demande des arguments supplémentaires; il n’est pas nécessaire pour conclure depuis une donnée lisse.

Sources primaires du critère :

- G. Prodi, [Un teorema di unicità per le equazioni di Navier–Stokes](https://doi.org/10.1007/BF02410664), Annali di Matematica Pura ed Applicata 48 (1959), 173–182.
- J. Serrin, [On the interior regularity of weak solutions of the Navier–Stokes equations](https://doi.org/10.1007/BF00253344), Archive for Rational Mechanics and Analysis 9 (1962), 187–195.
- L. Escauriaza, G. Seregin et V. Šverák, [\(L_{3,\infty}\)-solutions of Navier–Stokes equations and backward uniqueness](https://doi.org/10.1070/RM2003v058n02ABEH000609), Russian Mathematical Surveys 58 (2003), 211–250, pour l’endpoint critique.

### 1.4 Implication temporelle exacte

Si \(u_0\) est lisse et \(u\) est sa solution forte maximale, alors toute solution de Leray–Hopf \(v\) de même trace satisfait

\[
v(t)=u(t)
\qquad
\text{pour tout }0\leq t<T_{\max}^{\mathrm{fort}}.
\tag{9}
\]

Trois conséquences doivent rester séparées :

1. deux branches Leray–Hopf ne peuvent pas se séparer immédiatement depuis une donnée lisse;
2. elles ne peuvent se séparer à un temps \(T_0\) où la trace commune est lisse et où l’une des branches demeure forte à droite;
3. une non-unicité Leray–Hopf depuis une donnée lisse exige une perte antérieure de régularité de la branche forte.

La translation temporelle de deux solutions auto-similaires déjà distinctes à
\(t_0>0\) ne crée pas une donnée commune : leurs valeurs lisses
\(u^{(1)}(t_0)\) et \(u^{(2)}(t_0)\) sont différentes.

## 2. Ce que signifie réellement la trace à \(\tau=-\infty\)

### 2.1 Changement de variables forward

Le programme Jia–Šverák, repris par Hou–Wang–Yang et Ionescu–Jia–Palasek, utilise

\[
\xi=\frac{x}{\sqrt t},
\qquad
\tau=\log t,
\qquad
t=e^\tau,
\tag{10}
\]

et une solution de la forme

\[
u(t,x)
=
t^{-1/2}
\left[
U\left(\frac{x}{\sqrt t}\right)
+\phi\left(\log t,\frac{x}{\sqrt t}\right)
\right].
\tag{11}
\]

La condition

\[
\phi(\tau)\longrightarrow0
\qquad
\text{lorsque }\tau\to-\infty
\tag{12}
\]

signifie que les branches partagent la même trace physique au temps
\(t=0\). Elle n’est pas une donnée de Cauchy usuelle prescrite à un temps fini dans l’espace de phase rescalé.

Le profil stationnaire \(U\) a pour comportement à l’infini

\[
U(\xi)
=
\frac1{|\xi|}
A\left(\frac{\xi}{|\xi|}\right)
+O(|\xi|^{-3})
\]

où le produit entre le facteur radial et le champ angulaire est implicite. Sans ambiguïté typographique, cela signifie

\[
U(\xi)
=
\frac1{|\xi|}
\left[
A\left(\frac{\xi}{|\xi|}\right)
\right]
+O(|\xi|^{-3}).
\]

Avec la notation de Hou–Wang–Yang, la formule exacte de la trace est

\[
u_{\mathrm{in}}(x)
=
\frac1{|x|}
\left[
A\left(\frac{x}{|x|}\right)
\right],
\tag{13}
\]

et

\[
U(\xi)
=
\frac1{|\xi|}
\left[
A\left(\frac{\xi}{|\xi|}\right)
\right]
+o(|\xi|^{-1}).
\tag{14}
\]

Dans (13)–(14), \(A\) est un champ angulaire satisfaisant la contrainte de divergence; les crochets rendent explicite qu’il s’agit de la multiplication scalaire
\(|x|^{-1}A(x/|x|)\), non d’une somme.

La singularité est exactement d’ordre

\[
|u_{\mathrm{in}}(x)|\sim|x|^{-1}
\qquad
x\to0.
\tag{15}
\]

### 2.2 Position fonctionnelle de la trace

Après localisation extérieure par une coupure divergence-free, une telle trace est compacte et vérifie typiquement

\[
u_{\mathrm{loc}}\in
L^q(\mathbb R^3)\quad\text{pour tout }q<3,
\]

\[
u_{\mathrm{loc}}\in L^{3,\infty},
\qquad
u_{\mathrm{loc}}\in H^\alpha
\quad\text{pour }\alpha<1/2,
\tag{16}
\]

mais

\[
u_{\mathrm{loc}}\notin L^3,
\qquad
u_{\mathrm{loc}}\notin H^{1/2},
\qquad
u_{\mathrm{loc}}\notin C^\infty(\mathbb R^3).
\tag{17}
\]

Le seuil \(H^{1/2}\) est critique pour la mise en données de Fujita–Kato en dimension trois. Le mécanisme est placé juste du côté singulier de ce seuil.

La localisation de Hou–Wang–Yang est extérieure :

\[
u_{\mathrm{in}}
=
u_{\mathrm{loc}}+w,
\qquad
u^{\mathrm{cut}}=-e^{t\Delta}w.
\]

Elle rend la donnée compacte mais ne modifie pas la singularité (15) à l’origine.

### 2.3 Hou–Wang–Yang

Version vérifiée :

- T. Y. Hou, Y. Wang, C. Yang, [Nonuniqueness of Leray–Hopf solutions to the unforced incompressible 3D Navier–Stokes Equation](https://arxiv.org/abs/2509.25116), arXiv:2509.25116v2, 19 mars 2026; prépublication avec preuve assistée par ordinateur.

Le théorème principal annonce des solutions sur
\(\mathbb R^3\times[0,1]\) :

\[
u^{(a)}
\in
L^\infty_tL^2_x\cap L^2_tH^1_x,
\]

adaptées et lisses pour \(t>0\), avec une même donnée compacte

\[
u_{\mathrm{loc}}
\in
C^\infty(\mathbb R^3\setminus\{0\})
\cap\bigcap_{q<3}L^q.
\tag{18}
\]

Les branches partagent (18) parce que la correction satisfait (12). Les coordonnées instables sont prescrites à \(\tau=0\), c’est-à-dire au temps physique \(t=1\), et la trajectoire est construite vers
\(\tau=-\infty\).

Implication exacte :

\[
\text{HWY}
\Longrightarrow
\text{non-unicité Leray--Hopf pour une donnée finie-énergie singulière}.
\tag{19}
\]

Mais

\[
\text{HWY}
\centernot\Longrightarrow
\text{non-unicité Leray--Hopf pour une donnée lisse}.
\tag{20}
\]

Le passage de (19) à une donnée lisse nécessiterait un lemme nouveau qui surmonte (9), donc une perte réelle de régularité avant la bifurcation.

### 2.4 Ionescu–Jia–Palasek

Version vérifiée :

- A. D. Ionescu, H. Jia, S. Palasek, [On the non-uniqueness of solutions of the axi-symmetric swirl-free Navier–Stokes equations, I](https://arxiv.org/abs/2606.07501), arXiv:2606.07501v1, 5 juin 2026.

Leur Théorème 1.2 est analytique mais conditionnel. Il suppose l’existence exacte de champs \(C^2\), \(U,\widetilde U\), et d’une valeur propre
\(\Re\lambda>0\) tels que

\[
\Delta U+\frac12x\cdot\nabla U+\frac12U-\Pi(U\cdot\nabla U)=0,
\]

\[
\Delta\widetilde U+\frac12x\cdot\nabla\widetilde U+\frac12\widetilde U
-\Pi(U\cdot\nabla\widetilde U+\widetilde U\cdot\nabla U)
=\lambda\widetilde U,
\tag{21}
\]

avec

\[
|U(x)-U_0(x)|\lesssim\langle x\rangle^{-2},
\qquad
|\widetilde U(x)|\lesssim\langle x\rangle^{-2},
\tag{22}
\]

où \(U_0\) est homogène de degré \(-1\) et lisse seulement hors de l’origine.

Sous ces hypothèses, ils obtiennent conditionnellement deux solutions de même trace

\[
u_0\in H^\alpha\cap L^{3,\infty},
\qquad
0\leq\alpha<1/2,
\tag{23}
\]

lisses pour \(t>0\), avec identité d’énergie. Le profil et le mode instable proposés dans la même prépublication proviennent d’un calcul flottant de haute précision; ils ne sont pas certifiés.

Implication exacte :

\[
\text{existence exacte de (21)--(22)}
\Longrightarrow
\text{multiplicité pour la trace singulière (23)}.
\tag{24}
\]

Le calcul numérique présenté ne démontre pas l’antécédent de (24), et même une preuve de celui-ci ne rendrait pas \(u_0\) lisse.

## 3. Pourquoi une remise à l’origine à temps positif ne transfère pas la multiplicité

Pour chaque \(t_0>0\), les branches HWY ou les branches conditionnelles IJP sont lisses en espace. Cependant,

\[
u^{(a)}(t_0)\neq u^{(b)}(t_0)
\qquad
a\neq b
\tag{25}
\]

dans la construction. Elles ne donnent donc pas deux continuations d’une même donnée lisse à \(t_0\).

Supposons au contraire qu’elles se rencontrent :

\[
u^{(a)}(t_0)=u^{(b)}(t_0)=g,
\qquad
g\in C^\infty_\sigma.
\tag{26}
\]

Comme les deux solutions sont fortes à droite de \(t_0\), l’unicité locale forte, a fortiori l’unicité faible–forte, impose

\[
u^{(a)}(t)=u^{(b)}(t)
\qquad
t\in[t_0,t_0+\varepsilon].
\tag{27}
\]

La paramétrisation par des coordonnées instables distinctes au temps final exclut (26). Une translation \(t\mapsto t+t_0\) ne change pas cette conclusion.

Un lissage intérieur \(u_{\mathrm{loc},\rho}\) de (18) produit une donnée forte. Pour chaque \(\rho>0\), il existe donc un intervalle
\([0,T_\rho]\) sur lequel toutes les solutions de Leray–Hopf de cette donnée coïncident. Obtenir une multiplicité dans la limite
\(\rho\downarrow0\) ne suffit pas : il faudrait, pour un \(\rho\) strictement positif fixé, démontrer une perte de régularité avant la séparation.

Le quantificateur manquant est

\[
\exists\rho>0,\ \exists T_\rho^*<\infty
\quad
\text{tel que la solution forte de }
u_{\mathrm{loc},\rho}
\text{ perde sa régularité à }T_\rho^*.
\tag{28}
\]

Une borne seulement dégénérée lorsque \(\rho\to0\) ne prouve pas (28).

## 4. Résultats 2025–2026 voisins et hypothèse exacte qu’ils abandonnent

### 4.1 Coiculescu–Palasek : publié, données critiques d’énergie infinie

Version et statut :

- M. P. Coiculescu, S. Palasek, [Non-uniqueness of smooth solutions of the Navier–Stokes equations from critical data](https://doi.org/10.1007/s00222-025-01396-z), Inventiones mathematicae 244 (2026), 165–219; reçu le 18 mars 2025, accepté le 3 décembre 2025, version of record le 12 décembre 2025.
- Prépublication correspondante : [arXiv:2503.14699v2](https://arxiv.org/abs/2503.14699), 21 juillet 2025.

Sur \(\mathbb T^3\), les auteurs construisent

\[
U_0\in BMO^{-1}
\]

et deux solutions globales distinctes

\[
u^{(1)},u^{(2)}
\in
C^\infty((0,\infty)\times\mathbb T^3)
\cap L^\infty([0,\infty);BMO^{-1})
\cap C_0([0,\infty);\dot W^{-1,p})
\]

pour tout \(p<\infty\), dans le chemin de Koch–Tataru.

Ils précisent explicitement que

\[
U_0\notin L^2(\mathbb T^3)
\]

et que les solutions ne sont pas de Leray–Hopf. La donnée a une énergie infinie et n’est lisse qu’en dehors d’un ensemble de mesure nulle.

Implication :

\[
\text{Coiculescu--Palasek}
\Longrightarrow
\text{non-unicité mild non forcée depuis une donnée critique singulière},
\]

mais pas multiplicité Clay lisse, et le mécanisme est lacunaire/dyadique plutôt que le mode instable HWY/IJP.

### 4.2 Cheskidov–Zeng–Zhang : toute donnée \(H^{1/2}\), mais pas Leray–Hopf

Version et statut :

- A. Cheskidov, Z. Zeng, D. Zhang, [Global dissipative solutions of the 3D Navier–Stokes and MHD equations](https://arxiv.org/abs/2503.05692), arXiv:2503.05692v1, 7 mars 2025; prépublication non publiée localisée.

Sur \(\mathbb T^3\), leur Théorème 1.2 affirme que toute donnée divergence-free

\[
u_0\in H^{1/2}
\]

admet une infinité de solutions faibles « dissipatives ». Leur Définition 1.1 signifie seulement

\[
t\longmapsto\|u(t)\|_2
\quad
\text{continue et décroissante}.
\tag{29}
\]

Cela inclut les données \(C^\infty\). Toutefois, les auteurs soulignent que les solutions construites ne peuvent pas satisfaire l’inégalité de Leray–Hopf. Elles ne contrôlent pas le terme de dissipation comme dans (4), et la méthode d’intégration convexe reste hors de la classe faible–forte rigide.

Implication :

\[
\text{CZZ}
\Longrightarrow
\text{multiplicité faible depuis toute donnée lisse avec (29)},
\]

\[
\text{CZZ}
\centernot\Longrightarrow
\text{multiplicité Leray--Hopf depuis une donnée lisse}.
\]

Ce résultat est un contre-exemple direct à l’identification fautive

\[
\text{énergie décroissante}
\equiv
\text{inégalité énergie--dissipation de Leray--Hopf}.
\]

### 4.3 Cheskidov–Dai–Palasek : donnée lisse, injection instantanée d’énergie

Version et statut :

- A. Cheskidov, M. Dai, S. Palasek, [Instantaneous Type I blow-up and non-uniqueness of smooth solutions of the Navier–Stokes equations](https://arxiv.org/abs/2511.09556), arXiv:2511.09556v2, 12 janvier 2026; prépublication.

Pour toute donnée lisse divergence-free sur \(\mathbb T^d\), \(d\geq2\), ils construisent une famille de solutions faibles qui coïncide avec la solution classique sur
\([0,T_*]\), puis bifurque à droite de \(T_*\). Chaque tranche temporelle est spatialement lisse, mais

\[
\limsup_{t\downarrow T_*}
\sqrt{t-T_*}\|u(t)\|_\infty>0
\]

le long d’une suite, avec une borne Type I supérieure.

Leur Remark 1.4 et leur Théorème 2.4 donnent l’échappatoire exacte :

\[
u\notin L^\infty_tL^2_x,
\qquad
u\notin L^2_tH^1_x
\quad
\text{près de }T_*,
\tag{30}
\]

et même

\[
\lim_{t\downarrow T_*}\|u(t)\|_2=\infty.
\tag{31}
\]

L’énergie est injectée depuis les fréquences infinies. Les solutions ne sont donc pas Leray–Hopf. Le papier démontre lui-même que si une telle branche satisfaisait les hypothèses d’énergie qui la rendent Leray–Hopf, l’unicité faible–forte imposerait qu’elle coïncide avec la solution classique.

Implication :

\[
\text{CDP}
\Longrightarrow
\text{multiplicité faible générale depuis une trace lisse à temps fini},
\]

mais (30)–(31) excluent précisément le transfert Clay.

### 4.4 Cheskidov–Hou : donnée lisse possible, mais solution mild singulière

Version et statut :

- A. Cheskidov, H. Hou, [On non-uniqueness of mild solutions and stationary singular solutions to the Navier–Stokes equations](https://arxiv.org/abs/2603.03666), arXiv:2603.03666v2, 11 juin 2026; prépublication.

Le Corollaire 1.2 donne, pour certains espaces de Besov négatifs subcritiques ou critiques,

\[
u,v\in C([0,T];B^{-\theta}_{q,r}),
\qquad
u(0)=v(0)=u_{\mathrm{in}},
\qquad
u(t)\neq v(t)\quad(t>0),
\tag{32}
\]

pour toute donnée de cet espace. Une donnée \(C^\infty\) appartient à ces espaces, donc (32) s’applique formellement à une même donnée lisse.

Cependant, la notion de solution mild est explicitement élargie :

- les auteurs n’imposent pas \(u\in L^2_{\mathrm{loc}}\);
- \(u\otimes u\) peut ne pas appartenir à \(L^1_{\mathrm{loc}}\);
- le produit est défini par une série de paraproduits de Littlewood–Paley;
- la seconde branche peut être une solution stationnaire singulière.

Ainsi, (32) n’est pas une multiplicité de solutions distributionnelles Leray–Hopf. Pour une donnée lisse, la solution classique reste unique dans toutes les classes usuelles satisfaisant les hypothèses de faible–forte; l’autre branche vit dans la notion mild singulière agrandie.

Ce résultat n’utilise pas le profil HWY/IJP et ne le désingularise pas.

### 4.5 Palasek : croissance arbitraire, données distinctes

Version et statut :

- S. Palasek, [Arbitrary norm growth in the 3D Navier–Stokes equations](https://arxiv.org/abs/2509.18595), arXiv:2509.18595v1, 23 septembre 2025; prépublication.

Le papier construit une famille de données initiales lisses, bornée dans
\(BMO^{-1}(\mathbb T^3)\), dont les solutions globales peuvent devenir arbitrairement grandes dans certaines normes. Les données de la famille sont différentes et la construction reste dans un cadre bien posé. Une grande amplification ou une forte sensibilité ne constitue pas une non-unicité.

### 4.6 Liao–Qin : données presque identiques, calcul seulement

Version et statut :

- S. Liao, S. Qin, [Non-uniqueness of smooth solutions of the Navier–Stokes equations from almost the same initial conditions](https://arxiv.org/abs/2602.12666), arXiv:2602.12666v1, 13 février 2026; prépublication numérique.

Les auteurs donnent des trajectoires numériques issues de données dont la différence peut être de l’ordre de \(10^{-40}\). Les données ne sont pas identiques, les calculs ne sont pas certifiés et une divergence chaotique de trajectoires ne réfute pas l’unicité. Il n’existe aucune implication vers (1).

### 4.7 Galdi–Gazzola : blow-up avec force et unicité

Version et statut :

- G. P. Galdi, F. Gazzola, [Blow-up and uniqueness of Leray–Hopf solutions to forced Navier–Stokes equations](https://arxiv.org/abs/2606.15189), arXiv:2606.15189v3, révisé le 21 juillet 2026 (v1 soumis le 13 juin); prépublication.

Ils construisent des forces et des données lisses donnant une solution de Leray–Hopf forcée, unique, globale au sens faible et présentant des instants de blow-up. La force appartient à des classes d'intégrabilité explicitement choisies et porte la singularité temporelle. Le résultat ne réfute pas les alternatives non forcées (A)–(B) et ne réalise pas l'alternative (C), dont la force doit être `C∞` et rapidement décroissante avec ses dérivées. Il n'établit pas non plus une multiplicité HWY/IJP.

## 5. Tableau des implications logiques

| Résultat | Même donnée lisse | Équation non forcée | Classe Leray–Hopf | Multiplicité | Transfert HWY/IJP vers Clay |
|---|---:|---:|---:|---:|---:|
| Faible–forte classique | Oui | Oui | Oui | Interdite avant blow-up | Obstruction exacte |
| Hou–Wang–Yang v2 | Non, trace \(1/|x|\) | Oui | Oui, adaptée | Oui | Non |
| Ionescu–Jia–Palasek v1 | Non, \(H^\alpha,\alpha<1/2\) | Oui | Conditionnellement oui | Conditionnelle | Non |
| Coiculescu–Palasek, Inventiones | Non, \(BMO^{-1}\setminus L^2\) | Oui | Non | Oui | Non |
| Cheskidov–Zeng–Zhang v1 | Oui | Oui | Non; énergie décroissante seulement | Oui | Non |
| Cheskidov–Dai–Palasek v2 | Oui | Oui | Non; énergie instantanément infinie | Oui | Non |
| Cheskidov–Hou v2 | Oui possible | Oui | Non; mild singulière, pas \(L^2_{\rm loc}\) | Oui | Non |
| Palasek v1 | Données lisses distinctes | Oui | Solution forte | Non | Non |
| Liao–Qin v1 | Presque, pas exactement | Selon simulation | Calcul classique | Non démontrée | Non |
| Galdi–Gazzola v3 | Oui | Non, forcée | Oui | Non, unicité | Non |

## 6. Énoncé négatif obtenu par la veille

### Proposition d’audit

À la date du 2026-08-14, aucun article primaire localisé ne démontre l’existence de

\[
u_0\in C^\infty_\sigma
\]

admissible dans l’une des formulations Clay non forcées, et de deux solutions distinctes

\[
u^{(1)},u^{(2)}
\in
L^\infty_tL^2_x\cap L^2_tH^1_x
\]

satisfaisant l’inégalité énergie–dissipation et

\[
u^{(1)}(0)=u^{(2)}(0)=u_0.
\tag{33}
\]

Les annonces de multiplicité 2025–2026 avec donnée lisse qui ont été localisées utilisent toutes une classe strictement plus large que celle de (33).

Cette proposition est un résultat de veille, non un théorème d’inexistence absolue sur toute la littérature. Elle est falsifiable par la production d’une source primaire donnant simultanément les quatre quantificateurs :

1. donnée commune exactement lisse;
2. Navier–Stokes 3D incompressible standard, non forcé;
3. deux branches distinctes;
4. deux branches Leray–Hopf avec le terme de dissipation.

## 7. Lemme de raccord minimal qui manquerait

Un raccord véritable depuis HWY/IJP devrait avoir la forme suivante.

### Lemme de raccord hypothétique

Il existe une donnée

\[
g\in C^\infty_\sigma
\]

et un temps \(T_*<\infty\) tels que :

1. la solution forte \(U\) issue de \(g\) existe sur \([0,T_*)\);
2. \(U\) perd un critère de prolongement critique à \(T_*\);
3. une renormalisation autour de \(T_*\) converge fortement vers le profil HWY ou IJP dans une topologie préservant la pression et l’inégalité d’énergie;
4. deux trajectoires instables du profil se recollent à la même trace physique de \(U\) au temps \(T_*\);
5. les deux continuations sont Leray–Hopf et restent distinctes.

Les points 1–2 contiennent déjà le cœur d’un blow-up Clay. Les constructions actuelles ne donnent que la dynamique locale autour d’un profil forward alimenté par une trace singulière à \(t=0\); elles ne produisent pas les points 2–4.

### Quantificateur adverse

Tout schéma de « lissage puis limite » doit être testé à rayon intérieur
\(\rho>0\) fixé :

\[
u_{0,\rho}\in C^\infty_\sigma.
\]

S’il ne produit la séparation que dans la limite singulière
\(\rho\downarrow0\), alors il retrouve au mieux HWY/IJP et ne prouve pas le lemme de raccord. Pour être décisif, il doit donner

\[
\exists\rho_*>0,\quad
\exists t_{\mathrm{sep}}>T_{\max}^{\mathrm{fort}}(u_{0,\rho_*}),
\quad
u_{\rho_*}^{(1)}(t_{\mathrm{sep}})
\neq
u_{\rho_*}^{(2)}(t_{\mathrm{sep}}),
\tag{34}
\]

avec deux branches Leray–Hopf et une preuve de
\(T_{\max}^{\mathrm{fort}}(u_{0,\rho_*})<\infty\).

Le test doit être abandonné comme transfert Clay si la seule conclusion est

\[
T_{\rho}\downarrow0
\quad\text{ou}\quad
\|u_{0,\rho}\|_{H^{1/2}}\uparrow\infty
\quad
\text{lorsque }\rho\downarrow0,
\]

sans un \(\rho_*>0\) satisfaisant (34).

## 8. Recommandation falsifiable

La meilleure action suivante n’est pas de chercher à « déplacer » directement
\(\tau=-\infty\) vers un temps fini. Il faut tester l’impossibilité quantitative du raccord intérieur.

Pour une désingularisation divergence-free explicite
\(u_{0,\rho}\) de la donnée HWY, calculer avec bornes démontrées :

\[
M_\rho=\|u_{0,\rho}\|_{H^{1/2}},
\qquad
T_{\mathrm{FK}}(\rho),
\]

où \(T_{\mathrm{FK}}(\rho)\) est une borne inférieure explicite du temps de vie forte de Fujita–Kato, puis comparer ce temps à l’échelle où la coordonnée instable auto-similaire pourrait devenir \(O(1)\).

Le mécanisme de transfert est réfuté dans ce modèle de lissage si l’on démontre uniformément que la fenêtre de séparation proposée est incluse dans l’intervalle faible–fort :

\[
t_{\mathrm{inst}}(\rho)
\leq
T_{\mathrm{FK}}(\rho)
\qquad
\text{pour tout }\rho>0
\text{ dans le régime contrôlé}.
\tag{35}
\]

Il reste viable seulement si l’analyse produit un régime
\(t_{\mathrm{inst}}(\rho)>T_{\mathrm{FK}}(\rho)\); cette inégalité n’est encore qu’une absence d’obstruction et non une preuve de blow-up. Toute expérience doit suivre la pression non locale, la divergence, la dépendance en \(\rho\), la norme critique \(H^{1/2}\), et l’erreur de raccord.

## Sources primaires principales

- J. Leray, [Sur le mouvement d’un liquide visqueux emplissant l’espace](https://doi.org/10.1007/BF02547763), Acta Mathematica 63 (1934), 193–248.
- G. Prodi, [Un teorema di unicità per le equazioni di Navier–Stokes](https://doi.org/10.1007/BF02410664), 1959.
- J. Serrin, [On the interior regularity of weak solutions of the Navier–Stokes equations](https://doi.org/10.1007/BF00253344), 1962.
- H. Fujita, T. Kato, [On the Navier–Stokes initial value problem. I](https://doi.org/10.1007/BF00276188), 1964.
- T. Kato, [Strong \(L^p\)-solutions of the Navier–Stokes equation in \(\mathbb R^m\), with applications to weak solutions](https://doi.org/10.1007/BF01174182), 1984.
- H. Jia, V. Šverák, [Are the incompressible 3D Navier–Stokes equations locally ill-posed in the natural energy space?](https://arxiv.org/abs/1306.2136), JFA 268 (2015), 3734–3766.
- T. Y. Hou, Y. Wang, C. Yang, [arXiv:2509.25116v2](https://arxiv.org/abs/2509.25116).
- A. D. Ionescu, H. Jia, S. Palasek, [arXiv:2606.07501v1](https://arxiv.org/abs/2606.07501).
- M. P. Coiculescu, S. Palasek, [Inventiones mathematicae 244 (2026)](https://doi.org/10.1007/s00222-025-01396-z).
- A. Cheskidov, Z. Zeng, D. Zhang, [arXiv:2503.05692v1](https://arxiv.org/abs/2503.05692).
- A. Cheskidov, M. Dai, S. Palasek, [arXiv:2511.09556v2](https://arxiv.org/abs/2511.09556).
- A. Cheskidov, H. Hou, [arXiv:2603.03666v2](https://arxiv.org/abs/2603.03666).
- S. Palasek, [arXiv:2509.18595v1](https://arxiv.org/abs/2509.18595).
- S. Liao, S. Qin, [arXiv:2602.12666v1](https://arxiv.org/abs/2602.12666).
- G. P. Galdi, F. Gazzola, [arXiv:2606.15189v3](https://arxiv.org/abs/2606.15189).

## Conclusion

La trace commune des branches forward auto-similaires est située à
\(\tau=-\infty\), donc au temps physique \(t=0\), et elle est singulière au seuil critique. À tout temps strictement positif, les branches sont lisses mais déjà différentes. L’unicité faible–forte empêche de les recoller à une même donnée lisse sans démontrer d’abord une perte de régularité de la solution forte.

Les travaux 2025–2026 ont considérablement élargi les formes de non-unicité depuis des données critiques ou même lisses, mais ils le font dans des notions de solution qui abandonnent exactement la coercivité Leray–Hopf. Aucun ne fournit le maillon HWY/IJP
\(\to\) donnée Clay lisse
\(\to\) blow-up ou multiplicité admissible.
