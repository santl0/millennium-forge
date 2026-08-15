# Cycle 0048 — audit primaire de l'endpoint faible-\(L^3\)

**Date de coupure :** 15 août 2026

**Nature :** audit bibliographique primaire contradictoire indépendant

**Objet borné :** vérifier ce que démontrent exactement Barker--Seregin--
Šverák (BSS), Yamazaki, Koch--Nadirashvili--Seregin--Šverák (KNSS) et
Albritton--Barker à propos des solutions faible-\(L^3\), de la formulation
intégrale endpoint, de la continuité temporelle et de l'unicité.

L'équation cible de cet audit est Navier--Stokes incompressible, non forcé,
de viscosité un, dans l'espace entier :

\[
 \partial_t v-\Delta v+(v\cdot\nabla)v+\nabla q=0,
 \qquad \nabla\cdot v=0,
 \qquad (x,t)\in\mathbb R^3\times I.                       \tag{1}
\]

## Verdict

1. **La classe BSS n'est pas la classe
   \(L^\infty_tL^{3,\infty}_x\).** Dans la définition 1.1 publiée, la
   donnée initiale est dans \(L^{3,\infty}\), mais la solution est scindée
   en

   \[
    v(t)=e^{t\Delta}u_0+u(t),\qquad
    u\in L^\infty_tL^2_x\cap L^2_t\dot H^1_x,              \tag{2}
   \]

   avec trace énergétique, inégalités d'énergie globale perturbée et
   locale. Rien dans cette définition n'impose
   \(v\in L^\infty_tL^{3,\infty}_x\). Réciproquement, une borne uniforme
   faible-\(L^3\) ne produit pas la scission énergétique BSS.

2. **L'opérateur bilinéaire endpoint existe au sens faible-étoile.** Le
   lemme d'interpolation de Yamazaki donne, contre le prédual
   \(L^{3/2,1}_\sigma\), une intégrabilité temporelle qui manque à
   l'estimation ponctuelle naïve. Il permet de définir

   \[
    \mathcal B(a,b)(t)=
    -\int e^{(t-s)\Delta}\mathbb P\operatorname{div}
      (a\otimes b)(s)\,ds                                  \tag{3}
   \]

   comme intégrale de Gelfand dans \(L^{3,\infty}_\sigma\), et donne

   \[
    \|\mathcal B(a,b)\|_{L^\infty_tL^{3,\infty}_x}
    \le C\|a\|_{L^\infty_tL^{3,\infty}_x}
           \|b\|_{L^\infty_tL^{3,\infty}_x}.               \tag{4}
   \]

   Ce n'est généralement pas une intégrale de Bochner en norme
   \(L^{3,\infty}\). La constante de (4) ne contient aucun petit facteur
   de longueur de l'intervalle.

3. **Bornitude bilinéaire ne signifie pas continuité quadratique
   faible-étoile.** La multiplication n'est pas séquentiellement continue
   pour la topologie faible-étoile de \(L^{3,\infty}\). Le théorème de
   stabilité BSS compense précisément cette difficulté par une compacité
   forte locale du correcteur; il ne peut pas être remplacé par le seul
   passage faible-étoile dans (3).

4. **La continuité faible-étoile dérivée au cycle 0048 est strictement plus
   faible que la mildness publiée.** La conclusion interne

   \[
    v\in C_{w^*}(I;L^{3,\infty}_\sigma)
    \quad\text{et Duhamel au sens de Gelfand}                \tag{5}
   \]

   est compatible avec les estimations de Yamazaki. Les définitions mild
   utilisées par Yamazaki et reprises par Taniuchi demandent une continuité
   temporelle **en norme** (\(C\), \(BC\) ou \(BUC\), selon la fenêtre),
   en plus de l'identité duale. La littérature auditée ne fournit pas

   \[
    C_{w^*}(I;L^{3,\infty})
    \Longrightarrow C(I;L^{3,\infty}).                     \tag{6}
   \]

5. **Petites données : existence et unicité; grandes données : existence
   BSS, sans conclusion générale d'unicité ou de non-unicité.** La
   petitesse ferme une contraction grâce à (4). À grande norme, BSS
   construit des solutions globales scindées et démontre une stabilité
   subséquentielle; l'article ne démontre ni unicité inconditionnelle ni
   non-unicité dans cette classe.

6. **Aucun raccord automatique vers KNSS ou Albritton--Barker.** Les
   solutions anciennes de KNSS et celles intervenant dans le théorème Type I
   d'Albritton--Barker sont **mild et bornées dans l'espace**. Une ancienne
   seulement dans \(C_{w^*}L^{3,\infty}\), même munie de (3), n'est pas
   bornée et ne satisfait pas leur définition sans un lemme supplémentaire.

7. **La veille primaire 2025--2026 ne ferme aucun de ces écarts.** Aucun
   résultat primaire identifié ne transforme une trajectoire distributionnelle
   uniformément faible-\(L^3\) en solution mild forte, BSS ou KNSS, et aucun
   ne démontre la non-unicité dans la classe BSS.

## 1. Barker--Seregin--Šverák : énoncés exacts

### 1.1 Version et statut

La source publiée est H. Barker, G. Seregin et V. Šverák,
[*On Stability of Weak Navier--Stokes Solutions with Large
\(L^{3,\infty}\) Initial Data*](https://doi.org/10.1080/03605302.2018.1449219),
*Communications in Partial Differential Equations* **43** (2018), 628--651.
La prépublication primaire
[`arXiv:1603.03211v1`](https://arxiv.org/abs/1603.03211v1) porte le titre
*On global solutions to the Navier--Stokes equations with large
\(L^{3,\infty}\) initial data* et ne liste que Barker et Seregin. Les
métadonnées de la version publiée, son titre et sa liste d'auteurs doivent
donc être privilégiés pour `NS-SRC-0188`.

Équation : (1) sur \(\mathbb R^3\times(0,\infty)\), sans force, viscosité
un, donnée initiale solénoïdale \(u_0\in L^{3,\infty}(\mathbb R^3)\). Il
n'y a ni frontière ni condition au bord.

### 1.2 Définition 1.1 : la scission fait partie de la notion

Avec \(V(t)=e^{t\Delta}u_0\), une solution faible globale BSS est écrite
\(v=V+u\), où

\[
 u\in L^\infty(0,T;J)\cap L^2(0,T;\dot J^1_2)             \tag{7}
\]

pour tout \(T>0\). Elle doit en outre satisfaire :

- l'équation perturbée en distributions et
  \(q\in L^{3/2}_{\rm loc}\);
- la continuité temporelle faible du correcteur dans \(L^2\), puis la trace
  forte \(\|u(t)\|_2\to0\) au temps initial;
- l'inégalité globale d'énergie perturbée

  \[
   \|u(t)\|_2^2+2\int_0^t\|\nabla u\|_2^2
   \le 2\int_0^t\!\int_{\mathbb R^3}
        (V\otimes u+V\otimes V):\nabla u;                   \tag{8}
  \]

- l'inégalité locale d'énergie pour la paire complète \((v,q)\).

La pression BSS est locale, dans \(L^{3/2}_{\rm loc}\); la définition
n'impose pas la jauge globale de Riesz. Le correcteur (7) appartient par
interpolation à des espaces sous-critiques, par exemple
\(L^4_tL^3_x\), mais cela ne donne pas une borne
\(L^\infty_tL^{3,\infty}_x\) pour \(u\) ou \(v\).

**Transfert valide :** (7)--(8) définit une classe globale adaptée et
énergétique pour une donnée faible-\(L^3\).

**Transfert invalide :** appeler toute solution satisfaisant seulement
\(v\in L^\infty_tL^{3,\infty}_x\) une « solution faible BSS ».

### 1.3 Théorème 1.3 : stabilité subséquentielle, pas flot continu

Si \(u_0^{(k)}\rightharpoonup^*u_0\) dans \(L^{3,\infty}\) et si
\(v^{(k)}=e^{t\Delta}u_0^{(k)}+u^{(k)}\) sont des solutions globales BSS,
alors une sous-suite converge en distributions vers une solution globale
BSS issue de \(u_0\).

Les portes de passage au terme quadratique sont plus fortes que la seule
convergence faible-étoile des données : sur chaque cylindre compact, la
preuve extrait notamment

\[
 u^{(k)}\to u
 \quad\text{dans }C([0,n];L^{9/8}(B_n))
 \quad\text{et dans }L^s_{\rm loc},\ 1<s<10/3.             \tag{9}
\]

En particulier, le passage fort local en \(L^3\) contrôle le produit. Les
termes énergétiques passent par semi-continuité faible et les pressions par
les bornes locales correspondantes.

Le quantificateur exact est

\[
 \text{toute suite de solutions}\ \Longrightarrow\
 \text{il existe une sous-suite et une solution limite}.  \tag{10}
\]

Ce n'est ni un opérateur solution univoque, ni la continuité faible-étoile
d'un flot, ni une convergence de la trajectoire complète dans
\(C_{w^*}L^{3,\infty}\).

### 1.4 Continuité du semi-groupe et unicité conditionnelle

La proposition 2.4 distingue deux topologies :

- \(e^{t\Delta}u_0\rightharpoonup^*u_0\) dans
  \(L^{3,\infty}\) pour toute donnée;
- la convergence en norme faible-\(L^3\) au temps zéro est obtenue sur le
  sous-espace fermé engendré par les champs solénoïdaux lisses et compacts,
  pas sur tout \(L^{3,\infty}\). Une donnée homogène de degré \(-1\) fournit
  l'obstruction d'échelle classique.

La proposition 2.5 ne donne que la convergence distributionnelle des flots
de chaleur lorsque les données convergent faible-étoile.

Les résultats d'unicité de l'article gardent une porte supplémentaire :

- le théorème 1.5 impose une petitesse locale uniforme et la proximité
  \(\|v(t)-u_0\|_{3,\infty}<\varepsilon_0\);
- le corollaire 1.6 donne l'unicité si une solution BSS appartient déjà à
  \(C([0,T];L^{3,\infty})\);
- le théorème 1.7 traite la condition Kato
  \(\sup_{t>0}t^{1/5}\|e^{t\Delta}u_0\|_5\) petite;
- la proposition 1.8 obtient une unicité locale sous petitesse de la queue
  haute de la distribution de \(u_0\).

Aucun de ces énoncés ne donne l'unicité BSS pour toute grande donnée.

## 2. Yamazaki : construction exacte de l'opérateur endpoint

### 2.1 Source et cadre

La source publiée est M. Yamazaki,
[*The Navier--Stokes equations in the weak-\(L^n\) space with
time-dependent external force*](https://doi.org/10.1007/PL00004418),
*Mathematische Annalen* **317** (2000), 635--675. Elle traite
\(n\ge3\), dans \(\mathbb R^n\), le demi-espace et des domaines extérieurs,
avec force dépendant du temps. Le support de cours primaire de l'auteur,
[*Real Interpolation, Lorentz Spaces and the Navier--Stokes
Equation*](https://www.japan-germany.sci.waseda.ac.jp/event/2010yamazakilecture.pdf),
expose les estimations et le point fixe sous une forme directement
contrôlable.

Pour l'espace entier en dimension trois, posons

\[
 X=BUC(\mathbb R;L^{3,\infty}_\sigma),\qquad
 Y=BUC(\mathbb R;L^{3/2,\infty}).                         \tag{11}
\]

La force est écrite \(f=\operatorname{div}F\). L'opérateur linéaire

\[
 \mathcal U F(t)=\int_0^\infty
 e^{-sA}\mathbb P\operatorname{div}F(t-s)\,ds             \tag{12}
\]

ne converge généralement pas comme intégrale de Bochner dans
\(L^{3,\infty}\). Il est défini par dualité faible-étoile.

### 2.2 Estimation intégrée de Yamazaki

Le lemme 6.2 du support de cours donne, en dimension trois,

\[
 \int_0^\infty
 \|\nabla e^{-sA}\phi\|_{L^{3,1}}\,ds
 \le C\|\phi\|_{L^{3/2,1}}.                              \tag{13}
\]

Ici \(L^{3/2,1}_\sigma\) est un prédual de
\(L^{3,\infty}_\sigma\). La dualité de Lorentz et
\(L^{3,\infty}\cdot L^{3,\infty}\subset L^{3/2,\infty}\)
donnent

\[
 \int_s^t
 \left|\left\langle a\otimes b,
 \nabla e^{(t-\tau)\Delta}\mathbb P\phi\right\rangle\right|d\tau
 \le C\|a\|_{L^\infty_tL^{3,\infty}}
        \|b\|_{L^\infty_tL^{3,\infty}}
        \|\phi\|_{L^{3/2,1}}.                            \tag{14}
\]

L'estimation ponctuelle seule serait proportionnelle à
\((t-\tau)^{-1}\) et non intégrable. (13), obtenue par interpolation réelle
à travers les échelles, est donc le maillon endpoint décisif.

### 2.3 Ce que la petitesse fait, et ce qu'elle ne fait pas

Dans le cadre whole-time, Yamazaki pose schématiquement

\[
 T[u](t)=\int_0^\infty e^{-sA}\mathbb P
 \{-\operatorname{div}(u\otimes u)(t-s)
       +\operatorname{div}F(t-s)\}\,ds.                   \tag{15}
\]

Pour des constantes structurelles \(A,C\),

\[
 \|T[u]-T[v]\|_X
 \le AC(\|u\|_X+\|v\|_X)\|u-v\|_X.                     \tag{16}
\]

La petitesse de la force, formulée dans le cours par un seuil du type
\(1/(4C^2A)\), rend une petite boule invariante et contractante. Elle donne
alors une solution petite unique et la continuité du point fixe par rapport
à la force.

Deux conclusions ne suivent pas :

- rétrécir l'intervalle ne fournit pas automatiquement un facteur petit
  dans (14);
- une solution préexistante de grande norme qui satisfait l'identité
  intégrale n'entre pas dans le régime d'unicité de la contraction.

### 2.4 Taniuchi, définition 1 et lemme 7 attribué à Yamazaki

Y. Taniuchi,
[*On uniqueness of mild \(L^{3,\infty}\)-solutions on the whole time axis
to the Navier--Stokes equations in unbounded
domains*](https://doi.org/10.1007/s00208-023-02702-x),
*Mathematische Annalen* **389** (2024), donne une formulation primaire
lisible qui renvoie explicitement à Yamazaki.

Sa définition 1 suppose
\(v\in C(( -\infty,T);L^{3,\infty}_\sigma)\) **en norme** et exige, pour
tous \(s<t\) et \(\phi\in L^{3/2,1}_\sigma\), l'identité duale de Duhamel.
Sous \(F\in L^\infty_tL^{3/2,\infty}_x\) et une borne uniforme de \(v\),
la formule sur \((s,t)\) équivaut à la formule whole-past lorsque la limite
\(s\to-\infty\) est admissible.

Son **lemme 7, explicitement intitulé « Yamazaki [55] »**, contient les deux
bornes endpoint

\[
 \int_s^t |\langle F,\nabla e^{-(t-\tau)A}\phi\rangle|d\tau
 \le C\|F\|_{L^\infty L^{3/2,\infty}}
       \|\phi\|_{L^{3/2,1}},                              \tag{17}
\]

\[
 \int_s^t |\langle u\otimes w,
          \nabla e^{-(t-\tau)A}\phi\rangle|d\tau
 \le C\|u\|_{L^\infty L^{3,\infty}}
       \|w\|_{L^\infty L^{3,\infty}}
       \|\phi\|_{L^{3/2,1}}.                             \tag{18}
\]

Le lemme 8 donne l'unicité de l'équation de différence seulement lorsque la
borne pertinente de \(u+v\) est inférieure à un seuil universel. Le
théorème principal de Taniuchi permet une comparaison plus asymétrique à
l'infini passé, mais ajoute des hypothèses de queue/asymptotiques dans des
espaces \(L^{r,\infty}\), \(r<3\); ce n'est pas une unicité générale à
grande norme faible-\(L^3\).

La numérotation doit être attribuée sans ambiguïté : « lemme 7 » est le
numéro dans l'article de **Taniuchi**, qui crédite Yamazaki [55]; le support
de cours de Yamazaki numérote l'estimation d'interpolation sous-jacente
« lemme 6.2 ». Le verdict mathématique est identique : le lemme 7 contrôle
le terme linéaire forcé et le terme bilinéaire dans le dual
\(L^{3/2,1}\)--\(L^{3,\infty}\), mais n'affirme ni continuité forte de la
trajectoire, ni continuité faible-étoile du produit, ni unicité sans la
petitesse séparée du lemme 8.

## 3. Ledger des continuités et passages à la limite

| Objet | Conclusion vérifiée | Conclusion non vérifiée |
|---|---|---|
| Flot de chaleur sur tout \(L^{3,\infty}\) | faible-étoile au temps zéro | continuité forte au temps zéro |
| Flot de chaleur sur le sous-espace séparable de BSS | continuité forte | extension à tout \(L^{3,\infty}\) |
| Terme bilinéaire endpoint | élément de \(L^{3,\infty}\) par intégrale de Gelfand | intégrale de Bochner en norme |
| Trajectoire du lemme interne 0048 | \(C_{w^*}L^{3,\infty}\) et identité duale | \(CL^{3,\infty}\) en norme |
| Données BSS faible-étoile convergentes | sous-suite de solutions convergeant en distributions | flot solution unique et continu |
| Produits BSS | convergence grâce à (9) | passage par faible-étoile seul |
| Point fixe Yamazaki petit | existence et unicité dans une petite boule | unicité des grandes solutions |

### 3.1 Test adverse : défaut quadratique faible-étoile

Soit \(\varphi\in C_c^\infty(\mathbb R^3)\), choisie de sorte que
\(\mathbb P\operatorname{div}(\varphi^2e_2\otimes e_2)\ne0\), et

\[
 A_n=(0,0,n^{-1}\varphi(x)\cos(nx_1)),\qquad
 u_n=\operatorname{curl}A_n.                              \tag{19}
\]

Alors \(\nabla\cdot u_n=0\) exactement et

\[
 u_n=\big(n^{-1}\partial_2\varphi\cos(nx_1),
 \varphi\sin(nx_1)-n^{-1}\partial_1\varphi\cos(nx_1),0\big).
                                                                    \tag{20}
\]

La suite est uniformément bornée et à support compact; elle converge donc
vers zéro faible-étoile dans \(L^{3,\infty}\), par densité de
\(C_c^\infty\) dans le prédual \(L^{3/2,1}\). En revanche,

\[
 u_n\otimes u_n\rightharpoonup
 \tfrac12\varphi^2 e_2\otimes e_2                         \tag{21}
\]

en distributions. Le terme projeté limite est non nul par le choix de
\(\varphi\). Ainsi, même sur des champs solénoïdaux lisses, compacts et
uniformément bornés,

\[
 u_n\rightharpoonup^*0
 \quad\centernot\Longrightarrow\quad
 \mathcal B(u_n,u_n)\rightharpoonup^*\mathcal B(0,0).      \tag{22}
\]

Ce contre-profil analytique réfute la continuité faible-étoile conjointe de
l'opérateur quadratique sur son espace ambiant. Il ne constitue pas une
suite de solutions de Navier--Stokes; son rôle exact est de montrer pourquoi
l'équation seule doit fournir une compacité supplémentaire avant tout
passage à la limite non linéaire.

## 4. Différence avec KNSS et Albritton--Barker

### 4.1 KNSS : mild bornée n'est pas faible-\(L^3\) endpoint

Koch, Nadirashvili, Seregin et Šverák,
[*Liouville Theorems for the Navier--Stokes Equations and
Applications*](https://doi.org/10.1007/s11511-009-0039-6),
*Acta Mathematica* **203** (2009), 83--105,
[`arXiv:0709.3599`](https://arxiv.org/abs/0709.3599), travaillent avec des
solutions mild **bornées dans l'espace**. Sur une fenêtre \((s,t)\), elles
satisfont la formule d'Oseen/Leray et l'intégrale bilinéaire est contrôlée
dans \(L^\infty_x\) avec un facteur \(C\sqrt{t-s}\).

Une solution ancienne mild KNSS doit être mild à partir d'une suite de temps
\(T_j\downarrow-\infty\). Leur lemme 6.1 stabilise cette classe sous
convergence locale uniforme de solutions mild uniformément bornées.

La distinction n'est pas terminologique. Une solution faible bornée peut
contenir un parasite

\[
 u(x,t)=b(t),\qquad p(x,t)=-b'(t)\cdot x,                  \tag{23}
\]

alors que la formule mild force \(b\) à être constante. KNSS décompose une
solution faible bornée en composantes mild, calorique et parasite plutôt que
d'identifier automatiquement « faible bornée » et « mild bornée ».

Une borne \(L^{3,\infty}_x\) ne donne aucune borne \(L^\infty_x\), et
l'intégrale de Gelfand (3) ne fournit pas la convergence ponctuelle du noyau
d'Oseen demandée dans ce cadre. Le transfert vers KNSS est donc invalide.

### 4.2 Albritton--Barker : l'ancienne du scénario Type I reste mild bornée

La source primaire est D. Albritton et T. Barker,
[*On Local Type I Singularities of the Navier--Stokes
Equations and Liouville Theorems*](https://doi.org/10.1007/s00021-019-0448-z),
*Journal of Mathematical Fluid Mechanics* **21** (2019), article 43,
[`arXiv:1811.00502v2`](https://arxiv.org/abs/1811.00502).

Le théorème 1.1 caractérise l'existence d'un point singulier local Type I par
l'existence d'une solution ancienne non triviale **mild bornée**, avec une
quantité Type I finie. Le théorème 1.2 annule une telle ancienne lorsqu'elle
possède une suite de temps tendant vers \(-\infty\) uniformément bornée en
\(L^3\) fort. Le théorème 3.1 formule des équivalences locales Type I en
\(L^{p,\infty}\), \(3\le p<\infty\), mais la solution ancienne obtenue reste
mild et bornée.

Le théorème 4.1 touche l'endpoint faible-\(L^3\), mais ajoute à l'ancienne
mild une bornitude locale \(L^\infty_x\) sur les bandes de passé fini et une
condition de distance dans un espace de Besov. Il ne s'applique pas à toute
ancienne adaptée ou distributionnelle uniformément
\(L^{3,\infty}\).

Par conséquent,

\[
 \text{ancienne }C_{w^*}L^{3,\infty}+\text{Duhamel dual}
 \quad\centernot\Longrightarrow\quad
 \text{ancienne Type I mild bornée d'Albritton--Barker}.  \tag{24}
\]

## 5. Unicité, non-unicité et caractérisation : matrice exacte

| Classe | Existence | Unicité publiée dans les sources auditées | Non-unicité publiée dans cette même classe |
|---|---|---|---|
| Petite solution mild \(L^{3,\infty}\) de Yamazaki | oui | oui, par contraction | non |
| Grande solution globale scindée BSS | oui | seulement sous portes additionnelles | non |
| Distributionnelle \(L^\infty_tL^{3,\infty}_x\) avec (5) | supposée/dérivée en interne | non | non |
| Ancienne mild bornée KNSS | objet conditionnel | théorèmes de Liouville sous hypothèses | non-unicité non affirmée |
| Ancienne Type I d'Albritton--Barker | équivalente à un scénario singulier conditionnel | rigidité sous hypothèses | non-unicité non affirmée |

Les constructions par intégration convexe dans des classes faibles plus
larges ou avec force ne démontrent pas automatiquement la non-unicité BSS.
Il faudrait vérifier séparément la scission (2), la trace du correcteur,
(8), l'inégalité locale, la donnée et l'absence de force.

## 6. Passe contradictoire sur le lemme du cycle 0048

Le rapport analytique parallèle affirme, sous (1), une borne
\(L^\infty_tL^{3,\infty}_x\) et une pression globale de Riesz, l'existence
d'un représentant \(C_{w^*}\) et l'identité de Duhamel au sens de Gelfand.
L'audit primaire donne le bilan suivant.

### 6.1 Points corroborés

- Le couple prédual exact est
  \(L^{3/2,1}_\sigma\)--\(L^{3,\infty}_\sigma\).
- L'estimation temporelle intégrée (13) est publiée et suffit à rendre le
  terme quadratique absolument intégrable contre chaque test du prédual.
- La petitesse n'est pas nécessaire pour **représenter** une solution déjà
  connue; elle intervient dans le point fixe et l'unicité.
- L'interprétation correcte de l'intégrale est faible-étoile/Gelfand.
- Le passage \(s\to-\infty\) contre un test fixe est compatible avec les
  estimations whole-past de Yamazaki/Taniuchi, sans donner de décroissance
  en norme de \(v(s)\).

### 6.2 Portes qui restent ouvertes

- La littérature ne promeut pas \(C_{w^*}\) en continuité forte.
- L'identité endpoint ne produit ni \(L^2_t\dot H^1_x\), ni inégalité
  d'énergie, ni suitable-ness : elle ne caractérise donc pas une solution
  BSS ou Leray--Hopf.
- La jauge globale de Riesz est une hypothèse suffisante pour identifier la
  pression et éliminer certaines composantes harmoniques. Tester l'équation
  contre des champs solénoïdaux peut projeter la vitesse sans cette jauge,
  mais ne reconstruit pas la pression et ne suffit pas à importer les
  notions BSS/KNSS.
- Le passage à une ancienne non triviale exige une concentration stable;
  ni (4) ni la borne faible-\(L^3\) n'empêche une limite nulle.
- L'unicité à grande norme demeure absente; soustraire deux formules de
  Duhamel ne ferme pas (16) lorsque le coefficient n'est pas petit.

### 6.3 Premier transfert invalide à bloquer

Le chaînage

\[
 \boxed{
 L^\infty_tL^{3,\infty}_x+\text{équation distributionnelle}
 \Longrightarrow C_{w^*}L^{3,\infty}+\text{Duhamel dual}}
 \tag{25}
\]

est le lemme interne borné du cycle. Même s'il est correct, les flèches

\[
 \boxed{
 (25)\centernot\Longrightarrow
 \text{mild forte Yamazaki},\quad
 \text{BSS},\quad
 \text{mild bornée KNSS},\quad
 \text{ancienne Type I d'Albritton--Barker}}
 \tag{26}
\]

sont invalides sans lemmes supplémentaires respectivement de continuité en
norme, d'énergie/scission, de lissage-bornitude et de contrôle Type I.

## 7. Veille différentielle primaire 2025--2026

Deux contrôles suffisent; aucun n'altère le verdict.

1. **Cheskidov--Hou, déjà catalogué (`NS-SRC-0044`).** Leur prépublication
   2026 sur la non-unicité mild périodique construit le produit quadratique
   par paraproduit dans des espaces de Besov négatifs et peut sortir de
   \(L^2_{\rm loc}\). Sa notion « mild » n'est ni la classe BSS, ni la classe
   faible-\(L^3\) de Yamazaki, ni la classe bornée KNSS. Elle ne prouve donc
   aucune non-unicité dans les lignes correspondantes de la matrice.

2. **Source primaire nouvelle proposée, sans transfert :** O. Jarrín,
   [*A remark on very weak suitable solutions and Leray solutions for the
   3D Navier--Stokes equations*](https://arxiv.org/abs/2607.03602v1),
   `arXiv:2607.03602v1` (3 juillet 2026). Le théorème 1.1 promeut une
   solution très faible adaptée en solution de Leray sous donnée
   \(L^2\), trace forte au temps initial, continuité faible locale et une
   hypothèse de Morrey locale sous-critique. Les corollaires de Lorentz
   concernés ont des exposants spatiaux strictement entre \(3\) et
   \(9/2\); ils ne couvrent pas la seule borne
   \(L^\infty_tL^{3,\infty}_x\), les anciennes d'énergie infinie ou la
   promotion vers une solution mild endpoint.

Une seconde source à ajouter au catalogue, parce qu'elle fixe la définition
et les estimations endpoint dans une version publiée et lisible, est
Taniuchi (2024), cité en section 2.4. Le plafond de deux sources nouvelles
est ainsi respecté. Aucune annonce primaire 2025--2026 vérifiée ne donne une
unicité ou une non-unicité générale à grande norme faible-\(L^3\).

## 8. Registre des implications

| Implication | Statut | Justification |
|---|---|---|
| BSS \(\Rightarrow\) solution adaptée locale | publiée | définition 1.1 |
| BSS \(\Rightarrow L^\infty_tL^{3,\infty}_x\) | manquante | le correcteur est énergétique, pas endpoint uniforme |
| \(L^\infty_tL^{3,\infty}_x\Rightarrow\) scission BSS | manquante | dissipation et inégalités d'énergie absentes |
| Duhamel endpoint \(\Rightarrow\) intégrale de Gelfand bornée | publiée | Yamazaki (13)--(14) |
| Duhamel endpoint \(\Rightarrow\) continuité forte | manquante | semi-groupe non \(C_0\) sur tout faible-\(L^3\) |
| faible-étoile des vitesses \(\Rightarrow\) convergence du produit | faux | contre-profil (19)--(22) |
| BSS faible-étoile compact \(\Rightarrow\) limite BSS | publiée, subséquentielle | théorème 1.3 et compacité forte locale |
| petite mild faible-\(L^3\Rightarrow\) unicité | publiée | contraction Yamazaki |
| grande BSS \(\Rightarrow\) unicité ou non-unicité | ouverte dans les sources | aucune implication publiée |
| ancienne endpoint \(\Rightarrow\) KNSS/Albritton--Barker | manquante | bornitude et mildness forte absentes |

## 9. Sources primaires et empreintes contrôlées

| ID / rôle | Source primaire | Version contrôlée | Empreinte locale |
|---|---|---|---|
| `NS-SRC-0188` | Barker--Seregin--Šverák, CPDE 2018 | publié; arXiv v1 distinct | arXiv PDF SHA-256 `ADEACBBB2E18A2E4C2C29E057AEA8B7293949602066F68AC0BCD8C999A1003A2`; manuscrit accepté SHA-256 `E623CCA4A7F5622BB2BFE27681395B2578ED65E402882236D0F6990BD58699DB` |
| endpoint | Yamazaki, Math. Ann. 2000 | article publié; support auteur 2010 | DOI et PDF auteur primaire contrôlés; le téléchargement Springer reçu comme HTML n'a pas été traité comme PDF |
| définition mild endpoint | Taniuchi, Math. Ann. 2024 | article publié | HTML éditeur primaire contrôlé |
| KNSS | Koch et al., Acta Math. 2009 | `arXiv:0709.3599v1` | PDF SHA-256 `EE4444837EAF72A0298F2032BE63A93C5DE41B61784BB1A68AE1E3E8973F14D8` |
| `NS-SRC-0189` | Albritton--Barker, JMFM 2019 | `arXiv:1811.00502v2` | PDF SHA-256 `FBAF90712190E3AA2C700AF7D1FD4C79C5DAFDC1B98B3A3CCE1AF3992C9D3C66` |
| veille | Jarrín 2026 | `arXiv:2607.03602v1` | page et texte arXiv primaires contrôlés |

## Décision bibliographique

**CONTINUER** le lemme endpoint sous le statut
`AI_INTERNAL_DERIVATION`, avec l'estimation de Yamazaki comme dépendance
publiée. **RÉVISER** toute phrase identifiant (5) à une solution mild au sens
fort. **ABANDONNER** les transferts directs vers BSS, KNSS ou la réduction
Type I d'Albritton--Barker. Le prochain test décisif doit viser une condition
falsifiable plaçant chaque trace dans le sous-espace de continuité forte du
semi-groupe, ou produire un contre-profil dynamique montrant que cette
promotion échoue même sous l'équation.
