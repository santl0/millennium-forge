# Cycle 0060 — ancienne axisymétrique suitable uniformément faible-`L3`

Date de gel : 2026-08-15.

Statut : audit bibliographique primaire indépendant. Aucun changement de
`literature/navier-stokes/sources.json`; aucun commit.

## Verdict

Le résultat Ożański--Palasek (`NS-SRC-0088`) porte formellement sur une
**solution classique axisymétrique**, avec swirl autorisé, de Navier--Stokes
3D non forcé sur `R3`. Leur théorème 1.1 donne des bornes quantitatives de
toutes les dérivées sous une borne uniforme `L^(3,infinity)`. La trivialité
des anciennes solutions est annoncée comme conséquence dans le texte, mais
n'est pas un corollaire numéroté dans l'article publié ni dans arXiv v3.

Pris seul, ce théorème ne s'applique pas directement à une limite seulement
suitable. Le maillon manquant est toutefois déjà publié : Seregin 2020 prouve
la régularité locale d'une solution faible adaptée axisymétrique sous contrôle
local `L-infinity_t L^(3,infinity)_x`. En combinant les deux articles, on
obtient l'implication exacte

```text
ancienne suitable sur R3, pression axisymétrique,
axisymétrie exacte (swirl permis),
sup_(t<0)||u(t)||_(L^(3,infinity)(R3))<infinity
  --> régulière/classique partout             [Seregin 2020]
  --> u=0                                     [Ożański--Palasek 2023].
```

Cette chaîne corrige donc le diagnostic antérieur selon lequel la classicalité
serait encore un verrou pour cette sous-classe. Elle ne résout pas Clay : un
blow-up général ne donne ni axisymétrie exacte ni, sans hypothèse Type I
critique, la borne globale faible-`L3` de l'ancienne limite.

## 1. Équation et classes comparées

Toutes les affirmations positives ci-dessous concernent

```text
partial_t u-Delta u+(u dot nabla)u+nabla p=0,
div u=0                                                   (NS)
```

sur `R3`, sans frontière, sans force, avec viscosité normalisée à `1`.

Une solution ancienne est définie pour tout `t<0`. La classe cible du pipeline
Millennium Forge est une paire `(u,p)` qui, sur chaque cylindre compact, est
distributionnelle et suitable :

```text
u in L-infinity_t L2_x,loc intersect L2_t H1_x,loc,
p in L^(3/2)_loc,
```

avec l'inégalité locale d'énergie. La borne critique supplémentaire est

```text
A_*:=ess sup_(t<0)||u(t)||_(L^(3,infinity)(R3))<infinity. (60.1)
```

L'axisymétrie autour d'un axe fixe signifie, en coordonnées cylindriques,

```text
partial_theta u_r=partial_theta u_theta=partial_theta u_3=0. (60.2)
```

La composante de swirl `u_theta` n'est pas supposée nulle.

## 2. Ożański--Palasek 2023 : énoncé exact

### Identité et statut

- Wojciech S. Ożański et Stan Palasek, *Quantitative Control of Solutions
  to the Axisymmetric Navier-Stokes Equations in Terms of the Weak L3 Norm*,
  *Annals of PDE* 9, article 15 (2023).
- DOI primaire :
  [10.1007/s40818-023-00156-7](https://doi.org/10.1007/s40818-023-00156-7).
- Prépublication primaire :
  [arXiv:2210.10030v3](https://arxiv.org/abs/2210.10030v3), 12 juillet 2023.
- Catalogue : `NS-SRC-0088`.
- Statut : publié le 10 août 2023; preuve analytique papier, non reproduite
  ligne à ligne dans ce cycle.
- PDF arXiv v3 contrôlé, 42 pages :
  `SHA256 2D64D4FF35D9AB144F54320F0E80281FF95454749E08C05D03F9C7D23ED0594B`.

### Théorème 1.1

L'introduction parle de « strong solution », mais l'énoncé formel dit :

```text
u est une solution classique axisymétrique de (NS)
sur [0,T] x R3,
||u||_(L-infinity([0,T];L^(3,infinity)(R3)))<=A, A>>1.   (60.3)
```

Alors, pour tout entier `j>=0`, il existe une constante dans l'exposant,
dépendant de `j`, telle que

```text
||nabla^j u(t)||_infinity
 <=t^(-(1+j)/2) exp exp(A^(O_j(1))),    0<t<=T.          (60.4)
```

Les constantes sont indépendantes de `T`, des normes sous-critiques de la
donnée et de la position spatiale. Elles ne sont pas présentées comme
uniformes en `j`. Le résultat ne suppose pas l'absence de swirl : l'équation
de la quantité `Theta=r u_theta` et les énergies de
`Phi=omega_r/r`, `Gamma=omega_theta/r` sont au cœur de la preuve.

### Notion exacte de solution

Le théorème 1.1 exige une solution **classique** sur tout l'espace. L'article
ne redéfinit pas « classique » comme « suitable », « local energy » ou
« mild faible ». Sa section 5 utilise explicitement la régularité lisse du
champ, notamment la continuité de `u_theta` sur l'axe et la régularité de la
vorticité. Par conséquent l'implication

```text
suitable + (60.1) + axisymétrie --> appliquer directement (60.4)
```

n'est pas contenue dans cet article seul.

### Conséquence ancienne exacte

L'article affirme en prose, au §1.3, la non-existence de solutions anciennes
axisymétriques non triviales dans `L-infinity_t L^(3,infinity)_x`. Aucun
« corollaire ancien » numéroté ne figure dans le texte; les corollaires 1.2 et
1.3 concernent respectivement le taux de blow-up et une échelle de profil.

Pour une ancienne **classique**, la dérivation est immédiate et uniforme.
Fixons `t<0` et un temps `s<t`. Après translation de `[s,t]` vers `[0,t-s]`,
(60.4) avec `j=0` donne

```text
||u(t)||_infinity
 <=(t-s)^(-1/2) exp exp(A_*^(O(1))).                    (60.5)
```

Faire tendre `s` vers `-infinity` impose `u(t)=0`. Comme `t` est arbitraire,
`u=0`. Cette limite n'utilise ni absence de swirl, ni énergie globale `L2`,
ni décroissance forte à l'infini; elle utilise crucialement la même borne
`A_*` sur tout le passé.

## 3. Seregin 2020 : le raccord suitable vers classique

### Identité et statut

- Gregory Seregin, *Local Regularity of Axisymmetric Solutions to the
  Navier-Stokes Equations*, *Analysis and Mathematical Physics* 10, article
  46 (2020).
- DOI primaire :
  [10.1007/s13324-020-00392-1](https://doi.org/10.1007/s13324-020-00392-1).
- Prépublication primaire :
  [arXiv:2006.04140v1](https://arxiv.org/abs/2006.04140v1).
- Statut : publié le 10 septembre 2020; non enregistré comme entrée autonome
  dans `sources.json` au début de cet audit.
- PDF arXiv v1 contrôlé, 22 pages :
  `SHA256 EC569C89B3D60B3EB0B0B5FD690E3DD90254DBFAAD70F2365A701AC8299C1872`.

### Classe de solution

La définition 1.3 est celle d'une paire suitable `(v,q)` sur un cylindre :

```text
v in L_(2,infinity),    nabla v in L2,    q in L^(3/2),
(v,q) résout (NS) distributionnellement,
et satisfait l'inégalité locale d'énergie.               (60.6)
```

Dans la section axisymétrique, la paire est supposée axisymétrique :

```text
partial_phi v_r=partial_phi v_phi=partial_phi v_3
=partial_phi q=0.                                        (60.7)
```

Le swirl `v_phi` est conservé; la preuve étudie précisément
`sigma=r v_phi`.

### Exclusion Type I

Pour un point `z0`, Seregin emploie les quantités invariantes

```text
A(z0,r)=ess sup_(t0-r^2<t<t0) r^(-1) integral_(B_r)|v|^2,
E(z0,r)=r^(-1) integral_(Q_r)|nabla v|^2,
C(z0,r)=r^(-2) integral_(Q_r)|v|^3.                      (60.8)
```

Une singularité est Type I si

```text
g(z0):=min(limsup E,limsup A,limsup C)<infinity.          (60.9)
```

Le théorème 2.1 établit qu'un point singulier d'une paire suitable
axisymétrique doit être Type II. Il traite les solutions avec swirl.

### Le cas faible-`L3` est explicitement fermé au §3

Seregin considère ensuite

```text
v in L-infinity(-1,0;L^(3,infinity)(C)),                 (60.10)
```

où `C` est un cylindre spatial autour de l'axe. L'inégalité de Lorentz locale
donne, uniformément en `r`,

```text
r^(-1) integral_(C(x,r))|v(y,t)|^2 dy
 <=c||v(t)||_(L^(3,infinity)(C(x,r)))^2.                 (60.11)
```

Elle borne donc `A(z0,r)`. Le papier invoque ensuite son estimation critique
de Morrey antérieure (référence [16], lemme 1.8) pour obtenir une borne du
type (3.1) sur `A+D+E+C`. Le point ne peut alors être Type II; le théorème
2.1 impose sa régularité. Cette conclusion est écrite explicitement à la fin
du §3, et n'est pas une extrapolation à partir du seul résumé.

Une ancienne satisfying (60.1) vérifie (60.10) dans chaque cylindre compact.
Après translation en temps et le long de l'axe, le résultat régularise chaque
point axial intérieur. Les points singuliers d'une suitable axisymétrique sont
déjà confinés à l'axe dans la preuve. Tous les points de
`R3 x (-infinity,0)` sont donc réguliers, puis le bootstrap parabolique donne
une solution classique.

## 4. Pression et axe fixe

Le raccord exige une pression axisymétrique, car Seregin formule
l'axisymétrie pour la paire `(v,q)`. Dans le pipeline du laboratoire, la
pression globale est fixée par Riesz :

```text
p=R_i R_j(u_i u_j).                                      (60.12)
```

Les transformées de Riesz sont équivariantes sous les rotations. Si `u` est
axisymétrique autour de l'axe fixé, (60.12) donne donc un scalaire `p`
axisymétrique, modulo la jauge temporelle que la normalisation globale retire.
La suitability fournit séparément `p in L^(3/2)_loc`; une simple borne
globale Lorentz faible du tenseur ne remplacerait pas cette hypothèse locale.

Une axisymétrie dont l'axe dépend du temps ne satisfait pas (60.2) dans un
repère inertiel fixe et ne peut pas être injectée silencieusement dans cette
chaîne. Le cycle 0059 épingle au contraire un axe commun, ce qui est le bon
quantificateur.

## 5. Chaîne complète pour une limite suitable ancienne

Soit `(u,p)` sur `R3 x (-infinity,0)` telle que :

1. `(u,p)` est suitable sur tout cylindre compact;
2. `p` est la pression de Riesz normalisée;
3. `(u,p)` est exactement axisymétrique autour d'un axe spatial fixe, swirl
   permis;
4. (60.1) vaut avec une constante unique `A_*` sur tout le passé.

Alors :

```text
(1)+(3)+(4)
  --> régularité locale à tout point axial        [Seregin, §3 et Th. 2.1]
  --> régularité partout et bootstrap classique;

classicalité globale sur chaque [s,t] + (4)
  --> (60.5)                                      [Ożański--Palasek, Th. 1.1]
  --> u(t)=0 lorsque s->-infinity
  --> u identically 0.                            (60.13)
```

La pression de Riesz est alors nulle. Il n'est pas nécessaire d'obtenir une
mildness ancienne globale, une énergie globale finie, l'absence de swirl ou
la stationnarité.

## 6. Transfert au cycle 0059

Sous les hypothèses déjà séparées du pipeline,

```text
ess inf_J |beta_n| -> infinity
  --> mathcal R Z=0                               [lemme interne 0059]
  --> axisymétrie exacte de Z;

dérenormalisation standard + stabilité suitable + borne globale weak-L3
  --> ancienne suitable axisymétrique v;

capture/non-trivialité de v + (60.13)
  --> contradiction.                              (60.14)
```

La décroissance du résidu moyen de Haar et la stationnarité ne sont donc pas
nécessaires pour fermer **cette branche axisymétrique**. Les vraies dettes
restantes sont en amont : obtenir le régime de grande vitesse tangentielle,
conserver la borne globale faible-`L3`, la suitability, la pression de Riesz
et la non-trivialité sous passage à la limite.

Cette correction ne promeut pas le lemme de projection du cycle 0059 en
théorème de blow-up. Elle remplace seulement son endgame conditionnel par un
Liouville publié plus fort.

## 7. Veille différentielle 2024--2026

La recherche primaire, gelée au 2026-08-15, n'a pas identifié d'article
postérieur à Ożański--Palasek dont l'énoncé autonome soit exactement

```text
ancienne suitable + axisymétrie + L-infinity_t L^(3,infinity)_x
  --> trivialité.
```

Le résultat publié plus récent le plus proche est :

- Zhen Lei et Xiao Ren, *Quantitative partial regularity of the Navier-Stokes
  equations and applications*, *Advances in Mathematics* 445 (2024), 109654,
  DOI
  [10.1016/j.aim.2024.109654](https://doi.org/10.1016/j.aim.2024.109654),
  [arXiv:2210.01783v1](https://arxiv.org/abs/2210.01783v1).
  Leur théorème D régularise une solution locale suitable axisymétrique si,
  pour un `mu>0` universel,

  ```text
  limsup_(r->0) [integral_(Q_r)|nabla v|^2]
    /[r(log|log r|)^mu] < infinity.                       (60.15)
  ```

  Il améliore le critère Type I de Seregin et confirme la robustesse du
  maillon de régularité suitable. Il ne formule pas un Liouville ancien
  faible-`L3`; la trivialité utilise encore (60.5). PDF primaire contrôlé :
  `SHA256 7BB1A326176812F59B489BDE04D791B4A56DC3A8DF219EDF3B354D4AB05F800B`.

Les sources primaires récentes déjà cataloguées ne ferment pas un autre
maillon exact :

- Chen--Galdi--Poggi--Schikorra 2026 (`NS-SRC-0036`) traite des espaces de
  Lebesgue de Serrin, dont l'endpoint spatial **fort** `L3`, pas le Lorentz
  faible `L^(3,infinity)`;
- Pineau--Vicol 2026 (`NS-SRC-0051`) suppose des profils RSS/RDSS lisses et
  une borne Type I ponctuelle, avec paramètres de rotation restreints;
- Wang--Yang 2026 (`NS-SRC-0046`) traite des solutions axisymétriques
  stationnaires de type D;
- Taniuchi 2024 (`NS-SRC-0190`) part d'une solution mild faible-`L3` et ajoute
  des hypothèses de continuité/petitesse ou de comportement au passé.

Aucune de ces sources n'est requise pour (60.13), et aucune n'étend (60.13)
aux anciennes non axisymétriques.

## 8. Passe contradictoire

### Test 1 — supprimer la classicalité dans Ożański--Palasek

Échec : le théorème 1.1 dit explicitement « classical », et la preuve emploie
les équations lisses du swirl et de la vorticité. Le raccord correct passe par
Seregin; il ne faut pas réétiqueter une suitable en strong.

### Test 2 — interpréter le titre comme un théorème sans swirl

Échec : l'axisymétrie (60.2) conserve `u_theta`, et l'article contrôle
`Theta`, `Phi` et `Gamma`. Le Liouville ancien obtenu couvre le swirl.

### Test 3 — remplacer la borne uniforme passée par des bornes par fenêtre

Échec : si la constante devient `A(s,t)` dans (60.5), elle peut croître plus
vite que `(t-s)^(1/2)` et la limite `s->-infinity` ne donne rien. Un unique
`A_*` est indispensable.

### Test 4 — utiliser seulement une borne faible-`L3` locale dépendant du rayon

Échec pour la trivialité : elle peut suffire à une régularité point par point,
mais elle ne fournit pas la constante globale uniforme requise dans (60.5).

### Test 5 — pression arbitraire

Une pression non normalisée peut contenir une composante harmonique ou affine
et ne pas être manifestement axisymétrique. La suitable seule donne une
pression locale; le pipeline doit conserver sa pression de Riesz pour vérifier
sans ambiguïté (60.7) et exclure les solutions parasites à pression affine.

### Test 6 — conclure Clay depuis (60.13)

Échec : (60.13) ne concerne qu'une ancienne exactement axisymétrique avec
borne critique globale. Une singularité Clay générale peut rester
non axisymétrique, Type II ou perdre la borne globale lors de la sélection.

## 9. Corrections de registre recommandées

Sans modifier le catalogue dans ce cycle :

1. préciser dans `NS-SRC-0088` que le théorème 1.1 porte sur des solutions
   classiques; l'ancienne trivialité est une conséquence textuelle, non un
   corollaire numéroté;
2. ajouter Seregin 2020 comme source autonome du maillon
   `suitable axisymmetric L-infinity_t L^(3,infinity)_x -> regular`;
3. remplacer dans la carte la flèche manquante
   `ANCIENT-WEAK-L3-RIGIDITY-OR-MILDNESS`, lorsqu'une axisymétrie exacte est
   déjà obtenue, par la chaîne publiée Seregin puis Ożański--Palasek;
4. maintenir ouvert le verrou général non axisymétrique et le verrou amont
   qui doit produire l'axisymétrie depuis le scénario de blow-up.

## Conclusion auditée

Le résultat négatif initial « Ożański--Palasek ne s'applique pas directement à
une suitable » est exact mais incomplet. La conclusion scientifique correcte
est positive et conditionnelle :

```text
ancienne suitable axisymétrique à pression de Riesz
+ borne uniforme globale L^(3,infinity)
  --> classique                                      [Seregin 2020]
  --> triviale                                       [Ożański--Palasek 2023].
```

Pour le cycle 0059, cette rigidité publiée supprime le besoin de prouver la
stationnarité après collapse axisymétrique. Elle ne supprime ni l'hypothèse de
collapse, ni la capture, ni la stabilité suitable/pression/weak-`L3`.
