# Analyse PDE indépendante — cycle 0021 : admissibilité d’un profil ponctuel critique de vorticité

Date de vérification primaire : 2026-08-14

Statut : dérivation interne non publiée; revue séparée mais produite par la même famille de modèle que l’agent principal

## Verdict exécutif

La définition 2.1 de [Grujić, arXiv:2607.08866v2](https://arxiv.org/html/2607.08866v2) décrit une **magnitude scalaire** critique,

\[
\omega(x,t)=\Phi(x,t)|x|^{-2},
\tag{1}
\]

avec un facteur de forme borné, invariant d’échelle ou log-périodique au cœur, et `|∇Φ|≲|x|^{-1}`. Elle ne constitue pas à elle seule un champ de vorticité vectoriel admissible. Pour qu’une interprétation

\[
\boldsymbol\omega(x)=|x|^{-2}\Omega(x/|x|)
\tag{2}
\]

soit le curl d’une vitesse incompressible globale, deux conditions angulaires indépendantes sont nécessaires et, sous une régularité élémentaire, suffisantes :

\[
\operatorname{div}_{S^2}\Omega_T=0,
\qquad
\int_{S^2}\Omega_r\,dS=0,
\tag{3}
\]

où `Ω_r=Ω·θ` et `Ω_T=Ω-Ω_rθ`. La première annule la divergence sur `R³\{0}`; la seconde annule le monopôle de divergence à l’origine.

Deux contre-profils séparent exactement ces verrous :

1. `ω=e/|x|²`, de direction constante et donc de semi-norme `bmo_φ` nulle, vérifie
   \[
   \operatorname{div}\boldsymbol\omega
   =-2\frac{e\cdot\theta}{r^3}\neq0
   \quad (r>0);
   \tag{4}
   \]
2. `ω=θ/|x|²` est divergence-free hors de l’origine, mais
   \[
   \operatorname{div}\boldsymbol\omega=4\pi\delta_0.
   \tag{5}
   \]

Aucun de ces deux champs n’est le curl distributionnel d’une vitesse globale. Le gabarit scalaire critique, même joint à une direction parfaitement cohérente dans le premier exemple, n’implique donc pas l’admissibilité cinématique.

Le second résultat exact du cycle concerne les coupures. Si `χ(r)` est radiale et si le profil (2) satisfait (3), alors

\[
\operatorname{div}(\chi\boldsymbol\omega)
=\chi'(r)r^{-2}\Omega_r(\theta).
\tag{6}
\]

Pour une transition monotone complète, le défaut a la norme exacte

\[
\|\operatorname{div}(\chi\boldsymbol\omega)\|_{L^1(\mathbb R^3)}
=\|\Omega_r\|_{L^1(S^2)},
\tag{7}
\]

indépendamment de l’échelle de coupure. Une troncature radiale naïve ne préserve donc la contrainte de vorticité que si `Ω_r=0`. Une correction solénoïdale explicite existe lorsque le flux est nul, mais elle est de même ordre critique que le profil et ne disparaît pas quand la coupure se resserre.

## 1. Formulation primaire auditée

La version primaire consultée est la v2 du 13 juillet 2026 de *Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier–Stokes Equations*. Sa définition 2.1 :

- appelle « singularité ponctuelle critique » une magnitude de vorticité localement d’ordre `|x|^{-2}`;
- factorise cette magnitude sous la forme (1);
- donne comme exemples un facteur purement angulaire `Φ=U(x/|x|)` et un facteur radial log-périodique tel que `2+sin(log(1/|x|))`;
- suppose `Φ` uniformément borné et `|∇Φ|≲|x|^{-1}`;
- en déduit l’inclusion des grands superniveaux dans une boule de rayon `O(λ^{-1/2})`.

La notation de la définition et son superniveau `{ω>λ}` sont scalaires. La direction `ξ=boldsymbolω/|boldsymbolω|` intervient ailleurs dans le manuscrit. Pour raccorder la définition à Navier–Stokes incompressible, il faut donc ajouter explicitement au moins :

\[
\boldsymbol\omega=\nabla\times u,
\qquad
\nabla\cdot u=0,
\qquad
\nabla\cdot\boldsymbol\omega=0
\tag{8}
\]

au sens de distributions approprié. Le présent rapport analyse ce raccord cinématique; il ne valide pas l’existence dynamique d’un tel profil dans une solution de Navier–Stokes.

## 2. Lemme minimal d’admissibilité angulaire

### Lemme 2.1 — porte solénoïdale exacte

Soit `Ω∈C¹(S²;R³)` et définissons sur `R³\{0}`

\[
W(x)=r^{-2}\Omega(\theta),
\qquad r=|x|,
\qquad \theta=x/r.
\tag{9}
\]

Décomposons

\[
\Omega=\Omega_r\theta+\Omega_T,
\qquad
\Omega_r=\Omega\cdot\theta,
\qquad
\Omega_T\cdot\theta=0.
\tag{10}
\]

Alors :

1. `div W=0` sur `R³\{0}` si et seulement si
   \[
   \operatorname{div}_{S^2}\Omega_T=0;
   \tag{11}
   \]
2. sous (11), la divergence distributionnelle sur tout `R³` est
   \[
   \operatorname{div}W
   =F\delta_0,
   \qquad
   F:=\int_{S^2}\Omega_r(\theta)\,dS(\theta);
   \tag{12}
   \]
3. par conséquent, `W` est divergence-free dans `D'(R³)` si et seulement si les deux conditions (3) sont satisfaites.

Ces conditions sont nécessaires pour toute représentation `W=curl u`, puisque `div curl u=0` dans les distributions.

### Preuve et constante du monopôle

La formule de divergence sphérique donne, pour `r>0`,

\[
\begin{aligned}
\operatorname{div}W
&=\frac1{r^2}\partial_r(r^2W_r)
  +\frac1r\operatorname{div}_{S^2}W_T\\
&=r^{-3}\operatorname{div}_{S^2}\Omega_T.
\end{aligned}
\tag{13}
\]

Le champ `W` est localement intégrable à l’origine car

\[
\int_{B_R}|W|\,dx
=R\int_{S^2}|\Omega|\,dS.
\tag{14}
\]

Sous (11), testons sa divergence contre `ψ∈C_c^∞(R³)` et retirons `B_ε`. Le bord intérieur de `R³\setminus B_ε` a pour normale `-θ`, d’où

\[
\begin{aligned}
\langle\operatorname{div}W,\psi\rangle
&=-\lim_{\epsilon\downarrow0}
  \int_{|x|>\epsilon}W\cdot\nabla\psi\,dx\\
&=\lim_{\epsilon\downarrow0}
  \int_{S^2}\psi(\epsilon\theta)\Omega_r(\theta)\,dS\\
&=F\psi(0).
\end{aligned}
\tag{15}
\]

Le coefficient de `δ₀` est donc exactement le flux sphérique `F`, sans facteur caché. Pour `Ω=θ`, `F=|S²|=4π`, ce qui donne (5).

### Dictionnaire magnitude–direction

Si l’on veut interpréter le facteur scalaire primaire comme `|W|=r^{-2}Φ(θ)` et écrire

\[
\Omega(\theta)=\Phi(\theta)\xi(\theta),
\qquad |\xi|=1,
\tag{16}
\]

les contraintes manquantes deviennent

\[
\operatorname{div}_{S^2}
\left[(I-\theta\otimes\theta)\Phi\xi\right]=0,
\qquad
\int_{S^2}\Phi(\xi\cdot\theta)\,dS=0.
\tag{17}
\]

Elles couplent la magnitude et la direction. Une borne sur `Φ`, sur `∇Φ`, ou sur l’oscillation moyenne de `ξ` ne les implique pas séparément.

## 3. Existence de la vitesse par Biot–Savart

### Proposition 3.1 — reconstruction canonique

Sous les hypothèses du lemme 2.1 et les conditions (3), définissons, pour `x≠0`,

\[
u(x)=\frac1{4\pi}
\int_{\mathbb R^3}
W(y)\times\frac{x-y}{|x-y|^3}\,dy.
\tag{18}
\]

L’intégrale est absolument convergente :

- près de `y=0`, `|W(y)|=O(|y|^{-2})` est intégrable et le noyau est borné pour `x≠0`;
- près de `y=x`, le noyau `|x-y|^{-2}` est localement intégrable en dimension trois;
- à l’infini, le produit est `O(|y|^{-4})`.

La vitesse ainsi définie vérifie

\[
\nabla\cdot u=0,
\qquad
\nabla\times u=W
\quad\text{dans }\mathcal D'(\mathbb R^3),
\tag{19}
\]

et elle est homogène de degré `-1` :

\[
u(\lambda x)=\lambda^{-1}u(x).
\tag{20}
\]

Réciproquement, l’existence d’une vitesse distributionnelle dont le curl vaut `W` force (3).

### Borne ponctuelle avec constante

Avec `M=||Ω||_{L∞(S²)}`, on a

\[
|W(y)|\leq M|y|^{-2}.
\]

L’identité de convolution de Riesz

\[
\int_{\mathbb R^3}
\frac{dy}{|y|^2|x-y|^2}
=\frac{\pi^3}{|x|}
\tag{21}
\]

donne la borne sûre explicite

\[
|u(x)|\leq\frac{\pi^2}{4}\frac{M}{|x|}.
\tag{22}
\]

Cette constante provient d’une majoration en valeur absolue; elle n’est pas annoncée optimale pour le sous-espace solénoïdal.

### Exemple admissible explicite

Pour un vecteur constant `a`, posons

\[
\Omega(\theta)=a\times\theta,
\qquad
W(x)=\frac{a\times\theta}{r^2}.
\tag{23}
\]

Ce profil est tangent, de divergence sphérique nulle et de flux nul. Une vitesse incompressible explicite est

\[
u(x)=\frac1{2r}
\left[a+(a\cdot\theta)\theta\right].
\tag{24}
\]

En effet, `curl(a/r)=W`, tandis que l’ajout du gradient

\[
\nabla\left[-\frac12(a\cdot\theta)\right]
\]

annule la divergence sans changer le curl. Cet exemple montre que les contraintes (3) ne sont pas vides.

## 4. Scaling et espaces critiques

Sous le scaling de Navier–Stokes

\[
u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),
\qquad
W_\lambda(x,t)=\lambda^2W(\lambda x,\lambda^2t),
\tag{25}
\]

les profils exactement homogènes (9) et (20) sont invariants à temps fixé. Ils se trouvent aux exposants critiques attendus : `W∈L^{3/2,∞}` et `u∈L^{3,∞}`.

Pour le profil global (9), la fonction de distribution se calcule exactement :

\[
\left|\{x:|W(x)|>\lambda\}\right|
=\frac1{3\lambda^{3/2}}
\int_{S^2}|\Omega|^{3/2}\,dS.
\tag{26}
\]

Avec la convention

\[
\|f\|_{L^{p,\infty}}
=\sup_{\lambda>0}\lambda
|\{|f|>\lambda\}|^{1/p},
\]

on obtient

\[
\|W\|_{L^{3/2,\infty}}
=3^{-2/3}
\left(\int_{S^2}|\Omega|^{3/2}\,dS\right)^{2/3}.
\tag{27}
\]

Si `u=r^{-1}U(θ)`, le même calcul donne

\[
\|u\|_{L^{3,\infty}}
=3^{-1/3}\|U\|_{L^3(S^2)}.
\tag{28}
\]

Ces identités confirment la criticalité; elles ne disent pas que le profil satisfait l’équation d’évolution.

## 5. Énergie locale, énergie globale et enstrophie

Pour toute vitesse homogène `u=r^{-1}U(θ)`, on a l’identité exacte de coquille

\[
\int_{a<|x|<b}|u(x)|^2\,dx
=(b-a)\int_{S^2}|U|^2\,dS.
\tag{29}
\]

Ainsi :

- l’énergie locale près de l’origine est finie et
  \[
  \int_{B_R}|u|^2dx
  =R\|U\|_{L^2(S^2)}^2\longrightarrow0
  \quad(R\downarrow0);
  \tag{30}
  \]
- l’énergie globale diverge linéairement à l’infini dès que `U≠0`;
- le profil homogène sur toutes les échelles n’est donc pas une vitesse de donnée Clay à énergie finie.

La borne (22) fournit notamment

\[
\int_{B_R}|u|^2dx
\leq\frac{\pi^5}{4}M^2R.
\tag{31}
\]

Pour l’exemple (24), la constante exacte est

\[
\int_{S^2}|U|^2dS=2\pi|a|^2,
\qquad
\int_{B_R}|u|^2dx=2\pi|a|^2R.
\tag{32}
\]

La vorticité n’a, elle, aucune enstrophie locale finie à l’origine :

\[
\int_{\epsilon<|x|<R}|W|^2dx
=\|\Omega\|_{L^2(S^2)}^2
\left(\frac1\epsilon-\frac1R\right).
\tag{33}
\]

Sa norme forte critique diverge seulement logarithmiquement entre deux coupures :

\[
\int_{\epsilon<|x|<R}|W|^{3/2}dx
=\|\Omega\|_{L^{3/2}(S^2)}^{3/2}
\log\frac R\epsilon.
\tag{34}
\]

Le profil exact à l’origine ne peut donc représenter un temps régulier antérieur au blow-up. À un temps isolé, la singularité `u∼r^{-1}` reste compatible avec l’énergie spatiale locale; son admissibilité dans une solution faible adaptée dépend en outre de l’intégrabilité espace-temps et de la pression, que (1) ne précise pas.

## 6. Flux et circulation

Le flux de la vorticité à travers toute sphère centrée est indépendant du rayon :

\[
\int_{|x|=r}W\cdot n\,dS
=\int_{S^2}\Omega_r\,dS=F.
\tag{35}
\]

Pour un curl global, ce flux doit être nul. C’est exactement la seconde condition de (3), et non une conséquence de la seule décroissance `r^{-2}`.

Plus localement, soit `A⊂S²` un domaine régulier et `rA` la calotte correspondante sur la sphère de rayon `r`. Stokes donne

\[
\oint_{\partial(rA)}u\cdot d\ell
=\int_A\Omega_r\,dS.
\tag{36}
\]

Les deux membres sont invariants par changement de rayon : `u` croît comme `r^{-1}` et la longueur du lacet comme `r`, tandis que `W` croît comme `r^{-2}` et l’aire comme `r²`. Toute prétendue convergence vers un profil critique doit donc préserver ces circulations sans créer de monopôle caché au point central.

## 7. Coupures radiales : défaut exact et réparation

### Lemme 7.1 — défaut de divergence invariant d’échelle

Supposons (3), et soit `χ∈C¹((0,∞))` radiale. Alors

\[
\operatorname{div}(\chi(r)W)
=\nabla\chi\cdot W
=\chi'(r)r^{-2}\Omega_r(\theta).
\tag{37}
\]

Par intégration sphérique,

\[
\|\operatorname{div}(\chi W)\|_{L^1}
=\left(\int_0^\infty|\chi'(r)|dr\right)
\|\Omega_r\|_{L^1(S^2)}.
\tag{38}
\]

Pour une coupure monotone passant de zéro à un, ou de un à zéro, `∫|χ'|=1`, ce qui prouve (7). Pour une double coupure intérieure/extérieure à supports de transition disjoints, toutes deux monotones et complètes,

\[
\|\operatorname{div}(\chi_{\epsilon,R}W)\|_{L^1}
=2\|\Omega_r\|_{L^1(S^2)}.
\tag{39}
\]

Le défaut ne tend ni vers zéro quand `ε↓0`, ni vers zéro quand `R↑∞`. Une multiplication radiale brute est exacte uniquement pour les profils tangentiels `Ω_r=0`.

### Réparation solénoïdale explicite

La condition de flux nul permet de résoudre sur la sphère

\[
\Delta_{S^2}\psi=\Omega_r,
\qquad
\int_{S^2}\psi\,dS=0,
\qquad
V=\nabla_{S^2}\psi.
\tag{40}
\]

Alors `div_S V=Ω_r`. La coupure corrigée

\[
W^\chi
=\chi(r)W
-\frac{\chi'(r)}rV(\theta)
\tag{41}
\]

vérifie exactement

\[
\operatorname{div}W^\chi=0.
\tag{42}
\]

Avec la convention `Δ_S Y_{\ell m}=-\ell(\ell+1)Y_{\ell m}`, le gap spectral de la sphère donne la constante optimale

\[
\|V\|_{L^2(S^2)}
\leq\frac1{\sqrt2}\|\Omega_r\|_{L^2(S^2)},
\tag{43}
\]

atteinte sur les harmoniques de degré un. Pour le correcteur

\[
H^\chi=-\frac{\chi'(r)}rV(\theta),
\]

on a exactement

\[
\|H^\chi\|_{L^2(\mathbb R^3)}^2
=\|V\|_{L^2(S^2)}^2
\int_0^\infty|\chi'(r)|^2dr.
\tag{44}
\]

Si `χ_ρ(r)=χ(r/ρ)`, le dernier facteur vaut

\[
\int|\chi_\rho'|^2dr
=\rho^{-1}\int|\chi'|^2ds.
\tag{45}
\]

Le correcteur a donc la même croissance d’enstrophie `ρ^{-1}` que le cœur tronqué. Sa norme critique forte est, elle, invariante d’échelle :

\[
\|H^{\chi_\rho}\|_{L^{3/2}}^{3/2}
=\|V\|_{L^{3/2}(S^2)}^{3/2}
\int_0^\infty
|\chi_\rho'(r)|^{3/2}r^{1/2}dr,
\tag{46}
\]

et le changement `r=ρs` élimine exactement toute puissance de `ρ`. La réparation est donc possible, mais elle n’est pas une petite erreur sous le scaling critique.

### Défaut visqueux d’une coupure

Même lorsque (41) répare la divergence, une coupure ne préserve pas l’équation de vorticité. Pour la partie brute,

\[
[\Delta,\chi]W
=2\nabla\chi\cdot\nabla W+(\Delta\chi)W.
\tag{47}
\]

Si `χ_ρ(r)=χ(r/ρ)` transite dans `ρ≤r≤2ρ`, si

\[
\|\chi'\|_\infty\leq A_1,
\qquad
\|\chi''\|_\infty\leq A_2,
\]

et si

\[
M_0=\|\Omega\|_\infty,
\qquad
M_1=\|\nabla_{S^2}\Omega\|_\infty,
\]

alors `|∇W|≤r^{-3}(2M₀+M₁)` et

\[
|[\Delta,\chi_\rho]W|
\leq
\rho^{-4}
\left[2A_1(2M_0+M_1)+(A_2+2A_1)M_0\right]
\tag{48}
\]

sur cette coquille. Le défaut visqueux `ν[Δ,χρ]W` est d’ordre `νρ^{-4}`, exactement le scaling de `νΔW`. En outre, la vitesse doit être recalculée à partir de `W^χ` par Biot–Savart; les termes de transport et d’étirement ne sont pas obtenus en multipliant ceux du profil initial par `χ`. Une coupure solénoïdale n’est donc toujours pas une solution approchée certifiée sans estimation du résidu complet.

## 8. Extension aux facteurs log-périodiques

La définition primaire permet aussi une dépendance périodique en `log r`. Posons

\[
W(x)=r^{-2}\Omega(\theta,s),
\qquad s=\log(r/R_0),
\tag{49}
\]

avec `Ω` périodique en `s`. Sur l’espace ponctué,

\[
\operatorname{div}W
=r^{-3}
\left(\partial_s\Omega_r
+\operatorname{div}_{S^2}\Omega_T\right).
\tag{50}
\]

La contrainte exacte devient donc

\[
\partial_s\Omega_r
+\operatorname{div}_{S^2}\Omega_T=0.
\tag{51}
\]

En intégrant sur la sphère,

\[
\partial_s\int_{S^2}\Omega_r(\theta,s)dS=0.
\tag{52}
\]

Le flux radial est constant le long de la phase logarithmique et doit encore être nul pour éviter un défaut à l’origine. La périodicité scalaire du facteur de forme ne garantit ni (51), ni ce flux nul. Si la période vaut `P`, le profil est invariant seulement sous les dilatations discrètes `r↦e^P r`.

## 9. Passe contradictoire

### Attaque A — magnitude critique versus vorticité

Le champ `e/r²` a exactement la magnitude et le meilleur contrôle directionnel possible, mais échoue déjà à être divergence-free hors de l’origine, voir (4).

**Verdict :** le profil scalaire et l’hypothèse `bmo_φ` sur la direction ne suffisent pas à définir une vorticité.

### Attaque B — divergence ponctuée versus divergence globale

Le champ `θ/r²` satisfait l’équation `div W=0` pour tout `r>0`, mais transporte le flux `4π` à travers chaque sphère et crée `4πδ₀`.

**Verdict :** vérifier seulement l’équation sur le domaine ponctué perd une charge distributionnelle essentielle.

### Attaque C — appartenance critique versus énergie Clay

Le profil global appartient exactement à `L^{3/2,∞}` pour la vorticité, mais sa vitesse homogène non nulle a une énergie infinie à l’infini par (29).

**Verdict :** la criticalité Lorentz ne fournit pas une donnée globale d’énergie finie; une coupure extérieure est indispensable.

### Attaque D — coupure extérieure innocente

La formule (38) montre qu’une coupure radiale d’un profil ayant une composante radiale crée un défaut `L¹` indépendant de l’échelle. La correction (41) est de même taille critique.

**Verdict :** aucune limite `R→∞` ou `ε→0` ne permet d’ignorer automatiquement le défaut de divergence.

### Attaque E — énergie locale finie versus solution adaptée

La singularité `u∼r^{-1}` est dans `L²_loc`, mais `|u|³∼r^{-3}` n’est pas intégrable spatialement au cœur à un temps fixé. Une occurrence à un temps isolé peut néanmoins être compatible avec certaines intégrabilités espace-temps; une occurrence persistante sur un intervalle ne l’est pas.

**Verdict :** l’énergie locale seule ne décide ni l’admissibilité faible adaptée, ni le blow-up.

### Attaque F — profil solénoïdal versus solution de Navier–Stokes

Les conditions (3), Biot–Savart et l’énergie ne vérifient ni l’équation de vorticité, ni la pression, ni l’inégalité d’énergie locale. Le commutateur (47) montre que les coupures produisent des défauts au même ordre que les termes principaux.

**Verdict :** le lemme obtenu est un filtre cinématique nécessaire et une reconstruction de vitesse, pas un profil de blow-up Navier–Stokes construit.

## 10. Lemme transférable et prochain test décisif

Le premier maillon transférable est le suivant :

> Un profil vectoriel critique homogène `W=r^{-2}Ω(θ)` est une vorticité globale admissible au sens cinématique si et seulement si son champ tangent vérifie `div_S Ω_T=0` et si son flux radial moyen est nul. Sous ces conditions, Biot–Savart reconstruit une vitesse incompressible homogène `-1`; toute coupure radiale d’une composante `Ω_r≠0` exige le correcteur explicite (41), dont la taille critique ne décroît pas avec l’échelle.

Ce lemme est exact et falsifiable sur une décomposition en harmoniques sphériques. Le prochain test décisif devrait :

1. extraire le facteur vectoriel `Ω` de chaque profil candidat;
2. calculer les résidus `div_S Ω_T` et `∫Ω_r` avec bornes d’erreur;
3. appliquer la correction (41) aux coupures intérieure et extérieure;
4. reconstruire `u` par Biot–Savart;
5. mesurer le résidu complet de l’équation de vorticité, et non seulement sa divergence.

## 11. Limites et indépendance de la revue

- La définition primaire a été vérifiée directement dans la v2; aucune publication évaluée par les pairs n’est attribuée à cette prépublication.
- Les dérivations (3)–(52) sont nouvelles au laboratoire et ne reçoivent pas le statut `PAPER_PROOF`.
- Le rapport ne démontre pas qu’un profil satisfaisant (3) apparaît dans une solution de Navier–Stokes.
- La passe contradictoire est séparée de la synthèse principale, mais elle provient de la même famille de modèle et ne constitue pas une revue inter-familles indépendante.
