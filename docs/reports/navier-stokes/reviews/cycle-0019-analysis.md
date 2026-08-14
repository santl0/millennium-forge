# Cycle 0019 — audit contradictoire de l’endgame (49)–(58)

Date de la passe : 2026-08-14

Source auditée : Zoran Grujić, *Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier–Stokes Equations*, [arXiv:2607.08866v2](https://arxiv.org/abs/2607.08866v2), équations (49)–(58) et prérequis temporels.

Portée : niveau relatif, volume du superniveau, rayon de sparseness, rayon analytique, temps d’échappement, branches temporelles, deux cas du principe harmonique, sens des inégalités, seuils et dépendances des constantes.

> **Statut de la revue.** Cette passe est produite par un agent de la même famille de modèle que les autres passes de Millennium Forge. Elle est contradictoire dans sa méthode, mais **n’est pas une revue externe ni une réplication indépendante**.

## Verdict

L’endgame harmonique peut être formulé comme un lemme conditionnel correct à partir d’une borne de distribution uniforme du type (49). Le calcul spatial est cohérent après dimensionnement :

\[
|V_s|lesssim
U_s^{-3}\mathscr L(U_s)^{-3}
\quad\Longrightarrow\quad
r_s\lesssim
U_s^{-1}\mathscr L(U_s)^{-1},
\]

tandis que l’analyticité fournit

\[
\rho_s\gtrsim\nu U_s^{-1}.
\]

Le logarithme permet donc bien \(r_s\le\rho_s\) au-dessus d’un seuil fini. Les sens des inégalités dans les deux cas du principe harmonique sont également corrects après fixation des paramètres.

Cependant, la preuve telle qu’écrite saute la bifurcation temporelle indispensable. Elle pose \(s=t+T_t\), puis utilise

\[
\|u(s)\|_\infty>\|u(t)\|_\infty
\]

parce que \(t\) serait un temps d’échappement, sans avoir démontré \(s<T^*\). Si \(s\ge T^*\), la solution supposée seulement sur \((0,T^*)\) n’est pas encore définie à \(s\) ; en revanche, le théorème local d’analyticité fournit alors directement le prolongement au-delà de \(T^*\). C’est le **premier trou de quantificateur décisif** de cette section. Le critère primaire de Grujić (2013) sépare explicitement ces branches (i) et (ii) ; arXiv:2607.08866v2 les fusionne.

Autres corrections nécessaires :

1. \(T_t\) doit être un temps d’existence **certifié**, pas un « maximal local analyticity time » non calculé ;
2. le rayon analytique est une borne inférieure, non l’égalité affichée en (54) ; on peut choisir un sous-rayon certifié égal au membre droit ;
3. la borne (49) ne s’applique au niveau \(\vartheta\|u(s)\|_\infty\) que si ce niveau dépasse son seuil uniforme de grande amplitude ;
4. le logarithme de (49), (55) et (56) exige une amplitude de référence ;
5. la constante de volume doit être uniforme en temps et indépendante de \(\|u(s)\|_\infty\), sinon la synchronisation est circulaire ;
6. l’existence de temps d’échappement arbitrairement proches de \(T^*\) doit être déduite de la branche où le temps local ne franchit jamais \(T^*\), et non simplement attribuée à la « local well-posedness ».

Une fois ces points réparés, le lemme 0019-A de la section 9 ferme l’argument conditionnel.

## 1. Cadre exact et conventions

On considère Navier–Stokes incompressible, non forcé, sur \(\mathbb R^3\), avec viscosité \(\nu>0\), et une solution classique

\[
u\in C((0,T^*);L^\infty(\mathbb R^3))
\]

sur son intervalle maximal supposé fini. Posons

\[
U(t)=\|u(t)\|_\infty.
\]

L’endgame n’utilise aucune solution faible. Le théorème local en \(L^\infty\), l’unicité de la solution mild et son extension complexe sont requis à chaque redémarrage temporel.

### Entrée de distribution dimensionnée

Fixons une amplitude de référence \(U_*>0\), un seuil \(a_0>0\), et une constante \(C_\mu>0\) tels que, sur un intervalle final \(I_*=(T^*-\epsilon,T^*)\),

\[
\boxed{
\mu_u(a,t):=|\{x:|u(x,t)|>a\}|
\le
\frac{C_\mu}{a^3\mathscr L(a)^3},
\qquad
\mathscr L(a)=\log\left(e+\frac a{U_*}\right),
}
\tag{H49}
\]

pour tout \(a\ge a_0\), uniformément en \(t\in I_*\).

La constante \(C_\mu\) a la dimension

\[
[C_\mu]=[u]^3L^3=L^6T^{-3},
\]

et \(C_\mu^{1/3}\) a la même dimension \(L^2T^{-1}\) que \(\nu\). (H49) est la version exacte nécessaire de (49). Cette passe n’en redémontre pas la provenance ; les cycles 0016–0018 montrent qu’elle reste conditionnelle aux maillons antérieurs.

## 2. Constantes harmoniques et niveau relatif

Fixons la densité volumique du papier

\[
\delta_3=\frac34,
\qquad
\delta_1=\delta_3^{1/3}.
\]

Le complément d’un ensemble linéairement \(\delta_1\)-sparse occupe une fraction au moins \(1-\delta_1\) du diamètre. Le théorème extrémal de Solynin donne alors

\[
\boxed{
h_*
=\frac2\pi
\arcsin\left(
\frac{1-\delta_1^2}{1+\delta_1^2}
\right)
=\frac2\pi
\arcsin\left(
\frac{1-(3/4)^{2/3}}{1+(3/4)^{2/3}}
\right).
}
\tag{h}
\]

Pour la version additive du principe des deux constantes utilisée dans le papier, choisissons le facteur de croissance analytique

\[
\boxed{
M_A=\frac{1-h_*/2}{1-h_*}>1
}
\tag{MA}
\]

de sorte que

\[
\frac12h_*+(1-h_*)M_A=1.
\]

Le niveau relatif doit être renommé pour éviter la collision avec le niveau de troncature \(\lambda\) des sections antérieures :

\[
\boxed{
\vartheta=\frac1{2M_A}\in(0,1).
}
\tag{theta}
\]

À un temps \(s\), le superniveau actif est

\[
V_s=\{x:|u(x,s)|>\vartheta U(s)\}.
\tag{V}
\]

Le choix de \(M_A\) n’est pas circulaire : \(h_*\), puis \(M_A\), puis \(\vartheta\) sont fixés avant l’application du théorème local. En revanche, les constantes analytiques \(c_1(M_A)\) et \(c_2(M_A)\) dépendent de ce choix et doivent être conservées.

## 3. Volume du superniveau : (49), (50), (55)

Si

\[
\vartheta U(s)\ge a_0,
\tag{level}
\]

(H49) appliquée avec \(a=\vartheta U(s)\) donne

\[
\boxed{
|V_s|
\le
B_s:=
\frac{C_\mu}
{\vartheta^3U(s)^3
\mathscr L(\vartheta U(s))^3}.
}
\tag{55q}
\]

Cette substitution est correcte. Le papier omet toutefois (level). Elle sera obtenue en choisissant un temps d’échappement d’amplitude suffisamment élevée.

La quantité \(\log(e+\vartheta U(s))\) de (55) n’est dimensionnelle que si les variables ont été préalablement normalisées. Le quotient \(\vartheta U(s)/U_*\) de (H49) est le raccord requis.

## 4. Du volume au rayon de sparseness : (56)

Définissons le rayon sûr

\[
\boxed{
r_s
=\left(\frac{B_s}{\delta_3|B_1|}\right)^{1/3}
=\frac{A_s}
{U(s)\mathscr L(\vartheta U(s))},
}
\tag{rs}
\]

où

\[
\boxed{
A_s=\frac{C_\mu^{1/3}}
{\vartheta(\delta_3|B_1|)^{1/3}}.
}
\tag{As}
\]

Ici \(A_s\) est une constante — l’indice rappelle « sparseness », pas une dépendance temporelle — de dimension \(L^2T^{-1}\).

Pour tout centre \(x_0\),

\[
|V_s\cap B_{r_s}(x_0)|
\le |V_s|
\le B_s
=\delta_3|B_{r_s}|.
\]

Ainsi \(V_s\) est 3D \(\delta_3\)-sparse autour de **tout** \(x_0\) au même rayon \(r_s\). Le sens logique est important : on construit \(r_s\) par l’égalité (rs). Une simple assertion « il existe un rayon plus petit » ne suffirait pas, car réduire un rayon peut augmenter la densité locale.

### Passage 3D → 1D avec constante exacte

Pour un ensemble mesurable \(E\subset B_r(x_0)\), écrivons, en coordonnées sphériques signées,

\[
|E|
=\frac12\int_{S^2}\int_{-r}^{r}
\mathbf1_E(x_0+\sigma d)|\sigma|^2\,d\sigma\,dS(d).
\]

Parmi les sous-ensembles de \([-r,r]\) de longueur \(\ell\), l’intégrale de \(|\sigma|^2\) est minimale sur \([-\ell/2,\ell/2]\), avec valeur \(\ell^3/12\). Si chaque direction rencontrait \(E\) sur une longueur strictement supérieure à \(2r\delta_3^{1/3}\), on aurait

\[
|E|>\delta_3|B_r|,
\]

contradiction. Il existe donc une direction \(d=d(x_0)\) telle que

\[
\frac{|V_s\cap(x_0-r_sd,x_0+r_sd)|}{2r_s}
\le\delta_1.
\tag{1D}
\]

Le facteur \((3/4)^{1/3}\) employé dans le papier est correct.

## 5. Temps local et rayon analytique

Appliquons le théorème local \(L^\infty\) avec le facteur fixé \(M_A\). Il fournit des constantes

\[
c_1=c_1(M_A)>0,
\qquad
c_2=c_2(M_A)>0
\]

telles qu’au départ d’un temps \(t<T^*\), la solution mild existe au moins pendant

\[
\boxed{
\tau_t=\frac{\nu}{c_1U(t)^2},
}
\tag{tau}
\]

avec borne complexe

\[
\|u(t+\tau)\|_{L^\infty(\text{tube complexe})}
\le M_AU(t),
\qquad 0\le\tau\le\tau_t,
\]

et rayon spatial au temps \(t+\tau\) au moins

\[
\frac{\sqrt{\nu\tau}}{c_2}.
\]

À l’extrémité certifiée \(s=t+\tau_t\), le rayon est donc au moins

\[
\boxed{
\rho_t=\frac{\nu}{c_AU(t)},
\qquad
c_A=c_2\sqrt{c_1}.
}
\tag{rho-t}
\]

Il ne s’agit pas nécessairement du temps maximal d’analyticité ni du rayon maximal. Ce sont un temps et un rayon **certifiés**.

Si \(t\) est un temps d’échappement et si \(s<T^*\), alors \(U(s)>U(t)\), donc

\[
\rho_t
>\frac{\nu}{c_AU(s)}.
\]

On peut choisir le sous-rayon conservatif

\[
\boxed{
\rho_s^{\rm cert}=\frac{\nu}{c_AU(s)}.
}
\tag{54q}
\]

Le sens de l’inégalité est correct dans le papier, mais (54) doit être lu comme le choix d’un sous-rayon, pas comme une égalité pour le rayon analytique réel.

Source primaire de l’estimation analytique citée par l’article : R. Guberović, *Smoothness of Koch–Tataru solutions to the Navier–Stokes equations revisited*, DCDS 27 (2010), 231–236, [DOI 10.3934/dcds.2010.27.231](https://doi.org/10.3934/dcds.2010.27.231).

## 6. Première bifurcation obligatoire : branches temporelles (i)/(ii)

Pour tout temps candidat \(t\), il faut traiter exactement l’alternative suivante.

### Branche (i) — le temps local atteint \(T^*\)

Si

\[
t+\tau_t\ge T^*,
\tag{i}
\]

la solution mild redémarrée en \(t\) existe jusqu’à \(T^*\) avec une borne \(L^\infty\). Par unicité, elle coïncide avec la solution initiale avant \(T^*\), puis le théorème local la prolonge. Le temps \(T^*\) n’est pas singulier ; aucun argument de sparseness n’est requis.

### Branche (ii) — le temps local reste avant \(T^*\)

Si, pour tous les temps suffisamment proches de \(T^*\),

\[
t+\tau_t<T^*,
\tag{ii}
\]

alors

\[
U(t)^2>\frac{\nu}{c_1(T^*-t)},
\]

et donc

\[
U(t)\longrightarrow\infty
\quad\text{lorsque }t\uparrow T^*.
\tag{blow}
\]

Cette divergence, jointe à la continuité de \(U\), produit des temps d’échappement arbitrairement proches de \(T^*\). En effet, sur chaque intervalle final \([a,T^*)\), \(U\) atteint son minimum puisque (blow) repousse les petites valeurs loin de \(T^*\). Le dernier point où ce minimum est atteint satisfait

\[
U(s)>U(t)
\qquad\text{pour tout }s\in(t,T^*).
\tag{escape}
\]

En faisant tendre \(a\) vers \(T^*\), ces temps tendent vers \(T^*\), et leurs amplitudes tendent vers l’infini.

La phrase du papier selon laquelle la seule « local well-posedness » donne un temps d’échappement à tout niveau élevé est insuffisante. C’est la combinaison de la branche (ii), de la continuité et de la divergence (blow) qui fournit le quantificateur exact.

Le critère primaire de Grujić sépare précisément (i) et (ii) : Z. Grujić, *A geometric measure-type regularity criterion for solutions to the 3D Navier–Stokes equations*, Nonlinearity 26 (2013), 289–296, [arXiv:1111.0217v5](https://arxiv.org/html/1111.0217v5), [DOI 10.1088/0951-7715/26/1/289](https://doi.org/10.1088/0951-7715/26/1/289).

## 7. Seuil exact de synchronisation \(r_s\le\rho_s\)

Dans la branche (ii), prenons un temps d’échappement \(t\) et posons

\[
s=t+\tau_t<T^*.
\]

Alors \(U(s)>U(t)\), et les estimations de la section 5 s’appliquent. Pour que le rayon (rs) soit contenu dans le rayon analytique conservatif (54q), il suffit que

\[
\frac{A_s}{U(s)\mathscr L(\vartheta U(s))}
\le\frac{\nu}{c_AU(s)}.
\]

Les amplitudes se simplifient dans le bon sens, et la condition exacte devient

\[
\boxed{
\mathscr L(\vartheta U(s))
\ge\frac{c_AA_s}{\nu}.
}
\tag{sync}
\]

Posons

\[
K_{\rm sync}=\frac{c_AA_s}{\nu}.
\]

Un seuil suffisant est

\[
\boxed{
U(s)\ge U_{\rm sync}
:=\frac{U_*}{\vartheta}
\max\{0,e^{K_{\rm sync}}-e\}.
}
\tag{Usync}
\]

Il faut simultanément \(U(s)\ge a_0/\vartheta\). Le seuil total est donc

\[
\boxed{
U_{\rm th}=\max\left\{
\frac{a_0}{\vartheta},U_{\rm sync}
\right\}.
}
\tag{Uth}
\]

Le temps d’échappement peut être choisi avec \(U(t)>U_{\rm th}\), donc \(U(s)>U_{\rm th}\). Le seuil est fini et indépendant du temps si \(C_\mu,U_*,a_0,c_1,c_2\) sont uniformes. Il est toutefois exponentiel en

\[
\frac{C_\mu^{1/3}}{\nu},
\]

à facteurs géométriques près. Dire seulement que le logarithme « finit par dominer » masque cette dépendance, mais ne renverse pas l’inégalité.

Si \(C_\mu\) dépendait de \(U(s)\) ou d’une troncature qui diverge avec \(s\), (sync) deviendrait circulaire. L’uniformité de (H49) est donc un prérequis indispensable.

## 8. Deux cas spatiaux du principe harmonique : (57)–(58)

Fixons un point arbitraire \(x_0\). Par (1D), choisissons une direction \(d\) et un segment de rayon \(r_s\le\rho_s^{\rm cert}\). Après translation et rotation, ce segment devient \([-r_s,r_s]\) sur l’axe réel d’un disque complexe \(D_{r_s}\).

Posons

\[
K=[-r_s,r_s]\setminus(V_s\cap[-r_s,r_s]).
\]

Alors \(K\) est fermé et

\[
|K|\ge2r_s(1-\delta_1).
\]

### Cas spatial 1 — \(0\in K\)

On a directement

\[
|u(x_0,s)|
\le\vartheta U(s)
\le\vartheta M_AU(t)
=\frac12U(t)
\le U(t),
\tag{case1}
\]

où la deuxième inégalité est la borne du théorème analytique. Ce fait ne constitue pas à lui seul une contradiction avec le temps d’échappement ; il fournit la borne voulue au point arbitraire \(x_0\). Le mot « contradiction » employé localement dans le papier est prématuré.

### Cas spatial 2 — \(0\notin K\)

Si \(u(x_0,s)\ne0\), choisissons le vecteur réel

\[
e_0=\frac{u(x_0,s)}{|u(x_0,s)|}
\]

et la fonction harmonique

\[
v(z)=\Re(u(z,s)\cdot e_0).
\]

Alors

\[
v(0)=|u(x_0,s)|,
\qquad
v\le M_AU(t)\quad\text{dans }D_{r_s},
\]

et, sur \(K\),

\[
v\le|u(\cdot,s)|
\le\vartheta U(s)
\le\frac12U(t).
\]

Par invariance conforme, monotonie en \(K\) et théorème de Solynin,

\[
H:=h(0,D_{r_s}\setminus K,K)
\ge h_*.
\tag{H}
\]

Le principe additif des deux constantes donne

\[
\begin{aligned}
|u(x_0,s)|
&\le H\frac12U(t)+(1-H)M_AU(t)\\
&\le\left[\frac12h_*+(1-h_*)M_A\right]U(t)\\
&=U(t).
\end{aligned}
\tag{58q}
\]

Le second sens d’inégalité est correct parce que la fonction affine

\[
H\longmapsto\frac12H+(1-H)M_A
\]

est décroissante : \(M_A>1/2\). La borne inférieure \(H\ge h_*\) améliore donc le majorant.

Le théorème de Solynin employé ici est : A. Yu. Solynin, *Ordering of sets, hyperbolic metric, and harmonic measure*, POMI 237 (1997), 129–147 ; traduction J. Math. Sci. 95 (1999), 2256–2266, [DOI 10.1007/BF02172470](https://doi.org/10.1007/BF02172470).

Comme \(x_0\) était arbitraire, (case1) et (58q) donnent

\[
U(s)\le U(t),
\]

ce qui contredit seulement maintenant la propriété stricte (escape).

## 9. Lemme conditionnel minimal exact

### Lemme 0019-A — fermeture harmonique à partir de (49)

Soit \(u\) une solution classique maximale du système non forcé sur \(\mathbb R^3\times(0,T^*)\), \(T^*<\infty\). Supposons :

1. la borne de distribution uniforme (H49) sur un intervalle final ;
2. le théorème local analytique avec constantes \(c_1(M_A),c_2(M_A)\), unicité et dépendance en \(\nu\) décrites à la section 5 ;
3. le principe harmonique additif et la borne de Solynin sous les formes utilisées à la section 8.

Alors \(T^*\) n’est pas un temps singulier.

### Preuve

Pour un temps \(t\) proche de \(T^*\), définissons \(\tau_t\) par (tau).

- Si \(t+\tau_t\ge T^*\), la branche (i) prolonge directement la solution.
- Sinon, si cette alternative persiste près de \(T^*\), (blow) assure des temps d’échappement arbitrairement proches et d’amplitude arbitrairement grande.

Choisissons un tel temps \(t\) de façon que \(t\in I_*\) et \(U(t)>U_{\rm th}\), puis posons \(s=t+\tau_t<T^*\). Alors \(s\in I_*\), \(U(s)>U(t)>U_{\rm th}\), (55q) s’applique, le rayon (rs) est 3D sparse autour de tout point, (1D) fournit une direction, et (sync) garantit \(r_s\le\rho_s^{\rm cert}\). Les deux cas de la section 8 donnent \(U(s)\le U(t)\), en contradiction avec (escape). Les deux branches excluent donc la singularité.

### Minimalité

Pour cet endgame, (H49) peut être remplacée par toute borne donnant un rayon sûr \(r_s=o(U(s)^{-1})\) avec constantes uniformes. À l’inverse, une seule borne critique sans gain,

\[
|V_s|\le C U(s)^{-3},
\]

donne seulement \(r_s\le A/U(s)\). La comparaison avec \(\nu/(c_AU(s))\) dépend alors d’une petitesse non garantie de \(A/\nu\). Le gain logarithmique est exactement ce qui rend le seuil (Usync) fini sans hypothèse de petitesse.

## 10. Scaling Navier–Stokes

Sous

\[
u_\rho(x,t)=\rho u(\rho x,\rho^2t),
\]

on a

\[
U_\rho(t)=\rho U(\rho^2t),
\qquad
\mu_{u_\rho}(a,t)
=\rho^{-3}\mu_u(a/\rho,\rho^2t).
\]

Les paramètres se transforment par

\[
U_{*,\rho}=\rho U_*,
\qquad
a_{0,\rho}=\rho a_0,
\qquad
C_{\mu,\rho}=C_\mu,
\]

tandis que \(\nu,M_A,\vartheta,c_1,c_2,A_s\) sont invariants. Par conséquent,

\[
r_{s,\rho}=\rho^{-1}r_s,
\qquad
\rho_{s,\rho}^{\rm cert}=\rho^{-1}\rho_s^{\rm cert},
\qquad
\tau_{t,\rho}=\rho^{-2}\tau_t.
\]

Le rapport

\[
K_{\rm sync}=c_AA_s/\nu
\]

est sans dimension et invariant. Les seuils d’amplitude se multiplient par \(\rho\), comme ils le doivent. Aucun gain de puissance caché n’intervient dans l’endgame.

## 11. Tests adverses

### Test A — temps \(s\) non défini

Supposons

\[
t+\tau_t>T^*.
\]

La définition d’un temps d’échappement ne compare \(U(t)\) qu’aux temps de \((t,T^*)\). L’expression \(U(t+\tau_t)>U(t)\) est alors hors de son domaine et ne peut être utilisée. Ce test réfute directement le passage (389)–(390) sans branche temporelle. Il ne réfute pas la conclusion : le théorème local fournit précisément la branche de prolongement (i).

### Test B — mauvais sens pour un rayon arbitrairement petit

Prenons un ensemble contenant entièrement une petite boule autour de \(x_0\), mais de volume total très petit. Il peut vérifier \(|V_s|\le B_s\) tout en ayant densité un sur toutes les boules de rayon inférieur au rayon du cœur. Ainsi, de \(|V_s|\le B_s\), on ne peut conclure que **tout** rayon

\[
r\le(B_s/(\delta_3|B_1|))^{1/3}
\]

est sparse. Le rayon sûr est celui de (rs), ou tout rayon plus grand. La construction du papier est valide seulement si son symbole \(r_s\le\cdots\) signifie « il existe le rayon construit, dont la valeur est bornée », et non une monotonie vers les petites échelles.

### Test C — sens de la mesure harmonique

Pour

\[
g(H)=\frac12H+(1-H)M_A,
\]

on a \(g'(H)=1/2-M_A<0\). Ainsi \(H\ge h_*\) implique

\[
g(H)\le g(h_*)=1.
\]

Le sens employé dans (57)–(58) est certifié. Si le niveau sur \(K\) était supérieur à la borne complexe, le sens serait inversé ; le choix \(\vartheta=1/(2M_A)\) l’exclut.

### Test D — constante dépendant de l’amplitude

Si l’on remplaçait dans (H49) \(C_\mu\) par \(C_\mu(U)=\nu^3\mathscr L(\vartheta U)^3\), alors

\[
r_s\asymp\frac{\nu}{U},
\]

et le logarithme disparaîtrait entièrement de (sync). Ce contre-test montre que la seule mention « \(C\) indépendant du temps » ne suffit pas si \(C\) a été défini à partir d’une quantité dépendant implicitement du temps ou du niveau. La traçabilité amont de \(C_\mu\) est indispensable.

## 12. Statut maillon par maillon

| Maillon | Statut | Condition ou défaut exact |
|---|---|---|
| (47) → (49) | Conditionnel | Inversion quantitative préalable requise ; seuil et références d’amplitude nécessaires. |
| (49) → (55) | Correct sous seuil | Exiger \(\vartheta U(s)\ge a_0\), constante uniforme. |
| (55) → rayon 3D | Correct par construction | Choisir (rs) ; les rayons plus petits ne sont pas automatiquement sparse. |
| 3D → 1D | Correct | Densité \(\delta_1=\delta_3^{1/3}\), preuve sphérique donnée. |
| Théorème analytique → (54) | Correct comme sous-rayon | \(s=t+\tau_t\), rayon réel \(\ge\rho_t>\rho_s^{\rm cert}\), pas égalité. |
| Choix de \(s\) | Trou décisif dans le texte | Il faut d’abord séparer \(t+\tau_t\ge T^*\) et \(<T^*\). |
| Temps d’échappement | Réparable | Existence issue de la branche (ii), continuité et divergence de \(U(t)\). |
| Synchronisation | Correct avec seuil | Seuil explicite (Uth), exponentiel en \(C_\mu^{1/3}/\nu\). |
| Cas \(0\in K\) | Correct | Borne ponctuelle, pas encore contradiction. |
| Cas \(0\notin K\) | Correct | Fonction harmonique projetée, mesure \(H\ge h_*\), combinaison affine décroissante. |
| (58) → contradiction | Correct après universalité en \(x_0\) | Donne \(U(s)\le U(t)\), contraire à (escape). |

## 13. Écart avec le problème Clay

Le lemme 0019-A ferme uniquement l’endgame **si** (H49) est déjà établi avec constantes uniformes pour la solution classique maximale considérée. Il ne démontre pas :

- la borne critique de vorticité ou la géométrie directionnelle requises en amont ;
- le théorème 4.1 de l’article sans les réparations des cycles précédents ;
- l’applicabilité de (H49) à toutes les solutions Clay ;
- une version périodique ou sur domaine borné ;
- un passage depuis une solution faible jusqu’aux extensions analytiques ponctuelles.

Le premier verrou reste donc en amont, dans la production uniforme de (H49). Le trou temporel identifié ici est sérieux comme preuve écrite, mais localement réparable par la dichotomie classique du critère primaire.

## Sources primaires

- Z. Grujić, *Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier–Stokes Equations*, arXiv:2607.08866v2, sections 6.1–7.3, [HTML primaire](https://arxiv.org/html/2607.08866v2), [notice arXiv](https://arxiv.org/abs/2607.08866v2).
- Z. Grujić, *A geometric measure-type regularity criterion for solutions to the 3D Navier–Stokes equations*, Nonlinearity 26 (2013), 289–296, [arXiv:1111.0217v5](https://arxiv.org/html/1111.0217v5), [DOI](https://doi.org/10.1088/0951-7715/26/1/289).
- R. Guberović, *Smoothness of Koch–Tataru solutions to the Navier–Stokes equations revisited*, DCDS 27 (2010), 231–236, [page éditeur](https://www.aimsciences.org/article/doi/10.3934/dcds.2010.27.231), [DOI](https://doi.org/10.3934/dcds.2010.27.231).
- A. Yu. Solynin, *Ordering of sets, hyperbolic metric, and harmonic measure*, POMI 237 (1997), 129–147 ; J. Math. Sci. 95 (1999), 2256–2266, [source primaire](https://www.mathnet.ru/eng/znsl433), [DOI](https://doi.org/10.1007/BF02172470).

## Conclusion de la passe

**Résultat positif borné :** les conversions volume–sparseness, 3D–1D, analyticity–radius et les deux cas harmoniques ferment un lemme conditionnel exact avec seuil synchronisé.

**Résultat négatif :** l’usage de \(s=t+T_t\) avant de savoir si \(s<T^*\) est le premier trou temporel décisif ; la propriété d’échappement y est appliquée hors de son domaine dans la branche favorable de prolongement.

**État recommandé :** `CONTINUER` sur l’uniformité amont de (49). Réparer localement l’endgame en réintroduisant explicitement les branches (i)/(ii) du critère primaire et le seuil (Uth).
