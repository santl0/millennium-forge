# Cycle 0023 — budget de moment pour un axe mobile

Date de gel : 2026-08-14.

Statut : dérivation interne falsifiable, calcul rationnel exact et trois passes
contradictoires séparées par la même famille de modèles. Aucun résultat n'est
une preuve de régularité globale ou de blow-up.

## Décision du cycle

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| budget du premier harmonique pour un axe mobile | 5 | 5 | 5 | 5 | **20** |
| test centré log-BMO pour rotation lente/persistante | 4 | 5 | 5 | 5 | 19 |
| construction solénoïdale mobile par harmoniques croissants | 5 | 2 | 4 | 4 | 15 |

Le verrou sélectionné est `GAP-WANDERING-AXIS-PROFILE`. Le lemme actif
quantifie la variation minimale de l'axe nécessaire pour compenser la perte du
moment sphérique du cycle 0022. L'expérience décisive compare deux familles
radiales : rotation uniforme et dérive logarithmique.

## Équation et type de solution

Le problème Clay de référence reste Navier–Stokes incompressible, visqueux,
non forcé, sur `R³`, sans frontière :

```text
partial_t u+(u dot nabla)u=-nabla p+nu Delta u,
div u=0,                 omega=curl u,                 nu>0.
```

Les données Clay sont lisses, divergence-free et d'énergie finie. Ce cycle ne
construit aucune trajectoire et ne revendique aucune solution faible, forte,
mild ou adaptée. Il examine seulement la porte cinématique nécessaire
`div omega=0` pour un profil spatial dans une boule ponctuée.

Fixons

```text
r=|x|,  theta=x/r,  s=log(R_*/r),
W(x)=r^-2 Omega(s,theta),  Omega=Omega_r theta+Omega_T=Phi xi.
```

La formule exacte est

```text
div W=r^-3[div_(S²)Omega_T-partial_s Omega_r].           (1)
```

## Lemme actif : budget d'un axe mobile

La moyenne sphérique normalisée est notée `< >`. Supposons :

1. `Omega` est localement `W^(1,1)` et (1) s'annule;
2. `0<=Phi<=M`;
3. pour des constantes `L,kappa>0`, tout bloc vérifie

   ```text
   integral_S^(S+L)<Phi^(3/2)> ds >= kappa;              (2)
   ```

4. `e:[s_0,infinity)->S²` est absolument continu sur tout compact;
5. l'erreur directionnelle pondérée est

   ```text
   D(S,T)=integral_S^T <Phi|xi-e(s)|> ds.                (3)
   ```

Définissons

```text
mu_s(theta)=e(s) dot theta,
b(s)=<theta Omega_r>,
J(s)=e(s) dot b(s)=<mu_s Omega_r>.
```

Alors, presque partout,

```text
J'=e' dot b
   -<Phi(1-mu_s²)>
   -<Phi(xi-e) dot nabla_(S²)mu_s>.                      (4)
```

En effet, `partial_s Omega_r=div_(S²)Omega_T`, puis une intégration par
parties donne le second membre. Les bornes ponctuelles sont

```text
|J|<=M/2,
|<(e' dot theta)Omega_r>|<=M|e'|/2.                     (5)
```

La minoration par calottes du cycle 0022 et Cauchy–Schwarz donnent, sur
chaque bloc,

```text
integral_S^(S+L)<Phi(1-mu_s²)> ds
  >= a_0 := 2kappa²/(3M²L).                              (6)
```

Sur `N` blocs consécutifs, (4)–(6) impliquent le certificat quantitatif

```text
N a_0
 <= M + (M/2) Var(e;[S,S+NL]) + D(S,S+NL).              (7)
```

Par conséquent, si

```text
Var(e;[S,S+T])=o(T),        D(S,S+T)=o(T),               (8)
```

le profil ne peut s'étendre à une profondeur logarithmique infinie. Plus
précisément, tout candidat survivant avec `D/T->0` doit satisfaire

```text
liminf_(N->infinity) Var(e;[S,S+NL])/(NL)
  >= 4kappa²/(3M³L²).                                   (9)
```

Cette condition est nécessaire, non suffisante. Elle ne contrôle ni les
harmoniques supérieurs, ni Biot–Savart, ni la viscosité.

## Test décisif : rotation persistante contre dérive lente

Considérons uniquement une direction radiale `xi(x)=e(s)` et les boules
centrées au point du profil. Sur `B_R(0)`, si `S=log(R_*/R)`, la profondeur
supplémentaire `t=s-S` a densité volumique normalisée `3 exp(-3t)`.

### Rotation uniforme

Pour

```text
e(s)=(cos(alpha s),sin(alpha s),0),       alpha>0,
```

la moyenne complexe sur toute boule centrée vaut

```text
m_S=exp(i alpha S) 3/(3-i alpha),
|m_S|²=9/(9+alpha²).
```

La variance exacte est `alpha²/(9+alpha²)`. Comme la distance à la moyenne
est au plus deux, l'oscillation moyenne vérifie

```text
MO_(B_R)(xi) >= alpha²/[2(9+alpha²)].                    (10)
```

Cette borne est indépendante de `R`. Donc le coût pondéré par
`1+|log R|` diverge pour tout `alpha>0`. Une rotation uniforme peut payer le
budget linéaire (9), mais échoue déjà au test log-BMO **centré**.

### Dérive logarithmique

Pour

```text
e(s)=(cos[beta log(1+s)],sin[beta log(1+s)],0),          (11)
```

avec deux profondeurs exponentielles indépendantes `T,T'`, on a

```text
|e(S+T)-e(S+T')|<=beta|T-T'|/(1+S),
E|T-T'|=1/3,
MO_(B_R)(xi)<=beta/[3(1+S)].                             (12)
```

Cette famille passe donc le taux nécessaire sur les boules centrées, tout en
n'ayant aucune limite d'axe. Mais

```text
Var(e;[0,T])=beta log(1+T)=o(T),                         (13)
```

si bien que (7) l'exclut lorsque (2), la borne `Phi<=M` et l'erreur
pondérée sublinéaire sont maintenues.

Le test produit ainsi une dichotomie exacte dans ces deux familles :

- la rotation persistante peut recharger le moment mais coûte une oscillation
  centrée d'ordre un;
- la dérive logarithmique a le bon taux centré mais ne recharge pas assez le
  moment.

## Échelle des quantités

Sous

```text
u_lambda(x,t)=lambda u(lambda x,lambda²t),
W_lambda(x,t)=lambda²W(lambda x,lambda²t),
```

`Phi`, `xi`, `e`, `s`, `L`, `M`, `kappa`, `de/ds`, la variation par unité de
profondeur et le seuil (9) sont sans dimension. La masse de bloc est critique :

```text
integral_shell |W|^(3/2) dx
=4pi integral_block <Phi^(3/2)> ds.                     (14)
```

La norme énergétique `L²_x` reste supercritique par rapport à cette porte et
ne fournit ni (2), ni `Phi<=M`, ni (8).

## Passe contradictoire

1. La variation totale n'est pas une mesure canonique d'échappement : de
   petites boucles rapides autour d'un axe fixe peuvent avoir une grande
   variation tout en restant dans un cône fixe. Le résultat utilise la
   variation seulement comme budget nécessaire; il n'en déduit aucune
   diffusion angulaire macroscopique.
2. L'axe n'est pas unique si `Phi` est petit, nul ou réparti entre plusieurs
   cœurs. La quantité pertinente est l'erreur pondérée (3); aucune sélection
   canonique de `e(s)` n'est construite.
3. (10)–(12) portent uniquement sur les boules centrées. La semi-norme globale
   `bmo_phi` teste tous les centres; réussir (12) est donc nécessaire mais pas
   suffisant.
4. Une vitesse angulaire moyenne non nulle ne force pas une rotation uniforme.
   Des sauts rares, un axe de centre mobile ou une amplitude angulairement
   intermittente restent hors du test.
5. La borne faible-`L^(3/2)` globale n'implique toujours ni la borne de tranche
   `Phi<=M`, ni la minoration (2).
6. Aucun champ `Omega` réalisant les familles d'axes avec toutes les
   contraintes solénoïdales n'est construit; (7) est une obstruction
   conditionnelle.
7. Aucune pression n'intervient dans `div W=0`. Un profil franchissant cette
   porte devrait encore satisfaire Biot–Savart, la projection de Leray, la
   viscosité et l'évolution NS.

## Veille différentielle

La veille primaire n'a identifié aucun théorème publié qui déduise (2), (8)
ou une sélection d'axe mobile depuis les données Clay. Miller 2021 (`0089`)
autorise dans un critère de régularité une direction normale de plan variable
en espace-temps, mais suppose son gradient spatial borné et un contrôle
critique de la projection planaire de la vorticité; il ne fournit pas la
dérive logarithmique ici étudiée à partir de l'énergie.

Lei–Ren–Tian `arXiv:2501.08976v1` reste une prépublication v1. Son théorème
1.1 utilise un double cône fixe, mais son corollaire 1.6 tolère implicitement
un axe variable **en temps** sous une condition pairwise à temps égal portant
sur toute vorticité non nulle. Il ne couvre pas une direction spatiale radiale
qui parcourt un grand cercle à travers les échelles.

Enfin, aucune source ne donne le raccord
`log-BMO -> axe unitaire à variation sublinéaire`. Les moyennes dyadiques ont
des incréments `O(1/k)`, mais peuvent s'annuler et ne sont pas des axes. Le
champ directionnel radial de phase `log s` appartient localement à log-BMO,
parcourt l'équateur et échappe à tout cône fixe; ce falsificateur fonctionnel
n'est ni une vorticité solénoïdale ni une solution NS. S'il était couplé aux
hypothèses de tranche du lemme avec erreur nulle, sa variation logarithmique
serait précisément insuffisante dans (7).

## Verdict et écart avec Clay

Résultat positif borné : une non-dégénérescence critique à amplitude bornée
force tout axe rectifiant à accumuler une variation linéaire explicite, sauf
si l'erreur directionnelle elle-même a une densité positive. Cela étend le
budget à axe fixe du cycle 0022 et exclut les dérives `|e'|=O(1/s)`.

Résultat négatif : « laisser l'axe errer logarithmiquement » ne suffit pas à
réparer le profil critique. Une rotation assez persistante pour payer le
budget produit déjà une oscillation centrée d'ordre un dans la famille radiale
uniforme.

Le statut reste `COMPUTATION_ONLY`. Le verrou est resserré vers
`GAP-MULTICORE-ANGULAR-CASCADE` : phases multiples, intermittence angulaire,
axe ou centre mobile et harmoniques croissants pourraient casser la réduction
à un seul `e(s)`. Aucun passage vers une solution Clay, aucune pression et
aucun résidu d'évolution ne sont obtenus.

## Reproduction

```text
python -B experiments/navier-stokes/wandering-axis/wandering_axis_audit.py
```

Le script utilise seulement la bibliothèque standard et
`fractions.Fraction`. Il exécute 44 contrôles exacts, sans grille, flottant ni
aléa. Les résidus algébriques déclarés sont nuls. Empreinte SHA-256 :
`23802f4b094aaccd020ab6d5d0ae9b136cc8cf70738b069c712fa6cddc432ba4`.

Pour `M=2`, `kappa=1/2`, `L=3`, il certifie

```text
a_0=1/72,
v_*=1/216,
MO_centre(alpha=v_*)>=1/839810.
```

Ce dernier nombre est une borne inférieure analytique exacte, pas un résidu
PDE. Le résidu Navier–Stokes n'est pas défini parce qu'aucune vitesse candidate
n'est construite.
