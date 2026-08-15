# État de l'art vérifié — Navier–Stokes incompressible 3D

Instantané bibliographique : 2026-08-14. Une entrée `SOURCE_VERIFIED` signifie
que l'énoncé a été comparé à une source primaire ; elle ne transforme pas une
prépublication récente en théorème accepté. La formulation cible est fixée dans
[`FORMULATION_CLAY.md`](FORMULATION_CLAY.md) et les métadonnées détaillées sont
dans [`sources.json`](../../literature/navier-stokes/sources.json).

## État du problème

Le Clay Mathematics Institute continue de classer le problème parmi les
problèmes du millénaire non résolus. Aucun article publié et vérifié dans cette
veille ne démontre la régularité globale pour toute donnée lisse admissible, ni
ne construit un breakdown admissible de (C) ou (D). Le verrou n'est pas
l'existence faible : c'est le passage, uniforme en échelle, de l'énergie
supercritique à une quantité critique qui exclut une concentration en temps
fini.

## Carte des résultats établis

| Bloc | Équation, domaine, solution | Résultat utile | Limite exacte pour Clay |
|---|---|---|---|
| Leray 1934 | NS incompressible visqueux, `R^3`; solution faible d'énergie | existence globale faible et inégalité d'énergie | ni unicité ni lissité globale |
| Hopf 1951 | NS visqueux, domaines avec bord; solution faible | construction faible d'énergie | le domaine et la notion de solution diffèrent de Clay |
| Caffarelli–Kohn–Nirenberg 1982 | NS 3D, solution faible adaptée | l'ensemble singulier a mesure parabolique unidimensionnelle nulle | « petit » n'est pas « vide » |
| Prodi–Serrin–Ladyzhenskaya | solution faible/forte selon les versions | régularité si `u in L_t^p L_x^q`, `2/p+3/q<=1`, `q>3` | hypothèse critique non fournie par l'énergie |
| Escauriaza–Seregin–Šverák 2003 | NS 3D, endpoint spatial | une borne `L_t^infinity L_x^3` jusqu'au temps candidat exclut le blow-up | cette borne critique globale reste à démontrer |
| Koch–Tataru 2001 | mild NS sur `R^3` | bonne position globale pour petite donnée dans `BMO^(-1)` | petitesse; ne couvre pas toute donnée Clay |
| Gallagher–Koch–Planchon | mild NS critique sur `R^3` | décomposition en profils et élément minimal conditionnel dans des cadres critiques | la rigidité finale exige encore une propriété critique bornée ou compacte |
| Nečas–Růžička–Šverák 1996 | profil rétrograde auto-similaire, `R^3` | exclusion des profils non triviaux sous intégrabilité `L^3` | n'exclut ni Type II, ni multi-échelles, ni auto-similarité discrète générale |
| Koch–Nadirashvili–Seregin–Šverák 2009 | solutions anciennes à vitesse bornée, faibles ou mild selon le résultat | théorèmes de Liouville en classes particulières, notamment axisymétriques | sans mildness, les solutions parasites `u=b(t)`, `p=-b'(t)·x` subsistent; le Liouville général 3D mild borné reste hors de portée |
| Lei–Yang–Yuan 2024 | deux solutions mild bornées sur `R³ x [0,T]`, vorticités bornées | unicité à même donnée finale bornée, y compris non nulle | ne produit ni donnée finale ni classe limite depuis un blow-up; la route est seulement corroborante dans ce dépôt |
| Pineau–Vicol 2026, prépublication v2 | profils backward RSS/DSS/RDSS sur `R³`, borne Type I | exclusions quantitatives pour rotations petites ou grandes et critères locaux quasi-auto-similaires | rotation intermédiaire et Type II non couverts; aucune exclusion générale de blow-up |
| Constantin–Fefferman 1993 | vorticité d'une solution lisse | régularité conditionnelle sous cohérence géométrique de la direction de vorticité | l'alignement requis n'est pas une conséquence de l'énergie |
| axisymétrie sans swirl | NS 3D réduit | régularité globale classique dans cette classe | le swirl restaure l'étirement critique |

### Existence faible, énergie et supercriticité

Pour `f=0`, une solution de Leray–Hopf satisfait

```text
||u(t)||_2^2 + 2 nu integral_0^t ||nabla u||_2^2 <= ||u_0||_2^2.
```

Sous `u_lambda(x,t)=lambda u(lambda x,lambda^2t)`, l'énergie cinétique est
multipliée par `lambda^(-1)`. Elle permet donc davantage de concentration
relative aux petites échelles. Les constructions de Galerkin donnent une
compacité faible compatible avec l'existence, mais pas le contrôle critique ni
l'égalité locale suffisants pour éliminer tout défaut de concentration.

### Régularité partielle et solutions adaptées

Une solution faible adaptée satisfait une inégalité d'énergie locale incluant
la pression. Caffarelli–Kohn–Nirenberg réduit fortement la taille possible de
l'ensemble singulier. Le raccord manquant est qualitatif : aucune estimation
connue issue de l'énergie seule ne force cet ensemble à être vide. Les critères
`epsilon`-régularité sont locaux et invariants d'échelle, mais leur hypothèse de
petitesse peut se déplacer vers des cylindres de plus en plus fins.

### Critères critiques de prolongement

Les critères de Prodi–Serrin–Ladyzhenskaya sont invariants lorsque
`2/p+3/q=1`; l'endpoint `L_t^infinity L_x^3` est couvert par
Escauriaza–Seregin–Šverák. Des variantes emploient la vorticité, la pression ou
des espaces de Besov. Elles sont des implications conditionnelles : les
remplacer par une majoration a priori de cette même norme sans constante
uniforme serait circulaire.

`BMO^(-1)` est critique et plus large que plusieurs espaces classiques, mais le
théorème de Koch–Tataru repose sur la petitesse dans un espace de type Carleson.
L'invariance d'échelle d'une norme ne fournit ni coercivité, ni signe, ni
monotonie.

### Compacité–rigidité, solutions anciennes et profils

Une séquence de solutions remise à l'échelle près d'un premier temps singulier
peut, sous des bornes critiques assez fortes, produire une solution ancienne
non triviale. La chaîne comporte trois passages fragiles : compacité forte du
terme quadratique, contrôle non local de la pression, puis théorème de
Liouville dans la classe limite. L'exclusion des profils exactement
auto-similaires ne ferme que cette sous-classe.

La notion de solution limite est décisive. Une solution ancienne localement
adaptée, même lisse et à vitesse bornée, peut être parasite :
`u(x,t)=b(t)`, `p(x,t)=-b'(t)·x`. La pression affine est localement admissible
mais échappe à la jauge de Riesz/BMO, et la formule mild impose au contraire que
`b` soit constante. Ainsi, une rigidité portant seulement sur « ancienne,
adaptée, à vitesse bornée et de trace terminale nulle » est fausse; une
extraction de blow-up utile doit transmettre explicitement la mildness ou une
normalisation globale équivalente de la pression.

L'extraction détaillée ESS/GKP précise toutefois que la pression **lointaine
centrée** n'est pas un verrou supplémentaire lorsque la suite est globalement
bornée dans `L³` : Hölder donne une queue pondérée `O(A^-3)`. En revanche,
l'énergie seule n'assure pas cette tension après zoom, et cette estimation ne
donne aucune compacité forte pour la pression proche.

Le cycle 0008 ferme une porte de rigidité plus précise. Si une **même** solution
ancienne mild au sens KNSS est globalement bornée et possède une vraie limite
nulle dans `D'` au temps terminal, les estimations redémarrées de KNSS donnent
des bornes uniformes sur toutes ses dérivées; la vorticité a alors une trace
terminale classique nulle et l'unicité rétrograde ESS l'annule sur chaque bande
finie. Le champ restant est harmonique borné, donc spatialement constant, et la
mildness puis la trace l'annulent. Cette dérivation du laboratoire reste
`COMPUTATION_ONLY`, sans revue externe. Elle ne se transfère pas encore au
problème Clay : ESS transmet la trace sans la borne ponctuelle/mildness, tandis
que KNSS transmet mildness et bornitude avec la normalisation opposée
`|v(0,0)|=1`.

Le cycle 0009 ferme négativement le raccord maximum-normalisé lui-même. Pour
les temps records KNSS, les estimations paraboliques uniformes donnent une
compacité `C^m_local` jusqu'au temps redimensionné zéro : la limite des zooms
et la limite temporelle commutent déjà, et leur valeur commune conserve la
normalisation ponctuelle non nulle. Mais `s=0` est le temps-record physique
`t_k`, non le temps maximal `T`; ce dernier est l'extrémité future mobile
`B_k=M_k²(T-t_k)`. Une trace physique dans `D'` ne se transfère pas non plus
aux tests `M_k² phi(M_k(x-x_k))`, mobiles et concentrés. Le trou exact est donc
le contrôle de l'extrémité mobile, pas le commutateur au temps-record.

Cette analyse reformule quantitativement une obstruction critique connue : un
blow-up maximum-normalisé force une quantité strictement positive de masse
`L³` dans une boule de rayon comparable à
`||u(t_k)||_infinity^-1`. La disparition uniforme de cette masse sur toutes
les petites boules exclut donc le blow-up, mais ce n'est pas un critère
nouveau : elle implique la condition uniforme à seuil fixe (23) de Constantin
2023, déjà suffisante au prolongement. Elle n'est ni une conséquence de
l'énergie, ni d'une simple borne globale `L³`.

Un scénario Type I conserve une quantité critique de vitesse ou de vorticité à
l'échelle naturelle; un scénario Type II la laisse croître plus vite. Les
résultats Type I et plusieurs résultats au bord ne se transfèrent pas à un Type
II intérieur sans une nouvelle borne ou une nouvelle rigidité. La
prépublication de Seregin `arXiv:2606.29468` exclut certaines limites Type II
sous hypothèses supplémentaires; elle ne résout pas l'alternative Clay.

La veille d'août 2026 ajoute deux réductions Seregin (`arXiv:2402.13229v3` et
`arXiv:2507.08733v2`) : leurs zooms Type II conditionnels font disparaître la
viscosité et produisent des anciennes **Euler**, parfois axisymétriques sans
swirl. Elles ne renforcent donc pas le Liouville Navier–Stokes mild de KNSS.
Wang–Yang (`arXiv:2608.06040v1`) obtient de nouveaux Liouville pour des
`D`-solutions stationnaires sous décroissance cylindrique; cette classe n'est
pas connue pour contenir les limites ESS/KNSS. Binz–Coiculescu
(`arXiv:2607.12159v1`) traite des profils homothétiques forward à donnée
homogène singulière, pas des profils backward généraux.

Pineau–Vicol (`arXiv:2607.09619v2`, révisé le 2026-08-06) exclut des profils
backward rotated self-similar sous borne Type I lorsque la rotation est assez
petite ou assez grande, ainsi que certains régimes DSS/RDSS proches de
l'identité. C'est une exclusion substantielle de profils structurés, mais non
un Liouville pour toute solution ancienne : le régime de rotation intermédiaire
et les scénarios Type II restent hors de ses hypothèses.

### Vorticité, pression, cascade et intermittence

La vorticité vérifie

```text
partial_t omega + u dot nabla omega = omega dot nabla u + nu Delta omega.
```

Le terme d'étirement n'a pas de signe. Les critères d'alignement montrent une
déplétion conditionnelle, pas un alignement universel. La loi de Biot–Savart et
la reconstruction de pression couplent toutes les échelles : tronquer en
fréquence ou localiser en espace produit des commutateurs qu'il faut suivre.

Les flux de cascade et modèles intermittents guident les diagnostics, mais une
loi statistique ou une moyenne d'ensemble ne borne pas automatiquement chaque
solution déterministe. Le contre-profil triadique historique, reproduit dans ce
dépôt, élimine déjà une forme trop forte de déplétion énergétique universelle
par simple divergence nulle et hélicité globale nulle.

### Axisymétrie

Sans swirl, la quantité `omega_theta/r` obéit à une structure de maximum et la
régularité globale est classique. Avec swirl, le terme de production critique
réapparaît. Deux manuscrits de Rishad Shahmurov (`arXiv:2606.07869` pour
l'axisymétrie avec swirl et `arXiv:2605.09797` pour le problème complet)
revendiquent en 2026 des résultats beaucoup plus forts. Ce sont des
prépublications récentes, non validées ici : leurs réductions et constantes
critiques doivent faire l'objet d'une revue indépendante avant tout emploi.

## Non-unicité : ce qu'elle établit et ce qu'elle n'établit pas

| Résultat primaire | Cadre exact | Portée et non-implication |
|---|---|---|
| Buckmaster–Vicol 2019 | NS 3D, solutions faibles de faible régularité | non-unicité faible; pas un blow-up classique ni une non-unicité Leray–Hopf standard |
| Albritton–Brué–Colombo 2022 | NS 3D forcé, deux solutions de Leray, donnée initiale nulle | non-unicité dans un cadre forcé borderline; ne réfute pas (A) ou (B) |
| Hou–Wang–Yang, `arXiv:2509.25116v2` | NS 3D non forcé sur `R^3`, solutions adaptées de Leray–Hopf | la prépublication revendique une infinité de solutions issues d'une même donnée compacte, lisse hors de `0`, dans tout `L^q`, `q<3`, mais singulière à `0`; cette donnée n'est pas admissible par Clay |
| Ionescu–Jia–Palasek, `arXiv:2606.07501v1` | NS 3D non forcé sur `R^3`, profils forward axisymétriques sans swirl | calcul non certifié de profils instables à résidu annoncé `10^-10` et théorème conditionnel vers non-unicité dans `H^alpha∩L^{3,infinity}`, `alpha<1/2`; le profil exact et son mode restent des hypothèses, la donnée reste singulière |
| Cheskidov–Hou, `arXiv:2603.03666v2` | NS standard sur `T^d`, solutions mild singulières dans des Besov d'indice négatif | non-unicité pour données distributionnelles avec `u tensor u` renormalisé et sans `L²_loc` général; le mot « mild » ne raccorde pas cette classe à KNSS ni aux solutions classiques Clay |

Le résultat Hou–Wang–Yang est accompagné d'un calcul par intervalles pour un
profil auto-similaire et un mode instable. Le code public annonce Julia 1.11 et
environ 800 Go de mémoire; au commit `615ee6f`, il ne fournit ni release ni
`Manifest.toml` effectivement épinglé et dépend de candidats `.mat`
pré-calculés. Le calcul n'a pas été reproduit localement. La localisation de la
preuve coupe uniquement la queue à grand rayon : pour `p=4`, le point fixe
gagne `R^-1/8`, mais la donnée compacte conserve `1/|x|` à l'origine. Même si
la preuve prépubliée est correcte, l'implication vers Clay s'arrête à cette
donnée singulière. Régulariser le coeur déclenche l'unicité faible–forte sur
l'intervalle classique et détruit l'invariance auto-similaire exacte. Le cycle
0010 montre en outre que convergence `L²` et borne `L^{3,infinity}` ne donnent
pas la compacité `L³` requise par un raccord perturbatif naïf.

Le cycle 0011 ferme une seconde inférence naïve. Le profil HWY est pair sous
la réflexion axiale vectorielle et le mode instable certifié est impair. Les
cutoffs/convolutions radiaux, la chaleur et la projection de Leray respectent
cette parité : le lissage intérieur symétrique a donc une projection exactement
nulle sur ce mode, et la solution forte locale reste paire. Les artefacts CAP
publics audités exposent le mode droit et des bases de coercivité, mais pas une
fonction propre adjointe dynamique avec normalisation, borne de résolvante et
conditionnement suffisants pour mesurer un lissage asymétrique. Aucun mode
instable pair n'est exclu, et la brisure de symétrie faible après perte de
l'unicité forte reste possible.

Le cycle 0012 ferme la troisième inférence du même raccord. Une trace commune
dans la limite renormalisée `tau→-∞` n'est pas une même donnée de Cauchy à un
temps physique fini. Sur tout intervalle où une solution forte `u` existe et
où `∫||∇u||∞ dt<∞`, la différence `w=v-u` avec une solution de Leray–Hopf de
même donnée vérifie

```text
(1/2)d||w||²L²/dt + ||∇w||²L² <= ||∇u||∞ ||w||²L².
```

La pression disparaît ici seulement dans le pairing global divergence-free;
elle n'est pas devenue locale. Grönwall impose `w=0` jusqu'au temps maximal
fort. Dans le modèle normal exact `b'=ab-b²`, la famille
`b_A=aAe^(a tau)/(a+Ae^(a tau))` a pourtant la même trace nulle à
`tau=-∞`, tandis que l'état à tout temps fini détermine injectivement `A`.
Ainsi, une amplitude instable perdue dans la trace asymptotique ne fournit pas
deux branches depuis une même donnée lisse. Après les échecs indépendants de
compacité critique (0010), de parité (0011) et de donnée de Cauchy (0012), le
raccord HWY est suspendu.

Quatre sources récentes renforcent les barrières de vocabulaire sans fermer
Clay. Cheskidov–Zeng–Zhang (`2503.05692v1`) appellent « dissipatives » des
solutions à énergie continue et décroissante, mais indiquent explicitement
qu'elles ne satisfont pas l'inégalité de Leray–Hopf. Palasek
(`2509.18595v1`) construit une croissance arbitraire de normes pour une
famille de données lisses distinctes, chaque solution étant forte et globale.
Liao–Qin (`2602.12666v1`) calcule une sensibilité chaotique pour un écoulement
de Kolmogorov **2D forcé** depuis des données différentes. Galdi–Gazzola
(`2606.15189v3`) construit au contraire un blow-up rigoureux d'une unique
solution globale de Leray–Hopf avec égalité d'énergie, mais sous une force
extérieure spécialement ajustée. Les alternatives négatives Clay autorisent
une force, mais l'exigent lisse et rapidement décroissante avec ses dérivées;
les forces de cette construction sont seulement dans des classes
d'intégrabilité critiques/surcritiques et portent la singularité temporelle.

## Calculs, IA et preuve assistée par ordinateur

Quatre niveaux sont conservés séparément :

1. indice numérique flottant ;
2. calcul haute précision convergé mais non certifié ;
3. preuve assistée par ordinateur avec réduction analytique compacte et
   arithmétique d'intervalles ;
4. preuve analytique complète.

Les calculs de Hou sur une possible singularité axisymétrique visqueuse (2022–
2023) sont des indices numériques à haute résolution, pas un certificat de
blow-up. Les singularités instables découvertes en 2025 par réseaux de neurones
concernent surtout Euler, Boussinesq, Prandtl ou des géométries avec frontière.
Elles sont inviscides ou hors domaine Clay. La preuve assistée de Chen–Hou pour
Euler/Boussinesq est méthodologiquement transférable (réduction, résidu,
inverse approché, intervalles), mais aucune implication PDE ne transporte son
profil vers NS visqueux `R^3` ou `T^3`.

Le seul maillon immédiatement transférable du programme IA 2025–2026 est donc
méthodologique : produire un problème de point fixe compact, suivre le résidu et
certifier l'inversibilité. Le premier obstacle NS est analytique : dans une
échelle Euler auto-similaire `u=tau^lambda U(x/tau^(1+lambda))`, le rapport
viscosité/inertie est proportionnel à `nu tau^(-1-2lambda)`. Pour les exposants
`lambda>-1/2` proposés dans les scénarios inviscides concernés, la viscosité
domine à l'approche de `tau=0`; le profil Euler ne constitue pas une
approximation perturbative directe de NS.

## Formalisation

La veille des bibliothèques formelles est consignée dans
[`formal/navier-stokes/README.md`](../../formal/navier-stokes/README.md). Le
programme ne revendique aucune formalisation existante du problème Clay. Les
premières cibles stables sont l'identité d'échelle, la projection sur les
champs divergence-free et des identités d'énergie finies; elles ne certifieront
pas une régularité globale par elles-mêmes.

## Verrous irréductibles observés

| Perte | Premier endroit où elle apparaît | Ce qu'il faudrait ajouter |
|---|---|---|
| puissance d'échelle | énergie `L^2` sous zoom | quantité critique coercive ou mécanisme de déplétion démontré |
| dérivée | estimation directe de `u dot nabla u` | structure paraproductive avec sommation uniforme |
| constante uniforme | Galerkin, troncature spectrale, profils | borne indépendante de la dimension et de l'échelle |
| compacité forte | limite d'une séquence critique | exclusion de dichotomie/cascade et contrôle du défaut |
| pression | localisation physique | contrôle des queues et commutateurs de Riesz |
| positivité | flux triadiques et étirement | fonctionnelle de signe stable sous interactions |
| géométrie locale | passage de `xi` au strain total | queue Biot–Savart et quantificateurs uniformes sur tout le high-vorticity set |
| stabilité | passage d'un profil singulier à des données Clay | théorème robuste respectant unicité faible–forte |

## Conclusion falsifiable

La bibliographie ferme de nombreuses classes conditionnelles mais ne fournit
pas l'arête « énergie -> borne critique ». Seize cycles ont déjà éliminé ou
borné plusieurs substituts : transfert inviscide mono-échelle, déplétion
triadique universelle, tension de pression issue de l'énergie, compacité de
traces mobiles, module temporel critique et composition naïve ESS–KNSS. Le
raccord ESS–KNSS maximum-normalisé est suspendu : les deux profils ne sont pas
le même objet, le paquet hybride serait rigide, et la suite KNSS conserve
nécessairement une trace non nulle. Le raccord de la donnée homogène `-1` à
une même donnée Clay lisse est lui aussi suspendu après trois tests négatifs
distincts. Le cycle 0013 ferme ensuite la porte ponctuelle locale : deux champs
analytiques périodiques reliés par translation ont les mêmes quantités
quadratiques et les mêmes modules locaux de direction, mais des stretchings
centraux opposés. Une cohérence choisie dans un seul patch ne contrôle pas la
partie lointaine du strain et ne réfute aucun critère géométrique intégré. Le
verrou actif devient une inégalité avec queue non locale explicite et l'audit
des raccords de `arXiv:2607.08866v2` entre mesure de superniveau, sparseness
linéaire et rayon d'analyticité.

Le cycle 0014 ferme exactement le dernier de ces trois raccords géométriques :
la densité volumique `delta` implique une tranche linéaire
`delta^(1/3)` au même centre et rayon, avec constante un optimale. Pour
`delta=3/4`, une borne globale `|V_s|≤B_s` fournit le rayon sûr
`(B_s/pi)^(1/3)`; ce rayon doit être construit avant d'en démontrer la borne
supérieure logarithmique. La provenance est corrigée : Grujić 2013 porte le
critère 1D et la mesure harmonique, Farhat–Grujić–Leitmeyer 2017 la réduction
volumique à une échelle `rho≤r`, et Grujić–Xu 2019–2024 la formulation au même
rayon. `arXiv:2607.08866` reste une v2 non évaluée; ses estimations (47)–(55),
la queue du commutateur et l'uniformité des constantes ne sont pas validées.

Le cycle 0015 ferme ensuite, après correction, le sous-passage `(47) -> (49)`.
La relation exacte entre distribution et réarrangée est une implication de
pseudo-inverse; l'égalité utilisée informellement au niveau terminal est
fausse sur les plateaux. Avec un cutoff de petit volume uniforme, l'enveloppe
`v^(-1/3) log^(-1)` entraîne une queue
`lambda^(-3) log^(-3)` à seuils et constantes explicites, covariante sous le
scaling Navier–Stokes; la puissance logarithmique est optimale sous cette
seule hypothèse. Ce résultat mesurable ne valide ni l'obtention de (47) depuis
la vorticité, ni une représentation ponctuelle radiale de la vitesse. L'arête
active est désormais `(40) -> (41) -> (47)`, où subsistent la jauge
Biot–Savart, les deux intégrales d'O'Neil, le reste positif de (46) et leur
uniformité temporelle.

Le cycle 0016 ferme conditionnellement le raccord fonctionnel restant
`(40) -> (47)`. Une queue de vorticité
`lambda^(-3/2)log^(-3/2)`, avec seuil uniforme, contrôle global
`L^{3/2,infinity}` et jauge de Hodge fixée, entraîne une enveloppe de vitesse
`v^(-1/3)log^(-1)` à constante explicite et sans perte d'échelle. La source
primaire d'O'Neil confirme les deux opérateurs de (41).

L'audit découvre néanmoins deux défauts locaux dans la v2. Le reste positif de
(46) n'est pas `O(1)` : il diverge comme
`9v^(-1/3)log^(-2)(e/v)`, tout en restant inférieur au terme principal. Sous
la seule hypothèse `u_0∈L∞(R³)`, Biot–Savart détermine aussi la vitesse
seulement modulo une composante harmonique constante; le champ constant non
nul réfute (41) appliquée littéralement à la vitesse entière. Les deux défauts
sont réparables et ne valident pas pour autant la production dynamique de
(40). Celle-ci devient le verrou actif : uniformité des seuils de troncature,
du coefficient de Grönwall et de la constante de Poincaré dans l'étape
De Giorgi.

Le cycle 0017 isole ensuite le bloc (23)–(40). Sous une estimation uniforme
et dimensionnée du stretching restreint (22), une solution classique et la
borne critique uniforme faible-`L^(3/2)`, l'énergie tronquée produit bien la
queue `lambda^(-3/2)log^(-3/2)` avec seuil d'absorption, coefficient de
Grönwall et terme initial suivis. Cette étape n'est pas une itération De
Giorgi : aucun enchaînement de niveaux n'apparaît. La coercivité est
Hölder-sur-support plus Sobolev, non une Poincaré sur un domaine mobile.

Trois corrections empêchent toujours de promouvoir la v2. Faible-
`L^(3/2)` seul ne rend pas les tronqués énergétiques (`|x|^-2` les fait
diverger), donc la régularité classique pré-singulière est essentielle.
L'estimation terminale ne justifie aucune absorption aux temps antérieurs.
Enfin, le facteur deux de la sommation dyadique (20)–(21) est faux (`8/3`
sur un exemple exact), bien qu'une constante trois répare localement l'ordre.
Le premier maillon non reproduit est désormais le théorème de commutateur
(8)–(22), pas Grönwall ni Chebyshev.

Le cycle 0018 ferme ce maillon fonctionnel **conditionnellement**. Après
dimensionnement par une longueur `R_*`, l'extension de Jones contrôle la
semi-norme BMO du symbole avec une constante indépendante de la boule; CRW et
interpolation réelle contrôlent le champ proche dans faible-`L^(3/2)`. Les
termes lointains compensent exactement `R^-2` par le facteur local `R²`.
Dans la queue intermédiaire, les moyennes imbriquées peuvent dériver d'ordre
un, mais le poids du noyau `4^-k` donne la somme convergente
`sum_(k>=1)(k+1)4^-k=7/9` et conserve le gain logarithmique.

Trois erreurs littérales de `arXiv:2607.08866v2` sont isolées sans réfuter le
taux final : faible-`L^(3/2)` n'est pas réflexif; la réarrangée du noyau
tronqué est `1/(a³+s/|B_1|)` plutôt qu'un `min` exact; le facteur deux du
dernier anneau doit être remplacé par trois à petite échelle. Le lemme
`NS-LOCALIZED-LOG-COMMUTATOR` reste `COMPUTATION_ONLY` et exige déjà la borne
globale uniforme `bmo_phi` de la direction. Il ne la déduit pas de la
dynamique, ne gère pas automatiquement les zéros de vorticité ou plusieurs
cœurs et n'implique donc aucune alternative Clay. Le verrou actif passe à la
synchronisation quantitative de l'endgame `(49)–(58)`.

Le cycle 0019 ferme à son tour cet endgame **conditionnellement**. La lecture
littérale de la v2 est incomplète : si `T_t` est réellement le temps maximal
local à partir de `t`, alors `s=t+T_t=T*` et la propriété d'échappement n'est
pas applicable. Le critère publié de Grujić 2013 sépare au contraire le cas où
le temps local franchit `T*`, qui prolonge directement la solution, du cas où
un temps analytique garanti reste strictement avant `T*`.

Après cette réparation, une queue uniforme et dimensionnée
`C_mu/[a³log³(e+a/U_*)]` construit un rayon sparse
`C_4/[U log(e+theta U/U_*)]`. Il devient inférieur au rayon analytique
`nu/(c_AU)` au-dessus d'un seuil fini, puis Solynin et le principe additif des
deux constantes imposent `U(s)<=U(t)` au même temps d'échappement. Le facteur
de croissance analytique `M` doit être exactement celui verrouillé par la
combinaison harmonique; un facteur différent donne un contre-résidu `6/5>1`
dans un témoin rationnel.

Ce résultat ne promeut pas le théorème 7.4 de la prépublication au rang de
preuve Clay. Il suppose la queue uniforme et, plus en amont, la vorticité
faible-`L^(3/2)` et la direction globale `bmo_phi`. La prochaine question est
donc structurelle : une direction cohérente seulement sur chaque cœur actif
peut-elle être étendue à travers les zéros et entre plusieurs cœurs avec le
taux logarithmique uniforme exigé ?

Le cycle 0020 répond négativement à cette question sous ses seules prémisses.
Si une direction vaut `+e` et `-e` sur deux parties de fractions `a,b` d'un
même domaine test, toute extension a une oscillation moyenne au moins
`4ab/(a+b)`; la constante est optimale. Deux cœurs de fractions fixes à des
échelles tendant vers zéro imposent donc un coût logarithmique divergent,
malgré une cohérence parfaite dans chaque cœur. La réalisation par potentiel
compact lisse respecte exactement l'incompressibilité et le scaling critique
faible-`L^(3/2)`, mais reste une famille de données initiales distinctes, non
une trajectoire de blow-up.

Le même audit distingue les espaces utilisés : la v2 de Grujić suppose une
norme globale ancrée par `L∞`, tandis que Bradshaw–Grujić 2015 contrôlent
`psi xi` dans un `tilde-bmo_phi` ancré par `L¹`. Ni Goldberg, ni Janson, ni
Nakai–Yabuta n'autorisent à identifier littéralement ces normalisations. La
solution nulle révèle en outre une ambiguïté de définition : deux extensions
unitaires sur `{omega=0}` peuvent avoir respectivement une semi-norme nulle et
infinie.

Le théorème conditionnel 2026 n'est pas réfuté puisqu'il suppose déjà la
borne globale. Le raccord depuis une géométrie seulement active l'est. Toute
réparation doit imposer un packing inter-composantes de taille
`4ab/(a+b)=O(phi(r))` et fixer une extension mesurable en espace-temps. Le
verrou actif se déplace vers l'admissibilité complète du profil critique
ponctuel sous `div omega=0`, Biot–Savart, énergie et coupures uniformes.

Le cycle 0021 audite cette admissibilité. La Definition 2.1 de la v2 reste
phénoménologique : une lecture purement majorante de `O(r^-2)` inclut des
profils lisses, tandis qu'une lecture non dégénérée jusqu'au centre est déjà
singulière avant `T*`. Aucun rayon de cœur ni mode de convergence rescalée
n'est fixé. La v3 récente de Barker `arXiv:2510.20757`, enregistrée comme
`NS-SRC-0084`, fournit par contraste des notions explicites de solution faible
adaptée et de point singulier, mais ne valide pas le profil de la v2.

Le raccord vectoriel produit deux conditions sphériques exactes : la partie
tangentielle du facteur doit être sans divergence sur `S²` et le flux radial
moyen doit être nul. Sous ces conditions, Biot–Savart reconstruit une vitesse
homogène `-1`; sa constante ponctuelle absolue est au plus
`pi²||Omega||_infinity/(4r)`.

Un profil explicite réalise simultanément divergence nulle, magnitude
`r^-2`, faible-`L^(3/2)` et énergie locale finie, mais sa direction conserve
une oscillation au moins `2/3` à toutes les échelles. Le phénomène est rigide :
toute direction exactement périodique sous une dilatation et appartenant à
un `bmo_phi` avec `phi(r)->0` est constante; divergence nulle et faible-
`L^p` global forcent alors la vorticité à être nulle.

Cette exclusion concerne la récurrence **vectorielle spatiale exacte**, non
les profils de Leray généraux, la périodicité de la seule magnitude, les
directions asymptotiques ou Type II. Une coupure radiale brute crée en outre
un défaut de divergence `L¹` indépendant de son échelle; le correcteur exact
reste critique et le contrôle standard de pression perd un logarithme.

Le cycle 0022 traite cette rectification fixe. Dans les variables
`s=log(R_*/r)`, le signe exact est

```text
div(r^-2 Omega)=r^-3[div_(S²)Omega_T-partial_s Omega_r].
```

Le premier harmonique `e dot theta` fournit un moment borné. Si
`Phi=|Omega|` reste uniformément borné, si chaque bloc logarithmique conserve
une masse moyenne `Phi^(3/2)` non nulle et si la direction converge vers un
axe fixe en moyenne pondérée, ce moment doit décroître d'une quantité fixe à
chaque bloc. Le profil solénoïdal ne peut donc atteindre le centre. Cela
exclut en particulier une magnitude homogène ou log-périodique non nulle avec
direction uniforme `e+O(1/|log r|)`.

La frontière est explicite :

```text
W=(s²-s)e+s(e dot theta)theta,
u=(s²/2)e cross x
```

réalise exactement la rectification et le raccord div–curl, mais son facteur
critique dégénère comme `e^-2s s²`; la vorticité physique n'est plus que
logarithmique. Des calottes angulaires d'amplitude croissante montrent que la
borne faible-`L^(3/2)` globale seule ne remplace ni la borne de tranche ni la
masse par bloc.

La veille primaire ajoute quatre résultats publiés : Chae 2015 et Chae–Wolf
2017 excluent des classes asymptotiquement DSS, Giga–Miura 2011 traite une
direction uniformément continue sous Type I, et Ożański–Palasek 2023 obtient
une rigidité quantitative axisymétrique sous faible-`L³`. Lei–Ren–Tian
`arXiv:2501.08976v1` affirme en outre qu'un double cône fixe contenant toute
la forte vorticité régularise une solution faible adaptée; une rectification
uniforme espace-temps vers un axe fixe tombe dans ce critère, sous réserve du
statut de prépublication.

Le verrou restant n'est donc plus l'axe fixe : il faut construire ou exclure
un axe errant, une cascade angulaire ou plusieurs cœurs qui échappent à tout
double cône fixe, tout en conservant divergence, masse critique, Biot–Savart,
pression et résidu Navier–Stokes. C'est `GAP-WANDERING-AXIS-PROFILE`.

Le cycle 0023 resserre ce verrou. Pour un axe mobile absolument continu, le
premier harmonique donne un budget où la recharge maximale vaut
`(M/2)Var(e)`. Une masse critique non dégénérée par bloc force donc une
variation linéaire explicite, sauf densité positive de l'erreur
directionnelle. Une dérive de phase `beta log(1+s)` satisfait le taux
d'oscillation centré `O(1/s)` mais sa variation n'est que logarithmique; elle
est exclue. À l'inverse, une rotation uniforme accumule assez de variation
mais conserve une oscillation moyenne strictement positive sur toutes les
boules centrées et échoue au taux log-BMO.

Cette dichotomie ne traite pas une direction multivaluée, plusieurs cœurs ou
une intermittence angulaire rendant toute sélection d'axe non canonique. Elle
ne produit pas les hypothèses de masse et de tranche depuis l'énergie, et ne
calcule ni Biot–Savart, ni pression, ni résidu NS. Le verrou actif est donc
`GAP-MULTICORE-ANGULAR-CASCADE`.

La veille ajoute le critère publié de Miller 2021 : un plan variable en
espace-temps est permis si son gradient spatial est borné et si la composante
transverse de la vorticité appartient à `L⁴_tL²_x`. Cela tolère une rotation
purement temporelle mais pas un axe radial de gradient
`1/[r|log r|]`. Le corollaire 1.6 de Lei–Ren–Tian tolère lui aussi un axe par
tranche sous une condition pairwise sur toute vorticité non nulle. Aucun de
ces résultats ne convertit la seule hypothèse log-BMO en axe normalisable ni
ne ferme les configurations multicoeurs.

Le cycle 0024 corrige cette dernière formulation. Si la direction est déjà
prolongée en un **même champ global unitaire** `Xi`, alors

```text
average_B |Xi-(Xi)_B|² = 1-|(Xi)_B|²
```

et une oscillation logarithmique petite rend ses moyennes non dégénérées. La
dérive entre boules dyadiques reste toutefois `O(1/k)`, donc non sommable. Pour
une extension seulement bornée, égale à la direction unitaire sur le cœur
actif, une borne `Phi<=M` et une masse `Phi^(3/2)` par bloc donnent une fraction
active uniforme. Les axes normalisés ainsi extraits ont variation et erreur
pondérée `O(log N)`; le budget du cycle 0023, linéaire en `N`, exclut alors le
profil solénoïdal. Cela ferme `GAP-MULTICORE-ANGULAR-CASCADE` sous ces prémisses.

La frontière est nette : des fractions actives `a_n=n^-3` d'amplitude
`Phi_n=n²` conservent la masse critique tandis que l'extension par zéro a une
oscillation `2a_n(1-a_n)` et une moyenne de norme `a_n`, toutes deux tendant
vers zéro. Le faible-`L^(3/2)` seul ne remplace donc pas la borne d'amplitude.
Aucune source primaire inspectée ne construit par ailleurs un prolongement
global `S²`-valué log-BMO depuis la direction définie seulement sur
`{omega!=0}`. Le verrou actif devient
`GAP-UNBOUNDED-ANGULAR-INTERMITTENCY` : quantifier ou réaliser une concentration
angulaire d'amplitude non bornée qui satisfasse aussi divergence, Biot–Savart,
pression, évolution et admissibilité Clay.

Le cycle 0025 réalise quatre de ces portes par un train explicite de blobs.
Une vitesse de base polynomiale compacte est translatée aux rayons `2^-n` et
remise à l'échelle aux largeurs `2^-n/(8n)`. La somme a une énergie finie, sa
vorticité est dans `L¹ intersect L^(3/2,infinity)`, chaque bloc logarithmique
porte une masse critique constante et le raccord Biot–Savart est unique dans
`L²`. L'amplitude du facteur angulaire croît comme `n²`, tandis que
l'oscillation de la direction étendue par zéro sur les seules boules centrées
en l'origine décroît comme `n^-3`.

Ce contre-profil ne passe pas la prémisse globale : la forme directionnelle
interne non constante est reproduite sur des boules décentrées de rayon
`ell_n/2`. Leur oscillation garde une minoration positive uniforme pour
**toute** extension coïncidant avec la direction sur l'ensemble actif. La
sparsité ne peut donc masquer un motif récurrent à sa propre échelle. Le
résidu stationnaire a par ailleurs un curl polynomial non nul et une masse
`L¹` invariante par blob; aucune pression ne le transforme en solution.

Le nouveau verrou `GAP-DIRECTIONALLY-FLAT-INTERMITTENCY` exige une géométrie
interne qui s'aplatit avec l'échelle. Comme toute vorticité compacte de la
forme `curl U` a intégrale vectorielle nulle, une direction presque constante
doit être compensée par une région opposée de faible volume et forte
amplitude. Ce second niveau d'intermittence, sa divergence, son coût BMO et son
résidu dynamique sont désormais les quantités prioritaires.

Le cycle 0026 quantifie ce coût sans borne ponctuelle. Sur un domaine `D`, si
`W` a moyenne vectorielle nulle et quasi-norme faible-`L^(3/2)` égale à `K`,
toute masse `m` portée par le cône `xi·e>=alpha` force une masse opposée. La
borne de réarrangement critique donne

```text
MO_D(xi)>=2alpha³m³/[27K³|D|].
```

La passe analytique conserve le poids de projection négative et renforce la
borne provisoire `alpha^4/27`. Sans moyenne nulle, la version canonique
remplace ce raccord par la masse `nu_e=integral(-W·e)_+`.

Le quotient `m/[K|D|^(1/3)]` est invariant d'échelle. Une famille de blobs
log-BMO doit donc faire disparaître sa masse conique normalisée au moins comme
la racine cubique du module d'oscillation.

Cette condition ne découle pas de la masse critique. Le modèle à deux
amplitudes, de fractions `1-n^-3` et `n^-3`, garde moyenne nulle, quasi-norme
faible égale à un et masse forte `L^(3/2)` entre un et deux, tandis que sa
masse conique vaut `1/n` et son oscillation de domaine est
`4n^-3(1-n^-3)`. L'exposant cubique est donc optimal au niveau mesurable.

Une interface spatiale régulière entre les deux phases conserve toutefois une
oscillation locale égale à un. Si un corridor de zéros sépare les phases, une
extension unitaire logarithmique atteint plutôt un coût
`Theta(1/log(R/h))`; le volume seul ne contrôle pas le rapport géométrique.
Enfin, un champ exactement collinéaire, compact et divergence-free est nul,
donc le modèle atomique ne se relève pas directement en curl. Le verrou actif
devient `GAP-NESTED-RETURN-FLOW-CASCADE` : tester un potentiel axisymétrique
qui conserve ses composantes transverses, répartir son retournement sur une
cascade interne non-Dini qui passe toutes les boules, puis recalculer vitesse,
pression et résidu.

Le cycle 0027 exécute ce test pour
`U=chi(z)A_n(r)e_theta`. Le profil axial positif d'amplitude `n^-1` est
compensé par un anneau de largeur `n^-3` et d'amplitude
`3n^5/(8n^3+1)~(3/8)n²`. Le flux `integral r f_n(r)dr` s'annule exactement;
le champ est un curl compact divergence-free, sa quasi-norme faible-
`L^(3/2)` reste entre deux constantes et son énergie normalisée est
`O(n^-2)`.

La fermeture axiale révèle cependant une perte indépendante des amplitudes.
Dans le corridor où `A'+A/r=0` mais `A!=0`, la calotte impose
`W=-chi'Ae_r`. Une boule de rayon `w` à distance `R` de l'axe vérifie

```text
MO_B(W/|W|)>=3w/[2048(R+w)].
```

Pour un aspect fixé, cette borne survit à la concentration et fait diverger
le poids log-BMO. Le résidu stationnaire garde en outre une composante
azimutale `-Lpsi` non nulle qu'aucune pression monovaluée ne peut compenser.

Une seconde mise à l'échelle, où la largeur des calottes vaut aussi `n^-3`,
réalise `MO_D~n^-3` sur un domaine parent fixe tout en gardant la quasi-norme
faible critique uniforme. La passe analytique construit même une variante
`C_c^infinity` avec `m~epsilon^(1/3)` et `MO_D~epsilon`. La contrainte
div–curl compacte n'améliore donc pas l'exposant cubique du cycle 0026. Cette
petite moyenne parentale ne donne toutefois pas le BMO all-ball; de plus
`||U_epsilon||_3->0`, ce qui place la famille dans le régime régulier de
petites données.

La veille primaire confirme que la représentation axisymétrique est
classique (`NS-SRC-0102`); les correcteurs de de Rham (`0103`, `0111`) ne
fournissent pas d'uniformité directionnelle. Dix sources sont ajoutées et le
corpus atteint 111 entrées. La nouveauté revendiquée reste seulement la porte
quantitative interne, au statut `COMPUTATION_ONLY`. Les vortex rings usuels
portent une vorticité toroïdale et ne fournissent pas ce lift poloidal. Le
verrou actif
devient `GAP-NONSEPARABLE-RETURN-FLOW-MASKING` : tester une somme de couches
où la composante verticale suivante masque le retour radial précédent. Un
aspect croissant peut être nécessaire mais ne suffit pas à supprimer les
transitions locales. Il faut suivre les capacités des régions radialement
dominantes, le BMO all-ball, les normes critiques, l'énergie, le diamètre
physique et le résidu.

Le cycle 0028 réfute la nécessité de ce dernier mécanisme. Une vorticité
toroïdale pure `omega=A beta(d^2/h^2)e_theta` est divergence-free et de
moyenne nulle sans calotte radiale. Pour `h<<q<<R`, sa direction sur le cœur
s'étend vers `e_z` à travers un corridor logarithmique et satisfait une borne
log-BMO uniforme sur toutes les boules. Ce résultat est une dérivation interne
statique, non un théorème de propagation.

La passe Biot–Savart ferme toutefois le candidat comme profil critique de
vitesse : après normalisation faible-`L^(3/2)`,

```text
||u||_3^3<=C[(h/R)+(h/R)^2] -> 0.
```

Sur `R^3`, l'impulsion positive produit en plus une queue non-Schwartz et la
sous-classe axisymétrique sans swirl est globalement régulière. À temps
positif, pour un anneau unisigné, la diffusion réactive `e_theta` près de
l'axe et fait échouer le log-BMO global. La périodisation sur `T^3` fournit
seulement une donnée lisse admissible, sans symétrie continue propagée.

Le sous-problème poloidal reçoit parallèlement un lemme quantitatif : un excès
`Delta_Omega>0` minore la mesure puis la capacité newtonienne de
`{|W_r|>=|W|/4}`. Le rang fini seul ne force pas cet excès. Le verrou actif
devient `GAP-MOMENT-CORRECTED-TOROIDAL-CASCADE` : annuler d'abord l'impulsion
par une paire de tores signés, conserver faible-`L^(3/2)` et log-BMO, quitter
la classe sans swirl et empêcher `||u||_3` de tendre vers zéro.

Le cycle 0029 exécute cette première correction. Deux tores congruents, de
signes opposés et d'axes parallèles déplacés transversalement, annulent
exactement l'impulsion, conservent la criticité de vorticité et les corridors
log-BMO, et brisent l'axisymétrie globale. Ce succès cinématique ne répare
aucun des deux raccords Clay.

D'une part, le second moment translaté reste non nul et produit une queue
`|x|^-4` sur `R^3`; annuler l'impulsion n'équivaut pas à une vitesse de
Schwartz. D'autre part, Stokes sur les sections du cœur et le potentiel
tubulaire donnent l'équivalent critique

```text
cK^3 h/R<=||u||_3^3<=CK^3[(h/R)+(h/R)^2].
```

Il tend vers zéro dans le régime mince exigé par le corridor. Tout cardinal
uniformément borné de tubes disjoints subit la même obstruction, quels que
soient les signes et un nombre fini de moments annulés. Le verrou devient
`GAP-MANY-TORUS-CRITICAL-ACCUMULATION` : seul un cardinal croissant avec
addition cohérente des vitesses, ou une vitesse compacte construite en amont,
reste informatif.

La veille `NS-SRC-0113`–`0117` montre que les progrès 2025–2026 sur les
paires anti-parallèles établissent des croissances Euler à temps infini dans
la classe sans swirl. Ils n'impliquent ni concentration en temps fini, ni
uniformité à viscosité fixée. Pour une paire visqueuse coaxiale signée, la
diffusion crée en outre une interface directionnelle d'oscillation un sur le
plan de symétrie; ce rejet dynamique ne couvre pas la paire transversale.

## Cycle 0030 — cardinal croissant poreux et séparation des endpoints

Le régime de tores à paramètres communs est maintenant fermé même lorsque le
cardinal diverge. Pour une amplitude commune `A`, un coeur `h`, un corridor
`q`, une longueur totale `mathcal L` et un packing local
`length(B_r)<=C r^3/q^2`, la décomposition de Biot–Savart donne

```text
||u||_3^3<=C K^3[h/mathcal L+(h/q)^(4/3)],
K=||omega||_(L^(3/2,infinity))^*.
```

Le premier terme est le champ tubulaire proche. Le second utilise la densité
de Morrey effective `D=A(h/q)^2`, Hedberg, HLS
`I_1:L^(6/5)->L^2`, puis `||v||_3^3<=||v||_2^2||v||_infinity`.
Sur le tore unité, le reste lisse du noyau ajoute `C K^3 S`, où
`S~mathcal L h^2`; cette quantité doit tendre vers zéro. La famille exacte à
`N_n=2^(12n-12)` fait diverger la somme triangulaire mais satisfait
`||u_n||_3^3<=C[2^(-21n+12)+2^(-4n)+2^(-15n-12)]`.

Le résultat est elliptique et `COMPUTATION_ONLY`. Il exige des paramètres
communs et un packing local; une cascade hétérogène n'est pas couverte. La
réalisation coaxiale est en outre axisymétrique sans swirl et aucune
propagation log-BMO n'est démontrée.

Le pivot naïf « vitesse compacte et norme forte `L^3` non petite » est réfuté
dans le même cycle. Des copies compactes divergence-free à rayons
super-géométriques vérifient exactement `BS[curl U_N]=U_N`. Normalisées par
`N^(-1/3)`, elles gardent `||U_N||_3` constant tandis que leurs normes faibles
critiques tendent vers zéro; sans normalisation, ces normes faibles restent
bornées et `||U_N||_3^3` croît comme `N`. La direction interne d'un curl
compact non nul reste toutefois oscillante et coûte `|log r_j|` après
concentration.

La veille ajoute Yamazaki pour la petite donnée faible-`L^3`, six sources
2025–2026 sur anneaux et filaments, et Hedberg–Lieb–Adams pour les potentiels;
le corpus atteint 127 entrées. Aucun résultat récent ne fournit une constante
uniforme lorsque le nombre de filaments tend vers l'infini. Le verrou actif
est `GAP-COMPACT-VELOCITY-WEAK-CRITICAL-DIRECTION` : aplatir la direction
interne d'un curl compact multi-échelle sans tomber dans le régime faible-`L^3`
petite donnée ni perdre le temps d'interaction visqueux.

## Cycle 0031 — fermeture du rapport d'aspect séparable

Une vitesse compacte construite en amont évite les queues multipolaires, mais
un produit toroïdal séparable ne peut aplatir gratuitement sa direction. Pour

```text
U=V(R/r)eta((r-R)/a)chi(z/b)e_theta,
```

le facteur `R/r` annule exactement la courbure dans `curl U`. Les transitions
radiale et axiale occupent chacune un volume comparable à `Rab` et donnent

```text
||U||_(L^(3,infinity))^3~V^3Rab,
||curl U||_(L^(3/2,infinity))^3
 >=cV^3 max(R^2b^2/a,R^2a^2/b).
```

Une vitesse faible critique uniformément non petite et une vorticité faible
critique uniformément bornée forcent donc `a/R` et `b/R` à rester positifs.
Sur une boule de calotte, la direction vaut exactement `e_r`; son oscillation
ne peut plus décroître et le poids logarithmique diverge sous concentration.

Ce no-go est `COMPUTATION_ONLY` : les exposants sont dérivés analytiquement et
37 214 identités rationnelles les auditent, mais les constantes de profils ne
sont pas certifiées par intervalles. La veille primaire confirme que
`NS-SRC-0059` reste une prépublication v2 et `NS-SRC-0061` une v1; aucune ne
construit un curl compact satisfaisant simultanément les deux endpoints et le
gate directionnel. Les entrées `NS-SRC-0128`–`0131` ajoutent les grandes
données anisotropes régulières, deux critères axisymétriques publiés et une
construction Euler hélicoïdale récente; le corpus atteint 131 sources. Le
verrou actif devient
`GAP-NONSEPARABLE-COMPACT-CURL-FLATNESS`, où des couches décalées pourraient
masquer les transitions du produit simple.

## Cycle 0032 — collapse universel des swirls purs à section mince

Le masquage par couches est fermé sans séparer les transitions. Pour tout
`F in C_c^infinity` supporté dans `R/2<r<3R/2`, posons

```text
U=(R/r)F(r,z)e_theta,  W=curl U,
S_2=|supp F|_(dr dz).
```

Le potentiel bidimensionnel du gradient, le weak HLS
`I_1:L^(3/2,infinity)->L^(6,infinity)`, l'inclusion faible sur support fini et
les poids cylindriques donnent

```text
||U||_(L^(3,infinity)(R3))
 <=C(S_2/R^2)^(1/6)||W||_(L^(3/2,infinity)(R3)).
```

Le quotient `S_2/R^2` est invariant par scaling Navier–Stokes. Sous un gate
vitesse `>=kappa` et un gate vorticité `<=K`, il faut donc
`S_2/R^2>=C^-6(kappa/K)^6`. Ce théorème cinématique interne est indépendant
du nombre, des signes, des décalages et des annulations des couches parce
qu'il agit sur leur somme finale.

Le certificat P1 rationnel teste 384 masques non séparables sur quatre
maillages : 272 726 assertions exactes, zéro échec. Il ne certifie pas la
constante du continuum. Trois passes contradictoires distinctes vérifient les
sens weak-to-weak, les comparaisons cylindriques, les annulations locales et
la portée des outils canceling.

La veille ajoute coaire/TV et trois sources div–curl/Lorentz
(`NS-SRC-0132`–`0135`), portant le corpus à 135 sources. Aucune ne transforme
ce no-go statique en régularité générale. Les sections d'aire comparable à
`R^2`, les vitesses poloïdales et non axisymétriques, la pression et le temps
restent ouverts. Le verrou actif devient
`GAP-THICK-CROSS-SECTION-GRADIENT-DIRECTION`.

## Cycle 0033 — coercivité directionnelle sur une section de diamètre borné

Le support topologique épais n'est pas utilisé directement. À partir d'un
superniveau presque optimal de la vitesse, une troncature signée
`G=(sigma F-lambda/2)_+` vérifie simultanément :

```text
|{sigma F>lambda}|^(1/6)>=c K_f/K_g,
TV(G)>=c K_f^2/K_g,
integral |curl[(R/r)G e_theta]|>=c R K_f^2/K_g.
```

Le curl tronqué a moyenne vectorielle nulle. Une partition finie des directions
sélectionne une masse conique, puis `NS-LORENTZ-CONE-COMPENSATION` donne, sur
une vraie boule contenant la tranche axiale `|z-z_0|<Lambda R`,

```text
MO_B(zeta)>=c_Lambda
  (||U||_(L^(3,infinity))/||curl U||_(L^(3/2,infinity)))^6.
```

Cette borne vaut pour toute extension `L1` de la direction, même non unitaire
sur les zéros, et pour tout potentiel `F` non séparable. Sous les deux gates
endpoint et `R_n->0`, le poids `|log r_B|` diverge donc. Les plateaux épais et
les compensateurs rares restent exclus tant que le diamètre axial est `O(R)`.

Le certificat exact exécute 2 884 assertions sans échec. Il vérifie notamment
la réciprocité entre faible fraction directionnelle et coût endpoint, ainsi
que le coût `N` de `N` cellules identiques. Des amplitudes dyadiques gardent les
endpoints bornés mais laissent la première cellule dominante.

Le résultat est `COMPUTATION_ONLY`, statique et pure-swirl. Le verrou actif
devient `GAP-AXIALLY-DISPERSED-PURE-SWIRL-SELECTION` : sélectionner un bloc
local non dégénéré parmi des cellules hétérogènes séparées, ou construire une
distribution sans bloc dominant qui réfute cette sélection.

La veille topologique ajoute Hopf, Amann, Brezis–Nirenberg Part II et Whitney
(`NS-SRC-0136`–`0139`). Ils donnent qualitativement
`extremum isolé -> direction non-VMO -> log-BMO infini`, mais aucune masse de
vorticité ni constante endpoint. Le facteur de la vraie boule dans le résultat
quantitatif est `c(9/4+Lambda^2)^(-3/2)`; le meilleur facteur `Lambda^-1`
concerne seulement le domaine annulaire axial, qui n'est pas une boule.

## Cycle 0034 — cellules hétérogènes et registre BV

La sélection d'une cellule depuis les seules quasi-normes faibles est fausse.
Une famille dyadique exacte vérifie

```text
K_u=1,
1<=K_w<=(1-2^(-3/2))^(-2/3),
sup_j K_(u,j)/K_(w,j)=N^(-1/3)->0.
```

Elle ne satisfait pas `W_j=curl U_j` : sa masse de retour perd un facteur
géométrique croissant. Le claim abstrait
`NS-WEAK-LORENTZ-CELL-SELECTION` est donc `REFUTED` sans transfert silencieux
à la classe pure-swirl.

Le claim `NS-BV-REGISTERED-HETEROGENEOUS-CELL-SELECTION`, statut
`COMPUTATION_ONLY`, rétablit la sélection sous

```text
|Q_j|<=C v_j,
plateau effectif de taille v_j,
integral_(Q_j)|W_j|>=c A_j v_j^(2/3).
```

Il existe alors une cellule telle que

```text
K_(u,j)>=cK_u^2/K_w,
K_(u,j)/K_(w,j)>=c(K_u/K_w)^2.
```

Coaire et isopérimétrie donnent ce registre pour des cellules pure-swirl
épaisses, disjointes, à aspect et plateau uniformes. Le cycle 0033 transforme
le rapport sélectionné en
`MO_(B_j)>=c(K_u/K_w)^12`. Une suite ne donne un coût log-BMO divergent que
si les rayons des cellules sélectionnées tendent effectivement vers zéro.

Le corpus atteint 147 sources après ajout des outils de profils et des
résultats dynamiques de Barker–Prange. Aucun théorème publié contrôlé ne
fournit la même cellule depuis les seuls endpoints faibles. Le verrou devient
`GAP-DEGENERATE-CELL-REGISTER-OR-OVERLAP` : boîtes trop grandes, plateaux
dégénérés, curls qui se chevauchent, ou absence de sélection dynamique de
l'échelle.

## Cycle 0035 — bande de niveau commune sans boîte

Le volume témoin `v_j` du cycle 0034 ne calibre pas automatiquement un halo.
Une dilatation pure-swirl lisse avec `R_L=L`, `A_L=L^-1` conserve ses deux
endpoints, sur-satisfait le registre BV total et possède un témoin de volume
un, mais toute masse de curl sur un ensemble de volume borné est `O(L^-2)`,
contre `A_Lv_L^(2/3)=L^-1`. Le claim
`NS-FIXED-CORE-HALO-LOCALIZATION` est donc `REFUTED`.

La réparation n'utilise aucun halo fixé. Pour une famille finie de cellules

```text
U_j=(R_j/r)F_j e_theta,
supp F_j subset {R_j/2<r<3R_j/2},
```

à supports complets disjoints, un niveau global presque optimal `lambda`
définit les bandes signées

```text
H_(j,sigma)={lambda/4<sigma F_j<lambda/2}.
```

Elles sont incluses dans `{|U|>lambda/6}`. Coaire tridimensionnelle et
isopérimétrie donnent une masse de curl proportionnelle à
`lambda sum V_(j,sigma)^(2/3)`. Après la borne faible-`L^(3/2)`, une cellule
vérifie

```text
K_(u,j)>=(C_I/324)K_u^2/K_w,
K_(u,j)/K_(w,j)>=(C_I/324)(K_u/K_w)^2.
```

Le claim `NS-PURE-SWIRL-COMMON-LEVEL-CELL-SELECTION` reste
`COMPUTATION_ONLY` malgré trois passes contradictoires IA. Il ne suppose ni
diamètre axial, ni volume support, ni plateau uniforme. Il contrôle toutefois
seulement le volume total de la bande; une bande dispersée n'est pas localisée
dans une boule. Le corpus atteint 155 sources et le verrou actif devient
`GAP-ACTIVE-HALO-DIAMETER-OR-OVERLAP`.

## Cycle 0036 — sélection d'une composante active

La bande commune peut être décomposée aux composantes connexes de
`{sigma F_j>lambda/4}` rencontrant le coeur `lambda/2`. Pour chaque composante,

```text
G_alpha=(sigma F_j-lambda/4)_+ 1_(C_alpha)
```

est lipschitzienne compacte et s'annule sur son bord. Son curl est exactement
`sigma W_j` dans la composante et zéro ailleurs, sans mesure surfacique. Coaire
et isopérimétrie peuvent donc être sommées avant le pigeonhole. Une troncature
vérifie

```text
K_(u,alpha)>=(C_I/648)K_u^2/K_w,
K_(u,alpha)/K_(w,alpha)>=(C_I/648)(K_u/K_w)^2.
```

Si chaque composante tient dans une tranche axiale `O(R_j)`, l'extension
lipschitzienne explicite du gate 0033 donne
`MO_B>=c(K_u/K_w)^12`. Le claim principal et le claim d'interface restent
`COMPUTATION_ONLY`.

La géométrie générale est maintenant mieux bornée. Frank–Lieb garantit depuis
volume et périmètre une boule de rayon `V/P` captant `>=c(V/P)^3`, mais une
fragmentation en gouttes rend la fraction `cV^2/P^3` dégénérée. Même une
composante de périmètre fini peut avoir un diamètre arbitraire via un tube
mince. Seregin et Barker contrôlent plusieurs centres singuliers de vraies
solutions sous budgets critiques/d'epsilon-régularité supplémentaires; ils ne
fournissent pas le raccord Clay général.

Le certificat exact compte 1 920 familles, 10 560 composantes et 5 773
assertions sans échec. Des copies identiques ont un rapport global qui décroît
comme `m^-1/3`; un filament strictement sous `lambda/4` est supprimé. Le
corpus atteint 162 sources. Le verrou actif devient
`GAP-ABOVE-THRESHOLD-THIN-BRIDGE` : un pont de petite section mais d'amplitude
au-dessus du cutoff peut fusionner deux gouttes éloignées.

## Cycle 0037 — coût d'un pont persistant dans la section méridienne

La dimension méridienne deux corrige une généralisation trop pessimiste du
cycle 0036. Pour toute composante M-indécomposable planaire, Dayrens–Masnou–
Novaga–Pozzetta (`NS-SRC-0163`) prouvent

```text
2 diam(E^1)<=P_2(E).
```

Combinée à la coaire et au curl exact de
`U=(R/r)F e_theta`, cette borne donne la nouvelle obstruction critique

```text
a(b-a)RD<=9 K_u K_w/(8 pi).
```

Si une composante reste au-dessus d'un cutoff `A`, elle persiste sur la bande
`(A/2,A)` et vérifie

```text
A^2RD<=9 K_u K_w/(2 pi)<=(3/2)K_uK_w.
```

L'excès du pont au-dessus du cutoff peut donc tendre vers zéro sans réduire le
coût du curl original : les niveaux inférieurs doivent encore fermer. Sous le
calibrage `AR>=kappa K_u`, le diamètre normalisé est borné par
`9(K_w/K_u)/(2 pi kappa^2)`, ce qui raccorde conditionnellement la composante
au gate directionnel.

Le claim `NS-PURE-SWIRL-PERSISTENT-BRIDGE-DIAMETER` reste
`COMPUTATION_ONLY` : l'inégalité primaire périmètre–diamètre est publiée, mais
sa composition axisymétrique, ses constantes et son raccord endpoint sont une
dérivation IA auditée. Un ledger rationnel sur 1 035 familles et 5 197
assertions confirme la loi d'échelle. Le contre-profil à deux gouttes montre
qu'un curl tronqué borné exige `eta<~sqrt(delta)/L`, donc au mieux
`eta<~L^-3/2` sous `delta L<~1`, alors que le curl original diverge.

Deux limites sont exactes. D'une part, `AR>=kappa K_u` ne suit pas d'un niveau
global presque optimal lorsqu'il existe beaucoup de gouttes. D'autre part,
une composante basse peut devenir longue par une fusion sur une fenêtre de
niveaux évanescente; un grand diamètre à un niveau unique n'a aucun coût
coaire uniforme. Les merge trees (`NS-SRC-0164`–`0165`) offrent un registre
discret de cette persistance, pas un théorème continuum. La prépublication
BV récente `NS-SRC-0166` clarifie les représentants 1-fins; la prépublication
axisymétrique à petite donnée sur cylindre avec bord `NS-SRC-0167` ne se
transfère pas à `R3` ou `T3`.

Le corpus atteint 167 sources. Le verrou devient
`GAP-BRIDGE-SCALE-CALIBRATION-OR-MERGE-TREE` : calibrer localement la branche
sélectionnée ou trouver un niveau qui la scinde en morceaux de diamètre
`O(R)` sans perdre le rapport endpoint.

## Cycle 0038 — sélection adaptative d'une composante de diamètre contrôlé

L'héritage du rapport endpoint le long d'une retroncature est faux : deux
quasi-normes diminuent sous restriction sans que leur quotient soit monotone.
Un arbre dyadique exact pousse cette perte à profondeur arbitraire. Il réfute
le bookkeeping merge-tree seul, mais ne se réalise pas comme curl pure-swirl
compact parce que ses feuilles violent le coût coaire de fermeture.

La réparation ne parcourt aucun arbre. Dans une cellule annulaire
`U=(R/r)F e_theta`, un niveau faible-`L3` presque optimal `lambda` vérifie

```text
lambda R >= K^2/(432H),
K=||U||_(L^(3,infinity)), H=||curl U||_(L^(3/2,infinity)).
```

La preuve combine le volume des cores `{+/-F>lambda/2}`, la largeur radiale
`R`, `P_2>=2 diam_z`, la coaire cylindrique exacte et l'inclusion de la bande
dans `{|U|>lambda/6}`. Une moyenne sur
`(lambda/4,3lambda/8)` fournit ensuite un niveau régulier où la somme des
diamètres actifs est bornée. La sélection endpoint refaite parmi les
composantes de ce même niveau donne

```text
diam_z(C_beta)/R <= 2 239 488 (H/K)^3,
K_beta >= (C_I/20 736)K^2/H,
K_beta/H_beta >= (C_I/20 736)(K/H)^2.
```

Composé avec le cycle 0035, ce résultat produit dans une famille à supports
complets disjoints une troncature avec
`K_beta/K_global>=c q_global^3`, `q_beta>=c q_global^4` et
`diam/R_j<=C q_global^-6`. Le gate directionnel statique s'applique donc sans
hypothèse de diamètre additionnelle. Le claim reste `COMPUTATION_ONLY` : trois
audits IA et 21 756 assertions rationnelles cumulées ne constituent ni une
preuve publiée, ni une certification du continuum, ni une évolution PDE.

La veille ajoute quatre sources sur stabilité de la persistance, métriques de
merge trees, graphes de Reeb et une application Navier–Stokes 2D. Elles
confirment qu'un arbre PL devient robuste seulement avec une erreur uniforme
certifiée et des labels spatiaux; une longue barre H0 ne minore pas la marge
`col-cutoff`. Aucune arête nouvelle vers Clay n'en résulte.

Le corpus atteint 171 sources. Le verrou statique suivant est
`GAP-OVERLAPPING-CURL-CANCELLATION` : lorsque les curls de plusieurs cellules
se recouvrent, `H_beta<=H_global` peut échouer par annulation avant la valeur
absolue. Au-delà restent projection de Leray, pression, diffusion, stretching,
sélection d'un rayon `R(t)->0` et scénarios Type II.

## Cycle 0039 — multiplicité insuffisante et endpoint spectral

Le recouvrement borné ne remplace pas la disjonction. Pour un fond pure-swirl
lisse compact non nul `B` et

```text
Z_n=(chi(r)eta(z)sin(nz)/r)e_theta,
U_(1,n)=B+Z_n, U_(2,n)=-Z_n,
```

les deux supports ont multiplicité au plus deux et les sommes des vitesses et
des curls valent exactement `B` et `curl B`. Sur un ensemble de volume fixe
`4pi^2/3`, le curl de `Z_n` est d'ordre `n`, tandis que les vitesses restent
uniformément bornées. Il en résulte

```text
q(U_(1,n)),q(U_(2,n))=O(n^-1),
q(U_(1,n)+U_(2,n))=q(B)>0.
```

Le claim universel de sélection parmi les sommants est donc `REFUTED`, même
pour des champs lisses, divergence-free, curl-compatibles, de même axe et de
même anneau. Le défaut est une jauge de décomposition : ajouter `+Z_n,-Z_n`
ne change pas le champ total. Un certificat à quatre atomes vérifie exactement
344 121 assertions; un second calcul indépendant en vérifie 1 216.

La réparation positive consiste à agréger d'abord les potentiels lorsque la
géométrie commune le permet :

```text
sum_j (R/r)F_j e_theta=(R/r)(sum_jF_j)e_theta.
```

Le cycle 0038 s'applique alors au champ total, sans sélectionner un label.
Cette identité ne survit pas sous axes multiples ou localisations Hodge
différentes.

La veille fonctionnelle précise aussi la frontière spectrale. Le plein
`L^(p,infinity)` est non séparable et n'admet aucune base de Schauder
dénombrable norm-convergente. Karlovich (`NS-SRC-0172`) s'arrête à l'indice
Lorentz secondaire fini. Les carrés-fonctions de Stein/Hunt (`0173`, `0069`)
contrôlent le champ **après** sommation et ne récupèrent pas `+Z_n,-Z_n`.
Les ondelettes divergence-free de Deriaz–Perrier (`0174`) ne fournissent ni
minoration anti-annulation ni certification PDE.

La veille récente ajoute enfin Beirão da Veiga–Yang (`0175`, arXiv v1), perte
de bornitude pure-swirl pour le système incompressible forcé dans un cylindre.
Force terminalement singulière, frontière mixte et absorption de la convection
par la pression empêchent tout transfert au système Clay non forcé sur
`R3`/`T3`.

Le corpus atteint 175 sources. Le verrou devient
`GAP-MULTIAXIS-TOTAL-FIELD-LOCALIZATION` : localiser intrinsèquement le champ
total avec constantes critiques suivies, sans dépendre d'une décomposition
modifiable par jauge, puis seulement traiter pression et temps.

## Cycle 0040 — localisation solénoïdale critique et géométrie du correcteur

Une coupure du champ total peut être rendue divergence-free sans projection
globale de Leray. Pour une couronne de forme fixe
`A_R=B(x0,2R)\Bbar(x0,R)`, poser

```text
g=div(chi_R U)=grad chi_R dot U,
b=B_(A_R)g,
V=chi_R U-b.
```

La moyenne de `g` est exactement nulle parce que `chi_RU` est compact. Le
même opérateur de Bogovskiĭ, borné à deux exposants forts et interpolé, donne
le contrôle faible-`L^(3/2)`; l'homothétie rend la constante indépendante de
`x0,R`. Avec les conventions du registre,

```text
||curl V||_(3/2,infinity)
 <=3[H_out+C_chi(28pi/3)^(1/3)(1+sqrt(2)C_B)G_col].
```

La conclusion lisse utilise explicitement une réalisation préservant
`C_(c,0)^infinity`; une trace nulle Sobolev seule ne suffit pas après
prolongement par zéro. Biot–Savart faible HLS absorbe les deux budgets dans le
curl global et laisse comme seul facteur non contrôlé la fraction
`K_core/K_global`.

Le coût reste critique. Un plateau divergence-free lisse remis à l'échelle
sature le terme de col; 9 167 assertions rationnelles vérifient la loi
d'échelle avec résidu nul. Amincir la couronne ne répare rien : dans `L^p`
fort, Poincaré radiale et inf-sup imposent à toute droite inverse à trace nulle
une norme `>=c_pR/h`. Aucune version faible-Lorentz de cette minoration n'est
revendiquée.

Costabel–McIntosh (`0103`), Acosta–Durán–Muschietti (`0176`) et
Albritton–Barker–Prange (`0177`) sourcent respectivement l'opérateur sur
domaines Lipschitz/John et son usage NS sur une couronne fixe. Les
prépublications `0178`–`0179` n'apportent pas de constante critique nouvelle.
Le corpus atteint 179 sources.

Le sous-gap statique de cutoff multi-axe est fermé, mais aucune régularité
Clay n'en résulte. Le premier quantificateur non trivial est désormais la
capture d'une fraction du faible-`L3` par une boule à rayon pré-singulier
`R(t)->0`; une grande boule capture trivialement un champ compact et ne doit
pas être comptée comme progrès.

## Cycle 0041 — concentration Type I au endpoint faible-`L3`

Barker–Prange, ARMA 236 (2020), théorème 2 et appendice B, ferment le maillon
de capture au rayon parabolique lorsque la solution de Leray–Hopf sur `R3`
possède un premier point singulier et une borne Type I uniforme. L'hypothèse
publiée est une borne Morrey-énergie locale à trois suprema. Avec la convention
du registre,

```text
integral_E |u|^2 <= 3||u||_(3,infinity)^2|E|^(1/3)
```

montre que `sup_t||u(t)||_(3,infinity)<=M` l'implique avec
`A=sqrt(3)(4pi/3)^(1/6)M`. Les constantes Lorentz `gamma_w,S_w^*` donnent à
tout temps antérieur positif une boule centrée au point singulier de rayon
`2sqrt((T_*-t)/S_w^*(A))` et une fraction locale strictement supérieure à
`gamma_w/M`.

Le résultat publié est conditionnel : il suppose la singularité et la borne
Type I, n'exclut pas le blow-up et ne construit pas une singularité. La borne
d'énergie Clay ne contrôle pas `M`. En Type II, `M_j` peut diverger, la durée
normalisée dégénère et aucune fraction relative uniforme n'est obtenue.

Barker–Prange, CMP 385 (2021), renforce sous Type I la concentration en une
minoration logarithmique de `integral |u|^3` sur une boule
super-parabolique. Il ne minore la norme `L3` que comme `log^(1/3)` et ce
comportement est compatible avec une borne faible-`L3`, comme le profil
tronqué `|x|^-1` le montre. La veille primaire 2025–2026 ne ferme aucun de
ces trous; le catalogue reste à 179 sources après réaudit des notices 0146 et
0147.

## Cycle 0042 — ce que coûte réellement une localisation mobile

La littérature de localisation solénoïdale justifie un opérateur de
Bogovskii sur une couronne fixe et sa conjugaison homothétique, mais elle ne
permet pas d'ignorer sa dérivée temporelle. Pour
`B_Rg=R B[g(x_*+R dot)]((x-x_*)/R)`, la dérivée contient exactement un terme
de dilatation et le commutateur de l'opérateur unité avec `y dot nabla`.

Composée avec le rayon Type I du cycle 0041, cette identité donne une équation
Navier–Stokes **forcée** pour le champ localisé. La force locale est supportée
dans la couronne mobile et possède l'amplitude `R^-3`; sa norme `L1` est donc
invariante. La forme projetée par Leray est divergence-free mais acquiert une
queue non locale.

Un témoin pure-swirl lisse, compact et divergence-free vérifie
`nabla chi_R dot u_R=0`, donc annule tout correcteur de Bogovskii, tandis que
`R^3(partial_t chi_R)u_R` reste explicitement non nul. Le rayon décroissant
ne fournit donc aucune petitesse. Les couples critiques à exposant temporel
fini accumulent même un poids logarithmique si le profil annulaire persiste.

La borne Type I faible-`L3` contrôle le champ localisé, la pression faible-
`L^(3/2)` dans la jauge de Riesz et les termes d'ordre zéro. Elle ne contrôle
pas, sans nouveau lemme, les commutateurs de diffusion et de dilatation dans
un espace négatif critique. Même une telle borne produirait une limite forcée,
pas le problème ancien non forcé requis par les rigidités usuelles.

La veille ajoute Saari–Schwarzacher sur les inverses de divergence mobiles,
Wolf et Kwon sur la pression locale, Breit sur la régularité au bord mobile,
et la prépublication forcée de Zhang (`0180`–`0184`). Le catalogue atteint
184 sources. Le rayon parabolique viole l'hypothèse de vitesse de bord
`L3_t` de Breit, et aucune source ne fournit l'annulation critique manquante.

## Cycle 0043 — la croissance haute fréquence disparaît dans la norme négative

Geißert–Heck–Hieber étend l'opérateur exact de Bogovskii sur domaine
lipschitzien de `W_0^(s,p)` vers `W_0^(s+1,p)` pour
`s>-2+1/p`. Costabel–McIntosh identifie les opérateurs régularisés supportés
comme pseudodifférentiels d'ordre `-1`, avec échelle de régularité sans perte
sur une géométrie fixe. Ces deux résultats permettent de choisir le même
inverse exact pour lequel `[Delta,B M_a]` est d'ordre zéro et
`[D,B M_a]` d'ordre `-1`.

La conséquence interne est une borne de la force projetée complète dans

```text
X=L1+div L^(3/2,infinity),
||F_sol||_X<=C[M²+(1+|kappa|)M].
```

Le mode pure-swirl haute fréquence vérifie simultanément une croissance
`Theta(N)` en `L2` et un budget uniforme dans `X`. Il élimine donc la norme
positive terme à terme comme test du verrou, sans rendre la force petite.

Le catalogue atteint 185 sources après ajout de la source négative de
Geißert–Heck–Hieber. Le nouveau trou n'est plus la bornitude instantanée :
il est la compacité dans un espace non réflexif, puis la rigidité avec force
critique ou l'échappement contrôlé de la couronne à l'infini.

## Cycle 0044 — fuite locale critique, obstruction globale

Pour une troncation solénoïdale sur la couronne externe
`A_L={L<|y|<2L}`, la conjugaison exacte de Bogovskii conserve uniformément
la borne faible-`L3`. Sur tout compact `B_rho`, `L>=2rho`, l'équation
renormalisée donne exactement

```text
F_L=P div(Z_L tensor Z_L-U tensor U).
```

Le tenseur entre parenthèses est nul dans `B_L` et uniformément borné dans
`L^(3/2,infinity)`. Le noyau non local de `P div` est une troisième dérivée
du potentiel newtonien, homogène de degré `-4`; une somme sur couronnes
donne, pour tout multi-indice spatial `alpha`,

```text
||partial^alpha F_L||_Linf(B_rho)
  <= C_alpha(1+C_Q^2)M^2 L^(-3-|alpha|).
```

La force disparaît donc dans `C^infinity_x,loc`, uniformément sur la fenêtre
temporelle. Bradshaw–Tsai (`0186`) source le gain lointain de pression par
soustraction de jauge; Wolf (`0181`) et Kwon (`0182`) sourcent les corrections
locales. La borne Lorentz complète reste une dérivation interne auditée, pas
un théorème cité.

Cette fuite est strictement locale. Un témoin pure-swirl critique donne pour
la force complète, si le drift `kappa` est non nul,
`||F_L||_(L1+div L^(3/2,infinity))>=c|kappa|L^2-C`. Il réfute la convergence
globale dans cet espace tout en restant compatible avec la disparition sur
les compacts.

Le catalogue atteint 186 sources. Le verrou suivant est un ledger de
compacité locale : dérivée temporelle, pression, passage du produit,
inégalité d'énergie locale et trace non triviale. Même après ce passage, il
faut dérenormaliser exactement le drift puis traiter la rigidité des solutions
anciennes faible-`L3`; aucune de ces arêtes n'est fermée par ce cycle.

## Mise à jour 2026-08-15 — cycle 0045, compacité locale adaptée

Sous la borne Type I uniforme faible-`L3`, la pression globale de Riesz est
uniformément faible-`L^(3/2)`, donc localement `L^(4/3)`. Pour les champs
tronqués lisses dont la force disparaît dans `C^infinity_x,loc` uniformément
en temps, un test par cutoff donne, après absorption et remplissage des
trous, une borne uniforme

```text
Z_j dans L^infinity_tL2_x,loc inter L2_tH1_x,loc.
```

Simon produit alors la convergence forte `L2_loc`; la borne parabolique
`L^(10/3)_loc` l'améliore en forte `Lq_loc` pour tout `q<10/3`, notamment
`L3`. Le produit converge fortement dans `L^(3/2)_loc`. La décomposition de
pression en partie de Riesz proche et reste harmonique permet de passer
l'inégalité d'énergie locale : la limite est faible adaptée pour l'équation
renormalisée non forcée avec drift.

Ce progrès ne conserve pas la non-trivialité terminale. Simon ne donne que
`C_tH^-1_loc`; une minoration de norme critique ou `L2` à une tranche peut
disparaître par concentration ou oscillation. Il faut un moment contre un
test fixe, une trace fortement compacte ou un théorème de persistance des
singularités dont les hypothèses soient réellement vérifiées.

Albritton–Barker 2020 et Barker–Seregin–Šverák 2018 sont ajoutés comme
`NS-SRC-0187`–`0188`. Le corpus atteint 188 sources. Aucun résultat du cycle
ne dérenormalise encore la limite, ne la rend non triviale, ni ne résout une
branche du problème Clay.

## Mise à jour 2026-08-15 — cycle 0046, non-trivialité intégrée Type I

La porte de trace du cycle 0045 était surdimensionnée pour la seule
non-trivialité. Barker–Prange (`0146`) concentre la quasi-norme faible-`L3`
au point singulier fixe pour tout temps tardif; sous la borne globale du
programme, `r_0=infinity` et la fenêtre commence à zéro. L'horloge mobile

```text
R²=4(T_*-t)/S_w^*(C_MM),
d sigma/dt=R^-2,
d(log R)/d sigma=-kappa,
kappa=2/S_w^*(C_MM)
```

transporte cette minoration dans le même `B_1` pour presque tout temps de
toute fenêtre renormalisée fixe. Comme `Q_(L_j)=I` dans `B_1`,

```text
K_3(Z_j(s);B_1)>gamma_w
```

sur toute la fenêtre. La forte `L3_loc` du cycle 0045 et l'inégalité optimale
`K_3(f;B_1)^3<=integral_(B_1)|f|³` donnent alors

```text
integral_(J x B_1)|Z|³>=|J|gamma_w³>0.
```

La limite ancienne renormalisée est non triviale sans compacité forte d'une
tranche. Une tranche non nulle peut être choisie après la limite et placée en
zéro par translation de l'équation autonome; cela ne prouve ni que l'ancien
endpoint est non nul, ni que la limite y reste singulière.

Le claim interne
`NS-TYPE-I-PERSISTENT-CAPTURE-SPACETIME-NONTRIVIALITY` reste
`COMPUTATION_ONLY`. Aucune source nouvelle n'est ajoutée : le corpus reste à
188. Le verrou actif devient la dérenormalisation exacte de l'équation avec
drift, puis la classification ou rigidité de la classe ancienne obtenue.

## Mise à jour 2026-08-15 — cycle 0047, classe ancienne standard exacte

La conjugaison du drift est maintenant calculée dans les distributions. Si
`r=exp(-kappa s)`, `tau=(1-r²)/(2kappa)`, `x=x_0+ry`,
`v=r^-1Z` et `q=r^-2Pi`, alors `s in (-infinity,0]` correspond exactement à
`tau in (-infinity,0]` et

```text
N_renormalise[Z,Pi]=r³ N_standard[v,q],
div_y Z=r² div_x v,
L_renormalise=r^4 L_standard.
```

Le jacobien `dx d tau=r^5dy ds` transforme un test faible par le poids `r²`
et un test d'énergie locale par le poids positif `r`. L'inégalité locale
d'énergie est conservée sans résidu. Une extraction faible-étoile globale du
produit dans `L-infinity L^(3/2,infinity)`, identifiée par la forte `L3_loc`,
conserve aussi la jauge `Pi=R_iR_j(Z_iZ_j)`. La quasi-norme faible-`L3` est
exactement invariante et la non-trivialité espace–temps persiste.

La sortie exacte est une solution ancienne standard non triviale **faible
adaptée locale**, uniformément faible-`L3`, avec pression globale de Riesz.
Elle n'est pas automatiquement Leray–Hopf, local-energy avec trace forte,
mild, bornée ou singulière au temps zéro. Albritton–Barker (`0189`) exige
mildness et bornitude pour son équivalence Type I, ou mildness et `L3` fort
sur une suite reculée pour son Liouville. Le corpus atteint 189 sources;
aucun théorème audité ne rigidifie la classe faible-`L3` obtenue.

Le claim `NS-TYPE-I-DERENORMALIZED-ANCIENT-LOCAL-SUITABLE` reste
`COMPUTATION_ONLY`. `GAP-TYPE-I-DERENORMALIZATION-CLASS` est fermé au statut
interne; le verrou devient
`GAP-TYPE-I-ANCIENT-WEAK-L3-RIGIDITY-OR-MILDNESS`.

## Mise à jour 2026-08-15 — cycle 0048, Duhamel endpoint faible-étoile

Sur toute bande finie `[t_0,t_1]`, la solution ancienne standard du cycle
0047, supposée distributionnelle, solénoïdale, à pression globale de Riesz et
uniformément bornée dans `L^(3,infinity)`, possède un représentant
`C_w*([t_0,t_1];L^(3,infinity))`. La projection globale de l'équation fournit
la formule de Duhamel pour tout `s<t`.

La divergence logarithmique de l'estimation ponctuelle
`||S(h)P div||_(L^(3/2,infinity)->L^(3,infinity))~h^-1` ne détruit pas ce
raccord. Le lemme intégré de Yamazaki (`NS-SRC-0118`), réénoncé explicitement
par Taniuchi, définition 1 et lemme 7 (`NS-SRC-0190`), construit le terme
quadratique comme intégrale faible-étoile de Gelfand dans
`L^(3,infinity)`, avec borne `C M^2` indépendante de la longueur temporelle.
Cette borne n'est ni une intégrale de Bochner, ni une petitesse de court
temps, ni une continuité forte dans l'espace critique.

Dans les espaces sous-critiques, le noyau d'Oseen donne pour
`3/2<p<3`

```text
||B(v,v)(t)||_p <= C_p M^2 (t-t_0)^((3-p)/(2p)).
```

En particulier le correcteur calorique canonique appartient à `C_tL2_x`,
a une trace forte nulle et vérifie `||w(t)||_2<=CM^2(t-t_0)^(1/4)`. Il manque
encore `w in L2_tHdot1_x` et l'inégalité d'énergie perturbée globale de
Barker–Seregin–Šverák (`NS-SRC-0188`). La définition mild publiée de
Taniuchi exige par ailleurs `C_tL^(3,infinity)` en norme; les classes mild
bornées de KNSS et Albritton–Barker exigent davantage la bornitude spatiale.

Le témoin solénoïdal homogène
`U=(-x_2,x_1,0)/|x|^2` a exactement
`K_3(U)^3=pi^2/4` et une énergie `L2(B_R)^2=(8pi/3)R`; sa queue radiale ne
devient pas petite en faible-`L3`. Il réfute un split énergétique naïf, sans
être une solution Navier–Stokes. La prépublication récente de Jarrín
(`NS-SRC-0191`) requiert donnée `L2`, trace forte et contrôle Morrey
sous-critique; elle ne ferme pas le raccord ancien endpoint.

Le corpus atteint 191 sources et le registre 86 claims. Le claim
`NS-WEAK-L3-DUHAMEL-L2-CORRECTOR` reste `COMPUTATION_ONLY`. Le verrou actif
est raffiné en `GAP-TYPE-I-RELATIVE-ENERGY-GLOBALIZATION`.

## Mise à jour 2026-08-15 — cycle 0049, globalisation de l'énergie relative

Sur toute bande finie `[t_0,t_1]`, ajoutons aux sorties du cycle 0048 la
suitability locale de `v` et la jauge globale
`q=R_iR_j(v_iv_j)`. La combinaison de l'inégalité locale d'énergie de `v`,
de l'égalité calorifique pour `V=S(t-t_0)v(t_0)` et de l'identité croisée
donne une inégalité locale relative pour `w=v-V`, sans test global
prématuré par `w`.

Le taux indépendant `||w(t)||_2<=CM²(t-t_0)^(1/4)` rend intégrables les
deux sources critiques :

```text
||V||_4^4 <= CM^4(t-t_0)^(-1/2),
||V||_4^8||w||_2² <= CM^12(t-t_0)^(-1/2).
```

Une première passe de cutoff absorbe le flux total grâce à
`q in L^(3/2,infinity)` et à Sobolev local, avec reste `O(R^-1)` indépendant
du rayon. Elle donne `w in L2_t Hdot1_x`. Une seconde passe, sans majorer le
transfert signé, donne l'inégalité globale perturbée

```text
||w(t)||_2²+2 integral_(t_0)^t||nabla w||_2²
 <=2 integral_(t_0)^t integral
      (V tensor w+V tensor V):nabla w.
```

Les clauses énergétiques laissées ouvertes dans la classe scindée de
Barker--Seregin--Sverak (`NS-SRC-0188`) sont ainsi fermées au statut interne
sur chaque bande finie. La constante dépend de sa longueur; aucun passage
uniforme `t_0->-infinity`, continuité forte faible-`L3`, mildness bornée ou
rigidité ancienne n'en découle. `FAIL-NS-0085` montre que la suitability et
le contrôle Riesz ne peuvent être retirés : `L2 inter L^(3,infinity)` seul
peut porter un flux cubique de cutoff non nul à toutes les grandes échelles.

Le corpus passe à 192 sources et le registre à 87 claims. Le verrou actif se
scinde en `GAP-TYPE-I-BSS-TO-STRONG-MILD-CONTINUITY` et
`GAP-TYPE-I-BSS-ANCIENT-RIGIDITY`.

## Mise à jour 2026-08-15 — cycle 0050, cocycle et obstruction quotient

Pour `s<r<t`, les correcteurs canoniques issus d'une même solution ancienne
vérifient exactement

```text
g_(s,t)=g_(r,t)+S(t-r)g_(s,r).
```

La transition est calorifique et conserve exactement son énergie initiale.
Lorsque `s->-infinity`, le fond `S(t-s)v(s)` tend vers zéro localement; une
seule sous-suite uniformément bornée de `g_(s,r)` dans `L2` forcerait donc
`v(r) in L2(R3)`. Le taux disponible `O((r-s)^(1/4))` ne fournit pas cette
porte.

Le quotient algébrique
`L^(3,infinity)/(L2 inter L^(3,infinity))` n'est pas séparé; le quotient de
Banach correct utilise la fermeture du dénominateur. Dans les deux objets, le
profil `U=(-x_2,x_1,0)/|x|²` et sa variante lisse `U_sharp` portent une classe
fixe non nulle. Ils satisfont

```text
||(I-S(h))U||_2=C_U h^(1/4),
C_U²=(8pi^(5/2)/3)(1-1/sqrt(2)),
```

et produisent un défaut exact de commutation des limites égal à `8pi/3`.
`U_sharp` appartient à `tilde L^(3,infinity) inter Hdot1`, et ses incréments
sont énergétiques sur toute bande finie. Aucun profil n'est une solution
Navier--Stokes : une circulation azimutale non nulle exclut une pression
compensatrice.

Taniuchi (`NS-SRC-0190`) impose déjà la mildness cohérente et des conditions
au passé dans ses rigidités. Bradshaw--Hudson (`NS-SRC-0193`) confirme le
rebasage fini dans une classe supercritique, sans uniformité ancienne. Le
corpus atteint 193 sources et le registre 88 claims. Le verrou de cohérence
algébrique est fermé; restent `GAP-TYPE-I-ANCIENT-QUOTIENT-RIGIDITY` et
`GAP-TYPE-I-BSS-ENERGY-TAIL-TIGHTNESS`.

## Mise à jour 2026-08-15 — cycle 0051, saturation PDE et critère infrarouge

Jia--Sverak (`NS-SRC-0194`) construisent une solution exacte forward
auto-similaire de Leray locale depuis
`a=(-x_2,x_1,0)/|x|²`. Pour son profil relatif
`W=mathcal U-S(1)a`, la décroissance publiée donne
`W in L2 inter Hdot1`. Le calcul
`curl((a dot nabla)a)=4x_3(-x_2,x_1,0)/|x|^6` exclut `W=0`; par conséquent

```text
||u(t)-S(t)a||_2=||W||_2 t^(1/4),
integral_0^T||nabla(u-S(t)a)||_2²=2T^(1/2)||nabla W||_2².
```

La norme faible-`L3` reste uniforme. Cette vraie dynamique réfute donc toute
borne de correcteur forward, uniforme en horizon et dépendant seulement de
la norme critique. Les translations temporelles sont toutefois une famille
de solutions forward, non les restrictions d'une même solution ancienne;
la donnée est singulière et d'énergie infinie, donc non Clay.

Indépendamment, le Duhamel dyadique de toute ancienne conditionnelle donne

```text
||Delta_jg_(s,r)||_2
 <=CM²2^(-j/2)min(1,(r-s)2^(2j)),
sup_(s<r)sum_(j>J)||Delta_jg_(s,r)||_2²<=CM^4 2^(-J).
```

Toutes les hautes fréquences sont ainsi uniformément fermées. La porte
`liminf_s||g_(s,r)||_2<infinity` est équivalente à la bornitude de la somme
des blocs `j<=J` pour un seuil fixe, ou à celle de `||S(a)g_(s,r)||_2` pour
un unique `a>0` fixe. Le verrou est exactement l'annulation infrarouge du
stress sur une même orbite ancienne.

La veille ajoute `NS-SRC-0194` à `NS-SRC-0202`, couvrant saturation SS/DSS,
décroissance spatiale, espaces Herz/Besov et un Liouville axisymétrique à
queue imposée. Le corpus atteint 202 sources et le registre 90 claims. Les
deux nouveaux claims restent `COMPUTATION_ONLY`. `FAIL-NS-0087` clôt la
borne forward universelle; restent
`GAP-TYPE-I-SINGLE-ANCIENT-ORBIT-RECURRENCE` et
`GAP-TYPE-I-ANCIENT-INFRARED-STRESS-DEPLETION`.

## Mise à jour 2026-08-15 — cycle 0052, primitive signée du flux de base

Pour `r<T` et un filtre calorifique fixe `a>0`, le correcteur ancien
`g_(s,r)=v(r)-S(r-s)v(s)` vérifie, avec `G_a=S(a)g_(s,r)`,

```text
E_a(s;r)=||G_a(s;r)||_2²
        =integral_s^r Phi_a(sigma;r)dsigma,

Phi_a(s;r)=2 integral_R3 (v tensor v)(s)
                       :nabla S(2a+r-s)g_(s,r) dx.
```

Le signe, le facteur deux et le double lissage ont été contrôlés
indépendamment. Cette identité est exactement équivalente au critère
calorifique du cycle 0051 : une seule suite `s_n->-infinity` sur laquelle la
primitive signée reste bornée suffit à obtenir `v(r) in L2`. Elle ne demande
ni convergence impropre, ni variation totale finie.

La majoration disponible après valeur absolue est seulement

```text
|Phi_a(s;r)|<=CM^4(a+r-s)^(-3/4)
                    [(a+r-s)^(1/4)-a^(1/4)],
```

donc d'ordre `(r-s)^(-1/2)` au passé. Son intégrale reproduit la croissance
énergétique `(r-s)^(1/2)` et ne ferme rien. Une triade exacte sur `T3`
montre en outre que l'incompressibilité et la projection de Leray
n'imposent ni signe ni coercivité instantanés; la phase inverse le transfert
et une autre polarisation annule la sortie. Ce certificat ne construit pas
une orbite ancienne sur `R3`, et son ledger sur le temps visqueux décroît
comme `N^(-2)`.

La littérature primaire ferme séparément le profil backward
auto-similaire **exact** dans faible-`L3` : le théorème de
Guevara--Phuc annule tout profil de Leray faible dans
`W1,2_loc inter L^(3,infinity)`, et Chae--Wolf couvre une gamme Lorentz plus
large. Cette rigidité ne s'étend pas à une récurrence faible-étoile, modulée
ou discrètement auto-similaire sans hypothèses supplémentaires.

Le corpus atteint 205 sources et le registre 92 claims. Le verrou actif est
raffiné en `GAP-TYPE-I-ANCIENT-SIGNED-BASE-FLUX-CANCELLATION`.

## Mise à jour 2026-08-15 — cycle 0053, sous-suite stationnaire interdite

Soit `Z` la limite ancienne renormalisée du pipeline Type I, suitable locale,
uniformément bornée dans `L^(3,infinity)` et munie de la capture persistante
du cycle 0046. Pour un rayon `R`, le défaut distributionnel `D_R(s)` mesure
`partial_s Z` sur la fenêtre `[s-1,s]` contre les tests de
`W_0^(1,(3,1))(B_R)`. Ce choix Lorentz est obligatoire : le stress et la
pression ne sont a priori que dans `L^(3/2,infinity)`.

Si `D_R(s_n)->0` pour tous les rayons le long d'une même suite reculée, la
compacité suitable locale donne une limite forte `L3_loc`, indépendante du
temps. La capture la rend non nulle, tandis que la jauge globale de Riesz et
la limite d'énergie donnent un profil de Leray
`W1,2_loc inter L^(3,infinity)`. Après normalisation du coefficient positif
du drift, Guevara--Phuc impose que ce profil soit nul. Par diagonalisation
monotone, il existe donc `R_*`, `epsilon_*>0` et `S_*<0` tels que

```text
D_(R_*)(s)>=epsilon_* pour tout s<=S_*.
```

Le résultat est une dérivation IA conditionnelle au paquet de compacité déjà
construit, pas une conséquence du seul faible-`L3`. Les contre-tests exacts
montrent séparément que concentration critique, fuite spatiale, récurrence
non stationnaire et extractions non emboîtées invalident les raccourcis
correspondants. Le corpus reste à 205 sources; le registre passe à 93 claims.
Le verrou est raffiné en
`GAP-TYPE-I-RENORMALIZED-GENERATOR-TO-SIGNED-FLUX`.

## Mise à jour 2026-08-15 — cycle 0054, flux radial et activité tangentielle

Pour la même ancienne renormalisée, l'horloge exacte
`rho=exp(-kappa s)`, `tau=(1-rho^2)/(2kappa)` et le filtre physique fixe
`a>0` donnent

```text
B_s=(a-tau)/rho^2
   =1/(2kappa)+(a-1/(2kappa))rho^(-2),
L_kappa Z=partial_s Z-Delta Z+kappa(1+y dot nabla)Z.
```

Le correcteur du temps terminal zéro satisfait, presque partout,

```text
J_a(s):=rho^2 I_a(tau(s);0)
       =2 <G_a,T_rho S(B_s)L_kappa Z>
       =-partial_s ||G_a||_2^2.
```

La pression est conservée par la projection de Leray globale et le pairing
final est celui de `L^(3/2,infinity)` avec `L^(3,1)`. Le temps `B_s` reste
uniformément entre `a` et `1/(2kappa)`; la densité change toutefois par le
facteur d'horloge `rho^2`.

Cette identité ne raccorde pas le défaut local `D_R` au flux. `D_R` mesure
une norme intégrée de `partial_s Z`, sur une fenêtre et après supremum sur
tous les tests locaux. `J_a` mesure à un instant un unique appariement
global et signé du résidu complet `L_kappa Z` contre un test dépendant de la
trajectoire terminale. Un contre-modèle hilbertien exact conserve
`||G'||^2>=1/2` tout en ayant `J=-d||G||^2/ds`, `integral J=1` et
`J(s)->0` au passé. Sa réalisation solénoïdale sur `T3` a un résidu
Navier--Stokes non nul : elle réfute seulement la coercivité fonctionnelle,
pas un théorème PDE.

Le registre passe à 94 claims, sans nouvelle source. Pineau--Vicol v2 ferme
des orbites RSS Type I pour rotation suffisamment petite ou grande, mais
laisse le régime intermédiaire ouvert et n'obtient pas son hypothèse
ponctuelle Type I depuis le seul faible-`L3`. Le verrou devient
`GAP-TYPE-I-RENORMALIZED-TANGENTIAL-ACTIVITY-CLASSIFICATION`.

## Mise à jour 2026-08-15 — cycle 0055, orbites relatives exactes

Pour l'opérateur autonome renormalisé

```text
F_kappa(U)=-Delta U+P div(U tensor U)+kappa(1+y dot nabla)U,
```

fixons l'action de rotation centrée
`Q_theta U(y)=R_theta U(R_(-theta)y)` et son générateur
`mathcal R U=J U-(J y dot nabla)U`. L'opérateur est exactement équivariant,
pression de Riesz comprise.

Si une solution distributionnelle a la forme
`Z(s)=Q_(theta(s))U` avec `theta in W^(1,1)_loc`, alors

```text
theta'(s) mathcal R U+F_kappa(U)=0 p.p.
```

Deux branches seulement subsistent. Si `mathcal R U=0`, l'orbite est
stationnaire et `F_kappa(U)=0`. Sinon, un test compact détectant
`mathcal R U` force `theta'=alpha` constant presque partout et `U` satisfait
l'équation RSS exacte. Une symétrie de rotation discrète ne crée aucune
vitesse variable sous une phase absolument continue.

Avec suitability locale, le profil appartient à `W1,2_loc`. La branche
stationnaire faible-`L3` est alors annulée par Guevara--Phuc. La branche RSS
non stationnaire n'est exclue par Pineau--Vicol v2 que sous leur borne Type I
ponctuelle et pour rotations suffisamment petites ou grandes. Faible-`L3`
ne fournit pas cette borne, et la rotation intermédiaire reste ouverte.

Le contre-audit exact montre qu'un résidu `epsilon` contrôle seulement
`|beta(s)-beta(t)| ||mathcal R U||<=2epsilon`. Toute version compacte exige
donc une borne des vitesses et une alternative quantitative lorsque le
générateur rotationnel dégénère. Le registre passe à 95 claims, le corpus
atteint 208 sources et le verrou devient
`GAP-TYPE-I-APPROXIMATE-ROTATION-MODULATION-COMPACTNESS`.

## Mise à jour 2026-08-15 — cycle 0056, modulation bornée compactifiée

Soit `Z_n` une suite de solutions renormalisées sur `R3 x I`, de viscosité
un et sans force, convergeant fortement dans `L3_loc`, munie d'un ledger
suitable uniforme et d'une borne globale faible-`L3`. Si

```text
sup_n ||beta_n||_(L-infinity(I))<=B,
partial_s Z_n-beta_n mathcal R Z_n ->0 dans D',
```

alors, après extraction, `beta_n` converge faible-étoile vers `beta` et le
produit modulé passe à la limite. Le point exact est le lemme
faible-étoile borné fois fort `L1`; le générateur est déplacé sur le test par
`mathcal R^*phi=-Jphi+(Jy dot nabla)phi`. On obtient

```text
partial_s Z=beta(s) mathcal R Z,
Z(s)=Q_(theta(s))U,
theta'=beta.
```

L'autonomie du système et le cycle 0055 donnent ensuite la dichotomie : si
`mathcal R U=0`, la limite est stationnaire; sinon `beta=alpha` presque
partout et `U` satisfait l'équation RSS exacte. Une capture cylindrique
persistante et le Liouville stationnaire publié éliminent la première
branche, mais pas la RSS tournante faible-`L3`.

La conclusion suitable demande des constantes uniformes locales d'énergie,
de dissipation et de pression; le caractère suitable de chaque terme pris
isolément ne suffit pas. Des contre-modèles dyadiques exacts réfutent les
versions faible fois faible et vitesse non bornée. Le registre passe à 96
claims; deux sources adjacentes sur la reconstruction de phase sont ajoutées
et le corpus atteint 210.
Le verrou devient
`GAP-TYPE-I-UNBOUNDED-ROTATION-MODULATION-OR-RSS-RIGIDITY`.

## Mise à jour 2026-08-15 — cycle 0057, collapse des rotations rapides adiabatiques

Sur chaque fenêtre compacte `J`, posons `q_n=1/beta_n`. Sous forte
convergence `L3_loc`, borne uniforme `L-infinity_tL2_loc`,

```text
ess inf_J |beta_n| -> infinity,
||q_n||_infinity+Var_J(q_n) ->0,
r_n=partial_sZ_n-beta_n mathcal RZ_n ->0
    dans L1_t H^(-1)_loc,
```

le test `q_n phi` donne une estimation à trois constantes :

```text
|<mathcal RZ_n,phi>|
 <=C||q_n||_infinity||partial_sphi||
   +C Var(q_n)||phi||
   +||q_n||_infinity||r_n||||phi||_(H1).
```

Ainsi `mathcal RZ=0`. La moyenne de Haar `mathcal A` satisfait
`mathcal A mathcal R=0`; elle transforme le défaut nul en
`partial_s mathcal A Z=0`. Comme `mathcal A Z=Z`, la limite est
stationnaire. Avec le ledger suitable uniforme, la pression de Riesz, la
borne faible-`L3` et la capture, Guevara--Phuc impose simultanément `Z=0` et
`Z!=0`. Une famille compacte capturée de RSS exactes avec
`|alpha_n|->infinity` est donc exclue conditionnellement.

La variation du réciproque est essentielle à l'argument. Une stroboscopie
exacte à vitesses positives `N` et `N^4` a `||q_N||_infinity=1/N`, mais
`Var(q_N)~2N`; ses passages rapides ont mesure `O(N^-2)` et l'orbite converge
fortement vers un profil non axisymétrique. Ce modèle n'est pas une solution
Navier--Stokes. Le registre passe à 97 claims. Le verrou devient
`GAP-TYPE-I-FAST-ROTATION-STROBOSCOPIC-OR-RSS-RIGIDITY`.
