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
