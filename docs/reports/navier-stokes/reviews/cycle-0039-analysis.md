# Cycle 0039 — Contre-théorème de sélection sous multiplicité bornée

**Statut :** `AI_INTERNAL_DERIVATION` — ne pas classer `PAPER_PROOF`

**Verdict :** le contre-théorème est valide. Une multiplicité de supports
égale à deux ne remplace pas leur disjonction : deux curls de taille
\(\asymp n\) peuvent s'annuler exactement dans la somme. Le rapport endpoint
de chaque terme tend vers zéro, tandis que celui du champ total reste fixe et
strictement positif.

## Cadre exact

Fixons

\[
 \chi\in C_c^\infty((1/2,3/2)),
 \qquad
 0\le |\chi|\le1,
 \qquad
 \chi=1\text{ sur }[3/4,5/4],                 \tag{1}
\]

et

\[
 \eta\in C_c^\infty(\mathbb R),
 \qquad
 |\eta|\le1,
 \qquad
 \eta=1\text{ sur }[0,2\pi].                 \tag{2}
\]

Pour chaque entier \(n\ge1\), posons en coordonnées cylindriques

\[
 Z_n=\frac1r\chi(r)\eta(z)\sin(nz)e_\theta.    \tag{3}
\]

Soit aussi

\[
 B=\frac1r\Psi(r,z)e_\theta                   \tag{4}
\]

un champ fixe, non nul, avec
\(\Psi\in C_c^\infty((1/2,3/2)\times\mathbb R)\). Définissons

\[
 U_{1,n}=B+Z_n,
 \qquad
 U_{2,n}=-Z_n.                                 \tag{5}
\]

La convention est

\[
 \|f\|_{L^{p,\infty}}
 =\sup_{s>0}s|\{|f|>s\}|^{1/p}.                \tag{6}
\]

Pour un champ non nul \(U\) de curl non nul, écrivons

\[
 q(U)=
 \frac{\|U\|_{L^{3,\infty}}}
      {\|\operatorname{curl}U\|_{L^{3/2,\infty}}}. \tag{7}
\]

## Lissité, support et divergence

Un champ axisymétrique purement azimutal satisfait

\[
 \operatorname{div}(f(r,z)e_\theta)=0.         \tag{8}
\]

Les profils sont nuls dans un voisinage de l'axe. Malgré la singularité de la
base cylindrique \(e_\theta\) en \(r=0\), les champs prolongés par zéro sont
donc lisses en coordonnées cartésiennes. Ils sont compacts, exactement
divergence-free, et

\[
 U_{1,n}+U_{2,n}=B.                            \tag{9}
\]

Il n'existe que deux supports. Leur fonction de multiplicité vérifie

\[
 \mathbf1_{\operatorname{supp}U_{1,n}}
 +\mathbf1_{\operatorname{supp}U_{2,n}}
 \le2                                           \tag{10}
\]

partout. Cette assertion ne signifie ni disjonction, ni orthogonalité, ni
absence de cancellation.

## Curl exact du mode oscillant

Pour \(F_n=\chi(r)\eta(z)\sin(nz)\), la formule pure-swirl donne

\[
 \operatorname{curl}Z_n
 =\frac1r
 \left(-\partial_zF_n e_r+\partial_rF_n e_z\right), \tag{11}
\]

avec

\[
 \partial_zF_n
 =\chi(r)\bigl(\eta'(z)\sin(nz)
             +n\eta(z)\cos(nz)\bigr),          \tag{12}
\]

\[
 \partial_rF_n=\chi'(r)\eta(z)\sin(nz).       \tag{13}
\]

Les termes contenant \(\eta'\) et \(\chi'\) sont d'ordre un. La minoration
décisive est prise dans une région où ils sont exactement nuls.

## Volume témoin exact après révolution

Posons

\[
 I_n=\{z\in[0,2\pi]:|\cos(nz)|\ge1/2\}.        \tag{14}
\]

Sur une période de cosinus, \(|\cos y|\ge1/2\) occupe une longueur
\(4\pi/3\). Comme \(n\) est entier, le changement de variable \(y=nz\)
parcourt exactement \(n\) périodes et

\[
 |I_n|=\frac1n\,n\frac{4\pi}{3}
 =\frac{4\pi}{3}.                              \tag{15}
\]

Après révolution, l'ensemble témoin est

\[
 \mathcal E_n
 =\{3/4\le r\le5/4,\ 0\le\theta<2\pi,\ z\in I_n\}. \tag{16}
\]

Son volume est exactement

\[
 \begin{aligned}
 |\mathcal E_n|
 &=2\pi\int_{3/4}^{5/4}r\,dr\,|I_n|\\
 &=2\pi\left[\frac{r^2}{2}\right]_{3/4}^{5/4}
   \frac{4\pi}{3}\\
 &=2\pi\left(\frac12\right)\frac{4\pi}{3}
 =\boxed{\frac{4\pi^2}{3}}.                  \tag{17}
 \end{aligned}
\]

Il est indépendant de \(n\). Sur \(\mathcal E_n\),
\(\chi=\eta=1\), donc

\[
 \operatorname{curl}Z_n
 =-\frac nr\cos(nz)e_r.                        \tag{18}
\]

Comme \(r\le5/4\),

\[
 |\operatorname{curl}Z_n|
 \ge\frac45n\frac12=\frac{2n}{5}              \tag{19}
\]

sur tout le témoin.

## Bornes faibles explicites pour \(-Z_n\)

Si \(|f|\ge a\) sur un ensemble de volume \(m\), alors

\[
 \|f\|_{L^{p,\infty}}\ge a m^{1/p};           \tag{20}
\]

la stricte inégalité de la fonction de distribution est traitée en faisant
tendre le seuil vers \(a\) par valeurs inférieures. Les équations
(17)--(19) donnent

\[
 \|\operatorname{curl}Z_n\|_{L^{3/2,\infty}}
 \ge\frac{2n}{5}
 \left(\frac{4\pi^2}{3}\right)^{2/3}.         \tag{21}
\]

Soit \(S_Z\) le support tridimensionnel fixe obtenu par révolution de
\(\operatorname{supp}\chi\times\operatorname{supp}\eta\), et
\(M_Z=|S_Z|\). Sur ce support, \(1/r<2\), donc

\[
 \|Z_n\|_{L^{3,\infty}}
 \le\|Z_n\|_\infty M_Z^{1/3}
 \le2M_Z^{1/3}.                                \tag{22}
\]

Par (21)--(22),

\[
 q(U_{2,n})=q(-Z_n)
 \le\frac{5M_Z^{1/3}}
 {n(4\pi^2/3)^{2/3}}
 \longrightarrow0.                            \tag{23}
\]

## Bornes faibles pour \(B+Z_n\)

Posons

\[
 A_B=\|B\|_{L^\infty},
 \qquad
 M_B^{(1)}=\|\operatorname{curl}B\|_{L^\infty},
\]

et soit \(M=|\operatorname{supp}B\cup S_Z|\). La vitesse satisfait

\[
 \|B+Z_n\|_{L^{3,\infty}}
 \le(A_B+2)M^{1/3}.                            \tag{24}
\]

Sur \(\mathcal E_n\), l'inégalité triangulaire inverse ponctuelle donne

\[
 |\operatorname{curl}(B+Z_n)|
 \ge\frac{2n}{5}-M_B^{(1)}.                   \tag{25}
\]

Pour tout entier

\[
 n\ge5M_B^{(1)},                               \tag{26}
\]

le membre droit est au moins \(n/5\). Par conséquent,

\[
 \|\operatorname{curl}(B+Z_n)\|_{L^{3/2,\infty}}
 \ge\frac n5
 \left(\frac{4\pi^2}{3}\right)^{2/3}.        \tag{27}
\]

Les équations (24) et (27) donnent

\[
 q(U_{1,n})
 \le\frac{5(A_B+2)M^{1/3}}
 {n(4\pi^2/3)^{2/3}}
 \longrightarrow0.                            \tag{28}
\]

La borne fixe sur \(\operatorname{curl}B\) ne peut donc annuler le témoin de
fréquence \(n\) sur une fraction de volume indépendante de \(n\).

## Rapport du champ total

Le champ \(B\) est lisse, compact et non nul. Sa quasi-norme faible-
\(L^3\) est donc strictement positive et finie. De plus,

\[
 \operatorname{curl}B
 =\frac1r(-\partial_z\Psi e_r+\partial_r\Psi e_z). \tag{29}
\]

Si ce curl était nul, \(\nabla\Psi=0\), puis la compacité imposerait
\(\Psi=0\), contrairement à l'hypothèse. Ainsi

\[
 0<q(B)<\infty                                  \tag{30}
\]

est fixe, tandis que (9), (23) et (28) donnent

\[
 q(U_{1,n}+U_{2,n})=q(B)>0,
 \qquad
 \max_{j=1,2}q(U_{j,n})\longrightarrow0.       \tag{31}
\]

## Scaling pour un rayon majeur général

La généralisation géométrique à amplitude fixée est

\[
 Z_{n,R}(r,z)
 =\frac Rr\chi(r/R)\eta(z/R)
   \sin(nz/R)e_\theta.                         \tag{32}
\]

Le témoin devient

\[
 3R/4\le r\le5R/4,
 \qquad 0\le z\le2\pi R,
 \qquad |\cos(nz/R)|\ge1/2.                   \tag{33}
\]

Sa mesure axiale et son volume exacts sont

\[
 |I_{n,R}|=4\pi R/3,
 \qquad
 |\mathcal E_{n,R}|=\frac{4\pi^2}{3}R^3.      \tag{34}
\]

Sur ce témoin,

\[
 |\operatorname{curl}Z_{n,R}|\ge\frac{2n}{5R}. \tag{35}
\]

Par conséquent,

\[
 \|Z_{n,R}\|_{L^{3,\infty}}=O(R),
 \qquad
 \|\operatorname{curl}Z_{n,R}\|_{L^{3/2,\infty}}
 \ge\frac{2nR}{5}
       (4\pi^2/3)^{2/3},                       \tag{36}
\]

et le rapport reste \(O(n^{-1})\), uniformément en \(R\).

Pour la normalisation Clay exacte, on multiplie (32) par \(R^{-1}\), ce qui
correspond à

\[
 U_R(x)=R^{-1}U_1(x/R),
 \qquad
 W_R(x)=R^{-2}W_1(x/R).                        \tag{37}
\]

Les deux quasi-normes critiques deviennent alors indépendantes de \(R\), et
le rapport \(O(n^{-1})\) est inchangé. Un champ de fond \(B\) doit être
redimensionné selon la même convention pour conserver exactement son rapport.

## Premier quantificateur réfuté

Le contre-théorème réfute l'énoncé suivant, pour toute fonction positive
candidate \(\Phi\) et même à multiplicité \(m=2\) :

\[
 \begin{aligned}
 &\text{pour toute décomposition }
 U=\sum_{j=1}^N U_j
 \text{ en champs lisses compacts divergence-free,}\\
 &\sup_x\sum_j\mathbf1_{\operatorname{supp}U_j}(x)\le m,
 \quad q(U)>0
 \quad\Longrightarrow\quad
 \max_jq(U_j)\ge\Phi(q(U),m)>0.
 \end{aligned}                                  \tag{38}
\]

Le **premier quantificateur faux** est « pour toute décomposition à
multiplicité bornée ». La multiplicité limite le nombre de termes présents en
un point, mais pas leur taille ni leur opposition. Ici

\[
 \operatorname{curl}U_{1,n}
 +\operatorname{curl}U_{2,n}
 =\operatorname{curl}B,                        \tag{39}
\]

alors que chaque curl individuel a une quasi-norme \(\gtrsim n\).

La monotonie utilisée pour des cellules disjointes,

\[
 \|\operatorname{curl}U_j\|_{L^{3/2,\infty}}
 \le\|\operatorname{curl}U\|_{L^{3/2,\infty}}, \tag{40}
\]

est donc fausse sous la seule multiplicité bornée.

## Décomposition artificielle et portée

La décomposition (5) est volontairement artificielle et dépend de \(n\). Le
champ total est toujours le même champ \(B\), qui constitue lui-même une
décomposition à une cellule de bon rapport. Le résultat ne prouve donc pas
qu'un champ donné ne possède aucune décomposition géométrique utile. Il prouve
qu'une sélection ne peut pas être uniforme sur **toutes** les décompositions
à recouvrement borné.

En particulier, le contre-théorème ne réfute pas C35--C39 lorsque leurs
composantes sont déterminées par des superniveaux signés et leurs curls sont
des restrictions pointwise sans recouvrement. Il interdit seulement de
remplacer cette structure par le compteur de multiplicité (10).

## Passe adversariale complète

1. **Volume oscillant supposé décroissant.** Faux : pour \(n\in\mathbb N\),
   le sous-ensemble \(|\cos(nz)|\ge1/2\) occupe exactement \(4\pi/3\) dans
   \([0,2\pi]\), d'où le volume fixe (17).
2. **Jacobien cylindrique oublié.** L'intégrale radiale vaut exactement
   \(\int_{3/4}^{5/4}r\,dr=1/2\), et la révolution ajoute \(2\pi\).
3. **Dérivées des cutoffs.** Elles s'annulent identiquement sur le témoin ;
   ailleurs elles ne peuvent diminuer la fonction de distribution déjà
   minorée.
4. **Cancellation avec le fond.** Le curl de \(B\) est borné indépendamment
   de \(n\). Après (26), il ne retire au plus que la moitié de l'amplitude
   témoin conservatrice.
5. **Quasi-norme du numérateur.** Les vitesses ont amplitude et support
   uniformément bornés, ce qui suffit à (22) et (24) sans utiliser
   d'inégalité triangulaire délicate dans Lorentz.
6. **Seuil strict.** Les minorations faibles sont prises par limite à gauche
   du seuil ponctuel.
7. **Axe cylindrique.** Tous les profils sont nuls près de \(r=0\), donc les
   champs cartésiens sont lisses.
8. **Divergence.** Un swirl axisymétrique sans composantes radiale et axiale
   est exactement divergence-free.
9. **Support du curl.** Dériver un profil compact n'agrandit pas son support
   topologique au-delà de celui du profil ; les deux curls peuvent se
   recouvrir et s'annuler.
10. **Multiplicité prise pour disjonction.** À multiplicité deux, la valeur
    absolue de la somme peut être arbitrairement plus petite que les valeurs
    absolues individuelles.
11. **Non-linéarité.** Les champs \(U_{j,n}\) sont des données admissibles,
    pas des solutions dont la somme suivrait Navier--Stokes. La superposition
    n'est utilisée que dans un lemme statique.
12. **Clay.** Aucun blow-up, aucune évolution, pression, diffusion,
    projection de Leray temporelle ou solution admissible n'est construit.

## Verdict final et falsificateur

Le résultat négatif est **`VALIDER_COMME_DÉRIVATION_INTERNE`** :

\[
 \boxed{
 q(B)>0\text{ fixe},\qquad
 \max(q(U_{1,n}),q(U_{2,n}))=O(n^{-1})\to0.}    \tag{41}
\]

Un falsificateur devrait soit modifier le volume exact (17), soit exhiber une
croissance en \(n\) du numérateur faible-
\(L^3\), soit annuler sur un volume fixe le terme radial
\(-(n/r)\cos(nz)e_r\) par un curl de fond indépendant de \(n\). Les trois
possibilités sont exclues par les calculs explicites.

La prochaine réduction utile est une hypothèse anti-cancellation quantitative
sur les overlaps, par exemple une domination pointwise, une séparation
angulaire des curls ou une estimation de carré-fonction. Une simple borne de
multiplicité ne contient aucune de ces informations.
