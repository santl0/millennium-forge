# DÉCISION DU CYCLE

Sélection de l'exploitation de la dérivée de Bochner fournie par la PDE,
notée `20/20`, devant la phase canonique par matrice de Gram (`17/20`) et la
rigidité RSS extrême/intermédiaire (`14/20`). La variation de
`1/beta_n` est retirée du lemme de collapse. L'inférence de stationnarité
depuis un défaut seulement borné est abandonnée après un contre-exemple PDE
local exact.

# ÉQUATION ET TYPE DE SOLUTION

Navier--Stokes incompressible 3D renormalisé sur `R3 x I`, sans frontière,
viscosité un et drift `kappa(1+y dot nabla)`, `kappa>0`. Le cutoff extérieur
peut produire une force locale uniformément contrôlée qui tend vers zéro; la
limite et le problème Clay sont non forcés. Le cœur emploie des représentants
de Bochner; l'endgame exige une limite suitable `W1,2_loc`, pression de Riesz,
borne globale faible-`L3` et capture persistante.

# ÉCHELLE DES QUANTITÉS

Le temps similaire et `beta_n` sont sans dimension. La borne globale
`L^(3,infinity)` est critique; `W^(-2,4/3)(B_R)` est une topologie locale de
compacité non critique. La constante exacte est
`(C_dot(J,R)+C_r(J,R))/ess inf_J|beta_n|`; aucune uniformité en `R` ou sur un
intervalle ancien infini n'est revendiquée. Le redimensionnement homogène du
terme de force dans ce dual porte le facteur `lambda^(-5/4)`.

# AFFIRMATIONS AJOUTÉES OU MODIFIÉES

Ajout de `NS-TYPE-I-BOCHNER-FAST-ROTATION-COLLAPSE`, statut
`COMPUTATION_ONLY`, revue `adversarial_pass`. Le claim
`NS-TYPE-I-ADIABATIC-FAST-ROTATION-COLLAPSE` est conservé et marqué
`SUPERSEDED`. Le registre contient 98 claims. Ajout de `FAIL-NS-0094`, qui
réfute la stationnarité depuis un défaut seulement borné. Le verrou actif est
`GAP-TYPE-I-CANONICAL-PHASE-DEFECT-BOUND-OR-RSS-RIGIDITY`.

# PREUVE / SOURCE / CALCUL

Dans le même `L1_tW^(-2,4/3)_loc`, l'identité
`beta_n mathcal RZ_n=partial_sZ_n-r_n` se divise presque partout et donne
`mathcal RZ_n->0` dès que `ess inf|beta_n|->infinity`; aucun signe, `W1,1`
ou `BV(1/beta_n)` n'intervient. La convergence distributionnelle donne
`mathcal RZ=0`. La stationnarité suit séparément de
`mathcal A r_n->0`. Simon (`0218`) et Berselli--Fagioli--Spirito (`0219`)
fixent les maillons publiés de compacité/dérivée et de passage suitable; le
corpus atteint 219 sources. Aucun théorème primaire exact couvrant tout le
raccord n'a été trouvé.

# ÉCART AVEC LE PROBLÈME CLAY

Une singularité Clay arbitraire ne fournit actuellement ni phase canonique,
ni minoration uniforme de sa vitesse, ni borne du défaut modulé dans le même
dual, ni annulation de sa moyenne de Haar. Le lemme reste conditionnel au
paquet Type I, ne traite pas Type II, les axes mobiles ou les concentrations
multi-échelles, et n'exclut aucun profil RSS individuel à vitesse
intermédiaire.

# TEST ADVERSE ET RÉSIDU CERTIFIÉ

Le certificat exact vérifie le majorant de Bochner et montre qu'une
stroboscopie fortement compacte hors du stabilisateur a nécessairement
`||partial_sZ_N||_L1=N^2` dans le modèle. Deux compensations séparent borne
de la différence, bornes séparées et contrôle relatif à `beta`; le
stabilisateur rend la vitesse non identifiable. Une solution renormalisée
axisymétrique non stationnaire répétée avec `beta_n=n` réfute en plus la
stationnarité depuis résidu borné. Le script passe 586 assertions
rationnelles, résidu nul, sans PDE numérique ni arrondi, empreinte
`ad8474fa672697a9239a2d8567d122c631818021c6ebc3065695652d3ef7a8a5`.

# ARTEFACTS MIS À JOUR

Rapport principal, trois revues contradictoires, nouveau certificat exact,
deux claims modifiés, deux notices bibliographiques, graphe de dépendances,
état de l'art, questions ouvertes, journaux supercritique/échecs/expériences,
backlog formel et mémoire de gouvernance. Validation réussie : contrat du
dépôt, 98 claims, six prompts, expérience 0058 et régressions 0056--0057,
puis `git diff --check`. Commit scientifique : `cb2c9b0`.

# ÉTAT : CONTINUER / RÉVISER / ABANDONNER / À REPRENDRE

CONTINUER. Le collapse axisymétrique de Bochner est conservé; la
stationnarité depuis résidu borné est abandonnée. Aucune condition terminale
globale du programme n'est atteinte.

# PROCHAINE EXPÉRIENCE DÉCISIVE

Construire une condition de phase calculable depuis le champ total, dériver
son défaut dans `L1_tW^(-2,4/3)_loc` et tester sa borne lorsque la matrice de
Gram dégénère. Mesurer séparément `r_n` et `mathcal A r_n`. Après trois
sélections canoniques réellement distinctes échouant sur ce verrou, consigner
l'obstacle et pivoter vers la rigidité RSS faible-`L3` intermédiaire.
