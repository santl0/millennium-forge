# Questions ouvertes priorisées

Mise à jour : 2026-08-14. Une question descend dans la liste lorsqu'un test
réduit son incertitude ou lorsqu'un verrou préalable est découvert. L'historique
des décisions reste dans les checkpoints.

| Priorité | Question falsifiable | Pourquoi maintenant | Critère de sortie |
|---:|---|---|---|
| 1 | un retour de flux compact peut-il distribuer une rotation macroscopique sur une cascade interne non-Dini tout en gardant faible-`L^(3/2)`, log-BMO global et masse critique ? | le cycle 0026 prouve qu'une masse conique normalisée uniforme force une oscillation cubique; un corridor de zéros réduit le coût BMO à `Theta(1/log(R/h))`, mais le lift collinéaire compact est impossible | potentiel axisymétrique explicite à deux amplitudes, audit des composantes de cutoff et de toutes les boules; puis Biot–Savart et résidu, ou obstruction par épaisseur/capacité |
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
