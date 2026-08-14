# Revue d'analyse PDE — cycle 0010

## Verdict

La donnée de Hou–Wang–Yang n'est pas rendue lisse par leur localisation : leur opérateur de Bogovskii coupe seulement la queue à grande distance et laisse inchangé le cœur homogène de degré \(-1\). Une désingularisation intérieure canonique existe néanmoins. Si \(a=u_{\mathrm{loc}}\) désigne leur donnée compacte et divergence-free, alors

\[
a_\varepsilon=\rho_\varepsilon*a,
\qquad
\rho_\varepsilon(x)=\varepsilon^{-3}\rho(x/\varepsilon),
\tag{1}
\]

avec \(\rho\in C_c^\infty\) radiale, \(\rho\geq0\), \(\int\rho=1\), est compacte, \(C^\infty\), divergence-free et donc admissible dans l'alternative Clay non forcée sur \(\mathbb R^3\).

Cette approximation est forte dans \(L^2\), mais pas dans une norme forte critique. Pour un profil angulaire non nul,

\[
\|a_\varepsilon-a\|_2=O(\varepsilon^{1/2}),
\quad
\|a_\varepsilon\|_3^3=C_3\log(1/\varepsilon)+O(1),
\quad
\|a_\varepsilon\|_{\dot H^{1/2}}^2=D_A\log(1/\varepsilon)+O(1),
\quad
\|a_\varepsilon\|_{H^1}=\Theta(\varepsilon^{-1/2}),
\tag{2}
\]

alors que \(\|a_\varepsilon\|_{L^{3,\infty}}\) reste uniformément bornée. Les méthodes locales sous-critiques ne garantissent uniformément qu'un temps de taille \(c\varepsilon^2\). Ce temps tend vers zéro, mais il s'agit d'une **borne inférieure**, pas de la preuve que le temps maximal tend vers zéro.

Le résultat négatif précis est le suivant : pour chaque \(\varepsilon>0\), l'unicité faible–forte interdit que la multiplicité de Hou–Wang–Yang survive tant que la solution forte issue de \(a_\varepsilon\) existe. Tout transfert de leur non-unicité vers une donnée Clay unique doit donc d'abord produire une perte de régularité de cette solution forte. Cette étape est déjà une résolution négative du problème Clay non forcé ; la désingularisation ne fournit aucun raccourci.

## 1. Ce qui est sourcé dans Hou–Wang–Yang v2

Source primaire : T. Hou, Y. Wang, C. Yang, [*Nonuniqueness of Leray–Hopf solutions to the unforced incompressible 3D Navier–Stokes Equation*, arXiv:2509.25116v2](https://arxiv.org/html/2509.25116v2), révision du 19 mars 2026. La preuve assistée par ordinateur revendiquée par les auteurs n'est pas reproduite dans cette revue.

Les faits suivants sont attribués à la source, et non dérivés ici.

- **Équation.** Navier–Stokes incompressible tridimensionnel sur \(\mathbb R^3\), viscosité \(1\), sans force ; équation (1.1).
- **Donnée homogène.** Le point de départ est
  \[
  h(x)=\frac1{|x|}A\!\left(\frac{x}{|x|}\right),
  \qquad \nabla\cdot h=0,
  \tag{3}
  \]
  avec singularité \(O(|x|^{-1})\) en zéro ; équations (1.4) et (1.8).
- **Profil forward.** La branche de fond a la forme
  \[
  \widetilde u(t,x)=t^{-1/2}\widetilde U(x/\sqrt t),
  \tag{4}
  \]
  et il ne faut pas la confondre avec un profil backward de blow-up issu d'une donnée lisse ; équations (1.5)–(1.7) et avertissement qui les accompagne.
- **Théorème annoncé.** Le théorème 1 revendique une infinité de solutions adaptées de Leray–Hopf sur \([0,1]\), avec la même donnée \(u_{\mathrm{loc}}\), compacte, divergence-free, lisse sur \(\mathbb R^3\setminus\{0\}\), appartenant à \(L^q\) pour tout \(q<3\), et des solutions lisses pour \(t>0\).
- **Localisation extérieure seulement.** Dans la section 2.2, les auteurs écrivent
  \[
  h=u_{\mathrm{loc}}+w,
  \qquad w=0\quad\text{sur }\{|x|<R\},
  \tag{5}
  \]
  où \(u_{\mathrm{loc}}\) est compacte et divergence-free. Par conséquent
  \[
  u_{\mathrm{loc}}(x)=h(x)\quad\text{pour }|x|<R.
  \tag{6}
  \]
  Le cutoff de Bogovskii supprime donc la queue \(|x|^{-1}\) à l'infini mais conserve exactement la singularité à l'origine. La correction dynamique correspondante est \(u^{\mathrm{cut}}=-e^{t\Delta}w\), équations (2.8)–(2.12).
- **Classe temporelle.** Les solutions construites vérifient \(L^s_tL^q_x\) lorsque \(3/q+2/s>1\), et manquent la condition de Prodi–Serrin \(3/q+2/s\leq1\) ; théorème 1 et section 1.1.
- **Unicité faible–forte.** La source rappelle qu'une solution globale forte impose l'unicité dans la classe faible, tandis que l'existence globale forte pour des données lisses générales demeure ouverte ; section 1.1.

La mollification utilisée dans l'analyse de régularité du **profil** à la section 2.1 n'est pas une mollification de la donnée initiale destinée à la rendre Clay. Confondre ces deux opérations serait un changement d'objet.

## 2. Désingularisation intérieure exacte

### 2.1 Construction

On fixe le rayon extérieur \(R\) de (5) et on note désormais

\[
a=u_{\mathrm{loc}}.
\]

Ainsi \(a\) est compacte, divergence-free au sens des distributions, lisse hors de zéro, dans \(L^2\), et égale à (3) dans \(B_R\). On choisit \(0<\varepsilon<R/8\) et on définit \(a_\varepsilon\) par (1).

Les propriétés suivantes sont immédiates :

\[
a_\varepsilon\in C_c^\infty(\mathbb R^3;\mathbb R^3),
\qquad
\nabla\cdot a_\varepsilon
=\rho_\varepsilon*(\nabla\cdot a)=0.
\tag{7}
\]

Le support est contenu dans \(\operatorname{supp}a+B_\varepsilon\). En particulier, \(a_\varepsilon\) et toutes ses dérivées décroissent plus vite que toute puissance. La donnée satisfait donc exactement les hypothèses spatiales Clay sur \(\mathbb R^3\), avec force nulle et viscosité \(1\).

Cette construction doit être appliquée **après** la localisation extérieure. Mollifier le champ homogène global \(h\) enlèverait la singularité au centre, mais laisserait la queue \(|x|^{-1}\) et ne produirait pas une donnée de Schwartz.

### 2.2 Pourquoi un cutoff scalaire intérieur ne suffit pas

La formule naïve \(\chi(|x|/\varepsilon)a(x)\) est lisse au centre mais

\[
\nabla\cdot(\chi a)=\nabla\chi\cdot a
\tag{8}
\]

sur la couche de raccord. Elle requiert une correction de Bogovskii ou la projection de Leray, toutes deux non locales et porteuses de constantes de couche. La convolution (1) évite ce défaut : elle commute exactement avec la divergence. Elle ne commute pas avec la dynamique non linéaire, mais ici elle agit seulement sur la donnée initiale.

## 3. Audit des normes de la donnée lisse

Cette section est une dérivation du laboratoire à partir de (3), (6) et (1). On suppose \(A\in C^\infty(S^2)\), \(A\not\equiv0\), et on pose

\[
C_p=\int_{S^2}|A(\theta)|^p\,d\theta>0.
\tag{9}
\]

Toutes les constantes ci-dessous peuvent dépendre de \(A\), \(R\), du cutoff extérieur fixé et de \(\rho\), mais pas de \(\varepsilon\).

### 3.1 Énergie \(L^2\)

Young donne

\[
\|a_\varepsilon\|_2\leq\|a\|_2,
\qquad
a_\varepsilon\longrightarrow a\quad\text{fortement dans }L^2.
\tag{10}
\]

Une séparation entre \(B_{O(\varepsilon)}\) et son complément, suivie de l'estimation \(|\nabla a(x)|\lesssim |x|^{-2}\) dans le cœur homogène, donne le taux

\[
\|a_\varepsilon-a\|_2\leq C\varepsilon^{1/2}.
\tag{11}
\]

La contribution de \(|x|\lesssim\varepsilon\) vaut déjà \(O(\varepsilon)\) au carré. Sur \(\varepsilon\lesssim|x|<R\), l'erreur de mollification est \(O(\varepsilon|x|^{-2})\), dont le carré intégré est encore \(O(\varepsilon)\). Ainsi l'énergie initiale converge vers une limite finie et non nulle : aucune constante énergétique ne diverge.

### 3.2 Normes \(L^p\)

Le calcul de coquille du cycle 0001 survit à la convolution, car celle-ci ne modifie le profil qu'à distance relative \(O(\varepsilon/r)\) pour \(r\gg\varepsilon\). Le cœur mollifié \(|x|=O(\varepsilon)\) ne contribue qu'un terme du même ordre que la première coquille. On obtient

\[
\|a_\varepsilon\|_3^3
=C_3\log(R/\varepsilon)+O(1),
\tag{12}
\]

et, pour chaque \(p>3\),

\[
c_p\varepsilon^{3-p}
\leq\|a_\varepsilon\|_p^p
\leq C'_p\varepsilon^{3-p},
\qquad
\|a_\varepsilon\|_p=\Theta(\varepsilon^{3/p-1}).
\tag{13}
\]

En particulier,

\[
\|a_\varepsilon\|_\infty=\Theta(\varepsilon^{-1}).
\tag{14}
\]

En revanche, \(a\in L^{3,\infty}\), et la convolution par un noyau \(L^1\) est bornée sur cet espace de Lorentz :

\[
\sup_{0<\varepsilon<R/8}
\|a_\varepsilon\|_{L^{3,\infty}}<\infty.
\tag{15}
\]

La distinction est essentielle : \(L^3\) est critique fort et diverge logarithmiquement ; \(L^{3,\infty}\) est critique faible et reste borné, mais ne fournit pas le critère endpoint \(L^\infty_tL^3_x\).

### 3.3 \(H^1\) et \(\dot H^{1/2}\)

Sur la région homogène,

\[
|\nabla a(r,\theta)|^2
=r^{-4}\bigl(|A(\theta)|^2+|\nabla_{S^2}A(\theta)|^2\bigr).
\tag{16}
\]

Les couches \(r\simeq\varepsilon\), ainsi que la coquille \(c\varepsilon<r<R/2\), donnent des bornes supérieure et inférieure du même ordre :

\[
c\varepsilon^{-1}
\leq\|\nabla a_\varepsilon\|_2^2
\leq C\varepsilon^{-1},
\qquad
\|a_\varepsilon\|_{H^1}=\Theta(\varepsilon^{-1/2}).
\tag{17}
\]

Le seuil Sobolev critique diverge plus lentement. La singularité localisée \(r^{-1}A(\theta)\) a, aux hautes fréquences, une transformée de Fourier principale homogène de degré \(-2\). Comme \(\widehat{a_\varepsilon}(\xi)=\widehat\rho(\varepsilon\xi)\widehat a(\xi)\), l'intégrale radiale de la norme \(\dot H^{1/2}\) est \(\int^{c/\varepsilon}d|\xi|/|\xi|\). Il existe donc une constante \(D_A>0\), dépendant de la convention de Fourier et du profil angulaire, telle que

\[
\|a_\varepsilon\|_{\dot H^{1/2}}^2
=D_A\log(1/\varepsilon)+O(1).
\tag{18}
\]

Le fait que \(D_A>0\) vient de l'injectivité de la transformation de Fourier sur le profil homogène non nul. Ainsi les deux normes fortes critiques suivies ici, \(L^3\) et \(\dot H^{1/2}\), perdent une constante logarithmique. La convergence \(L^2\) de (10) ne peut être promue ni en convergence \(L^3\), ni en convergence \(\dot H^{1/2}\).

### 3.4 Tableau d'échelle

| Quantité initiale | Comportement quand \(\varepsilon\downarrow0\) | Nature NS |
|---|---:|---|
| \(\|a_\varepsilon\|_2\) | converge vers \(\|a\|_2\) | énergie, supercritique |
| \(\|a_\varepsilon-a\|_2\) | \(O(\varepsilon^{1/2})\) | convergence forte seulement énergétique |
| \(\|a_\varepsilon\|_{L^{3,\infty}}\) | \(O(1)\) | critique faible |
| \(\|a_\varepsilon\|_3\) | \(\Theta(\log(1/\varepsilon)^{1/3})\) | critique fort |
| \(\|a_\varepsilon\|_{\dot H^{1/2}}\) | \(\Theta(\log(1/\varepsilon)^{1/2})\) | critique fort |
| \(\|a_\varepsilon\|_p\), \(p>3\) | \(\Theta(\varepsilon^{3/p-1})\) | sous-critique pour la théorie locale |
| \(\|a_\varepsilon\|_{H^1}\) | \(\Theta(\varepsilon^{-1/2})\) | norme forte sous-critique |
| \(\|a_\varepsilon\|_\infty\) | \(\Theta(\varepsilon^{-1})\) | amplitude du cœur |

Les logarithmes critiques comptent le nombre \(\simeq\log(R/\varepsilon)\) d'échelles actives. La borne faible \(L^{3,\infty}\) ne les additionne pas ; les normes fortes les additionnent.

## 4. Temps local : ce qui est uniforme et ce qui ne l'est pas

Soit \(u_\varepsilon\) la solution forte maximale de Navier–Stokes issue de \(a_\varepsilon\), définie sur \([0,T_\varepsilon^*)\).

### 4.1 Estimation \(H^1\)

Pour \(Y(t)=\|\nabla u_\varepsilon(t)\|_2^2\), l'estimation classique au niveau \(H^1\) donne

\[
Y'(t)+\|\Delta u_\varepsilon(t)\|_2^2
\leq C Y(t)^3.
\tag{19}
\]

L'inégalité différentielle assure une existence contrôlée au moins jusqu'à

\[
T_{\varepsilon,H^1}
\geq cY(0)^{-2}
=c\|\nabla a_\varepsilon\|_2^{-4}
\geq c'\varepsilon^2.
\tag{20}
\]

Le même exposant ressort de la théorie locale \(L^p\), \(p>3\) :

\[
T_{\varepsilon,p}
\gtrsim
\|a_\varepsilon\|_p^{-2p/(p-3)}
\simeq\varepsilon^2.
\tag{21}
\]

Le facteur de contraction sans dimension est

\[
T^{(1-3/p)/2}\|a_\varepsilon\|_p,
\tag{22}
\]

qui reste petit uniformément seulement lorsque \(T=O(\varepsilon^2)\).

Les équations (20) et (21) n'établissent jamais

\[
T_\varepsilon^*=O(\varepsilon^2)
\quad\text{ou}\quad
T_\varepsilon^*\to0.
\tag{23}
\]

Elles disent seulement que les preuves locales usuelles perdent leur temps uniforme. Transformer cette perte de preuve en borne supérieure sur \(T_\varepsilon^*\) serait un quantificateur inversé.

### 4.2 Constante de faible–forte unicité

Soit \(v_\varepsilon\) une solution de Leray–Hopf issue de la **même** donnée \(a_\varepsilon\), et \(w=v_\varepsilon-u_\varepsilon\). Pour \(q>3\) et

\[
s=\frac{2q}{q-3},
\qquad \frac2s+\frac3q=1,
\tag{24}
\]

l'inégalité d'énergie relative et Grönwall donnent, sur tout intervalle où la norme de Serrin de \(u_\varepsilon\) est finie,

\[
\|w(t)\|_2^2
\leq
\|w(0)\|_2^2
\exp\!\left(C_q\int_0^t\|u_\varepsilon(\tau)\|_q^s\,d\tau\right).
\tag{25}
\]

Comme \(w(0)=0\), on a

\[
v_\varepsilon=u_\varepsilon
\quad\text{sur }[0,T_\varepsilon^*).
\tag{26}
\]

Pour qu'une seconde solution de Leray–Hopf issue de \(a_\varepsilon\) se sépare de la première, il faut donc d'abord atteindre un temps où la solution forte maximale ne se prolonge plus. En particulier, si \(T_\varepsilon^*=\infty\), aucune non-unicité de Leray–Hopf n'est possible pour cette donnée.

### 4.3 Pourquoi la constante critique de la branche singulière est infinie

Pour le fond auto-similaire exact (4), si \(q>3\),

\[
\|\widetilde u(t)\|_q
=t^{-1/2+3/(2q)}\|\widetilde U\|_q
=t^{-1/s}\|\widetilde U\|_q.
\tag{27}
\]

Donc

\[
\int_0^{t_0}\|\widetilde u(t)\|_q^s\,dt
=\|\widetilde U\|_q^s\int_0^{t_0}\frac{dt}{t}
=\infty.
\tag{28}
\]

De même,

\[
\|\nabla\widetilde u(t)\|_2
=t^{-1/4}\|\nabla\widetilde U\|_2,
\qquad
\int_0^{t_0}\|\nabla\widetilde u(t)\|_2^4dt=\infty.
\tag{29}
\]

Ces logarithmes sont exactement la porte par laquelle la construction singulière échappe à l'unicité faible–forte.

Supposons, comme hypothèse de stabilité à tester et non comme fait sourcé, qu'une solution désingularisée reste relativement proche du fond dans \(L^q\) sur une fenêtre auto-similaire : pour certains \(c,t_0>0\) et \(0<\theta<1\),

\[
\|u_\varepsilon(t)-\widetilde u(t)\|_q
\leq\theta\|\widetilde u(t)\|_q,
\qquad c\varepsilon^2\leq t\leq t_0.
\tag{30}
\]

Alors

\[
\int_{c\varepsilon^2}^{t_0}\|u_\varepsilon(t)\|_q^sdt
\geq
(1-\theta)^s\|\widetilde U\|_q^s
\log\!\frac{t_0}{c\varepsilon^2}.
\tag{31}
\]

Ainsi toute constante de stabilité obtenue par le Grönwall de Serrin croît au moins comme une puissance négative de \(\varepsilon\). Une stabilité uniforme jusqu'à un temps physique fixé ne peut pas être obtenue par ce mécanisme si la fenêtre (30) existe.

## 5. Lemme minimal falsifiable

### Lemme — porte de désingularisation HWY

Soit \(a\) une donnée compacte, divergence-free, lisse hors de zéro, égale à \(|x|^{-1}A(x/|x|)\) dans une boule, avec \(A\in C^\infty(S^2)\setminus\{0\}\). Pour la famille (1) :

1. \(a_\varepsilon\) est une donnée Clay non forcée sur \(\mathbb R^3\) et \(a_\varepsilon\to a\) dans \(L^2\) au taux \(O(\varepsilon^{1/2})\) ;
2. les asymptotiques (12), (13), (17) et (18) valent, tandis que (15) reste uniforme ;
3. les estimations locales standard ne donnent uniformément qu'une échelle parabolique \(c\varepsilon^2\) ;
4. toute solution de Leray–Hopf issue de \(a_\varepsilon\) coïncide avec la solution forte maximale avant \(T_\varepsilon^*\) ;
5. si (30) est vraie sur une fenêtre allant de \(c\varepsilon^2\) à \(t_0\), le coefficient critique de faible–forte stabilité diverge au moins logarithmiquement selon (31).

Les points 1–5 constituent une dérivation, pas un résultat revendiqué par Hou–Wang–Yang et pas une preuve au statut `PAPER_PROOF`.

### Critère de falsification

Le lemme serait réfuté par l'un des faits reproductibles suivants :

- une mollification divergence-free de (6) dont les normes fortes \(L^3\) ou \(\dot H^{1/2}\) restent uniformes ;
- un temps local sous-critique uniforme dépendant seulement des quantités de (10) et (15), sans petiteur ni hypothèse supplémentaire ;
- deux solutions de Leray–Hopf distinctes issues du même \(a_\varepsilon\) alors que l'une conserve une norme de Serrin finie jusqu'au temps de séparation ;
- une estimation de stabilité de la fenêtre (30) dont la constante reste uniforme malgré le minorant (31).

## 6. Résultat négatif de raccord à Clay

Considérons une tentative de transférer les deux branches HWY à la **même** donnée lisse \(a_\varepsilon\). Deux cas seulement sont compatibles avec (27).

1. **La solution forte est globale.** Toutes les solutions de Leray–Hopf issues de \(a_\varepsilon\) coïncident avec elle ; la multiplicité est détruite.
2. **La solution forte perd sa régularité à \(T_\varepsilon^*<\infty\).** Une multiplicité faible peut éventuellement apparaître ensuite, mais l'existence de ce temps maximal fini est déjà un blow-up admissible pour une donnée Clay lisse non forcée.

Par conséquent, aucune continuité en \(L^2\) depuis la donnée singulière, aucun passage faible de solutions et aucune persistance spectrale du profil auto-similaire ne suffisent seuls. Il faut démontrer la perte de la branche forte ou renoncer à avoir deux solutions pour la même donnée lisse.

Deux suites de données lisses différentes convergeant vers \(a\) peuvent éventuellement sélectionner deux limites faibles HWY différentes. Cela montrerait une non-unicité de la limite singulière ou une non-continuité de sélection, pas la non-unicité pour une donnée Clay fixée.

## 7. Passe contradictoire

- **Cutoff intérieur/extérieur.** La source coupe à l'infini ; la convolution (1) coupe l'échelle intérieure. Les deux opérations ne sont pas confondues.
- **Divergence.** La convolution préserve exactement \(\nabla\cdot a=0\). Un cutoff scalaire isolé ne le ferait pas.
- **Énergie.** La convergence \(L^2\) est forte et quantitative ; elle ne contrôle aucune des normes critiques fortes qui divergent dans (2).
- **Temps local.** \(T_\varepsilon\gtrsim\varepsilon^2\) n'est pas retourné en \(T_\varepsilon\lesssim\varepsilon^2\). Aucune singularité n'est inférée de grandes normes initiales.
- **Faible–forte.** La comparaison porte sur deux solutions de la même équation, même viscosité, même force nulle et même donnée \(a_\varepsilon\). Elle n'est pas appliquée directement à la donnée singulière \(a\).
- **Norme critique.** La borne \(L^{3,\infty}\) n'est pas remplacée illicitement par une borne \(L^3\), \(\dot H^{1/2}\) ou Prodi–Serrin.
- **Stabilité dynamique.** La fenêtre (30) est explicitement une hypothèse falsifiable. Elle n'est ni démontrée par la convergence initiale \(L^2\), ni attribuée à la source.
- **Portée Clay.** Une famille de données Clay dont les constantes divergent n'est pas un contre-exemple. Un membre fixé de la famille devrait réellement perdre sa solution classique maximale.
- **Statut de la source.** La prépublication v2 et sa CAP sont décrites comme une revendication primaire non reproduite, pas comme un théorème publié indépendamment vérifié.

## État et prochaine action

**État : CONTINUER sur le lemme de stabilité ; ABANDONNER le transfert direct par simple mollification et compacité \(L^2\).**

La prochaine expérience décisive est de comparer, pour des temps \(t=\kappa\varepsilon^2\) puis \(t\gg\varepsilon^2\), le flot mild issu de \(a_\varepsilon\) et le fond HWY dans une norme compatible avec leur projection spectrale instable. Elle doit mesurer séparément :

\[
\|u_\varepsilon(t)-\widetilde u(t)\|_q,
\quad
\int_{c\varepsilon^2}^{t}\|u_\varepsilon(\tau)\|_q^s d\tau,
\quad
\text{projection sur le mode instable},
\tag{32}
\]

avec résidu PDE et erreur de troncature certifiés. Si la constante nécessaire croît comme le logarithme ou la puissance prédite sans produire de perte forte, la piste de persistance sous désingularisation doit être classée comme obstruction confirmée, non comme raccord Clay.
