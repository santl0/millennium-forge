# Cycle 0044 — projection de Leray, fuite locale et passage ancien

**Date de vérification :** 15 août 2026

**Nature :** veille primaire contradictoire indépendante, sans modification du
catalogue d'affirmations

**Objet borné :** déterminer ce qui est publié, ce qui relève d'une dérivation
standard et ce qui reste ouvert dans la chaîne

\[
\text{stress soutenu loin}
\longrightarrow \mathbb P\operatorname{div}E_L\to0\text{ localement}
\longrightarrow \text{limite Navier--Stokes ancienne non triviale}.
\]

Le cadre de référence est Navier--Stokes incompressible visqueux en dimension
trois sur \(\mathbb R^3\), viscosité normalisée à un, sans force dans
l'équation cible :

\[
\partial_tu-\Delta u+\operatorname{div}(u\otimes u)+\nabla p=0,
\qquad \operatorname{div}u=0.                              \tag{1}
\]

Selon les sources, la notion de solution varie : solution distributionnelle,
faible adaptée, d'énergie locale, mild ou ancienne bornée. Ces notions ne sont
pas interchangeables.

## Verdict exécutable

1. Pour un tenseur \(E_L\) nul sur \(B_L\), la distribution
   \(\operatorname{div}E_L\) disparaît **exactement** sur tout compact fixé
   lorsque \(L\) est assez grand. Après projection de Leray globale, le support
   n'est plus préservé : \(\mathbb P\operatorname{div}E_L\) possède en général
   une queue de pression non nulle.

2. Loin du support, le noyau de
   \(\mathbb P\operatorname{div}\) est une troisième dérivée du potentiel
   newtonien et est homogène de degré \(-4\). Le noyau de \(\mathbb P\) agissant
   sur une force vectorielle est, lui, de degré \(-3\). Confondre les deux
   opérateurs coûte exactement une puissance de distance.

3. Les ingrédients publiés impliquent le lemme critique suivant, mais aucune
   source primaire auditée ne l'énonce mot pour mot : si

   \[
   \operatorname{supp}E_L\subset\mathbb R^3\setminus B_L,
   \qquad \|E_L\|_{L^{3/2,\infty}(\mathbb R^3)}\le K,
   \]

   alors, pour \(L\ge2\rho\) et tout multi-indice \(\alpha\),

   \[
   \|\partial^\alpha\mathbb P\operatorname{div}E_L
   \|_{L^\infty(B_\rho)}
   \le C_{\alpha}K L^{-3-|\alpha|}.                       \tag{2}
   \]

   En fait la constante peut être prise indépendante de \(\rho\) dès que
   \(L\ge2\rho\), à convention de norme de Lorentz fixée. Le statut correct de
   (2) est **`PUBLISHED_INGREDIENTS + AI_INTERNAL_DERIVATION`**, et non
   `PAPER_PROOF`.

4. La puissance \(L^{-3}\) est critique et cohérente avec l'échelle de (1) :
   \(E_\lambda(x,t)=\lambda^2E(\lambda x,\lambda^2t)\)
   conserve \(\|E\|_{L^{3/2,\infty}}\), tandis que
   \(\mathbb P\operatorname{div}E\) se dilate comme \(\lambda^3\).

5. La disparition locale de cette force projetée **ne ferme pas** le passage
   à une solution ancienne. Une borne uniforme
   \(u_n\in L^{3,\infty}\) donne bien
   \(u_n\otimes u_n\in L^{3/2,\infty}\), mais ne fournit seule ni compacité
   locale forte, ni identification de \(u_n\otimes u_n\), ni passage de
   l'inégalité d'énergie locale, ni convergence adéquate de la pression, ni
   non-trivialité de la limite.

6. Le meilleur raccord publié audité est Albritton--Barker (2020) : une
   troncature solénoïdale sur un anneau régulier, suivie d'un blow-up, produit
   une solution ancienne mild bornée non triviale. Leur preuve utilise une
   force qui tend vers zéro dans des espaces **sous-critiques plus forts**, des
   estimations de pression et une compacité de Hölder. Elle ne découle pas
   d'une seule borne faible-\(L^3\).

7. Aucune source primaire 2025--2026 trouvée et vérifiée ne ferme déjà (2)
   comme théorème identifié, ni surtout l'implication

   \[
   \sup_n\|u_n\|_{L^{3,\infty}}<\infty
   \Longrightarrow
   \text{solution ancienne NS admissible non triviale}.   \tag{3}
   \]

   Les résultats récents concernent des réductions conditionnelles, des
   limites Euler, des profils auto-similaires particuliers ou des solutions
   faibles issues de données critiques singulières. Aucun ne résout le verrou
   du cycle.

## 1. Calcul exact de l'opérateur non local

On adopte

\[
\Gamma(x)=-\frac1{4\pi|x|},\qquad \Delta\Gamma=\delta_0,
\qquad \mathbb P=I-\nabla\Delta^{-1}\operatorname{div}.   \tag{4}
\]

Pour un tenseur \(E=(E_{kj})\),

\[
(\mathbb P\operatorname{div}E)_i
=\partial_jE_{ij}
-\partial_i\Delta^{-1}\partial_k\partial_jE_{kj}.         \tag{5}
\]

Si \(x\notin\operatorname{supp}E\), le premier terme est localement nul et

\[
(\mathbb P\operatorname{div}E)_i(x)
=-\int_{\mathbb R^3}
 \partial_i\partial_k\partial_j\Gamma(x-y)E_{kj}(y)\,dy.  \tag{6}
\]

Le noyau

\[
M_{ikj}(z)=-\partial_i\partial_k\partial_j\Gamma(z)        \tag{7}
\]

est homogène de degré \(-4\). Explicitement,

\[
\partial_i\partial_j\partial_k|z|^{-1}
=3(\delta_{ij}z_k+\delta_{ik}z_j+\delta_{jk}z_i)|z|^{-5}
-15z_iz_jz_k|z|^{-7}.                                    \tag{8}
\]

La valeur principale n'intervient pas dans (6), puisque le point d'évaluation
reste à distance du support. En revanche, si l'objet de départ est une force
vectorielle \(f\), la partie non locale de \(\mathbb Pf\) utilise
\(\partial_i\partial_j\Gamma\), de degré \(-3\). L'affirmation « le noyau de
Leray est de degré \(-4\) » n'est donc correcte qu'après composition avec une
divergence de tenseur.

### 1.1 Démonstration par couronnes du résidu (2)

Fixons \(x\in B_\rho\), \(L\ge2\rho\), et

\[
A_k=\{2^kL<|y|\le2^{k+1}L\},\qquad k\ge0.
\]

L'inégalité de Lorentz sur un ensemble de mesure finie donne

\[
\int_{A_k}|E_L(y)|\,dy
\le C|A_k|^{1/3}\|E_L\|_{L^{3/2,\infty}(A_k)}
\le CK\,2^kL.                                             \tag{9}
\]

Pour \(y\in A_k\), \(|x-y|\ge c2^kL\), donc

\[
|\partial^\alpha M(x-y)|
\le C_\alpha(2^kL)^{-4-|\alpha|}.                         \tag{10}
\]

La somme de (9)--(10) est géométrique :

\[
\sum_{k\ge0} CK(2^kL)^{-3-|\alpha|}
\le C_\alpha K L^{-3-|\alpha|}.                          \tag{11}
\]

Cette preuve ne requiert pas que \(E_L\) soit compactement supporté. Elle
requiert seulement le support extérieur et une norme faible-\(L^{3/2}\)
globale uniforme. Des annulations de moments peuvent améliorer la décroissance,
mais ne sont pas nécessaires à (2).

Plus généralement, la même sommation donne pour
\(E_L\in L^{p,\infty}\), \(1<p<\infty\),

\[
\|\mathbb P\operatorname{div}E_L\|_{L^\infty(B_\rho)}
\lesssim \|E_L\|_{L^{p,\infty}}L^{-1-3/p},               \tag{12}
\]

tant que le support est extérieur. Le cas \(p=3/2\) redonne exactement
\(L^{-3}\).

### 1.2 Formulation locale sans projection globale

Si \(\varphi\in C_c^\infty(B_\rho;\mathbb R^3)\) est solénoïdale et
\(L>\rho\), alors

\[
\langle\operatorname{div}E_L,\varphi\rangle=0.            \tag{13}
\]

Dans la formulation faible solénoïdale, la pression disparaît également.
Ainsi, avant projection globale, la source extérieure ne laisse aucun résidu
sur les tests compacts. C'est souvent la voie la plus propre pour passer à
l'équation locale. L'estimation (2) devient nécessaire si l'on veut une
équation projetée, une formulation mild globale ou le contrôle explicite de
la pression.

## 2. Sources publiées sur pression locale et Leray localisé

### 2.1 Wolf 2017 : projection locale de gradient

Jörg Wolf,
[*On the local pressure of the Navier--Stokes equations and related
systems*](https://doi.org/10.57262/ade/1489802453), *Advances in
Differential Equations* **22** (2017), 305--338, DOI
`10.57262/ade/1489802453`,
[`arXiv:1611.01482v1`](https://arxiv.org/abs/1611.01482v1).

**Statut.** Article publié; version arXiv v1 du 4 novembre 2016 auditée.

Le théorème 6.4 et le corollaire 6.5 reconstruisent localement la pression :
si \(\partial_tu+F\) s'annule sur les tests solénoïdaux, alors, dans chaque
sous-domaine borné suffisamment régulier, la partie gradient se décompose en
\(\partial_t\nabla p_h+\nabla p_0\). Lorsque
\(\operatorname{div}u=0\), \(p_h\) est harmonique. Le théorème 7.2 applique
ce mécanisme aux systèmes visqueux incompressibles avec stress extérieur.

**Transfert.** La source publie le fait essentiel que la pression pertinente
sur un sous-domaine est un objet local projeté, auquel s'ajoute une correction
harmonique. Elle permet d'éviter d'imposer artificiellement une représentation
globale de la pression.

**Limite.** Wolf n'énonce ni le lemme extérieur faible-\(L^{3/2}\) (2), ni
une compacité ancienne à l'endpoint faible-\(L^3\). Son projecteur local de
gradient, défini via Stokes sur le sous-domaine, n'est pas le multiplicateur
de Fourier global \(\mathbb P\).

### 2.2 Kwon 2023 : Leray localisé et correction harmonique

Hyunju Kwon,
[*The Role of the Pressure in the Regularity Theory for the Navier--Stokes
Equations*](https://doi.org/10.1016/j.jde.2023.01.049), *Journal of
Differential Equations* **357** (2023), 1--31, DOI
`10.1016/j.jde.2023.01.049`,
[`arXiv:2104.03160v3`](https://arxiv.org/abs/2104.03160v3).

**Statut.** Article publié; arXiv v3 du 1er septembre 2021 auditée.

Pour un cutoff \(\phi\), l'article définit

\[
\mathbb P_\phi g=-\operatorname{curl}\Delta^{-1}
   (\phi\operatorname{curl}g).                            \tag{14}
\]

Les estimations (2.2)--(2.4) contrôlent cet opérateur localement. Si \(g\)
est divergence-free, \(g-\mathbb P_\phi g\) est harmonique, donc lisse, dans
la région où \(\phi=1\). Le lemme 2.5 décompose une solution dissipative en
\(u=v+h\), où \(v\) est une solution adaptée d'un système perturbé et \(h\)
est harmonique.

**Transfert.** Il existe un mécanisme publié pour isoler la partie locale
solénoïdale sans prétendre que le projecteur global préserve le support.

**Limite.** \(\mathbb P_\phi\) n'est pas \(\mathbb P\). Il ignore les données
éloignées grâce au cutoff, au prix d'une correction harmonique et d'erreurs de
transition. Il ne justifie pas l'assertion fausse
\(\operatorname{supp}\mathbb P\operatorname{div}E
\subset\operatorname{supp}E\), ni (3).

### 2.3 Bradshaw--Tsai 2022 : expansion locale de pression

Zachary Bradshaw et Tai-Peng Tsai,
[*On the Local Pressure Expansion for the Navier--Stokes
Equations*](https://doi.org/10.1007/s00021-021-00637-4), *Journal of
Mathematical Fluid Mechanics* **24** (2022), article 3, DOI
`10.1007/s00021-021-00637-4`,
[`arXiv:2001.11526v1`](https://arxiv.org/abs/2001.11526v1).

**Statut.** Article publié.

**Décision de catalogue.** Cette source doit être ajoutée sous l'identifiant
proposé **`NS-SRC-0186`** : elle documente directement l'expansion locale de
pression et le gain d'une puissance dans le champ lointain. Elle ne doit pas
recevoir l'affirmation que le lemme Lorentz (2) y est démontré textuellement.

Le noyau de pression est

\[
K_{ij}(z)=\partial_i\partial_j\frac1{4\pi|z|},             \tag{15}
\]

homogène de degré \(-3\). Dans l'expansion locale, le champ lointain apparaît
par la différence

\[
K_{ij}(x-y)-K_{ij}(x_0-y),                                \tag{16}
\]

qui gagne une puissance et décroît comme \(|y|^{-4}\). Les théorèmes 1.4 et
1.5 relient, sous leurs hypothèses, formulation mild et expansion locale de
pression.

**Transfert.** (16) est l'ingrédient publié le plus proche de l'ordre \(-4\)
utilisé dans (6)--(11). La dérivée spatiale de la pression lointaine et la
soustraction d'une jauge constante sont deux expressions du même gain.

**Limite.** L'article n'énonce pas (2) pour un stress extérieur arbitraire en
\(L^{3/2,\infty}\), et ne fournit pas à lui seul la compacité de l'endpoint.

### 2.4 Bradshaw--Kukavica 2025 : structure des solutions faibles

Zachary Bradshaw et Igor Kukavica,
[*The structure of weak solutions to the Navier--Stokes
equations*](https://arxiv.org/abs/2508.01009v1),
`arXiv:2508.01009v1`, 1er août 2025.

**Statut.** Prépublication, non identifiée comme publiée à la date de veille.

Le théorème 1.4 relie les solutions faibles paraboliquement uniformément
locales à une représentation de pression locale, après transformation
transgaliléenne. Le théorème 1.5 impose des décroissances moyennes en grandes
balles sur la donnée et l'énergie locale. Dans la section 4, la pression
lointaine est contrôlée par un terme du type

\[
R\int_{|y|>2R}|y|^{-4}|u(y,s)|^2\,dy.                     \tag{17}
\]

**Transfert.** Cette prépublication confirme que la puissance \(-4\) gouverne
la pression lointaine après localisation.

**Limite.** Les hypothèses de moyenne à l'infini et la transformation de
référentiel ne sont pas remplacées par la seule borne faible-\(L^3\). Elle ne
construit pas la limite ancienne non triviale requise ici.

## 3. Le raccord publié le plus proche : Albritton--Barker

Dallas Albritton et Tobias Barker,
[*Localised necessary conditions for singularity formation in the
Navier--Stokes equations with curved
boundary*](https://doi.org/10.1016/j.jde.2020.06.009), *Journal of
Differential Equations* **269** (2020), 7529--7573, DOI
`10.1016/j.jde.2020.06.009`,
[`arXiv:1811.00507v2`](https://arxiv.org/abs/1811.00507v2).

**Équation et notion de solution.** Navier--Stokes incompressible 3D non
forcé, sur un domaine borné à bord \(C^2/C^3\), avec non-glissement sur la
portion de frontière concernée; solution faible adaptée au bord.

La proposition 2.2 sélectionne un anneau régulier et construit, au moyen d'un
cutoff et d'un correcteur de Bogovskiĭ,

\[
V=\Phi v+w,                                                \tag{18}
\]

qui coïncide avec la solution originale dans la région intérieure. La nouvelle
équation comporte une force \(f\) très régulière et localisée; le contrôle
spatial faible-\(L^3\) est préservé. Lors du blow-up, leurs équations
(4.13)--(4.14) redimensionnent la force avec un facteur cubique, et donnent

\[
\|f_n\|_{L^{p,3/2}(Q_n)}\to0
\quad\text{pour }p>9/5,                                   \tag{19}
\]

dans leur notation espace-temps.

La preuve dispose en outre de \(|v_n|\le1\), d'une estimation de Hölder et
d'une convergence locale forte. La normalisation conserve
\(|U(0)|=1\), ce qui interdit la limite nulle. La pression est décomposée en
une partie de Riesz/BMO et des parties harmoniques liées au bord; lorsque le
bord recule sous redimensionnement, son gradient harmonique s'annule. Le
résultat est une solution ancienne mild bornée sur \(\mathbb R^3\) ou le
demi-espace.

**Portée exacte.** C'est une preuve publiée du schéma

\[
\text{anneau déjà régulier}
\to\text{troncature solénoïdale}
\to f_n\to0\text{ fortement}
\to\text{compacité Hölder}
\to\text{limite ancienne non triviale}.                   \tag{20}
\]

Elle ne prouve pas (3). Les données indispensables et absentes de la seule
borne critique sont : l'anneau régulier, la normalisation \(L^\infty\), les
normes sous-critiques de la force, la compacité parabolique forte, le contrôle
des pressions harmoniques et la persistance ponctuelle de la singularité.

Sources publiées complémentaires :

- Tobias Barker et Christophe Prange,
  [*Localized smoothing for the Navier--Stokes equations and concentration
  of critical norms near singularities*](https://doi.org/10.1007/s00205-020-01495-6),
  *Archive for Rational Mechanics and Analysis* **236** (2020), 1487--1541,
  [`arXiv:1812.09115v2`](https://arxiv.org/abs/1812.09115v2). Ils obtiennent
  lissage local et concentration de normes critiques pour solutions d'énergie
  locale, y compris des extensions spatiales faible-\(L^3\), mais sous
  petitesse ou hypothèses locales supplémentaires.

- Hao Jia et Vladimír Šverák,
  [*Local-in-space estimates near initial time for weak solutions of the
  Navier--Stokes equations and forward self-similar
  solutions*](https://doi.org/10.1007/s00222-013-0468-x), *Inventiones
  Mathematicae* **196** (2014), 233--265,
  [`arXiv:1204.0529`](https://arxiv.org/abs/1204.0529). Leur contrôle local
  près du temps initial est un ingrédient de compacité, non une annulation de
  stress lointain.

- Gregory Seregin et Vladimír Šverák,
  [*Rescalings at possible singularities of Navier--Stokes equations in
  half-space*](https://doi.org/10.1090/S1061-0022-2014-01317-9),
  *St. Petersburg Mathematical Journal* **25** (2014), 815--833,
  [`arXiv:1302.0141`](https://arxiv.org/abs/1302.0141). Ils extraient des
  solutions anciennes mild bornées sous des hypothèses plus fortes et avec un
  traitement précis de la pression de bord.

Ces travaux montrent que l'annulation de la force est seulement une arête du
graphe de preuve; elle ne remplace pas l'arête de compacité/non-trivialité.

## 4. Seuils faible-\(L^3\) et faible-\(L^{3/2}\)

### 4.1 Produit critique

L'inégalité de Hölder dans les espaces de Lorentz donne

\[
\|u\otimes u\|_{L^{3/2,\infty}}
\le C\|u\|_{L^{3,\infty}}^2.                              \tag{21}
\]

La compatibilité d'échelle est parfaite. C'est suffisant pour faire disparaître
la queue extérieure par (2), pas pour passer le terme quadratique à la limite.

Pour \(1<p<\infty\), \(L^{p,\infty}\) peut être vu comme dual de
\(L^{p',1}\) dans le cadre usuel. Une suite bornée admet donc des extractions
faible-étoile après choix de prédual. Mais \(L^{p,\infty}\) est non séparable
et non réflexif, et la convergence faible-étoile de \(u_n\) ne détermine pas
la limite de \(u_n\otimes u_n\). Il faut une compacité locale forte issue, par
exemple, d'estimations d'énergie locale et d'une borne sur la dérivée
temporelle.

### 4.2 Régularité endpoint publiée sous petitesse

Yuwen Luo et Tai-Peng Tsai,
[*Regularity Criteria in Weak \(L^3\) for 3D Incompressible Navier--Stokes
Equations*](https://arxiv.org/abs/1310.8307v5), *Funkcialaj Ekvacioj* **58**
(2015), 387--404.

**Statut.** Article publié; version arXiv v5 du 2 avril 2014 auditée.

Le théorème 1.1 considère une solution distributionnelle sur un cylindre
borné, avec \(p\in L^m_tL^1_x\), \(m>2\), et impose la petitesse de
\(\|u\|_{L^\infty_tL^{3,\infty}_x}\). Il conclut à la bornitude dans un
cylindre intérieur.

**Limite.** Il s'agit d'un critère epsilon-régulier avec hypothèse de pression,
non d'un théorème pour une borne faible-\(L^3\) arbitrairement grande. Le
symbole historique \(L_{3,\infty}\) doit aussi être lu avec prudence : suivant
les auteurs, il peut noter \(L^\infty_tL^3_x\), tandis que
\(L^{3,\infty}_x\) désigne ici l'espace de Lorentz spatial.

### 4.3 Trois défauts de compacité séparés

1. **Translation.** Si \(U\in L^{3,\infty}\) et
   \(u_n(x)=U(x-ne_1)\), alors la norme critique est constante mais
   \(u_n\to0\) localement. Une normalisation globale ne préserve pas la
   non-trivialité au point observé.

2. **Concentration.** La suite
   \(u_n(x)=nU(nx)\) conserve la norme faible-\(L^3\) et peut converger vers
   zéro sur tout compact évitant l'origine. La masse critique peut se
   concentrer sans convergence forte.

3. **Oscillation.** Des champs solénoïdaux oscillants peuvent converger
   faiblement vers zéro alors que leurs produits quadratiques conservent un
   défaut de Reynolds. Une borne faible-\(L^3\) ne supprime pas ce défaut.

Ces exemples fonctionnels ne sont pas nécessairement des solutions de (1),
mais ils réfutent toute preuve qui prétendrait tirer la compacité requise de la
seule topologie de Lorentz.

## 5. Veille différentielle 2025--2026

La recherche a couvert les versions primaires disponibles au 15 août 2026,
avec les combinaisons *Navier--Stokes local pressure*, *Leray projection far
field*, *ancient solution weak L3*, *blow-up compactness*, *Type I/II*,
*computer-assisted singularity* et *self-similar*.

### 5.1 Yu 2026 : réduction conditionnelle, pas solution ancienne

Runlong Yu,
[*Invisible Defect Cascades for Navier--Stokes
Regularity*](https://arxiv.org/abs/2606.12756v1),
`arXiv:2606.12756v1`, 10 juin 2026.

**Statut.** Prépublication.

L'article propose une architecture de défauts dyadiques. Ses propres sections
12 et 15 maintiennent comme hypothèses ou cibles à démontrer l'extraction du
défaut, la déplétion observable et la croissance de fenêtres mobiles. L'objet
limite n'est explicitement ni une solution ancienne de Navier--Stokes ni un
élément critique compact.

**Verdict.** Aucun raccord fermé vers (2) ou (3). Cette source ne peut être
citée comme preuve d'une cascade invisible ou d'une régularité Clay.

### 5.2 Seregin 2025--2026 : scénarios Type II et limites Euler

Gregory Seregin,
[*A note on certain scenarios of Type II blowups for the Navier--Stokes
equations*](https://arxiv.org/abs/2507.08733v2),
`arXiv:2507.08733v2`, v1 du 11 juillet 2025, v2 du 3 janvier 2026.

Sous des hypothèses supplémentaires de type énergie/pression invariantes par
échelle, le théorème 3.1 produit, après une échelle de type Euler, une solution
ancienne d'Euler non triviale satisfaisant une inégalité d'énergie locale. Les
exclusions ultérieures ajoutent une hypothèse de type
Ladyzhenskaya--Prodi--Serrin.

Gregory Seregin,
[*On potential Type II blowups for the Navier--Stokes
equations*](https://arxiv.org/abs/2606.29468v1),
`arXiv:2606.29468v1`, 28 juin 2026.

Cette prépublication exclut d'autres scénarios conditionnels et étudie des
structures Euler anciennes, notamment axisymétriques.

**Verdict commun.** Une limite ancienne d'Euler obtenue sous une échelle Type
II n'est pas la solution ancienne parabolique de (1). Ces résultats ne ferment
ni la queue de projection ni la compacité faible-\(L^3\).

### 5.3 Pineau--Vicol 2026 : profils tournants particuliers

Ben Pineau et Vlad Vicol,
[*On rotated backwards self-similar solutions to the 3D Navier--Stokes
equations*](https://arxiv.org/abs/2607.09619v2),
`arXiv:2607.09619v2`, v1 du 10 juillet 2026, v2 du 6 août 2026.

**Statut.** Prépublication.

Les auteurs démontrent des théorèmes de Liouville pour des profils rétrogrades
auto-similaires ou discrètement auto-similaires avec rotation, sous hypothèse
Type I et régimes extrêmes du paramètre de rotation. Ils obtiennent également
un critère local lié à une auto-similarité approchée à un temps.

**Verdict.** L'exclusion d'une classe d'ansatz n'exclut pas toute solution
ancienne, encore moins toute singularité. Aucune implication vers (3).

### 5.4 Non-unicité récente : classes non transférables au problème Clay

Alexey Cheskidov, Mimi Dai et Stan Palasek,
[*Instantaneous Type I blow-up and non-uniqueness of smooth solutions to the
Navier--Stokes equations*](https://arxiv.org/abs/2511.09556v2),
`arXiv:2511.09556v2`, v1 du 12 novembre 2025, v2 du 12 janvier 2026.

Sur \(\mathbb T^d\), \(d\ge2\), les auteurs construisent des solutions faibles
lisses en espace à chaque temps et hors d'un instant critique. Ils précisent
que ces solutions ne sont ni dans \(L^\infty_tL^2_x\) ni dans
\(L^2_tH^1_x\) près du blow-up : elles ne sont donc pas Leray--Hopf. Il ne
s'agit pas d'un blow-up d'une solution classique issue de données Clay.

Thomas Hou, Yixuan Wang et Changhe Yang,
[*Nonuniqueness of Leray--Hopf solutions to the unforced incompressible 3D
Navier--Stokes equation*](https://arxiv.org/abs/2509.25116v2),
`arXiv:2509.25116v2`, v1 du 29 septembre 2025, v2 du 19 mars 2026.

**Statut.** Prépublication revendiquant une preuve assistée par ordinateur;
le certificat et le code n'ont pas fait l'objet d'une reproduction
indépendante dans cette veille.

La construction annoncée est sur \(\mathbb R^3\), non forcée, avec donnée
compactement supportée mais singulière à l'origine, appartenant à \(L^q\)
pour \(q<3\). Elle emploie des solutions auto-similaires directes et une
localisation de Bogovskiĭ. Même si la certification est correcte, non-unicité
faible depuis une donnée critique singulière n'implique ni blow-up classique
depuis donnée lisse ni fermeture de (3).

Matei Coiculescu et Stan Palasek,
[*Non-uniqueness of smooth solutions of the Navier--Stokes equations from
critical data*](https://doi.org/10.1007/s00222-025-01396-z), *Inventiones
Mathematicae* **244** (2026), 165--219,
[`arXiv:2503.14699v2`](https://arxiv.org/abs/2503.14699v2).

**Statut.** Article publié.

Les données initiales sont dans l'espace critique \(BMO^{-1}\), et les
solutions sont lisses pour \(t>0\). La non-unicité à ce niveau de donnée ne
fournit pas une singularité d'une solution classique issue d'une donnée
lisse, ni une solution ancienne extraite par le mécanisme présent.

### 5.5 Résultat négatif de la veille récente

Aucun texte primaire 2025--2026 audité ne démontre simultanément :

- un cutoff extérieur pour une suite seulement bornée dans
  \(L^\infty_tL^{3,\infty}_x\);
- la disparition quantitative de toute la force projetée;
- une compacité locale forte suffisante pour le terme quadratique;
- le passage de la pression et de l'inégalité d'énergie locale;
- une normalisation empêchant la limite nulle;
- une solution ancienne Navier--Stokes appartenant à une classe de rigidité
  effectivement couverte.

Il n'existe donc pas de fermeture bibliographique récente du verrou du cycle.

## 6. Lemme transférable unique

> **Lemme de fuite locale critique pour un stress extérieur.** Soient
> \(\rho>0\), \(L\ge2\rho\), et
> \(E_L\in L^{3/2,\infty}(\mathbb R^3;\mathbb R^{3\times3})\) tel que
> \(E_L=0\) presque partout dans \(B_L\). Alors
> \(\mathbb P\operatorname{div}E_L\) est lisse dans \(B_L\) et, pour tout
> multi-indice \(\alpha\),
> \[
> \|\partial^\alpha\mathbb P\operatorname{div}E_L
> \|_{L^\infty(B_\rho)}
> \le C_\alpha L^{-3-|\alpha|}
> \|E_L\|_{L^{3/2,\infty}}.
> \]
> Si \(E_L=E_L(t)\) et la norme est uniformément bornée pour presque tout
> \(t\), la conclusion est uniforme en temps.

**Statut.** Les noyaux de pression/Leray, leur localisation et le gain
lointain sont publiés notamment dans Bradshaw--Tsai, Wolf et Kwon. La
sommation faible-\(L^{3/2}\) de (9)--(11) est la dérivation de ce cycle.
L'énoncé complet doit rester
`PUBLISHED_INGREDIENTS + AI_INTERNAL_DERIVATION` jusqu'à preuve séparée et
catalogage, pas `PAPER_PROOF`.

**Ce que le lemme donne.** La force projetée disparaît dans
\(C^m_{\mathrm{loc}}\) pour tout \(m\), à temps fixé et uniformément si la
borne temporelle est uniforme. Dans la formulation faible solénoïdale, on a
même la disparition exacte (13).

**Ce qu'il ne donne pas.** Il ne construit pas la suite \(u_n\), n'établit
pas de borne d'énergie locale, ne passe pas \(u_n\otimes u_n\) à la limite,
ne préserve pas une singularité et ne fournit aucun théorème de rigidité sur
la limite ancienne.

## 7. Passe contradictoire reproductible

### Test A — support après projection

Prendre un tenseur lisse compactement supporté dans une petite boule centrée
en \(Re_1\), avec un moment tensoriel générique non nul. Dans une boule autour
de l'origine,
\(\operatorname{div}E_R=0\) exactement, mais (6) donne en général

\[
\mathbb P\operatorname{div}E_R(0)
=-\int \nabla^3\Gamma(-y):E_R(y)\,dy\ne0.                 \tag{22}
\]

**Résidu certifié analytiquement :** la projection globale ne préserve pas le
support; sa queue est de taille générique \(R^{-4}\|E_R\|_{L^1}\), compatible
avec (2).

### Test B — mauvais noyau

Remplacer \(\mathbb P\operatorname{div}E\) par \(\mathbb Pf\). La partie
non locale utilise alors \(\nabla^2\Gamma\), donc \(|x|^{-3}\), et le calcul
de (11) perd une puissance.

**Résidu certifié :** toute dérivation doit enregistrer si la donnée est un
vecteur ou la divergence d'un tenseur.

### Test C — norme critique sans non-trivialité

Utiliser \(u_n(x)=U(x-ne_1)\) avec un profil solénoïdal non nul
\(U\in C_c^\infty\). Alors

\[
\|u_n\|_{L^{3,\infty}}=\|U\|_{L^{3,\infty}},
\qquad u_n\to0\quad\text{dans }C^\infty_{\mathrm{loc}}.   \tag{23}
\]

**Résidu certifié :** la norme uniforme ne localise pas la concentration et
ne rend pas la limite ancienne non nulle.

### Test D — terme quadratique

Une convergence faible-étoile dans \(L^{3,\infty}\) ne permet pas de
conclure

\[
u_n\otimes u_n\rightharpoonup u\otimes u.                 \tag{24}
\]

Des oscillations solénoïdales conservent un tenseur de Reynolds. La fermeture
de l'équation exige une compacité forte locale ou une preuve indépendante de
disparition du défaut.

**Résidu :** le lemme de queue traite l'erreur extérieure, pas le défaut
quadratique intérieur.

### Test E — espace entier contre tore

Sur \(\mathbb T^3\), il n'existe pas de « support allant à l'infini ». Un
argument de blow-up doit d'abord redimensionner le tore en un domaine dont la
période tend vers l'infini, puis contrôler les images périodiques et la jauge
de pression.

**Résidu Clay :** (2) est directement un lemme sur \(\mathbb R^3\); son
emploi dans le cas périodique exige un raccord de domaine séparé.

### Test F — admissibilité de la limite

Même si la force tend vers zéro distributionnellement, il faut montrer que la
limite satisfait la notion voulue : solution distributionnelle, adaptée,
d'énergie locale ou mild. Le passage de l'inégalité d'énergie locale contient
des termes de pression et des produits qui ne sont pas continus pour la seule
topologie faible-\(L^3\).

**Résidu Clay :** absence actuelle d'un théorème de compacité endpoint qui
préserve à la fois l'équation, l'admissibilité et la non-trivialité.

## 8. Graphe de transfert et écart exact avec Clay

| arête | statut | perte ou hypothèse restante |
|---|---|---|
| \(u_n\in L^{3,\infty}\Rightarrow u_n\otimes u_n\in L^{3/2,\infty}\) | classique, Hölder-Lorentz | aucune pour la norme seule |
| stress extérieur uniforme \(\Rightarrow\) queue projetée \(O(L^{-3})\) | ingrédients publiés + dérivation interne (2) | support extérieur et norme globale uniforme |
| source extérieure \(\Rightarrow0\) sur tests solénoïdaux compacts | identité distributionnelle | aucune, lorsque les supports sont réellement disjoints |
| borne faible-\(L^3\) \(\Rightarrow\) sous-suite faible-étoile | fonctionnel classique | topologie trop faible pour le produit |
| sous-suite \(\Rightarrow\) solution NS ancienne | **manquante à cet endpoint seul** | compacité forte, pression, énergie locale |
| solution ancienne \(\Rightarrow\) non triviale | **manquante sans normalisation persistante** | fuite par translation/concentration |
| solution ancienne faible-\(L^3\) \(\Rightarrow0\) | **théorème de rigidité général manquant** | les résultats publiés couvrent petitesse, bornitude ou scénarios spéciaux |
| rigidité \(\Rightarrow\) exclusion du blow-up Clay | conditionnelle | il faut que la réduction couvre la formulation Clay exacte |

Le premier maillon utile du cycle est donc (2), mais le prochain verrou n'est
plus la pression lointaine. Il est la construction d'un théorème de compacité
locale qui transforme les bornes effectivement disponibles après cutoff en
une solution ancienne admissible et non triviale. Albritton--Barker fournit le
modèle sous hypothèses plus fortes; toute extension doit identifier précisément
quelle estimation remplace leur borne \(L^\infty\)/Hölder.

## 9. Sources primaires et empreintes SHA256

Les empreintes portent sur les octets PDF effectivement téléchargés et audités
le 15 août 2026. Elles détectent une modification ultérieure du fichier servi;
elles ne valent pas validation mathématique ni certification éditoriale.

| source PDF primaire | version/état | octets | SHA256 |
|---|---:|---:|---|
| `https://arxiv.org/pdf/1611.01482` | Wolf v1, publié en 2017 | 377649 | `4E8BE26FBDE44FA9C506FAEB97FDB3055D4CF11CD5D7B3FF6D9C91873698325D` |
| `https://arxiv.org/pdf/2104.03160` | Kwon v3, publié en 2023 | 340543 | `BD122B4E50573146BC25D944364E27E3B168D0DDB892929B3726FD2650027C73` |
| `https://arxiv.org/pdf/2001.11526` | Bradshaw--Tsai v1, publié en 2022 | 383699 | `C264534A59BA09E2AFC9C5CFE3AA6FDC8EDFBC8C35C5207C174D6ACA83D267AF` |
| `https://arxiv.org/pdf/1811.00507` | Albritton--Barker v2, publié en 2020 | 476336 | `FDD91E657B5CF503286B4E45CC084C12C8B202AAF24BCDAD67EDEA46EDFA4102` |
| `https://arxiv.org/pdf/1812.09115` | Barker--Prange v2, publié en 2020 | 505915 | `D1C0D26270F784697460DC5CE56DC5599CFEABCE40C0F3AAA35372296BC7D78D` |
| `https://arxiv.org/pdf/1310.8307` | Luo--Tsai v5, publié en 2015 | 237387 | `A33F22D2404EA171A7AB5464E560ACD7F839048B07F50B82DE18761672B72F69` |
| `https://arxiv.org/pdf/1204.0529` | Jia--Šverák, publié en 2014 | 304378 | `1E8685FBE09C669854357278010F345FA5C98845C5888BA6720936A0B3F1591F` |
| `https://arxiv.org/pdf/1302.0141` | Seregin--Šverák, publié en 2014 | 234572 | `050212901E7CDBD1687618770DA6D3705DE9655CE94E3CE3555558706A4993BC` |
| `https://arxiv.org/pdf/2508.01009` | Bradshaw--Kukavica v1, prépublication | 442970 | `8E94A4B861477B3B2FCC7B70BA9F26EC9EC7F3B3CFE0E54C4EF280BEF5F144AF` |
| `https://arxiv.org/pdf/2606.12756` | Yu v1, prépublication | 863017 | `26CB6469578CB8CDFAD93BA85928E688893F7EB8F4C030BCE783E0FAFD0E7EFF` |
| `https://arxiv.org/pdf/2507.08733` | Seregin v2, prépublication | 329495 | `EACE90E2F799C8548BC2968DF4D6B7F51A8018CF8DFE39379F14A1C3ACCB8F94` |
| `https://arxiv.org/pdf/2606.29468` | Seregin v1, prépublication | 286905 | `3F895B24C995A2A664578B5E43EFE5CAE313E745FDCEEAAD8B3D6A00987436FD` |
| `https://arxiv.org/pdf/2607.09619` | Pineau--Vicol v2, prépublication | 617825 | `379591AA3C1036C9140702EBE71AAAB309FE207439A57DB5CEFF893F15D0AE8E` |
| `https://arxiv.org/pdf/2511.09556` | Cheskidov--Dai--Palasek v2, prépublication | 713631 | `16C366266A1DDAD7DF910A5D263A9B324ABD01B3A9E9B457B34F31EF5067FCC7` |
| `https://arxiv.org/pdf/2509.25116` | Hou--Wang--Yang v2, prépublication assistée par ordinateur | 2148337 | `2D369EADE29BD0D5E8DFC6D7DEF7ED19B8282AB4450860978F3691176D9F8318` |
| `https://arxiv.org/pdf/2503.14699` | Coiculescu--Palasek v2, publié en 2026 | 639920 | `040C5ABFE8471A709E56E5A5F77DDF5F6D01E6E250185721AE446D2A30F6B6EA` |

## Conclusion

La veille valide un résultat négatif précis et utile. La non-localité de la
pression n'empêche pas une force en forme divergence, soutenue au-delà de
\(B_L\) et uniformément bornée dans \(L^{3/2,\infty}\), de disparaître sur
les compacts : sa queue projetée est \(O(L^{-3})\), avec toutes les dérivées.
Ce maillon est analytiquement simple, critique par échelle et falsifiable.

Il ne résout toutefois pas le verrou central. Ni les articles publiés sur la
pression locale, ni les troncatures existantes, ni les prépublications
2025--2026 ne transforment une seule borne uniforme faible-\(L^3\) en solution
ancienne Navier--Stokes admissible non triviale. Le résidu certifié du cycle
est donc :

\[
\boxed{\text{compacité locale forte + persistance de non-trivialité à
l'endpoint }L^{3,\infty}.}
\]

Le prochain travail à forte valeur informationnelle est de comparer les
estimations disponibles pour la suite tronquée aux hypothèses exactes du
schéma Albritton--Barker, puis d'isoler le premier déficit quantitatif : borne
temporelle, énergie locale, pression harmonique ou normalisation ponctuelle.
