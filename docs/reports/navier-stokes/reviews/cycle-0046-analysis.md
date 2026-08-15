# Cycle 0046 — capture Type I sur une fenêtre translatée

Date : 2026-08-15.

Statut : AI_INTERNAL_DERIVATION; aucun résultat Clay, aucune simulation.

## Verdict

Sous les hypothèses pointwise du claim
NS-TYPE-I-WEAK-L3-PARABOLIC-CORE-CAPTURE, la capture du cycle 0041 vaut à
chaque temps d'une fenêtre normalisée translatée, pas seulement à sa tranche
terminale. Si

\[
 Z_j(s)=Q_{L_j}U(\sigma_j+s),\qquad s\in J,
\]

où \(J\) est un intervalle borné non dégénéré et \(L_j\geq1\), alors, pour
\(j\) assez grand,

\[
 \boxed{
 K_3(Z_j(s);B_1)=K_3(U(\sigma_j+s);B_1)>\gamma_w
 \quad\text{pour tout }s\in J.}                 \tag{1}
\]

Sous un simple supremum essentiel en temps, la formulation conservatrice de
(1) est « pour presque tout \(s\in J\) ». Cela suffit entièrement.

La convergence forte \(L^3_{\mathrm{loc}}\) espace-temps du cycle 0045
donne

\[
 \boxed{
 \|Z\|_{L^3(B_1\times J)}^3
 \geq |J|\gamma_w^3>0.}                         \tag{2}
\]

La limite renormalisée est donc non triviale sans convergence forte d'une
trace. En revanche, (2) ne donne ni \(Z(0)\neq0\), ni une minoration de
\(K_3(Z(0);B_1)\). Le verrou de trace du cycle 0045 reste pertinent seulement
si un argument ultérieur exige spécifiquement une donnée terminale non nulle;
il ne doit plus être placé avant la seule non-trivialité de la solution
ancienne.

Le premier trou exact dans la chaîne 0041–0045 est un raccord de
quantificateurs : le cycle 0045 introduit des champs génériques \(U_j\) sur
\([-S,0]\), sans les définir comme les translations d'une unique trajectoire
renormalisée, puis traite la capture comme une information portée seulement
par \(s=0\). L'horloge ci-dessous ferme ce raccord. Une fois (1) écrit, la
forte \(L^3\) espace-temps ferme immédiatement la non-trivialité par (2).

## 1. Cadre et horloge exacts

On conserve exactement le cadre du cycle 0041 : Navier–Stokes
incompressible 3D non forcé sur \(\mathbb R^3\), viscosité un, solution de
Leray–Hopf lisse avant son premier temps singulier fini \(T_*\), point
singulier fixe \((x_*,T_*)\), et

\[
 \sup_{0<t<T_*}\|u(t)\|_{L^{3,\infty}(\mathbb R^3)}\leq M.       \tag{3}
\]

Posons

\[
 A_*=S_w^*(C_MM)>0,\qquad
 R(t)=2\sqrt{\frac{T_*-t}{A_*}},\qquad
 \kappa=\frac2{A_*}.                              \tag{4}
\]

Avec

\[
 \frac{d\sigma}{dt}=R(t)^{-2}
 =\frac{A_*}{4(T_*-t)},                           \tag{5}
\]

on a, à constante additive près,

\[
 \sigma(t)-\sigma(t_0)
 =\frac{A_*}{4}\log\frac{T_*-t_0}{T_*-t}.         \tag{6}
\]

Soient \(\sigma_j\to+\infty\), \(t_j=t(\sigma_j)\) et
\(R_j=R(t_j)\). Pour tout \(s\) borné,

\[
 \begin{aligned}
 T_*-t(\sigma_j+s)
   &=(T_*-t_j)e^{-4s/A_*}
     =(T_*-t_j)e^{-2\kappa s},\\
 R(t(\sigma_j+s))
   &=R_je^{-2s/A_*}=R_je^{-\kappa s}.
 \end{aligned}                                                     \tag{7}
\]

Le signe est ainsi fixé : vers le passé normalisé, \(s<0\), le rayon
physique augmente. Pour chaque intervalle borné \(J\), les temps
\(t(\sigma_j+s)\) appartiennent à \((0,T_*)\) pour tout \(s\in J\) dès que
\(j\) est assez grand. Il n'y a ni extrapolation à \(t=T_*\), ni inversion
du quantificateur « fixer \(J\), puis prendre \(j\) grand ».

La trajectoire renormalisée exacte est

\[
 U(y,\sigma)=R(t)u(x_*+R(t)y,t),\qquad
 P(y,\sigma)=R(t)^2p(x_*+R(t)y,t),                \tag{8}
\]

et elle satisfait

\[
 \partial_\sigma U-\Delta U+(U\cdot\nabla)U+\nabla P
 +\kappa(1+y\cdot\nabla)U=0.                     \tag{9}
\]

Ainsi \(\kappa\) est le même sur toutes les fenêtres translatées. Aucun
\(\kappa_j\), aucun centre mobile et aucun rayon gelé \(R_j\) ne sont
introduits.

## 2. Transport exact de la capture vers \(B_1\)

Pour chaque \(t<T_*\), le changement de variables de (8) donne, sans
constante d'équivalence,

\[
 \begin{aligned}
 K_3(U(\sigma);B_1)
 &=\sup_{\lambda>0}\lambda
   \left|\{y\in B_1:
   |R(t)u(x_*+R(t)y,t)|>\lambda\}\right|^{1/3}\\
 &=K_3(u(t);B(x_*,R(t))).
 \end{aligned}                                                     \tag{10}
\]

Le rayon \(R(t)\) de (4) est exactement le rayon de capture du cycle 0041.
Par conséquent,

\[
 K_3(U(\sigma);B_1)>\gamma_w                     \tag{11}
\]

pour chaque temps sous l'hypothèse pointwise (3), ou presque partout si l'on
ne retient qu'une version essentielle de cette hypothèse. Le centre reste
\(y=0\) à tous les temps; aucun recentrage dépendant de \(j\) ou de \(s\)
n'est caché dans (10).

Pour la troncation externe du cycle 0044,

\[
 Q_LW=W\quad\text{dans }B_L.                     \tag{12}
\]

Donc, si

\[
 Z_j(s)=Q_{L_j}U(\sigma_j+s),\qquad
 L_j\to\infty,\quad L_j\geq1,                    \tag{13}
\]

alors \(Z_j(s)=U(\sigma_j+s)\) dans \(B_1\), pour tout \(s\), et (1)
résulte de (11). Le paramètre \(L_j\) est fixé sur toute la fenêtre : aucune
dérivée \(\partial_sQ_{L_j}\) n'apparaît.

La diagonale physique du cycle 0044 est elle aussi compatible avec une
fenêtre fixe. Si \(J=[-S,0]\) et \(L_jR_j\to0\), alors (7) donne

\[
 \sup_{s\in[-S,0]}L_jR(t(\sigma_j+s))
 \leq e^{\kappa S}L_jR_j\longrightarrow0.        \tag{14}
\]

Pour une extraction ancienne diagonale, il suffit que (14) vaille après
avoir fixé chaque \(S<\infty\); le facteur \(e^{\kappa S}\) est alors une
constante. Affirmer une petitesse uniforme sur une fenêtre croissante
\([-S_j,0]\) demanderait la condition plus forte
\(e^{\kappa S_j}L_jR_j\to0\), mais cette uniformité n'est pas requise pour
la diagonale locale sur tout intervalle fixé.

La translation ne perd pas non plus l'hypothèse de force du cycle 0045. La
borne 0044 est uniforme en \(\sigma\); pour tout \(\rho\) et tout
multi-indice \(\alpha\),

\[
 \sup_{s\in J}
 \|\partial^\alpha F_{L_j}(\sigma_j+s)\|_{L^\infty(B_\rho)}
 \leq C_{\rho,\alpha}M^2L_j^{-3-|\alpha|}
 \longrightarrow0.                              \tag{14a}
\]

Ainsi (13), avec le membre de droite translaté de (14a), instancie
effectivement la suite abstraite du claim 0045 sur chaque fenêtre fixe.

## 3. Mesure temporelle et représentants

La conclusion utile n'exige pas le mot « chaque ». Supposons seulement que
la capture du cycle 0041 soit disponible pour presque tout \(t\). Sur une
fenêtre bornée, \(s\mapsto t(\sigma_j+s)\) est un difféomorphisme \(C^1\)
dont la dérivée est

\[
 \frac{dt}{ds}=R(t)^2>0.                          \tag{15}
\]

Ce changement de variable et son inverse sont localement lipschitziens sur
la fenêtre propre à \(j\); les ensembles temporels nuls restent donc nuls.
La version presque-partout de (1) est suffisante pour intégrer.

Les valeurs exceptionnelles d'un représentant
\(L^\infty_tL^{3,\infty}_x\) ne peuvent pas être utilisées comme traces,
mais elles sont invisibles dans le raisonnement espace-temps. Si l'on veut
conserver « pour tout \(s\) », il faut garder l'hypothèse pointwise inscrite
dans le claim 0041, ou invoquer explicitement le représentant faible continu
et le lemme de semi-continuité décrit dans la revue analytique du cycle 0041.

## 4. Forte \(L^3\) espace-temps et non-trivialité

Avec la convention du laboratoire,

\[
 K_3(f;B_1)\leq\|f\|_{L^3(B_1)}                  \tag{16}
\]

par l'inégalité de Chebyshev. Soit
\(J\Subset(-S,0)\) un intervalle de longueur positive; ce choix intérieur
évite toute question de topologie aux endpoints. De (1) et (16),

\[
 \begin{aligned}
 \|Z_j\|_{L^3(B_1\times J)}^3
 &=\int_J\|Z_j(s)\|_{L^3(B_1)}^3\,ds\\
 &\geq |J|\gamma_w^3.
 \end{aligned}                                                     \tag{17}
\]

Le cycle 0045 donne, après extraction,

\[
 Z_j\longrightarrow Z
 \quad\text{fortement dans }L^3(B_1\times J).    \tag{18}
\]

La convergence des normes dans (18) et (17) donne (2). Une sous-suite
supplémentaire converge même dans \(L^3(B_1)\) pour presque tout \(s\in J\);
pour ces temps,

\[
 \|Z(s)\|_{L^3(B_1)}\geq\gamma_w.                \tag{19}
\]

La non-trivialité ne réside donc pas sur une section de mesure nulle : elle
occupe tout intervalle normalisé de mesure positive au sens presque-partout.
Elle survit à toute extraction diagonale ultérieure.

## 5. Ce que la dérivation ne donne pas

La conclusion (2) est strictement plus faible qu'une trace critique non
nulle et strictement suffisante pour dire que la solution limite n'est pas
identiquement nulle. Il reste possible que

\[
 Z(s)\to0\quad\text{dans }H^{-1}_{\mathrm{loc}}
 \quad\text{lorsque }s\uparrow0,                 \tag{20}
\]

tout en gardant une concentration \(L^3\) à sous-échelle pour presque tout
\(s<0\). Rien dans (17)–(19) ne donne

\[
 Z(0)\neq0,\qquad K_3(Z(0);B_1)\geq c,
 \quad\text{ou}\quad
 |\langle Z_j(0),\psi\rangle|\geq c_*.           \tag{21}
\]

La dérenormalisation et la mildness globale restent également des arêtes
séparées. Avec l'horloge singulière placée à \(\tau=0\), on peut écrire

\[
 \tau=-\frac{e^{-2\kappa s}}{2\kappa},\qquad
 r(s)=e^{-\kappa s}=\sqrt{-2\kappa\tau},\qquad
 v(x,\tau)=r(s)^{-1}Z(x/r(s),s).                 \tag{22}
\]

Cette transformation formelle préserve la non-nullité et convertit (9) en
l'équation standard. Si la limite renormalisée est construite pour tout
\(s\in\mathbb R\), son domaine est exactement \(\tau<0\). Si le ledger 0045
ne construit que \(s\leq0\), l'image est
\(\tau\leq-1/(2\kappa)\); une translation du temps standard place alors son
bord droit en zéro. Dans les deux cas, la justification de la classe de
solution globale et des propriétés de pression/énergie sous (22) n'est pas
incluse ici.

## 6. Passe adverse

1. **Capture seulement terminale.** Si l'on ne connaissait la minoration
   qu'à \(s=0\), (17) serait illégitime et les contre-profils du cycle 0045
   survivraient. Le gain vient exactement du quantificateur « tout temps »
   de Barker–Prange, pas d'une propriété abstraite de trace.
2. **Rayon gelé.** Remplacer (8) par une remise à l'échelle au rayon fixe
   \(R_j\) déplace la boule capturée. Son rayon normalisé devient
   \(R(t(\sigma_j+s))/R_j=e^{-\kappa s}\), et \(B_1\) n'est plus l'identité
   correcte sans nouveau ledger. La normalisation mobile des cycles 0042–0044
   évite cette erreur.
3. **Mauvais signe d'horloge.** Le facteur correct est
   \(R(t(\sigma_j+s))/R_j=e^{-\kappa s}\). Écrire \(e^{+\kappa s}\)
   inverse passé et futur et fausse (14).
4. **Endpoint.** La forte \(L^3_{\mathrm{loc}}\) n'a pas besoin de contenir
   la tranche \(s=0\). Tout \(J\Subset(-S,0)\) non dégénéré suffit à (2).
5. **Représentant.** Une borne essentielle ne justifie pas « chaque temps »;
   elle justifie au minimum « presque tout temps », ce qui suffit à (17).
6. **Centre mobile.** (10) utilise le même point singulier \(x_*\) à tous les
   temps. Une concentration en centres \(x_j(s)\) non contrôlés ne donnerait
   pas une capture dans le même \(B_1\).
7. **Cutoff.** La conclusion utilise l'identité exacte \(Q_{L_j}=I\) dans
   \(B_{L_j}\), pas seulement une convergence de \(Q_{L_j}\) vers l'identité.
8. **Concentration à sous-échelle.** Un profil
   \(C_n(x)=nV(nx)\) conserve sa norme critique, mais il ne peut converger
   fortement vers zéro dans \(L^3(B_1\times J)\) tout en satisfaisant (1) sur
   un ensemble temporel de mesure \(|J|\). Il reste un contre-profil valide
   contre la trace forte, non contre (2).
9. **Fenêtre croissante.** \(L_jR_j\to0\) suffit sur chaque fenêtre fixe;
   il ne suffit pas uniformément jusqu'à un bord gauche
   \(-S_j\to-\infty\). Confondre ces deux quantificateurs crée une fausse
   uniformité, mais ne bloque pas l'extraction diagonale locale.
10. **Rigidité.** Une limite ancienne non triviale ne contredit aucun
    théorème général de Liouville faible-\(L^3\) actuellement enregistré. Le
    résultat ferme la non-trivialité, pas la rigidité et encore moins le
    problème Clay.

## Conclusion logique

L'arête correcte est

\[
 \begin{aligned}
 &\text{capture Type I pour tout }t<T_*
 +\text{ horloge mobile exacte}
 +Q_{L_j}=I\text{ sur }B_1\\
 &\qquad\Longrightarrow
 K_3(Z_j(s);B_1)>\gamma_w
 \text{ pour tout/a.e. }s\in J\\
 &\qquad\overset{Z_j\to Z\ \mathrm{fort}\ L^3(B_1\times J)}
 {\Longrightarrow}
 Z\not\equiv0.
 \end{aligned}                                                     \tag{23}
\]

**Verdict de revue : RÉVISER.** La porte « trace critique non triviale » du
cycle 0045 ne doit pas être utilisée comme porte vers la non-trivialité de la
limite ancienne. Elle reste une question distincte si un futur théorème de
rigidité requiert une trace terminale. Le premier raccord à ajouter au graphe
et aux claims est (23), avec le quantificateur temporel et l'horloge (7)
explicitement inscrits.
