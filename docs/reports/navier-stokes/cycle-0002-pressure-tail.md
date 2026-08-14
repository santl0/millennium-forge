# Cycle 0002 — Pression distante centrée

Date : 2026-08-14.

## Décision du cycle

Après le gate de désingularisation, trois actions sont notées : pression
distante centrée (nouveauté 4, tractabilité 5, falsifiabilité 5, levier 5 :
19/20), nouvelle contrainte de vorticité (4+3+4+4=15) et Liouville Type II
(5+1+2+5=13). Le premier choix est exécuté.

## Équation et type de solution

NS incompressible 3D sur `R^3`, viscosité positive mais sans évolution dans le
test. Le lemme porte sur la pression instantanée induite par un paquet spatial
lisse compact divergence-free; il s'applique à une tranche temporelle d'une
solution suffisamment régulière.

## Échelle des quantités

Le noyau de pression est homogène de degré `-3`; son gradient est de degré
`-4`. À énergie `||v||_2²` fixée, la pression brute distante est donc d'ordre
`R^-3`, tandis que `p(x)-p(0)` sur une boule de rayon fixe est d'ordre `R^-4`.
Sous `v_lambda(x)=lambda v(lambda x)`, la norme `L²` au carré porte le facteur
`lambda^-1` et la géométrie devient `(a,rho,R)/lambda`; le membre droit de la
borne porte exactement le facteur `lambda²` de la pression. Le lemme est
covariant, sans gain critique caché.

## Affirmations ajoutées ou modifiées

- `NS-PRESSURE-TAIL-CENTERED`, `COMPUTATION_ONLY`, passe adverse séparée.
- arête pression du graphe raffinée : queue distante contrôlable à énergie
  fixe, uniformité rescalée et pression proche encore manquantes.

## Preuve / source / calcul

Pour `K_ij=partial_i partial_j(1/(4 pi |z|))`, un calcul direct donne, pour
toute direction `h`,

```text
|h dot nabla K_ij(z)| <= (7/pi)|h||z|^-4.
```

Le théorème des accroissements finis, la distance minimale
`R-a-rho` et `sum_ij |v_i v_j|<=3|v|²` donnent

```text
|p_v(x)-p_v(0)| <= (21/pi) a (R-a-rho)^-4 ||v||_2².
```

Le script `PRESSURE-TAIL-1` vérifie l'ordre sur un moment réalisable
`diag(1,1,0)` avec arithmétique rationnelle exacte après normalisation `4 pi`.

## Écart avec le problème Clay

La borne est instantanée, loin du support et dépend de l'énergie totale du
paquet. Elle ne fournit ni compacité forte du terme quadratique, ni contrôle de
la pression proche, ni constante uniforme dans une normalisation de blow-up.
Elle réduit le verrou : la seule non-localité à grande distance n'est pas
l'obstacle lorsque l'énergie globale rescalée reste uniforme.

## Test adverse et résidu certifié

Test initial : `R=2,4,...,128`, identité

```text
R^4[(R-1)^-3-R^-3]
  = R(3R²-3R+1)/(R-1)^3.
```

Résidu exact zéro. La passe contradictoire séparée confirme le signe du noyau,
la constante conservatrice `21/pi` (une optimisation élémentaire donne même
`18/pi`), l'annulation de jauge, la réalisabilité du moment et la covariance
d'échelle. Elle exige que `w` soit divergence-free et `phi*w` compactement
supporté, ce qui est désormais explicite dans le claim.

## Artefacts mis à jour

Script et protocole `PRESSURE-TAIL-1`, claim centré, graphe, questions et ce
checkpoint.

## État : continuer

Le calcul exact et la dérivation survivent à la passe contradictoire. La queue
lointaine à énergie fixée est rétrogradée comme verrou principal : le prochain
test doit viser l'énergie rescalée et la pression proche.

## Prochaine expérience décisive

Insérer la remise à l'échelle d'une séquence de premier blow-up dans la borne,
suivre `||v_lambda||_2²`, `a`, `rho` et `R`, puis construire une configuration
multi-échelle qui teste l'uniformité plutôt que la seule distance physique.
