# Cycle 0043 — haute fréquence contre norme positive du commutateur

Date d'audit : 2026-08-15.

## Verdict

Une famille lisse, compacte et divergence-free

\[
U_N=\varepsilon\,\phi(r,z)\sin(Nz)\,e_\theta
\]

sur une couronne torique évitant l'axe vérifie simultanément :

\[
\nabla\cdot U_N=0,\qquad
\nabla\chi\cdot U_N=0,\qquad
\nabla\chi\cdot\Delta U_N=0,
\]

pour un cutoff \(\chi\) radial autour d'un centre situé sur l'axe. Par conséquent, pour toute réalisation linéaire de Bogovskiĭ dans la localisation

\[
Qw=\chi w-\mathcal B(\nabla\chi\cdot w),
\]

on a exactement

\[
[\Delta,Q]U_N=[\Delta,\chi]U_N.
\]

La norme positive \(L^2\) de ce commutateur croît comme \(N\). En revanche, le même terme admet l'identité

\[
[\Delta,\chi]U_N=f_{0,N}+\operatorname{div}G_{0,N},
\]

avec des budgets \(L^1+ \operatorname{div}L^{3/2,\infty}\) indépendants de \(N\). Le test distingue donc une croissance forte réelle d'une croissance qui disparaît lorsqu'une dérivée est transférée sur le test.

Ce calcul ne simule pas Navier–Stokes et ne prouve aucune borne pour la force localisée complète.

## Géométrie fixée

Utilisons les coordonnées cylindriques \((r,\theta,z)\) et le centre de cutoff

\[
x_c=(0,0,-1),\qquad
\rho=\sqrt{r^2+(z+1)^2},\qquad
\chi(x)=\chi_*(\rho).
\]

On choisit \(\chi_*\in C_c^\infty([0,\infty))\), constante près du coeur, et exactement affine avec

\[
\chi_*'=-1,\qquad \chi_*''=0
\]

sur \(6/5\leq\rho\leq7/4\). Une telle fonction existe en raccordant l'intervalle affine à des transitions plates fixes.

La fonction \(0\leq\phi\leq1\) est \(C_c^\infty\), supportée dans

\[
S=\{1<r<5/4,\ |z|<1/8\},
\]

et égale à un sur

\[
P=\{17/16\leq r\leq19/16,\ |z|\leq1/16\}.
\]

Sur \(S\),

\[
\frac{113}{64}<\rho^2<\frac{181}{64},
\]

donc \(S\) est strictement contenu dans la zone affine du cutoff et reste à distance positive de l'axe. L'écriture cartésienne de \(e_\theta\) est alors lisse sur un voisinage du support.

## Divergence et annulation du correcteur

Le champ \(U_N\) n'a que la composante azimutale, indépendante de \(\theta\). Ainsi

\[
\nabla\cdot U_N
=\frac1r\partial_\theta(U_N)_\theta=0.
\]

Le vecteur \(a:=\nabla\chi\) appartient au plan engendré par \(e_r,e_z\), d'où

\[
a\cdot U_N=0.
\]

Le laplacien vectoriel d'un swirl axisymétrique reste un swirl axisymétrique :

\[
\Delta(qe_\theta)
=\left(\partial_r^2q+\frac1r\partial_rq+\partial_z^2q-\frac{q}{r^2}\right)e_\theta.
\]

Par conséquent \(a\cdot\Delta U_N=0\). Les entrées de Bogovskiĭ dans \(QU_N\) et \(Q\Delta U_N\) sont toutes deux nulles, indépendamment de la formule choisie pour \(\mathcal B\). Cela justifie l'identité complète

\[
\Delta(QU_N)-Q(\Delta U_N)
=\Delta(\chi U_N)-\chi\Delta U_N.
\]

## Croissance dans une norme positive

La règle de Leibniz donne

\[
C_N:=[\Delta,\chi]U_N
=(\Delta\chi)U_N+2\nabla\chi\cdot\nabla U_N.
\]

Sur \(P\), \(\phi=1\). Comme \(\chi_*'=-1\),

\[
\partial_z\chi=-\frac{z+1}{\rho},
\qquad
\Delta\chi=-\frac2\rho.
\]

Les bornes géométriques rationnelles

\[
|\partial_z\chi|>\frac12,\qquad
|\Delta\chi|\leq\frac85
\]

donnent

\[
C_N
=\varepsilon\left[
(\Delta\chi)\sin(Nz)
+2N(\partial_z\chi)\cos(Nz)
\right]e_\theta.
\]

Sur \(I=[-1/16,1/16]\),

\[
\int_I\cos^2(Nz)\,dz
=\frac1{16}+\frac{\sin(N/8)}{2N}
\geq\frac1{32}
\quad(N\geq16).
\]

De plus

\[
\int_{17/16}^{19/16}r\,dr=\frac9{64}.
\]

En utilisant uniquement \(3<\pi<22/7\), on obtient

\[
\|\cos(Nz)\|_{L^2(P)}>\frac5{32},
\qquad
|P|<\frac19.
\]

L'inégalité triangulaire fournit donc la minoration explicite

\[
\boxed{
\|C_N\|_{L^2(\mathbb R^3)}
\geq
\varepsilon\left(\frac{5N}{32}-\frac8{15}\right),
\qquad N\geq16.}
\]

Elle est positive dès \(N=16\) et supérieure à \(\varepsilon N/8\) pour \(N\geq32\).

Réciproquement, puisque les profils \(\phi,\chi\) sont fixes,

\[
|C_N|
\leq\varepsilon\left(\frac85+2\|\nabla\phi\|_\infty+2N\right)
\mathbf1_S.
\]

La norme \(L^2\) est donc \(O(\varepsilon N)\). Ensemble avec la minoration, ceci certifie une croissance \(\Theta(\varepsilon N)\), sans annulation signée.

## Représentation faible uniforme

Avec la convention

\[
(\operatorname{div}G)_i=\partial_jG_{ij},
\]

posons

\[
f_{0,N}=-(\Delta\chi)U_N,
\qquad
(G_{0,N})_{ij}=2(U_N)_i\partial_j\chi.
\]

La règle du produit donne exactement

\[
\operatorname{div}G_{0,N}
=2(\Delta\chi)U_N+2\nabla\chi\cdot\nabla U_N,
\]

et donc

\[
\boxed{
[\Delta,\chi]U_N=f_{0,N}+\operatorname{div}G_{0,N}.}
\]

La dérivée axiale \(N\cos(Nz)\) n'a pas disparu : elle est portée par la divergence distributionnelle et agit désormais sur la fonction test. Les coefficients \(f_{0,N}\) et \(G_{0,N}\), eux, ne contiennent aucune dérivée de \(U_N\).

Le volume du support vérifie

\[
|S|=\frac{9\pi}{64}<\frac{99}{224}<\frac12.
\]

Puisque \(|U_N|\leq\varepsilon\), \(|\nabla\chi|=1\) et \(|\Delta\chi|\leq8/5\) sur \(S\),

\[
\boxed{
\|f_{0,N}\|_{L^1}
\leq\frac{99}{140}\varepsilon,}
\]

et l'inclusion élémentaire d'un champ borné supporté sur un ensemble de mesure finie donne

\[
\boxed{
\|G_{0,N}\|_{L^{3/2,\infty}}
\leq\frac85\varepsilon.}
\]

Ces deux bornes sont uniformes en \(N\). Elles établissent pour ce commutateur particulier le budget demandé dans

\[
L^1+\operatorname{div}L^{3/2,\infty}.
\]

Elles ne donnent pas une borne uniforme de \(C_N\) comme fonction positive, ni une petite norme : les coefficients restent d'ordre \(\varepsilon\).

## Profil à correction de Bogovskiĭ nécessaire

La non-nullité du correcteur peut être certifiée sans choisir une formule de droite inverse. Prenons une fonction de courant axisymétrique compacte qui coïncide localement avec

\[
\Psi(r,z)=rz
\]

près de \((r,z)=(3/4,0)\), et définissons

\[
W_r=-\frac1r\partial_z\Psi,\qquad
W_z=\frac1r\partial_r\Psi,\qquad W_\theta=0.
\]

L'égalité des dérivées mixtes donne \(\nabla\cdot W=0\). Au point choisi,

\[
\rho=\frac54,\qquad
W_r=-1,\qquad W_z=0,
\]

et

\[
\nabla\chi=\left(-\frac35,0,-\frac45\right)
\quad\text{dans la base }(e_r,e_\theta,e_z).
\]

Ainsi

\[
g:=\nabla\chi\cdot W=\frac35\ne0.
\]

Comme \(g=\operatorname{div}(\chi W)\) est compact, sa moyenne globale est nulle et il est admissible pour Bogovskiĭ. Toute droite inverse satisfaisant

\[
\operatorname{div}\mathcal Bg=g
\]

produit nécessairement \(\mathcal Bg\ne0\). Cette non-nullité est indépendante du choix de \(\mathcal B\).

La limite exacte est la suivante : la valeur ponctuelle, la direction, la norme inférieure et les commutateurs de \(\mathcal Bg\) ne sont pas canoniques tant qu'une réalisation de Bogovskiĭ n'est pas fixée. Deux droites inverses peuvent différer d'un opérateur à valeurs divergence-free. Le présent test certifie donc l'activation du correcteur, mais pas son interaction quantitative avec les autres termes.

## Portée adverse

Le test établit :

1. une norme positive du commutateur peut diverger comme \(N\) sous une amplitude critique uniformément bornée ;
2. sur cette même famille, le budget négatif \(L^1+\operatorname{div}L^{3/2,\infty}\) reste uniforme ;
3. une estimation terme par terme en norme positive perd artificiellement la structure de divergence ;
4. cette réparation ne contrôle encore ni la pression, ni le terme mobile, ni le défaut non linéaire, ni la somme projetée complète.

Il serait donc incorrect de conclure soit que la force complète diverge, soit qu'elle est uniformément contrôlée, à partir du seul commutateur visqueux.

## Reproduction

~~~powershell
python -B experiments/navier-stokes/moving-commutator/moving_commutator_audit.py
~~~

Le programme utilise uniquement la bibliothèque standard et fractions.Fraction. Il vérifie les inclusions géométriques, la divergence, l'annulation des deux entrées de Bogovskiĭ, l'identité des coefficients sinus/cosinus, la minoration \(L^2\), les budgets uniformes et le témoin de correction non nulle.

Statut : **CONTINUER**. La prochaine expérience décisive doit appliquer la même décomposition à la somme de la dérivée mobile, du commutateur visqueux, du défaut quadratique et de la pression projetée, afin de détecter une éventuelle annulation ou une obstruction qui survive dans \(L^1+\operatorname{div}L^{3/2,\infty}\).
