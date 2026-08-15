# Cycle 0047 — dérenormalisation exacte et classe ancienne obtenue

Date : 2026-08-15.

## Décision adaptative

Le verrou relu est `GAP-TYPE-I-DERENORMALIZATION-CLASS`. Les trois actions
réversibles ont été notées avant dérivation :

| action | nouveauté | tractabilité | falsifiabilité | levier | total |
|---|---:|---:|---:|---:|---:|
| transporter exactement équation, pression et énergie locale | 3 | 5 | 5 | 5 | **18** |
| promouvoir immédiatement la limite en solution ancienne mild | 4 | 2 | 4 | 5 | 15 |
| appliquer directement une rigidité ancienne faible-`L3` | 4 | 2 | 4 | 5 | 15 |

La première action est sélectionnée. Le lemme actif est borné : identifier
la classe exacte produite par l'inverse du drift constant. La mildness et la
rigidité ne sont ni supposées ni traitées comme des conséquences formelles.

## Entrée exacte

Soit `kappa>0` et soit `Z,Pi` sur `R3 x (-infinity,0]` la limite diagonale des
cycles 0045–0046. Dans les distributions,

```text
partial_s Z-Delta_y Z+div_y(Z tensor Z)+nabla_y Pi
  +kappa(1+y dot nabla_y)Z=0,
div_y Z=0.                                           (47.1)
```

Sur chaque cylindre compact,

```text
Z in L-infinity_s L2_y,loc inter L2_s H1_y,loc,
Z in L3_loc,
Pi in L^(3/2)_loc,                                  (47.2)
```

et la distribution d'énergie vérifie

```text
L_Z:=partial_s E_Z-Delta_y E_Z+|nabla_y Z|²
     +div_y[(E_Z+Pi)Z]
     +kappa div_y(yE_Z)-kappa E_Z <=0,
E_Z=|Z|²/2.                                         (47.3)
```

Le cycle 0046 donne `Z` non identiquement nulle. Les champs prélimites
vérifient uniformément

```text
ess sup_s K_3(Z_j(s))<=M_0,
ess sup_s K_(3/2)(Pi_j(s))<=M_1,
Pi_j=R_aR_b(Z_(j,a)Z_(j,b)).                       (47.4)
```

## Héritage global de la jauge de pression

La convergence locale du cycle 0045 ne doit pas être confondue avec une
convergence globale forte. Elle suffit néanmoins à identifier les limites
faible-étoile globales.

Munissons `L^(3,infinity)` de la norme duale équivalente à sa quasi-norme de
distribution. Comme `L^(3/2,1)(R3)` est séparable, (47.4) et Banach–Alaoglu
donnent, sur chaque fenêtre finie,

```text
Z_j weak-* -> Z_tilde dans
L-infinity_s L^(3,infinity)_y.                     (47.5)
```

La forte convergence locale `L2` identifie `Z_tilde=Z` dans les
distributions. Ainsi

```text
ess sup_s K_3(Z(s))<=C M_0.                        (47.6)
```

La multiplication de Lorentz donne uniformément

```text
Z_j tensor Z_j borne dans
L-infinity_s L^(3/2,infinity)_y.                   (47.7)
```

Le prédual `L^(3,1)` est séparable. Une nouvelle extraction faible-étoile,
jointe à la forte `L3_loc`, identifie sa limite à `Z tensor Z`. Les Riesz sont
bornés sur `L^(3/2,infinity)` et leur transposée est bornée sur `L^(3,1)`;
ils sont donc continus pour ce passage faible-étoile. La pression de (47.3)
peut être choisie dans la jauge globale

```text
Pi=R_aR_b(Z_aZ_b),
ess sup_s K_(3/2)(Pi(s))<=C M_0².                  (47.8)
```

La partie harmonique du ledger local 0045 est alors la restriction de la
queue Riesz globale, pas un degré de liberté affine ajouté après la limite.
Cette identification ne rend pas la pression fortement compacte.

## Horloge inverse et domaine temporel

Fixons

```text
r(s)=exp(-kappa s),
tau(s)=[1-r(s)²]/(2kappa).                        (47.9)
```

Alors

```text
r_s=-kappa r,
tau_s=r²>0,
s=-(2kappa)^(-1)log(1-2kappa tau),
r=sqrt(1-2kappa tau).                            (47.10)
```

La fonction `s -> tau` est un difféomorphisme croissant de
`(-infinity,0]` sur `(-infinity,0]`. Le choix de la constante dans (47.9)
place simultanément `s=0` et `tau=0`; aucune translation temporelle finale
n'est cachée.

Définissons, avec `x_0` constant arbitraire,

```text
x=x_0+r(s)y,
v(x,tau)=r(s)^(-1)Z(y,s),
q(x,tau)=r(s)^(-2)Pi(y,s).                        (47.11)
```

Le jacobien espace–temps exact est

```text
dx d tau=r³ dy times r² ds=r^5 dy ds.             (47.12)
```

## Transport de l'équation

La relation inverse est `Z(y,s)=r v(x_0+ry,tau(s))`. À `y` fixé,

```text
partial_s Z
 =r³ partial_tau v-kappa r(v+x dot nabla_x v),
D_y Z:=Z+y dot nabla_y Z
 =r(v+x dot nabla_x v),                           (47.13)
```

où `x` désigne ici `x-x_0` dans le terme de dilatation. De plus,

```text
Delta_y Z=r³ Delta_x v,
div_y(Z tensor Z)=r³ div_x(v tensor v),
nabla_y Pi=r³ nabla_x q,
div_y Z=r² div_x v.                               (47.14)
```

Le drift de (47.1) annule donc exactement les deux termes de (47.13), et

```text
partial_tau v-Delta_x v+div_x(v tensor v)+nabla_x q=0,
div_x v=0                                         (47.15)
```

sur `R3 x (-infinity,0]` dans les distributions.

Pour le vérifier sans invoquer une différentiabilité de `Z`, soit `phi` un
test compact en `(x,tau)` et posons

```text
Psi(y,s)=r(s)² phi(x_0+r(s)y,tau(s)).              (47.16)
```

Le changement de variables (47.12) transforme l'action de (47.15) contre
`phi` en l'action de (47.1) contre `Psi`. Si `phi` est solénoïdal, alors
`div_y Psi=r³div_x phi=0`. Cette identité de tests justifie (47.15) pour la
solution faible, indépendamment du calcul formel (47.13).

## Pression, taille critique et non-trivialité

La covariance d'ordre zéro des Riesz donne depuis (47.8)

```text
q=R_aR_b(v_av_b).                                  (47.17)
```

En effet, `v_av_b=r^-2(Z_aZ_b)(dot/r)` et le facteur `r^-2` traverse
l'opérateur homogène d'ordre zéro.

Pour tout `lambda>0`, le changement `x=x_0+ry` donne exactement

```text
lambda |{|v|>lambda}|^(1/3)
 =(r lambda)|{|Z|>r lambda}|^(1/3),
K_3(v(tau))=K_3(Z(s)).                             (47.18)
```

La sortie vérifie donc

```text
v in L-infinity_tau L^(3,infinity)_x               (47.19)
```

au sens essentiel, avec la même quasi-norme. La transformation est
bijective. Plus quantitativement, sur toute région correspondante,

```text
integral |v|³ dx d tau
 =integral r²|Z|³ dy ds.                           (47.20)
```

Le poids est strictement positif et borné au-dessus et au-dessous sur toute
fenêtre finie. La non-trivialité du cycle 0046 est donc conservée.

## Transport de l'inégalité locale d'énergie

Posons `E_v=|v|²/2`. On a `E_Z=r²E_v`. Un calcul terme à terme donne

```text
partial_s E_Z
 =r^4 partial_tau E_v
  -kappa r²(2E_v+x dot nabla_x E_v),

-Delta_y E_Z+|nabla_y Z|²
 =r^4[-Delta_x E_v+|nabla_xv|²],

div_y[(E_Z+Pi)Z]
 =r^4 div_x[(E_v+q)v],

kappa div_y(yE_Z)-kappa E_Z
 =kappa r²(2E_v+x dot nabla_xE_v).                (47.21)
```

Les termes en `kappa` s'annulent exactement. Si

```text
L_v:=partial_tau E_v-Delta_xE_v+|nabla_xv|²
     +div_x[(E_v+q)v],                             (47.22)
```

alors

```text
L_Z=r^4 L_v.                                       (47.23)
```

Pour toute fonction test non négative `varphi` compacte,

```text
<L_v,varphi>_(x,tau)
 =<L_Z,r varphi(x_0+r dot,tau(s))>_(y,s).          (47.24)
```

Le test de droite reste lisse, compact et non négatif. (47.3) implique donc
`L_v<=0` : l'inégalité locale d'énergie standard est préservée.

Sur un cylindre physique compact, `r` est borné et minoré. Les identités

```text
integral_K |v(tau)|² dx
 =r integral_((K-x_0)/r)|Z(s)|²dy,

integral |nabla_xv|² dx d tau
 =integral r|nabla_yZ|²dy ds,

integral (|v|³+|q|^(3/2))dx d tau
 =integral r²(|Z|³+|Pi|^(3/2))dy ds              (47.25)
```

montrent que la classe d'énergie locale de (47.2) est conservée.

## Classe obtenue et classes non obtenues

La conclusion exacte est : `v,q` est une solution ancienne non triviale,
distributionnelle, solénoïdale et **faible adaptée locale** de Navier–Stokes
standard non forcé sur `R3 x (-infinity,0]`, avec pression globale de Riesz et
borne uniforme faible-`L3`.

Le ledger ne démontre pas :

1. `v in L-infinity_tau L2_x` ou une énergie globale finie; un champ
   faible-`L3` peut avoir une queue `|x|^-1` et une énergie infinie;
2. l'inégalité d'énergie globale d'une solution de Leray–Hopf;
3. une décomposition forward `v=e^{(tau-tau_0)Delta}v(tau_0)+w` avec le
   correcteur énergétique requis par la classe de Barker–Seregin–Šverák;
4. la formule intégrale de Duhamel sur chaque intervalle ancien, donc la
   mildness;
5. la bornitude `L-infinity_x`, la régularité classique ou une décroissance
   spatiale uniforme;
6. que `(x_0,0)` soit singulier, ni que la trace correspondant à l'ancien
   endpoint soit non nulle si aucune translation préalable n'a été faite.

La pression de Riesz (47.17) exclut les pressions affines parasites dans la
classe obtenue, mais ne remplace pas la mildness. Aucun théorème de Liouville
pour toute solution ancienne locale adaptée et uniformément faible-`L3`
non nulle n'est enregistré dans le corpus.

## Passe adverse principale

Les erreurs suivantes produisent un résidu non nul :

1. choisir `r=e^(+kappa s)` double le drift au lieu de l'annuler;
2. prendre `tau_s=1` laisse les coefficients `r^-2` devant diffusion et
   non-linéarité;
3. définir `v=Z` au lieu de `r^-1Z` désaccorde diffusion et convection;
4. définir `q=r^-1Pi` laisse un gradient de pression d'une autre puissance;
5. utiliser `dx d tau=r³dy ds` oublie l'horloge et fausse le test faible;
6. omettre `-kappa E_Z` dans (47.3) laisse un résidu `kappa E_Z` dans
   l'énergie physique;
7. déclarer Leray–Hopf depuis la seule borne faible-`L3` perd l'intégrabilité
   globale `L2`;
8. déclarer mild depuis l'absence de pression affine inverse une implication
   non démontrée.

Le certificat exact du cycle encode les cinq premiers résidus et la
cancellation énergétique; il ne simule pas Navier–Stokes.

## Portée Clay et prochain verrou

Le maillon `GAP-TYPE-I-DERENORMALIZATION-CLASS` est fermé au statut interne :
la branche conditionnelle produit une solution ancienne standard non triviale
locale adaptée, globalement bornée en faible-`L3`. Cela ne contredit aucun
théorème général connu et ne résout pas le problème Clay, car l'existence du
blow-up Type I reste supposée et la rigidité de cette classe manque.

Le verrou suivant est
`GAP-TYPE-I-ANCIENT-WEAK-L3-RIGIDITY-OR-MILDNESS`. L'expérience décisive doit
tester l'une des deux implications falsifiables :

```text
ancienne locale adaptée + Riesz + L-infinity_t L^(3,infinity)_x
  -> classe scindée/mild sur chaque intervalle forward,
```

ou construire un contre-objet admissible montrant exactement quelle énergie
de queue ou quelle continuité initiale manque. Une rigidité ne sera appliquée
qu'après fermeture de cette porte.

## Reproduction

~~~powershell
python -B experiments/navier-stokes/derenormalization/derenormalization_audit.py
~~~
