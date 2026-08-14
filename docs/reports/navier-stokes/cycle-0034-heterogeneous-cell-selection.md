# Cycle 0034 — sélection de cellules hétérogènes par registre BV

Date de gel : 2026-08-14.

Statut : dérivation analytique interne, contre-exemple mesurable exact et
certificat algébrique fini. Aucun énoncé nouveau de ce rapport n'est classé
`PAPER_PROOF` et aucune évolution de Navier–Stokes n'est construite.

## Décision adaptative

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| pigeonhole direct sur les seules quasi-normes cellulaires | 2 | 5 | 5 | 4 | 16 |
| contre-distribution dyadique puis sélection sous registre BV | 4 | 5 | 5 | 5 | **19** |
| décomposition de profils faible-endpoint curl-compatible générale | 5 | 2 | 4 | 5 | 16 |

La deuxième action est retenue. Elle sépare un résultat négatif exact — les
quasi-normes seules ne sélectionnent aucune cellule — d'un lemme positif où
la fermeture compacte de chaque cellule est enregistrée par sa variation
totale. Cette hypothèse est ensuite dérivée pour une classe pure-swirl épaisse,
à aspect borné et à plateau effectif.

## Équation et type d'objet

Le problème Clay de référence reste

```text
partial_t u+(u·nabla)u=-nabla p+nu Delta u,
div u=0, nu>0, f=0,
```

sur `R3` ou `T3`. Le cycle travaille seulement sur `R3`, à temps fixé, avec
des données initiales compactes divergence-free. Il ne construit ni solution
stationnaire, ni trajectoire forte, ni solution ancienne.

Pour une fonction mesurable `f`, la convention est

```text
K_p(f)=sup_(lambda>0) lambda |{|f|>lambda}|^(1/p).
```

## Résultat négatif : la sélection normique est fausse

Pour `N>=2`, prenons des cellules disjointes `V_j`, `0<=j<N`, de volume
`N^-1`, et des sous-ensembles `E_j` de volume

```text
|E_j|=N^-1 2^(-3j/2).
```

Définissons

```text
u_j=1_(V_j)e,
w_j=N^(2/3)2^j 1_(E_j)e,
```

avec `e` unitaire. Alors, exactement,

```text
K_(u,j)=N^(-1/3),
K_(w,j)=1,
K_u=1,
1<=K_w<=(1-2^(-3/2))^(-2/3).
```

Ainsi

```text
sup_j K_(u,j)/K_(w,j)=N^(-1/3)->0,
```

alors que `K_u/K_w` reste uniformément positif. Toute implication

```text
sup_j K_(u,j)/K_(w,j)>=c(K_u/K_w)^q
```

fondée seulement sur la disjonction et les quasi-normes faibles est donc
réfutée, quels que soient `c,q>0` fixés.

Le premier quantificateur faux est la synchronisation implicite du niveau
presque optimal de la vitesse avec les niveaux, différents pour chaque
cellule, qui réalisent la quasi-norme du curl.

Ce contre-exemple n'est pas curl-compatible. Sa masse de retour vaut

```text
integral |w_j|=N^(-1/3)2^(-j/2),
```

et perd le facteur nécessaire pour fermer une vitesse de plateau uniforme.

## Lemme actif : sélection sous registre BV

Soit une famille finie de cellules mesurables disjointes `Q_j` dans `R3`.
Les champs `U_j,W_j` sont supportés dans `Q_j`, et

```text
U=sum_j U_j,
W=sum_j W_j.
```

Supposons qu'il existe des constantes uniformes positives
`c_0,c_1,c_2,C_0,C_2`, ainsi que des amplitudes `A_j>0`, des volumes
effectifs `v_j>0` et des ensembles `E_j subset Q_j`, tels que

```text
|Q_j|<=C_0 v_j,
|E_j|>=c_0 v_j,
c_2 A_j<=|U_j| sur E_j,
|U_j|<=C_2 A_j sur Q_j,
integral_(Q_j)|W_j|>=c_1 A_j v_j^(2/3).       (1)
```

Écrivons

```text
K_u=||U||_(L^(3,infinity)),
K_w=||W||_(L^(3/2,infinity)).
```

### Théorème 1 — sélection BV hétérogène

Si `K_u>0` et `K_w<infinity`, il existe une cellule `j` telle que

```text
boxed{
K_(u,j)>=c_BV K_u^2/K_w,
K_(u,j)/K_(w,j)>=c_BV (K_u/K_w)^2,}           (2)
```

où `K_(u,j)=||U_j||_(L^(3,infinity))`,
`K_(w,j)=||W_j||_(L^(3/2,infinity))` et `c_BV>0` ne dépend que des constantes
de (1). Amplitudes, volumes, rayons et distances entre cellules peuvent être
arbitraires.

## Preuve du théorème 1

Posons

```text
epsilon=max_j K_(u,j).
```

Le plateau effectif de (1) donne

```text
K_(u,j)>=a_0 A_j v_j^(1/3),
a_0=c_2 c_0^(1/3).                              (3)
```

Choisissons un niveau `lambda>0` presque optimal pour `K_u`. Toute cellule
qui rencontre `{|U|>lambda}` vérifie `A_j>lambda/C_2`. Si `J_lambda` est cet
ensemble d'indices et `S=sum_(J_lambda)v_j`, alors

```text
lambda S^(1/3)>=(1-eta)C_0^(-1/3)K_u.          (4)
```

Pour `j in J_lambda`, (3) implique

```text
v_j^(1/3)<=C_2 epsilon/(a_0 lambda).
```

Par conséquent,

```text
sum_(J_lambda)v_j^(2/3)
 >=a_0 lambda S/(C_2 epsilon).                  (5)
```

Le registre BV de (1) et `A_j>lambda/C_2` donnent, sur
`Q=union_(J_lambda)Q_j`,

```text
integral_Q |W|
 >=c_1 a_0 lambda^2 S/(C_2^2 epsilon).         (6)
```

La disjonction est utilisée ici : aucune annulation entre cellules ne précède
la valeur absolue. D'autre part, l'inégalité faible-Lorentz exacte

```text
integral_E |f|<=3||f||_(L^(3/2,infinity))|E|^(1/3)
```

et `|Q|<=C_0S` donnent

```text
integral_Q |W|<=3K_w(C_0S)^(1/3).              (7)
```

En combinant (4), (6) et (7), puis en faisant `eta->0`,

```text
epsilon>=
 [c_1 a_0/(3C_2^2C_0)] K_u^2/K_w.             (8)
```

Une famille finie atteint son maximum. Enfin `K_(w,j)<=K_w` par monotonie de
la fonction de distribution, ce qui transforme (8) en (2).

## Corollaire pure-swirl épais

Pour chaque `j`, soient `R_j>0`, `z_j in R` et

```text
F_j in C_c^infinity((0,infinity)×R),
supp F_j subset
 {R_j/2<r<3R_j/2, |z-z_j|<Lambda R_j},          (9)
```

avec `Lambda` uniforme. Posons

```text
U_j=(R_j/r)F_j e_theta,
W_j=curl U_j=(R_j/r)(-partial_z F_j e_r
                     +partial_r F_j e_z).       (10)
```

Supposons les boîtes tridimensionnelles de (9) disjointes, ainsi que des
constantes uniformes `c_A,C_A,c_E>0` telles que

```text
||F_j||_infinity<=C_A A_j,
|{|F_j|>=c_A A_j}|_(dr dz)>=c_E R_j^2.          (11)
```

Les quatre premières conditions de (1) valent avec `v_j=R_j^3`. Pour la
dernière, on scinde le superniveau de `|F_j|` par signe et on tronque

```text
G_j=(sigma_j F_j-c_A A_j/2)_+.
```

Coaire et isopérimétrie plane donnent

```text
TV(G_j)>=c A_jR_j.
```

Comme

```text
||curl[(R_j/r)G_j e_theta]||_1=2pi R_j TV(G_j),
```

et `|nabla G_j|<=|nabla F_j|`, on obtient

```text
integral |W_j|>=c A_jR_j^2
                 =c A_jv_j^(2/3).              (12)
```

Le théorème 1 sélectionne donc une vraie cellule pure-swirl dont le rapport
endpoint est au moins quadratique dans le rapport global.

## Raccord au gate directionnel du cycle 0033

Le claim `NS-BOUNDED-CROSS-SECTION-DIRECTION-GATE` s'applique à la cellule
sélectionnée. Pour toute extension globale `zeta` de la direction de `W`, sa
restriction à la boule de cette cellule est une extension admissible de la
direction de `W_j`; les valeurs portées par d'autres cellules sont libres là
où `W_j=0`. Il vient

```text
MO_(B_j)(zeta)
 >=c_Lambda(K_(u,j)/K_(w,j))^6
 >=c_(Lambda,BV)(K_u/K_w)^12.                  (13)
```

Ainsi, sous gates globaux uniformes, les cellules épaisses, disjointes et à
plateau effectif ne peuvent toutes masquer leur direction. Si les rayons des
cellules sélectionnées tendent vers zéro, (13) force la divergence du poids
log-BMO. Les gates seuls ne prouvent toutefois pas que le rayon sélectionné
tend vers zéro.

## Expérience décisive exacte

Le certificat `HETEROGENEOUS-CELL-SELECTION-1` vérifie deux objets.

1. **Contre-exemple dyadique.** Quatre lignes fermées `N=8^n`, et deux lignes
   entièrement matérialisées, reproduisent `K_u^3=1`,
   `1<=K_w^3<=64/49` et le collapse local `N^-1` des rapports cubiques. Le
   déficit du registre BV vaut exactement `2^(n-j)`.
2. **Modèle enregistré.** Pour `v_j=r_j^3`, `q_j=s_j^3` et
   `B_j=A_jr_j^2/s_j^3`, il vérifie exactement

   ```text
   B_jq_j=A_jv_j^(2/3),
   epsilon>=K_u^2/(3K_w),
   max_j(K_(u,j)/K_(w,j))>=K_u^2/(3K_w^2).
   ```

Le script parcourt 1 152 familles hétérogènes, 9 792 cellules et exécute
31 746 assertions rationnelles exactes, sans graine ni racine flottante.
Empreinte SHA-256 :
`d918ff7ec5e200d388cde1d3ed5230ebdd4535bc65fc3b94a2c7ac21c0962763`.

## Veille primaire et portée des outils de profils

Lions, Solimini, Gérard, Jaffard, Koch et Bahouri–Cohen–Koch exigent une
mesure variationnelle ou une borne dans un espace source plus fort avant de
produire compacité ou profils. Aucun de leurs théorèmes ne décompose une paire
arbitraire seulement bornée dans `L^(3,infinity)` et
`L^(3/2,infinity)`, ni ne synchronise automatiquement les profils de `U` et
`curl U`.

Barker–Prange obtiennent le raccord dynamique publié le plus proche : sous
borne Type I et en supposant déjà un point singulier, ils localisent vitesse
critique et enstrophie autour du même centre. Leur résultat n'est pas le lemme
statique (2) et ne couvre pas Type II général.

La veille 2025–2026 laisse inchangés Lei–Ren–Tian `2501.08976v1`, Grujić
`2511.00725v3`, Grujić `2607.08866v2`, Barker `2510.20757v3` et les annonces
Shahmurov maintenues en quarantaine.

## Passes contradictoires séparées

- L'audit analytique réfute la sélection normique, démontre une sélection
  linéaire sous registre synchronisé et isole le niveau de curl comme premier
  quantificateur faux; empreinte
  `c9e86e38966aa6d5843a52c1624ae6bf9e8e2cbad2dcc48d26c9e5c83356697d`.
- Le contre-modèle recalcule les distributions totales, identifie le retour
  compact obligatoire et fournit une seconde preuve du lemme BV; empreinte
  `cbb7cb4a37ac4f5d7fbbdbf35e852f1e0c303d379dfc777422f8b5b87405cc67`.
- La revue primaire montre que concentration-compacité, profils séparés et
  Biot–Savart global ne fournissent pas la même cellule aux deux endpoints;
  empreinte
  `1f4e41b64845ca14b745bf71f657f4ce0db18d287068eb45b57021cb7c715631`.

Ces passes sont produites par des agents IA du même environnement. Elles sont
contradictoires et reproductibles, mais pas indépendantes au sens éditorial.

## Passe contradictoire principale

1. **Somme de normes.** Aucune somme triangulaire n'est utilisée; les fonctions
   de distribution totales sont calculées avant le supremum.
2. **Couple abstrait pris pour un curl.** Le contre-exemple ne satisfait pas
   `W=curl U`; il réfute seulement le maillon normique.
3. **Amplitude `A_j` non maximale.** La borne supérieure de (1) est explicite;
   sans elle, le seuil global ne sélectionne pas `J_lambda`.
4. **Support pris pour plateau.** Le volume `v_j` est effectif grâce à `E_j`;
   une queue infinitésimale ne peut pas l'épaissir artificiellement.
5. **Boîte trop grande.** `|Q_j|<=C_0v_j` est indispensable à (7). Des
   corridors ou queues de volume non uniforme restent hors du théorème.
6. **Signes.** La troncature du corollaire choisit un signe avant coaire; le
   changement de signe ne modifie pas la direction BMO après multiplication
   globale.
7. **Annulation.** Les supports complets des cellules sont disjoints. Des
   curls qui se chevauchent peuvent s'annuler avant la valeur absolue et ne
   sont pas couverts.
8. **Rayon majeur.** Le facteur cylindrique est uniforme seulement loin de
   l'axe et sous aspect borné; les régimes dégénérés doivent être recalculés.
9. **Localisation de Biot–Savart.** Couper `U` crée
   `nabla chi cross U` et un défaut de divergence critiques. Le théorème ne
   prétend pas reconstruire localement la vitesse depuis le curl.
10. **Échelle sélectionnée.** (2) sélectionne un rapport, pas nécessairement
    une cellule dont `R_j->0` dans une suite.
11. **PDE.** Pression, interactions lointaines, diffusion et stretching ne
    sont pas calculés.
12. **Clay.** (13) exclut une classe de profils statiques; il ne prouve ni
    régularité globale, ni absence de tout blow-up, ni singularité admissible.

## Résultat scientifique et pivot

Le résultat négatif est définitif dans la catégorie mesurable : les seules
quasi-normes faibles n'imposent aucune cellule commune. Le résultat positif
ferme les familles pure-swirl disjointes à cellules épaisses, aspect borné,
plateau effectif et boîte comparable; elles possèdent une cellule dont le
rapport local est quadratique dans le rapport global, puis une oscillation
directionnelle de puissance douze.

Le nouveau verrou est
`GAP-DEGENERATE-CELL-REGISTER-OR-OVERLAP`. Il reste à construire ou exclure :

```text
queues/corridors avec |Q_j|/v_j->infinity,
plateaux sans densité uniforme,
supports de curl qui se chevauchent et s'annulent,
ou sélection dynamique d'une échelle R_j->0.
```

## Reproduction

```text
python -B experiments/navier-stokes/heterogeneous-cell-selection/heterogeneous_cell_selection_audit.py
```

Le certificat prouve seulement des identités finies. Coaire, isopérimétrie,
registre BV continu, pression et passage à une trajectoire restent analytiques.
