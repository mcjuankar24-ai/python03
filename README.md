<p align="center">
  <img src="https://img.shields.io/badge/Language-Python%203.10%2B-blue?style=for-the-badge&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/Topic-Data%20Structures-red?style=for-the-badge" alt="Data Structures">
  <img src="https://img.shields.io/badge/Linter-Flake8-green?style=for-the-badge" alt="Flake8 Standard">
  <img src="https://img.shields.io/badge/Type%20Checking-Mypy-orange?style=for-the-badge" alt="Mypy Checked">
</p>

# Data Quest — Mastering Python Collections

**42 Málaga** | **Author:** jmesa-ci
**Version:** 3.0

## 📖 Summary

Journey through the digital realm as a data engineer! This project builds a game
analytics platform while mastering Python's core collection types: **lists**, **tuples**,
**sets**, and **dictionaries**, along with **generators** and **comprehensions**.

Each exercise unlocks a new data structure, moving from raw command-line arguments
to sophisticated data transformation pipelines, ending with elegant one-line
comprehensions for filtering and reshaping game data.

## 🛠 Requirements

- Python 3.10+
- Code respects `flake8` linter standards
- All functions and methods include type hints (checked with `mypy`)
- No file I/O — all data comes from command-line arguments or in-memory generation
- Command-line access via the `sys` module (`sys.argv`)
- Functions handle exceptions gracefully; programs must never crash

## 📂 Project Structure

```
.
├── ex0/
│   └── ft_command_quest.py        # Exercise 0: Command Quest
├── ex1/
│   └── ft_score_analytics.py      # Exercise 1: Score Cruncher
├── ex2/
│   └── ft_coordinate_system.py    # Exercise 2: Position Tracker
├── ex3/
│   └── ft_achievement_tracker.py  # Exercise 3: Achievement Hunter
├── ex4/
│   └── ft_inventory_system.py     # Exercise 4: Inventory Master
├── ex5/
│   └── ft_data_stream.py          # Exercise 5: Stream Wizard
├── ex6/
│   └── ft_data_alchemist.py       # Exercise 6: Data Alchemist
└── README.md
```

## 🌱 Exercises

### Exercise 0 — Command Quest (`ft_command_quest.py`)
Introduces **lists** through `sys.argv`, Python's command-line argument array. Displays
the program name, the number of arguments received, and each argument in order.

### Exercise 1 — Score Cruncher (`ft_score_analytics.py`)
Builds a **list** of game scores from command-line arguments, gracefully discarding
non-numeric values with an error message. Computes total, average, max, min, and
range using `sum()`, `max()`, and `min()`.

### Exercise 2 — Position Tracker (`ft_coordinate_system.py`)
Introduces **tuples** to represent immutable 3D coordinates. `get_player_pos()` prompts
the user for `x,y,z` input, retries on invalid syntax or non-numeric values, and returns a
3-tuple. Computes the Euclidean distance to the origin and between two points using
`math.sqrt()`.

### Exercise 3 — Achievement Hunter (`ft_achievement_tracker.py`)
Introduces **sets** to model unique, unordered collections. `gen_player_achievements()`
randomly samples a subset of achievements for each of four players. Demonstrates
`union()`, `intersection()`, and `difference()` to find all distinct achievements, achievements
common to every player, achievements unique to one player, and achievements a player
is still missing.

### Exercise 4 — Inventory Master (`ft_inventory_system.py`)
Introduces **dictionaries** to model an RPG-style inventory keyed by item name. Parses
`<item_name>:<quantity>` command-line parameters, raising custom exceptions
(`InvalidParameter`, `DuplicatedItem`) for malformed or repeated entries. Reports the
quantity percentage of each item, and the most/least abundant items, then updates the
inventory with a new item.

### Exercise 5 — Stream Wizard (`ft_data_stream.py`)
Introduces **generators** and the `yield` keyword. `gen_event()` is an infinite generator
that produces random `(player, action)` event tuples on demand. `consume_event()` is a
second generator that randomly drains a finite list of events, one at a time, until it's
empty — used directly in a `for ... in ...` loop.

### Exercise 6 — Data Alchemist (`ft_data_alchemist.py`)
Introduces **list and dictionary comprehensions** to transform and filter data in a single
expression: capitalizing all player names, filtering only already-capitalized ones,
building a `{name: score}` dictionary with random scores, and filtering it down to only
the above-average high scores.

## ▶️ Usage

Each exercise can be run independently, some with command-line arguments:

```bash
python3 ex0/ft_command_quest.py hello world 42
python3 ex1/ft_score_analytics.py 1500 2300 1800 2100 1950
python3 ex2/ft_coordinate_system.py
python3 ex3/ft_achievement_tracker.py
python3 ex4/ft_inventory_system.py sword:1 potion:5 shield:2
python3 ex5/ft_data_stream.py
python3 ex6/ft_data_alchemist.py
```

## ✅ Checks

```bash
flake8 .
mypy .
```

## 🤖 AI Usage Notice

In line with the project's AI Instructions chapter, any AI-assisted code in this
repository was reviewed, tested, and fully understood before submission. AI was used
to reduce repetitive tasks and support learning, not to replace understanding of the
underlying data structure concepts (lists, tuples, sets, dictionaries, generators, and
comprehensions).
