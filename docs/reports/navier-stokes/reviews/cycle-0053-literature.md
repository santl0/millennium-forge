# Cycle 0053 — petite dérivée renormalisée et extraction stationnaire

**Date de coupure :** 15 août 2026

**Nature :** audit bibliographique primaire indépendant, avec vérification des
quantificateurs et des statuts éditoriaux

**Question :** un théorème publié ferme-t-il déjà le raccord

\[
 \text{petitesse de }\partial_sV\text{ sur des fenêtres}
 +\text{ compacité locale}+\text{ capture non triviale}
 \Longrightarrow\text{ contradiction par Liouville} ?       \tag{Q}
\]

## Verdict

1. **La rigidité du profil terminal est publiée et couvre le vrai
   faible-$L^3$.** Guevara--Phuc annulent tout profil faible de Leray
   $U\in W^{1,2}_{\mathrm{loc}}(\mathbb R^3)\cap
   L^{3,\infty}(\mathbb R^3)$. Chae--Wolf fournissent une route parallèle
   pour les profils lisses dans $L^{p,\infty}$, $p>3/2$.

2. **Les exclusions asymptotiquement BSS/DSS publiées supposent une
   convergence vers le profil, elles ne la déduisent pas d'une petite dérivée
   sur fenêtres.** Chae 2007 et Chae--Wolf 2017 imposent une convergence
   rescalée locale ou globale vers un profil BSS. Chae 2015 impose une
   convergence locale, uniforme sur les temps futurs proches, vers un profil
   périodique DSS régulier et globalement $L^3$.

3. **Aucun théorème publié identifié dans les sources primaires interrogées
   n'a exactement les prémisses de (Q).** Cette phrase est un résultat de
   recherche documentaire à date, pas une affirmation d'inexistence. Les
   théorèmes publiés les plus proches ont des hypothèses différentes : profil
   limite déjà prescrit, $L^3$ fort, ansatz exact, énergie globale, ou critère
   de Serrin.

4. **Sous une formulation forte et correctement alignée des trois prémisses,
   (Q) se ferme néanmoins par un lemme distributionnel élémentaire puis le
   théorème publié de Guevara--Phuc.** Il faut que les fenêtres soient centrées
   aux mêmes temps que la capture, que $\partial_sV$ tende vers zéro dans les
   distributions sur toute fenêtre fixe, que le terme quadratique passe par
   compacité forte locale, que la borne globale $L^{3,\infty}$ soit héritée,
   et que la capture survive à la limite. Le verrou n'est donc plus le
   Liouville stationnaire; il est la production simultanée de ces hypothèses.

5. **Pineau--Vicol `arXiv:2607.09619v2` contourne ce pipeline, mais reste une
   prépublication.** Son théorème 1.9 conclut la régularité à partir d'une
   petitesse du générateur à une seule tranche, sous borne Type I ponctuelle,
   solution lisse et contrôle annulaire de la pression. Il ne part ni d'une
   solution ancienne faible-$L^3$, ni d'une compacité/capture.

6. **Le résultat publié 2026 de Hou sur un blow-up presque auto-similaire ne
   porte pas sur l'équation Clay.** Il s'agit de calculs sur des équations
   axisymétriques généralisées, dimension effective variable ou modèle 3D
   rescalé à deux viscosités. Il ne fournit ni singularité de Navier--Stokes
   3D standard ni critère pour (Q).

## 1. Équation et générateur

Le cadre est Navier--Stokes incompressible standard, non forcé, viscosité un,
sur $\mathbb R^3$ :

\[
 \partial_tu-\Delta u+(u\cdot\nabla)u+\nabla p=0,
 \qquad \nabla\cdot u=0.                                   \tag{1}
\]

Pour $t<0$, posons

\[
 y=\frac{x}{\sqrt{-t}},\qquad s=-\log(-t),\qquad
 V(y,s)=\sqrt{-t}\,u(x,t),\qquad P(y,s)=(-t)p(x,t).         \tag{2}
\]

Alors

\[
 \partial_sV-\Delta V+\frac12V+\frac12y\cdot\nabla V
 +(V\cdot\nabla)V+\nabla P=0,
 \qquad \nabla\cdot V=0.                                  \tag{3}
\]

La dérivée renormalisée est exactement

\[
 \partial_sV(y,s)=\sqrt{-t}\left[
 (-t)\partial_tu-\frac12u-\frac12(x\cdot\nabla)u
 \right](x,t).                                             \tag{4}
\]

Ainsi $\partial_sV=0$ signifie BSS exacte. Une petite dérivée en une norme
faible ne signifie ni proximité forte d'un profil fixe, ni périodicité, ni
petitesse de la vitesse.

## 2. Résultats primaires exactement vérifiés

| Source et statut | Équation / notion | Hypothèses pertinentes | Conclusion | Ce qu'elle ne fournit pas |
|---|---|---|---|---|
| Cristi Guevara, Nguyen Cong Phuc, *Leray's Self-Similar Solutions to the Navier--Stokes Equations with Profiles in Marcinkiewicz and Morrey Spaces*, *SIAM J. Math. Anal.* 50(1) (2018), 541--556, [DOI 10.1137/16M110099X](https://doi.org/10.1137/16M110099X), [arXiv:1509.08177v2](https://arxiv.org/abs/1509.08177), **publié** | équation stationnaire de Leray sur $\mathbb R^3$; profil faible $U\in W^{1,2}_{\rm loc}$ testé contre les champs solénoïdaux compacts | théorème 1.3 : $U\in L^{q,\infty}$, $12/5<q<6$, ou $U\in L^{12/5}$ | $U=0$; en particulier $q=3$ | aucune extraction du profil, aucune stabilité quantitative en $\partial_sV$ |
| Dongho Chae, Jörg Wolf, *On the Liouville Type Theorems for Self-Similar Solutions to the Navier--Stokes Equations*, *Arch. Ration. Mech. Anal.* 225 (2017), 549--572, [DOI 10.1007/s00205-017-1110-7](https://doi.org/10.1007/s00205-017-1110-7), [arXiv:1609.06962v1](https://arxiv.org/abs/1609.06962), **publié** | équation stationnaire de Leray; profil lisse | théorème 1.2 : décroissance locale des hauts niveaux en $L^q$, $q>3/2$; remarque 1.3 : cette décroissance suit de $U\in L^{p,\infty}$ avec $p>q$ | $U$ constant; pour $U\in L^{p,\infty}$, $p<\infty$, la constante est zéro | aucun théorème de compacité dynamique |
| Thomas Y. Hou, Ruo Li, *Nonexistence of Locally Self-Similar Blow-up for the 3D Incompressible Navier--Stokes Equations*, *Discrete Contin. Dyn. Syst.* 18(4) (2007), 637--642, [DOI 10.3934/dcds.2007.18.637](https://doi.org/10.3934/dcds.2007.18.637), [arXiv:math/0603126v1](https://arxiv.org/abs/math/0603126), **publié** | (1), solution forte issue de donnée $L^2\cap L^p$, structure locale auto-similaire | profil rescalé convergeant en $L^p$, $3<p<\infty$, plus régularité extérieure de l'ansatz local | exclusion du blow-up localement BSS considéré | la convergence est supposée; pas faible-$L^3$, pas petitesse de $\partial_sV$ |
| Dongho Chae, *Nonexistence of Asymptotically Self-Similar Singularities in the Euler and the Navier--Stokes Equations*, *Math. Ann.* 338 (2007), 435--449, [DOI 10.1007/s00208-007-0082-6](https://doi.org/10.1007/s00208-007-0082-6), [arXiv:math/0604234v8](https://arxiv.org/abs/math/0604234), **publié** | (1), solution classique $v\in C([0,T);L^p)$ | théorème 1.4 : convergence globale rescalée en $L^p$, $p\ge3$; théorème 1.5 : convergence locale rescalée, uniforme pour $t<\tau<T$, en $L^q$ sur boule de rayon $R\sqrt{T-t}$, avec $q\ge3$ pour un $R$, ou $2\le q<3$ pour tout $R$; profil dans $L^p$, $p\ge3$ | profil nul et prolongement/régularité locale | aucune déduction de la convergence depuis une dérivée moyenne |
| Dongho Chae, *Remarks on the Asymptotically Discretely Self-Similar Solutions of the Navier--Stokes and the Euler Equations*, *Nonlinear Analysis* 125 (2015), 251--259, [DOI 10.1016/j.na.2015.05.026](https://doi.org/10.1016/j.na.2015.05.026), [arXiv:1306.0305v5](https://arxiv.org/abs/1306.0305), **publié** | (1), solution $C_tL^3_{\rm loc}$; profil périodique en temps similaire | convergence locale rescalée en $L^q$, $2\le q\le\infty$, uniforme sur $t<\tau<0$; profil $V\in C(\mathbb R;L^3\cap C^2)$ périodique | le point n'est pas singulier | une sous-suite, une récurrence faible ou une petite dérivée ne vérifie pas la définition |
| Chae--Wolf 2017, théorème 1.5, même source que ci-dessus, **publié** | (1), solution $C^2(\mathbb R^3\times(0,t_*))$ | profil $U\in L^{p,\infty}$, $p>3/2$; pour un $q\ge2$, convergence locale rescalée en $L^q$ sur toute boule $B_{r\sqrt{t_*-t}}(x_*)$, uniforme pour $t<\tau<t_*$ | $U=0$ et $(x_*,t_*)$ régulier | le profil et la convergence forte sont des hypothèses, non des sorties d'une compacité faible |
| Ben Pineau, Vlad Vicol, *On Rotated Backwards Self-Similar Solutions of the Incompressible 3D Navier--Stokes Equations*, [arXiv:2607.09619v2](https://arxiv.org/abs/2607.09619), soumis le 10 juillet, révisé le 6 août 2026, **prépublication v2** | (1), solution lisse locale; variables (2) | théorème 1.9 détaillé ci-dessous | régularité du point sous petit générateur à une tranche | pas publié à la coupure; hypothèses Type I et pression fortes |
| Thomas Y. Hou, *Nearly Self-similar Blowup of Generalized Axisymmetric Navier--Stokes Equations*, *Found. Comput. Math.* (2026), [DOI 10.1007/s10208-026-09748-8](https://doi.org/10.1007/s10208-026-09748-8), [arXiv:2405.10916v3](https://arxiv.org/abs/2405.10916), **publié, étude numérique** | équations axisymétriques généralisées à dimension effective variable et modèle rescalé à deux viscosités | discrétisations et renormalisations propres au modèle; calculs haute précision | indices numériques de blow-up presque auto-similaire dans les modèles modifiés | pas l'équation (1), pas une preuve de blow-up, pas un critère pour (Q) |

### Correction bibliographique locale

La notice présente dans le catalogue local pour Hou--Li donne correctement le
volume 18 et le DOI, mais attribue actuellement l'article à Congming Li. La
page de l'éditeur AIMS, la notice CaltechAUTHORS et le texte original donnent
**Ruo Li**, volume **18(4)**, pages 637--642, DOI
`10.3934/dcds.2007.18.637`.

## 3. Deux rigidités stationnaires : portée et détail adversarial

### 3.1 Guevara--Phuc est le raccord faible principal

Leur définition 2.2 exige

\[
 U\in W^{1,2}_{\mathrm{loc}}(\mathbb R^3),\qquad
 \nabla\cdot U=0,                                          \tag{5}
\]

et l'identité faible de l'équation stationnaire de Leray contre tout test
solénoïdal compact. Le théorème 1.3 contient exactement $q=3$ dans
$(12/5,6)$; il ne demande ni énergie globale, ni mildness, ni pression choisie
globalement. La pression disparaît des tests solénoïdaux.

### 3.2 Chae--Wolf : conclusion correcte, corollaire imprimé incomplet

Le théorème 1.2 dit qu'un profil lisse satisfaisant, pour certains
$q>3/2$ et $\alpha>0$,

\[
 \int_{B_1(y_0)\cap\{|U|>\alpha\}}|U|^q\,dx\longrightarrow0
 \quad\text{lorsque }|y_0|\to\infty                         \tag{6}
\]

est constant. La remarque 1.3 dérive (6) de
$U\in L^{p,\infty}$ avec $p>q$. Pour tout $p>3/2$, on choisit
$q\in(3/2,p)$; un champ constant non nul n'appartient pas à
$L^{p,\infty}(\mathbb R^3)$, donc $U=0$.

La version PDF publiée/arXiv du **corollaire 1.4** énonce les hypothèses
$U\in L^{p,\infty}$, $p>3/2$, puis passe directement au paragraphe suivant,
sans phrase de conclusion visible. C'est une lacune typographique de
l'énoncé du corollaire, pas du raisonnement : la conclusion $U=0$ résulte
explicitement du théorème 1.2 et de la remarque 1.3. Guevara--Phuc fournit en
outre un énoncé autonome sans cette anomalie typographique.

## 4. Les théorèmes asymptotiques n'utilisent pas une dérivée sur fenêtres

Pour Chae 2007 et Chae--Wolf 2017, l'hypothèse prend la forme

\[
 (T-t)^{\frac{q-3}{2q}}
 \sup_{t<\tau<T}
 \left\|u(\tau)-\frac1{\sqrt{T-\tau}}
 U\!\left(\frac{\cdot-x_*}{\sqrt{T-\tau}}\right)
 \right\|_{L^q(B_{r\sqrt{T-t}}(x_*))}
 \longrightarrow0,                                        \tag{7}
\]

avec les plages et facteurs de normalisation précis de chaque article. (7)
est une convergence de l'orbite entière vers un profil fixé, uniforme sur
les temps futurs proches. Elle est beaucoup plus forte que

\[
 \frac1{|I_n|}\int_{I_n}\|\partial_sV(s)\|_X\,ds
 \longrightarrow0.                                        \tag{8}
\]

En particulier, (8) peut seulement sélectionner une sous-fenêtre où la
dérivée est petite; elle n'oblige pas cette sous-fenêtre à contenir le temps
où la capture est connue.

Le résultat DSS de Chae 2015 remplace $U$ par un profil périodique
$V_*(y,s+S)=V_*(y,s)$, mais conserve une convergence du type (7). Une limite
stationnaire extraite par petite dérivée relève donc du théorème BSS, non du
théorème DSS.

## 5. Lemme de raccord que les sources permettent déjà

Considérons des temps $s_n\to\infty$ et les trajectoires translatées

\[
 V_n(y,\tau)=V(y,s_n+\tau),\qquad
 P_n(y,\tau)=P(y,s_n+\tau).                                \tag{9}
\]

Voici une formulation suffisante et falsifiable de (Q). Pour tous
$R,L<\infty$, supposons :

1. $V_n\to U$ fortement dans
   $L^3(B_R\times(-L,L))$;
2. $\nabla V_n\rightharpoonup\nabla U$ dans
   $L^2(B_R\times(-L,L))$;
3. $\partial_\tau V_n\to0$ dans
   $\mathcal D'(B_R\times(-L,L))$;
4. $\sup_{n,\tau}\|V_n(\tau)\|_{L^{3,\infty}(\mathbb R^3)}\le M$,
   avec une convergence permettant l'héritage de cette borne;
5. la capture est continue sous cette convergence, par exemple il existe
   un test vectoriel compact $\phi$ et $\eta>0$ tels que
   $|\langle V_n(0),\phi\rangle|\ge\eta$, avec convergence des traces à
   $\tau=0$; une capture spacetime alignée convient aussi.

Alors :

- (3) et la convergence distributionnelle donnent
  $\partial_\tau U=0$;
- la convergence forte $L^3_{\rm loc}$ fait passer
  $V_n\otimes V_n$ dans $L^{3/2}_{\rm loc}$;
- en testant (3) contre des champs solénoïdaux, la pression disparaît et le
  profil indépendant de $\tau$ satisfait l'équation faible stationnaire de
  Leray;
- (2) et l'énergie locale donnent
  $U\in W^{1,2}_{\rm loc}$;
- (4) donne $U\in L^{3,\infty}$;
- Guevara--Phuc impose $U=0$;
- (5) impose $U\ne0$, contradiction.

Cette chaîne n'est pas un nouveau théorème de Liouville. C'est la composition
d'un passage à la limite distributionnel avec un théorème publié. Elle montre
exactement ce que doit certifier l'analyse du cycle.

### Les formulations insuffisantes

- Une moyenne petite sur une **fenêtre croissante** ne donne pas la petitesse
  sur toute fenêtre fixe centrée au temps capturé.
- Une compacité $L^3_{\rm loc}$ **spacetime** ne donne pas automatiquement une
  convergence forte de la trace au temps central.
- Une capture $\int_{B_R}|V_n(0)|^2\ge\eta$ peut se perdre si seule une
  convergence négative ou faible est disponible à $\tau=0$.
- Une convergence locale n'hérite pas automatiquement de la norme
  $L^{3,\infty}(\mathbb R^3)$ sans borne globale uniforme et argument
  faible-étoile/Fatou.
- La petitesse de $\partial_sV$ dans une norme trop négative rend la
  stationnarité distributionnelle accessible, mais ne fournit ni la compacité
  forte nécessaire au produit quadratique, ni la capture.
- Si les centres des fenêtres sont modifiés pour obtenir (3), les paramètres
  spatiaux de translation/dilatation de la capture doivent être transportés
  avec eux.

## 6. Pineau--Vicol : un autre raccord, beaucoup plus fort

Le théorème 1.9 considère une solution **lisse** sur
$B_1\times[-1,0)$ satisfaisant

\[
 |u(x,t)|\le\frac{C_u}{\sqrt{-t}+|x|},                     \tag{10}
\]

et un contrôle de pression

\[
 |p(x,t)|\le C_p
 \quad\text{sur }\{1/2<|x|<3/4\}\times[-1,0).             \tag{11}
\]

Il existe $\delta_0(C_u)>0$ et $s_0(C_u,C_p)$ tels que, si pour une seule
$\bar s\ge s_0$,

\[
 \|\partial_sV(\cdot,\bar s)\|_{L^\infty(B_{e^{\bar s/2}})}
 \le\delta_0,                                              \tag{12}
\]

alors $(0,0)$ est régulier. La remarque 1.11 remplace (12) par la condition
pondérée plus faible

\[
 \int_{B_{e^{\bar s/2}}}|\partial_sV(y,\bar s)|
 (1+|y|)e^{-|y|^2/8}\,dy\lesssim\delta_0.                  \tag{13}
\]

Le mécanisme est quantitatif : (12)/(13) donne une petite enstrophie locale,
le lemme 9.4 la propage vers les temps suivants, puis un critère
$\varepsilon$-régulier de Caffarelli--Kohn--Nirenberg conclut.

Une petitesse sur fenêtres implique ce théorème uniquement si elle permet de
sélectionner une tranche tardive vérifiant **(13)**, tout en conservant
(10)--(11). Une petitesse dans $H^{-m}_{\rm loc}$ ou en distributions ne
contrôle pas (13). De plus, la borne ponctuelle (10) implique une borne
uniforme $L^{3,\infty}$, mais l'implication réciproque est fausse. Le théorème 1.9 ne
ferme donc pas le raccord actif, même conditionnellement, sans trois nouvelles
arêtes fortes.

Statut : `arXiv:2607.09619v2`, aucune publication ni DOI trouvés à la coupure.
Il doit rester `PREPRINT_CLAIM`, malgré la précision de l'énoncé.

## 7. Veille différentielle 2025--2026

La veille a combiné les requêtes arXiv exactes `self-similar + Navier-Stokes`,
`scaling generator + Navier-Stokes`, `renormalized + Navier-Stokes + blowup`
et `quasi-self-similar + Navier-Stokes`, puis une recherche Crossref filtrée
du 1er janvier 2025 au 15 août 2026. Les titres candidats ont été reclassés
par équation et notion de résultat.

- **Pineau--Vicol 2026** est le seul résultat primaire direct trouvé portant
  sur le générateur de l'échelle pour Navier--Stokes incompressible 3D
  standard. C'est une prépublication v2.
- **Hou 2026** est bien publié et concerne explicitement le « nearly
  self-similar blowup », mais l'article annonce une investigation numérique
  d'équations généralisées/modifiées. Le texte précise que le modèle rescalé
  n'est pas identique aux équations 3D originales; il utilise notamment deux
  viscosités $\nu_1=0.0006$ et $\nu_2=10\nu_1$ dans l'expérience citée.
- **Huang--Karakhanyan `arXiv:2511.02579v1`** porte sur des solutions faibles
  adaptées *stationnaires* en dimension cinq et une formule de monotonie
  presque homogène. Équation, dimension et absence de temps renormalisé le
  rendent non transférable à (Q).
- **Binz--Coiculescu `arXiv:2607.12159v1`** traite des profils *forward*
  homothétiques. Il ne fournit pas le passage backward dynamique de (Q).
- Les critères de régularité 2025--2026 de type Serrin/localisation retrouvés
  par Crossref ne portent pas sur $\partial_sV$ et n'ajoutent pas le maillon
  recherché.

Cette veille qualifie les résultats indexés et inspectés. Elle ne transforme
pas l'absence de correspondance en théorème d'inexistence bibliographique.

## 8. Passe contradictoire

1. **Profil non nul.** Stationnarité plus Liouville ne produit une
   contradiction que si la capture survit dans une topologie compatible.
2. **Temps central.** Sélectionner une bonne sous-fenêtre par moyenne peut
   déplacer le centre loin de la capture.
3. **Produit quadratique.** La convergence faible seule ne passe pas
   $V_n\otimes V_n$; un défaut de Reynolds peut subsister et forcer le profil.
4. **Pression.** Elle peut être éliminée dans l'équation faible stationnaire,
   mais pas dans tous les critères locaux de régularité; Pineau--Vicol impose
   (11).
5. **Endpoint global.** La convergence locale ne contrôle pas les queues;
   l'appartenance globale $L^{3,\infty}$ du profil doit être démontrée.
6. **Dérivée moyenne.** $\int\partial_sV$ petit avec signe peut résulter
   d'annulations; il faut la norme de la dérivée ou la convergence dans
   $\mathcal D'$, pas seulement une différence de bouts de fenêtre.
7. **Pineau--Vicol.** Un seuil à une tranche sous Type I n'est pas un théorème
   de compacité faible-$L^3$, et son statut reste prépublication.
8. **Hou 2026.** « Publié » qualifie l'article, non une preuve de blow-up de
   l'équation standard; sa conclusion principale pertinente ici est
   numérique et concerne des modèles différents.
9. **Corollaire Chae--Wolf.** Ne pas citer textuellement une conclusion
   absente de la ligne imprimée; citer la déduction théorème 1.2 + remarque
   1.3, ou utiliser Guevara--Phuc.
10. **Asymptotique versus sous-suite.** Les théorèmes de Chae demandent une
    convergence de toute l'orbite tardive, non un unique profil d'adhérence.

## 9. Traçabilité des PDF primaires

| Texte | SHA-256 du PDF audité |
|---|---|
| Guevara--Phuc, `1509.08177v2` | `3AB53F7A6268767796837B7B09E5E9120B7E7773621C2FFD30D14242299593D9` |
| Chae--Wolf, `1609.06962v1` | `274073640A2216FCA2F5E376F47462E23B53F5256831C50B86D38488F3F0A7E7` |
| Hou--Li, `math/0603126v1` | `7D87D849E60D7457175792304EF41A3B9AD588D5C2F82139D70A70837BE83877` |
| Chae, `math/0604234v8` | `F2B6A4C5723C5986D52E1AF872AF667756CC3BECB8B3C2D47DEDD07E218DE82A` |
| Chae DSS, `1306.0305v5` | `C0439015DEA1432DCF4986C0A2537D3C61BF908363E036E7564B628A9F85521A` |
| Pineau--Vicol, `2607.09619v2` | `379591AA3C1036C9140702EBE71AAAB309FE207439A57DB5CEFF893F15D0AE8E` |
| Hou, `2405.10916v3` | `51A3CCB07866F834E20FC650BA03DB27C02DA732708D1CDD17A55BBF8ECF8A08` |

## 10. Décision scientifique

**Ne pas chercher un nouveau Liouville stationnaire faible-$L^3$.** Le
théorème publié nécessaire existe déjà.

**Ne pas invoquer un théorème asymptotique publié tant que (7) n'est pas
établi.** Une dérivée petite sur fenêtres n'est pas cette convergence.

**Lemme actif recommandé : alignement fenêtre--capture.** Formuler et prouver
que les mêmes centres $s_n$ satisfont simultanément :

\[
 \partial_\tau V_n\to0\text{ dans }\mathcal D'_{\rm loc},
 \quad V_n\to U\text{ fortement dans }L^3_{\rm loc},
 \quad U\ne0,\quad U\in L^{3,\infty}.                      \tag{14}
\]

Si (14) est obtenu avec l'énergie locale, la contradiction est fermée par
Guevara--Phuc. Si la seule sortie disponible est une moyenne de dérivée sur
des fenêtres croissantes ou une capture à une tranche sans convergence de
trace, le raccord reste ouvert et l'échec doit être enregistré précisément à
cette arête, non attribué au théorème de Liouville.
