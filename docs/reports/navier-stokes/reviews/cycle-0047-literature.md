# Cycle 0047 — de la limite renormalisée à une ancienne admissible : héritages et rigidité

**Date de coupure :** 15 août 2026

**Nature :** audit bibliographique primaire contradictoire indépendant

**Objet borné :** contrôler le changement de variables auto-similaires,
séparer les notions de solution anciennes et déterminer exactement quelles
propriétés la limite conditionnelle du cycle 0046 peut hériter.

Le modèle cible est toujours Navier--Stokes incompressible non forcé,
viscosité un, sur \(\mathbb R^3\) :

\[
 \partial_tu-\Delta u+(u\cdot\nabla)u+\nabla p=0,
 \qquad \nabla\cdot u=0.                                  \tag{1}
\]

## Verdict

**Réconciliation avec la dérivation principale.** Le zoom à rayon constant
de (2) est un contrôle bibliographique, pas la transformation réellement
requise après le cycle 0046 : celle-ci conserve le drift parce que son rayon
varie dans le temps. Le rapport principal du cycle 0047 calcule séparément
son inverse exact. De même, l'héritage de la pression de Riesz, seulement
conditionnel dans le présent audit, est fermé dans la branche réelle par une
extraction faible-étoile globale du produit, en plus de la convergence
locale. Ces deux raccords restent des dérivations internes.

1. **Le zoom du cycle 0046 produit directement une solution ancienne
   standard.** Pour

   \[
   U_n(y,s)=r_nu(x^*+r_ny,T^*+r_n^2s),\qquad r_n\downarrow0, \tag{2}
   \]

   les domaines temporels tendent vers \(( -\infty,0)\) et (1) est
   exactement invariant. Si les termes de l'équation convergent sur tout
   compact, la limite résout (1) en variables \((y,s)\). Aucun ansatz
   auto-similaire n'est nécessaire.

2. **Le changement de Leray est une opération différente.** Une solution
   \(V(y,\tau)\) de l'équation renormalisée se transforme en solution
   ancienne standard par

   \[
   u(x,t)=(-t)^{-1/2}V\!\left(\frac{x}{\sqrt{-t}},-log(-t)\right),
   \quad
   p(x,t)=(-t)^{-1}P\!\left(\frac{x}{\sqrt{-t}},-log(-t)\right). \tag{3}
   \]

   Stationnarité de \(V\) signifie auto-similarité exacte; périodicité en
   \(\tau\) signifie auto-similarité discrète. Une limite ancienne générale
   issue de (2) n'est ni stationnaire ni périodique dans ces variables.

3. **Sous la porte forte \(L^3_{\rm loc}\) et la stabilité de l'énergie
   locale, la limite du cycle 0046 peut être ancienne, adaptée et non nulle.**
   C'est le maximum actuellement justifié. La concentration intégrée du
   cycle 0046 assure \(U\not\equiv0\), mais ne donne ni singularité au temps
   terminal, ni trace terminale forte.

4. **Ne sont pas hérités automatiquement :** pression globale de Riesz,
   énergie globale, décroissance spatiale, classe d'énergie locale au sens
   global, mildness, bornitude, auto-similarité et singularité terminale.
   Chacune exige une porte distincte.

5. **Aucun théorème de rigidité publié ne ferme la classe obtenue.** Les
   résultats disponibles concernent \(L^3\) fort, les profils exactement
   auto-similaires, les anciennes mild bornées, l'axisymétrie, une donnée
   terminale prescrite ou des solutions stationnaires décroissantes. Le
   Liouville 3D général demeure ouvert, même dans des classes plus fortes que
   la limite adaptée actuellement accessible.

6. **La veille 2025--2026 ne change pas ce verdict.** Pineau--Vicol traite
   des profils tournés structurés, Seregin des scénarios Type II à limite
   Euler, Barker des données approximativement axisymétriques et Wang--Yang
   des solutions stationnaires. Aucun résultat récent ne rigidifie une
   ancienne adaptée 3D générale sous seule borne
   \(L^\infty_tL^{3,\infty}_x\).

## 1. Transformation auto-similaire inverse

### 1.1 Calcul exact

Pour \(t<0\), posons

\[
 y=\frac{x}{\sqrt{-t}},\qquad \tau=-\log(-t),
 \qquad
 u(x,t)=(-t)^{-1/2}V(y,\tau),\quad p(x,t)=(-t)^{-1}P(y,\tau). \tag{4}
\]

Un calcul direct donne

\[
 \partial_\tau V-\Delta V+\frac12V+\frac12(y\cdot\nabla)V
 +(V\cdot\nabla)V+\nabla P=0,
 \qquad \nabla\cdot V=0.                                  \tag{5}
\]

Réciproquement, toute paire distributionnelle satisfaisant (5), avec les
intégrabilités permettant les changements de variables, donne par (4) une
paire distributionnelle de (1) sur \(\mathbb R^3\times(-\infty,0)\).

Les lois d'échelle critiques sont exactes :

\[
 \|u(t)\|_{L^3}=\|V(\tau)\|_{L^3},\qquad
 \|u(t)\|_{L^{3,\infty}}=\|V(\tau)\|_{L^{3,\infty}}.       \tag{6}
\]

Une constante ajoutée à \(P(\cdot,\tau)\) devient une fonction du temps
ajoutée à \(p\); c'est une jauge admissible. En revanche, une composante
harmonique affine de pression peut porter une accélération spatiale uniforme
et n'est pas supprimée par une simple jauge temporelle.

Le signe des termes de dérive est important. Jia--Šverák utilisent pour les
solutions **forward** l'ansatz \(t^{-1/2}V(x/\sqrt t)\), qui donne les signes
opposés \(-V/2-(y\cdot\nabla)V/2\). Pineau--Vicol écrivent explicitement le
système backward (4)--(5) dans
[`arXiv:2607.09619v2`](https://arxiv.org/abs/2607.09619v2).

### 1.2 Stationnaire, périodique ou général

- Si \(V\) ne dépend pas de \(\tau\), (4) est une solution backward
  auto-similaire et le profil satisfait le système stationnaire de Leray.
- Si \(V(\tau+L)=V(\tau)\), (4) est discrètement auto-similaire, avec facteur
  de scaling \(\lambda=e^{L/2}\), à l'orientation de période près.
- Sans l'une de ces identités, (4) n'est qu'une réécriture d'une solution
  ancienne générale. Les théorèmes sur les profils stationnaires ou
  périodiques ne s'appliquent pas.

Le changement (4) ne crée pas la suitable-ness. L'inégalité d'énergie locale
se transporte si elle est supposée dans l'une des formulations et si les
fonctions test sont transformées avec tous les termes de dérive. Résoudre
seulement (5) au sens distributionnel ne suffit pas à conclure que (4) est
adaptée.

**Statut.** Les formules sont une `STANDARD_DERIVATION` contrôlée contre les
équations publiées de Pineau--Vicol et les formules forward de Jia--Šverák;
elles ne sont pas un nouveau théorème de régularité.

## 2. Notions de solution : dictionnaire source-exact

### 2.1 Solution faible adaptée

Dans Jia--Šverák,
[*Local-in-space estimates near initial time for weak solutions of the
Navier--Stokes equations and forward self-similar solutions*](https://doi.org/10.1007/s00222-013-0468-x),
*Inventiones Mathematicae* **196** (2014), 233--265,
[`arXiv:1204.0529`](https://arxiv.org/abs/1204.0529), une paire adaptée sur un
ouvert parabolique \(O\) possède localement

\[
 u\in L^\infty_tL^2_x\cap L^2_t\dot H^1_x,
 \qquad p\in L^{3/2}_{\rm loc},                            \tag{7}
\]

résout l'équation en distributions et satisfait l'inégalité d'énergie locale
en distributions. Cette notion est locale; elle n'impose ni énergie globale,
ni formule de Riesz globale, ni trace à \(-\infty\).

Le lemme A.2 d'Albritton--Barker,
[*Localised Necessary Conditions for Singularity Formation in the
Navier--Stokes Equations with Curved Boundary*](https://doi.org/10.1016/j.jde.2020.06.009),
*JDE* **269** (2020), 7529--7573,
[`arXiv:1811.00507v2`](https://arxiv.org/abs/1811.00507v2), stabilise cette
notion sous convergence forte \(L^3\) de la vitesse, faible
\(L^{3/2}\) de la pression et contrôle de la géométrie.

### 2.2 Solution d'énergie locale / local Leray

La définition 3.1 de Jia--Šverák demande davantage qu'une paire adaptée
locale. Pour une donnée \(u_0\in L^2_{\rm loc}\), elle exige :

- des bornes d'énergie uniformément locales et de dissipation sur chaque
  échelle finie;
- une condition de disparition spatiale de l'énergie locale intégrée;
- une trace forte \(u(t)\to u_0\) dans \(L^2(K)\) pour tout compact;
- l'équation distributionnelle et l'inégalité d'énergie locale.

La pression est alors développée localement comme somme d'un terme singulier
proche et d'un terme lointain où la différence de noyaux décroît comme
\(|y|^{-4}\), plus une fonction du temps. Cette soustraction non locale est
essentielle.

Ainsi, “adaptée sur chaque compact” n'implique pas automatiquement “solution
d'énergie locale” : les bornes uniformes en centre, la cohérence de trace,
la condition à l'infini et la formule de pression doivent encore être
transmises.

### 2.3 Solution faible \(L^{3,\infty}\) de Barker--Seregin--Šverák

Dans l'article publié
[*On Stability of Weak Navier--Stokes Solutions with Large
\(L^{3,\infty}\) Initial Data*](https://doi.org/10.1080/03605302.2018.1449219),
*CPDE* **43** (2018), 628--651, la définition 1.1 impose sur une fenêtre
forward

\[
 v=S(t)u_0+u,\qquad
 u\in L^\infty_tL^2_x\cap L^2_t\dot H^1_x,                \tag{8}
\]

avec continuité faible \(L^2\), trace forte nulle du correcteur, inégalité
d'énergie globale perturbée, pression locale \(L^{3/2}\) et inégalité
d'énergie locale. La prépublication
[`arXiv:1603.03211v1`](https://arxiv.org/abs/1603.03211v1) porte un autre
titre et ne liste que Barker et Seregin; les métadonnées publiées ajoutent
Šverák.

Ce n'est pas la simple propriété
\(v\in L^\infty_tL^{3,\infty}_x\). La scission calorique et le correcteur
énergétique font partie de la notion. Pour une solution ancienne, il faudrait
construire des scissions compatibles lorsque le temps initial recule vers
\(-\infty\); le théorème forward 1.3 ne fournit pas seul cette cohérence.

### 2.4 Solution mild ancienne

Koch--Nadirashvili--Seregin--Šverák (KNSS),
[*Liouville Theorems for the Navier--Stokes Equations and Applications*](https://doi.org/10.1007/s11511-009-0039-6),
*Acta Mathematica* **203** (2009), 83--105,
[`arXiv:0709.3599v1`](https://arxiv.org/abs/0709.3599), définit d'abord une
solution mild bornée par la formule d'Oseen/Leray

\[
 u(t)=e^{(t-s)\Delta}u(s)
 -\int_s^t e^{(t-r)\Delta}\mathbb P\operatorname{div}
 (u\otimes u)(r)\,dr.                                     \tag{9}
\]

La définition n'emploie pas la pression. Leur ancienne mild bornée est une
solution pour laquelle il existe \(T_j\downarrow-\infty\) telle que la formule
mild reparte de \(u(T_j)\) sur chaque \((T_j,0)\). Le lemme 6.1 stabilise
cette classe sous convergence locale uniforme de solutions mild uniformément
bornées.

Une ancienne faible bornée peut contenir les parasites

\[
 u(x,t)=b(t),\qquad p(x,t)=-b'(t)\cdot x.                  \tag{10}
\]

KNSS souligne qu'une ancienne mild de cette forme doit au contraire être
constante en temps. Mildness est donc une condition de jauge dynamique, pas
une simple amélioration de régularité locale.

## 3. Pression de Riesz : porte globale distincte

Si, pour presque tout temps,

\[
 U(t)\in L^{3,\infty}(\mathbb R^3),                       \tag{11}
\]

alors \(U_iU_j\in L^{3/2,\infty}\) et la bornitude des
Calderón--Zygmund sur les espaces de Lorentz permet de définir

\[
 P_R=R_iR_j(U_iU_j)\in L^{3/2,\infty}(\mathbb R^3),        \tag{12}
\]

à un signe dépendant de la convention de \(-\Delta\). Cette construction
est globale et fixe une classe de pression modulo fonction du temps.

Mais la forte convergence \(L^3_{\rm loc}\) du cycle 0046 ne suffit pas à
elle seule pour transmettre (12) : l'opérateur est non local et le produit
doit converger avec un contrôle des queues. Une voie suffisante serait :

- borne globale uniforme \(L^{3,\infty}\) de \(U_n\);
- convergence faible-étoile globale du produit dans
  \(L^{3/2,\infty}\), identifiée à \(U\otimes U\) par la forte convergence
  locale;
- pressions de départ toutes normalisées par la même formule de Riesz.

Sans ces trois points, la limite de pressions locales peut conserver une
partie harmonique. L'exemple (10) montre pourquoi l'équation projetée ou la
vorticité ne fixe pas à elle seule la pression affine parasite.

**Conclusion.** La pression de Riesz n'est pas héritée par le seul lemme de
non-trivialité du cycle 0046. Elle devient une `STANDARD_DERIVATION`
conditionnelle si le contrôle global précédent est démontré.

## 4. Matrice d'héritage de la limite du cycle 0046

On suppose seulement le cadre réellement établi au cycle précédent :
concentration Barker--Prange à tout temps tardif et, conditionnellement,
convergence forte \(L^3_{\rm loc}\) sur les bandes
\([-b,-a]\Subset(-\infty,0)\).

| propriété | héritée ? | porte exacte |
|---|---|---|
| équation projetée, divergence nulle | oui conditionnellement | convergence du produit local contre tests solénoïdaux |
| domaine ancien \(\mathbb R^3\times(-\infty,0)\) | oui | extraction diagonale sur les domaines croissants |
| non-trivialité | oui sous forte \(L^3\) | minoration intégrée du cycle 0046 |
| paire faible adaptée | oui si A.2 s'applique | forte \(L^3\), pression faible \(L^{3/2}\), énergie locale stable |
| borne \(L^\infty_tL^{3,\infty}_x\) | oui seulement si supposée uniformément avant zoom | extraction faible-étoile; identification avec la limite locale, pour p.p. temps |
| pression globale de Riesz | non automatique | normalisation globale et contrôle des queues du produit |
| énergie globale Leray--Hopf | non | \(\|U_n(s)\|_2^2=r_n^{-1}\|u(T^*+r_n^2s)\|_2^2\), donc borne dégénérante |
| solution d'énergie locale globale | non automatique | bornes uloc uniformes en centre, trace et decay à l'infini |
| décroissance spatiale | non | \(L^{3,\infty}\) n'a pas de norme de queue absolument continue |
| mildness | non | formule (9), trace de redémarrage et exclusion du mode harmonique |
| bornitude \(L^\infty_{x,t}\) | non | aucune estimation générale depuis faible-\(L^3\) en 3D |
| auto-similarité ou périodicité | non | aucune identité de scaling du profil limite n'est produite |
| trace terminale à \(s=0\) | non | la compacité espace-temps évite précisément cette tranche |
| singularité terminale | non | A.5 exige explosion \(L^\infty\) persistante; absente ici |

Deux pertes méritent une formulation explicite.

### 4.1 Énergie globale

Sous (2),

\[
 \|U_n(s)\|_{L^2(\mathbb R^3)}^2
 =r_n^{-1}\|u(T^*+r_n^2s)\|_{L^2(\mathbb R^3)}^2.          \tag{13}
\]

L'inégalité d'énergie Clay donne donc une borne qui explose comme
\(r_n^{-1}\). Elle peut produire des bornes locales après localisation, mais
pas une énergie globale uniforme de la limite.

### 4.2 Décroissance spatiale

Une fonction dans \(L^{3,\infty}\) a des ensembles de superniveau de mesure
finie, mais il peut exister des pics critiques arbitrairement loin. En général

\[
 \|U\mathbf1_{|x|>R}\|_{L^{3,\infty}}\not\longrightarrow0. \tag{14}
\]

La translation de paquets fournit aussi des suites de norme constante qui
convergent localement vers zéro. Ni le decay pointwise, ni l'intégrabilité
\(L^3\), ni une asymptotique \(C/|x|\) ne sont hérités.

## 5. Théorèmes de rigidité disponibles

### 5.1 Auto-similarité backward exacte

- Nečas--Růžička--Šverák,
  [*On Leray's Self-Similar Solutions of the Navier--Stokes
  Equations*](https://doi.org/10.1007/BF02551584), *Acta Math.* **176**
  (1996), 283--294 : un profil backward exact dans \(L^3(\mathbb R^3)\) est
  trivial.
- Tsai,
  [*On Leray's Self-Similar Solutions of the Navier--Stokes Equations
  Satisfying Local Energy Estimates*](https://doi.org/10.1007/s002050050099),
  *ARMA* **143** (1998), 29--51 : étend l'exclusion à la classe
  auto-similaire satisfaisant les estimations locales d'énergie de l'article.

Ces théorèmes exigent l'ansatz stationnaire de (5). Ils ne s'appliquent pas à
une ancienne générale issue de (2). Exclure ces profils ne suffit donc pas à
exclure tout blow-up.

### 5.2 Endpoint fort et backward uniqueness

Escauriaza--Seregin--Šverák,
[*\(L_{3,\infty}\)-solutions of Navier--Stokes Equations and Backward
Uniqueness*](https://doi.org/10.1070/RM2003v058n02ABEH000609), *Russian
Math. Surveys* **58** (2003), 211--250, exclut un blow-up sous
\(u\in L^\infty_tL^3_x\). La notation historique \(L_{3,\infty}\) désigne
ici la norme mixte forte \(L^\infty_tL^3_x\), pas le Lorentz spatial
\(L^{3,\infty}\).

L'argument produit une trace terminale adaptée à la backward uniqueness et
un contrôle de vorticité. La limite du cycle 0046 n'hérite ni \(L^3\) global,
ni trace terminale nulle. Ce théorème ne ferme donc pas sa classe.

### 5.3 Anciennes mild bornées

KNSS prouve :

- en dimension deux, une ancienne faible bornée est de la forme \(b(t)\), et
  une ancienne mild bornée est constante;
- en dimension trois axisymétrique sans swirl, une ancienne faible bornée est
  de la forme \((0,0,b_3(t))\);
- sous axisymétrie et \(|u(x,t)|\le C/r\), une ancienne faible bornée est
  nulle.

KNSS écrit explicitement que le Liouville 3D général est hors de portée et
était même ouvert pour les solutions stationnaires bornées. Leur proposition
6.1 extrait une ancienne mild bornée non nulle d'un zoom normalisé au maximum,
mais ce mécanisme exige une borne \(L^\infty\) et une convergence uniforme,
absentes du cycle 0046.

Lei--Yang--Yuan,
[*Backward Uniqueness for 3D Navier--Stokes Equations With Non-Trivial Final
Data and Applications*](https://doi.org/10.1093/imrn/rnae208), *IMRN* 2024,
13417--13431, [`arXiv:2311.02429v1`](https://arxiv.org/abs/2311.02429), donne
l'unicité de deux solutions mild bornées, de vorticités bornées, ayant la
même donnée finale. Là encore, mildness, bornitude et donnée finale ne sont
pas héritées.

### 5.4 Axisymétrie et faible-\(L^3\)

Ożański--Palasek,
[*Quantitative Control of Solutions to the Axisymmetric Navier--Stokes
Equations in Terms of the Weak \(L^3\) Norm*](https://doi.org/10.1007/s40818-023-00156-7),
*Annals of PDE* **9** (2023), article 15,
[`arXiv:2210.10030v3`](https://arxiv.org/abs/2210.10030v3), prouve pour une
solution classique axisymétrique

\[
 \|\nabla^ju(t)\|_\infty
 \le t^{-(1+j)/2}\exp\!\exp(A^{O_j(1)})                 \tag{15}
\]

sous borne \(L^\infty_tL^{3,\infty}_x\le A\). En redémarrant une ancienne
axisymétrique arbitrairement loin dans le passé, le facteur temporel de (15)
tend vers zéro; l'article en déduit l'absence d'ancienne axisymétrique non
triviale dans cette classe.

L'axisymétrie exacte doit passer au zoom. Aucune approximation quantitative
d'un axe ne suffit à invoquer ce résultat.

### 5.5 Profils tournés récents et stationnaire

Pineau--Vicol 2026 exclut les profils backward auto-similaires tournés sous
borne Type I lorsque la vitesse de rotation est suffisamment petite ou
grande; le cas discrètement auto-similaire ajoute un facteur proche de un.
Leur critère local à une tranche suppose explicitement une proximité
auto-similaire. Ces hypothèses ne viennent pas du cycle 0046.

Wang--Yang,
[`arXiv:2608.06040v1`](https://arxiv.org/abs/2608.06040v1),
*New Decay Estimates and Liouville Type Theorems for the 3D Axisymmetric
Stationary Navier--Stokes Equations*, 6 août 2026, concerne des
\(D\)-solutions stationnaires avec Dirichlet fini et enveloppes de
décroissance cylindrique, dont un gain logarithmique. L'article indique que
le problème stationnaire général reste ouvert. Stationnarité, Dirichlet fini
et decay ne sont pas hérités par (2).

## 6. Veille différentielle 2025--2026

La recherche primaire au 15 août 2026 a contrôlé les versions suivantes :

- Seregin, [`arXiv:2507.08733v2`](https://arxiv.org/abs/2507.08733v2) et
  [`arXiv:2606.29468v1`](https://arxiv.org/abs/2606.29468v1) : scénarios
  Type II conditionnels, scaling Euler et anciennes Euler; aucun Liouville
  pour l'ancienne NS adaptée du cycle 0046;
- Barker, [`arXiv:2510.20757v3`](https://arxiv.org/abs/2510.20757v3) :
  classification quantitative sous données approximativement
  axisymétriques et hypothèses de taux;
- Pineau--Vicol, [`arXiv:2607.09619v2`](https://arxiv.org/abs/2607.09619v2) :
  RSS/RDSS structurées et critère local de proximité auto-similaire;
- Yu, [`arXiv:2606.12756v1`](https://arxiv.org/abs/2606.12756v1) : réduction
  de cascades de défaut explicitement conditionnelle;
- Wang--Yang, [`arXiv:2608.06040v1`](https://arxiv.org/abs/2608.06040v1) :
  rigidité stationnaire sous decay;
- Cheskidov--Dai--Palasek,
  [`arXiv:2511.09556v2`](https://arxiv.org/abs/2511.09556v2) : constructions
  de blow-up/non-unicité instantanés dans une classe périodique hors contrôle
  Leray--Hopf près du temps concerné; aucun transfert à la limite admissible
  ici.

**Résultat de veille.** Aucun résultat primaire 2025--2026 vérifié n'établit

\[
 \left.
 \begin{array}{c}
 U\text{ ancienne adaptée sur }\mathbb R^3,\\
 \sup_{s<0}\|U(s)\|_{L^{3,\infty}}<\infty
 \end{array}
 \right\}
 \Longrightarrow U\equiv0.                                \tag{16}
\]

## 7. Passe contradictoire

### A. Appliquer NRS/Tsai sans auto-similarité

La concentration de Barker--Prange respecte l'échelle parabolique mais
n'impose aucune égalité entre deux échelles. Dans les variables (5), la
limite peut dépendre arbitrairement de \(\tau\). Les théorèmes stationnaires
ne s'appliquent pas.

### B. Confondre adaptée et mild

Le couple parasite (10) est lisse et localement adapté mais sa dynamique
n'est pas mild sauf si \(b\) est constante. Une inégalité d'énergie locale ne
fixe donc pas la jauge globale nécessaire à KNSS.

### C. Déduire la pression de Riesz de la convergence locale

Deux suites identiques sur tout compact croissant peuvent différer loin à
l'infini; leur pression locale diffère par un champ harmonique. Sans contrôle
de queue et normalisation commune, (12) ne passe pas.

### D. Utiliser l'énergie Clay après zoom

Le facteur \(r_n^{-1}\) dans (13) détruit toute borne globale uniforme. Une
limite localement énergétique peut avoir énergie totale infinie.

### E. Déduire decay de faible-\(L^3\)

La quasi-norme endpoint n'est pas absolument continue sur les queues. Des
paquets critiques disjoints et éloignés réfutent toute implication uniforme
vers (14).

### F. Importer la singularité terminale

La minoration intégrée prouve seulement \(U\not\equiv0\) pour des temps
négatifs. Une ancienne lisse non nulle satisfait cette conclusion. La
proposition A.5 d'Albritton--Barker ou la normalisation ponctuelle Hölder
reste nécessaire pour transmettre une singularité ou une valeur au sommet.

## 8. Source nouvelle retenue après synthèse

Albritton--Barker, *On Local Type I Singularities of the Navier--Stokes
Equations and Liouville Theorems*, JMFM 21:43 (2019),
`arXiv:1811.00502`, est ajouté comme `NS-SRC-0189`. Il ne faut pas le
confondre avec leur article JDE 2020 `arXiv:1811.00507v2`, déjà `0187`.
Le théorème 1.1 impose une ancienne **mild bornée** avec décroissance Type I;
le théorème 1.2 impose la mildness et une borne (L^3) forte le long d'une
suite de temps reculant vers (-\infty). Aucun des deux ne couvre la seule
classe adaptée faible-(L^3) de ce cycle.

## 9. Empreintes des PDF audités

| PDF primaire | octets | SHA256 |
|---|---:|---|
| `https://arxiv.org/pdf/0709.3599` | 279554 | `EE4444837EAF72A0298F2032BE63A93C5DE41B61784BB1A68AE1E3E8973F14D8` |
| `https://arxiv.org/pdf/1204.0529` | 304378 | `1E8685FBE09C669854357278010F345FA5C98845C5888BA6720936A0B3F1591F` |
| `https://arxiv.org/pdf/1603.03211v1` | 266074 | `ADEACBBB2E18A2E4C2C29E057AEA8B7293949602066F68AC0BCD8C999A1003A2` |
| `https://arxiv.org/pdf/1811.00507v2` | 476336 | `FDD91E657B5CF503286B4E45CC084C12C8B202AAF24BCDAD67EDEA46EDFA4102` |
| `https://arxiv.org/pdf/2210.10030v3` | 740077 | `2D64D4FF35D9AB144F54320F0E80281FF95454749E08C05D03F9C7D23ED0594B` |
| `https://arxiv.org/pdf/2607.09619v2` | 617825 | `379591AA3C1036C9140702EBE71AAAB309FE207439A57DB5CEFF893F15D0AE8E` |
| `https://arxiv.org/pdf/2608.06040v1` | 507806 | `CBB95814EE44689142303B7ECF46199F79413AE08FE8DBD148EFA4EE2D2C3918` |

## Conclusion opérationnelle

Le cycle 0046 ouvre une route de compacité--rigidité plus précise, mais pas
encore fermée :

\[
 \boxed{
 \text{forte }L^3_{\rm loc}+\text{pression/énergie adaptées}
 \Longrightarrow
 \text{ancienne adaptée non nulle}.}
\]

Pour atteindre un théorème de rigidité publié, il faut ensuite obtenir au
moins une des promotions suivantes :

1. auto-similarité stationnaire/périodique avec les intégrabilités NRS/Tsai;
2. \(L^3\) global fort et trace terminale de type ESS;
3. mildness, bornitude et donnée terminale pour KNSS/Lei--Yang--Yuan;
4. axisymétrie exacte et borne faible-\(L^3\) pour Ożański--Palasek.

Aucune de ces promotions n'est contenue dans la concentration intégrée. Le
prochain lemme bibliographiquement minimal est donc un **raccord de classe**,
non un nouveau Liouville : montrer que la suite réelle possède une pression
globalement normalisée et soit une formule mild compatible sur chaque bande
ancienne, soit une structure géométrique rigide qui passe à la limite. Sans
ce raccord, invoquer un théorème de profil ou de backward uniqueness serait
un changement silencieux de notion de solution.
