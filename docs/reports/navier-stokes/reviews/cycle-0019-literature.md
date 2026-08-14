# Revue bibliographique contradictoire — cycle 0019

Date de vérification : 2026-08-14  
Périmètre : équations (49)–(58), théorème de rayon d’analyticité et critère de sparseness/mesure harmonique de Z. Grujić, [arXiv:2607.08866v2](https://arxiv.org/abs/2607.08866).

## Verdict exécutif

1. Le dossier primaire demeure **arXiv v2**, révisé le 13 juillet 2026. Il ne liste ni v3, ni référence de revue, ni erratum. Les recherches exactes par titre, identifiant et mots « erratum/correction/published » n’ont révélé aucun autre enregistrement primaire au 2026-08-14. Le DOI [10.48550/arXiv.2607.08866](https://doi.org/10.48550/arXiv.2607.08866) est le DOI DataCite du préprint, pas un DOI de publication.
2. Les équations (49), (50), (53)–(58) et le théorème 7.4 sont des **énoncés ou dérivations propres à la prépublication**. Ils ne doivent pas être classés comme résultats publiés.
3. Les briques publiées sous-jacentes sont réelles : analyticité spatiale locale des solutions mild \(L^\infty\), principe de majoration par mesure harmonique, borne extrémale de Solynin et critère 1D de Grujić. Toutefois, leur raccord dans le préprint n’est pas une simple citation de théorème publié.
4. Le théorème 7.3 est correctement dimensionné après remise de la viscosité \(\nu\), mais son attribution « Gu [22] » doit être lue comme R. **Guberović**. La version à paramètre arbitraire \(M>1\) est explicitement consignée dans Grujić–Xu 2024; Grujić 2013 donne une version à constante absolue \(c_0\).
5. Le défaut local principal est temporel : le théorème d’analyticité ne définit aucun « maximal local analyticity time » \(T_t\). Si \(T_t\) désigne le temps maximal réel issu de \(t\), alors, sous l’hypothèse que \(T^*\) est le premier temps singulier, \(t+T_t=T^*\), où la solution utilisée dans (54)–(58) n’est pas disponible. S’il désigne seulement le temps garanti par le théorème, une dichotomie \(t+\tau_t\geq T^*\) / \(t+\tau_t<T^*\) manque.
6. Le critère publié de Grujić 2013 contient précisément cette dichotomie et impose un temps
   \[
   s\in\left[t+\frac{1}{4c_0^2\|u(t)\|_\infty^2},
                 t+\frac{1}{c_0^2\|u(t)\|_\infty^2}\right]
   \subset (t,T^*).
   \]
   La preuve du préprint est donc **réparable à ce maillon** en choisissant un temps garanti et non un temps « maximal », à condition que la borne de distribution uniforme (49) soit déjà valide à ce temps.
7. La réduction (55) vers la sparseness est correcte conditionnellement, mais (56) doit désigner **un rayon témoin explicitement choisi**. La seule inégalité \(r_s\leq\cdots\) ne garantit rien pour un rayon arbitraire plus petit.
8. Les constantes de Solynin et de la combinaison convexe dans (53), (57), (58) sont cohérentes. Le passage utilise néanmoins une nouvelle scalarisation \(F=u\cdot e\) et le principe additif pour \(\Re F\), tandis que Grujić 2013 utilise le théorème multiplicatif des deux constantes. La convention de norme vectorielle complexe doit être fixée pour conserver exactement le même \(M\).

**Statut du raccord (49)–(58) : RÉVISER.** Les briques harmoniques et géométriques sont publiées et compatibles; le choix temporel de \(s\) n’est pas justifié tel qu’écrit. Ce verdict ne certifie pas la borne amont (49).

## 1. Formulation mathématique auditée

Le préprint traite les équations de Navier–Stokes **incompressibles, visqueuses, non forcées**, en dimension trois et sur \(\mathbb R^3\), avec viscosité \(\nu>0\). Le théorème 7.4 part d’une solution unique spatialement analytique sur \((0,T^*)\), \(T^*\) étant supposé premier temps singulier possible. La reprise locale au temps \(t<T^*\) est une solution **mild** issue de \(u(t)\in L^\infty(\mathbb R^3)\).

Les hypothèses supplémentaires du théorème 7.4 ne sont pas celles du problème Clay général :

- profil ponctuel critique de vorticité uniforme près de \(T^*\), notamment
  \(\omega\in L^\infty_tL^{3/2,\infty}_x\);
- facteur de forme du profil soumis aux hypothèses de la définition 2.1 du préprint;
- direction de vorticité
  \(\xi\in L^\infty_t\mathrm{bmo}_{1/|\log r|}\).

La conclusion annoncée est une exclusion conditionnelle de ce scénario, non une régularité globale inconditionnelle de toutes les données Clay.

## 2. Statut primaire et versions

### 2.1 Prépublication auditée

La [notice arXiv officielle](https://arxiv.org/abs/2607.08866) indique :

- auteur : Zoran Grujić;
- v1 : 9 juillet 2026, 18:38:04 UTC;
- v2 : 13 juillet 2026, 15:30:27 UTC;
- commentaire v2 : corrections typographiques et reformulations;
- aucune v3, aucune référence de revue et aucun erratum listés.

L’en-tête du [texte HTML v2](https://arxiv.org/html/2607.08866v2) porte bien « arXiv:2607.08866v2 [math.AP] 13 Jul 2026 ». La date interne « August 11, 2026 » rendue dans le corps HTML ne constitue pas une version supplémentaire.

Une veille différentielle exacte par titre et identifiant n’a trouvé, à la date de coupure, que la notice arXiv et des agrégateurs reprenant cette notice. L’absence de résultat de recherche ne prouve pas l’inexistence absolue d’une soumission éditoriale privée; elle établit seulement qu’aucune publication, correction ou v3 **primaire et publiquement vérifiable** n’a été localisée.

### 2.2 Sources publiées du raccord

| Source | Statut et version | Équation, domaine, solution | Apport exact |
|---|---|---|---|
| R. Guberović, *Smoothness of Koch-Tataru solutions to the Navier-Stokes equations revisited*, DCDS 27(1), 231–236 (2010), [doi:10.3934/dcds.2010.27.231](https://doi.org/10.3934/dcds.2010.27.231) | Article publié; reçu janvier 2009, révisé décembre 2009, en ligne février 2010 | Navier–Stokes incompressible sur l’espace entier; solutions Koch–Tataru/mild | Analyticité spatiale et décroissance des dérivées. C’est la référence [22] du préprint. |
| Z. Grujić, *A geometric measure-type regularity criterion for solutions to the 3D Navier-Stokes equations*, Nonlinearity 26(1), 289–296 (2013), [doi:10.1088/0951-7715/26/1/289](https://doi.org/10.1088/0951-7715/26/1/289), [arXiv:1111.0217v5](https://arxiv.org/abs/1111.0217) | Article publié; v5 finale du 8 novembre 2012 | NSE 3D non forcées sur \(\mathbb R^3\), viscosité normalisée à 1; solution régulière jusqu’à \(T^*\), redémarrage mild \(L^\infty\) | Définition de sparseness 1D, fenêtre temporelle, rayon analytique et endgame par mesure harmonique. |
| Z. Grujić et L. Xu, *Asymptotic Criticality of the Navier–Stokes Regularity Problem*, J. Math. Fluid Mech. 26, 53 (2024), [doi:10.1007/s00021-024-00888-x](https://doi.org/10.1007/s00021-024-00888-x) | Article publié le 27 juillet 2024 | Formulation vitesse sur \(\mathbb R^d\), viscosité 1; théorème mild \(L^\infty\) rappelé | Énonce explicitement la version « pour tout \(M>1\), il existe \(c(M)\) », ainsi que la réduction sparseness \(d\)D vers 1D. |
| T. Ransford, *Potential Theory in the Complex Plane*, CUP (1995), chap. 4, [doi:10.1017/CBO9780511623776.006](https://doi.org/10.1017/CBO9780511623776.006) | Monographie publiée | Fonctions sous-harmoniques sur un domaine complexe | Principe additif de majoration par mesure harmonique utilisé dans (51). |
| A. Yu. Solynin, *Ordering of sets, hyperbolic metric, and harmonic measure*, POMI 237 (1997), 129–147; traduction J. Math. Sci. 95(3) (1999), 2256–2266, [doi:10.1007/BF02172470](https://doi.org/10.1007/BF02172470) | Article publié; notice primaire [Math-Net](https://www.mathnet.ru/eng/znsl433) | Problème extrémal de mesure harmonique dans le disque | Borne inférieure de (52). |

La référence [17] du préprint, Z. Grujić, *Localization and Geometric Depletion of Vortex-Stretching in the 3D NSE*, Comm. Math. Phys. 290, 861–870 (2009), [doi:10.1007/s00220-008-0726-8](https://doi.org/10.1007/s00220-008-0726-8), est un résultat publié de localisation des critères portant sur la direction de vorticité pour des solutions de Leray. Elle n’est pas la source du critère de sparseness 1D ni de la mesure harmonique employée dans (50)–(58).

## 3. Transcription des équations (49)–(58)

Cette section est une **transcription normalisée** de la v2, non une validation.

### (49) — distribution de la vitesse

\[
\left|\{x\in\mathbb R^3:|u(x,t)|>\lambda\}\right|
\leq \frac{C_u}{\lambda^3(\log\lambda)^3},
\tag{49}
\]

avec \(C_u\) annoncé indépendant du temps sur \((T^*-\epsilon,T^*)\).

### (50) — superniveau relatif

\[
V_t=\{x\in\mathbb R^3:\ |u(x,t)|
>\lambda\|u(t)\|_\infty\},
\qquad \lambda\in(0,1).
\tag{50}
\]

Le symbole \(\lambda\) change ici de rôle : niveau absolu dans (49), fraction sans dimension dans (50).

### (51) — principe additif de mesure harmonique

\[
v(z)\leq m\,h(z,\Omega,K)
+M_0\bigl(1-h(z,\Omega,K)\bigr).
\tag{51}
\]

### (52) — borne extrémale de Solynin

\[
h(0,\mathbb D\setminus K,K)
\geq \frac{2}{\pi}\arcsin
\left(\frac{1-(1-\alpha)^2}{1+(1-\alpha)^2}\right),
\quad K\subset[-1,1],\quad |K|=2\alpha,\quad 0\notin K.
\tag{52}
\]

### (53) — constante harmonique synchronisée

\[
h^*=\frac{2}{\pi}\arcsin
\left(\frac{1-(3/4)^{2/3}}{1+(3/4)^{2/3}}\right).
\tag{53}
\]

Le texte choisit ensuite \(M>1\) par
\[
\frac12h^*+(1-h^*)M=1,
\qquad
\lambda=\frac{1}{2M}.
\]

### (54) — rayon d’analyticité réécrit avec l’amplitude au temps \(s\)

\[
\rho_s=\frac{1}{c_3}\frac{\nu}{\|u(s)\|_\infty}.
\tag{54}
\]

### (55) — volume du superniveau au temps \(s\)

\[
|V_s|
\leq
\frac{C}
{\lambda^3\|u(s)\|_\infty^3
\log^3\!\bigl(e+\lambda\|u(s)\|_\infty\bigr)}.
\tag{55}
\]

### (56) — échelle annoncée de sparseness

\[
r_s\leq
\frac{c_4}
{\|u(s)\|_\infty
\log\!\bigl(e+\lambda\|u(s)\|_\infty\bigr)}.
\tag{56}
\]

### (57) — majoration harmonique au point arbitraire

\[
\begin{aligned}
|u(0,s)|=v(0)
&\leq h^*
\left(\frac{1}{2M}\|u(s)\|_\infty\right)\\
&\quad +(1-h^*)\left(M\|u(t)\|_\infty\right).
\end{aligned}
\tag{57}
\]

### (58) — combinaison finale

\[
|u(0,s)|
\leq
\left[\frac12h^*+(1-h^*)M\right]
\|u(t)\|_\infty.
\tag{58}
\]

## 4. Provenance équation par équation

| Maillon | Statut de provenance | Audit |
|---|---|---|
| (49) | Dérivation de la prépublication à partir de (47)–(48) | Aucun article publié cité ne fournit cette borne. Une version à grand niveau peut être dérivée conditionnellement d’une borne uniforme de réarrangement, mais l’égalité d’inversion et la notation \(\log\lambda\) de la v2 ne suffisent pas. |
| (50) | Définition de la prépublication | La notion de superniveau est classique. Le critère publié de 2013 utilise aussi des superniveaux de vitesse, mais avec un seuil calibré par les constantes du théorème. |
| (51) | Résultat publié de théorie du potentiel | Forme additive correcte pour une fonction sous-harmonique. Dans l’application, le domaine est le disque fendu \(D_{r_s}\setminus K\), même si la notation alterne entre \(h(0,D_{r_s},K)\) et \(h(0,D_{r_s}\setminus K,K)\). |
| (52) | Résultat publié de Solynin | Formule conforme au théorème repris dans Grujić 2013. Si \(|K|\) est seulement minorée, il faut utiliser la monotonie ou extraire un sous-compact de mesure exacte. |
| 3D \(\delta\)-sparse \(\Rightarrow\) 1D \(\delta^{1/3}\)-sparse | Résultat publié, mais attribution incomplète | Grujić 2013 définit directement la sparseness 1D et ne prouve pas ce passage volumique. La formulation même rayon apparaît explicitement dans la chaîne publiée jusqu’à Grujić–Xu 2024. |
| (53) | Calcul de la prépublication à partir de Solynin | Correct : la densité 1D vaut \(\eta=(3/4)^{1/3}\), le vide relatif vaut \(1-\eta\), d’où \(1-(1-\alpha)^2=1-\eta^2\). |
| Théorème 7.3 | Restatement d’un résultat publié, avec remise à l’échelle en \(\nu\) | Correct en structure; les constantes doivent être renommées explicitement et le temps doit être un temps écoulé depuis le redémarrage. Le théorème fournit un temps garanti, pas un temps maximal. |
| (54) | Dérivation de la prépublication | Conditionnellement correcte si \(s=t+\tau\) est dans l’intervalle analytique garanti. L’égalité signifie qu’on choisit un sous-rayon de la borne disponible. Tel qu’écrit, le choix de \(s\) n’est pas établi. |
| (55) | Substitution interne de (49) | Conditionnelle à (49), à un seuil de grande amplitude et à une constante uniforme. Le remplacement de \(\log\beta\) par \(\log(e+\beta)\) requiert une globalisation quantitative; il n’est pas une substitution littérale dans (49). |
| (56) | Dérivation interne géométrique | Réparable en définissant un rayon témoin. La direction logique est « choisir \(r_s\) assez grand par rapport à \(|V_s|^{1/3}\) »; un rayon arbitrairement plus petit peut perdre la sparseness. |
| (57)–(58) | Nouvelle dérivation de la prépublication à partir de (51)–(53) et du théorème 7.3 | L’algèbre est correcte si la borne complexe utilise la norme compatible avec la projection \(u\cdot e\), si \(s\) est admissible et si \(m\leq M_0\). Ce n’est pas la preuve multiplicative publiée en 2013. |

## 5. Théorème d’analyticité : énoncé exact et constantes

### 5.1 Forme publiée à viscosité normalisée

Le théorème 3.1 de [Grujić 2013, v5 finale](https://arxiv.org/html/1111.0217v5) affirme : pour \(u_0\in L^\infty(\mathbb R^3)\), il existe une constante absolue \(c_0>1\) telle que

\[
T=\frac{1}{c_0^2\|u_0\|_\infty^2},
\qquad
\mathcal R_\tau=
\left\{x+iy\in\mathbb C^3:\ |y|\leq\frac{\sqrt{\tau}}{c_0}\right\},
\]

et la solution mild unique vérifie

\[
\|U(\tau)\|_{L^\infty(\mathcal R_\tau)}
\leq c_0\|u_0\|_\infty,
\qquad 0\leq\tau\leq T.
\]

Le théorème 2.1 de [Grujić–Xu 2024](https://link.springer.com/article/10.1007/s00021-024-00888-x) donne la paramétrisation utilisée par le préprint : pour tout \(M>1\), il existe \(c(M)\) tel que

\[
T\geq\frac{1}{c(M)^2\|u_0\|_\infty^2},
\qquad
|y|\leq\frac{\sqrt{\tau}}{c(M)},
\qquad
\sup_{\tau\leq T}\|U(\tau)\|_\infty
\leq M\|u_0\|_\infty.
\]

Il s’agit d’un résultat sur une solution **mild \(L^\infty\)**, et non d’une borne a priori pour toute solution faible de Leray–Hopf.

### 5.2 Remise de la viscosité

Pour
\[
u_t+(u\cdot\nabla)u+\nabla p=\nu\Delta u,
\qquad \nabla\cdot u=0,
\]
le changement \(x=\nu y\), \(t=\nu\tau\) ramène \(\nu\) à 1 sans modifier l’amplitude de la vitesse. Il donne

\[
\tau_{\rm loc}
\geq \frac{\nu}{c(M)^2\|u_0\|_\infty^2},
\qquad
\rho(\tau)\geq\frac{\sqrt{\nu\tau}}{c(M)}.
\]

La forme du théorème 7.3,
\[
T\geq\frac{\nu}{c_1(M)\|u_0\|_\infty^2},
\qquad
\rho(\tau)\geq\frac{\sqrt{\nu\tau}}{c_2(M)},
\]
est donc équivalente après renommage des constantes.

Si l’on choisit exactement
\[
\tau_t=\frac{\nu}{c_1(M)\|u(t)\|_\infty^2},
\]
alors
\[
\rho(t+\tau_t)
\geq
\frac{1}{c_2(M)\sqrt{c_1(M)}}
\frac{\nu}{\|u(t)\|_\infty}.
\]
Ainsi, à ce seul niveau,
\[
c_3=c_2(M)\sqrt{c_1(M)}
\]
est une constante admissible. Si l’on choisit le quart inférieur de la fenêtre publiée, un facteur 2 supplémentaire apparaît.

### 5.3 Temps absolu contre temps écoulé

Dans le théorème local, la variable \(\tau\) est le **temps écoulé depuis la donnée initiale**. Après redémarrage à l’escape time \(t\), il faut écrire
\[
\tau=s-t,
\qquad
\rho_s\geq \frac{\sqrt{\nu(s-t)}}{c_2(M)}.
\]
Employer directement le temps absolu \(s\) serait faux. Le texte de la preuve utilise implicitement le temps écoulé, mais ne le formalise pas.

## 6. Trou temporel et raccord publié

Le préprint choisit
\[
s=t+T_t,
\]
où \(T_t\) est appelé « maximal local analyticity time ». Aucun objet de ce nom n’est défini par le théorème 7.3.

Deux interprétations échouent ou exigent une correction :

1. **Temps maximal réel.** Si \(T^*\) est le premier temps singulier et si l’on repart à \(t<T^*\), la durée maximale de la branche régulière est \(T^*-t\). Alors \(s=T^*\), mais les normes \(\|u(s)\|_\infty\), le superniveau \(V_s\) et l’extension holomorphe utilisés dans (54)–(58) ne sont pas disponibles.
2. **Temps local garanti.** Si \(T_t=\tau_t=\nu/(c_1(M)\|u(t)\|_\infty^2)\), le signe de
   \[
   T^*-t-\tau_t
   \]
   n’est pas fixé. La preuve doit distinguer les deux signes.

Le théorème 4.1 de Grujić 2013 effectue exactement le raccord manquant, à \(\nu=1\) :

- si \(t+1/(c_0^2\|u(t)\|_\infty^2)\geq T^*\), le théorème local prolonge directement la solution au-delà de \(T^*\);
- sinon, il exige un
  \[
  s\in
  \left[
  t+\frac{1}{4c_0^2\|u(t)\|_\infty^2},
  t+\frac{1}{c_0^2\|u(t)\|_\infty^2}
  \right]
  \subset(t,T^*)
  \]
  auquel la condition de sparseness est satisfaite.

Dans la stratégie de la v2, (49) est annoncé uniforme à tous les temps proches de \(T^*\). Conditionnellement à cette uniformité, on peut choisir le premier quart de la fenêtre :
\[
s=t+\frac{\nu}
{4c_1(M)\|u(t)\|_\infty^2}.
\]
On obtient alors simultanément \(s<T^*\), la borne complexe
\(\|U(s)\|_\infty\leq M\|u(t)\|_\infty\) et
\[
\rho_s\geq
\frac{1}{2c_2(M)\sqrt{c_1(M)}}
\frac{\nu}{\|u(t)\|_\infty}
\geq
\frac{1}{2c_2(M)\sqrt{c_1(M)}}
\frac{\nu}{\|u(s)\|_\infty},
\]
la dernière inégalité utilisant la propriété d’escape
\(\|u(s)\|_\infty>\|u(t)\|_\infty\).

Cette réparation est une **dérivation interne auditée**, pas un passage présent dans la v2.

## 7. Sparseness et mesure harmonique

### 7.1 Rayon témoin issu de (55)

Posons
\[
A_s=\|u(s)\|_\infty,\qquad
L_s=\log(e+\lambda A_s),\qquad
v_3=\frac{4\pi}{3},
\]
et supposons (55) avec
\[
B_s=\frac{C}{\lambda^3A_s^3L_s^3}.
\]
Pour \(\delta_3=3/4\), il faut **définir**
\[
r_s=\left(\frac{B_s}{\delta_3v_3}\right)^{1/3}
=
\left(\frac{C}{\delta_3v_3}\right)^{1/3}
\frac{1}{\lambda A_sL_s}.
\]
Alors, pour tout \(x_0\),
\[
\frac{|V_s\cap B_{r_s}(x_0)|}{|B_{r_s}|}
\leq
\frac{|V_s|}{v_3r_s^3}
\leq\delta_3.
\]

Ce calcul valide une forme existentielle de (56), conditionnellement à (55). Il ne permet pas d’affirmer la sparseness pour tout \(r_s\) plus petit que le membre droit de (56).

### 7.2 Passage 3D vers 1D

La sparseness 3D au même centre et au même rayon implique l’existence d’une direction \(\nu(x_0)\) telle que la densité linéaire soit au plus
\[
\eta=\delta_3^{1/3}=(3/4)^{1/3}.
\]
Le complément \(K\) du superniveau sur le diamètre réel a donc une longueur au moins
\[
|K|\geq2r_s(1-\eta).
\]

Ce lemme est publié dans la chaîne moderne des classes de sparseness, notamment Grujić–Xu 2024. La référence [18] de 2013 est pertinente pour le critère 1D qui suit, mais ne source pas à elle seule cette réduction volumique.

### 7.3 Constante de Solynin

Avec \(\alpha=1-\eta\), (52) donne
\[
h^*=
\frac2\pi\arcsin
\frac{1-\eta^2}{1+\eta^2}
=
\frac2\pi\arcsin
\frac{1-(3/4)^{2/3}}{1+(3/4)^{2/3}}.
\]
Les valeurs de contrôle sont

| Quantité | Valeur |
|---|---:|
| \(\eta=(3/4)^{1/3}\) | \(0.908560296416070\) |
| \(1-\eta\) | \(0.091439703583930\) |
| \(h^*\) | \(0.060954683483033\) |
| \(M=(1-h^*/2)/(1-h^*)\) | \(1.032455666628061\) |
| \(\lambda=1/(2M)\) | \(0.484282295270818\) |

La synchronisation de (53) est donc correcte.

### 7.4 Principe harmonique et norme

Au point \(x_0\), le préprint choisit
\[
e=\frac{u(x_0,s)}{|u(x_0,s)|},
\qquad
F(z)=U(z,s)\cdot e,
\qquad
v(z)=\Re F(z).
\]
Alors \(v(0)=|u(x_0,s)|\), et \(v\) est harmonique. Sur \(K\),
\[
v\leq|F|\leq|u|
\leq\frac{1}{2M}A_s.
\]
Sur le disque complexe, il faut disposer de
\[
v\leq|F|\leq M\|u(t)\|_\infty.
\]

Cette dernière implication est immédiate si le théorème d’analyticité emploie la norme euclidienne complexe et la projection par un vecteur réel unitaire. Si la source emploie la norme composante par composante
\(|z|_\infty=\max_j|z_j|\), alors seulement
\[
|F|\leq\|e\|_1\,|U|_\infty\leq\sqrt3\,|U|_\infty,
\]
et la combinaison exacte définissant \(M\) doit absorber \(\sqrt3\). Grujić–Xu 2024 annonce explicitement une convention de norme par maximum des composantes dans son cadre de sparseness. La v2 doit donc fixer la convention de norme de son théorème 7.3 ou recalibrer \(M\).

Sous la convention compatible, le remplacement de la mesure harmonique réelle \(h\geq h^*\) par \(h^*\) dans (57) est valide car
\[
m=\frac{A_s}{2M}
\leq\frac12\|u(t)\|_\infty
<
M\|u(t)\|_\infty=M_0,
\]
où l’on a utilisé \(A_s\leq M\|u(t)\|_\infty\). L’expression
\(mh+M_0(1-h)\) décroît donc avec \(h\).

## 8. Tests adverses reproductibles

### Test A — sémantique du « temps maximal »

Prendre au sérieux la définition littérale : \(T_t\) est la durée maximale de la branche analytique démarrant à \(t\). Sous l’hypothèse du préprint que \(T^*\) est le premier temps singulier,
\[
T_t=T^*-t,
\qquad
s=t+T_t=T^*.
\]
L’obligation de preuve est \(s<T^*\), alors que le résidu exact vaut
\[
T^*-s=0.
\]
Le test réfute l’interprétation « maximal ». Il ne réfute pas l’approche corrigée par un temps local garanti.

### Test B — signe non contrôlé du temps garanti

Avec
\[
\tau_t=\frac{\nu}{c_1(M)\|u(t)\|_\infty^2},
\]
le théorème d’analyticité ne fixe pas le signe de
\[
R_{\rm time}=T^*-t-\tau_t.
\]
Si \(R_{\rm time}\leq0\), la continuation locale règle déjà le problème; si \(R_{\rm time}>0\), le calcul harmonique doit choisir \(s<t+\tau_t<T^*\). Une preuve sans cette dichotomie est incomplète.

### Test C — orientation du rayon

À saturation de (55), définir \(r_s=(B_s/(\delta_3v_3))^{1/3}\). Le résidu de densité est exactement
\[
\frac{B_s}{v_3r_s^3}-\delta_3=0.
\]
Remplacer \(r_s\) par \(r_s/2\) multiplie la borne de densité par \(8\), donnant \(8\delta_3=6>1\). Ce calcul falsifie l’interprétation « tout rayon inférieur à la borne (56) est sparse ».

### Test D — synchronisation harmonique

Avec
\[
M=\frac{1-h^*/2}{1-h^*},
\]
le résidu symbolique de (58) est
\[
R_{\rm harm}
=\frac12h^*+(1-h^*)M-1
=0.
\]
Ce test confirme l’algèbre de (53), (57), (58), mais pas les hypothèses temporelles ou normatives nécessaires à (57).

### Test E — logarithme et seuil

Dans (49), \(\log\lambda\) est négatif pour \(0<\lambda<1\), tandis que (50) impose précisément une fraction \(\lambda\in(0,1)\). Les deux \(\lambda\) n’ont pas la même dimension ni le même rôle. Le test de substitution littérale échoue. Une version correcte doit introduire :

- un niveau absolu \(\Lambda\geq\Lambda_*\) dans (49);
- une fraction \(\theta\in(0,1)\) dans (50);
- un logarithme sans dimension, par exemple
  \(\log(e+\theta A_s/A_{\rm ref})\);
- un seuil assurant \(\theta A_s\geq\Lambda_*\).

## 9. Implication explicite vers le problème Clay

La chaîne publiée donne l’implication conditionnelle suivante :
\[
\begin{gathered}
\text{solution régulière jusqu’à }T^*
+\text{ analyticité mild locale}\\
+\text{ sparseness 1D des superniveaux à un temps admissible }s<T^*
\Longrightarrow
\text{prolongement au-delà de }T^*.
\end{gathered}
\]

Le préprint tente de produire automatiquement la sparseness requise à partir de (49). Si (49) est établie uniformément avec seuil et constante, si le rayon témoin de la section 7.1 est utilisé, si le temps est choisi par la dichotomie de la section 6 et si les normes sont synchronisées, alors le raccord au critère harmonique est plausible et quantitatif.

Cela ne transfère pas le théorème 7.4 au problème Clay général, car les hypothèses de profil ponctuel critique et de direction
\(\mathrm{bmo}_{1/|\log r|}\) restent supplémentaires. Le résultat transférable est seulement :

> exclusion conditionnelle d’un sous-ensemble de scénarios de blow-up classiques sur \(\mathbb R^3\).

Il ne couvre ni le cas périodique Clay sans nouveau raccord, ni des concentrations multi-points ou multi-échelles non décrites par la définition 2.1, ni une solution faible qui n’est pas déjà régulière avant \(T^*\).

## 10. Recommandations pour le graphe de preuves

- Classer (51), (52) et le théorème local d’analyticité comme **résultats publiés** avec leurs hypothèses exactes.
- Classer (49), (53)–(58) et le théorème 7.4 comme **prépublication / dérivation non publiée**.
- Remplacer le nœud « maximal local analyticity time » par une dichotomie :
  \[
  \text{temps garanti franchit }T^*
  \quad\text{ou}\quad
  s\text{ appartient à la fenêtre analytique avant }T^*.
  \]
- Définir \(r_s\) par égalité à partir de la borne \(B_s\), puis enregistrer la propriété « sparse à ce rayon et aux rayons supérieurs », pas « à tout rayon inférieur ».
- Ajouter un nœud explicite de convention de norme entre la borne holomorphe vectorielle et la projection scalaire \(F=U\cdot e\).
- Conserver séparément les obligations amont : validité uniforme de (49), seuil de grande amplitude, logarithme sans dimension et stabilité de la constante \(C_u\).

### Entrées recommandées pour le registre des affirmations

| Nœud proposé | Statut recommandé | Justification |
|---|---|---|
| Analyticité mild \(L^\infty\) sur \(\mathbb R^3\), durée \(O(\nu\|u_0\|_\infty^{-2})\), rayon \(O(\sqrt{\nu\tau})\) | \(PAPER\_PROOF\) | Guberović 2010; restatements quantifiés Grujić 2013 et Grujić–Xu 2024. |
| Borne extrémale de Solynin (52) | \(PAPER\_PROOF\) | Solynin 1997/1999. |
| Critère de régularité par sparseness 1D à un temps admissible | \(PAPER\_PROOF\) | Grujić 2013, avec dichotomie et fenêtre temporelles explicites. |
| Réduction 3D \(\delta\)-sparse vers 1D \(\delta^{1/3}\)-sparse au même rayon | \(PAPER\_PROOF\) | Chaîne publiée culminant dans Grujić–Xu 2024; ne pas l’attribuer à la seule référence [18]. |
| Distribution logarithmique de vitesse (49) | \(PREPRINT\_CLAIM\), conditionnelle | Propre à arXiv:2607.08866v2; inversion, seuil et uniformité à documenter séparément. |
| (55) vers rayon témoin sparse | \(INTERNAL\_DERIVATION\), vérifiée conditionnellement | Preuve algébrique de la section 7.1, sous (55). Ne pas lui attribuer automatiquement \(PAPER\_PROOF\). |
| Synchronisation (53), (57), (58) | \(INTERNAL\_DERIVATION\), vérifiée conditionnellement | Résidu algébrique nul; dépend encore du temps admissible et de la convention de norme. |
| Choix \(s=t+T_t\) avec \(T_t\) « maximal » | \(GAP\) / \(REFUTED\_AS\_STATED\) | Donne \(s=T^*\) sous l’interprétation littérale; le théorème cité ne définit pas \(T_t\). |
| Théorème 7.4 de la v2 | \(PREPRINT\_CLAIM\), non validé | Le raccord temporel doit être remplacé par la dichotomie publiée; les obligations amont demeurent ouvertes. |

## Sources primaires consultées

1. Z. Grujić, [arXiv:2607.08866, notice et historique](https://arxiv.org/abs/2607.08866).
2. Z. Grujić, [arXiv:2607.08866v2, texte HTML](https://arxiv.org/html/2607.08866v2).
3. Z. Grujić, [arXiv:1111.0217v5, texte final](https://arxiv.org/html/1111.0217v5), publié dans Nonlinearity 26 (2013), 289–296.
4. R. Guberović, [DCDS 27 (2010), 231–236](https://www.aimsciences.org/article/doi/10.3934/dcds.2010.27.231).
5. Z. Grujić et L. Xu, [J. Math. Fluid Mech. 26, 53 (2024)](https://link.springer.com/article/10.1007/s00021-024-00888-x).
6. A. Yu. Solynin, [notice primaire Math-Net](https://www.mathnet.ru/eng/znsl433).
7. T. Ransford, [Potential Theory in the Complex Plane, chapitre 4](https://www.cambridge.org/core/product/identifier/CBO9780511623776A031/type/BOOK_PART).
