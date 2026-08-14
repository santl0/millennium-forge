# Questions ouvertes priorisées

Mise à jour : 2026-08-14. Une question descend dans la liste lorsqu'un test
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
