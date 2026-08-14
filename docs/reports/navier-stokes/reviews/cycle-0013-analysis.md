# Revue d'analyse PDE — cycle 0013

## Verdict

Le champ périodique

\[
u_a(x,y,z)
=
\bigl(\sin y+a\sin x\cos z,\ 0,\ -a\cos x\sin z\bigr),
\qquad a\in\mathbb R,
\tag{1}
\]

est lisse, de moyenne nulle et exactement divergence-free sur
\(\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3\). À l'origine,

\[
\omega_a(0)=(0,0,-1),
\qquad
\omega_a(0)\cdot S_a(0)\omega_a(0)=-a.
\tag{2}
\]

Pour \(a<0\), la vorticité est donc exactement alignée avec une direction
propre étirante de \(S_a(0)\), alors que sa direction est stationnaire au
premier ordre :

\[
\nabla\!\left(\frac{\omega_a}{|\omega_a|}\right)(0)=0.
\tag{3}
\]

Pour \(a=\pm1\), les deux champs ont les mêmes énergie, enstrophie,
hélicité globale et constantes scalaires de cohérence locale calculées
ci-dessous, mais des stretchings opposés au centre. Cela réfute exactement
l'énoncé ponctuel

\[
\boxed{
\text{invariants pairs et même cohérence locale}
\ \Longrightarrow\
\text{signe universel de }\omega\cdot S\omega.}
\tag{F}
\]

La variante qui conclurait à l'annulation du stretching est réfutée de la
même manière.

Ce n'est pas l'énoncé de Constantin–Fefferman. Leur critère contrôle, avec
des constantes uniformes en temps, les angles entre toutes les vorticités
intenses pertinentes. Il déplète une intégrale singulière non locale ; il
n'affirme pas que \(\omega\cdot S\omega\) a un signe ponctuel.

Sur un cube \(Q_r\) centré à l'origine, une borne locale explicite est
obtenue ci-dessous. Elle est forte mais insuffisante pour invoquer le
critère : elle ne concerne qu'un instant, un seul cube, et aucune évolution
Navier–Stokes n'est contrôlée.

Enfin,

\[
u_{-a}(x,y,z)=u_a(x+\pi,y,z).
\tag{4}
\]

Le changement \(a\mapsto-a\) translate le motif périodique ; il ne change
aucune statistique globale invariante par translation. L'étirement positif
à l'origine est déplacé vers une zone compressive et réciproquement.

## 1. Cadre et conventions

Le calcul porte sur le tore de période \(2\pi\), sans frontière. Pour une
fonction intégrable \(f\), on note

\[
\langle f\rangle
=\frac1{(2\pi)^3}\int_{\mathbb T^3}f(x)\,dx.
\tag{5}
\]

La convention pour le gradient est

\[
(\nabla u)_{ij}=\partial_j u_i,
\qquad
S=\frac12\bigl(\nabla u+(\nabla u)^T\bigr),
\qquad
\omega=\nabla\times u.
\tag{6}
\]

Le champ (1) est un **champ initial admissible**, pas une solution
stationnaire ou une trajectoire déjà construite. Pour \(\nu>0\), il
engendre une solution forte locale unique de Navier–Stokes périodique.
Rien dans les calculs instantanés ci-dessous ne prouve que cette solution
reste régulière globalement.

## 2. Divergence, gradient, vorticité et strain

Les deux seules contributions à la divergence sont

\[
\partial_x u_{a,1}=a\cos x\cos z,
\qquad
\partial_z u_{a,3}=-a\cos x\cos z.
\tag{7}
\]

Ainsi

\[
\nabla\cdot u_a=0.
\tag{8}
\]

Le gradient complet est

\[
\nabla u_a
=
\begin{pmatrix}
a\cos x\cos z & \cos y & -a\sin x\sin z\\
0&0&0\\
a\sin x\sin z&0&-a\cos x\cos z
\end{pmatrix}.
\tag{9}
\]

Le rotationnel vaut

\[
\boxed{
\omega_a
=
\bigl(0,\ -2a\sin x\sin z,\ -\cos y\bigr).}
\tag{10}
\]

En effet,

\[
\partial_z u_{a,1}-\partial_xu_{a,3}
=-a\sin x\sin z-a\sin x\sin z.
\tag{11}
\]

La matrice de déformation symétrique est

\[
\boxed{
S_a
=
\begin{pmatrix}
a\cos x\cos z&\frac12\cos y&0\\
\frac12\cos y&0&0\\
0&0&-a\cos x\cos z
\end{pmatrix}.}
\tag{12}
\]

Les termes \(\pm a\sin x\sin z\) de (9) sont antisymétriques et
disparaissent de \(S_a\).

Le vecteur d'étirement est exactement

\[
S_a\omega_a
=
\bigl(
-a\sin x\sin z\cos y,\
0,\
a\cos x\cos z\cos y
\bigr).
\tag{13}
\]

Comme la partie antisymétrique de \(\nabla u_a\) annihile \(\omega_a\),
(13) est aussi \((\omega_a\cdot\nabla)u_a\). La densité scalaire
d'étirement est

\[
\boxed{
\omega_a\cdot S_a\omega_a
=-a\cos x\cos z\cos^2y.}
\tag{14}
\]

À l'origine,

\[
S_a(0)
=
\begin{pmatrix}
a&1/2&0\\
1/2&0&0\\
0&0&-a
\end{pmatrix}.
\tag{15}
\]

Le vecteur \(\omega_a(0)=-e_3\) est un vecteur propre de valeur propre
\(-a\). Par conséquent :

- \(a<0\) : étirement strict, de taux \(-a>0\) ;
- \(a=0\) : taux nul ;
- \(a>0\) : compression stricte.

Les deux autres valeurs propres de \(S_a(0)\) sont

\[
\frac{a\pm\sqrt{a^2+1}}2.
\tag{16}
\]

## 3. Énergie, enstrophie et hélicité

Par orthogonalité des modes trigonométriques,

\[
\begin{aligned}
\langle|u_a|^2\rangle
&=
\langle\sin^2y\rangle
+a^2\langle\sin^2x\cos^2z\rangle
+a^2\langle\cos^2x\sin^2z\rangle\\
&=\frac12+\frac{a^2}4+\frac{a^2}4
=\frac{1+a^2}{2}.
\end{aligned}
\tag{17}
\]

Avec la convention énergie cinétique moyenne
\(E(a)=\frac12\langle|u_a|^2\rangle\),

\[
\boxed{E(a)=\frac{1+a^2}{4}.}
\tag{18}
\]

De même,

\[
\langle|\omega_a|^2\rangle
=4a^2\langle\sin^2x\sin^2z\rangle
+\langle\cos^2y\rangle
=a^2+\frac12.
\tag{19}
\]

Avec \(Z(a)=\frac12\langle|\omega_a|^2\rangle\),

\[
\boxed{Z(a)=\frac{a^2}{2}+\frac14.}
\tag{20}
\]

L'identité périodique

\[
\langle|\nabla u_a|^2\rangle
=\langle|\omega_a|^2\rangle
=a^2+\frac12
\tag{21}
\]

est satisfaite, comme attendu pour un champ divergence-free.

La densité d'hélicité est

\[
u_a\cdot\omega_a
=a\cos x\sin z\cos y.
\tag{22}
\]

Elle n'est pas identiquement nulle si \(a\neq0\), mais son intégrale est
nulle :

\[
\boxed{
H(a):=\langle u_a\cdot\omega_a\rangle=0.}
\tag{23}
\]

De même, (14) a une moyenne nulle,

\[
\langle\omega_a\cdot S_a\omega_a\rangle=0.
\tag{24}
\]

Le stretching positif est donc compensé exactement par la compression à
l'instant initial. Pour mémoire,

\[
\langle|\nabla\omega_a|^2\rangle
=2a^2+\frac12.
\tag{25}
\]

Si \(u(t)\) est la solution forte locale issue de \(u_a\), l'identité
d'enstrophie donne seulement à \(t=0\)

\[
\left.\frac{d}{dt}\frac12\langle|\omega(t)|^2\rangle
\right|_{t=0}
=-\nu\left(2a^2+\frac12\right)<0.
\tag{26}
\]

Cette dérivée initiale négative ne décide pas l'évolution ultérieure, mais
elle exclut l'inférence « stretching positif en un point donc croissance
instantanée de l'enstrophie globale » pour cette famille.

## 4. Effet exact de \(a\mapsto-a\)

L'identité (4) suit de

\[
\sin(x+\pi)=-\sin x,
\qquad
\cos(x+\pi)=-\cos x.
\tag{27}
\]

Elle entraîne

\[
\omega_{-a}(x,y,z)=\omega_a(x+\pi,y,z),
\qquad
S_{-a}(x,y,z)=S_a(x+\pi,y,z).
\tag{28}
\]

À une coordonnée fixée :

- la deuxième composante de \(\omega_a\) change de signe ;
- les entrées diagonales de \(S_a\) dépendant de \(a\) changent de signe ;
- la densité (14) change de signe ;
- la densité d'hélicité (22) change de signe.

Globalement, ces changements ne font que translater les densités. On a

\[
E(-a)=E(a),\qquad
Z(-a)=Z(a),\qquad
H(-a)=H(a)=0.
\tag{29}
\]

Comme Navier–Stokes sur le tore est invariant par translation, les
solutions fortes issues de \(u_a\) et de \(u_{-a}\) sont elles-mêmes
translatées l'une de l'autre sur leur intervalle fort commun. Le signe de
\(a\) ne fournit donc pas deux scénarios dynamiques indépendants.

## 5. Loi d'échelle périodique

Pour un entier \(N\geq1\), définissons

\[
u_{a,N}(x)=N\,u_a(Nx),
\tag{30}
\]

où \(Nx=(Nx,Ny,Nz)\) modulo \(2\pi\). La restriction
\(N\in\mathbb N\) est nécessaire pour conserver la périodicité sur le même
tore.

Les dérivées et la vorticité se transforment selon

\[
\nabla u_{a,N}(x)=N^2\nabla u_a(Nx),
\qquad
S_{a,N}(x)=N^2S_a(Nx),
\qquad
\omega_{a,N}(x)=N^2\omega_a(Nx).
\tag{31}
\]

Ainsi

\[
\nabla\cdot u_{a,N}=0
\tag{32}
\]

et

\[
\bigl(\omega_{a,N}\cdot S_{a,N}\omega_{a,N}\bigr)(x)
=N^6
\bigl(\omega_a\cdot S_a\omega_a\bigr)(Nx).
\tag{33}
\]

En particulier,

\[
\omega_{a,N}(0)\cdot S_{a,N}(0)\omega_{a,N}(0)
=-aN^6.
\tag{34}
\]

Le quotient invariant d'échelle au centre est

\[
\frac{\omega_{a,N}(0)\cdot
S_{a,N}(0)\omega_{a,N}(0)}
{|\omega_{a,N}(0)|^3}
=-a.
\tag{34a}
\]

La transformation \(x\mapsto Nx\) préserve la moyenne de toute fonction
\(2\pi\)-périodique. Il en résulte

\[
\boxed{
E_N=N^2E(a)
=N^2\frac{1+a^2}{4},}
\tag{35}
\]

\[
\boxed{
Z_N=N^4Z(a)
=N^4\left(\frac{a^2}{2}+\frac14\right),}
\tag{36}
\]

et

\[
\boxed{
H_N=N^3H(a)=0.}
\tag{37}
\]

La moyenne de la densité d'étirement reste nulle, bien que sa taille
ponctuelle soit multipliée par \(N^6\). La palinstrophie moyenne est

\[
\langle|\nabla\omega_{a,N}|^2\rangle
=N^6\left(2a^2+\frac12\right).
\tag{38}
\]

Pour une trajectoire Navier–Stokes \(u(x,t)\), la remise à l'échelle
complète est

\[
u_N(x,t)=N u(Nx,N^2t),
\qquad
p_N(x,t)=N^2p(Nx,N^2t).
\tag{39}
\]

La seule formule (30), à un instant, ne construit pas cette trajectoire.

## 6. Borne rigoureuse de cohérence sur \(Q_r\)

Soit

\[
Q_r=\{(x,y,z): |x|,|y|,|z|\leq r\}
\subset\mathbb T^3,
\qquad
0<r<\sqrt2,
\tag{40}
\]

en utilisant le relèvement centré du tore. Posons

\[
c_r=1-\frac{r^2}{2}>0.
\tag{41}
\]

Les inégalités élémentaires demandées donnent, sur \(Q_r\),

\[
|\sin x\sin z|
\leq |xz|
\leq r^2,
\qquad
\cos y\geq1-\frac{y^2}{2}\geq c_r.
\tag{42}
\]

La vorticité ne s'annule donc pas sur \(Q_r\), puisque

\[
|\omega_a(x,y,z)|\geq|\cos y|\geq c_r.
\tag{43}
\]

Les mêmes bornes donnent aussi, pour \(a\neq0\),

\[
\operatorname{sgn}(\omega_a\cdot S_a\omega_a)
=-\operatorname{sgn}(a)
\quad\text{sur }Q_r,
\qquad
|\omega_a\cdot S_a\omega_a|
\geq |a|c_r^4.
\tag{43a}
\]

Ainsi le signe et une amplitude non nulle persistent sur tout le cube
contrôlé, et pas seulement au point central.

Écrivons

\[
b(x,y,z)=-2a\sin x\sin z,
\qquad
\theta(x,y,z)=\frac{b(x,y,z)}{\cos y}.
\tag{44}
\]

Alors

\[
\xi_a:=\frac{\omega_a}{|\omega_a|}
=\frac{(0,\theta,-1)}{\sqrt{1+\theta^2}}
\tag{45}
\]

et

\[
|\theta|
\leq
\eta_r,
\qquad
\boxed{
\eta_r:=\frac{2|a|r^2}{c_r}.}
\tag{46}
\]

### Cohérence avec la direction centrale

Comme \(\xi_a(0)=-e_3\),

\[
|\xi_a(x)+e_3|^2
=2\left(1-\frac1{\sqrt{1+\theta(x)^2}}\right)
\leq\theta(x)^2.
\tag{47}
\]

Ainsi

\[
\boxed{
\sup_{Q_r}|\xi_a-\xi_a(0)|
\leq\eta_r.}
\tag{48}
\]

Pour tout niveau angulaire \(\delta>0\), la condition suffisante explicite

\[
r^2
\leq
\frac{\delta}{2|a|+\delta/2}
\tag{49}
\]

implique \(\eta_r\leq\delta\). On peut donc rendre le cône de directions
arbitrairement étroit en diminuant \(r\), sans changer la valeur
\(-a\) de l'étirement à l'origine.

### Borne uniforme paire à paire

Posons \(\phi=\arctan\theta\). Alors

\[
\xi_a=(0,\sin\phi,-\cos\phi).
\tag{50}
\]

Pour \(P,Q\in Q_r\),

\[
|\phi(P)-\phi(Q)|
\leq2\arctan\eta_r,
\tag{51}
\]

d'où la borne de corde

\[
\boxed{
|\xi_a(P)-\xi_a(Q)|
\leq
\frac{2\eta_r}{\sqrt{1+\eta_r^2}}.}
\tag{52}
\]

Cette borne est toujours inférieure à \(2\), mais elle ne contient pas la
distance \(|P-Q|\). Une borne de type Constantin–Fefferman locale s'obtient
en différentiant (44). Sur \(Q_r\),

\[
|\partial_x\theta|
\leq\frac{2|a|r}{c_r},
\qquad
|\partial_z\theta|
\leq\frac{2|a|r}{c_r},
\qquad
|\partial_y\theta|
\leq\frac{2|a|r^3}{c_r^2}.
\tag{53}
\]

Par conséquent,

\[
\|\nabla\theta\|_{L^\infty(Q_r)}
\leq
\boxed{
L_r
:=
2|a|
\sqrt{\frac{2r^2}{c_r^2}+\frac{r^6}{c_r^4}}.}
\tag{54}
\]

Le cube est convexe dans le relèvement choisi. Comme
\(|(\arctan)'|\leq1\) et que la courbe
\(\phi\mapsto(0,\sin\phi,-\cos\phi)\) est paramétrée à vitesse un,

\[
\boxed{
|\xi_a(P)-\xi_a(Q)|
\leq L_r|P-Q|,
\qquad P,Q\in Q_r.}
\tag{55}
\]

Plus directement, la formule exacte

\[
|\sin\angle(\omega_a(P),\omega_a(Q))|
=
\frac{|\theta(P)-\theta(Q)|}
{\sqrt{1+\theta(P)^2}\sqrt{1+\theta(Q)^2}}
\tag{56}
\]

donne

\[
\boxed{
|\sin\angle(\omega_a(P),\omega_a(Q))|
\leq L_r|P-Q|.}
\tag{57}
\]

Lorsque \(r\downarrow0\),

\[
\eta_r=2|a|r^2+O_a(r^4),
\qquad
L_r=2\sqrt2\,|a|r+O_a(r^3).
\tag{58}
\]

En particulier \(L_r\to0\), ce qui est cohérent avec (3). Cette excellente
cohérence **locale et instantanée** coexiste avec l'étirement positif
\(-a\) pour \(a<0\).

### Borne après remise à l'échelle

Là où elle est définie,

\[
\xi_{a,N}(x)=\xi_a(Nx).
\tag{59}
\]

Sur le cube physique \(Q_{r/N}\), (48) conserve la même ouverture
\(\eta_r\), mais (57) devient

\[
|\sin\angle(\omega_{a,N}(P),\omega_{a,N}(Q))|
\leq
N L_r|P-Q|.
\tag{60}
\]

La longueur de cohérence locale est donc divisée par \(N\). L'amplitude de
vorticité croît comme \(N^2\), l'étirement comme \(N^6\), mais le rayon du
cube contrôlé et la constante de Lipschitz se dégradent exactement sous
l'échelle. Il n'existe ici aucune borne de cohérence uniforme en \(N\).

## 7. Ce que demande réellement Constantin–Fefferman

La source primaire est P. Constantin et C. Fefferman,
[*Direction of Vorticity and the Problem of Global Regularity for the
Navier–Stokes Equations*](https://doi.org/10.1512/iumj.1993.42.42034),
Indiana University Mathematics Journal 42 (1993), 775–789.

Pour éviter d'attribuer silencieusement au papier sur \(\mathbb R^3\) une
extension de domaine, la formulation périodique auditée ici est celle
rappelée par S. Li,
[*On Vortex Alignment and Boundedness of \(L^q\) Norm of
Vorticity*](https://arxiv.org/abs/1712.00551v2), Acta Mathematica
Scientia 40B (2020), 1700–1708, équations (1.6)–(1.9).

Dans cette formulation, si \(u\) est une solution de Leray–Hopf sur
\([0,T]\), \(\omega=\nabla\times u\), et si des constantes
\(\Lambda,\rho>0\), indépendantes de \(t,x,y\), satisfont

\[
|\sin\angle(\omega(t,x),\omega(t,y))|
\leq\frac{|x-y|}{\rho}
\tag{61}
\]

pour tous les temps pertinents et chaque paire telle que

\[
|\omega(t,x)|\geq\Lambda,
\qquad
|\omega(t,y)|\geq\Lambda,
\tag{62}
\]

alors la solution faible est forte/classique. Les zéros de vorticité ne
posent pas de problème dans (61), puisqu'ils sont exclus du superniveau
(62).

Le mécanisme est non local : la représentation de \(S\) par un opérateur
singulier de Biot–Savart contient un facteur géométrique contrôlé par
\(\sin\angle(\omega(x),\omega(y))\). La cohérence adoucit le noyau dans
l'estimation intégrée de l'enstrophie. Elle ne force pas
\(\omega\cdot S\omega\leq0\) point par point.

## 8. Hypothèses non satisfaites ou non testées

Le calcul du champ (1) ne vérifie pas les hypothèses suffisantes de
Constantin–Fefferman pour les raisons distinctes suivantes.

1. **Pas de trajectoire contrôlée.** Seul l'instant initial est calculé.
   La cohérence n'est pas propagée sur \([0,T]\).
2. **Pas de contrôle du superniveau global.** (57) vaut seulement sur
   \(Q_r\), pas pour toutes les paires de points où la vorticité est
   intense sur le tore.
3. **Pas de constantes uniformes en temps.** Ni un seuil \(\Lambda\), ni
   une longueur \(\rho\) valables pendant toute l'évolution ne sont
   fournis.
4. **Pas d'uniformité multi-échelle.** Sous (30), la constante locale est
   \(NL_r\) et le cube devient \(Q_{r/N}\). Une cohérence observée après
   zoom n'est pas une cohérence uniforme dans les variables physiques.
5. **Point central non représentatif.** À l'échelle non amplifiée,
   \(|\omega_a(0)|=1\), indépendamment de \(a\). Augmenter \(|a|\)
   augmente le strain local sans rendre la vorticité centrale plus grande.
6. **Direction globale avec zéros.** Hors \(Q_r\), \(\omega_a\) s'annule
   lorsque \(\cos y=0\) et \(\sin x\sin z=0\). La direction n'y est pas
   définie. Le critère peut ignorer ces zéros seulement après avoir fixé et
   contrôlé le superniveau intense.
7. **Domaine et noyau.** La formule périodique exige le noyau périodique ou
   une extension explicitement sourcée. Un calcul local ne permet pas de
   remplacer le strain non local par son approximation dans un cube.
8. **Mauvais objet géométrique.** L'alignement de \(\omega(0)\) avec un
   vecteur propre de \(S(0)\) est un objet à un point. Constantin–Fefferman
   compare \(\omega(x)\) et \(\omega(y)\) à deux points.
9. **Hélicité.** L'hélicité globale nulle (23) n'est ni l'hypothèse ni la
   conclusion du critère. Elle n'interdit pas une densité d'hélicité ou un
   stretching locaux non nuls.
10. **Signe local.** Le critère borne un terme intégré après compensation
    non locale. La positivité de (2) n'est pas un contre-exemple au
    théorème.

## 9. Passe contradictoire

### Faux énoncé effectivement réfuté

L'énoncé (F) est faux. Pour tout \(A>0\), la paire
\((u_A,u_{-A})\) a les mêmes valeurs (18), (20), (23), et les mêmes
constantes (46), (54), qui ne dépendent que de \(|a|=A\). Pourtant,

\[
(\omega_A\cdot S_A\omega_A)(0)=-A,
\qquad
(\omega_{-A}\cdot S_{-A}\omega_{-A})(0)=A.
\tag{62a}
\]

La réfutation subsiste sous une version renforcée au point central : pour
tout \(a<0\),

\[
\xi_a(0)=-e_3,
\qquad
\nabla\xi_a(0)=0,
\qquad
\omega_a(0)\cdot S_a(0)\omega_a(0)=-a>0.
\tag{63}
\]

En prenant \(a\to-\infty\), le stretching ponctuel devient arbitrairement
grand alors que la dérivée première de la direction reste exactement
nulle au point. Cela exclut toute borne ponctuelle du stretching qui ne
dépendrait que de \(\xi(0)\) et de \(\nabla\xi(0)\).

La taille du voisinage contrôlé n'est toutefois pas uniforme en \(a\).
Les constantes (46) et (54) enregistrent exactement cette perte. On ne
peut donc pas promouvoir (63) en contre-exemple à un critère global de
cohérence avec échelle fixée.

### Autres inférences éliminées

1. **Changer le signe crée deux mécanismes globaux.** Faux par (4).
2. **Stretching ponctuel positif implique production globale positive.**
   Faux à l'instant initial par (24)–(26).
3. **Grande amplitude après scaling préserve la même cohérence physique.**
   Faux par (60).
4. **Direction presque constante dans un cube implique régularité.**
   Non démontré : il manque le superniveau complet et toute la durée.
5. **Hélicité globale nulle implique absence de stretching.** Faux par
   (14) et (23).
6. **Un champ divergence-free est déjà une solution Navier–Stokes.**
   Faux : il est seulement une donnée initiale avant résolution de
   l'équation et de la pression.

## Conclusion

**Résultat positif borné.** Toutes les quantités demandées sont calculées
exactement. Sur \(Q_r\), la vorticité ne s'annule pas et satisfait les
bounds (48), (52) et la borne paire à paire de type Lipschitz (57), avec
les constantes explicites (41), (46) et (54).

**Résultat négatif.** La cohérence de direction au voisinage d'un point ne
contrôle ni le signe ni la taille du stretching en ce point. La famille
\(a<0\) réfute exactement ce raccourci, mais ne réfute pas
Constantin–Fefferman.

**Écart avec Clay.** Le champ est une donnée périodique lisse. Aucun
blow-up, aucune borne globale et aucune propagation temporelle de la
cohérence ne sont obtenus. La transformation \(u_{a,N}=Nu_a(Nx)\)
augmente les amplitudes en dégradant simultanément la longueur de
cohérence ; elle ne ferme aucune estimation critique uniforme.

**État : ABANDONNER** l'usage de l'alignement ou du stretching en un point
comme proxy du critère géométrique. **CONTINUER** seulement avec une
expérience évolutive qui suit, sur tout le superniveau
\(\{|\omega|\geq\Lambda\}\), la meilleure constante paire à paire de
(61), le stretching intégré et leur dépendance en \(N\), avec erreurs de
discrétisation certifiées.
