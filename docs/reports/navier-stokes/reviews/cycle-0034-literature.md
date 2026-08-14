# Cycle 0034 — revue primaire : sélection faible-Lorentz et localisation curl/Biot–Savart

Date de coupure : **2026-08-14**
Objet : outils publiés susceptibles de transformer les bornes globales
\(U\in L^{3,\infty}(\mathbb R^3)\) et
\(W=\nabla\times U\in L^{3/2,\infty}(\mathbb R^3)\) en un bloc spatial
commun; veille différentielle des prépublications Navier–Stokes déjà suivies.

## Verdict falsifiable

La littérature primaire contrôlée ne fournit pas le lemme statique recherché :

> à partir des seules bornes faible-\(L^3\) de \(U\) et
> faible-\(L^{3/2}\) de \(W=\operatorname{curl}U\), sélectionner une cellule
> \(Q\) qui porte une fraction uniforme de la quantité de vitesse et un
> contrôle de vorticité compatible sur cette même cellule.

Trois raisons distinctes sont établies.

1. Les identités de distribution sur supports disjoints n'impliquent aucune
   cellule de masse faible-Lorentz uniformément dominante.
2. Les décompositions de profils publiées partent d'une suite bornée dans un
   **espace source plus fort**, puis rendent le reste petit dans un espace
   cible plus faible. Elles ne décomposent pas une suite arbitraire seulement
   bornée dans \(L^{3,\infty}\) ou \(L^{3/2,\infty}\). Les empilements
   multi-échelles au même indice secondaire faible sont précisément un
   endpoint non couvert.
3. Biot–Savart donne un raccord global unilatéral, mais sa localisation laisse
   un champ lointain harmonique/de bord et des commutateurs de cutoff de taille
   critique. Une reconstruction locale depuis le seul curl est donc fausse
   sans donnée de bord, contrôle du champ lointain ou terme local de vitesse.

Le résultat publié le plus proche d'un raccord « même centre » est dynamique :
Barker–Prange obtiennent, sous borne Type I et en supposant déjà un point
singulier, des concentrations locales de vitesse et d'enstrophie centrées au
point singulier. Ce résultat ne devient pas un lemme statique aux deux
endpoints faibles.

## Cadre exact et échelle

Dans cette revue, sauf indication contraire,

\[
\nabla\cdot U=0,\qquad W=\nabla\times U
\quad\text{sur }\mathbb R^3,
\]

et l'on fixe la jauge globale par décroissance/intégrabilité suffisante lorsque
la formule de Biot–Savart est utilisée. La remise à l'échelle stationnaire
induite par Navier–Stokes est

\[
U_\lambda(x)=\lambda U(\lambda x),\qquad
W_\lambda(x)=\lambda^2W(\lambda x).
\]

Par conséquent,

\[
\|U_\lambda\|_{L^{3,\infty}}
=\|U\|_{L^{3,\infty}},\qquad
\|W_\lambda\|_{L^{3/2,\infty}}
=\|W\|_{L^{3/2,\infty}}.
\]

La concentration locale d'enstrophie est elle aussi critique sous la forme

\[
\int_{B(0,cr)}|W|^2\,dx\sim r^{-1}.
\]

Pour rendre les calculs de cette note indépendants des conventions de
quasi-norme, on pose

\[
K_p(f):=\sup_{\alpha>0}\alpha\,d_f(\alpha)^{1/p},
\qquad
d_f(\alpha):=|\{x:|f(x)|>\alpha\}|.
\]

## 1. Sommes disjointes : ce qui est exact, et ce qui ne suit pas

Si les supports mesurables des \(f_j\) sont deux à deux disjoints, alors

\[
\left|\sum_jf_j\right|=\sum_j|f_j|\quad\text{p.p.},\qquad
d_{\sum_jf_j}(\alpha)=\sum_jd_{f_j}(\alpha).
\]

Il en résulte exactement

\[
K_p\!\left(\sum_jf_j\right)^p
=\sup_{\alpha>0}\sum_j\alpha^p d_{f_j}(\alpha)
\leq\sum_j K_p(f_j)^p
\]

et

\[
\max_jK_p(f_j)\leq K_p\!\left(\sum_jf_j\right).
\]

La réciproque uniforme échoue déjà pour des fonctions scalaires. Prenons
\(N\) ensembles disjoints \(E_j\) de mesure \(1\) et

\[
f_j=N^{-1/p}\mathbf 1_{E_j}.
\]

Alors

\[
K_p(f_j)=N^{-1/p},\qquad
K_p\!\left(\sum_{j=1}^Nf_j\right)=1.
\]

Ainsi, une borne globale faible-\(L^p\) ne sélectionne pas une cellule portant
une fraction positive indépendante de \(N\).

### Limite adversariale de ce contre-exemple

Ce calcul ne réfute **pas** un éventuel lemme exploitant
\(W=\operatorname{curl}U\), la divergence nulle ou la dynamique
Navier–Stokes. Il interdit seulement de déduire la sélection cherchée de
l'algèbre de Banach-réseau de Lorentz.

En outre, les exposants des deux champs agrègent différemment. Pour des blocs
identiques et des niveaux alignés, la vitesse acquiert un facteur
\(N^{1/3}\), tandis que la vorticité acquiert un facteur \(N^{2/3}\).
Suivant le ratio choisi, la dispersion peut donc rendre un ratio local
meilleur que le ratio global. Une affirmation « la dispersion détruit
toujours le bon ratio » serait incorrecte. Le prochain test doit imposer le
curl exact et mesurer les deux quasi-normes, non juxtaposer deux exemples
scalaires indépendants.

## 2. Audit des théorèmes de concentration-compacité et de profils

| Source primaire et statut | Théorème utile | Hypothèse source réellement requise | Pourquoi il ne donne pas la même cellule \(U/W\) |
|---|---|---|---|
| P.-L. Lions, *The concentration-compactness principle in the Calculus of Variations. The locally compact case, part 1*, *Ann. IHP ANL* 1 (1984), 109–145, [DOI 10.1016/S0294-1449(16)30428-0](https://doi.org/10.1016/S0294-1449(16)30428-0), [texte primaire](https://ems.press/journals/aihpc/articles/4077966), publié | Alternative compacité/évanescence/dichotomie via fonction de concentration d'une mesure; application à des suites minimisantes sous sous-additivité stricte | Mesure positive et structure variationnelle/minimisante | Ne traite ni une paire \((U,\operatorname{curl}U)\), ni les deux endpoints faibles, ni une cellule commune; la dichotomie est une issue, pas un mécanisme général pour l'exclure |
| Sergio Solimini, *A note on compactness-type properties with respect to Lorentz norms of bounded subsets of a Sobolev Space*, *Ann. IHP ANL* 12 (1995), 319–337, [DOI 10.1016/S0294-1449(16)30159-7](https://doi.org/10.1016/S0294-1449(16)30159-7), [texte primaire](https://ems.press/journals/aihpc/articles/4076551), publié | Pour une suite bornée dans \(\dot W^{1,p}\), \(1<p<3\), extraction de profils par translations/dilatations; reste petit dans \(L^{p^\*,q}\) pour \(q>p\) | Borne Sobolev \(\dot W^{1,p}\), et indice secondaire cible non optimal \(q>p\) | Atteindre \(U\) dans \(L^{3,\infty}\) demanderait ici une borne \(\dot W^{1,3/2}\), absente des gates. Atteindre \(W\) dans \(L^{3/2,\infty}\) mène à l'endpoint \(p=1\), qui exige encore un contrôle de dérivée. Les profils sont ceux d'un seul champ; aucun synchronisme \(U/W\) |
| Patrick Gérard, *Description du défaut de compacité de l'injection de Sobolev*, *ESAIM COCV* 3 (1998), 213–233, [texte primaire NUMDAM](https://numdam.org/item/COCV_1998__3__213_0/), publié | Profils modulo translations/dilatations pour une injection de Sobolev homogène critique dans un cadre hilbertien | Borne dans l'espace de Sobolev source | Ne part pas d'une borne dans le seul espace cible faible-Lorentz et décompose un seul champ |
| Stéphane Jaffard, *Analysis of the Lack of Compactness in the Critical Sobolev Embeddings*, *J. Funct. Anal.* 161 (1999), 384–396, [DOI 10.1006/jfan.1998.3364](https://doi.org/10.1006/jfan.1998.3364), [page primaire éditeur](https://www.sciencedirect.com/science/article/pii/S002212369893364X), publié | Décomposition en profils de suites bornées dans des espaces potentiels de Sobolev; reste petit dans le Lebesgue critique fort | Borne Sobolev/Riesz source plus forte | Pas de suite arbitraire bornée dans faible-\(L^q\); pas de paire couplée par curl |
| Gabriel S. Koch, *Profile Decompositions for Critical Lebesgue and Besov Space Embeddings*, *Indiana Univ. Math. J.* 59 (2010), 1801–1830, [DOI 10.1512/iumj.2010.59.4426](https://doi.org/10.1512/iumj.2010.59.4426), [journal](https://iumj.org/article/5379/), [arXiv:1006.3064](https://arxiv.org/abs/1006.3064), publié | Décomposition ondélette abstraite pour plongements critiques \(X\hookrightarrow Y\), pertinente pour les espaces NS | Suite bornée dans \(X\), avec un plongement source-cible et des propriétés d'approximation non linéaire | Ne transforme pas une borne dans le seul espace cible \(Y=L^{3,\infty}\) en profil; un seul champ est décomposé |
| Hajer Bahouri, Albert Cohen et Gabriel Koch, *A general wavelet-based profile decomposition in the critical embedding of function spaces*, *Confluentes Math.* 3 (2011), 387–411, [DOI 10.1142/S1793744211000370](https://doi.org/10.1142/S1793744211000370), [texte primaire](https://cml.centre-mersenne.org/articles/10.1142/S1793744211000370/), publié | Théorème abstrait \(X\hookrightarrow Y\) : profils par translations/dilatations, reste petit dans \(Y\); exemples Sobolev, Besov, Triebel–Lizorkin, Lorentz et BMO | Suite bornée dans un espace source \(X\) plus coercif; hypothèses d'approximation/unconditionalité | Le cas \(X=Y=L^{q,\infty}\) n'est pas fourni. Pour les cibles Lorentz faibles, le mécanisme passe par un indice secondaire source strictement plus fort. L'empilement d'une ondelette par échelle fait échouer leur hypothèse au même indice secondaire; les auteurs conjecturent alors l'échec général, sans le démontrer |
| Gallagher, Koch et Planchon, *A profile decomposition approach to the \(L_t^\infty L_x^3\) Navier–Stokes regularity criterion*, *Math. Ann.* 355 (2013), 1527–1559, [DOI 10.1007/s00208-012-0830-0](https://doi.org/10.1007/s00208-012-0830-0), [arXiv:1012.0145](https://arxiv.org/abs/1012.0145), publié, déjà **NS-SRC-0014** | Décomposition de profils adaptée à NS et argument de solution critique/minimale dans le cadre fort \(L^3\) | Données dans les espaces critiques forts/Besov du théorème; dynamique NS | Le endpoint spatial est \(L^3\), pas \(L^{3,\infty}\); aucune sélection simultanée de vorticité faible-\(L^{3/2}\) |

### Lecture exacte de l'endpoint de Solimini

Pour \(N=3\), \(p^\*=3p/(3-p)\). Obtenir la cible
\(p^\*=3\) impose \(p=3/2\); la suite doit donc être bornée dans
\(\dot W^{1,3/2}\). Cette hypothèse contrôle précisément une dérivée qui
n'est pas contenue dans la seule borne \(U\in L^{3,\infty}\).

Pour viser \(p^\*=3/2\), on arrive à \(p=1\). Le texte discute l'extension
\(p=1\), avec une sommabilité plus faible, mais elle demanderait encore une
borne de type \(\dot W^{1,1}\) sur \(W\), absente du problème actif.

Le point positif est réel : \(\infty>p\), donc une cible
\(L^{p^\*,\infty}\) est compatible avec la partie « indice secondaire non
optimal » lorsque l'on possède la borne Sobolev source. Le point négatif est
tout aussi précis : cette borne source est exactement ce qui manque.

### Empilement multi-échelle : statut logique

Bahouri–Cohen–Koch exposent un empilement avec une ondelette à chaque échelle
qui fait échouer leur hypothèse d'approximation lorsque les indices
secondaires source et cible coïncident. Il faut conserver deux statuts
distincts :

- **démontré dans la source** : l'hypothèse abstraite employée par leur
  théorème échoue pour cet empilement;
- **conjecturé dans la source** : une décomposition de profils générale
  devrait alors échouer.

Cette source ne prouve donc pas l'impossibilité absolue d'une autre
décomposition en \(L^{q,\infty}\). Elle montre que le mécanisme publié ne peut
pas être invoqué au endpoint sans hypothèse supplémentaire.

## 3. Pourquoi deux décompositions séparées ne synchronisent pas les cellules

Même si l'on ajoutait assez de régularité pour appliquer séparément un
théorème de profils à \(U_n\) et à \(W_n\), les paramètres extraits

\[
(x^U_{j,n},\lambda^U_{j,n})
\quad\text{et}\quad
(x^W_{k,n},\lambda^W_{k,n})
\]

ne seraient pas automatiquement identiques. L'identité
\(W_n=\operatorname{curl}U_n\) doit être transportée à travers :

- les remises à l'échelle, dont les amplitudes diffèrent d'une puissance;
- les cutoffs ou projecteurs utilisés pour isoler les profils;
- la convergence faible, insuffisante pour identifier certains défauts
  quadratiques;
- le reste, petit dans un espace cible mais pas nécessairement après
  différentiation.

En faible-Lorentz, il n'existe en outre pas une « masse » additive commune.
La quasi-norme prend un supremum sur le niveau \(\alpha\), et les niveaux
optimisants peuvent être différents d'une cellule et d'un champ à l'autre.
Une preuve par pigeonhole qui additionnerait directement les quasi-normes de
\(U\) et \(W\) inverserait donc un supremum et une somme.

Conclusion : une décomposition de profils **jointe et curl-compatible** serait
un nouveau lemme; elle n'est pas une conséquence formelle des théorèmes
ci-dessus.

## 4. Biot–Savart global et défaut exact de localisation

Sous les hypothèses globales permettant de fixer la composante harmonique,

\[
U=\nabla\times(-\Delta)^{-1}W=K*W,
\qquad |K(z)|\lesssim |z|^{-2}.
\]

L'inégalité de convolution faible de O'Neil donne le raccord global
unilatéral

\[
\|U\|_{L^{3,\infty}(\mathbb R^3)}
\le C\|W\|_{L^{3/2,\infty}(\mathbb R^3)}.
\]

Source primaire : Richard O'Neil, *Convolution operators and
\(L(p,q)\) spaces*, *Duke Math. J.* 30 (1963), 129–142,
[DOI 10.1215/S0012-7094-63-03015-1](https://doi.org/10.1215/S0012-7094-63-03015-1),
déjà **NS-SRC-0067**.

Cette estimation n'est ni une minoration inverse, ni une estimation locale.
Pour \(B=B(x_0,r)\), la séparation

\[
W=W\mathbf 1_{2B}+W\mathbf 1_{(2B)^c}
\]

donne

\[
\|K*(W\mathbf 1_{2B})\|_{L^{3,\infty}}
\lesssim\|W\mathbf 1_{2B}\|_{L^{3/2,\infty}},
\]

mais, pour \(x\in B\), l'inégalité de Hölder de Lorentz et

\[
\big\||x-\cdot|^{-2}\mathbf 1_{(2B)^c}\big\|_{L^{3,1}}
\lesssim r^{-1}
\]

donnent seulement

\[
\|K*(W\mathbf 1_{(2B)^c})\|_{L^\infty(B)}
\lesssim r^{-1}\|W\|_{L^{3/2,\infty}}.
\]

Après multiplication par \(|B|^{1/3}\sim r\), la contribution lointaine en
faible-\(L^3(B)\) reste d'ordre
\(\|W\|_{L^{3/2,\infty}}\) : elle est **critique**, non petite lorsque
\(r\downarrow0\). À l'intérieur de \(B\), ce champ lointain est une composante
harmonique/de bord. Après la coupure brute de \(W\), il ne faut pas l'appeler
automatiquement « curl-free », car la coupure crée elle-même des défauts de
divergence.

### Le cutoff ne ferme pas le système

Pour une coupure \(\chi\) adaptée à une cellule de rayon \(r\),

\[
\operatorname{curl}(\chi U)
=\chi W+\nabla\chi\times U,\qquad
\operatorname{div}(\chi U)=\nabla\chi\cdot U.
\]

Comme \(|\nabla\chi|\sim r^{-1}\), le terme de col
\(\nabla\chi\times U\) est de taille critique sous l'échelle
Navier–Stokes. La projection de Leray de \(\chi U\) rétablit la divergence
nulle, mais elle est non locale. Ainsi \((\chi U,\chi W)\) n'est pas une paire
curl-compatible exacte.

Une formulation locale viable doit contrôler au moins l'un des objets
suivants :

- la composante harmonique/de bord;
- le terme de col \(\nabla\chi\times U\);
- une trace ou une jauge locale;
- un terme local de vitesse en plus du curl;
- une quantité de packing/Carleson qui rend ces défauts sélectionnables.

## 5. Le raccord dynamique publié le plus proche : Barker–Prange

### Localized smoothing, 2020

Tobias Barker et Christophe Prange,
*Localized Smoothing for the Navier–Stokes Equations and Concentration of
Critical Norms Near Singularities*, *Arch. Ration. Mech. Anal.* 236 (2020),
1487–1541,
[DOI 10.1007/s00205-020-01495-6](https://doi.org/10.1007/s00205-020-01495-6),
[arXiv:1812.09115](https://arxiv.org/abs/1812.09115), publié.

Équation : Navier–Stokes incompressible 3D non forcé sur \(\mathbb R^3\),
viscosité normalisée à \(1\). Notions : solutions d'énergie locale et
Leray–Hopf selon les énoncés. Le papier établit un lissage local depuis une
petitesse locale de la vitesse en \(L^3\); l'appendice traite aussi une donnée
locale faible-\(L^3\). Sous scénario Type I et présence d'une singularité, il
en déduit une concentration de norme critique près du point singulier.

Transfert : le centre singulier fournit une cellule de vitesse
dynamiquement distinguée. Non-transfert : aucune vorticité
\(L^{3/2,\infty}\) n'est simultanément sélectionnée par les seules gates
statiques du cycle.

### Quantitative concentration, 2021

Tobias Barker et Christophe Prange,
*Quantitative Regularity for the Navier–Stokes Equations Via Spatial
Concentration*, *Commun. Math. Phys.* 385 (2021), 717–792,
[DOI 10.1007/s00220-021-04122-x](https://doi.org/10.1007/s00220-021-04122-x),
[texte primaire éditeur](https://link.springer.com/article/10.1007/s00220-021-04122-x),
publié.

Équation : Navier–Stokes incompressible 3D, non forcé, sur
\(\mathbb R^3\times(0,T)\), \(\nu=1\). Sous

\[
\|u\|_{L^\infty_tL^{3,\infty}_x}\le M
\]

et si \((0,T^\*)\) est un point singulier au premier temps de blow-up, leur
théorème A donne, pour une plage explicite de rayons,

\[
\int_{|x|<R}|u(x,t)|^3\,dx
\ge
\frac{\log\!\left(R^2/(M^{802}|T^\*-t|)\right)}
{\exp(\exp(M^{1025}))}.
\]

Leur lemme 3.2 donne, pour une solution adaptée d'énergie finie sur
\([-1,0]\), une singularité en \((0,0)\) et presque tout \(t'<0\),

\[
\int_{B_0(4(S^\sharp)^{-1/2}(-t')^{1/2})}
|\omega(x,t')|^2\,dx
>
M^2(-t')^{-1/2}\sqrt{S^\sharp},
\qquad S^\sharp=CM^{-100}.
\]

Ces deux résultats sont centrés au même point singulier et aux échelles
paraboliques contrôlées. C'est le maillon publié le plus proche d'une
sélection commune. Mais :

- la vitesse est mesurée par un \(L^3\) local, la vorticité par une enstrophie
  locale \(L^2\), non par les deux quasi-normes faibles du lemme actif;
- un point singulier et une borne Type I sont supposés;
- la sélection dépend de la dynamique et de \(M\);
- elle ne donne pas un ratio local
  \(K_{3,Q}(U)/K_{3/2,Q}(W)\) issu de deux gates globales statiques.

Surtout, l'estimation elliptique locale (77) du papier est

\[
\|\nabla U\|_{L^2(B_0(2))}
\le C_{\rm ellip}\left(
\|\Omega\|_{L^2(B_0(4))}
+\|U\|_{L^2(B_0(4))}
\right).
\]

Le terme local \(\|U\|_{L^2}\) est une trace explicite de la composante
harmonique/de bord. Cette formule primaire confirme que le curl local seul ne
reconstruit pas la vitesse locale.

## 6. Implication vers le gap actif

La chaîne autorisée par les sources est :

\[
\begin{aligned}
&\text{borne dans un espace source plus fort}\\
&\quad\Longrightarrow
\text{profils modulo translations/dilatations}\\
&\quad\Longrightarrow
\text{reste petit dans une cible faible plus large}.
\end{aligned}
\]

La chaîne requise par le gap serait :

\[
\begin{aligned}
&U\in L^{3,\infty},\quad
W=\operatorname{curl}U\in L^{3/2,\infty}\\
&\quad\Longrightarrow
\text{profil/cellule jointe curl-compatible}\\
&\quad\Longrightarrow
\text{ratio local quantitativement favorable}.
\end{aligned}
\]

Le premier maillon de cette seconde chaîne est **manquant**. Ni Lions,
Solimini, Gérard, Jaffard, Koch, Bahouri–Cohen–Koch, ni
Gallagher–Koch–Planchon ne l'établissent.

Barker–Prange remplacent ce maillon par des hypothèses dynamiques fortes :

\[
\text{solution NS + Type I + point singulier}
\Longrightarrow
\text{même centre de concentration}.
\]

Ce résultat est transférable seulement si le programme actif accepte de
travailler par contradiction autour d'une singularité Type I. Il ne couvre ni
un scénario Type II général, ni un champ statique arbitraire, ni directement
le problème Clay complet.

## 7. Veille différentielle ciblée des prépublications suivies

Les notices arXiv primaires ont été recontrôlées le 2026-08-14. Cette veille
est ciblée; elle n'établit pas l'absence absolue de toute discussion ou source
future.

| Source primaire | Version visible le 2026-08-14 | Statut différentiel et rapport au gap |
|---|---|---|
| Zhen Lei, Xiao Ren, Gang Tian, *A Geometric Characterization of Potential Navier–Stokes Singularities*, [arXiv:2501.08976](https://arxiv.org/abs/2501.08976) | v1, soumise le 2025-01-15; aucune référence de revue affichée | Inchangé. Critère local conditionnel par double cône de forte vorticité pour solution faible adaptée; ne produit pas le cône ni une cellule faible-Lorentz depuis les gates globales |
| Zoran Grujić, *On taming Moffatt–Kimura vortices of doom in the viscous case*, [arXiv:2511.00725](https://arxiv.org/abs/2511.00725) | v3, révisée le 2026-06-10; aucune référence de revue affichée | Inchangé. Mécanisme conditionnel à deux couches pour le scénario de deux anneaux; pas une décomposition curl-compatible de suites générales |
| Zoran Grujić, *Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier–Stokes Equations*, [arXiv:2607.08866](https://arxiv.org/abs/2607.08866) | v2, révisée le 2026-07-13; aucune référence de revue affichée | Inchangé. Suppose précisément une borne critique faible-\(L^{3/2}\) et une géométrie log-BMO supplémentaire; ne sélectionne pas le bloc actif depuis les seules gates |
| Tobias Barker, *Quantitative classification of potential Navier–Stokes singularities beyond the blow-up time*, [arXiv:2510.20757](https://arxiv.org/abs/2510.20757) | v3, révisée le 2026-08-11; aucune référence de revue affichée | Inchangé depuis la précédente veille. Classifications quantitatives sous approximation axisymétrique; ne ferme pas la sélection faible-Lorentz statique |
| Rishad Shahmurov, *Global Regularity for Axisymmetric Navier--Stokes Flows with Swirl*, [arXiv:2606.07869](https://arxiv.org/abs/2606.07869) | v1, soumise le 2026-06-05; aucune référence de revue affichée | Inchangé; annonce non auditée, maintenue en quarantaine. Aucun lemme n'est importé |
| Rishad Shahmurov, *A Classical Two-Part First-Threshold Proof of Global Smoothness for Navier--Stokes: Axisymmetric Swirl Closure and Full-System Reduction*, [arXiv:2605.09797](https://arxiv.org/abs/2605.09797) | v2, révisée le 2026-05-15; aucune référence de revue affichée | Inchangé; revendication Clay non auditée, maintenue en quarantaine. Aucun lemme n'est importé |

Aucune nouvelle version ou publication affichée par ces notices ne ferme le
gap « même cellule ».

## 8. Identifiants proposés après NS-SRC-0139

Ces identifiants sont des propositions pour l'intégration par l'agent
principal; ce rapport ne modifie pas le catalogue.

| ID proposé | Source | Statut proposé | Rôle exact |
|---|---|---|---|
| **NS-SRC-0140** | Lions 1984, DOI 10.1016/S0294-1449(16)30428-0 | PUBLISHED / SOURCE_VERIFIED | concentration-compacité, alternative compacité/évanescence/dichotomie |
| **NS-SRC-0141** | Solimini 1995, DOI 10.1016/S0294-1449(16)30159-7 | PUBLISHED / SOURCE_VERIFIED | profils Sobolev vers Lorentz d'indice secondaire non optimal |
| **NS-SRC-0142** | Gérard 1998, URL primaire NUMDAM | PUBLISHED / SOURCE_VERIFIED | défaut de compacité de l'injection de Sobolev |
| **NS-SRC-0143** | Jaffard 1999, DOI 10.1006/jfan.1998.3364 | PUBLISHED / SOURCE_VERIFIED | profils des plongements critiques de Sobolev |
| **NS-SRC-0144** | Koch 2010, DOI 10.1512/iumj.2010.59.4426 | PUBLISHED / SOURCE_VERIFIED | décomposition ondélette abstraite des plongements critiques |
| **NS-SRC-0145** | Bahouri–Cohen–Koch 2011, DOI 10.1142/S1793744211000370 | PUBLISHED / SOURCE_VERIFIED | décomposition abstraite; diagnostic précis du même indice secondaire |
| **NS-SRC-0146** | Barker–Prange 2020, DOI 10.1007/s00205-020-01495-6 | PUBLISHED / SOURCE_VERIFIED | lissage local et concentration critique près d'une singularité |
| **NS-SRC-0147** | Barker–Prange 2021, DOI 10.1007/s00220-021-04122-x | PUBLISHED / SOURCE_VERIFIED | concentration quantitative de vitesse/enstrophie et Hodge local avec terme de vitesse |

Ne pas créer un nouvel ID pour Gallagher–Koch–Planchon : la source est déjà
**NS-SRC-0014**. O'Neil est déjà **NS-SRC-0067**.

## 9. Passe contradictoire indépendante

### Quantificateurs

- « Chaque profil est localisé » n'implique pas « un profil porte une fraction
  uniforme de la quasi-norme globale ».
- « Il existe un profil de \(U\) » et « il existe un profil de \(W\) »
  n'impliquent pas « il existe un profil commun ».
- Une concentration obtenue sous l'hypothèse d'un point singulier ne sélectionne
  pas une cellule pour tout champ admissible.

### Constantes et troncatures

- Le champ lointain vaut \(O(r^{-1}K_W)\) en \(L^\infty(B_r)\); sa contribution
  faible-\(L^3(B_r)\) est \(O(K_W)\), sans petit facteur.
- Le cutoff coûte \(r^{-1}U\) dans le col; ce terme est critique.
- Les constantes de Barker–Prange dépendent fortement de la borne Type I \(M\)
  et leurs rayons sont liés au temps restant avant \(T^\*\).

### Notions de solution

- Les théorèmes de profils sont fonctionnels; ils ne créent pas une solution
  NS et ne préservent pas automatiquement l'identité curl après localisation.
- Barker–Prange travaillent avec des solutions adaptées/d'énergie finie et une
  dynamique NS réelle; leur conclusion ne s'applique pas à un profil statique
  arbitraire.
- Une concentration d'enstrophie \(L^2\) n'est pas une borne
  \(L^{3/2,\infty}\), et inversement.

### Statut des résultats négatifs

- Le contre-exemple disjoint est un résultat exact contre la sélection de masse
  issue de la seule quasi-norme.
- L'échec de l'hypothèse abstraite de Bahouri–Cohen–Koch au même indice
  secondaire est sourcé.
- L'impossibilité de **toute** décomposition faible-endpoint n'est pas prouvée
  par cette source et ne doit pas être enregistrée comme théorème.
- Aucun contre-exemple curl-compatible au ratio « même cellule » n'est encore
  fourni par cette revue.

## 10. Expérience décisive recommandée

Écarter pour le prochain cycle une nouvelle tentative de décomposition de
profils dans le seul faible-Lorentz. Tester directement si la contrainte curl
répare ou non l'échec scalaire :

1. construire \(N\) cellules pure-swirl, lisses, divergence-free, largement
   séparées axialement, avec rayons et amplitudes paramétrés;
2. calculer \(W_N=\operatorname{curl}U_N\) exactement, y compris les couches de
   raccord;
3. mesurer par maximisation certifiée sur les niveaux les quasi-normes globales
   \(K_3(U_N)\), \(K_{3/2}(W_N)\) et leurs versions sur chaque cellule dilatée;
4. borner analytiquement les queues croisées de Biot–Savart;
5. chercher soit

\[
\sup_j\frac{K_{3,Q_j}(U_N)}
{K_{3/2,cQ_j}(W_N)}\longrightarrow0
\]

sous gates globales fixées, soit une inégalité de packing empêchant cette
limite.

Le premier résultat réfuterait la sélection uniforme dans la classe
curl-compatible testée. Le second isolerait le vrai lemme à démontrer.

Une voie positive doit ajouter explicitement une hypothèse qui paie le défaut
de localisation, par exemple un contrôle de packing/Carleson des cols

\[
\sum_j
\|\nabla\chi_j\times U\|_{L^{3/2,\infty}}^{3/2}
\le C K_W^{3/2},
\]

ou un indice secondaire Lorentz strictement meilleur. Cette inégalité est ici
une **candidate falsifiable**, non un résultat de la littérature.

## Conclusion opérationnelle

Le sous-problème ne se réduit pas à « appliquer concentration-compacité ».
Les outils publiés expliquent exactement quelle coercivité manque :
une borne source plus forte, un indice secondaire strict, une information
dynamique de singularité ou un contrôle du champ harmonique/de bord.

Décision bibliographique recommandée : **RÉVISER** le lemme de sélection pour
y faire apparaître l'un de ces couplages, et lancer d'abord le test
multi-cellule curl-compatible. La seule algèbre faible-Lorentz et le
Biot–Savart global ne ferment pas le maillon « même cellule ».
