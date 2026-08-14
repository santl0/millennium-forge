# Analyse contradictoire — cycle 0020 : obstruction d’extension `bmo_φ` à deux cœurs opposés

Date : 2026-08-14

Statut : dérivation interne, non publiée, non indépendante au sens inter-familles de modèles

Objet : coût minimal de toute extension mesurable bornée d’une direction prescrite par `+e` et `-e` sur deux cœurs disjoints.

## Verdict exécutif

Soit `D` une boule, un cube ou, plus généralement, un ensemble mesurable de mesure finie positive. Soient `E_+` et `E_-` deux sous-ensembles disjoints de `D`, de fractions volumiques

\[
a=\frac{|E_+|}{|D|},\qquad
b=\frac{|E_-|}{|D|},\qquad a+b>0.
\]

Si une extension mesurable bornée `ξ:D→R³` vérifie `ξ=e` sur `E_+` et `ξ=-e` sur `E_-`, avec `|e|=1`, alors

\[
\frac1{|D|}\int_D|\xi-\xi_D|
\geq \frac{4ab}{a+b}.
\tag{1}
\]

Cette constante est **optimale** parmi toutes les extensions mesurables bornées. Elle reste optimale si l’on impose `|ξ|≤1` presque partout : sur le complément des cœurs, l’extension extrémale est simplement

\[
\xi=\frac{a-b}{a+b}\,e.
\tag{2}
\]

Le corridor de zéros n’impose donc aucun coût supplémentaire par lui-même. Son seul effet, en l’absence de contrainte de régularité ou de module de continuité, est de diluer les fractions `a` et `b` dans le domaine test.

Pour

\[
\phi(r)=\frac1{1+\log(R_*/r)},\qquad 0<r\leq R_*,
\tag{3}
\]

une boule ou un cube test `D` d’échelle `r_D` donne l’obstruction exacte

\[
[\xi]_{bmo_\phi}
\geq
\frac{4ab}{a+b}
\left[1+\log\!\left(\frac{R_*}{r_D}\right)\right].
\tag{4}
\]

Une paire de cœurs opposés à une seule échelle force seulement une norme grande mais finie. Une impossibilité d’extension uniforme exige une suite `D_n`, `r_n→0`, telle que

\[
\frac{4a_nb_n}{a_n+b_n}
\left[1+\log\!\left(\frac{R_*}{r_n}\right)\right]
\longrightarrow +\infty.
\tag{5}
\]

En particulier, « deux directions opposées arbitrairement proches » n’est pas une obstruction suffisante : il faut que les deux cœurs conservent assez de volume relatif. Ce résultat élimine la version trop forte du lemme d’extension fondée sur le seul contraste de directions.

## 1. Cadre exact

Le calcul est purement géométrique. Il ne suppose pas que `ξ` soit la direction d’une solution de Navier–Stokes et ne produit aucune solution de cette équation.

- `D⊂R^d`, `1≤d≤3`, est mesurable, avec `0<|D|<∞`.
- `E_+,E_-⊂D` sont mesurables, disjoints, et `a+b>0`.
- `e∈R^3` est unitaire.
- `ξ:D→R^3` est mesurable et essentiellement bornée.
- Les traces prescrites sont `ξ=e` presque partout sur `E_+` et `ξ=-e` presque partout sur `E_-`.
- `G=D\setminus(E_+∪E_-)` représente le corridor de zéros et tout autre lieu où la direction de vorticité n’est pas prescrite.
- La moyenne et l’oscillation moyenne sont

\[
\xi_D=\frac1{|D|}\int_D\xi,
\qquad
\operatorname{MO}_D(\xi)
=\frac1{|D|}\int_D|\xi-\xi_D|.
\tag{6}
\]

Le fait que la vorticité soit nulle dans `G` signifie seulement que sa direction n’y est pas intrinsèquement définie. Il ne faut pas confondre « corridor où `ω=0` » et contrainte `ξ=0`. Ici `ξ` est précisément l’extension que l’on cherche à choisir sur `G`.

La semi-norme locale utilisée dans ce rapport est

\[
[\xi]_{bmo_\phi}
=\sup_{D}
\frac{\operatorname{MO}_D(\xi)}{\phi(r_D)},
\tag{7}
\]

où le supremum porte sur les boules, ou sur les cubes selon la convention fixée, d’échelle `0<r_D≤R_*`. La norme inhomogène du manuscrit 2026 ajoute `||ξ||_∞`; cette addition ne diminue évidemment pas la borne (4).

## 2. Lemme optimal d’oscillation moyenne

### Lemme 2.1 — deux cœurs antipodaux

Sous les hypothèses de la section 1,

\[
\operatorname{MO}_D(\xi)\geq H(a,b),
\qquad
H(a,b):=\frac{4ab}{a+b}.
\tag{8}
\]

De plus,

\[
\inf_{\substack{\xi\text{ extension mesurable bornée}}}
\operatorname{MO}_D(\xi)
=
\inf_{\substack{\xi\text{ extension mesurable}\\|\xi|\leq1\ \mathrm{p.p.}}}
\operatorname{MO}_D(\xi)
=H(a,b).
\tag{9}
\]

La quantité `H(a,b)` est deux fois la moyenne harmonique de `a` et `b`. Elle est gouvernée par le cœur minoritaire :

\[
2\min(a,b)\leq H(a,b)\leq4\min(a,b).
\tag{10}
\]

### Preuve

Projeter sur `e` ne peut qu’abaisser la distance euclidienne. Posons

\[
g=\xi\cdot e,qquad m=\fint_D g=\xi_D\cdot e,
\qquad s=a+b,qquad d=a-b.
\]

Alors

\[
\operatorname{MO}_D(\xi)
\geq \fint_D|g-m|.
\tag{11}
\]

Sur `E_+` et `E_-`, les contributions normalisées valent respectivement `a|1-m|` et `b|-1-m|`. Sur `G`, Jensen donne

\[
\fint_D\mathbf1_G|g-m|
\geq
\left|\fint_D\mathbf1_G(g-m)\right|.
\]

Or la moyenne globale de `g-m` est nulle, donc

\[
\fint_D\mathbf1_G(g-m)
=-a(1-m)-b(-1-m)=sm-d.
\]

Il vient, pour toute extension,

\[
\operatorname{MO}_D(\xi)
\geq F(m):=
a|1-m|+b|-1-m|+|sm-d|.
\tag{12}
\]

Supposons d’abord `a≥b`, donc `d≥0`. Sur `[-1,1]`,

\[
F(m)=s-dm+|sm-d|.
\]

Cette fonction affine par morceaux décroît jusqu’à

\[
m_*=\frac ds=\frac{a-b}{a+b}
\]

puis croît. Sa valeur minimale est

\[
F(m_*)=s-\frac{d^2}{s}
=\frac{s^2-d^2}{s}
=\frac{4ab}{a+b}.
\tag{13}
\]

Pour `m≥1`, `F(m)=2(sm-d)≥4b`; pour `m≤-1`, `F(m)=2(d-sm)≥4a`. Ces valeurs ne sont pas inférieures à (13). Le cas `b≥a` est symétrique.

Pour atteindre la borne, choisir

\[
\xi(x)=m_*e\quad\text{sur }G.
\tag{14}
\]

La moyenne de cette extension est exactement `m_*e`, sa contribution à l’oscillation sur `G` est nulle, et les deux contributions des cœurs somment à (13). Comme `|m_*|≤1`, cette extension est admissible avec ou sans la contrainte `|ξ|≤1`. Cela prouve (9).

### Ce que change une contrainte plus forte

La contrainte naturelle d’une direction unitaire serait `|ξ|=1` presque partout, et non seulement `|ξ|≤1`. La borne (8) reste valide sous cette contrainte, mais l’extension (14) n’est plus admissible lorsque `a≠0`, `b≠0` et `a≠b`. La constante optimale peut alors être plus grande et dépendre de la capacité à mélanger des directions unitaires sur `G`. Ce problème distinct n’est pas nécessaire pour réfuter une prétention d’extension dans la classe mesurable bornée ou dans la boule unité.

## 3. Choix de centre : moyenne imposée ou meilleure constante

Certaines conventions BMO remplacent la moyenne `ξ_D` par une meilleure constante :

\[
\inf_{c\in\mathbb R^3}\fint_D|\xi-c|.
\tag{15}
\]

Pour cette quantité, le problème analogue a pour valeur exacte

\[
\inf_{\xi\text{ extension}}
\inf_{c\in\mathbb R^3}\fint_D|\xi-c|
=2\min(a,b).
\tag{16}
\]

La borne inférieure découle de l’inégalité triangulaire appliquée aux deux traces `e` et `-e` : pour tout `c`,

\[
a|e-c|+b|-e-c|\geq2\min(a,b).
\]

Elle est atteinte en remplissant le complément par la direction du cœur majoritaire et en choisissant cette même direction comme constante `c`. Ainsi, la convention « moyenne du domaine » donne la constante optimale `4ab/(a+b)`, tandis que la convention « meilleure constante » donne `2 min(a,b)`. Elles coïncident pour `a=b`; leur équivalence qualitative ne justifie pas d’échanger les constantes dans un calcul certifié.

## 4. Conséquence exacte pour `bmo_φ`

Appliquons le lemme à chaque domaine admissible `D` d’échelle `r_D≤R_*`. D’après (3), (7) et (8),

\[
[\xi]_{bmo_\phi}
\geq
H(a,b)\,[1+\log(R_*/r_D)].
\tag{17}
\]

### Corollaire 4.1 — obstruction multi-échelle

S’il existe une suite de domaines tests `D_n`, de rayons ou échelles `r_n→0`, contenant des cœurs antipodaux de fractions `a_n,b_n`, et si

\[
H(a_n,b_n)\,[1+\log(R_*/r_n)]\to+\infty,
\tag{18}
\]

alors aucune extension mesurable bornée ne peut avoir une semi-norme `bmo_φ` finie. Le même énoncé vaut sous `|ξ|≤1`.

Une condition suffisante particulièrement simple est

\[
a_n\geq c_0>0,qquad b_n\geq c_0>0.
\tag{19}
\]

Dans ce cas, le membre de droite de (17) croît logarithmiquement.

À l’inverse, si `a_n=b_n=η_n`, alors

\[
H(a_n,b_n)=2\eta_n.
\tag{20}
\]

Le test ne donne aucune divergence lorsque

\[
\eta_n[1+\log(R_*/r_n)]
\]

reste borné. Il devient même asymptotiquement muet lorsque ce produit tend vers zéro. Cette faiblesse n’est pas un défaut de preuve : l’extension constante (14) montre qu’elle est intrinsèque aux seules données de volume et de signe.

### Cœurs de tailles comparables

Supposons que leurs volumes vérifient

\[
\kappa^{-1}\leq\frac{|E_+|}{|E_-|}\leq\kappa,
\qquad \kappa\geq1,
\tag{21}
\]

et notons leur occupation totale

\[
\sigma=a+b=\frac{|E_+|+|E_-|}{|D|}.
\]

Alors

\[
H(a,b)
\geq
\frac{4\kappa}{(1+\kappa)^2}\,\sigma.
\tag{22}
\]

La comparabilité seule ne suffit donc toujours pas : il faut aussi contrôler l’occupation `σ`. La borne est sûre et optimale pour le pire rapport autorisé par (21).

## 5. Géométrie unidimensionnelle

Considérons deux intervalles cœurs de longueurs `ℓ_+` et `ℓ_-`, séparés par un corridor ouvert de longueur `ε≥0`. Leur plus petit intervalle englobant a longueur

\[
L=\ell_++\epsilon+\ell_-=2\rho,
\tag{23}
\]

où `ρ` est le demi-diamètre. Les fractions sont `a=ℓ_+/L` et `b=ℓ_-/L`. Le lemme donne la valeur optimale

\[
\operatorname{MO}_{I}(\xi)
\geq
\frac{4\ell_+\ell_-}
{(\ell_++\ell_-)(\ell_++\ell_-+\epsilon)}.
\tag{24}
\]

Pour deux cœurs égaux `ℓ_+=ℓ_-=ℓ`,

\[
\operatorname{MO}_{I}(\xi)
\geq
\frac{2\ell}{2\ell+\epsilon}
=\frac{\ell}{\rho}.
\tag{25}
\]

- lorsque `ε→0`, la borne tend vers `1`;
- lorsque `ε≫ℓ`, elle est équivalente à `2ℓ/ε`;
- elle est atteinte en posant `ξ=0` sur le corridor lorsque les cœurs sont égaux.

Si (21) vaut pour les longueurs et si

\[
\epsilon\leq\gamma(\ell_++\ell_-),
\tag{26}
\]

alors `σ≥1/(1+γ)` et

\[
\operatorname{MO}_{I}(\xi)
\geq
\frac{4\kappa}{(1+\kappa)^2(1+\gamma)}.
\tag{27}
\]

Le coût pondéré s’obtient en multipliant (24) ou (27) par

\[
1+\log(R_*/\rho)
\]

si la convention `r_D` est le rayon de l’intervalle.

## 6. Géométrie tridimensionnelle

### 6.1 Deux boules égales dans la plus petite boule englobante

Soient deux cœurs qui sont des boules de rayon `r`, dont les centres sont séparés par `2r+ε`. La plus petite boule contenant les deux cœurs est centrée au milieu des centres et a pour rayon

\[
\rho_B=2r+\frac\epsilon2.
\tag{28}
\]

Les fractions des deux cœurs dans cette boule valent

\[
a=b=\left(\frac r{\rho_B}\right)^3.
\]

Par conséquent,

\[
\operatorname{MO}_{B_{\rho_B}}(\xi)
\geq
2\left(\frac r{2r+\epsilon/2}\right)^3.
\tag{29}
\]

La borne vaut `1/4` lorsque `ε=0`; lorsque `ε≫r`, elle est équivalente à `16(r/ε)^3`. Le coût `bmo_φ` certifié par cette boule est

\[
2\left(\frac r{2r+\epsilon/2}\right)^3
\left[1+\log\!\left(\frac{R_*}{2r+\epsilon/2}\right)\right].
\tag{30}
\]

### 6.2 Deux cubes égaux alignés

Soient deux cubes de côté `ℓ`, alignés et séparés de `ε` dans une direction coordonnée. Leur plus petit cube englobant aligné a côté

\[
L=2\ell+\epsilon.
\tag{31}
\]

On obtient

\[
\operatorname{MO}_{Q_L}(\xi)
\geq
2\left(\frac\ell{2\ell+\epsilon}\right)^3.
\tag{32}
\]

La valeur limite pour `ε=0` est encore `1/4`. Si l’échelle d’un cube est définie par son demi-côté, il faut employer `r_D=L/2` dans `φ`; si elle est définie par son côté, il faut employer `r_D=L`. Ce changement de convention modifie le facteur logarithmique d’une constante additive `log 2`, pas la conclusion multi-échelle.

### 6.3 Forme robuste indépendante de la géométrie fine

Pour des cœurs tridimensionnels quelconques vérifiant (21), toute information géométrique doit finalement fournir une borne inférieure sur

\[
\sigma=\frac{|E_+|+|E_-|}{|D|}.
\]

Le lemme sûr est alors (22). La seule largeur `ε` ne contrôle pas `σ` pour des cœurs filamenteux, fractals, très aplatis ou placés dans un domaine test excessivement grand. Il est donc incorrect de déduire une oscillation d’ordre un de `ε/r→0` sans une hypothèse quantitative de densité ou d’épaisseur.

## 7. Vérification d’échelle et dimensions

La direction `ξ`, les fractions `a,b,σ`, l’oscillation moyenne et la semi-norme `bmo_φ` sont sans dimension. Les longueurs `r`, `ε`, `r_D` et `R_*` ont la dimension d’une longueur; seuls les rapports

\[
\frac\epsilon r,
\qquad
\frac{R_*}{r_D}
\]

entrent dans les formules.

Sous la remise à l’échelle de Navier–Stokes

\[
u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),
\qquad
\omega_\lambda(x,t)=\lambda^2\omega(\lambda x,\lambda^2t),
\]

la direction se transforme selon

\[
\xi_\lambda(x,t)=\xi(\lambda x,\lambda^2t)
\]

là où la vorticité ne s’annule pas. Si toutes les longueurs, y compris `R_*`, sont transformées par `λ^{-1}`, les fractions de volume, `φ`, (8) et (17) sont invariantes. Si `R_*` est une échelle physique extérieure fixée pendant que `r_D→0`, le logarithme croît : c’est précisément le mécanisme de l’obstruction (18).

## 8. Passe contradictoire

### Attaque A — volume faible des cœurs

Prendre `a=b=η`. La valeur exacte est `2η`, qui tend vers zéro avec `η`. Des cœurs opposés peuvent donc être arbitrairement proches et parfaitement cohérents sur chacun d’eux sans coûter une oscillation d’ordre un s’ils occupent un volume relatif négligeable.

**Verdict :** l’énoncé sans hypothèse de densité est réfuté.

### Attaque B — cœur minoritaire évanescent

Si `b/a→0`, alors

\[
H(a,b)\sim4b.
\]

Même un grand cœur `+e` n’empêche pas l’extension si le cœur `-e` disparaît en volume relatif.

**Verdict :** la comparabilité des deux cœurs, ou une borne explicite sur le plus petit, est indispensable.

### Attaque C — remplissage optimal du corridor

Le choix (14) annule exactement la contribution du corridor à l’oscillation autour de la moyenne globale. Pour des cœurs égaux, ce choix est `ξ=0` dans le corridor. Il respecte `|ξ|≤1`.

**Verdict :** imposer seulement une extension mesurable bornée, même dans la boule unité, ne transforme pas une faible largeur de corridor en coût supplémentaire. Une continuité sans borne uniforme sur le gradient ne change que l’atteinte stricte : des couches de transition arbitrairement fines approchent le même infimum.

### Attaque D — domaine englobant trop grand

Ajouter du vide autour des cœurs réduit `a` et `b`. La semi-norme BMO prend un supremum, donc on doit chercher le domaine admissible qui maximise

\[
\frac{H(a_D,b_D)}{\phi(r_D)},
\]

et non choisir automatiquement une boule fortement rembourrée. La plus petite boule ou le plus petit cube englobant est naturel pour les géométries simples ci-dessus, mais son optimalité parmi tous les domaines tests dépend de la forme des cœurs.

**Verdict :** une preuve complète doit exhiber un domaine témoin, pas seulement annoncer l’existence de deux cœurs.

### Attaque E — choix de la moyenne

Remplacer silencieusement `ξ_D` par la meilleure constante change `4ab/(a+b)` en `2 min(a,b)`. Pour des volumes comparables, les deux bornes restent du même ordre; pour des constantes certifiées, elles ne sont pas interchangeables.

**Verdict :** la définition exacte de `bmo_φ` doit accompagner tout lemme d’extension.

### Attaque F — une seule échelle

Le facteur dans (17) est fini pour tout `r_D>0`. Une seule paire de cœurs ne prouve pas l’inexistence d’une extension `bmo_φ`; elle donne seulement une borne inférieure finie sur sa norme.

**Verdict :** l’obstruction forte requiert une suite d’échelles et la divergence quantitative (18).

### Attaque G — statut de la direction aux zéros

Sur `{ω=0}`, `ξ=ω/|ω|` n’est pas définie. Choisir une extension est une donnée supplémentaire. Le lemme montre exactement ce qu’une succession de cœurs antipodaux épais imposerait à toute telle sélection; il ne montre pas que ces cœurs apparaissent pour une solution de Navier–Stokes admissible.

**Verdict :** aucun raccord au problème Clay n’est obtenu sans un mécanisme PDE produisant la géométrie multi-échelle requise.

## 9. Résultat falsifiable et portée

Le résultat positif du cycle est le lemme optimal (8)–(9), avec sa conséquence pondérée (17). Le résultat négatif est tout aussi important : le corridor et le contraste antipodal ne suffisent pas, même sous `|ξ|≤1`; le volume relatif du cœur minoritaire est le paramètre irréductible.

Un test reproductible du prochain cycle peut donc chercher, dans des champs divergence-free construits analytiquement ou numériquement, une suite de domaines `D_n` pour laquelle les quatre quantités

\[
r_n,quad a_n,quad b_n,quad
H(a_n,b_n)[1+\log(R_*/r_n)]
\]

sont mesurées avec bornes d’erreur. Deux résultats seraient discriminants :

1. une divergence certifiée du dernier produit, qui exclurait toute extension globale uniforme `bmo_φ` pour ce champ;
2. une construction multi-échelle avec produit uniformément borné, qui réfuterait l’idée que des inversions de direction seules forcent l’échec de `bmo_φ`.

Cette analyse ne certifie ni blow-up, ni régularité globale, ni occurrence de ces configurations dans une solution de Leray–Hopf, forte ou classique. Elle réduit seulement le premier maillon d’extension à une inégalité exacte et attaquable.

## 10. Statut de revue

La dérivation a été effectuée par un agent de **la même famille de modèle** que l’agent principal. Elle constitue une passe contradictoire séparée au niveau de la tâche et des artefacts, mais pas une revue indépendante inter-familles. Les égalités d’optimisation peuvent être vérifiées mécaniquement par échantillonnage de la fonction affine par morceaux `F`; une certification formelle resterait à produire.
