# Passe analytique contradictoire — cycle 0022 : rectification lente d’un profil critique log-radial

Date : 2026-08-14

Statut : **dérivation IA interne**, non publiée, jamais `PAPER_PROOF`; passe séparée mais non indépendante inter-familles de modèles

## Verdict exécutif

Considérons, dans `0<r<R_*`,

\[
W(r,\theta)=r^{-2}\Omega(s,\theta),
\qquad
s=\log\frac{R_*}{r},
\qquad
\Omega=\Phi\xi,
\qquad |\xi|=1.
\tag{1}
\]

Le signe exact de la contrainte solénoïdale est

\[
\boxed{
\operatorname{div}W
=r^{-3}
\left(
\operatorname{div}_{S^2}\Omega_T
-\partial_s\Omega_r
\right)}.
\tag{2}
\]

Le signe devant `∂sΩ_r` est **négatif**, parce que `∂_r s=-1/r`. Ainsi `div W=0` équivaut à

\[
\partial_s\Omega_r
=\operatorname{div}_{S^2}\Omega_T.
\tag{3}
\]

Fixons un vecteur unitaire `e` et supposons, pour tout `s` assez grand,

\[
0<m\leq\Phi(s,\theta)\leq M,
\qquad
\|\xi(s,\cdot)-e\|_{L^\infty(S^2)}
\leq\frac Cs.
\tag{4}
\]

Alors aucun profil défini jusqu’à `s=+∞` ne peut satisfaire (3). Plus quantitativement, après

\[
s_c=\frac{3\pi MC}{4m},
\tag{5}
\]

la rectification ne peut persister sur un intervalle logarithmique de longueur supérieure à

\[
\boxed{\frac{3M}{m}}.
\tag{6}
\]

Le mécanisme est un budget exact sur le premier harmonique sphérique. Avec

\[
q(\theta)=e\cdot\theta,
\qquad
B_e(s)=\int_{S^2}\Omega_r(s,\theta)q(\theta)\,dS,
\tag{7}
\]

la contrainte (3) donne

\[
B_e'(s)
=-D_e(s),
\qquad
D_e(s):=
\int_{S^2}\Omega(s,\theta)
\cdot\nabla_{S^2}q(\theta)\,dS.
\tag{8}
\]

La rectification vers `e`, jointe à `Φ≥m`, force `D_e(s)` à rester strictement positif, tandis que `|B_e(s)|≤2πM`. Le moment borné ne peut donc décroître linéairement sur une profondeur logarithmique infinie.

Cette obstruction résiste à des oscillations arbitrairement rapides en `s` tant que (4) est uniforme. En revanche, elle disparaît si la borne inférieure `Φ≥m` est retirée :

\[
\Omega(s,\theta)=e^{-2s}e
\quad\Longrightarrow\quad
W(x)=R_*^{-2}e,
\tag{9}
\]

qui est divergence-free et possède exactement la direction `e`, mais n’est plus un cœur critique non dégénéré. La simple notation `O(r^{-2})` et l’appartenance faible-`L^{3/2}` ne suffisent donc pas à fournir l’hypothèse cruciale `m>0`.

## 1. Cadre et quantificateurs

Le rapport étudie un champ vectoriel spatial à temps fixé. Il ne suppose ni que ce champ résout l’équation de vorticité, ni qu’il apparaît comme limite d’une solution de Navier–Stokes.

Les hypothèses de régularité minimales utilisées pour les identités fortes sont :

- `Ω∈W^{1,1}_loc((s_0,∞)×S²;R³)`;
- `Φ=|Ω|` et `ξ=Ω/Φ` là où `Φ>0`;
- `Ω_r=Ω·θ` et `Ω_T=Ω-Ω_rθ`;
- la contrainte `div W=0` dans les distributions sur le domaine ponctué.

Pour le lemme quantitatif, on ajoute les bornes ponctuelles (4). Une version distributionnelle de l’identité de moment ne requiert aucune borne séparée sur `∂sξ`.

La formulation primaire du profil impose à son facteur scalaire une borne de type

\[
|\nabla_x\Phi|\lesssim r^{-1}.
\]

Dans les variables `(s,θ)`,

\[
\nabla_x\Phi
=\frac1r
\left(-\partial_s\Phi\,\theta
+\nabla_{S^2}\Phi\right),
\tag{10}
\]

donc cette hypothèse contrôle

\[
\left(
|\partial_s\Phi|^2
+|\nabla_{S^2}\Phi|^2
\right)^{1/2}
\tag{11}
\]

par une constante. Elle ne contrôle pas `∂sξ`. L’exclusion ci-dessous demeure vraie même si `∂sΦ` ou `∂sξ` oscillent rapidement, dès lors que (3), `m≤Φ≤M` et la proximité uniforme de direction restent valides.

## 2. Vérification du signe de la divergence

La formule sphérique est

\[
\operatorname{div}W
=\frac1{r^2}\partial_r(r^2W_r)
+\frac1r\operatorname{div}_{S^2}W_T.
\tag{12}
\]

Comme

\[
W_r=r^{-2}\Omega_r(s,\theta),
\qquad
W_T=r^{-2}\Omega_T(s,\theta),
\qquad
\partial_rs=-\frac1r,
\]

on obtient

\[
\frac1{r^2}\partial_r(r^2W_r)
=-r^{-3}\partial_s\Omega_r,
\qquad
\frac1r\operatorname{div}_{S^2}W_T
=r^{-3}\operatorname{div}_{S^2}\Omega_T,
\]

ce qui prouve (2).

### Test unitaire du signe

Prenons `Ω=e^{-2s}e`. Comme

\[
e=q\theta+\nabla_{S^2}q,
\qquad
\Delta_{S^2}q=-2q,
\tag{13}
\]

on a

\[
\partial_s\Omega_r=-2e^{-2s}q,
\qquad
\operatorname{div}_{S^2}\Omega_T
=e^{-2s}\Delta_{S^2}q
=-2e^{-2s}q.
\]

Leur différence dans (2) est nulle. Par ailleurs `r^{-2}e^{-2s}=R_*^{-2}`, donc `W` est le champ constant (9), effectivement divergence-free. Une formule portant un signe `+∂sΩ_r` échouerait sur ce test élémentaire.

## 3. Flux radial

Définissons le flux à la profondeur logarithmique `s` :

\[
F(s)=\int_{S^2}\Omega_r(s,\theta)\,dS.
\tag{14}
\]

En intégrant (3) sur la sphère,

\[
F'(s)
=\int_{S^2}\operatorname{div}_{S^2}\Omega_T\,dS
=0.
\tag{15}
\]

Le flux est donc constant en `s`, même pour un profil log-périodique. Pour que `W` soit le curl distributionnel d’une vitesse à travers l’origine, il faut en outre

\[
F(s)\equiv0.
\tag{16}
\]

Sinon, le champ transporte une charge de divergence `Fδ_0`. La condition (16) est une porte d’admissibilité globale séparée. Le lemme de rectification ci-dessous est plus fort sur un point : il donne déjà une contradiction sur le domaine ponctué et n’utilise pas (16).

## 4. Identité de budget du premier harmonique

Fixons `e∈S²` et posons

\[
q=e\cdot\theta.
\]

Les identités géométriques exactes sont

\[
\nabla_{S^2}q=e-q\theta,
\qquad
|\nabla_{S^2}q|^2=1-q^2,
\qquad
\Delta_{S^2}q=-2q.
\tag{17}
\]

Multiplions (3) par `q` et intégrons. Comme le gradient de `q` est tangent,

\[
\begin{aligned}
B_e'(s)
&=\int_{S^2}q\,\partial_s\Omega_r\,dS\\
&=\int_{S^2}q\,
  \operatorname{div}_{S^2}\Omega_T\,dS\\
&=-\int_{S^2}Omega_T\cdot\nabla_{S^2}q\,dS\\
&=-\int_{S^2}\Omega\cdot\nabla_{S^2}q\,dS
=-D_e(s).
\end{aligned}
\tag{18}
\]

Si seulement `|Ω|≤M`, alors

\[
|B_e(s)|
\leq M\int_{S^2}|q|\,dS
=2\pi M.
\tag{19}
\]

Par intégration de (18), tout intervalle `[s_0,s_1]` vérifie donc le budget exact

\[
\left|
\int_{s_0}^{s_1}D_e(s)\,ds
\right|
=|B_e(s_0)-B_e(s_1)|
\leq4\pi M.
\tag{20}
\]

### Lemme 4.1 — obstruction minimale signée

Sous `|Ω|≤M`, si

\[
D_e(s)\geq c>0
\quad\text{sur }[s_0,s_1],
\tag{21}
\]

alors

\[
s_1-s_0\leq\frac{4\pi M}{c}.
\tag{22}
\]

En particulier, aucune solution de (3) bornée ne peut avoir `D_e≥c` sur une demi-droite en `s`.

Cette forme est le lemme réellement minimal : la convergence de direction n’est qu’une condition suffisante explicite pour rendre `D_e` positif.

## 5. Exclusion quantitative de la rectification lente

Les constantes sphériques nécessaires sont

\[
\int_{S^2}(1-q^2)dS=\frac{8\pi}{3},
\qquad
\int_{S^2}|\nabla_{S^2}q|dS=\pi^2,
\qquad
\int_{S^2}|q|dS=2\pi.
\tag{23}
\]

Supposons `m≤Φ≤M` et notons

\[
\delta(s)=\|\xi(s,\cdot)-e\|_{L^\infty(S^2)}.
\]

Puisque `e·∇_Sq=|∇_Sq|²`, on a

\[
\begin{aligned}
D_e(s)
&=\int_{S^2}
\Phi e\cdot\nabla_{S^2}q\,dS
+\int_{S^2}
\Phi(\xi-e)\cdot\nabla_{S^2}q\,dS\\
&\geq
m\int_{S^2}|\nabla_{S^2}q|^2dS
-M\delta(s)
\int_{S^2}|\nabla_{S^2}q|dS\\
&\geq
\frac{8\pi m}{3}
-\pi^2M\delta(s).
\end{aligned}
\tag{24}
\]

On obtient le théorème conditionnel suivant.

### Théorème 5.1 — profondeur maximale d’une rectification `O(1/s)`

Supposons que (3) soit satisfaite sur `[s_a,S]×S²`, que

\[
0<m\leq\Phi\leq M,
\qquad
\delta(s)\leq\frac Cs,
\tag{25}
\]

et posons

\[
s_0=\max\left\{
s_a,\frac{3\pi MC}{4m}
\right\}.
\tag{26}
\]

Alors

\[
S-s_0\leq\frac{3M}{m}.
\tag{27}
\]

En effet, pour `s≥s_0`, (24) donne

\[
D_e(s)\geq\frac{4\pi m}{3}.
\tag{28}
\]

L’insertion de cette constante dans (22) donne (27).

Si `S=+∞`, la contradiction est immédiate. En variables radiales, un intervalle de longueur `L` en `s` correspond au rapport d’échelles

\[
\frac{r_{\mathrm{extérieur}}}
{r_{\mathrm{intérieur}}}=e^L.
\tag{29}
\]

Une fois le seuil de rectification atteint, le profil ne peut donc traverser un rapport supérieur à

\[
\exp(3M/m)
\tag{30}
\]

sans violer la contrainte solénoïdale ou l’une des hypothèses (25).

### Version en convergence moyenne

La norme uniforme n’est pas essentielle. La même preuve donne

\[
D_e(s)
\geq\frac{8\pi m}{3}
-M\int_{S^2}
|\xi-e||\nabla_{S^2}q|\,dS.
\tag{31}
\]

Une convergence de `ξ` vers `e` dans `L¹(S²)`, ou presque partout avec `|ξ|=1`, suffit donc par convergence dominée. En revanche, une convergence seulement le long d’une suite de valeurs de `s` ne donne aucun intervalle sur lequel appliquer le budget.

## 6. Compatibilité avec le faible-`L^{3/2}`

Sur `B_{R_*}`, la borne `Φ≤M` implique

\[
|W(x)|\leq Mr^{-2}.
\]

Pour la quasi-norme

\[
\|f\|_{L^{3/2,\infty}}
=\sup_{\lambda>0}
\lambda|\{|f|>\lambda\}|^{2/3},
\]

on en déduit

\[
\|W\mathbf1_{B_{R_*}}\|_{L^{3/2,\infty}}
\leq
\left(\frac{4\pi}{3}\right)^{2/3}M.
\tag{32}
\]

Si `Φ≥m`, l’inégalité inverse sûre est

\[
\|W\mathbf1_{B_{R_*}}\|_{L^{3/2,\infty}}
\geq
\left(\frac{4\pi}{3}\right)^{2/3}m.
\tag{33}
\]

Le profil non dégénéré du théorème 5.1 est donc parfaitement compatible avec l’échelle faible critique. C’est la combinaison de cette non-dégénérescence avec la rectification vers une direction fixe qui est impossible, pas la norme faible elle-même.

Réciproquement, une borne globale faible-`L^{3/2}` ne fournit ni `Φ≤M` sur chaque sphère logarithmique, ni `Φ≥m`. Elle contrôle une distribution tridimensionnelle, pas les traces uniformes en `s` nécessaires à (19) et (24).

## 7. Bornes de dérivées et oscillations rapides

### 7.1 Ne pas dériver un symbole `O(1/s)`

L’estimation

\[
\xi(s,\theta)=e+O(1/s)
\]

n’implique pas

\[
\partial_s\xi=O(1/s^2).
\]

Avec `a⊥e`, le champ unitaire

\[
\xi_{\mathrm{test}}(s)
=\frac{e+s^{-1}\sin(s^3)a}
{|e+s^{-1}\sin(s^3)a|}
\tag{34}
\]

vérifie la première estimation, tandis que sa dérivée contient un terme d’ordre `s cos(s³)`. Ce champ test n’est pas présenté comme solénoïdal; il réfute seulement toute différentiation automatique de l’asymptotique.

La preuve du théorème 5.1 évite ce piège : elle différentie le moment `B_e` par l’équation (3), jamais la factorisation `Φξ` terme à terme.

### 7.2 Les oscillations rapides n’aident pas sous proximité uniforme

La borne (24) est ponctuelle en `s` et ne contient aucune dérivée de `ξ`. Une oscillation de fréquence arbitraire à l’intérieur de la boule `|ξ-e|≤C/s` laisse `D_e` positif après `s_0`. Elle ne peut donc recharger le budget borné `B_e`.

### 7.3 Les excursions loin de `e` doivent occuper une proportion positive

Fixons `δ_0` tel que

\[
c:=\frac{8\pi m}{3}-\pi^2M\delta_0>0.
\tag{35}
\]

Sur l’ensemble « bon »

\[
G=\{s:\|\xi(s)-e\|_\infty\leq\delta_0\},
\]

on a `D_e≥c`. Sur son complément `A`, la borne générale

\[
|D_e(s)|
\leq M\int_{S^2}|\nabla_{S^2}q|dS
=\pi^2M
\tag{36}
\]

donne `D_e≥-π²M`. Sur tout intervalle `I` de longueur `L`, (20) implique

\[
|A\cap I|
\geq
\frac{cL-4\pi M}{c+\pi^2M}.
\tag{37}
\]

Ainsi

\[
\liminf_{L\to\infty}
\frac{|A\cap I_L|}{L}
\geq
\frac{c}{c+\pi^2M}
\tag{38}
\]

pour toute suite d’intervalles croissants partant d’un même point. Des « impulsions de dérectification » de mesure logarithmique négligeable ne peuvent pas compenser une rectification persistante sous les bornes `m,M`.

## 8. Contre-exemples lorsque les hypothèses sont affaiblies

### 8.1 Perte de la borne inférieure

Le profil (9) satisfait exactement

\[
\xi=e,
\qquad
\Phi=e^{-2s},
\qquad
\partial_s\Phi=-2\Phi,
\qquad
W=R_*^{-2}e.
\]

Il est lisse, divergence-free, borné et appartient localement à faible-`L^{3/2}`. Il vérifie même l’estimation supérieure `O(r^{-2})`. Il échappe au théorème uniquement parce que `inf_θΦ(s,θ)→0`.

**Conclusion :** remplacer « profil critique non dégénéré » par la seule majoration `|W|≤Cr^{-2}` rend l’exclusion fausse.

### 8.2 Oscillation log-radiale arbitraire dans le secteur tangent

Soit `a(s)` un vecteur quelconque de classe `C¹` et posons

\[
\Omega(s,\theta)=a(s)\times\theta.
\tag{39}
\]

Ce champ est tangent, donc `Ω_r=0`, et c’est un champ de Killing de divergence sphérique nulle pour chaque `s` :

\[
\operatorname{div}_{S^2}\Omega_T=0.
\]

La contrainte (3) est satisfaite pour **toute** dépendance de `a(s)`, même très rapide. Si `a` est borné, le profil est uniformément faible-`L^{3/2}` et son flux est nul. En choisissant

\[
a(s)=(\cos s^3,\sin s^3,0),
\]

on obtient une oscillation radiale accélérée que la norme critique et la divergence ne détectent pas. La direction n’approche toutefois aucun `e` fixe, et la magnitude s’annule aux deux pôles parallèles à `a(s)`.

**Conclusion :** la solénoïdalité et faible-`L^{3/2}` n’imposent aucun contrôle de fréquence en `s`; la rectification fixe et la non-dégénérescence font le travail dans le théorème 5.1.

### 8.3 Concentration sur des coquilles minces

La norme faible ne fournit pas de borne de trace uniforme. Prenons un champ tangent divergence-free `T(θ)` avec `|T|≤1`, et sur une coquille

\[
r_0e^{-w}<r<r_0
\]

posons

\[
W_{A,w}=Ar^{-2}T(\theta),
\tag{40}
\]

avec une coupure radiale lisse. Comme `T_r=0`, la coupure conserve la divergence. Un calcul direct de fonction de distribution donne la borne

\[
\|W_{A,w}\|_{L^{3/2,\infty}}
\leq
\left(\frac{4\pi}{3}\right)^{2/3}
A(1-e^{-3w})^{2/3}.
\tag{41}
\]

Pour `w=A^{-3/2}` et `A→∞`, le membre de droite reste borné, alors que l’amplitude sur la coquille tend vers l’infini. Des coquilles disjointes et suffisamment séparées peuvent reproduire ce mécanisme à plusieurs échelles.

**Conclusion :** une borne faible critique ne peut pas remplacer la borne de tranche `Φ≤M`; une borne uniforme de dérivée en `s` exclurait précisément ces transitions de plus en plus étroites.

### 8.4 Convergence le long d’une suite

Si `ξ(s_n)→e` pour une suite `s_n→∞`, mais que les voisinages de ces points ont une longueur totale finie, le budget (20) ne donne aucune contradiction. Le quantificateur nécessaire est une proximité sur une demi-droite, ou au moins sur un ensemble de densité logarithmique assez grande pour contredire (37).

**Conclusion :** « il existe une suite d’échelles rectifiées » et « toutes les petites échelles sont rectifiées » ne sont pas interchangeables.

## 9. Passe contradictoire ciblée

### Attaque A — signe radial

Le changement de variable `s=log(R_*/r)` porte `∂rs=-1/r`. Le champ constant construit en (9) certifie le signe négatif de (2).

**État :** signe vérifié; toute formule avec un signe positif doit utiliser la convention opposée `s=log(r/R_0)`.

### Attaque B — usage silencieux de `Φ≥m`

La définition scalaire primaire parle d’un ordre `O(r^{-2})` et d’un facteur borné; elle ne fournit pas automatiquement une borne inférieure uniforme. Le contre-exemple (9) satisfait toutes les bornes supérieures.

**État :** le théorème 5.1 est conditionnel à une non-dégénérescence explicitement ajoutée.

### Attaque C — faible-`L^{3/2}` comme contrôle de tranche

La construction (40)–(41) autorise des amplitudes de tranche arbitraires sur des coquilles logarithmiques minces.

**État :** une norme de Lorentz tridimensionnelle ne remplace pas `M` dans le budget.

### Attaque D — dérivée du reste directionnel

Le test (34) montre que `O(1/s)` n’est pas stable par dérivation.

**État :** toute preuve développant `∂s(Φξ)` doit imposer séparément une borne sur `∂sξ`; la preuve par moment n’en a pas besoin.

### Attaque E — oscillations rapides comme mécanisme de compensation

Sous (4), les oscillations rapides restent dans une région où `D_e≥c`; elles ne changent donc pas le signe du budget. Si la direction quitte cette région, (37) force ces excursions à avoir une densité logarithmique positive.

**État :** les impulsions rares sont exclues; les oscillations de densité positive restent possibles mais violent la rectification uniforme.

### Attaque F — confusion cinématique/dynamique

Le lemme utilise seulement `div curl=0`. Il ne vérifie ni la vorticité NSE, ni Biot–Savart, ni l’énergie locale, ni la pression.

**État :** résultat cinématique nécessaire, pas exclusion d’un blow-up Navier–Stokes général.

## 10. Lemme minimal transférable

Le noyau à transférer au graphe de preuve est l’identité suivante.

> **Budget de rectification.** Pour tout profil borné `W=r^{-2}Ω(log(R_*/r),θ)` divergence-free sur le domaine ponctué et tout `e∈S²`, le moment `B_e=∫Ω_r(e·θ)` satisfait `B_e'=-∫Ω·∇_S(e·θ)`. Par conséquent, la partie positive non intégrable de ce dernier intégrand est impossible. Si `m≤|Ω|≤M` et `Ω/|Ω|→e` uniformément, l’intégrand est finalement minoré par une constante positive; le profil ne peut donc atteindre `r=0`.

Ce lemme exclut une classe substantielle mais très spécifique : les cœurs critiques non dégénérés dont la direction se rectifie vers **un vecteur spatial fixe sur toute la sphère**. Il n’exclut pas :

- une direction limite dépendant de `θ`;
- des zéros ou une amplitude qui décroît avec `s`;
- une rectification seulement locale sur un sous-ensemble angulaire;
- des excursions de direction de densité logarithmique positive;
- un profil sans représentation log-radiale uniforme;
- les scénarios Type II généraux.

## 11. Prochain test décisif

Pour un profil candidat numérique ou analytique, calculer avec erreurs contrôlées

\[
B_e(s),
\qquad
D_e(s),
\qquad
R_{\mathrm{div}}(s,\theta)
=\operatorname{div}_{S^2}\Omega_T-\partial_s\Omega_r.
\]

Le test falsifiable est triple :

1. vérifier que `R_div` tend vers zéro dans une norme déclarée;
2. vérifier l’identité résiduelle `B_e'+D_e=0` avec la même discrétisation;
3. si `D_e≥c>0` est observé, vérifier que la longueur logarithmique disponible respecte `L≤4πM/c`.

Une violation persistante de cette dernière borne signale nécessairement au moins une des quatre défaillances suivantes : résidu de divergence non contrôlé, amplitude non uniformément bornée, direction non uniformément rectifiée, ou erreur numérique dans le premier harmonique.

## 12. Statut de preuve

Toutes les identités et inégalités nouvelles de ce rapport sont des dérivations IA internes. Elles n’ont reçu ni revue par les pairs, ni formalisation, ni validation par une famille de modèle indépendante. Elles ne doivent recevoir aucun statut `PAPER_PROOF`.
