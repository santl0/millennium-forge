# Cycle 0045 — compacité locale, pression et persistance au seuil faible-\(L^3\)

**Date de vérification :** 15 août 2026

**Nature :** veille primaire contradictoire indépendante

**Objet borné :** identifier les théorèmes exacts qui permettent, pour une
suite de solutions de Navier--Stokes, de passer d'estimations locales à une
limite forte, puis de conserver une singularité ou une normalisation non nulle.

Le cadre cible est

\[
\partial_tu-\Delta u+\operatorname{div}(u\otimes u)+\nabla p=f,
\qquad \operatorname{div}u=0,                              \tag{1}
\]

en dimension trois, avec viscosité normalisée à un. La limite ancienne
recherchée est non forcée, sur \(\mathbb R^3\) ou éventuellement le
demi-espace, et doit appartenir à une notion de solution explicitement
stable : faible adaptée, d'énergie locale ou mild.

## Verdict exécutable

1. **Une compacité forte locale publiée existe**, mais elle ne part pas de la
   seule borne \(L^\infty_tL^{3,\infty}_x\). Le lemme A.2
   d'Albritton--Barker (2020) suppose, sur chaque cylindre fixé, une borne

   \[
   \|u_n\|_{L^3(Q)}+\|p_n\|_{L^{3/2}(Q)}\le M              \tag{2}
   \]

   pour des solutions faibles adaptées, avec convergence de la géométrie de
   bord. Il conclut, après extraction, à

   \[
   u_n\to u\quad\hbox{fortement dans }L^3(Q'),
   \qquad p_n\rightharpoonup p\quad\hbox{dans }L^{3/2}(Q') \tag{3}
   \]

   sur les cylindres intérieurs.

2. **Le mécanisme abstrait est publié par Simon (1987).** Avec
   \(X\Subset B\hookrightarrow Y\), une borne dans
   \(L^p_tX\), \(1<p<\infty\), et une dérivée temporelle bornée dans
   \(L^1_tY\) donnent la compacité dans \(L^p_tB\). Une borne
   \(L^\infty_tX\) et une dérivée dans \(L^r_tY\), \(r>1\), donnent la
   compacité dans \(C_tB\). L'application

   \[
   H^1(B_R)\Subset L^2(B_R)\hookrightarrow W^{-1,3/2}(B_R) \tag{4}
   \]

   est une **spécialisation standard dérivée**, non un théorème
   Navier--Stokes énoncé par Simon.

3. Sous des bornes uniformes d'énergie locale et de pression, (4) donne
   \(u_n\to u\) fortement dans \(L^2_{t,x}\). La borne énergétique
   parabolique \(u_n\in L^{10/3}_{t,x}\) permet ensuite, par interpolation,
   la convergence forte dans tout \(L^q_{t,x}\), \(2\le q<10/3\), notamment
   \(L^3\). C'est la structure qui sous-tend (3).

4. **La borne faible-\(L^3\) seule n'est pas cette hypothèse.** Sur une boule,

   \[
   \|u_n(t)\|_{L^2(B_R)}\le C R^{1/2}
   \|u_n(t)\|_{L^{3,\infty}},                              \tag{5}
   \]

   mais elle ne donne pas la dissipation
   \(L^2_tH^1_x\). Le calcul global de Riesz donne seulement

   \[
   p_n\in L^\infty_tL^{3/2,\infty}_x,                     \tag{6}
   \]

   qui s'injecte localement dans \(L^r\) pour \(r<3/2\), pas dans
   l'endpoint \(L^{3/2}\). Le flux \(p_nu_n\) est formellement au seuil
   faible-\(L^1\), insuffisant pour une estimation uniforme par Hölder.

5. **Barker--Seregin--Šverák (2018) publie néanmoins une vraie stabilité
   faible-étoile à grande donnée \(L^{3,\infty}\)**, mais pour une classe
   spécialement définie. La solution est scindée

   \[
   v=S(t)u_0+u,
   \qquad
   u\in L^\infty_tL^2_x\cap L^2_t\dot H^1_x,              \tag{7}
   \]

   et le correcteur satisfait une inégalité d'énergie globale perturbée ainsi
   que l'inégalité d'énergie locale. Sous
   \(u_{0,n}\rightharpoonup^*u_0\) dans \(L^{3,\infty}\), leur théorème 1.3
   extrait une solution de même classe; la preuve donne plus précisément

   \[
   u_n\to u\text{ dans }C([0,T];L^{9/8}_{\rm loc})
   \quad\text{et dans }L^s_{\rm loc},\quad1<s<10/3.        \tag{8}
   \]

   Ce résultat ferme la compacité du produit à l'intérieur de cette classe.
   Il ne s'applique pas automatiquement à toute suite de solutions adaptées
   possédant seulement une borne de vitesse faible-\(L^3\), ni à des domaines
   croissants avec frontière sans lemme de raccord.

6. **La persistance de non-trivialité requiert une entrée distincte.** Deux
   mécanismes publiés sont disponibles :

   - Albritton--Barker, proposition A.5 : sous (3) et sous persistance de
     l'explosion \(L^\infty\) sur chaque cylindre, la limite reste singulière;
   - Albritton--Barker, section 4, et Seregin--Šverák : une normalisation
     ponctuelle \(|u_n(0,0)|=1\) jointe à une compacité locale uniforme ou
     Hölder donne \(|U(0,0)|=1\).

   Une minoration de norme critique à une tranche, sans convergence forte de
   cette tranche, ne suffit pas.

7. **Aubin--Lions intérieur ne donne pas la trace terminale forte.** Les
   bornes naturelles fournissent au mieux, en changeant l'espace compact,

   \[
   u_n\to u\quad\text{dans }C_tH^{-\sigma}_{x,\rm loc}
   \quad(\sigma>0),                                       \tag{9}
   \]

   pas dans \(C_tL^2_x\). Une couche terminale haute fréquence peut donc
   converger fortement dans l'espace-temps tout en conservant une énergie
   non nulle à \(t=0\). Cette distinction est compatible avec tous les
   théorèmes audités.

8. **La veille 2025--2026 est négative pour le raccord manquant.** Aucun
   résultat primaire vérifié ne démontre

   \[
   \sup_n\|u_n\|_{L^\infty_tL^{3,\infty}_x}<\infty
   \Longrightarrow
   \text{limite ancienne adaptée non triviale}             \tag{10}
   \]

   pour une suite arbitraire de blow-ups. Les articles récents ajoutent des
   hypothèses de scénario Type II, de symétrie, d'auto-similarité, de
   structure de solution ou de normalisation.

## 1. Le théorème abstrait de Simon et son application exacte

Jacques Simon,
[*Compact sets in the space \(L^p(0,T;B)\)*](https://doi.org/10.1007/BF01762360),
*Annali di Matematica Pura ed Applicata* **146** (1987), 65--96,
DOI `10.1007/BF01762360`.

**Statut.** Article publié. Le PDF éditeur et le corollaire 4 ont été
audités.

Soient trois espaces tels que

\[
X\Subset B\hookrightarrow Y.                              \tag{11}
\]

Le corollaire 4 contient les deux formes utiles :

- si une famille est bornée dans \(L^p(0,T;X)\),
  \(1<p<\infty\), et sa dérivée distributionnelle est bornée dans
  \(L^1(0,T;Y)\), elle est relativement compacte dans
  \(L^p(0,T;B)\);
- si elle est bornée dans \(L^\infty(0,T;X)\) et la dérivée est bornée dans
  \(L^r(0,T;Y)\), \(r>1\), elle est relativement compacte dans
  \(C([0,T];B)\).

Il est important que le premier énoncé ne donne qu'une compacité
espace-temps et que le second exige la borne \(L^\infty_tX\). Une borne
\(L^2_tH^1_x\) ne peut donc pas être promue sans autre entrée en compacité
\(C_tL^2_x\).

### 1.1 Ledger Navier--Stokes sur un cylindre intérieur

Supposons, sur \(Q=B_R\times(-S,0)\),

\[
\sup_n\left[
\|u_n\|_{L^\infty_tL^2_x}
+\|\nabla u_n\|_{L^2_{t,x}}
+\|p_n-(p_n)_{B_R}\|_{L^{3/2}(Q)}
\right]<\infty,                                           \tag{12}
\]

et une force uniformément bornée dans un espace négatif compatible. Par
Sobolev parabolique,

\[
\|u_n\|_{L^{10/3}(Q)}\le C(Q).                            \tag{13}
\]

L'équation donne, sur une boule légèrement plus petite,

\[
\partial_tu_n
=\Delta u_n-\operatorname{div}(u_n\otimes u_n)-\nabla p_n+f_n
\quad\text{borné dans }
L^{4/3}_tW^{-1,4/3}_x,                                    \tag{14}
\]

ou dans un espace négatif un peu plus faible. Les puissances exactes peuvent
être améliorées si la pression ou la force le permettent; \(4/3>1\) suffit.
Simon avec (4) donne

\[
u_n\to u\quad\text{fortement dans }L^2_{t,x}.             \tag{15}
\]

Interpoler (15) avec (13) donne, pour \(2\le q<10/3\),

\[
\|u_n-u\|_{L^q(Q')}\to 0.                                 \tag{16}
\]

En particulier \(q=3\), donc
\(u_n\otimes u_n\to u\otimes u\) fortement dans
\(L^{3/2}(Q')\).

**Statut.** Le corollaire abstrait est `PAPER_PROOF` par Simon. Le choix des
espaces (4), l'estimation (14) et l'interpolation (16) sont une
`STANDARD_DERIVATION` du laboratoire. Le résultat Navier--Stokes complet,
avec pression et énergie locale, est directement publié sous une forme plus
proche dans Albritton--Barker, lemme A.2.

### 1.2 Ce que Simon donne pour la trace

À partir de

\[
u_n\text{ borné dans }L^\infty_tL^2_x,
\qquad
\partial_tu_n\text{ borné dans }L^r_tH^{-1}_x, r>1,
\]

on peut choisir

\[
L^2(B_R)\Subset H^{-\sigma}(B_R)\hookrightarrow H^{-1}(B_R)
\quad(0<\sigma<1)                                         \tag{17}
\]

et obtenir la compacité dans \(C_tH^{-\sigma}_x\). Il manque la borne
\(L^\infty_tH^1_x\) qui serait nécessaire pour choisir \(B=L^2\) dans la
seconde partie du corollaire. L'énergie de Navier--Stokes ne fournit que
\(L^2_tH^1_x\).

Le passage de la trace dans \(H^{-\sigma}\) est utile pour identifier la
donnée distributionnelle. Il ne conserve ni une norme \(L^2\) inférieure,
ni une valeur ponctuelle, ni le produit quadratique terminal.

## 2. Albritton--Barker 2020 : compacité et persistance publiées

Dallas Albritton et Tobias Barker,
[*Localised necessary conditions for singularity formation in the
Navier--Stokes equations with curved
boundary*](https://doi.org/10.1016/j.jde.2020.06.009), *Journal of
Differential Equations* **269** (2020), 7529--7573, DOI
`10.1016/j.jde.2020.06.009`,
[`arXiv:1811.00507v2`](https://arxiv.org/abs/1811.00507v2).

**Équation et notion.** Navier--Stokes incompressible 3D non forcé sur un
domaine borné, avec non-glissement sur la portion de frontière; solution
faible adaptée au bord. Après troncature, une force régulière apparaît.

### 2.1 Lemme A.2 : théorème compact exact

Soit \((u_n,p_n,\varphi_n)\) une suite de solutions faibles adaptées des
équations aplaties dans un demi-cylindre \(Q^+\), avec
\(\varphi_n\to\varphi\) dans \(C^2\) et

\[
\sup_n\left(
\|u_n\|_{L^3(Q^+(R))}
+\|p_n\|_{L^{3/2}(Q^+(R))}
\right)\le M.                                             \tag{18}
\]

Le lemme A.2 extrait, pour tout \(0<R<1\), une solution faible adaptée
limite telle que

\[
u_n\to u\text{ dans }L^3(Q^+(R)),
\qquad p_n\rightharpoonup p\text{ dans }L^{3/2}(Q^+(R)).  \tag{19}
\]

Les auteurs indiquent explicitement que la preuve vient de l'inégalité
d'énergie locale et d'Aubin--Lions. L'analogue intérieur est standard; la
valeur de cette source est de traiter aussi le bord courbe convergent.

**Limite endpoint.** (18) n'est pas la borne
\(L^\infty_tL^{3,\infty}_x\). Sur un cylindre de mesure finie, cette dernière
ne contrôle que \(L^q\) pour \(q<3\), et le Riesz global ne donne que
\(p\in L^r\) pour \(r<3/2\). L'injection stricte interdit de remplacer les
exposants de (18) par leurs versions faibles sans refaire l'estimation locale
d'énergie et la compacité.

### 2.2 Proposition A.5 : persistance des singularités

Sous les convergences (19), et si

\[
\limsup_{n\to\infty}
\|u_n\|_{L^\infty(Q^+(R))}=\infty
\quad\text{pour tout }0<R<1,                              \tag{20}
\]

la proposition A.5 conclut que la limite a un point singulier à l'origine.
La preuve est une contraposée : si la limite était bornée, la convergence
forte \(L^3\), une itération de décroissance de pression et l'epsilon-régularité
donneraient une borne \(L^\infty\) uniforme pour la suite sur un cylindre
plus petit, contredisant (20).

Ce théorème préserve une singularité, non une valeur ponctuelle. Il requiert
la pression endpoint et la convergence forte déjà obtenues.

### 2.3 Théorème 1.2 : extraction ancienne par une route plus forte

Pour une singularité d'une solution adaptée, les auteurs sélectionnent un
anneau régulier, tronquent par Bogovskiĭ puis choisissent des points de
maximum. Les champs redimensionnés vérifient

\[
|v_n|\le1,qquad |v_n(0,0)|=1,                             \tag{21}
\]

et la force redimensionnée tend vers zéro dans des normes sous-critiques.
La proposition 4.1 donne une borne uniforme
\(C^{1/2}_{\rm par}\); le corollaire 4.2 fournit

\[
v_n\to U\quad\text{uniformément sur tout compact},
\qquad |U(0,0)|=1.                                        \tag{22}
\]

Les propositions de pression décomposent la pression en partie de Riesz/BMO
et parties harmoniques pondérées par la distance au bord. Cette information
permet de montrer que la limite est une solution ancienne mild, pas seulement
une solution distributionnelle.

**Conclusion.** Albritton--Barker ferme toute la chaîne compacité--pression--
non-trivialité grâce à la borne \(L^\infty\), à la force sous-critique et à la
compacité de Hölder. Leur théorème ne dit pas que la borne
\(L^\infty_tL^{3,\infty}_x\) seule produit ces trois propriétés.

## 3. Barker--Seregin--Šverák 2018 : stabilité faible-étoile structurée

Tobias Barker, Gregory Seregin et Vladimír Šverák,
[*On stability of weak Navier--Stokes solutions with large
\(L^{3,\infty}\) initial data*](https://doi.org/10.1080/03605302.2018.1449219),
*Communications in Partial Differential Equations* **43** (2018), 628--651,
DOI `10.1080/03605302.2018.1449219`.

La prépublication primaire
[`arXiv:1603.03211v1`](https://arxiv.org/abs/1603.03211v1), 10 mars 2016,
porte le titre *On global solutions to the Navier--Stokes system with large
\(L^{3,\infty}\) initial data* et liste Barker et Seregin. Les métadonnées
publiées Crossref et du dépôt institutionnel Oxford ajoutent Šverák et le
titre publié ci-dessus. Le texte intégral v1/accepté audité conserve la
numérotation employée ci-dessous. Cette différence de métadonnées doit être
conservée dans le registre de version.

### 3.1 Notion exacte de solution

Sur \(\mathbb R^3\times(0,\infty)\), sans force, les auteurs définissent une
solution faible globale \(L^{3,\infty}\) par

\[
v=V+u,
\qquad V=S(t)u_0,
\qquad u\in L^\infty(0,T;L^2_\sigma)
\cap L^2(0,T;\dot H^1_\sigma).                            \tag{23}
\]

Le correcteur \(u\) satisfait le système perturbé, une inégalité d'énergie
globale contenant \(V\otimes u+V\otimes V\), une continuité faible en temps,
une trace forte \(u(t)\to0\) dans \(L^2\), et l'inégalité d'énergie locale
pour \((v,p)\).

Cette notion est plus structurée qu'une solution distributionnelle ou adaptée
arbitraire dont seule la vitesse serait bornée dans un Lorentz critique. En
particulier, la partie calorique et le correcteur énergétique sont fixés par
la donnée initiale.

### 3.2 Théorème 1.3 et topologies réellement obtenues

Si

\[
u_{0,n}\rightharpoonup^*u_0
\quad\text{dans }L^{3,\infty}(\mathbb R^3)                 \tag{24}
\]

et \(v_n\) sont des solutions globales faibles de cette classe, le théorème
1.3 extrait une sous-suite convergeant au sens des distributions vers une
solution globale faible \(L^{3,\infty}\) de donnée \(u_0\).

La preuve est plus quantitative que le résumé du théorème. La décomposition
Lorentz des données donne une estimation d'énergie uniforme du correcteur,
leur équation (3.36). Les termes non linéaires sont séparés et les estimations
coercives de Stokes donnent les bornes (3.43)--(3.45) sur vitesse et gradient
de pression. Après diagonale,

\[
u_n\to u
\quad\text{dans }C([0,T];L^{9/8}(B_R))                   \tag{25}
\]

pour tout \(R,T<\infty\), puis

\[
u_n\to u
\quad\text{dans }L^s(B_R\times(0,T)),
\qquad1<s<10/3.                                           \tag{26}
\]

Le choix \(s=3\) identifie le produit quadratique local. Les auteurs passent
également les inégalités d'énergie globale et locale.

### 3.3 Transfert et non-transfert

Ce résultat est le meilleur théorème publié trouvé pour une stabilité
faible-étoile construite depuis le véritable endpoint spatial. Il montre que
l'endpoint n'interdit pas toute compacité : il faut transporter avec lui la
scission calorique et l'inégalité énergétique du correcteur.

Il ne ferme toutefois pas directement le cycle :

- (24) porte sur les **données initiales**, pas sur une borne arbitraire
  \(L^\infty_tL^{3,\infty}_x\) de solutions adaptées données;
- le théorème est forward sur \(\mathbb R^3\), avec un temps initial fixe;
  une extraction ancienne exige une diagonale cohérente lorsque le temps
  initial recule;
- aucune normalisation n'empêche la limite nulle;
- le théorème ne traite pas les domaines croissants ou le demi-espace;
- l'unicité de toute solution faible de grande donnée n'est pas obtenue. Les
  résultats d'unicité de l'article ajoutent petitesse/continuité locale.

## 4. Barker--Prange 2020 : concentration Type I, pas trace compacte

Tobias Barker et Christophe Prange,
[*Localized smoothing for the Navier--Stokes equations and concentration of
critical norms near
singularities*](https://doi.org/10.1007/s00205-020-01495-6), *Archive for
Rational Mechanics and Analysis* **236** (2020), 1487--1541,
[`arXiv:1812.09115v2`](https://arxiv.org/abs/1812.09115v2).

**Notions.** Solution d'énergie locale pour le lissage; solution de
Leray--Hopf pour l'application aux singularités sur \(\mathbb R^3\), sans
force.

Le théorème 1 suppose une borne \(L^2_{\rm uloc}\) globale sur la donnée et
une petite norme locale \(L^3\); l'appendice B étend le petit espace critique
à \(L^{3,\infty}\). La perturbation de la solution mild possède une trace
locale nulle et devient Hölder. Il ne s'agit pas d'un lissage pour grande
norme faible-\(L^3\) locale.

Sous leur borne Type I de Morrey-énergie et l'hypothèse qu'un point est
singulier au premier temps \(T_*\), le théorème 2 force, à tout temps assez
proche de \(T_*\), une masse \(L^3\) universelle sur une boule de rayon
\(C(M)\sqrt{T_*-t}\). L'appendice B donne la variante faible-\(L^3\).

Cette conclusion assure qu'une concentration critique reste près du centre
singulier à l'échelle parabolique. Mais après redimensionnement, une borne

\[
\|u_n(0)\|_{L^{3,\infty}(B_C)}\ge\gamma                  \tag{27}
\]

n'implique pas que la limite faible-étoile soit non nulle. Les normes peuvent
rester minorées sous oscillation ou concentration tandis que les fonctions
convergent faiblement vers zéro. Pour transférer (27), il faut soit une
convergence forte de tranche, soit la proposition de persistance A.5, soit
une normalisation ponctuelle et un module de continuité.

## 5. Jia--Šverák et Seregin--Šverák : deux routes sous-critiques/fortes

### 5.1 Jia--Šverák 2014

Hao Jia et Vladimír Šverák,
[*Local-in-space estimates near initial time for weak solutions of the
Navier--Stokes equations and forward self-similar
solutions*](https://doi.org/10.1007/s00222-013-0468-x), *Inventiones
Mathematicae* **196** (2014), 233--265,
[`arXiv:1204.0529`](https://arxiv.org/abs/1204.0529).

La notion de solution de Leray locale inclut
\(L^\infty_tL^2_{\rm uloc}\), \(L^2_tH^1_{\rm uloc}\), une représentation
locale de pression et l'inégalité d'énergie locale. Le théorème 3.1 suppose
que la donnée est localement dans \(L^m\), \(m>3\). Après extension
solénoïdale et soustraction de la solution mild, la perturbation a une trace
locale nulle; les auteurs obtiennent une décroissance quantitative de
l'énergie et de la pression près de \(t=0\), puis une régularité Hölder.

**Limite.** La condition \(m>3\) est sous-critique. Barker--Prange atteint
l'espace critique sous petitesse, mais aucune de ces sources ne donne la
compacité ancienne à grande borne faible-\(L^3\) sans la structure d'énergie
locale.

### 5.2 Seregin--Šverák 2014

Gregory Seregin et Vladimír Šverák,
[*Rescalings at possible singularities of Navier--Stokes equations in
half-space*](https://doi.org/10.1090/S1061-0022-2014-01317-9), *St.
Petersburg Mathematical Journal* **25** (2014), 815--833,
[`arXiv:1302.0141`](https://arxiv.org/abs/1302.0141).

Ils partent d'une solution forte du problème initial-au-bord dans le
demi-espace, supposée exploser en temps fini. Le zoom est fait aux maxima et
vérifie une borne uniforme \(L^\infty\) ainsi qu'une normalisation de valeur
un. La précompacité est obtenue par les représentations explicites du noyau
de Stokes du demi-espace et Arzelà--Ascoli. Dans les deux scénarios, intérieur
ou bord restant à distance finie, la convergence est uniforme sur les
compacts et conserve la valeur un. Une décomposition de pression BMO/harmonique
permet de conclure que la limite est ancienne mild et non parasitaire.

**Limite.** Le mécanisme exige la normalisation au maximum et la borne
globale \(L^\infty\) après zoom. Il ne dérive pas ces propriétés d'une borne
faible-\(L^3\).

## 6. Pression : données minimales de passage à la limite

Trois cadres doivent être distingués.

1. **Espace entier avec normalisation de Riesz.** Si
   \(p_n=\mathcal R_i\mathcal R_j(u_{n,i}u_{n,j})\), la borne faible-\(L^3\)
   donne (6). C'est une borne critique mais non l'endpoint fort requis dans
   (18).

2. **Cylindre local.** La pression se décompose en une partie de Riesz locale
   et une fonction harmonique. La constante spatiale dépendant du temps doit
   être soustraite. Une borne du gradient harmonique ou de l'oscillation est
   nécessaire; la vitesse locale seule ne la fixe pas.

3. **Demi-espace ou domaines croissants.** La pression contient une partie
   liée au bord. Seregin--Šverák utilise le noyau de Solonnikov;
   Albritton--Barker utilise des estimations harmoniques pondérées par la
   distance au bord. Une simple convergence distributionnelle de la vitesse
   ne garantit pas que la limite soit mild : elle peut laisser une solution
   parasitaire entraînée par un gradient spatialement constant.

Dans le ledger (12)--(16), la pression est donc une hypothèse ou une
conséquence d'une représentation uniformément contrôlée. Elle ne peut pas
être supprimée après coup de l'inégalité d'énergie locale.

## 7. Persistance de non-trivialité : quatre niveaux

| information avant passage | topologie de convergence | conclusion stable |
|---|---|---|
| \(|u_n(0,0)|=1\) + Hölder uniforme | uniforme locale | \(|u(0,0)|=1\) |
| singularité de chaque \(u_n\) + (19) | forte \(L^3\), pression faible \(L^{3/2}\) | limite singulière, proposition A.5 |
| masse \(L^3\) ou faible-\(L^3\) minorée à \(t=0\) | faible ou \(H^{-\sigma}\) | aucune non-trivialité en général |
| trace terminale forte \(L^2\) | \(C_tL^2_x\) | énergie terminale conservée |

Le quatrième niveau n'est pas fourni par les bornes naturelles
\(L^\infty_tL^2_x\cap L^2_tH^1_x\). Le troisième est exactement ce que
donne une concentration Type I si aucune régularité supplémentaire n'est
transportée.

Pour l'endpoint fort \(L^3\), Escauriaza--Seregin--Šverák (2003) et Seregin
(2012) utilisent l'absolue continuité de la norme \(L^3\) afin d'obtenir une
trace terminale nulle après un zoom centré au temps singulier, tandis qu'une
epsilon-régularité conserve la non-trivialité dans l'espace-temps. Cette
propriété d'ordre continu échoue dans \(L^{3,\infty}\). Le titre historique
*\(L_{3,\infty}\)-solutions* signifie ici
\(L^\infty_tL^3_x\), et non le Lorentz spatial
\(L^{3,\infty}_x\).

## 8. Passe adverse reproductible

### Test A — faible-\(L^3\) contre hypothèse du lemme A.2

Sur un ensemble de mesure finie, le profil

\[
f_\varepsilon(x)=|x|^{-1}\mathbf 1_{\{\varepsilon<|x|<1\}}
\]

a une norme \(L^{3,\infty}\) uniforme mais

\[
\int|f_\varepsilon|^3\,dx\simeq|\log\varepsilon|\to\infty. \tag{28}
\]

**Résidu certifié :** (2) ne suit pas de la borne faible-\(L^3\).

### Test B — compacité intérieure contre trace terminale

Une famille de couches de largeur \(n^{-2}\), de fréquence spatiale \(n\),
peut être bornée dans

\[
L^\infty_tL^2_x\cap L^2_tH^1_x,
\qquad \partial_tu_n\text{ dans }L^2_tH^{-1}_x,            \tag{29}
\]

et converger fortement vers zéro dans \(L^2_{t,x}\), tout en conservant une
trace terminale oscillante de norme \(L^2\) constante. Simon prédit bien
la compacité intérieure et seulement une trace compacte négative.

**Résidu certifié :** aucune implication de (29) vers
\(C_tL^2_x\) compact.

### Test C — translation critique

Pour \(U\in C_c^\infty\) solénoïdal,

\[
u_n(x,t)=U(x-ne_1)
\]

conserve toutes les normes critiques spatiales et converge localement vers
zéro. La stabilité BSS accepte une limite nulle si les données convergent
faible-étoile vers zéro.

**Résidu certifié :** le théorème de compacité ne produit pas la
non-trivialité.

### Test D — pression harmonique

Ajouter à une pression locale une fonction harmonique dépendant de la suite
ne change pas \(-\Delta p=\operatorname{divdiv}(u\otimes u)\), mais peut
faire diverger son gradient sur le compact si aucune normalisation ou
condition de bord n'est imposée.

**Résidu certifié :** l'équation de Poisson seule ne contrôle pas la pression
locale; il faut la représentation ou l'estimation harmonique.

### Test E — produit sous convergence de trace négative

Une suite de cisaillements solénoïdaux haute fréquence peut converger vers
zéro dans \(H^{-\sigma}\) tandis que
\(u_n\otimes u_n\) conserve une moyenne non nulle. La compacité (9) ne suffit
donc pas à transmettre le produit au temps terminal.

**Résidu certifié :** la convergence forte \(L^3\) espace-temps traite le
produit intérieur, pas la tranche finale.

## 9. Veille différentielle 2025--2026

La veille a interrogé les sources primaires disponibles au 15 août 2026 sur
les expressions *ancient solution*, *weak \(L^3\)*, *local energy
compactness*, *persistence of singularities*, *Type I/II blow-up* et
*terminal trace*.

- Gregory Seregin,
  [`arXiv:2507.08733v2`](https://arxiv.org/abs/2507.08733v2), et
  [`arXiv:2606.29468v1`](https://arxiv.org/abs/2606.29468v1), obtient ou
  exclut des limites anciennes de type Euler sous des scénarios Type II et
  des fonctionnelles supplémentaires. Ces limites ne sont pas la limite
  parabolique Navier--Stokes de (10).

- Tobias Barker,
  [*Quantitative classification of potential Navier--Stokes singularities
  beyond the blow-up time*](https://arxiv.org/abs/2510.20757v3),
  `arXiv:2510.20757v3`, révisé le 11 août 2026, traite des classifications
  quantitatives sous approximations axisymétriques et hypothèses de taux.
  Il ne fournit pas un théorème générique de compacité endpoint.

- Ben Pineau et Vlad Vicol,
  [`arXiv:2607.09619v2`](https://arxiv.org/abs/2607.09619v2), excluent des
  profils rétrogrades auto-similaires tournés dans des régimes particuliers.
  L'exclusion d'un ansatz n'établit pas la persistance générale d'une limite
  ancienne.

- Runlong Yu,
  [`arXiv:2606.12756v1`](https://arxiv.org/abs/2606.12756v1), maintient
  explicitement comme hypothèses plusieurs étapes d'extraction de défauts et
  ne construit pas une solution ancienne compacte.

- Les constructions de non-unicité 2025--2026 depuis données critiques
  singulières ou dans des classes faibles hors Leray--Hopf n'établissent pas
  (10) et ne donnent pas de blow-up classique Clay.

**Résultat de veille.** Aucun théorème publié ou prépublié vérifié en
2025--2026 ne remplace les hypothèses (12), (18), (20), (21) ou (23) par la
seule borne de vitesse \(L^\infty_tL^{3,\infty}_x\). Le statut de la veille
est donc **négatif pour la fermeture**, sans affirmation d'exhaustivité
absolue au-delà des sources primaires recherchées.

## 10. Deux entrées de source proposées

Le catalogue contient déjà Barker--Prange sous `NS-SRC-0146` et
Bradshaw--Tsai sous `NS-SRC-0186`. Deux nouvelles entrées seulement sont
indispensables à ce cycle :

1. **`NS-SRC-0187` proposé — Albritton--Barker 2020.** Source directe du
   lemme compact A.2, de la persistance A.5, de la compacité Hölder et du
   passage à une solution ancienne mild. Statut `PAPER_PROOF` pour ces
   théorèmes; aucune attribution d'un théorème faible-\(L^3\) général.

2. **`NS-SRC-0188` proposé — Barker--Seregin--Šverák 2018.** Source directe
   de la notion scindée de solution globale faible \(L^{3,\infty}\), de la
   stabilité faible-étoile et des convergences (25)--(26). Statut
   `PAPER_PROOF`; enregistrer la différence entre auteurs/titre de l'arXiv v1
   et métadonnées publiées.

Simon 1987 doit être cité comme outil fonctionnel primaire dans le rapport,
mais une troisième entrée n'est pas indispensable : le théorème
Navier--Stokes effectivement utilisé est déjà incarné par les deux sources
ci-dessus.

## 11. Graphe de preuve mis à jour

| arête | statut | hypothèse manquante ou perte |
|---|---|---|
| énergie locale + dérivée négative \(\Rightarrow\) forte \(L^2_{t,x}\) | Simon + dérivation standard | aucune sur cylindre intérieur |
| forte \(L^2\) + borne \(L^{10/3}\) \(\Rightarrow\) forte \(L^3\) | interpolation standard | borne énergétique uniforme |
| adaptée + \(L^3/L^{3/2}\) \(\Rightarrow\) limite adaptée | Albritton--Barker A.2 | pression endpoint, géométrie contrôlée |
| données faibles-\(L^3\) scindées \(\Rightarrow\) limite faible stable | Barker--Seregin--Šverák | classe scindée, temps initial fixe |
| forte \(L^3\) + explosion persistante \(\Rightarrow\) limite singulière | Albritton--Barker A.5 | condition (20) |
| normalisation ponctuelle + Hölder \(\Rightarrow\) limite non nulle | Seregin--Šverák; Albritton--Barker | borne \(L^\infty\)/Hölder |
| espace-temps compact \(\Rightarrow\) trace forte \(L^2\) | **faux en général** | module terminal plus fort |
| borne \(L^\infty_tL^{3,\infty}_x\) seule \(\Rightarrow\) ancienne non triviale | **manquante** | énergie uniforme, pression, trace/non-trivialité |

## 12. Empreintes SHA256 des PDF audités

Les empreintes portent sur les octets téléchargés et relus le 15 août 2026.
Elles détectent une modification du fichier servi, mais ne certifient ni le
contenu mathématique ni l'identité éditoriale.

| PDF primaire | version/état | octets | SHA256 |
|---|---:|---:|---|
| `https://arxiv.org/pdf/1811.00507` | Albritton--Barker v2, publié | 476336 | `FDD91E657B5CF503286B4E45CC084C12C8B202AAF24BCDAD67EDEA46EDFA4102` |
| `https://arxiv.org/pdf/1812.09115` | Barker--Prange v2, publié | 505915 | `D1C0D26270F784697460DC5CE56DC5599CFEABCE40C0F3AAA35372296BC7D78D` |
| `https://arxiv.org/pdf/1204.0529` | Jia--Šverák v1, publié | 304378 | `1E8685FBE09C669854357278010F345FA5C98845C5888BA6720936A0B3F1591F` |
| `https://arxiv.org/pdf/1302.0141` | Seregin--Šverák v1, publié | 234572 | `050212901E7CDBD1687618770DA6D3705DE9655CE94E3CE3555558706A4993BC` |
| `https://arxiv.org/pdf/1603.03211` | Barker--Seregin arXiv v1 | 266074 | `ADEACBBB2E18A2E4C2C29E057AEA8B7293949602066F68AC0BCD8C999A1003A2` |
| dépôt institutionnel Oxford, fichier `1603.03211.pdf` | manuscrit accepté associé à l'article publié | 440949 | `E623CCA4A7F5622BB2BFE27681395B2578ED65E402882236D0F6990BD58699DB` |
| `https://link.springer.com/content/pdf/10.1007/BF01762360.pdf` | Simon 1987, PDF éditeur | 1777278 | `86B81EB6BE3BE81AFD97FD43F185F63929F552FDAAAF13EE7A9D89F6483A3DB3` |

## Conclusion

La compacité intérieure n'est plus un verrou bibliographique vague. Elle est
publiée sous deux formes complémentaires :

\[
\boxed{
\begin{array}{c}
\text{solution adaptée + énergie/pression endpoint}
\Rightarrow \text{forte }L^3_{\rm loc},\\[2mm]
\text{solution faible }L^{3,\infty}\text{ scindée}
\Rightarrow \text{stabilité faible-étoile et forte locale.}
\end{array}}
\]

Le premier verrou restant est donc plus précis : démontrer que la suite
tronquée réelle du laboratoire satisfait uniformément l'une de ces deux
architectures. Il faut soit produire les bornes (12)/(18), avec pression
normalisée, soit prouver une scission calorique BSS stable sur chaque fenêtre
ancienne.

Même après cette étape, une seconde porte indépendante subsiste : conserver
la non-trivialité au temps terminal. La compacité espace-temps de Simon ne
la fournit pas. La prochaine expérience décisive doit tester si la suite
réelle possède la condition de persistance (20), un module Hölder analogue à
(22), ou un module temporel plus fort que la couche terminale critique. Sans
l'une de ces informations, une limite ancienne nulle reste compatible avec
toutes les bornes faibles du cycle.
