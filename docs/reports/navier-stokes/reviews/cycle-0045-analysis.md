# Cycle 0045 — compacité locale et porte de trace

Date : 2026-08-15

Statut : \`AI_INTERNAL_DERIVATION\`; aucun résultat Clay, aucune simulation.

## Verdict

Sous les hypothèses exactes des cycles 0041--0044, le passage local est plus
fort que ne le suggère la seule topologie faible-\(L^3\). Sur tout cylindre
fixe \(B_R\times[-S,0]\), l'équation et l'égalité d'énergie des champs lisses
\(Z_j\) donnent

\[
 \sup_j\left[
 \|Z_j\|_{L^\infty_\sigma L^2_x(B_R)}
 +\|\nabla Z_j\|_{L^2_{\sigma,x}(B_R\times[-S,0])}
 \right]<\infty.                                \tag{1}
\]

La seconde borne ne vient pas de
\(L^{3,\infty}\) comme implication fonctionnelle. Elle résulte d'une
estimation locale de l'équation, avec pression globale dans
\(L^{4/3}_{\rm loc}\), absorption puis remplissage des trous.

Le ledger Aubin--Lions--Simon ferme alors

\[
 Z_j\to Z
 \quad\text{fortement dans }
 L^2_{\rm loc}(\mathbb R^3\times[-S,0])
 \cap L^3_{\rm loc}(\mathbb R^3\times[-S,0]),   \tag{2}
\]

après extraction. Par conséquent,

\[
 Z_j\otimes Z_j\to Z\otimes Z
 \quad\text{dans }L^1_{\rm loc},                \tag{3}
\]

et aucun défaut de Reynolds intérieur ne subsiste. Avec la décomposition
proche/harmonique de la pression, on passe aussi l'inégalité d'énergie locale.
La limite est donc une solution faible adaptée de l'équation renormalisée
non forcée avec drift \(+\kappa D\), sur chaque fenêtre finie.

La première implication encore manquante est la **non-trivialité de la
trace**. Ni (1), ni (2), ni une minoration
\(\|Z_j(0)\|_{L^2(B_R)}\ge c\) n'empêchent

\[
 Z_j(0)\rightharpoonup0.                        \tag{4}
\]

Le lemme minimal qui change la situation est un moment signé persistant
contre une fonction test fixe, ou une compacité forte de la trace elle-même.

## 1. Cadre exact et quantificateurs

Fixons

\[
 I=[-S,0],\qquad S>0,\qquad R>0.                \tag{5}
\]

Soient

\[
 L_j\to\infty,\qquad L_j\ge8R,\qquad
 Z_j=Q_{L_j}U_j,\qquad \operatorname{div}Z_j=0. \tag{6}
\]

On utilise exactement :

\[
 \sup_j\operatorname*{ess\,sup}_{\sigma\in I}
 \|U_j(\sigma)\|_{L^{3,\infty}(\mathbb R^3)}
 \le M,                                         \tag{7}
\]

\[
 \|Q_{L_j}W\|_{L^{3,\infty}}
 \le C_Q\|W\|_{L^{3,\infty}},                   \tag{8}
\]

et, pour tout \(m\ge0\) et toute boule fixe,

\[
 \sup_{\sigma\in I}
 \|\nabla^mF_j(\sigma)\|_{L^\infty(B_{8R})}
 \longrightarrow0.                             \tag{9}
\]

La borne (8) vient de la conjugaison d'une même réalisation unité de
Bogovskii. Une famille seulement déclarée « solénoïdale » ne fournit pas
cette uniformité.

Les \(Z_j\) sont lisses sur \(I\), car les temps physiques considérés sont
strictement antérieurs au premier temps singulier. La lissité individuelle
autorise l'égalité d'énergie ; elle ne donne pas à elle seule une constante
uniforme.

Le coefficient Type I \(\kappa\) est fixe. Une famille
\(\kappa_j\) uniformément bornée se traite après extraction
\(\kappa_j\to\kappa\).

## 2. Équation renormalisée et pression

Avec

\[
 D=I+y\cdot\nabla,                               \tag{10}
\]

l'équation exacte est

\[
 \boxed{
 \partial_\sigma Z_j-\Delta Z_j
 +\mathbb P\operatorname{div}(Z_j\otimes Z_j)
 +\kappa DZ_j=F_j,\qquad
 \operatorname{div}Z_j=0.}                     \tag{11}
\]

Le signe du drift est positif. Il est cohérent avec l'équation de base
\(\partial_\sigma U-\Delta U+H+\kappa DU=0\) et avec le terme
\(+\kappa[D,Q_L]U\) de \(F_L\).

Dans la jauge globale de Riesz,

\[
 \pi_j=(-\Delta)^{-1}
 \partial_a\partial_b((Z_j)_a(Z_j)_b)
      =R_aR_b((Z_j)_a(Z_j)_b),                 \tag{12}
\]

et (11) devient

\[
 \partial_\sigma Z_j-\Delta Z_j
 +\operatorname{div}(Z_j\otimes Z_j)
 +\nabla\pi_j+\kappa DZ_j=F_j.                 \tag{13}
\]

La force est divergence-free. Une pression locale définie modulo une
fonction harmonique doit conserver cette composante ; seule une constante
spatiale disparaît après gradient.

## 3. Ledger brut avant énergie

### 3.1 Vitesse

Pour \(1\le q<3\), la formule des couches sur un ensemble \(E\) de mesure
finie donne

\[
 \|v\|_{L^q(E)}
 \le
 \left(\frac3{3-q}\right)^{1/q}
 |E|^{1/q-1/3}\|v\|_{L^{3,\infty}(E)}.          \tag{14}
\]

Ainsi

\[
 Z_j\text{ est bornée dans }
 L^\infty(I;L^q(B_{8R}))\quad(q<3).             \tag{15}
\]

En particulier,

\[
 \|Z_j\|_{L^\infty_IL^2(B_{8R})}
 \le \sqrt3\,|B_{8R}|^{1/6}C_QM.               \tag{16}
\]

L'endpoint fort \(q=3\) n'est pas disponible.

### 3.2 Produit et pression

Hölder--Lorentz et les transformées de Riesz donnent

\[
 \|Z_j\otimes Z_j\|_{L^{3/2,\infty}}
 +C_{\rm CZ}^{-1}\|\pi_j\|_{L^{3/2,\infty}}
 \le C_{\rm ON}(C_QM)^2.                       \tag{17}
\]

Sur une boule fixe, faible-\(L^{3/2}\) s'injecte dans \(L^p\) pour tout
\(p<3/2\). Au choix \(p=4/3\),

\[
 \|g\|_{L^{4/3}(E)}
 \le3^{3/2}|E|^{1/12}
 \|g\|_{L^{3/2,\infty}(E)}.                    \tag{18}
\]

Donc

\[
 Z_j\otimes Z_j,\ \pi_j
 \text{ sont bornés dans }
 L^\infty(I;L^{4/3}(B_{8R})).                  \tag{19}
\]

### 3.3 Dérivée temporelle négative

Sur \(B_{8R}\),

\[
 \Delta Z_j\in L^\infty_IW^{-2,2}_x,           \tag{20}
\]

et

\[
 DZ_j
 =\operatorname{div}(Z_j\otimes y)-2Z_j
 \in L^\infty_IW^{-1,2}_x.                    \tag{21}
\]

Les termes quadratique et de pression sont dans
\(L^\infty_IW^{-1,4/3}_x\), tandis que (9) borne la force dans
\(L^\infty_IL^{4/3}_x\). Par (13),

\[
 \boxed{
 \partial_\sigma Z_j
 \text{ est bornée dans }
 L^\infty(I;W^{-2,4/3}(B_{8R})).}               \tag{22}
\]

Sans utiliser encore l'énergie,

\[
 L^2(B_{8R})\Subset H^{-1}(B_{8R})
 \hookrightarrow W^{-2,4/3}(B_{8R}),           \tag{23}
\]

et le corollaire 4 de Simon donne déjà

\[
 Z_j\to Z
 \quad\text{dans }C(I;H^{-1}(B_{8R}))           \tag{24}
\]

après extraction.

Cette première compacité ne suffit pas au produit. Elle deviendra en revanche
la topologie utile pour la trace.

## 4. Estimation d'énergie locale uniforme

La flèche fonctionnelle

\[
 L^\infty_\sigma L^{3,\infty}_x
 \Longrightarrow L^2_\sigma H^1_{x,\rm loc}    \tag{25}
\]

est fausse pour des champs arbitraires. Ici, la PDE et l'égalité d'énergie
des champs lisses fournissent la dérivée manquante.

### 4.1 Inégalité de Caccioppoli avec rayon extérieur

Fixons \(R\le r<\rho\le4R\), posons
\(\delta=\rho-r\), et choisissons
\(\eta\in C_c^\infty(B_\rho)\), égale à un sur \(B_r\), avec

\[
 |\nabla\eta|\le C\delta^{-1},\qquad
 |\Delta\eta|\le C\delta^{-2}.                  \tag{26}
\]

On multiplie (13) par \(\eta^2Z_j\) et on intègre sur
\([-S,\tau]\). Les termes de diffusion croisés, de convection et de pression
donnent

\[
 \begin{aligned}
 D_j(r)\le{}&
 \theta D_j(\rho)
 +C_{\theta,R,S,\kappa}
 \Big[
 \sup_{\sigma\in I}\|Z_j(\sigma)\|_{L^2(B_\rho)}^2\\
 &\quad+
 \int_I\|Z_j\|_{L^3(B_\rho)}^3\,d\sigma
 +\int_I\|\pi_jZ_j\|_{L^1(B_\rho)}\,d\sigma
 +\|F_j\|_{L^\infty(I\times B_\rho)}
 \Big],
 \end{aligned}                                  \tag{27}
\]

où

\[
 D_j(r)=\int_I\!\int_{B_r}|\nabla Z_j|^2        \tag{28}
\]

et \(\theta>0\) peut être choisi arbitrairement petit. Les puissances de
\(\delta^{-1}\) sont absorbées dans la constante de (27).

Le drift ne perd aucune dérivée. En effet,

\[
 Z_j\cdot DZ_j
 =\operatorname{div}\left(y\frac{|Z_j|^2}{2}\right)
  -\frac{|Z_j|^2}{2},                           \tag{29}
\]

donc son coût est un terme quadratique local déjà borné par (16).

### 4.2 Absorption du terme cubique

Écrivons

\[
 E_j(\rho,\sigma)=\|Z_j(\sigma)\|_{L^2(B_\rho)}^2,
 \qquad
 G_j(\rho,\sigma)=\|\nabla Z_j(\sigma)\|_{L^2(B_\rho)}.
\]

La borne (16) donne

\[
 \sup_{j,\sigma}E_j(\rho,\sigma)\le C_RM^2.     \tag{30}
\]

Gagliardo--Nirenberg local donne

\[
 \|Z_j\|_{L^3(B_\rho)}^3
 \le C E_j^{3/4}
 \big(G_j+\delta^{-1}E_j^{1/2}\big)^{3/2}.
                                                               \tag{31}
\]

Par Young et (30), pour tout \(\varepsilon>0\),

\[
 \|Z_j\|_{L^3(B_\rho)}^3
 \le\varepsilon G_j^2+C_{\varepsilon,R,M}.      \tag{32}
\]

Il n'est donc pas nécessaire de prétendre que faible-\(L^3\) contrôle
directement \(L^3\) : c'est le gradient de l'égalité d'énergie qui est absorbé.

### 4.3 Absorption de la pression

Par (19),

\[
 \sup_{j,\sigma}
 \|\pi_j(\sigma)\|_{L^{4/3}(B_\rho)}
 \le C_{R,C_Q,C_{\rm CZ}}M^2.                  \tag{33}
\]

De plus,

\[
 \|Z_j\|_{L^4(B_\rho)}
 \le C E_j^{1/8}
 \big(G_j+\delta^{-1}E_j^{1/2}\big)^{3/4}.      \tag{34}
\]

Hölder \(L^{4/3}\)-\(L^4\), Young et (30)--(33) donnent

\[
 \|\pi_jZ_j\|_{L^1(B_\rho)}
 \le\varepsilon G_j^2+C_{\varepsilon,R,M}.      \tag{35}
\]

Enfin,

\[
 \int_{B_\rho}|F_j||Z_j|
 \le C_R\|F_j\|_\infty M.                      \tag{36}
\]

La convergence (9) rend ce terme uniformément borné, puis nul à la limite.

### 4.4 Remplissage des trous

En choisissant les paramètres de Young assez petits, (27), (32) et (35)
donnent

\[
 D_j(r)\le\theta D_j(\rho)+C_{R,S,M,\kappa},
 \qquad R\le r<\rho\le4R,                       \tag{37}
\]

où les puissances de \((\rho-r)^{-1}\) sont explicites mais indépendantes de
\(j\). Une suite de rayons emboîtés et le lemme standard de remplissage des
trous donnent

\[
 \boxed{
 \sup_jD_j(R)\le C_{R,S,M,\kappa}.}             \tag{38}
\]

Pour justifier la dernière itération sans hypothèse cachée, on choisit
\(\theta\) plus petit que l'inverse du facteur géométrique créé par les
dérivées des cutoffs. Le reste
\(\theta^nD_j(4R)\) tend vers zéro pour chaque \(j\), puisque chaque solution
est lisse et \(D_j(4R)<\infty\). La constante obtenue avant cette limite ne
dépend pas de \(j\).

Les équations (16) et (38) prouvent (1).

## 5. Aubin--Lions--Simon après énergie

Sur \(B_{2R}\),

\[
 H^1(B_{2R})\Subset L^2(B_{2R})
 \hookrightarrow W^{-2,4/3}(B_{2R}).           \tag{39}
\]

Les bornes

\[
 Z_j\text{ dans }L^2(I;H^1(B_{2R})),
 \qquad
 \partial_\sigma Z_j\text{ dans }
 L^\infty(I;W^{-2,4/3}(B_{2R}))                \tag{40}
\]

et le théorème de Simon impliquent

\[
 Z_j\to Z
 \quad\text{fortement dans }L^2(I;L^2(B_R)).   \tag{41}
\]

L'énergie locale donne aussi

\[
 Z_j\text{ bornée dans }
 L^{10/3}(I\times B_R)
 \cap L^{8/3}(I;L^4(B_R))
 \cap L^4(I;L^3(B_R)).                          \tag{42}
\]

En interpolant (41) avec la première borne de (42),

\[
 Z_j\to Z
 \quad\text{fortement dans }L^q(I\times B_R)
 \quad\text{pour tout }q<10/3.                 \tag{43}
\]

Le choix \(q=3\) donne

\[
 Z_j\otimes Z_j\to Z\otimes Z
 \quad\text{fortement dans }L^{3/2}_{\rm loc},  \tag{44}
\]

ce qui est plus fort que (3).

## 6. Pression et inégalité d'énergie locale

Choisissons \(\zeta\in C_c^\infty(B_{4R})\), égale à un sur \(B_{2R}\), et
décomposons

\[
 \pi_j=\pi_{j,\rm near}+h_j,\qquad
 \pi_{j,\rm near}
 =R_aR_b\big(\zeta(Z_j)_a(Z_j)_b\big).          \tag{45}
\]

Sur \(B_{2R}\), \(h_j\) est harmonique. Par (44) et la bornitude forte des
Riesz,

\[
 \pi_{j,\rm near}\to\pi_{\rm near}
 \quad\text{dans }L^{3/2}(I\times B_R).         \tag{46}
\]

La borne globale faible-\(L^{3/2}\), (18), et les estimations intérieures
harmoniques donnent, pour tout \(m\),

\[
 \sup_j\|h_j\|_{L^\infty(I;C^m(B_R))}
 \le C_{m,R,M}.                                 \tag{47}
\]

Après extraction, \(h_j\) converge faible-étoile en temps et localement
faiblement dans ces espaces. Comme \(Z_j\to Z\) fortement dans
\(L^1_{\rm loc}\), le produit \(h_jZ_j\) passe dans les distributions. La
partie proche passe par (43), (46).

Les égalités locales d'énergie de \(Z_j\) contiennent :

- \(|Z_j|^2\), qui converge dans \(L^1_{\rm loc}\) ;
- le flux cubique, qui converge grâce au \(L^3_{\rm loc}\) fort ;
- \(\pi_jZ_j\), traité par (45)--(47) ;
- \(F_j\cdot Z_j\), qui tend vers zéro par (9) ;
- le drift, réécrit par (29) ;
- \(|\nabla Z_j|^2\), qui passe par semi-continuité inférieure.

La limite satisfait donc

\[
 \begin{aligned}
 \partial_\sigma\frac{|Z|^2}{2}
 -\Delta\frac{|Z|^2}{2}
 +|\nabla Z|^2
 +\operatorname{div}
   \left[\left(\frac{|Z|^2}{2}+\pi\right)Z\right]\\
 +\kappa\operatorname{div}
   \left(y\frac{|Z|^2}{2}\right)
 -\kappa\frac{|Z|^2}{2}
 \le0
 \end{aligned}                                  \tag{48}
\]

dans les distributions. C'est l'inégalité d'énergie locale adaptée à
l'équation renormalisée avec drift. Après la dérenormalisation exacte, elle
correspond à l'inégalité locale standard ; cette dernière opération doit
encore suivre l'horloge et les domaines.

## 7. Limite locale obtenue

Les termes linéaires passent par (24), les produits par (44), la pression par
(45)--(47), et \(F_j\to0\) par (9). Ainsi

\[
 \boxed{
 \partial_\sigma Z-\Delta Z
 +\operatorname{div}(Z\otimes Z)
 +\nabla\pi+\kappa DZ=0,\qquad
 \operatorname{div}Z=0.}                       \tag{49}
\]

Il n'y a pas de tenseur de Reynolds résiduel.

Si les fenêtres disponibles s'étendent vers tout
\([-S,0]\), \(S<\infty\), une extraction diagonale produit une solution
ancienne locale de (49) sur
\(\mathbb R^3\times(-\infty,0]\), avec l'énergie locale (48). Cela ne prouve
ni mildness globale, ni égalité avec une ancienne KNSS, ni rigidité.

Le quantificateur temps est important :

- une borne essentielle dans (7) donne les estimations pour presque tout
  temps, puis les représentants continus négatifs de (24) ;
- \(L_j\) est fixe sur chaque fenêtre ; si \(L_j=L_j(\sigma)\), un terme
  \(\partial_\sigma Q_{L_j}\) manque dans (11) ;
- les constantes de (38) dépendent de \(S,R,M,\kappa\), mais pas de \(j\).

## 8. Première implication encore manquante : trace non nulle

La convergence (24) donne une trace dans \(H^{-1}_{\rm loc}\) :

\[
 Z_j(0)\to Z(0)
 \quad\text{dans }H^{-1}(B_R).                  \tag{50}
\]

Elle ne donne pas la convergence forte \(L^2\) au temps \(0\). La compacité
forte de (41) est une assertion de volume espace-temps et ne contrôle pas une
section de mesure temporelle nulle.

Une condition minimale suffisante est :

\[
 \exists\psi\in C_c^\infty(B_R;\mathbb R^3),\
 c_*>0:\qquad
 |\langle Z_j(0),\psi\rangle|\ge c_*
 \quad\text{pour tout }j.                       \tag{51}
\]

Alors (50) implique

\[
 |\langle Z(0),\psi\rangle|\ge c_*,
 \qquad Z(0)\ne0.                               \tag{52}
\]

Une autre condition suffisante est la convergence forte des traces dans
\(L^2(B_R)\), accompagnée d'une minoration de leur norme. En revanche,

\[
 \inf_j\|Z_j(0)\|_{L^2(B_R)}>0                  \tag{53}
\]

seule ne suffit pas. Une minoration de faible-\(L^3\), d'enstrophie ou de
mesure d'un superniveau non signé ne fournit pas automatiquement le moment
(51).

Le **lemme minimal actif** est donc la persistance d'un observable linéaire
fixe (51) depuis la normalisation du cycle 0041 jusqu'au temps commun de
l'extraction.

## 9. Passe adverse

### 9.1 Concentration critique

Pour \(a\ne0\),

\[
 V(x)=\frac{a\times x}{|x|^2}                  \tag{54}
\]

est tangent aux sphères et divergence-free hors de zéro. Une troncature
radiale lisse \(V_n\), égale à \(V\) sur
\(2/n<|x|<1/2\), vérifie

\[
 \sup_n\|V_n\|_{L^{3,\infty}(B_1)}<\infty,
 \qquad
 \int_{B_1}|V_n|^3\asymp\log n,
 \qquad
 \int_{B_1}|\nabla V_n|^2\gtrsim n.             \tag{55}
\]

Ce profil réfute (25) pour des champs arbitraires, mais il est exclu par la
borne PDE (38). Il confirme que l'étape énergie doit être démontrée, pas
attribuée à la norme de Lorentz.

### 9.2 Oscillation et défaut quadratique

Pour \(\varphi\in C_c^\infty(B_1)\), posons

\[
 A_n=(0,0,n^{-1}\varphi(x)\cos(nx_1)),\qquad
 W_n=\nabla\times A_n.                          \tag{56}
\]

Alors \(W_n\) est lisse, compact, divergence-free, uniformément borné dans
\(L^{3,\infty}\), mais

\[
 W_n\rightharpoonup0,\qquad
 (W_n)_2^2\rightharpoonup\frac12\varphi^2,
 \qquad
 \|\nabla W_n\|_2\asymp n.                     \tag{57}
\]

En ajoutant \(b(n^2\sigma)\), on conserve même une borne de
\(\partial_\sigma W_n\) dans \(W^{-2,4/3}\), car
\(\|W_n\|_{W^{-2,4/3}}\lesssim n^{-2}\). Cette famille attaque le ledger brut
(15), (22), (24), mais viole (38). Le défaut quadratique est donc réellement
éliminé par l'énergie locale, pas par la seule équicontinuité négative.

### 9.3 Couche temporelle et perte de trace

Sur \(\mathbb T^3\),

\[
 w_n(t,x)=e^{-n^2t}(0,\sin(nx_1),0),\qquad t\ge0,              \tag{58}
\]

est une solution Navier--Stokes exacte, globale, lisse, de pression nulle.
Elle satisfait une borne énergétique uniforme et

\[
 w_n\to0
 \text{ fortement dans }L^2((0,S)\times\mathbb T^3),          \tag{59}
\]

mais

\[
 \|w_n(0)\|_2=c>0,\qquad
 w_n(0)\rightharpoonup0.                        \tag{60}
\]

Le cycle 0004 possède une variante exacte avec pression non nulle et défaut
quadratique sur des traces mobiles \(t_n\asymp n^{-2}\).

Ces exemples sont périodiques et leur couche est attachée à une extrémité
temporelle ; ils ne réfutent pas l'extraction ancienne sur \(\mathbb R^3\).
Ils réfutent exactement la déduction (53) \(\Rightarrow Z(0)\ne0\) depuis la
seule compacité de volume.

## 10. Audit des cinq points potentiellement bloquants

1. **Calcul de cutoff.** Pour \(L_j\ge8R\), \(Q_{L_j}=I\) sur toutes les
   boules utilisées dans le ledger local. Aucun terme de Bogovskii ne rentre
   dans l'estimation de Caccioppoli. Son seul rôle restant est la borne
   globale uniforme (8), nécessaire à (16)--(19). Si \(Q_{L_j}\) n'est pas
   la conjugaison exacte de l'opérateur unité, la preuve s'arrête à (8).
2. **Calderón--Zygmund parabolique.** Aucun estimateur parabolique endpoint
   n'est invoqué. La pression utilise seulement les Riesz **spatiales** à
   chaque temps ; la dérivée temporelle est bornée directement dans l'espace
   négatif (22). Remplacer cette étape par une régularité parabolique forte
   au endpoint faible-\(L^3\) serait injustifié.
3. **Simon.** Les deux triplets sont réellement ordonnés :
   \(L^2\Subset H^{-1}\hookrightarrow W^{-2,4/3}\) pour (24), puis
   \(H^1\Subset L^2\hookrightarrow W^{-2,4/3}\) pour (41). La dérivée est
   contrôlée sur une boule plus grande que celle où la compacité est conclue.
   Il n'y a ni domaine mobile ni constante dépendant de \(L_j\).
4. **Interpolation.** (41) et la borne \(L^{10/3}\) donnent la convergence
   forte seulement pour \(q<10/3\). Le choix \(q=3\) est licite ; revendiquer
   l'endpoint fort \(10/3\) serait une erreur. Le produit fort est donc pris
   dans \(L^{3/2}\), pas dans \(L^{5/3}\).
5. **Pression de Riesz.** La pression complète n'est pas déclarée fortement
   compacte. Seule \(\pi_{j,\rm near}\) converge fortement par (44)--(46).
   Le reste \(h_j\) est harmonique et passe faible-étoile contre la vitesse
   forte. Omettre \(h_j\), ou identifier directement toute la pression avec
   \(R_aR_b(Z_aZ_b)\) depuis une convergence seulement locale, laisserait un
   trou.

Sous ces qualifications, aucune erreur bloquante n'est trouvée dans le lemme
de compacité locale. La conclusion ne couvre toujours ni le moment (51), ni
la mildness globale, ni le raccord Clay.

## 11. Ledger final

| Objet | Borne uniforme | Convergence après extraction | Statut pour la limite |
|---|---|---|---|
| \(Z_j\) | \(L^\infty_IL^q_{\rm loc}\), \(q<3\) | faible-étoile | insuffisant seul |
| \(\partial_\sigma Z_j\) | \(L^\infty_IW^{-2,4/3}_{\rm loc}\) | équicontinuité | \(C_IH^{-1}_{\rm loc}\) fort |
| \(\nabla Z_j\) | \(L^2_{I,x,\rm loc}\), par (38) | faible | dissipation semi-continue |
| \(Z_j\) | \(L^{10/3}_{I,x,\rm loc}\) | \(L^q_{\rm loc}\) fort, \(q<10/3\) | produit identifié |
| \(Z_j\otimes Z_j\) | \(L^{5/3}_{\rm loc}\) après énergie | \(L^{3/2}_{\rm loc}\) fort | aucun défaut de Reynolds |
| \(\pi_{j,\rm near}\) | Calderón--Zygmund local | \(L^{3/2}_{\rm loc}\) fort | flux de pression passe |
| \(h_j\) | \(L^\infty_IC^m_x\) sur le core | faible-étoile en temps | pression harmonique conservée |
| \(F_j\) | \(C^\infty_{x,\rm loc}\), uniforme en temps | zéro fortement | force locale éliminée |
| \(Z_j(0)\) | \(L^2_{\rm loc}\) borné | \(H^{-1}_{\rm loc}\) fort, \(L^2\) faible | non-trivialité non préservée |

## 12. Sources primaires

| ID | Source | Usage exact | Limite |
|---|---|---|---|
| veille ciblée, pas d'ID créé ici | Jacques Simon, *Compact sets in the space \(L^p(0,T;B)\)*, *Ann. Mat. Pura Appl.* **146** (1986), 65--96, [DOI 10.1007/BF01762360](https://doi.org/10.1007/BF01762360), corollaire 4 | (23)--(24), (39)--(43) | exige une vraie compacité spatiale pour conclure en norme positive |
| \`NS-SRC-0067\` | Richard O'Neil, *Convolution operators and \(L(p,q)\) spaces*, *Duke Math. J.* **30** (1963), 129--142, [DOI](https://doi.org/10.1215/S0012-7094-63-03015-1) | produit Lorentz (17) | aucune compacité |
| \`NS-SRC-0181\` | Jörg Wolf, *Adv. Differential Equations* **22** (2017), 305--338, [DOI](https://doi.org/10.57262/ade/1489802453) | pression locale/harmonique | domaine fixe et hypothèses duales |
| \`NS-SRC-0182\` | Hyunju Kwon, *J. Differential Equations* **357** (2023), 1--31, [DOI](https://doi.org/10.1016/j.jde.2023.01.049) | projection locale et composante harmonique | ne fournit pas la trace non triviale |
| \`NS-SRC-0186\` | Zachary Bradshaw et Tai-Peng Tsai, *J. Math. Fluid Mech.* **24** (2022), article 3, [DOI](https://doi.org/10.1007/s00021-021-00637-4) | expansion de pression et champ lointain | aucun observable de trace |
| \`NS-SRC-0005\` | Caffarelli, Kohn et Nirenberg, *Comm. Pure Appl. Math.* **35** (1982), 771--831, [DOI](https://doi.org/10.1002/cpa.3160350604) | notion adaptée et inégalité locale | ne construit pas la normalisation non triviale |
| \`NS-SRC-0043\` | Foias, Rosa et Temam, *Ann. Inst. Fourier* **63** (2013), 2515--2573, [DOI](https://doi.org/10.5802/aif.2836) | continuité faible des trajectoires d'énergie | pas de compacité forte uniforme des traces |
| \`NS-SRC-0012\` | Escauriaza, Seregin et Šverák, *Russian Math. Surveys* **58** (2003), 211--250, [DOI](https://doi.org/10.1070/RM2003v058n02ABEH000609) | modèle compacité--rigidité avec \(L^3\) fort | ne remplace pas la porte de trace sous faible-\(L^3\) |

Simon est la seule veille primaire ciblée nouvelle de cette revue. Aucun
identifiant canonique n'est ajouté, conformément au périmètre d'un fichier
unique.

## 13. Statut exact

| Implication | Statut |
|---|---|
| (7), (8) \(\Rightarrow L^\infty_IL^q_{\rm loc}\), \(q<3\) | **PROUVÉ** |
| pression globale dans \(L^\infty_IL^{3/2,\infty}_x\) | **PROUVÉ**, Riesz--Lorentz |
| équation \(\Rightarrow\partial_\sigma Z_j\) dans \(L^\infty_IW^{-2,4/3}_{\rm loc}\) | **PROUVÉ** |
| ledger brut \(\Rightarrow C_IH^{-1}_{\rm loc}\) compact | **PROUVÉ**, Simon |
| faible-\(L^3\) seul \(\Rightarrow\) énergie locale | **FAUX fonctionnellement** |
| équation lisse + bornes (7)--(9) \(\Rightarrow\) (38) | **PROUVÉ**, Caccioppoli et remplissage des trous |
| (38), (22) \(\Rightarrow L^2_{\rm loc}\) fort | **PROUVÉ**, Simon |
| produit quadratique sans défaut | **PROUVÉ** par (43)--(44) |
| passage de la pression et de l'énergie locale | **PROUVÉ** par (45)--(48) |
| limite locale adaptée non forcée avec drift | **PROUVÉ** sur chaque fenêtre finie |
| minoration de norme de trace \(\Rightarrow Z(0)\ne0\) | **FAUX** |
| moment fixe (51) \(\Rightarrow Z(0)\ne0\) | **PROUVÉ** |
| existence d'un moment (51) depuis la capture du cycle 0041 | **MANQUANT** |
| limite obtenue \(\Rightarrow\) ancienne mild KNSS non triviale | **NON DÉMONTRÉ** |

## 14. Prochain lemme décisif

Il faut désormais convertir la concentration scalaire du cycle 0041 en un
observable linéaire qui ne change ni avec \(j\), ni avec le temps-record :

\[
 \boxed{
 \exists R,\psi,c_*>0:
 \quad|\langle Z_j(0),\psi\rangle|\ge c_*.
 }                                             \tag{61}
\]

Le test adverse doit chercher des champs divergence-free concentrés ou
oscillants qui satisfont toutes les minorations non signées actuellement
enregistrées mais convergent vers zéro contre chaque test fixe. S'ils
survivent, la normalisation doit être renforcée ou modulée ; réutiliser une
simple norme critique sous un autre nom ne ferme pas la trace.
