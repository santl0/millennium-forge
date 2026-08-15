# Cycle 0053 — audit des hypothèses d'une sous-suite stationnaire

Date d'exécution : 2026-08-15

## Verdict

Quatre hypothèses logiquement distinctes sont nécessaires avant de promouvoir une suite d'objets critiques vers une limite stationnaire non triviale :

1. une compacité spatiale critique ou une dissipation uniforme ;
2. une tightness empêchant la masse de fuir hors du repère fixé ;
3. l'annulation effective du générateur temporel, et non une simple récurrence ;
4. une extraction diagonale emboîtée, avec le bon ordre des quantificateurs.

Les quatre contre-tests exacts ci-dessous montrent qu'aucune de ces portes ne découle automatiquement des trois autres. Ils sont fonctionnels ou de dimension finie. Aucun objet construit n'est présenté comme une solution de Navier–Stokes, ancienne ou non.

## 1. Concentration critique sans dissipation uniforme

Soit \(A\in C_c^\infty(B_{1/4};\mathbb R^3)\), non nul et divergence-free. Par exemple, on peut prendre

\[
A=\nabla\times(0,0,\psi)
\]

avec \(\psi\in C_c^\infty(B_{1/4})\) non constante. Définissons

\[
C_n(x)=nA(nx).
\]

La divergence reste nulle. La fonction de distribution satisfait

\[
|\{|C_n|>\lambda\}|
=n^{-3}|\{|A|>\lambda/n\}|.
\]

Par conséquent,

\[
\|C_n\|_{L^{3,\infty}}
=\|A\|_{L^{3,\infty}}.
\]

Comme \(\operatorname{supp}C_n\subset B_{1/(4n)}\subset B_1\), toute la masse forte critique reste dans la boule unité :

\[
\int_{B_1}|C_n|^3\,dx
=\int_{\mathbb R^3}|A|^3\,dx>0.
\]

Les trois autres lois d'échelle pertinentes sont

\[
\|C_n\|_2^2=n^{-1}\|A\|_2^2,
\]

\[
\|\nabla C_n\|_2^2
=n\|\nabla A\|_2^2,
\]

et

\[
|\operatorname{supp}C_n|
=n^{-3}|\operatorname{supp}A|.
\]

Ainsi la dissipation homogène \(\dot H^1\) au carré croît linéairement. Hors de l'origine, \(C_n(x)=0\) pour tout \(n\) assez grand ; la limite presque partout est donc zéro. Une convergence forte dans \(L^3(B_1)\) imposerait alors

\[
\|C_n\|_{L^3(B_1)}\to0,
\]

en contradiction avec la masse constante.

Portée précise : ce profil détruit la précompacité forte au niveau critique \(L^3\) et toute application d'une borne uniforme \(L^2_t\dot H^1_x\). Il ne détruit pas toute compacité sous-critique : en particulier, \(C_n\to0\) fortement dans \(L^2\). Le défaut pertinent est la perte de la masse critique et du passage compact dans les termes non linéaires.

## 2. Translation stationnaire mais non tight

Avec le même atome \(A\), posons

\[
T_n(t,x)=A(x-2ne_1).
\]

Chaque membre est indépendant du temps :

\[
\partial_tT_n=0.
\]

Toutes les normes invariantes par translation, notamment \(L^{3,\infty}\), \(L^3\), \(L^2\) et \(\dot H^1\), sont constantes. Cependant,

\[
\operatorname{supp}T_n
\subset B_{1/4}(2ne_1),
\]

donc, dès \(n\ge1\),

\[
\int_{B_1}|T_n|^p\,dx=0
\]

pour tout \(p>0\). Plus généralement, pour chaque rayon \(R<\infty\), on peut choisir \(n>R\) de sorte que toute la masse soit hors de \(B_R\).

Le générateur nul ne fournit donc aucune tightness spatiale. Dans le repère fixé, la suite converge localement vers zéro. Elle possède bien une limite stationnaire, mais cette limite est triviale ; le contre-test vise exactement toute conclusion de **stationnarité non triviale** qui oublierait la rétention de masse dans une boule commune.

Un recentrage par \(2ne_1\) récupère l'atome, mais change le choix de repère. Un tel recentrage doit faire partie explicitement des hypothèses et rester compatible avec la pression, les temps de base et les autres normalisations.

## 3. Récurrence exacte sans stationnarité

Considérons le système linéaire

\[
z'(t)=Jz(t),
\qquad
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad
z(0)=\binom10.
\]

Sa solution est

\[
z(t)=\binom{\cos t}{\sin t}.
\]

Elle satisfait la récurrence exacte

\[
z(t+2\pi m)=z(t)
\]

pour tout entier \(m\), mais

\[
\|z'(t)\|^2=\|Jz(t)\|^2=1.
\]

En particulier, les translates temporels aux temps \(2\pi m\) reproduisent exactement la même orbite périodique, pas un état stationnaire. Même le quotient sur une période,

\[
\frac{z(t+2\pi)-z(t)}{2\pi}=0,
\]

ne contrôle pas le générateur instantané. La moyenne vectorielle de \(z'\) sur une période est nulle, tandis que sa moyenne quadratique vaut un.

Le script évite toute approximation trigonométrique : il échantillonne les temps \(t=m\pi/2\), pour lesquels

\[
(1,0)\mapsto(0,1)\mapsto(-1,0)\mapsto(0,-1)\mapsto(1,0),
\]

et vérifie exactement \(Jz_m=z_{m+1}\), \(z_{m+4}=z_m\) et \(\|Jz_m\|^2=1\).

Conclusion logique : une hypothèse de récurrence doit être complétée par un défaut de générateur tendant vers zéro dans une topologie assez forte pour passer à l'équation limite.

## 4. Diagonale emboîtée : ce qu'elle donne réellement

Pour \(j\ge1\), définissons le défaut binaire

\[
d_j(n)=
\begin{cases}
0,&2^j\text{ divise }n,\\
1,&\text{sinon}.
\end{cases}
\]

Les ensembles

\[
S_j=\{n:d_j(n)=0\}
\]

sont emboîtés : \(S_{j+1}\subset S_j\). La diagonale

\[
n_m=2^m
\]

vérifie, pour chaque \(j\) fixé,

\[
d_j(n_m)=0
\qquad\text{dès que }m\ge j.
\]

C'est le bon mécanisme d'une extraction diagonale sur une famille dénombrable de tests.

Mais le défaut mobile reste

\[
d_{m+1}(n_m)=1.
\]

La diagonale donne donc une convergence **test fixé par test fixé**, et non

\[
\sup_jd_j(n_m)\to0.
\]

Toute étape ultérieure exigeant une uniformité sur les rayons, les temps, les fréquences ou les fonctions test ne peut pas être obtenue par la seule diagonale.

## 5. Pourquoi les sous-suites doivent être réellement emboîtées

Définissons deux autres défauts :

\[
e_0(n)=0\quad\text{si }n\text{ est pair},
\qquad
e_1(n)=0\quad\text{si }n\text{ est impair}.
\]

Chacun s'annule sur une sous-suite infinie. Pourtant,

\[
e_0(n)+e_1(n)=1
\]

pour tout \(n\), et leurs ensembles de zéros sont disjoints. Ainsi

\[
\forall j\ \exists\text{ une sous-suite annulant }e_j
\]

n'implique pas

\[
\exists\text{ une sous-suite commune annulant tous les }e_j.
\]

À chaque étape d'un argument PDE, la nouvelle extraction doit être une sous-suite de toutes les extractions précédentes. Il faut ensuite vérifier que les bornes nécessaires au passage de la famille dense de tests à tous les tests sont uniformes ; la diagonalisation ne fournit pas cette continuité.

## 6. Hypothèses minimales révélées par les contre-tests

Un lemme crédible de sous-suite stationnaire non triviale doit au moins distinguer :

1. **Compacité critique.** Une borne locale de dissipation ou un substitut excluant les concentrations \(C_n\), avec une topologie assez forte pour le terme quadratique.
2. **Tightness spatiale.** Une masse conservée dans une boule commune, ou un recentrage contrôlé et explicitement fixé.
3. **Défaut temporel.** Une quantité mesurant réellement le générateur et tendant vers zéro ; la récurrence de l'état ou la moyenne signée ne suffit pas.
4. **Extraction emboîtée.** Une suite unique satisfaisant les contraintes précédentes pour tout indice fixé.
5. **Stabilité PDE.** Contrôle de la pression, passage du produit à la limite, suitability et conservation de la non-trivialité.

Les quatre premières sont indépendantes au niveau fonctionnel. La cinquième n'est testée par aucun des exemples présents.

## 7. Portée par rapport à Navier–Stokes

Le champ concentré et les champs translatés sont divergence-free mais ne sont pas déclarés solutions d'une équation d'évolution. L'orbite périodique vit dans \(\mathbb R^2\) et ne représente qu'un contre-exemple logique à « récurrence implique stationnarité ». Les défauts diagonaux sont des modèles de quantificateurs.

En particulier, le rapport ne construit aucune solution ancienne sur \(\mathbb R^3\), ne réfute aucun théorème de compacité pour solutions suitable disposant de bornes de dissipation, et ne produit ni régularité ni blow-up pour le problème Clay.

## 8. Reproduction et certificat

Commande :

```powershell
python -B experiments/navier-stokes/stationary-subsequence/stationary_subsequence_audit.py
```

Sortie validée :

```text
stationary_subsequence_audit: PASS
exact_assertions=1814
concentration=weak-L3_and_local_L3_invariant; L2^2~n^-1; grad_L2^2~n
translation=temporal_generator_zero_but_mass_escapes_every_fixed_ball
periodic=z_prime=Jz; exact_recurrence_with_generator_norm_one
diagonal=nested_fixed_defects_vanish_but_moving_defect_equals_one
quantifiers=individual_subsequences_need_not_have_common_refinement
scope=functional_and_logical_certificate; no Navier-Stokes or PDE claim
```

Le programme utilise exclusivement la bibliothèque standard et `Fraction`. Les 1814 assertions sont exactes ; aucune approximation flottante, discrétisation ou simulation PDE n'intervient. Résidu rationnel : zéro.

Empreinte SHA-256 du script validé :

```text
8d6f53023bd21f0aad817c77f004ee6420d8688f73695dbc44289ff9ade3e702
```

## Décision contradictoire

**RÉVISER.** Refuser tout lemme « récurrence \(+\) borne critique \(\Rightarrow\) sous-suite stationnaire non triviale » qui n'énonce pas séparément dissipation/compacité, tightness, défaut du générateur et extraction emboîtée. Le prochain test doit porter sur la stabilité de ces quatre propriétés sous le passage à la limite d'une vraie suite de solutions suitable, notamment pour la pression et le produit quadratique.
