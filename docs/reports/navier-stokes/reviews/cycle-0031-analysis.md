# Cycle 0031 — localisation quantitative de la compensation directionnelle

Date : 2026-08-14  
Statut : dérivation analytique interne, non revue par les pairs, **pas** `PAPER_PROOF`  
Verrou : `GAP-COMPACT-VELOCITY-WEAK-CRITICAL-DIRECTION`

## Décision du cycle

Trois actions ont été comparées sur une échelle de 0 à 5.

| Action | Nouveauté | Tractabilité | Falsifiabilité | Effet de levier | Total |
|---|---:|---:|---:|---:|---:|
| Localiser la compensation par un défaut de flux de bord, puis sélectionner un bon rayon avec faible-`L^3(U)` | 4 | 5 | 5 | 5 | **19** |
| Déduire directement une boule critique de la seule identité globale `∫ curl U=0` | 2 | 3 | 4 | 3 | 12 |
| Construire et certifier une famille multi-échelle complète à compensateur rare | 4 | 2 | 4 | 3 | 13 |

L'action sélectionnée est la première. Le résultat positif est un lemme local avec défaut de bord et un lemme de sélection annulaire. Le résultat négatif est un contre-profil compact exact montrant que le défaut de bord ne peut pas être supprimé.

## 1. Cadre exact et normalisations

On travaille à temps fixé sur `R³`. Soit

\[
 U\in C_c^\infty(\mathbb R^3;\mathbb R^3),
 \qquad \nabla\cdot U=0,
 \qquad W=\nabla\times U.
\tag{1}
\]

Il ne s'agit pas ici d'une solution de Navier–Stokes, mais d'un lemme cinématique destiné à une éventuelle tranche temporelle d'une solution régulière ou d'un profil limite. On pose

\[
 K=\|W\|_{L^{3/2,\infty}(\mathbb R^3)},
 \qquad L=\|U\|_{L^{3,\infty}(\mathbb R^3)},
\tag{2}
\]

avec la quasi-norme

\[
 \|f\|_{L^{p,\infty}}
 =\sup_{\lambda>0}\lambda
   |\{|f|>\lambda\}|^{1/p}.
\tag{3}
\]

Sur `{W≠0}`, la direction est `ξ=W/|W|`. Dans une boule `B`, `ζ∈L¹(B;R³)` désigne une extension arbitraire de `ξ` à `{W=0}`. On note

\[
 \operatorname{MO}_B(\zeta)
 =\fint_B|\zeta-\zeta_B|\,dx,
 \qquad
 \zeta_B=\fint_B\zeta\,dx.
\tag{4}
\]

Pour `e∈S²` et `0<α≤1`, définissons la partie active dans le cône orienté

\[
 G_{B,\alpha,e}
 =\{x\in B:W(x)\ne0,\ \xi(x)\cdot e\geq\alpha\},
 \qquad
 m_B=\int_{G_{B,\alpha,e}}|W|\,dx.
\tag{5}
\]

La quantité sans dimension pertinente est

\[
 \theta_B=\frac{m_B}{K|B|^{1/3}}.
\tag{6}
\]

L'inégalité de Lorentz utilisée deux fois ci-dessous est

\[
 \int_E|f|\,dx
 \leq \frac p{p-1}\|f\|_{L^{p,\infty}}|E|^{1-1/p}.
\tag{7}
\]

Elle donne les constantes `3` pour `p=3/2` et `3/2` pour `p=3`.

## 2. Ce que donne exactement `∫ curl U=0`

La compacité du support de `U` implique, composante par composante,

\[
 \int_{\mathbb R^3}W\,dx=0.
\tag{8}
\]

Mais sur une boule arbitraire, l'identité exacte est

\[
 F_B:=\int_BW\,dx
 =\int_{\partial B}n\times U\,dS.
\tag{9}
\]

Le terme `F_B` est un flux de circulation, non une erreur que l'on peut ignorer. Il est nul si `U` s'annule au voisinage de `∂B`, notamment lorsqu'une boule contient tout le support de `U`, mais il n'est pas nul sur une boule active générale.

## 3. Lemme actif avec défaut de bord

### Lemme 3.1

Sous (1)–(5), pour toute boule `B` de mesure finie et `K>0`, toute extension intégrable `ζ` vérifie

\[
 \boxed{
 \operatorname{MO}_B(\zeta)
 \geq
 \frac{2}{27K^3|B|}
 \min\!\left\{
   \alpha m_B^3,
   (\alpha m_B-F_B\cdot e)_+^3
 \right\}.}
\tag{10}
\]

En particulier, si

\[
 F_B\cdot e\leq\frac{\alpha m_B}{2},
\tag{11}
\]

alors

\[
 \boxed{
 \operatorname{MO}_B(\zeta)
 \geq
 \frac{\alpha^3m_B^3}{108K^3|B|}
 =\frac{\alpha^3\theta_B^3}{108}.}
\tag{12}
\]

### Preuve

Posons

\[
 \nu_{e,B}=\int_B(-W\cdot e)_+\,dx.
\tag{13}
\]

Si `P=∫_B(W·e)_+` et `N=ν_{e,B}`, alors `P-N=F_B·e`. Or (5) donne `P≥αm_B`; donc

\[
 \nu_{e,B}\geq(\alpha m_B-F_B\cdot e)_+.
\tag{14}
\]

Le lemme de compensation de Lorentz sans hypothèse de moyenne nulle, établi au cycle 0026, donne

\[
 \operatorname{MO}_B(\zeta)
 \geq
 \frac{2}{27K^3|B|}
 \min\{\alpha m_B^3,\nu_{e,B}^3\}.
\tag{15}
\]

Les équations (14)–(15) prouvent (10). Sous (11), `ν_{e,B}≥αm_B/2`. Comme `0<α≤1`,

\[
 \min\{\alpha m_B^3,(\alpha m_B/2)^3\}
 =\frac{\alpha^3m_B^3}{8},
\]

ce qui donne (12). `□`

### Cas du support entier

Si `U=0` au voisinage de `∂B`, alors `F_B=0`. La version à moyenne exactement nulle du cycle 0026 est plus forte que (12) :

\[
 \operatorname{MO}_B(\zeta)
 \geq
 \frac{2\alpha^3m_B^3}{27K^3|B|}.
\tag{16}
\]

Cela fournit toujours une boule — toute boule contenant `supp U` — mais pas nécessairement une boule à la petite échelle du cœur actif. Le facteur `|B|^{-1}` peut donc diluer entièrement l'information pertinente pour un contrôle logarithmique aux petites échelles.

## 4. Sélection d'un rayon par faible-`L³(U)`

Le défaut (9) peut être rendu petit sur **au moins une** sphère d'une couronne, à condition que `L` soit assez petit par rapport à la masse active.

### Lemme 4.1 — bonne sphère annulaire

Fixons `x₀∈R³` et `R>0`. Écrivons `B_r=B(x₀,r)` et supposons qu'une masse active `m_R>0` est présente dans `B_R`. Posons

\[
 C_{\rm tr}
 =\frac32\left(\frac{28\pi}{3}\right)^{2/3}
 \simeq14.2631579608.
\tag{17}
\]

Il existe `s∈[R,2R]` tel que

\[
 |F_{B_s}|
 \leq\int_{\partial B_s}|U|\,dS
 \leq C_{\rm tr}LR.
\tag{18}
\]

Si

\[
 C_{\rm tr}LR\leq\frac{\alpha m_R}{2},
\tag{19}
\]

alors cette même boule vérifie

\[
 \boxed{
 \operatorname{MO}_{B_s}(\zeta)
 \geq
 \frac{\alpha^3m_R^3}{108K^3|B_s|}.}
\tag{20}
\]

Avec

\[
 \theta_R=\frac{m_R}{K|B_R|^{1/3}},
\tag{21}
\]

on obtient la forme explicite

\[
 \boxed{
 \operatorname{MO}_{B_s}(\zeta)
 \geq\frac{\alpha^3\theta_R^3}{864}.}
\tag{22}
\]

La condition suffisante (19) s'écrit

\[
 \frac LK
 \leq \kappa_0\alpha\theta_R,
 \qquad
 \kappa_0=
 \frac{(4\pi/3)^{1/3}}{2C_{\rm tr}}
 \simeq0.05650894278.
\tag{23}
\]

### Preuve

Par coaire et (7),

\[
\begin{aligned}
 \int_R^{2R}\int_{\partial B_s}|U|\,dS\,ds
 &=\int_{B_{2R}\setminus B_R}|U|\,dx\\
 &\leq\frac32L|B_{2R}\setminus B_R|^{2/3}\\
 &=C_{\rm tr}LR^2.
\end{aligned}
\tag{24}
\]

Un rayon `s∈[R,2R]` satisfait donc (18). La masse de cône est monotone sous l'inclusion, donc `m_{B_s}≥m_R`. Sous (19),

\[
 F_{B_s}\cdot e
 \leq|F_{B_s}|
 \leq\frac{\alpha m_R}{2}
 \leq\frac{\alpha m_{B_s}}2.
\tag{25}
\]

Le lemme 3.1 donne (20). Enfin `|B_s|≤|B_{2R}|=8|B_R|`, d'où (22). La substitution de `m_R=θ_RK(4π/3)^{1/3}R` dans (19) donne (23). `□`

### Conséquence pour une oscillation logarithmiquement pondérée

Considérons une famille de champs renormalisés et une suite `R_j→0`. Si, uniformément en `j`,

\[
 \theta_{R_j}\geq\theta_0>0,
 \qquad
 \frac{L_j}{K_j}
 \leq\kappa_0\alpha\theta_0,
\tag{26}
\]

alors il existe `s_j∈[R_j,2R_j]` avec

\[
 \operatorname{MO}_{B_{s_j}}(\zeta_j)
 \geq\frac{\alpha^3\theta_0^3}{864}>0.
\tag{27}
\]

Par conséquent, toute semi-norme du type

\[
 \sup_{0<r<r_0}
 \bigl(1+\log(r_0/r)\bigr)
 \operatorname{MO}_{B(x,r)}(\zeta)
\tag{28}
\]

diverge le long de cette suite. C'est une obstruction conditionnelle et falsifiable. Elle ne s'applique pas si `θ_R→0` ou si le rapport `L/K` n'est pas assez petit.

## 5. Échelle de toutes les quantités

Sous l'échelle de Navier–Stokes

\[
 U_\lambda(x)=\lambda U(\lambda x),
 \qquad
 W_\lambda(x)=\lambda^2W(\lambda x),
\tag{29}
\]

et pour la boule correspondante `B_{R/λ}`, on a :

| Quantité | Transformation |
|---|---|
| `||U||_{L^{3,∞}}=L` | invariante |
| `||W||_{L^{3/2,∞}}=K` | invariante |
| `m_B` | `λ⁻¹m_B` |
| `F_B` | `λ⁻¹F_B` |
| `K|B|^{1/3}` | `λ⁻¹K|B|^{1/3}` |
| `θ_B` | invariante |
| `MO_B(ζ)` | invariante |
| condition (19) | invariante |

Ainsi (10), (12), (20) et (22) sont exactement critiques. La pondération logarithmique (28), elle, détecte l'accumulation des mêmes oscillations à des rayons tendant vers zéro.

Le raccord de Biot–Savart

\[
 U=\nabla\times(-\Delta)^{-1}W
\tag{30}
\]

est valide ici parce que `div U=0` et `U` est compact. L'inégalité de Hardy–Littlewood–Sobolev en espaces de Lorentz donne qualitativement `L≤C_BS K`. Elle ne fournit toutefois pas la petite constante requise dans (23). Le rapport `L/K` est donc un véritable paramètre du lemme, pas une conséquence gratuite du raccord elliptique.

## 6. Audit du profil annulaire anisotrope

Le profil candidat communiqué pendant le cycle est, en coordonnées cylindriques,

\[
 U(r,\vartheta,z)
 =V\frac Rr
   \eta\!\left(\frac{r-R}{a}\right)
   \chi\!\left(\frac zb\right)e_\vartheta.
\tag{31}
\]

Pour rendre les comparaisons ci-dessous uniformes, il faut fixer des profils lisses `η,χ`, non nuls, compacts, dont les dérivées sont non nulles sur des ensembles de mesure positive, et supposer

\[
 0<a\leq c_0R,
 \qquad 0<b,
 \qquad c_0\sup\{|s|:s\in\operatorname{supp}\eta\}<1.
\tag{32}
\]

La dernière condition maintient le support à distance de l'axe `r=0` et assure `r≈R`. Le champ (31) est alors lisse, compact et exactement divergence-free. Son rotationnel a seulement deux composantes :

\[
 \omega_r=-\partial_zU_\vartheta
 =-\frac{VR}{rb}\eta\chi',
 \qquad
 \omega_z=\frac1r\partial_r(rU_\vartheta)
 =\frac{VR}{ra}\eta'\chi.
\tag{33}
\]

Le volume actif est comparable à `Rab`. Pour une fonction d'amplitude comparable à `A` sur un ensemble de volume comparable à `M`,

\[
 \|f\|_{L^{3,\infty}}^3\asymp A^3M,
 \qquad
 \|f\|_{L^{3/2,\infty}}^3\asymp A^3M^2.
\tag{34}
\]

Sous les hypothèses de non-dégénérescence ci-dessus, (34) donne bien

\[
 \boxed{
 K_u^3:=\|U\|_{L^{3,\infty}}^3
 \asymp V^3Rab,}
\tag{35}
\]

\[
 \boxed{
 K_z^3:=\|\omega_z\|_{L^{3/2,\infty}}^3
 \asymp \frac{V^3R^2b^2}{a},
 \qquad
 K_r^3:=\|\omega_r\|_{L^{3/2,\infty}}^3
 \asymp \frac{V^3R^2a^2}{b}.}
\tag{36}
\]

Les exposants annoncés sont donc corrects. Ce sont des comparabilités avec constantes dépendant des profils et de `c₀`, pas des identités universelles.

Supposons maintenant

\[
 K_u\geq\kappa>0,
 \qquad
 \|\omega\|_{L^{3/2,\infty}}\leq K.
\tag{37}
\]

Comme `|ω_r|,|ω_z|≤|ω|`, on a `K_r,K_z≤K`. Posons

\[
 x=\frac aR,
 \qquad y=\frac bR,
 \qquad q=\left(\frac\kappa K\right)^3.
\tag{38}
\]

Les quotients de (35)–(36) imposent

\[
 \frac{x^2}{y}\gtrsim q,
 \qquad
 \frac{y^2}{x}\gtrsim q.
\tag{39}
\]

Il n'est pas nécessaire de supposer `a≈b`. En combinant les deux inégalités dans les bonnes puissances,

\[
 x^3=left(\frac{x^2}{y}\right)^2
      \left(\frac{y^2}{x}\right)
 \gtrsim q^3,
 \qquad
 y^3=left(\frac{y^2}{x}\right)^2
      \left(\frac{x^2}{y}\right)
 \gtrsim q^3.
\tag{40}
\]

Par conséquent,

\[
 \boxed{
 \frac aR,\frac bR
 \gtrsim\left(\frac\kappa K\right)^3.}
\tag{41}
\]

L'implication annoncée est correcte, à trois réserves près :

1. `κ` doit être une minoration de la norme faible-`L³` de **ce profil**, et `K` une majoration de la norme faible-`L^{3/2}` de la vorticité **totale**;
2. les profils `η,χ` doivent rester dans une classe uniformément non dégénérée; s'ils dépendent de `a,b`, les constantes cachées peuvent absorber tout le gain;
3. le régime `a≈R` ou un support touchant l'axe demande un autre calcul géométrique; les proxies `volume≈Rab` et `R/r≈1` n'y sont plus uniformes.

La conclusion (41) constitue une borne uniforme sur l'anisotropie d'un tube unique. Elle ne contrôle pas encore une superposition de tubes, des annulations entre profils dans la norme de vitesse, ni la direction sur les boules traversant simultanément plusieurs échelles.

## 7. Passe contradictoire : contre-profil compact exact

Toute affirmation selon laquelle **chaque** boule active doit avoir une oscillation directionnelle positive est fausse, même sous toutes les hypothèses (1).

Soit `χ=χ(ρ,z)` une fonction axisymétrique lisse, compacte, constante au voisinage de l'axe, égale à `1` sur un cylindre central. Avec `ρ=(x₁²+x₂²)^{1/2}`, posons

\[
 U_\chi(x)
 =\frac12\chi(\rho,z)(-x_2,x_1,0).
\tag{42}
\]

Alors `Uχ∈C_c^∞` et un calcul exact donne

\[
 \nabla\cdot U_\chi=0,
\tag{43}
\]

\[
 W_\chi=\nabla\times U_\chi
 =-\frac{\rho}{2}\partial_z\chi\,e_\rho
  +\left(\chi+\frac{\rho}{2}\partial_\rho\chi\right)e_3.
\tag{44}
\]

Sur toute boule `B` strictement contenue dans la zone `{χ=1}`, on a

\[
 W_\chi=e_3,
 \qquad \xi=e_3,
 \qquad \operatorname{MO}_B(\xi)=0.
\tag{45}
\]

Pour `α=1`, cette boule est pourtant active avec

\[
 m_B=|B|,
 \qquad
 F_B\cdot e_3=|B|=m_B.
\tag{46}
\]

Le second terme de (10) est donc exactement nul. Le flux de bord exporte toute la moyenne locale vers la couche de troncature, tandis que l'identité globale (8) reste exacte. Ce contre-profil :

- réfute toute minoration uniforme sur toutes les boules actives fondée seulement sur `K`, `m_B` et `|B|` ;
- montre qu'une compensation globale ne se localise pas sans contrôler (9) ;
- ne réfute pas l'existence d'une autre boule, intersectant la couche de retour, sur laquelle l'oscillation est grande.

### Compensateur rare et de grande amplitude

Dans une tranche où `∂zχ=0`, la compensation axiale est

\[
 W_\chi\cdot e_3
 =\chi+\frac\rho2\partial_\rho\chi.
\tag{47}
\]

Pour un profil de transition fixé, comprimé dans une couche radiale d'épaisseur `δ` autour d'un rayon `a`, le second terme a amplitude `O(a/δ)` sur un volume `O(aδH)`, où `H` est la hauteur de la tranche. Sa contribution à faible-`L^{3/2}` est donc de taille

\[
 \frac a\delta(a\delta H)^{2/3}
 =a^{5/3}H^{2/3}\delta^{-1/3}.
\tag{48}
\]

À masse positive macroscopique fixée, rendre la couche arbitrairement rare fait donc diverger `K`. Plus abstraitement, si une masse de compensation projetée `ν` est portée par un ensemble `E`, (7) impose

\[
 |E|\geq\left(\frac{\nu}{3K}\right)^3.
\tag{49}
\]

L'exposant cubique des lemmes 3.1 et 4.1 est ainsi le bon coût d'échelle contre les compensateurs rares. En revanche, après normalisation de `K`, la masse active `θ_B` peut tendre vers zéro : aucune oscillation uniforme ne subsiste alors dans (12). C'est précisément le cas limite que devrait exclure un futur lemme dynamique.

## 8. Attaques logiques effectuées

1. **Quantificateur “toutes les boules”.** Réfuté par (42)–(46).
2. **Usage local de `∫curl U=0`.** Faux en général; l'identité correcte est (9).
3. **Compensateur arbitrairement rare à coût critique borné.** Impossible si `m_B/(K|B|^{1/3})` reste minoré; voir (49). Possible seulement en faisant dégénérer cette masse normalisée ou en augmentant `K`.
4. **Biot–Savart comme petite constante.** `L≤C_BS K` ne donne pas (23); aucun petit facteur n'apparaît sans hypothèse supplémentaire.
5. **Passage à Navier–Stokes.** Aucun : (1) est purement cinématique. Il manque un mécanisme dynamique garantissant simultanément (26) sur une suite de profils de concentration.
6. **Valeur de la direction sur `{W=0}`.** Les bornes valent pour toute extension intégrable; elles ne reposent donc pas sur une convention favorable.
7. **Haute fréquence.** Les deux normes de (2) et `θ_B` sont critiques; une simple remise à l'échelle ne crée pas la petitesse de `L/K`. Des oscillations internes supplémentaires peuvent la créer, mais elles risquent elles-mêmes de détruire l'alignement de direction.
8. **Constante dépendant du support.** (16) dépend de `|B|`; choisir une boule de support trop grande rend la borne non informative. Le lemme annulaire remplace ce défaut par la condition explicite (23).

9. **Proxy annulaire pris pour une identité.** (35)–(36) sont uniformes seulement pour des profils fixes et un tore restant loin de l'axe. Cette dépendance est désormais explicite.

## 9. Validation reproductible et résidus

### Vérification algébrique

Les résidus de divergence et de rotationnel de (42)–(44) sont exactement nuls par différentiation. Une vérification indépendante par différences centrées, avec le profil test non compact `χ=exp(-(ρ²+z²))` utilisé uniquement pour contrôler l'algèbre, est reproductible par :

```powershell
@'
import math

def chi(x,y,z): return math.exp(-(x*x+y*y+z*z))
def U(x,y,z):
    q=chi(x,y,z)
    return (-0.5*y*q,0.5*x*q,0.0)
def deriv(comp,var,p,h=1e-6):
    a=list(p); b=list(p); a[var]+=h; b[var]-=h
    return (U(*a)[comp]-U(*b)[comp])/(2*h)
for p in [(0.4,-0.3,0.2),(0.8,0.2,-0.5)]:
    x,y,z=p; q=chi(*p); rho=math.hypot(x,y)
    div=sum(deriv(i,i,p) for i in range(3))
    curl=(deriv(2,1,p)-deriv(1,2,p),
          deriv(0,2,p)-deriv(2,0,p),
          deriv(1,0,p)-deriv(0,1,p))
    pred=(x*z*q,y*z*q,(1-rho*rho)*q)
    print(p,'div',f'{div:.3e}',
          'curl_err',max(abs(a-b) for a,b in zip(curl,pred)))
'@ | python -
```

Sortie obtenue :

```text
(0.4, -0.3, 0.2) div -2.082e-11 curl_err 2.027444878649476e-11
(0.8, 0.2, -0.5) div 6.939e-12 curl_err 1.313960051874119e-11
```

Ces nombres ne sont pas une certification en arithmétique d'intervalles. La certification mathématique est l'identité symbolique (43)–(44); le calcul flottant n'est qu'un test de transcription.

### Résidu scientifique certifié

- Résidu de `div Uχ` : `0` exactement.
- Résidu de `curl Uχ-Wχ` : `0` exactement.
- Résidu de la compensation globale `∫R³ curl Uχ` : `0` exactement, par support compact.
- Résidu dimensionnel du profil (31) : nul; les trois exposants (35)–(36) et l'implication (41) sont cohérents.
- Résidu non fermé : aucune borne inférieure générale connue pour `θ_R` et aucun mécanisme connu imposant le petit rapport (23) à un profil de concentration Navier–Stokes.

## 10. Verdict et prochain test décisif

**Résultat positif.** Une masse de vorticité presque collinéaire dans une boule force une oscillation directionnelle critique dès que sa compensation ne peut pas sortir par le flux de bord; (10) quantifie exactement ce défaut. Le faible-`L³(U)` sélectionne une bonne sphère et donne la minoration sans dimension (22), sous l'hypothèse falsifiable (23).

**Résultat négatif.** L'identité globale `∫curl U=0` ne suffit pas à minorer l'oscillation sur chaque boule active. Le champ (42) est un contre-profil compact exact.

**État : CONTINUER, mais ne pas promouvoir en critère de régularité.**

La prochaine expérience décisive consiste à épingler des profils `η,χ` dans la famille annulaire (31), calculer leurs fonctions de distribution faible-Lorentz sans proxy de volume, puis optimiser le quotient

\[
 \mathcal Q(\eta,\chi,a/R,b/R)
=\frac{\|U\|_{L^{3,\infty}}}
        {\|\nabla\times U\|_{L^{3/2,\infty}}}
\tag{50}
\]

sous une contrainte `θ_R≥θ₀` et une contrainte d'oscillation logarithmique sur toutes les boules rencontrant la couche de retour. Le balayage doit inclure les boules de rayon comparable à `a`, à `b` et à `R`, et vérifier directement la minoration (41). Deux issues sont discriminantes :

- une borne inférieure uniforme sur `Q` bloquerait le recours à (23) dans cette famille et constituerait un résultat négatif exploitable;
- une suite avec `Q→0`, `θ_R≥θ₀` et direction log-BMO uniformément contrôlée contredirait (22), donc révélerait nécessairement une erreur de discrétisation, de calcul de faible-Lorentz ou de balayage des boules.

Références internes utilisées : `docs/reports/navier-stokes/reviews/cycle-0026-analysis.md`, en particulier l'inégalité de compensation sans moyenne nulle; `claims/navier-stokes/NS-LORENTZ-CONE-COMPENSATION.json`. Aucune nouvelle source externe n'est introduite par cette dérivation.
