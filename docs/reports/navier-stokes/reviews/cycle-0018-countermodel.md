# Cycle 0018 — passe adverse multi-échelle sur le commutateur localisé

Date : 2026-08-14.

Type de revue : **passe contradictoire par la même famille de modèle que
l'analyse principale; ce document n'est pas une revue externe indépendante**.

Source primaire auditée : Zoran Grujić,
[arXiv:2607.08866v2](https://arxiv.org/abs/2607.08866v2), version du 13 juillet
2026, théorème 4.1 et équations (8)–(22).

## Verdict

La loi d'échelle revendiquée

\[
 \|\alpha\|_{L^{3/2,\infty}(B_R)}
 \lesssim\frac1{|\log R|}
 \tag{1}
\]

**résiste** au contre-profil critique multi-échelle le plus défavorable testé :
vorticité de taille \(r_j^{-2}\) sur chaque anneau dyadique, oscillation de
direction de taille \(1/|\log r_j|\) par échelle, et dérive cumulative des
moyennes jusqu'à un ordre un entre \(R\) et \(\sqrt R\). Le poids géométrique
\(4^{-j}\) provenant du noyau de degré \(-3\) neutralise cette dérive et rend
la somme finale d'ordre \(1/|\log R|\).

Un défaut exact d'indexation est néanmoins trouvé aux lignes 191 et 209. Avec

\[
 N=\left\lfloor\frac12\log_2(1/R)\right\rfloor,
 \tag{2}
\]

l'anneau \(A_N=B_{2^{N+1}R}\setminus B_{2^NR}\) peut dépasser
\(R^{1/2}\). Pour \(R=2^{-2m}\), son rayon extérieur est
\(2R^{1/2}\), et

\[
 \phi(2^{N+1}R)=\frac1{(m-1)\log2}
 >\frac1{m\log2}=2\phi(R).
 \tag{3}
\]

L'inégalité utilisée à la ligne 209 est donc fausse littéralement. Elle se
répare soit en prenant \(N=m-1\) et en traitant le dernier anneau tronqué,
soit, pour \(|\log R|\geq4\log2\), en remplaçant \(2\phi(R)\) par
\(4\phi(R)\). Le résultat (1) et sa puissance ne changent pas.

La passe confirme aussi que :

- les moyennes \(c_k\) ne sont **pas** individuellement proches de \(c_0\) à
  l'ordre \(\phi(R)\) aux échelles externes ; leur dérive peut être d'ordre
  un ;
- la non-localité ne peut pas être supprimée : un paquet critique à distance
  \(R^{1/2}\) sature le terme macroscopique \(O(R)\) après restriction à
  \(B_R\) ;
- le passage restriction \(\mathrm{bmo}_\phi\) vers extension BMO est
  cohérent pour une boule, à condition de parler du **semi-norme BMO**, de
  suivre la constante d'extension uniforme par dilatation, et de ne pas
  exiger que l'extension reste unitaire ;
- plusieurs constantes et un facteur d'indice \(16/3\) sont cachés par les
  symboles \(\approx\) des équations (18)–(20).

Aucun contre-exemple au taux final (1) n'est produit. Le statut du maillon est
**RÉVISER**, non **ABANDONNER**.

## 1. Cadre exact et poids

On fixe

\[
 \phi(r)=\frac1{|\log r|},
 \qquad 0<r<1/2,
 \tag{4}
\]

et le semi-norme local

\[
 [\xi]_{\mathrm{bmo}_\phi}
 =\sup_{x,\,0<r<1/2}
 \frac1{\phi(r)}
 \frac1{|B_r(x)|}
 \int_{B_r(x)}|\xi-\xi_{B_r(x)}|.
 \tag{5}
\]

Le manuscrit ajoute \(\|\xi\|_\infty\) pour obtenir une norme. Pour une
direction de vorticité, \(|\xi|=1\) là où elle est définie, donc ce terme est
contrôlé. Dans toutes les estimations BMO de commutateur, c'est le semi-norme
modulo constantes qui intervient.

On note

\[
 r_j=2^jR,
 \qquad
 A_j=B_{2r_j}\setminus B_{r_j},
 \qquad
 c_j=\xi_{B_{r_j}}.
 \tag{6}
\]

Pour que toutes les boules utilisées restent dans le domaine du poids, il
faut un seuil uniforme tel que le dernier rayon agrandi soit inférieur à
\(1/2\). Avec l'indexation littérale du manuscrit, une condition simple est
\(2R^{1/2}<1/2\), soit \(R<1/16\).

## 2. Contre-profil de phase \(\log\log\)

Le profil radial borné

\[
 \xi_\eta(x)=
 \left(
 \cos\bigl(\eta\log\log(e/|x|)\bigr),
 \sin\bigl(\eta\log\log(e/|x|)\bigr),
 0
 \right)
 \tag{7}
\]

pour \(0<|x|<1/4\), prolongé de façon lisse et bornée au-delà, est le test
naturel. Sa phase n'a pas de limite à l'origine, mais une dilatation dyadique
à l'échelle \(r\) ne la modifie que de

\[
 \eta\left|
 \log\frac{\log(e/r)}{\log(e/(2r))}
 \right|
 =O\left(\frac{|\eta|}{|\log r|}\right).
 \tag{8}
\]

Un argument par oscillation radiale, puis l'inégalité
\(|e^{ia}-e^{ib}|\leq|a-b|\), donne

\[
 [\xi_\eta]_{\mathrm{bmo}_\phi}\leq C|\eta|.
 \tag{9}
\]

Ce profil appartient au type d'oscillation que le manuscrit entend
explicitement autoriser.

Pour \(R=2^{-2m}\), la différence de phase entre \(R\) et \(R^{1/2}\) vaut
asymptotiquement

\[
 \eta\log\frac{|\log R|}{|\log R^{1/2}|}
 =\eta\log2.
 \tag{10}
\]

Les moyennes de boule suivent la valeur à l'échelle extérieure à une erreur
\(O(\phi(r))\), car le volume radial est concentré près du bord. Il est donc
possible que

\[
 |c_N-c_0|\asymp |\eta|,
 \tag{11}
\]

alors que \(\phi(R)\to0\). Toute tentative de remplacer la somme télescopique
de (16) par \(|c_k-c_0|\lesssim\phi(R)\) uniformément en \(k\) est réfutée.

La preuve du manuscrit ne fait pas cette substitution : elle conserve la
somme des incréments, puis exploite le facteur \(4^{-k}\). C'est le point
structurel à tester.

## 3. Modèle annulaire critique multi-échelle

Sur chaque \(A_j\), plaçons une magnitude scalaire

\[
 \Omega_j\asymp M r_j^{-2}.
 \tag{12}
\]

Le volume cumulé jusqu'à l'échelle \(r_k\) est \(O(r_k^3)\), tandis que les
amplitudes décroissent comme \(r_k^{-2}\). Par conséquent,

\[
 \sup_{a>0}a\,|\{\Omega>a\}|^{2/3}\asymp M,
 \tag{13}
\]

uniformément dans le nombre d'anneaux. Ce profil est exactement compatible
avec l'échelle faible-\(L^{3/2}\).

L'incrément de direction à l'échelle \(r_j\) est pris de taille

\[
 d_j\asymp\phi(r_j).
 \tag{14}
\]

Une version scalaire en escaliers peut forcer les moyennes emboîtées à
vérifier \(c_j-c_{j-1}=d_j\). Pour respecter la condition VMO, on remplace
chaque saut par une rampe de largeur comparable à \(r_j\). Sur une boule de
rayon \(\rho\leq r_j\), son oscillation est alors contrôlée par

\[
 d_j\frac{\rho}{r_j}
 \lesssim\frac1{|\log\rho|}.
 \tag{15}
\]

Le profil de phase (7) fournit une réalisation bornée et unitaire de ce même
scaffold multi-échelle, à constantes près.

Ce modèle ne construit pas une vorticité Navier–Stokes divergence-free. Il
attaque exactement les majorations absolues de Lorentz et de BMO employées
dans (17)–(21). Les signes d'un composant de noyau de Calderón–Zygmund peuvent
être gardés fixes sur des secteurs coniques de proportion angulaire constante;
les lois d'échelle ne changent pas.

## 4. Dérive des moyennes : croissance réelle

Posons \(L=|\log R|\) et \(h=\log2\). L'estimation télescopique donne

\[
 D_k:=|c_{k+1}-c_0|
 \lesssim
 \sum_{j=1}^{k+1}\frac1{L-jh}.
 \tag{16}
\]

Pour \(k\) atteignant l'échelle \(R^{1/2}\),

\[
 \sum_{j=1}^{L/(2h)}\frac1{L-jh}
 \longrightarrow\frac{\log2}{h}=1
 \tag{17}
\]

à normalisation près. La dérive cumulative n'est donc pas petite. Le fait que
\(|\xi|=1\) fournit seulement la borne grossière \(|c_k-c_0|\leq2\), cohérente
avec (17).

La constante cachée dans chaque incrément provient du rapport de volumes

\[
 \frac{|B_{2r}|}{|B_r|}=8.
 \tag{18}
\]

Elle est indépendante de \(R\) mais doit multiplier
\([\xi]_{\mathrm{bmo}_\phi}\). Pour un champ vectoriel, l'estimation s'applique
composante par composante ou avec une constante dimensionnelle supplémentaire.

## 5. Pourquoi le poids \(4^{-k}\) sauve la somme

Sur \(A_k\), le noyau est \(O(r_k^{-3})\). La dualité
\(L^{3/2,\infty}\times L^{3,1}\) et John–Nirenberg donnent une norme
d'oscillation de taille

\[
 \|\xi-c_{k+1}\|_{L^{3,1}(A_k)}
 +\|c_{k+1}-c_0\|_{L^{3,1}(A_k)}
 \lesssim r_kD_k.
 \tag{19}
\]

Ainsi la contribution est

\[
 r_k^{-3}\,M\,(r_kD_k)
 =MR^{-2}4^{-k}D_k.
 \tag{20}
\]

La somme adverse maximale est donc

\[
 \begin{aligned}
 \mathcal S_N
 &=\sum_{k=1}^N4^{-k}
   \sum_{j=1}^{k+1}\phi(2^jR)\\
 &=\sum_{j=1}^{N+1}\phi(2^jR)
   \sum_{k=\max(1,j-1)}^N4^{-k}.
 \end{aligned}
 \tag{21}
\]

Pour \(j\geq2\),

\[
 \sum_{k=j-1}^{\infty}4^{-k}
 =\frac{16}{3}4^{-j}.
 \tag{22}
\]

Le symbole \(\approx\) entre les deux sommes de la ligne 208 cache donc un
facteur maximal \(16/3\), ainsi que le traitement séparé de \(j=1\). Ce
facteur est absolu.

Si l'on choisit l'index corrigé

\[
 N_{\rm corr}
 =\left\lfloor\frac{L}{2h}\right\rfloor-1,
 \tag{23}
\]

alors \(j\leq N_{\rm corr}+1\) implique \(L-jh\geq L/2\), et

\[
 \phi(2^jR)\leq2\phi(R).
 \tag{24}
\]

Comme \(\sum_{j\geq1}4^{-j}=1/3\), (21) donne

\[
 \mathcal S_{N_{\rm corr}}\leq C\phi(R).
 \tag{25}
\]

Le taux final est donc stable, même si le dernier \(D_k\) est d'ordre un.
Sans le facteur \(4^{-k}\), la dérive multi-échelle détruirait le gain.

## 6. Défaut d'indexation exact

Prenons \(R=2^{-2m}\), \(m\geq2\). Le choix du manuscrit donne \(N=m\), donc

\[
 2^{N+1}R=2^{1-m}=2R^{1/2}.
 \tag{26}
\]

Le poids au dernier rayon est

\[
 \phi(2^{N+1}R)=\frac1{(m-1)\log2},
 \tag{27}
\]

tandis que

\[
 \phi(R^{1/2})=2\phi(R)=\frac1{m\log2}.
 \tag{28}
\]

Le résidu signé de l'inégalité de la ligne 209 vaut exactement

\[
 \phi(2^{N+1}R)-2\phi(R)
 =\frac1{m(m-1)\log2}>0.
 \tag{29}
\]

Deux réparations sont possibles.

1. Remplacer \(N\) par \(N_{\rm corr}\) et couvrir séparément l'éventuel
   anneau tronqué jusqu'à \(R^{1/2}\).
2. Conserver \(N\). Si \(L\geq4h\), alors
   \(L/2-h\geq L/4\), donc
   \[
   \phi(2^{N+1}R)\leq4\phi(R).
   \tag{30}
   \]

Dans le cas dyadique exact, la somme pondérée reste même mieux contrôlée :

\[
 \sum_{j=1}^{m+1}
 \frac{4^{-j}}{(2m-j)\log2}
 \leq\frac{4}{3}\phi(R).
 \tag{31}
\]

L'erreur est donc une erreur de couverture et de constante, pas un
contre-exemple à (1).

## 7. Restriction \(\mathrm{bmo}_\phi\) et extension BMO

Pour toute boule \(B_\rho\subset B_{2R}\), avec \(2R<1/2\),

\[
 \frac1{|B_\rho|}\int_{B_\rho}|\xi-\xi_{B_\rho}|
 \leq[\xi]_{\mathrm{bmo}_\phi}\phi(\rho)
 \leq[\xi]_{\mathrm{bmo}_\phi}\phi(2R).
 \tag{32}
\]

Ainsi

\[
 [\xi]_{\mathrm{BMO}(B_{2R})}
 \leq C[\xi]_{\mathrm{bmo}_\phi}\phi(2R).
 \tag{33}
\]

La boule est un domaine uniforme. Le théorème d'extension BMO de Jones,
appliqué après translation et dilatation, fournit une extension
\(\widetilde\xi\) telle que

\[
 [\widetilde\xi]_{\mathrm{BMO}(\mathbb R^3)}
 \leq C_J[\xi]_{\mathrm{BMO}(B_{2R})},
 \tag{34}
\]

avec \(C_J\) indépendant de \(R\). Cette étape survit aux tests, avec quatre
précisions.

1. (34) contrôle un semi-norme modulo constantes. C'est suffisant puisque
   \([T,b+c]=[T,b]\).
2. L'extension n'a aucune raison de satisfaire \(|\widetilde\xi|=1\), ni de
   rester dans \(L^\infty\) avec norme \(1\). Ces propriétés ne sont pas
   utilisées par le commutateur proche.
3. Pour un champ vectoriel, on étend les composantes; une constante dépendant
   de la dimension peut apparaître.
4. L'identité du commutateur proche est exacte seulement parce que
   \(\omega_{in}\) est supportée dans \(B_{2R}\), que l'extension coïncide
   presque partout avec \(\xi\) sur cette boule, et que le point d'évaluation
   appartient à \(B_R\).

La phrase de la ligne 157 qualifiant les espaces Lorentz utilisés de
« reflexive » est incorrecte pour \(L^{3/2,\infty}\). Cela ne réfute pas la
borne : l'action forte du commutateur sur deux espaces \(L^{p_0}\),
\(L^{p_1}\) entourant \(3/2\), puis interpolation réelle, donne aussi le
contrôle dans \(L^{3/2,\infty}\). La justification doit être reformulée.

## 8. Non-localité : paquets adverses

La vorticité extérieure ne peut pas être ignorée. Plaçons un paquet de volume
\(\asymp d^3\), amplitude \(\asymp Md^{-2}\), à distance \(d\) du centre.
Sa quasi-norme faible-\(L^{3/2}\) est \(\asymp M\), tandis que sa contribution
absolue au noyau de degré \(-3\) sur \(B_R\) est

\[
 d^{-3}\,(Md^{-2})\,d^3
 \asymp Md^{-2}.
 \tag{35}
\]

Au seuil \(d=R^{1/2}\), cela vaut \(MR^{-1}\). La norme restreinte d'une
constante sur \(B_R\) dans \(L^{3/2,\infty}\) apporte \(R^2\), d'où

\[
 \|I_{2,far}\|_{L^{3/2,\infty}(B_R)}
 \asymp MR.
 \tag{36}
\]

C'est exactement la loi de (15). Elle est plus petite que
\(M\phi(R)\), mais elle n'est pas nulle. Un paquet encore plus lointain
décroît comme \(d^{-2}\).

Le même calcul à l'échelle \(d=r_k\), avec l'oscillation cumulative \(D_k\),
donne \(MR^{-2}4^{-k}D_k\), ce qui sature le scaffold de la section 5. Les
estimations non locales ont donc les bonnes puissances; leur suppression ou
leur remplacement par une donnée purement locale serait faux.

## 9. Audit des normes et facteurs

Les facteurs suivants doivent être conservés dans une version quantitative.

| Étape | Facteur ou condition cachée |
|---|---|
| restriction pondérée | \([\xi]_{\mathrm{bmo}_\phi}\) et comparaison \(\phi(2R)\leq C\phi(R)\) |
| extension Jones | constante \(C_J\) uniforme pour les boules dilatées |
| CRW/Lorentz | norme de l'opérateur singulier, constante de commutateur et interpolation vers \(q=\infty\) |
| Lorentz–Hölder | constante dépendant de la normalisation des quasi-normes |
| constante sur \(A_k\) | avec \(\|f\|_{L^{3,1}}=\int s^{1/3}f^*(s)ds/s\), \(\|1_{A_k}\|_{L^{3,1}}=3|A_k|^{1/3}\) |
| John–Nirenberg | constante du passage BMO vers \(L^4\) |
| moyennes emboîtées | rapport volumique exact \(8\) en dimension trois |
| inversion de la double somme | facteur maximal \(16/3\) dans (22) |
| dernier anneau | correction (23) ou facteur \(4\) de (30) |
| restriction finale | \(\|1_{B_R}\|_{L^{3/2,\infty}}=|B_R|^{2/3}=(4\pi/3)^{2/3}R^2\) sous la convention du supremum |

La constante \(C_0\) de (8) dépend donc de

\[
 \|\omega\|_{L_t^\infty L_x^{3/2,\infty}},
 \quad
 [\xi]_{L_t^\infty\mathrm{bmo}_\phi},
 \quad
 C_J,
 \quad
 \text{constantes CZ, Lorentz et John–Nirenberg}.
 \tag{37}
\]

Elle ne dépend pas d'une norme \(L^\infty_x\) de la vorticité. La formulation
de la ligne 146, « depends exclusively on the \(L^\infty_t\) suprema of
\(\omega\) and \(\xi\) », doit être lue avec les espaces spatiaux complets,
sinon elle est ambiguë.

## 10. Échelle

Sous la remise à l'échelle critique

\[
 \omega_\kappa(x)=\kappa^2\omega(\kappa x),
 \qquad R_\kappa=R/\kappa,
 \tag{38}
\]

la quasi-norme \(L^{3/2,\infty}\) de \(\omega\) est invariante. Le noyau de
degré \(-3\), le volume annulaire et l'amplitude critique donnent

\[
 r_j^{-3}\cdot r_j^{-2}\cdot r_j^3=r_j^{-2},
 \tag{39}
\]

puis la restriction à \(B_R\) apporte \(R^2\). Le résultat est sans dimension,
comme le facteur \(\phi(R)\) après choix d'une longueur de référence.

Le logarithme doit en réalité s'écrire
\(\phi(R)=1/|\log(R/R_*)|\). Sous dilatation,
\(R_*\) doit se transformer comme une longueur. L'écriture \(|\log R|\)
suppose la nondimensionnalisation du manuscrit.

## 11. Certificat exact standard-library

Le script ci-dessous encode le cas dyadique \(R=2^{-2m}\). Le facteur commun
\((\log2)^{-1}\) est supprimé, de sorte que toutes les vérifications utilisent
`fractions.Fraction`. Il certifie :

- le résidu positif de l'inégalité fausse (3) ;
- la dérive non petite des moyennes ;
- la compensation exacte de cette dérive par \(4^{-k}\) ;
- la compatibilité faible-\(L^{3/2}\) des amplitudes/volumes annulaires ;
- la loi d'échelle du paquet non local.

```python
from fractions import Fraction as F


def phi_coeff(m, j):
    """log(2) * phi(2^j R), for R=2^(-2m)."""
    return F(1, 2 * m - j)


def mean_drift(m, k):
    return sum((phi_coeff(m, j) for j in range(1, k + 2)), F(0))


def weighted_mid_sum(m):
    return sum((F(1, 4 ** k) * mean_drift(m, k)
                for k in range(1, m + 1)), F(0))


for m in range(2, 65):
    phi_R = F(1, 2 * m)
    phi_last = phi_coeff(m, m + 1)

    # Literal line-209 gate fails by an exact positive residual.
    residual = phi_last - 2 * phi_R
    assert residual == F(1, m * (m - 1))
    assert residual > 0

    # Repaired endpoint bound and weighted double-sum bound.
    assert phi_last <= 4 * phi_R
    S = weighted_mid_sum(m)
    assert S <= F(28, 9) * phi_R

    # The unweighted terminal drift is not O(phi_R): its ratio grows.
    terminal_ratio = mean_drift(m, m) / phi_R
    assert terminal_ratio >= m


# Critical shell family: r_j=2^j, amplitude=4^(-j), shell volume=8^j.
# Cubing the weak-L^(3/2) expression avoids fractional powers:
# [amplitude * cumulative_volume^(2/3)]^3 = amplitude^3 * volume^2.
for k in range(0, 20):
    amplitude = F(1, 4 ** k)
    cumulative_volume = F(8 ** (k + 1) - 1, 7)
    weak_cube = amplitude ** 3 * cumulative_volume ** 2
    assert weak_cube < F(64, 49)

    # kernel r^-3 * amplitude r^-2 * volume r^3 = 4^-j.
    kernel = F(1, 8 ** k)
    shell_volume = F(8 ** k)
    contribution = kernel * amplitude * shell_volume
    assert contribution == F(1, 4 ** k)


# Remote packet at d=q: kernel q^-3, amplitude q^-2, volume q^3 -> q^-2.
for q in (2, 4, 8, 16, 32):
    remote = F(1, q ** 3) * F(1, q ** 2) * F(q ** 3)
    assert remote == F(1, q ** 2)

print("dyadic endpoint residual and repaired bound: PASS")
print("mean-drift versus weighted-tail compensation: PASS")
print("critical shells and nonlocal scaling: PASS")
```

Commande de reproduction : extraire le bloc et exécuter `python -` depuis la
racine du dépôt. Dépendances : bibliothèque standard uniquement. Graine :
aucune. Les résidus sont rationnels exacts; aucune arithmétique flottante
n'intervient.

## 12. Obligations falsifiables

```json
{
  "cycle": "0018",
  "review_independence": "same-model-family adversarial pass; not external independent review",
  "source": "arXiv:2607.08866v2, equations (8)-(22)",
  "claims": [
    {
      "id": "NS-C0018-MID-LOG-RATE",
      "statement": "the weighted multi-scale mid tail is O(1/abs(log R))",
      "status": "SURVIVES_ADVERSARIAL_MODEL",
      "requirements": ["critical weak-L^(3/2) norm", "bmo_phi increments", "kernel weight 4^(-k)"]
    },
    {
      "id": "NS-C0018-MEAN-DRIFT-SMALL",
      "statement": "all nested mean drifts are O(phi(R)) up to the sqrt(R) scale",
      "status": "REFUTED",
      "witness": "log-log phase profile and harmonic dyadic sum"
    },
    {
      "id": "NS-C0018-LAST-ANNULUS",
      "statement": "the literal N=floor(log2(1/R)/2) keeps A_N inside radius sqrt(R) and phi <= 2 phi(R)",
      "status": "REFUTED",
      "exact_residual": "1/[m(m-1) log 2] for R=2^(-2m)",
      "repair": "N_corr=N-1 plus truncated annulus, or factor 4"
    },
    {
      "id": "NS-C0018-BMO-EXTENSION",
      "statement": "restriction to B_(2R) has a global BMO extension with R-uniform seminorm constant",
      "status": "SURVIVES_WITH_CLARIFICATIONS",
      "clarifications": ["seminorm modulo constants", "componentwise extension", "no unit-length preservation"]
    },
    {
      "id": "NS-C0018-NONLOCAL-PACKET",
      "statement": "far-field vorticity is negligible without calculation",
      "status": "REFUTED",
      "witness": "critical packet at distance sqrt(R) gives restricted size O(R)"
    }
  ],
  "pde_scope": "functional Calderon-Zygmund/BMO countermodels; no Navier-Stokes simulation or solution is constructed",
  "decision": "REVISE"
}
```

## Conclusion contradictoire

Le profil \(\log\log\) confirme l'obstacle réel : les moyennes emboîtées
peuvent dériver macroscopiquement malgré une oscillation locale
\(1/|\log r|\). La preuve ne survit que parce que le noyau fournit exactement
le poids sommable \(4^{-k}\). Ce mécanisme résiste au test annulaire critique.
La faute détectée dans le dernier anneau est exacte et reproductible, mais se
répare par une modification d'indice ou de constante. Le prochain audit
devrait donc viser la validité PDE du commutateur unidirectionnel (6)–(7) et
la définition globale de la direction aux zéros, plutôt que réattaquer la
somme dyadique après correction.
