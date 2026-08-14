# Cycle 0027 — porte BMO du retour axisymétrique compact

Date de gel : 2026-08-14.

Statut : dérivation interne falsifiable et certificat rationnel exact. Aucun
résultat n'est promu en preuve publiée ou en résolution Clay.

## Décision du cycle

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| porte BMO d'un lift axisymétrique à aspect fixé | 5 | 5 | 5 | 5 | **20** |
| construction torique à aspect croissant | 5 | 2 | 5 | 5 | 17 |
| évolution validée du retour compact | 4 | 1 | 3 | 4 | 12 |

Le verrou sélectionné est `GAP-NESTED-RETURN-FLOW-CASCADE`. Le lemme actif
teste si le premier lift spatial proposé au cycle 0026 peut cacher le retour
de flux dans une région rare tout en satisfaisant le log-BMO sur toutes les
petites boules.

## Équation et type de solution

La cible Clay reste

```text
partial_t u-Delta u+(u dot nabla)u+nabla p=0,
div u=0
```

sur `R³`, sans frontière ni force, viscosité normalisée. Le cycle construit
seulement un champ statique axisymétrique de type purement azimutal

```text
U=psi(r,z)e_theta,             psi(r,z)=chi(z)A(r),
W=curl U.
```

Le support radial reste éloigné de l'axe, donc aucune singularité de
coordonnées n'est cachée. Le certificat polynomial donne `U∈C_c^4` et
`W∈C_c^3`; une version `C_c^infinity` s'obtient en remplaçant le bump par un
bump standard, mais elle n'est pas le certificat rationnel.

## Construction exacte à deux amplitudes

Posons

```text
b(t)=t^4(1-t)^4  sur 0<t<1, zéro ailleurs,
delta_n=n^-3.
```

Les moments exacts sont

```text
integral_0^1 b(t)dt=1/630,
integral_0^1 t b(t)dt=1/1260.
```

Définissons le profil axial

```text
f_n(r)= n^-1 b(r-1),                         1<r<2,
       -B_n b((r-4)/delta_n),                4<r<4+delta_n,
        0                                    ailleurs,

B_n=3n^5/(8n^3+1).
```

Alors

```text
integral_0^infinity r f_n(r)dr=0,
24n²/65 <=B_n<3n²/8.                         (1)
```

Le potentiel radial

```text
A_n(r)=r^-1 integral_0^r s f_n(s)ds          (2)
```

est compactement supporté. Dans le corridor `2<r<4`,

```text
rA_n(r)=P_n=1/(420n).                         (3)
```

Le cutoff `chi` vaut un sur `|z|<=1`, zéro sur `|z|>=2`, et sa calotte
polynomiale est l'antidérivée normalisée de `b`. Elle vérifie
`chi'=-630b` après translation et `|chi'|<3`.

## Identités div–curl et moyenne

Le curl est exactement

```text
W_r=-chi'(z)A_n(r),
W_theta=0,
W_z=chi(z)[A_n'(r)+A_n(r)/r]=chi(z)f_n(r).    (4)
```

Par conséquent

```text
div W=(1/r)partial_r(rW_r)+partial_z W_z
     =-chi'(A_n'+A_n/r)+chi'f_n=0.            (5)
```

La moyenne de `W_z` est nulle par (1), tandis que la moyenne vectorielle de
`W_r e_r` est nulle après intégration en `theta`. Ainsi

```text
integral_R3 W dx=0,                           (6)
```

en accord avec `W=curl U` compact.

## Échelle critique et énergie

Sur le plateau axial, la phase positive a amplitude `O(n^-1)` et volume
`O(1)`. La phase négative a amplitude `B_n~n²` et largeur radiale `n^-3`.
Une sous-région explicite donne une minoration uniforme de la quasi-norme
faible-`L^(3/2)`; la décomposition des fonctions de distribution donne une
majoration uniforme `K_n<1/9` dans la mesure cylindrique normalisée. La masse
forte critique de la phase négative reste dans un intervalle compact non nul.

Le terme radial de fermeture satisfait dans le corridor

```text
|W_r|<=3P_n=1/(140n).                          (7)
```

Dans la mesure cylindrique normalisée `dtheta/(2pi) r dr dz`, le certificat
donne

```text
||U_n||_2²<=50P_n²=1/(3528n²).                 (8)
```

Sous le scaling Navier–Stokes

```text
U_(n,s)(x)=s^-1 U_n(x/s),
W_(n,s)(x)=s^-2 W_n(x/s),
```

la quasi-norme faible de la vorticité est invariante et l'énergie devient
`s||U_n||_2²`.

## Variante équilibrée — sharpness div–curl du cube

La passe analytique a testé l'échappatoire immédiate : comprimer aussi les
deux calottes axiales à l'épaisseur

```text
tau_n=delta_n=n^-3.                              (9)
```

Le terme radial atteint alors l'amplitude `O(n²)`, mais seulement sur un
volume `O(n^-3)`. Le certificat encadre encore la quasi-norme complète par
deux constantes indépendantes de `n`; dans le domaine parent fixe de volume
normalisé `108`, l'extension par `e_z` satisfait

```text
4n^-3/27 <=MO_D(zeta)<=n^-3.                    (10)
```

La masse conique positive vaut `m_n=1/(210n)` dans la même normalisation.
Ainsi `MO_D` est exactement de l'ordre de `m_n³/K_n³`: l'exposant cubique du
cycle 0026 reste optimal après réalisation compacte div–curl.

Le rapport analytique indépendant renforce ce résultat avec des bumps
`C_c^infinity`: il obtient `m_epsilon=4pi epsilon^(1/3)`,
`MO_D~epsilon`, énergie `~epsilon^(2/3)`, enstrophie
`~epsilon^(-1/3)` et raccord Biot–Savart exact. La vitesse vérifie toutefois
`||U_epsilon||_3->0`, donc ces données lisses sont dans le régime perturbatif
critique et ne sont pas des candidates au blow-up.

Cette variante certifie seulement l'oscillation sur le **domaine parent**.
Elle ne calcule pas le supremum BMO sur les boules qui résolvent les
transitions verticales–radiales. La passe contradictoire confirme que les
raccords directs et les cutoffs séparables usuels gardent des portes locales;
une construction non séparable à couches emboîtées reste ouverte.

Enfin, si une calotte de largeur `tau` transporte le même flux radial, la
masse `L¹` exacte du corridor et l'inégalité faible-Lorentz imposent

```text
tau>=16/[81*420³ K³ n³].                       (11)
```

Une couche exponentiellement plus mince ne peut donc cacher gratuitement le
retour sous une borne critique uniforme.

## Lemme actif — boule radiale de calotte

Soit plus généralement `U=chi(z)A(r)e_theta`. Supposons que le corridor
`R-w<r<R+w`, `z_0-w<z<z_0+w` vérifie

```text
f=A'+A/r=0,       A!=0,       chi' de signe fixe et non nul,
R>w>0.                                            (12)
```

Dans la boule cartésienne

```text
B=B_w((R,0,z_0)),
```

on a `W/|W|=+e_r` ou `-e_r`. Considérons les deux sous-boules de rayon
`w/8`, centrées en `(R,+/-w/2,z_0)`. Elles ont chacune une fraction `1/512`
du volume de `B`. Sur elles, la projection sur `e_y` vérifie respectivement

```text
xi dot e_y >= 3w/[8(R+w)],
xi dot e_y <=-3w/[8(R+w)].                     (13)
```

Le lemme de séparation scalaire donne donc

```text
MO_B(xi)>=3w/[2048(R+w)].                       (14)
```

Cette minoration ne dépend ni de l'amplitude de `W_r`, ni d'une convention
sur les zéros : la vorticité est non nulle dans toute la boule.

Pour la construction (1)–(4), `R=3`, `w=1/4`, `z_0=3/2`, d'où

```text
MO_B(xi)>=3/26624.                              (15)
```

Après remise à l'échelle par `s_n->0`, le rayon test devient `s_nw` mais la
borne (15) ne change pas. Toute semi-norme pondérée par
`1/phi(r)~|log r|` diverge. Le lift axisymétrique séparable à aspect fixé
échoue donc au log-BMO global avant Biot–Savart ou pression.

## Résidu stationnaire

Pour un swirl pur axisymétrique,

```text
(U dot nabla)U=-(psi²/r)e_r,
[-Delta U]_theta=-Lpsi,
L=partial_rr+r^-1partial_r+partial_zz-r^-2.      (16)
```

Dans le corridor, `A=P_n/r` annule la partie radiale de `L`, mais
`Lpsi=A chi''` et le cutoff certifié a cinq coefficients non nuls dans
`chi''`. Le résidu possède donc une composante azimutale non nulle. Une
pression monovaluée ne peut avoir une dérivée azimutale axisymétrique non
nulle. Aucun de ces champs n'est une solution stationnaire.

Sous le scaling ci-dessus, le résidu de vitesse se transforme comme
`R_s=s^-3R(x/s)` et sa norme `L¹` est invariante : la fermeture dynamique ne
devient pas perturbative par simple concentration.

## Passe contradictoire

1. L'annulation vectorielle et la criticité faible-Lorentz sont effectivement
   satisfaites; elles ne suffisent pas au log-BMO.
2. La petitesse de l'amplitude radiale `O(1/n)` est sans effet sur la direction
   normalisée dans le corridor.
3. La boule test utilise seulement des points actifs; aucune extension sur
   `{W=0}` ne peut la réparer.
4. La constante (14) décroît comme `w/R` lorsque l'aspect torique croît. Le
   lemme n'exclut pas `R_n/w_n->infinity`.
5. Le certificat est `C^4`, pas `C^infinity`; le lemme géométrique, lui,
   s'applique identiquement à un cutoff lisse présentant le même corridor.
6. La quasi-norme complète est encadrée, non calculée exactement.
7. La petite oscillation (10) est une moyenne parentale, pas une borne BMO
   all-ball; elle ne contredit pas la porte locale à aspect fixé.
8. La composante azimutale du résidu exclut la stationnarité, mais pas une
   évolution temporelle corrigée.

## Veille différentielle

La veille primaire séparée est conservée dans
`reviews/cycle-0027-literature.md`. Dix sources primaires sont ajoutées
(`NS-SRC-0102`–`0111`). Liu–Wang fournit l'antériorité exacte de la
représentation et les conditions au pôle; Costabel–McIntosh et
Guzmán–Salgado séparent existence d'un correcteur div–curl et uniformité de sa
constante géométrique. Cao–Zhan 2026 est publié; Guo–Jeong–Zhao et
Peralta-Salas–Slobodeanu restent des prépublications v1. Les revendications
2026 de régularité axisymétrique avec swirl restent hors chaîne de preuve,
faute d'audit ligne à ligne et de validation indépendante.

## Verdict et écart avec Clay

Résultat positif borné : le compensateur mesurable du cycle 0026 possède un
lift compact axisymétrique exact qui conserve divergence, moyenne nulle,
faible-`L^(3/2)`, masse critique et énergie finie. Une variante lisse réalise
le scaling cubique de l'oscillation sur un domaine parent, donc div–curl seul
n'améliore pas l'exposant trois.

Résultat négatif : avec une géométrie séparable à aspect fixé, la fermeture
axiale crée nécessairement ici une région active de direction `e_r`; une
seule boule y impose (14), puis fait diverger le log-BMO sous concentration.
Le résidu stationnaire est également non nul.

Ce résultat ne construit ni solution classique, ni trajectoire de Leray–Hopf,
ni pression dynamique, ni singularité admissible. Il exclut un ansatz, pas un
blow-up général.

Le verrou devient `GAP-NONSEPARABLE-RETURN-FLOW-MASKING` : remplacer le produit
`A(r)chi(z)` par une somme finie de couches où la composante verticale d'un
niveau masque le retour radial du précédent. L'aspect croissant reste une
condition possible mais insuffisante à lui seul; le test doit porter sur le
supremum BMO all-ball, les capacités des régions radialement dominantes, les
normes critiques, l'énergie et le résidu.

## Reproduction

```text
python -B experiments/navier-stokes/axisymmetric-return-flow/axisymmetric_return_flow_audit.py
```

Le script utilise Python 3.13.14 et `fractions.Fraction`, sans grille,
flottant ni graine. Il exécute 1251 contrôles exacts, résidus d'identités nuls.
Empreinte SHA-256 :
`cec8bd74aa0b5b1b9943fbd149fe06c4ca5b045b9a337bdfef2821a18c5d29a9`.

Les trois revues séparées sont conservées avec leurs empreintes : analyse
`f34f3746132775b8593d4544469221d4f6d56059ffae49e6188976395129be9b`,
contre-modèle
`a17ec89145051a6b81acf061e74dcf61bdbb2f6f25c18d31a5b5e32a367e9fc3`
et littérature
`65c3e9d9dd5d00d3e6499f5a971312495c783863945d1a182226d7a8cb1af5b0`.
