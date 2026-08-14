# Cycle 0019 — synchronisation conditionnelle de l’endgame analytique

Date : 2026-08-14. Lemme actif :
`CONDITIONAL-ENDGAME-SYNCHRONIZATION-1`.

## Décision adaptative

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total | Décision |
|---|---:|---:|---:|---:|---:|---|
| synchroniser temps garanti, niveau, deux rayons et fermeture harmonique de `(49)–(58)` | 4 | 4 | 5 | 5 | **18/20** | sélectionnée |
| tester l’extension `bmo_phi` depuis le seul cœur actif de vorticité | 5 | 3 | 5 | 5 | 18/20 | prochaine, car située en amont |
| tester l’admissibilité espace-temps du profil ponctuel critique | 4 | 3 | 4 | 5 | 16/20 | différée |

L’égalité des deux meilleurs scores est tranchée par l’ordre du graphe : le
cycle 0018 avait laissé l’endgame comme premier maillon aval non reproduit.
Le présent cycle ne traite qu’un lemme : fermer conditionnellement ce maillon
ou exhiber son premier quantificateur faux. L’expérience décisive emploie des
fractions exactes pour les deux branches temporelles et la combinaison
harmonique.

## Équation, domaine et type de solution

La cible est Navier–Stokes incompressible 3D non forcé sur `R³`, sans
frontière, avec viscosité `nu>0` :

```text
partial_t u+(u dot nabla)u-nu Delta u+nabla p=0,
div u=0.
```

On part d’une solution classique, donc mild et unique à chaque redémarrage,
sur son intervalle maximal supposé `(0,T*)`, avec

```text
U(t)=||u(t)||_infinity,
u in C((0,T*);L∞(R³)).
```

L’endgame n’est pas un argument pour une solution faible ou seulement
Leray–Hopf. Il utilise l’extension holomorphe spatiale d’une solution mild
`L∞` avant `T*`. Aucun passage périodique, avec frontière ou forcé n’est
effectué.

## Veille différentielle et provenance

La notice primaire de `arXiv:2607.08866` contrôlée le 2026-08-14 reste en
version 2, soumise le 9 juillet et révisée le 13 juillet 2026. Aucune v3,
publication évaluée ni correction publique n’a été identifiée. Le théorème
7.4 et le raccord `(49)–(58)` restent donc des affirmations de prépublication.

Les briques publiées ont été séparées :

- Guberović 2010 fournit l’analyticité spatiale des solutions de
  Koch–Tataru; la version à facteur arbitraire `M>1` est explicitée par
  Grujić–Xu 2024;
- Grujić 2013 contient le critère 1D et, surtout, les deux branches
  temporelles absentes de la rédaction 2026;
- Solynin 1997/1999 fournit la borne extrémale de mesure harmonique;
- Ransford 1995 fournit le principe additif des deux constantes.

Ils sont enregistrés sous `NS-SRC-0064`, `0066` et `0076` à `0078`. La
phrase « Gu [22] » de la v2 désigne Rafaela Guberović.

## Entrée uniforme et scaling

Le logarithme doit être sans dimension. On formule l’entrée réellement
nécessaire avec une amplitude de référence `U_*>0`, un seuil `a_0>0` et une
constante uniforme `C_mu>0` :

```text
|{x:|u(x,t)|>a}|
 <=C_mu/[a³ log³(e+a/U_*)]                         (H49)
```

pour `t` dans un intervalle terminal et `a>=a_0`. Sous

```text
u_kappa(x,t)=kappa u(kappa x,kappa²t),
```

les poids sont

```text
U,a,U_* : +1,       temps : -2,
rayons : -1,        volume : -3,
nu,C_mu^(1/3) : 0,  log(e+a/U_*) : 0.
```

Ainsi `C_mu^(1/3)` a physiquement la dimension de la viscosité, mais reste
invariant sous le scaling NS à viscosité fixée. Les formules
`tau~nu/U²`, `rho~nu/U` et `|V|~U^-3` sont covariantes. Le logarithme apporte
un gain critique, pas une puissance cachée.

La forme littérale `C/[a³(log a)³]` de (49) ne peut être remplacée par
`C/[a³log³(e+a)]` avec la même constante : le second membre est plus petit.
Pour `a/U_*>=3`, la comparaison
`log(e+a/U_*)<=2log(a/U_*)` préserve l’exposant avec un facteur sûr huit.

## Paramètres harmoniques verrouillés

Fixons la densité volumique `delta_3=3/4` et
`delta_1=delta_3^(1/3)`. La borne de Solynin donne

```text
h*=(2/pi) asin[(1-delta_3^(2/3))/(1+delta_3^(2/3))].
```

Le même facteur doit être utilisé dans le théorème d’analyticité et dans la
fermeture harmonique :

```text
M=(2-h*)/[2(1-h*)]>1,
theta=1/(2M)=(1-h*)/(2-h*),
h*/2+(1-h*)M=1,        theta M=1/2.                (P)
```

Si la borne analytique emploie un facteur plus grand que celui verrouillé
par (P), la fermeture peut échouer. Le contre-test rationnel
`h=1/3`, facteur verrouillé `5/4`, mais facteur analytique `3/2`, produit le
coefficient exact `6/5>1`.

## Premier trou littéral : le temps « maximal »

La v2 pose `s=t+T_t`, qualifie `T_t` de « maximal local analyticity time »,
puis utilise `U(s)>U(t)` parce que `t` est un temps d’échappement. Cette
inférence exige d’abord `s<T*`.

Sous l’interprétation maximale naturelle, la branche redémarrée depuis `t`
atteint son premier obstacle à `T*`; donc `T_t=T*−t` et

```text
s=T*,                 T*−s=0.
```

Le point n’appartient pas à `(t,T*)`. Le témoin exact
`T*=1,t=3/4,T_t=1/4` réfute l’inférence. Le claim
`NS-ENDGAME-MAXIMAL-TIME-SELECTION` est donc `REFUTED`.

Cette réfutation ne détruit pas l’endgame. Elle impose le temps garanti par
le théorème local,

```text
tau_t=nu/[c_1(M)U(t)²],                             (T)
```

et l’alternative exhaustive :

```text
t+tau_t>=T*  : la solution mild locale franchit T*;
t+tau_t<T*   : poser s=t+tau_t et exécuter l’endgame.
```

L’égalité appartient à la première branche. C’est exactement la structure du
critère publié de 2013.

## Temps d’échappement et rayon analytique

Si la première branche se produit arbitrairement près de `T*`, le
prolongement est déjà obtenu. Sinon, pour tout `t` assez terminal,

```text
t+nu/[c_1(M)U(t)²]<T*,
```

d’où `U(t)²>nu/[c_1(M)(T*−t)]` et `U(t)->infinity`. La continuité de `U`
permet alors de prendre le dernier minimiseur de chaque intervalle terminal;
ces temps d’échappement satisfont

```text
U(q)>U(t) pour tout q dans (t,T*)
```

et ont une amplitude arbitrairement grande.

Au temps intérieur `s=t+tau_t`, le théorème local donne une extension
holomorphe de borne `M U(t)` et un rayon au moins

```text
rho_t=sqrt(nu tau_t)/c_2(M)
     =nu/[c_A(M)U(t)],   c_A=c_2 sqrt(c_1).          (Rho)
```

Comme `U(s)>U(t)`, on peut choisir le sous-rayon conservatif
`rho_s=nu/[c_AU(s)]`. L’équation (54) doit désigner un sous-rayon certifié,
pas l’égalité avec le rayon maximal réel.

## Rayon sparse construit et seuil commun

Au niveau absolu `a=theta U(s)`, supposé supérieur à `a_0`, (H49) donne

```text
B_s=C_mu/[theta³U(s)³ log³(e+theta U(s)/U_*)].
```

On définit, et non choisit arbitrairement plus petit,

```text
r_s=[B_s/(delta_3 |B_1|)]^(1/3)
   =C_4/[U(s)log(e+theta U(s)/U_*)],                (Rs)
C_4=C_mu^(1/3)/[theta(delta_3|B_1|)^(1/3)].
```

Alors chaque boule `B_(r_s)(x_0)` contient au plus la fraction `delta_3` du
superniveau. Le lemme exact du cycle 0014 fournit, pour chaque `x_0`, une
direction où la densité linéaire est au plus `delta_1`. Les rayons plus
petits ne sont pas monotones : une boule centrale de masse `pi/8` donne un
contre-exemple exact.

La condition unique de synchronisation est

```text
log(e+theta U(s)/U_*) >= c_A C_4/nu.                (Sync)
```

Elle est satisfaite au-dessus d’un seuil fini, indépendant du temps si
`C_mu,U_*,a_0,c_1,c_2` le sont. Ce seuil est exponentiel en
`C_mu^(1/3)/nu`. Toute dépendance cachée de `C_mu` au niveau, au temps ou à
une troncature rendrait (Sync) circulaire.

## Fermeture des deux cas spatiaux

Fixons `x_0` et la direction sparse. Sur le diamètre réel du disque complexe,
soit `K` le complément du superniveau.

- Si le centre appartient à `K`,
  `|u(x_0,s)|<=theta U(s)<=theta M U(t)=U(t)/2`.
- Sinon, poser `e_0=u(x_0,s)/|u(x_0,s)|` et
  `v(z)=Re(u(z,s) dot e_0)`. Sur `K`, `v<=U(t)/2`; dans le disque,
  `v<=M U(t)`. La mesure harmonique `H` de `K` vérifie `H>=h*`.

La fonction affine `H/2+(1-H)M` décroît puisque `M>1/2`. Par (P),

```text
|u(x_0,s)|
 <=[H/2+(1-H)M]U(t)
 <=[h*/2+(1-h*)M]U(t)=U(t).
```

Le point `x_0` étant arbitraire, `U(s)<=U(t)`, contradiction avec le temps
d’échappement. Le mot « contradiction » dans le premier cas seul serait
prématuré; c’est l’universalité des deux cas qui ferme la norme `L∞`.

## Lemme conditionnel réparé

### `CONDITIONAL-ENDGAME-SYNCHRONIZATION-1`

Soit `u` une solution classique maximale de NS non forcé sur
`R³x(0,T*)`, `T*<infinity`. Supposons (H49) avec seuil et constantes uniformes,
le théorème local analytique avec un facteur `M` fixé par (P), l’unicité mild,
le principe additif des deux constantes et la borne de Solynin. Alors `T*`
n’est pas un temps singulier.

La preuve est la dichotomie temporelle, suivie dans la branche intérieure de
(Rs), (Sync) et des deux cas harmoniques. Le claim reçoit le statut
`COMPUTATION_ONLY` : la synthèse est une dérivation du laboratoire, non une
preuve formalisée ou revue extérieurement.

Le gain logarithmique est minimal pour cet argument : une queue seulement
critique `|V_s|<=CU(s)^-3` donne `r_s<=C'U(s)^-1`, au même ordre que
`rho_s`, et requiert une petitesse non fournie de `C'/nu`.

## Passe contradictoire

| Attaque | Résidu ou témoin exact | Verdict |
|---|---|---|
| `s=t+T_t^max` est intérieur | `T*=1,t=3/4,T_t=1/4`, donc `T*−s=0` | réfuté; réintroduire les deux branches |
| des asymptotiques sur deux suites se synchronisent | temps `1−1/(4n)` et `1−1/(4n+2)` disjoints | réfuté; toutes les estimations doivent porter sur `s=t+tau_t` |
| un seuil dépendant du temps est finalement franchi | `theta A_n=2^(n−2)<Lambda_n=2^(2n)` | réfuté; seuil uniforme requis |
| tout plus petit rayon est sparse | cœur concentrique de masse `pi/8` | réfuté; utiliser le rayon témoin (Rs) |
| changer `log a` en `log(e+a)` garde `C` | `log(e+a)>log a` pour `a>1` | réfuté; facteur sûr huit au-dessus du seuil normalisé trois |
| le même `M` ferme l’algèbre | `h=1/3,M=5/4,theta=2/5` donne exactement `U(t)` | certifié, branche cœur saturée |
| un `M` analytique différent est sans effet | facteur `3/2` donne `6/5>1` | réfuté |
| scaling, suites disjointes et comparaison cubée des rayons | onze contrôles exacts, zéro échec | certifié algébriquement |

Les trois revues sont de la même famille de modèle et ne constituent pas une
revue externe indépendante. Elles ont toutefois été exécutées avec objectifs
distincts : dérivation, provenance primaire et construction de
contre-systèmes.

## Écart avec le problème Clay

Le cycle ne démontre pas (H49) pour toute donnée de Schwartz divergence-free.
Il n’établit pas non plus les hypothèses amont de la v2 : vorticité
uniformément dans `L^(3/2,infinity)`, profil ponctuel critique et direction
globale dans `bmo_phi`. Les cycles 0015–0018 ont seulement fermé, sous ces
prémisses et plusieurs normalisations explicites, les transferts fonctionnels
conduisant à (H49).

Le résultat exclut donc conditionnellement une classe de scénarios classiques
sur `R³`; il ne traite ni le cas périodique Clay, ni une solution faible après
perte de régularité, ni toute concentration multi-cœur. Il ne constitue ni
une borne globale inconditionnelle ni un blow-up admissible.

`GAP-ENDGAME-SYNCHRONIZATION` est fermé conditionnellement. Le premier verrou
redevient l’extension depuis le cœur actif : une direction définie ou cohérente
seulement sur `{omega>lambda}` ne fournit pas automatiquement la prémisse
globale `bmo_phi` sur les zéros et entre plusieurs cœurs.

## Expérience reproductible

Artefact : `ENDGAME-SYNCHRONIZATION-AUDIT-1`.

```text
python -B experiments/navier-stokes/endgame-synchronization/endgame_synchronization_audit.py
```

- arithmétique : `fractions.Fraction`, aucun flottant;
- discrétisation : aucune grille PDE;
- graine : sans objet;
- contrôles : onze, zéro échec;
- empreinte SHA-256 :
  `41b27f8649977c8a2d564c80418678017eb5d409956c8f3c5e3eb9016f916a3b`;
- prémisses non certifiées par le script : analyticité mild, (H49), Solynin,
  Ransford et existence des temps d’échappement.

## Décision et prochain verrou

Résultat positif borné : le maillon `(49)–(58)` est conditionnellement fermé
avec un seuil quantifié et les deux branches temporelles. Résultat négatif :
le temps « maximal » de la v2, les seuils non uniformes et la monotonie vers
les petits rayons sont invalides tels quels.

État : `CONTINUER`.

Prochaine expérience décisive : construire deux cœurs actifs de vorticité de
directions opposées, séparés par un corridor de zéros de largeur `epsilon`, et
calculer une borne inférieure uniforme du coût `bmo_phi` de toute extension.
Si ce coût reste d’ordre un alors que `phi(epsilon)->0`, l’inférence
« cohérence sur chaque cœur implique direction globale `bmo_phi` » sera
réfutée; sinon, l’extension obtenue donnera le prochain lemme transférable.

## Sources primaires et passes

- Z. Grujić, `arXiv:2607.08866v2`, sections 6.1–7.3.
- Z. Grujić, *Nonlinearity* 26 (2013), DOI
  `10.1088/0951-7715/26/1/289`.
- R. Guberović, *DCDS* 27 (2010), DOI
  `10.3934/dcds.2010.27.231`.
- Z. Grujić et L. Xu, *J. Math. Fluid Mech.* 26 (2024), DOI
  `10.1007/s00021-024-00888-x`.
- A. Yu. Solynin, DOI `10.1007/BF02172470`.
- T. Ransford, DOI `10.1017/CBO9780511623776`.
- `reviews/cycle-0019-analysis.md` : calcul des temps, constantes et rayons.
- `reviews/cycle-0019-literature.md` : versions, attributions et textes
  publiés.
- `reviews/cycle-0019-countermodel.md` : quantificateurs disjoints, seuils et
  saturation harmonique.
