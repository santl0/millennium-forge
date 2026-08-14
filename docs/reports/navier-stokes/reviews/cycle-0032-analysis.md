# Cycle 0032 — deux couches décalées : variation totale, fonctions de distribution et masquage directionnel

Date : 2026-08-14  
Statut : dérivation analytique interne et calcul flottant adverse, non revus par les pairs, **pas** `PAPER_PROOF`  
Verrou : `GAP-NONSEPARABLE-COMPACT-CURL-FLATNESS`

## Décision du cycle

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Effet de levier | Total |
|---|---:|---:|---:|---:|---:|
| Minorer le curl du champ **total** par variation des fibres d'un superniveau presque optimal faible-`L³` | 4 | 5 | 5 | 5 | **19** |
| Additionner les coûts Lorentz des deux couches avant annulation | 3 | 4 | 5 | 3 | 15 |
| Optimiser numériquement les décalages et les signes sans lemme préalable | 3 | 4 | 4 | 3 | 14 |

La première action est retenue. La seconde est explicitement attaquée : une paire de translations de coefficients opposés fournit un contre-exemple à tout ledger couche par couche dépourvu de conditionnement. Le résultat robuste doit dépendre de la fonction de distribution et de la variation totale de la somme réelle `F`.

## 1. Cadre exact

On travaille à temps fixé dans `R³`, en coordonnées cylindriques `(r,θ,z)`. Fixons `R>0` et

\[
 \psi(r,z)=\frac RrF(r,z),
 \qquad
 U=\psi e_\theta,
\tag{1}
\]

où `F∈C_c^∞((0,∞)×R)` est réelle. On suppose

\[
 \operatorname{supp}F
 \subset I_r\times I_z
 \subset[c_-R,c_+R]\times\mathbb R,
 \qquad 0<c_-<c_+<\infty,
\tag{2}
\]

et on note

\[
 A=|I_r|,
 \qquad B=|I_z|.
\tag{3}
\]

Le support est donc séparé de l'axe. Le champ `U` est lisse, compact et exactement divergence-free. Son rotationnel est

\[
 W=\nabla\times U
 =-\frac Rr\partial_zF\,e_r
  +\frac Rr\partial_rF\,e_z.
\tag{4}
\]

En particulier,

\[
 |W|=\frac Rr|\nabla_{r,z}F|.
\tag{5}
\]

Le facteur `R/r` annule exactement le terme cylindrique dans `W_z`; aucune approximation `r≈R` n'est utilisée dans (4)–(5).

Posons

\[
 K_u=\|U\|_{L^{3,\infty}(\mathbb R^3)},
 \qquad
 K_\omega=\|W\|_{L^{3/2,\infty}(\mathbb R^3)},
\tag{6}
\]

avec

\[
 \|f\|_{L^{p,\infty}}
 =\sup_{\lambda>0}\lambda
   |\{|f|>\lambda\}|^{1/p}.
\tag{7}
\]

L'inégalité de Lorentz élémentaire utilisée ci-dessous est

\[
 \int_\Omega|f|\,dx
 \leq\frac p{p-1}
 \|f\|_{L^{p,\infty}}|\Omega|^{1-1/p}.
\tag{8}
\]

Pour `p=3/2`, la constante vaut exactement `3` avec la convention (7).

Ce cadre décrit une donnée initiale cinématique admissible pour Navier–Stokes incompressible non forcé sur `R³`. Aucun résultat d'évolution, de pression ou de blow-up n'est affirmé.

## 2. Annulation ponctuelle versus fonction de distribution

Pour une somme de deux produits décalés,

\[
 F(r,z)=\sum_{j=1}^2
 V_j\,
 \eta_j\!\left(\frac{r-R-s_j}{a_j}\right)
 \chi_j\!\left(\frac{z-t_j}{b_j}\right),
\tag{9}
\]

les dérivées réelles sont

\[
 \partial_rF
 =\sum_{j=1}^2\frac{V_j}{a_j}\eta_j'\chi_j,
 \qquad
 \partial_zF
 =\sum_{j=1}^2\frac{V_j}{b_j}\eta_j\chi_j'.
\tag{10}
\]

Il existe deux mécanismes distincts.

1. Les deux termes d'une **même** somme dans (10) peuvent s'annuler ponctuellement avant la valeur absolue. Une minoration obtenue en additionnant les variations ou les quasi-normes des couches séparées est donc fausse sans hypothèse de signe, de séparation des supports ou de conditionnement.
2. Les deux dérivées de la somme totale ne s'annulent pas entre elles dans le module du curl :
   \[
   |W|^2=(R/r)^2\bigl(|\partial_rF|^2+|\partial_zF|^2\bigr).
   \tag{11}
   \]
   Ajouter `∂rF` pour « masquer » directionnellement `∂zF` tourne la direction vers `e_z`, mais augmente le module ponctuel.

La quasi-norme faible n'est ni additive ni déterminée par une intégrale de couche. Elle dépend des superniveaux du **module après toutes les annulations**. Le ledger correct doit donc partir d'un superniveau de `U` et appliquer (8) au champ total `W`.

## 3. Lemme de variation totale sur un superniveau actif

Pour `λ>0`, définissons dans le demi-plan méridien

\[
 E_\lambda
 =\left\{(r,z):\frac Rr|F(r,z)|>\lambda\right\}.
\tag{12}
\]

Notons

\[
 S_\lambda=|E_\lambda|,
 \quad
 \ell_\lambda=|\operatorname{proj}_rE_\lambda|,
 \quad
 h_\lambda=|\operatorname{proj}_zE_\lambda|.
\tag{13}
\]

On a toujours `S_λ≤ℓ_λh_λ`.

### 3.1 Budget de variation exact

Pour chaque `r∈proj_r E_λ`, il existe un `z` tel que

\[
 |F(r,z)|>\frac rR\lambda\geq c_-\lambda.
\]

Comme `F(r,·)` est compacte dans `I_z`, elle doit partir de zéro et revenir à zéro. Par conséquent,

\[
 \int_{I_z}|\partial_zF(r,z)|\,dz
 \geq2c_-\lambda.
\tag{14}
\]

De même, sur chaque fibre radiale active,

\[
 \int_{I_r}|\partial_rF(r,z)|\,dr
 \geq2c_-\lambda
 \quad
 \text{pour }z\in\operatorname{proj}_zE_\lambda.
\tag{15}
\]

Après intégration,

\[
 \int_{\operatorname{proj}_rE_\lambda\times I_z}
 |\partial_zF|\,dr\,dz
 \geq2c_-\lambda\ell_\lambda,
\tag{16}
\]

\[
 \int_{I_r\times\operatorname{proj}_zE_\lambda}
 |\partial_rF|\,dr\,dz
 \geq2c_-\lambda h_\lambda.
\tag{17}
\]

Ces deux bornes portent sur la somme `F`; elles survivent à toutes les annulations internes des deux couches. Elles ne minorent pas séparément la variation de chaque produit.

### 3.2 Paramètre de masquage directionnel

La composante gênante pour un alignement sur l'axe fixe `e_z` est

\[
 \frac{|W_r|}{|W|}
 =\frac{|\partial_zF|}{|\nabla F|}.
\tag{18}
\]

Pour `0<δ≤1`, posons

\[
 \mathcal M_\delta
 =\{(r,z):|\partial_zF|\leq\delta|\nabla F|\}.
\tag{19}
\]

Le paramètre `δ` est l'ouverture du double cône autour de `±e_z`. Afin de permettre un masquage imparfait, supposons qu'une fraction `0<β≤1` de la variation verticale active est masquée :

\[
 \int_{\mathcal M_\delta\cap
   (\operatorname{proj}_rE_\lambda\times I_z)}
 |\partial_zF|\,dr\,dz
 \geq
 \beta
 \int_{\operatorname{proj}_rE_\lambda\times I_z}
 |\partial_zF|\,dr\,dz.
\tag{20}
\]

Si (20) échoue, au moins une fraction `1-β` de la variation verticale porte déjà une composante directionnelle radiale supérieure à `δ`; elle n'est donc pas masquée.

### Lemme 3.1 — ledger variation totale/Lorentz

Sous (1)–(20),

\[
 \boxed{
 K_\omega^3
 \geq C_0\lambda^3R^2
 \max\!\left\{
   \frac{\beta^3\ell_\lambda^2}{\delta^3B},
   \frac{h_\lambda^2}{A}
 \right\},}
\tag{21}
\]

où

\[
 C_0=\frac{32\pi^2c_-^3}{27c_+}.
\tag{22}
\]

Si `λ` est `ε`-presque optimal pour la quasi-norme de `U`, c'est-à-dire

\[
 \lambda^3
 |\{x\in\mathbb R^3:|U(x)|>\lambda\}|
 \geq(1-\varepsilon)K_u^3,
 \qquad 0<\varepsilon<1,
\tag{23}
\]

alors

\[
 \boxed{
 \left(\frac{K_\omega}{K_u}\right)^3
 \geq C_1(1-\varepsilon)R
 \max\!\left\{
   \frac{\beta^3\ell_\lambda^2}{\delta^3BS_\lambda},
   \frac{h_\lambda^2}{AS_\lambda}
 \right\},}
\tag{24}
\]

avec

\[
 C_1=\frac{16\pi c_-^3}{27c_+^2}.
\tag{25}
\]

En utilisant seulement `S_λ≤ℓ_λh_λ`, on obtient la version plus géométrique

\[
 \boxed{
 \left(\frac{K_\omega}{K_u}\right)^3
 \geq C_1(1-\varepsilon)R
 \max\!\left\{
   \frac{\beta^3\ell_\lambda}{\delta^3Bh_\lambda},
   \frac{h_\lambda}{A\ell_\lambda}
 \right\}.}
\tag{26}
\]

### Preuve

Relevons `proj_r E_λ×I_z` par rotation autour de l'axe et appelons ce volume `Ω_z`. Par (2),

\[
 |\Omega_z|
 \leq2\pi c_+R\ell_\lambda B.
\tag{27}
\]

L'élément de volume vaut `r dr dθ dz`; (5), (16), (19) et (20) donnent exactement

\[
\begin{aligned}
 \int_{\Omega_z}|W|\,dx
 &=2\pi R
   \int_{\operatorname{proj}_rE_\lambda\times I_z}
   |\nabla F|\,dr\,dz\\
 &\geq
 \frac{2\pi R}{\delta}
 \int_{\mathcal M_\delta
  \cap(\operatorname{proj}_rE_\lambda\times I_z)}
 |\partial_zF|\,dr\,dz\\
 &\geq\frac{4\pi c_-\beta}{\delta}
 R\lambda\ell_\lambda.
\end{aligned}
\tag{28}
\]

L'inégalité (8) donne

\[
 3K_\omega|\Omega_z|^{1/3}
 \geq\int_{\Omega_z}|W|\,dx.
\tag{29}
\]

Le cube de (28)–(29), puis (27), fournit le premier terme de (21). Le même calcul sur le relevé de `I_r×proj_z E_λ`, avec (17) et sans facteur de masquage, fournit le second.

Enfin,

\[
 |\{|U|>\lambda\}|
 =2\pi\int_{E_\lambda}r\,dr\,dz
 \leq2\pi c_+RS_\lambda.
\tag{30}
\]

Les équations (21), (23) et (30) donnent (24); (26) suit de `S_λ≤ℓ_λh_λ`. `□`

## 4. Spécialisation à deux couches de géométrie non dégénérée

Le lemme précédent n'exige pas la représentation (9). Pour retrouver les proxies du produit séparé, il faut seulement que le **superniveau de la somme** ait encore la géométrie de la cellule annoncée.

Supposons qu'à un niveau satisfaisant (23), il existe des échelles `a,b` et des constantes fixes positives telles que

\[
 A\leq C_Aa,
 \quad B\leq C_Bb,
 \quad \ell_\lambda\geq c_aa,
 \quad h_\lambda\geq c_bb.
\tag{31}
\]

Alors (26) implique

\[
 \boxed{
 \left(\frac{K_\omega}{K_u}\right)^3
 \geq c(1-\varepsilon)
 \max\!\left\{
   \frac{\beta^3}{\delta^3}\frac{Ra}{b^2},
   \frac{Rb}{a^2}
 \right\},}
\tag{32}
\]

où `c>0` dépend seulement de `c_±,C_A,C_B,c_a,c_b`. Les puissances `Ra/b²` et `Rb/a²` sont donc retrouvées sans additionner les coûts des couches.

### Corollaire 4.1 — impossibilité d'un masquage arbitrairement fin

Supposons en outre

\[
 a\leq c_0R,
 \qquad K_u\geq\kappa>0,
 \qquad K_\omega\leq K<\infty,
 \qquad \beta\geq\beta_0>0.
\tag{33}
\]

La version de (32) sans masquage, obtenue en prenant `δ=β=1`, et son second terme imposent les deux contraintes d'aspect usuelles. En posant `x=a/R`, `y=b/R` et `G=C(K/κ)^3`, elles donnent notamment

\[
 y\leq Gx^2.
\tag{34}
\]

Par suite,

\[
 \frac{x}{y^2}
 \geq\frac{1}{G^2x^3}
 \geq\frac{1}{G^2c_0^3}.
\tag{35}
\]

Le premier terme masqué de (32) donne alors

\[
 \boxed{
 \delta
 \geq c_*\frac{\beta_0}{c_0}
 \left(\frac\kappa K\right)^3,}
\tag{36}
\]

avec `c_*>0` dépendant uniquement des constantes géométriques et des profils. Ainsi, dans une classe à géométrie effective uniforme, deux transitions décalées ne peuvent rendre la direction arbitrairement proche de l'axe fixe tout en conservant `K_u` non petit et `K_ω` borné.

La puissance cubique de `κ/K` dans (36) provient de trois usages réels : le coût faible-`L^{3/2}`, la contrainte d'aspect transverse et la borne `a/R≤c₀`. Elle ne doit pas être remplacée par une puissance linéaire sans hypothèse supplémentaire.

## 5. Contre-exemple au ledger couche par couche

La condition (31) porte sur le champ total. Elle ne découle pas automatiquement de profils individuels non dégénérés. Même deux copies d'un profil fixe peuvent être arbitrairement mal conditionnées.

Soient `η,χ∈C_c^∞(R)` non nulles, `σ,τ` deux constantes non simultanément nulles et `ε>0`. Posons, avec `s=(r-R)/a` et `t=z/b`,

\[
 F_\varepsilon(r,z)
 =\frac{V}{\varepsilon}
 \left[
   \eta(s)\chi(t)
   -\eta(s-\varepsilon\sigma)
    \chi(t-\varepsilon\tau)
 \right].
\tag{37}
\]

C'est exactement une somme de deux produits dont les transitions radiales et axiales sont décalées, avec coefficients `±V/ε`. Taylor donne, dans toute norme `C^m` autorisée par la régularité des profils,

\[
 F_\varepsilon
 \longrightarrow
 F_0
 =V\bigl(\sigma\eta'\chi+\tau\eta\chi'\bigr),
\tag{38}
\]

\[
 \partial_rF_\varepsilon
 \longrightarrow
 \frac Va
 \bigl(\sigma\eta''\chi+\tau\eta'\chi'\bigr),
\tag{39}
\]

\[
 \partial_zF_\varepsilon
 \longrightarrow
 \frac Vb
 \bigl(\sigma\eta'\chi'+\tau\eta\chi''\bigr).
\tag{40}
\]

Les supports restent dans un compact fixe. Par conséquent,

\[
 \sup_{0<\varepsilon<\varepsilon_0}
 \left(
   \|U_\varepsilon\|_{L^{3,\infty}}
   +\|\nabla\times U_\varepsilon\|_{L^{3/2,\infty}}
 \right)<\infty,
\tag{41}
\]

et, si `F₀≠0`,

\[
 \liminf_{\varepsilon\downarrow0}
 \|U_\varepsilon\|_{L^{3,\infty}}>0.
\tag{42}
\]

En revanche, la quasi-norme de chaque couche prise isolément est de taille `ε⁻¹`; son cube diverge comme `ε⁻³`. L'annulation est ponctuelle, avant la construction des fonctions de distribution du champ total.

Ce contre-exemple réfute toute affirmation de la forme

\[
 \|\nabla\times U_1\|_{L^{3/2,\infty}}
 +\|\nabla\times U_2\|_{L^{3/2,\infty}}
 \leq C\|\nabla\times(U_1+U_2)\|_{L^{3/2,\infty}}
\tag{43}
\]

avec `C` indépendant des décalages et des coefficients. Il ne réfute pas le lemme 3.1 : celui-ci mesure `F_ε`, ses superniveaux et sa variation **après** annulation.

Trois hypothèses alternatives rendent un ledger de couches possible :

- supports des dérivées correspondantes disjoints à une échelle uniforme ;
- signes compatibles sur une zone de transition quantitativement large ;
- nombre de conditionnement borné, par exemple `Σ|V_j|≤C V_eff` pour une amplitude effective précisément définie.

Sans l'une de ces hypothèses, les amplitudes `V_j` n'ont aucune signification coercive.

## 6. Test numérique adverse des fonctions de distribution

Le test suivant utilise

\[
 q(s)=
 \begin{cases}
 e^{-1/(1-s^2)},&|s|<1,\\
 0,&|s|\geq1,
 \end{cases}
\tag{44}
\]

dans (37), avec `R=4`, `a=b=1`, `σ=0.6`, `τ=0.8`. Le domaine méridien `[-1.55,1.55]²` est discrétisé par `500×500` points milieux. Les poids tridimensionnels sont `2πr Δr Δz`. Pour chaque champ discrétisé, la quasi-norme faible est calculée en triant les modules décroissants puis en maximisant `v_k(Σ_{j≤k}w_j)^{1/p}`.

Commande reproductible :

```powershell
@'
import numpy as np, math
R=4.; a=b=1.; N=500; span=3.1
s=np.linspace(-span/2,span/2,N,endpoint=False)+span/(2*N)
ds=span/N
S,T=np.meshgrid(s,s,indexing='ij'); r=R+S

def bump(x):
    y=np.zeros_like(x); m=np.abs(x)<1
    y[m]=np.exp(-1/(1-x[m]**2)); return y
def dbump(x):
    y=np.zeros_like(x); m=np.abs(x)<1; q=x[m]
    y[m]=-2*q*np.exp(-1/(1-q*q))/(1-q*q)**2; return y
def weak(vals,weights,p):
    v=vals.ravel(); w=weights.ravel()
    o=np.argsort(v)[::-1]
    return np.max(v[o]*np.cumsum(w[o])**(1/p))

weights=2*math.pi*r*ds*ds
eta,etap,chi,chip=bump(S),dbump(S),bump(T),dbump(T)
for eps in [.4,.2,.1,.05,.025]:
    se,te=S-eps*.6,T-eps*.8
    eta2,etap2=bump(se),dbump(se)
    chi2,chip2=bump(te),dbump(te)
    F=(eta*chi-eta2*chi2)/eps
    Fr=(etap*chi-etap2*chi2)/eps
    Fz=(eta*chip-eta2*chip2)/eps
    fac=R/r
    Ku=weak(abs(fac*F),weights,3)
    Kw=weak(abs(fac)*np.sqrt(Fr*Fr+Fz*Fz),weights,1.5)
    Kw1=weak(abs(fac)*np.sqrt((etap*chi/eps)**2+
                             (eta*chip/eps)**2),weights,1.5)
    print(f'{eps:.3f} {Ku:.6f} {Kw:.6f} {eps*Kw1:.6f}')
'@ | python -
```

Sortie obtenue :

```text
0.400 0.393224 4.912554 2.031306
0.200 0.426286 4.959503 2.031306
0.100 0.439285 4.880234 2.031306
0.050 0.443172 4.849433 2.031306
0.025 0.444658 4.865859 2.031306
```

À `ε=0.025`, le triplet `(K_u,K_ω,εK_{ω,1})` vaut respectivement

```text
N=250   0.44460428  4.88564782  2.03443025
N=500   0.44465756  4.86585872  2.03130589
N=1000  0.44450518  4.85616585  2.03039029
```

Entre `N=500` et `N=1000`, les écarts relatifs sont environ `0.034 %`, `0.200 %` et `0.045 %`. Le test confirme que la norme de chaque couche croît comme `ε⁻¹`, tandis que les deux normes du champ total restent non dégénérée et bornée. Il s'agit d'un calcul flottant de découverte, non d'une borne d'erreur certifiée.

## 7. Échelle

Sous le scaling de Navier–Stokes

\[
 U_\mu(x)=\mu U(\mu x),
 \qquad W_\mu(x)=\mu^2W(\mu x),
\tag{45}
\]

on peut prendre

\[
 R_\mu=R/\mu,
 \quad F_\mu(r,z)=\mu F(\mu r,\mu z),
 \quad A_\mu=A/\mu,
 \quad B_\mu=B/\mu.
\tag{46}
\]

Les normes `K_u,K_ω`, le rapport `K_ω/K_u`, `δ`, `β` et les facteurs

\[
 \frac{R\ell}{Bh},
 \qquad
 \frac{Rh}{A\ell}
\tag{47}
\]

sont invariants. Les lemmes (21), (24), (26), (32) et (36) ont donc l'échelle critique exacte. Le paramètre `ε` du contre-exemple (37) est un décalage relatif sans dimension, et non le paramètre de scaling `μ`.

## 8. Passe contradictoire

1. **Addition des quasi-normes des couches.** Réfutée par (37)–(43).
2. **Annulation entre `∂rF` et `∂zF`.** Impossible dans `|W|`; les composantes sont orthogonales. Le « masquage » est une rotation payante, quantifiée par `δ⁻³`.
3. **Variation totale des couches.** Non coercive sans conditionnement. Seule la variation de la somme réelle intervient dans (14)–(17).
4. **Supremum faible non atteint.** Le paramètre `ε` de (23) évite de supposer l'existence d'un niveau maximisant exactement la quasi-norme.
5. **Superniveau filamentaire.** Conservé dans (24) via `S_λ,ℓ_λ,h_λ`. Le passage à (32) exige explicitement la géométrie non dégénérée (31).
6. **Masquage partiel.** Le facteur `β` empêche de déclarer masquée une grande mesure spatiale portant une variation négligeable. Si `β→0`, une part macroscopique de la variation reste hors du cône.
7. **Profils variables.** (21)–(26) ne dépendent d'aucun profil. En revanche, (31) et donc (32)–(36) doivent être revérifiées si les profils, coefficients ou décalages varient.
8. **Support touchant l'axe.** Exclu par `c_->0`; sinon le facteur `R/r`, la régularité et les constantes de volume changent.
9. **Fonction de distribution.** L'expérience trie le module du champ total après annulation. Elle ne certifie toutefois pas le continuum ni le supremum entre deux niveaux de grille.
10. **Direction BMO.** Un budget de variation directionnelle n'est pas encore une minoration d'oscillation moyenne sur une boule. Il manque une localisation spatiale de la variation non masquée ou de la zone où (19) tient.
11. **Dynamique et pression.** Aucun temps, terme visqueux, étirement, pression ou passage à un profil de blow-up n'est présent.

## 9. Contre-revue distincte : lemme universel de support méridien mince

Cette section audite un argument plus fort que le ledger de superniveaux. On spécialise (2) à

\[
 \operatorname{supp}F
 \subset\{(r,z):R/2<r<3R/2\}
\]

et on pose

\[
 S_2=|\operatorname{supp}F|_{dr\,dz}.
\tag{48}
\]

### 9.1 Potentiel de Riesz bidimensionnel

Pour `F∈C_c^∞(R²)`, la représentation par le noyau fondamental du Laplacien donne

\[
 |F(x)|
 \leq C_{\rm rep}
 \int_{\mathbb R^2}\frac{|\nabla F(y)|}{|x-y|}\,dy
 =C_{\rm rep}I_1(|\nabla F|)(x).
\tag{49}
\]

L'application faible–faible requise est

\[
 \boxed{
 \|I_1g\|_{L^{6,\infty}(\mathbb R^2)}
 \leq C_{\rm HLS}
 \|g\|_{L^{3/2,\infty}(\mathbb R^2)}.}
\tag{50}
\]

Les exposants sont corrects :

\[
 \frac16=\frac{2}{3}-\frac12.
\]

Le noyau `|x|⁻¹` appartient à `L^{2,∞}(R²)` et

\[
 \frac1{3/2}+\frac12=1+\frac16,
\tag{51}
\]

ce qui est exactement la relation de convolution de Lorentz d'O'Neil. La cible faible–faible est valide. Pour éviter toute ambiguïté entre les formulations du théorème d'O'Neil qui autorisent ou non explicitement des indices secondaires tous égaux à `∞`, on peut la certifier sans endpoint délicat par interpolation réelle :

\[
 I_1:L^{4/3}\to L^4,
 \qquad
 I_1:L^{12/7}\to L^{12}
\tag{52}
\]

sont deux cas forts de Hardy–Littlewood–Sobolev. À paramètre `θ=1/2`,

\[
 (L^{4/3},L^{12/7})_{1/2,\infty}
 =L^{3/2,\infty},
 \qquad
 (L^4,L^{12})_{1/2,\infty}
 =L^{6,\infty},
\tag{53}
\]

ce qui prouve (50). Il ne faut pas remplacer cette étape par un Hölder-Lorentz ponctuel naïf : le produit des réarrangements du noyau et d'une donnée faible critique peut ne pas être intégrable à l'origine, même si la sortie appartient bien à faible-`L⁶`.

La référence primaire pour la convolution de Lorentz est Richard O'Neil, *Convolution operators and L(p,q) spaces*, Duke Math. J. 30 (1963), 129–142, DOI [`10.1215/S0012-7094-63-03015-1`](https://doi.org/10.1215/S0012-7094-63-03015-1). L'interpolation (52)–(53) fournit ici une vérification indépendante de la convention précise retenue dans cette source.

### 9.2 Restriction de support : sens de l'inclusion faible

Si une fonction `f` est supportée sur un ensemble de mesure au plus `S₂`, alors

\[
\begin{aligned}
 \|f\|_{L^{3,\infty}}
 &=\sup_{t>0}t|\{|f|>t\}|^{1/3}\\
 &\leq S_2^{1/6}
 \sup_{t>0}t|\{|f|>t\}|^{1/6}\\
 &=S_2^{1/6}\|f\|_{L^{6,\infty}}.
\end{aligned}
\tag{54}
\]

Le sens est donc bien

\[
 L^{6,\infty}(\operatorname{supp}F)
 \hookrightarrow L^{3,\infty}(\operatorname{supp}F),
\]

avec facteur `S₂^{1/6}`. **Seul `supp F` est utilisé dans (54).** La taille de `supp ∇F` n'intervient pas dans cette restriction. D'ailleurs, pour `F` lisse et compacte, `supp ∇F⊂supp F`, mais cette inclusion supplémentaire n'est pas nécessaire à la preuve.

En combinant (49), (50) et (54),

\[
 \|F\|_{L^{3,\infty}(\mathbb R^2)}
 \leq C_2S_2^{1/6}
 \|\nabla F\|_{L^{3/2,\infty}(\mathbb R^2)}.
\tag{55}
\]

### 9.3 Comparaisons cylindriques et sens des inégalités

Pour toute fonction scalaire ou vectorielle `f(r,z)` supportée dans `R/2<r<3R/2`, son relèvement axisymétrique pondéré `\widetilde f=(R/r)f` satisfait, pour `0<p<∞`,

\[
 \boxed{
 \frac23(\pi R)^{1/p}
 \|f\|_{L^{p,\infty}(\mathbb R^2)}
 \leq
 \|\widetilde f\|_{L^{p,\infty}(\mathbb R^3)}
 \leq
 2(3\pi R)^{1/p}
 \|f\|_{L^{p,\infty}(\mathbb R^2)}.}
\tag{56}
\]

En effet, `2/3≤R/r≤2` et `πR≤2πr≤3πR`. Pour la majoration, le superniveau tridimensionnel à hauteur `t` est contenu dans le relèvement de `{|f|>t/2}` et son volume est au plus `3πR` fois l'aire méridienne. Pour la minoration, le relèvement de `{|f|>3t/2}` est contenu dans le superniveau tridimensionnel et son volume est au moins `πR` fois l'aire. Ces inclusions fixent les sens, souvent inversés par erreur.

Appliquée à `f=F`, la borne supérieure de (56) donne

\[
 K_u
 \leq2(3\pi R)^{1/3}
 \|F\|_{L^{3,\infty}(\mathbb R^2)}.
\tag{57}
\]

Appliquée à `f=∇F`, l'identité (5) et la borne **inférieure** de (56) donnent

\[
 \|\nabla F\|_{L^{3/2,\infty}(\mathbb R^2)}
 \leq\frac32(\pi R)^{-2/3}K_\omega.
\tag{58}
\]

Le choix de la borne inférieure dans (58) est indispensable : on doit contrôler la norme plane du gradient par la norme tridimensionnelle du curl, pas l'inverse.

### Théorème 9.1 — support méridien mince

Les équations (55), (57) et (58) donnent

\[
 \boxed{
 \|U\|_{L^{3,\infty}(\mathbb R^3)}
 \leq C_{\rm cyl}
 \left(\frac{S_2}{R^2}\right)^{1/6}
 \|\nabla\times U\|_{L^{3/2,\infty}(\mathbb R^3)},}
\tag{59}
\]

où, avec les constantes intermédiaires ci-dessus,

\[
 C_{\rm cyl}
 =3^{4/3}\pi^{-1/3}C_2.
\tag{60}
\]

La puissance et le facteur de `R` sont exacts : `S₂^{1/6}R^{-1/3}=(S₂/R²)^{1/6}`.

En particulier,

\[
 K_u\geq\kappa>0,
 \qquad K_\omega\leq K
 \quad\Longrightarrow\quad
 \boxed{
 \frac{S_2}{R^2}
 \geq C_{\rm cyl}^{-6}
 \left(\frac\kappa K\right)^6.}
\tag{61}
\]

Ce résultat est indépendant du nombre de couches, de leurs signes, de leurs décalages, de leurs annulations ponctuelles et de la géométrie de leurs superniveaux. Pour deux produits dont les supports méridiens ont des aires `O(a₁b₁)` et `O(a₂b₂)`, on a simplement

\[
 S_2\leq C(a_1b_1+a_2b_2),
\tag{62}
\]

même si les supports sont décalés. Ainsi deux couches toutes deux minces ne peuvent conserver les deux gates critiques. Les annulations ne constituent pas un échappement : elles peuvent seulement réduire `supp F`, ce qui renforce (59).

### Verdict de la contre-revue

**VALIDÉ.** Le lemme universel proposé est correct. Le weak-to-weak `L^{3/2,∞}→L^{6,∞}` est valide; l'interpolation (52)–(53) évite toute fragilité de formulation d'O'Neil. L'inclusion sur support fini a le bon sens et n'utilise que `supp F`. Les deux comparaisons cylindriques nécessaires ont les sens (57) et (58). Aucun profil ou module de non-annulation n'est requis.

## 10. Résultat scientifique et décision

### Résultat positif borné

Le théorème 9.1 est le résultat principal : toute vorticité de swirl compact portée par une aire méridienne `o(R²)` force `K_u/K_ω→0`, indépendamment de la séparabilité et des annulations. Le lemme 3.1 ajoute une information directionnelle plus fine : sous la géométrie effective (31), il montre qu'un masquage d'une fraction `β₀` de la transition ne peut avoir une ouverture `δ→0` sous les gates `K_u≥κ`, `K_ω≤K`; voir (36).

### Résultat négatif borné

La représentation comme somme de deux produits ne suffit pas à attribuer un coût Lorentz à chaque couche. Le dipôle de translations (37) conserve une vitesse faible-`L³` non petite et un curl faible-`L^{3/2}` borné, alors que les coûts individuels divergent. Tout futur claim doit soit travailler sur `F` après annulation, soit imposer un module de non-annulation explicite.

**État : ABANDONNER la branche “support méridien mince à deux couches” comme échappement aux gates; CONTINUER sur la localisation directionnelle.** La dégénérescence des superniveaux peut encore compliquer une minoration BMO, mais elle ne contourne plus le gate de support (59).

## 11. Prochaine expérience décisive

Restreindre désormais le balayage aux familles satisfaisant la borne nécessaire (61), puis calculer avec arithmétique d'intervalles les quatre quantités directionnelles du champ total

\[
 S_\lambda,
 \quad\ell_\lambda,
 \quad h_\lambda,
 \quad
 \beta_\lambda(\delta)
 =\frac{\int_{\mathcal M_\delta}|\partial_zF|}
        {\int|\partial_zF|}
\tag{63}
\]

au niveau `λ` presque optimal. Le test doit balayer les signes, amplitudes, décalages relatifs et rapports `a/b`, puis chercher l'une des deux issues suivantes :

- certification uniforme de (31) et `β≥β₀`, qui ferme la famille par (36) ;
- suite respectant (61), avec `K_u≥κ`, `K_ω≤K`, mais un des rapports `ℓ/a`, `h/b`, `S/(ab)` ou `β` tend vers zéro. Cette suite n'échapperait pas au gate de support, mais identifierait le mécanisme précis empêchant encore une boule BMO quantitative.

Références internes utilisées : `docs/reports/navier-stokes/cycle-0031-compact-swirl-aspect-gate.md` et `docs/reports/navier-stokes/reviews/cycle-0031-countermodel.md`. Source primaire fonctionnelle ajoutée à la contre-revue : O'Neil (1963), DOI indiqué ci-dessus.
