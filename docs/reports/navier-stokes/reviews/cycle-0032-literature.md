# Cycle 0032 — veille primaire : streamfunctions non séparables, coaire et cancellation Lorentz

Date de coupure : 2026-08-14.

Objet : audit différentiel du verrou
GAP-NONSEPARABLE-COMPACT-CURL-FLATNESS. La question est de savoir si une somme
de streamfunctions axisymétriques compactes, dont les couches de transition se
recouvrent, peut masquer le coût faible-\(L^{3/2}\) du rotationnel tout en
préservant une vitesse faible-\(L^3\) non petite et une direction de vorticité
régulière. Les identités marquées **AI_DERIVATION** sont des calculs du
laboratoire, pas des résultats publiés.

## Verdict différentiel

1. La représentation axisymétrique est linéaire. Pour
   \(U=(q/r)e_\theta\), avec \(q=q(r,z)\) compact et supporté loin de l'axe,

   \[
   W=\operatorname{curl}U
   =-\frac{\partial_zq}{r}e_r+\frac{\partial_rq}{r}e_z.         \tag{1}
   \]

   Ainsi \(q=\sum_kq_k\) donne exactement \(W=\sum_kW_k\), même lorsque les
   supports se chevauchent. Cette linéarité est seulement cinématique : une
   somme de solutions Grad–Shafranov ou Euler stationnaires n'est en général
   pas une solution de l'équation non linéaire correspondante.

2. La formule de coaire de Fleming–Rishel donne ici une identité exacte et
   pondérée de façon favorable :

   \[
   \|W\|_{L^1(\mathbb R^3)}
   =2\pi\int_{\mathbb R_+\times\mathbb R}|\nabla q|\,dr\,dz
   =2\pi\,TV(q).                                               \tag{2}
   \]

   En la combinant à l'inégalité faible-\(L^{3/2}\), on obtient, si
   \(E=\{W\ne0\}\) a mesure finie,

   \[
   \boxed{\;
   \|W\|_{L^{3/2,\infty}}
   \ge \frac{2\pi}{3}\,
        \frac{TV(q)}{|E|^{1/3}}.\;}                            \tag{3}
   \]

   (2)–(3) sont **AI_DERIVATION** à partir de deux théorèmes classiques.
   Le quotient de droite est exactement invariant par l'échelle
   Navier–Stokes.

3. (3) ne ferme pas le verrou non séparable. La variation totale est
   sous-additive,

   \[
   TV\!\left(\sum_kq_k\right)\le\sum_kTV(q_k),
   \]

   sans minoration inverse : \(q_2=-q_1\) annule exactement le membre gauche.
   La coaire contrôle les périmètres des niveaux de la **somme totale**, pas la
   somme des périmètres de chaque couche. Elle empêche de faire disparaître une
   transition du champ total, mais permet de la déplacer, de l'étaler ou de
   l'annuler localement.

4. Les théorèmes de Bourgain–Brezis et Van Schaftingen exploitent les
   contraintes différentielles div–curl pour améliorer des estimations à
   données \(L^1\). Ils donnent des bornes **supérieures** sur un potentiel ou
   une primitive à partir du champ total. Ils ne donnent aucune borne
   inférieure de \(\|\sum_kW_k\|_{L^{3/2,\infty}}\) en fonction des normes des
   couches. Dans le théorème 8.5 de Van Schaftingen 2013, le cas Lorentz
   \(q=\infty\) ne requiert même que l'ellipticité, contrairement aux
   \(q\in(1,\infty)\) où ellipticité et cancellation sont nécessaires et
   suffisantes. Le faible endpoint ne fournit donc pas le gain coercif espéré.

5. Tous les critères géométriques de régularité s'appliquent à la direction de
   la vorticité **totale** \(W/|W|\), jamais aux directions des \(W_k\)
   séparément. Une annulation peut déplacer les superniveaux, créer des zéros
   où la direction est instable, ou transformer deux couches individuellement
   cohérentes en un champ total transversal. Aucun critère publié repéré ne
   convertit un ledger de streamfunctions en contrôle de direction log-BMO.

6. La veille 2025–2026 ne change pas ce verdict. Grujić
   arXiv:2511.00725v3 étudie précisément deux anneaux et une cancellation
   Hardy/log-bmo, mais propose un mécanisme conditionnel et non une famille
   compacte NS certifiée. Lei–Ren–Tian reste en v1, Grujić
   arXiv:2607.08866 reste en v2, et l'annonce Shahmurov à swirl arbitraire
   reste en v1 sans validation indépendante.

## 1. Équation, objet et échelle

Le problème Clay de référence est Navier–Stokes incompressible non forcé sur
\(\mathbb R^3\), \(\nu>0\),

\[
 \partial_tu+(u\cdot\nabla)u+\nabla p=\nu\Delta u,\qquad
 \nabla\cdot u=0.                                             \tag{4}
\]

Le présent audit ne construit qu'une donnée à temps fixé. Dans le demi-plan
méridien \(H=\{(r,z):r>0\}\), soit

\[
 q\in C_c^\infty(H),\qquad
 U=\frac qr e_\theta.                                         \tag{5}
\]

Le support est supposé à distance positive de \(r=0\). Si le support touche
l'axe, les conditions au pôle de Liu–Wang doivent être imposées; la seule
formule formelle ne certifie pas la régularité cartésienne.

Sous

\[
 U_\lambda(x)=\lambda U(\lambda x),\qquad
 W_\lambda(x)=\lambda^2W(\lambda x),
\]

la streamfunction vérifie \(q_\lambda(r,z)=q(\lambda r,\lambda z)\). On a

| Quantité | Échelle |
|---|---|
| \(\|U\|_{L^{3,\infty}}\) | invariante |
| \(\|W\|_{L^{3/2,\infty}}\) | invariante |
| \(TV(q)\) dans le plan méridien | \(\lambda^{-1}TV(q)\) |
| \(|\{W\ne0\}|^{1/3}\) | \(\lambda^{-1}|\{W\ne0\}|^{1/3}\) |
| \(TV(q)/|\{W\ne0\}|^{1/3}\) | invariant |

La borne (3) est donc critique malgré l'emploi intermédiaire de \(L^1\).

## 2. Représentation par streamfunction et superposition

### Source structurelle déjà cataloguée

Jian-Guo Liu et Wei-Cheng Wang,
[*Characterization and Regularity for Axisymmetric Solenoidal Vector Fields
with Application to Navier–Stokes
Equation*](https://doi.org/10.1137/080739744), *SIAM J. Math. Anal.* **41**
(2009), 1825–1850, est déjà enregistrée sous **NS-SRC-0102**. L'article traite
les formulations primitive et vorticité–streamfunction des écoulements
axisymétriques incompressibles, les conditions au pôle et l'équivalence avec
la formulation faible de Leray dans son cadre. Il justifie le raccord
cinématique (5), mais ne fournit aucune constante Lorentz ou BMO pour des
couches dégénérantes.

Pour une somme non séparable

\[
 q=\sum_{k=1}^Nq_k,\qquad
 U=\sum_{k=1}^N\frac{q_k}{r}e_\theta,                          \tag{6}
\]

l'incompressibilité et (1) sont préservées exactement. En revanche, les
fonctions de distribution ne sont pas additives lorsque plusieurs \(W_k(x)\)
sont non nuls au même point :

\[
 \mu_{\left|\sum_kW_k\right|}(s)
 \ne\sum_k\mu_{|W_k|}(s)
\]

en général. Les proxies de volume du cycle 0031 ne peuvent donc être sommés
sans un lemme de non-annulation.

### Grad–Shafranov et Euler : la superposition s'arrête à la cinématique

Constantin, La et Vicol,
[*Remarks on a paper by Gavrilov: Grad–Shafranov equations, steady solutions
of the three dimensional incompressible Euler equations with compactly
supported velocities, and
applications*](https://doi.org/10.1007/s00039-019-00516-1),
*Geom. Funct. Anal.* **29** (2019), 1773–1793,
[arXiv:1903.11699](https://arxiv.org/abs/1903.11699), est déjà
**NS-SRC-0108**. L'article construit des vitesses Euler stationnaires lisses
compactes par une équation Grad–Shafranov localisable. Les fonctions sources
dépendent non linéairement de la streamfunction; additionner deux solutions
localisées ne conserve pas en général cette équation.

Daomin Cao et Weicheng Zhan,
[*On the Steady Axisymmetric Vortex Rings for 3D Incompressible Euler
Flows*](https://doi.org/10.1137/24M1678076), *SIAM J. Math. Anal.* **58**
(2026), 1288–1315, déjà **NS-SRC-0105**, construisent des anneaux Euler
axisymétriques avec ou sans swirl par une structure variationnelle et une
désingularisation. C'est une source 2026 publiée sur des streamfunctions
non triviales, pas un principe de superposition, et l'équation a
\(\nu=0\).

Paolo Buttà, Guido Cavallaro et Carlo Marchioro,
[*Leapfrogging Vortex Rings as Scaling Limit of Euler
Equations*](https://doi.org/10.1137/24M1642391), *SIAM J. Math. Anal.*,
publié en 2025, [arXiv:2310.00732v2](https://arxiv.org/abs/2310.00732v2),
déjà **NS-SRC-0119**, contrôlent une limite à \(N\) anneaux minces pour
\(N\) fixé et des coeurs initialement séparés. Le résultat ne donne aucune
uniformité lorsque les couches se chevauchent et s'annulent, et reste Euler
axisymétrique sans swirl.

## 3. Coaire et variation totale du champ total

### Source primaire nouvelle

Wendell H. Fleming et Raymond Rishel,
[*An integral formula for total gradient
variation*](https://doi.org/10.1007/BF01236935), *Archiv der Mathematik*
**11** (1960), 218–222, DOI
[10.1007/BF01236935](https://doi.org/10.1007/BF01236935), donnent la formule
de coaire pour la variation totale. Cette source n'est pas présente dans le
catalogue au HEAD audité.

Pour \(q\in C_c^\infty(H)\), la version signée utile est

\[
 TV(q)=\int_H|\nabla q|\,dr\,dz
 =\int_0^\infty
   \bigl[P_H(\{q>t\})+P_H(\{q<-t\})\bigr]\,dt.                 \tag{7}
\]

Par (1) et \(dx=r\,dr\,d\theta\,dz\),

\[
\begin{aligned}
 \int_{\mathbb R^3}|W|\,dx
 &=2\pi\int_H
   \frac{\sqrt{|\partial_rq|^2+|\partial_zq|^2}}r\,r\,dr\,dz\\
 &=2\pi TV(q),
\end{aligned}
\]

ce qui prouve (2). Si
\(K=\|W\|_{L^{3/2,\infty}}\), l'inégalité de réarrangement déjà auditée au
cycle 0026 donne

\[
 \int_E|W|\le3K|E|^{1/3}.
\]

Avec \(E=\{W\ne0\}\), cela donne (3).

### Ce que la coaire interdit

Si le champ total conserve une transition telle que

\[
 \frac{TV(q)}{|\{W\ne0\}|^{1/3}}\longrightarrow\infty,
\]

alors son endpoint faible-\(L^{3/2}\) diverge. Comprimer une variation totale
fixée dans une couche de volume décroissant a donc un coût critique. Cette
conclusion porte sur la vraie fonction de distribution du rotationnel total,
sans supposer que les transitions soient séparées.

### Ce que la coaire n'interdit pas

1. **Annulation exacte.** \(q_2=-q_1\) donne \(q=W=U=0\).
2. **Annulation partielle.** La variation de \(q_1+q_2\) peut être
   arbitrairement plus petite que \(TV(q_1)+TV(q_2)\).
3. **Déplacement de la transition.** Annuler \(\nabla q_1\) dans une couche
   peut déplacer la variation vers une couche plus large de \(q_1+q_2\).
4. **Étalement.** À variation totale fixée, augmenter
   \(|\{W\ne0\}|\) diminue le membre droit de (3).
5. **Queue diffuse adverse.** Ajouter à distance une perturbation lisse de
   gradient arbitrairement petit mais non nul sur un très grand ensemble peut
   augmenter \(|\{W\ne0\}|\) sans modifier sensiblement le gate vitesse ni la
   quasi-norme faible de la vorticité du coeur. La version « support total » de
   (3) devient alors vacue; une variante utile devra être tronquée par niveau.
6. **Direction.** (7) compte des périmètres, pas la courbure, le nombre de
   tours de la tangente, ni l'oscillation BMO de
   \(\nabla^\perp q/|\nabla q|\).
7. **Gate vitesse.** Aucune inégalité générale ne minore \(TV(q)\) à partir
   de la seule quasi-norme \(\|q/r\|_{L^{3,\infty}(\mathbb R^3)}\) avec une
   constante indépendante du support et de la concentration.

Le dernier point est le trou exact. Une borne BV–Sobolev dans le plan contrôle
une norme forte de \(q\), tandis que le gate du programme est faible-\(L^3\)
pour \(U\). Sur un ensemble de mesure finie, l'inclusion faible-\(L^3\) vers
\(L^2\) fournit une **majoration** de \(L^2\), pas la minoration requise.
Une masse faible-\(L^3\) peut être portée sur un sous-ensemble arbitrairement
petit.

## 4. Lorentz vectoriel et opérateurs canceling

### Sources déjà au catalogue

George Lorentz (**NS-SRC-0097**) et Richard O'Neil
(**NS-SRC-0067**) fournissent respectivement les espaces et les inégalités de
réarrangement/convolution utilisées dans le dépôt. Appliquées au module d'un
champ vectoriel, elles donnent une quasi-inégalité triangulaire supérieure.
Elles ne donnent aucune inégalité triangulaire inverse.

Smirnov (**NS-SRC-0099**) décompose les charges solénoïdales en solénoïdes
élémentaires. Ce théorème encode un retour géométrique du flux, mais ne donne ni
une décomposition compatible avec les couches \(q_k\), ni une minoration
faible-\(L^{3/2}\) sous recouvrement.

### Sources primaires nouvelles sur la cancellation différentielle

Jean Bourgain et Haïm Brezis,
[*New estimates for elliptic equations and Hodge type
systems*](https://doi.org/10.4171/JEMS/80), *J. Eur. Math. Soc.* **9**
(2007), 277–315, DOI
[10.4171/JEMS/80](https://doi.org/10.4171/JEMS/80), établissent des estimations
limites pour les systèmes div–curl et de Hodge à données \(L^1\). En
particulier, la contrainte divergence-free améliore l'action d'un champ
\(L^1\) sur des fonctions tests et permet des potentiels plus forts que
l'estimation scalaire naïve.

Jean Van Schaftingen,
[*Limiting Sobolev inequalities for vector fields and canceling linear
differential operators*](https://doi.org/10.4171/JEMS/380),
*J. Eur. Math. Soc.* **15** (2013), 877–921, DOI
[10.4171/JEMS/380](https://doi.org/10.4171/JEMS/380), caractérise les
opérateurs homogènes elliptiques et canceling pour lesquels

\[
 \|D^{k-1}v\|_{L^{n/(n-1)}}
 \le C\|A(D)v\|_{L^1}.                                      \tag{8}
\]

Son théorème 8.5 donne, pour \(q\in(1,\infty)\), la version
\(L^{n/(n-1),q}\) si et seulement si l'opérateur est elliptique et canceling.
Au cas \(q=\infty\), l'ellipticité seule est nécessaire et suffisante
(proposition 8.24); le cas général \(q=1\) y reste un problème ouvert.

Daniel Spector et Jean Van Schaftingen,
[*Optimal embeddings into Lorentz spaces for some vector differential
operators via Gagliardo's
lemma*](https://doi.org/10.4171/RLM/854), *Atti Accad. Naz. Lincei Cl. Sci.
Fis. Mat. Natur.* **30** (2019), no. 3, 413–436, DOI
[10.4171/RLM/854](https://doi.org/10.4171/RLM/854), obtiennent des
estimations optimales dans \(L^{n/(n-1),1}\) pour certaines classes
d'opérateurs différentiels du premier ordre. Le mot « certaines » est
essentiel : l'article n'établit pas une minoration universelle pour toute
superposition de curls axisymétriques.

Ces trois sources ne figurent pas dans le catalogue au HEAD audité.

### Pourquoi ces théorèmes ne ferment pas le ledger

Leur sens est schématiquement

\[
 \text{norme d'un potentiel}
 \le C\,\text{norme }L^1\text{ de la donnée différentielle totale}. \tag{9}
\]

Le verrou demanderait plutôt

\[
 \left\|\sum_kW_k\right\|_{L^{3/2,\infty}}
 \ge F\bigl(\|W_1\|,\ldots,\|W_N\|,
            \text{géométrie des couches}\bigr),                \tag{10}
\]

avec \(F>0\) malgré le recouvrement. (9) n'implique pas (10). En outre :

- l'entrée de (8)–(9) est \(L^1\) forte, non
  \(L^{3/2,\infty}\);
- l'exposant de sortie naturel en dimension trois est \(3/2\), non le gate
  vitesse \(L^{3,\infty}\) du programme;
- les contraintes div–curl portent sur le champ total;
- au faible endpoint \(q=\infty\), la théorie générale ne distingue pas les
  opérateurs canceling des opérateurs seulement elliptiques;
- le contre-exemple \(W_2=-W_1\) exclut toute minoration couche par couche sans
  hypothèse de cône, de séparation ou de signe.

L'estimation Biot–Savart–Lorentz classique reste valide :

\[
 \|U\|_{L^{3,\infty}}
 \le C_{\rm BS}\|W\|_{L^{3/2,\infty}}.                        \tag{11}
\]

Elle impose \(K_W\ge K_U/C_{\rm BS}\), mais aucune croissance avec le rapport
d'aspect et aucune oscillation directionnelle. La non-séparabilité peut donc
au mieux chercher à saturer une constante globale, pas à violer (11).

## 5. Conditions qui restaurent une minoration

Une somme vectorielle retrouve une coercivité sous une hypothèse orientée
forte. Si, pour un même \(e\in S^2\) et \(\alpha>0\),

\[
 W_k(x)\cdot e\ge\alpha|W_k(x)|
 \quad\text{pour tout }k\text{ actif en }x,
\]

alors

\[
 \left|\sum_kW_k(x)\right|
 \ge e\cdot\sum_kW_k(x)
 \ge\alpha\sum_k|W_k(x)|.                                   \tag{12}
\]

La couche ne peut plus être masquée. Mais une vorticité compacte non nulle ne
peut rester globalement dans un hémisphère orienté strict, puisque
\(\int_{\mathbb R^3}W=0\). Une hypothèse de cône globale assez forte pour
prouver (12) est donc incompatible avec le curl compact recherché.

D'autres hypothèses suffisent localement mais doivent être démontrées :

- supports de \(\nabla q_k\) disjoints;
- angle uniformément aigu entre les gradients actifs;
- dominance d'une couche sur la somme des autres;
- borne sur la multiplicité de recouvrement et absence de branche antipodale;
- minoration directe de \(TV(\sum q_k)\) à l'échelle du support total.

Le double cône projectif \(\{\pm e\}\) ne suffit pas : deux branches
antipodales s'annulent exactement.

## 6. Critères de direction : ils voient seulement le champ total

| Source primaire, identifiant du catalogue | Cadre exact | Ce que voit l'hypothèse | Non-transfert à la somme \(q=\sum q_k\) |
|---|---|---|---|
| Constantin–Fefferman 1993, **NS-SRC-0021**, [DOI 10.1512/iumj.1993.42.42034](https://doi.org/10.1512/iumj.1993.42.42034) | NS non forcé sur \(\mathbb R^3\), solution faible issue d'une donnée de type \(H^1\) | sinus de l'angle pairwise de la vorticité totale sur la zone high–high | insensible à \(+e/-e\); aucune stabilité sous décomposition en couches |
| Beirão da Veiga–Berselli 2002, **NS-SRC-0060**, [DOI 10.57262/die/1356060864](https://doi.org/10.57262/die/1356060864) | NS \(\mathbb R^3\), Leray–Hopf, cohérence Hölder de la direction totale; endpoint \(1/2\) | module spatial pairwise | une borne sur chaque \(\xi_k\) ne contrôle pas \(\xi_{\sum W_k}\) près des annulations |
| Berselli 2023, **NS-SRC-0063**, [DOI 10.1088/1361-6544/ace096](https://doi.org/10.1088/1361-6544/ace096) | NS périodique, et adaptation espace entier; petits sauts discrets de la direction | direction totale échantillonnée | aucun ledger Lorentz de streamfunctions |
| Grujić–Guberović 2010, **NS-SRC-0098**, [DOI 10.1007/s00220-010-1000-4](https://doi.org/10.1007/s00220-010-1000-4) | NS localisé; équilibre entre magnitude et cohérence de direction | vorticité totale et quotient d'angle local | les termes croisés de la somme ne sont pas contrôlés par les couches séparées |
| Lei–Ren–Tian 2025, **NS-SRC-0061**, [arXiv:2501.08976v1](https://arxiv.org/abs/2501.08976v1) | solution faible adaptée locale dans \(Q(1)\); double cône des fortes vorticités | direction de \(W=\sum W_k\), signe projectif autorisé | une géométrie conique de chaque couche ne garantit pas celle de la somme; v1 non publiée |
| Grujić 2026, **NS-SRC-0059**, [arXiv:2607.08866v2](https://arxiv.org/abs/2607.08866v2) | scénario critique conditionnel NS sur \(\mathbb R^3\), \(W\in L_t^\infty L_x^{3/2,\infty}\), direction totale en \(\mathrm{bmo}_{1/|\log r|}\) | oscillation moyenne orientée de la direction totale | suppose exactement les deux contrôles à produire; v2 non publiée |

Le passage

\[
 \{\xi_k\text{ cohérentes pour tout }k\}
 \Longrightarrow
 \frac{\sum_kW_k}{|\sum_kW_k|}
 \text{ cohérente}
\]

est faux sans une marge quantitative empêchant \(|\sum_kW_k|\) de devenir
petit. Au voisinage d'un zéro de la somme, une perturbation arbitrairement
petite peut faire tourner la direction d'un angle d'ordre un.

## 7. Veille 2025–2026

### Sources déjà cataloguées

- **NS-SRC-0112** : Zoran Grujić,
  [*On taming Moffatt–Kimura vortices of doom in the viscous
  case*](https://arxiv.org/abs/2511.00725v3),
  arXiv:2511.00725v3, soumise le 1er novembre 2025, révisée le 10 juin 2026.
  La note propose un mécanisme visqueux à deux couches pour deux anneaux
  contre-rotatifs en collision à angle non trivial, puis une cancellation
  Hardy/log-composite-bmo. Le résumé parle d'un mécanisme « potentially
  capable » d'éviter la singularité. Il ne s'agit ni d'un théorème global
  publié, ni d'une construction NS exacte des anneaux, ni d'un calcul
  certifié des endpoints de (3).
- **NS-SRC-0061** : Lei–Ren–Tian,
  arXiv:2501.08976v1 du 15 janvier 2025, reste une v1 sans publication
  affichée. Le double cône porte sur la vorticité totale high–vorticity.
- **NS-SRC-0059** : Grujić,
  arXiv:2607.08866v2 du 13 juillet 2026, reste une v2 sans publication
  affichée. Les hypothèses faible-\(L^{3/2}\) et log-BMO ne sont pas produites
  par une superposition.
- **NS-SRC-0105** : Cao–Zhan 2026 est publié, mais concerne Euler
  axisymétrique stationnaire avec/sans swirl.
- **NS-SRC-0119** : Buttà–Cavallaro–Marchioro 2025 est publié, mais le passage
  à \(N\) anneaux garde \(N\) fixé et exploite des coeurs minces séparés.
- **NS-SRC-0131** : Peralta-Salas–Wan,
  arXiv:2607.16141v1, construit une section hélicoïdale anisotrope Euler,
  seulement piècewise lisse et non compacte axialement; aucun raccord NS.
- **NS-WATCH-0004** : Shahmurov,
  [arXiv:2606.07869v1](https://arxiv.org/abs/2606.07869v1), revendique la
  régularité axisymétrique à swirl arbitraire. Au 2026-08-14, une seule v1 du
  5 juin 2026 est affichée, sans publication; la preuve n'est pas admise.

### Résultat négatif de la veille

Aucune source 2025–2026 repérée ne démontre l'une des deux implications
requises :

\[
 \|U\|_{L^{3,\infty}}\ge\kappa,\quad
 q=\sum_kq_k
 \Longrightarrow
 \frac{TV(q)}{|\operatorname{supp}\nabla q|^{1/3}}\ge c(\kappa)>0
\]

avec une amélioration dépendant de l'aspect, ou

\[
 \{\text{direction contrôlée couche par couche}\}
 \Longrightarrow
 \xi_{\operatorname{curl}U}
 \in\mathrm{bmo}_{1/|\log r|}.
\]

La première implication reste plausible seulement avec une contrainte
géométrique supplémentaire; la seconde est fausse près d'annulations non
quantifiées.

## 8. Sources nouvelles proposées pour le catalogue

Le catalogue s'arrête à **NS-SRC-0131** au HEAD audité. Les identifiants
provisoires suivants devront être réassignés si une écriture concurrente les
occupe :

| ID provisoire | Source primaire | Statut | Rôle exact |
|---|---|---|---|
| **NS-SRC-0132** | Fleming–Rishel, [DOI 10.1007/BF01236935](https://doi.org/10.1007/BF01236935), *Arch. Math.* 11 (1960), 218–222 | publié | formule coaire/variation totale utilisée dans (7) |
| **NS-SRC-0133** | Bourgain–Brezis, [DOI 10.4171/JEMS/80](https://doi.org/10.4171/JEMS/80), *JEMS* 9 (2007), 277–315 | publié | estimations limites div–curl/Hodge à données \(L^1\) |
| **NS-SRC-0134** | Van Schaftingen, [DOI 10.4171/JEMS/380](https://doi.org/10.4171/JEMS/380), *JEMS* 15 (2013), 877–921 | publié | caractérisation elliptique/canceling et comportement Lorentz, dont le faible endpoint |
| **NS-SRC-0135** | Spector–Van Schaftingen, [DOI 10.4171/RLM/854](https://doi.org/10.4171/RLM/854), *Rend. Lincei Mat. Appl.* 30 (2019), 413–436 | publié | embeddings \(L^{n/(n-1),1}\) pour certaines classes du premier ordre |

Ces sources sont des outils d'analyse géométrique ou harmonique; aucune ne
doit recevoir une pertinence Clay supérieure à TOOL_LEMMA sans raccord
dynamique.

## 9. Passe contradictoire

1. **Oubli du poids cylindrique.** (2) utilise exactement
   \(dx=r\,dr\,d\theta\,dz\); le facteur \(1/r\) de (1) s'annule.
2. **Support touchant l'axe.** Exclu dans (5). Sans cette hypothèse, les
   conditions au pôle de NS-SRC-0102 sont nécessaires.
3. **Coaire appliquée aux couches.** Le membre correct est
   \(TV(\sum q_k)\), pas \(\sum TV(q_k)\).
4. **Variation totale prise pour une norme critique.** \(TV(q)\) seul se
   redimensionne; seul le quotient de (3) est critique.
5. **Support actif non robuste.** Une queue diffuse de très petite amplitude
   peut gonfler \(|\{W\ne0\}|\). (3) est exacte mais peut devenir non
   informative; une expérience doit aussi enregistrer les ensembles de
   superniveau et une variation tronquée.
6. **Quasi-triangle inversée.** Elle est fausse par \(W+(-W)=0\).
7. **Cancellation différentielle prise pour non-annulation algébrique.** Les
   théorèmes Bourgain–Brezis/Van Schaftingen améliorent une estimation de
   potentiel; ils n'empêchent pas deux champs admissibles de s'annuler.
8. **Cas Lorentz \(q=1\) et \(q=\infty\) confondus.** Van Schaftingen 2013
   traite \(q\in(1,\infty)\) par ellipticité+cancellation, \(q=\infty\) par
   ellipticité seule, et laisse le résultat optimal général \(q=1\) ouvert.
   Spector–Van Schaftingen 2019 couvre certaines classes, pas toutes.
9. **Direction aux zéros.** Une extension arbitraire sur
   \(\{\sum W_k=0\}\) ne contrôle pas les rotations dans les régions où la
   somme est seulement petite.
10. **Euler vers NS.** Les constructions Grad–Shafranov et anneaux 2025–2026
   ont \(\nu=0\). Leur insertion dans (4) laisse un résidu visqueux et une
   pression/non-linéarité croisée.
11. **Annonce récente.** Les versions arXiv et statuts ont été vérifiés à la
    date de coupure; aucune v1/v2/v3 n'est promue en preuve publiée.

## 10. Conclusion et test discriminant

Le résultat positif du cycle bibliographique est (3) : la variation totale
méridienne du streamfunction **total**, normalisée par le volume actif, minore
l'endpoint critique de la vorticité. Le résultat négatif est que ni coaire, ni
Lorentz, ni la théorie des opérateurs canceling ne fournissent une coercivité
par couche sous recouvrement.

Le test décisif doit donc calculer, pour la somme à deux couches proposée au
cycle 0031,

\[
 q=q_1+q_2,\qquad
 q_k=V_kR\,\eta_k((r-R)/a_k)\chi_k((z-z_k)/b_k),               \tag{13}
\]

les quatre quantités **du total** :

\[
 K_U=\|q/r\|_{L^{3,\infty}},\quad
 K_W=\|\nabla q/r\|_{L^{3/2,\infty}},\quad
 \mathcal C=\frac{TV(q)}{|\{\nabla q\ne0\}|^{1/3}},\quad
 \mathcal M=\sup_B|\log r_B|\,\operatorname{MO}_B(\xi).        \tag{14}
\]

Il faut comparer \(K_W\) à la borne certifiée
\(K_W\ge(2\pi/3)\mathcal C\) et balayer les décalages \(z_2-z_1\), rapports
d'amplitude et rapports d'épaisseur. Pour neutraliser l'attaque par queue
diffuse, le ledger doit aussi répéter \(\mathcal C\) sur les superniveaux
\(\{|W|>\tau\}\), en enregistrant la variation effectivement portée par ces
niveaux. Deux issues sont réellement
discriminantes :

- si \(K_U\ge\kappa\) et \(K_W,\mathcal M\) bornés forcent
  \(\mathcal C\ge c(\kappa)>0\) avec une marge d'aspect quantifiée, le ledger
  non séparable devient un lemme candidat;
- si une suite garde \(K_U\ge\kappa\), \(K_W\) et \(\mathcal M\) bornés tout en
  faisant disparaître les coûts individuels, elle réfute toute extension
  additive du cycle 0031 et impose un pivot vers une contrainte dynamique ou
  topologique.

Même le second résultat serait seulement un contre-profil cinématique. Il ne
fournirait ni solution ancienne, ni profil de blow-up, ni solution NS
admissible du problème Clay.
