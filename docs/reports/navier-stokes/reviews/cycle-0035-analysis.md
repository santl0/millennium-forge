# Cycle 0035 — Audit analytique des cellules dégénérées et du registre de niveau

**Statut :** `AI_INTERNAL_DERIVATION` — ne pas classer `PAPER_PROOF`

**Verrou :** `GAP-DEGENERATE-CELL-REGISTER`, régime
\(|Q_j|/v_j\to\infty\).

**Verdict :** un halo de volume \(O(v_j)\) ne découle pas du plateau effectif,
de la borne d'amplitude, de \(W_j=\operatorname{curl}U_j\) et d'un registre
BV global. Un contre-exemple pure-swirl lisse et exactement curl-compatible le
réfute. Pour les cellules pure-swirl annulaires, un théorème plus fort évite
toutefois le halo fixé a priori : deux bandes construites au niveau global
presque optimal donnent directement la sélection quadratique, sans borne
axiale ni volume \(v_j\).

## Décision du cycle

| Action | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| Déduire un halo \(O(v_j)\) du seul registre BV total | 3 | 4 | 5 | 4 | 16 |
| Dilater un pur swirl et tester toute localisation de volume fixé | 4 | 5 | 5 | 5 | 19 |
| Remplacer \(v_j\) par des bandes au niveau global \(\lambda\) | 5 | 5 | 5 | 5 | **20** |

La troisième action est le lemme actif. La deuxième fournit le falsificateur
exact de la formulation naïve et identifie son premier quantificateur faux.

## Équation, domaine et type d'objet

Le problème Clay de référence est

\[
 \partial_tu+(u\cdot\nabla)u=-\nabla p+\nu\Delta u,
 \qquad \nabla\cdot u=0,
 \qquad \nu>0,
 \qquad f=0,
\]

sur \(\mathbb R^3\). Le présent cycle est strictement statique : il traite des
champs lisses compacts à un instant fixé et ne construit aucune trajectoire de
Navier--Stokes.

Pour chaque cellule pure-swirl,

\[
 U_j=\frac{R_j}{r}F_j(r,z)e_\theta,
 \qquad
 W_j=\operatorname{curl}U_j
 =\frac{R_j}{r}
   \left(-\partial_zF_j e_r+\partial_rF_j e_z\right).   \tag{1}
\]

Cette forme est exactement divergence-free. On utilise

\[
 K_u=\|U\|_{L^{3,\infty}},
 \qquad
 K_w=\|W\|_{L^{3/2,\infty}},
 \qquad
 K_{u,j}=\|U_j\|_{L^{3,\infty}},
 \qquad
 K_{w,j}=\|W_j\|_{L^{3/2,\infty}}.             \tag{2}
\]

## Résultat négatif : le halo \(O(v)\) n'est pas automatique

### Énoncé réfuté

L'implication suivante est fausse avec des constantes universelles
\(\Gamma,\gamma>0\) :

> Si \(U\) possède un plateau d'amplitude \(A\) et de volume au moins
> \(c_0v\), si \(|U|\le C_2A\), si \(W=\operatorname{curl}U\), et si
> \(\int_Q|W|\ge c_1Av^{2/3}\), alors il existe
> \(H\subset Q\) tel que
> \(|H|\le\Gamma v\) et
> \(\int_H|W|\ge\gamma Av^{2/3}\).

Le contre-exemple ci-dessous montre plus : aucun ensemble mesurable de ce
volume, même choisi loin du plateau et sans contrainte métrique de « halo »,
ne porte le registre demandé.

### Contre-exemple pure-swirl lisse

Fixons

\[
 \Phi\in C_c^\infty
 \bigl(\{1/2<\rho<3/2,\ |\zeta|<1\}\bigr),
\]

non constante, avec \(\Phi=1\) sur un ouvert
\(P\Subset\{3/4<\rho<5/4,\ |\zeta|<1/2\}\). Pour \(L\ge1\), posons

\[
 R_L=L,
 \qquad A_L=L^{-1},
 \qquad
 F_L(r,z)=A_L\Phi(r/L,z/L),
\]

\[
 U_L=\frac{L}{r}F_Le_\theta,
 \qquad W_L=\operatorname{curl}U_L.             \tag{3}
\]

Le champ est lisse, compact, divergence-free et supporté loin de l'axe. Dans
les variables \(\rho=r/L\), \(\zeta=z/L\),

\[
 |W_L|
 =\frac{A_L}{L\rho}|\nabla\Phi(\rho,\zeta)|,
 \qquad
 dx=L^3\rho\,d\rho\,d\theta\,d\zeta.          \tag{4}
\]

Il existe donc des constantes fixes positives \(q_0,b_0,M_0,k_u,k_w\), ne
dépendant que de \(\Phi\), telles que

\[
 |Q_L|=q_0L^3,
 \qquad
 \int|W_L|=b_0A_LL^2=b_0L,
 \qquad
 \|W_L\|_\infty\le M_0\frac{A_L}{L}=M_0L^{-2}, \tag{5}
\]

et, exactement par changement d'échelle,

\[
 \|U_L\|_{L^{3,\infty}}=k_uA_LL=k_u,
 \qquad
 \|W_L\|_{L^{3/2,\infty}}=k_wA_LL=k_w.         \tag{6}
\]

Dans la grande région correspondant à \(P\), \(|U_L|\) est comparable à
\(A_L\) et \(W_L=0\). Pour \(L\) assez grand, choisissons dans cette région
un ensemble \(E_L\) de volume exactement un et déclarons

\[
 v_L=1.
\]

Les constantes de plateau et d'amplitude sont uniformes : par exemple
\(|U_L|\ge(4/5)A_L\) sur \(E_L\) et
\(|U_L|\le2\|\Phi\|_\infty A_L\) sur \(Q_L\). Le registre BV global est
sur-satisfait,

\[
 \int_{Q_L}|W_L|=b_0L
 \ge b_0A_Lv_L^{2/3}=b_0/L.                    \tag{7}
\]

Cependant, pour tout \(H_L\subset Q_L\) tel que
\(|H_L|\le\Gamma v_L=\Gamma\),

\[
 \int_{H_L}|W_L|
 \le\|W_L\|_\infty|H_L|
 \le M_0\Gamma L^{-2}.                         \tag{8}
\]

Le quotient entre (8) et le registre local demandé
\(\gamma A_Lv_L^{2/3}=\gamma/L\) tend vers zéro. Pour
\(L>M_0\Gamma/\gamma\), aucun tel halo n'existe.

La famille est finie à chaque \(L\) — elle ne comporte qu'une cellule — et

\[
 \frac{|Q_L|}{v_L}=q_0L^3\longrightarrow\infty. \tag{9}
\]

En outre, tout superniveau à une fraction fixe de \(A_L\) contenant le
plateau a un volume \(\asymp L^3\), et la distance entre un petit
\(E_L\Subset P_L\) et la zone de transition peut être \(\asymp L\). Le défaut
n'est donc pas un mauvais choix de forme du halo.

### Premier quantificateur faux

Le plateau du claim C34 fournit seulement **un minorant**
\(|E_j|\ge c_0v_j\). Il ne fournit aucun majorant du superniveau complet, ni
aucune calibration de \(v_j\) par le volume réellement actif. Même imposer
\(|E_j|=v_j\) à l'ensemble témoin choisi ne suffit pas : dans (3), on peut
choisir \(|E_L|=v_L=1\) à l'intérieur d'un plateau total de volume
\(\asymp L^3\).

Le premier quantificateur faux est donc

\[
 \text{« pour tout volume témoin }v_j\text{ minorant un plateau, il existe
 un superniveau/halo de volume }O(v_j)\text{ ».}          \tag{10}
\]

Si l'on choisit au contraire le volume naturel
\(v_L\asymp L^3\), alors \(|Q_L|/v_L\asymp1\) et le contre-exemple disparaît.
Il falsifie l'inférence à partir des hypothèses littérales, pas un registre
où \(v_j\) serait défini par un superniveau complet à deux côtés.

## Pourquoi le faible-\(L^{3/2}\) ne localise pas le registre

Sous la normalisation critique (3), le curl a amplitude
\(O(L^{-2})\) sur un volume \(O(L^3)\). Par conséquent,

\[
 K_w\asymp L^{-2}(L^3)^{2/3}\asymp1,
 \qquad
 \|W_L\|_{L^1}\asymp L^{-2}L^3\asymp L.       \tag{11}
\]

L'inégalité de Lorentz

\[
 \int_H|W|\le3K_w|H|^{1/3}                    \tag{12}
\]

autorise exactement cette croissance sur le support total, mais elle
n'impose aucune tension spatiale. Sur un ensemble de volume fixé, la vraie
masse de (3) est même \(O(L^{-2})\), bien plus petite que la borne droite de
(12).

Les quatre attaques ont donc des statuts distincts.

- **Queue de faible amplitude sous un seuil de troncature.** Elle peut être
  supprimée dans la représentation scalaire pure-swirl et n'est pas, à elle
  seule, un obstacle si le registre de fermeture reste dans un halo compact.
- **Longue connexion au-dessus du seuil.** Elle fait croître le volume du
  superniveau ; aucune borne \(O(v_j)\) ne suit du plateau minoré.
- **Curl diffus sur un grand support.** C'est le mécanisme exact de (3)--(8) :
  la masse BV totale est grande, mais aucune fraction uniforme n'est locale.
- **Contrôle faible-\(L^{3/2}\).** Il contrôle l'intégrale une fois l'ensemble
  localisé ; il ne construit pas cet ensemble et ne borne pas son volume.

Pour un champ vectoriel général, l'identité
\(W=\operatorname{curl}U\) ne suffit pas non plus à tronquer \(|U|\) : la
troncature crée des termes de direction et ne commute ni avec le curl ni avec
la divergence. Le raccord positif ci-dessous utilise de façon essentielle la
représentation scalaire (1).

## Lemme minimal si un halo localisé est fourni

Le volume de la boîte complète n'est pas nécessaire. Soit \(\lambda\) un
niveau presque optimal pour \(K_u\), et \(J_\lambda\) les cellules actives.
Supposons les conditions de plateau et d'amplitude de C34, mais remplaçons la
borne sur \(Q_j\) et le registre total par des ensembles disjoints
\(H_j(\lambda)\subset Q_j\) tels que

\[
 \{|U_j|>\lambda\}\subset H_j(\lambda),
 \qquad
 |H_j(\lambda)|\le\Gamma v_j,                  \tag{13}
\]

\[
 \int_{H_j(\lambda)}|W_j|
 \ge\gamma A_jv_j^{2/3}.                       \tag{14}
\]

Alors la preuve C34 s'applique mot pour mot avec
\(C_0\) remplacé par \(\Gamma\) et \(c_1\) par \(\gamma\). Si
\(a_0=c_2c_0^{1/3}\), elle sélectionne une cellule telle que

\[
 K_{u,j}\ge
 \frac{\gamma a_0}{3C_2^2\Gamma}\frac{K_u^2}{K_w},
 \qquad
 \frac{K_{u,j}}{K_{w,j}}\ge
 \frac{\gamma a_0}{3C_2^2\Gamma}
 \left(\frac{K_u}{K_w}\right)^2.              \tag{15}
\]

Les deux parties de (13) sont nécessaires dans cette preuve : le halo doit
contrôler à la fois le volume du superniveau de vitesse utilisé pour
\(K_u\) et le support sur lequel le registre de curl est intégré. Les
hypothèses réfutées dans (10) ne dérivent ni l'une ni l'autre uniformément.

## Théorème renforcé : bandes dynamiques pure-swirl

Le lemme suivant supprime \(Q_j/v_j\) et même le volume \(v_j\), sans chercher
à prouver (13). C'est une conclusion propre à la géométrie pure-swirl.

### Hypothèses exactes

Soit une famille finie de
\(F_j\in C_c^\infty((0,\infty)\times\mathbb R)\) telle que

\[
 \operatorname{supp}F_j
 \subset\{R_j/2<r<3R_j/2\},                   \tag{16}
\]

sans aucune borne sur le diamètre axial. Les supports tridimensionnels
complets sont deux à deux disjoints. Définissons \(U_j,W_j\) par (1), puis
\(U=\sum_jU_j\), \(W=\sum_jW_j\). Supposons

\[
 0<K_u<\infty,
 \qquad K_w<\infty.                            \tag{17}
\]

La compacité et la finitude rendent ces normes finies automatiquement ; la
condition utile est \(K_u>0\).

### Conclusion

Il existe une cellule \(j_*\) telle que

\[
 \boxed{K_{u,j_*}\ge
 \frac{C_I}{324}\frac{K_u^2}{K_w}},           \tag{18}
\]

\[
 \boxed{\frac{K_{u,j_*}}{K_{w,j_*}}
 \ge\frac{C_I}{324}
 \left(\frac{K_u}{K_w}\right)^2},             \tag{19}
\]

où \(C_I>0\) est une constante admissible dans l'isopérimétrie
tridimensionnelle

\[
 \operatorname{Per}(E)\ge C_I|E|^{2/3}.       \tag{20}
\]

### Audit des inclusions de niveaux

Choisissons \(0<\eta<1\) et \(\lambda>0\) tels que

\[
 \lambda\mu_U(\lambda)^{1/3}
 \ge(1-\eta)K_u,                              \tag{21}
\]

où \(\mu_U(t)=|\{|U|>t\}|\). Pour chaque signe
\(\sigma\in\{-1,+1\}\), posons

\[
 E_{j,\sigma}=\{\sigma F_j>\lambda/2\},
 \qquad V_{j,\sigma}=|E_{j,\sigma}|,          \tag{22}
\]

\[
 H_{j,\sigma}
 =\{\lambda/4<\sigma F_j<\lambda/2\}.         \tag{23}
\]

Les volumes sont tridimensionnels, avec le jacobien cylindrique. Sur (16),

\[
 \frac23\le\frac{R_j}{r}\le2.                \tag{24}
\]

Les trois inclusions annoncées ont donc les bons sens :

\[
 \{|U|>\lambda\}
 \subset\bigcup_{j,\sigma}E_{j,\sigma},       \tag{25}
\]

car \(|U_j|>\lambda\) implique
\(|F_j|>\lambda/2\) ;

\[
 E_{j,\sigma}\subset\{|U_j|>\lambda/3\},     \tag{26}
\]

car \((2/3)(\lambda/2)=\lambda/3\) ; et

\[
 H:=\bigcup_{j,\sigma}H_{j,\sigma}
 \subset\{|U|>\lambda/6\},                   \tag{27}
\]

car \((2/3)(\lambda/4)=\lambda/6\). Les deux bandes de signes sont
disjointes, comme le sont les supports des différentes cellules.

En posant

\[
 V=\sum_{j,\sigma}V_{j,\sigma},
\]

(25) donne

\[
 V\ge\mu_U(\lambda).                          \tag{28}
\]

### Audit de coaire et de l'isopérimétrie

Étendons \(F_j(r,z)\) en une fonction axisymétrique sur \(\mathbb R^3\).
Elle est lisse car son support reste à distance positive de l'axe. Pour
presque tout \(t\), son superniveau signé est de périmètre fini et (20)
s'applique. La formule de coaire tridimensionnelle donne, pour chaque paire
\((j,\sigma)\) avec \(V_{j,\sigma}>0\),

\[
 \begin{aligned}
 \int_{H_{j,\sigma}}|\nabla F_j|\,dx
 &=\int_{\lambda/4}^{\lambda/2}
   \operatorname{Per}(\{\sigma F_j>t\})\,dt\\
 &\ge \frac{C_I\lambda}{4}V_{j,\sigma}^{2/3}.
 \end{aligned}                                  \tag{29}
\]

Les termes de volume nul doivent simplement être omis avant toute division.
L'identité pure-swirl (1) et (24) donnent alors

\[
 \int_{H_{j,\sigma}}|W_j|
 \ge\frac{C_I\lambda}{6}V_{j,\sigma}^{2/3}.   \tag{30}
\]

Cette étape n'utilise aucune borne axiale. C'est précisément l'isopérimétrie
tridimensionnelle, et non une isopérimétrie méridienne à constante dépendant
de l'aspect, qui absorbe une connexion longue.

### Audit de la sélection et de la constante 324

Posons

\[
 \varepsilon=\max_jK_{u,j}.
\]

Par (26), pour tout terme de volume positif,

\[
 \frac{\lambda}{3}V_{j,\sigma}^{1/3}
 \le K_{u,j}\le\varepsilon,
 \qquad
 V_{j,\sigma}^{1/3}\le\frac{3\varepsilon}{\lambda}. \tag{31}
\]

Le sens de l'étape de pigeonhole est donc

\[
 V_{j,\sigma}^{2/3}
 =\frac{V_{j,\sigma}}{V_{j,\sigma}^{1/3}}
 \ge\frac{\lambda}{3\varepsilon}V_{j,\sigma}. \tag{32}
\]

En sommant (30)--(32) et en utilisant la disjonction,

\[
 \int_H|W|
 \ge\frac{C_I\lambda^2}{18\varepsilon}V
 \ge\frac{C_I\lambda^2}{18\varepsilon}
       \mu_U(\lambda).                         \tag{33}
\]

D'autre part, (27) et la définition de \(K_u\) donnent

\[
 |H|^{1/3}
 \le\mu_U(\lambda/6)^{1/3}
 \le\frac{6K_u}{\lambda}.                     \tag{34}
\]

L'inégalité faible-Lorentz exacte fournit

\[
 \int_H|W|
 \le3K_w|H|^{1/3}
 \le\frac{18K_wK_u}{\lambda}.                 \tag{35}
\]

La comparaison de (33) et (35) donne

\[
 \varepsilon
 \ge\frac{C_I}{324}
 \frac{\lambda^3\mu_U(\lambda)}{K_wK_u}.      \tag{36}
\]

Enfin, le cube de (21) implique

\[
 \lambda^3\mu_U(\lambda)
 \ge(1-\eta)^3K_u^3.
\]

En laissant \(\eta\downarrow0\), on obtient (18). Le nombre

\[
 324=18\times18                              \tag{37}
\]

est donc correct : le premier facteur \(18\) vient de
\((\lambda/6)(\lambda/(3\varepsilon))\), le second de la constante Lorentz
\(3\) multipliée par le rapport de niveau \(6\). La finitude de la famille
permet de choisir \(j_*\) atteignant \(\varepsilon\). La disjonction donne
\(K_{w,j_*}\le K_w\), puis (19).

### Cas \(K_w=0\)

Ce cas ne crée pas de division silencieuse. Si \(K_w=0\), alors \(W=0\)
presque partout. La disjonction impose \(W_j=0\). Par (1),
\(\nabla F_j=0\), et la compacité impose \(F_j=0\), donc \(U=0\) et
\(K_u=0\), contradiction avec (17). Ainsi \(K_u>0\) entraîne
automatiquement \(K_w>0\). De même, la cellule sélectionnée a
\(K_{w,j_*}>0\).

## Hypothèses silencieuses et passe adversariale

1. **Structure pure-swirl exacte.** Le seul raccord
   \(W=\operatorname{curl}U\) ne donne pas
   \(|W|\gtrsim|\nabla|U||\). Un champ de déformation sans rotation peut avoir
   un gradient non nul et un curl nul localement. La borne ponctuelle utilisée
   dans (30) vient de (1), pas d'une identité vectorielle générale.
2. **Distance uniforme à l'axe.** Les constantes \(2/3\) et \(2\) exigent
   \(R_j/2<r<3R_j/2\). Une cellule touchant l'axe ou un rapport annulaire
   dégénéré change toutes les inclusions.
3. **Compacité individuelle.** Elle assure des volumes finis, la coaire sans
   terme à l'infini et l'implication \(W_j=0\Rightarrow F_j=0\). Aucun majorant
   uniforme du diamètre axial n'est requis.
4. **Disjonction des supports complets.** Il faut la disjonction des supports
   tridimensionnels de \(F_j\), donc aussi de leurs dérivées à mesure nulle
   près. La seule disjonction des plateaux ne suffit pas ; des curls qui se
   recouvrent peuvent s'annuler avant \(|W|\).
5. **Volumes tridimensionnels.** \(V_{j,\sigma}\) et \(|H|\) incluent le
   poids \(2\pi r\). Employer l'aire \(dr\,dz\) rendrait (20), (29) et les
   exposants faux.
6. **Deux signes.** Le superniveau de \(|U|\) doit être couvert par les deux
   signes de \(F_j\). Aucun signe unique global n'est disponible.
7. **Niveaux stricts.** Les égalités de niveau n'affectent ni la quasi-norme
   ni coaire ; les périmètres sont utilisés seulement pour presque tout
   \(t\). Les termes \(V_{j,\sigma}=0\) sont omis dans (32).
8. **Famille finie.** Elle assure que \(\varepsilon\) est atteint. Une famille
   dénombrable donnerait d'abord une sélection à facteur \(1-\delta\), pas
   automatiquement un maximum.
9. **Pas de halo \(O(v_j)\) produit.** Le volume de \(H\) est contrôlé par
   \(\mu_U(\lambda/6)\), donc par \((K_u/\lambda)^3\), et non cellule par
   cellule par un volume fixé. Le théorème contourne le quantificateur faux de
   (10) au lieu de le démontrer.
10. **Pas de gate directionnel sans aspect axial.** La sélection (18)--(19)
    survit aux longues connexions, mais le gate BMO du cycle 0033 exige une
    boule de volume \(O(R_j^3)\), donc un diamètre axial borné. Le théorème
    présent ne compose pas seul vers l'exposant directionnel douze.

Aucun contre-exemple satisfaisant (16)--(17) et violant (18) n'a été trouvé :
les inclusions, coaire, isopérimétrie, Lorentz et la constante 324 forment une
chaîne fermée. Un tel contre-exemple devrait donc falsifier au moins une de
ces cinq étapes explicitement vérifiables.

## Échelle

Sous l'échelle Navier--Stokes

\[
 U_\mu(x)=\mu U(\mu x),
 \qquad
 W_\mu(x)=\mu^2W(\mu x),
 \qquad
 R_{j,\mu}=R_j/\mu,
\]

les quatre quasi-normes de (2) sont invariantes. Le niveau et les volumes se
transforment comme

\[
 \lambda_\mu=\mu\lambda,
 \qquad
 V_\mu=\mu^{-3}V,
 \qquad
 |H_\mu|=\mu^{-3}|H|.
\]

Les deux côtés de (30) se multiplient par \(\mu^{-1}\), comme ceux de (35),
et (18)--(19) sont critiques. Le contre-exemple (3) est précisément la
dilatation critique \(\mu=L^{-1}\) d'un profil fixe ; ses endpoints restent
constants tandis que le volume témoin artificiel \(v_L=1\) ne suit pas la
loi d'échelle naturelle \(v\mapsto\mu^{-3}v\). Cette rupture de calibration
est le défaut mis en évidence par (10).

## Verdict, statut et falsificateurs

- **Halo \(O(v_j)\) issu des hypothèses littérales C34 sans
  \(|Q_j|\lesssim v_j\) : `ABANDONNER`.** Le champ (3) est un contre-exemple
  lisse, divergence-free et curl-compatible.
- **Lemme de halo conditionnel (13)--(15) : `CONTINUER`.** Il est exact, mais
  ses deux propriétés de localisation sont des hypothèses supplémentaires.
- **Sélection par bandes dynamiques pure-swirl (18)--(19) : `CONTINUER`.**
  L'audit valide les inclusions, les sens, l'isopérimétrie tridimensionnelle,
  l'intégrale faible-Lorentz et la constante \(C_I/324\).
- **Extension à tout champ divergence-free avec seulement
  \(W=\operatorname{curl}U\) : `À REPRENDRE`.** La troncature scalaire et la
  borne ponctuelle (30) manquent.

Le falsificateur du résultat négatif est reproductible analytiquement : fixer
\(\Phi\), prendre \(L>M_0\Gamma/\gamma\), puis vérifier (5)--(8). Un
falsificateur du théorème renforcé serait une famille finie pure-swirl
satisfaisant (16)--(17) pour laquelle

\[
 \max_jK_{u,j}<\frac{C_I}{324}\frac{K_u^2}{K_w}.
\]

Il devrait nécessairement exhiber soit une violation d'une inclusion de
niveau, soit une erreur de périmètre tridimensionnel, soit un recouvrement des
supports de curl, soit une violation de l'inégalité faible-Lorentz.

La prochaine réduction est le verrou
`GAP-LONG-CELL-DIRECTIONAL-GATE` : déterminer si la cellule sélectionnée par
(18) admet une boule ou une famille de boules à volume contrôlé sur laquelle
le retour directionnel reste coercif, sans supposer un diamètre axial
\(O(R_j)\).
