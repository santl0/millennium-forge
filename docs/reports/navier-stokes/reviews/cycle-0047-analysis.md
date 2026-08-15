# Cycle 0047 — audit de la dérenormalisation Type I

Date : 2026-08-15.

Statut : AI_INTERNAL_DERIVATION; aucun résultat Clay, aucune simulation.

## Verdict

La transformation proposée est exacte. Soit \(\kappa>0\) et soit
\((Z,\Pi)\) une solution distributionnelle de

\[
 \partial_sZ-\Delta_y Z+\operatorname{div}_y(Z\otimes Z)
 +\nabla_y\Pi+\kappa(1+y\cdot\nabla_y)Z=0,
 \qquad \operatorname{div}_yZ=0,                 \tag{1}
\]

sur \(\mathbb R^3\times(-\infty,0]\). Posons

\[
 r(s)=e^{-\kappa s},\qquad
 \tau(s)=\frac{1-r(s)^2}{2\kappa},\qquad
 x=r(s)y,                                        \tag{2}
\]

et

\[
 v(x,\tau)=r(s)^{-1}Z(y,s),\qquad
 q(x,\tau)=r(s)^{-2}\Pi(y,s).                    \tag{3}
\]

Alors \((x,\tau)\) parcourt exactement
\(\mathbb R^3\times(-\infty,0]\), et

\[
 \boxed{
 \partial_\tau v-\Delta_xv+\operatorname{div}_x(v\otimes v)
 +\nabla_xq=0,\qquad \operatorname{div}_xv=0.}   \tag{4}
\]

Le changement de variables préserve :

- la formulation distributionnelle sur chaque compact;
- la suitability locale et l'inégalité locale d'énergie;
- la jauge globale de Riesz, si elle est effectivement héritée de
  l'extraction faible-étoile globale;
- la borne \(L^{3,\infty}\), avec égalité exacte de quasi-normes;
- la non-trivialité espace-temps obtenue au cycle 0046.

Il ne produit pas automatiquement une solution de Leray–Hopf ni une solution
mild au sens normé. La première clause non héritée dans la hiérarchie usuelle
est déjà celle d'une solution local-energy complète : la dérivation transmet
les bornes locales et l'inégalité d'énergie, mais le claim 0045 ne fournit
pas la convergence forte \(L^2_{\mathrm{loc}}\) vers une trace initiale
prescrite à chaque bord gauche fini. Si la définition retenue de
local-energy n'impose pas cette clause de trace, cette classe locale est
héritée; le premier manque incontestable devient alors
\(v(\tau)\in L^2(\mathbb R^3)\), nécessaire à Leray–Hopf. La formule mild
forte demande encore un raccord séparé à Duhamel dans l'endpoint
\(L^{3,\infty}\).

## 1. Horloge, domaine et jacobiens

Les dérivées exactes de (2) sont

\[
 r_s=-\kappa r,\qquad
 \tau_s=-\frac{2rr_s}{2\kappa}=r^2>0,\qquad
 x_s\big|_y=r_sy=-\kappa x.                     \tag{5}
\]

Comme \(s\leq0\), on a \(r\geq1\), puis

\[
 \tau=\frac{1-e^{-2\kappa s}}{2\kappa}\leq0.    \tag{6}
\]

Les endpoints sont corrects :

\[
 s=0\Longleftrightarrow r=1\Longleftrightarrow\tau=0,
 \qquad
 s\to-\infty\Longleftrightarrow\tau\to-\infty.  \tag{7}
\]

L'inverse est

\[
 r=\sqrt{1-2\kappa\tau},\qquad
 s=-\frac1{2\kappa}\log(1-2\kappa\tau).          \tag{8}
\]

Il n'y a donc ni perte d'un intervalle temporel fini, ni singularité
intérieure. Sur chaque intervalle temporel compact, \(r\) et \(r^{-1}\) sont
uniformément bornés.

À temps fixé,

\[
 dx=r^3\,dy,\qquad d\tau=r^2\,ds,
\]

d'où le jacobien espace-temps

\[
 \boxed{dx\,d\tau=r^5\,dy\,ds.}                 \tag{9}
\]

Le facteur \(r^5\), et non \(r^3\) ou \(r^2\), est celui requis pour les
formulations distributionnelle et énergétique.

## 2. Calcul différentiel exact

Les relations inverses de (3) sont

\[
 Z(y,s)=r\,v(x,\tau),\qquad
 \Pi(y,s)=r^2q(x,\tau),\qquad x=ry.              \tag{10}
\]

La dérivée temporelle doit être calculée à \(y\) fixé. Avec (5),

\[
 \begin{aligned}
 \partial_sZ\big|_y
 &=r_sv+r\bigl(\tau_sv_\tau+x_s\cdot\nabla_xv\bigr)\\
 &=r^3v_\tau-\kappa r(v+x\cdot\nabla_xv).        \tag{11}
 \end{aligned}
\]

Par ailleurs,

\[
 \begin{aligned}
 \Delta_yZ&=r^3\Delta_xv,\\
 \operatorname{div}_y(Z\otimes Z)
   &=r^3\operatorname{div}_x(v\otimes v),\\
 \nabla_y\Pi&=r^3\nabla_xq,\\
 (1+y\cdot\nabla_y)Z
   &=r(v+x\cdot\nabla_x)v.                       \tag{12}
 \end{aligned}
\]

Le dernier terme de (12), multiplié par \(\kappa\), annule exactement les
deux termes de dilatation négatifs de (11). Ainsi

\[
 \mathcal N_s[Z,\Pi](y,s)
 =r^3\mathcal N_\tau[v,q](x,\tau),               \tag{13}
\]

où \(\mathcal N_s\) et \(\mathcal N_\tau\) désignent respectivement les
membres gauches de (1) et (4). Le signe positif du drift dans (1), le signe
négatif de \(r_s\) et le signe positif de \(\tau_s\) sont tous nécessaires.

La divergence se transforme séparément selon

\[
 \operatorname{div}_yZ(y,s)
 =r^2\operatorname{div}_xv(x,\tau).              \tag{14}
\]

Elle est donc préservée dans les deux sens.

## 3. Formulation distributionnelle

La carte

\[
 \Phi:(y,s)\longmapsto(ry,\tau(s))               \tag{15}
\]

est un difféomorphisme lisse entre les cylindres ouverts
\(\mathbb R^3\times(-\infty,0)\). Tout compact du cylindre cible a un
préimage compact, car \(r\) y reste borné au-dessus et au-dessous.

Pour une fonction test vectorielle
\(\varphi\in C_c^\infty(\mathbb R^3\times(-\infty,0))\), posons

\[
 \psi(y,s)=r(s)^2\varphi(\Phi(y,s)).              \tag{16}
\]

Les identités (9) et (13) donnent formellement

\[
 \langle\mathcal N_s[Z,\Pi],\psi\rangle_{y,s}
 =\langle\mathcal N_\tau[v,q],\varphi\rangle_{x,\tau}.             \tag{17}
\]

L'identité reste valable par densité pour les distributions, car toutes les
opérations sont des compositions par un difféomorphisme lisse et des
multiplications par des fonctions lisses strictement positives. Les produits
\(Z\otimes Z\) et \(v\otimes v\) sont localement intégrables dans la classe
énergétique du cycle 0045. L'équation (4) est donc obtenue dans les
distributions, sans supposer que \(Z\) soit classique.

La valeur \(s=0\) n'intervient pas dans l'équation distributionnelle
intérieure. Si une trace est disponible, (2)–(3) donnent simplement

\[
 v(\cdot,0)=Z(\cdot,0)                            \tag{18}
\]

dans la même topologie; la transformation n'améliore pas cette topologie.

## 4. Pression et jauge de Riesz

Supposons d'abord que la pression renormalisée soit fixée globalement par

\[
 \Pi=\mathcal R_i\mathcal R_j(Z_iZ_j).            \tag{19}
\]

Les transformées de Riesz sont homogènes de degré zéro. Comme

\[
 Z_iZ_j(y,s)=r^2(v_iv_j)(ry,\tau),
\]

on obtient exactement

\[
 \Pi(y,s)
 =r^2\bigl[\mathcal R_i\mathcal R_j(v_iv_j)\bigr](ry,\tau),
\]

puis, par (3),

\[
 \boxed{q=\mathcal R_i\mathcal R_j(v_iv_j).}      \tag{20}
\]

Aucune nouvelle constante temporelle n'apparaît dans cette jauge. Si l'on
part seulement d'une pression locale définie modulo \(c(s)\), la
transformation produit la jauge \(r^{-2}c(s)\), encore constante en espace;
elle ne permet pas d'affirmer (20).

Dans l'application du cycle 0045, (20) est héritée à condition d'effectuer
une extraction globale, et pas seulement la décomposition locale
proche/harmonique. En effet,

\[
 Z_j\otimes Z_j
 \quad\text{est borné dans}\quad
 L^\infty_sL^{3/2,\infty}_x.                    \tag{21}
\]

Après extraction faible-étoile contre le prédual
\(L^1_sL^{3,1}_x\), la convergence forte locale \(L^3\) identifie la limite
de (21) à \(Z\otimes Z\). La bornitude des Riesz sur
\(L^{3/2,\infty}\), ou dualement sur \(L^{3,1}\), permet alors de passer
(19) à la limite. Sans ce ledger faible-étoile global, la seule équation de
Poisson locale laisse un reste harmonique non identifié.

Sous la borne critique,

\[
 \|q(\tau)\|_{L^{3/2,\infty}}
 \leq C_{\mathrm{Riesz}}
 \|v(\tau)\|_{L^{3,\infty}}^2.                  \tag{22}
\]

Les propriétés locales \(L^{3/2}\) de la pression suitable se transportent
également sur tout compact, puisque \(r\) y est borné.

## 5. Inégalité locale d'énergie

Posons

\[
 e_Z=\frac{|Z|^2}{2},\qquad e_v=\frac{|v|^2}{2}.
\]

L'inégalité adaptée du cycle 0045 est

\[
 \begin{aligned}
 \mathcal E_s[Z,\Pi]
 :={}&\partial_se_Z-\Delta_ye_Z+|\nabla_yZ|^2
 +\operatorname{div}_y[(e_Z+\Pi)Z]\\
 &+\kappa\operatorname{div}_y(ye_Z)-\kappa e_Z
 \leq0.                                           \tag{23}
 \end{aligned}
\]

Le terme \(-\kappa e_Z\) est indispensable : il vient de
\(Z\cdot(1+y\cdot\nabla)Z\) en dimension trois.

À partir de

\[
 e_Z=r^2e_v,\qquad
 \nabla_yZ=r^2\nabla_xv,
\]

on calcule

\[
 \begin{aligned}
 \partial_se_Z
 &=r^4\partial_\tau e_v
   -\kappa r^2(2e_v+x\cdot\nabla_xe_v),\\
 -\Delta_ye_Z&=-r^4\Delta_xe_v,\\
 |\nabla_yZ|^2&=r^4|\nabla_xv|^2,\\
 \operatorname{div}_y[(e_Z+\Pi)Z]
 &=r^4\operatorname{div}_x[(e_v+q)v],\\
 \kappa\operatorname{div}_y(ye_Z)-\kappa e_Z
 &=\kappa r^2(2e_v+x\cdot\nabla_xe_v).           \tag{24}
 \end{aligned}
\]

Les deux dernières contributions de dilatation s'annulent, d'où

\[
 \mathcal E_s[Z,\Pi](y,s)
 =r^4\mathcal E_\tau[v,q](x,\tau),               \tag{25}
\]

avec

\[
 \mathcal E_\tau[v,q]
 =\partial_\tau e_v-\Delta_xe_v+|\nabla_xv|^2
 +\operatorname{div}_x[(e_v+q)v].               \tag{26}
\]

Pour une fonction test non négative
\(\varphi\in C_c^\infty\), le test correspondant est

\[
 \psi(y,s)=r(s)\varphi(\Phi(y,s))\geq0.           \tag{27}
\]

Les facteurs \(r^4\), \(r\) et le jacobien \(r^5\) s'annulent exactement :

\[
 \langle\mathcal E_s,\psi\rangle_{y,s}
 =\langle\mathcal E_\tau,\varphi\rangle_{x,\tau}. \tag{28}
\]

Ainsi (23) implique l'inégalité locale standard, sans résidu de drift et
sans changement de signe.

## 6. Espaces locaux et notion suitable

Sur un intervalle temporel compact, les domaines spatiaux se correspondent
par des dilatations dont les rapports sont bornés. Par exemple,

\[
 \int_{B_R}|v(x,\tau)|^2\,dx
 =r\int_{B_{R/r}}|Z(y,s)|^2\,dy,                 \tag{29}
\]

et

\[
 \int_{B_R}|\nabla_xv|^2\,dx
 =r^{-1}\int_{B_{R/r}}|\nabla_yZ|^2\,dy.         \tag{30}
\]

Comme \(d\tau=r^2ds\), les facteurs supplémentaires restent bornés sur
chaque compact temporel. Il en résulte

\[
 Z\in L^\infty_{\mathrm{loc},s}L^2_{\mathrm{loc},y}
 \cap L^2_{\mathrm{loc},s}H^1_{\mathrm{loc},y}
 \Longleftrightarrow
 v\in L^\infty_{\mathrm{loc},\tau}L^2_{\mathrm{loc},x}
 \cap L^2_{\mathrm{loc},\tau}H^1_{\mathrm{loc},x}.                \tag{31}
\]

Avec (17), la pression locale et (28), une solution faible adaptée locale de
(1) devient donc une solution faible adaptée locale de Navier–Stokes
standard sur \(\mathbb R^3\times(-\infty,0)\). La trace à \(\tau=0\), si
elle est incluse, reste seulement celle déjà disponible pour \(Z(0)\).

## 7. Faible-\(L^3\) et non-trivialité

À temps fixé,

\[
 |\{x:|v(x,\tau)|>\lambda\}|
 =r^3|\{y:|Z(y,s)|>r\lambda\}|.
\]

En prenant le supremum sur \(\lambda>0\),

\[
 \boxed{
 \|v(\tau)\|_{L^{3,\infty}(\mathbb R^3)}
 =\|Z(s)\|_{L^{3,\infty}(\mathbb R^3)}.}         \tag{32}
\]

La borne Type I est donc exactement préservée, sans facteur dépendant de
\(\tau\). Plus généralement,

\[
 \|v(\tau)\|_{L^p}
 =r^{-1+3/p}\|Z(s)\|_{L^p}.                      \tag{33}
\]

La transformation est bijective à tout temps fini et multiplie le champ par
un scalaire strictement positif; elle préserve donc la non-nullité. Le
résultat espace-temps du cycle 0046 se transporte quantitativement. Pour
\(J\Subset(-\infty,0]\) et

\[
 \Omega_J=\{(x,\tau(s)):s\in J,\ x\in B_{r(s)}\},
\]

on a

\[
 \int_{\Omega_J}|v|^3\,dx\,d\tau
 =\int_Jr(s)^2\int_{B_1}|Z(y,s)|^3\,dy\,ds.      \tag{34}
\]

Si \(K_3(Z(s);B_1)>\gamma_w\) presque partout sur \(J\), alors

\[
 \int_{\Omega_J}|v|^3\,dx\,d\tau
 \geq\gamma_w^3\int_Jr(s)^2\,ds>0.              \tag{35}
\]

Ainsi \(v\not\equiv0\), sans aucune information forte sur la trace
\(v(0)=Z(0)\).

## 8. Distinction des classes de solutions

| Classe | Ce qui est requis | Statut après (2)–(3) |
|---|---|---|
| Faible distributionnelle | équation et divergence dans les distributions, produits localement intégrables | hérité exactement par (13)–(17) |
| Faible adaptée locale | classe énergétique locale, pression locale \(L^{3/2}\), inégalité locale d'énergie | hérité sur chaque compact par (28)–(31) |
| Local-energy / local Leray | en plus, bornes \(L^2_{\mathrm{uloc}}\), dissipation uniformément locale, décomposition de pression et trace initiale forte \(L^2_{\mathrm{loc}}\) selon la définition | les bornes spatiales sont accessibles depuis faible-\(L^3\); la clause de trace à un bord gauche prescrit n'est pas fournie par le claim 0045 |
| Leray–Hopf | énergie globale finie, dissipation globale et inégalité d'énergie globale depuis une donnée \(L^2\) | non hérité; faible-\(L^3\) n'implique pas \(L^2(\mathbb R^3)\) |
| Mild | formule de Duhamel depuis une trace globale dans une classe où le terme bilinéaire est défini, avec la continuité temporelle correspondante | non hérité; la formulation distributionnelle locale ne suffit pas à l'endpoint faible-\(L^3\) |

La borne faible-\(L^3\) implique bien une borne spatiale
\(L^2_{\mathrm{uloc}}\) :

\[
 \sup_{x_0}\int_{B(x_0,1)}|v(\tau)|^2
 \leq 3|B_1|^{1/3}\|v(\tau)\|_{L^{3,\infty}}^2. \tag{36}
\]

Avec la pression globale (20), l'inégalité locale standard permet aussi de
reconstruire des bornes de dissipation uniformément locales sur tout
intervalle temporel compact. Cela ne crée toutefois pas une convergence
forte \(L^2_{\mathrm{loc}}\) vers une trace choisie. Le cycle 0045 donne
seulement une continuité forte dans \(H^{-1}_{\mathrm{loc}}\) et une
continuité faible énergétique après choix de représentant.

L'échec Leray–Hopf est indépendant de cette subtilité. Un champ
divergence-free lisse près de l'origine, de la forme

\[
 w(x)=\chi(|x|)\frac{a\times x}{|x|^2},
\]

avec \(\chi=1\) pour \(|x|\) grand, appartient à \(L^{3,\infty}\) mais pas à
\(L^2(\mathbb R^3)\). Ce témoin est cinématique, pas une solution de
Navier–Stokes; il suffit à réfuter l'implication fonctionnelle
\(L^{3,\infty}\subset L^2\).

Enfin, la formule de Duhamel peut être écrite distributionnellement entre
deux temps finis, mais cela n'est pas encore la mildness normée utilisée par
les théories critiques. À l'endpoint \(L^{3,\infty}\), le semi-groupe de la
chaleur n'est pas fortement continu sur tout l'espace et l'estimation brute
du terme bilinéaire est limite en temps. Il faut déclarer une classe
temporelle, une trace faible-étoile ou un sous-espace de continuité, puis
prouver que le reste calorique homogène est nul.

## 9. Première hypothèse non héritée

La chaîne certaine issue des cycles 0045–0046 est

\[
 \begin{aligned}
 &Z\text{ ancienne renormalisée, suitable locale,}
 \quad Z\in L^\infty_sL^{3,\infty}_y,
 \quad Z\not\equiv0\\
 &\Longrightarrow
 v\text{ ancienne standard, suitable locale,}
 \quad v\in L^\infty_\tau L^{3,\infty}_x,
 \quad v\not\equiv0.
 \end{aligned}                                                     \tag{37}
\]

Le premier manque dépend ensuite du nom de classe visé :

1. pour une solution local-energy au sens incluant une donnée de Cauchy à
   chaque bord gauche, il manque la trace forte
   \(L^2_{\mathrm{loc}}\) à ce temps;
2. pour Leray–Hopf, il manque déjà l'énergie globale finie;
3. pour mild, il manque la formule de Duhamel dans une topologie critique
   temporellement fermée.

Le manque le plus proche de (37) est donc la clause de trace de la classe
local-energy, non un signe, un jacobien, la pression ou l'inégalité locale.
Cette trace n'est pas nécessaire pour la non-trivialité espace-temps, mais
elle peut être nécessaire pour raccorder un théorème de Cauchy ou de
backward uniqueness formulé dans une classe plus forte.

## 10. Passe contradictoire

1. **Mauvaise horloge.** Avec \(\tau=(1-r^2)/(2\kappa)\), on a
   \(\tau_s=r^2>0\). Le choix \((r^2-1)/(2\kappa)\) inverse le temps et ne
   produit pas (4).
2. **Dérivée au mauvais point fixe.** Oublier
   \(x_s|_y=-\kappa x\) laisse un drift résiduel. La dérivée de (11) est à
   \(y\) fixé, pas à \(x\) fixé.
3. **Amplitude inversée.** La relation correcte est \(Z=rv\), donc
   \(v=r^{-1}Z\). Le choix \(v=rZ\) détruit à la fois (4) et l'invariance
   faible-\(L^3\).
4. **Pression.** Il faut \(\Pi=r^2q\), donc \(q=r^{-2}\Pi\). Une jauge locale
   ne devient pas spontanément la jauge globale de Riesz.
5. **Jacobiens séparés.** \(dx=r^3dy\) et \(d\tau=r^2ds\); omettre l'un des
   deux donne de mauvais poids dans (17), (28) et (34).
6. **Énergie du drift.** Le drift énergétique est
   \(\kappa\operatorname{div}(ye_Z)-\kappa e_Z\), pas seulement le terme de
   divergence. Sans \(-\kappa e_Z\), (24) ne s'annule pas.
7. **Endpoint temporel.** Le domaine est exactement
   \((-\infty,0]\); \(s=0\) est envoyé sur \(\tau=0\), tandis que
   \(s=-\infty\) n'est jamais un temps fini.
8. **Local contre global.** Une équivalence de normes sur chaque compact ne
   fournit aucune énergie globale. Le facteur de (33) ne répare pas une
   intégrale \(L^2\) infinie.
9. **Suitable contre mild.** L'inégalité locale d'énergie et la pression de
   Riesz ne prouvent pas à elles seules la continuité forte du semi-groupe à
   l'endpoint ni une identité de Duhamel normée.
10. **Non-trivialité contre trace.** (35) prouve
    \(v\not\equiv0\), mais reste compatible avec \(v(0)=0\) dans
    \(H^{-1}_{\mathrm{loc}}\). Réintroduire la porte de trace avant la
    non-trivialité répéterait l'erreur corrigée au cycle 0046.
11. **Clay.** Une solution ancienne suitable, non triviale et bornée dans
    faible-\(L^3\) n'est exclue par aucun théorème de rigidité général
    enregistré. La dérenormalisation ferme une conjugaison, pas le problème
    de régularité globale.

## Conclusion logique

La dérenormalisation exacte ferme l'arête

\[
 \boxed{
 \text{ancienne renormalisée suitable, faible-}L^3,\ \text{non nulle}
 \Longrightarrow
 \text{ancienne standard suitable, faible-}L^3,\ \text{non nulle}.} \tag{38}
\]

Verdict de revue : CONTINUER pour cette arête. RÉVISER toute affirmation
Leray–Hopf, local-energy avec trace forte, ou mild qui serait attachée
automatiquement à (38). Le prochain raccord analytique doit choisir la classe
exacte exigée par le théorème de rigidité visé et démontrer sa première clause
absente, sans réouvrir les calculs de signe et de jacobien désormais fermés.
