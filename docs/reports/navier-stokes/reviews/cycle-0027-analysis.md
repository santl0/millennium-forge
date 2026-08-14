# Passe analytique indépendante — cycle 0027 : contreprofil axisymétrique div–curl

Date : 2026-08-14

Statut : **dérivation IA interne**, non publiée, non indépendante au sens inter-familles et jamais `PAPER_PROOF`

## Verdict

L’ansatz axisymétrique

\[
U=\psi(r,z)e_\theta,
\qquad
W=\nabla\times U,
\]

permet de lisser et de rendre exactement solénoïdale la famille abstraite « plateau axial positif large / retour axial négatif rare » du cycle 0026.

Il existe une famille `C_c^∞(R³)` supportée dans un tore fixe éloigné de l’axe, paramétrée par `0<ε≤1/4`, telle que, dans un domaine fixe `D`,

\[
c_K\leq
\|W_\varepsilon\|_{L^{3/2,\infty}}^*
\leq C_K,
\qquad
m_\varepsilon=4\pi\varepsilon^{1/3},
\]

et pour une extension admissible de la direction,

\[
c_{\rm MO}\varepsilon
\leq
\operatorname{MO}_D(\zeta_\varepsilon)
\leq
\frac{20}{21}\varepsilon.
\]

On peut prendre `c_MO=8/81` uniformément pour `0<ε≤1/4`.

Ainsi

\[
\operatorname{MO}_D(\zeta_\varepsilon)
\asymp
\frac{m_\varepsilon^3}
{K_\varepsilon^3|D|}.
\]

La puissance cubique reste donc optimale même dans la classe

\[
W\in C_c^\infty(\mathbb R^3),
\qquad
\operatorname{div}W=0,
\qquad
W=\operatorname{curl}U,
\qquad
U\in C_c^\infty,\ \operatorname{div}U=0.
\]

Le terme radial dû au cutoff en `z` n’est pas un résidu négligeable. Si son épaisseur vaut `δ`, il force exactement

\[
K\geq
\frac{4\pi}{3(14\pi)^{1/3}}
A\delta^{-1/3}
\simeq1.1866682057\,A\delta^{-1/3},
\]

et

\[
\operatorname{MO}_D(\zeta)
\geq
\frac{2\delta}{15+21\delta}.
\]

Avec `A=ε^{1/3}`, maintenir simultanément `K=O(1)` et `MO=O(ε)` impose `δ≍ε` dans cet ansatz séparable. C’est le no-go quantitatif du cycle.

Cette construction est une donnée initiale lisse admissible sur `R³`, mais pas une candidate au blow-up : son énergie et sa norme critique de vitesse `L³` tendent vers zéro. Elle teste et clôt le verrou cinématique div–curl, non le verrou dynamique de Navier–Stokes.

## 1. Cinématique exacte de l’ansatz

Dans les coordonnées cylindriques `(r,θ,z)`, avec indépendance en `θ`,

\[
U_r=U_z=0,
\qquad
U_\theta=\psi(r,z).
\]

La divergence de `U` est nulle et le curl exact est

\[
W_r=-\partial_z\psi,
\qquad
W_\theta=0,
\qquad
W_z=\frac1r\partial_r(r\psi).
\tag{1}
\]

Introduisons la fonction de flux méridienne

\[
F(r,z)=r\psi(r,z).
\]

Alors

\[
W_r=-\frac{F_z}{r},
\qquad
W_z=\frac{F_r}{r}.
\tag{2}
\]

Cette écriture donne sans raccourci

\[
\frac1r\partial_r(rW_r)+\partial_zW_z
=-\frac{F_{rz}}r+\frac{F_{zr}}r=0.
\tag{3}
\]

Le terme `ψ/r` de (1) est inclus dans `F_r/r`; le supprimer produirait un faux champ de vorticité.

## 2. Profils lisses et support fixe

Fixons une densité

\[
\beta\in C_c^\infty((0,1)),
\qquad
\beta>0\text{ sur }(0,1),
\qquad
\int_0^1\beta(s)ds=1,
\]

symétrique autour de `1/2` et possédant un plateau à sa valeur maximale

\[
B:=\|\beta\|_\infty
\quad\text{sur }[1/3,2/3].
\]

Posons

\[
\eta(s)=\int_s^\infty\beta(t)dt.
\]

Ainsi `η=1` sur `(-∞,0]`, `η=0` sur `[1,∞)` et `η'=-β`.

Pour `0<ε,δ≤1/4`, définissons

\[
p(r)=\beta(r-2),
\qquad
q_\varepsilon(r)
=\varepsilon^{-1}\beta\!\left(\frac{r-4}{\varepsilon}\right),
\tag{4}
\]

\[
h_\varepsilon(r)
=\int_{-\infty}^r
\bigl(p(s)-q_\varepsilon(s)\bigr)ds,
\tag{5}
\]

et

\[
\chi_\delta(z)
=\eta\!\left(\frac{z-1}{\delta}\right)
 \eta\!\left(\frac{-z-1}{\delta}\right).
\tag{6}
\]

Les normalisations de (4) donnent

\[
0\leq h_\varepsilon\leq1,
\qquad
h_\varepsilon=1\text{ sur }[3,4],
\qquad
\operatorname{supp}h_\varepsilon\subset[2,4+\varepsilon].
\tag{7}
\]

De même,

\[
\chi_\delta=1\text{ sur }[-1,1],
\qquad
\operatorname{supp}\chi_\delta
\subset[-1-\delta,1+\delta],
\tag{8}
\]

et ses deux transitions sont monotones, de longueur `δ` chacune.

Pour une amplitude `A>0`, posons

\[
F_{\varepsilon,\delta}
=A h_\varepsilon(r)\chi_\delta(z),
\qquad
\psi_{\varepsilon,\delta}
=\frac{F_{\varepsilon,\delta}}r.
\tag{9}
\]

Le support est contenu dans `2<r<4+ε`, `|z|<1+δ`. Comme il reste à distance positive de l’axe, l’expression cartésienne

\[
U=\psi\left(-\frac yr,\frac xr,0\right)
\]

étendue par zéro est dans `C_c^∞(R³;R³)`.

La vorticité exacte vaut

\[
\boxed{
W_r=-\frac{A}{r}h_\varepsilon(r)\chi_\delta'(z),
\qquad
W_\theta=0,
\qquad
W_z=\frac{A}{r}
\bigl(p(r)-q_\varepsilon(r)\bigr)
\chi_\delta(z).}
\tag{10}
\]

Dans la suite, le choix équilibré est

\[
\delta=\varepsilon,
\qquad
A=\varepsilon^{1/3}.
\tag{11}
\]

Pour `ε=n^{-3}`, l’amplitude positive est d’ordre `n^{-1}` et les amplitudes du retour axial et des calottes radiales sont d’ordre `n²`.

## 3. Flux, divergence et moyenne

### 3.1 Flux axial par tranche

Pour chaque `z`,

\[
\int_0^\infty W_z(r,z)rdr
=A\chi_\delta(z)
\int_0^\infty(p-q_\varepsilon)dr
=0.
\tag{12}
\]

Le retour négatif n’est donc pas seulement global : dans cet ansatz produit, il compense le plateau positif sur chaque tranche horizontale. Il est impossible de déplacer tout le retour axial vers des valeurs lointaines de `z` sans abandonner la séparabilité de (9).

### 3.2 Flux radial pondéré

Pour chaque `r`,

\[
\int_{\mathbb R}W_r(r,z)dz
=-\frac{Ah_\varepsilon(r)}r
\int_{\mathbb R}\chi_\delta'(z)dz
=0.
\tag{13}
\]

Après multiplication par `2πr`, (13) dit exactement que le flux radial à travers chaque cylindre coaxial complet est nul.

En particulier,

\[
\int_0^\infty\int_{\mathbb R}
W_r(r,z)r\,dzdr=0.
\tag{14}
\]

Les deux calottes de cutoff portent des flux radiaux scalaires opposés.

### 3.3 Moyenne vectorielle

L’intégration en `θ` annule exactement la composante `W_re_r` :

\[
\int_0^{2\pi}e_r(\theta)d\theta=0.
\]

L’intégrale de la composante axiale est nulle par (12). Ainsi

\[
\boxed{
\int_{\mathbb R^3}W_{\varepsilon,\delta}(x)dx=0.}
\tag{15}
\]

La condition de moyenne nulle du cycle 0026 est donc satisfaite exactement, et non après correction ou projection.

## 4. Plateau positif et retour rare

Fixons

\[
D=\{(r,\theta,z):1<r<6,\ |z|<3\},
\qquad
|D|=210\pi,
\tag{16}
\]

et `e=e_z`, `α=1`.

Sur

\[
P=\{2<r<3,\ |z|<1\},
\]

on a `W=W_ze_z` avec `W_z>0`. Le sous-anneau correspondant au plateau de `β` a une mesure tridimensionnelle fixe et une amplitude comprise entre des multiples fixes de `A`.

Sur

\[
N_\varepsilon
=\{4<r<4+\varepsilon,\ |z|<1\},
\]

on a `W=-|W|e_z`. Sa mesure exacte est

\[
|N_\varepsilon|
=16\pi\varepsilon+2\pi\varepsilon^2,
\tag{17}
\]

tandis que son amplitude maximale est d’ordre `A/ε`.

Le cône

\[
G=\{W\neq0:\xi\cdot e_z\geq1\}
\]

coïncide presque partout avec `P`. En effet, dans les transitions de `χ_δ`, le terme radial de (10) est non nul. Par intégration cylindrique,

\[
\boxed{
m=\int_G|W|dx
=2\pi A
\int_{-1}^1dz
\int_2^3p(r)dr
=4\pi A.}
\tag{18}
\]

La masse axiale négative sur `N_ε` vaut elle aussi exactement `4πA`.

## 5. Scaling faible-`L^{3/2}` avec constantes

Écrivons

\[
K_{\varepsilon,\delta}
=\sup_{\lambda>0}
\lambda
|\{x\in D:|W_{\varepsilon,\delta}(x)|>\lambda\}|^{2/3}.
\tag{19}
\]

Spécialisons maintenant `δ=ε` et notons `E_ε` l’union :

- du tube `4<r<4+ε`, `|z|<1+ε`;
- des deux calottes `2<r<4+ε`, `1<|z|<1+ε`.

Un calcul exact des volumes, puis `ε≤1/4`, donne

\[
|E_\varepsilon|
\leq
\pi(8\varepsilon+\varepsilon^2)(2+2\varepsilon)
+2\pi\varepsilon\bigl((4+\varepsilon)^2-4\bigr)
<50\pi\varepsilon.
\tag{20}
\]

Hors de `E_ε`,

\[
|W|\leq\frac B2A.
\tag{21}
\]

Sur tout le support, `r≥2`, `0≤h≤1`, `|χ'|≤B/ε`, et les supports de `p` et `q_ε` sont disjoints. Par l’inégalité triangulaire,

\[
|W|\leq B\frac A\varepsilon.
\tag{22}
\]

La fonction de distribution séparée aux seuils de (21)–(22) donne, pour `A=ε^{1/3}`,

\[
K_{\varepsilon,\varepsilon}
\leq C_K,
\tag{23}
\]

avec la constante explicite

\[
C_K=
\max\left\{
\frac B{2\,4^{1/3}}(210\pi)^{2/3},
B(50\pi)^{2/3}
\right\}.
\tag{24}
\]

Pour la minoration, posons

\[
J=\{s\in(0,1):\beta(s)\geq B/2\},
\qquad
\ell=|J|\geq\frac13.
\]

Sur `r=4+εs`, `s∈J`, `|z|<1`,

\[
|W|\geq\frac{2B}{17}\frac A\varepsilon,
\]

et cet ensemble a une mesure au moins `16πℓε`. Par passage au suprémum dans (19),

\[
K_{\varepsilon,\varepsilon}
\geq c_K,
\qquad
c_K=
\frac{2B}{17}(16\pi\ell)^{2/3}.
\tag{25}
\]

Les constantes ne dépendent donc pas de `ε`. Par (18), (23)–(25),

\[
\frac{32\pi^2}{105C_K^3}\varepsilon
\leq
\frac{m^3}{K^3|D|}
\leq
\frac{32\pi^2}{105c_K^3}\varepsilon.
\tag{26}
\]

Cela vérifie directement, avec domaine et constantes fixes, le scaling cubique critique.

## 6. Oscillation de la direction

Définissons une extension bornée par

\[
\zeta_\varepsilon=
\begin{cases}
W_\varepsilon/|W_\varepsilon|,&W_\varepsilon\neq0,\\
e_z,&W_\varepsilon=0.
\end{cases}
\tag{27}
\]

Hors de `E_ε`, cette extension vaut `e_z`. Comme `|ζ_ε-e_z|≤2`,

\[
\fint_D|\zeta_\varepsilon-e_z|dx
\leq\frac{2|E_\varepsilon|}{|D|}.
\]

La distance de la moyenne à `e_z` est bornée par le même membre de droite. Donc

\[
\boxed{
\operatorname{MO}_D(\zeta_\varepsilon)
\leq\frac{4|E_\varepsilon|}{|D|}
\leq\frac{20}{21}\varepsilon.}
\tag{28}
\]

Cette borne supérieure, combinée à (26), montre qu’aucune minoration universelle

\[
\operatorname{MO}_D(\zeta)
\geq C
\left(\frac{m}{KV^{1/3}}\right)^p
\]

avec `C>0` et `p<3` ne peut être vraie dans cette classe div–curl.

La direction a aussi une oscillation d’ordre au moins `ε`, et pas seulement au plus. En effet, sur

\[
C_\varepsilon
=\{3<r<4,\ 1<|z|<1+\varepsilon\},
\]

le champ est purement radial, donc `ζ·e_z=0`, tandis que `ζ·e_z=1` sur `P`. Les mesures exactes sont

\[
|P|=10\pi,
\qquad
|C_\varepsilon|=14\pi\varepsilon.
\]

Le lemme des deux traces séparées appliqué à `ζ·e_z` donne, pour toute extension intégrable de la direction,

\[
\boxed{
\operatorname{MO}_D(\zeta)
\geq
\frac{2\varepsilon}{15+21\varepsilon}.}
\tag{29}
\]

Les bornes (28)–(29) certifient `MO≍ε`.

## 7. No-go du cutoff axial

Revenons à une largeur de cutoff `δ` indépendante de `ε`, sans changer le plateau radial `h=1` sur `(3,4)`.

Sur

\[
C_\delta=\{3<r<4,\ 1<|z|<1+\delta\},
\]

on a exactement

\[
W=-\frac A r\chi_\delta'(z)e_r,
\qquad
|C_\delta|=14\pi\delta.
\]

Comme chacune des deux transitions de `χ_δ` a variation totale `1`,

\[
\int_{C_\delta}|W|dx
=2\pi A
\int_3^4dr
\int_{1<|z|<1+\delta}|\chi_\delta'|dz
=4\pi A.
\tag{30}
\]

L’inégalité faible-`L^{3/2}`

\[
\int_E|W|dx\leq3K|E|^{1/3}
\]

appliquée à `C_δ` fournit le no-go quantitatif

\[
\boxed{
K\geq
\kappa_{\rm cut}A\delta^{-1/3},
\qquad
\kappa_{\rm cut}
=\frac{4\pi}{3(14\pi)^{1/3}}
\simeq1.1866682057.}
\tag{31}
\]

La même comparaison des traces `1` sur `P` et `0` sur `C_δ` donne

\[
\boxed{
\operatorname{MO}_D(\zeta)
\geq
\frac{2\delta}{15+21\delta}.}
\tag{32}
\]

Avec `A=ε^{1/3}` :

- une borne uniforme supérieure sur `K` impose `δ≥cε`;
- une oscillation `MO≤Cε` impose `δ≤C'ε` par (32).

Ainsi `δ≍ε` est nécessaire dans cette famille séparable pour conserver simultanément l’échelle critique et le contreprofil cubique. Rendre les calottes plus minces augmente leur amplitude trop vite; les rendre plus épaisses détruit la rareté directionnelle.

Ce résultat est falsifiable : il dépend seulement de (30), de la mesure exacte de `C_δ` et de la constante `3` de l’inégalité de Lorentz. Il ne prétend pas couvrir les flux non séparables `F(r,z)`.

## 8. Énergie, enstrophie et Biot–Savart

L’énergie cinétique se calcule sans reconstruction :

\[
\|U\|_2^2
=2\pi A^2
\left(\int_0^\infty\frac{h_\varepsilon(r)^2}{r}dr\right)
\left(\int_{\mathbb R}\chi_\delta(z)^2dz\right).
\tag{33}
\]

Pour `ε,δ≤1/4`, (7)–(8) donnent

\[
4\pi\log\!\frac43\,A^2
\leq\|U\|_2^2
\leq
5\pi\log\!\frac{17}{8}\,A^2.
\tag{34}
\]

Avec (11), l’énergie cinétique `\frac12\|U\|_2^2` est donc d’ordre `ε^{2/3}`.

Les deux composantes de (10) sont orthogonales. En posant

\[
B_2^2=\int_0^1\beta(s)^2ds,
\]

on obtient exactement

\[
\begin{aligned}
\|W\|_2^2
=2\pi A^2\Bigg[&
\left(\int\frac{h_\varepsilon^2}{r}dr\right)
\frac{2B_2^2}{\delta}\\
&+
\left(\int\frac{(p-q_\varepsilon)^2}{r}dr\right)
\left(\int\chi_\delta^2dz\right)
\Bigg].
\end{aligned}
\tag{35}
\]

Les supports de `p` et `q_ε` sont disjoints et

\[
\int\frac{q_\varepsilon(r)^2}{r}dr
=\frac1\varepsilon
\int_0^1\frac{\beta(s)^2}{4+\varepsilon s}ds.
\tag{36}
\]

Pour `δ=ε`, (35)–(36) montrent

\[
\|W\|_2^2\asymp\frac{A^2}{\varepsilon}
=\varepsilon^{-1/3}.
\tag{37}
\]

La concentration maintient donc la norme faible critique bornée mais fait diverger l’enstrophie.

La relation de Biot–Savart n’est pas une hypothèse supplémentaire. Puisque `U` est lisse, compact et divergence-free,

\[
\nabla\times W
=\nabla\times(\nabla\times U)
=-\Delta U.
\]

L’unicité de la solution décroissante de Poisson donne

\[
\boxed{
U=\nabla\times(-\Delta)^{-1}W,}
\tag{38}
\]

c’est-à-dire

\[
U(x)=\frac1{4\pi}
\int_{\mathbb R^3}
\frac{W(y)\times(x-y)}{|x-y|^3}dy.
\tag{39}
\]

Il n’y a ni projection de Leray cachée, ni champ harmonique résiduel.

Enfin,

\[
\|U\|_3^3
=2\pi A^3
\left(\int\frac{h_\varepsilon^3}{r^2}dr\right)
\left(\int\chi_\delta^3dz\right)
=O(\varepsilon).
\tag{40}
\]

Ainsi `\|U\|_3=O(ε^{1/3})→0`. Pour `ε` assez petit, cette donnée appartient au régime perturbatif critique de petites données. La famille ne peut donc servir de singularité candidate, même si son enstrophie initiale diverge.

## 9. Passe contradictoire

### A. Singularité artificielle sur l’axe

Le facteur `1/r` et le vecteur `e_θ` seraient dangereux à `r=0`.

**Verdict :** le support est contenu dans `r>2`; l’extension par zéro est lisse dans un voisinage entier de l’axe.

### B. Oubli du terme géométrique `ψ/r`

Écrire à tort `W_z=∂_rψ` briserait le flux nul.

**Verdict :** l’utilisation de `F=rψ` donne exactement `W_z=F_r/r`.

### C. Moyenne nulle seulement heuristique

La composante radiale n’a pas une intégrale scalaire nulle par simple axisymétrie.

**Verdict :** (13)–(14) prouvent la compensation scalaire; l’intégrale vectorielle radiale s’annule en plus angle par angle intégré. La composante axiale s’annule par tranche.

### D. Cutoff en `z` omis

Un champ indépendant de `z` aurait le profil axial souhaité mais ne serait pas compact.

**Verdict :** le cutoff produit nécessairement `W_r=-F_z/r`; (31) suit quantitativement son coût critique.

### E. Mauvaise puissance de volume dans `K`

Le tube rare est tridimensionnel de mesure `O(ε)`, non `O(ε²)` malgré son caractère annulaire.

**Verdict :** le facteur jacobien `r` reste compris entre deux constantes fixes; (20) suit les volumes cylindriques exacts.

### F. Confusion entre potentiel arbitraire et vitesse

Un champ `U` vérifiant seulement `curl U=W` ne serait pas nécessairement le champ de vitesse de Biot–Savart.

**Verdict :** ici `div U=0`, `U` est compact et (38)–(39) ferment exactement le raccord.

### G. Confusion entre profil cinématique et trajectoire Navier–Stokes

La construction ne vérifie aucune équation stationnaire ou auto-similaire et n’impose aucune croissance temporelle.

**Verdict :** elle réfute seulement l’espoir que la contrainte div–curl améliore à elle seule l’exposant cubique. Sa petite norme `L³` de vitesse la place au contraire du côté régulier.

### H. Portée en `α`

Le contreprofil utilise `α=1`.

**Verdict :** il établit l’optimalité de l’exposant de `m`, mais ne tranche pas l’optimalité de la puissance `α³` obtenue au cycle 0026.

## 10. Lemme canonique proposé

> **Lemme — réalisation axisymétrique compacte du scaling cubique.** Il existe des constantes universelles positives `c,C` et, pour tout `0<ε≤1/4`, un champ axisymétrique de swirl pur `U_ε∈C_c^∞(R³;R³)`, supporté dans un compact fixe éloigné de l’axe, tel que `div U_ε=0` et, pour `W_ε=curl U_ε`,
> \[
> \operatorname{div}W_\varepsilon=0,
> \qquad
> \int W_\varepsilon=0,
> \qquad
> c\leq\|W_\varepsilon\|_{L^{3/2,\infty}}^*\leq C.
> \]
> Dans le domaine fixe (16), avec `e=e_z`, `α=1`, la masse conique vaut `m_ε=4πε^{1/3}` et
> \[
> c\varepsilon
> \leq
> \inf_{\substack{\zeta\in L^1(D)\\
> \zeta=W_\varepsilon/|W_\varepsilon|\ \text{ sur }\{W_\varepsilon\neq0\}}}
> \operatorname{MO}_D(\zeta)
> \leq C\varepsilon.
> \]
> De plus `||U_ε||₂²≍ε^{2/3}` et `||W_ε||₂²≍ε^{-1/3}`.

Ce lemme est entièrement réduit aux identités (10), (18), (20), (25), (28), (29) et (35). Il est prêt pour une formalisation analytique légère; il ne constitue pas un résultat dynamique de Navier–Stokes.

## 11. Prochain verrou

Le verrou div–curl global est négativement résolu : il n’améliore pas l’exposant cubique. Le prochain test à forte valeur informationnelle doit ajouter une contrainte réellement dynamique.

La formulation recommandée est :

> Peut-on conserver `K_ε≈1`, `m_ε≈ε^{1/3}` et `MO≈ε` tout en imposant une borne inférieure fixe sur `||U_ε||₃`, ou sur une quantité locale de flux d’enstrophie compatible avec l’équation de vorticité ?

Pour la famille présente, `||U_ε||₃→0`; elle est éliminée par la théorie de petites données. Une nouvelle construction devrait donc découpler la concentration de la vorticité de la petitesse du champ de Biot–Savart, sans perdre la compacité, la divergence nulle ni les constantes uniformes. Si ce découplage est impossible sous une hypothèse géométrique explicite, le résultat négatif correspondant serait un vrai lemme de rigidité spatiale.

## 12. Statut de preuve

Toutes les assertions nouvelles ci-dessus sont des dérivations IA internes. Elles n’ont reçu ni revue par les pairs, ni validation inter-familles, ni formalisation. Aucun énoncé ne doit être étiqueté `PAPER_PROOF`.
