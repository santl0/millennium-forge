# Passe bibliographique séparée — cycle 0016

**Qualification.** Cette passe a été réalisée séparément de la dérivation principale du cycle. Elle ne constitue pas une revue extérieurement indépendante : elle est produite dans le même environnement de recherche.

**Périmètre.** Statut et texte courant de `arXiv:2607.08866`, équations (40)–(47), source d'O'Neil, prérequis de Biot–Savart sur `R³`, et traitement du reste positif de (46).

**Date de vérification en ligne.** 14 août 2026.

## Verdict

- Le dossier arXiv courant est toujours **v2**, dernière révision le 13 juillet 2026. Le dossier ne liste ni v3 ni référence de revue. Le statut primaire vérifiable est donc « prépublication arXiv v2 » ; la date « August 11, 2026 » inscrite dans le corps HTML n'est pas une nouvelle version arXiv ([notice arXiv](https://arxiv.org/abs/2607.08866), [texte v2](https://arxiv.org/html/2607.08866v2), DOI DataCite [10.48550/arXiv.2607.08866](https://doi.org/10.48550/arXiv.2607.08866)).
- L'équation (41) est bien la spécialisation attendue de l'inégalité de convolution de Richard O'Neil au noyau `|x|⁻²`.
- L'application à la vitesse entière demande néanmoins une normalisation de Biot–Savart absente des hypothèses affichées du théorème 7.4 : `u₀∈L∞(R³)` n'élimine pas une composante harmonique constante.
- Le reste positif de (46) **ne reçoit aucune borne uniforme dans le texte**. Plus précisément, ce reste n'est pas `O(1)` quand `v↓0` : il diverge comme `9v⁻¹/³/log²(e/v)`. Il est seulement d'ordre inférieur au terme principal. Une majoration relative uniforme est possible, mais n'est pas écrite.
- Par conséquent, le passage (46) → (47) est réparable localement, mais la constante et le seuil de petite mesure proclamés uniformes ne sont pas établis dans la version consultée.

Le présent verdict est limité à (40)–(47) et ne valide pas le théorème complet.

## Statut et hypothèses effectivement présentes

Le manuscrit de Zoran Grujić traite les Navier–Stokes incompressibles visqueuses en dimension trois sur `R³`, sur l'intervalle terminal

\[
I=(T^*-\varepsilon,T^*),
\]

où `T*` est supposé être le premier temps singulier possible et `ν>0` apparaît dans l'inégalité de vorticité. Dans le passage audité, \(\omega=|\boldsymbol{\omega}|\) désigne la norme de la vorticité.

Les hypothèses utilisées en amont de (40) sont les suivantes ([définition 2.1 et théorème 4.1 du texte v2](https://arxiv.org/html/2607.08866v2)) :

1. singularité ponctuelle critique centrée à l'origine, avec `ω(x,t)=Φ(x,t)|x|⁻²` ;
2. facteur `Φ` supposé invariant d'échelle ou log-périodique au cœur, uniformément borné, avec `|∇Φ|≲|x|⁻¹` uniformément en temps ;
3. confinement des hauts super-niveaux `A_λ(t)` dans une boule de rayon `R≤Cλ⁻¹/²`, avec `C` indépendant du temps ;
4. `ω∈L∞(I;L^{3/2,∞}(R³))`, de borne notée `M₀` ;
5. \(\boldsymbol{\xi}=\boldsymbol{\omega}/|\boldsymbol{\omega}|\in L^\infty(I;\mathrm{bmo}_{1/|\log r|}(\mathbb R^3))\) ;
6. solution unique et spatialement analytique sur `(0,T*)`, issue dans le théorème 7.4 d'une donnée `u₀∈L∞(R³)`.

Deux seuils de troncature apparaissent avant (40) :

- `λ≥λ₀`, afin d'absorber le terme non linéaire par `C_S²||α||_{L^{3/2,∞}(A_λ)}≤ν/2` ;
- `λ≥Λ₀=||ω(·,T*−ε)||∞`, afin que la vorticité tronquée soit nulle au temps d'ancrage.

Ainsi, la dérivation de (40) exige au minimum `λ≥max(λ₀,Λ₀)` — et en pratique `λ>1` pour que `log λ` soit positif — bien que ce seuil ne figure pas dans l'affichage (40).

## Extraction fidèle de (40)–(47)

Les affichages suivants reproduisent le contenu mathématique de la [version HTML primaire v2, sections 5.3 et 6](https://arxiv.org/html/2607.08866v2).

### Distribution de la vorticité

\[
\sup_{t\in(T^{*}-\epsilon,T^{*})}
\left|\left\{x\in\mathbb{R}^{3}:\omega(x,t)>\lambda\right\}\right|
\leq
\frac{C_{\omega}}
{\lambda^{3/2}(\log\lambda)^{\gamma_{1}}},
\quad\text{where}\quad
\gamma_{1}=\frac32.
\tag{40}
\]

**Hypothèses attachées.** Toutes celles listées ci-dessus ; `λ` doit provenir du régime de haute troncature. Le texte affirme que `C_ω` dépend seulement de paramètres uniformes en temps, mais l'affichage omet le seuil de `λ`.

La remarque 5.1 interposée entre (40) et (41) affirme, par une inversion écrite avec `v≈λ⁻³/²(log λ)⁻³/²`, que, pour petite mesure,

\[
\omega^*(v,t)\le C v^{-2/3}\log^{-1}(e/v).
\]

Aucun seuil `0<v≤v₀`, aucune convention d'inverse généralisé et aucune constante d'inversion n'y sont donnés.

### Inégalité de convolution

\[
u^{*}(v,t)\leq C\left(
v^{-2/3}\int_{0}^{v}\omega^{*}(s,t)\,ds
+\int_{v}^{\infty}s^{-2/3}\omega^{*}(s,t)\,ds
\right).
\tag{41}
\]

**Hypothèses attachées.** Le texte pose que la vitesse est donnée par le potentiel de Riesz d'ordre un associé à Biot–Savart, que `K*(s)∼s⁻²/³`, et emploie O'Neil. L'estimation améliorée de `ω*` est annoncée pour « small `s` », uniformément en `t∈I`; le contrôle global de base est `ω*(s,t)≤M₀s⁻²/³`.

### Noyau de Hardy

\[
v^{-2/3}\int_{0}^{v}s^{-2/3}\log^{-1}(e/s)\,ds.
\tag{42}
\]

\[
v^{-2/3}\left[
3s^{1/3}\log^{-1}(e/s)\Big|_{0}^{v}
-\int_{0}^{v}3s^{1/3}\frac{1}{s\log^{2}(e/s)}\,ds
\right]
\approx
3v^{-1/3}\log^{-1}(e/v).
\tag{43}
\]

**Hypothèses attachées.** `v` est dans le régime de petite mesure. Le signe négatif du reste est correct. Pour la seule majoration nécessaire à (47), on a directement, pour `0<v≤1`,

\[
v^{-2/3}\int_0^v\frac{s^{-2/3}}{\log(e/s)}\,ds
\le \frac{3v^{-1/3}}{\log(e/v)},
\]

donc cette partie ne requiert pas l'équivalence asymptotique.

### Queue macroscopique

\[
\int_{v}^{\infty}s^{-2/3}\omega^{*}(s,t)\,ds
=\int_{v}^{1}s^{-2/3}\omega^{*}(s,t)\,ds
+\int_{1}^{\infty}s^{-2/3}\omega^{*}(s,t)\,ds.
\tag{44}
\]

\[
\int_{1}^{\infty}s^{-2/3}\omega^{*}(s,t)\,ds
\leq M_{0}\int_{1}^{\infty}s^{-4/3}\,ds
=3M_{0}=O(1).
\tag{45}
\]

\[
\left[-3s^{-1/3}\log^{-1}(e/s)\right]_{v}^{1}
+\int_{v}^{1}3s^{-1/3}\frac{1}{s\log^{2}(e/s)}\,ds
\approx
3v^{-1/3}\log^{-1}(e/v)+O(1).
\tag{46}
\]

**Hypothèses attachées.** Le découpage impose `0<v<1`. (45) utilise le contrôle faible global. (46) substitue l'enveloppe logarithmique sur tout `[v,1]`, alors que la phrase précédente ne l'avait affirmée que pour petite mesure. Si elle n'est disponible que jusqu'à `s₀<1`, il faut découper `[v,s₀]∪[s₀,1]` et traiter le second morceau avec le contrôle global.

### Conclusion revendiquée

\[
u^{*}(v,t)\leq Cv^{-1/3}\log^{-1}(e/v).
\tag{47}
\]

**Hypothèses attachées.** Le texte vise `v→0`, uniformément pour `t∈I`, et dit que `C` est indépendant du temps. Aucun seuil `v₀`, aucune constante issue du reste de (46), et aucune définition globale du quasi-espace noté `L^{3,∞}(log L)` ne sont fournis.

## Source primaire exacte d'O'Neil

La référence `[33]` du manuscrit est exactement :

> Richard O'Neil, “Convolution operators and `L(p,q)` spaces”, *Duke Mathematical Journal* **30**(1), 129–142 (1963).

- DOI primaire : [10.1215/S0012-7094-63-03015-1](https://doi.org/10.1215/S0012-7094-63-03015-1)
- notice de l'éditeur : [Project Euclid](https://projecteuclid.org/journals/duke-mathematical-journal/volume-30/issue-1/Convolution-operators-and-Lpq-spaces/10.1215/S0012-7094-63-03015-1.full)

La forme de l'inégalité de réarrangement utilisée ici est

\[
(f*g)^{**}(v)
\le
v f^{**}(v)g^{**}(v)
+\int_v^\infty f^*(s)g^*(s)\,ds,
\qquad
f^{**}(v)=\frac1v\int_0^v f^*(s)\,ds.
\]

Pour `g(x)=c|x|⁻²` dans `R³`,

\[
g^*(s)=c_3s^{-2/3},
\qquad
g^{**}(s)=3c_3s^{-2/3}.
\]

En combinant `(f*g)*(v)≤(f*g)**(v)` avec `f=|ω|`, on obtient (41), à une constante dimensionnelle près. L'attribution à O'Neil et la forme de (41) sont donc correctes.

## Biot–Savart sur `R³` : condition manquante

Pour un champ suffisamment régulier satisfaisant

\[
\nabla\cdot u=0,
\qquad
\nabla\times u=\boldsymbol\omega,
\]

l'identité vectorielle donne \(-\Delta u=\nabla\times\boldsymbol{\omega}\). Un représentant particulier est

\[
\mathcal B[\boldsymbol\omega](x)
=\frac{1}{4\pi}\int_{\mathbb R^3}
\frac{x-y}{|x-y|^3}\times\boldsymbol\omega(y)\,dy,
\]

à un choix de signe équivalent selon l'ordre du produit vectoriel. Mais

\[
h=u-\mathcal B[\boldsymbol\omega]
\]

vérifie `curl h=div h=0`, donc chaque composante de `h` est harmonique. La vorticité détermine la vitesse seulement après avoir éliminé cette composante.

Des sources de référence primaires explicites sont :

- Thomas Y. Hou et Xinwei Yu, *Introduction to the Theory of Incompressible Inviscid Flows*, équation (2.9), qui précise immédiatement que `u(x)` doit tendre vers zéro à l'infini pour que la formule tienne ([PDF des auteurs](https://math.stanford.edu/~ryzhik/SCHOOL-13/hou_notes.pdf)) ;
- Andrew J. Majda et Andrea L. Bertozzi, *Vorticity and Incompressible Flow*, chapitre 2, formulation vorticité–courant et décomposition de Hodge, Cambridge University Press, DOI [10.1017/CBO9780511613203](https://doi.org/10.1017/CBO9780511613203), [notice officielle](https://www.cambridge.org/core/books/vorticity-and-incompressible-flow/393C35E544EDD0711CAA7F7AB05D7432).

Conditions suffisantes usuelles :

- `u(x)→0` quand `|x|→∞` ; ou
- `u∈L^p(R³)` pour un `1<p<∞`, ce qui exclut le mode harmonique dans la décomposition de Hodge ; en particulier `u∈L²` convient ; ou
- une normalisation explicite de la valeur à l'infini ou du mode harmonique.

Sous la seule hypothèse `u∈L∞`, Liouville implique seulement que `h` est une constante spatiale, pas qu'elle est nulle. Le champ constant non nul fournit le test minimal : \(\boldsymbol{\omega}=0\), tandis que `u≠0`; (41) donnerait pourtant `u*=0`. Il faut donc appliquer (41) à `u−h`, imposer `h=0`, ou contrôler séparément la translation constante. Le théorème 7.4 n'énonce aucune de ces trois options.

L'hypothèse globale `ω∈L^{3/2,∞}` rend, quant à elle, le membre droit d'O'Neil fini : avec `ω*(s)≤M₀s⁻²/³`, les intégrales de (41) se comportent comme `∫₀^v s⁻²/³ds` et `∫_v^∞s⁻⁴/³ds`. Elle contrôle donc le potentiel de Biot–Savart, mais elle ne détermine pas la composante harmonique de `u`.

## Le reste de (46) n'est pas uniformément borné

Posons `L(s)=log(e/s)`. L'intégration par parties exacte est

\[
\int_v^1\frac{s^{-4/3}}{L(s)}\,ds
=\left[-\frac{3s^{-1/3}}{L(s)}\right]_v^1
+R(v),
\qquad
R(v)=3\int_v^1\frac{s^{-4/3}}{L(s)^2}\,ds.
\]

Le manuscrit qualifie correctement `R(v)` de reste positif, mais ne le majore ensuite par aucune inégalité. Il passe directement à `≈3v⁻¹/³/L(v)+O(1)`, puis la phrase suivante absorbe seulement la queue physique `O(1)` de (45).

Or, pour `0<v≤1/2`, une minoration sur `[v,2v]` donne

\[
R(v)
\ge
3\int_v^{2v}\frac{s^{-4/3}}{L(s)^2}\,ds
\ge
3\,2^{-4/3}\frac{v^{-1/3}}{L(v)^2}
\xrightarrow[v\downarrow0]{}\infty.
\]

Ainsi, `R(v)` n'est pas `O(1)`. La théorie standard des fonctions à variation régulière — ou une seconde intégration par parties suivie d'un découpage dyadique — donne plus précisément

\[
R(v)\sim 9\frac{v^{-1/3}}{L(v)^2}
=o\!\left(\frac{v^{-1/3}}{L(v)}\right).
\]

Ce fait permettrait de choisir `v₀>0` et une constante `C` tels que

\[
\int_v^1\frac{s^{-4/3}}{L(s)}\,ds
\le C\frac{v^{-1/3}}{L(v)},
\qquad 0<v\le v_0,
\]

mais cette borne, son seuil et sa constante ne figurent pas dans v2.

## Conclusion falsifiable

1. **O'Neil → (41) :** source et calcul de noyau confirmés.
2. **Biot–Savart → vitesse entière :** hypothèse de normalisation manquante pour la classe `L∞(R³)` affichée ; contre-test constant immédiat.
3. **(46) :** l'assertion implicite « reste `O(1)` » est réfutée par la minoration ci-dessus.
4. **(46) → (47) :** résultat localement réparable parce que le reste est relativement petit, mais aucune borne uniforme correspondante n'est démontrée dans le texte.
5. **Statut :** prépublication arXiv v2 au 14 août 2026 ; aucune nouvelle version primaire repérée.
