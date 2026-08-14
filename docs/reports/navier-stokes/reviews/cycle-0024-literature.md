# Cycle 0024 — veille primaire : log-BMO, zéros et axes moyens

Date de coupure : **2026-08-14**.

Périmètre : direction de vorticité dans `BMO`, `VMO` et
\(\mathrm{bmo}_{1/|\log r|}\), convention sur l'ensemble des zéros,
prolongement depuis l'ensemble actif, non-dégénérescence des moyennes,
et raccords possibles avec les critères de Bradshaw–Grujić, Grujić,
Lei–Ren–Tian et Miller.

Type de revue : veille bibliographique différentielle sur sources primaires,
complétée par une dérivation élémentaire du laboratoire clairement séparée
des résultats publiés. Cette revue est produite par la même famille de modèle
que l'agent principal et n'est pas une reproduction indépendante des preuves.

## Verdict différentiel

La recherche primaire ne trouve **aucun théorème** réalisant le raccord

\[
 \xi=\frac{\omega}{|\omega|}\text{ sur }\{|\omega|>0\}
 \quad\Longrightarrow\quad
 \exists\,\Xi:\mathbb R^3\to\mathbb S^2,
 \quad \Xi=\xi\text{ sur }\{|\omega|>0\},
 \quad \Xi\in\mathrm{bmo}_{1/|\log r|},
\tag{V1}
\]

avec constante uniforme en temps. Les théorèmes d'extension de Jones et leurs
variantes portent sur des fonctions vectorielles dans un **domaine uniforme** ;
ils ne prolongent pas une donnée sur un ensemble actif arbitraire, ne
préservent pas la contrainte \(\mathbb S^2\), et ne produisent pas la
pondération logarithmique voulue.

La veille apporte en revanche une correction positive au cycle 0023. Si le
champ global \(\Xi\) de (V1) est **déjà donné et unitaire presque partout**,
alors ses moyennes sur les petites balles ne peuvent pas s'annuler : la petite
oscillation moyenne force quantitativement leur norme vers \(1\). On obtient
donc un axe normalisé local et un confinement en mesure. Ce fait est une
identité élémentaire, pas un théorème Navier–Stokes nouveau.

Ce gain ne ferme aucun critère connu :

- l'axe moyen peut encore dériver de \(O(1/k)\) entre échelles dyadiques, série
  non sommable ;
- la BMO donne un cône **hors d'un ensemble de petite mesure**, tandis que
  Lei–Ren–Tian demande un cône ponctuel sur tous les grands niveaux ;
- elle ne donne ni \(\nabla v\in L^\infty\) ni
  \(v\times\omega\in L^4_tL^2_x\), requis par Miller ;
- surtout, l'existence d'un prolongement global unitaire aux zéros reste une
  hypothèse supplémentaire non intrinsèque à \(\omega\).

Le transfert exact est donc :

\[
 \boxed{\text{log-BMO global + unitarité}}
 \Longrightarrow
 \boxed{\text{axes locaux non dégénérés, cohérents en mesure}}
 \not\Longrightarrow
 \boxed{\text{axe fixe, cône ponctuel ou critère de prolongement}}.
\tag{V2}
\]

## 1. Équation et échelle fixées

Les résultats globaux sont comparés à Navier–Stokes incompressible non forcé
sur \(\mathbb R^3\), viscosité normalisée à \(1\) :

\[
 \partial_tu-\Delta u+(u\cdot\nabla)u+\nabla p=0,
 \qquad \nabla\cdot u=0,
 \qquad \omega=\nabla\times u.
\tag{NS}
\]

La remise à l'échelle est

\[
 u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),
 \qquad
 \omega_\lambda(x,t)=\lambda^2\omega(\lambda x,\lambda^2t).
\]

La direction \(\xi\) est sans dimension, mais n'est définie par ce quotient
que sur

\[
 A(t)=\{x:\ |\omega(x,t)|>0\},
 \qquad Z(t)=\mathbb R^3\setminus A(t).
\]

La norme faible \(L^{3/2}\) de la vorticité et la norme
\(L^4_tL^2_x\) de \(v\times\omega\) sont critiques. La seminorme BMO usuelle
est invariante par dilatation, tandis que la norme locale pondérée avec
\(\phi(r)=1/|\log r|\) est attachée à une échelle de référence
(``\(r<1/2\)'') et n'est pas une loi de puissance exactement homogène.

Une donnée Clay lisse de Schwartz donne, avant son temps maximal, une solution
classique et mild ; localement, elle entre aussi dans la classe des solutions
faibles adaptées. Cela autorise l'application **conditionnelle** des critères
ci-dessous, mais l'énergie ne produit aucune de leurs hypothèses géométriques.

## 2. Statuts et versions vérifiés

| Source primaire | Statut au 2026-08-14 | Objet exact pertinent |
|---|---|---|
| Zachary Bradshaw et Zoran Grujić, [*A spatially localized \(L\log L\) estimate on the vorticity in the 3D NSE*](https://arxiv.org/abs/1309.2519), arXiv v5 du 7 février 2014 | publié, *Indiana Univ. Math. J.* **64** (2015), 433–440, [DOI 10.1512/iumj.2015.64.5496](https://doi.org/10.1512/iumj.2015.64.5496) | solution de Leray sur \(\mathbb R^3\), \(\omega_0\in L^1\cap L^2\), hypothèse uniforme sur \(\psi\xi\in\widetilde{\mathrm{bmo}}_{1/|\log r|}\), conclusion locale \(L\log L\) |
| Zoran Grujić, [*Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier-Stokes Equations*](https://arxiv.org/abs/2607.08866), v2 du 13 juillet 2026 | prépublication v2, aucune référence de revue indiquée | scénario de premier temps singulier ponctuel critique, \(\omega\in L^\infty_tL^{3/2,\infty}_x\), direction globale dans \(\mathrm{bmo}_{1/|\log r|}\), exclusion conditionnelle revendiquée |
| Zhen Lei, Xiao Ren et Gang Tian, [*A Geometric Characterization of Potential Navier-Stokes Singularities*](https://arxiv.org/abs/2501.08976), v1 du 15 janvier 2025 | prépublication v1, aucune référence de revue indiquée | solution faible adaptée locale dans \(Q(1)\), double cône sur la forte vorticité et critère pairwise sur toute vorticité non nulle |
| Evan Miller, [*A Locally Anisotropic Regularity Criterion for the Navier–Stokes Equation in Terms of Vorticity*](https://arxiv.org/abs/2002.02152), arXiv v1 du 6 février 2020 | publié, *Proc. Amer. Math. Soc. Ser. B* **8** (2021), 60–74, [DOI 10.1090/bproc/74](https://doi.org/10.1090/bproc/74) | solution mild \(H^1(\mathbb R^3)\), champ unitaire auxiliaire global \(v\), gradient spatial borné et contrôle critique de \(v\times\omega\) |
| Peter W. Jones, [*Extension Theorems for BMO*](https://iumj.org/article/2860/) | publié, *Indiana Univ. Math. J.* **29** (1980), 41–66, [DOI 10.1512/iumj.1980.29.29005](https://doi.org/10.1512/iumj.1980.29.29005) | extension BMO depuis les domaines uniformes, composante par composante |
| Almaz Butaev et Galia Dafni, [*On the extension of VMO functions*](https://arxiv.org/abs/1809.01049), v1 du 4 septembre 2018 | prépublication v1 ; aucune référence de revue indiquée sur la fiche arXiv | extension linéaire \(\mathrm{VMO}(\Omega)\to\mathrm{VMO}(\mathbb R^n)\) pour domaine uniforme, bornée dans la norme BMO |
| Zhongyang Gu, [*Extension theorem for \(bmo\) in a domain*](https://arxiv.org/abs/2310.18889), v1 du 29 octobre 2023 | prépublication v1, aucune référence de revue indiquée | extension du `bmo` local depuis un domaine uniformément \(C^2\) |

Aucune version postérieure de Grujić v2 ou Lei–Ren–Tian v1 n'apparaît dans
leurs historiques arXiv à la date de coupure. Aucune page secondaire n'est
utilisée pour établir un énoncé.

## 3. Où les zéros entrent dans les quatre critères

### 3.1 Bradshaw–Grujić 2015 : norme globale, convention non énoncée

La source pose

\[
 \xi=\frac{\omega}{|\omega|}
\]

et suppose au théorème 1

\[
 \sup_{0<t<T}\|\psi\xi(\cdot,t)\|_{
 \widetilde{\mathrm{bmo}}_{1/|\log r|}}<\infty.
\tag{3.1}
\]

Ici la norme comprend un ancrage \(L^1\) et la moyenne d'oscillation sur tous
les petits cubes de \(\mathbb R^3\). Le texte primaire ne donne pas de valeur
de \(\xi\) sur \(Z(t)\). Les termes de stretching de la preuve sont
insensibles à cette valeur lorsqu'ils sont multipliés par \(\omega\), mais
la propriété (3.1), prise isolément, peut changer avec le prolongement choisi
sur les zéros.

Le résultat exact est donc lisible sans ambiguïté sous la forme existentielle :
il existe un champ mesurable \(\Xi(\cdot,t)\) prolongeant \(\xi\) hors des
zéros et tel que \(\psi\Xi\) satisfasse (3.1). La source ne démontre pas
l'existence de ce prolongement depuis des données portant seulement sur
\(A(t)\). Sa conclusion est une borne locale \(L\log L\) sur la vorticité,
pas à elle seule la régularité globale Clay.

### 3.2 Grujić 2026 : unitarité globale utilisée, zéros non spécifiés

La définition (2) de la v2 est globale en espace :

\[
 \|f\|_{\mathrm{bmo}_\phi}
 =\|f\|_\infty+
 \sup_{x,,0<r<1/2}\frac1{\phi(r)}
 \fint_{B_r(x)}|f-f_{B_r(x)}|.
\tag{3.2}
\]

Le texte justifie \(\|\xi\|_\infty=1\) par le fait que la direction est un
champ unitaire. Pourtant \(\omega/|\omega|\) n'est pas défini sur \(Z(t)\),
et ni la définition ni le théorème 4.1 n'énoncent de convention sur cet
ensemble. La formulation mathématique robuste de l'hypothèse est donc

\[
 \exists\,\Xi:\mathbb R^3\to\mathbb S^2,
 \quad \Xi=\omega/|\omega|\ \text{p.p. sur }A(t),
 \quad
 \sup_t\|\Xi(\cdot,t)\|_{\mathrm{bmo}_\phi}<\infty.
\tag{3.3}
\]

Le passage de la restriction à une balle à une fonction BMO globale dans la
preuve du théorème 4.1 intervient **après** (3.3). Le théorème de Jones y
prolonge la restriction d'un champ déjà défini sur toute la balle ; il ne
construit pas (3.3) depuis \(A(t)\).

En outre, ce prolongement analytique n'est utilisé que comme symbole BMO pour
un commutateur. Jones ne garantit pas qu'il reste dans \(\mathbb S^2\). Cela
ne gêne pas nécessairement l'étape de commutateur, mais interdit d'utiliser ce
prolongement de Jones comme réponse au problème géométrique des zéros ou
comme axe unitaire.

### 3.3 Lei–Ren–Tian 2025 : convention aux zéros évitée

La source précise que \(\xi=\omega/|\omega|\) est bien défini lorsque
\(|\omega|\ne0\). Son théorème 1.1 n'évalue \(\xi\) que lorsque
\(|\omega|>M\). Son corollaire 1.6 impose

\[
 |\xi(x,t)\times\xi(y,t)|<1-\delta
\tag{3.4}
\]

pour des paires à temps égal satisfaisant
\(|\omega(x,t)|\,|\omega(y,t)|\ne0\). Dans la preuve, si
\(\omega(\cdot,t)\equiv0\), un axe arbitraire est choisi et l'inégalité
requise est triviale. Le critère est donc intrinsèque à \(\omega\) et ne
dépend pas d'une convention sur \(Z(t)\).

Cette robustesse ne fournit toutefois aucun raccord depuis BMO : le théorème
1.1 veut un double cône fixe à **tous** les points de forte vorticité, et le
corollaire 1.6 veut (3.4) sur **toute** la vorticité non nulle. Un contrôle en
moyenne avec un petit ensemble exceptionnel ne suffit pas.

### 3.4 Miller 2021 : champ auxiliaire, pas direction canonique

Le théorème 1.6 de Miller prend comme donnée un champ indépendant

\[
 v:\mathbb R^3\times[0,\infty)\to\mathbb S^2,
 \qquad
 \nabla_xv\in L^\infty_{\mathrm{loc},t}L^\infty_x,
\]

et donne une borne de \(\|u(t)\|_{\dot H^1}\) en fonction de
\(\|\nabla v\|_\infty\) et de
\(\int\|v\times\omega\|_2^4dt\). Comme
\(v\times\omega=0\) sur \(Z(t)\), l'intégrande critique ne demande aucune
direction de vorticité aux zéros.

Mais si l'on tente de prendre \(v=\xi\) sur \(A(t)\), la condition globale
sur \(\nabla_xv\) dépend fortement du prolongement dans \(Z(t)\). Une
extension log-BMO n'implique pas un gradient borné ; un axe radial de phase
\(\log\log(e/r)\) a typiquement
\(|\nabla v|\simeq1/(r\log(e/r))\). Miller contourne donc la canonicité des
zéros, sans fournir le pont log-BMO \(\to\) champ admissible dans son critère.

## 4. Audit des théorèmes d'extension

Le théorème de Jones donne un opérateur d'extension BMO pour un domaine
uniforme. Butaev–Dafni fournit l'analogue VMO, et Gu une version `bmo` locale
sur un domaine uniformément \(C^2\). Ces résultats sont précieux pour
localiser un commutateur sur une balle, mais leurs quantificateurs ne
correspondent pas à (V1) :

1. \(A(t)=\{|\omega|>0\}\) ou un superniveau de \(|\omega|\) n'est pas en
   général un domaine ouvert, connexe et uniforme avec constantes contrôlées ;
2. l'opérateur agit sur des fonctions à valeurs dans un espace vectoriel ;
   appliqué composante par composante, il ne préserve ni \(|\Xi|=1\) ni même
   une borne inférieure ponctuelle sur \(|\Xi|\) ;
3. Jones contrôle la BMO non pondérée ; Butaev–Dafni contrôle le module VMO
   après extension mais ne donne pas le module précis
   \(C/|\log r|\) requis ici ;
4. aucun de ces théorèmes n'impose une trace prescrite sur un ensemble actif
   arbitraire ni une constante uniforme pour une géométrie active évoluant en
   temps ;
5. normaliser l'extension vectorielle par \(F/|F|\) n'est légitime que si
   \(|F|\) reste ponctuellement séparé de zéro, propriété que BMO ne fournit
   pas.

La théorie de Brezis–Nirenberg sur le degré des applications VMO à valeurs
dans une variété compacte
([partie I](https://doi.org/10.1007/BF01671566),
[partie II](https://doi.org/10.1007/BF01587948)) permet de donner un sens
topologique à certaines applications VMO déjà définies. Elle ne fournit pas
non plus un opérateur de prolongement depuis \(A(t)\) vers un champ
\(\mathbb S^2\)-valué satisfaisant (3.3).

**Résultat négatif de veille :** aucune source primaire trouvée ne bouche le
maillon « direction seulement active \(\to\) prolongement global unitaire
log-BMO avec constante uniforme ».

## 5. Lemme élémentaire du laboratoire : BMO unitaire vers axe moyen

Cette section est une dérivation nouvelle du laboratoire ; son statut n'est
ni `PAPER_PROOF` ni résultat Navier–Stokes.

Soit \(B\subset\mathbb R^3\) une balle et
\(\Xi:B\to\mathbb S^2\) mesurable. Posons

\[
 m_B=\fint_B\Xi,
 \qquad
 \varepsilon_B=\fint_B|\Xi-m_B|.
\]

Alors l'identité exacte

\[
 \fint_B|\Xi-m_B|^2=1-|m_B|^2
\tag{5.1}
\]

et la borne \(|\Xi-m_B|\le2\) donnent

\[
 1-|m_B|^2\le2\varepsilon_B,
 \qquad
 |m_B|\ge\sqrt{\max(0,1-2\varepsilon_B)}.
\tag{5.2}
\]

Par conséquent, si

\[
 \fint_{B_r(x)}|\Xi-(\Xi)_{B_r(x)}|
 \le \frac K{|\log r|},
\tag{5.3}
\]

alors toute balle assez petite pour que
\(K/|\log r|\le3/8\) possède une moyenne de norme au moins \(1/2\).
L'axe

\[
 e_{B_r(x)}=\frac{(\Xi)_{B_r(x)}}{|(\Xi)_{B_r(x)}|}
\tag{5.4}
\]

est donc bien défini. De plus,

\[
 \fint_B|\Xi-e_B|
 \le \varepsilon_B+(1-|m_B|)
 \le3\varepsilon_B,
\tag{5.5}
\]

et, pour tout \(\delta>0\),

\[
 \frac{|\{y\in B:\ |\Xi(y)\times e_B|>\delta\}|}{|B|}
 \le \frac{3\varepsilon_B}{\delta}.
\tag{5.6}
\]

Ainsi la log-BMO **globale unitaire** donne bien un cône local dont la
fraction exceptionnelle décroît comme \(1/|\log r|\).

Pour deux balles concentriques \(B_{r/2}\subset B_r\),

\[
 |m_{r/2}-m_r|
 \le \frac{|B_r|}{|B_{r/2}|}\,
 \fint_{B_r}|\Xi-m_r|
 \le 8\varepsilon_{B_r}.
\tag{5.7}
\]

Si \(|m_r|,|m_{r/2}|\ge m_0>0\), la normalisation donne

\[
 |e_{r/2}-e_r|
 \le \frac{16}{m_0}\varepsilon_{B_r}.
\tag{5.8}
\]

Aux rayons \(r_k=2^{-k}\), (5.3) implique donc

\[
 |e_{k+1}-e_k|\lesssim\frac{K}{m_0k},
 \qquad
 |e_n-e_m|\lesssim\frac{K}{m_0}\log\frac nm.
\tag{5.9}
\]

La dérive par pas tend vers zéro, mais n'est pas sommable. Un axe peut tourner
indéfiniment. Le champ radial unitaire

\[
 \Xi(x)=\bigl(\cos(\log\log(e/|x|)),
                  \sin(\log\log(e/|x|)),0\bigr)
\tag{5.10}
\]

réalise précisément ce comportement : log-BMO local, moyennes petites-échelles
non dégénérées, mais absence d'axe limite et image limite égale à un grand
cercle. Ce contre-profil fonctionnel ne construit pas une vorticité
solénoïdale ni une solution de (NS).

### Rectification explicite du cycle 0023

La phrase du cycle 0023 selon laquelle les moyennes dyadiques « peuvent
s'annuler » était trop large. Elle est fausse aux échelles assez petites sous
les deux hypothèses simultanées :

1. \(\Xi\) est défini sur toute la balle et \(|\Xi|=1\) presque partout ;
2. son oscillation moyenne tend uniformément vers zéro.

Elle reste pertinente si l'on moyenne un prolongement non unitaire, si l'on
pose \(\Xi=0\) sur les zéros, ou si l'on ne contrôle que des morceaux actifs
sans raccord global.

En effet, pour le prolongement nul
\(F=\xi\mathbf1_A\), on a seulement

\[
 \fint_B|F-m_B|^2
 =\fint_B|F|^2-|m_B|^2,
\tag{5.11}
\]

et le premier terme est la fraction active lorsque \(|\xi|=1\) sur \(A\).
Si \(F=e\mathbf1_A\) et \(|A\cap B|/|B|=\theta\), alors

\[
 |m_B|=\theta,
 \qquad
 \fint_B|F-m_B|=2\theta(1-\theta).
\tag{5.12}
\]

Une petite oscillation provenant d'une fraction active \(\theta\ll1\) ne
donne donc aucune non-dégénérescence. À l'inverse, à une interface de densité
\(\theta=1/2\), l'oscillation reste \(1/2\) à toutes les échelles et le
prolongement par zéro n'est pas log-BMO. Cette alternative montre pourquoi
la densité et la géométrie de \(A(t)\) ne peuvent être omises.

## 6. Comparaison exacte avec les critères de régularité

| Hypothèse disponible | Conclusion valide | Ce qui manque pour le critère suivant |
|---|---|---|
| \(\Xi\) global, unitaire et uniformément log-BMO | axes moyens (5.4), non-dégénérescence (5.2), cône en mesure (5.6), dérive dyadique (5.9) | existence/canonicité de \(\Xi\) aux zéros ; contrôle ponctuel des exceptions |
| Bradshaw–Grujić (3.1) | borne locale uniforme \(L\log L\) sur \(|\omega|\) | la conclusion seule n'est pas un critère Clay ; hypothèse non produite par l'énergie |
| hypothèses complètes de Grujić v2, dont (3.3) et profil critique | exclusion conditionnelle revendiquée du scénario ponctuel décrit | prépublication ; scénario et bornes critiques non dérivés du cadre Clay général |
| double cône fixe sur tous les points où \(|\omega|>M\) | régularité locale par Lei–Ren–Tian, théorème 1.1 | (5.6) n'élimine pas le petit ensemble exceptionnel et l'axe dépend de la balle |
| cohérence pairwise sur tous les points où \(|\omega|\ne0\) | régularité au point par Lei–Ren–Tian, corollaire 1.6 | log-BMO ne contrôle pas ponctuellement toutes les petites vorticités |
| \(v\) unitaire global, \(\nabla_xv\in L^\infty\), \(v\times\omega\in L^4_tL^2_x\) | prolongement de la solution mild par Miller | axes (5.4) seulement mesurables/inter-échelles ; aucune borne de gradient ni intégrabilité transverse |

La proximité la plus forte est (5.6), mais elle est strictement insuffisante
pour Lei–Ren–Tian. Même avec une fraction exceptionnelle tendant vers zéro,
le champ (5.10) contient, au fond de chaque balle centrée au cœur, des
directions séparées d'un angle macroscopique. Les quantificateurs « presque
partout en mesure » et « pour tout point de grand niveau » ne sont pas
interchangeables.

## 7. Convention recommandée pour les affirmations du laboratoire

Toute affirmation utilisant une norme de la direction sur tout l'espace
devrait désormais spécifier l'un des trois objets suivants :

1. **direction active intrinsèque** : \(\xi:A(t)\to\mathbb S^2\), sans norme
   globale tant qu'une mesure et une géométrie sur \(A(t)\) ne sont pas fixées ;
2. **prolongement unitaire existentiel** : un \(\Xi\) satisfaisant (3.3), avec
   quantificateur \(\exists\) explicite ;
3. **prolongement nul** : \(F=\omega/|\omega|\) sur \(A(t)\) et \(F=0\) sur
   \(Z(t)\), donc \(|F|\le1\), sans invoquer les conséquences propres aux
   champs unitaires.

Une formulation disant simplement
« \(\omega/|\omega|\in\mathrm{bmo}_\phi(\mathbb R^3)\) » est insuffisamment
spécifiée dès que \(|Z(t)|>0\). Le choix existentiel est le plus proche des
preuves de Bradshaw–Grujić et Grujić ; le choix actif est le plus proche de
Lei–Ren–Tian ; Miller utilise un champ auxiliaire qui n'est pas canonique.

## 8. Transfert exact vers le problème Clay

Le seul nouveau maillon validé dans cette revue est purement fonctionnel :

\[
 \begin{aligned}
 &\exists\,\Xi\in L^\infty_t
 \mathrm{bmo}_{1/|\log r|}(\mathbb R^3;\mathbb S^2),
 \quad \Xi=\omega/|\omega|\text{ sur }A(t) \\
 &\hspace{2cm}\Longrightarrow
 \text{moyennes non nulles aux petites échelles et axes }e_{B_r}
 \text{ satisfaisant (5.6)–(5.9)}.
 \end{aligned}
\tag{8.1}
\]

Il ne donne pas :

- l'existence de \(\Xi\) à partir d'une solution de Leray–Hopf ou d'une
  donnée Clay ;
- un axe unique ou convergent ;
- un double cône ponctuel sur les grands niveaux ;
- un contrôle de la pression, de l'étirement ou de la quantité de Miller ;
- une exclusion générale des blow-ups Type I ou Type II.

La chaîne transférable reste donc conditionnelle : une solution Clay qui
satisfait **déjà** les hypothèses exactes d'un critère publié/prépublié entre
dans sa conclusion. Aucune source primaire ne montre que l'énergie, la
divergence nulle ou la dynamique de (NS) impose (3.3).

## 9. Décision scientifique

- **Résultat positif :** le verrou « moyenne possiblement nulle » disparaît
  une fois supposé un prolongement global réellement \(\mathbb S^2\)-valué ;
  les constantes sont explicites dans (5.2), (5.6) et (5.8).
- **Résultat négatif :** aucun théorème d'extension primaire ne fournit ce
  prolongement depuis l'ensemble actif, et aucun critère de régularité ne se
  déclenche avec le seul cône en mesure (5.6).
- **Attaque adverse :** le prolongement nul (5.12) détruit la
  non-dégénérescence lorsque la densité active décroît ; le champ radial
  (5.10) conserve l'unitarité et la log-BMO mais détruit l'axe limite et le
  cône ponctuel fixe.
- **Écart Clay :** la géométrie et la densité des zéros/superniveaux ne sont
  pas contrôlées uniformément par les estimations de Leray–Hopf.
- **Statut :** **CONTINUER**, mais déplacer le lemme actif de
  « non-dégénérescence des moyennes globales » vers
  « prolongement unitaire contrôlé depuis l'ensemble actif » ou vers un
  critère directement formulé avec exceptions pondérées par \(|\omega|\).
- **Prochaine expérience décisive :** tester sur des champs solénoïdaux
  multi-échelles si une petite mesure exceptionnelle dans (5.6) peut porter
  une fraction non petite de l'enstrophie ou du stretching. Si oui, abandonner
  tout raccord BMO \(\to\) Lei–Ren–Tian fondé seulement sur la mesure de
  Lebesgue ; si non, formuler la borne pondérée minimale exacte.
