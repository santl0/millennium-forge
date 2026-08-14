# Revue bibliographique contradictoire — cycle 0014

Date de vérification : 2026-08-14
Objet : passage « 3D \(\delta\)-sparse \(\Rightarrow\) 1D \(\delta^{1/3}\)-sparse » et chaîne de mesure harmonique dans [arXiv:2607.08866v2](https://arxiv.org/abs/2607.08866).

## Verdict exécutif

1. Le passage **au même point et au même rayon**
   \[
   \frac{|S\cap B_r(x_0)|}{|B_r|}\leq\delta_3
   \quad\Longrightarrow\quad
   \exists\nu\in\mathbb S^2:\
   \frac{\mathcal L^1(S\cap(x_0-r\nu,x_0+r\nu))}{2r}
   \leq \delta_3^{1/3}
   \]
   est correct, avec constante multiplicative exactement égale à 1. L'exposant et la constante sont optimaux, la boule concentrique étant un cas d'égalité.
2. Ce résultat porte sur une **tranche réelle par une droite passant par \(x_0\)**. Ce n'est ni une projection géométrique de \(S\), ni une tranche parallèle moyenne, ni la projection scalaire \(u\cdot e\) utilisée ensuite pour scalariser le champ analytique.
3. [Grujić 2013](https://arxiv.org/abs/1111.0217) définit et utilise directement la sparseness 1D par une telle tranche, puis applique le théorème extrémal de Solynin. Il **ne formule pas** la notion volumique 3D ni la réduction \(\delta\mapsto\delta^{1/3}\). La citation [18] de 2607.08866v2 est donc pertinente pour le critère 1D et la mesure harmonique, mais incomplète pour l'implication 3D \(\Rightarrow\) 1D.
4. Dans la chaîne primaire auditée, la première formulation explicite retrouvée est celle de Farhat–Grujić–Leitmeyer, arXiv:1603.08763v1 (2016), avec seulement **un rayon \(\rho\leq r\)**. La formulation exacte « même rayon \(r\) » apparaît explicitement dans Grujić–Xu, [arXiv:1903.03833v1](https://arxiv.org/abs/1903.03833) (9 mars 2019), puis dans Grujić–Xu, [arXiv:1911.00974v1](https://arxiv.org/abs/1911.00974) (3 novembre 2019) et sa version publiée de 2024.
5. 2607.08866v2 propage correctement \(\delta_3=3/4\) en densité linéaire \(\eta=(3/4)^{1/3}\), puis en vide relatif \(1-\eta\), et enfin dans la constante de Solynin. Aucun défaut de constante n'est trouvé sur **ce seul maillon**.
6. Au 2026-08-14, arXiv:2607.08866 est toujours en **v2**, déposée le 13 juillet 2026; aucune v3 n'est affichée. La date « August 11, 2026 » rendue dans le HTML n'est pas une nouvelle version arXiv : l'historique officiel reste v1 (9 juillet) puis v2 (13 juillet).

Statut du maillon audité : **LEMME VALIDÉ / ATTRIBUTION À RÉVISER**. Ce verdict ne valide pas les estimations amont (48)–(55), ni le théorème 7.4 dans son ensemble.

## 1. Objets à ne pas confondre

| Objet | Définition | Ce qu'il fournit | Suffisant pour le point \(x_0\) dans l'argument harmonique ? |
|---|---|---|---|
| Sparseness 3D | \(|S\cap B_r(x_0)|/|B_r|\leq\delta_3\) | Une densité volumique locale | Seulement après le lemme radial |
| Sparseness 1D faible | Il existe \(\nu\) tel que \(\mathcal L^1(S\cap(x_0-r\nu,x_0+r\nu))/(2r)\leq\eta\) | Une tranche sur une droite **passant par le même point** | Oui |
| Projection de l'ensemble | \(\pi_\nu(S)\subset\mathbb R\) | L'ombre de tout \(S\) sur un axe | Non; elle peut être grande malgré un volume arbitrairement petit |
| Tranche moyenne de Fubini | Moyenne des longueurs sur une famille de droites parallèles | Une bonne droite à un décalage non contrôlé | Non; la bonne droite peut ne pas passer par \(x_0\) |
| Projection scalaire du champ | \(F(z)=u(z,s)\cdot e\) | Une fonction holomorphe scalaire dont \(\Re F\) est harmonique | Oui, mais c'est une opération différente et postérieure |

Le vocabulaire de la phrase précédant (51) dans 2607.08866v2 (« 1D projections of the velocity field ») est donc ambigu. La géométrie utilise une **trace spatiale** de l'ensemble de superniveau; (57) utilise ensuite une **composante scalaire** du champ. Aucune des deux n'est la projection géométrique de l'ensemble étudiée dans l'article de 2001.

## 2. Chaîne historique primaire

### 2.1 Grujić 2001 : projection coordonnée, pas tranche 1D locale

Z. Grujić, *The geometric structure of the super-level sets and regularity for 3D Navier–Stokes equations*, Indiana Univ. Math. J. 50(3) (2001), 1309–1317, [doi:10.1512/iumj.2001.50.1900](https://doi.org/10.1512/iumj.2001.50.1900).

Cet antécédent utilise une **projection coordonnée sparse** et un principe de mesure plurisousharmonique dans des domaines produits. Grujić 2013 décrit lui-même cette contrainte de projection coordonnée dans son prologue. Elle est plus rigide et ne doit pas être identifiée à l'existence locale d'une direction de tranche passant par chaque \(x_0\).

### 2.2 Grujić 2013 : définition 1D et endgame harmonique

Z. Grujić, *A geometric measure-type regularity criterion for solutions to the 3D Navier–Stokes equations*, Nonlinearity 26(1) (2013), 289–296, [doi:10.1088/0951-7715/26/1/289](https://doi.org/10.1088/0951-7715/26/1/289); arXiv:1111.0217v5, déposé initialement le 1er novembre 2011, version finale du 8 novembre 2012.

- La définition 4.1 est exactement
  \[
  \frac{\mathcal L^1(S\cap(x_0-rd,x_0+rd))}{2r}\leq\delta_1
  \quad\text{pour au moins un }d\in\mathbb S^2.
  \]
- Le théorème 4.1 porte sur une solution régulière de Navier–Stokes incompressible 3D sur \(\mathbb R^3\), viscosité normalisée à 1, et sur les superniveaux de la **norme de la vitesse**. Il exige cette tranche 1D pour chaque \(x_0\), avec une direction et un rayon pouvant dépendre de \(x_0\).
- Après translation et rotation, la tranche devient le diamètre réel d'un disque complexe. Le fermé \(K\) est le complément du superniveau sur ce diamètre et vérifie \(|K|\geq2r(1-\delta_1)\).
- Le papier ne définit pas la sparseness volumique 3D et ne contient pas le passage \(\delta_3^{1/3}\).

### 2.3 Farhat–Grujić–Leitmeyer 2016–2017 : première occurrence explicite retrouvée

A. Farhat, Z. Grujić, K. Leitmeyer, *The space \(B^{-1}_{\infty,\infty}\), volumetric sparseness, and 3D NSE*, J. Math. Fluid Mech. 19 (2017), 515–523, [doi:10.1007/s00021-016-0288-z](https://doi.org/10.1007/s00021-016-0288-z); [arXiv:1603.08763v5](https://arxiv.org/abs/1603.08763).

- arXiv v1, 29 mars 2016 : « 3D \(\delta\)-sparse à l'échelle \(r\) » implique « 1D \(\delta^{1/3}\)-sparse à une échelle \(\rho\), pour un \(0<\rho\leq r\) ».
- v4–v5 ajoutent une indication de preuve par coordonnées polaires et scénario extrémal, mais conservent \(\rho\leq r\).
- L'article a un erratum, [doi:10.1007/s00021-016-0295-0](https://doi.org/10.1007/s00021-016-0295-0), concernant le lemme Besov/semi-mixing; rien dans l'erratum localisé ne modifie cette remarque géométrique.

Bradshaw–Farhat–Grujić, [arXiv:1704.05546v4](https://arxiv.org/abs/1704.05546), publié dans Arch. Ration. Mech. Anal. 231 (2019), 1983–2005, [doi:10.1007/s00205-018-1314-5](https://doi.org/10.1007/s00205-018-1314-5), reprend encore la version « un \(\rho\in(0,r]\) ».

### 2.4 Grujić–Xu 2019–2024 : formulation au même rayon

La première occurrence primaire **au même rayon** retrouvée dans cette chaîne est Grujić–Xu, *A regularity criterion for 3D NSE in dynamically restricted local Morrey spaces*, [arXiv:1903.03833v1](https://arxiv.org/abs/1903.03833), 9 mars 2019; publié dans Applicable Analysis 101(16) (2022), 5809–5823, [doi:10.1080/00036811.2021.1906418](https://doi.org/10.1080/00036811.2021.1906418). Le texte affirme explicitement
\[
\text{3D }\delta\text{-sparse à }r
\Longrightarrow
\text{1D }\delta^{1/3}\text{-sparse à }r.
\]

La généralisation en dimension \(d\), avec \(\delta^{1/d}\) au même rayon, apparaît dès [arXiv:1911.00974v1](https://arxiv.org/abs/1911.00974), puis dans la version publiée : Z. Grujić, L. Xu, *Asymptotic Criticality of the Navier–Stokes Regularity Problem*, J. Math. Fluid Mech. 26, 53 (2024), [doi:10.1007/s00021-024-00888-x](https://doi.org/10.1007/s00021-024-00888-x), définitions 1.1–1.2.

Ainsi, la source naturelle de la phrase de 2607.08866v2 est la chaîne 2016–2024, notamment sa propre référence [19], plutôt que la seule référence [18] de 2013.

## 3. Preuve indépendante avec constante suivie

Statut : **dérivation interne auditée**, pas attribution automatique à un article.

On translate \(x_0\) en 0 et on pose, pour \(\theta\in\mathbb S^{d-1}\),
\[
L(\theta)=\int_{-r}^{r}\mathbf 1_S(t\theta)\,dt.
\]
La formule polaire, où le facteur \(1/2\) corrige le double comptage des droites orientées, donne
\[
|S\cap B_r|
=\frac12\int_{\mathbb S^{d-1}}\int_{-r}^{r}
\mathbf 1_S(t\theta)|t|^{d-1}\,dt\,d\sigma(\theta).
\]
À longueur \(L(\theta)\) fixée, l'intégrale pondérée est minimale lorsque la tranche occupe l'intervalle centré de longueur \(L(\theta)\). Par conséquent,
\[
\int_{-r}^{r}\mathbf 1_S(t\theta)|t|^{d-1}\,dt
\geq 2\int_0^{L(\theta)/2}t^{d-1}\,dt
=\frac{L(\theta)^d}{2^{d-1}d}.
\]
Si toutes les directions vérifiaient \(L(\theta)>2r\delta^{1/d}\), alors
\[
|S\cap B_r|
>\frac{|\mathbb S^{d-1}|}{d}r^d\delta
=|B_r|\delta,
\]
contradiction. Il existe donc une direction avec \(L(\theta)/(2r)\leq\delta^{1/d}\). En dimension trois, la constante est exactement 1 et l'exposant est \(1/3\).

**Optimalité.** Pour \(S\cap B_r(x_0)=B_{\delta^{1/3}r}(x_0)\), la fraction volumique vaut \(\delta\) et chaque droite passant par \(x_0\) a une densité linéaire exactement \(\delta^{1/3}\). Aucun facteur strictement plus petit, uniforme en \(S\), n'est possible.

## 4. Constantes de la chaîne (55) → (58)

Notons \(U=\|u(s)\|_\infty\), \(L=\log(e+\lambda U)\), \(v_3=4\pi/3\), et supposons (55) sous la forme
\[
|V_s|\leq B_s:=\frac{C}{\lambda^3U^3L^3}.
\]
Pour rendre l'argument sans notation asymptotique, il suffit de **choisir**
\[
r_s=\left(\frac{B_s}{\delta_3v_3}\right)^{1/3}
=\left(\frac{C}{\delta_3v_3}\right)^{1/3}
\frac{1}{\lambda U L}.
\]
Alors, pour tout \(x_0\),
\[
\frac{|V_s\cap B_{r_s}(x_0)|}{|B_{r_s}|}
\leq\frac{|V_s|}{v_3r_s^3}\leq\delta_3.
\]
Le point logique important est que cette propriété vaut pour **ce rayon choisi** (et pour les rayons plus grands), pas pour tout rayon inférieur à la borne affichée dans (56). Une fois \(\lambda\), \(C\) et \(\delta_3\) fixés, le \(c_4\) de (56) peut absorber exactement \((C/(\delta_3v_3))^{1/3}\lambda^{-1}\).

Avec \(\delta_3=3/4\), le lemme donne
\[
\eta=\delta_3^{1/3}=(3/4)^{1/3},
\qquad |K|\geq2r_s(1-\eta).
\]
Le théorème 2.1 cité dans Grujić 2013 est le résultat de A. Yu. Solynin, *Ordering of sets, hyperbolic metric, and harmonic measure*, Zap. Nauchn. Sem. POMI 237 (1997), 129–147; traduction J. Math. Sci. 95(3) (1999), 2256–2266, [doi:10.1007/BF02172470](https://doi.org/10.1007/BF02172470). Pour un fermé \(K\subset[-1,1]\), \(|K|=2\alpha_K\), \(0\notin K\),
\[
\omega(0,\mathbb D\setminus K,K)
\geq \frac2\pi\arcsin
\frac{1-(1-\alpha_K)^2}{1+(1-\alpha_K)^2}.
\]
Si \(|K|\geq2(1-\eta)\), la monotonie de la mesure harmonique (ou le choix d'un sous-compact de longueur exacte) donne
\[
h^*=\frac2\pi\arcsin\frac{1-\eta^2}{1+\eta^2}
=\frac2\pi\arcsin\frac{1-(3/4)^{2/3}}{1+(3/4)^{2/3}},
\]
qui est bien (53). Vérification numérique indépendante :

| Quantité | Valeur |
|---|---:|
| \(\eta=(3/4)^{1/3}\) | 0.908560296416070 |
| \(1-\eta\) | 0.091439703583930 |
| \(h^*\) | 0.060954683483033 |
| \(M=(1-h^*/2)/(1-h^*)\) | 1.032455666628061 |
| \(\lambda=1/(2M)\) | 0.484282295270818 |

La relation \(\tfrac12h^*+(1-h^*)M=1\) est satisfaite par construction. Les paramètres de (53), (57) et (58) sont donc cohérents entre eux.

## 5. Tests adverses reproductibles

### Test A — saturation de la constante

Prendre \(r=1\), \(x_0=0\), \(S=B_{(3/4)^{1/3}}(0)\). On obtient exactement
\[
\frac{|S|}{|B_1|}=\frac34,
\qquad
\frac{\mathcal L^1(S\cap(-\nu,\nu))}{2}=(3/4)^{1/3}
\quad\text{pour tout }\nu.
\]
Ce test réfute toute amélioration uniforme de \(\delta^{1/3}\) et confirme le facteur 1.

### Test B — réfutation des variantes « projection » et « direction prescrite »

Prendre dans \(B_r(0)\) un cylindre de rayon \(\varepsilon r\) autour de l'axe \(e_1\). Sa fraction volumique tend vers 0 comme \(O(\varepsilon^2)\), tandis que sa projection sur l'axe \(e_1\) et sa tranche centrale dans la direction prescrite \(e_1\) occupent presque tout \((-r,r)\). La petitesse volumique ne contrôle donc ni une projection, ni une direction fixée. Le lemme reste vrai parce qu'il choisit une direction transverse, dont la densité est \(O(\varepsilon)\).

### Test C — piège de Fubini

Une moyenne sur les droites parallèles à \(e_1\) fournit éventuellement une droite peu occupée, mais son décalage transverse est libre. Elle ne garantit rien pour la droite parallèle passant par \(x_0\). Le calcul radial de la section 3 est indispensable pour conserver le centre \(x_0\).

Résidu certifié de ces tests : **0 au niveau symbolique**; aucune discrétisation ni arithmétique flottante n'intervient dans la preuve. Les valeurs décimales ci-dessus servent seulement de contrôle secondaire.

## 6. Audit de version de 2607.08866

L'[historique arXiv officiel](https://arxiv.org/abs/2607.08866) consulté le 2026-08-14 indique :

- v1 : 9 juillet 2026, 18:38:04 UTC;
- v2 : 13 juillet 2026, 15:30:27 UTC;
- commentaire v2 : corrections typographiques et reformulations de clarté;
- aucune v3 et aucun statut de publication évaluée par les pairs indiqué.

Le manuscrit doit donc rester enregistré comme **prépublication arXiv v2, non auditée par les pairs à notre connaissance**. La date interne rendue par le HTML expérimental ne remplace pas l'horodatage de version.

## 7. Recommandations pour le graphe de preuves

- Enregistrer comme nœud séparé le lemme géométrique mesurable, valable en dimension \(d\), avec constante 1 et preuve radiale ci-dessus.
- Relier la définition/condition 1D et l'endgame harmonique à Grujić 2013; relier la réduction volumique à Farhat–Grujić–Leitmeyer 2016–2017 puis à la formulation même-échelle de Grujić–Xu 2019/2024.
- Remplacer dans toute paraphrase « projection 1D de l'ensemble » par « tranche sur une droite passant par \(x_0\) ».
- Dans l'audit de 2607.08866v2, considérer le maillon (55) \(\Rightarrow\) sparseness 1D comme **validé conditionnellement à (55)**, avec le rayon explicite de la section 4.
- Maintenir ouverts et indépendants les audits des estimations amont qui produisent (49) et (55), de la constante uniforme \(C\), et du choix temporel \(s=t+T_t<T^*\); le présent contrôle ne les résout pas.
