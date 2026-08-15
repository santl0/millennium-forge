# Cycle 0049 — audit contradictoire de la porte d'énergie relative

Date d'exécution : 2026-08-15

## Verdict

Soient, sur \(\mathbb R^3\),

\[
V(h)=e^{h\Delta}a,
\qquad a\in L^{3,\infty}_\sigma,
\qquad \|a\|_{L^{3,\infty}}\le M,
\]

et un correcteur \(w\in C([0,H];L^2_\sigma)\) vérifiant

\[
\|w(h)\|_2\le C_wM^2h^{1/4}.
\]

Deux termes bulk formels de l'énergie relative sont uniformément intégrables près de \(h=0\) :

\[
\|V(h)\|_\infty^2\|w(h)\|_2^2
\lesssim M^6h^{-1/2},
\qquad
\|V(h)\|_4^4\lesssim M^4h^{-1/2}.
\]

Leur intégrabilité est un progrès réel vers une inégalité globale. Elle ne suffit toutefois pas à autoriser le test par \(w\) : ce test suppose précisément le gradient \(\nabla w\in L^2\) qu'il cherche à produire. Après localisation, les flux cubique et de pression ne sont pas contrôlés par les seules bornes \(L^2\) et faible-\(L^3\).

Un contre-profil solénoïdal multi-échelle explicite au niveau des lois d'échelle montre davantage : on peut avoir simultanément \(W\in L^2\cap L^{3,\infty}\), une infinité de couronnes, et un flux convectif de cutoff non nul le long d'une suite \(R_n\to\infty\). Ce profil n'est pas une solution de Navier–Stokes. Il réfute seulement le passage à l'infini comme conséquence fonctionnelle automatique ; suitability, équation et/ou contrôle du gradient restent des portes indispensables.

## 1. Lissage calorique et puissances exactes

La loi de lissage en dimension trois donne

\[
\|e^{h\Delta}a\|_{L^q}
\lesssim h^{-\gamma(q)}\|a\|_{L^{3,\infty}},
\qquad
\gamma(q)=\frac32\left(\frac13-\frac1q\right).
\]

Aux deux exposants utiles,

\[
\gamma(\infty)=\frac12,
\qquad
\gamma(4)=\frac18.
\]

La seconde estimation peut aussi être obtenue sans supposer une inclusion fausse entre espaces de Lorentz. Le semi-groupe préserve la borne faible-\(L^3\), puis la formule des couches donne, pour une fonction bornée \(f\),

\[
\|f\|_4^4
=4\int_0^{\|f\|_\infty}\lambda^3
  |\{|f|>\lambda\}|\,d\lambda
\le 4\|f\|_{L^{3,\infty}}^3\|f\|_\infty.
\]

Il s'ensuit, avec des constantes de semi-groupe explicitées mais non normalisées ici,

\[
\|V(h)\|_\infty\le C_\infty Mh^{-1/2},
\qquad
\|V(h)\|_4\le C_4Mh^{-1/8}.
\]

## 2. Sources bulk : intégrabilité exacte

Dans un test formel de l'équation du correcteur par \(w\), les termes

\[
\int |V||w||\nabla w|,
\qquad
\int |V|^2|\nabla w|
\]

sont transformés par Young en

\[
C\|V\|_\infty^2\|w\|_2^2
+C\|V\|_4^4
+\frac12\|\nabla w\|_2^2.
\]

Les exposants temporels sont

\[
2\left(-\frac12\right)+2\left(\frac14\right)
=-\frac12,
\qquad
4\left(-\frac18\right)=-\frac12.
\]

Par conséquent,

\[
\int_0^H\|V\|_\infty^2\|w\|_2^2\,dh
\le 2C_\infty^2C_w^2M^6H^{1/2},
\]

et

\[
\int_0^H\|V\|_4^4\,dh
\le 2C_4^4M^4H^{1/2}.
\]

Ces estimations utilisent le taux \(h^{1/4}\) du correcteur comme donnée déjà obtenue indépendamment. Elles ne permettent pas de le redémontrer en l'insérant rétroactivement dans une estimation dont il serait la conclusion.

## 3. Le coefficient de Grönwall reste critique

Pris seul,

\[
\|V(h)\|_\infty^2\lesssim M^2h^{-1},
\]

et \(\int_0^Hh^{-1}\,dh\) accumule une unité logarithmique par coquille dyadique. La finitude du produit

\[
\int_0^H\|V\|_\infty^2\|w\|_2^2\,dh
\]

n'implique pas celle du coefficient nu ; « simplifier » par \(\|w\|_2^2\) inverse les quantificateurs et supposerait en particulier une minoration inexistante de \(w\).

Cette obstruction n'est pas seulement celle d'un majorant trop grossier. Pour une donnée homogène critique non nulle de degré \(-1\), par exemple le champ solénoïdal du cycle 0048, le flot calorique conserve la forme

\[
e^{h\Delta}a(x)=h^{-1/2}F(x/\sqrt h)
\]

avec \(F\not\equiv0\). Sa norme \(L^\infty\) sature donc la puissance \(h^{-1/2}\), et le carré n'est effectivement pas intégrable à l'origine.

## 4. Ledger des flux de cutoff

Prenons \(\chi_R(x)=\chi(x/R)\), avec

\[
\|\nabla\chi_R\|_\infty\lesssim R^{-1},
\qquad
\|\Delta\chi_R\|_\infty\lesssim R^{-2}.
\]

Après les intégrations par parties formelles, les contributions de couronne ont les tailles suivantes. Les constantes de \(\chi\) sont omises.

| Contribution | Majorant global disponible | Puissance en \(h\) | Puissance en \(R\) | Verdict avec les seules hypothèses |
|---|---:|---:|---:|---|
| diffusion de cutoff | \(\|w\|_2^2\) | \(h^{1/2}\) | \(R^{-2}\) | intégrable, tend vers zéro |
| drift calorique | \(\|V\|_\infty\|w\|_2^2\) | \(h^0\) | \(R^{-1}\) | intégrable, tend vers zéro |
| forçage calorique | \(\|V\|_4^2\|w\|_2\) | \(h^0\) | \(R^{-1}\) | intégrable, tend vers zéro |
| convection propre | \(\int_{A_R}|w|^3\) | non contrôlée | \(R^{-1}\) | ouverte |
| pression | \(\int_{A_R}|q||w|\) | non contrôlée | \(R^{-1}\) | ouverte |

Les trois intégrales temporelles fermées ont respectivement les facteurs

\[
\frac23H^{3/2},\qquad H,\qquad H.
\]

En revanche, \(L^2\cap L^{3,\infty}\) ne contrôle pas la masse forte \(L^3\). Si la pression globale est seulement

\[
q=R_iR_j(v_iv_j)\in L^{3/2,\infty},
\]

alors le produit endpoint avec \(w\in L^{3,\infty}\) est au mieux faible-\(L^1\). Il n'existe ni intégrabilité absolue ni continuité absolue des queues qui découle de ce seul calcul. La suitability locale peut rendre le produit localement intégrable ; elle ne fournit pas automatiquement la domination uniforme nécessaire lorsque \(R\to\infty\).

## 5. Contre-profil solénoïdal multi-échelle

### 5.1 Atome à moment cubique signé

Il existe un champ \(\Phi\in C_c^\infty(\mathbb R^3;\mathbb R^3)\), divergence-free, tel que

\[
J:=\int_{\mathbb R^3}|\Phi|^2\Phi_1\,dx\ne0.
\]

Une construction directe consiste à poser

\[
\psi(x)=f(x_1)g(x_2)k(x_3),
\qquad
\Phi=(\partial_2\psi,-\partial_1\psi,0),
\]

où \(f,k\) sont des bosses positives et \(g\) une bosse asymétrique telle que \(\int(g')^3\ne0\). En effet,

\[
J=
\left(\int f^3\right)
\left(\int(g')^3\right)
\left(\int k^3\right),
\]

car le second terme contient \(\int g^2g'=0\). On normalise \(\|\Phi\|_\infty\le1\) et le volume de son support à au plus un.

### 5.2 Empilement dans les couronnes

Pour \(n\ge1\), définissons

\[
R_n=4^n,\qquad
\delta_n=2^{-n},\qquad
N_n=32^n,
\qquad
\ell_j=2^{-j}\quad(1\le j\le N_n).
\]

Dans une petite région de transition de la couronne de rayon \(R_n\), plaçons des supports disjoints et posons

\[
W_{n,j}(x)=
\delta_n\ell_j^{-1}
\Phi\!\left(\frac{x-x_{n,j}}{\ell_j}\right),
\qquad
W=\sum_{n\ge1}\sum_{j=1}^{N_n}W_{n,j}.
\]

Les couronnes sont disjointes et chaque groupe contient un nombre fini d'atomes. La somme est donc lisse localement et divergence-free. En notant \(E_2=\|\Phi\|_2^2\) et \(E_3=\|\Phi\|_3^3\),

\[
\sum_{j=1}^{N_n}\|W_{n,j}\|_2^2
=E_2\delta_n^2\sum_{j=1}^{N_n}2^{-j}
<E_2\delta_n^2.
\]

Comme \(\sum_n\delta_n^2=1/3\), on a \(W\in L^2\). L'empilement géométrique des amplitudes donne, groupe par groupe,

\[
K_3(W_n)^3\le\frac87\delta_n^3.
\]

Puisque \(\sum_n\delta_n^3=1/7\),

\[
K_3(W)^3\le\frac{8}{49}
\]

après la normalisation de l'atome. Ainsi \(W\in L^{3,\infty}\).

La masse forte critique et le moment cubique s'additionnent cependant :

\[
\sum_{j=1}^{N_n}\|W_{n,j}\|_3^3
=E_3N_n\delta_n^3=E_3R_n,
\]

\[
\sum_{j=1}^{N_n}
\int|W_{n,j}|^2(W_{n,j})_1\,dx
=JN_n\delta_n^3=JR_n.
\]

Choisissons une famille de cutoffs dont le gradient vaut exactement \(c_\chi e_1/R_n\) sur la petite région contenant le groupe \(n\). Les autres groupes sont soit dans la zone constante, soit hors du support de ce gradient. Le flux cubique normalisé est alors

\[
\frac{c_\chi}{R_n}
\sum_{j=1}^{N_n}
\int|W_{n,j}|^2(W_{n,j})_1\,dx
=c_\chi J,
\]

indépendamment de \(n\). Pour des cutoffs radiaux usuels, le même calcul donne ce terme principal et une erreur géométrique \(O(R_n^{-1})\), après orientation des atomes dans la direction radiale locale.

Le coût caché se trouve exactement dans le gradient :

\[
\|\nabla W_{n,j}\|_2^2
=\delta_n^2\ell_j^{-1}\|\nabla\Phi\|_2^2,
\]

dont la somme explose aux plus petites échelles. Le profil est donc exclu dès qu'une dissipation globale uniforme est disponible, mais pas par \(L^2\) et faible-\(L^3\) seuls.

### 5.3 Trace temporelle compatible avec le taux donné

Posons

\[
w(h,x)=h^{1/4}W(x).
\]

Après une normalisation fixe de \(W\), ce champ appartient à \(C([0,H];L^2)\) et vérifie le taux demandé. Son flux cubique intégré le long de la suite \(R_n\) vaut, à la constante atomique près,

\[
\int_0^Hh^{3/4}\,dh
=\frac47H^{7/4},
\]

et ne tend pas vers zéro lorsque \(n\to\infty\). Ce champ temporel ne vérifie ni l'équation du correcteur ni l'inégalité d'énergie locale. C'est précisément pourquoi il isole la donnée manquante : une propriété PDE, et non une interpolation des deux normes.

## 6. Inversions de quantificateurs attaquées

1. **Majorant critique versus petite constante.** La borne \(h^{1/2}\|V(h)\|_\infty\lesssim M\) uniforme en \(a\) ne dit pas que cette quantité tend vers zéro pour toute donnée de faible-\(L^3\).
2. **Produit intégrable versus coefficient intégrable.** Le facteur \(\|w(h)\|_2^2=O(h^{1/2})\) ne peut pas être supprimé de l'intégrale.
3. **Troncature finie versus profil complet.** Pour tout nombre fini \(K\) de groupes, le flux est nul au-delà de la dernière couronne. Mais, pour le profil complet, le flux sur la diagonale \(R_n\) est constant. Les limites \(K\to\infty\) et \(R\to\infty\) ne commutent pas.
4. **Suitability locale versus énergie globale.** Une inégalité vraie pour chaque cutoff fixé ne permet le passage \(R\to\infty\) qu'après une estimation uniforme des flux.
5. **Test par \(w\) versus construction de \(\nabla w\).** Utiliser directement \(w\) comme fonction test avant une approximation ou une inégalité locale légitime suppose la régularité recherchée.

## 7. Portée PDE et problème Clay

Le résultat positif du cycle est un ledger d'intégrabilité : les deux sources bulk critiques deviennent \(L^1_h\) grâce au taux \(h^{1/4}\). Le résultat négatif est qu'aucune fermeture globale ne suit des seules bornes fonctionnelles.

Le contre-profil n'est pas une solution de Navier–Stokes, n'a pas de pression PDE certifiée et n'est pas suitable. Il ne réfute donc pas la globalisation pour la solution ancienne conditionnelle du programme. Il impose au prochain lemme de faire intervenir explicitement l'équation locale adaptée, un contrôle de dissipation, ou une annulation structurée du flux total convection–pression. Aucun résultat de régularité ou de blow-up pour le problème Clay n'est revendiqué.

## 8. Reproduction et certificat

Commande :

```powershell
python -B experiments/navier-stokes/relative-energy/relative_energy_audit.py
```

Le script utilise exclusivement la bibliothèque standard et `Fraction`. Il certifie les exposants, les sommes géométriques, les deux ordres de limites et le flux diagonal normalisé ; il ne discrétise aucune PDE.

Sortie validée :

```text
relative_energy_audit: PASS
exact_assertions=97
bulk=||V||_inf^2||w||_2^2~M^6*h^-1/2
forcing=||V||_4^4~M^4*h^-1/2
bare_gronwall=||V||_inf^2~M^2*h^-1 is endpoint-logarithmic
multiscale=L2_and_weak-L3_bounded_but_diagonal_cubic_flux=1
```

L'empreinte exacte est régénérée automatiquement à chaque exécution. Résidu rationnel : zéro pour toutes les assertions. Résidu adverse : flux diagonal normalisé égal à un pour chaque couronne, et non convergent vers zéro.

Empreinte SHA-256 du script validé :

```text
b2ae64c546e0d155a305b43dd0d9f726aef67624af52d654091ca391467bd64d
```

## Décision contradictoire

**CONTINUER SOUS CONDITION.** Conserver l'intégrabilité des deux sources bulk. Refuser la globalisation tant qu'un argument issu de la suitability ne contrôle pas conjointement le flux cubique et le flux de pression, ou tant qu'une dissipation globale n'exclut pas l'empilement intermittent. Le prochain test décisif doit dériver l'inégalité locale exacte du correcteur à partir de celle de \(v\), sans employer \(w\) comme test a priori, puis suivre les deux flux ouverts avec constantes uniformes en \(R\).
