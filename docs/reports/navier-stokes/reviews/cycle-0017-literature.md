# Passe bibliographique séparée — cycle 0017

**Qualification.** Cette passe a été réalisée séparément de la dérivation principale du cycle. Elle constitue une revue contradictoire de **même famille de modèle et de même environnement**, utile pour vérifier les sources, les quantificateurs et l'algèbre, mais insuffisante comme validation extérieure indépendante.

**Périmètre.** Statut primaire de `arXiv:2607.08866`, transcription des équations (20)–(40), sources primaires des inégalités de Lorentz–Sobolev, Sobolev/Poincaré sur le support et de la méthode de De Giorgi, puis audit local du passage troncation–interpolation–amortissement.

**Date de vérification en ligne.** 14 août 2026.

## Verdict

- Le dossier primaire courant est toujours **arXiv v2**, soumis le 9 juillet 2026 et révisé le 13 juillet 2026. La notice ne liste ni v3, ni référence de revue, ni erratum. Le statut vérifiable reste donc « prépublication arXiv v2 » ([notice arXiv](https://arxiv.org/abs/2607.08866), [texte HTML v2](https://arxiv.org/html/2607.08866v2), DOI DataCite [10.48550/arXiv.2607.08866](https://doi.org/10.48550/arXiv.2607.08866)).
- La date « August 11, 2026 » imprimée dans le corps HTML n'est pas une nouvelle version arXiv : l'en-tête du même document porte explicitement `arXiv:2607.08866v2 [math.AP] 13 Jul 2026`.
- Une recherche différentielle par identifiant, titre exact, auteur, `erratum`, `correction` et `v3` n'a localisé **aucun erratum ni version primaire postérieure** au 14 août 2026. Ce résultat négatif porte sur les notices primaires publiquement indexées consultées ; il ne prouve pas l'absence d'une communication privée ou d'un dépôt non indexé.
- Les identités algébriques et les exposants des équations (23)–(39) sont, sous les hypothèses fonctionnelles requises, cohérents. En particulier, les puissances de `λ`, `M₀` et `ν` dans (31), (35) et (37) se recomposent correctement.
- L'équation (33) n'utilise pas une inégalité de Poincaré dépendant de la géométrie du superniveau. Elle combine Hölder sur le support et le Sobolev homogène sur `R³`. C'est une inégalité de « Poincaré sur le support » au sens dérivé, avec constante indépendante de la forme de `A_λ(t)`.
- L'appellation « interpolated De Giorgi energy method » est plus large que ce qui est effectivement écrit : (23)–(40) ne contiennent ni suite de niveaux, ni cylindres emboîtés, ni récurrence superlinéaire, ni passage à `L∞`. Le maillon effectivement présent est une **troncation positive à niveau fixé**, une interpolation de Lorentz, un ODE amorti et Tchebychev.
- Deux défauts de quantification sont identifiés : (i) (25) est disponible, par le théorème 4.1, seulement sur l'intervalle terminal `I=(T*−ε,T*)`, alors que le texte affirme ensuite l'absorption sur tout `(0,T*)`; (ii) les comparaisons logarithmiques de (21), (25) et du renommage (39) → (40) exigent des seuils explicites que les affichages omettent.
- Le défaut temporel de (25) est localement réparable pour (26)–(40), car l'ODE est ensuite intégré seulement sur `I`. En revanche, la présente passe ne réaudite pas les estimations de commutateur antérieures à (20), le transfert (40) → vitesse, ni l'endgame de mesure harmonique ; elle ne valide donc ni le théorème 4.1 ni le théorème 7.4.

## Statut primaire et équation étudiée

Le manuscrit est :

> Zoran Grujić, “Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier-Stokes Equations”, arXiv:2607.08866v2 [math.AP], 13 juillet 2026.

Il considère les Navier–Stokes incompressibles visqueuses en dimension trois sur `R³`, sans frontière, avec viscosité `ν>0`. Dans le passage audité,

\[
\boldsymbol\omega=\nabla\times\boldsymbol u,
\qquad
\omega=|\boldsymbol\omega|,
\qquad
\boldsymbol\xi=\boldsymbol\omega/|\boldsymbol\omega|,
\qquad
\alpha=\boldsymbol\xi\cdot S\boldsymbol\xi,
\]

et la magnitude vérifie l'inégalité scalaire

\[
(\partial_t+\boldsymbol u\cdot\nabla-\nu\Delta)\omega\leq\alpha\omega.
\]

Les hypothèses terminales utilisées en amont des équations reproduites sont notamment :

1. un premier temps singulier possible `T*` et l'intervalle `I=(T*−ε,T*)` ;
2. un profil ponctuel critique centré à l'origine, `ω(x,t)=Φ(x,t)|x|⁻²`, avec les contraintes supplémentaires de la définition 2.1 ;
3. le confinement `A_λ(t)⊂B_{Cλ^{-1/2}}` des hauts superniveaux ;
4. `ω∈L∞(I;L^{3/2,∞}(R³))`, de borne notée `M₀` ;
5. `ξ∈L∞(I;bmo_{1/|log r|}(R³))` ;
6. une solution unique et spatialement analytique sur `(0,T*)`.

Il ne s'agit donc pas d'un théorème de régularité globale pour toutes les données Clay : c'est un critère conditionnel pour une classe de scénarios ponctuels critiques assortis d'une hypothèse géométrique sur la direction de vorticité.

## Transcription fidèle des équations (20)–(40)

La transcription ci-dessous suit le [texte primaire v2, sections 4 et 5](https://arxiv.org/html/2607.08866v2). Les notations typographiques ont été normalisées en LaTeX sans modifier le contenu mathématique.

### Fin de l'estimation dyadique du commutateur

\[
|I_{2,mid}(x)|\lesssim\frac{1}{R^{2}}
\sum_{j=1}^{N+1}\phi(2^{j}R)
\sum_{k=\max(1,j-1)}^{N}4^{-k}
\approx\frac{1}{R^{2}}
\sum_{j=1}^{N+1}4^{-j}\phi(2^{j}R).
\tag{20}
\]

\[
|I_{2,mid}(x)|\leq\frac{C}{R^{2}}2\phi(R)
\sum_{j=1}^{\infty}4^{-j}
=C\frac{\phi(R)}{R^{2}}.
\tag{21}
\]

\[
\begin{aligned}
\|\alpha(\cdot,t)\|_{L^{3/2,\infty}(B_R)}
&\leq
\|[\mathcal T,\boldsymbol\xi](\omega_{in})\|_{L^{3/2,\infty}(B_R)}
+\|I_1\|_{L^{3/2,\infty}(B_R)}
+\|I_2\|_{L^{3/2,\infty}(B_R)}\\
&\leq\frac{C_0}{|\log R|}.
\end{aligned}
\tag{22}
\]

Ici `φ(r)=1/|log r|`, `N=⌊(1/2)log₂(1/R)⌋`, et le texte entend les estimations uniformément pour `t∈I` et `R` suffisamment petit.

### Troncation et absorption

Le manuscrit définit

\[
A_\lambda(t)=\{x\in\mathbb R^3:\omega(x,t)>\lambda\},
\qquad
U_\lambda(t)=|A_\lambda(t)|,
\qquad
\omega_\lambda=(\omega-\lambda)_+.
\]

\[
\frac12\frac d{dt}\|\omega_\lambda\|_2^2
+\nu\|\nabla\omega_\lambda\|_2^2
\leq
\underbrace{\int_{A_\lambda(t)}\alpha\omega_\lambda^2\,dx}_{\text{Nonlinear Stretching}}
+\underbrace{\lambda\int_{A_\lambda(t)}\alpha\omega_\lambda\,dx}_{\text{Linear Source}}.
\tag{23}
\]

\[
\begin{aligned}
\int_{A_\lambda(t)}\alpha\omega_\lambda^2\,dx
&\leq
\|\alpha(\cdot,t)\|_{L^{3/2,\infty}(A_\lambda(t))}
\|\omega_\lambda^2\|_{L^{3,1}}\\
&=
\|\alpha(\cdot,t)\|_{L^{3/2,\infty}(A_\lambda(t))}
\|\omega_\lambda\|_{L^{6,2}}^2.
\end{aligned}
\tag{24}
\]

\[
\|\alpha(\cdot,t)\|_{L^{3/2,\infty}(A_\lambda(t))}
\leq
\|\alpha(\cdot,t)\|_{L^{3/2,\infty}(B_{C\lambda^{-1/2}})}
\leq
\frac{C_0}{|\log(C\lambda^{-1/2})|}
\approx\frac{2C_0}{\log\lambda}.
\tag{25}
\]

Après l'affichage (25), le texte choisit `λ₀` de sorte que

\[
C_S^2\|\alpha(\cdot,t)\|_{L^{3/2,\infty}(A_\lambda(t))}
\leq\frac\nu2
\]

pour `λ≥λ₀`, puis affiche

\[
\frac12\frac d{dt}\|\omega_\lambda\|_2^2
+\frac\nu2\|\nabla\omega_\lambda\|_2^2
\leq
\lambda\int_{A_\lambda(t)}\alpha\omega_\lambda\,dx.
\tag{26}
\]

### Interpolation du terme source

\[
\lambda\int_{A_\lambda(t)}\alpha\omega_\lambda\,dx
\leq
\lambda\|\alpha(\cdot,t)\|_{L^{3/2,\infty}(A_\lambda(t))}
\|\omega_\lambda\|_{L^{3,1}}.
\tag{27}
\]

\[
\|\omega_\lambda\|_{L^{3,1}}
\leq
C_I\|\omega_\lambda\|_{L^{3/2,\infty}}^{1/3}
\|\omega_\lambda\|_{L^{6,2}}^{2/3}.
\tag{28}
\]

\[
\|\omega_\lambda\|_{L^{3,1}}
\leq
C_I M_0^{1/3}
\left(C_S\|\nabla\omega_\lambda\|_2\right)^{2/3}.
\tag{29}
\]

\[
\lambda\int_{A_\lambda(t)}\alpha\omega_\lambda\,dx
\leq
\lambda\left[\frac{2C_0}{\log\lambda}\right]
\left(C_I M_0^{1/3}C_S^{2/3}
\|\nabla\omega_\lambda\|_2^{2/3}\right).
\tag{30}
\]

\[
\begin{aligned}
\lambda\int_{A_\lambda(t)}\alpha\omega_\lambda\,dx
&\leq
\frac\nu4\|\nabla\omega_\lambda\|_2^2
+\frac{C_1}{\nu^{1/2}}
\left(\frac{\lambda}{\log\lambda}M_0^{1/3}\right)^{3/2}\\
&=
\frac\nu4\|\nabla\omega_\lambda\|_2^2
+\frac{C_1M_0^{1/2}}{\nu^{1/2}}
\frac{\lambda^{3/2}}{(\log\lambda)^{3/2}}.
\end{aligned}
\tag{31}
\]

\[
\frac12\frac d{dt}E_\lambda(t)
+\frac\nu4\|\nabla\omega_\lambda\|_2^2
\leq
\frac{C_1M_0^{1/2}}{\nu^{1/2}}
\frac{\lambda^{3/2}}{(\log\lambda)^{3/2}},
\qquad
E_\lambda(t)=\|\omega_\lambda(\cdot,t)\|_2^2.
\tag{32}
\]

### Sobolev sur le support, amortissement et distribution

\[
E_\lambda(t)=\|\omega_\lambda\|_2^2
\leq
\|\omega_\lambda\|_6^2|A_\lambda(t)|^{2/3}
\leq
C_S^2\|\nabla\omega_\lambda\|_2^2U_\lambda(t)^{2/3}.
\tag{33}
\]

Le texte utilise ensuite

\[
U_\lambda(t)\leq M_0^{3/2}\lambda^{-3/2},
\qquad
U_\lambda(t)^{2/3}\leq M_0\lambda^{-1},
\]

ce qui donne

\[
\|\nabla\omega_\lambda\|_2^2
\geq
\frac{\lambda}{C_S^2M_0}E_\lambda(t).
\tag{34}
\]

\[
\frac d{dt}E_\lambda(t)
+\left(\frac{\nu}{2C_S^2M_0}\right)\lambda E_\lambda(t)
\leq
\frac{2C_1M_0^{1/2}}{\nu^{1/2}}
\frac{\lambda^{3/2}}{(\log\lambda)^{3/2}}.
\tag{35}
\]

Avec `μ=ν/(2C_S²M₀)`, `K(λ)` égal au membre droit de (35), `t₀=T*−ε`, et `λ≥Λ₀=||ω(·,t₀)||∞`, le texte obtient

\[
\begin{aligned}
E_\lambda(t)
&\leq
\int_{t_0}^t e^{-\mu\lambda(t-\tau)}K(\lambda)\,d\tau\\
&=
\frac{K(\lambda)}{\mu\lambda}
\left(1-e^{-\mu\lambda(t-t_0)}\right)
\leq
\frac{K(\lambda)}{\mu\lambda}.
\end{aligned}
\tag{36}
\]

\[
E_\lambda(t)
\leq
\frac{4C_1C_S^2M_0^{3/2}}{\nu^{3/2}}
\frac{\lambda^{1/2}}{(\log\lambda)^{3/2}}.
\tag{37}
\]

\[
U_{2\lambda}(t)=|A_{2\lambda}(t)|
\leq
\frac1{\lambda^2}
\int_{A_{2\lambda}(t)}\omega_\lambda^2\,dx
\leq
\frac1{\lambda^2}E_\lambda(t).
\tag{38}
\]

\[
U_{2\lambda}(t)
\leq
\frac1{\lambda^2}
\left[C_2\frac{\lambda^{1/2}}{(\log\lambda)^{3/2}}\right]
=
\frac{C_2}{\lambda^{3/2}(\log\lambda)^{3/2}}.
\tag{39}
\]

\[
\sup_{t\in(T^*-\epsilon,T^*)}
|\{x\in\mathbb R^3:\omega(x,t)>\lambda\}|
\leq
\frac{C_\omega}{\lambda^{3/2}(\log\lambda)^{\gamma_1}},
\qquad
\gamma_1=\frac32.
\tag{40}
\]

## Sources primaires des outils fonctionnels

### Hölder et interpolation dans les espaces de Lorentz

Le manuscrit cite à juste titre Richard A. Hunt pour le Hölder lorentzien utilisé dans (24) et (27) :

- Richard A. Hunt, “On `L(p,q)` spaces”, *L'Enseignement Mathématique* **12** (1966), 249–276, [archive primaire E-Periodica](https://www.e-periodica.ch/digbib/view?lang=en&pid=ens-001%3A1966%3A12%3A%3A408). Aucun DOI n'a été localisé dans la notice primaire consultée.

L'identité de norme dans (24) est exacte avec la convention de réarrangement affichée par le manuscrit : puisque `(f²)*(s)=(f*(s))²`,

\[
\|f^2\|_{L^{3,1}}
=\int_0^\infty s^{1/3}(f^*(s))^2\frac{ds}{s}
=\|f\|_{L^{6,2}}^2.
\]

Pour l'interpolation réelle de (28) et le raffinement Sobolev–Lorentz de (24), une source primaire adaptée est :

- Jaak Peetre, “Espaces d'interpolation et théorème de Soboleff”, *Annales de l'Institut Fourier* **16**(1) (1966), 279–317, DOI [10.5802/aif.232](https://doi.org/10.5802/aif.232), [notice et texte de l'éditeur](https://aif.centre-mersenne.org/articles/10.5802/aif.232/).

Cette filiation couvre les plongements Sobolev raffinés dans l'échelle de Lorentz et les identités d'interpolation. Les constantes `C_I` et `C_S` dépendent néanmoins de la convention précise de quasi-norme ; le manuscrit ne les normalise pas au-delà de sa définition (1).

### Sobolev/Poincaré sur les superniveaux

Le maillon (33) se décompose exactement en deux inégalités : pour une fonction `f` supportée dans un ensemble mesurable `A` de mesure finie,

\[
\|f\|_2^2
\leq
\|f\|_6^2|A|^{2/3}
\]

par Hölder, puis

\[
\|f\|_6\leq C_S\|\nabla f\|_2
\]

par Sobolev homogène sur `R³`. Une source primaire du résultat de Sobolev avec constante optimale est :

- Giorgio Talenti, “Best constant in Sobolev inequality”, *Annali di Matematica Pura ed Applicata* **110** (1976), 353–372, DOI [10.1007/BF02418013](https://doi.org/10.1007/BF02418013).

Avec `f=ω_λ` et `supp f⊂A_λ(t)`, on obtient directement

\[
\|f\|_2^2
\leq
C_S^2|A_\lambda(t)|^{2/3}\|\nabla f\|_2^2.
\]

Cette forme est parfois appelée inégalité de Poincaré–Sobolev « sur le support ». Elle ne dépend ni de la connexité, ni de la régularité de la frontière, ni du diamètre de `A_λ(t)`. Il n'est donc pas nécessaire d'invoquer une inégalité de Poincaré sur un domaine mobile. Une formulation spectrale de type Faber–Krahn fournirait une autre route et une constante de même échelle, mais ce n'est pas la dérivation écrite en (33).

Le point fonctionnel à documenter dans une preuve complète est que `ω_λ` appartient bien à `\dot H^1(R³)` et possède un support de mesure finie. La borne faible `L^{3/2}` donne la seconde propriété. La première est plausible pour la solution analytique classique considérée à chaque temps `t<T*`, mais elle devrait être raccordée explicitement à une régularisation et à un passage à la limite si le raisonnement était transféré à une notion de solution plus faible.

### Étape dite de De Giorgi

La source originelle de la méthode est :

- Ennio De Giorgi, “Sulla differenziabilità e l'analiticità delle estremali degli integrali multipli regolari”, *Memorie dell'Accademia delle Scienze di Torino, Classe di Scienze Fisiche, Matematiche e Naturali*, série 3, **3** (1957), 25–43 ; [notice et reproduction MathNet](https://www.mathnet.ru/eng/mat161), MR0093649.

Une source primaire directement liée aux Navier–Stokes incompressibles et utilisant une véritable méthode de De Giorgi est :

- Alexis F. Vasseur, “A new proof of partial regularity of solutions to Navier-Stokes equations”, *NoDEA — Nonlinear Differential Equations and Applications* **14** (2007), 753–785, DOI [10.1007/s00030-007-6001-4](https://doi.org/10.1007/s00030-007-6001-4), [PDF de l'auteur](https://web.ma.utexas.edu/users/vasseur/documents/preprints/NS2.pdf).

La comparaison doit rester précise : Vasseur travaille avec des solutions faibles adaptées, la pression et des cylindres espace-temps pour obtenir de la régularité partielle. Cette référence établit la lignée Navier–Stokes de la méthode, mais ne justifie pas automatiquement le test scalaire de vorticité ni les hypothèses ponctuelles du manuscrit de Grujić.

Dans `arXiv:2607.08866v2`, l'étape effectivement exécutée est seulement :

1. multiplier l'inégalité scalaire de la magnitude par `(ω−λ)+` ;
2. intégrer sur `R³`, en annulant le transport par `div u=0` ;
3. absorber un terme avec Sobolev–Lorentz ;
4. interpoler le terme source ;
5. résoudre un ODE à `λ` fixé ;
6. appliquer Tchebychev au niveau `2λ`.

Une justification classique de (23) pour une solution lisse passe par une approximation convexe de \(|\boldsymbol\omega|\) au voisinage de ses zéros et de la fonction positive, éventuellement assortie de coupures spatiales avant le passage à `R³`. Le manuscrit ne fournit ni cette approximation, ni une référence spécifique. Sa régularité analytique rend le maillon vraisemblablement réparable, mais cette réparation n'est pas écrite et ne peut pas être transférée telle quelle aux solutions de Leray–Hopf ou faibles adaptées.

## Audit local, équation par équation

| Passage | Verdict local | Condition ou correction nécessaire |
|---|---|---|
| (20) | Réarrangement des séries correct à constantes multiplicatives près. | `≈` masque le facteur provenant de `Σ_{k≥j−1}4^{-k}` et les effets du dernier indice. |
| (21) | Échelle `R⁻²φ(R)` correcte. | Avec `N=⌊(1/2)log₂(1/R)⌋`, on a seulement `2^{N+1}R≤2R^{1/2}`. L'identité affichée `φ(2^jR)≤φ(R^{1/2})=2φ(R)` n'est pas littéralement vraie au dernier indice pour tout `R`; une constante uniforme un peu plus grande et un seuil `R≤R₀` réparent le passage. |
| (22) | Conclusion formelle compatible avec les trois morceaux précédents. | Non validée ici, car les estimations de commutateur (8)–(19) ne font pas partie du présent périmètre. |
| (23) | Calcul formel correct pour une solution classique suffisamment décroissante. | Il faut régulariser la norme de la vorticité vectorielle et `(·)+`, ou citer un lemme de troncation/Kato, puis contrôler les coupures à l'infini. |
| (24) | Hölder lorentzien et identité quadratique corrects avec la convention du papier. | Le membre de droite doit être compris avec `|α|`; la notation de l'intégrale non signée le masque. |
| (25) | Asymptotique logarithmique correcte lorsque `λ` est assez grand. | Remplacer `≈` par une inégalité explicite après un seuil dépendant de `C`; le résultat du théorème 4.1 vaut seulement sur `I`. |
| (26) | Absorption correcte sur l'intervalle où (25) est disponible. | `λ₀` n'est pas « absolu » : il dépend au moins de `ν`, `C₀`, `C_S` et du seuil géométrique. Remplacer `(0,T*)` par `I`. |
| (27)–(29) | Exposants corrects : `(L^{3/2,∞},L^{6,2})_{2/3,1}=L^{3,1}`. | Les constantes dépendent des conventions de quasi-norme ; `ω_λ∈dot H¹` doit être explicité. |
| (30)–(32) | Young avec exposants `3` et `3/2` donne bien `ν^{-1/2}λ^{3/2}(log λ)^{-3/2}`. | Les facteurs `2C₀`, `C_I`, `C_S` sont absorbés dans `C₁`; il faut le déclarer et garder `λ` au-dessus de tous les seuils. |
| (33)–(34) | Correct : Hölder sur le support + Sobolev + définition du faible `L^{3/2}`. | Ce n'est pas une Poincaré de domaine. La notation `M₀` est une norme, d'où `U_λ≤(M₀/λ)^{3/2}`. |
| (35)–(37) | Coefficient d'amortissement et rapport stationnaire recalculés correctement. | La validité uniforme porte sur `I`; `λ≥Λ₀=||ω(t₀)||∞` est requis pour `E_λ(t₀)=0`. |
| (38)–(39) | Tchebychev correct sur `A_{2λ}` car `ω_λ>λ`. | La borne vaut seulement dans le régime de haute troncature. |
| (39) → (40) | Exposant `γ₁=3/2` préservé. | Le changement `2λ↦λ` produit `log(λ/2)` et un facteur `2^{3/2}`. Pour écrire `log λ`, il faut fixer `λ≥λ_*` et absorber une constante de comparaison. |

## Recalculs adversariaux ciblés

### Young dans (31)

Posons

\[
A=\lambda\frac{2C_0}{\log\lambda}
C_IM_0^{1/3}C_S^{2/3},
\qquad
X=\|\nabla\omega_\lambda\|_2.
\]

Le terme est `AX^{2/3}`. Young avec les conjugués `3` et `3/2`, après insertion d'un paramètre proportionnel à `ν`, donne

\[
AX^{2/3}
\leq\frac\nu4X^2+C\nu^{-1/2}A^{3/2}.
\]

Comme `A^{3/2}` contient `M₀^{1/2}λ^{3/2}(log λ)^{-3/2}`, les puissances de (31) sont confirmées.

### Passage (32) → (35)

En multipliant (32) par deux puis en injectant (34),

\[
E_\lambda'
+\frac\nu2\frac{\lambda}{C_S^2M_0}E_\lambda
\leq
\frac{2C_1M_0^{1/2}}{\nu^{1/2}}
\frac{\lambda^{3/2}}{(\log\lambda)^{3/2}},
\]

ce qui reproduit exactement (35).

### Rapport stationnaire dans (37)

Avec

\[
\mu\lambda=\frac{\nu\lambda}{2C_S^2M_0},
\qquad
K(\lambda)=
\frac{2C_1M_0^{1/2}}{\nu^{1/2}}
\frac{\lambda^{3/2}}{(\log\lambda)^{3/2}},
\]

on trouve

\[
\frac{K(\lambda)}{\mu\lambda}
=
\frac{4C_1C_S^2M_0^{3/2}}{\nu^{3/2}}
\frac{\lambda^{1/2}}{(\log\lambda)^{3/2}},
\]

donc la constante et les puissances de (37) sont correctes.

## Implication exacte et limites pour le problème Clay

Sous l'acceptation provisoire du théorème de commutateur 4.1 et des hypothèses du profil ponctuel critique, les équations (23)–(40) établissent un gain logarithmique dans la fonction de distribution de la magnitude de vorticité sur l'intervalle terminal :

\[
U_\lambda(t)
\lesssim
\lambda^{-3/2}(\log\lambda)^{-3/2}
\quad
\text{pour }\lambda\geq\lambda_*.
\]

Ce maillon est conditionnel et ne résout pas le problème Clay, pour quatre raisons indépendantes :

1. le profil ponctuel `Φ(x,t)|x|⁻²` avec confinement uniforme des superniveaux est une hypothèse supplémentaire forte ;
2. la borne géométrique `ξ∈bmo_{1/|log r|}` n'est pas connue pour toutes les données Clay ;
3. le théorème de commutateur fournissant (22) n'est pas validé par la présente passe ;
4. le gain de distribution (40) doit encore être transféré à la vitesse puis raccordé sans perte à un critère de régularité, étapes hors périmètre ici et déjà signalées comme nécessitant leurs propres audits.

La conclusion scientifiquement défendable de ce cycle est donc locale : **le bloc d'énergie (23)–(39) est algébriquement cohérent et réparable avec des seuils explicites, mais il est improprement décrit comme une itération de De Giorgi complète et son domaine temporel a été élargi sans justification dans la phrase qui suit (25).**

## Limite d'indépendance de cette revue

Cette passe a été produite par un agent utilisant la même famille de modèle, le même dépôt et une partie du même contexte que la dérivation principale. Elle réduit le risque d'erreurs de transcription, de source et d'algèbre, mais pas les erreurs corrélées d'interprétation. Elle ne doit recevoir ni le statut `INDEPENDENT_REVIEW` ni celui de validation par un expert extérieur. Une revue réellement indépendante devrait au minimum :

- repartir du PDF/TeX v2 sans utiliser les analyses de cycles précédents ;
- vérifier les hypothèses exactes de `dot H¹` et le passage aux coupures dans (23) ;
- auditer séparément le théorème 4.1, notamment les termes non locaux et les constantes de localisation ;
- vérifier le transfert après (40) et l'endgame de mesure harmonique ;
- confirmer auprès d'une source extérieure la convention des normes de Lorentz et les constantes utilisées.

## Empreinte de la veille

Ressources primaires consultées le 14 août 2026 :

- `https://arxiv.org/abs/2607.08866`
- `https://arxiv.org/html/2607.08866v2`
- `https://doi.org/10.48550/arXiv.2607.08866`
- `https://www.e-periodica.ch/digbib/view?lang=en&pid=ens-001%3A1966%3A12%3A%3A408`
- `https://aif.centre-mersenne.org/articles/10.5802/aif.232/`
- `https://doi.org/10.1007/BF02418013`
- `https://www.mathnet.ru/eng/mat161`
- `https://web.ma.utexas.edu/users/vasseur/documents/preprints/NS2.pdf`
- `https://doi.org/10.1007/s00030-007-6001-4`

**État de la passe :** résultat négatif partiel sur la qualification « De Giorgi » et sur deux quantificateurs ; confirmation conditionnelle de l'algèbre (23)–(39). À reprendre par une revue indépendante après toute nouvelle version arXiv.
