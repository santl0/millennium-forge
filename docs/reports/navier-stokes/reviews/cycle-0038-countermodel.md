# Cycle 0038 — Arbre de fusion dyadique à persistences évanescentes

Date : 2026-08-15
Statut : contre-modèle exact de ledger analytique ; non réalisé comme champ pure-swirl compact
Verrou : GAP-BRIDGE-SCALE-CALIBRATION-OR-MERGE-TREE

## Verdict

La dichotomie

\[
\text{branche calibrée}
\quad\text{ou}\quad
\text{composante bornée de bon rapport}
\tag{38.1}
\]

est **fausse si elle utilise seulement** les fonctions de distribution, un
arbre de fusion fini, les persistences, le coût coaire
diamètre \(\times\) persistance et les endpoints retronqués.

Un arbre binaire explicite de profondeur \(n\) satisfait

\[
K_u=1,\qquad 1\le K_w\le C<\infty,
\tag{38.2}
\]

alors que

\[
\max_{\rm branches}{a_{\rm merge}R\over K_u(\rm branche)}\to0,
\tag{38.3}
\]

et toute composante de diamètre \(O(R)\), après toutes les retroncatures,
vérifie

\[
{K_{u,\rm local}\over K_{w,\rm local}}
\asymp2^{-n/3}\to0.
\tag{38.4}
\]

Ce n'est toutefois **pas** un contre-exemple pure-swirl admissible. Les
atomes de curl attribués aux feuilles violent la fermeture compacte imposée
par coaire :

\[
\int_{\rm feuille}|W|\ll |E_{\rm feuille}|^{2/3}.
\tag{38.5}
\]

Le calcul réfute donc un argument purement combinatoire sur le merge tree,
mais ne réfute pas une dichotomie enrichie par la coaire à chaque feuille et
à chaque niveau.

## 1. Arbre et paramètres

Fixons \(n\ge1\), \(N=2^n\). À la profondeur \(k=0,\ldots,n\), l'arbre
possède \(2^k\) noeuds de \(M_k=2^{n-k}\) feuilles et diamètre axial

\[
D_k=M_kR=2^{n-k}R.
\tag{38.6}
\]

Les ponts qui fusionnent les enfants d'un noeud de profondeur \(k<n\) ont

\[
a_k=2^{-4n+2k},\qquad
\Delta_k=a_k^2=2^{-8n+4k},
\tag{38.7}
\]

\[
b_k=a_k+\Delta_k,\qquad
\delta_k=2^{-3n+k}.
\tag{38.8}
\]

Les niveaux augmentent vers les feuilles, mais

\[
\max_{k<n}b_k<2^{-2n+1},\qquad
{\Delta_k\over a_k}=a_k\to0
\tag{38.9}
\]

uniformément. Les gouttes terminales ont diamètre \(R\) et amplitude un.

## 2. Distributions exactes des feuilles

Chaque feuille porte un atome de vitesse d'amplitude \(1\) et volume
\(v=N^{-1}=2^{-n}\). Ainsi

\[
\mu_{U,\rm feuilles}(t)=
\begin{cases}1,&0<t<1,\\0,&t\ge1,\end{cases}
\qquad K_{u,\rm feuilles}=1.
\tag{38.10}
\]

Numérotons les feuilles \(j=0,\ldots,N-1\). Leur ledger de curl est

\[
G_j=4^{n+j},\qquad
w_j=G_j^{-3/2}=8^{-(n+j)}.
\tag{38.11}
\]

Chaque feuille satisfait

\[
K_{w,j}=G_jw_j^{2/3}=1,\qquad
K_{u,j}=v^{1/3}=2^{-n/3}.
\tag{38.12}
\]

Pour un seuil juste sous \(G_q\),

\[
\mu_{W,\rm feuilles}(G_q^-)
=\sum_{j=q}^{N-1}8^{-(n+j)}
=8^{-(n+q)}{1-8^{-(N-q)}\over1-1/8}.
\tag{38.13}
\]

Donc

\[
1\le K_{w,\rm feuilles}\le(8/7)^{2/3}.
\tag{38.14}
\]

Ces expressions sont les fonctions de distribution totales, et non des
sommes de quasi-normes.

## 3. Ponts, caps et curl tronqué

À la profondeur \(k\), la longueur totale est

\[
2^kD_k=NR.
\tag{38.15}
\]

En unités \(R=1\), le volume total des plateaux et parois est

\[
Q_k=2^k\delta_kD_k=N\delta_k=2^{-2n+k}.
\tag{38.16}
\]

La vitesse ajoutée a la distribution

\[
\mu_{U,\rm ponts}(t)
=\sum_{k=0}^{n-1}Q_k\mathbf1_{\{t<b_k\}}.
\tag{38.17}
\]

Sur une paroi linéaire \(b_k\to0\), le curl original a amplitude

\[
H_k={b_k\over\delta_k}
\tag{38.18}
\]

sur \(Q_k\). Les caps de longueur \(R\) ont amplitude \(b_k\) et volume

\[
C_k=2^k\delta_k=2^{-3n+2k}.
\tag{38.19}
\]

Ainsi

\[
\mu_{W,\rm ponts}(s)
=\sum_{k=0}^{n-1}
\left[Q_k\mathbf1_{\{s<H_k\}}
+C_k\mathbf1_{\{s<b_k\}}\right].
\tag{38.20}
\]

Pour \(G_k=(F-a_k)_+\), seule la fraction

\[
\theta_k={\Delta_k\over b_k}={a_k\over1+a_k}
\tag{38.21}
\]

reste active. Sa distribution de curl est

\[
\mu_{W,G_k}(s)
=Q_k\theta_k\mathbf1_{\{s<H_k\}}
+C_k\theta_k\mathbf1_{\{s<b_k\}}.
\tag{38.22}
\]

Le coût de paroi vaut exactement

\[
H_kQ_k\theta_k
={b_k\over\delta_k}(N\delta_k){\Delta_k\over b_k}
=N\Delta_k.
\tag{38.23}
\]

La somme diamètre \(\times\) persistance des \(2^k\) branches est la même :

\[
\sum_{\nu=1}^{2^k}D_k\Delta_k
=2^kD_k\Delta_k=N\Delta_k.
\tag{38.24}
\]

La version pondérée du lemme C37 donne

\[
\sum_\nu a_k\Delta_kRD_k
=a_kN\Delta_kR^2
=2^{-11n+6k}R^2.
\tag{38.25}
\]

Les sommes sur toutes les profondeurs sont

\[
\sum_{k<n}N\Delta_k
=\sum_{k<n}2^{-7n+4k}
<{16\over15}2^{-3n-4},
\tag{38.26}
\]

\[
\sum_{k<n}a_kN\Delta_k
=\sum_{k<n}2^{-11n+6k}
<{64\over63}2^{-5n-6}.
\tag{38.27}
\]

Toutes les persistences deviennent donc invisibles.

## 4. Endpoints globaux avec les ponts

La masse totale des ponts vérifie

\[
\sum_{k<n}Q_k=2^{-2n}(2^n-1)<2^{-n}.
\tag{38.28}
\]

Comme \(b_k\ll1\), (38.17) ne modifie pas le maximum \(K_u=1\).
Pour les parois,

\[
H_k=2^{-n+k}(1+a_k),
\tag{38.29}
\]

\[
H_kQ_k^{2/3}
=(1+a_k)2^{-7n/3+5k/3}
\le2\,2^{-2n/3-5/3}.
\tag{38.30}
\]

Les caps sont plus petits. Les seuils de pont restent sous \(1\), tandis
que le premier seuil de curl des feuilles est \(G_0=4^n\). La distribution
globale est exactement la somme de (38.13) et (38.20). Elle donne

\[
K_u=1,\qquad1\le K_w\le C_0,
\tag{38.31}
\]

avec \(C_0\) universel. Le certificat calcule le supremum exact à tous les
seuils et vérifie \(K_w^3<2\) pour \(1\le n\le9\).

## 5. Toutes les retroncatures

Coupons juste au-dessus du merge de profondeur \(k-1\). Les composantes
obtenues sont les \(2^k\) sous-arbres de \(M_k\) feuilles. Dans chacune,

\[
K_{u,k}^3={M_k\over N}=2^{-k}.
\tag{38.32}
\]

Dans tout bloc de feuilles, les amplitudes \(G_j\) restent géométriques :

\[
1\le K_{w,k}^3\le(8/7)^2={64\over49}.
\tag{38.33}
\]

Par conséquent,

\[
{49\over64}2^{-k}
\le\left({K_{u,k}\over K_{w,k}}\right)^3
\le2^{-k}.
\tag{38.34}
\]

Le diamètre vaut \(D_k=2^{n-k}R\). Un diamètre \(O(R)\) exige
\(k=n-O(1)\), où (38.34) donne un rapport \(O(2^{-n/3})\).

La calibration d'une branche est aussi absente :

\[
\left({a_kR\over K_{u,k}}\right)^3
=a_k^3\,2^k=2^{-12n+7k}
\le2^{-5n-7}.
\tag{38.35}
\]

La retroncature récursive échange donc exactement le diamètre contre le
facteur \(2^{-k/3}\) du rapport endpoint.

## 6. Défaut géométrique décisif

Le modèle est un squelette analytique. Une feuille de volume \(v=2^{-n}\)
et plateau unitaire doit satisfaire, pour une fermeture pure-swirl compacte,

\[
\int_{\rm feuille}|W|\,dx
\ge c\,v^{2/3}=c\,2^{-2n/3}.
\tag{38.36}
\]

L'atome (38.11) ne transporte que

\[
G_jw_j=G_j^{-1/2}=2^{-(n+j)}.
\tag{38.37}
\]

Dès \(j=0\), le quotient entre (38.37) et l'échelle requise est
\(2^{-n/3}\), puis décroît comme \(2^{-j}\). Le registre coaire échoue
avant même l'ajout des ponts.

Si ces atomes sont remplacés par d'authentiques fermetures pure-swirl,
les amplitudes et volumes de curl ne sont plus indépendants. Les feuilles
comparables s'accumulent au même seuil, le facteur \(N^{2/3}\) réapparaît,
ou la sélection du cycle 0036 choisit une goutte de bon rapport.

Les ponts, eux, peuvent être rendus négligeables parce que leur niveau
absolu tend très vite vers zéro. Ce sont les feuilles abstraites qui
empêchent la réalisation pure-swirl.

## 7. Certificat Python standard library

Le script énumère toutes les amplitudes, calcule les suprema de Lorentz par
tri exact, teste chaque noeud de chaque retroncature et contrôle les
identités coaire. Toutes les assertions utilisent Fraction.

~~~python
from fractions import Fraction as Q


def weak_cube(atoms, p):
    # atoms = [(amplitude, volume), ...], disjoint step functions.
    atoms = sorted(atoms, key=lambda x: x[0], reverse=True)
    total = Q(0)
    best = Q(0)
    for amplitude, volume in atoms:
        total += volume
        if p == 3:
            candidate = amplitude ** 3 * total
        elif p == Q(3, 2):
            candidate = amplitude ** 3 * total ** 2
        else:
            raise ValueError(p)
        best = max(best, candidate)
    return best


checks = 0
for n in range(1, 10):
    N = 2 ** n
    v = Q(1, N)
    u_atoms = [(Q(1), v) for _ in range(N)]
    w_leaf = []
    for j in range(N):
        G = Q(4) ** (n + j)
        w = Q(1, 8 ** (n + j))
        assert G ** 3 * w ** 2 == 1
        w_leaf.append((G, w))
        checks += 1

    bridge_u = []
    bridge_w = []
    bridge_levels = []
    coarea_sum = Q(0)
    weighted_sum = Q(0)
    for k in range(n):
        count = 2 ** k
        diameter = Q(2 ** (n - k))
        a = Q(1, 2 ** (4 * n - 2 * k))
        Delta = a ** 2
        b = a + Delta
        delta = Q(1, 2 ** (3 * n - k))
        Qk = Q(N) * delta
        Ck = Q(count) * delta
        H = b / delta
        theta = Delta / b

        assert Qk == Q(1, 2 ** (2 * n - k))
        assert Q(count) * diameter == N
        assert H * Qk * theta == Q(N) * Delta
        assert Q(count) * diameter * Delta == Q(N) * Delta
        assert a * Q(N) * Delta == Q(1, 2 ** (11 * n - 6 * k))

        bridge_u.append((b, Qk))
        bridge_w.append((H, Qk))
        bridge_w.append((b, Ck))
        bridge_levels.append((b, Qk, H, Ck))
        coarea_sum += Q(N) * Delta
        weighted_sum += a * Q(N) * Delta
        checks += 5

    ku3 = weak_cube(u_atoms + bridge_u, 3)
    kw3 = weak_cube(w_leaf + bridge_w, Q(3, 2))
    assert ku3 == 1
    assert 1 <= kw3 < 2
    assert sum(volume for _, volume in bridge_u) < v
    checks += 3

    # Every node at every retruncation depth.
    for k in range(n + 1):
        block = 2 ** (n - k)
        for node in range(2 ** k):
            lo = node * block
            hi = lo + block
            node_u = [(Q(1), v) for _ in range(block)]
            node_w = list(w_leaf[lo:hi])
            # A depth-k node contains the fraction 2^-k of every deeper
            # bridge level l>=k.
            for b, Ql, H, Cl in bridge_levels[k:]:
                node_u.append((b, Ql / 2 ** k))
                node_w.append((H, Ql / 2 ** k))
                node_w.append((b, Cl / 2 ** k))
            ku_node3 = weak_cube(node_u, 3)
            kw_node3 = weak_cube(node_w, Q(3, 2))
            assert ku_node3 == Q(1, 2 ** k)
            assert 1 <= kw_node3 <= Q(64, 49)
            ratio3 = ku_node3 / kw_node3
            assert Q(49, 64) * Q(1, 2 ** k) <= ratio3
            assert ratio3 <= Q(1, 2 ** k)
            checks += 4

    for k in range(n):
        a = Q(1, 2 ** (4 * n - 2 * k))
        calibration_cube = a ** 3 * 2 ** k
        assert calibration_cube == Q(1, 2 ** (12 * n - 7 * k))
        assert calibration_cube <= Q(1, 2 ** (5 * n + 7))
        checks += 2

    # Failure of compact coarea at the first abstract leaf.
    first_l1 = w_leaf[0][0] * w_leaf[0][1]
    assert first_l1 ** 3 < v ** 2
    checks += 1

    print("n=%d N=%d Ku^3=%s Kw^3=%.12f coarea=%.3e weighted=%.3e" %
          (n, N, ku3, float(kw3), float(coarea_sum),
           float(weighted_sum)))

print("exact checks =", checks)
print("exact residual = 0")
~~~

## 8. Passe contradictoire

1. **Supremum non atteint.** Les distributions sont finies et étagées; tous
   les seuils sont testés à gauche.
2. **Somme de quasi-normes.** Elle n'est jamais utilisée : les volumes sont
   cumulés avant le produit de Lorentz.
3. **Toutes les retroncatures.** Les \(2^k\) noeuds de chaque profondeur
   sont testés.
4. **Ponts oubliés.** Parois originales et caps entrent dans (38.20) et
   dans le supremum exact.
5. **Curl tronqué.** La fraction \(\theta_k\) est suivie et son intégrale
   vaut exactement \(N\Delta_k\).
6. **Diamètre topologique.** Le diamètre est une donnée du squelette. Une
   réalisation devrait employer des bandes ouvertes, pas des filaments nuls.
7. **Fausse réalisation PDE.** Les atomes ne sont ni le curl d'un champ
   compact explicite, ni un état Navier–Stokes. (38.36)--(38.37) exhibe le
   défaut.
8. **Pont de niveau nul.** Tous les \(a_k\) sont positifs pour \(n\) fini;
   ils ne disparaissent que dans la limite.

## 9. Décision scientifique

**RÉSULTAT NÉGATIF :** abandonner une preuve fondée uniquement sur un merge
tree enrichi par diamètre, persistance et endpoints. Le ledger ci-dessus en
est un falsificateur exact.

**NON-RÉSULTAT :** aucune famille pure-swirl \(C_c^\infty\) gardant un
rapport global non nul tout en évitant les deux branches de (38.1) n'est
construite. Le candidat échoue précisément à (38.36).

Le prochain lemme doit attacher à chaque noeud le déficit

\[
\mathfrak d(E)
:={\int_{\rm fermeture}|W|\over a|E|^{2/3}}
\tag{38.38}
\]

et montrer que ces déficits ne peuvent être simultanément petits le long de
toutes les feuilles. Une formulation équivalente serait une inégalité de
Carleson pour les budgets coaire des bandes emboîtées. Sans cette donnée,
la retroncature perd exactement le facteur \(2^{-k/3}\).
