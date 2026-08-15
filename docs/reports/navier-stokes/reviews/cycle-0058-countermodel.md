# Cycle 0058 — rotation rapide, bornes de Bochner et non-identifiabilité

Date d'exécution : 2026-08-15

## Verdict

L'identité abstraite

\[
\partial_s Z-r=\beta RZ
\tag{1}
\]

donne une voie de collapse qui ne requiert aucune borne BV sur \(q=1/\beta\), à condition de disposer de vraies bornes de Bochner :

\[
\boxed{
\|RZ\|_{L^p(I;X^*)}
\le
\frac1{\operatorname*{ess\,inf}_I|\beta|}
\left(
\|\partial_s Z\|_{L^p(I;X^*)}
+\|r\|_{L^p(I;X^*)}
\right).}
\tag{2}
\]

Ainsi, si le numérateur reste uniformément borné et si \(\operatorname*{ess\,inf}_I|\beta_n|\to\infty\), alors \(RZ_n\to0\) dans \(L^p(I;X^*)\).

Trois portes adversariales sont indispensables :

1. une grande vitesse ne suffit pas si \(\|\partial_sZ_n\|_{L^p}\) explose ;
2. une compensation dans \(\partial_sZ_n-r_n\) ne borne aucun des deux termes séparément ;
3. sur le stabilisateur \(\ker R\), la vitesse \(\beta\) n'est pas identifiable.

Les certificats sont rationnels, discrets ou de dimension finie. Ils ne construisent aucune solution de Navier–Stokes.

## 1. Lemme positif de Bochner

Soient \(I\) un intervalle de mesure finie, \(X^*\) un espace de Banach et \(1\le p\le\infty\). Posons \(b=\operatorname*{ess\,inf}_I|\beta|\) et supposons :

- \(RZ,\partial_sZ,r\in L^p(I;X^*)\) ;
- l'identité (1) presque partout dans \(X^*\) ;
- \(\beta\) mesurable et \(|\beta(s)|\ge b>0\) presque partout.

Alors, point par point,

\[
b\|RZ(s)\|_{X^*}
\le
|\beta(s)|\|RZ(s)\|_{X^*}
=
\|\partial_sZ(s)-r(s)\|_{X^*}.
\]

La monotonie de la norme \(L^p\), puis Minkowski, donnent

\[
b\|RZ\|_{L^p(X^*)}
\le
\|\partial_sZ-r\|_{L^p(X^*)}
\le
\|\partial_sZ\|_{L^p(X^*)}
+\|r\|_{L^p(X^*)}.
\]

C'est exactement (2). Aucun contrôle de \(\partial_s(1/\beta)\) n'intervient. En revanche, la conclusion exige que les normes du membre droit soient uniformes en \(n\).

### Test rationnel

Le certificat utilise une grille pondérée de huit cellules, \(X^*=\ell^1(\mathbb Q^3)\), et huit échelles \(N=2,\ldots,256\). Il pose

\[
\beta_i=N+(i\bmod3)
\]

et choisit des vecteurs rationnels \(RZ_i=O(N^{-1})\) et \(r_i=O(1)\), puis définit

\[
(\partial_sZ)_i=\beta_iRZ_i+r_i.
\]

Il vérifie exactement :

- (1) sur chaque cellule ;
- l'inégalité ponctuelle issue de (2) ;
- (2) dans la norme \(L^1\) pondérée ;
- \(\inf_i|\beta_i|=N\) ;
- des bornes uniformes explicites sur \(\partial_sZ\) et \(r\) ;
- la décroissance de la norme rationnelle de \(RZ\).

Le cas \(L^1\) est choisi pour éviter toute racine irrationnelle dans le certificat. La preuve précédente couvre analytiquement tous les \(1\le p\le\infty\).

## 2. Stroboscopie non axisymétrique et explosion Bochner

Normalisons la période du groupe à \(1\). Soit \(Q_\alpha\) une action unitaire fortement continue, de générateur \(R\), et choisissons

\[
\|U\|=\|RU\|=1,
\qquad
RU\ne0.
\]

Le profil \(U\) n'est donc pas fixé par l'action. Pour \(N=2^m\), posons

\[
D_N=N^2+N+1,
\qquad
\delta_N=\frac{N+1}{D_N}.
\]

Sur chacun des \(N^2\) cycles, la phase parcourt :

- une fenêtre angulaire de largeur \(\delta_N\) à vitesse \(N\) ;
- le reste du cercle à vitesse \(N^4\).

Les mesures temporelles totales sont

\[
S_N=\frac{N^2+N}{D_N},
\qquad
F_N=\frac1{D_N}.
\]

La phase est absolument continue et sa dérivée vaut presque partout

\[
\beta_N\in\{N,N^4\}>0.
\]

Définissons

\[
Z_N(s)=Q_{\theta_N(s)}U.
\]

Sur les passages lents, \(\theta_N\bmod1\in[0,\delta_N]\). Sur les passages rapides, la distance à \(U\) est bornée par \(2\). Ainsi, pour tout \(1\le p<\infty\),

\[
\int_0^1\|Z_N-U\|^p\,ds
\le
S_N\delta_N^p\|RU\|^p
+F_N2^p\|U\|^p
\longrightarrow0.
\tag{3}
\]

La limite forte \(U\) reste non axisymétrique puisque \(RU\ne0\). D'autre part, presque partout,

\[
\partial_sZ_N
=\beta_NQ_{\theta_N}RU,
\qquad
RZ_N=Q_{\theta_N}RU.
\]

Par unitarité,

\[
\|RZ_N\|_{L^1}=1,
\]

tandis que

\[
\begin{aligned}
\|\partial_sZ_N\|_{L^1}
&=S_NN+F_NN^4\\
&=\frac{N(N^2+N)+N^4}{D_N}\\
&=N^2.
\end{aligned}
\tag{4}
\]

La dérivée de Bochner existe pour chaque \(N\), mais sa norme explose. Le membre droit de (2), avec \(r_N=0\) et \(\inf\beta_N=N\), vaut \(N\), pas une quantité tendant vers zéro.

Ce modèle réfute donc l'implication trop faible

\[
\inf\beta_N\to\infty
\quad+\quad
Z_N\to Z\text{ fortement dans }L^p
\quad\Longrightarrow\quad
RZ=0.
\]

La convergence forte temporelle de \(Z_N\) ne crée aucune symétrie : si \(R\) est borné, elle donne au contraire \(RZ_N\to RU\ne0\). Si \(R\) est non borné, un passage à la limite demanderait en plus un contrôle du graphe. Dans les deux cas, seule une borne de Bochner adaptée peut exploiter le facteur \(1/\inf|\beta_N|\) dans (2).

## 3. Compensation de grands termes

Sur l'intervalle unité, considérons des quantités scalaires constantes et \(\beta_N=N\).

### Famille A : différence uniformément bornée

Posons

\[
RZ_N=\frac1N,
\qquad
\partial_sZ_N=N^2,
\qquad
r_N=N^2-1.
\]

Alors

\[
\partial_sZ_N-r_N=1=\beta_NRZ_N.
\]

La différence est uniformément bornée, mais

\[
\|\partial_sZ_N\|=N^2,
\qquad
\|r_N\|=N^2-1
\]

divergent. Une borne sur la combinaison ne produit donc pas les deux bornes séparées nécessaires à un argument de compacité temporelle ou de convergence du résidu.

Cette famille ne réfute pas le collapse de \(RZ_N\) : ici \(RZ_N=1/N\to0\), et la borne plus fine

\[
\|RZ_N\|
\le
\frac{\|\partial_sZ_N-r_N\|}{\operatorname*{ess\,inf}|\beta_N|}
\]

suffit. Elle réfute seulement l'inférence abusive « différence bornée \(\Rightarrow\) chaque terme borné ».

### Famille B : différence seulement contrôlée relativement à \(\beta_N\)

Posons maintenant

\[
RZ_N=1,
\qquad
\partial_sZ_N=N^2,
\qquad
r_N=N^2-N.
\]

Alors

\[
\partial_sZ_N-r_N=N=\beta_NRZ_N,
\qquad
\frac{\partial_sZ_N-r_N}{\beta_N}=1.
\]

La combinaison normalisée est contrôlée, mais \(RZ_N\) ne s'effondre pas. Contrôler seulement \((\partial_sZ-r)/\beta\) revient précisément à contrôler \(RZ\), sans petit facteur supplémentaire.

Les deux familles montrent pourquoi les quantificateurs doivent être écrits séparément : soit on contrôle directement \(\partial_sZ-r\) dans une norme uniforme, soit on établit des bornes uniformes distinctes sur \(\partial_sZ\) et \(r\). Aucune de ces conclusions ne suit d'une simple compensation algébrique.

## 4. Stabilisateur dégénéré

Dans \(\mathbb R^3\), prenons le générateur de rotation

\[
R(x,y,z)=(-y,x,0)
\]

et le chemin

\[
Z(s)=(0,0,1+s).
\]

Il appartient entièrement au stabilisateur :

\[
RZ(s)=0.
\]

Avec

\[
\partial_sZ=r=(0,0,1),
\]

l'identité (1) devient

\[
0=\beta(s)\,0
\]

pour toute fonction \(\beta\). Les vitesses \(0\), \(N\), \(N^4\) et \(-N\) produisent exactement les mêmes \(Z\), \(\partial_sZ\) et \(r\).

La vitesse de groupe est donc non identifiable lorsque le profil appartient au stabilisateur. Une preuve qui reconstruit \(\beta\) en divisant par une composante de \(RZ\) doit d'abord exclure cette dégénérescence. Inversement, \(RZ=0\) est déjà la conclusion de symétrie ; aucune information sur \(\beta\) n'est alors nécessaire.

## 5. Passe contradictoire

| version trop faible | contre-modèle | défaut exact |
|---|---|---|
| grande vitesse seule | stroboscopie positive | \(\|\partial_sZ_N\|_{L^1}=N^2\) |
| grande vitesse et compacité forte de \(Z_N\) | même modèle | \(R\) ne passe pas par convergence forte sans contrôle de graphe |
| différence bornée donc deux termes bornés | compensation A | annulation de deux termes \(O(N^2)\) |
| différence divisée par \(\beta\) contrôlée donc collapse | compensation B | le quotient est exactement \(RZ_N=1\) |
| vitesse déduite du chemin observé | stabilisateur | \(RZ=0\), donc \(\beta\) disparaît de (1) |

Le lemme positif résiste à ces attaques lorsque ses hypothèses exactes sont conservées : identité dans \(L^p(X^*)\), minoration uniforme de \(|\beta|\), et numérateur uniformément borné.

## 6. Séparation stricte avec Navier–Stokes

Les phases, profils unitaires, vecteurs rationnels et résidus sont prescrits. Le certificat ne contient :

- aucune vitesse divergence-free sur \(\mathbb R^3\) ou \(\mathbb T^3\) ;
- aucune pression ni projection de Leray ;
- aucune convection ni dissipation visqueuse ;
- aucune solution faible, Leray–Hopf, suitable, forte ou ancienne ;
- aucun passage compact au continuum Navier–Stokes.

Dans une application PDE, il faudrait encore établir l'identité (1) dans un espace dual précis, l'existence de la dérivée de Bochner, les bornes uniformes du numérateur, la fermeture du générateur de groupe et la compatibilité avec la pression non locale.

Aucune régularité, singularité ou résolution du problème Clay n'est revendiquée.

## 7. Reproduction et certificat

Commande :

~~~powershell
python -B experiments/navier-stokes/bochner-fast-rotation/bochner_rotation_audit.py
~~~

Sortie validée :

~~~text
bochner_rotation_audit: PASS
exact_assertions=586
positive_L1=Bochner_estimate_verified_pointwise_and_on_weighted_grid
stroboscopic=Z_N_to_nonaxisymmetric_U_in_finite_Lp
stroboscopic_derivative=||d_s_Z_N||_L1=N^2_while_||RZ_N||_L1=1
compensation_A=d_s_Z=N^2_r=N^2-1_difference=1
compensation_B=(d_s_Z-r)/beta=1_without_collapse
stabilizer=RZ=0_makes_beta_nonidentifiable
seed=n/a; arithmetic=Fraction; no Navier-Stokes PDE claim
~~~

Le script utilise exclusivement la bibliothèque standard et **Fraction**. Les 586 assertions sont exactes. Graine : non applicable.

Empreinte SHA-256 du script validé :

~~~text
ad8474fa672697a9239a2d8567d122c631818021c6ebc3065695652d3ef7a8a5
~~~

## Décision

**CONSERVER** le lemme de Bochner (2). **ABANDONNER** toute version fondée sur la seule grandeur de \(\beta\), sur la seule compacité forte de \(Z\), ou sur une compensation non quantifiée. **RÉVISER** toute reconstruction de vitesse sur le stabilisateur.
