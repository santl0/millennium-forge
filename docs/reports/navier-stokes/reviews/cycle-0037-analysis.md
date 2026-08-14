# Cycle 0037 — Coût endpoint d'une composante axialement persistante

**Statut :** `AI_INTERNAL_DERIVATION` — ne pas classer `PAPER_PROOF`

**Verdict :** le lemme proposé est vrai. Avec la convention
\(\|f\|_{L^{p,\infty}}=\sup_{s>0}s|\{|f|>s\}|^{1/p}\), on peut prendre

\[
 \boxed{C=\frac{9}{8\pi}}.                     \tag{1}
\]

La conclusion porte sur un diamètre axial présent à presque tous les niveaux
de la bande. Elle ne contrôle pas automatiquement une composante du niveau
bas dont le grand diamètre provient de la fusion tardive de plusieurs
gouttes.

## Cadre exact

Soient \(R>0\) et

\[
 F\in C_c^\infty((0,\infty)\times\mathbb R),
 \qquad
 \operatorname{supp}F\subset\{R/2<r<3R/2\}.   \tag{2}
\]

Sur \(\mathbb R^3\), posons

\[
 U=\frac RrF(r,z)e_\theta,
 \qquad
 W=\operatorname{curl}U
 =\frac Rr(-\partial_zF e_r+\partial_rF e_z).   \tag{3}
\]

Le champ \(U\) est lisse, compact et divergence-free. Notons

\[
 K_u=\|U\|_{L^{3,\infty}(\mathbb R^3)},
 \qquad
 K_w=\|W\|_{L^{3/2,\infty}(\mathbb R^3)}.       \tag{4}
\]

Fixons \(0<a<b\) et \(\sigma\in\{-1,+1\}\). Supposons que, pour presque tout
\(t\in(a,b)\), le superniveau méridien

\[
 \mathcal E_t=\{(r,z):\sigma F(r,z)>t\}         \tag{5}
\]

possède une composante ouverte \(E_t\) telle que

\[
 \operatorname{diam}_z(E_t)
 :=\sup_{(r,z)\in E_t}z-inf_{(r,z)\in E_t}z
 \ge D.                                        \tag{6}
\]

La composante peut dépendre de \(t\) ; aucune sélection mesurable de
\(t\mapsto E_t\) n'est nécessaire.

## Lemme de périmètre plan

Si \(E\Subset\mathbb R^2\) est ouvert, connexe et de périmètre fini, alors

\[
 \operatorname{Per}_2(E)\ge2\operatorname{diam}_z(E). \tag{7}
\]

En effet, la projection d'un ouvert connexe sur l'axe \(z\) est un intervalle
ouvert de longueur \(\operatorname{diam}_z(E)\). Pour presque tout \(z\) de
cet intervalle, la tranche

\[
 E_z=\{r:(r,z)\in E\}
\]

est un ouvert borné non vide de \(\mathbb R\), donc son périmètre
unidimensionnel est au moins deux. Le théorème de tranchage BV donne

\[
 \operatorname{Per}_2(E)
 \ge |D_r\mathbf1_E|(\mathbb R^2)
 =\int_{\mathbb R}\operatorname{Per}_1(E_z)\,dz
 \ge2\operatorname{diam}_z(E).                 \tag{8}
\]

Pour un ensemble de périmètre fini seulement défini modulo les ensembles
nuls, (7) exige le **diamètre essentiel** de la projection d'une composante
indécomposable. Un représentant auquel on ajoute un filament de mesure nulle
peut avoir un diamètre topologique arbitraire sans changer son périmètre. Ce
piège ne concerne pas (5) aux niveaux réguliers : le superniveau strict d'une
fonction lisse est ouvert et ses composantes sont les représentants naturels.

## Niveaux réguliers, composantes et additivité

Par Sard, les valeurs critiques de \(F\) ont mesure de Lebesgue nulle. Pour
presque tout \(t\), \(\partial\mathcal E_t\) est une sous-variété lisse
compacte. Les composantes ouvertes ont alors un périmètre fini, et le
périmètre du superniveau est la somme de leurs périmètres. Ainsi l'existence
d'une composante vérifiant (6) implique

\[
 \operatorname{Per}_2(\mathcal E_t)
 \ge\operatorname{Per}_2(E_t)
 \ge2D                                             \tag{9}
\]

pour presque tout \(t\in(a,b)\). Les niveaux critiques, les plateaux et les
éventuelles égalités \(\sigma F=a,b\) n'affectent pas l'intégrale de coaire.

Dans un langage entièrement BV, il faut décomposer le superniveau en
composantes indécomposables et utiliser l'additivité du périmètre. La version
avec composantes topologiques arbitraires d'un représentant mesurable serait
fausse à cause des filaments nuls ; la version lisse (5) est correcte.

## Passage au périmètre tridimensionnel axisymétrique

La rotation d'un ensemble méridien \(E\) autour de l'axe possède le périmètre

\[
 \operatorname{Per}_3(\operatorname{Rot}E)
 =2\pi\int_{\partial^*E}r\,d\mathcal H^1.       \tag{10}
\]

Comme \(R/2<r<3R/2\),

\[
 \operatorname{Per}_3(\operatorname{Rot}E)
 \ge\pi R\operatorname{Per}_2(E)
 \ge2\pi RD.                                   \tag{11}
\]

Cette borne est correcte mais non optimale pour le lemme. Le poids
\(R/r\) du curl annule exactement le jacobien cylindrique. Pour
\(g=\sigma F\),

\[
 \begin{aligned}
 \int_{\{a<g<b\}}|W|\,dx
 &=2\pi R\int_{\{a<g<b\}}|\nabla F|\,dr\,dz\\
 &=2\pi R\int_a^b
   \operatorname{Per}_2(\{g>t\})\,dt.
 \end{aligned}                                  \tag{12}
\]

La seconde égalité est la coaire plane. Elle équivaut à une coaire
tridimensionnelle pondérée : sur une surface de révolution,
\(d\mathcal H^2=2\pi r\,d\mathcal H^1\), puis le facteur \(R/r\) redonne
\(2\pi R\). Aucune constante dépendant de l'axe ou de l'aspect axial n'est
perdue.

En utilisant (9) dans (12),

\[
 \boxed{
 \int_{\{a<\sigma F<b\}}|W|\,dx
 \ge4\pi R D(b-a)}.                            \tag{13}
\]

## Borne faible-Lorentz et constante

Sur la bande \(H=\{a<\sigma F<b\}\), on a \(|F|>a\). Le facteur annulaire
donne, dans le bon sens,

\[
 |U|=\frac Rr|F|>\frac{2a}{3},
 \qquad
 H\subset\{|U|>2a/3\}.                         \tag{14}
\]

Par définition de \(K_u\),

\[
 |H|^{1/3}
 \le\mu_U(2a/3)^{1/3}
 \le\frac{3K_u}{2a}.                           \tag{15}
\]

L'intégration de la fonction de distribution faible-
\(L^{3/2}\) donne, avec la constante exacte
\(p/(p-1)=3\),

\[
 \int_H|W|\,dx
 \le3K_w|H|^{1/3}
 \le\frac{9}{2a}K_uK_w.                        \tag{16}
\]

La comparaison de (13) et (16) fournit

\[
 4\pi RD(b-a)\le\frac{9}{2a}K_uK_w,
\]

soit

\[
 \boxed{
 a(b-a)RD
 \le\frac{9}{8\pi}K_uK_w}.                    \tag{17}
\]

Le signe \(\sigma\) ne change ni \(|\nabla F|\), ni \(|F|\), ni les
fonctions de distribution. Tous les sens d'inclusion et d'inégalité sont
donc identiques pour \(\sigma=-1\).

## Exemple de persistance suffisant

Supposons qu'un ensemble connexe

\[
 C_b\subset\{\sigma F\ge b\}
\]

ait un diamètre axial au moins \(D\). Pour chaque \(t<b\), il est contenu
dans une composante unique de \(\{\sigma F>t\}\), dont le diamètre est donc
au moins \(D\). L'hypothèse du lemme vaut sur tout \((a,b)\), même si \(b\)
est une valeur critique ou si \(C_b\) est porté par un plateau.

Si l'on part plutôt d'une composante de \(\{\sigma F>b\}\), le même argument
est immédiat par l'inclusion

\[
 \{\sigma F>b\}\subset\{\sigma F>t\},
 \qquad t<b.                                    \tag{18}
\]

La persistance d'une **même** composante n'est toutefois pas nécessaire pour
(17) : une composante différente peut réaliser le diamètre \(D\) à chaque
niveau.

## Corollaire quantitatif sous gates d'amplitude

Supposons en outre

\[
 aR\ge\kappa K_u,
 \qquad
 b-a\ge\gamma a,                               \tag{19}
\]

avec \(\kappa,\gamma>0\). Alors

\[
 a(b-a)RD
 \ge\gamma a^2RD
 \ge\gamma\kappa^2K_u^2\frac DR.
\]

L'équation (17) implique

\[
 \boxed{
 \frac DR
 \le\frac{9}{8\pi\gamma\kappa^2}
       \frac{K_w}{K_u}}.                       \tag{20}
\]

Sous un gate \(K_u/K_w\ge\delta>0\),

\[
 \frac DR
 \le\frac{9}{8\pi\gamma\kappa^2\delta}.      \tag{21}
\]

Cette conclusion est critique et uniforme : elle ne dépend ni de la longueur
du support complet, ni du nombre des autres composantes.

## Rapport exact au gate du cycle 0036

Pour les seuils du cycle 0036,

\[
 a=\lambda/4,
 \qquad b=\lambda/2,
 \qquad b-a=a,
\]

donc \(\gamma=1\). Si une composante pertinente persiste axialement à travers
tout l'intervalle et si

\[
 \frac{\lambda R}{4}=aR\ge\kappa K_u,          \tag{22}
\]

alors (21) lui fournit la boîte axiale uniforme exigée par C36. Le gate
directionnel local peut être appliqué à sa troncature lipschitzienne, sous la
dette d'interface C33 déjà enregistrée au cycle 0036.

Si la constante directionnelle de C33 est suivie comme

\[
 c_\Lambda\asymp(9/4+\Lambda^2)^{-3/2},
\]

l'insertion de
\(\Lambda\lesssim(\gamma\kappa^2\delta)^{-1}\) dans le gate C36 donne, dans
le régime \(\delta\ll1\), une minoration de la forme

\[
 \operatorname{MO}_B(\zeta)
 \gtrsim \gamma^3\kappa^6\delta^{15},          \tag{23}
\]

à constantes géométriques universelles près. Les douze premières puissances
proviennent de la sélection endpoint C36 ; trois puissances supplémentaires
proviennent du volume de la boule déduit de (20).

### Limite de cette composition

Une composante de \(\{\sigma F>a\}\) peut avoir un grand diamètre parce que
plusieurs gouttes éloignées fusionnent juste au-dessus de \(a\), puis se
séparent avant \(b\). Dans ce cas, aucun composant individuel des niveaux
proches de \(b\) ne conserve le grand diamètre. L'hypothèse de (17) échoue et
le lemme ne borne pas le diamètre de la composante basse.

Ainsi

\[
 \text{diamètre de la composante à }a
 \not\Rightarrow
 \text{diamètre persistant sur presque tout }(a,b).    \tag{24}
\]

Le théorème C37 complète C36 seulement pour une branche persistante ou pour
un minorant uniforme du diamètre maximal à presque tous les niveaux. Il ne
ferme pas le scénario de fusions et séparations multi-niveaux.

## Contre-profil à une borne de diamètre sans niveau d'amplitude

Les gates globaux seuls ne bornent pas le diamètre de **toute** composante.
Fixons un pur swirl compact principal de taille un, qui détermine des
endpoints \(K_u,K_w\asymp1\). Ajoutons loin de lui un profil axial lisse de
rayon méridien \(R=1\), de longueur \(D\), et d'amplitude

\[
 \varepsilon_D=D^{-1}.
\]

Pour un profil à section fixe, ses contributions d'échelle sont

\[
 K_{u,\mathrm{tail}}asymp
 \varepsilon_DD^{1/3}=D^{-2/3},
 \qquad
 K_{w,\mathrm{tail}}asymp
 \varepsilon_DD^{2/3}=D^{-1/3}.                \tag{25}
\]

Elles tendent vers zéro, tandis que des superniveaux à des fractions fixes de
\(\varepsilon_D\) ont un diamètre axial \(\asymp D\). Le champ reste lisse,
compact, divergence-free et exactement curl-compatible. On peut relier les
deux parties par une queue située sous le seuil \(a\).

Ce profil ne réfute pas (17), car pour
\(a\asymp b-a\asymp\varepsilon_D\),

\[
 a(b-a)RD\asymp D^{-1}.
\]

Il réfute l'inférence supplémentaire selon laquelle les seuls gates globaux
forceraient \(D/R=O(1)\) à tous les niveaux. La condition
\(aR\gtrsim K_u\) de (19) est substantielle.

## Scaling

Sous l'échelle Navier--Stokes

\[
 U_\rho(x)=\rho U(\rho x),
 \qquad W_\rho(x)=\rho^2W(\rho x),
\]

on a

\[
 a_\rho=\rho a,
 \quad (b-a)_\rho=\rho(b-a),
 \quad R_\rho=R/\rho,
 \quad D_\rho=D/\rho.
\]

Le produit \(a(b-a)RD\), comme \(K_uK_w\), est invariant. Les rapports
\(aR/K_u\), \((b-a)/a\), \(D/R\) et \(K_u/K_w\) de (19)--(21) sont également
critiques.

## Passe contradictoire

1. **Diamètre topologique d'un représentant BV.** Il est faux modulo les
   ensembles nuls ; utiliser une composante ouverte régulière ou un diamètre
   essentiel indécomposable.
2. **Périmètre de l'union.** Aux niveaux réguliers, les périmètres des
   composantes s'additionnent. Une composante longue suffit à minorer le
   périmètre total.
3. **Coaire plane contre coaire 3D.** Le poids \(R/r\) et le jacobien \(r\)
   s'annulent exactement ; la constante \(4\pi\) dans (13) est correcte.
4. **Sens de l'inclusion.** Sur la bande, \(|U|>2a/3\), donc son volume est
   majoré — non minoré — par la distribution de \(U\) au niveau \(2a/3\).
5. **Signe.** Remplacer \(F\) par \(-F\) ne change aucune norme ni variation.
6. **Niveaux critiques.** Ils forment un ensemble de valeurs nul par Sard et
   sont invisibles pour coaire ; les extrémités \(a,b\) peuvent être
   critiques.
7. **Composante variable avec le niveau.** Elle est autorisée ; aucune
   mesurabilité du choix n'est utilisée.
8. **Persistance inversée.** Une composante haute est contenue dans une
   composante basse. L'implication inverse est fausse lors d'une fusion.
9. **Gate C36.** Le lemme borne une branche persistante, pas nécessairement
   toutes les composantes basses auxquelles C36 voudrait appliquer son gate.
10. **Clay.** Le résultat est une obstruction cinématique statique ; il ne
    traite ni pression, ni diffusion, ni temps, ni admissibilité d'un blow-up.

## Premier quantificateur faux, falsificateur et état

Le **premier quantificateur faux** après (17) est :

\[
 \text{« le niveau presque optimal global satisfait automatiquement }
 aR\gtrsim K_u\text{ pour chaque composante pertinente ».}                \tag{26}
\]

Avec \(m\) gouttes comparables au même niveau,
\(K_u\asymp aR\,m^{1/3}\), donc
\(aR/K_u\asymp m^{-1/3}\). La condition (19) ne suit pas des fonctions de
distribution globales.

Un falsificateur du lemme principal serait un profil lisse compact satisfaisant
(2)--(6) mais tel que

\[
 a(b-a)RD>\frac{9}{8\pi}K_uK_w.
\]

Il devrait violer au moins l'une des trois briques exactes :
\(P_2(E)\ge2\operatorname{diam}_z(E)\), la coaire pondérée (12), ou la borne
faible-Lorentz (16). Aucun tel profil n'existe sous les hypothèses énoncées.

**État :** `CONTINUER` pour le lemme et son corollaire conditionnel ;
`À REPRENDRE` pour les fusions multi-niveaux et pour dériver
\(aR\gtrsim K_u\) sur la goutte effectivement sélectionnée par C36.
