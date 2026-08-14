# Cycle 0033 — gate directionnel des sections bornées

Date de gel : 2026-08-14.

Statut : dérivation analytique interne et certificat algébrique exact. Le
résultat reste `COMPUTATION_ONLY`; il ne constitue ni une preuve publiée, ni
une évolution de Navier–Stokes, ni une résolution du problème Clay.

## Décision adaptative

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| troncature presque optimale puis compensation conique sur une section de diamètre `O(R)` | 5 | 5 | 5 | 5 | **20** |
| obstruction topologique universelle par degré du gradient sans diamètre | 5 | 2 | 4 | 5 | 16 |
| optimisation numérique directe du BMO all-ball de plateaux | 4 | 3 | 4 | 3 | 14 |

La première action est retenue. Elle évite de supposer une régularité de la
Gauss map ou une borne de Hessienne : le niveau tronqué fournit lui-même la
masse conique, et le claim `NS-LORENTZ-CONE-COMPENSATION` transforme cette
masse en oscillation non pondérée sur une vraie boule tridimensionnelle.

## Équation et type d'objet

Le cadre Clay de référence est

```text
partial_t u+(u·nabla)u=-nabla p+nu Delta u,
div u=0,  nu>0,  f=0,
```

sur `R3` ou `T3`. Le cycle travaille seulement sur `R3`, à temps fixé. Soient
`R>0`, `z_0 in R`, `Lambda>=1` et

```text
F in C_c^infinity((0,infinity)×R),
supp F subset {R/2<r<3R/2, |z-z_0|<Lambda R}.
```

Posons

```text
U=(R/r)F(r,z)e_theta,
W=curl U=(R/r)(-partial_z F e_r+partial_r F e_z).       (1)
```

Alors `U` est lisse, compact et exactement divergence-free. Le facteur `R/r`
annule la courbure dans le curl. Écrivons

```text
K_u=||U||_(L^(3,infinity)(R3)),
K_w=||W||_(L^(3/2,infinity)(R3)).                        (2)
```

L'objet est une donnée initiale admissible, pas une solution stationnaire ni
une trajectoire.

## Lemme actif

Soit

```text
xi=W/|W|  sur {W!=0}.
```

Une extension est toute fonction `zeta in L1(B;R3)` qui coïncide presque
partout avec `xi` sur `{W!=0} intersection B`. Aucune valeur unitaire n'est
exigée sur les zéros.

### Théorème 1 — gate directionnel de diamètre borné

Il existe une boule

```text
B=B((0,0,z_0), C_Lambda R)                               (3)
```

contenant le support de `W`, et une constante `c_Lambda>0`, telles que toute
extension `zeta` vérifie, dès que `K_u>0`,

```text
boxed{
MO_B(zeta)>=c_Lambda (K_u/K_w)^6.}                       (4)
```

Ici

```text
MO_B(zeta)=|B|^-1 integral_B |zeta-zeta_B| dx.           (5)
```

On peut suivre la dépendance géométrique sous la forme
`c_Lambda=c(9/4+Lambda^2)^(-3/2)`. Elle dépend en outre seulement des
constantes dimensionnelles et de la convention de quasi-norme faible, mais ni
de `F`, ni de ses signes, plateaux, composantes, annulations internes ou
échelles de transition.

Sous les gates `K_u>=kappa>0`, `K_w<=K`, on obtient donc

```text
MO_B(zeta)>=c_Lambda (kappa/K)^6.                        (6)
```

## Preuve

### 1. Réduction plane exacte

Posons

```text
K_f=||F||_(L^(3,infinity)(dr dz)),
K_g=||nabla F||_(L^(3/2,infinity)(dr dz)).               (7)
```

Les comparaisons cylindriques du cycle 0032 donnent

```text
K_f>=c R^(-1/3) K_u,
K_g<=C R^(-2/3) K_w.                                     (8)
```

Le sens de la seconde inégalité est essentiel : la norme plane du gradient
doit être contrôlée par la norme tridimensionnelle du curl.

### 2. Troncature d'un niveau presque optimal

Choisissons `lambda>0` tel que

```text
lambda^3 |{|F|>lambda}| >= (1/2) K_f^3.                 (9)
```

Un signe `sigma in {+1,-1}` satisfait, avec

```text
A={sigma F>lambda},
lambda |A|^(1/3)>=c K_f.                                (10)
```

Définissons la troncature lipschitzienne compacte

```text
G=(sigma F-lambda/2)_+.                                 (11)
```

Sur `A`, `G>=lambda/2`, et

```text
||nabla G||_(L^(3/2,infinity))<=K_g.                    (12)
```

Le weak HLS bidimensionnel déjà audité donne

```text
||G||_(L^(6,infinity))<=C_H K_g.                        (13)
```

Comme `G>=lambda/2` sur `A`,

```text
(lambda/2)|A|^(1/6)<=C_H K_g.                           (14)
```

La combinaison de (10) et (14) fixe une aire active minimale :

```text
|A|^(1/6)>=c K_f/K_g.                                   (15)
```

Cette étape empêche une pointe de niveau presque optimal d'avoir une aire
arbitrairement petite sous les deux gates.

### 3. Coaire et variation totale

Pour `0<t<lambda/2`, l'ensemble `{G>t}` contient `A`. L'inégalité
isopérimétrique plane et la coaire donnent

```text
integral |nabla G| dr dz
 >= integral_0^(lambda/2) Per({G>t}) dt
 >= c lambda |A|^(1/2).                                 (16)
```

En réutilisant (10) et (15),

```text
boxed{
integral |nabla G| dr dz >= c K_f^2/K_g.}               (17)
```

Il s'agit de la variation de la somme tronquée réelle, jamais de la somme des
variations de couches.

### 4. Curl tronqué et annulation vectorielle

Construisons

```text
U_G=(R/r)G e_theta,
W_G=curl U_G=(R/r)nabla_perp G.                          (18)
```

Alors

```text
W_G=sigma 1_{sigma F>lambda/2} W                         (19)
```

presque partout, donc

```text
||W_G||_(L^(3/2,infinity))<=K_w.                        (20)
```

Le jacobien cylindrique donne exactement

```text
M:=integral |W_G| dx
 =2pi R integral |nabla G| dr dz
 >=c R K_f^2/K_g.                                       (21)
```

De plus,

```text
integral W_G dx=0.                                      (22)
```

Cette identité est celle du curl d'un champ compact; elle se vérifie aussi
directement : la composante radiale s'annule par intégration azimutale et la
composante verticale par `integral partial_r G dr dz=0`. La régularité
lipschitzienne de `G` suffit, ou peut être obtenue par approximation.

### 5. Sélection d'un cône et vraie boule BMO

Une famille finie de calottes orientées d'ouverture fixe couvre
`S2`. Il existe donc `e in S2` et `alpha>0` universel tels que

```text
m=integral_{W_G/|W_G| dot e>=alpha}|W_G| dx >= c M.     (23)
```

La boule (3), avec par exemple
`C_Lambda>sqrt(9/4+Lambda^2)`, contient le support de `W_G` et vérifie

```text
|B|<=C_Lambda R^3.                                      (24)
```

La fonction `sigma zeta` est une extension de la direction de `W_G`. Le claim
`NS-LORENTZ-CONE-COMPENSATION`, appliqué sur cette boule avec (20), (22) et
(23), donne

```text
MO_B(zeta)=MO_B(sigma zeta)
 >=c m^3/(K_w^3 |B|)
 >=c_Lambda K_f^6/(K_g^3 K_w^3).                        (25)
```

Enfin, (8) transforme exactement le dernier quotient en

```text
K_f^6/(K_g^3 K_w^3)>=c(K_u/K_w)^6,                     (26)
```

ce qui prouve (4).

## Échelle et conséquence log-BMO

Sous

```text
U_mu(x)=mu U(mu x),
W_mu(x)=mu^2 W(mu x),
R_mu=R/mu,
```

les deux endpoints et le rapport `K_u/K_w` sont invariants. La boule (3) se
redimensionne comme `R`; (4) est donc critique.

Pour une famille `R_n->0`, `K_(u,n)>=kappa` et `K_(w,n)<=K`, toute extension
vérifie, pour `n` assez grand,

```text
sup_{rho(B)<1/2}|log rho(B)| MO_B(zeta_n)
 >=c_Lambda (kappa/K)^6 |log(C_Lambda R_n)|
 ->infinity.                                            (27)
```

Ainsi aucune famille pure-swirl de diamètre axial `O(R_n)` ne satisfait le
gate directionnel log-BMO uniforme utilisé dans le scénario conditionnel
récent, même si sa section est épaisse et ses couches non séparables.

## Expérience adverse exacte

Le certificat `BOUNDED-CROSS-SECTION-DIRECTION-GATE-1` audite quatre attaques.

1. **Algèbre cylindrique.** Sur 32 échelles et 12 paires de cubes de normes,
   il vérifie exactement

   ```text
   K_f^6/(K_g^3 K_w^3)=(K_u^3/K_w^3)^2.                 (28)
   ```

2. **Plateau à coque mince.** Avec rayon extérieur `L=R/8` et épaisseur
   `delta`, les proxies exacts sont

   ```text
   K_w^3/K_u^3=R/delta,
   fraction_directionnelle=delta/L.                    (29)
   ```

   Sous normalisation `K_w^3=1`, `K_u^3=delta/R`; cacher la rotation dans une
   coque mince détruit le gate vitesse.

3. **Retour antipodal rare.** Une phase principale de volume `1-epsilon` et
   son compensateur de volume `epsilon` ont

   ```text
   K_w^3=(1-epsilon)^3/epsilon,
   MO=4epsilon(1-epsilon).                              (30)
   ```

   Leur produit reste `4(1-epsilon)^4`; le faible BMO se paie exactement à
   l'endpoint faible.

4. **Cellules axialement séparées.** Pour `N` cellules identiques,

   ```text
   K_w^3/K_u^3=N.                                       (31)
   ```

   Pour des amplitudes décroissant dyadiquement, les deux quasi-normes sont
   dominées par la première cellule : la séparation seule ne supprime pas un
   bloc local dominant.

Le script exécute 2 884 contrôles rationnels exacts, sans flottant ni graine.
Empreinte SHA-256 :
`4759238f59a46f64f0a547881f8aeb86ca6755ceea06c4a1728648db57847f8f`.

## Veille différentielle et revues séparées

Hopf (`NS-SRC-0136`), Amann (`0137`), Brezis–Nirenberg Part II (`0138`) et
Whitney (`0139`) permettent une autre obstruction : un extremum critique
isolé de `F` donne une direction de gradient de degré non nul, donc non-VMO et
de log-BMO infini. Cette route reste qualitative. Elle ne minore ni une masse
locale de `|W|`, ni le rayon d'une boule mauvaise, ni une constante fonction
de `K_u/K_w`; elle ne source donc pas (4).

Trois passes séparées ont ensuite été intégrées :

- l'audit analytique valide la chaîne niveau–HLS–coaire–cône et corrige la
  dépendance de la vraie boule en
  `(Lambda^2+9/4)^(-3/2)`, distincte du facteur `Lambda^-1` obtenu sur le
  domaine annulaire non sphérique; empreinte
  `10e91d1b91397265a18e4a2553c965aa90ae2d64e6d0b9ccf05e827ac1d81de7`;
- l'audit bibliographique établit la portée et la limite des outils de degré;
  empreinte
  `815b464657e02981d2b56be538ad875647e0a2b7659dca1ba0fe8c37fd23a97d`;
- le contre-profil torique réfute une minoration fondée uniquement sur deux
  directions antipodales, mais confirme le coût endpoint d'un retour rare;
  empreinte
  `885ae99a2382b228d910507c6fd92d7f33d0382887ac601cbbc2a2f76bfdf9f1`.

Ces revues sont produites par des agents IA du même environnement. Elles sont
contradictoires et reproductibles, mais ne constituent ni une revue humaine
externe ni une validation indépendante au sens éditorial.

## Passe contradictoire

1. **Signe silencieux.** Le superniveau de `|F|` est scindé avant troncature;
   `G` reste non négative et `W_G=sigma W` sur son support actif.
2. **Supremum faible non atteint.** Le facteur `1/2` dans (9) évite toute
   hypothèse d'atteinte exacte.
3. **Pointe de mesure nulle.** (13)--(15) imposent une aire active; une grande
   amplitude sur un ensemble arbitrairement petit ferait croître `K_g`.
4. **Coaire des couches.** (16) porte sur `G`, donc sur la somme finale après
   toutes les annulations.
5. **Troncature non lisse.** La formule de chaîne Sobolev, l'approximation
   lipschitzienne et l'identité directe (22) suffisent; aucun défaut de bord
   n'est omis.
6. **Direction inversée.** Pour `sigma=-1`, on applique le lemme à
   `sigma zeta`; la moyenne d'oscillation est inchangée.
7. **Domaine arbitraire pris pour une boule.** Le support axial borné fournit
   explicitement la boule (3), de volume `O_Lambda(R^3)`.
8. **Queue de support artificielle.** La preuve utilise un superniveau presque
   optimal, pas l'aire du support topologique; une queue infinitésimale ne
   change pas le résultat.
9. **Composantes multiples.** Elles sont couvertes si leur union reste dans la
   même tranche axiale `O(R)`. Une dispersion de diamètre bien plus grand que
   `R` n'est pas couverte.
10. **Degré topologique.** Aucun degré, contrôle de courbure ou Hessienne n'est
    invoqué; la conclusion vient de la masse conique et de l'annulation du curl.
11. **PDE.** La pression, la projection de Leray en temps, le stretching et la
    diffusion ne sont pas calculés.
12. **Clay.** Exclure cette classe de profils ne prouve ni régularité globale,
    ni absence de tout blow-up, ni construction d'une singularité admissible.

## Résultat scientifique et pivot

Le résultat positif borné est (4) : les deux endpoints critiques forcent une
oscillation directionnelle quantitative sur une vraie boule pour toute
section pure-swirl de diamètre axial `O(R)`. Les plateaux épais, retours rares
et superpositions non séparables de diamètre borné sont donc fermés ensemble.

Le résultat négatif méthodologique est que le seul degré de la Gauss map n'est
pas nécessaire et n'aurait pas contrôlé les volumes. Le premier trou réel est
la perte du volume de la boule lorsque des composantes actives sont séparées
sur une distance `L_n/R_n->infinity`.

Le verrou devient `GAP-AXIALLY-DISPERSED-PURE-SWIRL-SELECTION`. Le prochain
lemme doit sélectionner, parmi des cellules hétérogènes, une composante dont
le rapport local endpoint reste non dégénéré, ou construire une distribution
sans cellule dominante qui réfute cette sélection.

## Reproduction

```text
python -B experiments/navier-stokes/bounded-cross-section-direction/bounded_cross_section_direction_audit.py
```

Le calcul exact ne certifie ni les constantes HLS/coaire/conique, ni un
supremum BMO continu, ni le passage à l'évolution.
