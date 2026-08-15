# Cycle 0062 — veille primaire sur les numérateurs azimutaux

Date de gel : 2026-08-15.

Statut : **audit bibliographique indépendant**. Ce document ne revendique
ni preuve nouvelle de régularité, ni construction de blow-up, ni identité
publiée nouvelle. Les déductions qui comparent les observables publiées au
numérateur du cycle sont signalées comme telles.

## Question auditée et cadre figé

Le cycle 0062 considère, sur \(\mathbb R^3\), un champ de Schwartz réel,
divergence-free, et l'action covariante des rotations autour de l'axe
\(e_3\) :

\[
 (Q_\theta U)(y)=R_\theta U(R_{-\theta}y),\qquad
 \mathcal RU=JU-(Jy\!\cdot\!\nabla)U .                       \tag{L62.1}
\]

Pour les projecteurs isotypiques réels \(P_m\), \(m\geq1\), et

\[
 d(Z)=\Delta Z-\mathbb P\operatorname{div}(Z\otimes Z)
       -\kappa(1+y\!\cdot\!\nabla)Z ,                       \tag{L62.2}
\]

le numérateur à auditer est

\[
 C_m(Z)=\langle P_m d(Z),\mathcal RP_mZ\rangle_{L^2(\mathbb R^3)} .
                                                                    \tag{L62.3}
\]

La question bibliographique précise est la suivante : une identité publiée
pour Navier--Stokes force-t-elle

\[
 C_m=0\quad\hbox{pour tout }m,\qquad
 \sum_{m\geq1}C_m=0,                                      \tag{L62.4}
\]

ou seulement une annulation d'une autre observable après sommation ?

Ce cadre est celui du calcul instantané renormalisé du cycle, pas encore
celui d'une solution ancienne faible adaptée. La viscosité de l'équation
physique est positive; la normalisation de `(L62.2)` la fixe à un. Il n'y a
ni frontière ni force extérieure dans `(L62.2)`. Sur le tore cubique du
problème Clay, une rotation axiale continue ne préserve pas le réseau
\(\mathbb Z^3\) en général : les isotypes continus de `(L62.1)` sont donc
un outil propre à \(\mathbb R^3\), et non une décomposition globale
automatique sur \(\mathbb T^3\).

## Verdict

**Aucune source primaire localisée ne force \(C_m=0\), ni
\(\sum_m C_m=0\).** Les identités publiées se répartissent en trois familles
qui ne doivent pas être confondues.

1. **Énergie cinétique.** Pour un champ divergence-free et des flux de bord
   nuls,

   \[
   \langle \mathbb P\operatorname{div}(u\otimes u),u\rangle=0.
                                                                    \tag{L62.5}
   \]

   Après décomposition modale, ceci annule la somme des productions
   **radiales** \(\operatorname{Re}\langle N_m,u_m\rangle\). Waleffe
   annule la somme des trois transferts d'énergie d'une triade hélicoïdale;
   Yeung--Chu--Schmidt annulent des paires, des sextuplets et enfin la somme
   globale des transferts spectraux, sous hypothèse de flux de bord nul.
   Les transferts individuels sont signés et généralement non nuls.

2. **Moment angulaire spatial.** La loi publiée teste l'équation contre le
   champ de Killing rigide

   \[
   \phi_i(x)=x\times e_i,\qquad
   L_i=(u,\phi_i)=\int_{\Omega}(u\times x)_i\,dx.            \tag{L62.6}
   \]

   Elle donne \((NL(u),\phi_i)=0\) lorsque les termes de bord sont
   compatibles. Le champ test \(\phi_i\) est fixé et linéaire en \(x\).
   Il n'est pas la tangente d'orbite **dans l'espace des états**
   \(\mathcal Ru=Ju-(Jx\cdot\nabla)u\), qui dépend de \(u\). Cette loi ne
   contraint donc pas `(L62.3)`.

3. **Covariance rotationnelle et triades.** Elle impose seulement la règle
   de sélection

   \[
   k+\ell=m                                                    \tag{L62.7}
   \]

   dans la complexification, ou les variantes somme/différence dans les
   blocs réels. Elle ne fixe ni la phase ni le signe de la partie en
   quadrature qui apparaît quand le mode destinataire est testé contre
   \(\mathcal Rz_m=imz_m\).

La source récente la plus proche, Pineau--Vicol v2, va dans le même sens.
Dans le produit gaussien \(L^2_\mu\), son équation RSS donne exactement

\[
 |\alpha|\|\mathcal RU\|_{L^2_\mu}^2
 =\operatorname{sgn}(\alpha)
   \langle \mathcal RU,N\rangle_{L^2_\mu},                  \tag{L62.8}
\]

où \(N=-(U\cdot\nabla)U-\nabla P\). C'est un **couplage tangent**, pas une
annulation. Il est pondéré, global et non décomposé mode par mode; il ne
démontre donc pas directement qu'un \(C_m\) de `(L62.3)` est non nul, mais
il exclut toute lecture naïve « covariance rotationnelle \(\Rightarrow\)
orthogonalité à l'orbite ».

Enfin, même une hypothétique annulation de la partie convective ne suffirait
pas à annuler le \(C_m\) total de `(L62.3)`: le drift renormalisé
\(-\kappa(1+y\cdot\nabla)Z\) n'appartient pas aux lois de conservation de
l'équation physique. La partie unité est orthogonale à la tangente, mais le
couplage non pondéré de \(y\cdot\nabla\) et \(\mathcal R\) n'est couvert par
aucune des cancellations d'énergie inventoriées ci-dessous.

## Matrice des implications exactes

| identité publiée | équation et cadre | ce qui est nul | implication pour \(C_m\) |
|---|---|---|---|
| Waleffe 1992, transferts d'une triade hélicoïdale | Euler/NS incompressible, boîte périodique, modes de Fourier lisses | somme des trois transferts d'énergie; somme pondérée d'hélicité | aucune annulation individuelle; aucune projection contre \(im u_m\) |
| Charnyi et al. 2017, §3.1 | NS incompressible, \(d=2,3\), domaine borné, no-slip; support intérieur pour isoler la non-linéarité | \((NL(u),u)=0\) pour l'énergie; \((NL(u),x\times e_i)=0\) pour le moment angulaire, selon la formulation/divergence | le second test n'est pas \(\mathcal Ru\); aucune somme en \(m\) |
| Willis--Cvitanović--Avila 2013 | NS de pipe forcé, paroi no-slip, direction axiale périodique, DNS finie | covariance de l'évolution sous rotations/translations; action diagonale \(-im\) sur Fourier | règle de représentation seulement; pas de loi de signe |
| Nekkanti et al. 2025 | jet subsonique turbulent \(M=0.4\), \(Re=450000\), budget spectral issu de données | bilan global d'énergie; transferts azimutaux individuels signés | confirme \(m_1+m_2=m_3\), mais teste par \(u_m^*\), non par \(im u_m\) |
| Yeung--Chu--Schmidt 2026 | bilans spectraux de quantité de mouvement/énergie; DNS et données expérimentales | annulations par paires, sextuplets et somme globale si le flux de bord s'annule | cancellation d'énergie radiale; transferts individuels explicitement positifs ou négatifs |
| Pineau--Vicol 2026 v2 | NS 3D incompressible non forcé sur \(\mathbb R^3\), profil RSS lisse, borne Type I | orthogonalité des termes linéaires à \(\mathcal RU\) dans \(L^2_\mu\), **pas** celle de \(N\) | `(L62.8)` donne une projection tangentielle non nulle sauf \(\mathcal RU=0\) ou \(\alpha=0\) |
| Bertram 2026 | NS 3D incompressible forcé sur \(\mathbb T^3\), solution suffisamment lisse | somme globale du transfert d'énergie \(\sum T=0\) | objet radial \(\operatorname{Re}(v_k^*\cdot N_k)\); pas d'isotype azimutal |
| Biferale--Titi 2013 | modèle NS décimé à une hélicité sur \(\mathbb T^3\) | énergie et hélicité triade par triade; hélicité coercive après projection | modèle modifié; la coercivité disparaît avec les trois classes mixtes supprimées |
| Kankaria et al. 2026 v1 | NS Fourier-décimé forcé sur boîte triplement périodique; DNS \(512^3/1024^3\) | invariants quadratiques du modèle projeté | aucune identité de phase; calcul flottant et système modifié |

Conclusion logique de la matrice : les sources imposent seulement une
**cancellation globale d'énergie dans la direction radiale**, plus une loi
linéaire de moment angulaire distincte. Elles ne donnent aucune cancellation
tangentielle générale.

## 1. Waleffe 1992 : cancellation triadique, pas annulation de chaque transfert

### Source, version et statut

- Fabian Waleffe, *The nature of triad interactions in homogeneous
  turbulence*, *Physics of Fluids A* **4**(2), 350--363 (1992), DOI
  [10.1063/1.858309](https://doi.org/10.1063/1.858309), article publié.
- La notice primaire NASA NTRS, document `19920038608`, qualifie le fichier
  de « reprint (version printed in journal) » et rattache le même DOI :
  [notice NTRS](https://ntrs.nasa.gov/citations/19920038608).
- Le PDF éditeur AIP était protégé par un défi JavaScript lors de l'audit.
  Les équations ont été contrôlées visuellement dans le rapport primaire
  d'auteur qui précède l'article : F. Waleffe, *Triad interactions in
  homogeneous turbulence*, Center for Turbulence Research, Annual Research
  Briefs 1991, pp. 31--43,
  [PDF Stanford](https://web.stanford.edu/group/ctr/ResBriefs/1991/05_WALEFFE.pdf).

### Équation, domaine et notion

Le champ de vitesse incompressible est développé en série de Fourier dans
une boîte périodique de côté \(L\). Chaque coefficient est décomposé sur les
deux vecteurs hélicoïdaux, propres du rotationnel :

\[
 u(k)=a_+(k)h_+(k)+a_-(k)h_-(k),\qquad
 ik\times h_s=skh_s .                                      \tag{W1}
\]

Il s'agit d'une analyse spectrale de solutions suffisamment régulières et de
triades du système incompressible. La viscosité \(\nu\) figure dans les
équations modales; les identités de conservation sont celles de la partie
inviscide non forcée.

### Identité exacte

La non-linéarité quadratique ne couple que

\[
 k+p+q=0 .                                                   \tag{W2}
\]

Pour chacune des huit combinaisons de signes hélicoïdaux, les transferts
\(t^{(i)}\) satisfont

\[
 \begin{aligned}
 t^{(i)}(k,p,q)+t^{(i)}(p,q,k)+t^{(i)}(q,k,p)&=0,\\
 s_k k\,t^{(i)}(k,p,q)+s_p p\,t^{(i)}(p,q,k)
 +s_q q\,t^{(i)}(q,k,p)&=0 .
 \end{aligned}                                               \tag{W3}
\]

La première ligne est la conservation détaillée d'énergie, la seconde celle
d'hélicité. L'équation (8) du rapport donne un facteur d'amplitude complexe
plus son conjugué. Ainsi \(t^{(i)}\) est réel et dépend des phases. Rien dans
`(W3)` n'impose qu'un des trois termes soit nul; l'article classe précisément
les configurations selon le mode qui perd de l'énergie.

### Implication explicite pour le cycle

Une production d'énergie modale contient le coefficient destinataire dans
la direction **radiale** : schématiquement

\[
 T_m=\operatorname{Re}\langle N_m,u_m\rangle .              \tag{W4}
\]

Le numérateur tangent utilise au contraire

\[
 C_m=\operatorname{Re}\langle N_m,im u_m\rangle
    =-m\operatorname{Im}\langle N_m,u_m\rangle              \tag{W5}
\]

à convention hermitienne près. `(W3)` contraint `(W4)`, pas `(W5)`.
L'information « transferts signés dont la somme vaut zéro » ne peut donc ni
forcer \(C_m=0\), ni être multipliée aveuglément par des indices \(m\) pour
obtenir \(\sum_mC_m=0\).

### Non-transfert Clay

Le papier décrit exactement l'algèbre triadique du système périodique, mais
ne fournit pas de borne uniforme critique, de compacité, de solution
ancienne ou de rigidité. Il n'analyse pas le générateur de rotations
spatiales de `(L62.1)` et n'établit aucune régularité globale.

## 2. Charnyi--Heister--Olshanskii--Rebholz 2017 : le champ test du moment angulaire

### Source, version et statut

- Sergey Charnyi, Timo Heister, Maxim A. Olshanskii et Leo G. Rebholz,
  *On conservation laws of Navier--Stokes Galerkin discretizations*,
  *Journal of Computational Physics* **337**, 289--308 (2017), DOI
  [10.1016/j.jcp.2017.02.039](https://doi.org/10.1016/j.jcp.2017.02.039),
  [arXiv:1605.09763v2](https://arxiv.org/abs/1605.09763), article publié.
- v1 : 2016-05-31; v2 : 2017-01-20. Le PDF publié fourni par l'auteur a été
  contrôlé, notamment pp. 292--294 :
  [PDF auteur](https://www.math.uh.edu/~molshan/ftp/pub/CHOR2017.pdf).

### Équation, domaine, frontière et notion

Les auteurs partent de

\[
 u_t+(u\cdot\nabla)u+\nabla p-\nu\Delta u=f,
 \qquad\operatorname{div}u=0                               \tag{C1}
\]

sur \(\Omega\subset\mathbb R^d\), \(d=2,3\), avec condition no-slip.
L'objet principal est une approximation de Galerkin dont la divergence peut
n'être imposée que faiblement. Pour isoler la contribution non linéaire des
effets de paroi, §3 suppose que la solution discrète, la pression et la force
sont supportées dans un sous-domaine strictement intérieur.

Le papier compare les formes convective, skew, rotationnelle, conservative
et EMAC. Si la divergence est nulle point par point, ces formes coïncident au
niveau continu, à modification de pression près.

### Les deux tests exacts

Pour l'énergie, le test est \(v=u\), d'où

\[
 \frac12\frac d{dt}\|u\|_2^2+(NL(u),u)+\nu\|\nabla u\|_2^2=(f,u).
                                                                    \tag{C2}
\]

Pour le moment angulaire, §3.1.3 définit

\[
 (M_x)_i=(u,\phi_i),\qquad \phi_i=x\times e_i,
 \quad\operatorname{div}\phi_i=0,\quad\Delta\phi_i=0,       \tag{C3}
\]

et teste avec une restriction compatible de \(\phi_i\). Pour la forme
conservative et la forme EMAC, les auteurs obtiennent

\[
 (NL(u),\phi_i)=-b(u,\phi_i,u)=0,                           \tag{C4}
\]

car \(\nabla\phi_i\) est antisymétrique. Pour une solution exactement
divergence-free, la forme convective donne la même annulation. Les écarts
entre formulations du papier concernent la divergence discrète non nulle.

### Pourquoi `(C4)` n'est pas une identité sur \(C_m\)

Le champ \(\phi_i\) génère une rotation rigide **des points physiques** et ne
dépend pas de la solution. La tangente à l'orbite d'un champ vectoriel est

\[
 \mathcal Ru=Ju-(Jx\cdot\nabla)u,                           \tag{C5}
\]

qui dépend de \(u\), contient une dérivée, et est quadratique dans le produit
\(\langle NL(u),\mathcal Ru\rangle\). Il n'existe aucune substitution de
\(\phi_i\) par \(\mathcal Ru\) dans la preuve de `(C4)` : la propriété
antisymétrique de \(\nabla\phi_i\), centrale dans le calcul, disparaît.

En outre, sur \(\mathbb T^3\), \(x\times e_i\) n'est pas périodique. Sur un
domaine à paroi, le bilan complet comporte le couple exercé au bord. La loi
ne peut donc être importée dans `(L62.3)` sans changer de domaine et de champ
test.

## 3. Décomposition azimutale et sélection isotypique

### Willis--Cvitanović--Avila 2013

- Ashley P. Willis, Predrag Cvitanović et Marc Avila, *Revealing the state
  space of turbulent pipe flow by symmetry reduction*, *Journal of Fluid
  Mechanics* **721**, 514--540 (2013), DOI
  [10.1017/jfm.2013.75](https://doi.org/10.1017/jfm.2013.75),
  [arXiv:1203.3701v1](https://arxiv.org/abs/1203.3701), article publié.

Le modèle est Navier--Stokes incompressible pour la déviation au profil de
Hagen--Poiseuille dans un tuyau, à débit constant, paroi radiale no-slip et
direction axiale périodique. Les calculs sont à \(Re=2400\), avec série de
Fourier axiale et azimutale tronquée et différences finies radiales. Les
états génériques sont des trajectoires DNS, non des solutions faibles
certifiées.

L'équation (2.2) développe le champ selon

\[
 u(r,\theta,z)=\sum_{k,m'}u_{nkm'}
 e^{i(2\alpha kz+mm'\theta)} .                              \tag{WCA1}
\]

Les équations (2.9)--(2.10) donnent l'équivariance sous rotations
azimutales et translations axiales. Pour une fonction périodique abstraite,
les équations (2.13)--(2.14) donnent

\[
 g(\phi)a=\operatorname{diag}(e^{-im\phi})a,qquad
 T a=\operatorname{diag}(-im)a .                            \tag{WCA2}
\]

Cette source justifie l'action diagonale du générateur sur les caractères.
Elle ne projette pas la non-linéarité contre \(Ta\), ne dérive aucun
\(C_m\), et ne donne aucune somme nulle tangentielle. Le pipe forcé, la
paroi, les symétries discrètes imposées et la troncature numérique excluent
un transfert direct au problème Clay.

### Déduction de sélection, non attribuée comme théorème aux auteurs

De la covariance bilinéaire

\[
 B(Q_\theta z_k,Q_\theta z_\ell)
 =Q_\theta B(z_k,z_\ell)                                   \tag{SEL1}
\]

et de \(Q_\theta z_k=e^{ik\theta}z_k\), on déduit

\[
 P_m B(z_k,z_\ell)=0\quad\text{si }k+\ell\ne m .            \tag{SEL2}
\]

`(SEL2)` est une conséquence élémentaire de l'équivariance et des
caractères; elle ne fixe pas la partie réelle ou imaginaire du coefficient
triadique restant. L'audit n'a trouvé aucune source qui ajoute à `(SEL2)`
une positivité ou une annulation de \(\langle P_mB(z,z),imz_m\rangle\).

## 4. Les transferts signés récents ne sont pas des numérateurs tangentiels

### Nekkanti--Pickering--Schmidt--Colonius 2025

- Akhil Nekkanti, Ethan Pickering, Oliver T. Schmidt et Tim Colonius,
  *Bispectral decomposition and energy transfer in a turbulent jet*,
  *Journal of Fluid Mechanics* **1025**, A35 (2025), publié en ligne le
  2025-12-18, DOI
  [10.1017/jfm.2025.10922](https://doi.org/10.1017/jfm.2025.10922),
  [arXiv:2502.15091v1](https://arxiv.org/abs/2502.15091).

Le cas étudié est un jet turbulent subsonique à Mach \(0.4\) et
\(Re=450000\), ouvert et statistique. La décomposition bispectrale est un
post-traitement de données; ce n'est ni l'équation Clay non forcée sur
\(\mathbb R^3\), ni un calcul validé par intervalles.

La source impose explicitement les résonances

\[
 m_1+m_2=m_3,qquad f_1+f_2=f_3,                             \tag{N1}
\]

et définit le transfert d'énergie d'une triade par

\[
 T_{nl}=-\operatorname{Re}
 \left[\widehat u_j^*(m_3,f_3)\,
 \widehat u_i(m_1,f_1)\,
 \partial_i\widehat u_j(m_2,f_2)\right].                   \tag{N2}
\]

Les résultats montrent des transferts positifs et négatifs, y compris un
changement de sens avec la position axiale, et un transfert net différent
selon \(m\). Cela confirme expérimentalement que la sélection azimutale ne
produit pas une annulation mode par mode. Mais `(N2)` teste la convection
contre \(u_{m_3}\), donc mesure une énergie radiale. Remplacer ce test par
\(im_3u_{m_3}\) change la quadrature complexe; les données publiées ne
calculent pas `(L62.3)`.

### Yeung--Chu--Schmidt 2026

- Brandon Yeung, Tianyi Chu et Oliver T. Schmidt, *Triadic orthogonal
  decomposition reveals nonlinearity in fluid flows*, *Journal of Fluid
  Mechanics* **1031**, A34 (2026), publié en ligne le 2026-03-19, DOI
  [10.1017/jfm.2026.11183](https://doi.org/10.1017/jfm.2026.11183), article
  publié en libre accès.

Le papier part des équations spectrales de quantité de mouvement et
d'énergie et analyse trois jeux de données : DNS de sillage de cylindre à
\(Re=100\), PIV de sillage d'éolienne, et DNS de turbulence isotrope forcée
dans une boîte 3D périodique. La méthode est une décomposition statistique
optimale, pas une théorie de solutions faibles.

En présence de flux de bord nul, l'équation (2.48) donne la conservation par
paires

\[
 \widehat{\mathcal T}^{\mathcal R}_{l\to n}
 +\widehat{\mathcal T}^{\mathcal R}_{n\to l}=0,              \tag{Y1}
\]

l'équation (2.49) assemble trois paires en un ensemble de six transferts de
somme nulle, et l'équation (2.50) donne

\[
 \sum_n\sum_{l\ne0,n}
 \widehat{\mathcal T}^{\mathcal R}_{l\to n}=0 .             \tag{Y2}
\]

Les auteurs insistent simultanément sur le signe de chaque transfert : un
terme positif ou négatif indique le sens donneur--receveur. `(Y1)--(Y2)`
constituent donc l'exemple publié le plus explicite du verdict « cancellation
collective, non annulation individuelle ». Les indices sont des fréquences
temporelles et l'observable est l'énergie; aucune conclusion sur les
isotypes spatiaux ou \(C_m\) ne suit.

### Bertram 2026

- Erik Bertram, *From Triadic Interactions to Kolmogorov Scaling: A
  Deterministic, Scale-Resolved Formulation of Energy Flux*, *Physica D:
  Nonlinear Phenomena* (2026), article 135338, DOI
  [10.1016/j.physd.2026.135338](https://doi.org/10.1016/j.physd.2026.135338),
  [arXiv:2607.16381v1](https://arxiv.org/abs/2607.16381), publié.

L'équation est Navier--Stokes 3D incompressible forcé sur
\(\mathbb T^3=[0,2\pi]^3\), viscosité \(\nu>0\), pour des solutions
suffisamment lisses. L'équation (24) définit

\[
 T(k,p,q)=\operatorname{Re}
 \{v_k^*\cdot P(k)[(v_p\cdot iq)v_q]\},                     \tag{B1}
\]

et l'équation (26) donne \(\sum_k\sum_{p+q=k}T(k,p,q)=0\).
L'article précise que ses résultats de scaling sont structurels et
conditionnels. `(B1)` est encore le test radial par \(v_k^*\), non le test
tangent par \(imv_m\); aucune annulation de \(C_m\) n'est énoncée.

## 5. Pineau--Vicol 2026 : projection publiée contre le générateur de rotation

### Source, version et statut

- Ben Pineau et Vlad Vicol, *On rotated backwards self-similar solutions of
  the incompressible 3D Navier--Stokes equations*,
  [arXiv:2607.09619v2](https://arxiv.org/abs/2607.09619), prépublication
  primaire, v1 du 2026-07-10, v2 du 2026-08-06, 37 pages. Aucun DOI de revue
  ou statut publié n'était indiqué à la date de gel.

### Équation, domaine et notion

Les auteurs étudient Navier--Stokes 3D incompressible, non forcé,
viscosité un, sur \(\mathbb R^3\times[-1,0)\). L'ansatz backward RSS exact
fait tourner un profil lisse stationnaire \(U\) à vitesse constante
\(\alpha\) en temps similaire. Le profil résout

\[
 \alpha\mathcal RU+\frac12U+\frac12(y\cdot\nabla)U
 -\Delta U+(U\cdot\nabla)U+\nabla P=0,
 \qquad\operatorname{div}U=0,                               \tag{PV1}
\]

avec

\[
 \mathcal RU=JU-(Jy\cdot\nabla)U .                          \tag{PV2}
\]

Sous la borne Type I \(|U(y)|\le C/(1+|y|)\), le résultat de rigidité
exclut les profils non triviaux lorsque \(|\alpha|\) est suffisamment petit
ou suffisamment grand. Il ne couvre pas encore les vitesses intermédiaires
et ne traite pas un blow-up Type II général.

### Identité tangentielle exacte

En coordonnées cylindriques, §6.1 montre que \(\mathcal R\) agit comme
\(-\partial_\theta\) sur chaque composante cylindrique. Dans
\(L^2_\mu\), \(\mu=e^{-|y|^2/4}\), le lemme 6.2 établit que
\(\mathcal R\) est antisymétrique, tandis que
\(-\Delta+\tfrac12y\cdot\nabla\) est auto-adjoint. Avec

\[
 N=-(U\cdot\nabla)U-\nabla P,                               \tag{PV3}
\]

l'équation (6.16) devient

\[
 \alpha\mathcal RU+\frac12U+
 \left(-\Delta+\frac12y\cdot\nabla\right)U=N.              \tag{PV4}
\]

Le produit avec \(\operatorname{sgn}(\alpha)\mathcal RU\) donne l'équation
(6.18), reproduite en `(L62.8)`. Les auteurs ne posent donc jamais
\(\langle N,\mathcal RU\rangle=0\); ils l'utilisent pour contrôler
\(\|\mathcal RU\|\).

### Limites du raccord

- Le produit est gaussien. Dans ce produit, le gradient de pression ne
  disparaît pas par la seule condition \(\operatorname{div}\mathcal RU=0\),
  car la dérivée du poids crée un terme supplémentaire. Le \(N\) de
  `(PV3)` inclut donc explicitement la pression.
- La décomposition publiée sépare moyenne angulaire et partie
  non-axisymétrique; elle ne donne pas les \(C_m\) individuels.
- L'identité suppose un profil RSS lisse exact et une vitesse \(\alpha\)
  constante. Elle ne s'applique pas à une phase adaptative d'une suite de
  blow-up faible.
- Le théorème est une exclusion substantielle de profils sous Type I, mais
  exclure cette classe ne résout pas tous les scénarios Clay.

Malgré ces limites, `(L62.8)` est la vérification primaire la plus directe
que l'équivariance ne produit pas une orthogonalité tangentielle : la
projection de la non-linéarité-plus-pression équilibre le terme de rotation.

## 6. Modèles décimés et limites des conclusions triadiques

### Biferale--Titi 2013

- Luca Biferale et Edriss S. Titi, *On the Global Regularity of a
  Helical-decimated Version of the 3D Navier--Stokes Equations*, *Journal of
  Statistical Physics* **151**, 1089--1098 (2013), DOI
  [10.1007/s10955-013-0746-4](https://doi.org/10.1007/s10955-013-0746-4),
  [arXiv:1303.1215v1](https://arxiv.org/abs/1303.1215), article publié.

Sur le tore 3D périodique, le système projette exactement l'évolution sur
un seul signe d'hélicité :

\[
 \partial_t v^+=P^+[-v^+\cdot\nabla v^+-\nabla p^+]
 +\nu\Delta v^++f^+ .                                      \tag{BT1}
\]

Le papier rappelle que l'énergie et l'hélicité sont conservées triade par
triade par la partie inviscide. Après décimation, l'hélicité devient
positive et équivalente à \(\|v^+\|_{\dot H^{1/2}}^2\), ce qui donne des
bounds globaux et l'unicité pour les données de \(\dot H^{1/2}\).

Le transfert au système Clay échoue précisément parce que trois classes de
triades mixtes sont supprimées. Les auteurs concluent que les difficultés du
système complet doivent être cherchées dans ces classes éliminées. Le
résultat ne produit ni positivité des triades complètes, ni contrôle d'un
numérateur tangent.

### Kankaria--Mukherjee--Murugan--Rosti--Ray 2026

- Anikat Kankaria, Ritwik Mukherjee, Sugan Durai Murugan, Marco Edoardo
  Rosti et Samriddhi Sankar Ray, *Reduction of Triadic Interactions
  Suppresses Intermittency and Anomalous Dissipation in Turbulence*,
  [arXiv:2603.19180v1](https://arxiv.org/abs/2603.19180), prépublication
  primaire soumise le 2026-03-19.

Le champ est projeté par des variables de Bernoulli gelées \(\gamma_k\) :

\[
 v=Pu,\qquad
 \partial_t v=P[-\nabla p-(v\cdot\nabla)v]
 +\nu\Delta v+F.                                            \tag{K1}
\]

Les DNS portent sur une boîte cubique \(2\pi\)-périodique, \(512^3\) et
\(1024^3\) points de collocation, deux solveurs et deux forçages à grande
échelle, pour \(50\le Re_\lambda\le550\). Il s'agit d'un modèle modifié,
forcé, statistiquement stationnaire, et d'extrapolations numériques vers
grand Reynolds. Aucun calcul d'intervalles ou passage certifié au continuum
n'est fourni. La préservation des invariants quadratiques par la partie
inviscide non forcée du système décimé ne donne aucune loi de phase pour le
système complet.

## 7. Veille différentielle 2025--2026

La recherche a porté sur les combinaisons `Navier-Stokes`, `azimuthal
mode`, `isotypic`, `triadic transfer`, `angular momentum`, `rotation
generator` et `nonlinear projection`, dans les index arXiv, éditeurs et
pages primaires accessibles. Les résultats pertinents ont été vérifiés à la
date de gel; une page secondaire n'a servi qu'à retrouver un DOI ou un PDF
primaire.

| source récente | statut au 2026-08-15 | apport falsifiable | résultat négatif pour le cycle |
|---|---|---|---|
| Nekkanti et al., JFM 2025 | publié, DOI contrôlé | formule azimutale `(N2)` et transferts signés localement | aucun test par \(\mathcal Ru_m\), données de jet ouvert |
| Yeung et al., JFM 2026 | publié, DOI contrôlé | hiérarchie exacte d'annulations d'énergie sous flux de bord nul | démontre une somme radiale, pas \(\sum C_m\) |
| Kankaria et al., arXiv 2603.19180v1 | prépublication, DNS | sensibilité de l'intermittence à la suppression de triades | équation décimée, aucune preuve continuum |
| Pineau--Vicol, arXiv 2607.09619v2 | prépublication mathématique | rigidité RSS Type I pour rotation petite/grande; identité `(L62.8)` | ansatz exact, produit gaussien, aucune annulation modale |
| Bertram, Physica D 2026 | publié, DOI contrôlé | représentation triadique et somme d'énergie globale | résultats de scaling conditionnels, pas de rotation axiale |
| S.-i. Inage, *Mathematics* 14 (2026), 1410, DOI [10.3390/math14091410](https://doi.org/10.3390/math14091410) | publié le 2026-04-23 | cadre de triades dyadiques et « residence-time compression » | l'article dit explicitement ne pas établir la régularité globale complète; aucune identité de générateur de rotation ou de \(C_m\) localisée |

La veille ne révèle donc aucun nouveau théorème 2025--2026 qui fermerait la
loi de signe recherchée. Le résultat récent le plus transférable est
**négatif pour cette stratégie** : Pineau--Vicol doit estimer la projection
tangentielle de la non-linéarité; ils ne l'annulent pas.

## 8. Passe contradictoire des implications

### 8.1 Énergie \(\not\Rightarrow\sum_m C_m=0\)

L'antisymétrie de la forme trilineaire

\[
 b(u,v,w)=\int (u\cdot\nabla)v\cdot w,qquad
 b(u,v,w)=-b(u,w,v)                                        \tag{A1}
\]

pour \(\operatorname{div}u=0\) donne \(b(u,u,u)=0\). Elle ne donne pas
\(b(u,u,\mathcal Ru)=0\). La covariance de \(b\), différentiée le long du
groupe, donne

\[
 b(\mathcal Ru,u,u)+b(u,\mathcal Ru,u)+b(u,u,\mathcal Ru)=0. \tag{A2}
\]

Le premier terme est nul et les deux derniers sont opposés par `(A1)` :
`(A2)` est une tautologie, non une nouvelle annulation. Cette déduction est
interne, mais elle explicite exactement pourquoi les identités de Waleffe,
Bertram et Yeung ne se transfèrent pas.

### 8.2 Moment angulaire \(\not\Rightarrow\sum_m C_m=0\)

La preuve de Charnyi et al. utilise
\(u\cdot(\nabla\phi_i)u=0\) point par point parce que
\(\nabla\phi_i\) est antisymétrique. Pour \(\phi=\mathcal Ru\),
\(\nabla\phi\) contient \(\nabla u\) et \(x\nabla^2u\); elle n'est pas une
matrice antisymétrique fixée. Le changement de champ test invalide donc le
premier maillon de la preuve, avant toute question de sommation modale.

### 8.3 Équivariance \(\not\Rightarrow\) orthogonalité

Une application vectorielle équivariante peut avoir simultanément une
composante radiale et une composante tangentielle. Différencier
\(d(Q_\theta Z)=Q_\theta d(Z)\) donne une relation pour la dérivée de
Fréchet \(Dd(Z)[\mathcal RZ]\), non la relation scalaire
\(\langle d(Z),\mathcal RZ\rangle=0\). `(L62.8)` fournit un témoin publié
de cette distinction dans l'équation RSS.

### 8.4 Pression et localisation

Dans \(L^2(\mathbb R^3)\), si \(\mathcal RZ_m\) est divergence-free et les
champs décroissent, la partie gradient disparaît du produit global. Une
coupure spatiale crée des termes de bord et une pression harmonique. Dans
le produit gaussien de Pineau--Vicol, la pression reste dans \(N\). On ne
peut donc pas combiner leur `(L62.8)` avec l'annulation Leray non pondérée
sans recalculer le produit et la pression.

### 8.5 Quatre affirmations falsifiables

| affirmation testable | statut après audit | falsificateur primaire |
|---|---|---|
| « la conservation d'énergie force chaque transfert modal à zéro » | **RÉFUTÉ** | Waleffe `(W3)`; Nekkanti transferts signés |
| « le moment angulaire teste l'équation contre \(\mathcal Ru\) » | **RÉFUTÉ** | Charnyi `(C3)--(C4)` : test \(x\times e_i\) |
| « l'équivariance force la projection tangentielle globale à zéro » | **RÉFUTÉ comme implication** | Pineau--Vicol `(L62.8)` et calcul `(A2)` |
| « une source publiée force \(C_m=0\) ou \(\sum_mC_m=0\) dans le cadre `(L62.1)--(L62.3)` » | **NON TROUVÉ; aucun soutien primaire** | veille primaire et distinctions ci-dessus |

Le dernier statut est un résultat de recherche négatif, non une preuve
d'inexistence dans toute la littérature. Il doit être révisé si une source
fournissant exactement le produit non pondéré, les projecteurs spatiaux
isotypiques et la non-linéarité de Leray est identifiée.

## 9. Empreintes et reproductibilité de l'audit

PDF primaires ou versions d'auteur extraits avec `pdfplumber`; les pages
d'équations de Charnyi et Waleffe ont aussi été rendues et inspectées
visuellement. Empreintes SHA-256 :

| document contrôlé | SHA-256 |
|---|---|
| Charnyi et al. 2017, PDF publié auteur | `1402F7F37126FFFE22DA01FA2C861A86781813A78CB45231C08538C0AE38497D` |
| Waleffe 1991, rapport CTR primaire | `59FE42BF172EB7348AF9A2C26DDF4AD1EA99EC5E774309EF47526655A9A1BA86` |
| Willis--Cvitanović--Avila, arXiv 1203.3701v1 | `8021BFAC44AC4584609FE7663927D0A57811C095B189AAC960C95E99E79F7935` |
| Pineau--Vicol, arXiv 2607.09619v2 récupéré le 2026-08-15 | `379591AA3C1036C9140702EBE71AAAB309FE207439A57DB5CEFF893F15D0AE8E` |
| Biferale--Titi, arXiv 1303.1215v1 | `561F0A14B59226F580396D50275EEE9250E51382BC920826DB5EE176F5124FB8` |
| Bertram, arXiv 2607.16381v1 | `231B5E1F0FAD2350F19E30C1F14C021F4BFE6F6432BACBD55AE60AD93CBC7473` |
| Kankaria et al., arXiv 2603.19180v1 | `7FF07E5D43821154B4F304F2D0A42D3B306D21B6FD60F5C89A4A6130E9B145DB` |

Commandes de contrôle documentaire utilisées :

```powershell
Invoke-WebRequest -Uri <URL-primaire> -OutFile <pdf-temporaire>
Get-FileHash <pdf-temporaire> -Algorithm SHA256
```

```python
import pdfplumber
with pdfplumber.open(path) as pdf:
    text = pdf.pages[page_index].extract_text()
```

Les fichiers temporaires et rendus ne constituent pas des artefacts du
laboratoire et sont exclus du dépôt après l'audit.

## Conclusion à transmettre au cycle principal

Le premier maillon « symétrie rotationnelle \(\Rightarrow\) loi de signe
modale » doit être **abandonné**. L'état primaire vérifié est :

```text
SO(2)-covariance
    => sélection k+l=m,
    != signe de la phase triadique;

conservation d'énergie
    => somme des transferts radiaux = 0,
    != C_m=0,
    != somme_m C_m=0;

conservation du moment angulaire
    => test contre x cross e_i,
    != test contre R u.
```

Une loi utile sur les \(C_m\) devrait donc venir d'une hypothèse PDE
supplémentaire : géométrie de la vorticité, coercivité de phase, structure
d'un profil RSS exact, ou estimation quantitative des interactions. Elle ne
peut pas être attribuée aux seules symétries, à l'énergie ou au moment
angulaire.
