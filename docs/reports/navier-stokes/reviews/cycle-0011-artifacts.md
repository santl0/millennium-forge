# Cycle 0011 — audit des artefacts spectraux Hou–Wang–Yang

Date de l'audit : 2026-08-14.

## Verdict

Le dépôt public de Hou–Wang–Yang au commit épinglé contient le profil approché,
un **eigenpair droit impair** approché, les résidus et les inversions de rang
fini qui entrent dans la preuve assistée par ordinateur de l'existence d'un
eigenpair exact proche. Il ne contient ni vecteur propre adjoint, ni contour et
borne de résolvante, ni certificat de multiplicité algébrique, ni norme de
projection de Riesz, ni constantes quantitatives du semi-groupe et de la
séparation finale des branches.

La réponse à la question de projection est donc exactement la suivante.

1. Pour la couche intérieure paire du cycle 0010, sa projection sur le
   **secteur impair** certifié est exactement nulle par symétrie. Ce résultat
   est analytique et ne nécessite aucun fichier binaire.
2. Le dépôt public ne suffit pas à calculer ou certifier sa projection par le
   projecteur de Riesz complet employé dans la preuve, ni la projection d'une
   couche qui brise la parité. Un eigenpair droit ne détermine pas un
   projecteur pour un opérateur non normal.
3. Même un coefficient de projection approché ne donnerait pas une séparation
   quantitative des solutions : les constantes des estimations de semi-groupe,
   les normes des projecteurs, le nombre de modes instables, le rayon analytique
   de localisation et la taille admissible des coordonnées instables ne sont
   pas chiffrés.

L'artefact minimal manquant pour dépasser le test nul de symétrie est un unique
**paquet de certificat de projection instable**, défini précisément à la
section 7. Aucune CAP de grande taille n'a été lancée, aucun dépôt n'a été
cloné et aucun binaire n'a été importé.

## 1. Objet mathématique et sources primaires

L'article primaire est Thomas Hou, Yixuan Wang et Changhe Yang,
[*Nonuniqueness of Leray–Hopf solutions to the unforced incompressible 3D
Navier–Stokes Equation*, arXiv:2509.25116v2](https://arxiv.org/abs/2509.25116v2),
prépublication v2 du 19 mars 2026. Le code primaire audité est
[`HouGroup2026/3d-navier-stokes-nonuniqueness`](https://github.com/HouGroup2026/3d-navier-stokes-nonuniqueness/tree/615ee6f3eca3abad7b5814fe9334bcd80bea0328),
au commit `615ee6f3eca3abad7b5814fe9334bcd80bea0328` du 23 mars 2026.

L'équation est Navier–Stokes incompressible, non forcé, sur `R^3`, avec
viscosité normalisée à `1`. En variables auto-similaires, l'opérateur dont le
mode instable est utilisé est

\[
 \mathcal L_{\widetilde U}v
 =\tfrac12v+\tfrac12\xi\cdot\nabla v
 -\Pi(\widetilde U\cdot\nabla v+v\cdot\nabla\widetilde U)+\Delta v.
\]

Le système elliptique vérifié dans la CAP emploie l'opérateur de signe opposé.
Le candidat stocké a `bar(lambda)=-0.11314203274385946`; la preuve donne
`|lambda-bar correction| <= 0.0045`. L'opérateur évolutif possède donc au
moins une valeur propre réelle positive

\[
 a=-(\bar\lambda+\lambda)\ge 0.10864203274385946.
\]

Cela certifie l'existence d'un eigenpair droit instable. Cela ne certifie pas
que cette valeur propre est simple, qu'elle est la seule valeur propre
instable, ni sa distance aux autres valeurs propres discrètes. Le bord du
spectre essentiel est dans `Re z <= -1/4`, ce qui donne une séparation d'au
moins `0.35864203274385946` avec ce bord, mais pas une séparation spectrale
complète.

## 2. Manifeste récursif épinglé

L'API GitHub, interrogée en lecture seule, donne :

- SHA de l'arbre Git : `723afb3838aa53a588193829d4e60000cfdf1b6b` ;
- 70 blobs, taille cumulée `84 137 370` octets ;
- `data/` : 50 blobs, `83 385 744` octets ;
- `notebooks/` : 6 blobs, `406 818` octets ;
- `src/` : 11 blobs, `198 460` octets ;
- racine : 3 blobs, `146 348` octets.

Le SHA-256 du manifeste textuel obtenu en triant les blobs par chemin et en
concaténant `path<TAB>size<TAB>git_blob_sha<LF>` est
`cde7bc4c6784d6c2b799714fd3ee034580cf3f3d28c42402da8ff20cf1274969`.
Ce hash porte sur les métadonnées GitHub, pas sur la concaténation des contenus.

### Racine, notebooks et sources

| Chemin | Octets | SHA-1 du blob Git |
| --- | ---: | --- |
| `NS spherical.nb` | 136582 | `7f114773ddf8e69ed9c5ca00389ee356c0b7d741` |
| `Project.toml` | 750 | `1b1c9ce2c529723ebda12aba37ecf6241b3d0470` |
| `README.md` | 9016 | `da37c6d7440cdf53f967049c6aca1a049f3defdb` |
| `notebooks/eigen_linear_operator_finite_rank.ipynb` | 44469 | `183647a4ce6fcaabe8aaf3f754693fef9545bedb` |
| `notebooks/eigenpair_error_analysis.ipynb` | 10373 | `2b5fda4d14dcec85b585b4fbb36d3bafa358b08d` |
| `notebooks/finite_rank_construction.ipynb` | 288702 | `76b4e93468c97f19115cfa439db546ff7b45d53b` |
| `notebooks/get_bessel_zeros.ipynb` | 12601 | `b22470fca3e4bd377d81fc0ebf9bf5eea1225f25` |
| `notebooks/selfsimilar_linear_operator_finite_rank.ipynb` | 37879 | `a74b298466cb11f5f2af722be408a8e843bd8e81` |
| `notebooks/selfsimilar_profile_verification.ipynb` | 12794 | `e74a75241f9027296bb0849ee299e60bb0ffc2b0` |
| `src/Comb_Bound.jl` | 14413 | `089176e67f27847f25af11a4aac921edc5d2dc76` |
| `src/Matrix_Func.jl` | 20002 | `17e37c8ec6a442c26a57c40133835e752ef0cae4` |
| `src/My_Assembly.jl` | 25680 | `67fe2d72e06cb994bf556676cce9ef97f7bb5945` |
| `src/My_Bessel.jl` | 21558 | `6141acc5c45914240ac607096eadb69647bc96be` |
| `src/My_Fourier.jl` | 23249 | `de71598ec55307e9b1ba945102dcb3ad723816bb` |
| `src/My_Operator.jl` | 13518 | `d9893613f76606d7bd89e84b077ee193a984291d` |
| `src/My_Scalar.jl` | 18252 | `82f688d28efac7c39940c5dccead889fce7fce08` |
| `src/My_Vector.jl` | 20896 | `322c8b0baf5e7b3452836335f87cbf5ff402e17d` |
| `src/NS_Numerics.jl` | 2940 | `a148115eeb02aff5e2108f91602d303ff0727726` |
| `src/NS_Terms.jl` | 20801 | `d495a72f9a63c3d058cc111ca1281b990032a262` |
| `src/Trig_Poly.jl` | 17151 | `6ae59b8344a97a8416303b11fca4f589eb91ae25` |

### Données directement liées au profil et aux problèmes spectraux

| Chemin | Octets | SHA-1 du blob Git |
| --- | ---: | --- |
| `data/Q_bound.mat` | 3808 | `4dac25bcd9eedc4b9199ff4f42cbc4df6aabc376` |
| `data/UP.mat` | 1403520 | `c0bb278bd6c1310d1d228937c9a4d77ffb055832` |
| `data/approx_Q.mat` | 2164632 | `d182fdcf919633bd842edcabaecc33b8b097c937` |
| `data/bessel_zeros.mat` | 48392 | `65bff3598fca59eae2fad36f0fb762f4e55ef32d` |
| `data/eig.mat` | 423079 | `5e966084e53fe95060614d1e00afd5e5f5c3dc07` |
| `data/eig_calc.mlx` | 3416 | `45aa1e795704ffdd9e8b3800caac3607964256c6` |
| `data/up_eig.mat` | 1400937 | `4c0a541caafa7d2b2930366126cd4bb2cabd30fa` |

Les 19 fichiers `data/phi_even/UP_phi_{0..18}.mat` ont chacun `1 813 176`
octets. Leurs SHA-1 Git, dans l'ordre numérique, sont :

```text
0 fd6a9b8e3d11d1be751b6c6b01e0016c08af771c
1 6a6bab30f367516926f0a549e222321c1b8ad2a2
2 bc7271c6ab6cc253504c9781632218644eaceb44
3 895e75679d461fd94e5cba66ec00d40841098938
4 6b42b5d93f49dba59dd2db5de87769355d10bb08
5 480725e48fd97ed906232712ce2d13110e804812
6 b13482f7f88d3bde0ca9b719e541784dec870e21
7 db0d483d833ec6fa5e948fba379e74798f4c64b3
8 c23a591db5f090aa7ea2375a94b735386dab59f4
9 654e1b902f4f688d379e2c4708141245d260dbc7
10 41449f4a22a1e2431586b3b039b7ead139c26f44
11 e7b802d426417de5294bd78102f8879b9c5c9ebd
12 e8713f3977852e30f2b26f286f29b72c72f320cf
13 bb6f81c7cce977e09fb07431bf71e87768129351
14 6f42007564c26fff43d83bdad99fb9fa86bc15ba
15 ec348ee062213b1f3fc7d74e44614cdf98344cef
16 170280490791c8949fc42fbebe6a8371fb51af75
17 6a73d50f1caf8a118b4293f6b3b8a3c37fe49fa4
18 14cd5816fd717693744c3cc40a4ffa329ddafa1e
```

Les 24 fichiers `data/phi_odd/up_phi_{0..23}.mat` ont chacun `1 811 984`
octets. Leurs SHA-1 Git, dans l'ordre numérique, sont :

```text
0 9c245e84c630648daddf0581759fe2318af3cda7
1 3c11f5d746d459ef80d101038da750a271cbab8b
2 db797ec23758ef7c7cc3db7dc4e62e8bcba5954e
3 3f0bd1d2e5dd578ad29cf1c590a24cf5e74f67c6
4 d5db480567e598ab806fa262daaf0cf8f7419a40
5 e035646262f421e4bd46cafef379731593c9d572
6 191dba2b3f9d4734b98722e4d315e3da0b77c24d
7 77ce738d4ccce85b4875e5935f64dc89b9a49011
8 8d5360caf32d65c1708b5682e0d5354e611f720f
9 547897cd9c8dd5c8e970b592e200011474da8a78
10 590c0b8c55dcc1692dab4fc916eaf6f78243eaf8
11 745303144173ce6eab162606ee3c0d99a293df25
12 865112bc6711b086ccced1c0af60b73c2d8f0286
13 db0d0682bb1655b9bb0856c40057033ecbb5cdbe
14 71d3c87303d00ddd8a5db27090f1024148109d9c
15 79ad37880655910a717733ad1c679e878fd089ca
16 ae3bdaf703d56a92cd951874996a0827e396312a
17 18bbe0832e88d245e57deaf4be9be3a5d7a40268
18 10e7c4b08c3537992b4810a12fe14263794f3ce3
19 517a3045dd04f18c2b93669c67e18670ca906fff
20 28be9010e64241ab565d6752946d12fd53382b51
21 c16f2f90e01fc735c81961e5e1e2d610cf27c6f4
22 3633e96c3e6a463b0f27911e0b08bad196fb3aca
23 b3ed2878e2e6599112b403b20634ab002672721c
```

Les contenus modérés ont été lus en mémoire, sans conservation locale. Leurs
SHA-256 de contenu sont :

- `UP.mat` : `c654a7f3ae86446e705d16ac925087c23fa6ca38931b9034770023b5de50bba3` ;
- `up_eig.mat` : `8b72114a0856615a15b206d0122072ed441b626df8ac1f781802dd08470e0843` ;
- `eig.mat` : `10e6cd12b1d8632e89597e161a5b0fec7bf8f57ac2bf893049a55f408459cd8b` ;
- `eig_calc.mlx` : `9c37bd0bb7c26916966fe9c5f2c84e3291495fc6c164fefc90d8a0f8428c28ce`.

## 3. Ce que contiennent réellement les données spectrales

`up_eig.mat` contient uniquement `lambda`, `p`, `scl_fac`, `shape`, `u1`,
`u2`, `u3`. Les champs de vitesse et pression sont stockés sur une grille
`300 x 150`; `scl_fac=22` et `shape=(4097,2049)`. Aucun champ gauche ou
adjoint n'est présent.

`eig.mat` contient `eig_val_even` de forme `(19,1)`, `eig_val_odd` de forme
`(24,1)`, `eig_vec_even` de forme `(1257,19)` et `eig_vec_odd` de forme
`(1260,24)`. Ce sont les eigenpairs généralisés de l'opérateur auxiliaire
compact/coercif `Q` qui construit l'approximation de rang fini. Ils ne sont
pas les vecteurs propres gauches et droits de `mathcal L_tildeU`.

`notebooks/eigenpair_error_analysis.ipynb` calcule bien le résidu droit

\[
 E^v=\bar U\cdot\nabla\bar v+\bar v\cdot\nabla\bar U
       -L_0\bar v-\bar\lambda\bar v,
\]

puis la quantité nommée `eig_T_up` par la formule littérale

```julia
eig_T_up = u_grad_T_U - U_grad_u - apply(lin_T_mat, up)
```

Cette quantité est `L*` appliqué au **même candidat droit** `up`; elle n'est
pas un candidat gauche `ell` et le notebook ne borne pas
`||L*ell-a ell||`. Les sorties stockées donnent
`||E^v||_2 in [1.65374e-5,1.86929e-5]` et
`||eig_T_up||_2 in [6.38757,6.38757]`. La seconde valeur n'est donc pas un
petit résidu adjoint. `src/NS_Terms.jl` sait construire certaines expressions
avec `transpose=true`, mais aucun solveur, fichier de coefficients ou
certificat de vecteur gauche ne complète cette infrastructure.

`notebooks/eigen_linear_operator_finite_rank.ipynb` charge le profil, le
candidat droit, les bases impaires auxiliaires et les 24 inversions
`up_phi_*`. Il impose une normalisation/orthogonalité et ferme le point fixe de
correction de l'eigenpair droit. Il ne calcule pas un projecteur de Riesz.
Le fichier intermédiaire `data/rhs.mat` qu'il consomme n'est pas versionné,
mais est engendré par `finite_rank_construction.ipynb`; son absence n'est donc
pas le verrou de projection identifié ici.

Une recherche insensible à la casse dans tous les `.jl`, `.ipynb`, le README
et `Project.toml` trouve zéro occurrence de `riesz`, `resolvent`, `semigroup`,
`spectral gap`, `left eigen` et `v^l`. `adjoint` apparaît seulement dans le
notebook d'erreur et les formules d'opérateur. Le code public implémente la
CAP de l'eigenpair droit, pas la théorie spectrale quantitative de la section
2.2 de l'article.

## 4. Riesz, semi-groupe et séparation dans l'article

La section 2.2 définit abstraitement

\[
 P_{\lambda_j}=\frac{1}{2\pi i}\int_{\Gamma_j}
     (\lambda-\mathcal L_{\widetilde U})^{-1}\,d\lambda,
\]

où `Gamma_j` entoure une valeur propre instable et aucune autre valeur
spectrale. Aucune coordonnée de contour, borne de résolvante, dimension de
`X_j`, matrice de Jordan ou norme de `P_j` n'est publiée.

Les estimations (2.14)--(2.16) portent des constantes cachées `lesssim`. Avec
`p=4`, l'article choisit

\[
 \delta=\tfrac12\min\{1/8,\min_j\Re\lambda_j\}>0.
\]

La CAP ne certifie qu'une valeur propre instable; elle n'énumère pas tous les
`lambda_j`. Ce `delta` ne devient donc pas un nombre certifié à partir des
données publiques. Le papier pose ensuite `alpha=1/4`, choisit un rayon de
localisation `R` tel que
`C sum_j R^(-alpha/2) <= 1/12`, puis `eta` tel que `C eta <= 1/4`.
Ni `C`, ni le nombre de modes, ni `R`, ni `eta` ne sont chiffrés. Le `R_0=32`
de la CAP est le support de l'auxiliaire coercif `Q` et n'est pas ce rayon.

La distinction finale est qualitative mais mathématiquement valide dans le
papier : deux solutions qui ont des coordonnées instables `P_j U(0)`
différentes à `t=1` sont distinctes. Elle ne fournit pas une borne inférieure
numérique sur leur distance dans une norme physique, encore moins une borne
uniforme après désingularisation du coeur initial.

La section 5.1 utilise des vecteurs gauche et droit dans une formule de
Hellmann--Feynman, sous l'hypothèse que la valeur propre numérique est simple
et isolée. Il s'agit de l'algorithme de découverte du candidat. L'hypothèse de
simplicité, le candidat gauche et sa validation ne sont pas repris dans la
Proposition 2. Il ne faut donc pas transférer cette hypothèse numérique au
théorème CAP.

## 5. Test exact de parité pour la couche intérieure

Soit `S` la réflexion vectorielle par rapport au plan `z=0` :

\[
 (Sg)(x,y,z)=\big(g_x(x,y,-z),g_y(x,y,-z),-g_z(x,y,-z)\big).
\]

L'article impose `S U=U` au profil et `S v=-v` à l'eigenfonction. Puisque la
réflexion préserve la divergence, le Laplacien et la projection de Leray,

\[
 S\mathcal L_{\widetilde U}=\mathcal L_{\widetilde U}S.
\]

Le résolvant et tout projecteur de Riesz bien défini commutent donc également
avec `S`. Si un bloc spectral est entièrement impair, son projecteur annule
tout champ pair.

La couche explicite du cycle 0010 est

\[
 g_\varepsilon(x)=f_\varepsilon(|x|)
 \frac{(-x_2,x_1,0)}{|x|^2}.
\]

Ses deux composantes horizontales sont paires en `z` et sa composante
verticale est nulle : `S g_epsilon=g_epsilon`. Ainsi sa projection sur le
**secteur spectral impair restreint** vaut exactement zéro. De façon
équivalente, tout vecteur propre adjoint impair `ell` donnerait

\[
 \langle\ell,g_\varepsilon\rangle_{L^2}=0.
\]

Ce résultat ne doit pas être surinterprété. La Proposition 2 certifie un
eigenpair impair mais ne certifie ni la simplicité ni l'absence d'un bloc pair
à la même valeur propre. Elle ne suffit donc pas à conclure que le projecteur
de Riesz **complet** autour de cette valeur a une image entièrement impaire.
Elle suffit seulement au test sectoriel nul. Pour une couche paire, ce test
révèle surtout qu'une régularisation respectant la symétrie ne peut exciter le
mode brisant la symétrie au premier ordre.

Conséquence pour le transfert vers Clay : des données initiales lisses paires
ont, tant que la solution classique unique existe, une évolution paire. Une
suite de telles évolutions ne sélectionne pas directement la branche impaire
de Hou–Wang–Yang. Pour tester cette branche par désingularisation, il faudrait
soit une perturbation impaire contrôlée et un nouveau lemme de raccord à une
même donnée limite, soit un mécanisme non linéaire démontré qui contourne le
test de parité. Les fichiers publics n'offrent ni l'un ni l'autre.

## 6. Pourquoi l'eigenpair droit ne suffit pas

Même lorsque `a` est simple et isolée, un opérateur non normal requiert un
eigenvecteur droit `v` et un eigenvecteur adjoint `ell` :

\[
 Pg=v\,\frac{\langle\ell,g\rangle}{\langle\ell,v\rangle}.
\]

Le contre-exemple fini-dimensionnel

\[
 A_K=\begin{pmatrix}1&K\\0&0\end{pmatrix},\qquad
 v=\binom10,\qquad \ell_K=\binom1K
\]

a le même eigenpair droit `(1,v)` pour tout `K`, tandis que pour `g=(0,1)`

\[
 P_Kg=K v.
\]

La projection peut donc être arbitrairement grande sans changer les données
de l'eigenpair droit. Si la valeur propre est multiple ou défectueuse, il faut
en plus un contour résolvant certifié ou une base de chaînes de Jordan. Cette
obstruction est logique, pas une limite de précision flottante.

La CAP ne livre par ailleurs que l'existence de corrections `U,v,lambda` dans
des boules normées autour des candidats, pas leurs coefficients exacts. Un
calcul ponctuel avec `up_eig.mat` ne deviendrait donc pas automatiquement une
borne sur la projection de l'opérateur exact.

## 7. Artefact minimal manquant

Pour une couche qui possède une composante impaire, le plus petit objet
réellement utile est un paquet machine-readable, par exemple
`unstable_riesz_certificate`, contenant ensemble :

1. les coefficients d'un candidat adjoint `ell` dans une représentation
   divergence-free compatible avec `up_eig.mat`, avec convention de produit
   scalaire et normalisation ;
2. une borne par intervalles du résidu
   `||L_tildeU^* ell-a ell||` qui inclut l'incertitude sur le profil exact ;
3. une borne inférieure strictement positive de
   `|<ell,v>|`, également pour l'eigenpair exact ;
4. soit un certificat de simplicité et de multiplicité algébrique un, soit un
   contour `Gamma`, une borne de résolvante sur ce contour et le rang du
   projecteur ;
5. une quadrature par intervalles de `<ell,g_epsilon>` pour la couche explicite,
   avec troncature spatiale, queue analytique et conventions de parité ;
6. si la cible est une séparation de branches, les normes de `P_j`, les
   constantes des estimations de semi-groupe et les constantes `C,R,eta`
   utilisées dans la contraction.

Un simple fichier de vecteur gauche suffirait à produire un nombre approché.
Il ne suffirait pas à le **certifier**. Les six éléments forment donc un seul
artefact minimal de certification; les éléments 1--5 suffisent au coefficient
de projection, et le sixième est nécessaire au raccord quantitatif vers une
séparation dynamique.

## 8. Test léger reproductible

Le test ci-dessous utilise uniquement la bibliothèque standard Python. Il ne
télécharge aucun `.mat`, ne lance ni Julia ni la CAP, vérifie l'identité de
l'arbre, les blobs décisifs, l'absence des artefacts spectraux annoncés et le
contre-exemple matriciel. Il n'a ni discrétisation, ni graine aléatoire, ni
erreur numérique autre que des égalités entières exactes.

```powershell
@'
import hashlib, json, urllib.request

REPO = "HouGroup2026/3d-navier-stokes-nonuniqueness"
COMMIT = "615ee6f3eca3abad7b5814fe9334bcd80bea0328"
API = "https://api.github.com/repos/" + REPO
HEADERS = {"User-Agent": "Millennium-Forge-readonly-audit"}

def get_json(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as response:
        return json.load(response)

def get_text(path):
    url = "https://raw.githubusercontent.com/" + REPO + "/" + COMMIT + "/" + path
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")

commit = get_json(API + "/git/commits/" + COMMIT)
assert commit["tree"]["sha"] == "723afb3838aa53a588193829d4e60000cfdf1b6b"
tree = get_json(API + "/git/trees/" + commit["tree"]["sha"] + "?recursive=1")
blobs = sorted((x for x in tree["tree"] if x["type"] == "blob"), key=lambda x: x["path"])
assert len(blobs) == 70
assert sum(x["size"] for x in blobs) == 84137370
manifest = "".join(f'{x["path"]}\t{x["size"]}\t{x["sha"]}\n' for x in blobs).encode()
assert hashlib.sha256(manifest).hexdigest() == "cde7bc4c6784d6c2b799714fd3ee034580cf3f3d28c42402da8ff20cf1274969"

by_path = {x["path"]: (x["size"], x["sha"]) for x in blobs}
assert by_path["data/up_eig.mat"] == (1400937, "4c0a541caafa7d2b2930366126cd4bb2cabd30fa")
assert by_path["data/eig.mat"] == (423079, "5e966084e53fe95060614d1e00afd5e5f5c3dc07")
assert by_path["notebooks/eigenpair_error_analysis.ipynb"] == (10373, "2b5fda4d14dcec85b585b4fbb36d3bafa358b08d")

paths = [x["path"] for x in blobs if x["path"].endswith((".jl", ".ipynb", ".md", ".toml"))]
corpus = "\n".join(get_text(path) for path in paths).lower()
for absent in ("riesz", "resolvent", "semigroup", "spectral gap", "left eigen", "v^l"):
    assert absent not in corpus, absent
formula = "eig_t_up = u_grad_t_u - u_grad_u - apply(lin_t_mat, up)"
assert formula in corpus

# Même eigenpair droit, projections arbitraires.
for K in (0, 1, 7, 1000):
    A = ((1, K), (0, 0)); v = (1, 0); ell = (1, K); g = (0, 1)
    assert (A[0][0]*v[0] + A[0][1]*v[1], A[1][0]*v[0] + A[1][1]*v[1]) == v
    assert ell[0]*v[0] + ell[1]*v[1] == 1
    Pg = (v[0]*(ell[0]*g[0] + ell[1]*g[1]), 0)
    assert Pg == (K, 0)

print("tree/blob/formula audit: PASS")
print("right-eigenpair insufficiency test: PASS")
print("CAP executed: NO; heavyweight files downloaded: NO")
'@ | python -
```

Sortie de référence :

```text
tree/blob/formula audit: PASS
right-eigenpair insufficiency test: PASS
CAP executed: NO; heavyweight files downloaded: NO
```

## 9. Décision scientifique

**Résultat négatif conservé.** La couche intérieure paire du cycle 0010 est
un mauvais test de couplage au mode instable impair : le couplage sectoriel
est exactement nul. Les données publiques sont insuffisantes pour remplacer
ce test par un coefficient de Riesz général et certifié.

**À abandonner :** toute inférence de projection ou de séparation quantitative
fondée sur `up_eig.mat` seul, sur `eig_T_up`, ou sur les eigenvecteurs
auxiliaires de `eig.mat`.

**À poursuivre :** construire une couche test explicitement impaire mais
divergence-free, puis demander ou reconstruire le paquet adjoint/Riesz minimal.
Le test décisif suivant est une borne par intervalles non nulle sur
`<ell,g_epsilon>/<ell,v>` accompagnée d'un certificat de simplicité/isolation.
Sans cet artefact, l'axe doit rester classé **À REPRENDRE**, et non être promu
comme transfert vers le problème Clay.
