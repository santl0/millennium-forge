# Cycle 0061 — décomposition isotypique et robustesse de la vitesse projetée

Date : 2026-08-15.

Statut : **AI_INTERNAL_DERIVATION**. Audit fonctionnel pointwise d'une
projection dans un Hilbert réel \(SO(2)\)-invariant. Aucun résultat de
régularité Navier--Stokes ou Clay.

## Verdict

Soit \(H\) un Hilbert réel séparable muni d'une représentation fortement
continue et orthogonale \(Q_\theta\) de \(SO(2)\). Sa décomposition
isotypique réelle est

\[
 H=H_0\mathbin{\widehat\oplus}\bigoplus_{m\geq1}H_m,           \tag{1}
\]

où \(H_0\) est le sous-espace fixe et chaque \(H_m\) est une somme
hilbertienne, de multiplicité éventuellement infinie, de représentations
réelles planes de fréquence \(m\). Si \(\mathcal R\) est le générateur,

\[
 \mathcal R|_{H_0}=0,\qquad
 \mathcal R|_{H_m}=mJ_m,\qquad
 J_m^*=-J_m,\quad J_m^2=-I.                                  \tag{2}
\]

Pour \(d=\partial_sZ\in H\) et \(g=\mathcal RZ\in H\), écrivons

\[
 d=\sum_{m\geq0}d_m,\qquad
 g=\sum_{m\geq1}g_m,\qquad
 g_m=mJ_mZ_m.                                                  \tag{3}
\]

Sur chaque mode actif \(g_m\neq0\), définissons

\[
 a_m=\|g_m\|^2,\qquad
 c_m=\langle d_m,g_m\rangle,\qquad
 \beta_m=\frac{c_m}{a_m}.                                     \tag{4}
\]

Alors, si \(g\neq0\),

\[
 \boxed{
 \beta=\frac{\langle d,g\rangle}{\|g\|^2}
 =\frac{\sum_{m\geq1}a_m\beta_m}
        {\sum_{m\geq1}a_m}.}                                  \tag{5}
\]

Pour une repondération scalaire positive des blocs isotypiques,

\[
 \langle x,y\rangle_\omega
 =\omega_0\langle x_0,y_0\rangle
 +\sum_{m\geq1}\omega_m\langle x_m,y_m\rangle,\qquad
 \omega_m>0,                                                   \tag{6}
\]

la vitesse projetée vaut exactement

\[
 \boxed{
 \beta_\omega
 =\frac{\sum_{m\in A}\omega_ma_m\beta_m}
        {\sum_{m\in A}\omega_ma_m},\qquad
 A=\{m\geq1:a_m>0\}.}                                         \tag{7}
\]

Il en résulte deux critères pointwise nécessaires et suffisants.

1. **Indépendance exacte de la métrique modale.** Pour \(g\neq0\),
   \(\beta_\omega=\beta_*\) pour toute pondération positive admissible si et
   seulement si

   \[
   \beta_m=\beta_*\qquad\text{pour tout }m\in A.               \tag{8}
   \]

2. **Borne en module robuste sous toutes les pondérations.** Pour
   \(B>0\),

   \[
   \inf_{\omega_m>0}|\beta_\omega|\geq B                       \tag{9}
   \]

   si et seulement si l'une des deux alternatives vaut :

   \[
   \beta_m\geq B\quad\forall m\in A,
   \qquad\text{ou}\qquad
   \beta_m\leq-B\quad\forall m\in A.                           \tag{10}
   \]

Ainsi une grande vitesse pour une métrique fixe n'est pas une propriété
robuste : elle peut être créée ou détruite par la répartition métrique entre
modes. La robustesse sous une classe de métriques uniformément conditionnées
est intermédiaire et possède un critère variationnel différent, explicité
ci-dessous.

Ces critères portent sur les poids scalaires des **blocs isotypiques**. En
présence de multiplicité interne, ils ne couvrent pas toutes les métriques
\(SO(2)\)-invariantes. L'indépendance sous toutes ces métriques exige une
condition plus forte dans chaque bloc :

\[
 d_m-\beta_*g_m\in\operatorname{span}_{\mathbb R}\{J_mg_m\}
 \quad\text{pour tout }m\in A.                                \tag{11}
\]

## 1. Décomposition isotypique réelle

Les projecteurs spectraux réels sont

\[
 P_0x=\frac1{2\pi}\int_0^{2\pi}Q_\theta x\,d\theta,            \tag{12}
\]

et, pour \(m\geq1\),

\[
 P_mx=\frac1\pi\int_0^{2\pi}
             \cos(m\theta)Q_\theta x\,d\theta.                \tag{13}
\]

Ils sont orthogonaux, \(H_m=P_mH\), et les sommes partielles de (1)
convergent dans \(H\). Sur \(H_m\),

\[
 Q_\theta
 =\cos(m\theta)I+\sin(m\theta)J_m.                             \tag{14}
\]

Le domaine du générateur est

\[
 D(\mathcal R)=
 \left\{x=\sum_{m\geq0}x_m:
       \sum_{m\geq1}m^2\|x_m\|^2<\infty\right\},              \tag{15}
\]

et

\[
 \|\mathcal Rx\|^2
 =\sum_{m\geq1}m^2\|x_m\|^2.                                 \tag{16}
\]

La formule (3) suppose donc \(Z(s)\in D(\mathcal R)\) au temps considéré.
Le sous-espace fixe \(H_0\) contribue à \(d\), mais jamais à \(g\), au
numérateur ou au dénominateur de \(\beta\).

## 2. Pourquoi les modes \(+m\) et \(-m\) ne sont pas indépendants

Après complexification,

\[
 H_{\mathbb C}
 =\widehat\bigoplus_{m\in\mathbb Z}H^{(m)},\qquad
 Q_\theta z=e^{im\theta}z\quad\text{sur }H^{(m)}.             \tag{17}
\]

La conjugaison réelle échange

\[
 \overline{H^{(m)}}=H^{(-m)}.                                 \tag{18}
\]

Le bloc réel \(H_m\) de (1) est donc la forme réelle de la paire
\(H^{(m)}\oplus H^{(-m)}\), et non la somme de deux modes réels
indépendants. Une métrique réelle scalaire doit attribuer le même poids aux
deux caractères :

\[
 \omega_{-m}=\omega_m.                                        \tag{19}
\]

Pondérer \(+m\) et \(-m\) différemment ne définit pas la repondération réelle
(6). Dans une écriture complexe, les numérateurs doivent être pris en partie
réelle et les deux caractères conjugués combinés; sinon un facteur deux ou
une quantité complexe artificielle apparaît.

Pour un champ vectoriel sur \(\mathbb R^3\), l'indice \(m\) désigne le
caractère de l'action **covariante**

\[
 (Q_\theta Z)(y)=R_\theta Z(R_{-\theta}y),
\]

pas nécessairement le numéro de Fourier de chacune des composantes
cartésiennes prise séparément.

## 3. Formule de moyenne modale

Les projecteurs \(P_m\) commutent avec \(\mathcal R\). Par orthogonalité,

\[
 \langle d,g\rangle
 =\sum_{m\geq1}\langle d_m,g_m\rangle
 =\sum_{m\in A}a_m\beta_m,                                   \tag{20}
\]

et

\[
 \|g\|^2=\sum_{m\geq1}\|g_m\|^2=\sum_{m\in A}a_m.             \tag{21}
\]

La série du numérateur est absolument convergente :

\[
 \sum_{m\geq1}|\langle d_m,g_m\rangle|
 \leq
 \left(\sum_m\|d_m\|^2\right)^{1/2}
 \left(\sum_m\|g_m\|^2\right)^{1/2}
 \leq\|d\|\,\|g\|.                                            \tag{22}
\]

Les formules (20)--(21) prouvent (5). Pour (6), il faut au minimum que

\[
 0<\sum_m\omega_m\|g_m\|^2<\infty,\qquad
 \sum_m\omega_m\|d_m\|^2<\infty.                              \tag{23}
\]

La convergence absolue du numérateur pondéré suit alors de Cauchy--Schwarz.
Si

\[
 0<c\leq\omega_m\leq C<\infty,                                \tag{24}
\]

les conditions (23) sont automatiques et la nouvelle norme est équivalente
à la norme de départ. Pour des poids positifs non uniformément bornés, (6)
peut changer la topologie et \(d,g\) doivent être contrôlés de nouveau.

La formule (7) dit que \(\beta_\omega\) appartient à l'enveloppe convexe
fermée des vitesses modales actives. Elle ne moyenne ni les fréquences
temporelles \(m\beta_m\), ni les amplitudes \(Z_m\) : ses poids naturels sont
les Gram tangentiels

\[
 a_m=\|\mathcal RZ_m\|^2=m^2\|Z_m\|^2.                       \tag{25}
\]

## 4. Interprétation d'une vitesse modale

Si, dans un bloc actif,

\[
 Z_m(s)=Q_{\vartheta(s)}Z_m^*
\]

est une orbite de rotation pure, alors

\[
 d_m=\vartheta'(s)g_m,\qquad
 \beta_m=\vartheta'(s).                                      \tag{26}
\]

La fréquence temporelle du caractère complexe \(e^{im\vartheta}\) est
\(m\vartheta'\), mais la quantité (4) retrouve la vitesse du paramètre de
groupe \(\vartheta'\).

Plus généralement, \(d_m\) peut contenir :

- une composante tangentielle parallèle à \(g_m\), mesurée par \(\beta_m\);
- une composante radiale parallèle à \(J_mg_m=-mZ_m\);
- des déformations dans l'espace de multiplicité;
- une composante orthogonale aux précédentes.

La projection scalaire ne voit directement que la première composante. Une
grande valeur de \(\beta_m\) ne prouve donc pas que le mode suit une orbite
rigide.

## 5. Robustesse sous toutes les pondérations modales

Fixons un temps et supposons \(g\neq0\). Pour tout poids admissible, posons

\[
 p_m(\omega)=
 \frac{\omega_ma_m}{\sum_{k\in A}\omega_ka_k}.
                                                                  \tag{27}
\]

Alors \(p_m(\omega)>0\), \(\sum_mp_m(\omega)=1\), et

\[
 \beta_\omega=\sum_{m\in A}p_m(\omega)\beta_m.                \tag{28}
\]

En laissant croître le conditionnement de la métrique, les poids normalisés
peuvent approcher toute probabilité de support fini sur \(A\). Par
conséquent,

\[
 \overline{\{\beta_\omega:\omega>0\text{ admissible}\}}
 =
 \overline{\operatorname{co}}\{\beta_m:m\in A\}.              \tag{29}
\]

Comme les \(\beta_m\) sont réels, le membre droit est l'intervalle fermé

\[
 [\underline\beta,\overline\beta],\qquad
 \underline\beta=\inf_{m\in A}\beta_m,\quad
 \overline\beta=\sup_{m\in A}\beta_m,                         \tag{30}
\]

avec extrémités éventuellement infinies.

### 5.1 Indépendance exacte

Si toutes les \(\beta_m\) actives valent \(\beta_*\), (28) donne
\(\beta_\omega=\beta_*\). Réciproquement, si deux modes actifs ont des
vitesses différentes, une variation positive de leur poids relatif modifie
strictement la moyenne. Cela prouve (8).

Le même critère vaut déjà pour toute classe uniformément conditionnée
contenant un voisinage non trivial de la métrique de départ : une petite
variation indépendante de chaque poids détecte toute différence modale.

### 5.2 Borne robuste en module

La distance de zéro à l'intervalle (30) est

\[
 \inf_{\omega>0}|\beta_\omega|
 =
 \operatorname{dist}
 \bigl(0,[\underline\beta,\overline\beta]\bigr).               \tag{31}
\]

Elle est positive si et seulement si toutes les vitesses modales actives ont
le même signe et sont uniformément séparées de zéro. Plus précisément, (31)
est au moins \(B>0\) si et seulement si (10) vaut. Cela prouve le critère
nécessaire et suffisant annoncé.

Si des modes de signes opposés sont actifs, une repondération peut rendre
\(\beta_\omega\) arbitrairement proche de zéro, même si aucune vitesse
modale ne l'est. Si les vitesses ont le même signe mais
\(\inf_{m\in A}|\beta_m|=0\), l'infimum métrique vaut encore zéro.

## 6. Métriques uniformément conditionnées

Une classe à conditionnement borné ne permet pas de concentrer
arbitrairement le poids. Le facteur commun aux \(\omega_m\) s'annulant dans
(7), écrivons

\[
 1\leq\omega_m\leq K,\qquad K\geq1.                          \tag{32}
\]

Notons

\[
 L_K=\inf_{1\leq\omega_m\leq K}\beta_\omega,\qquad
 U_K=\sup_{1\leq\omega_m\leq K}\beta_\omega.                  \tag{33}
\]

L'ensemble des valeurs est l'intervalle \([L_K,U_K]\). Les extrémités sont
caractérisées exactement par les zéros des fonctions monotones

\[
 \Phi_K^-(t)
 =
 \sum_{\beta_m\geq t}a_m(\beta_m-t)
 +K\sum_{\beta_m<t}a_m(\beta_m-t),                            \tag{34}
\]

\[
 \Phi_K^+(t)
 =
 K\sum_{\beta_m>t}a_m(\beta_m-t)
 +\sum_{\beta_m\leq t}a_m(\beta_m-t).                         \tag{35}
\]

Plus précisément,

\[
 \Phi_K^-(L_K)=0,\qquad \Phi_K^+(U_K)=0,                      \tag{36}
\]

avec l'interprétation par limites si une extrémité n'est pas atteinte. En
effet, pour tester \(\beta_\omega\geq t\), on minimise

\[
 \sum_m\omega_ma_m(\beta_m-t)
\]

en prenant \(\omega_m=1\) sur les coefficients positifs et
\(\omega_m=K\) sur les coefficients négatifs, ce qui donne (34). Le calcul
dual donne (35).

Le critère exact de robustesse conditionnée est donc

\[
 \inf_{1\leq\omega_m\leq K}|\beta_\omega|\geq B
 \quad\Longleftrightarrow\quad
 L_K\geq B\ \text{ou}\ U_K\leq-B.                            \tag{37}
\]

Des vitesses modales de signes opposés peuvent satisfaire (37) si les modes
opposés ont un poids de Gram trop faible pour compenser sous le
conditionnement \(K\). Ce phénomène disparaît lorsque \(K\to\infty\), où
\([L_K,U_K]\) croît vers l'intervalle (30).

Il faut donc distinguer :

- une **métrique fixe**, qui donne une seule moyenne (7);
- une **classe uniformément conditionnée**, gouvernée par (33)--(37);
- l'**infimum pointwise sur toutes les métriques**, gouverné par l'enveloppe
  convexe (29)--(31).

Une conclusion démontrée dans la première classe ne passe pas
automatiquement aux deux autres.

## 7. Multiplicité interne

Le bloc \(H_m\) peut contenir plusieurs copies, voire une multiplicité
infinie, de la représentation plane de fréquence \(m\). Il s'identifie au
réalisé réel d'un Hilbert complexe de multiplicité \(K_m\), avec \(J_m\)
jouant la multiplication par \(i\).

Après choix d'une base orthonormale interne, on peut écrire

\[
 H_m=\widehat\bigoplus_\alpha H_{m,\alpha},\qquad
 a_m=\sum_\alpha a_{m,\alpha},\qquad
 c_m=\sum_\alpha c_{m,\alpha}.                               \tag{38}
\]

Si \(a_{m,\alpha}>0\),

\[
 \beta_{m,\alpha}
 =\frac{c_{m,\alpha}}{a_{m,\alpha}},
\qquad
 \beta_m
 =\frac{\sum_\alpha
        a_{m,\alpha}\beta_{m,\alpha}}
        {\sum_\alpha a_{m,\alpha}}.                           \tag{39}
\]

Cette décomposition en copies n'est pas canonique : une transformation
unitaire de \(K_m\) mélange les indices \(\alpha\). En revanche, le bloc
isotypique \(H_m\), et donc \(a_m,c_m,\beta_m\), sont canoniques pour la
métrique de départ.

Une métrique \(SO(2)\)-invariante générale n'est pas nécessairement de la
forme scalaire (6). Elle est donnée, relativement à la métrique de départ,
par des opérateurs positifs auto-adjoints \(A_m\) qui commutent avec \(J_m\) :

\[
 \langle x,y\rangle_A
 =\langle A_0x_0,y_0\rangle
 +\sum_{m\geq1}\langle A_mx_m,y_m\rangle.                     \tag{40}
\]

Elle peut repondérer et mélanger les directions de multiplicité à
l'intérieur d'un même \(H_m\). Les critères (8)--(10) ne prétendent donc
couvrir que les poids scalaires \(\omega_mI_{H_m}\).

Pour mémoire, l'indépendance exacte de la vitesse sous **toutes** les
métriques invariantes positives est caractérisée par (11). En effet, pour
\(r_m=d_m-\beta_*g_m\), l'égalité

\[
 \operatorname{Re}\langle A_mr_m,g_m\rangle_{\mathbb C}=0
 \quad\text{pour tout }A_m=A_m^*>0                            \tag{41}
\]

équivaut à

\[
 r_m=i\lambda_mg_m
\]

dans le modèle complexe, soit
\(r_m=\lambda_mJ_mg_m\) dans le modèle réel. La composante
\(J_mg_m=-mZ_m\) est la direction radiale, orthogonale à la tangente pour
toute métrique invariant par \(J_m\). Toute autre déformation interne peut
être détectée par un choix approprié de \(A_m\).

## 8. Gram dégénéré

Le Gram global est

\[
 G=\|g\|^2=\sum_{m\geq1}a_m.                                 \tag{42}
\]

Comme \(\mathcal R=mJ_m\) est inversible sur chaque \(H_m\),

\[
 G=0
 \quad\Longleftrightarrow\quad
 Z_m=0\ \text{pour tout }m\geq1
 \quad\Longleftrightarrow\quad
 Z\in H_0.                                                     \tag{43}
\]

Au stabilisateur (43), aucune vitesse tangentielle n'est identifiable. La
convention

\[
 \beta=0\quad\text{si }g=0                                   \tag{44}
\]

est mesurable et fixe une valeur, mais n'en fait pas une vitesse physique.
Les \(\beta_m\) des modes inactifs sont indéfinies et doivent être omises
des ensembles \(A\), (28)--(31).

Lorsque \(G>0\) est petit,

\[
 |\beta|\leq\frac{\|d\|}{\|g\|}
\]

peut exploser. Seul le vecteur projeté reste uniformément contractif :

\[
 \|\beta g\|\leq\|d\|.                                       \tag{45}
\]

Une divergence de \(\beta\) peut donc mesurer une dégénérescence du Gram
plutôt qu'une rotation rapide.

## 9. Mesurabilité temporelle

Supposons \(d,g:J\to H\) fortement mesurables. Les projecteurs \(P_m\) étant
bornés, \(d_m=P_md\) et \(g_m=P_mg\) sont fortement mesurables. Les fonctions

\[
 a_m(s)=\|g_m(s)\|^2,\qquad
 c_m(s)=\langle d_m(s),g_m(s)\rangle                         \tag{46}
\]

sont mesurables. Sur \(\{a_m>0\}\), \(\beta_m=c_m/a_m\) est mesurable.
Les sommes partielles de (20)--(21) sont mesurables et convergent, la
première absolument par (22). La convention (44) donne donc une fonction
\(\beta:J\to\mathbb R\) mesurable.

Pour une suite déterministe de poids \(\omega_m\) satisfaisant (23),
\(\beta_\omega\) est également mesurable. Des poids
\(\omega_m(s)\) mesurables donnent encore une fonction mesurable sous une
domination assurant les séries, mais définissent une métrique dépendant du
temps. Ils ne doivent pas être confondus avec une métrique fixe; dériver une
norme dépendant du temps créerait des termes \(\partial_s\omega_m\).

Les extrémités \(\underline\beta,\overline\beta\) de (30) sont mesurables en
prolongeant les vitesses inactives respectivement par \(+\infty\) et
\(-\infty\), puis en prenant un infimum ou supremum dénombrable. La distance
(31) est donc mesurable. Les extrémités conditionnées peuvent être obtenues
comme zéros mesurables des fonctions (34)--(35).

## 10. Attaque des quantificateurs

### 10.1 Métrique fixe contre métrique choisie pointwise

Sur une fenêtre \(J\), les deux quantités

\[
 \operatorname*{ess\,inf}_{s\in J}
 \inf_{\omega\in\Omega}|\beta_\omega(s)|
\quad\text{et}\quad
 \inf_{\omega\in\Omega}
 \operatorname*{ess\,inf}_{s\in J}|\beta_\omega(s)|           \tag{47}
\]

ne sont pas interchangeables. La première permet à l'adversaire de choisir
une métrique différente à chaque temps et vérifie seulement

\[
 \operatorname*{ess\,inf}_{s}
 \inf_\omega|\beta_\omega(s)|
 \leq
 \inf_\omega
 \operatorname*{ess\,inf}_{s}|\beta_\omega(s)|.               \tag{48}
\]

Une hypothèse pointwise uniforme sur toutes les métriques est donc plus
forte qu'une hypothèse vérifiée séparément par chaque métrique fixe.

### 10.2 Limite en \(n\) contre infimum métrique

Même

\[
 \forall\omega\text{ fixe},\qquad
 |\beta_{n,\omega}|\longrightarrow\infty                     \tag{49}
\]

n'implique pas

\[
 \inf_\omega|\beta_{n,\omega}|\longrightarrow\infty.          \tag{50}
\]

Contre-exemple à deux modes avec \(a_1=a_2=1\) :

\[
 \beta_{n,1}=n,\qquad \beta_{n,2}=-n^2.                       \tag{51}
\]

Pour tout couple de poids positifs fixé, la moyenne tend en module vers
l'infini, dominée par le second mode. Mais le choix dépendant de \(n\)

\[
 \omega_{n,1}=n,\qquad \omega_{n,2}=1
\]

donne exactement \(\beta_{n,\omega_n}=0\). Son conditionnement croît comme
\(n\); il est exclu d'une classe (32) avec \(K\) fixé. Cet exemple sépare
les trois régimes métriques.

### 10.3 Infimum essentiel et modes inactifs

Si \(g(s)=0\) sur un ensemble de mesure positive, la convention (44) impose

\[
 \operatorname*{ess\,inf}_{s\in J}|\beta_\omega(s)|=0
\]

pour toute métrique. Une hypothèse de grande vitesse en infimum essentiel
exclut donc automatiquement un stabilisateur de mesure positive. Supprimer
les temps dégénérés avant de prendre l'infimum changerait le quantificateur.

## 11. Ce qui se transfère, ou non, à Navier--Stokes

La décomposition précédente se transfère cinématiquement à tout espace
hilbertien de distributions sur lequel l'action covariante \(SO(2)\) est
fortement continue et unitaire, notamment au Hilbert négatif pondéré du
cycle 0059, à condition que

\[
 \partial_sZ,\ \mathcal RZ\in H.
\]

Elle fournit alors :

- une décomposition orthogonale exacte en caractères azimutaux covariants;
- la formule de moyenne (7);
- un diagnostic falsifiable de dépendance métrique;
- les critères pointwise (8), (10) et (37).

Elle ne fournit pas :

- une métrique canonique imposée par Navier--Stokes;
- une borne des constantes lorsque la métrique ou l'exhaustion change;
- la synchronisation (8) des vitesses modales;
- le signe commun et le gap modal (10);
- une phase temporelle intégrable;
- la petitesse du résidu orthogonal;
- la stationnarité de la moyenne de Haar;
- un contrôle de pression ou une inégalité d'énergie critique.

La multiplicité \(K_m\) est, pour les champs sur \(\mathbb R^3\), de nature
radiale, axiale et vectorielle et typiquement infinie. Une pondération
scalaire par \(m\) ignore cette structure. En outre, la non-linéarité
Navier--Stokes couple les caractères par les triades azimutales

\[
 m_1+m_2=m_3
\]

dans la complexification. Il n'existe donc pas d'équation fermée pour chaque
\(\beta_m\) obtenue par la seule décomposition isotypique.

Enfin, une grande \(\beta_\omega\) pour une métrique fixe peut provenir de
\(\|g\|\to0\), d'un seul mode dominant, ou de poids choisis pour favoriser
ce mode. Elle ne constitue ni une vitesse physique intrinsèque ni une preuve
de rotation cohérente multi-échelle. Même le critère robuste (10), s'il était
établi, ne supprimerait pas les composantes radiales et internes de \(d_m\)
et ne donnerait pas à lui seul la rigidité PDE manquante.

## 12. Passe contradictoire

1. **Paire réelle.** Les caractères \(+m\) et \(-m\) sont conjugués; les
   pondérer indépendamment brise la structure réelle.
2. **Domaine du générateur.** Écrire \(g=\mathcal RZ\in H\) exige (15).
   Une action continue seule ne rend pas tout vecteur différentiable.
3. **Mode fixe.** \(d_0\) peut être arbitraire et ne contribue jamais à
   \(\beta\).
4. **Série du numérateur.** Sa convergence est justifiée par (22), pas par
   une permutation formelle des modes.
5. **Poids non équivalents.** Des poids positifs arbitraires peuvent changer
   la topologie; les conditions (23) sont indispensables.
6. **Moyenne signée.** Une grande moyenne fixe ne force ni signe commun ni
   borne individuelle des \(\beta_m\).
7. **Conditionnement.** Le critère toutes métriques (10) ne doit pas être
   appliqué à la classe bornée (32); son critère exact est (37).
8. **Quantificateurs.** Les limites, infimums métriques et infimums
   essentiels ne commutent pas, comme le montre (51).
9. **Multiplicité.** Les poids scalaires modaux ne couvrent pas les
   opérateurs internes \(A_m\).
10. **Indépendance complète.** Pour toutes les métriques invariantes, (8)
    seule est insuffisante; il faut (11).
11. **Gram nul.** La convention \(\beta=0\) ne résout pas
    l'identifiabilité au stabilisateur.
12. **Gram petit.** L'explosion de \(\beta\) peut être purement
    dénominateur; seule \(\beta g\) est contractive.
13. **Mesure temporelle.** Des poids dépendant de \(s\) définissent une
    métrique mobile et ajoutent des termes dans toute identité différentielle.
14. **Navier--Stokes.** La décomposition ne contrôle ni les triades, ni la
    pression non locale, ni le transfert d'énergie entre modes.
15. **Portée Clay.** Aucun des critères de robustesse n'est déduit d'un
    scénario général de blow-up admissible.

## 13. Statut logique

| Affirmation | Statut |
|---|---|
| décomposition réelle (1)--(2) | **PROUVÉ** par théorie spectrale de \(SO(2)\) |
| domaine et norme du générateur (15)--(16) | **PROUVÉ** |
| formule modale (5) | **PROUVÉ** avec convergence (22) |
| formule repondérée (7) | **PROUVÉ** sous (23) |
| indépendance sous poids scalaires \(\Leftrightarrow\) synchronisation (8) | **PROUVÉ** |
| borne robuste toutes pondérations \(\Leftrightarrow\) signe et gap (10) | **PROUVÉ** par enveloppe convexe |
| classe conditionnée | **PROUVÉ** par les extrémités (34)--(37) |
| critère sous toutes les métriques invariantes (11) | **PROUVÉ** bloc par bloc |
| mesurabilité temporelle | **PROUVÉ** pour métrique fixe et poids admissibles |
| grande vitesse dans une métrique fixe \(\Rightarrow\) robustesse | **RÉFUTÉ** |
| permutation limite / infimum métrique | **RÉFUTÉ** par (51) |
| robustesse modale \(\Rightarrow\) rigidité Navier--Stokes | **NON DÉMONTRÉ** |

**Décision formelle : CONTINUER avec séparation stricte des métriques.** La
vitesse projetée est une moyenne de vitesses modales dont les poids sont les
Gram tangentiels modifiés par la métrique. Le test discriminant naturel est
de calculer l'intervalle conditionné \([L_K,U_K]\) et de vérifier s'il reste
séparé de zéro à mesure que \(K\) augmente. Sans synchronisation modale,
une divergence observée dans une seule métrique n'est pas robuste et ne doit
pas être promue en phase Navier--Stokes.
