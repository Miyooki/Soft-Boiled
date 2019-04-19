import gym
from gym import spaces
from gym.utils import seeding

import numpy as numpy
import os
import logging
import json

class PokeEnv(gym.Env):

    metadata = ({"render.modes": ["human"]})

    def __init__(self):
        """
        """
        logging.info("---Soft-Boiled v0.0.1---")
        action_space = self.get_action_state()
        self.current_step = -1

        self.action_space = spaces.Discrete() # Number of possible actions.
        self.observation_space = spaces.Dict({
            "self_health":spaces.Box([0.0], [100.0], )
        })


        self.current_episode = -1

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

        self.current_step += 1
        self.

        self.act(action)
        remaining_steps = 0
        reward = self.reward
        ob = self.env.getState()
        info = {}
        return (ob, reward, done, info)
    
    def reset(self):
        """
        """
        # TODO: Make it start a new battle.

    def seed(self, seed):
        """
        """
        self.seed = seeding.np_random(seed)
        return [seed]

    def act(self, move):
        """
        """
        return
    
    def get_reward(self):
        """
        """
        # TODO
        
    def get_state(self):
        """
        """
        # TODO

    def get_action_state(self, request):
        """
        """
        action_space = []

        action_space.append()

    def render(self, mode="human", close=False):
        """
        """
        return

