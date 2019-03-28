import gym
from gym import spaces
from gym.utils import seeding

import numpy as numpy
import os
import logging
import json

class PokeEnv(gym.Env):

    metadata = ("render.modes": ["human"])

    ACTION = [""]
    def __init__(self):
        """
        """
        self.action_space = spaces.Discrete()
        self.observation_space = spaces.Discrete()

        self.seed()
        self.reset()

    def step(self, action):
        """
        """
        TODO
        """
        self._take_action(action)
        self.status = self.env.step()
        reward = self._get_reward()
        ob = self.env.getState()
        episode_over = self.status != hfo_py.IN_GAME
        return ob, reward, episode_over, {}
        """
        return
    
    def reset(self):
        """
        """
        TODO

    def render(self, mode="human", close=False):
        """
        """
        TODO

