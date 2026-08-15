# Cycle 0042 — coût critique d'un cutoff solénoïdal mobile

Date d'audit : 2026-08-15.

## Verdict

Pour le rayon parabolique

\[
R(t)=c\sqrt{T_*-t},\qquad \tau=T_*-t,
\]

le terme de transport de la frontière mobile n'est pas petit. Sous une amplitude Type I \(u_R=R^{-1}U(x/R)\), il a l'échelle exacte d'une force Navier–Stokes :

\[
(\partial_t\chi_R)u_R=R^{-3}F_0(x/R).
\]

Il est invariant dans \(L^1_x\), croît comme \(R^{-1}\) dans \(L^{3/2,\infty}_x\) et comme \(R^{-1/2}\) dans \(\dot H^{-1}_x\). Les couples espace-temps critiques \(L^2_tL^{3/2,\infty}_x\) et \(L^4_t\dot H^{-1}_x\) accumulent une divergence logarithmique si le profil persiste jusqu'à \(T_*\). Un correcteur de Bogovskiĭ homothétiquement conjugué possède la même puissance \(R^{-3}\) après différentiation temporelle.

Ce résultat est un audit exact de scaling et un contre-test de petitesse. Il ne simule pas Navier–Stokes et ne démontre ni blow-up ni régularité.

## Horloge mobile exacte

Comme \(R^2=c^2\tau\),

\[
R'(t)=-\frac{c^2}{2R(t)},
\qquad
\frac{R'(t)}{R(t)}=-\frac1{2\tau}
=-\frac{c^2}{2R(t)^2}.
\]

Avec \(y=x/R(t)\) et \(\chi_R(x)=\chi(y)\),

\[
\partial_ty=-\frac{R'}R y,
\qquad
\partial_t\chi_R
=-\frac{R'}R(y\cdot\nabla\chi)(y)
=\frac{c^2}{2R^2}(y\cdot\nabla\chi)(y).
\]

Ainsi \(\partial_t\chi_R\) a amplitude \(R^{-2}\). Multipliée par une vitesse Type I d'amplitude \(R^{-1}\), elle produit \(R^{-3}\) sur un volume \(O(R^3)\).

## Conjugaison exacte de Bogovskiĭ

Soit \(A_R=R A_1\), le centre étant fixe, et fixons une droite inverse \(\mathcal B_1\) de la divergence sur \(A_1\). Sa conjugaison homothétique est

\[
(\mathcal B_Rg)(x)
=R\left[\mathcal B_1\big(g(R\,\cdot)\big)\right](x/R).
\]

Pour

\[
u_R(x)=R^{-1}U(y),\qquad
g_R=\nabla\chi_R\cdot u_R=R^{-2}g(y),
\]

on obtient, avec \(b=\mathcal B_1g\),

\[
\mathcal B_Rg_R=R^{-1}b(y).
\]

La dérivée de la conjugaison et celle de l'entrée ne peuvent pas être omises. Leur somme donne

\[
\partial_t(\mathcal B_Rg_R)
=-\frac{R'}{R^2}(b+y\cdot\nabla b)(y)
=\frac{c^2}{2R^3}(b+y\cdot\nabla b)(y).
\]

Cette identité vaut pour la famille auto-similairement dilatée ci-dessus et un centre fixe. Pour une entrée temporelle générale, un terme contenant sa dérivée transformée demeure ; pour un centre mobile, des termes supplémentaires proportionnels à la vitesse du centre apparaissent.

En posant

\[
W=\chi U-b,
\qquad
V_R=\chi_Ru_R-\mathcal B_Rg_R=R^{-1}W(y),
\]

les termes principaux ont tous la même amplitude :

\[
\partial_tV_R
=\frac{c^2}{2R^3}(W+y\cdot\nabla W),
\qquad
\Delta V_R=R^{-3}\Delta W,
\qquad
(V_R\cdot\nabla)V_R=R^{-3}(W\cdot\nabla)W.
\]

La pression compatible avec le scaling aurait \(P_R=R^{-2}P(y)\) et \(\nabla P_R=R^{-3}\nabla P(y)\). Le présent audit ne choisit ni ne résout cette pression non locale.

## Témoin solénoïdal lisse qui annule le correcteur

Définissons

\[
h(z)=
\begin{cases}
e^{-1/z},&z>0,\\
0,&z\leq0,
\end{cases}
\]

et le cutoff radial lisse

\[
\chi(r)=
\begin{cases}
1,&r\leq1,\\
\dfrac{h(2-r)}{h(2-r)+h(r-1)},&1<r<2,\\
0,&r\geq2.
\end{cases}
\]

Prenons également \(\eta\in C_c^\infty([0,\infty))\), radiale, égale à un sur \(r\leq2\), et

\[
U(y)=\eta(|y|)(-y_2,y_1,0).
\]

Ce champ est compact, lisse et divergence-free. Puisque \(U\) est azimutal et \(\chi\) radiale,

\[
\nabla\chi\cdot U=0.
\]

Par linéarité, \(g_R=0\), \(\mathcal B_Rg_R=0\), et \(V_R=\chi_Ru_R\) reste exactement divergence-free. Le correcteur ne peut donc pas être invoqué pour annuler le coût mobile dans ce témoin.

Au point \(y_0=(3/2,0,0)\), les facteurs exponentiels se simplifient exactement :

\[
\chi=\frac12,\qquad \chi'=-2,\qquad \chi''=0,
\qquad y_0\cdot\nabla\chi=-3,
\qquad U(y_0)=(0,3/2,0).
\]

On trouve alors

\[
R^3(\partial_t\chi_R)u_R(y_0R)
=\left(0,-\frac94c^2,0\right)\ne0,
\]

et, pour la dérivée temporelle complète,

\[
R^3\partial_tV_R(y_0R)
=\left(0,-\frac32c^2,0\right).
\]

Les deux autres jets vérifiés sont

\[
R^3\Delta V_R(y_0R)=(0,-8,0),
\qquad
R^3(V_R\cdot\nabla V_R)(y_0R)=(-3/8,0,0).
\]

Le résidu sans pression \(\partial_tV_R-\Delta V_R+(V_R\cdot\nabla)V_R\) a donc toujours une première composante \(-3/(8R^3)\). Cela montre seulement que cette famille n'est pas une solution sans force et sans pression ; une pression pourrait modifier le résidu et n'est pas auditée ici.

## Espaces naturels et accumulation temporelle

Si \(F_R(x)=R^{-3}F(x/R)\), les lois exactes sont

\[
\|F_R\|_{L^{p,\infty}}
=R^{-3+3/p}\|F\|_{L^{p,\infty}},
\]

et

\[
\|F_R\|_{\dot H^{-1}}
=R^{-1/2}\|F\|_{\dot H^{-1}}.
\]

Le profil de frontière ci-dessus est lisse, compact et non nul ; les constantes de référence correspondantes sont donc finies et strictement positives.

| espace spatial | puissance de \(R\) | conclusion à temps fixé |
|---|---:|---|
| \(L^1_x\) | \(0\) | critique, non petit |
| \(L^{3/2,\infty}_x\) | \(-1\) | divergent |
| \(L^3_x\) | \(-2\) | divergent |
| \(\dot H^{-1}_x\) | \(-1/2\) | divergent |

Sous \(R=c\sqrt\tau\), les couples invariants par scaling sont

\[
L^\infty_tL^1_x,\qquad
L^2_tL^{3/2,\infty}_x,\qquad
L^1_tL^3_x,\qquad
L^4_t\dot H^{-1}_x.
\]

Pour chacun des trois couples à exposant temporel fini, la puissance intégrée est exactement \(\tau^{-1}\). Chaque coquille logarithmique apporte donc la même quantité, et la norme sur un intervalle atteignant \(T_*\) diverge logarithmiquement si le coefficient de profil ne décroît pas. \(L^\infty_tL^1_x\) reste borné, mais pas petit lorsque \(R\downarrow0\).

L'identité de scaling est exacte pour \(\dot H^{-1}\). La norme inhomogène \(H^{-1}\) mélange les basses fréquences et ne possède pas cette identité exacte ; elle n'est pas substituée silencieusement à la norme homogène.

## Portée adverse

Le témoin réfute les raccourcis suivants :

1. \(R(t)\to0\) rendrait automatiquement le terme de cutoff petit ;
2. la correction solénoïdale absorberait toujours le transport de frontière ;
3. une borne ponctuelle critique suffirait à intégrer la force jusqu'au temps terminal dans un couple espace-temps endpoint.

Il ne réfute pas une annulation utilisant l'équation exacte de \(u\), la pression de Leray, une décroissance temporelle du profil annulaire, ou un espace de force plus faible. Tout progrès positif doit exhiber l'un de ces mécanismes avec une constante uniforme.

## Reproduction

~~~powershell
python -B experiments/navier-stokes/moving-solenoidal-cutoff/moving_cutoff_audit.py
~~~

Le script utilise uniquement la bibliothèque standard et fractions.Fraction. Il vérifie l'horloge sur 48 rayons rationnels, toutes les additions d'exposants, les jets rationnels du témoin, la puissance \(R^{-3}\) sur 36 configurations et le ledger de 64 coquilles critiques.

Statut : **CONTINUER** vers le calcul de la pression et de la force projetée. Le premier test décisif suivant est de déterminer si la projection de Leray ou une formulation en divergence place la combinaison complète des termes annulaires dans un espace strictement meilleur que chaque terme séparé.
