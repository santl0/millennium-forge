# Cycle 0020 — obstruction `bmo_phi` entre cœurs actifs

Date de gel : 2026-08-14.

Statut : dérivation interne falsifiable, certificat exact et trois passes
contradictoires par la même famille de modèles. Aucun résultat n'est une preuve
de régularité globale ou de blow-up.

## Décision du cycle

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| réfuter ou quantifier l'extension depuis plusieurs cœurs actifs | 5 | 5 | 5 | 5 | **20** |
| tester l'admissibilité PDE complète du profil critique ponctuel | 4 | 3 | 4 | 5 | 16 |
| construire une dynamique annulaire de déplétion | 4 | 3 | 4 | 5 | 16 |

Le verrou sélectionné est `GAP-ACTIVE-CORE-BMO`. Le lemme actif est une
borne inférieure d'oscillation indépendante de toute valeur choisie dans le
corridor où la vorticité s'annule. L'expérience décisive réalise deux cœurs
opposés par un champ initial lisse, compact et divergence-free.

## Équation et type de solution

Le cadre Clay pertinent est Navier–Stokes incompressible, visqueux, non forcé,
sur `R³`, sans frontière :

```text
partial_t u + (u dot nabla)u = -nabla p + nu Delta u,
div u = 0,
u(0)=u_0,                    nu>0.
```

La famille adverse de ce cycle fournit seulement des données
`u_0 in C_c^infinity(R³;R³)`, divergence-free. Chaque donnée engendre une
solution classique locale, mais le calcul ne montre pas que les deux cœurs
subsistent dans une trajectoire, encore moins près d'un temps singulier.

La dérivation géométrique s'applique à une direction mesurable bornée
`xi`. Lorsqu'elle est raccordée à la vorticité, on exige

```text
omega = curl u,        omega = |omega| xi,        |xi|<=1.
```

Sur `{omega!=0}`, `xi=omega/|omega|`. Sur `{omega=0}`, cette identité ne fixe
aucune valeur.

## Hypothèse primaire auditée

La version `arXiv:2607.08866v2` définit, pour `phi(r)=1/|log r|`,

```text
||f||_(bmo_phi)
 = ||f||_infinity
   + sup_(x in R³, 0<r<1/2)
       phi(r)^(-1) average_(B_r(x)) |f-c_(B_r(x))|.
```

Son théorème 4.1 suppose globalement

```text
xi in L^infinity((T*-epsilon,T*); bmo_phi(R³)).
```

Le supremum porte donc sur tous les centres, pas seulement sur un super-niveau
actif de `|omega|`. La petitesse d'échelle est locale, mais l'hypothèse
spatiale est globale. Le texte ne fixe pas `xi` sur `{omega=0}`.

Cette norme n'est pas littéralement le
`tilde-bmo_phi` de Bradshaw–Grujić (2015) : ce dernier est ancré par `L¹` et
porte sur `psi xi`, avec une coupure compacte. Les travaux de Goldberg,
Janson et Nakai–Yabuta expliquent les espaces locaux et pondérés, mais ne
permettent pas d'identifier silencieusement ces deux normalisations.

## Lemme actif : séparation de phases

Soit `D` un ensemble mesurable de mesure finie positive. Soient `E_+` et
`E_-` deux sous-ensembles disjoints de fractions

```text
a=|E_+|/|D|,        b=|E_-|/|D|,        a+b>0.
```

Si `|e|=1`, `xi=e` sur `E_+` et `xi=-e` sur `E_-`, alors toute extension
mesurable intégrable sur `D` vérifie

```text
MO_D(xi) := average_D |xi-xi_D| >= 4ab/(a+b).             (1)
```

### Preuve

Posons `G=D\(E_+ union E_-)`, `g=average_G xi` lorsque `|G|>0`, et
`c=xi_D`. Par Jensen, remplacer `xi` sur `G` par sa moyenne ne peut
qu'abaisser l'oscillation. Après projection orthogonale sur `e`, toute
composante transverse ne peut également qu'augmenter les distances. Le
problème se réduit donc à une valeur scalaire constante `z` dans le corridor.

La moyenne globale vaut `c=a-b+(1-a-b)z`. La fonction convexe

```text
F(z)=a|1-c|+b|-1-c|+(1-a-b)|z-c|
```

atteint son minimum pour

```text
z=(a-b)/(a+b),       c=z,
```

et sa valeur est `4ab/(a+b)`. Cette valeur satisfait `|z|<=1`; la constante
reste donc optimale même sous la contrainte `|xi|<=1`. Le détail, y compris
les cas limites, figure dans la passe contradictoire `cycle-0020-analysis.md`.

Une borne plus courte mais non optimale,

```text
MO_D(xi) >= min(a,b)|e-(-e)| = 2 min(a,b),
```

s'obtient directement par l'inégalité triangulaire avec `c=xi_D`. Elle est
suffisante dans le cas symétrique `a=b` et sert de certificat minimal dans le
script.

## Conséquence log-BMO et loi d'échelle

Pour éviter le logarithme d'une longueur dimensionnée, fixons une longueur
`R_*>0` et

```text
phi_*(r)=1/[1+log(R_*/r)],       0<r<=R_*.
```

Si `D` est une boule de rayon `r_D`, (1) impose

```text
[xi]_(bmo_phi*)
 >= [4ab/(a+b)] [1+log(R_*/r_D)].                       (2)
```

Sous le scaling Navier–Stokes

```text
u_kappa(x,t)=kappa u(kappa x,kappa²t),
omega_kappa(x,t)=kappa² omega(kappa x,kappa²t),
```

`xi`, `a`, `b` et l'oscillation sont invariants, tandis que `r_D` et `R_*`
ont tous deux le poids `-1`; le quotient `r_D/R_*` et (2) sont donc
invariants.

Une paire isolée ne force qu'un coût fini. Une famille à échelles
`r_n -> 0` interdit une borne uniforme seulement si

```text
[4a_n b_n/(a_n+b_n)] [1+log(R_*/r_n)] -> infinity.       (3)
```

Le volume relatif minoritaire est indispensable. Une affirmation reposant
sur le seul angle antipodal est fausse.

## Test exact à deux boules

Prenons deux boules `B_epsilon(+2epsilon e_1)` et
`B_epsilon(-2epsilon e_1)`, contenues dans `B_(3epsilon)(0)`. Chacune occupe
la fraction `1/27` de la boule test. Avec les directions `+e_3` et `-e_3`,

```text
MO_(B_(3epsilon)) xi >= 2/27.                            (4)
```

Pour `3epsilon_n=exp(-n)` dans la convention primaire,

```text
phi(3epsilon_n)=1/n,
[xi]_(bmo_phi) >= 2n/27 -> infinity.                     (5)
```

L'oscillation sur chaque cœur constant est pourtant nulle. La cohérence
parfaite composante par composante ne se globalise donc pas uniformément.

## Réalisation divergence-free instantanée

Autour de `p_sigma=sigma 2epsilon e_1`, choisissons une coupure lisse
`chi_sigma`, égale à un sur `B_epsilon(p_sigma)` et supportée dans
`B_(3epsilon/2)(p_sigma)`. Les supports sont disjoints. Définissons

```text
B_3=-(sigma A/4)(y_1²+y_2²) chi_sigma,
u_sigma=curl(B_3 e_3).
```

Alors `u=sum_sigma u_sigma` est dans `C_c^infinity`, et `div u=0` exactement.
Dans chaque cœur,

```text
u_sigma=(-sigma A y_2/2, sigma A y_1/2,0),
curl u_sigma=sigma A e_3.
```

Le polynôme de rotation solide non coupé vérifie localement l'équation
stationnaire avec `Delta u=0` et
`p=A²(y_1²+y_2²)/8`. Cette vérification n'est pas un calcul de la pression du
champ global coupé : les coquilles de transition ont un résidu non nul et la
pression de Leray y est non locale.

Avec `A_epsilon=epsilon^-2`, le ledger d'échelle donne

```text
|u|~epsilon^-1,   |omega|~epsilon^-2,   volume~epsilon³,
||u||_2²~epsilon, ||omega||_(L^(3/2,infinity))~1.
```

Une superposition dyadique idéale de cœurs internes, d'amplitude `4^N` et de
volume total `2*8^-N`, a exactement

```text
lambda^(3/2) measure{|omega|>lambda}=2/7
```

aux seuils stricts choisis, tandis que son budget d'énergie interne normalisé
somme à `1/5`. C'est un ledger de cœurs, pas une solution dynamique et pas un
certificat pour les coquilles.

## Ambiguïté intrinsèque aux zéros

La solution nulle `u=p=omega=0` sur `R³ x (0,infinity)` a résidu PDE,
divergence et relation `omega=curl u` exactement nuls. Les deux champs
unitaires

```text
xi_good=e_1,
xi_bad= e_1 si x_1>=0, -e_1 si x_1<0
```

satisfont tous deux `omega=|omega|xi`. Le premier a semi-norme nulle. Sur
toute boule centrée sur le plan `x_1=0`, le second a moyenne nulle et
oscillation moyenne un; son quotient par `phi(r)` tend vers l'infini.

Ainsi la propriété « la direction de vorticité appartient à `bmo_phi` »
n'est pas intrinsèque à `(u,omega)` tant qu'une convention ou un quantificateur
d'extension n'est pas spécifié. Ce test ne réfute pas un théorème reformulé
comme l'existence d'une bonne extension mesurable uniforme en temps.

## Passe contradictoire

1. **Constante optimale.** La borne grossière `2 min(a,b)` est remplacée par
   `4ab/(a+b)`; les deux coïncident seulement pour `a=b`.
2. **Dilution.** Si `min(a_n,b_n)=O(1/log(R_*/r_n))`, (2) ne diverge pas.
   Le contraste angulaire seul n'est pas un obstacle uniforme.
3. **Choix du corridor.** L'extension constante
   `(a-b)e/(a+b)` atteint l'optimum; attribuer arbitrairement zéro au corridor
   peut surestimer le coût.
4. **Zéros.** La solution nulle réfute la canonicité, pas l'existence d'une
   extension favorable.
5. **Pression.** Le calcul polynomial interne ne se transfère pas à la coupure
   compacte; aucune pression locale choisie indépendamment ne remplace la
   projection de Leray globale.
6. **Dynamique.** Les champs `u_epsilon` sont des données distinctes, pas des
   tranches d'une même solution approchant `T*`.
7. **Notion de solution.** Les données sont Clay-admissibles et donnent une
   solution forte locale, mais aucune assertion de Leray–Hopf globale,
   d'irrégularité ou de blow-up n'est déduite.

## Verdict et écart avec Clay

Le lemme d'extension universel

```text
cohérence sur chaque composante active
  -> borne globale uniforme bmo_phi
```

est **réfuté**. Une conclusion correcte doit ajouter au minimum une condition
quantitative de mélange ou de packing inter-composantes, équivalente dans le
test antipodal à

```text
4ab/(a+b) = O(phi_*(r_D)).
```

Le théorème conditionnel de la v2 n'est pas réfuté : il suppose déjà la norme
globale. Le transfert vers le problème Clay échoue en amont parce que ni
l'équation, ni l'énergie, ni une cohérence seulement locale ne fournissent la
condition de phase ci-dessus pour une solution générale.

Le sous-verrou `GAP-ACTIVE-CORE-BMO` est fermé négativement pour l'implication
universelle. Le verrou suivant est `GAP-CRITICAL-PROFILE-ADMISSIBILITY` :
tester si le profil critique ponctuel supposé dans la v2 est compatible avec
`div omega=0`, la loi de Biot–Savart, l'énergie finie et une direction globale
log-BMO, avec toutes les constantes indépendantes de la troncature.

## Reproduction

```text
python -B experiments/navier-stokes/active-core-bmo/active_core_bmo_audit.py
```

Le script utilise seulement la bibliothèque standard, des fractions exactes
et aucun aléa. Il exécute douze contrôles. Empreinte SHA-256 :
`df595323ec3630d25747548feb53295b9a849cef8aba1d6b22c101d4136644ae`.

Les trois rapports de revue sont :

- `reviews/cycle-0020-analysis.md` : optimum, scaling et sept attaques;
- `reviews/cycle-0020-countermodel.md` : contrechamp compact indépendant;
- `reviews/cycle-0020-literature.md` : définition primaire, provenance des
  espaces et test de la solution nulle.

