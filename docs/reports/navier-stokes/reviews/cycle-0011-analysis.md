# Revue d'analyse PDE — cycle 0011

## Verdict

Le facteur d'amplification linéaire entre la couche parabolique

\[
t_\varepsilon=\kappa\varepsilon^2,
\qquad
\tau_\varepsilon=\log t_\varepsilon
=\log\kappa+2\log\varepsilon,
\tag{1}
\]

et le temps terminal \(t=1\), \(\tau=0\), est exactement

\[
e^{a(0-\tau_\varepsilon)}
=(\kappa\varepsilon^2)^{-a}
\tag{2}
\]

pour un mode du générateur dynamique \(\mathcal L_U\) de valeur propre \(a>0\). Le signe est imposé par la convention de Hou–Wang–Yang (HWY) : leur valeur propre elliptique certifiée \(\widetilde\lambda<0\) vérifie

\[
a=-\widetilde\lambda>0.
\tag{3}
\]

Une coordonnée de couche \(O(1)\) ne produit donc pas légitimement une branche \(O(\varepsilon^{-2a})\) à \(\tau=0\) : elle quitte le régime perturbatif après un temps physique encore \(O(\varepsilon^2)\). Pour obtenir une coordonnée terminale \(O(1)\) tout en restant dans le régime linéaire, il faut une condition de tir ajustée à l'ordre

\[
b(\tau_\varepsilon)=O((\kappa\varepsilon^2)^a),
\tag{4}
\]

plus une compensation exacte des termes non linéaires, du cutoff extérieur et de la pression projetée.

Le résultat adverse principal est plus fort pour la régularisation radiale canonique du cycle 0010, appliquée à une localisation extérieure respectant les symétries HWY : le profil de base est pair dans la variable axiale et le mode instable certifié est impair. Une convolution radiale conserve cette symétrie ; la projection de la couche sur l'adjoint impair est alors **exactement nulle** tant que la solution forte unique existe. Le facteur (2) amplifie zéro en zéro. Créer une coordonnée non nulle exige de briser la symétrie dans la donnée lisse, ce qui produit des données Clay différentes, pas deux branches issues de la même donnée.

## 1. Cadre et faits sourcés

La source primaire est T. Hou, Y. Wang, C. Yang, [*Nonuniqueness of Leray–Hopf solutions to the unforced incompressible 3D Navier–Stokes Equation*, arXiv:2509.25116v2](https://arxiv.org/html/2509.25116v2), prépublication révisée le 19 mars 2026. La CAP revendiquée n'est pas reproduite ici.

Les éléments suivants sont sourcés dans les sections 1.2–1.4 et 2.2.

1. En variables
   \[
   \xi=x/\sqrt t,
   \qquad \tau=\log t,
   \qquad u(t,x)=t^{-1/2}V(\xi,\tau),
   \tag{5}
   \]
   le profil forward \(U\) est stationnaire.
2. Le générateur linéarisé dynamique est
   \[
   \mathcal L_U f
   =\frac12f+\frac12\xi\cdot\nabla f+\Delta f
   -\Pi(U\cdot\nabla f+f\cdot\nabla U).
   \tag{6}
   \]
3. L'équation elliptique certifiée par la CAP utilise \(-\mathcal L_U\). L'eigenpair exact satisfait
   \[
   -\mathcal L_U\widetilde v
   =\widetilde\lambda\widetilde v,
   \qquad \widetilde\lambda<0,
   \tag{7}
   \]
   d'où (3) et \(\mathcal L_U\widetilde v=a\widetilde v\).
4. L'approximation numérique \(\overline v\) est normalisée par \(\|\overline v\|_2=1\). L'eigenfonction exacte est \(\widetilde v=\overline v+v\), avec \(\langle v,\overline v\rangle=0\) et \(\|v\|_2\) petite. Ainsi \(\|\widetilde v\|_2^2=1+\|v\|_2^2\), et la source ne dit pas que \(\|\widetilde v\|_2=1\) exactement.
5. La décomposition spectrale de la section 2.2 est effectuée sur \(L^2_\sigma\) par projecteurs de Riesz. Les sous-espaces instables sont de dimension finie ; des blocs de Jordan sont autorisés dans l'énoncé général.
6. Les corrections non linéaires sont contrôlées dans la norme de similarité
   \[
   \|\Phi\|_X
   =\sup_{\tau<0}
   R^{(p-3)/(2p)}e^{-\delta\tau}
   \|\Phi(\tau)\|_{H^3_\xi},
   \tag{8}
   \]
   avec \(p=4\) et
   \[
   \delta=\frac12\min\left\{\frac{p-3}{2p},
   \min_j\Re\lambda_j\right\}>0.
   \tag{9}
   \]
7. Les coordonnées instables \(U_{j0}\) sont **prescrites à \(\tau=0\)**, puis intégrées vers le passé. Elles ne sont pas obtenues par l'évolution en avant d'une couche intérieure à temps fini.
8. Le profil de base construit est pair en \(z\), tandis que l'eigenmode certifié est impair en \(z\) et brise cette symétrie.

La suite de cette revue est une dérivation conditionnelle à partir de ces faits.

## 2. Transformation exacte de l'équation

Sur \(\mathbb R^3\), viscosité \(1\), force nulle, la forme projetée est

\[
\partial_tu-\Delta u+\Pi(u\cdot\nabla u)=0,
\qquad \nabla\cdot u=0.
\tag{10}
\]

La substitution (5) donne

\[
\partial_\tau V
=\frac12V+\frac12\xi\cdot\nabla V+\Delta V
-\Pi(V\cdot\nabla V).
\tag{11}
\]

Si \(V=U+\phi\) et si \(U\) résout l'équation stationnaire, alors

\[
\partial_\tau\phi
=\mathcal L_U\phi-\Pi(\phi\cdot\nabla\phi).
\tag{12}
\]

Ainsi un mode \(r\) tel que \(\mathcal L_Ur=ar\), \(a>0\), évolue dans l'équation homogène comme

\[
\phi(\tau)=e^{a(\tau-\tau_0)}c_0r.
\tag{13}
\]

Comme \(\tau\) augmente avec \(t\), ce mode décroît lorsque \(\tau\to-\infty\) et croît vers \(\tau=0\). Employer \(e^{-a(\tau-\tau_0)}\) ou identifier \(a\) à \(\widetilde\lambda<0\) inverserait le mécanisme.

## 3. La couche \(t=\kappa\varepsilon^2\)

### 3.1 Deux remises à l'échelle

Soit \(a_R\) la donnée HWY localisée extérieurement : elle est compacte, divergence-free et égale au champ homogène

\[
h(x)=|x|^{-1}A(x/|x|)
\tag{14}
\]

près de zéro. Sa régularisation intérieure est

\[
a_{R,\varepsilon}=\rho_\varepsilon*a_R.
\tag{15}
\]

Soit \(u_\varepsilon\) la solution forte maximale issue de (15). Introduisons le zoom de la couche intérieure

\[
W_\varepsilon(y,s)
=\varepsilon u_\varepsilon(\varepsilon y,\varepsilon^2s).
\tag{16}
\]

Il résout exactement la même équation de Navier–Stokes. À \(s=0\),

\[
W_\varepsilon(y,0)
=\int_{\mathbb R^3}\rho(y-z)\,\varepsilon a_R(\varepsilon z)\,dz.
\tag{17}
\]

Sur tout compact fixé en \(y\), le membre droit est, pour \(\varepsilon\) assez petit, exactement \((\rho*h)(y)\). Le cutoff extérieur est repoussé à distance \(R/\varepsilon\).

Le profil en variables HWY au temps de couche est

\[
V_\varepsilon(\xi,\tau_\varepsilon)
=\sqrt{t_\varepsilon}\,
u_\varepsilon(\sqrt{t_\varepsilon}\xi,t_\varepsilon)
=\sqrt\kappa\,
W_\varepsilon(\sqrt\kappa\xi,\kappa).
\tag{18}
\]

Pour \(\kappa\) fixé, (18) ne contient aucun petit facteur \(\varepsilon\). Si \(W_\varepsilon(\kappa)\) converge vers un flot limite \(W(\kappa)\) dans une topologie assez forte, le défaut de couche formel est

\[
D_\kappa(\xi)
=\sqrt\kappa W(\sqrt\kappa\xi,\kappa)-U(\xi).
\tag{19}
\]

Il est en général \(O_\kappa(1)\), pas \(O(\varepsilon^\gamma)\). La convergence nécessaire à (19), surtout globale dans \(L^2\) ou \(H^3\), n'est pas démontrée par la convergence locale de (17) : la pression et la queue extérieure restent non locales.

### 3.2 Le bon défaut global

Le profil \(U\sim|\xi|^{-1}A\) n'est pas dans \(L^2(\mathbb R^3)\). Par conséquent

\[
V_\varepsilon-U
\tag{20}
\]

n'est pas, en général, un objet admissible pour la projection spectrale \(L^2\). Il faut soustraire aussi le cutoff extérieur dynamique de HWY. Si

\[
u_R^{\mathrm{cut}}=-e^{t\Delta}w_R,
\qquad
U_R^{\mathrm{cut}}(\xi,\tau)
=\sqrt t\,u_R^{\mathrm{cut}}(\sqrt t\xi,t),
\tag{21}
\]

le défaut à projeter est

\[
\Phi_\varepsilon
=V_\varepsilon-U-U_R^{\mathrm{cut}}.
\tag{22}
\]

La construction HWY est précisément organisée pour que ce dernier objet soit dans les espaces énergétiques et \(H^3\) utilisés par le point fixe. Omettre \(U_R^{\mathrm{cut}}\) rend la projection globale potentiellement indéfinie.

## 4. Projection sur l'adjoint : normalisation correcte

### 4.1 Hypothèse spectrale minimale

Pour obtenir une coordonnée scalaire exacte, supposons que \(a>0\) soit une valeur propre réelle isolée et algébriquement simple de \(\mathcal L_U\). On choisit

\[
\mathcal L_Ur=ar,
\qquad
\mathcal L_U^*\ell=a\ell,
\qquad
\|r\|_2=1,
\qquad
\langle r,\ell\rangle_{L^2}=1.
\tag{23}
\]

Il est généralement impossible d'imposer en plus \(\|\ell\|_2=1\). Avec (23), le projecteur spectral de rang un est

\[
P_af=\langle f,\ell\rangle r,
\qquad
\|P_a\|_{L^2\to L^2}=\|\ell\|_2.
\tag{24}
\]

La norme \(\|\ell\|_2\) mesure le défaut de normalité de \(\mathcal L_U\). HWY normalise l'eigenmode droit approché dans \(L^2\), mais ne fournit pas dans les énoncés audités une eigenfonction adjointe certifiée, la normalisation (23), ni une valeur explicite de (24). La boundedness abstraite du projecteur de Riesz ne remplace pas ces constantes.

Sur le sous-espace divergence-free, un calcul formel donne

\[
\mathcal L_U^*\ell
=-\ell-\frac12\xi\cdot\nabla\ell+\Delta\ell
+\Pi\bigl(U\cdot\nabla\ell-(\nabla U)^T\ell\bigr).
\tag{25}
\]

La projection de Leray est auto-adjointe dans \(L^2\), mais elle reste non locale. La formule (25) exige les domaines opératoriels et décroissances nécessaires ; elle ne construit pas \(\ell\).

### 4.2 \(L^2\) contre \(H^3\)

La coordonnée spectrale est

\[
b_\varepsilon(\tau)
=\langle\Phi_\varepsilon(\tau),\ell\rangle_{L^2}.
\tag{26}
\]

Elle obéit à

\[
|b_\varepsilon(\tau)|
\leq\|\ell\|_2\|\Phi_\varepsilon(\tau)\|_2
\leq\|\ell\|_2\|\Phi_\varepsilon(\tau)\|_{H^3}.
\tag{27}
\]

Inversement, pour la composante pure \(b r\),

\[
\|P_a\Phi\|_{H^3}=|b|\,\|r\|_{H^3}.
\tag{28}
\]

La normalisation \(\|r\|_2=1\) ne normalise donc pas \(\|r\|_{H^3}\). Dans le schéma HWY, si le sous-espace est simple et si \(U_{a0}=Br\), la condition terminale

\[
R^{1/8}\|U_{a0}\|_{H^3}\leq\eta
\tag{29}
\]

devient

\[
|B|\leq\frac{\eta R^{-1/8}}{\|r\|_{H^3}}.
\tag{30}
\]

Ni \(\|r\|_{H^3}\), ni \(\|\ell\|_2\) ne doivent être absorbées dans un symbole « normalisé ».

Pour un défaut physique \(z(t,x)=t^{-1/2}\phi(x/\sqrt t,\log t)\),

\[
\|\nabla_x^m z(t)\|_{L^2_x}
=t^{1/4-m/2}
\|\nabla_\xi^m\phi(\tau)\|_{L^2_\xi}.
\tag{31}
\]

La norme \(H^3\) de (8) est donc une norme en \(\xi\), sans facteur d'échelle unique correspondant à la norme physique inhomogène \(H^3_x\).

## 5. Balance scalaire exacte et amplification

Après soustraction de \(U\) et du cutoff extérieur, l'équation HWY a la forme

\[
\partial_\tau\Phi_\varepsilon
=\mathcal L_U\Phi_\varepsilon+G_\varepsilon,
\tag{32}
\]

où, dans la notation de la source,

\[
G_\varepsilon
=\mathcal L_{\mathrm{far}}\Phi_\varepsilon
+F+N(\Phi_\varepsilon,\Phi_\varepsilon),
\qquad
N(f,g)=-\Pi(f\cdot\nabla g).
\tag{33}
\]

Sous les hypothèses de régularité permettant de dériver (26), on obtient

\[
b_\varepsilon'(\tau)
=a b_\varepsilon(\tau)+g_\varepsilon(\tau),
\qquad
g_\varepsilon(\tau)
=\langle G_\varepsilon(\tau),\ell\rangle.
\tag{34}
\]

La formule en avant entre \(\tau_\varepsilon\) et \(0\) est

\[
\boxed{
b_\varepsilon(0)
=(\kappa\varepsilon^2)^{-a}b_\varepsilon(\tau_\varepsilon)
+\int_{\tau_\varepsilon}^{0}e^{-as}
g_\varepsilon(s)\,ds.}
\tag{35}
\]

La formule équivalente, avec donnée terminale \(B=b_\varepsilon(0)\), est

\[
\boxed{
b_\varepsilon(\tau_\varepsilon)
=(\kappa\varepsilon^2)^aB
-\int_{\tau_\varepsilon}^{0}
e^{a(\tau_\varepsilon-s)}g_\varepsilon(s)\,ds.}
\tag{36}
\]

Le signe moins de (36) est exactement celui de l'intégration rétrograde des coordonnées instables dans l'équation (2.15) de HWY.

Dans le problème homogène \(g_\varepsilon=0\), si

\[
b_\varepsilon(\tau_\varepsilon)
=c_\varepsilon\varepsilon^\gamma,
\tag{37}
\]

alors

\[
b_\varepsilon(0)
=\kappa^{-a}c_\varepsilon
\varepsilon^{\gamma-2a}.
\tag{38}
\]

Le seuil exact est \(\gamma=2a\) :

- \(\gamma>2a\) : la coordonnée terminale tend vers zéro ;
- \(\gamma=2a\) : elle peut avoir une limite finie non nulle ;
- \(\gamma<2a\) : la prédiction linéaire diverge et quitte le voisinage où elle est justifiée.

Pour une coordonnée terminale \(B=O(1)\), la taille physique \(L^2\) de sa composante de couche est

\[
t_\varepsilon^{1/4}
|b_\varepsilon(\tau_\varepsilon)|
=O\bigl((\kappa\varepsilon^2)^{a+1/4}\bigr)
=O(\varepsilon^{2a+1/2}).
\tag{39}
\]

Elle est plus petite que l'erreur énergétique naturelle \(O(\varepsilon^{1/2})\) du cutoff intérieur. La convergence \(L^2\) ne résout donc absolument pas le signe ni la taille de cette coordonnée fine.

## 6. Sortie du régime perturbatif

Supposons pour simplifier \(g_\varepsilon=0\), et fixons un rayon perturbatif \(0<\eta\ll1\). Si

\[
|b_\varepsilon(\tau_\varepsilon)|\simeq c_\kappa>0
\tag{40}
\]

indépendamment de \(\varepsilon\), la coordonnée atteint \(\eta\) au temps

\[
\tau_{\mathrm{exit}}
=\tau_\varepsilon
+\frac1a\log\frac{\eta}{|c_\kappa|},
\qquad
t_{\mathrm{exit}}
=\kappa\varepsilon^2
\left(\frac{\eta}{|c_\kappa|}\right)^{1/a}.
\tag{41}
\]

Pour \(\kappa\) fixé, \(t_{\mathrm{exit}}=O(\varepsilon^2)\). L'expression formelle \(b(0)\simeq\varepsilon^{-2a}\) extrapole alors la linéarisation bien au-delà de son domaine. Elle ne prouve ni séparation à \(t=1\), ni blow-up, ni persistance d'une branche HWY.

Avec \(G_\varepsilon\neq0\), même la taille (4) n'est pas suffisante : c'est toute la condition de tir (36), qui dépend de l'évolution future inconnue, qui doit être satisfaite. Utiliser seulement la première composante de (36) puis estimer le reste après coup est circulaire si ce reste dépend de la solution qu'on cherche à contrôler.

## 7. Cutoff extérieur et pression

Pour \(p=4\), HWY pose

\[
\alpha=1-3/p=1/4.
\tag{42}
\]

Leur estimation (2.10) donne

\[
\|U_R^{\mathrm{cut}}(\tau)\|_{W^{k,4}}
\lesssim
R^{-\alpha}e^{\alpha\tau/2}.
\tag{43}
\]

À la couche,

\[
R^{-\alpha}e^{\alpha\tau_\varepsilon/2}
=R^{-1/4}\kappa^{1/8}\varepsilon^{1/4}.
\tag{44}
\]

Cette petitesse locale en \(\tau_\varepsilon\) ne permet pas de supprimer le terme extérieur dans (35), car il est intégré jusqu'à \(0\). Si une composante projetée satisfait abstraitement

\[
|g_{\mathrm{out}}(s)|
\leq C_\ell R^{-\alpha}e^{\beta s},
\qquad \beta=\alpha/2=1/8,
\tag{45}
\]

alors sa contribution est bornée par

\[
C_\ell R^{-\alpha}
\int_{\tau_\varepsilon}^{0}e^{(\beta-a)s}\,ds.
\tag{46}
\]

Cette intégrale reste bornée si \(\beta>a\), croît comme \(|\tau_\varepsilon|\) si \(\beta=a\), et comme \((\kappa\varepsilon^2)^{\beta-a}\) si \(\beta<a\). La simple phrase « le cutoff est loin » ne contrôle donc pas sa projection amplifiée. La valeur numérique candidate de \(a\) ne remplace pas une enclosure certifiée de \(a\), de \(C_\ell\) et du pairing.

La pression n'apparaît pas séparément dans (32) parce qu'elle est encodée dans \(\Pi\). Pour un adjoint divergence-free et des intégrations légitimes, \(\Pi\) est auto-adjointe et un gradient de pression ne contribue pas directement au pairing. Mais la pression détermine la dynamique globale et les queues de \(G_\varepsilon\) : la localité du défaut de vitesse ne permet pas de localiser (34). Les estimations (2.13) de HWY contrôlent \(\mathcal L_{\mathrm{far}}\), \(F\) et \(N\) dans \(H^2\) pour leur construction ; elles ne fournissent pas automatiquement les mêmes bornes pour le flot désingularisé \(u_\varepsilon\).

## 8. Contre-test de symétrie

Soit \(S\) l'involution unitaire représentant la réflexion axiale et les parités de composantes utilisées par HWY. La source construit

\[
SU=U,
\qquad Sr=-r.
\tag{47}
\]

Comme \(\mathcal L_U\) commute avec \(S\), son adjoint commute aussi avec \(S\). Dans le cas simple, l'adjoint peut être choisi dans la même classe impaire :

\[
S\ell=-\ell.
\tag{48}
\]

Une convolution radiale commute avec \(S\). Si la donnée homogène et sa localisation extérieure sont paires, alors la donnée Clay \(a_{R,\varepsilon}\) est paire. Par unicité de la solution forte locale et invariance de Navier–Stokes sous \(S\),

\[
SV_\varepsilon(\tau)=V_\varepsilon(\tau)
\tag{49}
\]

tant que cette solution forte existe. Le cutoff extérieur choisi symétriquement est également pair. Il en résulte

\[
b_\varepsilon(\tau)
=\langle\Phi_\varepsilon(\tau),\ell\rangle
=\langle S\Phi_\varepsilon,S\ell\rangle
=-b_\varepsilon(\tau),
\tag{50}
\]

donc

\[
\boxed{b_\varepsilon(\tau)=0}
\tag{51}
\]

sur tout l'intervalle fort. Le terme projeté \(g_\varepsilon\) est lui aussi nul par parité, ce qui est cohérent avec (34).

Ce contre-test élimine l'inférence « toute régularisation intérieure excite génériquement le mode instable certifié ». Une perturbation intérieure impaire peut produire une coordonnée non nulle, mais les signes ou amplitudes différents correspondent alors à des **données lisses différentes**. Elles peuvent converger vers la même donnée singulière et sélectionner des limites différentes sans donner deux solutions pour une même donnée Clay.

## 9. Lemme exact, conditionnel et falsifiable

### Lemme de couche parabolique projetée

Supposons :

1. \(u_\varepsilon\) existe sur \([t_\varepsilon,1]\) avec une régularité suffisante pour que le défaut (22) appartienne à \(C([\tau_\varepsilon,0];H^3_\sigma)\) ;
2. \(a>0\) est une valeur propre réelle, isolée et simple de \(\mathcal L_U\), avec le couple dual normalisé par (23) ;
3. le cutoff extérieur de (21) est le même que celui associé à \(a_R\) ;
4. \(G_\varepsilon\in L^1([\tau_\varepsilon,0];L^2_\sigma)\), avec toutes les contributions de Leray/pression incluses.

Alors les formules (35) et (36) sont exactes. Dans le cas homogène, le seuil de transmission d'une coordonnée finie non nulle à \(\tau=0\) est précisément \(b(\tau_\varepsilon)\asymp(\kappa\varepsilon^2)^a\). Pour une régularisation qui conserve la parité paire de HWY, cette coordonnée est identiquement nulle avant toute perte de la solution forte.

Ce lemme est une identité conditionnelle de dynamique projetée. Il ne démontre ni l'existence jusqu'à \(t=1\), ni la petitesse de \(\Phi_\varepsilon\), ni la convergence de la couche, ni la persistance non linéaire d'une branche.

### Test falsifiable minimal

Un test numérique ou assisté valable doit fournir, pour plusieurs \(\varepsilon\) et un \(\kappa\) fixé :

\[
\begin{aligned}
b_\varepsilon(\tau_\varepsilon)
&=\langle\Phi_\varepsilon(\tau_\varepsilon),\ell\rangle,\\
I_\varepsilon
&=\int_{\tau_\varepsilon}^{0}e^{-as}
\langle G_\varepsilon(s),\ell\rangle ds,\\
\mathcal R_\varepsilon
&=b_\varepsilon(0)
-(\kappa\varepsilon^2)^{-a}b_\varepsilon(\tau_\varepsilon)
-I_\varepsilon.
\end{aligned}
\tag{52}
\]

Il faut certifier \(\ell\), \(a\), les normes \(\|\ell\|_2\), \(\|r\|_{H^3}\), les queues du cutoff/pression, et une borne d'intervalle pour \(\mathcal R_\varepsilon\) contenant zéro. Pour la régularisation paire, le contrôle préalable est \(b_\varepsilon=I_\varepsilon=0\) à la précision certifiée par la symétrie ; un signal impair non nul mesure d'abord une erreur de discrétisation ou une rupture de symétrie.

## 10. Passe contradictoire et quantificateurs inversés

1. **Temps fixe contre temps de couche.** Pour \(\kappa\) fixé, \(t_\varepsilon\to0\) et \(\tau_\varepsilon\to-\infty\). Fixer \(t>0\) puis envoyer \(\varepsilon\to0\) n'est pas la même limite.
2. **Petitesse physique contre petitesse similaire.** Une erreur \(O(\varepsilon^{1/2})\) en \(L^2_x\) peut correspondre à une erreur \(O(1)\) en \(L^2_\xi\) au temps \(t\simeq\varepsilon^2\), d'après (31).
3. **Projection droite contre projection adjointe.** \(\langle\Phi,r\rangle\) n'est pas la coordonnée spectrale d'un opérateur non auto-adjoint. Il faut \(\ell\) et sa constante de conditionnement.
4. **Normalisation \(L^2\) contre \(H^3\).** La normalisation numérique de \(\overline v\) ne fixe ni la norme de l'eigenmode exact, ni \(\|r\|_{H^3}\), ni \(\|\ell\|_2\).
5. **Eigenpair contre simplicité.** Un eigenpair ne prouve pas l'absence de bloc de Jordan. Sans simplicité, il faut un système de coordonnées adjointes et des facteurs polynomiaux en \(|\tau_\varepsilon|\), que l'enveloppe avec \(\delta\) de HWY masque mais n'annule pas.
6. **Amplitude de couche contre amplitude terminale.** Le premier terme de (35) peut être annulé ou renforcé par l'intégrale. Une coordonnée initiale non nulle n'implique pas une séparation terminale.
7. **Régime linéaire contre extrapolation.** Une couche \(O(1)\) sort du voisinage perturbatif à \(t=O(\varepsilon^2)\) ; l'amplification jusqu'à \(t=1\) n'est alors plus justifiée.
8. **Parité.** La régularisation radiale naturelle n'excite pas le mode impair. Le mot « générique » ne peut pas remplacer ce calcul exact.
9. **Cutoff loin contre pression locale.** La queue extérieure recule dans les variables de couche, mais \(\Pi\) reste non locale et sa contribution amplifiée doit être intégrée comme dans (46).
10. **Existence jusqu'à \(\tau=0\).** Supposer \(\Phi_\varepsilon\in H^3\) jusqu'à \(t=1\) suppose déjà que la solution lisse désingularisée atteint ce temps. Si elle perd sa régularité avant, la formule \(H^3\) s'arrête ; si elle reste forte, l'unicité faible–forte interdit deux branches pour la même donnée.
11. **Choix terminal contre problème de Cauchy.** HWY choisit librement \(U_{j0}\) à \(\tau=0\) parce que la trace est imposée à \(\tau=-\infty\). Une donnée Clay lisse impose au contraire un état à temps fini ; ses coordonnées terminales ne sont pas libres.
12. **\(\kappa\) fixe contre \(\kappa(\varepsilon)\).** Faire croître \(\kappa\) pour espérer que \(D_\kappa\) devienne petit exige un théorème d'existence et de stabilité à grand temps pour le problème de couche. Il ne suit pas du calcul à \(\kappa\) fixé.

## Conclusion

**Résultat positif borné :** la balance projetée (35)–(36), son facteur exact \((\kappa\varepsilon^2)^{-a}\), son seuil \(\varepsilon^{2a}\) et les conversions \(L^2/H^3\) sont établis sous des hypothèses explicites.

**Résultat négatif :** la régularisation intérieure radiale conservant la symétrie HWY ne déclenche pas leur mode instable impair avant une éventuelle perte de régularité. Une couche non symétrique \(O(1)\) quitte le régime perturbatif à l'échelle \(\varepsilon^2\), tandis qu'une couche ajustée doit satisfaire la condition de tir non locale et non linéaire (36).

**État : RÉVISER.** La prochaine action utile n'est pas d'amplifier un pairing non certifié, mais de construire ou certifier l'eigenfonction adjointe, sa parité et la norme du projecteur, puis de mesurer le premier coefficient **impair** d'une famille de régularisations volontairement désymétrisées. Un tel test étudierait la sensibilité de sélection de la donnée singulière ; il ne constituerait pas encore une non-unicité pour une donnée Clay fixée.
