# Registre des échecs utiles — Navier–Stokes 3D

Ce registre est append-only : corriger une entrée consiste à ajouter un statut
ou une nouvelle affirmation, jamais à supprimer l'échec.

## `FAIL-NS-0001` — Transfert mono-échelle d'un profil Euler IA vers NS

- Date : 2026-08-14 (ré-audit d'une dérivation historique).
- Cible : profil de blow-up incompressible de type
  `u=tau^lambda U(x/tau^(1+lambda))`.
- Attaque : comparer exactement viscosité et inertie après remise à l'échelle.
- Résultat : le ratio est `nu C_U tau^(-1-2lambda)`. Pour
  `lambda>-1/2`, il diverge; le terme visqueux n'est pas perturbatif.
- Portée : réfute seulement le transfert mono-échelle direct pour ces exposants,
  pas l'existence de tout profil NS ni de toute construction multi-échelle.
- Statut : `REFUTED` pour l'arête de transfert; calcul rationnel à reproduire
  dans le nouveau dépôt.

## `FAIL-NS-0002` — Déplétion universelle par divergence et hélicité nulle

- Date : 2026-08-14 (ré-audit d'une expérience historique).
- Cible : une borne `|Pi_N| <= epsilon_N N E^(3/2)`, `epsilon_N -> 0`, valable
  pour tout polynôme trigonométrique divergence-free d'hélicité globale nulle.
- Attaque : triade exacte `a=(N,0,0)`, `b=(0,N,0)`, `c=(N,N,0)` avec phases
  signées et modes conjugués.
- Résultat : `E=6`, `Z=9N²`, hélicité `0`, mais `Pi_N=-2 sigma N`; le ratio
  normalisé ne tend pas vers zéro.
- Portée : ne réfute pas une déplétion avec cohérence locale de la direction de
  vorticité, intermittence contrôlée ou hypothèses dynamiques supplémentaires.
- Statut : contre-exemple algébrique fini à reproduire avant claim canonique.

## `FAIL-NS-0003` — Non-unicité faible présentée comme blow-up Clay

- Date : 2026-08-14.
- Cible : implications depuis Buckmaster–Vicol, Albritton–Brué–Colombo ou
  Hou–Wang–Yang vers une alternative (A)–(D).
- Attaque : vérifier force, donnée initiale, classe de solution et conclusion.
- Résultat : les constructions diffèrent respectivement par la classe
  énergétique, la présence d'une force, ou une donnée initiale singulière.
  Aucune n'exclut à elle seule une solution globale lisse pour toute donnée
  Clay.
- Statut : implication réfutée; les théorèmes ou prépublications sources ne sont
  pas réfutés.

## `FAIL-NS-0004` — Exclusion auto-similaire assimilée à exclusion de blow-up

- Date : 2026-08-14.
- Cible : conclure la régularité globale du théorème de Liouville pour profils
  rétrogrades `L³`.
- Attaque : comparer les quantificateurs à Type II, auto-similarité discrète et
  concentration multi-échelle.
- Résultat : le théorème élimine une sous-classe; les autres scénarios ne
  satisfont pas ses hypothèses.
- Statut : implication réfutée.

## `FAIL-NS-0005` — Grandes normes de cutoff assimilées à une obstruction dynamique

- Date : 2026-08-14.
- Cible : déduire de la divergence de `L^3` et `H^1` d'une famille lissée que
  son temps d'existence s'effondre ou qu'aucune stabilité dynamique ne subsiste.
- Attaque : solutions de cisaillement exactes sur `T^3`,
  `u_N=a_N exp(-nu N²t) sin(Nx_2)e_1`, pour lesquelles transport et pression
  s'annulent.
- Résultat : avec `a_N=(log N)^(1/3)` et
  `epsilon_N=[N²(log N)^(2/3)]^-1`, on a
  `||u_N(0)||_3^3` du même ordre que `log(1/epsilon_N)` et
  `||nabla u_N(0)||_2²` du même ordre que `epsilon_N^-1`, tout en ayant une
  solution globale lisse exacte.
- Portée : la coquille `r^-1` prouve la non-uniformité de certaines normes,
  mais pas une conséquence dynamique. Elle reste pertinente pour attaquer une
  preuve de stabilité dont la constante dépend précisément de ces normes.
- Statut : implication dynamique réfutée par la passe contradictoire séparée;
  le lemme radial restreint est conservé `COMPUTATION_ONLY`.

## `FAIL-NS-0006` — Énergie physique et séparation supposées suffisantes pour la pression

- Date : 2026-08-14.
- Cible : déduire d'une norme physique `L²` uniformément bornée et d'une distance
  rescalée `R_n->infinity` la disparition uniforme de la pression distante
  centrée.
- Attaque : paquets lisses compacts divergence-free avec
  `L_n=2^-6n`, `r_n=2^-7n`, moment `mu_n=2^-3n`, puis zoom NS à l'échelle
  `r_n`.
- Résultat : `||v_n||_2²=2mu_n->0` (énergie cinétique `mu_n`), mais le moment rescalé vaut
  `R_n^4`; la queue d'énergie pondérée tend vers `2` et
  `P_n(e_1)-P_n(0)->3/(4pi)`.
- Résidus : six familles d'identités d'échelle exactement nulles en fractions
  rationnelles pour `1<=n<=12`; la dépendance générale est symbolique.
- Portée : les champs sont des données Clay admissibles séparées, pas une même
  trajectoire NS. Le contre-profil ne réfute ni une tension critique supposée,
  ni un mécanisme dynamique de non-concentration.
- Statut : l'implication universelle depuis l'énergie seule est `REFUTED`;
  le critère positif de tension pondérée reste `COMPUTATION_ONLY`.

## `FAIL-NS-0007` — Convergence faible d'une trace assimilée à la compacité quadratique

- Date : 2026-08-14.
- Équation : Navier–Stokes incompressible 3D sur `T³`, viscosité `nu=1`, force
  nulle, solutions globales lisses et pression de moyenne nulle.
- Cible : déduire de bornes uniformes d'énergie et de dissipation, et de
  `u_N(t_N) weakly -> u` dans `L²` à des temps `t_N->0`, que
  `u_N tensor u_N -> u tensor u` et `p_N->p[u]` dans les distributions.
- Attaque : solution exacte issue de
  `psi_N=N^-1 sin(x_1)cos(Nx_2)` avec
  `t_N=log(2)/(N²+1)`.
- Résultat : `u_N(t_N) weakly ->0`, mais
  `u_N tensor u_N weakly ->diag((1/8)sin²(x_1),0,0)` et
  `p_N(t_N) weakly ->(1/16)cos(2x_1)`.
- Résidus : divergence, momentum, pression de Poisson, Laplacien et identité
  d'énergie sont exactement nuls pour `N=1,2,4,...,128`; les identités
  symboliques valent pour tout entier `N>=1`.
- Portée : le défaut vit dans une couche initiale `t_N~N^-2`. Pour tout temps
  fixe positif, la convergence est forte; la famille ne réfute ni la compacité
  d'Aubin–Lions intérieure, ni un passage à la limite espace-temps, ni une
  affirmation sur une donnée initiale fixée.
- Statut : implication universelle sur les traces mobiles `REFUTED`; la
  convergence forte `L³` reste un critère suffisant `COMPUTATION_ONLY`.

## `FAIL-NS-0008` — Module temporel faible assimilé à un module critique de trace

- Date : 2026-08-14.
- Équation : NS incompressible 3D; loi d'échelle sur `R³`, contre-test sur
  `T³`, `nu=1`, force nulle, solutions globales lisses.
- Cible : déduire des seules bornes uniformes
  `L^infinity_tL²_x intersection L²_tH¹_x` un semi-module uniforme
  `C_t^(1/4)L²_x` ou `C_t^(3/4)dot H^-1_x`, tous deux critiques.
- Attaque : la famille oscillatoire exacte du cycle 0004, observée entre `0`
  et `t_N=log(2)/(N²+1)`.
- Résultat : les deux quotients critiques croissent comme `N^(1/2)`. En
  revanche, le module énergétique `C_t^(1/4)dot H^-1` est uniformément borné
  et même décroît comme `N^(-1/2)` pour cette famille.
- Résidus : sept identités d'exposants, normes spectrales et puissances
  normalisées exactement nulles pour `N=1,2,4,...,128`; `log(2)` reste
  symbolique.
- Portée : réfute une estimation universelle depuis l'énergie, pas une
  équicontinuité supplémentaire imposée par minimalité, borne critique ou
  structure de premier blow-up.
- Statut : implication énergétique `REFUTED`; loi d'échelle et module faible
  positif conservés `COMPUTATION_ONLY`.

## Obstacle consolidé — `GAP-COMPACT-Q` sous énergie seule

Trois stratégies distinctes ont maintenant échoué sur la même tentative de
fermeture énergétique :

1. la pression distante après zoom n'est pas tendue (`FAIL-NS-0006`);
2. une trace faiblement convergente garde un défaut quadratique et de pression
   même pour des solutions NS exactes (`FAIL-NS-0007`);
3. le module temporel déduit de l'énergie perd une puissance d'échelle et ne
   contrôle aucun des deux modules critiques testés (`FAIL-NS-0008`).

Décision de pivot : ne plus chercher une compacité critique à partir de
l'énergie seule sans hypothèse structurelle nouvelle. L'axe actif suivant est
la rigidité des solutions anciennes et l'inventaire exact de la classe limite
réellement produite par un premier blow-up.

## `FAIL-NS-0009` — Ancienne à vitesse bornée adaptée à trace terminale nulle supposée rigide

- Date : 2026-08-14.
- Équation : NS incompressible 3D sur `R³ x (-infinity,0]`, `nu>0`, force
  nulle, sans frontière.
- Cible : conclure `u=0` de « lisse + ancienne + vitesse bornée + adaptée localement +
  `u(·,0)=0` » sans formule mild ni normalisation globale de pression.
- Attaque : `u=(-t/(1+t²))e_1` et
  `p=((1-t²)/(1+t²)²)x_1`.
- Résultat : la vitesse est bornée par `1/2`, non nulle à `t=-1`, la trace
  terminale est nulle et l'égalité locale d'énergie est satisfaite. Le gradient
  de pression affine porte exactement la variation temporelle.
- Résidus : divergence, convection, Laplacien, momentum, Poisson, énergie
  locale et identité de borne exactement nuls pour six temps rationnels; le
  défaut de formule mild entre `-1` et `0` vaut exactement `-1/2`.
- Pression : à `t=0`, `p=x_1` et son oscillation moyenne sur `[-R,R]³` vaut
  `R/2`; la pression n'est pas BMO et n'est pas la jauge Leray/Riesz.
- Portée : ne réfute pas KNSS ni un Liouville mild. La solution n'est ni dans
  `L²(R³)`, ni dans `L³(R³)`, ni décroissante; elle fixe seulement une hypothèse
  indispensable de jauge ou de mildness.
- Statut : Liouville faible/adapté sans jauge `REFUTED`; porte mild conservée
  `SOURCE_VERIFIED` dans la sous-classe spatialement constante.

## `FAIL-NS-0010` — Composition des propriétés ESS et KNSS

- Date : 2026-08-14.
- Cible : appliquer un Liouville « ancienne mild, globalement bornée en
  vitesse, non triviale et de trace terminale nulle » en prétendant que les
  ingrédients sont déjà transmis par les réductions classiques.
- Attaque : matrice exacte de treize propriétés pour ESS 2003, GKP v3, KNSS v1
  et Seregin `2606.29468v1`, avec inclusion de prémisses calculée sans flottant.
- Résultat : aucune chaîne unique ne vérifie le paquet. ESS porte la trace
  `L²_loc` nulle et `L∞_tL³_x`; KNSS porte mildness, borne ponctuelle et la
  normalisation opposée `|v(0,0)|=1`. Leur union à deux objets est l'unique
  couverture minimale du paquet hybride.
- Passe adverse : la limite ESS est en réalité éternelle et son témoin limite
  vaut `>=epsilon_*`; KNSS ne transmet aucune pression. Ces corrections ont été
  intégrées avant validation.
- Résidu : `assertion_failure_count=0`; aucune discrétisation PDE ni erreur
  flottante.
- Portée : ne réfute pas le Liouville hybride comme théorème abstrait. Réfute
  seulement son application sans lemme de raccord à l'une des quatre chaînes
  auditées.
- Statut : inférence de transfert `COMPUTATION_ONLY`, approche hybride
  abandonnée jusqu'à production d'une même limite satisfaisant toutes les
  prémisses.

## `FAIL-NS-0011` — Lei–Yang–Yuan employé comme support unique sans comparaison éditoriale

- Date : 2026-08-14.
- Cible : fermer seul le lemme ancien mild borné à trace nulle par le théorème
  1.1 publié de Lei–Yang–Yuan après extension mild au temps terminal.
- Attaque : lecture ligne à ligne de l'unique texte intégral accessible,
  `arXiv:2311.02429v1`, puis comparaison de ses métadonnées avec la notice
  éditeur IMRN.
- Résultat : trois anomalies ont été isolées dans `v1` : renvoi interne vers
  le mauvais numéro de corollaire, facteur `1/2` absent dans l'identité
  reliant `|nabla u_2|²`, `Delta|u_2|²` et `u_2 dot Delta u_2`, et discordance
  entre les poids `-k` et `-2k` dans l'énoncé et le début d'une preuve.
- Passe adverse : ces défauts paraissent localement réparables et ne
  constituent pas une réfutation de l'article publié. La version éditeur
  intégrale est sous contrôle d'accès et n'a pas pu être comparée ligne à
  ligne.
- Portée : seule la décision de faire de cette route le support **unique** est
  abandonnée. Le théorème publié reste un contrôle corroborant. La route
  principale du laboratoire passe par le lissage KNSS, la vorticité et
  l'unicité rétrograde ESS.
- Statut : `REVISE`; anomalie bibliographique conservée, résultat publié non
  réfuté.

## `FAIL-NS-0012` — Trace ESS forcée dans le zoom maximum KNSS par permutation des limites

- Date : 2026-08-14.
- Équation : NS incompressible 3D non forcé sur `R³`, viscosité `1`; zooms
  mild de temps records KNSS.
- Cible : obtenir une ancienne mild bornée, non triviale et de trace nulle en
  prétendant que les limites `k->infinity` et `s->0-` ne sont pas encore
  justifiées et pourraient être choisies dans l'ordre favorable.
- Attaque : recalcul du pairing sous zoom, estimations KNSS redémarrées jusqu'à
  `s=0`, puis test par couche terminale exacte à pression affine. Le recalcul
  montre que `s=0` correspond à `t_k`, tandis que le temps physique `T`
  correspond à `B_k=M_k²(T-t_k)>0`.
- Résultat : dans la vraie classe KNSS, `nabla v_k` et `partial_s v_k` sont
  uniformément bornés près de zéro. Les deux limites commutent localement et
  leur valeur commune au temps-record conserve `|v(0,0)|=1`; elle ne peut être
  nulle dans `D'`. Cela ne construit aucune trace à `T`. Une couche
  `e^(k²s)e_1` fait bien non-commuter les limites avec résidu
  PDE nul, mais elle n'est pas mild et son module temporel explose.
- Concentration : le zoom force au moins `pi/(48G³)` de masse `L³` dans une
  boule physique de rayon `1/(2GM_k)`. Une hypothèse de non-concentration
  critique exclut donc le blow-up au lieu de fournir un profil hybride non
  trivial.
- Résidu : zéro pour les identités d'échelle, la PDE affine et les neuf
  obligations encodées; aucun flottant ni discrétisation.
- Portée : réfute la permutation favorable au temps-record pour la
  normalisation maximum KNSS. Ne contrôle pas l'extrémité mobile `B_k`, ne
  réfute pas une autre extraction, une équivalence démontrée entre limites ESS
  et KNSS, ni tout argument de compacité–rigidité.
- Statut : `REFUTED` pour l'arête de permutation favorable; critère local `L³`
  conservé `COMPUTATION_ONLY`.

## Obstacle consolidé — paquet hybride ESS–KNSS

Trois stratégies distinctes ont maintenant traité le même verrou :

1. la matrice d'héritage montre que les propriétés ESS et KNSS appartiennent à
   deux objets (`FAIL-NS-0010`);
2. la rigidité du paquet abstrait est fermée conditionnellement : s'il était
   produit sur un même objet, celui-ci serait nul;
3. la permutation des limites au temps-record du zoom KNSS est impossible :
   la classe mild transmet au contraire une valeur non nulle, et expose que le
   vrai temps terminal est une extrémité mobile (`FAIL-NS-0012`).

Décision de pivot : suspendre la recherche d'une trace ESS à l'intérieur du
zoom maximum KNSS. Toute réouverture exige une nouvelle extraction ou un lemme
d'équivalence entre deux profils, pas un autre renommage de topologie.

## `FAIL-NS-0013` — Compacité critique d'une désingularisation depuis `L²` et `L^{3,infinity}`

- Date : 2026-08-14.
- Équation : aucune évolution; données initiales `C_c^infinity`,
  divergence-free sur `R³`, destinées à NS incompressible non forcé avec
  viscosité `1`.
- Cible : déduire un module uniforme de compacité forte `L³` de la convergence
  `L²` plus une borne uniforme `L^{3,infinity}` pour des cutoffs intérieurs
  d'un coeur homogène de degré `-1`.
- Attaque : champ tangent
  `a=(-x_2,x_1,0)/|x|²` et cutoffs radiaux plats aux échelles `epsilon` et
  `2epsilon`.
- Résultat : les données sont lisses, compactes et exactement
  divergence-free; leur distance `L²` tend vers zéro et leurs normes
  `L^{3,infinity}` sont uniformes, mais
  `||u_epsilon-u_(2epsilon)||_3³` est minorée par la constante positive
  `[e^(8/3)/(1+e^(8/3))]^3(3pi²/4)log(5/4)`.
- Résidus : antisymétrie, trace, tangence, constantes angulaires et facteurs
  radiaux exacts; zéro échec rationnel et zéro arrondi, transcendantes gardées
  symboliques.
- Passe adverse : la famille converge bien dans `L²`; le défaut ne réfute ni
  une stabilité à temps strictement positif, ni une constante dépendant de
  `L³`/`H¹`, ni un mécanisme dynamique propre au profil HWY. Les grandes normes
  ne fournissent aucune borne supérieure sur la durée forte.
- Portée : l'inférence fonctionnelle universelle est `REFUTED`. Le transfert
  non perturbatif des branches HWY reste ouvert et doit respecter
  l'unicité faible–forte.
- Artefact : `HWY-INNER-CUTOFF-GATE-1`.

## `FAIL-NS-0014` — Excitation générique du mode HWY impair par lissage symétrique

- Date : 2026-08-14.
- Équation : NS incompressible 3D non forcé sur `R³`, viscosité `1`; solution
  forte locale issue d'une donnée `C_c^infinity` divergence-free pour la
  transmission de symétrie, puis opérateur HWY linéarisé autour du profil
  auto-similaire singulier.
- Cible : déduire qu'un cutoff intérieur ou une convolution radiale du coeur
  `r^-1` excite génériquement le mode instable certifié par HWY.
- Hypothèse silencieuse trouvée : le profil et le lissage radial sont pairs
  pour `(Ju)(x)=S u(Sx)`, `S=diag(1,1,-1)`, alors que le mode certifié est
  impair.
- Attaque : recalcul de la projection de Leray
  `P(Sxi)=S P(xi)S`, commutation de la chaleur et de la linéarisation avec `J`,
  puis projecteurs exacts `Q_+=(I+J)/2`, `Q_-=(I-J)/2`.
- Résultat : `Q_-g_epsilon=0` et tout pairing avec un fonctionnel adjoint
  impair vaut zéro. Par unicité, la solution forte reste paire tant qu'elle
  existe. Le facteur instable n'amplifie donc que zéro.
- Horloge : à `t=kappa epsilon²`, une composante impaire
  `epsilon^beta` aurait au niveau linéaire le facteur
  `kappa^-a epsilon^(beta-2a)`; la borne source `a>=217/2000` rend
  `beta>=217/1000` nécessaire, non suffisante.
- Résidus : dix obligations rationnelles nulles, aucun flottant. Un opérateur
  adverse qui ne commute pas avec `J` a un commutateur maximal `2` et produit
  une composante impaire `3`, confirmant que la parité est le mécanisme exact.
- Portée : réfute seulement l'excitation du **mode impair certifié** par un
  lissage symétrique. N'exclut ni mode instable pair, ni lissage asymétrique,
  ni brisure faible après perte de l'unicité forte. Des perturbations impaires
  différentes sont des données Clay différentes et ne donnent pas une
  non-unicité pour une donnée lisse fixée.
- Statut : `REFUTED` pour l'arête d'excitation générique; claim de porte
  `COMPUTATION_ONLY`, sans revue indépendante externe.
- Artefact : `HWY-PARITY-PROJECTION-GATE-1`.

## `FAIL-NS-0015` — Confusion entre trace asymptotique HWY et donnée de Cauchy finie

- Date : 2026-08-14.
- Équation : NS incompressible 3D non forcé sur `R³`, viscosité `1`; une
  solution forte/classique et une solution de Leray–Hopf sur un intervalle
  commun issu d'une même donnée `L²` à temps fini.
- Cible : déduire de plusieurs branches HWY ayant la même trace critique
  singulière lorsque `tau->-infinity` plusieurs solutions depuis une même
  donnée Clay lisse posée à `t=0`.
- Hypothèse silencieuse trouvée : une condition asymptotique qui oublie le
  premier coefficient instable a été traitée comme un état de Cauchy fini.
- Attaque : identité de relative énergie pour `w=v-u`, coefficient exact de
  Grönwall, puis famille logistique
  `b_A=aA exp(a tau)/(a+A exp(a tau))` calculée en fractions exactes.
- Résultat : tant que `integral ||nabla u||_infinity dt<infinity`, une même
  donnée finie impose `w=0`. Dans le contre-modèle, toutes les branches ont la
  trace zéro à moins l'infini, mais leur état à tout temps fini détermine
  injectivement `A`. La trace commune n'est donc pas la donnée commune requise.
- Test adverse : `x'=2sqrt(x)` et `x_c(t)=(t-c)_+²` possèdent réellement la
  même donnée finie et des trajectoires distinctes, parce que la dynamique
  perd l'unicité localement lipschitzienne. Cela localise exactement la porte
  au breakdown de la classe forte.
- Pression : elle s'annule seulement dans le pairing global divergence-free;
  aucun contrôle local ou uniforme de pression n'est obtenu.
- Résidus : ODE, asymptotique, inverse, différence de branches et contrôle
  non lipschitzien exactement nuls; aucun flottant ni grille.
- Portée : réfute le transfert par simple identification des traces. N'exclut
  ni un breakdown fort, ni une non-unicité faible ultérieure, ni un nouveau
  mécanisme non perturbatif produisant la perte forte.
- Statut : `REFUTED` pour l'arête « même trace asymptotique -> même donnée de
  Cauchy finie »; claim de porte `COMPUTATION_ONLY`.
- Artefact : `ASYMPTOTIC-TRACE-CAUCHY-GATE-1`.

## Obstacle consolidé — désingularisation HWY vers une même donnée Clay

Trois stratégies distinctes ont fermé les inférences actuellement disponibles :

1. `FAIL-NS-0013` : `L²` plus une borne `L^{3,infinity}` n'apporte pas la
   compacité forte critique `L³` du cutoff intérieur;
2. `FAIL-NS-0014` : le lissage radial pair n'excite pas le mode instable impair
   certifié;
3. `FAIL-NS-0015` : une trace commune à `tau=-infinity` n'est pas une donnée
   de Cauchy finie commune, laquelle reste injective sur l'intervalle fort.

Décision de pivot : suspendre `GAP-LIMIT-ADMISSIBLE`. Toute réouverture devra
fournir un mécanisme de perte forte pour une donnée lisse fixée ou un théorème
de stabilité non perturbatif qui ne suppose aucune de ces trois arêtes. Le
prochain verrou actif devient la géométrie locale de la vorticité confrontée
aux triades de Fourier signées.

## Gabarit d'ajout

Chaque échec futur doit préciser cible, équation, domaine, type de solution,
hypothèses attaquées, test reproductible, résidu, portée négative exacte et
claim éventuellement supersédé.
