# 🧠 Tic Tac Toe AI Agent with Minimax & Alpha-Beta Pruning

Welcome to our intelligent Tic Tac Toe project, where strategy meets AI! Built as part of our *Introduction to Artificial Intelligence* course, this game features an unbeatable AI using classic search algorithms.

## 👥 Team Members
- **Priyanka Singh**
- **Heli Sureja**

Instructor: *Prof. Shivanjali Khare*

---

## 🎯 Project Goal

The aim of this project is to build an AI agent that **never loses** at Tic Tac Toe. We used the **Minimax algorithm**, enhanced with **Alpha-Beta Pruning**, to simulate smart decision-making in a zero-sum game.

This AI evaluates all possible game states, anticipates opponent moves, and selects the most optimal move instantly.

---

## 🚀 Introduction 
Often used to illustrate fundamental AI ideas, Tic Tac Toe is a straightforward, deterministic, 
turn-based strategic game. The aim is to create an artificial intelligence agent capable of 
efficiently fighting against human or random opponent and that which performs optimum, 
therefore guaranteeing it never loses. Implementing the Minimax method with Alpha-Beta 
pruning helps the agent improve computational efficiency and replicate adversarial decision
making. 

## 🧠 AI Technique Overview

### 🔄 Minimax Algorithm
- Explores all possible future moves.
- Maximizes the AI’s chance of winning while minimizing the opponent’s.
- Guarantees perfect play: the AI will either **win** or **draw**, never lose.

### ✂️ Alpha-Beta Pruning
- Optimization that skips unnecessary evaluations.
- Prunes parts of the decision tree that can't affect the outcome.
- Greatly improves performance and speed.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| Pygame | GUI for interactive play |
| Random | Used for simulating non-intelligent opponent |
| Time | Used optionally for performance tracking |

---

## 📁 File Breakdown

File              |        Description 
----------------------------------------------------------------
| `main.py`       | Starts the game and initializes AI |
| `game.py`       | Contains GUI logic and game rules |
| `ai.py`         | Implements Minimax with Alpha-Beta Pruning |
| `random_bot.py` | Simple bot that plays random moves |
| `ai_simple`     | Earlier or backup AI logic |
| `README.md`     | Project overview and setup instructions |

---

## 🚀 How to Run the Game

1. Install Pygame (if not already installed):
   ```bash
   pip install pygame
   ```

2. Start the game:
   ```bash
   python main.py
   ```

3. You’ll play as **X**, and the AI will play as **O**.

Click on a cell to make your move. The AI will respond instantly with the most optimal move.

---

## 📊 Evaluation Criteria

- ✅ **Win Rate**: The AI consistently defeats random bot.
- ✅ **No Losses**: The AI never loses a game.
- ✅ **Efficiency**: Alpha-Beta Pruning reduces decision time significantly.
- ✅ **User Feedback**: Easy to play, challenging to win.

---

## 🎮 Demo Video

Our demo includes:
- Introduction by both team members.
- Code walkthrough.
- Gameplay demo vs human and random bot.
- AI logic explained step-by-step.
- Final thoughts and project reflection.

---

## 💡 Future Ideas

- Add difficulty levels by limiting depth or adding randomness.
- Extend to 4x4 or larger boards.
- Implement multiplayer or online version.
- Record and visualize performance stats.

---

## 📘 License

This project was created for educational use under the AI curriculum at the **University of New Haven**.
