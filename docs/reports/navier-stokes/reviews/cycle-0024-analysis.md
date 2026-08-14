# Passe analytique contradictoire — cycle 0024 : des moyennes `bmo_φ` au budget d’axe mobile

Date : 2026-08-14

Statut : **dérivation IA interne**, non publiée, jamais `PAPER_PROOF`; passe séparée mais non indépendante inter-familles de modèles

## Verdict exécutif

Soit, dans `0<r<R_*`,

\[
W(r,\theta)=r^{-2}\Omega(s,\theta),
\qquad
s=\log\frac{R_*}{r},
\qquad
\Phi=|\Omega|\leq M.
\tag{1}
\]

Fixons les blocs logarithmiques unitaires

\[
I_n=[n,n+1],
\qquad n\geq n_0,
\tag{2}
\]

et la moyenne sphérique normalisée

\[
\langle f(s,\cdot)\rangle
=\frac1{4\pi}\int_{S^2}f(s,\theta)dS(\theta).
\tag{3}
\]

Les hypothèses analysées sont :

\[
\int_{I_n}
\langle\Phi(s,\cdot)^{3/2}\rangle ds
\geq\kappa>0
\quad\text{pour tout }n\geq n_0,
\tag{4}
\]

et l’existence d’une extension mesurable `ζ` de la direction telle que

\[
|\zeta|\leq1,
\qquad
\zeta=\xi:=\Omega/|\Omega|
\quad\text{sur }\{\Phi>0\}.
\tag{5}
\]

Sur les boules centrées

\[
B_n:=B_{r_n}(0),
\qquad
r_n=R_*e^{-n},
\]

supposons

\[
\delta_n
:=\fint_{B_n}|\zeta-m_n|dx
\leq\frac{B}{1+n},
\qquad
m_n:=\fint_{B_n}\zeta\,dx.
\tag{6}
\]

Posons

\[
\alpha=\frac{\kappa}{M^{3/2}}\in(0,1],
\qquad
\boxed{
\beta=\frac{e^{3\alpha}-1}{e^3-1}}.
\tag{7}
\]

La masse (4) force au moins une fraction `α` de points actifs en mesure logarithmique-angulaire dans chaque bloc. Après conversion exacte vers le volume physique, la fraction active de chaque coquille, puis de chaque boule `B_n`, est au moins `β`.

Cette fraction empêche l’annulation de la moyenne :

\[
\boxed{
|m_n|\geq1-\frac{\delta_n}{\beta}}.
\tag{8}
\]

Dès que `δ_n≤β/2`, l’axe orienté

\[
e_n=\frac{m_n}{|m_n|}
\tag{9}
\]

est bien défini et vérifie

\[
\fint_{B_n}|\zeta-e_n|dx
\leq
\left(1+\frac1\beta\right)\delta_n.
\tag{10}
\]

Les boules étant emboîtées avec `|B_n|/|B_{n+1}|=e^3`, leurs axes satisfont

\[
|e_{n+1}-e_n|
\leq
\frac{2e^3\delta_n}
{1-\delta_n/\beta}
\leq4e^3\frac{B}{1+n}
\tag{11}
\]

dans ce régime. La sélection constante par morceaux `e(s)=e_n` sur `I_n` a donc une variation cumulée `O(log N)`.

L’erreur directionnelle pondérée du cycle 0023 est également sommable bloc par bloc à coût harmonique :

\[
E_n
:=\int_{I_n}
\left\langle
\Phi|\xi-e_n|
\sqrt{1-(e_n\cdot\theta)^2}
\right\rangle ds
\leq
\frac{Me^3B}{3(1+n)}
\left(1+\frac1\beta\right).
\tag{12}
\]

Enfin, (4) force dans chaque bloc une masse transverse minimale

\[
\int_{I_n}
\left\langle
\Phi[1-(e_n\cdot\theta)^2]
\right\rangle ds
\geq
M\left(\alpha^2-\frac{\alpha^3}{3}\right).
\tag{13}
\]

Le budget à axe mobile du cycle 0023 implique alors, pour tout `N>n_*`,

\[
\boxed{
(N-n_*)
\left(\alpha^2-\frac{\alpha^3}{3}\right)
\leq
1+e^3B
\left[
2+\frac13\left(1+\frac1\beta\right)
\right]
(H_N-H_{n_*})},
\tag{14}
\]

où `H_N=∑_{j=1}^N1/j`, avec la convention `H_0=0`, et

\[
n_*\geq
\max\left\{
n_0,
\left\lceil\frac{2B}{\beta}-1\right\rceil
\right\}.
\tag{15}
\]

Le membre de gauche de (14) croît linéairement en `N`, le membre de droite logarithmiquement. Les hypothèses (1), (4)–(6) et `div W=0` ne peuvent donc toutes persister jusqu’à `s=+∞`. Ce résultat est conditionnel : il ne montre pas qu’une solution Navier–Stokes satisfait l’ansatz ou la masse uniforme par blocs.

## 1. Formulation exacte et normalisations

Le champ `W` est supposé divergence-free sur le domaine ponctué. Avec la convention de (1),

\[
\partial_s\Omega_r
=\operatorname{div}_{S^2}\Omega_T.
\tag{16}
\]

La quantité `κ` de (4) est une **masse moyenne sur un bloc unitaire** en mesure `ds dS/(4π)`. L’hypothèse impose nécessairement

\[
0<\kappa\leq M^{3/2}.
\tag{17}
\]

Si les blocs ont une autre largeur, les constantes doivent être remises à l’échelle comme indiqué en section 10; on ne peut pas garder simultanément (4) et (7) sans préciser si `κ` est une intégrale ou une moyenne.

L’oscillation (6) est calculée autour de la moyenne vectorielle `m_n`. La borne `|ζ|≤1` implique

\[
|m_n|\leq1.
\tag{18}
\]

Sur l’ensemble actif `{Φ>0}`, (5) donne `|ζ|=|ξ|=1`. Sur les zéros de `Φ`, aucune direction physique n’est imposée; l’extension peut prendre n’importe quelle valeur dans la boule unité.

## 2. Fraction active en mesure logarithmique

Notons

\[
A_n=\{(s,\theta)\in I_n\times S^2:\Phi(s,\theta)>0\}.
\]

Comme

\[
\Phi^{3/2}
\leq M^{3/2}\mathbf1_{A_n},
\]

(4) donne

\[
\int_{I_n}
\langle\mathbf1_{A_n}\rangle ds
\geq\frac\kappa{M^{3/2}}
=\alpha.
\tag{19}
\]

La constante est optimale : elle est atteinte, au niveau de cette seule contrainte, par `Φ=M` sur une partie de mesure `α` et `Φ=0` ailleurs.

Cette fraction est mesurée uniformément en `s`. Elle n’est pas encore la fraction volumique physique de la coquille correspondante.

## 3. Conversion volume logarithmique–volume physique

La coquille associée à `I_n` est

\[
\mathcal A_n
=B_{r_n}\setminus B_{r_{n+1}}.
\]

Écrivons `s=n+\tau`, `0≤τ≤1`. Le volume physique porte le poids

\[
dx
=R_*^3e^{-3(n+\tau)}\,d\tau\,dS.
\tag{20}
\]

Si

\[
a_n(\tau)
=\langle\mathbf1_{A_n}(n+\tau,\cdot)\rangle,
\]

la fraction active de la coquille est

\[
\operatorname{Frac}_{\mathcal A_n}(A_n)
=
\frac{
\int_0^1e^{-3\tau}a_n(\tau)d\tau
}{
\int_0^1e^{-3\tau}d\tau
}.
\tag{21}
\]

Sous `0≤a_n≤1` et `∫_0^1a_n≥α`, cette fraction est minimale en plaçant toute l’activité au bord intérieur, où le poids est le plus faible :

\[
a_n(\tau)
=\mathbf1_{[1-\alpha,1]}(\tau).
\]

Le principe de baignoire donne donc la constante optimale

\[
\begin{aligned}
\operatorname{Frac}_{\mathcal A_n}(A_n)
&\geq
\frac{
\int_{1-\alpha}^{1}e^{-3\tau}d\tau
}{
\int_0^1e^{-3\tau}d\tau
}\\
&=\frac{e^{3\alpha}-1}{e^3-1}
=\beta.
\end{aligned}
\tag{22}
\]

Chaque boule `B_n` est l’union disjointe, à un ensemble de mesure nulle près, des coquilles `A_j`, `j≥n`. Si (4) vaut sur tous ces blocs, chacune a une fraction active au moins `β`. Par moyenne pondérée,

\[
\frac{|B_n\cap\{\Phi>0\}|}{|B_n|}
\geq\beta.
\tag{23}
\]

La substitution naïve de `α` à `β` serait fausse : pour petite `α`,

\[
\beta
=\frac{3}{e^3-1}\alpha+O(\alpha^2),
\tag{24}
\]

donc le pire placement radial perd le facteur `3/(e³-1)`.

## 4. Non-annulation des moyennes

Posons

\[
E_n=B_n\cap\{\Phi>0\}.
\]

Sur `E_n`, `|ζ|=1`; par (18), `|m_n|≤1`. L’inégalité triangulaire inverse donne

\[
|\zeta-m_n|
\geq
\bigl||\zeta|-|m_n|\bigr|
=1-|m_n|
\quad\text{sur }E_n.
\tag{25}
\]

En intégrant et en utilisant (23),

\[
\delta_n
\geq
\frac{|E_n|}{|B_n|}
(1-|m_n|)
\geq
\beta(1-|m_n|).
\tag{26}
\]

C’est exactement (8).

### Seuil explicite

Choisissons

\[
n_*
=\max\left\{
n_0,
0,
\left\lceil\frac{2B}{\beta}-1\right\rceil
\right\}.
\tag{27}
\]

Pour tout `n≥n_*`,

\[
\delta_n\leq\frac\beta2,
\qquad
|m_n|\geq\frac12.
\tag{28}
\]

L’axe orienté (9) est alors unique. Aucun choix de signe n’est permis : il est fixé par la moyenne de l’extension.

### Erreur de normalisation

Puisque `m_n=|m_n|e_n`,

\[
|m_n-e_n|=1-|m_n|\leq\frac{\delta_n}{\beta}.
\tag{29}
\]

Par conséquent,

\[
\begin{aligned}
\fint_{B_n}|\zeta-e_n|dx
&\leq
\fint_{B_n}|\zeta-m_n|dx
+|m_n-e_n|\\
&\leq
\left(1+\frac1\beta\right)\delta_n.
\end{aligned}
\tag{30}
\]

La présence éventuelle d’un grand ensemble de zéros est entièrement absorbée dans `β`; aucune convention particulière sur `ζ` aux zéros n’est utilisée au-delà de `|ζ|≤1`.

## 5. Incréments des axes de boules emboîtées

Comme `B_{n+1}⊂B_n` et

\[
\frac{|B_n|}{|B_{n+1}|}=e^3,
\]

on a

\[
\begin{aligned}
|m_{n+1}-m_n|
&=\left|
\fint_{B_{n+1}}(\zeta-m_n)dx
\right|\\
&\leq
\frac{|B_n|}{|B_{n+1}|}
\fint_{B_n}|\zeta-m_n|dx\\
&\leq e^3\delta_n.
\end{aligned}
\tag{31}
\]

Pour deux vecteurs non nuls `a,b`,

\[
\left|
\frac a{|a|}-\frac b{|b|}
\right|
\leq
\frac{2|a-b|}{\min\{|a|,|b|\}}.
\tag{32}
\]

Les bornes (8) et la décroissance de `δ_n` donnent donc

\[
|e_{n+1}-e_n|
\leq
\frac{2e^3\delta_n}
{1-\delta_n/\beta}.
\tag{33}
\]

Sous (28),

\[
|e_{n+1}-e_n|
\leq4e^3\frac B{1+n}.
\tag{34}
\]

Définissons `e(s)=e_n` sur chaque `I_n`. Sur `[n_*,N]`, en incluant la trace finale `e_N`,

\[
\begin{aligned}
\operatorname{Var}_{[n_*,N]}(e)
&\leq
4e^3B
\sum_{n=n_*}^{N-1}\frac1{1+n}\\
&=4e^3B(H_N-H_{n_*}).
\end{aligned}
\tag{35}
\]

La variation est donc `O(log N)`, pas uniformément bornée. Cette distinction est cruciale : la pondération `1/(1+s)` est harmonique, non sommable.

## 6. Conversion de l’erreur de boule vers l’erreur de bloc

Pour une fonction positive `g`, le changement de variables radial donne exactement

\[
\fint_{B_n}g(x)dx
=3\int_0^\infty
e^{-3\tau}
\langle g(n+\tau,\cdot)\rangle d\tau.
\tag{36}
\]

Appliquons cette identité à

\[
g_n=|\zeta-e_n|.
\]

La borne (30) implique

\[
3\int_0^\infty
e^{-3\tau}\langle g_n(n+\tau)\rangle d\tau
\leq
\left(1+\frac1\beta\right)\delta_n.
\tag{37}
\]

Sur le premier bloc, `e^{-3τ}≥e^{-3}`. Ainsi

\[
\int_0^1
\langle g_n(n+\tau)\rangle d\tau
\leq
\frac{e^3}{3}
\left(1+\frac1\beta\right)
\delta_n.
\tag{38}
\]

Sur `{Φ>0}`, `ζ=ξ`; sur `{Φ=0}`, le poids directionnel est nul. De plus `sqrt(1-(e_n·θ)²)≤1` et `Φ≤M`. Il vient

\[
\begin{aligned}
E_n
&=\int_{I_n}
\left\langle
\Phi|\xi-e_n|
\sqrt{1-(e_n\cdot\theta)^2}
\right\rangle ds\\
&\leq
M\int_0^1
\langle|\zeta-e_n|\rangle d\tau\\
&\leq
\frac{Me^3}{3}
\left(1+\frac1\beta\right)
\delta_n.
\end{aligned}
\tag{39}
\]

C’est (12). En sommant,

\[
\sum_{n=n_*}^{N-1}E_n
\leq
\frac{Me^3B}{3}
\left(1+\frac1\beta\right)
(H_N-H_{n_*}).
\tag{40}
\]

L’erreur cumulée est elle aussi `O(log N)`.

## 7. Masse transverse issue de `Φ^{3/2}`

Pour un axe quelconque `e`, posons à chaque `s`

\[
P(s)=\langle\Phi(s,\cdot)\rangle.
\]

Comme `0≤Φ≤M`,

\[
\Phi^{3/2}\leq M^{1/2}\Phi,
\]

et (4) donne

\[
\int_{I_n}P(s)ds
\geq\frac\kappa{M^{1/2}}
=M\alpha.
\tag{41}
\]

Le principe de baignoire sphérique du cycle 0023 affirme

\[
\left\langle
\Phi[1-(e\cdot\theta)^2]
\right\rangle
\geq
f_M(P),
\qquad
f_M(P)=\frac{P^2}{M}-\frac{P^3}{3M^2}.
\tag{42}
\]

La fonction `f_M` est croissante et convexe sur `[0,M]`. Pour l’axe constant `e_n` dans `I_n`, Jensen et (41) donnent

\[
\begin{aligned}
\int_{I_n}
\left\langle
\Phi[1-(e_n\cdot\theta)^2]
\right\rangle ds
&\geq
f_M\left(\int_{I_n}P(s)ds\right)\\
&\geq f_M(M\alpha)\\
&=M\left(\alpha^2-\frac{\alpha^3}{3}\right).
\end{aligned}
\tag{43}
\]

Cette constante est optimale sous les seules contraintes de bloc : prendre `Φ=M` sur deux calottes polaires de fraction totale `α`, identiques pour presque tout `s` du bloc, sature simultanément la masse `Φ^{3/2}` et la baignoire transverse.

## 8. Raccord quantitatif au budget du cycle 0023

Le budget à axe mobile, avec moyennes sphériques normalisées, est

\[
\int_{n_*}^{N}
(\mathcal M_e-\mathcal E_e)ds
\leq
M+\frac M2
\operatorname{Var}_{[n_*,N]}(e),
\tag{44}
\]

où

\[
\mathcal M_e
=\left\langle
\Phi[1-(e\cdot\theta)^2]
\right\rangle.
\]

Pour la sélection constante par morceaux construite ci-dessus, (35), (40), (43) et (44) donnent

\[
\begin{aligned}
(N-n_*)M
\left(\alpha^2-\frac{\alpha^3}{3}\right)
&\leq M\\
&\quad+
\frac{Me^3B}{3}
\left(1+\frac1\beta\right)
(H_N-H_{n_*})\\
&\quad+
2Me^3B(H_N-H_{n_*}).
\end{aligned}
\tag{45}
\]

Après division par `M`, c’est exactement (14).

Comme

\[
H_N-H_{n_*}
\leq
\log\frac{N}{n_*}
\quad(n_*\geq1),
\tag{46}
\]

le membre de droite est `O(log N)`, tandis que

\[
\alpha^2-\frac{\alpha^3}{3}>0
\quad\text{pour }\alpha>0.
\]

Il existe donc un `N` fini au-delà duquel (45) est impossible. Le résultat négatif précis est :

> Aucun ansatz solénoïdal (1), borné par `Φ≤M`, ne peut conserver une masse `Φ^{3/2}` au moins `κ>0` dans **chaque** bloc logarithmique intérieur tout en admettant une extension de direction dans la boule unité dont l’oscillation moyenne sur toutes les boules centrées décroît comme `B/(1+s)`.

Ce lemme ne requiert pas de minoration ponctuelle de `Φ`; les zéros sont autorisés et suivis quantitativement par `α` puis `β`.

## 9. Forme avec résidus

Si la contrainte solénoïdale ou l’identité de moment du cycle 0023 n’est vérifiée qu’avec un résidu cumulé `R_N≥0`, le budget devient

\[
(N-n_*)
\left(\alpha^2-\frac{\alpha^3}{3}\right)
\leq
1+e^3B
\left[
2+\frac13\left(1+\frac1\beta\right)
\right]
(H_N-H_{n_*})
+\frac{R_N}{M}.
\tag{47}
\]

Une expérience numérique ne peut conclure à une obstruction que si `R_N=o(N)` avec une borne certifiée. Un résidu simplement borné bloc par bloc par une constante produit `R_N=O(N)` et peut absorber toute la masse transverse.

## 10. Blocs de largeur générale

Soient des blocs

\[
I_n=[S_n,S_n+h],
\qquad S_{n+1}=S_n+h,
\]

et supposons une **moyenne** de masse

\[
\frac1h\int_{I_n}
\langle\Phi^{3/2}\rangle ds
\geq\kappa_h.
\]

Alors

\[
\alpha_h=\frac{\kappa_h}{M^{3/2}},
\qquad
\beta_h
=\frac{e^{3h\alpha_h}-1}{e^{3h}-1}.
\tag{48}
\]

Le rapport de volume de deux boules consécutives est `e^{3h}`, et la conversion boule–bloc remplace `e³/3` par

\[
\frac{e^{3h}}{3}.
\tag{49}
\]

si l’erreur de bloc reste exprimée comme une intégrale en `ds`. Plus explicitement,

\[
\int_0^h\langle g(S_n+\tau)\rangle d\tau
\leq
\frac{e^{3h}}3
\fint_{B_{S_n}}g\,dx.
\tag{50}
\]

La masse transverse minimale du bloc devient

\[
hM\left(
\alpha_h^2-\frac{\alpha_h^3}{3}
\right).
\tag{51}
\]

Ces formules montrent pourquoi la largeur de bloc doit être figée avant toute comparaison de constantes.

## 11. Passe contradictoire

### Attaque A — zéros de la vorticité

L’extension peut utiliser les zéros pour modifier sa moyenne. La preuve ne suppose ni `ζ=0`, ni continuité sur ces zéros. Elle utilise uniquement `|ζ|≤1`, `|ζ|=1` sur l’ensemble actif et la fraction volumique `β`.

Si `κ=0`, alors `α=β=0`; (8) ne fournit plus aucune non-annulation et les axes normalisés peuvent ne pas exister.

**Verdict :** la masse positive par chaque bloc est indispensable à cette stratégie.

### Attaque B — suppression de la borne `|ζ|≤1`

Sans cette borne, `|m_n|≤1` est faux. L’inégalité (25) ne donne plus `1-|m_n|`, et des valeurs arbitrairement grandes sur les zéros peuvent déplacer la moyenne sans représenter une direction.

**Verdict :** la contrainte de boule unité sur l’extension est structurelle, pas cosmétique.

### Attaque C — confusion entre fraction logarithmique et fraction physique

L’hypothèse (4) donne `α` en mesure uniforme `ds dS`; les moyennes BMO sont prises en `dx`, qui porte le poids `e^{-3s}`. Le pire placement au bord intérieur d’une coquille réduit la fraction à `β`.

**Verdict :** utiliser `α` dans (8) surestime la non-annulation; la constante sûre est (7).

### Attaque D — erreur de boule versus erreur de bloc

Une boule centrée est dominée en volume par sa coquille extérieure. Le contrôle du premier bloc intérieur perd le facteur exact `e³/3` dans (38). Inversement, la moyenne sur la boule ne contrôle pas uniformément chaque profondeur `τ` du bloc.

**Verdict :** seule l’erreur intégrée en `s` est obtenue; une borne ponctuelle en `s` demanderait une hypothèse supplémentaire.

### Attaque E — blocs manquants

La borne de fraction active de `B_n` utilise (4) sur toutes les coquilles `j≥n`. Si la masse n’est présente que sur une sous-suite de blocs, la fraction de la boule peut tendre vers zéro et les intervalles vides peuvent faire tourner ou recharger le moment.

**Verdict :** « pour tout bloc intérieur » ne peut pas être remplacé par « pour une infinité de blocs ».

### Attaque F — blocs non contigus ou de largeur variable

Le raccord au cycle 0023 paie le budget de bord `M` une seule fois parce que les blocs couvrent un intervalle contigu. Des lacunes non contrôlées peuvent donner une contribution négative au moment. Une largeur variable change simultanément `β`, le rapport des volumes, l’erreur et la masse transverse.

**Verdict :** les quantificateurs et la partition font partie du lemme.

### Attaque G — axe issu d’une moyenne presque nulle

Normaliser une moyenne sans borne inférieure amplifie arbitrairement ses perturbations. Le seuil `δ_n≤β/2` garantit `|m_n|≥1/2` et rend la constante `4e³` de (34) légitime.

**Verdict :** toute construction d’axes avant le seuil `n_*` doit être exclue du budget ou traitée séparément.

### Attaque H — variation logarithmique non sommable

Les incréments `O(1/n)` donnent `Var(e)=O(log N)`, non une variation totale finie jusqu’à l’origine. L’obstruction survit néanmoins parce que la masse transverse est `O(N)`.

**Verdict :** prétendre à une convergence de `e_n` serait faux; le raccord nécessite seulement que la variation soit sous-linéaire.

### Attaque I — rôle de la pondération `Φ^{3/2}`

La masse critique ne contrôle pas ponctuellement `Φ`. Le passage

\[
\Phi^{3/2}\leq M^{1/2}\Phi
\]

perd exactement le facteur `M^{1/2}`. Sans borne supérieure `M`, une masse `Φ^{3/2}` peut se concentrer sur un ensemble de volume arbitrairement petit et `α`, `β` s’effondrent.

**Verdict :** `Φ≤M` est indispensable à la fraction active et au budget de bord.

### Attaque J — BMO complet versus boules centrées

Le calcul utilise uniquement les boules centrées à l’origine. Une norme `bmo_φ` globale avec

\[
\phi(r)=\frac1{1+\log(R_*/r)}
\]

implique (6) sur ces boules avec `B` égal à sa semi-norme, mais la réciproque est fausse.

**Verdict :** le lemme est une conséquence nécessaire plus faible du contrôle global; il ne certifie aucune extension `bmo_φ` hors des boules centrées.

## 12. Lemme minimal transférable

> **Raccord masse–moyennes–moment.** Sous `Φ≤M`, une masse normalisée `∫_{I_n}〈Φ^{3/2}〉≥κ>0` dans chaque bloc logarithmique unitaire impose une fraction active physique `β=(e^{3κ/M^{3/2}}-1)/(e³-1)` dans chaque boule centrée. Une extension dans la boule unité dont l’oscillation moyenne est `≤B/(1+n)` possède alors, après un seuil explicite, des moyennes non nulles dont les axes normalisés ont variation cumulée `O(log N)` et erreur directionnelle pondérée cumulée `O(log N)`. La masse transverse imposée est `O(N)`; le budget solénoïdal à axe mobile est donc violé à profondeur finie.

Le maillon reste conditionnel à l’existence de l’extension `ζ`, à la masse dans chaque bloc, à la borne `Φ≤M` et à l’ansatz log-radial. Il ne produit ni une solution Navier–Stokes, ni un blow-up, ni une régularité globale.

## 13. Prochain test décisif

Pour un profil candidat discrétisé :

1. certifier `M` et la masse `κ` dans chaque bloc;
2. mesurer la fraction active physique et vérifier la borne `β`;
3. calculer `m_n`, sa marge `|m_n|-(1-δ_n/β)` et l’axe `e_n`;
4. sommer exactement les incréments d’axes et les erreurs pondérées;
5. vérifier le résidu de divergence et du moment mobile;
6. confronter la masse transverse cumulée au membre de droite de (47).

Une conclusion certifiée exige des bornes d’erreur sur les quadratures angulaires, le poids radial `e^{-3s}`, les moyennes vectorielles et les résidus. Une simulation flottante sans ces bornes ne transforme pas (14) en preuve.

## 14. Statut de preuve

Toutes les affirmations nouvelles de ce rapport sont des dérivations IA internes. Elles n’ont reçu ni revue par les pairs, ni formalisation, ni validation inter-familles. Aucune ne doit être étiquetée `PAPER_PROOF`.
