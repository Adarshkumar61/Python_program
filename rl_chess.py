# import chess
# import random
# import numpy as np

# # Initialize the chess board
# board = chess.Board()

# # Define the Q-learning parameters
# alpha = 0.1  # learning rate
# gamma = 0.9  # discount factor
# epsilon = 0.1  # exploration rate

# # Initialize the Q-table
# q_table = {}

# # Function to get the current state of the board
# def get_state(board):
#     return str(board)

# # Function to get the possible actions (moves) from the current state
# def get_actions(board):
#     return list(board.legal_moves)

# # Function to choose an action (move) using epsilon-greedy
# def choose_action(board, q_table):
#     if random.random() < epsilon:
#         return random.choice(get_actions(board))
#     else:
#         return max(get_actions(board), key=lambda move: q_table.get((get_state(board), move), 0))

# # Function to update the Q-table
# def update_q_table(board, move, reward, q_table):
#     state = get_state(board)
#     q_table[(state, move)] = q_table.get((state, move), 0) + alpha * (reward + gamma * max(q_table.get((get_state(board), a), 0) for a in get_actions(board)) - q_table.get((state, move), 0))

# # Function to play a game of chess using Q-learning
# def play_game(q_table):
#     global board
#     board = chess.Board()
#     while not board.is_game_over():
#         move = choose_action(board, q_table)
#         board.push(move)
#         reward = 0
#         if board.is_checkmate():
#             reward = 1
#         elif board.is_stalemate():
#             reward = 0.5
#         update_q_table(board, move, reward, q_table)
#     return reward

# # Train the agent using Q-learning
# for i in range(1000):
#     reward = play_game(q_table)
#     print(f"Game {i+1}, Reward: {reward}")

# # Play a game using the trained agent
# board = chess.Board()
# while not board.is_game_over():
#     move = choose_action(board, q_table)
#     board.push(move)
#     print(board)

import gym
import numpy as np

# Create environment
env = gym.make("FrozenLake-v1", is_slippery=False)  # 4x4 grid

# Initialize Q-table
q_table = np.zeros((env.observation_space.n, env.action_space.n))

# Hyperparameters
alpha = 0.1      # learning rate
gamma = 0.99     # discount factor
epsilon = 0.1    # exploration rate
episodes = 10

# Training loop
for ep in range(episodes):
    state = env.reset()[0]
    done = False

    while not done:
        if np.random.rand() < epsilon:
            action = env.action_space.sample()  # explore
        else:
            action = np.argmax(q_table[state])  # exploit

        next_state, reward, done, _, _ = env.step(action)

        # Q-learning update
        q_table[state, action] = q_table[state, action] + alpha * (
            reward + gamma * np.max(q_table[next_state]) - q_table[state, action]
        )

        state = next_state

# Test the trained agent
state = env.reset()[0]
env.render()

done = False
while not done:
    action = np.argmax(q_table[state])
    state, _, done, _, _ = env.step(action)
    env.render()
