# Cycle 0051 — queues spatiales, basses fréquences et saturation forward

**Date de coupure :** 15 août 2026

**Nature :** veille bibliographique primaire indépendante et test
contradictoire analytique

**Question auditée :** la seule borne critique
\(L^\infty_tL^{3,\infty}_x(\mathbb R^3)\), complétée sur chaque fenêtre
forward par une scission calorique à correcteur énergétique, contrôle-t-elle
uniformément les queues spatiales ou les basses fréquences lorsque la longueur
de la fenêtre croît ? Existe-t-il un théorème publié qui fournisse la
tightness correspondante pour une solution ancienne ?

On considère uniquement Navier--Stokes incompressible standard, non forcé,
de viscosité un, sur \(\mathbb R^3\) :

\[
 \partial_tu-\Delta u+u\cdot\nabla u+\nabla p=0,
 \qquad \nabla\cdot u=0.                                  \tag{1}
\]

La transformation critique est

\[
 u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),
 \qquad p_\lambda(x,t)=\lambda^2p(\lambda x,\lambda^2t). \tag{2}
\]

## Verdict

1. **Oui : une vraie solution Navier--Stokes publiée sature exactement la
   croissance \(h^{1/4}\) du correcteur.** Jia--Šverák construisent des
   solutions forward auto-similaires lisses pour \(t>0\), issues de données
   solénoïdales homogènes de degré \(-1\). Dans leur notation, la solution
   appartient à \(N(u_0)\) : c'est une solution de Leray locale qui satisfait
   explicitement l'inégalité d'énergie locale de Caffarelli--Kohn--Nirenberg,
   donc une solution faible adaptée, mais pas nécessairement une solution de
   Leray--Hopf d'énergie globale. Pour une donnée lisse sur la sphère, leur
   profil satisfait

   \[
     W:=U-e^\Delta u_0\in H^1(\mathbb R^3).               \tag{3}
   \]

   Dès que \(W\ne0\), le correcteur vérifie exactement

   \[
     \|u(t)-e^{t\Delta}u_0\|_2=t^{1/4}\|W\|_2.           \tag{4}
   \]

   Un champ explicite admissible est donné ci-dessous et force \(W\ne0\).

2. **(4) réfute une uniformité forward dépendant seulement de la norme
   faible-\(L^3\).** Il n'existe pas de fonction finie \(C(M)\) telle que

   \[
     \sup_{h>0}\|u(h)-e^{h\Delta}u_0\|_2\le C(M)          \tag{5}
   \]

   pour toutes les solutions forward de cette classe avec
   \(\|u_0\|_{3,\infty}\le M\). L'exposant supérieur BSS \(h^{1/4}\) est
   donc optimal en puissance sur cette famille.

3. **La perte est simultanément spatiale et fréquentielle.** Pour la famille
   translatée démarrant au temps \(s\), le correcteur au temps terminal fixé
   \(t_*\) vit à l'échelle spatiale \(\sqrt{t_*-s}\) et à la fréquence
   \((t_*-s)^{-1/2}\). Après normalisation de son énergie, toute la masse
   quitte chaque boule spatiale fixe et entre dans chaque voisinage fixe de la
   fréquence zéro lorsque \(s\to-\infty\).

4. **Cette famille n'est pas une solution ancienne unique.** Elle est une
   suite de solutions exactes définies sur les intervalles
   \((s,\infty)\), avec le même majorant critique. Elle réfute donc toute
   déduction *universelle de fenêtre finie* fondée seulement sur
   \(L^{3,\infty}\), mais ne réfute pas un éventuel théorème exploitant la
   compatibilité dynamique supplémentaire d'une seule trajectoire ancienne.

5. **Le faible-\(L^3\), les espaces critiques de Morrey et les espaces de
   Besov à indice de sommation infini ne donnent pas la tightness.** Ils
   autorisent une contribution de taille critique sur chaque couronne ou
   chaque bloc dyadique. Les espaces de Herz rendent ce défaut visible : une
   norme \(\ell^\infty\) des couronnes contrôle la pire couronne, sans sommer
   les queues.

6. **Les résultats spatiaux les plus proches sont forward et conditionnels.**
   Bradshaw--Phelps (publié en 2023) donnent des taux algébriques pour les
   données DSS localement \(L^q\), \(q>3\), mais indiquent que l'endpoint
   \(q=3\), équivalent à faible-\(L^3\) dans la classe DSS, ne possède pas de
   taux algébrique général. Leur prépublication v1 de 2024 obtient à
   l'endpoint une décomposition « terme critique arbitrairement petit + terme
   en \((|x|+\sqrt t)^{-1}\) + reste », pas une queue \(L^2\) uniforme.

7. **Aucun théorème de tightness ancienne générale n'a été localisé.** KNSS,
   Taniuchi, Albritton--Barker et les Liouville axisymétriques utilisent
   mildness, petitesse, borne \(L^3\) forte, blow-down terminal, décroissance
   spatiale uniforme ou symétrie. Dans ces résultats, la condition qui
   empêche l'échappement est une hypothèse ou une conséquence d'un scénario
   plus fort; elle n'est pas dérivée de la seule borne
   \(L^\infty_tL^{3,\infty}_x\).

8. **Conclusion négative exacte :** le corpus contrôlé ne fournit pas

   \[
   \boxed{
   \sup_{t<0}\|v(t)\|_{3,\infty}<\infty
   \quad\Longrightarrow\quad
   \begin{cases}
    \sup_{s<t_*}\|w_s(t_*)\|_2<\infty,\\
    \displaystyle\lim_{R\to\infty}
       \sup_{s<t_*-1}\int_{|x|>R}|w_s(x,t_*)|^2dx=0,
   \end{cases}}                                          \tag{6}
   \]

   même en ajoutant seulement l'existence séparée des correcteurs sur chaque
   fenêtre finie. Cela signifie **aucun théorème trouvé**, et non
   impossibilité pour une trajectoire ancienne cohérente.

## 1. Saturation exacte par une solution forward auto-similaire

### 1.1 Théorème d'existence publié

Hao Jia et Vladimír Šverák,
[*Local-in-space estimates near initial time for weak solutions of the
Navier--Stokes equations and forward self-similar
solutions*](https://doi.org/10.1007/s00222-013-0468-x), *Inventiones
Mathematicae* **196** (2014), 233--265;
[`arXiv:1204.0529v1`](https://arxiv.org/abs/1204.0529v1).

Le théorème 1.1 traite une donnée \(u_0\) solénoïdale, homogène de degré
\(-1\) et localement höldérienne sur \(\mathbb R^3\setminus\{0\}\). Il
construit une solution globale scale-invariante

\[
 u(x,t)=t^{-1/2}U(x/\sqrt t),                             \tag{7}
\]

lisse sur \(\mathbb R^3\times(0,\infty)\). Le théorème 5.1 réalise
explicitement le cas lisse avec une solution qui appartient à la classe
\(N(u_0)\) de leur définition 3.1. Cette classe impose des bornes d'énergie
locales uniformes, la convergence locale \(L^2\) vers \(u_0\), l'équation au
sens des distributions et l'inégalité d'énergie locale CKN. La solution est
donc **locale de Leray et faible adaptée**; comme la donnée homogène \(-1\)
n'est en général pas dans \(L^2(\mathbb R^3)\), ce n'est pas une solution de
Leray--Hopf d'énergie globale. Il n'y a aucune force extérieure et aucune
petitesse de la donnée n'est demandée. Elle n'est définie que pour \(t>0\) :
elle est forward globale, non ancienne.

Pour une donnée lisse sur la sphère, le théorème 4.1 et la construction de la
section 5 donnent, pour tout multi-indice \(\alpha\),

\[
 |\partial^\alpha(U-e^\Delta u_0)(x)|
 \le {C_{\alpha,u_0}\over(1+|x|)^{3+|\alpha|}}.           \tag{8}
\]

Le profil et le flot calorique sont lisses au temps un. Par conséquent (8)
implique bien

\[
 W=U-e^\Delta u_0\in H^1(\mathbb R^3).                   \tag{9}
\]

Pour une donnée seulement \(C^\alpha\), l'estimation publiée est plus faible,
de l'ordre \((1+|x|)^{-1-\alpha}\). L'appartenance \(L^2\) du correcteur
n'est alors immédiate que si \(\alpha>1/2\). Le test de saturation utilise la
sous-classe lisse et n'extrapole pas ce point à tout l'endpoint.

### 1.2 Un coefficient strictement non nul

Prenons, pour \(\varepsilon\ne0\),

\[
 u_0(x)=\varepsilon {(-x_2,x_1,0)\over |x|^2}.           \tag{10}
\]

Ce champ est homogène de degré \(-1\), lisse hors de l'origine,
solénoïdal au sens des distributions et appartient à
\(L^{3,\infty}(\mathbb R^3)\). Son accélération convective, hors de
l'origine, vaut

\[
 (u_0\cdot\nabla)u_0
 =-\varepsilon^2{(x_1,x_2,0)\over |x|^4},                \tag{11}
\]

et

\[
 \nabla\times((u_0\cdot\nabla)u_0)
 ={4\varepsilon^2\over |x|^6}(-x_2x_3,x_1x_3,0),         \tag{12}
\]

qui n'est pas identiquement nul.

Si \(W=0\), l'auto-similarité donnerait
\(u(t)=e^{t\Delta}u_0\) pour tout \(t>0\). Le flot calorique serait alors
une solution de (1), donc son accélération convective serait un gradient.
En laissant \(t\downarrow0\) sur tout compact évitant l'origine, on
obtiendrait que (11) est un gradient, en contradiction avec (12). Ainsi

\[
 \boxed{\|W\|_2>0.}                                      \tag{13}
\]

Cette non-annulation est une dérivation élémentaire du laboratoire appuyée
sur le théorème d'existence publié; elle n'est pas attribuée à Jia--Šverák.
Elle peut aussi être contrôlée dans le régime de petite donnée par les
asymptotiques explicites de Brandolese décrites plus bas.

### 1.3 Loi exacte du correcteur

L'homogénéité de \(u_0\) donne

\[
 e^{t\Delta}u_0(x)=t^{-1/2}(e^\Delta u_0)(x/\sqrt t).
                                                               \tag{14}
\]

En soustrayant (14) à (7),

\[
 w(x,t)=u(x,t)-e^{t\Delta}u_0(x)
       =t^{-1/2}W(x/\sqrt t).                              \tag{15}
\]

Un changement de variable donne les identités, sans constante cachée,

\[
 \|w(t)\|_2=t^{1/4}\|W\|_2,\qquad
 \|\nabla w(t)\|_2^2=t^{-1/2}\|\nabla W\|_2^2,           \tag{16}
\]

et

\[
 \int_0^h\|\nabla w(t)\|_2^2dt
 =2h^{1/2}\|\nabla W\|_2^2.                              \tag{17}
\]

La solution est donc une solution exacte de (1), non un profil fonctionnel
arbitraire, et le correcteur appartient à la classe énergétique sur toute
fenêtre finie. La norme \(L^{3,\infty}\) de \(u(t)\) est indépendante de
\(t\). Les puissances \(h^{1/4}\) et \(h^{1/2}\) ne peuvent être supprimées
d'une estimation générale fondée sur cette seule norme critique.

## 2. Échappement spatial et condensation aux basses fréquences

Translatons la solution précédente. Pour chaque \(s<t_*\), posons

\[
 u^{(s)}(x,t)=(t-s)^{-1/2}
 U\left({x\over\sqrt{t-s}}\right),\qquad t>s.             \tag{18}
\]

Il s'agit d'une solution exacte de (1), de trace \(u_0\) au temps \(s\), et

\[
 w_s(x,t_*)=(t_*-s)^{-1/2}
 W\left({x\over\sqrt{t_*-s}}\right).                     \tag{19}
\]

Écrivons \(h=t_*-s\). La mesure d'énergie normalisée

\[
 \mu_h(A)={h^{-1/2}\over\|W\|_2^2}
           \int_A|w_s(x,t_*)|^2dx                       \tag{20}
\]

est une probabilité et satisfait

\[
 \mu_h(B_R)={1\over\|W\|_2^2}
 \int_{|y|<R/\sqrt h}|W(y)|^2dy\longrightarrow0          \tag{21}
\]

pour tout \(R<\infty\). La masse spatiale s'échappe donc à l'échelle
\(\sqrt h\).

Avec la convention de Fourier usuelle,

\[
 \widehat{w_s}(\xi,t_*)=h\,\widehat W(\sqrt h\,\xi).      \tag{22}
\]

Pour tout \(\delta>0\), la fraction d'énergie située dans
\(\{|\xi|>\delta\}\) tend vers zéro :

\[
 {\int_{|\xi|>\delta}|\widehat{w_s}(\xi,t_*)|^2d\xi
  \over \|w_s(t_*)\|_2^2}
 ={\int_{|\eta|>\delta\sqrt h}|\widehat W(\eta)|^2d\eta
  \over\|W\|_2^2}
 \longrightarrow0.                                      \tag{23}
\]

Le même défaut se lit donc comme une queue spatiale dilatée ou comme une
condensation vers la fréquence zéro. Une compacité seulement locale ne voit
pas cette énergie.

**Portée précise.** Les \(u^{(s)}\) de (18) ne sont pas les restrictions d'une
même solution ancienne. (21)--(23) démontrent que ni la PDE exacte, ni la
borne faible-\(L^3\), ni l'énergie relative sur chaque fenêtre n'impliquent
une uniformité en longueur de fenêtre dans une classe forward générale. Une
preuve ancienne doit donc utiliser une propriété de cohérence supplémentaire
qui est absente de ce contre-test.

## 3. Asymptotiques fines des profils auto-similaires

Lorenzo Brandolese,
[*Fine Properties of Self-Similar Solutions of the Navier--Stokes
Equations*](https://doi.org/10.1007/s00205-008-0149-x), *Archive for
Rational Mechanics and Analysis* **192** (2009), 375--401;
[`arXiv:0803.0210v1`](https://arxiv.org/abs/0803.0210v1).

L'article traite les solutions forward auto-similaires de petite donnée
homogène de degré \(-1\), lisse sur la sphère, en dimension \(d\ge2\). En
dimension trois, son théorème principal donne l'expansion

\[
 U(x)=u_0(x)+\Delta u_0(x)
 -\mathbb P\nabla\cdot(u_0\otimes u_0)(x)
 -{\mathcal Q(x):B\over |x|^7}
 +O(|x|^{-5}\log|x|),                                    \tag{24}
\]

où \(\mathcal Q\) est polynomial homogène de degré trois et \(B\) une
matrice dépendant de la donnée. Le datum \(u_0\) peut être remplacé dans
l'expansion par son filtrage \(e^\Delta u_0\). En particulier,

\[
 U-e^\Delta u_0=O(|x|^{-3}),                              \tag{25}
\]

et l'article indique que ce niveau est génériquement optimal. (24) montre
que la queue \(|x|^{-1}\) de la vitesse est principalement calorique, tandis
que le correcteur non linéaire est intégrable au carré mais non nul en
général. C'est exactement la configuration qui produit (16).

Ce résultat est analytique et publié. Il est limité à la petite donnée pour
son expansion explicite; Jia--Šverák donnent l'existence grande donnée et la
décroissance suffisante à (9).

## 4. Grande donnée faible-\(L^3\), Morrey et endpoint spatial

### 4.1 Existence et borne \(t^{1/4}\) publiée

Zachary Bradshaw et Tai-Peng Tsai,
[*Forward Discretely Self-Similar Solutions of the Navier--Stokes Equations
II*](https://doi.org/10.1007/s00023-016-0519-0), *Annales Henri Poincaré*
**18** (2017), 1095--1119;
[`arXiv:1510.07504v1`](https://arxiv.org/abs/1510.07504v1).

Le théorème 1.2 construit, pour toute donnée solénoïdale \(\lambda\)-DSS
arbitrairement grande dans \(L^{3,\infty}\), une solution locale de Leray
globale forward, \(\lambda\)-DSS, telle que

\[
 \|v(t)-e^{t\Delta}v_0\|_2\le C(v_0)t^{1/4}.             \tag{26}
\]

Le même article donne une construction SS pour toute donnée homogène
\(-1\) faible-\(L^3\). (26) est un majorant; le calcul du §1 fournit une
sous-classe publiée où sa puissance est atteinte avec égalité.

L'article observe aussi que le résultat subsiste sous une petite condition
locale de Morrey sur une couronne fondamentale. Une donnée DSS peut être dans
le Morrey critique \(M^{2,1}\) tout en échappant à faible-\(L^3\); leur
exemple (1.14) place une singularité remise à l'échelle sur chaque couronne.
Les auteurs précisent que leur approche échoue alors faute de contrôle de la
décroissance spatiale de \(e^{t\Delta}v_0\). Le contrôle de Morrey critique ne
doit donc pas être confondu avec une queue globale sommable.

### 4.2 Décroissance publiée pour \(q>3\)

Zachary Bradshaw et Patrick Phelps,
[*Spatial Decay of Discretely Self-Similar Solutions to the Navier--Stokes
Equations*](https://doi.org/10.2140/paa.2023.5.377), *Pure and Applied
Analysis* **5** (2023), 377--407;
[`arXiv:2202.08352v1`](https://arxiv.org/abs/2202.08352v1).

Pour une donnée DSS appartenant localement à \(L^q\) hors de l'origine,
\(q>3\), et une solution locale d'énergie DSS, le théorème 1.1 contrôle, dans
la région régulière \(|x|\ge R_0\sqrt t\),

\[
 |u-e^{t\Delta}u_0|(x,t)
 \lesssim {1\over
    (\sqrt t)^{6/q-1}(|x|+\sqrt t)^{2-6/q}}.              \tag{27}
\]

Les théorèmes suivants améliorent la décroissance après soustraction
d'itérés de Picard; pour une donnée \(C^{1,\alpha}\), le correcteur a la
décroissance optimale

\[
 |u-e^{t\Delta}u_0|(x,t)
 \lesssim {t\over(|x|+\sqrt t)^3}.                        \tag{28}
\]

La source distingue explicitement l'endpoint : pour une donnée seulement
\(L^{3,\infty}\cap DSS\), il n'existe pas de taux algébrique général pour le
flot calorique. Les résultats \(q>3\) approchent mais n'atteignent pas ce cas.
De plus, les bornes sont attachées au cône spatial naturel
\(|x|\sim\sqrt t\); elles ne donnent pas (6) lorsque la longueur de fenêtre
tend vers l'infini.

### 4.3 Endpoint 2024 : progrès réel, mais prépublication

Zachary Bradshaw et Patrick Phelps,
[*Asymptotic Properties of Discretely Self-Similar Navier--Stokes Solutions
with Rough Data*](https://arxiv.org/abs/2409.13586v1),
arXiv:2409.13586v1, 20 septembre 2024, 30 pages.

Au 15 août 2026, l'API primaire arXiv retourne toujours la version v1 et ne
donne ni référence de revue ni DOI d'article publié. Le statut exact est donc
**prépublication v1**.

Le théorème 1.4 traite précisément
\(u_0\in L^{3,\infty}\cap DSS\). Pour tout \(\varepsilon>0\), il décompose
la solution, dans la région régulière, en trois champs : un terme arbitrairement
petit dans une classe critique, un terme de taille
\((|x|+\sqrt t)^{-1}\), et un reste ayant un gain positif d'échelle. Une
version Besov critique \(\dot B^{-1+3/p}_{p,\infty}\), \(p>3\), est aussi
démontrée.

Ce résultat est une vraie localisation asymptotique à l'endpoint, mais il ne
donne pas :

- la petitesse de la solution entière dans \(L^{3,\infty}\) ;
- une somme des queues sur toutes les couronnes ;
- une borne \(L^2\) du correcteur uniforme en longueur de fenêtre ;
- une tightness ancienne ;
- un théorème de Liouville.

La partie arbitrairement petite peut rester répartie sur une infinité
d'échelles. « Petit dans une norme critique » n'est donc pas « compact dans
\(L^2\) ».

## 5. Lecture par Herz, Besov et Morrey

### 5.1 Herz : le défaut est l'indice \(\ell^\infty\)

Yohei Tsutsui,
[*The Navier--Stokes Equations and Weak Herz
Spaces*](https://doi.org/10.57262/ade/1355703112), *Advances in
Differential Equations* **16** (2011), 1049--1085.

Tsutsui développe le problème de Cauchy mild dans les espaces homogènes de
Herz faible \(W\dot K^\alpha_{p,q}\), y compris existence locale, petite
donnée globale, critères de blow-up et plongements vers des espaces de Besov
ou \(bmo^{-1}\). Sur les couronnes
\(A_k=\{2^{k-1}\le|x|<2^k\}\), la composante spatiale de la norme est de la
forme

\[
 \left\|\big(2^{k\alpha}
       \|f\|_{L^{p,\infty}(A_k)}\big)_{k\in\mathbb Z}
 \right\|_{\ell^q}.                                      \tag{29}
\]

Au cas critique avec \(q=\infty\), une donnée homogène \(-1\) a la même
taille normalisée sur toutes les couronnes. (29) est finie mais aucune queue
\(\ell^q\) ne tend à zéro. Un indice fini peut imposer une sommabilité
annulaire, mais il exclut alors les profils exactement homogènes non nuls sur
toutes les échelles.

Lucas C. F. Ferreira et Jhean E. Pérez-López,
[*Besov-Weak-Herz Spaces and Global Solutions for Navier--Stokes
Equations*](https://doi.org/10.2140/pjm.2018.296.57), *Pacific Journal of
Mathematics* **296** (2018), 57--77;
[`arXiv:1704.07001v1`](https://arxiv.org/abs/1704.07001v1).

Le théorème 1.1 prouve la bonne position globale mild pour petite donnée dans
des espaces critiques de Besov--weak-Herz. Les auteurs notent explicitement
que \(|x|^{-1}\) appartient à certaines de leurs classes à indices de
sommation infinis et que la solution est auto-similaire si la donnée l'est.
Leur critère d'asymptotique compare deux solutions lorsque la différence de
leurs **flots calorifiques** tend déjà vers zéro dans la norme critique. Il ne
dérive pas cette disparition à partir d'une simple borne.

### 5.2 Besov : contrôle de chaque échelle, pas ancrage infrarouge

Zachary Bradshaw et Tai-Peng Tsai,
[*Discretely Self-Similar Solutions to the Navier--Stokes Equations with
Besov Space Data*](https://doi.org/10.1007/s00205-017-1213-1), *Archive for
Rational Mechanics and Analysis* **229** (2018), 53--77;
[`arXiv:1703.03480v1`](https://arxiv.org/abs/1703.03480v1).

Les auteurs construisent des solutions SS et DSS pour des données
potentiellement grandes dans
\(\dot B^{-1+3/p}_{p,\infty}\), \(3<p<6\), classe strictement plus large que
\(L^{3,\infty}\). La construction décompose la donnée en une partie
faible-\(L^3\) et une petite partie traitée par Koch--Tataru, puis résout une
équation de Leray perturbée.

L'indice final \(\infty\) de Besov prend un supremum sur les blocs
fréquentiels. Il autorise une taille critique identique à une infinité de
basses fréquences. Le théorème produit des solutions forward, pas une
condition de vanishing infrarouge et pas de compacité ancienne.

### 5.3 Morrey : localisation uniforme sans queue globale

Le Morrey critique contrôle des intégrales sur chaque boule après
normalisation par son rayon. Il est adapté aux solutions d'énergie locale et
aux données homogènes, mais il est invariant par translation/dilatation et ne
somme pas les boules lointaines. L'exemple DSS de Bradshaw--Tsai dans
\(M^{p,3-p}\setminus L^{3,\infty}\) montre concrètement que des paquets
critiques peuvent se répéter de couronne en couronne.

Ainsi les trois langages donnent le même diagnostic :

| Langage | Contrôle obtenu | Information absente |
|---|---|---|
| faible-\(L^3\) | fonction de distribution globale critique | continuité absolue de la norme et queue uniforme |
| Herz, indice \(\infty\) | pire couronne dyadique | sommabilité des couronnes |
| Besov, indice \(\infty\) | pire bloc de fréquence | vanishing quand \(j\to-\infty\) |
| Morrey critique | énergie normalisée dans toute boule | somme/tightness des boules lointaines |

Une condition utile pour le verrou ancien doit remplacer au moins un de ces
suprema par un mécanisme de vanishing, une sommabilité, une précompacité
modulo symétries ou un moment quantitatif.

## 6. Solutions anciennes et théorèmes de Liouville

Les sources anciennes déjà cataloguées restent les références structurantes :

- KNSS, `NS-SRC-0015`, extrait des limites anciennes mild à partir de suites
  **uniformément bornées ponctuellement** et obtient une convergence locale
  uniforme. Ce mécanisme est plus fort que faible-\(L^3\) et n'est pas une
  tightness \(L^2\) globale ;
- Albritton--Barker, `NS-SRC-0189`, annule une solution mild ancienne sous une
  borne \(L^3\) forte le long d'une suite reculée; sa variante faible-\(L^3\)
  ajoute une condition terminale de blow-down dans
  \(\dot B^{-1}_{\infty,\infty}\) ;
- Taniuchi, `NS-SRC-0190`, suppose déjà la mildness et la continuité forte
  dans \(\widetilde L^{3,\infty}\), puis ajoute petitesse, décroissance ou
  approximation au passé. Son espace tilde ne fournit pas à lui seul (6).

Une source axisymétrique rend particulièrement visible le rôle d'une queue
ajoutée : Zhen Lei, Qi S. Zhang et Na Zhao,
[*Improved Liouville Theorems for Axially Symmetric Navier--Stokes
Equations*](https://arxiv.org/abs/1701.00868v1), version anglaise de
*Scientia Sinica Mathematica* **47** (2017), 1183--1198,
[DOI 10.1360/N012016-00149](https://doi.org/10.1360/N012016-00149).
Les théorèmes 1.1--1.3 imposent mildness ancienne et, selon le cas, décroissance
uniforme de la vorticité à l'infini, sublinéarité de la vitesse, ou
\(rv_\theta\in L^\infty_tL^p_x\) avec \(p<\infty\). La décroissance spatiale
est une hypothèse de Liouville dans une classe symétrique, pas une conséquence
de faible-\(L^3\) général.

**Résultat de la recherche ciblée :** aucun article primaire contrôlé ne
démontre que toute solution ancienne adaptée ou mild uniformément bornée dans
\(L^{3,\infty}\) possède des correcteurs satisfaisant (6). Aucun article ne
démontre non plus l'impossibilité d'un tel renforcement pour une trajectoire
ancienne cohérente.

## 7. Veille différentielle récente

La prépublication Bradshaw--Phelps 2024 ci-dessus est la source récente la
plus directement pertinente et n'était pas cataloguée. Les développements
2025--2026 déjà catalogués ne changent pas le verdict :

- Bradshaw--Hudson, `NS-SRC-0193`, étend la classe faible scindée à
  \(L^{p,\infty}\), \(2<p<3\), sur fenêtres forward et conserve une puissance
  positive du temps écoulé ;
- Binz--Coiculescu, `NS-SRC-0047`, arXiv:2607.12159v1, traite des profils
  homothétiques forward dans des espaces de Morrey avec régularité angulaire
  et donne des exclusions conditionnelles, pas une tightness ancienne ;
- les prépublications Type II `NS-SRC-0048` et `NS-SRC-0034` produisent des
  objets limites sous d'autres remises à l'échelle, souvent eulériennes, et
  ne contrôlent pas les correcteurs calorifiques faible-\(L^3\).

Aucune annonce primaire 2025--2026 localisée ne transforme les asymptotiques
forward du présent audit en un Liouville général faible-\(L^3\).

## 8. Entrées de catalogue recommandées

Les neuf sources suivantes sont absentes de `sources.json` à la date du
contrôle. Les identifiants sont proposés dans l'ordre libre courant; ils
doivent être réalloués si un autre cycle occupe entre-temps la plage.

| ID proposé | Source | Statut exact | Motif d'ajout |
|---|---|---|---|
| `NS-SRC-0194` | Jia--Šverák, Invent. Math. 196 (2014), 233--265, DOI `10.1007/s00222-013-0468-x`, arXiv `1204.0529v1` | publié | existence grande donnée SS et décroissance \(U-e^\Delta u_0\), source du saturateur PDE |
| `NS-SRC-0195` | Bradshaw--Tsai, Ann. Henri Poincaré 18 (2017), 1095--1119, DOI `10.1007/s00023-016-0519-0`, arXiv `1510.07504v1` | publié | grande donnée DSS faible-\(L^3\), borne explicite \(t^{1/4}\), extension Morrey |
| `NS-SRC-0196` | Bradshaw--Phelps, Pure Appl. Anal. 5 (2023), 377--407, DOI `10.2140/paa.2023.5.377`, arXiv `2202.08352v1` | publié | décroissance spatiale du correcteur et rupture de l'endpoint \(q=3\) |
| `NS-SRC-0197` | Bradshaw--Phelps, arXiv `2409.13586v1` | prépublication v1, non publiée repérée | décomposition asymptotique endpoint faible-\(L^3\) et Besov |
| `NS-SRC-0198` | Brandolese, ARMA 192 (2009), 375--401, DOI `10.1007/s00205-008-0149-x`, arXiv `0803.0210v1` | publié | expansion explicite et optimalité générique de la queue non linéaire |
| `NS-SRC-0199` | Bradshaw--Tsai, ARMA 229 (2018), 53--77, DOI `10.1007/s00205-017-1213-1`, arXiv `1703.03480v1` | publié | solutions SS/DSS pour données Besov critiques grandes |
| `NS-SRC-0200` | Ferreira--Pérez-López, Pacific J. Math. 296 (2018), 57--77, DOI `10.2140/pjm.2018.296.57`, arXiv `1704.07001v1` | publié | Besov--weak-Herz, auto-similarité et critère asymptotique calorique |
| `NS-SRC-0201` | Tsutsui, Adv. Differential Equations 16 (2011), 1049--1085, DOI `10.57262/ade/1355703112` | publié | formulation annulaire Herz des queues et théorie mild correspondante |
| `NS-SRC-0202` | Lei--Zhang--Zhao, Sci. Sin. Math. 47 (2017), 1183--1198, DOI `10.1360/N012016-00149`, arXiv `1701.00868v1` | publié, arXiv = traduction anglaise | Liouville ancien sous décroissance spatiale/symétrie explicitement ajoutées |

Les cinq premières entrées sont prioritaires pour le verrou actif. Les quatre
suivantes complètent le dictionnaire fonctionnel et le contraste Liouville.
Barraza (1996) n'est pas proposé dans ce lot : sa petite donnée auto-similaire
faible-\(L^3\) est historiquement pertinente, mais les maillons utilisés ici
sont déjà couverts plus précisément par Yamazaki (`NS-SRC-0118`),
Brandolese et les constructions grande donnée ci-dessus.

## 9. Empreintes des textes primaires contrôlés

| PDF primaire téléchargé | SHA-256 |
|---|---|
| `0803.0210.pdf` | `92E786E8E16FEB64FC711ACC82EC5A33A559BE27994A80347465FF1D88D32356` |
| `1204.0529.pdf` | `1E8685FBE09C669854357278010F345FA5C98845C5888BA6720936A0B3F1591F` |
| `1510.07504.pdf` | `89712F040EE949A15B525E79D2957ED3A36A8FF6E3D106FEA352188E099846E7` |
| `1703.03480.pdf` | `3C7D4E5D63C75434DB17B067DC543D241738C4117EB18F00ED3BCAFA5F101E40` |
| `1704.07001.pdf` | `2F8A5BF53E0A1D787828DDFD2354D1243BE42706A8F8C37A7C4E16255E97DAA5` |
| `2202.08352.pdf` | `506B5A7D6E154FA85FD5C2A75518AD4F3258BAC754C911A5699189AC409BB47A` |
| `2409.13586.pdf` | `549940689A87DE35237AD6AF95900BCDAE1D3C202B9C45F9FB88F82D29F5D2A6` |

Les métadonnées de publication ont été croisées avec les DOI/publishers;
les versions arXiv ont été contrôlées par l'API primaire. Les PDF servent à
vérifier les énoncés; aucune preuve complète n'a été reproduite dans ce cycle.

## 10. Décision scientifique

**État : RÉVISER le verrou, puis CONTINUER.** La recherche d'une estimation
uniforme des correcteurs à partir de la seule norme faible-\(L^3\) doit être
abandonnée : (16) la réfute dans la classe forward exacte et montre que la
puissance BSS est aiguë.

Le prochain lemme utile doit inclure une hypothèse qui exclut explicitement
la dilation (19). Deux formulations falsifiables restent admissibles :

1. une tightness infrarouge uniforme, par exemple

   \[
   \lim_{\delta\downarrow0}\sup_{s<t_*-1}
     \int_{|\xi|<\delta}|\widehat{w_s}(\xi,t_*)|^2d\xi=0,
                                                               \tag{30}
   \]

   complétée par une borne \(L^2\) uniforme ;

2. une sommabilité annulaire ou fréquentielle critique renforçant l'indice
   \(\infty\) de Herz/Besov, stable par le cocycle et assez forte pour donner
   Rellich global.

Le test adverse obligatoire est (18)--(23). Toute hypothèse prétendument
nouvelle qui l'accepte encore ne peut pas fournir la tightness recherchée par
un simple argument de compacité. Si l'hypothèse l'exclut, il faudra ensuite
prouver qu'elle est héritée d'un scénario de blow-up Clay; l'imposer
arbitrairement ne fermerait pas le graphe.
