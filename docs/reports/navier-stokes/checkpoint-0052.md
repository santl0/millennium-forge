## DÉCISION DU CYCLE

Action sélectionnée : dériver l'identité exacte du flux en temps de base et
attaquer son signe par triades, score `19/20`; audit de récurrence BSS/DSS
`17/20`; moment `L1` uniforme du stress `16/20`. Le résultat positif est
l'identité de primitive signée. Les fermetures par valeur absolue et par
signe triadique universel sont abandonnées.

## ÉQUATION ET TYPE DE SOLUTION

Navier--Stokes incompressible standard sur `R3 x (-infinity,T)`, sans bord,
viscosité un et force nulle. Objet principal conditionnel : solution ancienne
faible adaptée locale, représentant `C_w*L^(3,infinity)`, pression globale
`q=R_iR_j(v_iv_j)` et borne uniforme faible-`L3`. Objet adverse : algèbre
Fourier instantanée d'un champ lisse divergence-free sur `T3`, sans
prétention d'ancienneté ni de suitability `R3`.

## ÉCHELLE DES QUANTITÉS

Sous `v_lambda(x,t)=lambda v(lambda x,lambda²t)`, la norme
`L^(3,infinity)` est critique. Pour
`E_a(s;r)=||S(a)[v(r)-S(r-s)v(s)]||_2²`, on a
`E_a^lambda=lambda^(-1)E_(lambda²a)` et
`Phi_a^lambda=lambda Phi_(lambda²a)`; `Phi_a ds` a donc le poids
`lambda^(-1)`. Le contre-test sépare l'échelle absolue de la séparation
relative `|q|²/|k|²=N^(-2)`.

## AFFIRMATIONS AJOUTÉES OU MODIFIÉES

Ajout de `NS-WEAK-L3-BASE-TIME-SIGNED-FLUX-IDENTITY`, statut
`COMPUTATION_ONLY` avec passe adverse, et de
`NS-BACKWARD-SELFSIMILAR-WEAK-L3-LIOUVILLE`, statut `SOURCE_VERIFIED`. Le
premier formalise l'identité et son critère subséquentiel; le second ferme
seulement le profil backward auto-similaire exact faible-`L3`. Le registre
contient 92 claims.

## PREUVE / SOURCE / CALCUL

Le Duhamel lissé donne `partial_sG_a=S(a+r-s)Pdiv(v tensor v)` puis
`partial_sE_a=-Phi_a` et
`E_a(s;r)=integral_s^rPhi_a`. Guevara--Phuc, Chae--Wolf et
Wang--Jiu--Wei ajoutent trois sources publiées (`NS-SRC-0203` à `0205`);
le corpus atteint 205 sources. La veille 2026 conserve Pineau--Vicol comme
prépublication Type I ponctuelle, sans transfert depuis le seul endpoint
Lorentz.

## ÉCART AVEC LE PROBLÈME CLAY

La réduction reste conditionnelle à la branche Type I et à l'ancienne
faible-`L3` construite par les cycles précédents. L'identité de flux est une
reformulation exacte, pas une borne nouvelle. Le Liouville publié exige une
auto-similarité backward exacte; ni DSS faible-`L3` à paramètre arbitraire,
ni récurrence modulée, ni ancienne générale, ni Type II ne sont exclus.
Aucune régularité globale ou singularité admissible Clay n'est obtenue.

## TEST ADVERSE ET RÉSIDU CERTIFIÉ

La valeur absolue donne seulement
`|Phi_a|=O(M^4(r-s)^(-1/2))`, non intégrable au passé. Sur `T3`, la triade
`k=(N,0,0)`, `ell=(-N,0,1)`, `q=(0,0,1)` a une sortie basse indépendante de
`N` et des transferts exacts `(-2ABC,0,+2ABC)` : la phase inverse le signe et
une polarisation admissible annule la sortie. Le script exécute 1058
assertions en rationnels de Gauss, résidu rationnel nul, empreinte
`946bdab1e449ed56a8bbdfe7f7f1d09557e41e2caa8012b055e77f334cc68417`.
Le ledger sur la fenêtre visqueuse vaut `2N^(-2)` et ne prouve aucun transfert
cumulé.

## ARTEFACTS MIS À JOUR

Rapport principal et trois revues du cycle 0052; expérience
`experiments/navier-stokes/infrared-triad`; deux claims; trois sources
primaires et audit bibliographique; état de l'art, questions, carte, graphe
de dépendances, journal supercritique, registre des échecs, backlog formel et
mémoires de gouvernance. Contrat du dépôt, validation des claims, rendu des
prompts, expérience exacte, vérification des empreintes et
`git diff --check` exécutés.

## ÉTAT : CONTINUER / RÉVISER / ABANDONNER / À REPRENDRE

CONTINUER. `FAIL-NS-0088` réfute les deux raccourcis sélectionnés, mais
l'identité exacte localise un verrou plus fin :
`GAP-TYPE-I-ANCIENT-SIGNED-BASE-FLUX-CANCELLATION`. Le cas BSS exact est
reclassé classique publié; produire une stationnarité ou une cancellation à
partir de la même orbite reste ouvert.

## PROCHAINE EXPÉRIENCE DÉCISIVE

Décomposer `Phi_a` en triades Littlewood--Paley, conserver les phases, sommer
les interactions puis intégrer en temps sur une même orbite ancienne. Tester
si la viscosité et une récurrence de blow-down produisent, le long d'une
suite `s_n`, un gain basse fréquence
`integral_(s_n)^rPhi_(a,j)<=C_r2^(epsilon(j-J))` pour `j<=J`, en incluant des
paquets translatés et multi-échelles comme adversaires de tightness.
