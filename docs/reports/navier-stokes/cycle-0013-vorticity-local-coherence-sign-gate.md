# Cycle 0013 — porte locale cohérence–signe de l'étirement

Date : 2026-08-14. Verrou actif : `VORTICITY-LOCAL-COHERENCE-SIGN-GATE-1`.

## Décision adaptative

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total | Décision |
|---|---:|---:|---:|---:|---:|---|
| contre-profil périodique exact : cohérence locale contre stretching signé | 4 | 5 | 5 | 5 | **19/20** | sélectionnée |
| audit théorème-par-théorème de Grujić `2607.08866v2` | 5 | 2 | 4 | 5 | 16/20 | cycle suivant |
| formalisation du noyau Fourier vorticité–strain | 3 | 4 | 5 | 3 | 15/20 | différée |

Le cycle ne travaille que sur le lemme négatif suivant : des invariants
quadratiques globaux pairs, l'hélicité nulle et une direction de vorticité
arbitrairement cohérente dans un patch local ne peuvent, à eux seuls,
déterminer le signe ou imposer une petite borne sans échelle sur le stretching
ponctuel au centre.

## Équation et notion de solution figées

Le domaine est le tore normalisé
`T³=(R/2πZ)³`. La viscosité est un nombre fixé `ν>0`, la force est nulle et
les conditions au bord sont périodiques :

```text
∂t u + (u·∇)u - νΔu + ∇p = 0,
div u = 0,
u(0)=u₀.
```

Le certificat porte sur deux données initiales `C∞`, analytiques, de moyenne
nulle et divergence-free. La théorie locale classique fournit une solution
forte unique sur un intervalle non nul, mais aucune propriété géométrique n'est
revendiquée après l'instant initial. Ce n'est ni une solution ancienne, ni une
trajectoire de blow-up, ni deux solutions pour la même donnée.

## Contre-profil exact

Pour `a∈{−1,+1}`, posons

```text
u_a(x,y,z) = (sin y + a sin x cos z, 0, −a cos x sin z).
```

Alors

```text
div u_a = a cos x cos z − a cos x cos z = 0,
ω_a = curl u_a = (0, −2a sin x sin z, −cos y),
```

et

```text
∇u_a = [[a cos x cos z, cos y, −a sin x sin z],
        [0,              0,      0],
        [a sin x sin z,  0,     −a cos x cos z]],

S_a = [[a cos x cos z, (cos y)/2, 0],
       [(cos y)/2,     0,          0],
       [0,             0,         −a cos x cos z]].
```

Le terme signé est donc, partout,

```text
ω_a·S_aω_a = −a cos x cos z cos²y.                 (1)
```

À l'origine,

```text
ω_a(0)=(0,0,−1),       Dω_a(0)=0,
ξ_a(0)=−e₃,            ξ_a·S_aξ_a(0)=−a,
ω_a·S_aω_a(0)=−a.                                      (2)
```

Le renversement `a↦−a` est exactement la translation `x↦x+π`. Les deux
champs ont donc toutes les statistiques spatiales invariantes par translation
identiques, pas seulement les quantités calculées ci-dessous.

## Quantités globales et pression

Avec `〈f〉=(2π)⁻³∫_{T³}f`, Parseval donne

```text
E_a=(1/2)〈|u_a|²〉=(1+a²)/4,
Z_a=(1/2)〈|ω_a|²〉=1/4+a²/2,
P_a=〈|∇ω_a|²〉=1/2+2a²,
H_a=〈u_a·ω_a〉=0.
```

Pour `a=±1`, `(E,Z,P,H)=(1/2,3/4,5/2,0)`. L'enstrophie et la
palinstrophie sont ici des quantités quadratiques testées, pas des invariants
dynamiques 3D. La moyenne du stretching (1) est nulle; l'identité globale
initiale est donc

```text
dZ/dt|₀ = −ν〈|∇ω_a|²〉 = −(5/2)ν.
```

Le signe local ne doit pas être confondu avec la production globale.

La pression périodique de moyenne nulle est aussi recalculée. Comme

```text
∂i u_j ∂j u_i = a²(cos 2x + cos 2z),
```

on a exactement

```text
−Δp_a = ∂i u_j ∂j u_i,
p_a=(a²/4)(cos 2x+cos 2z).
```

La convolution des six modes Fourier reproduit ces quatre coefficients sans
résidu. La pression est paire en `a`; le renversement de signe en (2) n'est pas
un artefact d'une pression omise.

## Cohérence locale certifiée

Soit

```text
Q_r={|x|,|y|,|z|≤r},    0<r≤1/2,
c_r=1−r²/2.
```

Sur `Q_r`, `cos y≥c_r>0`. En écrivant la direction, à un signe commun près,
comme la normalisation de

```text
(0, θ_a, 1),    θ_a=2a sin x sin z / cos y,
```

les inégalités `|sin s|≤|s|` et `cos s≥1−s²/2` donnent

```text
sin angle(ξ_a(X),ξ_a(0)) ≤ 2|a|r²/c_r,               (3)
sin angle(ξ_a(X),ξ_a(Y)) ≤ (2|a|r/c_r)||X−Y||₁.      (4)
```

La dérivée en `y` est contrôlée par `2|a|r³/c_r²`, inférieure à la
constante de (4). Ces bornes dépendent seulement de `|a|`; elles sont donc
identiques pour la paire signée. Pourtant, (1) garde le signe `−a` sur tout
`Q_r`, et

```text
|ω_a·S_aω_a| ≥ c_r⁴ ≥ (7/8)⁴ = 2401/4096.           (5)
```

La borne (3) tend vers zéro comme `r²` tandis que le stretching central reste
égal à `±1`. La cohérence centre–boule arbitrairement fine obtenue en
rétrécissant le patch ne produit donc aucun coefficient de déplétion sans
échelle.

## Lois d'échelle

Sur le tore, pour un entier `N≥1`, le scaling Navier–Stokes est

```text
U_{a,N}(x)=N u_a(Nx),       P_{a,N}(x)=N²p_a(Nx).
```

Il donne

```text
E[U]=N²E[u],             Z[U]=N⁴Z[u],
P[U]=N⁶P[u],             H[U]=N³H[u]=0,
Ω(0)=−N²e₃,
ξ·Sξ(0)=−aN²,
Ω·SΩ(0)=−aN⁶.
```

Sur `Q_{r/N}`, les bornes (3)–(5) sont inchangées après composition par
`Nx`, et

```text
(Ω·SΩ)/|Ω|³ (0) = −a.
```

Le patch est donc à l'échelle critique `|Ω(0)|^{-1/2}`. Mais l'énergie croît
comme `N²` : cette famille ne conjugue pas cohérence critique et borne
énergétique uniforme. Le lift distinct `v_{a,N}=u_a(Nx)` garde l'énergie
fixe, mais son patch `r/N` est plus petit que l'échelle
`|curl v(0)|^{-1/2}=N^{-1/2}`. Les deux conventions sont testées séparément.

## Certificat reproductible

Commande :

```text
python -B experiments/navier-stokes/vorticity-local-coherence/local_coherence_audit.py
```

L'artefact utilise `fractions.Fraction`, six modes Fourier explicites, aucune
grille, aucun pas de temps, aucune FFT et aucun flottant. Il vérifie :

- réalité et divergence mode par mode ;
- curl, énergie, enstrophie, palinstrophie et hélicité ;
- gradient, strain, vorticité et premier jet au centre ;
- convolution exacte de l'équation de Poisson pour la pression ;
- signes `a=±1`, bornes rationnelles de cohérence et persistance du signe ;
- scaling Navier–Stokes et lift fréquentiel pour `N=1,2,4,8,16,32`.

Empreinte SHA-256 :
`04112a48e77a5286fd3e98a73471577a7f30a9b0acbd027699177b6204649708`.
Tous les résidus algébriques et tous les compteurs d'échec sont nuls. Les
seules inégalités hors calcul sont les deux bornes trigonométriques
élémentaires explicitées ci-dessus.

## Passe contradictoire

Trois dérivations séparées de même famille de modèle ont contrôlé le champ.
Elles ne constituent pas une revue externe indépendante. Elles ont attaqué les
quantificateurs suivants :

1. **centre–boule contre pairwise** : (3) ne suffit pas à elle seule; (4) est
   donc vérifiée séparément dans un seul cube ;
2. **rayon choisi après le champ** : tout champ analytique non nul est cohérent
   sur un voisinage assez petit; une hypothèse utile doit fixer le rayon ou le
   relier uniformément à l'échelle critique ;
3. **seuil de forte vorticité** : le scaling franchit tout seuil absolu sur le
   patch, mais ne contrôle pas toutes les composantes de l'ensemble global de
   forte vorticité ;
4. **analyticité non uniforme** : les normes sur une bande complexe fixe
   croissent avec `N`; le mot « analytique » seul n'est pas une constante ;
5. **non-localité** : `S` est reconstruit globalement par les modes, mais une
   localisation sur `R³` demanderait une correction divergence-free et un
   contrôle de la queue de Biot–Savart/pression ;
6. **instant contre trajectoire** : rien ne prouve la persistance temporelle de
   la cohérence ni du signe.

Les critères de Constantin–Fefferman et de Beirão da Veiga–Berselli ne sont
pas réfutés. Ils exigent un seuil et un module uniformes en temps sur toute la
région de forte vorticité; leur conclusion repose sur une estimation intégrée,
pas sur une règle universelle de signe ponctuel.

## Veille différentielle

Deux sources classiques sont fixées plus exactement : Constantin–Fefferman
1993 (`NS-SRC-0021`) traite `R³`, une solution faible issue de `H¹` et une
cohérence lipschitzienne uniforme sur la zone de forte vorticité; Beirão da
Veiga–Berselli 2002 (`NS-SRC-0060`) abaisse le seuil géométrique à
`1/2`-Hölder sous une hypothèse conditionnelle comparable.

La prépublication récente Grujić, `arXiv:2607.08866v2` (`NS-SRC-0059`),
revendique une chaîne logarithmique pour un scénario ponctuel critique sous
`ω∈L∞_tL^{3/2,∞}_x` et `ξ∈L∞_t bmo_{1/|log r|}` local. Elle est enregistrée
comme prépublication non reproduite. Elle ne constitue pas une résolution
générale; l'étape géométrique reliant sparseness tridimensionnelle et section
unidimensionnelle, ainsi que les constantes du commutateur localisé, deviennent
le prochain objet d'audit.

## Résultat et pivot

Résultat négatif acquis : abandonner toute recherche de signe fondée seulement
sur l'hélicité globale, les quantités quadratiques, l'analyticité sans constante
et une cohérence choisie dans un patch. Le premier maillon manquant est un
énoncé **global et uniforme** reliant géométrie de tout l'ensemble de forte
vorticité, partie lointaine du strain et quantité intégrée coercive.

Prochaine expérience décisive : extraire de `2607.08866v2` l'implication
géométrique exacte « sparseness 3D → sparseness 1D au même point et à la même
échelle », figer tous ses quantificateurs, puis construire soit une preuve
élémentaire, soit un ensemble mesurable adverse reproductible.
