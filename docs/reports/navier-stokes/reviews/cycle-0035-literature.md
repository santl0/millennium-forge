# Cycle 0035 — revue primaire : bande de transition pure-swirl et analogues de halo

Date de coupure : **2026-08-14**
Périmètre : localisation BV/coaire/isopérimétrie, troncations de
superniveaux, concentration-compacité, recouvrements good-\(\lambda\), et
localisation dynamique près d'une singularité Navier–Stokes.
Statut : revue bibliographique indépendante; aucun catalogue ni claim JSON
n'est modifié par ce rapport.

## Verdict

La sélection littérale du cycle n'a pas été trouvée comme théorème publié.
Elle est néanmoins **impliquée par une dérivation courte dont les briques
analytiques sont publiées**, sous les hypothèses très spéciales et figées de
la famille finie pure-swirl à supports complets disjoints.

Le point logique principal est une correction de vocabulaire :

> \(H\) n'est pas un halo contenant le cœur
> \(E=\{\pm F_j>\lambda/2\}\). C'est la bande de transition disjointe
> \(\{\lambda/4<\pm F_j<\lambda/2\}\), qui exclut le cœur.

Son volume n'a donc pas à être construit ni comparé géométriquement à celui
du cœur. Il est directement contrôlé par
\(H\subset\{|U|>\lambda/6\}\). Les théorèmes d'isopérimétrie relative, de
concentration-compacité, de Calderón–Zygmund/good-\(\lambda\) et de
localisation dynamique Navier–Stokes ne sont que des **analogues**; aucun
d'eux n'est requis pour fermer le lemme actif.

Le statut recommandé est par conséquent :

- briques : **PUBLISHED / SOURCE_VERIFIED**;
- assemblage et constante suivie ci-dessous : **AI_DERIVATION**, à faire
  relire/formaliser, jamais PAPER_PROOF par attribution automatique;
- transfert au problème Clay : **aucun transfert direct**, faute d'une
  réduction d'une solution générale à une famille finie pure-swirl disjointe.

## 1. Énoncé figé et échelle

On considère une famille finie

\[
U_j=\frac{R_j}{r}F_j(r,z)e_\theta,
\qquad F_j\in C_c^\infty,
\qquad
\operatorname{supp}F_j\subset\{R_j/2<r<3R_j/2\},
\]

dont les supports tridimensionnels complets sont deux à deux disjoints. On
pose

\[
U=\sum_jU_j,\qquad W=\nabla\times U,
\qquad K_u=K_3(U)>0,\qquad K_w=K_{3/2}(W)<\infty,
\]

avec la convention de quasi-norme

\[
K_p(f)=\sup_{\alpha>0}\alpha
\left|\{|f|>\alpha\}\right|^{1/p}.
\]

Sous l'échelle stationnaire induite par Navier–Stokes,

\[
U_\rho(x)=\rho U(\rho x),\qquad
W_\rho(x)=\rho^2W(\rho x),
\]

les deux quantités \(K_3(U)\) et \(K_{3/2}(W)\) sont invariantes. Les
conclusions candidates

\[
\max_jK_3(U_j)\gtrsim \frac{K_u^2}{K_w},
\qquad
\max_j\frac{K_3(U_j)}{K_{3/2}(W_j)}
\gtrsim\left(\frac{K_u}{K_w}\right)^2
\]

ont donc la bonne loi d'échelle.

Ce cadre est statique, incompressible, lisse, sans pression et sans
frontière. Chaque champ peut servir de donnée initiale lisse, mais aucune
dynamique Navier–Stokes n'intervient dans le lemme.

## 2. Audit ligne par ligne du lemme actif

### 2.1 Comparaison annulaire et superniveaux

Sur le support de \(F_j\),

\[
\frac23<\frac{R_j}{r}<2.
\]

Pour \(D=\{|U|>\lambda\}\), les supports disjoints donnent donc

\[
D\subset
\bigcup_{j,\sigma\in\{+,-\}}\{\sigma F_j>\lambda/2\}
\subset\{|U|>\lambda/3\}.
\]

En posant

\[
E_{j,\sigma}=\{\sigma F_j>\lambda/2\},\qquad
V_{j,\sigma}=|E_{j,\sigma}|,
\]

et

\[
H_{j,\sigma}=\{\lambda/4<\sigma F_j<\lambda/2\},
\qquad H=\bigcup_{j,\sigma}H_{j,\sigma},
\]

on a directement

\[
H\subset\{|U|>\lambda/6\},
\qquad
|H|\le \left(\frac{6K_u}{\lambda}\right)^3.
\]

Cette étape est algébrique. Elle n'utilise ni recouvrement, ni halo
\(E\subset H\), ni borne axiale, ni volume de cellule, ni plateau.

### 2.2 Curl exact du pure-swirl

Pour un champ axisymétrique sans composantes radiale et axiale,

\[
(W_j)_r=-\frac{R_j}{r}\partial_zF_j,
\qquad
(W_j)_z=\frac{R_j}{r}\partial_rF_j,
\qquad (W_j)_\theta=0.
\]

Ainsi

\[
|W_j|=\frac{R_j}{r}|\nabla_{r,z}F_j|
\ge \frac23|\nabla F_j|.
\]

Il n'y a pas ici de terme \(F_j/r\) caché : le choix
\(U_{j,\theta}=R_jF_j/r\) le fait disparaître de
\(r^{-1}\partial_r(rU_{j,\theta})\). L'exclusion de l'axe par
\(r>R_j/2\) évite toute singularité de coordonnées.

### 2.3 Troncation, coaire et isopérimétrie globale

Pour chaque signe, introduire la troncation lipschitzienne

\[
G_{j,\sigma}
=\min\big((\sigma F_j-\lambda/4)_+,\lambda/4\big).
\]

La règle de chaîne BV/Sobolev donne presque partout

\[
|\nabla G_{j,\sigma}|
=\mathbf 1_{H_{j,\sigma}}|\nabla F_j|.
\]

La formule de coaire de Fleming–Rishel, déjà cataloguée sous
**NS-SRC-0132**, donne

\[
\int_{H_{j,\sigma}}|\nabla F_j|,dx
=\int_{\lambda/4}^{\lambda/2}
P(\{\sigma F_j>t\})\,dt.
\]

Pour tout \(t\in(\lambda/4,\lambda/2)\), le superniveau
\(\{\sigma F_j>t\}\) contient \(E_{j,\sigma}\). L'isopérimétrie
euclidienne globale en dimension trois,

\[
P(A)\ge c_{\rm iso}|A|^{2/3},
\qquad c_{\rm iso}=(36\pi)^{1/3},
\]

entraîne alors

\[
\int_{H_{j,\sigma}}|W_j|,dx
\ge \frac{c_{\rm iso}}6\lambda V_{j,\sigma}^{2/3}.
\]

La source primaire proposée pour cette brique est Federer–Fleming,
**NS-SRC-0148**, dont l'inégalité isopérimétrique pour courants intégraux
couvre la formulation des ensembles de périmètre fini utilisée ici. La
preuve directe pour les ensembles de Caccioppoli est aussi celle de De
Giorgi, *Sulla proprietà isoperimetrica dell'ipersfera, nella classe degli
insiemi aventi frontiera orientata di misura finita*, *Atti Accad. Naz.
Lincei Mem.* (8) 5 (1958), 33–44, sans DOI identifié.

Point important : l'isopérimétrie **relative** n'est pas nécessaire. Les
fonctions sont compactement supportées et les superniveaux ont mesure finie
dans \(\mathbb R^3\). Il n'existe aucun terme de frontière de cellule à
absorber.

### 2.4 Intégration sur un ensemble de mesure finie en faible-Lorentz

Pour \(p>1\), la définition de \(K_p\) et la formule par couches donnent,
pour tout ensemble mesurable \(A\) de mesure finie,

\[
\int_A|f|\,dx
\le \frac{p}{p-1}K_p(f)|A|^{1-1/p}.
\]

En effet, on partage l'intégrale des distributions au niveau
\(a=K_p(f)|A|^{-1/p}\). Pour \(p=3/2\), la constante issue de ce calcul est
exactement \(3\). Cette brique relève aussi de la théorie Lorentz de Hunt,
déjà cataloguée sous **NS-SRC-0069**; la constante \(3\) ci-dessus est
recalculée, non attribuée textuellement à Hunt.

Ainsi

\[
\int_H|W|\,dx
\le 3K_w|H|^{1/3}
\le \frac{18K_wK_u}{\lambda}.
\]

La disjonction des supports complets permet ici d'identifier
\(|W|=|W_j|\) sur chaque bande et de sommer sans chevauchement.

### 2.5 Sélection quantitative et constante suivie

Choisir \(\lambda\) presque optimal, c'est-à-dire, pour \(0<\eta<1\),

\[
\lambda|D|^{1/3}\ge(1-\eta)K_u.
\]

Alors

\[
\sum_{j,\sigma}V_{j,\sigma}
\ge |D|
\ge\left(\frac{(1-\eta)K_u}{\lambda}\right)^3.
\]

Si

\[
\varepsilon=\max_jK_3(U_j),
\]

l'inclusion \(E_{j,\sigma}\subset\{|U_j|>\lambda/3\}\) donne

\[
V_{j,\sigma}^{1/3}
\le\frac{3K_3(U_j)}{\lambda}
\le\frac{3\varepsilon}{\lambda}.
\]

Par conséquent,

\[
\sum V_{j,\sigma}
\le\frac{3\varepsilon}{\lambda}
\sum V_{j,\sigma}^{2/3}.
\]

En combinant cette relation, la minoration coaire/isopérimétrie et la
majoration faible-Lorentz, on obtient

\[
\frac{c_{\rm iso}(1-\eta)^3K_u^3}
{18\varepsilon\lambda}
\le \int_H|W|\,dx
\le\frac{18K_wK_u}{\lambda}.
\]

Donc, puis en faisant \(\eta\downarrow0\),

\[
\boxed{
\varepsilon\ge
\frac{(36\pi)^{1/3}}{324}\frac{K_u^2}{K_w}}
\]

pour la convention de quasi-norme fixée. Comme la famille est finie, le
maximum est atteint. Si \(j_*\) le réalise, la disjonction donne
\(K_{3/2}(W_{j_*})\le K_w\), donc

\[
\boxed{
\frac{K_3(U_{j_*})}{K_{3/2}(W_{j_*})}
\ge
\frac{(36\pi)^{1/3}}{324}
\left(\frac{K_u}{K_w}\right)^2.}
\]

Le cas \(K_w=0\) est impossible lorsque \(K_u>0\) dans cette classe : la
formule du curl impose \(\nabla F_j=0\), puis le support compact impose
\(F_j=0\).

## 3. Ce que publient réellement les familles de théorèmes voisines

| Famille/source primaire | Résultat réellement disponible | Implication pour le lemme actif | Non-transfert exact |
|---|---|---|---|
| Fleming–Rishel 1960, DOI [10.1007/BF01236935](https://doi.org/10.1007/BF01236935), **NS-SRC-0132**, publié | Formule de coaire/variation totale | **Brique directe** de la bande tronquée | Ne contient ni pure-swirl ni sélection Lorentz |
| Federer–Fleming 1960, DOI [10.2307/1970227](https://doi.org/10.2307/1970227), proposé **NS-SRC-0148**, publié | Inégalité isopérimétrique pour courants intégraux | **Brique directe** vers \(P(E)\gtrsim|E|^{2/3}\) | N'identifie ni le bon superniveau ni le curl |
| Korte–Lahti 2014, DOI [10.1016/j.anihpc.2013.01.005](https://doi.org/10.1016/j.anihpc.2013.01.005), proposé **NS-SRC-0149**, publié | Isopérimétries relatives dans des boules/dilatées sur espaces métriques doublants avec Poincaré | Analogue utile si une vraie frontière de cellule était imposée | Inutile ici; n'engendre pas un halo et introduirait une quantité relative de complément/bord |
| Hunt 1966, [texte primaire](https://www.e-periodica.ch/digbib/view?pid=ens-001%3A1966%3A12%3A%3A408), **NS-SRC-0069**, publié | Espaces Lorentz et inégalités de Hölder | **Brique directe**; la majoration sur \(H\) se recalcule aussi par couches | Ne sélectionne pas la bande commune |
| Lions 1984, DOI [10.1016/S0294-1449(16)30428-0](https://doi.org/10.1016/S0294-1449(16)30428-0), **NS-SRC-0140**, publié | Alternative compacité/évanescence/dichotomie pour suites minimisantes via fonction de concentration | Analogue pour la perte par translation ou queues | Ne s'applique pas à une famille finie arbitraire sans structure variationnelle; n'est pas requis |
| Lions 1985, DOI [10.4171/RMI/12](https://doi.org/10.4171/RMI/12), proposé **NS-SRC-0150**, publié | Cas limite avec invariance par dilatations; applications incluant inégalités faibles-\(L^p\) | Analogue critique plus proche | Toujours variationnel; ne couple pas \(U\) et \(\operatorname{curl}U\), ne donne pas la sélection littérale |
| Calderón–Zygmund 1952, DOI [10.1007/BF02392130](https://doi.org/10.1007/BF02392130), proposé **NS-SRC-0151**, publié | Décomposition en cubes d'arrêt et contrôle de mesure des mauvais cubes | Peut créer une union mesurable dilatée à coût de volume contrôlé | Pas de périmètre, diamètre, connexité, curl ou bande de transition; superflu ici |
| Coifman–Fefferman 1974, DOI [10.4064/sm-51-3-241-250](https://doi.org/10.4064/sm-51-3-241-250), proposé **NS-SRC-0152**, publié | Comparaisons distributionnelles/good-\(\lambda\) pour fonctions maximales et intégrales singulières pondérées | Analogue de propagation entre niveaux | Contrôle des mesures de superniveaux d'opérateurs, pas de géométrie BV ni de cellule pure-swirl |

### Conséquence négative précise

Aucun des théorèmes des quatre dernières lignes n'implique le lemme actif.
Inversement, leur absence ne crée aucun trou dans la dérivation du §2. La
preuve n'a besoin ni d'exclure l'évanescence, ni de contrôler une queue à
l'infini, ni de choisir des cubes de Whitney, ni de dilater un cœur.

## 4. Localisation dynamique Navier–Stokes : analogues, pas raccord

### Résultats déjà catalogués

Barker–Prange 2020 (**NS-SRC-0146**, DOI
[10.1007/s00205-020-01495-6](https://doi.org/10.1007/s00205-020-01495-6))
et Barker–Prange 2021 (**NS-SRC-0147**, DOI
[10.1007/s00220-021-04122-x](https://doi.org/10.1007/s00220-021-04122-x))
localisent, sous hypothèses de solution Navier–Stokes et de singularité, des
normes critiques ou de l'enstrophie dans des boules centrées au point
singulier et à l'échelle parabolique \(\sqrt{T^*-t}\). Le second résultat
requiert notamment une borne Type I faible-\(L^3\) pour ses conclusions
quantitatives.

Ces boules ont un volume géométriquement contrôlé, mais elles ne sont pas le
halo d'un superniveau donné. Leurs centres viennent de la singularité et leur
rayon vient du temps restant, non de \(V_{j,\sigma}\).

### Li–Ozawa–Wang 2018

Kuijie Li, Tohru Ozawa et Baoxiang Wang, *Dynamical behavior for the solutions
of the Navier-Stokes equation*, *Commun. Pure Appl. Anal.* 17 (2018),
1511–1560, DOI
[10.3934/cpaa.2018073](https://doi.org/10.3934/cpaa.2018073), arXiv
[1608.06680](https://arxiv.org/abs/1608.06680), proposé **NS-SRC-0153**,
publié.

Équation : Navier–Stokes incompressible non forcé sur \(\mathbb R^d\),
viscosité normalisée à \(1\), solutions mild dans les énoncés de
concentration/profils. Le papier obtient des phénomènes de concentration pour
des solutions mild qui blow-up et, en dimension trois, des conclusions de
compacité/minimalité et de profil Type I sous hypothèses \(L^p\), \(p>3\).

Non-transfert : ces résultats dépendent de la dynamique, d'une hypothèse de
blow-up et d'espaces forts. Ils ne fournissent ni une bande entre deux
superniveaux, ni un contrôle de volume par \(K_3(U)\), ni une sélection
simultanée faible-\(L^3\)/faible-\(L^{3/2}\).

### Barker 2023

Tobias Barker, *Localized Quantitative Estimates and Potential Blow-Up Rates
for the Navier–Stokes Equations*, *SIAM J. Math. Anal.* 55 (2023),
5221–5259, DOI
[10.1137/22M1527179](https://doi.org/10.1137/22M1527179), proposé
**NS-SRC-0154**, version of record publiée le 2023-09-28.

Cadre : solution faible adaptée lisse avant \(T_*\) sur
\(B(0,4)\times(0,T_*)\), avec point singulier \((x_0,T_*)\). Le résultat
donne une minoration quantitative de la croissance locale de la norme
\(L^3(B(x_0,\delta))\) et quantifie une procédure de
troncation/localisation avec termes de coupure et de Bogovskii.

Non-transfert : la boule extérieure est fixée, la singularité est supposée,
et les cols sont choisis pour l'inégalité d'énergie locale et la pression.
Le papier ne produit pas un ensemble \(H\) de volume comparable à un
superniveau ni la sélection statique du §2.

### Barker–Fernández-Dalgo–Prange 2024

Tobias Barker, Pedro Gabriel Fernández-Dalgo et Christophe Prange, *Blow-up
of dynamically restricted critical norms near a potential Navier–Stokes
singularity*, *Math. Ann.* 389 (2024), 1517–1543, DOI
[10.1007/s00208-023-02675-x](https://doi.org/10.1007/s00208-023-02675-x),
arXiv [2302.06509v2](https://arxiv.org/abs/2302.06509v2), proposé
**NS-SRC-0155**. Prépublication v2 du 2023-02-24; version of record publiée
le 2023-07-20; numéro daté juin 2024.

Cadre : solution de Leray–Hopf/d'énergie finie sur
\(\mathbb R^3\times(-1,0)\), lisse avant un premier temps singulier, avec
point singulier \((0,0)\). Le théorème principal force le blow-up de normes
critiques restreintes à la région dynamique

\[
B_0(\sqrt a)\setminus B_0(\sqrt{-at}),
\]

en \(L^3\) dans le cas général et en faible-\(L^3\) dans le cas
axisymétrique. La preuve emploie des poids et coupures mobiles à l'échelle
\(N\sqrt{-t}\), avec \(N\) dépendant du contrôle critique, afin de maîtriser
notamment la pression non locale.

C'est le meilleur analogue publié d'un « anneau dynamique », mais il
n'implique pas le lemme actif :

- l'anneau est fixé par la géométrie parabolique d'une singularité, non par
  deux niveaux de \(F_j\);
- le volume de la zone de coupure dépend de \((-t)^{3/2}\) et de \(N\), pas
  de \(V_{j,\sigma}\);
- la conclusion est un critère de régularité/blow-up pour une vraie solution,
  pas une inégalité BV statique;
- le cas faible-\(L^3\) exige l'axisymétrie et ne sélectionne pas en parallèle
  une cellule faible-\(L^{3/2}\) de vorticité.

## 5. Identifiants proposés à partir de NS-SRC-0148

Ces identifiants sont réservés à l'intégration éventuelle par l'agent
principal. Ce rapport ne modifie pas sources.json.

| ID proposé | Métadonnées primaires et statut | Rôle exact |
|---|---|---|
| **NS-SRC-0148** | Herbert Federer et Wendell H. Fleming, *Normal and Integral Currents*, *Ann. Math.* 72 (1960), 458–520, DOI [10.2307/1970227](https://doi.org/10.2307/1970227), [JSTOR](https://www.jstor.org/stable/1970227), publié | isopérimétrie euclidienne pour courants/ensembles de périmètre fini; brique directe |
| **NS-SRC-0149** | Riikka Korte et Panu Lahti, *Relative isoperimetric inequalities and sufficient conditions for finite perimeter on metric spaces*, *Ann. IHP ANL* 31 (2014), 129–154, DOI [10.1016/j.anihpc.2013.01.005](https://doi.org/10.1016/j.anihpc.2013.01.005), [NUMDAM](https://www.numdam.org/item/AIHPC_2014__31_1_129_0/), publié | isopérimétrie relative; analogue non requis |
| **NS-SRC-0150** | Pierre-Louis Lions, *The Concentration-Compactness Principle in the Calculus of Variations. The Limit Case, Part 2*, *Rev. Mat. Iberoam.* 1 (1985), no 2, 45–121, DOI [10.4171/RMI/12](https://doi.org/10.4171/RMI/12), [EMS Press](https://ems.press/journals/rmi/articles/10762), publié le 1985-06-30 | défaut de compacité critique/dilatations, applications faible-\(L^p\); analogue |
| **NS-SRC-0151** | A. P. Calderón et A. Zygmund, *On the existence of certain singular integrals*, *Acta Math.* 88 (1952), 85–139, DOI [10.1007/BF02392130](https://doi.org/10.1007/BF02392130), publié | cubes d'arrêt/décomposition de mauvais niveaux; analogue de covering |
| **NS-SRC-0152** | R. R. Coifman et C. Fefferman, *Weighted norm inequalities for maximal functions and singular integrals*, *Studia Math.* 51 (1974), 241–250, DOI [10.4064/sm-51-3-241-250](https://doi.org/10.4064/sm-51-3-241-250), [éditeur primaire](https://www.impan.pl/en/publishing-house/journals-and-series/studia-mathematica/all/51/3/100345/weighted-norm-inequalities-for-maximal-functions-and-singular-integrals), publié | good-\(\lambda\)/comparaison distributionnelle; analogue |
| **NS-SRC-0153** | Kuijie Li, Tohru Ozawa et Baoxiang Wang, *Dynamical behavior for the solutions of the Navier-Stokes equation*, *CPAA* 17 (2018), 1511–1560, DOI [10.3934/cpaa.2018073](https://doi.org/10.3934/cpaa.2018073), arXiv [1608.06680](https://arxiv.org/abs/1608.06680), publié en avril 2018 | concentration/profils de solutions mild et scénarios Type I; analogue dynamique |
| **NS-SRC-0154** | Tobias Barker, *Localized Quantitative Estimates and Potential Blow-Up Rates for the Navier–Stokes Equations*, *SIAM J. Math. Anal.* 55 (2023), 5221–5259, DOI [10.1137/22M1527179](https://doi.org/10.1137/22M1527179), publié le 2023-09-28 | troncation/localisation quantitative près d'une singularité; analogue dynamique avec pression |
| **NS-SRC-0155** | Tobias Barker, Pedro Gabriel Fernández-Dalgo et Christophe Prange, *Blow-up of dynamically restricted critical norms near a potential Navier–Stokes singularity*, *Math. Ann.* 389 (2024), 1517–1543, DOI [10.1007/s00208-023-02675-x](https://doi.org/10.1007/s00208-023-02675-x), arXiv [2302.06509v2](https://arxiv.org/abs/2302.06509v2), version of record 2023-07-20, numéro 2024 | normes critiques sur anneau dynamique; meilleur analogue, mais non-transfert |

Ne pas créer de nouveaux IDs pour Fleming–Rishel (**NS-SRC-0132**), Hunt
(**NS-SRC-0069**), Lions 1984 (**NS-SRC-0140**) ou Barker–Prange
(**NS-SRC-0146** et **0147**).

## 6. Veille différentielle au 2026-08-14

Les notices primaires ciblées ont été recontrôlées. Aucun changement de
statut visible ne fournit la sélection littérale.

| Prépublication primaire | Version visible | Rapport au lemme |
|---|---|---|
| Lei–Ren–Tian, [arXiv:2501.08976](https://arxiv.org/abs/2501.08976) | v1, 2025-01-15; aucune référence de revue affichée | critère géométrique conditionnel pour solution faible adaptée; ne construit pas la bande |
| Grujić, [arXiv:2511.00725](https://arxiv.org/abs/2511.00725) | v3, 2026-06-10; aucune référence de revue affichée | mécanisme conditionnel pour deux anneaux de vorticité; pas de sélection générale |
| Grujić, [arXiv:2607.08866](https://arxiv.org/abs/2607.08866) | v2, 2026-07-13; aucune référence de revue affichée | suppose concentration faible-\(L^{3/2}\) et géométrie log-BMO supplémentaire |
| Barker, [arXiv:2510.20757](https://arxiv.org/abs/2510.20757) | v3, 2026-08-11; aucune référence de revue affichée | classification quantitative sous proximité axisymétrique; pas le lemme statique |
| Shahmurov, [arXiv:2606.07869](https://arxiv.org/abs/2606.07869) | v1, 2026-06-05; aucune référence de revue affichée | revendication récente non auditée, aucun transfert retenu |
| Shahmurov, [arXiv:2605.09797](https://arxiv.org/abs/2605.09797) | v2, 2026-05-15; aucune référence de revue affichée | revendication Clay non auditée, aucun transfert retenu |

Cette veille est différentielle et ciblée; elle n'est pas une preuve
d'absence absolue dans toute la littérature.

## 7. Passe contradictoire

### Quantificateurs et seuil presque optimal

- Le supremum définissant \(K_u\) n'a pas à être atteint. L'argument doit
  garder \(\eta>0\), puis faire \(\eta\downarrow0\).
- L'isopérimétrie est appliquée pour presque tout
  \(t\in(\lambda/4,\lambda/2)\). Les valeurs critiques aux deux extrémités
  n'affectent pas l'intégrale de coaire.
- Les ensembles positifs et négatifs doivent être séparés. Ils sont
  disjoints pour chaque cellule, comme les supports le sont entre cellules.

### Constantes, dimensions et supports

- La constante \(2/3\) vient uniquement de l'anneau radial figé. Élargir
  l'anneau change la constante; permettre l'axe détruit ce contrôle.
- Le facteur \(18\) de la majoration est \(3\times6\) : intégration
  faible-\(L^{3/2}\) puis inclusion de \(H\) dans le superniveau
  \(\lambda/6\).
- Aucune constante ne dépend du nombre de cellules, de leur longueur axiale,
  de leur volume ou d'un plateau.
- La disjonction doit porter sur les supports complets. Des supports de
  vitesse seulement « essentiellement disjoints » avec des curls qui se
  chevauchent ne justifient pas la sommation employée.

### Risques de mauvaise lecture

- \(H\not\supset E\). Toute preuve qui utilise cette inclusion est fausse.
- La minoration du périmètre d'un superniveau plus grand vient de
  l'isopérimétrie globale et de son volume, pas de la monotonie du périmètre,
  qui est fausse en général.
- Aucun contrôle de pression, projection de Leray ou frontière n'est caché :
  le résultat est une identité/inégalité sur des champs statiques explicites.
- Une version pour une famille infinie demanderait un passage à la limite et
  un contrôle de sommation qui ne sont pas prouvés ici.
- Une version pour cellules chevauchantes, champs non axisymétriques ou
  décompositions approchées demanderait des termes d'erreur nouveaux.

### Écart Clay

Le lemme s'applique à une sous-classe géométrique construite. Pour affecter le
problème Clay, il faudrait encore un maillon démontré du type

\[
\text{profil limite d'une solution NS générale}
\Longrightarrow
\text{décomposition finie pure-swirl, disjointe, sans reste critique}.
\]

Aucun résultat primaire contrôlé ne fournit ce maillon. La sélection ne
prouve donc ni régularité globale, ni exclusion d'un blow-up, ni existence
d'une solution ancienne rigide.

## Conclusion opérationnelle

Le verrou « halo de volume contrôlé » est **abandonné pour l'énoncé littéral** :
il provenait d'une mauvaise représentation de la bande. La dérivation du §2
ferme le lemme fini pure-swirl avec une constante universelle explicite à
partir de trois briques classiques.

La prochaine action à meilleure valeur informationnelle est une vérification
formelle indépendante du lemme fini, puis un test de stabilité sous l'une des
deux relaxations minimales suivantes :

1. supports de cellules ayant un recouvrement borné \(m>1\), avec constante
   explicitement suivie en \(m\);
2. somme infinie tronquée, avec contrôle uniforme des queues dans les deux
   quasi-normes faibles.

Un échec uniforme dans l'un de ces deux passages délimiterait exactement la
portée du mécanisme. Une recherche supplémentaire de halos géométriques ne
testerait plus le lemme actif.
