# Cycle 0020 — audit primaire de la direction de vorticité et des espaces log-BMO

**Date de veille différentielle :** 2026-08-14  
**Famille de modèle :** revue bibliographique et contradictoire par le même modèle ; elle n'est pas une revue indépendante inter-familles.  
**Périmètre :** définition de \(\xi=\boldsymbol\omega/|\boldsymbol\omega|\) aux zéros, portée exacte des hypothèses \(bmo_\phi\) et \(\widetilde{bmo}_\phi\), ancres, semi-normes et résultats de multiplicateurs.

## Verdict

La condition de la v2 de Grujić est **locale en échelle mais globale en espace** : elle prend le supremum sur tous les centres de \(\mathbb R^3\), à toutes les échelles \(0<r<1/2\), et elle est supposée uniformément en temps sur le dernier intervalle avant \(T^*\). Elle ne porte ni seulement sur \(\{\omega>0\}\), ni seulement sur un cœur de forte vorticité, ni sur une direction coupée spatialement.

L'espace affiché dans la v2 n'est pas celui de Bradshaw–Grujić (2015) :

\[
\|f\|_{bmo_\phi}^{(2026)}
=\|f\|_{L^\infty(\mathbb R^3)}
+\sup_{x\in\mathbb R^3,\,0<r<1/2}
\frac{\operatorname{MO}(f,B_r(x))}{\phi(r)},
\]

alors que Bradshaw–Grujić utilisent

\[
\|f\|_{\widetilde{bmo}_\phi}^{(2015)}
=\|f\|_{L^1(\mathbb R^3)}
+\sup_{x\in\mathbb R^3,\,0<r<1/2}
\frac{\operatorname{MO}(f,I(x,r))}{\phi(r)}.
\]

En 2015, l'hypothèse est appliquée à \(\psi\xi\), où \(\psi\) est une coupure compacte égale à un sur un cœur fixé. L'ancre \(L^1\) est alors finie grâce à la coupure. En 2026, l'hypothèse est appliquée directement à \(\xi\) sur tout \(\mathbb R^3\), et l'ancre est \(L^\infty\).

Le défaut le plus en amont est indépendant de cette différence : **aucun des deux textes ne prescrit la valeur de \(\xi\) sur \(\{\boldsymbol\omega=0\}\)**. Or les moyennes BMO voient toute partie de mesure positive de cet ensemble. La condition n'est donc pas intrinsèque à la solution tant qu'un prolongement mesurable, sa convention et son uniformité temporelle ne sont pas inclus dans l'énoncé.

## 1. Veille différentielle et statuts

- Zoran Grujić, *Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier–Stokes Equations*, [arXiv:2607.08866](https://arxiv.org/abs/2607.08866), texte [v2](https://arxiv.org/html/2607.08866v2). La notice primaire indique toujours : soumission le 9 juillet 2026, dernière révision v2 le 13 juillet 2026, commentaire « some typos fixed, some sentences rewritten for clarity ». Au 2026-08-14, la notice ne donne ni v3, ni référence de revue, ni erratum. La date interne ultérieure du manuscrit ne constitue pas une version arXiv.
- Zachary Bradshaw et Zoran Grujić, *A spatially localized \(L\log L\) estimate on the vorticity in the 3D NSE*, [arXiv:1309.2519](https://arxiv.org/abs/1309.2519), texte final [v5](https://arxiv.org/html/1309.2519v5), publié dans *Indiana University Mathematics Journal* **64**(2) (2015), 433–440, [DOI 10.1512/iumj.2015.64.5496](https://doi.org/10.1512/iumj.2015.64.5496). La notice arXiv reste à la v5 du 7 février 2014.
- David Goldberg, *A local version of real Hardy spaces*, *Duke Mathematical Journal* **46**(1) (1979), 27–42, [DOI 10.1215/S0012-7094-79-04603-9](https://doi.org/10.1215/S0012-7094-79-04603-9), [notice primaire Project Euclid](https://projecteuclid.org/journals/duke-mathematical-journal/volume-46/issue-1/A-local-version-of-real-Hardy-spaces/10.1215/S0012-7094-79-04603-9.full).
- Svante Janson, *On functions with conditions on the mean oscillation*, *Arkiv för Matematik* **14** (1976), 189–196, [DOI 10.1007/BF02385834](https://doi.org/10.1007/BF02385834), [texte primaire](https://archive.ymsc.tsinghua.edu.cn/pacm_download/116/7249-11512_2006_Article_BF02385834.pdf).
- Eiichi Nakai et Kôzô Yabuta, *Pointwise multipliers for functions of bounded mean oscillation*, *Journal of the Mathematical Society of Japan* **37**(2) (1985), 207–218, [DOI 10.2969/jmsj/03720207](https://doi.org/10.2969/jmsj/03720207), [PDF primaire de la société](https://www.jstage.jst.go.jp/article/jmath1948/37/2/37_2_207/_pdf/-char/en).

La recherche différentielle n'a trouvé aucune nouvelle version primaire des deux prépublications pertinentes ni correction publiée attachée à leurs notices. Cette observation ne vaut pas certification d'absence de critiques externes.

## 2. Équations et notions de solution réellement concernées

### Grujić 2026

Le manuscrit traite les équations de Navier–Stokes incompressibles, visqueuses, non forcées sur \(\mathbb R^3\), avec viscosité \(\nu>0\). Son théorème 7.4 part d'une solution unique spatialement analytique sur \((0,T^*)\), issue d'une donnée de vitesse \(u_0\in L^\infty(\mathbb R^3)\), et suppose près du premier temps singulier possible :

\[
\omega=|\boldsymbol\omega|
\in L^\infty_tL^{3/2,\infty}_x,
\qquad
\xi\in L^\infty_t bmo_{1/|\log r|}(\mathbb R^3).
\]

Il ne s'agit pas d'une hypothèse générale sur toute solution de Leray–Hopf : elle est ajoutée à un scénario de « critical point singularity » et à la solution analytique maximale considérée par le manuscrit.

### Bradshaw–Grujić 2015

Le texte fixe

\[
\partial_tu+(u\cdot\nabla)u=-\nabla p+\Delta u,
\qquad \nabla\cdot u=0,
\]

sur \(\mathbb R^3\), sans force, avec viscosité normalisée à un. Le théorème 1 concerne une solution de Leray faible au sens distributionnel, avec \(\omega_0\in L^1\cap L^2\), et un premier temps de blow-up possible \(T\). Pour l'exposition, la solution est lisse sur \((0,T)\) ; le texte mentionne les mollificateurs retardés comme alternative. La conclusion est une borne **localisée** \(L\log L\) de la vorticité, pas directement la régularité globale :

\[
\sup_{t\in(0,T)}\int_{\mathbb R^3}\psi(x)
\sqrt{1+|\boldsymbol\omega|^2}
\log\sqrt{1+|\boldsymbol\omega|^2}\,dx<\infty.
\]

## 3. Portée exacte des deux hypothèses géométriques

| Question | Grujić 2026, équation (2), th. 4.1 et 7.4 | Bradshaw–Grujić 2015, th. 1 |
|---|---|---|
| Domaine du champ normé | \(\xi\) sur tout \(\mathbb R^3\) | \(\psi\xi\) sur tout \(\mathbb R^3\), avec support compact |
| Localité | locale seulement en **échelle**, \(r<1/2\) | locale en échelle et localisée physiquement par \(\psi\) |
| Centres des moyennes | tous \(x\in\mathbb R^3\) | tous \(x\in\mathbb R^3\), après multiplication par \(\psi\) |
| Ensemble actif | aucune restriction à \(\{\omega>0\}\) ou à \(A_\lambda\) | aucune restriction à \(\{\omega>0\}\) ; \(\psi=1\) sur le cœur fixé et varie sur une couronne |
| Géométrie des moyennes | boules \(B_r(x)\) | cubes \(I(x,r)\) |
| Ancre | \(L^\infty\) | \(L^1\) |
| Partie oscillation | semi-norme pondérée | semi-norme pondérée |
| Temps | \(L^\infty((T^*-\epsilon,T^*);\,bmo_\phi)\), donc borne essentielle uniforme | supremum explicite sur \((0,T)\) |
| Poids | \(\phi(r)=1/|\log r|\) | même poids |
| Conclusion | exclusion conditionnelle du temps singulier revendiquée | borne localisée \(L\log L\) |

La v2 appelle son espace « local » parce que seules les petites boules interviennent. Cette terminologie ne doit pas être lue comme une restriction spatiale au cœur \(B_R\) utilisé plus tard dans la preuve. Le théorème suppose le supremum sur tous les centres avant de restreindre les estimations à \(B_R\).

L'énoncé de 2015 est physiquement localisé, mais pas par une norme prise uniquement sur \(B(0,R_0)\) : la fonction globale \(\psi\xi\) est testée sur tous les cubes, y compris ceux qui rencontrent la couronne de transition de \(\psi\).

## 4. Valeur de \(\xi\) sur les zéros de vorticité

La v2 écrit explicitement

\[
\xi(x)=\frac{\boldsymbol\omega(x)}{|\boldsymbol\omega(x)|}
\]

dans son introduction, puis utilise \(\boldsymbol\omega=\omega\xi\), \(\alpha=\xi\cdot S\xi\) et les moyennes de \(\xi\). Le texte consulté ne donne aucune convention sur \(\{\omega=0\}\). Il affirme en outre que la direction est unitaire et que son terme \(L^\infty\) vaut trivialement un. Bradshaw–Grujić définissent de même \(\xi=\boldsymbol\omega/|\boldsymbol\omega|\) sans convention aux zéros.

Trois niveaux doivent être distingués :

1. L'identité \(\boldsymbol\omega=\omega\xi\) est insensible à la valeur de \(\xi\) là où \(\omega=0\).
2. Les produits de stretching qui contiennent un facteur \(\omega\) peuvent souvent être redéfinis arbitrairement sur cet ensemble sans modifier leur classe presque partout.
3. La semi-norme BMO de \(\xi\), elle, dépend du prolongement dès que l'ensemble nul de vorticité a une partie de mesure positive. La condition géométrique n'est donc pas déterminée par \(\boldsymbol\omega\) seul.

Définir \(\xi=0\) sur les zéros donnerait un représentant canonique mesurable et \(|\xi|\leq1\), mais contredirait littéralement l'affirmation « champ unitaire » sur cet ensemble. Autoriser une extension unitaire arbitraire conserve \(|\xi|=1\), mais rend l'appartenance à \(bmo_\phi\) dépendante du choix. Une formulation correcte doit choisir l'une des options suivantes et la suivre dans les constantes :

- convention canonique \(\xi=0\) sur \(\{\omega=0\}\) ;
- existence explicitement quantifiée d'un prolongement mesurable \(|\xi|\leq1\) avec borne uniforme ;
- hypothèse intrinsèque sur une région de forte vorticité, accompagnée d'un théorème d'extension global à constante uniforme.

La troisième option est le raccord mathématique réellement utile au problème Clay, mais elle n'est fournie par aucun des deux textes audités.

## 5. Test adverse exact et reproductible

Considérons la solution stationnaire nulle sur \(\mathbb R^3\) :

\[
u\equiv0,\qquad p\equiv0,\qquad
\boldsymbol\omega\equiv0.
\]

Ses résidus sont exactement

\[
\partial_tu+(u\cdot\nabla)u+\nabla p-\nu\Delta u=0,
\quad \nabla\cdot u=0,
\quad \boldsymbol\omega-\nabla\times u=0,
\]

et son énergie, son enstrophie et leur défaut sont nuls. Aucun calcul flottant n'intervient.

Deux prolongements unitaires de la direction, tous deux compatibles avec \(\boldsymbol\omega=\omega\xi=0\), sont :

\[
\xi_{\rm bon}(x)=e_1,
\qquad
\xi_{\rm mauvais}(x)=
\begin{cases}
e_1,&x_1\ge0,\\
-e_1,&x_1<0.
\end{cases}
\]

Pour \(\xi_{\rm bon}\), toute oscillation moyenne est nulle et

\[
\|\xi_{\rm bon}\|_{bmo_\phi}^{(2026)}=1.
\]

Pour toute boule \(B_r(0)\), la symétrie donne \((\xi_{\rm mauvais})_{B_r}=0\) et

\[
\operatorname{MO}(\xi_{\rm mauvais},B_r(0))=1.
\]

Ainsi, avec \(\phi(r)=1/|\log r|\),

\[
\sup_{0<r<1/2}
\frac{\operatorname{MO}(\xi_{\rm mauvais},B_r(0))}{\phi(r)}
=\sup_{0<r<1/2}|\log r|=\infty.
\]

Le même test atteint la formulation de 2015. Si \(\psi=1\) près de l'origine, \(\psi\xi_{\rm mauvais}\) garde le saut sur tous les petits cubes centrés à l'origine et échoue à appartenir à \(\widetilde{bmo}_\phi\). En revanche, \(\psi\xi_{\rm bon}=\psi e_1\) est intégrable et, pour une coupure Lipschitz,

\[
\operatorname{MO}(\psi e_1,I(x,r))
\le C\|\nabla\psi\|_\infty r,
\qquad
\frac{r}{\phi(r)}=r|\log r|=O(1),
\]

donc \(\psi\xi_{\rm bon}\in\widetilde{bmo}_\phi\).

**Résidu certifié du test :** zéro pour l'équation, la divergence et la relation vorticité–vitesse ; zéro contre infini pour la semi-norme pondérée selon le prolongement. Le test réfute l'invariance de l'hypothèse sous changement de représentant sur le zéro de vorticité.

## 6. Provenance des espaces et des multiplicateurs

### Goldberg

Goldberg introduit le Hardy local \(h^1\) et son dual local \(bmo\). Le \(bmo\) inhomogène contrôle l'oscillation sur les petits cubes et une moyenne absolue sur les cubes de grande taille. Il ne définit pas le quotient log-pondéré de l'équation (2) de 2026, et il ne justifie pas le remplacement de l'ancre globale par \(L^\infty\).

### Janson

Janson définit les espaces d'oscillation pondérée \(BMO_\phi\) par une **semi-norme modulo les constantes**. Son résultat de multiplicateurs directement énoncé dans cet article est formulé sur le tore \(\mathbb T^d\), où une ancre \(L^1\) peut être ajoutée sans problème de volume infini. Janson explique aussi que si

\[
\int_0 \frac{\phi(r)}r\,dr=\infty,
\]

la classe peut contenir des fonctions non continues et non localement bornées. Cela autorise des contre-exemples, mais ne signifie pas que chaque fonction de la classe est discontinue.

### Nakai–Yabuta

Nakai–Yabuta étendent l'analyse des multiplicateurs du tore à \(\mathbb R^n\). Ils distinguent :

- \(BMO_\phi(\mathbb R^n)\), muni de la semi-norme d'oscillation et considéré modulo les constantes ;
- \(bmo_\phi(\mathbb R^n)\), rendu Banach par une ancre telle que \(|M(f,I(0,1))|\) ;
- un espace à poids \(w_\phi(x,r)\), dépendant aussi de la position, nécessaire dans leur théorème général de multiplicateurs sur \(\mathbb R^n\).

Leur théorème 1 ne dit donc pas simplement que les multiplicateurs du \(bmo_\phi(\mathbb R^n)\) euclidien sont le même \(bmo\) log-pondéré : le cas non compact comporte un poids spatial supplémentaire. Le théorème 2 traite séparément les intersections avec \(L^p\), et leur corollaire 4 relie le cas local de Goldberg à \(h^1\).

### Bradshaw–Grujić

Bradshaw–Grujić énoncent dans leur article le résultat précis dont ils ont besoin : si

\[
h\in\widetilde{bmo},
\qquad
g\in L^\infty\cap\widetilde{bmo}_{1/|\log r|},
\]

alors \(gh\in\widetilde{bmo}\), et ils identifient cet ensemble à l'espace des multiplicateurs ponctuels de leur \(\widetilde{bmo}\). Ils citent Janson, Nakai–Yabuta et la monographie de Maz'ya–Shaposhnikova, *Theory of Multipliers in Spaces of Differentiable Functions*, Pitman, 1985.

Cette chaîne de références ne permet pas de substituer silencieusement l'espace (2) de 2026 :

- \(L^1\) et \(L^\infty\) ne sont pas des ancres équivalentes sur \(\mathbb R^3\) ;
- les constantes non nulles appartiennent à l'espace 2026 mais pas au \(\widetilde{bmo}_\phi\) ancré par \(L^1\) ;
- les boules et cubes donnent des semi-normes comparables sous des hypothèses de poids et des changements d'échelle fixes, pas des expressions littéralement identiques ;
- l'espace 2015 porte sur \(\psi\xi\), l'espace 2026 sur \(\xi\).

Pour une fonction bornée à support compact, les deux conditions de finitude sont comparables à constantes près après conversion boules–cubes. Cette observation explique la proximité méthodologique, mais elle ne raccorde pas l'hypothèse globale non coupée de 2026 à celle de 2015.

Enfin, le théorème 4.1 de 2026 utilise un commutateur de Coifman–Rochberg–Weiss, pas le théorème de multiplicateurs ponctuels de 2015. L'audit de provenance des multiplicateurs ne réfute donc pas à lui seul le maillon commutateur ; il interdit seulement d'attribuer à l'espace (2), sans preuve séparée, toutes les propriétés du \(\widetilde{bmo}_\phi\) antérieur.

## 7. Uniformité en temps et constantes

Dans la v2, l'hypothèse

\[
\xi\in L^\infty((T^*-\epsilon,T^*);bmo_\phi)
\]

doit être lue comme l'existence d'une constante

\[
K_\xi=operatorname*{ess\,sup}_{t\in(T^*-\epsilon,T^*)}
\|\xi(t)\|_{bmo_\phi}<\infty.
\]

La ligne suivant l'estimation (8) dit que \(C_0\) dépend des « \(L^\infty_t\) suprema of \(\omega\) and \(\xi\) ». Si « supremum de \(\xi\) » signifie seulement \(\|\xi\|_{L^\infty_{t,x}}=1\), la dépendance annoncée omet \(K_\xi\), qui multiplie nécessairement les bornes d'oscillation. Une version quantitative doit écrire explicitement la dépendance en \(K_\xi\), en la borne \(L^{3/2,\infty}\) de \(\omega\), en la normalisation de \(\phi\) et en les constantes des opérateurs.

Le texte de 2015 expose au contraire directement

\[
\sup_{t\in(0,T)}|\psi\xi(t)\|_{\widetilde{bmo}_\phi}<\infty.
\]

Dans les deux cas, une convention de prolongement dépendant de \(t\) doit également être mesurable en espace-temps. Choisir séparément une « bonne » extension à chaque temps sans sélection mesurable ne suffit pas à définir l'hypothèse de Bochner ni les intégrales de la preuve.

## 8. Implications et non-implications pour le problème Clay

### Ce qui se transfère

- Les deux travaux étudient bien Navier–Stokes incompressible visqueux standard, non forcé, sur \(\mathbb R^3\), donc la famille d'équations est pertinente pour le cas entier du problème Clay.
- Une version correctement formulée de l'estimation de commutateur 2026 peut fournir un critère de régularité **conditionnel** pour une classe restreinte de scénarios critiques.
- Le résultat 2015 fournit sous son hypothèse une borne localisée \(L\log L\), utile comme maillon vers une amélioration de la distribution de la vorticité.

### Ce qui ne se transfère pas

- Aucune source n'établit que la direction d'une solution Clay arbitraire admet un prolongement global avec la borne log-BMO uniforme requise.
- La borne \(L\log L\) de 2015 n'est ni une preuve de régularité globale, ni une exclusion générale du blow-up.
- La v2 suppose en plus un profil ponctuel critique et une borne uniforme \(L^{3/2,\infty}\) de la vorticité ; elle ne traite pas tous les mécanismes Type II ou multi-échelles.
- Le cas périodique n'est pas couvert par simple changement de notation : l'ancre, les grandes échelles, la loi de Biot–Savart et la normalisation de la moyenne doivent être reformulées.
- Une condition sur une extension arbitraire de \(\xi\) aux zéros ne constitue pas un critère géométrique intrinsèque tant que le quantificateur d'extension n'est pas fixé.

Le premier lemme de raccord transférable est donc :

> **Lemme d'extension intrinsèque à établir.** À partir d'une condition géométrique portant seulement sur la direction dans une région de vorticité active, construire un prolongement mesurable \(\xi\) sur \(\mathbb R^3\), avec \(|\xi|\le1\), \(\boldsymbol\omega=|\boldsymbol\omega|\xi\), et une borne \(bmo_{1/|\log r|}\) uniforme en temps dont la constante ne dépend ni du seuil actif ni de l'échelle de localisation.

Le test de la solution nulle montre qu'un énoncé sans convention ou quantificateur d'extension échoue avant toute question de dynamique Navier–Stokes.

## 9. Sources à ajouter au registre central

La source Grujić 2026 est déjà enregistrée comme `0059`. Les entrées suivantes ne sont pas présentes dans `literature/navier-stokes/sources.json` lors de cette passe et devraient être ajoutées :

1. Bradshaw–Grujić 2015 — arXiv `1309.2519v5`, DOI `10.1512/iumj.2015.64.5496` ; rôle : définition de \(\widetilde{bmo}_\phi\), hypothèse \(\psi\xi\), borne localisée \(L\log L\).
2. Goldberg 1979 — DOI `10.1215/S0012-7094-79-04603-9` ; rôle : \(h^1\) local et \(bmo\) inhomogène.
3. Janson 1976 — DOI `10.1007/BF02385834` ; rôle : espaces d'oscillation pondérée modulo les constantes et multiplicateurs sur le tore.
4. Nakai–Yabuta 1985 — DOI `10.2969/jmsj/03720207` ; rôle : ancres et multiplicateurs sur \(\mathbb R^n\), distinction entre poids radial et poids position–échelle.
5. Maz'ya–Shaposhnikova 1985 — *Theory of Multipliers in Spaces of Differentiable Functions*, Monographs and Studies in Mathematics 23, Pitman ; rôle : provenance revendiquée du multiplicateur \(\widetilde{bmo}\). La normalisation exacte invoquée par Bradshaw–Grujić reste à contrôler directement dans la monographie avant de lui attribuer une affirmation détaillée.

## État de la revue

**Résultat négatif vérifié :** les hypothèses log-BMO de 2015 et 2026 ne sont pas intrinsèques à la vorticité en l'absence de définition de \(\xi\) sur ses zéros.  
**Résultat de provenance :** \(bmo_\phi^{(2026)}\neq\widetilde{bmo}_\phi^{(2015)}\) comme espaces ancrés sur \(\mathbb R^3\) ; Goldberg, Janson et Nakai–Yabuta n'identifient pas littéralement ces deux définitions.  
**Action suivante recommandée :** imposer une convention canonique aux zéros dans le lemme actif, puis tester si la semi-norme globale peut être déduite d'une hypothèse seulement sur les super-niveaux de vorticité avec constante indépendante du seuil.  
**État :** RÉVISER.
