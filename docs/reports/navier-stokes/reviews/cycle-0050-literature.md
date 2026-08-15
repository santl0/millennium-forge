# Cycle 0050 — cocycle calorique, quotient faible-\(L^3\) et passé ancien

**Date de coupure :** 15 août 2026

**Nature :** veille bibliographique primaire ciblée et passe contradictoire
indépendante

**Question auditée :** les scissions calorifiques construites séparément sur
les fenêtres finies d'une solution ancienne uniformément bornée dans
\(L^{3,\infty}(\mathbb R^3)\) possèdent-elles, dans la littérature, une
cohérence suffisamment uniforme lorsque le temps de base tend vers
\(-\infty\) pour produire une solution mild ancienne, une condition de
vanishing au passé, ou un théorème de Liouville ?

L'équation considérée est exclusivement Navier--Stokes incompressible,
non forcé, de viscosité un, sur \(\mathbb R^3\times(-\infty,0)\) :

\[
 \partial_t v-\Delta v+\operatorname{div}(v\otimes v)+\nabla q=0,
 \qquad \operatorname{div}v=0.                            \tag{1}
\]

La loi d'échelle est

\[
 v_\lambda(x,t)=\lambda v(\lambda x,\lambda^2t),\qquad
 q_\lambda(x,t)=\lambda^2q(\lambda x,\lambda^2t).        \tag{2}
\]

La norme \(L^{3,\infty}\) est invariante par (2), tandis que
\(\|f_\lambda\|_2^2=\lambda^{-1}\|f\|_2^2\). Cette différence d'échelle
est centrale : un correcteur énergétique existe sur chaque fenêtre finie
sans fournir, par cette seule propriété, une borne uniforme lorsque la
longueur de la fenêtre tend vers l'infini.

## Verdict

1. **La cohérence algébrique entre deux temps de base est exacte.** Si
   \(s<r<t\), alors les scissions

   \[
    V_s(t)=e^{(t-s)\Delta}v(s),\qquad w_s(t)=v(t)-V_s(t)   \tag{3}
   \]

   satisfont

   \[
    w_s(t)-w_r(t)=e^{(t-r)\Delta}w_s(r),
    \qquad
    V_s(t)-V_r(t)=-e^{(t-r)\Delta}w_s(r).                 \tag{4}
   \]

   C'est une dérivation du laboratoire à partir de la propriété de
   semi-groupe, non un théorème nouveau repéré dans une source.

2. **(4) définit une orbite quotient, mais pas une limite au passé.** Le
   quotient littéral \(L^{3,\infty}/L^2\) n'est pas bien défini sur
   \(\mathbb R^3\), car \(L^2\not\subset L^{3,\infty}\). L'objet sûr est

   \[
    X=L^{3,\infty}_\sigma(\mathbb R^3),\quad
    E=\overline{L^2\cap X}^{\,X},\quad Q=X/E.             \tag{5}
   \]

   Le semi-groupe de la chaleur préserve \(E\), donc induit
   \(\bar S(t)\) sur le quotient de Hausdorff \(Q\). Si chaque
   \(w_s(r)\in L^2\cap X\), alors

   \[
       [v(t)]_Q=\bar S(t-r)[v(r)]_Q.                      \tag{6}
   \]

   Ni une norme qui décroît quand \(r\to-\infty\), ni une compacité de
   représentants, ni une convergence forte de \(w_s\) ne suit de (6).

3. **Taniuchi (2024) donne une formule sur tout le passé, sous une hypothèse
   mild déjà cohérente.** Sa définition impose l'identité mild entre
   *chaque* paire de temps finis. Le passage \(s\to-\infty\) est obtenu en
   dualité parce que le semi-groupe adjoint appliqué au test tend vers zéro
   dans \(L^{3/2,1}\). Ce n'est ni
   \(e^{(t-s)\Delta}v(s)\to0\) fortement dans \(L^{3,\infty}\), ni une
   borne uniforme des correcteurs BSS dans \(L^2\).

4. **Les théorèmes de Liouville contrôlés demandent davantage que la borne
   faible-\(L^3\).** Koch--Nadirashvili--Seregin--Šverák (KNSS) définissent
   la mildness ancienne par compatibilité avec des problèmes de Cauchy le
   long d'une suite de temps tendant vers \(-\infty\). Leur Liouville
   général tridimensionnel pour les solutions mild anciennes bornées reste
   explicitement ouvert. Albritton--Barker (2019) obtiennent la rigidité à
   partir d'une suite bornée dans \(L^3\); leur variante faible-\(L^3\)
   requiert en plus une condition terminale de blow-down dans
   \(\dot B^{-1}_{\infty,\infty}\).

5. **BSS et Albritton--Barker (ARMA) ne construisent pas un objet ancien en
   reculant l'origine.** Les classes faibles concernées sont posées sur une
   fenêtre avant finie avec un correcteur énergétique. L'indépendance de
   l'ordre d'itération de Picard chez Albritton--Barker n'est pas une
   indépendance du temps de base. Aucun énoncé contrôlé dans ces articles
   ne donne une estimation uniforme quand \(s\to-\infty\).

6. **Une nouvelle source primaire de 2025 mérite une entrée au catalogue.**
   Bradshaw--Hudson étendent la théorie faible BSS à
   \(L^{p,\infty}\), \(2<p<3\), et utilisent explicitement la possibilité
   de rebaser une solution à un temps intérieur \(t_0\). L'argument reste
   local sur une fenêtre finie et ses bornes portent une puissance positive
   du temps écoulé. Il confirme donc la cohérence finie utile, mais ne ferme
   pas le passage ancien. Il s'agit au 15 août 2026 d'une prépublication
   arXiv v1, non d'un article publié repéré.

7. **Conclusion négative exacte : aucun théorème n'a été trouvé, dans le
   corpus primaire ciblé, établissant**

   \[
   \boxed{
   \begin{gathered}
    v\text{ ancienne localement adaptée},\quad
    \sup_{t<0}\|v(t)\|_{L^{3,\infty}}<\infty,\\
    \forall s<T:\quad
      v-e^{(\cdot-s)\Delta}v(s)
      \in L^\infty(s,T;L^2)\cap L^2(s,T;\dot H^1)
      \\
    \Longrightarrow
    \text{mildness ancienne compatible, vanishing au passé ou }v=0.
   \end{gathered}}                                        \tag{7}
   \]

   Cette conclusion signifie **absence de théorème localisé**, et non
   impossibilité de démontrer (7), ni existence d'un contre-exemple à (7).

## 1. Le cocycle exact et ce qu'il ne donne pas

### 1.1 Dérivation entre deux origines

Pour \(s<r<t\), la propriété de semi-groupe donne

\[
\begin{aligned}
 w_s(t)-w_r(t)
 &= -e^{(t-s)\Delta}v(s)+e^{(t-r)\Delta}v(r)\\
 &= e^{(t-r)\Delta}
    \big(v(r)-e^{(r-s)\Delta}v(s)\big)\\
 &= e^{(t-r)\Delta}w_s(r).
                                                               \tag{8}
\end{aligned}
\]

Il n'y a ici ni pression, ni passage à la limite, ni estimateur non
linéaire caché. En revanche, (8) suppose que les traces temporelles utilisées
dans (3) existent dans une notion compatible. Une solution convenable
locale abstraite n'offre pas automatiquement une trace forte
\(L^{3,\infty}\) à tout instant.

Sur chaque bande finie, l'estimation BSS à l'endpoint a la taille typique

\[
 \|w_s(r)\|_2\lesssim_M (r-s)^{1/4},
 \qquad
 \|w_s(r)\|_2^2\lesssim_M (r-s)^{1/2},                  \tag{9}
\]

avec \(M=\sup_{t<0}\|v(t)\|_{3,\infty}\). Même si la constante cachée est
uniforme à \(M\) fixé, le membre droit diverge quand \(s\to-\infty\) à
\(r\) fixé. (9) ne produit donc ni suite de Cauchy, ni représentant
énergétique global sur \(( -\infty,r]\).

### 1.2 Quotient correct

Puisque \(w_s(r)=v(r)-e^{(r-s)\Delta}v(s)\) appartient simultanément à
\(L^2\) et à \(X\) lorsque les deux termes faible-\(L^3\) sont définis,

\[
 [v(r)]_Q=\bar S(r-s)[v(s)]_Q.                            \tag{10}
\]

Le passage à la fermeture dans (5) est nécessaire pour que le quotient soit
séparé. Le quotient non fermé par \(L^2\cap X\) peut servir de quotient
algébrique, mais pas d'espace de Banach sur lequel une compacité ou une
convergence puisse être invoquée sans preuve supplémentaire.

Deux identifications tentantes sont fausses ou non établies :

- l'espace \(E\) de (5) ne doit pas être identifié sans preuve avec
  \(\widetilde L^{3,\infty}\) de Taniuchi, qui est la fermeture dans
  \(L^{3,\infty}\) de \(L^\infty\cap L^{3,\infty}\) ;
- on ne peut pas affirmer que
  \(e^{h\Delta}f-f\in L^2\) pour tout \(f\in L^{3,\infty}\).

Ainsi (10) encode un défaut de queue ou de faible amplitude persistant sous
le flot calorique, mais ne le rend ni petit ni compact.

## 2. Taniuchi : formule sur tout le passé, mais après mildness

Yasushi Taniuchi,
[*On uniqueness of mild \(L^{3,\infty}\)-solutions on the whole time axis to
the Navier--Stokes equations in unbounded
domains*](https://doi.org/10.1007/s00208-023-02702-x),
*Mathematische Annalen* **389** (2024), 2561--2594.

La définition 1, équation (2.2), demande

\[
 v\in C(( -\infty,T);L^{3,\infty}_\sigma)                \tag{11}
\]

en topologie forte et impose, pour **tous** \(-\infty<s<t<T\), l'identité
mild finie

\[
 v(t)=e^{(t-s)\Delta}v(s)
 -\int_s^t e^{(t-\tau)\Delta}\mathbb P
      \operatorname{div}(v\otimes v)(\tau)\,d\tau.       \tag{12}
\]

Sous une borne uniforme faible-\(L^3\), Taniuchi fait tendre
\(s\to-\infty\) contre un test. Le terme libre disparaît parce que

\[
 e^{(t-s)\Delta}\varphi\longrightarrow0
 \quad\text{dans }L^{3/2,1}\quad(s\to-\infty),           \tag{13}
\]

ce qui mène à la formule intégrale sur tout le passé (2.3). (13) est une
convergence du **test adjoint**. Elle ne justifie pas une convergence forte
de \(e^{(t-s)\Delta}v(s)\) dans \(L^{3,\infty}\), espace non séparable où
la forte continuité du semi-groupe n'est pas générale.

Le théorème 1 suppose que les deux solutions sont déjà mild et appartiennent
à

\[
 BC(( -\infty,T);\widetilde L^{3,\infty}_\sigma).         \tag{14}
\]

L'appartenance à cet espace `BC` assure la continuité forte
\(L^{3,\infty}\) à chaque temps initial **fini** auquel (12) est rebased.
Elle n'impose aucune limite de la trajectoire lorsque \(t\to-\infty\). Les
théorèmes anciens ajoutent précisément les conditions de petitesse, de
décroissance ou d'approximation au passé décrites ci-dessous; l'espace tilde
seul ne tue donc pas une classe non nulle dans le quotient \(Q\) sur une
durée arbitrairement grande.

Une solution est petite au passé,

\[
 \limsup_{t\to-\infty}\|u(t)\|_{3,\infty}<\delta,        \tag{15}
\]

et l'autre vérifie la condition (1.6) de proximité, au passé et dans le
champ lointain, à un profil fixe \(V\in L^{3,\infty}\). La conclusion est
l'unicité. Le corollaire 2 remplace une partie de cette hypothèse par un
contrôle \(L^{r,\infty}\), \(1<r<3\), avec taux; la remarque 1 note qu'une
borne uniforme correspondante au passé suffit. Le théorème 3 autorise un
profil \(V(t)\) dont l'image est contrôlée par une condition de recouvrement
fini de type précompacité.

Les lemmes 8 et 9 n'enlèvent pas le gap : le lemme 8 suppose l'identité
bilinéaire sur tout le passé et de petites normes; le lemme 9 suppose déjà
la mildness, la continuité bornée dans l'espace tilde et la petitesse au
passé. Rien dans ces énoncés ne transforme des scissions BSS séparées sur
fenêtres finies en (11)--(12).

**Implication contrôlée :**

\[
 \text{mildness cohérente + espace tilde + hypothèses au passé}
 \Longrightarrow \text{unicité},                         \tag{16}
\]

mais la flèche

\[
 \text{solution adaptée + scissions BSS finies}
 \dashrightarrow \text{hypothèses de (16)}               \tag{17}
\]

reste manquante.

## 3. KNSS : la compatibilité est dans la définition

Gabriel Koch, Nikolai Nadirashvili, Gregory Seregin et Vladimir Šverák,
[*Liouville theorems for the Navier--Stokes equations and applications*](https://doi.org/10.1007/s11511-009-0039-6),
*Acta Mathematica* **203** (2009), 83--105;
[`arXiv:0709.3599v1`](https://arxiv.org/abs/0709.3599v1),
catalogue `NS-SRC-0015`.

Une solution faible ancienne y est distributionnelle sur
\(\mathbb R^n\times(-\infty,0)\); cette classe peut contenir des solutions
parasites spatiales \(u(x,t)=b(t)\) compensées par une pression affine. Une
solution mild ancienne est définie plus strictement : il existe une suite
\(T_k\to-\infty\) telle que \(u(\cdot,T_k)\) soit définie et que \(u\) soit,
sur chaque \((T_k,0)\), la solution mild du problème de Cauchy ayant cette
donnée.

Cette définition impose précisément une compatibilité de rebasing le long
d'une suite. Elle n'est pas une conséquence annoncée de suitability locale,
d'une borne faible-\(L^3\), ou de correcteurs énergétiques fenêtre par
fenêtre.

Les résultats de Liouville de KNSS portent sur des solutions anciennes
globalement bornées. Ils couvrent notamment la dimension deux et des classes
axisymétriques particulières. L'article indique que le théorème de Liouville
pour une solution mild ancienne bornée générale en dimension trois est
ouvert. Aucune condition \(u(t)\to0\) quand \(t\to-\infty\) n'est placée
dans la définition : les champs constants appartiennent à la classe mild,
même si des hypothèses invariantes d'échelle additionnelles peuvent les
exclure.

**Conséquence adverse :** remplacer « ancienne adaptée » par « ancienne
mild » dans un argument de rigidité est un saut logique tant que la
compatibilité des problèmes de Cauchy reculés n'a pas été établie.

## 4. Albritton--Barker : rigidité et hypothèses exactes

Dallas Albritton et Tobias Barker,
[*Localised necessary conditions for singularity formation in the
Navier--Stokes equations with curved boundary*](https://doi.org/10.1007/s00021-019-0448-z),
*Journal of Mathematical Fluid Mechanics* **21** (2019), article 43;
[`arXiv:1811.00502v1`](https://arxiv.org/abs/1811.00502v1),
catalogue `NS-SRC-0189`.

Dans le cas entier pertinent ici, le théorème 1.1 relie une singularité de
Type I d'une solution convenable à l'existence d'une solution **mild ancienne
bornée**, non nulle, possédant une quantité invariante d'échelle de Type I
finie. Ce résultat fournit un objet limite déjà mild; il ne démontre pas
qu'une ancienne solution adaptée faible-\(L^3\) arbitraire devient mild par
recalage des scissions BSS.

Le théorème 1.2 affirme qu'une solution mild ancienne vérifiant, pour une
suite \(t_k\downarrow-\infty\),

\[
 \sup_k\|v(t_k)\|_{L^3}<\infty                            \tag{18}
\]

est identiquement nulle. Pour faible-\(L^3\), le théorème quantitatif 4.1
demande

\[
 \|v(t_k)\|_{L^{3,\infty}}\le M                          \tag{19}
\]

et, en plus, une condition au temps terminal

\[
 \operatorname{dist}_{\dot B^{-1}_{\infty,\infty}}
   (v(0),\mathcal B)\le\varepsilon(M),                    \tag{20}
\]

où \(\mathcal B\) est l'ensemble des distributions dont le blow-down
\(f(\lambda\,\cdot)\) tend vers zéro dans \(\mathcal D'\) lorsque
\(\lambda\to\infty\). Par conséquent, (19) seule n'est pas le contenu du
théorème. La remarque 4.3 donne des variantes de Besov et une annulation si
une norme \(BMO^{-1}\) est petite le long d'une suite au passé, toujours
dans une classe mild ancienne.

Dans leur preuve, chaque temps ancien est remis à l'échelle et donne un
problème BSS sur une fenêtre normalisée; la compacité et la rigidité portent
sur cette suite de problèmes. L'article ne construit pas un correcteur
\(L^2\) unique sur tout \(( -\infty,0)\), et ne démontre pas la convergence
des correcteurs lorsque l'origine recule.

## 5. BSS et solutions faibles Besov : fenêtres finies

Tobias Barker, Gregory Seregin et Vladimir Šverák,
[*On stability of weak Navier--Stokes solutions with large
\(L^{3,\infty}\) initial data*](https://doi.org/10.1080/03605302.2018.1449219),
*Communications in Partial Differential Equations* **43** (2018),
628--651; [`arXiv:1603.03211v1`](https://arxiv.org/abs/1603.03211v1),
catalogue `NS-SRC-0188`.

La définition 1.1 part d'un temps initial fini et inclut la scission par le
flot calorique ainsi que le correcteur dans la classe énergétique. Le lemme
3.3 permet de remplacer la scission initiale par une décomposition de
Calderón mieux adaptée, mais son hypothèse de départ est déjà une solution
BSS. Il ne traite pas une famille indexée par des temps initiaux tendant
vers \(-\infty\).

Dallas Albritton et Tobias Barker,
[*Global Weak Besov Solutions of the Navier--Stokes Equations and
Applications*](https://doi.org/10.1007/s00205-018-1319-0), *Archive for
Rational Mechanics and Analysis* **232** (2019), 197--263;
[`arXiv:1802.03164v2`](https://arxiv.org/abs/1802.03164v2),
catalogue `NS-SRC-0192`.

La proposition 3.4 de ce second article montre que la notion de solution
faible Besov ne dépend pas du niveau admissible choisi dans l'itération de
Picard. Ce résultat compare deux fonds explicites associés à la **même
donnée et au même temps initial**. Il ne compare pas les origines \(s\) et
\(r\) de (3), et ne doit donc pas être cité comme cohérence ancienne.

## 6. Veille différentielle 2025--2026

### 6.1 Nouvelle source directement pertinente

Zachary Bradshaw et Joshua Hudson,
[*Time asymptotics, time regularity and separation rates for Navier--Stokes
flows in supercritical solution classes*](https://arxiv.org/abs/2508.00714v1),
arXiv:2508.00714v1, 1er août 2025, 38 pages.

L'article étend la théorie faible BSS à des données
\(L^{p,\infty}(\mathbb R^3)\), \(2<p<3\). La définition 1.2 incorpore le
correcteur calorique dans la classe globale d'énergie sur une fenêtre
finie. Le théorème 1.4 fournit une borne a priori avec une puissance positive
du temps écoulé. À l'endpoint \(p=3\), les auteurs rappellent la taille BSS
\(\|u-e^{t\Delta}u_0\|_2\lesssim t^{1/4}\).

Dans la preuve de la régularité temporelle, page 33 du PDF v1, les auteurs
écrivent explicitement que, pour \(t>t_0\), on peut voir \(u\) comme une
solution faible \(L^{p,\infty}\) de donnée \(u(\cdot,t_0)\), puis appliquent
l'estimation a priori sur cette nouvelle fenêtre. C'est une preuve utile de
**rebasage local fini** dans cette classe. Le théorème 1.10 suppose toutefois
dès le départ que \(u\) est une solution faible \(L^{p,\infty}\) sur un
intervalle contenant zéro. Aucun théorème de limite projective ancienne,
aucune borne uniforme en \(t_0\to-\infty\), et aucune construction d'une
solution mild ancienne n'y sont énoncés.

**Décision catalogue : AJOUTER UNE SOURCE.** Cette prépublication est
primaire, postérieure au socle BSS, directement pertinente pour la
cohérence par rebasage et absente de `sources.json` au moment de l'audit.
Elle doit être enregistrée comme prépublication arXiv v1, sans statut de
preuve publiée. Le présent mandat interdit de modifier le catalogue; cette
recommandation est donc seulement consignée ici.

### 6.2 Sources récentes contrôlées mais non transférables au verrou

| Source primaire | Objet exact | Pourquoi elle ne ferme pas (7) | Catalogue |
|---|---|---|---|
| G. Seregin, [`arXiv:2507.08733v2`](https://arxiv.org/abs/2507.08733v2) | scénarios de singularité de Type II et limites anciennes sous une échelle de type Euler | ni classe BSS faible-\(L^3\), ni limite uniforme des correcteurs calorifiques reculés | `NS-SRC-0048` |
| T. Barker, [`arXiv:2510.20757v3`](https://arxiv.org/abs/2510.20757v3) | classification quantitative près des singularités | BSS intervient comme outil en temps fini; aucune cohérence ancienne des scissions n'est annoncée | `NS-SRC-0084` |
| G. Seregin, [`arXiv:2606.29468v1`](https://arxiv.org/abs/2606.29468v1) | nouveau scénario Type II et objet ancien limite | changement d'échelle et notion limite différents du cocycle calorique faible-\(L^3\) | `NS-SRC-0034` |
| O. Jarrín, [`arXiv:2607.03602v1`](https://arxiv.org/abs/2607.03602v1) | promotion local-vers-global sous hypothèses de Morrey | donnée énergétique/Morrey supplémentaire, pas seulement borne critique faible-\(L^3\) ancienne | `NS-SRC-0191` |

Ces contrôles ne justifient aucune nouvelle entrée : les quatre sources sont
déjà cataloguées. Ils ne constituent pas une recherche exhaustive de tout
arXiv, mais une veille différentielle ciblée sur le verrou actif et les
annonces récentes déjà identifiées par le laboratoire.

## 7. Matrice des implications

| Maillon | Statut | Source ou preuve | Trou exact |
|---|---|---|---|
| Deux scissions exactes \(\Rightarrow\) cocycle (8) | démontré algébriquement | propriété de semi-groupe | exige des traces compatibles aux temps de base |
| Correcteurs \(L^2\cap X\) \(\Rightarrow\) orbite dans \(Q\) | démontré algébriquement | (5), (8) | aucune coercivité du quotient |
| Solution BSS finie \(\Rightarrow\) rebasage fini | classique dans la classe, confirmé récemment | BSS; Bradshaw--Hudson 2025 | les bornes croissent avec la longueur de fenêtre |
| Famille rebasée \(\Rightarrow\) correcteur ancien uniforme | **manquant** | aucun théorème localisé | perte de constante quand \(s\to-\infty\) |
| Suitability + borne faible-\(L^3\) \(\Rightarrow\) mildness ancienne | **manquant** | aucun théorème localisé | cohérence forte et pression non locale au passage à la limite |
| Mild ancienne + borne \(L^3\) sur une suite \(\Rightarrow v=0\) | publié | Albritton--Barker, th. 1.2 | hypothèse \(L^3\), pas faible-\(L^3\) |
| Mild ancienne + faible-\(L^3\) sur une suite + (20) \(\Rightarrow v=0\) | publié | Albritton--Barker, th. 4.1 | condition terminale de blow-down non obtenue |
| Mild ancienne petite/approchable au passé dans l'espace tilde \(\Rightarrow\) unicité | publié | Taniuchi, th. 1--3, lemmes 8--9 | petitesse, approximation et mildness déjà supposées |
| Bounded ancient mild 3D \(\Rightarrow v\) trivial | ouvert en général | KNSS | théorème de Liouville tridimensionnel manquant |

## 8. Passe contradictoire

### 8.1 Quantificateur et uniformité

L'énoncé « pour tout \(s<T\), il existe un correcteur énergétique sur
\([s,T]\) » ne signifie pas « il existe un correcteur énergétique sur
\(( -\infty,T]\) ». L'échange entre \(\forall s\,\exists w_s\) et
\(\exists w\,\forall s\) requiert compatibilité et compacité uniformes. Le
cocycle (8) donne la première, sous réserve de traces, mais l'estimation (9)
ne donne pas la seconde.

### 8.2 Topologie endpoint

La dualité faible-* avec \(L^{3/2,1}\) est suffisante pour annuler le terme
calorique testé chez Taniuchi. Elle ne produit pas la continuité forte dans
\(L^{3,\infty}\), ni la continuité forte à un temps initial requise par une
solution mild de Cauchy. Toute preuve utilisant (13) comme une convergence
en norme inverse le sens topologique de l'argument.

### 8.3 Contre-profil fonctionnel

Un champ homogène divergence-free de degré \(-1\), lissé ou tronqué pour
les tests numériques, est invariant à l'échelle de \(L^{3,\infty}\) et
peut conserver une classe non nulle dans \(Q\). Il sert de contre-profil à
l'inférence « orbite quotient calorique \(\Rightarrow\) vanishing au
passé ». Un profil de type Landau ne doit toutefois pas être présenté comme
une solution lisse non forcée de (1) : les champs de Landau stationnaires
portent une singularité/force ponctuelle à l'origine. Le test réfute une
inférence fonctionnelle, pas l'énoncé Clay.

### 8.4 Pression et admissibilité

L'identité (8) n'utilise pas la pression, mais le passage d'une famille de
solutions sur fenêtres à une solution distributionnelle/mild unique exige
de recoller aussi les pressions, modulo fonctions du temps, ou de travailler
entièrement avec la projection de Leray. Une convergence seulement faible
des vitesses ne suffit pas à passer dans \(v\otimes v\). C'est une seconde
raison, indépendante de la croissance (9), pour laquelle le quotient seul
ne ferme pas la construction.

## 9. Protocole de recherche et portée du résultat négatif

La veille a contrôlé les pages/PDF primaires de Taniuchi, KNSS,
Barker--Seregin--Šverák, les deux articles Albritton--Barker pertinents et
Bradshaw--Hudson, puis les prépublications 2025--2026 du tableau ci-dessus.
Des recherches ciblées sur les expressions « \(L^{3,\infty}/L^2\) »,
quotient faible-\(L^3\) sous le semi-groupe de la chaleur, ancient Calderón
solutions, backward base-time consistency et weak-\(L^3\) ancient mild
solutions n'ont renvoyé aucun théorème primaire supplémentaire ajusté à
(7).

La formulation scientifique autorisée est donc :

> Aucun théorème fermant le maillon (7) n'a été localisé dans ce corpus
> primaire ciblé à la date de coupure.

Les formulations suivantes ne sont pas autorisées :

- « un tel théorème n'existe pas » ;
- « la construction est impossible » ;
- « le quotient démontre un obstacle absolu » ;
- « la borne faible-\(L^3\) permet nécessairement un blow-up ».

## 10. Empreintes et décision de cycle

| Artefact primaire contrôlé localement | SHA-256 |
|---|---|
| `0709.3599.pdf` (KNSS, arXiv v1) | `EE4444837EAF72A0298F2032BE63A93C5DE41B61784BB1A68AE1E3E8973F14D8` |
| `1811.00502.pdf` (Albritton--Barker, arXiv v1) | `FBAF90712190E3AA2C700AF7D1FD4C79C5DAFDC1B98B3A3CCE1AF3992C9D3C66` |
| `2508.00714.pdf` (Bradshaw--Hudson, arXiv v1) | `230C343BD337D212EC02AF056FE7F7D824B41DB03A07C03EA365EA47A7DBAEAB` |

La page Springer ouverte de Taniuchi a été contrôlée directement; aucune
empreinte d'un PDF n'est attribuée dans cet audit. L'API primaire arXiv
retourne encore `2508.00714v1`, publié et mis à jour le 1er août 2025, à la
date de coupure.

**État : CONTINUER, avec révision de la cible.** Le cocycle quotient est un
lemme structurel exact, mais insuffisant. Il faut cesser de traiter
Taniuchi comme un théorème de promotion BSS-vers-mild et tester une hypothèse
additionnelle minimale qui soit réellement falsifiable.

**Prochain lemme bibliographiquement admissible :** avec \(X,E,Q\) définis
par (5), démontrer proprement (10) pour les temps de Lebesgue admissibles,
puis isoler l'une des deux hypothèses supplémentaires suivantes :

1. existence d'une suite \(s_k\to-\infty\) telle que les correcteurs
   \(w_{s_k}\) soient uniformément bornés dans l'énergie sur toute fenêtre
   terminale fixe ;
2. existence de représentants de l'orbite quotient précompacts dans une
   topologie qui permette de passer fortement dans le terme quadratique.

Le test décisif doit déterminer si l'une de ces hypothèses implique soit la
mildness ancienne de KNSS/Taniuchi, soit la condition terminale (20)
d'Albritton--Barker. Si le profil homogène de degré \(-1\) satisfait la
nouvelle hypothèse sans vanishing, l'hypothèse est trop faible et doit être
abandonnée.
