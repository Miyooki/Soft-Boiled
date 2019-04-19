import gym
import numpy as np
import tensorflow as tf

n_steps = 100000
epsilon = 0.1 # 10% chance to make a random move.

def act(ob):

    if np.random.random_sample() < epsilon:
        return env.action_space.sample()

    else:

        return np.random.choice


ob = env.reset()
rewards = []
reward = 0.0

for step in range(n_steps):
    action = act(ob)
    
    ob_next, r, done, _ = env.step(action)
    update_Q(ob, r, action, ob_next, done)
    reward += r
    if done:
        rewards.append(reward)
        reward = 0.0
        ob = env.reset()
    
    else:
        ob = ob_next

        