# Cycle 0045 — compacité locale et couche de trace terminale

Date d'audit : 2026-08-15.

## Verdict

Trois profils divergence-free séparent exactement les conclusions disponibles.

1. Une famille espace–temps oscillante conserve
   \[
   L^\infty_tL^{3,\infty}_x,\qquad
   L^\infty_tL^2_x,\qquad
   \partial_tZ_n\ \text{bornée dans }L^2_t\dot H^{-1}_x,
   \]
   mais n'est pas fortement compacte dans \(L^2_{t,x}\) et crée un défaut quadratique non nul. Elle perd la borne \(L^2_tH^1_x\) et n'a pas une force visqueuse uniformément bornée.
2. Une couche terminale parabolique conserve en plus
   \[
   L^2_tH^1_x,\qquad
   \partial_tY_n\in L^2_t\dot H^{-1}_x,
   \qquad
   F_n\in L^2_t\dot H^{-1}_x,
   \]
   et sa force tend même vers zéro dans \(L^1_t\dot H^{-1}_x\). Elle converge fortement vers zéro dans l'espace–temps, mais ses traces terminales gardent une énergie et un produit quadratique non nuls.
3. Une concentration compacte stationnaire sur \(\mathbb R^3\) converge fortement vers zéro dans \(L^2\), a une dérivée temporelle identiquement nulle et reste bornée dans \(W^{1,q}\) pour \(q\leq3/2\), mais conserve exactement sa quasi-norme faible-\(L^3\) de trace. Elle montre que les sorties sous-critiques du ledger ne transportent pas à elles seules la concentration critique.

Ainsi, la compacité forte intérieure et la transmission d'une trace terminale sont deux verrous distincts. Au scaling de la couche parabolique, l'exposant temporel \(p=2\) pour \(\partial_tY_n\) ou \(F_n\) dans \(\dot H^{-1}\) est critique ; toute borne uniforme avec \(p>2\) détruit ce profil précis.

Le certificat exact est construit sur un tore plat. Il fournit un contre-modèle fonctionnel local et, pour la seconde famille, une solution de cisaillement d'une équation de Navier–Stokes **forcée périodique**. Il ne s'agit ni d'une solution sur \(\mathbb R^3\), ni de l'équation Clay non forcée.

## Cellule spatiale exacte

Prenons le tore

\[
\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3
\]

avec mesure normalisée, et

\[
W_n(x)=\sin(nx_1)e_2.
\]

Alors

\[
\nabla\cdot W_n=0,
\qquad
\operatorname{div}(W_n\otimes W_n)=0.
\]

La seconde identité vient du fait que la seule entrée tensorielle non nulle est

\[
(W_n\otimes W_n)_{22}=\sin^2(nx_1),
\]

dont la divergence utilise \(\partial_2\).

Avec la convention spectrale naturelle,

\[
\|W_n\|_2^2=\frac12,
\qquad
\|W_n\|_{\dot H^{-1}}^2=\frac1{2n^2},
\qquad
\|\nabla W_n\|_2^2=\frac{n^2}{2}.
\]

La distribution de \(|W_n|\), donc sa quasi-norme faible-\(L^3\), est indépendante de \(n\). Les \(W_n\) convergent faiblement vers zéro, mais

\[
W_n\otimes W_n
\rightharpoonup
\frac12e_2\otimes e_2.
\]

Une version compacte sur \(\mathbb R^3\) s'obtient à partir du potentiel

\[
A_n(x)=n^{-1}\eta(x)\sin(nx_1)e_3,
\qquad W_n^{\rm c}=\operatorname{curl}A_n,
\]

avec \(\eta\in C_c^\infty\). Elle est exactement divergence-free et vérifie les mêmes puissances

\[
\|W_n^{\rm c}\|_{L^{3,\infty}}\lesssim1,\quad
\|W_n^{\rm c}\|_{\dot H^{-1}}\lesssim n^{-1},\quad
\|\nabla W_n^{\rm c}\|_2\lesssim n.
\]

Le certificat arithmétique emploie le tore afin de ne pas masquer les constantes de bord ou de cutoff de cette réalisation compacte.

## Profil A : oscillation et défaut de produit

Sur \(t\in[-\pi,0]\), avec mesure temporelle normalisée, posons

\[
Z_n(t,x)=\cos(nt)W_n(x).
\]

Les identités exactes sont

\[
\|Z_n\|_{L^2_{t,x}}^2=\frac14,
\qquad
\|\partial_tZ_n\|_{L^2_t\dot H^{-1}_x}^2=\frac14,
\]

mais

\[
\|\nabla Z_n\|_{L^2_{t,x}}^2=\frac{n^2}{4}.
\]

Les familles de Fourier sont orthogonales. Pour \(m\ne n\),

\[
\|Z_n-Z_m\|_{L^2_{t,x}}^2=\frac12.
\]

Il n'existe donc aucune sous-suite fortement convergente dans \(L^2_{t,x}\). Pourtant \(Z_n\rightharpoonup0\), tandis que

\[
Z_n\otimes Z_n
\rightharpoonup
\frac14e_2\otimes e_2.
\]

Le produit de la limite faible est zéro : le passage du terme quadratique échoue.

À chaque temps,

\[
\|Z_n(t)\|_{L^{3,\infty}}\leq
\|W_1\|_{L^{3,\infty}},
\qquad
\|Z_n(t)\|_2^2\leq\frac12.
\]

La dérivée admet aussi une borne uniforme dans \(W^{-1,q}\), \(1<q<\infty\), car

\[
W_n=\partial_1\left(-\frac{\cos(nx_1)}n e_2\right),
\]

donc

\[
\|W_n\|_{W^{-1,q}}\leq\frac{C_q}{n}.
\]

La fréquence temporelle \(n\) compense exactement ce gain négatif.

Ce profil ne satisfait pas les bornes dissipatives de l'équation forcée. En effet, pour la force résiduelle de cisaillement

\[
F_n=\partial_tZ_n-\Delta Z_n
\]

— le terme quadratique étant nul — le certificat donne

\[
\|F_n\|_{L^2_t\dot H^{-1}_x}^2
=\frac{1+n^2}{4}.
\]

Cette croissance empêche de présenter le profil A comme contre-exemple à une hypothèse incluant simultanément énergie dissipative et force uniforme.

La trace terminale vaut \(Z_n(0)=W_n\). Elle converge faiblement vers zéro, mais

\[
\|Z_n(0)\|_2^2=\frac12.
\]

La masse de trace n'est donc pas transportée par la seule convergence faible espace–temps.

## Profil B : couche terminale parabolique

Sur \(t\in[-1,0]\), posons

\[
b_n(t)=(1+n^2t)_+,
\qquad
Y_n(t,x)=b_n(t)W_n(x).
\]

Cette fois,

\[
\int_{-1}^0b_n(t)^k\,dt
=\frac1{n^2(k+1)}.
\]

On obtient exactement

\[
\|Y_n\|_{L^2_{t,x}}^2=\frac1{6n^2}\longrightarrow0,
\]

\[
\|\nabla Y_n\|_{L^2_{t,x}}^2=\frac16,
\]

et

\[
\|\partial_tY_n\|_{L^2_t\dot H^{-1}_x}^2=\frac12.
\]

La famille est donc fortement compacte dans l'intérieur espace–temps, conformément à Aubin–Lions, mais sa trace terminale est

\[
Y_n(0)=W_n,
\qquad
\|Y_n(0)\|_2^2=\frac12.
\]

Elle ne possède aucune sous-suite de traces fortement convergente dans \(L^2_x\). Sa limite espace–temps est zéro et possède une trace nulle, tandis que les produits terminaux vérifient

\[
Y_n(0)\otimes Y_n(0)
\rightharpoonup
\frac12e_2\otimes e_2.
\]

En revanche,

\[
\|Y_n\otimes Y_n\|_{L^1_{t,x}}
=\frac1{6n^2}\longrightarrow0.
\]

Le produit passe donc dans l'intérieur, mais pas au bord terminal.

## Équation forcée exacte du profil B

Puisque le cisaillement annule exactement son terme quadratique et admet la pression \(p=0\),

\[
\partial_tY_n-\Delta Y_n=F_n,
\qquad
\nabla\cdot Y_n=0,
\]

avec

\[
F_n=(b_n'+n^2b_n)W_n.
\]

Il s'agit d'une solution exacte de Navier–Stokes forcée périodique, au sens fort presque partout en temps. Le coefficient \(b_n\) est Lipschitz ; son coin ne crée pas de masse de Dirac puisque \(b_n\) est continu.

Le calcul exact donne

\[
\|F_n\|_{L^2_t\dot H^{-1}_x}^2=\frac76,
\]

et

\[
\sqrt2\,
\|F_n\|_{L^1_t\dot H^{-1}_x}
=\frac{3}{2n}\longrightarrow0.
\]

De même,

\[
\sqrt2\,
\|\partial_tY_n\|_{L^1_t\dot H^{-1}_x}
=\frac1n.
\]

La disparition de la force dans \(L^1_t\dot H^{-1}_x\), même jointe aux bornes d'énergie naturelles, ne transmet donc pas une trace \(L^2\) forte au temps terminal.

Cette force n'est pas la force annulaire précise du cycle 0044 et ne disparaît pas dans sa topologie spatiale \(C^\infty_{\rm loc}\) uniforme en temps : elle est haute fréquence et concentrée temporellement. Le profil teste seulement ce qui arriverait si cette information était affaiblie en une convergence intégrée négative.

## Seuil temporel du profil terminal

Pour \(p\geq1\), le coût exact de la force est

\[
\|F_n\|_{L^p_t\dot H^{-1}_x}^p
=2^{-p/2}
n^{p-2}
\frac{2^{p+1}-1}{p+1}.
\]

Ainsi :

- \(p<2\) : le coût tend vers zéro ;
- \(p=2\) : le coût reste constant ;
- \(p>2\) : le coût diverge.

Le même seuil vaut pour \(\partial_tY_n\), à une constante fixe près, et pour \(W^{-1,q}\) dès que \(\|W_n\|_{W^{-1,q}}\asymp n^{-1}\).

Plus généralement, pour une couche de largeur \(n^{-\alpha}\) :

\[
\int\|\nabla Y_n\|_2^2dt
\asymp n^{2-\alpha},
\]

tandis que

\[
\|\partial_tY_n\|_{L^p_tW^{-1,q}_x}
\asymp
n^{\alpha-1-\alpha/p}.
\]

La borne dissipative impose \(\alpha\geq2\). La borne temporelle est compatible seulement si

\[
p\leq\frac{\alpha}{\alpha-1}\leq2.
\]

Par conséquent :

\[
\boxed{\text{toute borne uniforme avec }p>2
\text{ exclut cette classe de couches terminales.}}
\]

Il s'agit du seuil minimal pour ce mécanisme parabolique, non d'un théorème universel de compacité des traces. Une autre géométrie ou une norme spatiale négative plus faible peut modifier le seuil.

## Profil C : concentration critique compacte sur \(\mathbb R^3\)

Choisissons

\[
A\in C_c^\infty(\mathbb R^3;\mathbb R^3),
\qquad
V=\operatorname{curl}A\ne0,
\]

et posons, pour tout temps,

\[
C_n(t,x)=nV(nx).
\]

Ce champ est lisse, compact et exactement divergence-free. Sa dérivée temporelle est identiquement nulle dans \(H^{-1}\), dans \(W^{-1,q}\) et dans toute autre topologie distributionnelle spatiale.

La fonction de distribution satisfait

\[
\mu_{C_n}(\lambda)
=n^{-3}\mu_V(\lambda/n).
\]

En posant \(\lambda=ns\), on obtient

\[
\lambda^3\mu_{C_n}(\lambda)
=s^3\mu_V(s),
\]

d'où l'identité critique exacte

\[
\boxed{
\|C_n\|_{L^{3,\infty}}
=\|V\|_{L^{3,\infty}}.}
\]

Pour tout \(1\leq r<\infty\),

\[
\boxed{
\|C_n\|_{L^r}
=n^{1-3/r}\|V\|_{L^r}.}
\]

En particulier,

\[
\|C_n\|_2^2=n^{-1}\|V\|_2^2\longrightarrow0.
\]

La famille et ses traces terminales convergent donc fortement vers zéro dans \(L^2\), alors que leur taille critique faible-\(L^3\) reste strictement constante.

Pour les dérivées spatiales,

\[
\boxed{
\|\nabla C_n\|_{L^q}
=n^{2-3/q}\|\nabla V\|_{L^q}.}
\]

Cette quantité est bornée exactement lorsque \(q\leq3/2\). À l'endpoint,

\[
\|\nabla C_n\|_{L^{3/2}}
=\|\nabla V\|_{L^{3/2}},
\]

mais l'enstrophie vérifie

\[
\boxed{
\|\nabla C_n\|_2^2
=n\|\nabla V\|_2^2.}
\]

Le contrôle spatial endpoint \(W^{1,3/2}\) ne fournit donc aucune borne énergétique \(H^1\).

La représentation négative est elle aussi exacte. Définissons

\[
T_{ij}=\varepsilon_{ijk}A_k.
\]

Alors

\[
\operatorname{div}T=V
\]

et, par la règle de chaîne,

\[
\boxed{
C_n=\operatorname{div}_x(T(nx)).}
\]

Par conséquent,

\[
\boxed{
\|C_n\|_{W^{-1,q}}
\leq
n^{-3/q}\|T\|_{L^q}.}
\]

Le profil converge donc fortement vers zéro dans chaque espace négatif ainsi contrôlé, plus vite encore que dans \(L^2\), sans perdre son \(K_3\) critique.

Son produit quadratique vérifie

\[
\|C_n\otimes C_n\|_{L^1}
=\|C_n\|_2^2
=n^{-1}\|V\|_2^2\longrightarrow0.
\]

Il ne crée donc pas de défaut quadratique dans les topologies sous-critiques du ledger. Son obstruction porte uniquement sur la trace critique faible-\(L^3\).

### Pourquoi le profil C n'est pas une solution admissible du cycle 0044

Pour l'équation projetée stationnaire sans drift, définissons le résidu de base

\[
\mathcal R(V)
=-\Delta V+\mathbb P_{\mathrm L}
\operatorname{div}(V\otimes V).
\]

Le scaling donne exactement

\[
\mathcal R(C_n)(x)
=n^3\mathcal R(V)(nx).
\]

Un champ compact non nul ne peut satisfaire \(\mathcal R(V)=0\) : tester l'équation stationnaire par \(V\) imposerait

\[
\|\nabla V\|_2^2=0,
\]

donc \(V=0\). Ainsi le \(V\) choisi possède un résidu non nul. Sur tout compact contenant l'origine et pour \(n\) assez grand, la norme locale du résidu rencontre une valeur d'amplitude \(n^3|\mathcal R(V)(y_0)|\) pour un \(y_0\) fixé où le résidu ne s'annule pas.

Un drift renormalisé \(\kappa D C_n\) n'a que l'amplitude \(n\) et ne peut annuler universellement ce terme cubique. La force résiduelle ne tend donc pas vers zéro dans \(C^\infty_{\rm loc}\). Le profil C satisfait les sorties fonctionnelles de compacité et de dérivée temporelle, mais pas l'équation forcée localement évanescente du cycle 0044. Il n'est pas présenté comme une solution de Navier–Stokes.

## Distinctions contractuelles

| objet | profil A | profil B | profil C |
|---|---|---|---|
| domaine exact du certificat | \(\mathbb T^3\) | \(\mathbb T^3\) | \(\mathbb R^3\) |
| divergence-free | oui, exactement | oui, exactement | oui, exactement |
| \(L^\infty_tL^{3,\infty}_x\) | uniforme | uniforme | invariant |
| énergie \(L^\infty_tL^2_x\) | uniforme | uniforme | tend vers zéro |
| \(L^2_tH^1_x\) | diverge | uniforme | diverge |
| \(\partial_t\) dans \(L^2_t\dot H^{-1}_x\) | uniforme | uniforme | nulle |
| force dans \(L^2_t\dot H^{-1}_x\) | diverge | uniforme | non uniforme |
| compacité forte espace–temps | non | oui, vers zéro | oui, vers zéro |
| produit quadratique intérieur | défaut \(1/4\) | converge vers zéro | converge vers zéro |
| trace terminale forte \(L^2\) | non | non | oui vers zéro, mais \(K_3\) constant |
| solution PDE | famille fonctionnelle ; équation résiduelle coûteuse | solution NS forcée périodique | famille fonctionnelle ; résidu cubique |
| transfert Clay | aucun | aucun | aucun |

Les bornes locales du cycle 0044 sont spatiales et essentielles en temps ; elles ne contiennent pas automatiquement les informations temporelles ou dissipatives du tableau.

## Reproduction

~~~powershell
python -B experiments/navier-stokes/local-compactness/local_compactness_audit.py
~~~

Le script utilise uniquement la bibliothèque standard et fractions.Fraction. Il certifie les normes spectrales, les distances orthogonales, les produits, tous les moments de la rampe, les coûts de force pour \(p=1,\dots,5\), le seuil sur une grille rationnelle de \((\alpha,p)\), et tous les exposants de scaling du profil compact C.

Statut : **CONTINUER**. Une fermeture positive du verrou exige une information qui contrôle simultanément l'intérieur et la trace : par exemple un module temporel dans une topologie interpolant compactement jusqu'au bord, une borne \(p>2\) compatible avec l'équation, ou une propagation quantitative de la concentration Type I sur un intervalle terminal non dégénéré.
