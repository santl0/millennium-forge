# Cycle 0034 — sélection de cellule et distributions dyadiques

Date : 2026-08-14.

Type de passe : contre-modèle de distributions, audit géométrique et calcul
reproductible. Cette passe est une dérivation IA interne, et non une revue
externe indépendante.

## Verdict

La sélection d'une cellule est **fausse au niveau purement
mesure-théorique**. Il existe des familles finies d'atomes disjoints telles
que

\[
 K_u^{\rm glob}\geq1,\qquad
 K_w^{\rm glob}\leq(8/7)^{2/3},
 \tag{1}
\]

alors que

\[
 \sup_j\frac{K_{u,j}}{K_{w,j}}=2^{-n}\longrightarrow0.
 \tag{2}
\]

Ce contre-modèle utilise les fonctions de distribution totales; aucune
somme triangulaire n'intervient. Il montre qu'un argument abstrait portant
seulement sur des quasi-normes de Lorentz disjointes ne peut sélectionner
une bonne cellule.

En revanche, la distribution abstraite n'est pas celle du curl obligatoire
d'un potentiel pure-swirl compact et épais. Pour une cellule de volume
\(v_j\asymp\ell_j^3\), dont le plateau de vitesse a une amplitude \(A_j\),
la fermeture compacte impose une variation totale

\[
 \int_{Q_j}|W_j|\,dx
 \geq c A_jv_j^{2/3}.
 \tag{3}
\]

Cette contrainte géométrique manque au contre-modèle abstrait. Sous des
hypothèses uniformes de plateau effectif et de cellule épaisse, elle donne
un vrai lemme de sélection :

\[
 K_u^{\rm glob}\geq\kappa,\qquad
 K_w^{\rm glob}\leq K
 \tag{4}
\]

impliquent l'existence de \(j\) tel que

\[
 K_{u,j}\geq c\frac{\kappa^2}{K},
 \qquad
 \frac{K_{u,j}}{K_{w,j}}
 \geq c\frac{\kappa^2}{K^2}.
 \tag{5}
\]

Ainsi :

- **oui** pour des distributions abstraites indépendantes;
- **non** pour les cellules compactes épaisses, axialement séparées,
  satisfaisant (3);
- **ouvert** si les cellules ont des queues volumineuses, des sections
  cuspidales, des rayons majeurs dégénérés ou des supports qui se
  chevauchent.

## 1. Cadre et quantités

Les cellules \(Q_j\subset\mathbb R^3\) sont disjointes. Dans chaque cellule,

\[
 U_j=\psi_j e_\theta,
 \qquad
 W_j=\nabla\times U_j.
 \tag{6}
\]

Les champs globaux sont

\[
 U=\sum_jU_j,\qquad W=\sum_jW_j.
 \tag{7}
\]

La disjonction donne exactement

\[
 \mu_U(\lambda)
 :=|\{|U|>\lambda\}|
 =\sum_j|\{|U_j|>\lambda\}|,
 \tag{8}
\]

\[
 \mu_W(\lambda)
 :=|\{|W|>\lambda\}|
 =\sum_j|\{|W_j|>\lambda\}|.
 \tag{9}
\]

Par définition,

\[
 K_u^{\rm glob}
 =\sup_{\lambda>0}
 \lambda\mu_U(\lambda)^{1/3},
 \tag{10}
\]

\[
 K_w^{\rm glob}
 =\sup_{\lambda>0}
 \lambda\mu_W(\lambda)^{2/3}.
 \tag{11}
\]

Les quasi-normes individuelles sont définies par les mêmes formules avec
une seule cellule.

Les identités (8)--(11), et non
\(\|U\|\leq\sum_j\|U_j\|\), sont utilisées dans tout le cycle.

## 2. Contre-modèle abstrait exact

### 2.1 Atomes de vitesse

Fixons \(n\geq1\) et

\[
 N=8^n,\qquad v=8^{-n}.
 \tag{12}
\]

Dans chacune des \(N\) cellules, posons un atome de vitesse de module un et
de volume \(v\). Alors

\[
 \mu_U(\lambda)
 =
 \begin{cases}
 Nv=1,&0<\lambda<1,\\
 0,&\lambda\geq1.
 \end{cases}
 \tag{13}
\]

Donc

\[
 K_u^{\rm glob}=1,
 \qquad
 K_{u,j}=v^{1/3}=2^{-n}.
 \tag{14}
\]

### 2.2 Atomes de curl dyadiques

Indexons les cellules par \(j=0,\ldots,N-1\). Dans la cellule \(j\), posons
un atome abstrait de curl de module

\[
 G_j=4^{n+j}
 \tag{15}
\]

et de volume

\[
 w_j=G_j^{-3/2}=8^{-(n+j)}.
 \tag{16}
\]

On a \(w_j\leq v\), donc l'atome tient mesure-théoriquement dans sa cellule.
Chaque quasi-norme individuelle vaut exactement

\[
 K_{w,j}=G_jw_j^{2/3}=1.
 \tag{17}
\]

Par (14) et (17),

\[
 \sup_jK_{u,j}/K_{w,j}=2^{-n}.
 \tag{18}
\]

### 2.3 Fonction de distribution totale du curl

Pour un seuil juste inférieur à \(G_k\), les indices actifs sont
\(j\geq k\). Leur volume total est

\[
 \begin{aligned}
 T_k
 &=\sum_{j=k}^{N-1}8^{-(n+j)}\\
 &=8^{-(n+k)}
 \frac{1-8^{-(N-k)}}{1-1/8}.
 \end{aligned}
 \tag{19}
\]

Entre deux amplitudes successives, le produit de Lorentz augmente avec le
seuil. Il suffit donc de tester les \(G_k\). Or

\[
 G_kT_k^{2/3}
 =
 \left[
 \frac{1-8^{-(N-k)}}{1-1/8}
 \right]^{2/3}.
 \tag{20}
\]

Ainsi

\[
 1\leq K_w^{\rm glob}
 \leq(8/7)^{2/3}.
 \tag{21}
\]

Les amplitudes géométriques empêchent les volumes du curl de s'accumuler à
un même seuil. Le contre-modèle (12)--(21) répond positivement à la question
abstraite.

## 3. Pourquoi ces atomes ne sont pas des retours compacts

### 3.1 Géométrie d'une cellule épaisse

Prenons une cellule pure-swirl de diamètre

\[
 \ell=2^{-n},
 \tag{22}
\]

de volume \(v\asymp\ell^3=8^{-n}\), portant une vitesse de plateau
d'amplitude un.

Si la chute de un à zéro se fait dans une coquille d'épaisseur \(h_j\),
alors

\[
 G_j\asymp h_j^{-1},
 \qquad
 w_j^{\rm geom}\asymp\ell^2h_j
 \asymp\frac{\ell^2}{G_j}.
 \tag{23}
\]

Le cube de la quasi-norme individuelle géométrique est

\[
 \begin{aligned}
 (K_{w,j}^{\rm geom})^3
 &\asymp
 G_j^3(w_j^{\rm geom})^2\\
 &=
 G_j\ell^4.
 \end{aligned}
 \tag{24}
\]

Pour les amplitudes (15),

\[
 (K_{w,j}^{\rm geom})^3
 \asymp4^{j-n}.
 \tag{25}
\]

Seuls \(O(n)\) niveaux vérifient \(K_{w,j}^{\rm geom}\lesssim1\), alors que
le contre-modèle demande \(N=8^n\) niveaux distincts.

### 3.2 Incompatibilité de volume

Le volume abstrait de (16) correspondrait à une épaisseur

\[
 h_j^{\rm abs}
 =w_j/\ell^2
 =2^{-n-3j}.
 \tag{26}
\]

La variation transportée par un gradient \(G_j\) sur cette épaisseur vaut

\[
 G_jh_j^{\rm abs}
 =2^{n-j}.
 \tag{27}
\]

Elle vaut un uniquement au niveau \(j=n\). Pour \(j<n\), l'atome transporte
plusieurs variations inutiles; pour \(j>n\), il ne ferme même pas le
plateau. Les paires indépendantes \((G_j,w_j)\) de (15)--(16) ne peuvent
donc pas être les uniques couches de retour des potentiels compacts.

### 3.3 Retour épais minimal

Même avant d'ajouter les atomes dyadiques, chaque plateau compact possède
un retour de base. Pour une épaisseur comparable à \(\ell\),

\[
 G_{\rm base}\asymp\ell^{-1}=2^n,
 \qquad
 w_{\rm base}\asymp\ell^3=8^{-n}.
 \tag{28}
\]

Chaque cellule a alors

\[
 K_{w,j}^{\rm base}\asymp2^{-n},
 \tag{29}
\]

mais les \(N=8^n\) retours ont la même amplitude. Leur fonction de
distribution totale donne

\[
 K_w^{\rm base,glob}
 \asymp
 2^n(N8^{-n})^{2/3}
 =2^n.
 \tag{30}
\]

Ce terme obligatoire suffit à détruire (1). Ajouter des oscillations
dyadiques de curl ne l'annule pas, puisque les cellules sont disjointes et
la distribution porte sur \(|W|\).

## 4. Lemme de sélection géométrique

### 4.1 Hypothèses de cellule

Pour chaque \(j\), supposons :

1. une amplitude de plateau \(A_j>0\);
2. un ensemble effectif \(E_j\subset Q_j\) de volume
   \(|E_j|\geq c_0v_j\), sur lequel \(|U_j|\geq c_0A_j\);
3. un volume de boîte \(|Q_j|\leq C_0v_j\);
4. une fermeture compacte pure-swirl satisfaisant

\[
 \int_{Q_j}|W_j|\,dx
 \geq c_1A_jv_j^{2/3}.
 \tag{31}
\]

La dernière inégalité est la version tridimensionnelle du coût de variation
totale. Pour une section méridienne épaisse d'aire \(\asymp\ell_j^2\) et un
rayon majeur \(\asymp\ell_j\), la coaire/isopérimétrie bidimensionnelle
donne un périmètre \(\gtrsim\ell_j\); l'intégration azimutale ajoute un
facteur \(\ell_j\), d'où \(A_j\ell_j^2=A_jv_j^{2/3}\).

Les constantes \(c_0,C_0,c_1\) doivent être uniformes. Une queue de très
faible amplitude ne peut pas être comptée dans \(v_j\) sans vérifier
l'hypothèse 2.

### 4.2 Sélection au seuil global

Posons

\[
 \varepsilon=\sup_jK_{u,j}.
 \tag{32}
\]

À constantes de cellule près,

\[
 K_{u,j}\asymp A_jv_j^{1/3}.
 \tag{33}
\]

Si \(K_u^{\rm glob}\geq\kappa\), il existe un seuil \(\lambda>0\) et un
ensemble d'indices

\[
 J_\lambda=\{j:A_j\geq c\lambda\}
 \tag{34}
\]

tels que, avec

\[
 S=\sum_{j\in J_\lambda}v_j,
 \tag{35}
\]

on ait

\[
 \lambda S^{1/3}\geq c\kappa.
 \tag{36}
\]

Pour \(j\in J_\lambda\), (32)--(34) donnent

\[
 v_j^{1/3}
 \leq C\varepsilon/\lambda.
 \tag{37}
\]

Donc

\[
 \sum_{j\in J_\lambda}v_j^{2/3}
 =
 \sum_j\frac{v_j}{v_j^{1/3}}
 \geq
 c\frac{\lambda S}{\varepsilon}.
 \tag{38}
\]

En sommant (31),

\[
 \int_{\bigcup_{j\in J_\lambda}Q_j}|W|\,dx
 \geq
 c\lambda
 \sum_{j\in J_\lambda}v_j^{2/3}
 \geq
 c\frac{\lambda^2S}{\varepsilon}.
 \tag{39}
\]

### 4.3 Usage exact de la norme faible

Pour \(p=3/2\), toute fonction vérifie

\[
 \int_E|f|\,dx
 \leq3\|f\|_{L^{3/2,\infty}}|E|^{1/3}.
 \tag{40}
\]

Les boîtes étant disjointes et \(|Q_j|\leq C_0v_j\),

\[
 \left|\bigcup_{j\in J_\lambda}Q_j\right|
 \leq C_0S.
 \tag{41}
\]

Si \(K_w^{\rm glob}\leq K\), (39)--(41) donnent

\[
 c\frac{\lambda^2S}{\varepsilon}
 \leq CK S^{1/3}.
 \tag{42}
\]

Par (36),

\[
 \boxed{
 \varepsilon
 \geq c\frac{\kappa^2}{K}.
 }
 \tag{43}
\]

Il existe donc une cellule avec

\[
 K_{u,j}\geq c\kappa^2/K.
 \tag{44}
\]

Comme

\[
 K_{w,j}\leq K_w^{\rm glob}\leq K
 \tag{45}
\]

par monotonie des fonctions de distribution, on obtient (5).

Le lemme utilise la fonction de distribution globale une première fois
pour choisir \(\lambda\), puis l'inégalité Lorentz exacte (40). Il ne
remplace jamais la norme globale par une somme de normes individuelles.

## 5. Distributions hétérogènes et niveaux dyadiques

Pour des amplitudes \(A_j\), volumes \(v_j\), gradients \(G_j\) et volumes
de retour \(w_j\), le problème abstrait complet est

\[
 \mu_U(\lambda)
 =\sum_jv_j\mathbf1_{\{A_j>\lambda\}},
 \tag{46}
\]

\[
 \mu_W(\lambda)
 =\sum_jw_j\mathbf1_{\{G_j>\lambda\}}.
 \tag{47}
\]

Pour une liste finie, les suprema sont atteints juste sous une amplitude
\(A_j\) ou \(G_j\). Le calcul exact consiste donc à :

1. trier les amplitudes décroissantes;
2. cumuler les volumes correspondants;
3. maximiser \(A_k(\sum_{j\leq k}v_j)^{1/3}\) ou
   \(G_k(\sum_{j\leq k}w_j)^{2/3}\).

La construction (12)--(21) exploite la différence entre les exposants
\(1/3\) et \(2/3\). La condition géométrique (31) recouple les deux listes
et interdit de les choisir indépendamment.

### Cellules axialement dispersées

La distance entre les cellules n'entre pas dans (46)--(47), tant que leurs
supports sont disjoints. De grands vides axiaux ne doivent pas être ajoutés
à \(v_j\) ni au volume \(S\) de (35). Le lemme sélectionne l'union des
boîtes, pas leur enveloppe convexe.

### Signes

Changer les signes de cellules n'affecte pas \(\mu_U\) ou \(\mu_W\).
L'annulation lointaine des vitesses ou des impulsions est une question
distincte; elle ne répare pas le coût local de fermeture (31).

## 6. Support artificiellement épaissi

Le lemme échoue si \(v_j\) désigne le support topologique d'une queue alors
que le plateau effectif est beaucoup plus petit.

Pour deux niveaux dans une cellule,

\[
 |U_j|=
 \begin{cases}
 A_j,&\text{volume }\mu_jv_j,\\
 \tau_jA_j,&\text{volume }(1-\mu_j)v_j,
 \end{cases}
 \tag{48}
\]

la distribution exacte est

\[
 \mu_{U_j}(\lambda)
 =
 v_j\left[
 \mu_j\mathbf1_{\{\lambda<A_j\}}
 +(1-\mu_j)\mathbf1_{\{\lambda<\tau_jA_j\}}
 \right].
 \tag{49}
\]

Ainsi

\[
 K_{u,j}
 =
 A_jv_j^{1/3}
 \max\{\mu_j^{1/3},\tau_j\}.
 \tag{50}
\]

Si \(\tau_j\ll\mu_j^{1/3}\), la queue ne contribue pas à la norme et le
volume effectif est \(\mu_jv_j\). Utiliser \(v_j\) dans (31) surestimerait
alors le coût isopérimétrique.

Si \(\tau_j\gtrsim\mu_j^{1/3}\), la queue contribue réellement à
\(K_{u,j}\). Sa propre fermeture doit apparaître dans (47) et dans
l'intégrale (31).

Une application future du lemme doit donc stocker la distribution complète
de chaque cellule, et non une seule taille de support.

## 7. Énergie, pression et diffusion

Pour une cellule épaisse de taille \(\ell_j\) et amplitude \(A_j\),

\[
 \|U_j\|_2^2\asymp A_j^2\ell_j^3,
 \tag{51}
\]

\[
 \|W_j\|_2^2
 \asymp
 A_j^2\ell_j^3/h_j^2
 \times(h_j/\ell_j)
 =
 A_j^2\ell_j^2/h_j.
 \tag{52}
\]

Ces ordres supposent un retour en coquille d'épaisseur \(h_j\). La
dispersion axiale rend les énergies additives, mais pas les pressions :

\[
 p=\mathcal R_i\mathcal R_j(U_iU_j)
 \tag{53}
\]

reste non locale.

Le temps diffusif le plus court de la cellule est

\[
 \tau_j=\frac{h_j^2}{\nu}.
 \tag{54}
\]

Dans l'essai abstrait, imposer \(G_j=h_j^{-1}=4^{n+j}\) donnerait

\[
 \tau_j=\nu^{-1}4^{-2(n+j)}.
 \tag{55}
\]

Au dernier des \(N=8^n\) niveaux, ce temps est doublement exponentiel en
\(n\). Même si les distributions abstraites étaient raccordées, leur
stabilité visqueuse disparaîtrait instantanément à l'échelle
macroscopique.

## 8. Test Python standard-library

Le test calcule les fonctions de distribution par tri et cumul, puis
vérifie les formules fermées. Il distingue :

- rationnels exacts : volumes, cubes de quasi-normes, queues géométriques;
- flottants : racines \(1/3\) et \(2/3\);
- proxy géométrique : coquille de surface \(\ell^2\);
- aucune simulation PDE.

~~~python
from fractions import Fraction as F


def weak_norm(atoms, exponent):
    """Exact cumulative volumes, floating final powers."""
    ordered = sorted(atoms, key=lambda item: item[0], reverse=True)
    cumulative = F(0)
    maximum = 0.0
    for amplitude, volume in ordered:
        cumulative += volume
        candidate = float(amplitude) * float(cumulative) ** exponent
        maximum = max(maximum, candidate)
    return maximum


max_exact_residual = F(0)

for n in (1, 2, 3, 4):
    component_count = 8**n
    cell_volume = F(1, 8**n)
    cell_ku = F(1, 2**n)

    assert component_count * cell_volume == 1
    assert cell_ku**3 == cell_volume

    # Closed-form exact W distribution at every dyadic threshold.
    global_kw_cube_upper = F(64, 49)
    for k in (0, min(n, component_count - 1), component_count - 1):
        remaining_factor = (
            1 - F(1, 8 ** (component_count - k))
        ) / (1 - F(1, 8))
        kw_cube = remaining_factor**2
        assert F(1) <= kw_cube <= global_kw_cube_upper

    individual_kw_cube = F(1)
    ratio_cube = cell_ku**3 / individual_kw_cube
    assert ratio_cube == F(1, 8**n)

    # A genuine shell with G_j=4^(n+j) has Kw_j^3=4^(j-n).
    for j in (0, min(n, component_count - 1), component_count - 1):
        gradient = F(4 ** (n + j))
        cell_scale = F(1, 2**n)
        shell_volume = cell_scale**2 / gradient
        geometric_kw_cube = gradient**3 * shell_volume**2
        expected = F(4 ** j, 4 ** n)
        residual = geometric_kw_cube - expected
        assert residual == 0
        max_exact_residual = max(max_exact_residual, abs(residual))

        abstract_volume = F(1, 8 ** (n + j))
        abstract_thickness = abstract_volume / cell_scale**2
        transported_drop = gradient * abstract_thickness
        assert transported_drop == F(2 ** n, 2 ** j)

    # The compulsory thick return already has global Kw=2^n.
    base_gradient = F(2**n)
    base_volume = cell_volume
    global_base_volume = component_count * base_volume
    global_base_kw_cube = (
        base_gradient**3 * global_base_volume**2
    )
    assert global_base_kw_cube == F(8**n)

# Explicit total-distribution calculation for manageable finite rows.
for n in (1, 2):
    component_count = 8**n
    cell_volume = F(1, 8**n)
    u_atoms = [(F(1), cell_volume) for _ in range(component_count)]
    w_atoms = [
        (F(4 ** (n + j)), F(1, 8 ** (n + j)))
        for j in range(component_count)
    ]

    ku = weak_norm(u_atoms, F(1, 3))
    kw = weak_norm(w_atoms, F(2, 3))
    assert abs(ku - 1.0) < 2.0e-14
    upper = float(F(8, 7)) ** (2.0 / 3.0)
    assert 1.0 - 2.0e-14 <= kw <= upper + 2.0e-14

# Exact core-tail distribution formula.
for denominator in (8, 32, 128):
    mu = F(1, denominator)
    tau = F(1, denominator)
    amplitude = F(5, 3)
    volume = F(7, 4)
    core_cube = amplitude**3 * volume * mu
    tail_cube = (tau * amplitude) ** 3 * volume
    exact_cube = max(core_cube, tail_cube)
    formula_cube = (
        amplitude**3 * volume * max(mu, tau**3)
    )
    residual = exact_cube - formula_cube
    assert residual == 0
    max_exact_residual = max(max_exact_residual, abs(residual))

print("maximum exact algebraic residual:", max_exact_residual)
print("abstract global Ku and Kw distributions: PASS")
print("individual-ratio collapse: PASS")
print("compact-shell geometric obstruction: PASS")
print("compulsory-return accumulation: PASS")
print("core-tail distribution: PASS")
~~~

Commande PowerShell de reproduction, depuis la racine du dépôt :

~~~powershell
$text = Get-Content docs/reports/navier-stokes/reviews/cycle-0034-countermodel.md
$start = [Array]::IndexOf($text, '~~~python') + 1
$stop = [Array]::IndexOf($text, '~~~', $start)
$text[$start..($stop - 1)] | python -
~~~

Précision : les résidus annoncés nuls sont des rationnels exacts. Les
racines de Lorentz utilisent des doubles IEEE 754 avec tolérance
\(2\times10^{-14}\). Graine : aucune. Dépendances : bibliothèque standard
Python uniquement.

Le test ne certifie pas l'inégalité géométrique (31), qui est une
conséquence analytique de coaire/isopérimétrie sous les hypothèses de
cellule. Il ne résout aucune évolution Navier--Stokes.

Exécution locale observée le 2026-08-14 : résidu rationnel maximal nul;
les distributions finies \(n=1,2\), les quatre lignes fermées
\(n=1,2,3,4\), les coquilles géométriques et les trois distributions
coeur--queue passent. La seule tolérance flottante est
\(2\times10^{-14}\).

## 9. Passe contradictoire

### 9.1 Exact versus abstrait

Les distributions (13) et (19) sont exactes pour des fonctions étagées
disjointes. Elles constituent un vrai contre-exemple au principe de
sélection dans la catégorie des fonctions mesurables.

Elles ne constituent pas un couple \(U,\nabla\times U\) : les quatre
paramètres \(A_j,v_j,G_j,w_j\) y sont indépendants. Les identités
(23)--(27) localisent précisément le raccord manquant.

### 9.2 Exact versus proxy géométrique

La loi \(w_j^{\rm geom}\asymp\ell_j^2/G_j\) est exacte en puissances pour
un retour de hauteur un, de surface \(\asymp\ell_j^2\), et de gradient
\(G_j\). Les constantes dépendent du profil et de la forme de cellule.

L'inégalité (31) est plus robuste que le proxy de coquille : elle autorise
des retours distribués et ne fixe aucune épaisseur unique. Elle requiert
toutefois une cellule épaisse et un plateau effectif.

### 9.3 Chevauchement

Si les supports de curl se chevauchent, des annulations pointwise signées
peuvent réduire \(W\) avant prise du module. Les identités (8)--(9) et le
lemme ne s'appliquent plus tels quels. Une telle construction n'est plus
une famille de cellules axialement séparées.

### 9.4 Rayon majeur et aspect

Si le rayon majeur est beaucoup plus grand que la section, le facteur
isopérimétrique de (31) change. Les cycles 0031 et 0033 montrent que ce
grand aspect diminue déjà le rapport critique. Le présent lemme suppose les
aspects uniformément bornés.

### 9.5 Faible-\(L^p\), pas fort-\(L^p\)

L'unique passage intégral est (40), qui est valide pour
\(L^{3/2,\infty}\). Aucune norme forte ni somme triangulaire de
quasi-normes n'est introduite.

### 9.6 Statut PDE

Après lissage, chaque cellule géométrique peut être une donnée initiale
pure-swirl compacte et divergence-free. Le contre-modèle abstrait ne le
peut pas sans ajouter les retours de (3). La pression, les interactions
lointaines et la dynamique ne sont pas calculées.

## 10. Énoncés falsifiables

### Résultat positif C34-A

Les atomes (12)--(16) satisfont exactement (1)--(2). La sélection de cellule
ne découle donc pas des seules fonctions de distribution disjointes.

Falsificateur : un seuil \(\lambda\) pour lequel le produit calculé avec la
distribution totale de (19) dépasse \((8/7)^{2/3}\).

### Résultat négatif C34-B

Sous les hypothèses de cellule 1--4 de la section 4.1, les bornes globales
(4) impliquent la sélection (5).

Falsificateur : une famille de cellules disjointes satisfaisant
uniformément (31), \(K_u^{\rm glob}\geq\kappa\),
\(K_w^{\rm glob}\leq K\), mais

\[
 \sup_jK_{u,j}/K_{w,j}\longrightarrow0.
 \tag{56}
\]

Elle invaliderait l'une des étapes (36), (38), (39) ou (40).

~~~json
{
  "cycle": "0034",
  "claim": "HETEROGENEOUS_CELL_SELECTION",
  "status": "ABSTRACT_SELECTION_FALSE_GEOMETRIC_SELECTION_CONDITIONAL_TRUE",
  "equation": "pure-swirl compact initial-data kinematics",
  "domain": "R^3",
  "solution_type": "disjoint compact initial cells after mollification; no evolution claim",
  "exact_results": [
    "finite dyadic abstract distributions with global gates and vanishing cell ratio",
    "total distribution formulas by sorted cumulative volumes",
    "geometric-shell exponent mismatch",
    "core-tail two-level distribution"
  ],
  "analytic_result": [
    "cell selection from uniform BV/isoperimetric closure cost"
  ],
  "limits": [
    "overlapping curl supports are excluded",
    "uniform thick effective plateaus and bounded aspects are required",
    "tails cannot be counted as plateau volume",
    "no pressure or Navier-Stokes evolution claim"
  ],
  "next_test": "prove the BV closure inequality for a pinned class of smooth toroidal cells"
}
~~~

État : **ABANDONNER** toute sélection fondée sur les seules quasi-normes
cellulaires. **POURSUIVRE** la sélection géométrique via (31).

Prochaine expérience décisive : fixer une classe lisse de cellules toriques
avec plateau de niveau \(A_j/2\), prouver (31) avec une constante explicite
par coaire dans la section méridienne, puis vérifier sa stabilité sous
queues de niveau \(\tau_jA_j\) et rayons majeurs variables.
