# Cycle 0050 — cocycle calorique critique et défaut de base uniforme

Date d'exécution : 2026-08-15

## Verdict

Le champ cinématique critique

\[
U(x)=\frac{(-x_2,x_1,0)}{|x|^2}
\]

est divergence-free au sens des distributions et appartient à \(L^{3,\infty}(\mathbb R^3)\). Pour le semi-groupe de la chaleur \(S(h)=e^{h\Delta}\), son défaut

\[
D_h=(I-S(h))U
\]

appartient à \(L^2\) pour tout \(h>0\) et vérifie l'identité exacte

\[
\|D_h\|_2=C_Uh^{1/4},
\qquad
0<C_U:=\|(I-S(1))U\|_2<\infty.
\]

Ainsi, chaque transition de base finie a une énergie finie, mais aucune borne \(L^2\) uniforme ne subsiste lorsque la base recule vers \(-\infty\). Le cocycle est algébriquement exact ; il ne transforme pas cette famille non uniforme en une limite énergétique globale.

Le profil \(U\) n'est pas une solution stationnaire des équations de Navier–Stokes incompressibles non forcées. Le certificat ne construit donc ni solution ancienne, ni blow-up, ni contre-exemple au problème Clay. Il montre exactement ce que les seules lois d'échelle faible-\(L^3\) et calorique ne peuvent pas garantir.

## 1. Champ solénoïdal critique

Hors de l'origine,

\[
\partial_1\left(-\frac{x_2}{|x|^2}\right)
+\partial_2\left(\frac{x_1}{|x|^2}\right)
=\frac{2x_1x_2}{|x|^4}-\frac{2x_1x_2}{|x|^4}=0.
\]

Sur toute sphère centrée,

\[
U\cdot n=0.
\]

Le champ est localement intégrable près de zéro et son flux normal à travers les petites sphères est identiquement nul. L'intégration par parties sur \(\mathbb R^3\setminus B_\varepsilon\), suivie de \(\varepsilon\downarrow0\), donne donc

\[
\nabla\cdot U=0
\]

au sens des distributions, sans source ponctuelle cachée.

En coordonnées sphériques, \(|U|=\sin\theta/r\). La fonction de distribution et l'énergie locale sont

\[
|\{|U|>\lambda\}|=\frac{\pi^2}{4\lambda^3},
\qquad
K_3(U)^3=\frac{\pi^2}{4},
\]

\[
\int_{B_R}|U|^2\,dx=\frac{8\pi}{3}R.
\]

Ainsi \(U\in L^{3,\infty}\cap L^2_{\mathrm{loc}}\), mais \(U\notin L^2(\mathbb R^3)\).

## 2. Exclusion comme solution Navier–Stokes non forcée

Écrivons \(\rho=(x_1^2+x_2^2)^{1/2}\), \(r=(\rho^2+x_3^2)^{1/2}\). Alors

\[
U=\frac{\rho}{r^2}e_\theta.
\]

Hors de zéro,

\[
\Delta U=-\frac{2}{r^2}U
=-\frac{2\rho}{r^4}e_\theta,
\qquad
(U\cdot\nabla)U=-\frac{\rho}{r^4}e_\rho.
\]

Le résidu stationnaire sans pression possède donc la composante azimutale

\[
\bigl[-\Delta U+(U\cdot\nabla)U\bigr]\cdot e_\theta
=\frac{2\rho}{r^4}.
\]

Sa circulation sur le cercle \(\{\rho=\rho_0,\ x_3=z_0\}\) vaut

\[
\oint \bigl[-\Delta U+(U\cdot\nabla)U\bigr]\cdot d\ell
=\frac{4\pi\rho_0^2}{(\rho_0^2+z_0^2)^2}\ne0.
\]

La circulation d'un gradient de pression monovalué est nulle. Aucun \(p\) ne peut donc satisfaire

\[
-\Delta U+(U\cdot\nabla)U+\nabla p=0
\]

même sur le domaine ponctué. Cette vérification interdit d'interpréter le profil comme une solution stationnaire singulière de Navier–Stokes non forcée.

## 3. Loi de similitude du semi-groupe

L'homogénéité \(U(\lambda x)=\lambda^{-1}U(x)\) et le noyau

\[
G_h(x)=h^{-3/2}G_1(x/\sqrt h)
\]

donnent, après \(y=\sqrt h\,z\),

\[
S(h)U(x)=h^{-1/2}(S(1)U)(x/\sqrt h).
\]

Par conséquent,

\[
D_h(x)=h^{-1/2}D_1(x/\sqrt h).
\]

Dès que \(D_1\in L^2\), le changement de variables exact donne

\[
\|D_h\|_2^2=h^{1/2}\|D_1\|_2^2,
\qquad
\|D_h\|_2=C_Uh^{1/4}.
\]

La puissance \(1/4\) n'est donc pas seulement un majorant de noyau : elle est saturée par ce profil homogène.

## 4. Finitude et positivité de \(C_U\)

À une constante de Fourier non nulle près,

\[
\widehat U(\xi)=
iA\,\frac{e_3\times\xi}{|\xi|^3}.
\]

Sa magnitude est homogène de degré \(-2\). Après intégration angulaire, la norme du défaut est un multiple positif de

\[
\int_0^\infty
\frac{(1-e^{-h\rho^2})^2}{\rho^2}\,d\rho.
\]

Près de \(\rho=0\), le multiplicateur est d'ordre \(\rho^2\), donc l'intégrande est d'ordre \(\rho^2\). À l'infini, elle est d'ordre \(\rho^{-2}\). Les deux extrémités sont intégrables. De plus, l'intégrande est strictement positive sur un ensemble de mesure positive. Ainsi

\[
0<C_U<\infty.
\]

Le calcul radial exact est

\[
\int_0^\infty
\frac{(1-e^{-h\rho^2})^2}{\rho^2}\,d\rho
=\sqrt\pi(2-\sqrt2)\sqrt h.
\]

Le script conserve les radicaux comme combinaisons linéaires formelles à coefficients `Fraction` ; aucune comparaison flottante n'est utilisée.

## 5. Cocycle de chaleur

L'identité de semi-groupe donne, pour \(h,k>0\),

\[
D_{h+k}=D_h+S(h)D_k.
\]

Pour trois incréments,

\[
D_{h+k+\ell}
=D_h+S(h)D_k+S(h+k)D_\ell.
\]

Les deux parenthésages coïncident exactement. Au niveau de chaque multiplicateur spectral \(z=e^{-|\xi|^2}\), l'identité devient

\[
1-z^{h+k+\ell}
=(1-z^h)+z^h(1-z^k)+z^{h+k}(1-z^\ell).
\]

Le certificat vérifie cette égalité sur plusieurs triplets d'entiers et plusieurs \(z\) rationnels. La preuve opératorielle reste l'identité \(S(h+k)=S(h)S(k)\), pas l'échantillonnage.

## 6. Énergie exacte d'une transition calorique

Pour \(a,b\ge0\), posons

\[
\mathcal E(a,b)=\|S(a)U-S(b)U\|_2^2.
\]

L'intégrale radiale

\[
\int_0^\infty
\frac{(e^{-a\rho^2}-e^{-b\rho^2})^2}{\rho^2}\,d\rho
=\sqrt\pi\left(
2\sqrt{a+b}-\sqrt{2a}-\sqrt{2b}
\right)
\]

donne la formule normalisée

\[
\boxed{
\mathcal E(a,b)=
\frac{C_U^2}{2-\sqrt2}
\left(
2\sqrt{a+b}-\sqrt{2a}-\sqrt{2b}
\right).}
\]

Elle est symétrique, nulle exactement lorsque \(a=b\), et strictement positive sinon. En effet,

\[
4(a+b)-\left(\sqrt{2a}+\sqrt{2b}\right)^2
=2(\sqrt a-\sqrt b)^2.
\]

En particulier,

\[
\mathcal E(0,h)=C_U^2\sqrt h.
\]

Le pont calorique \(S(\tau)D_h=S(\tau)U-S(\tau+h)U\) satisfait l'identité d'énergie \(L^2\)

\[
\frac12\mathcal E(\tau,\tau+h)
+\int_0^\tau
\|\nabla S(s)D_h\|_2^2\,ds
=\frac12C_U^2\sqrt h.
\]

Lorsque \(\tau\to\infty\), le premier terme tend vers zéro et l'énergie calorique totale dissipée vaut exactement

\[
\int_0^\infty\|\nabla S(s)D_h\|_2^2\,ds
=\frac12C_U^2\sqrt h.
\]

## 7. Obstruction à l'uniformité du temps de base

Plaçons le temps d'observation à zéro et la base à \(-T\). Le défaut entre le profil et son représentant calorique issu de cette base est

\[
U-S(T)U=D_T.
\]

Ainsi,

\[
\|U-S(T)U\|_2=C_UT^{1/4}\xrightarrow[T\to\infty]{}\infty.
\]

Le quantificateur correct est donc

\[
\forall T<\infty,\quad D_T\in L^2,
\]

et non

\[
\sup_{T>0}\|D_T\|_2<\infty.
\]

Le cocycle compare exactement deux bases finies, mais ne produit aucune compacité \(L^2\) lorsque la première base tend vers \(-\infty\).

## 8. Non-commutation des limites spatiale et de base

Définissons

\[
E(T,R)=\int_{B_R}|D_T(x)|^2\,dx.
\]

Pour tout \(T<\infty\), \(D_T\in L^2(\mathbb R^3)\), donc

\[
\lim_{R\to\infty}\frac{E(T,R)}R=0.
\]

Pour tout \(R<\infty\), la similitude calorique donne

\[
\|S(T)U\|_{L^\infty}\lesssim T^{-1/2},
\]

donc \(D_T\to U\) dans \(L^2(B_R)\). Par l'énergie locale exacte de \(U\),

\[
\lim_{T\to\infty}\frac{E(T,R)}R=\frac{8\pi}{3}.
\]

Les limites itérées normalisées sont donc

\[
\boxed{
\lim_{T\to\infty}\lim_{R\to\infty}\frac{E(T,R)}R=0,
\qquad
\lim_{R\to\infty}\lim_{T\to\infty}\frac{E(T,R)}R=\frac{8\pi}{3}.}
\]

Cette différence mesure une fuite d'uniformité, pas un défaut de l'identité de semi-groupe. Elle interdit d'échanger silencieusement « domaine entier » et « base ancienne » dans une énergie de correcteur construite seulement temps de base par temps de base.

## 9. Attaques de quantificateurs

1. **Chaque base versus toutes les bases.** La finitude de \(D_T\) pour tout \(T\) ne donne pas une borne uniforme en \(T\).
2. **Cocycle versus convergence.** Une identité exacte entre trois bases ne donne aucune convergence de la famille lorsque sa norme croît.
3. **Local versus global.** La convergence \(D_T\to U\) sur tout \(B_R\) fixé n'est pas globale dans \(L^2\), puisque \(U\notin L^2\).
4. **Espace puis base versus base puis espace.** Les limites normalisées calculées ci-dessus ne commutent pas.
5. **Profil critique versus solution PDE.** La saturation de \(h^{1/4}\) par un champ divergence-free faible-\(L^3\) ne dit rien sans l'équation, la pression et la suitability.

## 10. Portée et reproduction

Le certificat porte sur la divergence distributionnelle, les lois de similitude, l'intégrabilité spectrale, les identités radicales d'énergie, le cocycle et le ledger des limites. Il ne certifie aucune solution de Navier–Stokes. La circulation résiduelle démontre au contraire que \(U\) n'est pas une solution stationnaire non forcée.

Commande :

```powershell
python -B experiments/navier-stokes/heat-cocycle/heat_cocycle_audit.py
```

Sortie attendue :

```text
heat_cocycle_audit: PASS
exact_assertions=161
defect=||(I-S(h))U||_2=C_U*h^1/4 with 0<C_U<infinity
cocycle=D_(h+k+l)=D_h+S(h)D_k+S(h+k)D_l
uniformity=sup_T||(I-S(T))U||_2=infinity
limit_order_over_pi=space_then_base:0, base_then_space:8/3
scope=heat-semigroup ledger for a kinematic field; U is not an NS solution
```

Le programme utilise seulement la bibliothèque standard, `Fraction` et une représentation interne exacte des sommes de radicaux. Résidu rationnel et radical : zéro. Aucune discrétisation ni approximation flottante.

Empreinte SHA-256 du script validé :

```text
2b463738f3bc415c1a3ae90c843ca87661a62538f17514bc777e1570326129a6
```

## Décision contradictoire

**RÉVISER.** Toute globalisation de l'énergie relative vers une base \(-\infty\) doit fournir une annulation PDE supplémentaire ou une borne uniforme absente du contrôle faible-\(L^3\). Le prochain test décisif doit déterminer si la suitability de la solution ancienne réelle produit cette uniformité, plutôt que de la déduire du cocycle calorique seul.
