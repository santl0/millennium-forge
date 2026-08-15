# Cycle 0055 — classification d'une orbite de rotation exacte

Date : 2026-08-15.

Statut : `AI_INTERNAL_DERIVATION`; lemme de symétrie pour l'équation
renormalisée, sans conclusion Clay. Les rigidités finales citées sont soit
publiées et déjà auditées, soit une prépublication dont la preuve n'est pas
reproduite ici.

## Verdict

Le lemme est **vrai après explicitation de la jauge de pression, de l'axe de
rotation et du sens distributionnel**. Sa forme correcte est la dichotomie
exclusive suivante.

Soit \(I\subset\mathbb R\) un intervalle connexe, \(\kappa>0\), et soit
\(Z\) une solution distributionnelle divergence-free de l'équation autonome
projetée

\[
 \partial_sZ+\mathcal F_\kappa(Z)=0,
 \qquad
 \mathcal F_\kappa(W)
 =-\Delta W+\mathbb P\operatorname{div}(W\otimes W)
 +\kappa(1+y\cdot\nabla)W,                       \tag{1}
\]

sur \(\mathbb R^3\times I\). Fixons un sous-groupe de rotations autour d'un
axe passant par l'origine du drift. Si

\[
 Z(s)=Q_{\theta(s)}U,qquad
 \theta\in W^{1,1}_{\rm loc}(I),                 \tag{2}
\]

au sens des distributions, alors :

1. si \(\mathcal RU=0\), où \(\mathcal R\) est le générateur de \(Q\),
   alors \(Q_\beta U=U\) pour tout \(\beta\), \(Z(s)=U\) est stationnaire
   et \(\mathcal F_\kappa(U)=0\); aucune contrainte sur \(\theta'\) n'est
   possible ni nécessaire;
2. si \(\mathcal RU\neq0\) dans \(\mathcal D'(\mathbb R^3)\), il existe une
   constante réelle \(\alpha\) telle que

   \[
    \theta'(s)=\alpha\quad\text{pour presque tout }s\in I,
    \qquad \theta(s)=\alpha s+\theta_0,           \tag{3}
   \]

   et

   \[
    \mathcal F_\kappa(U)+\alpha\mathcal RU=0.     \tag{4}
   \]

Dans le second cas,

\[
 Z(s+\tau)=Q_{\alpha\tau}Z(s)                   \tag{5}
\]

pour tous les temps admissibles : c'est un équilibre relatif, donc une RSS
exacte dans les variables renormalisées. La phase constante \(\theta_0\)
peut être absorbée dans le profil.

La faille de la formulation abrégée est triple. « Suitable » ne fixe pas à
lui seul une pression globale; une rotation autour d'un centre différent de
l'origine ne commute pas avec le drift; enfin le « soit... soit » n'est pas
logiquement exclusif si l'on omet \(\mathcal RU\neq0\) dans la seconde
branche. Ces corrections n'altèrent pas le cœur du lemme.

## 1. Convention de rotation et signe du générateur

Soit \(A\) une matrice antisymétrique fixe, normalisée de sorte que
\(R_\beta=e^{\beta A}\) soit la rotation d'angle \(\beta\) autour de l'axe
choisi. Pour un champ vectoriel lisse, définissons

\[
 (Q_\beta U)(y)=R_\beta U(R_{-\beta}y).          \tag{6}
\]

Cette convention est celle de l'ansatz
\(Z(s,y)=R_{\theta(s)}U(R_{-\theta(s)}y)\). Sa dérivée en \(\beta=0\) est

\[
 \boxed{
 \mathcal RU=AU-(Ay\cdot\nabla)U.}              \tag{7}
\]

Le signe négatif du transport vient de la variable \(R_{-\beta}y\). Avec
la convention opposée \(R_{-\beta}U(R_\beta y)\), \(\mathcal R\) et
\(\alpha\) changeraient simultanément de signe; l'équilibre relatif serait
le même après renommage.

Pour une distribution vectorielle, (7) se définit par dualité :

\[
 \langle\mathcal RU,\varphi\rangle
 =\langle U,(Ay\cdot\nabla)\varphi-A\varphi\rangle,
 \qquad \varphi\in C_c^\infty(\mathbb R^3)^3.   \tag{8}
\]

En effet, \(\operatorname{div}(Ay)=\operatorname{tr}A=0\). L'application
\(\beta\mapsto Q_\beta U\) est \(C^\infty\) à valeurs dans
\(\mathcal D'\), et

\[
 \frac d{d\beta}Q_\beta U=Q_\beta\mathcal RU.  \tag{9}
\]

Si \(\theta\in W^{1,1}_{\rm loc}(I)\), la règle de chaîne vaut pour chaque
appariement scalaire avec une fonction test, donc

\[
 \partial_s[Q_{\theta(s)}U]
 =\theta'(s)Q_{\theta(s)}\mathcal RU             \tag{10}
\]

dans \(\mathcal D'(I\times\mathbb R^3)\). Aucune dérivée classique de
\(U\) n'est requise pour (10).

## 2. Régularité minimale

Pour que la forme **locale non projetée** soit définie, il suffit pour le
cœur de la classification que

\[
 U\in L^2_{\rm loc}(\mathbb R^3)^3,qquad
 \operatorname{div}U=0,                         \tag{11}
\]

car \(U\otimes U\in L^1_{\rm loc}\), tandis que les termes linéaires et
\(\mathcal RU\) sont des distributions. La forme projetée globale (1)
demande en plus que ces distributions soient tempérées, ou une construction
équivalente de \(\mathbb P\). Dans le cadre actif,

\[
 U\in L^{3,\infty}(\mathbb R^3)
 \subset L^2_{\rm loc}(\mathbb R^3),            \tag{12}
\]

donc (11) est automatique, \(U\otimes U\in L^{3/2,\infty}\), et la
projection de Leray globale est bien définie.

La régularité

\[
 \boxed{\theta\in W^{1,1}_{\rm loc}(I)\text{ suffit.}}      \tag{12a}
\]

En effet, pour chaque test spatial, l'orbite
\(\beta\mapsto\langle Q_\beta U,\varphi\rangle\) est lisse; sa composition
avec une fonction AC est AC et vérifie la règle de chaîne presque partout.
Après intégration contre un test temporel, cela donne (10) dans les
distributions. Ni \(W^{1,\infty}\), ni \(C^1\), ni une dérivée seconde de
\(\theta\) ne sont utilisées.

La suitability est une propriété espace-temps de \(Z\), pas une propriété
isolée d'une distribution spatiale \(U\). Si \(Z\) est faible adaptée locale
et a la forme (2), les rotations de (6) préservent chaque boule centrée en
zéro. Sur tout sous-intervalle \(J\Subset I\) de longueur positive,

\[
 \int_J\int_{B_R}|\nabla Z|^2
 =|J|\int_{B_R}|\nabla U|^2.                    \tag{13}
\]

Ainsi la dissipation locale de \(Z\) donne

\[
 U\in W^{1,2}_{\rm loc}(\mathbb R^3).           \tag{14}
\]

La norme \(L^{3,\infty}\) est exactement invariante sous \(Q_\beta\).
Les propriétés (12)--(14) sont nécessaires aux raccords de Liouville, mais
pas à la réduction algébrique de la phase.

## 3. Équivariance de l'opérateur renormalisé

Les rotations (6) commutent avec le Laplacien et avec la projection de Leray.
Elles transportent exactement le terme quadratique :

\[
 \mathbb P\operatorname{div}
 [(Q_\beta U)\otimes(Q_\beta U)]
 =Q_\beta\mathbb P\operatorname{div}(U\otimes U).          \tag{15}
\]

Le drift est lui aussi invariant, parce que la rotation est linéaire,
orthogonale et centrée à l'origine :

\[
 (1+y\cdot\nabla)Q_\beta U
 =Q_\beta(1+y\cdot\nabla)U.                    \tag{16}
\]

Il en résulte

\[
 \boxed{\mathcal F_\kappa(Q_\beta U)
 =Q_\beta\mathcal F_\kappa(U).}                \tag{17}
\]

Une rotation autour d'un point \(c\neq0\) ne vérifie pas (16) : le champ
\(y\cdot\nabla\) sélectionne l'origine. Un axe ou un centre dépendant du
temps produirait en outre des générateurs supplémentaires. Le lemme ne couvre
aucune de ces modulations.

## 4. Réduction distributionnelle à deux distributions fixes

Par (10) et (17), l'équation de \(Z\) devient formellement

\[
 Q_{\theta(s)}
 [\theta'(s)\mathcal RU+\mathcal F_\kappa(U)]=0.            \tag{18}
\]

Cette écriture est licite sans évaluation ponctuelle de la PDE. En effet, les
deux termes entre crochets appartiennent à
\(L^1_{\rm loc}(I;\mathcal D'_x)\). Une distribution espace-temps de cette
forme qui est nulle est nulle comme distribution spatiale pour presque tout
temps. Comme \(Q_{\theta(s)}\) est inversible, on obtient sur un même ensemble
de temps de mesure pleine

\[
 \boxed{
 \theta'(s)\mathcal RU+\mathcal F_\kappa(U)=0
 \quad\text{dans }\mathcal D'(\mathbb R^3).}     \tag{19}
\]

Pour rendre le « même ensemble » explicite, on choisit une famille
dénombrable dense de tests dans chaque \(C_c^\infty(B_m)\), on intersecte les
ensembles de pleine mesure, puis on utilise la continuité distributionnelle.
Il n'y a pas un ensemble exceptionnel différent laissé pour chaque test.

L'argument ne suppose ni unicité de l'évolution faible, ni différentiabilité
forte dans \(L^{3,\infty}\). Il utilise seulement l'ansatz exact (2), la
phase AC et l'autonomie équivariante de l'équation.

## 5. Classification de la vitesse angulaire

### 5.1 Branche \(\mathcal RU\neq0\)

Puisque \(\mathcal RU\) est une distribution non nulle, il existe un test
\(\varphi_0\in C_c^\infty(\mathbb R^3)^3\) tel que

\[
 c_0=\langle\mathcal RU,\varphi_0\rangle\neq0.  \tag{20}
\]

En testant (19) contre \(\varphi_0\), on trouve pour presque tout \(s\),

\[
 \theta'(s)
 =-\frac{\langle\mathcal F_\kappa(U),\varphi_0\rangle}{c_0}
 =:\alpha.                                      \tag{21}
\]

Le membre droit ne dépend pas du temps. Comme \(I\) est connexe et
\(\theta\) localement absolument continue, le théorème fondamental donne
(3). L'équation (19) devient (4).

La valeur de \(\alpha\) ne dépend pas du test choisi : tout autre test avec
un appariement non nul donne la même valeur parce que la même distribution
(19) s'annule. Si \(\alpha=0\), l'orbite est stationnaire même si sa
représentation utilise un profil sans symétrie continue. Sous les hypothèses
faible-\(L^3\) et \(W^{1,2}_{\rm loc}\), la rigidité de Guevara--Phuc
éliminera ensuite ce sous-cas non trivial; cette élimination n'appartient pas
à la classification abstraite.

### 5.2 Branche \(\mathcal RU=0\)

Par (9),

\[
 \frac d{d\beta}Q_\beta U=0
 \quad\text{dans }\mathcal D'.                  \tag{22}
\]

L'orbite de groupe étant connexe,

\[
 Q_\beta U=U\qquad\text{pour tout }\beta\in\mathbb R.      \tag{23}
\]

La phase \(\theta(s)\) peut donc être arbitraire dans
\(W^{1,1}_{\rm loc}\), mais (2) donne toujours \(Z(s)=U\). L'équation (19)
impose alors \(\mathcal F_\kappa(U)=0\). Tenter de conclure que
\(\theta'\) est constante dans cette branche serait une erreur
d'identifiabilité : la phase est une jauge redondante.

## 6. Stabilisateur non trivial

Définissons le stabilisateur dans le cercle de rotations :

\[
 H_U=\{\beta\in\mathbb R/(2\pi\mathbb Z):Q_\beta U=U\}.    \tag{24}
\]

La continuité de l'action rend \(H_U\) fermé. Les sous-groupes fermés du
cercle sont soit le cercle entier, soit un groupe cyclique fini.

- \(H_U=S^1\) si et seulement si \(\mathcal RU=0\). C'est la branche
  axisymétrique relativement à l'axe fixé; \(Z\) est stationnaire quelle que
  soit la phase.
- Si \(H_U=C_m\) est fini et non trivial, alors \(\mathcal RU\neq0\). Le
  profil et la phase sont définis modulo \(2\pi/m\), mais cela ne permet pas
  une vitesse variable. Deux relèvements AC d'une même orbite diffèrent par
  une fonction continue à valeurs dans le groupe discret \(C_m\); cette
  fonction est constante sur \(I\). Leur dérivée et donc \(\alpha\) sont les
  mêmes.

Une suite de sauts entre éléments du stabilisateur fini pourrait masquer une
phase variable si aucune continuité n'était imposée. Elle est exclue par
\(\theta\in W^{1,1}_{\rm loc}\). C'est l'une des raisons pour lesquelles
l'hypothèse AC ne doit pas être remplacée par une phase seulement mesurable.

## 7. Pression et projection de Leray

Si la pression est fixée par la jauge globale

\[
 P_U=R_iR_j(U_iU_j),                             \tag{25}
\]

alors la pression de \(Q_\beta U\) est le scalaire tourné

\[
 P_{Q_\beta U}(y)=P_U(R_{-\beta}y).             \tag{26}
\]

Les doubles transformées de Riesz commutent avec les rotations. L'équation
de profil non projetée dans la seconde branche est donc

\[
 -\Delta U+\operatorname{div}(U\otimes U)+\nabla P_U
 +\kappa(1+y\cdot\nabla)U+\alpha\mathcal RU=0.  \tag{27}
\]

Dans la première branche, il suffit de poser \(\alpha=0\). Une pression
locale définie modulo une fonction du temps ne change pas (27), car son
gradient est nul. En revanche, une composante harmonique spatiale sans
contrôle global n'est pas éliminée par le mot « suitable ». Le lemme doit
alors être formulé directement pour l'équation projetée (1), ou accompagné
d'une hypothèse assurant que la pression donnée coïncide avec (25) modulo une
fonction du temps.

Avec \(U\in L^{3,\infty}\), on a
\(U\otimes U,P_U\in L^{3/2,\infty}\). La projection est bien définie sur
ces distributions tempérées. Dans les formulations faibles, on peut aussi
tester uniquement contre des champs solénoïdaux compacts; aucune intégration
globale illégitime de la pression n'est alors requise.

## 8. Notion exacte de RSS

Après absorption de \(\theta_0\), la seconde branche s'écrit

\[
 Z(s,y)=R_{\alpha s}U(R_{-\alpha s}y).           \tag{28}
\]

L'identité (5) montre que c'est une symétrie relative exacte pour tout
incrément de temps, et non :

- une récurrence le long d'une suite;
- une orbite seulement asymptotiquement RSS;
- une RDSS, qui autoriserait en plus une période non nulle dans un quotient;
- une rotation à axe mobile;
- une modulation de phase lente avec \(\theta''\neq0\).

Le profil (27) est l'équation elliptique RSS correspondant à notre convention
de signe. Sous la dilatation critique

\[
 \lambda=\sqrt{2\kappa},\qquad
 U(y)=\lambda V(\lambda y),                     \tag{29}
\]

elle devient

\[
 -\Delta V+\operatorname{div}(V\otimes V)+\nabla Q
 +\frac12(1+x\cdot\nabla)V
 +\omega\mathcal RV=0,
 \qquad \omega=\frac{\alpha}{2\kappa}.          \tag{30}
\]

La norme \(L^{3,\infty}\) est préservée. Le signe de \(\omega\) doit être
comparé à la convention de rotation de chaque source; les régimes fondés sur
\(|\omega|\) ne sont pas affectés.

## 9. Raccord conditionnel à Guevara--Phuc

Dans la première branche, ou dans la seconde avec \(\alpha=0\), le profil
satisfait l'équation stationnaire de Leray sans terme rotationnel. Si

\[
 U\in W^{1,2}_{\rm loc}(\mathbb R^3)
 \cap L^{3,\infty}(\mathbb R^3),                \tag{31}
\]

la dilatation (29) rejoint exactement la normalisation du théorème 1.3 de
Guevara--Phuc, *SIAM J. Math. Anal.* 50 (2018), 541--556, DOI
`10.1137/16M110099X`. Le cas \(q=3\in(12/5,6)\) donne

\[
 U=0.                                            \tag{32}
\]

Ainsi, sous capture persistante non triviale, la branche
\(\mathcal RU=0\) et le sous-cas \(\alpha=0\) sont exclus. Guevara--Phuc ne
s'applique pas à (30) lorsque \(\omega\neq0\) : traiter le terme
\(\omega\mathcal RV\) comme nul ou comme une pression serait une fausse
extension du théorème.

## 10. Raccord conditionnel à Pineau--Vicol

Le second cas produit exactement le type d'équilibre relatif RSS considéré
par Pineau--Vicol, `arXiv:2607.09619v2`, après accord des conventions et de la
normalisation (30). Leur prépublication exclut les profils RSS dans des
régimes de vitesse de rotation suffisamment petite ou suffisamment grande,
avec seuils dépendant de la constante Type I.

Ce raccord exige toutefois des hypothèses qui ne suivent pas du lemme :

1. une solution/profil de la régularité classique demandée dans la source;
2. surtout une borne Type I ponctuelle du type

   \[
    |u(x,t)|\leq\frac{C_*}{|x|+\sqrt{-t}},       \tag{33}
   \]

   ou sa forme exacte pour le profil;
3. le régime quantitatif petit ou grand de \(|\omega|\) prescrit en fonction
   de \(C_*\);
4. un ansatz backward RSS exact sur le domaine temporel de la source.

La borne \(U\in L^{3,\infty}\) est une conséquence de (33), mais la
réciproque est fausse. Le faible-\(L^3\) permet concentrations et
intermittence sans majorant ponctuel. Par conséquent,

\[
 \text{classification RSS faible-}L^3
 \not\Longrightarrow
 \text{hypothèses de Pineau--Vicol}.             \tag{34}
\]

Même si un bootstrap elliptique local de (27) fournit la régularité locale du
profil depuis (14), il ne crée pas la décroissance ponctuelle globale (33).
Les rotations intermédiaires restent en outre hors des régimes exclus par la
prépublication. Le statut de cette dernière demeure `PREPRINT_CLAIM`, non
`PAPER_PROOF`.

## 11. Passe contradictoire

1. **Signe de \(\mathcal R\).** Pour l'action (6), le générateur est
   \(AU-(Ay\cdot\nabla)U\). Un signe positif devant le transport correspond
   à l'action inverse.
2. **Pression locale.** La suitability seule n'identifie pas une jauge
   globale. Utiliser (1) requiert la pression de Riesz ou une formulation
   projetée explicitement admise.
3. **Origine du drift.** Une rotation non centrée en zéro ne commute pas avec
   \(y\cdot\nabla\); le défaut est un transport spatial supplémentaire.
4. **Phase seulement mesurable.** Sans AC, la règle de chaîne (10) échoue et
   des sauts dans un stabilisateur fini peuvent être invisibles dans \(Z\).
5. **Ensemble exceptionnel.** Le passage à (19) doit utiliser une famille
   dénombrable dense de tests pour obtenir un ensemble de temps commun.
6. **Division par une distribution.** On ne divise pas formellement par
   \(\mathcal RU\). On choisit un test unique \(\varphi_0\) tel que (20), ce
   qui produit le scalaire (21).
7. **Stabilisateur continu.** Si \(\mathcal RU=0\), une phase non affine est
   compatible avec la PDE parce que le champ ne bouge pas. Conclure
   \(\theta'=\alpha\) dans cette branche serait faux comme assertion sur le
   paramétrage.
8. **Stabilisateur fini.** Une symétrie d'ordre \(m\) ne permet pas une
   modulation AC; elle ne change que la phase constante modulo \(2\pi/m\).
9. **Stationnaire contre RSS.** \(\alpha=0\) dans la branche
   \(\mathcal RU\neq0\) donne une trajectoire stationnaire. Le mot RSS peut
   l'inclure comme vitesse nulle, mais Guevara--Phuc la réduit à zéro sous
   (31).
10. **Guevara--Phuc.** Leur théorème ne contient pas le terme
    \(\omega\mathcal R U\). Il ne ferme aucune RSS tournante non nulle.
11. **Pineau--Vicol.** Faible-\(L^3\) ne fournit ni la borne Type I
    ponctuelle, ni les seuils de rotation extrêmes. Le transfert reste
    conditionnel.
12. **Orbites approchées.** Si
    \(Z-Q_{\theta(s)}U\to0\) seulement asymptotiquement, (19) acquiert un
    résidu. Le lemme exact ne donne aucune stabilité quantitative de la
    classification.
13. **Portée Clay.** L'ansatz (2) est une hypothèse structurelle très forte.
    Rien ici ne montre qu'une limite de blow-up Clay appartient à une orbite
    de rotation d'un profil fixe.

## 12. Statut logique

| Implication | Statut |
|---|---|
| action (6) + phase AC \(\Rightarrow\) règle de chaîne (10) | **PROUVÉ** dans \(\mathcal D'\) |
| autonomie et rotation centrée \(\Rightarrow\) équivariance (17) | **PROUVÉ** |
| ansatz exact + PDE projetée \(\Rightarrow\) identité (19) | **PROUVÉ** |
| \(\mathcal RU\neq0\Rightarrow\theta'=\alpha\) p.p. | **PROUVÉ**, par un test non nul |
| \(\mathcal RU=0\Rightarrow Q_\beta U=U\) et \(Z\) stationnaire | **PROUVÉ** |
| stabilisateur fini \(\Rightarrow\) liberté de vitesse angulaire | **RÉFUTÉ** sous phase AC; seule une phase constante modulo le stabilisateur subsiste |
| branche stationnaire + (31) \(\Rightarrow U=0\) | **SOURCE_VERIFIED**, Guevara--Phuc |
| branche RSS + faible-\(L^3\) \(\Rightarrow U=0\) | **NON DÉMONTRÉ** pour rotation générale |
| branche RSS + hypothèses Type I et rotation extrême de la source \(\Rightarrow U=0\) | **PREPRINT_CLAIM conditionnel**, Pineau--Vicol v2 |
| classification d'orbite \(\Rightarrow\) toute limite Type I est BSS/RSS | **NON DÉMONTRÉ** |
| classification \(\Rightarrow\) résolution Clay | **NON DÉMONTRÉ** |

**Décision analytique : CONTINUER.** Le lemme ferme exactement la
classification des orbites contenues dans une unique orbite de rotation d'un
profil fixe : elles sont stationnaires ou RSS à vitesse constante. Le verrou
suivant n'est plus cinématique. Il faut soit produire cet ansatz exact depuis
la PDE, soit contrôler quantitativement le résidu d'une orbite modulée, soit
étendre une rigidité RSS au faible-\(L^3\) dans le régime de rotation
intermédiaire. Aucun de ces trois raccords n'est obtenu ici.
