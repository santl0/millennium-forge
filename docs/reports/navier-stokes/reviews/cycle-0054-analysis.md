# Cycle 0054 — conjugaison du flux de temps de base

Date : 2026-08-15.

Statut : `AI_INTERNAL_DERIVATION`; audit algébrique et fonctionnel
indépendant, sans résultat Clay et sans calcul numérique.

## Verdict

La conjugaison est exacte, avec les signes et facteurs suivants. Soit
\(\kappa>0\), \(x_0\in\mathbb R^3\),

\[
 \rho(s)=e^{-\kappa s},\qquad
 t(s)=\frac{1-\rho(s)^2}{2\kappa},\qquad s\leq0,            \tag{1}
\]

et

\[
 (T_\rho f)(x)=\rho^{-1}f\!\left(\frac{x-x_0}{\rho}\right).
                                                               \tag{2}
\]

Si \(Z\) résout l'équation renormalisée projetée

\[
 \partial_sZ-\Delta Z+\kappa DZ
 +\mathbb P\operatorname{div}(Z\otimes Z)=0,
 \qquad D=1+y\cdot\nabla_y,                    \tag{3}
\]

alors \(v(t(s))=T_\rho Z(s)\) résout Navier--Stokes standard. Pour
\(S(h)=e^{h\Delta}\), \(a>0\), posons

\[
 A_s=\frac{1-\rho^{-2}}{2\kappa},\qquad
 B_s=A_s+\frac a{\rho^2}.                       \tag{4}
\]

On a exactement

\[
 A_s=\frac{-t(s)}{\rho^2},\qquad
 B_s=\frac{a-t(s)}{\rho^2},                    \tag{5}
\]

et

\[
 S(a-t(s))v(t(s))=T_\rho S(B_s)Z(s).            \tag{6}
\]

Ainsi, si

\[
 G_a(s)=S(a)\,[v(0)-S(-t(s))v(t(s))],           \tag{7}
\]

alors, dans les distributions tempérées et dans la classe \(L^2\) du
correcteur,

\[
 G_a(s)=S(a)v(0)-T_\rho S(B_s)Z(s),             \tag{8}
\]

et, pour presque tout \(s<0\),

\[
 \boxed{
 \partial_sG_a(s)
 =T_\rho S(B_s)\mathbb P\operatorname{div}(Z\otimes Z)(s)
 =\rho^2S(a-t(s))\mathbb P\operatorname{div}(v\otimes v)(t(s)).}
                                                               \tag{9}
\]

Avec

\[
\begin{aligned}
 I_a(t)&=2\int_{\mathbb R^3}(v\otimes v)(t):
 \nabla S(a-t)G_a(t)\,dx,\\
 J_a(s)&=\rho(s)^2I_a(t(s)),
\end{aligned}                                                  \tag{10}
\]

le signe et le facteur exacts sont

\[
 \boxed{
 \frac d{ds}\|G_a(s)\|_2^2=-J_a(s)
 =-\rho(s)^2I_a(t(s)).}                         \tag{11}
\]

Le facteur \(\rho^2=dt/ds\) ne peut être absorbé dans la définition de
\(I_a\) si l'on veut conserver le flux du cycle 0052 par unité de temps
physique. Le défaut \(D_R\) du cycle 0053 ne contrôle ni \(I_a\), ni
\(J_a\) : il ne mesure que \(\partial_sZ\) localement, tandis que (9) mesure
le bilan elliptique--drift--non linéaire global après lissage. En particulier,
le terme de conjugaison ne se réduit jamais à
\(T_\rho S(B_s)\partial_sZ\).

## 1. Horloge et temps calorifiques

Les dérivées de l'horloge sont

\[
 \rho_s=-\kappa\rho,\qquad
 t_s=-\frac{2\rho\rho_s}{2\kappa}=\rho^2>0.     \tag{12}
\]

La carte \(s\mapsto t(s)\) est donc un difféomorphisme croissant de
\(( -\infty,0]\) sur \(( -\infty,0]\). Ses extrémités sont

\[
 s=0:\ \rho=1,\ t=0;\qquad
 s\to-\infty:\ \rho\to\infty,\ t\to-\infty.  \tag{13}
\]

Puisque

\[
 -t(s)=\frac{\rho^2-1}{2\kappa},                \tag{14}
\]

la première identité de (5) est immédiate. La loi de conjugaison du
semi-groupe sous une translation-dilatation isotrope est

\[
 S_x(h)T_\rho=T_\rho S_y(h/\rho^2),\qquad h\geq0.           \tag{15}
\]

Elle donne successivement

\[
 S(-t)v(t)=T_\rho S(A_s)Z(s),                   \tag{16}
\]

puis

\[
 S(a)S(-t)v(t)
 =S(a-t)T_\rho Z
 =T_\rho S((a-t)/\rho^2)Z.                     \tag{17}
\]

Par conséquent le temps de chaleur de (17) est bien

\[
 \boxed{B_s=\frac{a-t}{\rho^2}
 =A_s+\frac a{\rho^2}.}                        \tag{18}
\]

Il satisfait les identités utiles

\[
\begin{aligned}
 B_s&=\frac1{2\kappa}
 +\left(a-\frac1{2\kappa}\right)\rho^{-2},\\
 B_s'&=(2\kappa a-1)\rho^{-2}=2\kappa B_s-1,  \tag{19}\\
 \min\{a,(2\kappa)^{-1}\}
 &\leq B_s\leq\max\{a,(2\kappa)^{-1}\}.
\end{aligned}
\]

En particulier, \(B_s\) reste strictement positif et borné en temps
renormalisé; il ne tend ni vers zéro, ni vers l'infini lorsque
\(s\to-\infty\). Le lissage physique \(a-t=\rho^2B_s\), lui, croît comme
\(\rho^2/(2\kappa)\).

À la tranche terminale,

\[
 A_0=0,\qquad B_0=a,                            \tag{20}
\]

de sorte que les deux termes de (8) coïncident et \(G_a(0)=0\).

## 2. Dérivée de la dilatation

Pour une famille régulière \(f(s,y)\), avec
\(y=(x-x_0)/\rho(s)\), on a \(y_s=\kappa y\). Un calcul composante par
composante donne

\[
\begin{aligned}
 \partial_s[T_\rho f(s)](x)
 &=\rho^{-1}\bigl(\partial_sf+\kappa f
                   +\kappa y\cdot\nabla f\bigr)(s,y)\\
 &=T_\rho(\partial_s+\kappa D)f.                \tag{21}
\end{aligned}
\]

Le signe devant \(\kappa D\) est positif : il provient du signe négatif de
\(\rho_s\) à la fois dans l'amplitude \(\rho^{-1}\) et dans la variable
\(y=x/\rho\).

## 3. Commutateur du générateur avec la chaleur

Le générateur est \(D=1+y\cdot\nabla\). Puisque

\[
 \Delta(y\cdot\nabla f)=y\cdot\nabla\Delta f+2\Delta f,
                                                               \tag{22}
\]

on obtient, avec la convention \([A,B]=AB-BA\),

\[
 \boxed{[D,\Delta]=-2\Delta,\qquad [\Delta,D]=2\Delta.}   \tag{23}
\]

La version semi-groupe est

\[
 D S(B)=S(B)D-2B\Delta S(B).                   \tag{24}
\]

Le terme constant \(1\) dans \(D\) commute avec \(\Delta\), mais il est
indispensable dans (21) et dans l'équation. Une convention opposée pour le
commutateur sans modification de (24) inverserait le signe calorifique.

## 4. Dérivée exacte de \(T_\rho S(B_s)Z\)

Posons

\[
 H(s)=T_\rho S(B_s)Z(s).                       \tag{25}
\]

Les équations (21), (24) et \(B_s'-2\kappa B_s=-1\) donnent

\[
\begin{aligned}
 \partial_sH
 &=T_\rho(\partial_s+\kappa D)[S(B_s)Z]\\
 &=T_\rho\Bigl[
 S(B_s)(\partial_sZ+\kappa DZ)
 +(B_s'-2\kappa B_s)\Delta S(B_s)Z\Bigr]\\
 &=T_\rho S(B_s)(\partial_sZ-\Delta Z+\kappa DZ).          \tag{26}
\end{aligned}
\]

La combinaison \(-\Delta Z+\kappa DZ\) est donc créée par la dérivée de la
dilatation et du temps de chaleur. Le seul terme \(\partial_sZ\) n'est pas
la dérivée conjuguée.

En appliquant la projection de Leray à (3),

\[
 \partial_sZ-\Delta Z+\kappa DZ
 =-\mathbb P\operatorname{div}(Z\otimes Z),     \tag{27}
\]

donc

\[
 \boxed{
 \partial_s[T_\rho S(B_s)Z]
 =-T_\rho S(B_s)\mathbb P\operatorname{div}(Z\otimes Z).} \tag{28}
\]

Comme le premier terme de (8) est indépendant de \(s\), son signe s'inverse
une seconde fois et donne le premier membre de (9).

Une vérification indépendante part directement de la variable physique :

\[
\begin{aligned}
 \frac d{dt}[S(a-t)v(t)]
 &=S(a-t)(\partial_tv-\Delta v)\\
 &=-S(a-t)\mathbb P\operatorname{div}(v\otimes v),         \tag{29}
\end{aligned}
\]

puis \(G_a=S(a)v(0)-S(a-t)v(t)\) et \(dt/ds=\rho^2\). Cela
redonne le signe positif et le facteur \(\rho^2\) de (9).

## 5. Échelle du terme projeté et pression

À temps correspondant,

\[
 v(x,t)=\rho^{-1}Z(y,s),\qquad
 q(x,t)=\rho^{-2}\Pi(y,s),qquad
 y=\frac{x-x_0}{\rho}.                          \tag{30}
\]

Ainsi

\[
 (v\otimes v)(x,t)=\rho^{-2}(Z\otimes Z)(y,s)              \tag{31}
\]

et, puisque la projection de Leray est un multiplicateur homogène de degré
zéro et commute avec les translations,

\[
 \mathbb P_x\operatorname{div}_x(v\otimes v)
 =\rho^{-3}
 [\mathbb P_y\operatorname{div}_y(Z\otimes Z)](y)
 =\rho^{-2}T_\rho\mathbb P_y\operatorname{div}_y(Z\otimes Z).
                                                               \tag{32}
\]

En combinant (15), (18) et (32),

\[
 \rho^2S_x(a-t)\mathbb P_x\operatorname{div}_x(v\otimes v)
 =T_\rho S_y(B_s)\mathbb P_y\operatorname{div}_y(Z\otimes Z),
                                                               \tag{33}
\]

ce qui vérifie le second membre de (9), facteur compris.

Dans la jauge globale de Riesz,

\[
 \Pi=R_iR_j(Z_iZ_j),\qquad q=R_iR_j(v_iv_j),                \tag{34}
\]

et (30) est compatible avec (34), car les doubles transformées de Riesz
sont homogènes de degré zéro. En outre,

\[
 \operatorname{div}(Z\otimes Z)+\nabla\Pi
 =\mathbb P\operatorname{div}(Z\otimes Z).      \tag{35}
\]

La projection dans (27)--(33) n'omet donc pas la pression; elle la fixe. Avec
une pression seulement locale, modulo une fonction harmonique non contrôlée,
la formulation projetée globale demanderait un lemme supplémentaire.

## 6. Espaces de définition et pairing du flux

Le cadre du cycle 0052 donne

\[
 v(t)\in L^{3,\infty},\qquad
 F(t)=v(t)\otimes v(t)\in L^{3/2,\infty},        \tag{36}
\]

uniformément en \(t\leq0\). Pour \(h=a-t>0\),

\[
 \|S(h)\mathbb P\operatorname{div}F\|_2
 \leq C h^{-3/4}\|F\|_{3/2,\infty}.            \tag{37}
\]

Il en résulte que \(G_a\in AC_{\rm loc}(( -\infty,0];L^2)\) en temps
physique et renormalisé. En variable \(s\),

\[
 \|\partial_sG_a(s)\|_2
 \leq C\rho^2(a-t)^{-3/4}M^2.                  \tag{38}
\]

Cette borne est locale en \(s\), mais pas intégrable uniformément vers
\(-\infty\) : puisque \(a-t\simeq c_\kappa\rho^2\), son membre droit est
d'ordre \(\rho^{1/2}\).

Il faut aussi éviter une fausse décomposition \(L^2\). Les deux termes
\(S(a)v(0)\) et \(T_\rho S(B_s)Z(s)\) de (8) ne sont pas nécessairement
dans \(L^2(\mathbb R^3)\) séparément. Leur différence l'est par la formule
de Duhamel lissée. L'identité (8) est d'abord une identité de distributions
tempérées, puis une identité pour ce correcteur \(L^2\).

Le champ \(G_a\) est solénoïdal. Le noyau calorifique donne

\[
 \|\nabla S(a-t)G_a\|_{L^{3,1}}
 \leq C(a-t)^{-3/4}\|G_a\|_2.                 \tag{39}
\]

La dualité exacte
\(L^{3/2,\infty}\)--\(L^{3,1}\) rend donc l'intégrale de (10)
absolument convergente. L'auto-adjonction de \(S\) et de \(\mathbb P\),
puis l'intégration par parties, donnent

\[
\begin{aligned}
 \frac d{ds}\|G_a\|_2^2
 &=2\rho^2\langle G_a,
 S(a-t)\mathbb P\operatorname{div}F\rangle\\
 &=-2\rho^2\int F:\nabla S(a-t)G_a\,dx,
                                                               \tag{40}
\end{aligned}
\]

soit (11). Le signe négatif apparaît seulement à l'intégration par parties;
la dérivée de \(G_a\) dans (9) est positive devant le terme projeté.

Comme \(G_a(0)=0\), l'intégration sur une bande finie donne aussi, sans
changer d'orientation,

\[
 \|G_a(s)\|_2^2
 =\int_s^0J_a(\sigma)\,d\sigma
 =\int_{t(s)}^0I_a(\tau)\,d\tau.                \tag{40a}
\]

Cette primitive est non négative, mais ses densités \(I_a\) et \(J_a\)
peuvent changer de signe.

La pression explicite donnerait
\(\int q\,\operatorname{div}S(a-t)G_a=0\). Cette annulation est licite
globalement grâce à (34), (39) et la solénoïdalité; elle ne doit pas être
inférée d'une pression locale non normalisée.

## 7. Le second temps de chaleur dans le flux

Posons le correcteur non lissé

\[
 g(t)=v(0)-S(-t)v(t),\qquad G_a(t)=S(a)g(t).      \tag{41}
\]

Le test effectif du stress dans (10) est

\[
 S(a-t)G_a=S(2a-t)g.                            \tag{42}
\]

Il contient donc deux occurrences de \(a\), comme au cycle 0052. Dans les
variables renormalisées, si

\[
 \widetilde g_s=T_\rho^{-1}g(t(s)),\qquad
 C_s=\frac{2a-t(s)}{\rho^2},                    \tag{43}
\]

alors

\[
 C_s=A_s+\frac{2a}{\rho^2}=B_s+\frac a{\rho^2},             \tag{44}
\]

et

\[
 I_a(t(s))
 =2\rho^{-1}\int_{\mathbb R^3}(Z\otimes Z)(s):
 \nabla_yS(C_s)\widetilde g_s\,dy,              \tag{45}
\]

donc

\[
 J_a(s)
 =2\rho\int_{\mathbb R^3}(Z\otimes Z)(s):
 \nabla_yS(C_s)\widetilde g_s\,dy.              \tag{46}
\]

Les facteurs de (45) viennent de
\(dx=\rho^3dy\), \(v\otimes v=\rho^{-2}Z\otimes Z\) et
\(\nabla_x[T_\rho f]=\rho^{-2}(\nabla_y f)((x-x_0)/\rho)\). Écrire \(B_s\)
à la place de \(C_s\) dans le test final oublierait le lissage déjà présent
dans \(G_a\).

## 8. Ce que le défaut \(D_R\) peut et ne peut pas impliquer

Le cycle 0053 définit

\[
 D_R(s)=\int_{s-1}^{s}
 \|\partial_\sigma Z(\sigma)\|_{(W^{1,3}_0(B_R))^*}\,d\sigma. \tag{47}
\]

Sous suitability locale, (47) est bien défini. Il mesure une variation
temporelle renormalisée **locale**, sur une fenêtre et une boule fixes.
L'identité non projetée avant usage de la PDE est toutefois

\[
 \partial_s[T_\rho S(B_s)Z]
 =T_\rho S(B_s)(\partial_sZ-\Delta Z+\kappa DZ).            \tag{48}
\]

Ainsi une petitesse de \(\partial_sZ\) ne rend pas le membre gauche petit :
les termes \(-\Delta Z\) et \(\kappa DZ\) subsistent et, pour une solution,
ils se combinent avec le stress selon (27).

Plus précisément, \(D_R(s_n)\to0\) pour tout \(R\) peut, avec la compacité
forte locale et la capture persistante, produire une limite stationnaire et
la contradiction de Guevara--Phuc décrite au cycle 0053. Mais cette hypothèse
ne donne pas :

- \(I_a(t(s_n))\to0\) ou \(J_a(s_n)\to0\), car (47) est une norme intégrée
  sur une fenêtre tandis que le flux est une valeur presque partout à un
  instant;
- une borne globale de \(T_\rho S(B_s)\mathbb P\operatorname{div}(Z\otimes
  Z)\), car \(D_R\) est local en \(y\) et le noyau calorifique ainsi que
  \(\mathbb P\) sont non locaux;
- un taux uniforme en \(R\) capable de compenser \(\rho_n\to\infty\);
- l'annulation du bilan stationnaire
  \(-\Delta U+\kappa DU+\mathbb P\operatorname{div}(U\otimes U)=0\) terme
  par terme;
- un signe pour le pairing scalaire (10).

Le point d'échelle est particulièrement défavorable à une telle déduction :
\(B_{s_n}\to(2\kappa)^{-1}\), donc le lissage reste à une échelle finie
dans les coordonnées \(y\), tandis que \(J_a\) conserve le facteur
\(\rho_n^2\). La convergence locale sans taux du cycle 0053 ne neutralise
pas ce facteur.

Réciproquement, \(J_a(s)=0\) est une seule orthogonalité signée entre le
stress et un test dépendant de toute la trajectoire terminale. Elle n'implique
aucune petitesse de la norme de \(\partial_sZ\) dans (47). Même une intégrale
signée bornée de \(J_a\) peut résulter de cancellations et ne contrôle pas sa
variation absolue.

Enfin, sous la capture persistante et les autres hypothèses du cycle 0053,
une suite satisfaisant \(D_R(s_n)\to0\) pour tout \(R\) est précisément
exclue. Elle ne peut donc pas servir ensuite, sans contradiction, de suite
de temps de base pour fermer le critère de flux du cycle 0052.

## 9. Quantificateurs exacts

Les conclusions précédentes portent sur :

\[
 \kappa>0,\quad x_0\in\mathbb R^3,\quad a>0
 \quad\text{fixés avant de faire varier }s.      \tag{49}
\]

Les identités (5)--(8), (18)--(28) valent distributionnellement pour tout
\(s\leq0\) où les représentants sont définis. Les dérivées (9)--(11) et
(40) valent pour presque tout \(s<0\); leurs formes intégrées valent sur
toute bande finie par absolue continuité. Aucune intégrabilité de
\(J_a\) sur \(( -\infty,0)\), aucune limite impropre et aucune convergence
ponctuelle le long d'une suite ne suivent de l'identité seule.

Le paramètre \(a\) doit rester fixe en temps physique. Le paramètre
renormalisé correspondant \(a/\rho^2\) varie; le remplacer par une constante
dans (4) changerait le filtre physique et détruirait
\(B_s'-2\kappa B_s=-1\).

## 10. Passe contradictoire

1. **Mauvais temps de chaleur.** \(A_s=-t/\rho^2\), non \(-t\), et
   \(B_s=A_s+a/\rho^2\), non \(A_s+a\). Le semi-groupe se dilate comme un
   temps quadratique.
2. **Dérivée de \(B_s\).** La bonne identité est
   \(B_s'=2\kappa B_s-1\). Omettre la dérivée de \(a/\rho^2\) laisse un
   résidu \(2\kappa a/\rho^2\).
3. **Commutateur.** Avec \([A,B]=AB-BA\),
   \([D,\Delta]=-2\Delta\). Employer \(+2\Delta\) dans (24) inverse le
   terme \(-\Delta Z\) de (26).
4. **Dilatation temporelle.** La dérivée de \(T_\rho\) est
   \(T_\rho(\partial_s+\kappa D)\), pas
   \(T_\rho(\partial_s-\kappa D)\). Le centre \(x_0\) doit être fixe; un
   centre mobile ajouterait un terme de transport.
5. **Signe non linéaire.** \(H_s\) porte un signe négatif par (27), puis
   \(G_a=S(a)v(0)-H\) le renverse. Le signe du flux énergétique redevient
   négatif seulement après intégration par parties.
6. **Jacobian temporel.** \(dt/ds=\rho^2\), donc
   \(J_a=\rho^2I_a\). Une formule \(J_a=I_a\) compare des densités par deux
   horloges différentes.
7. **Double lissage.** La dérivée de \(G_a\) utilise \(B_s\), mais le test
   énergétique utilise \(C_s=B_s+a/\rho^2\), puisque \(G_a=S(a)g\).
8. **Fausse séparabilité \(L^2\).** Les deux termes de (8) peuvent avoir une
   norme \(L^2\) infinie séparément. Seule leur différence lissée est acquise
   dans \(L^2\).
9. **Pression.** Elle disparaît uniquement après jauge de Riesz/projection et
   test solénoïdal dans la dualité
   \(L^{3/2,\infty}\)--\(L^{3,1}\).
10. **Dérivée locale contre flux global.** \(D_R\) ne contrôle ni les queues
    du stress, ni la projection de Leray, ni le facteur \(\rho^2\), ni le
    pairing signé avec \(G_a\).
11. **Temps exceptionnel.** Le flux instantané est défini presque partout;
    un choix arbitraire de \(s_n\) peut tomber sur des représentants
    exceptionnels. Les identités intégrées évitent ce défaut, mais ne
    produisent pas de petitesse.
12. **Portée Clay.** La conjugaison ne fournit ni borne uniforme ancienne,
    ni signe coercif, ni régularité globale, ni blow-up admissible. Elle
    relie exactement deux formulations conditionnelles d'une même solution.

## 11. Statut logique

| Implication ou identité | Statut |
|---|---|
| \(A_s=-t/\rho^2\), \(B_s=A_s+a/\rho^2\) | **PROUVÉ algébriquement** |
| \([D,\Delta]=-2\Delta\), \(B_s'=2\kappa B_s-1\) | **PROUVÉ algébriquement** |
| dérivée (28) de \(T_\rho S(B_s)Z\) | **PROUVÉ dans les distributions** |
| conjugaison projetée (9), pression comprise | **PROUVÉ**, sous jauge globale de Riesz |
| \(d\|G_a\|_2^2/ds=-\rho^2I_a\) | **PROUVÉ** presque partout, pairing Lorentz justifié |
| \(D_R(s_n)\to0\Rightarrow J_a(s_n)\to0\) | **NON DÉMONTRÉ et non impliqué par les normes disponibles** |
| \(J_a=0\Rightarrow D_R=0\) | **FAUX comme implication fonctionnelle** : un pairing signé ne contrôle pas une norme |
| identité de flux \(\Rightarrow\) critère ancien borné | **NON DÉMONTRÉ** |
| conjugaison \(\Rightarrow\) résolution du problème Clay | **NON DÉMONTRÉ** |

**Décision analytique : CONTINUER.** La conjugaison n'offre pas de raccourci
du défaut local \(D_R\) vers le flux global. Le prochain lemme utile devrait
contrôler directement une primitive de \(J_a\) sur des fenêtres normalisées,
avec queues spatiales, facteur \(\rho^2\) et cancellations signées suivis;
une estimation de \(\partial_sZ\) seule ne peut pas remplir ce rôle.
