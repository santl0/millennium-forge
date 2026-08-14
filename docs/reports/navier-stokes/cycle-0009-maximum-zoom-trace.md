# Cycle 0009 — horloges du zoom maximum et concentration critique

Date : 2026-08-14.

## Décision automatisée

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| auditer les deux horloges, la commutation au temps-record et la masse critique | 4 | 5 | 5 | 5 | **19** |
| poser une équi-intégrabilité locale `L³` comme critère | 3 | 5 | 5 | 4 | 17 |
| chercher une nouvelle normalisation hybride ESS–KNSS | 4 | 2 | 3 | 5 | 14 |

Action sélectionnée : première ligne. Le lemme actif est borné au zoom par
temps records de la proposition 6.1 de KNSS. L'expérience décisive vérifie les
exposants, constantes et portes logiques sans discrétiser la PDE.

## Équation et notion de solution

On considère une solution classique, donc mild, de

```text
partial_t u - Delta u + (u dot nabla)u + nabla p = 0,
div u = 0
```

sur `R³ x [0,T)`, viscosité `nu=1`, force nulle, sans frontière, avec `T<infinity`
hypothétiquement maximal et `||u(t)||_infinity` non bornée quand `t->T-`.
Ce cycle ne porte ni sur Euler, ni sur le cas forcé, ni sur une solution faible
arbitraire.

## Lemme retenu et correction des horloges

Pour des temps records `t_k->T`, centres `x_k` et amplitudes
`M_k=|u(x_k,t_k)|->infinity`, KNSS utilisent

```text
v_k(y,s)=M_k^-1 u(x_k+y/M_k,t_k+s/M_k²).
```

Le domaine temporel est `(A_k,B_k)`, avec

```text
A_k=-M_k²t_k -> -infinity,
B_k=M_k²(T-t_k) >= c > 0.
```

La construction assure, pour `s<=0`,

```text
|v_k(y,s)|<=gamma_k,  gamma_k->1,
|v_k(0,0)|=1.
```

La correction décisive est

```text
s=0 <-> temps physique t_k,
s=B_k <-> temps physique T.
```

Ainsi, toute commutation avec `s->0-` concerne le temps-record, pas la trace
physique terminale.

## Commutation au temps-record

La proposition 4.1 de KNSS, redémarrée sur une bande normalisée passée fixe,
donne pour chaque ordre utile des bornes indépendantes de `k` sur
`nabla^m v_k` et `partial_s v_k` jusqu'à `s=0`. Après extraction,
`v_k->v` dans `C^m_local` jusqu'à ce temps. Pour tout test compact `phi`,

```text
|<v_k(s)-v_k(0),phi>| <= L |s| ||phi||_1,
```

d'où

```text
lim_(s->0-) lim_(k->infinity) <v_k(s),phi>
 = lim_(k->infinity) lim_(s->0-) <v_k(s),phi>
 = <v(0),phi>.
```

La convergence `C^0_local` et `|v_k(0,0)|=1` donnent `|v(0,0)|=1`. La valeur
commune au temps-record est donc non nulle. Une trace ESS nulle ne peut pas
être injectée à cet endroit par un choix favorable de l'ordre des limites.

## Le trou terminal exact

Pour placer `T` à l'origine, il faut définir

```text
w_k(y,tau)=v_k(y,tau+B_k).
```

Alors `tau=0` correspond à `T` et le témoin ponctuel est à `tau=-B_k`.

- Si `B_k->infinity`, le témoin non nul fuit vers le passé.
- Si `B_k->beta<infinity`, le témoin reste à `-beta`, mais la borne issue des
  temps records ne contrôle que `tau<=-B_k`, pas `(-B_k,0)`.

Le maillon manquant est donc une compacité et un contrôle de pression sur une
bande terminale mobile. Le cycle ne produit pas ce contrôle.

## Tests fixes, tests mobiles et échelle

Pour un test `phi` dans les variables zoomées,

```text
<v_k(s),phi>
 = M_k² integral u(x,t_k+s/M_k²) phi(M_k(x-x_k)) dx.
```

Le test physique `Phi_k=M_k²phi(M_k(x-x_k))` se concentre, se translate et
vérifie exactement `||Phi_k||_(3/2)=||phi||_(3/2)`. Une trace dans `D'` contre
chaque test physique fixe ne contrôle pas cette famille critique mobile.

La masse locale obéit à

```text
integral_(B_R)|v_k|^q
 = M_k^(3-q) integral_(B_(R/M_k)(x_k))|u|^q.
```

Le seuil invariant est `q=3`; `L²` est supercritique dans cette direction de
zoom.

## Concentration quantitative et borne de nouveauté

Si le lissage donne `||nabla v_k(0)||_infinity<=G`, alors
`|v_k(y,0)|>=1/2` pour `|y|<=1/(2G)`. Par l'identité critique précédente,

```text
integral_(B_(1/(2GM_k))(x_k)) |u(x,t_k)|³ dx
 >= pi/(48G³).
```

Le coefficient `1/48` est calculé exactement et `pi` reste symbolique.
Ce corollaire est une dérivation du laboratoire, non un `PAPER_PROOF` et non un
nouveau critère de régularité. En effet, l'équi-intégrabilité uniforme complète
de `|u|³` implique la condition à seuil fixe (23) de Constantin 2023, plus
faible; son théorème 2 donne déjà une borne explicite de `Hdot1` et le
prolongement. Le résultat utile ici est la localisation quantitative de la
concentration imposée par le zoom KNSS.

## Passe adverse

Premier contre-profil, exact sur `R³ x (-infinity,0]` :

```text
u_k=e^(k²s)e_1,
p_k=-k²e^(k²s)x_1.
```

La divergence, la convection, le Laplacien, le résidu de quantité de mouvement
et le résidu de Poisson sont nuls. Les limites itérées au bord `s=0` ne
commutent pas. Mais le champ n'est pas mild au sens de Leray/Oseen, sa pression
affine n'est pas dans la jauge Riesz/BMO et
`||partial_s u_k(0)||_infinity=k²`.

Second contre-profil, exact et mild sur `T³` :

```text
w_k=e^(-k²s) cos(kx_2)e_1,  s<=0.
```

Il a un résidu nul et une tranche oscillante au bord, mais croît comme
`e^(k²|s|)` vers le passé. Il perd toute borne uniforme sur une bande passée
fixe et appartient à un domaine différent de `R³`.

Ces familles montrent que résidu PDE nul, adaptation locale ou mildness prise
isolément ne remplacent pas le paquet complet de bornes KNSS. Elles ne
construisent aucune singularité Clay.

## Sources et statut

- KNSS, *Acta Mathematica* 203 (2009), DOI
  `10.1007/s11511-009-0039-6` : propositions 4.1 et 6.1, lemme 6.1.
- Seregin, *Communications in Mathematical Physics* 312 (2012), DOI
  `10.1007/s00220-011-1391-x` : comparaison avec le zoom centré en `T` sous
  contrôle `L³`.
- Constantin, *Journal of Mathematical Fluid Mechanics* 25 (2023), article
  36, DOI `10.1007/s00021-023-00779-7` : condition (23), théorème 2.
- Barker–Seregin, *Mathematische Annalen* 369 (2017), DOI
  `10.1007/s00208-016-1488-9`, arXiv `1508.05313v1` : comparaison au
  demi-espace dans `L^{3,q}`, `q<infinity`.

La veille 2025–2026 n'a identifié aucune source primaire fermant l'extrémité
mobile `B_k`. Le résultat right-sided de Cheskidov–Dai–Palasek reste hors de
la classe Leray–Hopf et ne fournit pas un blow-up Clay admissible.

## Résultat et pivot

Résultat négatif : l'arête « obtenir une trace ESS nulle par permutation au
temps zéro du zoom maximum » est réfutée; ce zéro est un temps-record, et la
valeur limite y est non nulle. Résultat positif borné : la concentration
`L³>=pi/(48G³)` sur l'échelle `M_k^-1` est vérifiée algébriquement, sans
revendication de nouveauté théorématique.

Les cycles 0007–0009 ont appliqué trois stratégies distinctes au même verrou :
matrice d'héritage, rigidité abstraite, puis audit des horloges et du
commutateur. L'axe hybride ESS–KNSS est suspendu. Le prochain axe actif est la
stabilité sous désingularisation de la donnée homogène de degré `-1` de
Hou–Wang–Yang vers une donnée lisse admissible Clay, avec suivi des constantes
en cutoff et confrontation à l'unicité faible–forte.

Statut : `CONTINUER` sur le programme global; `ABANDONNER` la permutation au
temps-record comme mécanisme de raccord.
