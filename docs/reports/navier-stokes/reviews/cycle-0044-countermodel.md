# Cycle 0044 — queue externe de Leray et budget global annulaire

Date d'audit : 2026-08-15.

## Verdict

Soit \(\mathbb P_{\mathrm L}\) la projection de Leray sur \(\mathbb R^3\), et soit un tenseur \(S\) supporté hors de \(B_L\), \(L\geq2\), avec

\[
\left\|\sum_{k,j}|S_{kj}|\right\|_{L^{3/2,\infty}(\mathbb R^3)}
\leq M.
\]

Sur le compact \(B_1\), la partie locale de \(\mathbb P_{\mathrm L}\operatorname{div}S\) est nulle et le noyau newtonien donne, pour \(m=0,1\),

\[
\boxed{
\sup_{|x|\leq1}
|\nabla^m\mathbb P_{\mathrm L}\operatorname{div}S(x)|_{\ell^\infty}
\leq A_m M L^{-3-m},}
\]

avec les constantes rationnelles explicites

\[
A_0=\frac{11904}{35},
\qquad
A_1=\frac{134912}{25}.
\]

Ces constantes sont volontairement majorées : elles privilégient un certificat rationnel simple à une optimisation tensorielle.

Un ledger indépendant montre cependant qu'un profil annulaire critique peut avoir une norme faible critique uniforme tout en produisant un budget global de dilatation d'ordre \(L^2\), et des sommes terme à terme logarithmiques. La disparition locale après projection ne fournit donc pas, à elle seule, une borne globale uniforme des erreurs de cutoff.

Ce rapport ne simule pas Navier–Stokes et ne revendique aucune compacité de solutions.

## Convention de Leray et noyau extérieur

Fixons

\[
N(x)=\frac1{4\pi|x|},
\qquad
\mathbb P_{\mathrm L}
=I+\nabla(-\Delta)^{-1}\operatorname{div}.
\]

Pour un tenseur lisse \(S\), avec

\[
(\operatorname{div}S)_k=\partial_jS_{kj},
\]

la partie non locale s'écrit, loin du support,

\[
(\mathbb P_{\mathrm L}\operatorname{div}S)_i(x)
=\int_{\mathbb R^3}
\partial_i\partial_k\partial_jN(x-y)S_{kj}(y)\,dy.
\]

Le terme local \(\operatorname{div}S\) est supporté avec \(S\) et disparaît donc dans \(B_1\). Le signe éventuel du noyau n'affecte pas les bornes absolues.

La dérivée troisième de \(|z|^{-1}\) est

\[
\partial_i\partial_k\partial_j|z|^{-1}
=3(\delta_{ik}z_j+\delta_{ij}z_k+\delta_{kj}z_i)|z|^{-5}
-15z_iz_kz_j|z|^{-7}.
\]

La somme brute des coefficients absolus vaut

\[
3+3+3+15=24.
\]

Ainsi

\[
|\partial_i\partial_k\partial_jN(z)|
\leq\frac6\pi|z|^{-4}
<2|z|^{-4}.
\]

Après une dérivée supplémentaire, les contributions absolues sont

\[
3\cdot3(1+5)=54,
\qquad
15(3+7)=150,
\]

d'où le total \(204\) et

\[
|\partial_\ell\partial_i\partial_k\partial_jN(z)|
\leq\frac{51}{\pi}|z|^{-5}
<17|z|^{-5}.
\]

Les normes tensorielles sont fixées afin d'éviter une constante silencieuse : le tenseur source est mesuré par \(\sum_{kj}|S_{kj}|\), et la sortie par le maximum des composantes.

## Inclusion faible-\(L^{3/2}\) sur une coquille

Pour \(f\in L^{3/2,\infty}(E)\), la formule des couches avec

\[
\mu_f(t)\leq
\min\left\{|E|,\|f\|_{L^{3/2,\infty}}^{3/2}t^{-3/2}\right\}
\]

donne la constante exacte

\[
\|f\|_{L^1(E)}
\leq3|E|^{1/3}\|f\|_{L^{3/2,\infty}(E)}.
\]

Décomposons l'extérieur en

\[
A_k=\{2^kL\leq|y|<2^{k+1}L\},
\qquad r_k=2^kL.
\]

Pour \(x\in B_1\) et \(L\geq2\),

\[
|x-y|\geq|y|-1\geq\frac{|y|}{2}\geq\frac{r_k}{2}.
\]

De plus,

\[
|A_k|=\frac{28\pi}{3}r_k^3.
\]

Les inégalités rationnelles

\[
\pi<\frac{22}{7},
\qquad
\frac{88}{3}<\left(\frac{31}{10}\right)^3
\]

impliquent

\[
|A_k|^{1/3}<\frac{31}{10}r_k.
\]

La restriction à chaque coquille a une quasi-norme faible au plus \(M\). Il vient

\[
\sup_{B_1}
|\nabla^m\mathbb P_{\mathrm L}\operatorname{div}
(S\mathbf1_{A_k})|_{\ell^\infty}
\leq
C_m M r_k^{-3-m},
\]

où

\[
C_0=\frac{1488}{5},
\qquad
C_1=\frac{25296}{5}.
\]

La somme géométrique est absolument convergente :

\[
\sum_{k=0}^\infty r_k^{-3-m}
=\frac{L^{-3-m}}{1-2^{-(3+m)}}.
\]

On obtient exactement

\[
A_0
=\frac{1488}{5}\frac8{7}
=\frac{11904}{35},
\]

et

\[
A_1
=\frac{25296}{5}\frac{16}{15}
=\frac{134912}{25}.
\]

Les constantes non rationalisées issues du même calcul sont plus petites :

\[
\widetilde A_0
=\frac{2304}{7\pi}
\left(\frac{28\pi}{3}\right)^{1/3},
\]

\[
\widetilde A_1
=\frac{26112}{5\pi}
\left(\frac{28\pi}{3}\right)^{1/3}.
\]

Aucune annulation de moment de \(S\) n'est utilisée. Ici \(m\) désigne le nombre de dérivées spatiales supplémentaires du champ observé, et non un ordre multipolaire.

## Ledger adverse : profil critique sur des coquilles

Le calcul précédent est local. Pour tester les constantes globales d'un cutoff extérieur, considérons un ledger scalaire dyadique normalisé :

\[
|A_j|_{\mathrm{norm}}=7\,8^j,
\qquad
|U_j|=\varepsilon\,2^{-j},
\qquad 0\leq j\leq J.
\]

Il représente les plateaux d'un profil critique \(1/r\) ; une réalisation lisse sur des sous-couronnes modifie seulement des constantes fixes. Le ledger lui-même n'est pas présenté comme une solution PDE.

La masse cumulée est

\[
\sum_{j=0}^k7\,8^j=8^{k+1}-1.
\]

Par conséquent,

\[
\sup_k
(\varepsilon2^{-k})^3
\sum_{j=0}^k|A_j|_{\mathrm{norm}}
<8\varepsilon^3.
\]

La quasi-norme faible-\(L^3\) reste donc uniforme lorsque \(J\) croît.

### Terme de dilatation

Sur une transition de taille \(L=2^J\),

\[
|\nabla\chi_L|\asymp L^{-1},
\qquad
|D\chi_L|=|y\cdot\nabla\chi_L|\asymp1.
\]

Le terme \((D\chi_L)U_J\) a amplitude \(\varepsilon L^{-1}\) sur un volume normalisé \(7L^3\). Son budget \(L^1\) vaut donc

\[
\boxed{
\|(D\chi_L)U_J\|_{L^1,\mathrm{ledger}}
=7\varepsilon L^2.}
\]

Si une transition est comptée sur chaque coquille,

\[
\sum_{j=0}^J7\varepsilon4^j
=\frac{7\varepsilon}{3}(4^{J+1}-1).
\]

Une borne faible-\(L^3\) globale ne rend donc pas ce budget \(L^1\) uniforme.

### Termes visqueux et stress de cutoff

Le produit \((\Delta\chi_j)U_j\) a amplitude \(\varepsilon2^{-3j}\). Son coût \(L^1\) est exactement \(7\varepsilon\) par coquille, donc

\[
\sum_{j=0}^J
\|(\Delta\chi_j)U_j\|_{L^1,\mathrm{ledger}}
=7\varepsilon(J+1).
\]

Le stress \(U_j\otimes\nabla\chi_j\) a amplitude \(\varepsilon4^{-j}\). Sa norme faible-\(L^{3/2}\) par coquille est inférieure à \(4\varepsilon\), donc la somme naïve des quasi-normes croît au plus comme

\[
4\varepsilon(J+1).
\]

Mais l'union disjointe des stresses vérifie encore

\[
\left\|\sum_{j=0}^J
U_j\otimes\nabla\chi_j\right\|_{L^{3/2,\infty}}
<4\varepsilon,
\]

uniformément en \(J\). Cette différence avertit que la croissance d'un ledger par triangle n'est pas automatiquement une minoration de la norme quotient optimale.

## Ce qui est établi, et ce qui ne l'est pas

Le certificat établit :

1. la décroissance locale \(L^{-3}\) de \(\mathbb P_{\mathrm L}\operatorname{div}S\) et \(L^{-4}\) de sa première dérivée pour une queue uniformément bornée dans faible-\(L^{3/2}\) ;
2. la sommabilité dyadique absolue avec constantes explicites ;
3. la compatibilité de cette disparition locale avec une croissance globale des budgets naturels de dilatation ou avec une croissance artificielle des sommes terme à terme.

Il n'établit pas :

- une borne uniforme des opérateurs de Bogovskiĭ lorsque la géométrie externe varie ;
- la disparition de tous les termes de la force localisée ;
- une annulation entre pression, dilatation, diffusion et non-linéarité ;
- la compacité forte d'une suite de champs ;
- un passage au temps singulier ou une solution ancienne non forcée.

Le ledger annulaire n'est ni une simulation de Navier–Stokes, ni une donnée Clay uniformément énergétique : son énergie globale peut croître avec \(J\).

## Reproduction

~~~powershell
python -B experiments/navier-stokes/outer-cutoff/outer_cutoff_audit.py
~~~

Le script utilise seulement la bibliothèque standard et fractions.Fraction. Il vérifie les coefficients \(24,204\), les constantes rationnelles des noyaux, les séries dyadiques pour plusieurs troncatures, les puissances \(L^{-3-m}\), la borne faible critique du profil annulaire et chaque budget global.

Statut : **RÉVISER**. La queue de la projection de Leray disparaît localement sous le contrôle faible-\(L^{3/2}\), mais l'envoi du cutoff externe à l'infini exige encore une décomposition globale qui évite la croissance de dilatation et suit les constantes de Bogovskiĭ.
