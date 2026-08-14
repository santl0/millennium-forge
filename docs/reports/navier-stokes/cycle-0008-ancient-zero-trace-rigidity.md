# Cycle 0008 — rigidité ancienne mild bornée à trace terminale nulle

Date de coupure : **2026-08-14**.

## Décision du cycle

Le verrou sélectionné était le lemme unique suivant :

> Soit `u` une solution ancienne mild au sens de KNSS de Navier–Stokes
> incompressible 3D, non forcé, de viscosité `1`, sur
> `R³ x (-infinity,0)`. Si `M=sup|u|<infinity` et si la même solution vérifie
> `u(t)->0` dans `D'(R³)` lorsque `t->0-`, alors `u=0`.

Trois actions réversibles ont été notées avant exécution :

| Action | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| lissage KNSS puis rétro-unicité ESS de la vorticité | 3 | 5 | 5 | 5 | **18** |
| pont `D' -> L-infinity`, puis unicité finale Lei–Yang–Yuan | 4 | 4 | 4 | 4 | 16 |
| contre-exemple dans la classe faible/adaptée élargie | 3 | 4 | 5 | 3 | 15 |

La première action a été sélectionnée. La seconde est conservée comme
recoupement; la troisième avait déjà un contre-profil spatialement constant et
ne cible pas la mildness indispensable.

## Équation et type de solution

Le problème borné de ce cycle est exactement

```text
partial_t u + (u dot nabla)u + nabla p = Delta u,
div u = 0,
(x,t) in R³ x (-infinity,0),
f = 0, nu = 1.
```

Il n'y a ni frontière ni condition au bord. La solution est ancienne et mild
au sens de Koch–Nadirashvili–Seregin–Šverák : il existe des temps
`T_j->-infinity` sur lesquels la formule d'Oseen/Leray est valable, donc elle
peut être redémarrée à tout `s<t<0`. Les hypothèses ne sont ni celles d'une
simple solution faible, ni seulement celles d'une solution adaptée locale.

La trace est une **limite** dans `D'(R³)` de cette solution quand `t->0-`.
Assigner arbitrairement la valeur zéro au bord temporel exclu ne suffit pas.

## Échelle et constantes

Sous l'échelle Navier–Stokes

```text
u_lambda(x,t)=lambda u(lambda x,lambda²t),
```

on a

```text
nabla^k partial_t^l u_lambda
  =lambda^(k+2l+1)(nabla^k partial_t^l u)(lambda x,lambda²t).
```

La proposition 4.1 de KNSS donne, après redémarrage à `s=t-h`,

```text
h^(k/2+l)||nabla^k partial_t^l u(s+h)||_infinity
  <= C_(k,l)||u(s)||_infinity
```

pour `h<=epsilon_(k,l)||u(s)||_infinity^-2`. Avec
`h=epsilon_(k,l)/(2M²)`, on obtient uniformément pour tout `t<0`

```text
||nabla^k partial_t^l u(t)||_infinity
  <= C'_(k,l) M^(k+2l+1).                                    (1)
```

La puissance de `M` est exactement celle imposée par l'échelle. Les constantes
dépendent de `(k,l)` et de la normalisation du noyau, mais pas de `t`, du
choix de `T_j` ni de la distance au temps terminal.

## Dérivation analytique

### 1. Promotion de la trace

Sur tout compact `K` et à tout ordre `m`, (1) rend les tranches
`{u(t):-1<t<0}` précompactes dans `C^m(K)`. Toute sous-limite forte est aussi
une limite distributionnelle et vaut donc zéro. Par contradiction séquentielle,

```text
u(t)->0 dans C^m_loc(R³), pour tout m.                         (2)
```

En particulier, `omega=curl u` est bornée et
`omega(t)->0` dans `C^0_loc`. La borne `(k,l)=(0,1)` fournit en outre un module
global `||u(t)-u(s)||_infinity<=C M³|t-s|`, donc une vraie trace globale nulle
dans `L-infinity`. Cette dernière observation n'est pas nécessaire à la route
ESS, mais contrôle la route corroborante.

### 2. Unicité rétrograde de la vorticité

La vorticité vérifie

```text
partial_t omega-Delta omega
  =(omega dot nabla)u-(u dot nabla)omega.
```

Après renversement du temps sur chaque bande finie, (1) donne

```text
|partial_tau omega+Delta omega|
  <= C_M(|omega|+|nabla omega|).                              (3)
```

Les dérivées sont localement de carré intégrable, la vorticité bornée satisfait
la croissance gaussienne requise, et (2) donne la trace terminale ponctuelle
nulle. Le théorème 5.1 d'Escauriaza–Seregin–Šverák s'applique sur chaque
demi-espace translaté et chaque bande finie. L'union des demi-espaces couvre
`R³`; la quantification sur toutes les bandes donne `omega=0` sur tout le
domaine ancien.

### 3. Mode harmonique et jauge mild

Pour chaque temps,

```text
Delta u=nabla div u-curl curl u=0.
```

Le Liouville harmonique et la bornitude globale donnent `u(x,t)=b(t)`. La
formule mild conserve les constantes spatiales et annule
`div(b tensor b)`; elle impose donc `b(t)=b(s)` pour tous `s<t`. La trace
distributionnelle nulle force cette constante à être zéro.

Le lemme conditionnel est ainsi fermé. Il s'agit d'une dérivation du
laboratoire à partir de théorèmes publiés, pas d'un résultat attribué mot pour
mot à une source et pas d'un `PAPER_PROOF`.

## Sources et veille différentielle

- [KNSS, Acta Mathematica 203 (2009)](https://doi.org/10.1007/s11511-009-0039-6) : définition ancienne mild, proposition 4.1 et rigidité des modes constants mild.
- [ESS, Russian Mathematical Surveys 58 (2003)](https://www.mathnet.ru/eng/rm609) et [article d'unicité rétrograde](https://doi.org/10.1007/s00205-003-0263-8) : inégalité de vorticité et Carleman sur domaine extérieur.
- [Lei–Yang–Yuan, IMRN 2024](https://academic.oup.com/imrn/article/2024/20/13417/7769704) : unicité de solutions mild bornées à même donnée finale; contrôle corroborant seulement.
- [Pineau–Vicol, arXiv:2607.09619v2](https://arxiv.org/abs/2607.09619) : exclusions récentes de profils RSS/DSS/RDSS backward sous borne Type I; ni rotation intermédiaire ni Type II général.

La veille a corrigé le statut de Lei–Yang–Yuan : l'article est publié dans
l'IMRN 2024, malgré l'absence de version arXiv postérieure à `v1`. Elle a aussi
ajouté l'article ESS spécifiquement consacré à l'unicité rétrograde et la
prépublication Pineau–Vicol révisée le 2026-08-06.

## Expérience décisive

`ANCIENT-ZERO-TRACE-RIGIDITY-AUDIT-1` encode neuf obligations de la route
principale et deux contrôles de la route Lei–Yang–Yuan. Le script n'intègre pas
la PDE et ne prétend pas certifier les théorèmes sources. Il contrôle sans
flottant :

- l'exhaustivité annoncée des prémisses et dépendances;
- les exposants d'échelle des quatre termes NS;
- la puissance `M^(k+2l+1)` pour `0<=k<=3`, `0<=l<=2`;
- un module temporel rationnel témoin;
- la décroissance exacte de la queue de Duhamel sur `delta=4^-j`;
- cinq contre-profils, chacun rejeté par au moins une porte nécessaire.

Commande :

```text
python experiments/navier-stokes/ancient-zero-trace-rigidity/rigidity_audit.py
```

Résultat : `PASSED`, `assertion_failure_count=0`. Les SHA-256 sont :

```text
rigidity_obligations.json
d0d6da661fb195f8eb44caf013e0ffe430fbb31b575212172d07ceccf860e078

rigidity_audit.py
5bd28f4e420744e3ebdda9b672afb6d6c050b906bec160476510709ba5588cf5
```

Il n'y a aucune discrétisation spatiale ou temporelle, donc aucun résidu PDE
continu certifié. Le résidu annoncé est exclusivement un résidu logique et
algébrique exact.

## Passe contradictoire

Cinq attaques sont conservées :

1. `u=b(t)`, `p=-b'(t) dot x` réfute la version sans mildness;
2. une constante non nulle avec valeur terminale artificiellement assignée
   réfute une notion de trace sans limite;
3. des tranches divergence-free à haute fréquence perdent les bornes de
   vorticité et ne sont pas une même trajectoire ancienne mild;
4. des paquets traduits à l'infini montrent que `D'` seule ne donne pas une
   trace globale, mais violent le module temporel uniforme issu de (1);
5. la limite KNSS maximum-normalisée satisfait mildness et bornitude mais
   porte `|v(0,0)|=1`, donc précisément pas la trace nulle requise.

La lecture du texte intégral accessible de Lei–Yang–Yuan (`arXiv v1`) a relevé
trois anomalies : un renvoi interne erroné, un facteur `1/2` absent dans une
identité de Laplacien et une discordance `-k/-2k` de poids. Elles semblent
réparables localement et ne réfutent pas l'article publié. Comme le texte
éditeur intégral n'a pas été comparé, cette route a été rétrogradée de support
principal à recoupement.

Trois revues séparées ont porté sur les sources, la dérivation PDE et la veille
des annonces. Elles utilisent toutefois la même famille de modèles Codex et ne
constituent pas une revue externe indépendante.

## Écart exact avec Clay

Le graphe conditionnel

```text
ancienne + mild KNSS + borne globale L-infinity + vraie trace D' nulle
  -> u=0
```

est fermé. Aucune chaîne auditée ne produit cependant toutes ces prémisses sur
un même objet non trivial :

- ESS produit une limite éternelle adaptée avec trace locale nulle et
  `L-infinity_tL³_x`, sans borne ponctuelle globale ni mildness KNSS;
- GKP produit un élément critique mild forward et une trace `S'`, pas une
  ancienne globalement bornée;
- KNSS produit une ancienne mild bornée, mais avec normalisation terminale non
  nulle;
- les zooms Type II de Seregin audités dégénèrent vers Euler.

Le nouveau verrou dominant est donc `GAP-HYBRID-INHERITANCE`, pas un théorème
de Liouville supplémentaire.

## Décision de poursuite

**CONTINUER.** Le prochain test doit isoler le défaut de commutation entre la
limite des zooms `k->infinity` et la limite terminale `t->0-`. Il recherchera
le module uniforme ou l'équi-intégrabilité minimale qui transmettrait la trace
sur une extraction maximum-normalisée, puis testera si cette hypothèse est
réellement nouvelle ou équivaut déjà à une borne critique telle que
`L-infinity_tL³_x`.
