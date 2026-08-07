# 🐍 Préparation aux certifications Python Institute (PCEP • PCAP • PCPP)

> **Repo :** `202608Python_Certif_Prep`
> **Objectif :** préparer et obtenir les certifications **PCEP** (Entry), **PCAP** (Associate), **PCPP1** et **PCPP2** (Professional) du **Python Institute / OpenEDG**, sur la piste **General-Purpose Programming**.
> **Source officielle :** <https://pythoninstitute.org/certification-tracks>

---

## 1. Vue d'ensemble de la piste General-Purpose Programming

Le Python Institute structure ses certifications en trois niveaux (Entry / Associate / Professional). Sur la piste *General-Purpose Programming* :

| Niveau | Certification | Code examen typique | Prérequis |
|---|---|---|---|
| Entry | **PCEP** – Certified Entry-Level Python Programmer | `PCEP-30-0x` | Aucun |
| Associate | **PCAP** – Certified Associate Python Programmer | `PCAP-31-0x` | PCEP recommandé |
| Professional 1 | **PCPP1** – Certified Professional Python Programmer 1 | `PCPP-32-0x` | PCAP requis |
| Professional 2 | **PCPP2** – Certified Professional Python Programmer 2 | `PCPP_EPP-32-0x` | PCAP + PCPP1 |

> Passe chaque niveau dans l'ordre : **PCEP → PCAP → PCPP1 → PCPP2**.

Le site mentionne aussi d'autres pistes (Data Science avec PCED/PCAD, Testing avec PCET/PCAT, Security avec PCES, Automation avec PCEA, AI avec PCEI). Tu peux les ajouter plus tard comme extensions.

---

## 2. Format commun des examens

- **Type :** QCM + glisser-déposer de snippets de code (aucun IDE externe).
- **Surveillance :** via **TestNow** (OpenEDG) — webcam + partage d'écran.
- **Score :** **70 %** pour réussir (toutes les certifications listées).
- **Langue :** anglais (traduction possible dans certaines langues).
- **Validité :** permanente (pas de recertification).
- **Badge :** badge numérique + certificat PDF + vérification publique sur `verify.openedg.org`.

---

## 3. PCEP — Certified Entry-Level Python Programmer

### Infos examen
- **Durée :** 45 minutes
- **Questions :** 30
- **Score de réussite :** 70 %
- **Format :** QCM + drag-and-drop

### Syllabus détaillé (poids par section)

| Domaine | Poids | Sujets clés |
|---|---|---|
| 1. Fundamentals of Computer Programming & Python | ~12 % | Interpreter vs compilateur, lexique, PEP 8, types fondamentaux |
| 2. Data Types, Evaluations & Basic I/O | ~19 % | `int`, `float`, `complex`, `bool`, `str`, opérateurs, `print()`, `input()`, conversions |
| 3. Control Flow – Conditional Blocks & Loops | ~20 % | `if/elif/else`, `while`, `for`, `range()`, `break`, `continue`, branchement |
| 4. Data Collections – List, Tuple, Dict, Set, String | ~17 % | slicing, méthodes, immutabilité, mutabilité, opérateurs d'appartenance |
| 5. Functions & Exceptions | ~32 % | `def`, `return`, paramètres, portée, `*args`/`**kwargs`, `try/except/finally`, `raise` |

### Compétences cibles
- Lire et prédire l'exécution d'un script simple.
- Manipuler strings, listes, tuples, dicts, sets.
- Écrire des fonctions propres et gérer les exceptions de base.

### Mini-projets suggérés
- `calc.py` — calculatrice en CLI avec gestion d'erreurs.
- `quiz.py` — QCM interne (utilise ton propre jeu de questions).
- `palindrome_check.py` — manipulations de strings.

### Checklist PCEP
- [ ] Acheter le voucher (bouton « Voucher Store » sur le site).
- [ ] Terminer **Python Essentials 1** (cours officiel open-edg / Cisco NetAcad).
- [ ] Réussir 3 mocks complets (40/30 minimum).
- [ ] Planifier le passage TestNow.

---

## 4. PCAP — Certified Associate Python Programmer

### Infos examen
- **Durée :** 65 minutes
- **Questions :** 40
- **Score de réussite :** 70 %
- **Prérequis conseillé :** PCEP validé.
- **Format :** QCM + drag-and-drop.

### Syllabus détaillé

| Domaine | Poids | Sujets clés |
|---|---|---|
| 1. Modules, Packages & PIP | ~14 % | `import`, `from…import`, `sys.path`, `__name__ == "__main__"`, `pip`, `venv`, `pyproject.toml` |
| 2. Exceptions & Strings | ~14 % | hiérarchie d'exceptions, `else`/`finally`, exceptions personnalisées, méthodes de `str`, encodage ASCII / Unicode |
| 3. Object-Oriented Programming | ~22 % | classes, instances, attributs, méthodes, `self`, `__init__`, `__str__`/`__repr__`, encapsulation, visibilité (convention) |
| 4. Advanced OOP | ~14 % | héritage simple et multiple, `super()`, MRO, polymorphisme, `isinstance`, `issubclass`, `__bases__` |
| 5. Comprehensions, Lambdas, Closures, I/O | ~36 % | list/dict/set comprehensions, generator expressions, `lambda`, `map`/`filter`, closures, `with open(...)`, modes d'ouverture |

### Compétences cibles
- Structurer un projet Python en modules/paquets.
- Écrire du code orienté objet idiomatique et hiérarchies propres.
- Lire et écrire des fichiers (texte, binaire, JSON).

### Mini-projets suggérés
- `oop_zoo/` — hiérarchie d'animaux avec polymorphisme.
- `pkg_inventory/` — paquet structuré pour gérer un inventaire CSV.
- `logger_mod/` — module de logging réutilisable.

### Checklist PCAP
- [ ] Terminer **Python Essentials 2**.
- [ ] Maîtriser `venv`, `pip`, `pyproject.toml`.
- [ ] Mock 1, Mock 2, Mock 3 ≥ 32/40.
- [ ] Passer TestNow.

---

## 5. PCPP1 — Certified Professional Python Programmer 1

### Infos examen
- **Durée :** 65 minutes
- **Questions :** 45
- **Score de réussite :** 70 %
- **Prérequis obligatoire :** PCAP validé.
- **Format :** QCM + drag-and-drop.

### Syllabus détaillé

| Domaine | Poids | Sujets clés |
|---|---|---|
| 1. Advanced OOP | ~15 % | `__dict__`, `__class__`, introspection, méthodes spéciales (`__iter__`, `__next__`, `__enter__`/`__exit__`, `__eq__`/`__lt__`, …), `dataclasses`, `enum`, métaclasses |
| 2. GUI Programming | ~15 % | Tkinter : `Tk`, `Frame`, widgets, événements, callbacks, layout (`pack`/`grid`/`place`), `ttk`, dialogues, threads dans une GUI |
| 3. Python in Networking & IPC | ~15 % | sockets (`socket`, `AF_INET`/`AF_UNIX`), client/serveur TCP/UDP, threading, multiprocessing, `queue`, pipes |
| 4. Python in DBMS & SQL | ~15 % | `sqlite3`, requêtes paramétrées, transactions, `peewee`/`SQLAlchemy` (introduction) |
| 5. Miscellaneous (decorators, logging, testing, conventions) | ~40 % | décorateurs simples et paramétrés (`functools.wraps`), `logging` (loggers, handlers, formatters), `unittest`, `pytest` (introduction), PEP 8 / PEP 257, outils de profilage (`cProfile`, `timeit`) |

### Compétences cibles
- Maîtriser les patterns avancés de POO et la métaprogrammation légère.
- Construire de petites GUI et services réseau.
- Persister des données proprement (SQLite / ORM léger).

### Mini-projets suggérés
- `gui_chat_client/` — client Tkinter qui se connecte au projet `sockets_server/`.
- `sqlite_bookshelf/` — base de livres avec PEP 257 docstrings.
- `decorator_kit/` — mini-bibliothèque de décorateurs (timing, retry, memoize, cache).

### Checklist PCPP1
- [ ] Terminer **Python Professional 1** (cours officiel).
- [ ] Connaître par cœur les méthodes spéciales clés (`__init__`, `__str__`, `__repr__`, `__len__`, `__iter__`/`__next__`, `__enter__`/`__exit__`, `__eq__`, `__lt__`, `__add__`).
- [ ] Mocks ≥ 35/45.
- [ ] Passer TestNow.

---

## 6. PCPP2 — Certified Professional Python Programmer 2

### Infos examen
- **Durée :** 65 minutes
- **Questions :** 45
- **Score de réussite :** 70 %
- **Prérequis obligatoire :** PCAP **et** PCPP1.
- **Format :** QCM + drag-and-drop.

### Syllabus détaillé

| Domaine | Poids | Sujets clés |
|---|---|---|
| 1. Advanced Packages & Imports | ~15 % | `__init__.py`, sous-paquets, `namespace` packages, `importlib`, lazy imports, versioning (PEP 440), `pyproject.toml` |
| 2. Design Patterns | ~20 % | Singleton, Factory, Abstract Factory, Builder, Façade, Proxy, Observer, Command, Template Method, State, Strategy — implémentation Python idiomatique |
| 3. IPC (Interprocess Communication) | ~10 % | `multiprocessing`, `concurrent.futures`, `pipe`, file-locks, `signal`, gestion de pools |
| 4. Network Programming | ~15 % | sockets avancés, HTTP, REST, JSON, email (SMTP/POP3/IMAP), `urllib`, `requests`, `xmlrpc`, gRPC (intro) |
| 5. Python-SQL & Python-NoSQL | ~15 % | `psycopg`, `mysql-connector`, `pymongo`/MongoEngine, transactions, ORM avancé (SQLAlchemy) |
| 6. Testing & Quality | ~25 % | `unittest`, `pytest` avancé, `coverage`, TDD, mocking (`unittest.mock`), `doctest`, fixtures, parametrize |

### Compétences cibles
- Concevoir des paquets distribuables (`pip install` locaux).
- Implémenter les design patterns GoF en Python idiomatique.
- Robustifier un service réseau + base SQL/NoSQL.

### Mini-projets suggérés
- `pkg_microservice/` — paquet installable exposant un serveur REST.
- `design_patterns_kit/` — chaque pattern avec tests unitaires.
- `test_driven_kata/` — Kata de TDD en pytest + coverage 100 %.

### Checklist PCPP2
- [ ] Terminer **Python Professional 2**.
- [ ] Mini-projet `pkg_microservice` installable via `pip`.
- [ ] Mocks ≥ 35/45.
- [ ] Passer TestNow.

---

## 7. Plan d'étude suggéré (≈ 6 mois, ~10 h/semaine)

| Semaine | Focus | Livrable dans le repo |
|---|---|---|
| W1–W4 | PCEP — Python Essentials 1 + mocks PCEP | `pcep/` |
| W5–W9 | PCAP — Python Essentials 2 + projet OOP + mocks | `pcap/` |
| W10–W15 | PCPP1 — Professional + GUI + sockets | `pcpp1/` |
| W16–W22 | PCPP2 — design patterns + réseau + tests | `pcpp2/` |
| W23–W24 | Révisions transverses, mocks blancs chronométrés, test de la config TestNow | `mocks/` |

---

## 8. Structure suggérée du repo

```
202608Python_Certif_Prep/
├── README.md                ← ce fichier
├── .gitignore               ← Python std (généré depuis github/gitignore)
├── LICENSE
├── pcep/
│   ├── notes/
│   ├── exercises/
│   └── mocks/
├── pcap/
│   ├── notes/
│   ├── oop_zoo/
│   └── mocks/
├── pcpp1/
│   ├── notes/
│   ├── gui_chat_client/
│   ├── sqlite_bookshelf/
│   └── mocks/
├── pcpp2/
│   ├── notes/
│   ├── pkg_microservice/
│   ├── design_patterns_kit/
│   └── mocks/
└── resources/
    └── links.md
```

---

## 9. Ressources

### Officielles
- Piste complète : <https://pythoninstitute.org/certification-tracks>
- Pearson VUE (TestNow) : <https://home.pearsonvue.com/openedg>
- Vérification d'un badge : <https://verify.openedg.org>

### Cours officiels (gratuits)
- **Python Essentials 1** — Cisco Networking Academy / OpenEDG.
- **Python Essentials 2**.
- **Python Professional 1** & **Python Professional 2**.

### Pratique
- Mocks OpenEDG (téléchargeables après achat du voucher).
- `pcep/mocks/` — fichiers d'entraînement par chapitre (à construire).
- KatAs Python sur Exercism / Codewars (filtre : niveau Associate/Professional).

### Lecture
- *Python Distilled* — D. Beazley (2021).
- *Fluent Python* — L. Ramalho (2e éd.).
- PEP 8, PEP 20, PEP 257, PEP 8 Style Guide.

---

## 10. Conseils pour le jour J (TestNow)

- **Environnement :** pièce calme, webcam visible, second écran autorisé mais toutes les fenêtres doivent être visibles.
- **Outillage :** papier blanc autorisé (eauplate, vierge, sans texte pré-écrit).
- **Pacing :** 30 questions en 45 min ≈ **90 s/question** (PCEP), 40 questions en 65 min ≈ **98 s/question** (PCAP), 45 questions en 65 min ≈ **86 s/question** (PCPP).
- **Révision express la veille :** relire la table des matières du syllabus + les méthodes spéciales.

---

## 11. Checklist globale d'avancement

| Étape | Statut |
|---|---|
| Repo créé et privé | ☐ |
| `.gitignore` Python ajouté | ☐ |
| `LICENSE` choisi (MIT/Apache-2.0) | ☐ |
| PCEP — syllabus couvert | ☐ |
| PCEP — mock blanc chronométré ≥ 70 % | ☐ |
| PCEP — voucher acheté + TestNow planifié | ☐ |
| PCEP — badge récupéré | ☐ |
| PCAP — syllabus couvert | ☐ |
| PCAP — mock blanc ≥ 70 % | ☐ |
| PCAP — TestNow réussi | ☐ |
| PCAP — badge récupéré | ☐ |
| PCPP1 — syllabus couvert | ☐ |
| PCPP1 — mock blanc ≥ 70 % | ☐ |
| PCPP1 — TestNow réussi | ☐ |
| PCPP2 — syllabus couvert | ☐ |
| PCPP2 — mock blanc ≥ 70 % | ☐ |
| PCPP2 — TestNow réussi | ☐ |

---

> **Bon courage — et Happy Coding! 🐍🎓**

