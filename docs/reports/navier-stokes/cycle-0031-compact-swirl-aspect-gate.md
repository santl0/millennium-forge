# Cycle 0031 — rapport d'aspect d'un swirl compact

Date de gel : 2026-08-14.

Statut : dérivation analytique interne pour une classe séparable explicite et
audit rationnel exact des exposants. Aucun calcul d'évolution, aucune preuve de
singularité et aucune certification par arithmétique d'intervalles.

## Décision adaptative

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| budget Lorentz anisotrope d'un swirl compact | 5 | 5 | 5 | 5 | **20** |
| no-go universel pour toute vitesse compacte | 5 | 2 | 5 | 5 | 17 |
| évolution pseudospectrale d'un profil torique | 4 | 2 | 4 | 4 | 14 |

Le verrou `GAP-COMPACT-VELOCITY-WEAK-CRITICAL-DIRECTION` est sélectionné.
Le lemme actif demande si un rapport d'aspect croissant peut rendre la
direction de `curl U` presque constante sur les calottes d'une vitesse compacte
sans perdre simultanément l'une des deux normes critiques faibles.

## Équation et type d'objet

Le cadre Clay de référence reste

```text
partial_t u+(u·nabla)u=-nabla p+nu Delta u,
div u=0,
nu>0,
f=0,
```

sur `R^3` ou `T^3`. Le présent cycle ne traite qu'une donnée initiale
`U in C_c^infinity(R^3)^3`, divergence-free, et sa vorticité
`W=curl U`. La donnée engendre classiquement une solution forte locale, mais
aucune assertion n'est faite sur son évolution au-delà de ce fait standard.

## Classe compacte séparée

En coordonnées cylindriques, fixons deux profils lisses `eta` et `chi` :

- `eta` est supporté dans `(-2,2)`, vaut un sur `(-1,1)` et possède un
  sous-intervalle de transition où `|eta'|>=c_eta>0` ;
- `chi` est supporté dans `(-2,2)`, vaut un sur `(-1,1)` et possède un
  sous-intervalle de transition où `|chi'|>=c_chi>0`.

Pour `V>0`, `R>0`, `0<a<=R/8` et `b>0`, posons

```text
psi(r,z)=V (R/r) eta((r-R)/a) chi(z/b),
U=psi e_theta.                                             (1)
```

Le support reste loin de l'axe. Ainsi `U` est lisse, compact et
divergence-free. Le facteur `R/r` n'est pas décoratif : il annule exactement
le terme de courbure dans la composante axiale du rotationnel. On obtient

```text
W_r=-V (R/r) eta((r-R)/a) chi'(z/b)/b,
W_theta=0,
W_z= V (R/r) eta'((r-R)/a) chi(z/b)/a.              (2)
```

La pression et la projection de Leray n'interviennent pas dans (2). Le champ
est une donnée admissible de l'énoncé entier, pas une solution stationnaire.

## Échelle critique et budget de dérivées

Sur une fraction fixe du tore, `|U|` est comparable à `V`; sur les deux
zones de transition de volume comparable à `Rab`, `|W_z|` est comparable à
`V/a` et `|W_r|` à `V/b`. Avec la quasi-norme

```text
||f||_(L^(p,infinity))^*=sup_(t>0) t |{|f|>t}|^(1/p),
```

les constantes ne dépendent que des deux profils et donnent

```text
c V^3Rab <= ||U||_(L^(3,infinity))^3 <= C V^3Rab,          (3)

||W||_(L^(3/2,infinity))^3
 >=c V^3 max(R^2b^2/a, R^2a^2/b).                         (4)
```

Les cubes des rapports critiques satisfont donc

```text
K_z^3/K_u^3 >=c Rb/a^2,
K_r^3/K_u^3 >=c Ra/b^2,                                   (5)
```

et, en particulier,

```text
K_W/K_U >=c (R^2/(ab))^(1/6).                              (6)
```

La forme la plus utile prend `m=min(a,b)/R`. Si `a<=b`, le premier
rapport de (5) est au moins `R/a=1/m`; le cas `b<=a` utilise le second.
Ainsi

```text
K_W^3/K_U^3 >=c/m,
K_U <=C K_W m^(1/3).                                      (6a)
```

Le coût du grand aspect est donc quantitatif même sans supposer à l'avance
que les deux endpoints restent non dégénérés.

Toutes les quantités de (3)--(6) sont invariantes sous le scaling
Navier–Stokes `U_lambda(x)=lambda U(lambda x)`, pour lequel
`(R,a,b,V)` devient `(R/lambda,a/lambda,b/lambda,lambda V)`.

## Lemme de non-amincissement critique

Supposons, le long d'une famille de profils (1),

```text
||U_n||_(L^(3,infinity)) >= kappa>0,
||W_n||_(L^(3/2,infinity)) <= K<infinity.                  (7)
```

Les deux bornes séparées de (4), combinées à la majoration de (3), imposent

```text
R_nb_n/a_n^2 <= H,
R_na_n/b_n^2 <= H,
H=C(K/kappa)^3.                                            (8)
```

Écrivons `x=a/R` et `y=b/R`. Les inégalités deviennent
`y<=Hx^2` et `x<=Hy^2`. En substituant l'une dans l'autre,

```text
x>=H^(-1),  y>=H^(-1).                                     (9)
```

Ainsi aucun des deux rapports d'aspect `R/a` et `R/b` ne peut diverger tant
que les deux gates critiques (7) restent non dégénérés. Cette conclusion
utilise les deux composantes de la vorticité : contrôler seulement la calotte
axiale ou seulement la transition radiale laisserait une anisotropie ouverte.

## Raccord à l'obstruction directionnelle

Dans le corridor radial où `eta=1` et sur un sous-intervalle où `chi'` garde
son signe, (2) donne exactement

```text
W=W_r e_r.
```

Une boule de rayon `w=c min(a,b)`, centrée à rayon majeur `R`, tient dans ce
corridor. Le lemme géométrique du cycle 0027 donne sur cette boule

```text
average_B |xi-(xi)_B| >= c w/R,  xi=W/|W|.                 (10)
```

Par (9), le membre droit est minoré par une constante dépendant seulement de
`K/kappa` et des profils. Si une famille entière se concentre, alors
`w_n->0`, et le facteur logarithmique de la norme `BMO_(1/|log r|)` donne

```text
|log w_n| average_(B_n)|xi-(xi)_(B_n)| -> infinity.        (11)
```

Il n'existe donc pas, dans la classe (1), de famille concentrante qui vérifie
à la fois un gate faible-`L^3` non petit, un gate faible-`L^(3/2)` borné et
une extension directionnelle log-BMO uniforme.

Plus précisément, si la semi-norme log-BMO est au plus `M`, (10) donne
`m_n<=CM/|log w_n|`. La forme (6a) implique alors, sous `K_(W,n)<=K`,

```text
K_(U,n)<=CK M^(1/3)|log w_n|^(-1/3)->0.                   (11a)
```

Le produit séparable retombe donc quantitativement dans la petite vitesse
critique; il ne se contente pas d'échouer qualitativement au BMO.

## Famille adverse à rapport d'aspect croissant

Le test le plus favorable au contournement de (10) prend

```text
R_n=2^(-n),
a_n=b_n=2^(-2n),
m_n=R_n/a_n=2^n.                                          (12)
```

Sous la normalisation `V_n^3R_na_nb_n=1`, le cube du gate vitesse vaut un,
mais chacun des deux cubes de vorticité vaut `m_n=2^n`. Si l'amplitude est
au contraire divisée afin de garder le proxy vorticité égal à un, alors

```text
K_(U,n)^3=2^(-n)->0.                                      (13)
```

Le seul minorant géométrique connu devient `c/m_n`; pondéré par
`|log_2 a_n|=2n`, il tend vers zéro. La famille neutralise donc réellement ce
minorant BMO, mais paie exactement la divergence prédite par (5). Elle est un
test adverse du lemme, pas une singularité candidate.

## Veille différentielle primaire

- `NS-SRC-0059` (Grujić, arXiv `2607.08866v2`) reste une prépublication
  conditionnelle : le faible-`L^(3/2)` et le log-BMO directionnel sont des
  hypothèses, pas des propriétés produites par un curl compact.
- `NS-SRC-0061` (Lei–Ren–Tian, arXiv `2501.08976v1`) reste une v1 sur les
  solutions faibles adaptées locales et un double cône projectif. Elle ne
  fournit ni endpoint Lorentz ni construction compacte.
- `NS-SRC-0128` (Chemin–Gallagher–Paicu) montre au contraire qu'une forte
  anisotropie structurée peut conduire à des solutions globales régulières;
  son domaine principal est `T^2×R` et sa classe n'est pas (1).
- `NS-SRC-0129` et `0130` donnent des théorèmes globaux axisymétriques sous
  condition critique de circulation ou petitesse du swirl. Aucun ne transforme
  (1) en candidat singulier.
- `NS-SRC-0131` construit une section hélicoïdale anisotrope pour Euler,
  piècewise lisse et non compacte dans `R^3`; viscosité, admissibilité Clay et
  endpoints du présent cycle manquent tous.

Aucune source primaire auditée n'énonce le couplage
`curl compact + faible-L^3 non petit + faible-L^(3/2) borné + direction
log-BMO`. Le corpus atteint 131 entrées; le lemme ci-dessus demeure une
dérivation interne.

## Passe contradictoire

1. **Courbure.** Le terme `psi/r` n'est pas négligé : le choix `R/r` l'annule
   exactement dans `W_z`.
2. **Endpoint faible.** Les bornes inférieures viennent de sous-ensembles de
   mesure explicite; aucune interpolation forte n'est utilisée.
3. **Anisotropie.** Les deux transitions sont nécessaires. Les inégalités
   séparées de (8), et non leur seul produit, forcent `a/R` et `b/R` à rester
   tous deux positifs.
4. **Zéros de vorticité.** La direction n'est évaluée que dans une boule où
   `|chi'|>=c_chi` et `eta=1`; aucun choix de direction aux zéros n'intervient.
5. **Compacité.** `U` est construit en amont et `W=curl U`; il n'existe aucun
   problème de moment ou de queue de Biot–Savart.
6. **Profils variables.** Les constantes de transition de `eta_n,chi_n`
   pourraient dégénérer. Le lemme exige des profils fixes, ou une non-
   dégénérescence uniforme équivalente.
7. **Superpositions.** Des couches non séparables peuvent masquer une zone de
   transition par une autre composante. Elles ne sont pas couvertes.
8. **Dynamique.** Le temps diffusif de la plus petite largeur vaut
   `min(a,b)^2/nu`. Aucun temps d'interaction uniforme ni propagation de la
   géométrie n'est démontré.
9. **Clay.** Exclure cette classe de données initiales ne prouve ni régularité
   globale ni absence de tout profil de blow-up.

La passe analytique indépendante confirme les trois proxies et l'identité
algébrique plus directe suivante. Si `q=c(kappa/K)^3`, les gates donnent
`x^2/y>=q` et `y^2/x>=q`; donc

```text
x^3=(x^2/y)^2(y^2/x)>=q^3,
y^3=(y^2/x)^2(x^2/y)>=q^3.
```

Elle attaque aussi toute généralisation abusive à un curl compact arbitraire.
Sur une boule `B`, l'identité exacte n'est pas `integral_B curl U=0`, mais

```text
integral_B curl U=integral_(partial B) n cross U.
```

Le champ compact
`U_chi=chi(r,z)(-x_2,x_1,0)/2` a `curl U_chi=e_3` sur son cœur : toute boule
interne y a oscillation directionnelle nulle, la compensation étant exportée
par le flux de bord. Le rapport d'audit isole une minoration avec ce défaut et
une bonne sphère conditionnelle via faible-`L^3(U)`. Ce contre-profil ne touche
pas la boule de calotte explicite de (1), mais prouve que le pivot non séparable
devra suivre les flux locaux au lieu d'invoquer seulement
`integral_(R^3)curl U=0`.

## Résultat négatif et pivot local

Le grand rapport d'aspect ne sauve pas la construction compacte séparable du
cycle 0027 : il échange l'obstruction log-BMO contre une perte critique
quantifiée. Le verrou est donc révisé en
`GAP-NONSEPARABLE-COMPACT-CURL-FLATNESS`.

La prochaine expérience décisive doit tester une somme compacte à deux couches

```text
psi=sum_(k=1)^2 V_k(R/r) eta_k((r-R)/a_k)chi_k(z/b_k),
```

avec transitions décalées. Elle cherchera soit un masquage réel des deux zones
de dérivée à normes faibles bornées, soit un ledger de distribution montrant
que le coût de (5) survit aux annulations vectorielles. Le critère d'abandon
sera une minoration uniforme du coût Lorentz par couche active, indépendante
du décalage.

## Reproduction

```text
python -B experiments/navier-stokes/compact-swirl-aspect/compact_swirl_aspect_audit.py
```

Le script emploie seulement `fractions.Fraction`. Il vérifie les identités
d'échelle, les deux budgets anisotropes, l'implication de non-amincissement et
la famille dyadique (12). Il ne certifie ni les constantes des profils lisses,
ni le lemme géométrique all-ball, ni une évolution de Navier–Stokes.

Sortie obtenue : 37 214 contrôles, zéro échec. Empreinte SHA-256 du script :
`e392e3570e4de6f85bcb5f91a7eef6b36a1ed22c55bf8c483a918319b9a848e4`.
