# Cycle 0039 — Annulation étiquetée à multiplicité deux

Date : 2026-08-15
Statut : certificat exact de distributions atomiques et raccord analytique non certifié
Portée : obstruction à la sélection cellule par cellule sous chevauchement des curls

## Verdict

Une borne de multiplicité égale à deux ne suffit pas à transférer un rapport
endpoint global vers l'une des deux cellules étiquetées.

Il existe deux paires abstraites

\[
(U_1,W_1)=(V+P_n,B+Z_n),\qquad
(U_2,W_2)=(-P_n,-Z_n)
\tag{39.1}
\]

telles que, point par point,

\[
U_1+U_2=V,\qquad W_1+W_2=B.
\tag{39.2}
\]

Le champ total vérifie un rapport fixe

\[
q_{\rm glob}
={\|V\|_{L^{3,\infty}}\over
\|B\|_{L^{3/2,\infty}}}=1,
\tag{39.3}
\]

alors que, pour \(M_n=2^n\),

\[
q_1={4^{1/3}\over M_n-1}\longrightarrow0,
\qquad
q_2={1\over M_n}\longrightarrow0.
\tag{39.4}
\]

La somme est exactement \(B\), pas seulement proche de \(B\), et aucun
argument de quasi-triangle n'intervient.

Le même mécanisme possède un raccord analytique exact au niveau des champs :
si \(P_n=\varepsilon\Phi\sin(nz/R)\), les deux curls oscillatoires
\(Z_n\) et \(-Z_n\) se compensent algébriquement. Leur taille individuelle
est \(O(n)\), tandis que la vitesse reste \(O(1)\). Le certificat embarqué
ne certifie cependant que le ledger atomique ; il ne certifie ni les
fonctions de distribution continues du sinus, ni une PDE.

## 1. Espace atomique partitionné

Prenons quatre atomes

\[
A_{p,z},\qquad p,z\in\{-1,+1\},\qquad
|A_{p,z}|={1\over4}.
\tag{39.5}
\]

Sur chaque atome, définissons

\[
V=1,\qquad B=1,\qquad P_n=p,\qquad Z_n=M_nz,
\qquad M_n=2^n.
\tag{39.6}
\]

Les étiquettes \(p\) et \(z\) sont indépendantes. Chaque point appartient
aux deux cellules (39.1) : la multiplicité de recouvrement est exactement
deux.

Les identités de somme sont atomiquement exactes :

\[
(V+P_n)+(-P_n)=V,
\qquad
(B+Z_n)+(-Z_n)=B.
\tag{39.7}
\]

Il ne reste aucun résidu sur aucun atome.

## 2. Fonctions de distribution exactes

On note

\[
\mu_f(t)=|\{|f|>t\}|.
\tag{39.8}
\]

### Curl global et oscillation

\[
\mu_B(t)=
\begin{cases}
1,&0<t<1,\\
0,&t\ge1,
\end{cases}
\tag{39.9}
\]

\[
\mu_{Z_n}(t)=\mu_{-Z_n}(t)=
\begin{cases}
1,&0<t<M_n,\\
0,&t\ge M_n.
\end{cases}
\tag{39.10}
\]

Sur les deux atomes \(z=+1\), \(|B+Z_n|=M_n+1\); sur les deux atomes
\(z=-1\), \(|B+Z_n|=M_n-1\). Donc

\[
\mu_{B+Z_n}(t)=
\begin{cases}
1,&0<t<M_n-1,\\
1/2,&M_n-1\le t<M_n+1,\\
0,&t\ge M_n+1.
\end{cases}
\tag{39.11}
\]

Les inégalités sont strictes. Au seuil \(M_n-1\), la moitié de module
exactement \(M_n-1\) est déjà exclue. Pour calculer la quasi-norme, on prend
la limite à gauche, conformément au supremum sur \(t>0\).

### Vitesses

\[
\mu_V(t)=\mu_{-P_n}(t)=
\begin{cases}
1,&0<t<1,\\
0,&t\ge1,
\end{cases}
\tag{39.12}
\]

tandis que \(V+P_n=2\) sur \(p=+1\) et \(0\) sur \(p=-1\), d'où

\[
\mu_{V+P_n}(t)=
\begin{cases}
1/2,&0<t<2,\\
0,&t\ge2.
\end{cases}
\tag{39.13}
\]

Ces six distributions sont complètes à tous les seuils.

## 3. Quasi-normes et rapports

Avec

\[
K_3(f)=\sup_{t>0}t\mu_f(t)^{1/3},\qquad
K_{3/2}(g)=\sup_{t>0}t\mu_g(t)^{2/3},
\tag{39.14}
\]

les cubes évitent toute racine :

\[
K_3(V)^3=K_3(P_n)^3=1,\qquad
K_3(V+P_n)^3=2^3{1\over2}=4.
\tag{39.15}
\]

Pour le curl,

\[
K_{3/2}(B)^3=1,\qquad
K_{3/2}(Z_n)^3=K_{3/2}(-Z_n)^3=M_n^3.
\tag{39.16}
\]

Les deux candidats pour \(B+Z_n\) sont

\[
(M_n-1)^3,\qquad{(M_n+1)^3\over4}.
\tag{39.17}
\]

Pour \(M_n\ge8\), le premier est le plus grand, donc

\[
K_{3/2}(B+Z_n)^3=(M_n-1)^3.
\tag{39.18}
\]

Les rapports cubiques sont exactement

\[
q_{\rm glob}^3=1,\qquad
q_1^3={4\over(M_n-1)^3},\qquad
q_2^3={1\over M_n^3}.
\tag{39.19}
\]

La multiplicité deux ne fournit ainsi aucune constante
\(c>0\) telle que

\[
\max(q_1,q_2)\ge c\,q_{\rm glob}.
\tag{39.20}
\]

## 4. Cancellation partielle

Remplaçons la deuxième étiquette par

\[
W_2^{(\rho)}=-(1-\rho)Z_n.
\tag{39.21}
\]

Le curl total devient

\[
B+\rho Z_n.
\tag{39.22}
\]

Si \(\rho\) est fixe, sa norme croît comme \(\rho M_n\) et le rapport global
dégénère. Pour garder le résidu global borné, il faut

\[
\rho M_n=O(1),\qquad\text{donc}\qquad
\rho=O(M_n^{-1}).
\tag{39.23}
\]

Le certificat teste le choix critique \(\rho=M_n^{-1}\). Alors
\(B+\rho Z_n\) vaut \(2\) sur la moitié des atomes et \(0\) sur l'autre,
si bien que

\[
K_{3/2}(B+\rho Z_n)^3
=2^3(1/2)^2=2.
\tag{39.24}
\]

L'obstruction est donc stable sous une erreur absolue \(O(1)\), mais exige
une précision relative \(O(M_n^{-1})\) lorsque les curls individuels
croissent.

## 5. Raccord analytique pure-swirl

Fixons \(R>0\), une fonction

\[
\Phi\in C_c^\infty(\{R/2<r<3R/2,\ |z|<2R\})
\tag{39.25}
\]

égale à un sur un cylindre annulaire intérieur, et un potentiel de base
\(F_0\in C_c^\infty\) dans le même anneau. Posons

\[
P_n(r,z)=\varepsilon\Phi(r,z)\sin(nz/R).
\tag{39.26}
\]

Les deux vitesses étiquetées sont

\[
U_1={R\over r}(F_0+P_n)e_\theta,\qquad
U_2=-{R\over r}P_ne_\theta.
\tag{39.27}
\]

Leur somme est exactement

\[
U_1+U_2={R\over r}F_0e_\theta=:V.
\tag{39.28}
\]

Avec

\[
B={R\over r}(-\partial_zF_0\,e_r+\partial_rF_0\,e_z),
\tag{39.29}
\]

\[
Z_n={R\over r}(-\partial_zP_n\,e_r+\partial_rP_n\,e_z),
\tag{39.30}
\]

la linéarité du curl donne exactement

\[
\operatorname{curl}U_1=B+Z_n,\qquad
\operatorname{curl}U_2=-Z_n,\qquad
\operatorname{curl}(U_1+U_2)=B.
\tag{39.31}
\]

Le terme principal est

\[
(Z_n)_r
=-\varepsilon{n\over r}\Phi(r,z)\cos(nz/R)
-\varepsilon{R\over r}\Phi_z(r,z)\sin(nz/R).
\tag{39.32}
\]

Sur une proportion fixe du cylindre intérieur,
\(|\cos(nz/R)|\ge1/2\). Le terme de cutoff est \(O(\varepsilon/R)\),
tandis que le premier est \(O(\varepsilon n/R)\). Il existe donc des
constantes indépendantes de \(n\) telles que

\[
K_{3/2}(Z_n)\ge c\varepsilon nR-C\varepsilon R,
\tag{39.33}
\]

\[
K_3(U_2)\le C\varepsilon R,\qquad
K_3(U_1)\le C(\|F_0\|_\infty+\varepsilon)R.
\tag{39.34}
\]

Ainsi \(q_1,q_2=O(n^{-1})\), tandis que le rapport du champ total, fixé par
\(F_0\), est indépendant de \(n\).

Ce raccord est une dérivation analytique de lois d'échelle. Le certificat
atomique ne prouve pas (39.33), ne calcule pas la distribution exacte du
sinus fenêtré et ne fournit aucun résidu PDE. Il n'y a ni évolution,
pression, diffusion, stretching ni assertion Clay.

## 6. Certificat Python standard library

Le script parcourt \(M=2^n\) jusqu'à \(2^{40}\). Pour chaque fréquence, il
matérialise les quatre atomes, vérifie les sommes pointwise, calcule toutes
les distributions strictes à chaque seuil et leurs limites à gauche, puis
calcule les quasi-normes sans quasi-triangle. Toutes les assertions utilisent
Fraction.

~~~python
from fractions import Fraction as Q


def mu_strict(values, volumes, threshold):
    return sum((v for x, v in zip(values, volumes)
                if abs(x) > threshold), Q(0))


def mu_left(values, volumes, amplitude):
    # Limit t -> amplitude from below.
    return sum((v for x, v in zip(values, volumes)
                if abs(x) >= amplitude), Q(0))


def weak_cube(values, volumes, p):
    best = Q(0)
    for amplitude in sorted({abs(x) for x in values if x != 0}):
        measure = mu_left(values, volumes, amplitude)
        if p == 3:
            candidate = amplitude ** 3 * measure
        elif p == Q(3, 2):
            candidate = amplitude ** 3 * measure ** 2
        else:
            raise ValueError(p)
        best = max(best, candidate)
    return best


checks = 0
volumes = [Q(1, 4)] * 4
labels = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

for exponent in range(3, 41):
    M = Q(2 ** exponent)
    V = [Q(1)] * 4
    B = [Q(1)] * 4
    P = [Q(p) for p, _ in labels]
    Z = [M * z for _, z in labels]
    U1 = [v + p for v, p in zip(V, P)]
    U2 = [-p for p in P]
    W1 = [b + z for b, z in zip(B, Z)]
    W2 = [-z for z in Z]

    for i in range(4):
        assert U1[i] + U2[i] == V[i]
        assert W1[i] + W2[i] == B[i]
        checks += 2

    # Strict distributions at every breakpoint.
    assert mu_strict(B, volumes, Q(0)) == 1
    assert mu_strict(B, volumes, Q(1)) == 0
    assert mu_strict(Z, volumes, M - 1) == 1
    assert mu_strict(Z, volumes, M) == 0
    assert mu_strict(W1, volumes, M - 2) == 1
    assert mu_strict(W1, volumes, M - 1) == Q(1, 2)
    assert mu_strict(W1, volumes, M) == Q(1, 2)
    assert mu_strict(W1, volumes, M + 1) == 0
    assert mu_strict(W2, volumes, M - 1) == 1
    assert mu_strict(W2, volumes, M) == 0
    assert mu_strict(U1, volumes, Q(0)) == Q(1, 2)
    assert mu_strict(U1, volumes, Q(2)) == 0
    checks += 12

    ku_global3 = weak_cube(V, volumes, 3)
    kw_global3 = weak_cube(B, volumes, Q(3, 2))
    ku1_3 = weak_cube(U1, volumes, 3)
    ku2_3 = weak_cube(U2, volumes, 3)
    kw1_3 = weak_cube(W1, volumes, Q(3, 2))
    kw2_3 = weak_cube(W2, volumes, Q(3, 2))

    assert ku_global3 == 1
    assert kw_global3 == 1
    assert ku1_3 == 4
    assert ku2_3 == 1
    assert kw1_3 == (M - 1) ** 3
    assert kw2_3 == M ** 3
    assert ku1_3 / kw1_3 == Q(4, (M - 1) ** 3)
    assert ku2_3 / kw2_3 == Q(1, M ** 3)
    checks += 8

    # Critical partial cancellation rho=1/M.
    rho = 1 / M
    W2_partial = [-(1 - rho) * z for z in Z]
    residual = [w1 + w2 for w1, w2 in zip(W1, W2_partial)]
    assert residual == [Q(0), Q(2), Q(0), Q(2)]
    assert weak_cube(residual, volumes, Q(3, 2)) == 2
    checks += 2

    # Scale covariance: amplitude c and volume c^-3 preserve both cubes
    # for velocity scaling; curl uses amplitude c^2 and volume c^-3.
    c = Q(2 ** (exponent % 7))
    scaled_V = [c * x for x in V]
    scaled_B = [c ** 2 * x for x in B]
    scaled_volumes = [v / c ** 3 for v in volumes]
    assert weak_cube(scaled_V, scaled_volumes, 3) == ku_global3
    assert weak_cube(scaled_B, scaled_volumes, Q(3, 2)) == kw_global3
    checks += 2

    if exponent in (3, 8, 16, 24, 32, 40):
        print("M=2^%d q_global^3=%s q1^3=%s q2^3=%s" %
              (exponent, ku_global3 / kw_global3,
               ku1_3 / kw1_3, ku2_3 / kw2_3))

print("exact checks =", checks)
print("exact residual = 0")
~~~

## 7. Passe contradictoire

1. **Quasi-triangle.** Aucune étape ne remplace
   \(\|W_1+W_2\|\) par \(\|W_1\|+\|W_2\|\). La distribution du total est
   recalculée après la somme pointwise.
2. **Cancellation seulement en norme.** (39.7) vérifie la cancellation sur
   chacun des quatre atomes. (39.31) est également une identité de champs.
3. **Cancellation partielle.** Une erreur relative fixe échoue; elle doit
   être \(O(M_n^{-1})\). Ce coût de précision est explicite.
4. **Seuils.** Les superniveaux sont stricts et tous les breakpoints
   \(1,2,M_n-1,M_n,M_n+1\) sont testés des deux côtés pertinents.
5. **Mauvais exposant Lorentz.** Le certificat forme
   \(t^3\mu\) pour \(L^{3,\infty}\) et
   \(t^3\mu^2\) pour \(L^{3/2,\infty}\).
6. **Changement d'échelle.** La covariance
   \(U_c=cU(cx)\), \(W_c=c^2W(cx)\) est vérifiée exactement; elle ne
   modifie aucun rapport.
7. **Directions vectorielles.** Le ledger scalaire représente le pire cas
   colinéaire. Dans le raccord lisse, \(Z_n\) s'annule exactement entre les
   deux étiquettes comme vecteur; l'inégalité
   \(|B+Z_n|\ge|Z_n|-|B|\) suffit à la croissance individuelle.
8. **Continuum.** Le profil sinus est analytique, mais ses distributions ne
   sont pas certifiées par le script. Aucun résultat numérique n'est promu
   en preuve continue.

## 8. Décision scientifique

**CONTRE-EXEMPLE ABSTRAIT ET ANALYTIQUE À LA SÉLECTION ÉTIQUETÉE :**
la multiplicité deux, sans condition de signe ou de coercivité de Gram, ne
préserve aucun rapport local. La somme totale peut rester exactement fixe
pendant que les deux curls étiquetés divergent.

Le prochain lemme minimal doit imposer une hypothèse empêchant
l'anti-alignement, par exemple une borne uniforme

\[
\left|\sum_jW_j\right|^2
\ge c_{\rm Gram}\sum_j|W_j|^2
\tag{39.35}
\]

sur les bandes sélectionnées, ou utiliser une décomposition non étiquetée
du curl total. Une simple borne de multiplicité ne contient aucune
information de signature.
