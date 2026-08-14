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
| Koch–Nadirashvili–Seregin–Šverák 2009 | solutions anciennes bornées | théorèmes de Liouville en classes particulières, notamment axisymétriques | le Liouville général 3D borné reste hors de portée |
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

L'extraction détaillée ESS/GKP précise toutefois que la pression **lointaine
centrée** n'est pas un verrou supplémentaire lorsque la suite est globalement
bornée dans `L³` : Hölder donne une queue pondérée `O(A^-3)`. En revanche,
l'énergie seule n'assure pas cette tension après zoom, et cette estimation ne
donne aucune compacité forte pour la pression proche.

Un scénario Type I conserve une quantité critique de vitesse ou de vorticité à
l'échelle naturelle; un scénario Type II la laisse croître plus vite. Les
résultats Type I et plusieurs résultats au bord ne se transfèrent pas à un Type
II intérieur sans une nouvelle borne ou une nouvelle rigidité. La
prépublication de Seregin `arXiv:2606.29468` exclut certaines limites Type II
sous hypothèses supplémentaires; elle ne résout pas l'alternative Clay.

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

Le résultat Hou–Wang–Yang est accompagné d'un calcul par intervalles pour un
profil auto-similaire et un mode instable. Le code public annonce Julia 1.11 et
environ 800 Go de mémoire; le dépôt consulté ne fournit pas de manifeste Julia
effectivement épinglé. Le calcul n'a pas été reproduit localement. Même si la
preuve prépubliée est correcte, l'implication vers Clay s'arrête à la donnée
initiale singulière. Régulariser cette donnée déclenche l'unicité faible–forte
sur l'intervalle classique et détruit l'invariance auto-similaire exacte.

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
| stabilité | passage d'un profil singulier à des données Clay | théorème robuste respectant unicité faible–forte |

## Conclusion falsifiable

La bibliographie ferme de nombreuses classes conditionnelles mais ne fournit
pas l'arête « énergie -> borne critique ». La première campagne du laboratoire
testera des arêtes plus petites : (i) stabilité d'une construction singulière
sous désingularisation, (ii) impossibilité de déplétions triadiques universelles,
et (iii) compatibilité d'un profil renormalisé avec la viscosité. Tout résultat
est raccordé explicitement au graphe et peut être abandonné sans modifier
l'énoncé Clay.
