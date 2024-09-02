# 🏴‍☠️ Pirate Island Jump

A 2D platformer set in a pirate world, featuring multiple levels, collectible coins, enemy encounters, and a rising water mechanic that puts your speed and survival instincts to the test.

---

## 🎮 Gameplay Overview

Navigate through a series of pirate-themed levels, jumping across platforms, defeating enemies, and collecting coins — all while keeping an eye on the rising water below. Can you escape before the tide catches up?

### Core Mechanics

**Health System** — The player takes damage from enemies and water. Health is fully restored upon returning to the overworld.
**Crates** — Touch crates to regain health.
**Rising Water** — Starting at Level 5, water slowly rises. If it reaches the player before the level is completed, they die.
**Coins** — Collect coins throughout levels. Gather 20 to earn a special power.
**Speed Boost** — Touch a treasure box or collect 20 coins to activate a speed boost.
**Timer** — A countdown timer begins at Level 3 and runs through Level 6, adding urgency to each run.

---

## 🗺️ Level Structure

| Level (In-Game) | Description |
| Overworld | Hub world; player health resets upon return |
| Level 1 | Introductory platforming |
| Level 2 | Standard platforming |
| Level 3 (In-game: 4) | Timer begins |
| Level 4 | Timed platforming |
| Level 5 | Rising water mechanic begins |
| Level 6 | Final challenge — timed + rising water |

> **Note:** Level numbering in the codebase does not always match the in-game display. Level labeled "3" in files corresponds to in-game Level 4. Level labeled "2" in files corresponds to in-game Level 3.

---

## 🕹️ Controls

| Action | Key |
| Move Left | ← Arrow / A |
| Move Right | → Arrow / D |
| Jump | Space / ↑ Arrow / W |

---

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.x
- [Pygame](https://www.pygame.org/) library

### Install Dependencies

```bash
pip install pygame
```

### Run the Game

```bash
python main.py
```
---

## 📁 Project Structure

```
Pirate_Island_Jump/
├── code/           # Game logic and Python source files
├── audio/          # Sound effects and music
├── graphics/       # Sprites, tiles, and visual assets
├── levels/         # Level map files (created with Tiled)
├── .vscode/        # Editor settings
└── README.txt      # Original development notes
```

---

## 🛠️ Tools & Resources

- **[Tiled Map Editor](https://www.mapeditor.org/)** — Used to design and build level layouts
- **[Mixkit](https://mixkit.co/free-sound-effects/game/)** — Source for coin collection sound effects

---

## 🚀 Planned Features

- [ ] Redesigned levels built around the rising water mechanic
- [ ] Moving platforms
- [ ] Enemies that swim during water levels (different colors)
- [ ] Home/start screen with game instructions
- [ ] High score screen
- [ ] Gold coins that grant special powers
- [ ] Fix: player takes repeated damage when touching enemy

---

## 📝 Developer Notes

- Player health is capped at the maximum value and never exceeds it
- Water rise speed is still being tuned — currently under active development
- Later level ordering may be reshuffled as the water mechanic is refined

---

## 👩‍💻 Author

**Christina Trujillo** — [GitHub](https://github.com/christinatrujillo)
