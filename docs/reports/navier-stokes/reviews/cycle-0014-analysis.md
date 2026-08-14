# Revue d'analyse géométrique — cycle 0014

## Verdict

Le lemme de restriction est **vrai**, dans toute dimension entière
\(d\geq1\), avec constante exactement égale à \(1\).

Soient \(r>0\), \(x_0\in\mathbb R^d\), \(0\leq\delta\leq1\), et
\(S\subset\mathbb R^d\) mesurable. Si

\[
\frac{|S\cap B_r(x_0)|}{|B_r|}\leq\delta,
\tag{1}
\]

alors il existe une direction \(\nu\in\mathbb S^{d-1}\), dont la section
est mesurable, telle que

\[
\boxed{
\frac1{2r}
\left|\left\{t\in(-r,r):x_0+t\nu\in S\right\}\right|
\leq\delta^{1/d}.}
\tag{2}
\]

En dimension trois, l'exposant est \(1/3\), sans facteur géométrique
supplémentaire. La boule concentrique

\[
S\cap B_r(x_0)=B_{\delta^{1/d}r}(x_0)
\tag{3}
\]

sature (1)–(2) dans toutes les directions. La constante \(1\) et
l'exposant \(1/d\) sont donc optimaux.

Le passage des lignes 348–349 de
[arXiv:2607.08866v2](https://arxiv.org/html/2607.08866v2) est valide.
L'application des lignes 393–397 au majorant global de \(|V_s|\) est
également valide après avoir **défini explicitement** le rayon. Pour
\(\delta=3/4\) et \(\omega_3=|B_1|=4\pi/3\), on a
\(\delta\omega_3=\pi\). Si

\[
|V_s|
\leq
A_s
:=
\frac{C_V}
{\lambda^3U_s^3
\log^3(e+\lambda U_s)},
\qquad
U_s=\|u(s)\|_\infty,
\tag{4}
\]

alors le choix

\[
\boxed{
R_s
=
\left(\frac{A_s}{\pi}\right)^{1/3}
=
\frac{(C_V/\pi)^{1/3}}
{\lambda U_s\log(e+\lambda U_s)}
}
\tag{5}
\]

rend \(V_s\) \(3/4\)-sparse dans \(B_{R_s}(x_0)\), pour **tout**
\(x_0\).

Le sens des quantificateurs doit toutefois être corrigé dans la prose du
manuscrit. À partir du seul volume global, la condition suffisante est

\[
r^3\geq\frac{|V_s|}{\delta\omega_3}.
\tag{6}
\]

Une borne supérieure \(r_s\leq R_s\), prise isolément, ne garantit pas la
sparseness : les rayons plus petits peuvent avoir densité \(1\). La formule
(56) du manuscrit est légitime si \(r_s\) désigne le rayon minimal construit
avec le volume réel, ou si l'on choisit directement \(r_s=R_s\). Elle est
fausse si elle est lue comme « tout rayon inférieur au membre droit
convient ».

Cet audit valide uniquement le maillon géométrique et son application
conditionnelle à (4). Il ne valide pas les estimations PDE qui produisent
(4), ni le théorème final de la prépublication.

## 1. Notations, sections et mesurabilité

Notons

\[
\sigma_{d-1}=|\mathbb S^{d-1}|,
\qquad
\omega_d=|B_1|=\frac{\sigma_{d-1}}{d}.
\tag{7}
\]

Pour une direction orientée \(\nu\in\mathbb S^{d-1}\), posons

\[
A_\nu
=
\{t\in(-r,r):x_0+t\nu\in S\},
\qquad
L(\nu)=\frac{|A_\nu|}{2r}.
\tag{8}
\]

Les directions \(\nu\) et \(-\nu\) paramètrent la même droite et

\[
L(-\nu)=L(\nu).
\tag{9}
\]

### Ensemble ouvert ou borélien

Si \(S\) est ouvert, \(A_\nu\) est ouvert dans \((-r,r)\) pour toute
direction. Si \(S\) est borélien, \(A_\nu\) est borélien. Dans les deux
cas, la longueur de (8) est définie pour tout \(\nu\), et Tonelli montre
que \(\nu\mapsto L(\nu)\) est mesurable.

### Ensemble seulement Lebesgue-mesurable

Une section exceptionnelle d'un ensemble Lebesgue-mesurable de
\(\mathbb R^d\) n'est pas nécessairement mesurable en dimension un. En
dimension \(d\geq2\), tout sous-ensemble, même non mesurable sur la droite,
d'une droite fixée est contenu dans un ensemble de mesure
\(d\)-dimensionnelle nulle et appartient à la complétion de la mesure de
Lebesgue de \(\mathbb R^d\).

Ce défaut n'affecte pas l'énoncé existentiel. Choisissons un représentant
borélien \(S_B\) tel que

\[
|S\mathbin{\triangle}S_B|=0.
\tag{10}
\]

La formule polaire appliquée à
\(N=S\mathbin{\triangle}S_B\) donne

\[
\int_{\mathbb S^{d-1}}\int_{-r}^{r}
\mathbf1_N(x_0+t\nu)|t|^{d-1}\,dt\,d\sigma(\nu)=0.
\tag{11}
\]

Pour presque toute direction, la section de \(N\) a donc longueur nulle.
En effet, le poids est strictement positif pour \(t\neq0\), et l'on peut
épuiser \((-r,r)\setminus\{0\}\) par les ensembles
\(\{|t|\geq1/n\}\). Sur ces directions, la section de \(S\) est mesurable
et coïncide presque partout avec celle de \(S_B\).

Le sous-ensemble de directions satisfaisant (2) pour \(S_B\) a une mesure
angulaire positive : s'il était nul, on aurait
\(L(\nu)^d>\delta\) presque partout, en contradiction avec la moyenne
(24). Il rencontre donc l'ensemble de mesure pleine des directions pour
lesquelles les sections de \(S\) et \(S_B\) coïncident. Ainsi le lemme
fournit une direction admissible pour \(S\). Pour éviter toute ambiguïté,
la version la plus propre suppose \(S\) borélien ou ouvert ; dans
l'application à \(V_s\), l'ensemble est ouvert.

## 2. Inégalité unidimensionnelle optimale

### Lemme de réarrangement croissant

Soit \(E\subset(-r,r)\) mesurable, de longueur

\[
|E|=m=2r\ell,
\qquad 0\leq\ell\leq1.
\tag{12}
\]

Alors, pour tout entier \(d\geq1\),

\[
\boxed{
\int_E|t|^{d-1}\,dt
\geq
\frac{2}{d}(r\ell)^d
=
\frac{m^d}{d\,2^{d-1}}.}
\tag{13}
\]

Le poids \(|t|^{d-1}\) est croissant avec la distance à l'origine. Parmi
les ensembles de longueur \(m\), son intégrale est donc minimale sur
l'intervalle centré

\[
E^*=(-m/2,m/2)=(-r\ell,r\ell).
\tag{14}
\]

Le calcul de la constante est

\[
\int_{-r\ell}^{r\ell}|t|^{d-1}\,dt
=2\int_0^{r\ell}t^{d-1}\,dt
=\frac{2}{d}(r\ell)^d.
\tag{15}
\]

Une preuve sans invocation abstraite du réarrangement consiste à comparer
\(E\setminus E^*\) et \(E^*\setminus E\). Ces deux ensembles ont même
mesure ; le poids est au moins \((r\ell)^{d-1}\) sur le premier et au plus
cette valeur sur le second.

Pour \(d>1\), le poids est strictement croissant en \(|t|\), et l'égalité
dans (13) impose

\[
E=E^*
\quad\text{modulo un ensemble de longueur nulle}.
\tag{16}
\]

Pour \(d=1\), le poids vaut \(1\) : (13) est une identité pour tout
ensemble \(E\), sans unicité de l'extrémiseur.

### Constante en dimension trois

Lorsque \(d=3\),

\[
\boxed{
\int_E t^2\,dt\geq\frac{m^3}{12}.}
\tag{17}
\]

En effet, \(m^3/(3\cdot2^2)=m^3/12\). Cette constante \(1/12\) est le
coefficient qui doit apparaître avant la formule polaire.

## 3. Formule polaire symétrisée

La paramétrisation signée

\[
(t,\nu)\longmapsto x_0+t\nu,
\qquad
t\in(-r,r),\quad \nu\in\mathbb S^{d-1},
\tag{18}
\]

couvre chaque point de \(B_r(x_0)\setminus\{x_0\}\) deux fois. Par
conséquent,

\[
\boxed{
|S\cap B_r(x_0)|
=
\frac12
\int_{\mathbb S^{d-1}}\int_{-r}^{r}
\mathbf1_S(x_0+t\nu)|t|^{d-1}\,dt\,d\sigma(\nu).}
\tag{19}
\]

Appliquons (13) à \(E=A_\nu\), dont la longueur est
\(2rL(\nu)\). On obtient

\[
\int_{-r}^{r}
\mathbf1_S(x_0+t\nu)|t|^{d-1}\,dt
\geq
\frac{2r^d}{d}L(\nu)^d.
\tag{20}
\]

Après intégration angulaire,

\[
|S\cap B_r(x_0)|
\geq
\frac{r^d}{d}
\int_{\mathbb S^{d-1}}L(\nu)^d\,d\sigma(\nu).
\tag{21}
\]

Puisque

\[
|B_r|=\omega_dr^d=\frac{\sigma_{d-1}}d r^d,
\tag{22}
\]

la forme normalisée exacte est

\[
\boxed{
\frac{|S\cap B_r(x_0)|}{|B_r|}
\geq
\frac1{\sigma_{d-1}}
\int_{\mathbb S^{d-1}}L(\nu)^d\,d\sigma(\nu).}
\tag{23}
\]

Le sens de (23) est important : la densité volumique contrôle par le haut
la moyenne angulaire de la puissance \(d\) des densités linéaires.

## 4. Preuve du lemme et quantificateurs

Sous l'hypothèse (1), (23) donne

\[
\frac1{\sigma_{d-1}}
\int_{\mathbb S^{d-1}}L(\nu)^d\,d\sigma(\nu)
\leq\delta.
\tag{24}
\]

Il existe donc une direction telle que

\[
L(\nu)^d\leq\delta.
\tag{25}
\]

Sinon \(L(\nu)^d>\delta\) pour presque toute direction et l'intégrale de
la fonction strictement positive
\(L^d-\delta\) serait strictement positive, en contradiction avec (24).
L'inégalité (25) est exactement (2).

Le quantificateur obtenu est

\[
\forall x_0,\ \forall r>0,\ \forall S
\text{ admissible vérifiant (1)},\
\exists\nu=\nu(S,x_0,r).
\tag{26}
\]

Le lemme ne produit pas une direction unique, continue en \(x_0\), ni
indépendante du temps. L'application par mesure globale ci-dessous produit
un même rayon pour tous les centres, mais la direction peut dépendre du
centre.

### Formule spécialisée à \(d=3\)

Notons \(m(\nu)=|A_\nu|=2rL(\nu)\). Les constantes deviennent

\[
|S\cap B_r|
\geq
\frac1{24}\int_{\mathbb S^2}m(\nu)^3\,d\sigma(\nu)
=
\frac{r^3}{3}
\int_{\mathbb S^2}L(\nu)^3\,d\sigma(\nu).
\tag{27}
\]

Comme \(|B_r|=4\pi r^3/3\),

\[
\frac{|S\cap B_r|}{|B_r|}
\geq
\frac1{4\pi}
\int_{\mathbb S^2}L(\nu)^3\,d\sigma(\nu).
\tag{28}
\]

Il n'y a ni facteur \(2\), ni \(3\), ni \(4\pi\) résiduel dans le seuil
\(\delta^{1/3}\).

## 5. Cas limites, égalité et optimalité

### Valeurs de \(\delta\)

- Si \(\delta=0\), (24) impose \(L=0\) presque partout ; une direction de
  section nulle existe. Pour \(S\) ouvert, (1) implique même
  \(S\cap B_r(x_0)=\varnothing\).
- Si \(0<\delta<1\), le résultat non trivial est (2).
- Si \(\delta=1\), toute section satisfait \(L\leq1=\delta^{1/d}\).
- Pour \(\delta>1\), la conclusion est encore triviale puisque
  \(L\leq1<\delta^{1/d}\), mais le vocabulaire de densité sparse n'est plus
  pertinent.
- Une hypothèse avec \(\delta<0\) est impossible sauf convention vide.

### Extrémiseur radial

Posons \(q=\delta^{1/d}\) et

\[
S\cap B_r(x_0)=B_{qr}(x_0).
\tag{29}
\]

Alors

\[
\frac{|S\cap B_r|}{|B_r|}=q^d=\delta
\tag{30}
\]

et, pour toute direction,

\[
A_\nu=(-qr,qr),
\qquad
L(\nu)=q=\delta^{1/d}.
\tag{31}
\]

Ainsi on ne peut remplacer le coefficient \(1\) de (2) par une constante
strictement plus petite, ni l'exposant \(1/d\) par un exposant plus grand
sur \((0,1)\).

Si la densité volumique est strictement inférieure à \(\delta\), (24)
fournit une direction satisfaisant l'inégalité stricte

\[
L(\nu)<\delta^{1/d}.
\tag{32}
\]

Dans le cas extrémal où la densité vaut \(\delta\) et où aucune direction
n'a \(L<q\), on doit avoir \(L=q\) presque partout et l'égalité dans le
réarrangement (13) presque partout. Pour \(d>1\), les sections sont donc
les intervalles centrés \((-qr,qr)\) presque partout : l'extrémiseur est la
boule concentrique, modulo les ensembles nuls et les directions
exceptionnelles.

## 6. Loi d'échelle

Pour \(\kappa>0\), définissons

\[
S_\kappa
=x_0+\kappa(S-x_0),
\qquad
r_\kappa=\kappa r.
\tag{33}
\]

Alors

\[
\frac{|S_\kappa\cap B_{r_\kappa}(x_0)|}
{|B_{r_\kappa}|}
=
\frac{|S\cap B_r(x_0)|}{|B_r|}
\tag{34}
\]

et, pour chaque direction,

\[
\frac1{2r_\kappa}
\left|\{t\in(-r_\kappa,r_\kappa):
x_0+t\nu\in S_\kappa\}\right|
=L(\nu).
\tag{35}
\]

Le lemme est exactement invariant par translation et dilatation. Le
facteur \(1/d\) provient uniquement du jacobien radial
\(|t|^{d-1}\), et la racine \(d\)-ième est forcée par l'homogénéité entre
volume et longueur.

Si l'on ne connaît qu'un majorant global

\[
|S|\leq A,
\tag{36}
\]

un rayon uniforme pour tous les centres est

\[
\boxed{
R_A=\left(\frac{A}{\delta\omega_d}\right)^{1/d}.}
\tag{37}
\]

Sous une dilatation de facteur \(\kappa\), \(A\) est multiplié par
\(\kappa^d\) et \(R_A\) par \(\kappa\), comme requis.

## 7. Audit des lignes 348–397 de la prépublication

La source est Z. Grujić,
[*Logarithmic Depletion of Vortex Stretching and Singularity Evasion in
the 3D Navier–Stokes Equations*,
arXiv:2607.08866v2](https://arxiv.org/html/2607.08866v2),
prépublication de 2026 non évaluée ici dans son ensemble.

### Lignes 348–349 : restriction 3D vers 1D

La définition de la 3D \(\delta\)-sparseness est (1), et celle de la 1D
\(\delta\)-sparseness est (8). La phrase

\[
\text{3D \(\delta\)-sparse}
\quad\Longrightarrow\quad
\text{1D \(\delta^{1/3}\)-sparse au même rayon}
\tag{38}
\]

est correcte par (28). L'ouverture demandée dans la définition du
manuscrit est plus forte que nécessaire et élimine l'ambiguïté des
sections mesurables.

La conversion du complément linéaire est également correcte. Pour
\(q=\delta^{1/3}\), une section de \(S\) de longueur au plus \(2rq\)
laisse un complément de longueur au moins

\[
2r(1-q)=2r(1-\delta^{1/3}).
\tag{39}
\]

Avec \(\delta=3/4\), le paramètre des lignes 377–378 est donc

\[
\alpha=1-(3/4)^{1/3},
\tag{40}
\]

et \(1-\alpha=(3/4)^{1/3}\). Le carré apparaissant dans la borne de
Solynin est bien

\[
(1-\alpha)^2=(3/4)^{2/3}.
\tag{41}
\]

### Ligne 351 : ouverture du superniveau

À l'instant analytique \(s\), le champ \(u(\cdot,s)\) est continu. Le
superniveau

\[
V_s
=
\{x:|u(x,s)|>\lambda\|u(s)\|_\infty\}
\tag{42}
\]

est donc ouvert et mesurable. Le lemme s'applique sans choix de
représentant.

### Lignes 393–397 : du volume global au rayon local

Acceptons conditionnellement le majorant (55) du manuscrit, écrit sous la
forme (4). Pour tout \(x_0\) et tout \(r>0\),

\[
|V_s\cap B_r(x_0)|
\leq |V_s|
\leq A_s.
\tag{43}
\]

La condition suffisante pour une densité au plus \(\delta\) est donc

\[
A_s\leq\delta\omega_3r^3.
\tag{44}
\]

Avec \(\delta=3/4\) et \(\omega_3=4\pi/3\),

\[
\delta\omega_3=\pi.
\tag{45}
\]

Le choix (5) vérifie exactement

\[
\delta|B_{R_s}|
=\pi R_s^3
=A_s.
\tag{46}
\]

Ainsi, simultanément pour tous les centres,

\[
\frac{|V_s\cap B_{R_s}(x_0)|}
{|B_{R_s}|}
\leq\frac{A_s}{\omega_3R_s^3}
=\delta.
\tag{47}
\]

Le lemme fournit alors, pour chaque \(x_0\), au moins une direction
\(\nu_s(x_0)\) telle que

\[
\frac1{2R_s}
\left|
\{t\in(-R_s,R_s):
x_0+t\nu_s(x_0)\in V_s\}
\right|
\leq(3/4)^{1/3}.
\tag{48}
\]

Le rayon est uniforme en \(x_0\) ; la direction ne l'est pas et n'a pas
besoin de l'être pour une application ponctuelle du maximum harmonique.

### Deux définitions correctes du rayon

Le manuscrit peut être rendu exact de l'une des deux manières suivantes.

1. Utiliser le volume réel :
   \[
   r_s^\sharp
   =
   \left(\frac{|V_s|}{\pi}\right)^{1/3}
   \leq
   \frac{(C_V/\pi)^{1/3}}
   {\lambda U_s\log(e+\lambda U_s)}.
   \tag{49}
   \]
   Si \(|V_s|=0\), tout rayon positif convient et la définition
   dégénérée \(r_s^\sharp=0\) doit être remplacée par un choix arbitraire
   dans le rayon analytique.
2. Utiliser directement le majorant \(A_s\), en posant \(r_s=R_s\) comme
   dans (5). Ce rayon est positif et satisfait (47), y compris lorsque
   \(V_s\) est vide.

Dans la première convention, l'inégalité \(r_s^\sharp\leq R_s\) de type
(56) est correcte. Dans la seconde, on dispose d'une égalité explicite.
Dans aucune convention la propriété n'est affirmée pour tous les rayons
inférieurs.

## 8. Sens du rayon : test adverse

La condition obtenue du volume réel est

\[
r\geq
\left(\frac{|V_s|}{\delta\omega_3}\right)^{1/3}.
\tag{50}
\]

Elle va dans le sens opposé à la lecture « une échelle plus petite est
automatiquement plus sparse ». Considérons le contre-test

\[
S=B_\varepsilon(x_0),
\qquad 0<\varepsilon<r.
\tag{51}
\]

Pour tout \(0<\rho\leq\varepsilon\),

\[
\frac{|S\cap B_\rho(x_0)|}{|B_\rho|}=1,
\tag{52}
\]

donc aucun de ces petits rayons n'est \(\delta\)-sparse lorsque
\(\delta<1\). Le premier rayon certifié par le seul volume est

\[
\rho=\varepsilon\delta^{-1/3},
\tag{53}
\]

car

\[
\frac{|B_\varepsilon|}{|B_\rho|}
=\left(\frac{\varepsilon}{\rho}\right)^3
=\delta.
\tag{54}
\]

Ce contre-test ne réfute pas (49) : il réfute seulement l'usage d'une borne
supérieure sur un rayon non défini comme si tout rayon plus petit
préservait la sparseness.

## 9. Comparaison exacte avec le rayon analytique

Le manuscrit utilise le rayon analytique

\[
\rho_s=\frac{\nu}{c_3U_s}.
\tag{55}
\]

Avec le choix conservateur (5),

\[
\frac{R_s}{\rho_s}
=
\frac{c_3}{\nu\lambda}
\left(\frac{C_V}{\pi}\right)^{1/3}
\frac1{\log(e+\lambda U_s)}.
\tag{56}
\]

La condition suffisante exacte \(R_s\leq\rho_s\) est

\[
\log(e+\lambda U_s)
\geq
\frac{c_3}{\nu\lambda}
\left(\frac{C_V}{\pi}\right)^{1/3}.
\tag{57}
\]

Si \(C_V,c_3,\nu,\lambda\) sont uniformes et si
\(U_s\to\infty\) le long des temps d'échappement, le membre gauche finit
par satisfaire (57). Le rapport logarithmique annoncé aux lignes 398–399
est donc cohérent **conditionnellement** au majorant global et à
l'uniformité de ses constantes.

Deux précisions restent nécessaires.

1. La borne de distribution (49) du manuscrit est asymptotique aux grandes
   amplitudes. Son application au niveau
   \(\beta=\lambda U_s\) exige de choisir le temps assez proche du temps
   putatif de blow-up pour que \(\beta\) soit dans le régime où cette borne
   est prouvée.
2. Le logarithme doit porter sur une quantité sans dimension. Dans une
   formulation dimensionnée, il faut écrire par exemple
   \[
   \log\left(e+\frac{\lambda U_s}{U_*}\right)
   \tag{58}
   \]
   avec une vitesse de référence \(U_*>0\). L'écriture du manuscrit
   suppose implicitement une nondimensionnalisation.

Sous l'échelle Navier–Stokes

\[
u_\kappa(x,t)=\kappa u(\kappa x,\kappa^2t),
\tag{59}
\]

le volume d'un superniveau relatif est multiplié par
\(\kappa^{-3}\), et son rayon géométrique algébrique par
\(\kappa^{-1}\). Le facteur logarithmique ajoute précisément la correction
subcritique revendiquée ; il n'est compatible dimensionnellement qu'après
le choix d'une échelle de référence.

## 10. Passe contradictoire

1. **Poids radial oublié.** La moyenne brute des longueurs des sections
   n'est pas contrôlée directement par le volume. Le jacobien
   \(|t|^{d-1}\) est indispensable ; (13) le convertit en puissance
   \(L^d\).
2. **Double comptage.** La paramétrisation signée couvre chaque point deux
   fois. Le facteur \(1/2\) de (19) est nécessaire.
3. **Mauvaise constante 3D.** Le minimum est \(m^3/12\), puis le facteur
   polaire donne \(m^3/24\). Après normalisation, toutes les constantes
   géométriques s'annulent et la constante finale vaut \(1\).
4. **Centre fixé.** Le lemme exige que la droite passe par le centre du
   même ball \(B_r(x_0)\). Il ne produit pas une bonne droite translatée.
5. **Direction dépendante.** La direction peut dépendre de
   \(S,x_0,r\) et du temps. Aucune direction globale n'est démontrée.
6. **Sections pathologiques.** Pour un ensemble seulement
   Lebesgue-mesurable, certaines sections peuvent être non mesurables. Une
   bonne section existe néanmoins presque sûrement ; l'ouverture de
   \(V_s\) supprime ce problème.
7. **Égalité.** La boule concentrique sature la borne. Aucun gain uniforme
   sur \(\delta^{1/d}\) n'est possible.
8. **Rayon minimal.** Le contrôle par volume global s'améliore lorsque le
   rayon augmente. Une borne supérieure sur un rayon arbitraire est
   insuffisante.
9. **Uniformité spatiale.** Le même rayon fonctionne pour tous les centres
   uniquement parce que (43) utilise le volume global entier, pas une
   estimation locale centrée en un point privilégié.
10. **Portée PDE.** Le lemme ne certifie ni (4), ni l'analyticité, ni le
    choix des temps d'échappement, ni le maximum harmonique.
11. **Projection harmonique.** La phrase de la ligne 352 selon laquelle
    les projections 1D du champ sont « harmoniques » est imprécise. C'est
    la partie réelle d'une projection scalaire de l'extension holomorphe
    qui est harmonique, comme le manuscrit le formule correctement à la
    ligne 402.

## Conclusion

**Résultat positif borné.** Le passage

\[
\text{densité \(d\)-dimensionnelle }\leq\delta
\quad\Longrightarrow\quad
\text{une densité linéaire }\leq\delta^{1/d}
\tag{60}
\]

est démontré avec toutes les constantes, pour les ensembles ouverts,
boréliens et Lebesgue-mesurables au sens précisé. Il est invariant
d'échelle et optimal.

**Application à arXiv:2607.08866v2.** Le maillon des lignes 348–349 est
valide. Le passage des lignes 393–397 est valide si le rayon est défini
par (49) ou choisi par (5). Pour \(\delta=3/4\), la constante exacte issue
du volume de la boule est

\[
c_4=\frac1\lambda\left(\frac{C_V}{\pi}\right)^{1/3}.
\tag{61}
\]

**Correction requise.** Remplacer la formulation ambiguë
« le rayon requis satisfait \(r_s\lesssim|V_s|^{1/3}\) » par le choix
explicite

\[
r_s
=
\left(\frac{|V_s|}{\delta\omega_3}\right)^{1/3}
\quad\text{ou}\quad
r_s
=
\left(\frac{A_s}{\delta\omega_3}\right)^{1/3}.
\tag{62}
\]

**État : CONTINUER.** Le raccord géométrique survit à la passe adverse.
Le prochain verrou n'est pas la restriction 3D vers 1D, mais la validité
uniforme du majorant global (55), la dépendance exacte de \(C_V\), puis la
compatibilité complète du disque analytique avec le rayon choisi.
