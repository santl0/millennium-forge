# Cycle 0017 — audit de la chaîne d’énergie tronquée (20)–(40)

Date de la passe : 2026-08-14

Source auditée : Zoran Grujić, *Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier–Stokes Equations*, [arXiv:2607.08866v2](https://arxiv.org/abs/2607.08866v2), principalement les équations (20)–(40).

Portée : passage de la borne localisée du stretching (22) à l’enveloppe de distribution (40), avec constantes, seuils, temps, troncature et scaling suivis.

> **Statut de la revue.** Cette passe contradictoire est produite par un agent de la même famille de modèle que les autres passes de Millennium Forge. Elle **n’est ni une revue externe ni une réplication indépendante**.

## Verdict

Sous une version dimensionnée, uniforme en temps et effectivement démontrée de la borne localisée (22), la chaîne algébrique (23)–(40) est réparable et conserve les bons exposants :

\[
\text{source}\sim
\frac{\lambda^{3/2}}{\mathcal L_\lambda^{3/2}},
\qquad
\text{damping}\sim\lambda E_\lambda,
\qquad
E_\lambda\sim
\frac{\lambda^{1/2}}{\mathcal L_\lambda^{3/2}},
\]

puis

\[
|\{\omega>2\lambda\}|
\lesssim
\frac{\lambda^{-3/2}}{\mathcal L_\lambda^{3/2}}.
\]

Il n’y a donc pas d’erreur de puissance dans l’interpolation, Young, la coercivité ou Grönwall. En revanche, trois affirmations quantitatives du texte ne sont pas exactes telles qu’écrites :

1. juste avant (21), la borne \(\phi(2^jR)\le2\phi(R)\) est fausse au dernier anneau dyadique pour tout \(R>0\) fini avec la définition donnée de \(N\) ; une constante \(3\) convient pour \(R\) assez petit ;
2. après (25), le seuil d’absorption n’est pas « absolu » : il dépend au moins exponentiellement du rapport critique \(C_\alpha/\nu\), des constantes fonctionnelles et des échelles de normalisation ;
3. la même phrase affirme une absorption sur tout \((0,T^*)\), tandis que (22) n’est supposée que sur \((T^*-\epsilon,T^*)\). Le raisonnement de Grönwall n’a besoin que de ce dernier intervalle, mais le quantificateur affiché est faux.

En outre, le coefficient \(C_1\) de (31) cache nécessairement un facteur \(C_\alpha^{3/2}\). Or le \(C_0\) de (22), correspondant ici à \(C_\alpha\), dépend lui-même du contrôle critique de la vorticité et de la norme géométrique. La puissance apparente \(M_0^{3/2}\) de (37) n’est donc pas la dépendance totale en \(M_0\) tant que (22) n’est pas quantitativement fermée.

Le premier maillon réellement conditionnel reste ainsi (22). Le lemme exact minimal qui en découle est formulé en section 7.

## 1. Équation, domaine et notion de solution

Cette passe fixe :

- Navier–Stokes incompressible, non forcé, sur \(\mathbb R^3\) ;
- viscosité \(\nu>0\) ;
- solution classique sur un intervalle \(I=[t_0,T^*)\), avec décroissance/intégrabilité suffisante pour toutes les intégrations par parties ;
- vorticité vectorielle \(\boldsymbol\omega=\nabla\times u\), magnitude \(\omega=|\boldsymbol\omega|\), direction \(\xi=\boldsymbol\omega/\omega\) là où \(\omega>0\) ;
- tenseur de déformation \(S=(\nabla u+\nabla u^{T})/2\) et stretching scalaire \(\alpha=\xi\cdot S\xi\).

La magnitude vérifie l’inégalité de Kato

\[
(\partial_t+u\cdot\nabla-\nu\Delta)\omega
\le\alpha\omega.
\tag{V}
\]

Pour une solution classique, tester (V) par une approximation lisse de \((\omega-\lambda)_+\) puis passer à la limite est standard. La même opération n’est pas automatique pour une solution de Leray–Hopf : elle requerrait une construction renormalisée de l’équation de vorticité et le contrôle des commutateurs de mollification. Le résultat ci-dessous n’est donc pas affirmé, sans travail supplémentaire, pour une solution faible.

Une force extérieure ajouterait le rotationnel de la force à (V) et un terme supplémentaire à l’énergie tronquée. Cette passe ne couvre pas ce cas.

## 2. Normalisation dimensionnelle de l’entrée (22)

Les dimensions physiques utiles sont

\[
[u]=LT^{-1},\quad
[\omega]=[\alpha]=T^{-1},\quad
[\nu]=L^2T^{-1}.
\]

Puisque

\[
\|\alpha\|_{L^{3/2,\infty}}
\sim [\alpha]\,L^2,
\]

la constante d’une borne telle que (22) a la même dimension que \(\nu\). Un logarithme de rayon exige par ailleurs une longueur de référence.

Fixons :

- une longueur \(R_*>0\) ;
- un coefficient de profil \(K_{\rm prof}>0\), de dimension \(L^2T^{-1}\) ;
- \(\lambda_*=K_{\rm prof}/R_*^2\), de dimension \(T^{-1}\) ;
- une constante critique \(C_\alpha>0\), de dimension \(L^2T^{-1}\).

On suppose que, pour tout \(t\in I\) et tout \(\lambda\ge\lambda_{\rm prof}\),

\[
A_\lambda(t):=\{x:\omega(x,t)>\lambda\}
\subset B_{r_\lambda},
\qquad
r_\lambda=\left(\frac{K_{\rm prof}}{\lambda}\right)^{1/2}.
\tag{P}
\]

On suppose aussi la version dimensionnée de (22) :

\[
\boxed{
\|\alpha(\cdot,t)\|_{L^{3/2,\infty}(B_r)}
\le
\frac{C_\alpha}{\log(eR_*/r)}
}
\tag{H22}
\]

pour \(0<r\le R_*\), uniformément en \(t\in I\). Dès que \(\lambda\ge\max\{\lambda_{\rm prof},\lambda_*\}\),

\[
\boxed{
\|\alpha(\cdot,t)\|_{L^{3/2,\infty}(A_\lambda(t))}
\le\frac{C_\alpha}{\mathcal L_\lambda},
\qquad
\mathcal L_\lambda
=1+\frac12\log\frac{\lambda}{\lambda_*}.
}
\tag{A22}
\]

Cette écriture remplace les expressions dimensionnellement ambiguës \(|\log R|\) et \(\log\lambda\).

### Audit limité de (20)–(22)

La réorganisation de la somme dans (20) est correcte à constante universelle près :

\[
\sum_{k=1}^{N}4^{-k}\sum_{j=1}^{k+1}\phi(2^jR)
=
\sum_{j=1}^{N+1}\phi(2^jR)
\sum_{k=\max(1,j-1)}^{N}4^{-k}.
\]

Cependant, avec

\[
N=\left\lfloor\frac12\log_2(R_*/R)\right\rfloor,
\]

le dernier rayon peut atteindre \(2\sqrt{RR_*}\). Pour

\[
\phi(r)=\frac1{\log(R_*/r)},
\]

on obtient au bord

\[
\frac{\phi(2\sqrt{RR_*})}{\phi(R)}
=
\frac{\log(R_*/R)}{\frac12\log(R_*/R)-\log2}
>2.
\]

La constante \(2\) annoncée avant (21) est donc littéralement fausse. Si \(R/R_*\le2^{-6}\), ce ratio est au plus \(3\), ce qui répare (21) sans modifier sa conclusion. L’argument présenté dans le papier est compatible avec (H22) modulo cette correction et les constantes des extensions BMO/commutateurs, mais la présente passe **prend (H22) comme hypothèse** : elle ne certifie pas indépendamment toute la preuve du théorème 4.1.

## 3. Identité tronquée : (23)

Posons

\[
f_\lambda=(\omega-\lambda)_+,
\qquad
E_\lambda(t)=\|f_\lambda(t)\|_2^2,
\qquad
G_\lambda(t)=\|\nabla f_\lambda(t)\|_2.
\]

Le support essentiel de \(f_\lambda\) est contenu dans \(A_\lambda(t)\). L’incompressibilité annule le transport et donne

\[
\frac12E_\lambda'(t)+\nu G_\lambda(t)^2
\le
\int_{A_\lambda(t)}\alpha f_\lambda^2
+\lambda\int_{A_\lambda(t)}\alpha f_\lambda.
\tag{23q}
\]

La décomposition vient simplement de \(\omega=f_\lambda+\lambda\) sur \(A_\lambda\). Lorsque \(\alpha\) change de signe, les majorations suivantes s’appliquent aux valeurs absolues des deux termes ; l’absence de barres dans (23)–(27) est une omission notationnelle, pas une amélioration par positivité.

## 4. Absorption du terme quadratique : (24)–(26)

Notons :

- \(C_H\) la constante de Hölder–Lorentz
  \(L^{3/2,\infty}\cdot L^{3,1}\to L^1\) ;
- \(S_L\) la constante de Sobolev–Lorentz
  \(\|g\|_{L^{6,2}}\le S_L\|\nabla g\|_2\).

Avec la convention de norme de réarrangement utilisée dans le papier,

\[
\|f_\lambda^2\|_{L^{3,1}}
=\|f_\lambda\|_{L^{6,2}}^2
\]

est une identité exacte. Par conséquent,

\[
\left|\int\alpha f_\lambda^2\right|
\le
C_H\frac{C_\alpha}{\mathcal L_\lambda}
S_L^2G_\lambda^2.
\tag{N}
\]

L’absorption de la moitié de la dissipation exige

\[
\boxed{
\mathcal L_\lambda
\ge
\frac{2C_HS_L^2C_\alpha}{\nu}.
}
\tag{Abs}
\]

Un seuil suffisant et explicite est donc

\[
\boxed{
\lambda_{\rm abs}
=
\lambda_*
\exp\!\left(
2\max\left\{0,
\frac{2C_HS_L^2C_\alpha}{\nu}-1
\right\}
\right).
}
\tag{labs}
\]

Le seuil final doit aussi dépasser \(\lambda_{\rm prof}\). Il est uniforme en temps si, et seulement si, \(C_\alpha,K_{\rm prof},R_*\) et la plage de validité de (H22) le sont.

Sous (Abs), (23q) devient

\[
\frac12E_\lambda'+\frac\nu2G_\lambda^2
\le
\lambda\int_{A_\lambda}|\alpha|f_\lambda.
\tag{26q}
\]

Le papier affirme après (25) l’existence d’un niveau « absolute, time-independent » valable sur \((0,T^*)\). Seule la partie « time-independent » est justifiée, et seulement sur \(I=(T^*-\epsilon,T^*)\). Le seuil (labs) montre explicitement sa dépendance, généralement exponentielle, en \(C_\alpha/\nu\).

## 5. Interpolation et Young : (27)–(32)

Supposons

\[
M:=\sup_{t\in I}\|\omega(\cdot,t)\|_{L^{3/2,\infty}}<\infty.
\tag{M}
\]

Comme \(0\le f_\lambda\le\omega\), sa norme faible est au plus \(M\). L’interpolation réelle

\[
(L^{3/2,\infty},L^{6,2})_{2/3,1}=L^{3,1}
\]

est compatible avec

\[
\frac13
=\frac{1/3}{3/2}+\frac{2/3}{6}.
\]

Si \(C_I\) désigne sa constante,

\[
\|f_\lambda\|_{L^{3,1}}
\le
C_IM^{1/3}(S_LG_\lambda)^{2/3}.
\tag{I}
\]

Ainsi,

\[
\lambda\int_{A_\lambda}|\alpha|f_\lambda
\le
a_\lambda G_\lambda^{2/3},
\]

avec

\[
a_\lambda
=C_HC_IS_L^{2/3}
C_\alpha M^{1/3}
\frac{\lambda}{\mathcal L_\lambda}.
\tag{a}
\]

La forme exacte de Young utilisée ici est

\[
ax^{2/3}
\le
\varepsilon x^2
+\frac{2}{3\sqrt{3\varepsilon}}a^{3/2}.
\tag{Y}
\]

Pour \(\varepsilon=\nu/4\),

\[
a_\lambda G_\lambda^{2/3}
\le
\frac\nu4G_\lambda^2
+F_\lambda,
\]

où

\[
\boxed{
F_\lambda
=
\frac{4}{3\sqrt3}\nu^{-1/2}
(C_HC_IS_L^{2/3}C_\alpha)^{3/2}
M^{1/2}
\frac{\lambda^{3/2}}{\mathcal L_\lambda^{3/2}}.
}
\tag{F}
\]

On retrouve exactement la puissance de \(\lambda\) et le facteur \(\nu^{-1/2}\) de (31). La constante notée \(C_1\) dans le papier absorbe nécessairement

\[
(C_HC_IS_L^{2/3}C_\alpha)^{3/2}.
\]

Elle n’est donc pas universelle si \(C_\alpha\) ne l’est pas. En particulier, comme le texte de (22) fait dépendre \(C_0\) de \(M\), le facteur explicite \(M^{1/2}\) de (31) ne décrit pas la dépendance totale en \(M\).

Après Young,

\[
\boxed{
\frac12E_\lambda'
+\frac\nu4G_\lambda^2
\le F_\lambda.
}
\tag{32q}
\]

## 6. Coercivité sur le support : (33)–(35)

Notons \(S_6\) la constante de l’injection homogène

\[
\|g\|_6\le S_6\|\nabla g\|_2.
\]

Il est prudent de la distinguer de \(S_L\). Par Hölder sur le support de \(f_\lambda\),

\[
E_\lambda
\le
\|f_\lambda\|_6^2|A_\lambda|^{2/3}
\le
S_6^2G_\lambda^2U_\lambda^{2/3}.
\tag{33q}
\]

La norme faible (M) donne exactement

\[
U_\lambda(t)
\le\left(\frac M\lambda\right)^{3/2},
\qquad
U_\lambda(t)^{2/3}\le\frac M\lambda.
\]

Il s’ensuit

\[
\boxed{
G_\lambda^2
\ge
\frac{\lambda}{S_6^2M}E_\lambda.
}
\tag{34q}
\]

Cette « Poincaré sur superniveau » ne requiert aucune régularité géométrique de \(A_\lambda\). Elle est la combinaison robuste support–Sobolev. L’exposant \(\lambda^1\) est imposé par la criticité \(L^{3/2,\infty}\).

En multipliant (32q) par deux puis en utilisant (34q), on obtient

\[
\boxed{
E_\lambda'
+d_\lambda E_\lambda
\le2F_\lambda,
\qquad
d_\lambda=\frac{\nu\lambda}{2S_6^2M}.
}
\tag{35q}
\]

Le coefficient de Grönwall de (35) est donc correct. Il dépend de \(\lambda\), de \(\nu\) et de \(M\), mais pas du temps si (M) est uniforme. Il ne dépend pas de la forme du superniveau.

## 7. Lemme conditionnel exact

### Lemme 0017-A — amélioration de distribution par énergie tronquée

Soit une solution classique du système non forcé sur \(\mathbb R^3\times[t_0,T^*)\). Supposons (P), (H22) et (M), avec constantes uniformes en temps. Définissons

\[
\Lambda_{\rm anc}=\|\omega(\cdot,t_0)\|_\infty
\]

et

\[
\lambda_{\min}
=\max\{\lambda_{\rm prof},\lambda_*,
\lambda_{\rm abs},\Lambda_{\rm anc}\}.
\]

Alors, pour tout \(\lambda\ge\lambda_{\min}\) et tout \(t\in[t_0,T^*)\),

\[
\boxed{
E_\lambda(t)
\le
C_E
\left(\frac{C_\alpha}{\nu}\right)^{3/2}
M^{3/2}
\frac{\lambda^{1/2}}{\mathcal L_\lambda^{3/2}},
}
\tag{37q}
\]

où

\[
C_E
=\frac{16}{3\sqrt3}
S_6^2(C_HC_IS_L^{2/3})^{3/2}.
\]

En conséquence,

\[
\boxed{
|\{x:\omega(x,t)>2\lambda\}|
\le
C_E
\left(\frac{C_\alpha}{\nu}\right)^{3/2}
M^{3/2}
\frac{\lambda^{-3/2}}{\mathcal L_\lambda^{3/2}}.
}
\tag{40q}
\]

### Preuve et transitoire exact

Pour tout niveau admissible, (35q) donne

\[
E_\lambda(t)
\le
e^{-d_\lambda(t-t_0)}E_\lambda(t_0)
+\frac{2F_\lambda}{d_\lambda}
\left(1-e^{-d_\lambda(t-t_0)}\right).
\tag{G}
\]

Comme \(\lambda\ge\Lambda_{\rm anc}\), \(f_\lambda(t_0)=0\) et le premier terme disparaît. Puis

\[
\frac{2F_\lambda}{d_\lambda}
=\frac{4S_6^2M}{\nu\lambda}F_\lambda,
\]

ce qui donne (37q) après substitution de (F). Sur \(A_{2\lambda}\), on a \(f_\lambda>\lambda\), donc

\[
|A_{2\lambda}|
\le\lambda^{-2}E_\lambda,
\]

et (40q) suit.

Si \(E_\lambda(t_0)\ne0\), le terme transitoire de (G) doit être conservé. Il n’est pas permis de le supprimer en invoquant seulement la régularité au temps \(t_0\) : il faut aussi choisir \(\lambda\ge\|\omega(t_0)\|_\infty\).

Enfin, relabeller \(2\lambda\) en \(\Lambda\) modifie la constante et remplace \(\mathcal L_\lambda\) par

\[
1+\frac12\log\frac{\Lambda}{2\lambda_*}.
\]

L’écriture (40) en \((\log\Lambda)^{-3/2}\) n’est qu’une forme asymptotique nondimensionnée.

## 8. Lois d’échelle

Sous le scaling Navier–Stokes

\[
u_\rho(x,t)=\rho u(\rho x,\rho^2t),
\qquad
\omega_\rho(x,t)=\rho^2\omega(\rho x,\rho^2t),
\qquad
\alpha_\rho(x,t)=\rho^2\alpha(\rho x,\rho^2t),
\]

la viscosité reste inchangée et

\[
\|\omega_\rho\|_{L^{3/2,\infty}}
=\|\omega\|_{L^{3/2,\infty}},
\qquad
\|\alpha_\rho\|_{L^{3/2,\infty}}
=\|\alpha\|_{L^{3/2,\infty}}.
\]

Les paramètres se transforment comme

\[
R_{*,\rho}=\rho^{-1}R_*,
\quad
K_{{\rm prof},\rho}=K_{\rm prof},
\quad
\lambda_{*,\rho}=\rho^2\lambda_*,
\quad
\lambda_\rho=\rho^2\lambda,
\]

tandis que \(M,C_\alpha,\nu\) sont invariants. Ainsi \(\mathcal L_{\lambda,\rho}=\mathcal L_\lambda\) et la condition (Abs) est critique.

Pour les énergies tronquées,

\[
E_{\lambda_\rho}[\omega_\rho](t)
=\rho E_\lambda[\omega](\rho^2t),
\qquad
G_{\lambda_\rho}[\omega_\rho](t)^2
=\rho^3G_\lambda[\omega](\rho^2t)^2.
\]

On vérifie alors :

- \(F_{\lambda_\rho}=\rho^3F_\lambda\) ;
- \(d_{\lambda_\rho}=\rho^2d_\lambda\) ;
- le membre droit de (37q) est multiplié par \(\rho\) ;
- le membre droit de (40q) est multiplié par \(\rho^{-3}\).

Chaque équation est donc exactement compatible avec le scaling. L’amélioration logarithmique ne provient pas d’une puissance subcritique cachée, mais de l’hypothèse dimensionnellement critique (H22).

## 9. Passe contradictoire

### 9.1 Profil critique saturant les puissances

Soit \(\psi\in C_c^\infty(B_1)\) non nulle et, avec \(r_\lambda=(K_{\rm prof}/\lambda)^{1/2}\), considérons le contre-profil d’échelle

\[
f_\lambda(x)=\lambda\psi(x/r_\lambda).
\]

Alors

\[
\|f_\lambda\|_{L^{3/2,\infty}}\sim K_{\rm prof},
\qquad
E_\lambda\sim K_{\rm prof}^{3/2}\lambda^{1/2},
\qquad
G_\lambda^2\sim K_{\rm prof}^{1/2}\lambda^{3/2}.
\]

En particulier,

\[
\frac{G_\lambda^2}{E_\lambda}\sim\frac\lambda{K_{\rm prof}}.
\]

Ce test confirme que le coefficient linéaire en \(\lambda\) de (34) est optimal par scaling. Aucune amélioration algébrique de la coercivité ne peut être obtenue à partir du seul contrôle faible \(L^{3/2}\). Le gain de (40) doit donc venir entièrement du facteur logarithmique de (H22).

### 9.2 Quantificateur temporel

Prenons une fonction abstraite \(a(t)\) satisfaisant

\[
a(t)\le C_\alpha/\mathcal L_\lambda
\quad\text{seulement pour }t\in[t_0,T^*),
\]

et arbitrairement grande avant \(t_0\). Elle satisfait exactement l’hypothèse temporelle de (22), mais réfute l’assertion d’absorption sur \((0,T^*)\). L’ODE démarrée à \(t_0\) reste valide : le défaut de quantificateur est réel mais localisé.

### 9.3 Dépendance cachée de \(C_1\)

Remplaçons \(C_\alpha\) par \(qC_\alpha\) sans changer \(M\). Le terme linéaire avant Young est multiplié par \(q\), donc son reste après Young est multiplié par \(q^{3/2}\). Toute version de (31) où \(C_1\) serait universel et indépendant de \(C_\alpha\) est immédiatement réfutée. La constante (F) expose la dépendance nécessaire.

### 9.4 Troncature et passage faible

Les constantes de (23q)–(40q) sont uniformes en \(\lambda\) une fois les dépendances explicites séparées ; aucun cutoff spatial auxiliaire n’est utilisé. En revanche, pour dériver ces formules depuis une solution non classique par mollification, il faudrait démontrer que les commutateurs de transport, la chaîne de Kato et le terme \(\alpha\omega\) convergent avec un contrôle uniforme. Le papier raisonne avant \(T^*\) sur une solution classique, ce qui évite ce passage ; la chaîne ne peut pas être transportée telle quelle aux solutions de Leray–Hopf.

## 10. Statut maillon par maillon

| Maillon | Statut | Observation exacte |
|---|---|---|
| (20) → (21) | Réparable | Réordonnancement correct ; constante \(2\) fausse au bord dyadique, \(3\) suffit à petite échelle. |
| (21) → (22) | Conditionnel | Nécessite toutes les constantes BMO, extension et Calderón–Zygmund uniformes, ainsi qu’une longueur de référence. Pris comme (H22) ici. |
| (22) → (25) | Correct après normalisation | Le rayon de profil et le logarithme doivent être dimensionnés. |
| (23) | Correct pour solution classique | Valeurs absolues de \(\alpha\) requises dans les majorations. |
| (24) → (26) | Correct conditionnellement | Seuil donné par (labs), non absolu et valide seulement sur l’intervalle de (H22). |
| (27) → (32) | Correct | Interpolation \(\theta=2/3\), Young \(3\)–\(3/2\), facteur caché \(C_\alpha^{3/2}\). |
| (33) → (34) | Correct et critique | Coercivité support–Sobolev, constante \(S_6^2M\), exposant \(\lambda\) optimal. |
| (34) → (37) | Correct | Coefficient \(d_\lambda=\nu\lambda/(2S_6^2M)\) ; terme initial nul seulement au-dessus de \(\Lambda_{\rm anc}\). |
| (37) → (40) | Correct | Chebyshev à \(2\lambda\) ; relabelling et logarithme changent la constante et le seuil. |

## 11. Écart avec le problème Clay et prochain verrou

Le lemme 0017-A est un résultat conditionnel pour une solution classique non forcée sur \(\mathbb R^3\). Il ne démontre pas que les hypothèses (P), (H22) et (M) sont satisfaites par une solution Clay arbitraire. En particulier :

- le contrôle faible critique (M) est supposé, non produit par l’énergie de Leray ;
- la concentration dans un unique cœur \(B_{r_\lambda}\) est supposée ;
- la borne logarithmique du stretching (H22) reste le premier lemme dynamique non certifié par cette passe ;
- \(C_\alpha\) peut dépendre de \(M\) et de la norme \(\mathrm{bmo}_\phi\), ce qui doit être explicité avant toute comparaison quantitative ultérieure ;
- la formulation périodique et les domaines bornés demandent des adaptations distinctes ;
- aucune conclusion n’est obtenue pour des solutions faibles sans lemme de renormalisation.

Le prochain verrou de meilleure valeur informationnelle est une révision indépendante et quantitative de (22), en commençant par la validité exacte de l’extension BMO locale avec petite seminorme, puis par chaque queue du commutateur avec une échelle \(R_*\) fixée. Si (H22) survit, la chaîne énergétique ci-dessus la transmet sans perte d’exposant jusqu’à (40).

## Source primaire

- Z. Grujić, *Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier–Stokes Equations*, arXiv:2607.08866v2, sections 4–5, [HTML primaire](https://arxiv.org/html/2607.08866v2), [notice arXiv](https://arxiv.org/abs/2607.08866v2).
- R. A. Hunt, *On \(L(p,q)\) spaces*, L’Enseignement Mathématique 12(4), 249–276 (1966), référence primaire employée par l’article pour les espaces de Lorentz.

## Conclusion de la passe

**Résultat positif borné :** le lemme conditionnel 0017-A donne une version exacte, dimensionnée et invariante d’échelle de (23)–(40), avec seuil d’absorption, transitoire et constantes exposés.

**Résultats négatifs :** la constante \(2\) avant (21), l’adjectif « absolu » et le quantificateur temporel après (25) sont réfutés tels qu’écrits. La dépendance de \(C_1\) en \(C_\alpha^{3/2}\) ne peut pas être omise dans un audit quantitatif.

**État recommandé :** `CONTINUER`, mais considérer (40) comme conditionnel à une preuve quantitative complète de (22), et non comme une amélioration a priori autonome.
