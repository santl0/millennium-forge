# Cycle 0013 — contre-profil Fourier de vorticité cohérente

Date de la passe adverse : 2026-08-14.

## Verdict

Sur le tore `T3=(R/2piZ)^3`, le champ réel analytique

\[
 u_a(x,y,z)=
 \bigl(\sin y+a\sin x\cos z,\ 0,\ -a\cos x\sin z\bigr)
 \tag{1}
\]

fournit un contre-profil exact pour `a=+1` et `a=-1` :

- les deux champs sont divergence-free et ont les mêmes énergie, enstrophie,
  palinstrophie, hélicité globale nulle et bornes rationnelles de cohérence de
  direction de vorticité autour de l'origine ;
- leur vorticité vaut la même valeur `omega(0)=-e_3`, son jet d'ordre un est
  nul, et la direction varie seulement à l'ordre quadratique ;
- le stretching ponctuel change pourtant de signe :
  `omega(0)^T S_a(0) omega(0)=-a` ;
- sur chaque boule `B_(2^-k)(0)`, `k>=1`, le signe persiste et la valeur
  absolue du stretching reste au moins `2401/4096` ;
- sous le scaling Navier–Stokes entier `U_(a,N)(x)=N u_a(Nx)`, la cohérence
  demeure identique sur la boule critique `B_(2^-k/N)`, tandis que
  `|Omega(0)|=N^2` et le stretching vaut `-a N^6`.

Le résultat négatif est précis : une règle universelle qui déduirait le signe,
ou une déplétion ponctuelle stricte de
`omega^T S omega / |omega|^3`, des seuls invariants pairs en `a`, de
l'analyticité et d'une cohérence locale de direction telle que celle certifiée
ci-dessous est réfutée. Le rapport ne réfute pas un critère global de type
Constantin–Fefferman, une hypothèse pairwise sur toute la région de grande
vorticité, une borne d'énergie uniforme sous scaling, ni une propriété
dynamique persistante de solutions Navier–Stokes.

## 1. Convention et équation

Toutes les intégrales sont des moyennes spatiales

\[
 \langle f\rangle=(2\pi)^{-3}\int_{\mathbb T^3}f(x)\,dx.
\]

Le champ (1) est une donnée initiale lisse, périodique et de moyenne nulle pour
Navier–Stokes incompressible 3D, sans force et de viscosité `nu>0` :

\[
 \partial_tu+(u\cdot\nabla)u-\nu\Delta u+\nabla p=0,
 \qquad \nabla\cdot u=0.
\]

Le certificat porte sur l'instant initial. Il ne prétend pas que (1) soit une
solution stationnaire ni que ses propriétés géométriques persistent. La
solution forte locale issue de cette donnée existe classiquement; sa pression
initiale est reconstruite à la section 4.

## 2. Dictionnaire Fourier réel exact

Avec la convention

\[
 u(x)=\sum_{k\in\mathbb Z^3}\widehat u(k)e^{ik\cdot x},
\]

les seuls modes non nuls sont, pour `eta,sigma,tau in {-1,+1}`,

\[
 \widehat u_a(0,\eta,0)
 =-\frac{i\eta}{2}(1,0,0),
 \tag{2}
\]

et

\[
 \widehat u_a(\sigma,0,\tau)
 =\frac{ia}{4}(-\sigma,0,\tau).
 \tag{3}
\]

Les six modes satisfont séparément

\[
 k\cdot\widehat u_a(k)=0,
 \qquad
 \widehat u_a(-k)=\overline{\widehat u_a(k)}.
 \tag{4}
\]

Ils certifient donc simultanément la divergence nulle et la réalité. Les modes
de vorticité `widehat(omega)(k)=ik cross widehat(u)(k)` sont

\[
 \widehat\omega_a(0,\eta,0)=(0,0,-1/2),
 \qquad
 \widehat\omega_a(\sigma,0,\tau)=(0,a\sigma\tau/2,0).
 \tag{5}
\]

Chaque mode a une hélicité modale nulle : la vitesse et la vorticité
correspondantes sont orthogonales. L'annulation de l'hélicité intégrée ne
provient donc pas d'une compensation flottante entre grands termes.

## 3. Champs dérivés, invariants et jets

Le calcul direct donne

\[
 \omega_a=\nabla\times u_a
 =\bigl(0,-2a\sin x\sin z,-\cos y\bigr),
 \tag{6}
\]

et

\[
 \nabla u_a=
 \begin{pmatrix}
 a\cos x\cos z&\cos y&-a\sin x\sin z\\
 0&0&0\\
 a\sin x\sin z&0&-a\cos x\cos z
 \end{pmatrix}.
 \tag{7}
\]

La partie symétrique est particulièrement simple :

\[
 S_a=\frac{\nabla u_a+\nabla u_a^T}{2}
 =\begin{pmatrix}
 a\cos x\cos z&\frac12\cos y&0\\
 \frac12\cos y&0&0\\
 0&0&-a\cos x\cos z
 \end{pmatrix}.
 \tag{8}
\]

Par Parseval et orthogonalité trigonométrique,

\[
 \begin{aligned}
 \langle|u_a|^2\rangle&=\frac{1+a^2}{2},
 &K_a:=\frac12\langle|u_a|^2\rangle&=\frac{1+a^2}{4},\\
 \langle|\omega_a|^2\rangle&=\frac12+a^2,
 &Z_a:=\frac12\langle|\omega_a|^2\rangle&=\frac14+\frac{a^2}{2},\\
 \langle|\nabla\omega_a|^2\rangle&=\frac12+2a^2,
 &\langle u_a\cdot\omega_a\rangle&=0.
 \end{aligned}
 \tag{9}
\]

La densité d'hélicité n'est pas identiquement nulle :

\[
 u_a\cdot\omega_a=a\cos x\sin z\cos y,
 \tag{10}
\]

mais sa moyenne est zéro. Pour `a=+1` et `a=-1`, les trois normes de (9) sont
respectivement `1`, `3/2` et `5/2`, tandis que `K=1/2` et `Z=3/4`.

À l'origine,

\[
 u_a(0)=0,\qquad
 \nabla u_a(0)=
 \begin{pmatrix}a&1&0\\0&0&0\\0&0&-a\end{pmatrix},
 \qquad
 \omega_a(0)=(0,0,-1).
 \tag{11}
\]

Le premier jet de vorticité est nul. Les seuls termes du deuxième jet utiles
ici sont

\[
 \partial_{xz}\omega_{a,2}(0)=-2a,
 \qquad
 \partial_{yy}\omega_{a,3}(0)=1.
 \tag{12}
\]

La direction est donc plate au premier ordre au centre, mais le jet mixte
encode déjà le signe de `a`.

## 4. Stretching signé et pression périodique

Le stretching scalaire exact vaut partout

\[
 \mathcal S_a(x)
 :=\omega_a^T S_a\omega_a
 =-a\cos x\cos z\cos^2y.
 \tag{13}
\]

En particulier,

\[
 \mathcal S_{+1}(0)=-1,
 \qquad
 \mathcal S_{-1}(0)=+1.
 \tag{14}
\]

Sa moyenne globale est néanmoins nulle pour les deux signes. Ainsi le champ ne
produit pas une croissance globale instantanée de l'enstrophie :

\[
 \frac{dZ}{dt}\bigg|_{t=0}
 =\langle\mathcal S_a\rangle
 -\nu\langle|\nabla\omega_a|^2\rangle
 =-\nu(1/2+2a^2).
 \tag{15}
\]

Le test distingue donc un stretching **local signé** d'une production globale
d'enstrophie.

La pression n'est pas omise. La contraction quadratique est

\[
 \partial_i u_j\,\partial_j u_i
 =a^2(\cos2x+\cos2z).
 \tag{16}
\]

La solution périodique de moyenne nulle de l'équation de pression est

\[
 -\Delta p_a=\partial_i u_j\,\partial_j u_i,
 \qquad
 p_a=\frac{a^2}{4}(\cos2x+\cos2z).
 \tag{17}
\]

Elle est paire en `a`; elle ne peut expliquer le renversement de (14). Le code
ci-dessous reconstruit (17) par convolution exacte des six modes.

## 5. Cohérence locale à bornes rationnelles

Fixons désormais `a=+1` ou `a=-1`, `k>=1` et

\[
 r=2^{-k}\leq1/2,
 \qquad B_r=B_r(0)\subset\mathbb T^3.
\]

Pour `X=(x,y,z) in B_r`, les inégalités élémentaires
`|sin s|<=|s|`, `1-cos s<=s^2/2` et
`cos s>=1-s^2/2` donnent

\[
 |\omega_a(X)-\omega_a(0)|
 \leq 2r^2+\frac12r^2=\frac52r^2,
 \tag{18}
\]

et

\[
 |\omega_a(X)|\geq|\cos y|
 \geq1-\frac12r^2\geq\frac78.
 \tag{19}
\]

Posons `xi_a=omega_a/|omega_a|`. Le calcul différentiel exact donne

\[
 |D\omega_a|_F^2
 \leq4z^2+4x^2+y^2\leq4r^2,
 \]

puis

\[
 |D\xi_a|
 \leq\frac{|D\omega_a|}{|\omega_a|}
 \leq\frac{16}{7}r.
 \tag{20}
\]

Comme la boule est convexe, on obtient deux obligations distinctes :

\[
 \sup_{X\in B_r}|\xi_a(X)-\xi_a(0)|
 \leq\frac{16}{7}r^2,
 \tag{21}
\]

et, pour tous `X,Y in B_r`,

\[
 |\xi_a(X)-\xi_a(Y)|
 \leq\frac{16}{7}r|X-Y|,
 \qquad
 |\xi_a(X)\times\xi_a(Y)|
 \leq\frac{16}{7}r|X-Y|.
 \tag{22}
\]

La seconde borne est réellement pairwise et dépend de `|X-Y|`; elle n'est pas
remplacée par la seule distance au centre.

En même temps, chaque facteur cosinus de (13) reste positif et

\[
 |\mathcal S_a(X)|
 \geq(1-r^2/2)^4
 \geq(7/8)^4
 =\frac{2401}{4096}.
 \tag{23}
\]

Le signe de `mathcal S_a` est donc constant sur `B_r` et opposé pour les deux
valeurs de `a`, malgré les mêmes constantes de cohérence.

Le quantificateur est explicite : pour tout entier `m>=0`, choisir

\[
 k\geq\left\lceil\frac{m+2}{2}\right\rceil
\]

assure, puisque `16/7<4`, que le membre droit de (21) est au plus `2^-m`,
alors que `|mathcal S_a(0)|=1`. Une cohérence centre–boule arbitrairement forte
obtenue en rétrécissant la boule ne produit donc aucune petite constante de
stretching au centre.

## 6. Contrôles de scaling entier

Deux conventions sont vérifiées séparément pour tout entier `N>=1`.

### Lift fréquentiel périodique

Posons

\[
 v_{a,N}(x)=u_a(Nx).
\]

La multiplication par `N` des fréquences préserve la périodicité et les
moyennes. On a

\[
 \begin{aligned}
 \langle|v_{a,N}|^2\rangle&=(1+a^2)/2,\\
 \langle|\nabla\times v_{a,N}|^2\rangle
 &=N^2(1/2+a^2),\\
 \langle v_{a,N}\cdot\nabla\times v_{a,N}\rangle&=0,\\
 \mathcal S[v_{a,N}](0)&=-aN^3.
 \end{aligned}
 \tag{24}
\]

Ce lift garde l'énergie bornée, mais son rayon de cohérence certifié est
`r/N`, plus petit que la longueur `|omega(0)|^-1/2=N^-1/2`.

### Scaling Navier–Stokes

Posons

\[
 U_{a,N}(x)=N u_a(Nx),
 \qquad P_{a,N}(x)=N^2p_a(Nx).
 \tag{25}
\]

Alors

\[
 \begin{aligned}
 \langle|U_{a,N}|^2\rangle&=N^2(1+a^2)/2,\\
 \langle|\Omega_{a,N}|^2\rangle&=N^4(1/2+a^2),\\
 \langle U_{a,N}\cdot\Omega_{a,N}\rangle&=0,\\
 \Omega_{a,N}(0)&=-N^2e_3,\\
 \mathcal S[U_{a,N}](0)&=-aN^6.
 \end{aligned}
 \tag{26}
\]

Sur `B_(r/N)`, les bornes (21)--(23) restent identiques après composition par
`Nx`. De plus,

\[
 |\Omega_{a,N}(X)|\geq\frac78N^2,
 \qquad
 \frac{\mathcal S[U_{a,N}](0)}{|\Omega_{a,N}(0)|^3}=-a.
 \tag{27}
\]

Le rayon `r/N=r |Omega(0)|^-1/2` est maintenant à l'échelle critique de
vorticité, avec `r=2^-k` fixé avant `N`. Le prix est une énergie globale qui
croît comme `N^2`. Le contre-profil ne satisfait donc pas simultanément cette
normalisation critique et une borne énergétique uniforme.

## 7. Bugs de quantificateurs et faux transferts

### Centre–boule contre pairwise

Une borne `|xi(X)-xi(0)|<=delta` donne au mieux une borne absolue `2delta`
entre deux points. Elle ne donne pas une loi
`C|X-Y|^alpha` quand `X` et `Y` sont arbitrairement proches. Les obligations
(21) et (22) doivent rester séparées. Ce certificat vérifie les deux dans une
seule boule, mais pas entre toutes les composantes d'une région globale de
grande vorticité.

### Petite échelle choisie après le champ

Pour tout champ analytique avec `omega(0)!=0`, la direction est cohérente sur
une boule assez petite. Une hypothèse de la forme « il existe un rayon dépendant
du champ » est presque vide. Un énoncé falsifiable doit fixer l'ordre des
quantificateurs : rayon absolu uniforme, constante uniforme, ou rayon relié à
`|omega|^-1/2`. Le scaling (25) traite ce dernier cas pour un `r=2^-k` fixé,
mais pas une borne d'énergie uniforme.

### Seuil de grande vorticité

Le champ non rescalé a `|omega(0)|=1`; il n'entre pas dans une hypothèse dont le
seuil absolu est supérieur à `1`. Dans (25), la boule certifiée satisfait
`|Omega|>=7N^2/8`, ce qui franchit tout seuil absolu fixé pour `N` assez grand.
Cela ne prouve pas la cohérence pairwise sur **tous** les points du tore qui
franchissent ce seuil. Un critère formulé globalement sur le high-vorticity set
n'est donc pas attaqué par le seul patch local.

### Analyticité

Les champs sont des polynômes trigonométriques et donc réels analytiques. Mais
les normes analytiques sur une bande complexe fixe croissent comme `exp(N rho)`
sous le lift fréquentiel, et encore avec l'amplitude `N` sous (25). Le mot
« analytique » sans rayon et constante uniformes ne fournit aucune déplétion;
avec de telles constantes uniformes, la famille rescalée peut sortir des
hypothèses.

### Déformation et pression non locales

Le stretching utilise `S`, pas seulement le jet de direction de `omega`.
Dans l'équation incompressible, `S` est relié non localement à `omega` par
Biot–Savart/Riesz. On ne pourrait donc pas assigner arbitrairement (8) à un jet
local de vorticité. Ici, les six modes globaux reconstruisent ensemble `u`,
`omega`, `S` et la pression (17); le contre-profil est compatible. Une
localisation sur `R3` exigerait en revanche une correction de divergence et un
nouveau contrôle des queues de pression : elle n'est pas couverte.

### Instant initial contre dynamique

La paire `a=+-1` donne deux données initiales différentes. Elle ne donne ni
deux solutions pour une même donnée, ni une trajectoire qui change le signe du
stretching, ni un blow-up. Elle teste seulement une implication algébrique
instantanée proposée entre géométrie et stretching.

## 8. Obligations machine-readable proposées

```json
{
  "artifact_id": "VORTICITY-COHERENCE-SIGNED-STRETCH-GATE-1",
  "version": 1,
  "domain": "T3=(R/2piZ)^3",
  "arithmetic": "Gaussian rationals represented by pairs of Fraction",
  "parameters": {
    "a": [-1, 1],
    "k_min": 1,
    "r": "2^-k",
    "N": "positive integer"
  },
  "obligations": [
    {"id": "F1_REALITY", "expected": "uhat(-m)=conj(uhat(m)) for every mode"},
    {"id": "F2_DIVERGENCE", "expected": "m dot uhat(m)=0 for every mode"},
    {"id": "F3_CURL", "expected": "omegahat(m)=i*m cross uhat(m)"},
    {"id": "I1_ENERGY", "expected": "<|u|^2>=(1+a^2)/2"},
    {"id": "I2_ENSTROPHY", "expected": "<|omega|^2>=1/2+a^2"},
    {"id": "I3_HELICITY", "expected": "every modal helicity and the total helicity are zero"},
    {"id": "J1_CENTER", "expected": "u(0)=0, omega(0)=(0,0,-1), Domega(0)=0"},
    {"id": "J2_HESSIAN", "expected": "d_xz omega_2(0)=-2a and d_yy omega_3(0)=1"},
    {"id": "S1_SIGN", "expected": "omega(0)^T S(0) omega(0)=-a"},
    {"id": "P1_PRESSURE", "expected": "-Delta[(a^2/4)(cos 2x+cos 2z)]=d_i u_j d_j u_i"},
    {"id": "C1_NONVANISHING", "expected": "inf_Br |omega|>=1-r^2/2>=7/8"},
    {"id": "C2_CENTER_TO_BALL", "expected": "sup_Br |xi-xi(0)|<=(16/7)r^2"},
    {"id": "C3_PAIRWISE", "expected": "|xi(X)-xi(Y)|<=(16/7)r|X-Y| on Br"},
    {"id": "C4_STRETCH_PERSISTS", "expected": "sign(S_a)=-a and |S_a|>=2401/4096 on Br"},
    {"id": "C5_QUANTIFIER", "expected": "k>=ceil((m+2)/2) gives center coherence <=2^-m while |stretch(0)|=1"},
    {"id": "N1_FREQUENCY_LIFT", "expected": "energy N^0, enstrophy N^2, stretch -a*N^3"},
    {"id": "N2_NS_SCALING", "expected": "energy N^2, enstrophy N^4, stretch -a*N^6"},
    {"id": "N3_CRITICAL_PATCH", "expected": "on B_(r/N), |Omega|>=7N^2/8 and direction bounds inherit C2-C3"},
    {"id": "G1_NO_GLOBAL_PROMOTION", "expected": "local patch is not the full high-vorticity set"},
    {"id": "G2_NO_DYNAMIC_PROMOTION", "expected": "instantaneous identity is not persistence or blow-up"},
    {"id": "G3_NO_ENERGY_UNIFORMITY", "expected": "NS-scaled family has energy proportional to N^2"}
  ]
}
```

## 9. Certificat Python stdlib exact

Le script suivant utilise seulement `fractions.Fraction`. Les nombres
complexes sont des couples de rationnels `(partie_reelle,partie_imaginaire)`;
aucun `complex` flottant n'est employé. Les bornes trigonométriques des
sections 5--6 sont les lemmes analytiques; la boucle rationnelle vérifie leurs
constantes pour `k=1,...,16`.

```python
from fractions import Fraction as F

Z = (F(0), F(0))

def add(x, y):
    return (x[0] + y[0], x[1] + y[1])

def neg(x):
    return (-x[0], -x[1])

def scale(q, x):
    return (q*x[0], q*x[1])

def mul(x, y):
    return (x[0]*y[0] - x[1]*y[1],
            x[0]*y[1] + x[1]*y[0])

def conj(x):
    return (x[0], -x[1])

def multiply_by_i_k(k, x):
    return (-k*x[1], k*x[0])

def abs2(x):
    return x[0]*x[0] + x[1]*x[1]

def velocity_modes(a):
    out = {}
    for eta in (-1, 1):
        out[(0, eta, 0)] = [(F(0), -F(eta, 2)), Z, Z]
    for sigma in (-1, 1):
        for tau in (-1, 1):
            out[(sigma, 0, tau)] = [
                (F(0), -F(a*sigma, 4)),
                Z,
                (F(0), F(a*tau, 4)),
            ]
    return out

def curl(modes):
    out = {}
    for k, u in modes.items():
        out[k] = [
            add(multiply_by_i_k(k[1], u[2]),
                neg(multiply_by_i_k(k[2], u[1]))),
            add(multiply_by_i_k(k[2], u[0]),
                neg(multiply_by_i_k(k[0], u[2]))),
            add(multiply_by_i_k(k[0], u[1]),
                neg(multiply_by_i_k(k[1], u[0]))),
        ]
    return out

def jet_at_zero(modes, derivative_indices):
    out = [Z, Z, Z]
    for k, vector in modes.items():
        factor = (F(1), F(0))
        for j in derivative_indices:
            factor = mul(factor, (F(0), F(k[j])))
        for i in range(3):
            out[i] = add(out[i], mul(factor, vector[i]))
    return out

def metrics(modes):
    omega_modes = curl(modes)
    energy = sum(abs2(z) for v in modes.values() for z in v)
    enstrophy = sum(abs2(z) for v in omega_modes.values() for z in v)
    helicity = Z
    for k, v in modes.items():
        for i in range(3):
            helicity = add(helicity,
                           mul(v[i], conj(omega_modes[k][i])))
    gradient = [
        [jet_at_zero(modes, (j,))[i][0] for j in range(3)]
        for i in range(3)
    ]
    omega0 = [z[0] for z in jet_at_zero(omega_modes, ())]
    strain = [
        [F(gradient[i][j] + gradient[j][i], 2) for j in range(3)]
        for i in range(3)
    ]
    stretching = sum(
        omega0[i]*strain[i][j]*omega0[j]
        for i in range(3) for j in range(3)
    )
    return energy, enstrophy, helicity, gradient, omega0, strain, stretching, omega_modes

for a in (-1, 1):
    modes = velocity_modes(a)

    for k, v in modes.items():
        assert modes[tuple(-q for q in k)] == [conj(z) for z in v]
        divergence = Z
        for j in range(3):
            divergence = add(divergence, scale(k[j], v[j]))
        assert divergence == Z

    E, Z2, H, G, omega0, S, stretch, omega_modes = metrics(modes)
    assert E == F(1 + a*a, 2)
    assert Z2 == F(1, 2) + a*a
    assert H == Z
    for mode, v in modes.items():
        modal_helicity = Z
        for i in range(3):
            modal_helicity = add(
                modal_helicity,
                mul(v[i], conj(omega_modes[mode][i])),
            )
        assert modal_helicity == Z
    palinstrophy = sum(
        sum(j*j for j in mode)*sum(abs2(z) for z in value)
        for mode, value in omega_modes.items()
    )
    assert palinstrophy == F(1, 2) + 2*a*a
    assert G == [[F(a), F(1), F(0)],
                 [F(0), F(0), F(0)],
                 [F(0), F(0), F(-a)]]
    assert omega0 == [F(0), F(0), F(-1)]
    for j in range(3):
        assert jet_at_zero(omega_modes, (j,)) == [Z, Z, Z]
    assert stretch == -a
    assert jet_at_zero(omega_modes, (0, 2)) == [Z, (F(-2*a), F(0)), Z]
    assert jet_at_zero(omega_modes, (1, 1)) == [Z, Z, (F(1), F(0))]

    # qhat is the exact convolution for d_i u_j d_j u_i.
    qhat = {}
    for k, uk in modes.items():
        for ell, ul in modes.items():
            K = tuple(k[j] + ell[j] for j in range(3))
            value = Z
            for i in range(3):
                for j in range(3):
                    value = add(
                        value,
                        mul(multiply_by_i_k(k[i], uk[j]),
                            multiply_by_i_k(ell[j], ul[i])),
                    )
            qhat[K] = add(qhat.get(K, Z), value)
    qhat = {k: z for k, z in qhat.items() if z != Z}

    phat = {
        (2, 0, 0): (F(a*a, 8), F(0)),
        (-2, 0, 0): (F(a*a, 8), F(0)),
        (0, 0, 2): (F(a*a, 8), F(0)),
        (0, 0, -2): (F(a*a, 8), F(0)),
    }
    assert qhat == {
        k: scale(sum(j*j for j in k), value)
        for k, value in phat.items()
    }

    for N in range(1, 9):
        lift = {tuple(N*j for j in k): v for k, v in modes.items()}
        ns_scaled = {
            k: [scale(N, z) for z in v]
            for k, v in lift.items()
        }
        El, Zl, Hl, _, _, _, Tl, _ = metrics(lift)
        Ens, Zns, Hns, _, _, _, Tns, _ = metrics(ns_scaled)
        assert (El, Zl, Hl, Tl) == (E, N*N*Z2, Z, -a*N**3)
        assert (Ens, Zns, Hns, Tns) == (N*N*E, N**4*Z2, Z, -a*N**6)

for k in range(1, 17):
    r = F(1, 2**k)
    assert F(1) - r*r/F(2) >= F(7, 8)
    assert F(16, 7)*r*r <= F(5)*r*r
    assert F(7, 8)**4 == F(2401, 4096)

for m in range(17):
    k = (m + 3)//2  # ceil((m+2)/2)
    r = F(1, 2**k)
    assert F(16, 7)*r*r <= F(1, 2**m)

print("fourier/reality/divergence/jets: PASS")
print("energy/enstrophy/helicity/stretching/pressure: PASS")
print("integer scaling and rational local bounds: PASS")
```

Sortie observée :

```text
fourier/reality/divergence/jets: PASS
energy/enstrophy/helicity/stretching/pressure: PASS
integer scaling and rational local bounds: PASS
```

Le calcul est déterministe, sans graine, grille, pas de temps ni flottant. Les
sommes de Fourier, jets, convolutions et identités de scaling ont un résidu
rationnel nul. Les inégalités trigonométriques sont analytiques; la boucle ne
fait qu'en contrôler la transcription rationnelle.

## 10. Statut scientifique et décision

Statuts proposés, sans création automatique de claim dans cette passe :

- certificat Fourier et bornes locales : **COMPUTATION_ONLY**, avec dérivation
  analytique et passe adverse interne ;
- implication « invariants globaux pairs + analyticité non uniforme +
  cohérence locale certifiée impliquent un signe universel du stretching » :
  **REFUTED** par la paire `a=+-1` ;
- implication vers une déplétion globale de type Constantin–Fefferman :
  **NON TESTÉE**, car la cohérence sur tout le high-vorticity set et les
  constantes globales uniformes ne sont pas établies ;
- implication vers régularité, singularité ou non-unicité Navier–Stokes :
  **NON ÉTABLIE**.

Décision : **ABANDONNER** toute recherche de signe fondée seulement sur
l'hélicité globale, les normes quadratiques, l'analyticité sans constante et
une cohérence choisie dans un seul patch. **CONTINUER** uniquement avec un
lemme qui fixe avant le champ :

1. la région exacte de grande vorticité et le seuil ;
2. une condition pairwise sur toute cette région ;
3. le rayon critique et une constante uniformes sous scaling ;
4. la norme globale qui contrôle la partie lointaine du Biot–Savart ;
5. la quantité de déplétion visée, sans la confondre avec un signe ponctuel.

La prochaine expérience décisive est de tester le même dictionnaire de modes
contre une hypothèse **globale** de cohérence sur toutes les composantes du
high-vorticity set, ou de démontrer qu'une telle hypothèse impose une borne
non locale sur `S` que le présent patch local ne voit pas.
