# Cycle 0044 — échappement local de la force sous cutoff externe

Date : 2026-08-15

Statut : `AI_INTERNAL_DERIVATION`; aucun résultat Clay.

## Décision adaptative

| Action | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| déplacer la transition à l'échelle `L` et estimer directement la queue de Leray sur les compacts | 4 | 5 | 5 | 5 | **19** |
| rechercher une borne globale uniforme dans `X=L1+div L^(3/2,infinity)` | 3 | 3 | 5 | 4 | 15 |
| définir d'abord une topologie faible-étoile abstraite pour `X` | 3 | 2 | 4 | 4 | 13 |

La première action est sélectionnée. La seconde sera utilisée comme test
adverse : elle est incompatible avec le scaling du terme de dilatation sur
une famille annulaire critique. La troisième est différée jusqu'à ce que la
topologie réellement requise par le passage local soit connue.

## Cadre exact

On conserve le cadre des cycles 0041–0043 : Navier–Stokes incompressible 3D
non forcé, viscosité un, sur `R3`, pour une solution classique avant `T_*`.
Dans les variables Type I normalisées,

```text
U(y,sigma)=R u(x_*+Ry,t),
P(y,sigma)=R²p(x_*+Ry,t),
D=1+y dot nabla,
kappa=-RR',
sup_sigma K_3(U(sigma))<=M.
```

La pression est fixée par la jauge globale de Riesz et

```text
H=P_L div(U tensor U)=div(U tensor U+P I),
```

où `P_L` désigne la projection de Leray globale. Toutes les identités sont
d'abord établies pour `U,P` lisses. La conclusion du cycle est locale dans
l'espace, uniforme en `sigma`, et conditionnelle à la borne Type I.

## Cutoff externe et opérateur conjugué

Fixons

```text
A={1<|z|<2},
chi in C_c^infinity(B_2),
chi=1 sur un voisinage de Bbar_1,
supp nabla chi compact dans A.
```

Pour `L>=1`, posons

```text
chi_L(y)=chi(y/L),
a_L(y)=nabla chi_L(y)=L^-1 a(y/L),
A_L=L A.
```

La droite inverse fixée du cycle 0043 est conjuguée par

```text
B_L g(y)=L B_A[g(L dot)](y/L).                (44.1)
```

Alors `div B_Lg=g`, le support de `B_Lg` est contenu dans `A_L`, et

```text
Q_LW=chi_LW-B_L(a_L dot W)                    (44.2)
```

est divergence-free lorsque `W` l'est. De plus,

```text
Q_LW=W dans B_L,
supp Q_LW subset Bbar_(2L),
K_3(Q_LW)<=C_Q K_3(W),                        (44.3)
```

avec `C_Q` indépendant de `L`. La dernière borne est exactement la
conjugaison à rapport d'aspect fixe du claim
`NS-SOLENOIDAL-ANNULAR-CUTOFF`; aucun estimateur sur une couronne mince n'est
utilisé.

Définissons `Z_L=Q_LU`. Dans la convention de signe des cycles précédents,
l'équation est

```text
partial_sigma Z_L-Delta Z_L+P_L div(Z_L tensor Z_L)+kappa D Z_L=F_L.
```

Sa force vaut

```text
F_L=
  P_L div(Z_L tensor Z_L)
  -Q_LH
  -[Delta,Q_L]U
  +kappa[D,Q_L]U.                              (44.4)
```

## Lemme actif : identité locale exacte

Soit `rho>0` fixé et `L>=2rho`. Dans `B_rho`, (44.3) implique, pour toute
entrée lisse,

```text
Q_LH=H,
[Delta,Q_L]U=0,
[D,Q_L]U=0.                                   (44.5)
```

Il ne s'agit pas d'une petitesse : chaque égalité est exacte parce que la
transition et le correcteur sont supportés hors de `B_L`. En utilisant la
jauge de pression fixée,

```text
H=P_L div(U tensor U),
```

les équations (44.4)–(44.5) donnent dans `B_rho`

```text
F_L=P_L div E_L,
E_L=Z_L tensor Z_L-U tensor U,                 (44.6)
supp E_L subset R3\B_L.                        (44.7)
```

Le tenseur `E_L` n'est pas compact : hors de `B_(2L)`, il vaut
`-U tensor U`. Cette queue ne doit pas être supprimée.

## Estimation explicite de la queue de Leray

Écrivons

```text
K_E=K_(3/2)(E_L).
```

Le produit Lorentz et (44.3) donnent, composante par composante,

```text
K_E<=C_E(1+C_Q²)M²,                            (44.8)
```

où `C_E` est la constante nommée du produit et du quasi-triangle
faible-Lorentz. Elle ne dépend ni de `L`, ni de `sigma`.

Loin du support de `E_L`, la partie locale `div E_L` de la projection est
nulle. Il reste le noyau de

```text
-nabla Delta^-1 div div E_L,
```

soit trois dérivées du potentiel newtonien. Pour tout multi-indice `alpha`,
fixons la constante explicite de noyau

```text
|partial^alpha partial_i partial_j partial_k N(x)|
 <=C_(P,alpha)|x|^(-4-|alpha|).                 (44.9)
```

Décomposons l'extérieur en coquilles

```text
A_k={2^kL<|y|<=2^(k+1)L}, k>=0.
```

Leur volume vaut

```text
|A_k|=(28pi/3)(2^kL)^3.
```

L'inclusion exacte sur un ensemble de mesure finie,

```text
integral_E |f|
 <=3 K_(3/2)(f)|E|^(1/3),                      (44.10)
```

et `|x-y|>=(2^kL)/2` pour `x in B_rho`, donnent

```text
integral_(A_k)
 |E_L(y)| |partial^alpha nabla^3N(x-y)| dy

 <=3(28pi/3)^(1/3) C_(P,alpha) 2^(4+|alpha|)
   K_E L^(-3-|alpha|)2^(-k(3+|alpha|)).        (44.11)
```

La série géométrique est sommable. Ainsi,

```text
sup_sigma ||partial^alpha F_L(sigma)||_(L-infinity(B_rho))
 <=C_(rho,alpha,Q) M² L^(-3-|alpha|),          (44.12)

C_(rho,alpha,Q)=
  [3(28pi/3)^(1/3)2^(4+|alpha|)
   /(1-2^(-3-|alpha|))]
  C_(P,alpha)C_E(1+C_Q²).                      (44.13)
```

La constante écrite ne dépend en fait de `rho` dès que `L>=2rho`; l'indice
`rho` rappelle seulement la condition géométrique. En particulier,

```text
F_L ->0 dans C^infinity_(x,loc)(R3)
```

uniformément en temps sur toute fenêtre où la borne Type I vaut. Cette
conclusion porte sur la force de (44.4), non sur chaque terme projeté pris
séparément.

## Diagonale physique licite

Si `R_j->0` est une suite d'échelles pré-singulières, on peut choisir

```text
L_j->infinity,
L_jR_j->0,                                     (44.14)
```

par exemple après sous-suite `L_j=min(j,R_j^(-1/2))`. Le core physique
`B_(R_j)` reste inchangé, la transition se trouve à la distance `L_jR_j`
qui tend encore vers zéro, tandis que son image normalisée s'éloigne de tout
compact. Le paramètre `L_j` est constant sur la fenêtre temporelle de chaque
élément; aucune dérivée `L_j'` n'est introduite.

La capture Type I dans `B_1` est donc conservée exactement et (44.12) donne
une force localement évanescente. Cela ne fournit pas encore la compacité
temporelle des solutions ni la non-trivialité d'une trace limite.
Sur une fenêtre normalisée fixe, ce raccord physique suppose aussi que
`R(t)/R_j` reste entre deux constantes; cette comparabilité doit être
recalculée lors du futur ledger temporel.

## Test adverse : la norme globale ne reste pas uniforme

La décroissance locale ne peut pas être promue en une borne globale uniforme
dans `X`. Prenons ici `chi` radial et choisissons un pure-swirl lisse `U_*`,
supporté dans la région où
`z dot nabla chi` n'est pas identiquement nul, puis

```text
U_L(y)=L^-1U_*(y/L).                            (44.15)
```

Cette famille est divergence-free et `K_3(U_L)=K_3(U_*)`. La radialité du
cutoff annule les deux entrées de Bogovskii. Si `P_*` est la pression de
Riesz de `U_*` et `H_*=P_L div(U_* tensor U_*)`, posons

```text
h=[D,Q_1]U_*=(z dot nabla chi)U_* !=0,
B_0=P_L div(Q_1U_* tensor Q_1U_*)
    -Q_1H_*-[Delta,Q_1]U_*,
```

La conjugaison exacte, l'invariance de Leray et les ordres respectifs des
termes donnent pour la force complète

```text
F_L=L^-3B_0(y/L)+kappa L^-1h(y/L).             (44.16)
```

Prenons un test lisse `psi` tel que
`A=<h,psi>!=0`, puis `psi_L(y)=psi(y/L)`. La norme `L-infinity` de `psi_L`
et la norme `L^(3,1)` de `nabla psi_L` sont indépendantes de `L`. Pour toute
représentation `F_L=f+div G`, la dualité de Lorentz donne

```text
|<F_L,psi_L>|
 <=C_psi[||f||_L1+||G||_(L^(3/2,infinity))].   (44.17)
```

Or (44.16) implique

```text
<F_L,psi_L>=kappa L²A+<B_0,psi>.               (44.18)
```

Si `kappa!=0`, alors

```text
||F_L||_X >=c_psi|kappa|L²-C_psi'.             (44.19)
```

Le budget global de la force complète croît donc au moins comme `L²` sur
cette famille critique, même si `F_L` tend vers zéro sur chaque compact
fixé pour `L` assez grand. Le facteur externe ne doit jamais être injecté
dans la constante globale du cycle 0043 comme s'il était gratuit.

Ce profil est un test cinématique à temps fixé, non une solution ancienne ou
stationnaire de Navier–Stokes. Il réfute seulement une estimation spatiale
globale qui dépendrait de la borne faible-`L3` seule.

## Passe contradictoire

1. **Delta de Leray.** Le noyau de `P_L div` contient une partie locale.
   Elle ne peut être omise qu'après (44.7), lorsque le point d'évaluation est
   séparé du support de `E_L`.
2. **Queue non compacte.** `E_L=-U tensor U` hors de `B_(2L)`. La preuve
   somme toutes les coquilles jusqu'à l'infini; elle ne remplace pas cette
   queue par un support fini.
3. **Pression.** L'identité (44.6) utilise la jauge globale de Riesz. Une
   pression locale définie modulo une fonction harmonique requiert un terme
   de raccord supplémentaire.
4. **Lorentz faible.** La décroissance vient du noyau d'ordre quatre et de
   l'inclusion locale (44.10), non de l'absolue continuité de la quasi-norme
   faible-`L^(3/2)`, qui est fausse en général.
5. **Temps.** Le supremum en `sigma` de (44.12) utilise la borne Type I au
   même quantificateur temporel. Un supremum essentiel ne donne qu'une
   conclusion presque partout sans choix de représentant.
6. **Global contre local.** (44.19) interdit toute conclusion de convergence
   dans le `X` global. Seule la convergence sur tests compacts est obtenue.
7. **Diagonale.** Il faut simultanément `L_j->infinity` et `L_jR_j->0`.
   Prendre `L_j=R_j^-1` laisserait une transition physique macroscopique.
8. **Solution limite.** Une force tendant vers zéro dans `C^infinity_loc`
   ne fournit pas à elle seule la compacité forte de `Z_j`, le passage de
   `Z_j tensor Z_j`, l'inégalité d'énergie locale ou une trace terminale non
   nulle.
9. **Dérenormalisation et rigidité.** Une limite à force nulle résout d'abord
   l'équation renormalisée avec drift `+kappa D`. Le raccord à une solution
   ancienne standard doit être effectué avec son horloge exacte. Même alors,
   une solution ancienne non triviale bornée dans faible-`L3` ne tombe pas
   automatiquement sous un théorème de Liouville général connu.
10. **Clay.** La borne Type I globale n'est pas contrôlée par l'énergie des
    données Clay et le cas Type II n'entre dans aucun estimateur uniforme.

## Résultat et nouveau verrou

Le cycle ferme le sous-gap

```text
GAP-TYPE-I-FORCE-LOCAL-ESCAPE
```

pour les cutoffs externes homothétiques : la force complète disparaît à la
vitesse `L^-3` sur tout compact, avec dérivées. Il réfute simultanément la
version globale uniforme dans `X` lorsque `kappa!=0`.

Le gap `GAP-TYPE-I-FORCE-COMPACTNESS` n'est donc pas fermé en bloc. Il est
remplacé par

```text
GAP-TYPE-I-LOCAL-COMPACTNESS-TRACE
  : obtenir, sur une suite (j,L_j), la compacité forte locale, le passage de
    l'inégalité d'énergie et une trace non triviale;

GAP-TYPE-I-ANCIENT-WEAK-L3-RIGIDITY
  : dérenormaliser avec l'horloge exacte, puis obtenir, exclure ou classifier
    une solution ancienne non forcée, sans supposer auto-similarité,
    axisymétrie ou bornitude L-infinity.
```

La prochaine expérience décisive doit écrire un ledger Aubin–Lions local sur
les cylindres `B_rho x [-S,0]`, avec espaces exacts pour `partial_sigma Z_j`,
pression, force et produit quadratique, puis rechercher un contre-profil de
concentration temporelle qui conserve toutes les bornes disponibles mais
empêche la compacité forte.
