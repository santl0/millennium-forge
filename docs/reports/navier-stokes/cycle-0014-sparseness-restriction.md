# Cycle 0014 — restriction volumique 3D vers sparseness linéaire

Date : 2026-08-14. Lemme actif : `SPARSENESS-RESTRICTION-1`.

## Décision adaptative

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total | Décision |
|---|---:|---:|---:|---:|---:|---|
| prouver ou réfuter la restriction sharp 3D `delta` vers 1D `delta^(1/3)` | 3 | 5 | 5 | 5 | **18/20** | sélectionnée |
| auditer l'inversion logarithmique des réarrangées, équations (47)–(49) | 4 | 4 | 5 | 5 | **18/20** | cycle suivant possible |
| auditer la queue dyadique du commutateur, théorème 4.1 | 5 | 2 | 4 | 5 | 16/20 | différée |

Le premier candidat gagne le départage parce qu'il est indépendant de toute
estimation PDE et décide exactement une arête utilisée dans l'étape finale de
la prépublication récente `arXiv:2607.08866v2`.

## Équation et portée

Le manuscrit ciblé considère Navier–Stokes incompressible 3D non forcé sur
`R³`, viscosité `nu>0`, donnée `u_0∈L∞(R³)` et solution mild unique,
spatialement analytique avant un premier temps singulier possible `T*` :

```text
partial_t u + (u·nabla)u - nu Delta u + nabla p = 0,
div u = 0.
```

Le lemme audité est toutefois un résultat autonome de théorie de la mesure. Il
ne suppose ni divergence nulle, ni pression, ni équation d'évolution. Cette
séparation interdit de promouvoir sa validation en validation du théorème 7.4.

## Énoncé exact audité

Soient `x_0∈R³`, `r>0`, `0<delta<1` et un ensemble borélien `S` — en
particulier un ouvert, comme dans le manuscrit. Posons

```text
D_3(S;x_0,r)=|S intersect B_r(x_0)|/|B_r|,
L(S;x_0,r,nu)=|{t∈(-r,r):x_0+t nu∈S}|/(2r).
```

Le maillon est

```text
D_3(S;x_0,r) <= delta
  => il existe nu∈S² tel que L(S;x_0,r,nu) <= delta^(1/3).    (G)
```

Le point et le rayon sont identiques des deux côtés. Le manuscrit l'emploie à
`delta=3/4`, donc au seuil linéaire `q=(3/4)^(1/3)`.

## Preuve à constante suivie

Par translation et dilatation, il suffit de traiter `x_0=0`, `r=1`. Pour une
direction orientée `nu∈S²`, définissons

```text
A_nu={t∈(-1,1):t nu∈S},    m(nu)=|A_nu|.
```

La formule polaire symétrisée est

```text
|S intersect B_1|
  =(1/2) integral_(S²) integral_(-1)^1 1_S(t nu)|t|² dt d sigma(nu).  (1)
```

Le facteur `1/2` corrige la double représentation `(t,nu)=(-t,-nu)`.

Pour tout ensemble mesurable `A⊂(-1,1)` de longueur `m`, la fonction paire
croissante `t²` est minimisée par l'intervalle centré de même longueur :

```text
integral_A t² dt >= integral_(-m/2)^(m/2) t² dt = m³/12.      (2)
```

Une preuve élémentaire de (2) compare `A` à `[-m/2,m/2]` : les parties
échangées ont même mesure, `t²` est au moins `(m/2)²` à l'extérieur et au plus
ce seuil à l'intérieur.

Supposons par contradiction que chaque direction ait une densité linéaire
strictement supérieure à `q=delta^(1/3)`, donc `m(nu)>2q`. Les équations
(1)–(2) donnent

```text
|S intersect B_1|
  > (1/2)|S²| (2q)³/12
  = (4pi/3)q³
  = delta |B_1|,
```

contradiction. Le même calcul avec des inégalités larges traite les cas
limites. L'énoncé (G) est donc valide avec constante `1`.

## Sharpness et dimension générale

La boule centrale

```text
S=B_(r delta^(1/3))(x_0)
```

a densité volumique `delta` et densité linéaire `delta^(1/3)` dans **toutes**
les directions. Ni la constante ni l'exposant ne peuvent être améliorés sans
hypothèse géométrique supplémentaire.

En dimension `d`, le poids polaire devient `|t|^(d-1)` et

```text
min_(|A|=m) integral_A |t|^(d-1) dt
  = 2(m/2)^d/d.
```

Le même argument donne exactement le seuil `delta^(1/d)`.

## Application d'un majorant global de superniveau

Supposons qu'un superniveau `V⊂R³` vérifie `|V|≤B`. Avec
`v_3=|B_1|=4pi/3`, fixons

```text
r_B=(B/(delta v_3))^(1/3).                              (3)
```

Alors, pour **tout** `x_0`,

```text
|V intersect B_(r_B)(x_0)| <= |V| <= B
  = delta |B_(r_B)|.
```

L'énoncé (G) fournit donc une direction dépendant de `x_0`, au même rayon
`r_B`, avec densité linéaire au plus `delta^(1/3)`.

Le sens des quantificateurs est important : par le seul majorant global, les
rayons garantis satisfont

```text
r³ >= B/(delta v_3).
```

Une échelle arbitrairement plus petite n'est pas garantie. L'application du
manuscrit reste cohérente si l'on **construit** le rayon minimal (3), puis si
l'on montre que ce rayon construit possède la borne supérieure nécessaire au
rayon d'analyticité.

À partir de son équation (55), avec

```text
A=||u(s)||_infinity,
B(A)=C/[lambda³ A³ log³(e+lambda A)],
```

le choix (3) donne explicitement

```text
r_B = [C/(delta v_3)]^(1/3)
      /[lambda A log(e+lambda A)].                       (4)
```

Ainsi `r_B=O(A^-1 log^-1 A)`. Cette arête géométrique est compatible avec la
comparaison `r_B≤rho_s` lorsque le rayon d'analyticité satisfait
`rho_s=c nu/A` et que `A` est suffisamment grand. Cette conclusion dépend
toujours de la validité antérieure du majorant (55) et de la constante
d'analyticité.

Pour `delta=3/4`, la constante se simplifie exactement :

```text
delta v_3=(3/4)(4pi/3)=pi,
r_s^sharp=(|V_s|/pi)^(1/3) <= R_s=(B(A)/pi)^(1/3),
R_s=(C/pi)^(1/3)/[lambda A log(e+lambda A)].             (5)
```

Le premier rayon emploie le volume réel; le second est le rayon sûr calculable
depuis le majorant. Si `|V_s|=0`, tout rayon positif sous le rayon analytique
convient et on utilise `R_s`, pas le rayon dégénéré zéro. Avec
`rho_s=nu/(c_3 A)`, la condition suffisante suivie avec constantes est

```text
log(e+lambda A) >= [c_3/(nu lambda)] (C/pi)^(1/3).        (6)
```

Cette comparaison est conditionnelle à l'uniformité de `C,c_3,nu,lambda` et
au régime d'amplitude où le majorant est établi. Dans une formulation
dimensionnée, l'argument du logarithme doit en outre être normalisé par une
vitesse de référence; l'écriture reprend ici la nondimensionnalisation
implicite de la prépublication.

## Échelle Navier–Stokes

Sous

```text
u_kappa(x,t)=kappa u(kappa x,kappa²t),
```

le pic `A` porte le facteur `kappa`, le volume d'un superniveau relatif porte
`kappa^-3`, et le rayon (3) porte `kappa^-1`. Le rayon d'analyticité porte lui
aussi `kappa^-1`. Les densités `D_3`, `L` et le rapport `r_B/rho_s` sont
invariants : le maillon confirmé est critique, sans gain d'échelle caché.

## Certificat reproductible

Commande :

```text
python -B experiments/navier-stokes/sparseness-restriction/sparseness_restriction_audit.py
```

Le script utilise uniquement `fractions.Fraction`. Il vérifie :

- le coefficient `1/12` du moment centré ;
- la normalisation polaire et l'annulation de `pi` dans le rapport ;
- la sharpness des boules centrales ;
- le slack exact des coquilles concentriques ;
- plusieurs profils angulaires anisotropes finis ;
- la loi `delta^(1/d)` pour `d=1,...,6` ;
- le choix de rayon depuis un majorant global ;
- un encadrement rationnel strict de `(3/4)^(1/3)`.

Les profils finis servent de tests adverses des constantes. La preuve
universelle reste l'argument analytique (1)–(2), non une extrapolation du
calcul.

Empreinte SHA-256 du script exécuté :
`efe3ccaa41bd97988a7bd7c58c728af35f8dc6665d53d3f9df7052a1f34fe19b`.

## Passe contradictoire et limites

Les attaques obligatoires sont :

1. ne pas remplacer une **tranche par une droite** par une projection ;
2. conserver le facteur `1/2` de la paramétrisation polaire signée ;
3. fixer `x_0` avant de choisir la direction, celle-ci pouvant dépendre du
   point ;
4. distinguer la borne inférieure sur les rayons garantis par le volume de la
   borne supérieure obtenue ensuite en fonction de l'amplitude ;
5. tester la boule centrale, qui sature exactement l'exposant `1/3` ;
6. ne pas attribuer la réduction au seul papier de 2013, qui porte le critère
   1D et la mesure harmonique : la version `rho≤r` est dans FGL 2017 et la
   formulation même-rayon dans la chaîne Grujić–Xu 2019–2024.

Le résultat ne valide ni le commutateur logarithmique, ni l'interpolation de
De Giorgi, ni le transfert vorticité–vitesse, ni l'inversion des réarrangées,
ni le choix du temps analytique, ni le maximum harmonique du théorème 7.4.

## Revues contradictoires séparées

Trois dérivations Codex séparées, toutes de la même famille de modèle et donc
non indépendantes au sens externe, convergent sur le lemme sharp. Elles ont
recalculé la constante par deux paramétrisations polaires et attaqué la
mesurabilité, le double comptage, les orientations, les cas d'égalité et le
sens du rayon :

- la passe d'analyse en dimension `d` confirme le seuil `delta^(1/d)`, la
  constante `1`, le rayon (5) et l'extrémiseur central;
- la passe contre-modèle paire explicitement les orientations et réfute la
  lecture « tout rayon inférieur convient » par une boule centrale de masse
  `pi/8`, sparse à `r=1/2` mais de densité `1` à `r=1/4`;
- la passe bibliographique confirme la v2 du 13 juillet 2026 et corrige
  l'attribution historique : Grujić 2013 porte le critère 1D et l'endgame
  harmonique, tandis que la réduction volumique apparaît dans la chaîne
  Farhat–Grujić–Leitmeyer 2016–2017 puis Grujić–Xu 2019–2024.

Les rapports sont conservés dans `docs/reports/navier-stokes/reviews/`. Leur
accord justifie `adversarial_pass`, jamais `independently_reviewed`.

## Décision

Le maillon géométrique « volume 3D → tranche 1D au même rayon » est
**confirmé**, sharp et compatible avec le scaling. Il sort de la liste des
trous de la chaîne Grujić v2, tout en restant `COMPUTATION_ONLY` dans le
laboratoire parce que la dérivation est nouvelle et produite par IA.

Le prochain audit doit remonter d'une arête : soit rendre quantitative
l'inversion (47)–(49), écrite avec des équivalences asymptotiques, soit attaquer
la queue dyadique (16)–(22) du commutateur. Le choix sera fait après scoring des
passes indépendantes du présent cycle.
