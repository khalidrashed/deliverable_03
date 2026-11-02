# Virtual environment
.venv/

# Python cache
__pycache__/
*.pyc

# Jupyter checkpoints
.ipynb_checkpoints/

# System files
.DS_Store
Thumbs.db


# INF201 – Deliverable 3: RPG Battle Simulator

## Project Description

This project is a mini-RPG battle simulator developed in Python as part of INF201.

The program allows two characters to fight until one of them wins. Characters can have different specialisations, use weapons, and have different abilities.

The project demonstrates object-oriented programming concepts such as classes, objects, inheritance, encapsulation, and composition.

## Classes

The project contains six main classes:

- **Character:** Represents a basic character with health points, damage, and attack methods.
- **Warrior:** A specialised character with armour that reduces incoming damage.
- **Mage:** A specialised character that uses mana to perform powerful magical attacks.
- **Dice:** Generates random numbers to determine weapon damage.
- **Weapon:** Represents weapons that use dice to calculate damage.
- **Battle:** Manages the battle between two characters.

## Project Structure

```text
deliverable_03/
├── character.py
├── dice.py
├── items.py
├── battle.py
├── game_simulator.ipynb
├── requirements.txt
├── README.md
└── git_log.txt
```

## Requirements

- Python 3.13
- Jupyter Notebook
- Packages listed in `requirements.txt`

## How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/khalidrashed/deliverable_03.git
```

2. Open the project folder:

```bash
cd deliverable_03
```

3. Create a virtual environment:

```bash
py -3.13 -m venv .venv
```

4. Activate the virtual environment in Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

5. Install the required packages:

```bash
python -m pip install -r requirements.txt
```

6. Start Jupyter Notebook:

```bash
python -m notebook
```

7. Open `game_simulator.ipynb` and run the notebook cells from beginning to end.

## Testing

The notebook includes tests and demonstrations of:

- Character health, damage, and healing.
- Dice rolls with different numbers of sides.
- Weapon damage.
- Warrior armour.
- Mage mana and magical attacks.
- Battles with and without weapons.

INF201 – Group Project

