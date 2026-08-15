## DÉCISION DU CYCLE

Sélectionner l'intégration de la capture Type I contre la forte `L3`
espace–temps, score `19/20`. Réviser le checkpoint 0045 : un moment signé à
la tranche est nécessaire pour conserver cet endpoint précis, mais pas pour
prouver que la limite ancienne est non identiquement nulle. Fermer le raccord
temporel exact puis pivoter vers la dérenormalisation.

## ÉQUATION ET TYPE DE SOLUTION

Sur `R3`, viscosité un, sans force ni frontière, `u` est Leray–Hopf d'énergie
finie, lisse avant son premier temps singulier `T_*`, avec point singulier
fixe `(x_*,T_*)` et borne Type I pointwise faible-`L3`. Les cutoffs translatés
`Z_j` sont classiques et satisfont l'équation renormalisée forcée avec
pression globale de Riesz et drift `+kappa(1+y dot nabla)`; leur limite est
faible adaptée locale pour l'équation renormalisée non forcée. Elle n'est pas
encore une solution ancienne standard identifiée comme mild ou Leray–Hopf.

## ÉCHELLE DES QUANTITÉS

Sous `u_lambda=lambda u(lambda x,lambda²t)`, vitesse, pression et force ont
les amplitudes `lambda`, `lambda²`, `lambda³`; `K_3` et `L3` sont critiques.
Avec `R²=4(T_*-t)/S_w^*(C_MM)`, `d sigma/dt=R^-2` et
`kappa=2/S_w^*(C_MM)`, on a exactement
`d(log R)/d sigma=-kappa` et
`R(sigma_j+s)/R_j=exp(-kappa s)`. Le zoom conserve
`K_3(u;B(x_*,R))=K_3(Ru(x_*+R dot);B_1)`. La masse cubique espace–temps sur
une fenêtre normalisée fixe est donc sans facteur d'échelle caché.

## AFFIRMATIONS AJOUTÉES OU MODIFIÉES

Ajout de `NS-TYPE-I-PERSISTENT-CAPTURE-SPACETIME-NONTRIVIALITY`, statut
`COMPUTATION_ONLY`, portant le registre à 84 claims. Fermeture interne de
`GAP-TYPE-I-CRITICAL-TRACE-PERSISTENCE` pour la seule non-trivialité de la
branche Type I persistante. `FAIL-NS-0081` est restreint aux informations de
tranche; ajout de `FAIL-NS-0082`, qui réfute la nécessité d'un moment signé à
l'ancien endpoint. Le verrou actif devient
`GAP-TYPE-I-DERENORMALIZATION-CLASS`.

## PREUVE / SOURCE / CALCUL

Barker–Prange 2020, théorème 2 avec appendice B, fournit au centre singulier
fixe `K_3(u(t);B(x_*,R(t)))>gamma_w` pour tout temps tardif; `r_0=infinity`
donne ici tous les temps antérieurs. L'horloge mobile et `Q_(L_j)=I` dans
`B_1` transportent la capture sur chaque fenêtre normalisée fixe. Puis
`K_3(f;B_1)^3<=integral_(B_1)|f|³` et la forte `L3_loc` du cycle 0045 donnent
`integral_(J x B_1)|Z|³>=|J|gamma_w³>0`. Aucune source nouvelle : le corpus
reste à 188. La composition du laboratoire ne reçoit pas `PAPER_PROOF`.

## ÉCART AVEC LE PROBLÈME CLAY

La branche suppose un premier blow-up Type I et une borne uniforme
`L-infinity_tL^(3,infinity)_x`, non fournie par l'énergie Clay. La conclusion
est une solution ancienne **renormalisée** non triviale; elle ne conserve ni
un point singulier terminal ni l'ancien endpoint. Il manque la
dérenormalisation distributionnelle, la classe globale exacte, puis une
rigidité générale ancienne faible-`L3`. Type II et le cas périodique ne sont
pas traités; aucun blow-up admissible ni régularité globale n'est obtenu.

## TEST ADVERSE ET RÉSIDU CERTIFIÉ

Le certificat exact passe 417 assertions. Pour une capture de taille
`gamma_j` sur `E_j`, le coût optimal est `|E_j|gamma_j³`; un profil à un
niveau atteint l'égalité. Une tranche isolée et une impulsion triangulaire de
largeur `delta` peuvent disparaître, avec coût exact `gamma³delta/2`.
Centres et échelles mobiles ne réduisent pas le coût tant que la capture reste
dans le même `B_1`. L'horloge et le scaling critique sont aussi vérifiés en
fractions rationnelles. Résidu numérique nul; empreinte du script
`26b93eb4c751d3a366340bae21ddb8803e601a4801b275b45936969109ff42f6`.

## ARTEFACTS MIS À JOUR

Rapport principal, trois revues séparées, script de 417 assertions, claim
JSON, audit de sources, état de l'art, carte, graphe, journal supercritique,
questions ouvertes, échecs, expériences, formalisation, contexte, décisions
et tâches persistantes. Contrat, 84 claims, six prompts, 188 sources, le
certificat dépendant de 401 assertions et le diff Git sont validés.

## ÉTAT : CONTINUER / RÉVISER / ABANDONNER / À REPRENDRE

CONTINUER. La porte de trace du cycle 0045 est révisée : elle reste valide
pour l'ancien endpoint, mais est abandonnée comme préalable à la seule
non-trivialité. La limite renormalisée non nulle est conservée au statut
interne conditionnel. Aucun résultat Clay n'est revendiqué.

## PROCHAINE EXPÉRIENCE DÉCISIVE

Calculer exactement l'inverse du drift avec
`R(s)=exp(-kappa s)`, `dt/ds=R²` et
`u(x,t(s))=R^-1Z((x-x_*)/R,s)`. Vérifier séparément l'équation dans les
distributions, la transformation de la pression, l'inégalité d'énergie
locale, le domaine temporel ancien et la borne faible-`L3`. Abandonner toute
application de rigidité qui exigerait une mildness ou une énergie globale
non héritée.
