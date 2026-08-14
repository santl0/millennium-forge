# DÉCISION DU CYCLE

Retenir le correcteur de Bogovskiĭ sur couronne fixe, score `18/20`, devant
la projection directe de Leray (`16/20`) et la matrice de Gram multi-axe
(`16/20`). Fermer `GAP-MULTIAXIS-SOLENOIDAL-CUTOFF` au niveau statique et
activer `GAP-WEAK-L3-CORE-CAPTURE-AT-PRESINGULAR-SCALE`.

# ÉQUATION ET TYPE DE SOLUTION

Référence : Navier–Stokes incompressible non forcé sur `R3`, viscosité
`nu>0`, donnée lisse compacte divergence-free. Objet effectivement traité :
un champ statique `U in C_c^infinity(R3;R3)`, `div U=0`, `W=curl U`. Le champ
localisé est une donnée lisse admissible sous l'hypothèse explicite d'un
correcteur préservant le support lisse; aucune solution en temps, pression,
force, solution de Leray–Hopf, faible adaptée ou singularité n'est construite.

# ÉCHELLE DES QUANTITÉS

Sous `U_rho(x)=rho U(rho x)` et `W_rho(x)=rho^2W(rho x)`, les quasi-normes
`L^(3,infinity)` et `L^(3/2,infinity)` sont invariantes. Le facteur `R^-1` du
gradient du cutoff est exactement compensé par le volume `O(R^3)` de la
couronne. Le coût est critique, non `o_R(1)`. Pour une couronne mince, la
constante forte de divergence perd au moins `R/h`.

# AFFIRMATIONS AJOUTÉES OU MODIFIÉES

Ajout de `NS-SOLENOIDAL-ANNULAR-CUTOFF` et
`NS-THIN-ANNULUS-DIVERGENCE-COST`, statuts `COMPUTATION_ONLY`, revues
`adversarial_pass`. Correction de `NS-SRC-0111` : ses estimations sont des
majorations constructives, pas une preuve d'impossibilité. Le registre compte
77 claims canoniques.

# PREUVE / SOURCE / CALCUL

La moyenne de `div(chi_RU)` est nulle; le même opérateur de Bogovskiĭ est
interpolé des exposants forts `4/3` et `2` vers
`L^(3/2,infinity)`. Pour `V=chi_RU-B_R(div(chi_RU))`, le curl est recalculé
terme à terme et sa quasi-inégalité conserve le facteur trois. Biot–Savart
faible HLS donne
`q(V)>=C_loc^-1(K_core/K_global)q(U)`. La veille ajoute
`NS-SRC-0176`–`0179` et porte le corpus à 179 sources; `NS-SRC-0177` confirme
un usage Navier–Stokes publié sur une couronne fixe.

# ÉCART AVEC LE PROBLÈME CLAY

Le lemme est cinématique. Il ne sélectionne pas de rayon pré-singulier, ne
contrôle ni `partial_tB_R`, ni diffusion, convection, pression ou force
effective, et ne produit aucune compacité temporelle. Une grande boule
capture trivialement un champ compact; seule une capture uniforme à une
échelle `R(t)->0` liée au temps maximal serait transférable. Le cas périodique
et le passage à une solution ancienne restent non traités.

# TEST ADVERSE ET RÉSIDU CERTIFIÉ

Un plateau divergence-free lisse remis à l'échelle sature le coût du col. Le
certificat exécute 9 167 assertions `Fraction`, seize profils étagés et les
rayons `2^-40` à `2^80` : zéro échec, résidu arithmétique nul, empreinte
`510be7b9354f6e18a188afd87bbec510ecde01d97e187671fe6334c2529ba6e5`.
Le test inf-sup analytique donne `||T||>=c_pR/h` en `L^p` fort. Aucun résidu
PDE, aucune borne d'erreur continuum et aucune minoration faible-Lorentz sur
les couronnes minces ne sont revendiqués.

# ARTEFACTS MIS À JOUR

Deux claims, rapport principal, trois revues, expérience, quatre sources,
watchlist discrète, catalogue et audit bibliographique, état de l'art, carte,
graphe, questions, registre supercritique, échec `FAIL-NS-0076`, backlog
formel, contexte, décisions, todo et ce checkpoint. Les contrôles du contrat,
des 77 claims, des prompts, le certificat exact et `git diff --check` sont
exécutés avec succès.

# ÉTAT : CONTINUER / RÉVISER / ABANDONNER / À REPRENDRE

CONTINUER vers la capture faible-`L3` à échelle pré-singulière. RÉVISER la
conclusion `C_c^infinity` si la réalisation support-lisse n'est pas conservée.
ABANDONNER tout gain fondé sur `R->0` ou `h/R->0` seul. À REPRENDRE pour la
pression, la dynamique, Type I/II, le tore et la formalisation de Bogovskiĭ.

# PROCHAINE EXPÉRIENCE DÉCISIVE

Construire une famille lisse compacte divergence-free à paquets dyadiques
séparés et calculer exactement, pour une gamme de rayons imposée
`R in [c r_*,C r_*]`, le supremum de
`||1_(B(x,R))U||_(3,infinity)/||U||_(3,infinity)`. Soit une hypothèse de
concentration sourcée force une minoration uniforme, soit cette famille
réfute la capture depuis les seules bornes endpoint.
