# Cycle 0022 — obstruction solénoïdale aux profils log-rectifiés

Date de gel : 2026-08-14.

Statut : dérivation interne falsifiable, calcul exact et passes contradictoires
séparées par la même famille de modèles. Aucun résultat n'est une preuve de
régularité globale ou de blow-up.

## Décision du cycle

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| moment sphérique de degré un pour une direction rectifiée | 5 | 5 | 5 | 5 | **20** |
| perturbation harmonique avec contrôle de `partial_s xi` | 4 | 4 | 5 | 4 | 17 |
| construction numérique d'un jet angulairement intermittent | 5 | 2 | 4 | 4 | 15 |

Le verrou sélectionné est `GAP-LOG-RECTIFIED-PROFILE`. Le lemme actif teste
si un profil de vorticité critique peut conserver une masse par coquille tout
en rectifiant sa direction vers un vecteur fixe. L'expérience décisive suit
exactement le budget du premier harmonique sphérique et construit les deux
échappatoires qui empêchent de supprimer silencieusement ses hypothèses.

## Équation et type de solution

Le problème Clay de référence reste Navier–Stokes incompressible, visqueux,
non forcé, sur `R³`, sans frontière :

```text
partial_t u+(u dot nabla)u=-nabla p+nu Delta u,
div u=0,                 omega_vec=curl u,                 nu>0.
```

Les données Clay sont lisses, divergence-free et d'énergie finie. Le présent
cycle ne construit ni donnée initiale, ni trajectoire, ni solution faible ou
forte. Il examine une vorticité spatiale candidate dans une boule ponctuée à
un temps de blow-up hypothétique. La seule équation utilisée est la condition
cinématique nécessaire

```text
div omega_vec=0.
```

Cette condition précède Biot–Savart, la pression de Leray, la viscosité et le
résidu d'évolution. Son échec exclut le profil; son succès ne suffirait pas à
le raccorder au problème Clay.

## Coordonnées critiques et correction de signe

Fixons `R_*>0` et écrivons

```text
r=|x|,       theta=x/r,       s=log(R_*/r),
W(x)=r^-2 Omega(s,theta),
Omega=Omega_r theta+Omega_T.
```

La formule exacte, sur la boule ponctuée, est

```text
div W=r^-3[div_(S²) Omega_T-partial_s Omega_r].           (1)
```

Le signe moins vient de `partial_r s=-1/r`. La formule provisoire avec un
signe plus consignée à la fin du cycle 0021 était donc fausse. Deux contrôles
fixent le signe :

- `Omega=e` représente `W=e/r²` et donne `div W=-2(e dot theta)r^-3`;
- `Omega=r²e=R_*² exp(-2s)e` représente le champ constant `W=e`; les deux
  termes de (1) valent `-2r²(e dot theta)` et s'annulent.

La condition solénoïdale devient

```text
partial_s Omega_r=div_(S²) Omega_T.                       (2)
```

La moyenne de `Omega_r` est donc constante en `s`. Pour qu'un tel champ soit
un curl distributionnel à travers l'origine, cette constante doit en outre
être nulle. Le lemme ci-dessous n'a pas besoin de cette seconde condition :
il exclut déjà le profil dans le domaine ponctué.

## Lemme actif : obstruction du moment de degré un

Notons

```text
<f>=(1/4pi) integral_(S²) f(theta) dS(theta).
```

Soient `s_0` réel, `L>0`, `M>0` et `kappa>0`. Supposons que
`Omega` soit assez régulière pour (2), par exemple
`W^(1,1)_loc((s_0,infinity) times S²)`, et posons

```text
Phi=|Omega|,          xi=Omega/Phi sur {Phi>0}.
```

Supposons :

1. `0<=Phi<=M` presque partout;
2. la masse critique par bloc logarithmique ne dégénère pas :

   ```text
   integral_S^(S+L) <Phi^(3/2)> ds >= kappa              (3)
   ```

   pour tout `S>=s_0`;
3. il existe un vecteur unitaire fixe `e` tel que la rectification pondérée
   vérifie

   ```text
   integral_S^(S+L) <Phi |xi-e|> ds -> 0                 (4)
   ```

   lorsque `S->infinity`;
4. `W=r^-2 Omega` est divergence-free dans la boule ponctuée.

Alors ces quatre hypothèses sont incompatibles : aucun profil de profondeur
logarithmique infinie ne les satisfait.

En particulier, (4) découle de la rectification uniforme

```text
ess sup_(theta:Phi>0)|xi(s,theta)-e|=O(1/s),              (5)
```

car `<Phi> <= M`. Le lemme ne suppose aucune borne sur `partial_s xi` et
reste donc valable pour une erreur `O(1/s)` oscillant arbitrairement vite en
`s`.

### Preuve avec constantes

Posons

```text
mu=e dot theta,        h=1-mu²=|nabla_(S²)mu|²,
J(s)=<mu Omega_r(s)>.
```

Puisque `<|mu|>=1/2`, on a

```text
|J(s)|<=M/2.                                             (6)
```

En testant (2) contre le premier harmonique `mu` et en intégrant par parties
sur la sphère,

```text
J'(s)
=-<Omega_T dot nabla_(S²)mu>
=-<Phi h>-<Phi (xi-e) dot nabla_(S²)mu>.                 (7)
```

Il reste à borner le premier terme par la masse critique. Pour
`q=<Phi>` et `a=q/M`, le principe de remplissage des plus petites valeurs de
`h` donne exactement

```text
<Phi h> >= M(a²-a³/3) >= (2q²)/(3M).                    (8)
```

La constante s'obtient en remplissant à hauteur `M` les deux calottes
`|mu|>=1-a`. Une preuve élémentaire soustrait ce minimiseur : à l'intérieur
des calottes, `Phi-M<=0` là où `h` est sous le seuil; à l'extérieur,
`Phi>=0` là où `h` est au-dessus du seuil.

Si `K=<Phi^(3/2)>`, alors `K<=sqrt(M)q`, d'où

```text
<Phi h> >= (2K²)/(3M²).                                  (9)
```

Cauchy–Schwarz et (3) donnent sur chaque bloc

```text
integral_S^(S+L)<Phi h> ds >= 2kappa²/(3M²L).            (10)
```

Comme `|nabla_(S²)mu|<=1`, (4) rend le module du terme
d'erreur intégré inférieur à `kappa²/(3M²L)` à partir d'un rang. Ainsi,

```text
J(S+L)-J(S) <= -kappa²/(3M²L).                           (11)
```

Après `N` blocs, la baisse forcée vaut
`N kappa²/(3M²L)`, alors que (6) limite toute variation de `J` à `M`.
Il est donc impossible de dépasser

```text
N <= 3M³L/kappa²                                         (12)
```

blocs après l'entrée dans le régime rectifié. C'est la contradiction.

Dans le cas uniforme `|xi-e|<=delta`, une condition quantitative suffisante
pour (11) est

```text
delta <= kappa²/(3M³L²).                                 (13)
```

Si `delta(s)<=C/s`, le régime (13) commence au plus tard à
`s=3CM³L²/kappa²`, puis (12) donne une profondeur restante finie explicite.

## Échelle des quantités

Sous le scaling Navier–Stokes

```text
u_lambda(x,t)=lambda u(lambda x,lambda²t),
W_lambda(x,t)=lambda² W(lambda x,lambda²t),
```

`Phi`, `xi`, `s` relatif à l'échelle externe remise à l'échelle, `M`, `L` et
`kappa` sont sans dimension. Plus précisément,

```text
integral_(R_*e^(-(S+L))<r<R_*e^(-S)) |W|^(3/2) dx
=4pi integral_S^(S+L)<Phi^(3/2)> ds.                    (14)
```

La prémisse (3) est donc une non-dégénérescence forte `L^(3/2)` par coquille
logarithmique, exactement critique. Une simple borne supérieure globale dans
`L^(3/2,infinity)` ne fournit pas (3).

## Corollaire pour les magnitudes récurrentes

Si `Phi` est non nulle, bornée et périodique en `s` de période `L`, alors

```text
kappa=integral_0^L <Phi^(3/2)> ds > 0
```

est indépendant du bloc. Le lemme exclut donc une magnitude scalaire
exactement homogène ou log-périodique non nulle accompagnée d'une direction
qui converge uniformément vers un vecteur fixe, même si le champ vectoriel
complet n'est jamais récurrent. Ce corollaire touche précisément l'ansatz
rectifié envisagé après le cycle 0021; il ne déduit pas la rectification de
la condition `bmo_(1/|log r|)`.

## Test adverse et échappatoires

Deux hypothèses ne peuvent pas être effacées par la preuve.

### Intermittence angulaire sans borne uniforme

Sur deux calottes de mesure normalisée `a_n=2^(-3n)`, posons formellement

```text
Phi_n=2^(2n).
```

Alors

```text
<Phi_n^(3/2)>=1,
<Phi_n>=2^-n,
<Phi_n h>=2^(-4n)-(1/3)2^(-7n) -> 0.                   (15)
```

La masse critique reste fixe tandis que la coercivité du moment disparaît.
Cette suite n'est pas annoncée solénoïdale : elle réfute seulement toute
version de (9) qui supprimerait `Phi<=M`. Elle identifie l'intermittence
angulaire polaire comme l'échappatoire suivante à tester.

### Masse critique dégénérée

Le champ constant `W=e` est exactement divergence-free et de direction
constante. Dans les coordonnées critiques, `Omega=r²e`; aux rayons
`r_n=2^-n`, son amplitude vaut `4^-n` et sa densité critique par coquille
vaut `8^-n`. Il échappe au lemme uniquement parce que (3) s'effondre et ne
représente aucune singularité critique.

Une construction moins triviale atteint exactement le taux directionnel
visé. Avec `mu=e dot theta`, posons

```text
Omega=e^(-2s)[s² mu theta+(s²-s)nabla_(S²)mu],
W=(s²-s)e+s mu theta
 =s²[e-s^-1 nabla_(S²)mu].                              (16)
```

La décomposition harmonique de degré un donne

```text
div_(S²) Omega_T=partial_s Omega_r
```

exactement. Pour `s>=2`, la direction de `W` est à distance au plus
`2/(s-1)` de `e`, mais

```text
|Omega| asymp e^(-2s)s²,
|W| asymp s².                                            (17)
```

Le facteur `r^-2` est donc annulé et la masse (3) dégénère
exponentiellement. Pour `R_*=1`, une vitesse explicite est

```text
u=(s²/2)e cross x,
div u=0,                         curl u=W.                (18)
```

Ce profil rectifié est cinématiquement réalisable et localement énergétique,
mais il n'est pas un profil stationnaire de Navier–Stokes. Le certificat
exact donne

```text
Delta W=r^-2[3e-(1+6s)mu theta],
(u dot nabla)W-(W dot nabla)u=s³ mu e cross theta.       (19)
```

Les deux résidus sont dans des directions orthogonales; aucune pression ne
peut réparer l'équation de vorticité stationnaire. Une coupure scalaire à
`r~epsilon` a en outre un commutateur visqueux d'ordre
`epsilon^-2 s_epsilon²`, donc une norme `L^(3/2)` de coquille d'ordre
`s_epsilon²`, non uniforme. Ce sont des identités et des lois d'échelle, pas
une minoration universelle après toute correction solénoïdale.

### Attaques de portée

1. La borne faible-`L^(3/2)` est un majorant, pas une minoration par coquille.
2. `bmo_(1/|log r|)` contrôle une oscillation moyenne; il ne choisit pas un
   unique vecteur `e` et n'implique pas (4).
3. Une direction rectifiée seulement sur un cœur actif ou hors de ses zéros
   ne donne (4) qu'après un contrôle pondéré du complément.
4. Des amplitudes croissant dans des calottes qui se resserrent peuvent
   conserver la masse critique et annuler le moment transverse.
5. Le test utilise le centre fixe de la représentation; un centre mobile
   exige des termes de transport supplémentaires.
6. La régularité `W^(1,1)_loc` en `(s,theta)` est une hypothèse de profil;
   aucun passage depuis une suite de solutions NS n'est obtenu.
7. L'absence de profil dans cette classe ne contrôle ni les scénarios Type II,
   ni les profils multi-échelles, ni les solutions anciennes générales.

## Veille différentielle

Au 2026-08-14, la source primaire `arXiv:2607.08866` reste en v2 du 13
juillet 2026, sans publication ni erratum indiqué. `arXiv:2510.20757` reste
en v3 du 11 août 2026. La recherche primaire ciblée n'a pas identifié de
théorème qui produise (3)–(5) depuis les données Clay ou qui invalide
l'identité de moment (7).

Elle resserre néanmoins le transfert dynamique. Lei–Ren–Tian,
`arXiv:2501.08976v1`, affirme pour une solution faible adaptée locale que le
confinement de toute forte vorticité dans un double cône fixe implique la
régularité intérieure. Une rectification **uniforme en espace-temps** de tous
les grands niveaux vers `+/-e` satisfait élémentairement ce cône. Cette porte
est `SOURCE_VERIFIED`, mais reste une prépublication v1 dont la preuve n'est
pas reproduite ici. Giga–Miura 2011 fournit un résultat publié apparenté sous
borne Type I et continuité uniforme de direction.

Quatre sources publiées manquantes ont été ajoutées au registre : Chae 2015
et Chae–Wolf 2017 pour les exclusions asymptotiquement DSS, Giga–Miura 2011
pour la géométrie Type I, et Ożański–Palasek 2023 pour la rigidité
axisymétrique sous faible-`L³`. Aucune ne ferme une dérive apériodique,
non axisymétrique et Type II. Le rapport de veille séparé consigne la frontière
exacte avec les solutions anciennes et scénarios auto-similaires.

## Verdict et écart avec Clay

Résultat positif : sous amplitude angulaire uniformément bornée, masse
critique non dégénérée par blocs et rectification pondérée vers un vecteur
fixe, la condition `div W=0` mène à une contradiction quantitative après un
nombre fini de blocs logarithmiques. Le signe, le moment, la constante de
calottes et le budget sont exacts.

Résultat négatif : une construction du type `xi=e+O(1/|log r|)` ne peut pas
réparer un facteur de magnitude homogène ou log-périodique non nul et borné.
Toute échappatoire doit perdre la masse critique par coquille, concentrer une
amplitude non uniformément bornée dans des angles polaires, perdre la
rectification vers un `e` fixe, ou abandonner la représentation ponctuelle.

Ce résultat reste cinématique et `COMPUTATION_ONLY`. Il ne produit aucune
borne a priori sur une solution de Navier–Stokes, aucune pression, aucun
résidu visqueux, aucune compacité et aucune conclusion Clay. Le verrou devient
`GAP-WANDERING-AXIS-PROFILE` : déterminer si une cascade angulaire ou un axe
`e=e(s)` peut échapper à tout double cône fixe tout en restant solénoïdal,
ponctuellement localisé, faible-`L^(3/2)` uniforme et compatible avec
Biot–Savart sans recréer une oscillation directionnelle d'ordre un.

## Reproduction

```text
python -B experiments/navier-stokes/log-rectified-profile/log_rectified_profile_audit.py
```

Le script utilise uniquement la bibliothèque standard et
`fractions.Fraction`. Il exécute 62 contrôles exacts, sans grille PDE, sans
flottant et sans aléa. Les résidus certifiés des identités de signe, de
calottes, de budget, du raccord div–curl et du calcul polynomial sont nuls.
Empreinte SHA-256 :
`e5c24374ab40c7d52d12ddbd8c96e7aedee51a3c6b35154b90142c6c12781efe`.

Le calcul ne simule ni Navier–Stokes, ni pression, ni coupure. Pour la classe
non dégénérée, le résidu d'évolution n'est pas défini parce que le candidat
est déjà exclu à la porte solénoïdale. Pour l'échappatoire dégénérée (16), les
deux termes de (19) sont certifiés mais aucun intégrateur temporel ni raccord
Clay n'est construit.
