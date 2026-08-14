# Cycle 0028 — échappatoire torique log-BMO et effondrement de la vitesse critique

Date de coupure : 2026-08-14.

Statut : dérivation IA interne et certificat d'échelles exact. Aucun énoncé
nouveau de ce rapport n'est un `PAPER_PROOF`.

## Équation et notion de solution figées

Le cadre principal est la branche périodique du problème Clay :

```text
partial_t u+(u dot nabla)u=-nabla p+nu Delta u,
div u=0,
(t,x) in [0,T) x T^3,
nu>0, force=0.
```

La cellule est identifiée à `(-1/2,1/2)^3`. Les objets construits ci-dessous
sont des **données initiales lisses périodiques**, pas des solutions
stationnaires. Pour chaque vorticité lisse, de moyenne nulle et divergence
nulle, la vitesse moyenne nulle est définie exactement par

```text
u_hat(k)=i k cross omega_hat(k)/|k|^2,   k!=0,
u_hat(0)=0.                                             (1)
```

Alors `div u=0` et `curl u=omega`. La pression et l'évolution ne sont pas
calculées dans le certificat fini.

## Actions candidates

| Action | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| fermeture torique mince avec extension log-BMO all-ball | 4 | 5 | 5 | 5 | **19** |
| no-go de capacité pour toute somme tensorielle finie | 5 | 2 | 4 | 5 | 16 |
| évolution pseudo-spectrale du lift non séparable | 3 | 2 | 4 | 3 | 12 |

La première action est retenue. Elle teste si le verrou de masquage est une
conséquence réelle de `div omega=0`, ou un artefact du choix poloïdal
`omega=curl(psi e_theta)` du cycle 0027.

## Construction torique

Dans les coordonnées cylindriques autour de l'axe `e_z`, posons

```text
r=sqrt(x_1^2+x_2^2),
d_n=sqrt((r-R_n)^2+z^2),
R_n=2^-n,
q_n=2^-2n,
h_n=2^-n^2,       n>=4.                                (2)
```

Ainsi `h_n<<q_n<<R_n`, et le tore extérieur de rayon mineur `q_n` reste dans
la cellule et loin de l'axe. Soit `beta` une bosse non négative
`C_c^infinity([0,1/4))`, positive sur `[0,1/16]`. Avec

```text
V_n=R_n h_n^2,
A_n=V_n^(-2/3),
omega_n=A_n beta(d_n^2/h_n^2)e_theta,                  (3)
```

on a exactement

```text
div omega_n=0.                                         (4)
```

En effet, une composante purement azimutale indépendante de `theta` a
divergence `r^-1 partial_theta omega_theta=0`. L'intégration en `theta` donne
aussi

```text
integral_(T^3) omega_n dx=0.                           (5)
```

La formule (1) fournit donc une donnée de vitesse `u_n` lisse, périodique,
solénoïdale et de moyenne nulle. Contrairement au lift du cycle 0027, les
lignes de vorticité se ferment dans la direction azimutale sans créer de
calotte radialement dominante.

## Normes critiques

Le volume du cœur satisfait, avec constantes universelles indépendantes de
`n`,

```text
c V_n<=|supp omega_n|<=C V_n.                          (6)
```

La normalisation (3) donne

```text
||omega_n||_(L^(3/2,infinity))~1,
||omega_n||_(L^(3/2))~1,
||omega_n||_1^3~V_n,
||omega_n||_(6/5)^6~V_n,
||omega_n||_2^6~V_n^-1.                               (7)
```

La vorticité reste donc non dégénérée dans les espaces critiques fort et
faible, tandis que sa masse `L1` s'annule et son enstrophie diverge.

Par (1), Sobolev dual et (7),

```text
||u_n||_2<=C||omega_n||_(6/5)<=C V_n^(1/6).            (8)
```

L'énergie tend vers zéro, ce qui n'est pas en soi un critère critique.

## Extension globale de la direction

Sur le cœur actif, la direction vaut `e_theta`. Elle peut être prolongée vers
`e_z` dans le corridor `h_n<d_n<q_n`. Posons

```text
L_n=log(q_n/h_n)=(n^2-2n)log 2,
s_n(d)=clamp(log(q_n/d)/L_n,0,1).                      (9)
```

Après lissage aux extrémités sans changer les bornes ci-dessous, soit

```text
zeta_n=cos(Theta(s_n))e_z+sin(Theta(s_n))e_theta,      (10)
```

où `Theta(0)=0`, `Theta(1)=pi/2` et `Theta` est constante près des deux
extrémités. Alors `zeta_n=e_theta` sur `supp omega_n`, `zeta_n=e_z` hors du
tore `d_n<q_n`, `|zeta_n|=1`, et le champ est lisse sur le tore périodique.

La boucle `theta -> e_theta` n'est pas un obstacle topologique : elle est
contractile dans `S^2` par l'hémisphère supérieur utilisé en (10).

## Réduction all-ball

Pour

```text
MO_B(f)=average_B |f-f_B|,
[f]_(bmo_log)=sup_(0<rho<1/4) |log rho| MO_(B_rho)(f), (11)
```

les boules sont divisées en quatre régimes. Les coordonnées tubulaires ont des
constantes uniformes car `q_n/R_n<=1/16`.

### 1. Boules `rho<=h_n`

Dans le cœur, seule la rotation azimutale contribue. Aux zones lissées de
(9),

```text
MO_B(zeta_n)<=C[rho/(h_n L_n)+rho/R_n].                (12)
```

Comme `rho |log rho|` croît sur l'intervalle considéré,

```text
|log rho|MO_B<=C[|log h_n|/L_n+h_n|log h_n|/R_n].     (13)
```

### 2. Boules `h_n<=rho<=q_n`

La norme BMO non pondérée de `log d` dans la section transverse bidimensionnelle
est universelle. La troncature et la composition Lipschitz donnent

```text
MO_B(zeta_n)<=C[L_n^-1+rho/R_n].                       (14)
```

D'où

```text
|log rho|MO_B<=C[|log h_n|/L_n
                  +|log q_n|q_n/R_n].                 (15)
```

### 3. Boules `q_n<=rho<=R_n/2`

L'intégrale transverse du défaut `|zeta_n-e_z|` est

```text
<=C(q_n^2/L_n+h_n^2).                                 (16)
```

Un segment de tore dans la boule a longueur `O(rho)`, donc

```text
MO_B(zeta_n)<=C[(q_n/rho)^2/L_n+(h_n/rho)^2].          (17)
```

Le membre pondéré est maximal, à constante près, pour `rho=q_n`.

### 4. Boules `rho>=R_n/2`

L'intégrale totale du défaut est

```text
<=C R_n(q_n^2/L_n+h_n^2),                             (18)
```

et la division par le volume de la boule donne la même décroissance avec un
facteur supplémentaire de sparsité globale.

En unités `log 2`, les quatre régimes sont dominés par

```text
n^2/(n^2-2n)
+2n/(n^2-2n)
+2n(q_n/R_n)
+2n(h_n/q_n)^2
+n(q_n/R_n)^2/(n^2-2n)
+n(h_n/R_n)^2.                                        (19)
```

Le certificat rationnel vérifie que (19) est strictement inférieur à `4`
pour `4<=n<=64` et décroît. Les formules montrent directement la borne pour
tout `n>=4`. Il existe donc une constante universelle `C` telle que

```text
sup_n [zeta_n]_(bmo_log)<=C.                           (20)
```

La constante universelle de (20) n'est pas calculée numériquement : elle
contient les constantes de coordonnées tubulaires et de BMO de `log d`.

## Effondrement de la vitesse critique

La même géométrie qui rend (20) possible détruit la norme critique de vitesse.
On suppose ici `h_n<R_n/8<R_*`, où `R_*` est un rayon d'injectivité fixe de
`T^3`, un profil `beta` fixe borné, `integral omega_n=0` et la normalisation de
moyenne nulle de `u_n`. Le noyau de Biot–Savart périodique est `O(|x|^-2)`
près de l'origine, avec un reste lisse. En découpant selon la distance `d` au
cercle central :

```text
|u_n|<=C A_n h_n,                   d<=h_n,
|u_n|<=C A_n h_n^2/d,               h_n<d<R_n,
|u_n|<=C A_n R_n^2 h_n^2/d^3,       d>=R_n.            (21)
```

La dernière ligne utilise la moyenne vectorielle nulle (5) et le développement
du noyau lointain; sur `R_n<=d<=2R_n`, la borne absolue suffit. L'intégration
dans les volumes `C R_n h_n^2`, tubulaires `C R_n d dd`, puis sphériques
`C d^2 dd` donne

```text
||u_n||_3^3
 <=C[A_n^3 R_n h_n^5+A_n^3 h_n^6]
 <=C[h_n/R_n+(h_n/R_n)^2].                            (22)
```

Ainsi

```text
||u_n||_3 -> 0                                        (23)
```

plus vite que toute puissance de `R_n`. La famille est donc finalement dans
le régime de petites données critiques; elle ne peut être une suite de
profils de blow-up. Le certificat vérifie exactement le facteur principal

```text
h_n/R_n=2^(-n^2+n).                                   (24)
```

## Passe contradictoire

1. **Boule contenant tout le tore.** Elle n'a pas une oscillation d'ordre un :
   le défaut à `e_z` n'occupe qu'un tube de fraction `O((q_n/R_n)^2/L_n)`.
2. **Boule de rayon `q_n`.** La rotation est macroscopique ponctuellement,
   mais l'aire transverse est pondérée par `d dd`; la moyenne du profil
   logarithmique vaut `O(1/L_n)`.
3. **Boule de rayon `h_n`.** Le lissage de (9) coûte
   `|log h_n|/L_n=O(1)`, pas `log(1/h_n)`.
4. **Axe cylindrique.** Le champ vaut `e_z` dans un voisinage de l'axe; aucune
   singularité de `e_theta` n'y subsiste.
5. **Quantité critique.** La vorticité reste critique, mais (22) montre que la
   vitesse ne l'est plus. Omettre Biot–Savart produirait un faux candidat.
6. **Domaine.** Le raccord périodique est exact. Sur `R^3`, la vitesse de
   Biot–Savart a une queue multipolaire et n'est pas automatiquement une donnée
   rapidement décroissante de la formulation Clay entière.
7. **Dynamique.** Aucune croissance temporelle, pression ou norme de résidu
   n'est certifiée par le script. Plus fortement, pour un anneau sans swirl
   unisigné sur `R^3`, la diffusion rend `omega^theta(r,z,t)>0` pour `r>0` à
   temps positif. La direction active redevient alors `e_theta` arbitrairement
   près de l'axe. Sur toute boule axiale, sa moyenne vectorielle est nulle et
   son oscillation moyenne vaut exactement un : le log-BMO global diverge.
   Le corridor statique à zéros n'est donc pas propagé par cette dynamique.
   Une coupure localisée à distance fixe de l'axe n'a pas cette obstruction,
   mais elle ne fournit aucun critère global.

## Lemme collatéral sur le retour poloidal

La passe analytique isole aussi ce qui reste sauvable de la somme tensorielle.
Pour un champ poloidal axisymétrique `W`, de quasi-norme faible-`L^(3/2)` `K`,
posons `E={|W_r|>=|W|/4}` et

```text
Delta_Omega=integral_(Omega*) |W_r|
            -(1/sqrt(15)) integral_(Omega*) |W_z|.
```

Alors

```text
|E intersection Omega*|>=((Delta_Omega)_+/(3K))^3,
Cap_2(E intersection Omega*)>=(Delta_Omega)_+/(3 S_3^2 K).       (26)
```

La preuve combine `|W_r|<|W_z|/sqrt(15)` hors de `E`, l'inégalité de Lorentz
`integral_E |W|<=3K|E|^(1/3)` et Sobolev. Le rang fini d'une décomposition ne
force toutefois pas `Delta_Omega>0`; (26) ne ferme donc pas le masquage
non séparable sans un excès radial uniforme.

## Verdict

Le besoin d'une hiérarchie non séparable n'est pas une conséquence universelle
de `div omega=0` : une fermeture azimutale très mince évite toute composante
radiale et admet une extension globale unitaire uniformément log-BMO. Elle
réfute donc un no-go purement topologique ou fondé sur la seule capacité des
virages.

Mais cette échappatoire paie exactement par

```text
||u_n||_3^3<=C K_n^3 h_n/R_n,                         (25)
```

où `K_n~||omega_n||_(L^(3/2,infinity))`. Le verrou à plus fort levier devient
`GAP-CRITICAL-VELOCITY-NONDEGENERACY` : produire ou exclure une famille avec
simultanément `K_n=O(1)`, direction log-BMO uniforme et
`liminf ||u_n||_3>0`.

La somme tensorielle non séparable reste ouverte, mais elle doit désormais
être testée avec cette condition critique de vitesse. Cacher le dernier retour
dans une capacité superpolynomiale sans suivre Biot–Savart ne constitue plus
un progrès suffisant.

## Reproduction

```text
python -B experiments/navier-stokes/toroidal-log-bmo/toroidal_log_bmo_audit.py
```

Le script utilise uniquement `fractions.Fraction`, aucune grille, aucun
flottant et aucune graine. Il contrôle les identités d'échelle, les six termes
de l'enveloppe (19), la criticité et la décroissance (24). Les constantes
géométriques de la réduction all-ball et l'estimation du noyau (21) restent
des lemmes analytiques, non des sorties d'arithmétique d'intervalle.

Audits contradictoires conservés :

- analyse PDE, excès radial et Biot–Savart :
  `0a72c41226785dc5d32e9f153bd257797484de65f9219be3c8543ae5d3fc4be0`;
- contre-modèle et estimation indépendante :
  `76c911877b5a127c021623be5a4851ed44de8b876d68c6c416bd7ecec3fcb2c5`;
- veille primaire et obstruction dynamique :
  `3559f06919e531b10ebf4ab3e1878789ec8aecacc83024f0db2e7ecfacb54a68`.

Ces passes utilisent des instances Codex séparées, mais ne constituent pas une
revue externe indépendante.
