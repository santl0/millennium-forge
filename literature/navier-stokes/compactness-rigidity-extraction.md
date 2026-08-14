# Extraction compacité–rigidité : quatre sources primaires

Dernière vérification : 2026-08-14.

## Objet et convention d'audit

Ce document isole les maillons effectivement démontrés dans quatre sources primaires. Il ne transforme ni une prépublication en théorème accepté, ni une conséquence élémentaire calculée ici en résultat attribué aux auteurs.

Les étiquettes ont le sens suivant :

- **[SOURCE]** : énoncé ou étape explicitement présent dans la source primaire indiquée ;
- **[CALCUL]** : calcul vérifiable effectué dans cette extraction ;
- **[INFÉRENCE]** : conséquence logique explicitée ici, non revendiquée comme formulation des auteurs ;
- **[MANQUANT]** : hypothèse ou théorème qui n'est pas fourni par le maillon examiné.

Sauf indication contraire, l'équation est Navier–Stokes incompressible, non forcée, de viscosité normalisée à (1) :

\[
\partial_t u+u\cdot\nabla u-\Delta u+\nabla p=0,
\qquad \nabla\cdot u=0.
\]

La notation historique (L_{3,\infty}(Q_T)) d'Escauriaza–Seregin–Šverák signifie (L^\infty_tL^3_x), et non l'espace de Lorentz faible (L^{3,\infty}_x).

## Sources primaires et versions

1. L. Escauriaza, G. Seregin, V. Šverák, *(L_{3,\infty})-solutions of the Navier–Stokes equations and backward uniqueness*, **Russian Mathematical Surveys 58:2 (2003), 211–250**, DOI [10.1070/RM2003v058n02ABEH000609](https://doi.org/10.1070/RM2003v058n02ABEH000609), [notice et texte primaire MathNet](https://www.mathnet.ru/eng/rm609). Article publié ; reçu le 15 février 2003.
2. I. Gallagher, G. S. Koch, F. Planchon, *A profile decomposition approach to the (L^\infty_t(L^3_x)) Navier–Stokes regularity criterion*, [arXiv:1012.0145v3](https://arxiv.org/abs/1012.0145), 16 juillet 2012, version publiée dans *Mathematische Annalen* 355 (2013), DOI [10.1007/s00208-012-0830-0](https://doi.org/10.1007/s00208-012-0830-0). L'extraction suit la v3.
3. G. Koch, N. Nadirashvili, G. Seregin, V. Šverák, *Liouville theorems for the Navier–Stokes equations and applications*, [arXiv:0709.3599v1](https://arxiv.org/abs/0709.3599), 22 septembre 2007, version publiée dans *Acta Mathematica* 203 (2009), DOI [10.1007/s11511-009-0039-6](https://doi.org/10.1007/s11511-009-0039-6). L'extraction suit la v1.
4. G. Seregin, *On potential Type II blowups for the Navier–Stokes equations*, [arXiv:2606.29468v1](https://arxiv.org/abs/2606.29468), 28 juin 2026. **Prépublication arXiv v1** lors de l'audit ; aucune version publiée n'est identifiée dans les métadonnées primaires consultées.

## 1. Escauriaza–Seregin–Šverák (ESS, 2003)

### Théorèmes 1.3 et 1.4

| Champ | Extraction |
|---|---|
| Domaine et équation | **[SOURCE]** Théorème 1.3 : problème de Cauchy sur (\mathbb R^3\times(0,T)), sans force, viscosité (1). Théorème 1.4 : cylindre local (Q=B(1)\times(-1,0)), même système au sens des distributions. |
| Notion de solution | **[SOURCE]** Théorème 1.3 : solution faible de Leray–Hopf. Théorème 1.4 : paire locale distributionnelle \((v,p)\) avec \(v\in L^\infty(-1,0;L^2(B))\cap L^2(-1,0;W^{1,2}(B))\) et \(p\in L^{3/2}(Q)\). L'énoncé du théorème 1.4 ne pose pas séparément l'inégalité d'énergie locale comme hypothèse ; la preuve de blow-up emploie la structure locale adaptée. |
| Borne critique | **[SOURCE]** (v\in L^\infty(0,T;L^3(\mathbb R^3))) dans le théorème global ; (\|v\|_{L^\infty_tL^3_x(Q)}<\infty) dans le théorème local. Cette norme est invariante sous (v_\lambda(x,t)=\lambda v(\lambda x,\lambda^2t)). |
| Conclusion | **[SOURCE]** Théorème 1.3 : (v\in L^5(Q_T)), puis lissité et unicité. Théorème 1.4 : Hölder-régularité dans (\overline{Q(1/2)}). Équivalent contraposé pour une solution classique maximale : un temps singulier fini force (\limsup_{t\uparrow T_*}\|v(t)\|_3=\infty). |

### Normalisation, compacité et pression dans la preuve locale

Sous l'hypothèse contradictoire qu'un point (z_0=(x_0,t_0)) est singulier, les auteurs choisissent (R_k\downarrow0) et utilisent la remise à l'échelle Navier–Stokes

\[
v^{(k)}(x,t)=R_kv(x_0+R_kx,t_0+R_k^2t),\qquad
p^{(k)}(x,t)=R_k^2p(x_0+R_kx,t_0+R_k^2t).
\]

- **[SOURCE] Convergence de la vitesse.** Après extraction,
  (v^{(k)}\rightharpoonup^*u) dans (L^\infty(\mathbb R;L^3(\mathbb R^3))),
  (v^{(k)}\to u) fortement dans (L^3(Q')) pour tout cylindre compact (Q'\Subset\mathbb R^3\times\mathbb R), et
  (v^{(k)}\to u) dans (C([a,b];L^2(\Omega))) pour (\Omega\Subset\mathbb R^3).
- **[SOURCE] Pression.** La pression locale est scindée en une partie (p_1), contrôlée globalement par le terme quadratique, et une partie (p_2), harmonique en espace dans la région intérieure. Les remises à l'échelle vérifient
  (p_1^{(k)}\rightharpoonup^*q) dans (L^\infty(\mathbb R;L^{3/2}(\mathbb R^3))), tandis que
  (p_2^{(k)}\to0) dans (L^{3/2}(\mathbb R;L^\infty(\Omega))) pour tout (\Omega\Subset\mathbb R^3).
- **[SOURCE] Non-trivialité.** L'epsilon-régularité et le choix des rayons donnent, pour une constante universelle (\varepsilon_*>0),
  \[
  \sup_{-1\le t\le0}\int_{B(1)}|u(x,t)|^2\,dx>\varepsilon_*.
  \]
- **[SOURCE] Trace terminale.** La continuité forte locale en (L^2), combinée à l'intégrabilité (L^3) de la solution originale, donne (u(\cdot,0)=0) localement, donc partout.
- **[SOURCE] Rigidité.** La petitesse des queues spatiales de (u\in L^3) et (q\in L^{3/2}) donne la régularité hors d'une grande boule. La vorticité satisfait à l'extérieur une inégalité parabolique permettant l'unicité rétrograde ; elle y est nulle parce que sa trace terminale est nulle. Une continuation unique spatiale propage ensuite (\omega=0) à tout l'espace. Comme (u(\cdot,t)) est alors harmonique et appartient à (L^3(\mathbb R^3)), (u=0), contradiction avec la non-trivialité.

**[MANQUANT pour le problème Clay]** L'estimation énergétique de Leray–Hopf ne donne pas (L^\infty_tL^3_x). ESS ferme complètement la chaîne *si* cette borne critique est disponible ; il ne la produit pas à partir de (L^2_x). La preuve est sur (\mathbb R^3), sans frontière et sans force ; tout transfert à un autre domaine demande un raccord distinct pour la pression, l'unicité rétrograde et les bords.

## 2. Gallagher–Koch–Planchon (GKP, arXiv:1012.0145v3)

### Décomposition de profils : théorèmes 1 et 3

| Champ | Extraction |
|---|---|
| Domaine et solution | **[SOURCE]** (\mathbb R^d), (d\ge3), solutions fortes/mild du problème de Cauchy, obtenues avec le semi-groupe de chaleur et la projection de Leray. L'application de rigidité est en (d=3), données divergence-free dans (L^3). |
| Quantité critique | **[SOURCE]** (L^d(\mathbb R^d)), ainsi que les espaces homogènes (\dot B^{d/p-1}_{p,q}). La transformation (\Lambda_{j,n}f(x)=\lambda_{j,n}^{-1}f((x-x_{j,n})/\lambda_{j,n})) conserve la norme (L^d). |
| Compacité des données | **[SOURCE]** Théorème 1 : une suite bornée de (L^d) est somme d'une limite faible, de profils translatés-dilatés à paramètres orthogonaux et d'un reste tendant vers zéro dans un espace de Besov critique plus faible. Les cubes des normes (L^3) des profils sont asymptotiquement découplés dans l'application tridimensionnelle. |
| Évolution non linéaire | **[SOURCE]** Théorème 3 : les profils sont évolués par Navier–Stokes ; le reste linéaire et le reste non linéaire sont petits dans les espaces critiques de résolution, sous les restrictions d'indices du théorème. Il s'agit d'une décomposition modulo translations et dilatations, non d'une convergence forte globale en (L^3). |
| Pression | **[SOURCE]** Elle n'est pas une variable indépendante de la formulation mild : la projection de Leray est incluse dans le terme bilinéaire de Duhamel. **[INFÉRENCE]** Le théorème de profils ne fournit donc pas, à lui seul, une topologie globale séparée pour une suite de pressions ; la pression réapparaît dans l'étape de rigidité locale reprise d'ESS. |

### Chaîne critique : théorèmes 4 à 7

| Théorème | Hypothèses et conclusion | Normalisation / topologie | Non-trivialité et rigidité | Hypothèse exacte non fournie |
|---|---|---|---|---|
| Th. 4, endpoint (L^3) | **[SOURCE]** Pour (u_0\in L^3(\mathbb R^3)), si (\sup_{0\le t<T^*(u_0)}\|NS(u_0)(t)\|_3<\infty), alors (T^*(u_0)=\infty). | Solution forte/mild maximale, sans frontière ni force. | Conclusion finale de la chaîne Th. 5–7. | La borne (L^\infty_tL^3_x) ne découle pas de l'énergie. |
| Th. 5, élément critique | **[SOURCE]** Supposer le seuil (A_c<\infty) et une suite de données de blow-up (u_{0,n}), avec (A_n=\sup_t\|NS(u_{0,n})(t)\|_3\to A_c). Un profil (U_{j_0}) a (T^*<\infty) et norme maximale exactement (A_c). | Décomposition des (u_{0,n}) par (\lambda_{j,n},x_{j,n}), puis évolution non linéaire. | La non-trivialité est (T^*(U_{j_0})<\infty) et (\sup_t\|U_{j_0}(t)\|_3=A_c>0), pas une normalisation ponctuelle. | Sans hypothèse contradictoire (A_c<\infty), aucun élément critique singulier n'est construit. |
| Th. 6, « compacité » | **[SOURCE]** Un élément critique fini vérifie (u(t)\to0) dans (\mathcal S'(\mathbb R^3)) quand (t\uparrow T^*). | Les tranches (u(s_n)) sont redécomposées ; le profil de blow-up est isolé à une échelle (\lambda_{0,n}\to0). La conclusion du théorème est une convergence distributionnelle, pas la précompacité forte de toute l'orbite en (L^3). La remarque 3.5 ne donne qu'une sous-suite de temps, compacte modulo symétries dans un Besov critique. | La minimalité (A_c) interdit plusieurs profils singuliers et force la limite faible à échelle fixe à être nulle. | Une précompacité globale de l'orbite critique en (L^3) ne doit pas être ajoutée à l'énoncé. |
| Th. 7, rigidité | **[SOURCE]** Si une solution forte/mild est bornée dans (L^\infty_tL^3_x) jusqu'à un (T^*<\infty) et tend vers zéro dans (\mathcal S'), alors en fait (T^*=\infty). | Localisation, régularité hors d'une boule, trace terminale nulle et argument ESS d'unicité rétrograde/continuation unique. | Le prétendu élément critique fini est éliminé ; donc (A_c=\infty). | Le théorème n'élimine pas un blow-up dont la norme (L^3) diverge. |

**[MANQUANT pour le problème Clay]** Le raccord bloquant est toujours

\[
u_0\in C_c^\infty,\quad \nabla\cdot u_0=0
\quad\Longrightarrow?\quad
\sup_{t<T^*}\|u(t)\|_3<\infty.
\]

GKP montre que ce seul contrôle exclurait le blow-up, mais ni la décomposition de profils ni la minimalité ne le déduisent de l'énergie. Il serait circulaire d'annoncer un « blow-up minimal (L^3) » sans conserver l'hypothèse contradictoire (A_c<\infty).

## 3. Koch–Nadirashvili–Seregin–Šverák (KNSS, arXiv:0709.3599v1)

### Définitions et compacité, lemme 6.1

- **[SOURCE] Domaine.** (\mathbb R^n\times(-\infty,0)), principalement (n=2,3), équation sans force de viscosité (1).
- **[SOURCE] Solution ancienne faible.** Solution testée seulement contre des champs divergence-free ; cette notion autorise les solutions parasites (u(x,t)=b(t)), avec pression linéaire en (x).
- **[SOURCE] Solution ancienne mild.** Pour une suite (T_ell\downarrow-\infty), la solution satisfait sur chaque ((T_ell,0)) la formule intégrale de Stokes/Navier–Stokes. Cette notion élimine les (b(t)) non constants ; une solution mild de la forme (b(t)) est constante.
- **[SOURCE] Lemme 6.1.** Des solutions mild (u_ell) sur (\mathbb R^n\times(T_ell,0)), uniformément bornées ponctuellement et avec (T_ell\downarrow-\infty), admettent une sous-suite convergeant **localement uniformément** vers une solution ancienne mild, avec la même borne.
- **[SOURCE] Pression.** La formule mild emploie le noyau de Stokes et la projection de Helmholtz ; la pression n'intervient pas explicitement et n'est définie qu'à une fonction du temps près pour une donnée bornée. **[INFÉRENCE]** Le lemme 6.1 ne revendique donc aucune convergence normalisée d'une pression globale.

### Proposition 6.1 : zoom (L^\infty)

Soit une solution mild sur son intervalle maximal ((0,T)), avec (T<\infty). Les auteurs posent

\[
h(t)=\sup_x|u(x,t)|,\qquad H(t)=\sup_{0\le s\le t}h(s),
\]

choisissent des temps records (t_k\uparrow T), (N_k=H(t_k)), des (\gamma_k\downarrow1), et des points (x_k) tels que

\[
M_k=|u(x_k,t_k)|\ge N_k/\gamma_k.
\]

La normalisation est

\[
v^{(k)}(y,s)=M_k^{-1}u\!\left(x_k+M_k^{-1}y,
t_k+M_k^{-2}s\right).
\]

Elle est définie sur (\mathbb R^n\times(A_k,B_k)), avec (A_k=-M_k^2t_k\to-\infty), et vérifie pour (s\le0)

\[
|v^{(k)}|\le\gamma_k,\qquad |v^{(k)}(0,0)|=1.
\]

Par le lemme 6.1, une sous-suite converge localement uniformément vers une solution ancienne mild (v) telle que

\[
|v|\le1,qquad |v(0,0)|=1.
\]

C'est la non-trivialité ponctuelle exacte de la proposition 6.1 : tout blow-up mild en temps fini produit une solution ancienne mild bornée non nulle.

### Théorèmes de rigidité disponibles

| Théorème | Classe | Conclusion | Limite exacte |
|---|---|---|---|
| Th. 5.1 | **[SOURCE]** Solution ancienne faible bornée sur (\mathbb R^2\times(-\infty,0)). | (u(x,t)=b(t)) ; si elle est mild, (b) est constant. | Dimension (2), pas le problème tridimensionnel. |
| Th. 5.2 | **[SOURCE]** Solution ancienne faible bornée, axisymétrique sans swirl, sur (\mathbb R^3\times(-\infty,0)). | (u=(0,0,b_3(t))) ; mild implique constante. | Symétrie et absence de swirl essentielles. |
| Th. 5.3 | **[SOURCE]** Solution ancienne faible bornée, axisymétrique, avec ( |u(x,t)|\le C/r), (r=(x_1^2+x_2^2)^{1/2}). | (u=0). | Hypothèses axisymétrique et (C/r), invariantes d'échelle, non disponibles en général. |
| Th. 6.1 | **[SOURCE]** Solution faible axisymétrique sur (\mathbb R^3\times(0,T)), localement bornée avant (T), avec ( |u|\le C/r). | Borne uniforme (M(C)), solution mild et lisse. | Le zoom conserve l'axisymétrie et (C/r), puis Th. 5.3 contredit ( |v(0,0)|=1). |

**[MANQUANT pour le problème Clay]** Il faudrait un théorème de Liouville tridimensionnel excluant toute solution ancienne mild bornée non constante dans une classe qui contient les limites de blow-up, plus une propriété empêchant la limite d'être une constante non nulle. KNSS dit explicitement que le cas tridimensionnel général est ouvert, même stationnaire. Un théorème seulement axisymétrique, sans swirl ou sous (C/r), ne se transfère pas aux données Clay générales.

## 4. Seregin (arXiv:2606.29468v1, 2026)

### Cadre local et définition propre de Type I/II

- **[SOURCE] Domaine et solution.** (Q=B(1)\times(-1,0)). Paire faible adaptée (v,q) avec (v\in L^\infty_tL^2_x), (\nabla v\in L^2(Q)), (q\in L^{3/2}(Q)), équation Navier–Stokes de viscosité (1) au sens des distributions et inégalité d'énergie locale.
- **[SOURCE] Quantités invariantes Navier–Stokes.** Pour (Q(r)=B(r)\times(-r^2,0)),
  \[
  A(v,r)=\sup_{-r^2<t<0}\frac1r\int_{B(r)}|v|^2,
  \quad E(v,r)=\frac1r\int_{Q(r)}|\nabla v|^2,
  \quad C(v,r)=\frac1{r^2}\int_{Q(r)}|v|^3.
  \]
- **[SOURCE] Terminologie de l'article.** (g_0(v)=\min\{\liminf A,\liminf E,\liminf C\}). Un point singulier est appelé Type I si (g_0(v)<\infty), Type II si (g_0(v)=\infty). Cette définition locale propre à l'article ne doit pas être confondue sans preuve avec toutes les notions de Type I/II basées sur un taux (L^\infty).
- **[SOURCE] Scénario conditionnel.** Pour (s,l>1),
  \[
  M^{s,l}_\kappa(v,r)=r^{-\kappa}\int_{-r^2}^0
  \left(\int_{B(r)}|v|^s\right)^{l/s}dt,
  \qquad l>\kappa=l\left(\frac3s+\frac2l-1\right)>0,
  \]
  et une suite (r_k\downarrow0) vérifie (g(r_k)\to0) mais
  (g(r_k)M^{s,l}_\kappa(v,r_k)\ge\varepsilon_0).
- **[SOURCE] Contrôle pondéré par \(f\), pas par \(|y|^{-4}\).** L'hypothèse (1.7) est
  \[
  \sup_{0<r<1}\{A_f(v,r)+E_f(v,r)+D_f(q,r)\}<\infty,
  \]
  avec (A_f=f(r)^2A), (E_f=f(r)E), (D_f=f(r)^2r^{-2}\int_{Q(r)}|q|^{3/2}), où (f(r)\downarrow0) quand (r\downarrow0).

### Théorème 2.1 : exclusion quantitative d'un scénario

**[SOURCE]** Si (1.7) tient, si (s<p(\eta)), (l<q(\eta)), et si la relation asymptotique (2.4) entre (f) et (g) diverge comme demandé, alors

\[
g(r)M^{s,l}_\kappa(v,r)\longrightarrow0.
\]

Le scénario de non-vanishing (1.3) est donc impossible. C'est une exclusion conditionnelle d'une classe de scénarios, pas une régularité de toute solution adaptée.

Le zoom employé est

\[
v^\lambda(y,\tau)=\lambda f(\lambda)v(\lambda y,\lambda^2f(\lambda)\tau),
\quad
q^\lambda(y,\tau)=\lambda^2f(\lambda)^2q(\lambda y,\lambda^2f(\lambda)\tau),
\]

avec (r_k=\lambda_k\sqrt{f(\lambda_k)}) dans la preuve du théorème 2.1.

- **[CALCUL] Équation remise à l'échelle.** Une substitution directe donne
  \[
  \partial_\tau v^\lambda+v^\lambda\cdot\nabla v^\lambda
  -f(\lambda)\Delta v^\lambda+\nabla q^\lambda=0.
  \]
  Comme (f(\lambda)\to0), la limite est Euler, non Navier–Stokes.
- **[SOURCE] Topologies.** Pour tout (a>0) et (1\le\nu<10/9), après extraction :
  \[
  v^{\lambda_k}\to u\text{ dans }L^{3\nu}(Q(a)),\quad
  v^{\lambda_k}\rightharpoonup^*u\text{ dans }L^\infty_tL^2_x(Q(a)),\quad
  \nabla v^{\lambda_k}\rightharpoonup\nabla u\text{ dans }L^2(Q(a)).
  \]
- **[SOURCE] Pression.** Les (D_{F_{\lambda_k}}(q^{\lambda_k},a)) sont uniformément contrôlés et le couple limite est noté (u,p), avec (D_F(p,a)) fini. **[LIMITE DE L'ÉNONCÉ]** La liste de convergences affichée dans la preuve ne donne pas une topologie séparée explicite pour (q^{\lambda_k}\to p) ; il ne faut pas en inventer une.

### Théorème 3.1 : limite ancienne d'Euler

Le signal de non-trivialité est remplacé par

\[
g(r_k)\overline M^{s,l}_\kappa(v,r_k)\ge\varepsilon_0,
\qquad
\overline M^{s,l}_\kappa(v,r)=r^{-\kappa}
\int_{-r^2f(r)}^0\left(\int_{B(r)}|v|^s\right)^{l/s}dt,
\]

avec (g(r)=f(r)^{l-1}) et la condition nécessaire (3.3). Ici la preuve prend (\lambda_k=r_k).

**[SOURCE]** Il existe alors sur (Q_-=\mathbb R^3\times(-\infty,0)) une paire (u,p) telle que :

1. (\sup_{a>0}\{A_F(u,a)+E_F(u,a)+D_F(p,a)\}<\infty) ;
2. (\partial_\tau u+u\cdot\nabla u+\nabla p=0), (\nabla\cdot u=0), au sens des distributions ;
3. la paire satisfait l'inégalité locale d'énergie **inviscide** (3.7) ;
4. (M^{s,l}_\kappa(u,1)\ge\varepsilon_0/2), donc (u\not\equiv0).

**[SOURCE] Rigidité partielle.** Pour l'exemple (f(\lambda)=\lambda^{\alpha-1}/\log^\gamma(e/\lambda)), on a (F(a)=a^{\alpha-1}). Si (2\alpha-3>0), la borne énergétique pondérée (3.5) force (u=0), en contradiction avec (3.8), et le scénario est exclu.

**[MANQUANT pour le problème Clay]** Deux raccords distincts manquent :

1. les hypothèses (1.7), (3.1) et (3.3) ne sont pas démontrées pour tout blow-up Clay hypothétique ; elles sélectionnent un scénario ;
2. dans le régime non éliminé, il faudrait un théorème de Liouville pour les **paires anciennes dissipatives d'Euler** satisfaisant exactement (3.5), (3.7) et (3.8). Un théorème de rigidité pour les solutions anciennes de Navier–Stokes ne suffit pas, puisque la viscosité du zoom vaut (f(\lambda_k)\to0).

## 5. Tension pondérée (\int_{|y|>A}|U_n|^2|y|^{-4}dy)

### Ce que disent les sources

- **[SOURCE/NÉGATIF TEXTUEL]** La chaîne de caractères correspondant à cette intégrale ou au poids ( |y|^{-4}) n'a pas été trouvée dans les versions HTML primaires des trois prépublications arXiv inspectées (GKP, KNSS, Seregin 2026).
- **[AUDIT LIMITÉ]** Elle n'a pas été repérée dans les passages pertinents du texte primaire ESS consultés sur MathNet. Cela documente la recherche effectuée, mais ne prétend pas prouver l'absence de toute notation équivalente dans chaque ligne du PDF.
- Le « poids » (f(r)) de Seregin porte sur les fonctionnelles d'échelle (A_f,E_f,D_f) ; ce n'est pas le poids spatial ( |y|^{-4}).

### Conséquence exacte d'une borne globale (L^3)

Soit (U_n\in L^3(\mathbb R^3)) et (A>0). Par Hölder avec exposants (3/2) et (3),

\[
\begin{aligned}
\int_{|y|>A}|U_n(y)|^2|y|^{-4}\,dy
&\le
\left(\int_{|y|>A}|U_n|^3dy\right)^{2/3}
\left(\int_{|y|>A}|y|^{-12}dy\right)^{1/3}\\
&=
\left(\frac{4\pi}{9}\right)^{1/3}A^{-3}
\|U_n\|_{L^3(|y|>A)}^2\\
&\le
\left(\frac{4\pi}{9}\right)^{1/3}A^{-3}
\|U_n\|_{L^3(\mathbb R^3)}^2.
\end{aligned}
\]

Par conséquent,

\[
\sup_n\|U_n\|_3\le M
\quad\Longrightarrow\quad
\sup_n\int_{|y|>A}|U_n|^2|y|^{-4}dy
\le \left(\frac{4\pi}{9}\right)^{1/3}M^2A^{-3}
\xrightarrow[A\to\infty]{}0.
\]

Cette implication est **[CALCUL]**, pas un lemme attribué aux quatre articles. Elle ne requiert aucune compacité, aucune convergence de (U_n), ni aucune tension uniforme non pondérée des queues (L^3). Elle reste vraie pour une suite translatée ou dilatée, car seul intervient le majorant global uniforme de la norme (L^3).

### Ce que la borne ne donne pas

- Elle ne donne pas la précompacité forte de (U_n) dans (L^3) ou (L^2_{\mathrm{loc}}).
- Elle ne contrôle pas à elle seule une pression : la projection de Leray et les transformées de Riesz restent non locales.
- Elle ne suit pas de simples bornes (L^3_{\mathrm{loc}}) uniformes. **[CALCUL adverse]** Si (\phi\in C_c^\infty(\mathbb R^3;\mathbb R^3)) est divergence-free et non nulle, (e_1=(1,0,0)), et
  \[
  U_n(y)=n^2\phi(y-ne_1),
  \]
  alors (U_n\to0) sur tout compact, mais pour tout (A) fixé et (n\) assez grand,
  \[
  \int_{|y|>A}|U_n(y)|^2|y|^{-4}dy
  \longrightarrow \|\phi\|_2^2
  \]
  à un facteur géométrique tendant vers (1) près, tandis que (\|U_n\|_3=n^2\|\phi\|_3\to\infty). Les contrôles locaux seuls ne remplacent donc pas la borne globale (L^3).
- La quantité pondérée n'est pas critique : pour (U_\lambda(y)=\lambda U(\lambda y)),
  \[
  \int |U_\lambda(y)|^2|y|^{-4}dy
  =\lambda^3\int |U(x)|^2|x|^{-4}dx.
  \]
  Elle est une queue utile dans des coordonnées déjà normalisées, pas une nouvelle quantité critique de Navier–Stokes.

## 6. Graphe logique consolidé et verrou transférable

\[
\begin{array}{c}
\text{blow-up fini}\\
\downarrow\\
\text{normalisation critique ou par le maximum}\\
\downarrow\\
\text{limite ancienne non triviale}\\
\downarrow\\
\text{théorème de rigidité dans la classe limite}\\
\downarrow\\
\bot
\end{array}
\]

Les quatre sources remplissent des arêtes différentes :

| Chaîne | Limite | Non-trivialité | Rigidité disponible | Verrou restant |
|---|---|---|---|---|
| ESS | Navier–Stokes adapté, ancien/local-global, (L^\infty_tL^3_x) | énergie locale (>\varepsilon_*) | unicité rétrograde + continuation unique | obtenir (L^\infty_tL^3_x) depuis les données/énergie Clay |
| GKP | élément critique mild et profils (L^3) | (T^*<\infty), niveau (A_c) | ESS après convergence vers (0) dans (\mathcal S') | même borne critique (L^3), non fournie par l'énergie |
| KNSS | Navier–Stokes ancien mild borné | ( |v(0,0)|=1) | seulement 2D ou 3D axisymétrique sous hypothèses supplémentaires | Liouville 3D général + exclusion des constantes |
| Seregin 2026 | Euler ancien dissipatif pondéré | (M^{s,l}_\kappa(u,1)\ge\varepsilon_0/2) | seulement sous certains poids/cas | Liouville Euler dans la classe exacte et raccord de tout blow-up au scénario |

**Lemme transférable minimal, déjà fermé.** Pour toute suite globalement bornée dans (L^3(\mathbb R^3)), la queue pondérée (L^2(|y|^{-4}dy)) est uniformément (O(A^{-3})). Elle ne constitue donc pas une hypothèse supplémentaire dans les chaînes ESS/GKP si le contrôle (L^3) global est conservé.

**Verrou scientifique exact.** Cette observation n'aide pas le régime général de l'énergie ni le zoom Type II de Seregin, où aucune borne globale (L^3) uniforme des profils n'est fournie. Toute stratégie qui utilise cette queue doit donc exhiber d'abord, sans circularité, soit une borne globale (L^3), soit une estimation pondérée indépendante stable sous la limite et compatible avec le contrôle non local de la pression.

## 7. Audit des traces temporelles — cycle 0005

### Classe énergétique classique

**[SOURCE]** Foias–Rosa–Temam 2013, définition 2.1 et lemme 2.4, placent les
solutions Leray–Hopf dans le triplet `V subset H subset V'` avec

```text
u in L^infinity(0,T;H) intersection L²(0,T;V),
partial_t u in L^(4/3)(0,T;V'),
u in C([0,T];H_weak).
```

Pour chaque solution fixée, l'inégalité d'énergie et la trace faible donnent
la continuité forte en `H=L²_sigma` à l'instant initial. Ce résultat est
individuel : il ne contient pas de taux uniforme pour une famille dont les
données parcourent seulement une boule bornée de `H`.

**[CALCUL]** Dans le cas périodique de moyenne nulle, `V'` s'identifie au
`dot H^-1` solénoïdal. L'équation projetée et Gagliardo–Nirenberg donnent le
module explicite du claim `NS-ENERGY-HMINUS1-TIME-MODULUS`. Son exposant
temporel `1/4` n'est pas critique dans `dot H^-1`; le seuil d'échelle serait
`3/4`.

### Raccord positif pour des données précompactes

**[CALCUL]** Posons `H=L²_sigma(T³)`, `V=H¹_sigma(T³)` et notons `V'` son dual.
Soit une famille de solutions non forcées, de moyenne nulle, dont le
représentant satisfait l'inégalité d'énergie depuis `0`, avec `u_n(0)` dans un
ensemble relativement compact de `H`; on note `K` sa clôture compacte. Supposons
un module uniforme `omega(t)` dans `V'` pour `t in [0,T]`. Pour le projecteur
orthogonal solénoïdal de Fourier de rang fini `P_m:H->V`, l'énergie donne

```text
||u_n(t)-u_n(0)||_H²
 <=2 <u_n(0)-u_n(t),u_n(0)>.
```

En écrivant `u_n(0)=P_m u_n(0)+(I-P_m)u_n(0)`, on obtient

```text
||u_n(t)-u_n(0)||_H²
 <=2 omega(t) sup_(v in K)||P_m v||_V
   +4 sup_(v in K)||v||_H sup_(v in K)||(I-P_m)v||_H.
```

La compacité de `K` rend le dernier supremum arbitrairement petit pour `m`
grand; à `m` fixé, `omega(t)->0` ferme le premier terme. Donc

```text
sup_n ||u_n(t)-u_n(0)||_2 ->0 quand t->0+.
```

La famille adverse du cycle 0004 ne contredit pas ce lemme : ses données
initiales convergent seulement faiblement vers zéro et gardent une norme
`L²` non nulle, donc elles ne sont pas fortement précompactes.

### Mécanismes ESS et GKP

**[SOURCE]** Dans ESS, la convergence forte locale des zooms sur des cylindres
intérieurs utilise les estimations renforcées de dérivée temporelle, dérivées
spatiales secondes et pression localisée; la nullité de la trace terminale
emploie en plus l'absolue continuité de l'intégrale `L³` sur des boules qui se
rétrécissent. Elle n'est donc pas produite par l'énergie seule.

**[SOURCE]** Dans GKP, les objets sont mild/forts dans `L³`, puis décomposés en
profils critiques. La convergence vers zéro au temps critique est dans
`S'`; elle ne constitue pas un module fort uniforme pour des tranches de
familles énergétiques changeantes.

**Conclusion de raccord.** La vraie alternative n'est pas « continuité ou
absence de continuité » : la continuité forte individuelle est classique. Le
verrou est la précompacité forte uniforme des tranches rescalées. ESS/GKP
l'obtiennent seulement sous la structure critique qui nourrit déjà leur
argument de rigidité; l'énergie générale ne la fournit pas.
