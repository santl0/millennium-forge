# DÉCISION DU CYCLE

Réfuter par un test exact de tangence l'invariance de l'orthant modal fini,
puis abandonner la piste des phases modales après trois stratégies
distinctes bloquées. Pivot vers le défaut de Haar pondéré critique.

# ÉQUATION ET TYPE DE SOLUTION

Navier--Stokes incompressible 3D standard sur `R3`, sans frontière, force
nulle, viscosité un :
`partial_t Z=Delta Z-P div(Z tensor Z)`, `div Z=0`. Donnée initiale réelle,
divergence-free et de Schwartz; solution forte/classique locale unique.
Aucune assertion sur une solution faible, ancienne, suitable ou Type I.

# ÉCHELLE DES QUANTITÉS

Sous `Z_lambda(y)=lambda Z(lambda y)`, le numérateur modal
`C_m=<P_mF(Z),mathcal RZ_m>` porte `lambda` et sa dérivée le long du flot
porte `lambda^3`; le signe sortant est préservé. Le prochain observable
`D_H(Z)=integral |(I-A)Z(y)|^2/|y| dy` est invariant sous cette échelle.

# AFFIRMATIONS AJOUTÉES OU MODIFIÉES

- Ajout : `NS-DYNAMIC-MODAL-CONE-OUTWARD-CROSSING`, statut
  `COMPUTATION_ONLY`, revue `adversarial_pass`.
- Modification : `NS-TYPE-I-INSTANTANEOUS-MODAL-SIGN-COUNTEREXAMPLE` pour
  enregistrer la non-invariance dynamique du cycle suivant.
- Registre : 104 affirmations canoniques; échec `FAIL-NS-0099` ajouté.

# PREUVE / SOURCE / CALCUL

Le champ explicite à isotypes `m=1,2,3` vérifie exactement
`C=(8/9,16/9,0)(pi/3)^(3/2)` et
`C'_3=-(1076547/1281280)pi^(3/2)<0`. La théorie locale et la
différentiabilité impliquent `C_3(t)<0` pour tout petit temps positif. La
veille ajoute Nagumo 1942, Brezis 1970, Pavel 1977 et Zgliczyński 2003; le
catalogue atteint 231 sources primaires ou auditées.

# ÉCART AVEC LE PROBLÈME CLAY

Le calcul utilise bien l'équation Clay sur `R3`, mais ne prouve ni
singularité ni régularité globale. Il exclut seulement un orthant construit
avec trois numérateurs modaux pour le semiflot fort local; aucune implication
automatique vers tous les modes, les limites faibles suitable, une solution
ancienne minimale ou un scénario Type I/II.

# TEST ADVERSE ET RÉSIDU CERTIFIÉ

La passe contradictoire a détecté que
`A=Delta Z-(Z dot nabla)Z` n'est pas divergence-free et a invalidé le
premier partage local/pression. Après recomposition : partie locale
`-(675/256)pi^(3/2)`, pression globale
`+(575457/320320)pi^(3/2)`, total strictement négatif. Le certificat exécute
1173 assertions rationnelles exactes, sans quadrature, avec résidus de
divergence, isotypie, parité de Fourier et identités égaux à zéro. Contrôle
pseudo-spectral indépendant : erreur absolue `1.123e-5` sur `C'_3` et
`||div F||_2=5.521e-12`.

# ARTEFACTS MIS À JOUR

- Rapport, reviews formelle/bibliographique/contre-modèle et checkpoint
  `0063`.
- Claim JSON, graphe de dépendances, état de l'art, carte de recherche,
  questions ouvertes, journal supercritique et registre des échecs.
- Expérience reproductible `dynamic-modal-cone`, README et `results.json`.
- Catalogue `sources.json`, audit des sources, contexte, décisions, todo et
  backlog de formalisation.
- Validations : contrat du dépôt, 104 claims, 6 prompts rendus, 231 sources
  uniques, empreintes de preuves et `git diff --check` réussis.

# ÉTAT : CONTINUER

La stratégie modale est abandonnée; le programme Navier--Stokes persistant
continue sur un verrou différent.

# PROCHAINE EXPÉRIENCE DÉCISIVE

Dériver le budget exact du défaut de Haar pondéré critique
`D_H`, pression non locale comprise, puis chercher deux champs de Schwartz
divergence-free donnant des dérivées de signes opposés. Si les deux signes
sont certifiés, abandonner la monotonie universelle et pivoter vers le lemme
minimal de rigidité RSS faible-`L3` à vitesse intermédiaire.
