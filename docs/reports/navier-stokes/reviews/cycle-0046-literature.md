# Cycle 0046 — persistance temporelle de la concentration Type I et non-trivialité ancienne

**Date de coupure :** 15 août 2026

**Nature :** veille primaire contradictoire indépendante

**Objet borné :** déterminer si la concentration faible-\(L^3\) de
Barker--Prange est disponible à chaque temps tardif, puis si son intégration
après zoom parabolique suffit à préserver la non-trivialité d'une limite
ancienne sous convergence forte \(L^3\) espace-temps.

Le cadre est Navier--Stokes incompressible tridimensionnel non forcé sur
\(\mathbb R^3\), de viscosité normalisée à un :

\[
 \partial_tu-\Delta u+(u\cdot\nabla)u+\nabla p=0,
 \qquad \nabla\cdot u=0.                                  \tag{1}
\]

## Verdict

1. **Le quantificateur de Barker--Prange est “pour tout temps assez proche
   de \(T^*\)”, pas “le long d'une suite”.** Le théorème 2 imprimé donne la
   concentration \(L^3\) pour tout \(t\in(t_*,T^*)\). Le texte qui suit le
   théorème affirme explicitement que l'appendice B étend ce résultat à
   \(L^{3,\infty}\), et l'appendice remplace les quatre blocs nécessaires des
   sections 2--4 par leurs versions de Lorentz. La version faible-\(L^3\)
   hérite donc du même quantificateur temporel.

2. **Ce quantificateur ferme conditionnellement la non-trivialité
   espace-temps.** Après zoom parabolique autour du point singulier fixe,
   la minoration faible-\(L^3\) vaut à chaque temps d'une bande normalisée
   \([-b,-a]\), \(0<a<b\). Comme

   \[
   \|f\|_{L^{3,\infty}(E)}^3\le \int_E|f|^3,              \tag{2}
   \]

   elle donne une minoration uniforme de l'intégrale cubique sur un cône
   parabolique. Une convergence forte \(L^3_{\rm loc}\) espace-temps transmet
   cette intégrale à la limite et exclut la limite ancienne nulle.

3. **La conclusion précédente est une dérivation du laboratoire, pas un
   théorème énoncé par Barker--Prange.** Leur article fournit la persistance
   temporelle, mais pas la compacité forte \(L^3\) de la suite de zooms.
   Cette compacité exige encore, par exemple, les hypothèses vitesse/pression
   du lemme A.2 d'Albritton--Barker ou la classe scindée de
   Barker--Seregin--Šverák.

4. **La non-trivialité intégrée est plus faible que la persistance de la
   singularité.** Elle montre \(U\not\equiv0\) sur un intervalle négatif;
   elle ne montre ni que \((0,0)\) reste singulier, ni que \(U(0,0)\ne0\),
   ni même qu'une trace forte existe à \(t=0\). La proposition A.5
   d'Albritton--Barker et leur normalisation ponctuelle ferment précisément
   ces conclusions plus fortes, sous des hypothèses supplémentaires.

5. **Une translation temporellement mobile n'est pas gratuite.** Barker--
   Prange concentre au point singulier spatial fixe. Il est donc préférable
   de zoomer autour de ce point. Si des centres normalisés mobiles restent
   bornés, une grande boule fixe suffit encore pour l'argument intégré. S'ils
   s'échappent, la masse peut disparaître de tout compact. Si l'on change
   réellement de coordonnées avec un centre dépendant du temps, l'équation
   acquiert un terme de dérive et la compacité doit être redémontrée.

6. **La veille 2025--2026 ne fournit pas le raccord inconditionnel
   manquant.** Les nouveaux résultats audités traitent de scénarios Type II
   avec zoom eulérien, de données approximativement axisymétriques, ou de
   profils auto-similaires tournés. Aucun ne remplace la porte “forte
   \(L^3_{\rm loc}\)” pour une suite Type I arbitraire uniquement bornée dans
   \(L^\infty_tL^{3,\infty}_x\).

## 1. Barker--Prange 2020 : source, version et notion de solution

Tobias Barker et Christophe Prange,
[*Localized Smoothing for the Navier--Stokes Equations and Concentration of
Critical Norms Near Singularities*](https://doi.org/10.1007/s00205-020-01495-6),
*Archive for Rational Mechanics and Analysis* **236** (2020), 1487--1541,
DOI `10.1007/s00205-020-01495-6`,
[`arXiv:1812.09115v2`](https://arxiv.org/abs/1812.09115v2).

**Statut.** Preuve analytique publiée. Le PDF arXiv v2 et le manuscrit
auteur accepté déposé à Warwick ont été audités. Le théorème de lissage porte
sur des solutions d'énergie locale; l'application de concentration porte sur
une solution de Leray--Hopf d'énergie finie sur
\(\mathbb R^3\times(0,\infty)\). Il n'y a ni force, ni frontière, ni modèle
modifié.

La solution est supposée développer ses premières singularités au temps
\(T^*>0\), et \((x^*,T^*)\) est supposé singulier au sens où aucune boule
parabolique rétrospective centrée en ce point ne porte une borne
\(L^\infty_{x,t}\). Le théorème ne construit pas cette singularité.

### 1.1 Hypothèse Type I exacte

Pour \(M<\infty\) et \(r_0\in(0,\infty]\), le théorème 2 suppose

\[
 \sup_{\bar x\in\mathbb R^3}
 \sup_{0<r<r_0}
 \sup_{T^*-r^2<t<T^*}
 r^{-1/2}\|u(t)\|_{L^2(B_r(\bar x))}\le M.                \tag{3}
\]

Cette borne de Morrey-énergie locale est critique. Elle est uniforme en
centre, échelle et temps dans la fenêtre rétrospective; elle n'est pas une
conséquence de l'inégalité d'énergie globale.

La borne plus spéciale

\[
 \sup_{0<t<T^*}\|u(t)\|_{L^{3,\infty}(\mathbb R^3)}\le K \tag{4}
\]

implique (3) avec \(M=C K\) et \(r_0=\infty\), par l'inclusion locale
\(L^{3,\infty}\hookrightarrow L^2\) sur une boule. La réciproque n'est pas
établie.

### 1.2 Théorème 2 : le quantificateur temporel contrôlé

Il existe un seuil universel \(\gamma_3>0\), un temps normalisé
\(S_3^*(M)\in(0,1/4]\) et

\[
 t_*=T^*-S_3^*(M)r_0^2                                  \tag{5}
\]

(avec la convention physique \(t_*\ge0\), et \(t_*=0\) lorsque
\(r_0=\infty\)) tels que

\[
 \|u(t)\|_{L^3(B(x^*,c_3(M)\sqrt{T^*-t}))}>\gamma_3,
 \qquad c_3(M)=\frac{2}{\sqrt{S_3^*(M)}},                 \tag{6}
\]

**pour tout** \(t\in(t_*,T^*)\).

La preuve, section 4.2, est la contraposée du lissage local. Si (6) échouait
à un seul temps \(t_0\) tardif, le zoom de facteur

\[
 \lambda=\sqrt{\frac{T^*-t_0}{S_3^*(M)}}                 \tag{7}
\]

produirait une donnée petite dans \(L^3(B_2)\) et bornée dans
\(L^2_{\rm uloc}\); le théorème 1 rendrait alors \((x^*,T^*)\) régulier.
Cette contradiction fonctionne séparément pour chaque \(t_0\), d'où le
quantificateur “tout temps”.

L'article contraste lui-même ce résultat avec une concentration antérieure
obtenue le long d'une suite \(t_n\uparrow T^*\), puis avec une amélioration
à tout temps dont le centre \(x(t)\) n'était pas identifié. Ici le centre est
le point singulier fixe \(x^*\).

### 1.3 Ce que l'appendice B prouve exactement

Le théorème 2 est imprimé en \(L^3\); il n'existe pas dans l'article un
second théorème autonome réénonçant tous les symboles en
\(L^{3,\infty}\). Immédiatement après (6), les auteurs écrivent qu'ils
prouvent dans l'appendice B la concentration de la norme critique
\(L^{3,\infty}\). Cet appendice :

- définit la quasi-norme
  \(\|f\|_{L^{3,\infty}}=\sup_{\alpha>0}
  \alpha|\{|f|>\alpha\}|^{1/3}\);
- remplace le mild petit \(L^3\) par le mild petit
  \(L^{3,\infty}\);
- répare l'itération de Morrey et la pression par les inégalités de Hunt et
  d'O'Neil;
- remplace les estimations critiques des sections 3 et 4, y compris la
  construction de l'extension solénoïdale locale.

La contraposition du même lissage fournit donc des constantes propres
\(\gamma_w>0\), \(S_w^*(M)>0\) telles que

\[
 \boxed{
 \|u(t)\|_{L^{3,\infty}
 (B(x^*,c_w(M)\sqrt{T^*-t}))}>\gamma_w,
 \quad c_w(M)=\frac{2}{\sqrt{S_w^*(M)}} }
                                                               \tag{8}
\]

pour tout temps tardif soumis aux mêmes quantificateurs. Les constantes
Lorentz ne sont pas évaluées numériquement et ne doivent pas être identifiées
aux constantes optimales du cas \(L^3\).

**Conclusion bibliographique.** (8) est `PAPER_PROOF` lorsque le théorème 2
et l'appendice B sont cités ensemble. La reformulation avec les noms
\(\gamma_w,S_w^*\) est une normalisation prudente du laboratoire.

## 2. Lemme transférable : intégrer avant de passer à la limite

Cette section est une `AI_INTERNAL_DERIVATION`, soumise à l'attaque
ci-dessous. Elle ne doit pas recevoir le statut `PAPER_PROOF`.

Soit une suite d'échelles \(r_n\downarrow0\) et zoomons au point singulier
fixe :

\[
 U_n(y,s)=r_n u(x^*+r_n y,T^*+r_n^2s),
 \qquad s<0.                                                \tag{9}
\]

L'échelle faible-\(L^3\) est invariante. Pour
\(I=[-b,-a]\Subset(-\infty,0)\), \(0<a<b\), l'instant physique le plus
ancien de cette bande est \(T^*-br_n^2\). Il appartient à \((t_*,T^*)\)
pour tout \(n\) assez grand, uniformément pour \(s\in I\). L'équation (8)
devient alors

\[
 \|U_n(s)\|_{L^{3,\infty}
 (B(0,c_w(M)\sqrt{-s}))}>\gamma_w
 \quad\text{pour tout }s\in I.                            \tag{10}
\]

Pour toute fonction mesurable \(f\) sur \(E\), la convention de quasi-norme
de l'article donne

\[
 \|f\|_{L^{3,\infty}(E)}^3
 =\sup_{\alpha>0}\alpha^3|\{|f|>\alpha\}\cap E|
 \le\int_E|f|^3.                                          \tag{11}
\]

En posant le cône tronqué

\[
 \mathcal C_I=
 \{(y,s):s\in[-b,-a],\ |y|<c_w(M)\sqrt{-s}\},             \tag{12}
\]

(10)--(11) impliquent

\[
 \int_{\mathcal C_I}|U_n|^3\,dy\,ds
 \ge (b-a)\gamma_w^3.                                    \tag{13}
\]

Le cône est contenu dans le cylindre fixe
\(B(0,c_w(M)\sqrt b)\times[-b,-a]\). Supposons maintenant la porte de
compacité

\[
 U_n\longrightarrow U
 \quad\text{fortement dans }L^3_{\rm loc}
 (\mathbb R^3\times(-\infty,0)).                           \tag{14}
\]

Alors \(|U_n|^3\to|U|^3\) dans \(L^1\) sur le cylindre fixe. En passant à
la limite dans (13),

\[
 \boxed{
 \int_{\mathcal C_I}|U|^3\,dy\,ds
 \ge(b-a)\gamma_w^3>0.}                                  \tag{15}
\]

Ainsi \(U\not\equiv0\). L'argument ne requiert aucune convergence forte de
la trace \(U_n(\cdot,0)\) et évite exactement le contre-profil de couche
terminale qui annule une normalisation portée sur une seule tranche.

### 2.1 Ce qui est publié et ce qui manque

| maillon | statut | commentaire |
|---|---|---|
| (3) + point singulier \(\Rightarrow\) (8) à tout temps tardif | publié, Barker--Prange | citer théorème 2 **et** appendice B |
| (8) \(\Rightarrow\) (13) | dérivation élémentaire | dépend de la quasi-norme de distribution (11) |
| (14) \(\Rightarrow\) (15) | dérivation élémentaire | vraie sur tout compact éloigné de \(s=0\) |
| borne faible-\(L^3\) Type I \(\Rightarrow\) (14) pour une suite arbitraire | **manquant** | énergie locale, pression endpoint et stabilité de classe à établir |
| (15) \(\Rightarrow\) singularité de \(U\) en \((0,0)\) | **faux sans entrée supplémentaire** | une solution ancienne lisse non nulle satisfait la conclusion non-triviale |

Le lemme A.2 d'Albritton--Barker fournit (14) pour des solutions faibles
adaptées si la vitesse et la pression possèdent uniformément les bornes
fortes \(L^3\) et \(L^{3/2}\) sur les cylindres. Le théorème de stabilité de
Barker--Seregin--Šverák fournit aussi une forte \(L^s_{\rm loc}\), notamment
pour \(s=3\), mais dans leur classe forward scindée en flot calorique et
correcteur énergétique. Barker--Prange 2020 ne démontre aucune de ces portes
pour la seule borne de vitesse (4).

## 3. Translation fixe, centre mobile et perte de compacité

La translation spatiale fixe \(x\mapsto x-x^*\) est une symétrie exacte de
(1). Barker--Prange donne (8) autour de ce même \(x^*\) à chaque temps; il
n'est donc pas nécessaire de sélectionner une trajectoire de centres.

Trois situations doivent être séparées.

### 3.1 Décalage normalisé borné

Si un autre zoom utilise des centres constants \(x_n\) tels que

\[
 \frac{|x_n-x^*|}{r_n}\le A,                              \tag{16}
\]

les boules de (10) sont contenues, dans les nouvelles coordonnées, dans
\(B(0,A+c_w\sqrt b)\). La minoration intégrée sur cette grande boule fixe
passe encore sous (14). La localisation exacte du cône peut bouger, mais la
non-trivialité subsiste.

La même conclusion scalaire reste vraie pour des centres mesurables
dépendant de \(s\), si leur décalage normalisé est uniformément borné sur
\(I\) et si l'on conserve des coordonnées fixes : on intègre simplement sur
une boule englobante.

### 3.2 Centre qui s'échappe

Si \(|x_n-x^*|/r_n\to\infty\), une forte convergence locale autour de
\(x_n\) ne voit plus nécessairement la masse centrée en \(x^*\). Inversement,
un théorème ne fournissant qu'un centre \(x(t)\) à chaque temps, sans borne
sur sa trajectoire normalisée, ne suffit pas à construire un profil local
non nul. C'est précisément la différence entre la concentration ancienne à
centre libre rappelée dans l'introduction de Barker--Prange et leur théorème
au point singulier fixé.

### 3.3 Changement de coordonnées réellement mobile

Pour \(V_n(y,s)=U_n(y+a_n(s),s)\), la dérivation temporelle donne un terme
additionnel \(-a_n'(s)\cdot\nabla V_n\), selon la convention de signe. Une
borne de \(a_n\) ne contrôle pas \(a_n'\); oscillations et sauts peuvent
détruire l'équicontinuité temporelle. Sans contrôle de variation de la
trajectoire et sans pression recalculée, \(V_n\) n'est pas une suite de
solutions de (1) dans le cadre compact invoqué. Le choix conservateur est le
zoom fixe (9).

## 4. Comparaison avec Albritton--Barker

Dallas Albritton et Tobias Barker,
[*Localised Necessary Conditions for Singularity Formation in the
Navier--Stokes Equations with Curved Boundary*](https://doi.org/10.1016/j.jde.2020.06.009),
*Journal of Differential Equations* **269** (2020), 7529--7573,
DOI `10.1016/j.jde.2020.06.009`,
[`arXiv:1811.00507v2`](https://arxiv.org/abs/1811.00507v2).

### 4.1 Proposition A.5 : persister comme point singulier

Pour des solutions faibles adaptées au bord aplati, la proposition A.5
suppose

\[
 v_k\to v\text{ fortement dans }L^3(Q^+),
 \qquad p_k\rightharpoonup p\text{ dans }L^{3/2}(Q^+),     \tag{17}
\]

ainsi qu'une explosion \(L^\infty\) persistante sur chaque cylindre
parabolique centré en l'origine. La ligne (A.21) imprime
\(L^\infty(B^+(R))\), mais la preuve et (A.23)--(A.24) utilisent
\(Q^+(R)\); la lecture opérationnelle est donc cylindrique. La conclusion
est que la limite possède un point singulier à l'origine.

La preuve est une contraposée : si la limite était bornée sur un petit
cylindre, la forte convergence \(L^3\), la décroissance de pression et
l'epsilon-régularité rendraient les \(v_k\) uniformément bornés sur un
cylindre plus petit, contredisant l'explosion.

La minoration Barker--Prange (10) ne donne pas cette explosion : elle donne
une quantité critique positive, compatible avec des suites uniformément
bornées. On ne peut donc pas déduire A.5 de (10). En revanche, si le but est
seulement \(U\not\equiv0\), (15) demande moins que A.5.

### 4.2 Normalisation ponctuelle : persister jusqu'au temps terminal

Dans la section 4 du même article, les auteurs choisissent des points de
maximum \(z_n=(x_n,t_n)\) et des facteurs
\(M_n=|v(z_n)|\to\infty\). Le zoom satisfait exactement

\[
 |v_n|\le1,\qquad |v_n(0,0)|=1.                            \tag{18}
\]

La proposition 4.1 donne une borne uniforme
\(C^{1/2}_{\rm par}\) sur chaque compact jusqu'à \(s=0\); le corollaire 4.2
donne la convergence uniforme locale et donc

\[
 |U(0,0)|=1.                                               \tag{19}
\]

Cette voie est plus forte que (15), mais utilise une normalisation
\(L^\infty\), une compacité de Hölder, une troncature contrôlée, une force
sous-critique qui disparaît et des estimations non locales de pression. Elle
ne se déduit pas d'une simple borne faible-\(L^3\).

### 4.3 Hiérarchie exacte

| mécanisme | entrée de non-trivialité | topologie | conclusion |
|---|---|---|---|
| Barker--Prange + intégration (présent cycle) | faible-\(L^3\) positive à **tout** temps tardif | forte \(L^3\) espace-temps supposée | \(U\not\equiv0\) sur un intervalle négatif |
| Albritton--Barker A.5 | explosion \(L^\infty\) sur tout cylindre | forte \(L^3\) vitesse + faible \(L^{3/2}\) pression | origine singulière dans la limite |
| Albritton--Barker 4.1--4.2 | \(|v_n(0,0)|=1\), \(|v_n|\le1\) | convergence uniforme locale jusqu'à \(0\) | \(|U(0,0)|=1\) et limite ancienne mild |

## 5. Passe contradictoire

### Test A — remplacer “tout temps” par “une suite”

Une minoration uniquement aux instants \(s_n\) a mesure temporelle nulle.
Elle ne donne aucune version de (13). Une couche temporelle de largeur
tendant vers zéro peut porter une norme de tranche positive tout en
convergeant fortement vers zéro dans \(L^3_{t,x}\). Le quantificateur exact
de Barker--Prange est donc indispensable.

**Résidu :** sans épaisseur temporelle uniforme, aucune masse espace-temps
certifiée.

### Test B — abaisser la convergence à \(L^q\), \(q<3\)

Des pics d'amplitude \(A_n\) et de volume spatial \(A_n^{-3}\) gardent une
masse cubique d'ordre un mais leur norme \(L^q\) tend vers zéro pour tout
\(q<3\). La convergence forte \(L^q_{\rm loc}\), \(q<3\), ne transmet donc
pas (13).

**Résidu :** l'exposant fort \(3\) est une vraie porte critique.

### Test C — confondre faible-\(L^3\) globale et masse locale

Une borne supérieure globale dans \(L^{3,\infty}\) ne donne aucune
minoration locale. La masse peut être répartie ou s'échapper. Ici la
minoration locale vient de la singularité Type I et du théorème 2; elle ne
vient pas de (4) seule.

**Résidu :** singularité et concentration Barker--Prange restent des
hypothèses/conclusions conditionnelles, non une conséquence de l'énergie
Clay.

### Test D — conclure une singularité terminale depuis (15)

Une solution ancienne lisse non nulle possède une masse espace-temps
positive. L'équation (15) ne distingue pas ce cas d'une limite singulière.
La conclusion A.5 ou la normalisation (19) ne peut pas être importée sans ses
hypothèses.

**Résidu :** non-trivialité ancienne, mais aucune persistance de blow-up.

### Test E — centre mobile

Des bosses de même masse dont les centres normalisés tendent vers l'infini
convergent vers zéro sur tout compact. Une sélection \(x(t)\) non confinée
ne répare donc pas la non-trivialité locale.

**Résidu :** utiliser le centre singulier fixe de Barker--Prange, ou prouver
explicitement une borne comme (16).

## 6. Veille différentielle 2025--2026

Les PDF primaires et leurs versions ont été contrôlés au 15 août 2026.

- Gregory Seregin,
  [`arXiv:2507.08733v2`](https://arxiv.org/abs/2507.08733v2),
  *A note on certain scenarios of Type II blowups of suitable weak solutions
  to the Navier--Stokes equations*, révisé le 3 janvier 2026 : les théorèmes
  ajoutent des fonctionnelles de scénario Type II et utilisent un zoom
  eulérien. Ils ne donnent pas (14) pour la renormalisation parabolique
  Type I.

- Gregory Seregin,
  [`arXiv:2606.29468v1`](https://arxiv.org/abs/2606.29468v1),
  *On potential Type II blowups for the Navier--Stokes equations*,
  28 juin 2026 : le théorème 3.1 obtient, sous les hypothèses intégrées
  (1.7), (3.1) et (3.3) de l'article, une limite ancienne **Euler** non nulle
  grâce à une minoration espace-temps. Ce résultat confirme la robustesse du
  principe “intégrer avant la limite”, mais dans un scaling et une équation
  différents; il ne ferme pas la porte Navier--Stokes (14).

- Tobias Barker,
  [`arXiv:2510.20757v3`](https://arxiv.org/abs/2510.20757v3),
  *Quantitative classification of potential Navier--Stokes singularities
  beyond the blow-up time*, révisé le 11 août 2026 : les théorèmes 1--3
  supposent des données approximativement axisymétriques et des bornes
  quantitatives spécifiques. Ils ne constituent pas un théorème générique
  de compacité ancienne faible-\(L^3\).

- Ben Pineau et Vlad Vicol,
  [`arXiv:2607.09619v2`](https://arxiv.org/abs/2607.09619v2),
  *On rotated backwards self-similar solutions of the incompressible 3D
  Navier--Stokes equations*, révisé en août 2026 : l'exclusion concerne des
  solutions auto-similaires ou discrètement auto-similaires tournées, sous
  borne Type I et régimes de rotation/scaling supplémentaires. Le critère à
  une tranche suppose une proximité auto-similaire; il ne transmet pas une
  concentration arbitraire à une limite ancienne.

- Runlong Yu,
  [`arXiv:2606.12756v1`](https://arxiv.org/abs/2606.12756v1),
  *Invisible Defect Cascades for Navier--Stokes Regularity*, 10 juin 2026 :
  la réduction est explicitement conditionnelle à des hypothèses
  d'extraction, d'observabilité et de contrôle de fenêtres mobiles. Elle ne
  fournit pas la forte compacité (14).

**Verdict de veille.** Aucun article primaire 2025--2026 contrôlé ne rend
inconditionnelle l'implication

\[
 L^\infty_tL^{3,\infty}_x\text{ Type I}
 \Longrightarrow
 \text{limite ancienne NS fortement compacte et non triviale}.             \tag{20}
\]

## 7. Sources nouvelles proposées

**Aucune.** Barker--Prange 2020 est déjà `NS-SRC-0146`,
Albritton--Barker 2020 `NS-SRC-0187` et Barker--Seregin--Šverák 2018
`NS-SRC-0188`. Les prépublications 2025--2026 mentionnées sont déjà couvertes
par la veille générale du dépôt. Ce cycle modifie l'implication logique
entre sources existantes; il ne justifie pas un identifiant supplémentaire.

## 8. Empreintes des PDF audités

Les empreintes portent sur les octets téléchargés et relus le 15 août 2026.

| PDF | octets | SHA256 |
|---|---:|---|
| `https://arxiv.org/pdf/1812.09115` | 505915 | `D1C0D26270F784697460DC5CE56DC5599CFEABCE40C0F3AAA35372296BC7D78D` |
| manuscrit accepté Warwick de Barker--Prange 2020 | 1164139 | `BFE409C7730E8F3419474982EB05BA7DC8128F01882B1CB1279BB39D87191CDD` |
| `https://arxiv.org/pdf/1811.00507` | 476336 | `FDD91E657B5CF503286B4E45CC084C12C8B202AAF24BCDAD67EDEA46EDFA4102` |
| `https://arxiv.org/pdf/2507.08733v2` | 329495 | `EACE90E2F799C8548BC2968DF4D6B7F51A8018CF8DFE39379F14A1C3ACCB8F94` |
| `https://arxiv.org/pdf/2606.29468v1` | 286905 | `3F895B24C995A2A664578B5E43EFE5CAE313E745FDCEEAAD8B3D6A00987436FD` |
| `https://arxiv.org/pdf/2510.20757v3` | 496127 | `E04702B4179F6C91DE9AD6E6D3C918F05B7FCE79EFD22174FF98371C4AD7AD90` |
| `https://arxiv.org/pdf/2607.09619v2` | 617825 | `379591AA3C1036C9140702EBE71AAAB309FE207439A57DB5CEFF893F15D0AE8E` |
| `https://arxiv.org/pdf/2606.12756v1` | 863017 | `26CB6469578CB8CDFAD93BA85928E688893F7EB8F4C030BCE783E0FAFD0E7EFF` |

## Conclusion opérationnelle

Le verrou de non-trivialité se sépare désormais proprement en deux portes :

\[
\boxed{
\begin{array}{c}
\text{Barker--Prange à tout temps}
\ +\ \text{forte }L^3_{\rm loc}
\ \Longrightarrow\ U\not\equiv0,\\[1mm]
\text{explosion }L^\infty\text{ ou normalisation ponctuelle}
\ \Longrightarrow\ \text{singularité/valeur terminale persistante.}
\end{array}}
\]

La première implication est suffisante pour alimenter un théorème de
rigidité excluant **toute** solution ancienne non nulle de la classe limite;
elle n'est pas suffisante pour un argument exigeant que la limite reste
singulière à \(s=0\). La prochaine vérification décisive doit donc porter sur
la suite réelle de zooms : satisfait-elle les bornes fortes de vitesse et de
pression d'Albritton--Barker A.2, ou la scission énergétique stable de
Barker--Seregin--Šverák, sur chaque bande \([-b,-a]\) ? Si oui, l'équation
(15) ferme la non-trivialité sans trace terminale. Sinon, le raccord demeure
conditionnel et doit être enregistré comme tel.
