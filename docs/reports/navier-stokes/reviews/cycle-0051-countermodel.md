# Cycle 0051 — fuite basse fréquence et faux raccord Littlewood–Paley

Date d'exécution : 2026-08-15

## Verdict

Le contrôle uniforme faible-\(L^3\), un cocycle exact et une formule de Duhamel de type semi-groupe ne suffisent pas, à eux seuls, à produire une tightness \(L^2\) lorsque le temps de base tend vers \(-\infty\).

Le contre-test reste explicitement fonctionnel. Il utilise

\[
U(x)=\frac{(-x_2,x_1,0)}{|x|^2},
\qquad
D_T=(I-e^{T\Delta})U.
\]

La famille \(D_T\) est uniformément bornée dans \(L^{3,\infty}\), chaque \(D_T\) appartient à \(L^2\), et elle satisfait un cocycle ainsi qu'un Duhamel calorique exact. Pourtant,

\[
\|D_T\|_2=C_UT^{1/4}\to\infty.
\]

Le ledger dyadique montre que cette croissance est une fuite vers les basses fréquences \(|\xi|\simeq T^{-1/2}\). Toute preuve qui passe la limite de base sous une somme de Littlewood–Paley doit donc fournir une domination sommable uniforme absente du seul endpoint faible-\(L^3\).

Aucune solution forward auto-similaire de Navier–Stokes n'est utilisée : un tel résultat, même disponible sous des hypothèses adaptées, vit pour \(t>0\) et ne fournit pas automatiquement une solution ancienne, une énergie de correcteur uniforme, ni le raccord de suitability nécessaire. Le champ \(U\) lui-même n'est pas une solution stationnaire Navier–Stokes non forcée.

## 1. Trois propriétés exactes, mais insuffisantes

Le semi-groupe est borné sur \(L^{3,\infty}\). Par quasi-inégalité triangulaire,

\[
\sup_{T>0}\|D_T\|_{L^{3,\infty}}
\lesssim \|U\|_{L^{3,\infty}}<\infty.
\]

Le cocycle est

\[
D_{T+H}=D_T+e^{T\Delta}D_H,
\]

et, pour trois durées,

\[
D_{T+H+K}
=D_T+e^{T\Delta}D_H+e^{(T+H)\Delta}D_K.
\]

Enfin, dans les distributions tempérées,

\[
D_T
=-\int_0^T\Delta e^{s\Delta}U\,ds
=\int_0^Te^{s\Delta}(-\Delta U)\,ds.
\]

Il s'agit d'une formule de Duhamel linéaire exacte. Le terme \(-\Delta U\) n'est pas identifié à la non-linéarité \(-\mathbb P\nabla\cdot(U\otimes U)\), et la famille n'est pas une solution de Navier–Stokes. Le contre-test réfute l'implication fonctionnelle, pas un théorème PDE qui utiliserait réellement l'équation, la pression et la suitability.

## 2. Mesure spectrale critique

À une constante angulaire et de Fourier positive \(A_U\) près,

\[
|\widehat U(\xi)|^2\,d\xi
\leadsto \rho^{-2}\,d\rho.
\]

Indexons les coquilles vers les basses fréquences par

\[
I_j=[2^{-j-1},2^{-j}],
\qquad j\in\mathbb Z.
\]

Plus \(j\) est grand, plus la fréquence est basse. La masse \(L^2\) formelle non filtrée d'une coquille vaut exactement

\[
w_j:=\int_{I_j}\rho^{-2}\,d\rho=2^j.
\]

Chaque bloc est fini, mais

\[
\sum_{j=0}^Jw_j=2^{J+1}-1\xrightarrow[J\to\infty]{}\infty.
\]

C'est la divergence infrarouge correspondant à la queue spatiale \(|x|^{-1}\). La finitude bloc par bloc ne donne aucune sommabilité basse fréquence.

## 3. Défaut calorique aux temps \(T_n=4^n\)

La contribution radiale réelle de la coquille \(I_j\) est

\[
H_{n,j}=
\int_{I_j}
(1-e^{-4^n\rho^2})^2\rho^{-2}\,d\rho.
\]

Pour tout \(x\ge0\),

\[
\frac12\min(1,x)
\le 1-e^{-x}
\le \min(1,x).
\tag{1}
\]

La borne inférieure découle de \(1-e^{-x}\ge x/2\) sur \([0,1]\) et de \(1-e^{-1}>1/2\). Elle n'utilise aucune approximation numérique.

Le seuil calorique est \(j=n\). Sur les coquilles \(j<n\), le multiplicateur est saturé et

\[
\frac14w_j\le H_{n,j}\le w_j.
\]

Sur les coquilles \(j\ge n\), (1) et l'identité

\[
\int_{I_j}\rho^2\,d\rho
=\frac{7}{24}2^{-3j}
\]

donnent

\[
\frac{7}{96}16^n2^{-3j}
\le H_{n,j}
\le\frac{7}{24}16^n2^{-3j}.
\]

En sommant exactement,

\[
\sum_{j<n}2^j=2^n,
\qquad
\sum_{j\ge n}2^{-3j}=\frac87,2^{-3n}.
\]

Par conséquent,

\[
\boxed{
\frac13,2^n
\le \sum_{j\in\mathbb Z}H_{n,j}
\le \frac43,2^n.}
\tag{2}
\]

Le facteur fixe \(A_U\) a été retiré. La largeur résiduelle certifiée de l'encadrement est exactement \(2^n\), soit une unité après normalisation par \(2^n\). La formule radiale fermée du cycle 0050 donne plus précisément

\[
\sum_jH_{n,j}=\sqrt\pi(2-\sqrt2)2^n,
\]

compatible avec (2). Ainsi \(\|D_{4^n}\|_2^2\asymp2^n\) et \(\|D_{4^n}\|_2\asymp2^{n/2}=T_n^{1/4}\).

## 4. Proxy dyadique rationnel exact

Pour auditer les séries sans exponentielle flottante, définissons

\[
m_{n,j}=\min(1,4^n2^{-2j}),
\qquad
P_{n,j}=2^jm_{n,j}^2.
\]

Alors

\[
\sum_{j<n}P_{n,j}=2^n,
\]

et

\[
\sum_{j\ge n}P_{n,j}
=16^n\sum_{j\ge n}2^{-3j}
=\frac87,2^n.
\]

La masse totale du proxy est donc exactement

\[
\boxed{P_n=\frac{15}{7}2^n.}
\]

Pour la somme tronquée

\[
P_{n,J}=\sum_{j\le J}P_{n,j},
\]

on obtient

\[
P_{n,J}=
\begin{cases}
2^{J+1},&J<n,\\[2mm]
2^n+\dfrac87,2^n
\left(1-8^{-(J-n+1)}\right),&J\ge n.
\end{cases}
\tag{3}
\]

Le programme vérifie (3) contre les sommes finies pour 126 couples \((n,J)\), en arithmétique rationnelle exacte.

## 5. Ordres de limites non commutatifs

Normalisons par l'échelle d'énergie \(2^n\). Pour tout \(n\) fixé,

\[
\lim_{J\to\infty}\frac{P_{n,J}}{2^n}=\frac{15}{7}.
\]

Pour tout \(J\) fixé et \(n>J\), (3) donne

\[
\frac{P_{n,J}}{2^n}=2^{J+1-n}\xrightarrow[n\to\infty]{}0.
\]

Donc

\[
\boxed{
\lim_{n\to\infty}\lim_{J\to\infty}\frac{P_{n,J}}{2^n}
=\frac{15}{7},
\qquad
\lim_{J\to\infty}\lim_{n\to\infty}\frac{P_{n,J}}{2^n}
=0.}
\]

Équivalemment, pour tout cutoff fréquentiel fixé \(J\),

\[
\sup_{n>J}
\frac{P_n-P_{n,J}}{2^n}
=\frac{15}{7}.
\]

Chaque défaut à base fixée a une queue très basse fréquence sommable, mais aucune sélection de \(J\) ne rend cette queue petite uniformément lorsque la base recule. Le vrai multiplicateur calorique possède la même non-commutation, avec la constante positive \(\sqrt\pi(2-\sqrt2)\) à la place de \(15/7\).

## 6. Version spatiale de la fuite

La similitude exacte est

\[
D_T(x)=T^{-1/2}D_1(x/\sqrt T).
\]

La famille renormalisée

\[
\widetilde D_T=T^{-1/4}D_T
=T^{-3/4}D_1(x/\sqrt T)
\]

a une norme \(L^2\) constante. Pourtant, pour tout \(R<\infty\),

\[
\int_{B_R}|\widetilde D_T|^2\,dx
=\int_{B_{R/\sqrt T}}|D_1(y)|^2\,dy
\xrightarrow[T\to\infty]{}0.
\]

Toute la masse normalisée quitte donc les boules fixes. La famille n'est pas tight dans \(L^2\), même après suppression de la croissance de norme. La fuite basse fréquence et la fuite vers les grandes échelles spatiales sont les deux faces de la même dilation.

## 7. Faux usages de Littlewood–Paley à l'endpoint

Le contre-test exclut les étapes suivantes sans hypothèse supplémentaire :

1. **Bloc fini \(\Rightarrow\) somme uniforme.** Chaque \(\Delta_jD_T\) est dans \(L^2\), mais la constante de la somme dépend de \(T\).
2. **Convergence terme à terme \(\Rightarrow\) convergence de la somme.** Après normalisation, chaque ensemble fini de blocs tend vers zéro, tandis que la somme complète reste positive.
3. **Faible-\(L^3\) \(\Rightarrow\ell^2(L^2)\).** La borne faible critique ne donne pas \(\sum_j\|\Delta_jf\|_2^2<\infty\) uniformément aux basses fréquences.
4. **Bernstein dans le mauvais sens.** Sur \(\mathbb R^3\), une localisation fréquentielle ne permet pas de convertir gratuitement un contrôle \(L^{3,\infty}\) en contrôle global \(L^2\) ; le passage demandé va vers un exposant plus petit et exige une information spatiale.
5. **Norme de fonction carrée \(\Rightarrow\) somme des normes.** Un contrôle de \(\|(\sum_j|\Delta_jf|^2)^{1/2}\|_{L^{3,\infty}}\) ne justifie pas l'échange avec \((\sum_j\|\Delta_jf\|_{L^{3,\infty}}^2)^{1/2}\).
6. **Queue petite pour chaque base \(\Rightarrow\) queue uniformément petite.** Cette inversion est exactement réfutée par (3).
7. **Cocycle \(\Rightarrow\) Cauchy.** L'identité algébrique ne fournit ni sommabilité, ni tightness, ni compacité forte.

## 8. Test Duhamel et cocycle rationnel

Le script vérifie séparément, pour plusieurs \(q\in\mathbb Q\cap(0,1)\), l'identité discrète

\[
1-q^N=(1-q)\sum_{s=0}^{N-1}q^s
\]

et le cocycle triple

\[
1-q^{a+b+c}
=(1-q^a)+q^a(1-q^b)+q^{a+b}(1-q^c).
\]

Toutes les égalités sont exactes dans `Fraction`. Ce test ne remplace pas le semi-groupe de la chaleur ; il isole le fait logique que Duhamel et cocycle sont des identités algébriques ne contenant, par elles-mêmes, aucune estimation compacte des modes \(q\uparrow1\).

## 9. Pourquoi aucune branche auto-similaire NS n'est revendiquée

Une solution forward auto-similaire hypothétique issue d'une donnée homogène de degré \(-1\) aurait l'échelle

\[
u(t,x)=t^{-1/2}F(x/\sqrt t).
\]

Mais la présente question concerne une limite de bases anciennes, la pression de Riesz, la suitability locale et une énergie globale de correcteur. Une existence pour \(t>0\) ne fournit aucune de ces arêtes sans un lemme de raccord séparé. De plus, le générateur \(U\) utilisé ici échoue directement à l'équation stationnaire non forcée. Importer une branche forward dans ce contre-test créerait donc précisément la confusion de quantificateurs qu'il cherche à détecter.

## 10. Portée, reproduction et résidu

Le certificat porte sur les masses spectrales, les séries géométriques, les enveloppes rationnelles du vrai multiplicateur calorique, les ordres de limites et l'algèbre Duhamel/cocycle. Il ne certifie ni solution de Navier–Stokes, ni suitability, ni pression, ni singularité.

Commande :

```powershell
python -B experiments/navier-stokes/low-frequency-tail/low_frequency_tail_audit.py
```

Sortie validée :

```text
low_frequency_tail_audit: PASS
exact_assertions=615
proxy_total=(15/7)*2^n for T_n=4^n
true_heat_bounds=(1/3)*2^n <= radial_energy <= (4/3)*2^n
limit_order=frequency_then_base:15/7, base_then_frequency:0
LP_endpoint=finite_blocks_do_not_give_uniform_low_frequency_sum
scope=functional heat ledger; no forward self-similar or ancient NS claim
```

Résidu des 615 assertions rationnelles : zéro. Largeur résiduelle de l'enveloppe calorique : \(2^n\), exactement une après normalisation. Écart entre les deux ordres de limites du proxy : \(15/7\).

Empreinte SHA-256 du script validé :

```text
5d6aa3c61cd3a67445c7e1eb760d704b581c54acb43afe12b329d5d21e5b19c2
```

## Décision contradictoire

**ABANDONNER** toute déduction de tightness \(L^2\) ancienne fondée seulement sur faible-\(L^3\), cocycle et Duhamel. **CONTINUER** uniquement si le prochain lemme apporte une annulation PDE basse fréquence, une condition uniforme de moment/queue, ou une estimation de suitability qui produit un dominateur sommable indépendant du temps de base.
