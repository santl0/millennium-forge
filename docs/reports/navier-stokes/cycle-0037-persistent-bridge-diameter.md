# Cycle 0037 — Diamètre d'une branche de superniveaux persistante

Date : 2026-08-15
Statut : `AI_INTERNAL_DERIVATION`, à conserver `COMPUTATION_ONLY`
Portée : obstruction cinématique statique dans une sous-classe pure-swirl;
aucune évolution Navier–Stokes n'est construite.

## Décision adaptative

| Action | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| ledger direct du pont linéaire à deux gouttes | 4 | 5 | 5 | 4 | 18 |
| périmètre–diamètre sur une branche persistante | 5 | 5 | 5 | 5 | **20** |
| arbre de fusion et retroncature adaptative | 5 | 2 | 4 | 5 | 16 |

Le deuxième axe est sélectionné. Il ferme le pont de persistance relative
positive dès que son niveau est calibré à l'échelle endpoint locale. Le test
linéaire est conservé comme falsificateur reproductible et comme mesure de la
loi d'échappement lorsque la persistance tend vers zéro.

## Cadre exact

Soient (R>0), (sigma\in\{-1,+1\}) et

\[
 F\in C_c^\infty((0,\infty)\times\mathbb R),\qquad
 \operatorname{supp}F\subset\{R/2<r<3R/2\}.
\]

Sur (mathbb R^3), en coordonnées cylindriques, on pose

\[
 U=\frac RrF(r,z)e_\theta,
 \qquad
 W=\operatorname{curl}U
 =\frac Rr(-\partial_zF\,e_r+\partial_rF\,e_z).
\]

Le champ (U) est lisse, compact et exactement divergence-free. Les
quasi-normes sont

\[
 K_u=\sup_{s>0}s\,|\{|U|>s\}|^{1/3},\qquad
 K_w=\sup_{s>0}s\,|\{|W|>s\}|^{2/3}.
\]

Fixons (0<a<b). On suppose que, pour presque tout (t\in(a,b)), le
superniveau méridien

\[
 \mathcal E_t=\{(r,z):\sigma F(r,z)>t\}
\]

possède une composante ouverte (E_t) de diamètre axial au moins (D>0).
La composante peut dépendre de (t). Pour des représentants seulement BV,
le diamètre doit être celui de la projection essentielle d'une composante
indécomposable; le diamètre topologique d'un représentant arbitraire serait
faux modulo les ensembles nuls.

## Lemme actif

Sous les hypothèses précédentes,

\[
 \boxed{
 a(b-a)RD\le {9\over8\pi}K_uK_w.}
 \tag{37.1}
\]

Le produit de gauche et (K_uK_w) sont tous deux invariants sous le scaling
Clay. Le résultat est uniforme en la longueur du support total, le nombre
d'autres composantes et la finesse du pont.

## Dérivation à constantes suivies

Pour presque tout niveau régulier (t), une composante ouverte connexe de
(mathcal E_t) est indécomposable. Le lemme 2.13 de Dayrens–Masnou–Novaga–
Pozzetta donne (2\operatorname{diam}(E_t^1)\le P_2(E_t)); la version axiale
plus faible suit aussi directement du tranchage BV : la projection axiale est
un intervalle et presque chaque tranche non vide a périmètre unidimensionnel
au moins deux. Par additivité du périmètre,

\[
 P_2(\mathcal E_t)\ge P_2(E_t)\ge2D.
 \tag{37.2}
\]

Le poids du curl annule exactement le jacobien cylindrique. La coaire plane
donne, pour (H=\{a<\sigma F<b\}),

\[
 \begin{aligned}
 \int_H|W|\,dx
 &=2\pi R\int_{\{a<\sigma F<b\}}|\nabla F|\,dr\,dz\\
 &=2\pi R\int_a^bP_2(\mathcal E_t)\,dt\\
 &\ge4\pi RD(b-a).
 \end{aligned}
 \tag{37.3}
\]

Sur (H), le confinement annulaire implique

\[
 |U|={R\over r}|F|>{2a\over3},
 \qquad |H|^{1/3}\le {3K_u\over2a}.
 \tag{37.4}
\]

L'intégration de la fonction de distribution faible-(L^{3/2}), avec la
constante exacte (p/(p-1)=3), donne

\[
 \int_H|W|\,dx\le3K_w|H|^{1/3}
 \le {9\over2a}K_uK_w.
 \tag{37.5}
\]

La comparaison de (37.3) et (37.5) prouve (37.1). Les valeurs critiques sont
négligeables par Sard; aucun choix mesurable de (E_t) n'est utilisé. Le signe
(sigma) ne change ni les normes ni la coaire.

## Corollaires de persistance

Si une composante de ({\sigma F>b\}), ou un continuum inclus dans
({\sigma F\ge b\}), a diamètre axial (D), elle appartient pour tout
(t<b) à une composante de ({\sigma F>t\}) de diamètre au moins (D).
Le lemme s'applique donc à toute bande inférieure ((a,b)).

En particulier, si un pont reste au-dessus d'un cutoff (A>0), choisir
(a=A/2) et un (b>A) porté par le pont donne

\[
 \boxed{A^2RD\le {9\over2\pi}K_uK_w
 \le {3\over2}K_uK_w.}
 \tag{37.6}
\]

La seconde constante utilise seulement (pi>3) et sert au certificat
rationnel. Elle est indépendante de l'excès (b-A) : même si le pont dépasse
le cutoff d'une quantité arbitrairement petite, le curl original paie la
fermeture des niveaux entre (A/2) et (A).

Sous l'étalonnage critique additionnel

\[
 AR\ge\kappa K_u,
 \tag{37.7}
\]

on obtient

\[
 {D\over R}\le {9\over2\pi\kappa^2}{K_w\over K_u}.
 \tag{37.8}
\]

Ainsi un gate (K_u/K_w\ge q>0) borne uniformément le diamètre axial de la
branche persistante. Composé conditionnellement avec le cycle 0036 et le gate
directionnel du cycle 0033, il redonne une minoration d'oscillation locale de
type (c\kappa^6q^{15}), à constantes géométriques universelles près.

## Test adverse reproductible

Le profil à deux gouttes relie deux blocs de taille (R), distants de
(LR), par un pont de demi-largeur (w=\delta R), de cutoff (A) et de
hauteur (A(1+\eta)). Les parois radiales imposent au curl original

\[
 {K_{w,\mathrm{pont}}\over AR}
 \gtrsim(1+\eta)L^{2/3}\delta^{-1/3}.
 \tag{37.9}
\]

Si (AR\asymp K_u), le volume plateau impose (delta L\lesssim1), donc le
meilleur choix (delta\asymp L^{-1}) fait croître (K_w/(AR)) comme (L).
Un pont de persistance relative fixe est donc abandonné.

Pour le champ tronqué (G=(F-A)_+), seule une fraction
(eta/(1+\eta)) des rampes linéaires reste active et

\[
 {K_{w,G}^3\over(AR)^3}
 \asymp (1+\eta)\eta^2{L^2\over\delta}.
 \tag{37.10}
\]

Le coût tronqué peut rester borné si
(eta\lesssim\sqrt\delta/L), soit (eta\lesssim L^{-3/2}) sous
(delta L\lesssim1). Cela ne réfute pas (37.6) : le curl original voit
toujours l'amplitude absolue (A), et une retroncature dans la fenêtre
évanescente sépare les gouttes.

Le script `persistent_bridge_audit.py` utilise uniquement
`fractions.Fraction` et (3<\pi<22/7). Il vérifie 1 035 familles, 5 197
assertions et les identités exactes de la famille
(L=m^2,delta=L^{-1},eta=L^{-3/2}). Résidu arithmétique : zéro. Il ne
certifie pas la coaire continue ni le passage lipschitzien-lisse.

## Passe contradictoire

1. **Représentant BV.** Un filament nul peut rendre le diamètre topologique
   arbitraire; le diamètre essentiel ou les composantes ouvertes régulières
   sont indispensables.
2. **Fusion de composantes.** Une composante longue juste au-dessus du niveau
   bas peut provenir de gouttes qui fusionnent tardivement; elle ne persiste
   pas nécessairement sur une fenêtre relative positive.
3. **Niveau global.** Avec (m) gouttes comparables,
   (K_u\asymp ARm^{1/3}). L'étalonnage (37.7) n'est pas une conséquence
   automatique d'un niveau presque optimal global.
4. **Curl tronqué contre curl original.** Faire (eta\to0) économise le
   premier, jamais la fermeture compacte du second.
5. **Pression et dynamique.** Aucune pression, projection de Leray, diffusion,
   étirement, compacité temporelle ou solution ancienne n'intervient.

Le falsificateur analytique de (37.1) serait un (F) lisse satisfaisant les
hypothèses mais tel que le membre gauche dépasse (9K_uK_w/(8\pi)). Il devrait
contredire le périmètre–diamètre, la coaire pondérée exacte ou l'intégration
faible-Lorentz. Les profils testés n'en fournissent aucun.

## Résultat et prochain verrou

`GAP-ABOVE-THRESHOLD-THIN-BRIDGE` est fermé pour toute branche persistante
calibrée par (37.7), et un pont de persistance relative fixe est abandonné.
Le résultat ne borne pas encore la composante sélectionnée au niveau bas :
le premier quantificateur manquant est une dichotomie uniforme

\[
 \text{branche persistante et calibrée}
 \quad\text{ou}\quad
 \text{niveau intermédiaire qui scinde en morceaux de diamètre }O(R).
\]

Le prochain verrou est
`GAP-BRIDGE-SCALE-CALIBRATION-OR-MERGE-TREE`: relier le niveau local
(AR) à la quasi-norme de la composante sélectionnée, ou construire une
retroncature quantitative le long de l'arbre de fusion des superniveaux.
