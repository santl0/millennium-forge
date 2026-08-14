# Audit bibliographique séparé — cycle 0015

**Objet.** Passage réarrangée–distribution autour de (40)–(49), avec priorité à l'implication (47) → (49), dans `arXiv:2607.08866v2`.

**Date de vérification.** 14 août 2026.

## Verdict borné

1. Le dossier arXiv ne comporte toujours que deux versions : v1 du 9 juillet 2026 et v2 du 13 juillet 2026. En l'absence de métadonnée de publication dans le dossier consulté, le statut vérifiable ici est celui d'une prépublication v2, et non celui d'un article évalué ou publié ([dossier arXiv](https://arxiv.org/abs/2607.08866), [texte v2](https://arxiv.org/html/2607.08866v2)).
2. L'inégalité de convolution qui mène à (41) est une application standard de l'inégalité de réarrangement d'O'Neil, sous réserve que la représentation de Biot–Savart de `u` par `ω` soit effectivement valable dans la classe de fonctions considérée.
3. Les puissances annoncées dans les deux inversions sont cohérentes :
   \[
   \mu_\omega(\lambda)\lesssim \lambda^{-3/2}(\log\lambda)^{-3/2}
   \quad\Longrightarrow\quad
   \omega^*(s)\lesssim s^{-2/3}(\log(1/s))^{-1},
   \]
   puis
   \[
   u^*(s)\lesssim s^{-1/3}(\log(1/s))^{-1}
   \quad\Longrightarrow\quad
   \mu_u(\lambda)\lesssim \lambda^{-3}(\log\lambda)^{-3}.
   \]
   Elles sont toutefois obtenues dans le manuscrit par des équivalences asymptotiques, sans lemme quantifié donnant les constantes et les seuils uniformes.
4. L'égalité utilisée dans (48), `λ = u*(|{|u|>λ}|)`, est fausse en général avec la définition standard de la réarrangée décroissante. Les plateaux de la fonction de distribution suffisent à la réfuter. L'implication recherchée reste réparable par une propriété d'inverse généralisé ; un lemme explicite est donné ci-dessous.
5. Les logarithmes de (40), (47) et (49) portent sur des quantités dimensionnées et les seuils nécessaires ne sont pas explicités. Ils doivent être remplacés par des rapports à des échelles de référence, et les énoncés doivent préciser respectivement `λ ≥ λ_*`, `0 < s ≤ s_*` et `λ ≥ λ_{u,*}`.

Ce constat ne valide ni n'invalide le théorème complet. Il identifie un trou local, réparable pour (47) → (49), et des prérequis distincts en amont.

## Conventions exactes

Pour une fonction mesurable `f` sur un espace de mesure non atomique, on fixe

\[
\mu_f(\lambda)=\bigl|\{x:|f(x)|>\lambda\}\bigr|,
\qquad
f^*(s)=\inf\{\lambda\ge 0:\mu_f(\lambda)\le s\},
\]

et

\[
f^{**}(s)=\frac1s\int_0^s f^*(r)\,dr.
\]

Le manuscrit indique seulement que `f*` est la réarrangée décroissante ; il ne fixe pas la convention d'inverse généralisé, ni `f**`. Avec la convention ci-dessus, les implications utilisables sont

\[
\mu_f(\lambda)>s\ \Longrightarrow\ f^*(s)\ge\lambda,
\qquad
f^*(s)<\lambda\ \Longrightarrow\ \mu_f(\lambda)\le s,
\]

mais pas l'identité `f*(μ_f(λ))=λ`.

**Contre-exemple reproductible à (48).** Soit `f=a 1_E`, avec `0<|E|=m<∞`, et soit `λ=a/2`. Alors `μ_f(λ)=m`, tandis que, pour la convention ci-dessus, `f*(m)=0`. Ainsi `λ≠f*(μ_f(λ))`. Changer la convention aux points de saut peut changer la valeur au bord, mais ne rend pas vraie une identité universelle sur les plateaux.

## Source primaire d'O'Neil et portée de (41)

La source primaire est Richard O'Neil, « Convolution operators and `L(p,q)` spaces », *Duke Mathematical Journal* **30** (1963), 129–142, DOI [10.1215/S0012-7094-63-03015-1](https://doi.org/10.1215/S0012-7094-63-03015-1), avec notice et texte sur [Project Euclid](https://projecteuclid.org/journals/duke-mathematical-journal/volume-30/issue-1/Convolution-operators-and-Lpq-spaces/10.1215/S0012-7094-63-03015-1.full).

La forme standard pertinente est

\[
(f*g)^{**}(s)
\le s f^{**}(s)g^{**}(s)
   +\int_s^\infty f^*(r)g^*(r)\,dr.
\]

Pour le noyau de Biot–Savart de taille `|x|^{-2}` dans `R³`,

\[
K^*(s)=c_3s^{-2/3},
\qquad
K^{**}(s)=3c_3s^{-2/3}.
\]

Comme `(f*g)*(s)≤(f*g)**(s)`, la substitution donne, à constante dimensionnelle près,

\[
u^*(s)
\le C\left(
s^{-2/3}\int_0^s\omega^*(r)\,dr
+\int_s^\infty r^{-2/3}\omega^*(r)\,dr
\right),
\]

qui est bien (41). Cette étape est **classique et sourcée**.

Elle ne contrôle toutefois que la partie reconstruite par Biot–Savart. Sur `R³`, une hypothèse de décroissance ou d'intégrabilité, ou une normalisation éliminant la composante harmonique, est nécessaire. Un champ de vitesse constant a une vorticité nulle et n'est pas reconstruit par `curl(-Δ)^{-1}ω`. Ce prérequis ne relève pas de l'inversion (47) → (49), mais doit être énoncé avant d'appliquer (41).

## Audit équation par équation

| Passage | Statut vérifié | Réserve ou correction nécessaire |
|---|---|---|
| (40) | Forme de queue compatible avec l'enveloppe annoncée pour `ω*`. | L'affichage doit porter `λ≥λ_ω,*`; `log λ` doit être adimensionné. |
| (40) → remarque 5.1 | Puissances correctes, au sens asymptotique. | L'inversion doit employer l'inverse généralisé. Une formule exacte fait intervenir la fonction de Lambert `W`; une simple relation `≈` ne fournit pas une borne uniforme. |
| (41) | Conséquence standard de l'inégalité d'O'Neil pour le noyau `|x|^{-2}`. | Vérifier la représentation de Biot–Savart et l'absence, ou le contrôle séparé, de la composante harmonique. |
| (42)–(43) | Substitution correcte. Le signe du reste dans (43) est correct. | Pour une borne supérieure, l'asymptotique est inutile : `log(e/r)≥log(e/s)` pour `0<r≤s≤1`, donc le terme est au plus `3s^{-1/3}/log(e/s)`. |
| (44)–(45) | Découpage et contrôle de la queue large corrects si `ω∈L^{3/2,∞}` : `∫_1^∞r^{-4/3}dr=3`. | Le point de découpage `1` suppose une normalisation de la mesure. |
| (46) | L'équivalent principal est correct et le signe du reste positif est correct. | L'égalité écrite ne donne pas à elle seule une borne uniforme par le terme principal. Il faut une estimation du reste, par régularité lente/Karamata ou par un découpage dyadique, et fixer `0<s≤s_0`. |
| (47) | Conséquence réparable de (41) si les enveloppes précédentes sont des inégalités uniformes. | Le manuscrit passe d'équivalences à une inégalité sans suivre seuils et constantes. La notation `L^{3,∞}(log L)` n'est pas définie sur l'espace de mesure infinie. |
| (48) | Heuristique d'inversion correcte au premier ordre. | L'égalité `λ=u*(μ_u(λ))` est fausse en général. |
| (49) | Exposants `3` et `-3` corrects. | Nécessite le lemme d'inverse généralisé ci-dessous, une amplitude de référence et un seuil de grande amplitude. |

## Réparation quantitative de (47) → (49)

### Lemme d'inversion

Soient `A>0` et `s₀>0`. Supposons que, pour tout `0<s≤s₀`,

\[
f^*(s)\le
\frac{A s^{-1/3}}{\log(e s_0/s)}.
\tag{R47}
\]

Alors, pour

\[
q=\frac{\lambda s_0^{1/3}}{A}\ge2,
\qquad
W_q=\log(e+q),
\]

on a

\[
\mu_f(\lambda)
\le
\frac{8A^3}{\lambda^3W_q^3}.
\tag{R49}
\]

En particulier, la constante et le seuil sont explicites et uniformes dans un paramètre supplémentaire, par exemple le temps, dès que `A` et `s₀` le sont.

### Preuve

Posons

\[
s_\lambda=s_0\left(\frac{2}{qW_q}\right)^3.
\]

Pour `q≥2`, on a `s_λ≤s₀` et

\[
\frac{A s_\lambda^{-1/3}}
{\log(e s_0/s_\lambda)}
=
\frac{\lambda W_q}
{2\,[1+3\log(qW_q/2)]}
<\lambda.
\]

Par (R47), `f*(s_λ)<λ`. La propriété d'inverse généralisé donne donc `μ_f(λ)≤s_λ`. Enfin,

\[
s_\lambda
=\frac{8A^3}{\lambda^3W_q^3},
\]

ce qui prouve (R49). Cette preuve remplace l'égalité incorrecte de (48) par une implication valide et ne requiert aucune continuité de la fonction de distribution.

### Contrôle de l'exposant logarithmique

L'équation modèle

\[
\lambda=\frac{A s^{-1/3}}{\log(e s_0/s)}
\]

donne, avec `y=(s₀/s)^{1/3}`, une relation du type `q≈y/(3 log y)`. Son inversion donne `y≈q log q`, donc

\[
s\asymp \frac{A^3}{\lambda^3[\log(\lambda s_0^{1/3}/A)]^3}.
\]

Le facteur logarithmique de (49) n'est donc pas une erreur d'exposant ; le défaut est le manque de quantification et l'usage d'une fausse identité d'inversion.

## Inversion de (40) et distinction « standard / asymptotique »

Après adimensionnement, supposons par exemple

\[
\mu_\omega(\lambda)
\le
\frac{B}{\lambda^{3/2}[\log(\lambda/\lambda_0)]^{3/2}},
\qquad \lambda\ge e\lambda_0.
\]

Élever la relation modèle à la puissance `2/3` conduit à

\[
\lambda\log(\lambda/\lambda_0)
=B^{2/3}s^{-2/3}.
\]

Son inversion exacte est exprimable avec la fonction de Lambert `W` : si

\[
X=\frac{B^{2/3}}{\lambda_0s^{2/3}},
\]

alors l'amplitude modèle vaut

\[
\lambda=\frac{B^{2/3}s^{-2/3}}{W(X)}.
\]

Comme `W(X)~log X`, on retrouve l'enveloppe `s^{-2/3}/log(1/s)`. Le fait que les puissances soient les bonnes est donc **standard au sens de la variation régulière**. En revanche, le manuscrit n'explicite ni le lemme d'inverse généralisé, ni le seuil `s≤s_ω,*`, ni les comparaisons quantitatives de `W(X)` nécessaires à une inégalité uniforme. Cette partie est seulement **asymptotique telle qu'elle est écrite**.

## Logarithmes, unités et seuils manquants

Les expressions `log λ` et `log(e/s)` ne sont invariantes ni sous changement d'unités d'amplitude ni sous changement d'unité de volume. Une formulation covariante doit employer, par exemple,

\[
\log\!\left(e+\frac{\lambda}{\lambda_{\rm ref}}\right),
\qquad
\log\!\left(\frac{e s_{\rm ref}}s\right).
\]

Le choix implicite `s_ref=1`, visible dans le découpage de (44), doit être déclaré comme une normalisation. Sinon, un simple changement d'échelle spatiale modifie le logarithme sans suivre la loi d'échelle de Navier–Stokes.

Les versions quantifiées minimales des trois affichages doivent donc contenir :

- (40) : `λ≥λ_ω,*`, avec `λ/λ_ref` dans le logarithme ;
- (47) : `0<s≤s_u,*`, avec `s/s_ref` dans le logarithme ;
- (49) : `λ≥λ_u,*`, avec `λ/λ_ref` dans le logarithme ;
- uniformité en temps : `A`, `s_u,*`, `λ_u,*` et les références indépendants de `t`.

## Portée exacte pour la suite

Le maillon (47) → (49) peut être considéré comme **réparé conditionnellement** par le lemme (R47)–(R49), mais seulement si (47) a préalablement été établi avec une constante et un seuil uniformes. Le présent audit ne certifie pas cette hypothèse : les étapes qui produisent (40), la validité fonctionnelle de Biot–Savart, la fermeture des constantes, et toute implication ultérieure vers un critère de régularité restent hors de ce verdict.

La correction minimale recommandée au manuscrit est donc :

1. définir `μ_f`, `f*` et `f**` ;
2. remplacer (48) par le lemme d'inverse généralisé ;
3. remplacer tous les `≈` utilisés comme bornes par des inégalités avec constantes et seuils ;
4. adimensionner les logarithmes ;
5. définir précisément le quasi-espace noté `L^{3,∞}(log L)`, au moins dans son régime de petite mesure, et contrôler séparément la grande mesure.
