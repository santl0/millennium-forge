# Passe analytique contradictoire — cycle 0025 : train de blobs critiques compacts

Date : 2026-08-14

Statut : **dérivation IA interne**, non publiée, jamais `PAPER_PROOF`; aucun énoncé dynamique de Navier–Stokes n’est revendiqué

## Verdict exécutif

Le train proposé peut être construit rigoureusement après avoir fixé

\[
r_n=2^{-n},
\qquad
\ell_n=c\frac{r_n}{n},
\qquad
c=\frac14,
\qquad
x_n=r_ne_3,
\qquad n\geq1.
\tag{1}
\]

Avec

\[
f(t)=(1-t^2)^4_+,
\qquad
\psi(x,y,z)=f(x)f(y)f(z),
\tag{2}
\]

et

\[
U_0=(\partial_y\psi,-\partial_x\psi,0),
\qquad
W_0=\nabla\times U_0,
\tag{3}
\]

les champs remis à l’échelle

\[
U_n(x)=\ell_n^{-1}
U_0\left(\frac{x-x_n}{\ell_n}\right),
\qquad
W_n(x)=\ell_n^{-2}
W_0\left(\frac{x-x_n}{\ell_n}\right)
\tag{4}
\]

ont des supports cubiques deux à deux disjoints. Les sommes

\[
U=\sum_{n=1}^{\infty}U_n,
\qquad
W=\sum_{n=1}^{\infty}W_n
\tag{5}
\]

vérifient dans `D'(R³)`

\[
\operatorname{div}U=0,
\qquad
\nabla\times U=W,
\qquad
\operatorname{div}W=0.
\tag{6}
\]

Le champ de vitesse a une énergie finie exacte :

\[
\|U\|_2^2
=E_0\sum_{n\geq1}\ell_n
=\frac{E_0\log2}{4},
\tag{7}
\]

où

\[
E_0=\|U_0\|_2^2
=\frac{1125899906842624}{539065498096125}
\approx2.0886142979.
\tag{8}
\]

La vorticité totale appartient uniformément à faible-`L^{3/2}` : si

\[
M_0=\|W_0\|_\infty\leq17,
\]

alors

\[
\boxed{
\|W\|_{L^{3/2,\infty}}
\leq
\left(\frac{64}{7}\right)^{2/3}M_0}.
\tag{9}
\]

La même constante vaut pour toutes les sommes partielles. Pourtant chaque blob porte la masse critique forte constante

\[
\int_{\mathbb R^3}|W_n|^{3/2}dx
=K_0
:=\int_{\mathbb R^3}|W_0|^{3/2}dx>0,
\tag{10}
\]

si bien que `W` n’appartient pas à `L^{3/2}` fort.

Le facteur angulaire associé à l’écriture `W=r^{-2}\Omega` n’est pas uniformément borné. Au centre du blob,

\[
W_0(0)=16e_3
\]

et donc

\[
\boxed{
|x_n|^2|W_n(x_n)|
=256n^2}.
\tag{11}
\]

Le train réalise ainsi exactement le mécanisme « masse critique constante + fraction angulaire décroissante + amplitude angulaire d’ordre `n²` ». Il ne satisfait pas l’hypothèse uniforme `\Phi\leq M` du cycle 0024.

Enfin, si la direction est prolongée par zéro hors de `{W\neq0}`, chaque face régulière `x=1` d’un blob fournit une boule de rayon `\ell_n/16` sur laquelle

\[
\boxed{
\operatorname{MO}(\zeta)\geq\frac1{8192}}.
\tag{12}
\]

Ces rayons tendent vers zéro. Le prolongement par zéro n’appartient donc à aucun espace pondéré dont les oscillations doivent décroître comme `1/[1+log(R_*/r)]`. Cette conclusion concerne ce prolongement précis; elle n’exclut pas toutes les extensions mesurables possibles de la direction.

## 1. Champ de base et régularité

La fonction `f` est `C³` à support dans `[-1,1]`; ses trois premières dérivées se raccordent à zéro aux extrémités. Ainsi

\[
\psi\in C_c^3(\mathbb R^3),
\qquad
U_0\in C_c^2(\mathbb R^3;\mathbb R^3),
\qquad
W_0\in C_c^1(\mathbb R^3;\mathbb R^3).
\tag{13}
\]

Le support est contenu dans le cube

\[
Q_0=[-1,1]^3.
\tag{14}
\]

Dans l’intérieur de ce cube,

\[
f'(t)=-8t(1-t^2)^3,
\qquad
f''(t)=8(1-t^2)^2(7t^2-1).
\tag{15}
\]

Les composantes de la vorticité sont

\[
\begin{aligned}
(W_0)_1&=f'(x)f(y)f'(z),\\
(W_0)_2&=f(x)f'(y)f'(z),\\
(W_0)_3&=-f(z)
\left[f''(x)f(y)+f(x)f''(y)\right].
\end{aligned}
\tag{16}
\]

En particulier,

\[
W_0(0,0,0)=16e_3,
\tag{17}
\]

donc `W₀` n’est pas identiquement nul et `K₀>0` dans (10).

Les bornes élémentaires

\[
\|f\|_\infty=1,
\qquad
\|f'\|_\infty
=\frac{1728}{343\sqrt7},
\qquad
\|f''\|_\infty=8
\tag{18}
\]

donnent

\[
|W_0|
\leq
\sqrt{
2\left(\frac{1728}{343\sqrt7}\right)^4
+16^2}
<17.
\tag{19}
\]

### Divergence et curl au niveau de base

Par commutation des dérivées distributionnelles,

\[
\operatorname{div}U_0
=\partial_x\partial_y\psi
-\partial_y\partial_x\psi
=0.
\tag{20}
\]

La définition même de `W₀` donne

\[
\nabla\times U_0=W_0,
\qquad
\operatorname{div}W_0
=\operatorname{div}(\nabla\times U_0)=0
\tag{21}
\]

dans les distributions. La régularité (13) exclut tout terme de surface caché sur les faces du cube.

## 2. Scaling exact

Pour `y=(x-x_n)/ℓ_n`,

\[
\nabla_x=\ell_n^{-1}\nabla_y.
\]

Les identités (20)–(21) donnent donc

\[
\operatorname{div}U_n
=\ell_n^{-2}
(\operatorname{div}U_0)(y)=0,
\tag{22}
\]

\[
\nabla\times U_n
=\ell_n^{-2}(\nabla\times U_0)(y)
=W_n,
\tag{23}
\]

et

\[
\operatorname{div}W_n
=\ell_n^{-3}
(\operatorname{div}W_0)(y)=0.
\tag{24}
\]

Les normes se transforment selon

\[
\|U_n\|_2^2
=\ell_n\|U_0\|_2^2,
\tag{25}
\]

\[
\|W_n\|_1
=\ell_n\|W_0\|_1,
\qquad
\int|W_n|^{3/2}dx
=\int|W_0|^{3/2}dx,
\tag{26}
\]

et

\[
\|W_n\|_{6/5}^{6/5}
=\ell_n^{3/5}
\|W_0\|_{6/5}^{6/5}.
\tag{27}
\]

Les exposants de (26) montrent directement la criticalité de `L^{3/2}`.

## 3. Séparation des supports

Le support du blob `n` est contenu dans

\[
Q_n=x_n+\ell_n[-1,1]^3.
\tag{28}
\]

Les centres sont alignés sur l’axe `e₃`. Pour deux indices consécutifs,

\[
\begin{aligned}
(r_n-\ell_n)
-(r_{n+1}+\ell_{n+1})
&=r_n\left[
\frac12
-c\left(\frac1n+\frac1{2(n+1)}\right)
\right].
\end{aligned}
\tag{29}
\]

Avec `c=1/4`, le crochet est minimal pour `n=1` et vaut

\[
\frac12-\frac14\left(1+\frac14\right)
=\frac3{16}>0.
\tag{30}
\]

Les intervalles de support en `z` sont donc strictement disjoints; les cubes `Q_n` le sont aussi. Les cubes non consécutifs sont séparés par ordre sur l’axe.

De plus,

\[
r_n-\ell_n
=r_n\left(1-\frac1{4n}\right)>0,
\tag{31}
\]

donc aucun support ne contient l’origine. Ils s’y accumulent néanmoins quand `n→∞`.

## 4. Énergie finie et constantes de base

Posons

\[
A=\int_{-1}^{1}f(t)^2dt,
\qquad
D=\int_{-1}^{1}f'(t)^2dt.
\]

L’intégration des polynômes donne exactement

\[
A=\frac{65536}{109395},
\qquad
D=\frac{131072}{45045}.
\tag{32}
\]

Les deux composantes de `U₀` ont la même norme, d’où

\[
E_0
=2A^2D
=\frac{1125899906842624}{539065498096125}.
\tag{33}
\]

Comme les supports sont disjoints,

\[
\|U\|_2^2
=\sum_{n\geq1}\|U_n\|_2^2
=E_0c\sum_{n\geq1}\frac{2^{-n}}n.
\]

L’identité

\[
\sum_{n\geq1}\frac{2^{-n}}n=\log2
\]

prouve (7).

En revanche,

\[
\|\nabla U_n\|_2^2
=\ell_n^{-1}\|\nabla U_0\|_2^2,
\tag{34}
\]

et la somme des `ℓ_n^{-1}` diverge. Le champ construit n’appartient pas à `H¹`; l’énergie finie ne doit pas être confondue avec une enstrophie finie.

## 5. Passage distributionnel à la somme et point d’accumulation

Les sommes partielles `U^(N)=sum_{n≤N}U_n` convergent vers `U` dans `L²`, par (7). De même,

\[
\sum_{n\geq1}\|W_n\|_1
=\|W_0\|_1c\log2<\infty,
\tag{35}
\]

donc les sommes partielles de `W` convergent dans `L¹`.

Les opérateurs différentiels sont continus de `D'` dans `D'`. En passant à la limite dans (22)–(24), on obtient (6). En particulier, aucun delta de divergence ou de curl n’apparaît à l’origine : la queue de vorticité a une norme `L¹`

\[
\sum_{n\geq N}\|W_n\|_1
\longrightarrow0.
\tag{36}
\]

Cette conclusion est distributionnelle, pas classique. Dans toute boule centrée à l’origine, certains blobs ont des amplitudes

\[
\|U_n\|_\infty
=\ell_n^{-1}\|U_0\|_\infty,
\qquad
\|W_n\|_\infty
=\ell_n^{-2}M_0,
\]

qui tendent vers l’infini. Le champ `U` n’est pas continu à l’origine et `W` n’y est pas borné.

## 6. Faible-`L^{3/2}` uniforme de la somme

Pour `λ>0`, notons

\[
\mu_W(\lambda)
=|\{x:|W(x)|>\lambda\}|.
\]

La disjonction des supports et `|supp W₀|≤8` donnent

\[
\mu_W(\lambda)
\leq
8\sum_{n:\,\lambda\ell_n^2<M_0}
\ell_n^3.
\tag{37}
\]

La suite `ℓ_n` est strictement décroissante. Soit `N(λ)` le premier indice de la somme. Pour `k≥0`,

\[
\frac{\ell_{N+k}}{\ell_N}
=2^{-k}\frac{N}{N+k}
\leq2^{-k}.
\tag{38}
\]

Ainsi

\[
\sum_{n\geq N}\ell_n^3
\leq\ell_N^3\sum_{k\geq0}2^{-3k}
=\frac87\ell_N^3.
\tag{39}
\]

Comme `λℓ_N²<M₀`,

\[
\lambda^{3/2}\mu_W(\lambda)
\leq\frac{64}{7}M_0^{3/2}.
\tag{40}
\]

Avec la convention

\[
\|F\|_{L^{3/2,\infty}}
=\sup_{\lambda>0}
\lambda|\{|F|>\lambda\}|^{2/3},
\]

(40) donne (9). Le même raisonnement, avec une somme tronquée, donne la même constante uniformément pour toutes les sommes partielles.

Par contraste,

\[
\int|W|^{3/2}dx
=\sum_{n\geq1}K_0
=+\infty.
\tag{41}
\]

La géométrie de séparation est donc suffisante pour faible-`L^{3/2}`, mais pas pour l’espace fort critique.

## 7. Biot–Savart et absence de mode harmonique

L’identité (27) et la décroissance géométrique donnent

\[
\sum_{n\geq1}
\|W_n\|_{6/5}^{6/5}
=\|W_0\|_{6/5}^{6/5}
\sum_{n\geq1}\ell_n^{3/5}
<\infty.
\tag{42}
\]

Ainsi `W∈L^{6/5}`. L’opérateur de Biot–Savart

\[
\mathcal B[W]
=\nabla\times(-\Delta)^{-1}W
\]

appartient à `L²` par Hardy–Littlewood–Sobolev et vérifie

\[
\operatorname{div}\mathcal B[W]=0,
\qquad
\nabla\times\mathcal B[W]=W.
\]

La différence

\[
H=U-\mathcal B[W]
\]

est dans `L²` et vérifie `curl H=div H=0`. En Fourier, son support est contenu dans `{0}`; un champ `L²` de cette nature est nul. Par conséquent,

\[
U=\mathcal B[W]
\quad\text{dans }L^2.
\tag{43}
\]

Il n’existe pas de mode harmonique `L²` caché. Cette égalité ne signifie pas que la somme locale (5) puisse être reconstruite blob par blob sans interactions dans une représentation ponctuelle : Biot–Savart est non local, et les annulations globales sont encodées par (43).

## 8. Masse critique par blob et coordonnées log-angulaires

Pour tout champ spatial, définissons formellement

\[
\Omega(s,\theta)=r^2W(r\theta),
\qquad
r=R_*e^{-s},
\qquad
\Phi=|\Omega|.
\tag{44}
\]

Le jacobien est

\[
dx=r^2dr\,dS=r^3ds\,dS
\]

en valeur absolue. Comme `|W|=r^{-2}Φ`,

\[
|W|^{3/2}dx
=\Phi^{3/2}ds\,dS.
\tag{45}
\]

Si `D_n` est l’image du support du blob `n` dans les coordonnées `(s,θ)`, alors

\[
\int_{D_n}\Phi^{3/2}ds\,dS
=K_0.
\tag{46}
\]

Avec la moyenne angulaire normalisée, la masse correspondante vaut `K₀/(4π)` par blob.

Cette égalité est une masse **sur le domaine courbe `D_n`**, pas automatiquement sur un bloc rectangulaire prédéfini `[s_n,s_n+1]×S²`. Le support cubique peut traverser une frontière de bloc logarithmique. On peut choisir des blocs adaptés à chaque blob, mais on ne peut pas revendiquer sans vérification la même minoration dans toute partition fixée.

## 9. Amplitude angulaire d’ordre `n²`

Sur le support du blob `n`, écrivons `x=x_n+ℓ_n y` avec `y∈Q₀`. Les inégalités triangulaires donnent

\[
r_n-\sqrt3\ell_n
\leq|x|
\leq r_n+\sqrt3\ell_n.
\tag{47}
\]

Par conséquent,

\[
\Phi(x)
=|x|^2\ell_n^{-2}|W_0(y)|
\leq
M_0\left(\frac{n}{c}+\sqrt3\right)^2.
\tag{48}
\]

Au centre `x=x_n`, (17) donne l’égalité

\[
\Phi(x_n)
=16\frac{r_n^2}{\ell_n^2}
=16\left(\frac nc\right)^2
=256n^2.
\tag{49}
\]

La taille angulaire du support est simultanément

\[
\frac{\ell_n}{r_n}
=\frac{1}{4n}.
\tag{50}
\]

Le volume angulaire-logarithmique se concentre donc tandis que l’amplitude croît. C’est précisément la raison pour laquelle une masse critique par blob et une norme faible globale n’impliquent aucune borne uniforme `Φ≤M`.

## 10. Minoration BMO à une face régulière

Définissons le prolongement par zéro de la direction de base :

\[
\zeta_0(y)=
\begin{cases}
W_0(y)/|W_0(y)|,&W_0(y)\neq0,\\
0,&W_0(y)=0.
\end{cases}
\tag{51}
\]

Considérons la face `x=1` du cube, le point

\[
p=(1,0,0),
\qquad
\rho=\frac1{16},
\qquad
\mathcal Q=B_\rho(p).
\tag{52}
\]

Deux sous-boules de `Q` sont

\[
\mathcal Q_{\mathrm{in}}
=B_{\rho/4}(p-(\rho/2)e_1),
\qquad
\mathcal Q_{\mathrm{out}}
=B_{\rho/4}(p+(\rho/2)e_1).
\tag{53}
\]

Elles ont chacune la fraction volumique

\[
\frac{|\mathcal Q_{\mathrm{in}}|}{|\mathcal Q|}
=\frac{|\mathcal Q_{\mathrm{out}}|}{|\mathcal Q|}
=\frac1{64}.
\tag{54}
\]

La boule extérieure est entièrement hors de `{x≤1}`; `ζ₀=0` sur `Q_out`. Dans la boule intérieure,

\[
\frac{61}{64}\leq x\leq\frac{63}{64},
\qquad
|y|,|z|\leq\frac1{64}.
\tag{55}
\]

Sur ce pavé, `-(W₀)₃>0`. Les formules (15)–(16) donnent les bornes rationnelles sûres

\[
\frac{f(x)|f''(y)|}{f''(x)f(y)}
\leq\frac1{500},
\tag{56}
\]

\[
\frac{|(W_0)_1|}{-(W_0)_3}
\leq\frac1{400},
\qquad
\frac{|(W_0)_2|}{-(W_0)_3}
\leq\frac1{100000}.
\tag{57}
\]

Pour vérifier (56)–(57), on utilise

\[
\frac{|f'(t)|}{f(t)}
=\frac{8|t|}{1-t^2},
\qquad
\frac{|f'(x)|}{f''(x)}
=\frac{x(1-x^2)}{7x^2-1},
\tag{58}
\]

ainsi que `1-x²≤375/4096`, `7x²-1≥21951/4096` et `|y|,|z|≤1/64`. En particulier,

\[
\zeta_0\cdot(-e_3)
\geq
\left[
1+400^{-2}+100000^{-2}
\right]^{-1/2}
>\frac12
\quad\text{sur }\mathcal Q_{\mathrm{in}}.
\tag{59}
\]

La borne garantit aussi que `W₀` ne s’annule pas dans cette sous-boule; les zéros internes du blob ne contaminent pas le test.

### Oscillation moyenne

Posons

\[
g=\zeta_0\cdot(-e_3).
\]

Pour toute fonction scalaire,

\[
\fint_{\mathcal Q}|g-g_{\mathcal Q}|
\geq
\frac12
\fint_{\mathcal Q}\fint_{\mathcal Q}
|g(y)-g(y')|dy\,dy'.
\tag{60}
\]

Les deux croisements `Q_in×Q_out` et `Q_out×Q_in`, (54) et (59) donnent

\[
\fint_{\mathcal Q}|g-g_{\mathcal Q}|
\geq
\frac12\cdot2
\left(\frac1{64}\right)^2
\cdot\frac12
=\frac1{8192}.
\tag{61}
\]

La projection ne peut qu’abaisser la norme vectorielle, donc

\[
\operatorname{MO}_{\mathcal Q}(\zeta_0)
\geq\frac1{8192}.
\tag{62}
\]

Pour le blob `n`, la boule test est

\[
\mathcal Q_n
=x_n+\ell_n\mathcal Q,
\tag{63}
\]

de rayon `ρℓ_n`. La séparation des supports assure que sa partie extérieure ne rencontre aucun autre blob. La direction est invariante par le scaling positif de (4), et l’oscillation moyenne est invariante par translation et dilatation. Ainsi

\[
\operatorname{MO}_{\mathcal Q_n}(\zeta)
\geq\frac1{8192}
\quad\text{pour tout }n.
\tag{64}
\]

Si

\[
\phi(r)=\frac1{1+\log(R_*/r)},
\]

alors

\[
\frac{\operatorname{MO}_{\mathcal Q_n}(\zeta)}
{\phi(\rho\ell_n)}
\geq
\frac1{8192}
\left[
1+\log\frac{R_*}{\rho\ell_n}
\right]
\longrightarrow+\infty.
\tag{65}
\]

Le prolongement par zéro échoue donc dans `bmo_φ`.

## 11. Cube support, coquilles et boules centrées

Le support d’un blob est cubique, pas sphérique. D’après (47), il est contenu dans une coquille relative d’épaisseur `O(1/n)` autour de `r_n`, mais il ne remplit pas cette coquille.

Dans une boule centrée de rayon comparable à `r_n`, sa fraction volumique est de l’ordre

\[
\left(\frac{\ell_n}{r_n}\right)^3
=\frac1{64n^3}.
\tag{66}
\]

Par conséquent, la minoration d’ordre un (64) repose sur des boules **décentrées**, adaptées à une face. Elle ne fournit aucune minoration d’ordre un sur les boules centrées à l’origine utilisées au cycle 0024. Confondre ces deux familles de boules invaliderait le raccord.

De même, la masse critique (46) est concentrée dans un domaine angulaire de taille décroissante. Elle ne donne pas la fraction active uniforme obtenue au cycle 0024 sous `Φ≤M`.

## 12. Passe contradictoire

### Attaque A — chevauchements

Sans facteur fixe, `ℓ_1=r_1` ferait toucher l’origine et chevaucherait les premiers supports. Le choix `c=1/4` donne le gap explicite (30). La disjonction est utilisée dans l’énergie, la fonction de distribution et la direction par zéro.

**Verdict :** correction nécessaire et fermée.

### Attaque B — zéros internes de `W₀`

La direction n’est pas définie sur les zéros de la vorticité. Le prolongement (51) les fixe à zéro. Le test BMO ne suppose pas que `W₀` soit non nul partout : la sous-boule intérieure est choisie dans une région où (56)–(59) certifient `-(W₀)₃>0`.

**Verdict :** les zéros internes ne détruisent pas la minoration locale, mais ils empêchent toute affirmation globale de continuité de la direction.

### Attaque C — autre extension sur les zéros

La borne (64) utilise `ζ=0` hors des blobs. Une extension qui prolonge la direction limite `-e₃` de l’autre côté de la face peut supprimer ce saut local.

**Verdict :** le rapport réfute le prolongement par zéro, pas l’existence de toute extension `bmo_φ`. Une obstruction universelle demanderait deux cœurs directionnels incompatibles ou une condition topologique supplémentaire.

### Attaque D — support cube versus bloc logarithmique

Le jacobien critique donne la masse exacte (46), mais le domaine `D_n` n’est pas un bloc produit. Une frontière de partition peut partager la masse d’un blob.

**Verdict :** « masse par blob » est prouvée; « même masse dans chaque bloc fixé » ne l’est pas sans choix et vérification supplémentaires.

### Attaque E — faible-`L^{3/2}` versus facteur angulaire borné

La norme faible est uniformément bornée par (9), tandis que `Φ(x_n)=256n²`.

**Verdict :** faible-`L^{3/2}` ne produit pas la borne `Φ≤M`; ce train est un contre-exemple explicite à ce raccord fonctionnel.

### Attaque F — Biot–Savart non local

La formule locale (5) pourrait sembler incompatible avec la non-localité de Biot–Savart. L’unicité `L²` (43) ferme ce point : les interactions non locales se compensent exactement dans la représentation globale. Ajouter un champ harmonique non nul détruirait `L²`.

**Verdict :** aucun mode harmonique `L²`; ne pas conclure pour autant à une localisation du noyau de Biot–Savart.

### Attaque G — point d’accumulation

Les amplitudes divergent près de l’origine. Cependant les convergences `U^(N)→U` dans `L²` et `W^(N)→W` dans `L¹` empêchent un défaut distributionnel ponctuel.

**Verdict :** admissibilité cinématique faible, mais absence de régularité classique à l’origine.

### Attaque H — donnée ou solution de Navier–Stokes

Le champ `U` est divergence-free et d’énergie finie, mais il n’est ni lisse, ni dans `H¹`. Aucun temps, aucune pression et aucun résidu de Navier–Stokes ne sont fournis.

**Verdict :** ce train n’est ni une solution, ni un profil de blow-up admissible du problème Clay. Il peut servir de donnée `L²` pour la théorie faible, pas de contre-exemple à la régularité classique des données lisses.

## 13. Ce qui est prouvé et ce qui ne l’est pas

### Prouvé dans ce rapport

- construction explicite de `U₀,W₀` et régularité jusqu’aux faces;
- identités distributionnelles `div U=0`, `curl U=W`, `div W=0`;
- supports disjoints avec `c=1/4` et gap minimal `3r_n/16`;
- énergie exacte finie `E₀log(2)/4`;
- appartenance de la somme et des sommes partielles à faible-`L^{3/2}` avec la constante (9);
- masse forte critique `K₀` identique par blob;
- masse log-angulaire exacte par le jacobien (45);
- amplitude angulaire exacte `256n²` aux centres;
- égalité avec la reconstruction de Biot–Savart dans `L²`;
- minoration `1/8192` de l’oscillation de la direction prolongée par zéro sur des boules de face;
- absence de défaut distributionnel au point d’accumulation.

### Non prouvé

- appartenance de la direction à `bmo_φ` pour une extension optimisée;
- masse `κ` dans chaque bloc d’une partition arbitraire;
- borne uniforme du facteur angulaire;
- régularité ou enstrophie finie à l’origine;
- satisfaction de l’équation de Navier–Stokes, de sa pression ou de son inégalité d’énergie locale;
- apparition de ce train comme limite d’une solution lisse;
- blow-up, non-unicité ou réfutation du problème Clay.

## 14. Lemme transférable

> Il existe un champ divergence-free `U∈L²(R³)` dont la vorticité `W=curl U` appartient à `L¹∩L^{6/5}∩L^{3/2,∞}`, est somme de blobs compacts disjoints portant chacun une masse `L^{3/2}` critique constante, mais dont le facteur log-angulaire `r²|W|` croît comme `n²`. Le prolongement par zéro de sa direction possède des oscillations moyennes uniformément minorées sur une suite de boules décentrées de rayons tendant vers zéro.

Ce lemme élimine deux raccourcis : faible-`L^{3/2}` n’implique pas `Φ≤M`, et une masse critique par blob n’implique pas une cohérence directionnelle pondérée. Il ne contourne aucune hypothèse du problème Clay.

## 15. Statut de preuve

Toutes les affirmations nouvelles de ce rapport sont des dérivations IA internes. Elles n’ont reçu ni revue par les pairs, ni formalisation, ni validation inter-familles. Aucune ne doit être étiquetée `PAPER_PROOF`.
