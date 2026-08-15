# Cycle 0041 — capture faible-L3 au rayon parabolique Type I

Date : 2026-08-15
Statut : `SOURCE_VERIFIED` pour le théorème de Barker–Prange;
`AI_INTERNAL_DERIVATION` pour le raccord à constantes suivies; aucun résultat
Clay.

## Décision adaptative

| Action | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| auditer et composer la capture Lorentz Type I publiée | 3 | 5 | 5 | 5 | **18** |
| construire un contre-profil statique à rayon imposé | 4 | 4 | 5 | 3 | 16 |
| chercher un inverse faible-HLS sans hypothèse Type I | 5 | 2 | 4 | 5 | 16 |

La première action est sélectionnée. La veille montre que le verrou formulé
au cycle 0040 est déjà fermé dans la branche Type I par un théorème publié;
le travail utile consiste à vérifier exactement ses quantificateurs, à
recalculer l'injection vers son hypothèse de Morrey et à isoler ce qui reste
réellement ouvert en Type II.

## Cadre exact

On fixe Navier–Stokes incompressible non forcé, viscosité normalisée à un,
sur `R3` :

```text
partial_t u-Delta u+(u dot nabla)u+nabla p=0,
div u=0.                                             (41.1)
```

Le cadre publié est une solution de Leray–Hopf d'énergie finie, lisse avant
son premier temps singulier fini `T_*`, et un point singulier `(x_*,T_*)`.
Pour une donnée Clay lisse rapidement décroissante, la solution forte locale
et la solution de Leray–Hopf coïncident jusqu'au temps maximal; l'hypothèse
de singularité reste toutefois conditionnelle.

Pour un ensemble mesurable `E`, posons

```text
K_3(f;E)=sup_(s>0) s |E intersection {|f|>s}|^(1/3),
K_3(f)=K_3(f;R3).                                    (41.2)
```

L'hypothèse Type I active est

```text
sup_(0<t<T_*) K_3(u(t)) <= M < infinity.             (41.3)
```

Elle est critique. Elle n'est ni l'énergie de Leray, ni une hypothèse sur la
vorticité, ni une conséquence connue de données Clay arbitraires.

## Lemme élémentaire — faible-L3 vers Morrey local L2

Soit `f in L^(3,infinity)(R3)` et `E` de mesure finie `V`. Avec
`K=K_3(f)`, la fonction de distribution locale vérifie

```text
mu_E(s)<=min(V,K^3/s^3).                             (41.4)
```

La formule des couches et le point de croisement `s_0=K V^(-1/3)` donnent

```text
integral_E |f|^2
 <= integral_0^s0 2sV ds+integral_s0^infinity 2K^3s^-2 ds
 =3K^2V^(1/3).                                      (41.5)
```

En notant `omega_3=4pi/3`, on obtient pour toute boule

```text
r^(-1/2)||f||_(L2(B(x,r)))
 <= C_M K_3(f),
C_M=sqrt(3) omega_3^(1/6).                           (41.6)
```

La constante trois est la constante exacte de cette preuve par seule
distribution : les profils continus de réarrangée `f*(a)=K a^(-1/3)` la
saturent, et les profils rationnels étagés du certificat l'approchent.

## Théorème source — concentration Type I

Barker–Prange, *Localized Smoothing for the Navier–Stokes Equations and
Concentration of Critical Norms Near Singularities*, ARMA 236 (2020),
arXiv:1812.09115v2, prouvent un lissage local depuis une petitesse critique et
en déduisent, par contraposition au point singulier, une concentration au
rayon parabolique. Le théorème 2 est écrit en `L3`; l'appendice B étend le
lissage et la conclusion de concentration à `L^(3,infinity)`.

Sous leur borne Type I de Morrey

```text
sup_x sup_r sup_(T_*-r^2<t<T_*)
r^(-1/2)||u(t)||_(L2(B(x,r))) <= A,                  (41.7)
```

il existe un seuil universel `gamma_w>0` et une durée normalisée
`S_w^*(A)>0` tels que

```text
K_3(u(t);B(x_*,R_A(t))) > gamma_w,
R_A(t)=2 sqrt((T_*-t)/S_w^*(A)),                     (41.8)
```

pour tout `0<t<T_*`. Les constantes `gamma_w,S_w^*` désignent celles de
l'extension Lorentz et peuvent être plus petites que les constantes imprimées
dans l'énoncé `L3`. Lorsque la borne (41.7) vaut à toutes les échelles, le
paramètre extérieur `r_0` de la source peut être pris infini et son temps
initial devient zéro.

L'équation (41.6) montre que (41.3) implique (41.7) avec

```text
A=C_M M.                                             (41.9)
```

Il n'y a donc aucune hypothèse de Morrey silencieuse supplémentaire dans ce
raccord.

## Corollaire actif — fraction du numérateur global

Si un blow-up Type I satisfaisant (41.3) existe, alors, pour

```text
R_M(t)=2 sqrt((T_*-t)/S_w^*(C_M M)),                 (41.10)
```

le centre singulier lui-même vérifie

```text
K_3(u(t);B(x_*,R_M(t))) > gamma_w,
K_3(u(t);B(x_*,R_M(t)))/K_3(u(t)) > gamma_w/M.       (41.11)
```

Le second quotient est licite puisque la singularité exclut `M=0`. Le rayon
tend vers zéro comme `sqrt(T_*-t)` et n'est ni choisi après inspection
arbitraire du champ ni remplacé par une grande boule.

Ainsi `GAP-WEAK-L3-CORE-CAPTURE-AT-PRESINGULAR-SCALE` est fermé sous la borne
Type I globale (41.3). La constante relative se détériore comme `1/M`, ce qui
est attendu et doit rester visible.

## Raccord au cutoff solénoïdal du cycle 0040

La construction locale du cycle 0040 n'a en réalité pas besoin que `u(t)`
soit compact dans tout `R3`. Il suffit que le champ soit lisse dans
`B(x_*,2R_M(t))` et divergence-free : `chi_Ru(t)` est alors compact, donc

```text
integral div(chi_Ru(t))=0.                           (41.12)
```

Le correcteur annulaire produit un champ compact divergence-free `V_t`, égal
à `u(t)` dans le core, avec

```text
K_3(V_t)>=gamma_w.                                  (41.13)
```

Si l'on suppose en plus
`H(t)=||curl u(t)||_(L^(3/2,infinity))<infinity`, le corollaire global du
cycle 0040 donne

```text
q(V_t)>=C_loc^-1 (gamma_w/M) q(u(t)).                (41.14)
```

Cette hypothèse sur `H(t)` n'appartient pas au théorème de concentration et
n'est pas introduite dans le claim de capture. Surtout, `V_t` ne satisfait
pas automatiquement l'équation (41.1).

## Échelle et viscosité

Sous

```text
u_rho(x,t)=rho u(rho x,rho^2t),
p_rho(x,t)=rho^2p(rho x,rho^2t),                    (41.15)
```

`M`, `gamma_w`, le quotient de (41.11) et
`R_M(t)/sqrt(T_*-t)` sont invariants. Pour une viscosité Clay fixée `nu>0`,
la normalisation `s=nu t`, `v=u/nu`, `q=p/nu^2` ramène l'équation à viscosité
un; les constantes doivent alors être retranscrites avec cette normalisation,
et non déclarées indépendantes de `nu` sans calcul.

## Test adverse décisif

Pour `q>1` rationnel et `N>=1`, considérons une distribution étagée de volume
un, amplitudes `a_k=q^k` et volumes de couches

```text
m_k=q^(-3k)-q^(-3(k+1)), 0<=k<N,
m_N=q^(-3N).                                         (41.16)
```

Les volumes cumulés au-dessus de `a_k` valent exactement `q^(-3k)`, donc

```text
K_3=1,
||f||_2^2
 =(1+q^-1+q^-2)(1-q^-N)+q^-N <3.                   (41.17)
```

En faisant d'abord `N->infinity`, puis `q->1`, le membre de droite tend vers
trois. Le certificat doit vérifier (41.16)–(41.17), les fonctions de
distribution complètes, les remises à l'échelle `V=beta R^3` et la nécessité
logique de la borne globale `M` pour passer d'une concentration absolue à une
fraction relative.

Ce test ne simule pas Navier–Stokes. Il certifie seulement l'interface
fonctionnelle (41.5), qui est la seule dérivation quantitative nouvelle dans
le raccord au théorème publié.

Le certificat en arithmétique rationnelle exécute `1346` assertions exactes.
Son cas extrême `m=128,N=2048` donne
`||f||_2^2=2.976804041858` et un écart exact à trois affiché
`0.023195958142`. Son empreinte SHA-256 est
`8337e0aced23e4bd815f1d759e226a41a8867c4de826932dcf261aa3f051de76`.

## Passe contradictoire interne

1. **Norme forte contre norme faible.** La concentration `L3` du théorème 2
   n'implique pas à elle seule une concentration faible-`L3`; le raccord cite
   explicitement l'appendice B.
2. **Type I exact.** La borne globale faible-`L3` n'est pas identifiée sans
   preuve à la borne Morrey de la source; (41.5)–(41.9) fournissent ce passage.
3. **Centre.** La boule est centrée au point singulier `x_*`, pas en un centre
   choisi par un pigeonhole statique.
4. **Temps.** Le rayon est calculé depuis `T_*-t`; un rayon arbitrairement
   petit à temps fixé ne convient pas.
5. **Relatif.** `gamma_w` est une minoration absolue. Le facteur relatif
   `gamma_w/M` utilise séparément la borne globale (41.3).
6. **Type II.** Si `K_3(u(t))` n'est pas uniformément borné, (41.11) ne donne
   aucune fraction positive uniforme, même si une concentration absolue
   subsiste.
7. **Notion de solution.** Le théorème source traite des solutions de
   Leray–Hopf/local energy avec premier temps singulier; il ne s'applique pas
   à un champ statique arbitraire.
8. **Support.** Le cutoff annulaire s'étend aux champs localement lisses parce
   que `chi_Ru` est compact; l'absorption globale par Biot–Savart demande des
   hypothèses globales séparées.
9. **PDE localisée.** Le champ `V_t` est une donnée test compacte, pas la
   restriction d'une solution non forcée. Pression, dérivée temporelle et
   commutateurs restent à calculer.
10. **Représentant temporel.** L'hypothèse (41.3) est ici pointwise. Si elle
    n'était donnée que comme borne `L^infinity_t` essentielle, (41.11) ne
    vaudrait a priori que presque partout sans choix justifié d'un
    représentant temporel.

## Résultat et prochain verrou

La capture du numérateur au rayon pré-singulier est un maillon **déjà publié
dans la branche Type I**, et le raccord quantitatif donne la fraction explicite
`gamma_w/M`. Le cycle ne revendique donc pas un nouveau théorème de
concentration; il corrige la carte de recherche et évite une expérience
statique moins informative.

Le verrou se scinde maintenant :

```text
Type I faible-L3
  --> core capture publié
  --> cutoff solénoïdal statique disponible
  -?-> équation localisée uniforme et rigidité;

Type II faible-L3
  --> aucune borne M
  -?-> capture relative après normalisation, profil minimal ou autre quantité.
```

Le prochain cycle doit choisir entre le raccord dynamique Type I du champ
`V_t` et une formulation de concentration-compacité Type II. Le premier est
plus tractable : calculer exactement l'équation satisfaite par
`chi_Ru-B_R(grad chi_R dot u)` avec `R=R_M(t)`, y compris le terme
`R'(t)`, la pression et toutes les puissances de `T_*-t`.
