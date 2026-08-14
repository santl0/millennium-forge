# Passe analytique indépendante — cycle 0030 : nombreux tores, porosité et cohérence

Date : 2026-08-14

Statut : **dérivation IA interne**, non publiée, non indépendante au sens inter-familles et jamais `PAPER_PROOF`

## Verdict

Le cardinal `N→∞` ne compense pas l’effondrement de la vitesse dans la classe **homogène et localement poreuse** isolée par le rapport racine. Si les tubes ont une amplitude commune `A`, un rayon de cœur commun `h`, des corridors disjoints de rayon commun `q`, une longueur totale `𝓛`, et si le packing est local à toute échelle `r≥q`, alors

\[
\boxed{
c_bK^3\frac h{\mathcal L}
\leq
\|\operatorname{BS}W\|_3^3
\leq
C_bK^3
\left[
\frac h{\mathcal L}
+\left(\frac hq\right)^{4/3}
\right].}
\tag{1}
\]

Ici

\[
K=\|W\|_{L^{3/2,\infty}}^*
\asymp_b A(\mathcal Lh^2)^{2/3}.
\tag{2}
\]

La minoration est la somme de tests de Stokes locaux disjoints. La majoration traite collectivement tous les champs lointains et reste valable sous cohérence constructive maximale : elle n’utilise ni les signes, ni une quasi-orthogonalité, ni une annulation de moments.

Les quatre points attaqués se ferment comme suit.

1. **Exposant `4/3`.** Il est correct. Le packing donne une densité de Morrey `D=A(h/q)²`; Hedberg donne `||u_far||∞≤CD^{2/3}M^{1/3}`, HLS donne `||u_far||₂²≤CA²S^{5/3}`, et l’interpolation produit exactement `(h/q)^{4/3}`.
2. **Troncature à `q`.** Il n’y a ni trou ni logarithme manquant. La coquille `[q/2,q]` coûte `CDq`, et les formules locale et lointaine ont toutes deux la taille `Ah²/q` au raccord.
3. **Normalisation.** Pour un profil transverse fixe et une amplitude commune, la fonction de distribution se factorise; (2) est exacte à une constante de profil explicite. En particulier `K³≈A³𝓛²h⁴`, ce qui transforme les deux estimations sans perte de puissance.
4. **Tore périodique.** Sur une cellule unité, sous moyenne nulle, le reste lisse du noyau ajoute
   \[
   C K^3S,
   \qquad S\asymp_b\mathcal Lh^2.
   \]
   La conclusion périodique exige donc aussi `S→0`, à moins d’une cancellation supplémentaire du reste.

Ce résultat ne donne toutefois **aucun no-go sous les seules prémisses vagues** « faible-`L^{3/2}` global, corridors log-BMO et containment dans une boule de taille `ℓ` ». La borne (1) utilise réellement : amplitude, `h` et `q` communs; packing **local** dans chaque boule; géométrie tubulaire uniforme; et, pour interpréter `W` comme vorticité, `div W=0`. Une cascade hétérogène n’est pas couverte. La voie « vitesse compacte d’abord » montre même qu’aucune inégalité abstraite

\[
\|\operatorname{curl}u\|_{L^{3/2,\infty}}\leq C,
\quad
\operatorname{supp}u\subset B_\ell
\quad\Longrightarrow\quad
\|u\|_3\to0
\]

ne peut être vraie sans l’hypothèse directionnelle : une construction compacte multi-échelle ci-dessous garde le faible-`L^{3/2}` du curl uniforme et fait croître `||u||₃³` comme `N`. Elle échoue précisément au log-BMO de direction.

## 1. Cadre exact et quantificateurs

Soient des courbes fermées lisses `Γ_j⊂ℝ³`, de longueurs `L_j`, et

\[
\mathcal L=\sum_{j=1}^NL_j.
\tag{3}
\]

On suppose :

- `reach(Γ_j)≥8q`;
- les tubes `T_{4q}(Γ_j)` sont deux à deux disjoints;
- `0<h<q/8`;
- le profil `b(ρ)=\bar b(ρ²)` est fixe, lisse, radial, supporté dans `ρ<1`, positif et égal à un sur `ρ≤1/2`;
- les amplitudes ont même module `A>0` et des signes `σ_j∈{−1,+1}`.

Le champ est

\[
W(x)=A\sum_{j=1}^N
\sigma_j b(d_j(x)/h)\tau_j(x),
\tag{4}
\]

où `d_j` est la distance à `Γ_j` et `τ_j` la tangente transportée dans le tube.

Le lemme supérieur ne demande que (4) comme source du potentiel

\[
\operatorname{BS}W
=\nabla\times(-\Delta)^{-1}W.
\tag{5}
\]

Mais, pour que `curl BS[W]=W` et pour appliquer Stokes à `W`, il faut en plus

\[
\operatorname{div}W=0.
\tag{6}
\]

La formule naïve `b(d/h)τ` n’est pas automatiquement divergence-free autour d’une courbe gauche arbitraire : le jacobien tubulaire et la torsion interviennent. La réalisation du rapport racine par cercles coaxiaux est exacte, car `τ=e_θ` et le coefficient est indépendant de `θ`. Les conclusions de vorticité et la minoration de (1) sont donc inconditionnelles pour ces cercles; pour des courbes générales, (6) est une hypothèse ou requiert un correcteur de Hodge à constantes suivies.

Le packing pertinent est local : pour toute boule `B_r(x)` et tout `r≥q`,

\[
\sum_j
\mathcal H^1(\Gamma_j\cap B_r(x))
\leq P\frac{r^3}{q^2},
\tag{7}
\]

avec `P` uniforme. La disjonction des tubes de rayon `4q` et le reach uniforme impliquent (7), à changement de constante, par comparaison des volumes des sous-tubes contenus dans `B_{r+Cq}`.

Un simple budget global

\[
\mathcal Lq^2\lesssim\ell^3
\tag{8}
\]

pour un cluster inclus dans `B_ℓ` ne remplace pas (7) : (8) autorise une sous-concentration de toute la longueur dans une boule beaucoup plus petite que `ℓ`.

## 2. Normalisation faible-`L^{3/2}`

Dans les coordonnées tubulaires d’une courbe, l’intégration angulaire annule le terme linéaire de courbure du jacobien. Pour une amplitude commune et des supports disjoints, la fonction de distribution est

\[
|\{|W|>t\}|
=c_b\mathcal Lh^2F_b(t/A),
\qquad 0<t<A\|b\|_\infty,
\tag{9}
\]

où `F_b` est la distribution adimensionnée du profil transverse et `c_b` ne dépend ni de `N`, ni de `h`, ni des longueurs. Par conséquent

\[
K
=\sup_{t>0}t|\{|W|>t\}|^{2/3}
=\kappa_bA(\mathcal Lh^2)^{2/3},
\tag{10}
\]

avec `0<κ_b<∞` fixé. En particulier,

\[
\boxed{K^3=\kappa_b^3A^3\mathcal L^2h^4.}
\tag{11}
\]

La relation utilisée par le rapport racine est donc correcte. Elle cesse d’être vraie avec un seul `A` effectif dès que les amplitudes varient.

Pour mémoire, si les tubes ont des amplitudes `A_j` et des volumes actifs `v_j≈L_jh_j²`, la formule exacte devient

\[
|\{|W|>t\}|
=\sum_jc_bv_jF_b(t/A_j).
\tag{12}
\]

Dans le modèle étagé, en ordonnant `A_1≤⋯≤A_N` et en posant `V_m=\sum_{j=m}^Nv_j`,

\[
K^{3/2}\asymp
\sup_m A_m^{3/2}V_m.
\tag{13}
\]

Ce ledger faible-Lorentz permet des cascades : si `v_{j+1}≤cv_j`, `c<1`, et `A_j=v_j^{-2/3}`, alors chaque composante a un budget critique d’ordre un tandis que le budget global reste d’ordre un. C’est la raison précise pour laquelle (1) ne doit pas être extrapolée à des paramètres hétérogènes.

## 3. Partie locale : majoration et minoration assorties

Écrivons le noyau euclidien sous la forme `|K_BS(z)|≤C|z|^{-2}` et tronquons les sources à distance `q/2` du point d’observation. La disjonction des tubes `4q` garantit qu’à cette échelle une boule ne voit qu’une géométrie tubulaire.

Si `d` est la distance à la courbe locale, l’intégration absolue le long de l’arc et dans sa section donne

\[
|u_{\rm loc}(x)|
\leq CA
\begin{cases}
h,&d\leq2h,\\[1mm]
h^2/d,&2h<d<q.
\end{cases}
\tag{14}
\]

La première ligne inclut la singularité intégrable du noyau. La seconde vient de

\[
Ah^2\int_{\mathbb R}
\frac{ds}{d^2+s^2}
\lesssim\frac{Ah^2}{d}.
\]

Les coordonnées tubulaires et leur multiplicité bornée donnent

\[
\begin{aligned}
\|u_{\rm loc}\|_3^3
&\leq
CA^3\mathcal L
\left[
h^3h^2
+\int_h^q
\left(\frac{h^2}{d}\right)^3d\,dd
\right]\\
&\leq CA^3\mathcal Lh^5.
\end{aligned}
\tag{15}
\]

Après (11),

\[
\boxed{
\|u_{\rm loc}\|_3^3
\leq CK^3\frac h{\mathcal L}.}
\tag{16}
\]

Cette puissance est optimale dans la classe. Supposons (6), et orientons chaque section normale. Pour `h/4≤ρ≤h/2`, Stokes appliqué au champ **total** donne

\[
\left|
\oint_{C_{j,s,\rho}}u\cdot dl
\right|
=A\pi\rho^2.
\tag{17}
\]

Les autres tubes ne rencontrent pas le disque, donc ils ne peuvent modifier sa circulation. Hölder sur le cercle, puis intégration sur `ρ` et le long de toutes les courbes, fournit

\[
\|u\|_3^3
\geq c_bA^3\mathcal Lh^5
=c_b'K^3\frac h{\mathcal L}.
\tag{18}
\]

Pour le plateau utilisé au cycle 0029, on peut reprendre la constante locale `31π²/20480` avant conversion par `κ_b`; son optimisation n’est pas nécessaire ici. L’essentiel est que (18) est indépendant des signes et de toute cancellation du champ extérieur.

## 4. Partie lointaine : audit de l’exposant `4/3`

Posons

\[
d\mu=|W|dx,
\qquad
M=\mu(\mathbb R^3)\leq C_bAS,
\qquad
S\asymp_b\mathcal Lh^2.
\tag{19}
\]

Par (7), pour `r≥q`,

\[
\mu(B_r(x))
\leq
C A h^2
\sum_j\mathcal H^1(\Gamma_j\cap B_{r+Ch}(x))
\leq Dr^3,
\tag{20}
\]

avec

\[
\boxed{D=CP A(h/q)^2.}
\tag{21}
\]

### 4.1 Hedberg avec la troncature

Soit

\[
r_0=(M/D)^{1/3}.
\tag{22}
\]

Pour le potentiel tronqué `|x-y|≥q/2`, la coquille `[q/2,q]` satisfait

\[
\int_{q/2\leq|x-y|<q}
\frac{d\mu(y)}{|x-y|^2}
\leq Cq^{-2}\mu(B_q(x))
\leq CDq.
\tag{23}
\]

Si `r₀≥q`, une décomposition dyadique de `[q,r₀]` donne une somme géométrique, et non harmonique :

\[
\int_{q\leq|x-y|<r_0}
\frac{d\mu(y)}{|x-y|^2}
\leq CDr_0.
\tag{24}
\]

La queue vérifie

\[
\int_{|x-y|\geq r_0}
\frac{d\mu(y)}{|x-y|^2}
\leq CM r_0^{-2}.
\tag{25}
\]

Comme `Dr₀=Mr₀^{-2}=D^{2/3}M^{1/3}`, (23) est absorbée. Si `r₀<q`, la borne directe `CMq^{-2}` est encore plus petite que `CD^{2/3}M^{1/3}` puisque `M<Dq³`. Dans tous les cas,

\[
\boxed{
\|u_{\rm far}\|_\infty
\leq CD^{2/3}M^{1/3}.}
\tag{26}
\]

Le raccord est cohérent : à `d=q`, (14) vaut `CAh²/q`, tandis que la densité de (21) sur une coquille de taille `q` donne `Dq=CAh²/q`. Il n’y a donc ni zone oubliée, ni facteur `log(q/h)` caché.

### 4.2 HLS et interpolation

Le noyau tronqué reste dominé par `C|z|^{-2}`. Hardy–Littlewood–Sobolev donne

\[
\|u_{\rm far}\|_2
\leq C\|W\|_{6/5}
\leq CA S^{5/6},
\tag{27}
\]

donc

\[
\|u_{\rm far}\|_2^2
\leq CA^2S^{5/3}.
\tag{28}
\]

L’inégalité élémentaire

\[
\|v\|_3^3
\leq\|v\|_2^2\|v\|_\infty
\tag{29}
\]

et (19), (21), (26) donnent

\[
\begin{aligned}
\|u_{\rm far}\|_3^3
&\leq
C A^2S^{5/3}
\left[A(h/q)^{4/3}S^{1/3}\right]\\
&=CA^3S^2(h/q)^{4/3}.
\end{aligned}
\tag{30}
\]

Puisque `A³S²≈K³`,

\[
\boxed{
\|u_{\rm far}\|_3^3
\leq CK^3(h/q)^{4/3}.}
\tag{31}
\]

L’exposant `4/3` est donc algébriquement forcé : `D` contient `(h/q)²`, Hedberg l’élève à `2/3`, et HLS n’ajoute aucune puissance de `h/q`. Un exposant `2/3` signalerait l’oubli de cette élévation; un exposant `2` demanderait une information d’orthogonalité ou de cancellation absente. Le modèle d’une mesure de densité `D` presque uniforme dans une boule de rayon `r₀` sature les puissances de (26); aucune amélioration ne suit des seuls nombres `D,M`.

## 5. Somme, termes croisés et cohérence

La décomposition `u=u_loc+u_far` et

\[
(a+b)^3\leq4(a^3+b^3)
\]

donnent la majoration de (1). Elle traite les termes croisés sans les développer : `u_far` est calculé depuis la mesure collective `|W|dx`, donc tous les champs lointains peuvent être alignés avec le même signe dans (26)–(31).

Pour comparer, sans packing local et avec des paramètres individuels

\[
K_j\asymp A_j(L_jh_j^2)^{2/3},
\qquad
\eta_j=h_j/R_j,
\]

les seules bornes générales héritées du cycle 0029 sont

\[
c_b\sum_jK_j^3\eta_j
\leq
\left\|\sum_ju_j\right\|_3^3
\leq
C_b
\left[
\sum_jK_j(\eta_j+\eta_j^2)^{1/3}
\right]^3.
\tag{32}
\]

La gauche utilise les coquilles de Stokes disjointes; la droite est Minkowski. Une autre majoration, sans gain d’aspect, est

\[
\left\|\sum_ju_j\right\|_3^3
\leq
C
\left(\sum_jK_j^{3/2}\right)^2,
\tag{33}
\]

par HLS et la disjonction des supports de vorticité.

L’intervalle entre les deux côtés de (32) est réel. Pour `N` tubes de même volume, le ledger faible (13) permet par exemple

\[
K_j\asymp K j^{-2/3}.
\tag{34}
\]

Alors

\[
\sum_jK_j^3\eta
\asymp K^3\eta,
\qquad
\left(\sum_jK_j\eta^{1/3}\right)^3
\asymp K^3N\eta.
\tag{35}
\]

Au choix `η=N^{-1}`, Stokes ne donne qu’un minorant `O(K³/N)` tandis que Minkowski autorise `O(K³)`. Seul un contrôle collectif tel que (7), ou une quasi-orthogonalité de vitesse, ferme cette fenêtre de cohérence. Les signes annulant l’impulsion ne suffisent pas : ils améliorent la queue extérieure, mais ne contrôlent pas les interactions à l’intérieur du cluster.

Un critère de collapse immédiatement suffisant dans la classe hétérogène est

\[
\sum_jK_j\eta_j^{1/3}\longrightarrow0.
\tag{36}
\]

Sous une estimation de quasi-orthogonalité

\[
\left\|\sum_ju_j\right\|_3^3
\leq C\sum_jK_j^3\eta_j,
\tag{37}
\]

il suffirait que le membre droit tende vers zéro. Ni (36), ni (37) ne découle d’une borne faible-`L^{3/2}` globale.

## 6. Corridors log-BMO et packing

Soit `ζ=e_3+\sum_jf_j` l’extension unitaire, où le défaut `f_j` est supporté dans le corridor `T_q(Γ_j)` et les corridors sont disjoints. Pour toute boule `B`,

\[
\operatorname{MO}_B(\zeta)
\leq
2\fint_B\sum_j|f_j|dx.
\tag{38}
\]

Pour l’interpolation logarithmique de profondeur

\[
\Lambda=\log(q/h),
\]

le défaut transverse vérifie

\[
\int_{T_q(\Gamma_j)}|f_j|dx
\leq
C L_j\left(\frac{q^2}{\Lambda}+h^2\right).
\tag{39}
\]

Les petites boules rencontrant un seul corridor sont contrôlées par le lemme all-ball du cycle 0028. Pour les boules de rayon `r≥q`, (7), (38) et (39) donnent

\[
\operatorname{MO}_{B_r}(\zeta)
\leq
C\left(\frac1\Lambda+\frac{h^2}{q^2}\right).
\tag{40}
\]

Une borne uniforme de log-BMO suit donc si

\[
\frac{|\log h|}{\Lambda}\leq C,
\qquad
\frac{|\log q|}{\Lambda}\leq C.
\tag{41}
\]

Le second rapport gouverne les boules qui voient plusieurs corridors; le premier gouverne la transition près du cœur. Dans la famille explicite du rapport racine,

\[
h_n=2^{-12n},
\qquad
q_n=2^{-9n},
\qquad
\ell_n=2^{-3n},
\]

on a `Λ_n=3n log2`, `|log h_n|/Λ_n=4` et `|log q_n|/Λ_n=3`. L’audit all-ball est donc compatible avec le collapse.

En revanche, le containment et le packing global (8) seuls donnent au mieux, sur la boule parente,

\[
|\log\ell|\operatorname{MO}_{B_\ell}(\zeta)
\lesssim
|\log\ell|\frac{\mathcal Lq^2}{\ell^3\Lambda}.
\tag{42}
\]

Ils ne contrôlent aucune sous-boule. La bonne hypothèse est une condition de Carleson logarithmique, dont (7) est une version homogène :

\[
\sup_{B_r}
\frac{|\log r|}{r^3}
\sum_j
\mathcal H^1(\Gamma_j\cap B_{r+Cq})
\left(\frac{q^2}{\Lambda}+h^2\right)
<\infty.
\tag{43}
\]

Enfin, la direction et ses corridors ne voient ni `A`, ni les signes. Une borne log-BMO ne fournit donc pas à elle seule le ledger d’amplitudes nécessaire pour passer de (13) à un analogue hétérogène de (21).

## 7. Raccord périodique

Plaçons le cluster dans une boule d’injectivité d’une cellule unité et supposons

\[
\int_{\mathbb T^3}Wdx=0,
\qquad
\operatorname{div}W=0.
\tag{44}
\]

Le noyau périodique s’écrit, après une coupure fixe autour de l’origine,

\[
K_{\mathbb T^3}(z)
=\chi(z)K_{\mathbb R^3}(z)+H(z),
\qquad H\in C^\infty(\mathbb T^3).
\tag{45}
\]

La partie singulière satisfait les mêmes preuves locale et lointaine. Pour le reste,

\[
\|H*W\|_\infty
\leq C\|W\|_1
\leq CAS.
\tag{46}
\]

Comme la cellule a volume un,

\[
\|H*W\|_3^3
\leq CA^3S^3
\asymp CK^3S.
\tag{47}
\]

Ainsi

\[
\boxed{
\|\operatorname{BS}_{\mathbb T^3}W\|_3^3
\leq
CK^3
\left[
\frac h{\mathcal L}
+(h/q)^{4/3}
+S
\right].}
\tag{48}
\]

Le terme `S` inclut toutes les images périodiques; il ne doit pas être absorbé silencieusement dans les deux rapports de forme. Pour la famille explicite,

\[
S_n\asymp\mathcal L_nh_n^2=2^{-15n-12}\to0,
\]

donc le raccord du rapport racine est valide. Pour une famille générale où `S` ne tend pas vers zéro, (48) ne conclut pas au collapse périodique. La moyenne nulle est également indispensable : sinon le mode zéro de la vorticité n’est pas le curl d’une vitesse périodique.

## 8. Comparaison : partir d’une vitesse compacte

Le changement de paramétrage résout automatiquement le problème de Schwartz mais non la direction. Fixons

\[
v\in C_c^\infty(B_1;\mathbb R^3),
\qquad
\operatorname{div}v=0,
\qquad
v\neq0,
\]

et posons `w=curl v`. Choisissons des boules disjointes

\[
B(c_j,r_j)\subset B_\ell,
\qquad
r_j=\ell2^{-j-3},
\qquad
c_j=\ell2^{-j}e_1,
\tag{49}
\]

après avoir initialement réduit le support de `v` d’une constante fixe. Définissons

\[
v_j(x)=r_j^{-1}v((x-c_j)/r_j),
\qquad
w_j(x)=r_j^{-2}w((x-c_j)/r_j),
\tag{50}
\]

et

\[
u_N=\sum_{j=1}^Nv_j,
\qquad
W_N=\operatorname{curl}u_N=\sum_{j=1}^Nw_j.
\tag{51}
\]

Les supports des vitesses sont disjoints, d’où l’identité exacte

\[
\boxed{
\|u_N\|_3^3
=N\|v\|_3^3.}
\tag{52}
\]

En revanche, le faible-`L^{3/2}` de `W_N` reste uniforme. En effet, si `A=||w||∞` et `V=|supp w|`, alors, pour un seuil `t`, seuls les indices dont `Ar_j^{-2}>t` contribuent; la somme géométrique de leurs volumes est au plus `Cr_m³`, où `m` est le premier indice actif. Ainsi

\[
t^{3/2}|\{|W_N|>t\}|
\leq C A^{3/2}V
\tag{53}
\]

uniformément en `N`. Chaque `u_N` est compact, lisse et divergence-free. De plus,

\[
\nabla\times(-\Delta)^{-1}W_N=u_N,
\tag{54}
\]

car le projecteur de Leray agit comme l’identité sur `u_N`. Toutes les queues multipolaires extérieures s’annulent automatiquement.

La construction (49)–(54) réfute tout no-go fondé seulement sur le faible-`L^{3/2}` du curl et le packing compact. Mais elle échoue au log-BMO directionnel. Un curl compact non nul ne peut avoir une direction constante partout sur son ensemble actif : si `w=f e` avec `e` constant, `div w=e·∇f=0` et la compacité imposent `f=0`. On peut donc choisir dans le profil de base une boule relative sur laquelle la direction a une oscillation moyenne `m₀>0`. La copie d’échelle `r_j` contient une boule de rayon `c r_j` avec la même oscillation, et

\[
|\log(cr_j)|m_0\longrightarrow\infty.
\tag{55}
\]

Aucune valeur assignée sur le lieu nul ne supprime l’oscillation entre deux sous-régions actives de mesure positive. Le prochain verrou est donc exactement : construire une vitesse compacte dont le curl devient directionnellement plus plat à mesure que l’échelle diminue, sans perdre (52) ni la borne (53).

## 9. Passe contradictoire

### A. « Le faible-`L^{3/2}` suffit à HLS fort »

**Réfuté.** L’opérateur d’ordre `−1` envoie l’endpoint faible seulement vers faible-`L³`. La preuve de (31) utilise séparément la masse `L¹`/Morrey, `L^{6/5}`, puis l’interpolation `L²`–`L∞`.

### B. Exposant `4/3`

**Vérifié.** Les puissances sont `[(h/q)²]^{2/3}=(h/q)^{4/3}`. Les dimensions et la normalisation (11) ferment sans facteur de longueur résiduel.

### C. Coquille de troncature

**Vérifié.** La coquille `[q/2,q]` est (23). Elle a la même taille que les deux formules au raccord et n’engendre pas de logarithme.

### D. Cohérence parfaite

**Couverte par la majoration.** Les mesures et noyaux sont remplacés par leurs modules avant Hedberg et HLS. Une cohérence de signes ne peut dépasser (31). Elle pourrait en revanche rendre (31) non négligeable; aucun minorant correspondant n’est démontré.

### E. Packing seulement global

**Insuffisant.** (8) ne donne ni (20), ni le contrôle all-ball (43). Une famille peut concentrer une proportion importante de sa longueur dans une sous-boule.

### F. Courbes arbitraires

**Réviser la formulation.** Le champ tangent à coefficient radial est automatiquement divergence-free pour les cercles axisymétriques utilisés, pas pour toute courbe gauche sans calcul du jacobien. La majoration de potentiel reste vraie; le raccord vorticité–vitesse et Stokes exigent (6).

### G. Hétérogénéité

**Non couverte.** (12)–(13) montrent que le faible-Lorentz autorise des amplitudes et volumes en cascade. Un analogue de (20) doit être formulé comme ledger de Morrey–Carleson pondéré; sommer (1) composante par composante est invalide.

### H. Atome macroscopique persistant

**Quantificateur à exclure.** Si une composante fixe reste présente pendant que `N→∞`, Stokes donne trivialement un `liminf ||u_N||₃>0`. Une question de concentration significative doit imposer la disparition du plus gros budget individuel ou `ℓ_n→0` avec paramètres contrôlés.

### I. Reste périodique

**Vérifié sous `S→0`.** La borne est (47), non zéro par simple annulation d’impulsion. La famille explicite satisfait `S_n→0`; une famille générale doit l’ajouter aux hypothèses terminales.

### J. Classe globalement régulière

Les cercles coaxiaux de même axe restent axisymétriques sans swirl. Cela fournit une seconde raison de ne pas les interpréter comme blow-up, indépendante de la petitesse `L³`. Une réalisation non axisymétrique du lemme supérieur ne construirait toujours aucune dynamique singulière.

### K. Pression et temps

Tout le rapport est cinématique et elliptique. La pression, `(u·∇)u`, la diffusion, le vortex stretching et la propagation des corridors ne sont pas contrôlés.

## 10. Lemme canonique et décision

> **Lemme — collapse poreux homogène.** Sous (3)–(7), avec un profil fixe, une amplitude commune et des rayons communs `0<h<q/8`, le champ de Biot–Savart sur `ℝ³` satisfait la majoration droite de (1). Si `W` est divergence-free et possède un plateau sur chaque cœur, la minoration gauche de (1) vaut. Les constantes dépendent seulement du profil, du reach normalisé et de la constante de packing `P`, jamais de `N`, des signes ou de `𝓛`.

> **Corollaire périodique.** Sous (44) et dans une cellule d’injectivité fixe, (48) vaut.

**DÉCISION : ABANDONNER la branche des tores à amplitude et rayons communs sous packing local uniforme.** Si

\[
\sup_nK_n<\infty,
\qquad
\frac{h_n}{\mathcal L_n}\to0,
\qquad
\frac{h_n}{q_n}\to0,
\tag{56}
\]

alors `||BS W_n||₃→0` sur `ℝ³`; sur `T³`, ajouter `S_n→0`.

**NE PAS ÉTENDRE ce no-go sans nouveau lemme.** Les alternatives encore ouvertes sont :

1. cascade hétérogène avec ledger Morrey–Carleson pondéré;
2. géométrie sans packing local (au risque de perdre log-BMO);
3. vitesse compacte divergence-free construite en amont, avec aplatissement directionnel multi-échelle.

La troisième est la plus falsifiable : (52)–(55) séparent exactement le bénéfice — Schwartz et masse `L³` — du coût encore fatal — récurrence directionnelle log-BMO.

## 11. Statut de preuve

Les identités d’échelle (9)–(13), les estimations locales (14)–(18), la dérivation Hedberg–HLS (19)–(31), le reste périodique (45)–(48) et la construction compacte (49)–(54) sont analytiques. La constante numérique optimale de (1) n’est pas calculée. La borne all-ball (40) dépend des constantes géométriques du cycle 0028 et du packing local (7); elle n’est pas certifiée par arithmétique d’intervalles.

Toutes les affirmations restent des dérivations IA internes sans revue externe, validation inter-familles ou formalisation. Aucune ne doit être étiquetée `PAPER_PROOF`.
