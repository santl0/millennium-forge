# Cycle 0039 — revue primaire : bases, carrés-fonctions et endpoint faible-Lorentz

Date de coupure : **2026-08-15**
Objet : déterminer si une décomposition canonique/inconditionnelle, un frame
divergence-free ou un carré-fonction peut empêcher les cancellations entre
cellules superposées sous les seules bornes

\[
U\in L^{3,\infty}(\mathbb R^3),\qquad
W=\operatorname{curl}U\in L^{3/2,\infty}(\mathbb R^3).
\]

## Verdict endpoint

Le mécanisme recherché n'est pas disponible au endpoint `q=∞`.

1. Le plein espace `L^{p,∞}` est non séparable. Il ne peut donc posséder
   aucune base de Schauder dénombrable, a fortiori aucune base ondelette
   inconditionnelle dont les sommes partielles convergent en norme pour tout
   élément.
2. Les théorèmes publiés d'inconditionnalité dans les Lorentz exigent un
   indice secondaire fini. Karlovich 2021 suppose explicitement un espace de
   fonctions de Banach **séparable** et spécialise son résultat à
   `L^{p,q}`, `1<p<∞`, `1≤q<∞`. Le endpoint du verrou actif est omis.
3. Un carré-fonction de Littlewood–Paley reste contrôlable en
   `L^{p,∞}`, `1<p<∞`, par interpolation. Mais il porte sur le **champ total**.
   Si deux cellules étiquetées contiennent `+Z_n` et `-Z_n`, leur somme est
   effectuée avant la projection fréquentielle et avant le carré : le mode
   annulé est irrécupérable.
4. Les ondelettes divergence-free de Deriaz–Perrier donnent une
   représentation cinématique et un algorithme de Hodge en dimensions deux et
   trois. Elles ne donnent ni une base inconditionnelle du plein
   `L^{3,∞}`, ni une minoration de Gram des curls de cellules superposées.
5. La projection de Leray rétablit la divergence nulle après cutoff, mais ne
   supprime pas le curl de col et demeure non locale. Elle ne transforme donc
   pas une partition spatiale recouvrante en décomposition positive de la
   vorticité.

Le résultat négatif est précis : un carré-fonction peut empêcher la
cancellation **entre bandes du champ déjà sommé**; il ne peut empêcher la
cancellation **entre composantes étiquetées avant sommation**. Réparer le
contre-théorème du cycle exige une hypothèse anti-cancellation supplémentaire
(Gram, angle, positivité ou packing), ou un indice Lorentz secondaire fini.

## Cadre exact et échelle

La partie fonctionnelle de cette revue concerne des champs statiques lisses,
ou plus généralement des distributions tempérées, sur `R³` :

\[
\operatorname{div}U=0,\qquad W=\operatorname{curl}U.
\]

Le raccord Clay visé est l'équation incompressible 3D non forcée

\[
\partial_tu-\nu\Delta u+(u\cdot\nabla)u+\nabla p=0,
\qquad \operatorname{div}u=0
\]

sur `R³×(0,T)` ou le tore périodique, avec `ν>0`, donnée initiale lisse
divergence-free et solution classique/forte jusqu'au temps maximal. Aucun
théorème de bases utilisé ci-dessous ne crée une solution, ne contrôle le terme
quadratique ou la pression dans le temps, ni ne fournit un critère de
prolongement.

Sous l'échelle Navier–Stokes

\[
U_\lambda(x)=\lambda U(\lambda x),\qquad
W_\lambda(x)=\lambda^2W(\lambda x),
\]

les deux quantités actives sont critiques :

\[
\|U_\lambda\|_{L^{3,\infty}}=\|U\|_{L^{3,\infty}},\qquad
\|W_\lambda\|_{L^{3/2,\infty}}=\|W\|_{L^{3/2,\infty}}.
\]

Pour fixer les conventions, on écrit

\[
K_p(f)=\sup_{s>0}s\,|\{|f|>s\}|^{1/p}.
\]

## 1. Obstruction topologique : aucune base dénombrable du plein endpoint

L'obstruction ne dépend pas d'un choix particulier d'ondelettes. Prenons des
ensembles disjoints `E_n` de mesures `2^{-n}` et, pour chaque partie
`A⊂N`, posons

\[
f_A=\sum_{n\in A}2^{n/p}\mathbf 1_{E_n}.
\]

La somme géométrique des mesures donne uniformément

\[
K_p(f_A)\le 2^{1/p}.
\]

Si `A≠B`, un indice `n∈A△B` fournit

\[
K_p(f_A-f_B)\ge
2^{n/p}|E_n|^{1/p}=1.
\]

La boule de `L^{p,∞}` contient donc une famille non dénombrable séparée : le
plein espace est non séparable. Or l'adhérence des combinaisons rationnelles
finies d'une base de Schauder dénombrable est séparable. Il s'ensuit :

\[
\boxed{L^{p,\infty}(\mathbb R^3)
\text{ n'a pas de base de Schauder dénombrable}.}
\]

La même preuve vaut pour `p=3` et `p=3/2`. Elle interdit également un frame
dénombrable qui reconstruirait **tout** le plein espace par convergence en
norme de combinaisons finies. Elle n'interdit pas un frame continu, une
décomposition au sens des distributions, ni une base du sous-espace séparable

\[
L^{p,\infty}_0=overline{L^\infty_c}^{\,L^{p,\infty}}.
\]

Ce sous-espace ne ferme toutefois pas le problème de blow-up : une solution
lisse appartient au cœur séparable à chaque temps strictement antérieur au
temps maximal, mais une suite de temps ou de remises à l'échelle peut perdre
uniformément cette propriété.

### Source primaire qui matérialise la frontière

Alexei Yu. Karlovich, *Wavelet Bases in Banach Function Spaces*, *Bulletin of
the Malaysian Mathematical Sciences Society* 44 (2021), 1669–1689,
[DOI 10.1007/s40840-020-01024-4](https://doi.org/10.1007/s40840-020-01024-4),
publié avec évaluation par les pairs.

Le théorème suppose que l'opérateur maximal de Hardy–Littlewood est borné sur
un espace de fonctions de Banach **séparable** `X(R)` et son associé. Il donne
alors une base ondelette inconditionnelle et se spécialise aux Lorentz pondérés
`L^{p,q}(R,w)` pour `1<p<∞`, `1≤q<∞`, `w∈A_p`. La source ne traite pas
`q=∞` et ne doit pas être extrapolée à `R³` ou au plein faible-Lorentz sans un
autre théorème. Sa valeur ici est de confirmer que la séparabilité et
l'exclusion de `q=∞` sont structurelles, non une omission cosmétique.

Cette frontière est cohérente avec Bahouri–Cohen–Koch 2011
(`NS-SRC-0145`) : leur profil ondelette suppose une base inconditionnelle et
un gain d'approximation source-cible; leur discussion Lorentz passe par des
indices secondaires finis, tandis que le même indice secondaire faible ne
fournit pas l'approximation uniforme requise.

## 2. Décomposition canonique par amplitude : pointwise, pas en norme

La décomposition

\[
A_k(f)=\{2^k<|f|\le 2^{k+1}\},\qquad
f=\sum_{k\in\mathbb Z}f\mathbf 1_{A_k(f)}
\]

est canonique et invariante par permutation des cellules de niveau. La borne
faible donne seulement

\[
|A_k(f)|\le K_p(f)^p2^{-kp}.
\]

Il n'existe aucune sommabilité en `k` au endpoint. Plus fortement, pour

\[
f(x)=|x|^{-3/p}\mathbf 1_{|x|<1},
\]

la troncature de haute amplitude satisfait

\[
K_p\bigl(f\mathbf 1_{\{|f|>M\}}\bigr)\asymp 1
\quad\text{pour tout }M\ge1.
\]

Les sommes partielles bornées ne convergent donc pas vers `f` en norme
faible-`L^p`. Découper ensuite chaque `A_k` en cubes produit une
décomposition spatiale, mais aucune cellule ne porte une fraction uniforme :
le contre-exemple à `N` supports disjoints du cycle 0034 subsiste. La
canonicité des niveaux ne crée ni additivité de la quasi-norme ni cellule
dominante.

## 3. Ce qu'un carré-fonction contrôle réellement

Soit `(Δ_j)` une résolution dyadique lisse et

\[
S(f)(x)=\left(\sum_{j\in\mathbb Z}|\Delta_jf(x)|^2\right)^{1/2}.
\]

Pour `1<p<∞`, les estimations fortes de Littlewood–Paley et l'interpolation
de Hunt (`NS-SRC-0069`) donnent, d'abord pour les fonctions de Schwartz puis
par le prolongement approprié,

\[
\|S(f)\|_{L^{p,\infty}}\lesssim_p
\|f\|_{L^{p,\infty}}.
\]

La réciproque se lit par la formule de reproduction et la dualité
`L^{p,∞}`–`L^{p',1}` :

\[
\left|\int f g\right|
\lesssim\int S(f)\widetilde S(g)
\lesssim
\|S(f)\|_{L^{p,\infty}}\|g\|_{L^{p',1}}.
\]

Ainsi, avec les réserves habituelles sur les polynômes dans la version
homogène,

\[
\|f\|_{L^{p,\infty}}\asymp_p
\|S(f)\|_{L^{p,\infty}}.
\]

La source primaire classique pour les fonctions de Littlewood–Paley/Lusin est
Elias M. Stein, *On the functions of Littlewood-Paley, Lusin, and
Marcinkiewicz*, *Transactions of the AMS* 88 (1958), 430–466,
[DOI 10.2307/1993226](https://doi.org/10.2307/1993226). Le passage exact au
Lorentz faible affiché ci-dessus est une dérivation par interpolation et
dualité utilisant Hunt; il ne doit pas être attribué mot pour mot à Stein.

### Pourquoi cela ne répare pas les overlaps

Pour les champs du contre-théorème du cycle 0039,

\[
U_1=B+Z_n,\qquad U_2=-Z_n,qquad U_1+U_2=B,
\]

la linéarité donne

\[
\Delta_j(U_1+U_2)=\Delta_jB,qquad
S(U_1+U_2)=S(B).
\]

Le carré n'est pris qu'après l'annulation exacte de `Z_n`. Calculer
`(S(U_1)^2+S(U_2)^2)^{1/2}` empêcherait cette annulation, mais cette quantité
dépend de la décomposition étiquetée et n'est pas déterminée par le champ
total. Elle peut être rendue arbitrairement grande en ajoutant `+Z` et `-Z`
à n'importe quelle décomposition.

Même sans overlap, le faible `L^p` extérieur ne somme pas les cellules. Pour
`N` fonctions indicatrices disjointes d'amplitude `N^{-1/p}`, le carré local
est simplement le module, la norme globale vaut un et chaque cellule vaut
`N^{-1/p}`. Le carré-fonction résout donc une orthogonalité fréquentielle,
pas le pigeonhole spatial manquant.

## 4. Frames divergence-free et compatibilité curl

Erwan Deriaz et Valérie Perrier, *Divergence-free and curl-free wavelets in
two dimensions and three dimensions: application to turbulent flows*,
*Journal of Turbulence* 7, no. 3 (2006), 1–37,
[DOI 10.1080/14685240500260547](https://doi.org/10.1080/14685240500260547),
[arXiv:cs/0502092](https://arxiv.org/abs/cs/0502092) sous le titre de
prépublication *Divergence-free Wavelets for Navier-Stokes*, publié.

La source construit et implémente des ondelettes compactement supportées
divergence-free/curl-free en dimensions deux et trois, avec décomposition de
Hodge et tests numériques pour des écoulements incompressibles. Cela fournit
un dictionnaire cinématique intéressant : si `ψ_α` est divergence-free, alors
`curl ψ_α` est couplé exactement au même indice.

Mais aucun des maillons suivants n'est établi par cette source :

- convergence inconditionnelle en norme du plein `L^{3,∞}` ou
  `L^{3/2,∞}`;
- sélection d'un coefficient portant une fraction uniforme de la norme;
- minoration de Gram pour des curls d'atomes recouvrants;
- stabilité uniforme de la pression ou du non-linéaire Navier–Stokes;
- certificat d'erreur transformant les essais numériques en preuve PDE.

L'oscillation à fréquence `n` dans un volume fixé se distribue entre un nombre
croissant de coefficients fins. La relation exacte
`curl(Σc_αψ_α)=Σc_αcurl ψ_α` ne garantit pas qu'un terme possède le rapport
endpoint du total.

## 5. Localisation Hodge–Leray : défaut exact

Sur `R³`, avec

\[
\mathbb P=I-\nabla\Delta^{-1}\operatorname{div}
\]

et `div U=0`, une coupure lisse `χ` donne

\[
\mathbb P(\chi U)
=\chi U-\nabla\Delta^{-1}(\nabla\chi\cdot U).
\]

La correction est un gradient non local. Comme le curl d'un gradient est nul,

\[
\operatorname{curl}\mathbb P(\chi U)
=\operatorname{curl}(\chi U)
=\chi W+\nabla\chi\times U.
\]

Le projecteur répare donc la divergence, pas le curl de col. Pour une cellule
de rayon `r`, `|∇χ|≈r^{-1}`; le terme `∇χ×U` est critique sous la remise à
l'échelle Navier–Stokes. En sens inverse, localiser la vorticité produit

\[
\operatorname{div}(\chi W)=\nabla\chi\cdot W,
\]

et impose une nouvelle correction de Hodge avant Biot–Savart. La vitesse
reconstruite conserve alors une queue non locale.

Les opérateurs de Leray/Riesz sont globalement bornés sur `L^{p,∞}` pour
`1<p<∞` par interpolation; cette stabilité globale ne fournit aucune petite
constante de localisation. Les opérateurs de Bogovskiĭ à support contrôlé
(`NS-SRC-0103`) et leurs constantes géométriques (`NS-SRC-0111`) permettent
de construire des corrections locales, mais le coût du col et la dépendance à
la géométrie doivent rester dans les estimations. Les estimations locales de
Barker (`NS-SRC-0154`) conservent précisément des termes locaux de vitesse et
de pression; elles ne ferment pas le système avec le curl seul.

## 6. « Cancellations de vorticité » : ce qui ne suffit pas

Toute vorticité `W=curl U` vérifie `div W=0`. Cette identité différentielle
n'interdit pas l'anti-alignement. Le couple `Z_n,-Z_n` du cycle 0039 est déjà
formé de curls exacts de champs lisses divergence-free et s'annule pointwise.

Les estimations compensées de Bourgain–Brezis (`NS-SRC-0133`) et la théorie
des opérateurs canceling de Van Schaftingen (`NS-SRC-0134`) améliorent des
inégalités différentielles limites. Elles ne donnent pas une minoration du
type

\[
\left|\sum_\alpha W_\alpha\right|^2
\ge c\sum_\alpha|W_\alpha|^2.
\]

Cette dernière est une hypothèse de coercivité de Gram/angle. Elle est
exactement l'information manquante pour transformer un carré des composantes
en quantité contrôlée par le curl total. Elle n'est impliquée ni par
`div W_α=0`, ni par une multiplicité de supports bornée, ni par le fait que
chaque `W_α` soit un curl.

## 7. Implication explicite vers le problème Clay

La chaîne publiée disponible est

\[
\begin{aligned}
&q<\infty\text{ ou espace source plus fort}\
&\quad\Longrightarrow
\text{base/profils ondelettes et sommabilité de coefficients}\
&\quad\Longrightarrow
\text{sélection ou approximation quantitative conditionnelle}.
\end{aligned}
\]

La chaîne nécessaire aux seules gates Clay serait

\[
\begin{aligned}
&U\in L^{3,\infty},\quad W=\operatorname{curl}U\in L^{3/2,\infty}\
&\quad\Longrightarrow
\text{décomposition jointe norm-convergente et anti-cancellante}\
&\quad\Longrightarrow
\text{cellule commune de rapport uniforme}\
&\quad\Longrightarrow
\text{contrôle dynamique puis prolongement}.
\end{aligned}
\]

Le premier maillon de la seconde chaîne est faux pour une base dénombrable du
plein endpoint et faux pour une décomposition arbitraire à multiplicité deux.
Un carré-fonction du total ne le remplace pas. Même si ce maillon était ajouté
sous une hypothèse `q<∞` ou Gram, il resterait à contrôler la pression, les
commutateurs de cutoff, la compacité temporelle et le passage au temps maximal.

Conséquence : aucun résultat de cette revue n'établit régularité globale,
blow-up, ni nouveau critère Clay. Le gain falsifiable est l'exclusion d'une
classe précise de réparations « purement canoniques » au endpoint.

## 8. Veille différentielle 2026 au 15 août

Une interrogation primaire arXiv sur les soumissions du 1er au 15 août 2026
contenant « Navier–Stokes » a retourné 38 notices. Le filtrage des équations,
dimensions et notions de singularité a isolé deux nouveautés à signaler.

### Incompressible standard, mais forcé et avec frontière

Hugo Beirão da Veiga et Jiaqi Yang, *Pure-swirl loss of boundedness under
`L¹_tL²_x` forcing: exact mixed-norm ranges*,
[arXiv:2608.11553v1](https://arxiv.org/abs/2608.11553), soumise le
2026-08-12, **prépublication non évaluée**.

Équation exacte : Navier–Stokes incompressible 3D avec viscosité normalisée à
un et force `f`, dans le cylindre

\[
D=B_2(0,1)\times(0,1),
\]

no-slip sur la paroi verticale et free-slip sur les bases horizontales. Le
champ est pure-swirl, indépendant de la coordonnée axiale. Pour une donnée
initiale lisse, la solution est classique sur `[0,T)`, appartient à la classe
d'énergie, admet une trace forte `L²` au temps `T`, se prolonge en l'unique
solution de Leray–Hopf avec égalité d'énergie, tandis que
`||v(t)||_∞→∞`. La force construite appartient toujours à `L¹_tL²_x` et
devient singulière au temps terminal. Le terme convectif est exactement
absorbé par la pression; le même exemple vaut pour Stokes.

Non-transfert Clay : la force terminalement singulière est essentielle, le
domaine a une frontière et des conditions mixtes, et le mécanisme ne contient
aucune amplification non linéaire. Ce n'est ni un blow-up du système non forcé
sur `R³`/`T³`, ni une réfutation de la régularité Clay. La construction est en
revanche un bon test adverse contre toute affirmation « énergie +
`f∈L¹_tL²_x` implique bornitude » dans ce problème forcé.

### Implosion voisine, non incompressible

Yongteng Gu et Xiangdi Huang, *Formation of Implosion Singularities in 3D
Compressible Navier-Stokes-Korteweg Equation*,
[arXiv:2608.10554v1](https://arxiv.org/abs/2608.10554), soumise le
2026-08-11, **prépublication non évaluée**.

Le système est compressible sur `R³`, avec densité `ρ`, viscosités dépendant
de `ρ` et tenseur de Korteweg :

\[
\rho_t+\operatorname{div}(\rho u)=0,
\]

\[
(\rho u)_t+\operatorname{div}(\rho u\otimes u)+\nabla P
=\operatorname{div}(2\mu(\rho)Du)
+\nabla(\lambda(\rho)\operatorname{div}u)+\operatorname{div}K,
\]

avec `μ(ρ)=νρ^α`, `λ(ρ)=2ν(α-1)ρ^α` et une capillarité
`κ(ρ)=ε²α²ρ^{2α-3}`. L'annonce construit, pour certains petits `α<1/2`,
une implosion où la densité devient infinie. La compressibilité, la
capillarité, la viscosité variable et même le régime de viscosité volumique
non positive rompent tout raccord direct au système Clay. Aucun ID de
catalogue n'est recommandé pour ce cycle, sauf si le laboratoire ouvre un axe
comparatif sur les modèles compressibles.

Les notices déjà surveillées au cycle 0034 n'affichent pas de nouvelle version
postérieure à celles alors consignées : Grujić `arXiv:2607.08866v2` reste daté
du 2026-07-13 et Barker `arXiv:2510.20757v3` du 2026-08-11. Aucun changement
différentiel ne ferme le gap endpoint.

## 9. Sources minimales proposées après NS-SRC-0171

Ce rapport ne modifie pas le catalogue. Les quatre promotions suivantes sont
suffisantes; les autres références utiles sont déjà présentes.

| ID proposé | Source primaire | Statut | Rôle exact |
|---|---|---|---|
| **NS-SRC-0172** | Karlovich 2021, DOI `10.1007/s40840-020-01024-4` | publié / source vérifiée | base ondelette sous séparabilité; Lorentz seulement `q<∞` |
| **NS-SRC-0173** | Stein 1958, DOI `10.2307/1993226` | publié / source vérifiée | estimation forte de Littlewood–Paley/Lusin à interpoler avec `NS-SRC-0069` |
| **NS-SRC-0174** | Deriaz–Perrier 2006, DOI `10.1080/14685240500260547`, arXiv `cs/0502092` | publié / source vérifiée | ondelettes divergence-free et Hodge algorithmique 2D/3D; aucune certification endpoint |
| **NS-SRC-0175** | Beirão da Veiga–Yang, arXiv `2608.11553v1` | prépublication / revendication à auditer | perte de bornitude incompressible forcée dans un cylindre; non-transfert Clay explicite |

Ne pas créer de nouvel ID pour Bahouri–Cohen–Koch, Hunt,
Costabel–McIntosh, Guzmán–Salgado, Bourgain–Brezis, Van Schaftingen ou Barker :
ils sont déjà `NS-SRC-0145`, `0069`, `0103`, `0111`, `0133`, `0134` et
`0154`.

## 10. Passe contradictoire

1. **Non-séparabilité prise pour absence de tout outil spectral.** Elle exclut
   une base dénombrable norm-convergente du plein endpoint, pas un
   carré-fonction, une transformée continue ou une expansion distributionnelle.
2. **Théorème unidimensionnel extrapolé.** Karlovich est cité exactement sur
   `R`; aucune extension automatique à `R³` n'est revendiquée. L'obstruction
   de non-séparabilité est, elle, démontrée directement sur `R³`.
3. **Carré avant ou après somme.** Le carré-fonction canonique du champ total
   est pris après la somme linéaire. Prendre le carré des cellules avant la
   somme change la donnée et dépend de l'étiquetage.
4. **Confusion fréquence/espace.** L'orthogonalité dyadique ne produit pas une
   cellule spatiale dominante; le faible `L^p` conserve le contre-exemple
   disjoint.
5. **Divergence-free supposé anti-cancellant.** Les curls `Z_n` et `-Z_n`
   respectent exactement les contraintes différentielles et s'annulent
   néanmoins.
6. **Leray supposé local.** `P(χU)` contient
   `∇Δ^{-1}(∇χ·U)` et son curl contient toujours `∇χ×U`.
7. **Solution lisse donc cœur séparable uniforme.** L'appartenance à chaque
   temps fixé ne fournit aucune modulus uniforme à l'approche du temps maximal.
8. **Annonce forcée assimilée à Clay.** La force de `2608.11553v1` devient
   singulière, le domaine est borné à conditions mixtes, et la convection est
   absorbée par la pression.
9. **Calcul numérique promu en preuve.** Deriaz–Perrier valide un algorithme
   de représentation; aucun résidu PDE certifié ni passage au continuum n'est
   utilisé ici.

## 11. Lemme et expérience décisive recommandés

Le prochain lemme positif minimal ne doit pas demander une « meilleure base »
du plein endpoint. Il doit isoler une hypothèse quantitativement testable, par
exemple : pour une famille canonique `U_α` et
`W_α=curl U_α`, sur les bandes retenues,

\[
\left|\sum_\alpha W_\alpha(x)\right|^2
\ge c_{\rm Gram}\sum_\alpha|W_\alpha(x)|^2
\quad\text{avec }c_{\rm Gram}>0
\]

et une borne de packing des cols de cutoff. Sous cette hypothèse, tester si le
carré-fonction de phase-espace produit effectivement une cellule commune.

Expérience falsifiable : appliquer une transformée divergence-free à la
famille pure-swirl exacte du cycle 0039, puis mesurer simultanément

\[
G_U(x)=\left(\sum_\alpha|U_\alpha(x)|^2\right)^{1/2},\qquad
G_W(x)=\left(\sum_\alpha|\operatorname{curl}U_\alpha(x)|^2\right)^{1/2}
\]

avant et après sommation des labels. Si le quotient entre la quantité
pré-somme et celle du champ total croît comme `n`, toute constante de frame
indépendante des cancellations est réfutée. Si une règle canonique empêche
cette croissance, la propriété exacte empêchante — angle, signe, localisation
ou coefficient packing — devient le nouvel énoncé à démontrer.

## Conclusion opérationnelle

**ABANDONNER** la réparation « base inconditionnelle du plein
faible-Lorentz ». **RÉVISER** la piste square-function : elle ne devient utile
qu'avec une coercivité anti-cancellation explicite ou une amélioration
`L^{p,q}`, `q<∞`. Le verrou n'est pas l'absence d'un dictionnaire
divergence-free; c'est l'absence de sommabilité et de positivité au endpoint,
aggravée par le commutateur non local de Leray sous localisation.
