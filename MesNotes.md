# Python Essentials 1 — Notes de cours (PCEP)

---

## Module 1 — Introduction à Python et à la programmation

### 1. Comment fonctionne Python ?

**Langage naturel vs langage de programmation**

Un langage — qu'il soit naturel ou de programmation — possède quatre composantes : un **alphabet**, un **lexique**, une **syntaxe** et une **sémantique**.

L'ordinateur ne comprend qu'une seule langue : le **langage machine** (des suites de 0 et de 1). Les humains, eux, écrivent du code dans un **langage de haut niveau** (Python, C, Java…), plus simple à manipuler que des instructions machine brutes. Un traducteur est donc nécessaire pour convertir le code source en instructions exécutables par la machine.

### 2. Compilateur vs Interpréteur

Il existe deux grandes approches pour traduire un programme écrit dans un langage de haut niveau en langage machine.

| Aspect | 🔨 Compilateur | 🔄 Interpréteur |
|---|---|---|
| **Principe** | Traduit **une fois** tout le code source en un fichier exécutable, distribuable ensuite librement | Traduit et exécute le code **ligne par ligne**, à chaque exécution, via un programme interpréteur |
| **Quand a lieu la traduction ?** | Avant l'exécution | Pendant l'exécution |
| **Résultat** | Un fichier exécutable autonome | Pas de fichier exécutable séparé |
| **Détection des erreurs** | Toutes en même temps, à la compilation | Une par une (arrêt à la première erreur rencontrée) |
| **Vitesse d'exécution** | ⚡ Rapide (déjà traduit) | 🐢 Plus lente (traduite à chaque exécution) |
| **Exemples de langages** | C, C++, Go, Rust | Python, JavaScript, Ruby, PHP |

> **À retenir pour le PCEP :** en réalité, Python compile d'abord son code en **bytecode** (fichiers `.pyc`), ensuite interprété par la **PVM** (Python Virtual Machine). Mais pour l'examen, il suffit de retenir : **Python = langage interprété**.

### 3. Installer et utiliser Python

- **Linux** : Python est installé par défaut (utilisé en interne par de nombreux composants du système).
- **macOS** : Python 2 est installé par défaut.
- Pour utiliser Python, il faut : un **IDE**, une **console** et un **debugger**.
- Python 3 est fourni avec **IDLE** (*Integrated Development & Learning Environment*).

| Système | Lancer IDLE | Quitter |
|---|---|---|
| macOS | `python3 -m idlelib` | `exit()` |
| Windows | `python -m idlelib` | `exit()` |

### 4. Écrire et exécuter son premier script

1. Lancer `python3 -m idlelib`
2. Créer un nouveau fichier, renommer la fenêtre d'édition
3. Écrire le code, par exemple :
   ```python
   print("On démarre avec Python3. Objectif : être certifié pour des compétences réelles.")
   ```
4. Enregistrer (`Cmd + S`)
5. Exécuter avec **F5**

---

## Module 2 — Types de données, variables, entrées/sorties, opérateurs

### 1. La fonction `print()`

Une **fonction** est une portion de code identifiée par un nom, qui peut :
- provoquer un effet,
- évaluer une valeur,
- la renvoyer comme résultat.

Une fonction peut être **native**, issue d'un **module**, ou **créée par le programmeur** — dans ce dernier cas, son nom doit rester clair et explicite.

| Code | Résultat |
|---|---|
| `print()` | Ligne vide |
| `print("Eldave DIBALA\n36 ans")` | `Eldave DIBALA` puis `36 ans` sur une nouvelle ligne (`\n` = *newline*) |
| `print("Eldave", "Nisi", "Prince", "DIBALA.")` | `Eldave Nisi Prince DIBALA.` *(espace ajouté automatiquement entre les arguments)* |
| `print("Eldave", "Nisi", "Prince", "DIBALA.", sep="_")` | `Eldave_Nisi_Prince_DIBALA.` |
| `print("Pour citer :", end=" ")` puis `print("...")` | Les deux `print()` s'affichent sur la même ligne |

**Keyword arguments courants :** `sep="..."` (séparateur entre arguments), `end="..."` (caractère de fin, par défaut `\n`).

### 2. Littéraux et types de base

| Notion | Définition | Exemple |
|---|---|---|
| **Littéral** | Notation représentant une valeur fixe dans le code | `123`, `"Test"` |
| **Binaire** | Système en base 2 (0 et 1) | `1010` = 10 en décimal |
| **Octal / Hexadécimal** | Bases 8 et 16 (l'hexadécimal ajoute 6 lettres) | — |
| **Entier (int)** | Nombre sans partie fractionnaire | `256`, `-1` |
| **Flottant (float)** | Nombre avec partie fractionnaire | `1.27` |
| **Caractère d'échappement** | Permet d'insérer guillemet/apostrophe dans une chaîne | `"I\'m happy"` |
| **Booléen** | `True` / `False` — `1` équivaut à `True`, `0` à `False` | — |
| **None (NoneType)** | Représente l'absence de valeur | `None` |

### 3. Python comme calculatrice — opérateurs arithmétiques

| Opérateur | Rôle | Règle du résultat |
|---|---|---|
| `**` | Exponentiation (`a ** b` = a puissance b) | Le type du résultat suit celui des opérandes (int/int → int, sinon float) |
| `*` | Multiplication | Idem |
| `/` | Division | **Toujours** un float, quels que soient les types d'entrée |
| `//` | Division entière | Résultat toujours arrondi vers l'entier le plus proche (sans décimale conservée en valeur, mais le **type** peut rester float) |

**Exemples de division entière :**
```python
print(6 // 4)    # 1   → arrondi vers l'entier positif le plus proche
print(6. // 4)   # 1.0
print(6 // 4.)   # 1.0

print(-6 // 4)   # -2  → arrondi vers l'entier négatif le plus proche
print(-6 // 4.)  # -2.0
print(6. // -4)  # -2.0
```

### 4. Expressions et opérateurs — points clés

- Une **expression** est une combinaison de valeurs dont le résultat est une valeur.
- Les **opérateurs** sont des symboles ou mots-clés réalisant des opérations sur des valeurs.
- **Opérateur unaire** : un seul opérande (`-1`, `+2`).
- **Opérateur binaire** : deux opérandes (`12 % 5`).
- La **priorité des opérateurs** varie : `**` a la priorité la plus élevée, `+` et `-` binaires la plus faible.
- Les sous-expressions entre **parenthèses** sont prioritaires sur tout le reste.
- L'opérateur d'exponentiation (`**`) utilise la **liaison à droite**.

### 5. Les variables

Une **variable** est un emplacement nommé et réservé en mémoire pour stocker une valeur. Elle est créée automatiquement lors de sa première affectation.

**Règles PEP 8 pour nommer une variable :**
- minuscules, mots séparés par un underscore (`_`) ;
- doit commencer par une lettre ;
- l'underscore est considéré comme une "lettre" valide en début de nom ;
- sensible à la casse : `alice` ≠ `Alice` ≠ `ALICE` (trois identifiants distincts) ;
- ne doit pas être un mot-clé réservé de Python.

---

## Module 3 — Booléens, conditions, boucles, listes, opérateurs logiques et bit à bit

### 1. Opérateurs de comparaison et d'égalité

| Opérateur | Rôle |
|---|---|
| `=` | Assignation d'une valeur |
| `==` | Test d'égalité |
| `!=` | Test d'inégalité |

`==` est un opérateur **binaire**, à liaison **gauche → droite**, nécessitant deux arguments.

### 2. Conditions et exécution conditionnelle

- Pas d'accolades : l'**indentation** (4 espaces, PEP 8) délimite les blocs.
- `elif` peut être répété autant de fois que nécessaire.
- `else` est optionnel.

**Valeurs "truthy" / "falsy" :** Python évalue implicitement `bool(x)` dans un `if`. Tout est *truthy* sauf les valeurs *falsy* usuelles (`0`, `""`, `None`, `[]`, etc.).
> ⚠️ Piège classique : `bool([0])` → `True` (la liste n'est pas vide, même si son unique élément est falsy).

**`==` vs `is` :** `==` compare les **valeurs**, `is` compare les **identités** (`id()`). Pour `None`, toujours utiliser `is None` / `is not None`.

**Évaluation en court-circuit** (souvent demandée à l'examen) : très utile pour éviter des erreurs, par exemple `obj is not None and obj.valeur`.

**Expression conditionnelle (ternaire) :**
```python
resultat = valeur_si_vrai if condition else valeur_si_faux
```
C'est une **expression** (elle renvoie une valeur), pas une instruction. Elle peut être imbriquée, mais cela nuit à la lisibilité :
```python
signe = "positif" if x > 0 else "négatif" if x < 0 else "nul"
```

**`match` / `case`** (PEP 634, Python 3.10+ — au programme du **PCPP2**, pas du PCEP) :
- `_` = joker, capture tout sans nommer la valeur ;
- les *guards* (`if`) s'ajoutent après le pattern ;
- peut déstructurer listes, tuples, dicts et objets.

### 3. Pièges fréquents à l'examen

- **Affectation vs comparaison** : `=` (affectation) ≠ `==` (comparaison). `if x = 5:` est un `SyntaxError` en Python.
- **Walrus operator `:=`** (PEP 572, Python 3.8+) : affecte **et** renvoie une valeur dans une expression.
- **Comparaison de types différents** : `1 == 1.0` → `True`, mais `1 is 1.0` → `False`.
- **`in` / `not in`** : test d'appartenance, souvent préférable à une chaîne de `or`.
- **Blocs vides** : utiliser `pass` si un bloc conditionnel ne doit rien faire (obligatoire syntaxiquement).

### 4. Bonnes pratiques PEP 8

- Ne pas comparer explicitement à `True` / `False` : préférer `if flag:` à `if flag == True:`.
- Préférer `if not x:` à `if x == False:` ou `if x == []:`.
- Limiter la profondeur d'imbrication des `if` (privilégier les retours anticipés / *guard clauses*).

### 5. Opérateurs logiques

```markdown
# 📌 Pense-bête : Opérateurs Logiques en Python

Source du cours : [Logic and bit operations in Python | and, or, not](https://edube.org/learn/pe-1/logic-and-bit-operations-in-python-and-or-not-6)

---

## 💡 Concept Général

Dans la vraie vie comme en programmation, les conditions sont souvent complexes. Les **opérateurs logiques** permettent d'associer plusieurs expressions booléennes (`True` ou `False`) pour créer des conditions composées.

---

## 1. L'opérateur `and` (Conjonction)

L'opérateur `and` requiert que **toutes les conditions** soient vraies simultanément.

* **Priorité :** Plus faible que les opérateurs de comparaison (`>`, `==`, etc.).
* **Règle :** Retourne `True` uniquement si $A$ **et** $B$ sont vrais.

### 📊 Table de vérité (`and`)

| Argument A | Argument B | A `and` B |
| :---: | :---: | :---: |
| `False` | `False` | **`False`** |
| `False` | `True` | **`False`** |
| `True` | `False` | **`False`** |
| `True` | `True` | **`True`** |

### 🐍 Exemple d'code

```python
temps_libre = True
beau_temps = True

# La promenade n'a lieu que si TOUTES les conditions sont vérifiées
if temps_libre and beau_temps:
    print("On va se promener !")

counter = 10
value = 100
resultat = counter > 0 and value == 100  # Evalué à True

```

---

## 2. L'opérateur `or` (Disjonction)

L'opérateur `or` nécessite qu'**au moins une des conditions** soit vraie.

* **Priorité :** Plus faible que l'opérateur `and` (de la même manière que l'addition `+` passe après la multiplication `*`).
* **Règle :** Retourne `True` si $A$ **ou** $B$ (ou les deux) est vrai.

### 📊 Table de vérité (`or`)

| Argument A | Argument B | A `or` B |
| --- | --- | --- |
| `False` | `False` | **`False`** |
| `False` | `True` | **`True`** |
| `True` | `False` | **`True`** |
| `True` | `True` | **`True`** |

### 🐍 Exemple de code

```python
moi_au_centre_commercial = False
toi_au_centre_commercial = True

# Le cadeau est acheté si AU MOINS UNE personne est au centre commercial
if moi_au_centre_commercial or toi_au_centre_commercial:
    print("Un cadeau pour Maman sera acheté !")

```

---

## 3. L'opérateur `not` (Négation)

L'opérateur unaire `not` inverse la valeur logique d'une expression.

* **Priorité :** Très élevée (identique aux opérateurs unaires `+` et `-`).
* **Règle :** Transforme le vrai en faux et le faux en vrai.

### 📊 Table de vérité (`not`)

| Argument | `not` Argument |
| --- | --- |
| `False` | **`True`** |
| `True` | **`False`** |

### 🐍 Exemple de code

```python
il_pleut = False

# not il_pleut devient True
if not il_pleut:
    print("Pas besoin de parapluie !")

```

---

## ⚡ Ordre de Priorité des Opérateurs

En cas de conditions mixtes sans parenthèses, Python évalue les expressions selon cette hiérarchie :

```text
1. Opérateurs de comparaison (==, !=, >, <, >=, <=) et unary `not`  [Priorité Haute]
2. `and`                                                           [Priorité Moyenne]
3. `or`                                                            [Priorité Basse]

```

> **Conseil :** Utilisez toujours des parenthèses `()` pour clarifier les conditions complexes et éviter les ambiguïtés.

```

```
---

## ⚡ Plan de révision — 45 jours restants

| # | Règle |
|---|---|
| 🕐 | Minimum **5h/jour** de travail focalisé (idéalement 6-7h) |
| 📝 | **1 test blanc par semaine** minimum — analyser chaque erreur |
| 💻 | Coder chaque concept soi-même — ne pas se contenter de lire |
| 🔁 | Révision espacée : relire les notes des phases précédentes |
| 😴 | Dormir **7h+** — la mémoire se consolide pendant le sommeil |
| 📅 | Réserver les examens dès maintenant pour fixer une deadline ferme |
