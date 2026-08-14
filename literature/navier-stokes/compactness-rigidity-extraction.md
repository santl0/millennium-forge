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

- **[SOURCE] Domaine limite.** La paire limite est construite sur
  `(R³ x R)`; elle est donc éternelle. Sa restriction à `t<0` est une solution
  ancienne, mais ce vocabulaire ne doit pas masquer l'information plus forte.
- **[SOURCE] Convergence de la vitesse.** Après extraction,
  (v^{(k)}\rightharpoonup^*u) dans (L^\infty(\mathbb R;L^3(\mathbb R^3))),
  (v^{(k)}\to u) fortement dans (L^3(Q')) pour tout cylindre compact (Q'\Subset\mathbb R^3\times\mathbb R), et
  (v^{(k)}\to u) dans (C([a,b];L^2(\Omega))) pour (\Omega\Subset\mathbb R^3).
- **[SOURCE] Pression.** La pression locale est scindée en une partie (p_1), contrôlée globalement par le terme quadratique, et une partie (p_2), harmonique en espace dans la région intérieure. Les remises à l'échelle vérifient
  (p_1^{(k)}\rightharpoonup^*q) dans (L^\infty(\mathbb R;L^{3/2}(\mathbb R^3))), tandis que
  (p_2^{(k)}\to0) dans (L^{3/2}(\mathbb R;L^\infty(\Omega))) pour tout (\Omega\Subset\mathbb R^3).
- **[SOURCE] Non-trivialité.** L'epsilon-régularité et le choix des rayons donnent, pour une constante universelle (\varepsilon_*>0),
  \[
  \sup_{-1\le t\le0}\int_{B(1)}|u(x,t)|^2\,dx\ge\varepsilon_*.
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
| ESS | Navier–Stokes adapté, éternel puis restreint aux temps anciens, (L^\infty_tL^3_x) | énergie locale (\ge\varepsilon_*) | unicité rétrograde + continuation unique | obtenir (L^\infty_tL^3_x) depuis les données/énergie Clay |
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

## 8. Porte de pression pour les solutions anciennes — cycle 0006

### Distinction KNSS entre faible et mild

**[SOURCE]** KNSS signale dès l'introduction les solutions parasites

```text
u(x,t)=b(t),
p(x,t)=-b'(t) dot x,
```

et choisit la notion mild pour les éliminer. Le théorème 5.1 montre en 2D
qu'une solution ancienne faible bornée est de la forme `b(t)`; la remarque 6.1
ajoute qu'une solution ancienne mild de cette forme est constante. Dans la
construction par blow-up de la section 6, les limites pertinentes sont
explicitement anciennes et mild, et leur non-trivialité est normalisée par une
valeur ponctuelle telle que `|v(0,0)|=1`.

La définition littérale d'une ancienne mild demande une suite
`T_l->-infinity` telle que la formule intégrale de Stokes vaille sur chaque
`(T_l,0)`. Elle implique donc la formule entre deux temps finis situés dans un
même intervalle. Pour une solution faible `u=b(t)` avec `b` seulement
mesurable, la pression `-b'(t) dot x` est distributionnelle; le contre-profil
du laboratoire choisit `b in C^infinity` et possède une pression classique.

**[SOURCE]** Le papier ne démontre pas que toute solution ancienne mild bornée
3D est constante. Il obtient des résultats partiels, notamment dans des cadres
axisymétriques. Remplacer « mild » par « faible », « adaptée » ou simplement
« lisse » agrandit réellement la classe et invalide une étape de Liouville.

### Contre-profil exact avec trace terminale nulle

**[CALCUL]** Avec

```text
b(t)=(-t/(1+t²))e_1,
p(x,t)=((1-t²)/(1+t²)²)x_1,
```

on obtient sur `R³ x (-infinity,0]` une solution classique non forcée,
divergence-free, à vitesse bornée par `1/2`, localement adaptée et satisfaisant l'égalité
d'énergie locale. Elle vérifie pourtant

```text
u(·,0)=0,
u(·,-1)=(1/2)e_1.
```

Le défaut n'est ni visqueux ni convectif : il est entièrement porté par la
partie affine harmonique de la pression. L'équation de Poisson ne la voit pas,
car ses deux membres sont nuls.

### Lemme minimal de fermeture

Soit une solution spatialement constante `u=b(t)` avec `b in C¹`. L'équation
implique

```text
p(x,t)=-b'(t) dot x+c(t).
```

Chacune des hypothèses suivantes force `b'=0` :

- formule mild sur tous les sous-intervalles compacts;
- pression `p(·,t)` dans `BMO(R³)` modulo les constantes temporelles;
- normalisation Leray/Riesz excluant toute composante harmonique affine.

Pour la première, le semi-groupe de chaleur conserve les constantes et le terme
de Duhamel est nul. Pour la seconde, l'oscillation moyenne d'une fonction affine
sur `[-R,R]³` croît comme `R`. Une trace terminale nulle force alors `b=0`.

**Portée.** Ce lemme ne prouve aucun Liouville 3D général. Il fixe le premier
quantificateur : toute classe limite de blow-up doit transporter une propriété
mild ou une jauge de pression assez forte. La seule adaptation locale, même
avec bornitude et trace terminale nulle, ne suffit pas.

La porte `BMO`/Riesz et la vérification d'adaptation locale sont des
**[CALCULS]** propres au cycle, non des énoncés attribués à KNSS. De même, la
préservation de mildness en section 6 vient de la structure mild des
approximants; elle ne s'étend pas automatiquement à une extraction arbitraire
de solutions seulement faibles ou adaptées.

## 9. Matrice d'héritage et interdiction de composition — cycle 0007

### Sorties de chaque chaîne

| Propriété | ESS 2003 | GKP v3 | KNSS v1 | Seregin `2606.29468v1` |
|---|---|---|---|---|
| objet temporel | **[SOURCE]** paire éternelle sur `R³ x R`, ancienne par restriction | **[SOURCE]** élément critique forward sur `[0,T*)`; pas d'ancienne | **[SOURCE]** ancienne sur `(-infinity,0)` | **[SOURCE]** ancienne sur `(-infinity,0)` |
| équation obtenue après passage à la limite | NS visqueux, `nu=1` | NS visqueux, `nu=1` | NS visqueux, `nu=1` | Euler, viscosité limite nulle |
| notion de solution | paire adaptée; égalité locale d'énergie dans la construction | forte/mild `L³` à temps strictement antérieur à `T*` | ancienne mild bornée | paire Euler dissipative pondérée |
| convergence principale | faible-* `L∞_tL³_x`, forte `L³_loc` et `C_tL²_loc` | profils faibles, restes Besov; pas une convergence ancienne unique | localement uniforme | forte locale `L^(3 nu)` pour `nu<10/9`, plus convergences faibles énergétiques |
| borne globale transmise | `L∞_tL³_x` | niveau critique `L∞_tL³_x=A_c` | `|v|<=1` | fonctionnelles locales pondérées |
| trace terminale | **[SOURCE]** zéro fortement dans `L²_loc` | **[SOURCE]** zéro dans `S'` seulement | **[SOURCE]** normalisation opposée `|v(0,0)|=1` | non fournie |
| non-trivialité | **[SOURCE]** énergie locale `>=epsilon_*` | `T*<infinity`, `A_c>0` | `|v(0,0)|=1` | fonctionnelle locale `>=epsilon_0/2` |
| pression | scission convergente `p_1+p_2`, avec partie harmonique locale évanescente | aucune topologie séparée transmise par les théorèmes de profils | aucune suite de pressions suivie par le lemme 6.1 | pression limite et borne pondérée, sans topologie séparée affichée dans l'étape auditée |
| rigidité effectivement fermée | oui, sous `L∞_tL³_x`, par rétro-unicité et continuation unique | oui, théorème 7, toujours sous la borne critique | non en 3D générale; sous-classes seulement | sous-cas pondérés/autosimilaires seulement |

La ligne ESS corrige deux imprécisions d'une version antérieure de l'audit : la
limite est **éternelle**, et l'équation (3.28) donne `>=epsilon_*`, non une
inégalité stricte. La ligne KNSS sépare désormais deux faits : la formule mild
élimine le mode affine parasite, mais aucun champ de pression ni aucune
convergence de pression n'est transmis par le lemme 6.1.

### Lemme de raccord logique

**[CALCUL]** Soit `H` l'ensemble des prémisses d'un théorème de rigidité et
`Out(C)` l'ensemble des propriétés transmises par une construction `C`. Une
application sourcée exige

```text
H subset Out(C) union Bridge(C),
```

où chaque élément de `Bridge(C)` est un lemme explicite démontré sur **le même
objet limite**. La condition

```text
H subset Out(C_1) union Out(C_2)
```

ne suffit pas lorsque `C_1` et `C_2` construisent des objets distincts.

Pour le paquet

```text
H_hybrid = {
  limite NS visqueuse, ancienne, mild, globalement bornée en vitesse,
  trace L²_loc nulle, non-trivialité
},
```

aucune des quatre chaînes ne vérifie `H_hybrid subset Out(C)`. La couverture
minimale à deux chaînes est `ESS + KNSS` : ESS apporte la trace nulle; KNSS
apporte mildness et la borne ponctuelle. Mais KNSS apporte aussi
`|v(0,0)|=1`, tandis qu'ESS n'apporte aucune borne ponctuelle globale. Il ne
s'agit donc pas de deux descriptions du même profil.

### Candidat analytique séparé

**[DÉRIVATION À AUDITER, non promue]** Une ancienne mild globalement bornée au
sens KNSS qui satisfait une vraie limite `u(t)->0` dans `D'` lorsque
`t->0-` devrait être triviale : les estimations intérieures bornées donnent une
trace classique locale de la vorticité, l'unicité rétrograde donne
`curl u=0`, puis `div u=0` et la bornitude imposent `u=b(t)`; la remarque 6.1 de
KNSS et la trace imposent `b=0`.

Trois points restent à contrôler avant tout statut supérieur à spéculatif :

1. les hypothèses exactes de croissance et de régularité du théorème de
   backward uniqueness sur tout `R³`;
2. le passage uniforme de la trace distributionnelle de `u` à la trace nulle
   de `curl u`, sans seulement assigner une valeur en `t=0`;
3. l'applicabilité à une chaîne existante. La matrice montre déjà que ce
   troisième point échoue pour ESS, GKP et KNSS pris séparément.

Le fichier machine et son validateur sont dans
`experiments/navier-stokes/blowup-inheritance-audit/`. Le résultat négatif est
borné au corpus : une nouvelle construction ou un vrai lemme `Bridge(C)` peut
le falsifier.

## 10. Rigidité de la porte mild bornée à trace nulle — cycle 0008

### Énoncé fermé conditionnellement

**[DÉRIVATION DU LABORATOIRE, non promue en preuve papier]** Soit `u` une
solution ancienne mild au sens de KNSS de Navier–Stokes incompressible 3D,
non forcé, viscosité `1`, sur `R³ x (-infinity,0)`. Si

```text
M=sup_(R³ x (-infinity,0)) |u| < infinity
```

et si `u(t)->0` dans `D'(R³)` lorsque `t->0-`, alors `u=0`.

Le point nouveau de l'audit n'est pas un nouveau Carleman. Il est le raccord
de topologie entre la définition ancienne KNSS et l'unicité rétrograde ESS
appliquée à la vorticité. Le théorème publié de Lei–Yang–Yuan fournit une
seconde route au niveau de la vitesse, non nécessaire à la route sélectionnée.

### Étape A — constantes de lissage uniformes

La définition KNSS permet de redémarrer la formule mild à tout temps fini.
La proposition 4.1 de KNSS donne, depuis une donnée `L-infinity`,

```text
h^(k/2+l)||nabla^k partial_t^l u(s+h)||_infinity
  <= C_(k,l)||u(s)||_infinity
```

pour `h<=epsilon_(k,l)||u(s)||_infinity^-2`. En choisissant
`h=epsilon_(k,l)/(2M²)` et en redémarrant à `s=t-h`, on obtient pour tout
`t<0`

```text
||nabla^k partial_t^l u(t)||_infinity
  <= C'_(k,l) M^(k+2l+1).                                    (10.1)
```

La puissance est imposée par l'échelle NS : sous
`u_lambda=lambda u(lambda x,lambda²t)`, le membre de gauche porte
`lambda^(k+2l+1)`. Les constantes sont indépendantes de `t`, de la distance
au bord terminal et du temps ancien choisi.

Pour `k=0,l=1`, (10.1) donne un module global

```text
||u(t)-u(s)||_infinity <= C M³ |t-s|.                         (10.2)
```

Les tranches sont donc de Cauchy dans `L-infinity` quand `s,t->0-`. Leur
limite bornée `u_*` est aussi leur limite dans `D'`; l'hypothèse impose
`u_*=0`. Cette étape est plus forte que la seule promotion locale par
Arzelà–Ascoli et exclut les paquets qui s'échappent à l'infini.

### Étape B — extension mild au temps terminal

Pour tout `a<0`, la formule mild vaut sur `[a,t]`, `t<0`. Le noyau d'Oseen
différentié satisfait

```text
||K(t)||_1 <= C_K t^(-1/2).
```

La queue de Duhamel sur un intervalle de longueur `delta` est donc au plus

```text
2 C_K M² sqrt(delta),                                         (10.3)
```

uniformément en espace. Les autres termes convergent en `L-infinity` par
continuité du semi-groupe à temps strictement positif. En passant `t->0-`, on
obtient la formule mild sur `[a,0]` avec donnée finale `u(0)=0`. La borne
`k=1,l=0` de (10.1) donne en même temps une vorticité bornée.

### Étape C — unicité rétrograde de la vorticité

La vorticité vérifie

```text
partial_t omega-Delta omega
  =(omega dot nabla)u-(u dot nabla)omega.
```

Après renversement du temps sur une bande finie, (10.1) donne

```text
|partial_tau omega+Delta omega|
  <= C_M(|omega|+|nabla omega|).                              (10.4)
```

La convergence `D'` et les bornes uniformes de toutes les dérivées donnent
`omega(t)->0` dans `C^0_local`. **[SOURCE]** Le théorème 5.1 d'ESS s'applique
sur chaque demi-espace translaté : régularité locale quadratique, croissance
gaussienne, coefficients bornés et trace finale nulle sont toutes vérifiées.
L'union des demi-espaces annule `omega` sur `R³` et le raisonnement vaut sur
toute bande finie.

Alors `Delta u=nabla div u-curl curl u=0`. Le Liouville harmonique et la
bornitude donnent `u=b(t)`; la remarque 6.1 de KNSS rend `b` constante, et la
trace l'annule.

**Contrôle corroborant.** Le théorème 1.1 publié de
[Lei–Yang–Yuan 2024](https://doi.org/10.1093/imrn/rnae208) donne aussi
l'unicité de deux solutions mild bornées à même donnée finale. L'extension
mild jusqu'à `t=0`, justifiée par (10.3), permettrait de comparer `u` à zéro.
Cette route n'est pas le seul support retenu : l'arXiv v1 comporte un renvoi
interne erroné, un facteur `1/2` manquant dans une identité de Laplacien et un
écart `k/2k` dans un poids. Ces anomalies paraissent localement réparables et
ne réfutent pas l'article évalué, mais la version éditeur sous accès contrôlé
n'a pas été comparée ligne à ligne.

### Attaques et portée Clay

- Sans mildness, `u=b(t)`, `p=-b'(t) dot x` est un contre-exemple classique.
- Une valeur `u(0)=0` assignée à une constante non nulle sur `t<0` n'est pas
  une trace.
- Une suite `f_N=(0,sin(Nx_1),0)` converge dans `D'`, mais perd la borne de
  vorticité et ne constitue pas une trajectoire ancienne unique.
- Des paquets traduits à l'infini conservent toutes leurs dérivées et
  convergent dans `D'`, mais violent le module temporel global (10.2) s'ils
  sont assemblés sans structure mild.
- La limite KNSS par maximum satisfait précisément toutes les portes sauf la
  trace nulle : elle porte la normalisation opposée `|u(0,0)|=1`.

Le lemme de rigidité est donc fermé, mais son raccord au problème Clay ne
l'est pas. Aucune chaîne ESS, GKP ou KNSS ne transmet à un **même objet**
`mildness + borne L-infinity globale + trace terminale nulle + non-trivialité`.
Le prochain verrou est la possibilité — ou l'impossibilité quantitative — de
faire hériter cette trace à une extraction maximum-normalisée sans réintroduire
une borne critique circulaire.

## 11. Trace du zoom maximum et concentration critique — cycle 0009

### Les tests physiques deviennent mobiles

Pour le zoom KNSS

```text
v_k(y,s)=M_k^-1 u(x_k+M_k^-1 y,t_k+M_k^-2 s),
```

les deux extrémités temporelles sont

```text
A_k=-M_k²t_k -> -infinity,
B_k=M_k²(T-t_k)>0.
```

Le point essentiel est que `s=0` correspond au temps-record physique `t_k`,
et non au temps maximal `T`; celui-ci correspond à l'extrémité future mobile
`s=B_k`. Toute « trace » obtenue ci-dessous à `s=0` est donc une valeur au
temps-record. Elle ne peut être identifiée à une trace terminale physique.

et `phi in C_c^infinity(R³)`, le changement de variable exact donne

```text
<v_k(s),phi>
  =M_k² integral u(x,t_k+s/M_k²) phi(M_k(x-x_k)) dx.          (11.1)
```

Le test physique est donc
`Phi_k(x)=M_k² phi(M_k(x-x_k))`. Son support se concentre et se translate,
tandis que

```text
||partial^alpha Phi_k||_infinity
  =M_k^(2+|alpha|)||partial^alpha phi||_infinity,
||Phi_k||_(3/2)=||phi||_(3/2).                                (11.2)
```

Une trace de `u(t)` dans `D'` contrôle chaque test **fixe**; elle ne contrôle
pas automatiquement cette famille critique mobile. Même une borne `L³`
globale n'apporte pas la compacité manquante : les champs
`U_k(x)=M_k w(M_kx)`, avec `w` compact divergence-free, convergent vers zéro
dans `D'` et gardent une norme `L³` constante, tandis que leur zoom est
exactement `w`. Ces champs ne sont pas les tranches démontrées d'une même
trajectoire de blow-up; ils réfutent seulement l'inférence fonctionnelle.

### Dans la vraie classe KNSS, les limites commutent au temps-record

**[SOURCE + DÉRIVATION]** La proposition 6.1 fournit, pour les temps records,
`|v_k|<=gamma_k` sur le passé, `gamma_k->1`, et `|v_k(0,0)|=1`. Pour `k` assez
grand, `gamma_k<=2`. En redémarrant la proposition 4.1 un temps normalisé fixe
avant chaque `s in [-delta,0]`, on obtient pour tous les ordres nécessaires

```text
sup_k sup_(-delta<=s<=0)
  (||nabla^m v_k(s)||_infinity+||partial_s v_k(s)||_infinity)
  < infinity.                                                 (11.3)
```

La convergence du lemme 6.1 se renforce donc, après sous-suite, jusqu'au
temps-record `s=0` dans `C^m_local`. Pour tout test compact,

```text
|<v_k(s)-v_k(0),phi>|
  <= L |s| ||phi||_1,                                        (11.4)
```

uniformément en `k`. Par conséquent,

```text
lim_(s->0-) lim_(k->infinity) <v_k(s),phi>
 =lim_(k->infinity) lim_(s->0-) <v_k(s),phi>
 =<v(0),phi>.                                                 (11.5)
```

Comme `|v(0,0)|=1`, une fonction test vectorielle fixe, supportée assez près de
l'origine et alignée avec `v(0,0)`, a un pairing non nul. La valeur commune au
temps-record n'est donc pas zéro. Une tentative de raccord ESS à ce temps est
**incompatible** avec la normalisation maximum; ce n'est pas une liberté
laissée par l'ordre des limites. Le constat ne porte pas encore sur le temps
physique `T`.

Pour aligner l'horloge sur `T`, il faut poser

```text
w_k(y,tau)=v_k(y,tau+B_k),
```

de sorte que `tau=0` corresponde à `T` et que le témoin
`|v_k(0,0)|=1` se trouve à `tau=-B_k`. Deux branches restent : si
`B_k->infinity`, le témoin fuit vers le passé; si `B_k->beta<infinity`, il
reste à `tau=-beta`, mais la borne maximum `|v_k|<=gamma_k` ne contrôle que
`tau<=-B_k`, pas l'intervalle `(-B_k,0)`. C'est l'extrémité mobile, et non le
commutateur en `s=0`, qui constitue le trou exact.

### Masse `L³` nécessaire et critère conditionnel

Soit `G` une borne uniforme de `||nabla v_k(0)||_infinity` donnée par (11.3).
La normalisation ponctuelle et l'inégalité des accroissements finis donnent

```text
|v_k(y,0)|>=1/2 pour |y|<=1/(2G).
```

Puisque la masse locale vérifie exactement

```text
integral_(B_R)|v_k(y,0)|^q dy
 =M_k^(3-q) integral_(B_(R/M_k)(x_k))|u(x,t_k)|^q dx,         (11.6)
```

le cas critique `q=3` donne

```text
integral_(B_(1/(2GM_k))(x_k)) |u(x,t_k)|³ dx
  >= pi/(48G³).                                               (11.7)
```

**[DÉRIVATION DU LABORATOIRE + COMPARAISON DE SOURCE]** Une conséquence par
contraposée est l'énoncé suivant : si, pour un voisinage terminal de `T`,

```text
lim_(r->0) sup_(t<T, x in R³)
  integral_(B_r(x)) |u(x,t)|³ dx =0,                         (11.8)
```

alors `T` ne peut pas être un temps maximal fini d'une solution mild. Ce n'est
pas revendiqué comme un nouveau critère. L'équi-intégrabilité uniforme complète
de (11.8) implique la condition uniforme à seuil fixe (23) de Constantin 2023,
dont le théorème 2 donne déjà une borne explicite de `Hdot1` et le
prolongement. La concentration (11.7) est ici une reformulation quantitative
de l'obstruction connue dans la normalisation KNSS. Elle n'est pas fournie par
l'énergie et ne découle pas d'une simple borne `L-infinity_tL³_x`, car une
boule d'absolue continuité valable séparément pour chaque tranche n'est pas
uniforme en temps.

### Contre-test de la porte mild

La famille exacte sur `R³ x (-infinity,0]`

```text
u_k(x,s)=exp(k²s)e_1,
p_k(x,s)=-k²exp(k²s)x_1
```

est classique, divergence-free, uniformément bornée et localement adaptée.
Son résidu NS est identiquement nul, mais

```text
lim_(s->0-)lim_(k->infinity)u_k(s)=0,
lim_(k->infinity)lim_(s->0-)u_k(s)=e_1.
```

Elle échoue exactement à la mildness KNSS : la formule d'Oseen imposerait la
constance temporelle du mode spatial constant. De plus
`||partial_s u_k(0)||_infinity=k²`. Le test prouve que la PDE locale et
l'inégalité d'énergie locale ne suffisent pas à (11.4); il ne réfute pas le
résultat positif dans la classe mild.

### Décision de raccord

Le paquet « ancienne mild bornée + trace nulle au temps-record + normalisation
non triviale » est contradictoire dans le zoom maximum KNSS. Une vraie trace à
`T` demanderait au contraire de contrôler la suite décalée `w_k` jusqu'à son
extrémité mobile. Après trois stratégies sur le raccord hybride, cet axe est
suspendu : une réouverture exige une extraction différente ou un lemme
d'équivalence de profils, pas une nouvelle permutation au même temps-record.
