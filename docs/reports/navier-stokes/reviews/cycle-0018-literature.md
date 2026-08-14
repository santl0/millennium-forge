# Passe bibliographique séparée — cycle 0018

**Qualification.** Revue contradictoire effectuée séparément de la dérivation principale, mais dans le même dépôt, avec la même famille de modèle et une partie du même contexte. Elle n'est donc **pas une revue extérieure indépendante** et ne doit pas recevoir le statut `INDEPENDENT_REVIEW`.

**Périmètre.** Statut primaire de `arXiv:2607.08866`, transcription des équations (8)–(22), énoncés utiles de Coifman–Rochberg–Weiss, Jones, John–Nirenberg et Hunt, filiation des espaces locaux pondérés `bmo_φ`, et audit particulier de l'extension de `ξ|_{B_{2R}}` en un symbole BMO global.

**Date de vérification en ligne.** 14 août 2026.

## Verdict

- Le dossier primaire courant reste **arXiv v2**, soumis le 9 juillet 2026 et révisé le 13 juillet 2026. La notice ne liste ni v3, ni référence de revue, ni erratum ([notice arXiv](https://arxiv.org/abs/2607.08866), [texte v2](https://arxiv.org/html/2607.08866v2), DOI DataCite [10.48550/arXiv.2607.08866](https://doi.org/10.48550/arXiv.2607.08866)). La date interne « August 11, 2026 » ne constitue pas une nouvelle version : l'en-tête du même HTML indique `arXiv:2607.08866v2 [math.AP] 13 Jul 2026`.
- Une recherche par identifiant, titre exact, auteur, `v3`, `erratum` et `correction` n'a localisé aucune version primaire ultérieure au 14 août 2026. Ce constat ne couvre pas une éventuelle communication privée ou une ressource non indexée.
- La restriction à `B_{2R}` **admet bien** une extension globale dont la **semi-norme homogène BMO** est `O(φ(2R))`, uniformément en `R`, car une boule est un domaine uniforme et le théorème de Jones est invariant par dilatation. Cette conclusion contrôle, par définition, les boules traversant le bord et toutes les grosses boules.
- Le même énoncé est faux si « norme BMO » signifie une norme inhomogène qui contrôle une moyenne absolue ou une ancre : le champ constant `ξ≡e₁` a une moyenne de module un alors que `φ(R)→0`. Le passage (9) ne requiert que la semi-norme, puisque le commutateur est invariant sous l'ajout d'une constante.
- L'extension de Jones ne préserve en général ni `|ξ|=1` ni une borne `L∞` indépendante. Cela n'affecte pas (9), car l'extension n'est utilisée que comme symbole BMO et coïncide avec `ξ` sur le support de `ω_in` et au point d'évaluation. Elle ne pourrait pas être réutilisée sans preuve dans les estimations physiques du champ directionnel.
- L'application Coifman–Rochberg–Weiss à (9) est réparable et correcte composante par composante pour la matrice de Calderón–Zygmund `𝒯`. Pour atteindre `L^{3/2,∞}`, il faut interpoler entre deux exposants Lebesgue strictement voisins de `3/2`. La phrase du manuscrit parlant de « reflexive Lorentz spaces » est fausse : `L^{3/2,∞}` n'est pas réflexif. L'interpolation reste toutefois valable pour l'indice secondaire `∞`.
- John–Nirenberg justifie correctement les passages `BMO→L²` dans (13) et `BMO→L⁴` dans (18), avec des constantes dimensionnelles et un facteur `q` pour `L^q`.
- Les références `[4]`, `[5]` et `[16]` du manuscrit ne définissent pas exactement l'espace affiché en (2). Goldberg traite le `bmo` local inhomogène ; Bradshaw–Grujić utilisent une variante `\widetilde{bmo}_φ` ancrée par `L¹`; le manuscrit 2026 remplace cette ancre par `L∞`. La théorie de Spanne, Janson et Nakai–Yabuta est plus directement pertinente pour les oscillations pondérées et les multiplicateurs, mais n'est pas citée dans le théorème 4.1.
- L'algèbre et les échelles de (9)–(20) sont cohérentes à constantes près. Deux approximations doivent être réécrites comme comparabilités avec seuil : le réarrangement de (12) est comparable à, et non exactement égal à, la fonction `min`; le majorant `2φ(R)` utilisé dans (21) échoue au dernier indice pour certains `R`, bien qu'une constante uniforme légèrement plus grande répare le résultat.

La présente passe valide donc **le maillon Jones–CRW en lecture homogène**, mais ne valide pas le théorème 4.1 complet : elle n'a pas réaudité l'identité de commutateur (7) à partir du noyau exact de Biot–Savart ni les hypothèses de définition du champ directionnel aux zéros de la vorticité.

## Cadre et notation BMO à figer

Le théorème 4.1 porte sur les Navier–Stokes incompressibles visqueuses en dimension trois sur `R³`. Il suppose, sur l'intervalle terminal

\[
I=(T^*-\varepsilon,T^*),
\]

un profil ponctuel critique, une borne

\[
\omega=|\boldsymbol\omega|
\in L^\infty(I;L^{3/2,\infty}(\mathbb R^3)),
\]

et

\[
\boldsymbol\xi
=\frac{\boldsymbol\omega}{|\boldsymbol\omega|}
\in L^\infty(I;bmo_\phi(\mathbb R^3)),
\qquad
\phi(r)=\frac1{|\log r|}.
\]

Pour éviter l'ambiguïté centrale du passage d'extension, on note

\[
[b]_{\mathrm{BMO}(\Omega)}
=
\sup_{Q\subset\Omega}
\frac1{|Q|}\int_Q|b-b_Q|,
\qquad
b_Q=\frac1{|Q|}\int_Q b.
\]

Il s'agit d'une **semi-norme**, nulle sur les constantes. Les formulations avec boules ou cubes sont équivalentes à constantes dimensionnelles près. Le commutateur est pris sous la forme

\[
[\mathcal T,b]f=\mathcal T(bf)-b\,\mathcal T f,
\]

à un signe global sans effet sur les normes.

## Transcription fidèle des équations (8)–(22)

Les affichages suivants reproduisent le contenu mathématique de la [version primaire v2, section 4](https://arxiv.org/html/2607.08866v2). Les notations ont seulement été normalisées en LaTeX.

### Énoncé et champ proche

\[
\|\alpha(\cdot,t)\|_{L^{3/2,\infty}(B_R)}
\leq
\frac{C_0}{|\log R|}.
\tag{8}
\]

Le texte pose

\[
\omega_{in}=\omega\chi_{B_{2R}},
\qquad
\omega_{out}=\omega\chi_{\mathbb R^3\setminus B_{2R}},
\]

puis prolonge `ξ|_{B_{2R}}` en `\widetilde{ξ}` et affiche

\[
\begin{aligned}
\|[\mathcal T,\boldsymbol\xi](\omega_{in})\|_{L^{3/2,\infty}(B_R)}
&\leq
\|[\mathcal T,\widetilde{\boldsymbol\xi}](\omega_{in})\|_{L^{3/2,\infty}(\mathbb R^3)}\\
&\leq
C\|\widetilde{\boldsymbol\xi}\|_{\mathrm{BMO}(\mathbb R^3)}
\|\omega_{in}\|_{L^{3/2,\infty}(\mathbb R^3)}\\
&\leq
C\phi(2R)\|\omega\|_{L^{3/2,\infty}}
\leq
\frac{C'}{|\log R|}.
\end{aligned}
\tag{9}
\]

### Décomposition du champ lointain

Avec

\[
c_R=\frac1{|B_R|}\int_{B_R}\boldsymbol\xi(z)\,dz,
\]

le texte écrit

\[
\begin{aligned}
[\mathcal T,\boldsymbol\xi](\omega_{out})(x)
&=
\underbrace{(c_R-\boldsymbol\xi(x))\cdot
\mathcal T(\omega_{out})(x)}_{I_1(x)}\\
&\quad+
\underbrace{\int_{|y|>2R}K(x-y)\omega(y)
(\boldsymbol\xi(y)-c_R)\,dy}_{I_2(x)}.
\end{aligned}
\tag{10}
\]

\[
|\mathcal T(\omega_{out})(x)|
\leq
C\int_{|y|>2R}\frac{|\omega(y)|}{|y|^3}\,dy
\leq
C\|\omega\|_{L^{3/2,\infty}}
\||y|^{-3}\chi_{\{|y|>2R\}}\|_{L^{3,1}}.
\tag{11}
\]

Pour `f(y)=|y|^{-3}χ_{\{|y|>2R\}}`, le manuscrit écrit

\[
\begin{aligned}
\|f\|_{L^{3,1}}
&=
\int_0^\infty t^{1/3}f^*(t)\frac{dt}{t}\\
&=
\int_0^{CR^3}t^{-2/3}R^{-3}\,dt
+\int_{CR^3}^{\infty}t^{-5/3}\,dt\\
&=C_1R^{-2}+C_2R^{-2}=CR^{-2}.
\end{aligned}
\tag{12}
\]

### Terme `I₁`

\[
\|\boldsymbol\xi-c_R\|_{L^2(B_R)}
\leq
C|B_R|^{1/2}\|\boldsymbol\xi\|_{\mathrm{BMO}(B_R)}
\leq
CR^{3/2}\phi(R).
\tag{13}
\]

\[
\begin{aligned}
\|\boldsymbol\xi-c_R\|_{L^{3/2,\infty}(B_R)}
&\leq
CR^{1/2}\|\boldsymbol\xi-c_R\|_{L^2(B_R)}\\
&\leq
CR^{1/2}[R^{3/2}\phi(R)]
=CR^2\phi(R).
\end{aligned}
\tag{14}
\]

### Queue macroscopique de `I₂`

\[
\begin{aligned}
|I_{2,far}(x)|
&\leq
\int_{|y|>R^{1/2}}\frac{C}{|y|^3}|\omega(y)|\,dy\\
&\leq
C\|\omega\|_{L^{3/2,\infty}}
\||y|^{-3}\chi_{\{|y|>R^{1/2}\}}\|_{L^{3,1}}\\
&\leq C(R^{1/2})^{-2}=CR^{-1}.
\end{aligned}
\tag{15}
\]

### Coquilles dyadiques de `I₂`

Le texte prend

\[
A_k=B_{2^{k+1}R}\setminus B_{2^kR},
\qquad
N=\left\lfloor\frac12\log_2(1/R)\right\rfloor,
\qquad
c_k=c_{B_{2^kR}},
\]

et obtient

\[
\begin{aligned}
|c_{k+1}-c_0|
&\leq
\sum_{j=1}^{k+1}|c_j-c_{j-1}|\\
&\leq
C\sum_{j=1}^{k+1}
\frac{|B_j|}{|B_{j-1}|}
\frac1{|B_j|}\int_{B_j}|\boldsymbol\xi-c_j|\,dy\\
&\leq
C\sum_{j=1}^{k+1}\phi(2^jR).
\end{aligned}
\tag{16}
\]

\[
\begin{aligned}
\int_{A_k}\frac{|\omega(y)|}{|y|^3}
|\boldsymbol\xi(y)-c_R|\,dy
&\leq
\frac{C}{(2^kR)^3}\|\omega\|_{L^{3/2,\infty}}\\
&\quad\times
\Big(
\|\boldsymbol\xi-c_{k+1}\|_{L^{3,1}(A_k)}
+\|c_{k+1}-c_0\|_{L^{3,1}(A_k)}
\Big).
\end{aligned}
\tag{17}
\]

\[
\begin{aligned}
\|\boldsymbol\xi-c_{k+1}\|_{L^{3,1}(B_{k+1})}
&\leq
C|B_{k+1}|^{\frac13-\frac14}
\|\boldsymbol\xi-c_{k+1}\|_{L^4(B_{k+1})}\\
&\leq
C(2^kR)^{1/4}
[(2^kR)^{3/4}\phi(2^{k+1}R)]\\
&\approx
(2^kR)\phi(2^{k+1}R).
\end{aligned}
\tag{18}
\]

\[
\begin{aligned}
|I_{2,mid}(x)|
&\leq
C\sum_{k=1}^N\frac1{(2^kR)^3}(2^kR)
\sum_{j=1}^{k+1}\phi(2^jR)\\
&\approx
\frac{C}{R^2}\sum_{k=1}^N4^{-k}
\sum_{j=1}^{k+1}\phi(2^jR).
\end{aligned}
\tag{19}
\]

\[
|I_{2,mid}(x)|
\lesssim
\frac1{R^2}\sum_{j=1}^{N+1}\phi(2^jR)
\sum_{k=\max(1,j-1)}^N4^{-k}
\approx
\frac1{R^2}\sum_{j=1}^{N+1}4^{-j}\phi(2^jR).
\tag{20}
\]

\[
|I_{2,mid}(x)|
\leq
\frac{C}{R^2}2\phi(R)\sum_{j=1}^{\infty}4^{-j}
=C\frac{\phi(R)}{R^2}.
\tag{21}
\]

### Conclusion revendiquée

\[
\begin{aligned}
\|\alpha(\cdot,t)\|_{L^{3/2,\infty}(B_R)}
&\leq
\|[\mathcal T,\boldsymbol\xi](\omega_{in})\|_{L^{3/2,\infty}(B_R)}
+\|I_1\|_{L^{3/2,\infty}(B_R)}
+\|I_2\|_{L^{3/2,\infty}(B_R)}\\
&\leq
\frac{C_0}{|\log R|}.
\end{aligned}
\tag{22}
\]

## Énoncés primaires utiles

### Coifman–Rochberg–Weiss : commutateur

Pour un opérateur singulier de Calderón–Zygmund de convolution

\[
Tf(x)=\operatorname{p.v.}\int_{\mathbb R^n}
\frac{\Omega((x-y)/|x-y|)}{|x-y|^n}f(y)\,dy,
\]

avec noyau suffisamment régulier et de moyenne sphérique nulle, pour `b∈BMO(Rⁿ)` et `1<p<∞`, le commutateur vérifie

\[
\|[T,b]f\|_{L^p}
\leq
C_{n,p,T}[b]_{\mathrm{BMO}}\|f\|_{L^p}.
\]

La matrice `𝒯` qui reconstruit le tenseur de déformation à partir de la vorticité est une combinaison finie de tels opérateurs homogènes ; l'énoncé s'applique donc composante par composante. Source primaire :

- Ronald R. Coifman, Richard Rochberg et Guido Weiss, “Factorization theorems for Hardy spaces in several variables”, *Annals of Mathematics* **103**(3) (1976), 611–635, DOI [10.2307/1970954](https://doi.org/10.2307/1970954), [notice de l'éditeur](https://annals.math.princeton.edu/1976/103-3/p13).

Seule la semi-norme BMO intervient. Les constantes ajoutées à `b` disparaissent exactement de `[T,b]`.

### Jones : extension BMO

Dans la forme utile ici, si `Ω⊂Rⁿ` est un domaine uniforme au sens de Jones, il existe un opérateur d'extension borné

\[
E:\mathrm{BMO}(\Omega)\longrightarrow\mathrm{BMO}(\mathbb R^n),
\qquad
Ef=f\quad\text{p.p. sur }\Omega,
\]

tel que

\[
[Ef]_{\mathrm{BMO}(\mathbb R^n)}
\leq
C(n,\text{constante d'uniformité de }\Omega)
[f]_{\mathrm{BMO}(\Omega)}.
\]

Une boule est un domaine uniforme avec une constante indépendante de son rayon. La semi-norme BMO est invariante par translation et dilatation ; la constante d'extension pour `B_{2R}` est donc indépendante de `R`. Source primaire :

- Peter W. Jones, “Extension Theorems for BMO”, *Indiana University Mathematics Journal* **29**(1) (1980), 41–66, DOI [10.1512/iumj.1980.29.29005](https://doi.org/10.1512/iumj.1980.29.29005), [notice de l'éditeur](https://iumj.org/article/2860/).

Le théorème contrôle la semi-norme sur **tous** les cubes ou boules de `Rⁿ`; les boules coupant `∂B_{2R}` et celles de rayon beaucoup plus grand que `R` ne constituent donc pas une hypothèse supplémentaire. En revanche, l'énoncé ne borne pas chaque moyenne `(Ef)_Q` par la semi-norme.

### John–Nirenberg : intégrabilité exponentielle

Il existe des constantes dimensionnelles `c₁,c₂>0` telles que, pour tout cube `Q`, tout `b∈BMO` et tout `λ>0`,

\[
|\{x\in Q:|b(x)-b_Q|>\lambda\}|
\leq
c_1|Q|\exp\left(-c_2
\frac{\lambda}{[b]_{\mathrm{BMO}}}\right).
\]

Par intégration de la fonction de distribution, pour tout `1≤q<∞`,

\[
\left(\frac1{|Q|}\int_Q|b-b_Q|^q\right)^{1/q}
\leq
C_n q[b]_{\mathrm{BMO}}.
\]

Les cas `q=2` et `q=4` donnent respectivement (13) et le second passage de (18). Source primaire :

- Fritz John et Louis Nirenberg, “On functions of bounded mean oscillation”, *Communications on Pure and Applied Mathematics* **14**(3) (1961), 415–426, DOI [10.1002/cpa.3160140317](https://doi.org/10.1002/cpa.3160140317), [PDF de l'éditeur](https://onlinelibrary.wiley.com/doi/pdf/10.1002/cpa.3160140317).

### Hunt : Hölder et interpolation de Lorentz

La forme de Hölder utilisée dans (11), (15) et (17) est

\[
\int_{\mathbb R^n}|fg|
\leq
C_p\|f\|_{L^{p,\infty}}\|g\|_{L^{p',1}},
\qquad
1<p<\infty.
\]

Pour le commutateur, choisir `1<p₀<3/2<p₁<∞`. Coifman–Rochberg–Weiss fournit des bornes fortes sur `L^{p₀}` et `L^{p₁}`. L'interpolation réelle donne, avec

\[
\frac{2}{3}=\frac{1-\theta}{p_0}+\frac{\theta}{p_1},
\]

\[
(L^{p_0},L^{p_1})_{\theta,\infty}
=L^{3/2,\infty},
\]

et donc

\[
\|[T,b]f\|_{L^{3/2,\infty}}
\leq
C_{n,p_0,p_1,T}[b]_{\mathrm{BMO}}
\|f\|_{L^{3/2,\infty}}.
\]

L'indice secondaire `∞` est admis par l'interpolation ; aucune réflexivité n'est utilisée. Source primaire :

- Richard A. Hunt, “On `L(p,q)` spaces”, *L'Enseignement Mathématique* **12**(4) (1966), 249–276, spécialement les sections 1 et 3, [archive primaire E-Periodica](https://www.e-periodica.ch/digbib/view?lang=en&pid=ens-001%3A1966%3A12%3A%3A408).

Aucun DOI n'a été localisé dans la notice primaire consultée.

## Espaces locaux pondérés `bmo_φ` : filiation et écarts de définition

### Définition du manuscrit 2026

L'équation (2) de `arXiv:2607.08866v2` définit

\[
\|f\|_{bmo_\phi}
=
\|f\|_{L^\infty}
+
\sup_{x\in\mathbb R^3,\,0<r<1/2}
\frac1{\phi(r)}
\frac1{|B_r(x)|}\int_{B_r(x)}|f-f_{B_r(x)}|.
\]

Cette définition suffit immédiatement à donner, pour une boule `Q` de rayon `r<1/2`,

\[
\operatorname{MO}(f,Q)
\leq
\phi(r)\|f\|_{bmo_\phi}.
\]

Comme `φ(r)→0`, elle implique une oscillation moyenne uniformément évanescente aux petites échelles. La condition de Dini

\[
\int_0^{r_0}\frac{\phi(r)}r\,dr<\infty
\]

est la condition classique permettant de sommer les différences de moyennes dyadiques et d'obtenir un représentant uniformément continu, avec module contrôlé par une intégrale de `φ(r)/r`. Pour `φ(r)=1/|log r|`, cette intégrale diverge ; la classe n'est alors pas plongée en général dans les fonctions uniformément continues. Cela signifie que des contre-exemples discontinus sont permis, non que tout membre de la classe est discontinu.

Sources primaires pertinentes :

- Sergio Campanato, “Proprietà di hölderianità di alcune classi di funzioni”, *Annali della Scuola Normale Superiore di Pisa* **17** (1963), 175–188, [texte primaire Numdam](https://www.numdam.org/article/ASNSP_1963_3_17_1-2_175_0.pdf) ;
- Sven Spanne, “Some function spaces defined using the mean oscillation over cubes”, *Annali della Scuola Normale Superiore di Pisa* **19**(4) (1965), 593–608, [texte primaire Numdam](https://www.numdam.org/item/ASNSP_1965_3_19_4_593_0.pdf) ;
- Svante Janson, “On functions with conditions on the mean oscillation”, *Arkiv för Matematik* **14** (1976), 189–196, DOI [10.1007/BF02385834](https://doi.org/10.1007/BF02385834).

Le manuscrit cite Campanato mais pas Spanne ni Janson dans sa bibliographie, malgré la mention textuelle « Spanne and Campanato ».

### Goldberg n'est pas le même espace

Goldberg définit le `bmo(Rⁿ)` local inhomogène par une oscillation BMO sur les petits cubes et un contrôle de la moyenne absolue sur les cubes de grande taille. Il ne définit pas le quotient pondéré par `φ(r)` affiché en (2). Source primaire :

- David Goldberg, “A local version of real Hardy spaces”, *Duke Mathematical Journal* **46**(1) (1979), 27–42, DOI [10.1215/S0012-7094-79-04603-9](https://doi.org/10.1215/S0012-7094-79-04603-9), [notice Project Euclid](https://projecteuclid.org/journals/duke-mathematical-journal/volume-46/issue-1/A-local-version-of-real-Hardy-spaces/10.1215/S0012-7094-79-04603-9.full).

### Bradshaw–Grujić et les multiplicateurs

Bradshaw–Grujić définissent une variante

\[
\|f\|_{\widetilde{bmo}_\phi}
=
\|f\|_{L^1}
+\sup_{x,\,0<r<1/2}
\frac{\operatorname{MO}(f,I(x,r))}{\phi(r)},
\]

et utilisent le résultat de multiplicateurs ponctuels selon lequel les multiplicateurs du `\widetilde{bmo}` local appartiennent à

\[
L^\infty\cap\widetilde{bmo}_{1/|\log r|}.
\]

Sources primaires :

- Zachary Bradshaw et Zoran Grujić, “A spatially localized `L log L` estimate on the vorticity in the 3D NSE”, *Indiana University Mathematics Journal* **64**(2) (2015), 433–440, DOI [10.1512/iumj.2015.64.5496](https://doi.org/10.1512/iumj.2015.64.5496), [arXiv v5](https://arxiv.org/html/1309.2519) ;
- Eiichi Nakai et Kôzô Yabuta, “Pointwise multipliers for functions of bounded mean oscillation”, *Journal of the Mathematical Society of Japan* **37**(2) (1985), 207–218, DOI [10.2969/jmsj/03720207](https://doi.org/10.2969/jmsj/03720207), [PDF de la société](https://www.jstage.jst.go.jp/article/jmath1948/37/2/37_2_207/_pdf/-char/en).

Ces résultats expliquent le poids logarithmique, mais ils ne sont pas nécessaires au mécanisme Jones–CRW de (9). Surtout, aucune des sources citées ne transforme automatiquement une extension BMO de Jones en extension pondérée `bmo_φ`; heureusement, (9) ne demande qu'une extension **BMO non pondérée** de la restriction à une boule fixée.

## Test décisif de l'extension sur `B_{2R}`

Posons

\[
M_\phi(t)
=
\|\boldsymbol\xi(\cdot,t)\|_{bmo_\phi}.
\]

Pour `R` assez petit, toute boule `Q⊂B_{2R}` a un rayon au plus `2R<1/2`. Puisque `φ` est croissante,

\[
\frac1{|Q|}\int_Q|\boldsymbol\xi-\boldsymbol\xi_Q|
\leq
M_\phi(t)\phi(r_Q)
\leq
M_\phi(t)\phi(2R).
\]

Ainsi,

\[
[\boldsymbol\xi]_{\mathrm{BMO}(B_{2R})}
\leq
M_\phi(t)\phi(2R).
\]

La boule `B_{2R}` étant uniforme avec constante indépendante de `R`, Jones donne une extension composante par composante telle que

\[
[\widetilde{\boldsymbol\xi}]_{\mathrm{BMO}(\mathbb R^3)}
\leq
C_JM_\phi(t)\phi(2R).
\]

Ce dernier supremum porte déjà sur :

1. les petites boules entièrement incluses dans `B_{2R}` ;
2. les boules traversant `∂B_{2R}` ;
3. les boules de taille comparable à `R` ;
4. les boules de rayon arbitrairement grand.

Le contrôle des grosses boules est donc une conclusion de Jones, pas une conséquence d'une extension naïve par zéro ou par constante. Une telle extension naïve peut créer une oscillation de bord non petite et ne doit pas être substituée au prolongement de Jones.

Pour traiter les moyennes sans ambiguïté, on peut recentrer :

\[
f=\boldsymbol\xi-c_{2R},
\]

étendre `f` par Jones, puis ajouter `c_{2R}`. Le commutateur satisfait

\[
[\mathcal T,\widetilde f+c_{2R}]
=[\mathcal T,\widetilde f].
\]

Aucune borne `|c_{2R}|=O(φ(R))` n'est requise. Elle serait fausse en général : pour `ξ≡e₁`,

\[
[\xi]_{\mathrm{BMO}(B_{2R})}=0,
\qquad
|c_{2R}|=1.
\]

Ce contre-test impose d'interpréter les doubles barres BMO de (9) comme une semi-norme homogène. Sous cette interprétation standard, l'étape d'extension est valide.

Enfin, comme `\omega_{in}` est supportée dans `B_{2R}`, que l'extension coïncide avec `ξ` sur `B_{2R}` et que `x∈B_R`, on a exactement

\[
[\mathcal T,\boldsymbol\xi](\omega_{in})(x)
=[\mathcal T,\widetilde{\boldsymbol\xi}](\omega_{in})(x).
\]

## Audit local des équations (8)–(22)

| Passage | Verdict | Réserve ou réparation |
|---|---|---|
| (8) | Énoncé conditionnel clair sur l'intervalle terminal. | `C₀` dépend des normes uniformes, de la normalisation de `𝒯` et des constantes dimensionnelles ; « exclusivement » doit être lu avec ces données structurelles fixées. |
| restriction `B_{2R}` | Correcte. | Selon la convention cubes/boules, remplacer `φ(2R)` par `Cφ(CR)` ; pour le logarithme, ces poids sont comparables après un seuil `R≤R₀`. |
| Jones → (9) | Correct pour la semi-norme BMO. | Faux pour une norme ancrée par une moyenne ou `L∞`; l'extension ne reste pas nécessairement unitaire ou bornée. |
| CRW → Lorentz dans (9) | Correct par interpolation entre deux `L^p`. | `L^{3/2,∞}` n'est pas réflexif ; la justification textuelle doit être corrigée. |
| (10) | Décomposition algébrique correcte, à convention de signe du commutateur près. | Les produits matriciels/vectoriels devraient être indicés pour une preuve formelle. |
| (11) | Lorentz–Hölder correct, le noyau étant séparé de sa singularité. | La constante dépend du noyau de `𝒯`. |
| (12) | Échelle `R⁻²` correcte. | Le réarrangement exact est de type `C/(t+cR³)`, seulement comparable à `min(R⁻³,Ct⁻¹)`. Les égalités doivent devenir `≍`. |
| (13) | John–Nirenberg avec `q=2`, correct. | Exiger `R<1/2` et préciser la semi-norme locale. |
| (14) | Inclusion finie-mesure `L²→L^{3/2,∞}` et facteur `R^{1/2}` corrects. | Aucun défaut d'échelle. |
| (15) | Échelle ponctuelle `R⁻¹` correcte. | Le passage `CR≪φ(R)` après multiplication par `|B_R|^{2/3}` exige seulement un seuil explicite. |
| (16) | Télescopage des moyennes correct ; `|B_j|/|B_{j-1}|=8`. | Toutes les échelles doivent rester `<1/2`; `R<1/16` suffit pour la coquille maximale à constantes près. |
| (17) | Hölder `L^{3/2,∞}×L^{3,1}` correct. | La norme faible de `ω` doit être uniforme en temps. |
| (18) | John–Nirenberg `q=4` puis inclusion `L⁴→L^{3,1}` corrects. | Les rayons réels sont comparables à `2^kR`; les signes `≈` absorbent ces constantes. |
| (19)–(20) | Sommation et inversion de l'ordre correctes à constantes près. | Les symboles `≈` ne sont pas des identités. |
| (21) | Conclusion d'échelle réparable. | Avec `N=⌊(1/2)log₂(1/R)⌋`, `2^{N+1}R` peut atteindre `2R^{1/2}`; l'inégalité littérale `φ(2^jR)≤2φ(R)` peut échouer au dernier indice. Utiliser `Cφ(R)` après `R≤R₀`. |
| (22) | Suit des trois estimations si les comparabilités sont rendues explicites. | Ne vaut que pour `R` suffisamment petit et `t∈I`; ne constitue pas une conclusion Clay sans les hypothèses de profil et de direction. |

## Écart avec le problème Clay

Même après validation du prolongement de Jones, (22) reste un résultat conditionnel sous :

- le profil ponctuel critique et le confinement de tous les hauts superniveaux dans une boule centrée fixe ;
- la borne uniforme `L^{3/2,∞}` de la magnitude de vorticité ;
- la borne uniforme de la direction dans la variante `bmo_{1/|log r|}` définie par le manuscrit ;
- la validité de la réduction exacte à un commutateur Calderón–Zygmund.

Le maillon transférable est donc limité : **si** ces hypothèses sont satisfaites et si (7) est valide pour le noyau exact, alors Jones + Coifman–Rochberg–Weiss donnent bien le gain `O(1/|log R|)` pour le champ proche. Aucun de ces théorèmes d'analyse harmonique ne fournit l'hypothèse géométrique `bmo_φ` pour des données Clay générales.

## Limite de la revue

Cette passe ne constitue pas une validation indépendante : elle utilise la même famille de modèle et le même environnement que le programme principal. Elle peut détecter les erreurs de source, de quantificateur et de semi-norme, mais des erreurs corrélées restent possibles. Une revue extérieure devrait notamment :

- vérifier dans le PDF original de Jones la convention exacte de `BMO(Ω)` utilisée pour une boule ;
- reconstruire `𝒯` composante par composante depuis Biot–Savart et vérifier les hypothèses exactes de Coifman–Rochberg–Weiss ;
- contrôler le représentant de `ξ` aux zéros de `ω` et la mesurabilité temporelle des extensions ;
- refaire indépendamment les comparaisons de Lorentz et toutes les constantes de localisation.

## Empreinte de la veille

Ressources primaires consultées le 14 août 2026 :

- `https://arxiv.org/abs/2607.08866`
- `https://arxiv.org/html/2607.08866v2`
- `https://doi.org/10.48550/arXiv.2607.08866`
- `https://annals.math.princeton.edu/1976/103-3/p13`
- `https://doi.org/10.2307/1970954`
- `https://iumj.org/article/2860/`
- `https://doi.org/10.1512/iumj.1980.29.29005`
- `https://doi.org/10.1002/cpa.3160140317`
- `https://www.e-periodica.ch/digbib/view?lang=en&pid=ens-001%3A1966%3A12%3A%3A408`
- `https://doi.org/10.1215/S0012-7094-79-04603-9`
- `https://www.numdam.org/item/ASNSP_1965_3_19_4_593_0.pdf`
- `https://doi.org/10.1007/BF02385834`
- `https://arxiv.org/html/1309.2519`
- `https://doi.org/10.1512/iumj.2015.64.5496`
- `https://doi.org/10.2969/jmsj/03720207`

**État de la passe :** maillon d'extension validé sous lecture en semi-norme homogène ; terminologie de réflexivité réfutée ; références `bmo_φ` incomplètes et définitions non identiques ; corrections locales requises en (12) et (21). À réauditer extérieurement et après toute nouvelle version primaire.
