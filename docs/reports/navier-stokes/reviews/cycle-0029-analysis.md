# Passe analytique indépendante — cycle 0029 : paire torique à impulsion annulée

Date : 2026-08-14

Statut : **dérivation IA interne**, non publiée, non indépendante au sens inter-familles et jamais `PAPER_PROOF`

## Verdict

Une paire de tubes de vorticité toroïdaux lisses, congruents, disjoints et de signes opposés annule exactement son impulsion hydrodynamique. Cette annulation ne suffit à aucun des deux raccords recherchés.

1. Elle supprime le terme dipolaire `|x|^{-3}` de la vitesse, mais une paire séparée d’un vecteur non nul conserve un multipôle d’ordre suivant. Pour la paire coaxiale placée aux hauteurs `±s`,
   \[
   u_z(Ze_z)
   =\frac{3s\mathcal I_h}{\pi Z^4}
   +O(Z^{-5}),
   \qquad Z\to+\infty,
   \]
   où `𝓘_h>0` est l’impulsion d’un anneau. Pour la paire utilisée par le rapport racine, dont les axes sont translatés de `±3Re₁`, le témoin correspondant est
   \[
   u(te_1)
   =-\frac{9R\mathcal I_h}{2\pi t^4}e_3
   +O(t^{-5}).
   \]
   Dans les deux cas, la vitesse n’est donc pas de Schwartz.

2. Après normalisation
   \[
   K=\|W\|_{L^{3/2,\infty}}^*,
   \qquad q=h/R,
   \]
   il existe des constantes `0<c_b<C_b<∞`, indépendantes de `h` et `R`, telles que
   \[
   c_bK^3q
   \leq\|u\|_3^3
   \leq C_bK^3(q+q^2).
   \]
   La minoration est une conséquence exacte de Stokes sur les sections du tube; elle ne peut pas être détruite par le champ de l’anneau opposé. Ainsi `||u||₃≈Kq^{1/3}→0` lorsque le tube devient mince. L’annulation de l’impulsion améliore la queue, pas la masse critique locale de vitesse.

3. Une paire coaxiale reste exactement dans la classe axisymétrique sans swirl. Une translation latérale d’un anneau détruit cette symétrie tout en conservant l’annulation de l’impulsion, mais ne change ni la queue multipolaire non nulle ni l’effondrement `L³`. Pour `q` assez petit, même la paire non axisymétrique appartient au régime perturbatif de petites données critiques.

4. Pour les paramètres discrets du rapport racine, l’extension directionnelle de chaque tore vers le même fond `e₃` conserve la borne log-BMO sur **toutes** les boules. La preuve ne suppose pas qu’une boule ne voie qu’un corridor : la sous-additivité de l’oscillation moyenne donne directement une constante au plus double de celle du tore unique.

La paire à impulsion opposée ne franchit donc ni le gate de Schwartz sur `R³`, ni le gate de non-dégénérescence critique. Elle élimine seulement le premier multipôle.

## 1. Construction et quantificateurs

Fixons un profil transverse

\[
b(\rho)=\bar b(\rho^2),
\qquad
\bar b\in C_c^\infty([0,1)),
\qquad
b\geq0,
\qquad
b=1\text{ sur }[0,1/2].
\tag{1}
\]

Soient `R>0`, `0<σ≤1/2`,

\[
s=\sigma R,
\qquad
0<h<\frac{\sigma R}{4},
\qquad
q=\frac hR.
\tag{2}
\]

Dans les coordonnées cylindriques autour de l’axe `e_z`, posons

\[
d_\pm(r,z)
=\sqrt{(r-R)^2+(z\mp s)^2}
\tag{3}
\]

et, pour `a>0`,

\[
\boxed{
W_{h,s}(x)
=a\left[
b(d_+(x)/h)-b(d_-(x)/h)
\right]e_\theta(x).}
\tag{4}
\]

Les deux supports sont disjoints. Ils restent dans `r≥R-h>0`; (1) rend chaque tube `C_c^∞(R³)`. L’indépendance en `θ` donne

\[
\operatorname{div}W_{h,s}
=\frac1r\partial_\theta W^\theta_{h,s}=0.
\tag{5}
\]

Chaque anneau a une moyenne vectorielle nulle, car

\[
\int_0^{2\pi}e_\theta(\theta)d\theta=0.
\tag{6}
\]

La vitesse désigne toujours le représentant décroissant de Biot–Savart :

\[
u_{h,s}
=\nabla\times(-\Delta)^{-1}W_{h,s}
=\frac1{4\pi}
\int_{\mathbb R^3}
\frac{W_{h,s}(y)\times(x-y)}{|x-y|^3}dy.
\tag{7}
\]

Il n’y a donc pas de composante harmonique ajoutée.

## 2. Normalisation faible-`L^{3/2}`

Dans les coordonnées toriques d’un anneau,

\[
x(\theta,\rho,\phi)
=((R+\rho\cos\phi)\cos\theta,
  (R+\rho\cos\phi)\sin\theta,
  z_0+\rho\sin\phi),
\]

le jacobien vaut `(R+ρcosφ)ρ`. Définissons

\[
M_b(t)=4\pi^2
\int_{\{0<\rho<1:b(\rho)>t\}}\rho d\rho,
\qquad
\kappa_b=\sup_{t>0}tM_b(t)^{2/3}>0.
\tag{8}
\]

Les supports étant disjoints,

\[
|\{|W_{h,s}|>\lambda\}|
=2Rh^2M_b(\lambda/a).
\tag{9}
\]

La quasi-norme est donc exactement

\[
\boxed{
K
=2^{2/3}\kappa_b
aR^{2/3}h^{4/3}.}
\tag{10}
\]

Pour prescrire `K`, il faut choisir

\[
a
=\frac{K}
{2^{2/3}\kappa_bR^{2/3}h^{4/3}}.
\tag{11}
\]

La norme forte critique reste elle aussi proportionnelle à `K` :

\[
\|W_{h,s}\|_{3/2}^{3/2}
=8\pi^2a^{3/2}Rh^2
\int_0^1b(\rho)^{3/2}\rho d\rho
=C_bK^{3/2}.
\tag{12}
\]

La séparation `s` n’entre ni dans (9), ni dans (10), tant que les supports ne se rencontrent pas.

## 3. Impulsion : annulation exacte

Pour une vorticité compacte, l’impulsion hydrodynamique est

\[
I[W]=\frac12
\int_{\mathbb R^3}x\times W(x)dx.
\tag{13}
\]

Pour un anneau positif centré à une hauteur arbitraire `z₀`, les composantes horizontales s’annulent par intégration en `θ` et

\[
I[W^+]\cdot e_z
=\frac12\int r|W^+|dx
=\pi a\int b(d/h)r^2drdz.
\tag{14}
\]

Avec

\[
B_1=\int_0^1b(\rho)\rho d\rho,
\qquad
B_3=\int_0^1b(\rho)\rho^3d\rho,
\]

le changement de variables torique donne la valeur exacte

\[
\boxed{
\mathcal I_h
:=I[W^+]\cdot e_z
=2\pi^2aR^2h^2B_1
+\pi^2ah^4B_3>0.}
\tag{15}
\]

Cette quantité ne dépend pas de `z₀`. Plus généralement, l’impulsion est invariante par translation parce que `∫W^+=0` :

\[
I[W^+(\cdot-c)]
=I[W^+]
+\frac12c\times\int W^+
=I[W^+].
\tag{16}
\]

Le second anneau de (4) est congruent et porte le signe opposé. Par linéarité,

\[
\boxed{
I[W_{h,s}]
=\mathcal I_he_z-\mathcal I_he_z=0.}
\tag{17}
\]

Cette annulation est exacte pour tout `h,R,s,a`; elle ne repose sur aucune limite de tube mince.

## 4. Ce que l’impulsion annule réellement

### 4.1 Premier moment

Posons

\[
M_{ij}=\int x_iW_j(x)dx.
\]

Pour tout champ compact divergence-free,

\[
0=\int\operatorname{div}(x_ix_jW)dx
=M_{ij}+M_{ji}.
\tag{18}
\]

Le tenseur `M` est antisymétrique et

\[
I_k=\frac12\varepsilon_{kij}M_{ij},
\qquad
M_{ij}=\varepsilon_{ijk}I_k.
\tag{19}
\]

L’annulation de l’impulsion équivaut donc à l’annulation de **tout** le premier moment de `W`, pas seulement de sa composante axiale. Comme `∫W=0`, le développement de Biot–Savart perd ses termes d’ordres `|x|^{-2}` et `|x|^{-3}`; il donne au moins

\[
u_{h,s}(x)=O(|x|^{-4}).
\tag{20}
\]

### 4.2 Second moment d’une paire traduite

Soit

\[
Q_{klm}[W]=\int x_kx_lW_m(x)dx.
\]

Pour un champ de moyenne nulle traduit de `c`,

\[
Q_{klm}[W(\cdot-c)]
=Q_{klm}[W]
+c_kM_{lm}+c_lM_{km}.
\tag{21}
\]

Pour une paire congruente de signes opposés, séparée par

\[
d=c_+-c_-,
\]

le moment propre `Q[W]` s’annule et

\[
\boxed{
Q^{\rm pair}_{klm}
=d_kM_{lm}+d_lM_{km}.}
\tag{22}
\]

Le moment d’un anneau vérifie `M_{12}=𝓘_h`, `M_{21}=-𝓘_h`. Ainsi `Q^{pair}≠0` pour tout `d≠0`. Par exemple :

\[
Q^{\rm pair}_{312}=d_3\mathcal I_h,
\qquad
Q^{\rm pair}_{112}=2d_1\mathcal I_h.
\tag{23}
\]

Le premier multipôle survivant est donc déterminé par la séparation des anneaux et leur impulsion individuelle.

### 4.3 Coefficient explicite sur l’axe

Pour la paire coaxiale (4), la composante axiale de la vitesse sur l’axe est exactement

\[
u_z(Ze_z)
=\frac12
\int_{0}^{\infty}\int_{\mathbb R}
\frac{W^\theta(r,z)r^2}
{(r^2+(Z-z)^2)^{3/2}}
drdz.
\tag{24}
\]

Écrivons le profil positif sous la forme `w₀(r,ζ)`, paire en `ζ`. L’expansion uniforme pour `Z→+∞` donne

\[
\begin{aligned}
u_z(Ze_z)
&=\frac12Z^{-3}
\int w_0(r,\zeta)r^2
\left[
\frac{3(s+\zeta)}Z
-\frac{3(-s+\zeta)}Z
\right]drd\zeta
+O(Z^{-5})\\
&=3sZ^{-4}
\int w_0(r,\zeta)r^2drd\zeta
+O(Z^{-5}).
\end{aligned}
\tag{25}
\]

Par (14), l’intégrale vaut `𝓘_h/π`. Par conséquent,

\[
\boxed{
u_z(Ze_z)
=\frac{3s\mathcal I_h}{\pi Z^4}
+O(Z^{-5}).}
\tag{26}
\]

Le coefficient est non nul dès que `s>0` et `a>0`.

## 5. Schwartz exige une infinité de cancellations

Hors du support de `W`, le champ `u` vérifie

\[
\Delta u=0,
\qquad
\operatorname{div}u=0,
\qquad
\operatorname{curl}u=0.
\tag{27}
\]

Son développement extérieur est une série de multipôles harmoniques. Si `u` était de Schwartz, tous les coefficients de cette série seraient nuls; par analyticité, `u` serait identiquement nul dans la composante extérieure. Autrement dit, pour une vorticité compacte, une vitesse de Biot–Savart de Schwartz exige l’annulation de **tous les coefficients multipolaires extérieurs**, et non seulement de l’impulsion.

La paire (4) échoue déjà au second moment par (22), et son échec est quantitativement visible dans (26). Elle a seulement amélioré

\[
|u(x)|=O(|x|^{-3})
\quad\text{vers}\quad
|u(x)|=O(|x|^{-4}).
\tag{28}
\]

Pour la famille explicite, le second membre de (28) est optimal dans certaines directions.

Une paire arbitraire à impulsion nulle pourrait annuler accidentellement aussi son second moment. La seule conclusion universelle de `I=0` est la majoration `O(|x|^{-4})`; la non-nullité du coefficient exige un calcul comme (22) ou (26).

## 6. Norme critique de vitesse : minoration exacte par Stokes

La cancellation lointaine ne peut pas supprimer la circulation locale d’un tube.

Fixons l’anneau positif. Pour chaque angle `θ` et chaque

\[
\frac h4\leq\rho\leq\frac h2,
\]

soit `D_{θ,ρ}` le disque méridien de rayon `ρ`, centré en `(r,z)=(R,s)`, et `C_{θ,ρ}=∂D_{θ,ρ}`. Le disque ne rencontre pas le tube négatif. Comme `b=1` dans le demi-cœur, Stokes donne exactement

\[
\oint_{C_{\theta,\rho}}u\cdot dl
=\int_{D_{\theta,\rho}}
W\cdot e_\theta dA
=a\pi\rho^2.
\tag{29}
\]

Par Hölder sur le cercle de longueur `2πρ`,

\[
\int_{C_{\theta,\rho}}|u|^3dl
\geq
\frac{(a\pi\rho^2)^3}{(2\pi\rho)^2}
=\frac{a^3\pi}{4}\rho^4.
\tag{30}
\]

Le jacobien torique vaut `(R+ρcosφ)ρ`. En intégrant (30) en `θ` et `ρ`, puis en utilisant `h<R`,

\[
\begin{aligned}
\|u\|_3^3
&\geq
(R-h/2)
\int_0^{2\pi}d\theta
\int_{h/4}^{h/2}
\frac{a^3\pi}{4}\rho^4d\rho\\
&=\frac{31\pi^2}{10240}
(R-h/2)a^3h^5\\
&\geq
\frac{31\pi^2}{20480}
a^3Rh^5.
\end{aligned}
\tag{31}
\]

Cette borne utilise le **champ total** `u`. Une vitesse produite par l’autre anneau peut modifier les valeurs ponctuelles, mais pas la circulation (29); aucune hypothèse de petitesse du champ externe n’est requise.

En substituant (11),

\[
\boxed{
\|u\|_3^3
\geq
\frac{31\pi^2}
{81920\,\kappa_b^3}
K^3\frac hR.}
\tag{32}
\]

La constante affichée n’est pas optimale, mais elle est indépendante de `σ,h,R,K` sous la seule condition de disjonction utilisée par le disque de Stokes.

## 7. Borne supérieure et équivalence d’échelle

Pour un anneau isolé, le potentiel tubulaire donne, avec `d` distance au cercle central,

\[
|u(x)|\leq Ca
\begin{cases}
h,&d\leq2h,\\
h^2/d,&2h<d<R,\\
R^2h^2/d^3,&d\geq R.
\end{cases}
\tag{33}
\]

Les volumes sont respectivement `O(Rh²)`, `O(Rd\,dd)` et `O(d²dd)`. Ainsi

\[
\|u^{\rm ring}\|_3^3
\leq C_ba^3(Rh^5+h^6).
\tag{34}
\]

Pour la paire, l’inégalité `(A+B)³≤4(A³+B³)` et la linéarité de Biot–Savart donnent

\[
\|u_{h,s}\|_3^3
\leq C_ba^3(Rh^5+h^6).
\tag{35}
\]

Combinons (11), (32) et (35). Pour `0<q<σ/4`,

\[
\boxed{
c_bK^3q
\leq\|u_{h,s}\|_3^3
\leq C_bK^3(q+q^2).}
\tag{36}
\]

En particulier, pour `K=1`,

\[
\|u_{h,s}\|_3
\asymp q^{1/3}
\longrightarrow0
\qquad(q\to0).
\tag{37}
\]

Une remise à l’échelle isotrope modifie `R` et `h` par le même facteur, conserve `q`, `K` et `||u||₃`; elle ne peut pas réparer (37).

L’impulsion annulée améliore la troisième ligne de (33) en `O(aR³h²d^{-4})` au-delà d’une boule contenant les deux anneaux. Cette amélioration ne change pas (36), dominée par les deux premières zones.

## 8. Énergie

Chaque auto-interaction possède le logarithme du filament. Lorsque `s/R=σ` reste fixé, l’interaction croisée des deux anneaux est sans logarithme. Pour `q` assez petit,

\[
\|u_{h,s}\|_2^2
\asymp_{b,\sigma}
a^2Rh^4\log\frac Rh.
\tag{38}
\]

Après (11),

\[
\boxed{
\|u_{h,s}\|_2^2
\asymp_{b,\sigma}
K^2R q^{4/3}\log\frac1q.}
\tag{39}
\]

L’énergie tend vers zéro à `R` fixé lorsque `q→0`. L’enstrophie, au contraire, vaut `Θ(K²R^{-1}q^{-2/3})` et diverge. Ni l’une ni l’autre ne remplace le contrôle critique (36).

## 9. Axisymétrie et swirl

### 9.1 Paire coaxiale

Le champ (4) est axisymétrique et purement toroïdal. Biot–Savart commute aux rotations autour de `e_z`, donc `u` est axisymétrique. Écrivons

\[
u=u^re_r+u^\theta e_\theta+u^ze_z.
\]

Comme `curl u=W` n’a pas de composante poloïdale,

\[
-\partial_zu^\theta=0,
\qquad
\frac1r\partial_r(ru^\theta)=0.
\tag{40}
\]

Ainsi `ru^θ` est constant. La régularité sur l’axe et la décroissance à l’infini imposent ce constant égal à zéro :

\[
\boxed{u^\theta=0.}
\tag{41}
\]

La paire coaxiale reste exactement dans la classe axisymétrique sans swirl, connue pour être globalement régulière pour des données lisses de taille arbitraire. Changer le signe d’un anneau ne sort pas de cette classe.

### 9.2 Paire latéralement décalée

L’annulation de l’impulsion ne requiert pas la coaxialité. Soit `W₀` un anneau de référence et

\[
W(x)=W_0(x-c_+)-W_0(x-c_-),
\qquad
c_+-c_-\notin\mathbb Re_z.
\tag{42}
\]

Par (16), les impulsions s’annulent encore. Si les axes parallèles sont distincts, aucun axe de rotation commun ne préserve la paire : la donnée sort de la classe axisymétrique sans swirl.

Les calculs de distribution et de Stokes sont locaux à chaque tube; (10) et (36) restent vrais lorsque la séparation est comparable à `R`. Le tenseur (22) reste non nul. Cette cassure de symétrie ne restaure donc pas la norme critique : `||u||₃→0` lorsque `q→0`.

### 9.3 Audit exact de la paire transverse du rapport racine

La famille effectivement retenue dans le rapport racine est une spécialisation de (42). Pour `n≥4`, elle prend

\[
R_n=2^{-n},
\qquad
h_n=2^{-n^2},
\qquad
H_n=2^{-2n},
\qquad
c_\pm=\pm3R_ne_1,
\tag{42a}
\]

où `H_n` est le rayon extérieur du corridor directionnel, à ne pas confondre avec le rapport d’aspect `h_n/R_n`. Si `W_{0,n}` est le tore positif d’axe `ℝe₃`, la paire est

\[
W_n(x)=W_{0,n}(x-c_+)-W_{0,n}(x-c_-).
\tag{42b}
\]

#### Impulsion et moment traduit

Chaque tore a une moyenne vectorielle nulle. La formule de translation (16), valable aussi pour une translation transverse, donne donc exactement

\[
I[W_{0,n}(\cdot-c_+)]=\mathcal I_ne_3,
\qquad
I[-W_{0,n}(\cdot-c_-)]=-\mathcal I_ne_3,
\qquad
I[W_n]=0.
\tag{42c}
\]

Ici `c_+-c_-=6R_ne₁`. En prenant `k=l=1,m=2` dans (22),

\[
Q^{\rm pair}_{112}
=12R_n\mathcal I_n\neq0.
\tag{42d}
\]

Le coefficient `12`, parfois masqué par la notation de demi-séparation, vient de `Q_{112}=2(c_+-c_-)_1M_{12}`.

#### Queue `|x|^{-4}` comme dérivée du dipôle

Avec la convention (7), le dipôle d’impulsion `I` est

\[
D_I(x)=\frac1{4\pi}
\left(
\frac{3(I\cdot x)x}{|x|^5}
-\frac I{|x|^3}
\right).
\tag{42e}
\]

Écrivons `a_n=3R_n`. Comme les deux champs sont deux translations signées du **même** champ, leurs multipôles propres d’ordre `|x|^{-4}` s’annulent entre eux et

\[
\begin{aligned}
D_{\mathcal I_ne_3}(x-a_ne_1)
-D_{\mathcal I_ne_3}(x+a_ne_1)
&=-2a_n\partial_1D_{\mathcal I_ne_3}(x)
+O(|x|^{-5}).
\end{aligned}
\tag{42f}
\]

Cette dérivée n’est pas identiquement nulle. Plus précisément, pour `t→+∞`,

\[
D_{\mathcal I_ne_3}(te_1)
=-\frac{\mathcal I_n}{4\pi t^3}e_3,
\]

et par conséquent

\[
\boxed{
u_n(te_1)
=-\frac{3a_n\mathcal I_n}{2\pi t^4}e_3
+O(t^{-5})
=-\frac{9R_n\mathcal I_n}{2\pi t^4}e_3
+O(t^{-5}).}
\tag{42g}
\]

Le reste est entendu pour `n` fixé, uniformément en direction sur toute région `|x|` plus grande qu’un multiple du diamètre du support. L’énoncé requis ici est la non-nullité du coefficient pour chaque membre de la famille; aucune uniformité en `n` du seuil spatial n’est utilisée. Cette paire a donc exactement une queue d’ordre `|x|^{-4}` dans au moins une direction et n’est pas de Schwartz.

#### Log-BMO sur toutes les boules

Posons

\[
L_n=\log(H_n/h_n)=(n^2-2n)\log2,
\qquad
s_n(d)=\operatorname{clamp}
\left(\frac{\log(H_n/d)}{L_n},0,1\right).
\tag{42h}
\]

Dans le corridor du tore positif, une extension unitaire relie `+e_{θ,c_+}` à `e₃`; dans celui du tore négatif, elle relie `-e_{θ,c_-}` au **même** fond `e₃`. Notons ces extensions locales `ζ_{n,+}`, `ζ_{n,-}` et leurs défauts compacts

\[
f_{n,\pm}=\zeta_{n,\pm}-e_3.
\]

Les cercles centraux sont distants de `4R_n` et `H_n/R_n=2^{-n}≤1/16`; les deux corridors sont donc disjoints. L’extension globale est exactement

\[
\zeta_n=e_3+f_{n,+}+f_{n,-}.
\tag{42i}
\]

Pour toute boule euclidienne `B`, sans restriction sur le nombre de corridors qu’elle rencontre,

\[
\begin{aligned}
\operatorname{MO}_B(\zeta_n)
&=\fint_B
\left|
(f_{n,+}-(f_{n,+})_B)
+(f_{n,-}-(f_{n,-})_B)
\right|dx\\
&\leq
\operatorname{MO}_B(f_{n,+})
+\operatorname{MO}_B(f_{n,-}).
\end{aligned}
\tag{42j}
\]

La translation du domaine et la rotation cible `diag(-1,-1,1)` montrent que les deux termes ont exactement la même borne all-ball que l’extension du tore unique du cycle 0028. L’enveloppe adimensionnée utilisée par ce lemme est, dans la notation présente,

\[
\begin{aligned}
E_n={}&\frac{n^2}{n^2-2n}
+\frac{2n}{n^2-2n}
+2n\frac{H_n}{R_n}
+2n\left(\frac{h_n}{H_n}\right)^2\\
&+\frac{n}{n^2-2n}
\left(\frac{H_n}{R_n}\right)^2
+n\left(\frac{h_n}{R_n}\right)^2<4,
\qquad n\geq4.
\end{aligned}
\]

Cette dernière inégalité ne dépend pas d’un balayage flottant : à `n=4`,
`E₄=7/2+1/8192+1/512+2^{-22}<4`; pour `n≥5`, les deux premiers termes somment à `(n+2)/(n-2)≤7/3`, le troisième est au plus `5/16`, et les trois termes exponentiels restants somment à moins de `1/256` (leurs suites sont décroissantes dès `n=5`).

Ainsi, avec la convention

\[
[f]_{\mathrm{bmo}_{\log}}
=\sup_{0<\rho<1/4}
|\log\rho|\operatorname{MO}_{B_\rho}(f),
\]

la sous-additivité donne

\[
\boxed{
[\zeta_n]_{\mathrm{bmo}_{\log}}
\leq
[f_{n,+}]_{\mathrm{bmo}_{\log}}
+[f_{n,-}]_{\mathrm{bmo}_{\log}}
\leq2CE_n,
\qquad E_n<4.}
\tag{42k}
\]

Cette preuve couvre en particulier la boule adversariale rencontrant les deux corridors; elle ne repose ni sur une moyenne globale petite, ni sur une vérification de seules boules centrées. Si la norme localisée comprend aussi un terme `L¹`, il faut l’appliquer au défaut `ζ_n-e₃`, et non au champ unitaire non intégrable. On a alors

\[
\|\zeta_n-e_3\|_1
\leq C R_n
\left(\frac{H_n^2}{L_n}+h_n^2\right),
\tag{42l}
\]

à une constante double absorbée dans `C`; ce terme est lui aussi uniformément borné et tend vers zéro.

#### Sortie de l’axisymétrie sans swirl

Une symétrie de rotation continue de la paire devrait, par continuité près de l’identité, préserver séparément les deux cœurs toriques connexes où le profil vaut son plateau : elle ne peut pas permuter ces deux composantes distantes pour des angles arbitrairement petits. Or chaque cœur torique mince a pour unique axe de rotation continue la droite `c_±+ℝe₃`. Ces droites sont parallèles et distinctes. Il n’existe donc aucun axe commun et la paire (42b) n’est axisymétrique relativement à aucune droite. Elle sort bien de la classe axisymétrique sans swirl, même si chacun de ses deux termes y appartient après recentrage.

## 10. Compatibilité Clay

### 10.1 Formulation entière `R³`

La vorticité (4) est lisse et compacte; sa vitesse est lisse, divergence-free et d’énergie finie. Mais (26) montre une queue `Z^{-4}` non nulle. La vitesse n’est pas rapidement décroissante avec toutes ses dérivées et n’est donc pas, telle quelle, une donnée admissible de l’alternative Clay (A).

Même si une correction infinie des multipôles produisait une vitesse compacte ou de Schwartz tout en restant toroïdale axisymétrique, (41) placerait encore la donnée dans la classe sans swirl globalement régulière.

Pour une paire non axisymétrique du type (42), (37) implique la petitesse de `L³` lorsque `q` est assez petit. La théorie perturbative critique donne alors une solution globale régulière, malgré l’absence de décroissance de Schwartz. La paire ne peut pas fournir un blow-up.

### 10.2 Formulation périodique

Une périodisation dans une cellule contenant les deux tubes donne une vorticité lisse périodique de moyenne nulle et une vitesse périodique lisse. Elle est admissible pour le cas Clay (B). La norme `L³` périodique conserve la borne (36), à un reste lisse d’images absorbé dans la constante. Pour `q` petit, cette donnée est également dans le régime de petites données.

### 10.3 Absence de dynamique singulière

La paire est un profil initial statique. Elle ne vérifie aucune équation stationnaire de Navier–Stokes, aucun scénario auto-similaire et aucun résidu temporel contrôlé. L’annulation de l’impulsion est conservée cinématiquement à l’instant initial; aucune conséquence sur un temps maximal n’est démontrée.

## 11. Passe contradictoire

### A. « Impulsion nulle implique Schwartz »

**Réfuté.** L’impulsion annule seulement le premier moment antisymétrique. Le coefficient `3s𝓘_h/π` de (26) est non nul.

### B. Translation de l’impulsion

**Vérifié.** Le terme correctif est `c×∫W/2` et chaque anneau a une moyenne vectorielle nulle. L’impulsion ne dépend pas de la hauteur ou du décalage latéral.

### C. Annulation locale des vitesses

**Réfuté comme moyen d’échapper à (32).** Stokes porte sur le champ total. L’autre anneau peut annuler ponctuellement une composante, pas la circulation de chaque section positive.

### D. Dépendance de la constante en séparation

La constante inférieure explicite de (32) exige seulement que les disques `ρ≤h/2` ne rencontrent pas le tube opposé. La constante supérieure et l’énergie uniforme utilisent en plus une séparation comparable à `R`; elles peuvent dégénérer si les tubes se rapprochent à l’échelle `h`.

### E. Tubes qui se chevauchent

Les formules (9)–(12) utilisent la disjonction. Un chevauchement de signes opposés peut diminuer la vorticité pointwise et change la normalisation `K`; il n’est pas couvert.

### F. Profil sans plateau

La constante `31π²/81920κ_b³` utilise `b=1` sur `[0,1/2]`. Pour un profil seulement positif, la même preuve remplace `aπρ²` par `2πa∫₀^ρb(t/h)t dt`; une minoration subsiste sur tout intervalle où cette primitive est uniformément positive.

### G. Moment quadrupolaire accidentellement nul

L’implication universelle est seulement `I=0⇒u=O(|x|^{-4})`. L’optimalité `|x|^{-4}` est prouvée pour la paire traduite congruente avec séparation non nulle, pas pour toute paire imaginable.

### G bis. Coefficient transversal et convention de séparation

**Vérifié.** Pour `c_±=±3Re₁`, la demi-séparation vaut `a=3R` tandis que la séparation totale vaut `d=6Re₁`. Les deux écritures concordent : `Q_{112}=2d₁𝓘_h=12R𝓘_h` et le champ dominant vaut `-2a∂₁D_{𝓘_he₃}`, soit le coefficient `-9R𝓘_h/(2π)` sur le rayon `te₁`. Confondre `a` et `d` produirait un facteur deux erroné.

### H. Sortie de la classe sans swirl

Une paire coaxiale n’en sort pas. Une paire latéralement décalée en sort, mais reste petite en `L³`; casser la symétrie ne suffit pas à créer une donnée critique non dégénérée.

### I. Confusion énergie/norme critique

L’énergie de (39) et la norme critique de (36) tendent toutes deux vers zéro, avec des puissances différentes. L’enstrophie diverge; aucun de ces faits n’indique un blow-up.

### J. Pression et évolution

La pression n’est pas définie par le profil statique seul. Aucun calcul de Biot–Savart instantané ne contrôle le terme `(u·∇)u`, la diffusion ou le vortex stretching au cours du temps.

### K. Boule rencontrant les deux corridors

**Vérifié sans hypothèse de dilution.** L’inégalité (42j) vaut boule par boule. Une grande boule ne crée donc aucune interaction BMO croisée cachée. La disjonction sert à faire de (42i) une extension unitaire; la borne de semi-norme elle-même vient de la sous-additivité et reste valide pour toute boule.

## 12. Lemme canonique proposé

> **Lemme — paire torique opposée, multipôle et norme critique.** Fixons `b` comme en (1) et `σ∈(0,1/2]`. Pour `s=σR` et `0<h<σR/4`, soit `W_{h,s}` la paire (4), et soit `u_{h,s}` son champ de Biot–Savart décroissant. Alors :
>
> 1. `W_{h,s}∈C_c^∞(R³)`, `div W_{h,s}=0`, `∫W_{h,s}=0` et `I[W_{h,s}]=0`;
> 2. la quasi-norme faible vérifie exactement (10);
> 3. `u_z(Ze_z)=3s𝓘_h/(πZ⁴)+O(Z⁻⁵)`, donc `u` n’est pas de Schwartz;
> 4. pour des constantes positives dépendant seulement de `b` et `σ`, la double borne (36) vaut; la constante inférieure peut être prise égale à `31π²/(81920κ_b³)`;
> 5. la paire coaxiale engendre une vitesse axisymétrique sans swirl.

Ce lemme est cinématique et elliptique. Il ne formule aucune trajectoire singulière de Navier–Stokes.

> **Corollaire — spécialisation transverse du cycle 0029.** Pour les paramètres (42a) et la paire (42b), l’impulsion s’annule exactement, la queue vérifie (42g), l’extension directionnelle satisfait la borne all-ball (42k), et la paire n’est axisymétrique par rapport à aucun axe. Les estimations faible-`L^{3/2}` et `L³` précédentes sont invariantes par translation et restent valides.

## 13. Décision et prochain verrou

**ÉTAT : ABANDONNER la paire opposée comme mécanisme de non-dégénérescence critique.** Elle annule l’impulsion mais conserve une queue quadrupolaire et satisfait `||u||₃→0`.

Le prochain lemme minimal ne doit plus ajouter des anneaux un par un. Il doit décider si une famille de vorticités compactes peut satisfaire simultanément

\[
\|W_n\|_{L^{3/2,\infty}}\leq C,
\qquad
\inf_n\|\operatorname{BS}[W_n]\|_3>0,
\qquad
\operatorname{BS}[W_n]\in\mathcal S(\mathbb R^3),
\tag{43}
\]

tout en conservant une extension directionnelle log-BMO uniforme et en évitant les classes globalement régulières connues.

Une expérience décisive peut partir non d’une vorticité prescrite, mais d’une vitesse compacte divergence-free `u_n`, puis calculer `W_n=curl u_n`. Cette inversion impose Schwartz dès le départ et évite une cascade infinie de moments. Le test d’abandon est alors immédiat : si normaliser `||W_n||_{L^{3/2,∞}}` force encore `||u_n||₃→0`, l’axe des tubes minces est clos.

## 14. Statut de preuve

Les identités (5)–(19), (21)–(24), (29)–(32), (40)–(42d) et (42h)–(42j) sont exactes. Les expansions (25)–(26) et (42e)–(42g) sont des développements multipolaires avec reste uniforme pour un profil compact fixé. La borne (42k) dépend du lemme all-ball du tore unique du cycle 0028, dont elle double au plus la constante; elle ne réévalue pas la constante géométrique `C`. Les bornes supérieures (33)–(36) utilisent des constantes de géométrie tubulaire; les équivalences énergétiques (38)–(39) sont asymptotiques lorsque `h/R→0` à `σ` fixé.

Toutes les affirmations nouvelles restent des dérivations IA internes sans revue par les pairs, validation inter-familles ou formalisation. Aucune ne doit être étiquetée `PAPER_PROOF`.
