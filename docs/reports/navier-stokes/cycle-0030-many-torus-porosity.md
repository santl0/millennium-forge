# Cycle 0030 — cardinal croissant et porosité tubulaire

Date de gel : 2026-08-14.

Statut : dérivation analytique interne et audit rationnel exact. Aucun calcul
d'évolution, aucune preuve de singularité et aucune certification du continuum
par arithmétique d'intervalles.

## Décision adaptative

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| borne Biot–Savart poreuse pour `N_n->infinity` | 5 | 5 | 5 | 5 | **20** |
| vitesse compacte divergence-free construite en amont | 5 | 4 | 5 | 5 | 19 |
| simulation pseudospectrale d'un réseau cohérent | 4 | 2 | 4 | 4 | 14 |

Le verrou `GAP-MANY-TORUS-CRITICAL-ACCUMULATION` est sélectionné. Le lemme
actif demande si le nombre croissant de composantes peut compenser la petite
vitesse de chaque tube lorsque les corridors log-BMO restent disjoints.

## Équation et type d'objet

Le cadre Clay de référence est

```text
partial_t u+(u·nabla)u=-nabla p+nu Delta u,
div u=0,
nu>0,
f=0,
```

sur `R^3` ou `T^3`. Le cycle construit seulement des vorticités initiales
lisses et leur vitesse instantanée de Biot–Savart. Sur `R^3`, la reconstruction
est la solution décroissante de `curl u=W`, `div u=0`; sur `T^3`, elle est la
solution périodique de moyenne nulle. Aucune notion de solution faible ou
forte en temps n'est utilisée dans le lemme.

La preuve de noyau ci-dessous est formulée sur `R^3`. Sur un tore unité, le
noyau périodique est le noyau entier plus un reste lisse sur la cellule; ce
reste ajoute au cube de la norme au plus `C K^3S`. Il tend aussi vers zéro dans
la famille explicite, mais n'est pas omis dans le raccord périodique.

## Classe tubulaire exacte

Soient des courbes fermées lisses `Gamma_j`, de longueurs `L_j`, avec rayon de
reach au moins `8q`. On suppose leurs tubes `T_(4q)(Gamma_j)` disjoints. Pour
un profil transverse fixe `b`, supporté dans le disque unité, posons

```text
W=A sum_(j=1)^N sigma_j b(d_j/h) tau_j,
0<h<q/8,
sigma_j in {-1,+1}.                                  (1)
```

Ici `tau_j` est le champ tangent. Pour la réalisation exacte utilisée plus
bas, les `Gamma_j` sont des cercles coaxiaux, `tau_j=e_theta`, et chaque terme
de (1) est divergence-free. Les signes n'interviennent pas dans la majoration.

Notons

```text
mathcal L=sum_j L_j,
S=|support W|~mathcal L h^2,
K=||W||_(L^(3/2,infinity))^*~A S^(2/3).              (2)
```

Les constantes de `~` dépendent seulement du profil et de la géométrie
tubulaire uniforme. Les quantités `K`, `||u||_3`, `h/mathcal L` et `h/q` sont
invariantes sous le scaling Navier–Stokes.

## Hypothèse de packing local

La disjonction des tubes `q` et le contrôle de reach donnent, pour toute boule
`B_r(x)` avec `r>=q`,

```text
sum_j length(Gamma_j intersection B_r(x))
 <=C r^3/q^2.                                        (3)
```

En épaississant seulement à l'échelle `h`, (3) implique

```text
|support W intersection B_r(x)|
 <=C (h/q)^2 r^3.                                    (4)
```

La localité de (3) est essentielle. Un seul budget global de volume ne permet
pas la borne lointaine ci-dessous.

## Décomposition locale de Biot–Savart

Écrivons le noyau `K_BS(z)=O(|z|^-2)` et séparons les sources à distance
inférieure ou supérieure à `q/2` du point d'observation.

Dans le voisinage d'un tube, la contribution locale satisfait

```text
|u_loc(x)|<=C A h,               d<=2h,
|u_loc(x)|<=C A h^2/d,           2h<d<q.             (5)
```

Les voisinages de sortie ont multiplicité bornée. En coordonnées tubulaires,

```text
||u_loc||_3^3
 <=C A^3 mathcal L
   [h^3 h^2+integral_h^q (h^2/d)^3 d dd]
 <=C A^3 mathcal L h^5.                              (6)
```

Comme `K^3~A^3 mathcal L^2h^4`,

```text
||u_loc||_3^3<=C K^3 h/mathcal L.                    (7)
```

Cette formule retrouve `h/R` pour un seul anneau et `h/(NR)` pour `N`
anneaux comparables. Elle ne suppose aucune annulation mutuelle des vitesses.

## Partie lointaine : Morrey, Hedberg et HLS

Posons `mu=|W|dx`, `M=mu(R^3)<=CAS`, et

```text
D=C A(h/q)^2.                                        (8)
```

Pour la partie tronquée à `q/2`, (4) donne
`mu(B_r(x))<=D r^3`. L'intégration en couches, avec le rayon de transition
`r_0=(M/D)^(1/3)`, fournit l'inégalité de Hedberg élémentaire

```text
||u_far||_infinity
 <=C D^(2/3) M^(1/3).                                (9)
```

Par Hardy–Littlewood–Sobolev,

```text
||u_far||_2^2
 <=C ||W||_(6/5)^2
 <=C A^2 S^(5/3).                                   (10)
```

L'interpolation `||v||_3^3<=||v||_2^2||v||_infinity` donne

```text
||u_far||_3^3
 <=C A^3S^2(h/q)^(4/3)
 <=C K^3(h/q)^(4/3).                                (11)
```

Le calcul utilise `|W|`; il reste valable si les champs lointains sont
parfaitement alignés. Les signes et les corrections de moments ne peuvent
donc pas l'invalider.

## Lemme de collapse poreux

En combinant les deux morceaux et `(a+b)^3<=4(a^3+b^3)`, on obtient

```text
boxed{
||BS[W]||_3^3
 <=C K^3 [h/mathcal L+(h/q)^(4/3)].}                 (12)
```

Sur `T^3`, le membre droit devient
`C K^3[h/mathcal L+(h/q)^(4/3)+S]` dans une cellule unité.

Ainsi, pour toute famille telle que

```text
K_n<=K_*,
h_n/mathcal L_n->0,
h_n/q_n->0,                                         (13)
```

la vitesse critique tend vers zéro, même si `N_n->infinity`. Un corridor de
profondeur logarithmique
`log(q_n/h_n)>=c|log ell_n|` implique précisément le second passage à zéro.

La conclusion couvre des signes arbitraires et tout nombre de moments annulés,
mais seulement des rayons `h,q` communs et un packing local uniforme.

## Famille adverse à cardinal explosif

Pour montrer que (12) n'est pas une reformulation de l'inégalité triangulaire,
prenons

```text
ell_n=2^(-3n),
q_n=2^(-9n),
h_n=2^(-12n),
M_n=2^(6n-6),
N_n=M_n^2=2^(12n-12).                               (14)
```

Dans le plan méridien, plaçons les centres de `M_n^2` cercles coaxiaux sur une
grille de pas `8q_n`, avec rayons comparables à `ell_n`. La grille occupe
exactement `ell_n/8` dans chacune des deux directions et les corridors sont
disjoints. À constantes géométriques fixes,

```text
mathcal L_n~N_n ell_n,
mathcal L_n q_n^2/ell_n^3=2^-12,
mathcal L_n h_n^2/ell_n^3=2^(-6n-12).                (15)
```

La profondeur du corridor est exactement

```text
log_2(q_n/h_n)=3n=|log_2 ell_n|.                     (16)
```

Après normalisation `A_n^3S_n^2=1`, l'estimation composante par composante
autoriserait faussement

```text
N_n h_n/ell_n=2^(3n-12)->infinity.                   (17)
```

La borne poreuse donne au contraire

```text
||u_n||_3^3
 <=C[2^(-21n+12)+2^(-4n)+S_n]
 ->0.                                                (18)
```

Le premier terme est local; le second vient de toute addition cohérente
possible au-delà de `q_n`. Cette famille est donc un test adverse décisif de
la borne triangulaire.

## Direction log-BMO statique

Tous les cercles coaxiaux de même signe portent `e_theta`. Dans chaque
corridor, on tourne logarithmiquement de `e_theta` vers le fond `e_z`. Les
estimations locales du cycle 0028 coûtent

```text
|log h_n|/log(q_n/h_n)=4.                            (19)
```

À l'échelle parente, les corridors occupent une fraction `2^-12`, mais la
déviation moyenne de chaque profil logarithmique gagne un facteur
`1/log(q_n/h_n)`. Le poids `|log ell_n|` se compense. Les boules intermédiaires
sont contrôlées par (3) et la même moyenne radiale. La réduction donne une
enveloppe all-ball uniforme à constantes tubulaires universelles. Le script
n'en certifie que les puissances dyadiques : les constantes géométriques de
cette enveloppe restent une dérivation analytique interne, non une preuve
assistée par ordinateur.

Cette extension est statique et la réalisation coaxiale reste axisymétrique
sans swirl, donc globalement régulière. Le lemme (12), lui, ne dépend ni de ce
théorème de régularité ni du signe.

## Passe contradictoire

1. **Triangle contre cohérence.** (17) diverge; il ne mesure pas la norme de
   la somme. La partie lointaine est auditée collectivement par (9)–(11).
2. **Packing global contre local.** Remplacer (3) par
   `mathcal L q^2<=Cell^3` seulement laisse possible une sous-concentration;
   le lemme exige le contrôle dans chaque boule.
3. **Endpoint faible.** HLS seul depuis faible-`L^(3/2)` donne seulement
   faible-`L^3`. La preuve emploie séparément `L^(6/5)`, le Morrey effectif et
   l'interpolation; aucun endpoint fort n'est supposé.
4. **Moments et signes.** Ils peuvent réduire `u_far`, jamais dépasser la
   majoration obtenue avec `|W|`.
5. **Hétérogénéité.** Des `h_j/q_j` et amplitudes variant sur une cascade ne
   sont pas couverts par (12). Les sommer sans ledger Carleson serait abusif.
6. **BMO.** Le script vérifie les échelles, pas les constantes de Poincaré ou
   la géométrie de toutes les boules.
7. **Clay.** La donnée entière n'est pas automatiquement de Schwartz et aucune
   dynamique n'est construite. Sur le tore, la donnée est lisse mais petite en
   `L^3`, sans singularité candidate.

## Trois stratégies fermées et pivot

Le même verrou de non-dégénérescence critique a maintenant subi trois attaques
réellement différentes :

1. un tore unique à corridor logarithmique — cycle 0028;
2. une paire ou un cardinal fixé avec moments corrigés — cycle 0029;
3. un cardinal croissant, égal-échelle et localement packé — cycle 0030.

Toutes donnent `||u_n||_3->0`. Conformément au protocole, la branche des tubes
azimutaux disjoints à paramètres uniformes est abandonnée.

### Test adverse immédiat du pivot « vitesse compacte »

La seule non-petitesse de la norme forte `L^3` ne constitue pas un gate. Fixons
un champ non nul `u_0 in C_c^infinity(B_1)^3`, divergence-free, et
`omega_0=curl u_0`. Pour

```text
c_j=2^(-j)e_1,  r_j=2^(-j^2-10),  a_N=N^(-1/3),
u_(j,N)(x)=a_N r_j^(-1)u_0((x-c_j)/r_j),
U_N=sum_(j=1)^N u_(j,N),  W_N=curl U_N,                 (20)
```

les supports sont disjoints et l'identité de Hodge donne exactement
`BS[W_N]=U_N`. La distribution super-géométrique des rayons implique

```text
||U_N||_3^3=||u_0||_3^3,
||W_N||_(L^(3/2,infinity))^*<=C N^(-1/3),
||U_N||_(L^(3,infinity))^*<=C N^(-1/3),
||U_N||_2^2<=C N^(-2/3).                              (21)
```

Ainsi, (20) réfute toute inégalité forte universelle
`||BS[W]||_3<=C||W||_(L^(3/2,infinity))` et réfute le gate « vitesse compacte,
vorticité faible critique bornée, `L^3` fort non nul ». Pour `N` grand, la
petitesse faible-`L^3` place ces données de Clay lisses et compactes dans le
régime global perturbatif de Yamazaki. Sans le facteur `a_N`, la même famille
garde ses deux quasi-normes faibles critiques uniformément d'ordre un et
vérifie `||U_N||_3^3=N||u_0||_3^3`; le seul gate fonctionnel faible est donc
lui aussi insuffisant. Enfin, si le bloc de base possède une
boule active d'oscillation directionnelle `c_0>0`, sa copie à l'échelle `r_j`
coûte `c_0|log r_j|` dans le log-BMO; la concentration ne résout donc pas le
return-flow interne.

Le verrou actif est affiné en
`GAP-COMPACT-VELOCITY-WEAK-CRITICAL-DIRECTION` : construire ou exclure une
famille `U_N in C_c^infinity`, divergence-free, telle que la norme
`L^(3,infinity)` ne tombe pas dans le régime de petite donnée, que
`curl U_N` reste bornée dans `L^(3/2,infinity)`, et surtout que la direction
active admette une extension log-BMO uniforme. Un temps d'interaction
indépendant de la plus petite échelle sera exigé avant tout raccord dynamique.

Le test d'abandon sera l'une des trois pertes quantitatives : petite donnée
faible-`L^3`, oscillation interne `|log r_N|`, ou temps diffusif
`r_N^2/nu->0`. Une cascade tubulaire hétérogène reste enregistrée, mais reçoit
une priorité inférieure tant qu'elle n'a pas de ledger Carleson précis.

## Reproduction

```text
python -B experiments/navier-stokes/many-torus-porosity/many_torus_porosity_audit.py
```

Le script utilise seulement `fractions.Fraction`, sans grille numérique,
flottant ni graine. Il vérifie packing, fraction active, normalisation critique,
profondeur logarithmique, divergence de la borne triangulaire et collapse de
(18). Les lemmes tubulaires, Morrey–Hedberg, HLS et all-ball restent
analytiques.
