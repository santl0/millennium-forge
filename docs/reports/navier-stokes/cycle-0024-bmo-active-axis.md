# Cycle 0024 — extraction d'un axe actif depuis log-BMO

Date de gel : 2026-08-14.

Statut : dérivation interne falsifiable et calcul rationnel exact. Les revues
séparées sont produites par la même famille de modèles et ne constituent pas
une validation externe. Aucun résultat n'est une preuve Clay.

## Décision du cycle

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| extraire un axe depuis log-BMO et une fraction active minimale | 5 | 5 | 5 | 5 | **20** |
| coercivité par matrice de covariance sans axe | 5 | 3 | 5 | 4 | 17 |
| jet intermittent à amplitude non bornée | 5 | 2 | 4 | 4 | 15 |

Le verrou sélectionné est `GAP-MULTICORE-ANGULAR-CASCADE`. Le lemme actif
teste si les zéros ou plusieurs phases peuvent réellement empêcher la
normalisation des moyennes lorsqu'une borne de tranche et une masse critique
par coquille sont déjà disponibles. L'expérience décisive suit toutes les
constantes sur des boules dyadiques.

## Équation et type de solution

Le problème Clay de référence est toujours

```text
partial_t u+(u dot nabla)u=-nabla p+nu Delta u,
div u=0,                 omega=curl u,                 nu>0
```

sur `R³`, sans frontière et sans force, pour une donnée initiale lisse,
divergence-free et d'énergie finie. Le cycle ne construit aucune solution.
Il examine la condition cinématique nécessaire `div W=0` pour

```text
W(x)=r^-2 Omega(s,theta),
s=log(R_*/r),
Phi=|Omega|,
xi=Omega/Phi sur A={Phi>0}.                             (1)
```

La direction utilisée dans la semi-norme est une extension mesurable `zeta`
telle que

```text
|zeta|<=1 partout,          zeta=xi sur A.              (2)
```

Cette convention inclut l'extension par zéro, mais ne l'impose pas.

## Hypothèses du lemme

Fixons un rapport `q∈(0,1)`, `L=-log q`, et les profondeurs

```text
S_k=S_0+kL,              R_k=R_*exp(-S_k).
```

Supposons, pour tout `k` assez grand :

1. `Omega` est localement `W^(1,1)` et `W` est divergence-free;
2. `0<=Phi<=M` presque partout;
3. chaque bloc extérieur vérifie

   ```text
   integral_(S_k)^(S_k+L)<Phi^(3/2)> ds>=kappa>0;       (3)
   ```

4. l'extension (2) a une oscillation logarithmique sur les boules centrées :

   ```text
   epsilon_k:=average_(B_(R_k))|zeta-(zeta)_(B_(R_k))|
   <=B/(1+S_k).                                         (4)
   ```

La condition globale `bmo_(1/|log r|)` implique (4), mais le lemme n'utilise
que cette sous-famille de boules.

## Étape 1 : la masse empêche la moyenne de s'annuler

Dans `B_(R_k)`, la profondeur supplémentaire `t=s-S_k` a densité volumique
normalisée `3exp(-3t)`. Puisque

```text
Phi^(3/2)<=M^(3/2) 1_A,
```

(3) donne une fraction active physique uniforme

```text
a_k:=|A∩B_(R_k)|/|B_(R_k)|
 >= a_*:=3q³kappa/M^(3/2)>0.                            (5)
```

Cette constante volontairement grossière n'utilise que le premier bloc
intérieur. La passe analytique séparée donne la constante optimale lorsque
tous les blocs ont largeur `L`. Avec

```text
alpha=kappa/[L M^(3/2)],
beta=[exp(3L alpha)-1]/[exp(3L)-1],
```

le principe de baignoire radial donne une fraction active au moins `beta`
dans chaque coquille, donc dans chaque boule. Le reste du rapport conserve
`a_*`, plus simple et déjà strictement positif.

Posons `m_k=(zeta)_(B_(R_k))`. Sur l'ensemble actif, `|zeta|=1`, donc

```text
|zeta-m_k|>=1-|m_k|.
```

Après moyenne,

```text
|m_k|>=1-epsilon_k/a_*.                                 (6)
```

Pour `k` assez grand, `m_k` est donc non nul. L'axe canonique

```text
e_k=m_k/|m_k|                                            (7)
```

vérifie

```text
average_(B_(R_k))|zeta-e_k|
 <=(1+1/a_*)epsilon_k.                                  (8)
```

Les zéros et les multicœurs ne peuvent donc annuler la moyenne sans payer une
oscillation d'ordre un, tant que (5) demeure uniforme.

## Étape 2 : les axes imbriqués ont une variation sublinéaire

Écrivons `C_*=1+1/a_*`. Comme
`|B_(R_k)|/|B_(R_(k+1))|=q^-3`, (8) sur deux boules imbriquées donne

```text
|e_(k+1)-e_k|
 <=C_*[q^-3 epsilon_k+epsilon_(k+1)].                   (9)
```

On relie `e_k` à `e_(k+1)` par le plus court arc de grand cercle. Sa longueur
est au plus deux fois la corde. Une interpolation absolument continue
`e(s)` satisfait alors

```text
Var(e;[S_1,S_N])
 <=2C_*(q^-3+1) sum_(k=1)^(N-1) epsilon_k.              (10)
```

Or (4) et `S_k=S_0+kL` donnent

```text
sum_(k=1)^N epsilon_k=O(log N)=o(N).                    (11)
```

La variation de l'axe extrait est donc sous-linéaire dans la profondeur
logarithmique.

## Étape 3 : l'erreur directionnelle est aussi sublinéaire

La moyenne physique (8) contrôle le bloc logarithmique non pondéré, car
`exp(-3t)>=q³` pour `0<=t<=L` :

```text
integral_(S_k)^(S_k+L)<Phi|xi-e_k|>ds
 <=[M/(3q³)]C_*epsilon_k.                               (12)
```

Le mouvement de l'interpolation ajoute au plus

```text
2ML C_*(q^-3+1)epsilon_k.                               (13)
```

Ainsi, avec l'axe continu construit,

```text
D(S_1,S_N)=integral <Phi|xi-e(s)|>ds=O(log N)=o(NL).    (14)
```

Les hypothèses du budget mobile `NS-WANDERING-AXIS-MOMENT-BUDGET` sont
maintenant satisfaites avec variation et erreur sublinéaires. Pourtant la
masse (3) force, sur `N` blocs,

```text
N*2kappa²/(3M²L)
 <=M+(M/2)Var(e)+D.                                     (15)
```

Le membre gauche est linéaire et le membre droit sous-linéaire, à la constante
de bord `M` près. La contradiction exclut le profil.

## Échelle des quantités

Sous le scaling Navier–Stokes

```text
u_lambda(x,t)=lambda u(lambda x,lambda²t),
W_lambda(x,t)=lambda²W(lambda x,lambda²t),
```

`Phi`, `M`, `kappa`, `q`, `L`, `zeta`, `epsilon_k`, `a_*`, les axes et les
deux budgets de (15) sont sans dimension. L'identité critique reste

```text
integral_shell |W|^(3/2)dx
=4pi integral_block <Phi^(3/2)>ds.                      (16)
```

Aucune quantité supercritique contrôlée par l'énergie ne produit (3) ou la
borne ponctuelle `Phi<=M`.

## Test adverse et frontière exacte

La borne de tranche est indispensable. Sur une fraction active

```text
a_n=n^-3,
```

prenons une direction constante, l'extension par zéro, et une amplitude
`Phi_n=n²`. Alors

```text
<Phi_n^(3/2)>=1,
|m_n|=a_n->0,
MO(zeta_n)=2a_n(1-a_n)->0.                              (17)
```

La masse critique reste fixe tandis que la moyenne directionnelle devient
non normalisable. Cette famille ne constitue pas une vorticité solénoïdale;
elle réfute exactement l'extraction si `Phi<=M` est supprimée.

Autres attaques :

1. Une simple borne faible-`L^(3/2)` ne fournit pas `Phi<=M`; (17) est
   compatible avec une concentration critique de plus en plus haute.
2. Si la masse n'est imposée que sur des blocs lacunaires, les boules entre
   eux peuvent avoir une fraction active nulle et les axes ne se raccordent
   pas.
3. L'extension doit être la même fonction dans toutes les boules. Choisir
   a posteriori une valeur différente sur les zéros à chaque échelle serait
   circulaire.
4. Le résultat n'exige pas `|zeta|=1` hors du cœur; il utilise seulement
   `|zeta|<=1` et l'unité sur le cœur actif.
5. La BMO globale est plus forte que (4). Le calcul n'établit aucune réciproque
   depuis les seules boules centrées.
6. La pression et Biot–Savart n'apparaissent pas : le profil est exclu avant
   ces portes. Si `Phi<=M` est abandonnée, elles redeviennent des obligations
   ouvertes.
7. Aucun passage depuis une solution ou une suite de zooms Clay ne produit les
   hypothèses de profil, de masse et de tranche.

## Passes contradictoires séparées

Trois audits distincts sont conservés, sans les qualifier d'indépendants au
sens externe :

- `reviews/cycle-0024-analysis.md` optimise la fraction active par le principe
  de baignoire et recalcule une contradiction quantitative générale;
- `reviews/cycle-0024-countermodel.md` teste zéros, phases antipodales,
  lacunes, coquilles minces et centres non emboîtés;
- `reviews/cycle-0024-literature.md` corrige le cas globalement unitaire par
  l'identité de variance et vérifie l'absence de théorème d'extension adapté.

La synthèse retient la constante grossière (5), suffisante et plus facile à
auditer. Le contre-audit multicentres ne réfute pas le lemme fixé : les
boules du profil ponctuel gardent ici le même centre. Il identifie une autre
porte lors d'une extraction espace-temps à centre mobile. L'attaque décisive
dans le cadre fixé reste (17), qui détruit précisément la borne d'amplitude.

## Veille différentielle

La recherche primaire ciblée ne trouve aucun théorème qui fournisse
simultanément (3), `Phi<=M` et (4) depuis les données Clay. La prépublication
Grujić `arXiv:2607.08866v2` suppose une direction log-BMO et une concentration
critique. Sa section 2.3 appelle `xi` un champ unitaire global et fixe sa norme
de base à un : sous cette lecture littérale, la non-annulation asymptotique des
moyennes suit déjà de la petite oscillation, sans (5). Mais la valeur de `xi`
sur `{omega=0}` n'est pas déterminée par la vorticité; l'existence d'une même
extension unitaire log-BMO reste une hypothèse géométrique supplémentaire.
Le présent lemme couvre aussi l'extension par zéro grâce à la fraction active.

Miller 2021 suppose plutôt un
gradient spatial borné de l'axe mobile et un contrôle critique transverse.
Lei–Ren–Tian v1 impose un cône fixe aux grands niveaux dans son théorème 1.1,
ou une condition pairwise sur toute vorticité non nulle dans son corollaire
1.6. Aucun ne produit la borne de tranche depuis l'énergie.

## Verdict et écart avec Clay

Résultat positif borné : sous amplitude critique uniformément bornée, masse
critique non dégénérée sur chaque bloc et direction étendue avec oscillation
centrée `O(1/|log r|)`, la condition `div W=0` est impossible jusqu'au centre.
Le lemme construit l'axe qui manquait au cycle 0023 et couvre les zéros et
configurations multicoeurs tant que leur extension BMO et leur fraction active
restent uniformes.

Résultat négatif : la borne faible-`L^(3/2)` seule ne suffit pas. Une
intermittence angulaire de hauteur croissante conserve la masse critique tout
en faisant disparaître la moyenne active.

Le claim reste `COMPUTATION_ONLY`. Il ne s'applique pas à toute solution Clay,
car ni `Phi<=M`, ni la masse par bloc, ni l'ansatz spatial ne sont hérités d'un
blow-up général. Le verrou actif devient
`GAP-UNBOUNDED-ANGULAR-INTERMITTENCY` : remplacer la borne de tranche par un
contrôle critique plus faible ou construire un profil intermittent réellement
solénoïdal et solution-admissible.

## Reproduction

```text
python -B experiments/navier-stokes/bmo-axis-extraction/bmo_axis_extraction_audit.py
```

Le script utilise uniquement `fractions.Fraction`. Il enferme exactement
`log 2` entre `6931/10000` et `6932/10000`, vérifie les constantes dyadiques,
les enveloppes harmoniques et le contre-profil intermittent en 66 contrôles
sans échec. Pour

```text
q=1/2, M=1, kappa=1/4, B=1/100,
```

il obtient `a_*=3/32`, `C_*=35/3` et certifie une première contradiction à
`N=2^10-1=1023` blocs avec marge rationnelle strictement positive. Aucune
grille, aucun flottant, aucune graine et aucun résidu PDE ne sont utilisés.
Empreinte SHA-256 :
`e2603081b46d4aab9599e9681eaf50cbc460df46e3b6d1c3d2383b0a71005e0e`.
