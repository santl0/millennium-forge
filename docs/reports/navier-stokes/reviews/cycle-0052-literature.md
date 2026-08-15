# Cycle 0052 — profils backward, solutions anciennes et récurrence

**Date de coupure :** 15 août 2026

**Nature :** veille bibliographique primaire indépendante et passe
contradictoire

**Question auditée :** quelles rigidités publiées s'appliquent à une solution
ancienne de Navier--Stokes 3D uniformément bornée dans le vrai espace de
Lorentz spatial $L^{3,\infty}(\mathbb R^3)$, lorsqu'elle est exactement
backward self-similar (BSS), backward discretely self-similar (DSS), mild,
locale de Leray ou faible adaptée ? Une propriété de récurrence en temps
similaire permet-elle de rejoindre ces rigidités ?

## Verdict différentiel

1. **Le sous-cas exactement BSS et faible $L^3$ est déjà fermé.** Deux
   résultats publiés, absents du maillon bibliographique actif, l'établissent
   directement. Chae--Wolf excluent tout profil lisse
   $U\in L^{p,\infty}(\mathbb R^3)$, $3/2<p<\infty$. Guevara--Phuc
   excluent tout profil faible
   $U\in W^{1,2}_{\mathrm{loc}}\cap L^{q,\infty}$,
   $12/5<q<6$. Les deux intervalles contiennent $p=q=3$.

2. **Ce résultat se raccorde bien à une ancienne locale de Leray/faible
   adaptée exactement BSS.** L'énergie locale sur une bande de temps séparée
   de $0$, jointe à l'ansatz exact, donne
   $U\in W^{1,2}_{\mathrm{loc}}$; l'équation distributionnelle donne
   l'équation stationnaire de Leray faible; la borne critique donne
   $U\in L^{3,\infty}$. Le théorème de Guevara--Phuc impose alors
   $U=0$. Une ancienne mild vérifiant les mêmes hypothèses est a fortiori
   couverte.

3. **Le sous-cas exactement DSS avec la seule borne faible $L^3$ n'est pas
   fermé.** Les exclusions publiées portent soit sur $L^3$ fort, soit sur
   un profil périodique avec convergence forte, soit sur une borne Type I
   ponctuelle et un facteur de discrétisation proche de $1$. Aucune source
   primaire examinée ne prouve

   \[
     u\ \lambda\text{-DSS},\qquad
     \sup_{t<0}\|u(t)\|_{L^{3,\infty}}<\infty
     \quad\Longrightarrow\quad u=0                         \tag{V1}
   \]

   pour tout $\lambda>1$, dans une classe locale de Leray, adaptée ou mild.

4. **Une simple récurrence faible de l'orbite renormalisée ne fournit pas
   (V1).** La compacité faible-étoile de boules de $L^{3,\infty}$ ne donne
   ni retour au même état, ni compacité forte, ni stationnarité, ni
   périodicité. Dans une classe faible non unique, même une égalité à deux
   temps ne propage pas automatiquement une orbite périodique. Aucun théorème
   primaire trouvé ne promeut une ancienne faible $L^3$ récurrente en profil
   BSS ou DSS.

5. **La nouveauté primaire directe de 2026 est Pineau--Vicol
   `arXiv:2607.09619v2`.** Elle exclut des profils RSS/DSS/RDSS backward sous
   borne Type I ponctuelle, pour rotations extrêmes ou périodes suffisamment
   courtes, et donne un critère local de quasi-auto-similarité sur une tranche.
   C'est un progrès substantiel, mais la borne Type I ponctuelle est
   strictement plus forte que la seule borne $L^{3,\infty}$, et les régimes
   DSS de période arbitraire, rotation intermédiaire et orbite apériodique
   restent hors champ.

Le correctif important pour le graphe est donc :

   \[
 \boxed{\text{ancienne exactement BSS et }L^{3,\infty}
        \Longrightarrow U=0}\quad\text{publié},             \tag{V2}
   \]

mais

\[
 \text{ancienne }L^{3,\infty}
 \dashrightarrow \text{orbite compacte/récurrente}
 \dashrightarrow \text{BSS ou DSS}                          \tag{V3}
\]

reste un raccord manquant, et la seconde flèche n'est pas vraie en dynamique
générale sans hypothèse de rigidité supplémentaire.

## 1. Équation, échelle et dictionnaire exact

L'audit porte exclusivement sur Navier--Stokes incompressible standard, non
forcé, de viscosité normalisée à un, dans l'espace entier :

\[
 \partial_tu-\Delta u+(u\cdot\nabla)u+\nabla p=0,
 \qquad \nabla\cdot u=0,
 \qquad (x,t)\in\mathbb R^3\times(-\infty,0).                \tag{1}
\]

La remise à l'échelle Clay est

\[
 u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),
 \qquad p_\lambda(x,t)=\lambda^2p(\lambda x,\lambda^2t).    \tag{2}
\]

La norme $L^{3,\infty}_x$ est invariante par (2). Avec

\[
 y=\frac{x}{\sqrt{-t}},\qquad s=-\log(-t),\qquad
 u(x,t)=(-t)^{-1/2}V(y,s),                                  \tag{3}
\]

l'équation renormalisée est

\[
 \partial_sV-\Delta V+\frac12V+\frac12y\cdot\nabla V
 +(V\cdot\nabla)V+\nabla P=0,
 \qquad \nabla\cdot V=0.                                   \tag{4}
\]

Les notions ne sont pas interchangeables :

- **BSS exacte :** $V$ est stationnaire. Son profil $U$ résout

  \[
   -\Delta U+\frac12U+\frac12y\cdot\nabla U
   +(U\cdot\nabla)U+\nabla P=0,
   \qquad\nabla\cdot U=0.                                   \tag{5}
  \]

- **λ-DSS exacte :** $V(s+S)=V(s)$, avec $S=2\log\lambda$.
- **RSS/RDSS :** équilibre relatif/orbite périodique relative sous le groupe
  des rotations; ce n'est pas une BSS/DSS ordinaire sauf rotation nulle.
- **Asymptotiquement BSS/DSS :** la solution converge, dans une topologie
  prescrite, vers un profil stationnaire/périodique. Une sous-suite récurrente
  ne suffit pas à cette définition.
- **Ancienne locale de Leray/faible adaptée :** solution distributionnelle
  avec contrôle énergétique local et inégalité d'énergie locale. Ces axiomes
  ne donnent ni formule mild globale, ni unicité.
- **Ancienne mild :** satisfait une représentation de Duhamel avec projection
  de Leray dans une classe fonctionnelle où les termes sont définis. C'est une
  hypothèse plus rigide que « faible adaptée ».

Enfin, le titre d'Escauriaza--Seregin--Šverák de 2003 emploie la notation
$L_{3,\infty}$ pour $L^\infty_tL^3_x$. Leur endpoint est le **$L^3$
spatial fort**, et non le Lorentz spatial $L^{3,\infty}_x$ examiné ici.

## 2. Tableau des résultats primaires

| Source primaire et statut | Équation, domaine, solution | Hypothèses exactes utiles | Conclusion | Transfert vers une ancienne $L^{3,\infty}$ |
|---|---|---|---|---|
| Nečas--Růžička--Šverák, *Acta Math.* 176 (1996), [DOI 10.1007/BF02551584](https://doi.org/10.1007/BF02551584), publié | (1), $\mathbb R^3$, profil BSS | profil $U\in L^3(\mathbb R^3)$ | $U=0$ | Non direct : $L^{3,\infty}\not\subset L^3$. |
| Tsai, *Arch. Ration. Mech. Anal.* 143 (1998), [DOI 10.1007/s002050050106](https://doi.org/10.1007/s002050050106), publié | (1), $\mathbb R^3$, solution/profil BSS faible | énergie locale finie jusqu'au temps terminal, ou profil $L^q$, $3<q<\infty$ | solution/profil trivial | Utile, mais le raccord terminal et $L^q$ fort ne suivent pas de la seule norme faible $L^3$. |
| Chae--Wolf, *Arch. Ration. Mech. Anal.* 225 (2017), 549--572, [DOI 10.1007/s00205-017-1110-7](https://doi.org/10.1007/s00205-017-1110-7), [arXiv:1609.06962v1](https://arxiv.org/abs/1609.06962), publié | équation de Leray (5), profil lisse | théorème 1.2 : décroissance locale des hauts niveaux en $L^q$, $q>3/2$; corollaire 1.4 : $U\in L^{p,\infty}$, $3/2<p<\infty$ | $U$ constant, puis $U=0$ sous l'intégrabilité Lorentz globale | **Oui pour BSS exacte**, après régularité du profil. Inclut $p=3$. Pas DSS. |
| Guevara--Phuc, *SIAM J. Math. Anal.* 50 (2018), 541--556, [DOI 10.1137/16M110099X](https://doi.org/10.1137/16M110099X), [arXiv:1509.08177v2](https://arxiv.org/abs/1509.08177), publié | (5), profil faible $U\in W^{1,2}_{\rm loc}$, testé contre les champs solénoïdaux compacts | théorème 1.3 : $U\in L^{q,\infty}$, $12/5<q<6$, ou $U\in L^{12/5}$ | $U=0$ | **Raccord direct le plus propre pour BSS locale de Leray/adaptée**. Inclut $q=3$. |
| Wang--Jiu--Wei, *SIAM J. Math. Anal.* 54 (2022), 2768--2791, [DOI 10.1137/20M1346055](https://doi.org/10.1137/20M1346055), [arXiv:2006.15776v1](https://arxiv.org/abs/2006.15776), publié | (5), profil faible $W^{1,2}_{\rm loc}$ | $U\in\dot M^{q,l}$, $2<l\le q<\infty$, ou $U\in\dot M^{q,1}$, $3/2<q<6$ | $U=0$ | Confirme l'exclusion dans une famille de Morrey contenant le faible $L^3$; ne traite pas les orbites périodiques. |
| Chae, *Nonlinear Analysis* 125 (2015), 251--259, [DOI 10.1016/j.na.2015.05.026](https://doi.org/10.1016/j.na.2015.05.026), [arXiv:1306.0305v5](https://arxiv.org/abs/1306.0305), publié | (1), $\mathbb R^3\times(-\infty,0)$, solution $C_tL^3_x$; puis blow-up local asymptotiquement DSS | théorème 1.1 : DSS exacte et $C((-\infty,0);L^3)$; théorème 1.2 : convergence locale rescalée en $L^q$, $2\le q\le\infty$, vers $V\in C_s(L^3\cap C^2_y)$ périodique | le temps $0$ n'est pas singulier | $L^3$ fort ou convergence vers un profil périodique imposés; pas le seul $L^{3,\infty}$, pas une simple sous-suite. |
| Chae--Wolf, *Commun. PDE* 42 (2017), 1359--1374, [DOI 10.1080/03605302.2017.1358275](https://doi.org/10.1080/03605302.2017.1358275), [arXiv:1610.09464v2](https://arxiv.org/abs/1610.09464), publié | (1), $Q=\mathbb R^3\times(-\infty,0)$, solution DSS lisse | théorème 1.1 : $u\in C_tL^p_x$, $3\le p<\infty$; théorème 1.3 : borne ponctuelle Type I $C_*/(\lvert x\rvert+\sqrt{-t})$ et $1<\lambda<\lambda_*(C_*)$ | régularité/borne Type I; sous les secondes hypothèses, $u=0$ | Ne couvre ni Lorentz faible $L^3$ seul, ni λ arbitraire. Pour $p=3$, ESS donne la régularité complète. |
| Koch--Nadirashvili--Seregin--Šverák, *Acta Math.* 203 (2009), 83--105, [DOI 10.1007/s11511-009-0039-6](https://doi.org/10.1007/s11511-009-0039-6), publié | (1), $\mathbb R^3\times(-\infty,0)$, anciennes faibles et mild | théorèmes de Liouville sous dimension deux, axisymétrie sans swirl, ou hypothèses supplémentaires; distinction des solutions parasites $u=b(t)$ | rigidités partielles et cadre des anciennes mild bornées | Aucun Liouville 3D général, donc aucun résultat automatique pour une ancienne faible $L^3$ non BSS. Les parasites non nuls ne sont toutefois pas dans $L^{3,\infty}(\mathbb R^3)$. |
| Albritton--Barker, *J. Math. Fluid Mech.* 21 (2019), article 43, [DOI 10.1007/s00021-019-0448-z](https://doi.org/10.1007/s00021-019-0448-z), [arXiv:1811.00502](https://arxiv.org/abs/1811.00502), publié | (1), locale puis $\mathbb R^3$, faible adaptée/mild ancienne | singularité Type I et fonctionnelle Type I finie; exclusion si norme $L^3$ forte bornée le long d'une suite vers $-\infty$ | équivalence conditionnelle avec une ancienne mild bornée non triviale; Liouville sous hypothèse $L^3$ forte séquentielle | Le passage Type I vers ancienne est pertinent; l'hypothèse forte $L^3$ ne suit pas de $L^{3,\infty}$. |
| Ożański--Palasek, *Annals of PDE* 9 (2023), article 15, [DOI 10.1007/s40818-023-00156-7](https://doi.org/10.1007/s40818-023-00156-7), [arXiv:2210.10030v3](https://arxiv.org/abs/2210.10030), publié | (1), $\mathbb R^3\times(-\infty,0)$, ancienne axisymétrique régulière | axisymétrie exacte et borne uniforme $L^{3,\infty}$ | solution triviale | Vrai Liouville endpoint, mais l'axisymétrie ne découle pas d'une borne Clay. |
| Taniuchi, *Math. Ann.* 389 (2024), 2561--2594, [DOI 10.1007/s00208-023-02702-x](https://doi.org/10.1007/s00208-023-02702-x), publié, catalogue `NS-SRC-0190` | (1), $\mathbb R^3$ et domaines non bornés, avec/sans force, solutions mild faible $L^3$ | continuité forte dans le Lorentz et conditions supplémentaires de petitesse/comportement passé pour l'unicité | bien-posée/unicité dans les sous-classes énoncées | Ne donne pas un Liouville ancien endpoint sans ces hypothèses. |
| Barker--Prange, *Commun. Math. Phys.* 385 (2021), 717--792, [DOI 10.1007/s00220-021-04122-x](https://doi.org/10.1007/s00220-021-04122-x), [arXiv:2003.06717v3](https://arxiv.org/abs/2003.06717), publié | (1), solutions lisses/énergie finie et scénarios Type I; corollaire conditionnel DSS | suppose l'existence d'une solution backward DSS non nulle dans $C_tL^p_x$, $p\ge3$ | bornes quantitatives de concentration | Le papier dit explicitement que l'existence de DSS backward non nulles reste ouverte; son corollaire ne les construit ni ne les exclut. |
| Pineau--Vicol, [arXiv:2607.09619v2](https://arxiv.org/abs/2607.09619), soumis le 10 juillet et révisé le 6 août 2026, prépublication sans DOI/journal trouvé à la coupure | (1), $\mathbb R^3\times[-1,0)$, solution lisse, profils $C^2$ | borne Type I ponctuelle; RSS : rotation petite ou grande; DSS : λ proche de 1; RDSS : couples rotation/période quantifiés; critère local : pression contrôlée sur une couronne et petit générateur d'échelle en $L^\infty$ à un temps | trivialité des profils dans les régimes indiqués; régularité locale pour le critère à une tranche | Progrès récent le plus direct. Type I ponctuel ⇒ faible $L^3$, mais la réciproque est fausse; période arbitraire et rotation intermédiaire restent ouvertes. |

## 3. Raccord rigoureux du cas BSS faible $L^3$

Soit (u) une solution ancienne locale de Leray ou faible adaptée de (1),
exactement BSS au sens distributionnel :

\[
 u(x,t)=(-t)^{-1/2}U\!\left(\frac{x}{\sqrt{-t}}\right).      \tag{6}
\]

Supposons

\[
 \operatorname*{ess\,sup}_{t<0}
 \|u(t)\|_{L^{3,\infty}(\mathbb R^3)}<\infty.              \tag{7}
\]

Le raccord se décompose en trois arêtes vérifiables.

### 3.1 Énergie locale → profil faible

Sur toute bande (I=[-2,-1/2]), les axiomes locaux donnent

\[
 u\in L^\infty(I;L^2_{\mathrm{loc}}),
 \qquad \nabla u\in L^2(I;L^2_{\mathrm{loc}}).              \tag{8}
\]

Dans (6), (x\mapsto x/\sqrt{-t}) reste une dilatation uniformément
bornée et inversible pour (t\in I). L'intégration de (8) sur un sous-intervalle
de mesure positive donne donc

\[
 U\in W^{1,2}_{\mathrm{loc}}(\mathbb R^3).                 \tag{9}
\]

L'insertion de (6) dans la formulation distributionnelle, avec changement de
variables dans les tests solénoïdaux compacts, donne exactement la formulation
faible de (5) de la définition 2.2 de Guevara--Phuc. La pression n'est pas
supposée locale arbitraire : elle est éliminée par les tests solénoïdaux; elle
peut ensuite être reconstruite modulo fonction du temps.

### 3.2 Échelle critique → endpoint du profil

Pour presque tout (t<0), l'invariance Lorentz de (2) donne

\[
 \|u(t)\|_{L^{3,\infty}}=\|U\|_{L^{3,\infty}}.             \tag{10}
\]

Ainsi (7) implique (U\in L^{3,\infty}). Il n'y a ici ni constante dépendant
d'une troncature, ni perte de puissance d'échelle, ni passage au domaine
infini.

### 3.3 Théorème publié → trivialité

Le théorème 1.3 de Guevara--Phuc s'applique avec (q=3\in(12/5,6)) à
(9)--(10) et donne (U=0). Par (6), (u=0). Leur article rappelle en outre
que les profils faibles ainsi définis sont lisses, ce qui permet aussi
d'appliquer le corollaire 1.4 de Chae--Wolf avec (p=3).

Ce raccord prouve (V2) dans les classes standards locale de Leray/faible
adaptée. Il ne requiert pas une trace d'énergie globale à (t=0). Il ne dit
rien d'une ancienne non exactement BSS.

## 4. Pourquoi DSS faible $L^3$ reste distinct

Une DSS exacte donne une solution périodique de (4), pas une solution de (5).
Les arguments maximum-principle/coercivité des profils stationnaires ne
s'appliquent donc pas terme à terme : le terme (∂_sV) ne disparaît pas.

Les frontières publiées sont les suivantes :

1. **(L^3) fort.** Chae 2015 exclut une singularité DSS pour
   (u\in C_tL^3_x). La continuité absolue des intégrales (L^3), utilisée
   dans les mécanismes endpoint forts, échoue dans (L^{3,\infty}).
2. **Période courte avec Type I ponctuel.** Chae--Wolf 2017 puis
   Pineau--Vicol 2026 excluent λ suffisamment proche de (1), avec un seuil
   dépendant de la constante Type I. La dépendance
   $\lambda_*=\lambda_*(C_*)$ est essentielle et ne permet pas d'itérer
   jusqu'à une
   période arbitraire.
3. **Profil asymptotique imposé.** Chae 2015 suppose une convergence locale
   rescalée vers un profil périodique régulier dans une topologie (L^q).
   Une convergence faible-étoile le long d'une sous-suite ne vérifie pas cette
   hypothèse.
4. **Quantification conditionnelle.** Barker--Prange 2021 quantifie la
   concentration qu'aurait une DSS non nulle, mais conserve son existence
   comme hypothèse.

L'implication ponctuelle

\[
 |u(x,t)|\le \frac{C_*}{|x|+\sqrt{-t}}
 \quad\Longrightarrow\quad
 \sup_{t<0}\|u(t)\|_{L^{3,\infty}}\le C\,C_*              \tag{11}
\]

est immédiate par fonction de distribution. La réciproque est fausse : une
norme Lorentz globale n'impose aucun majorant ponctuel, aucune régularité
uniforme du profil et aucune valeur exploitable de (C_*). Les théorèmes Type
I récents ne se transfèrent donc pas par simple inclusion d'espaces.

## 5. Anciennes : local Leray, adaptée et mild

### 5.1 Ce que les classes donnent réellement

- Une ancienne locale de Leray/faible adaptée donne l'équation
  distributionnelle, l'énergie locale et la compacité locale nécessaire aux
  zooms. Elle ne donne pas une évolution unique dans le temps similaire.
- Une ancienne mild globale donne un cocycle de Duhamel et élimine les
  solutions parasites dépendant seulement du temps lorsque le cadre impose
  l'intégrabilité spatiale. Elle reste toutefois soumise aux hypothèses de la
  classe de mildness et à la normalisation non locale de la pression.
- La borne (L^{3,\infty}) élimine elle-même les parasites spatiaux constants
  non nuls de KNSS, car ceux-ci n'appartiennent pas à
  (L^{3,\infty}(\mathbb R^3)). Elle ne fournit pas pour autant un théorème
  de Liouville.

### 5.2 Frontière exacte connue

Les résultats KNSS restent conditionnels en dimension trois générale.
Albritton--Barker relient certains blow-ups Type I à des anciennes mild
bornées non triviales, mais leur rigidité endpoint réutilise du (L^3) fort
le long d'une suite de temps. Ożański--Palasek obtiennent bien le Liouville
uniforme faible-(L^3), mais seulement sous axisymétrie exacte. Taniuchi traite
la mildness/unicité faible-(L^3) sous continuité forte et hypothèses
additionnelles, non toute ancienne locale de Leray.

À la date de coupure, aucun résultat primaire audité n'établit

\[
 \left.
 \begin{array}{c}
 u\text{ ancienne locale de Leray, adaptée ou mild},\\
 \sup_{t<0}\|u(t)\|_{L^{3,\infty}}<\infty
 \end{array}
 \right\}
 \Longrightarrow u=0                                      \tag{12}
\]

sans auto-similarité exacte, symétrie ou hypothèse supplémentaire.

## 6. Audit de la « récurrence »

Le mot doit être remplacé par un quantificateur et une topologie.

### 6.1 Périodicité exacte


\[
 V(s+S)=V(s)\quad\text{pour tout }s                         \tag{13}
\]

est exactement DSS. Une égalité isolée
(V(s_0+S)=V(s_0)) ne donne (13) que dans une classe où l'évolution issue de
cet état est unique, au moins vers les temps futurs. Étendre la périodicité
aux temps antérieurs exige en plus une injectivité/backward uniqueness
appropriée. Ces propriétés ne font pas partie des axiomes d'une solution
faible adaptée.

### 6.2 Retour faible ou faible-étoile

Comme

\[
 L^{3,\infty}=(L^{3/2,1})^*                                \tag{14}
\]

au sens usuel des espaces de Lorentz, une orbite bornée admet des sous-suites
faible-étoile après les précautions de séparabilité du prédual. Cela fournit
au plus

\[
 V(s_n)\stackrel{*}{\rightharpoonup}W.                     \tag{15}
\]

Rien dans (15) n'impose (W=V(s_0)), ne contrôle la perte de masse par
translation/dilatation, ni ne rend le terme quadratique continu. Il manque une
compacité locale forte et un contrôle de la pression pour passer de l'orbite
à un système dynamique fermé.

### 6.3 Précompacité ou récurrence topologique

Même une orbite précompacte récurrente d'un système dynamique autonome n'est
en général ni fixe ni périodique. Il faudrait une fonctionnelle de Lyapunov
strictement monotone, un principe de gradient, une monotonie à égalité rigide,
ou un petit générateur d'échelle quantitatif. Aucun de ces mécanismes ne
découle actuellement de la seule borne faible-(L^3) pour (4).

Le théorème 1.9 de Pineau--Vicol montre une forme falsifiable de l'information
manquante : à une tranche tardive, le résidu du générateur d'échelle est petit
en (L^\infty(B_1)), en présence d'une borne Type I locale et d'un contrôle de
pression sur une couronne. Ce résultat ne déduit aucun de ces trois contrôles
de (L^{3,\infty}).

### 6.4 Arêtes du graphe

| Arête | Statut au 15 août 2026 | Obstacle |
|---|---|---|
| ancienne uniforme (L^{3,\infty}) → sous-suite faible-étoile | classique, après choix de topologie | ne donne pas de limite forte ni de retour |
| sous-suite faible-étoile → ancienne limite | conditionnel | produit quadratique, pression, tightness et translations |
| ancienne limite → même état récurrent | manquante | aucune récurrence imposée par bornitude |
| un retour → périodicité | conditionnelle à l'unicité | unicité absente dans la classe adaptée |
| orbite récurrente/précompacte → BSS ou DSS | manquante et fausse abstraitement | aucune fonctionnelle de rigidité |
| BSS (L^{3,\infty}) → zéro | **classique publié** | Chae--Wolf; Guevara--Phuc |
| DSS (L^{3,\infty}), λ arbitraire → zéro | ouverte | terme temporel et absence de compactification forte |
| DSS Type I ponctuel, λ proche de 1 → zéro | publié/préprint renforcé | seuil dépendant de la constante Type I |

## 7. Veille différentielle 2025--2026

La veille primaire a interrogé les index arXiv par les chaînes exactes
`backward self-similar + Navier-Stokes`, `discretely self-similar +
Navier-Stokes` et `ancient solution + Navier-Stokes + Liouville`, puis vérifié
les PDF/versionnements et les métadonnées Crossref des résultats pertinents.

- **Résultat direct nouveau :** Pineau--Vicol,
  [arXiv:2607.09619v2](https://arxiv.org/abs/2607.09619), soumis le 10 juillet
  2026 et révisé le 6 août 2026. Aucun DOI ni statut publié n'a été trouvé à la
  coupure; il reste donc `PREPRINT_CLAIM`, non `PAPER_PROOF` dans le registre.
- **Résultats Type II de Seregin :** les prépublications 2025--2026 auditées
  ailleurs dans le laboratoire produisent, sous scénarios quantitatifs
  supplémentaires, des limites anciennes d'Euler parce que la viscosité
  disparaît dans le zoom. Elles ne donnent ni récurrence Navier--Stokes ni
  Liouville endpoint pour (12).
- **Aucun autre résultat primaire direct 2025--2026 trouvé** ne ferme (V1),
  (12), ou ne promeut un retour faible en BSS/DSS. Les occurrences sur modèles
  dyadiques, Navier--Stokes compressible ou solutions DSS *forward* ont été
  écartées : l'équation, le sens du temps ou la notion de singularité diffère.

Cette conclusion est une veille à date et non une preuve d'inexistence d'un
manuscrit non indexé.

## 8. Passe contradictoire

1. **Confusion endpoint ESS.** Remplacer (L^{3,\infty}_x) par le
   (L^\infty_tL^3_x) du titre ESS fermerait artificiellement le problème.
   Les espaces sont distincts.
2. **Quantificateur DSS.** « λ proche de 1 pour chaque (C_*) » n'est pas
   « tout λ » et le seuil n'est pas uniforme en (C_*).
3. **Hypothèse silencieuse Type I.** Le majorant ponctuel (11) n'est pas une
   conséquence de la norme Lorentz; l'utiliser inverserait une implication.
4. **Notion de solution.** Un théorème sur profil lisse ne s'applique à une
   solution faible qu'après le raccord (W^{1,2}_{\rm loc}) et la régularité
   elliptique. Guevara--Phuc fournit précisément la formulation faible.
5. **Pression.** Le passage au profil est fait contre des tests solénoïdaux;
   aucune pression locale arbitraire n'est utilisée comme pression globale.
6. **Compacité.** Banach--Alaoglu ne fournit que (15), pas la convergence
   forte requise par le terme (V\otimes V) ni la tightness à l'infini.
7. **Unicité.** Un retour à deux temps n'est pas une période dans la classe
   faible adaptée. Supposer le contraire rendrait l'argument circulaire.
8. **Asymptotique.** Exclure un profil BSS ou DSS exact n'exclut ni une orbite
   apériodique, ni une cascade multi-échelle, ni un blow-up Type II.
9. **Corollaire conditionnel.** Barker--Prange ne prouve pas l'existence d'une
   DSS : il quantifie ce qui suivrait de son existence.
10. **Solution parasite.** Les parasites KNSS avertissent que la pression et
    la mildness comptent, mais ne sont pas des contre-exemples à (12), car un
    champ spatialement constant non nul n'est pas faible-(L^3) global.

## 9. Sources à ajouter au catalogue

Les identifiants effectivement alloués sont :

- `NS-SRC-0203` — Guevara--Phuc 2018, profil faible
  Marcinkiewicz/Morrey, `PAPER_PROOF`, priorité haute;
- `NS-SRC-0204` — Chae--Wolf 2017, Liouville BSS Lorentz,
  `PAPER_PROOF`, priorité haute;
- `NS-SRC-0205` — Wang--Jiu--Wei 2022, extension Morrey,
  `PAPER_PROOF`, priorité contextuelle.

Les sources Nečas--Růžička--Šverák, Tsai, KNSS, Chae 2015, Chae--Wolf DSS,
Ożański--Palasek, Albritton--Barker, Barker--Prange, Taniuchi et
Pineau--Vicol existent déjà dans le catalogue et ne doivent pas être
dupliquées.

## 10. Traçabilité des textes primaires

Les PDF arXiv ont été lus intégralement par extraction locale. Empreintes
SHA-256 :

| arXiv | SHA-256 du PDF audité |
|---|---|
| `1306.0305v5` | `C0439015DEA1432DCF4986C0A2537D3C61BF908363E036E7564B628A9F85521A` |
| `1509.08177v2` | `3AB53F7A6268767796837B7B09E5E9120B7E7773621C2FFD30D14242299593D9` |
| `1609.06962v1` | `274073640A2216FCA2F5E376F47462E23B53F5256831C50B86D38488F3F0A7E7` |
| `1610.09464v2` | `1F537BC2B6B2E7752DB275A1EB1C903782068510C4D7BCD68DBDD45D14C0EFDC` |
| `2003.06717v3` | `A701151163BEB5F45C2695F30658EA0DE903534604D7F717102B3530E21A3D10` |
| `2006.15776v1` | `DC4FE65753E19DA9DD454D97BA7E25B8E45C4F7FE99E7341C78CAD0BD512E2F3` |
| `2607.09619v2` | `379591AA3C1036C9140702EBE71AAAB309FE207439A57DB5CEFF893F15D0AE8E` |

## 11. Décision et expérience décisive suivante

**Résultat scientifique positif :** reclasser le maillon « ancienne
exactement BSS + uniforme faible-(L^3) → zéro » en **classique publié**,
avec Guevara--Phuc comme raccord faible principal et Chae--Wolf comme
confirmation Lorentz lisse.

**Résultat négatif :** abandonner toute stratégie qui prétend déduire BSS ou
DSS de la seule précompacité/récurrence faible de l'orbite renormalisée. Trois
obstacles indépendants sont identifiés : absence de tightness forte, absence
d'unicité dans la classe adaptée, absence de fonctionnelle rendant les orbites
récurrentes stationnaires ou périodiques.

**Lemme falsifiable à viser :** sous une hypothèse additionnelle produite par
la PDE et strictement plus forte que la récurrence faible, montrer soit

\[
 \|\partial_sV(s_n)\|_X\longrightarrow0                    \tag{16}
\]

dans un espace (X) assez fort pour passer à la limite dans (4), soit une
contraction stricte sur une période. Le test adverse minimal doit être mené
sur des orbites divergence-free translatées et multi-échelles, uniformément
bornées dans (L^{3,\infty}), afin de vérifier que l'hypothèse proposée ne
réintroduit ni tightness ni Type I de façon cachée. Si (16) donne une limite
stationnaire (U\in W^{1,2}_{\rm loc}\cap L^{3,\infty}), la rigidité finale
est désormais disponible par Guevara--Phuc; c'est la production de (16), et
non le Liouville du profil BSS, qui est le verrou actif.
