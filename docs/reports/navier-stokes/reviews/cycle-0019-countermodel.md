# Cycle 0019 — contre-modèles de synchronisation distribution–analyticité

Date : 2026-08-14.

Type de revue : **passe contradictoire par la même famille de modèle que
l'analyse principale; ce document n'est pas une revue externe indépendante**.

Source primaire auditée : Zoran Grujić,
[arXiv:2607.08866v2](https://arxiv.org/abs/2607.08866v2), version du 13 juillet
2026, équations (49)–(58) et lignes 328–421.

## Verdict

La synchronisation finale est **réparable**, mais elle n'est pas certifiée par
la simple juxtaposition des trois asymptotiques

\[
 |V_s|\lesssim A_s^{-3}(\log A_s)^{-3},
 \qquad
 \rho_s\gtrsim\nu A_s^{-1},
 \qquad
 \tau_t\gtrsim\nu A_t^{-2}.
 \tag{1}
\]

Il faut que ces estimations soient vraies au **même temps \(s\)**, au niveau
relatif \(\beta=\theta A_s\), avec des constantes et des seuils uniformes.
Des systèmes rationnels explicites ci-dessous satisfont chaque loi sur des
suites convergeant vers \(T^*\), ou à des niveaux admissibles séparés, sans
qu'aucun couple temps–niveau commun existe.

Trois défauts précis sont trouvés dans la rédaction du manuscrit.

1. Le théorème d'analyticité donne une fenêtre garantie à partir de \(t\), pas
   automatiquement un « maximal local analyticity time » utilisable comme
   temps \(s<T^*\). Il faut une dichotomie : soit la fenêtre traverse \(T^*\)
   et le temps prétendument singulier est déjà prolongé, soit un temps
   parabolique prescrit \(s=t+\tau_t<T^*\) est disponible.
2. (49) emploie \(\log\lambda\), tandis que (55) emploie
   \(\log(e+\lambda)\). Le remplacement est licite aux grands niveaux après
   changement de constante et seuil; il ne l'est pas avec la même constante
   par simple substitution.
3. La propriété issue du volume s'améliore quand le rayon **augmente**. Une
   borne \(r_s\leq c_4/(A_s\log A_s)\) ne certifie pas qu'un rayon arbitraire
   plus petit est sparse. (56) devient correcte seulement si \(r_s\) est
   défini comme le rayon sûr construit depuis le majorant volumique.

En revanche, l'algèbre des deux branches du critère harmonique, (57)–(58), est
correcte si le **même** paramètre \(M\) est utilisé pour le seuil de
superniveau et pour le majorant holomorphe. Un système rationnel la sature
exactement. Employer deux constantes \(M\) différentes peut faire dépasser
le coefficient final au-dessus de \(1\).

## 1. Paramètres distincts

Pour éviter les collisions de notation, posons

\[
 A_t=\|u(t)\|_\infty,
 \qquad
 \theta=\frac1{2M},
 \qquad
 \beta_s=\theta A_s,
 \tag{2}
\]

où \(M>1\) est le paramètre du théorème d'analyticité et du maximum
harmonique. On réserve

\[
 C_V
 \tag{3}
\]

à la constante de distribution de vitesse, et

\[
 \tau_t=\frac{a(M)\nu}{A_t^2},
 \qquad
 \rho(t,\tau_t)=b(M)(\nu\tau_t)^{1/2}
 =c_A(M)\frac{\nu}{A_t}
 \tag{4}
\]

à une fenêtre et un rayon analytiques garantis. Avec les constantes de la
ligne 368–371, on peut prendre
\(a(M)=1/c_1(M)\) et
\(c_A(M)=1/[c_2(M)\sqrt{c_1(M)}]\), éventuellement avec une marge stricte.

La constante \(C_V\), les seuils de (49), \(a(M)\) et \(c_A(M)\) doivent tous
être indépendants des temps d'échappement sélectionnés.

## 2. Système rationnel à temps disjoints

Voici un falsificateur des quantificateurs faibles « il existe des temps
arbitrairement proches où chaque asymptotique vaut ». Fixons \(T^*=1\) et,
pour \(n\geq1\),

\[
 d_n=1-\frac1{4n},
 \qquad
 a_n=1-\frac1{4n+2}.
 \tag{5}
\]

Les deux suites sont rationnelles, disjointes et convergent vers \(1\). Au
temps de distribution \(d_n\), posons

\[
 A(d_n)=2^n,
 \qquad
 L_n=n,
 \qquad
 |V_{d_n}|=2^{-3n}n^{-3},
 \qquad
 r_{d_n}=2^{-n}n^{-1}.
 \tag{6}
\]

Ici \(L_n=\log_2 A(d_n)\); changer de base logarithmique ne fait que modifier
une constante fixe. Les lois de volume et de rayon sont satisfaites avec
rapport exactement \(1\).

Au temps analytique \(a_n\), posons

\[
 A(a_n)=2^n,
 \qquad
 \rho_{a_n}=2^{-n},
 \qquad
 \tau_{a_n}=2^{-2n}.
 \tag{7}
\]

Les lois analytique et temporelle sont elles aussi satisfaites avec rapport
exactement \(1\). Pourtant,

\[
 \{d_n:n\geq1\}\cap\{a_n:n\geq1\}=\varnothing.
 \tag{8}
\]

Aucun temps ne porte simultanément les données de (6) et (7). Ce système ne
réfute pas une estimation de distribution réellement uniforme sur tout
\((T^*-\varepsilon,T^*)\), combinée à un théorème analytique applicable à
chaque temps d'échappement. Il prouve exactement que des asymptotiques
séquentielles séparées ne suffisent pas.

## 3. Système à seuil de niveau non uniforme

Même à un temps commun, le niveau relatif peut manquer le régime où (49) est
valable. Prenons rationnellement

\[
 A_n=2^n,
 \qquad
 \theta=\frac14,
 \qquad
 \beta_n=\theta A_n=2^{n-2},
 \qquad
 \Lambda_n=A_n^2=2^{2n}.
 \tag{9}
\]

Supposons qu'à l'instant \(s_n\), la queue de distribution possède la bonne
forme pour tout niveau \(\lambda\geq\Lambda_n\), mais sans seuil uniforme en
\(n\). Alors

\[
 \beta_n<\Lambda_n
 \qquad(n\geq1),
 \tag{10}
\]

et (49) est inutilisable au niveau de (50), bien que \(A_n\to\infty\) et que
chaque temps possède une asymptotique de hauts niveaux.

La réparation est exacte : il faut un même \(\Lambda_V\) tel que (49) soit
vraie pour tous les temps considérés et tous les niveaux
\(\lambda\geq\Lambda_V\). Puis sélectionner l'échappement assez tard pour
que

\[
 \theta A_s\geq\Lambda_V.
 \tag{11}
\]

Le cycle 0016 a déjà montré le défaut analogue pour le petit-volume de la
réarrangée.

## 4. Fenêtre analytique : dichotomie temporelle

Fixons encore \(T^*=1\), \(A_n=2^n\), \(\nu=a(M)=1\). La fenêtre parabolique
est rationnelle :

\[
 \tau_n=A_n^{-2}=4^{-n}.
 \tag{12}
\]

Deux suites de temps d'ancrage illustrent les deux cas.

### Fenêtre intérieure

Pour

\[
 t_n^-=1-2\,4^{-n},
 \tag{13}
\]

le temps prescrit

\[
 s_n^-=t_n^-+\tau_n=1-4^{-n}<T^*
 \tag{14}
\]

est disponible. C'est à ce temps précis qu'il faut appliquer simultanément
la distribution et l'analyticité.

### Fenêtre traversant le temps supposé singulier

Pour

\[
 t_n^+=1-\frac12\,4^{-n},
 \tag{15}
\]

on a

\[
 t_n^++\tau_n=1+\frac12\,4^{-n}>T^*.
 \tag{16}
\]

Il n'existe pas de temps terminal \(s=t_n^++\tau_n<T^*\). Mais si le théorème
local fournit réellement la solution sur cette fenêtre à partir de la tranche
classique \(u(t_n^+)\), il prolonge déjà la solution au-delà de \(T^*\). Ce
n'est pas un blocage; c'est la première branche positive de la preuve.

La rédaction sûre est donc :

1. choisir \(\tau_t\) explicitement dans la fenêtre garantie, plutôt que le
   « maximal local analyticity time » non quantifié ;
2. si \(t+\tau_t\geq T^*\), conclure par prolongement local ;
3. sinon poser \(s=t+\tau_t<T^*\) et continuer le critère géométrique.

Une fraction stricte de \(\tau_t\) peut être utilisée pour éviter toute
question d'endpoint dans le domaine holomorphe; elle ne change que
\(c_A(M)\).

## 5. Rayon volumique : sens exact

Pour \(\delta=3/4\),

\[
 \delta|B_r|=\frac34\frac{4\pi}{3}r^3=\pi r^3.
 \tag{17}
\]

Si \(m_s=|V_s|\), la condition suffisante obtenue du seul volume global est

\[
 r^3\geq\frac{m_s}{\pi}.
 \tag{18}
\]

Le sens est donc \(r\geq(m_s/\pi)^{1/3}\). Une boule centrale montre que ce
seuil universel est optimal.

Supposons disponible le majorant synchronisé

\[
 m_s\leq\mathcal M_s:=
 \frac{C_V}
 {\theta^3A_s^3[\log(e+\theta A_s)]^3}.
 \tag{19}
\]

Le choix constructif correct est

\[
 R_s:=\left(\frac{\mathcal M_s}{\pi}\right)^{1/3}
 =\frac{(C_V/\pi)^{1/3}}
 {\theta A_s\log(e+\theta A_s)}.
 \tag{20}
\]

Alors, pour chaque centre \(x_0\),

\[
 |V_s\cap B_{R_s}(x_0)|
 \leq m_s\leq\mathcal M_s
 =\pi R_s^3
 =\delta|B_{R_s}|.
 \tag{21}
\]

Le même rayon est uniforme en \(x_0\); la direction linéaire sparse obtenue
ensuite peut dépendre de \(x_0\).

### Contre-test du mauvais sens

Prenons une masse \(m=\pi/8\), donc un rayon sûr

\[
 R_{safe}=(m/\pi)^{1/3}=1/2.
 \tag{22}
\]

Réalisons cette masse par une boule concentrique de rayon
\(r_0=(3/32)^{1/3}\). Comme

\[
 (1/4)^3=1/64<3/32<(1/2)^3=1/8,
 \tag{23}
\]

la boule \(B_{1/4}\) est entièrement remplie : sa densité vaut \(1\), et elle
n'est pas \(3/4\)-sparse. Pourtant \(1/4\leq R_{safe}\).

Ainsi (56), lue comme « tout \(r_s\) inférieur au membre droit est sparse »,
est fausse. Lue comme une borne supérieure sur le **rayon sûr construit**
(20), elle est correcte. Il faut ensuite vérifier

\[
 R_s\leq\rho_s,
 \tag{24}
\]

de sorte que l'intervalle admissible de rayons
\([R_{safe},\rho_s]\) ne soit pas vide.

## 6. Synchronisation exacte des constantes

Depuis le temps \(t\), le théorème analytique donne au temps prescrit \(s\)

\[
 A_s\leq MA_t,
 \qquad
 \rho_{actual}(s)\geq c_A(M)\frac{\nu}{A_t}.
 \tag{25}
\]

Si \(t\) est un temps d'échappement et \(s<T^*\), alors \(A_s>A_t\), donc

\[
 \rho_{actual}(s)
 \geq c_A(M)\frac{\nu}{A_t}
 >c_A(M)\frac{\nu}{A_s}
 =:\rho_s.
 \tag{26}
\]

Le remplacement de \(A_t\) par \(A_s\) à la ligne 390 a donc le bon sens.

En combinant (20) et (26), une condition suffisante explicite pour (24) est

\[
 \log(e+\theta A_s)
 \geq
 \frac{(C_V/\pi)^{1/3}}
 {\theta c_A(M)\nu}.
 \tag{27}
\]

La synchronisation complète exige simultanément

\[
 \begin{cases}
 t\in(T^*-\varepsilon,T^*)\text{ est un temps d'échappement},\\
 s=t+\tau_t<T^*,\\
 A_t<A_s\leq MA_t,\\
 \theta A_s\geq\Lambda_V,\\
 \text{(27)},\\
 \text{les constantes }C_V,\Lambda_V,c_A(M)\text{ sont uniformes.}
 \end{cases}
 \tag{28}
\]

Si \(A_t\to\infty\) le long des temps d'échappement et si toutes les
constantes sont uniformes, les deux conditions portant sur \(A_s\) finissent
par être vraies. Sans divergence de \(A_t\) ou sans seuil uniforme, les
asymptotiques seules ne fournissent pas (28).

## 7. Passage \(\log\lambda\) vers \(\log(e+\lambda)\)

L'équation (49) est écrite avec \(\log\lambda\), alors que (55) utilise
\(\log(e+\lambda)\). Pour \(x\geq e\),

\[
 \log x\leq\log(e+x)leq\log(2x)leq2\log x.
 \tag{29}
\]

Ainsi

\[
 \frac1{(\log x)^3}
 \leq
 \frac8{[\log(e+x)]^3}.
 \tag{30}
\]

Une borne avec \((\log x)^{-3}\) implique donc une borne avec
\([\log(e+x)]^{-3}\) après multiplication de la constante par \(8\). Comme
\(\log(e+x)>\log x\), employer le même \(C_V\) produirait un membre droit
plus petit et n'est pas justifié.

Les deux logarithmes doivent en outre porter sur un rapport d'amplitudes sans
dimension. Une référence \(A_*>0\) change le seuil et la constante de (27).

## 8. Deux branches du critère harmonique : certificat rationnel

La constante réelle \(h^*\) de (53) n'est pas rationnelle. Pour tester
l'algèbre indépendamment de sa valeur géométrique, choisissons

\[
 h=\frac13,
 \qquad
 M=\frac54,
 \qquad
 \theta=\frac1{2M}=\frac25.
 \tag{31}
\]

Ces nombres satisfont exactement

\[
 \frac12h+(1-h)M
 =\frac16+\frac23\frac54=1.
 \tag{32}
\]

Prenons \(A_t=20\) et le cas extrême \(A_s=MA_t=25\).

### Branche \(0\in K\)

Le seuil sur le vide donne

\[
 |u(x_0,s)|\leq\theta A_s
 =\frac25\cdot25=10=\frac12A_t.
 \tag{33}
\]

Cette estimation est correcte. À un point fixé, elle ne « contredit » pas à
elle seule la définition globale d'un temps d'échappement; elle constitue la
borne pointwise de cette branche. La contradiction arrive après traitement
de chaque \(x_0\) et prise du supremum.

### Branche \(0\notin K\)

Avec une mesure harmonique au moins \(h\), le cas défavorable sature

\[
 h\theta A_s+(1-h)MA_t
 =\frac13\cdot10+rac23\cdot25
 =20=A_t.
 \tag{34}
\]

L'algèbre de (57)–(58) est donc exacte. Une mesure harmonique plus grande ne
détériore pas la borne, car le seuil sur \(K\), \(\theta A_s\leq A_t/2\), est
strictement inférieur au majorant du cercle \(MA_t\).

### Dépendance cachée : le même \(M\)

Conservons \(h=1/3\), \(M_H=5/4\) pour définir
\(\theta=1/(2M_H)=2/5\), mais supposons que le majorant holomorphe disponible
soit seulement \(M_A=3/2\). Le coefficient défavorable devient

\[
 M_A\,[h\theta+(1-h)]
 =\frac32\left(\frac{2}{15}+\frac23\right)
 =\frac65>1.
 \tag{35}
\]

La branche harmonique ne ferme plus. Le choix du manuscrit d'appliquer le
théorème 7.3 avec exactement le \(M\) défini par (53) est donc indispensable.
Les constantes \(c_1(M),c_2(M)\), et par suite \(c_A(M)\), doivent être
recalculées avec ce même paramètre.

## 9. Autres dépendances et endpoints

1. **Amplitude non bornée.** Un premier temps singulier pour une théorie
   locale \(L^\infty\) doit fournir des temps d'échappement avec
   \(A_t\to\infty\). Cette implication doit être citée ou dérivée de la borne
   de temps d'existence locale; elle ne découle pas de la seule notation
   \(T^*\).
2. **Temps d'échappement.** La stricte propriété
   \(A_s>A_t\) est utilisée dans (26) et à la contradiction finale. Une suite
   de simples pics ou de temps où \(A_t\) est grand ne suffit pas.
3. **Domaine analytique ouvert.** Pour appliquer le maximum harmonique sur
   un disque de rayon égal au bord de la bande analytique, il faut contrôler
   les limites au bord. Un choix \(R_s<(1-\eta)\rho_{actual}\) évite la
   question au prix d'une constante arbitrairement proche.
4. **Point arbitraire.** La direction sparse et le vecteur de projection
   \(e=u(x_0,s)/|u(x_0,s)|\) dépendent de \(x_0\). C'est compatible avec une
   preuve pointwise, pas avec le choix d'une direction globale unique.
5. **Champ harmonique constant.** Comme au cycle 0016, la distribution de
   vitesse et le superniveau relatif exigent une normalisation de Biot–Savart
   ou de la vitesse à l'infini. Cette dépendance est amont de (49), mais elle
   affecte directement (50).
6. **Cas \(V_s=\varnothing\).** Le rayon réel minimal est nul, mais le maximum
   harmonique demande un rayon positif. Le choix depuis le majorant
   \(\mathcal M_s>0\) dans (20) évite cette dégénérescence.

## 10. Ce qui survit

| Maillon | Verdict | Réparation ou condition |
|---|---|---|
| queue (49) au niveau \(\theta A_s\) | survit conditionnellement | seuil uniforme \(\theta A_s\geq\Lambda_V\), changement de constante logarithmique |
| fenêtre analytique | survit avec dichotomie | temps prescrit \(\tau_t\), soit prolongement, soit \(s<T^*\) |
| remplacement \(A_t\) par \(A_s\) dans le rayon | sens correct | utilise strictement \(A_s>A_t\) |
| (55) vers rayon sparse | rédaction ambiguë | définir \(R_s=(\mathcal M_s/\pi)^{1/3}\); ne pas choisir un rayon arbitrairement plus petit |
| comparaison rayon sparse/analytique | survit | condition exacte (27), constantes uniformes |
| branche \(0\in K\) | survit | borne pointwise \(A_t/2\), pas contradiction isolée |
| branche \(0\notin K\) | survit et sature | même \(M\) dans \(\theta\), analytique et identité convexe |
| paramètres \(M_H\ne M_A\) | peut échouer | témoin rationnel (35) |
| conclusion simultanée | non obtenue d'asymptotiques séparées | quantificateurs communs (28) indispensables |

## 11. Certificat standard-library exact

Le script suivant vérifie avec `fractions.Fraction` les systèmes de temps et
niveaux disjoints, la dichotomie temporelle, le mauvais sens du rayon et les
deux branches harmoniques. Le logarithme est encodé dans la première famille
par \(L_n=\log_2(2^n)=n\), exactement rationnel.

```python
from fractions import Fraction as F


# 1. Two rational time sequences approaching T*=1 but never intersecting.
D = {F(1) - F(1, 4 * n) for n in range(1, 65)}
A = {F(1) - F(1, 4 * n + 2) for n in range(1, 65)}
assert D.isdisjoint(A)

for n in range(1, 33):
    amp = F(2 ** n)
    log2_amp = F(n)
    volume = 1 / (amp ** 3 * log2_amp ** 3)
    sparse_radius = 1 / (amp * log2_amp)
    analytic_radius = 1 / amp
    time_window = 1 / amp ** 2
    assert volume * amp ** 3 * log2_amp ** 3 == 1
    assert sparse_radius * amp * log2_amp == 1
    assert analytic_radius * amp == 1
    assert time_window * amp ** 2 == 1


# 2. A non-uniform distribution threshold always misses the relative level.
theta_level = F(1, 4)
for n in range(1, 33):
    amp = F(2 ** n)
    beta = theta_level * amp
    threshold = amp ** 2
    assert beta < threshold


# 3. Exact time-window dichotomy.
for n in range(1, 20):
    tau = F(1, 4 ** n)
    t_inside = F(1) - 2 * tau
    t_crossing = F(1) - tau / 2
    assert t_inside + tau < 1
    assert t_crossing + tau > 1


# 4. Radius-direction countertest, with volumes measured in units of pi.
mass_over_pi = F(1, 8)
R_safe = F(1, 2)
assert R_safe ** 3 == mass_over_pi
small = F(1, 4)
physical_ball_radius_cube = F(3, 32)
assert small ** 3 < physical_ball_radius_cube < R_safe ** 3
# Hence B_small is filled (density 1) although small <= R_safe.


# 5. Rational harmonic-measure algebra.
h = F(1, 3)
M = F(5, 4)
theta = 1 / (2 * M)
At = F(20)
As = M * At
assert theta == F(2, 5)
assert h / 2 + (1 - h) * M == 1

branch_void = theta * As
branch_core = h * theta * As + (1 - h) * M * At
assert branch_void == At / 2
assert branch_core == At

# Mismatch between harmonic locking and analytic growth breaks closure.
M_analytic = F(3, 2)
bad_coefficient = M_analytic * (h * theta + (1 - h))
assert bad_coefficient == F(6, 5) > 1

print("disjoint time/level synchronization countermodels: PASS")
print("analytic-window dichotomy and radius-direction gate: PASS")
print("two harmonic branches and M-mismatch residual: PASS")
```

Commande de reproduction : extraire le bloc et exécuter `python -` depuis la
racine du dépôt. Dépendances : bibliothèque standard uniquement. Graine :
aucune. Toutes les égalités et tous les résidus sont rationnels exacts.

## 12. Obligations falsifiables

```json
{
  "cycle": "0019",
  "review_independence": "same-model-family adversarial pass; not external independent review",
  "source": "arXiv:2607.08866v2, equations (49)-(58)",
  "claims": [
    {
      "id": "NS-C0019-SEPARATE-ASYMPTOTICS",
      "statement": "separate asymptotic sequences automatically synchronize",
      "status": "REFUTED",
      "witness": "rational disjoint time sets (5)-(8)"
    },
    {
      "id": "NS-C0019-NONUNIFORM-LEVEL",
      "statement": "a time-dependent high-level threshold eventually contains theta A_s",
      "status": "REFUTED",
      "witness": "beta_n=2^(n-2), Lambda_n=2^(2n)"
    },
    {
      "id": "NS-C0019-RADIUS-DIRECTION",
      "statement": "every radius below the cube-root volume scale is sparse",
      "status": "REFUTED",
      "witness": "central ball of mass pi/8"
    },
    {
      "id": "NS-C0019-HARMONIC-BRANCHES",
      "statement": "both harmonic branches close with the locked common M",
      "status": "PROVED_ALGEBRAICALLY",
      "sharpness": "core branch attains coefficient 1"
    },
    {
      "id": "NS-C0019-M-MISMATCH",
      "statement": "different harmonic and analytic M constants are harmless",
      "status": "REFUTED",
      "exact_bad_coefficient": "6/5"
    }
  ],
  "pde_scope": "scalar synchronization systems and harmonic algebra; no Navier-Stokes simulation or blow-up solution is constructed",
  "decision": "REVISE"
}
```

## Conclusion contradictoire

Le verrou de (49)–(58) n'est pas l'identité convexe harmonique : elle est
exacte et saturée. Le verrou est la portée commune des quantificateurs.
L'argument devient rigoureux si l'on produit un seuil de distribution
uniforme, choisit un temps analytique prescrit avec la dichotomie de
prolongement, définit le rayon sparse par (20), puis vérifie l'unique
condition quantitative (27) avec le même \(M\). L'inégalité (56) a le mauvais
sens seulement sous la lecture « tout plus petit rayon convient »; comme
borne supérieure sur le rayon sûr explicitement construit, elle est valide.
