# Passe analytique contradictoire — cycle 0023 : moment mobile et coût de rotation de l’axe

Date : 2026-08-14

Statut : **dérivation IA interne**, non publiée, jamais `PAPER_PROOF`; passe séparée mais non indépendante inter-familles de modèles

## Verdict exécutif

Considérons

\[
W(r,\theta)=r^{-2}\Omega(s,\theta),
\qquad
s=\log\frac{R_*}{r},
\qquad
\Omega=\Phi\xi,
\qquad
0\leq\Phi=|\Omega|\leq M,
\tag{1}
\]

et supposons `div W=0` sur le domaine ponctué. Avec la moyenne sphérique normalisée

\[
\langle f\rangle
:=\frac1{4\pi}\int_{S^2}f(\theta)\,dS(\theta),
\tag{2}
\]

la contrainte exacte est

\[
\partial_s\Omega_r
=\operatorname{div}_{S^2}\Omega_T.
\tag{3}
\]

Soit maintenant un axe mobile `e(s)∈S²`, absolument continu, et posons

\[
q(s,\theta)=e(s)\cdot\theta,
\qquad
J(s)=\langle q\Omega_r\rangle.
\tag{4}
\]

Le moment mobile satisfait l’identité exacte

\[
\boxed{
J'(s)
=-D_e(s)+A_e(s)}
\tag{5}
\]

avec

\[
D_e(s)=
\left\langle
\Omega\cdot\nabla_{S^2}q
\right\rangle,
\qquad
A_e(s)=
\left\langle
(e'(s)\cdot\theta)\Omega_r
\right\rangle.
\tag{6}
\]

Définissons la masse critique transverse et l’erreur directionnelle pondérée

\[
\mathcal M_e(s)
=\left\langle
\Phi(1-q^2)
\right\rangle,
\qquad
\mathcal E_e(s)
=\left\langle
\Phi|\xi-e|\sqrt{1-q^2}
\right\rangle.
\tag{7}
\]

Alors

\[
D_e(s)\geq
\mathcal M_e(s)-\mathcal E_e(s),
\qquad
|A_e(s)|\leq\frac M2|e'(s)|,
\qquad
|J(s)|\leq\frac M2.
\tag{8}
\]

Par conséquent, sur tout intervalle `I=[a,b]`,

\[
\boxed{
\int_I
(\mathcal M_e-\mathcal E_e)\,ds
\leq
M+\frac M2\operatorname{Var}_I(e)}.
\tag{9}
\]

La même borne vaut pour un axe `BV`, en comptant ses sauts dans la variation totale. Elle donne la condition minimale d’impossibilité recherchée : aucun profil ne peut exister sur une demi-droite en `s` si

\[
\int_{s_0}^{S}
(\mathcal M_e-\mathcal E_e)\,ds
-\frac M2\operatorname{Var}_{[s_0,S]}(e)
\longrightarrow+\infty.
\tag{10}
\]

Le point nouveau pour une « masse critique par blocs » est que la masse scalaire suffit si elle ne peut pas disparaître en moyenne. Si

\[
P(s)=\langle\Phi(s,\cdot)\rangle,
\]

alors le principe de baignoire optimal donne

\[
\boxed{
\mathcal M_e(s)
\geq
f_M(P(s)),
\qquad
f_M(P)=\frac{P^2}{M}-\frac{P^3}{3M^2}}.
\tag{11}
\]

Pour des blocs contigus `I_k` de longueur `L_k`, de masse moyenne

\[
p_k=\frac1{L_k}\int_{I_k}P(s)\,ds,
\]

on obtient la condition nécessaire

\[
\sum_{k=1}^{N}L_kf_M(p_k)
\leq
M+\sum_{k=1}^{N}
\int_{I_k}\mathcal E_e\,ds
+\frac M2
\operatorname{Var}_{\cup_{k=1}^NI_k}(e).
\tag{12}
\]

Une somme d’excès dépassant `M` exclut le profil. Des axes choisis indépendamment bloc par bloc ne suffisent pas : leurs sauts doivent être inclus dans la variation totale, et les lacunes entre blocs peuvent recharger le moment.

## 1. Cadre exact et régularité

Les identités fortes sont d’abord établies sous

\[
\Omega\in W^{1,1}_{\mathrm{loc}}
((s_0,S)\times S^2;\mathbb R^3),
\qquad
e\in W^{1,1}((s_0,S);S^2).
\tag{13}
\]

On décompose

\[
\Omega_r=\Omega\cdot\theta,
\qquad
\Omega_T=\Omega-\Omega_r\theta.
\]

La direction `ξ` peut être définie arbitrairement sur `{Φ=0}` : toutes les quantités où elle intervient sont multipliées par `Φ`.

Avec la convention `s=log(R_*/r)`, le signe de (3) vient de

\[
\operatorname{div}W
=r^{-3}
\left(
\operatorname{div}_{S^2}\Omega_T
-\partial_s\Omega_r
\right).
\tag{14}
\]

Le rapport n’utilise ni l’équation d’évolution de la vorticité, ni Biot–Savart, ni l’inégalité d’énergie. Il fournit une obstruction cinématique nécessaire pour qu’un tel ansatz puisse être un curl.

## 2. Dérivation exacte du moment mobile

Pour

\[
q=e(s)\cdot\theta,
\]

on a

\[
\partial_sq=e'(s)\cdot\theta,
\qquad
\nabla_{S^2}q=e-q\theta,
\qquad
|\nabla_{S^2}q|^2=1-q^2.
\tag{15}
\]

En dérivant (4) et en utilisant (3),

\[
\begin{aligned}
J'(s)
&=\left\langle
(e'\cdot\theta)\Omega_r
\right\rangle
+\left\langle
q\,\partial_s\Omega_r
\right\rangle\\
&=A_e(s)
+\left\langle
q\,\operatorname{div}_{S^2}\Omega_T
\right\rangle\\
&=A_e(s)
-\left\langle
\nabla_{S^2}q\cdot\Omega_T
\right\rangle\\
&=A_e(s)-D_e(s).
\end{aligned}
\tag{16}
\]

La dernière égalité utilise le fait que `∇_Sq` est tangent, donc orthogonal à la partie radiale de `Ω`.

L’identité (16) isole les deux mécanismes :

- `D_e` dépense le moment lorsque la direction de `Ω` est alignée avec `e`;
- `A_e` recharge éventuellement le moment en faisant tourner l’axe test.

## 3. Constantes sphériques

Pour tout axe unitaire `e` et tout vecteur `a`,

\[
\langle|e\cdot\theta|\rangle=\frac12,
\qquad
\langle(e\cdot\theta)^2\rangle=\frac13,
\qquad
\langle1-(e\cdot\theta)^2\rangle=\frac23,
\tag{17}
\]

et

\[
\langle|a\cdot\theta|\rangle=\frac{|a|}{2}.
\tag{18}
\]

Comme `|Ω_r|≤Φ≤M`, ces identités donnent

\[
|J(s)|
\leq M\langle|q|\rangle
=\frac M2,
\tag{19}
\]

et

\[
|A_e(s)|
\leq M\langle|e'\cdot\theta|\rangle
=\frac M2|e'(s)|.
\tag{20}
\]

La constante `1/2` de (20) est optimale sans information directionnelle : on peut choisir `Ω_r` avec le signe de `e'·θ` et de module arbitrairement proche de `M`.

## 4. Masse transverse et erreur pondérée

Puisque `Ω=Φξ` et `e·∇_Sq=|∇_Sq|²`,

\[
\begin{aligned}
D_e
&=\left\langle
\Phi e\cdot\nabla_{S^2}q
\right\rangle
+\left\langle
\Phi(\xi-e)\cdot\nabla_{S^2}q
\right\rangle\\
&\geq
\left\langle
\Phi|\nabla_{S^2}q|^2
\right\rangle
-\left\langle
\Phi|\xi-e||\nabla_{S^2}q|
\right\rangle\\
&=\mathcal M_e-\mathcal E_e.
\end{aligned}
\tag{21}
\]

Le poids `sqrt(1-q²)` est nécessaire. Une erreur de direction concentrée près des pôles de l’axe coûte peu dans le moment, car `∇_Sq` s’y annule. Remplacer `E_e` par une norme non pondérée est possible mais moins précis :

\[
\mathcal E_e
\leq
\langle\Phi|\xi-e|\rangle
\leq M\|\xi-e\|_{L^1(S^2;dS/4\pi)}.
\tag{22}
\]

## 5. Budget en variation totale

Intégrons (16) sur `I=[a,b]` :

\[
\int_I D_e(s)\,ds
=J(a)-J(b)+\int_I A_e(s)\,ds.
\tag{23}
\]

Les bornes (19)–(21) donnent

\[
\int_I(\mathcal M_e-\mathcal E_e)ds
\leq
M+\frac M2\int_I|e'(s)|ds,
\tag{24}
\]

qui est (9) pour un axe absolument continu.

### Extension aux axes `BV`

Supposons `e∈BV(I;S²)` et que `Ω_r` admette les traces nécessaires. Au sens des mesures, la règle du produit ajoute à (16) le terme de Stieltjes

\[
dJ
=-D_e(s)ds
+\left\langle
(\theta\cdot de)\Omega_r
\right\rangle.
\tag{25}
\]

Pour toute direction vectorielle `v`,

\[
\left|
\left\langle
(v\cdot\theta)\Omega_r
\right\rangle
\right|
\leq\frac M2|v|.
\tag{26}
\]

Cela contrôle à la fois la partie absolument continue, la partie singulière continue et les sauts de `e`, et redonne exactement (9) avec `Var_I(e)`.

La forme la plus précise conserve le coût mobile effectif

\[
\mathcal V_\Omega(e;I)
:=\left|
\int_I
\left\langle
(\theta\cdot de)\Omega_r
\right\rangle
\right|
\leq\frac M2\operatorname{Var}_I(e).
\tag{27}
\]

Une condition d’impossibilité encore plus proche de l’identité exacte est donc

\[
\int_I(\mathcal M_e-\mathcal E_e)ds
>M+\mathcal V_\Omega(e;I).
\tag{28}
\]

La version en variation totale est plus robuste, car elle ne dépend pas du signe des recharges de moment.

## 6. Conversion optimale d’une masse scalaire en masse transverse

La quantité `M_e` peut être petite si `Φ` se concentre près des deux pôles `±e`, même lorsque `〈Φ〉` est positive. Sous la seule contrainte `0≤Φ≤M`, le pire cas se calcule exactement.

Posons

\[
P=\langle\Phi\rangle,
\qquad
\alpha=P/M\in[0,1].
\tag{29}
\]

Pour minimiser

\[
\langle\Phi(1-q^2)\rangle
\]

à masse `P` fixée, le principe de baignoire place `Φ=M` là où `1-q²` est le plus petit, c’est-à-dire sur les deux calottes

\[
|q|\geq1-\alpha.
\]

Comme `|q|` est uniforme sur `[0,1]` sous la mesure sphérique normalisée,

\[
\begin{aligned}
\mathcal M_e
&\geq
M\int_{1-\alpha}^{1}(1-z^2)dz\\
&=M\left(\alpha^2-\frac{\alpha^3}{3}\right)\\
&=\frac{P^2}{M}-\frac{P^3}{3M^2}
=f_M(P).
\end{aligned}
\tag{30}
\]

La constante est optimale parmi les fonctions mesurables `0≤Φ≤M`. On vérifie les extrêmes :

\[
f_M(0)=0,
\qquad
f_M(M)=\frac{2M}{3},
\tag{31}
\]

le second étant exactement la moyenne de `M(1-q²)` pour une amplitude uniforme.

En outre,

\[
f_M''(P)=\frac{2(M-P)}{M^2}\geq0.
\tag{32}
\]

La convexité permet une hypothèse de masse seulement **par bloc**. Si `I` a longueur `L` et

\[
p_I=\frac1L\int_I\langle\Phi\rangle ds,
\]

alors Jensen donne

\[
\int_I\mathcal M_e(s)ds
\geq Lf_M(p_I).
\tag{33}
\]

## 7. Critère par blocs contigus

Soient

\[
I_k=[s_{k-1},s_k],
\qquad
L_k=s_k-s_{k-1},
\qquad
k=1,\ldots,N,
\]

des blocs adjacents couvrant `[s_0,s_N]`. Définissons

\[
p_k=\frac1{L_k}
\int_{I_k}\langle\Phi\rangle ds,
\qquad
E_k=\int_{I_k}\mathcal E_e(s)ds.
\tag{34}
\]

Les inégalités (9) et (33) impliquent

\[
\sum_{k=1}^{N}
\left[L_kf_M(p_k)-E_k\right]
\leq
M+\frac M2
\operatorname{Var}_{[s_0,s_N]}(e).
\tag{35}
\]

### Corollaire 7.1 — excès cumulatif

Si

\[
\sum_{k=1}^{N}
\left[
L_kf_M(p_k)-E_k
\right]
-\frac M2
\operatorname{Var}_{[s_0,s_N]}(e)
>M
\tag{36}
\]

pour un certain `N`, les hypothèses sont incompatibles avec `div W=0`.

Si le membre de gauche tend vers `+∞` quand `N→∞`, aucun profil ne peut atteindre `r=0`.

### Corollaire 7.2 — taux uniformes

Supposons, sur une union contiguë de longueur totale `L`,

\[
p_k\geq p_0>0,
\qquad
\sum_kE_k\leq\varepsilon_0L,
\qquad
\operatorname{Var}(e)
\leq v_0L+V_0.
\tag{37}
\]

Si

\[
g:=f_M(p_0)-\varepsilon_0-\frac M2v_0>0,
\tag{38}
\]

alors

\[
L\leq
\frac{M+(M/2)V_0}{g}.
\tag{39}
\]

Le critère compare donc trois taux sur l’échelle logarithmique : masse transverse produite, erreur directionnelle et vitesse totale de rotation de l’axe.

## 8. Coût affiné du mouvement pour un axe absolument continu

La constante `M/2` est optimale sans utiliser `ξ≈e`, mais elle peut être améliorée lorsque l’erreur pondérée est petite. Comme `e'·e=0` presque partout,

\[
\begin{aligned}
A_e
&=\left\langle
\Phi(e'\cdot\theta)(e\cdot\theta)
\right\rangle\\
&\quad+
\left\langle
\Phi(e'\cdot\theta)((\xi-e)\cdot\theta)
\right\rangle.
\end{aligned}
\tag{40}
\]

Pour deux directions orthogonales unitaires,

\[
\left\langle
|(e' /|e'|)\cdot\theta|\,|e\cdot\theta|
\right\rangle
=\frac{2}{3\pi}.
\tag{41}
\]

Comme le produit signé a moyenne nulle et `0≤Φ≤M`, le principe de baignoire signé améliore ce facteur de moitié :

\[
\left|
\left\langle
\Phi(e'\cdot\theta)(e\cdot\theta)
\right\rangle
\right|
\leq\frac{M}{3\pi}|e'|.
\tag{42}
\]

De plus,

\[
|e'\cdot\theta|
\leq|e'|\sqrt{1-q^2},
\]

donc

\[
|A_e(s)|
\leq
|e'(s)|
\left(
\frac{M}{3\pi}+\mathcal E_e(s)
\right).
\tag{43}
\]

Pour un axe absolument continu, on peut ainsi remplacer le coût mobile de (9) par

\[
\int_I
|e'|
\min\left\{
\frac M2,
\frac{M}{3\pi}+\mathcal E_e
\right\}ds.
\tag{44}
\]

Cette amélioration ne s’étend pas automatiquement aux sauts de l’axe : la valeur de `ξ-e` doit alors être synchronisée avec les deux traces de `e`.

## 9. Faible-`L^{3/2}`, BMO et variation de l’axe

### 9.1 La norme critique ne fournit pas la masse par blocs

La borne `Φ≤M` entraîne la borne locale habituelle

\[
\|W\mathbf1_{B_{R_*}}\|_{L^{3/2,\infty}}
\leq
\left(\frac{4\pi}{3}\right)^{2/3}M.
\tag{45}
\]

Mais une borne faible tridimensionnelle ne donne aucune minoration de `p_k`. Une amplitude peut disparaître sur une infinité de blocs, ou se concentrer sur des coquilles minces. La « masse critique par blocs » de (34) est donc une hypothèse supplémentaire explicite, compatible avec l’échelle critique mais non produite par elle.

### 9.2 BMO n’est pas une variation totale

La semi-norme BMO mesure une oscillation spatiale moyenne; elle ne contrôle pas directement la longueur de la courbe `s↦e(s)` sur `S²`. Au niveau des tranches angulaires, le champ

\[
\xi(s,\theta)=e(s)
\]

a une oscillation BMO nulle pour chaque `s`, alors que `e(s)` peut avoir une variation totale arbitraire. Cet exemple n’est pas présenté comme une vorticité solénoïdale; il réfute seulement l’implication fonctionnelle « BMO par tranche implique variation de l’axe ».

Même une taille d’incrément `O(1/s)` n’est pas sommable en variation :

\[
e(s)=(\cos\log s,\sin\log s,0)
\quad\Longrightarrow\quad
|e'(s)|=\frac1s,
\qquad
\operatorname{Var}_{[s_0,\infty)}(e)=\infty.
\tag{46}
\]

Un raccord depuis `bmo_φ` vers (9) devrait donc prouver séparément une borne de variation ou un coût mobile pondéré. Il ne peut pas remplacer `Var(e)` par une semi-norme BMO sans lemme supplémentaire.

## 10. Passe contradictoire

### Attaque A — régularité de l’axe

Pour `e∈W^{1,1}`, (16) est classique. Pour `e∈BV`, les sauts produisent le terme de Stieltjes (25) et coûtent au plus `(M/2)|Δe|`. Pour un axe seulement mesurable, `J'` n’est pas défini et aucune borne de type (9) ne suit.

**Verdict :** l’existence d’un axe à chaque échelle ne suffit pas; il faut une sélection au moins `BV` ou un contrôle direct du terme mobile.

### Attaque B — axes choisis indépendamment par bloc

Si chaque bloc possède un axe `e_k` mais que ces axes ne sont pas raccordés, appliquer (9) séparément paie le budget de bord `M` à chaque bloc et ne produit aucune contradiction cumulative. Les raccorder en une fonction constante par morceaux ajoute

\[
\sum_k|e_{k+1}-e_k|
\]

à la variation totale.

**Verdict :** le quantificateur utile est « il existe une sélection globale à variation contrôlée », non « pour chaque bloc il existe un axe ».

### Attaque C — blocs non contigus

Sur une lacune entre deux bons blocs, `D_e` peut devenir négatif et recharger `J`. Sommer seulement les contributions positives des bons blocs viole l’identité (23).

**Verdict :** les blocs doivent être contigus, ou les lacunes doivent porter leurs propres bornes d’erreur et de variation.

### Attaque D — masse scalaire concentrée aux pôles

Une minoration de `〈Φ〉` n’est pas directement une minoration de `M_e`. La concentration optimale sur les calottes polaires donne exactement la perte quadratique `f_M(P)∼P²/M` pour petite masse.

**Verdict :** remplacer (11) par la fausse borne linéaire `M_e≥cP` sans hypothèse d’anti-concentration invalide les constantes.

### Attaque E — axe non unique

Lorsque la masse est faible, plusieurs axes peuvent presque minimiser `E_e`. Une sélection qui change de minimiseur peut avoir une variation énorme sans changement matériel du champ. Inversement, choisir a posteriori l’axe qui maximise le budget peut créer une circularité.

Pour la direction de vorticité, l’axe est orienté : `e` et `-e` ne sont pas équivalents. Si l’objet géométrique étudié est une ligne non orientée, la variation doit être définie dans `RP²` avec la distance

\[
d_{\mathrm{ligne}}(e,f)
=\min\{|e-f|,|e+f|\}.
\tag{47}
\]

**Verdict :** la règle de sélection et l’orientation doivent être figées avant de calculer la variation.

### Attaque F — oscillations rapides réellement solénoïdales

Soit `a(s)` une courbe bornée quelconque et

\[
\Omega(s,\theta)=a(s)\times\theta.
\tag{48}
\]

Alors `Ω_r=0` et `div_SΩ_T=0`; (3) est satisfaite quelle que soit la fréquence de `a`. Pour `|a|=1`,

\[
\langle\Phi\rangle
=\langle|a\times\theta|\rangle
=\frac\pi4,
\tag{49}
\]

donc le profil possède une masse scalaire par bloc non nulle et une borne critique uniforme. En choisissant

\[
a(s)=(\cos s^3,\sin s^3,0),
\]

on obtient un motif solénoïdal à oscillation accélérée. Sa direction n’est toutefois proche d’aucun axe spatial constant sur toute la sphère, et son erreur `E_e` paie cette défaillance.

**Verdict :** divergence, masse par blocs et faible-`L^{3/2}` ne contrôlent pas à elles seules la fréquence d’un axe ou d’un motif.

### Attaque G — rotation suffisamment rapide

Même avec une petite erreur directionnelle, (9) ne donne aucune contradiction si

\[
\frac M2\operatorname{Var}(e)
\]

croît au même rythme que la masse transverse. Cela ne construit pas un profil, mais montre que la preuve par moment ne peut exclure ce régime.

**Verdict :** la condition d’excès (10) est la frontière réelle de cette méthode.

## 11. Lemme minimal transférable

Le noyau destiné au graphe de preuve est :

> **Budget à axe mobile.** Pour `W=r^{-2}Ω(log(R_*/r),θ)` divergence-free, `|Ω|≤M` et toute sélection d’axe `e∈BV([s_0,S];S²)`, le moment `J=〈(e·θ)Ω_r〉` vérifie une identité de transport dont le coût mobile est au plus `(M/2)Var(e)`. Toute masse transverse cumulée, après soustraction de l’erreur pondérée de direction et du coût de variation, est bornée par l’unique budget de bord `M`. Une masse scalaire moyenne `P` produit au moins `f_M(P)=P²/M-P³/(3M²)` de masse transverse, constante optimale sous `0≤Φ≤M`.

En formulation entièrement correcte :

\[
e\in BV([s_0,S];S^2),
\qquad
\int_{s_0}^{S}(\mathcal M_e-\mathcal E_e)ds
\leq
M+\frac M2\operatorname{Var}_{[s_0,S]}(e).
\tag{50}
\]

## 12. Prochain test décisif

Pour un profil candidat discrétisé en `s` et sur `S²` :

1. sélectionner `e(s)` par une règle fixée avant le calcul;
2. certifier `P(s)`, `M_e(s)` et `E_e(s)` avec quadrature sphérique bornée;
3. calculer `Var(e)` en incluant les changements de blocs et les ambiguïtés de signe;
4. vérifier le résidu de l’identité
   \[
   R_J=J'+D_e-A_e;
   \]
5. tester (35) avec un terme d’erreur accumulé provenant de `R_J`.

Une violation certifiée de (35) ne serait pas un blow-up : elle réfuterait au moins une des hypothèses de l’ansatz, de la sélection d’axe ou de la solénoïdalité numérique.

## 13. Statut de preuve

Toutes les affirmations nouvelles de ce rapport sont des dérivations IA internes. Elles n’ont reçu ni revue par les pairs, ni formalisation, ni validation inter-familles. Aucune ne doit être étiquetée `PAPER_PROOF`.
