import gym
from gym import spaces
from gym.utils import seeding

import numpy as numpy
import os
import logging
import json

class PokeEnv(gym.Env):

    metadata = ({"render.modes": ["human"]})
    ACTIONS = ["Move1", "Move2", "Move3", "Move4",
                "Mega-Move1", "Mega-Move2", "Mega-Move3", "Mega-Move4",
                "Z-Move1", "Z-Move2", "Z-Move3", "Z-Move4",
                "Switch1", "Switch2", "Switch3", "Switch4", "Switch5"]

    def __init__(self):
        """
        """
        logging.info("---Soft-Boiled v0.0.1---")
        self.current_step = -1

        self.action_space = spaces.Discrete(len(ACTIONS)) # Number of possible actions.
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

        remaining_steps = 0
        return
    
    def reset(self):
        """
        """
        # TODO: Make it start a new battle.

    def seed(self, seed):
        """
        """
        # TODO MAYBEEeeeeeeeeEE

    def act(self, move):
        """
        """
        return
    
    def get_state(self):
        """
        """
        # TODO

    def render(self, mode="human", close=False):
        """
        """
        return

