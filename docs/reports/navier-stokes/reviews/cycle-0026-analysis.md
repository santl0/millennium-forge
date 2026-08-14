# Audit analytique indépendant — cycle 0026 : compensation directionnelle sous faible-`L^{3/2}`

Date : 2026-08-14

Statut : **dérivation IA interne**, non publiée, jamais `PAPER_PROOF`; aucun énoncé dynamique de Navier–Stokes n’est revendiqué

## Verdict exécutif

Soit `D⊂R³` mesurable avec

\[
0<V:=|D|<\infty,
\]

et soit

\[
W\in L^{3/2,\infty}(D;\mathbb R^3),
\qquad
K=\sup_{\lambda>0}
\lambda|\{|W|>\lambda\}|^{2/3}<\infty.
\tag{1}
\]

Supposons

\[
\int_DW(x)\,dx=0.
\tag{2}
\]

Pour `e∈S²`, `α∈(0,1]`, posons

\[
\xi=\frac{W}{|W|}
\quad\text{sur }\{W\neq0\},
\]

\[
G=\{W\neq0:\xi\cdot e\geq\alpha\},
\qquad
m=\int_G|W|dx.
\tag{3}
\]

Pour toute extension

\[
\zeta\in L^1(D;\mathbb R^3),
\qquad
\zeta=\xi
\quad\text{p.p. sur }\{W\neq0\},
\tag{4}
\]

on a non seulement la borne proposée

\[
\boxed{
\operatorname{MO}_D(\zeta)
\geq
\frac{\alpha^4m^3}
{27K^3V}},
\tag{5}
\]

mais la borne strictement plus forte

\[
\boxed{
\operatorname{MO}_D(\zeta)
\geq
\frac{2\alpha^3m^3}
{27K^3V}}.
\tag{6}
\]

Ici

\[
\operatorname{MO}_D(\zeta)
=\frac1V\int_D|\zeta-\zeta_D|dx,
\qquad
\zeta_D=\frac1V\int_D\zeta dx.
\tag{7}
\]

La preuve de (5) par deux ensembles utilise exactement

\[
\int_E|W|dx
\leq3K|E|^{1/3}.
\tag{8}
\]

La preuve améliorée conserve le poids de projection négative

\[
q=(-\xi\cdot e)_+
\]

et utilise la variante

\[
\int_D|W|q\,dx
\leq3K
\left(\int_Dq\,dx\right)^{1/3}.
\tag{9}
\]

La puissance `m³/K³` est imposée par le scaling et ne peut pas être remplacée par une puissance plus petite. La famille à deux niveaux demandée réalise

\[
K=1,
\qquad
m=\frac1n,
\qquad
\operatorname{MO}_D(\xi)
=4n^{-3}(1-n^{-3}),
\tag{10}
\]

et certifie cette optimalité d’exposant. Elle ne sature pas la constante `2/27`; l’optimalité numérique globale de cette constante reste ouverte sous les seules hypothèses abstraites.

La condition (2) est automatique pour `W=curl U` lorsque `U` est compactement supporté à l’intérieur de `D`, mais pas sur un sous-domaine arbitraire : un terme de circulation de bord apparaît. Le prochain verrou est précisément de spatialiser la compensation globale sous les contraintes `div W=0` et `W=curl U`.

## 1. Préliminaire : faible-`L^{3/2}` implique `L¹` sur un domaine fini

La définition (1) donne, pour tout `λ>0`,

\[
|\{|W|>\lambda\}|
\leq
\left(\frac K\lambda\right)^{3/2}.
\tag{11}
\]

Pour un ensemble mesurable `E⊂D`, posons

\[
\lambda_E=K|E|^{-2/3}.
\]

La formule de Cavalieri et la séparation à `λ_E` donnent

\[
\begin{aligned}
\int_E|W|dx
&=\int_0^\infty
|E\cap\{|W|>\lambda\}|d\lambda\\
&\leq
\lambda_E|E|
+\int_{\lambda_E}^{\infty}
\left(\frac K\lambda\right)^{3/2}d\lambda\\
&=K|E|^{1/3}
+2K|E|^{1/3}\\
&=3K|E|^{1/3}.
\end{aligned}
\tag{12}
\]

C’est (8). En prenant `E=D`,

\[
\|W\|_{L^1(D)}
\leq3KV^{1/3}.
\tag{13}
\]

L’intégrale vectorielle de (2) est donc bien définie. La constante `3=p/(p-1)` pour `p=3/2` est la constante optimale de cette estimation de réarrangement.

## 2. Compensation négative imposée par la moyenne nulle

Projetons (2) sur `e`. Sur `G`,

\[
W\cdot e
=|W|\xi\cdot e
\geq\alpha|W|.
\]

Par conséquent,

\[
\int_GW\cdot e\,dx
\geq\alpha m.
\tag{14}
\]

Définissons l’ensemble négatif et son poids de projection

\[
H=\{W\neq0:\xi\cdot e<0\},
\qquad
q=(-\xi\cdot e)_+.
\tag{15}
\]

La partie positive totale de `W·e` peut être plus grande que sa partie sur `G`; la moyenne nulle donne donc

\[
\int_H|W|q\,dx
=\int_D(W\cdot e)_+dx
\geq\alpha m.
\tag{16}
\]

En oubliant le poids `q≤1`,

\[
\int_H|W|dx\geq\alpha m.
\tag{17}
\]

L’estimation (8) appliquée à `G` et `H` donne

\[
|G|
\geq
\left(\frac m{3K}\right)^3,
\qquad
|H|
\geq
\left(\frac{\alpha m}{3K}\right)^3.
\tag{18}
\]

Ces bornes n’utilisent pas `div W=0`; seule la compensation vectorielle globale (2) intervient.

## 3. Première preuve : deux ensembles séparés

Posons

\[
g=\zeta\cdot e,
\qquad
c=g_D=\frac1V\int_Dg dx.
\]

Sur `G`, `g≥α`; sur `H`, `g<0`. Notons

\[
a=\frac{|G|}{V},
\qquad
b=\frac{|H|}{V}.
\]

### Lemme 3.1 — deux traces séparées

Pour toute fonction intégrable `g` vérifiant `g≥α` sur un ensemble de fraction `a` et `g≤0` sur un ensemble disjoint de fraction `b`,

\[
\fint_D|g-g_D|dx
\geq
\frac{2\alpha ab}{a+b}.
\tag{19}
\]

### Preuve

Posons `h=g-c`. Comme `∫h=0`,

\[
\int_Dh_+dx
=\int_Dh_-dx
=\frac12\int_D|h|dx.
\tag{20}
\]

- Si `c≤0`, la contribution positive de `G` est au moins `aαV`.
- Si `c≥α`, la contribution négative de `H` est au moins `bαV`.
- Si `0<c<α`, les contributions sont au moins
  \[
  a(\alpha-c)V
  \quad\text{et}\quad
  bcV.
  \]
  Leur maximum est minimal lorsque
  \[
  a(\alpha-c)=bc,
  \qquad
  c=\frac{a\alpha}{a+b},
  \]
  et vaut `αabV/(a+b)`.

Dans les trois cas, (20) donne (19). La constante est atteinte pour deux valeurs de bord `α` et `0`, le complément étant choisi égal à `aα/(a+b)`.

La projection est contractante :

\[
|g-c|
\leq|\zeta-\zeta_D|.
\tag{21}
\]

Insérons les minorations (18). La fonction `2ab/(a+b)` est croissante en chaque variable, d’où

\[
\begin{aligned}
\operatorname{MO}_D(\zeta)
&\geq
\frac{2\alpha^4}{1+\alpha^3}
\frac{m^3}{27K^3V}\\
&\geq
\frac{\alpha^4m^3}{27K^3V},
\end{aligned}
\tag{22}
\]

car `2/(1+α³)≥1`. Cela prouve exactement le lemme demandé.

## 4. Inégalité de Lorentz pondérée

La perte d’une puissance de `α` dans (22) vient de l’oubli du poids `q`. On peut le conserver.

### Lemme 4.1 — poids compris entre zéro et un

Si `0≤q≤1`, alors

\[
\int_D|W|q\,dx
\leq
3K\left(\int_Dq\,dx\right)^{1/3}.
\tag{23}
\]

### Preuve

La représentation en couches

\[
q(x)=\int_0^1
\mathbf1_{\{q(x)>t\}}dt
\]

et (8) donnent

\[
\begin{aligned}
\int_D|W|qdx
&=\int_0^1
\int_{\{q>t\}}|W|dx\,dt\\
&\leq3K\int_0^1
|\{q>t\}|^{1/3}dt.
\end{aligned}
\]

La concavité de `x↦x^{1/3}` et Cavalieri donnent

\[
\int_0^1|\{q>t\}|^{1/3}dt
\leq
\left(
\int_0^1|\{q>t\}|dt
\right)^{1/3}
=\left(\int_Dqdx\right)^{1/3}.
\]

C’est (23).

En combinant (16) et (23),

\[
Q:=\frac1V\int_Dqdx
\geq
\frac{\alpha^3m^3}{27K^3V}.
\tag{24}
\]

## 5. Borne améliorée

Conservons

\[
a=\frac{|G|}{V}
\geq
\frac{m^3}{27K^3V}
\tag{25}
\]

et `Q` de (24). Soit encore `c=g_D`.

- Si `c≥0`, alors sur `H`
  \[
  (g-c)_-=q+c\geq q.
  \]
  La partie négative moyenne de `g-c` est au moins `Q`.
- Si `c<0`, alors sur `G`
  \[
  (g-c)_+\geq\alpha-c>\alpha.
  \]
  La partie positive moyenne est au moins `αa`.

Comme les parties positive et négative d’une fonction de moyenne nulle ont la même intégrale,

\[
\fint_D|g-c|dx
\geq
2\min\{Q,\alpha a\}.
\tag{26}
\]

Pour `0<α≤1`, (24)–(25) donnent

\[
Q\geq
\frac{\alpha^3m^3}{27K^3V},
\qquad
\alpha a\geq
\frac{\alpha m^3}{27K^3V}
\geq
\frac{\alpha^3m^3}{27K^3V}.
\]

La projection (21) conclut :

\[
\operatorname{MO}_D(\zeta)
\geq
\frac{2\alpha^3m^3}{27K^3V}.
\tag{27}
\]

C’est (6). Par rapport à (5), on gagne au moins un facteur `2/α`.

## 6. Formulation sans moyenne nulle

Le rôle de (2) peut être isolé. Posons

\[
\nu_e
=\int_D(-W\cdot e)_+dx
=\int_D|W|qdx.
\tag{28}
\]

Sans supposer `∫W=0`, la même preuve donne

\[
\boxed{
\operatorname{MO}_D(\zeta)
\geq
\frac{2}{27K^3V}
\min\{\alpha m^3,\nu_e^3\}}.
\tag{29}
\]

Sous (2),

\[
\nu_e
=\int_D(W\cdot e)_+dx
\geq\alpha m,
\]

et (29) devient (27). Cette version est canonique lorsqu’un calcul fournit directement la compensation négative mais pas une moyenne vectorielle exactement nulle.

## 7. Quantificateurs et cas limites

### 7.1 Mesure du domaine

Il faut supposer `0<|D|<∞`. Pour `|D|=0`, la moyenne est indéfinie; pour `|D|=∞`, faible-`L^{3/2}` ne donne pas automatiquement `L¹` et le budget de moyenne doit être reformulé.

### 7.2 Cas `K=0`

Si `K=0`, alors `W=0` presque partout : pour tout `λ>0`, l’ensemble `{|W|>λ}` a mesure nulle. Ainsi `m=0`.

Les quotients `m³/K³` sont néanmoins de forme `0/0`; le théorème doit être énoncé pour `K>0`. Le cas `K=0` est séparément trivial avec le membre de droite défini comme zéro.

### 7.3 Cas `m=0`

Si `m=0`, les bornes sont vraies mais vides. Aucun ensemble actif de mesure positive n’est forcé.

### 7.4 Frontières de `G` et `H`

Le choix `ξ·e≥α` dans `G` est compatible avec `α=1`. Le choix strict `ξ·e<0` dans `H` ne perd aucune compensation : les points où `ξ·e=0` ne contribuent pas à la projection négative. Modifier ces ensembles sur des ensembles nuls ne change rien.

### 7.5 Valeurs de l’extension sur `{W=0}`

La preuve n’impose ni `|ζ|≤1`, ni une extension par zéro. Elle autorise toute extension **intégrable**, même non bornée, parce que seul le scalaire `g=ζ·e` et sa moyenne sont utilisés.

Si `ζ` n’appartient pas à `L¹(D)`, `ζ_D` et `MO_D(ζ)` ne sont pas définis. L’énoncé « pour toute extension mesurable » est donc mal posé sans condition d’intégrabilité ou convention de valeur infinie.

## 8. Invariance d’échelle

Considérons une translation, une rotation spatiale et la transformation

\[
W_{A,L}(x)
=A\,R\,W\left(\frac{R^{T}(x-x_0)}{L}\right),
\qquad
D_{L,R}=x_0+LRD,
\tag{30}
\]

avec `A,L>0` et `R` orthogonale. Alors

\[
|D_{L,R}|=L^3V,
\qquad
K_{A,L}=AL^2K,
\qquad
m_{A,L}=AL^3m.
\tag{31}
\]

Par conséquent,

\[
\frac{m_{A,L}^3}
{K_{A,L}^3|D_L|}
=\frac{m^3}{K^3V}.
\tag{32}
\]

La direction et son oscillation moyenne sont invariantes après rotation simultanée de `e`. La borne est donc invariante sous toute remise à l’échelle amplitude–espace, notamment sous le scaling de vorticité de Navier–Stokes.

Cette invariance force le quotient cubique. Elle n’établit pas à elle seule que l’exposant `3` est optimal; la famille suivante le fait.

## 9. Famille à deux niveaux

Prenons `|D|=1`, `n≥2`,

\[
\varepsilon=n^{-3},
\qquad
a_n=\frac{n^2}{n^3-1},
\tag{33}
\]

et partageons `D` en deux ensembles de mesures `1-ε` et `ε`. Définissons

\[
W=
\begin{cases}
a_ne,&\text{sur la partie de mesure }1-\varepsilon,\\
-n^2e,&\text{sur la partie de mesure }\varepsilon.
\end{cases}
\tag{34}
\]

### Moyenne nulle

On a

\[
a_n(1-\varepsilon)
=\frac1n
=n^2\varepsilon,
\]

donc

\[
\int_DWdx=0.
\tag{35}
\]

### Norme faible exacte

La fonction de distribution de `|W|` est

\[
\mu(\lambda)=
\begin{cases}
1,&0<\lambda<a_n,\\
\varepsilon,&a_n\leq\lambda<n^2,\\
0,&\lambda\geq n^2,
\end{cases}
\]

aux conventions de seuil près. Ainsi

\[
K=\max\{a_n,n^2\varepsilon^{2/3}\}
=\max\{a_n,1\}=1.
\tag{36}
\]

### Masse du cône et oscillation exacte

Pour tout `α∈(0,1]`, `G` est la partie positive et

\[
m=a_n(1-\varepsilon)=\frac1n.
\tag{37}
\]

Il n’y a pas de zéros; l’extension est imposée :

\[
\zeta=\xi=
\begin{cases}
e,&1-\varepsilon,\\
-e,&\varepsilon.
\end{cases}
\]

Sa moyenne est `(1-2ε)e`, et

\[
\begin{aligned}
\operatorname{MO}_D(\xi)
&=(1-\varepsilon)2\varepsilon
+\varepsilon2(1-\varepsilon)\\
&=4\varepsilon(1-\varepsilon)\\
&=\frac4{n^3}
\left(1-\frac1{n^3}\right).
\end{aligned}
\tag{38}
\]

### Ce que cette famille rend sharp

Pour `α=1`, `K=V=1` et `m=1/n`. Toute borne universelle dont le membre principal serait `m^p` avec `p<3` dépasserait (38) pour `n` assez grand. L’exposant cubique est donc optimal.

La famille donne aussi la contrainte suivante sur une borne hypothétique

\[
\operatorname{MO}\geq C\frac{m^3}{K^3V}:
\]

nécessairement `C≤4`. Notre constante améliorée vaut `2/27`, très loin de cette barrière. La famille ne prouve donc pas l’optimalité de la constante.

Pour `α<1`, l’oscillation exacte ne dépend pas de `α`; cette famille ne décide pas à elle seule l’optimalité de la puissance `α³`. La méthode pondérée montre néanmoins rigoureusement que `α⁴` n’est pas le meilleur exposant fourni par les hypothèses.

## 10. Constantes et possibilité d’amélioration

### 10.1 Borne demandée

La constante `1/27` vient de `3³` dans (8). Elle est valide.

### 10.2 Amélioration démontrée

La meilleure borne obtenue ici est

\[
\frac{2\alpha^3}{27}
\frac{m^3}{K^3V}.
\]

Elle améliore à la fois la puissance de `α` et la constante uniforme devant `α⁴`.

### 10.3 Optimalité non démontrée

La constante `3` de l’inégalité de Lorentz et le facteur `2` issu de l’équilibre des parties positive et négative sont séparément sharp. Cela ne prouve pas que toutes les égalités intermédiaires puissent être approchées simultanément sous `∫W=0` et avec une direction prescrite.

Une famille quasi extrémale devrait combiner :

- une queue de distribution proche de `K t^{-2/3}` sur le compensateur négatif;
- une masse positive `m` dans le cône;
- une extension sur le complément qui place sa moyenne au seuil critique;
- si l’on vise une vorticité réelle, `div W=0` et une reconstruction par curl.

Ce problème d’optimalité est distinct de la validité de (5)–(6).

## 11. Raccord avec `W=curl U` compact

Soit `U∈C_c^1(R³;R³)` et `W=curl U`. Chaque composante de `W` est une dérivée d’une fonction compacte; par intégration,

\[
\int_{\mathbb R^3}Wdx=0.
\tag{39}
\]

Plus généralement, si `D` est un domaine lipschitzien contenant le support de `U` dans son intérieur,

\[
\int_DWdx=0.
\]

Si `U` ne s’annule pas au bord, la formule exacte est

\[
\int_D\nabla\times U\,dx
=\int_{\partial D}n\times U\,dS.
\tag{40}
\]

La moyenne nulle sur un sous-domaine n’est donc pas automatique.

En outre,

\[
\operatorname{div}W
=\operatorname{div}(\nabla\times U)=0
\tag{41}
\]

est une contrainte supplémentaire que le lemme abstrait n’utilise pas. La famille à deux niveaux (34), définie seulement par valeurs et mesures, n’est pas automatiquement divergence-free : les sauts créent des charges de surface sauf si la géométrie des interfaces est spécialement organisée.

Ainsi :

- `W=curl U` compact implique la moyenne nulle globale;
- la moyenne nulle seule n’implique ni `div W=0`, ni l’existence d’un potentiel compact;
- le lemme s’applique à toute vorticité compacte admissible, mais sa famille sharp abstraite n’est pas encore une vorticité admissible.

## 12. Passe contradictoire

### Attaque A — extension non intégrable

Sur `{W=0}`, une extension mesurable peut être non bornée et non intégrable. Sa moyenne n’existe alors pas.

**Verdict :** remplacer « toute extension mesurable » par « toute extension `L¹` », ou imposer `|ζ|≤1`.

### Attaque B — oubli du cas `K=0`

La formule quotient n’est pas définie lorsque `K=0`, même si `W=0`.

**Verdict :** séparer explicitement le cas trivial.

### Attaque C — compensation sur la frontière `ξ·e=0`

Les points de projection nulle ne portent aucune compensation négative pondérée et ne peuvent satisfaire (16).

**Verdict :** aucun terme de frontière directionnelle ne manque.

### Attaque D — constante issue de la seule mesure de `H`

Oublier `q` produit la puissance `α⁴`. Garder `q` donne (27).

**Verdict :** le lemme proposé est vrai mais non optimal sous ses propres hypothèses.

### Attaque E — confusion moyenne globale/moyenne locale

Pour un curl compact, (39) vaut sur un domaine contenant tout le support. Elle ne vaut pas nécessairement sur une boule locale rencontrant seulement le cône positif.

**Verdict :** la borne globale de `MO_D` ne devient pas automatiquement une borne BMO à toutes les petites échelles.

### Attaque F — famille sharp non solénoïdale

La famille (34) fixe seulement la distribution des valeurs. Sans géométrie d’interfaces, `div W` contient des mesures de saut.

**Verdict :** elle certifie l’exposant fonctionnel, pas le verrou spatial div–curl.

### Attaque G — pression et Navier–Stokes

Ni le lemme ni la famille ne vérifient l’équation de vorticité, Biot–Savart local, la pression ou l’inégalité d’énergie.

**Verdict :** résultat cinématique/fonctionnel uniquement.

## 13. Formulation canonique recommandée

> **Lemme de compensation directionnelle faible critique.** Soient `0<|D|<∞`, `W∈L^{3/2,∞}(D;R³)` de quasi-norme de distribution `K>0`, `e∈S²` et `α∈(0,1]`. Posons `G={W≠0:ξ·e≥α}`, `m=∫_G|W|` et `ν_e=∫_D(-W·e)_+`. Pour toute extension `ζ∈L¹(D;R³)` de `ξ`,
> \[
> \operatorname{MO}_D(\zeta)
> \geq
> \frac{2}{27K^3|D|}
> \min\{\alpha m^3,\nu_e^3\}.
> \]
> Si `∫_DW=0`, alors `ν_e≥αm` et
> \[
> \operatorname{MO}_D(\zeta)
> \geq
> \frac{2\alpha^3m^3}{27K^3|D|}.
> \]

Cette version :

- sépare le cas `K=0`;
- rend l’intégrabilité de l’extension explicite;
- montre exactement où intervient la moyenne nulle;
- conserve l’invariance d’échelle;
- améliore la borne demandée;
- se localise dès qu’une compensation négative `ν_e` est disponible, même sans moyenne exactement nulle.

## 14. Prochain verrou spatial/div–curl

Le lemme ne localise pas la compensation. La masse négative peut être placée arbitrairement loin du cône positif dans `D`, et une unique moyenne globale suffit encore.

Le prochain problème falsifiable est :

> Pour une vorticité compacte `W=curl U`, `div W=0`, peut-on soit construire une famille approchant le scaling sharp `m³/K³` tout en respectant les interfaces solénoïdales, soit démontrer qu’une fraction quantitative de la compensation `ν_e` doit apparaître dans une boule comparable au support de `G` ?

Les termes à contrôler sont :

\[
\int_BWdx
=\int_{\partial B}n\times U\,dS,
\tag{42}
\]

la fuite de circulation au bord, la non-localité de Biot–Savart et les charges de divergence aux interfaces. Une réponse positive de localisation convertirait (29) en minoration BMO réellement spatiale; un contre-exemple solénoïdal compact proche de la famille (34) éliminerait cette stratégie.

## 15. Statut de preuve

Toutes les affirmations nouvelles de ce rapport sont des dérivations IA internes. Elles n’ont reçu ni revue par les pairs, ni formalisation, ni validation inter-familles. Aucune ne doit être étiquetée `PAPER_PROOF`.
