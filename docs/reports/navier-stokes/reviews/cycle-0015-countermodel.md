# Cycle 0015 — contre-modèles pour l'inversion réarrangée–distribution

Date de la passe adverse : 2026-08-14.

Source primaire auditée : Zoran Grujić, [arXiv:2607.08866v2](https://arxiv.org/abs/2607.08866v2), version du 13 juillet 2026, en particulier les équations (47)–(49) et les lignes 323–335 de la version HTML.

## Verdict

La phrase précédant (48), selon laquelle

\[
 \lambda=u^*(\mu_f(\lambda))
 \quad\text{« par définition »},
 \tag{1}
\]

est **fausse en général**, même pour une fonction bornée à support compact sur
\(\mathbb R^3\). Ici il faut lire \(f=|u|\),
\(\mu_f(\lambda)=|\{f>\lambda\}|\), et \(f^*\) pour la réarrangée décroissante
de \(f\). Les plateaux de niveau et les lacunes dans l'image essentielle de
\(f\) rendent l'inégalité stricte.

Le passage de (47) à une borne de la forme (49) n'est toutefois **pas réfuté**
par ce défaut. Il admet la réparation exacte suivante. Si, pour des constantes
uniformes \(C>0\) et \(v_0>0\),

\[
 f^*(v)\leq \frac{C v^{-1/3}}{\log(e/v)}
 \qquad(0<v\leq v_0),
 \tag{2}
\]

alors, pour \(y=\lambda/C\geq e\) assez grand pour que

\[
 s_\lambda:=
 \frac{1}{27y^3(\log y)^3}
 =\frac{C^3}{27\lambda^3(\log(\lambda/C))^3}
 \leq v_0,
 \tag{3}
\]

on a rigoureusement

\[
 \mu_f(\lambda)\leq s_\lambda.
 \tag{4}
\]

La constante principale \(C^3/27\) est asymptotiquement optimale pour
l'enveloppe exacte de (2). Ainsi, le \(C_u\) non explicité de (49) doit au
minimum absorber le cube de la constante de (47), le facteur \(1/27\), le
seuil de petit volume et toute normalisation dimensionnelle. La conclusion
(49) est donc **réparable comme inégalité aux grands niveaux**, mais la chaîne
écrite avec « \(=\) » et « \(\approx\) » ne constitue pas telle quelle une
preuve à constantes et quantificateurs suivis.

## 1. Conventions exactes

Soit \((X,m)\) un espace mesuré et \(f:X\to[0,\infty)\) mesurable, finie
presque partout, avec
\(\mu_f(a)<\infty\) pour tout niveau \(a>0\). On fixe les conventions

\[
 \mu_f(a)=m\{x:f(x)>a\},
 \qquad
 f^*(s)=\inf\{a\geq0:\mu_f(a)\leq s\},\quad s>0.
 \tag{5}
\]

La fonction \(a\mapsto\mu_f(a)\) est décroissante et continue à droite,
car \(\{f>a_n\}\uparrow\{f>a\}\) lorsque \(a_n\downarrow a\). La relation
de pseudo-inverses correcte est

\[
 f^*(s)>a
 \quad\Longleftrightarrow\quad
 \mu_f(a)>s.
 \tag{6}
\]

De façon équivalente,

\[
 f^*(s)\leq a
 \quad\Longleftrightarrow\quad
 \mu_f(a)\leq s.
 \tag{7}
\]

En prenant \(s=\mu_f(a)\), (7) ne donne que

\[
 f^*(\mu_f(a))\leq a.
 \tag{8}
\]

Si \(s=\mu_f(a)>0\) et si
\(f^*(s-)=\lim_{r\uparrow s}f^*(r)\), alors (6) donne le crochet exact

\[
 f^*(s)\leq a\leq f^*(s-).
 \tag{9}
\]

Une égalité dans (8) exige des hypothèses supplémentaires, par exemple une
inversion sans plateau ni lacune au niveau considéré. Elle ne fait pas partie
de la définition générale d'une réarrangée.

## 2. Contre-profil fini à deux plateaux

Prenons deux ensembles mesurables disjoints \(E_5,E_2\subset\mathbb R^3\)
de volumes respectifs \(3\) et \(4\), et

\[
 f=5\mathbf 1_{E_5}+2\mathbf 1_{E_2}.
 \tag{10}
\]

Avec des superniveaux stricts,

\[
 \mu_f(a)=
 \begin{cases}
 7,&0\leq a<2,\\
 3,&2\leq a<5,\\
 0,&a\geq5,
 \end{cases}
 \qquad
 f^*(s)=
 \begin{cases}
 5,&0<s<3,\\
 2,&3\leq s<7,\\
 0,&s\geq7.
 \end{cases}
 \tag{11}
\]

Au niveau \(a=4\),

\[
 \mu_f(4)=3,
 \qquad
 f^*(\mu_f(4))=f^*(3)=2<4,
 \tag{12}
\]

tandis que \(f^*(3-)=5>4\). Le crochet (9) est saturé de part et d'autre,
mais l'égalité (1) échoue.

Ce contre-exemple vit sur l'espace de Lebesgue sans atome. L'« atome » en
cause est un atome de la **loi des valeurs**, c'est-à-dire un plateau de
mesure positive. Le même phénomène apparaît a fortiori sur un espace mesuré
atomique abstrait. Un point de Dirac n'est en revanche pas une fonction de
vitesse mesurable admissible sur \(\mathbb R^3\) et n'est pas nécessaire à
la réfutation.

Changer silencieusement \(\{f>a\}\) en \(\{f\geq a\}\) ne répare pas le
problème. Pour (10), au niveau \(a=2\),
\(|\{f\geq2\}|=7\) et \(f^*(7)=0\), tandis que la convention stricte donne
\(\mu_f(2)=3\) et \(f^*(3)=2\). La convention de seuil doit donc être figée
et conservée dans toute la chaîne.

## 3. Réparation exacte de (47) vers (49)

On suppose (2) sur un intervalle **uniforme** \((0,v_0]\). Pour
\(y=\lambda/C\geq e\), choisissons \(s_\lambda\) comme dans (3). Alors

\[
 s_\lambda^{-1/3}=3y\log y
 \tag{13}
\]

et

\[
 \begin{aligned}
 \log(e/s_\lambda)
 &=1+\log\bigl(27y^3(\log y)^3\bigr)\\
 &=1+3\log y+3\log(3\log y)\\
 &\geq3\log y,
 \end{aligned}
 \tag{14}
\]

car \(y\geq e\). Par conséquent,

\[
 \frac{C s_\lambda^{-1/3}}{\log(e/s_\lambda)}
 \leq
 \frac{3Cy\log y}{3\log y}
 =\lambda.
 \tag{15}
\]

Sous la condition \(s_\lambda\leq v_0\), (2) et (15) donnent
\(f^*(s_\lambda)\leq\lambda\). L'implication exacte (7), et non l'égalité
fausse (1), donne alors (4).

Le seuil peut être écrit sans notation asymptotique : il suffit que

\[
 \frac{\lambda}{C}\geq e,
 \qquad
 3\frac{\lambda}{C}\log\frac{\lambda}{C}
 \geq v_0^{-1/3}.
 \tag{16}
\]

Il est uniforme en temps si et seulement si \(C\) et un même \(v_0\) le
sont. Une phrase « pour \(v\) assez petit » avec un seuil \(v_0(t)\) non
uniforme ne suffit pas à produire la constante et le seuil temporellement
uniformes revendiqués dans (49).

### Variante robuste sans résoudre l'équation

Pour une enveloppe positive \(H(v)\) décroissante sur \((0,v_0]\), la forme
sans ambiguïté est : choisir un \(s\leq v_0\) tel que

\[
 H(s)\leq\lambda.
 \tag{17}
\]

Alors

\[
 f^*(s)\leq H(s)\leq\lambda
 \quad\Longrightarrow\quad
 \mu_f(\lambda)\leq s.
 \tag{18}
\]

Le plus petit tel \(s\), au sens de pseudo-inverse généralisé de \(H\), est
le rayon de mesure optimal fourni par cette seule enveloppe. Cette procédure
reste valide avec des plateaux de \(f^*\), des sauts de \(\mu_f\) et des
ensembles de mesure finie.

## 4. Constante asymptotiquement optimale

Considérons l'enveloppe saturante

\[
 g^*(v)=\frac{C v^{-1/3}}{\log(e/v)},
 \qquad 0<v\leq v_0<e^{-2},
 \tag{19}
\]

prolongée de manière décroissante après \(v_0\). Elle est bien décroissante
sur cet intervalle, puisque, avec \(L(v)=\log(e/v)>3\),

\[
 \frac{d\log g^*}{d\log v}=-\frac13+\frac1{L(v)}<0.
 \tag{20}
\]

Toute fonction décroissante de ce type est réalisable comme réarrangée d'une
fonction radiale sur \(\mathbb R^3\), par exemple en posant
\(g(x)=g^*(|B_1||x|^3)\) dans la boule de volume \(v_0\), puis zéro hors de
cette boule.

À un niveau de continuité de l'inverse, posons \(y=\lambda/C\),
\(s=\mu_g(\lambda)\) et \(L=\log(e/s)\). L'égalité de l'enveloppe donne

\[
 y=s^{-1/3}L^{-1},
 \qquad
 s=\frac1{y^3L^3},
 \qquad
 L=1+3\log y+3\log L.
 \tag{21}
\]

Donc

\[
 \frac{L}{3\log y}\longrightarrow1,
 \qquad
 \mu_g(\lambda)
 \sim
 \frac{C^3}{27\lambda^3(\log(\lambda/C))^3}.
 \tag{22}
\]

Par suite, aucune borne universelle ayant, devant
\(\lambda^{-3}\log^{-3}(\lambda/C)\), une constante strictement inférieure à
\(C^3/27\) ne peut découler de (2) seule. Le candidat (3) a donc le bon
coefficient principal; l'inégalité non asymptotique est volontairement un
peu lâche à niveau fini à cause du terme positif \(1+3\log(3\log y)\).

Le symbole \(C_u\) de (49) peut absorber ce coefficient. En revanche, on ne
peut ni conserver automatiquement la même constante \(C\), ni omettre sa
mise au cube.

## 5. Plateaux tangents et seuils stricts

Les plateaux ne détruisent pas (4), précisément parce que (7) emploie le
superniveau strict. Si \(f^*(s_\lambda)=\lambda\), on obtient encore

\[
 |\{f>\lambda\}|\leq s_\lambda.
 \tag{23}
\]

Pour contrôler \(\{f\geq\lambda\}\), l'égalité tangentielle ne suffit pas.
Deux réparations sûres sont :

1. choisir \(s\) de sorte que \(H(s)<\lambda\) ;
2. pour tout \(0<\varepsilon<1\), utiliser
   \(\{f\geq\lambda\}\subset\{f>(1-\varepsilon)\lambda\}\), au prix du
   facteur \((1-\varepsilon)^{-3}\) et d'un logarithme évalué au niveau
   abaissé.

Le manuscrit emploie dans (49) et (50) des ensembles \(\{|u|>\lambda\}\) :
la convention stricte est compatible avec la réparation (3)–(4). Il ne faut
pas la remplacer par une convention fermée lors du raccord géométrique.

## 6. Nécessité d'un seuil de petit volume uniforme

Voici un contre-profil à toute lecture non uniforme. Soit \(v_n\downarrow0\)
et soit \(H(v)=Cv^{-1/3}/\log(e/v)\). Construisons une réarrangée décroissante
\(f_n^*\) qui coïncide avec \(H\) sur \((0,v_n]\), puis possède un plateau de
hauteur \(H(v_n)\) jusqu'au volume \(1\). Chaque \(f_n^*\) satisfait (2) avec
le même \(C\), mais seulement jusqu'au seuil \(v_0=v_n\).

Au niveau \(\lambda_n=H(v_n)/2\), qui tend vers l'infini,

\[
 \mu_{f_n}(\lambda_n)\geq1.
 \tag{24}
\]

Une borne uniforme de type
\(K\lambda_n^{-3}\log^{-3}\lambda_n\) tend au contraire vers zéro. Il n'existe
donc aucun seuil de grand niveau commun à cette famille. Ce profil ne réfute
pas une estimation de (47) établie sur un intervalle \((0,v_0]\) commun; il
montre que cette uniformité doit être explicitement dérivée avant (49).

## 7. Corrections logarithmiques lentes

Pour l'enveloppe régulière plus générale

\[
 H_{\beta,\gamma}(v)=
 \frac{C v^{-1/3}}
 {L(v)^\beta[\log L(v)]^\gamma},
 \qquad L(v)=\log(e/v),
 \tag{25}
\]

sur un régime où elle est décroissante et les facteurs sont positifs, une
inversion régulière donne formellement, et rigoureusement après encadrement,

\[
 \mu_f(\lambda)
 \lesssim
 \frac{C^3}
 {3^{3\beta}\lambda^3
  [\log(\lambda/C)]^{3\beta}
  [\log(3\log(\lambda/C))]^{3\gamma}}.
 \tag{26}
\]

Le facteur \(3^{-3\beta}\) provient du changement
\(\log(1/v)\sim3\log(\lambda/C)\); il n'est pas facultatif lorsque les
constantes principales sont suivies. Pour \(\beta=1,\gamma=0\), (26) retrouve
\(1/27\).

Pour une correction lentement variable arbitraire, la substitution naïve
« \(v\sim\lambda^{-3}\), donc on remplace \(v\) dans le logarithme » ne
préserve pas nécessairement les constantes, et peut même perdre une
équivalence sans hypothèse d'auto-négligence. L'inverse correct est celui de
la fonction complète \(H\); dans le langage de la variation régulière, il
fait intervenir la correction conjuguée de de Bruijn.

Un test explicite de la perte de constante est fourni par

\[
 H(v)=v^{-1/3}\exp\{-\sqrt{\log(1/v)}\}.
 \tag{27}
\]

Le facteur \(\exp(\sqrt{\log x})\) est lentement variable en \(x=1/v\).
Si \(z=\sqrt{\log(1/v)}\) et \(a=\sqrt{3\log\lambda}\), l'équation
\(\lambda=H(v)\) donne exactement

\[
 z^2-3z-3\log\lambda=0,
 \qquad
 z=\frac{3+\sqrt{9+12\log\lambda}}2
 =a+\frac32+o(1).
 \tag{28}
\]

Remplacer directement la correction par sa valeur en \(\lambda^3\) manque
donc le facteur limite
\(\exp(3/2)\) dans la correction, soit \(\exp(9/2)\) après cubage dans la
distribution. Le logarithme pur de (47) est suffisamment explicite pour
éviter ce piège via (13)–(15); l'argument « lentement variable » seul ne
suffit pas à certifier des constantes.

## 8. Logarithmes, dimensions et domaine de validité

L'écriture \(\log(e/v)\) n'est positive que pour \(v<e^1\) et mélange un
nombre pur avec un volume dimensionné. Elle ne peut être une borne globale
pour tout \(v>0\) : pour \(v>e\), son membre droit devient négatif. De même,
\(\log\lambda\) dans (49) exige un niveau positif, supérieur à une référence,
et sans dimension.

Une formulation dimensionnellement explicite peut employer un volume de
référence \(v_* >0\) et une amplitude de référence \(\lambda_*>0\), par
exemple

\[
 f^*(v)\leq
 \frac{C v^{-1/3}}{\log(e+v_*/v)},
 \qquad
 \mu_f(\lambda)\leq
 \frac{C_u}{\lambda^3
 [\log(e+\lambda/\lambda_*)]^3}.
 \tag{29}
\]

Le passage exact doit alors recalculer \(C_u\) et le seuil à partir de
\(C,v_*,\lambda_*\). Dans un système nondimensionné, on peut fixer ces
références à \(1\), mais ce choix doit être annoncé.

## 9. Certificat stdlib exact

Le script suivant ne remplace pas les preuves analytiques (6)–(22). Il
certifie exactement, avec `fractions.Fraction`, le contre-profil à plateaux,
le crochet de pseudo-inverses, le facteur critique \(1/27\), et les
conditions algébriques auxquelles se réduit (15) sur les niveaux
\(y=e^n\). Le dernier test utilise seulement
\(3n\geq1\Rightarrow\log(3n)\geq0\), pas une approximation flottante.

```python
from fractions import Fraction


# Simple function: value 5 on mass 3, value 2 on mass 4, zero elsewhere.
LEVELS = ((Fraction(5), Fraction(3)),
          (Fraction(2), Fraction(4)))


def mu_gt(level):
    """Exact mass of {f > level}."""
    return sum((mass for height, mass in LEVELS if height > level),
               Fraction(0))


def mu_ge(level):
    """Exact mass of {f >= level}."""
    return sum((mass for height, mass in LEVELS if height >= level),
               Fraction(0))


def f_star(s):
    """inf{a >= 0: mu_gt(a) <= s} for the exact step profile."""
    candidates = (Fraction(0),) + tuple(sorted({h for h, _ in LEVELS}))
    return min(a for a in candidates if mu_gt(a) <= s)


def f_star_left(s):
    """Left limit for this finite step profile."""
    cumulative = Fraction(0)
    for height, mass in LEVELS:
        cumulative += mass
        if s <= cumulative:
            return height
    return Fraction(0)


# Refutation of lambda = f*(mu(lambda)).
lam = Fraction(4)
s = mu_gt(lam)
assert s == 3
assert f_star(s) == 2
assert f_star(s) < lam < f_star_left(s)

# Strict versus closed threshold at a value plateau.
assert mu_gt(Fraction(2)) == 3
assert mu_ge(Fraction(2)) == 7
assert f_star(mu_ge(Fraction(2))) == 0

# Exact leading constant for p=3 and one inverse logarithm.
A_CRIT = Fraction(1, 27)
assert 27 * A_CRIT == 1
assert 27 * Fraction(1, 28) < 1  # asymptotically too small

# At y=e^n, n>=1, the proof of H(s_lambda)<=lambda reduces to
# log(e/s_lambda)-3 log(y) = 1 + 3 log(3n) >= 0.
# Since log is increasing and 3n>=1, these are exact order checks.
for n in range(1, 10_001):
    assert 3 * n >= 1

print("plateau equality counterexample: PASS")
print("strict/closed threshold separation: PASS")
print("pseudo-inverse bracket and 1/27 constant gate: PASS")
```

Commande de reproduction depuis la racine du dépôt : extraire le bloc Python
ci-dessus et l'exécuter avec `python -`. Aucune dépendance externe ni graine
aléatoire n'est utilisée.

## 10. Conséquence précise pour arXiv:2607.08866v2

La chaîne peut être classée comme suit.

| Maillon | Statut après attaque | Réparation minimale |
|---|---|---|
| « \(\lambda=u^*(\mu_f(\lambda))\) par définition » | **réfuté** par (10)–(12) | remplacer par (7)–(9) |
| enveloppe (47) \(\Rightarrow\) queue cubique-logarithmique | **valide conditionnellement** | utiliser (3)–(4), avec \(C,v_0\) uniformes |
| puissance logarithmique \(1\mapsto3\) | **correcte** | conserver le facteur principal \(1/27\) dans \(C_u\) |
| validité pour tous les niveaux | **réfutée sous lecture littérale** | imposer le seuil (16) |
| contrôle de \(\{|u|\geq\lambda\}\) | non démontré par l'égalité tangentielle | garder \(>\), ou introduire une marge |
| logarithmes dimensionnés | implicite | fixer \(v_*\), \(\lambda_*\) ou annoncer la nondimensionnalisation |
| uniformité en temps | conditionnelle | suivre un même petit-volume \(v_0\), pas seulement \(C\) |

Cette passe n'audite pas la preuve amont de (47), notamment l'inversion de la
distribution de vorticité et les deux intégrales d'O'Neil. Elle établit le
résultat borné suivant : **si (47) est disponible avec une constante et un
seuil uniformes, alors une version rigoureuse de (49) suit malgré la fausse
égalité intermédiaire**. Aucun contre-exemple à cette implication corrigée
n'a été trouvé; l'enveloppe saturante (19) montre au contraire qu'elle a les
bonnes puissances et fixe sa constante principale optimale.

## 11. Obligations falsifiables

```json
{
  "cycle": "0015",
  "source": "arXiv:2607.08866v2, equations (47)-(49)",
  "claims": [
    {
      "id": "NS-C0015-INVERSE-EQUALITY",
      "statement": "lambda = f*(mu_f(lambda)) for every measurable f",
      "status": "REFUTED",
      "witness": "two plateaus of heights 5 and 2 and masses 3 and 4; lambda=4"
    },
    {
      "id": "NS-C0015-LOG-TAIL",
      "statement": "uniform f*(v) <= C v^(-1/3)/log(e/v) implies a uniform lambda^(-3) log^(-3)(lambda/C) distribution tail at large levels",
      "status": "PROVED_IN_REPORT",
      "constant": "C^3/27",
      "thresholds": "lambda/C >= e and s_lambda <= v0"
    },
    {
      "id": "NS-C0015-UNIFORM-CUTOFF",
      "statement": "a time-independent C without a time-independent small-volume cutoff suffices for a uniform tail",
      "status": "REFUTED",
      "witness": "shrinking cutoffs v_n followed by a plateau up to mass 1"
    }
  ],
  "pde_scope": "functional rearrangement gate only; no Navier-Stokes solution is constructed",
  "decision": "REVISE"
}
```

## Conclusion contradictoire

Le vrai défaut de (47)–(49) n'est pas la puissance cubique du logarithme :
elle est correcte et optimale pour l'enveloppe pure. Le défaut est le recours
à une égalité d'inverses inexistante, puis à des équivalences sans seuils ni
constantes. La réparation (3)–(4) ferme ce maillon fonctionnel à condition
que le rapport principal établisse en amont un \(C\) **et un intervalle de
petit volume uniformes en temps**. Le prochain point adverse doit donc porter
sur l'uniformité réelle et la validité de l'estimation (47), non sur une
nouvelle inversion heuristique.
