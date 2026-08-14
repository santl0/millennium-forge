# Cycle 0034 — Analyse du verrou `GAP-AXIALLY-DISPERSED-PURE-SWIRL-SELECTION`

**Statut :** `AI_INTERNAL_DERIVATION` — ne pas classer `PAPER_PROOF`

**Objet :** sélection d'une cellule méridienne à rapport faible-
\(L^3\)/faible-\(L^{3/2}\) non dégénéré à partir d'un rapport global non
dégénéré.

**Verdict court :** la sélection fondée sur les seules quasi-normes est
réfutée par un contre-exemple abstrait exact. Une sélection linéaire est en
revanche démontrée sous une hypothèse explicite de synchronisation des zones de
transition. Les cellules pure-swirl isotropes à profil fixe satisfont cette
hypothèse à l'échelle formelle des constantes uniformes. Le cas de cellules
pure-swirl lisses complètement arbitraires reste ouvert.

## Décision du cycle

Trois actions ont été comparées (notes sur 5 ; total sur 20).

| Action | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| Déduire directement une cellule par pigeonhole sur les quasi-normes | 2 | 5 | 5 | 4 | 16 |
| Construire des distributions disjointes à niveaux de curl échelonnés | 4 | 5 | 5 | 5 | **19** |
| Prouver une sélection sous un registre de transition synchronisé | 4 | 4 | 5 | 5 | **18** |

L'action principale est le contre-exemple exact. La troisième action est
retenue comme réduction positive : elle identifie l'hypothèse géométrique
manquante plutôt que de laisser un échec purement normique.

## Notation et formule exacte pour une somme disjointe

Pour une fonction mesurable \(f\), on fixe

\[
 \|f\|_{L^{p,\infty}}
 :=\sup_{\lambda>0}\lambda\,
       |\{x:|f(x)|>\lambda\}|^{1/p}.
\]

Si les supports des \(f_j\) sont deux à deux disjoints, alors

\[
 |\{|\sum_j f_j|>\lambda\}|=
 \sum_j |\{|f_j|>\lambda\}|.                 \tag{1}
\]

La quasi-norme de la somme n'est pourtant pas la somme des quasi-normes : le
suprémum en \(\lambda\) est pris **après** la somme des fonctions de
distribution. On a seulement

\[
 \max_j\|f_j\|_{L^{p,\infty}}
 \le \Big\|\sum_jf_j\Big\|_{L^{p,\infty}}
 \le \left(\sum_j\|f_j\|_{L^{p,\infty}}^p\right)^{1/p}.       \tag{2}
\]

La borne droite peut être arbitrairement non optimale lorsque les niveaux
d'amplitude des cellules sont séparés.

## Contre-exemple abstrait exact

Soit \(N\ge2\). Prenons des cellules mesurables \(V_j\), \(0\le j<N\), deux
à deux disjointes et de volumes

\[
 |V_j|=v_j=N^{-1}.
\]

Dans chaque \(V_j\), choisissons \(E_j\subset V_j\) de volume

\[
 s_j=N^{-1}2^{-3j/2}.
\]

Définissons, pour un vecteur unitaire fixe \(e\),

\[
 u_j={\bf1}_{V_j}e,
 \qquad
 w_j=b_j{\bf1}_{E_j}e,
 \qquad
 b_j=N^{2/3}2^j.
\]

Les quasi-normes locales sont exactement

\[
 K_{u,j}:=\|u_j\|_{L^{3,\infty}}=N^{-1/3},
 \qquad
 K_{w,j}:=\|w_j\|_{L^{3/2,\infty}}
 =b_js_j^{2/3}=1.                              \tag{3}
\]

Par conséquent,

\[
 \frac{K_{u,j}}{K_{w,j}}=N^{-1/3}
 \quad\hbox{pour tout }j.                       \tag{4}
\]

Pour \(u=\sum_j u_j\), l'amplitude vaut un sur un ensemble de volume total
un, donc

\[
 K_u:=\|u\|_{L^{3,\infty}}=1.                  \tag{5}
\]

Pour \(w=\sum_jw_j\), si \(b_k\le\lambda<b_{k+1}\), la stricte fonction de
distribution satisfait

\[
 |\{|w|>\lambda\}|
 =\sum_{j=k+1}^{N-1}s_j
 \le \frac{N^{-1}2^{-3(k+1)/2}}{1-2^{-3/2}}.
\]

En utilisant \(\lambda<b_{k+1}=N^{2/3}2^{k+1}\), et de même sous \(b_0\),
on obtient

\[
 K_w:=\|w\|_{L^{3/2,\infty}}
 \le C_*:=(1-2^{-3/2})^{-2/3}
 =1.3375547214\ldots .                          \tag{6}
\]

Réciproquement, en faisant tendre \(\lambda\) vers \(b_j\) par valeurs
inférieures, la contribution de \(E_j\) donne \(K_w\ge b_js_j^{2/3}=1\).
Ainsi

\[
 1\le K_w\le C_*,
 \qquad
 C_*^{-1}\le\frac{K_u}{K_w}\le1,              \tag{7}
\]

alors que le supremum de tous les rapports locaux tend vers zéro comme
\(N^{-1/3}\). En particulier, pour toutes constantes fixes \(c>0\) et
\(q>0\), l'implication

\[
 \sup_j\frac{K_{u,j}}{K_{w,j}}
 \ge c\left(\frac{K_u}{K_w}\right)^q           \tag{8}
\]

est fausse pour \(N\) assez grand si ses seules hypothèses sont la disjonction
des supports et le contrôle de ces quasi-normes.

La différence entre agrégation et sommation est maximale ici :

\[
 \left(\sum_jK_{u,j}^3\right)^{1/3}=1=K_u,
 \qquad
 \left(\sum_jK_{w,j}^{3/2}\right)^{2/3}=N^{2/3},
 \qquad
 K_w\le C_* .                                  \tag{9}
\]

Les volumes et amplitudes ne sont donc pas un détail : le faible-
\(L^{3/2}\) global peut voir chaque curl à un niveau différent, tandis que le
faible-\(L^3\) global agrège toutes les vitesses au même niveau.

## Ce que le contre-exemple ne démontre pas

Le couple ci-dessus est mesurable et exact, mais il n'impose ni
\(w_j=\nabla\times u_j\), ni axisymétrie, ni structure pure-swirl. Il réfute
le maillon **normique abstrait**, pas encore une sélection géométrique pour des
champs admissibles.

Son défaut géométrique est quantifiable. On a

\[
 \int|w_j|=b_js_j=N^{-1/3}2^{-j/2}.             \tag{10}
\]

Au niveau de vitesse \(t=1\), avec \(v_j=N^{-1}\) et le rapport local
\(\rho_j=N^{-1/3}\), une transition synchronisée devrait fournir une masse
de curl de taille

\[
 \frac{t\,v_j^{2/3}}{\rho_j}=N^{-1/3}.         \tag{11}
\]

La construction perd précisément le facteur \(2^{-j/2}\). Elle concentre le
curl sur une fraction de plus en plus petite de la cellule et décorrèle son
niveau critique du niveau global de vitesse.

## Lemme positif : sélection sous synchronisation de transition

Soient des paires \((u_j,w_j)\) supportées dans des cellules deux à deux
disjointes, et posons

\[
 v_j(t)=|\{|u_j|>t\}|,
 \qquad S(t)=\sum_jv_j(t).
\]

Supposons qu'à un niveau \(t>0\), pour chaque cellule active, il existe un
ensemble de registre \(\Omega_j(t)\) contenu dans la même cellule tel que

\[
 |\Omega_j(t)|\le C_0v_j(t),                   \tag{12}
\]

\[
 \int_{\Omega_j(t)}|w_j|
 \ge c_0\,\frac{t\,v_j(t)^{2/3}}{\rho_j},      \tag{13}
\]

avec \(c_0,C_0>0\) uniformes. Alors, si
\(\rho_*:=\sup_j\rho_j\),

\[
 tS(t)^{1/3}
 \le \frac{3C_0^{1/3}}{c_0}\,\rho_*K_w.       \tag{14}
\]

En effet, les registres sont disjoints et, pour
\(\Omega=\bigcup_j\Omega_j\),

\[
 \int_\Omega|w|
 \ge\frac{c_0t}{\rho_*}\sum_jv_j(t)^{2/3}
 \ge\frac{c_0t}{\rho_*}S(t)^{2/3}.             \tag{15}
\]

L'inégalité de Lorentz faible, avec sa constante élémentaire, donne

\[
 \int_\Omega|w|
 \le3K_w|\Omega|^{1/3}
 \le3K_w(C_0S(t))^{1/3},                       \tag{16}
\]

d'où (14).

Si le registre existe à un niveau \(t_*\) presque optimal pour le faible-
\(L^3\) global,

\[
 t_*S(t_*)^{1/3}\ge(1-\varepsilon)K_u,         \tag{17}
\]

alors

\[
 \rho_*
 \ge\frac{c_0(1-\varepsilon)}{3C_0^{1/3}}
       \frac{K_u}{K_w}.                         \tag{18}
\]

Enfin, si la géométrie de chaque cellule donne uniformément

\[
 \rho_j\le C_1\frac{K_{u,j}}{K_{w,j}},         \tag{19}
\]

il existe une cellule telle que

\[
 \frac{K_{u,j}}{K_{w,j}}
 \ge\frac{c_0(1-\varepsilon)}{3C_1C_0^{1/3}}
       \frac{K_u}{K_w}.                         \tag{20}
\]

Ce résultat accepte des amplitudes, volumes, rayons et échelles arbitraires :
leur hétérogénéité est absorbée dans les \(v_j(t)\). L'uniformité requise porte
uniquement sur les constantes géométriques de (12), (13) et (19).

## Vérification sur des cellules pure-swirl à profil fixe

Considérons une cellule axisymétrique standard

\[
 F_j(r,z)=A_j\,
 \eta\!\left(\frac{r-R_j}{\ell_j}\right)
 \chi\!\left(\frac{z-z_j}{\ell_j}\right),
 \qquad
 U_j=\frac{R_j}{r}F_j e_\theta,
 \qquad \ell_j\le cR_j< R_j,
\]

où \(\eta,\chi\) ont un plateau et des transitions non dégénérées fixés. La
vorticité exacte est

\[
 W_{j,r}=-\frac{R_j}{r}\partial_zF_j,
 \qquad
 W_{j,z}=\frac{R_j}{r}\partial_rF_j,
 \qquad W_{j,\theta}=0.                         \tag{21}
\]

Sur le tore support, \(r\simeq R_j\) uniformément. Les lois d'échelle sont

\[
 v_j\asymp R_j\ell_j^2,
 \qquad |U_j|\asymp A_j,
 \qquad |W_j|\asymp A_j/\ell_j
\]

sur des fractions uniformes du plateau et des transitions. Il vient

\[
 K_{u,j}\asymp A_j(R_j\ell_j^2)^{1/3},
\]

\[
 K_{w,j}\asymp \frac{A_j}{\ell_j}
                    (R_j\ell_j^2)^{2/3},
 \qquad
 \rho_j\asymp\frac{K_{u,j}}{K_{w,j}}
 \asymp\left(\frac{\ell_j}{R_j}\right)^{1/3}.  \tag{22}
\]

La masse de curl de transition vérifie

\[
 \int_{\Omega_j}|W_j|\asymp A_jR_j\ell_j.      \tag{23}
\]

Au niveau de plateau \(t\asymp A_j\), le membre droit requis par (13) est

\[
 \frac{t\,v_j^{2/3}}{\rho_j}
 \asymp
 \frac{A_j(R_j\ell_j^2)^{2/3}}
      {(\ell_j/R_j)^{1/3}}
 =A_jR_j\ell_j,                                \tag{24}
\]

exactement la même échelle que (23). Le lemme positif s'applique donc aux
cellules de profil fixe si le niveau global presque optimal appartient à une
plage de plateau uniforme pour toutes les cellules actives.

Cette dernière phrase est une hypothèse réelle, non une conséquence des seules
quasi-normes. Des profils dont les plateaux, fractions de transition ou
variations dégénèrent peuvent faire perdre l'uniformité de \(c_0,C_0,C_1\).

## Passe contradictoire

1. **Quasi-norme de somme remplacée par somme des quasi-normes.** Faux en
   général, et l'écart \(N^{2/3}/C_*\) dans (9) diverge.
2. **Niveau local du curl supposé synchronisé avec le niveau global de
   vitesse.** C'est le premier quantificateur non justifié ; (10)--(11)
   fournissent le défaut exact.
3. **Disjonction méridienne.** Elle doit inclure les supports complets des
   transitions dérivées. La simple disjonction des plateaux ne suffit pas.
4. **Annulation du curl.** Pour des supports réellement disjoints, elle est
   absente. Si des couches de transition se recouvrent, les contributions aux
   mêmes composantes de (21) peuvent s'annuler avant le calcul de la fonction
   de distribution.
5. **Facteur cylindrique.** Les estimations uniformes exigent
   \(r\simeq R_j\), par exemple \(\ell_j\le cR_j\) avec \(c<1\). Une cellule
   touchant l'axe n'est pas couverte.
6. **Amplitudes et volumes arbitraires.** Ils ne posent pas de difficulté dans
   (15), grâce à la concavité
   \(\sum_jv_j^{2/3}\ge(\sum_jv_j)^{2/3}\). Ce sont les constantes de profil,
   non les tailles elles-mêmes, qui doivent rester uniformes.
7. **Raccord PDE.** Aucune évolution de Navier--Stokes n'est utilisée ici. Le
   résultat est un lemme statique de sélection pour un champ à un instant
   donné ; il ne constitue ni critère de régularité ni scénario de blow-up.

## Verdict, falsificateur et prochaine réduction

- **Sélection par les seules quasi-normes : `ABANDONNER`.** Le contre-exemple
  (3)--(8) est exact.
- **Sélection de cellules à profils uniformes synchronisés : `CONTINUER`.** Le
  lemme (12)--(20) donne un rapport local au moins linéaire en \(K_u/K_w\).
- **Sélection pour toute famille pure-swirl lisse disjointe : `À REPRENDRE`.**
  Le contre-exemple abstrait n'est pas encore réalisé sous la contrainte
  \(W_j=\nabla\times U_j\).

Le **premier quantificateur faux** est : « pour toute famille de distributions
faibles appariées et disjointes, un rapport global non dégénéré impose un
rapport local non dégénéré ». Il traite implicitement le niveau réalisant
\(K_{w,j}\) comme s'il était synchronisé avec un niveau presque optimal commun
pour \(K_u\).

Un **falsificateur décisif** de la sélection pure-swirl générale serait une
suite explicite de cellules \(F_{j,N}\in C_c^\infty\), à supports de transition
disjoints, telle que

\[
 \inf_N K_u/K_w>0,
 \qquad
 \max_jK_{u,j}/K_{w,j}\longrightarrow0.
\]

Le calcul devrait inclure tout le curl de raccord et de base, pas seulement
une sous-couche artificielle à fort gradient. Réciproquement, une famille
satisfaisant (12)--(13) avec constantes uniformes mais violant (20)
falsifierait le lemme positif ; la démonstration montre qu'un tel résultat
signalerait nécessairement une erreur dans les fonctions de distribution ou
la disjonction.

La **prochaine réduction** est unique : démontrer, par coaire et/ou
isopérimétrie pondérée cylindrique, un registre de transition de la forme
(12)--(13) pour une troncature de chaque cellule pure-swirl au **même** niveau
global presque optimal. Si cette borne échoue, construire une famille lisse
pure-swirl qui reproduit les niveaux échelonnés du contre-exemple tout en
payant explicitement le curl de toutes les transitions.

## Addendum contradictoire — audit de la formulation finale du théorème BV

Cet addendum audite littéralement le théorème principal désormais formulé
dans `cycle-0034-heterogeneous-cell-selection.md`. La famille est finie, les
cellules \(Q_j\) sont disjointes, \(U_j,W_j\) sont supportés dans \(Q_j\), et

\[
 |Q_j|\le C_0v_j,\qquad
 |E_j|\ge c_0v_j,\qquad
 |U_j|\ge c_2A_j\ \hbox{sur }E_j,
\]

\[
 |U_j|\le C_2A_j\ \hbox{sur }Q_j,
 \qquad
 \int_{Q_j}|W_j|\ge c_1A_jv_j^{2/3}.           \tag{25}
\]

Toutes les constantes sont strictement positives et uniformes. Le cas
\(K_u>0\) implique que la famille n'est pas vide. Le registre dans (25)
implique alors \(K_w>0\) : si \(K_w=0\), \(W=0\) presque partout, ce qui
contredit le registre de toute cellule. Les divisions par \(K_w\) sont donc
légitimes.

### Vérification ligne par ligne de la sélection

Posons

\[
 a_0=c_2c_0^{1/3},
 \qquad
 \varepsilon=\max_jK_{u,j}.
\]

1. Le plateau donne, avec le bon sens d'inégalité,

   \[
   K_{u,j}\ge c_2A_j|E_j|^{1/3}
   \ge a_0A_jv_j^{1/3}.                        \tag{26}
   \]

2. Pour \(0<\eta<1\), choisissons \(\lambda>0\) tel que, si
   \(m(\lambda)=|\{|U|>\lambda\}|\),

   \[
   \lambda m(\lambda)^{1/3}\ge(1-\eta)K_u.
   \]

   Il faut interpréter une cellule qui « rencontre » ce superniveau comme
   une cellule dont l'intersection a une mesure positive. Pour l'ensemble
   correspondant \(J_\lambda\), la borne \(|U_j|\le C_2A_j\) impose
   \(A_j>\lambda/C_2\). Avec
   \(S=\sum_{j\in J_\lambda}v_j\), la disjonction et la borne sur les boîtes
   donnent

   \[
   m(\lambda)\le\sum_{j\in J_\lambda}|Q_j|
   \le C_0S,
   \]

   donc

   \[
   \lambda S^{1/3}
   \ge(1-\eta)C_0^{-1/3}K_u.                  \tag{27}
   \]

3. Pour chaque \(j\in J_\lambda\), (26) et
   \(A_j>\lambda/C_2\) donnent

   \[
   v_j^{1/3}<\frac{C_2\varepsilon}{a_0\lambda}.
   \]

   Le passage décisif conserve bien le sens :

   \[
   v_j^{2/3}=\frac{v_j}{v_j^{1/3}}
   \ge\frac{a_0\lambda}{C_2\varepsilon}v_j.
   \]

   Par sommation,

   \[
   \sum_{j\in J_\lambda}v_j^{2/3}
   \ge\frac{a_0\lambda S}{C_2\varepsilon}.     \tag{28}
   \]

4. Comme les supports complets de \(W_j\) sont disjoints, sur
   \(Q=\bigcup_{j\in J_\lambda}Q_j\),

   \[
   \int_Q|W|
   =\sum_{j\in J_\lambda}\int_{Q_j}|W_j|
   \ge\frac{c_1a_0\lambda^2S}
            {C_2^2\varepsilon}.                \tag{29}
   \]

   Il n'y a ici ni inégalité triangulaire inversée ni hypothèse de signe : la
   disjonction rend l'égalité initiale exacte.

5. L'intégration de la fonction de distribution faible-
   \(L^{3/2}\) donne

   \[
   \int_Q|W|\le3K_w|Q|^{1/3}
   \le3K_w(C_0S)^{1/3}.                        \tag{30}
   \]

6. Les équations (29)--(30) impliquent

   \[
   \varepsilon\ge
   \frac{c_1a_0}{3C_2^2C_0^{1/3}}
   \frac{\lambda^2S^{2/3}}{K_w}.
   \]

   En élevant (27) au carré, puis en laissant \(\eta\downarrow0\), on obtient
   exactement

   \[
   \boxed{\varepsilon\ge
   c_{BV}\frac{K_u^2}{K_w}},
   \qquad
   c_{BV}=\frac{c_1a_0}{3C_2^2C_0}.             \tag{31}
   \]

   Le facteur \((1-\eta)^2\), présent avant la limite, est correctement
   éliminé. La puissance entière \(C_0^{-1}\) vient de
   \(C_0^{-1/3}C_0^{-2/3}\).

7. La finitude de la famille permet de choisir \(j_*\) avec
   \(K_{u,j_*}=\varepsilon\). La monotonie des fonctions de distribution sur
   des supports disjoints donne \(K_{w,j_*}\le K_w\). Ainsi

   \[
   K_{u,j_*}\ge c_{BV}\frac{K_u^2}{K_w},
   \qquad
   \boxed{\frac{K_{u,j_*}}{K_{w,j_*}}
   \ge c_{BV}\left(\frac{K_u}{K_w}\right)^2}. \tag{32}
   \]

Les deux conclusions ont donc les bons sens, puissances et constantes. Pour
une famille infinie, le maximum pourrait ne pas être atteint ; cette extension
n'est pas revendiquée.

### Recherche de contre-exemple sous toutes les hypothèses

Aucun contre-exemple ne subsiste sous (25). Les quatre mécanismes adverses
naturels sont neutralisés par des hypothèses différentes :

- des volumes \(v_j\) arbitrairement petits sont absorbés par (28) ;
- des amplitudes \(A_j\) échelonnées sont filtrées au niveau commun
  \(\lambda\) ;
- une pointe de vitesse cachée est exclue par \(|U_j|\le C_2A_j\) ;
- un curl repoussé sur un niveau minuscule reste soumis à sa masse \(L^1\)
  minimale dans (25), tandis qu'une boîte artificiellement immense est
  exclue par \(|Q_j|\le C_0v_j\).

Un falsificateur littéral devrait satisfaire simultanément (26)--(30) et
violer (31), ce qui est algébriquement impossible. Les seules sorties sont la
dégénérescence d'une constante uniforme, le recouvrement des supports, ou la
suppression d'une des bornes de (25). Le contre-exemple dyadique précédent
échoue précisément sur le registre \(L^1\), donc ne falsifie pas ce théorème.

### Audit du corollaire pure-swirl par troncature et coaire

Pour

\[
 U_j=(R_j/r)F_je_\theta,
 \qquad
 \operatorname{supp}F_j\subset
 \{R_j/2<r<3R_j/2,\ |z-z_j|<\Lambda R_j\},
\]

prenons pour \(Q_j\) la boîte torique tridimensionnelle complète. Son volume
vérifie explicitement

\[
 |Q_j|\le4\pi\Lambda R_j^3.                    \tag{33}
\]

Avec \(v_j=R_j^3\), le superniveau plan de mesure au moins
\(c_ER_j^2\) engendre un ensemble tridimensionnel de volume au moins
\(\pi c_ER_j^3\). Sur celui-ci,

\[
 |U_j|\ge\frac23c_AA_j,
 \qquad
 |U_j|\le2C_AA_j\quad\hbox{sur }Q_j.           \tag{34}
\]

On peut donc prendre, par exemple,

\[
 C_0=4\pi\Lambda,
 \quad c_0=\pi c_E,
 \quad c_2=2c_A/3,
 \quad C_2=2C_A.
\]

Pour le registre, l'un des deux ensembles
\(\{F_j\ge c_AA_j\}\) ou \(\{F_j\le-c_AA_j\}\) a une aire au moins
\(c_ER_j^2/2\). Avec son signe \(\sigma_j\), posons

\[
 G_j=(\sigma_jF_j-c_AA_j/2)_+.
\]

Sur cet ensemble, \(G_j\ge c_AA_j/2\). L'inégalité BV--Sobolev plane, ou de
façon équivalente coaire plus isopérimétrie, fournit

\[
 \operatorname{TV}(G_j)
 \ge C_{\rm iso}^{-1}\|G_j\|_{L^2}
 \ge \frac{c_A}{2C_{\rm iso}}
       \sqrt{\frac{c_E}{2}}\,A_jR_j.           \tag{35}
\]

Le facteur cylindrique se compense exactement avec le jacobien :

\[
 \|\nabla\times[(R_j/r)G_je_\theta]\|_{L^1(\mathbb R^3)}
 =2\pi R_j\operatorname{TV}(G_j).              \tag{36}
\]

Comme \(|\nabla G_j|\le|\nabla F_j|\) presque partout,

\[
 \int|W_j|
 =2\pi R_j\int|\nabla F_j|\,dr\,dz
 \ge \frac{\pi c_A}{C_{\rm iso}}
       \sqrt{\frac{c_E}{2}}\,A_jR_j^2.         \tag{37}
\]

C'est exactement (25), avec une constante \(c_1\) indépendante de
\(A_j,R_j,z_j\). La compacité de \(F_j\) rend \(G_j\) compact ; sa seule
régularité lipschitzienne suffit dans BV. Le raccord est donc valide si les
**boîtes tridimensionnelles complètes**, et non seulement les plateaux, sont
disjointes et si \(\Lambda,c_A,C_A,c_E\) restent uniformes. Il ne couvre ni
les cellules touchant l'axe, ni l'aspect \(\Lambda\to\infty\), ni une densité
de plateau \(c_E\to0\).

### Composition avec le gate directionnel et exposant 12

Sur la cellule sélectionnée, le gate du cycle 0033 donne, pour toute extension
admissible \(\zeta\) de la direction du curl,

\[
 \operatorname{MO}_{B_{j_*}}(\zeta)
 \ge c_\Lambda
 \left(\frac{K_{u,j_*}}{K_{w,j_*}}\right)^6.  \tag{38}
\]

Une extension globale de la direction de \(W=\sum_jW_j\) est bien admissible
pour \(W_{j_*}\) sur \(B_{j_*}\) : sur le support de \(W_{j_*}\), les curls
disjoints coïncident, et ailleurs les valeurs sont libres dans la définition
du gate local. Même si la boule contient une autre cellule, la contrainte
supplémentaire sur \(\zeta\) ne nuit pas à une borne valable pour **toute**
extension locale.

L'insertion de (32) dans (38) donne sans perte de puissance

\[
 \boxed{\operatorname{MO}_{B_{j_*}}(\zeta)
 \ge c_\Lambda c_{BV}^{6}
 \left(\frac{K_u}{K_w}\right)^{12}}.           \tag{39}
\]

L'exposant \(12\) est donc exactement le produit de l'exposant de sélection
\(2\) et de l'exposant directionnel \(6\). La conclusion exige que
\(c_\Lambda\) et les constantes entrant dans \(c_{BV}\) restent uniformes le
long de la famille.

### Cas où le rayon sélectionné ne tend pas vers zéro

Le théorème sélectionne un rapport endpoint, pas une échelle. Pour une suite
de familles, notons \(R_{j_*(n)}\) le rayon de la cellule choisie.

- Si \(R_{j_*(n)}\to0\), (39), combiné à un rapport global uniformément
  positif, impose une oscillation non nulle sur des boules qui rétrécissent et
  le poids logarithmique diverge.
- La même contradiction uniforme suit déjà de
  \(\liminf_nR_{j_*(n)}=0\), après extraction d'une sous-suite.
- Si \(\liminf_nR_{j_*(n)}>0\), (39) ne donne qu'une borne inférieure
  d'oscillation sur une échelle macroscopique. Elle est compatible avec une
  borne log-BMO uniforme ; si \(C_\Lambda R_{j_*(n)}\ge1/2\), la boule peut
  même se trouver hors de la fenêtre locale utilisée par le seminorme.

Ainsi l'implication « rapport sélectionné \(\Rightarrow\) divergence
log-BMO » est fausse sans un lemme supplémentaire forçant une sous-suite de
rayons sélectionnés vers zéro. C'est le premier quantificateur encore ouvert
après validation du théorème BV ; il relève de la localisation dynamique, pas
de l'algèbre de sélection statique.
