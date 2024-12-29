import numpy as np
import random
from collections import defaultdict

class GomokuEnv:
    def __init__(self, board_size=15):
        self.board_size = board_size
        self.board = np.zeros((board_size, board_size), dtype=int)
        self.done = False
        self.winner = None

    def reset(self):
        self.board = np.zeros((self.board_size, self.board_size), dtype=int)
        self.done = False
        self.winner = None
        return self.get_state()

    def get_state(self):
        return tuple(self.board.flatten())

    def is_valid_action(self, action):
        row, col = action
        return self.board[row, col] == 0

    def step(self, action, player):
        row, col = action
        if not self.is_valid_action(action):
            raise ValueError("Invalid action")

        self.board[row, col] = player

        # Check for a winner
        if self.check_winner(row, col, player):
            self.done = True
            self.winner = player
            return self.get_state(), 1 if player == 1 else -1, self.done

        # Check for a draw
        if np.all(self.board != 0):
            self.done = True
            self.winner = 0
            return self.get_state(), 0, self.done

        return self.get_state(), 0, self.done

    def check_winner(self, row, col, player):
        # Check rows, columns, and diagonals for a win
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1
            for step in [-1, 1]:
                r, c = row, col
                while True:
                    r += step * dr
                    c += step * dc
                    if 0 <= r < self.board_size and 0 <= c < self.board_size and self.board[r, c] == player:
                        count += 1
                    else:
                        break
            if count >= 5:
                return True
        return False

    def get_valid_actions(self):
        return [(r, c) for r in range(self.board_size) for c in range(self.board_size) if self.board[r, c] == 0]

def q_learning(env, episodes=100, alpha=0.1, gamma=0.9, epsilon=0.1):
    q_table = defaultdict(float)

    for episode in range(episodes):
        state = env.reset()
        done = False
        player = 1

        while not done:
            if random.uniform(0, 1) < epsilon:
                # Exploration
                action = random.choice(env.get_valid_actions())
            else:
                # Exploitation
                q_values = [q_table[(state, a)] for a in env.get_valid_actions()]
                max_q = max(q_values)
                best_actions = [a for a in env.get_valid_actions() if q_table[(state, a)] == max_q]
                action = random.choice(best_actions)

            next_state, reward, done = env.step(action, player)

            if not done:
                # Update Q-value
                next_q_values = [q_table[(next_state, a)] for a in env.get_valid_actions()]
                max_next_q = max(next_q_values)
                q_table[(state, action)] += alpha * (reward + gamma * max_next_q - q_table[(state, action)])
            else:
                # Terminal state update
                q_table[(state, action)] += alpha * (reward - q_table[(state, action)])

            state = next_state
            player = 3 - player  # Switch player

    return q_table

# Example usage
env = GomokuEnv(board_size=15)
q_table = q_learning(env, episodes=100)

# Play a game using the trained Q-table
def play_game(env, q_table):
    state = env.reset()
    done = False
    player = 1

    while not done:
        if player == 1:
            # AI's turn
            q_values = [q_table[(state, a)] for a in env.get_valid_actions()]
            max_q = max(q_values)
            best_actions = [a for a in env.get_valid_actions() if q_table[(state, a)] == max_q]
            action = random.choice(best_actions)
        else:
            # Random opponent
            action = random.choice(env.get_valid_actions())

        state, reward, done = env.step(action, player)
        print(env.board)
        print()
        if done:
            if env.winner == 1:
                print("AI wins!")
            elif env.winner == 2:
                print("Opponent wins!")
            else:
                print("It's a draw!")
        player = 3 - player

play_game(env, q_table)
