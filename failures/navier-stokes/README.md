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

## `FAIL-NS-0016` — Signe local du stretching déduit de la seule cohérence locale

- Date : 2026-08-14.
- Équation : Navier–Stokes incompressible 3D non forcé sur
  `T³=(R/2piZ)³`, viscosité `nu>0`; données initiales analytiques,
  périodiques, de moyenne nulle et divergence-free.
- Cible : déduire un signe universel ou une petite borne ponctuelle sans
  facteur d'échelle sur `omega·S omega` au centre à partir de la cohérence de
  `xi=omega/|omega|` dans un patch et de quantités quadratiques globales.
- Contre-profil :
  `u_a=(sin y+a sin x cos z,0,-a cos x sin z)`, `a=+-1`.
  Les deux signes sont reliés par la translation `x->x+pi` et ont les mêmes
  énergie `1/2`, enstrophie `3/4`, palinstrophie `5/2`, hélicité nulle,
  vorticité centrale `-e_3` et premier jet de vorticité nul.
- Résultat :
  `omega_a·S_a omega_a=-a cos x cos z cos²y`. Le terme vaut `-a` à
  l'origine et garde ce signe sur `Q_r`, tandis que les défauts angulaires
  centre–boule et pairwise sont respectivement `O(r²)` et `O(r|X-Y|)`.
- Non-localité : la pression périodique est reconstruite exactement et paire
  en `a`; le degré de liberté manquant est le strain global de Biot–Savart,
  non un terme local de la direction.
- Scaling : `U_N=N u_a(Nx)` conserve le ratio critique signé sur
  `Q_{r/N}` mais son énergie croît comme `N²`; aucune famille énergétique
  uniforme n'est revendiquée.
- Test : six modes Fourier et fractions rationnelles exactes; divergence,
  réalité, pression, jets, quantités quadratiques et scalings ont un résidu
  zéro. Empreinte du script :
  `04112a48e77a5286fd3e98a73471577a7f30a9b0acbd027699177b6204649708`.
- Portée : réfute seulement le lemme ponctuel local sans queue lointaine. Ne
  réfute ni Constantin–Fefferman, ni Beirão da Veiga–Berselli, ni un critère
  espace-temps uniforme sur tout l'ensemble de forte vorticité, ni un bilan
  intégré.
- Statut : `COMPUTATION_ONLY` avec dérivation exacte et trois passes
  adversariales de même famille de modèle; aucune revue externe indépendante.
- Artefact : `VORTICITY-LOCAL-COHERENCE-SIGN-GATE-1`.

## `FAIL-NS-0017` — Égalité terminale entre niveau et réarrangée

- Date : 2026-08-14.
- Cadre : théorie de la mesure sur `R³`; application conditionnelle à la
  solution mild analytique de NS incompressible 3D non forcé utilisée dans
  `arXiv:2607.08866v2`.
- Cible : l'identité présentée autour de (48),
  `lambda=f*(mu_f(lambda))`, supposée vraie « par définition ».
- Convention : `mu_f(lambda)=|{|f|>lambda}|` et
  `f*(v)=inf{a>=0:mu_f(a)<=v}`.
- Contre-profil : `f=5` sur une masse `3`, `f=2` sur une masse `4`, zéro
  ailleurs. Au niveau `lambda=4`, `mu_f(4)=3` mais `f*(3)=2`; le crochet exact
  est `f*(3)<=4<=f*(3-)`.
- Résultat : l'égalité terminale est réfutée sur un espace non atomique par un
  simple plateau de valeurs. Changer silencieusement `>` en `>=` ne la répare
  pas universellement.
- Réparation : pour tout `v<mu_f(lambda)`, on a `f*(v)>lambda`; faire croître
  `v` jusqu'à la masse du superniveau fournit l'implication quantitative
  corrigée. Le passage (47)→(49) n'est donc pas réfuté.
- Test : fractions rationnelles exactes, équivalence de pseudo-inverse sur une
  grille finie complète; zéro échec et aucun flottant. Empreinte :
  `0b306177085e584f1a658b4b9534ea74d7ca0ce07c599c7bf9295a95fdc804f7`.
- Portée : ne valide pas l'obtention de (47), O'Neil dans l'application PDE,
  les constantes uniformes, le commutateur ou le théorème 7.4.
- Statut : claim `REFUTED` pour l'égalité; lemme réparé séparé au statut
  `COMPUTATION_ONLY`.
- Artefact : `REARRANGEMENT-INVERSION-1`.

## `FAIL-NS-0018` — Reste positif de (46) déclaré `O(1)`

- Date : 2026-08-14.
- Cadre : transfert fonctionnel de la vorticité vers la vitesse dans
  `arXiv:2607.08866v2`, équations (41)–(47), sur `R³`.
- Cible : traiter comme uniformément borné, lorsque `v->0`, le reste
  `R(v)=3 integral_v^1 s^(-4/3)/log²(e/s) ds` de (46).
- Réfutation : avec `v=exp(-3n)`, l'intégration sur les trois dernières unités
  logarithmiques et `exp(n-1)>=(n-1)^3/6` donnent
  `R(v)>=3n/256`; le reste diverge.
- Ordre correct :
  `R(v)~9v^(-1/3)/log²(e/v)`. Il est inférieur d'un logarithme au terme
  principal et s'absorbe avec un cutoff uniforme, mais il n'est pas `O(1)`.
- Test : fractions exactes pour `n=2,...,64`, aucune approximation flottante;
  résidu rationnel non négatif. Empreinte :
  `cab6da2b536cfd5a72fd669887fe7dc444a283eba081bbfb9b02b9889897c06f`.
- Portée : réfute la justification additive de (46), pas l'exposant final de
  (47), réparé séparément sous des hypothèses uniformes.
- Statut : claim `NS-EQ46-BOUNDED-REMAINDER` `REFUTED`.
- Artefact : `ONEIL-TRANSFER-1`.

## `FAIL-NS-0019` — Reconstruction Biot–Savart sans fixation du mode harmonique

- Date : 2026-08-14.
- Équation : Navier–Stokes incompressible 3D non forcé sur `R³`; test sur une
  solution stationnaire analytique bornée.
- Cible : déduire `u=B[curl u]` de la seule bornitude, de la divergence nulle
  et de la connaissance de la vorticité.
- Contre-profil : `u=(2,-3,6)`, `p=0`. Le champ résout exactement NS,
  `div u=0`, `curl u=0` et `|u|=7`; pourtant `B[0]=0`.
- Conséquence : le membre droit littéral de (41) est zéro, tandis que la
  réarrangée de la vitesse vaut sept à tout volume fini.
- Réparation : imposer une décroissance à l'infini, `u∈L^p` pour un `p` fini,
  une moyenne nulle dans le cadre périodique, ou écrire
  `u=B[omega]+h` et contrôler `h` séparément.
- Scaling : `HV^(1/3)` est invariant sous la remise à l'échelle NS; la
  correction ne perd aucune puissance critique.
- Portée : ne réfute ni la régularité de la solution constante, ni une
  formulation Clay à données de Schwartz. Elle réfute l'inférence sous la
  seule hypothèse `L∞` affichée dans le raccord audité.
- Statut : claim `NS-BIOT-SAVART-LINF-ZERO-MODE` `REFUTED`.
- Artefact : `ONEIL-TRANSFER-1`.

## `FAIL-NS-0020` — Faible-`L^(3/2)` ne lance pas l'énergie tronquée

- Date : 2026-08-14.
- Cadre : fonction scalaire sur `R³`; variante vorticité divergence-free;
  aucun de ces profils n'est une solution Navier–Stokes.
- Cible : déduire de `f∈L^(3/2,infinity)` que
  `(f-lambda)_+∈H¹(R³)` pour tout niveau fini.
- Contre-profil : `f=|x|^-2 1_(0<|x|<1)`. Sa distribution vaut
  `(4pi/3)a^-3/2` pour `a>=1`, mais l'énergie tronquée contient
  `integral_0^R r^-2 dr=infinity` et la dissipation diverge davantage.
- Compatibilité vectorielle : `(a cross x)/|x|³`, à coupure radiale, est
  divergence-free et conserve la divergence énergétique sur tout cône où
  l'angle est non dégénéré.
- Réparation : pour la v2, invoquer explicitement la solution classique
  bornée et lissée à chaque temps `t<T*`; la norme faible sert ensuite à la
  mesure du support, pas à la finitude de l'énergie.
- Portée : ne réfute ni (23) pour une solution classique, ni la coercivité
  (33)–(34), ni un scénario Clay.
- Statut : claim `NS-WEAK-L32-TRUNCATION-H1` `REFUTED`.
- Artefact : `DEGIORGI-UNIFORMITY-AUDIT-1`.

## `FAIL-NS-0021` — Extension de l'intervalle terminal à tout `(0,T*)`

- Date : 2026-08-14.
- Cible : la phrase après (25) de `arXiv:2607.08866v2`, qui étend
  l'absorption à `(0,T*)` alors que le théorème 4.1 porte seulement sur
  `(T*−epsilon,T*)`.
- Contre-modèle logique : choisir la norme restreinte conforme à l'enveloppe
  sur l'intervalle terminal et égale à un avant celui-ci. Les prémisses
  terminales sont satisfaites et l'absorption antérieure échoue.
- Réparation : intégrer l'ODE depuis `t_0=T*−epsilon`; c'est exactement
  l'intervalle utilisé en (36), donc aucun exposant aval n'est perdu.
- Portée : contre-modèle abstrait, non solution PDE; réfutation du
  quantificateur littéral seulement.
- Statut : claim `NS-DEGIORGI-ENTIRE-INTERVAL-ABSORPTION` `REFUTED`.

## `FAIL-NS-0022` — Facteur dyadique deux avant (21)

- Date : 2026-08-14.
- Cible : avec `phi(r)=1/|log r|`, `N=floor((1/2)log_2(1/R))`, prétendre
  `phi(2^jR)<=2phi(R)` pour tout `j<=N+1`.
- Contre-test exact : `R=2^-8`, `N=4`, `j=5` donne
  `phi(2^jR)/phi(R)=8/3>2`.
- Famille exacte : pour `R=2^(-2m)`, l'excès signé au dernier indice est
  `1/[m(m-1)log 2]>0`. Une constante trois convient lorsque
  `log_2(1/R)>=6` et préserve l'ordre `R^-2phi(R)`.
- Réparation vérifiée : le cycle 0018 valide séparément extension BMO,
  interpolation, champ proche et queues; le résultat réparé reste
  conditionnel aux hypothèses globales de direction et de vorticité.
- Portée : réfute une constante locale de (20)–(21), pas le théorème 4.1
  complet ni sa conclusion après révision.
- Statut : claim `NS-DYADIC-PHI-FACTOR-TWO` `REFUTED`.
- Empreinte :
  `cbdca92eec11a287c31bb67d48dfeda339768863b2ccfa58b6cd8f66e3682721`;
  audit étendu
  `387898492a0dc370d6ca50aadbc18e7e524ebdc0d7326fe2347952cbce57ebbf`.

## `FAIL-NS-0023` — Réarrangée `min` exacte du noyau tronqué

- Date : 2026-08-14.
- Cadre : fonction radiale `h_a(y)=|y|^-3 1_(|y|>a)` sur `R³`; aucun objet
  Navier–Stokes n'est construit.
- Cible : l'identité `h_a^*(s)=min(a^-3,Cs^-1)` annoncée avant (12) de
  `arXiv:2607.08866v2`.
- Calcul exact : la fonction de distribution s'inverse en
  `h_a^*(s)=1/(a³+s/|B_1|)`, strictement décroissante pour tout `s>0`.
  Toute fonction `min` avec `C>0` possède un plateau; aucune constante ne
  donne l'identité.
- Réparation : les deux expressions sont comparables et
  `||h_a||_(L^(3,1))=(2pi/sqrt(3))|B_1|^(1/3)a^-2`. La puissance utilisée en
  (11)–(15) survit.
- Portée : réfute une formule exacte, pas la borne de Lorentz ni le taux du
  commutateur réparé.
- Statut : claim `NS-TRUNCATED-KERNEL-MIN-REARRANGEMENT` `REFUTED`.
- Artefact : `COMMUTATOR-UNIFORMITY-AUDIT-1` et dérivation du cycle 0018.

## `FAIL-NS-0024` — Petite dérive uniforme des moyennes emboîtées

- Date : 2026-08-14.
- Cadre : enveloppe scalaire des moyennes BMO sur les rayons `2^jR`; le
  contre-profil n'est pas une solution Navier–Stokes.
- Cible : remplacer la somme télescopique de (16) par
  `|c_k-c_0|<=Cphi(R)` uniformément jusqu'à l'échelle `sqrt(RR_*)`.
- Contre-profil : choisir tous les incréments au plafond
  `c_j-c_(j-1)=phi(2^jR)`. Pour `T=log_2(R_*/R)`, le rapport de la dérive
  terminale à `phi(R)` est au moins `floor(T/2)+1` et diverge.
- Réalisation géométrique adverse : une phase unitaire de type
  `eta log log(eR_*/|x|)` accumule une variation d'ordre un entre `R` et
  `sqrt(RR_*)` tout en gardant l'oscillation moyenne logarithmique.
- Réparation : conserver la double somme. Le facteur `4^-k` du noyau donne
  exactement `sum_(k>=1)(k+1)4^-k=7/9`, donc le taux final reste
  `O(phi(R))`.
- Portée : élimine une simplification tentante; ne réfute pas la preuve
  annulaire qui conserve les poids géométriques.
- Artefact : `COMMUTATOR-UNIFORMITY-AUDIT-1`, contrôle exact
  `unweighted_mean_drift_not_small`.

## `FAIL-NS-0025` — Temps maximal utilisé comme temps intérieur

- Date : 2026-08-14.
- Cadre : solution classique maximale de NS incompressible 3D non forcé sur
  `R³x(0,T*)`, viscosité `nu>0`.
- Cible : dans la preuve du théorème 7.4 de `arXiv:2607.08866v2`, poser
  `s=t+T_t` avec `T_t` « maximal local analyticity time », puis appliquer la
  propriété d'échappement sur `(t,T*)`.
- Contre-test exact : `T*=1`, `t=3/4`, `T_t=1/4` donne `s=1` et le résidu
  strict `T*−s=0`. Le point n'est pas dans l'intervalle où la solution est
  supposée définie.
- Réparation : employer le temps garanti
  `tau_t=nu/[c_1(M)||u(t)||_infinity²]` et séparer
  `t+tau_t>=T*` (prolongement direct) de `t+tau_t<T*` (endgame intérieur),
  comme dans le critère publié de Grujić 2013.
- Portée : réfute le choix temporel littéral, pas le lemme conditionnel réparé
  ni les théorèmes publiés d'analyticité.
- Statut : claim `NS-ENDGAME-MAXIMAL-TIME-SELECTION` `REFUTED`.

## `FAIL-NS-0026` — Synchronisation de suites asymptotiques séparées

- Date : 2026-08-14.
- Cadre : contre-système scalaire de temps, niveaux et rayons; aucune solution
  PDE n'est construite.
- Cible : conclure qu'une suite de temps portant la queue de distribution et
  une autre portant l'analyticité fournissent automatiquement un temps commun.
- Contre-test rationnel : les suites
  `d_n=1−1/(4n)` et `a_n=1−1/(4n+2)` tendent toutes deux vers un même temps
  terminal et portent séparément les lois attendues, mais leurs ensembles de
  temps sont disjoints.
- Réparation : toutes les estimations doivent être appliquées au temps unique
  `s=t+tau_t`, avec constantes uniformes sur l'intervalle terminal.
- Portée : réfute une inférence de quantificateurs, pas l'existence d'une
  solution possédant réellement les estimations uniformes.
- Artefact : passe adverse `cycle-0019-countermodel.md`.

## `FAIL-NS-0027` — Seuil de superniveau non uniforme

- Date : 2026-08-14.
- Cadre : enveloppes scalaires de distribution; aucune PDE simulée.
- Cible : une amplitude relative croissante `theta A_s` dépasse forcément un
  seuil de validité qui peut lui-même dépendre du temps ou de la troncature.
- Contre-test exact : `theta A_n=2^(n−2)` et `Lambda_n=2^(2n)` divergent,
  mais `theta A_n<Lambda_n` pour tout `n`. Une asymptotique « haut niveau »
  sans seuil commun ne s'applique jamais au niveau actif.
- Réparation : fixer `a_0,C_mu,U_*` indépendamment du temps, du niveau et de
  la troncature avant de choisir le temps d'échappement. Le changement
  `log a -> log(e+a)` exige en outre une perte de constante; un facteur huit
  est sûr au-dessus du seuil normalisé trois.
- Portée : réfute l'automaticité du seuil, pas une borne uniforme explicitement
  démontrée.
- Artefact : `ENDGAME-SYNCHRONIZATION-AUDIT-1` et passe contradictoire 0019.

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

## `FAIL-NS-0028` — Cohérence composante par composante vers `bmo_phi` global

- Date : 2026-08-14.
- Cadre : données `C_c^infinity(R³)` divergence-free pour NS incompressible
  3D non forcé, viscosité `nu>0`; calcul instantané, pas une trajectoire.
- Cible : déduire une borne globale uniforme `bmo_phi` d'une direction
  constante, donc parfaitement cohérente, sur chaque composante active.
- Contre-test : deux boules de rayon `epsilon`, centrées en
  `+/-2epsilon e_1`, portent `+e_3` et `-e_3` dans une boule commune de rayon
  `3epsilon`. Toute extension dans le corridor a
  `MO>=2/27`. Pour `3epsilon_n=exp(-n)`, le coût log-pondéré est au moins
  `2n/27`.
- Lemme optimal : avec fractions `a,b`, le coût minimal exact est
  `4ab/(a+b)`, atteint par la valeur de corridor `(a-b)e/(a+b)`. Une phase
  minoritaire suffisamment diluée peut donc éviter la divergence.
- Réalisation : potentiel compact lisse, divergence exactement nulle,
  vorticités internes antipodales et scaling critique faible-`L^(3/2)`.
- Résidu : douze contrôles exacts passent; aucune pression globale ni
  persistance dynamique des cœurs n'est revendiquée.
- Réparation : imposer un packing inter-composantes
  `4ab/(a+b)=O(phi(r))`, avec convention aux zéros et uniformité temporelle.
- Statut : claim `NS-ACTIVE-CORE-BMO-EXTENSION` `REFUTED`.

## `FAIL-NS-0029` — Canonicité de la direction sur les zéros de vorticité

- Date : 2026-08-14.
- Cadre : solution classique nulle de NS incompressible non forcé sur `R³`,
  toute viscosité `nu>0`.
- Cible : considérer l'appartenance globale de `xi=omega/|omega|` à
  `bmo_phi` comme une propriété intrinsèque sans définir `xi` aux zéros.
- Contre-test exact : `u=p=omega=0`. Les extensions unitaires `xi=e_1` et
  `xi=sign(x_1)e_1` satisfont la même identité `omega=|omega|xi`; la première
  a semi-norme zéro et la seconde une semi-norme log-pondérée infinie.
- Résidu : PDE, divergence et relation rotationnel–vorticité exactement nuls.
- Réparation : fixer une convention canonique, ou quantifier explicitement
  l'existence d'une extension espace-temps mesurable avec borne uniforme.
- Portée : ne réfute pas un théorème déjà formulé avec une telle existence.
- Statut : claim `NS-VORTICITY-DIRECTION-ZERO-CANONICITY` `REFUTED`.

## `FAIL-NS-0030` — Magnitude critique vers vorticité admissible

- Date : 2026-08-14.
- Cadre : profils statiques `W=r^-2 Omega(theta)` sur `R³`; raccord visé à
  NS incompressible non forcé.
- Cible : considérer la factorisation scalaire `|W|=Phi r^-2` comme une
  spécification suffisante du champ de vorticité.
- Contre-tests : `W=e/r²` a une direction constante mais
  `div W=-2(e dot theta)r^-3`; `W=theta/r²` est solénoïdal hors de zéro mais
  vérifie `div W=4pi delta_0`.
- Porte exacte : il faut simultanément
  `div_(S²)Omega_T=0` et `integral_(S²)Omega_r=0`.
- Réparation : imposer ces contraintes au facteur vectoriel, puis seulement
  reconstruire la vitesse par Biot–Savart.
- Portée : critique la suffisance du gabarit scalaire, pas l'existence de
  profils vectoriels satisfaisant la porte.

## `FAIL-NS-0031` — Profil vectoriel critique exactement récurrent et log-BMO

- Date : 2026-08-14.
- Cadre : `W in L1_loc intersection L^(p,infinity)(R³)`, `p<infinity`, non
  nul presque partout, divergence-free et `W(qx)=q^-2W(x)` pour `0<q<1`.
- Cible : construire dans cette classe une direction globale
  `bmo_phi`, `phi(r)->0`.
- Obstruction : la récurrence rend `MO_(B_(q^n r))` indépendante de `n`,
  tandis que `bmo_phi` la force vers zéro. La direction devient constante.
  Alors `div(m e)=0` rend `m` invariant le long de `e`; tout superniveau non
  vide a une mesure infinie, contrairement au faible-`L^p` global.
- Contrechamp décisif : un curl explicite satisfait `|W|=r^-2`, divergence
  nulle et faible-`L^(3/2)`, mais conserve `MO>=2/3` à tout rayon.
- Portée : n'exclut ni une direction non récurrente, ni un profil seulement
  asymptotique, ni la récurrence de la seule magnitude.
- Statut : `NS-DILATION-RECURRENT-BMO-RIGIDITY`, `COMPUTATION_ONLY`.

## `FAIL-NS-0032` — Coupure radiale à erreur critique évanescente

- Date : 2026-08-14.
- Cadre : profil solénoïdal `W=r^-2 Omega(theta)` et coupure radiale `chi`.
- Cible : rendre le profil globalement énergétique en le multipliant par une
  coupure dont le défaut de divergence disparaît avec l'échelle.
- Résidu exact :
  `||div(chi W)||_1=Var(chi)||Omega_r||_(L¹(S²))`; une double coupure monotone
  coûte deux fois cette constante, indépendamment des rayons.
- Réparation : résoudre `Delta_(S²)psi=Omega_r` et ajouter
  `-[chi'(r)/r]nabla_(S²)psi`. La constante optimale est `1/sqrt(2)` en `L²`,
  mais le correcteur reste de taille critique.
- Défaut PDE restant : `[Delta,chi]W` a le même ordre `nu r^-4` que le terme
  visqueux principal; transport, étirement et pression doivent être recalculés
  globalement.
- Portée : réfute une coupure gratuite, pas l'existence d'une correction
  solénoïdale ni d'un profil dynamique.

## Obstacle consolidé — profil ponctuel exactement récurrent

Trois stratégies réellement différentes ferment la classe actuelle :

1. `FAIL-NS-0030` : la magnitude scalaire ne garantit pas l'admissibilité
   vectorielle;
2. `FAIL-NS-0031` : une direction exactement récurrente est rigidifiée par
   log-BMO puis annulée par divergence plus faible-Lorentz;
3. `FAIL-NS-0032` : une coupure spatiale ne rend pas l'erreur petite à
   l'échelle critique.

Décision de pivot : suspendre l'ansatz vectoriel exactement homogène ou
log-périodique. Le prochain test porte sur une direction rectifiée seulement
à la vitesse `1/|log r|`, avec masse critique et résidu PDE suivis.

## Gabarit d'ajout

Chaque échec futur doit préciser cible, équation, domaine, type de solution,
hypothèses attaquées, test reproductible, résidu, portée négative exacte et
claim éventuellement supersédé.
