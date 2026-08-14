# Cycle 0029 — veille primaire et revue contradictoire

Date de coupure : 2026-08-14 (Europe/Paris).

Périmètre : moments d'une vorticité compacte, développement multipolaire de
Biot–Savart, paires d'anneaux signés axisymétriques sans swirl, critères
critiques en \(L^3\) et log-BMO, et veille différentielle 2025–2026.

Statut : audit bibliographique indépendant. Toutes les identités marquées
« recalculé ici » sont des dérivations du laboratoire et ne doivent pas être
classées `PAPER_PROOF` sans source ou formalisation séparée.

## Verdict exécutif

1. Pour toute vorticité \(\omega\in C_c^\infty(\mathbb R^3)^3\),
   \(\nabla\!\cdot\omega=0\), le moment d'ordre zéro s'annule et le premier
   moment est antisymétrique. Le premier terme non nul du champ de
   Biot–Savart est donc le dipôle d'impulsion, d'ordre \(|x|^{-3}\). Si
   l'impulsion totale s'annule, le champ décroît comme \(O(|x|^{-4})\), sous
   contrôle du second moment absolu. Cela améliore la queue, mais n'implique
   ni vitesse compacte ni petitesse critique.
2. Une paire anti-parallèle exactement impaire en \(z\) a une impulsion
   hydrodynamique **totale nulle**, alors que son moment radial sur le
   demi-espace supérieur peut croître. Les résultats de Choi–Jeong,
   Gustafson–Miller–Tsai, Egamberganov–Yao et Cao–Fan–Qin portent sur ce
   second objet. Il n'y a aucune contradiction : l'annulation multipolaire
   globale n'empêche pas l'étirement interne.
3. Tous les nouveaux résultats quantitatifs forts trouvés sur ces paires
   signées concernent Euler incompressible, inviscide, sur \(\mathbb R^3\),
   axisymétrique sans swirl, et une croissance en temps infini. Ils ne
   donnent ni blow-up fini ni singularité Navier–Stokes au sens Clay.
4. Pour Navier–Stokes visqueux, la classe axisymétrique sans swirl reste
   globalement régulière, même avec vorticité signée. La proposition de
   Choi–Jeong sur \(\nu\to0\) donne une inflation d'enstrophie non uniforme
   en viscosité, pas un blow-up pour une viscosité fixée.
5. Une paire signée impaire fournit un test adverse plus fort que le test
   axial du cycle 0028 : à tout temps visqueux positif, la direction de
   vorticité saute de \(+e_\theta\) à \(-e_\theta\) de part et d'autre du
   plan \(z=0\). Toute boule centrée sur ce plan, loin de l'axe, a une
   oscillation moyenne exactement égale à 1. La norme log-BMO globale, et
   toute version localisée dont la coupure vaut 1 sur cette boule, diverge.
6. Le théorème de petite donnée \(L^3\) de Kato catalogué sous
   `NS-SRC-0010` est un résultat sur \(\mathbb R^3\), pas sur \(\mathbb T^3\).
   La version périodique est standard par théorie mild/semigroupe, mais la
   veille n'a pas identifié de source primaire dédiée dont l'énoncé exact
   ait été contrôlé. Il faut conserver ce raccord comme trou de sourçage.

## 1. Équations, notions de solution et échelles

Le problème visqueux de référence est, sur \(\mathbb R^3\), sans force,

\[
\partial_tu+(u\cdot\nabla)u=-\nabla p+\nu\Delta u,
\qquad \nabla\cdot u=0,\qquad \nu>0.
\]

Les articles de croissance signée audités ci-dessous traitent au contraire
Euler, c'est-à-dire la même équation avec \(\nu=0\), dans la sous-classe

\[
u=u^r(r,z,t)e_r+u^z(r,z,t)e_z,
\qquad \omega=\omega^\theta(r,z,t)e_\theta.
\]

Sous l'échelle Navier–Stokes

\[
u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),\qquad
\omega_\lambda(x,t)=\lambda^2\omega(\lambda x,\lambda^2t),
\]

les normes \(\|u\|_{L^3}\) et
\(\|\omega\|_{L^{3/2,\infty}}\) sont invariantes, tandis que l'impulsion

\[
I(\omega)=\frac12\int_{\mathbb R^3}x\times\omega(x)\,dx
\]

se transforme selon \(I(\omega_\lambda)=\lambda^{-2}I(\omega)\). Une
condition d'impulsion nulle est donc invariante, mais sa taille non nulle
n'est pas une quantité critique.

## 2. Moments compacts et champ lointain de Biot–Savart

### 2.1 Identités cinématiques — recalculées ici

Soit \(\omega\in C_c^\infty(\mathbb R^3)^3\) avec
\(\nabla\cdot\omega=0\). Une intégration par parties donne

\[
\int\omega_j
=\int\nabla\cdot(x_j\omega)=0.
\]

Pour \(M_{ij}=\int y_i\omega_j(y)\,dy\),

\[
0=\int\nabla\cdot(y_i y_j\omega)=M_{ij}+M_{ji},
\]

donc \(M\) est antisymétrique. Avec
\(I=\frac12\int y\times\omega(y)\,dy\), on a

\[
M_{ij}=\varepsilon_{ijk}I_k.
\]

En utilisant la normalisation

\[
u(x)=\frac1{4\pi}\int_{\mathbb R^3}
\frac{\omega(y)\times(x-y)}{|x-y|^3}\,dy,
\]

le développement de Taylor du noyau, pour \(|x|\) supérieur à deux fois le
rayon du support, donne

\[
u(x)=\frac1{4\pi}
\left(\frac{3x(I\cdot x)}{|x|^5}-\frac I{|x|^3}\right)
+O\!\left(
\frac{\int |y|^2|\omega(y)|\,dy}{|x|^4}
\right).
\]

Conséquences vérifiables :

- le terme potentiel d'ordre \(|x|^{-2}\) disparaît automatiquement ;
- si \(I\ne0\), la queue générique est \(|x|^{-3}\), donc n'est pas
  intégrable dans \(L^1\) à l'infini, mais appartient à \(L^p\) pour tout
  \(p>1\), notamment \(L^3\) ;
- si \(I=0\), tous les premiers moments s'annulent et
  \(u(x)=O(|x|^{-4})\) ;
- annuler un nombre fini de moments n'impose jamais à lui seul la compacité
  de \(u\).

La condition de vitesse compacte est infiniment plus rigide. Dans l'espace
de Fourier,

\[
\widehat u(\xi)=\frac{i\,\xi\times\widehat\omega(\xi)}{|\xi|^2}.
\]

Pour que \(u\) soit compacte, ce quotient doit satisfaire la condition
d'extension entière de type exponentiel appropriée de Paley–Wiener. Il
s'agit d'une famille infinie de compatibilités, équivalente à l'annulation
de tous les multipôles harmoniques pertinents, et non de la seule impulsion.
Des exemples non triviaux existent : choisir
\(u\in C_c^\infty\), divergence-free, puis
\(\omega=\nabla\times u\). Biot–Savart restitue ce \(u\) dans la jauge
décroissante. Il serait donc également faux d'affirmer que toute vorticité
associée à une vitesse compacte a tous ses moments ordinaires nuls.

### 2.2 Verdict sur une source primaire de la formule multipolaire

`NS-SRC-0068` (Majda–Bertozzi) suffit pour la normalisation de Biot–Savart
et le cadre Hodge, mais c'est une monographie et non une source de recherche
primaire pour le coefficient dipolaire exact ci-dessus.

La veille a identifié P. G. Saffman, *Dynamics of vorticity*, Journal of
Fluid Mechanics 106 (1981), 49–58,
[DOI](https://doi.org/10.1017/S0022112081001511), et sa
[notice de dépôt Caltech](https://authors.library.caltech.edu/records/t96z5-br480),
comme source primaire classique pertinente pour vorticité et impulsion.
Les métadonnées et le périmètre ont été vérifiés, mais le PDF primaire n'a
pas pu être récupéré dans cette passe ; la page exacte portant le coefficient
dipolaire n'a donc pas été contrôlée. Verdict conservateur :

- conserver la formule comme **dérivation interne autoportée** ;
- ne pas attribuer à Saffman l'exact coefficient avant lecture du PDF ;
- une nouvelle entrée Saffman est utile mais non nécessaire au support
  logique de cette dérivation, et doit rester `metadata_only` jusque-là.

## 3. Paires d'anneaux signés : deux moments à ne pas confondre

Pour \(\omega=\omega^\theta(r,z)e_\theta\), l'intégration en \(\theta\)
donne, toujours par calcul direct,

\[
I(\omega)=\pi e_z\int_0^\infty\!\int_{\mathbb R}
r^2\omega^\theta(r,z)\,dr\,dz.
\]

Deux anneaux minces de circulations \(\Gamma_i\) et rayons \(R_i\) ont donc,
au premier ordre,

\[
I_z\simeq \pi\sum_i\Gamma_iR_i^2.
\]

Une compensation approchée impose
\(\Gamma_2\simeq-\Gamma_1R_1^2/R_2^2\). Pour une paire exactement impaire
en \(z\), de même profil radial réfléchi, \(I=0\) exactement.

Les travaux anti-parallèles définissent plutôt sur \(z>0\), avec la
convention de signe de Choi–Jeong,

\[
P(t)=\int_0^\infty\!\int_0^\infty-r^2\omega^\theta(r,z,t)\,dr\,dz.
\]

Ainsi

\[
I_{\mathrm{total}}=0
\quad\centernot\Longrightarrow\quad
P(t)=0,
\]

et \(P(t)\) peut croître alors que le dipôle global reste annulé par
symétrie. C'est le point de raccord exact entre l'analyse multipolaire et la
littérature récente : le meilleur champ lointain ne déplète pas
automatiquement le stretching à l'intérieur de chaque demi-espace.

## 4. Résultats primaires sur la dynamique signée

### 4.1 Résultats publiés

**Choi–Jeong.** K. Choi et I.-J. Jeong, *On vortex stretching for
anti-parallel axisymmetric flows*, American Journal of Mathematics 147(5)
(2025), 1251–1284, DOI
[10.1353/ajm.2025.a971091](https://doi.org/10.1353/ajm.2025.a971091),
[arXiv:2110.09079v2](https://arxiv.org/abs/2110.09079).

- Équation : Euler 3D incompressible, \(\mathbb R^3\), sans frontière,
  \(\nu=0\), axisymétrique sans swirl.
- Hypothèses : \(\omega^\theta\) impaire en \(z\), non positive pour
  \(z>0\), \(\omega\) et \(\omega/r\) dans \(L^1\cap L^\infty\), moments
  initiaux finis et strictement positifs dans la convention de l'article.
- Conclusion : le moment vertical diminue strictement, \(P(t)\) augmente
  strictement et, pour tout \(\varepsilon>0\),
  \(P(t)\ge C_\varepsilon(1+t)^{2/15-\varepsilon}\). Certaines données
  classiques compactes ont des normes de vorticité/Sobolev non bornées
  lorsque \(t\to\infty\).
- Raccord visqueux exact : leur proposition 6.1 implique, si l'enstrophie
  Euler est non bornée à temps infini, que pour toute approximation initiale
  convergeant fortement dans \(L^2\),
  \[
  \liminf_{\nu\to0^+}\sup_{t\ge0}\|\omega^\nu(t)\|_2=\infty.
  \]
  Le `sup` en temps est pris avant la limite \(\nu\to0\). Chaque solution
  Navier–Stokes à \(\nu>0\) reste globale dans la classe sans swirl.

**Gustafson–Miller–Tsai.** S. Gustafson, E. Miller et T.-P. Tsai,
*Growth rates for anti-parallel vortex tube Euler flows in three and higher
dimensions*, Journal of Mathematical Fluid Mechanics 28 (2026), no. 1,
article 19, DOI
[10.1007/s00021-026-01001-0](https://doi.org/10.1007/s00021-026-01001-0),
[arXiv:2303.12043v1](https://arxiv.org/abs/2303.12043).

- Équation : Euler axisymétrique sans swirl en dimensions \(d\ge3\), avec
  spécialisation pertinente à \(d=3\).
- Hypothèses : paire généralisée anti-parallèle, signe dans le demi-espace,
  imparité par rapport au plan, bornitude et décroissance suffisante à l'axe
  et à l'infini.
- Conclusion en dimension trois : le moment radial pertinent vérifie une
  borne inférieure \(R(t)\ge C_\varepsilon(1+t)^{3/4-\varepsilon}\), sous
  les hypothèses additionnelles exactes du théorème 1.4.
- Limite : croissance inviscide à temps infini, pas singularité finie.

**Lim–Jeong.** D. Lim et I.-J. Jeong, *On the Optimal Rate of Vortex
Stretching for Axisymmetric Euler Flows Without Swirl*, Archive for Rational
Mechanics and Analysis 249 (2025), article 32, publié le 2025-05-09,
[DOI](https://doi.org/10.1007/s00205-025-02103-1),
[arXiv:2409.19497v2](https://arxiv.org/abs/2409.19497).

- Équation : Euler 3D incompressible sur \(\mathbb R^3\), axisymétrique sans
  swirl.
- Hypothèses : \(\omega_0^\theta\) compacte et
  \(\omega_0^\theta/r\in L^\infty\). Aucun signe n'est requis pour cette
  borne supérieure.
- Conclusion : la solution globale satisfait
  \(\|\omega(t)\|_\infty\le A(\omega_0)(1+|t|)^{4/3}\). La constante dépend
  des normes initiales \(L^\infty\) de \(\omega_0\) et \(\omega_0/r\), de
  \(\|\omega_0/r\|_1\) et de l'énergie cinétique initiale.
- Limite : borne polynomiale dans une classe Euler déjà globale ; aucune
  implication de régularité grande donnée pour Navier–Stokes général.

### 4.2 Prépublications 2025–2026

**Egamberganov–Yao.** K. Egamberganov et Y. Yao, *Growth estimates for
axisymmetric Euler equations without swirl*,
[arXiv:2512.13456v1](https://arxiv.org/abs/2512.13456), soumis le 2025-12-15,
22 pages ; aucune référence de revue affichée au jour de coupure.

- Équation : Euler 3D, \(\mathbb R^3\), axisymétrique sans swirl.
- Partie générale : sous les hypothèses d'intégrabilité/bornitude de
  \(\omega\) et \(\omega/r\), bornes supérieures sur les moments et nouvelle
  preuve de la borne \(t^{4/3}\) pour la vorticité maximale.
- Partie signée : sous imparité en \(z\) et signe dans le demi-espace,
  \(P_2(t)\gtrsim t/\log(2+t)\), croissance en limsup au moins
  \(t^{1/4}\) pour toutes les normes \(L^p\), \(1\le p\le\infty\), et
  évasion radiale au sens intégré en temps.
- Identité structurante annoncée :
  \(P_2'(t)=\int_0^\infty r\,u_r(r,0,t)^2\,dr\).
- Statut à employer : `PREPRINT_CLAIM`, pas `PAPER_PROOF`.

**Cao–Fan–Qin.** D. Cao, J. Fan et G. Qin, *Linear Growth of the Vorticity
Maximum for Axisymmetric Euler Flows Without Swirl*,
[arXiv:2511.03171v4](https://arxiv.org/abs/2511.03171), v1 le 2025-11-05,
v2 retirée, v3 le 2026-07-28, v4 le 2026-08-03 ; aucune référence de revue
affichée.

- Équation et classe : Euler 3D, \(\mathbb R^3\), axisymétrique sans swirl,
  donnée compacte non triviale, impaire en \(z\), non positive pour
  \(z>0\), avec les intégrabilités indiquées dans le manuscrit.
- Résultats v4 :
  \[
  \frac{P(t)[\log(2+t)]^{5/2}}{(1+t)^{3/2}}\longrightarrow\infty,
  \]
  évasion radiale/collision quantitative, et échelle linéaire atteinte par
  le rayon extérieur sur une proportion au moins \(1-\eta\) de chaque grand
  intervalle dyadique. Pour les patches d'intensité relative unité, ce rayon
  est la norme maximale de vorticité ; une borne pleine en temps plus faible
  est également obtenue.
- Limite : la croissance \(t^{4/3}\) conjecturée par Childress n'est pas
  atteinte ; il s'agit toujours d'une croissance régulière à temps infini.
- Statut à employer : `PREPRINT_CLAIM`, avec version `v4` obligatoire ; la
  version retirée `v2` ne doit pas être citée.

**Source récente examinée mais secondaire pour ce verrou.** C. García,
Z. Hassainia et T. Hmidi, *Time-periodic leapfrogging vortex rings in the 3D
Euler equations*, [arXiv:2603.21644v1](https://arxiv.org/abs/2603.21644),
soumis le 2026-03-23, construit des anneaux d'Euler en leapfrogging par
désingularisation, formulation hamiltonienne et Nash–Moser. Ce ne sont ni
des anneaux anti-parallèles en collision frontale ni Navier–Stokes visqueux.

### 4.3 Ce qui se transfère, explicitement, au problème Clay

La chaîne valide est seulement

\[
\begin{aligned}
&\text{anneaux anti-parallèles Euler sans swirl}
\\[-2mm]
&\quad\Longrightarrow
\text{croissance quantitative à }t\to\infty
\\[-2mm]
&\quad\Longrightarrow
\text{familles visqueuses éventuellement non uniformes quand }\nu\to0.
\end{aligned}
\]

Les deux implications requises pour Clay manquent : uniformité à viscosité
fixée et concentration en temps fini dans la classe 3D générale. De plus,
la sous-classe visqueuse sans swirl est globalement régulière. Les travaux
de Feng–Šverák autorisent l'existence depuis des combinaisons de filaments
coaxiaux ; le théorème multi-filaments de Lévy–Liu porte explicitement sur
des combinaisons **positives**. En revanche, le cadre mild signé de
Gallay–Šverák pour une vorticité \(L^1\) n'impose pas le signe. Il ne faut ni
déduire une unicité multi-filaments signés du seul résultat Lévy–Liu, ni
présenter une paire signée lisse sans swirl comme candidat de blow-up.

## 5. Critères critiques \(L^3\) : espace entier et tore

### 5.1 \(\mathbb R^3\) : raccord primaire établi

Trois résultats déjà catalogués suffisent :

- `NS-SRC-0010`, Kato (1984) : petite donnée solénoïdale dans
  \(L^3(\mathbb R^3)\), solution mild/forte globale unique ; le seuil est de
  taille \(c\nu\) sous la normalisation dimensionnelle usuelle ;
- `NS-SRC-0012`, Escauriaza–Seregin–Šverák (2003) : une borne
  \(L_t^\infty L_x^3\) empêche le blow-up ;
- `NS-SRC-0011`, Koch–Tataru (2001) : petite donnée dans
  \(BMO^{-1}(\mathbb R^3)\).

L'annulation de l'impulsion ne fournit aucune des petitesse requises. Pour
un profil fixé, la remise à l'échelle critique conserve \(\|u\|_3\), même
si le dipôle lointain est annulé. La contribution proche des cœurs peut
rester arbitrairement grande. Le seul raccord valide est quantitatif : si la
norme \(L^3\) de la somme signée elle-même est sous le seuil de Kato, alors
la solution est globale. Aucune cancellation de moment ne remplace cette
hypothèse.

### 5.2 \(\mathbb T^3\) : résultat standard, source exacte non verrouillée

Kato 1984 énonce son résultat sur \(\mathbb R^m\) ; le citer directement
pour le tore serait une erreur de domaine. Une adaptation périodique par le
semi-groupe de Stokes est standard pour une donnée de moyenne nulle (la
moyenne constante se retire par transformation galiléenne), sur un tore de
période fixée. Cependant :

- la veille ciblée n'a pas trouvé un article primaire dont le texte contrôlé
  énonce précisément la petite donnée \(L^3(\mathbb T^3)\) ;
- Giga–Miyakawa, *Solutions in \(L^r\) of the Navier–Stokes initial value
  problem*, Arch. Rational Mech. Anal. 89 (1985), 267–281, DOI
  [10.1007/BF00276875](https://doi.org/10.1007/BF00276875), est un candidat
  de raccord par théorie de Stokes, mais son application périodique exacte
  n'a pas été vérifiée dans le texte primaire ;
- les résultats périodiques en algèbre de Wiener, par exemple
  [arXiv:2205.12383](https://arxiv.org/abs/2205.12383), portent sur un autre
  espace et ne sourcent pas le théorème \(L^3\) demandé ;
- changer l'échelle change aussi la période du tore. Toute affirmation de
  seuil « critique uniforme » doit fixer la géométrie et suivre la
  dépendance en \(\nu\) et en période.

Verdict : le raccord périodique peut être enregistré comme
`AI_DERIVATION`/lemme standard à démontrer, mais pas comme conséquence
littérale de `NS-SRC-0010`. Ne pas ajouter Giga–Miyakawa avant audit du
texte intégral et du domaine exact.

## 6. Test adverse log-BMO pour une paire signée visqueuse

Dans Navier–Stokes axisymétrique sans swirl,

\[
\eta=\frac{\omega^\theta}{r},\qquad
\partial_t\eta+u\cdot\nabla\eta
=\nu\left(\partial_r^2+\frac3r\partial_r+\partial_z^2\right)\eta.
\]

Prenons une donnée lisse compacte non triviale, impaire en \(z\), et
unisignée dans \(z>0\). Symétrie et signe sont préservés. Le principe du
maximum fort donne à tout \(t>0\) un signe strict dans chacun des deux
demi-espaces ouverts \(r>0,z>0\) et \(r>0,z<0\).

Fixons \(x_0\) dans le plan \(z=0\), avec \(r_0>0\), et
\(0<\rho<r_0/2\). Presque partout sur la moitié supérieure de
\(B_\rho(x_0)\), la direction vaut, selon la convention, \(-e_\theta\) ;
sur la moitié inférieure elle vaut \(+e_\theta\). La réflexion en \(z\)
conserve \(e_\theta\), échange les moitiés et change le signe. Donc

\[
\xi_{B_\rho(x_0)}=0,
\qquad
\fint_{B_\rho(x_0)}|\xi-\xi_{B_\rho(x_0)}|=1.
\]

La valeur choisie sur le plan où \(\omega=0\) est sans effet, puisque ce
plan est de mesure nulle. Il s'ensuit

\[
|\log\rho|\operatorname{MO}_{B_\rho(x_0)}(\xi)
=|\log\rho|\longrightarrow\infty.
\]

Le même contre-test détruit la norme localisée de Bradshaw–Grujić dès que
la coupure \(\psi\) vaut 1 sur une telle boule. Il ne contredit pas un
critère localisé sur une région située d'un seul côté du plan, ni les
critères qui ne comparent la direction qu'entre points de grande vorticité.

Pour Euler, la vorticité compacte reste transportée et peut conserver à
temps fini un corridor ouvert de vorticité nulle entre les supports. Le saut
ci-dessus est donc une conséquence de la diffusion visqueuse et ne doit pas
être importé tel quel dans les théorèmes inviscides de croissance.

### Test reproductible minimal

1. Initialiser deux tores lisses réfléchis en \(z\), de signes opposés, avec
   \(\nabla\cdot\omega=0\) contrôlée.
2. Pour chaque temps positif, échantillonner des boules centrées en
   \((r_0,\theta_0,0)\), \(\rho<r_0/2\), avec quadrature appariée sous
   \(z\mapsto-z\).
3. Mesurer séparément la moyenne vectorielle et l'oscillation moyenne ; le
   résidu certifié analytique attendu est
   \(|\xi_B|=0\), \(\operatorname{MO}_B=1\).
4. Un résidu numérique non nul doit être expliqué par l'erreur de symétrie,
   de divergence, de quadrature ou par un seuil artificiel appliqué à
   \(|\omega|\), avant toute interprétation PDE.

## 7. Recommandations précises pour `sources.json`

Le fichier n'est pas modifié dans cette revue. Les identifiants ci-dessous
sont provisoires et doivent être attribués après relecture du `HEAD`.

### Entrées réellement nécessaires, priorité haute

| ID provisoire | Métadonnées minimales | Vérification et portée à encoder |
|---|---|---|
| `NS-SRC-0113` | Choi; Jeong, titre ci-dessus, 2025, AJM 147(5), 1251–1284, DOI `10.1353/ajm.2025.a971091`, arXiv `2110.09079v2` | `published`; Euler 3D, \(\mathbb R^3\), axisymétrique sans swirl, anti-parallèle ; croissance du moment supérieur et inflation d'enstrophie \(\nu\to0\) ; aucun blow-up NS à \(\nu>0\). Vérification : texte arXiv v2 + métadonnées publiées ciblées. |
| `NS-SRC-0114` | Lim; Jeong, titre ci-dessus, 2025, ARMA 249:32, DOI `10.1007/s00205-025-02103-1`, arXiv `2409.19497v2` | `published`; Euler 3D sans swirl ; borne supérieure \(t^{4/3}\), sans hypothèse de signe ; constante dépendant des quatre quantités initiales explicitées ci-dessus. Vérification : texte primaire Springer/arXiv. |
| `NS-SRC-0115` | Gustafson; Miller; Tsai, titre ci-dessus, 2026, JMFM 28(1):19, DOI `10.1007/s00021-026-01001-0`, arXiv `2303.12043v1` | `published`; Euler axisymétrique sans swirl \(d\ge3\) ; paire signée ; borne \(t^{3/4-\varepsilon}\) en 3D sous les hypothèses exactes du théorème 1.4. Vérification : texte arXiv + journal reference/DOI. |
| `NS-SRC-0116` | Egamberganov; Yao, titre ci-dessus, 2025, arXiv `2512.13456v1` | `preprint`; Euler 3D sans swirl ; moment \(t/\log t\), limsup \(L^p\) \(t^{1/4}\), identité de dérivée et évasion radiale ; `PREPRINT_CLAIM`. Vérification : texte arXiv v1, aucune revue identifiée. |
| `NS-SRC-0117` | Cao; Fan; Qin, titre courant ci-dessus, 2025–2026, arXiv `2511.03171v4` | `preprint`; Euler 3D anti-parallèle ; croissance superlinéaire du moment et rayon linéaire en densité dyadique ; noter explicitement `v2 withdrawn`, `v4 current`; `PREPRINT_CLAIM`. |

Ces cinq entrées sont nécessaires pour que la carte actuelle des anneaux
signés ne s'arrête pas aux bornes de 2021–2023 et pour enregistrer les
changements de statut publiés en 2025–2026.

### Entrées utiles mais non nécessaires à ce verrou

- García–Hassainia–Hmidi, arXiv `2603.21644v1` : utile à la veille générale
  des anneaux, mais géométrie leapfrogging Euler différente ; priorité basse.
- Saffman 1981, DOI `10.1017/S0022112081001511` : utile pour l'historique de
  l'impulsion ; n'ajouter avec niveau supérieur à `metadata_only` qu'après
  contrôle du PDF et de la formule exacte.
- Giga–Miyakawa 1985, DOI `10.1007/BF00276875` : ne pas ajouter comme source
  périodique \(L^3\) avant vérification primaire du domaine et du théorème.

### Aucune nouvelle entrée nécessaire

Kato, Escauriaza–Seregin–Šverák, Koch–Tataru, Feng–Šverák,
Gallay–Šverák, Lévy–Liu, Majda–Bertozzi, Bradshaw–Grujić et les deux
prépublications récentes de Grujić sont déjà catalogués. Le présent audit
change leur raccord logique, pas leurs métadonnées.

## 8. Classification et décision scientifique

| Affirmation | Niveau justifié |
|---|---|
| Annulation de \(\int\omega\), antisymétrie du premier moment, coefficient dipolaire | `AI_DERIVATION`, calcul exact autoporté |
| \(I=0\Rightarrow u=O(|x|^{-4})\) sous support compact et second moment fini | `AI_DERIVATION`, reste de Taylor explicitement bornable |
| \(I=0\Rightarrow u\) compacte ou petite dans \(L^3\) | Faux ; contre-implication éliminée |
| Borne \(t^{4/3}\) de Lim–Jeong | `PAPER_PROOF`, Euler sans swirl uniquement |
| Résultats Choi–Jeong et Gustafson–Miller–Tsai | `PAPER_PROOF`, Euler signé et croissance à temps infini |
| Résultats Egamberganov–Yao et Cao–Fan–Qin | `PREPRINT_CLAIM` |
| Blow-up Navier–Stokes issu de ces anneaux | Non établi ; incompatible avec la régularité globale de la classe sans swirl lisse |
| Échec log-BMO sur une boule coupant le plan de signe à \(t>0\) | `ANALYTIC_PROOF`, symétrie + principe du maximum |
| Petite donnée \(L^3(\mathbb R^3)\) | `PAPER_PROOF`, Kato (`NS-SRC-0010`) |
| Petite donnée \(L^3(\mathbb T^3)\) | Mathématiquement standard, mais raccord primaire exact non sourcé dans cette passe |

Décision recommandée pour le verrou actif : **réviser** toute stratégie qui
utilise l'impulsion nulle comme substitut à la petitesse critique ou à une
cohérence directionnelle. Le lemme falsifiable qui subsiste est :

> Sous annulation de l'impulsion, quantifier séparément la contribution
> proche des cœurs à \(\|u\|_{L^3}\) et la queue \(O(|x|^{-4})\) ; aucune
> conclusion de Kato n'est permise sans une borne de petitesse sur la norme
> totale.

La prochaine expérience décisive devrait construire une famille de paires
signées d'impulsion exactement nulle, normalisée à norme \(L^3\) fixée, et
mesurer séparément cœur, zone d'interaction et queue multipolaire. Le test
doit démontrer quantitativement que la cancellation lointaine laisse le
coefficient critique du cœur inchangé. En parallèle analytique, le raccord
périodique \(L^3\) doit être soit sourcé dans un texte primaire, soit dérivé
comme lemme de semigroupe avec constantes explicites en \(\nu\) et en
période.
