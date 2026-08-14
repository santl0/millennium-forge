# Cycle 0016 — audit d’analyse fonctionnelle de (40)–(47)

Date de la passe : 2026-08-14.
Objet : Section 6 de Zoran Grujić, *Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier–Stokes Equations*, [arXiv:2607.08866v2](https://arxiv.org/abs/2607.08866v2), version 2 datée du 13 juillet 2026 dans l’enregistrement arXiv (le HTML porte aussi la date du 11 août 2026).
Portée : implication quantitative (40) → remarque sur \(\omega^*\) → O’Neil (41) → (42)–(46) → (47), et seulement cette implication.

> **Indépendance de la revue.** Cette passe est produite par un agent de la même famille de modèle que les passes principales de Millennium Forge. Elle est contradictoire dans sa méthode, mais **ne constitue pas une revue externe ni une réplication indépendante**.

## Verdict synthétique

Le mécanisme fonctionnel visé est valide après réparation : une queue de distribution

\[
\mu_\omega(\Lambda,t)
\lesssim
\Lambda^{-3/2}\bigl(\log \Lambda\bigr)^{-3/2}
\]

à grandes amplitudes, complétée par un contrôle global uniforme de \(\omega\) dans \(L^{3/2,\infty}\) et par une représentation globale admissible de Biot–Savart, entraîne bien

\[
u^*(v,t)\lesssim
\frac{v^{-1/3}}{\log(e/v)}
\qquad (v\downarrow0).
\]

Les exposants, les poids de (41), les signes des intégrations par parties et le scaling Navier–Stokes sont cohérents. Cependant, le texte publié sur arXiv ne fournit pas à cet endroit une implication quantitative dimensionnée complète. Trois corrections sont nécessaires :

1. les logarithmes et la coupure volumique doivent être normalisés par des références d’amplitude et de volume ;
2. (41) provient en premier lieu d’une borne sur la réarrangée maximale \((k*|\omega|)^{**}\), et requiert une représentation de Biot–Savart sans composante harmonique non contrôlée ;
3. dans (46), le reste positif n’est **pas** \(O(1)\) quand \(v\downarrow0\). Il vaut au premier ordre \(O(v^{-1/3}\log^{-2}(e/v))\) : il diverge, mais reste absorbable dans le terme principal avec une constante uniforme après fixation d’un seuil.

Le dernier point invalide l’égalité asymptotique additive affichée dans l’explication de (46), mais pas la majoration (47). Le lemme quantitatif ci-dessous répare la chaîne avec toutes les dépendances utiles.

## 1. Cadre exact et conventions

On travaille sur \(\mathbb R^3\), à un temps fixé \(t\), avec

\[
\nabla\cdot u=0,
\qquad
\boldsymbol\omega=\nabla\times u,
\qquad
\omega=|\boldsymbol\omega|.
\]

Pour une fonction mesurable scalaire \(f\), on note

\[
\mu_f(\lambda)=|\{x\in\mathbb R^3:|f(x)|>\lambda\}|,
\qquad
f^*(s)=\inf\{\lambda\ge0:\mu_f(\lambda)\le s\},
\]

et

\[
f^{**}(s)=\frac1s\int_0^s f^*(r)\,dr.
\]

La convention de Lorentz est

\[
\|f\|_{L^{p,\infty}}=\sup_{s>0}s^{1/p}f^*(s).
\]

Les valeurs sur les plateaux ne changent aucune estimation : utiliser un inverse généralisé droit ou gauche ne modifie que des inégalités non strictes sur un ensemble de niveaux négligeable.

### Références dimensionnelles

Fixons :

- une amplitude de vorticité \(\Omega_0>0\), de dimension \(T^{-1}\) ;
- un volume \(V_0>0\), de dimension \(L^3\) ;
- une constante sans dimension \(D_\omega>0\) ;
- un seuil d’amplitude \(\Lambda_0\ge\Omega_0\).

La formule (40) du papier, dans ses variables nondimensionnées et avec \(\gamma_1=3/2\), est

\[
\sup_t|\{x:\omega(x,t)>\lambda\}|
\le
\frac{C_\omega}{\lambda^{3/2}(\log\lambda)^{3/2}}
\qquad(\lambda\ \text{grand}).
\]

La présence de \(\log\lambda\) impose soit que les variables aient déjà été nondimensionnées, soit l’introduction explicite d’une amplitude de référence.

Posons

\[
W=D_\omega V_0,
\qquad
L_W(s)=1+\log\frac Ws=\log\frac{eW}{s}.
\]

Ainsi, chaque argument de logarithme est sans dimension. L’analogue dimensionné de (40) utilisé dans cette passe est

\[
\boxed{
\mu_\omega(\Lambda,t)
\le
W\left(\frac{\Omega_0}{\Lambda}\right)^{3/2}
\left(1+\log\frac{\Lambda}{\Omega_0}\right)^{-3/2}
}
\tag{H40}
\]

pour tout \(\Lambda\ge\Lambda_0\), uniformément en \(t\) dans l’intervalle considéré. C’est une normalisation exacte du régime asymptotique de (40), pas une affirmation que les constantes implicites du papier valent un.

Il faut en plus isoler l’hypothèse globale de queue

\[
\boxed{
M_\omega:=\sup_t\|\omega(\cdot,t)\|_{L^{3/2,\infty}}
<\infty .
}
\tag{HW}
\]

(H40) ne porte que sur les grandes amplitudes et ne suffit donc pas, à elle seule, à contrôler l’intégrale de (41) jusqu’à \(+\infty\).

## 2. Inversion quantitative de (40)

Définissons

\[
Q_0=max\left\{e^9,
\left(\frac{\Lambda_0}{3\Omega_0}\right)^3\right\},
\qquad
s_0=\frac W{Q_0},
\qquad
L_0=L_W(s_0)=1+\log Q_0\ge10.
\]

### Lemme d’inversion

Sous (H40), pour tout \(0<s\le s_0\), uniformément en \(t\),

\[
\boxed{
\omega^*(s,t)
\le
3\Omega_0
\frac{(W/s)^{2/3}}{1+\log(W/s)}
=:
B_\omega\frac{s^{-2/3}}{L_W(s)},
}
\tag{R40}
\]

où

\[
B_\omega=3\Omega_0W^{2/3}.
\]

### Preuve avec seuil suivi

Posons \(q=W/s\ge Q_0\) et

\[
\Lambda_s=3\Omega_0\frac{q^{2/3}}{1+\log q}.
\]

Pour \(q\ge e^9\),

\[
1+\log q\le q^{1/3}.
\]

Donc \(\Lambda_s\ge3\Omega_0q^{1/3}\ge\Lambda_0\), et (H40) est applicable. De plus,

\[
\log(1+\log q)\le\frac13\log q,
\]

d’où, avec \(y=\Lambda_s/\Omega_0\),

\[
1+\log y
=1+\log3+\frac23\log q-\log(1+\log q)
\ge\frac13(1+\log q).
\]

Par conséquent,

\[
\begin{aligned}
\mu_\omega(\Lambda_s,t)
&\le W y^{-3/2}(1+\log y)^{-3/2}\\
&\le W\,3^{-3/2}q^{-1}(1+\log q)^{3/2}
\left(\frac{1+\log q}{3}\right)^{-3/2}\\
&=Wq^{-1}=s.
\end{aligned}
\]

La définition de la réarrangée décroissante donne \(\omega^*(s,t)\le\Lambda_s\), ce qui prouve (R40).

### Ce que la remarque suivant (40) omet

La remarque du papier obtient le bon profil, mais :

- la constante et le seuil de petite mesure ne sont pas suivis ;
- \(\log(e/v)\) est dimensionnellement illicite avant normalisation ;
- l’uniformité temporelle du seuil doit venir de constantes uniformes dans (40) ;
- une borne de grande amplitude ne fournit pas automatiquement le contrôle global de queue (HW).

Ces omissions sont réparables et ne changent pas l’exposant logarithmique.

## 3. Biot–Savart et forme exacte de l’inégalité d’O’Neil

### Représentation admissible

Sur \(\mathbb R^3\), si \(u\) est divergence-free, \(\boldsymbol\omega=\nabla\times u\), et si la composante harmonique est exclue par une condition globale appropriée, alors

\[
u(x)=\frac1{4\pi}\int_{\mathbb R^3}
\frac{\boldsymbol\omega(y)\times(x-y)}{|x-y|^3}\,dy
\]

au sens approprié. Ainsi,

\[
|u(x)|\le (k*\omega)(x),
\qquad
k(x)=\frac1{4\pi}|x|^{-2}.
\tag{BS}
\]

En notant \(\varpi_3=|B_1|=4\pi/3\), un calcul direct de la fonction de distribution de \(k\) donne

\[
k^*(s)=\kappa_Bs^{-2/3},
\qquad
\kappa_B=\frac{\varpi_3^{2/3}}{4\pi}.
\tag{K}
\]

### Hypothèses réellement nécessaires

La seule identité \(\boldsymbol\omega=\nabla\times u\) ne suffit pas à (BS). Il faut au minimum :

1. \(\nabla\cdot u=0\) au sens des distributions ;
2. absence d’une composante à la fois sans divergence et sans rotation qui échapperait à la vorticité ;
3. une condition à l’infini ou une classe fonctionnelle dans laquelle l’inversion de \(-\Delta\) est fixée ;
4. existence de la convolution, éventuellement comme limite de troncatures, avec une majoration absolue utilisable par réarrangement.

Par exemple, une vitesse de Leray à énergie finie exclut la vitesse constante non nulle, et la représentation peut être fixée par le multiplicateur de Fourier

\[
\widehat u(\xi)=i\frac{\xi\times\widehat{\boldsymbol\omega}(\xi)}{|\xi|^2}
\quad(\xi\ne0),
\]

avec le mode nul traité par la classe globale. Le contre-test élémentaire est décisif : \(u\equiv c\ne0\) vérifie \(\nabla\cdot u=0\) et \(\nabla\times u=0\), alors que le membre droit de (BS) est nul. Une condition éliminant ce mode n’est donc pas facultative.

Sur \(\mathbb T^3\), le noyau périodique et la moyenne de \(u\) doivent être traités séparément. La dérivation présente concerne \(\mathbb R^3\) et ne se transfère pas littéralement au cas périodique ou à un domaine borné.

### O’Neil avec les bons poids

La forme classique du théorème de réarrangement de convolution d’O’Neil est

\[
(f*g)^{**}(v)
\le
v f^{**}(v)g^{**}(v)
+\int_v^\infty f^*(s)g^*(s)\,ds,
\tag{ON}
\]

pour des fonctions non négatives dans le régime où les membres sont définis. Source primaire : R. O’Neil, *Convolution operators and \(L(p,q)\) spaces*, Duke Math. J. 30 (1963), 129–142, [DOI 10.1215/S0012-7094-63-03015-1](https://doi.org/10.1215/S0012-7094-63-03015-1).

Comme

\[
k^{**}(v)=\frac1v\int_0^v\kappa_Bs^{-2/3}\,ds
=3\kappa_Bv^{-2/3},
\]

(BS), \(h^*\le h^{**}\) et (ON) donnent

\[
\boxed{
u^*(v,t)
\le
\kappa_B\left[
3v^{-2/3}\int_0^v\omega^*(s,t)\,ds
+\int_v^\infty s^{-2/3}\omega^*(s,t)\,ds
\right].
}
\tag{ON-BS}
\]

Ainsi, les deux poids de (41) sont corrects, à une constante universelle près. La formulation exacte passe néanmoins par \((k*\omega)^{**}\), et le facteur \(3\) du premier terme provient de \(k^{**}\). L’emploi de la valeur absolue détruit les annulations vectorielles, mais donne une majoration sûre.

## 4. Audit des intégrales (42)–(46)

Fixons \(0<v\le s_0\) et posons

\[
F_W(v)=\frac{v^{-1/3}}{L_W(v)}.
\]

### 4.1 Terme de cœur

Par (R40),

\[
v^{-2/3}\int_0^v\omega^*(s,t)\,ds
\le
B_\omega v^{-2/3}\int_0^v\frac{s^{-2/3}}{L_W(s)}\,ds.
\]

Puisque \(L_W(s)\ge L_W(v)\) pour \(s\le v\),

\[
\int_0^v\frac{s^{-2/3}}{L_W(s)}\,ds
\le
\frac1{L_W(v)}\int_0^v s^{-2/3}\,ds
=3\frac{v^{1/3}}{L_W(v)}.
\]

Donc

\[
\boxed{
v^{-2/3}\int_0^v\omega^*(s,t)\,ds
\le3B_\omega F_W(v).
}
\tag{C}
\]

L’intégration par parties de (43) a bien le signe négatif annoncé :

\[
\int_0^v\frac{s^{-2/3}}{L_W(s)}\,ds
=3\frac{v^{1/3}}{L_W(v)}
-3\int_0^v\frac{s^{-2/3}}{L_W(s)^2}\,ds.
\]

Le reste est fini et non négatif avant son signe moins. La majoration (C) est donc immédiate et ne requiert pas d’équivalent asymptotique.

### 4.2 Queue intermédiaire

Scindons la seconde intégrale de (ON-BS) à \(s_0\) :

\[
\int_v^\infty s^{-2/3}\omega^*(s,t)\,ds
=\int_v^{s_0}s^{-2/3}\omega^*(s,t)\,ds
+\int_{s_0}^\infty s^{-2/3}\omega^*(s,t)\,ds.
\]

Pour la première partie, (R40) donne

\[
I(v):=\int_v^{s_0}\frac{s^{-4/3}}{L_W(s)}\,ds.
\]

Avec \(G(s)=s^{-1/3}/L_W(s)\),

\[
G'(s)=s^{-4/3}
\left(-\frac1{3L_W(s)}+\frac1{L_W(s)^2}\right),
\]

et donc

\[
I(v)=3G(v)-3G(s_0)
+3\int_v^{s_0}\frac{s^{-4/3}}{L_W(s)^2}\,ds.
\tag{IP}
\]

Le signe positif du dernier terme dans (46) est correct. En revanche, ce reste n’est pas \(O(1)\) lorsque \(v\downarrow0\). Il est de taille

\[
O\!\left(\frac{v^{-1/3}}{L_W(v)^2}\right),
\]

donc divergent, quoique inférieur d’un facteur logarithmique au terme principal. L’écriture « terme principal \(+O(1)\) » dans le passage à (46) est fausse comme assertion additive uniforme.

Une réparation sans asymptotique consiste à utiliser \(L_W(s)\ge L_0>3\) sur \([v,s_0]\). À partir de (IP),

\[
I(v)
\le3G(v)+\frac3{L_0}I(v),
\]

d’où

\[
\boxed{
I(v)
\le C_TF_W(v),
\qquad
C_T=\frac3{1-3/L_0}
\le\frac{30}{7}.
}
\tag{T1}
\]

Par conséquent,

\[
\int_v^{s_0}s^{-2/3}\omega^*(s,t)\,ds
\le C_TB_\omega F_W(v).
\]

### 4.3 Queue lointaine

L’hypothèse globale (HW) implique

\[
\omega^*(s,t)\le M_\omega s^{-2/3}
\qquad(s>0),
\]

et donc

\[
\int_{s_0}^\infty s^{-2/3}\omega^*(s,t)\,ds
\le M_\omega\int_{s_0}^\infty s^{-4/3}\,ds
=3M_\omega s_0^{-1/3}.
\tag{T2a}
\]

La fonction \(F_W(v)\) croît lorsque \(v\) décroît dans le régime \(L_W(v)>3\). Ainsi,

\[
F_W(v)\ge F_W(s_0)=\frac{s_0^{-1/3}}{L_0},
\]

et (T2a) devient

\[
\boxed{
\int_{s_0}^\infty s^{-2/3}\omega^*(s,t)\,ds
\le3L_0M_\omega F_W(v).
}
\tag{T2}
\]

La coupure en \(s=1\) utilisée dans (44)–(45) doit être comprise après nondimensionnement. Dans une formulation physique, \(1\) n’est pas un volume ; \(s_0\) fournit la coupure dimensionnée et uniforme.

## 5. Lemme minimal exact reliant (40) à (47)

### Lemme 0016-A — transfert Lorentz–Zygmund vorticité-vitesse

Soient \(u(\cdot,t)\) et \(\boldsymbol\omega(\cdot,t)\) des champs sur \(\mathbb R^3\) tels que, uniformément en \(t\) :

1. \(\nabla\cdot u=0\), \(\boldsymbol\omega=\nabla\times u\), et la représentation (BS) est valide sans composante harmonique résiduelle ;
2. la distribution de \(\omega=|\boldsymbol\omega|\) vérifie (H40) pour \(\Lambda\ge\Lambda_0\) ;
3. \(\|\omega\|_{L^{3/2,\infty}}\le M_\omega\).

Avec les constantes \(Q_0,s_0,L_0,B_\omega,\kappa_B\) définies ci-dessus, on a, pour tout \(0<v\le s_0\),

\[
\boxed{
u^*(v,t)
\le C_u\frac{v^{-1/3}}{L_W(v)},
}
\tag{47q}
\]

où la constante explicite

\[
\boxed{
C_u=
\kappa_B\left[
\left(9+\frac3{1-3/L_0}\right)B_\omega
+3L_0M_\omega
\right]
}
\tag{Cu}
\]

est uniforme en \(t\).

### Démonstration

Insérons (C), (T1) et (T2) dans (ON-BS) :

\[
\begin{aligned}
u^*(v,t)
&\le\kappa_B\left[
3(3B_\omega F_W(v))
+C_TB_\omega F_W(v)
+3L_0M_\omega F_W(v)
\right]\\
&=C_uF_W(v).
\end{aligned}
\]

C’est exactement le contenu fonctionnel requis pour (47), avec références, seuil et constantes suivis.

### Minimalité des hypothèses pour cette route

- La seule queue logarithmique à petite mesure suffit aux termes \([0,v]\) et \([v,s_0]\), mais pas à \([s_0,\infty)\).
- Un contrôle global peut remplacer (HW) s’il rend explicitement finie et uniforme la quantité
  \(\int_{s_0}^\infty s^{-2/3}\omega^*(s,t)\,ds\). Le faible \(L^{3/2}\) est une condition simple, critique et directement compatible avec le papier, mais n’est pas logiquement unique.
- La représentation exacte de Biot–Savart peut être remplacée par la seule majoration (BS), à condition qu’elle soit démontrée dans la notion de solution considérée.
- Aucune dynamique Navier–Stokes n’intervient dans ce lemme une fois (H40), (HW) et (BS) supposées. Le verrou dynamique demeure entièrement en amont : établir ces hypothèses uniformément près d’un temps singulier potentiel.

## 6. Vérification du scaling Navier–Stokes

Sous la remise à l’échelle naturelle

\[
u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),
\qquad
\boldsymbol\omega_\lambda(x,t)
=\lambda^2\boldsymbol\omega(\lambda x,\lambda^2t),
\]

les distributions satisfont

\[
\mu_{\omega_\lambda}(\Lambda,t)
=\lambda^{-3}\mu_\omega(\Lambda/\lambda^2,\lambda^2t),
\]

et les réarrangées

\[
\omega_\lambda^*(s,t)=\lambda^2\omega^*(\lambda^3s,\lambda^2t),
\qquad
u_\lambda^*(s,t)=\lambda u^*(\lambda^3s,\lambda^2t).
\]

Les références se transforment comme

\[
\Omega_{0,\lambda}=\lambda^2\Omega_0,
\qquad
V_{0,\lambda}=\lambda^{-3}V_0,
\qquad
W_\lambda=\lambda^{-3}W,
\]

alors que \(D_\omega,Q_0,L_0\) restent invariants. En particulier,

\[
B_{\omega,\lambda}
=3\Omega_{0,\lambda}W_\lambda^{2/3}
=B_\omega,
\]

et

\[
\|\omega_\lambda\|_{L^{3/2,\infty}}
=\|\omega\|_{L^{3/2,\infty}}.
\]

La constante \(C_u\) est donc invariante, tandis que

\[
\frac{s^{-1/3}}{L_{W_\lambda}(s)}
=\lambda\frac{(\lambda^3s)^{-1/3}}{L_W(\lambda^3s)},
\]

ce qui reproduit exactement le scaling de \(u_\lambda^*\). La chaîne réparée ne perd ni puissance d’échelle ni constante dépendant de la troncature.

Vérification dimensionnelle : \(B_\omega\) et \(M_\omega\) ont la dimension \(L^2T^{-1}\), \(v^{-1/3}\) a la dimension \(L^{-1}\), et le membre droit de (47q) a donc la dimension \(LT^{-1}\) d’une vitesse.

## 7. Tests adverses reproductibles sur le lemme

### Test A — reste de (46)

Prenons l’enveloppe exacte

\[
\omega^*(s)=B_\omega\frac{s^{-2/3}}{L_W(s)}
\quad(0<s\le s_0).
\]

Le reste de (IP),

\[
R(v)=3\int_v^{s_0}\frac{s^{-4/3}}{L_W(s)^2}\,ds,
\]

est positif et

\[
R(v)\asymp\frac{v^{-1/3}}{L_W(v)^2}
\quad(v\downarrow0).
\]

Donc \(R(v)\to\infty\), ce qui réfute l’étiquette \(O(1)\), tandis que

\[
\frac{R(v)}{F_W(v)}=O\!\left(\frac1{L_W(v)}\right)\to0.
\]

Ce test confirme simultanément le défaut d’exposition et la validité de la borne principale réparée.

Une vérification numérique reproductible consiste à calculer, pour \(W=1\), \(s_0=e^{-9}\), et \(v=10^{-m}s_0\), les deux ratios

\[
R(v),
\qquad
\frac{R(v)L_W(v)}{v^{-1/3}}.
\]

Le premier doit croître sans borne et le second décroître approximativement comme \(1/L_W(v)\). Une quadrature en variable \(z=\log(W/s)\) évite la singularité numérique :

\[
R(v)=3W^{-1/3}
\int_{\log(W/s_0)}^{\log(W/v)}
\frac{e^{z/3}}{(1+z)^2}\,dz.
\]

### Test B — composante harmonique oubliée

Le champ \(u(x)\equiv c\ne0\) sur \(\mathbb R^3\) est divergence-free et possède \(\boldsymbol\omega=0\), mais ne vérifie pas (BS). Il réfute toute version du lemme où « \(\nabla\cdot u=0\) et \(\nabla\times u=\boldsymbol\omega\) » serait la seule hypothèse de raccord. La restriction d’énergie finie, de décroissance, ou une normalisation du mode nul est nécessaire.

### Test C — absence de contrôle global de queue

Une prescription de \(\omega^*(s)\) satisfaisant (R40) seulement sur \((0,s_0]\), mais telle que

\[
\int_{s_0}^\infty s^{-2/3}\omega^*(s)\,ds=\infty,
\]

laisse le membre droit d’O’Neil infini. Par exemple, sur un espace de mesure infinie, prolonger formellement l’enveloppe par \(\omega^*(s)=s^{-1/3}\) pour \(s>s_0\) produit une intégrande \(s^{-1}\). Ce contre-profil n’est pas dans \(L^{3/2,\infty}\), précisément l’hypothèse manquante. Il montre que (40), interprétée comme une seule asymptotique de hauts niveaux, ne peut justifier seule (47).

## 8. Trous et statut de chaque maillon

| Maillon | Statut après audit | Dépendance ou défaut exact |
|---|---|---|
| (40) → borne sur \(\omega^*\) | Réparable, démontré ci-dessus | Nécessite références dimensionnelles, constante et seuil uniformes. |
| Biot–Savart → convolution scalaire | Conditionnel | Domaine \(\mathbb R^3\), inversion fixée, absence de mode harmonique, convolution admissible. |
| O’Neil → (41) | Correct à constante suivie | Porte d’abord sur \((k*\omega)^{**}\) ; le facteur du noyau et le facteur \(3\) doivent être absorbés dans \(C\). |
| (42)–(43), cœur | Correct | Le signe du reste est négatif ; borne supérieure immédiate. |
| (44)–(45), queue lointaine | Correct sous (HW) | La coupure \(1\) doit être remplacée par un volume de référence ; uniformité de \(M_\omega\) requise. |
| (46), queue intermédiaire | Conclusion correcte, justification asymptotique fautive | Le reste positif est \(O(v^{-1/3}L_W(v)^{-2})\), pas \(O(1)\). Absorption quantitative via \(L_0>3\). |
| (47) | Démontré conditionnellement par le lemme 0016-A | Ne démontre rien sur la production dynamique de (40) ni sur l’étape ultérieure d’analyticité/sparseness. |

## 9. Écart résiduel avec le problème Clay

Même sous sa forme réparée, le lemme 0016-A est un transfert statique conditionnel de réarrangements. Il ne fournit pas :

- la preuve que toute solution lisse maximale du problème Clay satisfait (H40) ;
- la preuve que l’hypothèse géométrique amont du papier vaut pour des données Clay arbitraires ;
- la conservation uniforme de (HW) à l’approche d’un temps singulier pour une solution générale ;
- le raccord automatique entre (47q) et un critère de prolongement sans vérifier les constantes et quantificateurs de l’étape harmonique suivante ;
- une extension immédiate au tore, aux domaines bornés, ou aux solutions faibles après perte de la représentation ponctuelle.

Le gain logarithmique est critique et compatible avec l’échelle, mais reste une conclusion conditionnelle. Le verrou de plus forte valeur informationnelle est désormais en amont : auditer si la dérivation de (40) fournit effectivement des constantes uniformes dans le temps et un seuil \(\Lambda_0\) indépendant de la troncature/de l’itération de De Giorgi. En aval, il faut vérifier séparément que la constante \(C_u\) obtenue ici satisfait les seuils quantitatifs de l’argument d’analyticité et de mesure harmonique ; une simple amélioration asymptotique ne synchronise pas automatiquement ces constantes.

## Sources primaires utilisées

- Z. Grujić, *Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier–Stokes Equations*, arXiv:2607.08866v2, Section 6 et équations (40)–(47), [HTML primaire](https://arxiv.org/html/2607.08866v2), [notice arXiv](https://arxiv.org/abs/2607.08866v2).
- R. O’Neil, *Convolution operators and \(L(p,q)\) spaces*, Duke Mathematical Journal 30 (1963), 129–142, [DOI](https://doi.org/10.1215/S0012-7094-63-03015-1).

## Conclusion de la passe

**Résultat positif borné :** l’implication fonctionnelle (40) → (47) admet une formulation quantitative exacte et invariante d’échelle, donnée par le lemme 0016-A.

**Résultat négatif :** le reste de (46) n’est pas borné ; l’assertion additive \(+O(1)\) est réfutée. Ce défaut est local et réparé par l’estimation d’absorption (T1).

**Statut recommandé :** `CONTINUER`, sans promouvoir pour autant la conclusion principale de l’article. Auditer ensuite la production uniforme de (40), puis la synchronisation quantitative de (47q) avec le rayon d’analyticité.
