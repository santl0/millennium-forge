# Questions ouvertes priorisées

Mise à jour : 2026-08-15. Une question descend dans la liste lorsqu'un test
réduit son incertitude ou lorsqu'un verrou préalable est découvert. L'historique
des décisions reste dans les checkpoints.

| Priorité | Question falsifiable | Pourquoi maintenant | Critère de sortie |
|---:|---|---|---|
| 1 | un streamfunction axisymétrique non séparable peut-il masquer chaque retour radial par une couche verticale suivante tout en gardant faible-`L^(3/2)`, masse critique, énergie et log-BMO all-ball ? | le cycle 0027 réalise le scaling cubique compact div–curl mais exclut l'aspect fixé et montre qu'un aspect croissant seul ne contrôle pas les transitions locales; le flux-angle général ne donne qu'une obstruction trop faible | somme finie `psi_n=sum_j A_(n,j)chi_(n,j)` avec calcul des capacités `|W_r|>=|W|/4`, audit all-ball et résidu, ou abandon dès qu'une couche garde une capacité polynomiale |
| 2 | la définition du « critical point singularity » de la v2 se raccorde-t-elle sans contradiction à une solution classique bornée pour chaque `t<T*` et au confinement uniforme `A_lambda(t)⊂B_(C lambda^-1/2)` ? | faible-`L^(3/2)` seul ne rend pas l'énergie tronquée finie; les nouveaux budgets supposent encore une borne de tranche et une masse par bloc | formulation espace-temps quantifiée du profil avec seuils uniformes, ou contre-exemple logique à la coexistence des hypothèses |
| 3 | la queue annulaire de strain issue du cœur actif reste-t-elle petite pour un champ divergence-free multi-échelle compatible avec une dynamique NS ? | le commutateur du cycle 0018 conserve la queue, mais aucun mécanisme dynamique ne force les phases ou directions lointaines favorables | champ adverse explicite avec résidu NS suivi, ou borne uniforme de la queue depuis une hypothèse héritée |
| 4 | un problème renormalisé NS peut-il être réduit à un opérateur compact avec bornes de queue certifiables ? | préalable à toute preuve assistée par ordinateur | rayon de contraction validable sous raffinement |
| 5 | le noyau Fourier fini énergie–Leray peut-il être formalisé sans axiome ni `sorry` en Lean ? | petite brique stable, indépendante des scénarios spéculatifs | build épinglé + `#print axioms` vide hors logique standard |

## Questions suspendues

- Reproduire le CAP Hou–Wang–Yang : suspendu faute des quelque 800 Go de RAM
  annoncés. Au commit primaire `615ee6f`, le `Project.toml` existe mais aucun
  `Manifest.toml`; le README se contredit sur ce point. Les candidats `.mat`
  amont ne sont pas tous reliés à une chaîne génératrice et des empreintes.
- Auditer intégralement les manuscrits Shahmurov 2026 : veille conservée, mais
  une revendication unilatérale non publiée ne dépasse pas les verrous mieux
  bornés ci-dessus sans vérification indépendante.
- Forcer une trace nulle dans le zoom maximum KNSS : suspendu après trois
  stratégies. Le cycle 0009 montre que les limites commutent déjà dans la
  classe mild au temps-record `s=0`, où elles conservent une valeur non nulle;
  le temps physique `T` est l'extrémité mobile `B_k`. Une réouverture demande
  une nouvelle extraction, pas une autre topologie sur la même suite.
- Déduire une compacité critique de trace depuis l'énergie seule : suspendu
  après les trois échecs `FAIL-NS-0006` à `0008`.
- Transférer la multiplicité HWY vers une même donnée Clay lisse : suspendu
  après `FAIL-NS-0013` à `0015`. Les trois portes indépendantes sont la
  compacité critique, l'annulation par parité du mode certifié et la différence
  entre trace asymptotique et donnée de Cauchy finie. Une couche impaire et son
  adjoint ne seront réouverts qu'avec un mécanisme de perte forte non circulaire.

## Question fermée conditionnellement au cycle 0008

Une ancienne mild au sens KNSS sur `R³ x (-infinity,0)`, globalement bornée et
ayant une vraie trace nulle dans `D'` quand `t->0-`, est nécessairement nulle.
Le statut reste `COMPUTATION_ONLY` parce que le chaînage est une dérivation du
laboratoire non revue extérieurement. Le raccord de ces hypothèses à une
extraction Clay reste ouvert mais est suspendu après le troisième test du
cycle 0009. La désingularisation Hou–Wang–Yang a ensuite été suspendue après
trois tests supplémentaires; la priorité active est désormais la géométrie
locale de la vorticité confrontée aux triades signées.

## Question fermée conditionnellement au cycle 0018

Sous une borne uniforme de vorticité faible-`L^(3/2)`, une semi-norme globale
de direction `bmo_phi`, l'extension BMO de Jones et le raccord tensoriel de
Biot–Savart, les quatre morceaux de `(8)->(22)` conservent le taux
`1/[1+log(R_*/R)]` avec constante uniforme. Le poids `4^-k` est indispensable :
la dérive brute des moyennes n'est pas petite. Le statut est
`COMPUTATION_ONLY`; l'hypothèse géométrique globale et sa compatibilité avec
les zéros de vorticité restent ouvertes.

## Question fermée conditionnellement au cycle 0019

Sous une queue de vitesse uniforme
`C_mu/[a³log³(e+a/U_*)]`, le théorème local d'analyticité et les résultats
publiés de mesure harmonique, `(49)->(58)` se synchronise au même temps. La
preuve doit utiliser `tau_t=nu/[c_1(M)U(t)²]` et séparer le prolongement direct
du temps intérieur; le choix « maximal » donne au contraire `s=T*`. Dans la
branche intérieure, le rayon témoin sparse est inférieur au sous-rayon
analytique au-dessus d'un seuil fini et les deux cas harmoniques donnent la
contradiction. Statut `COMPUTATION_ONLY`; la queue uniforme et la direction
globale `bmo_phi` ne sont pas produites pour les données Clay générales.

## Résultat négatif du cycle 0010

La localisation HWY est extérieure et conserve le coeur `1/r`. Pour une
régularisation intérieure, la convergence `L²` et une borne uniforme
`L^{3,infinity}` ne donnent pas de compacité `L³` : une famille
`C_c^infinity`, divergence-free, satisfait ces deux prémisses tout en gardant
un écart `L³` strict entre les échelles `epsilon` et `2epsilon`. Toute preuve
de transfert reposant uniquement sur ce module statique est abandonnée. Une
stabilité à temps strictement positif, avec projection instable et couche
parabolique explicites, n'est pas réfutée.

## Résultat négatif du cycle 0011

Le profil HWY est pair sous la réflexion axiale vectorielle, tandis que le mode
instable certifié est impair. La chaleur, les cutoffs/convolutions radiaux, la
projection de Leray et l'opérateur linéarisé autour du profil pair commutent
avec cette réflexion. Ainsi la couche de régularisation symétrique a une
projection impaire exactement nulle et la solution forte locale reste paire
par unicité. La route « lissage radial puis excitation générique du mode
certifié » est abandonnée. Une asymétrie contrôlée reste testable, mais ses
signes différents sont des données Clay différentes et sa balance terminale
exige un adjoint certifié ainsi que les termes non linéaires et non locaux.

## Résultat négatif du cycle 0012

Une condition commune à `tau=-infinity` oublie les coefficients instables et
ne constitue pas une même donnée de Cauchy à temps fini. Sur l'intervalle fort,
l'identité de relative énergie et Grönwall imposent au contraire l'injectivité
faible–forte depuis une donnée finie commune. La famille logistique exacte
`b_A=aA exp(a tau)/(a+A exp(a tau))` partage la trace zéro, tandis que son état
à tout temps fini récupère `A`. Le transfert par identification des traces est
abandonné. Après ce troisième échec HWY réellement distinct, le programme
pivote vers la géométrie locale de la vorticité et les triades signées.

## Résultat négatif du cycle 0013

La paire périodique exacte `u_a`, `a=+-1`, a les mêmes quantités
quadratiques, la même vorticité centrale, un premier jet nul et les mêmes
bornes de cohérence locale, mais
`omega_a·S_a omega_a(0)=-a`. Sous scaling Navier–Stokes, le ratio critique
signé reste `-a` sur un patch à l'échelle `|omega|^-1/2`, au prix d'une énergie
croissant comme `N²`. Toute règle de signe ponctuel fondée seulement sur un
patch local est donc abandonnée. Une réouverture doit inclure tout l'ensemble
de forte vorticité, l'uniformité temporelle et une queue Biot–Savart explicite.

## Résultat positif borné du cycle 0014

Pour tout borélien `S⊂R³`, une densité au plus `delta` dans `B_r(x_0)` impose
une tranche centrale de densité au plus `delta^(1/3)` au même rayon; la boule
concentrique prouve l'optimalité. Si `|S|≤B`, le rayon uniforme construit est
`[B/(delta|B_1|)]^(1/3)`. Le sens adverse est essentiel : le seul volume
garantit les rayons au-dessus de ce seuil, pas tout rayon inférieur. Le maillon
est fermé avec le statut `COMPUTATION_ONLY`; les estimations PDE qui produisent
le majorant de volume restent ouvertes.

## Résultat positif borné et correction du cycle 0015

Une enveloppe uniforme
`f*(v)≤A v^(-1/3)/log(eV_*/v)` sur `0<v≤v_0` implique, pour les niveaux assez
grands,

```text
mu_f(lambda) ≤ A^3 /
  [lambda^3 (1+3 log(lambda/(A V_*^(-1/3))))^3].
```

Le lemme est invariant sous le scaling Navier–Stokes et la puissance
logarithmique trois est asymptotiquement optimale. En revanche, l'identité
`lambda=f*(mu_f(lambda))` est réfutée par un profil à plateaux; l'uniformité
temporelle est aussi fausse si le cutoff `v_0` dégénère. Le passage
`(47) -> (49)` est donc fermé après réparation au statut `COMPUTATION_ONLY`,
sans valider l'obtention de (47) ni un profil ponctuel radial de la vitesse.

## Résultat positif borné et réfutations du cycle 0016

Une queue (40) adimensionnée et uniforme, complétée par
`omega∈L^{3/2,infinity}` et une décomposition
`u=B[omega]+h` à mode harmonique borné, implique quantitativement

```text
u*(v)<=Qv^(-1/3)/log(eV/v),  0<v<=Vexp(-6),
```

avec `Q` explicite et invariant d'échelle. Le transfert fonctionnel
`(40) -> (47)` est donc fermé après révision au statut `COMPUTATION_ONLY`.

Deux lectures littérales sont réfutées. Le reste positif de (46) diverge
comme `9v^(-1/3)/log²(e/v)` et n'est pas `O(1)`, même s'il reste absorbable.
Par ailleurs, un champ constant borné a vorticité nulle mais vitesse non nulle;
(41) doit fixer ou retrancher la composante harmonique. Ces corrections ne
produisent pas (40) depuis la dynamique et ne valident pas le théorème 7.4.

## Règle de pivot

Après trois stratégies mathématiquement différentes bloquées sur la même
question, ajouter leurs échecs au registre, abaisser la question et sélectionner
la meilleure valeur informationnelle suivante. Un simple renommage de norme ou
de profil ne compte pas comme stratégie distincte.

## Priorité active après le cycle 0028

1. **`GAP-MOMENT-CORRECTED-TOROIDAL-CASCADE`.** Construire ou réfuter une
   paire de tores signés dont l'impulsion hydrodynamique s'annule, avec
   faible-`L^(3/2)` uniforme, extension log-BMO all-ball et
   `liminf ||u||_3>0`.
2. **Propagation localisée.** Quantifier `bmo_log(psi xi(t))` pour une coupure
   restant à distance de l'axe et suivre `sqrt(nu t)/R`; la version globale
   unisignée est déjà réfutée par l'oscillation axiale un.
3. **Excès radial.** Pour une somme non séparable, produire un minorant
   uniforme `Delta_Omega>0`; sans lui, la borne de capacité est vide.

Abandonner la première voie si l'annulation du seul moment d'impulsion crée
une interface antipodale de capacité comparable au cœur, fait diverger la
quasi-norme critique ou force encore `||u||_3->0`.

## Priorité active après le cycle 0029

1. **`GAP-MANY-TORUS-CRITICAL-ACCUMULATION`.** Pour `N_n->infinity`, combiner
   la normalisation faible-`L^(3/2)`, le packing des corridors et les termes
   croisés de `||sum_j u_j||_3^3`; décider si une cohérence non locale peut
   donner un minorant positif.
2. **Vitesse compacte d'abord.** Construire un `u_n` compact divergence-free,
   poser `omega_n=curl u_n`, puis tester faible-Lorentz et log-BMO. Cette voie
   impose Schwartz sans cascade infinie de moments.
3. **Propagation.** Seulement si une famille passe les deux gates précédents,
   calculer résidu visqueux, pression et stabilité temporelle.

Abandonner les tores disjoints si packing et faible-Lorentz forcent
`||sum_j u_j||_3->0`, ou si le seul régime non petit exige des corridors qui
se chevauchent et recréent une interface directionnelle d'ordre un.

## Priorité active après le cycle 0030

1. **`GAP-COMPACT-VELOCITY-WEAK-CRITICAL-DIRECTION`.** Construire ou exclure
   une famille `U_n in C_c^infinity(R^3)`, divergence-free, avec
   `curl U_n` borné dans faible-`L^(3/2)`, `U_n` hors du régime de petite donnée
   faible-`L^3`, et direction active uniformément log-BMO. Le premier test doit
   porter sur une boule entièrement active, pas sur le seul domaine parent.
2. **Ledger hétérogène.** Formuler une condition Morrey–Carleson pondérée pour
   des `A_j,h_j,q_j` variables. Abandonner si l'optimiseur se concentre sur un
   nombre borné de blocs ou si le corridor BMO impose une somme Carleson qui
   force encore `||u||_3->0`.
3. **Temps commun.** Pour toute famille passant les deux gates statiques,
   comparer le temps d'interaction à `r_min^2/nu`; une dynamique qui se découple
   avant un temps uniforme ne raccorde pas un scénario de blow-up.

Trois variantes réellement distinctes du tube homogène sont fermées : tore
unique, cardinal fixé avec moments, cardinal croissant sous packing local. Ne
pas rouvrir cette branche sans hétérogénéité quantitative ou chevauchement
géométrique explicitement compatible avec le log-BMO all-ball.

## Priorité active après le cycle 0031

1. **`GAP-NONSEPARABLE-COMPACT-CURL-FLATNESS`.** Deux couches de
   streamfunction à transitions décalées peuvent-elles masquer les zones où
   `partial_r U_theta` ou `partial_z U_theta` est grande, tout en gardant
   faible-`L^3(U)` non petit, faible-`L^(3/2)(curl U)` borné et log-BMO
   all-ball ? Le test décisif est un ledger exact de fonctions de distribution
   pour deux couches, avec signes et échelles indépendants.
2. **Flux de bord critique.** Le quotient
   `||U||_(L^(3,infinity))/||curl U||_(L^(3/2,infinity))` peut-il être assez
   petit pour sélectionner une bonne sphère tout en conservant une masse
   conique normalisée non dégénérée ? Le contre-profil compact de la revue
   0031 interdit de supprimer le terme de bord.
3. **Temps commun.** Toujours différé : une famille statique admissible devra
   d'abord passer les trois gates avant l'audit de `min(a,b)^2/nu`, de la
   pression et du stretching.

Abandonner la construction à deux couches si chaque zone de transition porte
un sous-ensemble dont le coût Lorentz se minore indépendamment des autres
couches, ou si tout masquage exige une nouvelle transition de capacité au
moins comparable.

## Priorité active après le cycle 0032

1. **`GAP-THICK-CROSS-SECTION-GRADIENT-DIRECTION`.** Pour
   `U=(R/r)F e_theta` avec `|supp F|/R^2>=c>0`, déterminer si la compacité de
   `F` force une boule active où la direction
   `nabla_perp F/|nabla F|` a une oscillation quantitative. Le lemme minimal
   doit être invariant d'échelle et localisé, pas une simple variation totale.
2. **Plateaux dégénérés et compensateurs rares.** Construire le test adverse
   le plus agressif : extrema en plateau, cols multiples et transitions de
   faible capacité. Abandonner l'argument de degré si ces profils gardent les
   deux endpoints tout en repoussant toute rotation directionnelle hors des
   boules critiques.
3. **Sortie du swirl pur.** Si la topologie plane ne donne aucune coercivité,
   introduire une composante poloïdale compacte avec projection de Leray
   recalculée; ne pas réutiliser silencieusement le lemme scalaire.

La branche « deux couches minces » est fermée plus fortement que le critère
d'abandon prévu : le weak HLS du champ total donne directement
`K_U<=C(S_2/R^2)^(1/6)K_W`, sans isoler aucune transition.

## Priorité active après le cycle 0033

1. **`GAP-AXIALLY-DISPERSED-PURE-SWIRL-SELECTION`.** Pour une union de cellules
   éloignées, les quasi-normes globales impliquent-elles l'existence d'une
   cellule ou troncature locale avec rapport endpoint non dégénéré ? Le lemme
   doit couvrir amplitudes, tailles et supports hétérogènes.
2. **Distribution sans bloc dominant.** Chercher une suite où les fonctions de
   distribution globales satisfont les deux gates, alors que chaque cellule
   a un rapport local tendant vers zéro. Une telle suite réfuterait le pivot de
   sélection et imposerait un ledger collectif non local.
3. **Corridors entre cellules.** Même si un bloc local est sélectionné, auditer
   si une extension globale peut réduire son oscillation sur la boule locale;
   le théorème 0033 affirme que non lorsque la direction active du bloc est
   conservée.

Le degré topologique seul est abaissé : il ne quantifie ni la masse active ni
le volume de la boule. La troncature/coaire est désormais le mécanisme retenu.

## Priorité active après le cycle 0034

1. **`GAP-DEGENERATE-CELL-REGISTER-OR-OVERLAP`.** Le registre BV sélectionne
   une cellule si sa boîte a un volume comparable au plateau effectif. Peut-on
   traiter des corridors ou queues avec `|Q_j|/v_j->infinity` sans perdre la
   constante faible-Lorentz ?
2. **Chevauchements et annulations.** Construire deux potentiels pure-swirl
   dont les plateaux restent spatialement identifiables mais dont les curls
   se chevauchent et s'annulent avant la fonction de distribution, ou prouver
   qu'un packing signé conserve un registre local.
3. **Échelle dynamique.** Les gates sélectionnent un bon rapport, pas un rayon
   tendant vers zéro. Relier la cellule au coeur pré-singulier par un argument
   Type I publié, puis identifier exactement le trou Type II.
4. **Cutoff curl-compatible.** Quantifier simultanément
   `nabla chi cross U`, le défaut de divergence, la projection de Leray et la
   composante harmonique/de bord à l'échelle critique.

Le pigeonhole fondé uniquement sur les quasi-normes est définitivement
abandonné : `NS-WEAK-LORENTZ-CELL-SELECTION` est réfuté par distributions
totales exactes. Toute nouvelle sélection doit afficher son registre
géométrique ou dynamique.

## Priorité active après le cycle 0035

1. **`GAP-ACTIVE-HALO-DIAMETER-OR-OVERLAP`.** La bande commune a un volume
   contrôlé mais peut comporter de nombreuses gouttelettes séparées. Un budget
   faible-Lorentz sélectionne-t-il une composante contenue dans une boule
   `O(R_j)`, ou seulement leur union dispersée ?
2. **Décomposition par composantes de niveau.** Quantifier les raccords créés
   lorsqu'un filament sous `lambda/4` relie des superniveaux actifs et décider
   si chaque composante peut être traitée comme une pseudo-cellule.
3. **Chevauchements.** Après le test mono-cellule, autoriser un multiplicité de
   recouvrement bornée et suivre les annulations de curls avant la valeur
   absolue.
4. **Échelle dynamique.** Même une boule statique sélectionnée doit encore
   être liée à `R(t)->0` pour produire un coût log-BMO pré-singulier.

Le halo fixé par un volume témoin est abandonné; seule une bande construite au
niveau global est admissible dans la branche pure-swirl.

## Priorité active après le cycle 0036

1. **`GAP-ABOVE-THRESHOLD-THIN-BRIDGE`.** Deux gouttes de taille `R`, séparées
   par `LR`, peuvent-elles rester dans la même composante de
   `{sigma F>lambda/4}` grâce à un tube de rayon `delta R` sans faire diverger
   `||curl U||_(L^(3/2,infinity))` ni dégrader le gate vitesse ?
2. **Seconde troncature adaptative.** Si le pont coûte trop cher, formuler le
   niveau `lambda/4+tau` ou le cutoff capacitaire qui isole une goutte sans
   réintroduire de mesure de bord et avec constante uniforme en `L`.
3. **Chevauchements signés.** Après le pont mono-cellule, permettre une
   multiplicité bornée de supports originaux et mesurer la perte exacte de
   `K_(w,alpha)<=K_w` sous annulation.
4. **Raccord dynamique.** Barker `NS-SRC-0162` borne des centres sous faible
   `L3`; déterminer quelle hypothèse supplémentaire transformerait la boule
   statique sélectionnée en échelle `R(t)->0`, en séparant Type I et Type II.

Les gouttes reliées strictement sous `lambda/4` sont fermées. Ne pas rouvrir
la branche par un covering volume-seul : Frank–Lieb est optimal en échelle et
ne donne qu'une fraction `cV^2/P^3` potentiellement nulle.

## Priorité active après le cycle 0037

1. **`GAP-BRIDGE-SCALE-CALIBRATION-OR-MERGE-TREE`.** Pour la composante
   sélectionnée au cycle 0036, obtenir soit `AR>=kappa K_u` sur une branche
   persistante, soit un niveau de retroncature qui la scinde en morceaux de
   diamètre `O(R)` sans perdre le rapport endpoint quadratique.
2. **Arbre de fusion enrichi.** Définir pour chaque branche son intervalle de
   niveaux, son diamètre essentiel minimal et son budget coaire. Le merge tree
   discret n'est admissible qu'avec bornes d'interpolation et certification
   des cols plus fins que la maille.
3. **Multi-gouttes à amplitudes hétérogènes.** Tester si une distribution
   dyadique peut faire échouer simultanément le calibrage local et toutes les
   retroncatures, malgré la somme de coûts
   `integral diam(E_t^1) dt`.
4. **Chevauchements signés.** Une fois la dichotomie mono-cellule stabilisée,
   autoriser les supports de curl superposés et recalculer les annulations
   avant toute fonction de distribution locale.
5. **Raccord dynamique.** Toujours différé : relier la branche statique à un
   rayon `R(t)->0`, contrôler pression et projection de Leray, puis séparer
   Type I et Type II.

Un pont de persistance relative fixe et calibrée est désormais fermé par
`NS-PURE-SWIRL-PERSISTENT-BRIDGE-DIAMETER`. Ne pas confondre ce résultat avec
le diamètre d'une composante au seul niveau bas : les fusions tardives restent
le premier quantificateur ouvert.

## Priorité active après le cycle 0038

1. **`GAP-OVERLAPPING-CURL-CANCELLATION`.** La fermeture statique vaut pour
   un curl unique et pour des supports cellulaires disjoints. Si deux curls se
   recouvrent, la distribution de leur somme peut être plus petite que chaque
   distribution locale. Construire une annulation lisse critique ou établir
   une sélection stable sous multiplicité/signature contrôlée.
2. **Registre après projection de Leray.** Un cutoff spatial introduit
   `nabla chi cross U`, un défaut de divergence et une correction non locale.
   Quantifier ces trois termes au même endpoint avant d'utiliser une boule
   locale dans une solution réelle.
3. **Échelle dynamique.** Relier la cellule sélectionnée à un rayon
   `R_j(t)->0` sous une hypothèse Type I précisément sourcée; isoler ensuite le
   premier passage qui échoue pour Type II.
4. **Formalisation.** Certifier d'abord l'algèbre finie et la sélection au
   même niveau; ne formaliser l'interface BV/coaire qu'après stabilisation des
   représentants et des constantes.

`GAP-BRIDGE-SCALE-CALIBRATION-OR-MERGE-TREE` est fermé dans la classe
pure-swirl annulaire disjointe par le niveau moyen adaptatif. L'itération le
long d'un merge tree et la persistance H0 seule sont abandonnées : leurs
contre-ledgers exacts ne respectent pas le registre coaire d'un curl compact.

## Priorité active après le cycle 0039

1. **`GAP-MULTIAXIS-TOTAL-FIELD-LOCALIZATION`.** Construire une décomposition
   intrinsèque du champ total, indépendante de tout étiquetage, lorsque les
   axes et anneaux locaux diffèrent. Quantifier simultanément divergence,
   curl de col, correction de Leray et queue de pression.
2. **Coercivité anti-annulation testable.** Déterminer si une hypothèse de
   Gram/angle ou un packing de phase-espace, formulé sur une décomposition
   canonique, suffit à transférer le rapport global vers une cellule. Elle
   doit être vérifiable depuis le champ total et stable sous remise à l'échelle.
3. **Endpoint secondaire fini.** Tester si une amélioration uniforme
   `L^(3,q)` et `L^(3/2,q)` avec `q<infinity` apparaît dans une classe
   pré-singulière sourcée; sans telle amélioration, une base norm-convergente
   du plein faible-Lorentz est exclue par non-séparabilité.
4. **Échelle dynamique.** Après seulement une localisation intrinsèque
   survivante, relier la cellule à `R(t)->0`, d'abord sous Type I puis en
   localisant le premier échec Type II.

`GAP-OVERLAPPING-CURL-CANCELLATION` est fermé négativement pour les sommants
arbitrairement étiquetés et positivement, par agrégation, lorsque axe, rayon et
anneau sont communs. La multiplicité seule et le caractère curl-compatible ne
sont plus des hypothèses admissibles d'anti-annulation.

## Priorité active après le cycle 0040

1. **`GAP-WEAK-L3-CORE-CAPTURE-AT-PRESINGULAR-SCALE`.** Sous une hypothèse
   pré-singulière précisément sourcée, existe-t-il `x(t),R(t)` avec
   `R(t)->0` et
   `||1_(B(x(t),R(t)))u(t)||_(3,infinity)>=alpha||u(t)||_(3,infinity)` ?
   Sans la contrainte `R(t)->0`, la question est triviale pour un champ
   compact et doit être rejetée.
2. **Dichotomie multi-échelle adverse.** Construire un champ lisse compact
   divergence-free dont la norme faible-`L3` se répartit sur un nombre
   croissant d'échelles de sorte qu'aucune boule de la gamme candidate ne
   capture une fraction uniforme, ou prouver qu'une concentration issue d'un
   temps maximal interdit cette dispersion.
3. **Dénominateur local.** Si l'usage de Biot–Savart global est incompatible
   avec la future compacité, sélectionner simultanément une couronne où
   `H_out+G_col` est contrôlé par le core, avec constantes explicites.
4. **Raccord dynamique.** Calculer l'équation satisfaite par
   `V_R=chi_Ru-B_R(grad chi_R dot u)`, y compris dérivée temporelle,
   diffusion, non-linéarité et pression. Ce travail ne commence qu'après une
   capture d'échelle non triviale.
5. **Formalisation.** Certifier d'abord moyenne nulle, inclusion Lorentz de
   mesure finie et constantes algébriques; l'opérateur de Bogovskiĭ demeure
   une interface papier tant qu'une bibliothèque épinglée manque.

`GAP-MULTIAXIS-TOTAL-FIELD-LOCALIZATION` est partiellement fermé : la partie
cinématique solénoïdale ne requiert aucun axe. Il reste ouvert comme problème
dynamique, car la sélection d'échelle, la pression et les commutateurs ne sont
pas contrôlés.

## Priorité active après le cycle 0041

1. **`GAP-TYPE-I-LOCALIZED-EVOLUTION`.** Pour
   `R(t)=2sqrt((T_*-t)/S_w^*(C_MM))`, calculer au sens exact l'équation de
   `V=chi_Ru-B_R(grad chi_R dot u)`. Suivre `R'(t)`, la dérivée de l'opérateur
   remis à l'échelle, diffusion, convection, pression et support de la force.
2. **Uniformité critique.** Déterminer si la force localisée reste bornée dans
   un espace invariant après remise à l'échelle par `R(t)`, ou produire un
   profil admissible qui la fait diverger. Une constante dépendant de
   `T_*-t` au-delà de sa puissance dimensionnelle ferme négativement l'axe.
3. **`GAP-TYPE-II-RELATIVE-CORE-CAPTURE`.** Sans borne uniforme `M`, tester
   quantitativement la dégénérescence de `S_w^*(M_j)` et des constantes de
   Carleman pour `M_j->infinity`; ne pas remplacer une fenêtre temporelle par
   une borne sur une seule tranche.
4. **Formalisation.** Formaliser l'inclusion de mesure finie avec constante
   trois et l'invariance d'échelle. L'interface Barker–Prange demeure un
   axiome papier sourcé, non un théorème formel du dépôt.

Le verrou de capture relative est fermé uniquement dans la branche Type I
globale pointwise. Il reste ouvert en Type II et ne fournit ni contrôle de la
vorticité au même centre, ni solution ancienne, ni rigidité.

## Priorité active après le cycle 0042

1. **`GAP-TYPE-I-MOVING-COMMUTATOR-BOUND`.** Pour la réalisation
   support-lisse fixée de Bogovskii, établir ou réfuter
   `||[Delta,Q]U-kappa[D,Q]U||_(L1+div L^(3/2,infinity))<=C(M)` sans utiliser
   une borne de dérivées déjà équivalente à la régularité recherchée.
2. **Test haute fréquence complet.** Injecter
   `U_N=epsilon phi(r,z)sin(Nz)e_theta` dans la formule intégrale de `B` et
   déterminer si le terme `O(N)` survit dans la somme complète, pas seulement
   terme par terme.
3. **`GAP-TYPE-I-FORCED-RIGIDITY`.** Si la borne critique survit, classifier
   les solutions anciennes de l'équation renormalisée avec force annulaire
   critique. Une borne grande ne constitue pas une petitesse perturbative.
4. **Pression.** Comparer la forme locale avec pression `chi_Rp` à la forme
   projetée non locale; suivre la jauge de pression et les queues de Leray.
5. **Type II.** Conserver séparément
   `GAP-TYPE-II-RELATIVE-CORE-CAPTURE`; aucune formule 0042 ne répare la
   dépendance dégénérante en `M`.

La simple implication `R(t)->0` vers une force de cutoff `o(1)` est fermée
négativement. L'échelle instantanée naturelle de la force est `L1`, ou une
divergence de stress faible-`L^(3/2)`, et elle est exactement critique.

## Priorité active après le cycle 0043

1. **`GAP-TYPE-I-FORCE-COMPACTNESS`.** Une borne uniforme dans
   `X=L1+div L^(3/2,infinity)` ne donne aucune compacité forte. Identifier une
   topologie où la pression et les produits quadratiques passent à la limite
   sans supposer le lissage recherché.
2. **Couronne externe `L`.** Choisir `chi_L=1` sur `B_1`, placer la transition
   près de `B_L`, puis suivre les normes de Bogovskii et des commutateurs en
   fonction de `L`. Tester si la force s'échappe de tout compact.
3. **Localité contre Leray.** Comparer la forme annulaire avec pression locale
   et la forme solénoïdale à queue non locale; ne pas confondre disparition du
   support source et disparition de la pression harmonique.
4. **`GAP-TYPE-I-FORCED-RIGIDITY`.** Si une force limite subsiste, classifier
   les solutions anciennes correspondantes. Une borne critique grande n'est
   pas perturbative.
5. **Type II.** Maintenir `GAP-TYPE-II-RELATIVE-CORE-CAPTURE` séparé : la
   dépendance de `kappa` et du rayon en `M` n'est pas uniforme.

Le sous-gap `GAP-TYPE-I-MOVING-COMMUTATOR-BOUND` est fermé uniquement pour la
réalisation exacte, supportée et pseudodifférentielle fixée au cycle 0043. Le
caractère qualitatif `C_c^infinity->C_c^infinity` ne suffirait pas.

## Priorité active après le cycle 0044

1. **`GAP-TYPE-I-LOCAL-COMPACTNESS-TRACE`.** Sur une diagonale
   `R_j->0`, `L_j->infinity`, `L_jR_j->0`, obtenir des bornes locales de
   temps suffisantes pour une compacité forte de `Z_j` et le passage de
   `Z_j tensor Z_j`, sans réintroduire une norme globale qui croît comme
   `L_j²`.
2. **Inégalité d'énergie.** Vérifier que la force localement évanescente et
   les pressions de Riesz permettent de passer l'inégalité d'énergie locale;
   suivre toutes les fonctions tests et les queues harmoniques.
3. **Trace non triviale.** Transporter la fraction Type I capturée dans
   `B_1` jusqu'à une trace de la limite. Une borne pointwise à des temps
   variables ne suffit pas sans compacité temporelle.
4. **Horloge.** Dérenormaliser l'équation avec drift `+kappa D` vers une
   solution ancienne standard, avec domaines temporels et facteur de
   viscosité exacts.
5. **`GAP-TYPE-I-ANCIENT-WEAK-L3-RIGIDITY`.** Classifier ou exclure une
   limite ancienne non triviale seulement bornée dans faible-`L3`; ne pas
   supposer auto-similarité, axisymétrie ou bornitude `L-infinity`.
6. **Type II.** Garder `M_j->infinity` hors de cette branche : ni la capture,
   ni `kappa(M_j)`, ni les constantes locales ne sont uniformes.

`FAIL-NS-0080` exclut une convergence dans le `X` global quand
`kappa!=0`. Le résultat positif du cycle est strictement local en espace et
ne comporte aucune dérivée temporelle.

## Priorité active après le cycle 0045

1. **`GAP-TYPE-I-CRITICAL-TRACE-PERSISTENCE`.** Déduire de la capture Type I
   un test fixe `psi` et `c_*>0` tels que
   `|<Z_j(0),psi>|>=c_*`, ou une topologie de trace assez forte pour
   conserver une minoration non signée.
2. **Test adverse PDE-compatible.** Construire ou exclure une cascade de
   solutions qui conserve `K_3` à la tranche, respecte la force
   `C^infinity_x,loc->0` uniforme en temps, mais annule chaque observable
   fixe. Les profils purement fonctionnels ne suffisent plus.
3. **Persistance publiée.** Tester si la condition d'explosion persistante de
   la proposition A.5 d'Albritton–Barker peut être dérivée du premier temps
   singulier et de la normalisation actuelle, avec pression endpoint suivie.
4. **Horloge.** Une fois la trace non nulle obtenue, dérenormaliser
   `+kappa D` sur tout `(-infinity,0]` avant d'appliquer une rigidité standard.
5. **`GAP-TYPE-I-ANCIENT-WEAK-L3-RIGIDITY`.** Ne devient actif qu'après
   non-trivialité, dérenormalisation et identification de la classe adaptée
   ou mild.
6. **Type II.** Reste séparé : aucune constante de capture ni `kappa(M)`
   n'est uniforme pour `M_j->infinity`.

`FAIL-NS-0081` réfute la transmission automatique d'une norme terminale par
la seule compacité volumique. Le produit et l'énergie locale sont désormais
fermés; la trace, pas la compacité intérieure, est le premier verrou.

## Priorité active après le cycle 0046

1. **`GAP-TYPE-I-DERENORMALIZATION-CLASS`.** Partir de
   `partial_sZ-Delta Z+div(Z tensor Z)+nabla Pi+kappa DZ=0` et vérifier dans
   les distributions, avec pression et inégalité d'énergie locale, la
   transformation `R=e^(-kappa s)`, `dt/ds=R²`,
   `u=R^-1Z(dot/R,s)` vers Navier–Stokes standard ancien.
2. **Classe globale.** Déterminer si la sortie est seulement faible adaptée
   locale, dissipative, Leray–Hopf locale ou mild; ne pas importer une
   rigidité dont les hypothèses de pression, décroissance ou énergie globale
   ne sont pas satisfaites.
3. **`GAP-TYPE-I-ANCIENT-WEAK-L3-RIGIDITY`.** Classifier ou exclure une
   solution ancienne standard non triviale uniformément bornée dans
   faible-`L3`, sans supposer auto-similarité, axisymétrie ou bornitude.
4. **Singularité terminale optionnelle.** Si la rigidité choisie exige un
   point singulier à l'endpoint, tester séparément Albritton–Barker A.5; la
   non-trivialité intégrée du cycle 0046 ne donne pas cette propriété.
5. **Type II.** Reste hors de la branche : `M_j`, `S_w^*(M_j)`, `kappa_j` et
   les constantes de compacité ne sont pas uniformes.

`FAIL-NS-0082` réfute la nécessité d'un moment signé porté par l'ancien temps
terminal dans la branche Type I persistante. Il ne réfute pas les
contre-profils de tranche de `FAIL-NS-0081` et ne ferme aucune rigidité.

## Priorité active après le cycle 0047

1. **`GAP-TYPE-I-ANCIENT-WEAK-L3-RIGIDITY-OR-MILDNESS`.** Décider si une
   ancienne adaptée locale, à pression de Riesz et uniformément
   `L^(3,infinity)`, admet sur chaque bande forward la scission calorique et
   le correcteur énergétique de Barker–Seregin–Šverák.
2. **Trace de redémarrage.** Identifier la topologie minimale à un temps
   fini `tau_0<0` qui annule tout reste calorique homogène dans Duhamel sans
   invoquer la forte continuité, fausse sur tout `L^(3,infinity)`.
3. **Test adverse admissible.** Chercher une solution ancienne suitable à
   pression de Riesz dont les queues faibles-L3 interdisent une énergie
   globale du correcteur; un simple champ cinématique `|x|^-1` ne suffit pas
   pour réfuter le raccord PDE.
4. **Rigidités plus fortes.** Tester séparément les portes `L3` fort sur une
   suite reculée, bornitude mild, axisymétrie exacte ou récurrence de
   dilatation. Ne transférer aucun théorème sans sa porte.
5. **Endpoint singulier.** Ne le réintroduire que si le théorème choisi
   l'exige; la non-trivialité volumique ne donne pas une singularité à zéro.
6. **Type II.** Reste séparé : le pipeline dépend d'une borne Type I finie et
   ses constantes ne sont pas uniformes lorsque cette borne diverge.

`GAP-TYPE-I-DERENORMALIZATION-CLASS` est fermé au statut interne par le claim
0047. `FAIL-NS-0083` bloque seulement la promotion fonctionnelle automatique
vers Leray–Hopf; la question PDE de mildness reste ouverte.

## Priorité active après le cycle 0048

1. **`GAP-TYPE-I-RELATIVE-ENERGY-GLOBALIZATION`.** Partir du correcteur
   canonique `w=v-S(t-t_0)v(t_0) in C_tL2_x` et globaliser l'inégalité
   d'énergie relative avec des cutoffs `chi_R`, sans tester par `w` avant
   d'avoir obtenu `nabla w in L2`.
2. **Flux à l'infini.** Suivre séparément convection, gradient du flot
   calorique, pression de Riesz et termes de cutoff sur les couronnes. Le
   contrôle faible-Lorentz n'est pas absolument continu sur les queues.
3. **Dissipation.** Décider si l'équation et la suitability locale réparent
   la perte du noyau `nabla K_h~h^-5/4`; la seule taille critique ne le fait
   pas.
4. **Branche de continuité forte.** Tester en parallèle, sans la confondre
   avec BSS, si les traces appartiennent au sous-espace
   `tilde L^(3,infinity)` de continuité du semi-groupe. Duhamel Gelfand et
   `C_w*` ne donnent pas ce fait.
5. **Contre-profil PDE-compatible.** Transformer ou réfuter le témoin
   cinématique homogène à queue persistante en une solution adaptée qui
   porte un flux d'énergie relatif non nul à l'infini.
6. **Rigidité et Type II.** Aucune rigidité KNSS/Albritton–Barker n'est
   applicable avant bornitude ou mildness forte; Type II reste hors du
   pipeline à constantes fixées.

`NS-WEAK-L3-DUHAMEL-L2-CORRECTOR` ferme la trace faible-étoile, le Duhamel
endpoint de Gelfand et le correcteur `C_tL2`. `FAIL-NS-0084` interdit d'en
déduire une intégrale de Bochner, une petite constante temporelle, une
dissipation globale ou un split énergétique naïf.

## Priorité active après le cycle 0049

1. **`GAP-TYPE-I-BSS-ANCIENT-RIGIDITY`.** Décider si les scissions BSS
   obtenues séparément depuis chaque `t_0<0` ont une cohérence ou une
   compacité uniforme lorsque `t_0->-infinity`.
2. **`GAP-TYPE-I-BSS-TO-STRONG-MILD-CONTINUITY`.** Identifier une condition
   falsifiable plaçant les traces dans le sous-espace de continuité du
   semi-groupe `tilde L^(3,infinity)`.
3. **Dépendance au temps de base.** Suivre la croissance `T^(1/2)` des bornes
   d'énergie relative et décider si une annulation ancienne peut l'améliorer.
4. **Non-unicité à grande donnée.** Ne pas recoller deux redémarrages par une
   unicité de classe BSS qui n'est pas disponible.
5. **Rigidité minimale.** Formuler un Liouville pour solution ancienne
   localement suitable, globalement faible-`L3`, munie de scissions
   énergétiques sur toutes bandes, puis rechercher ses contre-profils.
6. **Branches hors portée.** Le pipeline reste conditionnel à Type I; Type II
   et les données Clay générales ne sont pas réduits à cette classe.

`NS-WEAK-L3-RELATIVE-ENERGY-GLOBALIZATION` ferme le verrou énergétique sur
une bande finie. `FAIL-NS-0085` interdit d'effacer la suitability ou de
remplacer le contrôle des flux par une simple interpolation globale.

## Priorité active après le cycle 0050

1. **`GAP-TYPE-I-BSS-ENERGY-TAIL-TIGHTNESS`.** Chercher une identité issue
   du transfert non linéaire, de la pression de Riesz ou d'une annulation de
   basse fréquence qui force
   `liminf_(s->-infinity)||v(r)-S(r-s)v(s)||_2<infinity`.
2. **`GAP-TYPE-I-ANCIENT-QUOTIENT-RIGIDITY`.** Classifier les orbites PDE
   dans le quotient séparé
   `L^(3,infinity)/closure(L2 inter L^(3,infinity))`; la seule dynamique
   calorifique admet des classes fixes non nulles.
3. **Test adverse PDE.** Modifier le profil à queue `|x|^-1` seulement si le
   résidu Navier--Stokes, la pression et l'inégalité locale d'énergie sont
   tous suivis; un contre-profil cinématique supplémentaire n'a plus de
   valeur informationnelle.
4. **Mildness.** La continuité forte dans `tilde L^(3,infinity)` à temps fini
   ne contrôle pas le passé. Toute promotion doit produire l'identité mild
   entre temps finis puis une hypothèse quantitative au passé.
5. **Critère de sortie positif.** Une seule suite reculée de correcteurs
   uniformément `L2` suffit à obtenir une trace énergétique globale; viser ce
   quantificateur minimal plutôt qu'une borne pour tous les temps de base.
6. **Branches séparées.** Type II et le problème Clay général restent hors
   de cette réduction Type I conditionnelle.

`FAIL-NS-0086` ferme la stratégie purement semi-groupale. La prochaine
expérience doit mesurer une quantité PDE sensible aux queues, pas répéter le
cocycle calorique.

## Priorité active après le cycle 0051

1. **`GAP-TYPE-I-ANCIENT-INFRARED-STRESS-DEPLETION`.** Pour
   `B_j(s,r)=-integral_s^r Delta_jS(r-tau)Pdiv(v tensor v)(tau)dtau`, obtenir
   le long d'une suite ancienne un gain signé
   `||B_j||_2<=C_r2^(epsilon(j-J))` pour `j<=J`, ou le réfuter par une même
   orbite ancienne admissible.
2. **`GAP-TYPE-I-SINGLE-ANCIENT-ORBIT-RECURRENCE`.** Identifier une propriété
   de cohérence au passé qui distingue une solution ancienne unique des
   translations de la solution forward Jia--Sverak.
3. **Critère calorifique minimal.** Il suffit de trouver un seul `a>0` et une
   suite `s_n->-infinity` avec `||S(a)g_(s_n,r)||_2` borné. Ne pas imposer
   inutilement une uniformité en `a` ou en tout temps de base.
4. **Phases avant normes.** Le critère exact porte sur les intégrales
   vectorielles `B_j`. Sommer les normes temporelles absolues détruit les
   cancellations et ne donne qu'une condition suffisante beaucoup plus
   forte.
5. **Queues critiques.** Tester si une condition Herz/Besov à indice fini,
   un moment nul du stress ou une identité de flux signée est héritée par la
   réduction Type I; l'ajouter comme hypothèse sans héritage ne ferme rien.
6. **Branches séparées.** La solution forward saturante n'est ni ancienne,
   ni Leray--Hopf globale, ni issue d'une donnée Clay. Type II reste hors du
   pipeline.

`NS-WEAK-L3-ANCIENT-INFRARED-CRITERION` ferme les hautes fréquences mais pas
le critère bas. `NS-FORWARD-SELFSIMILAR-CORRECTOR-SATURATION` et
`FAIL-NS-0087` interdisent désormais toute nouvelle tentative d'obtenir une
borne uniforme de fenêtre depuis la seule taille faible-`L3`.

## Priorité active après le cycle 0052

1. **`GAP-TYPE-I-ANCIENT-SIGNED-BASE-FLUX-CANCELLATION`.** Obtenir, pour un
   filtre `a>0` fixe et une suite ancienne, une borne de la primitive signée
   `integral_s^r Phi_a`, sans remplacer `Phi_a` par son module.
2. **Gain dyadique dynamique.** Tester un énoncé non tautologique
   `integral_(s_n)^r Phi_(a,j)<=C_r2^(epsilon(j-J))` pour `j<=J`, après
   somme des triades et intégration temporelle. La coercivité d'une triade
   isolée est réfutée.
3. **Récurrence de blow-down.** Déterminer si une suite de retours de la même
   orbite force une compensation entre primitives. Distinguer récurrence
   faible-étoile, DSS exacte et auto-similarité backward exacte.
4. **Liouville exact déjà fermé.** Ne pas réattaquer les profils backward
   auto-similaires exacts dans faible-`L3` : Guevara--Phuc et Chae--Wolf les
   excluent sous leurs hypothèses. Chercher le premier raccord vers une
   récurrence moins rigide.
5. **Pression et localisation.** Tout passage dyadique doit conserver la
   projection globale ou suivre la pression de Riesz dans la dualité
   `L^(3/2,infinity)`--`L^(3,1)`.
6. **Branches séparées.** Le pipeline reste conditionnel à Type I. Type II,
   une donnée Clay générale et un blow-up admissible ne sont pas réduits au
   critère de flux.

`FAIL-NS-0088` abandonne les valeurs absolues et le signe triadique
universel. La prochaine expérience doit porter sur une corrélation
temporelle d'une même trajectoire ancienne.

## Priorité active après le cycle 0053

1. **`GAP-TYPE-I-RENORMALIZED-GENERATOR-TO-SIGNED-FLUX`.** Relier la
   minoration locale du générateur renormalisé à la densité signée `Phi_a`
   du temps de base, ou construire une orbite compatible où le générateur
   reste non nul mais tangent à une récurrence sans gain infrarouge.
2. **Fonctionnelle coercive.** Chercher une fonctionnelle locale, critique et
   intégrable au passé dont la dissipation domine un `D_R`; une telle borne
   forcerait une sous-suite presque stationnaire et fermerait la branche par
   le Liouville publié.
3. **Pression et endpoint.** Conserver les tests
   `W_0^(1,(3,1))`, la pression globale de Riesz et les queues de ses
   transformées. Toute utilisation de `W_0^(1,3)` doit d'abord exploiter
   explicitement l'énergie suitable locale.
4. **Récurrence.** Ne pas confondre retour de l'état et petit générateur :
   l'orbite exacte `z'=Jz` est périodique avec générateur de norme un.
5. **Compacité.** Toute extraction doit préserver dans une même sous-suite
   la forte `L3_loc`, la capture sur une fenêtre et tous les rayons fixes;
   aucune uniformité en rayon ne vient de la seule diagonale.
6. **Branches séparées.** La minoration ne traite que le scénario Type I
   capturé. Elle ne couvre ni Type II, ni DSS arbitraire, ni les données Clay
   générales.

`NS-TYPE-I-RENORMALIZED-GENERATOR-NONVANISHING` ferme le raccord
« petit générateur sur toutes les boules -> profil BSS interdit ». Il ne
contrôle pas encore le flux signé ni l'énergie globale.

## Priorité active après le cycle 0054

1. **`GAP-TYPE-I-RENORMALIZED-TANGENTIAL-ACTIVITY-CLASSIFICATION`.**
   Déterminer si une ancienne suitable Type I capturée peut porter une
   activité asymptotiquement tangentielle aux niveaux du correcteur
   calorifié, ou si la PDE fournit une coercivité absente du bilan scalaire.
2. **Orbites relatives de rotation.** Partir de
   `Z(s,y)=R(alpha s)U(R(-alpha s)y)` et reproduire les régimes RSS déjà
   exclus. Isoler exactement ce qui reste pour les rotations intermédiaires,
   sans remplacer la borne Type I ponctuelle par faible-`L3`.
3. **Angle PDE.** Chercher un contrôle quantitatif de la composante de
   `L_kappa Z` orthogonale au test `Theta_a`, avec queues de chaleur et de
   Riesz, facteur `rho^2` et constantes uniformes.
4. **Orbites non exactes.** Tester ensuite une modulation de phase lente ou
   une pseudo-orbite RSS; une exclusion des profils exacts ne couvre pas ces
   mouvements.
5. **Critère d'abandon.** Abandonner l'axe si trois classes distinctes
   (RSS, modulation, multi-échelle) admettent des contre-profils compatibles
   avec toutes les identités disponibles sans produire de coercivité PDE.
6. **Portée.** La branche reste conditionnelle à Type I; Type II et la donnée
   Clay générale demeurent hors de ce raccord.

`FAIL-NS-0090` interdit désormais d'inférer la petitesse du générateur depuis
un flux scalaire instantané ou intégrable sans inégalité angulaire propre à
Navier--Stokes.

## Priorité active après le cycle 0055

1. **`GAP-TYPE-I-APPROXIMATE-ROTATION-MODULATION-COMPACTNESS`.** Transformer
   un petit défaut
   `partial_s Z_n-beta_n mathcal R Z_n` sur toutes les boules en limite RSS
   ou stationnaire, avec une même sous-suite et le stress quadratique fermé.
2. **Vitesses bornées.** Prouver d'abord la variante où `beta_n` reste dans
   un compact : extraction `beta_n->alpha`, forte `L3_loc`, passage de la
   pression de Riesz et conservation de la capture.
3. **Générateur dégénéré.** Si `mathcal R Z_n->0`, éviter toute division par
   sa norme et raccorder directement la limite axisymétrique/stationnaire au
   Liouville faible-`L3`.
4. **Vitesses non bornées.** Déterminer si l'équation et les bornes Type I
   interdisent `|beta_n|->infinity`, ou si une moyenne angulaire compacte
   remplace la convergence des phases.
5. **RSS intermédiaire.** Ne réattaquer la rigidité de profil qu'après cette
   réduction; Pineau--Vicol v2 laisse `|alpha|` d'ordre un ouvert sous sa
   borne ponctuelle plus forte.
6. **Critère d'abandon.** Pivoter si les trois régimes `beta_n` borné,
   non borné et `mathcal R Z_n` dégénéré ne peuvent être séparés par des
   constantes uniformes issues du paquet suitable.

`NS-TYPE-I-EXACT-RELATIVE-ROTATION-CLASSIFICATION` ferme la vitesse variable
**exacte**. Il ne fournit aucune stabilité quantitative de cette
classification.

## Priorité active après le cycle 0056

1. **`GAP-TYPE-I-UNBOUNDED-ROTATION-MODULATION-OR-RSS-RIGIDITY`.** Le cas
   `sup_n||beta_n||_infinity<infinity` est fermé conditionnellement. Séparer
   désormais vitesses divergentes, moyenne axisymétrique et RSS à rotation
   intermédiaire.
2. **Production de la modulation.** Déduire, depuis le pipeline Type I, une
   même sous-suite avec forte `L3_loc`, ledger suitable uniforme et défaut
   `partial_sZ_n-beta_n mathcal RZ_n->0`; ces hypothèses ne sont pas encore
   produites par une singularité générale.
3. **Vitesses non bornées.** Tester si `|beta_n|->infinity` impose, après
   moyennage angulaire, `mathcal R Z=0`, ou si une compensation
   `beta_n mathcal R Z_n=O(1)` survit comme dans le contre-modèle exact.
4. **Pression et capture.** Conserver une jauge globale de Riesz, les queues,
   les bornes locales uniformes et la capture sur un cylindre centré dans
   chaque extraction.
5. **RSS intermédiaire.** Même une RSS exacte non stationnaire faible-`L3`
   n'est pas éliminée par les théorèmes actuels sans borne Type I ponctuelle
   supplémentaire et régime de rotation extrême.
6. **Critère d'abandon.** Pivoter après trois mécanismes distincts échouant
   à contrôler la vitesse non bornée; conserver alors l'obstruction comme
   séparation nette entre compacité cinématique et rigidité PDE.

`NS-TYPE-I-BOUNDED-MODULATION-COMPACTNESS-TO-RSS` ferme le sous-cas borné,
sans division par `||mathcal R U||`. `FAIL-NS-0092` interdit d'étendre ce
passage à faible fois faible ou à une modulation non uniformément bornée.
