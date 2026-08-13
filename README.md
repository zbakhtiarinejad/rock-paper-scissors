## Rock-Paper-Scissors Game (Python)

A simple, interactive command-line **Rock, Paper, Scissors** game built using Python. The game lets a user play against the computer, tracks the score across multiple rounds, and declares a final winner when the player decides to quit.

### 🌟 Features

* **Persistent Score Tracking:** Keeps track of both user and computer wins throughout the session.
* **Input Validation:** Handles invalid inputs gracefully without crashing the game.
* **Tie Handling:** Detects ties and immediately moves to the next round.
* **Final Score Summary:** Displays a congratulations or encouragement message with the final scores upon quitting.

---

### 🚀 How to Play

1. **Run the script** in your terminal:
```bash

```



python main.py

```
2. **Enter your choice** when prompted:
   *   `r` for Rock
   *   `p` for Paper
   *   `s` for Scissors
   *   `q` to quit the game and see the final results.

---

### 🛠️ Technologies Used
*   **Python 3**
*   `random` module (built-in)

---
Technical Challenges & Problem Solving:

Bug 1: Handling Invalid User Input (Non-Numeric Strings)Issue: User input via input() defaults to a string. If a player entered text or special characters instead of an integer, converting it directly with int() would throw a ValueError runtime exception, crashing the application.
Fix: Implemented guard-clause input validation using .isdigit(). The script checks if the string consists entirely of digits before casting it to an integer. If invalid input is detected, it alerts the user and utilizes a continue statement to safely restart the loop without incrementing errors or breaking execution.

Bug 2: Infinite Loop Potential & Turn Constraints
Issue: Without an explicit turn limit, a player could remain stuck in an infinite while True loop indefinitely if they failed to guess correctly.
Fix: Introduced an explicit counter guesses that increments on every attempt. Added a condition (if guesses >= 5) that checks if the player has reached the maximum allowed attempts. Once reached, it notifies the user, reveals the target number (rn), and safely exits the loop using break.

Bug 3: Output Grammar Precision (Pluralization Handling)
Issue: Displaying a generic result string like "your number of guesses: 1" creates a minor grammatical inconsistency when the user succeeds on their very first attempt.
Fix: Added conditional logic at the end of execution to evaluate guesses > 1. The system dynamically renders "guesses" for multiple attempts and "guess" for a single attempt, ensuring polished final output formatting.  
