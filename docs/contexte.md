# Contexte de Millennium Forge

## Objet

Millennium Forge centralise, sous Git et de manière ouverte, les sources, graphes de dépendances, expériences reproductibles, résultats négatifs et formalisations liés aux six problèmes du millénaire encore ouverts :

1. P versus NP ;
2. hypothèse de Riemann ;
3. existence de Yang–Mills et gap de masse ;
4. existence et régularité de Navier–Stokes ;
5. conjecture de Hodge ;
6. conjecture de Birch et Swinnerton-Dyer.

Le dépôt GitHub public cible est `santl0/millennium-forge`. `main` contient uniquement des éléments relus et reproductibles. Les explorations utilisent des branches `codex/millennium-forge/*` et des pull requests en brouillon.

## Positionnement

Le projet complète les formulations Lean existantes et les corpus de conjectures formelles ; il ne prétend pas les remplacer. Sa valeur propre est la couche de recherche : registre des affirmations, provenance, graphes de preuve, expériences, contradictions et reprise autonome par agents.

## Principe de sûreté scientifique

Une ressemblance, un calcul numérique ou une preuve générée par IA ne change jamais seul le statut d'une affirmation. Les conclusions canoniques doivent rester proportionnées à la meilleure preuve effectivement disponible.

## État Navier–Stokes au cycle 0023

Le programme actif a reproduit conditionnellement la chaîne fonctionnelle et
l'endgame `(8)->(58)` de `arXiv:2607.08866v2`, avec corrections des temps,
seuils, constantes, semi-normes et queues. Cette synthèse reste
`COMPUTATION_ONLY` et suppose une vorticité critique ainsi qu'une direction
globale `bmo_phi`; elle n'est pas une résolution Clay.

Le cycle 0020 réfute le raccord universel depuis une cohérence seulement
composante par composante : deux cœurs antipodaux imposent le coût optimal
`4ab/(a+b)` et une divergence logarithmique lorsque leurs fractions restent
fixes à petite échelle. La solution nulle montre aussi que la direction n'est
pas intrinsèque sans convention aux zéros. Le verrou actif est désormais
l'admissibilité PDE complète du profil critique ponctuel supposé en amont.

Le cycle 0021 ferme négativement la sous-classe vectorielle exactement
récurrente. Un profil critique homogène doit satisfaire une porte sphérique de
divergence et de flux; un exemple explicite montre que magnitude `r^-2`,
faible-`L^(3/2)`, divergence et Biot–Savart peuvent coexister tandis que la
direction échoue dans log-BMO. Plus généralement, log-BMO rigidifie toute
direction récurrente par dilatation en une constante, ensuite incompatible
avec une vorticité solénoïdale globale faible-Lorentz non nulle.

La coupure ne fournit pas d'échappatoire perturbative : son défaut de
divergence est invariant d'échelle et son correcteur reste critique. Le verrou
actif devient un profil non récurrent dont la direction se rectifie seulement
comme `1/|log r|`, avec pression et résidu PDE suivis.

Le cycle 0022 ferme négativement cette rectification lorsqu'elle vise un axe
fixe, que l'amplitude critique est uniformément bornée et que chaque bloc
logarithmique conserve une masse `L^(3/2)` non dégénérée. Le premier
harmonique sphérique impose alors une dérive monotone impossible à un moment
borné. Une construction exacte montre la frontière : la direction peut se
rectifier comme `1/|log r|`, mais seulement ici en perdant la masse critique
comme `e^-2s s²`.

La veille primaire ajoute que le confinement uniforme espace-temps de toute
forte vorticité autour d'un axe fixe tombe déjà, conditionnellement, sous le
critère de double cône de Lei–Ren–Tian v1. Le verrou actif devient donc un axe
errant, une cascade angulaire ou plusieurs cœurs échappant à tout cône fixe,
avec le coût de recharge du moment et le résidu visqueux suivis.

Le cycle 0023 quantifie ce coût pour un axe mobile. La recharge du premier
harmonique est au plus `(M/2)Var(e)`, tandis que la masse critique par blocs
impose une dépense linéaire. Une sélection d'axe à variation et erreur
pondérée sublinéaires est donc impossible. La rotation uniforme possède le
budget de variation mais échoue au taux log-BMO déjà sur les boules centrées;
la phase `beta log(1+s)` possède le taux d'oscillation mais seulement une
variation logarithmique.

Cette conclusion reste cinématique et `COMPUTATION_ONLY`. Log-BMO ne produit
pas automatiquement un axe unitaire : les moyennes actives peuvent s'annuler
ou refléter plusieurs phases. Le pivot actif est
`GAP-MULTICORE-ANGULAR-CASCADE`, avec occupation angulaire, divergence,
Biot–Savart et résidu visqueux à suivre.

Le cycle 0024 corrige et précise ce point. Une **même extension globalement
unitaire** à petite oscillation a nécessairement des moyennes proches de la
sphère; mais sa valeur sur `{omega=0}` n'est pas intrinsèque et aucune source
primaire inspectée ne fournit cette extension. Plus généralement, si
`Phi<=M` et chaque bloc porte une masse critique, la fraction active est
uniforme et même une extension seulement bornée fournit un axe. Sa variation
et son erreur pondérée sont `O(log N)`, en contradiction avec le budget
linéaire du cycle 0023. Le contre-profil sparse `a_n=n^-3`, `Phi_n=n²` montre
que faible-`L^(3/2)` seul ne remplace pas `Phi<=M`. Le verrou actif est
`GAP-UNBOUNDED-ANGULAR-INTERMITTENCY`.

Le cycle 0025 construit cette intermittence sous forme d'un train de blobs
critiques. Le champ satisfait exactement divergence, curl, énergie finie,
`L¹ intersection L^(3/2,infinity)`, masse par bloc et Biot–Savart; son
amplitude angulaire croît comme `n²`. L'oscillation de la direction par zéro
est `O(n^-3)` sur les boules centrées en l'origine, mais toute extension voit
une oscillation fixe sur des boules internes de rayon `ell_n/2`. Le motif
répété échoue donc au log-BMO global. Son résidu stationnaire n'est pas un
gradient et garde un coût critique. Le verrou actif devient
`GAP-DIRECTIONALLY-FLAT-INTERMITTENCY` : aplatir la direction interne tout en
compensant l'intégrale nulle d'un curl compact.

La veille corrige simultanément l'ancien accent sur les valeurs exactement
aux zéros : à temps positif régulier non trivial, l'analyticité spatiale rend
le lieu nodal de la vorticité nul en mesure. Les conventions ponctuelles y
sont équivalentes en BMO; la phase au voisinage des zéros et les superniveaux
de mesure intermédiaire restent les objets pertinents.

Le cycle 0026 ferme le premier maillon du blob directionnellement plat sous
une forme quantitative. Si `K` est la quasi-norme faible-`L^(3/2)`, si le
champ a moyenne vectorielle nulle et si une masse `m` se trouve dans un cône
d'ouverture `alpha`, toute extension de la direction vérifie
`MO_D>=2alpha^3m^3/(27K^3|D|)`. Cette borne, renforcée par la passe adverse
qui conserve la projection négative pondérée, est critique par changement
d'échelle et son exposant cubique est optimal dans la classe mesurable.

La passe adverse empêche cependant d'en faire une exclusion générale : un
compensateur de fraction `n^-3` et d'amplitude `n²` garde une masse critique
forte d'ordre un tout en faisant décroître la masse conique comme `1/n`.
Une séparation par interface conserve en revanche une oscillation locale
égale à un, tandis qu'un corridor de zéros peut réduire ce coût à l'ordre
`1/log(R/h)`. Un lift exactement collinéaire ne peut pas être à la fois non
nul, compact et divergence-free. Le verrou actif est donc
`GAP-NESTED-RETURN-FLOW-CASCADE` : lever ce modèle par un potentiel
axisymétrique, quantifier les composantes transverses et distribuer la rotation
sur une cascade interne compatible avec toutes les boules BMO, avant tout
calcul de pression ou d'évolution.

Le cycle 0027 réalise ce lift. Un swirl compact séparable conserve exactement
divergence, moyenne nulle, faible-`L^(3/2)`, masse critique et énergie finie.
Une calotte d'aspect fixé contient toutefois une boule active de direction
`e_r` avec `MO>=3w/[2048(R+w)]`; la concentration isotrope ne réduit pas ce
coût. Le résidu stationnaire possède aussi une composante azimutale non
gradient.

Une variante aux calottes de largeur `n^-3` montre en parallèle que
`MO_D~n^-3` sur un domaine parent et que l'exposant cubique reste optimal même
pour des curls compacts lisses. Cette moyenne parentale n'est pas le BMO
all-ball, et la vitesse de la variante `C_c^infinity` satisfait
`||U||_3->0`. Le verrou devient `GAP-NONSEPARABLE-RETURN-FLOW-MASKING` : une
somme de couches doit masquer successivement les retours radiaux sans créer
une région de capacité polynomiale où la direction transverse domine.

Le cycle 0028 montre qu'un tore azimutal mince contourne ce retour radial :
il est divergence-free, de moyenne nulle, critique en `L^(3/2,infinity)` et
sa direction admet une extension statique log-BMO uniforme. La passe
indépendante confirme `||u||_3^3<=C[(h/R)+(h/R)^2]`; la vitesse critique
s'annule. Sur `R^3`, le profil porte une impulsion non nulle, une queue
non-Schwartz et appartient à la classe sans swirl globalement régulière.

La diffusion fournit un second rejet : pour un anneau unisigné sans swirl,
la direction `e_theta` devient active arbitrairement près de l'axe à temps
positif et son oscillation sur une boule axiale vaut un. Le corridor statique
n'est pas une propriété propagée. Le verrou actif est maintenant
`GAP-MOMENT-CORRECTED-TOROIDAL-CASCADE` : annuler les moments, conserver une
vitesse `L^3` non dégénérée, quitter la classe régulière connue et réauditer
toutes les boules.

Le cycle 0029 annule exactement l'impulsion par une paire de tores signés et
transversalement déplacés. Les corridors restent disjoints et l'axisymétrie
globale est brisée, mais un second multipôle produit une queue `|x|^-4` sur
`R^3`. Plus décisif, Stokes et le potentiel tubulaire ferment l'échelle

```text
||u||_3^3~K^3h/R ->0.
```

La correction d'un nombre fini de moments et tout cardinal fixé sont donc
abandonnés. Le verrou actif devient `GAP-MANY-TORUS-CRITICAL-ACCUMULATION` :
un cardinal croissant doit surmonter simultanément la normalisation
faible-Lorentz, le packing, les annulations de moments et la cohérence non
locale des vitesses. Une seconde voie part directement d'une vitesse compacte
divergence-free pour imposer Schwartz avant d'auditer sa vorticité.

Le cycle 0030 ferme également la branche homogène à cardinal croissant sous
packing local. La décomposition proche/lointaine donne sur `R^3`

```text
||BS[omega]||_3^3
 <= C K^3[h/mathcal L+(h/q)^(4/3)],
```

et ajoute `CK^3S` sur `T^3`. La famille dyadique à cardinal explosif fait
diverger la somme triangulaire mais tous ces termes tendent vers zéro. Le
résultat reste statique, à paramètres communs, et `COMPUTATION_ONLY`.

La voie compacte est immédiatement resserrée. Des copies super-géométriques
de vitesses compactes divergence-free vérifient exactement
`BS[curl U_N]=U_N`; elles peuvent garder `L^3` fort non nul tout en devenant
petites dans faible-`L^3`, ou garder les deux endpoints faibles bornés sans
contrôler la direction. Toute oscillation active du bloc est amplifiée par le
poids `|log r_j|` et le temps diffusif tend vers zéro.

Après trois stratégies tubulaires réellement différentes, la branche des
tores homogènes est abandonnée. Le verrou actif est
`GAP-COMPACT-VELOCITY-WEAK-CRITICAL-DIRECTION` : construire ou exclure un curl
compact intérieurement plat, hors petite donnée faible-`L^3`, avec temps
d'interaction uniforme. Le corpus primaire compte désormais 127 sources.

Le cycle 0031 construit ensuite un swirl compact séparable et suit exactement
les deux dérivées méridiennes. Les gates critiques forcent ses deux largeurs à
rester comparables au grand rayon; le grand rapport d'aspect ne fournit donc
aucun bloc directionnellement plat non perturbatif. Le verrou est déplacé vers
les superpositions non séparables.

Le cycle 0032 ferme plus largement toute superposition pure-swirl dont l'aire
méridienne est `o(R^2)`. Le weak HLS bidimensionnel et l'inclusion de support
fini donnent
`K_U<=C(S_2/R^2)^(1/6)K_W`, indépendamment des couches. Un certificat exact à
384 masques exécute 272 726 assertions sans échec; trois passes séparées
attaquent l'analyse fonctionnelle, les contre-profils et la littérature. Le
corpus compte 135 sources. Le verrou actif est désormais la direction du
gradient sur une section épaisse, avant toute dynamique.

Au checkpoint 0032, le remote GitHub ne possédait aucune branche de base. Le
premier push autorisé de
`codex/millennium-forge/navier-stokes-state-of-art` l'a donc fait devenir la
branche par défaut distante. La branche `main` reste uniquement locale et
intacte; aucune pull request ne peut être ouverte tant qu'une base distante
distincte n'est pas publiée par le socle. Aucun historique n'a été réécrit.

Le cycle 0033 remplace le test topologique brut par une troncature quantitative.
Pour tout swirl pur dont le support axial tient dans `O(R)`, weak HLS et coaire
produisent une masse `L1` du curl tronqué; son annulation vectorielle et le
lemme conique du cycle 0026 forcent
`MO_B>=c(K_u/K_w)^6` sur une boule de rayon `O(R)`. Les deux endpoints rendent
donc le log-BMO non uniforme sous concentration, y compris pour les plateaux
épais et les compensateurs rares. Le prochain verrou porte sur des cellules
axialement dispersées et hétérogènes, avant toute sortie du swirl pur.

Le cycle 0034 réfute le pigeonhole fondé sur les seules quasi-normes : des
niveaux de curl échelonnés gardent le rapport global non nul tout en faisant
tendre tous les rapports locaux vers zéro. La fermeture compacte rétablit la
sélection si chaque cellule possède un plateau effectif, une boîte comparable
et le registre BV `integral|W_j|>=cA_jv_j^(2/3)`. Une cellule a alors un
rapport local `>=c(K_u/K_w)^2`, puis une oscillation directionnelle
`>=c(K_u/K_w)^12`. Le prochain verrou est la dégénérescence des boîtes, le
chevauchement des curls et la sélection dynamique d'une échelle tendant vers
zéro.

Le cycle 0035 montre que le volume de boîte du cycle 0034 est évitable dans
la géométrie pure-swirl exacte. Un halo de volume fixé par un témoin `v_j` est
d'abord réfuté par dilatation critique. La réparation choisit au niveau global
`lambda` la bande `lambda/4<+/-F_j<lambda/2`; coaire R3, isopérimétrie et
faible-Lorentz donnent une cellule avec rapport local
`>=(C_I/324)(K_u/K_w)^2`, sans borne axiale, volume support ou plateau
uniforme. Le volume actif est contrôlé mais son diamètre ne l'est pas. Le
verrou devient `GAP-ACTIVE-HALO-DIAMETER-OR-OVERLAP`, d'abord sur une cellule
à gouttelettes dispersées.

Le cycle 0036 décompose ce superniveau inférieur en composantes connexes et
tronque séparément à `lambda/4`. La trace nulle supprime tout curl de bord;
coaire par composante et faible-Lorentz sélectionnent une goutte avec
constante `C_I/648`. Si son diamètre axial est `O(R_j)`, l'interface
lipschitzienne du gate 0033 donne une oscillation directionnelle de puissance
douze. Les filaments strictement sous le seuil et les copies identiques sont
fermés. Un pont mince restant au-dessus du seuil peut encore fusionner deux
gouttes éloignées; `GAP-ABOVE-THRESHOLD-THIN-BRIDGE` devient actif. Le corpus
compte 162 sources.

Le cycle 0037 montre qu'un pont au-dessus du cutoff n'est pas gratuit dans la
section méridienne. Le périmètre d'une composante M-indécomposable contrôle
deux fois son diamètre essentiel; coaire et le poids exact du curl donnent
`a(b-a)RD<=9K_uK_w/(8pi)`. Un pont au-dessus de `A` vérifie donc
`A^2RD<=9K_uK_w/(2pi)`, même si son excès tend vers zéro. Sous
`AR>=kappa K_u`, son diamètre est uniforme et le gate directionnel se raccorde
conditionnellement. Le niveau global ne fournit toutefois pas ce calibrage
pour chaque goutte, et une fusion tardive peut ne persister que sur une bande
évanescente. Le prochain verrou est
`GAP-BRIDGE-SCALE-CALIBRATION-OR-MERGE-TREE`. Le corpus compte 167 sources.

Le cycle 0038 évite finalement l'arbre de fusion. Le volume des cores et la
largeur radiale calibrent directement le niveau presque optimal par
`lambda R>=K^2/(432H)`. Une moyenne de coaire choisit un niveau régulier où la
somme des diamètres est `O((H/K)^3R)`; au même niveau, isopérimétrie et Lorentz
sélectionnent une composante avec rapport endpoint quadratique. Composé avec
la sélection cellulaire 0035, le diamètre statique disjoint est fermé sans
hypothèse locale. Deux contre-ledgers réfutent l'héritage récursif et l'arbre
topologique seul. Le corpus compte 171 sources et le verrou devient
`GAP-OVERLAPPING-CURL-CANCELLATION`.

Le cycle 0039 ferme ce verrou négativement pour les sommants étiquetés. Deux
champs lisses pure-swirl de multiplicité deux, `B+Z_n` et `-Z_n`, ont des
rapports locaux `O(n^-1)` alors que leur total reste le fond fixe `B`. La
multiplicité ne contrôle donc pas les annulations de curls; le claim universel
est `REFUTED`. Un ledger principal vérifie 344 121 assertions rationnelles et
un second 1 216, tous deux à résidu nul. Dans la sous-classe même axe–même
anneau, l'agrégation du potentiel total rétablit cependant exactement le cycle
0038. La veille porte le corpus à 175 sources, exclut une base dénombrable du
plein faible-Lorentz et classe l'annonce forcée `arXiv:2608.11553v1` hors du
problème Clay. Le verrou actif est
`GAP-MULTIAXIS-TOTAL-FIELD-LOCALIZATION`.

Le cycle 0040 ferme la partie statique solénoïdale de ce verrou. Pour une
couronne homothétique fixe, le correcteur de Bogovskiĭ appliqué à
`grad chi_R dot U` produit un champ compact divergence-free égal au champ
total dans le core, avec toutes les constantes critiques suivies. Un plateau
lisse montre que le coût du col ne décroît pas avec `R`; une couronne mince
coûte au moins `c_pR/h` dans les espaces forts. Les deux claims internes sont
`NS-SOLENOIDAL-ANNULAR-CUTOFF` et
`NS-THIN-ANNULUS-DIVERGENCE-COST`.

Après absorption par Biot–Savart faible HLS, le seul facteur statique non
contrôlé est `K_core/K_global`. Le nouveau verrou est
`GAP-WEAK-L3-CORE-CAPTURE-AT-PRESINGULAR-SCALE` : le rayon doit appartenir à
une gamme dictée par la concentration et tendre vers zéro. Sans cette
contrainte, une boule assez grande capture trivialement tout champ compact.
Pression, temps et équation du champ localisé restent ouverts. Le corpus
primaire compte 179 sources.

Le cycle 0041 réaudite le raccord Type I au lieu de reconstruire une capture
statique. Barker–Prange 2020, théorème 2 et appendice B, concentre le
faible-`L3` au premier point singulier sur un rayon parabolique. L'inclusion
exacte
`integral_E|u|^2<=3K_3(u)^2|E|^(1/3)` transforme la borne globale pointwise
`K_3(u(t))<=M` en leur hypothèse Morrey avec
`C_M=sqrt(3)(4pi/3)^(1/6)`. On obtient pour tout `0<t<T_*` la fraction
`K_core/K_global>gamma_w/M` au rayon
`2sqrt((T_*-t)/S_w^*(C_MM))`.

La constante trois est optimale et certifiée sur 1 346 assertions exactes.
Deux paquets disjoints réfutent toute fraction sans borne globale. La veille
2025–2026 n'ajoute aucune source et confirme la dégénérescence Type II. Le
cutoff du cycle 0040 est en outre valable pour un champ seulement lisse au
voisinage de `Bbar(x0,2R)`, puisque `chi_RU` est compact; seul son corollaire
Biot–Savart exige des données globales.

Le verrou actif est désormais `GAP-TYPE-I-LOCALIZED-EVOLUTION` : calculer
l'équation exacte du cutoff mobile, sa pression et sa force. Le verrou
`GAP-TYPE-II-RELATIVE-CORE-CAPTURE` reste séparé. Aucun résultat du cycle ne
prouve ni blow-up ni régularité globale Clay.

Le cycle 0042 calcule l'équation jusque-là manquante. La conjugaison
homothétique de l'opérateur de Bogovskii montre que sa dérivée temporelle
contient un commutateur avec le générateur de dilatation. Pour
`R=2sqrt((T_*-t)/S_w^*(C_MM))`, le coefficient renormalisé
`kappa=-RR'=2/S_w^*(C_MM)` est constant dans le temps mais dépend de `M`.

Le champ `V=chi_Ru-B_R(nabla chi_R dot u)` satisfait une équation forcée
exacte avec pression locale `chi_Rp` et force annulaire `R^-3F`. La forme
projetée est solénoïdale mais non locale. Un témoin pure-swirl lisse annule le
correcteur tout en gardant un coût de frontière mobile non nul et une norme
`L1` constante; 499 assertions rationnelles certifient l'horloge, les jets et
les normes. Le rétrécissement du support ne fournit donc aucune petitesse.

Deux verrous remplacent `GAP-TYPE-I-LOCALIZED-EVOLUTION` :
`GAP-TYPE-I-MOVING-COMMUTATOR-BOUND`, puis
`GAP-TYPE-I-FORCED-RIGIDITY`. La borne Type I contrôle les termes d'ordre
zéro mais pas encore les commutateurs de diffusion/dilatation dans un espace
négatif critique. Aucune annulation de la force complète, compacité forte ou
rigidité ancienne n'est revendiquée. La veille ajoute cinq sources primaires
sur domaines mobiles, pression locale et blow-up forcé; le corpus atteint 184
sources sans théorème couvrant le collapse parabolique.

Le cycle 0043 fixe une réalisation exacte et pseudodifférentielle d'ordre
`-1` de l'inverse de divergence. Le commutateur mobile et les termes de
pression/non-linéarité se regroupent alors dans l'espace invariant
`X=L1+div L^(3/2,infinity)`, avec borne
`C[M²+(1+|kappa|)M]`. Le mode haute fréquence croît comme `N` dans une norme
positive mais garde un budget `X` uniforme; 222 assertions exactes ferment
ce faux contre-test. Le corpus atteint 185 sources.

`GAP-TYPE-I-MOVING-COMMUTATOR-BOUND` est fermé pour l'opérateur fixé. Le
verrou actif devient `GAP-TYPE-I-FORCE-COMPACTNESS`, suivi de la rigidité
forcée. Aucune petitesse, convergence forte ou régularité Clay n'est obtenue.

Le cycle 0044 dilate la transition à la couronne
`A_L={L<|y|<2L}` sans modifier la capture dans `B_1`. Sur tout compact, les
commutateurs et `Q_LH-H` s'annulent exactement; la seule contribution est la
queue de Leray du tenseur `Z_L tensor Z_L-U tensor U`, nul dans `B_L`. Son
noyau d'ordre quatre donne
`||partial^alpha F_L||_infinity<=C M²L^(-3-|alpha|)`.

Le gain est strictement local. Un pure-swirl critique à l'échelle `L` donne
pour la force complète
`F_L=L^-3B_0(dot/L)+kappa L^-1A(dot/L)` et donc
`||F_L||_X>=c|kappa|L²-C`. La convergence globale dans `X` est réfutée.
Le certificat dyadique porte 253 assertions exactes.

Le verrou actif devient `GAP-TYPE-I-LOCAL-COMPACTNESS-TRACE` : compacité
forte locale, passage de l'énergie et trace non triviale sur une diagonale
`L_j->infinity`, `L_jR_j->0`. La dérenormalisation puis la rigidité ancienne
faible-`L3` restent séparées; aucun résultat Clay n'est obtenu.

Le cycle 0045 ferme la partie compacité de ce verrou. La borne faible-`L3`,
la pression de Riesz locale `L^(4/3)` et l'équation lisse permettent un test
de Caccioppoli avec absorption puis remplissage des trous. On obtient
uniformément `L-infinity_tL2_x,loc inter L2_tH1_x,loc`. Simon et
l'interpolation parabolique donnent forte `L3_loc`; le produit et
l'inégalité d'énergie locale passent après décomposition de la pression en
partie proche et harmonique.

La limite est faible adaptée pour l'équation renormalisée non forcée, mais
sa trace peut encore être nulle. `FAIL-NS-0081` sépare compacité volumique et
trace critique. Le verrou actif devient
`GAP-TYPE-I-CRITICAL-TRACE-PERSISTENCE` : construire un moment signé contre
un test fixe, ou une compacité forte de trace, avant toute dérenormalisation
et rigidité ancienne. Le corpus compte 188 sources.
