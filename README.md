**Tic-Tac-Toe Game in Python**

This is a text-based implementation of the classic game Tic-Tac-Toe, developed by Abdallah Alnuaimy. It allows two players to take turns marking spaces on a 3x3 grid with X's and O's. The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins the game.

**How to Play**

1. **Run the Game:** Execute the Python script (`python tictactoe.py`) to start the game.
2. **The Toss:** A virtual coin toss randomly determines who goes first (X or O).
3. **Taking Turns:**
   - Players take turns entering the number (1-9) corresponding to the position they want to mark on the grid. 
   - The grid is displayed after each move to show the current state of the game.
4. **Winning:** The first player to get three of their marks in a row wins!
5. **Draw:** If all nine spaces are filled and neither player has won, the game is a draw.
6. **Play Again:** You'll be asked if you want to play another round.

**Code Structure and Functionality**

* **`main_menu()`:**
   - Welcomes the players.
   - Simulates a coin toss to decide the starting player (`Toss()` function).
   - Starts the game (`xoImplementation()` function).

* **`xoImplementation()`:**
   - Initializes a dictionary (`struc`) to represent the game board, with keys like 'n1', 'n2' corresponding to positions, and values initially set to '1', '2', etc.
   - Manages the game loop:
     - Prints the current state of the board.
     - Checks for winning conditions or a draw after each move.
     - Prompts the current player for their move.
     - Validates the input to ensure it's a valid position and not already taken.
     - Updates the board and switches turns.
     - Ends the game if there's a winner or a draw (`end()` function).

* **`Toss()`:**
   - Uses a random number generator to determine the starting player (X or O).

* **`end()`:**
   - Declares the winner or a draw.
   - Asks the players if they want to play again.
     - If yes, restarts the game from `main_menu()`.
     - If no, exits the program.

**Key Improvements:**

- **Clear Prompts and Messages:** The game provides clear instructions and feedback to the players.
- **Input Validation:** Prevents invalid inputs (out-of-range numbers, already occupied positions).
- **Game Logic:**  Handles win/draw conditions correctly and determines the next player's turn.

**Future Enhancements:**

- **Graphical User Interface (GUI):**  Enhance the visual experience by creating a graphical interface.
- **AI Opponent:** Implement an AI player using algorithms like Minimax to make the game more challenging.
- **Advanced Features:**  Add features like score tracking, difficulty levels, or different board sizes.



**How to Run the Game**

1. **Clone the Repository:** 
   ```bash
   git clone <repository_url>
   ```
2. **Navigate to the Directory:**
    ```bash
    cd tic-tac-toe-python
    ```
3. **Run the Script:**
    ```bash
    python tictactoe.py
    ```
