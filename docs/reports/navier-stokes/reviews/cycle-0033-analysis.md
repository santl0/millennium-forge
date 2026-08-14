# Cycle 0033 — troncature active, compensation conique et verrou de localisation en boule

Date : 2026-08-14
Statut : dérivation analytique IA interne, non revue par les pairs, **pas** `PAPER_PROOF`
Verrou : `GAP-NONSEPARABLE-COMPACT-CURL-FLATNESS`

## Décision du cycle

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Effet de levier | Total |
|---|---:|---:|---:|---:|---:|
| Tronquer un niveau presque optimal, rétablir `∫curl=0`, puis appliquer la compensation conique | 4 | 5 | 5 | 5 | **19** |
| Déduire directement une boule par coaire et isopérimétrie composante par composante | 5 | 2 | 4 | 5 | 16 |
| Tester la dispersion axiale et les satellites de faible amplitude contre le passage domaine→boule | 3 | 5 | 5 | 4 | 17 |

La première action est sélectionnée. Elle produit un lemme conditionnel de boule avec une constante explicite et isole un unique résidu géométrique : le rapport de remplissage d'un superniveau du curl tronqué dans une boule contenant sa compensation. La troisième action réfute deux raccourcis possibles, sans fournir de contre-exemple au lemme existentiel final.

## 1. Cadre exact

Dans le plan méridien, soit

\[
 F\in C_c^\infty((0,\infty)\times\mathbb R),
 \qquad
 \operatorname{supp}F
 \subset\{(r,z):R/2<r<3R/2,
                    \ |z-z_0|<\Lambda R\},
 \qquad \Lambda>0.
\tag{1}
\]

Dans `R³`, posons

\[
 U=\frac RrF(r,z)e_\theta,
 \qquad
 W=\nabla\times U
 =-\frac RrF_z e_r+\frac RrF_r e_z.
\tag{2}
\]

Le champ `U` est lisse, compact et exactement divergence-free. On suppose les deux gates

\[
 K_u:=\|U\|_{L^{3,\infty}(\mathbb R^3)}\geq\kappa>0,
 \qquad
 K_\omega:=\|W\|_{L^{3/2,\infty}(\mathbb R^3)}\leq K<\infty.
\tag{3}
\]

On abrège

\[
 q=\frac\kappa K\leq C,
\tag{4}
\]

la borne supérieure universelle provenant du raccord de Biot–Savart. Le problème du cycle est de déduire de (1)–(3) une boule `B` de rayon au plus `R` fois un polynôme en `q⁻¹`, telle que toute extension bornée `ζ` de

\[
 \xi=\frac W{|W|}\quad\text{sur }\{W\ne0\}
\tag{5}
\]

vérifie `MO_B(ζ)≥c q^p` pour un exposant universel fini `p`.

Il s'agit uniquement d'un énoncé cinématique à temps fixé. Aucun terme de Navier–Stokes, aucune pression et aucune évolution ne sont présents.

## 2. Comparaison cylindrique utilisée

Pour une fonction méridienne `f` supportée dans la couronne (1), son relèvement `(R/r)f` vérifie

\[
 \frac23(\pi R)^{1/p}
 \|f\|_{L^{p,\infty}(\mathbb R^2)}
 \leq
 \left\|\frac Rrf\right\|_{L^{p,\infty}(\mathbb R^3)}
 \leq
 2(3\pi R)^{1/p}
 \|f\|_{L^{p,\infty}(\mathbb R^2)}.
\tag{6}
\]

Les sens sont importants : la borne supérieure avec `p=3` extrait un niveau de `F` depuis `K_u`; la borne inférieure avec `p=3/2` contrôle le gradient méridien par le curl tridimensionnel.

## 3. Troncature signée d'un niveau de vitesse

### Lemme 3.1 — extraction d'un paquet compact non dégénéré

Il existe un signe `ε₀∈{−1,+1}`, un niveau `t>0` et

\[
 G=(\varepsilon_0F-t)_+
\tag{7}
\]

tels que, en posant

\[
 U_G=\frac RrG e_\theta,
 \qquad W_G=\nabla\times U_G,
\tag{8}
\]

on ait

\[
 \|U_G\|_{L^{3,\infty}}
 \geq c_T\kappa,
 \qquad
 0<c_T<6^{-4/3},
\tag{9}
\]

\[
 |W_G|\leq|W|\quad\text{p.p.},
 \qquad
 \|W_G\|_{L^{3/2,\infty}}\leq K,
\tag{10}
\]

et

\[
 \int_{\mathbb R^3}W_G\,dx=0.
\tag{11}
\]

De plus, sur `{W_G≠0}`,

\[
 \frac{W_G}{|W_G|}=\varepsilon_0\xi.
\tag{12}
\]

### Preuve

Par la borne supérieure de (6),

\[
 \|F\|_{L^{3,\infty}(\mathbb R^2)}
 \geq\frac{\kappa}{2(3\pi R)^{1/3}}.
\tag{13}
\]

Choisissons `s>0` presque optimal pour cette quasi-norme. L'un des ensembles `{F>s}` ou `{F<−s}` contient au moins la moitié de `{|F|>s}`. Prenons le signe correspondant et `t=s/2`. Sur cet ensemble, `G>s/2`; par conséquent,

\[
 \|G\|_{L^{3,\infty}(\mathbb R^2)}
 \geq2^{-4/3}(1-o(1))
 \|F\|_{L^{3,\infty}(\mathbb R^2)}.
\tag{14}
\]

La borne inférieure de (6), puis (13), donne (9), avec toute constante strictement inférieure à `6⁻⁴ᐟ³` en absorbant le défaut `o(1)` du supremum.

La règle de chaîne lipschitzienne donne presque partout

\[
 \nabla G
 =\varepsilon_0\mathbf1_{\{\varepsilon_0F>t\}}\nabla F.
\tag{15}
\]

Les équations (2), (8) et (15) prouvent (10) et (12). Enfin `U_G` est compactement supporté, donc l'intégrale de son rotationnel est nulle composante par composante, ce qui donne (11). `□`

### Conséquence elliptique

Puisque `U_G` est divergence-free et compact,

\[
 U_G=\nabla\times(-\Delta)^{-1}W_G.
\tag{16}
\]

Le potentiel de Riesz d'ordre un en dimension trois donne

\[
 \|U_G\|_{L^{3,\infty}}
 \leq C_{\rm BS}\|W_G\|_{L^{3/2,\infty}}.
\tag{17}
\]

Ainsi, avec `K_G=||W_G||_{L^{3/2,∞}}`,

\[
 c_0\kappa\leq K_G\leq K,
 \qquad c_0=c_T/C_{\rm BS}>0.
\tag{18}
\]

Cette étape interdit que la troncature choisie ne conserve la vitesse tout en supprimant tout son curl.

## 4. Du paquet tronqué à une oscillation sur une boule

Choisissons `σ>0` presque optimal pour `K_G` et posons

\[
 E_\sigma=\{x:|W_G(x)|>\sigma\},
 \qquad v_\sigma=|E_\sigma|,
\tag{19}
\]

de sorte que, pour `0<η<1`,

\[
 \sigma v_\sigma^{2/3}
 \geq(1-\eta)K_G.
\tag{20}
\]

Les six cônes signés associés aux axes de coordonnées couvrent `S²` avec ouverture

\[
 \alpha=1/\sqrt3.
\tag{21}
\]

Il existe donc `e∈{±e₁,±e₂,±e₃}` et un sous-ensemble

\[
 H=\left\{x\in E_\sigma:
 \frac{W_G}{|W_G|}\cdot e\geq\frac1{\sqrt3}\right\}
\tag{22}
\]

de mesure au moins `v_σ/6`. Sa masse conique satisfait

\[
 m_H=\int_H|W_G|\,dx
 \geq\frac{\sigma v_\sigma}{6}.
\tag{23}
\]

### Lemme 4.1 — boule conditionnelle avec facteur de remplissage

Soit `B` une boule telle que `supp U_G` soit compactement contenu dans `B`. Toute extension bornée `ζ` de (5) satisfait

\[
 \boxed{
 \operatorname{MO}_B(\zeta)
 \geq
 \frac{(1-\eta)^3}{8748\sqrt3}
 \frac{v_\sigma}{|B|}.}
\tag{24}
\]

### Preuve

Par (11), `∫_B W_G=0`. La fonction `ε₀ζ` est une extension de la direction de `W_G` sur `{W_G≠0}`, et

\[
 \operatorname{MO}_B(\varepsilon_0\zeta)
 =\operatorname{MO}_B(\zeta).
\tag{25}
\]

Le claim `NS-LORENTZ-CONE-COMPENSATION` appliqué à `W_G`, (21) et (23) donne

\[
 \operatorname{MO}_B(\zeta)
 \geq
 \frac{2\alpha^3m_H^3}{27K_G^3|B|}.
\tag{26}
\]

Or (20) implique

\[
 m_H^3
 \geq\frac{(1-\eta)^3}{216}K_G^3v_\sigma.
\tag{27}
\]

En insérant `α³=1/(3√3)` dans (26), on obtient (24). `□`

La borne vaut pour toute extension intégrable, donc a fortiori pour toute extension bornée. Aucune borne uniforme sur `||ζ||_∞` n'est utilisée.

### Forme directement exploitable

Si l'on peut construire `B` avec

\[
 \operatorname{rad}(B)
 \leq C Rq^{-a},
 \qquad
 \frac{v_\sigma}{|B|}\geq c q^b,
\tag{28}
\]

alors le lemme demandé suit avec

\[
 \operatorname{MO}_B(\zeta)\geq c' q^b.
\tag{29}
\]

Le facteur `q³` issu de la taille de `K_G/K` s'annule dans (24), parce que le claim de cône est appliqué avec la norme exacte `K_G`. Toute la perte polynomiale finale est donc un problème de localisation et de remplissage, pas de compensation directionnelle.

## 5. Ce que les gates donnent déjà sur le support tronqué

Soit

\[
 S_G=|\operatorname{supp}G|_{dr\,dz}.
\tag{30}
\]

Le lemme universel de support mince du cycle 0032 donne

\[
 \|U_G\|_{L^{3,\infty}}
 \leq C_{\rm cyl}
 \left(\frac{S_G}{R^2}\right)^{1/6}K_G.
\tag{31}
\]

Les équations (9), (10) et (31) impliquent

\[
 \boxed{
 \frac{S_G}{R^2}
 \geq c_s q^6,}
 \qquad
 c_s=(c_T/C_{\rm cyl})^6.
\tag{32}
\]

Le volume tridimensionnel du support satisfait donc

\[
 |\operatorname{supp}U_G|
 \geq \pi R S_G
 \geq c_s\pi R^3q^6.
\tag{33}
\]

Ce résultat exclut une troncature active d'aire méridienne super-polynomialement petite.

Le ledger de variation totale du cycle 0032 donne aussi, pour un superniveau presque optimal de `U_G`, une borne sur la **mesure** de sa projection axiale. Si `h` est cette mesure et si `A≤R` est la largeur radiale disponible, alors

\[
 \left(\frac{K_G}{\|U_G\|_{L^{3,\infty}}}\right)^3
 \geq c\frac{Rh}{A^2}
 \geq c\frac hR,
\tag{34}
\]

d'où

\[
 h\leq C Rq^{-3}.
\tag{35}
\]

Mais (32)–(35) ne donnent ni le diamètre de l'union des composantes, ni la fraction `v_σ/|supp U_G|`.

## 6. Pourquoi coaire et isopérimétrie ne ferment pas encore (28)

Pour presque tout niveau `τ`, chaque composante `C` de `{G>τ}` vérifie l'isopérimétrie plane

\[
 \operatorname{Per}(C)\geq2\sqrt{\pi|C|}.
\tag{36}
\]

La coaire donne

\[
 \int|\nabla G|\,dr\,dz
 =\int_0^\infty
 \operatorname{Per}(\{G>\tau\})\,d\tau.
\tag{37}
\]

Ces identités contrôlent une somme de périmètres, mais le gate faible-`L^{3/2}` contrôle seulement les fonctions de distribution de `|∇G|`. L'estimation

\[
 \int_E|\nabla G|
 \leq3\|\nabla G\|_{L^{3/2,\infty}}|E|^{1/3}
\tag{38}
\]

requiert de choisir un ensemble `E` de volume contrôlé. Si les transitions sont réparties entre de nombreuses composantes ou de nombreux niveaux d'amplitude, prendre l'union de tous leurs supports réintroduit précisément le facteur de dilution que (28) doit éviter.

Deux informations manquent simultanément :

1. **sélection de composante** : une composante de troncature doit conserver une fraction polynomiale de la quasi-norme faible de `U_G` ;
2. **densité de curl** : dans cette composante, un superniveau réalisant une fraction polynomiale de `K_G` doit remplir une fraction polynomiale d'une boule contenant la compensation `∫curl U_G=0`.

La seule aire totale (32) ne prouve aucune de ces deux assertions.

## 7. Composantes séparées et dispersion axiale hors borne de diamètre

### 7.1 Satellite de faible amplitude : nécessité de l'hypothèse axiale

Soient deux profils fixes `F₀,F₁` satisfaisant (1), avec supports axiaux compacts. Pour `Z` plus grand que leurs diamètres et `0<ε≪1`, posons

\[
 F_{\varepsilon,Z}(r,z)
 =F_0(r,z)+\varepsilon F_1(r,z-Z).
\tag{39}
\]

Les supports sont disjoints. En choisissant `F₀` avec une marge dans les gates, on conserve uniformément

\[
 K_u(F_{\varepsilon,Z})\geq K_u(F_0)\geq\kappa,
\tag{40}
\]

\[
 K_\omega(F_{\varepsilon,Z})
 \leq C_{3/2}\bigl(K_\omega(F_0)
 +\varepsilon K_\omega(F_1)\bigr)
 \leq K,
\tag{41}
\]

où `C_{3/2}` est la constante de quasi-triangle faible-Lorentz. Pourtant,

\[
 \operatorname{diam}_z(\operatorname{supp}F_{\varepsilon,Z})
 \sim Z
\tag{42}
\]

est arbitraire, même super-polynomial en `q⁻¹`.

Ce profil réfute l'inférence auxiliaire

\[
 \text{« les gates bornent le diamètre du support total ».}
\tag{43}
\]

Il ne réfute pas le lemme existentiel recherché : la boule décisive peut rester près de `F₀`, et la troncature (7) élimine le satellite si son amplitude est sous le niveau actif.

Pour `Z>2ΛR`, il ne satisfait plus l'hypothèse axiale renforcée de (1). Il montre pourquoi cette hypothèse est matérielle et ne peut être déduite des seuls gates.

### 7.2 Support axial de petite mesure mais grand diamètre

Même après avoir borné la mesure `h` dans (35), une union de petits intervalles axiaux peut avoir un diamètre arbitraire. Ainsi

\[
 |\operatorname{proj}_zE|\leq C Rq^{-3}
\quad\not\Longrightarrow\quad
 \operatorname{diam}(\operatorname{proj}_zE)
 \leq C'Rq^{-a}.
\tag{44}
\]

Le premier quantificateur faux d'une preuve naïve est donc le remplacement de la **mesure** d'une projection par son **diamètre**, avant sélection d'une composante connectée.

## 8. Domaine arbitraire versus boule

Le claim de compensation conique est valide sur tout domaine fini qui contient une compensation de moyenne nulle. Il n'existe cependant pas de conversion abstraite

\[
 \operatorname{MO}_D(\zeta)\geq c
 \quad\Longrightarrow\quad
 \exists B_{\rho},\ \rho\leq L:
 \operatorname{MO}_{B_\rho}(\zeta)\geq c'
\tag{45}
\]

sans contrôle géométrique de `D`.

Contre-modèle mesurable précis : prenons deux boules unités `D_+` et `D_-` distantes de `Z`, posons `ζ=e` sur `D_+`, `ζ=−e` sur `D_-`, et interpolons `ζ` sur le complément avec pente `O(1/Z)`. Sur `D=D_+∪D_-`, l'oscillation est d'ordre un. Pour toute boule de rayon au plus `L≪Z` qui ne rencontre qu'une phase ou le corridor d'interpolation,

\[
 \operatorname{MO}_B(\zeta)\leq C\frac LZ.
\tag{46}
\]

Ce contre-modèle réfute uniquement le passage fonctionnel abstrait (45). Il n'est pas présenté comme le curl d'un `U` de la forme (2), car chaque paquet compact de vitesse possède sa propre compensation. La structure `W_G=curl U_G` est précisément l'information supplémentaire qu'un futur lemme de sélection doit exploiter.

## 9. Signes, composantes et flux de bord

1. **Signes de `F`.** La troncature choisit un seul signe. Sur la branche négative, `W_G=−W`; l'oscillation est inchangée après multiplication de l'extension par `−1`.
2. **Composantes connexes.** Chaque composante d'une troncature peut définir son propre champ compact après une nouvelle troncature au niveau de bord. Mais aucune composante n'est encore prouvée porteuse d'une fraction polynomiale de `K_u`.
3. **Composantes de `W`.** Les composantes `W_r` et `W_z` sont orthogonales; elles ne s'annulent pas dans `|W|`. En revanche, les contributions de plusieurs couches à une même dérivée de `F` s'annulent avant la fonction de distribution.
4. **Boule locale.** Sur une boule arbitraire,
   \[
   \int_BW_G\,dx
   =\int_{\partial B}n\times U_G\,dS,
   \tag{47}
   \]
   et non zéro en général. Le lemme 4.1 exige que la boule contienne le support de `U_G`; sinon il faut suivre ce flux de bord.
5. **Extension aux zéros.** La preuve conique est uniforme sur toutes les extensions intégrables. Les valeurs choisies sur `{W=0}` ou `{W_G=0}` ne peuvent supprimer les deux phases actives contenues dans la même boule.

## 10. Échelle

Sous

\[
 U_\lambda(x)=\lambda U(\lambda x),
 \qquad
 W_\lambda(x)=\lambda^2W(\lambda x),
\tag{48}
\]

les deux gates, `q`, la direction et les oscillations moyennes sont invariants. Les longueurs `R`, les rayons de boule et les diamètres sont divisés par `λ`; les volumes `v_σ` et `|B|` sont divisés par `λ³`. Le rapport de remplissage dans (24) et les conditions (28) sont donc exactement invariants.

## 11. Passe contradictoire

1. **Troncation de `|F|` sans signe.** Évitée : `( |F|-t )_+` aurait une dérivée `sign(F)∇F`; la formulation signée (7) rend (12) exact à un signe global près.
2. **Supremum faible supposé atteint.** Évité par les défauts arbitraires dans (14) et (20).
3. **Norme du curl tronqué supposée égale à `K`.** Faux; seule (18) est prouvée. La compensation conique utilise la norme exacte `K_G`.
4. **Moyenne nulle sur une boule locale.** Faux sans (47). Elle est vraie dans le lemme 4.1 parce que la boule contient tout `supp U_G`.
5. **Aire de support confondue avec volume de superniveau.** (32) minore `S_G`; elle ne minore pas `v_σ/|supp U_G|`.
6. **Projection axiale confondue avec intervalle.** Réfuté par (44).
7. **Domaine de compensation pris pour une boule.** Réfuté abstraitement par (45)–(46).
8. **Satellites.** (39)–(43) montrent que le diamètre du support total n'est pas contrôlé par les gates.
9. **Claim plus fort que la preuve.** Aucun exposant universel `p` pour la boule finale n'est annoncé tant que (28) n'est pas obtenu.
10. **Navier–Stokes.** Aucun résultat statique ici ne construit un profil de blow-up ni un critère dynamique.

## 12. Résultat scientifique et état

### Résultat positif

La troncature signée transforme les gates initiaux en un paquet compact `U_G` qui conserve une vitesse critique `≥c_Tκ`, possède un curl critique entre `c₀κ` et `K`, et satisfait exactement `∫curl U_G=0`. La compensation conique donne ensuite la minoration de boule explicite (24). Le problème de direction est réduit au seul rapport géométrique `v_σ/|B|`.

### Résultat négatif sans borne axiale

En l'absence de la borne `|z-z₀|<ΛR`, les gates ne contrôlent ni le diamètre du support total ni le diamètre d'une projection axiale de mesure contrôlée. Le satellite (39) et l'implication fausse (44) empêchent alors de choisir comme boule le support global ou son enveloppe convexe.

### Ce qui reste ouvert sans borne axiale

Aucun contre-profil admissible de la forme (2) n'a été trouvé contre l'existence d'une **autre** boule locale satisfaisant une minoration polynomiale lorsque `Λ` n'est pas contrôlé. Le contre-modèle (45) ne possède pas la structure curl compacte requise.

**État intermédiaire : À REPRENDRE sans borne axiale; l'addendum de diamètre borné ci-dessous conclut sous l'hypothèse (1).**

## 13. Prochaine expérience décisive

Prouver ou réfuter le lemme de sélection suivant : pour le paquet `G` du lemme 3.1, il existe une composante de double troncature `H=(G-s)_+` et un superniveau de `|curl U_H|` tels que

\[
 \operatorname{rad}(B_H)
 \leq C Rq^{-a},
 \qquad
 \frac{|\{|\operatorname{curl}U_H|>\sigma_H\}|}{|B_H|}
 \geq c q^b,
\tag{49}
\]

où `B_H` contient `supp U_H`. Une preuve de (49), insérée dans (24), conclurait immédiatement avec `p=b`. Un contre-exemple doit garder `K_u≥κ` et `K_ω≤K` tout en faisant dégénérer **toutes** les composantes de double troncature; ajouter seulement des satellites sous le niveau actif ne suffit pas.

Références internes utilisées : `claims/navier-stokes/NS-LORENTZ-CONE-COMPENSATION.json`, `docs/reports/navier-stokes/reviews/cycle-0026-analysis.md` et `docs/reports/navier-stokes/reviews/cycle-0032-analysis.md`.

## 14. Contre-revue distincte sous hypothèse de diamètre axial borné

Cette section vérifie la chaîne renforcée demandée sous l'hypothèse complète (1). Elle fournit une preuve directe plus forte que le lemme conditionnel 4.1, car elle emploie la masse `L¹` totale du curl tronqué plutôt qu'un superniveau de ce curl.

Posons les quasi-normes méridiennes

\[
 K_f=\|F\|_{L^{3,\infty}(\mathbb R^2)},
 \qquad
 K_g=\|\nabla F\|_{L^{3/2,\infty}(\mathbb R^2)}.
\tag{50}
\]

### 14.1 Niveau, signe et troncature

Choisissons `λ>0` avec

\[
 \lambda|\{|F|>\lambda\}|^{1/3}
 \geq(1-\varepsilon)K_f,
 \qquad 0<\varepsilon<1.
\tag{51}
\]

Il existe un signe `σ∈{−1,+1}` tel que

\[
 A=\{\sigma F>\lambda\}
\]

vérifie

\[
 |A|\geq\frac12|\{|F|>\lambda\}|,
 \qquad
 \lambda|A|^{1/3}
 \geq2^{-1/3}(1-\varepsilon)K_f.
\tag{52}
\]

Définissons

\[
 G=(\sigma F-\lambda/2)_+.
\tag{53}
\]

Sur `A`, `G>λ/2`. Le weak HLS bidimensionnel

\[
 \|G\|_{L^{6,\infty}(\mathbb R^2)}
 \leq C_{\rm HLS}
 \|\nabla G\|_{L^{3/2,\infty}(\mathbb R^2)}
 \leq C_{\rm HLS}K_g
\tag{54}
\]

donne dans l'autre sens

\[
 \frac\lambda2|A|^{1/6}
 \leq C_{\rm HLS}K_g.
\tag{55}
\]

La division de (52) par (55) est licite et produit

\[
 \boxed{
 |A|^{1/6}
 \geq c_1(1-\varepsilon)\frac{K_f}{K_g}.}
\tag{56}
\]

Le sens de (55) est un point critique : HLS majore la norme faible-`L⁶` de `G`, tandis que la présence de `A` la minore par `(λ/2)|A|^{1/6}`.

### 14.2 Coaire et isopérimétrie

Pour presque tout `t∈(0,λ/2)`,

\[
 \{G>t\}=\{\sigma F>\lambda/2+t\}
 \supset A.
\]

L'isopérimétrie plane donne

\[
 \operatorname{Per}(\{G>t\})
 \geq2\sqrt{\pi|A|}.
\tag{57}
\]

La formule de coaire, (52) et (56) impliquent

\[
\begin{aligned}
 \operatorname{TV}(G)
 &=\int_{\mathbb R^2}|\nabla G|\,dr\,dz\\
 &=\int_0^\infty
   \operatorname{Per}(\{G>t\})\,dt\\
 &\geq\lambda\sqrt{\pi|A|}\\
 &=(\lambda|A|^{1/3})
   \sqrt\pi|A|^{1/6}\\
 &\geq c_2(1-\varepsilon)^2
   \frac{K_f^2}{K_g}.
\end{aligned}
\tag{58}
\]

Cette étape emploie le périmètre de la réunion entière. Des composantes séparées ou des signes internes ne diminuent pas l'isopérimétrie du superniveau réel après annulation.

### 14.3 Masse tridimensionnelle et cône signé

Posons

\[
 U_G=\frac RrG e_\theta,
 \qquad W_G=\nabla\times U_G.
\tag{59}
\]

L'identité cylindrique exacte vaut

\[
 M:=\int_{\mathbb R^3}|W_G|\,dx
 =2\pi R\operatorname{TV}(G)
 \geq c_3(1-\varepsilon)^2
 R\frac{K_f^2}{K_g}.
\tag{60}
\]

Partitionnons la sphère des directions en six cônes signés d'ouverture `α=1/√3`, en attribuant chaque direction à une coordonnée signée maximale. L'un d'eux porte une masse

\[
 m\geq M/6.
\tag{61}
\]

Cette sélection se fait par **masse `L¹`**, non par mesure de superniveau; elle reste valide si les amplitudes des composantes sont très différentes.

Par la règle de chaîne,

\[
 W_G=\sigma W
 \quad\text{sur }\{W_G\ne0\}.
\tag{62}
\]

Si `ζ` est une extension bornée de `ξ=W/|W|`, alors `σζ` est une extension de la direction de `W_G`, et

\[
 \operatorname{MO}_B(\sigma\zeta)
 =\operatorname{MO}_B(\zeta).
\tag{63}
\]

Le signe ne crée donc aucune lacune.

### 14.4 Domaine axial versus vraie boule

Le domaine annulaire axial

\[
 D_\Lambda
 =\{(r,\theta,z):R/2<r<3R/2,
                     \ |z-z_0|<\Lambda R\}
\tag{64}
\]

a le volume exact

\[
 |D_\Lambda|=4\pi\Lambda R^3.
\tag{65}
\]

Il contient `supp U_G`, donc

\[
 \int_{D_\Lambda}W_G\,dx=0.
\tag{66}
\]

Le claim `NS-LORENTZ-CONE-COMPENSATION`, (60)–(61) et `||W_G||_{L^{3/2,∞}}≤K_ω` donnent

\[
 \operatorname{MO}_{D_\Lambda}(\zeta)
 \geq
 c\frac{R^3}{|D_\Lambda|}
 \frac{K_f^6}{K_g^3K_\omega^3}.
\tag{67}
\]

Les comparaisons cylindriques (6) ont les sens

\[
 K_f\geq cR^{-1/3}K_u,
 \qquad
 K_g\leq CR^{-2/3}K_\omega.
\tag{68}
\]

Ainsi

\[
 \boxed{
 \operatorname{MO}_{D_\Lambda}(\zeta)
 \geq c\Lambda^{-1}
 \left(\frac{K_u}{K_\omega}\right)^6.}
\tag{69}
\]

Mais `D_Λ` n'est pas une boule. La boule euclidienne centrée sur l'axe

\[
 B_\Lambda
 =B\!\left((0,0,z_0),
 R\sqrt{\Lambda^2+9/4}+0^+\right)
\tag{70}
\]

contient compactement `supp U_G` et a, à la limite `0⁺→0`, le volume

\[
 |B_\Lambda|
 =\frac{4\pi}{3}R^3
   (\Lambda^2+9/4)^{3/2}.
\tag{71}
\]

En appliquant directement le même claim sur cette boule,

\[
 \boxed{
 \operatorname{MO}_{B_\Lambda}(\zeta)
 \geq
 c(\Lambda^2+9/4)^{-3/2}
 \left(\frac{K_u}{K_\omega}\right)^6.}
\tag{72}
\]

Le rayon est `O(R(1+Λ))`. Pour `Λ≥1`, la perte de boule est `Λ⁻³`, et non `Λ⁻¹`. Confondre le cylindre (64) avec une boule de volume `O(ΛR³)` est le premier trou de la chaîne proposée si l'on réclame réellement une boule.

### 14.5 Forme polynomiale et verdict “diamètre borné”

Sous les gates (3), (72) devient

\[
 \boxed{
 \operatorname{MO}_{B_\Lambda}(\zeta)
 \geq c(1+\Lambda)^{-3}q^6.}
\tag{73}
\]

Si

\[
 \Lambda\leq C_\Lambda q^{-a}
\tag{74}
\]

pour un exposant fixé `a≥0`, alors

\[
 \operatorname{rad}(B_\Lambda)
 \leq C Rq^{-a},
 \qquad
 \operatorname{MO}_{B_\Lambda}(\zeta)
 \geq c q^{6+3a}.
\tag{75}
\]

**VERDICT DISTINCT — DIAMÈTRE BORNÉ : VALIDÉ**, avec `p=6` si `Λ` est une constante uniforme, et `p=6+3a` sous (74). La chaîne niveau→HLS→coaire→masse→cône est correcte. La seule correction est géométrique : `Λ⁻¹` vaut sur le domaine annulaire axial, tandis qu'une vraie boule coûte `Λ⁻³`.

La troncature `G` est lipschitzienne plutôt que `C∞`; les identités de chaîne, coaire et curl sont valides presque partout. Une approximation lisse monotone de la partie positive conserve toutes les estimations avec un défaut arbitraire, ce qui justifie l'application au cadre lisse du claim de cône.

**État final du cycle : CONTINUER sous diamètre borné; À REPRENDRE pour supprimer ou produire dynamiquement la borne (74).**
